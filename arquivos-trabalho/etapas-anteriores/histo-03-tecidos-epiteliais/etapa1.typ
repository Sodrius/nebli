#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Coloque qualquer órgão sob o microscópio e a primeira coisa que aparece é uma fileira de células coladas umas nas outras, com núcleos alinhados e uma linha rosa-magenta logo abaixo. Esse arranjo se repete por todo lado — revestindo o intestino, a traqueia, a bexiga, a pele, os túbulos do rim — e ele tem um nome: tecido epitelial. É um dos quatro tecidos básicos que constroem todos os órgãos do corpo, e provavelmente o mais visualmente reconhecível na lâmina.

  Este resumo é sobre como o epitélio funciona e, principalmente, sobre como reconhecer cada subtipo dele em uma lâmina histológica. Em uma frase: o epitélio é a célula em comunidade densa, com lado de cima diferente do de baixo, apoiada num tapete molecular chamado lâmina basal, e sempre cumprindo uma de cinco funções — revestir, proteger, absorver, secretar ou perceber estímulo. Conhecer o epitélio começa por entender o que torna uma célula "epitelial", segue por aprender o algoritmo de classificação dos subtipos de revestimento — onde o foco prático em lâmina é maior — e termina nas glândulas, que são epitélios profissionalizados em secretar.
]

#parte-title("PARTE I — O que torna um epitélio um epitélio", primeira: true)

#subtopico("1.1 — Quatro tecidos básicos e o lugar do epitélio na taxonomia")

O corpo inteiro, com seus muitos órgãos e funções, é construído de apenas quatro tipos de tecido. Tecido epitelial é um deles; os outros três são o tecido conjuntivo (cobre cartilagem, osso, gordura, sangue, conjuntivo propriamente dito), o tecido muscular (esquelético, cardíaco, liso) e o tecido nervoso. Essa redução do biológico a quatro categorias parece arbitrária, e em parte é — mas a divisão sobrevive porque cada categoria responde a uma pergunta diferente: o epitélio responde a "como o corpo separa um compartimento do outro", o conjuntivo a "como o corpo dá sustentação e enche o espaço entre estruturas", o muscular a "como o corpo se move" e o nervoso a "como o corpo conduz informação".

A regra de ouro para reconhecer epitélio em uma lâmina é olhar a relação entre célula e matriz. No epitélio, as células estão grudadas umas nas outras com pouquíssima matriz entre elas — quase parece que a lâmina foi pintada de fileiras de núcleos. No conjuntivo, ao contrário, a célula vive cercada por uma matriz extracelular abundante que ela mesma produziu (colágeno, fibras elásticas, substância fundamental), e por isso fibroblastos aparecem espalhados em meio a estrias rosa. Essa diferença visual é o que permite, em segundos, dizer "aqui é epitélio, ali é conjuntivo".

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-04.png",
  largura: 55%,
  legenda: [Os quatro tecidos básicos. O epitélio é o que reveste superfícies e cavidades; o conjuntivo preenche e sustenta; o muscular contrai; o nervoso conduz. Reconhecer um tecido começa por perguntar a qual dessas quatro categorias ele pertence.])

#mini-resumo[Epitélio: células justapostas com pouca matriz, sempre apoiadas em lâmina basal, com função de revestir/proteger/absorver/secretar/perceber.]

#subtopico("1.2 — Origem nas três folhas embrionárias: por que a folha não define o tecido")

Entre a segunda e a terceira semana do desenvolvimento, o embrião humano se organiza em três folhas: ectoderma (camada externa), mesoderma (camada do meio) e endoderma (camada interna). Cada folha vai gerar tecidos específicos depois — mas, contra a intuição inicial, todas as três geram epitélio em algum lugar do corpo. A epiderme da pele e a córnea vêm de ectoderma; o revestimento do estômago, do intestino e do trato respiratório vêm de endoderma; o endotélio dos vasos, os túbulos renais e o mesotélio das serosas vêm de mesoderma.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-07.png",
  largura: 60%,
  legenda: [Origem embriológica dos epitélios. As três folhas (ecto, meso e endoderma) geram epitélios distintos. O ponto importante: não é a folha que define o tecido como epitelial — é a organização tecidual final.])

Esse é um ponto que pega muito aluno: pensar que mesoderma "só vira conjuntivo" e que epitélio "só vem de ecto e endoderma". Não é assim. O que define epitélio NÃO é a folha de origem — é o que aquelas células viram depois de organizadas: se ficarem agrupadas, justapostas, em superfície ou cavidade, com lâmina basal embaixo, são epitélio, venha de onde vier.

#subtopico("1.3 — Polaridade apico-basal: a célula com lado de cima diferente do de baixo")

Quase nenhuma célula epitelial é simétrica. A face voltada para o lúmen (a "luz" do tubo — interior do intestino, da traqueia, do túbulo renal) chama-se domínio apical. A face oposta, encostada na lâmina basal, chama-se domínio basal. As laterais, que tocam as células vizinhas, são os domínios laterais. E o ponto pedagógico importante é que essas três regiões da mesma célula têm composições moleculares diferentes — proteínas de transporte, receptores e organelas estão distribuídos de forma assimétrica.

Dois exemplos tornam isso concreto. No enterócito do intestino delgado, o domínio apical concentra microvilos cheios de transportadores de glicose do tipo #sigla("SGLT1", [sodium-glucose linked transporter 1 — cotransporta sódio e glicose do lúmen para dentro da célula]), enquanto o domínio basal tem o transportador #sigla("GLUT2", [glucose transporter 2 — facilita a saída da glicose da célula para o sangue]). A glicose entra por um lado, sai pelo outro. No túbulo renal, a bomba sódio-potássio fica restrita ao domínio basolateral, e isso é o que gera o gradiente que move toda a reabsorção. A polaridade não é decoração — ela é a base do transporte direcional epitelial.

