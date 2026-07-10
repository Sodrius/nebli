#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Antes de entrar nos detalhes, é preciso fixar o problema que a replicação precisa resolver. O #sigla("DNA", [ácido desoxirribonucleico — molécula que carrega a informação genética]) é uma dupla-hélice antiparalela: as duas fitas correm em direções opostas, e a única enzima capaz de sintetizar DNA novo só opera em um sentido específico. Isso cria um impasse que a célula resolve com uma bateria de proteínas especializadas — cada uma atacando um aspecto diferente do problema. Esta etapa explica o que cada agente faz, *por que* ele existe, e o que aconteceria sem ele.
]

#parte-title("PARTE I — O problema que a célula resolve", primeira: true)

#subtopico("1.1 — A estrutura que tudo complica: antiparalelidade e 5'→3'")

A replicação parte de um dado estrutural que não pode ser ignorado: o DNA é uma dupla-hélice onde as duas fitas correm em sentidos opostos. Uma fita vai de 5' para 3' em uma direção; a outra vai de 3' para 5' nessa mesma direção. Essa *antiparalelidade* é exatamente o que permite o pareamento de bases — adenina com timina (dois pontos de contato por ponte de hidrogênio), citosina com guanina (três pontos de contato) — mas também é o que torna a cópia complicada.

A complicação vem de uma propriedade universal das DNA-polimerases: elas só conseguem adicionar nucleotídeos ao *extremo 3'-OH livre* de uma cadeia já existente. O mecanismo é direto — o dNTP entrante chega com seu trifosfato no carbono 5', que é atacado pelo 3'-OH da cadeia em crescimento, formando a nova ligação fosfodiéster e liberando pirofosfato (#sigla("PPi", [pirofosfato inorgânico — subproduto liberado a cada adição de nucleotídeo durante a síntese de DNA])). O resultado: a cadeia nova sempre cresce de 5' para 3'.

Agora o problema torna-se claro: como copiar a segunda fita, que corre no sentido oposto ao da primeira? A polimerase não pode simplesmente "inverter" seu modo de trabalho. A solução que a evolução encontrou é elegante — sintetizar essa fita em pedaços curtos, cada um no sentido correto 5'→3', mas dispostos de modo que o conjunto avance na direção contrária à abertura da dupla-hélice. Esses pedaços são os #termo-nota[fragmentos de Okazaki][segmentos curtos de DNA sintetizados discontinuamente na fita retardada: ~1.000–2.000 nt em procariotos, ~100–200 nt em eucariotos]. Entendê-los exige primeiro entender por que a forquilha começa em um ponto específico e por que cada enzima existe.

#figura-nebli("/figuras/replicacao-dna/slide-04.png",
  largura: 65%,
  legenda: [Dupla-hélice do DNA: antiparalelidade das fitas, espaçamento de 3,4 Å entre pares de bases consecutivos e uma volta completa a cada 3,4 nm (10 pares de bases). A-T forma 2 pontes de hidrogênio; G-C forma 3 — diferença que determina onde a replicação começa.])

#subtopico("1.2 — A origem de replicação: oriC")

A replicação não abre o DNA em qualquer ponto ao acaso — começa em uma sequência específica chamada #termo-nota[origem de replicação][sequência de DNA reconhecida por proteínas iniciadoras específicas; ponto onde a replicação se inicia; em procariotos é única (oriC); em eucariotos, centenas a milhares por genoma]. Em *Escherichia coli*, existe uma única origem, o #sigla("oriC", [origin of replication in Chromosome — sequência de ~245 pb do cromossomo de *E. coli* onde a replicação se inicia]). A sequência do oriC tem uma característica não acidental: é excepcionalmente rica em pares A=T.

A razão é termodinâmica. Adenina e timina formam apenas duas pontes de hidrogênio entre si, enquanto citosina e guanina formam três. Menos pontes de hidrogênio significam menos energia para separar as fitas — a abertura começa mais facilmente em regiões ricas em A=T. As proteínas iniciadoras reconhecem o oriC, montam um complexo iniciador e promovem a fusão local (separação das fitas) nessa região termicamente vulnerável, dando início à montagem de toda a maquinaria de replicação.

