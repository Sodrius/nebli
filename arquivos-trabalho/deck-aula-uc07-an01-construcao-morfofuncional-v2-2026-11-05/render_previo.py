"""Prévia de conteúdo antes da instalação; não substitui render vivo do Anki naE8."""
from pathlib import Path
import json,re,sys,os,html
from PIL import Image,ImageDraw,ImageOps
from playwright.sync_api import sync_playwright
R=Path(__file__).parent.resolve();sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
A=Anki();P=json.loads((R/'plan.json').read_text());out=R/'render-previo';out.mkdir(exist_ok=True)
media=out/'media';media.mkdir(exist_ok=True);live=Path(A('getMediaDirPath'))
E=P['entries']+[dict(v,key='sh-'+nid) for nid,v in P['compartilhados'].items()];E.sort(key=lambda e:e['order'])
for e in E:
 for f in e['fields'].values():
  for src in re.findall(r'src="([^"]+)"',f):
   q=(R/P['media'][src]) if src in P['media'] else live/src
   d=media/src
   if not d.exists() and q.exists():d.symlink_to(q)
def khhtml(template,fields):
 for _ in range(5):
  template=re.sub(r'\{\{#([^}]+)\}\}(.*?)\{\{/\1\}\}',lambda m:m[2] if fields.get(m[1]) else '',template,flags=re.S)
 return re.sub(r'\{\{([^}]+)\}\}',lambda m:fields.get(m[1],''),template)
css={};tm={};images=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch()
 pages={name:browser.new_page(viewport={'width':width,'height':1000}) for name,width in [('pc',1000),('cel',390)]}
 for i,e in enumerate(E):
  model=e['model'];f=e['fields'];css.setdefault(model,A('modelStyling',modelName=model)['css'])
  for side in ('front','back'):
   if 'Text' in f:
    body=re.sub(r'\{\{c(\d+)::(.*?)(?:::([^}]*))?\}\}',lambda m:('<span class="cloze">'+(m[2] if side=='back' else '['+(m[3] or '...')+']')+'</span>') if m[1]=='1' else m[2],f['Text'],flags=re.S)
    if side=='back':body+='<hr><div id="extra">'+f.get('Extra','')+'</div>'
    body='<div id="text">'+body+'</div>'
   else:
    tm.setdefault(model,A('modelTemplates',modelName=model));template=next(iter(tm[model].values()))['Front' if side=='front' else 'Back'];body=khhtml(template,f)
   for screen,page in pages.items():
    arq=out/(e['key']+'-'+screen+'-'+side+'.html')
    arq.write_text('<html><head><meta charset="utf-8"><base href="'+media.as_uri()+'/"><style>'+css[model]+'\nbody{margin:18px;background:#202124;color:#eee;} .card{text-align:center;} #text{max-width:900px;margin:auto;} #text img,#extra img{max-width:100%;height:auto;} #extra{font-size:18px;} .cloze{font-weight:bold;color:#57b7ff;}</style></head><body class="card nightMode">'+body+'</body></html>')
    page.goto(arq.as_uri());page.wait_for_timeout(80);page.screenshot(path=str(out/(e['key']+'-'+screen+'-'+side+'.png')),full_page=True)
  images.append((e['key'],out/(e['key']+'-cel-back.png')))
  if i%15==0:print(i+1,'/',len(E),flush=True)
 browser.close()
for n in range(0,len(images),4):
 sheet=Image.new('RGB',(1200,1500),'#ddd');draw=ImageDraw.Draw(sheet)
 for j,(key,path) in enumerate(images[n:n+4]):
  im=Image.open(path).convert('RGB');im.thumbnail((590,710));x=(j%2)*600;y=(j//2)*750
  sheet.paste(im,(x,y+25));draw.text((x+3,y+5),key,fill='black')
 sheet.save(out/('folha-%02d.jpg'%(n//4+1)))
print(len(images),'notas;prévia pc/celular,frente/verso')
