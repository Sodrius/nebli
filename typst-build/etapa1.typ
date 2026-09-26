#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Depois de uma refeição, o sangue fica cheio de glicose; horas depois, em jejum, essa glicose some da circulação — e mesmo assim o seu cérebro, que só queima glicose, continua funcionando sem falhar. Alguém está segurando a glicemia por trás dos panos. Esse alguém é o *glicogênio*: um polímero de glicose que o fígado monta quando sobra açúcar e desmonta quando falta. No músculo, o mesmo polímero cumpre outro papel — é o tanque de combustível que sustenta os primeiros minutos de um esforço intenso, antes de qualquer outra fonte entrar em campo.

A pergunta que organiza este resumo é direta: *como a célula guarda glicose de um jeito que ela possa ser retirada rápido, sem envenenar a célula com pressão osmótica, e sob controle hormonal fino?* A resposta tem três peças, e cada PARTE pega uma.

Na PARTE I você vai entender a *molécula* e a *lógica do estoque*: por que o glicogênio é ramificado, o que são extremidades redutora e não redutora, por que fígado e músculo guardam glicogênio por motivos opostos, e por que a evolução escolheu um polímero em vez de glicose solta.

Na PARTE II entram as *duas vias*: a degradação (glicogenólise), onde a glicogênio fosforilase corta com fosfato e a enzima desramificadora resolve os galhos; e a síntese (glicogênese), onde a glicose precisa ser "ativada" como UDP-glicose antes de ser costurada ao polímero. Você vai ver por que síntese e degradação são vias *separadas*, não uma o inverso da outra.

Na PARTE III a gente fecha com a *regulação coordenada*: como glucagon e adrenalina disparam uma cascata que fosforila as enzimas e libera glicose, como a insulina desliga tudo pela fosfatase PP1, e por que a fosforilase do fígado é, ela mesma, um sensor de glicose no sangue — coisa que a do músculo não é. No fim, um panorama das doenças de depósito de glicogênio, que são o que acontece quando uma peça dessa máquina falta.
]

#parte-title("PARTE I — A molécula e a lógica do estoque", primeira: true)

#subtopico("1.1 — O glicogênio é uma árvore de glicose com muitas pontas")

Comece pela forma, porque nela já está metade da função. O #termo-nota[glicogênio][polímero ramificado de glicose que é a forma de estoque de carboidrato nos animais; concentra-se em fígado e músculo] é um polímero feito só de resíduos de D-glicose, unidos de dois jeitos diferentes. O tronco e os ramos são cadeias de glicoses ligadas por ligação *α(1→4)* — o carbono 1 de uma glicose amarrado ao carbono 4 da seguinte. A cada oito a doze resíduos, porém, sai um galho: uma ligação *α(1→6)*, em que o carbono 1 de uma glicose se prende ao carbono 6 de outra, criando um ponto de ramificação. O resultado é uma estrutura que lembra uma árvore muito densa, com um único tronco na base e centenas de pontas na copa.

Essas pontas têm nomes que valem a pena fixar agora, porque toda a bioquímica das próximas páginas gira em torno delas. A *extremidade redutora* é uma só: é o carbono 1 (anomérico) da primeira glicose de todas, o ponto pelo qual o polímero inteiro fica preso a uma proteína chamada glicogenina (voltaremos a ela). As *extremidades não redutoras* são muitas — uma para cada galho —, e são os carbonos 4 livres na periferia da molécula. Guarde a ideia central: *é nas extremidades não redutoras que tanto a síntese quanto a degradação trabalham*. Quanto mais galhos, mais pontas; quanto mais pontas, mais enzimas conseguem atacar o polímero ao mesmo tempo.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-07.png",
  largura: 70%,
  legenda: [A arquitetura do glicogênio: tronco e ramos em ligação α(1→4), pontos de ramificação em α(1→6). Uma única extremidade redutora (ancorada à glicogenina) e muitas extremidades não redutoras na periferia — os locais onde as enzimas de síntese e de quebra atuam.])

Aqui mora uma confusão clássica que atravessa toda a bioquímica de carboidratos, e vale desarmá-la de uma vez.

