from pathlib import Path
import json,sys,re,html,os
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
R=Path(__file__).parent.parent.resolve();C=R;sys.path.insert(0,str(R.parents[1]));from nebli.decks import Anki
A=Anki();P=json.loads((R/'plan.json').read_text());receipt=json.loads((R/'receipt.json').read_text());ids=[n['nid'] for n in receipt['notes']]+list(map(int,P['compartilhados']));ns=A('notesInfo',notes=ids)
cs=A('cardsInfo',cards=[cid for n in ns for cid in n['cards']]);
valid={n['noteId']:({int(x)-1 for x in re.findall(r'\{\{c(\d+)::',n['fields']['Text']['value'])}if 'Text'in n['fields']else None)for n in ns};cs=[c for c in cs if valid[c['note']]is None or c['ord']in valid[c['note']]]
only=set(map(int,os.environ.get('ONLY_NIDS','').split(',')))if os.environ.get('ONLY_NIDS')else set()
if only:cs=[c for c in cs if c['note']in only]
M=Path(A('getMediaDirPath'));O=C/'render-vivo-auditoria';O.mkdir(exist_ok=True);(O/'fonte.json').write_text(json.dumps(cs,ensure_ascii=False));res=[];shots=[]
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
 out.save(O/((f'css-folha-{start//4+1:02}.jpg')if only else(f'folha-{start//4+1:02}.jpg')))
if only:
 prior=json.loads((C/'render-vivo-auditoria-conferencia.json').read_text());res=[x for x in prior['resultados']if x['nid']not in only]+res
bad=[r for r in res if r['overflow']or r['missing']or(r['tables']and min(r['tables'])<15)]
(C/'render-vivo-auditoria-conferencia.json').write_text(json.dumps({'notas':len(ns),'cards':len(set(x['cid']for x in res)),'faces':len(res),'falhas':bad,'resultados':res},ensure_ascii=False,indent=1));print('FINAL',len(cs),'cards',len(res),'faces',len(bad),'falhas',flush=True)