Para que essa separação molecular se mantenha, a célula precisa de uma barreira que impeça as proteínas de andarem livremente entre o apical e o basolateral — e essa barreira é a zônula de oclusão, que vamos ver agora.

#subtopico("1.4 — Junções celulares: rebites, parafusos e portinholas")

As células epiteliais não estão simplesmente encostadas — elas estão amarradas umas nas outras por um conjunto de junções com funções complementares. Pense em uma analogia construtiva: para montar uma parede de blocos justapostos é preciso vedar (impedir vazamento por entre os blocos), colar mecanicamente (impedir que os blocos deslizem) e abrir passagens para fios passarem (comunicação). O epitélio resolve cada um desses três problemas com um tipo de junção diferente.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-21.png",
  largura: 60%,
  legenda: [As junções formam um complexo na região apical lateral. De cima para baixo: zônula de oclusão (vedação), zônula de adesão (colagem mecânica anelar), desmossomos (rebites pontuais). Mais abaixo, hemidesmossomos ancoram a célula à lâmina basal.])

A #termo-nota[zônula de oclusão][junção apical em forma de cinto, feita de claudinas e ocludinas, que veda o espaço paracelular e mantém a polaridade] é a vedação — uma faixa contínua em volta do ápice da célula, feita das proteínas claudina e ocludina, que efetivamente "costura" a membrana de uma célula na outra e impede que líquido escape pelo espaço entre elas (a chamada via paracelular). Ela também segura a polaridade: como funciona como cerca, impede que as proteínas do domínio apical migrem para o basolateral. Diferentes claudinas têm permeabilidades diferentes — no túbulo proximal do rim, a claudina-2 cria poros seletivos para sódio; no intestino, claudinas mais "apertadas" bloqueiam quase tudo.

Mais abaixo da zônula de oclusão vem a zônula de adesão — outro cinto, mas agora de função mecânica. Aqui as proteínas envolvidas são #termo-nota[caderinas clássicas][família de proteínas de adesão Ca²⁺-dependentes que conectam citoesqueleto de actina de células vizinhas — E-caderina é a forma epitelial], que dependem de Ca²⁺ para funcionar e que conectam o citoesqueleto de actina das duas células. Se você remover Ca²⁺ do meio (com EDTA, por exemplo), o epitélio se desfaz — é uma demonstração clássica.

Mais abaixo ainda aparecem os desmossomos. Eles também usam caderinas (desmogleínas e desmocolinas), mas agora ancoram filamentos intermediários — queratinas, principalmente — e funcionam como rebites pontuais, distribuídos em pequenos pontos ao longo das laterais. São especialmente abundantes onde o epitélio sofre estresse mecânico (epiderme, esôfago).

#confusao-prevista(
  titulo: "Zônula de oclusão NÃO é junção mecânica",
  aluno_acha: [Como ela está no topo e tem o nome "oclusão", parece que segura mecanicamente as células — afinal, fecha o espaço lateral.],
  mecanismo: [O que segura mecanicamente são a zônula de adesão (caderinas + actina) e os desmossomos (caderinas + filamentos intermediários). A zônula de oclusão veda paracelularmente e mantém polaridade — função de barreira, não de cola. Se você dissociar epitélio com Ca²⁺ baixo, os desmossomos rompem e o tecido cai apesar de a oclusão estar lá.]
)

Há ainda dois tipos extras de junção. As junções comunicantes (gap junctions) são canais formados por hexâmeros de conexinas que conectam o citoplasma de células vizinhas — passam íons e moléculas pequenas (< 1 kDa), permitindo comunicação química direta sem precisar de receptor de membrana. E na face basal, os hemidesmossomos — atenção: "hemi" porque é meio desmossomo, com um único lado celular — ancoram a célula à lâmina basal usando integrinas (que são Ca²⁺-independentes, o que distingue dos verdadeiros desmossomos).

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-30.png",
  largura: 55%,
  legenda: [#emph[Clostridium perfringens] ataca diretamente a zônula de oclusão: a enterotoxina se liga a claudinas e destrói o vedamento paracelular dos enterócitos. Líquido escapa do interstício para o lúmen — daí a diarreia aquosa intensa. A figura amarra mecanismo molecular (claudina rompida) à doença real (intoxicação alimentar).])

#clinica-box("Clostridium perfringens e a barreira intestinal")[
  Uma forma de entender o quanto a vedação paracelular importa é olhar o que acontece quando ela falha. #emph[Clostridium perfringens] produz uma enterotoxina (CPE) que se liga especificamente a claudinas — destrói a zônula de oclusão dos enterócitos. O resultado é que a barreira da via paracelular cai, líquido extravasa do espaço intersticial para o lúmen do intestino, e o paciente apresenta diarreia aquosa intensa. #emph[Helicobacter pylori] faz algo parecido no estômago: a proteína bacteriana CagA se liga a domínios extracelulares da zônula de oclusão e induz reorganização do citoesqueleto, contribuindo para inflamação crônica e risco de adenocarcinoma gástrico. Ambos exemplos mostram que a junção apical não é detalhe — é literalmente a fronteira que mantém o "fora" fora.
]

#subtopico("1.5 — Lâmina basal e membrana basal: o tapete onde o epitélio se senta")

Toda célula epitelial repousa sobre uma estrutura de matriz extracelular muito fina e contínua, chamada #termo-nota[lâmina basal][folheto fino (50-100 nm) de colágeno IV, lamininas, entactina e proteoglicanos, secretado pelo próprio epitélio, que ancora as células e separa o tecido epitelial do conjuntivo subjacente]. Ela é tão fina que não é visível ao microscópio óptico comum — só aparece em #sigla("ME", [microscopia eletrônica]). A composição molecular é específica: a rede principal é feita de colágeno tipo IV (que NÃO forma fibras grossas, mas uma malha em folha), lamininas (que dão pontos de ancoragem), entactina/nidogênio e proteoglicanos de heparan sulfato.

