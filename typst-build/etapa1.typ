#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Toda imagem do fígado é uma pergunta sobre estrutura. O #sigla("US", [ultrassonografia — imagem formada pelos ecos que o tecido devolve ao transdutor]) mostra quanto o tecido devolve de som; a #sigla("TC", [tomografia computadorizada — imagem formada pela atenuação de um feixe de raios X, medida em unidades Hounsfield]) mostra quanto ele freia um feixe de raios X; e as duas coisas mudam quando a arquitetura interna muda. É por isso que existe correlação radiopatológica: o patologista corta a peça e vê o arranjo real das células, dos vasos e do colágeno, e esse arranjo é exatamente a causa física do que o radiologista viu antes. Este resumo percorre o caminho nas duas direções, sobre um único órgão. A PARTE I monta a régua — como o fígado normal se organiza e por que essa organização produz um padrão de imagem previsível. A PARTE II segue uma mulher de 20 anos, assintomática, com um nódulo achado por acaso, até o bloco de parafina que explica o padrão dela. A PARTE III acompanha um homem de 30 anos, etilista, com dor abdominal, pelo caminho que vai da gordura no hepatócito até a hipertensão portal e seus desfechos. No fim, o que sobra não é uma lista de doenças: é o hábito de olhar uma imagem e perguntar que alteração de tecido a produziu.
]

#parte-title("PARTE I — O fígado normal e a régua da imagem", primeira: true)

#subtopico("1.1 — A arquitetura que a imagem enxerga")

O fígado é o único órgão do corpo que recebe sangue por duas vias ao mesmo tempo, e essa peculiaridade governa tudo o que vem depois — a distribuição das lesões, o comportamento do contraste, o caminho da hipertensão portal. Cerca de três quartos do sangue que chega vêm da veia porta, sangue venoso já usado pelo intestino, pobre em oxigênio mas carregado de tudo o que foi absorvido. O quarto restante vem da artéria hepática, sangue arterial rico em oxigênio. As duas correntes chegam juntas ao #termo-nota[espaço porta][região de tecido conjuntivo nos vértices do lóbulo hepático, contendo ramo da veia porta, ramo da artéria hepática e ducto biliar — a "tríade portal"], se misturam e atravessam o parênquima por capilares de parede descontínua, os #termo-nota[sinusoides][capilares hepáticos de endotélio fenestrado, sem membrana basal contínua, que permitem contato direto do plasma com o hepatócito]. No fim do percurso, um único caminho de saída: a veia centrolobular, que converge para as veias hepáticas e destas para a veia cava inferior.

Repare no que essa geometria implica. O sangue entra pela periferia do lóbulo e sai pelo centro, então o hepatócito que fica perto do espaço porta recebe sangue oxigenado e cheio de nutrientes, e o hepatócito que fica perto da veia central recebe o resto — sangue já espremido pelos vizinhos. Essa desigualdade é tão sistemática que se convencionou dividir o parênquima em três zonas ao longo do trajeto: zona 1 junto ao espaço porta, zona 2 intermediária, zona 3 junto à centrolobular. A consequência prática aparece na lâmina de qualquer necrópsia: numa queda de perfusão — choque, insuficiência cardíaca, parada — quem morre primeiro é a zona 3, porque ela já vivia no limite do oxigênio disponível.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-07.png",
  largura: 68%,
  legenda: [Histologia do fígado normal. À esquerda, o espaço porta com a tríade; os números 1, 2 e 3 marcam o gradiente do parênquima ao longo do trajeto do sangue, da periferia do lóbulo até a veia centrolobular. Repare que os cordões de hepatócitos se dispõem em raios convergentes — é essa geometria radial que define as zonas.]
)

Há uma sutileza de nomenclatura que vale desfazer agora, porque ela reaparece toda vez que se fala em lesão zonal. O *lóbulo clássico* é a unidade morfológica: um hexágono centrado na veia centrolobular, com espaços porta nos vértices. O *ácino de Rappaport* é a unidade funcional: um losango centrado no eixo vascular que sai do espaço porta, cujas pontas são duas veias centrolobulares. Quem explica o gradiente metabólico é o ácino, não o lóbulo — e é por isso que a zona 1 concentra gliconeogênese e oxidação de ácidos graxos, funções caras em oxigênio, enquanto a zona 3 concentra glicólise e a metabolização de xenobióticos pelo citocromo P450. Essa última informação tem consequência direta: a intoxicação por paracetamol necrosa preferencialmente a zona 3 porque é lá que a enzima que gera o metabólito tóxico está mais concentrada, somando dano químico a uma região que já é a mais hipóxica.

#mini-resumo[Em uma frase: o sangue entra pelo espaço porta e sai pela centrolobular, e essa direção única cria um gradiente de oxigênio que faz a zona 3 ser a primeira a sofrer em qualquer queda de perfusão.]

Na macroscopia, o fígado normal tem superfície lisa, cor marrom-avermelhada uniforme e borda fina e cortante. Ao corte, o parênquima é homogêneo e os espaços porta aparecem como pequenos pontos esbranquiçados de tecido conjuntivo, com os vasos abertos no meio. Guardar essa imagem importa mais do que parece: praticamente todo diagnóstico macroscópico de doença hepática crônica é feito por comparação com ela — superfície que deixou de ser lisa, cor que deixou de ser uniforme, borda que deixou de ser fina.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-06.png",
  largura: 60%,
  legenda: [Fígado normal. Acima, a superfície externa: lisa, brilhante, cor uniforme, sem nódulos. Abaixo, o corte mostrando um espaço porta de grande calibre com seus ramos ramificando-se em leque no parênquima marrom homogêneo. É esta a referência contra a qual toda peça alterada será comparada.]
)

#subtopico("1.2 — Ecogenicidade e densidade: as duas réguas do fígado normal")

