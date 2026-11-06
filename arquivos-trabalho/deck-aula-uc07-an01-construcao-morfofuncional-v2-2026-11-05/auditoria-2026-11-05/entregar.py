from pathlib import Path
import sys,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parent.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita,em_tela
A=Anki();out=Path.home()/'NEBLI-privado/pacotes/2026-11-06/NEBLI - UC07.apkg';out.parent.mkdir(parents=True,exist_ok=True)
if out.exists():raise RuntimeError('Pacote já existe; conferir recibo antes de sobrescrever')
with escrita(A,'UC07 AN01 entrega privada',sync=False):
 ok=A('exportPackage',deck='NEBLI::UC07',path=str(out),includeSched=True,includeMedia=True)
 if not ok or not out.exists():raise RuntimeError('Exportação não concluída')
rec={'pacote':str(out),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'sync_concluido':False,'at':datetime.now(timezone.utc).isoformat()}
(R/'auditoria-2026-11-05/entrega-final.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2));print(json.dumps(rec,ensure_ascii=False))
