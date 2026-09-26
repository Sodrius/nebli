import json,uuid
from pathlib import Path
from urllib.request import Request,urlopen
from datetime import datetime,timezone
p=Path(__file__).parent;lock=p.parent/'ANKI-ESCRITA.lock'
def call(action,**params):
    with urlopen(Request('http://127.0.0.1:8765',json.dumps(dict(action=action,version=6,params=params)).encode(),{'Content-Type':'application/json'}),timeout=45) as f:r=json.load(f)
    if r['error']:raise RuntimeError(r['error'])
    return r['result']
rows=[json.loads(l) for l in (p/'fix-journal.jsonl').read_text(encoding='utf-8').splitlines()]
blue={r['cid'] for r in rows if r['action']=='pink_to_blue'}
assert blue <= set(call('findCards',query='deck:NEBLI::UC* flag:4'))
assert not call('findCards',query='nid:1790271593612')
s=json.loads((p/'snapshot.json').read_text(encoding='utf-8'))
old={c['cardId'] for c in s['cards']};live=set(call('findCards',query='deck:NEBLI::UC*'))
removed=old-live;added=live-old
assert removed=={c['cardId'] for c in s['cards'] if c['note']==1790271593612}
addcards=call('cardsInfo',cards=sorted(added)) if added else []
token=str(uuid.uuid4());sync='not attempted: another writer lock' if lock.exists() else None
if sync is None:
    with lock.open('x',encoding='utf-8') as f:json.dump(dict(executor='Codex',task='sync-correcoes-auditoria',token=token),f)
    try:sync=call('sync')
    finally:
        if json.loads(lock.read_text(encoding='utf-8')).get('token')==token:lock.unlink()
receipt=dict(at=datetime.now(timezone.utc).isoformat(),cards=len(live),blue_migrated=len(blue),
    field_notes=[r['nid'] for r in rows if r['action']=='update_fields'],
    origin_notes=len([r for r in rows if r['action']=='origin_tag']),
    deleted_note=1790271593612,deleted_card_ids=sorted(removed),
    concurrent_added_cards=[dict(cid=c['cardId'],deck=c['deckName']) for c in addcards],
    concurrent_work_not_modified=True,sync_result=sync,
    flags={i:len(call('findCards',query=f'deck:NEBLI::UC* flag:{i}')) for i in range(8)},
    backup='backup-intestinos-before-exclusion.apkg',core_not_classified=True)
with (p/'fix-receipt.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps(receipt,ensure_ascii=True))
