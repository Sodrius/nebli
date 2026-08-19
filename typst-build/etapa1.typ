#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Uma célula do fígado não tem como saber que você acabou de almoçar. Ela não vê o prato, não sente o cheiro, não conversa com o intestino. Mesmo assim, minutos depois da primeira garfada, ela para de fabricar glicose e começa a guardá-la — e faz isso com uma precisão que nenhum comando consciente conseguiria. O que atravessa essa distância é uma molécula lançada no sangue por outro órgão: um hormônio. Este resumo persegue uma única pergunta ao longo de três caminhos: como uma molécula que existe no sangue em quantidade quase inexistente consegue reprogramar o metabolismo de um órgão inteiro. Primeiro, o mecanismo geral — o que faz de uma molécula um hormônio, por que a especificidade mora no receptor e não no mensageiro, e as duas maneiras que a célula tem de ler o recado. Depois, o par insulina e glucagon, que decide a cada hora se o corpo guarda ou gasta, e que serve de caso-modelo das duas grandes rotas de sinalização. Por fim, adrenalina, hormônios tireoidianos e cortisol, que mostram a mesma lógica operando em escalas de tempo diferentes — de segundos a dias — e o que acontece quando uma molécula estranha se senta no lugar do hormônio verdadeiro.
]

#parte-title("PARTE I — Como um sinal químico vira ordem metabólica", primeira: true)

#subtopico("1.1 — As três alavancas da regulação")

Regular o metabolismo significa interferir na velocidade das reações químicas que acontecem no corpo — acelerar uma via, frear outra, e propagar esse ajuste por todas as rotas que dependem dos mesmos intermediários. A célula tem exatamente três maneiras de fazer isso, e elas se distinguem menos pelo *quanto* mudam e mais pelo *quão rápido* mudam.

A primeira é modular a atividade de uma enzima que já existe. Um metabólito se encaixa num sítio da enzima diferente do sítio onde a reação acontece, muda a forma da proteína e, com isso, muda sua eficiência. Enzimas assim — as #termo-nota[enzimas alostéricas][enzimas cuja atividade é modulada por moléculas que se ligam fora do sítio ativo, mudando a forma da proteína inteira] — respondem em milissegundos e sua curva de velocidade contra concentração de substrato não é a hipérbole clássica de Michaelis-Menten, mas uma curva em S: perto do ponto de inflexão, uma variação pequena na concentração produz uma variação enorme na velocidade. É a alavanca da resposta imediata, e ela é sempre local — a enzima está sentindo o que existe dentro daquela célula, naquele instante.

A segunda é a modificação covalente. Uma proteína-quinase pega um grupo fosfato do #sigla("ATP", [adenosina trifosfato — a moeda energética da célula, cujo fosfato terminal é transferido em reações de fosforilação]) e o pendura numa serina, treonina ou tirosina da enzima; uma fosfatase tira esse fosfato de volta. O fosfato é volumoso e carregado negativamente, de modo que sua presença reorganiza a vizinhança da proteína e muda a atividade dela — para cima em algumas enzimas, para baixo em outras. Isso leva segundos a minutos e, ao contrário da modulação alostérica, *não* precisa que o metabólito esteja presente: quem decide fosforilar é uma quinase que recebeu uma ordem de fora. É por essa porta que os hormônios entram.

A terceira é mudar a quantidade de enzima, ligando ou desligando a transcrição do gene que a codifica. Aqui não se ajusta a eficiência de uma molécula: constrói-se ou se desmonta o parque de máquinas. Leva horas a dias, e é a alavanca das adaptações duradouras — o fígado de quem jejua há três dias não tem só enzimas gliconeogênicas mais ativas, tem *mais* enzimas gliconeogênicas.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-03.png",
  largura: 76%,
  legenda: [As três alavancas, lado a lado. À esquerda, a curva sigmoide da enzima alostérica contrasta com a hipérbole de Michaelis-Menten: perto da inflexão, pouca mudança de substrato muda muito a velocidade. No meio, o fosfato indo e voltando entre quinase e fosfatase. À direita, o hormônio chegando à membrana e mudando a expressão. Milissegundos, minutos, horas.])

#mini-resumo[Modulação alostérica responde ao que a própria célula sente, em milissegundos. Modificação covalente e expressão gênica respondem a uma ordem vinda de fora — e é exatamente aí que o hormônio se conecta ao metabolismo.]

Essa distinção é o que torna o controle hormonal necessário. A regulação alostérica resolve muito bem o problema de uma célula isolada se autogerenciando, mas ela é cega para o organismo: o hepatócito não tem como saber, pela sua própria concentração interna de metabólitos, se o intestino está absorvendo nutrientes ou se o músculo está correndo. A integração entre órgãos — responder à abundância e à escassez, adaptar-se às oscilações do dia, atender a uma necessidade fisiológica súbita — exige um sinal que viaje. Esse sinal é químico, viaja pelo sangue e se chama hormônio.

#subtopico("1.2 — O que define um hormônio")

Um hormônio não é definido pelo efeito que produz, e sim por três características que andam juntas: é produzido numa parte do corpo e regula uma função *a distância*, age em quantidades minúsculas, e só produz efeito em células que tenham o receptor certo. A terceira característica é a mais importante e a menos intuitiva, porque desloca a especificidade do lugar onde o aluno costuma colocá-la.

A insulina lançada no sangue banha absolutamente todas as células do corpo — a córnea, o neurônio, o osteoclasto, o eritrócito. Nada na molécula de insulina diz "vá ao músculo". Quem decide é a célula que a recebe: se ela expressa o receptor de insulina, ela responde; se não expressa, a insulina passa por ela como se não existisse. A especificidade, portanto, é uma propriedade do #termo-nota[receptor][proteína da célula-alvo que reconhece o hormônio com altíssima afinidade e converte esse reconhecimento em uma mudança dentro da célula], não do hormônio. Isso tem uma consequência prática enorme: o mesmo hormônio produz efeitos *diferentes* em tecidos diferentes, porque o que muda não é o sinal, é a máquina que está do outro lado do receptor.

A segunda característica — agir em quantidades minúsculas — é uma consequência direta da afinidade. Os receptores hormonais ligam seu hormônio com afinidade altíssima, o que significa que metade deles já está ocupada quando a concentração de hormônio é da ordem de nanomolar ou até picomolar. Para efeito de comparação, a glicose circula em torno de 5 milimolar: o hormônio que a controla está presente num milionésimo dessa concentração. A célula não precisa de muito porque o receptor é um leitor extraordinariamente sensível.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-10.png",
  largura: 58%,
  legenda: [A distância percorrida define o nome, não o mecanismo. No modo endócrino, a molécula cai na corrente sanguínea e age longe; no parácrino, difunde-se pelo interstício e age na célula vizinha; no autócrino, volta e age na própria célula que a produziu. Em todos os três, a resposta depende do receptor da célula que recebe.])