#confusao-prevista(
  titulo: "α(1→4) não é β(1→4): a ligação decide se dá para digerir",
  aluno_acha: [aluno mistura glicogênio, amido e celulose como se a diferença fosse só o tamanho da molécula.],
  mecanismo: [Os três são polímeros de glicose, mas a *ligação* muda tudo. O glicogênio (animais) e o amido (plantas) usam ligação *α*, que as nossas enzimas — amilase, fosforilase — reconhecem e quebram. A celulose usa ligação *β(1→4)*, que o corpo humano não consegue clivar: por isso ela é fibra, passa reto pelo intestino. Além disso, o glicogênio é *muito mais ramificado* que o amido (galhos a cada 8–12 resíduos, contra 24–30 na amilopectina), o que o torna mobilizável mais depressa. Mesma glicose, ligações diferentes, destinos opostos.],
)

Uma nota de aprofundamento que amarra estrutura e velocidade: a ramificação não é enfeite. Cada ponto α(1→6) cria uma nova extremidade não redutora, e é dessas pontas que a glicose sai durante a mobilização. Uma molécula com centenas de pontas pode ser degradada por centenas de moléculas de fosforilase agindo em paralelo — é isso que permite despejar glicose no sangue em segundos, quando a adrenalina manda. A forma ramificada é, literalmente, o que torna o estoque de acesso rápido.

#mini-resumo[O glicogênio é um polímero de glicose com tronco α(1→4) e galhos α(1→6) a cada 8–12 resíduos. Uma extremidade redutora (presa à glicogenina), muitas não redutoras (as pontas de trabalho). Ligação *α* = digerível (glicogênio, amido); ligação *β* = celulose, indigerível. Ramificar = multiplicar pontas = mobilizar rápido.]

#subtopico("1.2 — Dois estoques, duas funções: fígado versus músculo")

O corpo guarda glicogênio principalmente em dois tecidos, e o mesmo polímero serve a propósitos que quase se opõem. No *fígado*, o glicogênio ocupa até 10% da massa do órgão (algo como 50 a 100 g num adulto) e existe para uma missão de interesse público: *manter a glicemia de todo o organismo*. Entre as refeições e durante a noite, o fígado desmonta seu glicogênio e joga glicose livre no sangue, alimentando cérebro, hemácias e todos os tecidos que dependem da glicose circulante.

No *músculo*, o glicogênio representa cerca de 1 a 2% da massa — proporção menor, mas como a massa muscular total é grande, o estoque absoluto é considerável. A função aqui é *egoísta*: o músculo guarda glicogênio para seu próprio consumo, como combustível pronto para a contração. Ele não compartilha essa glicose com ninguém. E há uma razão molecular precisa para isso, que é talvez o detalhe mais cobrado da aula.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-05.png",
  largura: 65%,
  legenda: [Fígado (≈10% da massa, reserva para a glicemia sistêmica) e músculo (≈2% da massa, reserva energética local). No músculo, o estoque é mobilizado durante e após o exercício, para consumo próprio.])

#atencao-box("Por que a glicose do músculo não sai do músculo", [
O músculo *não possui a enzima glicose-6-fosfatase* — a enzima que remove o fosfato da glicose-6-fosfato e libera glicose livre. Sem ela, a glicose derivada do glicogênio muscular fica presa na forma de glicose-6-fosfato, que é carregada e não atravessa a membrana. Resultado: essa glicose só tem um caminho, entrar na glicólise e virar energia ali mesmo. O fígado, ao contrário, *tem* glicose-6-fosfatase, por isso consegue exportar glicose para o sangue. Essa única diferença enzimática explica por que o fígado regula a glicemia de todos e o músculo cuida só de si.
])

Vale um aprofundamento que integra com a via da gliconeogênese: mesmo sem exportar glicose diretamente, o músculo contribui indiretamente para a glicemia. Durante o exercício intenso, o glicogênio muscular vira lactato, que cai no sangue, chega ao fígado e é reconvertido em glicose (o ciclo de Cori). Ou seja, o músculo devolve carbono ao pool de glicose — só que pela via longa, passando pelo fígado, e não por liberação direta.

#mini-resumo[Fígado: glicogênio ≈10% da massa, serve à *glicemia sistêmica* (tem glicose-6-fosfatase, exporta glicose). Músculo: glicogênio ≈2% da massa, serve à *contração local* (sem glicose-6-fosfatase, a glicose fica retida como glicose-6-fosfato e entra na glicólise). A diferença é uma única enzima.]

#subtopico("1.3 — Por que estocar como polímero, e não como glicose solta")

