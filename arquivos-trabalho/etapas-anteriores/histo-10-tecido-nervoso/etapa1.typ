#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Todo tecido do corpo resolve um problema. O tecido nervoso resolve o problema da *comunicação a longa distância*: como levar uma informação de um dedo do pé até o cérebro — mais de um metro — em milésimos de segundo, sem que o sinal se perca no caminho. A histologia inteira deste tecido é a resposta estrutural a esse desafio. Cada peça que vamos ver existe porque a comunicação exige: uma célula que *gera e conduz* o sinal (o neurônio), um time de apoio que a *mantém viva e acelera* a condução (a glia), e um *isolamento* que impede o sinal de vazar (a mielina).

  Este resumo segue essa lógica em três blocos. Na PARTE I montamos o *neurônio* peça por peça — o corpo que fabrica, os prolongamentos que recebem e enviam, e a sinapse onde o sinal passa adiante. Na PARTE II conhecemos a *glia*, as células sem as quais o neurônio não sobrevive nem conduz depressa, e a bainha de *mielina* que elas constroem. A PARTE III sobe um nível: como neurônio e glia se *organizam* para formar o cérebro, o cerebelo, a medula e os nervos — e como reconhecer cada arranjo ao microscópio, na lâmina corada por #sigla("HE", [hematoxilina-eosina — a coloração de rotina: hematoxilina cora núcleos e o retículo rugoso de roxo-azul; eosina cora o citoplasma de rosa]).
]

#parte-title("PARTE I — O neurônio: a célula que fala", primeira: true)

#subtopico("1.1 De onde vêm e os tipos de neurônio")

O tecido nervoso é feito de dois grandes grupos de células que nascem, em sua maioria, da mesma origem embrionária: o #termo-nota[neuroectoderma][a camada mais externa do embrião que se dobra para formar o tubo neural, origem do sistema nervoso central] — a parede do tubo neural. Dessa parede saem tanto os *neurônios*, as células que geram e conduzem o sinal, quanto a maior parte das células da *glia*, o time de apoio. Há duas exceções que vale guardar desde já, porque explicam diferenças que voltam adiante: as células do sistema nervoso *periférico* (os neurônios dos gânglios e as células que os apoiam) vêm da #termo-nota[crista neural][população de células que se destaca da borda do tubo neural e migra pelo corpo, formando neurônios periféricos, células de Schwann, melanócitos e mais]; e a *microglia*, o fagócito do sistema nervoso, vem do *mesoderma* — a mesma linhagem dos glóbulos brancos. Essa origem tripla vai reaparecer quando falarmos de cada célula: *quem vem de onde* prevê o que a célula faz.

O neurônio é uma célula *excitável*: responde a estímulos gerando um pulso elétrico e o propaga. Para isso ele tem uma forma inconfundível — um corpo central de onde partem prolongamentos. E é justamente pela forma dos prolongamentos que fazemos a primeira classificação. O que muda de um tipo para o outro é *quantos* prolongamentos saem do corpo.

#figura-nebli("/figuras/histo-10-tecido-nervoso/slide-04.png",
  largura: 62%,
  legenda: [Os três tipos morfológicos. *Multipolar*: vários dendritos e um axônio — a maioria (motores, interneurônios, Purkinje). *Bipolar*: um dendrito e um axônio em polos opostos — retina, mucosa olfatória, gânglios da audição e do equilíbrio. *Pseudounipolar*: um tronco único que se bifurca em T — neurônio sensitivo do gânglio da raiz dorsal.])

O *neurônio multipolar* tem vários dendritos e um único axônio, e é de longe o mais comum: são multipolares os neurônios motores, os interneurônios e os grandes neurônios do cérebro e do cerebelo. O *neurônio bipolar* tem apenas dois prolongamentos — um dendrito e um axônio, saindo de polos opostos do corpo — e é restrito a alguns lugares muito específicos: a retina, a mucosa olfatória e os gânglios da audição e do equilíbrio. O *neurônio pseudounipolar* é o que mais confunde: dele parece sair um só prolongamento, que logo se divide em dois ramos em forma de T. Ele nasce bipolar no embrião e os dois prolongamentos se fundem num tronco comum — daí o "pseudo". É o neurônio *sensitivo* dos gânglios da raiz dorsal, aquele que leva a sensação da pele até a medula. *O detalhe que confunde todo mundo* é chamá-lo de "unipolar": unipolar de verdade praticamente não existe em humanos.

