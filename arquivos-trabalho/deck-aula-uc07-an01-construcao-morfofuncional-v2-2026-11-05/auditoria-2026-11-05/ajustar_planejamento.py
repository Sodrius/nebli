from pathlib import Path
import sys,json,re
D=Path(__file__).resolve().parent;R=D.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
from nebli.etapa import registrar
A=Anki()
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
rows=json.loads((D/'suplemento-planejado.json').read_text());ren={'kh-1792338033014':'sh-1792696997556','kh-1792328845991':'sh-1792572870673','kh-1792328848446':'sh-1792697128127','kh-1792244771792':'sh-1792696994258'}
for x in rows:
 for k in ('target','item_id'):
  for old,new in ren.items():x[k]=x[k].replace(old,new)
 if x['key']=='nucleos-cranianos-funcao':x['text']='<div data-nebli-organizacao="true"><b>Núcleos cranianos no tronco</b>:<br>Recebem <b>aferências dos nervos cranianos</b>: {{c1::sensitivos}}<br>Originam <b>eferências para efetores</b>: {{c1::motores}}</div>'
extra_defs=[
('sna-definicao',1701788951760,11,'A <b>eferência visceral</b> constitui o sistema nervoso {{c1::autônomo}}.','Autonomic output targets smooth muscle, cardiac muscle and glands.<br>Visceral afferents carry information inward and are not this efferent division.','funcional','Histology'),
('rm-foco-visual',1481596982488,24,'O <b>foco posterior ao olhar palavras</b>, nesta RM funcional, está no lobo {{c1::occipital}}.','Visual input recruits occipital cortical regions.<br>The other task conditions recruit different combinations of regions; activation is not confined to a single isolated center.','funcional-imagem','AnKing'),
('rm-foco-auditivo',1560651148559,24,'Ao <b>ouvir palavras</b>, o córtex {{c3::auditivo primário}} do lobo {{c1::temporal}} processa {{c2::sons}}.','Auditory cortical processing is temporal.<br>Listening to words also recruits association and language networks, so the task map is broader than primary auditory cortex alone.','funcional-imagem','AnKing-MCAT'),
]
src={}
for key,nid,slide,text,extra,img,origin in extra_defs:
 n=A('notesInfo',notes=[nid])[0];src[str(nid)]=n
 if key not in [x['key'] for x in rows]:rows.append(dict(key=key,src=nid,slide=slide,text=text,extra=extra,img=img,kind='teoria',origin=origin,nid=None,fonte='Lâmina'+str(slide)+'; apostila Aula1; Machado cap2–3',target='audit-'+key,item_id='audit-s%02d-'%slide+key))
put(D/'fontes-funcao-integrais.json',src)
m=json.loads((R/'mapa-de-profundidade.json').read_text());co=json.loads((R/'compreensao-aula.json').read_text());mo=json.loads((R/'motivacoes.json').read_text())
for x in rows:
 if x['kind']!='kenhub':
  old=x.get('relacao','');new=re.sub(r'\{\{c\d+::(.*?)(?:::[^}]+)?\}\}',r'\1',re.sub('<[^>]+>',' ',x['text']));x['relacao']=new
  for b in co['blocos']:b['aprender']=[new if q==old else q for q in b['aprender']]
 else:new=x['relacao']
 found=False
 for step in m['passos']:
  for item in step['itens']:
   if item['id']==x['item_id']:item.update(o_que=new,cards=[x['key']]);found=True
 if not found:
  slide=x['slide'];pi=0 if slide<=3 else 1 if slide<=6 else 2 if slide<=10 else 3 if slide<=12 else 4 if slide<=18 else 5
  m['passos'][pi]['itens'].append(dict(id=x['item_id'],tipo='explicar',o_que=new,fonte=x['fonte'],termos=[re.sub('<[^>]+>','',z.split('::')[0]) for z in re.findall(r'\{\{c\d+::(.*?)\}\}',x['text'])],cards=[x['key']]))
  b=next(b for b in co['blocos'] if b['laminas'][0]<=slide<=b['laminas'][-1]);b['aprender'].append(new);b['cards_associados'].append(x['key'])
  mo['motivacoes'].append(dict(id='m-'+x['target'],item_mapa=x['item_id'],reconstruir=new,por_que_dura='Relação básica ou leitura simples de imagem explícita na aula; não importa o detalhamento regional.',depois_de=b['cards_associados'][0],atendida_por=[x['key']]))
 for mot in mo['motivacoes']:
  if mot['item_mapa']==x['item_id']:mot.update(reconstruir=new,atendida_por=[x['key']])
put(D/'suplemento-planejado.json',rows);put(R/'mapa-de-profundidade.json',m);put(R/'compreensao-aula.json',co);put(R/'motivacoes.json',mo)
registrar(R,'E3','Ajuste final das relações antes da busca complementar: preservar aliases/IDs,alvo Aα específico e interpretação elementar das tarefas visuais/auditivas; nenhum IO regional novo.')
print(len(rows),'entradas complementares')
for nid,n in src.items():
 print(nid)
 for k in ('Text','Extra'):print(k,re.sub('<[^>]+>',' ',n['fields'].get(k,{}).get('value',''))[:3400])
