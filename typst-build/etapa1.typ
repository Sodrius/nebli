#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Para cada substância que a célula contém há uma taxa de entrada — ou de produção — e uma de saída — ou de consumo. Enquanto as duas se equilibram, a quantidade fica sob controle. Quando o equilíbrio se rompe, a substância sobra, e sobrar dentro de uma célula tem nome: acúmulo. O que muda de um acúmulo para outro não é o princípio, é *qual perna do balanço quebrou*.

Essa pergunta organiza as três PARTES: a lógica geral e a gordura no fígado; proteína, glicogênio e cálcio; e os pigmentos, que são acúmulos coloridos e por isso os que mais contam história — cor de peça e cor de lâmina dizem o que aconteceu ali e há quanto tempo.
]

#parte-title("PARTE I — A lógica do acúmulo e a gordura no fígado", primeira: true)

#subtopico("1.1 — Acúmulo é balanço quebrado")

Todo acúmulo intracelular é resposta a um distúrbio do metabolismo: a célula passou a conter mais de alguma coisa do que consegue processar. Essa coisa cai em três grupos — um *constituinte normal* em excesso (água, lípide, proteína), uma *substância anormal* exógena ou endógena (proteína mal montada, mineral, metal pesado), ou um *pigmento*, que pertenceria a um dos dois anteriores mas ganha categoria própria porque a cor lhe dá identificação e comportamento próprios.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-03.png", largura: 74%, legenda: [As quatro rotas. Em nenhuma delas a célula "escolheu" acumular.])

Cada rota é um ponto de falha diferente. No *metabolismo anormal*, a via não parou, foi desviada, e o produto desviado sobra — é o hepatócito de quem bebe. No *defeito de dobramento ou transporte*, a proteína sai do ribossomo com a conformação errada e não se encaixa no maquinário que a colocaria numa vesícula: fica presa na célula que a fabricou. Na *falta de enzima*, um substrato complexo que só uma enzima quebra se acumula no compartimento onde a reação deveria ocorrer. Na *ingestão de material indigerível*, a célula engoliu, guardou e não tem como desmontar.

Diante de um acúmulo na lâmina, três perguntas separam o achado banal do grave.