Se o objetivo é ter glicose à mão, por que não guardar glicose livre? A resposta tem dois motivos, e ambos são consequências diretas de ser um polímero. O primeiro é *osmótico*. A pressão osmótica de uma solução depende do número de partículas dissolvidas, não da massa delas. Se uma célula hepática guardasse na forma livre toda a glicose que hoje mantém como glicogênio, seriam centenas de milimols por litro de partículas puxando água para dentro — a célula incharia e estouraria. Ao amarrar milhares de glicoses numa única molécula gigante, a célula reduz o número de partículas osmoticamente ativas para praticamente uma. O glicogênio é um jeito de estocar açúcar sem pagar o preço osmótico.

O segundo motivo é a *velocidade de mobilização*, e aqui a estrutura ramificada volta a ser a heroína. Como vimos, cada galho é uma nova ponta de trabalho; muitas pontas significam muitas enzimas cortando ao mesmo tempo. Quando a adrenalina anuncia perigo, o corpo precisa de glicose *agora* — e o glicogênio entrega, porque a degradação acontece em paralelo em centenas de extremidades.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-08.png",
  largura: 62%,
  legenda: [A glicose armazenada como glicogênio é mobilizada conforme a necessidade: no fígado, para manter o açúcar no sangue; no músculo, para gerar energia quando a demanda sobe.])

Cabe contrastar com a gordura, para não confundir os papéis. O tecido adiposo guarda muito mais energia por grama e é a reserva profunda do corpo — mas é lenta de mobilizar, não rende energia sem oxigênio e não consegue sustentar a glicemia de forma aguda (ácidos graxos não viram glicose líquida no humano). O glicogênio é o oposto: reserva pequena, porém de saque imediato e utilizável até em anaerobiose. Um é a poupança de longo prazo; o outro, o dinheiro no bolso.

#mini-resumo[Estocar como glicogênio, e não glicose livre, resolve dois problemas: *osmótico* (um polímero gigante conta como uma partícula, não puxa água) e *cinético* (a ramificação cria muitas pontas, permitindo mobilização rápida e paralela). Contraste com a gordura: reserva grande, mas lenta e sem sustentar glicemia.]

#parte-title("PARTE II — Quebrar e construir: as duas vias")

#subtopico("2.1 — Glicogenólise: a fosforilase corta com fosfato, não com água")

A degradação começa nas extremidades não redutoras, e a enzima protagonista — reguladora e limitante da glicogenólise — é a *glicogênio fosforilase*. O nome já entrega o truque: ela não hidrolisa a ligação (não usa água), ela faz *fosforólise* — ataca a ligação α(1→4) com um fosfato inorgânico (Pi). A cada corte, sai uma *glicose-1-fosfato* e o polímero encurta em um resíduo. A fosforilase depende de um cofator, o #termo-nota[piridoxal-fosfato][forma ativa da vitamina B6; seu grupo fosfato atua como catalisador ácido-base na fosforilase, doando e recebendo próton na clivagem] (PLP), cujo grupo fosfato participa diretamente da catálise.

Por que cortar com fosfato em vez de água? Porque a fosforólise já entrega o produto na forma útil. A glicose sai *pré-fosforilada*, como glicose-1-fosfato — o que economiza o gasto de um #sigla("ATP", [adenosina trifosfato — a moeda energética da célula]) que seria necessário para fosforilar a glicose depois. E há um bônus: por estar carregada, a glicose-1-fosfato não atravessa a membrana, então o carbono capturado do glicogênio fica retido dentro da célula. Cortar com fosfato é energeticamente esperto e evita vazamento.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-12.png",
  largura: 66%,
  legenda: [Clivagem fosforolítica: a fosforilase usa Pᵢ (não água) para liberar glicose-1-fosfato do glicogênio, com participação do piridoxal-fosfato (PLP). O produto sai já fosforilado — economia de ATP e retenção do carbono na célula.])

Há um limite físico, porém: a fosforilase é uma enzima que só trabalha em cadeia reta e *para quando chega a quatro resíduos de um ponto de ramificação*. O que sobra é uma estrutura de galhos curtos chamada dextrina-limite. Para seguir, entra a *enzima desramificadora*, que é bifuncional — uma única cadeia proteica com duas atividades. Primeiro, sua atividade *transferase* (glicosiltransferase) pega um bloco de três resíduos do galho e o transfere para uma extremidade não redutora vizinha, alongando aquela cadeia. Depois, sua atividade *α(1→6)-glicosidase* hidrolisa o último resíduo, o que ficou preso pela ligação de ramificação — e esse sai como *glicose livre*, não fosforilada.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-14.png",
  largura: 64%,
  legenda: [A enzima desramificadora em dois atos: a transferase move um bloco de três glicoses para uma ponta vizinha; a α(1→6)-glicosidase hidrolisa o resíduo de ramificação, liberando-o como glicose livre.])

