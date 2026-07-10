#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Imagine que você precisa estudar um único gene humano — o da insulina, digamos. Esse gene é uma frase minúscula perdida em uma enciclopédia de três bilhões de letras, e dentro de cada célula existe apenas *uma cópia* dele em cada cromossomo. Para fazer qualquer coisa útil — ler a sequência, produzir a proteína, testar se um paciente carrega uma mutação — você precisa primeiro de duas coisas: *isolar* esse pedaço específico e *multiplicá-lo* até ter bilhões de cópias idênticas na mão.

  A tecnologia do DNA recombinante é exatamente o conjunto de truques que resolve esse problema. Ela tem dois motores de cópia que vamos destrinchar: a *PCR*, que copia o DNA dentro de um tubo de ensaio, e a *clonagem molecular*, que sequestra uma bactéria e a obriga a copiar o DNA para você. Para a clonagem funcionar, três ferramentas de bancada precisam se encaixar: uma tesoura molecular que corta o DNA em pontos exatos, uma cola que junta pedaços de origens diferentes, e um veículo que carrega o pedaço para dentro da bactéria. Este resumo segue essa lógica: primeiro a grande ideia, depois a PCR, e por fim a bancada completa da clonagem.
]

#parte-title("PARTE I — O problema e a grande ideia", primeira: true)

#subtopico("1.1 — Por que copiar um pedaço específico de DNA")

O DNA tem uma propriedade que o torna o material genético mais fácil de manipular na bancada: ele é uma molécula *previsível e modular*. Cada fita é uma sequência de quatro letras, e cada letra só pareia com uma parceira — A com T, G com C. Essa regra de pareamento é o que permite cortar, colar e copiar DNA de forma controlada, porque sempre que você conhece uma fita, conhece automaticamente a outra. É essa previsibilidade que a tecnologia do DNA recombinante explora do começo ao fim.

#sigla("DNA", [ácido desoxirribonucleico — o polímero de quatro bases que guarda a informação genética])

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-18.png",
  largura: 50%,
  legenda: [Dentro do cromossomo compactado, o que a tecnologia do DNA recombinante quer alcançar é uma *região específica* da dupla-hélice — isolá-la do resto e obtê-la em grande quantidade.])

O ponto de partida é sempre o mesmo obstáculo prático: a região que interessa está presente em quantidade ínfima e misturada a todo o resto do genoma. Determinar a sequência de um gene, produzir a proteína que ele codifica, fazer um teste de paternidade, diagnosticar uma doença genética ou identificar um vírus a partir do seu material genético — todas essas tarefas exigem *muitas cópias puras* daquele trecho. Daí o desafio central que organiza toda a aula é sempre o mesmo: como sair de uma cópia diluída para bilhões de cópias isoladas? Há dois caminhos, e a tecnologia usa os dois conforme a conveniência: copiar o trecho quimicamente num tubo (PCR) ou inseri-lo numa bactéria e deixar a bactéria se multiplicar carregando o trecho dentro dela (clonagem).

#mini-resumo[O DNA é manipulável porque o pareamento de bases é uma regra fixa: conhecer uma fita é conhecer a outra. O problema prático é sempre obter muitas cópias puras de um trecho específico.]

#subtopico("1.2 — DNA recombinante e o organismo quimérico")

DNA recombinante é, ao pé da letra, uma molécula de DNA montada com pedaços que *não estavam juntos na natureza*. Você pega um fragmento de um organismo — o gene humano da insulina, por exemplo — e o emenda a uma molécula de DNA de outra origem, geralmente de uma bactéria. O resultado é uma molécula híbrida, recombinada, que nunca existiria sem a intervenção da bancada.

#figura-lateral("/figuras/biomol-26-dna-recombinante-pcr/slide-07.png",
  lado: "right",
  largura-figura: 30%,
  texto: [O nome técnico para um organismo que carrega material genético de outra espécie é *quimera*, emprestado da mitologia grega: a criatura com cabeça de leão, corpo de cabra e cauda de dragão. Quando uma bactéria passa a carregar e expressar o gene humano da insulina, ela é, nesse sentido literal, um organismo quimérico — uma fábrica viva de uma proteína que não é dela.],
  legenda: [A quimera mitológica: partes de organismos distintos no mesmo corpo.])

