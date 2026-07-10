#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O corpo é constantemente invadido — bactérias na pele ferida, vírus na mucosa respiratória, restos de células mortas. Contra tudo isso existe um sistema de defesa que não fica parado num lugar: ele *circula*. Células de defesa nascem em um órgão, amadurecem em outro, patrulham o sangue, saem para os tecidos, entram na linfa e voltam ao sangue, num rodízio que nunca para. Esse é o *sistema linfoide* (ou linfático): o conjunto de células, tecidos e órgãos que produz, abriga e organiza a resposta imune.

  Este resumo é sobre a *histologia* desse sistema — como ele é montado quando olhamos no microscópio. E há uma lógica que vale a pena guardar desde já, porque ela vai se repetir três vezes: em todo tecido linfoide existem *células fixas*, que formam uma malha de sustentação e filtram o que passa, e *células livres*, que se movem por essa malha e fazem a resposta propriamente dita. Cada órgão linfoide é uma variação sobre esse mesmo tema — muda apenas *qual líquido* ele filtra e *como* organiza as células dentro. No fim, você vai conseguir olhar uma lâmina e dizer, por uma única pista, qual órgão está vendo.
]

#parte-title("PARTE I — As células e a arquitetura do tecido linfoide", primeira: true)

#subtopico("1.1 O mapa geral: quem produz, quem responde")

O sistema linfoide se divide em dois grandes grupos de órgãos, e essa divisão organiza tudo o que vem depois. De um lado estão os *órgãos linfoides primários* (ou centrais): a *medula óssea* e o *timo*. São as fábricas e escolas — neles os linfócitos nascem e amadurecem, ganhando a capacidade de reconhecer o que é estranho ao corpo. Do outro lado estão os *órgãos linfoides secundários* (ou periféricos): os *linfonodos*, o *baço* e os *agregados de tecido linfoide* espalhados pelas mucosas. Neles a resposta imune *acontece* — é onde o linfócito já pronto encontra o invasor e reage.

A função de fundo é sempre a mesma: distinguir o *próprio* do *não-próprio*. O corpo precisa reconhecer suas próprias células como "de casa" e atacar apenas o que é estranho — uma bactéria, um vírus, uma célula infectada. Qualquer molécula capaz de ser reconhecida como estranha e disparar essa resposta é um #termo-nota[antígeno][molécula reconhecida como estranha pelo sistema imune, capaz de disparar a resposta imunitária]. Guarde a dupla primário/secundário — ela é o esqueleto das PARTES II e III.

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-33.png",
  largura: 55%,
  legenda: [Os vasos e órgãos linfáticos distribuídos pelo corpo. Repare que não é um sistema concentrado num ponto: é uma rede, e as células de defesa estão em trânsito constante entre sangue, linfa e tecido conjuntivo.])

#subtopico("1.2 As linhagens de linfócitos: três células, três estratégias")

Antes de montar os órgãos, precisamos conhecer as células que os habitam. O protagonista do tecido linfoide é o *linfócito* — mas "linfócito" não é uma célula só. Existem três linhagens, todas nascidas de precursores na medula óssea, e cada uma resolve o problema da defesa de um jeito diferente.

O *linfócito B* é o braço da chamada *resposta humoral*. A palavra "humoral" vem de "humor", líquido — porque a arma do B é uma proteína solúvel que circula nos líquidos do corpo: o *anticorpo*. Só que o B em repouso ainda não secreta anticorpo; ele carrega moléculas de #sigla("Ig", [imunoglobulina — a classe de proteína a que pertencem os anticorpos]) Ig (imunoglobulina) de superfície (IgM e IgD) funcionando como antena para detectar o antígeno. Quando o B é ativado, ele se transforma em *plasmócito* — e é o plasmócito, essa célula final, que secreta anticorpo em grande quantidade. Essa cadeia importa: *linfócito B ativa → vira plasmócito → plasmócito secreta anticorpo*. O B não é o produtor direto; o plasmócito é.

