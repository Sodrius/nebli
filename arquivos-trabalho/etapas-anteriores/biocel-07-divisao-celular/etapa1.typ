#import "../typst-template/nebli_v2_apostila.typ": *

// ============================================================================
// etapa1.typ — Hemoglobina (1º resumo no template v3, 2026-05-30)
// ============================================================================

#intro-box[
  Antes de mergulhar na hemoglobina, vale ancorar o porquê. O oxigênio é pouco
  solúvel no plasma — em água pura, a quantidade dissolvida na pressão do nível
  do mar daria conta de alimentar, talvez, um verme pequeno. A evolução
  resolveu o problema com uma proteína carregadora dentro da hemácia: a
  hemoglobina aumenta em cerca de setenta vezes a capacidade do sangue de
  transportar O#sub[2]. E faz isso de um jeito esperto — captura o gás onde
  ele sobra (pulmão, alto pO#sub[2]) e entrega justamente onde os tecidos
  estão pedindo (músculo em exercício, foco inflamatório, qualquer ponto
  com hipóxia local). Esse comportamento bimodal não é truque: é alostería
  pura. Quem entende como ela funciona pega de bandeja a maior parte da
  clínica respiratória básica e várias doenças moleculares clássicas — anemia
  falciforme, talassemia, metahemoglobinemia, intoxicação por monóxido de
  carbono. Este resumo abre pelas peças (heme, globina, curva de ligação),
  passa pela alostería em ação (T#sym.harpoons.ltrb;R, Bohr, BPG) e fecha
  na hemoglobina no mundo real (tamponamento, variantes da molécula, gases
  que sequestram o sítio.)
]

#parte("PARTE I", "I", "As peças")

#secao("1.1", "Heme e globina")

A hemoglobina madura do adulto é um *tetrâmero* — quatro cadeias proteicas
amarradas, duas chamadas #sigla("α", [cadeia alfa da globina]) e duas
chamadas #sigla("β", [cadeia beta da globina]), montadas em dois dímeros
simétricos (#sym.alpha#sub[1]#sym.beta#sub[1] + #sym.alpha#sub[2]#sym.beta#sub[2]).
Cada uma das quatro cadeias carrega, encaixado dentro de uma bolsa
hidrofóbica, um #termo-nota[grupo prostético][molécula não-proteica que vive
ligada à proteína de forma estável, fazendo parte da identidade dela —
diferente de uma coenzima como NAD#super[+], que entra, reage e sai] chamado
heme. Esse heme só vai embora se a proteína for desmontada — não é cofator
solto que circula entre enzimas.

O heme em si é uma molécula plana, em forma de anel, chamada
#term[protoporfirina IX], que segura no centro um íon de ferro. E é esse
ferro que faz o trabalho: precisa estar no estado ferroso, Fe#super[2+],
para ligar O#sub[2]. Se oxidar para Fe#super[3+] (férrico), a hemoglobina
vira #term[metahemoglobina] — molécula intacta no formato, mas inerte para
transporte. Cada hemácia tem um sistema enzimático (a
#sigla("metHb redutase", [NADH-citocromo b5 redutase — devolve o ferro do
estado férrico ao ferroso continuamente])) que reverte essa oxidação
acidental o tempo todo. Quando esse sistema falha, ou quando uma droga
oxidante força a coisa, o paciente fica cianótico apesar de ter hemácia.

Vale comparar com a #sigla("Mb", [mioglobina — proteína monomérica do
músculo, armazena O#sub[2] em vez de transportar]), prima monomérica que
vive dentro do músculo esquelético e cardíaco. Mb tem uma só cadeia
globina, um único heme, e em vez de transportar O#sub[2] ela #term[armazena]:
capta quando o sangue chega rico em oxigênio (descanso) e libera quando o
músculo entra em demanda alta. A diferença estrutural — uma cadeia contra
quatro — é exatamente o que vai gerar tudo de interessante adiante, porque
cooperatividade só aparece em proteína oligomérica. Subunidade isolada não
tem como "perceber" o que outra subunidade está fazendo.