Essa capacidade de combinar genomas é o que dá à tecnologia o seu poder quase ilimitado: introduzir genes em bactérias para produzir insulina humana, hormônio de crescimento ou vacinas; introduzir genes em plantas e animais para gerar organismos *transgênicos*; estudar como um gene é replicado e expresso colocando-o num contexto controlado. Tudo isso depende de um gesto único — recortar DNA de uma fonte e colá-lo noutra de forma estável.

#confusao-prevista(
  titulo: "Clonagem molecular não é clonagem reprodutiva",
  aluno_acha: [aluno associa "clonagem" à ovelha Dolly — copiar um indivíduo inteiro.],
  mecanismo: [na biologia molecular, *clonar* significa obter muitas cópias idênticas de *um fragmento de DNA*. O termo vem da genética bacteriana: uma colônia de bactérias é um clone porque todas descendem de uma só célula e são geneticamente idênticas. Clonagem molecular é multiplicar uma sequência, não um organismo.],
)

#subtopico("1.3 — Clonagem molecular em dois estágios")

A clonagem molecular é a técnica central de todo o campo, e ela se resume a dois estágios encadeados. No *primeiro estágio*, o fragmento de DNA de interesse — chamado de *inserto* — é ligado a uma segunda molécula de DNA capaz de se replicar dentro de uma célula. Essa segunda molécula é o #termo-nota[vetor][molécula de DNA que se replica dentro de uma célula hospedeira e carrega o inserto junto — plasmídeo, fago, cosmídeo, BAC ou YAC]. A junção do inserto com o vetor produz justamente a molécula de DNA recombinante.

No *segundo estágio*, essa molécula recombinante é introduzida numa célula hospedeira compatível — em geral uma bactéria — num processo chamado #termo-nota[transformação][entrada de DNA exógeno em uma bactéria, que passa a replicá-lo como se fosse seu]. A partir daí, a natureza faz o trabalho pesado: a célula hospedeira se divide indefinidamente, e a cada divisão copia também o vetor com o inserto dentro. Em poucas horas, uma única bactéria transformada vira uma colônia de milhões — todas carregando cópias idênticas do fragmento. Esse é o clone.

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-08.png",
  largura: 58%,
  legenda: [Os dois estágios condensados: o plasmídeo recombinante (já portando o inserto) entra na célula hospedeira _E. coli_; a célula transformada passa a se dividir, copiando o DNA recombinante a cada geração. A multiplicação da bactéria é a multiplicação do DNA.])

O contraste entre os dois motores de cópia já fica visível aqui. A clonagem terceiriza a multiplicação para um ser vivo — é mais trabalhosa de montar, mas entrega o fragmento dentro de um sistema biológico que pode expressá-lo como proteína. A PCR, que veremos a seguir, faz o oposto: dispensa a célula e copia o DNA quimicamente, num tubo, em poucas horas. Para montar o vetor recombinante do primeiro estágio, no entanto, precisaremos das três ferramentas de bancada — a tesoura, a cola e o veículo — que são o assunto da PARTE III. Antes disso, vamos ao motor que revolucionou a biologia molecular.

#sintese-box(1)[Clonagem molecular = dois estágios: (1) ligar o inserto a um vetor, formando DNA recombinante; (2) transformar uma bactéria, que multiplica o conjunto ao se dividir. O clone é a colônia de células geneticamente idênticas carregando o fragmento.]

#parte-title("PARTE II — PCR: a fábrica de cópias num tubo")

#subtopico("2.1 — Replicação in vitro dirigida por iniciadores")