Fixe a proporção, porque é um ponto de confusão frequente: a maior parte da glicose do glicogênio sai como *glicose-1-fosfato* (obra da fosforilase, ~90%), e uma fração menor sai como *glicose livre* (obra da glicosidase da enzima desramificadora, ~10%, nos pontos de ramificação). Como aprofundamento clínico, vale saber que a falta da fosforilase muscular causa a doença de McArdle: o músculo não consegue mobilizar o próprio glicogênio, e o paciente tem intolerância ao exercício e não eleva o lactato no esforço — porque o combustível não é liberado.

#mini-resumo[A glicogênio fosforilase faz *fosforólise* (corta com Pᵢ, não água), liberando glicose-1-fosfato pré-fosforilada — economia de ATP + retenção do carbono. Usa PLP (vitamina B6). Para a 4 resíduos do galho; a *enzima desramificadora bifuncional* transfere um bloco de 3 (transferase) e hidrolisa o resíduo α(1→6) (glicosidase), soltando glicose livre. ~90% sai como glicose-1-fosfato, ~10% como glicose livre.]

#subtopico("2.2 — De glicose-1-fosfato ao destino: a bifurcação hepática e muscular")

A glicose-1-fosfato ainda não é a moeda que a célula usa. Uma enzima chamada *fosfoglicomutase* converte glicose-1-fosfato em *glicose-6-fosfato*, numa reação reversível que passa por um intermediário difosforilado (glicose-1,6-bisfosfato). A glicose-6-fosfato é a verdadeira encruzilhada do metabolismo — dela partem a glicólise, a via das pentoses, a devolução ao glicogênio e, no fígado, a liberação de glicose livre.

E é exatamente aqui que os dois tecidos se separam, retomando o que a PARTE I abriu. No *fígado*, a glicose-6-fosfato é levada ao retículo endoplasmático, onde a *glicose-6-fosfatase* remove o fosfato e produz glicose livre, que sai para o sangue e sustenta a glicemia. No *músculo*, que não tem essa fosfatase, a glicose-6-fosfato só pode descer pela glicólise e virar ATP para a contração. A mesma molécula, dois destinos, decididos pela presença ou ausência de uma enzima.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-11.png",
  largura: 72%,
  legenda: [Panorama da glicogenólise: fosforilase e desramificadora liberam glicose-1-fosfato, que a fosfoglicomutase converte em glicose-6-fosfato. No fígado, a glicose-6-fosfatase gera glicose para o sangue; no músculo, a glicose-6-fosfato segue para glicólise, piruvato e lactato.])

Como aprofundamento que conecta com a clínica, a ausência da glicose-6-fosfatase — desta vez no fígado, por defeito genético — causa a doença de von Gierke. Sem a fosfatase, o fígado não libera glicose nem do glicogênio nem da gliconeogênese: o paciente faz hipoglicemia grave em jejum, acumula glicogênio (fígado aumentado) e desvia o excesso de glicose-6-fosfato para lactato, causando acidose. É o retrato do que acontece quando a última porta da via hepática se fecha.

#mini-resumo[A *fosfoglicomutase* converte glicose-1-fosfato em glicose-6-fosfato (reversível). A glicose-6-fosfato é a encruzilhada: no fígado, a *glicose-6-fosfatase* a transforma em glicose livre para o sangue; no músculo, sem essa enzima, ela entra na glicólise. Falha hepática da glicose-6-fosfatase = doença de von Gierke (hipoglicemia de jejum, hepatomegalia, acidose láctica).]

#subtopico("2.3 — Glicogênese: a glicose ativada (UDP-glicose) e a costura do polímero")

A síntese *não é a degradação ao contrário* — é uma via própria, com enzimas próprias, e isso é proposital: vias separadas podem ser reguladas de forma independente, ligando uma e desligando a outra. O ponto de partida é a glicose-6-fosfato, que a fosfoglicomutase converte em glicose-1-fosfato (a mesma reação de antes, no sentido inverso). Mas, antes de ser costurada ao polímero, a glicose precisa ser *ativada*.

