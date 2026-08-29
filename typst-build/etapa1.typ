#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
O corpo não tem um metabolismo. Ele tem vários, rodando ao mesmo tempo em tecidos diferentes, e a maior parte do que parece complicado nesta aula vem de tratar todos eles como se fossem a mesma célula. O fígado quebra glicogênio para devolver glicose ao sangue; o músculo quebra o dele e não devolve nada. O tecido adiposo libera ácido graxo quando o glucagon sobe; o fígado, no mesmo instante, queima esse ácido graxo. O cérebro consome glicose sem parar e não guarda quase nenhuma. São comportamentos opostos diante do mesmo sinal hormonal, e nenhum deles é arbitrário.

A chave está numa ideia simples: *a especialização de um tecido não se explica por intensidade, e sim por repertório*. O que separa o fígado do músculo não é fazer as mesmas coisas mais rápido — é ter enzimas e transportadores que o outro não tem, e não ter alguns que o outro tem. A enzima ausente explica tanto quanto a presente: é a falta de uma única fosfatase que impede o músculo de exportar glicose, é a falta de uma única transferase que impede o fígado de queimar os corpos cetônicos que ele mesmo fabrica. Guarde esse gesto de leitura, porque ele organiza as três PARTES.

A PARTE I monta o mapa: quanto cada tecido guarda, de que forma guarda, e por que o fígado ocupa a posição que ocupa. A PARTE II entra no hepatócito e mostra, ponto de controle por ponto de controle, como a glicemia é decidida — transportador, enzima de entrada, par de vias opostas, sinal alostérico e cascata hormonal. A PARTE III percorre os demais tecidos, cada um com uma peça faltando ou sobrando, e fecha no pâncreas, que mede o resultado de tudo e reinicia o circuito.
]

#parte-title("PARTE I — Um corpo, muitos tecidos: quem guarda, quem gasta, quem manda", primeira: true)

#subtopico("1.1 Reservas desiguais: cada tecido guarda um combustível diferente")

Um adulto de setenta quilos carrega energia guardada em três moedas químicas, e elas não estão distribuídas igualmente pelos tecidos. Vale começar pelos números, porque a desproporção entre eles é o primeiro fato que organiza a aula. Em glicogênio, o fígado guarda algo em torno de quatrocentas quilocalorias e o músculo, somado, guarda cerca de mil e duzentas — três vezes mais que o fígado, simplesmente porque a massa muscular é muito maior. Em triacilglicerol, o tecido adiposo guarda perto de cento e trinta e cinco mil quilocalorias. Em proteína mobilizável, o músculo responde por vinte e quatro mil. O sangue circulante carrega umas sessenta quilocalorias de glicose livre, e o cérebro, oito.

Ponha essas grandezas lado a lado e a conclusão é desconfortável. *Todo o carboidrato armazenado do corpo dá para pouco mais de um dia*, enquanto a gordura sustentaria semanas. A razão dessa diferença é química e vale entender, porque ela reaparece em toda decisão metabólica adiante. O ácido graxo é uma cadeia de carbonos quase totalmente reduzida — cada carbono carrega hidrogênios que serão entregues como elétrons à cadeia respiratória, de onde sai o #sigla("ATP", [adenosina trifosfato — a moeda energética que a célula gasta em praticamente todo trabalho químico e mecânico]) —, ao passo que o carbono do carboidrato já vem parcialmente oxidado, com oxigênio pendurado em quase todas as posições. Só isso já mais que dobra o rendimento por grama. Some a isso o fato de que o glicogênio é uma molécula hidrofílica, que arrasta consigo duas a três vezes o próprio peso em água, enquanto a gota de gordura do adipócito é praticamente anidra. *A gordura é a reserva de longo prazo porque é densa e seca; o glicogênio é a reserva de emergência porque é rápido de mobilizar, e paga por isso em peso.*

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-05.png",
  largura: 56%,
  legenda: [As reservas de energia distribuídas pelos tecidos, em quilocalorias. Repare em duas colunas antes de mais nada: a de triacilglicerol, dominada pelo tecido adiposo por duas ordens de grandeza, e a de proteína mobilizável, concentrada no músculo. A linha do cérebro é quase toda zero — ele não guarda nada e depende inteiramente do que circula.])

Falta comentar a coluna da proteína, e é aqui que a leitura ingênua da tabela engana. As vinte e quatro mil quilocalorias em proteína muscular parecem uma reserva respeitável, e em termos de energia disponível elas são. Só que *não existe proteína de estoque*. Cada aminoácido mobilizado é retirado de uma proteína que estava fazendo alguma coisa: uma miofibrila que contraía, uma enzima que catalisava, um anticorpo que circulava. Mobilizar aminoácido para produzir glicose significa desmontar função, e é por isso que o organismo adia essa decisão o quanto pode, protegendo a massa muscular enquanto tiver glicogênio ou gordura disponíveis. O aluno que guarda apenas "proteína também vira energia" perde a hierarquia — e é a hierarquia que explica por que o emagrecimento saudável poupa músculo e a desnutrição grave não.

Uma distinção precisa ser desfeita antes de seguir, porque ela contamina tudo o que vem depois. À primeira vista, parece natural somar o glicogênio hepático ao muscular e falar em "reserva de carboidrato do corpo".

#confusao-prevista(
  titulo: "O glicogênio do músculo não é reserva do organismo",
  aluno_acha: [aluno soma as mil e duzentas quilocalorias do músculo às quatrocentas do fígado e conclui que o corpo tem mil e seiscentas quilocalorias de glicose disponíveis para a glicemia],
  mecanismo: [o músculo não expressa *glicose-6-fosfatase*. Quando ele degrada o próprio glicogênio, o produto é glicose-6-fosfato, uma molécula com carga negativa que nenhum transportador reconhece e que, por isso, não atravessa a membrana. Ela é obrigada a seguir para a glicólise ali dentro e virar ATP para a contração daquela fibra. O fígado, que tem a fosfatase, remove o fosfato e libera glicose livre no sangue. *A mesma reserva, nos dois tecidos, tem destinos incomunicáveis* — e essa é a diferença de repertório mais importante da aula inteira.],
)

#mini-resumo[Em uma frase: a gordura guarda muito porque é reduzida e seca, o glicogênio guarda pouco porque é oxidado e hidratado, e a proteína só entra na conta quando o organismo aceita perder função.]

#subtopico("1.2 A divisão do trabalho: o que cada órgão faz com o que recebe")

A imagem que a professora usa para abrir o assunto é a de uma orquestra, e ela rende mais do que parece à primeira vista. Cada tecido é um instrumento com um som próprio, nenhum toca a peça inteira sozinho, e há um maestro coordenando as entradas — no caso, os hormônios, que dizem a cada tecido o que fazer em cada momento. O que vale explicitar, porque a analogia costuma parar antes disso, é *o que constitui o "som" de cada instrumento*: é o conjunto de enzimas e transportadores que aquele tecido expressa. O maestro é o mesmo para todos, mas o violino não vira trompete por receber a mesma batuta.

Percorrendo o corpo com essa lente, o mapa fica curto. O *intestino* absorve os nutrientes da dieta e os empurra para dois caminhos distintos, conforme sejam hidrossolúveis ou não. O *sistema linfático* carrega os lipídios absorvidos até a circulação. O *fígado* recebe o resto e processa carboidrato, aminoácido e gordura, sintetiza e distribui lipídio, corpo cetônico e glicose para os outros tecidos, e converte o excesso de nitrogênio em ureia. O *tecido adiposo* sintetiza, armazena e mobiliza triacilglicerol. O *músculo esquelético* consome ATP para trabalho mecânico. O *cérebro* gasta energia para manter gradientes iônicos, integra sinais que vêm do corpo inteiro e devolve comandos. E o *pâncreas* secreta insulina e glucagon conforme a concentração de glicose no sangue — ele é o instrumento que escuta os outros.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-06.png",
  largura: 66%,
  legenda: [A divisão do trabalho metabólico entre os órgãos. Vale ler a figura duas vezes: uma seguindo as setas de nutriente (intestino para o fígado pela veia porta, intestino para a circulação pelo linfático) e outra seguindo as setas de informação (pâncreas medindo glicemia, cérebro integrando e comandando). O fígado é o único que aparece nos dois circuitos.])

