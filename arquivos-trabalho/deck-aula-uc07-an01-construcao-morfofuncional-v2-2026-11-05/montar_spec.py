from pathlib import Path
import json
R=Path(__file__).parent
original=(R/'spec.py').read_text()
if '<ucNN-' in original:(R/'spec-molde-original.txt').write_text(original)
text='''"""UC07P1 Anatomia01,Gerson2026: curadoria da aula inteira; E0–E8 v15."""
import pathlib as _pl,sys as _sys,json as _json,re as _re
HERE=_pl.Path(__file__).parent
_sys.path.insert(0,str(HERE.parents[1]))
from nebli.spec_lib import ak,au,sh,ORG,finalizar
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
SECOES_DA_AULA=[str(p.relative_to(HERE)) for p in sorted((HERE/'busca/secoes').glob('*.txt')) if any(t in p.name for t in ('Cells_of_the','Neurulation','Regionalization','origins_CNS','origins_PNS','Major_Division'))]
T={x['key']:x for x in _json.loads((HERE/'alvos-planejados.json').read_text())}
SOURCES=_json.loads((HERE/'candidatos-vivos.json').read_text())
CUR=_json.loads((HERE/'curadoria.json').read_text())
AUT=_json.loads((HERE/'autorais.json').read_text())
VIS=_json.loads((HERE/'visuais-reuso.json').read_text())
MEDIA={p.name:'img/'+p.name for p in (HERE/'img').glob('*.png')}
def fig(name):return '<img src="nebli-u7an01-'+name+'.png" style="width:100%;max-width:820px;height:auto">'
CARDS=[]
SHARED_FIELDS={}
META={}
for row in CUR:
 target=T[row['target']];slide=target['slide'];block='A-%02d'%target['bloco'];key=row['key'];cod=row['cod']
 extra=row['extra']+'<br><br>'+fig(row['img'])
 if row.get('back_image'):extra=row['extra']+'<br><br><img src="'+row['back_image']+'" style="width:100%;max-width:820px;height:auto">'
 if 'nid' in row:
  nid=row['nid'];c=sh(nid,{'V':'verde','A':'azul','R':'rosa'}[cod[0]],block,target['relacao'],slide,cod+': '+target['relacao'])
  old=SOURCES[str(nid)]['fields'];SHARED_FIELDS[str(nid)]={'Extra':extra}
  if row.get('text'):SHARED_FIELDS[str(nid)]['Text']=row['text']
  CARDS.append(c)
 else:
  front=row['text']
  if row.get('front_image'):front+='<br><img src="'+row['front_image']+'" style="width:100%;max-width:820px;height:auto">'
  opts={k:row[k] for k in ('contraste_complementar','organizador','copia_traducao_uc07') if k in row}
  c=ak(key,row['src'],cod,block,target['relacao'],slide,'Recupera a relação ensinada nesta lâmina: '+target['relacao'],origin=row['origin'],text=front,extra=extra,**opts)
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
# Cor por rubrica: relações de percurso mantidas na vida; detalhes próximos ficam azuis.
PILARES={'transducao','circuito-funcional','dendritos','soma','axonio','microglia','morfologias','nucleo-ganglio','cortex-nucleos','tracadores','redes','sh-1792588686960','sh-1792588686964','sh-1792588686971','sh-1792329455992'}
for c in CARDS:
 if c['key'] in PILARES:
  if c['kind']=='compartilhado':c['cor']='verde';c['motivo']=_re.sub(r'^[A-Z]-[a-z]+:','V-pilar:',c['motivo'])
  else:c['cod']='V-pilar'
CARDS.sort(key=lambda c:int(_re.search(r'\\d+',c['evid']).group()))
finalizar(CARDS,HERE,BUSCA)
EXCLUIDOS=[]
FORA_DO_RECORTE=[]
VERSO={}
DUPLICACAO={}
IMAGENS_VISTAS={p.name:'Figura real da aula,recorte visto e corrigido; mostra '+p.stem.removeprefix('nebli-u7an01-')+' no plano e contexto pertinentes.' for p in (HERE/'img').glob('*.png')}
REVISAO={}
ESCOPO={'objetivo':'Base celular,organização e relação estrutura/função da aulaGerson2026.','centrais':sorted(PILARES),'exemplos':[],'outras_aulas':['Comunicação celular e arco reflexo','Medula,tronco e cerebelo','Neuroimagem','Córtex']}
# Decisão de todas as notas das seções do assunto,após leitura integral.
_used={str(c.get('src')) for c in CARDS if c.get('src')}
_used|={next((t.split('nid-')[-1] for t in SOURCES[str(c['nid'])]['tags'] if '::source::nid-' in t),'') for c in CARDS if c['kind']=='compartilhado' and str(c['nid']) in SOURCES}
_SELECT={r['src']:r['target'] for r in CUR if r.get('src')}
_reasons=_json.loads((HERE/'exclusoes-secoes.json').read_text()) if (HERE/'exclusoes-secoes.json').exists() else {}
for _file in SECOES_DA_AULA:
 for _line in (HERE/_file).read_text().splitlines()[1:]:
  _m=_re.match(r'(\\d{13}) ',_line)
  if _m and _m[1] not in _used:
   _nid=int(_m[1]);EXCLUIDOS.append((_nid,_reasons.get(str(_nid),'PENDENTE: decidir pertinência específica desta nota.')))
EXCLUIDOS=list(dict(EXCLUIDOS).items())
'''
# Python3.9 accepts str.removeprefix.
(R/'spec.py').write_text(text)
print('spec v15 escrito')
