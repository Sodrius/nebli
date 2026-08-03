#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Você já sabe que a glicose é o principal combustível da célula, e já viu a glicólise quebrá-la para arrancar energia. Mas a célula não vive só de energia: ela também precisa *construir* — fabricar membranas, montar DNA e RNA, e se defender de moléculas que a corroem por dentro. Para essas tarefas de construção, a glicose toma um desvio: a *via das pentoses-fosfato*. Ela não gera ATP. Em vez disso, entrega dois produtos que nenhuma outra parte do metabolismo da glicose fornece: o *poder redutor* na forma de NADPH e o *açúcar de 5 carbonos* que vira material genético. Este resumo segue um fio único: primeiro o que a via entrega e por que ela existe (PARTE I), depois como ela funciona por dentro e como a célula liga cada parte conforme a necessidade (PARTE II), e por fim por que, sem o NADPH dela, o glóbulo vermelho se rompe sob estresse — a história clínica que fecha o assunto (PARTE III).
]

#parte-title("PARTE I — O que a via entrega e por que ela existe", primeira: true)

#subtopico("1.1 — Os três destinos da glicose-6-fosfato")

Assim que a glicose entra na célula, ela é imediatamente fosforilada a #sigla("G6P", [glicose-6-fosfato — a glicose com um fosfato no carbono 6, forma em que ela fica "presa" dentro da célula]), e é a partir desse ponto que a célula decide o que fazer com o açúcar. Há três caminhos possíveis, e escolher entre eles é uma decisão de economia interna. A G6P pode ser guardada como reserva, sendo polimerizada em glicogênio para uso posterior. Pode descer a glicólise, sendo quebrada em piruvato para arrancar energia — o destino que rende #sigla("ATP", [adenosina trifosfato — a moeda de energia da célula]). Ou pode entrar na *via das pentoses-fosfato*, e é aqui que mora a novidade desta aula.

O ponto que precisa ficar claro desde já é que a via das pentoses não existe para produzir energia. Ela existe para produzir *insumos de construção*. Enquanto a glicólise é uma linha de produção de ATP, a via das pentoses é uma fábrica de peças: o poder redutor que as reações de síntese consomem e o esqueleto de açúcar que o material genético exige. Confundir os propósitos das duas vias é o erro mais comum do tema, e vamos voltar a ele várias vezes.

#mini-resumo[Se você só lembrar de uma coisa: a G6P tem três saídas — reserva (glicogênio), energia (glicólise) e construção (via das pentoses). A via das pentoses é a saída de construção, não de energia.]

#subtopico("1.2 — Dois produtos, um propósito: NADPH e ribose-5-fosfato")

Tudo o que a via das pentoses faz pode ser resumido em dois produtos que ela coloca na mesa. O primeiro é o #sigla("NADPH", [nicotinamida adenina dinucleotídeo fosfato reduzido — o transportador de poder redutor usado nas reações de construção]), uma coenzima carregada de elétrons que as vias de biossíntese usam como "moeda de construção". Sempre que a célula precisa *reduzir* alguma coisa para montá-la — encaixar hidrogênios na síntese de ácidos graxos e de colesterol, ou recarregar um antioxidante gasto —, é o NADPH que paga a conta em elétrons. O segundo produto é a #termo-nota[ribose-5-fosfato][açúcar de 5 carbonos fosforilado que forma o esqueleto dos nucleotídeos, e portanto do DNA e do RNA], o açúcar de cinco carbonos que serve de esqueleto para os *nucleotídeos*#footnote[nucleotídeo: a unidade que forma DNA e RNA — uma base nitrogenada, mais um açúcar de 5 carbonos (a ribose), mais fosfato.]. Sem ribose, a célula não monta #sigla("DNA", [ácido desoxirribonucleico]), #sigla("RNA", [ácido ribonucleico]), nem coenzimas como ATP, #sigla("NAD", [nicotinamida adenina dinucleotídeo — transportador de elétrons do catabolismo])#super[+], #sigla("FAD", [flavina adenina dinucleotídeo — coenzima transportadora de elétrons]) e a #sigla("CoA", [coenzima A — carregadora de grupos acila no metabolismo]).