Na face epitelial da lâmina basal, os hemidesmossomos das células se conectam a integrinas que, por sua vez, agarram lamininas. Na face conjuntiva, ela se ancora ao tecido subjacente por fibrilas de colágeno tipo VII, que se estendem como pequenos ganchos. Funcionalmente, a lâmina basal cumpre quatro papéis: estrutural (sustenta o epitélio), de filtro molecular (controla o que atravessa do conjuntivo para o epitélio e vice-versa), de pista para migração (durante reparo, células migram sobre ela), e de regulação metabólica (sinaliza para o epitélio sobre estado da matriz).

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-36.png",
  largura: 60%,
  legenda: [Quando juntamos a lâmina basal do epitélio com as fibras reticulares (colágeno III) do conjuntivo logo abaixo, formamos a membrana basal — essa sim, visível ao microscópio óptico com a coloração #sigla("PAS", [periodic acid-Schiff — reação histoquímica que marca polissacarídeos em rosa-magenta]).])

Aqui entra uma distinção que confunde com muita frequência: #termo-nota[lâmina basal × membrana basal][a lâmina basal é a estrutura molecular fina e contínua só visível ao ME; quando somada às fibras reticulares de colágeno III do conjuntivo subjacente, forma a membrana basal — esta visível ao microscópio óptico com PAS]. Em outras palavras: toda membrana basal contém lâmina basal, mas o que você vê em rosa-magenta na lâmina de PAS é a membrana basal completa. A coloração PAS marca polissacarídeos — e tanto as glicoproteínas da lâmina basal quanto os proteoglicanos das fibras reticulares são polissacarídeos, daí a reação positiva.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-39.png",
  largura: 70%,
  legenda: [Glândulas intestinais do cólon em #sigla("HE", [hematoxilina-eosina — coloração histológica de rotina, em que núcleos ficam arroxeados e citoplasma/matriz ficam em tons de rosa]) (esquerda) e em PAS (direita). Em HE quase não se vê a membrana basal; em PAS, ela aparece como linha rosa-magenta nítida contornando cada glândula. PAS é o método de escolha para visualizar membranas basais ao microscópio óptico.])

#mini-resumo[Lâmina basal = só ao ME (colágeno IV + lamininas). Membrana basal = lâmina basal + fibras reticulares do conjuntivo, visível ao MO com PAS.]

#subtopico("1.6 — Avascularidade: por que vaso sanguíneo não entra no epitélio")

Quase nenhum epitélio tem vasos sanguíneos atravessando-o — uma exceção rara é a estria vascular do ouvido interno, lembrada justamente por ser exceção. A regra geral, portanto, é avascularidade: o vaso fica no conjuntivo, e o epitélio recebe oxigênio e nutrientes por difusão através da lâmina basal. Isso faz sentido pela própria arquitetura do tecido. Um capilar precisa de espaço de matriz e trajeto próprio; o epitélio, ao contrário, é uma parede de células justapostas, com pouco espaço entre uma célula e outra.

Essa restrição tem consequência prática: como a difusão limita até onde o nutriente chega, o epitélio não pode ser muito espesso. Mesmo em epitélios estratificados grossos como a epiderme, as camadas mais superficiais já estão em processo de morte celular — porque longe demais do capilar para sobreviver. Sempre que pensar "como esse epitélio se alimenta?", a resposta é "via difusão a partir do conjuntivo abaixo da lâmina basal" — e isso explica por que o conjuntivo subjacente, em todos os epitélios, é ricamente vascularizado.

Avascularidade ajuda a entender outro ponto, mas não é a única causa dele: muitos epitélios renovam células continuamente porque vivem em superfícies de atrito, secreção, absorção e descamação. As células-tronco ficam na região basal, encostadas na lâmina basal e próximas da fonte de nutrientes; quando se dividem, empurram as filhas para a superfície. Na epiderme queratinizada, esse caminho termina em morte celular e formação do estrato córneo. Em mucosas, muitas células descamam ainda nucleadas. O princípio é o mesmo — reposição constante da barreira — mas o destino final muda conforme o epitélio. Esse ciclo dura cerca de 5 dias no intestino, 28 dias na epiderme, dias a semanas em outros epitélios; por isso carcinomas são tão frequentes: muita divisão significa muitas oportunidades de acumular mutações.

#parte-title("PARTE II — Atlas de identificação: nomear o epitélio que está na lâmina")

#subtopico("2.1 — O algoritmo de classificação: número de camadas × forma da superficial × especialização apical")

Cada epitélio de revestimento ganha um nome composto por três peças, na ordem: (1) número de camadas, (2) forma da camada mais superficial, e (3) presença de especialização apical (cílios, queratina), quando relevante. "Epitélio simples colunar ciliado" significa uma camada (simples), com células em forma de coluna na superfície (colunar = cilíndrico), com cílios na borda apical (ciliado). "Epitélio estratificado pavimentoso queratinizado" significa muitas camadas, com células achatadas (pavimentosas) na superfície, com queratina nas camadas mais superiores. Decorou a regra, decorou todos os nomes.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-69.png",
  largura: 75%,
  legenda: [Os três epitélios simples lado a lado: pavimentoso (núcleo achatado paralelo à basal), cúbico (núcleo redondo central, altura ≈ largura) e cilíndrico (núcleo oval na base, célula alta). A forma e a posição do núcleo são as pistas mais rápidas em lâmina.])

Repare uma coisa: o nome considera a camada SUPERFICIAL, não a basal. Isso importa porque em epitélios estratificados a camada basal costuma ser cúbica ou cilíndrica em todos eles — o que muda é a superficial. O esôfago tem epitélio estratificado pavimentoso porque a camada superior é achatada; a epiderme é estratificado pavimentoso queratinizado porque acima da camada achatada ainda há queratina morta.

E há um conselho prático para olhar lâmina: comece sempre buscando a lâmina basal. Onde ela está, o epitélio termina. Quantas camadas de núcleo você conta acima dela? Uma só = simples. Várias = estratificado. Várias com TODAS encostando na basal (vai conferir!) = pseudoestratificado. Tipos especiais (transição/urotélio) ficam para o fim. Depois disso, olhe a forma das células superficiais. Pronto, nomeou.

#subtopico("2.2 — Simples pavimentoso: a linha fininha de núcleos achatados")

Pavimentoso vem de "pavimento" — chão liso. As células são tão achatadas que parecem ladrilhos vistos de cima. Em corte transversal aparecem como uma linha fininha contínua, e o núcleo, também achatado (oblongo, paralelo à lâmina basal), faz uma pequena saliência onde está. Para identificar em lâmina: procure uma linha celular de espessura tão pequena que mal se distingue do conjuntivo abaixo, com núcleos isolados, achatados, espaçados ao longo dela.

Onde encontrar: revestindo todo o sistema vascular (chama-se endotélio aí), revestindo as cavidades pleural, peritoneal e pericárdica (chama-se mesotélio nesse caso), revestindo a cápsula de Bowman do rim, e formando os alvéolos pulmonares (pneumócitos tipo I). A função, em todos esses locais, é a mesma: maximizar difusão de gás ou líquido com espessura mínima de barreira. Endotélio precisa ser fino para o O₂ atravessar do alvéolo ao sangue; mesotélio precisa ser fino para o líquido seroso lubrificar.

#confusao-prevista(
  titulo: "Endotélio É epitélio (e mesotélio também)",
  aluno_acha: [Endotélio "soa" como tecido vascular, mesotélio como serosa — então não devem ser epitélio, devem ser outra coisa.],
  mecanismo: [Endotélio = epitélio simples pavimentoso especializado dos vasos sanguíneos e linfáticos. Mesotélio = epitélio simples pavimentoso (às vezes cúbico) das serosas (pleura, peritônio, pericárdio). Nomes próprios herdados por localização anatômica, mas ambos são histologicamente epitélio simples pavimentoso, com lâmina basal, justaposição e polaridade.]
)