A distância que a molécula percorre até encontrar seu receptor gera três modos de entrega. No modo endócrino, ela é lançada no sangue e atua em órgãos distantes — é o caso da insulina e do cortisol. No modo parácrino, difunde-se pelo líquido intersticial e age nas células vizinhas, como fazem os eicosanoides no foco inflamatório. No modo autócrino, a molécula volta e se liga a receptores da própria célula que a secretou, um arranjo comum em fatores de crescimento e explorado por células tumorais, que passam a fabricar o próprio estímulo de proliferação. O mecanismo de ação é o mesmo nos três casos; muda só a geografia.

Vale desfazer aqui uma fronteira que parece rígida e não é. Adrenalina, noradrenalina e dopamina são hormônios quando a medula da suprarrenal as despeja no sangue, e são neurotransmissores quando um neurônio as libera na fenda sináptica. A molécula é idêntica; o que muda é o modo de entrega e, com ele, a escala. Na fenda sináptica, a concentração é altíssima, a distância é de nanômetros e o efeito dura milissegundos; no sangue, a concentração é nanomolar, a distância é o corpo inteiro e o efeito dura minutos. Sinalização química é um continuum, e as etiquetas descrevem trechos dele.

#figura-lateral("/figuras/bioq-mecanismo-acao-hormonal/slide-12.png",
  lado: "right",
  largura-figura: 44%,
  texto: [Medir algo que existe em concentração nanomolar exigiu um truque engenhoso. No #termo-nota[radioimunoensaio][método de dosagem em que o hormônio da amostra compete com hormônio radioativo por uma quantidade limitada de anticorpo: quanto mais hormônio na amostra, menos radioatividade fica presa ao anticorpo] (#sigla("RIA", [radioimunoensaio — dosagem por competição entre hormônio marcado e hormônio da amostra])), uma quantidade fixa e insuficiente de anticorpo é oferecida a uma mistura de hormônio radioativo com o hormônio da amostra do paciente. Os dois competem pelos mesmos sítios. Quanto mais hormônio o paciente tiver, menos hormônio radioativo consegue se prender ao anticorpo — e é a *queda* do sinal radioativo que mede a concentração. O princípio é o mesmo da afinidade que define o receptor, usado como ferramenta.],
  legenda: [O ensaio por competição: mais hormônio na amostra, menos marcador preso ao anticorpo.])

#subtopico("1.3 — A cadeia regulável e as classes químicas")

A vida de um hormônio é uma sequência de etapas, e cada etapa é simultaneamente um ponto de controle fisiológico e um ponto possível de falha. Ele precisa ser sintetizado, muitas vezes estocado, secretado no momento certo, transportado até o alvo, reconhecido pelo receptor, traduzido numa resposta e, por fim, degradado. Parar em qualquer um desses degraus produz uma doença diferente com o mesmo hormônio no centro: um defeito de síntese, uma falha de secreção, uma proteína transportadora ausente, um receptor mutado e uma degradação lenta demais dão quadros clínicos distintos. Quando se pensa em qualquer distúrbio endócrino, vale percorrer a cadeia inteira antes de culpar a glândula.

Onde cada hormônio se encaixa nessa cadeia depende, em grande parte, de uma única propriedade física: se ele se dissolve em água ou em gordura. E isso, por sua vez, decorre da matéria-prima com que ele foi construído.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-09.png",
  largura: 74%,
  legenda: [As quatro grandes classes químicas pela estrutura. Eicosanoides derivam de um ácido graxo de 20 carbonos; catecolaminas, de tirosina; esteroides, do colesterol — repare no esqueleto de quatro anéis idêntico em todos eles, com pequenas diferenças de grupo lateral separando cortisol de aldosterona e de testosterona; peptídicos, de aminoácidos encadeados, como as duas cadeias da insulina unidas por pontes dissulfeto.])

Os hormônios peptídicos e proteicos — insulina, glucagon, hormônio de crescimento — são cadeias de aminoácidos, portanto hidrofílicos. Dissolvem-se no plasma sem carregador, mas não atravessam a membrana da célula-alvo: o receptor deles fica obrigatoriamente na superfície. Como são fabricados por ribossomos e guardados em vesículas, existe um estoque pronto que pode ser despejado em segundos.

As catecolaminas vêm da tirosina e, embora sejam moléculas pequenas, carregam hidroxilas e um grupo amino que as mantêm hidrofílicas — também são estocadas em vesículas e também usam receptor de superfície.

Os esteroides são o caso oposto. Todos derivam do colesterol e herdam dele o esqueleto de quatro anéis, o que os torna lipossolúveis. Isso muda tudo: eles atravessam membranas livremente, o que significa que *não podem ser estocados* — se fossem, vazariam da célula. São sintetizados sob demanda, e a regulação da secreção é, na prática, a regulação da síntese. No sangue, precisam de proteínas transportadoras para circular, e só a fração livre, não ligada, tem acesso ao receptor — a fração ligada funciona como um reservatório tamponante que sustenta o nível livre. Por ficarem protegidos dentro dessas proteínas, têm meia-vida longa, de horas.

Os hormônios tireoidianos são construídos a partir de tirosinas iodadas e, apesar da origem aminoácida, comportam-se como os esteroides: lipossolúveis, transportados ligados a proteínas, com meia-vida de dias e receptor dentro da célula. Já os eicosanoides, derivados do ácido araquidônico da própria membrana, são o extremo oposto — fabricados na hora, agem na vizinhança imediata e são destruídos em segundos.

#table(
  columns: (auto, auto, auto, auto, auto),
  inset: 7pt,
  align: left,
  table.header([*Classe*], [*Precursor*], [*Solubilidade*], [*Estocagem*], [*Onde está o receptor*]),
  [Peptídicos], [aminoácidos], [em água], [vesículas], [superfície da célula],
  [Catecolaminas], [tirosina], [em água], [vesículas], [superfície da célula],
  [Eicosanoides], [ácido araquidônico], [em lipídio], [não estoca], [superfície da célula],
  [Esteroides], [colesterol], [em lipídio], [não estoca], [dentro da célula],
  [Tireoidianos], [tirosina iodada], [em lipídio], [coloide da tireoide], [dentro da célula],
)

#mini-resumo[A solubilidade decide quase tudo: quem se dissolve em água é estocado, tem meia-vida curta e usa receptor de superfície; quem se dissolve em gordura não pode ser estocado, viaja ligado a proteína, dura muito e usa receptor intracelular.]

#subtopico("1.4 — Receptor de superfície e receptor nuclear")