Essa classificação pela forma cruza com uma segunda, *pela função*, e as duas são independentes — um mesmo neurônio tem uma forma e uma função. Pela função, o neurônio é *aferente* (ou sensitivo), quando traz informação da periferia para o sistema nervoso; *eferente* (ou motor), quando leva a ordem do sistema nervoso para um músculo ou glândula; ou *interneurônio*, quando faz a ponte entre os dois dentro do próprio sistema nervoso — e os interneurônios são a esmagadora maioria.

#mini-resumo[Os neurônios vêm do neuroectoderma (com o periférico vindo da crista neural e a microglia do mesoderma). Classificam-se por *forma* (multipolar é a maioria; bipolar em retina/olfato/audição; pseudounipolar no gânglio sensitivo) e, à parte, por *função* (aferente, eferente, interneurônio).]

#subtopico("1.2 O corpo celular: a fábrica do neurônio")

Todo prolongamento do neurônio depende de um centro que o sustenta: o *corpo celular*, também chamado #termo-nota[pericário][o corpo celular do neurônio — a região que contém o núcleo e a maquinaria de síntese, o "centro trófico" da célula] ou *soma*. É o centro trófico da célula — é ele que fabrica praticamente todas as proteínas e organelas que serão usadas ao longo de prolongamentos que podem ter um metro de comprimento. Por isso, tudo no pericário grita "célula de altíssima síntese".

#figura-lateral("/figuras/histo-10-tecido-nervoso/slide-05.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O núcleo é *grande, esférico e claro*, com a cromatina bem distendida (eucromática) e um *nucléolo evidente* — o retrato de uma célula que mantém seus genes o tempo todo em uso. No citoplasma, o sinal mais marcante ao microscópio são os *corpúsculos de Nissl*: grumos basófilos que se coram de roxo no HE.],
  legenda: [Pericário: núcleo grande e claro, nucléolo evidente e os corpúsculos de Nissl (RER + polirribossomos) espalhados pelo citoplasma.])

O #termo-nota[corpúsculo de Nissl][acúmulo de retículo endoplasmático rugoso e polirribossomos no corpo do neurônio; cora-se intensamente por ser rico em RNA] não é uma organela nova e exclusiva do neurônio — e essa é a primeira armadilha. Ele é apenas #sigla("RER", [retículo endoplasmático rugoso — o retículo coberto de ribossomos, onde se fabricam proteínas]) organizado em grande quantidade, junto de polirribossomos livres. Cora-se de roxo com intensidade justamente porque está lotado de RNA, e o RNA é ávido pela hematoxilina. Em outras palavras: o corpúsculo de Nissl é a *marca visível da vocação do neurônio para fabricar proteína*. Além dele, o pericário tem um complexo de Golgi bem desenvolvido, muitas mitocôndrias, e um citoesqueleto próprio de *neurofilamentos* (filamentos intermediários) e neurotúbulos, que dão forma à célula e servem de trilho para o transporte — mas *não* conduzem o sinal elétrico; quem conduz é a membrana. Com a idade, acumula-se ainda um pigmento marrom, a *lipofuscina*, resto de digestão dos lisossomos: é sinal de neurônio *velho*, não de neurônio doente.

#subtopico("1.3 Dendritos, axônio e o transporte a longa distância")

Do pericário partem os dois tipos de prolongamento, e distinguir um do outro é uma das habilidades centrais na lâmina — porque eles têm papéis opostos. Os *dendritos* são a antena de *entrada*: em geral são vários, saem grossos e vão *afilando* e ramificando como galhos de árvore perto do corpo, e — ponto decisivo — eles *contêm corpúsculos de Nissl*, como o pericário. Sua superfície é coberta por milhares de *espinhas* (ou gêmulas), pequenas saliências que são o primeiro ponto de contato das sinapses e cuja quantidade muda com o aprendizado — são o substrato físico da plasticidade.

O *axônio* é a via de *saída*, e é uma só por neurônio. Ele parte de uma região especializada do corpo, o #termo-nota[cone de implantação][a saliência do corpo celular de onde parte o axônio, também chamada zona de gatilho por ser onde o potencial de ação começa] (o *hillock*), mantém um calibre *uniforme* por toda a sua extensão e — aqui está a diferença que se lê na lâmina — *não contém corpúsculos de Nissl*, nem no cone nem no restante do axônio.

