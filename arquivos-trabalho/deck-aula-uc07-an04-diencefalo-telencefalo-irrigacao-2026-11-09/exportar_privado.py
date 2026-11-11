from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import json,hashlib,zipfile
from datetime import datetime,timezone
from nebli.decks import Anki,escrita
from nebli.rotulos import canonical
from nebli.preflight import deck_query
root=Path('/Users/davisousa/NEBLI');r=root/'arquivos-trabalho/deck-aula-uc07-an04-diencefalo-telencefalo-irrigacao-2026-11-09';out=Path('/Users/davisousa/NEBLI-privado/pacotes/2026-11-11-an04/NEBLI - UC07.apkg');assert not out.exists();out.parent.mkdir(parents=True,exist_ok=True);A=Anki()
with escrita(A,'UC07: pacote pessoal AN04, sem publicação',sync=False):
 deck=next(d for d in A('deckNames') if canonical(d)=='NEBLI::UC07');ids=A('findCards',query=deck_query(deck));before=A('cardsInfo',cards=ids)
 assert A('exportPackage',deck=deck,path=str(out),includeSched=True) and out.is_file()
 after=A('cardsInfo',cards=ids);sig=lambda cs:{c['cardId']:(c['note'],c['flags'],c['queue'],c['due'],c['reps'],c['lapses']) for c in cs}
 assert sig(before)==sig(after),'Coleção mudou durante exportação; investigar antes de certificar pacote.'
with zipfile.ZipFile(out) as z:assert z.testzip() is None;names=z.namelist()
receipt={'at':datetime.now(timezone.utc).isoformat(),'arquivo':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'cards_uc':len(ids),'uso':'Pessoal, contémKenhub; não publicado nem enviado aoDrive','preserva_flags_e_agendamento':True,'colecao_inalterada_na_exportacao':True,'arquivo_zip_integro':True,'teste_importacao':'não realizado; deckjá instalado na coleção viva','componentes_anki':[n for n in names if n.startswith('collection.') or n=='media']}
(r/'pacote-uc07-privado.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=1));print(json.dumps(receipt,ensure_ascii=False))
