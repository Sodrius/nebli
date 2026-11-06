"""UC07P1 Anatomia01,Gerson2026: curadoria da aula inteira; E0–E8 v15."""
import pathlib as _pl,sys as _sys,json as _json,re as _re
HERE=_pl.Path(__file__).parent
_sys.path.insert(0,str(HERE.parents[1]))
from nebli.spec_lib import ak,au,sh,kh,ORG,finalizar
PIPELINE_VERSAO=15
PIPELINE="anking-primeiro"
MODO="aula"
RUN_ID="uc07-an01-20261105v2"
SHORT="u7an01v2"
LESSON = "2026-uc07-anatomia-01-construcao-morfofuncional"
DECK="NEBLI::UC07::P1::Anatomia::01 Construção morfofuncional do sistema nervoso"
CRITERIOS="MEMORY e guias vigentes; F-20261105-CODEX-03; aulaGerson2026,Machado,veteranos."
BUSCA="Três caminhos na E4: seções celulares e embriológicas,palavra e significado nos11 acervos e NEBLI-vivo. "
AUTORAL_EXCECAO=""
SECOES_MOTIVO=""
SECOES_DA_AULA=[p.name for p in sorted((HERE/'busca/secoes').glob('*.txt')) if any(t in p.name for t in ('Cells_of_the','Neurulation','Regionalization','origins_CNS','origins_PNS','Major_Division'))]
T={x['key']:x for x in _json.loads((HERE/'alvos-planejados.json').read_text())}
SOURCES=_json.loads((HERE/'candidatos-vivos.json').read_text())
CUR=_json.loads((HERE/'curadoria.json').read_text())
AUT=[x for x in _json.loads((HERE/'autorais.json').read_text()) if not x.get('src')]
VIS=_json.loads((HERE/'visuais-reuso.json').read_text())
MEDIA={p.name:'img/'+p.name for p in (HERE/'img').glob('*.png')}
def fig(name):return '<img src="nebli-u7an01-'+name+'.png" style="width:100%;max-width:'+('600' if name=='poda' else '820')+'px;height:auto">'
CARDS=[]
SHARED_FIELDS={}
META={}
for row in CUR:
 if row['key']=='ressonancia-funcional':
  row=dict(row,img='bold-exemplo',extra='Functional MRI measures oxygenation-dependent hemodynamic changes rather than neuronal spikes directly. Colored activation is overlaid on structural MR images.');row.pop('back_image',None)
 if row['key']=='tracadores':
  row=dict(row,text='<div data-nebli-organizacao="true"><b>Traçadores neurais</b>:<br>Revelar <b>destinos dos axônios</b>: {{c1::anterógrado}}<br>Revelar <b>somas que projetam ao local</b>: {{c1::retrógrado}}</div>',img='tracadores');row.pop('back_image',None)
 target=T[row['target']];slide=target['slide'];block='A-%02d'%target['bloco'];key=row['key'];cod=row['cod']
 extra=row['extra']+'<br><br>'+fig(row['img'])
 if row.get('back_image'):extra=row['extra']+'<br><br><img src="'+row['back_image']+'" style="width:100%;max-width:820px;height:auto">'
 if 'nid' in row:
  nid=row['nid'];c=sh(nid,{'V':'verde','A':'azul','R':'rosa'}[cod[0]],block,target['relacao'],slide,cod+': '+target['relacao'])
  old=SOURCES[str(nid)]['fields'];SHARED_FIELDS[str(nid)]={'Extra':extra}
  if row.get('text'):SHARED_FIELDS[str(nid)]['Text']=row['text']+('<br><img src="'+row['front_image']+'" style="width:100%;max-width:820px;height:auto">' if row.get('front_image') else '')
  CARDS.append(c)
 else:
  front=row['text']
  if row.get('front_image'):front+='<br><img src="'+row['front_image']+'" style="width:100%;max-width:820px;height:auto">'
  opts={k:row[k] for k in ('contraste_complementar','organizador','copia_traducao_uc07','manter_focal') if k in row}
  c=ak(key,row['src'],cod,block,target['relacao'],slide,'Recupera a relação ensinada nesta lâmina: '+target['relacao'],origin=row['origin'],text=front,extra=extra,**opts)
  if row.get('manter_focal'):c['manter']=False
  CARDS.append(c)
 META[key]={'target':row['target'],'slide':slide,'bloco':block,'origem':row.get('origin','Compartilhado')}
for row in AUT:
 target=T[row['target']];front=row['text']
 if row.get('front_img'):front+='<br>'+fig(row['front_img'])
 extra=row['extra']+('' if row.get('front_img') else '<br><br>'+fig(row['img']))
 c=au(row['key'],front,row['cod'],'A-%02d'%target['bloco'],target['relacao'],target['slide'],row['ensina'],extra=extra,motivacao='m-'+row['target'],espelhos=(1479430487028,1479515890214),organizador='data-nebli-organizacao' in front)
 CARDS.append(c);META[row['key']]={'target':row['target'],'slide':target['slide'],'bloco':c['bloco'],'origem':'Autoral'}
