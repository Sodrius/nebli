import json,sys,hashlib,collections
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
from nebli.rotulos import canonical
A=Anki();out={};union=set();problems=[]
def values(n):return {k:v['value'] for k,v in n['fields'].items()}
def h(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
for folder in ['complemento','inflamacao']:
 p=R/folder;plan=json.loads((p/'plan.json').read_text());receipt=json.loads((p/'receipt.json').read_text());before=json.loads((p/'before.json').read_text());nids=[n['nid'] for n in receipt['notes']];notes={n['noteId']:n for n in A('notesInfo',notes=nids)}
 for e,r in zip(plan['entries'],receipt['notes']):
  n=notes[r['nid']]
  if values(n)!=e['fields']:problems.append((folder,r['key'],'fields diverged'))
  if set(n['cards'])!=set(map(int,r['cards'])):problems.append((folder,r['key'],'siblings diverged'))
  if n['fields']['NEBLI_Comentario']['value'] or n['fields']['ankihub_id']['value']:problems.append((folder,r['key'],'personal field/ankihub'))
  e['fields_hash']=h(e['fields'])
 # Original sources stayed unchanged. Shared notes may have user edits after delivery; report, do not revert.
 changed_sources=[]
 for n in A('notesInfo',notes=list(map(int,before['sources']))):
  b=before['sources'][str(n['noteId'])]
  if values(n)!=values(b) or set(n['tags'])!=set(b['tags']):changed_sources.append(n['noteId'])
 if changed_sources:problems.append((folder,'original sources changed',changed_sources))
 cids=[int(cid) for n in receipt['notes'] for cid in n['cards']];cards=A('cardsInfo',cards=cids);allcards=A('cardsInfo',cards=receipt['exact_card_ids']);union.update(receipt['exact_card_ids'])
 (p/'rendered-cards-final.json').write_text(json.dumps(cards,ensure_ascii=False,indent=1))
 effective=h(plan['entries']);plan['effective_selection_hash']=effective;(p/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1))
 origin=collections.Counter(next(t.split('::')[-1] for t in notes[c['note']]['tags'] if t.startswith('NEBLI::origem::')) for c in cards)
 out[folder]={'notes':len(notes),'cards':len(cards),'origins':dict(origin),'flags':dict(collections.Counter(c['flags'] for c in cards)),'new':sum(c['type']==0 for c in cards),'reviewed':sum(c['reps']>0 for c in cards),'suspended':sum(c['queue']==-1 for c in cards),'associated_notes':len(receipt['shared']),'associated_cards':len(allcards)-len(cards),'logical_cards':len(allcards),'effective_selection_hash':effective}
 (p/'verification-final.json').write_text(json.dumps({'problems':problems,'fields_checked':len(notes),'sources_checked':len(before['sources']),'card_ids_verified':set(A('findCards',query=receipt['query']))==set(receipt['exact_card_ids']),'effective_selection_hash':effective},ensure_ascii=False,indent=1))
cs=A('cardsInfo',cards=sorted(union));out['union']={'cards':len(cs),'notes':len(set(c['note'] for c in cs)),'new':sum(c['type']==0 for c in cs),'reviewed':sum(c['reps']>0 for c in cs),'suspended':sum(c['queue']==-1 for c in cs),'flags':dict(collections.Counter(c['flags'] for c in cs))};out['problems']=problems
(R/'contagens-exatas.json').write_text(json.dumps(out,ensure_ascii=False,indent=1));print(out);assert not problems