#table(
  columns: 2,
  fill: (col, row) => if row == 0 { rgb("#1f3551") } else { none },
  stroke: 0.5pt + rgb("#5a6c84"),
  inset: 6pt,
  [#text(white, weight: "bold")[A pergunta]],
  [#text(white, weight: "bold")[Por que muda o significado do achado]],
  [Isso é tóxico?],
  [A toxicidade vai do inerte ao destrutivo: lipofuscina não faz nada; proteína amiloide agregada acompanha morte neuronal.],
  [Está no lugar certo?],
  [Muco na célula caliciforme é onde ele deve estar. O mesmo muco no interstício significa que algo se rompeu.],
  [Produziu ou só guardou?],
  [Conter a substância não é tê-la sintetizado. O macrófago cheio de colesterol apenas fagocitou — e isso decide onde intervir.],
)

A última pergunta se desdobra numa distinção que vale para toda substância endógena: para acumular, ou a *produção* subiu ou o *metabolismo* caiu. As duas apontam para condutas opostas — frear a síntese, ou repor a via que falta.

#subtopico("1.2 — O trânsito da gordura no hepatócito")

O acúmulo de lípide chama-se #termo-nota[esteatose][acúmulo de lípide, em geral triglicéride, no citoplasma; "esteato" de gordura, "ose" de acúmulo] e é o mais comum de todos. O órgão preferencial é o fígado, o grande metabolizador de gorduras — o ponto por onde o ácido graxo passa para ser processado e redistribuído. Coração, rim e músculo também acumulam, em quantidade muito menor.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-06.png", largura: 64%, legenda: [Cada número é um ponto que pode travar — e cada travamento produz uma esteatose de causa diferente.])

O ácido graxo livre é absorvido no intestino, circula e entra no hepatócito, onde não tem destino único: parte é oxidada a corpo cetônico, combustível alternativo quando falta carboidrato; parte vai para fosfolipídio de membrana; parte vira éster de colesterol. O restante é esterificado sobre o esqueleto de α-glicerofosfato e forma #termo-nota[triglicéride][três ácidos graxos esterificados a um glicerol; forma de estoque da gordura, insolúvel em meio aquoso].

Mas o triglicéride é lipossolúvel, e molécula lipossolúvel não circula no plasma sozinha. Para sair, conjuga-se a uma apoproteína: o conjunto é uma *lipoproteína*, de miolo lipídico insolúvel e casca proteica hidrofílica, e é a casca que torna a partícula transportável. A que o fígado monta para exportar triglicéride é a #sigla("VLDL", [very low density lipoprotein — lipoproteína com que o fígado exporta triglicéride]), da mesma família da #sigla("LDL", [low density lipoprotein — principal veículo de colesterol para os tecidos]) e da #sigla("HDL", [high density lipoprotein — recolhe colesterol dos tecidos de volta ao fígado]), mais dedicadas ao colesterol. O ponto fino é que *sem proteína não há exportação de gordura*.

#mini-resumo[O hepatócito normal é estação de passagem, não depósito: recebe ácido graxo, esterifica em triglicéride e exporta como VLDL. Três lugares podem romper esse trajeto.]

#subtopico("1.3 — Esteatose: onde o trânsito quebra")

Chega ácido graxo demais; ou a esterificação é empurrada por substrato extra; ou a exportação trava e o triglicéride pronto não acha saída. Desnutrição, alcoolismo e diabetes não são mecanismos independentes — são combinações desses três.

O *excesso de oferta* aparece sempre que o organismo mobiliza gordura para gerar energia. No jejum e na desnutrição falta carboidrato; a primeira alternativa é mobilizar proteína, mas num jejum prolongado ou numa desnutrição grave não há proteína sobrando, e o corpo recorre ao lipídio do adipócito, que converge todo para o fígado. No diabetes o resultado é o mesmo por outro caminho: sem insulina a célula não capta glicose e se comporta *como se* estivesse em jejum, apesar da glicemia alta. Além disso a insulina é o freio da #termo-nota[lipase hormônio-sensível][enzima do adipócito que hidrolisa o triglicéride estocado e devolve ácido graxo à circulação; a insulina a mantém inibida] — sem freio, ela quebra gordura no adipócito e despeja mais ácido graxo no hepatócito, que esterifica o excedente.

*À primeira vista, parece contraditório que a desnutrição engorde o fígado.*

#confusao-prevista(
  titulo: "Esteatose por desnutrição não é contradição",
  aluno_acha: [aluno acha que quem come pouco não teria gordura para acumular],
  mecanismo: [a gordura acumula *no hepatócito*, e veio do adipócito, mobilizada para gerar energia. Dois efeitos somam: a desnutrição aumenta a *oferta* ao fígado e, por faltar proteína, reduz a *exportação* — sem apoproteína não se monta lipoproteína. O fígado engorda enquanto o corpo emagrece.],
)

O *bloqueio da exportação* é o segundo ponto: na inanição, pouca proteína significa pouca apoproteína e triglicéride retido. O #termo-nota[tetracloreto de carbono][solvente hepatotóxico que interfere na conjugação do triglicéride com apoproteína, bloqueando a saída de lipoproteína] produz o mesmo efeito quimicamente, com oferta normal na entrada.

O álcool age por três mecanismos convergentes. O etilista costuma ser desnutrido crônico — caloria vazia, pouco substrato nutricional —, então produz pouca proteína e mobiliza ácido graxo. O etanol lesa diretamente o hepatócito, reduzindo a capacidade metabólica do órgão. E o próprio metabolismo do etanol alimenta a via da gordura: a álcool-desidrogenase o converte em acetaldeído, a aldeído-desidrogenase converte o acetaldeído em ácido acético, e esse acetato em excesso serve de substrato para esterificar mais ácido graxo.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-10.png", largura: 68%, legenda: [O fígado esteatótico é amarelo e amolecido; o normal, acastanhado e firme. Na lâmina, os vacúolos são o espaço que a gordura ocupava antes de o processamento dissolvê-la.])

A morfologia decorre da química. Insolúvel no citosol, o triglicéride forma glóbulos que confluem e rechaçam o núcleo para a periferia. Macroscopicamente o órgão fica *amarelo e amolecido* — a cor do lípide substituindo o castanho do parênquima, e a consistência frouxa da gordura.

#subtopico("1.4 — Colesterol fora do fígado")

