"""Prévia dos campos propostos com CSS real; análise de layout em todas as faces."""
from pathlib import Path
import json,re,sys,html,os
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki
A=Anki();P=json.load(open(C/'propostas.json'));N={n['noteId']:n for n in json.load(open(C/'notas-antes-com-similares.json'))};M=Path(A('getMediaDirPath'));O=C/'render-previo';O.mkdir(exist_ok=True);css={};res=[];shots=[]
new=json.load(open(C/'novo-scid.json'));source=N[1791625424233];N[0]=dict(source,noteId=0);P['0']={'fields':new['fields']}
with sync_playwright()as pw:
 b=pw.chromium.launch();pages={key:b.new_page(viewport={'width':width,'height':1000})for key,width in [('pc',1280),('cel',390)]}
 for i,(nid,p)in enumerate(P.items()):
  n=N[int(nid)];f={k:v['value']for k,v in n['fields'].items()};f.update(p['fields']);t=f['Text'];extra=f.get('Extra','');model=n['modelName'];css.setdefault(model,A('modelStyling',modelName=model)['css']);indices=sorted(set(re.findall(r'\{\{c(\d+)::',t)))
  def media(m):
   name=html.unescape(m[1]);q=C/'img'/name
   if not q.exists():q=M/name
   return 'src="'+q.as_uri()+'"'
  for idx in indices:
   for side in ['front','back']:
    def cl(m):
     target=m[2].split('::');ans=target[0];hint='::'.join(target[1:])
     return '<span class="cloze">'+(ans if side=='back' else '['+(hint or '...')+']')+'</span>' if m[1]==idx else ans
    body=re.sub(r'\{\{c(\d+)::(.*?)\}\}',cl,t,flags=re.S)
    body='<div id="text">'+body+'</div>'
    if side=='back':body+='<hr><div id="extra">'+extra+'</div>'
    body=re.sub(r'src="([^"]+)"',media,body)
    for screen,page in pages.items():
     q=O/f'{nid}-c{idx}-{screen}-{side}.html';q.write_text('<html><head><meta charset="utf-8"><style>'+css[model]+'\nbody{margin:16px;background:#202124;color:#eee}.card{text-align:center}#text{max-width:950px;margin:auto}#extra{font-size:18px}img{max-width:100%;height:auto}.cloze{font-weight:bold;color:#59b9ff}table{width:100%;table-layout:fixed;font-size:15px;border-collapse:collapse}td,th{padding:5px;overflow-wrap:anywhere;border:1px solid #888}</style></head><body class="card nightMode">'+body+'</body></html>')
     page.goto(q.as_uri());page.wait_for_timeout(20)
     state=page.evaluate('''()=>({overflow:document.documentElement.scrollWidth>innerWidth+2,missing:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),width:innerWidth})''')
     res.append({'nid':int(nid),'indice':idx,'lado':side,'tela':screen,**state})
     if idx==indices[0]and screen=='cel'and side=='back':
      path=q.with_suffix('.png');page.screenshot(path=str(path),full_page=True);shots.append((nid,path))
  if i%15==0:print(i+1,'/',len(P),flush=True)
 b.close()
for start in range(0,len(shots),4):
 out=Image.new('RGB',(1600,2000),'#ddd');dr=ImageDraw.Draw(out)
 for j,(nid,p)in enumerate(shots[start:start+4]):
  im=Image.open(p).convert('RGB');im.thumbnail((790,960));x=j%2*800;y=j//2*1000;out.paste(im,(x,y+25));dr.text((x,y),nid,fill='black')
 out.save(O/f'folha-{start//4+1:02}.jpg')
(C/'render-conferencia.json').write_text(json.dumps({'faces':len(res),'notas':len(P),'falhas':[r for r in res if r['overflow']or r['missing']],'resultados':res},ensure_ascii=False,indent=1));print('FINAL',len(res),'faces;',sum(r['overflow']or bool(r['missing'])for r in res),'falhas',flush=True)
