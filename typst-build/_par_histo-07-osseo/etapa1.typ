#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Cartilagem e osso são tecidos irmãos: mesma origem mesenquimal, mesma lógica de "célula + matriz abundante", mesma família de moléculas. A diferença que separa um do outro cabe numa palavra — mineralização. Quando a matriz extracelular deixa de ser um gel hidratado e passa a ser uma fase sólida endurecida por cristais de fosfato de cálcio, o tecido ganha capacidade nova: aguentar carga sem deformar. Esse é o passo histológico que permite ao vertebrado ter esqueleto rígido em vez de molde flexível. Neste resumo vamos sair da ideia ingênua de que "osso é cartilagem dura" e construir, passo a passo, a noção de que osso é um tecido vivo, vascularizado, em remodelação contínua, com três tipos celulares de origens distintas que se equilibram para construir e desmontar matriz mineralizada ao longo da vida inteira.
]

#parte-title("PARTE I — Identidade e composição do tecido ósseo", primeira: true)

#subtopico("1.1 De onde vem e por que importa")

No resumo anterior fechamos a cartilagem como conjuntivo especializado de matriz hidratada, avascular, que sustenta tensões mas não suporta compressão prolongada sem colapsar. O osso resolve exatamente esse limite. É também um conjuntivo especializado, derivado do mesênquima, mas com uma matriz extracelular#sigla("MEC", [matriz extracelular — conjunto de moléculas que a célula secreta para o espaço fora dela]) #emph[mineralizada] — endurecida pela deposição de cristais de hidroxiapatita sobre as fibras de colágeno. Essa mineralização muda quatro coisas de uma vez: a matriz passa a ser rígida em compressão, deixa de permitir difusão de moléculas pelo seu interior, vira reservatório de íons cálcio e fosfato, e exige células especializadas para ser construída, mantida e desmontada.

#figura-nebli("/figuras/histo-07-osseo/slide-04.png",
  largura: 60%,
  legenda: [As funções clássicas do tecido ósseo: sustentação mecânica do corpo, proteção de órgãos internos (crânio, costelas, coluna) e reservatório regulador de cálcio e fosfato sanguíneos. As três decorrem da mesma propriedade — matriz mineralizada.])

A partir dessa propriedade central, todas as funções do osso seguem. A sustentação mecânica do corpo vem da rigidez à compressão. A proteção de cérebro, medula espinhal, coração e pulmões depende dessa mesma rigidez aplicada como caixa. A reserva metabólica de cálcio e fosfato — fundamental para regular calcemia sanguínea, contração muscular, coagulação e excitabilidade neuronal — depende da matriz ter cristais que podem ser dissolvidos sob demanda. E o papel hematopoético dos ossos longos do adulto, embora não seja função do tecido ósseo propriamente dito, depende da arquitetura esponjosa que ele forma para abrigar a medula. Tudo volta para mineralização da matriz.

#mini-resumo[Osso é conjuntivo especializado, derivado do mesênquima, com MEC mineralizada por hidroxiapatita. Dessa propriedade central nascem as funções de sustentação, proteção e reserva de cálcio/fosfato.]

#subtopico("1.2 A marca: matriz mineralizada como solução mecânica")

Em cartilagem, a matriz aguenta compressão por estar hidratada — proteoglicanos atraem água por osmose, o gel inchado funciona como esponja que comprime e descomprime. Esse mecanismo tem teto: água é incompressível mas o gel pode ser espremido até um limite, e a difusão de nutrientes pelo seu interior limita a espessura útil. O osso resolve o mesmo problema por caminho oposto. Em vez de prender água, deposita um cristal duro. Cristais de hidroxiapatita preenchem o espaço entre fibras de colágeno e formam uma fase sólida que não se deforma sob carga. A consequência é dupla: o tecido aguenta peso sem espremer (vantagem mecânica), mas perde permeabilidade interna a moléculas (desvantagem nutricional, resolvida por uma rede vascular interna que veremos adiante).

#confusao-prevista(
  titulo: "Matriz óssea calcificada não é cartilagem calcificada",
  aluno_acha: [aluno acha que mineralizar cartilagem é "virar osso"],
  mecanismo: [matriz óssea tem colágeno #emph[tipo I] em feixes orientados, com hidroxiapatita depositada sobre o colágeno desde o início. Cartilagem calcificada é matriz cartilaginosa (colágeno II + proteoglicanos) que recebeu mineral em cima, sem reorganizar. São duas matrizes quimicamente distintas — a calcificação da cartilagem é etapa preparatória para que o osso a substitua, não conversão de uma na outra.],
)

A solução mecânica do osso traz junto uma consequência que muda a fisiologia toda. Como a matriz mineralizada é impermeável a difusão de O₂ e glicose, a célula que ficar enterrada nela morre — a menos que tenha um sistema interno de canais para se comunicar com vasos. Por isso o osso é altamente vascularizado por dentro (canais de Havers e de Volkmann) e por isso suas células maduras (osteócitos) ficam conectadas por prolongamentos finos dentro de canalículos. A arquitetura microscópica que vamos detalhar na PARTE III é resposta direta à escolha de mineralizar a matriz.

#subtopico("1.3 Matriz inorgânica e orgânica: concreto armado biológico")

