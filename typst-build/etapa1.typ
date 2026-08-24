#import "../typst-template/nebli_v2_apostila.typ": *

// Helper local: esquema desenhado em Typst nativo (mesma moldura visual do figura-nebli)
#let esquema-nebli(corpo, legenda: [], largura: 80%) = figure(
  placement: auto, caption: none, numbering: none, supplement: none,
  block(breakable: false, stack(
    block(width: largura, corpo),
    v(6pt),
    align(left, text(size: 9.5pt, style: "italic", fill: text-light, legenda))
  ))
)

#intro-box[
O tubo digestório tem cerca de nove metros e precisa mover o alimento ao longo de todos eles numa velocidade muito específica: rápido o bastante para não estagnar, lento o bastante para dar tempo de quebrar as moléculas e absorvê-las. Quem executa esse transporte é músculo. Quem decide onde e quando esse músculo contrai é um sistema nervoso que mora dentro da própria parede do tubo e que continua funcionando mesmo quando o cérebro não está prestando atenção.

Este resumo percorre esse arranjo em três descidas de profundidade. Primeiro o efetor: que músculo existe em cada trecho, como as camadas estão dispostas e quais modos de contração elas conseguem produzir. Depois o comando: os circuitos nervosos que escolhem o padrão motor, tanto os que se fecham dentro da parede quanto os que sobem até o tronco encefálico e voltam. Por fim, a máquina molecular que converte um neurotransmissor em força dentro da célula muscular lisa.

O fio condutor é sempre o mesmo, e vale mantê-lo à vista: cada estrutura que aparecer aqui existe porque resolve um problema mecânico concreto de mover conteúdo dentro de um tubo.
]

#parte-title("PARTE I — A parede que se move", primeira: true)

#subtopico("1.1 — Esquelético nas pontas, liso no meio")

A musculatura do #sigla("TGI", [trato gastrointestinal — o tubo contínuo da boca ao ânus e as glândulas que despejam secreção nele]) não é a mesma do começo ao fim, e a divisão acompanha exatamente até onde a vontade ainda tem serventia. Nas duas extremidades do tubo — faringe, terço superior do esôfago, esfíncter anal externo — o músculo é esquelético estriado, inervado por motoneurônio somático, exatamente como o bíceps. É por isso que engolir de propósito é possível, e é por isso que segurar as fezes é uma decisão consciente. Somando as duas pontas, o esquelético responde por aproximadamente um terço da musculatura do tubo.

Os outros dois terços — do terço médio do esôfago até o esfíncter anal interno — são de músculo liso. Aqui não há motoneurônio somático nem controle voluntário: as células recebem ordens do sistema nervoso autônomo e dos neurônios que vivem dentro da parede. Ninguém decide contrair o antro gástrico, e ninguém consegue impedir uma contração do cólon transverso pensando com força.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-anatomia-tgi.png",
  largura: 42%,
  legenda: [O tubo contínuo da boca ao reto. Repare que as duas pontas — a região da faringe e o canal anal — são justamente onde a musculatura é esquelética e o controle pode ser voluntário; todo o miolo, do esôfago médio ao esfíncter anal interno, é músculo liso e trabalha sem consulta à consciência.])

A fronteira entre os dois territórios é gradual, não abrupta: no esôfago existe uma zona de transição em que fibras estriadas e lisas convivem, e o vago carrega, lado a lado, dois tipos de fibra motora para dar conta disso. As fibras que comandam o segmento estriado saem do núcleo ambíguo e são somáticas na forma de agir — liberam acetilcolina direto sobre a fibra muscular, sem gânglio no caminho. As fibras que comandam o segmento liso saem do núcleo motor dorsal do vago, são pré-ganglionares e terminam em neurônios que ficam dentro da parede do tubo. Um mesmo nervo, portanto, opera segundo duas lógicas diferentes conforme o alvo.

Há um detalhe que costuma passar batido e que muda o modo de pensar o assunto: ser estriado não significa ser voluntário o tempo todo. A deglutição começa como ato voluntário, mas assim que o bolo cruza os pilares da faringe o programa motor é disparado por um circuito reflexo do tronco encefálico e segue até o fim sem possibilidade de interrupção — inclusive na porção estriada do esôfago. O músculo é o mesmo do bíceps; o comando, a partir dali, não é.

#mini-resumo[Esquelético nas duas pontas do tubo (um terço) porque ali a vontade precisa ter acesso; liso no miolo (dois terços) porque ali o transporte precisa acontecer independentemente da atenção.]

Vale ainda desfazer uma associação intuitiva errada. Músculo liso não é músculo fraco. Ele gera tensão comparável à do estriado por área de secção, e a sustenta por horas gastando uma fração do #sigla("ATP", [adenosina trifosfato — a moeda energética que a célula gasta para realizar trabalho]) que o estriado consumiria para o mesmo feito. Essa economia não é um detalhe secundário: ela é o que torna possível um esfíncter permanecer fechado a noite inteira sem fadigar, e o mecanismo molecular por trás dela reaparece na PARTE III.

#subtopico("1.2 — Circular estreita, longitudinal encurta")

Pense num tubo de borracha com dois conjuntos de elásticos amarrados nele. Um conjunto envolve o tubo como anéis, perpendicular ao seu eixo; o outro corre ao longo do comprimento, como tiras coladas de ponta a ponta. Puxar um conjunto ou o outro produz efeitos geométricos completamente diferentes, e é dessa diferença que nasce todo o repertório motor do tubo digestório.

Os anéis são a *camada circular*, a mais interna das duas. Quando as fibras circulares encurtam, o diâmetro da luz diminui naquele ponto: o conteúdo que estava ali é espremido e obrigado a se deslocar para onde ainda há espaço. As tiras longitudinais formam a *camada longitudinal*, mais externa. Quando elas encurtam, o segmento fica mais curto e, por consequência, mais largo — a luz naquele ponto se abre em vez de fechar.

