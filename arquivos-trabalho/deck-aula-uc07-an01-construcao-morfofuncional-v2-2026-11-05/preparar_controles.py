from pathlib import Path
import json,re,sys,importlib.util
R=Path(__file__).parent
sys.path.insert(0,str(R.parents[1]));sys.path.insert(0,str(R))
import spec
P=json.loads((R/'plan.json').read_text())
T={x['key']:x for x in json.loads((R/'alvos-planejados.json').read_text())}
META=spec.META
entries=P['entries'];shared=P['compartilhados'];allentries=entries+[dict(v,key='sh-'+nid,kind='compartilhado') for nid,v in shared.items()]
bytarget={k:[e['key'] for e in allentries if META[e['key']]['target']==k] for k in T}
bytarget['mielina-clinica']+=['oligodendrocito','schwann']
def put(file,data): (R/file).write_text(json.dumps(data,ensure_ascii=False,indent=2))
# Referência cortical consultada somente no recorte lido e necessário ao integrador da lâmina23.
full=Path('arquivos-trabalho/uc07-profundidade-2026-10-22/fontes/machado.txt').read_text().splitlines()
(R/'livros/machado-cortex-conferencia.txt').write_text('\n'.join(full[19824:19990]))
(R/'fontes/legendas-conferidas.txt').write_text('''Transcrição manual dos rótulos vistos nas figuras,sem atribuir fala oral ao professor.
Lâmina10: TIPOS DE NEURÔNIOS. BIPOLAR. MULTIPOLAR. PSEUDO-UNIPOLAR. Dendritos. Axônios. Terminal axônico. Direção do impulso.
Lâmina12: Nervos Espinhais. Plexos Nervosos. Cervical. Braquial. Lombossacral. Formação do Nervo espinhal e Componentes Funcionais. Raízes,tronco,ramos.Gânglio e Raiz Dorsal.
Lâmina17: Cervical (cabeça,pescoço,braços). Alargamento cervical. Lombar (perna inferior,tronco e pernas). Alargamento lombar.
Lâmina22: Correlações estrutura e imagens no SNC. Hemisfério cerebral. Corpo caloso. Diencéfalo. Mesencéfalo. Ponte. Cerebelo. Bulbo. Medula espinal.
Lâmina23: Áreas CONECTADAS do SNC se mobilizam para realizar funções complexas. Córtex pré-motor. Córtices visuais. Amígdala. Hipotálamo. Córtex motor. Núcleos da base. Hipocampo. Córtex parietal posterior. Cerebelo. Núcleos do tronco encefálico. Medula espinal.
''')
# Motivações conservam os campos congelados; somente vincular as notas escolhidas.
m=json.loads((R/'motivacoes.json').read_text())
for x in m['motivacoes']:x['atendida_por']=bytarget[x['id'][2:]]
put('motivacoes.json',m)
terms={'circuito':'aferente','receptor':'transdução','neurulacao':'neural','vesiculas':'mesencéfalo','metencefalo':'bulbo','neuronio':'neurônio','soma':'corpo celular','astrocito':'astrócitos','microglia':'micróglia','mielinizadores':'mielina','mielina-clinica':'mielina','sinapses':'sinapse','liberacao':'cálcio','saltatoria':'Ranvier','velocidade':'fibras','fibras-sensoriais':'grupo','primeira-dor':'dor','morfologias':'multipolar','pseudounipolar':'pseudounipolar','snc-snp':'periférico','encefalo':'encéfalo','somatico-visceral':'visceral','autonomo':'visceral','pares-nervos':'pares','raizes':'raiz','ganglio':'gânglios','ramos':'ramos','regioes':'Cérebro','cinzenta-branca':'substância','cortex-nucleos':'cinzenta','nucleo-ganglio':'corpos neuronais','tronco-seccoes':'tronco','medula-cinzenta':'medula','intumescencias':'intumescência','branca-rostral':'rostral','corno-ventral':'corno','somatotopia':'corno','flexores':'corno','corticoespinal':'corticoespinal','broca':'Broca','tracadores':'transporte','imagem-estrutural':'plano','redes':'córtex','imagem-funcional':'funcional'}
oldmap=json.loads((R/'mapa-de-profundidade.json').read_text())
items={i['id']:i for p in oldmap['passos'] for i in p['itens']}
for i in items.values():
 target=i['id'].split('-',1)[1];i['cards']=bytarget[target];i['termos']=[terms[target]]