O *linfócito T* é o braço da *resposta celular* — ele age por contato célula a célula, não por proteína solúvel. Seu marcador de superfície é o #sigla("TCR", [receptor de célula T — reconhece o antígeno na superfície de outra célula]) TCR (*T cell receptor*), a molécula que reconhece o antígeno apresentado por outra célula. Há subtipos com papéis bem distintos, e confundi-los é o erro clássico. O *T citotóxico* (ou killer) é o assassino: reconhece uma célula infectada por vírus ou uma célula tumoral e a mata, perfurando sua membrana com *perforinas*. O *T helper* (auxiliar) não mata ninguém — ele coordena: secreta *interleucinas*, mensageiros químicos que ativam macrófagos, linfócitos B e os próprios T citotóxicos. E o *T regulador* (Treg) faz o freio: encerra a resposta quando o estímulo acaba e impede que o sistema ataque o próprio corpo, prevenindo doenças autoimunes.

A terceira linhagem é o *linfócito* #sigla("NK", [*natural killer* — linfócito da imunidade inata, mata sem sensibilização prévia]) NK (*natural killer*). Ele é diferente dos outros dois num ponto essencial: pertence à *imunidade inata*, a defesa rápida e inespecífica. O NK não precisa de sensibilização prévia nem reconhece um antígeno específico — ele já nasce pronto para atacar células anormais (infectadas ou tumorais). Por isso não tem TCR e não gera memória imunológica.

Como são quatro tipos celulares com um traço definidor cada, vale organizá-los lado a lado:

#table(
  columns: (auto, auto, 1fr),
  inset: 7pt,
  align: (left, left, left),
  stroke: 0.5pt + gray-border,
  table.header(
    [*Célula*], [*Ramo da imunidade*], [*O que faz*]
  ),
  [Linfócito B], [Adquirida (humoral)], [ativa e vira plasmócito, que secreta anticorpo],
  [Linfócito T citotóxico], [Adquirida (celular)], [mata célula infectada/tumoral com perforina],
  [Linfócito T helper], [Adquirida (celular)], [secreta interleucinas que ativam outras células],
  [Linfócito T regulador], [Adquirida (celular)], [encerra a resposta e previne autoimunidade],
  [Linfócito NK], [Inata], [mata células anormais sem sensibilização prévia],
)

Falta um coadjuvante essencial: o *macrófago*, e com ele as chamadas *células apresentadoras de antígeno*. O macrófago fagocita (engole e digere) o invasor, mas faz mais que limpeza — ele quebra o antígeno e o *exibe* na própria superfície para que o linfócito T o reconheça. Sem essa apresentação, o T não consegue "ver" a maioria dos antígenos. Essas células, que você vai reencontrar dentro de cada órgão adiante, são a ponte entre engolir o invasor e disparar a resposta específica.

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-14.png",
  largura: 72%,
  legenda: [Do linfócito imaturo às funções finais. À esquerda, o B ativado vira plasmócito e produz anticorpo (resposta humoral). No centro, o T se divide em helper — que ativa macrófagos e outras células — e citotóxico, que lisa a célula infectada (resposta celular adquirida). À direita, o NK lisa sem sensibilização (resposta inata). Este é o mapa que vamos povoar nos órgãos.])

#mini-resumo[B faz anticorpo (via plasmócito); T age por contato (citotóxico mata, helper coordena, Treg freia); NK é o matador inato. Macrófago apresenta o antígeno e conecta os dois mundos.]

#subtopico("1.3 O tecido linfoide como tecido: a malha e o que passa por ela")

Agora que temos as células, podemos montar o tecido. O *tecido linfoide* é um tipo especial de tecido conjuntivo, e como todo tecido conjuntivo ele tem duas populações que convém separar na cabeça: as células *fixas*, que ficam ancoradas formando um arcabouço, e as células *livres*, que se movem por dentro dele.