#esquema-nebli(largura: 88%, legenda: [As duas camadas da muscular própria e o efeito geométrico de cada uma. Nenhuma delas propele sozinha: o transporte nasce da combinação — a circular fecha atrás do bolo enquanto a longitudinal encurta o segmento que vai recebê-lo à frente.])[
#grid(columns: (1fr, 1fr), gutter: 18pt,
  block(stroke: 0.7pt + gray-border, radius: 4pt, inset: 10pt, width: 100%)[
    #align(center)[
      #text(font: titulo-fam, size: 9pt, weight: "bold", fill: navy)[Camada circular]
      #v(9pt)
      #text(size: 13pt, fill: teal)[#sym.arrow.b#h(16pt)#sym.arrow.b#h(16pt)#sym.arrow.b]
      #v(3pt)
      #rect(width: 92%, height: 13pt, radius: 3pt, fill: rgb("#eef2f7"), stroke: 0.8pt + navy)
      #v(3pt)
      #text(size: 13pt, fill: teal)[#sym.arrow.t#h(16pt)#sym.arrow.t#h(16pt)#sym.arrow.t]
      #v(9pt)
      #text(size: 8.5pt)[o anel aperta e a *luz estreita* — o conteúdo é expulso do ponto que fechou]
    ]
  ],
  block(stroke: 0.7pt + gray-border, radius: 4pt, inset: 10pt, width: 100%)[
    #align(center)[
      #text(font: titulo-fam, size: 9pt, weight: "bold", fill: navy)[Camada longitudinal]
      #v(26pt)
      #grid(columns: (auto, 1fr, auto), align: horizon, column-gutter: 4pt,
        text(size: 15pt, fill: gold)[#sym.arrow.r],
        rect(width: 100%, height: 13pt, radius: 3pt, fill: rgb("#f7f2e6"), stroke: 0.8pt + navy),
        text(size: 15pt, fill: gold)[#sym.arrow.l])
      #v(26pt)
      #text(size: 8.5pt)[as tiras encurtam e o *segmento fica mais curto* — e, por isso mesmo, mais largo]
    ]
  ]
)
]

Entre as duas camadas, encaixado nesse plano, corre o *plexo mioentérico*. A posição não é acidente anatômico decorativo: quem mora entre os dois músculos é exatamente quem precisa coordená-los, e é por isso que esse plexo governa motilidade — assunto da PARTE II. Mais para dentro, logo abaixo do epitélio, há uma lâmina fina e independente chamada muscular da mucosa, que não participa do transporte do conteúdo; ela movimenta as pregas e as vilosidades, expondo mais superfície ao quimo. Confundir as duas leva o raciocínio para o lugar errado: a muscular própria empurra o bolo, a muscular da mucosa agita a superfície que o recebe.

A partir dessas duas camadas, o tubo monta dois padrões motores distintos com o mesmo material. Na #termo-nota[peristalse][onda coordenada em que a circular contrai atrás do conteúdo e relaxa à frente, empurrando-o num sentido só], as contrações são ordenadas no espaço e caminham numa direção definida, transportando o conteúdo. Na *segmentação*, anéis circulares contraem em pontos alternados ao longo do intestino, sem sequência espacial: o conteúdo é dividido, empurrado para os dois lados e volta a se juntar quando os anéis relaxam. O resultado é mistura, não transporte — o #termo-nota[quimo][massa semilíquida de alimento parcialmente digerido, misturada às secreções, que deixa o estômago] é picotado e reencostado contra a mucosa absortiva repetidas vezes.

#mini-resumo[Circular fecha a luz, longitudinal encurta o segmento. Ordenar essas duas ações no espaço gera peristalse; embaralhá-las de propósito gera segmentação e mistura.]

#subtopico("1.3 — Contração fásica e contração tônica")

O ponto onde o raciocínio costuma quebrar aqui é a palavra "tônica". Ela sugere uma contração fixa, permanente, ligada de fábrica e imune a regulação — e é justamente o contrário. O tônus é ativamente construído e ativamente desmontado; ele apenas dura muito mais do que a contração que estamos acostumados a imaginar.

Os dois modos ficam evidentes quando se registra ao mesmo tempo o cálcio dentro da célula, a fosforilação das pontes cruzadas e a força produzida. Na *contração fásica*, um estímulo breve faz o cálcio disparar, a fosforilação subir logo atrás e a força aparecer e desaparecer em poucos segundos. Tudo sobe e tudo desce, na mesma ordem. É o modo do corpo do estômago, do intestino delgado e do cólon — órgãos que precisam produzir ondas repetidas de transporte e mistura.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-fasica-tonica.png",
  largura: 62%,
  legenda: [Em A, contração fásica: estímulo curto, cálcio em pico e força que aparece e some. Em B, contração tônica: o estímulo se mantém, a força faz platô por todo o tempo — mas o cálcio e a fosforilação das pontes cruzadas caem para perto do basal logo depois do pico inicial. Essa dissociação entre força alta e fosforilação baixa é a pista de que existe um segundo mecanismo sustentando a tensão.])

Na *contração tônica*, o estímulo se mantém e a força faz um platô que dura minutos ou horas. O detalhe revelador está nas outras duas curvas: o cálcio sobe num pico, cai e permanece perto do valor de repouso; a fosforilação faz o mesmo. Ou seja, a célula sustenta uma força alta com pouco cálcio e pouca fosforilação. Isso só é possível porque, uma vez formada, a ponte entre miosina e actina consegue permanecer presa mesmo depois de perder o fosfato, ciclando muito devagar. Esse estado de trava — o #termo-nota[latch][regime em que as pontes cruzadas permanecem acopladas com fosforilação e velocidade muito baixas, mantendo tensão a custo mínimo de ATP] — é o que torna barato manter um esfíncter fechado o dia inteiro.

Falta ainda explicar de onde vem o ritmo das contrações fásicas, porque elas não acontecem em momentos aleatórios. Espalhadas entre as camadas musculares existem células especializadas, as células intersticiais de Cajal, que despolarizam e repolarizam espontaneamente numa frequência própria de cada segmento — cerca de três ciclos por minuto no estômago e doze no duodeno. Essa oscilação, chamada #termo-nota[onda lenta][despolarização rítmica espontânea das células de Cajal que se propaga ao músculo e define quando a contração pode ocorrer], se propaga pelas junções comunicantes para as células musculares vizinhas e funciona como um marcapasso: ela não gera contração por si só, mas define os momentos em que a contração *pode* ocorrer. Se um estímulo excitatório chegar quando a onda lenta está no ponto alto, o limiar é cruzado e a contração acontece; se chegar no vale, nada acontece. Por isso o ritmo máximo de contrações de um segmento é ditado pela sua frequência de ondas lentas, e a intensidade do estímulo nervoso só decide quantas dessas oportunidades serão de fato aproveitadas.