#subtopico("2.3 — Simples cúbico: núcleo redondo e centralizado")

Aqui a célula tem altura aproximadamente igual à largura, formando um cubo (na verdade, em corte é um quadrado). O núcleo é redondo e fica posicionado no centro da célula — uma pista visual rápida. Em lâmina, o epitélio cúbico aparece como uma fileira de "quadradinhos" com bolinhas centrais.

Onde encontrar: nos túbulos renais (proximal e distal), revestindo os folículos da tireoide (onde o coloide armazenado dentro da esfera é o reservatório de tireoglobulina), na superfície do ovário, em pequenos ductos de glândulas exócrinas. Cada um desses locais usa o cúbico para combinar barreira leve com transporte ativo — o túbulo renal absorve íons e água, a tireoide reabsorve coloide, o ducto conduz secreção sem absorvê-la em excesso.

#subtopico("2.4 — Simples cilíndrico (colunar): núcleo oval na base, célula alta como pilha de tijolos verticais")

Pense em tijolos colocados em pé, com altura maior que largura. Cada célula é alta e estreita, com núcleo ovalado posicionado na metade inferior — quase encostado na lâmina basal. Em lâmina, isso forma uma "muralha" de células altas com uma linha bem definida de núcleos próxima à base.

Onde encontrar: revestindo o intestino delgado e o cólon (onde há também caliciformes intercaladas, que veremos na PARTE 3), revestindo a vesícula biliar (que concentra a bile reabsorvendo água), revestindo o estômago (com células secretoras de muco). A função varia — absorção, secreção, concentração — mas a forma alta e estreita serve a todos esses casos porque oferece muito espaço apical para microvilos (no caso absortivo) ou para vesículas secretoras (no caso secretor).

Uma variante específica é o simples colunar ciliado, que aparece na tuba uterina (deslocando o oócito em direção ao útero) e parte do endométrio em fase apropriada do ciclo. Sempre que você vir cílios sobre célula alta com núcleo basal e camada única, é colunar ciliado.

#subtopico("2.5 — Pseudoestratificado: o impostor que parece estratificado mas não é")

Esse é o subtipo que mais confunde aluno em lâmina — e por isso vale insistir no critério diagnóstico. O pseudoestratificado tem aparência de várias camadas porque os núcleos estão posicionados em alturas diferentes na altura da célula, o que dá ilusão de estratificação. Mas é uma ilusão: todas as células encostam na lâmina basal. Algumas são altas e chegam até a superfície apical (e levam o núcleo bem alto); outras são baixas, ficam só na metade inferior do epitélio (e levam o núcleo baixo). Como todas tocam a base e a aparência das alturas dos núcleos varia, parece haver mais de uma camada — daí "pseudo".

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-75.png",
  largura: 70%,
  legenda: [Pseudoestratificado ciliado da traqueia. Todas as células encostam na lâmina basal — incluindo as células mais baixas, cujos núcleos ficam próximos à base. O efeito de estratificação vem só do escalonamento dos núcleos. Cílios na superfície apical varrem muco para faringe.])

O critério operacional para distinguir pseudo de estratificado verdadeiro em lâmina: foque o microscópio no plano da lâmina basal e siga uma célula bem corada do ápice ao fundo. Se ela atravessa o epitélio inteiro até tocar a basal, é pseudo. Se só a camada mais profunda toca a basal e as outras camadas vivem sobre elas, é estratificado verdadeiro.

Na lâmina você reconhece por: (1) núcleos em alturas escalonadas (impressão de várias camadas), (2) confirmação de que TODA célula encosta na lâmina basal (basta seguir uma célula bem corada do ápice à base), e (3) cílios móveis ou estereocílios na superfície apical quando presentes.