#figura("/figuras/hemoglobina/slide-02.png",
  num: "Figura 1.1",
  legenda-txt: [Tetrâmero da hemoglobina (#sym.alpha#sub[2]#sym.beta#sub[2])
  com quatro grupos heme encaixados nas bolsas hidrofóbicas. Compare com a
  mioglobina monomérica.],
  largura: 70%)

#callout(tipo: "confusao",
  rotulo: "Confusão prevista",
  titulo: "Grupo prostético não é coenzima")[
  #passo("aluno acha", [heme é \"cofator\" como NAD#super[+], que entra,
    reage, sai])
  #v(3pt)
  #passo("mecanismo correto", [heme é grupo prostético — fica ligado à
    proteína de forma estável. Só sai se a proteína for degradada. Coenzima
    é molécula solta que circula entre enzimas; grupo prostético é parte da
    identidade da proteína.])
]

#secao("1.2", "K#sub[d], ligante e curva")

A ligação entre proteína e ligante é um equilíbrio reversível: a
hemoglobina prende o O#sub[2] com certa força, mas pode soltar a qualquer
momento. A medida dessa força é uma constante chamada *constante de
dissociação*, ou #term[K#sub[d]]. Por convenção:

$ K_d = ([P] dot [L]) / ([P L]) $

onde $[P]$ é a proteína livre, $[L]$ é o ligante livre e $[P L]$ é o
complexo. A intuição costuma escorregar aqui — instintivamente o aluno
pensa que "K#sub[d] alto = afinidade alta" porque alto soa mais forte.
É o inverso. Se K#sub[d] é alto, o equilíbrio favorece os reagentes
separados (proteína sem ligante), então a afinidade é #term[baixa]; se
K#sub[d] é baixo, o equilíbrio favorece o complexo, então a afinidade é
#term[alta]. Vale gravar essa inversão antes de seguir, porque ela vai
voltar em toda discussão de afinidade e P#sub[50].

Operacionalmente, a forma mais usada na fisiologia é o
#termo-nota[P#sub[50]][pressão parcial de oxigênio em que metade dos
sítios de ligação está ocupada — quanto MENOR o P#sub[50], MAIOR a
afinidade]. Mioglobina tem P#sub[50] em torno de 2,8 mmHg; hemoglobina
adulta tem P#sub[50] em torno de 26 mmHg. Já dá para antecipar o que isso
significa biologicamente: mioglobina é uma armazenadora ávida (alta
afinidade, segura forte o O#sub[2] disponível); hemoglobina é uma
transportadora moderada (afinidade ajustável, pega e solta conforme a
pressão).

A curva que descreve a saturação como função do pO#sub[2] tem formato
diferente nas duas. Mioglobina: curva *hiperbólica*, sobe rápido em
pO#sub[2] baixa e satura quase totalmente já em pressão modesta.
Hemoglobina: curva *sigmoide* (em S) — começa devagar, dispara na faixa
intermediária, satura no alto. Esse formato em S é a assinatura visual
da #term[cooperatividade]: quando uma subunidade liga um O#sub[2], ela
aumenta a afinidade das outras três; conforme mais sítios são ocupados,
mais fácil fica ocupar os próximos. A curva parece relutante no começo
e ávida no meio.

#figura("/figuras/hemoglobina/slide-03.png",
  num: "Figura 1.2",
  legenda-txt: [Curva sigmoide da hemoglobina contra curva hiperbólica
  da mioglobina. O \"joelho\" da sigmoide é a zona onde a proteína está
  mudando de conformação de baixa para alta afinidade.],
  largura: 65%)

#callout(tipo: "atencao",
  titulo: "K#sub[d] alto NÃO é afinidade alta")[
  Esta é uma das inversões clássicas que mais arruínam o raciocínio
  posterior em bioquímica.
  K#sub[d] mede dissociação — se está alto, a molécula tende a se
  dissociar com facilidade, e portanto a afinidade pelo ligante é
  #term[baixa]. Para K#sub[d] mental, lembre que ele é o
  #term[inverso] de afinidade: K#sub[d] alto, afinidade baixa, e
  vice-versa. P#sub[50] segue a mesma lógica: menor P#sub[50] significa
  que basta menos O#sub[2] disponível para encher metade dos sítios —
  portanto, afinidade alta.
]