Falta a peça que dá ao fígado a posição central: a velocidade com que ele se reorganiza. Ele é capaz de aumentar ou diminuir a concentração de uma enzima em poucas horas, aumentando ou reduzindo a transcrição do gene correspondente, e essa é a forma mais poderosa de regular uma via — se não há enzima, não há reação. Só que ela é lenta, porque exige transcrever, traduzir e degradar proteína. *Por isso o controle metabólico opera em três velocidades encaixadas.* A mais rápida é a alostérica, instantânea: um metabólito se liga fora do sítio catalítico, a enzima muda de forma e a velocidade muda junto, sem que nada seja sintetizado ou destruído. A intermediária é a modificação covalente, de segundos a minutos: uma quinase pendura um fosfato e uma fosfatase o retira, ligando ou desligando a enzima conforme o caso, e é por esse degrau que os hormônios agem. A mais lenta é a mudança de quantidade de enzima, de horas a dias, e é ela que adapta o fígado a uma dieta que mudou de vez. Guarde as três: a PARTE II inteira é a aplicação delas ao mesmo órgão.

#subtopico("1.3 A circulação porta: por que o fígado vê tudo primeiro")

Toda a lógica do subtópico anterior depende de um detalhe anatômico que costuma passar batido. O sangue que drena o intestino não segue direto para o coração. Ele é recolhido pela veia porta e despejado no fígado, que o filtra antes de devolvê-lo à circulação geral. A consequência é dupla, e as duas metades importam.

A primeira metade é metabólica. *A glicose absorvida chega ao hepatócito antes de chegar a qualquer outro tecido, e chega concentrada.* Depois de uma refeição rica em carboidrato, a concentração de glicose no sangue portal é bem maior do que a que se mede numa veia do braço, justamente porque o fígado ainda não retirou a sua parte. É essa concentração alta que aciona os mecanismos de captação hepática que a PARTE II vai detalhar — e isso não é coincidência de arranjo, é o desenho do sistema: o órgão encarregado de amortecer a glicemia foi posto exatamente onde a onda de glicose passa primeiro. O mesmo vale para os aminoácidos da dieta, que chegam ao fígado antes de ficarem disponíveis para a síntese proteica dos outros tecidos.

#figura-lateral("/figuras/biomol-04-integracao-metabolica-i/slide-40.png",
  lado: "right",
  largura-figura: 42%,
  texto: [Os dois caminhos destacados na figura resolvem problemas diferentes. A veia porta leva ao fígado o que é hidrossolúvel — glicose, aminoácido, frutose, e também o que veio junto de indesejável. O vaso linfático leva o que é lipídico, porque a gordura da dieta sai do enterócito empacotada em partículas grandes demais para entrar no capilar sanguíneo. Por esse desvio, *a gordura da refeição alcança músculo e tecido adiposo antes de passar pelo fígado* — exatamente o inverso do que acontece com a glicose.],
  legenda: [Veia porta e sistema linfático: as duas portas de entrada dos nutrientes absorvidos.])

A segunda metade é defensiva. Tudo o que foi absorvido no intestino, inclusive o que não deveria ter sido, encontra o fígado antes de alcançar o cérebro ou o coração. É essa posição de sentinela que dá sentido ao papel de detoxificação: o hepatócito recebe a molécula estranha, oxida-a e a conjuga a grupos que a tornam mais hidrossolúvel, de modo que o rim consiga excretá-la ou a bile consiga carregá-la. Vale ser preciso quanto ao verbo, porque a palavra engana — *detoxificar é transformar, não eliminar*, e a transformação nem sempre reduz a toxicidade. Alguns medicamentos chegam inativos e só são ativados nessa passagem; outros são tão eficientemente degradados na primeira passagem pelo fígado que pouco deles alcança a circulação, e é por isso que a dose oral de vários fármacos é muito maior que a dose injetada.

#subtopico("1.4 O painel do hepatócito: glicose-6-fosfato como encruzilhada")

Uma molécula de glicose acabou de atravessar a membrana do hepatócito. O que acontece com ela em seguida decide quase tudo, e o ponto de decisão é uma única molécula: a glicose-6-fosfato. Ela é a forma em que a glicose existe dentro da célula, e é dali que partem quatro caminhos concorrentes.

O primeiro caminho é o glicogênio: a glicose-6-fosfato é isomerizada e polimerizada, e o carbono fica guardado numa árvore ramificada dentro do próprio citoplasma. O segundo é a glicólise, que quebra a molécula até piruvato, e daí para acetil-CoA — matéria-prima tanto para o ciclo de Krebs, quando falta ATP, quanto para a síntese de ácido graxo e de colesterol, quando sobra. O terceiro é a via das pentoses-fosfato, que não rende ATP nenhum e não existe para isso: ela entrega #sigla("NADPH", [nicotinamida adenina dinucleotídeo fosfato reduzido — o doador de elétrons das vias de biossíntese, diferente do NADH, que alimenta a cadeia respiratória]) para as sínteses redutoras e ribose-5-fosfato para os nucleotídeos. E o quarto caminho é a saída: a glicose-6-fosfato perde o fosfato e volta ao sangue como glicose livre.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-10.png",
  largura: 58%,
  legenda: [O painel de destinos da glicose no hepatócito. A glicose-6-fosfato ocupa o centro por um motivo: todos os quatro caminhos partem dela. Repare que as duas setas horizontais no alto — glicogênio à esquerda, glicose sanguínea à direita — são as únicas reversíveis no desenho, e são justamente as que o fígado usa para amortecer a glicemia nos dois sentidos.])

Esse quarto caminho merece atenção, porque é ele que separa o fígado de quase todo o resto do corpo. A remoção do fosfato é feita pela glicose-6-fosfatase, uma enzima alojada na membrana do retículo endoplasmático, e *ela só é expressa no fígado e no córtex renal*. Todo tecido que capta glicose a fosforila imediatamente, e a razão é a mesma em todos: a glicose-6-fosfato tem carga negativa, nenhum transportador de glicose a reconhece, e ela fica presa. A fosforilação é uma catraca. O que muda de tecido para tecido é ter ou não a chave que destranca essa catraca — e ter essa chave é, por definição, ser um exportador de glicose.

#clinica-box("Quando falta a chave da catraca", [Existe uma doença hereditária em que a glicose-6-fosfatase não funciona. O quadro é um bom teste de raciocínio, porque a intuição erra o sinal: como falta a enzima que libera glicose, seria de esperar que faltasse glicogênio — e é o contrário. O fígado continua sintetizando e degradando glicogênio normalmente, mas a glicose-6-fosfato produzida na degradação não consegue sair da célula e é reincorporada ao polímero. O resultado é um fígado enorme, carregado de glicogênio, num paciente que faz hipoglicemia grave depois de poucas horas sem comer.

O restante do quadro vem por consequência direta desse acúmulo. A glicose-6-fosfato represada é empurrada para a glicólise, o piruvato produzido em excesso vira lactato, e o paciente cursa com acidose láctica. Parte do carbono transborda para a síntese de ácido graxo, produzindo hipertrigliceridemia. E o consumo elevado de fosfato dentro do hepatócito acelera a degradação de nucleotídeos de adenina, elevando o ácido úrico. *Uma enzima ausente, quatro achados laboratoriais* — e todos eles decorrem do mesmo represamento, não de quatro defeitos independentes.])

#mini-resumo[O que ficou de pé: a fosforilação prende a glicose dentro da célula, e só o fígado e o córtex renal têm a fosfatase que a solta. Quem não tem essa enzima pode guardar glicose, mas nunca devolvê-la.]

O mapa está montado. A partir daqui a lente fecha sobre o hepatócito, porque é dentro dele que os pontos de controle da glicemia estão instalados — começando pela porta de entrada.

#parte-title("PARTE II — O fígado decide a glicemia: onde o controle mora")

#subtopico("2.1 GLUT-2 e glicoquinase: dois filtros de baixa afinidade em série")

