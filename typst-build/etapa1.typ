#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Uma célula do fígado não tem como saber que você almoçou. Ela não vê o prato, não sente o cheiro, não conversa com o intestino. E, no entanto, minutos depois da refeição, ela para de despejar glicose no sangue e começa a estocar. O que atravessou essa distância foi um hormônio — uma molécula em concentração ínfima que carrega uma ordem e encontra, na superfície ou no interior da célula certa, uma proteína feita sob medida para reconhecê-la. Este resumo persegue o caminho dessa ordem, do lado de fora da célula até a enzima que muda de comportamento. Primeiro, o mecanismo geral: o que é um hormônio, por que a solubilidade dele decide onde fica seu receptor, e como um punhado de moléculas consegue mobilizar gramas de combustível. Depois, o par insulina e glucagon trabalhado até o fim, porque é nele que a regulação metabólica fica visível em detalhe — inclusive no metabolismo do glicogênio, que a aula usa como bancada de demonstração. Por fim, catecolaminas, hormônios tireoidianos e esteroides, três classes que respondem em velocidades diferentes e explicam por que o corpo precisa de mais de um tipo de mensageiro. A pergunta que costura tudo é sempre a mesma: como um sinal químico vira uma mudança de metabolismo.
]

#parte-title("PARTE I — Do sinal ao segundo mensageiro", primeira: true)

#subtopico("1.1 — Regular o metabolismo é mexer na velocidade das reações")

Regular o metabolismo significa uma coisa bem concreta: interferir na velocidade das reações químicas que acontecem no organismo, acelerando umas e freando outras. Não existe uma reação sendo "ligada" ou "desligada" no sentido absoluto — o que existe é uma reação que passa a ocorrer mais rápido ou mais devagar, e como as vias metabólicas estão encadeadas, mexer na velocidade de um passo propaga efeito por toda a rede. A célula tem três maneiras de fazer isso, e vale conhecê-las de saída porque os hormônios usam as três.

A primeira é a *modulação da atividade enzimática*: uma molécula pequena se encaixa na enzima e muda o desempenho dela sem alterar a estrutura covalente. Enzimas que respondem assim costumam ter curva de velocidade em S, e não a hipérbole clássica de Michaelis-Menten — a resposta é abrupta dentro de uma faixa estreita de concentração de substrato, o que faz delas bons interruptores. A segunda é a #termo-nota[modificação covalente][ligação química de um grupo — na regulação metabólica, quase sempre um fosfato — ao esqueleto da proteína, mudando seu comportamento até que outra enzima o remova], em que uma enzima pendura um grupo fosfato na outra. Vale fixar o pré-requisito: fosforilar é pendurar um grupo fosfato numa proteína, e o volume e a carga negativa desse grupo mudam o formato dela — o formato define se ela trabalha ou não. Quem pendura é uma quinase, usando #sigla("ATP", [adenosina trifosfato — moeda energética da célula e doadora do fosfato usado pelas quinases]) como frasco de fosfato; quem retira é uma fosfatase, devolvendo o fosfato à água. A terceira é a *expressão gênica*: a célula fabrica mais cópias — ou menos — daquela enzima.

As três se distinguem sobretudo pelo tempo. Modular alostericamente uma enzima que já existe leva o tempo de uma colisão molecular. Fosforilar uma cascata inteira leva segundos. Fabricar proteína nova leva horas. Guardar essa escala explica praticamente todas as diferenças entre as classes de hormônio que vêm adiante.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-03.png",
  largura: 74%,
  legenda: [As três alavancas da regulação metabólica lado a lado. À esquerda, a curva sigmoide da enzima alostérica contrastada com a hipérbole de Michaelis-Menten — é a forma em S que permite ligar e desligar dentro de uma faixa estreita. No meio, o ciclo quinase/fosfatase que pendura e retira o fosfato. À direita, a via que termina alterando a quantidade de proteína.])

#subtopico("1.2 — Hormônio é ordem escrita em concentração baixíssima")

O que qualifica uma molécula como #termo-nota[hormônio][biomolécula produzida numa parte do corpo que regula a função de células distantes, agindo em concentrações muito baixas por meio de receptores específicos] não é sua estrutura química — hormônios são feitos de aminoácidos, de colesterol e de ácidos graxos, coisas bem diferentes entre si. O que qualifica é o modo de operar. Ele é produzido numa parte do corpo e regula funções a distância, age em quantidades muito pequenas, e só produz efeito onde existe um receptor capaz de reconhecê-lo. Organismos multicelulares dependem disso: sem um sistema de mensagens químicas, cada célula responderia apenas ao que acontece no seu próprio microambiente, e não haveria resposta coordenada a comer, correr ou passar fome.

A palavra "distância" merece um cuidado, porque ela varia. Quando a molécula cai na corrente sanguínea e vai agir num órgão distante, a sinalização é *endócrina* — é o caso da insulina, que sai do pâncreas e trabalha no fígado, no músculo e no tecido adiposo. Quando ela apenas se difunde para as células vizinhas, sem entrar na circulação, a sinalização é *parácrina*. E quando a célula secreta uma molécula que age sobre ela mesma, é *autócrina*. O mecanismo intracelular é o mesmo nos três casos; muda o alcance. Vale notar de passagem que a fronteira entre hormônio e neurotransmissor é mais tênue do que parece: a adrenalina é hormônio quando a medula adrenal a lança no sangue e neurotransmissor quando um neurônio a libera numa fenda sináptica. É a mesma molécula, com o mesmo tipo de receptor — o que muda é a rota de entrega.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-10.png",
  largura: 48%,
  legenda: [O alcance da mensagem define o nome: endócrina viaja pelo sangue até um órgão distante, parácrina difunde para o vizinho, autócrina volta para a própria célula que a produziu.])