Do oriC, a replicação avança nos dois sentidos simultaneamente — fenômeno chamado de *replicação bidirecional*. Formam-se duas #termo-nota[forquilhas de replicação][estrutura em Y onde a dupla-hélice parental está sendo separada e o DNA novo sintetizado; avança bidirecionalmente a partir da origem; cada forquilha carrega toda a maquinaria replicativa], que se afastam em direções opostas ao redor do cromossomo circular até se encontrarem no ponto diametralmente oposto. Cada forquilha carrega o mesmo conjunto de enzimas trabalhando em paralelo.

#figura-nebli("/figuras/replicacao-dna/slide-06.png",
  largura: 75%,
  legenda: [Acima: cromossomo circular de *E. coli* com oriC marcado — duas forquilhas se afastam em sentidos opostos a partir da origem (replicação bidirecional) até se encontrarem no ponto oposto. A sequência de círculos mostra a progressão da "bolha" de replicação em expansão. Abaixo: experimento de autoradiografia com marcação pesada/leve confirmando a bidirecionalidade — dois focos simétricos de DNA recém-sintetizado.])

#subtopico("1.3 — Abrindo a forquilha: helicase, SSB e girase")

A fusão inicial das fitas no oriC é apenas o ponto de partida. Para que a replicação avance ao longo de centenas de quilobases, três proteínas trabalham em conjunto para manter a forquilha aberta, estável e topologicamente viável.

A *helicase* é o motor da abertura. Ela usa energia de #sigla("ATP", [adenosina trifosfato — moeda energética celular]) para quebrar as pontes de hidrogênio entre as bases, separando fisicamente as duas fitas à medida que a forquilha avança. Sem helicase, a replicação pararia imediatamente após o aquecimento local inicial — as fitas voltariam a se reenrolar espontaneamente pela estabilidade das pontes de hidrogênio.

As *proteínas #sigla("SSB", [Single-Strand Binding — proteínas que se ligam especificamente à fita simples de DNA, estabilizando-a na forma aberta])* entram logo após a helicase separar as fitas. Elas se ligam cooperativamente às fitas únicas e impedem que se reenrolem antes que a polimerase chegue. Sem as SSB, a helicase gastaria energia em vão — abriria e a fita se fecharia logo a seguir. As SSB funcionam como "travesseiros" que mantêm as fitas abertas e disponíveis para a polimerase.

A *DNA girase* (#termo-nota[topoisomerase II bacteriana][topoisomerase que corta as duas fitas do DNA, permite o giro da molécula para aliviar tensão torcional e as religa; alvo das fluoroquinolonas]) resolve um problema topológico que não é imediatamente óbvio: o superenrolamento. Imagine separar duas cordas enroladas entre si — à medida que você as puxa, a região à frente fica cada vez mais retorcida e comprimida. Na forquilha de replicação, o mesmo acontece: cada par de bases separado pela helicase gera um superenrolamento positivo à frente da forquilha. Sem alívio, esse superenrolamento acumula tensão mecânica suficiente para bloquear fisicamente o avanço da helicase. A DNA girase corta as duas fitas, deixa que a torção se dissipe, e as religa — processo que consome ATP e pode ser bloqueado pelos antibióticos fluoroquinolonas (ciprofloxacino, levofloxacino), que aprisionam a girase no complexo covalente com o DNA, tornando o nick um fator letal.

#confusao-prevista(
  titulo: "Helicase e topoisomerase têm ações distintas",
  aluno_acha: [as duas "desenovelam" o DNA, portanto têm a mesma função],
  mecanismo: [A helicase quebra *pontes de hidrogênio entre as bases* no ponto da forquilha — é ela quem separa fisicamente as duas fitas. A topoisomerase (girase) corta e religa *o esqueleto fosfodiéster* à frente da forquilha, aliviando o superenrolamento torcional causado pela abertura. Uma atua nas bases; a outra atua no esqueleto. Bloquear a helicase impede a abertura das fitas. Bloquear a girase deixa a forquilha travada pelo acúmulo de tensão à frente.],
)

#figura-nebli("/figuras/replicacao-dna/slide-09.png",
  largura: 70%,
  legenda: [Visão geral da forquilha de replicação: fita líder (leading strand) crescendo continuamente e fita retardada (lagging strand) sintetizada em fragmentos de Okazaki. As setas na fita retardada apontam na direção contrária ao avanço da forquilha — cada fragmento cresce 5'→3', mas o conjunto progride em sentido oposto ao movimento da forquilha.])