#confusao-prevista(
  titulo: "Fásico não é sinônimo de peristáltico",
  aluno_acha: [o aluno tende a colar as duas palavras e concluir que toda contração fásica transporta conteúdo],
  mecanismo: [fásico e tônico descrevem o *decurso temporal* de uma contração — quanto ela dura. Peristalse e segmentação descrevem a *organização espacial* de várias contrações — em que ordem elas acontecem ao longo do tubo. A segmentação é feita de contrações fásicas e não transporta nada: ela mistura. O que transforma contrações fásicas em transporte é a coordenação imposta pelo circuito nervoso da parede, não a duração de cada uma.],
)

#subtopico("1.4 — Esfíncteres: o tônus que vira porta")

O modo tônico ganha sentido funcional quando um anel de músculo liso o assume em caráter permanente: nasce um esfíncter. Um esfíncter é, na descrição mais honesta, um segmento de músculo circular espessado que fica contraído por padrão e que precisa ser ativamente relaxado para deixar alguma coisa passar. A porta é fechada de fábrica; abrir custa sinal.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-esfincteres.png",
  largura: 58%,
  legenda: [Os pontos de controle ao longo do tubo: esfíncter esofágico superior e inferior, piloro, válvula ileocecal e o par anal interno/externo. A regra geral que vale para todos eles: a chegada de conteúdo distendendo o segmento imediatamente anterior é o sinal que relaxa a porta à frente.])

São cinco pontos de controle, e vale reconhecê-los pela função e não pela lista. O #sigla("EES", [esfíncter esofágico superior — anel de músculo esquelético no início do esôfago]) fica fechado para impedir que o ar da respiração entre no esôfago a cada inspiração e que o conteúdo esofágico suba de volta à faringe. O #sigla("EEI", [esfíncter esofágico inferior — anel de músculo liso na junção entre esôfago e estômago]) separa um compartimento de pressão negativa (o tórax) de um de pressão positiva e conteúdo ácido (o abdome), e essa diferença de pressão empurra o suco gástrico para cima o tempo todo — manter esse anel contraído é o que impede o refluxo. O piloro regula a velocidade com que o quimo sai do estômago. A válvula ileocecal impede que o conteúdo do cólon, densamente colonizado por bactérias, reflua para o íleo. E o par anal — interno liso e involuntário, externo esquelético e voluntário — separa a chegada de fezes ao reto da decisão social de eliminá-las.

A regra que unifica todos eles é a mesma e aparece explicitamente no material da aula: distensão do tubo relaxa o esfíncter à frente. Quando o segmento imediatamente anterior é distendido pelo conteúdo, o circuito nervoso da parede detecta o estiramento e ordena o relaxamento da porta seguinte, para que o conteúdo continue avançando. É esse arranjo que faz o EEI relaxar antes mesmo do bolo chegar nele, e que faz o esfíncter anal interno relaxar quando as fezes distendem a ampola retal.

O piloro merece um parágrafo à parte porque recebe duas ordens de sentidos opostos, e o equilíbrio entre elas é que determina o esvaziamento gástrico. Do lado de trás, a distensão do antro pela chegada de alimento gera a *regulação antral anterógrada*: o piloro relaxa e deixa passar. Do lado da frente, a chegada de quimo ao duodeno gera a *regulação duodenal retrógrada*: o piloro contrai e trava a saída. O duodeno tem capacidade limitada de neutralizar ácido, digerir gordura e lidar com uma carga osmótica alta; se o estômago despejasse tudo de uma vez, o intestino não daria conta. O freio duodenal é, portanto, o mecanismo que protege o segmento seguinte da própria eficiência do segmento anterior — e quando ele falha, como acontece após ressecções gástricas que removem o piloro, o quimo hiperosmolar chega de uma vez ao delgado, puxa água para a luz e produz o quadro de mal-estar, taquicardia e diarreia conhecido como síndrome de dumping.

#clinica-box("Doença do refluxo gastroesofágico", [O EEI mantém uma pressão de repouso maior que a do estômago, e é só essa diferença que segura o conteúdo ácido embaixo. Além do tônus basal, o esfíncter sofre episódios normais de *relaxamento transitório* — não desencadeados por deglutição — que servem para eructar o ar deglutido. Na doença do refluxo, dois mecanismos podem estar operando: o tônus basal está baixo demais para vencer o gradiente de pressão tóraco-abdominal, ou os relaxamentos transitórios estão frequentes demais e prolongados. Em qualquer um dos casos o resultado é o mesmo — ácido em contato com um epitélio esofágico que não tem a barreira de muco e bicarbonato do estômago, gerando pirose e, na exposição crônica, esofagite. Situações que reduzem o tônus do EEI, como a gestação avançada ou o aumento da pressão intra-abdominal, agravam o quadro pelo mesmo caminho mecânico.])

Fechando a PARTE I: o tubo dispõe de dois tipos de músculo, duas camadas com efeitos geométricos opostos e dois modos temporais de contrair. Esse é todo o repertório do efetor. Ele não explica, sozinho, por que a circular contrai atrás do bolo e relaxa à frente, nem por que o piloro sabe que o duodeno está cheio. Falta o comando — e o comando não vem de fora do tubo.

#parte-title("PARTE II — Quem dá as ordens")

#subtopico("2.1 — Plexos mioentérico e submucoso: o cérebro da parede")

Dentro da parede do tubo digestório existe uma rede de neurônios própria, com cerca de cem milhões de células — número comparável ao de toda a medula espinhal. Essa rede é o #sigla("SNE", [sistema nervoso entérico — a rede de neurônios contida na própria parede do tubo digestório]), e ela é completa no sentido funcional do termo: tem neurônios sensoriais que leem o que acontece na luz e na parede, interneurônios que processam essa informação, e neurônios motores que comandam músculo, glândulas e vasos. Um arco reflexo inteiro cabe dentro da parede, sem precisar consultar ninguém.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-sne-sna.png",
  largura: 72%,
  legenda: [O comando da parede em dois níveis. O sistema entérico, dentro da parede, dividido em dois plexos com funções distintas; o sistema autônomo, vindo de fora, modulando o que o entérico já faz — o parassimpático somando, o simpático subtraindo. A ingestão distende o tubo e é o gatilho que aciona motilidade, secreção e vasodilatação ao mesmo tempo.])