#subtopico("1.3 — Sete pontos onde a mensagem pode ser regulada")

Pensar no hormônio apenas como "a molécula que age" esconde metade da regulação, porque a via completa tem sete etapas, e cada uma delas é um ponto de controle possível. A molécula precisa ser *sintetizada*; costuma ser *estocada* em grânulos até a hora de sair; é *secretada* mediante um estímulo; *transporta-se* pelo sangue, muitas vezes ligada a uma proteína carreadora que a protege e a mantém em reserva; é *reconhecida* por um receptor na célula-alvo; desencadeia a *resposta* intracelular; e é finalmente *degradada*, o que determina por quanto tempo o sinal dura.

Essa lista não é enfeite taxonômico — é o mapa de onde as coisas dão errado e de onde os medicamentos agem. Uma tireoide que não consegue fabricar o hormônio falha na biossíntese. Um tecido que fabrica e libera normalmente, mas cujas células-alvo respondem mal, falha no reconhecimento, e é exatamente esse o problema central da resistência à insulina. Um remédio que força a célula beta a esvaziar seus grânulos age na secreção. Um hormônio que circula quase todo preso a proteína carreadora tem meia-vida longa e efeito prolongado, porque só a fração livre é ativa e ela vai sendo reposta aos poucos pela fração ligada. Mais adiante, quando aparecerem sulfonilureia, insulinoma e as doenças da adrenal, vale voltar a esta lista e perguntar em qual dos sete pontos cada uma delas se instala.

#subtopico("1.4 — A solubilidade decide o endereço do receptor")

Um hormônio é uma carta, e a membrana plasmática é um muro de gordura. Cartas que se dissolvem em água não atravessam o muro e precisam entregar o recado na portaria; cartas que se dissolvem em gordura passam pelo muro e entregam em mãos, lá dentro. Essa é, literalmente, a regra que organiza todas as classes de hormônio, e ela decide não só onde fica o receptor mas também quanto tempo a resposta demora.

Do lado hidrossolúvel estão os hormônios peptídicos e proteicos — insulina, glucagon — e as catecolaminas, como a adrenalina. Eles não entram na célula. Ligam-se a receptores na face externa da membrana e precisam que o recado seja retransmitido por dentro, tarefa dos *segundos mensageiros*. Como o alvo final é uma enzima que já existe e só precisa mudar de estado, a resposta é rápida: segundos a minutos. Do lado lipossolúvel estão os hormônios esteroides, derivados do colesterol, como o cortisol. Eles atravessam a membrana, encontram o receptor dentro da célula e o complexo hormônio-receptor age no núcleo, alterando a transcrição de genes específicos. Como o efeito só aparece quando a proteína nova estiver pronta, a resposta demora horas. Os #termo-nota[eicosanoides][mensageiros derivados de ácidos graxos de vinte carbonos, como as prostaglandinas; agem sobretudo de forma parácrina, perto de onde são produzidos] completam o quadro pelo lado lipídico, com atuação predominantemente local.

Os hormônios tireoidianos são a exceção que testa se a regra foi entendida. Eles nascem de tirosina, um aminoácido, e por essa origem seria natural agrupá-los com as catecolaminas. Mas o que decide não é a origem e sim o comportamento físico da molécula pronta: iodada e apolar, ela atravessa a membrana e vai ao núcleo, como um esteroide. Origem em aminoácido, mecanismo de esteroide.

#confusao-prevista(
  titulo: "Rápido e lento não é o mesmo que hidrossolúvel e lipossolúvel — é consequência",
  aluno_acha: [o aluno decora "peptídico é rápido, esteroide é lento" como se fosse propriedade da molécula, e então trava quando aparece o hormônio tireoidiano, que é derivado de aminoácido mas age devagar],
  mecanismo: [a velocidade vem do *tipo de alvo*, não da classe química. Mexer numa enzima que já está pronta — fosforilar, desfosforilar — é rápido porque a maquinaria toda já existe. Fabricar proteína nova exige transcrever o gene, traduzir o mensageiro e dobrar a proteína, e isso não acontece em segundos. Por isso qualquer hormônio que trabalhe por receptor nuclear é lento, venha ele do colesterol ou da tirosina.],
)

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-14.png",
  largura: 80%,
  legenda: [Os quatro tipos de receptor em paralelo, com a escala de tempo na base — e ela conta a história inteira. Canal iônico controlado por ligante responde em milissegundos; receptor acoplado à proteína G, em segundos; receptor ligado a quinase e receptor nuclear, em horas, porque ambos terminam em transcrição e síntese de proteína.])

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-15.png",
  largura: 62%,
  legenda: [Os dois grandes mecanismos, lado a lado. À esquerda, o hormônio peptídico ou amina fica fora, gera segundo mensageiro e altera a *atividade de enzima preexistente*. À direita, o esteroide ou tireoidiano entra, e o complexo hormônio-receptor altera a *quantidade de proteína recém-sintetizada*.])

#subtopico("1.5 — A cascata do AMPc, degrau por degrau")

Todos os hormônios agem por receptores de alta afinidade, e a expressão merece ser levada a sério: afinidade alta significa que o receptor consegue capturar seu hormônio mesmo quando ele está presente em concentração nanomolar ou menor. Isso resolve o problema da detecção, mas cria outro. Se há tão pouca molécula de sinal, como esse punhado de eventos consegue mobilizar gramas de glicogênio.