Cada método de imagem mede uma grandeza física diferente, e trocar uma pela outra é o erro mais comum de quem está começando. Pense no ultrassom como alguém batendo na parede e ouvindo o retorno: o aparelho emite um pulso sonoro e escuta o eco que volta de cada interface entre tecidos de impedância diferente. A #termo-nota[ecogenicidade][capacidade de um tecido de refletir o som de volta ao transdutor; quanto mais interfaces refletoras, mais claro o tecido aparece] de uma estrutura é, portanto, a densidade de interfaces refletoras que ela contém, não a sua dureza nem o seu peso. Já a tomografia mede outra coisa: quanto de um feixe de raios X o tecido absorve pelo caminho. Essa atenuação é expressa em #sigla("UH", [unidade Hounsfield — escala de atenuação de raios X ancorada em dois pontos fixos: água igual a zero, ar igual a menos mil]), e é ela que define se um pixel sai claro ou escuro na TC.

Com as duas réguas na mão, o fígado normal fica fácil de descrever. No ultrassom, o parênquima é homogêneo, finamente granular, e sua ecogenicidade é igual ou discretamente maior que a do córtex renal adjacente — a comparação fígado/rim é a referência de rotina justamente porque os dois ficam lado a lado na mesma imagem. As veias hepáticas e portais aparecem como estruturas tubulares anecoicas, isto é, pretas, porque sangue fluindo é homogêneo e devolve pouquíssimo eco; as portais se distinguem por terem parede ecogênica, o brilho da bainha fibrosa que as acompanha. Na tomografia sem contraste, o parênquima hepático mede em torno de 55 a 65 UH, e o baço fica alguns pontos abaixo — o fígado é normalmente *mais* denso que o baço.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-11.png",
  largura: 58%,
  legenda: [Ultrassom hepático normal em dois cortes. Parênquima homogêneo e finamente granular, ecogenicidade semelhante à do córtex renal, veias hepáticas visíveis como trilhos escuros convergindo para a cava. A cápsula aparece como a linha branca fina que contorna o órgão.]
)

Essa última frase carrega mais do que aparenta, porque ela é a base de toda a quantificação de gordura hepática por tomografia. A gordura tem atenuação baixíssima, em torno de menos cem unidades Hounsfield; cada ponto percentual de infiltração gordurosa derruba a densidade do fígado em aproximadamente uma unidade e meia. Então, quando o parênquima hepático fica *menos* denso que o baço na imagem sem contraste, a inversão da relação normal já é diagnóstico de esteatose sem precisar de qualquer contraste — e essa é exatamente a leitura que vai reaparecer no caso 2.

#atencao-box("Hiperecogênico e hiperdenso não são a mesma coisa",
  [O erro nasce da semelhança dos prefixos e sobrevive porque as duas palavras significam "claro na imagem". Só que uma lesão pode ser hiperecogênica ao ultrassom e hipodensa à tomografia ao mesmo tempo, sem nenhuma contradição — o hemangioma e a esteatose focal fazem exatamente isso. A razão é física: brilho no ultrassom vem de quantidade de interfaces que refletem som; brilho na tomografia vem de capacidade de absorver raios X. São propriedades independentes do tecido. Descrever uma lesão com o adjetivo do método errado transforma o laudo em ruído para quem o lê depois.]
)

#subtopico("1.3 — As três fases do contraste, e por que elas existem")

A dupla aferência que a PARTE I abriu no subtópico anterior é o que torna a tomografia com contraste tão poderosa no fígado. Injetado numa veia periférica, o contraste iodado chega primeiro ao coração direito, atravessa o pulmão, retorna ao coração esquerdo e sai pela aorta — e a partir daí só existem dois caminhos para alcançar o parênquima hepático. Um é curto: aorta, tronco celíaco, artéria hepática, sinusoide. O outro é longo: aorta, artéria mesentérica, capilares do intestino, veia porta, sinusoide. Como o segundo trajeto atravessa um leito capilar inteiro antes de chegar, ele demora aproximadamente meio minuto a mais. É essa diferença de tempo que cria as fases.

Na *fase arterial*, adquirida cerca de 25 a 35 segundos após a injeção, só chegou ao fígado o contraste que veio pela artéria hepática — um quarto do fluxo total. O parênquima normal, portanto, realça pouco. Quem acende nessa fase é qualquer estrutura que receba sangue predominantemente arterial: a própria aorta, o baço, e as lesões hipervasculares que se alimentam por neovasos arteriais. Na *fase portal*, entre 60 e 80 segundos, chega a onda grande, os três quartos que vieram pela porta, e o parênquima hepático atinge o pico de realce. Na *fase de equilíbrio*, a partir de três minutos, o contraste já se distribuiu pelo interstício de todo o corpo e começa a ser eliminado; o fígado vai clareando de volta ao basal.

#figura-lateral(
  "/figuras/correlacao-radio-pato-2/slide-26.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O sistema porta explica por que a fase portal é a fase do fígado. As veias mesentéricas superior e inferior drenam todo o intestino, a veia esplênica drena o baço, e as três convergem atrás do pâncreas formando a veia porta, que entra no hilo hepático e se ramifica até os sinusoides. Todo esse sangue precisa atravessar o fígado antes de alcançar a cava inferior — e é exatamente por isso que, quando o fígado oferece resistência à passagem, a pressão sobe em todo o território a montante, do esôfago ao reto.],
  legenda: [Anatomia do sistema porta: mesentérica superior, mesentérica inferior e esplênica confluindo para a veia porta.]
)