A reação em cadeia da polimerase parte de uma constatação simples: a célula já sabe copiar DNA com perfeição na replicação. A #sigla("PCR", [reação em cadeia da polimerase — método in vitro de amplificação seletiva de DNA]) apenas toma emprestada essa maquinaria e a faz rodar dentro de um tubo, sob controle do experimentador. Foi desenvolvida por Kary Mullis em 1983, rendeu-lhe o Nobel de Química de 1993, e o que ela entrega é espetacular: a amplificação seletiva de uma sequência definida de DNA a partir de uma amostra complexa, gerando em poucas horas bilhões de cópias daquele trecho e só dele.

A palavra-chave é *seletiva*, e é aqui que mora a primeira condição de quebra. A PCR não copia o DNA inteiro — ela copia apenas a região delimitada por dois *iniciadores* (os #termo-nota[iniciadores][pequenas sequências de DNA fita simples, os "primers", que pareiam nas bordas da região-alvo e dão à polimerase um ponto de partida]), pequenos trechos de fita simples que pareiam, um em cada borda da região-alvo. A polimerase só consegue estender a partir de um iniciador já pareado. Consequência direta e inescapável: *as sequências que flanqueiam a região a ser amplificada precisam ser conhecidas de antemão*, porque sem conhecê-las você não consegue desenhar os iniciadores. A PCR é cega ao que está no meio do alvo, mas exige conhecer com precisão as duas pontas.

#mini-resumo[A PCR amplifica só o trecho entre dois iniciadores. Por isso, é obrigatório conhecer as sequências que flanqueiam o alvo — os iniciadores são desenhados contra elas.]

A mistura inicial da reação reúne quatro ingredientes num só tubo: o DNA-molde de fita dupla que contém o alvo, um par de iniciadores de fita simples, os quatro #sigla("dNTP", [desoxirribonucleotídeos trifosfato — os tijolos A, T, G e C usados para construir as novas fitas]) que servem de matéria-prima, e a enzima DNA-polimerase que monta as cópias. A reação então roda em ciclos, e cada ciclo é, no fundo, um jogo de *temperatura*.

#subtopico("2.2 — Os três passos do ciclo e o crescimento 2 elevado a n")

Cada ciclo da PCR tem três passos, e cada passo é definido por uma temperatura específica que liga ou desliga uma etapa da cópia. O gráfico abaixo mostra a alternância no tempo.

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-19.png",
  largura: 68%,
  legenda: [Um ciclo de PCR como uma onda de temperatura: sobe a 95 °C para *desnaturar*, desce a ~55 °C para os iniciadores *anelarem*, sobe a 72 °C para a polimerase *estender* as novas fitas. O ciclo se repete dezenas de vezes.])

O *primeiro passo é a desnaturação*, a 93–95 °C por cerca de 30 segundos a 1 minuto. O calor rompe as pontes de hidrogênio entre as duas fitas e separa a dupla-hélice em duas fitas simples — cada uma agora disponível como molde. O *segundo passo é o anelamento*, entre 37 e 65 °C: ao baixar a temperatura, os iniciadores encontram suas sequências complementares nas bordas do alvo e pareiam ali. A temperatura exata depende da composição do iniciador — quanto mais forte o pareamento previsto, mais alta a temperatura que ele tolera sem se soltar. O *terceiro passo é a extensão*, a 72 °C: a polimerase se acopla a cada iniciador pareado e sintetiza a fita complementar, percorrendo o molde e incorporando os dNTP na direção certa, gerando cópias idênticas da região-alvo.

Agora vem o detalhe que dá à técnica o nome de "reação em cadeia". Ao final de um ciclo, cada molde original virou dois. No ciclo seguinte, esses dois viram quatro; depois oito, dezesseis, e assim por diante. O número de cópias cresce como *2ⁿ*, onde n é o número de ciclos. Com 25 a 35 ciclos típicos, 2ⁿ chega à casa dos bilhões — é por isso que partir de pouquíssimo DNA-molde basta.

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-24.png",
  largura: 52%,
  legenda: [A partir do segundo ciclo, começam a se acumular fragmentos delimitados *exatamente* pelos iniciadores nas duas pontas. São essas cópias de tamanho definido que se multiplicam exponencialmente — 2ⁿ ao longo de n ciclos.])

