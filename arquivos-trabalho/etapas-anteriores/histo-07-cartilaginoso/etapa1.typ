#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Cartilagem é um dos tecidos mais estranhos do corpo. Não tem vaso, não tem nervo, não tem linfático. As células ficam presas em pequenas câmaras escavadas na própria matriz que elas secretaram, e mesmo assim o tecido segura tensões mecânicas brutais durante a vida inteira. A pergunta que abre tudo é simples: como um tecido que parece isolado do resto consegue continuar vivo e funcional? A resposta está na matriz. Neste resumo, vamos sair da ideia ingênua de que tecido é "um monte de células" e construir, passo a passo, a noção de que no cartilaginoso o protagonista é o que está fora da célula. Quem entende isso entende por que cartilagem é resistente, por que cresce devagar, por que não cicatriza, e por que precisa ser substituída por osso para virar esqueleto adulto.
]

#parte-title("PARTE I — Identidade do tecido cartilaginoso", primeira: true)

#subtopico("1.1 De onde vem e por que importa")

Na aula passada vimos o tecido conjuntivo geral: células espalhadas numa matriz rica em colágeno e substância fundamental, sustentando e nutrindo os outros tecidos. O cartilaginoso é uma forma especializada desse tecido conjuntivo — mesma origem embrionária (mesoderma), mesma lógica de "célula + matriz abundante", mas com uma diferença que muda tudo: a matriz aqui é tão densa, tão hidratada e tão organizada que vira o componente funcional principal. A célula recua para um papel de manutenção. O tecido passa a ser definido pelo que ela #emph[secretou], não pelo que ela #emph[é].

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-04.png",
  largura: 60%,
  legenda: [Histogênese: ambos os tecidos cartilaginoso e ósseo descendem da mesma linhagem mesenquimal tripoblástica. A escolha entre virar cartilagem ou osso depende de sinais locais — o mesmo precursor que vira condroblasto pode, em outro contexto, virar osteoblasto.])

As funções de cartilagem se resumem a três, e elas seguem da estrutura. Primeiro, suporte de tecidos moles mantendo a forma — orelha, ponta do nariz, traqueia, brônquios. Segundo, revestimento de superfícies articulares facilitando o deslizamento dos ossos — joelho, ombro, quadril, qualquer articulação móvel. Terceiro, formação e crescimento dos ossos longos: o esqueleto fetal é quase todo cartilagem hialina, que vai sendo substituída por osso até a vida adulta, num processo chamado ossificação endocondral. Esse último ponto é importante porque o próximo resumo da disciplina é justamente sobre tecido ósseo — e a ponte entre os dois passa por aqui.

#mini-resumo[Cartilagem é conjuntivo especializado de origem mesodérmica, com três funções que servem ao esqueleto: sustentar a forma, revestir articulações, e moldar os ossos antes da ossificação.]

#subtopico("1.2 A marca registrada: avascular, abundante matriz")

A característica que separa cartilagem de quase todos os outros tecidos do corpo é a #emph[avascularidade]. Não há capilar entrando, não há linfático drenando, não há terminação nervosa dentro do tecido. Some-se a isso uma matriz extracelular#sigla("MEC", [matriz extracelular — conjunto de moléculas que a célula secreta para o espaço fora dela]) que representa 95% do volume do tecido, e a célula vira minoria absoluta. Os 3–5% celulares restantes são condroblastos jovens na borda e condrócitos maduros aprisionados em pequenas câmaras chamadas #termo-nota[lacunas][espaços na matriz cartilaginosa que cada condrócito escava ao secretar MEC ao seu redor].

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-38.png",
  largura: 72%,
  legenda: [Proporção em cartilagem hialina: ~95% matriz extracelular contra ~3-5% células. Dentro da MEC, água é o componente majoritário (60-80%), seguida de colágeno, proteoglicanos e glicoproteínas multiadesivas.])

Essa proporção é a inversão de tudo que se aprende sobre epitélios, onde célula encostada em célula é a regra. Aqui é o oposto: célula é exceção dentro de um mar de matriz. A consequência mecânica é direta — a matriz hidratada é o que resiste a compressão, distribui carga, absorve choque. Quando a articulação do joelho aguenta o peso do corpo em corrida, não são os condrócitos que estão segurando; é a água presa pelos proteoglicanos da MEC que faz o trabalho. Os condrócitos só mantêm e renovam essa matriz lentamente.