Duas consequências decorrem disso e valem ser ditas explicitamente, porque são a chave de leitura de metade das tomografias de abdome. A primeira: uma lesão que realça intensamente na fase arterial e depois fica *mais escura* que o parênquima nas fases tardias é uma lesão que tem aporte arterial próprio e drenagem venosa rápida. Esse comportamento tem nome — #termo-nota[washout][queda relativa de realce de uma lesão em relação ao parênquima nas fases tardias, porque ela perde contraste mais rápido do que o tecido ao redor] — e é o comportamento típico do carcinoma hepatocelular. A segunda: uma lesão que capta pouco na arterial, capta um pouco mais na portal e *retém* contraste no tardio tem um compartimento vascular lento, onde o meio de contraste entra devagar e demora a sair. Esse é o comportamento do hemangioma, e é o que o caso 1 vai mostrar imagem por imagem.

#mini-resumo[O que ficou de pé: fase arterial mostra quem tem artéria própria, fase portal mostra o parênquima no pico, fase de equilíbrio mostra quem retém e quem lava. A leitura dinâmica vale mais do que qualquer imagem isolada.]

#clinica-box("Por que a fase importa na prática",
  [Um paciente cirrótico faz ultrassom de rastreio a cada seis meses. O exame encontra um nódulo de dois centímetros que antes não existia. Se a tomografia seguinte for adquirida só na fase portal — que é a fase de rotina do abdome —, o nódulo pode passar despercebido, porque nessa fase ele fica com densidade parecida com a do parênquima. É preciso pedir explicitamente o protocolo trifásico. Quando a arterial mostra realce intenso e a tardia mostra washout, o diagnóstico de carcinoma hepatocelular está feito por imagem, sem punção. Escolher a fase errada não atrasa o laudo: atrasa o tratamento.]
)

#parte-title("PARTE II — Caso 1: o nódulo achado por acaso")

#subtopico("2.1 — O achado incidental e a pergunta que ele obriga")

Mulher de 20 anos, sem queixa nenhuma, faz exames de rotina e o ultrassom de abdome encontra um nódulo no fígado. A situação parece banal e não é: ela inaugura uma categoria inteira de problema clínico, o achado incidental, em que a lesão foi encontrada *antes* de dar qualquer sintoma e a pergunta deixa de ser "o que está causando a queixa" e passa a ser "isto precisa de alguma coisa". Uma paciente jovem, sem hepatopatia, sem fator de risco, com fígado de arquitetura normal ao redor, tem probabilidade pré-teste baixíssima de câncer primário de fígado — e probabilidade alta de estar diante da lesão hepática benigna mais comum que existe.

A imagem confirma o palpite. O nódulo é sólido, pequeno, homogeneamente claro, de contornos bem definidos e regulares, sem halo escuro ao redor, situado no parênquima sem distorcer os vasos vizinhos. Cada um desses adjetivos carrega informação estrutural: homogêneo significa que o interior é uniforme, sem áreas de necrose ou hemorragia; bem delimitado significa que a lesão empurra o parênquima em vez de infiltrá-lo; a ausência de halo hipoecoico afasta o anel de parênquima comprimido e edemaciado que costuma acompanhar as metástases.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-03.png",
  largura: 56%,
  legenda: [Ultrassom da paciente. A seta aponta o nódulo hiperecogênico, homogêneo e de limites nítidos, no interior de um parênquima hepático de textura normal. Repare que as veias hepáticas ao redor seguem seu trajeto sem desvio nem compressão — a lesão convive com a arquitetura, não a destrói.]
)

O brilho da lesão tem explicação mecânica direta, e entendê-la vale mais do que memorizar o adjetivo. Uma lesão feita de muitos espaços vasculares pequenos separados por finas paredes de tecido conjuntivo é, do ponto de vista do som, uma esponja: cada transição entre sangue e parede é uma interface refletora, e a lesão contém milhares delas por milímetro cúbico. O parênquima hepático ao redor, comparativamente uniforme, devolve muito menos eco. O resultado é uma lesão que aparece francamente mais clara — hiperecogênica — sem que isso diga nada sobre dureza ou malignidade.

Vale registrar que essa não é a única lesão hepática que sai clara no ultrassom, e o exame isolado não resolve. Uma área de esteatose focal também é hiperecogênica, porque a gordura dentro dos hepatócitos multiplica as interfaces do mesmo jeito; a diferença é que ela costuma ter formato geográfico, limites imprecisos e não desloca vasos. Metástases de tumores produtores de mucina e alguns adenomas com conteúdo lipídico também podem ser claros. É por isso que o passo seguinte não é a biópsia: é a caracterização dinâmica por tomografia, que separa essas possibilidades pelo comportamento no tempo.

#subtopico("2.2 — O padrão dinâmico que fecha o diagnóstico")

O que o subtópico anterior deixou em aberto — a natureza do nódulo — a tomografia trifásica resolve em três imagens. Na fase arterial, o contraste não preenche a lesão inteira nem contorna sua borda de maneira contínua: aparecem *bolotas* de realce intenso, descontínuas, distribuídas na periferia, com densidade tão alta quanto a da aorta na mesma imagem. Na fase portal, essas bolotas cresceram e caminharam para dentro, deixando ainda um centro não preenchido. Na fase de equilíbrio, a lesão inteira já se encheu e ficou com densidade igual ou levemente superior à do parênquima ao redor — praticamente indistinguível dele.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-04.png",
  largura: 82%,
  legenda: [As três fases lado a lado, o exame inteiro numa linha. ART: realce nodular periférico descontínuo, em bolotas separadas, tão denso quanto a aorta. PORT: as bolotas coalescem e avançam para o centro, que ainda permanece escuro. EQUIL: preenchimento completo, a lesão iguala o parênquima. Este trajeto do contraste — de fora para dentro, ao longo do tempo — é o achado que fecha o diagnóstico de hemangioma cavernoso.]
)

