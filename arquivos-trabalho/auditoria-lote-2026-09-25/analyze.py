import json,re,html
from pathlib import Path
from collections import Counter,defaultdict
from statistics import median
p=Path(__file__).parent
s=json.loads((p/'snapshot.json').read_text(encoding='utf-8'))
notes={n['noteId']:n for n in s['notes']}
flags={cid:int(k) for k,ids in s['flags'].items() for cid in ids}
def plain(v):
    v=re.sub(r'<(style|script)\b[^>]*>.*?</\1>','',v,flags=re.S|re.I)
    return ' '.join(html.unescape(re.sub('<[^>]+>',' ',v)).split())
def origin(n):return next((t.split('::')[-1] for t in n['tags'] if t.startswith('NEBLI::origem::')),'unknown')
summary={}; lines=[]; noimage=[]; source=defaultdict(list); normalized=defaultdict(list)
for n in s['notes']:
    for t in n['tags']:
        if t.startswith('NEBLI::source::'):source[t].append(n['noteId'])
    fs={k:v['value'] for k,v in n['fields'].items()}
    if origin(n)=='Autoral' and not re.search(r'<img|<svg', ' '.join(fs.values()),re.I):noimage.append(n['noteId'])
    tx=plain(fs.get('Text',fs.get('Front','')))
    if tx: normalized[re.sub(r'\{\{c\d+::','{{c::',tx).lower()].append(n['noteId'])
for deck in sorted({c['deckName'] for c in s['cards']}):
    cs=[c for c in s['cards'] if c['deckName']==deck]; ns=[notes[i] for i in sorted({c['note'] for c in cs})]
    summary[deck]={'cards':len(cs),'notes':len(ns),'origins':dict(Counter(origin(notes[c['note']]) for c in cs)),
      'flags':dict(Counter(flags[c['cardId']] for c in cs)),
      'author_notes_no_image':sum(n['noteId'] in noimage for n in ns),
      'shared_notes':sum(sum(t.startswith('NEBLI::2026-') for t in n['tags'])>1 for n in ns)}
    lines.append('\n## '+deck)
    for n in ns:
        fs={k:v['value'] for k,v in n['fields'].items()}; nc=[c for c in cs if c['note']==n['noteId']]
        tx=plain(fs.get('Text',fs.get('Front',fs.get('Title',''))))
        extra=plain(fs.get('Extra',fs.get('Back',fs.get('Clinical',''))))
        imgs=re.findall(r'<img[^>]+src=[\"\x27]([^\"\x27]+)', ' '.join(fs.values()),re.I)
        lines.append(f"{n['noteId']} [{origin(n)};{','.join(str(flags[c['cardId']]) for c in nc)};{len(nc)}c;{len(imgs)}img] {tx} | {extra}")
result=dict(by_deck=summary,origins=dict(Counter(origin(notes[c['note']]) for c in s['cards'])),
  author_notes_no_image=noimage,duplicate_source={k:v for k,v in source.items() if len(v)>1},
  identical_text_notes={k:v for k,v in normalized.items() if len(v)>1},
  green_without_literal_hy=[c['cardId'] for c in s['cards'] if flags[c['cardId']]==3 and '#AK_Step1_v12::#Low/HighYield::1-HighYield' not in notes[c['note']]['tags']],
  live_ankihub_ids=[n['noteId'] for n in s['notes'] if n['fields'].get('ankihub_id',{}).get('value')])
(p/'metrics.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(p/'cards-readable.txt').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))