#parte-title("PARTE II — As polimerases: especialistas com papéis distintos")

Com a forquilha aberta e as fitas estabilizadas pelas SSB, chegam os protagonistas da síntese: as DNA-polimerases. Em *E. coli* existem três (Pol I, Pol II e Pol III), mas a Pol II tem papel predominante em reparo. As protagonistas da replicação são Pol I e Pol III — com funções complementares e precisamente delimitadas.

#subtopico("2.1 — DNA-Pol I: a enzima de revisão e reparo")

Em 1957, Arthur Kornberg isolou a primeira DNA-polimerase conhecida — a DNA-Pol I. Foi o primeiro exemplo de enzima dirigida por molde: sem uma fita-molde de DNA para ler, ela não adiciona nenhum nucleotídeo. A descoberta rendeu a Kornberg o Prêmio Nobel de 1959.

A DNA-Pol I é um monômero de 103 kDa que adiciona ~100 nucleotídeos por segundo — velocidade modesta, adequada à sua função: ela não é a polimerase principal de replicação. Sua estrutura carrega *três atividades catalíticas* em domínios fisicamente próximos, mas distintos, de modo que o DNA pode deslocar-se entre eles sem sair da enzima:

O *sítio de polimerização* (5'→3') adiciona #sigla("dNTP", [desoxirribonucleotídeo trifosfato — os quatro substratos da DNA-polimerase: dATP, dCTP, dGTP, dTTP]) ao 3'-OH livre da cadeia em crescimento, lendo o molde no sentido 3'→5'.

O *sítio de exonuclease 3'→5'* é o mecanismo de #termo-nota[proofreading][revisão imediata de erros de incorporação: a enzima verifica se o último nucleotídeo adicionado está corretamente pareado antes de prosseguir; responsável pela alta fidelidade da replicação]. Após cada adição, a extremidade 3' da cadeia desloca-se para esse sítio. Se o nucleotídeo estiver mal pareado, a exonuclease 3'→5' o remove — e a síntese recomeça no sítio de polimerização. Se estiver correto, a extremidade volta e a adição continua. Polimerização e revisão ocorrem simultaneamente, sem que o DNA se solte da enzima.

O *sítio de exonuclease 5'→3'* tem outra função: remove nucleotídeos *à frente* da polimerase. É essa atividade que permite à Pol I retirar o primer de #sigla("RNA", [ácido ribonucleico]) da fita retardada — ao avançar sintetizando DNA, a Pol I usa a exonuclease 5'→3' para degradar os ribonucleotídeos do primer imediatamente à sua frente ("nick translation"). Essa mesma atividade remove *dímeros de timina*, lesões formadas quando a radiação ultravioleta funde covalentemente duas timinas adjacentes na mesma fita.

#figura-nebli("/figuras/replicacao-dna/slide-19.png",
  largura: 70%,
  legenda: [Esquerda: estrutura da DNA-Pol I — conformação (a) com o sítio de polimerase ativo e conformação (b) após o terminal 3' deslizar para o sítio de exonuclease 3'→5'. A proximidade dos dois sítios permite que o proofreading ocorra sem soltar o DNA. Direita: base T mal pareada no terminal 3' é capturada pelo sítio de exonuclease 3'→5' e removida antes que o próximo nucleotídeo seja adicionado.])

#confusao-prevista(
  titulo: "Exonuclease 3'→5' e exonuclease 5'→3' têm funções opostas",
  aluno_acha: [as duas atividades exonucleásicas fazem proofreading],
  mecanismo: [São funções distintas. A exonuclease *3'→5'* faz proofreading — remove o último nucleotídeo incorporado (do terminal 3' da cadeia) se ele estiver mal pareado. A exonuclease *5'→3'* não toca o terminal 3' da cadeia crescente: ela remove nucleotídeos da fita deslocada à frente, usada para retirar o primer de RNA e dímeros de timina. Confundir as duas inverte completamente a lógica da revisão.],
)

A DNA-Pol I tem *baixa processividade* — solta o molde com frequência. Isso reflete sua função: preencher buracos curtos, não sintetizar longos trechos contínuos.