A consistência rígida-mas-firme da cartilagem vem dessa combinação: malha de colágeno mantendo a forma, proteoglicanos atraindo água por carga negativa, e a célula no meio orquestrando a manutenção. Em geral, todo esse conjunto está envolvido por uma bainha de conjuntivo denso chamada pericôndrio, com duas exceções importantes que vamos ver adiante.

#subtopico("1.3 Como um tecido sem vaso se alimenta")

Aqui aparece a primeira pergunta mecânica séria. Se não há capilar dentro, de onde vêm O₂, glicose, aminoácido? Para onde vão CO₂ e metabólitos? A resposta é #emph[difusão pela MEC hidratada]. Como 60-80% do volume da matriz é água, ela funciona como gel viscoso por onde moléculas pequenas atravessam por gradiente de concentração. O suprimento vem de três fontes possíveis: capilares do pericôndrio (a fonte normal); líquido sinovial (em cartilagem articular, que é nua); e capilares de tecidos vizinhos (em fibrocartilagem).

#confusao-prevista(
  titulo: "Avascularidade não é isolamento",
  aluno_acha: [aluno acha que sem vaso a cartilagem está "desligada" do organismo],
  mecanismo: [há nutrição ativa, só que indireta: difusão pelos 70% de água da MEC, partindo do pericôndrio. O metabolismo do condrócito é anaeróbio porque o O₂ não atravessa bem em distâncias grandes — por isso o tecido não pode crescer em massas espessas sem morrer no centro.],
)

A difusão de O₂ tem alcance limitado: alguns milímetros, no máximo. Por isso o condrócito desenvolve metabolismo anaeróbio — glicólise sem oxigênio, produzindo lactato — para sobreviver em camadas profundas. E por isso também o tamanho de um agregado cartilaginoso é geometricamente limitado: cartilagem espessa demais mata as células centrais por hipóxia, gerando calcificação e necrose. É o princípio mecânico que explica por que a cartilagem articular tem espessura medida em milímetros, não centímetros, e por que cartilagem velha calcifica de dentro para fora.

#mini-resumo[Sem vaso, o tecido vive de difusão a partir do pericôndrio e da água da MEC. O alcance limitado da difusão obriga metabolismo anaeróbio e limita a espessura do tecido.]

#subtopico("1.4 O pericôndrio: bainha que nutre e renova")

O pericôndrio é uma capa de conjuntivo denso que envolve a cartilagem, contínua com o conjuntivo adjacente. Tem duas camadas com funções diferentes, e essa estratificação é o que permite ao tecido se manter durante toda a vida.

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-19.png",
  largura: 65%,
  legenda: [Pericôndrio em duas camadas: a externa (fibrosa) é rica em colágeno tipo I e fibroblastos, traz os vasos; a interna (condrogênica) tem células capazes de virar condroblasto, e é por ela que a cartilagem cresce em superfície.])

A camada externa, fibrosa, é rica em colágeno tipo I e fibroblastos. É por ela que entram os vasos sanguíneos e linfáticos que vão alimentar o tecido por difusão. A camada interna, condrogênica, tem células-tronco mesenquimais capazes de se diferenciar em condroblasto. Essa segunda camada é a fonte permanente de células novas — sem ela, a cartilagem não conseguiria repor o que perde nem crescer em superfície depois da puberdade.

A regra geral é "toda cartilagem tem pericôndrio", e essa regra tem #emph[duas exceções importantes]. A cartilagem articular, na superfície dos ossos longos, não tem pericôndrio — ela é exposta diretamente à cavidade articular e nutrida pelo líquido sinovial. E a fibrocartilagem (disco intervertebral, menisco, sínfise púbica) também não tem pericôndrio próprio, porque está sempre integrada a um conjuntivo denso modelado que cumpre função parecida. Essas duas exceções não são curiosidade: elas explicam por que lesão articular cicatriza tão mal (sem progenitora local disponível) e por que o disco intervertebral é tão vulnerável (sem bainha protetora, depende do conjuntivo vizinho para se manter).

#subtopico("1.5 Duas idades da mesma célula: condroblasto e condrócito")