Um hormônio hidrofílico esbarra na membrana da célula-alvo e não entra. O recado, portanto, tem de ser recriado do lado de dentro por outra molécula — e é essa molécula intracelular fabricada em resposta ao sinal externo que se chama #termo-nota[segundo mensageiro][molécula pequena produzida dentro da célula em resposta à ligação do hormônio ao receptor de superfície, que carrega o recado adiante — o exemplo clássico é o AMP cíclico]. É como um interfone: quem chega não entra no prédio, fala num aparelho na porta, e alguém lá dentro repassa o recado. Um hormônio lipossolúvel, ao contrário, atravessa a membrana como se ela não estivesse lá e vai encontrar seu receptor dentro da célula — tem a chave da porta e vai direto ao arquivo.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-15.png",
  largura: 60%,
  legenda: [As duas rotas gerais. À esquerda, o hormônio peptídico ou amínico se liga do lado de fora e o recado é recriado por um segundo mensageiro, que altera a atividade de enzimas *já existentes* — resposta em segundos a minutos. À direita, o hormônio esteroide ou tireoidiano entra, encontra seu receptor e o complexo age sobre o DNA, alterando a *quantidade* de proteína — resposta em horas.])

A diferença entre as duas rotas não é apenas onde o receptor mora: é o tipo de mudança que cada uma produz e, por consequência, quanto tempo leva. A rota de superfície mexe na atividade de enzimas que já estão prontas na célula — fosforila, desfosforila, abre canal — e por isso responde em segundos. A rota intracelular muda a taxa de transcrição de genes específicos, o que só se traduz em proteína nova depois de transcrever, processar, exportar e traduzir: horas. Em compensação, o efeito dura muito mais, porque a proteína permanece.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-13.png",
  largura: 78%,
  legenda: [O catálogo dos transdutores. O receptor acoplado à proteína G (1) ativa uma enzima que fabrica segundo mensageiro; o receptor tirosina-quinase (2) se autofosforila e dispara uma cascata de quinases que pode chegar ao núcleo; a guanilil-ciclase (3) produz seu próprio segundo mensageiro; o canal iônico com portão (4) muda a concentração de um íon dentro da célula; o receptor de adesão (5) traduz o sinal em mudança de citoesqueleto; e o receptor nuclear (6) regula diretamente a expressão de genes.])

Vale desfazer uma simplificação tentadora. Não é verdade que o hormônio de membrana "só mexe em enzima" e o hormônio lipossolúvel "só mexe em gene". A cascata disparada na superfície também chega ao núcleo — a proteína-quinase A fosforila fatores de transcrição, e o receptor tirosina-quinase termina ativando programas inteiros de expressão. A diferença real é de *velocidade e de rota*: o hormônio de superfície age primeiro sobre o que já existe e só depois, se o estímulo persistir, sobre o que será construído; o hormônio intracelular começa e termina no gene.

Falta explicar como uma concentração nanomolar consegue reprogramar um órgão de centenas de gramas. A resposta está na aritmética da cascata. Uma única molécula de hormônio ativa um receptor; esse receptor, enquanto o hormônio estiver ligado, ativa *várias* moléculas de proteína G; cada proteína G ativa uma adenilato-ciclase, e cada ciclase, enquanto ativa, converte *muitas* moléculas de ATP em segundo mensageiro; cada segundo mensageiro ativa uma quinase, e cada quinase fosforila *muitas* moléculas de enzima-alvo. Como o ganho de cada degrau se multiplica pelo do degrau seguinte, o fator total facilmente alcança dezenas de milhares.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-16.png",
  largura: 68%,
  legenda: [A pirâmide da amplificação. Cada degrau multiplica o número de moléculas ativadas pelo degrau anterior: um receptor ativa várias proteínas G, cada ciclase fabrica muitos segundos mensageiros, cada quinase fosforila muitos alvos. O sinal que entrou em quantidade nanomolar sai como uma resposta em massa.])

Um sistema tão amplificado precisa, obrigatoriamente, de freios igualmente eficientes — e cada degrau tem o seu. A subunidade alfa da proteína G é ela própria uma enzima que hidrolisa o #sigla("GTP", [guanosina trifosfato — nucleotídeo que, ao ser ligado pela proteína G, a mantém na forma ativa]) que a mantém ativa, desligando-se sozinha depois de alguns segundos. A #termo-nota[fosfodiesterase][enzima que quebra o AMP cíclico, encerrando o sinal do segundo mensageiro] destrói o segundo mensageiro. E as fosfatases removem os fosfatos que as quinases puseram. Um sinal que não pode ser desligado é tão perigoso quanto um sinal que nunca chega.

#clinica-box("Quando o interruptor trava ligado: a cólera", [
  A toxina do _Vibrio cholerae_ modifica quimicamente a subunidade alfa da proteína G do enterócito de modo que ela perde a capacidade de hidrolisar o GTP. O resultado não é um sinal mais forte: é um sinal que nunca se desliga. A adenilato-ciclase fica permanentemente ativa, o AMP cíclico se acumula, a proteína-quinase A fosforila sem parar o canal de cloreto da membrana apical, e o enterócito despeja cloreto na luz intestinal. A água segue o sal por osmose, e o paciente perde litros por dia numa diarreia aquosa que pode matar por desidratação em horas. Repare que a lesão não está no hormônio nem no receptor — está no *freio* de um único degrau da cascata.
])

#parte-title("PARTE II — Insulina e glucagon: o par que decide guardar ou gastar")

#subtopico("2.1 — A insulina nasce cortada")

O gene da insulina não codifica insulina. Ele codifica uma cadeia única e contínua de aminoácidos que precisa ser cortada em dois lugares antes de virar hormônio — e entender por que esse desperdício aparente existe explica um dos exames mais úteis da endocrinologia.

O ribossomo da célula beta do pâncreas produz a *pré-pró-insulina*: uma cadeia com um segmento inicial hidrofóbico, a sequência-sinal, seguida das regiões que virarão as cadeias B, C e A. A sequência-sinal é o endereço que leva a cadeia crescente para dentro do retículo endoplasmático e é cortada assim que a entrega é feita, sobrando a *pró-insulina*. Dentro do retículo, a cadeia se dobra sobre si mesma e três pontes dissulfeto se formam entre cisteínas: duas unindo as futuras cadeias A e B, uma terceira interna à cadeia A. Só depois que essas pontes estão prontas, já nas vesículas que brotam do complexo de Golgi, proteases cortam fora o segmento do meio — o #termo-nota[peptídeo C][segmento central da pró-insulina, removido por proteases e secretado junto com a insulina em quantidade equivalente].

O trabalho desse segmento intermediário é justamente ser um andaime. Ele mantém as duas cadeias na geometria certa enquanto as pontes dissulfeto se formam; feitas as pontes, o andaime é dispensável e sai. A insulina madura, portanto, é uma proteína de duas cadeias separadas mantidas juntas apenas pelas pontes — uma arquitetura que seria impossível de montar se as cadeias tivessem sido sintetizadas separadamente.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-22.png",
  largura: 78%,
  legenda: [Da pré-pró-insulina à insulina madura. Acima, os dois cortes: a sequência-sinal sai na entrada do retículo, o peptídeo C sai depois de formadas as três pontes dissulfeto. Abaixo, o trajeto dentro da célula beta — ribossomo, retículo, vesícula de transporte, Golgi, vesícula de secreção — com o processamento acontecendo ao longo do caminho.])