Vale a pena pensar na malha como uma rede de pescador tridimensional, esticada dentro do órgão. Quem fabrica e mantém essa rede são as *células reticulares* — #termo-nota[célula reticular][célula fixa que produz e se apoia nas fibras reticulares, formando o arcabouço do tecido linfoide] células fixas de longos prolongamentos que produzem as *fibras reticulares*. A #termo-nota[fibra reticular][fibra fina e ramificada de colágeno tipo III que forma a trama de sustentação; é o produto da célula reticular, não a célula] fibra reticular é um fio delgado de colágeno tipo III, fino e muito ramificado, que forma a trama de sustentação frouxa por onde tudo transita. Repare na distinção que confunde meio mundo: a *célula* reticular é quem produz; a *fibra* reticular é o produto. Não são a mesma coisa. Junto das reticulares ficam os *macrófagos fixos*, também chamados #termo-nota[histiócito][macrófago fixo (residente) do tecido conjuntivo, ancorado na malha para fagocitar o que passa] histiócitos — plantados na malha como filtros vivos, prontos para fagocitar o que a rede segurar.

Pela malha circulam as *células livres*: os linfócitos (B, T e NK que vimos há pouco), os plasmócitos e os macrófagos livres. São elas que fazem a resposta — a rede fixa só as segura, organiza e apresenta o que precisa ser combatido. Aqui está, em miniatura, o princípio que abre este resumo: *fixas fazem a estrutura e o filtro; livres fazem a resposta*. Esse par vai reaparecer em cada órgão, com nomes diferentes, mas sempre a mesma divisão de trabalho.

#subtopico("1.4 Frouxo, denso, nodular: três arranjos da mesma malha")

A mesma malha reticular pode ser arrumada de três maneiras dentro dos órgãos, e o nome de cada arranjo descreve *qual população predomina*. No arranjo *frouxo*, predomina a rede de células fixas, com poucos linfócitos entre as fibras — é o que forma os *seios* (canais por onde a linfa ou o sangue escorrem devagar, sendo filtrados). No arranjo *denso*, predomina a população de células livres, com linfócitos amontoados na malha — é o que forma os *cordões*. E o arranjo *nodular* é o tecido denso enrolado em bola: uma esfera compacta de linfócitos chamada *nódulo linfático*.

O nódulo merece atenção porque quase todo mundo o imagina errado. À primeira vista, parece uma estrutura fixa e permanente do órgão, como um cômodo da casa — mas não é. O nódulo é uma estrutura *temporária*, *sem cápsula*, que depende de estímulo antigênico para existir. Quando um antígeno chega e ativa os linfócitos B, eles proliferam e formam, no meio do nódulo, uma região mais clara: o #termo-nota[centro germinativo][região central e mais clara do nódulo linfático, onde linfócitos B proliferam durante a resposta imune] *centro germinativo*, o sítio dessa multiplicação intensa de B. Terminada a resposta, o centro germinativo regride. Ou seja: nódulo com centro germinativo bem visível é sinal de tecido *reagindo*, não de anatomia fixa. E note — o centro germinativo é território de linfócito *B*, fenômeno da resposta humoral; não se produz linfócito T ali.

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-18.png",
  largura: 55%,
  legenda: [O tecido linfoide ao microscópio: os pontos arroxeados escuros e pequenos são núcleos de linfócitos (células livres) preenchendo a malha; os espaços mais claros e rosados são os seios, por onde o líquido filtra. Quanto mais denso o amontoado de linfócitos, mais "denso" o arranjo.])