A célula da cartilagem é uma só, mas em duas idades distintas. #termo-nota[Condroblasto][célula jovem secretora de matriz cartilaginosa, ativa em síntese, localizada na superfície] é a versão jovem, ativa, que está secretando matriz na borda do tecido (vinda do pericôndrio condrogênico). À medida que secreta MEC ao seu redor, ela vai sendo cercada pela própria produção, até ficar aprisionada dentro de uma câmara minúscula. Naquele momento, ela vira #termo-nota[condrócito][célula madura, aprisionada em lacuna na matriz; metabolismo anaeróbio, baixa atividade sintética, papel de manutenção] — mesma célula, idade adulta.

#figura-lateral("/figuras/histo-07-cartilaginoso/slide-23.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O condrócito ocupa uma lacuna na matriz — uma câmara que ele mesmo escavou ao secretar MEC enquanto era condroblasto. Quando o corte histológico atravessa a lacuna, dá a impressão de um espaço vazio com a célula encolhida no meio. Esse é o critério visual mais direto para reconhecer cartilagem na lâmina: célula arredondada dentro de um halo claro, geralmente em pequenos grupos.],
  legenda: [Condrócito em lacuna — note o halo claro ao redor.])

O condrócito não é uma célula passiva: ele continua secretando matriz lentamente, mantém a hidratação local, responde a sinais mecânicos e ajusta a composição da MEC. Mas perde quase totalmente a capacidade de mitose. Quando consegue se dividir (algo raro no adulto, comum no jovem), forma um #termo-nota[grupo isógeno][conjunto de 2 a 8 condrócitos vindos de um único condroblasto por divisões sucessivas; ficam apertados na mesma lacuna ou em lacunas vizinhas]. Esses grupos são o sinal histológico de crescimento intersticial — a cartilagem cresceu de dentro, por divisão das próprias células.

Há outro detalhe morfológico importante: condrócitos têm reentrâncias e saliências na superfície, e estocam lipídios e glicogênio no citoplasma. As reentrâncias aumentam área de contato com a MEC, melhorando a difusão. O glicogênio é reserva para a glicólise anaeróbia que sustenta o metabolismo. Vendo tudo junto — célula arredondada em halo, grupos isógenos, citoplasma rico em lipídio — o reconhecimento na lâmina vira automático.

#confusao-prevista(
  titulo: "Condroblasto e condrócito não são tipos diferentes",
  aluno_acha: [aluno acha que são duas linhagens, como neurônio e glia],
  mecanismo: [é a #emph[mesma] célula em duas idades. Jovem (condroblasto) na borda, ativa em síntese; madura (condrócito) aprisionada na lacuna, papel de manutenção. Não há "condroclasto" estabelecido — diferente do tecido ósseo, onde reabsorção tem célula própria (osteoclasto).],
)

#mini-resumo[Uma só linhagem celular, duas idades: condroblasto secreta na borda, condrócito mantém aprisionado em lacuna. Crescimento interno se faz por mitose dos condrócitos formando grupos isógenos.]

#parte-title("PARTE II — A matriz que define tudo")

#subtopico("2.1 Por que a matriz é o tecido, não a célula")

Em quase todo tecido do corpo, a célula é o protagonista funcional — o neurônio conduz, o miócito contrai, o hepatócito metaboliza. No cartilaginoso, isso se inverte. As células ocupam 3-5% do volume; o trabalho mecânico de absorver compressão, distribuir carga, manter a forma articular sob peso é feito pela #emph[matriz]. A célula é, em essência, o operário de manutenção de uma estrutura que ela secretou e que agora a contém.

A consequência prática é que entender cartilagem é entender três componentes da MEC: colágeno (que dá a malha tensional), proteoglicanos (que prendem água por carga negativa), e glicoproteínas multiadesivas (que conectam o condrócito à malha). A função sai da interação entre eles. Trocar a proporção desses componentes muda o tipo de cartilagem — hialina, elástica, fibrosa — e portanto a função mecânica que ela desempenha.

#subtopico("2.2 Colágeno tipo II: a malha tensional")

O colágeno principal da cartilagem hialina e da elástica é o tipo II — diferente do tipo I do conjuntivo denso e do osso. Fibras de colágeno II são finas, não formam feixes grossos visíveis, e se organizam numa malha tridimensional que envolve toda a MEC. A função dessa malha é #emph[resistir a tensão]: quando a cartilagem é puxada ou estirada, o colágeno é a parte que aguenta.

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-32.png",
  largura: 60%,
  legenda: [Fibras de colágeno tipo II na MEC cartilaginosa: malha fina, tridimensional, que segura o tecido contra tensão. Em micrografia eletrônica, as fibras aparecem dispersas, sem formação de feixes paralelos — diferente do colágeno I do tendão.])

