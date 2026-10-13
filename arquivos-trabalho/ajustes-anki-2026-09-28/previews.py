import html,json,re,sys
from pathlib import Path
BASE=Path(__file__).parent
P=json.loads((BASE/'plan.json').read_text())
C=json.loads((BASE/('cards-after-final.json' if (BASE/'cards-after-final.json').exists() else 'cards-after.json')).read_text())
edited={n['noteId'] for n in P['notes']}
ids=json.loads((BASE/'index.json').read_text())
sample={ids[i] for i in [1186,1190,1201,1203,1216,1225,1250,1297]}
mcat=next(c['cardId'] for c in C if 'AnKingMCAT' in c['modelName']);sample.add(mcat)
if '--finish' in sys.argv:
 edited={1790173050491,1790173050816,1790271540358,1790271540623}
 sample={ids[1225]}
jobs=[]
media=Path('/Users/davisousa/Library/Application Support/Anki2/User 1/collection.media')
for c in C:
 if c['note'] not in edited and c['cardId'] not in sample:continue
 for side in ['question','answer']:
  content=re.sub(r'(<img\b[^>]*\bsrc=["\'])([^"\']+)',lambda m:m[1]+(media/html.unescape(m[2])).as_uri() if not m[2].startswith(('data:','http:','https:')) else m[0],c[side],flags=re.I)
  for width in ([820,390] if c['cardId'] in sample else [820]):
   name=f'{c["cardId"]}-{side}-{width}'
   classes='mobile android' if width==390 else ''
   bodyclass='card nightMode'
   page=f'<!DOCTYPE html><html class="{classes}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{c["css"]}</style></head><body class="{bodyclass}"><div id="qa">{content}</div></body></html>'
   (BASE/(name+'.html')).write_text(page)
   jobs.append({'name':name,'html':name+'.html','width':width})
(BASE/'render-jobs.json').write_text(json.dumps(jobs))
print('Renderizações:',len(jobs))