O colesterol é material de construção entregue por toda a cidade: toda célula o usa na síntese das próprias membranas. O problema não é a entrega, é o material ficar onde não há obra. E, ao contrário da esteatose, esse acúmulo pressupõe um fígado funcionando *bem* — é preciso conjugar e exportar lipoproteína para o colesterol chegar longe.

O endereço mais comum é a parede arterial. O colesterol se deposita na íntima e dispara resposta inflamatória local; lípide mais inflamação formam a placa que se projeta para a luz. Daí a consequência é mecânica: a obstrução parcial favorece turbilhonamento em vez de fluxo laminar, e o turbilhonamento facilita ativação endotelial e trombose — que é o que fecha o vaso. A placa não mata por ser grande, e sim por ser instável: o evento agudo é trombótico.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-12.png", largura: 50%, legenda: [A luz reduzida a uma fenda excêntrica; o resto é núcleo lipídico e necrótico sob a capa fibrosa.])

O segundo endereço é a vesícula biliar. A bile carrega pigmento biliar, sais biliares e colesterol, de modo que colesterol alto no sangue dá colesterol alto na bile. Ele pode precipitar na luz e formar cálculo, mas pode também ser fagocitado por macrófagos da parede: a peça resultante é a vesícula "em morango", mucosa acastanhada salpicada de pontos amarelos, cada ponto um agregado de macrófagos espumosos. Isso é #termo-nota[colesterolose][acúmulo de colesterol em macrófagos da lâmina própria da vesícula, produzindo a mucosa pontilhada conhecida como vesícula "em morango"] — depósito *na parede*, não concreção *na luz*.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-13.png", largura: 55%, legenda: [Os pontos amarelos da mucosa são as células de citoplasma espumoso que expandem as pregas.])

O terceiro é a pele e os tendões, onde o depósito em macrófagos forma nódulos amarelados chamados #termo-nota[xantomas][nódulos de macrófagos repletos de colesterol na derme ou em tendões; em pálpebra, xantelasmas]. Interessam menos pela lesão — benigna — do que pelo que anunciam: a dislipidemia ficando visível na superfície do corpo.

Quimicamente é o mesmo lípide nos três lugares; o que muda é o tecido que o recebe. Na artéria, sob pressão e fluxo, a consequência é trombótica e pode ser letal; na vesícula, é litogênica; na pele, apenas informativa. É a segunda pergunta do subtópico 1.1 aplicada por inteiro — e o mesmo raciocínio abre a PARTE II, agora com proteína, glicogênio e cálcio no lugar do lípide.

#parte-title("PARTE II — Proteína, glicogênio e cálcio")

#subtopico("2.1 — Proteínas e o controle de qualidade")

Proteína acumulada é visível ao microscópio óptico comum: agrega-se em glóbulos, cristais ou massas amorfas, porque perdeu a solubilidade da conformação nativa. O que muda entre os casos é a razão de ter agregado, e são três.

A primeira é *produção em excesso*. No mieloma múltiplo, o plasmócito neoplásico não só prolifera: produz imunoglobulina muito além do que consegue secretar, e o excedente se acumula dentro dele — carga inútil, já que imunoglobulina só serve circulante.

A segunda é *dificuldade de reabsorção*. A célula tubular renal reabsorve proteína filtrada; quando a carga filtrada sobe muito, a reabsorção satura e as gotículas captadas se acumulam como glóbulos hialinos. Aqui a célula não produziu nada — recebeu mais do que devolve.

A terceira é *falha do controle de qualidade*. Toda proteína recém-sintetizada sai do ribossomo como cadeia linear e precisa adquirir a conformação correta, acompanhada por uma #termo-nota[chaperona][proteína que assiste o enovelamento de outra, impedindo agregação prematura e conduzindo-a à conformação nativa ou ao compartimento correto]. Quando uma proteína sai malformada, ou se desnatura por radical livre, radiação ou calor, há duas saídas: a chaperona tenta redobrá-la; ou, se o dano é irrecuperável, ela é marcada com ubiquitina e triturada no proteassoma. Se qualquer das duas falha, a proteína não é consertada nem destruída, e só lhe resta agregar.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-15.png", largura: 70%, legenda: [Acima, a produção normal com chaperonas. Abaixo, o reparo: redobramento ou ubiquitinação e proteassoma. O acúmulo é o que sobra quando nenhuma das duas dá conta — e a via terminal é a morte celular.])