A matriz óssea tem duas frações que cumprem funções complementares. A fração inorgânica responde por 50-60% do peso seco da matriz e é a fase que dá #emph[dureza] e resistência à compressão. A fração orgânica responde por 40-50% e dá #emph[flexibilidade] e resistência à tração. Quando atuam juntas, o tecido aguenta compressão sem esmagar e aguenta tração sem rachar — exatamente o comportamento mecânico do concreto armado, em que o concreto (fase mineral) resiste a compressão e a armadura de aço (fase orgânica de fibras) resiste a tração. Sem mineral, o osso fica mole como tendão; sem colágeno, fica quebradiço como giz.

#figura-nebli("/figuras/histo-07-osseo/slide-10.png",
  largura: 60%,
  legenda: [Associação hidroxiapatita + colágeno na matriz óssea. Mineral sozinho seria quebradiço; colágeno sozinho seria flexível demais. Juntos, dureza e resistência à tração coexistem — a lógica do concreto armado.])

A fração inorgânica é dominada por #termo-nota[hidroxiapatita][Ca₁₀(PO₄)₆(OH)₂, sal mineral que confere dureza à matriz óssea, depositado em cristais sobre fibras de colágeno] — cristais com fórmula Ca₁₀(PO₄)₆(OH)₂, depositados em forma de placas ou agulhas finas sobre as fibras de colágeno. Junto da hidroxiapatita aparecem íons em quantidades menores (magnésio, sódio, citrato). Cada cristal tem ao redor uma capa de hidratação — uma camada fina de água que permite troca iônica com o líquido intersticial. Essa capa é o que torna o reservatório ósseo de cálcio metabolicamente útil: íons entram e saem do cristal por difusão na água da capa, e quando o sangue precisa de cálcio, a remoção do cristal pode ser feita sem desmontar a matriz inteira.

A fração orgânica é dominada por colágeno do tipo I (90% da fração orgânica), com pequena quantidade de tipo V. Diferente do colágeno II da cartilagem, o tipo I forma feixes grossos, orientados, paralelos no osso lamelar — é o que dá direção mecânica preferencial à matriz. Os outros 10% da fração orgânica são proteínas não-colagenosas (osteocalcina, osteopontina, sialoproteína óssea, fosfatase alcalina) que organizam a nucleação dos cristais de hidroxiapatita e regulam crescimento e remodelação. Essas proteínas funcionam como sinalizadores — dizem ao osteoblasto onde, quando e quanto mineral depositar.

#clinica-box("Osteomalácia e raquitismo",
  [Quando falta vitamina D, a absorção intestinal de cálcio e fosfato cai. O osteoblasto continua secretando matriz orgânica (osteóide), mas não consegue mineralizá-la — falta substrato. O resultado é osso mole, deformável, doloroso à compressão. Em criança (raquitismo), as placas epifisárias ficam alargadas e os ossos longos se curvam sob peso. Em adulto (osteomalácia), o esqueleto perde rigidez e dor difusa surge nas regiões de carga. O tratamento devolve vitamina D — o osteoblasto retoma a mineralização do osteóide acumulado.])

#mini-resumo[Matriz óssea = inorgânica (50-60%, hidroxiapatita) + orgânica (40-50%, colágeno I em feixes orientados + proteínas não-colagenosas). Dureza vem do mineral, resistência à tração vem do colágeno. A combinação é concreto armado biológico.]

#subtopico("1.4 Periósteo e endósteo: fontes de osteoblasto novo")

A cartilagem tem pericôndrio cobrindo sua superfície externa. O osso tem #termo-nota[periósteo][bainha de conjuntivo denso que reveste a superfície externa do osso, com camada osteogênica interna que fornece osteoblastos] cobrindo a superfície externa e #termo-nota[endósteo][camada celular fina que reveste cavidades internas do osso — canal medular, canais de Havers e Volkmann, trabéculas do esponjoso] cobrindo a superfície interna (canal medular, trabéculas do esponjoso, paredes dos canais de Havers e Volkmann). Os dois cumprem função análoga ao pericôndrio: bainha de conjuntivo com células progenitoras que repõem osteoblasto durante crescimento e reparo.

#figura-nebli("/figuras/histo-07-osseo/slide-45.png",
  largura: 70%,
  legenda: [Periósteo em duas camadas. A externa (fibrosa) contém colágeno tipo I, fibroblastos e vasos sanguíneos que penetram pelos canais de Volkmann. A interna (osteogênica) contém células osteoprogenitoras capazes de virar osteoblastos — é a fonte de células para crescimento em espessura e reparo de fratura.])

O periósteo tem duas camadas. A externa, fibrosa, é rica em colágeno tipo I e fibroblastos, e por ela passam os vasos sanguíneos e nervos que vão alimentar e inervar o osso. A interna, osteogênica, contém células osteoprogenitoras — descendentes diretas do mesênquima que mantêm capacidade de virar osteoblasto sob demanda. A ancoragem do periósteo ao osso é feita por #termo-nota[fibras de Sharpey][feixes de colágeno tipo I que atravessam do periósteo (ou tendão) para dentro da matriz óssea cortical, ancorando a bainha ao osso], feixes de colágeno I que atravessam do periósteo para dentro da matriz cortical e ficam parcialmente mineralizados. Tendões e ligamentos que se inserem no osso usam o mesmo mecanismo — suas fibras de colágeno se tornam fibras de Sharpey ao entrar na cortical.