A glicose não atravessa a membrana sozinha — ela precisa de uma proteína transportadora, e existe uma família inteira delas. Todos os membros dessa família compartilham a mesma arquitetura e o mesmo mecanismo: difusão facilitada, a favor do gradiente, sem gasto de energia. Essa família é a dos #sigla("GLUT", [transportadores facilitadores de glicose — família de proteínas de membrana que deixam a glicose atravessar a favor do gradiente, sem gasto de energia]), e o que muda de um membro para outro é a *constante de Michaelis para a glicose*, o valor de concentração em que o transportador trabalha à metade da velocidade máxima. E essa diferença não é um detalhe biofísico: ela decide em que faixa de glicemia cada tecido capta glicose com avidez. Como a glicemia normal gira em torno de cinco milimolares, é esse o valor contra o qual a tabela abaixo deve ser lida.

#table(
  columns: (auto, auto, 1fr, 1.2fr),
  inset: 7pt,
  align: (left, center, left, left),
  stroke: 0.5pt + gray-border,
  table.header(
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Transportador]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Km (mM)]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Onde está]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[O que isso significa]],
  ),
  [GLUT-1], [2 a 4], [hemácia, barreira hematoencefálica], [captação basal contínua — trabalha saturado em qualquer glicemia compatível com a vida],
  [GLUT-3], [2 a 4], [neurônio], [garante entrada de glicose mesmo quando a glicemia cai],
  [GLUT-4], [cerca de 5], [músculo e adipócito], [fica guardado em vesículas e só vai para a membrana quando a insulina chega],
  [GLUT-2], [15 a 25], [hepatócito, célula beta, rim], [de baixa afinidade e sempre presente na membrana — só transporta em volume quando a glicemia está alta],
)

Repare no desenho que a tabela revela. *Os tecidos que não toleram interrupção de suprimento têm transportadores de alta afinidade*: a hemácia e o neurônio captam glicose praticamente na velocidade máxima mesmo numa hipoglicemia moderada, porque seus transportadores estão saturados desde concentrações baixas. Já o fígado tem o transportador de menor afinidade de todos. Isso significa que, na hipoglicemia, o hepatócito quase não capta — e isso é exatamente o que se quer, porque seria absurdo que o órgão encarregado de defender a glicemia competisse com o cérebro pela glicose escassa. Quando a glicemia sobe depois de uma refeição, o GLUT-2 acelera proporcionalmente, e a captação hepática dispara. O transportador funciona nos dois sentidos, o que também é necessário: é por ele que a glicose recém-liberada da glicose-6-fosfatase sai do hepatócito.

O transporte, porém, é só a primeira metade do filtro. Como a glicose entra e sai livremente pelo GLUT-2, a concentração dentro do hepatócito acompanha de perto a do sangue, e reter a molécula depende do segundo passo: a fosforilação. A enzima que faz isso no músculo, no cérebro e na maioria dos tecidos é a hexoquinase, com Km em torno de um décimo de milimolar — ela satura em qualquer glicemia e é inibida pelo próprio produto, o que a impede de consumir toda a glicose e todo o ATP da célula. No fígado, a enzima é outra: a #termo-nota[glicoquinase][hexoquinase IV, a isoforma hepática e pancreática, de baixa afinidade e cinética sigmoide], e as diferenças entre as duas são o coração deste subtópico.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-13.png",
  largura: 64%,
  legenda: [As duas curvas contam a história inteira. A hexoquinase (verde) já está praticamente na velocidade máxima na glicemia basal de cinco milimolares — a linha pontilhada. A glicoquinase (azul) mal chega à metade nesse ponto, e continua subindo enquanto a glicose sobe. Repare também no formato: a curva da glicoquinase é sigmoide, não hiperbólica, o que torna a resposta ainda mais sensível a variações na faixa fisiológica.])

Três diferenças, e cada uma resolve um problema. A primeira é a afinidade: com meia-velocidade só perto de oito milimolares, *a glicoquinase praticamente não trabalha durante o jejum*, e a glicose que entrar no hepatócito nesse momento simplesmente sai de volta pelo GLUT-2, sem ser sequestrada. A segunda é a cinética sigmoide, que amplifica a resposta: uma variação modesta de glicemia dentro da faixa fisiológica produz uma variação grande de velocidade. A terceira é a mais fina: a glicoquinase *não é inibida pela glicose-6-fosfato*. Se fosse, ela pararia de fosforilar assim que o produto se acumulasse — ou seja, pararia justamente quando o fígado mais precisa estocar. Livre dessa inibição, ela continua trabalhando enquanto houver substrato, e o produto segue para o glicogênio.

Existe ainda uma quarta camada de controle, que quase nunca é mencionada e explica um fenômeno curioso. A glicoquinase hepática é sequestrada dentro do núcleo por uma proteína reguladora quando há frutose-6-fosfato disponível — isto é, quando a via glicolítica está represada e não faz sentido fosforilar mais glicose. Quando a glicose sobe, ela desloca essa ligação e a enzima é liberada para o citoplasma, onde encontra o substrato. *É um controle de endereço somado ao controle de velocidade*, e ele acrescenta um atraso proposital: o fígado só se compromete a estocar depois que a elevação da glicemia se confirma.

#confusao-prevista(
  titulo: "Glicoquinase não é o nome hepático da hexoquinase",
  aluno_acha: [aluno trata as duas como a mesma enzima com nomes regionais, e conclui que o fígado fosforila glicose do mesmo jeito que o músculo],
  mecanismo: [são isoformas com cinéticas opostas, e cada uma serve à função do seu tecido. A hexoquinase muscular tem alta afinidade e é inibida pelo produto: ela existe para garantir que a fibra capture glicose mesmo em concentração baixa, e para se autolimitar quando já tem o bastante. A glicoquinase hepática tem baixa afinidade, curva sigmoide e escapa da inibição pelo produto: ela existe para *medir* a glicemia e só sequestrar glicose quando há excesso. Ler o Km alto como ineficiência inverte o sentido — a baixa afinidade é o mecanismo do sensor, não uma limitação dele.],
)

#clinica-box("Quando o sensor é recalibrado", [Existe uma forma hereditária de diabetes, de início precoce e curso brando, causada por mutação em um único gene: o da glicoquinase. O raciocínio é elegante e vale seguir passo a passo, porque ele confirma tudo o que foi dito acima.

Uma glicoquinase com atividade reduzida precisa de mais glicose para atingir a mesma velocidade. No fígado, isso significa que a captação e o estoque de glicose só começam com a glicemia mais alta que o normal. Na célula beta do pâncreas — que usa a mesma enzima, como a PARTE III vai mostrar — significa que a secreção de insulina também só é disparada acima do usual. *O resultado não é ausência de controle, e sim controle com o ponto de ajuste deslocado para cima:* o paciente mantém a glicemia estável, porém alguns miligramas por decilitro acima da faixa habitual, ao longo da vida inteira e com pouca progressão. O contraste com o diabetes comum é instrutivo — ali o problema é de resposta à insulina ou de falência da célula beta; aqui, o sistema funciona perfeitamente, só que regulado num valor errado.])

#subtopico("2.2 Glicólise e gliconeogênese: por que as duas não podem rodar juntas")

O fígado sabe fazer glicose e sabe destruir glicose, e as duas capacidades convivem no mesmo citoplasma. Isso cria um problema que não existe na maioria das vias: *se as duas rodarem ao mesmo tempo, o resultado líquido é zero — só que um zero caro*. Vale acompanhar a conta, porque ela é o argumento inteiro.

Primeira etapa: reconhecer que as vias não são simétricas. A glicólise quebra a glicose em dois piruvatos e rende, de saldo, dois ATP e dois #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzido — carrega elétrons até a cadeia respiratória, onde eles serão convertidos em ATP]). A gliconeogênese refaz uma glicose a partir de dois piruvatos, mas não pode simplesmente inverter a glicólise: três das dez reações liberam energia demais para serem revertidas, e precisam ser contornadas por enzimas próprias. São quatro delas — a piruvato-carboxilase e a fosfoenolpiruvato-carboxiquinase, que juntas contornam a piruvato-quinase; a frutose-1,6-bifosfatase, que contorna a fosfofrutoquinase-1; e a glicose-6-fosfatase, que contorna a glicoquinase.