A escolha do tipo II (em vez do tipo I) tem razão mecânica: fibras finas e dispersas em malha aguentam tensão em qualquer direção, ao contrário das fibras grossas e paralelas do tipo I, que aguentam tensão num eixo só (por isso tipo I aparece em tendão, onde a tração é uniaxial). Em cartilagem articular, a carga vem em direções variadas — colágeno II distribui melhor.

Existe também um colágeno tipo VI, em quantidade pequena mas crítica: ele forma uma rede mais fina ao redor de cada condrócito, criando a chamada #emph[matriz capsular]. Essa cápsula colagênica delimita o microambiente imediato da célula, e é a base da organização territorial da matriz que vamos ver no próximo subtópico.

#subtopico("2.3 Proteoglicanos e GAGs: a esponja que segura água")

Se o colágeno aguenta tensão, quem aguenta compressão são os #termo-nota[proteoglicanos][PGs: eixo proteico com cadeias de GAG saindo lateralmente como cerdas; ocupam volume e atraem água por carga negativa] da MEC. A lógica é simples: cartilagem articular precisa não-colapsar quando comprimida por 80kg de peso corporal. Como?

O proteoglicano é um eixo proteico com dezenas de cadeias polissacarídicas saindo lateralmente, chamadas #sigla("GAG", [glicosaminoglicanos — cadeias polissacarídicas não-ramificadas com unidade dissacarídica repetida, geralmente sulfatadas, altamente aniônicas]). Cada cadeia de GAG é fortemente aniônica — tem carboxilas e sulfatos que estão desprotonados em pH fisiológico, portanto carga negativa densa. Essa carga atrai cátions (Na⁺, K⁺, Ca²⁺) que arrastam água por osmose. O resultado é um gel hidratado a 70-80% que se comporta como esponja: comprime, espreme água para fora, alivia a pressão; descomprime, água volta para dentro, recupera o volume.

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-35.png",
  largura: 75%,
  legenda: [Agregados de proteoglicanos: dezenas de PGs ancorados num único eixo de ácido hialurônico via proteínas de ligação. Cada PG tem seu próprio eixo proteico com cadeias de GAG perpendiculares. O resultado parece uma escova de garrafa gigante presa numa árvore de Natal — alta densidade de carga negativa por unidade de volume.])

A organização vai mais longe: muitos proteoglicanos se ancoram em paralelo num único filamento longuíssimo de #termo-nota[ácido hialurônico][AH: GAG não-sulfatado, sem eixo proteico, livre na matriz; funciona como espinha para ancorar proteoglicanos via proteínas de ligação] (AH), formando agregados gigantes. Esses agregados são o que mantém a cartilagem firme e elástica ao mesmo tempo — densidade de carga negativa máxima por unidade de volume, então a osmose mantém a matriz inchada como pneu cheio de ar.

#mini-resumo[Colágeno II resiste a tensão; proteoglicanos com GAG aniônicos retém água por osmose e resistem a compressão; ácido hialurônico ancora os PGs em agregados gigantes. A função mecânica nasce dessa divisão de trabalho na matriz.]

#confusao-prevista(
  titulo: "Ácido hialurônico não é proteoglicano",
  aluno_acha: [aluno mistura AH e PG por estarem juntos],
  mecanismo: [AH é GAG livre, sem eixo proteico. Ele serve de espinha onde dezenas de PGs (esses sim com eixo proteico) se ancoram. A confusão é fácil porque ambos estão no mesmo agregado, mas a química é diferente: AH é polissacarídeo puro; PG tem proteína + polissacarídeo.],
)

A glicoproteína multiadesiva mais característica é a #termo-nota[condronectina][glicoproteína multiadesiva da MEC cartilaginosa; tem sítios para colágeno II, GAGs e receptores do condrócito — funciona como "cola tripla"]. Ela tem sítios de ligação para colágeno tipo II, para GAGs, e para receptores de superfície do condrócito. Sem condronectina, a célula se desconecta da matriz, perde estímulo mecânico, atrofia. Essa adesão é o que permite ao condrócito "sentir" a carga aplicada ao tecido e ajustar a síntese de MEC em resposta.