#figura-nebli("/figuras/replicacao-dna/slide-17.png",
  largura: 55%,
  legenda: [Ação de exonuclease 3'→5' em detalhe: o resíduo C mal pareado no terminal 3' é hidrolisado pelo sítio de exonuclease. Após a remoção, a polimerase retoma a síntese e adiciona o nucleotídeo correto (G).])

#subtopico("2.2 — Por que a polimerase precisa de primer")

Aqui está um dos pontos de quebra mais importantes de todo o tema: a DNA-Pol I (assim como a Pol III) *não consegue iniciar uma cadeia do zero*. Ela só é capaz de *estender* uma cadeia já existente que tenha um 3'-OH livre e pareado com o molde. Sem esse 3'-OH inicial, a polimerase não tem onde ancorar o primeiro dNTP.

Isso cria um problema: para copiar o DNA, precisa-se de uma cadeia pré-existente. A solução biológica é o #termo-nota[primer][curta sequência de RNA (≈10 nt) sintetizada pela primase, que fornece o 3'-OH inicial para a DNA-polimerase começar a extensão] — um curto segmento de #sigla("RNA", [ácido ribonucleico]), em torno de 10 nucleotídeos, sintetizado pela *primase*.

A primase é uma RNA-polimerase especializada que, diferente das DNA-polimerases, *consegue iniciar uma cadeia do zero* — sem 3'-OH pré-existente. Ela sintetiza um curto oligorribonucleotídeo complementar ao molde de DNA, e então a DNA-Pol III assume: usa o 3'-OH da última ribose do primer como ponto de partida para adicionar desoxirribonucleotídeos.

O primer de RNA é temporário. Após a síntese do fragmento de DNA adjacente, a Pol I chega pelo outro lado e usa sua exonuclease 5'→3' para remover os ribonucleotídeos do primer, substituindo-os por DNA. O espaço residual (um nick de fita simples entre o 3'-OH recém-formado e o 5'-fosfato do fragmento seguinte) é então selado pela DNA ligase.

#figura-nebli("/figuras/replicacao-dna/slide-14.png",
  largura: 50%,
  legenda: [Primer de RNA (fita superior em amarelo, 5'→3') pareado com a fita-molde de DNA (faixa cinza à direita, 3'→5'). O 3'-OH exposto na extremidade do primer é o ponto de entrada para a DNA-polimerase — ela usa esse hidroxila para iniciar a adição do primeiro desoxirribonucleotídeo.])

#subtopico("2.3 — DNA-Pol III: a máquina principal")

Se a Pol I é a faxineira especializada, a DNA-Pol III é o motor da fábrica. É ela quem sintetiza o grosso do DNA novo durante a replicação. Sua velocidade é de *1.000 nucleotídeos por segundo* — dez vezes maior que a Pol I — e sua #termo-nota[processividade][capacidade de permanecer ligada ao molde e sintetizar longos trechos sem se dissociar; a Pol III não solta o molde até terminar todo o cromossomo] é extraordinária: uma única Pol III copia os ~4,6 milhões de pares de bases do cromossomo de *E. coli* sem soltar o molde.

A Pol III tem 10 subunidades com massa total de ~900 kDa. O segredo de sua processividade é a subunidade *β₂* (beta-dois): um anel formado por dois monômeros β que circunda completamente a dupla-hélice como um #termo-nota[grampo deslizante][anel proteico que envolve a dupla-hélice de DNA e ancora a polimerase ao molde sem impedir o deslizamento; equivalente ao PCNA em eucariotos]. O anel tem 35 Å de diâmetro — amplo para que o DNA deslize e gire livremente durante a síntese, mas fechado o suficiente para manter a polimerase ancorada. Sem o grampo β₂, a Pol III se desprenderia após poucas centenas de nucleotídeos, perdendo a processividade que a torna eficiente.

A Pol III também possui atividade de exonuclease 3'→5' (proofreading) na subunidade ε. Combinando velocidade de 1.000 nt/s, processividade quase infinita no contexto do cromossomo e proofreading, a Pol III chega a uma taxa de erro de apenas 1 em cada 10⁷ nucleotídeos. Com os sistemas de reparo pós-replicativo, o erro final cai para 1 em 10⁹–10¹⁰.

#figura-nebli("/figuras/replicacao-dna/slide-22.png",
  largura: 65%,
  legenda: [Esquerda: estrutura tridimensional da Pol III completa com subunidades coloridas. Direita: diagrama do holoenzima como dímero assimétrico — subunidades α (sítio catalítico de polimerização, em verde), ε (exonuclease 3'→5', em rosa) e θ, mais o grampo β₂ (em amarelo) que ancora a enzima ao molde. As duas cópias do núcleo catalítico processam simultaneamente a fita líder e um fragmento de Okazaki na mesma forquilha.])

#parte-title("PARTE III — A orquestra completa na forquilha")

Com os agentes individuais compreendidos, é hora de ver a replicação como uma operação coordenada. O ponto de quebra desta PARTE: muitos estudantes entendem os agentes em isolado, mas ficam confusos com como eles operam *simultaneamente* na mesma forquilha, com a fita retardada sendo sintetizada em direção contrária ao avanço da forquilha. A figura do slide-28 é o mapa orientador.

#subtopico("3.1 — Fita líder e fita retardada: a assimetria fundamental")

No ponto da forquilha, as duas fitas-molde parentais têm orientações opostas. Isso cria dois cenários radicalmente diferentes para a polimerase:

A *fita-molde que corre 3'→5' na direção do avanço da forquilha* permite que a Pol III sintetize diretamente no sentido 5'→3', acompanhando a abertura. Essa síntese é *contínua* — um único primer de RNA no início basta para que a Pol III replique toda a fita sem interrupção. Chama-se *fita líder* (leading strand).

A *fita-molde que corre 5'→3' na direção do avanço da forquilha* cria o constrangimento: a Pol III só sintetiza 5'→3', mas o molde aponta "na direção errada". Ela não pode inverter a síntese. A solução é sintetizar em pequenos fragmentos — cada um no sentido correto 5'→3', mas iniciando sempre em um ponto novo (mais próximo da forquilha) e crescendo em direção contrária ao avanço. Essa é a *fita retardada* (lagging strand), e seus fragmentos são os fragmentos de Okazaki.

#atencao-box("A fita retardada não sintetiza de trás para frente", [Cada fragmento de Okazaki é sintetizado no sentido *5'→3'*, igual a qualquer outra síntese de DNA — não existe polimerase que trabalhe de 3' para 5'. O que é "invertido" é a *direção de preenchimento dos fragmentos em relação ao avanço da forquilha* — o fragmento mais recente começa perto da forquilha e termina longe dela, enquanto os fragmentos anteriores ficam progressivamente mais distantes. Confundir isso com "síntese no sentido errado" é o erro mais comum neste tema.])

A Pol III opera como um *dímero assimétrico* na mesma forquilha: um núcleo catalítico replica a fita líder continuamente; o outro replica a fita retardada em fragmentos. Para fazer isso sem se mover no sentido "errado", a fita retardada forma um laço (loop), de modo que a Pol III lê o molde da fita retardada no mesmo sentido físico que lê a fita líder. Quando um fragmento de Okazaki termina, o laço se desfaz, a Pol III se desliga e um novo laço é formado mais à frente.

#subtopico("3.2 — Fragmentos de Okazaki: síntese e resolução")

Para cada fragmento de Okazaki, a célula executa uma sequência de quatro eventos coordenados:

A *primase* (associada fisicamente à helicase no complexo primassome) sintetiza um novo primer de RNA de ~10 nucleotídeos no molde da fita retardada, mais próximo da forquilha que o fragmento anterior.

A *Pol III* usa o 3'-OH do primer para iniciar a extensão com desoxirribonucleotídeos, sintetizando o fragmento de Okazaki (1.000–2.000 nt em procariotos) até encontrar o 5' do primer do fragmento anteriormente sintetizado.

A *Pol I* entra na extremidade 5' do primer anterior e usa sua exonuclease 5'→3' para remover os ribonucleotídeos à medida que avança, preenchendo o espaço com DNA (nick translation). O primer de RNA é substituído nucleotídeo a nucleotídeo por DNA.

A *DNA ligase* sela o nick residual — o corte de fita simples que persiste entre o 3'-OH do DNA recém-sintetizado pela Pol I e o 5'-fosfato do fragmento adjacente mais antigo.

#figura-nebli("/figuras/replicacao-dna/slide-28.png",
  largura: 80%,
  legenda: [Forquilha de replicação completa em ação. À direita: helicase/primase separa as fitas e sintetiza primers; grampo β₂ ancora a Pol III dimérica ao molde; SSBs (esferas verdes) estabilizam a fita retardada já separada; DNA girase alivia o superenrolamento à frente. À esquerda: fragmentos de Okazaki sendo processados — Pol I remove o primer do fragmento anterior (em lilás) e DNA ligase sela o nick. Note o fragmento de Okazaki atual (em teal) crescendo na direção oposta ao avanço da forquilha.])