#clinica-box("Placa senil da doença de Alzheimer", [Proteínas de conformação alterada — as amiloides — agregam-se no parênquima cerebral em depósitos extracelulares chamados placa senil. O neurônio comprometido degenera, atrofia e morre, e o depósito *permanece*: a chaperona não redobra a proteína amiloide e a ubiquitinação não a encaminha eficientemente ao proteassoma. Essa permanência explica por que a lesão é cumulativa — cada depósito é definitivo, e a perda neuronal se soma ao longo dos anos em vez de se resolver.])

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-16.png", largura: 48%, legenda: [O material central denso é o amiloide; o depósito sobreviveu à célula que o cercava.])

#subtopico("2.2 — Glicogênio: duas causas, um estoque")

Assim como o triglicéride estoca gordura, o glicogênio estoca glicose — e a razão do estoque é a velocidade: mobilizá-la do glicogênio é muito mais rápido que fabricá-la a partir de proteína ou lipídio. Quando ele se acumula, o que travou não foi a entrada de glicose, foi a mobilização.

As causas são duas e correspondem a duas das quatro rotas da PARTE I. Um *distúrbio adquirido* do metabolismo, como o diabetes — metabolismo desviado, a primeira rota. Ou um *defeito genético* de enzima: as glicogenoses, a terceira rota.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-18.png", largura: 62%, legenda: [Cada linha é uma enzima da via de degradação — e o tecido afetado segue de onde ela trabalha: glicose-6-fosfatase é hepática e renal, e sua falta dá hipoglicemia grave; fosforilase muscular dá cãibra ao esforço.])

O princípio vale mais que a lista. A degradação do glicogênio é uma sequência de enzimas, e a deficiência em qualquer uma bloqueia a via e represa o polímero a montante. O que muda entre uma glicogenose e outra é *qual* enzima falta, e disso decorrem o tecido afetado e o quadro clínico. Os nomes próprios são homenagens históricas; o mecanismo é um só.

A morfologia se resolve por solubilidade: o triglicéride não se mistura ao citosol e faz vacúolos nítidos que empurram o núcleo, enquanto o glicogênio se dissolve no citoplasma e dá textura difusa e rendilhada.

#confusao-prevista(
  titulo: "Vacúolo de gordura e citoplasma rendilhado não são a mesma imagem",
  aluno_acha: [aluno acha que todo acúmulo citoplasmático produz o mesmo vacúolo claro],
  mecanismo: [lípide é insolúvel: forma glóbulos de contorno nítido que *rechaçam o núcleo*. Glicogênio é hidrossolúvel: distribui-se pelo citosol e deixa aspecto rendilhado, com núcleo central. E como ele arrasta água por osmose, a célula sobrecarregada ainda incha — some-se edema celular ao acúmulo.],
)

#subtopico("2.3 — Calcificação distrófica: cálcio no lugar errado")

Depositar cálcio não é anormal — a mineralização da matriz óssea é fisiológica. Calcificação patológica é a deposição de sais de cálcio *fora* do osso, e ela se divide em dois tipos que respondem a perguntas opostas: na distrófica o problema está no *tecido*; na metastática, no *sangue*. Essa oposição é a única coisa que realmente precisa ser sabida para não errar as duas.

A distrófica ocorre onde houve lesão celular. Numa área de necrose, muitas células se rompem e derramam o conteúdo; os mecanismos de reparo produzem matriz e colágeno; e nesse ambiente carregado de restos celulares, membranas fragmentadas e matriz nova, o cálcio que circula normalmente encontra superfícies onde se ligar. O processo passa a ser o mesmo da mineralização óssea — os componentes celulares servem de núcleo de cristalização. Daí o nome: cálcio no lugar errado, por um estímulo errado, que é a lesão do tecido.

O ponto que decide a compreensão é que *a distrófica não depende da calcemia*. A concentração sérica é normal; o que mudou foi o tecido, que passou a oferecer sítio de nucleação. Por isso ela aparece em situações tão diferentes quanto necrose caseosa da tuberculose, placas de ateroma cujos macrófagos espumosos morreram, valvas alteradas por senilidade ou febre reumática, tumores necróticos e cicatrizes antigas. O denominador comum não é a doença — é a lesão prévia.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-20.png", largura: 60%, legenda: [Depósitos basofílicos grosseiros sobre tecido desestruturado e parede vascular calcificada: o cálcio se ancora onde havia tecido morto, não se distribui.])