Repare no que a via *não* faz: ela não produz nem consome ATP como saldo líquido. Toda a lógica é entregar poder redutor e açúcar-esqueleto, não energia. É por isso que uma célula que está crescendo e se dividindo — e portanto duplicando seu DNA — depende tanto desta via, e por isso também que uma célula que fabrica gordura, como a do fígado ou a do tecido adiposo, a mantém sempre ligada.

#figura-nebli("/figuras/bioq-20-pentoses-radicais-livres/slide-08.png",
  largura: 60%,
  legenda: [A via em uma imagem: a glicose-6-fosfato (6 carbonos) é convertida em ribose-5-fosfato (5 carbonos), liberando 1 CO#sub[2] e gerando 2 NADPH. Os produtos podem seguir para a síntese de nucleotídeos ou ser reciclados como frutose-6-fosfato e gliceraldeído-3-fosfato — os intermediários que a via compartilha com a glicólise.])

O açúcar de cinco carbonos que a via entrega, a ribose, é quase idêntico à desoxirribose que forma o DNA — a diferença é apenas uma hidroxila a mais no carbono 2. Essa proximidade estrutural é o que permite à célula partir da ribose para montar todo o repertório de nucleotídeos.

#figura-lateral("/figuras/bioq-20-pentoses-radicais-livres/slide-33.png",
  lado: "right",
  largura-figura: 34%,
  texto: [A ribose (à direita na figura) tem hidroxilas nos carbonos 2 e 3; a desoxirribose (à esquerda) perdeu a do carbono 2 — daí o "desoxi". A via das pentoses fornece a ribose-5-fosfato; uma redução posterior, feita à custa de NADPH, é o que a converte em desoxirribose para o DNA. Ou seja, os dois produtos da via se encontram: a ribose vira esqueleto, e o poder redutor a transforma na versão do DNA.],
  legenda: [Ribose vs. desoxirribose])

#subtopico("1.3 — NADPH não é NADH: duas moedas redutoras separadas")

Aqui está a inversão que mais derruba o estudante, e vale enfrentá-la de frente. Olhando a fórmula, o NADPH e o #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzido — transportador de elétrons do catabolismo, alimenta a produção de ATP]) são quase gêmeos: a única diferença é um grupo fosfato extra no NADPH. E, no entanto, os dois têm papéis *opostos* no metabolismo. A intuição de que "moléculas quase iguais fazem quase a mesma coisa" é exatamente o que induz ao erro.

O NADH é o transportador do *catabolismo*: ele é gerado quando a célula oxida combustíveis (na glicólise, no ciclo de Krebs) e entrega seus elétrons à cadeia respiratória#footnote[cadeia respiratória: a sequência de complexos na mitocôndria que recebe os elétrons do NADH e os usa para fabricar ATP — é a moeda da produção de energia.] para fabricar ATP. O NADPH faz o contrário: ele é gerado na via das pentoses e *doa* elétrons para as reações de construção — a #termo-nota[biossíntese redutora][reações que constroem moléculas grandes, como ácidos graxos e colesterol, adicionando elétrons e hidrogênios; consomem NADPH] de lipídios e a regeneração dos antioxidantes. Um leva elétrons para *queimar*; o outro leva elétrons para *construir e proteger*.

E o fosfato extra? Ele é a *etiqueta* que as enzimas leem para não confundir os dois estoques. Uma enzima que precisa oxidar um combustível procura NAD#super[+]; uma enzima que precisa reduzir um substrato de construção procura NADPH. A célula mantém os dois pools em concentrações muito diferentes justamente para manter os fluxos separados: a razão NAD#super[+]/NADH fica em torno de 1000 (há muito NAD#super[+] oxidado disponível, pronto para *receber* elétrons e oxidar combustível), enquanto a razão NADPH/#sigla("NADP", [nicotinamida adenina dinucleotídeo fosfato oxidado — a forma que a G6PD reduz a NADPH])#super[+] é mantida alta (há muito NADPH reduzido disponível, pronto para *doar* elétrons e construir). Mesma química de óxido-redução, dois propósitos que a célula trata de manter sempre separados.