A resposta é a amplificação em cascata, e ela vale a pena ser reconstruída passo a passo. O hormônio hidrossolúvel se liga ao receptor pela face externa. O receptor, agora com formato alterado, ativa do lado de dentro uma proteína G — um interruptor que fica ligado enquanto segura #sigla("GTP", [guanosina trifosfato — nucleotídeo que mantém a proteína G no estado ativo até ser hidrolisado]) e se desliga sozinho quando corta esse GTP em #sigla("GDP", [guanosina difosfato — forma inativa que a proteína G assume após hidrolisar o GTP]). A proteína G ativa, por sua vez, ativa a *adenilato ciclase*, uma enzima de membrana que pega ATP e o fecha num anel, produzindo #sigla("AMPc", [adenosina monofosfato cíclico — o segundo mensageiro que transmite, dentro da célula, a ordem que o hormônio deixou do lado de fora]). Esse AMPc é o segundo mensageiro: ele se difunde pelo citoplasma e ativa a #sigla("PKA", [proteína quinase A — enzima ativada pelo AMPc que fosforila proteínas-alvo, transmitindo adiante a ordem hormonal]). E a PKA fosforila as proteínas-alvo, que executam o efeito.

O que faz a conta explodir é que cada degrau é catalítico. Um receptor ocupado não ativa uma proteína G — ativa várias, uma depois da outra, enquanto o hormônio estiver ligado. Uma adenilato ciclase ativa não produz um AMPc, produz muitos. Uma PKA ativa não fosforila um alvo, fosforila muitos. Como cada nível multiplica o anterior em vez de somar, o efeito final é o produto de quatro fatores de amplificação. É por isso que uma concentração nanomolar de adrenalina consegue liberar uma quantidade macroscópica de glicose.

#mini-resumo[Em uma frase: o hormônio hidrossolúvel nunca entra na célula — ele ocupa o receptor, o receptor liga a proteína G, a proteína G liga a adenilato ciclase, a ciclase fabrica AMPc, e o AMPc ativa a PKA, que fosforila o alvo. Cada degrau é catalítico, e a multiplicação dos quatro é o que transforma poucas moléculas de sinal em muito efeito.]

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-16.png",
  largura: 58%,
  legenda: [A pirâmide da amplificação. Cada faixa é um degrau da cascata, e a largura crescente representa o número de moléculas envolvidas: poucos receptores ocupados no topo, um exército de moléculas efetoras na base.])

#parte-title("PARTE II — Insulina e glucagon: o interruptor recíproco do metabolismo")

#subtopico("2.1 — A insulina nasce grande e é cortada até ficar pronta")

A cascata da PARTE I fica abstrata enquanto não tiver um hormônio de carne e osso percorrendo-a, e o candidato natural é a insulina — um hormônio peptídico, hidrossolúvel, que trabalha exatamente pelo modelo de receptor de superfície. Antes de acompanhar seu efeito, vale ver como ela é fabricada, porque o processamento explica um detalhe clínico de peso.

Hormônios peptídicos e proteicos sofrem processamento pós-traducional: o gene não codifica a molécula final, e sim um precursor maior que vai sendo aparado. No caso da insulina, o produto inicial é a *pré-pró-insulina*. O prefixo "pré" corresponde a um peptídeo-sinal, o endereço que leva a cadeia recém-sintetizada para dentro do retículo endoplasmático e é cortado assim que ela chega. Sobra a *pró-insulina*, uma cadeia única que se dobra e trava sua forma com pontes dissulfeto. Já no grânulo de secreção, proteases cortam nas duas extremidades de um trecho central, liberando duas moléculas: a insulina madura, formada por duas cadeias — A e B — mantidas juntas pelas pontes dissulfeto que já haviam se formado, e o trecho central que foi removido, o #termo-nota[peptídeo C][segmento retirado da pró-insulina durante o processamento; é secretado junto com a insulina em quantidade equivalente e serve para medir a produção própria do pâncreas].

A consequência prática é elegante. Como o peptídeo C é secretado na mesma proporção da insulina, dosá-lo no sangue informa quanta insulina o pâncreas *daquele paciente* está produzindo. Insulina aplicada por injeção não vem acompanhada de peptídeo C. Diante de uma hipoglicemia com insulina alta, portanto, o peptídeo C separa duas histórias muito diferentes: alto aponta para produção endógena excessiva, como num tumor de células beta; baixo aponta para insulina que veio de fora.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-22.png",
  largura: 68%,
  legenda: [O processamento pós-traducional da insulina. O peptídeo-sinal sai na entrada do retículo; as pontes dissulfeto travam a forma da pró-insulina; e o corte final no grânulo separa a insulina madura do peptídeo C, que sai junto com ela na secreção.])

#subtopico("2.2 — A célula beta transformou a própria glicólise num medidor")

A célula beta da ilhota pancreática precisa resolver um problema de engenharia: medir a glicemia continuamente e converter essa medida em secreção proporcional. A solução que ela encontrou é economicamente engenhosa — em vez de construir um sensor dedicado, ela usa o começo da própria via glicolítica como instrumento de medição.

