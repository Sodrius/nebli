import json, re, html, sys
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent
S = json.loads((BASE/'snapshot.json').read_text())
N = {n['noteId']:n for n in S['notes']}
F = {cid:int(f) for f,ids in S['flags'].items() for cid in ids}
MEDIA = Path('/Users/davisousa/Library/Application Support/Anki2/User 1/collection.media')
def plain(value):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', value))).strip()
def row(c, full=False):
    n=N[c['note']]
    fields={k:v['value'] for k,v in n['fields'].items() if v['value']}
    text=fields.get('Text',fields.get('Front',fields.get('Title','')))
    return {'cid':c['cardId'],'nid':c['note'],'ord':c['ord'],'flag':F[c['cardId']],
      'deck':c['deckName'].split('::')[-1], 'model':n['modelName'],
      'text':plain(text),'tags':[t for t in n['tags'] if t.startswith('NEBLI') or 'Yield' in t],
      **({'fields':fields} if full else {})}
mode=sys.argv[1]
if mode=='feedback':
    for c in S['cards']:
        if F[c['cardId']] in (1,2) or N[c['note']]['fields'].get('NEBLI_Comentario',{}).get('value'):
            print(json.dumps(row(c,True),ensure_ascii=False))
elif mode=='models':
    for name,m in S['models'].items():
        print(name, 'fields:',m['fields'])
        print(json.dumps(m,ensure_ascii=False)[:16000])
elif mode=='media':
    missing=[]
    for c in S['cards']:
        refs=set(re.findall(r'<img[^>]+src=[\"\']([^\"\']+)',c['question']+c['answer'],re.I))
        bad=[r for r in refs if not r.startswith(('http','data:')) and not (MEDIA/html.unescape(r)).exists()]
        if bad:missing.append({'cid':c['cardId'],'deck':c['deckName'],'missing':bad})
    (BASE/'missing-media.json').write_text(json.dumps(missing,ensure_ascii=False,indent=1))
    print(json.dumps({'cards_with_missing_media':len(missing),'decks':dict(Counter(x['deck'] for x in missing)),'examples':missing[:12]},ensure_ascii=False,indent=1))
elif mode=='cards':
    pattern=sys.argv[2].casefold()
    for c in S['cards']:
        if pattern in c['deckName'].casefold():
            print(json.dumps(row(c, '--full' in sys.argv),ensure_ascii=False))
elif mode=='configs':
    unique={v['id']:v for v in S['configs'].values()}
    print(json.dumps(unique,ensure_ascii=False,indent=1))
