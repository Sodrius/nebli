import json,sys,re,html
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from nebli.preflight import ReadOnlyAnki, chunks
call=ReadOnlyAnki(); p=Path(__file__).parent
root=next(d for d in call('deckNames') if d.lower().endswith('::anking step deck'))
queries=['properdin','hemosiderin','"nutmeg"','"Cori cycle"','puborectalis','"TLR3"','"TLR5"','"autoclave"','"PAMPs"','"lacZ"','"CR3"','"fructosamine"','"central lacteal"']
rows=[]
for term in queries:
    ids=call('findCards',query=f'deck:"{root}" {term}')
    cs=call('cardsInfo',cards=ids[:35]) if ids else []
    ns=call('notesInfo',notes=sorted({c['note'] for c in cs})) if cs else []
    vals=[]
    for n in ns:
        f=n['fields']; t=html.unescape(re.sub('<[^>]*>',' ',f.get('Text',{}).get('value','')))
        vals.append(dict(nid=n['noteId'],text=' '.join(t.split())))
    rows.append(dict(query=term,total_cards=len(ids),notes=vals))
(p/'targeted-source-search.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(rows,ensure_ascii=True))