A cadeia funciona assim. A glicose entra na célula beta pelo transportador GLUT2, que tem baixa afinidade e não satura na faixa de glicemia fisiológica — ou seja, quanto mais glicose houver do lado de fora, mais entra, sem teto atrapalhando. Dentro, ela é fosforilada pela #termo-nota[glicoquinase][isoforma hepática e pancreática da hexoquinase, com baixa afinidade pela glicose e sem inibição pelo próprio produto; sua velocidade acompanha a glicemia em toda a faixa fisiológica], que tem a mesma característica: baixa afinidade, sem saturação precoce. O resultado é que a velocidade da glicólise na célula beta é proporcional à glicemia. Mais glicólise significa mais ATP, e é o ATP que fecha um canal de potássio específico da membrana — o canal de potássio sensível ao ATP. Com esse canal fechado, o potássio deixa de vazar para fora, a face interna da membrana fica menos negativa e a célula despolariza. A despolarização abre canais de cálcio dependentes de voltagem, o cálcio entra, e é o cálcio que dispara a fusão dos grânulos com a membrana — a exocitose da insulina.

Vale insistir no ponto que costuma escapar. A glicoquinase não está ali para gerar energia; ela está ali justamente para *não saturar*. Uma enzima de alta afinidade, como a hexoquinase dos outros tecidos, já estaria trabalhando na velocidade máxima em glicemia normal e não conseguiria distinguir uma glicemia de 90 de uma de 180 — as duas dariam a mesma resposta. Uma enzima de baixa afinidade, ao contrário, ainda tem folga para acelerar quando a glicose sobe, e é essa folga que faz do ATP produzido uma leitura fiel do açúcar circulante. Há ainda um segundo motivo, do mesmo tipo: a hexoquinase é inibida pelo seu próprio produto, a glicose-6-fosfato, e portanto se autolimita assim que o produto acumula; a glicoquinase não sofre essa inibição, e por isso continua acompanhando a oferta em vez de se desligar. A mesma lógica explica por que o fígado usa glicoquinase: ele só deve capturar glicose em massa quando há abundância, e não competir com o cérebro no jejum.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-25.png",
  largura: 60%,
  legenda: [As duas curvas contam a diferença. A hexoquinase (verde) já está próxima da velocidade máxima na glicemia basal e não tem para onde subir; a glicoquinase (azul) cruza a glicemia basal na metade do caminho, e por isso ainda responde quando a glicose sobe. Fígado e célula beta usam a segunda; os demais tecidos, a primeira.])

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-26.png",
  largura: 72%,
  legenda: [A cadeia completa na célula beta: a glicose entra pelo GLUT2, a glicoquinase a fosforila, a oxidação mitocondrial eleva o ATP, o ATP fecha o canal de potássio, a membrana despolariza, o canal de cálcio dependente de voltagem se abre e o cálcio dispara a exocitose dos grânulos de insulina.])

#subtopico("2.3 — Duas drogas empurram a mesma porta em sentidos opostos")

Se o canal de potássio é o interruptor que converte química em elétrica, então mexer nele é mexer diretamente na secreção — e a farmacologia faz exatamente isso, nos dois sentidos.

As #termo-nota[sulfonilureias][classe de medicamentos orais que fecham o canal de potássio sensível ao ATP da célula beta, forçando despolarização e secreção de insulina independentemente da glicemia] fecham o canal por conta própria, sem esperar que o ATP suba. A célula despolariza, o cálcio entra e a insulina sai. Por isso são úteis no diabetes tipo 2, em que a periferia responde mal à insulina e uma oferta maior do hormônio ajuda a vencer essa resistência — desde que ainda haja célula beta funcionante para ser estimulada. E por isso mesmo o efeito adverso característico é a hipoglicemia: a droga força secreção mesmo quando a glicemia já está baixa, porque ela substitui o sensor em vez de obedecê-lo.

No sentido inverso está o problema do insulinoma, um tumor de células beta que secreta insulina de forma autônoma e produz hipoglicemia com insulina inapropriadamente alta. O tratamento definitivo é cirúrgico, mas enquanto isso não acontece existe uma opção medicamentosa que é a imagem espelhada da sulfonilureia: um agonista do canal de potássio, que o mantém *aberto*. Com o canal aberto, o potássio continua vazando, a membrana não despolariza, o cálcio não entra e a secreção é contida. É o mesmo canal, operado no sentido contrário.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-27.png",
  largura: 58%,
  legenda: [A sulfonilureia atua sobre o canal de potássio sensível ao ATP da célula beta, fechando-o e forçando a despolarização — a secreção passa a ocorrer sem depender da glicose ter subido.])

#subtopico("2.4 — Glucagon: a mesma cascata, a ordem contrária")

Se a insulina é o hormônio da abundância, o glucagon é o da escassez, e o desenho dos dois é deliberadamente espelhado. Ele é um peptídeo de vinte e nove aminoácidos, produzido pelas células alfa das mesmas ilhotas de Langerhans que abrigam as células beta — os dois sinais opostos nascem lado a lado, no mesmo microambiente, o que facilita a coordenação.

Os estímulos revelam a lógica. A secreção de glucagon é estimulada por hipoglicemia, por adrenalina e pelo aumento de aminoácidos no sangue. Os dois primeiros são intuitivos: falta açúcar, ou o corpo entrou em modo de esforço. O terceiro merece explicação, e ela é bonita — uma refeição rica em proteína e pobre em carboidrato faz subir a insulina, que joga aminoácidos para dentro das células mas também baixaria a glicemia perigosamente; a subida simultânea de glucagon protege contra essa hipoglicemia. É a razão pela qual comer bife puro não derruba o açúcar. Do outro lado, a secreção é inibida pela própria insulina, por corpos cetônicos e pela ureia — sinais de que combustível alternativo já está disponível ou de que a proteólise já foi longe demais.