Esse tecido aparece de duas formas espalhadas pelo corpo, fora dos órgãos encapsulados. O *tecido linfoide difuso* é uma população solta de linfócitos e plasmócitos infiltrada nas mucosas dos sistemas digestório, respiratório, urinário e genital — a primeira barreira imunológica dessas superfícies. E o *tecido linfoide nodular* forma nódulos isolados ou agregados, como as *placas de Peyer* do intestino. Esse conjunto associado às mucosas recebe o nome de #sigla("MALT", [tecido linfoide associado à mucosa — *mucosa-associated lymphoid tissue*]) MALT (tecido linfoide associado à mucosa). Guarde o MALT: é a defesa distribuída nas portas de entrada do corpo, e fecha a lógica de que o sistema linfoide está *em toda parte*, não só nos órgãos que veremos a seguir.

#mini-resumo[Frouxo (fixas predominam, forma seios), denso (livres predominam, forma cordões), nodular (denso em bola, forma o nódulo). O nódulo é temporário, sem cápsula, e seu centro germinativo é fábrica de linfócito B em resposta.]

#parte-title("PARTE II — Órgãos linfoides primários: onde os linfócitos nascem e amadurecem")

#subtopico("2.1 Primários são a escola: medula óssea e timo")

Os órgãos linfoides primários são onde os linfócitos são *produzidos* e *educados* — ou seja, onde ganham a capacidade de reconhecer antígenos antes de serem enviados para o front. São dois. A *medula óssea* é a origem de todas as células do sangue, linfócitos incluídos; é também onde o *linfócito B completa seu amadurecimento* (não à toa o "B" remete a *bone marrow*, medula óssea). O *timo* é o segundo órgão primário, e sua especialidade é uma só: educar o *linfócito T* (o "T" vem justamente de timo). Um linfócito T sai da medula ainda imaturo, viaja até o timo e só ali termina sua formação.

Por que separar produção de educação em órgãos distintos? Porque educar o T é uma tarefa delicada e perigosa: o timo precisa testar cada linfócito T contra as moléculas do próprio corpo e eliminar os que reagiriam contra ele — e isso exige um ambiente controlado, isolado, que a medula não oferece. É esse ambiente que a histologia do timo revela. Vamos a ele.

#subtopico("2.2 A estrutura do timo: lóbulos, córtex e medula")

O timo é revestido por uma cápsula de tecido conjuntivo que manda *septos* para dentro, dividindo o órgão em *lóbulos tímicos*. Esses lóbulos são *incompletos*: os septos não isolam totalmente um do outro, de modo que a parte interna de lóbulos vizinhos é contínua. Cada lóbulo tem duas regiões com aparência bem diferente ao microscópio, e a diferença é só de *densidade de linfócitos*.

O *córtex* é a região externa, escura e basófila, densamente preenchida por linfócitos T imaturos — é a região "cheia". A *medula* é a região interna, mais clara, com menos linfócitos e mais do arcabouço aparente — é a região "vazia" por comparação. Como os lóbulos são incompletos, a medula de lóbulos vizinhos se conecta num miolo contínuo. Essa geografia córtex-escuro/medula-clara é o primeiro passo de qualquer leitura de lâmina do timo, e vai carregar a lógica do órgão inteiro: o córtex é onde o T imaturo é testado; a medula é a antessala de saída do T já pronto.

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-26.png",
  largura: 60%,
  legenda: [Timo em baixa potência. Os lóbulos são separados por septos; em cada um, o córtex aparece escuro (denso em timócitos) e a medula, mais clara. Repare que a medula dos lóbulos se comunica — os lóbulos são incompletos.])

#subtopico("2.3 As duas células do timo: estroma epitelial e timócitos")

Aqui está o ponto que mais confunde nesta aula, e vale desfazer o erro antes de construir o certo. Em todos os tecidos linfoides que vimos na PARTE I, o arcabouço era feito de células reticulares que produzem fibras reticulares de colágeno. É natural supor que no timo seja igual — *só que não é*. O estroma do timo não é feito de células reticulares comuns do conjuntivo: é feito de #termo-nota[célula reticular epitelial][célula de origem epitelial que forma o estroma do timo; unida por desmossomos e produtora de hormônios tímicos — não produz fibra reticular de colágeno] *células reticulares epiteliais*.