O sistema entérico se organiza em dois plexos, e a posição de cada um antecipa a função. O *plexo mioentérico*, também chamado de plexo de Auerbach, fica entre as camadas circular e longitudinal — exatamente no plano onde é preciso coordenar os dois músculos. Ele governa motilidade: contração, relaxamento, tônus dos esfíncteres. O *plexo submucoso*, ou plexo de Meissner, fica na submucosa, logo abaixo do epitélio — o plano onde ficam as glândulas e a rede vascular da mucosa. Ele governa secreção, fluxo sanguíneo local e transporte de água e íons pelo epitélio. Guardar a posição resolve a função sem decorar a dupla de nomes: quem está no meio dos músculos manda no movimento, quem está junto das glândulas manda na secreção.

Sobre essa rede intrínseca age a inervação extrínseca, que vem de fora do tubo: o #sigla("SNA", [sistema nervoso autônomo — a divisão simpática e parassimpática que chega ao tubo a partir do sistema nervoso central]). O parassimpático é excitatório na motilidade — o nervo vago para o esôfago, estômago, delgado e cólon proximal; os nervos pélvicos, saindo dos segmentos sacrais, para o cólon distal e o reto. O simpático é inibitório, chegando pelos nervos esplâncnicos. Vale notar o ponto que muda o modo de pensar: nenhum dos dois manda direto no músculo. Ambos terminam sobre neurônios entéricos, e o neurônio entérico é o motor final que fala com a célula muscular. O extrínseco *modula* um sistema que já funciona sozinho — ele sobe ou abaixa o volume de padrões motores que o entérico gera por conta própria.

#mini-resumo[Quem mora entre os músculos manda em movimento (mioentérico); quem mora junto das glândulas manda em secreção (submucoso). O autônomo não substitui essa rede — ele a modula, terminando sempre num neurônio entérico.]

Essa arquitetura tem uma consequência que só fica visível quando o sistema é destruído. Se o entérico fosse apenas um relé do vago, perder o plexo seria pouco relevante enquanto o vago estivesse íntegro. Não é o que se observa: a perda dos neurônios entéricos de um segmento paralisa aquele segmento de modo permanente, e o vago intacto não compensa.

#clinica-box("Megaesôfago e megacólon chagásicos", [O #emph[Trypanosoma cruzi] tem tropismo pelos neurônios do plexo mioentérico. Na fase crônica da doença de Chagas, a inflamação persistente destrói progressivamente essas células ao longo de segmentos inteiros do esôfago e do cólon. O segmento desnervado perde principalmente o braço inibitório do circuito — os neurônios que relaxam o músculo à frente do conteúdo e abrem os esfíncteres. Sem relaxamento coordenado, o esfíncter esofágico inferior não abre na deglutição e o segmento colônico não relaxa para receber as fezes: o conteúdo para. A montante da obstrução funcional, a pressão crônica dilata a parede, e é essa dilatação que dá nome ao quadro — megaesôfago e megacólon. O ponto mecanístico que costuma escapar: a dilatação não é o defeito primário, é a consequência de um segmento estreito mais adiante que não consegue relaxar.])

#subtopico("2.2 — Reflexo curto: o tubo resolvendo sozinho")

O arco reflexo mais econômico do tubo digestório é aquele que nunca sai da parede, e a PARTE I deixou uma pergunta mecânica em aberto que ele responde: como a circular sabe que deve contrair atrás do bolo e relaxar à frente dele.

O estímulo é mecânico. A chegada de conteúdo distende a parede, e essa distensão é lida por *mecanorreceptores* — terminações de neurônios sensoriais que respondem a estiramento. O neurônio sensorial leva o sinal a interneurônios do plexo mioentérico, e é aqui que o circuito ganha a propriedade decisiva: os interneurônios se projetam em dois sentidos. Os ascendentes levam a informação para trás, na direção da boca; os descendentes levam para a frente, na direção do ânus. Cada ramo termina num tipo diferente de neurônio motor.

No lado oral, o interneurônio ascendente ativa o neurônio motor *excitatório*, que libera acetilcolina e substância P sobre o músculo circular: o anel atrás do bolo contrai e empurra. No lado aboral, o interneurônio descendente ativa o neurônio motor *inibitório*, que libera #sigla("VIP", [peptídeo intestinal vasoativo — neurotransmissor inibitório do sistema entérico, relaxa músculo liso]) e #sigla("NO", [óxido nítrico — gás sinalizador de meia-vida curta, também inibitório sobre o músculo liso]): o segmento à frente relaxa e se abre para receber. Esse par de ações opostas em pontos vizinhos é o que se chama de reflexo peristáltico, e sua propriedade essencial é a polaridade — ele tem um sentido, e é por isso que o conteúdo caminha em vez de apenas ser espremido no lugar.

#esquema-nebli(largura: 92%, legenda: [A polaridade do reflexo peristáltico. O mesmo estímulo — distensão pelo bolo — produz efeitos opostos conforme o lado, porque o interneurônio ascendente recruta o motor excitatório e o descendente recruta o inibitório. Sem essa assimetria, a contração espremeria o conteúdo para os dois lados e nada se moveria.])[
#block(stroke: 0.7pt + gray-border, radius: 5pt, inset: 12pt, width: 100%)[
  #align(center)[
    #text(font: titulo-fam, size: 9pt, weight: "bold", fill: navy)[Sentido do transporte #h(6pt) #sym.arrow.r.long]
    #v(10pt)
    #grid(columns: (1fr, 0.55fr, 1fr), gutter: 10pt, align: horizon,
      block(width: 100%, fill: rgb("#fbeceb"), stroke: 0.8pt + red-alert, radius: 4pt, inset: 8pt)[
        #align(center)[
          #text(size: 8.5pt, weight: "bold", fill: navy)[atrás do bolo]
          #v(3pt)
          #text(size: 9pt)[circular *contrai*]
          #v(3pt)
          #text(size: 8pt, fill: text-light)[acetilcolina · substância P]
        ]
      ],
      block(width: 100%, inset: 6pt)[
        #align(center)[
          #circle(radius: 13pt, fill: rgb("#e6e2d4"), stroke: 0.8pt + slate)
          #v(3pt)
          #text(size: 8pt, fill: text-light)[bolo]
        ]
      ],
      block(width: 100%, fill: rgb("#eaf1f8"), stroke: 0.8pt + blue-clin, radius: 4pt, inset: 8pt)[
        #align(center)[
          #text(size: 8.5pt, weight: "bold", fill: navy)[à frente do bolo]
          #v(3pt)
          #text(size: 9pt)[circular *relaxa*]
          #v(3pt)
          #text(size: 8pt, fill: text-light)[VIP · óxido nítrico]
        ]
      ]
    )
    #v(9pt)
    #text(size: 8.5pt)[a longitudinal contrai à frente e *encurta* o segmento que vai receber o conteúdo]
  ]
]
]