O mecanismo intracelular é a cascata da PARTE I sem nenhuma novidade estrutural: receptor de superfície no hepatócito, proteína G, adenilato ciclase, AMPc, PKA. O que muda é o repertório de alvos que a PKA encontra no fígado. O resultado é a mobilização de reservas: quebra de glicogênio, produção de glicose a partir de precursores, e, no jejum prolongado, oferta de combustível alternativo. Clinicamente, essa capacidade de elevar a glicemia rapidamente faz do glucagon injetável o socorro para uma hipoglicemia grave em que não se consegue dar açúcar por via oral.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-37.png",
  largura: 60%,
  legenda: [A sinalização do glucagon no hepatócito: receptor de membrana, proteína G trimérica, adenilato ciclase, AMPc, proteína quinase A — e, na saída, a fosforilase quinase que ativa a glicogênio fosforilase.])

#subtopico("2.5 — Fosforilase e sintase: um fosfato, dois destinos opostos")

O metabolismo do glicogênio é o lugar onde a ação hormonal fica visível com mais nitidez, e por isso vale usá-lo como bancada. O pré-requisito, em uma frase: glicogênio é um polímero ramificado de glicose — a despensa de açúcar que o fígado abre para o sangue e que o músculo consome para si. Duas enzimas cuidam dele em sentidos opostos: a #termo-nota[glicogênio fosforilase][enzima que quebra o glicogênio, retirando glicose das extremidades na forma de glicose-1-fosfato] e a glicogênio sintase, que o constrói.

O ponto que organiza tudo é que ambas são reguladas pelo mesmo evento — a fosforilação pela PKA — e respondem a ele de maneira oposta. Fosforilar a fosforilase a *ativa*; fosforilar a sintase a *inativa*. Quando o glucagon ou a adrenalina elevam o AMPc e a PKA entra em ação, a degradação liga e a síntese desliga, simultaneamente e pelo mesmo sinal. Quando a insulina domina, a fosforilação é revertida nas duas enzimas, e o sentido se inverte junto. Essa reciprocidade é o que impede o desperdício de um ciclo fútil, em que a célula gastaria ATP construindo e destruindo o mesmo polímero ao mesmo tempo.

#atencao-box("Fosforilar não é sinônimo de ativar", [A tentação é guardar "fosforilou, ligou" como regra geral, e ela falha exatamente aqui. Fosforilar significa *mudar de estado*; o sentido dessa mudança é uma propriedade da enzima, não do fosfato. A mesma PKA, na mesma célula, no mesmo instante, ativa a glicogênio fosforilase e inativa a glicogênio sintase — e é justamente por o efeito ser oposto nas duas que um único sinal consegue coordenar a via inteira. Quem carrega a regra errada acaba concluindo que o glucagon estimula a síntese de glicogênio, invertendo o sentido do metabolismo no jejum.])

Há ainda uma segunda camada de regulação, alostérica, que roda em paralelo à hormonal e conta uma diferença importante entre tecidos. No músculo, a fosforilase responde ao estado energético local: ATP e glicose-6-fosfato favorecem a forma tensa, menos ativa, sinalizando que há energia de sobra; o AMP faz o contrário, empurrando a enzima para a forma relaxada e ativa, porque AMP alto significa que o ATP está sendo consumido. Assim o músculo pode quebrar glicogênio no início de um esforço mesmo antes de qualquer hormônio chegar. No fígado o sensor é outro: o AMP praticamente não oscila ali, e quem regula é a *glicose livre*, que se liga à forma ativa da enzima e a empurra de volta ao estado inativo. Faz sentido — o fígado quebra glicogênio para servir ao sangue, então basta a glicemia estar reposta para ele parar.

E aqui entra a diferença que mais gera confusão. O músculo não possui glicose-6-fosfatase. A glicose-6-fosfato que ele obtém do próprio glicogênio fica presa dentro da célula, porque a carga do fosfato impede a saída pela membrana, e é queimada localmente para gerar energia. Só o fígado, que possui essa fosfatase, consegue retirar o fosfato e exportar glicose livre para o sangue. Por isso a glicogenólise muscular sustenta a contração, e apenas a hepática sustenta a glicemia.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-31.png",
  largura: 64%,
  legenda: [A glicogênio fosforilase entre suas duas formas. A fosforilase quinase pendura o fosfato e leva a enzima para a forma ativa; a fosfoproteína fosfatase o retira. Em paralelo, os moduladores alostéricos: ATP e glicose-6-fosfato empurram para a forma inativa, o AMP para a ativa, e a glicose age sobre a forma já fosforilada.])

Vale percorrer esses alvos, porque eles mostram que a insulina age em várias frentes ao mesmo tempo e não apenas sobre o glicogênio. No músculo e no tecido adiposo, ela aumenta a captação de glicose recrutando para a membrana o transportador GLUT4, que na ausência do hormônio fica guardado dentro de vesículas — é por isso que esses dois tecidos captam pouca glicose no jejum, enquanto cérebro e fígado, que usam transportadores independentes de insulina, continuam servidos. No endotélio dos capilares, ela induz a lipase lipoproteica, enzima que quebra o triacilglicerol das lipoproteínas circulantes e libera ácidos graxos para o tecido estocar — razão pela qual a insulina também baixa o triacilglicerol do plasma.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-33.png",
  largura: 66%,
  legenda: [O efeito da insulina visto de cima, com os alvos enzimáticos à direita. Repare que o hormônio não faz uma coisa só: aumenta a captação de glicose pelo transportador GLUT4 no músculo e no tecido adiposo, ativa a glicoquinase e a glicogênio sintase no fígado, freia a glicogênio fosforilase e empurra a glicólise adiante.])