#subtopico("2.4 Territórios da matriz: ler a lâmina")

A MEC não é homogênea ao redor de cada lacuna. Há três zonas concêntricas, e elas se diferenciam tanto na composição quanto na coloração — o que permite identificá-las na lâmina sem dificuldade.

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-40.png",
  largura: 75%,
  legenda: [Três zonas da matriz ao redor de um grupo isógeno: matriz capsular (rede de colágeno VI imediatamente ao redor da lacuna, basófila intensa), matriz territorial (PGs recentes, basofilia média), matriz interterritorial (mais antiga, mais colágeno II, basofilia baixa). A leitura da lâmina passa por reconhecer esses halos concêntricos.])

A #emph[matriz capsular] é a zona estreita imediatamente ao redor de cada condrócito, rica em colágeno tipo VI, anteriormente chamada de "cápsula". É a interface direta célula-matriz. A #emph[matriz territorial] é a região logo ao redor, rica em proteoglicanos recém-secretados pelo condrócito vizinho — por isso cora basofílica (PGs sulfatados atraem corantes básicos). E a #emph[matriz interterritorial] é o resto, mais antiga, com PGs em densidade menor e proporcionalmente mais colágeno II. Como o PG sulfatado é o que cora basófilo, a matriz territorial aparece como um halo escuro ao redor da lacuna, e a interterritorial fica mais clara.

Essa leitura morfológica não é decorativa: ela permite identificar quem secretou o quê, e em que ordem. A matriz capsular e territorial são produto recente do condrócito vivo; a interterritorial é matriz mais antiga, depositada quando aquele setor do tecido estava em crescimento. O patologista usa essa hierarquia para reconhecer cartilagem jovem (mais matriz territorial) vs. cartilagem envelhecida (matriz mais homogênea, com calcificações dispersas).

#clinica-box("Osteoartrose começa na perda de proteoglicano",
  [Na osteoartrose, o primeiro evento bioquímico é a perda de proteoglicanos da matriz territorial — enzimas como agrecanases (ADAMTS) clivam o agregam, e a cartilagem articular começa a perder água, ficar menos elástica, e a se desgastar. A perda inicial é da hidratação, não do colágeno. Por isso terapias antigas com glucosamina e condroitin-sulfato tentaram repor o substrato dos GAGs, com resultado modesto. A perda de colágeno II vem depois, na fase tardia da doença, e é irreversível.])

#parte-title("PARTE III — Tipos, crescimento e clínica")

#subtopico("3.1 Dois jeitos de crescer: intersticial e aposicional")

Cartilagem cresce por dois mecanismos distintos, com origens celulares diferentes. Entender essa duplicidade é o que explica por que a cartilagem jovem cresce em massa, mas a do adulto cresce só em superfície (e mal).

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-46.png",
  largura: 72%,
  legenda: [Dois modos de crescimento da cartilagem. Intersticial (esquerda): condrócito existente se divide por mitose, gera grupos isógenos, nova matriz é depositada entre eles — a cartilagem cresce de dentro para fora. Aposicional (direita): célula condrogênica da camada interna do pericôndrio se diferencia em condroblasto e deposita nova matriz sobre a superfície existente — a cartilagem cresce de fora para dentro.])

O crescimento #emph[intersticial] vem dos próprios condrócitos. Eles se dividem por mitose, formam grupos isógenos, e cada célula nova passa a secretar matriz ao seu redor, empurrando o tecido para fora. Esse mecanismo só funciona enquanto os condrócitos têm capacidade mitótica — ou seja, na cartilagem fetal e infantil. No adulto, a mitose desaparece, e o crescimento intersticial cessa. É por isso, por exemplo, que a placa epifisária dos ossos longos cresce em comprimento durante a infância e para na puberdade: o crescimento intersticial da cartilagem em proliferação acaba.

O crescimento #emph[aposicional] vem do pericôndrio. Células condrogênicas da camada interna se diferenciam em condroblastos novos, que depositam matriz cartilaginosa sobre a superfície já existente. Esse mecanismo continua disponível enquanto o pericôndrio existe (com a exceção da cartilagem articular e da fibrocartilagem, que não têm pericôndrio próprio). Por isso, em adulto, cartilagem só cresce por aposição — e mesmo assim de forma limitada.