O detalhe que rende clinicamente é este: o peptídeo C é secretado na mesma vesícula e em quantidade equivalente à de insulina, mas não é retirado da circulação pelo fígado com a mesma avidez. Dosá-lo, portanto, mede quanta insulina o pâncreas do próprio paciente está fabricando. Como a insulina de farmácia não vem acompanhada dele, um paciente com hipoglicemia, insulina alta e peptídeo C *baixo* está recebendo insulina de fora; se o peptídeo C estiver alto junto com a insulina, a produção é dele mesmo. A mesma dosagem serve para estimar quanta função de célula beta ainda resta em alguém com diabetes de longa data.

Vale registrar o quanto essa molécula custou a ser encontrada. Em 1889, Minkowski removeu o pâncreas de um cão e viu o animal desenvolver um quadro idêntico ao diabetes, provando que a glândula produzia algo que faltava na doença. Só em 1921 Banting e Best conseguiram extrair esse algo e tratar um cão pancreatectomizado; no ano seguinte, um menino de 14 anos em coma diabético em Toronto recebeu a primeira dose. O Nobel veio em 1923. Entre a demonstração de que existia e o isolamento, passaram-se trinta e dois anos — a dificuldade estava em extrair um peptídeo sem que as próprias proteases do pâncreas o destruíssem.

#subtopico("2.2 — Como a célula beta mede a glicemia")

Para secretar insulina na medida certa, a célula beta precisa antes *medir* a glicemia — e ela faz isso convertendo concentração de glicose em quantidade de ATP. A cadeia inteira tem seis elos, e cada elo existe por uma razão mecânica precisa.

O primeiro elo é a entrada. A glicose atravessa a membrana da célula beta por um transportador da família #sigla("GLUT", [transportadores de glicose por difusão facilitada; a família tem membros com afinidades e distribuições teciduais diferentes]), especificamente o GLUT2, que tem baixa afinidade — ou seja, precisa de muita glicose para trabalhar perto do máximo. É exatamente o que se quer num sensor: um transportador de alta afinidade estaria saturado em qualquer glicemia e informaria sempre a mesma coisa. O GLUT2 fica longe da saturação na faixa fisiológica, de modo que a quantidade de glicose que entra acompanha proporcionalmente a quantidade que existe no sangue.

O segundo elo é a fosforilação. Dentro da célula, a glicose é fosforilada pela #termo-nota[glicoquinase][isoforma hepática e pancreática da hexoquinase, com baixa afinidade pela glicose e sem inibição pelo próprio produto — funciona como sensor de glicemia], que repete a mesma lógica em nível enzimático: alta constante de Michaelis, atividade proporcional à glicemia na faixa que importa, e — decisivo — nenhuma inibição pelo produto glicose-6-fosfato. As hexoquinases dos outros tecidos são o contrário: saturam com pouca glicose e são freadas pelo próprio produto, porque a função delas é abastecer a célula, não medir o meio.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-25.png",
  largura: 56%,
  legenda: [Duas curvas, duas funções. A hexoquinase do músculo já está praticamente no máximo na glicemia basal de 5 mM — ela garante abastecimento constante. A glicoquinase do fígado e da célula beta está em torno de metade da velocidade nessa mesma glicemia, e é justamente por isso que consegue *informar* se a glicose subiu ou caiu.])

Do terceiro elo em diante, a informação vira sinal elétrico. A glicose fosforilada segue pela glicólise e pela oxidação mitocondrial, e a razão entre ATP e ADP dentro da célula sobe. Esse ATP se liga ao #termo-nota[canal de potássio sensível a ATP][canal da membrana da célula beta que fica aberto em repouso deixando potássio sair, e que se fecha quando o ATP intracelular sobe] e o *fecha*. Aqui está o ponto que mais se inverte: fechar um canal de potássio não hiperpolariza, despolariza. Em repouso, esse canal está aberto e o potássio escapa a favor do seu gradiente, levando carga positiva embora e mantendo o interior bem negativo. Fechá-lo interrompe essa fuga, as cargas positivas ficam retidas e o potencial de membrana sobe em direção a valores menos negativos.

A despolarização abre canais de cálcio dependentes de voltagem, o cálcio entra a favor de um gradiente enorme, e é ele quem dispara a fusão das vesículas de insulina com a membrana. A glicose que entrou também estimula, mais lentamente, a síntese de insulina nova — de modo que a mesma molécula que provoca a liberação repõe o estoque.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-26.png",
  largura: 76%,
  legenda: [A cadeia completa da célula beta: glicose entra pelo GLUT2, é fosforilada pela glicoquinase, é oxidada, o ATP sobe, o canal de potássio fecha, a membrana despolariza, o canal de cálcio abre e as vesículas de insulina se fundem com a membrana. Cada seta é um ponto onde um medicamento ou uma mutação pode agir.])

#clinica-box("Sulfonilureias e insulinoma: os dois lados do mesmo canal", [
  As sulfonilureias, usadas no diabetes tipo 2, ligam-se diretamente ao canal de potássio sensível a ATP e o fecham — pulando os elos da glicose, do metabolismo e do ATP. A célula beta despolariza e secreta insulina *independentemente* da glicemia, o que explica ao mesmo tempo a eficácia da droga em quem ainda tem função de célula beta preservada, e o seu risco característico: como a secreção não é mais proporcional à glicose, o paciente pode fazer hipoglicemia se pular uma refeição.

  O insulinoma faz o mesmo estrago por outro caminho: um tumor de células beta secreta insulina de forma autônoma, e o paciente apresenta hipoglicemia com insulina e peptídeo C inapropriadamente altos. O tratamento definitivo é cirúrgico; enquanto ele não vem, usa-se um fármaco que *abre* o canal de potássio, mantendo a célula hiperpolarizada e silenciando a secreção. Esse mesmo fármaco abre canais equivalentes no músculo liso vascular, relaxando o vaso — e é por isso que ele também baixa a pressão arterial.
])

#figura-lateral("/figuras/bioq-mecanismo-acao-hormonal/slide-24.png",
  lado: "left",
  largura-figura: 46%,
  texto: [A família dos transportadores de glicose ilustra como uma mesma função vira tecidos diferentes. O GLUT1 é ubíquo e garante o suprimento basal, inclusive na barreira hematoencefálica. O GLUT2, de baixa afinidade, serve fígado, pâncreas e intestino, onde interessa acompanhar oscilações. O GLUT3, de alta afinidade, abastece o neurônio, que não pode ficar sem glicose nem quando ela cai. E o GLUT4, do músculo e do tecido adiposo, é o único que depende da insulina para chegar à membrana — os demais estão lá o tempo todo.],
  legenda: [Quatro transportadores, quatro estratégias de afinidade e localização.])