#subtopico("2.6 — Desligar o sinal é trabalho ativo, não simples desaparecimento")

Uma cascata que amplifica tanto tem um problema óbvio: se ela não for desmontada, um estímulo passageiro produziria efeito permanente. A célula resolve isso com duas enzimas dedicadas a apagar o que a cascata escreveu, e é importante perceber que ambas *fazem* alguma coisa — o sinal não termina só porque o hormônio saiu do sangue.

A primeira é a *fosfodiesterase*, que abre o anel do AMPc e o converte em AMP comum. Sem AMPc, a PKA volta ao estado inibido, e a cascata para de escrever novos fosfatos. O caminho inverso também é instrutivo: substâncias que inibem a fosfodiesterase deixam o AMPc durar mais e, por isso, prolongam o efeito hormonal sem que uma única molécula de hormônio a mais tenha chegado — é assim que a cafeína potencializa a mobilização de reservas. A segunda é a #sigla("PP1", [proteína fosfatase 1 — enzima que remove os grupos fosfato pendurados pela cascata, revertendo o estado das enzimas do glicogênio]), que remove os fosfatos já pendurados. Repare que as duas atuam em momentos diferentes da mesma história: a fosfodiesterase corta o mensageiro, a fosfatase desfaz a mensagem que já havia sido escrita. É preciso as duas, porque cortar o AMPc não desfosforila sozinho as enzimas que já foram modificadas.

A PP1, além disso, é o ponto em que a insulina fecha o circuito com elegância. Ativar a PP1 significa, num só gesto, desfosforilar a glicogênio fosforilase — que assim se inativa — e desfosforilar a glicogênio sintase — que assim se ativa. A insulina, portanto, não precisa de uma via separada para cada enzima: ela promove a remoção dos fosfatos, e a reciprocidade que já existia entre as duas enzimas faz o resto. Quebra desligada e síntese ligada, com um único movimento.

#mini-resumo[O que ficou de pé: um único sinal, a fosforilação pela PKA, liga a degradação e desliga a síntese do glicogênio; o sinal contrário, a desfosforilação promovida pela insulina através da PP1, faz exatamente o inverso. Duas enzimas apagadoras — fosfodiesterase e PP1 — garantem que o efeito termine quando o estímulo termina.]

#parte-title("PARTE III — Catecolaminas, tireoidianos e esteroides")

#subtopico("3.1 — Adrenalina: um hormônio, dois recados diferentes")

A insulina e o glucagon respondem à disponibilidade de nutriente; a adrenalina responde a outra pergunta — há uma ameaça ou um esforço agora. Ela pertence às catecolaminas, sintetizadas a partir da tirosina numa via curta e bem definida: a tirosina é hidroxilada e vira dopa, a dopa é descarboxilada e vira dopamina, a dopamina recebe outra hidroxila e vira noradrenalina, e a noradrenalina é metilada e vira adrenalina. Duas coisas dessa sequência valem retenção. A primeira é que o passo inicial, catalisado pela tirosina hidroxilase, é o passo limitante da velocidade — é ele que determina o quanto de catecolamina o tecido consegue produzir. A segunda é que a última conversão, de noradrenalina em adrenalina, ocorre essencialmente na medula da glândula adrenal; por isso ela é a fonte da adrenalina que circula no sangue, enquanto os neurônios liberam sobretudo noradrenalina.

O ponto conceitualmente mais rico é que a mesma molécula produz efeitos diferentes conforme o tecido, e a razão não está no hormônio, e sim no receptor que cada tecido expressa. A adrenalina mobiliza combustível nos dois lugares em que o glicogênio importa, mas o destino do açúcar é diferente: no fígado, a glicose sai para o sangue e sustenta o organismo inteiro; no músculo, ela fica dentro e alimenta a contração, pelo motivo já visto — falta a glicose-6-fosfatase. Ao mesmo tempo, o hormônio acelera o coração, dilata as vias respiratórias e redistribui o fluxo sanguíneo. Esse conjunto é o que faz da adrenalina uma droga de emergência, usada em parada cardíaca, choque e anafilaxia — em todos esses cenários o que se busca são exatamente esses efeitos, obtidos em segundos porque a via é a cascata rápida do AMPc, agindo sobre enzimas que já estão prontas.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-40.png",
  largura: 70%,
  legenda: [A biossíntese das catecolaminas em quatro conversões, da tirosina à adrenalina. A tirosina hidroxilase, no primeiro passo, é a etapa limitante da velocidade; a enzima do último passo é praticamente exclusiva da medula adrenal.])

#subtopico("3.2 — Hormônios tireoidianos: o termostato do gasto basal")

Se a adrenalina é o hormônio do sobressalto, os hormônios tireoidianos são o ajuste fino do termostato — mexem no nível em que a máquina inteira funciona, e demoram para produzir efeito porque agem sobre a expressão gênica. A tireoide produz sobretudo tiroxina, o #sigla("T4", [tiroxina — forma predominante secretada pela tireoide, com quatro átomos de iodo; funciona como reservatório circulante]), que carrega quatro átomos de iodo e circula em grande quantidade. Mas a molécula que efetivamente age nos tecidos é a tri-iodotironina, o #sigla("T3", [tri-iodotironina — forma ativa do hormônio tireoidiano, com três átomos de iodo, gerada nos tecidos pela retirada de um iodo do T4]).