Por se fechar inteiramente dentro da parede, esse arco é chamado de *reflexo curto* ou *reflexo intramural*. Curto aqui é literal: o sinal não sai do tubo, não passa por gânglio pré-vertebral, não sobe à medula nem ao encéfalo. Menos sinapses e menos distância significam menor latência, e é essa rapidez que permite ajustar a contração segmento a segmento enquanto o bolo avança.

#atencao-box("Distensão abre a porta da frente, não fecha", [O reflexo aqui inverte a intuição mecânica de quem pensa em canos e válvulas. É tentador supor que, se o tubo está cheio, o esfíncter à frente deve fechar para conter o conteúdo — como uma comporta que segura água. O circuito faz o oposto: a distensão de um segmento é justamente o sinal que *relaxa* o esfíncter seguinte, porque o problema a ser resolvido não é conter, é escoar. Quem lê a distensão são os mecanorreceptores da parede; quem executa o relaxamento é o neurônio inibitório liberando VIP e óxido nítrico sobre o anel esfincteriano. Guardar o sinal na direção errada estraga o raciocínio em cadeia: sem essa inversão bem fixada, fica impossível entender por que o esfíncter esofágico inferior relaxa antes do bolo chegar nele, por que o esfíncter anal interno relaxa quando as fezes distendem o reto, e por que a perda dos neurônios inibitórios — e não dos excitatórios — é o que produz obstrução funcional na doença de Chagas.])

#subtopico("2.3 — Reflexo longo vago-vagal")

Se o reflexo curto é o operário que resolve o problema no chão de fábrica, o reflexo longo é a linha direta com a central: a informação sai do tubo, sobe até o tronco encefálico, é processada lá e volta. O trajeto é mais demorado, mas permite algo que o circuito local não faz — coordenar segmentos distantes entre si e integrar o estado do tubo com o resto do organismo.

O arco começa igual: mecanorreceptores da parede detectam distensão. A diferença é o destino. O sinal entra em fibras sensoriais que caminham dentro do nervo vago até o tronco encefálico, onde fazem sinapse no núcleo do trato solitário. Dali a informação é repassada ao núcleo motor dorsal do vago, que dispara fibras parassimpáticas pré-ganglionares de volta ao tubo. Essas fibras terminam em neurônios do plexo mioentérico — o mesmo motor final do reflexo curto. Como a alça de ida e a de volta correm ambas no vago, o circuito é chamado de *reflexo vago-vagal*.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-reflexos-curto-longo.png",
  largura: 80%,
  legenda: [Os dois arcos partindo do mesmo estímulo. À esquerda, o reflexo curto se fecha dentro da parede; à direita, o reflexo longo sobe ao tronco encefálico pela aferência vagal e volta pela eferência parassimpática. Os dois convergem para o mesmo neurônio motor entérico, que libera acetilcolina se for excitatório e VIP se for inibitório — e é essa convergência que faz os circuitos somarem em vez de competirem.])

Há um dado sobre o vago que reorganiza a compreensão do assunto. Costuma-se pensar o vago como nervo motor do parassimpático, mas cerca de quatro em cada cinco fibras vagais abdominais são *aferentes*: o tráfego predominante é do intestino para o encéfalo, não o contrário. Isso significa que o tronco encefálico é continuamente informado sobre o volume, a tensão e a composição química do conteúdo do tubo, e é essa informação que permite respostas antecipatórias.

O exemplo mais limpo é o *relaxamento receptivo* do estômago. Quando o bolo distende o esôfago — antes, portanto, de chegar ao estômago — a aferência vagal leva o aviso ao tronco encefálico, e a eferência vagal ativa os neurônios entéricos inibitórios do fundo gástrico. O fundo relaxa e acomoda o volume que está chegando com um aumento mínimo de pressão. Sem esse reflexo, cada refeição elevaria fortemente a pressão intragástrica, e o conteúdo seria empurrado de volta contra o esfíncter esofágico inferior. É por isso que a vagotomia troncular, feita no passado para reduzir a secreção ácida, cursava com sensação de plenitude precoce e retardo de esvaziamento — o estômago perdia a capacidade de relaxar para receber.

#mini-resumo[Reflexo curto se fecha na parede e é rápido; reflexo longo sobe ao tronco pelo vago e volta, permitindo coordenação entre segmentos distantes. Os dois terminam no mesmo neurônio motor entérico e somam.]

#subtopico("2.4 — Acetilcolina, VIP e óxido nítrico: o léxico do entérico")

O nome dos neurotransmissores inibitórios é uma armadilha silenciosa. "Peptídeo intestinal vasoativo" e "óxido nítrico" soam como moléculas que fazem alguma coisa acontecer, e o aluno tende a arquivá-las como excitatórias. São o oposto: são o par que relaxa, e o circuito inteiro da PARTE II depende de guardar esse sinal na direção certa.

O neurônio motor excitatório do plexo mioentérico libera *acetilcolina*, que age em receptores muscarínicos da célula muscular lisa e produz contração; junto vem a *substância P*, que reforça o mesmo efeito. O neurônio motor inibitório libera VIP e óxido nítrico, e frequentemente também ATP, que juntos produzem relaxamento. Esses dois neurônios motores são as únicas duas saídas do sistema entérico para o músculo — todo o repertório motor do tubo, por mais complexo que pareça, é construído distribuindo no espaço e no tempo essas duas ordens.

O óxido nítrico merece um degrau a mais de mecanismo, porque ele não funciona como os demais. Não é armazenado em vesículas: é sintetizado na hora pela óxido nítrico sintase neuronal a partir da arginina, difunde livremente através das membranas por ser um gás pequeno e apolar, e por isso não precisa de receptor de superfície. Dentro da célula muscular, liga-se diretamente à guanilato ciclase solúvel, que passa a produzir #sigla("GMPc", [monofosfato cíclico de guanosina — segundo mensageiro que ativa a proteína quinase G e leva a relaxamento do músculo liso]). Esse segundo mensageiro ativa a proteína quinase G, que reduz o cálcio disponível e favorece a desfosforilação da miosina — os dois caminhos que a PARTE III vai destrinchar. Sua meia-vida é de segundos, o que faz do óxido nítrico um sinal estritamente local e rapidamente reversível.