# Seis passos de aprendizagem; preservam os44 itens e sua ordem,sem criar motivação posterior.
groups=[('Do circuito à origem das estruturas',[0,1]),('Neurônio sustentado pela glia',[2]),('Comunicação,velocidade e morfologia',[3,4]),('Classificação e ligação com a periferia',[5,6]),('Arquitetura central e somatotopia',[7,8]),('Inferir função por lesão,transporte e imagem',[9,10,11,12,13])]
steps=[]
for title,blocks in groups:
 its=[i for i in items.values() if int(i['id'].split('-')[0][1:]) in blocks]
 steps.append(dict(passo=title,itens=its))
oldmap['passos']=steps
oldmap['extras_fora_da_aula']=[dict(o_que='GFAP como marcador de astrócitos',cards=['gfap'],por_que_essencial='Pequeno complemento AnKingHY1 para reconhecer a identidade astroglial em histologia e patologia,sem importar tumores específicos ou diagnóstico clínico.',nao_e_de_outra_aula='Não há aula dedicada de histologia glial no cronogramaUC07; apenas este marcador ligado à célula ensinada entra. Outras células e doenças específicas foram excluídas.')]
put('mapa-de-profundidade.json',oldmap)
comp=json.loads((R/'compreensao-aula.json').read_text())
for i,b in enumerate(comp['blocos']):
 keys=[e['key'] for e in allentries if int(META[e['key']]['bloco'].split('-')[1])==i]
 b['cards_associados']=keys
 b['cards_exemplo']=keys if b['papel']=='exemplo' else []
 if b['papel']=='exemplo':b['principios_ilustrados']=[dict(principio=a,cards=keys) for a in b['aprender']]
 b['motivo_volume']='Há notas AnKing com recuperação em mais de um sentido e todos os irmãos foram preservados. Cada pergunta foi confrontada com a relação do bloco; não se acrescentaram fichas de doenças. O total de irmãos não equivale a novos tópicos.'
comp['reconstrucoes'][0]['cards']=sum((bytarget[x] for x in ('circuito','raizes','ganglio','saltatoria','corticoespinal')),[])
put('compreensao-aula.json',comp)
# Corrigir a árvore de inventário para apontar às chaves curadas,sem alterar as ideias previamente inventariadas.
import inventario
slides=[]
for n,kind,title,it in inventario.SLIDES:
 ns=[]
 for iid,rel,old in it:ns.append((iid,rel,bytarget[iid]))
 slides.append((n,kind,title,ns))
(R/'inventario.py').write_text('"""Inventário integral antes da seleção; vínculos a notas curadas atualizados naE5."""\nPREFIXO="u7an01v2"\nAULA="Construção morfofuncional do SN,UC07P1,Gerson2026"\nEXC="EXC: "\nSLIDES='+repr(slides)+'\nJUSTIFICATIVAS={}\nCAPITULO=[("Machado,cap1–3",[])]\nEXERCICIOS=[("Apostila-guia,Aula1,p9–15",[])]\n')
esc=json.loads((R/'escopo.json').read_text());esc['linha_logica']=[]
for j,step in enumerate(steps):
 keys=list(dict.fromkeys(k for it in step['itens'] for k in it['cards']))
 esc['linha_logica'].append(dict(passo=step['passo'],mecanismo=True,liga_ao_proximo=steps[j+1]['passo'] if j+1<len(steps) else 'A localização anatômica prepara a interpretação das aulas regionais.',cards=keys))
