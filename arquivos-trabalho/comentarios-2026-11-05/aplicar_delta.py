import json,sys,re,base64
from pathlib import Path
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki,escrita,em_tela
A=Anki();D=json.load(open(C/'delta-visual.json'));receipt=[]
with escrita(A,'comentários05/11:delta após revisão visual independente',sync=False):
 sources={name for d in D for v in d['fields'].values()for name in re.findall(r'(?:src|srcset)="([^"]+)"',v)}
 for name in sources:
  p=C/'img'/name
  if p.exists():assert A('storeMediaFile',filename=name,data=base64.b64encode(p.read_bytes()).decode())==name
 for d in D:
  nid=d['nid']
  if nid in em_tela(A):raise RuntimeError('Nota em tela, aguardar: '+str(nid))
  n=A('notesInfo',notes=[nid])[0];assert all(n['fields'][k]['value']==v for k,v in d['antes'].items()),nid
  A('updateNoteFields',note={'id':nid,'fields':d['fields']});n=A('notesInfo',notes=[nid])[0];assert all(n['fields'][k]['value']==v for k,v in d['fields'].items()),nid
  receipt.append(nid)
 if not(C/'novo-scid-recibo.json').exists():
  new=json.load(open(C/'novo-scid.json'));model=A('notesInfo',notes=[1791625424233])[0]['modelName'];tags=['NEBLI::2026-uc03-imunologia-51-disturbios-sistema-imune','NEBLI::origem::Autoral','NEBLI::author::scid-mecanismos-20261105','NEBLI::run::comentarios-20261105'];deck='NEBLI::UC03::P3::Imunologia::Distúrbios do sistema imune'
  nid=A('addNote',note={'deckName':deck,'modelName':model,'fields':new['fields'],'tags':tags,'options':{'allowDuplicate':False}});cs=A('notesInfo',notes=[nid])[0]['cards']
  for cid in cs:A('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[4],warning_check=True)
  (C/'novo-scid-recibo.json').write_text(json.dumps({'nid':nid,'cards':cs,'deck':deck,'fields':new['fields'],'flag':4},ensure_ascii=False,indent=1))
(C/'delta-visual-recibo.json').write_text(json.dumps(receipt));print('delta',len(receipt),'e novoorganizadorSCID instalado')
