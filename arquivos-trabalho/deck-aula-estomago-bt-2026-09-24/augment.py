"""Add inspected targets discovered in the X5 content audit."""
import json
from datetime import datetime,timezone
from apply import call,digest,ident,LOCK,HERE,PLAN,TAG,MODELS

assert call('getActiveProfile')==PLAN['profile']
receipt_path=HERE/'receipt.json'
receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
existing={r['identity'] for r in receipt['created']}
missing=[e for e in PLAN['entries'] if ident(e) not in existing]
assert missing and all(e['source_nid'] for e in missing)
for entry in missing:
 source=call('notesInfo',notes=[entry['source_nid']])[0]
 assert digest({k:v['value'] for k,v in source['fields'].items()})==entry['source_fields_hash']
 assert not call('findNotes',query=f'tag:"{ident(entry)}"')
with LOCK.open('x',encoding='utf-8') as f:f.write(json.dumps(dict(executor='Codex',lesson=PLAN['lesson_id'],action='augment',at=datetime.now(timezone.utc).isoformat())))
try:
 for entry in missing:
  nid=call('addNote',note=dict(deckName=PLAN['target_deck'],modelName=MODELS[entry['source_model']],fields=entry['fields'],tags=entry['source_tags']+[TAG,ident(entry),'NEBLI::origem::'+entry['origin']],options=dict(allowDuplicate=True)))
  assert nid
  note=call('notesInfo',notes=[nid])[0]
  cards=call('cardsInfo',cards=note['cards'])
  assert len(cards)==entry['expected_cards'] and all(c['deckName']==PLAN['target_deck'] for c in cards)
  flag=5 if entry['pink'] else 3 if entry['high_yield'] else 0
  if flag:
   for c in cards:call('setSpecificValueOfCard',card=c['cardId'],keys=['flags'],newValues=[flag],warning_check=True)
  row=dict(identity=ident(entry),source_nid=entry['source_nid'],note_id=nid,card_ids=note['cards'],flag=flag,origin=entry['origin'])
  receipt['created'].append(row)
  with (HERE/'journal.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 receipt['totals']=PLAN['totals']
 receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
 print('sync:',call('sync'))
finally:LOCK.unlink(missing_ok=True)
