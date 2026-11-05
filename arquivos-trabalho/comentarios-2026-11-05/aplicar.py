"""Aplica só conteúdo, sem dar pedidos por concluídos; marcadores após render vivo."""
import json,re,sys,sqlite3,time
from pathlib import Path
from datetime import datetime,timezone
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki,escrita,em_tela
from nebli.rotulos import canonical
A=Anki();P=json.load(open(C/'propostas.json'));N={n['noteId']:n for n in json.load(open(C/'notas-antes-com-similares.json'))};B=C/'backup';B.mkdir(exist_ok=True)
def save(name,data):(C/name).write_text(json.dumps(data,ensure_ascii=False,indent=1))
def tela():
 for i in range(20):
  try:return em_tela(A)
  except RuntimeError as e:
   if 'collection operation'in str(e).lower():time.sleep(.5)
   else:raise
 raise RuntimeError('Não foi possível verificar tela')
# Backup consistente por API SQLite de cópia, somente leitura na origem.
source=Path.home()/'Library/Application Support/Anki2/User 1/collection.anki2'
if not(B/'collection.anki2').exists():
 with sqlite3.connect('file:'+str(source)+'?mode=ro',uri=True)as src,sqlite3.connect(B/'collection.anki2')as dst:src.backup(dst)
ids=list(map(int,P));live=A('notesInfo',notes=ids);save('backup/notas.json',live);cids=[c for n in live for c in n['cards']];before=A('cardsInfo',cards=cids);save('backup/cards.json',before)
record={'inicio':datetime.now(timezone.utc).isoformat(),'aplicados':[],'protegidos':[],'divergencias':[]}
with escrita(A,'comentários05/11:conteúdo e9similares',sync=False):
 for nid,p in P.items():
  nid=int(nid)
  if nid in tela():record['protegidos'].append(nid);continue
  current=A('notesInfo',notes=[nid])[0];old=N[nid]
  bad=[k for k in p['fields'] if current['fields'][k]['value']!=old['fields'][k]['value']]
  if bad:record['divergencias'].append({'nid':nid,'campos':bad});continue
  if p['fields']:A('updateNoteFields',note={'id':nid,'fields':p['fields']})
  reread=A('notesInfo',notes=[nid])[0]
  assert all(reread['fields'][k]['value']==v for k,v in p['fields'].items()),nid
  if p.get('suspender'):
   A('suspend',cards=current['cards']);A('addTags',notes=[nid],tags='NEBLI::retirado::step2-only')
  record['aplicados'].append(nid);save('aplicacao-conteudo.json',record)
 if not(C/'novo-scid-recibo.json').exists():
  new=json.load(open(C/'novo-scid.json'));original=A('notesInfo',notes=[1791625424233])[0];cards=A('cardsInfo',cards=original['cards']);d=canonical(cards[0]['deckName']);tags=[t for t in original['tags'] if t.startswith('NEBLI::2026-') or t.startswith('NEBLI::objetivo')]
  tags+=['NEBLI::origem::Autoral','NEBLI::author::scid-mecanismos-20261105','NEBLI::run::comentarios-20261105']
  nid=A('addNote',note={'deckName':d,'modelName':original['modelName'],'fields':new['fields'],'tags':tags,'options':{'allowDuplicate':False}})
  cs=A('notesInfo',notes=[nid])[0]['cards']
  for cid in cs:A('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[4],warning_check=True)
  save('novo-scid-recibo.json',{'nid':nid,'cards':cs,'deck':d,'fields':new['fields'],'flag':4})
# Agenda/flags não são tocados; apenas a suspensão curricular expressamente pedida é exceção.
after=A('cardsInfo',cards=cids);save('cards-depois.json',after);by={c['cardId']:c for c in before};problems=[]
for c in after:
 for k in ['reps','lapses','factor','due','interval','left','type','flags','queue']:
  if c[k]!=by[c['cardId']][k] and not(c['note']==1793803589750 and k=='queue'and c[k]==-1):problems.append({'cid':c['cardId'],'campo':k,'antes':by[c['cardId']][k],'depois':c[k]})
record['integridade_agenda']=problems;record['fim']=datetime.now(timezone.utc).isoformat();save('aplicacao-conteudo.json',record);print(json.dumps({k:len(v)if isinstance(v,list)else v for k,v in record.items()},ensure_ascii=False))
