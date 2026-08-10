#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Uma célula da sua adrenal libera adrenalina e, segundos depois, o glicogênio do seu fígado começa a se desmontar. Entre um evento e outro há metros de distância e uma diluição brutal: a adrenalina chega ao hepatócito numa concentração da ordem de nanomolar — algo como uma gota num tanque. Mesmo assim, a resposta é rápida, grande e específica. Essa desproporção entre a fraqueza do sinal e o tamanho do efeito é o problema central desta apostila.

  A ideia que costura tudo é a seguinte: *um hormônio não carrega energia nem executa trabalho — ele carrega apenas informação, e toda a maquinaria da sinalização existe para resolver dois problemas dessa informação.* O primeiro é o *reconhecimento*: como garantir que só a célula certa responda, se o hormônio circula por todo o corpo? A resposta é o receptor de alta afinidade, e é ele — não o hormônio — que define quem é célula-alvo. O segundo é a *amplificação*: como um punhado de moléculas produz uma resposta metabólica maciça? A resposta é a cascata, em que cada etapa multiplica a anterior.

  A partir daí, uma única propriedade química organiza o resto: *ser ou não ser solúvel em água*. Hormônio hidrossolúvel não atravessa a membrana, então seu receptor fica na superfície, e a resposta é rápida e transitória — modifica enzimas que já existem. Hormônio lipossolúvel atravessa, seu receptor está dentro da célula, e a resposta é lenta e duradoura — muda quais proteínas a célula fabrica. A PARTE I monta essa lógica geral; a PARTE II a percorre pelo lado rápido (insulina, glucagon, catecolaminas e o controle da glicemia); a PARTE III pelo lado lento (tireoidianos, esteroides e o cortisol).
]

#parte-title("PARTE I — A lógica do sinal hormonal", primeira: true)

#subtopico("1.1 — Três alavancas para mudar a velocidade de uma via")

Antes de falar em hormônio, vale perguntar o que exatamente se quer controlar. Regular o metabolismo significa interferir na *velocidade* das reações químicas do organismo — acelerar uma via, frear outra — e o efeito nunca fica isolado: mexer num ponto propaga consequências por todas as vias conectadas.

A célula dispõe de três alavancas para isso, e elas se distinguem pela escala de tempo em que agem. A primeira é a #termo-nota[modulação alostérica][ligação de um metabólito a um sítio da enzima diferente do sítio ativo, mudando a conformação e, com ela, a atividade — resposta imediata, sem gasto de energia e sem alterar a quantidade de enzima]: o próprio substrato ou um metabólito da via se liga à enzima e muda sua atividade em *milissegundos*. A segunda é a *modificação covalente*, tipicamente a fosforilação — uma quinase transfere um fosfato do ATP para a enzima, uma fosfatase o retira, e a enzima alterna entre duas formas com atividades diferentes; isso leva *segundos a minutos*. A terceira é o controle da *expressão gênica*: muda-se quanta enzima existe na célula, o que leva *horas*.

Guarde essa graduação, porque ela vai reaparecer o tempo todo: os hormônios de ação rápida operam pela segunda alavanca, e os de ação lenta pela terceira.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-03.png",
  largura: 90%,
  legenda: [As três alavancas de regulação, da mais rápida à mais lenta. À esquerda, a cinética alostérica (curva sigmoide) contrastada com a michaeliana; ao centro, o par quinase/fosfatase ligando e desligando a enzima por fosforilação; à direita, o controle da expressão. Toda a apostila mora nas duas últimas.])

#subtopico("1.2 — O que faz de uma molécula um hormônio")

Um hormônio é uma biomolécula produzida numa parte do corpo que regula funções *a distância*, age em quantidades muito baixas e atua sempre por meio de um receptor na célula-alvo. Essa última cláusula é a que costuma passar batido e é a mais importante: o hormônio banha indistintamente todas as células do corpo, mas só produz efeito naquelas que possuem o receptor. Uma célula sem o receptor simplesmente não é célula-alvo — o hormônio passa por ela sem consequência.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-07.png",
  largura: 60%,
  legenda: [A célula secretora libera o hormônio no meio; ele alcança as duas células abaixo igualmente. A de cima responde porque tem receptor; a de baixo não é alvo, apesar de estar exposta à mesma concentração. Quem define o alvo é o receptor, não o hormônio.])

