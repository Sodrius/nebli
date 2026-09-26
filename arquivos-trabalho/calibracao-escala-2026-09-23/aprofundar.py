"""Read-only supporting checks; not a curation/apply script."""
import json, re, sys
from collections import defaultdict
from inspecionar import call, ROOT, plain
sys.stdout.reconfigure(encoding='utf-8')
s=json.loads((ROOT/'snapshot.json').read_text(encoding='utf-8'))
source_map=defaultdict(list)
for n in s['notes']:
    for t in n['tags']:
        if '::source::nid-' in t: source_map[t].append(n['noteId'])
print('Repeated source IDs:',json.dumps({k:v for k,v in source_map.items() if len(v)>1}))
for n in s['notes']:
    lesson_tags=[t for t in n['tags'] if t.startswith('NEBLI::2026-')]
    if len(lesson_tags)>1: print('Shared note:',n['noteId'],lesson_tags,'cards',n['cards'])
    comment=n['fields'].get('NEBLI_Comentario',{}).get('value','')
    if comment: print('User comment:',n['noteId'],plain(comment))
    if n['modelName'].startswith('AnKingOverhaul') and n['fields'].get('ankihub_id',{}).get('value',''):
        print('Nonempty ankihub_id on medical copy:',n['noteId'])
for term in ['properdin','palindromic','nucleoid','restriction enzyme','factor H','Lgr5']:
    ids=call('findCards',query='deck:"AnKing Step Deck" '+term)
    found=call('cardsInfo',cards=ids[:80]) if ids else []
    matches=[]
    for c in found:
        text=' '.join(plain(c['fields'].get(k,{}).get('value','')) for k in ['Text','Extra'])
        if term.lower() in text.lower():
            matches.append(dict(nid=c['note'],text=plain(c['fields'].get('Text',{}).get('value','')),extra=plain(c['fields'].get('Extra',{}).get('value',''))[:260]))
    unique={m['nid']:m for m in matches}
    print('Targeted source check:',term,'raw cards',len(ids),'text matches',json.dumps(list(unique.values()),ensure_ascii=False))
print('Image examples:')
for nid in [1790110920730,1790161083441,1790161084566,1790111511038]:
    n=next(n for n in s['notes'] if n['noteId']==nid)
    imgs=re.findall(r'<img[^>]+src=[\"\x27]([^\"\x27]+)', ' '.join(v['value'] for v in n['fields'].values()))
    print(nid,imgs[:4])