Segunda etapa: somar o custo desses contornos. Cada volta consome dois ATP na piruvato-carboxilase, dois #sigla("GTP", [guanosina trifosfato — equivalente energético do ATP, usado por algumas enzimas em vez dele]) na fosfoenolpiruvato-carboxiquinase e mais dois ATP na fosfoglicerato-quinase operando ao contrário. São *seis ligações de alta energia gastas para refazer uma glicose que, ao ser quebrada, rende duas*. Lido em palavras: fabricar glicose custa três vezes o que ela devolve, e essa assimetria é o preço termodinâmico de tornar as duas direções controláveis de forma independente.

Terceira etapa: imaginar as duas ligadas simultaneamente. A fosfofrutoquinase-1 gasta um ATP para fosforilar a frutose-6-fosfato; a frutose-1,6-bifosfatase, logo em seguida, hidrolisa esse mesmo fosfato e devolve a frutose-6-fosfato. O balanço de matéria é nulo, o balanço de energia é a perda de um ATP por volta, e a energia sai como calor. É o que se chama de ciclo de substrato — e uma célula que deixasse isso acontecer sem controle queimaria ATP indefinidamente sem produzir nada.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-14.png",
  largura: 56%,
  legenda: [A regulação recíproca nos dois pontos de contorno. Em cada par, o mesmo sinal aparece com efeito oposto nas duas enzimas: a frutose 2,6-bifosfato e o AMP ativam a fosfofrutoquinase-1 e inibem a frutose-1,6-bifosfatase; o citrato faz o contrário. Repare que os sinais escolhidos são leituras do estado energético e do estoque de matéria-prima da célula — não são intermediários dessas vias.])

A solução do fígado é regular as enzimas irreversíveis, e regulá-las *reciprocamente*: cada sinal que acelera um lado freia o outro. O ATP inibe a fosfofrutoquinase-1, porque muito ATP significa que não há por que produzir mais; o AMP a ativa, porque muito AMP significa exatamente o contrário. O citrato inibe a via glicolítica, e o motivo é bonito — citrato acumulado é sinal de que o ciclo de Krebs está abastecido e transbordando, de modo que enviar mais carbono para lá seria desperdício. Do outro lado, o acetil-CoA ativa a piruvato-carboxilase, sinalizando que há combustível de sobra e que o piruvato pode ser desviado para fabricar glicose em vez de ser queimado.

#clinica-box("Por que o etanol derruba a glicemia", [Um paciente que bebe muito e come pouco pode chegar hipoglicêmico, e a explicação não é apenas a falta de alimento. O mecanismo é bioquímico e direto.

A oxidação do etanol acontece no fígado em dois passos, e cada um deles reduz uma molécula de #sigla("NAD⁺", [nicotinamida adenina dinucleotídeo na forma oxidada — o aceptor de elétrons das desidrogenases]) a NADH. Beber muito, portanto, satura o hepatócito de NADH. Esse excesso empurra dois equilíbrios ao mesmo tempo: o piruvato é reduzido a lactato e o oxaloacetato é reduzido a malato. *Os dois metabólitos sequestrados são exatamente os substratos de que a gliconeogênese precisa* — o piruvato como ponto de partida e o oxaloacetato como intermediário obrigatório da primeira reação de contorno.

O resultado é uma gliconeogênese travada por falta de substrato, num paciente que já esgotou o glicogênio hepático por não comer. Sem as duas fontes, a glicemia cai. O mesmo excesso de NADH e de acetil-CoA empurra a produção de corpos cetônicos, o que explica a cetoacidose que costuma acompanhar o quadro.])

#subtopico("2.3 Frutose 2,6-bifosfato: o sinal que não é intermediário de nada")

O subtópico anterior deixou um ponto em aberto. A regulação por ATP, AMP e citrato informa à célula qual é o *seu próprio* estado energético — mas o fígado não trabalha para si, e sim para o organismo. Ele precisa de um sinal que traduza a informação hormonal, isto é, a notícia de que há glicose sobrando no sangue ou de que ela está faltando. Esse sinal é a frutose 2,6-bifosfato, e a primeira coisa a fixar sobre ela é o que ela não é.

#atencao-box("Frutose 2,6-bifosfato não é intermediário de via nenhuma", [Todos os outros metabólitos vistos até aqui pertencem a uma via: são consumidos por uma enzima e produzidos por outra, dentro de uma sequência. A frutose 2,6-bifosfato não. *Ela não é substrato nem produto da glicólise, da gliconeogênese ou de qualquer outra rota* — é fabricada e destruída por uma única enzima, e existe apenas para informar. Confundi-la com a frutose 1,6-bifosfato, que é intermediário genuíno da glicólise, é o erro que desmonta o subtópico inteiro: a diferença entre elas é a posição de um fosfato, e essa posição separa um metabólito de um recado.])

O efeito desse recado é duplo e recíproco, como convém a um sinal de escolha de direção: a frutose 2,6-bifosfato *ativa a fosfofrutoquinase-1*, acelerando a glicólise, e ao mesmo tempo *inibe a frutose-1,6-bifosfatase*, travando a gliconeogênese. Uma única molécula liga uma via e desliga a oposta, o que resolve de uma vez o problema do ciclo de substrato.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-16.png",
  largura: 60%,
  legenda: [O efeito da frutose 2,6-bifosfato sobre a fosfofrutoquinase-1. Sem ela (curva vermelha), a enzima tem comportamento sigmoide e trabalha devagar nas concentrações fisiológicas de frutose-6-fosfato. Com um micromolar dela (curva verde), a curva vira hiperbólica e a enzima satura logo. À direita, o mesmo sinal aparece com sinal invertido sobre a enzima da gliconeogênese.])

Falta a peça mais engenhosa: quem fabrica e quem destrói esse sinal. É a mesma proteína. A enzima chamada fosfofrutoquinase-2 é *bifuncional* — tem dois sítios ativos em domínios distintos da mesma cadeia. Um deles é uma quinase, que pega frutose-6-fosfato e a fosforila na posição 2, produzindo o sinal. O outro é uma fosfatase, que retira esse mesmo fosfato e destrói o sinal, devolvendo frutose-6-fosfato. Qual dos dois domínios está ativo depende do estado de fosforilação da própria enzima, e é aí que o hormônio entra.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-17.png",
  largura: 58%,
  legenda: [A enzima bifuncional em ação. À direita, os dois sentidos da mesma proteína: a atividade de quinase fabrica a frutose 2,6-bifosfato a partir da frutose-6-fosfato, e a atividade de fosfatase a desmonta. À esquerda, os dois alvos do sinal produzido, um em cada sentido da via.])

Vale seguir a cadeia inteira, porque o encadeamento é o conteúdo. O glucagon chega ao hepatócito, ativa a produção de #sigla("AMPc", [monofosfato de adenosina cíclico — segundo mensageiro produzido pela adenilato-ciclase em resposta a hormônios]) e, por meio dele, a #sigla("PKA", [proteína-quinase A — quinase dependente de AMPc, executora da maioria dos efeitos do glucagon e da adrenalina]). A PKA fosforila a enzima bifuncional. A enzima fosforilada perde a atividade de quinase e ganha a de fosfatase, de modo que a concentração de frutose 2,6-bifosfato despenca. Sem o ativador, a fosfofrutoquinase-1 desacelera; sem o inibidor, a frutose-1,6-bifosfatase se solta. *A glicólise hepática para e a gliconeogênese começa* — e repare que o glucagon nunca tocou em nenhuma das duas enzimas de controle. Ele agiu sobre o fabricante do sinal. A insulina faz o percurso inverso, ativando a fosfatase que remove esse fosfato e devolvendo a enzima bifuncional ao modo quinase.

Há um detalhe que fecha o raciocínio e mostra que o mecanismo não é uma regra cega. A enzima bifuncional existe em isoformas diferentes conforme o tecido, e a isoforma do músculo cardíaco responde à fosforilação *ao contrário*: fosforilada, ela ativa a atividade de quinase e aumenta a frutose 2,6-bifosfato. A consequência é que a adrenalina, que no fígado desliga a glicólise, no coração a acelera. Faz sentido do ponto de vista do organismo: o mesmo susto que manda o fígado despejar glicose no sangue manda o coração queimar mais depressa. *A molécula sinalizadora é a mesma, a quinase é a mesma, e o resultado é oposto porque o alvo é diferente* — que é, de novo, a tese de repertório desta aula.