O material da aula lista ainda outros neuromediadores que circulam nesses circuitos: serotonina, catecolaminas, ATP e #sigla("GABA", [ácido gama-aminobutírico — neurotransmissor de ação predominantemente inibitória, também presente em circuitos entéricos]). A serotonina merece destaque porque a maior parte da serotonina do corpo não está no encéfalo, e sim nas células enterocromafins da mucosa intestinal; liberada quando a mucosa é mecanicamente estimulada, ela é um dos gatilhos que disparam o neurônio sensorial do reflexo peristáltico.

O simpático fecha o quadro, e o faz por dois caminhos que vale separar. O principal é *pré-sináptico*: as fibras noradrenérgicas terminam sobre os próprios neurônios entéricos e reduzem a liberação de acetilcolina — ou seja, o simpático inibe a motilidade desligando o excitador, não agindo diretamente no músculo. O segundo caminho é direto e vale para os esfíncteres, que o simpático *contrai*. A combinação é coerente do ponto de vista funcional: em situações de estresse e demanda periférica, a parede para de empurrar e as portas se fecham, retendo o conteúdo no lugar. É o mesmo mecanismo que, exagerado após uma manipulação cirúrgica do abdome, produz o #termo-nota[íleo adinâmico][parada funcional da motilidade sem obstrução mecânica, por inibição neural excessiva da parede] — a parede fica atônica, o conteúdo estagna e o abdome distende sem que haja qualquer obstrução mecânica.

#clinica-box("Acalasia: quando falta o braço inibitório", [Na acalasia há perda seletiva dos neurônios inibitórios do plexo mioentérico na região do esfíncter esofágico inferior. Os neurônios excitatórios colinérgicos permanecem, e a consequência é um desequilíbrio, não uma paralisia: sem VIP e sem óxido nítrico para contrapor, o esfíncter mantém tônus elevado e não relaxa na deglutição. Ao mesmo tempo, o corpo do esôfago perde a polaridade da onda peristáltica, porque essa polaridade dependia justamente do relaxamento à frente. O resultado clínico é disfagia progressiva para sólidos e líquidos, com o alimento parando acima de um esfíncter que não abre, e dilatação lenta do esôfago a montante. O tratamento persegue o mecanismo: dilatação ou secção cirúrgica das fibras musculares do esfíncter reduzem mecanicamente o tônus que o neurônio inibitório não consegue mais reduzir quimicamente.])

Fechando a PARTE II: o comando existe em dois níveis — um circuito local rápido, que decide onde contrair e onde relaxar, e um circuito longo que integra segmentos distantes. Ambos terminam no mesmo lugar, um neurônio motor entérico que despeja acetilcolina ou VIP e óxido nítrico sobre a célula muscular lisa. O que acontece dentro dessa célula depois que o neurotransmissor chega é o que falta explicar.

#parte-title("PARTE III — Do nervo à força")

#subtopico("3.1 — Junção neuroefetora: varicosidades sem placa motora")

A PARTE II terminou com o neurotransmissor sendo liberado sobre a célula muscular lisa. O modo como essa entrega acontece é diferente de tudo o que se aprende na junção neuromuscular esquelética, e ignorar a diferença leva a previsões erradas sobre velocidade e alcance da resposta.

Na junção neuromuscular esquelética existe uma placa motora: o axônio termina num botão que se encaixa numa região especializada da fibra muscular, a fenda é estreitíssima, a densidade de receptores é altíssima e a relação é rigorosamente um-para-um — um motoneurônio, um ponto de contato por fibra, uma resposta previsível e do tipo tudo-ou-nada.

No músculo liso do tubo digestório não há nada disso. O axônio do neurônio entérico atravessa o tecido muscular e, ao longo do seu trajeto, apresenta dilatações repetidas em forma de contas de rosário. Cada uma dessas #termo-nota[varicosidades][dilatações sucessivas ao longo do axônio, cheias de vesículas e mitocôndrias, que liberam neurotransmissor lateralmente em vez de numa terminação única] é carregada de vesículas com neurotransmissor e de mitocôndrias, e libera seu conteúdo lateralmente, no espaço entre as células musculares. Não há terminação única, não há aparato pós-sináptico especializado, e a distância que o neurotransmissor precisa percorrer por difusão é muito maior.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-juncao-neuroefetora.png",
  largura: 46%,
  legenda: [O axônio do neurônio autônomo pós-ganglionar atravessa o tecido muscular liso formando varicosidades sucessivas, cada uma repleta de vesículas e mitocôndrias. O neurotransmissor é liberado lateralmente e banha várias células ao mesmo tempo — arranjo que troca precisão por alcance.])

Três consequências saem diretamente desse arranjo, e vale extraí-las uma a uma. A primeira é temporal: quanto maior a distância de difusão, mais lenta a resposta — no liso ela se instala em centenas de milissegundos, não em milissegundos. A segunda é espacial: uma varicosidade banha um território com muitas células, de modo que uma única fibra nervosa comanda um bloco de músculo, e não uma célula. A terceira é a graduação: sem placa motora e sem exigência de potencial de ação, a resposta pode ser proporcional à quantidade de neurotransmissor liberada, em vez de tudo-ou-nada.

O que costura esse território numa unidade funcional são as *junções comunicantes* entre as células musculares lisas. São canais que conectam diretamente o citoplasma de células vizinhas e deixam passar íons e pequenas moléculas. Uma despolarização que comece numa célula se espalha eletricamente pelas vizinhas sem precisar de neurotransmissor no meio do caminho, e o bloco inteiro passa a se comportar como uma única unidade contrátil — o que se chama de #termo-nota[sincício funcional][conjunto de células separadas que, por estarem acopladas eletricamente, respondem como se fossem uma só]. É também por essas junções que a onda lenta gerada pelas células de Cajal alcança todo o segmento, sincronizando o ritmo das contrações fásicas descrito na PARTE I.

#mini-resumo[Sem placa motora, a inervação do liso é difusa: neurotransmissor liberado lateralmente por varicosidades, resposta lenta e graduada, alcance de muitas células — e as junções comunicantes transformam esse bloco num sincício que contrai junto.]

#subtopico("3.2 — Cálcio, calmodulina e MLCK: a fosforilação que gera força")

O sinal que chega à célula muscular lisa, seja ele qual for, converge sempre para a mesma variável: a concentração de cálcio no citoplasma. Em repouso ela é mantida cerca de dez mil vezes menor que a do meio extracelular, o que faz de qualquer abertura de canal um evento com enorme força motriz a favor da entrada.

