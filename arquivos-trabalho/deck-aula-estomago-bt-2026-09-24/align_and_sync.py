import json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
from apply import call,ROOT,PLAN

lock=ROOT/'ANKI-ESCRITA.lock'
with lock.open('x',encoding='utf-8') as f:f.write(json.dumps(dict(executor='Codex',lesson=PLAN['lesson_id'],action='align-sync',at=datetime.now(timezone.utc).isoformat())))
try:
    assert call('getActiveProfile')==PLAN['profile']
    p=subprocess.run([sys.executable,'-X','utf8','flashcards/scripts/nebli_novos.py','--alinhar'],cwd=ROOT.parent,capture_output=True,text=True,check=True)
    print(p.stdout)
    print('sync:',call('sync'))
finally:lock.unlink(missing_ok=True)