#subtopico("2.4 Glicogênio hepático: a fosforilase que escuta a glicose")

Se a glicoquinase é o filtro de entrada, a glicogênio-fosforilase é a torneira de saída. Ela funciona como uma válvula com duas posições em equilíbrio: um estado tenso, de baixa atividade, e um estado relaxado, ativo. Não se trata de ligada ou desligada — trata-se de para que lado o equilíbrio está pendendo, e vários fatores empurram esse equilíbrio ao mesmo tempo.

O primeiro fator é a fosforilação. A enzima fosforilada é chamada fosforilase a e tende ao estado ativo; a não fosforilada, fosforilase b, tende ao inativo. Quem adiciona esse fosfato é uma quinase acionada pela cascata do glucagon, e no fígado é o glucagon que domina — a adrenalina participa, por receptores próprios e inclusive por uma via que passa pelo cálcio, mas o hormônio da glicemia baixa, ali, é o glucagon.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-19.png",
  largura: 52%,
  legenda: [A cascata que ativa a degradação de glicogênio. O glucagon age por um receptor próprio, a adrenalina por receptores adrenérgicos, e os dois caminhos convergem no AMPc e na proteína-quinase A, que fosforila a fosforilase-quinase. Repare no ramo do cálcio à direita: ele existe para que a contração muscular possa disparar a mesma via sem hormônio nenhum — assunto da PARTE III.])

O segundo fator é o que distingue o fígado de todo o resto, e é o ponto alto deste subtópico. *A fosforilase hepática é inibida pela glicose livre.* A glicose se encaixa num sítio da enzima e empurra o equilíbrio para o estado tenso, mesmo que a enzima esteja fosforilada. Ou seja: quando a glicemia sobe, a própria glicose que chega ao hepatócito desliga a degradação do glicogênio, sem precisar esperar por hormônio nenhum. A enzima é, ela mesma, o sensor.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-18.png",
  largura: 56%,
  legenda: [A fosforilase hepática nos dois estados. À esquerda, o estado tenso, de baixa atividade; à direita, o relaxado, ativo. A seta indica o efeito da glicose: ela empurra a enzima fosforilada de volta ao estado tenso. Note o fosfato marcado nas duas formas — a enzima continua fosforilada; o que mudou foi a conformação.])

O terceiro fator é a consequência elegante do segundo. Ao empurrar a fosforilase a para o estado tenso, a glicose expõe o fosfato dessa enzima à fosfoproteína-fosfatase 1, que o remove — convertendo a fosforilase a em b e encerrando de vez a degradação. A mesma fosfatase, agora livre, desfosforila também a glicogênio-sintase, e a sintase desfosforilada é a forma ativa. *Um único evento, a chegada de glicose, primeiro desliga a degradação e só depois liga a síntese, nessa ordem obrigatória* — o que evita o ciclo fútil de degradar e sintetizar glicogênio ao mesmo tempo. A insulina reforça essa mesma direção ativando a fosfatase, e é assim que ela promove o acúmulo de glicogênio.

#mini-resumo[Se você só lembrar de uma coisa: no fígado, quem informa à fosforilase que a glicemia subiu é a própria glicose, e a fosfatase que ela libera encerra a degradação antes de abrir a síntese.]

#subtopico("2.5 Aminoácidos: o nitrogênio que precisa virar ureia")

O fígado não recebe apenas glicose pela veia porta. Ele recebe também todo o aminoácido absorvido, e aqui entra a restrição já anunciada na PARTE I: não existe depósito de aminoácido. O que não for usado para sintetizar proteína ou seus derivados — bases nitrogenadas, hormônios, porfirinas — precisa ser desmontado, e desmontar um aminoácido significa separar duas partes com destinos completamente diferentes.

O esqueleto de carbono é a parte fácil. Ele entra no metabolismo intermediário como piruvato, acetil-CoA ou algum intermediário do ciclo de Krebs, e daí segue para a gliconeogênese ou para a síntese de gordura, conforme o estado do organismo. *O excesso de proteína da dieta é, em boa medida, armazenado como triacilglicerol* — porque essa é a única forma de estoque disponível para o carbono excedente.

O grupo amino é o problema. Removê-lo produz amônia, que é tóxica sobretudo para o sistema nervoso, e o fígado a converte imediatamente em ureia, uma molécula neutra, hidrossolúvel e excretável pelo rim. Essa conversão custa energia — quatro ligações de alta energia por molécula de ureia formada —, e é por isso que uma dieta hiperproteica cobra um preço metabólico mesmo quando o aminoácido é usado apenas como combustível.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-23.png",
  largura: 60%,
  legenda: [Os dois fluxos de aminoácido que chegam ao hepatócito. Pelo alto, os da dieta, destinados sobretudo à síntese de proteínas e derivados. Pela direita, os que vêm do músculo — e repare que eles não chegam como aminoácidos quaisquer, e sim como alanina, que o hepatócito converte em piruvato entregando o nitrogênio ao ciclo da ureia.])

Essa seta que vem do músculo merece nome e explicação, porque ela é um dos dois grandes circuitos entre tecidos desta aula. Quando o músculo degrada proteína própria para obter energia, ele precisa se livrar do nitrogênio — e não pode fabricar ureia, porque o ciclo da ureia é essencialmente hepático. A solução é transferir o grupo amino para o piruvato produzido na sua própria glicólise, formando alanina, e enviá-la pelo sangue ao fígado. Lá, a reação é revertida: a alanina devolve o nitrogênio, que segue para a ureia, e o esqueleto volta a ser piruvato, matéria-prima da gliconeogênese. A glicose fabricada retorna ao músculo. Esse é o #termo-nota[ciclo glicose-alanina][circuito que leva ao fígado, embalado em alanina, o nitrogênio e o carbono que o músculo precisa descartar], e ele resolve dois problemas com um transporte só: *tira o nitrogênio do músculo de forma atóxica e devolve o carbono ao fígado como substrato*.

Uma última precisão, porque ela reaparece o tempo todo. Nem todo aminoácido serve para fabricar glicose. Aqueles cujo esqueleto é degradado até acetil-CoA ou acetoacetato não contribuem, e a razão é a mesma que impede o ácido graxo de virar glicose: a reação que transforma piruvato em acetil-CoA libera gás carbônico e é irreversível. Uma vez que o carbono chegou a acetil-CoA, o caminho de volta à glicose está fechado.

#subtopico("2.6 Lipídios: o fígado que exporta gordura e empacota acetil-CoA")

O terceiro grande fluxo que atravessa o hepatócito é o dos lipídios, e o fígado é ao mesmo tempo fábrica, refinaria e distribuidora. Ele sintetiza ácido graxo e triacilglicerol quando há carbono sobrando, sintetiza colesterol e a partir dele os sais biliares, monta as lipoproteínas que carregam gordura pelo sangue e, na direção oposta, oxida ácido graxo para obter energia. Qual desses programas está ligado depende, mais uma vez, da razão entre insulina e glucagon.

Com insulina alta, o programa é de construção. O carbono que sobra da glicólise, na forma de acetil-CoA, é usado para montar ácidos graxos, que são esterificados a triacilglicerol. Parte fica no hepatócito, parte é embalada em lipoproteínas e exportada para os tecidos que vão usá-la ou guardá-la. Na mesma direção, a insulina estimula a síntese de colesterol, matéria-prima dos sais biliares que emulsificam a gordura da dieta, dos hormônios esteroides e das próprias membranas celulares.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-25.png",
  largura: 58%,
  legenda: [O metabolismo lipídico do hepatócito nos dois sentidos. Para cima, a beta-oxidação do ácido graxo entregando elétrons e acetil-CoA; para a direita, as três saídas — lipoproteína plasmática, ácido graxo livre e corpo cetônico. Repare que o acetil-CoA ocupa aqui a mesma posição de encruzilhada que a glicose-6-fosfato ocupava no metabolismo de carboidrato.])

