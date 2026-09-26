import json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
from apply import LOCK,call,save

with LOCK.open('x',encoding='utf-8') as f:f.write(json.dumps({'executor':'Codex','lesson':'X3 preset and sync','at':datetime.now(timezone.utc).isoformat()}))
try:
    proc=subprocess.run([sys.executable,'-X','utf8','flashcards/scripts/nebli_novos.py','--alinhar'],cwd=Path(__file__).parents[2],capture_output=True,text=True,encoding='utf-8',check=True)
    print(proc.stdout)
    result=call('sync')
    save('sync-after-preset.json',{'result':result,'at':datetime.now(timezone.utc).isoformat()})
finally:LOCK.unlink(missing_ok=True)