#mini-resumo[Desnaturar (95 °C, separa as fitas) → anelar (~55 °C, iniciadores pareiam) → estender (72 °C, polimerase copia). Cada ciclo dobra o número de cópias: 2ⁿ após n ciclos.]

#subtopico("2.3 — Taq polimerase e o preço da termoestabilidade")

A descrição acima esconde um problema sério que quase matou a PCR no berço. A cada ciclo, a reação sobe a 95 °C para desnaturar o DNA — mas uma polimerase comum, como a das nossas células, é uma proteína que *também* desnatura a 95 °C. Nos primeiros experimentos, era preciso adicionar enzima nova a cada ciclo, porque o calor destruía a anterior. A solução não veio da engenharia, e sim da ecologia: existem bactérias *extremófilas* que vivem em fontes termais a temperaturas altíssimas, e as enzimas delas evoluíram para funcionar nesse calor sem se desnaturar.

#figura-lateral("/figuras/biomol-26-dna-recombinante-pcr/slide-14.png",
  lado: "left",
  largura-figura: 36%,
  texto: [A primeira DNA-polimerase #termo-nota[termoestável][que mantém sua estrutura e atividade em temperaturas que desnaturariam uma proteína comum] purificada foi a *Taq polimerase*, isolada da bactéria _Thermus aquaticus_, encontrada nas fontes termais do Parque Yellowstone. Por ser termoestável, a Taq sobrevive aos repetidos saltos a 95 °C; basta colocá-la uma vez no início. Sua atividade tem pico justamente perto de 72 °C — exatamente a temperatura de extensão.],
  legenda: [Fontes termais de Yellowstone, habitat de _Thermus aquaticus_.])

A termoestabilidade veio com um custo, e esse custo importa muito quando a PCR alimenta uma clonagem ou um sequenciamento. A Taq *não tem atividade exonuclease 3'→5'* — ou seja, ela não revisa o que acabou de incorporar. Uma polimerase com revisão volta atrás quando coloca a base errada e a remove; a Taq apenas segue em frente. O resultado é uma taxa de erro de cerca de 1 base errada a cada 20 mil bases copiadas. Para muitos usos isso é tolerável, mas quando a fidelidade é crítica usam-se polimerases também termoestáveis isoladas de arqueias — *Pfu* e *Pwo* — que *têm* a atividade revisora 3'→5' e reduzem drasticamente os erros de amplificação.

#atencao-box("Termoestável não quer dizer fiel", [
  É fácil juntar duas qualidades que não andam juntas. A Taq é valiosa por ser *termoestável* — resiste ao calor dos ciclos. Mas ser termoestável nada diz sobre *fidelidade*: a Taq erra com frequência porque lhe falta a revisão exonuclease 3'→5'. Se você vai clonar e expressar o produto, ou sequenciá-lo, um erro introduzido pela Taq vira uma mutação fixa em todas as cópias seguintes. Para esses casos, escolhe-se uma polimerase revisora (Pfu, Pwo), que também é termoestável mas, além disso, corrige.
])

#clinica-box("PCR no diagnóstico", [
  A sensibilidade da PCR — amplificar a partir de pouquíssimo material — é o que a tornou central na medicina. A partir de uma quantidade mínima de DNA ou RNA, ela permite detectar diretamente o material genético de um agente infeccioso (um vírus, uma bactéria) antes mesmo de o corpo montar resposta detectável, identificar mutações em doenças genéticas e fazer investigação forense e de paternidade pela análise direta do DNA. Em todos esses casos, o que se testa é a presença de uma sequência específica — e a PCR só a amplifica se os iniciadores corresponderem a ela.
])

#sintese-box(2)[A PCR copia DNA in vitro em ciclos de temperatura, dobrando o material a cada ciclo (2ⁿ). A Taq polimerase, termoestável, viabilizou a automação, mas paga com infidelidade por não ter revisão 3'→5'; quando a fidelidade importa, usam-se Pfu/Pwo.]