A ativação é a jogada central da via. A glicose-1-fosfato reage com *#sigla("UTP", [uridina trifosfato — nucleotídeo que ativa a glicose para a síntese, análogo ao ATP])* — uma molécula-irmã do ATP —, formando *UDP-glicose* e liberando pirofosfato (PPi). A enzima é a UDP-glicose pirofosforilase. Sozinha, essa reação seria facilmente reversível; o que a torna irreversível na prática é o destino do pirofosfato: uma pirofosfatase o hidrolisa imediatamente em dois fosfatos, e essa quebra puxa a reação para frente de forma definitiva. A UDP-glicose é a *forma ativada da glicose* — a peça pronta para ser encaixada. (Foi Luis Leloir quem descobriu esse mecanismo, rendendo-lhe o Nobel de Química de 1970.)

#figura-nebli("/figuras/bioq-24-glicogenio/slide-18.png",
  largura: 60%,
  legenda: [Ativação da glicose: glicose-1-fosfato + UTP formam UDP-glicose + pirofosfato (PPᵢ). A hidrólise imediata do pirofosfato em dois Pᵢ torna a reação irreversível — a UDP-glicose é a forma ativada, pronta para a síntese.])

Com a peça ativada, entra a *glicogênio sintase* — a enzima reguladora e limitante da glicogênese: ela transfere a glicose da UDP-glicose para uma extremidade não redutora do glicogênio, formando uma nova ligação α(1→4) no carbono 4. Há um detalhe importante — a sintase *não sabe começar do zero*: ela só alonga uma cadeia que já tenha ao menos quatro resíduos. Quem fornece esse primer inicial é a *glicogenina*, uma proteína que catalisa a própria glicosilação, ligando as primeiras glicoses a um resíduo de tirosina seu e permanecendo presa à extremidade redutora do polímero para sempre. Todo glicogênio nasce, portanto, grudado a uma glicogenina.

Mas a sintase só faz cadeia reta. Para criar os galhos que dão ao glicogênio sua forma ramificada, entra a *enzima ramificadora* (uma amilo-(1,4→1,6)-transglicosilase): quando um ramo cresce o suficiente, ela recorta um bloco de cerca de sete resíduos da ponta e o reconecta mais para dentro, por uma ligação α(1→6), criando um novo galho. É essa enzima que constrói a árvore.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-21.png",
  largura: 58%,
  legenda: [A glicogenina inicia a molécula: com atividade de glicosiltransferase, monta o primer inicial e permanece ancorada à extremidade redutora. A glicogênio sintase depois alonga as cadeias, e a enzima ramificadora abre os galhos.])

Feche a via com o balanço energético, que também vale fixar bem: *a síntese custa 2 ATP por glicose incorporada*. Um ATP foi gasto lá atrás para fosforilar a glicose em glicose-6-fosfato (pela hexoquinase ou glicoquinase); o segundo é o custo de regenerar o UTP a partir do UDP liberado pela sintase (o UDP é refosforilado às custas de um ATP). Sintetizar glicogênio é, portanto, um investimento: gasta-se energia para guardar energia.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-23.png",
  largura: 68%,
  legenda: [Contabilidade da glicogênese: 1 ATP na fosforilação inicial da glicose + 1 ATP na regeneração do UTP = 2 ATP gastos por glicose adicionada ao glicogênio. Guardar energia custa energia.])

#mini-resumo[Síntese é via *separada* da degradação. Glicose-1-fosfato + UTP → *UDP-glicose* (forma ativada; a hidrólise do PPᵢ torna a reação irreversível — Leloir, Nobel 1970). A *glicogênio sintase* transfere a glicose para o C4 de uma cadeia (α1→4), mas precisa de primer de ≥4 resíduos, fornecido pela *glicogenina* (fica presa à extremidade redutora). A *enzima ramificadora* cria os galhos α(1→6). Custo: *2 ATP por glicose*.]

#parte-title("PARTE III — A regulação coordenada")

#subtopico("3.1 — O princípio: nunca as duas vias ao mesmo tempo")