O endósteo é mais simples — uma camada única de células osteogênicas achatadas. Mas cumpre o mesmo papel fundamental: é a fonte interna de osteoblasto novo. Durante o crescimento em espessura, o periósteo deposita matriz nova na superfície externa enquanto o endósteo, do lado de dentro, reabsorve cortical antiga — assim o canal medular se mantém proporcional ao diâmetro externo do osso. No reparo de fratura, é dos dois lados (periósteo por fora, endósteo por dentro) que vem a maior parte dos osteoblastos do calo ósseo. Sem essas duas camadas, o osso não cicatriza.

#confusao-prevista(
  titulo: "Periósteo e endósteo não são só revestimento",
  aluno_acha: [aluno acha que são bainhas passivas, sem papel funcional],
  mecanismo: [as duas camadas têm #emph[células osteoprogenitoras] ativas — fonte permanente de osteoblasto novo durante toda a vida. Periósteo nutre e protege a superfície externa; endósteo controla a remodelação interna. Sem eles, o osso não cresce em espessura e não cicatriza fratura.],
)

#parte-title("PARTE II — As três células e o balanço dinâmico")

#subtopico("2.1 Três células com origens distintas para uma função integrada")

A cartilagem tinha uma só linhagem celular em duas idades: condroblasto jovem virando condrócito maduro. O osso tem #emph[três] tipos celulares distintos, e dois deles nem têm a mesma origem embrionária. Osteoblasto e osteócito formam uma linhagem só — derivam do mesênquima, descendentes diretos da célula osteoprogenitora do periósteo e endósteo, mesma linhagem do condroblasto. Mas o osteoclasto vem de outro lugar: linhagem hematopoética, descendente de progenitor de monócito-macrófago, vindo da medula óssea pelo sangue. O resultado é um tecido em que a célula que constrói matriz e a célula que reabsorve matriz são geneticamente parentes distantes — e essa separação de origens vai ser central para entender como o equilíbrio é regulado.

#figura-nebli("/figuras/histo-07-osseo/slide-11.png",
  largura: 70%,
  legenda: [As três células do tecido ósseo: osteoblasto (formador, derivado mesenquimal), osteócito (osteoblasto aprisionado na matriz) e osteoclasto (reabsorvedor, derivado hematopoético). Apesar do tecido único, são duas linhagens embrionárias separadas trabalhando juntas.])

A consequência funcional dessa separação é forte. Sinais que regulam um lado da equação não precisam, em princípio, afetar o outro — pode-se acelerar formação sem mexer em reabsorção, ou inibir reabsorção sem mexer em formação. Mas na prática há acoplamento: o osteoblasto, vindo do mesênquima, fala com o osteoclasto, vindo da medula, através de moléculas-chave que vamos detalhar em 2.5 (o eixo RANK/RANKL/OPG). Esse acoplamento é o que permite manter o saldo de matriz óssea aproximadamente zero ao longo da vida adulta — para cada miligrama desmontado, outro miligrama é depositado. Quando o acoplamento desregula (na menopausa, no hipertireoidismo, no uso crônico de corticoide), o saldo vira negativo e aparece osteoporose.

#subtopico("2.2 Osteoblasto: o que fabrica a matriz")

O osteoblasto é a célula formadora de matriz, derivada das células osteoprogenitoras do periósteo e endósteo. Quando entra em atividade, fica em fila — uma camada única de células justapostas na superfície onde o osso está crescendo, parecida com uma fileira de operários de uma obra. Visualmente é cúbica ou prismática, citoplasma intensamente basofílico (denuncia retículo endoplasmático rugoso abundante e ribossomos livres — a célula está fabricando muita proteína), núcleo deslocado para o polo oposto à matriz que ela está produzindo.

#figura-nebli("/figuras/histo-07-osseo/slide-14.png",
  largura: 55%,
  legenda: [Osteoblastos formando fila na superfície de matriz óssea em formação. Citoplasma basofílico denuncia o RER ativo. O núcleo fica no polo distante da matriz, e o produto secretado (osteóide) se acumula no polo oposto, em contato com a superfície óssea preexistente.])

O que o osteoblasto secreta é #termo-nota[osteóide][matriz óssea recém-secretada pelo osteoblasto, ainda não-mineralizada — colágeno I + proteínas não-colagenosas; fica mineralizada em ~10 dias] — matriz orgânica ainda não-mineralizada, composta de colágeno tipo I, proteoglicanos e proteínas não-colagenosas (osteocalcina, osteopontina, sialoproteína óssea). O osteóide forma uma camada fina (~10 µm) entre o osteoblasto e o osso já mineralizado. Aproximadamente 10 dias depois da secreção, a hidroxiapatita começa a se depositar sobre essa matriz — processo conhecido como nucleação mineral. A fosfatase alcalina do osteoblasto cliva pirofosfato (que inibe a cristalização) e libera fosfato, criando condições para que o cristal se forme. As proteínas não-colagenosas servem como sítios de nucleação — definem onde, exatamente, o primeiro cristal vai aparecer.

Outro detalhe importante: osteoblastos vizinhos se comunicam por #emph[junções comunicantes] (gap junctions). Isso permite que o grupo deposite matriz de forma coordenada — não cada um produzindo no seu canto, mas como camada sincronizada. Quando a deposição termina numa região, o osteoblasto tem três destinos possíveis: (1) ficar aprisionado pela matriz que produziu e virar osteócito; (2) achatar-se sobre a superfície e virar célula de revestimento ósseo (inativa, em repouso, pronta para reativar); (3) entrar em apoptose. Cada destino corresponde a um estado funcional diferente da superfície óssea — crescimento, repouso ou término.