#parte-title("PARTE III — A bancada da clonagem")

#subtopico("3.1 — Enzimas de restrição: a tesoura da bactéria")

Para montar o vetor recombinante do primeiro estágio da clonagem, é preciso primeiro *cortar* o DNA em pontos definidos. A ferramenta que faz isso não foi inventada no laboratório: ela é um sistema de defesa bacteriano descoberto por acaso. Observou-se que certos bacteriófagos (vírus que infectam bactérias) não conseguiam crescer em determinadas linhagens — e a razão era a presença, nessas bactérias, de nucleases que clivavam o DNA viral invasor. A bactéria, em outras palavras, *restringe* o crescimento do fago degradando o DNA estranho. Daí o nome: enzimas de restrição.

Isso levanta de imediato um paradoxo: se a enzima corta DNA estranho, por que não corta o próprio DNA da bactéria, que tem as mesmas sequências? A resposta é o segundo braço do sistema, chamado de *modificação*. A bactéria marca o seu próprio DNA com grupos metila em bases específicas dentro dos sítios de reconhecimento. A metilação funciona como um crachá: o DNA marcado é reconhecido como "próprio" e *não* é clivado; o DNA do fago, sem a marca, é cortado. Por isso o conjunto é chamado de sistema de *restrição-modificação*.

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-29.jpeg",
  largura: 52%,
  legenda: [O mesmo sítio é *clivado* quando nu e *protegido* quando uma de suas bases recebe um grupo metila (aqui, uma adenina metilada, A\*). A metilação é o crachá que distingue o DNA próprio do DNA invasor.])

As enzimas mais úteis para a tecnologia são as do *Tipo II*: pequenas, simples, e com uma propriedade que as torna precisas — elas clivam o DNA *no mesmo sítio que reconhecem*. E esse sítio tem uma geometria especial: é uma sequência #termo-nota[palindrômica][lida igual nas duas fitas no sentido 5'→3', graças à simetria do pareamento — uma repetição invertida], uma repetição invertida. Vale a pena ver o que isso significa exatamente.

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-34.jpeg",
  largura: 54%,
  legenda: [O sítio de reconhecimento tem um *eixo de simetria*: lendo a fita de cima de 5' para 3' obtém-se a mesma sequência que lendo a de baixo de 5' para 3'. Os dois pontos de clivagem ficam dispostos simetricamente em torno desse eixo.])

#confusao-prevista(
  titulo: "Palíndromo genético não é palíndromo de palavra",
  aluno_acha: [aluno imagina "arara" — a mesma fita lida de trás para frente.],
  mecanismo: [no DNA, o palíndromo é entre as *duas fitas*: a sequência da fita de cima lida 5'→3' é idêntica à da fita de baixo lida 5'→3'. Em GAATTC, a fita complementar também é GAATTC no seu próprio sentido 5'→3'. É a simetria de dupla-fita que a enzima reconhece.],
)

O modo de cortar divide as enzimas em dois grupos de enorme consequência prática. Algumas, como a HaeIII ou a EcoRV, fazem um *corte reto*: cortam as duas fitas na mesma posição, deixando extremidades de fita dupla "cegas" (blunt). Outras, como a EcoRI, fazem um *corte desalinhado*: cortam as duas fitas em posições deslocadas, deixando em cada fragmento uma pequena saliência de fita simples. Essas saliências são as #termo-nota[pontas coesivas][extremidades de fita simples complementares geradas por corte desalinhado, que se reparam por pareamento com qualquer ponta cortada pela mesma enzima — também ditas "pegajosas"] — e elas são o segredo de toda a montagem, como veremos em 3.3.

A nomenclatura segue uma regra fixa que vale memorizar pela lógica: a primeira letra (maiúscula) vem do gênero da bactéria, as duas seguintes da espécie, e um algarismo romano indica a ordem de descoberta naquela linhagem. EcoRI vem de _Escherichia coli_, primeira enzima de restrição daquela linhagem; HaeIII de _Haemophilus aegyptius_, e assim por diante. O nome carrega a origem biológica da tesoura.