#secao("1.3", "Por que um transportador precisa de sigmoide")

A pergunta certa para entender por que a evolução escolheu uma proteína
cooperativa em vez de uma monomérica de alta afinidade é prática. Imagine
um transportador hipotético com afinidade altíssima e *constante*: ele
pegaria todo o O#sub[2] no pulmão (pO#sub[2] em torno de 100 mmHg),
perfeito; mas no tecido (pO#sub[2] ~40 mmHg) também continuaria segurando
o O#sub[2] com força e não entregaria praticamente nada. Eficiência de
entrega: péssima. Agora imagine o inverso, afinidade baixa constante: no
tecido descarregaria fácil, mas no pulmão mal carregaria. Os dois extremos
falham em transporte.

A solução evolutiva foi uma proteína #term[bimodal] — capaz de existir em
dois estados de afinidade diferente, e que transita entre os dois conforme
a pressão de O#sub[2] ao redor. Em pO#sub[2] alta (pulmão), assume
conformação de alta afinidade e carrega quase totalmente; em pO#sub[2]
baixa (tecido), volta para baixa afinidade e descarrega o suficiente para
nutrir o tecido. A curva sigmoide reflete justamente essa transição: o
pedaço íngreme do "S" (entre 20 e 60 mmHg, mais ou menos) é a zona onde
a molécula está mudando de modo. Operacionalmente, hemoglobina entrega
~25% do O#sub[2] que carrega na passagem pulmão-tecido em repouso, e bem
mais (40-50%) em exercício intenso, quando o tecido pede mais.

E essa bimodalidade só é possível porque a proteína é multimérica. Uma
subunidade isolada não tem como "saber" o que está acontecendo nas outras;
sem subunidades para conversar, não existe cooperatividade, não existe
transição em duas etapas, não existe sigmoide. Mioglobina, monomérica,
nunca poderia ser transportadora — segura o O#sub[2] forte demais e
sempre da mesma forma. Por isso ela é armazenadora local. Conclusão
operacional: hemoglobina precisa ser tetramérica não por elegância
estrutural, mas por necessidade funcional.

#recap[
  Hemoglobina é tetrâmero #sym.alpha#sub[2]#sym.beta#sub[2] com quatro
  hemes (Fe#super[2+] que liga O#sub[2]). K#sub[d] baixo = afinidade alta.
  P#sub[50] baixo = afinidade alta. Curva hiperbólica = monomérico,
  curva sigmoide = cooperativo. A sigmoide existe porque o transportador
  precisa de duas afinidades — alta no pulmão, baixa no tecido.
]

A próxima PARTE vai abrir o que a hemoglobina faz por dentro durante essa
transição entre os dois modos: como as subunidades conversam, o que muda
fisicamente na molécula, e por que sinais do tecido (pH, CO#sub[2], BPG)
conseguem deslocar a curva inteira para um lado ou para o outro.

#parte("PARTE II", "II", "A alostería ao vivo")

#secao("2.1", "Os dois estados T e R")

O que a primeira PARTE descreveu como "bimodalidade" tem nome técnico:
hemoglobina existe em equilíbrio entre dois estados conformacionais
distintos. O estado #term[T] (tenso, do inglês *tense*) é a forma de
baixa afinidade — as quatro subunidades estão amarradas entre si por
pontes salinas e interações iônicas que apertam o tetrâmero, deixando o
sítio de ligação do O#sub[2] menos acessível. O estado #term[R]
(relaxado, do inglês *relaxed*) é a forma de alta afinidade — algumas
dessas pontes salinas se quebraram, as subunidades giram cerca de 15° umas
em relação às outras, e o sítio fica mais aberto para receber o O#sub[2].

A transição entre T e R é #term[concertada]: quando a hemoglobina decide
mudar de estado, todas as quatro subunidades trocam de conformação
praticamente ao mesmo tempo, não uma de cada vez. Isso é central — é a
origem mecanística da cooperatividade. Imagine: a primeira molécula de
O#sub[2] chega numa hemoglobina em estado T e tem dificuldade de ligar
(afinidade baixa). Mas o simples ato de ligar perturba a estrutura local,
puxa o ferro para dentro do plano do anel porfirínico, e isso dispara uma
cascata de mudanças conformacionais que empurra o tetrâmero inteiro
para o estado R. Agora os outros três sítios estão em alta afinidade e
recebem O#sub[2] muito mais facilmente. É como se a primeira ligação
"abrisse a porta" para as três seguintes.

#figura("/figuras/hemoglobina/slide-05.png",
  num: "Figura 2.1",
  legenda-txt: [Transição T#sym.harpoons.ltrb;R. À esquerda, estado T
  (baixa afinidade, predominante na ausência de O#sub[2]). À direita,
  estado R (alta afinidade, predominante quando todos os sítios estão
  ligados). A transição é concertada — todas as subunidades giram juntas.],
  largura: 70%)

Importante: T não é "vazia" e R não é "cheia". As duas formas existem em
equilíbrio o tempo todo, e qualquer hemoglobina individual pode estar em
T mesmo com 1-2 O#sub[2] ligados, ou em R com nenhum O#sub[2] ligado — é
probabilístico. O que muda com o pO#sub[2] do ambiente é a #term[fração]
de hemoglobinas em cada estado: pO#sub[2] alto empurra a população para R,
pO#sub[2] baixo empurra para T. A curva sigmoide é, no fundo, a soma
desses dois equilíbrios — quantos tetrâmeros estão em R vezes a afinidade
de R, mais quantos estão em T vezes a afinidade de T.

#callout(tipo: "confusao",
  rotulo: "Confusão prevista",
  titulo: "T e R não são proteínas diferentes")[
  #passo("aluno acha", [T e R seriam codificados por genes diferentes, ou
    seriam pós-traduções distintas da mesma cadeia])
  #v(3pt)
  #passo("mecanismo correto", [T e R são o MESMO tetrâmero em duas
    conformações alternativas. A mudança é puramente espacial — quebra de
    pontes salinas, rotação de subunidades. Nenhuma ligação covalente é
    feita ou desfeita. A molécula transita centenas de vezes por segundo
    entre os dois estados.])
]