Com glucagon alto, o programa se inverte. A beta-oxidação corta os ácidos graxos de dois em dois carbonos e o acetil-CoA resultante alimenta o ciclo de Krebs, fornecendo ATP para o próprio hepatócito — inclusive o ATP caro da gliconeogênese, o que é uma coincidência conveniente: *o fígado queima gordura para poder fabricar glicose*. Quando a produção de acetil-CoA supera a capacidade do ciclo de Krebs de consumi-lo, o excedente é condensado em #termo-nota[corpos cetônicos][acetoacetato e beta-hidroxibutirato, combustíveis hidrossolúveis fabricados no fígado para exportação], que saem do fígado pelo sangue.

Vale entender por que esse empacotamento existe, porque a lógica é bonita. O ácido graxo é insolúvel e precisa viajar ligado a proteínas plasmáticas; além disso, ele não atravessa a barreira hematoencefálica em quantidade útil. O corpo cetônico resolve as duas limitações: é pequeno, hidrossolúvel, viaja livre no plasma e chega ao cérebro. *Ele é, na prática, acetil-CoA em formato de entrega* — e o tecido que o recebe o reconverte a acetil-CoA e o joga no próprio ciclo de Krebs.

E há um detalhe que fecha o assunto e é frequentemente esquecido. O fígado é o único produtor de corpos cetônicos e não é consumidor deles. Falta ao hepatócito a transferase que reativa o acetoacetato a acetoacetil-CoA, passo obrigatório para queimá-lo. A ausência dessa enzima não é um defeito — *é a garantia de que o combustível fabricado sai inteiro para músculo, coração e cérebro*, em vez de ser consumido no próprio lugar onde foi produzido. Mais uma vez, a enzima que falta explica o comportamento do tecido.

Com o hepatócito destrinchado, o que resta é ver como cada um dos outros tecidos difere dele — e cada diferença, daqui em diante, vai se resumir a uma peça a mais ou a menos.

#parte-title("PARTE III — Os outros tecidos e o sensor que fecha o circuito")

#subtopico("3.1 Músculo esquelético: reserva própria, e o ciclo de Cori")

O músculo esquelético existe para converter energia química em trabalho mecânico, e faz isso consumindo ATP em quantidade que nenhum outro tecido consome em picos. Toda a organização metabólica dele decorre dessa demanda: ele guarda a maior massa de glicogênio do corpo, guarda esse glicogênio para si, e dispõe de fontes de ATP escalonadas por velocidade.

A mais rápida é a #termo-nota[fosfocreatina][reservatório muscular de fosfato de alta energia, capaz de recarregar o ATP em uma única reação], que transfere seu fosfato diretamente ao #sigla("ADP", [adenosina difosfato — o que sobra do ATP depois que ele cede um fosfato; recarregá-lo é o que toda via energética faz]) numa reação de um passo só, sem via metabólica nenhuma no meio. É instantânea — e por isso mesmo é a primeira a ser usada. Também é a primeira a acabar: o estoque é pequeno e se esgota em poucos segundos de esforço máximo. Em seguida entra o glicogênio próprio, degradado a glicose-6-fosfato e queimado na glicólise, com ou sem oxigênio conforme o tipo de fibra. Por último, e sustentando o esforço prolongado, entram o ácido graxo trazido pelo sangue e, quando disponíveis, os corpos cetônicos fabricados pelo fígado.

A distinção entre os tipos de fibra segue exatamente essa lógica. As *fibras vermelhas* são ricas em mitocôndrias e sustentam fosforilação oxidativa — trabalham por muito tempo, em ritmo moderado, oxidando completamente o combustível. As *fibras brancas* têm mais glicogênio e menos mitocôndria, e produzem ATP por glicólise com formação de lactato: pouco rendimento por glicose, mas velocidade de produção muito maior. Não é que uma seja melhor; são soluções para regimes de esforço diferentes.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-29.png",
  largura: 64%,
  legenda: [O músculo esquelético e o circuito que ele mantém com o fígado. À direita, o ciclo de Cori: o lactato produzido na contração viaja pelo sangue, o fígado o reconverte em glicose gastando ATP, e a glicose volta ao músculo. Embaixo, a reação da fosfocreatina — repare que ela ocorre nos dois sentidos, carregando durante a recuperação e descarregando durante o esforço.])

O lactato produzido pela fibra branca não fica parado. Ele sai da célula, entra na circulação e é captado pelo fígado, que o reconverte a piruvato e, pela gliconeogênese, a glicose — devolvida ao sangue e disponível de novo para o músculo. Esse é o #termo-nota[ciclo de Cori][circuito lactato-glicose que liga o músculo em esforço ao fígado], e a conta que ele embute merece ser feita com cuidado, porque o resultado costuma surpreender.

Primeira etapa: contar o que o músculo ganhou. Ao quebrar uma glicose até dois lactatos, a fibra obteve dois ATP — o saldo da glicólise anaeróbia. Segunda etapa: contar o que o fígado gastou para desfazer isso. Refazer uma glicose a partir de dois lactatos passa pela gliconeogênese completa, ao custo já calculado de seis ligações de alta energia. Terceira etapa: fechar o balanço do organismo. Foram seis gastas contra duas obtidas, *saldo líquido de quatro ligações de alta energia perdidas a cada volta do circuito*.

Lido em palavras: o ciclo de Cori é deficitário para o corpo como um todo. Ele não existe para produzir energia, e sim para deslocar o problema — permite que a fibra muscular continue produzindo ATP em ritmo alto sem depender de oxigênio, transferindo ao fígado, que está bem oxigenado e não está correndo, a conta de reconstruir a glicose. É uma divisão de trabalho entre um tecido que precisa de velocidade e outro que tem capacidade oxidativa sobrando.

#confusao-prevista(
  titulo: "O ciclo de Cori não gera energia — ele transfere custo",
  aluno_acha: [aluno lê "o lactato vira glicose de novo" como reciclagem eficiente, e conclui que o circuito recupera a energia do esforço],
  mecanismo: [cada volta consome quatro ligações de alta energia a mais do que produziu. O que o ciclo entrega não é energia, é *localização*: ele tira do músculo a obrigação de oxidar completamente o combustível no momento do esforço, e passa essa obrigação ao fígado, que a cumpre depois, com oxigênio. Pela mesma razão, o consumo de oxigênio permanece elevado por um tempo após o exercício — o fígado ainda está pagando a conta.],
)

#subtopico("3.2 A fosforilase muscular escuta outra coisa")

A enzima que degrada glicogênio no músculo é a mesma família da hepática e obedece ao mesmo esquema de dois estados, tenso e relaxado. O que muda é *quem tem permissão de empurrar esse equilíbrio*, e a diferença é inteiramente coerente com a função de cada tecido.

No fígado, o sinal era a glicose livre, porque o fígado trabalha para a glicemia do organismo. No músculo, a glicose livre praticamente não oscila dentro da fibra e não informaria nada útil. O que oscila ali, e muito, é a carga energética: durante a contração, o ATP cai e o AMP sobe. É a isso que a fosforilase muscular responde. *O AMP a empurra para o estado ativo e o ATP para o inativo*, competindo pelo mesmo sítio de ligação de nucleotídeo, de modo que a razão entre os dois é lida diretamente pela enzima. A glicose-6-fosfato acompanha o ATP, favorecendo o estado inativo — o que é coerente: se ela está acumulada, a glicólise está represada e não há por que liberar mais.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-32.png",
  largura: 58%,
  legenda: [A fosforilase muscular e seus dois sensores. À esquerda, a via hormonal: a epinefrina leva à fosforilação e à forma ativa. À direita, a via metabólica: o AMP que sobe durante o exercício ativa a enzima mesmo sem fosforilação. Repare que os dois caminhos chegam ao mesmo estado relaxado por rotas independentes.])