#confusao-prevista(
  titulo: "Dendrito e axônio se distinguem pelo Nissl",
  aluno_acha: [aluno acha que dendrito e axônio só se diferenciam pela espessura ou por algo elétrico],
  mecanismo: [o critério prático na lâmina é o *corpúsculo de Nissl*: ele está no pericário e nos *dendritos*, mas *falta no cone de implantação e no axônio*. Um prolongamento que sai do corpo já sem Nissl, com calibre uniforme, é o axônio; os que afilam e mantêm grumos de Nissl são dendritos.],
)

Essa ausência de Nissl no axônio traz uma consequência funcional enorme, e ela é o ponto de quebra deste subtópico: *o axônio não fabrica as próprias proteínas*. Um axônio pode ter um metro de comprimento, e tudo o que ele precisa — enzimas, componentes de membrana, mitocôndrias, vesículas — é produzido no corpo celular e precisa ser *transportado* até a ponta. E aqui a difusão simples é inútil: levaria anos para uma proteína se difundir de uma ponta a outra de um axônio longo. A solução é um sistema de transporte *ativo*, que corre sobre os microtúbulos gastando #sigla("ATP", [adenosina trifosfato — a moeda de energia da célula]), e que anda nos dois sentidos com dois motores diferentes.

#figura-nebli("/figuras/histo-10-tecido-nervoso/slide-07.png",
  largura: 66%,
  legenda: [O transporte axonal, sobre os microtúbulos, em dois sentidos. *Anterógrado*: a *cinesina* leva organelas e vesículas do corpo celular para o terminal. *Retrógrado*: a *dineína* traz material do terminal de volta ao corpo (para reciclagem — e, patologicamente, é a via por onde o vírus da raiva e a toxina tetânica sobem até o SNC).])

No sentido *anterógrado* — do corpo para o terminal — o motor é a *cinesina*, que carrega para a ponta as mitocôndrias, as vesículas e as enzimas recém-fabricadas. No sentido *retrógrado* — do terminal de volta para o corpo — o motor é a *dineína*, que traz material usado para reciclagem e sinais de sobrevivência captados no terminal. *Trocar os dois é o erro mais comum*, então vale a âncora: a *cinesina* vai para a ponta (anterógrado); a *dineína* traz de volta (retrógrado). Essa via retrógrada tem uma face clínica marcante: é exatamente por ela que o *vírus da raiva* e a *toxina do tétano*, captados numa terminação nervosa, viajam para dentro do neurônio até alcançar o sistema nervoso central — são neurotrópicos porque *sequestram a dineína*, não porque circulam pelo sangue.

#mini-resumo[O axônio não tem Nissl porque não sintetiza proteína — tudo vem do corpo celular por transporte ativo sobre microtúbulos. *Cinesina leva ao terminal (anterógrado); dineína traz de volta (retrógrado)*. A via retrógrada é a porta de entrada da raiva e do tétano no sistema nervoso.]

#subtopico("1.4 A sinapse: onde o sinal passa adiante")

Chegando ao fim do axônio, o sinal precisa ser entregue à célula seguinte, e o local dessa entrega é a *sinapse*. Pense nela como um bastão de revezamento numa corrida: o sinal elétrico corre dentro de um neurônio, mas para passar ao próximo ele é convertido, na maioria dos casos, num sinal *químico* — um mensageiro liberado no minúsculo espaço entre as duas células. Essa conversão parece um rodeio, mas é o que permite ao sistema nervoso *modular, amplificar e integrar* sinais, em vez de apenas repassá-los.

A sinapse *química* tem três peças fixas, e reconhecê-las é o que importa na histologia. O *componente pré-sináptico* é o terminal do axônio, dilatado num *botão*, e recheado de *vesículas sinápticas* cheias de neurotransmissor e de mitocôndrias. A *fenda sináptica* é o espaço estreito entre as duas células. E a *membrana pós-sináptica*, na célula seguinte, é onde ficam os receptores. Funcionalmente, em duas ou três frases: o potencial de ação chega ao botão, abre canais de cálcio, o cálcio faz as vesículas se fundirem à membrana e despejarem o neurotransmissor na fenda, e ele atravessa e se liga aos receptores do outro lado — encerrando o revezamento.