for row in VIS:
 target=T[row['target']];nid=row['nid'];key='sh-'+str(nid)
 CARDS.append(sh(nid,'azul','A-%02d'%target['bloco'],target['relacao'],target['slide'],row['cod']+': Identificação visual distinta da recuperação da relação.'))
 SHARED_FIELDS[str(nid)]={'Extra':row['extra']}
 META[key]={'target':row['target'],'slide':target['slide'],'bloco':'A-%02d'%target['bloco'],'origem':'Kenhub'}
target=T['regioes']
CARDS.append(kh('cerebelo-visual',1792261715771,'A-aula','A-07',target['relacao'],13,'Identificação visual do cerebelo completo na vista medial,distinta da origem embrionária ou função de coordenação.',extra='The cerebellum lies dorsal to the brainstem. Its position distinguishes it from the cerebrum and from the three brainstem divisions.'))
META['cerebelo-visual']={'target':'regioes','slide':13,'bloco':'A-07','origem':'Kenhub'}
# Auditoria incremental autorizada F-20261105-CODEX-06/07.
_AUD=HERE/'auditoria-2026-11-05'
_SUP=_json.loads((_AUD/'suplemento-planejado.json').read_text())
_LIVE=_json.loads((_AUD/'campos-mantidos.json').read_text())
for _n,_f in _LIVE.items():
 if _n in SHARED_FIELDS:SHARED_FIELDS[_n].update(_f)
def _bloco(_s):return 0 if _s<=2 else 1 if _s==3 else 2 if _s<=6 else 3 if _s<=8 else 4 if _s<=10 else 5 if _s==11 else 6 if _s==12 else 7 if _s<=16 else 8 if _s<=18 else 9 if _s<=21 else 10
for _r in _SUP:
 _k=_r['key'];_s=_r['slide'];_t=_r['target'];_b='A-%02d'%_bloco(_s)
 T[_t]={'slide':_s,'bloco':_bloco(_s),'relacao':_r['relacao'],'query':_r.get('name',_k)}
 _extra=_r['extra']
 if _r['kind']!='kenhub' and not _r.get('front_img'):_extra+='<br><br>'+fig(_r['img'])
 if _r.get('nid'):
  _c=sh(_r['nid'],'azul',_b,_r['relacao'],_s,'A-aula: '+_r['ganho'] if _r.get('ganho') else 'A-aula: relação básica anteriormente omitida.')
  SHARED_FIELDS[str(_r['nid'])]={'Extra':_extra}
  if _r.get('usar_campos_origem'):SHARED_FIELDS[str(_r['nid'])].update({k:_r['fields_source'][k] for k in ('Nome PT','Imagem','MascaraP','MascaraR')})
  if _r.get('text'):SHARED_FIELDS[str(_r['nid'])]['Text']=_r['text']
 elif _r['kind']=='kenhub':
  _c=kh(_k,_r['src'],'A-aula',_b,_r['relacao'],_s,_r['ganho'],extra=_extra)
 elif _r['kind']=='autoral':
  _front=_r['text']+('<br>'+fig(_r['img']) if _r.get('front_img') else '')
  _c=au(_k,_front,'A-aula',_b,_r['relacao'],_s,_r['ensina'],extra=_extra,motivacao='m-'+_t,organizador='data-nebli-organizacao' in _front)
  AUT.append(_r)
 else:
  _front=_r['text']+('<br>'+fig(_r['img']) if _r.get('front_img') else '')
  _c=ak(_k,_r['src'],'A-aula',_b,_r['relacao'],_s,'Lacuna básica localizada na auditoria; '+_r['fonte'],origin=_r['origin'],text=_front,extra=_extra,copia_traducao_uc07=True)
  if _r['origin']=='Histology':_c.update(manter_focal=True,manter=False)
 if _r['key'] in ('rm-estruturas','nucleos-cranianos-funcao'):_c['duplicacao_ok']=_r['ensina']+' A identificação do atlas não substitui a transferência para RM; o núcleo central não é o mesmo alvo que raiz ou gânglio periférico.'
 CARDS.append(_c);META[_c['key']]={'target':_t,'slide':_s,'bloco':_b,'origem':_r['origin'] if 'origin' in _r else 'Kenhub'}

# Cor por rubrica: relações de percurso mantidas na vida; detalhes próximos ficam azuis.
PILARES={'transducao','circuito-funcional','dendritos','soma','axonio','microglia','morfologias','nucleo-ganglio','cortex-nucleos','tracadores','redes','sh-1792588686960','sh-1792588686964','sh-1792588686971','sh-1792329455992'}
for c in CARDS:
 if c['key'] in PILARES:
  if c['kind']=='compartilhado':c['cor']='verde';c['motivo']=_re.sub(r'^[A-Z]-[a-z]+:','V-pilar:',c['motivo'])
  else:c['cod']='V-pilar'