#secao("2.2", "Bohr, CO#sub[2] e o tecido que pede")

Toda a graça da hemoglobina como transportadora vem de ela conseguir
SENTIR onde está. No pulmão, ela percebe que tem muito O#sub[2] e pouco
CO#sub[2], então fica em R e carrega; no tecido, percebe o inverso e
solta. O mecanismo molecular dessa "percepção" é o que o livro chama
#term[modulação alostérica]: pequenas moléculas que se ligam à hemoglobina
em sítios diferentes do sítio do O#sub[2] e empurram o equilíbrio T#sym.harpoons.ltrb;R
para um lado ou para o outro. Os principais moduladores são H#super[+]
(prótons, ou seja, pH), CO#sub[2], #sigla("BPG", [2,3-bisfosfoglicerato —
metabólito da via glicolítica das hemácias que estabiliza o estado T
da hemoglobina]) e NO (óxido nítrico).

O #term[efeito Bohr] descreve o que H#super[+] e CO#sub[2] fazem: tecido
metabolicamente ativo gera lactato (em hipóxia) ou ácido carbônico (em
oxidação aeróbica), e o pH local cai. Esses H#super[+] extras se ligam a
resíduos de histidina (especialmente a His146 da cadeia β) e estabilizam
o estado T — afinidade cai, hemoglobina solta mais O#sub[2] localmente.
Do outro lado, no pulmão, o sangue chega com pH levemente mais alto
(porque o CO#sub[2] foi expirado e o H#super[+] foi tamponado), as
histidinas perdem seus prótons, T se desestabiliza, R volta a predominar
e a hemoglobina recarrega. Mecanisticamente, é o sinal "tecido em
necessidade ácida" sendo traduzido em "entrega mais oxigênio aqui".

O CO#sub[2] atua por DOIS caminhos. O primeiro, indireto: CO#sub[2] +
H#sub[2]O #sym.harpoons.ltrb; H#sub[2]CO#sub[3] #sym.harpoons.ltrb; H#super[+] + HCO#sub[3]#super[#sym.minus],
catalisado pela #sigla("AC", [anidrase carbônica — enzima abundante na
hemácia, equilibra CO#sub[2] e bicarbonato em milissegundos]), gera mais
prótons e amplifica o Bohr. O segundo, direto: CO#sub[2] se liga
covalentemente aos grupos amino N-terminais das cadeias da globina,
formando #term[carbamatos]. Esses carbamatos têm carga negativa e
estabilizam pontes salinas adicionais que prendem o tetrâmero em T,
contribuindo para diminuir a afinidade. Cerca de 23% do CO#sub[2]
transportado do tecido para o pulmão viaja desta forma, ligado à
hemoglobina; o restante viaja como bicarbonato no plasma (~70%) ou
dissolvido (~7%).

#figura("/figuras/hemoglobina/slide-06.png",
  num: "Figura 2.2",
  legenda-txt: [Efeito Bohr na prática. A curva de dissociação se
  desloca para a direita em pH baixo, pCO#sub[2] alto e temperatura
  elevada — ou seja, condições do tecido em atividade. Para a esquerda
  no pulmão, onde pH sobe e CO#sub[2] cai.],
  largura: 70%)

#callout(tipo: "atencao",
  titulo: "Efeito Bohr tem direção fixa")[
  pH baixo (ácido) #sym.arrow.r curva para DIREITA #sym.arrow.r afinidade
  CAI #sym.arrow.r hemoglobina ENTREGA MAIS O#sub[2]. É o sinal "tecido em
  necessidade". A inversão clássica é decorar como "ácido aumenta
  afinidade", e essa inversão arruína todo o raciocínio fisiológico
  subsequente — exercício intenso produz lactato, lactato é ácido,
  músculo precisa de MAIS O#sub[2], então a curva precisa estar
  deslocada para a direita.
]