#confusao-prevista(
  titulo: "\"O hormônio escolhe o órgão-alvo\"",
  aluno_acha: [aluno imagina o hormônio sendo endereçado a um destino, como uma carta],
  mecanismo: [o hormônio é distribuído pelo sangue para o corpo inteiro, sem endereço. A especificidade é *do lado do receptor*: expressar ou não o receptor é o que torna um tecido responsivo. É por isso que o mesmo hormônio pode ter efeitos diferentes em tecidos diferentes — os receptores e as vias acopladas a eles é que mudam.],
)

Uma segunda classificação, independente da química, olha para a *distância percorrida*. Na sinalização *endócrina*, a molécula cai na corrente sanguínea e age longe. Na *parácrina*, difunde-se no interstício e age nas células vizinhas. Na *autócrina*, age na própria célula que a produziu. É o mesmo princípio de mensagem química, mudando só o alcance.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-10.png",
  largura: 65%,
  legenda: [Endócrino (pelo sangue, a distância), parácrino (na vizinhança) e autócrino (na própria célula). A diferença é de alcance, não de mecanismo.])

Vale registrar também o contraste com o neurotransmissor, porque a fronteira é menos nítida do que parece: adrenalina e noradrenalina são *as duas coisas* — neurotransmissores na sinapse e hormônios quando lançados na circulação pela medula adrenal. A diferença operacional é de geografia e de tempo: o neurotransmissor age numa fenda de nanômetros e em milissegundos; o hormônio, a metros de distância e em segundos a horas.

#subtopico("1.3 — As classes químicas e a regra mestra da solubilidade")

Os hormônios se agrupam por estrutura química em algumas famílias: *peptídicos* (insulina, glucagon), *catecolaminas* (adrenalina, noradrenalina, dopamina), *eicosanoides* (prostaglandinas, tromboxanos, leucotrienos), *esteroides* (cortisol, aldosterona, testosterona, estradiol, progesterona), *tireoidianos* (T3, T4), além de vitamina D, retinoides e óxido nítrico.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-09.png",
  largura: 85%,
  legenda: [As quatro famílias químicas destacadas na aula. Repare no contraste visual que interessa: eicosanoides e esteroides são esqueletos de carbono apolares; o peptídico (insulina) é uma cadeia de aminoácidos com carga.])

Essa lista, decorada, não ensina nada. O que ela vale é como atalho para a propriedade que realmente decide o comportamento: a *solubilidade*. E aqui está a regra mestra da apostila inteira, que vale a pena enunciar de forma limpa:

#mini-resumo[Hormônio *hidrossolúvel* (peptídico, catecolamina) não atravessa a membrana → receptor *na superfície* → segundo mensageiro → modifica enzimas preexistentes → resposta em *segundos*, transitória. Hormônio *lipossolúvel* (esteroide, tireoidiano, vitamina D, retinoide) atravessa a membrana → receptor *intracelular/nuclear* → liga-se ao DNA → muda a quantidade de proteína → resposta em *horas*, duradoura.]

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-15.png",
  largura: 60%,
  legenda: [Os dois mecanismos gerais lado a lado. À esquerda, o hormônio peptídico/amínico age *sem entrar* na célula, via segundo mensageiro, alterando a atividade de enzima preexistente. À direita, o esteroide/tireoidiano entra, encontra o receptor e altera a transcrição — muda a *quantidade* de proteína nova.])

Uma consequência prática que decorre direto dessa regra, e que a aula não enuncia mas está implícita: hormônio lipossolúvel não é solúvel no plasma, então precisa de *proteína carreadora* no sangue e tem meia-vida longa; hormônio hidrossolúvel viaja livre e é degradado rápido. É por isso que o cortisol circula ligado à globulina ligadora de corticosteroide, enquanto a adrenalina dura menos de um minuto.

#confusao-prevista(
  titulo: "Tireoidiano é derivado de aminoácido, então deveria agir na membrana",
  aluno_acha: [aluno classifica T3/T4 junto com as catecolaminas, porque ambos vêm da tirosina],
  mecanismo: [a origem biossintética é a mesma (tirosina), mas o que decide o mecanismo é a *solubilidade do produto final*. A iodação torna T3 e T4 suficientemente lipofílicos para atravessar a membrana, e eles agem em *receptor nuclear*, como esteroides. As catecolaminas permanecem hidrossolúveis e agem em *receptor de superfície*. Mesmo precursor, mecanismos opostos.],
)

#subtopico("1.4 — Os tipos de transdutor de sinal")

