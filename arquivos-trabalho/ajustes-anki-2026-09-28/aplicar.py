"""Aplica só plan.json, com backup SQLite consistente, lock, precondições e recibo."""
import hashlib, json, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parents[1]))
from nebli.decks import Anki, escrita
from nebli.preflight import chunks, deck_query
from nebli.rotulos import canonical

A=Anki(); P=json.loads((BASE/'plan.json').read_text()); S=json.loads((BASE/'snapshot.json').read_text())
NS={n['noteId']:n for n in S['notes']}
SC={c['cardId']:c for c in S['cards']}
assert A('getActiveProfile')==S['profile']=='User 1'
def save(name,value):
 (BASE/name).write_text(json.dumps(value,ensure_ascii=False,indent=1))
def getcards(ids):
 return {c['cardId']:c for batch in chunks(sorted(ids),100) for c in A('cardsInfo',cards=batch)}
def model(name):
 return {'fields':A('modelFieldNames',modelName=name), 'templates':A('modelTemplates',modelName=name), 'styling':A('modelStyling',modelName=name)}
def preflight():
 roots=[d for d in A('deckNames') if canonical(d)=='NEBLI'];assert len(roots)==1
 assert set(A('findCards',query=deck_query(roots[0])))==set(SC),'A coleção mudou: refazer o plano.'
 for m in P['models']:
  assert model(m['name'])==m['before'], ('Modelo editado após snapshot',m['name'])
  expected={n['noteId'] for n in S['notes'] if n['modelName']==m['name']}
  assert set(A('findNotes',query='note:"'+m['name']+'"'))==expected, ('Modelo compartilhado fora do escopo',m['name'])
 for n in P['notes']:
  live=A('notesInfo',notes=[n['noteId']])[0]
  assert live['fields']==NS[n['noteId']]['fields'], ('Nota editada após snapshot',n['noteId'])
  assert live['tags']==NS[n['noteId']]['tags'], ('Tags mudaram',n['noteId'])
 for batch in chunks([r['cardId'] for r in P['flags']],100):
  for cid,c in getcards(batch).items():
   expected=next(r for r in P['flags'] if r['cardId']==cid)
   assert c['flags']&7==expected['before'], ('Bandeira mudou desde snapshot',cid)
 return roots[0]

root=preflight()
if '--check' in sys.argv:
 print(json.dumps({'preflight':'ok','notes':len(P['notes']),'models':len(P['models']),'flags':len(P['flags'])}));sys.exit(0)
if (BASE/'recibo.json').exists():
 previous=json.loads((BASE/'recibo.json').read_text())
 assert previous['status']=='iniciado' and not any(previous[k] for k in ('notes','models','flags')), 'Já houve escrita: não reaplicar automaticamente.'
record={'started':datetime.now(timezone.utc).isoformat(),'plan_sha256':hashlib.sha256((BASE/'plan.json').read_bytes()).hexdigest(),
        'status':'iniciado','notes':[],'models':[],'flags':[]}
save('recibo.json',record)
with escrita(A,'Ajustes finos: comentários, imagens, MCAT e bandeiras incrementais 28/09'):
 preflight()
 source=Path('/Users/davisousa/Library/Application Support/Anki2/User 1/collection.anki2')
 backup=BASE/'collection-before.anki2'
 with sqlite3.connect(source.as_uri()+'?mode=ro',uri=True) as src, sqlite3.connect(backup) as dst:
  src.backup(dst)
  dst.create_collation('unicase',lambda a,b:(a.casefold()>b.casefold())-(a.casefold()<b.casefold()))
  assert dst.execute('PRAGMA quick_check').fetchone()[0]=='ok'
 record['backup']=str(backup);save('recibo.json',record)
 before=getcards(SC)
 save('cards-before-compact.json',[{k:v for k,v in c.items() if k not in ('question','answer','css','fields')} for c in before.values()])
 for m in P['models']:
  if m['before']['styling']!=m['after']['styling']:
   A('updateModelStyling',model={'name':m['name'],'css':m['after']['styling']['css']})
  if m['before']['templates']!=m['after']['templates']:
   A('updateModelTemplates',model={'name':m['name'],'templates':m['after']['templates']})
  assert model(m['name'])==m['after']
  record['models'].append(m['name']);save('recibo.json',record)
 for n in P['notes']:
  A('updateNoteFields',note={'id':n['noteId'],'fields':n['after']})
  live=A('notesInfo',notes=[n['noteId']])[0]
  assert all(live['fields'][k]['value']==v for k,v in n['after'].items())
  assert set(live['cards'])==set(NS[n['noteId']]['cards'])
  record['notes'].append(n['noteId']);save('recibo.json',record)
 for r in P['flags']:
  current=getcards([r['cardId']])[r['cardId']]
  assert current['flags']&7==r['before'], ('Flag mudou durante execução',r['cardId'])
  result=A('setSpecificValueOfCard',card=r['cardId'],keys=['flags'],newValues=[(current['flags']&~7)|r['after']])
  assert result==[True],result
  record['flags'].append(r['cardId'])
 save('recibo.json',record)
 after=getcards(SC)
 invariant=['note','ord','type','queue','due','interval','reps','lapses','left','factor']
 differences=[{'cardId':cid,'fields':[k for k in invariant if before[cid][k]!=after[cid][k]]} for cid in before if any(before[cid][k]!=after[cid][k] for k in invariant)]
 assert not differences, differences
 for r in P['flags']:assert after[r['cardId']]['flags']&7==r['after']
 for cid in set(SC)-{r['cardId'] for r in P['flags']}:assert after[cid]['flags']==before[cid]['flags']
 roots=[d for d in A('deckNames') if canonical(d)=='NEBLI'];assert len(roots)==1
 assert set(A('findCards',query=deck_query(roots[0])))==set(SC)
 save('cards-after.json',list(after.values()))
 record.update(status='conferido',scheduler_preserved=True,card_ids_preserved=True,finished=datetime.now(timezone.utc).isoformat())
 save('recibo.json',record)
record['sync']='AnkiWeb solicitado e retornou sem erro; aparelhos não conferidos'
save('recibo.json',record)
print(json.dumps({k:v for k,v in record.items() if k not in ('notes','flags')},ensure_ascii=False))
print('Notas:',len(record['notes']),'Bandeiras:',len(record['flags']))