O cálcio que sobe durante a contração vem de duas fontes, e no músculo liso do tubo digestório a de fora pesa mais que no músculo esquelético. A principal é o meio extracelular, através de canais de cálcio da membrana — uns abertos por despolarização, outros abertos diretamente pela ligação do neurotransmissor ao seu receptor. A segunda é o retículo endoplasmático liso, que libera o cálcio que tinha estocado. As duas fontes somam, e é essa dependência do cálcio externo que explica por que bloquear canais de cálcio da membrana relaxa o músculo liso de modo tão eficaz.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-calmodulina-mlck.png",
  largura: 80%,
  legenda: [A cadeia completa do acoplamento no músculo liso: quatro íons cálcio mudam a conformação da calmodulina, o complexo formado ativa a quinase da cadeia leve da miosina, e a fosforilação da cadeia leve reguladora converte miosina inativa em miosina ativada, capaz de ciclar contra a actina. Note onde está a regulação — no filamento grosso, do lado da miosina.])

A partir daí a cadeia é direta. Quatro íons cálcio se ligam à #termo-nota[calmodulina][proteína citoplasmática que muda de conformação ao ligar cálcio e, assim modificada, ativa enzimas-alvo], que muda de forma e expõe a superfície com que se acopla à sua enzima-alvo. O complexo cálcio-calmodulina ativa a #sigla("MLCK", [quinase da cadeia leve da miosina — enzima que, ativada pelo complexo cálcio-calmodulina, fosforila a cadeia leve reguladora da miosina]). A enzima ativa transfere um fosfato do ATP para a *cadeia leve reguladora* da miosina, na posição serina 19. A miosina fosforilada muda de conformação, sua atividade ATPásica é liberada e ela passa a formar e desfazer pontes cruzadas com a actina — cada ciclo puxa o filamento fino alguns nanômetros, e a soma de milhões desses ciclos é a força que fecha a luz do tubo.

#atencao-box("No músculo liso o cálcio não liga na troponina", [Esta é a transferência indevida mais destrutiva do assunto, porque ela desloca a regulação para o filamento errado e faz todo o resto desandar. No músculo esquelético o cálcio liga na *troponina*, que arrasta a tropomiosina e libera o sítio da *actina* — a regulação é do lado do filamento fino, e a miosina está sempre pronta. O músculo liso *não possui troponina*. Aqui o cálcio liga na calmodulina, o complexo ativa uma quinase, e a quinase modifica a *miosina* — a regulação é do lado do filamento grosso, e é a miosina que precisa ser ligada. A consequência prática de guardar isso certo aparece imediatamente: no músculo esquelético, tirar o cálcio encerra a contração quase instantaneamente, porque a troponina solta o cálcio e o sítio da actina volta a ser coberto. No liso, tirar o cálcio desativa a quinase, mas o fosfato que já foi colocado na miosina continua lá até que uma segunda enzima o remova — e é exatamente essa defasagem que permite a contração tônica barata descrita na PARTE I.])

#subtopico("3.3 — Relaxamento: tirar o cálcio e desfosforilar a miosina")

Aqui está o ponto em que a intuição mais frequentemente quebra: relaxar não é deixar de estimular. Relaxamento é um processo ativo, com gasto de ATP, e depende de duas engrenagens independentes trabalhando ao mesmo tempo. Desligar apenas uma delas não devolve o músculo ao repouso.

A primeira engrenagem retira o cálcio do citoplasma. A membrana plasmática tem uma ATPase de cálcio que bombeia o íon para fora contra um gradiente altíssimo — daí o gasto energético; o retículo endoplasmático liso tem a sua própria ATPase, que recolhe o cálcio de volta ao estoque; e existe ainda um trocador que joga cálcio para fora aproveitando a entrada de sódio a favor do gradiente. Esse último detalhe amarra a bomba de sódio e potássio ao relaxamento: é ela que mantém o sódio intracelular baixo e, portanto, mantém disponível o gradiente que o trocador usa como fonte de energia. Em paralelo, a abertura de canais de potássio hiperpolariza a membrana, o que fecha os canais de cálcio dependentes de voltagem e interrompe a entrada pela porta principal.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-ca-contracao-relaxamento.png",
  largura: 62%,
  legenda: [As duas metades do ciclo lado a lado. À esquerda, cálcio entrando, complexo com calmodulina, quinase ativa e contração. À direita, extrusão de cálcio pelas ATPases da membrana e do retículo, queda da atividade da quinase e ativação da miosina fosfatase, que retira o fosfato e encerra a contração. Note que a seta verde da fosfatase incide sobre a contração — ela não remove cálcio, ela desfaz o efeito do que o cálcio já produziu.])

A segunda engrenagem desfaz a marca deixada pela quinase. A *miosina fosfatase* retira o fosfato da cadeia leve reguladora, e só então a miosina volta ao estado inativo e as pontes cruzadas param de ciclar. Essa separação de tarefas é o que costuma se embaralhar: a ATPase de cálcio mexe no íon, a fosfatase mexe no fosfato. Sem a fosfatase, o cálcio pode cair a zero que a miosina fosforilada continua trabalhando; sem as ATPases, a fosfatase remove fosfato mas a quinase, ainda ativa pelo cálcio alto, recoloca outro imediatamente.

Dessa arquitetura sai a leitura correta do gráfico da contração tônica que apareceu na PARTE I. Naquele registro, o cálcio e a fosforilação caem enquanto a força permanece em platô. Isso acontece porque a proporção entre quinase ativa e fosfatase ativa determina a *fração* de miosinas fosforiladas em cada instante — e algumas pontes já formadas permanecem acopladas, ciclando muito lentamente, mesmo depois de perderem o fosfato. A força se mantém com um número pequeno de pontes trabalhando devagar, o que custa pouquíssimo ATP.

Duas intervenções clínicas usadas todos os dias operam exatamente sobre essas engrenagens — os bloqueadores de canal de cálcio impedem a entrada do íon e reduzem o tônus do esfíncter esofágico inferior, enquanto os nitratos doam óxido nítrico e ativam a via do GMPc, que age nas duas frentes ao mesmo tempo, baixando o cálcio e favorecendo a fosfatase.

#mini-resumo[Relaxar exige duas coisas: tirar o cálcio (ATPases da membrana e do retículo, trocador com sódio, hiperpolarização por potássio) e tirar o fosfato (miosina fosfatase). Só uma delas não basta.]

#subtopico("3.4 — Sensibilização ao cálcio: quando a mesma dose rende mais força")