#mini-resumo[A divisão de trabalho na fita retardada é precisa: a Pol III faz o trabalho pesado (síntese do fragmento); a Pol I faz o acabamento fino (remoção do primer e preenchimento); a ligase fecha. Nenhuma das três faz o trabalho das outras duas.]

#subtopico("3.3 — DNA ligase: fechando o nick")

A DNA ligase merece atenção especial porque o mecanismo que ela usa revela algo importante: a formação de uma ligação fosfodiéster entre dois fragmentos já existentes não é espontânea — exige input de energia.

Em *E. coli*, a DNA ligase usa #sigla("NAD", [nicotinamida adenina dinucleotídeo — cofator energético e de oxirredução da célula])⁺ como fonte de energia. Em eucariotos (e no fago T4), usa ATP. Independente do cofator, o mecanismo ocorre em três passos: (1) a enzima captura o grupamento AMP (derivado de ATP ou NAD⁺), formando um intermediário enzima-AMP por ligação covalente com uma lisina catalítica; (2) o AMP é transferido para o 5'-fosfato do nick, ativando-o com alta energia; (3) o 3'-OH adjacente ataca o 5'-fosfato adenilado, formando a nova ligação fosfodiéster e liberando AMP. O nick está fechado.

#figura-nebli("/figuras/replicacao-dna/slide-29.png",
  largura: 60%,
  legenda: [Mecanismo da DNA ligase. Esquerda: ativação da enzima por NAD⁺ (em *E. coli*) ou ATP (eucariotos), gerando o intermediário enzima-AMP. Direita: três passos — (1) DNA com nick, enzima-AMP ativa; (2) AMP transferido para o 5'-P do nick; (3) ataque do 3'-OH, formação da ligação fosfodiéster, liberação de AMP.])