Onde encontrar pseudoestratificado: traqueia e brônquios grandes, como epitélio colunar ciliado com caliciformes, varrendo muco para cima; e ducto do epidídimo, com estereocílios longos aumentando a superfície de reabsorção. Vale separar esse exemplo dos ductos eferentes: eles também fazem parte da via espermática, mas misturam células ciliadas e células absortivas, então não são o exemplo clássico de "pseudoestratificado com estereocílios". É um epitélio caro de manter porque cada célula precisa equilibrar metabolismo com ancoragem basal, mas funciona quando o objetivo é modificar ou mover material na superfície sem montar várias camadas verdadeiras.

#confusao-prevista(
  titulo: "Esôfago NÃO é pseudoestratificado",
  aluno_acha: [Como o esôfago tem aparência de várias camadas e está num tubo, o aluno tende a chutar pseudoestratificado por analogia com traqueia.],
  mecanismo: [Esôfago é estratificado pavimentoso NÃO queratinizado. As células superficiais são achatadas, claramente diferentes das basais (cúbicas ou cilíndricas), e há várias camadas verdadeiras onde só a basal toca a lâmina basal. Pseudoestratificado típico está na traqueia, brônquios e ductos do trato reprodutor masculino — não em esôfago.]
)

#subtopico("2.6 — Estratificado pavimentoso: queratinizado (epiderme) × não queratinizado (esôfago, vagina)")

Em estratificado pavimentoso há várias camadas verdadeiras de células sobrepostas — só a camada basal toca a lâmina basal. A camada basal tem células cúbicas/cilíndricas com alta atividade mitótica (são as células-tronco do epitélio); à medida que as filhas são empurradas para cima, elas vão achatando, perdendo organelas e aumentando o conteúdo de queratina. Quando atingem a superfície, são pavimentosas.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-73.png",
  largura: 70%,
  legenda: [Estratificado pavimentoso em três versões: não queratinizado (esôfago), queratinizado (epiderme), e variantes estratificados cúbico/cilíndrico (raros). Note como no queratinizado as camadas superiores perdem o núcleo e formam estrato córneo anucleado.])

A divisão queratinizado × não queratinizado depende de onde o epitélio mora. Onde há ar seco encostando na superfície — pele exposta — a camada superficial passa por queratinização completa: as células superficiais morrem, perdem núcleo e organelas, e ficam recheadas de filamentos de queratina compactados. O resultado é o estrato córneo, uma "casca" impermeável que reduz perda de água e protege contra atrito. Onde há ambiente úmido — esôfago, mucosa oral (exceto gengiva), vagina — as células superficiais permanecem vivas, com núcleo, e o epitélio é não queratinizado.

Aqui mora outra armadilha: pense que toda célula epitelial expressa queratinas (filamentos intermediários), independente de qualquer "queratinização" visível. A diferença é que no esôfago e vagina a queratina permanece dispersa pelo citoplasma normal; na epiderme da pele, ela é compactada nas camadas superiores em massa morta. Quando falamos de "epitélio queratinizado", queremos dizer esse processo completo terminando em estrato córneo, não simples presença de queratina como molécula.

Na lâmina você reconhece por: (1) várias camadas verdadeiras com só a basal tocando a lâmina basal, (2) gradiente de forma — basal cúbica/cilíndrica que vai achatando até virar pavimentosa na superfície, e (3) presença (queratinizado) ou ausência (não queratinizado) de estrato córneo anucleado eosinofílico no topo.

#mini-resumo[Estratificado pavimentoso = várias camadas, só basal toca a lâmina basal. Queratinizado = pele exposta, com estrato córneo morto. Não queratinizado = mucosas úmidas (esôfago, vagina, cavidade oral exceto gengiva).]

#subtopico("2.7 — Transição (urotélio): muda de cara quando você não está olhando")

O nome "transição" tem origem histórica e induz erro: parece sugerir que o epitélio transita entre dois tipos diferentes. Não — o epitélio é o mesmo, mas muda de configuração conforme o órgão (a bexiga, principalmente) enche ou esvazia. O nome mais limpo hoje é urotélio; na nomenclatura clássica, ele continua sendo epitélio estratificado de transição. O ponto que não pode escapar é justamente esse: ele é distensível, mas não é pseudoestratificado. Há várias camadas verdadeiras, e a mudança de aparência vem do estiramento das células e das dobras da mucosa, não de uma ilusão produzida por núcleos em alturas diferentes.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-76.png",
  largura: 60%,
  legenda: [Urotélio em duas configurações. Bexiga vazia (à esquerda): epitélio espesso, com várias camadas aparentes e células superficiais em cúpula. Bexiga cheia (à direita): epitélio estirado, células superficiais achatadas. Mesmo tecido, formas diferentes.])

Em lâmina, urotélio se reconhece por duas pistas: (1) camada superficial com células grandes, em forma de cúpula, voltadas para o lúmen — chamadas células guarda-chuva (umbrella cells); (2) o epitélio é geralmente espesso quando o órgão está vazio (5-6 camadas aparentes) e fino quando está cheio (2-3 camadas aparentes). As células guarda-chuva têm uma membrana apical especializada com placas de uroplaquina que tornam a superfície impermeável à urina — proteção contra a osmolaridade variável e contra os íons agressivos do filtrado urinário.

Onde encontrar: cálices renais, pelve renal, ureteres, bexiga, parte proximal da uretra. Toda via urinária acima da uretra distal é urotélio.

Na lâmina você reconhece por: (1) células superficiais grandes em forma de cúpula (guarda-chuva) voltadas ao lúmen, (2) espessura variável (5–6 camadas no órgão vazio, 2–3 no estirado) e (3) localização — basta o corte estar em qualquer ponto da via urinária acima da uretra distal.

#subtopico("2.8 — Especializações apicais: microvilos, estereocílios, cílios móveis, cílio primário")

A última camada do nome do epitélio às vezes é uma especialização apical. Há quatro formas principais, com mecanismos e funções bem distintos.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-49.png",
  largura: 55%,
  legenda: [Microvilos vistos em corte. Cada microvilo é uma projeção digitiforme sustentada por um feixe central de filamentos de actina. Não batem — são imóveis. Função: aumentar área apical para absorção.])

