"""Registro da leitura do executor. Rodar antes de preparar os pacotes independentes."""
from pathlib import Path
import json,re,sys
R=Path(__file__).parent;sys.path.insert(0,str(R));import spec
P=json.loads((R/'plan.json').read_text());E=P['entries']+[dict(v,key='sh-'+k) for k,v in P['compartilhados'].items()];E.sort(key=lambda e:e['order']);T=spec.T
put=lambda f,x:(R/f).write_text(json.dumps(x,ensure_ascii=False,indent=2))
bytarget={t:[e['key'] for e in E if spec.META[e['key']]['target']==t] for t in T}
# Fotografias/diagramas efetivamente vistos, inclusive versões corrigidas.
figs={}
for name,meta in json.loads((R/'figuras-preparadas.json').read_text()).items():
 figs[meta['arquivo']]={'qualidade':'boa','intencao':'Lâmina%d: figura real vista no arquivo e na prévia; usada para a relação %s.'%(meta['slide'],name)}
for name,txt in {
 'vesiculas':'AnKing1479351788638,imagem30dbfac5c5ef93cbcca926e8d30dcd25.jpg completa: três vesículas primárias,cinco secundárias e derivados adultos; nenhuma coluna ou seta cortada.',
 'vesiculas-adulto':'Mesma figura AnKing completa de desenvolvimento; ponte/cerebelo saem do metencéfalo e bulbo do mielencéfalo. Preservados todos os rótulos e desenhos.',
 'morfologias':'Bitmap139 da lâmina10,extraído integralmente sem a sobreposição da pequena imagem secundária; bipolar,multipolar e pseudounipolar com seus prolongamentos.',
 'divisoes':'Bitmaps152 e150 da lâmina11 dispostos verticalmente,sem cortar rótulos; componentes centrais e periféricos correspondem aos organizadores.',
 'funcional':'Bitmap154 da lâmina11,retirado somente o cabeçalho incorreto que dizia Central; caminhos somático/visceral e aferente/eferente completos.',
 'raizes':'Bitmap175 da lâmina12: raiz dorsal e gânglio,raiz ventral,união e ramos mistos,com rótulos completos.',
 'encefalo':'Machado3ed,fig2.8,p14(PDF25),somente figura; desenho sagital e chaves mostram cérebro,cerebelo,tronco e continuidade medular sem texto cortado ao lado.',
 'nucleos-ganglios':'Montagem de duas figuras reais: núcleos profundos da lâmina14 e gânglio dorsal da lâmina12; distingue os agregados centrais e periféricos sem usar corno como sinônimo de núcleo.',
 'transporte':'Imagemf9d262 de transporte axonal do acervo AnKing,com microtúbulos,dineína/cinesina e direções; copiada integralmente,sem desenhar esquema novo.'}.items():figs['nebli-u7an01-'+name+'.png']={'qualidade':'boa','intencao':txt}