#mini-resumo[Enzimas de restrição são a defesa bacteriana (restrição) calibrada pela metilação do DNA próprio (modificação). As do Tipo II cortam sítios palindrômicos curtos — em corte reto (pontas cegas) ou desalinhado (pontas coesivas).]

#subtopico("3.2 — Eletroforese em gel: enxergar os fragmentos")

Depois de cortar o DNA com uma enzima de restrição, você tem uma mistura de fragmentos de tamanhos diferentes — e precisa de um jeito de *vê-los* e medi-los. A eletroforese em gel de agarose resolve isso explorando uma propriedade física simples do DNA. Cada nucleotídeo carrega um grupo fosfato com carga negativa, de modo que toda molécula de DNA é uniformemente negativa. Coloque os fragmentos num gel poroso e aplique um campo elétrico: todos migram em direção ao polo positivo.

#figura-lateral("/figuras/biomol-26-dna-recombinante-pcr/slide-38.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O que *separa* os fragmentos é o gel agindo como uma peneira tridimensional. Os fragmentos menores se enfiam pelos poros com facilidade e avançam mais; os maiores ficam emperrados e migram menos. Ao fim da corrida, os fragmentos estão distribuídos por tamanho ao longo do gel — *os menores mais adiante, os maiores mais atrás*. Comparando com um padrão de tamanhos conhecidos, lê-se diretamente o comprimento de cada fragmento.],
  legenda: [Os fragmentos menores movem-se adiante dos maiores.])

#sigla("pb", [pares de base — unidade de comprimento de um fragmento de DNA de fita dupla])

Falta ainda tornar o DNA visível, porque ele é incolor. Para isso usa-se o *brometo de etídio*, uma molécula que se intercala entre as bases empilhadas do DNA e, ao ser iluminada por #sigla("UV", [luz ultravioleta]), emite fluorescência alaranjada. Fotografando o gel sob luz UV num transiluminador, cada fragmento aparece como uma banda brilhante na posição correspondente ao seu tamanho. É assim que se faz a caracterização visual de fragmentos: um mapa de bandas que revela quantos fragmentos existem e qual o tamanho de cada um, medido em pb.

#figura-lateral("/figuras/biomol-26-dna-recombinante-pcr/slide-42.png",
  lado: "left",
  largura-figura: 34%,
  texto: [Num gel real corado com brometo de etídio, cada faixa horizontal é um fragmento de DNA de determinado tamanho. A primeira coluna costuma ser um padrão de peso molecular (o "ladder"), com fragmentos de tamanhos conhecidos, contra o qual se calibram os demais. Digerir o mesmo plasmídeo com enzimas diferentes gera padrões de banda diferentes — uma assinatura do mapa de cortes.],
  legenda: [Bandas de DNA num gel de agarose, com padrão de tamanhos à esquerda.])

#subtopico("3.3 — Ligase e vetores: colar e dar um veículo")

Cortar é metade do trabalho; a outra metade é *colar*. Aqui entra a beleza das pontas coesivas. Como uma enzima de restrição reconhece sempre a *mesma* sequência, dois DNAs de origens completamente diferentes — digamos, de uma bactéria e de um ser humano — cortados pela *mesma* enzima ficam com *o mesmo conjunto de pontas de fita simples*. As saliências de um pareiam espontaneamente com as saliências do outro, por simples complementaridade de bases. É o que permite recombinar genomas que jamais se encontrariam na natureza.