#figura-lateral("/figuras/bioq-20-pentoses-radicais-livres/slide-09.png",
  lado: "left",
  largura-figura: 40%,
  texto: [A única diferença estrutural entre as duas moléculas é o fosfato destacado em vermelho no NADPH, ligado à ribose da adenina. Estruturalmente trivial; funcionalmente decisiva. Esse fosfato é o crachá que separa a "bateria de construção" (NADPH) da "bateria de energia" (NADH), permitindo que a célula direcione cada uma para o tipo certo de reação sem que uma invada o território da outra.],
  legenda: [NADPH (esq.) e NADH (dir.): o fosfato extra em vermelho])

#confusao-prevista(
  titulo: "NADPH e NADH não são intercambiáveis",
  aluno_acha: [como só diferem por um fosfato, o aluno assume que um pode substituir o outro],
  mecanismo: [na prática, enzimas de biossíntese só aceitam NADPH e enzimas da cadeia respiratória só aceitam NADH. NADPH constrói e protege; NADH alimenta a produção de ATP. O fosfato existe justamente para que a célula mantenha os dois fluxos separados.],
)

#subtopico("1.4 — Onde, quando e quanto: citosol, tecidos que constroem e a hemácia")

Sabendo o que a via entrega, dá para prever onde e quando ela roda com mais força, e isso amarra a PARTE I à fisiologia. A via inteira acontece no *citosol*, sem entrar na mitocôndria, e por ela passa cerca de 20% da glicose numa célula típica. Mas essa média esconde grandes diferenças entre tecidos. A via é mais ativa exatamente onde a demanda por seus produtos é maior: no fígado, no tecido adiposo, na glândula mamária em lactação e no córtex adrenal — tecidos que *sintetizam* ácidos graxos, colesterol ou hormônios esteroides, todos consumidores vorazes de NADPH. Ela também é ativa em qualquer célula em divisão intensa, que precisa de ribose para duplicar o material genético.

Quanto ao *quando*, a via liga preferencialmente quando há glicose disponível e a glicólise está freada — situação típica de fartura energética, com ATP alto, em que a célula tem açúcar de sobra e pode desviá-lo para a construção em vez de queimá-lo.

Há um tecido, porém, que merece destaque desde já porque será o protagonista da PARTE III: a *hemácia*#footnote[hemácia: o glóbulo vermelho — uma célula sem núcleo e sem mitocôndria, cheia de hemoglobina; não fabrica proteínas novas nem produz ATP/NADPH pela mitocôndria.]. Sem mitocôndria, a hemácia não tem nenhuma outra maneira de fabricar NADPH — a via das pentoses é a sua *única* fonte de poder redutor. Guarde essa dependência absoluta: ela é a chave para entender por que uma falha nesta via, que muitos tecidos toleram, é catastrófica no glóbulo vermelho.

#mini-resumo[O que ficou de pé: a via entrega NADPH (poder redutor para construir e proteger) e ribose (esqueleto de nucleotídeos), roda no citosol, e é vital em tecidos que sintetizam lipídios e na hemácia — que não tem outra fonte de NADPH.]

#parte-title("PARTE II — Como a via funciona por dentro")

#subtopico("2.1 — Duas fases: uma que oxida, outra que rearranja")

A via das pentoses não é uma linha reta: ela se divide em duas fases de naturezas bem diferentes, e entender essa divisão é o que permite prever o comportamento da via em cada situação. A primeira é a *fase oxidativa*: ela é irreversível, oxida a glicose-6-fosfato e, nesse processo, produz o NADPH, além de liberar um CO#sub[2] e gerar o primeiro açúcar de cinco carbonos. É a fase que *fabrica* poder redutor. A segunda é a *fase não-oxidativa*: ela é reversível, não produz NADPH nenhum, e se limita a *rearranjar* açúcares — interconverter moléculas de 3 a 7 carbonos, embaralhando esqueletos para produzir exatamente o açúcar de que a célula precisa naquele momento.