figs['755339a3d01c11c1d48372dfa571e5f2.jpg']={'qualidade':'boa','intencao':'Arco reflexo com receptor periférico,aferente,interneurônio e motoneurônio: corresponde à transdução e ao percurso entrada/saída,sem afirmar que todo reflexo exige interneurônio.'}
figs['e9f45268de22c8894d3f362154c4880b.png']={'qualidade':'boa','intencao':'Junções comunicantes ligam duas membranas e conduzem corrente na sinapse elétrica; figura vista no arquivo original,distinta da fenda química.'}
put('figuras-julgadas.json',figs);put('imagens-vistas.json',figs)
# Todos os textos e Extras foram lidos. Cada ligação tem justificativa específica pelo alvo.
notas={
 'circuito':'Entrada aferente e saída eferente são recuperadas em conjunto; interneurônio tem lugar na integração e Extra delimita reflexo polissináptico.',
 'receptor':'Transdução transforma a modalidade do estímulo em sinal neural; não foi confundida com a condução posterior do axônio.',
 'neurulacao':'Placa,pregas,tubo e crista seguem a sequência da figura; a origem central/periférica preserva a exceção mesodérmica microglial no Extra.',
 'vesiculas':'Três primárias e cinco secundárias são recuperadas pelos irmãos originais AnKing; os15 cards do bloco embrionário testam origens e derivados,sem anomalias regionais.',
 'metencefalo':'Ponte/cerebelo no mesmo cloze contrastam com bulbo derivado do mielencéfalo; a figura conserva os destinos adultos.',
 'neuronio':'Dendritos recuperam recepção e axônio a condução de saída; não é só rótulo solto nem afirmação de direção em todas as situações especiais.',
 'soma':'O centro metabólico e síntese proteica dão significado ao corpo celular; diferente de perguntar onde o soma fica no neurônio pseudounipolar.',
 'astrocito':'Potássio,recaptação,cicatriz e prolongamentos podais cobrem suporte e capilares. Extra distingue suporte astroglial do selo físico endotelial.',
 'microglia':'Fagocitose e defesa identificam micróglia,com ontogenia de precursores do saco vitelino corrigida pelo estudo primário; glia geral dá o conjunto.',
 'mielinizadores':'Oligodendrócito central e Schwann periférico são ligados ao número de internódulos/axônios; segmentação periférica não foi confundida com envolver axônios amielínicos.',
 'mielina-clinica':'EM e forma desmielinizante deGuillain–Barré ilustram central versus periférico; não entraram tratamento,prognóstico ou critérios diagnósticos.',
 'sinapses':'Mensageiro químico e corrente via junções comunicantes são contrastados; não se afirmou que a despolarização pós-sináptica sempre dispara outro potencial.',
 'liberacao':'Potencial abre canais de cálcio no terminal pré-sináptico e promove exocitose; os quatro irmãos recuperam elementos distintos da mesma transição.',
 'saltatoria':'Nó,Ranvier,canais de sódio e regeneração do potencial nos intervalos explicam condução saltatória; mielina não é o local de geração do potencial.',
 'velocidade':'FibrasC amielínicas e pequenas oferecem o contraste de velocidade com fibras maiores; Extra explicita resistência axial e ausência de condução saltatória.',
 'fibras-sensoriais':'Propriocepção/tato e dor com frio/calor cobrem os quatro grupos; o rótuloIII/Aδ eIV/C conserva as duas nomenclaturas da tabela.',
 'primeira-dor':'O contraste Aδ/C explica a primeira dor rápida e a segunda lenta pela mielina e velocidade,sem importar vias ascendentes regionais.',
 'morfologias':'As três classes usam o mesmo eixo de disposição dos prolongamentos; umc1 recupera o grupo e a figura agora não contém a sobreposição do slide.',
 'pseudounipolar':'A posição lateral do corpo celular deixa a via periférico→central contínua; Extra evita chamar o ramo periférico de dendrito.',
 'snc-snp':'Encéfalo/medula definem o limite central e nervos/gânglios/terminações o periférico; os dois organizadores têm alvos complementares.',
 'encefalo':'Cérebro,cerebelo e tronco são o conjunto; mesencéfalo,ponte e bulbo ordenam somente o tronco. Todos os itens do conjunto ficam escondidos.',
 'somatico-visceral':'Domínio corporal ou visceral é um eixo distinto da direção aferente/eferente; entrada visceral não foi chamada de saída autônoma.',
 'autonomo':'Via eferente visceral tem relé ganglionar e efetor; simpático/parassimpático são divisões e entérico foi delimitado como circuito local.',
 'pares-nervos':'12pares cranianos e31espinais pertencem a grupos diferentes; divisão segmentar dos31 fica explicada no Extra,sem transformar este começo em uma aula regional.',
 'raizes':'Anterior/eferente e posterior/aferente são contrastes com dois índices preservados. União mista e ramos são demonstrados na figura original completa.',
 'ganglio':'Corpos sensitivos primários ficam fora da medula,no gânglio dorsal; a oclusão testa identificar a estrutura enquanto a pergunta textual cobra seu conteúdo.',
 'ramos':'Ramos posteriores e anteriores já são mistos. O organizador agrupa destinos e corrige o antigoTórax→nenhum para intercostais típicos.',
 'regioes':'As oclusões localizam encéfalo,cérebro,medula e cerebelo em vistas reais; o tronco é organizado em pergunta de conjunto e figura sagital própria. Não são as perguntas de origem embrionária nem de coordenação funcional.',
 'cinzenta-branca':'Somas/dendritos e axônios mielinizados distinguem cinzenta/branca; Extra registra que nenhuma das duas é tecido puro e há núcleos profundos.',
 'cortex-nucleos':'A figura encefálica mostra córtex e núcleos profundos; a pergunta combate explicitamente a inferência de que toda cinzenta fica na superfície.',
 'nucleo-ganglio':'O eixo é local central/periférico do agregado de somas; foram reunidas figuras com núcleos reais e gânglio para não ilustrar apenas a medula.',
 'tronco-seccoes':'Três cortes sem rótulos na frente e correspondentes identificados no verso; aqueduto,base pontina e olivas/IVventrículo sustentam o reconhecimento do nível.',
 'medula-cinzenta':'Cinzenta central e branca periférica são recuperadas em perguntas próprias já estudadas; figura medular confirma a inversão em relação ao córtex superficial.',
 'intumescencias':'Superior/cervical e inferior/lombossacral são recuperados em dois cards de acervo; Extra liga a maior população de neurônios à inervação dos membros,sem copiar o Extra errado do avulsoAnatoKing.',
 'branca-rostral':'A direção rostral agora é o alvo recuperado; o Extra liga o aumento de branca ao acúmulo das vias,melhorando a antiga pergunta restrita ao nível sacral.',
 'corno-ventral':'Localização dos corpos motores no corno anterior é o alvo; função sensitiva do posterior aparece na oposição e no desenho,sem misturar com grupos flexores dorsais dentro do anterior.',
 'somatotopia':'Lateral/distal contrasta com medial/axial; não se troca eixo mediolateral por eixo sensitivo-motor da raiz.',
 'flexores':'Dorsal/flexor e ventral/extensor valem DENTRO do corno anterior. Qualificador na frente e Extras impedem confusão com o corno posterior sensitivo.',
 'corticoespinal':'O exemplo ocupa uma nota e dois irmãos depois da arquitetura central; decussação no bulbo explica lado do déficit acima/abaixo,sem abrir ficha de síndromes motoras.',
 'broca':'Não fluência recupera a associação clínica básica do exemplo histórico; Extra situa o frontal dominante e lembra participação da rede.',
 'tracadores':'Microtúbulos dão a base e anterógrado/retrógrado recuperam direção; Extra explica como os sentidos revelam destinos ou origens de conexões.',
 'imagem-estrutural':'Os dois painéis vistos no slide22 são sagitais e mostram estruturas da linha média; a pergunta usa a mesma figura antes da resposta,sem rótuloSagital exposto.',
 'redes':'Visual,pré-motor,motor e cerebelo recuperam contribuições no mesmo ato. Planejamento não foi atribuído exclusivamente a uma região nem cerebelo a força motora direta.',
 'imagem-funcional':'Ativação relacionada à tarefa se diferencia de anatomia estrutural; Extra explicita sinal hemodinâmico e ausência de prova de causalidade.'}