Quando o receptor está na superfície, o problema passa a ser converter um evento de ligação do lado de fora em um evento bioquímico do lado de dentro. Existem alguns desenhos de transdutor que resolvem isso, e a aula os apresenta em conjunto.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-13.png",
  largura: 90%,
  legenda: [Os seis tipos. (1) Receptor acoplado à proteína G — o ligante ativa uma proteína G que regula uma enzima geradora de segundo mensageiro. (2) Receptor tirosina-quinase — o ligante ativa a atividade quinase por autofosforilação, e a cascata pode terminar num fator de transcrição. (3) Guanilil-ciclase — gera cGMP. (4) Canal iônico com portão — abre ou fecha, mudando concentração iônica ou potencial de membrana. (5) Receptor de adesão — liga matriz extracelular e citoesqueleto. (6) Receptor nuclear — o único intracelular, regula transcrição diretamente.])

A comparação mais útil não é a lista, e sim a *escala de tempo* de cada um, porque ela explica para que serve cada desenho:

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-14.png",
  largura: 80%,
  legenda: [Canal iônico controlado por ligante: milissegundos (receptor nicotínico da ACh). Receptor acoplado à proteína G: segundos (receptor muscarínico). Receptor ligado a quinase: horas (receptores de citocinas). Receptor nuclear: horas (receptor de estrógenos). O desenho do transdutor é escolhido pela urgência da resposta.])

#subtopico("1.5 — Alta afinidade e amplificação: por que pouco hormônio faz muito efeito")

Duas propriedades tornam o sistema viável. A primeira é a *alta afinidade*: os receptores hormonais ligam seu ligante com constantes de dissociação na faixa nanomolar ou menor, o que permite responder a concentrações ínfimas — exatamente a faixa em que os hormônios circulam.

A segunda é a *amplificação em cascata*, e é ela que resolve a desproporção do parágrafo de abertura. Cada etapa da cascata é catalítica: uma molécula ativada na etapa anterior ativa muitas na seguinte. Um único hormônio ligado ativa várias proteínas G; cada proteína G ativa uma adenilato-ciclase que produz *muitas* moléculas de AMPc; cada AMPc contribui para ativar PKA; cada PKA fosforila muitos substratos. O resultado é um ganho de várias ordens de grandeza entre o número de moléculas de hormônio e o número de moléculas de produto final.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-16.png",
  largura: 70%,
  legenda: [A pirâmide da amplificação: cada nível é mais largo que o anterior. À esquerda, o mecanismo elementar — o receptor ativa a proteína G, que troca GDP por GTP e ativa a enzima efetora. É a repetição catalítica desse passo que gera o ganho.])

#confusao-prevista(
  titulo: "Amplificação é a mesma coisa que ter muitos receptores",
  aluno_acha: [aluno explica o efeito grande dizendo que a célula tem muitos receptores],
  mecanismo: [ter muitos receptores aumenta a *sensibilidade* (a chance de captar o sinal), não o ganho. A amplificação vem da natureza *catalítica* de cada etapa: uma enzima ativada trabalha repetidamente enquanto estiver ativa, produzindo muitos produtos. Sem catálise em cascata, mil receptores dariam mil eventos — com cascata, dão milhões.],
)

#subtopico("1.6 — Onde um sistema hormonal pode ser regulado (e onde pode falhar)")

Vale fixar o percurso completo de um hormônio, porque cada seta é um ponto regulável e também um ponto onde uma doença ou um fármaco pode agir:

#mini-resumo[Biossíntese → Estocagem → Secreção → Transporte → Reconhecimento → Resposta → Degradação.]

Esse mapa será útil adiante: as sulfonilureias agem na *secreção*; a resistência insulínica, no *reconhecimento/resposta*; a doença de Addison, na *biossíntese*; os disruptores endócrinos, no *reconhecimento*; as deiodinases, na conversão que antecede a *resposta*.

#parte-title("PARTE II — O lado rápido: hidrossolúveis e o controle da glicemia")

#subtopico("2.1 — Insulina: uma proteína que precisa ser cortada para existir")

A insulina madura é formada por duas cadeias — A, com 21 resíduos, e B, com 30 — unidas por pontes dissulfeto. Ela não é sintetizada assim. O ribossomo produz uma cadeia única, a *pré-pró-insulina*; a remoção do peptídeo-sinal no retículo endoplasmático gera a *proinsulina*, que se dobra e forma as pontes dissulfeto; e um corte proteolítico posterior remove um segmento interno — o *peptídeo C* — deixando as cadeias A e B ligadas apenas pelas pontes já formadas.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-22.png",
  largura: 85%,
  legenda: [O processamento pós-traducional da insulina. Repare na ordem que importa: as pontes dissulfeto se formam *enquanto* a cadeia ainda é contínua (proinsulina) — é o peptídeo C que mantém as cadeias A e B alinhadas para que as pontes certas se formem. Só depois ele é removido. À direita, o trajeto celular: retículo → vesícula de transporte → Golgi → vesícula secretora.])

