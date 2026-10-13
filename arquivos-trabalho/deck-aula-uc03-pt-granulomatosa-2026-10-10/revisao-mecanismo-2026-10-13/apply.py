import json, sys, runpy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from nebli.decks import Anki, escrita, em_tela
from nebli.delta import same
R=Path(__file__).resolve().parent.parent; B=Path(__file__).resolve().parent
A=Anki(); changes=json.loads((B/'changes.json').read_text()); old=json.loads((B/'plan.json').read_text()); rec=json.loads((R/'receipt.json').read_text())
keys={x['key']:x['nid'] for x in rec['notes']}; ids=list(keys.values())+[int(x) for x in old['compartilhados']]
notes={n['noteId']:n for n in A('notesInfo',notes=ids) if n}; cards=A('cardsInfo',cards=[c for n in notes.values() for c in n['cards']])
if not (B/'anki-before.json').exists():(B/'anki-before.json').write_text(json.dumps({'notes':notes,'cards':cards},ensure_ascii=False,indent=1))
if '--inspect' in sys.argv:
 print(json.dumps({'notes':len(notes),'cards':len(cards),'protected':list(em_tela(A)),'other_lesson_removals':{k:[t for t in notes[keys[k]]['tags'] if t.startswith('NEBLI::2026-') and old['lesson_id'] not in t] for k in changes['remove'] if k in keys}},ensure_ascii=False));sys.exit()
if '--finish' in sys.argv:
 from nebli.delta import base_of
 from datetime import datetime, timezone
 plan=json.loads((R/'plan.json').read_text()); pending=[];base=base_of(R,plan['short'])
 targets=[(keys[e['key']],e) for e in plan['entries']]+[(int(n),e) for n,e in plan['compartilhados'].items()]
 with escrita(A,'PT47 ordem após revisão 13/10',sync=False):
  for nid,e in targets:
   if nid in em_tela(A):pending.append(nid);continue
   n=A('notesInfo',notes=[nid])[0];prefix='NEBLI::ordem::pt47-';want=e.get('ordem_tag') or next(t for t in e['tags'] if t.startswith(prefix))
   stale=[t for t in n['tags'] if t.startswith(prefix) and t!=want]
   if stale:A('removeTags',notes=[nid],tags=' '.join(stale))
   if want not in n['tags']:A('addTags',notes=[nid],tags=want)
   if nid in keys.values():
    for c in A('cardsInfo',cards=n['cards']):
     if c['type']==0:A('setSpecificValueOfCard',card=c['cardId'],keys=['due'],newValues=[base+e['order']*10+c['ord']],warning_check=True)
 assert not pending, pending
 results=[]
 for e in plan['entries']:
  nid=keys[e['key']];n=A('notesInfo',notes=[nid])[0]
  assert all(same(n['fields'][f]['value'],v) for f,v in e['fields'].items() if f in ('Text','Extra')),e['key']
  ci=A('cardsInfo',cards=n['cards']);results.append({'key':e['key'],'nid':nid,'cards':{str(c['cardId']):{'ord':c['ord'],'flag':c['flags']} for c in ci}})
 flags=[c['flag'] for n in results for c in n['cards'].values()]
 rec.update(notes=results,selection_hash=plan['selection_hash'],cards_tag_aula=len(A('findCards',query='tag:NEBLI::'+plan['lesson_id'])),cards_new_lesson=len(flags),expected=plan['totais']['cards'],green=flags.count(3),blue=flags.count(4),pink=flags.count(5),problems=[],at=datetime.now(timezone.utc).isoformat())
 (R/'receipt.json').write_text(json.dumps(rec,ensure_ascii=False,indent=1));(R/'plan-aplicado.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1));print('ordem e readback ok',rec['cards_tag_aula']);sys.exit()
prior=json.loads((B/'result.json').read_text()) if (B/'result.json').exists() else {}
removed=[];updated=[];pending=[];L=old['lesson_id'];short=old['short']
with escrita(A,'PT47 revisão mecanismo geral 13/10',sync=False):
 for k in changes['remove']:
  if k not in keys:continue
  nid=keys[k];n=A('notesInfo',notes=[nid])[0]
  if nid in em_tela(A):pending.append(k);continue
  others=[t for t in n['tags'] if t.startswith('NEBLI::2026-') and L not in t]
  if others:
   # The note remains in the other lesson with its scheduling and flags intact.
   lesson=others[0].split('::',1)[1]
   targets=[]
   for pp in R.parent.glob('*/plan.json'):
    data=json.loads(pp.read_text())
    if data.get('lesson_id')==lesson:targets.append(data['deck'])
   assert targets, f'No destination deck for {lesson}'
   A('changeDeck',cards=n['cards'],deck=targets[0])
  else:A('suspend',cards=n['cards'])
  rm=[t for t in n['tags'] if L in t or t.startswith(f'NEBLI::ordem::{short}-') or t==f'NEBLI::compartilhado::{short}']
  if rm:A('removeTags',notes=[nid],tags=' '.join(rm))
  A('addTags',notes=[nid],tags=f'NEBLI::retirado::especificidade-sem-ganho-para-mecanismo-geral NEBLI::retirado-de::{short}')
  check=A('notesInfo',notes=[nid])[0];assert f'NEBLI::{L}' not in check['tags'];assert others or all(A('areSuspended',cards=n['cards']))
  assert check['fields'].get('NEBLI_Comentario')==n['fields'].get('NEBLI_Comentario')
  removed.append(k)
 for k,v in changes['updates'].items():
  if k in prior.get('updated',[]):continue
  nid=keys[k]
  if nid in em_tela(A):pending.append(k);continue
  fields={'Text':v['text'],'Extra':v['extra']};A('updateNoteFields',note={'id':nid,'fields':fields})
  check=A('notesInfo',notes=[nid])[0];assert all(same(check['fields'][f]['value'],x) for f,x in fields.items())
  updated.append(k)
# Persist completed operations only. Refuse a rebuild if the protected note was deferred.
rec['notes']=[n for n in rec['notes'] if n['key'] not in removed];(R/'receipt.json').write_text(json.dumps(rec,ensure_ascii=False,indent=1))
p=R/'retirados.json';rr=json.loads(p.read_text()) if p.exists() else [];rr.extend({'key':k,'nid':keys[k],'motivo':'especificidade-sem-ganho-para-mecanismo-geral'} for k in removed);p.write_text(json.dumps(rr,ensure_ascii=False,indent=1))
p=R/'correcoes-vivas.json';cc=json.loads(p.read_text())
for k in updated:cc[k]={'Text':changes['updates'][k]['text'],'Extra':changes['updates'][k]['extra'],'_motivo':'F-20261013-CODEX-02: mecanismo geral','_nid':keys[k]}
p.write_text(json.dumps(cc,ensure_ascii=False,indent=1))
result={'removed':list(dict.fromkeys(prior.get('removed',[])+removed)),'updated':list(dict.fromkeys(prior.get('updated',[])+updated)),'pending':pending};(B/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=1));print(json.dumps(result,ensure_ascii=False))
assert not pending,'Resolver notas protegidas/compartilhadas antes de reconstruir o plano'
