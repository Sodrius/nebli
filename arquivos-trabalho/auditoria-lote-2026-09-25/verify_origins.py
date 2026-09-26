import json,sys,re
from pathlib import Path
from collections import Counter,defaultdict
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from nebli.preflight import ReadOnlyAnki,chunks
p=Path(__file__).parent;s=json.loads((p/'snapshot.json').read_text(encoding='utf-8'));call=ReadOnlyAnki()
mapping={n['noteId']:int(t.split('nid-')[-1]) for n in s['notes'] for t in n['tags'] if t.startswith('NEBLI::source::nid-')}
ids=sorted(set(mapping.values()));ns=[n for b in chunks(ids) for n in call('notesInfo',notes=b)]
cids=sorted({i for n in ns for i in n.get('cards',[])})
cs=[c for b in chunks(cids) for c in call('cardsInfo',cards=b)]
decks={c['note']:c['deckName'] for c in cs};nn={n['noteId']:n for n in s['notes']}
origin=lambda d: 'AnKing' if 'anking step deck' in d.lower() else d.split('Referências Externas::')[-1].split('::')[0]
counts=Counter();mismatch=[];bydeck=defaultdict(Counter)
for c in s['cards']:
    n=nn[c['note']];source=mapping.get(n['noteId']);declared=next(t.split('::')[-1] for t in n['tags'] if t.startswith('NEBLI::origem::'))
    actual=origin(decks[source]) if source in decks else declared
    counts[actual]+=1;bydeck[c['deckName']][actual]+=1
    if declared=='AnKing' and actual!='AnKing':mismatch.append(dict(cid=c['cardId'],nid=n['noteId'],source=source,declared=declared,actual=actual))
result=dict(counts=counts,bydeck=bydeck,mismatch=mismatch,unresolved_sources=[i for i in ids if i not in decks])
(p/'verified-origins.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))