#figura-lateral("/figuras/histo-10-tecido-nervoso/slide-09.png",
  lado: "left",
  largura-figura: 44%,
  texto: [Há também sinapses *elétricas*, bem mais raras, em que as duas células são unidas por *junções comunicantes* (gap): íons passam direto de uma para a outra, sem mensageiro químico, e o sinal é praticamente instantâneo e bidirecional. E há uma classificação pela *posição* do contato: quando o botão toca um dendrito, é *axodendrítica* (a mais comum); quando toca o corpo, *axossomática*; quando toca outro axônio, *axoaxônica*.],
  legenda: [Sinapse química passo a passo: o potencial de ação abre canais de Ca²⁺ no botão; o Ca²⁺ dispara a fusão das vesículas; o neurotransmissor cruza a fenda e ativa os receptores pós-sinápticos.])

Com o neurônio montado — corpo que fabrica, dendritos que recebem, axônio que conduz e sinapse que entrega — falta a pergunta que abre a próxima PARTE: como uma célula tão exigente sobrevive e conduz tão depressa? A resposta não está no neurônio. Está no time que o cerca.

#parte-title("PARTE II — A glia e a bainha de mielina")

#subtopico("2.1 Astrócitos e a barreira hematoencefálica")

O neurônio que acabamos de montar é uma célula cara e frágil: consome muita energia, é sensível a variações do meio e não se divide para se repor. Ele só funciona porque está cercado por células de apoio, a *glia* (ou neuroglia), que no sistema nervoso central são até dez vezes mais numerosas que os próprios neurônios. A primeira delas, e a mais versátil, é o *astrócito* — uma célula grande, estrelada, cujos prolongamentos preenchem quase todo o espaço entre os neurônios.

O astrócito faz muito mais do que "encher espaço". Ele *tampona o potássio* que sai dos neurônios em atividade, impedindo que o excesso desregule a excitabilidade; *recicla neurotransmissores* retirados da fenda sináptica; e *nutre o neurônio*, captando glicose do sangue e repassando-a. Mas sua função mais célebre está no contato com os vasos: cada astrócito estende um prolongamento que termina num *pé perivascular*, uma expansão achatada que abraça o capilar.

#figura-nebli("/figuras/histo-10-tecido-nervoso/slide-11.png",
  largura: 58%,
  legenda: [O astrócito faz a ponte entre o sangue e o neurônio: um prolongamento termina em *pé perivascular* sobre o capilar, e é esse contato que induz o endotélio a formar a barreira hematoencefálica. Outros prolongamentos envolvem os neurônios e as sinapses.])

É esse pé perivascular que constrói a #termo-nota[barreira hematoencefálica][a barreira que controla rigorosamente o que passa do sangue para o tecido nervoso central] (#sigla("BHE", [barreira hematoencefálica — filtro seletivo entre o sangue e o tecido nervoso])). A barreira em si é feita pelas *junções oclusivas* entre as células do endotélio do capilar — junções tão apertadas que fecham o espaço entre elas e obrigam qualquer substância a atravessar *através* das células, sob controle. Só que quem *induz* o endotélio a formar essas junções é o astrócito, com seu pé perivascular.

#confusao-prevista(
  titulo: "Quem faz a barreira hematoencefálica é o astrócito, não o oligodendrócito",
  aluno_acha: [aluno associa "barreira" à mielina, e atribui a BHE ao oligodendrócito ou à microglia],
  mecanismo: [a BHE nasce das *junções oclusivas do endotélio*, e quem induz o endotélio a formá-las é o *pé perivascular do astrócito*. O oligodendrócito faz mielina; a microglia é o fagócito. Cada glia tem seu papel — só o astrócito toca o vaso.],
)

Os astrócitos vêm em duas variedades que se leem pela vizinhança: o *protoplasmático*, de muitos prolongamentos curtos e ramificados, habita a substância cinzenta (onde estão os corpos dos neurônios); o *fibroso*, de prolongamentos longos e finos, ricos em filamentos, habita a substância branca (onde correm os axônios). Quando o tecido nervoso é lesado, são os astrócitos que proliferam e formam a cicatriz — a *gliose* —, tapando o buraco que o neurônio, incapaz de se dividir, não consegue preencher.

#subtopico("2.2 Oligodendrócito, Schwann e a mielina")