esc['cards_de_conexao']=['somatico-visceral','imagem-estrutural','redes']
esc['clinica_lateral']=['guillain-barre','esclerose-multipla']
esc['uso_das_fontes']={'aula':[e['key'] for e in allentries],'bibliografia':['transporte-axonal','redes','somatico-visceral'],'apostila':['somatico-visceral','intumescencia-cervical','nucleo-ganglio'],'prova':[]}
esc['provas_ausentes']={'autorizado_por':'Davi confirmou ainda não ter provas antigas e autorizou iniciar este deck com as aulas,bibliografia e veteranos disponíveis,em05/11/2026.'}
esc['provas']=[dict(id='UC07 sem provas antigas disponíveis',fora='Davi confirmou ainda não ter provas; busca no Drive não localizou gabaritos.Não atribuir recorrência nem inventar questão.')]
put('escopo.json',esc)
fd=json.loads((R/'fontes-decl.json').read_text());fd.setdefault('drive_url',fd['drive_pasta']);fd['drive_pasta']='UC07/Anatomia/01 - Construção morfofuncional do SN'
fd['familias']['bibliografia']=[x for x in fd['familias']['bibliografia'] if 'cortex' not in x['arquivo']]+[dict(arquivo='livros/machado-cortex-conferencia.txt',localizador='Machado3ed,cap26,p253–254; somente recorte para conferir a lâmina23',contribuicao='Confere planejamento pré-motor e execução motora no integrador; detalhes regionais lidos não selecionam cards.',alvos='todos')]
put('fontes-decl.json',fd)
# Fonte literal para cada organizador autoral; fonte de imagem separada de interpretação.
orgsource={'somatico-visceral':('fontes/veteranos-introducao.txt','Além disso, o Sistema Nervoso também pode ser subdividi-','Capítulo 6: Principais Estruturas'),'intumescencias':('fontes/legendas-conferidas.txt','Lâmina17:','Lâmina22:'),'redes':('livros/machado-cortex-conferencia.txt','A motricidade voluntária só é possível','3.1 ÁREA MOTORA PRIMÁRIA')}
put('organizadores-fontes.json',{k:dict(arquivo=f,trecho=(R/f).read_text().split(a,1)[1].split(b,1)[0]) for k,(f,a,b) in orgsource.items()})
# Prova de busca para os quatro autorais novos e dois preservados; candidatos reais,relevantes e lidos.
auth=[x for x in spec.AUT];chosen={
 'somatico-visceral':[1701788951760,1479351970168,1479351952248],
 'intumescencias':[1549136367353,1549136300119,1792328914296],
 'imagem-estrutural':[1540250940612,1540251271030,1481513231397],
 'redes':[1481513287366,1481562789448,1792624810919]}
put('candidatos-autorais-escolhidos.json',chosen)
rows=['chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao'];dec={};review=['# Revisão dos autorais e organizadores\n','Organizadores necessários: sim — classificação morfológica e funcional,organização central/periférica e cooperação da rede precisam de recuperação do conjunto,com critérios explícitos.\n']
for e in entries:
 target=META[e['key']]['target'];auto=e['origin']=='Autoral';row=next((x for x in auth if x['key']==e['key']),{})
 answers=re.findall(r'\{\{c\d+::(.*?)(?:::[^}]*)?\}\}',e['fields'].get('Text',''))
 ans=re.sub('<[^>]+>','',answers[0]) if answers else e.get('alvo','')
 ids=chosen.get(e['key'],[e['src']] if e.get('src') else [])
 decision=row.get('lacuna','Nota de acervo lida,recortada e traduzida para recuperar esta relação da aula,com imagem correspondente e original preservado.')
 if e.get('origin')=='Histology':decision='Conteúdo encontrado no Histology. Recorte focal autorizado emF-20261003-CLAUDE-14; original longo preservado,sem importar itens de outras aulas.'
 rows.append('\t'.join([e['key'],T[target]['relacao'],'Lâmina%d,Gerson2026;apostila-guiaAula1'%T[target]['slide'],'parcial' if auto else 'coberto',','.join(map(str,ids)),ans,decision]))
 if auto:
  dec[e['key']]={'acao':'autoral','por_que':decision,'motivo':decision,'fonte':'Lâmina%d'%T[target]['slide'],'decora':ans}
  review.append('- %s — par: §2 — tipo-informacao: %s — ensina: %s — EXEMPLAR %s — semelhança: recuperação da relação entre os componentes,com critério comum e contexto discriminante — adaptação: %s — ANTI %s — decora: %s — revisão do executor em andamento.\n'%(e['key'],row['tipo'],row['ensina'],row['exemplar'],row['lacuna'],row['anti'],ans))
(R/'busca/cobertura.tsv').write_text('\n'.join(rows)+'\n')
put('decisoes.json',dec)
(R/'REVISAO-AUTORAIS.md').write_text('\n'.join(review))
types=['chave\ttipo\tprincipio\tvisual\tpapel']
for e in allentries:
 target=META[e['key']]['target'];t=T[target]
 typ='comparacao' if t['tipo'] in ('distinguir','organizar') else 'mecanismo' if t['tipo'] in ('explicar','e-se') else 'fato-chave'
 if target=='mielina-clinica' or target=='broca':typ='base-clinica'
 if e['key'] in ('imagem-estrutural',) or META[e['key']]['origem']=='Kenhub' and e['key'].startswith('sh-179257'):typ='fato-chave'
 types.append('\t'.join([e['key'],typ,t['relacao'],'sim','fio' if e.get('origin')=='Autoral' else '']))
(R/'tipos.tsv').write_text('\n'.join(types)+'\n')
print('vínculos',len(allentries),'notas',len(items),'itens;',len(auth),'autorais novos')