A diferença não é um detalhe de nomenclatura. Essas células têm *origem epitelial*, não conjuntiva; ligam-se umas às outras por *desmossomos* (as junções típicas de epitélio) e formam uma rede tridimensional viva, e não uma trama de fibras de colágeno. Além de sustentar, elas *produzem hormônios* (as timosinas), que estimulam o amadurecimento dos linfócitos T. Ou seja, o estroma do timo não é só andaime: é andaime que ensina. Por isso, no timo, quem forma o arcabouço são células, e não fibras reticulares como nos outros órgãos linfoides.

Feita a distinção do estroma, o parênquima é mais simples. As células que fazem a função do órgão — os linfócitos T em maturação — são os *timócitos*. #termo-nota[timócito][linfócito T em processo de maturação dentro do timo; compõe o parênquima do órgão] Eles compõem o parênquima, ocupam sobretudo o córtex denso, e são justamente as células que a rede epitelial abraça, nutre e testa. Não caia na inversão: timócito é *parênquima* (a função); célula reticular epitelial é *estroma* (o suporte).

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-28.png",
  largura: 55%,
  legenda: [O arranjo das células reticulares epiteliais (*epithelio-reticular cells*): seus prolongamentos se tocam por desmossomos e formam uma rede que envolve os timócitos (*T lymphocytes*). É essa rede epitelial — não fibras de colágeno — que dá estrutura ao timo.])

#subtopico("2.4 A barreira hematotímica: uma sala de aula isolada")

Educar o linfócito T exige um ambiente protegido, e o timo constrói isso literalmente. No córtex existe uma *barreira hematotímica* — uma barreira entre o *sangue* e o *timo* que impede antígenos circulantes de alcançarem os timócitos imaturos. #termo-nota[barreira hematotímica][conjunto de estruturas que isola o córtex do timo do sangue, protegendo os timócitos imaturos do contato prematuro com antígenos] Pense nela como uma sala de aula com a porta filtrada: os alunos (timócitos) precisam ser testados contra as moléculas do próprio corpo em paz, sem serem bombardeados por antígenos estranhos vindos do sangue, o que atrapalharia a seleção.

O detalhe que precisa ficar gravado é *onde* essa barreira existe: exclusivamente no *córtex*. A medula não é isolada — e faz sentido, porque a medula é onde o linfócito T *já maduro* aguarda para cair na circulação e ir trabalhar; ele já passou pelo teste e não precisa mais de proteção. Então: barreira no córtex (aluno em formação, protegido); medula sem barreira (formado, pronto para sair). Guarde essa localização — ela é uma armadilha frequente.

#subtopico("2.5 O corpúsculo de Hassall, a involução e a assinatura do timo")

Na medula do timo aparece uma estrutura que é a *assinatura histológica* do órgão — a pista que permite reconhecê-lo na lâmina. É o #termo-nota[corpúsculo de Hassall][estrutura da medula do timo formada por células reticulares epiteliais degeneradas dispostas em camadas concêntricas acidófilas; assinatura histológica do órgão] *corpúsculo tímico*, ou *corpúsculo de Hassall*: um agregado de células reticulares epiteliais degeneradas ou em involução, dispostas em *camadas concêntricas* como uma cebola, com aspecto acidófilo (rosado). Nenhum outro órgão linfoide tem essa estrutura. Não a confunda com um nódulo linfático: o corpúsculo de Hassall é feito de células epiteliais em camadas, sem linfócitos B e sem centro germinativo; o nódulo é uma bola de linfócitos B. Além de identificar o órgão, o corpúsculo parece auxiliar na formação dos linfócitos T reguladores (Treg), que aprendem ali a conter respostas contra o próprio corpo.

