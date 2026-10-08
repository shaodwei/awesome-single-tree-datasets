"""Read-only snapshot; never open a live worker's replaceable status/lock."""
import argparse,collections,csv,io,json,os,pathlib,subprocess

def pid_alive(pid):
    if os.name=='nt':
        r=subprocess.run(['tasklist','/FI',f'PID eq {int(pid)}','/FO','CSV','/NH'],capture_output=True,text=True,check=False)
        return any(len(row)>1 and row[1]==str(pid) for row in csv.reader(io.StringIO(r.stdout))) if r.returncode==0 else None
    try:os.kill(int(pid),0);return True
    except ProcessLookupError:return False
    except PermissionError:return None

def snapshot(root):
    root=pathlib.Path(root);verified={}
    catalog=pathlib.Path(__file__).resolve().parents[1]/'catalog/datasets.json'
    allowed={d['dataset_id'] for d in json.loads(catalog.read_text(encoding='utf-8'))}
    for name in ['IMPORT_MANIFEST.jsonl','MANIFEST.jsonl']:
        p=root/name
        if not p.exists():continue
        for line in p.read_text(encoding='utf-8').splitlines():
            try:r=json.loads(line)
            except json.JSONDecodeError:continue # Writer may be appending its final line.
            if r.get('status','').startswith('verified') and r.get('dataset_id') in allowed and (root/'raw'/r['relative_path']).is_file():
                verified[r['relative_path']]=r
    active=None;failures=[]
    for p in sorted((root/'runs').glob('*/identity.json'),reverse=True):
        if (p.parent/'summary.json').exists():continue
        r=json.loads(p.read_text(encoding='utf-8')) # Immutable owner receipt.
        if pid_alive(r['pid']):active=r;break
    if active and active.get('stdout_log'):
        log=root/active['stdout_log']
        if log.is_file():
            for line in log.read_text(encoding='utf-8').splitlines():
                try:event=json.loads(line)
                except json.JSONDecodeError:continue
                if event.get('event')=='result' and event.get('status')=='failed':failures.append(dict(file=event['file'],error=event.get('error','')))
    copy_only=[r for r in verified.values() if r.get('checksum_basis','').startswith('verified legacy')]
    return dict(verified_release_files=len(verified),verified_bytes=sum(r['size'] for r in verified.values()),official_checksum_verified_files=len(verified)-len(copy_only),legacy_copy_integrity_only_files=len(copy_only),files_by_dataset=dict(collections.Counter(r['dataset_id'] for r in verified.values())),active_run=active,current_batch_failures=failures,guard_present=(root/'staging/.downloader.lock').exists(),note='Release files are not biological tree counts. Live replaceable status/lock files are never opened. Failures are read from append-only stdout when a log is registered.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',required=True);a=p.parse_args();print(json.dumps(snapshot(a.root),ensure_ascii=False,indent=2))