Duas vias opostas que compartilham metabólitos criam um risco óbvio: se síntese e degradação rodassem juntas, a célula ficaria montando e desmontando glicogênio sem parar, gastando ATP e não produzindo nada — um ciclo fútil. Por isso o metabolismo do glicogênio é regulado de forma *recíproca*: o sinal que liga uma via desliga a outra, sempre. Essa coordenação opera em três camadas que se somam: *alostérica* (metabólitos que sinalizam o estado energético da célula), *covalente* (fosforilação e desfosforilação das enzimas em resposta a hormônios) e *hormonal* (o comando de cima, que decide o sentido).

#figura-nebli("/figuras/bioq-24-glicogenio/slide-24.png",
  largura: 60%,
  legenda: [Três camadas de regulação coordenada: efetores alostéricos, modificação covalente por fosforilação e comando hormonal. Síntese e degradação são reguladas em sentidos opostos, para nunca operarem simultaneamente.])

A elegância do desenho é que uma *única* modificação — a fosforilação — tem efeitos *opostos* nas duas enzimas: fosforilar *ativa* a fosforilase (liga a degradação) e ao mesmo tempo *inativa* a sintase (desliga a síntese). Um comando, dois efeitos casados, sentidos contrários. Guardar essa assimetria é a chave para não se perder na cascata que vem a seguir.

#mini-resumo[Síntese e degradação são reguladas *reciprocamente* para evitar ciclo fútil. Três camadas: alostérica (estado energético), covalente (fosforilação), hormonal (comando). Regra de ouro: *a fosforilação ativa a fosforilase e inativa a sintase* — um sinal, efeitos opostos nas duas vias.]

#subtopico("3.2 — A cascata do glucagon e da adrenalina: fosforilar para quebrar")

Quando o corpo precisa de glicose — jejum, para o fígado; luta ou fuga, para o músculo —, os hormônios *glucagon* (fígado) e *adrenalina* (músculo e fígado) disparam a mesma lógica. Eles se ligam a receptores de membrana acoplados à proteína G, que ativam a *adenilato-ciclase*, que fabrica *#sigla("AMPc", [adenosina-monofosfato cíclico — segundo mensageiro intracelular gerado a partir do ATP])* a partir de ATP. O AMPc é o segundo mensageiro, e seu alvo é a *#sigla("PKA", [proteína-quinase A — enzima ativada pelo AMPc que fosforila alvos da cascata])*.

A PKA ativa, então, dispara os dois efeitos casados. De um lado, ela fosforila e ativa a *fosforilase-quinase*, que por sua vez fosforila a glicogênio fosforilase, convertendo-a de *fosforilase b* (menos ativa) em *fosforilase a* (ativa) — a degradação liga. De outro lado, a mesma PKA fosforila a *glicogênio sintase*, inativando-a — a síntese desliga. Um hormônio, uma cascata, as duas vias ajustadas em sentidos opostos.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-32.png",
  largura: 66%,
  legenda: [A cascata de ativação: hormônio → receptor acoplado à proteína G → adenilato-ciclase → AMPc → PKA → fosforilase-quinase → fosforilase a. Cada nível amplifica o sinal, e o mesmo AMPc que liga a quebra desliga a síntese.])

A palavra-chave dessa arquitetura é *amplificação*. Cada etapa da cascata é uma enzima ativando muitas cópias da enzima seguinte, de modo que *uma* molécula de hormônio acaba liberando *milhões* de moléculas de glicose. É por isso que um susto libera açúcar no sangue quase instantaneamente.

No músculo, soma-se a essa cascata hormonal uma camada *alostérica* afinada ao esforço. Durante o exercício, o AMP se acumula (sinal de que o ATP está sendo consumido) e ativa diretamente a fosforilase b, empurrando-a para o estado R (relaxado, ativo) — sem precisar de fosforilação. Já o ATP e a glicose-6-fosfato, sinais de fartura energética, empurram a enzima para o estado T (tenso, inativo). E há uma conexão engenhosa com a contração: o cálcio liberado para contrair o músculo também ativa a fosforilase-quinase (por meio de uma subunidade calmodulina), acoplando o próprio ato de contrair à mobilização do combustível.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-28.png",
  largura: 64%,
  legenda: [Fosforilase muscular: o AMP (energia baixa) favorece o estado R ativo; ATP e glicose-6-fosfato favorecem o estado T inativo. A adrenalina, via fosforilação, converte b em a; o cálcio da contração ativa a fosforilase-quinase pela calmodulina.])