Uma última particularidade do timo é temporal. Diferente do que a intuição sugere, o timo *não cresce* ao longo da vida — ele *involui*. É grande e ativo na infância, atinge o auge perto da puberdade e depois regride progressivamente, sendo substituído por tecido adiposo. No idoso, resta apenas uma linfopoiese T residual. Isso explica por que a educação de novos linfócitos T é intensa na criança e cada vez mais escassa com a idade — um dado que reaparece quando se discute imunidade no envelhecimento.

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-29.png",
  largura: 55%,
  legenda: [Medula do timo com o corpúsculo de Hassall (à esquerda, estrutura clara em camadas concêntricas). Ao redor, os núcleos escuros dos timócitos. Ver um corpúsculo de Hassall = você está olhando um timo. É o diagnóstico diferencial do órgão.])

#confusao-prevista(
  titulo: "O estroma do timo não é célula reticular comum",
  aluno_acha: [aluno acha que o arcabouço do timo é feito de células reticulares que produzem fibras reticulares, como nos outros órgãos linfoides],
  mecanismo: [no timo o estroma é de células reticulares *epiteliais* — origem epitelial, unidas por desmossomos, que produzem hormônios e formam a rede *elas mesmas*, sem fibra de colágeno como andaime. Por isso a barreira hematotímica e o corpúsculo de Hassall (feito dessas mesmas células degeneradas) são exclusivos do timo.],
)

#mini-resumo[Timo = escola do linfócito T. Estroma de células reticulares *epiteliais* (com desmossomos e hormônios), parênquima de timócitos. Barreira hematotímica só no córtex; corpúsculo de Hassall na medula é a assinatura do órgão. O timo involui com a idade.]

#parte-title("PARTE III — Órgãos linfoides secundários: onde a resposta acontece")

#subtopico("3.1 O linfonodo: o filtro da linfa")

Os órgãos linfoides secundários são onde o linfócito já educado encontra o antígeno e monta a resposta. O primeiro é o *linfonodo* (ou gânglio linfático), e sua função define tudo: ele *filtra a linfa*. A linfa é o líquido que escorre dos tecidos para dentro dos vasos linfáticos; antes de retornar ao sangue, ela passa por linfonodos que a peneiram em busca de antígenos. Um ponto para não errar nunca: *linfonodo filtra linfa, não sangue* — quem filtra sangue é o baço, e trocar os dois é o engano mais comum da aula.

A arquitetura do linfonodo serve a esse fluxo. Ele tem uma *cápsula* de conjuntivo, um *córtex* externo, uma *medula* interna e um *hilo* (a reentrância por onde passam vasos). A linfa entra por *vários vasos aferentes* na convexidade, atravessa o órgão sendo filtrada e sai por um *único vaso eferente* no hilo — muitos entram, um sai, concentrando a linfa já limpa. Por dentro, a linfa corre por *seios*: primeiro o *seio subcapsular* (logo abaixo da cápsula), depois os *seios peritrabeculares*, e por fim os *seios medulares*. Esses seios são o arranjo *frouxo* da PARTE I — canais forrados de macrófagos fixos que fagocitam o que a linfa traz.

Agora a organização das células livres, que é onde mora a lógica funcional. No *córtex* estão os *nódulos linfáticos*, com seus centros germinativos — e nódulo, você já sabe, é território de *linfócito B*. Logo abaixo, numa faixa chamada *região paracortical* (ou paracórtex), estão os *linfócitos T*; por isso o paracórtex é chamado de *área timo-dependente* — ela depende do timo, que fabricou aqueles T. É no paracórtex que ficam as #termo-nota[vênula de endotélio alto][vênula do paracórtex, de células endoteliais cúbicas altas, por onde os linfócitos do sangue entram no linfonodo] *vênulas de endotélio alto*, vasos de parede cúbica por onde os linfócitos *do sangue* atravessam para dentro do linfonodo. Vale fixar: o linfócito entra no linfonodo pelo *sangue*, através dessas vênulas no paracórtex — não pela linfa aferente. Finalmente, na *medula* do linfonodo estão os *cordões medulares* (arranjo denso), ricos em plasmócitos que despejam anticorpo na linfa que está saindo. Assim se fecha a recirculação: o linfócito entra pelo sangue, patrulha o linfonodo, e volta à circulação pela linfa eferente.

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-39.png",
  largura: 72%,
  legenda: [O linfonodo em corte. Vários vasos aferentes entram pela periferia; a linfa atravessa córtex (nódulos de B), paracórtex (T) e medula, e sai por um único eferente no hilo, junto com artéria e veia. A convergência muitos-aferentes → um-eferente é a marca do órgão que concentra a linfa filtrada.])