A lógica desse arranjo merece ser explicitada, porque é o melhor exemplo da aula de por que o processamento existe: se as cadeias A e B fossem sintetizadas separadas, seria improvável que se encontrassem e formassem as pontes corretas. O peptídeo C é um *gabarito temporário* — descartável depois que a estrutura está pronta. Como ele é secretado em quantidade equimolar à insulina e não é extraído pelo fígado na primeira passagem, a dosagem de peptídeo C serve para estimar a produção *endógena* de insulina, algo que a dosagem da insulina não faz quando o paciente usa insulina exógena.

#subtopico("2.2 — A célula β como sensor de glicose")

O mecanismo de secreção da insulina é um dos trechos mais cobrados da aula, e ele é inteiramente encadeado — vale seguir passo a passo, porque cada elo tem um motivo.

A glicose entra na célula β pelo *GLUT2*, um transportador independente de insulina e de baixa afinidade (K#sub[m] alto). Dentro, é fosforilada pela *glicoquinase*, também de K#sub[m] alto. Essas duas escolhas não são acidentais: por terem baixa afinidade, ambos só operam com velocidade apreciável quando a glicose está *alta*. É isso que torna a célula β um medidor de glicemia em vez de um consumidor constante de glicose.

O metabolismo dessa glicose aumenta a razão ATP/ADP. O ATP *fecha* o canal de K#super[+] sensível a ATP (K#sub[ATP]). Com o efluxo de potássio interrompido, a membrana *despolariza*. A despolarização abre canais de *Ca#super[2+] dependentes de voltagem*, e o influxo de cálcio dispara a exocitose das vesículas contendo insulina.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-26.png",
  largura: 85%,
  legenda: [A cadeia completa na célula β: GLUT2 → glicólise e oxidação → ↑ATP → fechamento do canal K#sub[ATP] → despolarização → abertura do canal de Ca#super[2+] voltagem-dependente → exocitose da insulina. Cada seta é um alvo farmacológico em potencial.])

#confusao-prevista(
  titulo: "O ATP abre o canal de potássio",
  aluno_acha: [aluno associa \"ATP\" a \"ativação\" e supõe que o canal abre],
  mecanismo: [o nome do canal é \"sensível a ATP\", e o efeito do ATP é *fechá-lo*. O canal está aberto em repouso, deixando K#super[+] sair e mantendo a membrana polarizada. Fechar o canal é o que despolariza. A regra prática: ATP alto = glicose alta = fechar o canal = secretar insulina.],
)

#subtopico("2.3 — Glicoquinase e hexoquinase: a mesma reação, dois propósitos")

A fosforilação da glicose a glicose-6-fosfato é feita por enzimas diferentes conforme o tecido, e o contraste entre elas é um dos melhores exemplos de como a cinética serve à fisiologia.

As *hexoquinases* (músculo, cérebro, maioria dos tecidos) têm K#sub[m] baixo — alta afinidade — e portanto já estão praticamente saturadas na glicemia basal. Elas garantem que o tecido capte glicose mesmo quando ela está escassa, e são inibidas pelo próprio produto. A *glicoquinase* (fígado e célula β) tem K#sub[m] alto — baixa afinidade — e por isso sua velocidade continua subindo conforme a glicemia sobe acima do basal.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-25.png",
  largura: 60%,
  legenda: [Na glicemia basal (linha tracejada), a hexoquinase já está no platô: capta glicose com prioridade e de forma constante. A glicoquinase opera a meia velocidade e ainda tem margem para acelerar — é isso que a torna um *sensor* de excesso de glicose, adequada ao fígado (que só deve estocar quando sobra) e à célula β (que só deve secretar quando sobra).])

Convém guardar também a família dos transportadores, porque o GLUT4 é o único regulado por insulina — e é essa dependência que explica por que músculo e tecido adiposo captam glicose sob comando hormonal, enquanto cérebro e hemácia captam continuamente:

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-24.png",
  largura: 60%,
  legenda: [GLUT1 (hemácia, barreira hematoencefálica) e GLUT3 (neurônios) são de alta afinidade e independentes de insulina — garantem suprimento contínuo ao tecido que não pode faltar. GLUT2 (fígado, pâncreas, intestino) é de baixa afinidade e trabalha como sensor. GLUT4 (músculo esquelético, adiposo, coração) é o dependente de insulina.])

#subtopico("2.4 — O canal K#sub[ATP] como alvo de fármaco, nos dois sentidos")

Uma vez entendido que fechar o canal K#sub[ATP] secreta insulina, dois usos clínicos caem por gravidade — e a aula apresenta os dois, em direções opostas.

As *sulfonilureias* (glibenclamida) *inibem* o canal K#sub[ATP], imitando o efeito do ATP. O resultado é despolarização e aumento da secreção de insulina independentemente da glicemia. São usadas no diabetes tipo 2, e são eficazes justamente porque nele há resistência periférica com célula β ainda funcionante — o que se ganha é secreção adicional para vencer a resistência.

Na direção contrária, o *diazóxido* é um *ativador* do canal K#sub[ATP]: mantém o canal aberto, impede a despolarização e *reduz* a secreção de insulina. Sua indicação na aula é a hiperinsulinemia do insulinoma — um tumor de células β que secreta insulina de forma autônoma e causa hipoglicemia. O tratamento definitivo é a remoção cirúrgica; o diazóxido é o controle medicamentoso enquanto isso.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-27.png",
  largura: 85%,
  legenda: [As sulfonilureias inibem o canal K#sub[ATP] e aumentam a secreção de insulina — mesmo ponto da cascata em que o ATP age, mas por fármaco.])

#mini-resumo[Mesmo canal, dois sentidos: *fechar* K#sub[ATP] (sulfonilureia, ATP) → despolariza → *mais* insulina. *Abrir* K#sub[ATP] (diazóxido) → hiperpolariza → *menos* insulina.]

#subtopico("2.5 — O que a insulina faz depois de secretada")

A insulina é o hormônio do estado *alimentado*, e todos os seus efeitos podem ser derivados de uma única frase: guardar o excesso de nutriente. No fígado e no músculo, ativa a síntese de glicogênio e freia sua degradação; no músculo e no tecido adiposo, aumenta a captação de glicose ao recrutar GLUT4 para a membrana; estimula a glicólise e a produção de acetil-CoA; no fígado, aumenta a síntese de ácidos graxos; no adiposo, a síntese de triacilgliceróis; e estimula a síntese proteica.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-33.png",
  largura: 90%,
  legenda: [À esquerda, o panorama por tecido. À direita, a tabela que interessa para o card: cada efeito metabólico com a enzima-alvo correspondente — captação de glicose via GLUT4, síntese de glicogênio via glicogênio sintase, freio da degradação via glicogênio fosforilase, glicólise via PFK-1/PFK-2, lipogênese via acetil-CoA carboxilase.])

#subtopico("2.6 — Glicogênio: duas enzimas reguladas em espelho")

O metabolismo do glicogênio é o lugar onde os hormônios desta aula convergem, e ele é organizado por um princípio simples: *as duas enzimas opostas são reguladas pelo mesmo sinal, em sentidos contrários*. Isso evita o desperdício de sintetizar e degradar ao mesmo tempo.

A *glicogênio fosforilase* (degradação) existe em duas formas: fosforilase *b*, menos ativa, e fosforilase *a*, fosforilada pela fosforilase quinase e mais ativa. Além disso, ambas respondem alostericamente ao estado energético — AMP desloca para a forma ativa; ATP, glicose-6-fosfato e glicose deslocam para a inativa. A *glicogênio sintase* (síntese) é o espelho: a fosforilação a *inativa* (sintase b), e a desfosforilação pela fosfatase PP1 a *ativa* (sintase a).

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-31.png",
  largura: 85%,
  legenda: [A fosforilase em quatro estados: os eixos horizontal (fosforilação, pela fosforilase quinase) e vertical (moduladores alostéricos — AMP ativa; ATP, G6P e glicose inativam) são independentes. Verde é ativo, vermelho é inativo. Repare que a fosforilação e o AMP empurram na mesma direção: degradar glicogênio.])