#confusao-prevista(
  titulo: "Fosforilase a e b, estado T e R: dois eixos diferentes",
  aluno_acha: [aluno confunde o par a/b (modificação covalente) com o par T/R (alosteria), como se fossem a mesma coisa.],
  mecanismo: [São dois controles independentes que convergem na mesma enzima. *a versus b* é sobre *fosforilação*: a fosforilase *a* está fosforilada (efeito do hormônio), a *b* está desfosforilada. *T versus R* é sobre *conformação alostérica*: T é tenso/inativo, R é relaxado/ativo. A fosforilase *a* tende ao estado R (ativa por padrão); a *b* tende ao T, mas o AMP pode empurrá-la para R no músculo em exercício. Ou seja: o hormônio age por a/b, o estado energético age por T/R, e os dois se somam.],
)

#mini-resumo[Glucagon (fígado) e adrenalina (músculo/fígado) acionam, pela proteína G, a adenilato-ciclase, que faz *AMPc*, que ativa a *PKA*. A PKA ativa a *fosforilase-quinase* (fosforilase b vira a, degradação liga) e inativa a *sintase* (síntese desliga). A cascata *amplifica* (um hormônio → milhões de glicoses). No músculo: AMP ativa (estado R), ATP/glicose-6-fosfato inibem (estado T); o Ca²⁺ da contração ativa a fosforilase-quinase.]

#subtopico("3.3 — Desligar a máquina: insulina, PP1 e o sensor de glicose do fígado")

Ligar a degradação é metade da história; saber *desligá-la* e voltar a estocar é a outra. Dois mecanismos apagam a cascata. Primeiro, a *fosfodiesterase* degrada o AMPc, convertendo-o em AMP comum: sem AMPc, a PKA volta ao repouso e para de fosforilar as enzimas. Segundo, e mais importante, a *insulina* — hormônio da fartura, liberado após a refeição — ativa a *#sigla("PP1", [proteína-fosfatase 1 — desfosforila as enzimas do glicogênio, revertendo a ação da PKA])*, que faz o serviço inverso da PKA: ela *desfosforila* as enzimas. Ao remover o fosfato, a PP1 converte a fosforilase a de volta em b (desliga a degradação) e converte a sintase de sua forma inativa para a ativa (liga a síntese). Novamente, um só agente, efeitos opostos casados — só que agora no sentido de armazenar.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-36.png",
  largura: 64%,
  legenda: [O desligamento: a fosfodiesterase converte AMPc em AMP (encerra o sinal da PKA); a proteína-fosfatase 1 (PP1), estimulada pela insulina, desfosforila as enzimas — inativa a fosforilase e ativa a sintase, revertendo a célula para o modo de síntese.])

Sobre a sintase, vale explicitar a simetria que fecha a lógica da PARTE III: a *glicogênio sintase a* (ativa) é a forma *desfosforilada*, e a *sintase b* (inativa) é a *fosforilada* — exatamente o inverso da fosforilase. Por isso a fosforilação tem "efeitos opostos" nas duas: o mesmo fosfato que acorda a fosforilase adormece a sintase, e a mesma PP1 que adormece a fosforilase acorda a sintase.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-39.png",
  largura: 62%,
  legenda: [Regulação recíproca por fosforilação: na fosforilase, a forma fosforilada (a) é ativa; na sintase, a forma fosforilada (b) é inativa. O mesmo evento covalente liga a degradação e desliga a síntese — e a desfosforilação faz o contrário.])

Falta o toque mais fino, que distingue o fígado do músculo e retoma o papel de "guardião da glicemia". No fígado, a *fosforilase a funciona como um sensor direto de glicose*. Quando a glicemia sobe, a glicose se liga à fosforilase a e a empurra para o estado T (inativo), o que expõe seu fosfato à PP1 — a fosforilase é então desfosforilada e desligada, *e* a PP1 liberada vai ativar a sintase. Assim, o próprio nível de glicose no sangue comanda o fígado a parar de quebrar e começar a estocar, sem precisar de intermediário. No músculo isso não acontece: a fosforilase muscular *não é sensível à glicose*, porque o músculo responde ao seu próprio estado energético (AMP), não à glicemia — afinal, não é ele que regula o açúcar do sangue.

#figura-nebli("/figuras/bioq-24-glicogenio/slide-30.png",
  largura: 62%,
  legenda: [O fígado como sensor de glicemia: níveis altos de glicose deslocam a fosforilase a hepática do estado R para o T, expondo-a à desfosforilação pela PP1. A fosforilase muscular, ao contrário, responde ao AMP e não à glicose.])