#confusao-prevista(
  titulo: "Crescimento intersticial não ocorre no adulto",
  aluno_acha: [aluno diz "cartilagem cresce por mitose dos condrócitos" como se valesse sempre],
  mecanismo: [só vale na cartilagem jovem (fetal/infantil), enquanto os condrócitos ainda têm capacidade mitótica. No adulto sobra aposicional via pericôndrio — e cartilagem articular não tem pericôndrio, então praticamente não cresce mais.],
)

#subtopico("3.2 Hialina, elástica e fibrosa: o mesmo princípio em três versões")

Há três tipos de tecido cartilaginoso, e eles compartilham a lógica geral (célula em lacuna, matriz abundante, avascular) mas variam na composição da MEC — o que muda a função mecânica.

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-60.png",
  largura: 80%,
  legenda: [Comparativo dos três tipos. Hialina (esquerda): matriz homogênea, vítrea, colágeno II disperso, pericôndrio presente. Elástica (centro): igual à hialina mas com fibras elásticas entremeadas, matriz menos translúcida. Fibrosa (direita): condrócitos em fileiras, matriz com colágeno tipo I em feixes grossos paralelos, sem pericôndrio próprio.])

A #emph[cartilagem hialina] é o padrão. Matriz translúcida (daí o nome — hialos é "vidro" em grego), colágeno tipo II disperso, alta proporção de proteoglicanos e água. Aparece em superfícies articulares, traqueia, brônquios, cartilagens costais e moldes embrionários de ossos longos. É o tipo mais abundante e o mais estudado.

A #emph[cartilagem elástica] tem todos os componentes da hialina, mais fibras elásticas (elastina + fibrilina) entremeadas no colágeno II. Essas fibras dão flexibilidade e capacidade de recuperação após deformação — a orelha externa pode ser dobrada e volta sozinha à forma. Aparece na aurícula da orelha, epiglote, laringe, tuba auditiva. Ainda tem pericôndrio, ainda é avascular, ainda tem condrócitos em lacunas.

A #emph[fibrocartilagem] é o híbrido: tem condrócitos em lacunas (como toda cartilagem), mas a matriz é dominada por #emph[colágeno tipo I em feixes grossos paralelos] (como conjuntivo denso) em vez de colágeno II disperso. A proporção de PG e água é menor. Os condrócitos se organizam em fileiras paralelas aos feixes de colágeno. Não há pericôndrio próprio — está sempre integrada a conjuntivo denso. Aparece em disco intervertebral, menisco do joelho, sínfise púbica, inserções tendinosas.

#mini-resumo[Os três tipos diferem na matriz: hialina (colágeno II + muito PG, padrão), elástica (hialina + fibras elásticas), fibrosa (colágeno I + condrócitos, resiste tração).]

#subtopico("3.3 Onde cada uma aparece e por quê")

A localização de cada tipo segue da função mecânica predominante na região. Vale conectar tipo + lugar + razão, porque a clínica dessas regiões depende dessa lógica.

Hialina aparece onde se precisa de superfície lisa resistente a compressão: articulações, traqueia (para não colabar na inspiração), brônquios (mesma razão), cartilagens costais (sustentam a parede torácica deformável), placa epifisária (zona de crescimento dos ossos longos), molde embrionário dos ossos longos. A presença ubíqua se explica porque hialina é a configuração mais econômica — colágeno fino, muita matriz hidratada, resistência mecânica geral.

Elástica aparece onde se precisa de retorno após deformação: aurícula da orelha (dobra e volta), epiglote (fecha a traqueia na deglutição, abre na respiração), laringe (vibração da fala), tuba auditiva. A fibra elástica adicional é o que distingue mecanicamente: hialina entortada não volta sozinha, elástica volta.

Fibrocartilagem aparece onde se precisa resistir simultaneamente a tração e compressão: disco intervertebral (anel fibroso comprime e o anel resiste tração), menisco (distribui carga no joelho e resiste cisalhamento), sínfise púbica (resiste tração durante a marcha e compressão durante a gravidez), inserções de tendão no osso (transição entre tendão e cartilagem articular).

#clinica-box("Hérnia de disco vista pela histologia",
  [O disco intervertebral é um sanduíche: fibrocartilagem no anel externo (anel fibroso), gel de proteoglicanos no centro (núcleo pulposo, resíduo embrionário da notocorda). Sob compressão crônica, o anel se enfraquece e o núcleo gelatinoso pode extravasar — é a hérnia de disco. O tecido herniado comprime a raiz nervosa adjacente, gerando dor radicular. O reparo é difícil porque a fibrocartilagem do anel não regenera (sem pericôndrio próprio, sem vascularização para entregar progenitora), e o núcleo perde proteoglicano com a idade independentemente da hérnia, predispondo a recorrência.])