#subtopico("2.3 — O que a insulina faz no fígado e no músculo")

Do lado de fora do hepatócito e da fibra muscular, a insulina encontra um receptor que é ele próprio uma enzima: um receptor tirosina-quinase. A ligação do hormônio aproxima as duas metades do receptor, que se fosforilam mutuamente em resíduos de tirosina, e essas tirosinas fosforiladas viram plataformas de ancoragem para proteínas intracelulares. A partir daí a via se ramifica, mas o braço que interessa ao metabolismo termina ativando a proteína-quinase B — também chamada Akt — que é a executora de quase tudo o que a insulina faz.

O primeiro efeito é o mais rápido e o mais visível. No músculo e no tecido adiposo, o transportador GLUT4 não fica na membrana: fica guardado dentro de vesículas no citoplasma. A proteína-quinase B ordena que essas vesículas se desloquem e se fundam com a membrana plasmática, o que multiplica o número de transportadores na superfície. Repare no verbo correto: a insulina não "abre" o GLUT4 nem o fabrica na hora — ela *recruta* transportadores que já existiam. É por isso que o efeito aparece em minutos, e é por isso também que o fígado, cujo GLUT2 já está permanentemente na membrana, não depende da insulina para captar glicose.

O segundo efeito é a inversão em massa do estado de fosforilação da célula. A proteína-quinase B ativa a #termo-nota[fosfoproteína-fosfatase 1][fosfatase que remove fosfatos de várias enzimas do metabolismo do glicogênio ao mesmo tempo, ativando umas e inativando outras] e, ao mesmo tempo, inativa a quinase que mantinha a glicogênio-sintase fosforilada. O resultado é que enzimas do metabolismo do glicogênio perdem seus fosfatos em bloco. E aqui está o detalhe elegante: perder o fosfato *ativa* a glicogênio-sintase e *inativa* a glicogênio-fosforilase. Uma única fosfatase, agindo sobre duas enzimas, liga a síntese e desliga a degradação — porque a mesma marca química significa coisas opostas em cada uma delas.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-32.png",
  largura: 74%,
  legenda: [A cascata da insulina no metabolismo do glicogênio. A quinase ativada pela insulina ativa a fosfatase e desliga as quinases opostas; a fosfatase então desfosforila as duas enzimas de uma vez, ativando a sintase e inativando a fosforilase. À direita, a fosfodiesterase ativada destrói o AMP cíclico — a insulina não só liga a sua própria via, ela apaga a via do sinal contrário.])

O terceiro efeito é o que fecha o círculo com a PARTE I: a insulina também aumenta a *quantidade* de certas enzimas, ligando a transcrição de seus genes. A glicoquinase hepática é o exemplo mais direto — quanto mais insulina de forma sustentada, mais glicoquinase o fígado fabrica, e melhor ele consegue capturar a glicose que chega. Ou seja, um único hormônio aciona as três alavancas da regulação: modula alostericamente, modifica covalentemente e muda a expressão.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-33.png",
  largura: 82%,
  legenda: [O efeito da insulina visto de cima. No fígado, glicose vira glicogênio e o excedente vira gordura exportada como lipoproteína; no músculo, entra glicose e monta-se proteína; no tecido adiposo, os triacilgliceróis são estocados. À direita, os alvos enzimáticos correspondentes — repare que a lista mistura transportador recrutado, enzima desfosforilada e enzima cuja expressão aumentou.])

#subtopico("2.4 — O glucagon e a cascata do AMP cíclico")

Quando a glicemia cai, a célula alfa da mesma ilhota secreta um peptídeo de 29 aminoácidos que dá ao fígado a ordem exatamente oposta. E aqui vale um cuidado: a lógica não é simétrica em todos os detalhes. O estímulo mais óbvio para secretar glucagon é a hipoglicemia, mas ele também é secretado quando chega uma refeição rica em proteínas, situação em que os aminoácidos disparam insulina — e, sem o glucagon acompanhando, essa insulina derrubaria a glicemia de alguém que não comeu carboidrato nenhum. A adrenalina também estimula sua secreção; insulina, corpos cetônicos e ureia a inibem.

O peptídeo é retirado de uma cadeia maior, o pró-glucagon, e é aqui que aparece uma das ideias mais bonitas do processamento pós-traducional. O mesmo gene é transcrito na célula alfa do pâncreas e na célula L do intestino, mas cada tecido expressa uma protease diferente. Na célula alfa, o corte libera o glucagon; na célula intestinal, o mesmo precursor é cortado em outros pontos e libera o GLP-1, uma incretina que *estimula* a secreção de insulina. Um gene, dois produtos com efeitos opostos sobre a glicemia, e quem decide é a tesoura.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-36.png",
  largura: 78%,
  legenda: [O mesmo pró-glucagon, cortado por proteases diferentes, gera produtos diferentes: no pâncreas predomina o corte que libera glucagon; no intestino e no encéfalo, o corte que libera GLP-1 e GLP-2. O processamento é, ele próprio, um ponto de regulação — exatamente como no caso da pró-insulina.])

No hepatócito, o glucagon encontra um receptor de sete hélices transmembrana acoplado a proteína G. A ligação do hormônio muda a forma do receptor, que passa a funcionar como um trocador de nucleotídeo: ele faz a subunidade alfa da proteína G soltar seu #sigla("GDP", [guanosina difosfato — a forma que mantém a proteína G desligada]) e pegar um GTP. Assim carregada, a subunidade alfa se desprende e vai ativar a adenilato-ciclase, uma enzima de membrana que converte ATP em #sigla("AMPc", [AMP cíclico — segundo mensageiro formado a partir do ATP pela adenilato-ciclase]). O segundo mensageiro se liga às subunidades reguladoras da #sigla("PKA", [proteína-quinase A — quinase ativada pelo AMP cíclico, executora da resposta ao glucagon e à adrenalina]), que se soltam e liberam as subunidades catalíticas para fosforilar.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-37.png",
  largura: 72%,
  legenda: [A cascata completa: hormônio, receptor de sete hélices, proteína G trocando GDP por GTP, adenilato-ciclase, AMP cíclico, proteína-quinase A, fosforilase-quinase e, finalmente, a glicogênio-fosforilase passando da forma b para a forma a. Cinco degraus entre o sinal e a glicose liberada — e amplificação em cada um deles.])