#mini-resumo[Osteoblasto = formador de matriz, vindo do mesênquima, em fila na superfície. Secreta osteóide (colágeno I + proteínas não-colagenosas), que depois nuclea hidroxiapatita. Termina como osteócito, célula de revestimento ou apoptose.]

#subtopico("2.3 Osteócito: a célula que sente o esforço")

Quando o osteoblasto fica aprisionado pela própria matriz que secretou, ele muda — reduz citoplasma, desliga grande parte da síntese, ganha prolongamentos finos e vira #termo-nota[osteócito][célula óssea madura aprisionada em lacuna, conectada por canalículos a vizinhos, faz mecanotransdução e mantém matriz local]. Ocupa um espaço escavado na matriz chamado lacuna. Da lacuna, emite prolongamentos finos por canais ainda mais finos, chamados canalículos, que se conectam com prolongamentos de outros osteócitos vizinhos. Essa rede tridimensional — lacunas + canalículos + prolongamentos com junções comunicantes nas pontas — transforma cada porção de matriz óssea numa unidade vigiada e mantida por células interconectadas.

#figura-nebli("/figuras/histo-07-osseo/slide-24.png",
  largura: 70%,
  legenda: [Osteócitos em lacunas, conectados por prolongamentos que correm em canalículos da matriz. A rede é tridimensional e atravessa o ósteon inteiro, conectando célula a vaso central por uma cadeia de 4-7 osteócitos.])

A distância máxima entre um osteócito e um vaso sanguíneo é cerca de 100 µm — limite imposto pela difusão de O₂ e nutrientes através dos canalículos. Por isso o ósteon não pode ser muito mais grosso do que ~200 µm de diâmetro, com vaso no centro: cada osteócito da periferia precisa estar a no máximo 100 µm do canal central, com a difusão acontecendo pelos canalículos preenchidos por líquido intersticial.

A função do osteócito vai muito além de "manutenção passiva". Ele faz #emph[mecanotransdução]: percebe deformações mecânicas da matriz (curvaturas, compressões, microestresse) e converte essa informação em sinais bioquímicos que regulam remodelação local. Quando o esforço mecânico aumenta numa região, os osteócitos liberam sinais que recrutam osteoblastos para depositar mais matriz ali (osso se adapta engrossando onde é solicitado). Quando o esforço cai (imobilização, microgravidade), o sinal vai no sentido oposto e ativa reabsorção. É a chamada lei de Wolff em base celular — o esqueleto se molda à demanda mecânica, e quem ouve a demanda são os osteócitos.

#confusao-prevista(
  titulo: "Osteócito não é osteoblasto aposentado",
  aluno_acha: [aluno acha que osteócito é osteoblasto velho, sem função],
  mecanismo: [é a mesma linhagem, mas com #emph[função nova]. O osteoblasto fabrica matriz; o osteócito faz mecanotransdução, mantém a matriz local e dura até 25 anos. Não é "célula passiva enterrada" — é a parte do osso que ouve o que o corpo está fazendo e direciona a remodelação.],
)

#mini-resumo[Osteócito = osteoblasto aprisionado, em lacuna conectada por canalículos. Faz mecanotransdução (lê esforço mecânico → sinal bioquímico que ajusta remodelação) e mantém a matriz local. Vida útil de até 25 anos.]

#subtopico("2.4 Osteoclasto: como se desmonta osso")

O osteoclasto é uma célula completamente diferente das outras duas. Origem hematopoética — fusão de vários progenitores de monócito-macrófago em uma só célula gigante, multinucleada (5 a 50 núcleos), com diâmetro de até 100 µm. Função única no organismo: reabsorver matriz óssea mineralizada. Para isso, é polarizada — diferente do osteoblasto cúbico simétrico, o osteoclasto tem dois polos morfologicamente distintos, e essa polaridade é central para entender como ele dissolve um tecido tão duro.

#figura-lateral("/figuras/histo-07-osseo/slide-34.png",
  lado: "right",
  largura-figura: 42%,
  texto: [O osteoclasto polarizado em ação. Na face voltada para o osso, dois compartimentos: a zona de vedação (um anel de actina ancorado por integrinas, que sela hermeticamente a borda da lacuna de Howship), e a borda franzida (membrana intensamente pregueada, com canais e bombas, que faz o trabalho de dissolver mineral e digerir colágeno). Na face oposta, basolateral, sai o material reabsorvido em vesículas para o líquido intersticial e dali para o sangue.],
  legenda: [Osteoclasto polarizado sobre a lacuna de Howship.])

A primeira coisa que o osteoclasto faz ao atingir o osso é selar uma área da superfície. A célula encosta no osso pela borda externa e organiza um anel de filamentos de actina ancorados por integrinas — essa é a #termo-nota[zona de vedação][região do osteoclasto em contato direto com o osso, selada por um anel de actina ancorado por integrinas; isola a lacuna de reabsorção do meio extracelular]. Dentro desse anel fica isolada uma região do espaço extracelular — a #termo-nota[lacuna de Howship][depressão na superfície óssea onde o osteoclasto reabsorve matriz; espaço selado entre célula e osso onde ocorre a digestão local], uma cavidade rasa entre a célula e o osso onde toda a digestão acontece sem vazamento. É como um operário que pede um isolamento ao redor de uma área antes de demolir.