Cada um desses três traços tem uma causa estrutural, e é aqui que a correlação com a patologia deixa de ser metáfora. O realce em bolotas separadas existe porque a lesão não é um saco único de sangue: é um conjunto de espaços vasculares grandes e independentes, cada um alimentado por seu próprio ramo arterial na periferia — de modo que o contraste entra por várias portas ao mesmo tempo, e não por uma frente contínua. O preenchimento centrípeto, de fora para dentro, existe porque dentro desses espaços o sangue circula devagar, quase estagnado; o contraste avança por difusão e por deslocamento lento do sangue residual, e leva minutos para alcançar os lagos centrais. E a retenção tardia existe porque esses espaços não têm drenagem venosa eficiente: enquanto o parênquima normal já eliminou seu contraste e voltou ao basal, a lesão ainda o tem preso dentro de si.

#confusao-prevista(
  titulo: "Realce periférico nodular não é realce em anel",
  aluno_acha: [que qualquer lesão que acenda na borda tem o mesmo significado, e que "realce periférico" é uma descrição única],
  mecanismo: [são dois padrões opostos. No hemangioma o realce periférico é *nodular e descontínuo* — bolotas isoladas, com falhas entre elas, que depois coalescem e avançam para o centro. Na metástase e no abscesso o realce periférico é um *anel contínuo* que acende inteiro de uma vez e permanece anel, porque o que capta ali é a borda vascularizada em volta de um centro necrótico ou de pus, que nunca vai se preencher. A palavra que separa os dois é "descontínuo", e o tempo confirma: hemangioma preenche, anel não preenche.]
)

Convém também nomear o que o hemangioma *não* faz, porque é o contraste com o caso mais temido. Ele não faz washout. Uma lesão que acende forte na arterial e depois fica mais escura que o fígado nas fases tardias está perdendo contraste mais rápido que o parênquima, o que denuncia neovasos arteriais com drenagem venosa própria e rápida — a assinatura do carcinoma hepatocelular. O hemangioma faz exatamente o oposto: entra devagar e sai devagar. Diante de uma lesão hepática, portanto, a leitura decisiva não está em nenhuma fase isolada, e sim na direção do movimento do contraste ao longo das três.

#mini-resumo[Se você só lembrar de uma coisa: hemangioma entra pela borda em bolotas, caminha para o centro e retém no tardio; carcinoma hepatocelular acende inteiro cedo e lava depois. A direção do contraste no tempo é o diagnóstico.]

#subtopico("2.3 — A macroscopia e a histologia que explicam o padrão")

A peça de patologia confirma, ponto por ponto, o que a tomografia previu. Na macroscopia, a lesão aparece como uma área bem delimitada, vermelho-escura, de aspecto esponjoso, situada logo abaixo da cápsula e nitidamente demarcada do parênquima marrom ao redor. Não há cápsula fibrosa própria, não há necrose central, não há infiltração das bordas. A cor escura não é necrose: é sangue estagnado dentro dos espaços vasculares, exatamente o mesmo sangue lento que fez o contraste demorar a entrar e demorar a sair.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-08.png",
  largura: 58%,
  legenda: [Macroscopia do corte hepático. A lesão vermelho-escura, esponjosa, subcapsular e bem delimitada, contrasta com o parênquima homogêneo. A delimitação nítida sem cápsula fibrosa e a ausência de necrose central são achados macroscópicos de benignidade.]
)

A microscopia fecha o raciocínio. O que se vê são espaços vasculares dilatados, de calibres muito variados, cheios de hemácias, separados por septos finos de tecido conjuntivo fibroso. Cada espaço é revestido por uma única camada de células endoteliais achatadas, de núcleo pequeno e regular, sem estratificação, sem figuras de mitose e sem qualquer atipia. Não há hepatócitos dentro da lesão. Esse conjunto — espaços cavernosos, septos fibrosos, endotélio plano e monótono — é a definição histológica de hemangioma cavernoso.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-09.png",
  largura: 62%,
  legenda: [Histologia da lesão. Lagos vasculares de tamanhos irregulares, repletos de hemácias, separados por septos fibrosos delgados. O revestimento é uma monocamada de endotélio achatado, sem atipia nem empilhamento. Cada interface sangue-septo desta imagem é um refletor de som: é a soma de milhares delas que produziu o nódulo hiperecogênico do ultrassom.]
)

O detalhe do endotélio merece peso, porque é ele — e não a presença de vasos — que separa o benigno do maligno neste território. O angiossarcoma hepático também é feito de espaços vasculares, mas seu endotélio é atípico: núcleos grandes e hipercromáticos, células empilhadas em várias camadas, projeções papilares para dentro da luz e, sobretudo, dissecção dos cordões de hepatócitos pelas células tumorais, que crescem *por dentro* dos sinusoides preexistentes em vez de respeitar uma borda. Vaso não é sinal de benignidade nem de malignidade; quem carrega o diagnóstico é a célula que reveste o vaso.

#clinica-box("Por que não se puncionam hemangiomas",
  [A conduta diante de uma lesão com esse padrão de imagem é observação, e a razão é anatômica. Uma agulha de biópsia atravessando uma lesão feita de lagos de sangue de baixa pressão, sem trama de sustentação e sem capacidade de vasoconstrição, abre um trajeto que não se fecha sozinho — o sangramento intraperitoneal é uma complicação descrita e evitável. Some-se a isso que o rendimento diagnóstico da punção é baixo, porque o fragmento aspirado costuma trazer apenas sangue. Quando o padrão trifásico é típico, portanto, o exame de imagem *é* o diagnóstico, e a decisão correta é não fazer nada além de documentar. Hemangiomas grandes e sintomáticos, ou que rompem, são a exceção cirúrgica rara.]
)