A consequência prática dessa divisão é enorme: como as duas fases são independentes, a célula pode rodá-las em velocidades diferentes. Pode acionar só a parte que fabrica NADPH, só a parte que rearranja açúcares, ou as duas juntas — dependendo do que falta. As duas subseções seguintes destrincham cada fase, e a subseção 2.4 mostra como a célula combina as duas conforme a demanda.

#subtopico("2.2 — Fase oxidativa: a G6PD abre o caminho e solta NADPH")

A fase oxidativa é onde nasce o NADPH, e ela se resolve em três reações encadeadas que vale acompanhar passo a passo. A primeira é a reação decisiva: a enzima #sigla("G6PD", [glicose-6-fosfato desidrogenase — a enzima que abre a via das pentoses e controla sua velocidade]), a glicose-6-fosfato desidrogenase, oxida a glicose-6-fosfato a uma lactona (a 6-fosfoglicono-δ-lactona) e, ao arrancar esses elétrons, reduz um NADP#super[+] a NADPH. Essa primeira reação é *irreversível* e é o passo controlador de toda a via — guarde a G6PD, porque é dela que a PARTE III vai depender inteiramente. Em seguida, uma lactonase hidrolisa a lactona, abrindo-a em 6-fosfogliconato. E na terceira reação a 6-fosfogliconato desidrogenase faz duas coisas ao mesmo tempo: oxida o 6-fosfogliconato — gerando o *segundo* NADPH — e o *descarboxila*, liberando um #sigla("CO2", [dióxido de carbono]) e encurtando a molécula de seis para cinco carbonos, que sai como ribulose-5-fosfato. Uma isomerase simples então converte a ribulose-5-fosfato em ribose-5-fosfato, o produto que vai para os nucleotídeos.

O saldo da fase oxidativa, portanto, é limpo: para cada glicose-6-fosfato que entra, saem *2 NADPH*, *1 CO#sub[2]* e uma pentose. Note que o CO#sub[2] da via das pentoses é liberado *aqui*, na descarboxilação da terceira reação — é uma das poucas reações do metabolismo dos carboidratos, fora o ciclo de Krebs, que solta carbono como CO#sub[2].

#figura-nebli("/figuras/bioq-20-pentoses-radicais-livres/slide-16.png",
  largura: 72%,
  legenda: [A fase oxidativa (setas verdes, à esquerda) e sua conexão com a glicólise (setas laranjas, à direita). A glicose-6-fosfato é oxidada pela G6PD, passa por 6-fosfogliconato e chega a ribulose-5-fosfato, gerando 2 NADPH e 1 CO#sub[2]; a ribulose vira ribose-5-fosfato. Repare que as duas vias partem do mesmo ponto — a glicose-6-fosfato — e que os produtos da via das pentoses podem retornar à glicólise como gliceraldeído-3-fosfato e frutose-6-fosfato.])

#subtopico("2.3 — Fase não-oxidativa: remontar o carbono sem gastar NADPH")

A fase não-oxidativa resolve um problema de contabilidade de carbono. Às vezes a célula precisa de ribose mas não de tanto NADPH; às vezes é o contrário, e sobra ribose que seria desperdiçada. É aqui que entram duas enzimas que funcionam como carpinteiros do açúcar, cortando e colando pedaços de carbono para remontar as moléculas. A #termo-nota[transcetolase][enzima da fase não-oxidativa que transfere blocos de 2 carbonos de um açúcar para outro] transfere blocos de *dois carbonos* de uma cetose para uma aldose; a #termo-nota[transaldolase][enzima da fase não-oxidativa que transfere blocos de 3 carbonos de um açúcar para outro] transfere blocos de *três carbonos*. Trabalhando juntas, e ajudadas por isomerases e epimerases que apenas rearranjam as pentoses, elas convertem açúcares de cinco carbonos em açúcares de seis (#sigla("F6P", [frutose-6-fosfato — intermediário compartilhado entre a via das pentoses e a glicólise])) e de três (#sigla("G3P", [gliceraldeído-3-fosfato — intermediário compartilhado entre a via das pentoses e a glicólise])).

O detalhe que faz toda a diferença é que a F6P e o G3P são exatamente intermediários da *glicólise*#footnote[glicólise: a sequência que quebra a glicose em piruvato no citosol, rende ATP e NADH, e passa pelos intermediários glicose-6-P, frutose-6-P e gliceraldeído-3-P — os mesmos que a via das pentoses usa.]. Por isso a fase não-oxidativa é a "porta giratória" entre a via das pentoses e a glicólise: como todas as suas reações são reversíveis, a via pode *tanto* transformar pentoses em intermediários glicolíticos *quanto* fazer o inverso — pegar frutose-6-fosfato e gliceraldeído-3-fosfato da glicólise e montar ribose sem passar pela fase oxidativa. Essa reversibilidade é o que dá à célula a flexibilidade que a subseção seguinte explora.

#figura-nebli("/figuras/bioq-20-pentoses-radicais-livres/slide-49.png",
  largura: 66%,
  legenda: [As enzimas da fase não-oxidativa. A transcetolase move blocos de 2 carbonos; a transaldolase move blocos de 3 carbonos; isomerase e epimerase apenas rearranjam as pentoses. O resultado é a interconversão reversível entre açúcares de 3, 4, 5, 6 e 7 carbonos — a célula "remonta" o esqueleto conforme a necessidade, sem gerar nem gastar NADPH nesta fase.])