Volte ao axônio de um metro de comprimento. Se ele conduzisse o potencial de ação ponto a ponto por toda a sua membrana, como um pavio queimando, a condução seria lenta e cara — a corrente vazaria pela membrana o tempo todo, exigindo que cada trecho fosse regenerado. A solução da evolução foi *isolar* o axônio, e é isso que faz a *bainha de mielina*: um envoltório de múltiplas camadas de membrana enroladas em espiral, riquíssimo em lipídio, que funciona como a capa isolante de um fio elétrico. E quem constrói essa bainha são duas células diferentes, uma em cada sistema — e a diferença entre elas é o ponto mais cobrado do tema.

#figura-nebli("/figuras/histo-10-tecido-nervoso/slide-13.png",
  largura: 66%,
  legenda: [A mesma bainha, dois construtores. No *SNC*, um *oligodendrócito* emite vários prolongamentos e mieliniza *vários axônios ao mesmo tempo*. No *SNP*, uma *célula de Schwann* se enrola em torno de *um único trecho de um único axônio* — um internódulo por célula.])

No sistema nervoso central (#sigla("SNC", [sistema nervoso central — encéfalo e medula espinal])), quem faz a mielina é o *oligodendrócito*: uma célula que estende *vários* prolongamentos e envolve, cada um, um trecho de um axônio diferente — um só oligodendrócito mieliniza vários axônios de uma vez. No sistema nervoso periférico (#sigla("SNP", [sistema nervoso periférico — nervos e gânglios fora do encéfalo e da medula])), quem faz a mielina é a *célula de Schwann*: e ela se dedica a *um único trecho de um único axônio*, enrolando-se toda em volta dele para formar um segmento de bainha (um internódulo).

#atencao-box("A inversão que custa caro: oligodendrócito × Schwann", [No SNC, *um oligodendrócito mieliniza vários axônios*. No SNP, *uma célula de Schwann faz um único internódulo de um único axônio*. Inverter isso derruba todo o raciocínio sobre por que as doenças desmielinizantes do SNC (esclerose múltipla) e do SNP (Guillain-Barré) atingem células diferentes. A âncora: o oligodendrócito é generoso (serve muitos); a Schwann é dedicada (serve um só).])

Entre um segmento de mielina e o seguinte há uma pequena falha propositalmente descoberta: o #termo-nota[nó de Ranvier][o intervalo sem mielina entre dois segmentos da bainha, onde a membrana do axônio fica exposta e concentra canais de sódio]. E é aqui que se entende por que a mielina acelera a condução — e por que a explicação intuitiva está errada. A mielina *não conduz* o impulso melhor; ela é *isolante*, e impede a corrente de vazar nos trechos cobertos. O potencial de ação, então, não consegue se regenerar sob a mielina — ele só pode "reacender" nos nós, onde a membrana está exposta e cheia de canais de sódio. O resultado é que o sinal *salta de nó em nó*, em vez de percorrer cada milímetro da membrana: é a #termo-nota[condução saltatória][a propagação do potencial de ação "saltando" de um nó de Ranvier ao seguinte, muito mais rápida que a condução contínua], muito mais rápida e econômica.

#figura-nebli("/figuras/histo-10-tecido-nervoso/slide-14.png",
  largura: 70%,
  legenda: [A mielina isola; os *nós de Ranvier* são os únicos pontos onde o potencial de ação se regenera. Por isso o sinal *salta* de nó em nó — condução saltatória. Nas fibras amielínicas, sem essa capa, a condução é contínua e lenta.])

Falta desfazer uma última confusão, sobre as fibras que *não* têm mielina. No SNP, mesmo os axônios *amielínicos* são embrulhados por células de Schwann — só que de outro jeito: uma única célula de Schwann acomoda *vários* axônios finos em sulcos da sua superfície, *sem se enrolar em espiral* em torno deles. Ou seja, ter uma célula de Schwann ao redor não é o mesmo que ter mielina; a mielina exige o *enrolamento em espiral*, e ele só acontece em axônios mielínicos, um por célula.

#mini-resumo[A mielina é um isolante que força o potencial de ação a se regenerar só nos nós de Ranvier — daí a condução saltatória, rápida e econômica. *No SNC quem a faz é o oligodendrócito (vários axônios por célula); no SNP é a célula de Schwann (um internódulo por célula)*. Fibra amielínica ainda tem Schwann, mas sem o enrolamento em espiral.]

#subtopico("2.3 Microglia, ependimárias e células satélites")