A esclerose calcificante de Mönckeberg merece nota porque a anatomia salva o raciocínio: nela o cálcio se deposita na túnica *média*, não na íntima. A placa de ateroma calcificada é lesão de íntima que sofreu necrose de macrófagos carregados de lípide e mineralizou depois. As duas endurecem o vaso, mas nascem de camadas diferentes — e a segunda amarra a PARTE I à PARTE II: o colesterol do subtópico 1.4 acaba, pela morte dos macrófagos que o fagocitaram, virando o sítio de nucleação do cálcio.

#subtopico("2.4 — Calcificação metastática: o problema está no sangue")

Se na distrófica o tecido chama o cálcio, na metastática o cálcio sobra e se deposita onde encontrar. O pré-requisito não é lesão, é hipercalcemia. E a hipercalcemia se entende pelo par de hormônios que governa o cálcio: a calcitonina favorece a deposição na matriz óssea; o #sigla("PTH", [paratormônio — hormônio da paratireoide que promove reabsorção óssea e eleva o cálcio circulante]) faz o oposto, retira cálcio do osso e o disponibiliza na circulação. É uma gangorra: consumo baixo eleva o paratormônio e mobiliza o osso; consumo alto eleva a calcitonina e reabastece.

Quatro situações a quebram para o lado do excesso. *Secreção anormal de paratormônio*, tipicamente por neoplasia de paratireoide, que produz sem obedecer ao controle. *Destruição do tecido ósseo* — mieloma, metástases ósseas —, que libera na circulação o cálcio mineralizado. *Distúrbios da vitamina D*, que reduzem a captação óssea e deixam mais cálcio livre. E a *insuficiência renal*: o rim retém fosfato; o fosfato derruba o cálcio sérico; a queda estimula cronicamente a paratireoide; e esse hiperparatireoidismo secundário acaba jogando cálcio na circulação. O caminho passa por uma #strong[hipo]calcemia inicial — quem tenta encurtá-lo erra.

#atencao-box("Calcificação metastática não tem relação com metástase tumoral", [O nome engana e a confusão é sistemática. "Metastática" não descreve implante de célula tumoral: é termo histórico, cunhado porque o quadro era frequente em pacientes com metástases ósseas — e o motivo é que a destruição do osso libera cálcio na circulação. O mecanismo é a hipercalcemia, com ou sem câncer envolvido. A consequência prática é grande: o depósito ocorre em *tecido viável e normal*, difusamente. Pulmão, rim, mucosa gástrica e vasos calcificam sem nunca terem sofrido necrose. Quem procura calcificação metastática numa área de lesão está procurando no lugar errado.])

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-21.png", largura: 50%, legenda: [Depósitos escuros num parênquima de arquitetura preservada: o cálcio se deposita *apesar de* o tecido estar íntegro.])