#secao("2.3", "BPG, o ajuste fino")

O BPG é uma peça à parte, porque não vem do ambiente — é produzido
*dentro* da própria hemácia, em um ramo lateral da via glicolítica
(catalisado pela bisfosfoglicerato mutase). A concentração de BPG na
hemácia é alta, ~5 mmol/L em equilíbrio, e ela ajusta a afinidade basal
da hemoglobina ao longo de minutos a horas — escala temporal mais lenta
que o Bohr, que opera em segundos.

Mecanisticamente, BPG se encaixa em uma cavidade central entre as duas
cadeias β do tetrâmero, faz pontes iônicas com resíduos básicos das
duas cadeias e estabiliza o estado T. Resultado: na presença de BPG,
P#sub[50] sobe (afinidade cai). Sem BPG (in vitro, hemoglobina purificada
livre de metabólitos), P#sub[50] da hemoglobina cairia para algo perto
de 1 mmHg — virtualmente indescarregável. O BPG, portanto, é o que ajusta
a hemoglobina humana ao P#sub[50] fisiológico de ~26 mmHg, exatamente na
faixa em que a entrega tecidual funciona bem.

A adaptação à #term[hipóxia crônica] (altitude, doença pulmonar) é em
grande parte mediada por BPG. Quando a oferta de O#sub[2] cai, hemácias
elevam BPG ao longo de dias, P#sub[50] sobe, a curva desloca para a
direita e o tecido começa a receber proporcionalmente mais O#sub[2] do
sangue que passa. É por isso que alpinistas levam semanas para se
aclimatar — não é só ventilação, é remodelamento do BPG eritrocitário.

#callout(tipo: "atencao",
  titulo: "BPG NÃO se liga ao Fe#super[2+]")[
  Sítio do BPG fica na cavidade CENTRAL do tetrâmero, entre as cadeias
  β — bem longe dos hemes. BPG ajusta o equilíbrio T#sym.harpoons.ltrb;R
  estabilizando T, mas não compete com o O#sub[2] pelo mesmo sítio.
  Quando o O#sub[2] liga e empurra a hemoglobina para R, a cavidade
  central se fecha e o BPG é expelido — daí a competição funcional sem
  competição direta.
]

