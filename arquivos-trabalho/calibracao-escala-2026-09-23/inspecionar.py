"""Read-only Anki inspection for the user's calibration questionnaire."""
import json, urllib.request, re, html
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone

ROOT = Path(__file__).parent
ALLOWED = {'deckNames', 'findCards', 'cardsInfo', 'notesInfo', 'getMediaDirPath'}
def call(action, **params):
    assert action in ALLOWED
    req = urllib.request.Request('http://127.0.0.1:8765', json.dumps(dict(action=action,version=6,params=params)).encode(), {'Content-Type':'application/json'})
    with urllib.request.urlopen(req, timeout=90) as r:
        result=json.load(r)
    if result.get('error'): raise RuntimeError(result['error'])
    return result['result']

def plain(s):
    s=re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', s or '', flags=re.S|re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', s))).strip()

def batches(action, key, ids):
    out=[]
    for start in range(0,len(ids),100): out.extend(call(action, **{key:ids[start:start+100]}))
    return out

if __name__=='__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    decks=call('deckNames')
    counts={d:len(call('findCards',query='deck:"'+d+'"')) for d in decks if not any(x.startswith(d+'::') for x in decks)}
    all_ids=call('findCards',query='')
    ids=call('findCards',query='deck:NEBLI::UC*')
    cards=batches('cardsInfo','cards',ids)
    notes=batches('notesInfo','notes',sorted({c['note'] for c in cards}))
    flags={i:set(call('findCards',query=f'deck:NEBLI::UC* flag:{i}')) for i in range(1,8)}
    for c in cards: c['audit_flag']=next((i for i,s in flags.items() if c['cardId'] in s),0)
    snapshot=dict(at=datetime.now(timezone.utc).isoformat(),collection_cards=len(all_ids),leaf_counts=counts,cards=cards,notes=notes)
    (ROOT/'snapshot.json').write_text(json.dumps(snapshot,ensure_ascii=False),encoding='utf-8')
    report=[]
    for d in sorted({c['deckName'] for c in cards}):
        cs=[c for c in cards if c['deckName']==d]
        report.append(dict(deck=d,notes=len({c['note'] for c in cs}),cards=len(cs),flags=dict(Counter(c['audit_flag'] for c in cs)),reviewed=sum(c.get('reps',0)>0 for c in cs),suspended=sum(c.get('queue')==-1 for c in cs),models=dict(Counter(c['modelName'] for c in cs))))
    compact=[]
    for n in notes:
        cs=[c for c in cards if c['note']==n['noteId']]
        compact.append(dict(nid=n['noteId'],deck=cs[0]['deckName'],model=n['modelName'],tags=[t for t in n['tags'] if 'NEBLI' in t or 'HighYield' in t],fields={k:plain(v['value']) for k,v in n['fields'].items() if v['value'] and k not in ['ankihub_id']},cards=[dict(cid=c['cardId'],ord=c.get('ord'),flag=c['audit_flag'],reps=c.get('reps'),lapses=c.get('lapses'),question=plain(c.get('question',''))) for c in cs]))
    (ROOT/'conteudo-notas.json').write_text(json.dumps(compact,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'resumo.json').write_text(json.dumps(dict(collection_cards=len(all_ids),leaf_counts=counts,medical=report),ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(collection_cards=len(all_ids),leaf_counts=counts,medical=report),ensure_ascii=False,indent=2))
