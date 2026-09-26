import collections,hashlib,html,json,re,sqlite3,sys,tempfile,zipfile
from pathlib import Path
from inventory import call
from prepare import ROOT,DECK

sys.stdout.reconfigure(encoding='utf-8')
plan=json.loads((ROOT/'plan.json').read_text(encoding='utf-8'))
receipt=json.loads((ROOT/'receipt.json').read_text(encoding='utf-8'))
ids=[x['new_nid'] for x in receipt['results']]
notes=call('notesInfo',notes=ids)
cards=call('cardsInfo',cards=[cid for n in notes for cid in n['cards']])
errors=[]
if len(notes)!=receipt['notes'] or len(cards)!=receipt['cards']: errors.append('Live counts differ')
if any(c['deckName']!=DECK for c in cards): errors.append('Cards in wrong deck')
if any(c['queue']==-1 for c in cards): errors.append('Unexpected suspension')
green=call('findCards',query=f'deck:"{DECK}" flag:3')
red=call('findCards',query=f'deck:"{DECK}" flag:1')
if len(green)!=plan['totals']['HY_green'] or red: errors.append('Flag mismatch')
for c in cards:
    shown=c.get('question','')+' '+c.get('answer','')
    if '{{c' in shown: errors.append(f'Unrendered cloze {c["cardId"]}')
    if any(x in shown for x in ('Faculdade:','High yield:','Low yield:')): errors.append(f'Visible meta {c["cardId"]}')
media=set()
for n in notes:
    for f in n['fields'].values():
        media.update(html.unescape(x) for x in re.findall(r'<img[^>]+src=["\x27]([^"\x27]+)',f['value'],re.I) if not x.startswith(('http:','https:','data:')))
missing_live=sorted(x for x in media if not (Path(plan['profile_evidence'])/x).exists())
if missing_live: errors.append({'missing_live_media':missing_live})
package=Path(receipt['package'])
with zipfile.ZipFile(package) as z:
    package_media=set(json.loads(z.read('media')).values())
    missing_package=sorted(media-package_media)
    if missing_package: errors.append({'missing_package_media':missing_package})
    sql_name=next((x for x in ('collection.anki21','collection.anki2') if x in z.namelist()),None)
    package_counts=None
    if sql_name:
        with tempfile.TemporaryDirectory(prefix='nebli-complemento-check-') as d:
            path=Path(d)/sql_name;path.write_bytes(z.read(sql_name))
            db=sqlite3.connect(f'{path.as_uri()}?mode=ro',uri=True)
            package_counts={'notes':db.execute('select count(*) from notes').fetchone()[0],'cards':db.execute('select count(*) from cards').fetchone()[0]}
            db.close()
        if package_counts!={'notes':len(notes),'cards':len(cards)}: errors.append({'package_counts':package_counts})
    package_summary={'files':len(z.namelist()),'media_files':len(package_media),'counts':package_counts}
origins=collections.Counter(r['origin'] for r in receipt['results'] for _ in r['cards'])
verification={'status':'passed' if not errors else 'failed','notes':len(notes),'cards':len(cards),'origins':dict(origins),'green':len(green),'red':len(red),'suspended':0,'required_media':len(media),'package':package_summary,'errors':errors,'sha256_matches':hashlib.sha256(package.read_bytes()).hexdigest()==receipt['package_sha256']}
(ROOT/'verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(verification,ensure_ascii=False,indent=2))
if errors: raise SystemExit(1)