O detalhe que transforma isso em mecanismo é a conversão periférica. Enzimas chamadas #termo-nota[desiodases][enzimas que retiram um átomo de iodo do T4, convertendo-o na forma ativa T3 dentro do próprio tecido-alvo] retiram um iodo do T4 já dentro do tecido-alvo, gerando ali o T3 ativo. Isso significa que o T4 funciona como um reservatório circulante de meia-vida longa, e que cada tecido regula localmente quanto hormônio ativo quer produzir a partir dele — uma camada de controle que fica fora do alcance da glândula. Uma vez formado, o T3 entra no núcleo, liga-se ao seu receptor, que se emparelha com um segundo receptor nuclear — o receptor de retinoide X, ou RXR — sobre a região reguladora do gene, e altera a transcrição. Os alvos são amplos: frequência e força cardíacas, crescimento neuronal, síntese e degradação de colesterol e de gordura no fígado, catabolismo proteico e utilização de glicose no músculo, crescimento e maturação óssea.

Essa amplitude explica por que a doença tireoidiana produz quadros tão espalhados. No hipotireoidismo, com pouco hormônio, o gasto cai e o corpo desacelera em várias frentes ao mesmo tempo: fadiga, intolerância ao frio, ganho de peso, pele seca, constipação, lentidão de raciocínio, bradicardia e colesterol alto. No hipertireoidismo, tudo acelera: perda de peso apesar do apetite aumentado, intolerância ao calor, sudorese, tremor, palpitações, diarreia, ansiedade e insônia. Não são duas listas para decorar — são o mesmo eixo, lido nos dois sentidos, e quase todo item pode ser deduzido perguntando o que acontece quando a taxa metabólica sobe ou desce.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-45.png",
  largura: 76%,
  legenda: [À esquerda, a variedade de órgãos-alvo do hormônio tireoidiano — coração, músculo, osso, cérebro, fígado — que explica a amplitude dos sintomas. À direita, o mecanismo: o T4 entra, a desiodase o converte em T3, e o T3 liga seu receptor nuclear sobre o elemento de resposta do gene, alterando a expressão.])

#subtopico("3.3 — Cortisol e o receptor que espera dentro da célula")

O cortisol é o representante dos hormônios esteroides, todos derivados do colesterol, e seu mecanismo é o outro grande modelo de ação hormonal — aquele em que não existe segundo mensageiro nenhum. Sendo lipossolúvel, ele atravessa a membrana sem transportador e encontra seu receptor já dentro da célula. Enquanto não há hormônio, esse receptor fica preso a proteínas acompanhantes que o mantêm inativo; a chegada do esteroide desfaz essa associação e muda o formato do receptor.

O que vem a seguir é sequência pura. Dois complexos hormônio-receptor se juntam formando um dímero, e é esse dímero que reconhece uma sequência específica de DNA na região reguladora dos genes-alvo — o #termo-nota[elemento de resposta][sequência curta e específica de DNA, na região reguladora de um gene, reconhecida pelo complexo hormônio-receptor; é o endereço que define quais genes aquele hormônio controla]. Ligado ali, ele recruta proteínas coativadoras, e o conjunto liga a transcrição daquele gene. O #sigla("RNAm", [RNA mensageiro — cópia do gene que é lida pelo ribossomo para fabricar a proteína correspondente]) recém-produzido é traduzido, e só quando a proteína nova estiver pronta o efeito aparece.

Duas consequências merecem ser guardadas. A primeira é a lentidão: a resposta esteroide começa em horas, porque cada etapa — transcrever, traduzir, dobrar — consome tempo. A segunda é a inércia no sentido inverso: a proteína recém-fabricada continua trabalhando depois que a molécula de hormônio que a encomendou já foi degradada, e por isso o efeito sobrevive à queda do hormônio no sangue. Nada disso acontece com a insulina ou a adrenalina, cujo efeito acaba quando as fosfatases desfazem os fosfatos.

Quanto ao que o cortisol faz, o fio condutor é a mobilização de substrato para enfrentar um período de demanda: ele aumenta a glicemia, favorece a quebra de proteína no músculo para fornecer aminoácidos à produção hepática de glicose, mobiliza gordura, e contém a resposta inflamatória e imune — propriedade que é a base do uso terapêutico dos glicocorticoides. O eixo que o controla vem do hipotálamo, que estimula a hipófise, que libera #sigla("ACTH", [hormônio adrenocorticotrófico — secretado pela hipófise, estimula o córtex da adrenal a produzir cortisol]) para o córtex da adrenal; e o cortisol produzido volta inibindo os dois andares acima, num circuito de retroalimentação negativa.

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-49.png",
  largura: 64%,
  legenda: [A sequência do receptor de hormônio esteroide: o ligante chega, o receptor muda de forma e dimeriza sobre o DNA, e o recrutamento de coativadores é o que efetivamente liga a transcrição do gene.])

#subtopico("3.4 — Quando o eixo quebra, o sentido do erro define o quadro")

Com o mecanismo do cortisol no lugar, as duas doenças clássicas da adrenal deixam de ser nomes a memorizar e passam a ser leituras do mesmo eixo em direções opostas.