Há ainda um terceiro caminho, e ele é o mais elegante dos três. A enzima que fosforila a fosforilase possui uma subunidade que é a própria calmodulina, sensível a cálcio. Quando o potencial de ação chega à fibra e o retículo sarcoplasmático libera cálcio para desencadear a contração, *esse mesmo cálcio ativa parcialmente a fosforilase-quinase*. Contração e mobilização de glicogênio ficam acopladas no mesmo sinal, sem necessidade de hormônio. O músculo não espera a adrenalina chegar para começar a queimar o próprio estoque — ele começa no instante em que se contrai, e a adrenalina apenas amplifica uma resposta já em curso.

Do lado da síntese, a lógica se completa. A glicogênio-sintase muscular também é regulada por fosforilação, mas é ativada alostericamente pela glicose-6-fosfato. O encadeamento vale ser seguido: quando o ATP está alto, ele inibe a fosfofrutoquinase-1, a via glicolítica se represa, a frutose-6-fosfato e a glicose-6-fosfato se acumulam, e esse acúmulo ativa a sintase. *A fibra em repouso, com ATP sobrando, converte automaticamente o excesso de substrato em glicogênio* — sem hormônio nenhum, apenas por acúmulo de intermediário. A insulina reforça a mesma direção, ativando a fosfatase que desfosforila a sintase.

#figura-lateral("/figuras/biomol-04-integracao-metabolica-i/slide-33.png",
  lado: "right",
  largura-figura: 38%,
  texto: [O ponto que costuma escapar é a direção da causa. Não é a glicose que ativa a sintase muscular, e sim a glicose-6-fosfato — ou seja, o sinal chega já do lado de dentro da catraca, depois da hexoquinase. Isso é consistente com um tecido que não exporta glicose e portanto só precisa saber quanto substrato já capturou, não quanto existe circulando lá fora.],
  legenda: [A fosfofrutoquinase-1 inibida represa a via e o acúmulo de glicose-6-fosfato ativa a glicogênio-sintase.])

#clinica-box("Quando a fosforilase muscular falta", [Há uma doença hereditária em que a isoforma muscular da glicogênio-fosforilase não funciona, e o quadro é um teste direto de tudo o que este subtópico afirmou. O paciente é uma pessoa jovem que apresenta dor muscular intensa, cãibras e fraqueza logo no início de um esforço vigoroso, e que melhora se diminuir o ritmo e persistir.

O mecanismo encadeia-se assim. Sem a fosforilase, o glicogênio muscular está lá, e em quantidade até aumentada, mas não pode ser mobilizado. No começo do exercício intenso, quando a demanda de ATP dispara e o suprimento de ácido graxo pelo sangue ainda não subiu, a fibra depende exatamente do glicogênio que não consegue acessar — e entra em déficit energético, com contratura e lesão da própria célula. *Um achado laboratorial confirma o raciocínio de forma limpa: o lactato sanguíneo, que deveria subir durante o esforço isquêmico, não sobe*, porque não há glicose-6-fosfato entrando na glicólise. Passados alguns minutos, a mobilização de ácido graxo do tecido adiposo e a captação de glicose do sangue assumem, e o paciente consegue retomar o exercício com mais conforto.])

#subtopico("3.3 Coração: o consumidor aeróbio obrigatório")

O músculo cardíaco resolve um problema diferente do esquelético: ele não trabalha em picos, trabalha sem parar. Essa continuidade define todo o resto. O miocárdio é densamente povoado de mitocôndrias, tem metabolismo primariamente aeróbio e obtém a maior parte do ATP oxidando ácidos graxos, complementados por corpos cetônicos, por lactato captado da circulação e por alguma glicose.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-30.png",
  largura: 50%,
  legenda: [Miocárdio em microscopia eletrônica. As fileiras de mitocôndrias alinhadas entre as miofibrilas ocupam uma fração do volume celular que nenhum outro músculo alcança — é essa densidade que sustenta um metabolismo aeróbio contínuo, e é ela que torna o tecido dependente de fluxo de oxigênio ininterrupto.])

Duas consequências merecem destaque. A primeira é que o coração *praticamente não tem reserva*: o glicogênio é pouco, o lipídio estocado é pouco, e o depósito de fosfocreatina é modesto. Ele é um tecido de fluxo, que depende da entrega contínua de combustível e de oxigênio pelo sangue coronariano. Quando esse fluxo é interrompido, o ATP cai em minutos, e é por isso que a isquemia miocárdica produz lesão tão rapidamente — não há tampão metabólico local.

A segunda é que o coração é um bom cliente para o que os outros tecidos descartam. O lactato despejado pelo músculo esquelético em exercício é captado pelo miocárdio, reconvertido a piruvato e oxidado no ciclo de Krebs; os corpos cetônicos fabricados pelo fígado em jejum também são bem-vindos. *Ele é o consumidor final de vários resíduos aparentes do sistema*, o que reforça a ideia de que "resíduo metabólico" quase sempre significa apenas "combustível para outro tecido".

#subtopico("3.4 Tecido adiposo: o banco de triacilglicerol e o gerador de calor")

O tecido adiposo funciona como um banco, e a comparação se paga em mecanismo. Ele recebe depósitos quando há excedente, guarda em formato compacto, e libera quando há saque — só que, ao contrário de um banco, ele não devolve exatamente aquilo que recebeu. Distribuído por todo o corpo e correspondendo a cerca de quinze por cento da massa de um adulto, com até noventa por cento do adipócito ocupado por triacilglicerol, ele é um tecido muito mais ativo do que a aparência inerte sugere.

Do lado do depósito, a insulina comanda. Ela aumenta a captação de glicose pelo adipócito e estimula a glicólise, e o carbono que sobra dessa glicólise se acumula como citrato quando o ATP está alto. Esse citrato é ao mesmo tempo sinal e matéria-prima: sinaliza abundância e fornece o carbono para a síntese de ácido graxo. A maior parte da gordura estocada, porém, não é fabricada ali — chega pronta, seja a sintetizada pelo fígado e exportada em lipoproteína, seja a absorvida da dieta.

Do lado do saque, o sinal é o oposto. Glucagon e adrenalina chegam por receptores distintos, convergem no mesmo AMPc e na mesma proteína-quinase A, e essa quinase fosforila a #termo-nota[lipase hormônio-sensível][enzima do adipócito que hidrolisa o triacilglicerol estocado, ativada por fosforilação], além das proteínas que revestem a gotícula lipídica e impedem o acesso da enzima. O triacilglicerol é hidrolisado, e os ácidos graxos saem para a circulação ligados à albumina, disponíveis para músculo, coração e fígado.

Sobra o glicerol, e aqui há uma sutileza que fecha o circuito com a PARTE II. *O adipócito não possui glicerol-quinase*, de modo que não consegue reaproveitar o próprio glicerol para refazer triacilglicerol. Ele precisa obter glicerol-3-fosfato da glicólise — isto é, precisa de glicose — ou fabricá-lo a partir de piruvato por uma via curta chamada #termo-nota[gliceroneogênese][via abreviada que refaz glicerol-3-fosfato a partir de piruvato dentro do adipócito]. Duas consequências decorrem disso: a re-esterificação dos ácidos graxos depende de glicose e insulina, e o glicerol liberado na lipólise viaja para o fígado, onde é um substrato gliconeogênico barato — bem mais barato que o piruvato, porque entra na via já fosforilado, depois do trecho mais caro.

Uma variante do tecido merece nota. O tecido adiposo marrom é rico em mitocôndrias e expressa uma proteína desacopladora que abre, na membrana mitocondrial interna, um caminho de retorno para o próton. O gradiente construído pela cadeia respiratória se dissipa por esse atalho sem passar pela ATP-sintase, e a energia sai como calor. *É oxidação sem produção de ATP, e o produto útil é a temperatura* — a #termo-nota[termogênese sem tremor][produção de calor por dissipação do gradiente de prótons, sem contração muscular], especialmente importante no recém-nascido.

#subtopico("3.5 Cérebro, hemácia e rim: os clientes obrigatórios da glicose")

Depois de percorrer os tecidos que guardam e mobilizam, faltam os que apenas consomem — e são justamente eles que explicam por que toda a maquinaria anterior existe. O cérebro pesa cerca de dois por cento do corpo e consome, em repouso, perto de um quinto de todo o oxigênio utilizado pelo organismo. Esse consumo não sustenta contração nem síntese em larga escala: sustenta sobretudo as bombas iônicas que restabelecem os gradientes de sódio e potássio depois de cada potencial de ação.