#mini-resumo[Fosforilação: *ativa* a fosforilase (degrada) e *inativa* a sintase (não sintetiza) — perfil de glucagon/adrenalina. Desfosforilação por PP1: o inverso — perfil de insulina.]

A insulina fecha esse circuito por uma via própria: pela PKB, ela *ativa a PP1* (que desfosforila e portanto ativa a sintase e inativa a fosforilase), *inativa a GSK3* (que, se ativa, fosforilaria e inativaria a sintase) e *ativa a fosfodiesterase*, que degrada o AMPc e desliga a PKA. São três frentes convergindo no mesmo desfecho.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-32.png",
  largura: 80%,
  legenda: [A cascata da insulina via PKB atuando em quatro alvos: ativa PP1, inibe GSK3, inibe PKA e ativa a PDE (que converte AMPc em 5'-AMP). Todas as setas terminam no mesmo lugar — síntese de glicogênio.])

#confusao-prevista(
  titulo: "Fosforilar sempre ativa a enzima",
  aluno_acha: [aluno generaliza \"fosforilação = ativação\" a partir da fosforilase],
  mecanismo: [a fosforilação muda a conformação; se isso ativa ou inativa depende da enzima. Neste par, o mesmo evento — adicionar fosfato — *ativa* a fosforilase e *inativa* a sintase. É justamente essa oposição que permite a um único sinal hormonal coordenar as duas vias em sentidos contrários.],
)

#subtopico("2.7 — Glucagon: o espelho da insulina")

O glucagon é um peptídeo de 29 resíduos produzido nas *células α* das ilhotas de Langerhans (a insulina vem das *β*; a somatostatina, das *δ*). Sua secreção é estimulada por hipoglicemia, epinefrina e aumento de aminoácidos séricos, e inibida por insulina, corpos cetônicos e ureia. Clinicamente, é usado no tratamento agudo da hipoglicemia.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-36.png",
  largura: 75%,
  legenda: [A ilhota de Langerhans com as três populações (α: glucagon; β: insulina; δ: somatostatina) e a sequência dos 29 resíduos do glucagon.])

Há um detalhe de processamento que a aula destaca e que é conceitualmente rico: glucagon e GLP-1 vêm do *mesmo precursor*, o proglucagon, e o produto final depende de qual protease predomina no tecido. Na célula α pancreática, a PCSK2 predomina e o produto é o *glucagon*; no intestino e no cérebro, a PCSK1/3 predomina e o produto é o *GLP-1*. O mesmo gene, o mesmo transcrito, produtos com funções opostas sobre a glicemia.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-37.png",
  largura: 85%,
  legenda: [O proglucagon clivado de dois modos. À esquerda (PCSK2, célula α): glucagon. À direita (PCSK1/3, intestino e cérebro): GLP-1. O processamento pós-traducional tecido-específico é o que decide a mensagem.])