Na doença de Addison, o córtex adrenal é destruído — classicamente por um ataque autoimune contra o próprio tecido — e falta cortisol. Como o cortisol era quem freava os andares de cima, sua ausência libera a hipófise, e o ACTH sobe muito. Esse ACTH elevado explica um sinal que de outro modo pareceria arbitrário: o escurecimento da pele. Os primeiros aminoácidos da molécula de ACTH correspondem ao hormônio estimulante de melanócitos, o #sigla("MSH", [hormônio estimulante de melanócitos — sua sequência coincide com o início da molécula de ACTH]), de modo que ACTH em excesso estimula a produção de pigmento. O achado é, literalmente, o excesso do hormônio de cima ficando visível na pele.

Na direção oposta está a síndrome de Cushing, definida por excesso de #termo-nota[glicocorticoide][classe de hormônio esteroide do córtex adrenal, representada pelo cortisol, que eleva a glicemia, mobiliza substrato e contém a inflamação], venha ele da própria adrenal, de estímulo hipofisário aumentado ou de tratamento prolongado com corticoide. Os achados são o efeito fisiológico do cortisol levado ao exagero e mantido no tempo: glicemia alta, catabolismo da proteína muscular com fraqueza, redistribuição da gordura para o tronco e a face, pele fina e defesa imune reduzida. Nenhum desses itens precisa ser decorado se a função do hormônio estiver entendida — basta perguntar o que acontece quando ela roda sem freio.

Por fim, vale registrar uma vulnerabilidade que decorre de todo o mecanismo visto até aqui. Se a especificidade hormonal depende inteiramente do encaixe entre molécula e receptor, então qualquer substância ambiental com formato parecido pode se intrometer nesse encaixe. É o que fazem os #termo-nota[disruptores endócrinos][substâncias ambientais capazes de imitar um hormônio, ativando seu receptor, ou de bloqueá-lo, impedindo o hormônio verdadeiro de agir]: uns imitam o hormônio e ativam o receptor na hora errada; outros ocupam o receptor sem ativá-lo e impedem o hormônio verdadeiro de trabalhar. A precisão do sistema é também a sua fragilidade — um receptor de alta afinidade que reconhece uma molécula em concentração nanomolar é, por construção, sensível a impostores.

#clinica-box("Por que o corticoide não pode ser interrompido de repente", [Um paciente que usa glicocorticoide em dose alta por semanas tem, o tempo todo, o eixo de cima freado pela retroalimentação negativa: com cortisol de sobra vindo do comprimido, o hipotálamo e a hipófise reduzem o estímulo, e o córtex adrenal, sem ser cobrado, vai atrofiando. Se a medicação é suspensa bruscamente, some a fonte externa e a fonte interna ainda não está pronta para assumir — o paciente fica agudamente sem cortisol, exatamente como num Addison, e pode chegar a um quadro grave de hipotensão e hipoglicemia. Por isso a retirada é feita em degraus, dando tempo para o eixo religar. Repare que a explicação inteira sai do circuito de retroalimentação, sem nenhuma informação nova.])

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-50.png",
  largura: 60%,
  legenda: [O eixo hipotálamo-hipófise-adrenal e sua alça de retroalimentação negativa: o cortisol produzido inibe os dois andares acima. É a quebra desse circuito que produz os quadros de falta e de excesso.])

#figura-nebli("/figuras/bioq-10-acao-hormonal/slide-54.png",
  largura: 64%,
  legenda: [Os efeitos do excesso de glicocorticoide distribuídos por tecido — apetite e comportamento, tecido adiposo central, gordura periférica e tecido adiposo marrom. O quadro clínico do excesso é a função normal do hormônio, ampliada e prolongada.])

#conclusao-box[
  O princípio que atravessa esta aula inteira cabe numa frase: *a especificidade está no receptor, e a velocidade está no tipo de alvo*. Nenhum hormônio "escolhe" seu órgão — ele circula por todo o corpo, e responde apenas quem possui a proteína capaz de reconhecê-lo. E nenhum hormônio é rápido ou lento por natureza química: é rápido quando seu alvo final é uma enzima que já existe e só precisa mudar de estado, e lento quando o alvo final é uma proteína que ainda precisa ser fabricada.

  O mecanismo nuclear que sustenta isso é a cascata de amplificação com sinal recíproco. O hormônio hidrossolúvel fica de fora, liga a proteína G, a adenilato ciclase fabrica AMPc, a PKA fosforila os alvos — e como cada degrau é catalítico, poucas moléculas de sinal produzem muito efeito. O mesmo fosfato que ativa a glicogênio fosforilase inativa a glicogênio sintase, e é essa oposição que garante que a célula nunca construa e destrua a mesma reserva ao mesmo tempo. Do outro lado, o hormônio lipossolúvel dispensa segundo mensageiro: entra, encontra o receptor, dimeriza sobre o elemento de resposta e altera a transcrição.

  A clínica que apareceu ao longo do texto não é ilustração — é o mecanismo visto de fora. A sulfonilureia fecha o canal de potássio da célula beta e força secreção, com hipoglicemia como preço; o peptídeo C separa insulina própria de insulina injetada porque só a primeira sai acompanhada dele; a hiperpigmentação do Addison é ACTH elevado ficando visível na pele; a retirada gradual do corticoide respeita o tempo de religar um eixo que ficou meses freado.

  O que vem depois se apoia diretamente nisto. Quando o curso avançar para a integração metabólica entre jejum e período alimentado, a pergunta deixará de ser "o que este hormônio faz" e passará a ser "quais sinais estão presentes ao mesmo tempo, e qual deles domina em cada tecido" — e a resposta será montada com exatamente as peças montadas aqui: quem fosforila, quem desfosforila, e qual tecido tem o receptor e a fosfatase certos para obedecer.
]