#clinica-box("Antibióticos fluoroquinolonas e a DNA girase", [
  Os antibióticos *fluoroquinolonas* (ciprofloxacino, norfloxacino, levofloxacino) inibem especificamente a DNA girase bacteriana (topoisomerase tipo II), aprisionando o complexo enzima–DNA no estado de fita cortada. O resultado é acúmulo de quebras de dupla-fita no cromossomo bacteriano → morte celular. Como a topoisomerase II de mamíferos tem estrutura diferente da girase bacteriana, as fluoroquinolonas têm seletividade para bactérias. São usadas clinicamente em infecções urinárias (ciprofloxacino para enterobactérias), respiratórias (levofloxacino para pneumococos) e gastrointestinais.
])

#subtopico("3.4 — Eucariotos: mesma lógica, escala maior")

A lógica da replicação eucariota é idêntica à de *E. coli* — separação de fitas, primer de RNA, polimerase principal de alta processividade, remoção do primer e ligação dos fragmentos. O que muda é a escala e a complexidade organizacional.

Uma célula humana precisa copiar *3 bilhões de pares de bases* antes de cada divisão, organizados em cromossomos lineares envoltos por histonas. Com uma única origem de replicação, o processo levaria semanas. A solução: *múltiplas origens de replicação*, uma a cada 3.000–300.000 pb, gerando centenas a milhares de bolhas de replicação simultâneas que se fundem até cobrir todo o genoma.

Em vez das três polimerases procarióticas, os eucariotos têm quatro principais:

- *Pol α* — associada à primase eucariota; sintetiza o primer de RNA e as primeiras dezenas de desoxirribonucleotídeos
- *Pol δ* — polimerase principal da fita retardada (análogo funcional da Pol III); alta processividade, ancorada pelo #sigla("PCNA", [Proliferating Cell Nuclear Antigen — grampo deslizante trimérico de eucariotos; análogo estrutural e funcional do β₂ de *E. coli*])
- *Pol ε* — polimerase principal da fita líder
- *Pol β* — envolvida principalmente no reparo por excisão de bases, não na replicação

O PCNA é o equivalente eucarioto do grampo β₂ — um anel trimérico que ancora as polimerases δ e ε ao molde, garantindo a processividade necessária para percorrer cromossomos de dezenas de megabases.