Dentro da zona vedada, a membrana do osteoclasto vira #emph[borda franzida] — intensamente pregueada, multiplicando muitas vezes a área de superfície. Por essa borda, duas coisas acontecem em sequência. Primeiro, bombas V-ATPase bombeiam H⁺ contra gradiente para dentro da lacuna, acidificando aquela região até pH ~4,5. O ácido dissolve a hidroxiapatita — Ca²⁺ e fosfato saem em solução. Em paralelo, vesículas exocitadas pela borda franzida liberam enzimas proteolíticas, principalmente #emph[catepsina K] e colagenases (MMPs), que digerem o colágeno I exposto após a dissolução do mineral. A sequência é obrigatória: dissolver mineral antes, digerir colágeno depois. Se as enzimas atuassem antes do ácido, o colágeno ainda estaria protegido pelos cristais de hidroxiapatita.

O material dissolvido (Ca²⁺, fosfato, fragmentos de colágeno) é então #emph[transcitado] pela célula — entra pela borda franzida em vesículas endocíticas, atravessa o citoplasma, sai pela face basolateral oposta para o líquido intersticial e dali para o capilar mais próximo. Por isso a calcemia sobe quando a reabsorção é intensa. Quando termina o trabalho local, o osteoclasto se desprende e entra em apoptose. Cada ciclo dura horas a dias; o tecido onde a lacuna foi cavada vai depois ser preenchido por osteoblastos recrutados — é assim que a remodelação se completa.

#atencao-box("A polaridade é o que define o osteoclasto funcional",
  [Sem zona de vedação, o ácido escapa para o tecido e a reabsorção não acontece — o osteoclasto fica "ligado" mas inútil. É exatamente isso que mutações no gene da bomba V-ATPase causam (osteopetrose maligna infantil): osteoclasto multinucleado presente, mas sem capacidade de acidificar a lacuna. O esqueleto fica densamente mineralizado, sem remodelação, e a medula óssea é sufocada — anemia grave e morte precoce.])

#mini-resumo[Osteoclasto = célula gigante multinucleada, origem hematopoética, polarizada. Sela área da superfície (zona de vedação por anel de actina), acidifica a lacuna de Howship (V-ATPase → H⁺ → dissolve hidroxiapatita), digere colágeno (catepsina K), transcita material para o sangue. Termina em apoptose.]

#subtopico("2.5 RANK, RANKL e OPG: o triângulo que decide o saldo")

Três proteínas decidem se o saldo do balanço ósseo do dia vai ser positivo (osso ganha) ou negativo (osso perde). Esse é o eixo mais importante da fisiologia óssea moderna, e é onde a separação de origens das células (osteoblasto = mesênquima, osteoclasto = medula) ganha sentido funcional. O #sigla("RANKL", [receptor activator of nuclear factor kappa B ligand — ligante expresso pelo osteoblasto que ativa osteoclasto via RANK]) é uma proteína produzida pelo #emph[osteoblasto] e expressa na sua superfície ou liberada na MEC. O #sigla("RANK", [receptor activator of nuclear factor kappa B — receptor expresso pelo osteoclasto e pelo seu precursor, ativado pelo RANKL]) é o receptor correspondente, expresso no #emph[osteoclasto] e no seu precursor monocítico. Quando RANKL do osteoblasto se liga ao RANK do precursor osteoclástico, o sinal ativa a diferenciação, a fusão dos progenitores e a ativação da reabsorção.

#figura-nebli("/figuras/histo-07-osseo/slide-39.png",
  largura: 75%,
  legenda: [O eixo RANK/RANKL/OPG. Osteoblasto expressa RANKL (ativa) e OPG (inibe) e decide o saldo da reabsorção. RANKL → osteoclasto ativado, reabsorve matriz. OPG → sequestra RANKL antes que ele encontre RANK, freia reabsorção. Estrogênio aumenta OPG; sua queda na menopausa explica a perda óssea pós-menopausa.])

A terceira proteína do triângulo é a #sigla("OPG", [osteoprotegerina — receptor-armadilha solúvel produzido pelo osteoblasto; liga RANKL e impede ativação do osteoclasto]) — também produzida pelo osteoblasto, mas com função oposta. OPG é um receptor-armadilha: liga RANKL antes que ele encontre o RANK do osteoclasto, e bloqueia o sinal. Quanto mais OPG, mais RANKL sequestrado, menos reabsorção. A razão RANKL/OPG produzida pelo osteoblasto controla, na prática, a quantidade de reabsorção do tecido. É o mesmo grupo de células (mesênquima/osteoblasto) decidindo se vai liberar o gatilho ou o freio.

Esse mecanismo explica diretamente vários fenômenos clínicos. Estrogênio aumenta OPG e reduz RANKL — por isso mulheres pré-menopausa têm reabsorção freada. Na menopausa, o estrogênio cai, OPG cai junto, RANKL fica mais livre, reabsorção acelera e o saldo do balanço fica negativo — aparece osteoporose pós-menopausa. Glicocorticoides aumentam RANKL e reduzem OPG — por isso uso crônico de corticoide causa osteoporose iatrogênica. Hiperparatireoidismo aumenta produção de RANKL pelo osteoblasto via PTH (paratormônio) — por isso a calcemia sobe e o osso fica frágil. O tratamento moderno com denosumabe é um anticorpo monoclonal que neutraliza RANKL — bloqueia o gatilho da reabsorção diretamente, mimetizando a função fisiológica da OPG.