O ponto crítico é a restrição de combustível. *O neurônio utiliza glicose e, depois de dias de jejum, corpos cetônicos — e nada além disso.* Ácido graxo de cadeia longa não atravessa a barreira hematoencefálica em quantidade útil e não é oxidado pelo neurônio em escala relevante; a glia tem alguma capacidade de usá-lo, o neurônio não. Como o encéfalo praticamente não estoca glicogênio, ele depende, minuto a minuto, da concentração de glicose no sangue — e é exatamente essa dependência que dá sentido a todo o aparato hepático da PARTE II. Vale registrar que nem no jejum prolongado a substituição é completa: os corpos cetônicos passam a cobrir a maior parte da demanda, mas uma fração de glicose continua obrigatória.

#figura-nebli("/figuras/biomol-04-integracao-metabolica-i/slide-38.png",
  largura: 54%,
  legenda: [Consumo cerebral de glicose visto por tomografia com glicose marcada. Em cima, o encéfalo em repouso; embaixo, o de uma pessoa privada de sono por quarenta e oito horas, com consumo global menor. A imagem torna visível o que o texto afirma: a captação de glicose acompanha a atividade elétrica, região por região.])

A hemácia depende de glicose por um motivo diferente, e a comparação entre os dois casos é instrutiva. Ela não tem mitocôndria alguma — perdeu-a na maturação, junto com o núcleo, para abrir espaço para hemoglobina. Sem mitocôndria, não há ciclo de Krebs nem fosforilação oxidativa, e todo o ATP vem da glicólise anaeróbia, com rendimento de dois ATP por glicose e produção obrigatória de lactato. *O neurônio depende de glicose por falta de acesso a outro combustível; a hemácia depende por falta da maquinaria que queimaria esse outro combustível* — e o lactato que ela despeja continuamente no sangue alimenta o ciclo de Cori mesmo em repouso.

O rim, por fim, acumula dois papéis. Ele excreta a ureia fabricada pelo fígado, e também expressa glicose-6-fosfatase, o que faz dele o segundo órgão gliconeogênico do corpo — em volume bem menor que o fígado, mas com peso crescente conforme o jejum se prolonga, usando principalmente glutamina como substrato. Ao consumir glutamina, ele libera amônia na urina, o que acopla o descarte de nitrogênio ao controle do equilíbrio ácido-base.

#table(
  columns: (auto, 1fr, auto, 1fr),
  inset: 7pt,
  align: (left, left, center, left),
  stroke: 0.5pt + gray-border,
  table.header(
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Tecido]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Combustível preferido]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Exporta glicose]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Peça que define o comportamento]],
  ),
  [Fígado], [ácido graxo em jejum; glicose após a refeição], [sim], [tem glicose-6-fosfatase e glicoquinase; não tem a transferase de corpos cetônicos],
  [Músculo esquelético], [glicogênio próprio, depois ácido graxo], [não], [não tem glicose-6-fosfatase; fosforilase lê AMP e ATP],
  [Coração], [ácido graxo, corpos cetônicos e lactato], [não], [densidade mitocondrial alta e reserva local mínima],
  [Tecido adiposo], [glicose para re-esterificar], [não], [não tem glicerol-quinase; tem lipase hormônio-sensível],
  [Cérebro], [glicose; corpos cetônicos no jejum longo], [não], [barreira que barra ácido graxo; sem reserva],
  [Hemácia], [glicose, obrigatoriamente anaeróbia], [não], [sem mitocôndria],
  [Córtex renal], [ácido graxo e glutamina], [sim], [tem glicose-6-fosfatase],
)

#subtopico("3.6 Pâncreas: o sensor que usa as mesmas peças do fígado")

Todo o circuito descrito até aqui depende de alguém medir a glicemia e traduzir essa medida em hormônio. Esse alguém é a porção endócrina do pâncreas, e o mecanismo que ela usa é uma reaplicação exata do par que abriu a PARTE II — o que é a melhor confirmação possível de que aquele par é mesmo um sensor.

As ilhotas contêm dois tipos celulares que interessam aqui. As células alfa secretam glucagon em resposta à queda da glicemia, ao aumento de aminoácidos circulantes e à adrenalina. As células beta secretam insulina em resposta à elevação da glicemia. A resposta a aminoácido merece um comentário: uma refeição rica em proteína e pobre em carboidrato eleva a insulina, o que sozinho derrubaria a glicemia; a secreção simultânea de glucagon impede exatamente isso.

O ponto fino é como a célula beta enxerga a glicose. *Não existe receptor de glicose na membrana dela.* O que existe é o GLUT-2, de baixa afinidade, e a glicoquinase, também de baixa afinidade — os mesmos do hepatócito. A glicose entra proporcionalmente à concentração no sangue, é fosforilada em proporção a essa entrada, e segue pela glicólise e pelo ciclo de Krebs. A produção de ATP sobe, a razão entre ATP e ADP sobe com ela, e essa razão fecha um canal de potássio da membrana. Fechado o canal, a célula despolariza; a despolarização abre canais de cálcio; o cálcio que entra dispara a exocitose dos grânulos de insulina.

Vale reler a cadeia pelo que ela tem de econômico: a célula beta não mede glicose, *ela metaboliza glicose e mede o próprio ATP*. E como a etapa limitante desse metabolismo é a glicoquinase, é ela quem determina em que glicemia a secreção começa a subir — ou seja, a glicoquinase é o ponto de ajuste do sistema inteiro, no pâncreas exatamente como no fígado. Isso explica, retroativamente, por que uma mutação nessa enzima desloca para cima a glicemia mantida pelo organismo, sem desorganizar o controle.

#conclusao-box[
Um princípio percorreu as três PARTES: *a especialização metabólica se decide por repertório, não por intensidade*. O fígado, o músculo, o adipócito e o neurônio não fazem as mesmas coisas em graus diferentes — eles dispõem de conjuntos diferentes de enzimas e transportadores, e cada peça ausente fecha uma via inteira. Foi assim que a aula avançou: a falta da glicose-6-fosfatase define o músculo, a falta da glicerol-quinase define o adipócito, a falta da transferase de corpos cetônicos define o fígado como produtor que não consome, a falta de mitocôndria define a hemácia.

No centro do mecanismo está uma molécula e um limiar. A glicose-6-fosfato é a encruzilhada onde todo o carbono glicídico passa, e a fosforilação que a produz é a catraca que prende a glicose dentro da célula. Quem tem a fosfatase que desfaz essa catraca exporta glicose e serve ao organismo; quem não tem, consome o que captou e serve a si mesmo. O limiar, por sua vez, é dado pelo par de baixa afinidade — GLUT-2 e glicoquinase —, que faz fígado e célula beta só reagirem quando há glicose sobrando, deixando a glicose escassa para o cérebro. Sobre essa base, três camadas de controle atuam em velocidades encaixadas: alostérica em instantes, covalente em minutos por meio dos hormônios, e mudança de quantidade de enzima em horas.

A clínica retomada confirma o desenho a cada falha. Sem a glicose-6-fosfatase, o fígado acumula glicogênio e ainda assim não sustenta a glicemia, com acidose láctica e hipertrigliceridemia por transbordamento do carbono represado. Sem a fosforilase muscular, o glicogênio da fibra existe mas é inacessível, e o lactato não sobe no esforço. Com a glicoquinase enfraquecida, todo o sistema continua funcionando, apenas regulado alguns miligramas por decilitro acima do normal. E com o hepatócito saturado de NADH pelo etanol, a gliconeogênese trava por falta dos dois substratos que foram desviados.

O que fica para o próximo passo é o mesmo elenco, agora em movimento no tempo. Aqui os tecidos foram apresentados por sua especialização permanente; falta ver como eles se revezam ao longo das horas — quem trabalha logo após a refeição, quem assume nas primeiras horas de jejum, quem entra em cena quando o jejum se prolonga por dias e o cérebro precisa aprender a viver de corpos cetônicos. As peças já estão todas na mesa; o que muda, dali em diante, é a razão entre insulina e glucagon.
]