O caso 1 termina onde o caso 2 vai começar. Repare que tudo o que foi dito até aqui pressupôs um fígado de arquitetura preservada ao redor da lesão — parênquima homogêneo, vasos no lugar, cápsula lisa. É essa normalidade de fundo que tornou o raciocínio simples. Quando o parênquima ao redor está ele próprio doente, a mesma imagem passa a significar outra coisa, e é para esse cenário que a PARTE III se desloca.

#parte-title("PARTE III — Caso 2: o fígado que endureceu")

#subtopico("3.1 — Do álcool à esteatose: quando a gordura muda a imagem")

Homem de 30 anos, dor abdominal difusa há dois dias, etilista e tabagista. A idade chama atenção: trinta anos é jovem demais para que a queixa seja lida como banal quando existe consumo crônico de álcool no histórico, porque a lesão hepática alcoólica se instala em silêncio e só aparece quando já avançou. O ultrassom mostra um fígado difusamente mais ecogênico que o córtex renal, com atenuação do feixe nas porções profundas — as camadas mais distantes do transdutor ficam apagadas — e com as paredes dos ramos portais menos visíveis do que deveriam.

Esses três achados têm uma causa comum e uma explicação física única: gordura dentro do hepatócito. Cada gotícula lipídica no citoplasma cria uma interface com o meio aquoso ao redor, e milhões delas transformam o parênquima num meio altamente refletor — daí o aumento difuso da ecogenicidade. Como parte da energia do som é devolvida logo na entrada, sobra menos para atravessar, e o feixe chega enfraquecido ao fundo — daí a atenuação posterior. E como o parênquima ficou tão claro quanto a parede fibrosa dos vasos portais, o contraste entre os dois desaparece — daí o apagamento das paredes.

A tomografia diz a mesma coisa por outra régua. Como a PARTE I estabeleceu, o fígado normal é mais denso que o baço. Na infiltração gordurosa a relação se inverte: a gordura tem atenuação muito negativa e puxa a densidade hepática para baixo, de modo que o fígado aparece mais escuro que o baço na aquisição sem contraste. É um achado quantificável — a queda é de cerca de uma unidade e meia de Hounsfield para cada ponto percentual de gordura acumulada —, e isso permite não só afirmar que há esteatose, mas estimar quanta há.

A microscopia mostra o que produziu tudo isso. Os hepatócitos contêm uma gota única e grande de lipídio que ocupa quase todo o citoplasma e empurra o núcleo contra a membrana, dando à célula um aspecto de anel de sinete — é a #termo-nota[esteatose macrovesicular][acúmulo de triglicerídeo em gota única e volumosa no hepatócito, deslocando o núcleo para a periferia; padrão do álcool, da obesidade e do diabetes]. A distribuição costuma começar na zona 3, ao redor da veia centrolobular, justamente onde o oxigênio é mais escasso e onde a enzima que metaboliza o etanol está mais concentrada.

O mecanismo é elegante e vale ser dito por inteiro, porque explica por que a gordura aparece antes de qualquer outra lesão. Oxidar etanol a acetaldeído e depois a acetato consome nicotinamida adenina dinucleotídeo em duas etapas seguidas, e o resultado é uma razão de #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzido — carreador de elétrons cuja acumulação sinaliza excesso de poder redutor na célula]) para a forma oxidada muito acima do normal dentro do hepatócito. Com excesso de poder redutor, a célula lê o ambiente como "sobra de energia": a beta-oxidação de ácidos graxos é freada, porque oxidar mais gordura é desnecessário, e a síntese de triglicerídeo é favorecida. Os ácidos graxos que chegam do tecido adiposo deixam de ser queimados, são esterificados e ficam armazenados. Nada disso é dano celular ainda — é desvio metabólico —, e essa é precisamente a razão pela qual a esteatose pura regride em semanas de abstinência.

#confusao-prevista(
  titulo: "Esteatose reverte; fibrose não",
  aluno_acha: [que "gordura no fígado" já é um estágio avançado e irreversível da doença hepática alcoólica],
  mecanismo: [a esteatose é acúmulo de triglicerídeo dentro de uma célula viva e funcionante, e desaparece quando o desvio metabólico que a causou cessa. O que não volta atrás é o passo seguinte: quando a agressão persiste, hepatócitos morrem, o infiltrado inflamatório se instala e a célula estrelada é ativada a depositar colágeno. Colágeno depositado não é reabsorvido de forma significativa. A janela terapêutica, portanto, existe — e ela se fecha entre a esteatose e a fibrose, não depois.]
)

#subtopico("3.2 — Fibrose e nódulos: a arquitetura refeita errada")

Quando a agressão não cessa, o fígado passa a fazer duas coisas ao mesmo tempo, e é a combinação delas que define a cirrose. A primeira é depositar colágeno. A segunda é regenerar hepatócitos. Isoladamente, nenhuma das duas seria catastrófica; juntas, elas reorganizam o órgão inteiro numa arquitetura nova em que o sangue não consegue mais atravessar direito.

A deposição de colágeno tem um responsável identificado. No #termo-nota[espaço de Disse][fenda estreita entre o endotélio do sinusoide e a superfície do hepatócito, por onde o plasma banha a célula diretamente] vive a #termo-nota[célula estrelada][célula perissinusoidal que em repouso armazena vitamina A e, quando ativada por lesão, se transforma em miofibroblasto produtor de colágeno], que em condições normais apenas estoca vitamina A. Diante de hepatócitos lesados, de citocinas liberadas por macrófagos residentes e de espécies reativas de oxigênio, ela muda de fenótipo: perde os grânulos de vitamina A, adquire actina de músculo liso, ganha capacidade contrátil e passa a sintetizar colágeno tipo I. Esse colágeno é depositado exatamente no espaço de Disse, e a consequência é dupla. As fenestras do endotélio sinusoidal são obliteradas — o sinusoide deixa de ser um capilar poroso e vira um capilar comum, fenômeno chamado de capilarização —, e o hepatócito perde o contato direto com o plasma de que dependia para captar e secretar. Ao mesmo tempo, o miofibroblasto contrátil enrijece e estreita o sinusoide, aumentando fisicamente a resistência à passagem do sangue.

