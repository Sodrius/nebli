"""Fechamento único autorizado: aguarda revisão terminar, reposiciona novos e sincroniza."""
from pathlib import Path
import sys,time,json,subprocess
from datetime import datetime,timezone
R=Path(__file__).resolve().parent.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita,em_tela,SYNC_PENDENTE
A=Anki();D=R/'auditoria-2026-11-05';SYNC_PENDENTE.write_text(datetime.now(timezone.utc).isoformat())
for attempt in range(720):
 try:
  busy=bool(em_tela(A))
 except RuntimeError:
  time.sleep(5);continue
 if busy:
  if attempt%12==0:print('Aguardando fim da revisão para ordem/sync',flush=True)
  time.sleep(5);continue
 try:
  if not(D/'reposicao-nativa.json').exists():
   subprocess.run([sys.executable,str(D/'reposicionar.py')],check=True,capture_output=True,text=True)
  with escrita(A,'UC07 AN01 sincronização após revisão',sync=True):
   if em_tela(A):raise RuntimeError('Revisão retomada; aguardar')
  if SYNC_PENDENTE.exists():continue
  p=D/'entrega-final.json';d=json.loads(p.read_text());d.update(sync_concluido=True,sync_em=datetime.now(timezone.utc).isoformat());p.write_text(json.dumps(d,ensure_ascii=False,indent=2));print('ORDEM E SYNC CONCLUÍDOS',flush=True);break
 except (RuntimeError,subprocess.CalledProcessError)as exc:
  print(str(exc),flush=True);time.sleep(5)
else:print('Anki permaneceu ocupado; fechamento registrado como pendente',flush=True)
