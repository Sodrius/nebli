import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki
from nebli.explicacoes import open_store

p = Path(__file__).resolve().parent
a = Anki()
if '--siblings' in sys.argv:
    ns=a('notesInfo',notes=a('findNotes',query='deck:NEBLI* "nebli-uc08-an01-p05b.png"'))
    (p/'siblings-before.json').write_text(json.dumps({'notes':ns},ensure_ascii=False,indent=2))
    print('siblings',len(ns));sys.exit()
if '--related' in sys.argv:
    query = 'deck:NEBLI* ("576cbd235527ed0da189465acdf9daa7.webp" OR "7622bdccaa72d53bb3fae2ccf397d414.webp" OR "99707c085e94c71df7d290c44906e875.webp" OR "09b1a4ed4f6059189a53ef4cad0f4753.webp" OR "b8647af3199815237f7622aff1f2a0fc.webp" OR "477f80c20c979758e5f388cc1e5639dc.webp" OR "short vasa" OR "clasia" OR "eosinofilia" OR "-íase")'
    ns = a('notesInfo', notes=a('findNotes', query=query))
    cs = a('cardsInfo', cards=[c for n in ns for c in n['cards']])
    db = open_store()
    db.row_factory = __import__('sqlite3').Row
    ts = [dict(row) for c in cs for row in db.execute('select * from explicacoes where card_id=?',(c['cardId'],))]
    out = p / 'related-before.json'
    if not out.exists(): out.write_text(json.dumps({'notes':ns,'cards':cs,'tabs':ts},ensure_ascii=False,indent=2))
    for n in ns:
        print(n['noteId'], n['fields'].get('Text',{}).get('value','')[:220])
    print('MODEL', json.dumps(a('modelTemplates', modelName='NEBLI Image Occlusion Enhanced+ independente - v2'),ensure_ascii=False)[:7000])
    sys.exit()
if len(sys.argv) > 1 and '--refresh' not in sys.argv:
    for query in sys.argv[1:]:
        ids = a('findNotes', query=query)
        ns = a('notesInfo', notes=ids[:35])
        print('QUERY', query, 'TOTAL', len(ids))
        for n in ns:
            print(json.dumps({'nid': n['noteId'], 'model': n['modelName'], 'fields': {k:v['value'] for k,v in n['fields'].items() if v['value'] and k in ['Text','Extra','Front','Back','Image','Remarks','Question Mask','Answer Mask']}, 'tags': [t for t in n['tags'] if t.startswith('NEBLI::ordem')]}, ensure_ascii=False))
    sys.exit()
ids = a('findNotes', query='NEBLI_Comentario:_*')
notes = a('notesInfo', notes=ids)
cards = a('cardsInfo', cards=[cid for n in notes for cid in n['cards']])
db = open_store()
tabs = [dict(zip([d[0] for d in cur.description], row)) for c in cards for cur in [db.execute('select * from explicacoes where card_id=?', (c['cardId'],))] for row in cur.fetchall()]
snapshot = {'profile': a('getActiveProfile'), 'notes': notes, 'cards': cards, 'tabs': tabs}
out = p / ('refresh.json' if '--refresh' in sys.argv else 'before.json')
if out.exists():
    raise SystemExit('Snapshot already exists')
out.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2))
for n in notes:
    print('\nNOTE', n['noteId'], n['modelName'], 'CARDS', n['cards'])
    for k,v in n['fields'].items():
        if v['value'] and k not in ['Tags', 'ankihub_id']:
            print(k, ':', v['value'][:3500])