#termo-nota[microvilos][projeções digitiformes da superfície apical, sustentadas por feixes de actina, imóveis, abundantes (centenas por célula), com função absortiva] são curtos (~1 µm) e densos. Sustentados internamente por feixes paralelos de actina, são imóveis — não batem. A função é multiplicar a área apical para absorção. No enterócito do intestino delgado, a parede de microvilos é tão densa que aparece em lâmina como uma faixa rosa contínua chamada borda em escova. Em túbulo proximal do rim, o mesmo padrão tem o mesmo nome.

#termo-nota[estereocílios][microvilos extremamente longos e imóveis, sustentados por actina, presentes em epidídimo e em células sensoriais auditivas — apesar do nome "cílios", são microvilos] são microvilos longos demais. O nome "estereo-cílios" induz erro: parecem cílios pelo comprimento (até 10× mais longos que microvilos normais), mas a estrutura interna é actina, igual a microvilos. Aparecem só em duas localizações: ductos do epidídimo (onde aumentam a área para reabsorção de fluido testicular) e células sensoriais auditivas da cóclea (onde detectam vibração mecânica). Não batem.

Cílios móveis são fundamentalmente diferentes. São longos (~5-10 µm), sustentados por um esqueleto de #termo-nota[axonema 9+2][arranjo de microtúbulos do cílio móvel — 9 pares periféricos de microtúbulos em volta de 1 par central, com braços de dineína que geram movimento], que tem braços de dineína consumindo ATP para gerar movimento. Cada célula apresenta centenas de cílios, e o conjunto bate em ondas coordenadas para mover muco e secreções pela superfície epitelial. Aparecem em traqueia (batendo muco e partículas inaladas para cima, em direção à faringe), em tuba uterina (carregando o oócito em direção ao útero) e em ventrículos cerebrais (movendo líquor).

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-57.png",
  largura: 60%,
  legenda: [Cílios móveis emergindo da superfície apical, ancorados em corpúsculos basais. O axonema 9+2 (9 pares de microtúbulos periféricos + 1 par central) com braços de dineína é o motor que consome ATP para gerar a batida ciliar.])

E há o cílio primário: um único cílio por célula, imóvel, com estrutura 9+0 — sem o par central de microtúbulos e sem dineína funcional, daí não bate. Sua função é sensorial: detectar fluxo de fluido (mecanossensorial), composição química (quimiossensorial) ou osmolaridade. Praticamente toda célula epitelial tem um cílio primário, embora ele não seja proeminente em lâmina. Quando defeitos genéticos comprometem o cílio primário, surgem síndromes ciliopáticas — rim policístico autossômico dominante e síndrome de Bardet-Biedl são exemplos clínicos.

#confusao-prevista(
  titulo: "Microvilos NÃO são cílios reduzidos",
  aluno_acha: [Pelos nomes parecidos e pela aparência de projeção, parece que microvilos seriam cílios pequenos ou imaturos.],
  mecanismo: [Microvilos têm núcleo de actina e são curtos e imóveis; cílios têm núcleo de microtúbulos 9+2 e são longos e móveis (ou 9+0 sensoriais). Estruturas completamente diferentes. Estereocílios complicam o vocabulário porque o nome contém "cílio" mas a estrutura é actina — são microvilos longos, apesar do nome.]
)

#parte-title("PARTE III — O epitélio que secreta: glandulares exócrinos e endócrinos")

#subtopico("3.1 — Como uma glândula nasce do epitélio de revestimento")

Toda glândula do corpo começou como uma porção de epitélio de revestimento que se aprofundou no conjuntivo subjacente. Durante o desenvolvimento, uma região do epitélio cresce para dentro, formando um cordão de células que se enterra no conjuntivo. A partir desse cordão, dois destinos são possíveis. Se a porção mais profunda mantém ligação com o epitélio de origem através de um canal — o ducto — a glândula é exócrina: o produto secretado pela porção profunda escoa pelo ducto e atinge uma superfície (pele, lúmen do tubo digestivo, lúmen da traqueia). Se a porção profunda perde a ligação com o epitélio de origem, ficando isolada no conjuntivo, ela é endócrina: o produto secretado cai direto no capilar próximo e vai para a circulação sanguínea.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-94.png",
  largura: 60%,
  legenda: [Desenvolvimento das glândulas a partir do epitélio. Quando o cordão mantém conexão com a superfície via ducto, a glândula é exócrina. Quando o cordão perde essa conexão durante a embriogênese e fica ilhada no conjuntivo perto do capilar, é endócrina.])

Esse modo de origem explica algumas características funcionais. Exócrinas têm ducto e dirigem o produto para uma superfície externa (no sentido amplo — incluindo o lúmen do tubo digestivo, que se comunica com o exterior). Endócrinas não têm ducto e dirigem o produto para a circulação. Em ambos os casos, a porção secretora tem origem epitelial — o que mantém a glândula como tópico do tecido epitelial.

#subtopico("3.2 — Caliciformes: a glândula unicelular embutida no epitélio")

Uma única célula pode constituir uma glândula. Esse é o caso da célula caliciforme, espalhada entre as células absortivas do epitélio cilíndrico do intestino e do epitélio pseudoestratificado da traqueia. Cada caliciforme tem um "cálice" cheio de muco que vai sendo continuamente exocitado para o lúmen do tubo, lubrificando a superfície e protegendo das condições químicas e mecânicas. Em lâmina, a caliciforme aparece como célula pálida (citoplasma cheio de mucina, que praticamente não cora em HE) com núcleo achatado encostado na base — em meio às células cilíndricas vizinhas, mais coradas e com núcleo basal mais redondo.

A caliciforme é a versão mais simples possível de glândula: uma célula só, sem ducto (a própria luz do intestino é o destino), sem porção secretora separada. Ela ilustra o princípio de que tipo de tecido e tipo de função independem do tamanho da estrutura.