A peça final é a hemoglobina fetal (HbF, #sym.alpha#sub[2]#sym.gamma#sub[2],
discutida em mais detalhe na PARTE III). A cadeia γ tem aminoácidos
ligeiramente diferentes nessa cavidade central — falta uma das
histidinas que ligam BPG forte. Consequência: HbF é menos sensível ao
BPG, fica preferencialmente em R, tem afinidade maior pelo O#sub[2] que
a HbA da mãe, e por isso consegue extrair O#sub[2] da circulação
materna na placenta. Não é "mais hemes" nem "ferro diferente" —
é a insensibilidade ao BPG.

#recap[
  Hemoglobina alterna entre T (baixa afinidade) e R (alta afinidade);
  H#super[+], CO#sub[2] e BPG estabilizam T (curva desloca para
  direita, entrega mais); pulmão alcalino e pobre em CO#sub[2]
  estabiliza R (curva para esquerda, captura). Tudo é equilíbrio
  conformacional concertado entre as 4 subunidades.
]

A PARTE III traz o que a hemoglobina faz quando sai do bloco didático
ideal e entra em situações do mundo real — tamponamento do sangue
venoso, variantes de cadeia (HbA, HbF, HbS) e dois venenos clássicos
do sítio do heme.

#parte("PARTE III", "III", "Hemoglobina no mundo")

#secao("3.1", "Tamponamento sanguíneo")

Hemoglobina não é só transportadora de O#sub[2] — ela também é o
principal #term[tampão proteico] do sangue. Em condições fisiológicas,
ela é responsável por absorver cerca de 30% dos prótons gerados pelo
metabolismo entre uma passagem pulmonar e a próxima. O sistema
bicarbonato/CO#sub[2] cuida da maior parte do tamponamento sanguíneo,
mas é dentro da hemácia, com a hemoglobina, que ele acontece de fato.

O mecanismo é justamente o efeito Bohr olhado de outro ângulo. No
tecido, a hemoglobina chega oxigenada (em R), encontra um pH local mais
ácido (CO#sub[2] e lactato do metabolismo), as histidinas βHis146
captam H#super[+], a hemoglobina vai para T, libera o O#sub[2] e
"engole" o próton ao mesmo tempo. No pulmão, faz o caminho inverso: o
O#sub[2] entra, empurra para R, as histidinas perdem afinidade pelo
H#super[+] e devolvem o próton — que reage com bicarbonato e vira
CO#sub[2], expirado. Bohr e tamponamento são o MESMO mecanismo
molecular, em direções opostas. Não são processos separados.

O caso clássico onde esse tamponamento aparece é a #term[acidose
respiratória] aguda (retenção de CO#sub[2]): se ventilação cai, CO#sub[2]
sobe no sangue, AC gera mais H#super[+], hemoglobina absorve parte
desses prótons na sua passagem tecidual, e isso atrasa a queda do pH
sanguíneo por algumas horas, dando tempo do rim começar a compensar
excretando H#super[+] e reabsorvendo bicarbonato. Hemoglobina não
*resolve* o problema, mas oferece o buffer de curto prazo enquanto o
sistema lento (rim) acorda.

#callout(tipo: "clinica", titulo: "Por que anêmico descompensa rápido")[
  Paciente com anemia grave perde simultaneamente a capacidade de
  transportar O#sub[2] *e* a capacidade tamponante do sangue. Em
  doença pulmonar crônica, o limite de tolerância à acidose cai —
  menos hemoglobina, menos buffer, descompensação respiratória mais
  precoce. Não é só "menos hemácia, menos oxigênio"; é também "menos
  hemácia, menos margem ácido-básica".
]

#secao("3.2", "HbA, HbF e HbS")

A hemoglobina não é uma molécula única — é uma família de variantes que
muda ao longo do desenvolvimento e que pode ter mutações pontuais
relevantes na clínica. As três que importam para o 1º ano são:

#term[HbA] (#sym.alpha#sub[2]#sym.beta#sub[2]): a forma adulta normal,
~97% das hemoglobinas do adulto. É o que tudo o que se discutiu até
agora descreve.