#clinica-box("Doenças de depósito de glicogênio", [
As *glicogenoses* são doenças autossômicas recessivas em que falta uma das enzimas da via — e cada enzima ausente produz um quadro característico, de modo que reconhecer o defeito é reconstruir a via de trás para frente. O glicogênio acumulado cora fortemente pelo #termo-nota[PAS][ácido periódico de Schiff — coloração histológica que marca carboidratos, útil para identificar o glicogênio acumulado nas glicogenoses], o que ajuda a identificá-las na biópsia.

Na *doença de von Gierke* (tipo I) falta a glicose-6-fosfatase hepática: como o fígado não libera glicose nem do glicogênio nem da gliconeogênese, há hipoglicemia grave de jejum e fígado muito aumentado; o excesso de glicose-6-fosfato é desviado, elevando *lactato*, *triglicérides* e *ácido úrico* (podendo causar gota secundária). Na *doença de Pompe* (tipo II) falta a maltase ácida lisossomal — a exceção que degrada glicogênio dentro do lisossomo, fora da regulação citosólica —, com acúmulo em coração e músculo que leva a cardiomegalia (miocardiopatia hipertrófica), hipotonia e fraqueza muscular. Na *doença de Cori* (tipo III) falta a enzima desramificadora: sobra glicogênio com galhos curtos (dextrina-limite); é uma forma mais branda que a de von Gierke, com lactato normal, porque a gliconeogênese continua funcional. Na *doença de Andersen* (tipo IV) falta a enzima ramificadora, gerando um glicogênio anormal, pouco ramificado. Na *doença de McArdle* (tipo V) falta a fosforilase muscular: intolerância ao exercício, cãibras e ausência da elevação normal de lactato no esforço, muitas vezes com urina escura por mioglobinúria (rabdomiólise) e o clássico "segundo fôlego" quando o fluxo sanguíneo ao músculo aumenta. Na *doença de Hers* (tipo VI) falta a fosforilase hepática: hipoglicemia de jejum mais leve e hepatomegalia — no fígado, o espelho do que McArdle é no músculo.
])

#mini-resumo[Desligar a cascata: a *fosfodiesterase* degrada o AMPc; a *insulina* ativa a *PP1*, que desfosforila as enzimas — inativa a fosforilase, ativa a sintase (modo síntese). *Sintase a* = desfosforilada/ativa (inverso da fosforilase). No fígado, a *fosforilase a é sensor de glicose*: glicose alta → estado T → PP1 a desliga e libera a sintase. No músculo, não há esse sensor (responde a AMP). Faltas enzimáticas = doenças de depósito (von Gierke, Pompe, Cori, McArdle).]

#conclusao-box[
Chegamos ao princípio unificador: *o glicogênio é energia guardada de um jeito que pode ser sacada rápido e sob controle preciso*. Tudo o que estudamos serve a essa frase. A *forma ramificada* resolve o osmótico e cria as muitas pontas que permitem mobilização veloz. A *fosforólise* devolve a glicose já fosforilada, economizando ATP e prendendo o carbono na célula, enquanto a *desramificadora* resolve os galhos. A *síntese*, via separada, ativa a glicose como *UDP-glicose* e gasta 2 ATP para estocar — porque guardar energia é um investimento que vale a pena.

O mecanismo nuclear, que amarra a PARTE III, é a *reciprocidade por fosforilação*: um único evento covalente liga a degradação e desliga a síntese, e a desfosforilação faz o oposto — de modo que as duas vias nunca correm juntas. Em cima disso, os hormônios decidem o sentido (glucagon e adrenalina quebram; insulina estoca) e a alosteria afina pelo estado energético (AMP no músculo, glicose no fígado).

A clínica retomada mostra o custo de cada falha: von Gierke fecha a saída hepática, Pompe entope o lisossomo, Cori deixa galhos por resolver, McArdle trava o combustível do músculo. E a projeção para as próximas aulas é natural: a glicose-6-fosfato que aparece o tempo todo aqui é a mesma encruzilhada da glicólise, da gliconeogênese e da via das pentoses — o glicogênio é uma das portas desse centro, e entender essa porta é entender como o corpo equilibra estocar e gastar açúcar ao longo do dia.
]