#confusao-prevista(
  titulo: "RANK fica no OSTEOCLASTO, não no osteoblasto",
  aluno_acha: [aluno tende a inverter — coloca RANK no osteoblasto porque o nome lembra "construir"],
  mecanismo: [a regra mnemônica é: o L de #emph[L]igante vem do osteob#emph[L]asto. Quem expressa o ligante (RANKL) e a armadilha (OPG) é o osteoblasto. Quem expressa o receptor (RANK) é o osteoclasto. O sinal nasce no formador e ativa o reabsorvedor — é o formador que decide quanto vai ser desmontado.],
)

#clinica-box("Osteoporose pós-menopausa",
  [O cenário clínico mais comum em ambulatório de endocrinologia. A queda de estrogênio reduz OPG e aumenta RANKL. O resultado é reabsorção descontrolada — osteoclastos cavam mais lacunas e mais profundas; osteoblastos preenchem só parcialmente. A cada ciclo de remodelação, sobra menos matriz que antes. O esqueleto fica fino, trabéculas se afinam, a microarquitetura se desorganiza. Fraturas surgem em locais de baixa carga (vértebra, colo de fêmur, punho). O tratamento moderno usa bisfosfonatos (matam osteoclasto), denosumabe (anti-RANKL) ou teriparatida (estimula osteoblasto), e ataca diretamente o desequilíbrio do triângulo.])

#mini-resumo[Osteoblasto expressa RANKL (gatilho) e OPG (freio); osteoclasto expressa RANK. A razão RANKL/OPG decide o saldo da remodelação. Estrogênio ↑OPG; menopausa ↓estrogênio → ↓OPG → ↑reabsorção → osteoporose. Denosumabe = anti-RANKL terapêutico.]

#parte-title("PARTE III — Tipos, histogênese e regeneração")

#subtopico("3.1 Compacto e esponjoso, lamelar e não-lamelar")

O tecido ósseo é classificado por duas escalas independentes — uma macroscópica, outra microscópica — e o aluno costuma confundi-las. Em escala macro, observada a olho nu ou em microscopia de pequena ampliação, divide-se em #emph[compacto] (denso, sem cavidades visíveis a olho nu) e #emph[esponjoso] (trabeculado, com espaços medulares grandes entre as trabéculas). Em escala micro, observando a organização das fibras de colágeno na matriz, divide-se em #emph[lamelar] (colágeno organizado em camadas paralelas chamadas lamelas) e #emph[não-lamelar] ou primário (colágeno aleatório, sem organização lamelar).

#figura-nebli("/figuras/histo-07-osseo/slide-50.png",
  largura: 70%,
  legenda: [Osso longo em corte: cortical compacta na periferia da diáfise, esponjoso nas epífises e na metáfise, canal medular central. As duas frações cumprem funções complementares — cortical resiste a flexão e torção, esponjoso distribui carga nas articulações e abriga medula hematopoética.])

As duas classificações são ortogonais. No adulto normal, tanto o osso compacto quanto o esponjoso são, em geral, lamelares. O não-lamelar é osso "jovem" — aparece no embrião durante a histogênese, aparece no calo de fratura durante o reparo, e em alguns locais específicos do adulto (alvéolos dentários, suturas cranianas, inserções de tendão). Não-lamelar tem fibras de colágeno aleatórias, menor mineralização, e maior densidade de osteócitos por unidade de matriz — é menos resistente mecanicamente, e por isso é #emph[substituído] por lamelar ao longo do tempo via remodelação.

A escolha macroscópica entre compacto e esponjoso responde a demandas mecânicas distintas. Compacto resiste a flexão e torção — por isso domina a diáfise dos ossos longos, onde o estresse principal é dobramento e rotação. Esponjoso distribui carga e absorve impacto — por isso domina epífises e metáfises (próximas às articulações), corpos vertebrais (que recebem carga axial distribuída) e ossos chatos. Como bônus, as cavidades do esponjoso são onde mora a medula óssea hematopoética no adulto.

#mini-resumo[Compacto/esponjoso = escala macro (densidade). Lamelar/não-lamelar = escala micro (organização). As duas se cruzam: no adulto, compacto e esponjoso são lamelares; não-lamelar é embrionário, de reparo ou de locais especiais.]

#subtopico("3.2 Sistema de Havers: a unidade do osso compacto")

A unidade estrutural do osso compacto lamelar é o #termo-nota[ósteon][unidade estrutural do osso lamelar compacto; canal central com lamelas concêntricas, lacunas com osteócitos e canalículos que conectam ao canal] ou sistema de Havers. Cada ósteon é um tubo cilíndrico vertical, com 4 a 20 lamelas concêntricas de matriz óssea organizadas ao redor de um canal central — o canal de Havers — que contém vaso sanguíneo, nervo amielínico e líquido intersticial. As lamelas se sobrepõem como camadas de uma cebola; entre elas ficam as lacunas com osteócitos, conectadas por canalículos perpendiculares à lamela que correm em direção ao canal central. O resultado é uma estrutura em que cada osteócito está a menos de 100 µm de um vaso, conectado por uma cadeia de prolongamentos.

#figura-nebli("/figuras/histo-07-osseo/slide-58.png",
  largura: 70%,
  legenda: [Sistema de Havers em corte transversal. Canal de Havers central com vaso, lamelas concêntricas ao redor, lacunas com osteócitos entre lamelas, canalículos atravessando perpendicularmente. Cada ósteon mede ~200 µm de diâmetro, e dezenas deles compõem a cortical da diáfise.])