Enquanto isso, os hepatócitos sobreviventes proliferam. Mas eles proliferam dentro de compartimentos já cercados por septos fibrosos, e crescem sem reconstruir o eixo vascular original. O resultado é o #termo-nota[nódulo de regeneração][massa arredondada de hepatócitos proliferados, cercada por septo fibroso, que não possui veia centrolobular própria nem espaço porta organizado]: uma bola de células funcionalmente vivas, mas desconectada da geometria de entrada e saída que fazia o fígado funcionar.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-18.png",
  largura: 54%,
  legenda: [Superfície externa do fígado cirrótico. Onde antes havia uma cápsula lisa e brilhante, agora há uma granulação fina e difusa — cada grânulo é a cúpula de um nódulo de regeneração empurrando a cápsula por baixo. A borda, antes fina e cortante, ficou romba.]
)

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-19.png",
  largura: 60%,
  legenda: [Corte do mesmo tipo de fígado. Nódulos amarelados de poucos milímetros, homogêneos em tamanho, separados por finas traves brancas de tecido fibroso — o padrão micronodular, característico da doença alcoólica. O amarelo denuncia que os hepatócitos dos nódulos ainda estão carregados de gordura: esteatose e cirrose coexistem.]
)

A coloração para fibras reticulares ou para colágeno torna o desenho inescapável: nódulos arredondados de parênquima delimitados por septos que se anastomosam entre si, cercando cada nódulo por inteiro. É a essa configuração — fibrose em ponte *somada* a nódulos de regeneração — que se dá o nome de cirrose. Nenhuma das duas isoladamente basta: fibrose extensa sem nodularidade é fibrose hepática; nodularidade sem fibrose ocorre na hiperplasia nodular regenerativa. O diagnóstico exige as duas.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-23.png",
  largura: 66%,
  legenda: [Coloração que evidencia a trama fibrosa. Os nódulos de hepatócitos aparecem claros, e os septos que os circundam aparecem escuros e contínuos, formando pontes entre si. Repare que nenhum nódulo tem uma veia centrolobular no meio: a arquitetura foi refeita, e refeita errada.]
)

O tamanho dos nódulos ainda carrega uma pista de origem, ainda que não conclua nada sozinho. Nódulos pequenos e uniformes, abaixo de três milímetros, formam o padrão micronodular e sugerem agressão difusa e contínua, típica do álcool. Nódulos maiores e desiguais, de vários milímetros a centímetros, formam o padrão macronodular e sugerem surtos de necrose extensa seguidos de regeneração, como nas hepatites virais. A ressalva é importante: a mesma cirrose migra de micronodular para macronodular ao longo dos anos, especialmente se o agente agressor é retirado, de modo que o padrão orienta a suspeita mas não substitui a história clínica.

#mini-resumo[Cirrose é fibrose em ponte mais nódulo de regeneração, as duas coisas ao mesmo tempo. A fibrose vem da célula estrelada ativada; o nódulo vem do hepatócito que regenera sem reconstruir o eixo vascular. Juntas, elas fecham o caminho do sangue.]

#subtopico("3.3 — Hipertensão portal: quando o sangue procura outro caminho")

Um fígado cirrótico é como uma estrada de mão única cujas pistas foram estreitadas e cheias de curvas: o mesmo volume de tráfego que antes passava sem esforço agora se acumula na entrada. Como todo o sangue do intestino, do baço e do pâncreas precisa atravessar o fígado antes de chegar à cava, o aumento da resistência intra-hepática eleva a pressão em todo o território a montante. É isso que se chama hipertensão portal — e o gradiente entre a pressão da veia porta e a da veia hepática, normalmente abaixo de cinco milímetros de mercúrio, é a medida direta do problema.

A resistência aumentada, no entanto, é apenas metade da explicação, e ignorar a outra metade leva a um entendimento incompleto do quadro. O fígado doente deixa de depurar substâncias vasodilatadoras vindas do intestino e o endotélio esplâncnico passa a produzir óxido nítrico em excesso; as arteríolas do território mesentérico se dilatam, e mais sangue entra no sistema porta por unidade de tempo. Ou seja: aumenta a resistência à saída *e* aumenta o fluxo de entrada. As duas forças se somam, e é por isso que a hipertensão portal se agrava progressivamente mesmo quando a fibrose se estabiliza.

Com a passagem obstruída, o sangue procura rotas alternativas — e as encontra, porque elas já existiam. Em vários pontos do abdome, veias do território portal fazem contato com veias do território sistêmico; são as #termo-nota[anastomoses portossistêmicas][conexões preexistentes entre veias do sistema porta e veias tributárias das cavas, normalmente colapsadas, que se dilatam quando a pressão portal sobe], normalmente irrelevantes porque colapsadas. Sob pressão, elas dilatam e passam a carregar volume para o qual não foram feitas. Na transição esofagogástrica, as veias gástricas curtas e a coronária se conectam às esofágicas, tributárias da ázigos: nascem as varizes esofágicas e gástricas. Ao redor do umbigo, a veia paraumbilical recanalizada se liga às veias da parede abdominal: nasce a cabeça de medusa. No reto, a veia hemorroidária superior se conecta às médias e inferiores: nascem as hemorroidas de causa portal. No retroperitônio, colaterais silenciosas drenam parte do fluxo sem dar sinal externo.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-27.png",
  largura: 70%,
  legenda: [Mapa das anastomoses portossistêmicas. Cada seta é um ponto onde o território portal encontra o sistêmico e onde, sob pressão, uma colateral se abre: esôfago e estômago acima, umbigo à frente, reto abaixo, retroperitônio atrás. O organismo não cria vasos novos — ele reabre caminhos que sempre estiveram lá.]
)