#figura-nebli("/figuras/replicacao-dna/slide-30.png",
  largura: 65%,
  legenda: [Comparativo procarioto × eucarioto: tempo de replicação (curto vs longo), número de bolhas de replicação (uma vs múltiplas), número de DNA-polimerases (Pol I/II/III em *E. coli* vs Pol α/β/γ/δ em eucariotos). A concepção é idêntica; a implementação é escalada para a complexidade genômica de células com cromossomos e histonas.])

*O problema das extremidades — telômeros e telomerase.* Os cromossomos lineares dos eucariotos têm um problema que os circulares de *E. coli* não têm: quando o último fragmento de Okazaki da fita retardada é sintetizado na extremidade do cromossomo e seu primer é removido, não há DNA à frente para a Pol δ preencher o espaço. O resultado: a cada replicação, as extremidades dos cromossomos ficam alguns pares de bases mais curtas. Essas extremidades são os #termo-nota[telômeros][sequências repetitivas protetoras nas extremidades de cromossomos lineares de eucariotos — TTAGGG em humanos; encurtam progressivamente a cada divisão celular e protegem os genes do encurtamento inicial] — compostos de repetições TTAGGG (em humanos) que protegem o material gênico do encurtamento.

A *telomerase* é a solução para esse problema. Ela é, na prática, uma *transcriptase reversa* que carrega seu próprio molde interno de RNA (componente hTR, ~450 nt em humanos) e usa esse molde para adicionar novas repetições de TTAGGG ao 3' da fita mais longa do telômero — estendendo-a sem precisar de molde de DNA externo. Com a fita 3' estendida pela telomerase, a Pol α/primase pode então sintetizar a fita complementar, completando a replicação da extremidade.

#clinica-box("Telomerase, envelhecimento e câncer", [
  Células somáticas normais têm a telomerase silenciada. A cada divisão, os telômeros encurtam ~50–200 pb — o "relógio biológico" celular (limite de Hayflick: ~50–70 divisões). Quando o telômero atinge comprimento crítico, a célula entra em senescência ou apoptose. Esse mecanismo é um freio natural contra tumores: sem telomerase, células cancerígenas eventualmente morrem pelos telômeros encurtados. Para escapar, *85–90% dos tumores humanos reativam a telomerase*, adquirindo imortalidade replicativa. Por isso a telomerase é um alvo ativo de pesquisa oncológica — inibidores de telomerase podem privar tumores de imortalidade sem afetar células somáticas normais.
])

#conclusao-box[
  A replicação do DNA resolve, de forma elegante, três constrangimentos impostos pela estrutura molecular do DNA. *Primeiro constrangimento:* a polimerase não inicia do zero → solução = primer de RNA feito pela primase, depois removido pela Pol I. *Segundo constrangimento:* a polimerase só sintetiza 5'→3' mas o molde tem dois sentidos → solução = fita líder contínua + fita retardada em fragmentos de Okazaki, cada um 5'→3' mas em direção oposta ao avanço. *Terceiro constrangimento:* separar a dupla-hélice gera superenrolamento à frente → solução = DNA girase aliviando a tensão torcional continuamente.

  O resultado é uma operação com divisão de trabalho precisa: helicase e SSB abrem e estabilizam; primase inicia; Pol III replica com alta processividade (grampo β₂); Pol I remove primers e preenche; ligase sela os nicks. Cada molécula-filha herda uma fita parental intacta e sintetiza uma fita nova complementar — a *replicação semiconservativa* de Watson e Crick, confirmada por Meselson e Stahl com experimento de ultracentrifugação em gradiente de CsCl.

  Na clínica, esse processo é alvo de quimioterápicos (análogos de nucleosídeos bloqueiam as polimerases; agentes intercalantes travam a forquilha) e antibióticos (fluoroquinolonas aprisionam a DNA girase bacteriana). A reativação da telomerase em tumores é um dos marcos moleculares da imortalização neoplásica — e um alvo terapêutico em investigação ativa.

  O próximo tema é a *transcrição* — onde o DNA serve de molde não para se copiar, mas para ser lido como RNA mensageiro. A lógica de molde e complementaridade permanece; a enzima muda (RNA-polimerase, que não precisa de primer) e o produto também (RNA de fita simples, não duplex de DNA).
]
