"""Read-only size/checksum check for files downloaded into manual_inbox.

Does not publish or mutate raw; safe while a background downloader is active.
"""
import argparse,json,pathlib,hashlib
from library_io import contained

def check(queue,root):
    rows=[];known=set();inbox=pathlib.Path(root).resolve()/'manual_inbox'
    for item in json.loads(pathlib.Path(queue).read_text(encoding='utf-8')):
        p=contained(pathlib.Path(root).resolve()/'manual_inbox',item['relative_path'])
        known.add(p)
        if not p.is_file():
            rows.append(dict(file=item['relative_path'],status='not_present'));continue
        if p.stat().st_size!=item['size']:
            rows.append(dict(file=item['relative_path'],status='size_mismatch'));continue
        algorithm,expected=item['checksum'].split(':',1);official=hashlib.new(algorithm);sha=hashlib.sha256()
        with p.open('rb') as f:
            while b:=f.read(8*1024*1024):official.update(b);sha.update(b)
        rows.append(dict(file=item['relative_path'],status='verified_manual_pending_import' if official.hexdigest()==expected.lower() else 'checksum_mismatch',sha256=sha.hexdigest()))
    for p in inbox.rglob('*'):
        if p.is_file() and not p.is_symlink() and p.resolve() not in known:rows.append(dict(file=p.relative_to(inbox).as_posix(),status='no_official_checksum_in_this_queue'))
    return rows

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--queue',required=True);p.add_argument('--root',required=True);a=p.parse_args();print(json.dumps(check(a.queue,a.root),ensure_ascii=False,indent=2))