Na imagem, a hipertensão portal se anuncia por um conjunto de achados que aparecem juntos. O contorno hepático fica irregular e ondulado, refletindo os nódulos que empurram a cápsula por baixo. O lobo caudado e o segmento lateral esquerdo costumam hipertrofiar enquanto o lobo direito atrofia, mudando as proporções do órgão. O baço aumenta. Aparece líquido livre na cavidade. E veias tortuosas e dilatadas surgem no hilo esplênico, ao redor do esôfago distal e na parede abdominal — as colaterais, agora visíveis porque carregam volume.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-28.png",
  largura: 74%,
  legenda: [Tomografia na hipertensão portal. Em destaque, o contorno hepático delineado em verde mostra a ondulação da superfície nodular; o líquido livre contorna o fígado e se acumula nas goteiras; o baço está aumentado. À direita, o derrame pleural que acompanha os quadros com ascite volumosa.]
)

O baço aumenta por congestão, não por infiltração: ele drena pela veia esplênica diretamente para a porta, e quando a pressão sobe a jusante, o sangue se represa no parênquima esplênico. A peça macroscópica mostra um baço grande, tenso, de cor vermelho-escura homogênea ao corte, exatamente o aspecto de um órgão cheio de sangue estagnado. A consequência clínica é o hiperesplenismo: o baço congesto sequestra e destrói plaquetas e leucócitos em excesso, e o paciente cirrótico chega ao consultório com plaquetopenia sem ter nenhuma doença hematológica primária.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-30.png",
  largura: 50%,
  legenda: [Baço aumentado ao corte. Parênquima vermelho-escuro, homogêneo, túrgido — o aspecto da congestão passiva crônica. O órgão não está infiltrado por células estranhas: está represado de sangue que não consegue drenar.]
)

A ascite merece o mesmo cuidado mecanístico, porque a explicação corrente pela hipoalbuminemia isolada é insuficiente. O motor principal é a hipertensão sinusoidal: com a pressão elevada dentro do sinusoide, a produção de linfa hepática dispara e ultrapassa a capacidade de drenagem do ducto torácico, e o excesso extravasa pela cápsula direto para a cavidade peritoneal. A isso se soma a queda da pressão oncótica, porque o fígado doente sintetiza menos albumina. E há um terceiro componente, renal: a vasodilatação esplâncnica reduz o volume arterial efetivo, o rim interpreta a situação como hipovolemia e ativa o sistema renina-angiotensina-aldosterona, retendo sódio e água que alimentam o processo. Os três mecanismos operam juntos, e é por isso que o tratamento combina restrição de sódio, diurético que bloqueia a aldosterona e reposição de albumina — cada medida ataca uma das pernas.

#clinica-box("A varize que sangra",
  [A parede de uma veia esofágica não foi feita para pressão alta. Sob hipertensão portal sustentada, ela se dilata progressivamente, a parede afina à medida que o diâmetro cresce, e o vaso passa a protruir sob uma mucosa esofágica que tem poucos milímetros de espessura. Quando a tensão parietal ultrapassa o limite, a variz rompe — e como a veia está sob pressão elevada e o paciente cirrótico frequentemente tem plaquetopenia por hiperesplenismo e queda dos fatores de coagulação por falência hepática, o sangramento é volumoso e não se contém sozinho. É a hemorragia digestiva alta do cirrótico, uma das causas mais letais de descompensação. O gradiente de pressão explica também por que o rastreio endoscópico é sistemático: varizes existem a partir de cerca de dez milímetros de mercúrio de gradiente, e sangram a partir de doze — profilaxia com betabloqueador ou ligadura elástica é indicada antes do primeiro episódio, não depois dele.]
)

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-31.png",
  largura: 62%,
  legenda: [Varizes esofágicas nos dois olhares. À esquerda, o corte histológico da parede do esôfago mostra veias submucosas enormemente dilatadas e repletas de sangue, separadas da luz por uma camada delgada de mucosa. À direita, a mesma lesão vista por endoscopia: cordões azulados abaulando para dentro da luz.]
)

#subtopico("3.4 — Colestase, falência e carcinoma: os desfechos que a imagem procura")

Se a PARTE III até aqui seguiu o caminho do sangue, resta seguir o caminho da bile e o caminho da célula. Os dois fecham o quadro do fígado crônico e explicam os dois achados que restam nas peças da aula.

O primeiro é a cor. Peças de fígado cirrótico avançado frequentemente são verdes, e o verde não é necrose: é bile retida. O hepatócito capta a bilirrubina do sangue, conjuga-a com ácido glicurônico e a excreta pelo polo canalicular. Cada um desses três passos depende de transportadores de membrana e de energia, e todos os três falham num hepatócito comprimido por septos fibrosos, mal perfundido e metabolicamente exausto. A bilirrubina conjugada se acumula dentro da célula e nos canalículos, formando trombos biliares visíveis à microscopia, e impregna toda a peça. É colestase intra-hepática — nada está obstruindo a via biliar; o problema é a célula que deixou de bombear. Reconhecer isso muda a conduta: o paciente com colestase de origem hepatocelular não se beneficia de desobstrução, porque não há nada a desobstruir.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-21.png",
  largura: 56%,
  legenda: [Fígado cirrótico com colestase intensa. Os nódulos de regeneração estão impregnados de bile e assumem tonalidade esverdeada, delimitados por septos fibrosos esbranquiçados. A cor é pigmento acumulado dentro de células vivas, não tecido morto.]
)