Os ósteons se orientam paralelos ao eixo longo do osso. Para distribuir vasos transversalmente — conectando um ósteon a outro e à superfície externa (periósteo) e interna (endósteo) — existem os #emph[canais de Volkmann], que correm perpendiculares aos canais de Havers. Volkmann atravessa, Havers corre longitudinal. Em corte transversal de diáfise, vê-se Havers central (círculo) e Volkmann conectando lateralmente (traços oblíquos). Essa rede vascular interna é o que diferencia o osso da cartilagem do ponto de vista nutricional — não há difusão a partir de uma superfície, há vaso por dentro.

Entre ósteons, sobram lamelas que não pertencem a nenhum sistema completo — são lamelas intersticiais, restos de ósteons antigos que foram parcialmente reabsorvidos em ciclos passados de remodelação. Na superfície externa e interna da cortical aparecem lamelas circunferenciais, paralelas à superfície, sem canal central. A cortical madura é então um mosaico: ósteons inteiros + lamelas intersticiais + lamelas circunferenciais — registro estratificado de toda a história de remodelação local.

#confusao-prevista(
  titulo: "Ósteon só existe em osso compacto lamelar",
  aluno_acha: [aluno aplica "sistema de Havers" ao esponjoso por inércia],
  mecanismo: [o esponjoso é #emph[trabecular] — uma rede de espigões finos de matriz óssea, sem canal central com vaso e sem lamelas concêntricas. Trabéculas têm lamelas paralelas e ficam nutridas por difusão a partir da medula adjacente. Não há ósteon. A regra: ósteon = compacto lamelar; trabécula lamelar = esponjoso lamelar; ambos são lamelares, mas com geometrias diferentes.],
)

#subtopico("3.3 Duas rotas para virar osso: intramembranosa e endocondral")

Existem dois caminhos histológicos para formar tecido ósseo no embrião e ao longo do crescimento, e os dois usam o mesmo ponto de partida (mesênquima) mas seguem trajetórias diferentes. A primeira rota, #emph[ossificação intramembranosa], vai direto: mesênquima condensa, células viram osteoblasto, osteoblasto deposita matriz, matriz mineraliza. Sem etapa intermediária. É a rota que forma os ossos chatos do crânio (frontal, parietal, partes do occipital e temporal), maxilas superior e inferior, e clavícula. Também é a rota responsável pelo crescimento em #emph[espessura] dos ossos longos durante a vida.

#figura-nebli("/figuras/histo-07-osseo/slide-70.png",
  largura: 70%,
  legenda: [Ossificação intramembranosa. Centro de ossificação primária: mesênquima condensa, células-tronco mesenquimais se diferenciam em osteoblastos sem cartilagem intermediária. Osteoblastos depositam osteóide, que mineraliza, formando ilhotas de osso que se expandem por crescimento aposicional e se fundem.])

A segunda rota, #emph[ossificação endocondral], usa cartilagem como molde. Primeiro o mesênquima condensa e vira cartilagem hialina (um pequeno fêmur cartilaginoso, por exemplo). Depois os condrócitos centrais hipertrofiam (incham), reduzem a matriz cartilaginosa a tabiques finos, mineralizam essa matriz e morrem por apoptose. As cavidades deixadas pelos condrócitos mortos são invadidas por brotos vasculares vindos do periósteo, que trazem junto células osteogênicas. Essas células se diferenciam em osteoblastos e começam a depositar matriz óssea sobre os restos de cartilagem mineralizada — o tecido cartilaginoso vai sendo substituído por tecido ósseo de dentro para fora. Essa é a rota dos ossos longos e curtos (fêmur, tíbia, úmero, falanges, vértebras), e ela continua ativa nas placas epifisárias até cerca de 20 anos, mantendo o crescimento longitudinal.

#figura-nebli("/figuras/histo-07-osseo/slide-76.png",
  largura: 70%,
  legenda: [Ossificação endocondral. Cartilagem hialina (molde) sofre hipertrofia condrocítica, mineralização da matriz cartilaginosa e morte dos condrócitos. Vasos invadem; osteoblastos vindos do periósteo depositam matriz óssea sobre os restos cartilaginosos. O tecido ósseo substitui o cartilaginoso de dentro para fora.])

#confusao-prevista(
  titulo: "Intramembranosa NÃO precisa de cartilagem",
  aluno_acha: [aluno acha que toda ossificação passa por cartilagem],
  mecanismo: [intramembranosa vai #emph[direto] de mesênquima a osso. Endocondral usa cartilagem como molde substituível. São histogêneses #emph[paralelas], não etapas de um mesmo processo. Confunde porque ambas começam em mesênquima — mas só a endocondral cria um intermediário cartilaginoso.],
)

A placa epifisária — disco fino de cartilagem hialina entre epífise e diáfise dos ossos longos em crescimento — é onde a ossificação endocondral continua ativa pós-nascimento. Ela funciona como zona de produção contínua: condrócitos proliferam de um lado (lado epifisário) e hipertrofiam/morrem do outro (lado diafisário), enquanto osteoblastos substituem o que morre. O osso longo cresce longitudinalmente nessa interface, mantendo a placa do mesmo tamanho enquanto a diáfise se alonga. Quando os hormônios sexuais aumentam na puberdade, a proliferação dos condrócitos é frenada, a placa é totalmente substituída por osso, e o crescimento longitudinal termina — isso é o "fechamento das placas epifisárias", definitivo.

