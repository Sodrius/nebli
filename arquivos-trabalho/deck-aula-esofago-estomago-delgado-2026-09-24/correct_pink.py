import json
from datetime import datetime,timezone
from apply import HERE,LOCK,call,save

TARGETS={1482022126258,1482022129277}
with LOCK.open('x',encoding='utf-8') as f:f.write(json.dumps({'executor':'Codex','lesson':'X3 pink correction','at':datetime.now(timezone.utc).isoformat()}))
try:
    receipt=json.loads((HERE/'receipt.json').read_text(encoding='utf-8'))
    changed=[]
    for row in receipt['created']:
        if row['source_nid'] not in TARGETS:continue
        for c in call('cardsInfo',cards=row['card_ids']):
            if c['flags']!=5 or c['queue']<0:raise RuntimeError(f'Unexpected state on {c["cardId"]}')
            call('setSpecificValueOfCard',card=c['cardId'],keys=['flags'],newValues=[0],warning_check=True)
            changed.append(c['cardId'])
        row['flag']=0
    if len(changed)!=2:raise RuntimeError(changed)
    receipt['totals']['pink']=8
    save('receipt.json',receipt)
    (HERE/'journal.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in receipt['created']),encoding='utf-8')
    print(changed)
    print(call('sync'))
    save('sync-after-pink-correction.json',{'cards':changed,'at':datetime.now(timezone.utc).isoformat()})
finally:LOCK.unlink(missing_ok=True)