#subtopico("3.3 — Exócrinas pluricelulares: três eixos de classificação")

As glândulas exócrinas pluricelulares são classificadas em três eixos cruzados, e o aluno geralmente erra exatamente por confundir qual eixo descreve qual estrutura.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-101.png",
  largura: 75%,
  legenda: [Os três eixos de classificação das glândulas exócrinas pluricelulares. (1) Ducto simples (sem ramos) ou composto (ramificado). (2) Porção secretora ramificada ou não ramificada. (3) Forma da porção secretora: tubular, acinar ou tubuloacinar. Os três eixos são independentes — qualquer combinação é possível.])

O primeiro eixo — simples × composta — refere-se ao ducto. Ducto simples não ramifica (uma glândula sudorípara, por exemplo). Ducto composto ramifica como uma árvore antes de chegar aos pontos secretores (pâncreas e glândulas salivares maiores).

O segundo eixo — ramificada × não ramificada — refere-se à porção secretora. Mesmo dentro de um único ducto simples, a porção terminal pode ser uma só (não ramificada) ou várias subdivididas (ramificada).

O terceiro eixo — tubular × acinar (também chamada alveolar) × tubuloacinar — refere-se à forma da porção secretora. Tubular significa que a porção secretora forma um cilindro com lúmen grande, células cúbicas a cilíndricas ao redor (glândula sudorípara écrina). Acinar significa que a porção secretora forma um "saco" arredondado com lúmen reduzido, células piramidais convergindo para o centro (pâncreas, parótida). Tubuloacinar tem porções de ambas as formas (submandibular, próstata).

#confusao-prevista(
  titulo: "Simples × composto refere-se ao DUCTO, não à porção secretora",
  aluno_acha: [Como "simples" e "composto" parecem termos gerais, o aluno mistura: aplica "simples" para porção não ramificada, "composto" para qualquer ramificação que apareça.],
  mecanismo: [Simples × composto descreve só o ducto. A porção secretora tem seus dois próprios eixos: ramificação (ramificada ou não) e forma (tubular, acinar, tubuloacinar). Os três eixos cruzam livremente: glândula sudorípara écrina = ducto simples + porção secretora não ramificada + forma tubular; pâncreas exócrino = ducto composto + porção secretora ramificada + forma acinar.]
)

#subtopico("3.4 — Natureza do produto: mucoso × seroso × misto, com pistas tintoriais")

Outro eixo, independente dos três anteriores, classifica a natureza do produto secretado: mucoso, seroso ou misto. Em HE, o tipo de produto deixa pistas tintoriais nítidas que permitem reconhecer o ácino em segundos.

Ácino mucoso: o produto é muco, formado principalmente por mucinas — glicoproteínas muito glicosiladas e hidratadas. Essa composição explica a lâmina: a porção rica em carboidrato não pega bem a coloração HE, então o citoplasma da célula mucosa aparece quase incolor, pálido, levemente basófilo. O núcleo é empurrado pelo conteúdo apical e fica achatado, encostado na base da célula. O lúmen do ácino mucoso costuma ser dilatado.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-107.png",
  largura: 55%,
  legenda: [Ácino mucoso. Citoplasma quase incolor (mucinas hidratadas não coram bem em HE), núcleo achatado encostado na base da célula, lúmen dilatado. As células parecem "vazias" — esse é o aspecto que indica produto mucoso.])

Ácino seroso: o produto é proteico — geralmente enzimas digestivas ou proteínas antimicrobianas. Aqui a coloração tem duas pistas ao mesmo tempo. A base da célula tende a ser basófila porque há muito #sigla("RER", [retículo endoplasmático rugoso — organela rica em ribossomos, responsável por produzir proteínas destinadas à secreção]) fabricando proteína; o ápice fica mais eosinofílico porque acumula grânulos de zimogênio, isto é, vesículas cheias de proteína secretória pronta para sair. O núcleo é arredondado e ocupa posição central ou levemente basal — não está achatado nem encostado na base como no mucoso. O lúmen é reduzido, quase imperceptível, porque as células piramidais ocupam quase todo o espaço convergindo para o centro.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-114.png",
  largura: 55%,
  legenda: [Ácino seroso. Base basófila pelo RER, ápice eosinofílico pelos grânulos de zimogênio, núcleo arredondado central ou basal e lúmen reduzido. A coloração revela a fábrica de proteína embaixo e o estoque secretório em cima.])

Ácino misto é um caso específico: predomina o tipo mucoso (com aspecto pálido e núcleo basal), e sobreposta a ele aparece uma "meia-lua" de células serosas (com citoplasma eosinofílico e núcleo arredondado) — chamada semiluna de Gianuzzi. Não é mistura difusa de mucoso e seroso espalhados — é arranjo específico: mucoso no corpo do ácino + capuz seroso por cima.

A distribuição entre glândulas salivares humanas ilustra: parótida é exclusivamente serosa (daí inflamar dramaticamente na caxumba — produção de muito conteúdo proteico inflamado); sublingual é quase exclusivamente mucosa (saliva grossa e lubrificante); submandibular é mista, com predominância serosa e algumas meias-luas.

#mini-resumo[Mucoso: pálido em HE, núcleo achatado basal, lúmen amplo. Seroso: base basófila, ápice eosinofílico, núcleo arredondado e lúmen reduzido. Misto: mucoso de base + meia-lua serosa por cima. Parótida = seroso. Sublingual = mucoso. Submandibular = misto.]

#subtopico("3.5 — Células mioepiteliais: o músculo da glândula que continua sendo epitélio")

Em torno da porção secretora de algumas glândulas (mamária, salivares, sudoríparas) há uma fileira de células fusiformes, com filamentos contráteis de actina e miosina, posicionadas entre a célula secretora e a lâmina basal. São as células mioepiteliais. Quando contraem, comprimem a porção secretora e ajudam a expelir o produto pelo ducto. Funcionalmente são contráteis, mas histologicamente são EPITELIAIS — origem epitelial mesma das secretoras, unidas a elas por desmossomos, com filamentos contráteis que apenas mimetizam função muscular.

