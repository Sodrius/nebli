"""Validação de readback e APKG exportado; não escreve na coleção viva."""
import collections, html, json, re, sqlite3, tempfile, zipfile
from pathlib import Path
from preparar_v2 import OUT

def main():
    p=json.loads((OUT/'plan.json').read_text(encoding='utf-8'))
    receipt=json.loads((OUT/'receipt.json').read_text(encoding='utf-8'))
    after=json.loads((OUT/'after.json').read_text(encoding='utf-8'))
    notes={n['noteId']:n for n in after['notes']}
    cards={c['cardId']:c for c in after['cards']}
    result_by_key={r['key']:r for r in receipt['results']}
    errors=[];rendered=[]
    for e in p['entries']:
        r=result_by_key[e['key']]
        for cid in r['cards']:
            c=cards[cid]
            if '{{c' in c['question'] or '{{c' in c['answer']:errors.append(('cloze_not_rendered',cid))
            if not re.search(r'class=["\x27]cloze',c['question']):errors.append(('missing_cloze',cid))
            if 'Faculdade:' not in c['answer']:errors.append(('missing_priority',cid))
            if c['deckName']!=p['target_deck']:errors.append(('wrong_deck',cid))
            rendered.append({'key':e['key'],'cid':cid,'cloze':c['ord']+1,'question':c['question'],'answer':c['answer']})
    package=Path(receipt['package'])
    with zipfile.ZipFile(package) as z:
        names=z.namelist()
        dbname='collection.anki21' if 'collection.anki21' in names else 'collection.anki2'
        media=json.loads(z.read('media'))
        with tempfile.TemporaryDirectory(prefix='nebli-check-apkg-') as tmp:
            db=Path(tmp)/dbname;db.write_bytes(z.read(dbname))
            conn=sqlite3.connect(f'{db.as_uri()}?mode=ro',uri=True)
            n=conn.execute('select count(*) from notes').fetchone()[0]
            c=conn.execute('select count(*) from cards').fetchone()[0]
            assert n==receipt['notes'] and c==receipt['cards'],(n,c)
            package_notes={r[0]:r[1:] for r in conn.execute('select id,guid,flds from notes')}
            package_cards={r[0]:r[1:] for r in conn.execute('select id,nid,ord from cards')}
            assert set(package_cards)==set(cards)
            for nid,note in notes.items():
                fields='\x1f'.join(v['value'] for _,v in sorted(note['fields'].items(),key=lambda kv:kv[1]['order']))
                assert fields==package_notes[nid][1],nid
            conn.close()
        required=set()
        for note in notes.values():
            for v in note['fields'].values():
                for name in re.findall(r'<img[^>]+src=["\x27]([^"\x27]+)',v['value']):
                    name=html.unescape(name)
                    if not name.startswith(('https:','http:','data:')):required.add(name)
        missing=required-set(media.values())
        if missing:errors.append(('missing_package_media',sorted(missing)))
        assert all(k in names for k in media),'Media index entry without file'
    stats={'notes':len(notes),'cards':len(cards),'cards_by_origin':dict(collections.Counter(e['origin'] for e in p['entries'] for _ in e['clozes'])),'cards_by_group':dict(collections.Counter(e['retention_group'] for e in p['entries'] for _ in e['clozes'])),'cards_by_yield':dict(collections.Counter(e['step_yield'] for e in p['entries'] for _ in e['clozes'])),'media_files_in_package':len(media),'required_images':len(required),'package_notes_cards_fields_ids_match':True,'render_checks':len(rendered),'errors':errors,'limits':['Not imported into a clean profile or tested on Mac/Android.','Existing 31 notes retain original shared model; no original template modified.','Flags unchanged; color mapping pending.']}
    (OUT/'verification.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'rendered-cards.json').write_text(json.dumps(rendered,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(stats,ensure_ascii=False))
    if errors:raise SystemExit(1)
    # Prévia fiel do HTML já renderizado, campos locais e CSS do modelo.
    previews=['source-1487642801171','source-1474503768203','contracao-lesao','v-ulcera','v-flegmao','v-abscesso']
    source=json.loads((OUT.parent/'before-v2.json').read_text(encoding='utf-8'))
    css=next(iter(source['models'].values()))['modelStyling']['css']
    rows=[]
    for key in previews:
        entry=next(x for x in rendered if x['key']==key)
        sides=[]
        for side in ['question','answer']:
            raw=entry[side]
            raw=re.sub(r'<script\b[^>]*>.*?</script>','',raw,flags=re.S|re.I)
            def path(m):
                name=html.unescape(m[1]);local=OUT/name
                if not local.exists():local=Path(p['profile_evidence'])/name
                return 'src="'+(local.as_uri() if local.exists() else name)+'"'
            raw=re.sub(r'src=["\x27]([^"\x27]+)["\x27]',path,raw)
            sides.append('<div class="card preview">'+raw+'</div>')
        rows.append('<h2>'+key+'</h2><section>'+''.join(sides)+'</section>')
    page='<html><meta charset="utf-8"><style>'+css+'\nbody{margin:20px;background:#eee} section{display:flex;gap:15px} .preview{box-sizing:border-box;width:48%;padding:22px;background:white;position:relative} img{max-width:100%;height:auto} h2{font:18px Arial;color:#111} .preview .nebli-aula-v2{display:block!important} </style>'+''.join(rows)+'</html>'
    (OUT/'preview.html').write_text(page,encoding='utf-8')

if __name__=='__main__':main()
