import json,re,sys,sqlite3
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from nebli.explicacoes import store_path
from prepare import clean
P=Path(__file__).resolve().parent
ns={n['noteId']:n for n in json.loads((P/'snapshot.json').read_text())}
changes=json.loads((P/'changes.json').read_text())
db=sqlite3.connect(f'file:{store_path()}?mode=ro',uri=True);db.row_factory=sqlite3.Row
tabs={r['card_id']:dict(r) for r in db.execute('select * from explicacoes')}
(P/'tabs-before.json').write_text(json.dumps(tabs,ensure_ascii=False,indent=2))
for c in changes:
    old=c['before'].get('Text','');new=c['fields'].get('Text','')
    if old and clean(old)!=clean(new) and c['nid'] in {int(x) for x in sys.argv[1:] if x.isdigit()}:
        for cid in ns[c['nid']]['cards']:
            t=tabs.get(cid,{})
            print(c['nid'],cid,'STATUS',t.get('status'), '\nNEW',clean(new),'\nTAB',t.get('texto','')[:1400])
print('Missing Tabs',[(c['nid'],cid) for c in changes for cid in ns[c['nid']]['cards'] if cid not in tabs])
numbered=[t for t in tabs.values() if t['note_id'] in ns and re.search(r'(?:^|\n|Por quê:)\s*1[.)]',t['texto'] or '')]
print('Numbered Tabs',len(numbered))
if '--numbered' in sys.argv:
    for t in numbered: print(t['card_id'],t['note_id'],t['texto'])