O alvo final dessa fosforilação em cadeia é a glicogênio-fosforilase, a enzima que arranca unidades de glicose do glicogênio. A proteína-quinase A não a fosforila diretamente: ela fosforila uma fosforilase-quinase, e *esta* fosforila a fosforilase, convertendo-a da forma b, pouco ativa, para a forma a, ativa. Ao mesmo tempo, a proteína-quinase A fosforila a glicogênio-sintase, inativando-a. É o espelho exato do que a insulina fazia — só que agora a marca colocada é o fosfato, e não a sua remoção.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-31.png",
  largura: 62%,
  legenda: [A fosforilase tem dois níveis de controle sobrepostos. O eixo horizontal é o controle covalente: a quinase põe o fosfato e converte b em a; a fosfatase o retira. O eixo vertical é o controle alostérico, independente do hormônio: no músculo, o AMP acumulado ativa a forma b mesmo sem fosfato, enquanto ATP e glicose-6-fosfato a inibem; no fígado, a própria glicose se liga à forma a e a entrega à fosfatase.])

Esse duplo controle merece atenção porque revela como a ordem hormonal e a informação local se compõem em vez de competir. No músculo em contração intensa, o AMP se acumula porque o ATP está sendo consumido, e esse AMP ativa a fosforilase b diretamente — a fibra mobiliza glicogênio pela sua própria necessidade energética, sem esperar hormônio nenhum. No fígado, ao contrário, a glicose livre se liga à fosforilase a e muda sua conformação de um jeito que a expõe à fosfatase: quando a glicemia já subiu, a própria glicose desliga a enzima que a estava produzindo. O hormônio dá a ordem geral; o metabólito local ajusta a execução.

#mini-resumo[Insulina e glucagon usam receptores de famílias diferentes — tirosina-quinase e acoplado a proteína G — e produzem efeitos opostos sobre as mesmas duas enzimas. A insulina desfosforila em bloco, o glucagon fosforila em cadeia. O estado de fosforilação do fígado é o placar dessa disputa.]

#atencao-box("Glucagon age no fígado; a adrenalina é quem chega ao músculo", [
  A fibra muscular não expressa receptor de glucagon — a mobilização de glicogênio muscular é comandada pela adrenalina, não pelo glucagon. E a diferença não para no receptor: o músculo não tem glicose-6-fosfatase, de modo que a glicose liberada do glicogênio muscular fica presa dentro da própria fibra na forma fosforilada e é queimada ali mesmo. Só o fígado exporta glicose para o sangue. Confundir os dois faz o aluno atribuir ao glucagon um papel na glicemia durante o exercício que na verdade é da adrenalina — e imaginar que o glicogênio do músculo serve para socorrer o cérebro, quando ele serve exclusivamente ao próprio músculo.
])

#parte-title("PARTE III — Adrenalina, tireoidianos e esteroides: a mesma lógica em outras escalas de tempo")

#subtopico("3.1 — Catecolaminas: o metabolismo em alerta")

A adrenalina usa exatamente a mesma cascata que o glucagon — receptor acoplado a proteína G, adenilato-ciclase, AMP cíclico, proteína-quinase A — e é justamente por isso que ela merece ser estudada logo depois dele: o que muda não é o mecanismo, é *onde* o receptor está e *o que mais* o organismo faz ao mesmo tempo.

A síntese parte da tirosina, que a própria célula pode obter da fenilalanina. A tirosina-hidroxilase acrescenta uma hidroxila e produz DOPA; essa é a etapa limitante de toda a via, e portanto o ponto onde a produção é regulada. Uma descarboxilase remove o grupo carboxila e gera dopamina; uma hidroxilase acrescenta outra hidroxila e gera noradrenalina; e uma metiltransferase acrescenta um grupo metila, produzindo adrenalina. Cada enzima muda um grupo químico pequeno, e cada mudança gera uma molécula com perfil de receptor diferente — a via é literalmente uma escada em que cada degrau é um mensageiro distinto.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-40.png",
  largura: 80%,
  legenda: [A escada da biossíntese: tirosina, DOPA, dopamina, noradrenalina, adrenalina. A primeira seta, catalisada pela tirosina-hidroxilase, é a etapa limitante — regular a via é regular essa enzima. Os grupos acrescentados a cada passo estão destacados, e são eles que mudam a afinidade pelos diferentes receptores adrenérgicos.])

A última enzima da via, a que converte noradrenalina em adrenalina, só é expressa em quantidade na medula da suprarrenal — e a razão é anatômica. O sangue que irriga a medula passa antes pelo córtex adrenal, chegando carregado de cortisol em concentração muito maior do que a do sangue sistêmico, e é esse cortisol que induz a expressão daquela enzima. A localização da adrenalina no corpo é, literalmente, uma consequência da ordem em que o sangue atravessa a glândula.

Como catecolaminas são hidrofílicas e ficam prontas dentro de vesículas, a resposta é imediata: um susto libera adrenalina em segundos. E o conjunto dos efeitos tem uma coerência única — todos preparam o corpo para gastar energia agora. No coração, aumentam frequência e força de contração; nos vasos e brônquios, redistribuem o fluxo e ampliam a via aérea, o que junto aumenta a entrega de oxigênio ao músculo. No fígado e no músculo, disparam a mesma cascata do AMP cíclico e mobilizam glicogênio; no tecido adiposo, mobilizam ácidos graxos. E, para não deixar dúvida sobre a direção, ainda estimulam a secreção de glucagon e inibem a de insulina. Todo o organismo converge para o mesmo objetivo: combustível disponível no sangue.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-41.png",
  largura: 82%,
  legenda: [À esquerda, a cascata — idêntica à do glucagon, mas disparada no músculo e no fígado. À direita, a lista de efeitos agrupados pelo resultado que produzem: mais oxigênio entregue, mais glicose produzida, mais ácido graxo disponível, e o reforço hormonal que mantém o quadro.])

#clinica-box("Por que a adrenalina é o fármaco da anafilaxia", [
  Na anafilaxia, mediadores liberados em massa dilatam vasos, aumentam a permeabilidade capilar e contraem a musculatura lisa dos brônquios: o paciente perde pressão porque o leito vascular se abriu e perde ar porque a via se fechou. A adrenalina injetada reverte as três coisas ao mesmo tempo, e por receptores diferentes — contrai o vaso e restaura a pressão pelos receptores alfa, aumenta débito cardíaco e relaxa o brônquio pelos receptores beta. Nenhum outro fármaco age nos três eixos simultaneamente, e é por isso que ela não tem substituto nessa situação, nem na parada cardíaca e no choque.
])

#subtopico("3.2 — Tireoidianos: o hormônio que a tireoide lança não é o ativo")

A tireoide secreta majoritariamente tiroxina, uma molécula com quatro átomos de iodo, mas o receptor dentro da célula-alvo tem afinidade muito maior por uma versão com *três* iodos. Ou seja: o que circula em quantidade é um pró-hormônio, e a decisão de ativá-lo é tomada não pela glândula, mas por cada tecido, um a um.