#term[HbF] (#sym.alpha#sub[2]#sym.gamma#sub[2]): a forma fetal,
predominante até o nascimento. A diferença é a cadeia γ no lugar da
β, e a consequência funcional é exatamente a insensibilidade ao BPG
mencionada antes — γ tem aminoácidos ligeiramente diferentes na
cavidade central. HbF tem P#sub[50] em torno de 19 mmHg (afinidade
maior que a HbA), o que permite extrair O#sub[2] da circulação
materna na placenta, onde a HbA materna está descarregando. A
transição HbF #sym.arrow.r HbA acontece nos primeiros 6 meses de vida —
por volta dos 6 meses a HbF cai para menos de 1%.

#term[HbS] (#sym.alpha#sub[2]#sym.beta#sub[2]#super[S]): variante
mutante encontrada na anemia falciforme. A mutação é uma única troca
de aminoácido na cadeia β: o glutamato da posição 6 (Glu6) vira valina
(Val6). É uma mutação de ponto, herdada de forma autossômica recessiva.
A consequência molecular é absurdamente desproporcional ao tamanho da
mudança: a valina tem cadeia lateral hidrofóbica que cria um "ponto
adesivo" novo na superfície da β. Esse ponto adesivo só consegue se
encaixar em uma cavidade hidrofóbica complementar que existe na cadeia
β de OUTRA hemoglobina S — e essa cavidade fica exposta apenas no
estado T (desoxigenada). Quando uma molécula de HbS encontra outra HbS
desoxigenada, as duas se ligam pela região mutada; uma terceira
encontra a segunda, e assim sucessivamente, formando #term[polímeros
longos e rígidos] dentro da hemácia. Hemácia rígida não passa pelo
capilar, oclui, e o tecido a jusante sofre infarto. A crise vaso-oclusiva
da anemia falciforme é exatamente isso.

#figura("/figuras/hemoglobina/slide-09.png",
  num: "Figura 3.1",
  legenda-txt: [Variantes da hemoglobina. HbA adulta (#sym.alpha#sub[2]#sym.beta#sub[2]),
  HbF fetal (#sym.alpha#sub[2]#sym.gamma#sub[2]) e HbS falcêmica
  (mutação Glu6#sym.arrow.r Val6 na cadeia β). Detalhe da mutação
  pontual que gera polimerização.],
  largura: 70%)

A polimerização da HbS depende criticamente de duas coisas:
desoxigenação (HbS no estado R não polimeriza, porque a cavidade
hidrofóbica fica escondida) e concentração suficiente de HbS dentro da
hemácia. Por isso a crise é desencadeada por qualquer situação que
diminua a saturação local de O#sub[2] — exercício extenuante, febre
(aumenta demanda tecidual), desidratação (concentra a HbS),
hipoventilação na altitude, infecção. Tratamento crônico inclui
hidroxiureia, que induz síntese de HbF reativada — e como HbF não tem
o ponto adesivo da mutação, ela se intercala entre as moléculas de HbS
e interrompe a cadeia de polimerização.

#callout(tipo: "confusao",
  rotulo: "Confusão prevista",
  titulo: "Anemia falciforme não é problema de ferro")[
  #passo("aluno acha", [a doença teria a ver com Fe#super[2+] alterado,
    ou com produção insuficiente de hemoglobina (como nas anemias
    carenciais)])
  #v(3pt)
  #passo("mecanismo correto", [a estrutura primária da globina está
    mudada (Glu6#sym.arrow.r Val6 na β). O ferro está normal, em
    Fe#super[2+]; a síntese é normal; o problema é a polimerização
    espacial da molécula no estado T. É doença molecular pura — defeito
    em uma única letra do DNA.])
]

#secao("3.3", "CO e metahemoglobina")

Dois venenos clássicos do sítio do heme aparecem na clínica do 1º ano,
e os dois são frequentemente confundidos entre si.

#term[Monóxido de carbono] (CO) liga-se ao mesmo sítio do O#sub[2] no
ferro Fe#super[2+], mas com afinidade absurdamente maior — em torno de
220 vezes mais forte que o O#sub[2]. Resultado: mesmo concentração baixa
de CO no ar ambiente desloca o O#sub[2] dos hemes e bloqueia o
transporte. E tem um agravante mecanístico: cada heme ocupado por CO
estabiliza a hemoglobina em R (a alta afinidade), o que joga a curva
de dissociação para a esquerda. Os hemes restantes, que ainda têm
O#sub[2], soltam menos no tecido. Por isso a clínica é dupla — menos
O#sub[2] transportado E menos do que está transportado é entregue.
A vítima de intoxicação por CO morre por hipóxia tecidual com
saturação aparentemente normal no oxímetro de pulso (que confunde
oxiemoglobina com carboxihemoglobina, ambas têm absorbância
parecida no espectro vermelho).