#subtopico("2.8 — A cascata do AMPc, em concreto")

A sinalização do glucagon no fígado — e da epinefrina no músculo — é a instância concreta da amplificação apresentada na PARTE I, e vale acompanhá-la nome por nome: o hormônio liga-se ao *receptor de sete domínios transmembrana* (7TM), que ativa a *proteína G trimérica* (troca de GDP por GTP na subunidade α); a Gα ativa a *adenilato-ciclase*, que converte ATP em *AMPc*; o AMPc ativa a *proteína quinase A*; a PKA fosforila e ativa a *fosforilase quinase*; esta fosforila a fosforilase *b*, convertendo-a em fosforilase *a* — e o glicogênio começa a ser degradado.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-38.png",
  largura: 70%,
  legenda: [A cascata completa, do receptor 7TM à fosforilase a. Note que o mesmo desenho serve para epinefrina no músculo e glucagon no fígado — muda o receptor e o tecido, não a maquinaria.])

Os efeitos hepáticos do glucagon seguem daí: aumenta a degradação de glicogênio, reduz a síntese de glicogênio, freia a glicólise, estimula a gliconeogênese, mobiliza ácidos graxos do tecido adiposo e favorece a cetogênese — tudo convergindo para *liberar glicose no sangue* e oferecer combustível alternativo ao cérebro.

#subtopico("2.9 — Catecolaminas: síntese e resposta ao estresse")

As catecolaminas derivam da tirosina numa sequência linear que vale conhecer com as enzimas: tirosina → (tirosina hidroxilase) → DOPA → (DOPA descarboxilase) → dopamina → (dopamina β-hidroxilase) → noradrenalina → (feniletanolamina N-metiltransferase) → adrenalina. A *tirosina hidroxilase* é a *etapa limitante da velocidade*.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-41.png",
  largura: 85%,
  legenda: [A biossíntese das catecolaminas com as quatro enzimas. Em destaque, a tirosina hidroxilase como etapa limitante — o ponto onde a via inteira é regulada. À esquerda, a origem da tirosina a partir da fenilalanina pela fenilalanina hidroxilase.])