Quem executa essa decisão são as desiodinases. Uma #termo-nota[desiodinase][enzima que remove um átomo de iodo do hormônio tireoidiano; conforme o anel de onde retira o iodo, o produto é o hormônio ativo ou uma forma inativa] retira um iodo do anel externo e produz #sigla("T3", [tri-iodotironina — a forma ativa do hormônio tireoidiano, com três iodos]), a forma ativa; outra retira um iodo do anel interno da mesma molécula de #sigla("T4", [tiroxina — forma secretada em maior quantidade pela tireoide, com quatro iodos, que funciona como pró-hormônio]) e produz T3 reverso, que não ativa o receptor. O substrato é o mesmo; o produto depende de qual anel perdeu o iodo. Isso dá a cada tecido um controle local sobre a intensidade do sinal que recebe — e explica um achado clínico frequente: em doença grave, jejum prolongado ou estresse fisiológico intenso, a desiodinase que inativa é favorecida, o T3 cai, o T3 reverso sobe, e o organismo baixa deliberadamente seu gasto energético mesmo com a tireoide funcionando normalmente.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-43.png",
  largura: 62%,
  legenda: [O eixo hipotálamo-hipófise-tireoide e o desvio para o T3 reverso. O hormônio liberador do hipotálamo estimula a hipófise a secretar o hormônio tireoestimulante, que estimula a tireoide; T4 e T3 retroalimentam negativamente os dois andares acima. Repare que, no estresse fisiológico, a mesma quantidade de T4 pode gerar mais forma inativa do que ativa.])

Acima da glândula existe o eixo clássico: o hipotálamo secreta #sigla("TRH", [hormônio liberador de tireotrofina — peptídeo hipotalâmico que estimula a hipófise]), a hipófise responde com #sigla("TSH", [hormônio tireoestimulante — hormônio hipofisário que estimula a tireoide a produzir e liberar hormônio tireoidiano]), e o hormônio tireoidiano produzido retroalimenta negativamente os dois andares de cima. É a arquitetura de um termostato: quanto mais produto no sangue, menos ordem de produzir. Por isso a dosagem do hormônio hipofisário é um indicador tão sensível — ele se move na direção *oposta* à do hormônio da glândula.

Chegando à célula, o T3 encontra um receptor que já está sentado no DNA, ligado a uma sequência específica junto com um receptor parceiro, mesmo *antes* de o hormônio chegar. E, na ausência de hormônio, esse complexo não é neutro: ele recruta correpressores e freia ativamente a transcrição dos genes que controla. A chegada do T3 muda a forma do receptor, os correpressores saem, coativadores entram, e a transcrição dispara. A consequência conceitual é importante: falta de hormônio tireoidiano não é apenas ausência de estímulo, é presença de um freio — e é parte da razão pela qual a carência durante o desenvolvimento do sistema nervoso produz um dano tão profundo e irreversível.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-45.png",
  largura: 80%,
  legenda: [À esquerda, os órgãos-alvo e o que o hormônio faz em cada um: frequência e hipertrofia no coração, crescimento e maturação no osso, catabolismo proteico e uso de glicose no músculo, síntese de colesterol e metabolismo de gordura no fígado, crescimento neuronal no encéfalo. À direita, o mecanismo comum: T4 convertido em T3 pela desiodinase, T3 ligando-se ao receptor já pousado sobre o elemento responsivo do DNA, e a expressão do gene mudando.])

#subtopico("3.3 — Cortisol: do colesterol ao gene")

O cortisol é o exemplo mais completo de hormônio esteroide, e cada etapa da sua vida ilustra uma consequência da lipossolubilidade. Ele é fabricado no córtex da suprarrenal a partir do colesterol, por uma sequência de hidroxilações e oxidações: uma enzima corta a cadeia lateral do colesterol e produz pregnenolona — esse é o passo limitante, e é exatamente nele que o estímulo hipofisário age; daí a via segue por progesterona e 17-hidroxi-progesterona até o cortisol. Os mesmos intermediários, desviados por hidroxilases diferentes, dão aldosterona numa zona do córtex e androgênios em outra: uma única árvore metabólica, três produtos, e a zona da glândula decidindo o ramo.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-51.png",
  largura: 78%,
  legenda: [A árvore da esteroidogênese adrenal. Do colesterol saem, pelo mesmo tronco, os três ramos: mineralocorticoide (aldosterona), glicocorticoide (cortisol) e androgênio. Bloquear uma das hidroxilases não apenas derruba o produto daquele ramo — desvia o fluxo acumulado para os ramos vizinhos, e é por isso que deficiências enzimáticas dessa via dão, ao mesmo tempo, falta de um hormônio e excesso de outro.])

Como esteroide não pode ser estocado, não existe reserva pronta: regular a secreção é regular a síntese, e é por isso que a resposta do cortisol a um estresse leva minutos a horas, não segundos como a da adrenalina. No sangue, mais de nove décimos do cortisol viajam ligados a uma globulina transportadora, e só a fração livre entra nas células — o que torna a fração ligada um reservatório que amortece oscilações e prolonga a meia-vida.

O eixo que o comanda tem três andares. O estresse leva o hipotálamo a secretar #sigla("CRH", [hormônio liberador de corticotrofina — peptídeo hipotalâmico que estimula a hipófise a secretar ACTH]); a hipófise responde com #sigla("ACTH", [hormônio adrenocorticotrófico — hormônio hipofisário que estimula o córtex adrenal a sintetizar cortisol]); o córtex adrenal produz cortisol; e o cortisol freia tanto o hipotálamo quanto a hipófise.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-50.png",
  largura: 64%,
  legenda: [O eixo do cortisol com suas duas alças de retroalimentação negativa — no hipotálamo e na hipófise. Abaixo, o que acontece quando o córtex adrenal falha: sem cortisol, o freio some, e o hormônio hipofisário sobe sem limite.])

#atencao-box("A pele escurecida da insuficiência adrenal não vem do cortisol baixo", [
  Quando uma agressão autoimune destrói o córtex adrenal, o cortisol despenca — e, sem cortisol, desaparece a retroalimentação negativa sobre a hipófise. O hormônio adrenocorticotrófico então sobe muito, tentando estimular uma glândula que não pode responder. Acontece que os primeiros aminoácidos dessa molécula são idênticos aos do hormônio estimulante de melanócitos, de modo que, em concentração alta, ele ativa o melanócito e escurece a pele e as mucosas. Ou seja: a hiperpigmentação é sinal de *ACTH alto*, não de cortisol baixo em si — e é justamente por isso que ela aparece na falência da própria glândula adrenal e não quando a hipófise é que falhou.
])

Dentro da célula-alvo, o cortisol atravessa a membrana e encontra seu receptor no citoplasma, mantido inativo por uma proteína-chaperona que o segura. A ligação do hormônio solta a chaperona, o receptor muda de forma, dimeriza e entra no núcleo, onde se prende a sequências específicas do DNA — os elementos responsivos a glicocorticoide — e liga ou desliga a transcrição dos genes vizinhos. Resposta em horas, duradoura, e proporcional ao número de genes que aquele tipo celular tem sob esse controle.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-52.png",
  largura: 74%,
  legenda: [O caminho do glicocorticoide: atravessa a membrana, libera o receptor da chaperona que o mantinha inativo, entra no núcleo, liga-se ao elemento responsivo no DNA e altera a quantidade de RNA mensageiro — e, portanto, a quantidade das proteínas que executam a resposta. É o mesmo desenho do receptor de hormônio tireoidiano, de vitamina D e de ácido retinoico.])

