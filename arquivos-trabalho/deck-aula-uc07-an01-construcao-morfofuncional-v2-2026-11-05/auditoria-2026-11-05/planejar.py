"""Amplia o inventário ANTES de compor o suplemento; preserva o contrato original."""
from pathlib import Path
import sys,json,re,hashlib
D=Path(__file__).resolve().parent;R=D.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
A=Anki()
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
rows=json.loads((D/'selecao-kenhub.json').read_text())+json.loads((D/'selecao-teoria.json').read_text())
# Não usar histologia periférica fina como identificação obrigatória desta introdução.
rows=[x for x in rows if x['src'] not in (1792265004509,1792265005765)]
extras=[
('velocidade-comparacao',1560656209940,9,'Entre fibras de <b>maior diâmetro e maior mielinização</b>, a condução é {{c1::mais rápida}}.','Larger axons have lower internal resistance, while myelin reduces membrane current loss. In the lecture table the relative order is Aα, Aβ, Aδ and C, from fastest to slowest.','fibras'),
('bipolar-local',1701788849706,10,'Na <b>retina</b>, neurônios com um dendrito e um axônio são {{c1::bipolares}}.','Bipolar neurons illustrate a sensory specialization. Primary sensory neurons in spinal ganglia are generally pseudounipolar, with two axonal branches and a soma beside the conduction route.','morfologias'),
('disparo-limiar',1701800847428,5,'O <b>potencial de ação</b> inicia quando a despolarização alcança o {{c1::limiar}} no segmento inicial do axônio.','Excitatory and inhibitory postsynaptic potentials are integrated before firing. They are graded; a single postsynaptic response does not necessarily trigger an action potential.','neuronio'),
('poda-sinaptica',1561072653903,3,'Na <b>maturação neural</b>, conexões pouco utilizadas são eliminadas por {{c1::poda sináptica}}.','Synaptic pruning refines developing circuits by removing excess connections. This is distinct from the programmed death of excess neurons, which is also influenced by trophic support.','glia'),
('broca-localizacao',1481513318381,20,'A <b>área de Broca</b> situa-se no giro {{c1::frontal inferior}} do hemisfério dominante.','A focal lesion can disrupt speech production while leaving other functions less affected. This is the localization principle illustrated by the lecture, rather than a catalogue of aphasia syndromes.','broca'),
('resposta-pos-sinaptica',1555081340886,7,'Um <b>potencial pós-sináptico excitatório</b> {{c1::despolariza}} a membrana e aproxima-a do limiar.','Neurotransmitter binding changes postsynaptic membrane conductance. Excitatory responses increase the probability of firing, but firing still depends on the integrated membrane potential reaching threshold.','sinapse'),
('fibras-amielinicas',1701866032096,8,'No <b>SNP</b>, axônios amielínicos também recebem suporte de células de {{c1::Schwann}}.','Schwann cells can enclose several small axons without forming compact myelin. Conduction remains continuous rather than saltatory, so absence of myelin does not imply absence of glial support.','mielina'),
]
sources={}
for key,src,slide,text,extra,img in extras:
 n=A('notesInfo',notes=[src])[0];sources[str(src)]=n
 # Mantém irmãos originais dos AnKings; recorte focal só nos Histology longos.
 if src==1555081340886:text='Um <b>potencial pós-sináptico</b> {{c2::excitatório}} {{c1::despolariza}} a célula.'
 if src==1561072653903:text='A {{c1::poda sináptica}} elimina {{c2::conexões em excesso}} durante a <b>maturação neural</b>.'
 rows.append(dict(key=key,src=src,slide=slide,text=text,extra=extra,img=img,kind='teoria',origin='Histology' if src in (1701788849706,1701800847428,1701866032096) else 'AnKing-MCAT' if src in (1560656209940,1561072653903,1555081340886) else 'AnKing',nid=None,fonte=f'Lâmina {slide}; Machado cap2–3; apostila Aula1'))
for key,src,name,slide in [('hipotalamo-visual',1540251093523,'Hipotálamo',13),('raiz-posterior-visual',1792264998268,'Raiz posterior',12)]:
 n=A('notesInfo',notes=[src])[0];sources[str(src)]=n;f={k:v['value'] for k,v in n['fields'].items()}
 imgs=''.join(f.get(k,'') for k in ('Model','Cadaver'))
 if not imgs:imgs=''.join(re.findall(r'<img[^>]+>',f['Text']))
 rows.append(dict(key=key,src=src,slide=slide,text='<b>Qual estrutura a seta indica?</b> {{c1::'+name+'}}<br>'+imgs,extra={'hipotalamo-visual':'The hypothalamus lies below the thalamus and forms the floor of the third ventricle. Its position distinguishes it from the midbrain and pituitary gland.','insula-visual':'The insula is a cortical lobe concealed within the lateral sulcus. It is not visible as an exposed lateral surface lobe unless the opercula are displaced.','raiz-posterior-visual':'The posterior root carries sensory fibers toward the spinal cord. The sensory ganglion belongs to this root; anterior and posterior rami form after the roots unite.'}[key],img='encefalo' if slide==13 else 'cinzenta' if slide==14 else 'raizes',kind='teoria',origin='AnatoKing',nid=None,fonte=f'Lâmina {slide}; apostila Aula1; fallback: nenhum IO Kenhub adequado deste alvo no corpus pesquisado.'))