#subtopico("3.4 Por que cartilagem lesionada não cicatriza")

Aqui está a propriedade mais clinicamente relevante do tecido cartilaginoso: ele cicatriza mal, e em muitos casos não cicatriza nada. A razão é estritamente mecânica e celular, e se entende a partir de tudo que foi visto.

Para regenerar cartilagem, é preciso entregar condroblasto novo no local da lesão. Condroblasto vem do pericôndrio (camada condrogênica). Mas o pericôndrio só existe na superfície externa do tecido, e nem em toda cartilagem ele está presente — a cartilagem articular não tem pericôndrio. Pior: as células condrogênicas precisam migrar até o local da lesão, e a migração requer suprimento sanguíneo. Cartilagem é avascular. Logo, a célula reparadora não tem como chegar facilmente em lesão profunda.

#figura-nebli("/figuras/histo-07-cartilaginoso/slide-62.png",
  largura: 60%,
  legenda: [Reparo de cartilagem é, na prática, substituição por tecido conjuntivo cicatricial. Fibroblastos do conjuntivo vizinho invadem o defeito e depositam colágeno tipo I — o reparo tem aparência de cartilagem na coloração, mas mecanicamente é tecido fibroso. O tecido reparado é menos elástico, menos resistente a compressão, e tem vida útil curta.])

O que acontece na prática: fibroblastos do conjuntivo adjacente invadem a lesão e depositam tecido fibroso cicatricial — colágeno tipo I, pouca matriz hidratada, sem condrócitos verdadeiros. O tecido tem aparência grosseira de cartilagem, mas mecanicamente é conjuntivo denso. Lesões pequenas em cartilagem jovem com pericôndrio próximo podem regenerar parcialmente; lesões profundas em cartilagem articular adulta praticamente não regeneram, e o que se vê é fibrocartilagem cicatricial, mais frágil que a original.

#confusao-prevista(
  titulo: "Calcificação não é ossificação",
  aluno_acha: [aluno troca calcificação da cartilagem por ossificação endocondral],
  mecanismo: [calcificação é a deposição de fosfato de cálcio na MEC cartilaginosa envelhecida — não há substituição celular, é só "endurecer" a matriz, e ela mata o condrócito por bloquear difusão. Ossificação endocondral é diferente: capilares e osteoblastos invadem a cartilagem calcificada, removem a MEC velha e depositam MEC óssea nova com colágeno tipo I e hidroxiapatita. São dois processos distintos, o segundo depende do primeiro.],
)

Vale destacar uma exceção parcial: cartilagem articular não tem pericôndrio (toda nutrição vem do líquido sinovial), e justamente por isso ela é a que regenera pior. Toda a indústria de terapia para osteoartrose (visco-suplementação com AH, células-tronco, próteses) gira em torno desse fato. Entender por que cartilagem não cicatriza é a base para entender por que o joelho de um corredor de 50 anos não fica como o de um de 20.

#conclusao-box[
  Cartilagem é um tecido de poucas células e muita matriz, onde a função mecânica nasce de uma divisão de trabalho na MEC: colágeno tipo II aguenta tensão, proteoglicanos com cadeias de GAG aniônicas retém água por osmose e aguentam compressão, e glicoproteínas multiadesivas como a condronectina prendem o condrócito a essa malha para que ele continue mantendo o tecido. O preço da independência vascular é alto — o tecido vive de difusão pelo pericôndrio, cresce lentamente, e cicatriza muito mal. O ganho é uma estrutura que combina rigidez com elasticidade como nenhum outro tecido conjuntivo, sustenta articulações sob carga, e serve de molde para o esqueleto inteiro durante o desenvolvimento. Essa última função — molde — abre a porta para o próximo resumo. Quando, no embrião, a cartilagem hialina começa a calcificar e ser invadida por capilares trazendo osteoblastos, ela está cumprindo seu destino: virar osso. Sair de uma matriz hidratada que aguenta compressão por absorção para uma matriz mineralizada que aguenta carga por rigidez é o passo seguinte, e é o que vamos seguir no tecido ósseo.
]