O conjunto dos efeitos metabólicos tem uma coerência que vale enunciar de uma vez: manter glicose disponível para o cérebro num contexto de estresse prolongado. No fígado, o cortisol estimula a gliconeogênese e o acúmulo de glicogênio. No músculo, inibe a captação de glicose e acelera a degradação de proteína, fornecendo os aminoácidos que o fígado usará como matéria-prima. No tecido adiposo, também inibe a captação de glicose e estimula a lipólise, liberando o glicerol que serve de esqueleto para a glicose nova. E no pâncreas, inibe a secreção de insulina e estimula a de glucagon, garantindo que a glicose produzida não seja imediatamente guardada de volta. Cada tecido faz uma coisa diferente, e todas apontam para o mesmo lugar.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-53.png",
  largura: 80%,
  legenda: [À direita, os efeitos tecido a tecido — fígado, músculo esquelético, tecido adiposo e pâncreas — que juntos sustentam a glicemia. À esquerda, o que o excesso crônico produz: hiperglicemia, hipertensão, imunossupressão, alterações de humor e redistribuição de gordura.])

Esses mesmos efeitos, sustentados por tempo demais, explicam o quadro do excesso crônico de glicocorticoide: a gliconeogênese permanente e a resistência à insulina dão hiperglicemia; o catabolismo proteico prolongado adelgaça músculo e pele; a supressão da transcrição de mediadores inflamatórios — que é a razão pela qual glicocorticoides são fármacos anti-inflamatórios tão potentes — vira imunossupressão indesejada; e a redistribuição da gordura, que se acumula no tronco enquanto se perde nos membros, desenha a silhueta característica. Vale reter que o mesmo mecanismo que torna a droga útil é o que produz seus efeitos adversos: não são fenômenos separados.

#subtopico("3.4 — Quando o receptor é enganado")

Se a especificidade do sistema endócrino mora no encaixe entre uma molécula e um bolso de proteína, então qualquer molécula com a forma aproximadamente certa pode entrar nesse bolso — e o receptor não tem como saber que aquilo não é o hormônio verdadeiro. É essa vulnerabilidade que define os #termo-nota[disruptores endócrinos][substâncias do ambiente que se ligam a receptores hormonais, imitando o hormônio ou bloqueando o acesso dele, e alterando a sinalização normal].

Há duas maneiras opostas de enganar o receptor, e ambas produzem doença. Uma molécula que se liga *e* ativa é um imitador: o tecido recebe uma ordem hormonal que não foi dada por glândula nenhuma, no momento errado e na intensidade errada. Uma molécula que se liga e *não* ativa é um bloqueador: ela ocupa o sítio e impede o hormônio verdadeiro de entrar, de modo que a ordem legítima deixa de ser lida mesmo com a glândula funcionando perfeitamente. Diante de um distúrbio hormonal, portanto, a dosagem do hormônio no sangue pode estar normal e a sinalização estar profundamente alterada.

#figura-nebli("/figuras/bioq-mecanismo-acao-hormonal/slide-55.png",
  largura: 78%,
  legenda: [À esquerda, a situação normal: o hormônio ocupa o receptor e a resposta acontece. No meio, o imitador ocupa o receptor e dispara uma resposta que não deveria existir. À direita, o bloqueador ocupa o receptor sem ativá-lo, e a resposta legítima não acontece. Em nenhum dos três casos o receptor "percebe" a diferença — ele só lê forma.])

Os receptores mais vulneráveis são justamente os intracelulares, dos hormônios lipossolúveis. Uma molécula ambiental que se dissolve em gordura atravessa membranas com a mesma facilidade do esteroide, alcança o núcleo e ainda por cima se acumula no tecido adiposo do organismo, prolongando a exposição muito além do contato inicial. É por isso que compostos industriais persistentes e lipossolúveis são o grupo clássico de preocupação.

Vale fechar reconhecendo que a farmacologia inteira trabalha por esse mesmo princípio, de propósito. A sulfonilureia fecha um canal que o ATP fecharia; o fármaco usado no insulinoma abre esse mesmo canal; a adrenalina injetada é um agonista de receptores que existem para a adrenalina endógena; um betabloqueador é um antagonista que ocupa o receptor sem ativá-lo; e o glicocorticoide sintético usa o receptor do cortisol para desligar genes da inflamação. A diferença entre um medicamento e um disruptor não está no mecanismo — está em quem escolheu a dose, o momento e o alvo.

#conclusao-box[
  Um princípio único atravessou as três partes deste resumo: a informação hormonal não está na molécula que viaja, e sim no receptor que a lê. Como a especificidade mora no receptor, o mesmo sinal pode significar coisas opostas em tecidos diferentes, uma concentração nanomolar basta para reprogramar um órgão inteiro, e qualquer molécula com a forma certa pode se passar pelo mensageiro verdadeiro.

  O mecanismo nuclear que se repetiu em todos os casos é a conversão de um recado externo numa mudança do estado de uma proteína. Os hormônios hidrofílicos fazem isso pela via do segundo mensageiro — receptor de superfície, proteína G ou tirosina-quinase, cascata de quinases, fosforilação de enzimas prontas, resposta em segundos; e o par insulina-glucagon mostrou que essa fosforilação é um placar disputado, com uma fosfatase de um lado e uma quinase do outro escrevendo sinais opostos nas mesmas duas enzimas do glicogênio. Os hormônios lipossolúveis fazem o mesmo por outro caminho — atravessam a membrana, encontram um receptor que é um fator de transcrição e mudam a quantidade de proteína, em horas, de forma duradoura.

  A clínica que apareceu ao longo do texto não foi ilustração: cada quadro localizava a lesão num degrau específico dessa cadeia. A cólera trava o freio da proteína G; a sulfonilureia entra no canal de potássio da célula beta; o insulinoma remove a proporcionalidade entre glicose e secreção; a insuficiência adrenal derruba a retroalimentação e libera o hormônio hipofisário a ponto de escurecer a pele; e o disruptor endócrino ocupa o bolso do receptor. Saber onde está o degrau é saber o que a doença vai produzir.

  Daqui em diante, a mesma cadeia reaparece em escala maior. O passo seguinte é a integração metabólica propriamente dita — o que acontece no corpo inteiro nas horas após a refeição, no jejum curto, no jejum prolongado e no exercício, quando esses mesmos hormônios atuam simultaneamente sobre fígado, músculo e tecido adiposo. Tudo o que foi visto aqui como mecanismo isolado vira, ali, o vocabulário para descrever estados fisiológicos completos.
]