authorals=[
dict(key='somatotopia-definicao',slide=18,text='A <b>correspondência ordenada entre regiões corporais e regiões do SNC</b> chama-se {{c1::somatotopia}}.',extra='An orderly body map allows a focal lesion to produce a predictable distribution of deficits.<br>Within the ventral horn, medial motor groups supply axial/proximal muscles and lateral groups supply distal limb muscles.',img='somatotopia',fonte='Lâmina18, título e mapa; apostila PDF19',ensina='Dar nome ao princípio geral que permite interpretar o mapa corporal, não apenas decorar seus pares.'),
dict(key='rm-estruturas',slide=22,text='<div data-nebli-organizacao="true"><b>RM sagital, estruturas apontadas</b>:<br><b>A</b>: {{c1::Corpo caloso}}<br><b>B</b>: {{c1::Ponte}}<br><b>C</b>: {{c1::Cerebelo}}</div>',extra='The bright callosal arch lies above the diencephalon.<br>The pons bulges ventrally in the brainstem, while the cerebellum lies dorsally.<br>The same major anatomy must be recognized across atlas drawings and magnetic resonance images.',img='rm-apontada',front_img=True,fonte='Lâmina22, RM sagital real; três setas sobre a mesma imagem',ensina='Transferir o reconhecimento de três grandes estruturas do atlas para a RM da própria aula.'),
dict(key='cone-crescimento',slide=3,text='No <b>desenvolvimento axonal</b>, o {{c1::cone de crescimento}} reconhece pistas que orientam o axônio ao alvo.',extra='The growth cone explores the local environment and responds to attractive or repulsive cues.<br>This guides axon extension, whereas radial glia provide a scaffold for neuronal cell-body migration.',img='neuronio',fonte='Apostila PDF13–14; Machado cap2§3.2 PDF22',ensina='Distinguir orientação da extremidade axonal de migração do soma; complemento básico de diferenciação neuronal.'),
dict(key='nucleos-cranianos-funcao',slide=15,text='<div data-nebli-organizacao="true"><b>Núcleos cranianos no tronco</b>:<br>Recebem <b>aferências</b>: {{c1::sensitivos}}<br>Originam <b>eferências</b>: {{c1::motores}}</div>',extra='A cranial nerve nucleus is a central group of neuronal somata.<br>Sensory nuclei receive afferent input; motor nuclei send efferent axons into cranial nerves.<br>A peripheral sensory ganglion and the nerve fibers are different structures.',img='nucleos',fonte='Lâmina15, legenda de núcleos e fibras aferentes/eferentes; Machado cap2–3',ensina='Aplicar o eixo aferente/eferente aos agregados centrais, sem exigir agora localização de todos os núcleos.'),
]
for x in authorals:x.update(kind='autoral',origin='Autoral',nid=None)
authorals=[x for x in authorals if x["key"]!="cone-crescimento"]
rows+=authorals
for x in rows:
 if x.get('nid'):x['key']='sh-'+str(x['nid'])
 if x.get('key')=='glia-radial':x['img']='glia-radial'

put(D/'suplemento-planejado.json',rows);put(D/'novas-fontes-integrais.json',sources)
# A auditoria é reentrada incremental na mesma aula instalada: nenhum spec antigo é copiado para aula nova.
m=json.loads((D/'antes-mapa-de-profundidade.json').read_text());co=json.loads((D/'antes-compreensao-aula.json').read_text());mo=json.loads((R/'motivacoes.json').read_text());mo['motivacoes']=[x for x in mo['motivacoes'] if not x['id'].startswith('m-audit-')]
for i,x in enumerate(rows):
 key=x['key'];slide=x['slide'];rel=('Reconhecer sem legenda '+x['name']+' e distinguir sua posição das estruturas vizinhas.') if x['kind']=='kenhub' else re.sub(r'\{\{c\d+::(.*?)(?:::[^}]+)?\}\}',r'\1',re.sub('<[^>]+>',' ',x['text']))
 x['relacao']=rel;x['target']='audit-'+key;x['item_id']='audit-s%02d-'%slide+key
 pi=0 if slide<=3 else 1 if slide<=6 else 2 if slide<=10 else 3 if slide<=12 else 4 if slide<=18 else 5
 m['passos'][pi]['itens'].append({'id':x['item_id'],'tipo':'decorar' if x['kind']=='kenhub' else 'organizar' if 'data-nebli-organizacao' in x.get('text','') else 'explicar','o_que':rel,'fonte':x['fonte'],'termos':[x['name']] if x['kind']=='kenhub' else [re.sub('<[^>]+>','',z.split('::')[0]) for z in re.findall(r'\{\{c\d+::(.*?)\}\}',x['text'])],'cards':[key]})
 b=next(b for b in co['blocos'] if b['laminas'][0]<=slide<=b['laminas'][-1]);b['aprender'].append(rel);b['cards_associados'].append(key)
 mo['motivacoes'].append({'id':'m-'+x['target'],'item_mapa':x['item_id'],'reconstruir':rel,'por_que_dura':x.get('ensina',x.get('ganho','Recuperar relação introdutória documentada que estava apenas no verso ou ausente; não importar o conteúdo regional inteiro.')),'depois_de':b['cards_associados'][0],'atendida_por':[key]})
co['onde_se_encaixa']+=' Reaberta em05/11: o básico visual entra agora; IO profundo de núcleos/feixes/cortes tem destino explícito nas aulas03/04. Previsto não é coberto.'
put(R/'mapa-de-profundidade.json',m);put(R/'compreensao-aula.json',co);put(R/'motivacoes.json',mo);put(D/'suplemento-planejado.json',rows)
put(R/'fontes-decl.json',dict(json.loads((R/'fontes-decl.json').read_text()),auditoria_incremental='24 lâminas revistas em imagem; apostila integral introdutória e Machado cap1–3 relidos. Escopo básico atual versus IO regional com destino em auditoria-2026-11-05/io-aulas-proprias.json.'))
print(len(rows),'novas entradas planejadas;',len(authorals),'lacunas autorais a investigar')