A epinefrina prepara o organismo para a ação, e seus efeitos se dividem em duas famílias coerentes. Os *fisiológicos* — aumento da frequência cardíaca, da pressão arterial e dilatação das vias respiratórias — servem a entregar mais oxigênio aos tecidos. Os *metabólicos* — degradação de glicogênio em músculo e fígado, freio da síntese de glicogênio, gliconeogênese hepática, glicólise muscular, mobilização de ácidos graxos, além de estimular glucagon e inibir insulina — servem a disponibilizar combustível. Clinicamente, a aula registra seu uso em parada cardíaca, choque e anafilaxia.

#parte-title("PARTE III — O lado lento: lipossolúveis e o controle por transcrição")

#subtopico("3.1 — Hormônios tireoidianos: o pró-hormônio e a ativação periférica")

A tireoide secreta predominantemente *T4* (tiroxina, com quatro iodos), que é pouco ativo, e em menor quantidade *T3* (tri-iodotironina), que é a forma ativa. A conversão de T4 em T3 acontece *nos tecidos periféricos*, pelas deiodinases (DIO1/DIO2), removendo um iodo do anel externo. A remoção do iodo do anel interno gera o *T3 reverso (rT3)*, que é inativo — e é esse desvio que aumenta em situações de estresse fisiológico, doença ou jejum.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-43.png",
  largura: 85%,
  legenda: [À esquerda, as estruturas: tirosina, T4 (quatro iodos), T3 (três) e rT3 (três, mas na posição que o torna inativo). À direita, o T3 entrando por transportador de membrana e agindo no núcleo pelo par THR/RXR sobre o elemento responsivo (TRE).])

O eixo que controla tudo isso é hierárquico e com retroalimentação negativa: o hipotálamo libera *TRH*, que faz a hipófise liberar *TSH*, que faz a tireoide produzir T4 e T3; os hormônios tireoidianos, por sua vez, inibem hipotálamo e hipófise.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-44.png",
  largura: 70%,
  legenda: [O eixo TRH → TSH → T4, a conversão periférica em T3 (ativo) ou rT3 (inativo), e as alças de feedback negativo que fecham o circuito sobre hipotálamo e hipófise.])

#confusao-prevista(
  titulo: "T4 é o hormônio ativo porque é o mais abundante",
  aluno_acha: [aluno equipara abundância a atividade],
  mecanismo: [T4 é essencialmente um *pró-hormônio*: circula em maior quantidade e com meia-vida longa, funcionando como reservatório. A atividade está no T3, gerado localmente pelas deiodinases no tecido-alvo. Isso permite que *cada tecido regule sua própria exposição* ao hormônio ativo, algo impossível se a tireoide já secretasse só T3.],
)

Os efeitos do T3 são amplos — no coração, frequência e hipertrofia; no osso, crescimento e maturação; no cérebro, crescimento neuronal; no músculo, catabolismo proteico e utilização de glicose; no fígado, síntese de colesterol e metabolismo de gorduras.

#subtopico("3.2 — Esteroides: do colesterol ao cortisol")

Todos os hormônios esteroides derivam do *colesterol*. No córtex adrenal, a via se ramifica: colesterol → (desmolase) → pregnenolona → progesterona, e daí, conforme a hidroxilase que atua, para *aldosterona* (mineralocorticoide), *cortisol* (glicocorticoide) ou *androgênios* (androstenediona → testosterona → estradiol nos tecidos periféricos).

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-52.png",
  largura: 85%,
  legenda: [A árvore de síntese dos esteroides adrenais a partir do colesterol, com as hidroxilases que definem cada ramo. À direita, o destino do cortisol: ligado à globulina ligadora de corticosteroide na circulação, conjugado no fígado (>95%) e excretado — menos de 2% aparece como cortisol livre urinário.])

#subtopico("3.3 — O receptor nuclear: um fator de transcrição ativado por ligante")

