import json,sys,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from nebli.decks import Anki,escrita,em_tela
from nebli.delta import same,base_of
from nebli.reconcilia import aplicar_correcoes
R=Path(__file__).resolve().parent.parent;B=Path(__file__).resolve().parent;A=Anki()
p=json.loads((R/'plan.json').read_text());aplicar_correcoes(R,p)
old=json.loads((B/'receipt.json').read_text());rec=json.loads((R/'receipt.json').read_text())
ids={n['key']:n['nid'] for n in old['notes']};ids.update({n['key']:n['nid'] for n in rec['notes']})
statepath=B/'v2-created.json';created=json.loads(statepath.read_text()) if statepath.exists() else {};ids.update(created)
L=p['lesson_id'];short=p['short'];base=base_of(R,short);want={e['key'] for e in p['entries']}
allids=list(ids.values());live={n['noteId']:n for n in A('notesInfo',notes=allids) if n};cids=[c for n in live.values() for c in n['cards']]
backup=B/'v2-before-delete.json'
if not backup.exists():
 reviews=A('getReviewsOfCards',cards=cids)
 backup.write_text(json.dumps({'notes':live,'cards':A('cardsInfo',cards=cids),'reviews':reviews},ensure_ascii=False,indent=1))
pending=[];deleted=[];preserved=[]
with escrita(A,'PT47 reconstrução de princípios e exclusão autorizada',sync=False):
 for k,nid in list(ids.items()):
  if k in want or nid not in live:continue
  if nid in em_tela(A):pending.append(k);continue
  n=A('notesInfo',notes=[nid])[0]
  if any(t.startswith('NEBLI::2026-') and L not in t for t in n['tags']):
   # A nota pertence a outra aula: mantém conteúdo, histórico e cartões dela,
   # mas remove somente sua associação desta aula que acabou de ser excluída.
   stale=[t for t in n['tags'] if t == f'NEBLI::{L}' or t.startswith(f'NEBLI::ordem::{short}-') or t.startswith(f'NEBLI::cor::{L}::') or t.startswith('NEBLI::objetivo::') or t == 'NEBLI::escopo::aula' or t.startswith(f'NEBLI::run::{p["run_id"]}')]
   if stale:A('removeTags',notes=[nid],tags=' '.join(stale))
   preserved.append(k);continue
  # A segunda leitura também elimina cartões que ainda estavam ativos na
  # primeira revisão. Eles vieram do recibo desta aula e foram preservados no
  # backup acima; nunca alcançar notas de outra aula.
  assert f'NEBLI::{L}' in n['tags'],k
  A('deleteNotes',notes=[nid]);assert not A('findNotes',query=f'nid:{nid}');deleted.append(k)
 for e in p['entries']:
  k=e['key'];nid=ids.get(k);n=A('notesInfo',notes=[nid])[0] if nid else None
  if nid in em_tela(A):pending.append(k);continue
  new=not n
  if new:
   nid=A('addNote',note={'deckName':p['deck'],'modelName':e['model'],'fields':e['fields'],'tags':e['tags'],'options':{'allowDuplicate':True}})
   ids[k]=nid;created[k]=nid;statepath.write_text(json.dumps(created));n=A('notesInfo',notes=[nid])[0]
  else:
   # Same cloze identities, so all prior scheduling remains valid.
   assert set(re.findall(r'\{\{c(\d+)::',n['fields']['Text']['value']))==set(re.findall(r'\{\{c(\d+)::',e['fields']['Text'])),k
   upd={f:v for f,v in e['fields'].items() if f in ('Text','Extra') and not same(n['fields'][f]['value'],v)}
   if upd:A('updateNoteFields',note={'id':nid,'fields':upd})
   stale=[t for t in n['tags'] if t.startswith(f'NEBLI::ordem::{short}-') or t.startswith(f'NEBLI::cor::{L}::') or t.startswith('NEBLI::retirado')]
   if stale:A('removeTags',notes=[nid],tags=' '.join(stale))
   A('addTags',notes=[nid],tags=' '.join(e['tags']))
   # Undo only the suspension introduced by the rejected first revision.
   if k in json.loads((B/'restore.json').read_text()):
    before=json.loads((B/'anki-before.json').read_text());original={c['cardId']:c for c in before['cards']}
    uns=[c for c in n['cards'] if original[c]['queue']!=-1]
    if uns:A('unsuspend',cards=uns)
  for c in A('cardsInfo',cards=n['cards']):
   if new:A('setSpecificValueOfCard',card=c['cardId'],keys=['flags'],newValues=[next(x['flag'] for x in e['cards'] if x['ord']==c['ord'])],warning_check=True)
   if c['type']==0:A('setSpecificValueOfCard',card=c['cardId'],keys=['due'],newValues=[base+e['order']*10+c['ord']],warning_check=True)
 for nid,s in p['compartilhados'].items():
  nid=int(nid)
  if nid in em_tela(A):pending.append(str(nid));continue
  n=A('notesInfo',notes=[nid])[0];stale=[t for t in n['tags'] if t.startswith(f'NEBLI::ordem::{short}-')]
  if stale:A('removeTags',notes=[nid],tags=' '.join(stale))
  A('addTags',notes=[nid],tags=s['ordem_tag'])
 # Compartilhado que deixou o escopo: só desassociar esta aula; a nota e o
 # histórico continuam intactos na aula de origem.
 for nid in (1791625430332,):
  if nid in em_tela(A):pending.append(str(nid));continue
  n=A('notesInfo',notes=[nid])[0]
  stale=[t for t in n['tags'] if t == f'NEBLI::{L}' or t.startswith(f'NEBLI::ordem::{short}-') or t.startswith(f'NEBLI::cor::{L}::')]
  if stale:A('removeTags',notes=[nid],tags=' '.join(stale))
results=[]
for e in p['entries']:
 k=e['key'];nid=ids.get(k)
 if not nid:continue
 n=A('notesInfo',notes=[nid])[0];ci=A('cardsInfo',cards=n['cards'])
 if k not in pending:assert all(same(n['fields'][f]['value'],e['fields'][f]) for f in ('Text','Extra')),k
 results.append({'key':k,'nid':nid,'cards':{str(c['cardId']):{'ord':c['ord'],'flag':c['flags']} for c in ci}})
flags=[c['flag'] for n in results for c in n['cards'].values()]
rec.update(notes=results,selection_hash=p['selection_hash'],cards_tag_aula=len(A('findCards',query=f'tag:NEBLI::{L}')),cards_new_lesson=len(flags),expected=p['totais']['cards'],green=flags.count(3),blue=flags.count(4),pink=flags.count(5),problems=pending,at=datetime.now(timezone.utc).isoformat())
(R/'receipt.json').write_text(json.dumps(rec,ensure_ascii=False,indent=1));(R/'plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=1))
if not pending:(R/'plan-aplicado.json').write_text(json.dumps(p,ensure_ascii=False,indent=1))
report={'deleted':deleted,'preserved_other_lesson':preserved,'pending':pending,'cards':rec['cards_tag_aula']};(B/('v2-result-'+datetime.now().strftime('%H%M%S')+'.json')).write_text(json.dumps(report,ensure_ascii=False,indent=1));print(json.dumps(report,ensure_ascii=False))