#figura-lateral("/figuras/histo-11-orgaos-linfaticos/slide-40.png",
  lado: "right",
  largura-figura: 42%,
  texto: [Quando precisar reconhecer um linfonodo na lâmina, procure o *seio subcapsular*: aquele espaço claro logo abaixo da cápsula, entre ela e o córtex denso de linfócitos, por onde a linfa aferente se espalha antes de filtrar. Esse seio abaixo da cápsula é o *diagnóstico diferencial do linfonodo* — o baço não o tem, porque não recebe linfa. É a mesma estratégia de leitura que usamos com o corpúsculo de Hassall no timo: uma estrutura, um órgão.],
  legenda: [Seio subcapsular: a assinatura do linfonodo.])

#subtopico("3.2 O baço: o filtro do sangue")

O baço aplica ao *sangue* exatamente a lógica que o linfonodo aplica à linfa — por isso vale abrir por essa comparação. Ele *filtra o sangue*, e uma consequência estrutural cai direto dessa função: o baço *não tem vasos linfáticos aferentes*, porque não recebe linfa. O sangue entra pela *artéria esplênica*, que se ramifica até virar a *artéria central*, e é em torno dessa artéria que todo o tecido linfoide do baço se organiza.

O baço tem cápsula e *trabéculas* (septos de conjuntivo que entram a partir da cápsula), e dois tipos de "polpa" que não podem ser invertidos. A *polpa branca* é o tecido linfoide propriamente dito, e se arruma ao redor da artéria central em dois compartimentos: a *bainha linfoide periarteriolar* — #sigla("PALS", [bainha linfoide periarteriolar — *periarteriolar lymphoid sheath*, manguito de linfócitos T em volta da artéria central do baço]) PALS, um manguito de *linfócitos T* envolvendo diretamente a artéria — e, encostados nela, os *nódulos linfáticos* de *linfócitos B*. Note o paralelo perfeito com o linfonodo: T em volta do vaso, B em nódulo — mudam os nomes, não a lógica de separar os territórios. A *polpa vermelha* é o compartimento do sangue: feita de *cordões esplênicos* (os #termo-nota[cordões de Billroth][cordões da polpa vermelha do baço, feitos de malha reticular e macrófagos, onde hemácias velhas são reconhecidas e removidas] *cordões de Billroth*, malha reticular cheia de macrófagos) e de *capilares sinusóides* repletos de hemácias. É na polpa vermelha que hemácias velhas ou defeituosas são reconhecidas e removidas — o baço é o coador que aposenta hemácias gastas.

A circulação amarra os dois: o sangue chega pela artéria central, banha a polpa branca (onde os linfócitos vigiam o que passa), segue para a polpa vermelha e é devolvido à veia. Parte desse trajeto é *fechada* (sangue direto nos sinusóides) e parte é *aberta* (sangue jogado nos cordões, obrigado a se espremer de volta para dentro dos sinusóides — e é nesse aperto que a hemácia velha, rígida, fica para trás e é fagocitada).

#figura-nebli("/figuras/histo-11-orgaos-linfaticos/slide-44.png",
  largura: 72%,
  legenda: [A circulação do baço. A artéria central corre dentro da polpa branca, cercada pela PALS (linfócitos T) e pela periferia de linfócitos B. Ao redor, a polpa vermelha com seus sinusóides. A artéria dentro do tecido linfoide é a chave do órgão.])