O segundo desfecho é o mais temido, e nasce de um raciocínio simples sobre proliferação. Um fígado cirrótico é um fígado em regeneração permanente: hepatócitos entram em ciclo celular continuamente, ano após ano, num ambiente carregado de espécies reativas de oxigênio e de citocinas inflamatórias. Cada divisão é uma oportunidade de mutação que não é corrigida, e mutações se acumulam. É por isso que a cirrose, qualquer que seja a causa, é o fator de risco dominante para o #sigla("CHC", [carcinoma hepatocelular — tumor maligno primário derivado do hepatócito, que surge tipicamente em fígado cirrótico]). O nódulo de regeneração é o ponto de partida de uma sequência que passa por nódulo displásico de baixo grau, depois de alto grau, e termina em carcinoma.

#figura-nebli(
  "/figuras/correlacao-radio-pato-2/slide-24.png",
  largura: 62%,
  legenda: [Carcinoma hepatocelular sobre fígado cirrótico. Acima, a superfície de corte de um tumor volumoso, heterogêneo, com áreas de necrose e hemorragia. Abaixo, um nódulo verde bem delimitado destacando-se do parênquima cirrótico amarelado — a cor denuncia que as células tumorais ainda produzem bile, marca de diferenciação hepatocelular.]
)

O que torna esse tumor reconhecível por imagem é uma mudança de suprimento sanguíneo que acompanha a transformação. O nódulo de regeneração é irrigado, como o parênquima, sobretudo pela porta. À medida que evolui para displasia e depois para carcinoma, os espaços porta desaparecem de dentro dele e neovasos arteriais tomam o lugar — o nódulo passa a ser alimentado quase só por artéria. A tradução na tomografia trifásica é direta e é aquela que a PARTE I anunciou: realce intenso na fase arterial, quando só o sangue arterial chegou, e washout nas fases portal e tardia, quando o parênquima ao redor recebe sua onda portal e fica mais denso que o tumor. Em paciente com cirrose conhecida, esse par de achados num nódulo maior que um centímetro é considerado diagnóstico, e a punção é dispensada.

#atencao-box("Nódulo de regeneração e carcinoma não se distinguem por serem nódulos",
  [Todo fígado cirrótico é feito de nódulos, e por isso "achei um nódulo" não significa nada por si só — o que separa o benigno do maligno é o comportamento vascular e o tamanho ao longo do tempo. Nódulo de regeneração mantém suprimento portal, não realça na fase arterial e não cresce. Carcinoma trocou o suprimento por arterial, acende cedo e lava tardiamente, e cresce entre os exames. Tratar todo nódulo em fígado cirrótico como regeneração perde um tumor curável; tratar todo nódulo como tumor leva a intervenções desnecessárias num paciente com reserva hepática limitada. O que decide é a dinâmica do contraste e a comparação com o exame anterior.]
)

#clinica-box("Por que o cirrótico faz ultrassom a cada seis meses",
  [O rastreio de carcinoma hepatocelular no paciente cirrótico é semestral e usa ultrassom, e a escolha tem lógica dupla. Primeiro, a biologia: o tempo médio de duplicação do tumor permite que um nódulo detectável apareça e ainda esteja em fase tratável dentro de um intervalo de seis meses. Segundo, a economia do método: o ultrassom não usa radiação ionizante, não usa contraste nefrotóxico, custa pouco e pode ser repetido indefinidamente — atributos que importam quando o exame será feito duas vezes ao ano pelo resto da vida do paciente. A tomografia e a ressonância não competem com o ultrassom no rastreio; elas entram depois, para caracterizar o nódulo que o rastreio encontrou. Cada método ocupa o lugar em que sua física rende mais.]
)

#conclusao-box[
Uma única ideia atravessa este resumo do começo ao fim: *a imagem é a sombra da arquitetura*. Nada do que o ultrassom mostra é arbitrário, nada do que a tomografia mede é convenção — cada achado é a consequência física de um arranjo real de células, vasos e matriz que o patologista poderia mostrar num corte.

O mecanismo nuclear que sustenta essa correspondência no fígado é a dupla aferência somada à unidade de saída. É porque três quartos do sangue chegam pela porta e um quarto pela artéria que existem fases de contraste distintas, e é a leitura dessas fases que distingue uma lesão que enche devagar de fora para dentro e retém — o hemangioma, com seus lagos vasculares de fluxo lento — de uma lesão que acende cedo e lava — o carcinoma, com seus neovasos arteriais. E é porque existe uma única via de saída, atravessando obrigatoriamente o parênquima, que a fibrose e os nódulos de regeneração da cirrose se convertem em hipertensão portal: aumentam a resistência à passagem, somam-se ao hiperfluxo esplâncnico e empurram o sangue para anastomoses que sempre existiram, produzindo varizes, cabeça de medusa, hemorroidas, baço congesto e ascite.

A clínica que percorremos não é ilustração: é o próprio mecanismo aplicado. A paciente de 20 anos não foi puncionada porque a dinâmica do contraste já dizia que seus lagos vasculares eram benignos, e porque uma agulha em vasos de baixa pressão sangra. O paciente de 30 anos tem gordura reversível e fibrose irreversível ao mesmo tempo, e a janela terapêutica está exatamente na fronteira entre as duas. A variz do cirrótico sangra por tensão parietal em veia dilatada num paciente que perdeu plaquetas para o baço congesto e fatores de coagulação para o hepatócito falido — três mecanismos deste resumo convergindo num único evento.

O passo seguinte estende esse raciocínio para os outros órgãos do andar superior do abdome, onde a lógica se repete com física própria: as vias biliares, onde o problema é obstrução e a régua é o calibre do ducto; e o pâncreas, onde a inflamação e a neoplasia disputam a mesma imagem. O hábito construído aqui — ver um achado e perguntar que alteração de tecido o produziu — é transferível inteiro.
]