#table(
  columns: 3,
  fill: (col, row) => if row == 0 { rgb("#1f3551") } else { none },
  stroke: 0.5pt + rgb("#5a6c84"),
  inset: 6pt,
  [#text(white, weight: "bold")[Critério]],
  [#text(white, weight: "bold")[Distrófica]],
  [#text(white, weight: "bold")[Metastática]],
  [Onde está o problema], [No tecido — houve lesão prévia], [No sangue — há hipercalcemia],
  [Calcemia], [Normal; irrelevante], [Elevada; condição necessária],
  [Tecido que calcifica], [Necrótico, cicatricial ou degenerado], [Viável e histologicamente normal],
  [Distribuição], [Focal, na área lesada], [Difusa, em vários órgãos],
  [Exemplos], [Necrose caseosa, ateroma, valva alterada, cicatriz antiga], [Hiperparatireoidismo, destruição óssea, vitamina D, insuficiência renal],
)

#clinica-box("Por que a insuficiência renal crônica calcifica tudo", [O rim insuficiente não excreta fosfato; o fosfato retido se combina ao cálcio circulante e derruba o cálcio sérico. A paratireoide interpreta corretamente essa queda e aumenta o paratormônio — resposta adequada, mas que nunca cessa, porque o rim continua retendo fosfato. Instala-se o hiperparatireoidismo secundário: reabsorção óssea sustentada, cálcio despejado continuamente e, com produto cálcio-fosfato alto, deposição em tecidos viáveis por todo o corpo. A calcinose generalizada nasce, paradoxalmente, de uma hipocalcemia inicial.])

Uma se investiga olhando a lesão; a outra, dosando o cálcio. Os acúmulos da PARTE III trazem um dado a mais para essa investigação: a cor.

#parte-title("PARTE III — Pigmentos: a memória colorida da célula")

#subtopico("3.1 — Pigmentos exógenos: o que entra e não sai")

A tatuagem é um experimento de biologia celular feito em escala populacional. A tinta é depositada na derme, macrófagos residentes a fagocitam — é o que fazem com qualquer partícula estranha — e o processo para aí: nenhuma enzima do macrófago degrada aquele pigmento, nenhuma via o exporta. Ele fica dentro da célula pelo resto da vida dela, e quando ela morre outro macrófago o recolhe. Por isso a tatuagem é permanente — o desenho persiste *dentro* da célula. Fagocitado, indigerível, retido: a propriedade define toda a categoria.

O exemplo de importância médica é a #termo-nota[antracose][acúmulo de pigmento de carvão em macrófagos e linfonodos pulmonares, por inalação crônica de material particulado da poluição ou do tabagismo]. A queima incompleta de qualquer coisa gera material particulado contendo carvão elementar; inalado, ele chega ao alvéolo, é fagocitado e não pode ser digerido. O pulmão fica progressivamente pontilhado e depois enegrecido, com o pigmento nos septos e nos linfonodos de drenagem.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-22.png", largura: 62%, legenda: [Nos dois casos a célula fagocitou corretamente e falhou na etapa seguinte: não existe enzima que degrade tinta nem carvão.])

Antracose, porém, não equivale a pneumopatia: o carvão é inerte e algum grau dele existe em quase todo adulto urbano. Quem determina a doença é a carga acumulada e o tipo de partícula — poeiras minerais fibrogênicas reagem muito diferente do carvão puro. É a primeira pergunta do subtópico 1.1: encontrar o acúmulo é uma coisa, atribuir-lhe toxicidade é outra.

#subtopico("3.2 — Lipofuscina e melanina: dois marrons endógenos")

Os pigmentos endógenos que *não* derivam da hemoglobina são dois, ambos acastanhados. A lipofuscina nasce da autofagia, processo que a célula executa a vida inteira: ela envolve organelas velhas numa vesícula, funde-a com o lisossomo e recicla o conteúdo. As membranas dessas organelas são lipídicas, e durante a digestão esse lípide sofre peroxidação — e o produto peroxidado é justamente o que as enzimas lisossômicas não quebram. Ele se acumula em grânulos acastanhados perinucleares.

O que torna a #termo-nota[lipofuscina][pigmento acastanhado de lípide peroxidado não-digerível, resíduo da autofagia de membranas; acumula com a idade e é atóxico] interessante é ela não fazer nada: atóxica e sem significado patológico próprio, indica tempo de vida e turnover de membranas, não agressão em curso — daí o apelido de pigmento do envelhecimento. Em coração e músculo esquelético, de células longevas e alto metabolismo, ela dá ao órgão do idoso a coloração da *atrofia parda*.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-23.png", largura: 60%, legenda: [Grânulos escuros junto aos polos nucleares das fibras, com o resto da fibra normal — coerente com resíduo inerte. A mesma soma, na peça, é um coração acastanhado e de massa reduzida.])

#confusao-prevista(
  titulo: "Lipofuscina é achado, não agressor",
  aluno_acha: [aluno acha que muita lipofuscina indica lesão ativa ou toxicidade],
  mecanismo: [ela é resíduo insolúvel da peroxidação lipídica das membranas digeridas na autofagia — quanto mais tempo a célula viveu e mais organela reciclou, mais pigmento sobrou. Marca idade celular, não causa dano. Na atrofia parda, quem produz a atrofia é outro processo; a lipofuscina apenas fica mais evidente no citoplasma reduzido.],
)

A melanina ocupa posição singular: é o único pigmento endógeno *fisiológico* de cor marrom. Sua produção não é resíduo de nada, é via enzimática dedicada — nos melanócitos, a tirosina vira dihidroxifenilalanina e esta vira melanina, pela tirosinase. A lipofuscina é o que sobrou de uma digestão incompleta; a melanina é produto de síntese deliberada. Coincidem só na cor.

#subtopico("3.3 — Hemossiderina: o destino do ferro")

O terceiro marrom vem da hemoglobina, que é um anel heme com um átomo de ferro no centro acoplado a cadeias de globina. Quando uma hemácia é destruída e essa molécula é processada, ela se parte em dois destinos independentes: o ferro segue por um caminho, o restante do anel por outro. Este subtópico acompanha o ferro; o próximo, o resto.

O processo é visível a olho nu na cor de um hematoma: arroxeado no início, por desoxiemoglobina acumulada nos tecidos; esverdeado quando a hemoglobina é metabolizada e se forma biliverdina; acastanhado depois de alguns dias — e esse acastanhado é a #termo-nota[hemossiderina][pigmento amarronzado e granular formado pela agregação de micelas de ferritina; é o ferro estocado em excesso, derivado da hemoglobina]. A cronologia da cor é a cronologia da degradação.

A cadeia bioquímica é curta e vale pela sequência. O ferro liberado do heme liga-se à apoferritina, e o complexo é a ferritina, solúvel, forma de estoque fisiológica. Quando a ferritina excede o que a célula mantém em solução, as micelas se agregam, e esses agregados insolúveis são os grânulos de hemossiderina — grandes o bastante para serem vistos ao microscópio óptico como material amarronzado, granular e brilhante. Aparecem primeiro nos órgãos que lidam com hemácia em volume: medula óssea, o centro de produção, e fígado e baço, os de retirada.

Três situações enchem esses órgãos de ferro. *Destruição aumentada de hemácias* — hemorragia, em que o sangue extravasado é removido no local, e hemólise, como na anemia falciforme. *Transfusão de repetição*: por mais compatível que seja o sangue, uma fração das hemácias é destruída pelo receptor, e transfusões sucessivas somam ferro que o organismo não excreta. E *absorção ou oferta dietética aumentada*, terreno das hemocromatoses.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-26.png", largura: 62%, legenda: [Castanho, sozinho, é ambíguo — bile também é castanha. A coloração específica converte o ferro em azul e desfaz a dúvida: cor sugere, técnica confirma.])

Daí existir uma coloração dedicada ao ferro: como a bile também é acastanhada, um fígado marrom não diz qual pigmento está ali. O raciocínio a reter não é a técnica, é o princípio — quando duas substâncias produzem a mesma cor, a cor deixa de ser critério.

#clinica-box("Hemocromatose: quando o ferro passa a doer", [Pode ser primária, por defeito genético que aumenta a absorção intestinal de ferro, ou secundária, por hemólise crônica, transfusões repetidas ou aporte alimentar excessivo. A consequência decorre de onde o ferro se deposita. Na pele, dá pigmentação em tom bronze. No pâncreas, compromete as ilhotas e leva a diabetes mellitus — daí "diabetes bronzeado", que reúne os dois achados. No miocárdio, desorganiza a condução e gera arritmias, entre as causas de morte da doença. É mais frequente do que parece: nos Estados Unidos, a prevalência estimada da forma genética é de 1 para cada 200 a 500 pessoas. O mecanismo é implacável — o organismo tem vias eficientes para *absorver* ferro e nenhuma via regulada para *excretá-lo*.])

#subtopico("3.4 — Bilirrubina e icterícia: o destino do resto do heme")

O raciocínio costuma quebrar aqui: como hemossiderina e bilirrubina saem da mesma molécula e ambas são acastanhadas, acabam tratadas como variantes uma da outra. A diferença é de composição — o ferro do heme segue para a ferritina e a hemossiderina; o restante é convertido no fígado em bilirrubina, que *não contém ferro*. Uma via carrega o metal, a outra o anel.

#atencao-box("Hemossiderina tem ferro; bilirrubina não", [A separação é química e não admite meio-termo: o ferro do centro do heme entra na via apoferritina → ferritina → hemossiderina, e todo o restante vira bilirrubina no fígado, sem nenhum átomo de ferro. É essa distinção que justifica a coloração específica — um corante que precipita ferro cora a hemossiderina de azul e deixa a bilirrubina intocada, permitindo separar num fígado castanho o que é sobrecarga de ferro do que é colestase. Confundir as duas troca o diagnóstico e a conduta: sobrecarga de ferro se trata retirando ferro; colestase se trata desobstruindo ou tratando o hepatócito.])

O percurso normal da bilirrubina é curto: produzida no hepatócito, excretada no canalículo biliar, drenada até a vesícula e lançada no duodeno para emulsificar gorduras. A bile não é só bilirrubina — carrega sais biliares e colesterol, e é por isso que o colesterol da PARTE I podia precipitar dentro dela.

Acumulada, a bilirrubina impregna órgãos e mucosas de amarelo-esverdeado: é a icterícia. O que decide o raciocínio clínico é que há dois pontos de falha opostos. A bile pode empoçar *dentro do hepatócito*, quando um problema metabólico impede que ele excrete o pigmento que produziu. Ou pode acumular *na via biliar* obstruída: o hepatócito produz e excreta normalmente, mas o produto não tem para onde drenar e reflui. Nos dois casos o paciente fica ictérico; a diferença está em onde a coluna parou.

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-28.png", largura: 42%, legenda: [Tampões de bile em canalículos dilatados, com arquitetura preservada ao redor — problema de escoamento, não de destruição do parênquima.])

A árvore dos pigmentos mostra por que a classificação é feita assim: primeiro exógenos e endógenos; entre os endógenos, os não-hemoglobinogênicos (melanina, lipofuscina) e os hemoglobinogênicos; e entre estes, o metabolismo normal (hemossiderina, bilirrubina) e o patológico (metemoglobina, carboxiemoglobina).

#figura-nebli("/figuras/patologia-02-acumulos-celulares/slide-29.png", largura: 50%, legenda: [Cada bifurcação é uma pergunta: veio de fora ou de dentro? Deriva da hemoglobina? O metabolismo foi normal ou patológico?])

#mini-resumo[Do heme saem dois pigmentos: hemossiderina, que leva o ferro, e bilirrubina, que leva o anel. A bilirrubina acumulada dá icterícia, por defeito de excreção do hepatócito ou por obstrução da via biliar. A coloração para ferro é o que separa as duas num fígado castanho.]

#conclusao-box[
Um princípio percorreu as três PARTES: *acúmulo é quantidade que ultrapassou a capacidade de processamento*. Toda vez que uma substância sobrou dentro de uma célula, bastou perguntar qual perna do balanço quebrou. Foi essa pergunta que separou a esteatose do diabetes (oferta) da esteatose da inanição (exportação), o acúmulo proteico do mieloma (produção) do da placa senil (degradação), e a calcificação distrófica (o tecido chama) da metastática (o sangue sobra).

O mecanismo nuclear que sustenta o princípio é a *solubilidade*. O triglicéride precisa de apoproteína porque é insolúvel — e é por isso que a desnutrição, que tira proteína, engorda o fígado. O glicogênio é solúvel, e por isso rendilha o citoplasma em vez de fazer vacúolo, ainda arrastando água. A ferritina é solúvel e a hemossiderina não é, e é essa passagem que torna o ferro visível ao microscópio óptico. A proteína agregada perdeu a solubilidade da conformação nativa, e por isso forma glóbulo. Quem entende o comportamento físico da molécula prevê a imagem da lâmina antes de vê-la.

Na clínica a cadeia se fecha nos mesmos termos. O renal crônico calcifica pulmão e vasos porque retém fosfato, derruba o cálcio sérico e mantém a paratireoide cronicamente estimulada. O paciente com hemocromatose fica bronzeado, diabético e arrítmico porque absorve ferro sem ter via regulada para excretá-lo. O ictérico pode ter hepatócito que não excreta ou via que não drena — e distinguir os dois muda a conduta inteira.

Daqui em diante, o passo natural é sair do acúmulo dentro da célula e olhar a resposta do tecido em volta. Abrem-se duas continuações: a das *adaptações celulares* — atrofia, hipertrofia, hiperplasia e metaplasia —, em que a célula não acumula, muda de tamanho, número ou identidade para caber numa demanda nova; e a da *inflamação e do reparo*, que o ateroma, a necrose calcificada e a cicatriz antiga vinham anunciando, em que o acúmulo foi só o gatilho e a doença nasceu da reação do tecido a ele.
]