Faltam três tipos de glia para completar o time, cada um com um endereço e uma tarefa próprios. A *microglia* é a exceção da família: enquanto as demais glias vêm do neuroectoderma, ela vem do *mesoderma*, da mesma linhagem dos monócitos do sangue. Isso prevê exatamente o que ela faz — é o *macrófago residente* do sistema nervoso central, o fagócito que vigia o tecido, engole restos celulares e microrganismos e dispara a resposta inflamatória quando há lesão. É uma célula pequena, de prolongamentos curtos e espinhosos, que se ativa e incha diante de qualquer agressão.

As *células ependimárias* revestem as cavidades internas do sistema nervoso — os ventrículos do encéfalo e o canal central da medula. Formam um epitélio de células cúbicas a cilíndricas, muitas com *cílios* que ajudam a movimentar o líquido, e uma face voltada para a cavidade. Onde esse epitélio se especializa sobre tufos de capilares, ele forma o #termo-nota[plexo coroide][a estrutura, feita de ependimárias modificadas sobre capilares, que produz o líquido cerebroespinal (liquor)] — e é aí, importante, que se *produz o liquor*. A ependimária comum reveste; o plexo coroide, que é ependimária modificada, é que fabrica o líquido.

Por fim, no sistema nervoso periférico, as *células satélites* envolvem completamente o corpo dos neurônios dentro dos gânglios, formando uma cápsula que os isola e ajuda a controlar o microambiente ao redor deles — o equivalente periférico do abraço que a glia central dá aos neurônios. Cuidado com o nome: *célula satélite* aqui não tem nada a ver com a célula satélite do músculo (aquela é célula-tronco de regeneração); são apenas homônimas.

#parte-title("PARTE III — A arquitetura do tecido nervoso")

#subtopico("3.1 Substância branca e substância cinzenta")

Junte milhões de neurônios e sua glia e você tem um órgão — o cérebro, a medula, um nervo. Visto a olho nu num corte, o sistema nervoso central se separa em duas cores, e a diferença entre elas é a chave para ler qualquer corte do encéfalo ou da medula. Pense na distinção assim: onde estão os *escritórios* (os corpos que decidem) o tecido é cinzento; onde estão os *cabos* (os axônios que só transmitem) o tecido é branco.

A *substância cinzenta* é onde se concentram os *corpos celulares* dos neurônios, seus dendritos e o emaranhado de prolongamentos e sinapses entre eles — a esse emaranhado dá-se o nome de #termo-nota[neurópilo][a rede densa de dendritos, axônios finos e prolongamentos de glia que preenche o espaço entre os corpos dos neurônios na substância cinzenta]. É a região do *processamento*: é ali que a informação é integrada. A *substância branca*, por outro lado, quase não tem corpos celulares: é feita de *axônios mielinizados* correndo em feixes, e ela é branca *justamente por causa da mielina* — o lipídio da bainha, abundante, dá a cor esbranquiçada.

#figura-nebli("/figuras/histo-10-tecido-nervoso/slide-15.png",
  largura: 58%,
  legenda: [Substância cinzenta (corpos celulares, dendritos e sinapses — o processamento) e substância branca (axônios mielinizados, esbranquiçados pela mielina). O arranjo das duas é o que identifica cada região do sistema nervoso central ao corte.])

#confusao-prevista(
  titulo: "A substância branca não é a que tem \"mais neurônios\"",
  aluno_acha: [aluno acha que a substância branca é a mais "cheia" de neurônios],
  mecanismo: [é o contrário: os *corpos* dos neurônios ficam na *cinzenta* (com os dendritos e as sinapses — o processamento). A *branca* é feita de *axônios mielinizados* de passagem, quase sem corpos celulares; sua cor vem da mielina, não de uma abundância de células.],
)

#subtopico("3.2 Córtex cerebral, cerebelo e medula espinal")

A mesma dupla — cinzenta e branca — se arranja de formas diferentes em cada região, e é o *arranjo* que identifica o corte. No *córtex cerebral*, a cinzenta fica por *fora*, formando uma casca de poucos milímetros na superfície das circunvoluções, enquanto a branca ocupa o miolo. Essa casca é organizada em *seis camadas* de neurônios, e as pequenas diferenças de espessura e tipo celular entre camadas, de região para região, formam o mapa que Brodmann desenhou — um mapa de #termo-nota[citoarquitetura][a organização microscópica dos neurônios em camadas; a base do mapa de Brodmann, que divide o córtex por como as camadas se dispõem, não pelos giros a olho nu], não de anatomia macroscópica.