#subtopico("2.4 — Quatro cenários de demanda: como a célula escolhe o ramo")

Juntando as duas fases, dá para entender por que a via é tão versátil: a célula liga a fase oxidativa, a não-oxidativa, ou as duas, conforme o que está faltando. O erro a evitar é imaginar que a via sempre roda inteira, do começo ao fim. Na verdade ela funciona por combinação, e há quatro cenários que cobrem quase tudo o que acontece na prática.

No primeiro cenário, a célula precisa *só de ribose* — é o caso de uma célula em divisão intensa, que duplica o DNA mas não tem grande demanda por NADPH. Ela roda *só a fase não-oxidativa*, montando ribose a partir de frutose-6-fosfato e gliceraldeído-3-fosfato desviados da glicólise, sem sequer acionar a G6PD. No segundo, a demanda por NADPH e por ribose é *equilibrada*: aí predomina a fase oxidativa, que entrega os dois de uma vez. No terceiro, a célula precisa de *muito NADPH e pouca ribose* — o cenário clássico do tecido que fabrica ácidos graxos. Ela roda a fase oxidativa para gerar NADPH e, em seguida, usa a fase não-oxidativa para *reciclar* a ribose excedente de volta a frutose-6-fosfato e gliceraldeído-3-fosfato, que reentram na via para render ainda mais NADPH. No quarto, a célula precisa de NADPH *e* de ATP: roda as duas fases e manda o gliceraldeído-3-fosfato resultante descer a glicólise para gerar energia.

A tabela abaixo condensa os quatro cenários, porque aqui há três dimensões que se cruzam — o que a célula precisa, qual ramo ela liga, e se há geração de NADPH — e vê-las lado a lado torna o padrão evidente.

#table(
  columns: (auto, auto, auto),
  inset: 7pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    [*Do que a célula precisa*], [*Qual ramo ela liga*], [*Gera NADPH?*]
  ),
  [Só ribose (célula em divisão)], [Só a fase não-oxidativa, a partir de F6P/G3P], [Não],
  [NADPH e ribose em igual medida], [Predomina a fase oxidativa], [Sim (2 por G6P)],
  [Muito NADPH, pouca ribose (lipogênese)], [Oxidativa + não-oxidativa reciclando a ribose], [Sim, maximizado],
  [NADPH e ATP], [Oxidativa + não-oxidativa; o G3P desce a glicólise], [Sim, e ainda rende ATP],
)