#figura-lateral("/figuras/histo-11-orgaos-linfaticos/slide-45.png",
  lado: "left",
  largura-figura: 42%,
  texto: [Na polpa vermelha, o detalhe da filtragem: os *cordões esplênicos* (cheios de macrófagos) ficam entre os *sinusóides*. Na circulação *aberta*, o sangue é lançado no cordão e precisa se espremer de volta para dentro do sinusóide, passando por frestas estreitas entre as células que o forram. A hemácia jovem e flexível passa; a velha e enrijecida não passa e é devorada pelo macrófago. A estrutura *é* o mecanismo do controle de qualidade das hemácias.],
  legenda: [Cordão esplênico e sinusóide: onde a hemácia velha fica presa.])

Para reconhecer o baço na lâmina, a pista é a imagem da polpa branca: um *nódulo linfático com uma artéria central* atravessando-o. Nenhum outro órgão tem uma artéria correndo dentro do tecido linfoide desse jeito — no linfonodo, os nódulos não têm artéria central. Fecha-se assim a tríade de leitura da aula: corpúsculo de Hassall aponta o timo, seio subcapsular aponta o linfonodo, e nódulo com artéria central aponta o baço.

#figura-lateral("/figuras/histo-11-orgaos-linfaticos/slide-48.png",
  lado: "right",
  largura-figura: 45%,
  texto: [O diagnóstico diferencial do baço: um nódulo (polpa branca) com a *artéria central* atravessando-o, cercado pela polpa vermelha. Ver a artéria dentro do tecido linfoide = baço.],
  legenda: [Baço: nódulo com artéria central.])

#atencao-box("Não inverta o filtro nem as polpas", [
  Dois enganos custam caro aqui. Primeiro: *linfonodo filtra linfa; baço filtra sangue* — o baço nem sequer recebe vasos linfáticos aferentes, o sangue entra pela artéria esplênica. Segundo: *polpa branca é tecido linfoide* (PALS de T + nódulo de B + artéria central), enquanto *polpa vermelha é o sangue* (cordões de Billroth + sinusóides). Trocar as polpas inverte completamente a leitura da lâmina.
])

#conclusao-box[
  Três órgãos, uma única gramática. Em todos eles, o tecido linfoide se monta sobre o mesmo par que abriu este resumo: *células fixas* formam a malha de sustentação e o filtro (reticulares e macrófagos no linfonodo e no baço; a rede epitelial no timo), enquanto *células livres* — os linfócitos — fazem a resposta imune propriamente dita. O que distingue um órgão do outro é apenas *qual líquido* ele processa e *como separa* seus territórios de linfócito. O timo educa o T num ambiente isolado do sangue (barreira hematotímica no córtex) e o marca com o corpúsculo de Hassall. O linfonodo filtra a linfa, colocando B nos nódulos do córtex e T no paracórtex timo-dependente, com o seio subcapsular como assinatura. O baço filtra o sangue, repetindo a separação B/T ao redor da artéria central da polpa branca, e usa a polpa vermelha para aposentar hemácias velhas.

  Esse desenho tem consequência clínica direta. Como o baço é o grande filtro do sangue e um posto avançado de resposta a bactérias que circulam nele, um paciente que perde o baço (esplenectomia) fica perigosamente vulnerável a *bactérias encapsuladas* — sem o filtro esplênico e sem os macrófagos da polpa vermelha para capturá-las, uma infecção por esses germes pode evoluir para uma sepse fulminante. Do mesmo modo, um linfonodo aumentado e doloroso que você palpa numa infecção nada mais é do que este órgão trabalhando: seus centros germinativos de linfócitos B se expandindo em plena resposta.

  Guardada a arquitetura, o próximo passo é entrar nas moléculas: *como* exatamente o linfócito reconhece o antígeno, como o anticorpo é produzido e como a resposta é regulada — a fisiologia da imunidade que estes órgãos hospedam, e que você verá a seguir.
]
