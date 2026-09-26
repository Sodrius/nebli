"""Remove one freshly created out-of-scope copy, preserving its original source."""
import json
from datetime import datetime,timezone
from apply import call,LOCK,HERE,PLAN

receipt_path=HERE/'receipt.json'
receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
row=next(r for r in receipt['created'] if r['source_nid']==1486591317696)
assert row['origin']=='AnKing' and len(row['card_ids'])==1
assert row['note_id'] in call('findNotes',query=f'deck:"{PLAN["target_deck"]}"')
assert call('notesInfo',notes=[1486591317696])[0]['cards']
with LOCK.open('x',encoding='utf-8') as f:f.write(json.dumps(dict(executor='Codex',lesson=PLAN['lesson_id'],action='prune',at=datetime.now(timezone.utc).isoformat())))
try:
    call('deleteNotes',notes=[row['note_id']])
    assert row['note_id'] not in call('findNotes',query=f'deck:"{PLAN["target_deck"]}"')
    assert call('notesInfo',notes=[1486591317696])[0]['cards']
    receipt['created']=[r for r in receipt['created'] if r['note_id']!=row['note_id']]
    receipt['totals']=PLAN['totals']
    receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    (HERE/'prune.json').write_text(json.dumps(dict(removed_copy=row,reason='Budd-Chiari is not in the lecture or old E1 scope',source_preserved=True),ensure_ascii=False,indent=2),encoding='utf-8')
    print('sync:',call('sync'))
finally:LOCK.unlink(missing_ok=True)