Esse pareamento, porém, é frágil: são só algumas pontes de hidrogênio temporárias. Para tornar a junção permanente, é preciso *selar* a ligação no esqueleto de açúcar-fosfato. Quem faz isso é a *DNA ligase*, que catalisa a formação da ligação fosfodiéster entre os fragmentos. A ligase tem uma exigência química precisa: requer um grupo *hidroxila livre na extremidade 3'* de uma cadeia e um grupo *fosfato na extremidade 5'* da outra — e gasta energia para formar a ligação.

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-46.png",
  largura: 44%,
  legenda: [A DNA ligase consome #sigla("ATP", [adenosina trifosfato — moeda energética da célula]) (liberando AMP + pirofosfato) para selar a quebra entre dois fragmentos pareados, costurando o 3'-OH de uma cadeia ao 5'-fosfato da outra. Depois dela, os dois pedaços são uma molécula contínua.])

Com inserto e cola na mão, falta o veículo. O inserto, sozinho, não se replica dentro da bactéria — ele precisa estar fisicamente ligado a um vetor que carregue os elementos para se multiplicar. O vetor mais simples é o #termo-nota[plasmídeo][pequena molécula de DNA circular de fita dupla, independente do cromossomo bacteriano, capaz de se replicar sozinha], uma pequena molécula de DNA circular de dupla fita, separada do cromossomo, que se replica de forma independente. Um bom plasmídeo de clonagem precisa de duas coisas: uma *origem de replicação* (#sigla("Ori", [origem de replicação — sequência onde a maquinaria de cópia do DNA começa])), sem a qual ele não é copiado, e pelo menos um *gene de resistência a antibiótico*, que serve para selecionar depois quais bactérias receberam o plasmídeo.

#figura-nebli("/figuras/biomol-26-dna-recombinante-pcr/slide-47.jpeg",
  largura: 50%,
  legenda: [O plasmídeo pBR322: a *origem de replicação* (Ori) garante que ele seja copiado; os genes de *resistência a ampicilina e a tetraciclina* permitem selecionar as bactérias transformadas; os sítios únicos de EcoRI, SalI e PstI oferecem pontos exatos para abrir o círculo e inserir o fragmento.])

Plasmídeos comportam insertos pequenos. Para fragmentos maiores existem outros vetores: o *bacteriófago λ*, cujo DNA linear de fita dupla de cerca de 48.500 pb tem nas pontas trechos de fita simples complementares que o fecham em círculo dentro da célula; e vetores de altíssima capacidade como o #sigla("BAC", [cromossomo artificial de bactéria — vetor para insertos muito grandes]) e o #sigla("YAC", [cromossomo artificial de levedura — vetor para os maiores insertos]). O fago tem ainda um traço biológico relevante: ao infectar a bactéria, pode seguir o caminho *lítico* (replicar-se e arrebentar a célula) ou o caminho #termo-nota[lisogênico][estado em que o DNA do fago se integra ao cromossomo bacteriano como profago e é copiado junto, sem matar a célula], em que seu DNA se integra ao cromossomo como profago e é herdado silenciosamente — a escolha entre os dois depende das condições da célula.

#atencao-box("A mesma enzima nas duas pontas", [
  O encaixe inserto–vetor só funciona porque ambos foram cortados pela *mesma* enzima de restrição: é isso que garante pontas coesivas complementares. Cortar o inserto com uma enzima e o vetor com outra produz saliências que *não* pareiam, e a ligação não ocorre. Por isso o sítio de restrição escolhido no vetor (como o EcoRI do pBR322) tem de ser o mesmo usado para liberar o inserto. Pontas cegas (corte reto) ligam-se entre si, mas sem a especificidade e a eficiência das coesivas.
])

#mini-resumo[Pontas coesivas geradas pela mesma enzima pareiam inserto e vetor; a ligase sela a ligação fosfodiéster (precisa de 3'-OH, 5'-fosfato e ATP). O vetor — plasmídeo, fago λ, BAC, YAC — fornece origem de replicação e marcador de seleção.]

#subtopico("3.4 — Transformação: fazer a bactéria engolir o DNA")

Resta o último obstáculo, e ele é físico: a molécula recombinante está no tubo, mas precisa *atravessar a membrana* da bactéria para ser replicada lá dentro. Bactérias normalmente não absorvem DNA grande e carregado do meio. É preciso forçá-las a um estado especial chamado de *competência*.