#figura-lateral("/figuras/histo-10-tecido-nervoso/slide-17.png",
  lado: "right",
  largura-figura: 42%,
  texto: [O *cerebelo* tem três camadas fáceis de reconhecer. A externa é a *camada molecular*, pobre em corpos celulares. No meio, uma fileira única de células gigantes: a *camada de Purkinje*. E a interna é a *camada granular*, densíssima de pequenos neurônios. A célula de *Purkinje* é a assinatura do cerebelo — seu corpo fica na camada que leva seu nome, seus dendritos se abrem em leque na molecular, e seu axônio é a *única via de saída* de todo o córtex cerebelar.],
  legenda: [Córtex cerebelar: camadas molecular, de Purkinje e granular. A célula de Purkinje integra tudo e é a única saída.])

Na *medula espinal*, o arranjo se inverte em relação ao córtex: a *cinzenta fica por dentro*, desenhando uma figura em forma de *H* (ou de borboleta) no centro do corte, e a *branca a envolve* por fora. No centro exato do H corre o canal central, revestido de epêndima. É por isso que "cinzenta é interna" ou "cinzenta é externa" nunca vale como regra geral: no córtex ela é externa, na medula é interna — *o que importa é reconhecer o arranjo de cada corte*.

#subtopico("3.3 O nervo periférico, os gânglios e as meninges")

Fora do sistema nervoso central, os axônios se agrupam em *nervos*, e um nervo é uma obra de engenharia de tecido conjuntivo — o mesmo material de suporte que embrulha o músculo e conduz vasos, aqui organizado em três bainhas encaixadas. Cada *fibra nervosa* individual (o axônio com sua célula de Schwann) é envolvida por uma fina camada de conjuntivo frouxo, o *endoneuro*. Vários axônios reunidos formam um *fascículo*, embrulhado pelo *perineuro*. E o conjunto de fascículos que forma o nervo inteiro é envolto pelo *epineuro*, a camada externa mais espessa, por onde correm os vasos.

#figura-nebli("/figuras/histo-10-tecido-nervoso/slide-21.png",
  largura: 64%,
  legenda: [As três bainhas do nervo periférico: *endoneuro* (cada fibra), *perineuro* (cada fascículo) e *epineuro* (o nervo inteiro, com os vasos). O perineuro, além de embrulhar, funciona como barreira, com junções oclusivas entre suas células.])

O arranjo lembra as bainhas do músculo (endo, peri e epimísio), mas há uma diferença funcional que vale fixar: o *perineuro* não é só embalagem — suas células têm junções oclusivas e formam uma *barreira*, controlando o que chega aos axônios, um papel que o perimísio do músculo não tem. Quando os corpos dos neurônios se agrupam *fora* do sistema nervoso central, esse acúmulo é um *gânglio*. E nem todo gânglio é igual: o *gânglio sensitivo* (o da raiz dorsal) é feito de neurônios *pseudounipolares* envolvidos por células satélites, e ali *não há sinapse* — o neurônio só passa por ele; já o *gânglio autônomo* é feito de neurônios *multipolares* e é uma verdadeira estação de *sinapse*, onde uma via troca de neurônio.

Uma última camada protege todo o conjunto: as *meninges*, três envoltórios de conjuntivo — a *dura-máter* externa e espessa, a *aracnoide* intermediária, e a *pia-máter* delicada, colada ao tecido nervoso. Entre a aracnoide e a pia circula o #termo-nota[liquor][o líquido cerebroespinal, produzido no plexo coroide, que circula em torno e dentro do sistema nervoso central, nutrindo-o e amortecendo impactos] (líquido cerebroespinal, ou #sigla("LCR", [líquido cerebroespinal — o liquor, produzido no plexo coroide])), o líquido produzido no plexo coroide que amortece o encéfalo e a medula contra traumas e ajuda a nutri-los. Da célula única que fala, subimos até o órgão inteiro que pensa — e cada nível, como prometido, foi só a forma servindo à função de comunicar.

#mini-resumo[Do neurônio ao órgão, cada estrutura serve à comunicação. A *cinzenta* processa (corpos e sinapses), a *branca* transmite (axônios mielinizados); no córtex a cinzenta é externa, na medula é interna. Fora do sistema central, os axônios viram *nervos* (com endoneuro, perineuro e epineuro) e os corpos se agrupam em *gânglios* — sensitivos, sem sinapse, ou autônomos, com sinapse.]