#confusao-prevista(
  titulo: "A via não roda sempre inteira",
  aluno_acha: [o aluno imagina que toda vez a glicose percorre a via do início ao fim],
  mecanismo: [a célula aciona apenas o ramo de que precisa: só a não-oxidativa quando quer ribose sem NADPH, ou os dois ramos quando quer maximizar NADPH. O custo de rodar só a não-oxidativa é apenas 1 ATP da hexoquinase, e nenhum NADPH é desperdiçado.],
)

#subtopico("2.5 — O termostato da via: a razão NADPH/NADP+ e a G6PD")

Falta explicar quem decide *quanto* a via oxidativa roda, e a resposta é elegante porque a via se autorregula pelo próprio produto. O controle principal não vem de fora, de um hormônio distante, mas de dentro, imediato: a G6PD — o passo controlador que conhecemos na subseção 2.2 — é *ativada* pelo NADP#super[+] e *inibida* pelo NADPH. Ou seja, o produto da via desliga a enzima que o fabrica, um caso clássico de #termo-nota[inibição por produto][quando o produto de uma via se liga à enzima controladora e a desliga, evitando fabricar o que já há de sobra].

O sensor real, portanto, é a *razão NADPH/NADP#super[+]*. Quando a célula está "cheia" de poder redutor, o NADPH acumulado trava a G6PD e a via desacelera — não faz sentido continuar produzindo o que não está sendo gasto. Mas assim que uma via de construção ou a defesa antioxidante *consome* NADPH, o NADP#super[+] volta a subir, a inibição sobre a G6PD é aliviada e a via reacelera para repor o estoque. É um termostato químico: a via responde em tempo real ao próprio consumo, sem precisar de nenhum sinal externo.