put('julgamentos-alvos-executor.json',notas)
put('imagens-batem.json',{e['key']:{'veredito':'ok','porque':notas[spec.META[e['key']]['target']]+' Figura confrontada com esta frente na prévia; procedência e recorte em figuras-julgadas.json.'} for e in E})
# Texto-base para o julgamento independente; citações são recortes literais,com imagem local acessível.
fd=json.loads((R/'fontes-decl.json').read_text());fd['familias']['bibliografia']=[x for x in fd['familias']['bibliografia'] if x['arquivo']!='livros/machado-recortes-figuras.txt']+[{'arquivo':'livros/machado-recortes-figuras.txt','localizador':'Machado,cap4§2 e cap7§3.2,apenas os dois recortes conferidos','contribuicao':'Confere motivo das intumescências e plano sagital mediano da figura; sem importar conteúdo regional.','alvos':['u7an01v2-s17-intumescencias','u7an01v2-s22-imagem-estrutural']}];fd['verificacao_microglia']={'url':'https://pubmed.ncbi.nlm.nih.gov/20966214/','nota':'Ginhoux2010: precursores primitivos do saco vitelino para micróglia residente; leitura primária usada somente para corrigir a origem no Extra.'};put('fontes-decl.json',fd)
fontes={'somatico-visceral':[('fontes/veteranos-introducao.txt',json.loads((R/'organizadores-fontes.json').read_text())['somatico-visceral']['trecho'],'Apostila-guia,Aula1,p9–15,subdivisão funcional')],
'intumescencias':[('livros/machado-recortes-figuras.txt',(R/'livros/machado-recortes-figuras.txt').read_text().split('\n\n')[0],'Machado,cap4§2,intumescências')],
'imagem-estrutural':[('livros/machado-recortes-figuras.txt',(R/'livros/machado-recortes-figuras.txt').read_text().split('\n\n')[1],'Machado,cap7§3.2,face medial')],
'redes':[('livros/machado-cortex-conferencia.txt',(R/'livros/machado-cortex-conferencia.txt').read_text(),'Machado,cap26,recorte dasp253–254'),('livros/machado-cap1-3.txt','\n'.join((R/'livros/machado-cap1-3.txt').read_text().splitlines()[1130:1146]),'Machado,cap2,coordenação do movimento')],
'sh-1792697128629':[('fontes/plexos-rotulos.txt',(R/'fontes/plexos-rotulos.txt').read_text(),'Lâmina12,bitmap169,plexos e nervos intercostais'),('fontes/legendas-conferidas.txt',(R/'fontes/legendas-conferidas.txt').read_text().split('Lâmina12:')[1].split('Lâmina17:')[0],'Lâmina12,plexos e nervo espinal'),('livros/machado-recortes-figuras.txt',(R/'livros/machado-recortes-figuras.txt').read_text().split('\n\n')[0],'Machado,cap4§2,raízes que formam plexos') ]}
ns=json.loads((R/'candidatos-autorais-lidos.json').read_text());N={n['noteId']:n for n in ns};chosen=json.loads((R/'candidatos-autorais-escolhidos.json').read_text());N.update({n['noteId']:n for n in json.loads((R/'candidatos-plexos-lidos.json').read_text())});chosen['sh-1792697128629']=[1554064218108,1699448053473,1479515714285];context={}
for e in E:
 if e.get('origin')!='Autoral':continue
 key=e['key'];target=spec.META[key]['target'];cand=[]
 for nid in chosen.get(key,[]):
  n=N[nid];cand.append({'fields':{k:v['value'] for k,v in n['fields'].items() if k in ('Text','Header','Extra')},'decisao':next((a['lacuna'] for a in spec.AUT if a['key']==key),'Organizador do percurso dos ramos,distinto da identificação de raiz ou nervo.')})
 f=[{'arquivo':a,'trecho':t,'localizador':l} for a,t,l in fontes[key]]
 src=re.findall(r'src="([^"]+)"',e['fields'].get('Text','')+e['fields'].get('Extra',''))
 context[key]={'origin':'Autoral','motivacao':'m-'+target,'fontes':f,'busca':{'descricao':'Seções,palavra e significado em todos os acervos; candidatos efetivamente lidos e decisão específica abaixo.','candidatos':cand,'decisao':next((a['lacuna'] for a in spec.AUT if a['key']==key),'Os avulsos de raiz e ramos não organizam os destinos; este conjunto recupera plexos e exceção intercostal sem criar quatro perguntas.')},'contexto':{'aula':P['lesson_id'],'relacao':T[target]['relacao'],'conferencia_executor':notas[target],'imagens_locais':[str((R/'img'/s).resolve()) if (R/'img'/s).exists() else s for s in src],'previa_celular':str((R/'render-previo'/(key+'-cel-back.png')).resolve())}}