A célula mioepitelial está bem ilustrada na ejeção do leite materno: quando a ocitocina é liberada pela hipófise posterior em resposta à sucção do bebê, ela age sobre células mioepiteliais ao redor das porções secretoras da glândula mamária, e a contração delas espreme o leite estocado nos alvéolos para o ducto galactóforo.

#subtopico("3.6 — Endócrinas: cordonais × foliculares, sem ducto, próximas ao capilar")

As glândulas endócrinas, lembrando, perderam o ducto durante a embriogênese. O produto é secretado direto no capilar adjacente, daí a riqueza vascular ao redor delas. Em lâmina, identificar endócrina passa por dois critérios: ausência de ducto visível (não há canal escoando produto para uma superfície) e proximidade óbvia entre célula secretora e capilares.

A organização interna divide as endócrinas em duas categorias arquitetônicas: cordonal e folicular.

#figura-nebli("/figuras/histo-03-tecidos-epiteliais/slide-126.png",
  largura: 65%,
  legenda: [Endócrinas: arquitetura cordonal (adrenal, paratireoide, hipófise, células de ilhotas pancreáticas) com cordões de células entre capilares × arquitetura folicular (tireoide), com esferas de células cúbicas envolvendo o coloide estocado.])

Endócrina cordonal tem as células dispostas em cordões ou aglomerados entre capilares fenestrados densos. As células secretam direto no capilar e o produto entra na circulação sem armazenamento prolongado. Adrenal, paratireoide, hipófise (boa parte dela) e as ilhotas de Langerhans do pâncreas seguem esse padrão.

Endócrina folicular é exceção e está representada principalmente pela tireoide. Aqui as células cúbicas (foliculares) formam esferas ocas, e dentro delas há um material estocado chamado coloide — composto essencialmente de tireoglobulina, a forma de armazenamento do hormônio tireoidiano. Quando o organismo precisa de hormônio, as células foliculares reabsorvem coloide e o processam para liberar T3 e T4 nos capilares próximos.

#confusao-prevista(
  titulo: "Tireoide é endócrina FOLICULAR, não cordonal",
  aluno_acha: [Como a maioria das endócrinas é cordonal, o aluno tende a generalizar e dizer que tireoide também é.],
  mecanismo: [Tireoide é o exemplo prototípico de arquitetura folicular: células cúbicas formando esferas ocas com coloide central (tireoglobulina armazenada). Adrenal, paratireoide, hipófise e ilhotas pancreáticas são cordonais. A arquitetura folicular da tireoide tem razão funcional: o hormônio tireoidiano é estocado extracelularmente como precursor (tireoglobulina) e mobilizado conforme demanda, comportamento que outras endócrinas não compartilham.]
)

#clinica-box("Pâncreas: o exemplo do epitélio glandular misto")[
  O pâncreas é o exemplo mais didático de glândula que combina exócrina e endócrina no mesmo órgão. Cerca de 98% do parênquima é exócrino — ácinos serosos pluricelulares organizados em torno de pequenos ductos que confluem em ductos maiores e finalmente no ducto pancreático principal, secretando enzimas digestivas (tripsinogênio, lipase, amilase, etc.) para o duodeno. Os outros 2% são endócrinos: as ilhotas de Langerhans, aglomerados de células cordonais espalhados em meio aos ácinos, secretando insulina (células β), glucagon (α), somatostatina (δ) e polipeptídeo pancreático (PP) direto no capilar. Em lâmina, as ilhotas aparecem como ilhas claras e pálidas em meio à eosinofilia intensa dos ácinos serosos — um contraste tintorial nítido. O fígado é outro exemplo de função mista, mas em arquitetura diferente: hepatócitos secretam bile para canalículos que drenam por ductos biliares (exócrino) e simultaneamente secretam proteínas plasmáticas direto para os sinusoides (endócrino lato sensu).
]

#conclusao-box[
  O epitélio é a célula em comunidade densa — colada lateralmente por junções, polarizada entre ápice e base, sentada num tapete molecular (a lâmina basal) e cumprindo uma de cinco missões: revestir superfícies e cavidades, proteger contra ambiente externo, absorver nutrientes, secretar produtos, ou perceber estímulos. Esses princípios universais valem desde o endotélio mais fino do capilar (epitélio simples pavimentoso) até a epiderme estratificada queratinizada da palma da mão.

  O mecanismo nuclear que une todas as variantes é a polaridade apico-basal sustentada pela zônula de oclusão: domínios moleculares diferentes em uma mesma célula, ancorados a um tapete basal comum, permitem transporte direcional, secreção orientada e barreira seletiva. Sem a barreira da zônula de oclusão, não há separação entre lúmen e tecido — e é justamente isso que doenças como infecção por Clostridium perfringens demonstram quando arrebentam a vedação paracelular.

  Na clínica, reconhecer epitélio em lâmina é o primeiro passo da histologia diagnóstica: carcinomas (tumores epiteliais) representam a maioria absoluta das neoplasias humanas, e diferenciá-los entre si depende justamente da capacidade de identificar de qual subtipo epitelial o tumor se originou — adenocarcinoma de cólon herdou o cilíndrico simples, carcinoma de células escamosas do pulmão herdou o estratificado pavimentoso, carcinoma urotelial herdou o urotélio.

  Os próximos resumos da disciplina vão complementar essa visão: tecido conjuntivo (o que vive abaixo da lâmina basal e nutre o epitélio), tecido muscular (que muitas vezes circunda epitélios tubulares e move o conteúdo do lúmen) e tecido nervoso (que inerva epitélios glandulares regulando a secreção). Tudo conecta de volta aqui — e o reflexo treinado de "olhar a lâmina e identificar o tecido em segundos" começa pelo epitélio.
]