A conclusão a que a leitura do subtópico anterior conduz é que a força depende do cálcio — e essa conclusão é verdadeira apenas até certo ponto. A célula muscular lisa consegue produzir mais força com exatamente a mesma concentração de cálcio, e o mecanismo que permite isso é o que fecha a lógica inteira do tônus.

O ponto de partida é o tipo de receptor. Muitos dos mediadores que agem no músculo liso — acetilcolina em receptor muscarínico, noradrenalina, VIP, hormônios locais — se ligam a receptores acoplados a proteína G, que não são canais: são receptores que disparam cascatas intracelulares. Confundi-los com canais iônicos apaga justamente a etapa que interessa aqui.

#figura-nebli("/figuras/fisio-tgi-01-motilidade/fig-gpcr-rhoa.png",
  largura: 72%,
  legenda: [Os dois braços que saem do mesmo tipo de receptor. À esquerda, a proteína Gq ativa a fosfolipase C, gerando os mensageiros que liberam cálcio do retículo e ativam a proteína quinase C. À direita, a proteína G12/13 ativa RhoA, que ativa a Rho-quinase; esta e a proteína quinase C convergem para inibir a miosina fosfatase. Com a fosfatase freada, a mesma quantidade de miosina fosforilada se acumula — mais força pelo mesmo cálcio.])

O primeiro braço é o que já tem cara conhecida. A proteína Gq ativa a fosfolipase C, que quebra um fosfolipídio de membrana em dois fragmentos sinalizadores: o #sigla("IP₃", [trifosfato de inositol — segundo mensageiro que abre canais de cálcio no retículo endoplasmático]), que abre canais no retículo e libera cálcio estocado, e o diacilglicerol, que fica na membrana e ativa a #sigla("PKC", [proteína quinase C — enzima ativada por diacilglicerol, com múltiplos alvos na regulação da contração do músculo liso]). Esse braço aumenta a força pelo caminho esperado: mais cálcio, mais complexo com calmodulina, mais quinase ativa, mais fosforilação.

O segundo braço é o que muda o raciocínio. A proteína G12/13 ativa um fator que troca o nucleotídeo da pequena proteína RhoA, deixando-a ligada a #sigla("GTP", [trifosfato de guanosina — nucleotídeo que, ao substituir o GDP, mantém a proteína G na conformação ativa]) e portanto ativa. A RhoA ativa a sua quinase efetora, a Rho-quinase, e essa enzima fosforila a subunidade reguladora da miosina fosfatase — inibindo-a. A proteína quinase C chega ao mesmo destino por outro caminho, ativando uma proteína inibidora chamada CPI-17, que também trava a fosfatase.

O resultado é elegante justamente por não mexer no cálcio. Se a fosfatase é freada, o fosfato colocado pela quinase demora mais para ser removido, e a fração de miosinas fosforiladas em equilíbrio sobe — sem que a concentração de cálcio tenha mudado nada. É por isso que o fenômeno se chama *sensibilização ao cálcio*: a mesma dose do íon passa a render mais força. E é assim que um esfíncter mantém tônus alto por horas mantendo o cálcio citoplasmático baixo, o que resolve o problema energético que a PARTE I havia deixado em aberto: manter a porta fechada seria proibitivamente caro se dependesse de cálcio permanentemente elevado.

#clinica-box("Nitratos e sildenafila no esôfago que não relaxa", [A via do óxido nítrico é o espelho exato da sensibilização, e por isso ela é o alvo farmacológico natural quando um esfíncter não abre. O óxido nítrico ativa a guanilato ciclase solúvel, que produz GMPc; o GMPc ativa a proteína quinase G, que atua em duas frentes simultâneas — reduz o cálcio citoplasmático e *ativa* a miosina fosfatase, exatamente a enzima que a Rho-quinase inibia. O resultado é dessensibilização ao cálcio e relaxamento. Na acalasia e no espasmo esofágico difuso, em que os neurônios inibitórios não conseguem mais entregar óxido nítrico, os nitratos administrados por via sublingual fornecem a molécula de fora e reduzem a pressão do esfíncter esofágico inferior. A sildenafila chega ao mesmo lugar por outro ponto da via: ela inibe a fosfodiesterase-5, a enzima que degrada o GMPc, e assim prolonga o efeito do pouco óxido nítrico que ainda existe. Duas drogas, dois pontos diferentes da mesma cadeia, um único efeito mecânico — a porta abre.])

#conclusao-box[
O princípio que costura as três partes é que motilidade nunca foi um problema de força, e sim de geometria controlada no tempo. Músculo liso capaz de contrair, sozinho, não move nada: um anel que aperta sem que o segmento vizinho relaxe apenas espreme o conteúdo para os dois lados. O que transforma contração em transporte é a decisão de onde contrair e onde relaxar, tomada segmento a segmento.

Essa decisão desce por uma cadeia única, e vale reconstruí-la inteira. Distensão da parede aciona o mecanorreceptor; o circuito da parede escolhe o braço excitatório atrás e o inibitório à frente; acetilcolina ou VIP e óxido nítrico atravessam a fenda larga da junção neuroefetora; dentro da célula, o cálcio sobe ou desce e o balanço entre a quinase da cadeia leve e a miosina fosfatase define quantas miosinas estão fosforiladas naquele instante. Tudo o que o tubo faz de motor — peristalse, segmentação, abertura de esfíncter, tônus sustentado — é uma configuração diferente dessa mesma cadeia. O mecanismo nuclear, portanto, cabe numa frase: força no músculo liso é a fração de cadeias leves de miosina fosforiladas, e todo o resto do sistema existe para regular essa fração.

A clínica que apareceu ao longo do texto agora se lê pelo mesmo eixo, e não como lista de doenças. Chagas e acalasia são a mesma lesão em locais diferentes — perda dos neurônios inibitórios, esfíncter que não relaxa, dilatação a montante por pressão crônica. A doença do refluxo é o defeito espelhado: tônus insuficiente onde ele deveria existir. O íleo adinâmico é o excesso do freio simpático desligando o braço excitatório. E as drogas que tratam esses quadros não fazem nada de novo — elas entram na cadeia num ponto específico, seja bloqueando a entrada de cálcio, seja repondo o óxido nítrico que o neurônio inibitório não entrega mais.

O próximo passo é trocar o efetor mantendo o circuito. O plexo submucoso, os mesmos mecanorreceptores e os mesmos reflexos curto e longo comandam também as glândulas e o epitélio — e é assim que o tubo acopla, no mesmo instante, o movimento do conteúdo e a secreção que vai digeri-lo.
]