put('revisor-autorais-contexto.json',{'cards':context})
# Avulsos: consulta e resultados são os reais já lidos; não suspender notas de referência.
orgs={}
for e in E:
 if 'data-nebli-organizacao' not in e['fields'].get('Text',''):continue
 target=spec.META[e['key']]['target'];ids=[]
 for n in spec.CUR:
  if n['target']==target and n['key']!=e['key']:ids.append(n.get('nid') or n.get('src'))
 if e['key']=='intumescencias':ids=[1549136300119,1549136367353,1792328914296]
 orgs[e['key']]={'busca':'Consultas reais E4 por '+T[target]['query']+'; seções e candidatos-vivos.json lidos.','decisoes':[{'nid':nid,'acao':'manter','motivo':('Referência original preservada e avulso não adicionado ao novo deck; o organizador substitui a entrada de avulsos nesta aula.' if e['key']=='intumescencias' else 'Ganho próprio confrontado: identidade,localização visual ou território específico,distinto do eixo do organizador; preservar também o acervo de referência.')} for nid in sorted(set(ids))], 'nenhum_porquê':'Não há avulso redundante selecionado no novo deck neste eixo; notas antigas remanescentes ficam na reserva histórica,sem exclusão de estudo.'}
put('avulsos-cobertos.json',orgs)
# Despejo do plano precede instalação; inclui campos integrais sem comentários pessoais no pacote independente.
lines=[]
for e in E:
 lines += [str(e['order'])+' '+e['key']+' | '+e['origin'],e['fields'].get('Text',e['fields'].get('Nome PT','')),e['fields'].get('Extra','')]
(R/'revisao-despejo-plano.txt').write_text('\n'.join(lines))
print(len(E),'notas lidas;',len(context),'autorais no pacote;',len(orgs),'organizadores auditados')