#mini-resumo[Duas histogêneses paralelas. Intramembranosa: mesênquima → osso direto (ossos chatos, crescimento em espessura). Endocondral: mesênquima → cartilagem hialina (molde) → osso substituto (ossos longos e curtos, crescimento longitudinal nas placas epifisárias até ~20 anos).]

#subtopico("3.4 Crescimento, remodelação e reparo de fratura")

O osso adulto não é tecido estático. Mesmo depois que as placas epifisárias fecham e o crescimento termina, há remodelação contínua — osteoclastos cavam pequenas regiões, osteoblastos repõem matriz no lugar, em ciclos coordenados que renovam ~10% do esqueleto adulto por ano. A remodelação cumpre três funções centrais. Primeiro, repara microfraturas que o uso normal cria — o osso muito antigo acumula microdano cumulativo e seria frágil sem renovação. Segundo, adapta a arquitetura à demanda mecânica — onde a carga aumenta, há deposição preferencial; onde cai, há reabsorção preferencial (lei de Wolff em base celular, ouvida pelos osteócitos). Terceiro, regula a calcemia — quando o sangue precisa de cálcio, a reabsorção é estimulada por PTH; quando há excesso, a calcitonina freia osteoclasto e o cálcio fica retido na matriz.

O reparo de fratura é um caso particularmente bonito porque #emph[recapitula] a histogênese embrionária. Quando o osso quebra, a sequência de eventos é a seguinte. Primeiro fase o hematoma: vasos do periósteo, do endósteo e do canal medular rompem, e o sangue extravasado coagula no foco — esse coágulo é a matriz provisória onde tudo vai se montar. Em seguida, em 1 a 2 semanas, o hematoma é invadido por macrófagos (que limpam restos), fibroblastos e capilares vindos do periósteo e endósteo — forma-se o calo fibroso, tecido conjuntivo provisório. Em seguida, no calo cartilaginoso (2 a 4 semanas), surge cartilagem hialina substituindo parte do conjuntivo — exatamente como no molde embrionário. Por fim, em 4 a 12 semanas, vem o calo ósseo primário: osteoblastos depositam matriz óssea não-lamelar substituindo a cartilagem (ossificação endocondral local) e também depositando direto sobre as superfícies preservadas (intramembranosa local). Por último, em meses a anos, vem a remodelação para osso lamelar — o calo primário é substituído por ósteons organizados, e o contorno cortical é refeito por osteoclastos e osteoblastos cooperando.

#clinica-box("Fratura em criança vs idoso",
  [Em criança, o periósteo é espesso, bem vascularizado, repleto de células osteoprogenitoras — fraturas frequentemente são incompletas ("em galho verde"), e a consolidação acontece em 4 a 6 semanas com calo robusto. Em idoso, o periósteo afina, a vascularização diminui, a resposta osteoblástica é mais lenta — fraturas demoram 3 a 6 meses para consolidar, e algumas (colo de fêmur, escafoide) podem evoluir para não-consolidação. A diferença está exatamente nas duas camadas (periósteo + endósteo) que vimos em 1.4: quem cicatriza fratura é a célula osteoprogenitora delas, e a abundância dela cai com a idade.])

O crescimento dos ossos longos é o último ponto que fecha esta PARTE. O crescimento em comprimento depende exclusivamente da placa epifisária — endocondral, ativa até ~20 anos. O crescimento em espessura depende do periósteo, que deposita matriz nova na superfície externa enquanto o endósteo reabsorve do lado de dentro — o canal medular se mantém proporcional ao diâmetro externo do osso conforme ele engrossa. As duas operações são simultâneas e coordenadas: a criança cresce em comprimento na placa e em espessura no periósteo, e o adulto, mesmo sem ganhar tamanho, mantém renovação contínua pelos mesmos mecanismos em menor escala.

#conclusao-box[
  Osso é conjuntivo especializado em matriz mineralizada. Essa mineralização resolve o problema mecânico da carga compressiva sustentada — solução oposta à da cartilagem, que aguenta compressão por hidratação. O preço da mineralização é a impermeabilidade interna: o tecido precisa ser vascularizado por dentro (canais de Havers e Volkmann), e suas células maduras precisam ficar conectadas por canalículos para se nutrir. Três linhagens celulares trabalham juntas: osteoblasto (mesênquima) fabrica matriz, osteócito (osteoblasto aprisionado) faz mecanotransdução e mantém matriz, osteoclasto (medula hematopoética) reabsorve matriz. O equilíbrio entre formação e reabsorção é regulado pelo eixo RANK/RANKL/OPG, que parte do osteoblasto e atua sobre o osteoclasto — e é nesse eixo que age toda a fisiologia hormonal (estrogênio, PTH, calcitonina, vitamina D) e a farmacologia moderna (bisfosfonatos, denosumabe, teriparatida). A arquitetura interna se organiza em ósteons no compacto e trabéculas no esponjoso, ambos em geral lamelares no adulto, e a histogênese segue duas rotas paralelas: intramembranosa (direta) e endocondral (via cartilagem-molde), com a última mantendo o crescimento longitudinal pelas placas epifisárias até a puberdade tardia. Quando a fratura acontece, a sequência embrionária se repete em miniatura — hematoma, calo fibroso, calo cartilaginoso, calo ósseo primário, remodelação lamelar — porque o tecido nunca esquece como nasceu.
]