O método clássico explora a química da membrana. A _E. coli_ torna-se uma #termo-nota[célula competente][bactéria tratada para absorver DNA exógeno do meio, em geral por CaCl₂ gelado seguido de choque térmico] quando é suspensa em cloreto de cálcio (CaCl₂) gelado e então submetida a um breve *choque térmico* a 42 °C. O cálcio neutraliza as cargas negativas que se repeliriam — a membrana e o DNA são ambos negativos — e o choque de temperatura aumenta transitoriamente os poros da membrana, abrindo passagem para o plasmídeo entrar. A eficiência típica é da ordem de 10⁵ a 10⁷ bactérias transformadas por micrograma de plasmídeo.

Há ainda dois métodos físicos para empurrar o rendimento para cima. A *eletroporação* aplica descargas elétricas de baixa intensidade que abrem poros transitórios na membrana, aumentando muito a entrada de DNA. E a *biolística* (ou "DNA shooting") literalmente dispara partículas de ouro recobertas de plasmídeo contra as células — útil sobretudo para plantas e células difíceis de transformar pelos métodos químicos.

Fechado o circuito, o gene de resistência a antibiótico do vetor revela seu propósito. Após a transformação, espalham-se as bactérias num meio com o antibiótico: só sobrevivem e formam colônia as que receberam o plasmídeo (com seu gene de resistência). Cada colônia sobrevivente é um clone puro carregando o inserto — exatamente o que a PARTE I prometia entregar. A tesoura cortou, o gel conferiu, a ligase colou, o vetor carregou e a transformação introduziu; a seleção por antibiótico separa o sucesso do fracasso.

#sintese-box(3)[Transformação é a entrada do DNA recombinante na bactéria: competência por CaCl₂ + choque térmico, ou eletroporação, ou biolística. A seleção por antibiótico, graças ao marcador do vetor, isola as colônias transformadas — cada uma um clone do inserto.]

#conclusao-box[
  *O princípio que costura a aula inteira é a especificidade do reconhecimento molecular.* Em cada etapa, o que dá controle ao experimentador é uma molécula reconhecendo uma sequência exata: a enzima de restrição reconhece seu palíndromo, os iniciadores reconhecem as bordas do alvo, as pontas coesivas reconhecem suas complementares, o marcador de resistência reconhece quem foi transformado. Tirar a especificidade de qualquer um desses passos derruba a técnica toda.

  *O mecanismo nuclear* é o pareamento de bases — a mesma regra A–T/G–C que torna possíveis o anelamento de iniciadores na PCR, o reencaixe de pontas coesivas na clonagem e a leitura de uma fita-molde. Dois motores de cópia dividem o trabalho a partir daí: a PCR multiplica num tubo, a clonagem multiplica numa bactéria; cada um tem seu lugar conforme você queira apenas DNA em quantidade ou também um sistema vivo que expresse a proteína.

  *Na clínica*, esse arsenal sustenta o diagnóstico de doenças infecciosas e genéticas, os testes de paternidade e a forense por análise direta do DNA, e a produção de proteínas terapêuticas — a insulina humana recombinante, o primeiro grande triunfo da quimera bacteriana, é fabricada exatamente assim.

  *Para onde isso vai a seguir.* O título desta aula menciona ainda o *sequenciamento*, que é o passo natural depois de obter muitas cópias de um fragmento: na lógica de Sanger, copia-se o fragmento incorporando, de vez em quando, nucleotídeos "terminadores" (didesoxi) que travam a síntese; isso gera fragmentos de todos os comprimentos possíveis, que, separados por tamanho num gel ou capilar exatamente como na eletroforese da PARTE III, revelam a sequência letra a letra. As mesmas ferramentas — polimerase, eletroforese, pareamento de bases — reaparecem montadas de outro jeito. E o próximo tema, a *identificação de bactérias patogênicas*, é só esse ferramental aplicado a um problema clínico concreto: pegar o DNA do microrganismo, amplificá-lo e lê-lo para dizer quem ele é.
]
