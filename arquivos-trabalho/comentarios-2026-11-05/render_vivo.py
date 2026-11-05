from pathlib import Path
import json,sys,re,html
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki
A=Anki();P=json.load(open(C/'propostas.json'));new=json.load(open(C/'novo-scid-recibo.json'));ids=list(map(int,P))+[new['nid']];ns=A('notesInfo',notes=ids);problems=[]
for n in ns:
 expected=new['fields']if n['noteId']==new['nid']else P[str(n['noteId'])]['fields']
 for k,v in expected.items():
  if n['fields'][k]['value']!=v:problems.append({'nid':n['noteId'],'campo':k})
(C/'readback.json').write_text(json.dumps({'notas':len(ns),'divergencias':problems},ensure_ascii=False,indent=1));assert not problems,problems
cs=A('cardsInfo',cards=[cid for n in ns for cid in n['cards']]);M=Path(A('getMediaDirPath'));O=C/'render-vivo';O.mkdir(exist_ok=True);(O/'fonte.json').write_text(json.dumps(cs,ensure_ascii=False));res=[];shots=[]
with sync_playwright()as pw:
 b=pw.chromium.launch();pages={k:b.new_page(viewport={'width':w,'height':1000})for k,w in [('pc',1280),('cel',390)]}
 for i,c in enumerate(cs):
  for screen,page in pages.items():
   for side in ['question','answer']:
    q=O/f'{c["note"]}-{c["cardId"]}-{screen}-{side}.html';body=c[side]
    doc='<html class="'+('mobile 'if screen=='cel'else'')+'nightMode"><head><meta charset="utf-8"><base href="'+M.as_uri()+'/"><style>'+c['css']+'</style></head><body class="card card'+str(c['ord']+1)+' nightMode'+(' mobile'if screen=='cel'else'')+'">'+body+'</body></html>'
    q.write_text(doc);page.goto(q.as_uri());page.wait_for_timeout(80)
    state=page.evaluate('''()=>({overflow:document.documentElement.scrollWidth>innerWidth+2,missing:[...document.images].filter(i=>i.getAttribute('src')&&getComputedStyle(i).display!=='none'&&(!i.complete||!i.naturalWidth)).map(i=>i.getAttribute('src')),tables:[...document.querySelectorAll('table td')].filter(e=>e.getBoundingClientRect().width>0).map(e=>parseFloat(getComputedStyle(e).fontSize)),images:[...document.querySelectorAll('#extra img')].map(i=>({src:i.currentSrc||i.src,width:i.width,height:i.height}))})''')
    res.append({'nid':c['note'],'cid':c['cardId'],'lado':side,'tela':screen,**state})
    if screen=='cel'and side=='answer':
     dest=q.with_suffix('.png');page.screenshot(path=str(dest),full_page=True);shots.append((c['note'],c['cardId'],dest))
  if i%15==0:print(i+1,'/',len(cs),flush=True)
 b.close()
for start in range(0,len(shots),4):
 out=Image.new('RGB',(1600,2000),'#ddd');dr=ImageDraw.Draw(out)
 for j,(nid,cid,p)in enumerate(shots[start:start+4]):
  im=Image.open(p).convert('RGB');im.thumbnail((790,960));x=j%2*800;y=j//2*1000;out.paste(im,(x,y+25));dr.text((x,y),str(nid)+'/'+str(cid),fill='black')
 out.save(O/f'folha-{start//4+1:02}.jpg')
bad=[r for r in res if r['overflow']or r['missing']or(r['tables']and min(r['tables'])<15)]
(C/'render-vivo-conferencia.json').write_text(json.dumps({'notas':len(ns),'cards':len(cs),'faces':len(res),'falhas':bad,'resultados':res},ensure_ascii=False,indent=1));print('FINAL',len(cs),'cards',len(res),'faces',len(bad),'falhas',flush=True)
