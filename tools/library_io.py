"""Verified, restartable downloads. Raw sources are never edited or removed."""
import argparse, concurrent.futures, hashlib, json, os, pathlib, shutil, time
import urllib.error, urllib.request, re, subprocess, http.client, ssl, threading, datetime, stat, signal

STOP=threading.Event()
LEASE_LOCK=threading.Lock()
AGENTHUB_SCRIPT=str(pathlib.Path.home()/'AgentHub/bin/agenthub.ps1')
class ChecksumError(ValueError): pass

def ensure_ownership(root):
    lock=root/'.agent/LOCK'
    if not lock.exists():raise PermissionError('AgentHub archive lock is required')
    with LEASE_LOCK:
        d=json.loads(lock.read_text(encoding='utf-8-sig'))
        expires=datetime.datetime.fromisoformat(d['expires_at'])
        now=datetime.datetime.now(datetime.timezone.utc)
        if d['owner']!='codex' or expires<=now:raise PermissionError('No active Codex archive lock')
        if expires-now<datetime.timedelta(hours=3):
            subprocess.run(['pwsh','-NoProfile','-File',AGENTHUB_SCRIPT,'lock',str(root),'-Owner','codex','-Task','single tree download worker','-Hours','48'],check=True)

def atomic_json(path,data):
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');tmp.replace(path)

def digest(path, algorithms=('sha256',)):
    hashes={a:hashlib.new(a) for a in algorithms}
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(8*1024*1024),b''):
            for h in hashes.values(): h.update(chunk)
    return {a:h.hexdigest() for a,h in hashes.items()}

def contained(root, relative):
    root=pathlib.Path(root).resolve()
    rel=pathlib.PurePosixPath(relative.replace('\\','/'))
    reserved={'CON','PRN','AUX','NUL',*[f'COM{i}' for i in range(1,10)],*[f'LPT{i}' for i in range(1,10)]}
    if rel.is_absolute() or '..' in rel.parts or ':' in str(rel): raise ValueError('Unsafe relative path')
    if any(x.endswith((' ','.')) or x.split('.')[0].upper() in reserved for x in rel.parts):raise ValueError('Reserved path component')
    p=(root/pathlib.Path(*rel.parts)).resolve()
    if not p.is_relative_to(root): raise ValueError('Path outside destination')
    return p

def verify(p, item):
    if p.stat().st_size!=item['size']: raise ValueError('size mismatch')
    algo,expected=item['checksum'].split(':',1)
    h=digest(p,tuple(dict.fromkeys([algo,'sha256'])))
    if h[algo].lower()!=expected.lower(): raise ChecksumError('published checksum mismatch')
    return h['sha256']

def download_one(item,root,reserve):
    if STOP.is_set():raise InterruptedError('cancelled')
    final=contained(root/'raw',item['relative_path'])
    part=contained(root/'staging',item['relative_path']+'.part')
    final.parent.mkdir(parents=True,exist_ok=True);part.parent.mkdir(parents=True,exist_ok=True)
    if final.exists():
        return dict(item,status='verified_existing',sha256=verify(final,item),path=str(final))
    remaining=item['size']-(part.stat().st_size if part.exists() else 0)
    if shutil.disk_usage(root).free<reserve+max(0,remaining): raise OSError('Storage reserve would be crossed')
    meta_path=part.with_suffix('.part.meta.json')
    for attempt in range(3):
        try:
            offset=part.stat().st_size if part.exists() else 0
            if offset>item['size']: raise ValueError('partial file exceeds declared size; preserved')
            if offset<item['size']:
                headers={'User-Agent':'awesome-single-tree-datasets/0.1 research-download','Accept-Encoding':'identity'}
                if offset: headers['Range']=f'bytes={offset}-'
                previous=json.loads(meta_path.read_text(encoding='utf-8')) if meta_path.exists() else {}
                if offset and previous.get('validator'):headers['If-Range']=previous['validator']
                with urllib.request.urlopen(urllib.request.Request(item['url'],headers=headers),timeout=60) as r:
                    ctype=r.headers.get('Content-Type','').lower()
                    if 'text/html' in ctype: raise ValueError('Unexpected HTML instead of data')
                    if r.headers.get('Content-Encoding','identity').lower() not in ('','identity'):raise ValueError('Encoded response cannot be resumed safely')
                    validator=r.headers.get('ETag') or r.headers.get('Last-Modified')
                    if offset and r.status==206:
                        match=re.fullmatch(r'bytes (\d+)-(\d+)/(\d+)',r.headers.get('Content-Range',''))
                        if not match or int(match[1])!=offset or int(match[2])!=item['size']-1 or int(match[3])!=item['size']: raise ValueError('Bad Content-Range')
                        if previous.get('validator') and validator and previous['validator']!=validator:raise ChecksumError('Source validator changed during resume')
                        mode='ab'
                    elif r.status==200:
                        # Server ignored Range: restart this partial only, never append a full response.
                        mode='wb';offset=0
                    else: raise ValueError(f'Unexpected HTTP status {r.status}')
                    if r.headers.get('Content-Length') and int(r.headers['Content-Length'])!=item['size']-offset:raise ValueError('Content-Length mismatch')
                    atomic_json(meta_path,{'validator':validator,'url':item['url'],'checksum':item['checksum']})
                    last=time.monotonic()
                    with part.open(mode) as f:
                        total=offset
                        while True:
                            if STOP.is_set():raise InterruptedError('cancelled')
                            b=r.read(4*1024*1024)
                            if not b: break
                            total+=len(b)
                            if total>item['size']: raise ValueError('response exceeds expected size')
                            f.write(b)
                            if time.monotonic()-last>30:
                                ensure_ownership(root)
                                if shutil.disk_usage(root).free<reserve: raise OSError('Storage reserve reached')
                                print(json.dumps({'event':'progress','file':item['relative_path'],'bytes':total,'size':item['size']}),flush=True);last=time.monotonic()
                        f.flush();os.fsync(f.fileno())
                    if total!=item['size']:raise ConnectionError('short read')
            sha=verify(part,item)
            if final.exists(): raise FileExistsError('Destination appeared during download; preserved')
            if os.name=='nt':part.rename(final)
            else:os.link(part,final);part.unlink()
            os.chmod(final,stat.S_IREAD)
            print(json.dumps({'event':'verified','file':item['relative_path'],'bytes':item['size']}),flush=True)
            return dict(item,status='verified_download',sha256=sha,path=str(final))
        except ChecksumError:
            if part.exists():
                bad=contained(root/'staging/quarantine',item['relative_path']+'.'+str(time.time_ns())+'.bad')
                bad.parent.mkdir(parents=True,exist_ok=True);part.rename(bad)
                if meta_path.exists():meta_path.rename(bad.with_suffix('.meta.json'))
            raise
        except (urllib.error.URLError,TimeoutError,ConnectionError,http.client.HTTPException,ssl.SSLError) as e:
            if attempt==2: raise
            print(json.dumps({'event':'retry','file':item['relative_path'],'attempt':attempt+1,'error':str(e)}),flush=True)
            time.sleep(3*(attempt+1))