#term[Metahemoglobina] é diferente. Aqui o ferro está oxidado para
Fe#super[3+] (férrico) — não há ligação de CO, e o O#sub[2] também
não consegue ligar (Fe#super[3+] não tem o elétron livre necessário
para a coordenação com O#sub[2]). A molécula está estruturalmente
intacta, o sítio existe, mas é inerte. Pequenas quantidades de
metahemoglobina aparecem o tempo todo (oxidação espontânea), e a
metHb redutase eritrocitária reverte continuamente. Quando essa
enzima falha (deficiência congênita, ou em recém-nascido com sistema
imaturo) ou quando algum oxidante exógeno satura a capacidade do
sistema (nitritos, dapsona, anestésicos locais como benzocaína em
dose alta, alguns corantes de anilina), a fração de Fe#super[3+]
sobe e o paciente fica cianótico, sem responder a oxigênio
suplementar — porque o problema não é falta de O#sub[2] no ar, é
incapacidade da molécula de ligar.

#callout(tipo: "clinica",
  titulo: "Diferenciar CO de metahemoglobinemia na cabeceira")[
  Os dois quadros podem se apresentar com cianose, taquipneia e
  confusão mental. Pistas práticas: intoxicação por CO costuma
  ocorrer em ambiente fechado com combustão (gerador a gasolina,
  aquecedor a gás, incêndio); a SpO#sub[2] no oxímetro de dedo é
  *enganadoramente normal* (~95-100%) — porque o aparelho não
  distingue HbO#sub[2] de HbCO. Metahemoglobinemia costuma surgir
  após exposição a oxidante (anestésico tópico, nitritos);
  o sangue tem cor *chocolate* característica (versus vermelho-vivo
  da HbCO); SpO#sub[2] pode ficar entre 80-90% mesmo com pO#sub[2]
  arterial normal na gasometria. Tratamento: CO #sym.arrow.r oxigênio
  100% (ou hiperbárico em casos graves); metHb #sym.arrow.r azul de
  metileno (cofator que reduz Fe#super[3+] de volta a Fe#super[2+]).
]

#callout(tipo: "atencao",
  titulo: "CO desloca a curva para a esquerda, não para a direita")[
  A intuição errada — "se prejudica oxigenação, deveria entregar mais
  para compensar" — é exatamente o oposto do que acontece. CO ligado
  em alguns hemes ESTABILIZA o estado R, AUMENTA a afinidade dos
  hemes restantes, e por isso a curva desloca para a ESQUERDA. O
  tecido recebe ainda menos O#sub[2] do pouco que está sendo
  transportado. É efeito duplo: transporte caído + entrega prejudicada.
]

#conclusao-box[
  A hemoglobina é, em uma frase, uma proteína #term[bimodal
  multimérica] que existe para entregar O#sub[2] onde ele é necessário.
  O princípio unificador é a cooperatividade entre 4 subunidades, e o
  mecanismo nuclear é a transição concertada entre os estados T e R,
  modulada por sinais do tecido (pH, CO#sub[2], BPG, temperatura). Toda
  a clínica relevante para o 1º ano é variação sobre esse tema: anemia
  falciforme quebra a estrutura quaternária via mutação pontual da β;
  metahemoglobinemia destrói a funcionalidade do ferro sem mexer no
  formato; CO sequestra o sítio e ainda aumenta a afinidade dos hemes
  vizinhos, prejudicando a entrega. O próximo passo natural, em
  metabolismo, é entender de onde vem a energia que o tecido usa após
  receber esse O#sub[2] — entramos na cadeia respiratória mitocondrial,
  onde o O#sub[2] vira aceptor final de elétrons e produz a água que
  fecha o ciclo.
]