#figura-nebli("/figuras/bioq-20-pentoses-radicais-livres/slide-51.png",
  largura: 62%,
  legenda: [A regulação da via. A G6PD (destacada) é o passo controlador: o NADPH, produto da via, inibe-a por competição, enquanto o NADP#super[+] a estimula. A razão NADPH/NADP#super[+] funciona como sensor — alta trava a via, baixa a libera. Assim a célula fabrica NADPH exatamente no ritmo em que o consome.])

#mini-resumo[Em uma frase: a fase oxidativa (irreversível, faz 2 NADPH + CO#sub[2] + ribose) é comandada pela G6PD, que a razão NADPH/NADP#super[+] liga e desliga; a fase não-oxidativa (reversível, sem NADPH) remonta açúcares e conversa com a glicólise nos dois sentidos.]

#parte-title("PARTE III — NADPH contra os radicais livres")

#subtopico("3.1 — Radicais livres: o preço de respirar oxigênio")

Chegamos ao motivo pelo qual todo esse poder redutor importa clinicamente, e ele começa com um paradoxo do oxigênio. O O#sub[2] que nos mantém vivos é também uma ameaça constante, porque a própria respiração é imperfeita: cerca de 0,2% de todo o oxigênio que a cadeia respiratória processa escapa parcialmente reduzido, formando um *radical livre*#footnote[radical livre: átomo ou molécula com um elétron desemparelhado, o que o torna muito reativo e ávido por arrancar elétrons de outras moléculas.]. Isso soma cerca de 400 gramas de superóxido por ano num adulto — não é um evento raro, é um gotejamento permanente.

O problema não para no primeiro radical, porque as #sigla("ERO", [espécies reativas de oxigênio — moléculas derivadas do O#sub[2] com alta reatividade, como superóxido, peróxido de hidrogênio e radical hidroxila]) se convertem umas nas outras numa cascata. O oxigênio ganha um elétron e vira #termo-nota[superóxido][primeira espécie reativa da cascata, formada quando o O#sub[2] recebe um único elétron]; o superóxido, processado pela superóxido dismutase, vira peróxido de hidrogênio; e o peróxido de hidrogênio, se não for neutralizado, pode gerar o radical hidroxila, o mais agressivo de todos. Um detalhe que amarra esse ponto ao ferro: na *reação de Fenton*, o peróxido de hidrogênio reage com ferro na forma Fe#super[2+] e produz diretamente o radical hidroxila — é por isso que ferro livre na célula é perigoso, e por isso que manter o ferro sob controle importa tanto. Enzimas como a catalase e a glutationa peroxidase existem justamente para desarmar essa cascata antes que ela corroa lipídios de membrana, proteínas e o DNA.

#figura-nebli("/figuras/bioq-20-pentoses-radicais-livres/slide-39.png",
  largura: 60%,
  legenda: [A cascata das espécies reativas de oxigênio. O O#sub[2] é reduzido por etapas — superóxido, peróxido de hidrogênio, radical hidroxila — até água. A superóxido dismutase e a glutationa peroxidase/catalase interrompem a cascata em cada ponto. A reação de Fenton (H#sub[2]O#sub[2] + Fe#super[2+]) mostra por que o ferro livre acelera a formação do radical hidroxila.])

#subtopico("3.2 — A glutationa: o escudo que o NADPH mantém carregado")

O elo que conecta a via das pentoses à defesa antioxidante tem nome: *glutationa*. Ela é um tripeptídeo pequeno (glutamato-cisteína-glicina), e sua arma é o grupo tiol (-SH) da cisteína, que doa elétrons com facilidade. Na forma reduzida, chamada #sigla("GSH", [glutationa reduzida — o antioxidante que doa elétrons para neutralizar peróxidos]), a glutationa entrega seus elétrons ao peróxido de hidrogênio — reação catalisada pela glutationa peroxidase —, neutralizando-o em água. Ao fazer isso, porém, ela própria se oxida: duas moléculas se unem por uma ponte dissulfeto e formam a #sigla("GSSG", [glutationa oxidada — o dímero formado depois que a GSH doa seus elétrons; precisa ser reduzido de volta]), a forma oxidada e inativa.

E aqui fecha o circuito de toda a aula. Para voltar a proteger a célula, a GSSG precisa ser *reduzida* de volta a duas GSH — e a enzima que faz isso, a glutationa redutase, paga essa redução com *NADPH*. Sem NADPH, a glutationa fica presa na forma oxidada, o escudo permanece descarregado, e as espécies reativas passam a corroer a célula livremente. A cadeia causal é direta e vale memorizar como um todo: a G6PD gera NADPH, o NADPH recarrega a glutationa, e a glutationa reduzida neutraliza as ERO. Tire qualquer elo e o seguinte cai.

#figura-nebli("/figuras/bioq-20-pentoses-radicais-livres/slide-41.png",
  largura: 74%,
  legenda: [O circuito completo, da via das pentoses à remoção do radical. À direita, a G6PD gera NADPH; o NADPH alimenta a glutationa redutase, que converte GSSG em 2 GSH; a GSH, via glutationa peroxidase, neutraliza o peróxido de hidrogênio em água. Se a G6PD falha (esquerda), o NADPH não é reposto, a glutationa não recarrega e o dano oxidativo a lipídios, proteínas e DNA avança.])

#subtopico("3.3 — A hemácia no fio da navalha")

De todas as células do corpo, a hemácia é a que vive mais perto do limite dessa defesa, e entender por quê explica toda a clínica que vem a seguir. Pense na situação dela: seu trabalho é carregar oxigênio, então ela está permanentemente exposta a uma fonte de espécies reativas. Ao mesmo tempo, ela não tem mitocôndria — logo, como vimos na PARTE I, a via das pentoses é sua *única* fonte de NADPH. E, por fim, ela não tem núcleo nem ribossomos, então não consegue fabricar enzimas novas para repor as que forem danificadas. A hemácia é, portanto, uma célula que enfrenta muito estresse oxidativo com um único cano de abastecimento de defesa e nenhuma peça de reposição.

Enquanto a via das pentoses funciona, esse arranjo precário se sustenta: o NADPH mantém a glutationa reduzida, e a glutationa protege dois alvos críticos — os lipídios da membrana e o ferro da hemoglobina, que precisa permanecer na forma Fe#super[2+] para transportar oxigênio. Mas se o suprimento de NADPH falha, os dois alvos caem juntos: a hemoglobina se oxida, desnatura e precipita dentro da célula em grumos chamados #termo-nota[corpos de Heinz][precipitados de hemoglobina oxidada e desnaturada dentro da hemácia, sinal de dano oxidativo], e a membrana, sem proteção, é danificada. A célula rígida e marcada é então destruída — a hemácia hemolisa.

#figura-nebli("/figuras/bioq-20-pentoses-radicais-livres/slide-27.png",
  largura: 60%,
  legenda: [Na hemácia (à esquerda), a via das pentoses alimenta o ciclo da glutationa (à direita): a glutationa reduzida mantém as proteínas na forma ativa e o ferro da hemoglobina como Fe#super[2+]. É esse fornecimento contínuo de NADPH que impede a oxidação da hemoglobina e a ruptura da célula.])

#subtopico("3.4 — Deficiência de G6PD: favismo, primaquina e malária")

Agora que a dependência da hemácia está clara, a doença se explica sozinha. A #termo-nota[deficiência de G6PD][a enzimopatia mais comum do mundo; reduz a produção de NADPH na hemácia e a expõe à hemólise sob estresse oxidativo] é a *enzimopatia*#footnote[enzimopatia: doença causada por defeito em uma enzima.] mais comum do mundo, afetando cerca de 400 milhões de pessoas. O ponto que precisa ser entendido é *quando* ela se manifesta: em repouso, a G6PD deficiente ainda produz NADPH suficiente e a hemácia se vira bem. A crise só aparece quando um *estresse oxidativo* eleva bruscamente a demanda de NADPH — e aí a enzima insuficiente não dá conta, a glutationa não recarrega e vem a hemólise aguda.

O que dispara essa demanda? Classicamente, certos fármacos oxidantes, como o antimalárico *primaquina*, algumas sulfas e a dapsona; infecções, que aumentam a produção de espécies reativas pelas células de defesa; e a ingestão de favas, de onde vem o nome *favismo*. Um traço importante da herança: a deficiência de G6PD é *ligada ao X*#footnote[ligado ao X: o gene fica no cromossomo X; como o homem tem um X só, uma cópia defeituosa já o afeta, enquanto a mulher costuma ter uma segunda cópia que compensa.], por isso afeta mais os homens.

Há ainda uma reviravolta evolutiva que amarra tudo. A mesma fragilidade que torna a hemácia vulnerável ao oxidante também a torna um *hospedeiro ruim* para o parasita da malária: o Plasmodium falciparum não completa bem seu ciclo dentro de uma hemácia deficiente de G6PD. Isso dá aos portadores uma resistência parcial à malária — e é por isso que a mutação, apesar de causar doença, é tão frequente justamente nas regiões onde a malária é endêmica. A mesma falha que fragiliza a célula, num contexto, a protege, em outro.

#clinica-box("Crise hemolítica na deficiência de G6PD", [
  Um homem com deficiência de G6PD recebe primaquina para tratar malária. O fármaco eleva a produção de peróxidos na hemácia; a G6PD deficiente não repõe NADPH no ritmo necessário; a glutationa fica presa na forma oxidada (GSSG) e para de neutralizar as espécies reativas. A hemoglobina, sem proteção, oxida e precipita em corpos de Heinz, e a membrana é danificada. O resultado, em dias, é uma anemia hemolítica aguda — a mesma cadeia G6PD → NADPH → glutationa → defesa que estudamos, agora rompida elo por elo pelo oxidante.
])

#atencao-box("A hemólise depende de um gatilho", [
  O erro perigoso é imaginar que a deficiência de G6PD causa hemólise o tempo todo. Não causa: em repouso a hemácia se mantém. A crise exige um *oxidante* que dispare a demanda de NADPH — primaquina, sulfas, dapsona, infecção ou favas. Reconhecer o gatilho é o que separa o entendimento do mecanismo da simples memorização do nome da doença.
])