def run(queue_path,root,phase,workers,reserve_gib,budget_gib,release_lock):
    root=pathlib.Path(root).resolve();ensure_ownership(root)
    q=json.loads(pathlib.Path(queue_path).read_text(encoding='utf-8'))
    items=[x for x in q if x['phase'] in phase.split(',')]
    if len({str(contained(root/'raw',x['relative_path'])).casefold() for x in items})!=len(items): raise ValueError('Duplicate destination in queue')
    total=sum(x['size'] for x in items)
    if total>budget_gib*1024**3: raise ValueError('Download batch exceeds budget')
    # All workers' potential writes are reserved before any transfer starts.
    required=sum(x['size'] for x in items if not contained(root/'raw',x['relative_path']).exists())
    if shutil.disk_usage(root).free<reserve_gib*1024**3+required: raise OSError('Insufficient space for batch + reserve')
    run_id=time.strftime('RUN-%Y%m%d-%H%M%S-download')
    guard=root/'staging/.downloader.lock';guard.parent.mkdir(parents=True,exist_ok=True)
    fd=os.open(guard,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    with os.fdopen(fd,'w') as f:json.dump({'pid':os.getpid(),'run_id':run_id,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},f)
    dest=root/'runs'/run_id
    results=[]
    try:
        dest.mkdir(parents=True,exist_ok=False)
        atomic_json(dest/'identity.json',{'pid':os.getpid(),'run_id':run_id,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
        print(json.dumps({'event':'start','run_id':run_id,'phase':phase,'files':len(items),'bytes':total}),flush=True)
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            futs={ex.submit(download_one,i,root,reserve_gib*1024**3):i for i in items}
            for fut in concurrent.futures.as_completed(futs):
                try: result=fut.result()
                except Exception as e: result=dict(futs[fut],status='failed',error=str(e))
                results.append(result)
                atomic_json(dest/'status.json',results)
                if result['status'].startswith('verified'):
                    with (root/'MANIFEST.jsonl').open('a',encoding='utf-8') as ledger:ledger.write(json.dumps(dict(result,run_id=run_id,verified_at=datetime.datetime.now(datetime.timezone.utc).isoformat()),ensure_ascii=False)+'\n')
                print(json.dumps({'event':'result','file':result['relative_path'],'status':result['status'],'error':result.get('error','')}),flush=True)
        summary={'run_id':run_id,'status':'completed' if all(x['status'].startswith('verified') for x in results) else 'completed_with_failures','files':len(results),'verified':sum(x['status'].startswith('verified') for x in results),'bytes_verified':sum(x['size'] for x in results if x['status'].startswith('verified'))}
        atomic_json(dest/'summary.json',summary)
        print(json.dumps(summary),flush=True)
        return summary
    finally:
        guard.unlink()
        if release_lock:
            released=subprocess.run(['pwsh','-NoProfile','-File',AGENTHUB_SCRIPT,'unlock',str(root),'-Owner','codex'],check=False)
            atomic_json(dest/'lock_release.json',{'returncode':released.returncode})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--queue',required=True);p.add_argument('--root',required=True);p.add_argument('--phase',default='P0');p.add_argument('--workers',type=int,choices=[1,2],default=2);p.add_argument('--reserve-gib',type=int,default=1024);p.add_argument('--budget-gib',type=int,default=250);p.add_argument('--release-lock',action='store_true')
    a=p.parse_args()
    signal.signal(signal.SIGINT,lambda signum,frame:STOP.set())
    if hasattr(signal,'SIGTERM'):signal.signal(signal.SIGTERM,lambda signum,frame:STOP.set())
    run(a.queue,a.root,a.phase,a.workers,a.reserve_gib,a.budget_gib,a.release_lock)