O mecanismo dos lipossolúveis é o mesmo para todos, e é bom vê-lo como uma sequência. Na ausência do hormônio, o receptor de glicocorticoide está no citoplasma preso a chaperonas, notadamente a *HSP90*, que o mantêm inativo. O hormônio, sendo lipofílico, atravessa a membrana e liga-se ao receptor; o complexo se desprende da HSP90, sofre mudança conformacional, dimeriza e migra para o núcleo. Lá, liga-se a uma sequência específica de DNA — o *elemento responsivo* (GRE para glicocorticoides, TRE para tireoidianos) — e recruta *coativadores*, aumentando ou diminuindo a transcrição de genes específicos. O efeito final é uma mudança na quantidade de mRNA e, portanto, de proteína.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-53.png",
  largura: 80%,
  legenda: [O percurso do glicocorticoide: atravessa a membrana, desloca a HSP90, entra no núcleo, liga-se ao elemento responsivo e altera a transcrição — mudando a quantidade de mRNA e de proteína. É por isso que o efeito demora horas e persiste depois que o hormônio sai.])

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-50.png",
  largura: 70%,
  legenda: [Detalhe do receptor sobre o DNA: sem ligante, dímero inativo; com o ligante (estrógeno), muda de conformação; com o coativador recrutado, a transcrição é ativada. O ligante age como uma chave conformacional, não como parte da maquinaria transcricional.])

#mini-resumo[A diferença de tempo entre os dois mecanismos tem causa mecanística: modificar covalentemente enzimas que já existem é imediato; fabricar proteínas novas exige transcrição, tradução e acúmulo — horas. E, pela mesma razão, o efeito lipossolúvel *persiste* depois que o hormônio some, porque a proteína sintetizada continua lá.]

#subtopico("3.4 — Cortisol: o eixo, o feedback e o efeito por tecido")

O cortisol é regulado pelo eixo hipotálamo-hipófise-adrenal: o estresse leva o hipotálamo a liberar *CRH*, que leva a hipófise a liberar *ACTH*, que leva a adrenal a produzir cortisol; o cortisol inibe hipotálamo e hipófise, fechando a alça.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-51.png",
  largura: 75%,
  legenda: [O eixo HPA com as duas alças de feedback negativo do cortisol. Repare no detalhe embutido: os primeiros 13 aminoácidos do ACTH correspondem ao MSH, o hormônio estimulador de melanócitos — por isso o excesso de ACTH escurece a pele.])

Esse detalhe do ACTH/MSH é o que dá sentido a um sinal clínico. Na *doença de Addison* — destruição autoimune do córtex adrenal — falta cortisol, o feedback negativo se perde, e o ACTH sobe muito; o excesso de ACTH, contendo a sequência do MSH, causa *hiperpigmentação cutânea*. Já a *doença de Cushing* é a hipersecreção de glicocorticoide.

Metabolicamente, o cortisol é um hormônio do jejum e do estresse, e seus efeitos por tecido são coerentes com isso: no fígado, promove gliconeogênese e aumenta o estoque de glicogênio; no músculo esquelético, inibe a captação de glicose e aumenta a degradação proteica, fornecendo aminoácidos como precursores gliconeogênicos; no tecido adiposo, inibe a captação de glicose e aumenta a lipólise, fornecendo glicerol; no pâncreas, inibe a secreção de insulina e aumenta a de glucagon.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-54.png",
  largura: 85%,
  legenda: [Os efeitos do cortisol organizados por tecido. Todos convergem para o mesmo objetivo — sustentar a glicemia durante o estresse — mesmo que isso custe proteína muscular e gordura periférica.])

#subtopico("3.5 — Disruptores endócrinos")

A aula fecha com uma consequência direta de tudo o que foi construído: se a especificidade do sistema depende do encaixe entre ligante e receptor, então uma molécula estranha com forma parecida pode interferir. Os *disruptores endócrinos* são compostos ambientais que fazem exatamente isso, de dois modos opostos. Como *miméticos*, ligam-se ao receptor e o ativam, produzindo resposta celular na ausência do hormônio verdadeiro. Como *bloqueadores*, ligam-se ao receptor sem ativá-lo e impedem que o hormônio real se ligue — a resposta celular é abolida.

#figura-nebli("/figuras/bioq-24-controle-hormonal/slide-55.png",
  largura: 85%,
  legenda: [À esquerda, a situação normal: hormônio liga o receptor e gera resposta. Ao centro, o mimético ocupa e *ativa* o receptor. À direita, o bloqueador ocupa e *não ativa*, cancelando a resposta. É a mesma alta afinidade que dá especificidade ao sistema que o torna vulnerável.])

#mini-resumo[Fechando a apostila pela ideia inicial: o hormônio é só informação. A alta afinidade resolve o reconhecimento; a cascata resolve a amplificação; a solubilidade decide se a resposta será rápida e reversível (enzima modificada) ou lenta e duradoura (proteína nova). Insulina, glucagon e adrenalina são o primeiro caso; tireoidianos e esteroides, o segundo.]