CARDS.sort(key=lambda c:int(_re.search(r'\d+',c['evid']).group()))
finalizar(CARDS,HERE,BUSCA)
# Mesmo contrato de hx_cortes: notas Histology longas são recortadas,fatos da fonte preservados.
for c in CARDS:
 if c.get('manter_focal'):
  cor=next(iter(c['flags'].values()),4)
  c['flags']={int(n):cor for n in _re.findall(r'\{\{c(\d+)::',c['text'])}
  c['recorte_de']='Histology-'+str(c['src'])
  c['manter']=False
  c['motivo']+=' Recorte da nota longa conforme F-20261003-CLAUDE-14.'

for _c in CARDS:
 if _c['key']=='pseudounipolar-trajeto':_c['duplicacao_ok']='soma recupera a identidade do centro metabólico; pseudounipolar-trajeto recupera a posição do soma fora da via direta de condução. São relações diferentes com o corpo celular,não duas definições do mesmo nome.'
 if _c['key']=='redes':_c['duplicacao_ok']='O cerebelo aparece como derivado do metencéfalo e como parte do encéfalo. Este organizador recupera sua contribuição de coordenação em uma rede visual/pré-motora/motora; origem e cooperação funcional têm ganhos distintos.'
 _os=_json.loads((HERE/'organizadores-fontes.json').read_text()).get(_c['key'])
 if _os:_c.update(organizacao_fonte=_os['arquivo'],organizacao_trecho=_os['trecho'])
EXCLUIDOS=[]
FORA_DO_RECORTE=[]
VERSO={}
DUPLICACAO={}
IMAGENS_VISTAS={k:v['intencao'] for k,v in _json.loads((HERE/'figuras-julgadas.json').read_text()).items()} if (HERE/'figuras-julgadas.json').exists() else {}
REVISAO={}
ESCOPO={'objetivo':'Base celular,organização e relação estrutura/função da aulaGerson2026.','centrais':[(k,k) for k in sorted(PILARES)],'exemplos':[],'outras_aulas':['Comunicação celular e arco reflexo','Medula,tronco e cerebelo','Neuroimagem','Córtex']}
# Decisão de todas as notas das seções do assunto,após leitura integral.
_used={str(c.get('src')) for c in CARDS if c.get('src')}
_used|={next((t.split('nid-')[-1] for t in SOURCES[str(c['nid'])]['tags'] if '::source::nid-' in t),'') for c in CARDS if c['kind']=='compartilhado' and str(c['nid']) in SOURCES}
_SELECT={r['src']:r['target'] for r in CUR if r.get('src')}
_reasons=_json.loads((HERE/'exclusoes-secoes.json').read_text()) if (HERE/'exclusoes-secoes.json').exists() else {}
for _file in SECOES_DA_AULA:
 for _line in (HERE/'busca/secoes'/_file).read_text().splitlines()[1:]:
  _m=_re.match(r'(\d{13}) ',_line)
  if _m and _m[1] not in _used:
   _nid=int(_m[1]);EXCLUIDOS.append((_nid,_reasons.get(str(_nid),'PENDENTE: decidir pertinência específica desta nota.')))
EXCLUIDOS=list(dict(EXCLUIDOS).items())

EXCLUIDOS += [(1792241266646,'Poda microglial na esquizofrenia pertence a correlação patológica específica,não à função fagocitária e sustentação glial desta aula.'),(1792338041292,'Sinapse específica do neurônio motor superior no inferior aprofunda a aula regional de vias motoras; aqui a lesão piramidal ilustra localização e cruzamento,sem estudo sináptico desta via.'),(1792340184440,'Déficit visual pós-quiasmático exige a aula de vias ópticas; não ilustra o conteúdo celular ou as divisões desta introdução.')]

# Reusos dos cortes já são IO de pergunta explícita: preservar modelo e IDs.
for _nid in (1792244864867,1792244863743,1792244863368):
 _f=SHARED_FIELDS[str(_nid)];_t=_f.pop("Text","");_f["Nome PT"]=_re.search(r"\{\{c1::(.*?)\}\}",_t)[1];_f["Pergunta"]="Qual nível do tronco encefálico está no corte?"

# Auditoria: recuperar também o lado abaixo do cruzamento,sem novos irmãos.
SHARED_FIELDS["1792329760618"]["Text"]='<div data-nebli-organizacao="true"><b>Via motora voluntária</b>, trato {{c1::corticoespinal}}:<br><b>Lesão acima da decussação</b>: déficit {{c2::contralateral}}<br><b>Lesão abaixo da decussação</b>, no trato lateral: déficit {{c2::ipsilateral}}</div>'

# Par funcional dos cornos,sem criar irmãos ou notas.
SHARED_FIELDS["1792329455992"]["Text"]='<div data-nebli-organizacao="true"><b>Cornos da medula espinal</b>:<br><b>Corpos de motoneurônios somáticos</b>: corno {{c1::anterior}}<br><b>Recepção e processamento sensitivo</b>: corno {{c1::posterior}}</div>'
