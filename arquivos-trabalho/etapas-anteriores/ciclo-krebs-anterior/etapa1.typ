#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Você tem cerca de 30 trilhões de células no corpo. Todas elas vieram de UMA célula só — o zigoto formado quando o espermatozoide do seu pai encontrou o óvulo da sua mãe. Para sair de uma e chegar em 30 trilhões, foi preciso uma sequência de divisões celulares — e cada uma delas teve que copiar perfeitamente 2 metros de #sigla("DNA", [ácido desoxirribonucleico — molécula que guarda a informação genética]) e dividir esse material em duas células-filhas idênticas. Uma divisão errada num momento ruim vira câncer; uma divisão errada no embrião vira síndrome ou aborto.

A pergunta que organiza este resumo é: *como a célula consegue duplicar e dividir todo o seu conteúdo sem errar, milhões de vezes, ao longo da sua vida?* A resposta tem três peças, e cada PARTE pega uma.

Na PARTE I você vai entender o que é o ciclo celular e como os cientistas descobriram suas fases — porque você não pode resolver um problema sem antes ver o problema. Vai conhecer G1, S, G2 e M, e por que falar de "quantidade de DNA" é diferente de falar de "número de cromossomos". Vai ver os experimentos clássicos (BrdU, citometria de fluxo, Ki67) que aparecem direto em prova.

Na PARTE II entra o motor molecular: *ciclinas* e *quinases dependentes de ciclina* (CDKs). Esse é o coração da disciplina. Você vai entender por que ciclinas têm que oscilar (subir e descer), por que CDKs precisam de uma ciclina para funcionar, e como o sistema usa proteólise por ubiquitina (APC/C, SCF) para tornar cada passo irreversível. Vai ver também como os mitógenos (sinais externos de "pode dividir") usam a proteína Rb para abrir a comporta entre G1 e S.

Na PARTE III a gente vê a mitose pelo motor — não como sequência de fases bonitinhas, mas como uma cascata de fosforilações e degradações que o M-CDK orquestra. Você vai entender por que o envelope nuclear se desmonta na prófase (M-CDK fosforila as laminas), por que a anáfase é irreversível (APC/C ativa separase, que clivam coesinas), e por que a citocinese precisa de actina e miosina II, não de microtúbulos. E vai ver o que acontece quando o sistema falha: p53 mutado, Rb inativado pelo HPV, e o nascimento do câncer.
]

#parte-title("PARTE I — O ciclo celular e como se estuda", primeira: true)

#subtopico("1.1 — Por que a célula precisa dividir, e o que muda quando ela divide")

A pergunta certa para começar não é "como a célula se divide" — é uma anterior: *por que dividir?* Uma célula que não se divide pode crescer, mas só até certo ponto: o volume cresce ao cubo enquanto a superfície cresce ao quadrado, então a partir de um tamanho a difusão deixa de dar conta de nutrir o interior. Crescer indefinidamente não é solução. Para fazer um organismo grande, é preciso uma estratégia diferente: *multiplicar células pequenas*.

Vale separar dois termos que a Profa. Cella destaca logo no início da aula, porque o aluno frequentemente os mistura. *Crescimento celular* é aumento da MASSA de uma célula individual — a célula fica maior, acumula mais proteína, mais membrana, mais organelas. *Divisão celular* (ou proliferação) é aumento do NÚMERO de células — uma vira duas. São processos relacionados, mas não sinônimos. Uma célula precisa crescer antes de se dividir (senão as filhas saem pequenas demais), mas pode crescer sem dividir (neurônios maduros, hepatócitos quiescentes).

E quando, na vida toda, a célula realmente precisa se dividir? Em quatro situações principais. *No embrião*, para sair de zigoto até organismo: ~14 trilhões de divisões em nove meses, num ritmo que diminui à medida que a diferenciação avança. *No crescimento pós-natal*, para o organismo aumentar de tamanho. *Na reposição*, ao longo da vida adulta — sua pele troca todas as células a cada 4 semanas, o epitélio intestinal a cada 4 dias, hemácias a cada 120 dias. *Em ferimentos*, quando tecido lesado precisa ser refeito. E uma quinta, patológica: o *câncer*, divisão fora de controle. Em todos os casos saudáveis, a regra geral é: na homeostase, *divisão* e *morte celular* estão em equilíbrio. Quando a balança quebra, alguma coisa séria está acontecendo.

#figura-nebli("/figuras/divisao-celular/slide-06.png",
  largura: 70%,
  legenda: [Os quatro contextos fisiológicos em que a divisão celular acontece (embrião, crescimento, reposição, ferimentos) somados ao quinto, patológico (câncer). A divisão é regulada precisamente em cada um — não é "ligada" o tempo todo.])

Uma observação clínica útil: a velocidade de divisão num tecido importa para a toxicidade de quimioterápicos. Drogas que atacam células em divisão (como a doxorrubicina) machucam justo os tecidos que mais se dividem — medula óssea (queda de hemácias, neutrófilos, plaquetas), epitélio intestinal (diarreia, mucosite) e folículos pilosos (queda de cabelo). O efeito colateral *é* o mecanismo terapêutico desviado para um alvo errado.

#mini-resumo[Em uma frase: *a célula divide para construir, repor e curar — e mantém a divisão num equilíbrio fino com a morte celular*. Crescimento é uma célula ficando maior; divisão é uma virando duas — não confundir.]

#subtopico("1.2 — As quatro fases: G1, S, G2, M — e por que falar de DNA não é o mesmo que falar de cromossomos")

Imagine uma fábrica que precisa entregar 2 caminhões idênticos a partir de 1 caminhão. O processo tem que ter etapas claras: comprar peças, montar o segundo caminhão, conferir, e só então separar fisicamente. A célula resolve um problema análogo, e por isso o ciclo celular tem quatro fases bem definidas: *G1*, *S*, *G2* e *M*.

*G1* (do inglês "gap 1") é a fase em que a célula cresce, sintetiza proteína, e *decide* se vai entrar em divisão. É o momento dos "vou ou não vou": se há nutrientes, se há mitógenos no meio (sinais de "pode dividir"), se o DNA está íntegro. Uma célula que decide *não* se dividir sai de G1 para um estado chamado #sigla("G0", [estado de quiescência reversível — célula viva mas fora do ciclo]) — neurônios maduros vivem em G0 a vida inteira, hepatócitos passam anos em G0 e voltam ao ciclo só quando o fígado é lesado.

*S* (de "synthesis") é a fase em que o DNA é duplicado. Cada uma das 46 moléculas de DNA do humano é replicada uma única vez, gerando duas cópias idênticas que ficam unidas pelo centrômero. Essas duas cópias unidas são as *cromátides-irmãs*. Aqui mora uma confusão que dura o curso inteiro, então vamos parar pra fixar.

#confusao-prevista(
  titulo: "Cromátide-irmã, cromossomo, cromossomo homólogo: 3 coisas diferentes",
  aluno_acha: [aluno acha que duplicar o DNA dobra o número de cromossomos.],
  mecanismo: [Não. Em G1, você tem 46 cromossomos, cada um com 1 molécula de DNA → 46 moléculas no total. Após S, você tem ainda 46 cromossomos (cada um agora com 2 cromátides-irmãs unidas pelo centrômero) → 92 moléculas de DNA no total. O número de *cromossomos* é o mesmo; o que dobrou foi a *quantidade de DNA* (de 2C para 4C). Cromátides-irmãs são cópias idênticas, geradas em S. Cromossomos homólogos são o par materno+paterno (ex.: o cromossomo 7 da mãe + o 7 do pai) — esse conceito não muda em S.],
)

*G2* (gap 2) é uma fase de verificação: a célula confere se a duplicação foi completa e correta antes de se comprometer com a divisão física. É a última chance de parar — se houver dano no DNA, o ponto de checagem G2/M (que veremos adiante) impede a entrada em M.

*M* (mitose) é a fase da divisão propriamente dita: o envelope nuclear desmonta, os cromossomos condensam, o fuso mitótico se forma, as cromátides-irmãs alinham-se na placa equatorial, separam-se para polos opostos, e o citoplasma é dividido (citocinese). Tudo isso em cerca de 1 hora — comparado a 12-24 horas para o ciclo todo, M é só ~5% do tempo.

Juntando G1, S e G2, a célula está em *intérfase* — a parte "invisível" do ciclo, em que nada parece acontecer ao microscópio óptico (núcleo intacto, cromatina dispersa), mas é onde acontece a maior parte do trabalho preparatório. Essa é justamente a etapa que a aula da Profa. Cella escolhe como foco: a intérfase é onde os reguladores moleculares atuam, e onde o aluno pisa em ovos.

#figura-nebli("/figuras/divisao-celular/slide-10.png",
  largura: 65%,
  legenda: [O ciclo celular como um círculo: G1 → S → G2 → M → G1 de novo. M é a fatia pequena visível ao microscópio; G1+S+G2 (intérfase) é o tempo "invisível" mas regulatoriamente decisivo. Notar que G0 é uma saída lateral a partir de G1, não uma fase do ciclo ativo.])

#mini-resumo[As 4 fases: *G1* (crescer, decidir), *S* (duplicar DNA → cromátides-irmãs), *G2* (conferir), *M* (dividir). Após S, o número de *cromossomos* não muda (segue 46), mas a *quantidade de DNA* dobra (de 2C para 4C) — distinção que aparece em prova.]

#subtopico("1.3 — Como saber em que fase está? BrdU, citometria, Ki67")

Você pode olhar uma célula no microscópio e dizer se ela está em mitose (cromossomos condensados aparecem) — mas como diferenciar G1 de S, ou G2 de G1? Essas são fases invisíveis. A solução foi inventar marcadores que se acoplam ao processo em andamento. Três deles são clássicos e caem direto em prova.

O primeiro é o *#sigla("BrdU", [bromo-deoxiuridina — análogo da timidina que é incorporado ao DNA durante a replicação])*. BrdU é uma molécula que se parece com a timidina (a "T" do DNA), tão parecida que a maquinaria de replicação a incorpora ao novo DNA sendo sintetizado durante a fase S. Como BrdU tem um bromo no lugar do metila da timidina, a gente consegue detectá-la depois com um anticorpo específico (anti-BrdU). O protocolo: injeta BrdU no animal, espera 2-3 horas, coleta o tecido, e usa imunofluorescência (anti-BrdU + anti-anti-BrdU conjugado a fluoróforo) para ver quais células incorporaram BrdU — *essas* foram as que estavam em S durante a janela de exposição. É um marcador de "quem estava replicando".

O segundo é a *citometria de fluxo com #sigla("IP", [iodeto de propídio — corante intercalante que se liga ao DNA estequiometricamente, permitindo quantificar a quantidade de DNA por célula])*. A lógica é elegante: você marca o DNA das células com um corante que se intercala estequiometricamente (quanto mais DNA, mais corante; o sinal é proporcional). Passa as células uma por uma por um laser e mede a fluorescência de cada uma. O resultado é um histograma com a distribuição da quantidade de DNA por célula: um pico em "2C" (células em G1), um pico em "4C" (células em G2 e M), e um vale-com-cauda entre os dois (células em S, em diferentes estágios da replicação). Olhando o histograma, dá pra dizer quantas células de uma população estão em cada fase. É o método quantitativo padrão da disciplina.

#figura-nebli("/figuras/divisao-celular/slide-18.png",
  largura: 75%,
  legenda: [Análise do ciclo celular por citometria de fluxo. O eixo X é a quantidade de DNA por célula; o eixo Y é o número de células. Pico G1 (2C) à esquerda, pico G2+M (4C) à direita, vale-S (replicação em curso) no meio. O perfil muda quando se trata as células com drogas que param o ciclo em um ponto específico.])

O terceiro marcador é o *Ki67* — uma proteína nuclear que aparece em todas as células em ciclo ativo (G1, S, G2, M) e está *ausente* em células quiescentes (G0). Em patologia tumoral, o índice de Ki67 é usado para estimar o índice proliferativo do tumor: tumores com Ki67 alto (>20%) são mais proliferativos e geralmente mais agressivos. Ki67 não diz em qual fase a célula está — só diz se ela está dentro do ciclo (ativa) ou fora (G0).

#clinica-box("Ki67 e o que ele realmente significa", [
Aluno frequentemente erra a ideia de Ki67. Pense assim: Ki67 não é um "marcador de proliferação rápida" — é um marcador de *presença no ciclo*. Uma célula em G1 lento (24 h) tem Ki67 positivo do mesmo jeito que uma célula em divisão acelerada. O que muda entre tumores agressivos e indolentes é a *fração* de células no ciclo: tumor agressivo tem mais células Ki67-positivas porque mais células estão ativas. Isso aparece em prova como pergunta sobre por que aumento de Ki67 implica aumento da fração proliferativa, não aumento da velocidade individual de divisão.
])

Um quarto bloco de evidência veio da genética: a Profa. Cella menciona os genes *#sigla("Cdc", [cell division cycle — família de genes identificados em leveduras com mutações que param o ciclo num ponto específico, mapeando a maquinaria do ciclo])*. Em leveduras, mutar um gene Cdc para sensível à temperatura permite "ligar e desligar" o ciclo: a 23°C a célula divide normal, a 36°C ela trava em um ponto específico. Diferentes genes Cdc travam em pontos diferentes, e foi assim que se mapeou a maquinaria — descoberta que rendeu o Nobel de 2001 (Hartwell, Hunt, Nurse).

#mini-resumo[Três ferramentas para "ver" fases invisíveis: *BrdU* marca quem replicou DNA (S); *citometria com IP* dá o histograma 2C/4C (G1 vs G2+M); *Ki67* marca quem está no ciclo (não em G0). Em prova, lembrar: BrdU = S; histograma 2C = G1; Ki67 = ciclo ativo (não fase específica).]

#subtopico("1.4 — Lógica tudo-ou-nada e os pontos de checagem")

Agora a peça que organiza todo o restante da apostila: o ciclo celular não funciona com transições suaves. Funciona em *saltos abruptos*, ativações tipo "tudo-ou-nada", e cada salto é *irreversível* uma vez disparado. Por quê?

Pense no risco. Se a fase S começasse "um pouquinho" — replicando parte do DNA mas não tudo — a célula entraria em M com cromossomos parcialmente duplicados e a segregação seria caótica. Se a anáfase começasse "meio que" — separando algumas cromátides mas não outras — uma célula-filha ganharia 47 cromossomos e a outra 45 (aneuploidia). A única forma de evitar esse tipo de catástrofe é exigir que cada transição seja: (a) *toda ou nenhuma* — não meio caminho; (b) *irreversível* — uma vez começada, vai até o fim; (c) *só após verificação* — só dispara se as condições prévias estiverem corretas.

Essas três exigências resultam num desenho de sistema com duas camadas. A camada *de motor* — ciclinas e CDKs — gera transições abruptas por feedback positivo (veremos na PARTE II). A camada *de controle* — os pontos de checagem (#termo-nota[checkpoint][ponto de verificação que bloqueia o avanço do ciclo se condições prévias não foram cumpridas — ex.: dano no DNA, replicação incompleta, alinhamento incorreto dos cromossomos]) — verifica condições antes de liberar a próxima transição.

Há três checkpoints principais na maioria das células somáticas. O *checkpoint G1/S* (também chamado #termo-nota[ponto de restrição][momento em G1 a partir do qual a célula está comprometida com a divisão, mesmo se os sinais mitogênicos desaparecerem; antes do ponto, a célula pode voltar para G0]) verifica se há mitógenos suficientes no meio externo (a célula é "convidada" a dividir?), se há nutrientes, e se o DNA está íntegro. É o checkpoint da decisão de entrar em ciclo. Passou disso, a célula vai até a divisão; antes disso, ainda pode voltar para G0.

O *checkpoint G2/M* verifica se a replicação foi completada e se o DNA replicado não tem danos. Se houver quebras de fita dupla, esse checkpoint ativa #sigla("ATM", [ataxia telangiectasia mutated — quinase que detecta quebras de DNA de dupla fita e ativa cascata p53]) e #sigla("ATR", [ataxia telangiectasia and Rad3-related — quinase relacionada a ATM, ativada por fitas simples expostas durante replicação travada]), que ativam #sigla("p53", [proteína supressora tumoral codificada pelo gene TP53; o "guardião do genoma"]) e param a entrada em mitose até que o reparo aconteça (ou que a célula seja induzida à apoptose, se o dano for irreparável).

O *checkpoint do fuso* (também chamado #sigla("SAC", [spindle assembly checkpoint — sistema de vigilância que mantém APC/C inibido até que todos os cinetócoros atinjam tensão bipolar])) atua dentro da mitose, na metáfase: verifica se todos os cromossomos estão devidamente ligados ao fuso e sob tensão bipolar. Se há um único cinetócoro desprendido, o checkpoint inibe o #sigla("APC/C", [anaphase-promoting complex/cyclosome — ligase de ubiquitina que dispara a anáfase quando todos os cromossomos estão alinhados]) e a anáfase não acontece. Esse é o checkpoint que falha em muitos cânceres, gerando aneuploidias.

#figura-nebli("/figuras/divisao-celular/slide-22.png",
  largura: 70%,
  legenda: [Os pontos de checagem como vias de sinalização que entram no ciclo em pontos críticos. Cada um integra um conjunto específico de informações (mitógenos, dano, replicação, alinhamento) e decide se permite avançar.])

#mini-resumo[A engenharia do ciclo: *transições abruptas, irreversíveis, só após verificação*. Três checkpoints clássicos: *G1/S* (entrar ou não), *G2/M* (replicação fiel?), *fuso* (alinhamento bipolar?). Cada um é uma via de sinalização, não um botão — entender o motor (PARTE II) é entender por que cada checkpoint para o ciclo no ponto que para.]

#parte-title("PARTE II — O motor: ciclinas, CDKs e seus controladores")

#subtopico("2.1 — Por que precisava existir uma 'ciclina' — a descoberta")

Antes de despejar nomes (CDK4, ciclina D, p21, MDM2…), vale entender por que o sistema *tem que ter* essa cara molecular. O problema era o seguinte: o ciclo celular precisa ser um cronômetro — uma coisa que dispara passos em sequência, no momento certo, e que não dispara passos fora de hora. Quando os bioquímicos foram procurar o cronômetro nos anos 80, esperavam achar UMA proteína cuja atividade subisse e descesse ciclicamente.

E acharam — em ouriço-do-mar. Tim Hunt, premiado com o Nobel em 2001, identificou uma proteína cuja *concentração* oscilava drasticamente ao longo do ciclo: acumulava durante a intérfase, despencava abruptamente na transição metáfase-anáfase, e voltava a acumular. Ele chamou de *ciclina*. E aqui veio a primeira surpresa: a ciclina sozinha não fazia nada — era preciso uma segunda proteína, uma quinase (enzima que adiciona fosfato em outras proteínas), para de fato disparar o ciclo. A quinase sozinha também não fazia nada — só funcionava quando ligada à ciclina. Daí o nome: *quinase dependente de ciclina*, ou #sigla("CDK", [cyclin-dependent kinase — quinase que só é cataliticamente ativa quando ligada a uma ciclina parceira]).

Por que esse arranjo de duas partes? Por economia evolutiva e por segurança. Se a quinase ativa fosse uma única proteína que tivesse que ser sintetizada e degradada a cada ciclo, isso gastaria muita energia. Manter a quinase sempre presente mas só ativa quando ligada a uma ciclina (que oscila) é mais eficiente: a célula só precisa controlar a oscilação da ciclina. E mais: se houver um problema, dá pra parar o sistema *destruindo a ciclina* (proteólise rápida) — a quinase fica inativa imediatamente, sem precisar destruí-la também. É um interruptor com botão de pânico embutido.

#figura-nebli("/figuras/divisao-celular/slide-29.png",
  largura: 75%,
  legenda: [O sistema é modular: várias CDKs (CDK1, CDK2, CDK4, CDK6) parceadas com várias ciclinas (D, E, A, B), gerando complexos diferentes para fases diferentes do ciclo. A ciclina é a "etiqueta de tempo"; a CDK é o motor que executa.])

#mini-resumo[O cronômetro do ciclo é um sistema de duas partes: *ciclina* oscila (acumula e degrada), *CDK* não oscila (mas só é ativa com ciclina). Oscilar uma e manter a outra é evolutivamente mais econômico — e dá um botão de pânico (destrói a ciclina, para a CDK).]

#subtopico("2.2 — Anatomia do par ciclina-CDK e por que o controle precisa ser multicamadas")

OK, agora a anatomia. Uma CDK isolada está num estado "quase ativo, mas não": ela tem o sítio catalítico parcialmente ocluído por uma alça flexível ("T-loop"). A ciclina, ao se ligar, *reposiciona* essa alça e expõe o sítio catalítico — agora a CDK pode pegar #sigla("ATP", [adenosina trifosfato — fornece o grupo fosfato que a CDK transfere para o substrato]) e transferir um fosfato para suas proteínas-alvo. Isso é a *ativação por ligação*: a ciclina liga, a CDK liga.

Mas só essa ligação não basta. A célula adiciona mais duas camadas de controle para evitar disparos acidentais.

A primeira camada é *fosforilação ativadora*: depois da ligação, uma enzima chamada #sigla("CAK", [CDK-activating kinase — quinase que adiciona o fosfato ativador na alça T da CDK, completando a ativação enzimática]) adiciona um fosfato ativador na CDK. Sem esse fosfato, a CDK ainda não dispara. Com ele, está cataliticamente competente.

A segunda camada são *fosforilações inibitórias*: enzimas chamadas Wee1 adicionam fosfatos *inibitórios* em outros pontos da CDK, "trancando" o sistema mesmo com ciclina ligada e fosfato ativador presente. Para destrancar, uma fosfatase chamada Cdc25 remove esses fosfatos inibitórios. O resultado é que a ativação efetiva de uma CDK depende de quatro coisas ao mesmo tempo: (1) ciclina ligada, (2) fosfato ativador presente, (3) fosfatos inibitórios removidos, (4) nenhum inibidor proteico (CKI) acoplado ao complexo.

#figura-nebli("/figuras/divisao-celular/slide-26.png",
  largura: 65%,
  legenda: [A regulação multicamadas das CDKs: ligação à ciclina + fosforilação ativadora (CAK) + remoção de fosfatos inibitórios (Cdc25). Cada camada é um ponto de entrada para sinais de checagem.])

Por que tanto controle? Porque cada camada é uma porta de entrada para um sinal de checagem. Dano no DNA? Atua via fosfatos inibitórios (mantém Wee1 ativa, Cdc25 inativa). Falta de mitógenos? Atua via síntese da ciclina (não sintetiza, não há complexo). Replicação incompleta? Atua via #sigla("CKI", [CDK inhibitor — proteína que se liga ao complexo ciclina-CDK e bloqueia atividade catalítica; ex.: p21, p27, p16]) (segura o complexo num estado inativo). O sistema é multilateral porque os sinais são multilaterais.

#mini-resumo[Para uma CDK ficar ativa, *quatro condições simultâneas*: ciclina ligada, fosfato ativador (CAK), fosfatos inibitórios removidos (Cdc25), sem CKI acoplado. Cada condição é uma porta de checagem — é por isso que o sistema responde a tantos sinais diferentes.]

#subtopico("2.3 — Quatro complexos para quatro fases — o 'TIMER'")

Agora a parte que cai em prova como pergunta direta: *qual complexo ciclina-CDK atua em qual fase?* A Profa. Cella sintetiza no slide do "TIMER":

Em *G1*, o complexo dominante é a *ciclina D + CDK4/6*. Sua função: fosforilar a proteína Rb (vamos detalhar adiante) e liberar a célula da inibição que mantinha G0.

Na transição *G1/S* (passar do ponto de restrição), o complexo é *ciclina E + CDK2*. Sua função: ativar a maquinaria de replicação, iniciar a duplicação dos centrossomos, e preparar a entrada em S.

Em *S*, é *ciclina A + CDK2*. Sua função: sustentar a replicação e impedir nova carga das origens de replicação (o "DNA licenciado" — mais sobre isso em 2.4).

Em *G2/M e M*, é *ciclina B + CDK1* (historicamente chamado #sigla("MPF", [maturation-promoting factor — o complexo ciclina B + CDK1 que dispara a entrada em mitose; nome histórico, identificado em oócitos antes da caracterização molecular])). Esse é o motor da mitose: fosforila as laminas (desmonta envelope nuclear), os condensinos (condensa cromossomos), e os componentes do fuso (montagem).

Note o desenho: cada complexo tem uma *janela temporal* específica, gerada pela síntese e degradação de sua ciclina. As CDKs (1, 2, 4, 6) ficam mais ou menos constantes. As ciclinas (D, E, A, B) é que sobem e descem, e quem determina a fase do ciclo é qual ciclina está acumulada no momento.

#figura-nebli("/figuras/divisao-celular/slide-32.png",
  largura: 80%,
  legenda: [Visão geral do ciclo com a oscilação das ciclinas. Ciclina D sobe em G1, ciclina E na transição G1/S, ciclina A em S/G2, ciclina B em G2/M. Cada uma "passa o bastão" para a próxima, e a degradação rápida na transição metáfase-anáfase reseta o sistema.])

Uma observação útil: a ciclina D é uma exceção parcial. Ela não oscila de forma abrupta como as outras — sua concentração depende continuamente da presença de mitógenos. Tira o mitógeno, ciclina D cai; coloca de novo, ciclina D sobe. É essa propriedade que torna a entrada em ciclo dependente do meio externo: sem sinal de "pode dividir", não há ciclina D, não há CDK4/6 ativo, e a célula fica em G0.

#mini-resumo[Mapa CDK-ciclina por fase, decorar: *G1 = CDK4/6 + ciclina D*; *G1/S = CDK2 + ciclina E*; *S = CDK2 + ciclina A*; *M = CDK1 + ciclina B (MPF)*. Ciclina D é a "antena de mitógeno" — sem mitógeno, não há ciclina D, não há entrada em ciclo.]

#subtopico("2.4 — CKIs, APC/C e a destruição programada — por que o ciclo é irreversível")

A ciclina sobe quando a célula precisa dela. Mas para a fase terminar e a próxima começar, a ciclina precisa *desaparecer*. E não dá pra esperar a meia-vida natural da proteína (horas) — o ciclo iria devagar demais. A solução evolutiva foi instalar duas máquinas de destruição programada que jogam ciclinas (e outras proteínas reguladoras) no lixo celular sob comando.

A primeira máquina é o *complexo APC/C* (anaphase-promoting complex/cyclosome). Quando ativado, APC/C cola uma cadeia de #sigla("Ub", [ubiquitina — pequena proteína de 76 aminoácidos que, ao ser ligada em cadeia a uma proteína-alvo, sinaliza para o proteassoma destruí-la]) nas proteínas-alvo, marcando-as para destruição pelo proteassoma. O alvo central do APC/C é a ciclina B — e por isso, quando APC/C é ativado na transição metáfase-anáfase, a ciclina B despenca e o motor da mitose desliga rapidamente. APC/C também destrói outra proteína crítica chamada *securina*, e isso libera a separase (vamos ver na PARTE III). Em resumo: APC/C é o gatilho que termina a mitose.

A segunda máquina é o *#sigla("SCF", [Skp1-Cullin-F-box — ligase de ubiquitina E3 que destrói principalmente CKIs como p27 nas transições G1/S, liberando o complexo CDK-ciclina para disparar a fase seguinte])*. Funciona o ano todo, mas seu alvo principal nas transições do ciclo são as CKIs (inibidores de CDK). Quando uma célula precisa avançar de G1 para S, ela ativa SCF para destruir a CKI p27, que estava segurando o complexo CDK2-ciclina E inativo. Sem p27, CDK2-ciclina E dispara e a replicação começa.

#figura-nebli("/figuras/divisao-celular/slide-31.png",
  largura: 70%,
  legenda: [O sistema ubiquitina-proteassoma como degradador programado. APC/C e SCF são as duas ligases de ubiquitina mais importantes do ciclo. Marcação por cadeia de ubiquitina → proteína vai para o proteassoma 26S → degradação em peptídeos.])

Por que a destruição programada importa tanto? Porque ela é o que torna cada passo do ciclo *irreversível*. Pense no contrário: se as transições fossem reversíveis (a célula entrasse em mitose e voltasse), o sistema teria que tomar a decisão de "continuar em M" o tempo todo. Em vez disso, a célula "queima a ponte" — destrói as ciclinas que mantinham o motor anterior — e fica forçada a seguir em frente. Uma vez que ciclina B foi degradada e securina destruída, não dá pra "des-clivar" a coesina entre cromátides-irmãs. O caminho é só pra frente.

#confusao-prevista(
  titulo: "Inibição reversível e irreversível: dois mecanismos diferentes",
  aluno_acha: [aluno trata "inibir CDK" como sinônimo, sem perceber que pode acontecer de duas formas diferentes.],
  mecanismo: [Há duas formas de desligar uma CDK. *Reversível*: ligar uma CKI (p21, p27, p16) ao complexo — segura o complexo num estado inativo, mas se a CKI for removida ou degradada, a CDK volta a funcionar. Isso é usado em checkpoints (parar o ciclo, mas poder retomar). *Irreversível*: ubiquitinar e destruir a ciclina — agora a CDK não tem parceira, e a única forma de voltar é sintetizar nova ciclina. Isso é usado em transições de fase (queimar a ponte). Em prova, identificar o mecanismo pela palavra-chave: "p21 inibe" = reversível; "APC/C degrada" = irreversível.],
)

Uma propriedade adicional que vale destacar: o *#sigla("Pre-RC", [pre-replicative complex — complexo pré-replicativo que se monta nas origens de replicação durante G1, licenciando-as para disparo único na fase S])* ("complexo pré-replicativo"). Para que cada origem de replicação seja disparada *uma única vez por ciclo*, a célula só permite a carga do Pre-RC nas origens quando as CDKs estão *baixas* — ou seja, em G1. Quando as CDKs sobem (em S, G2, M), o Pre-RC não consegue mais se ligar. Assim, mesmo que uma origem já tenha disparado, ela não pode ser recarregada até a próxima G1 — quando as ciclinas estão zeradas e as CDKs estão de novo baixas. Isso garante o "uma replicação por ciclo".

#mini-resumo[Duas ligases de ubiquitina governam a destruição programada: *APC/C* destrói ciclina B e securina (termina mitose); *SCF* destrói CKIs (libera transições G1/S). Destruir, não inibir, é o que torna o ciclo irreversível. Pre-RC só carrega em G1 (CDKs baixas) — garante 1 replicação por ciclo.]

#subtopico("2.5 — Mitógenos, Rb/E2F e a comporta de G1/S")

Falta uma peça importante: como o meio externo (sinais de "pode dividir", "tem nutriente", "tem espaço") chega até o motor interno? A resposta é uma via que vai dos *mitógenos* (fatores de crescimento extracelulares) até o complexo *Rb–E2F*, que controla a passagem por G1/S.

#termo-nota[mitógeno][molécula extracelular que estimula a divisão celular ao se ligar a um receptor de superfície e disparar a cascata Ras-MAPK, que culmina na transcrição da ciclina D — fator de crescimento epidérmico (EGF), PDGF, e em alguns tecidos a insulina] é qualquer molécula extracelular que estimule a divisão celular. Exemplos: EGF (fator de crescimento epidérmico), PDGF, hormônios como insulina em alguns tecidos. Eles se ligam a receptores na superfície da célula e disparam uma cascata intracelular (via Ras, #sigla("MAPK", [mitogen-activated protein kinase — família de quinases que transduz sinais mitogênicos do receptor até o núcleo, culminando na transcrição da ciclina D])) que culmina na transcrição de *ciclina D*. Lembrando da seção 2.3: ciclina D só sobe quando há mitógeno. Daí o link.

Quando a ciclina D sobe, o complexo *CDK4/6 + ciclina D* fosforila uma proteína chamada *#sigla("Rb", [retinoblastoma — proteína supressora tumoral que, na forma hipofosforilada, sequestra E2F e bloqueia a transcrição dos genes da fase S])*. Rb, em sua forma não-fosforilada (ativa como supressor), está ligada a um fator de transcrição chamado *E2F*. Enquanto Rb segura E2F, E2F não consegue transcrever seus genes-alvo — que incluem ciclina E, ciclina A, e enzimas da replicação. Logo, sem Rb fosforilada, não há síntese de ciclina E, não há ativação de CDK2, não há entrada em S.

Quando CDK4/6 + ciclina D fosforila Rb, E2F é liberado e transcreve a ciclina E. CDK2 + ciclina E agora ativa fosforila *ainda mais* Rb (feedback positivo), liberando ainda mais E2F, gerando ainda mais ciclina E. Esse loop de feedback positivo é o que torna a entrada em S abrupta — *tudo ou nada*. Uma vez disparado, a célula passa o ponto de restrição e está comprometida com a replicação. Isso é uma transição binária implementada em hardware molecular.

#figura-nebli("/figuras/divisao-celular/slide-36.png",
  largura: 75%,
  legenda: [A via mitógeno → ciclina D → CDK4/6 → fosforilação de Rb → liberação de E2F → transcrição de ciclina E → CDK2-ciclina E → fosforila Rb mais → libera mais E2F. O loop de feedback positivo torna a transição G1/S abrupta e irreversível.])

E aqui mora um pedaço crucial da clínica da divisão celular. Se você inativa Rb (mutação, ou degradação por #sigla("HPV", [human papillomavirus — vírus oncogênico cuja proteína E7 degrada Rb, liberando E2F constitutivamente e dirigindo proliferação descontrolada do epitélio cervical/orofaríngeo]) E7), a célula entra em S mesmo sem mitógenos. Câncer. Se você inativa p16 (uma CKI que normalmente inibe CDK4/6 em resposta a estresse), CDK4/6 fica sempre ativa, fosforila Rb constitutivamente, E2F fica sempre liberada. Câncer. A via Rb/E2F é mutada ou inativada em praticamente *todos* os tumores humanos — é o eixo central da regulação do ciclo e o ponto de falha mais comum.

#clinica-box("HPV, Rb e o câncer cervical", [
O HPV oncogênico (tipos 16 e 18 principalmente) expressa duas proteínas virais que sequestram a maquinaria do ciclo. *E7* degrada Rb — libera E2F, dirige proliferação. *E6* degrada p53 — bloqueia apoptose mesmo na presença de dano genético. As duas juntas geram uma célula que prolifera sem parar e não morre quando deveria. É a base do câncer cervical e de boa parte dos cânceres de orofaringe. A vacina contra HPV (Gardasil, Cervarix) previne a infecção e, por consequência, esses cânceres.
])

#mini-resumo[A comporta G1/S é a *via mitógeno → ciclina D → CDK4/6 → fosforila Rb → libera E2F → transcreve ciclina E → loop de feedback positivo*. Sem mitógeno, Rb fica não-fosforilada, E2F sequestrada, célula em G0. Com mitógeno, a comporta abre abrupta e irreversível. HPV E7 degrada Rb; HPV E6 degrada p53 — duplo nocaute, câncer cervical.]

#parte-title("PARTE III — A mitose vista pelo motor: do envelope ao câncer")

#subtopico("3.1 — Entrada em M: como o M-CDK reorganiza a célula inteira")

Vamos refazer a mitose agora pela ótica do motor — não como "fases que aparecem no microscópio", mas como *cascata de fosforilações disparadas pelo M-CDK*. Essa é a forma que cai em prova de nível mais alto.

Em G2, a célula acumula ciclina B. Ciclina B + CDK1 começa a se montar, mas é mantido inativo por fosforilações inibitórias (Wee1). No momento certo, uma fosfatase chamada Cdc25 é ativada e remove os fosfatos inibitórios. Cdc25 também é fosforilada (ativada) pelo próprio CDK1 — outro feedback positivo. O resultado é que o M-CDK (ciclina B + CDK1) liga abruptamente, em alguns minutos, com toda a força.

Agora o M-CDK ativo começa a fosforilar uma lista de proteínas-alvo, cada uma resultando num evento visível da mitose. *Fosforila proteínas do envelope nuclear* (laminas A, B, C e proteínas do poro nuclear) — o envelope desmonta. *Fosforila condensinas* — os cromossomos condensam (passam de cromatina dispersa a estruturas em "X" visíveis). *Fosforila proteínas associadas aos microtúbulos* — o citoesqueleto se reorganiza, os microtúbulos dos centrossomos crescem rapidamente formando o fuso mitótico. *Fosforila inibidores do Pre-RC* — impede que o DNA seja replicado de novo. *Inativa inibidores das ciclinas próprias (CKIs)* — sustenta a atividade do motor.

#figura-nebli("/figuras/divisao-celular/slide-55.png",
  largura: 75%,
  legenda: [O M-CDK ativo como um maestro que dispara uma cascata simultânea de eventos: desmontagem do envelope nuclear, condensação cromossômica, formação do fuso, inibição da re-replicação. Cada efeito é fosforilação direta de uma proteína-alvo específica.])

Veja a diferença pedagógica. A mitose tradicional do livro-texto descreve fases (prófase, prometáfase, metáfase…) como uma sequência *visual*. Aqui você vê que cada fase é o *efeito visível* de um evento molecular: a prófase é "M-CDK fosforilou laminas + condensinas"; a prometáfase é "envelope desmontou e microtúbulos invadiram o nucleoplasma"; a metáfase é "cinetócoros conectados, tensão bipolar atingida". Quando o aluno aprende a mitose pelo motor, fases param de ser memorização e viram consequência lógica.

#mini-resumo[Entrada em M: ciclina B se acumula em G2 → CDK1 monta com ciclina B mas é mantido inativo por Wee1 → Cdc25 remove fosfatos inibitórios em feedback positivo → M-CDK liga abruptamente → fosforila laminas (envelope cai), condensinas (cromossomos condensam), MAPs (fuso forma), Pre-RC (não re-replica). Cada fase visível é efeito de uma fosforilação molecular.]

#subtopico("3.2 — Metáfase, cinetócoro e o checkpoint do fuso")

Com o fuso formado e o envelope dissolvido, cada cromossomo precisa fazer uma conexão específica: cada uma das suas duas cromátides-irmãs precisa ligar-se a microtúbulos que vêm de polos opostos do fuso. A estrutura que faz essa conexão é o *#termo-nota[cinetócoro][complexo proteico que se monta sobre o centrômero de cada cromátide-irmã e funciona como ponto de ancoragem para os microtúbulos do fuso — é onde a tensão bipolar é gerada e medida]*. Cada cromátide-irmã tem seu próprio cinetócoro; os dois cinetócoros do mesmo cromossomo apontam em direções opostas (back-to-back).

A conexão correta gera *tensão bipolar*: o microtúbulo de um polo puxa uma cromátide para um lado, o microtúbulo do outro polo puxa a outra cromátide para o outro lado, e o conjunto fica esticado no meio do fuso (placa equatorial). Quando todos os 46 cromossomos atingem essa tensão bipolar, a célula está em metáfase.

Mas e se a conexão estiver errada — só uma cromátide ligada, ou as duas ligadas ao mesmo polo? Aí entra o *checkpoint do fuso* (SAC). Enquanto houver *um único* cinetócoro sem tensão correta, o checkpoint produz um sinal inibitório (um complexo chamado MCC, mitotic checkpoint complex) que se liga ao APC/C e o mantém inativo. APC/C inativo = securina não destruída = separase não liberada = coesina não cortada = cromátides-irmãs ainda unidas. A célula fica parada em metáfase, aguardando.

O checkpoint só "desliga" quando o último cinetócoro discordante alcança tensão correta. Aí o sinal inibitório desaparece, APC/C é liberado, e a anáfase pode disparar. É um sistema de "aprovação por unanimidade": basta um cromossomo mal-conectado para a célula esperar.

#figura-nebli("/figuras/divisao-celular/slide-58.png",
  largura: 70%,
  legenda: [Alinhamento das cromátides-irmãs na metáfase: cada cromossomo com seus dois cinetócoros conectados a microtúbulos vindos de polos opostos, sob tensão bipolar. Coesinas (anéis em torno do par) ainda mantêm cromátides-irmãs unidas.])

#atencao-box("Falha do SAC = aneuploidia = câncer", [
O checkpoint do fuso é o ponto de falha mais importante para *aneuploidia* — número anormal de cromossomos. Quando o SAC está defeituoso (mutações em proteínas como Mad2, BubR1), a célula pode entrar em anáfase com cromossomos mal-conectados, gerando células-filhas com 47 e 45 cromossomos. Em embriões, isso causa síndromes (Down = trissomia 21, Edwards = trissomia 18, Patau = trissomia 13) ou aborto espontâneo. Em adultos, isso é uma marca registrada da maioria dos tumores sólidos — instabilidade cromossômica é um dos *hallmarks of cancer* mais consistentes.
])

#mini-resumo[Cinetócoro = ponto de conexão cromossomo-fuso, um por cromátide. Tensão bipolar = cromátides puxadas para polos opostos, conjunto centrado na placa metafásica. Checkpoint do fuso = "aprovação por unanimidade" — qualquer cinetócoro sem tensão bloqueia APC/C, célula espera. SAC defeituoso → aneuploidia → câncer.]

#subtopico("3.3 — Anáfase: APC/C, separase e coesinas — por que é irreversível")

Chegou o momento mais dramático e mais elegante do ciclo. Todos os cromossomos alinhados, todos os cinetócoros com tensão bipolar, SAC silenciado. APC/C livre, finalmente.

O APC/C ativo faz duas coisas simultâneas, com consequências profundas. *Primeiro*, ubiquitina a *securina* — uma proteína que estava segurando inativa uma enzima chamada *#termo-nota[separase][protease que cliva a subunidade Scc1 da coesina, liberando as cromátides-irmãs umas das outras na anáfase]*. Sem securina, a separase fica livre e ativa. *Segundo*, ubiquitina a ciclina B — degradando o motor da mitose e iniciando a saída de M.

A separase ativa imediatamente cliva a *#termo-nota[coesina][complexo proteico em forma de anel que abraça as duas cromátides-irmãs, mantendo-as unidas desde a fase S até a anáfase, quando é clivada pela separase]* — anéis proteicos que estavam abraçando as cromátides-irmãs desde a fase S. Cortar a coesina é como cortar a corda que segurava as duas metades de uma carga: as cromátides-irmãs, que estavam sendo puxadas em direções opostas pelos microtúbulos, separam-se subitamente e voam cada uma para seu polo.

#figura-nebli("/figuras/divisao-celular/slide-60.png",
  largura: 75%,
  legenda: [O gatilho molecular da anáfase: APC/C ativo → ubiquitina securina (que mantinha separase inativa) → securina destruída → separase livre → cliva Scc1 da coesina → cromátides-irmãs separam.])

Por que esse mecanismo é evolutivamente belo? Porque a separação é *química, não mecânica*. Os microtúbulos já estavam aplicando tensão sobre as cromátides desde a metáfase — mas a coesina segurava. A célula não precisa "puxar mais forte" — precisa apenas *cortar o que estava prendendo*. Quando a coesina é clivada, a tensão acumulada é o que dispara o movimento. É como cortar a corda de uma catapulta carregada: o trabalho mecânico já estava feito; só faltou liberar.

E por que é *irreversível*? Porque os dois eventos do APC/C — destruição de securina e destruição de ciclina B — são, eles próprios, irreversíveis (a célula não pode "des-degradar" uma proteína). Uma vez que coesina foi clivada, não dá pra recolá-la; uma vez que ciclina B caiu, o motor da mitose desliga e a célula tem que sair de M. O caminho é só pra frente — como vimos lá no 2.4.

Há ainda duas componentes mecânicas da anáfase que vale nomear. *Anáfase A* é o movimento das cromátides em direção aos polos, conduzido pelo encurtamento dos microtúbulos do cinetócoro (despolimerização na ponta + ação de motores moleculares). *Anáfase B* é o afastamento dos próprios polos do fuso, conduzido pelo crescimento dos microtúbulos interpolares e por motores como cinesinas que "empurram" os polos separados.

#mini-resumo[Gatilho da anáfase: APC/C ativo → destrói securina e ciclina B. Securina destruída → separase livre → cliva coesina → cromátides separam (a tensão dos microtúbulos já estava aplicada). Ciclina B destruída → M-CDK desliga → saída de M. Separação é química (cortar coesina), não mecânica. Irreversibilidade vem da degradação proteolítica.]

#subtopico("3.4 — Telófase e citocinese: o anel contrátil é actina + miosina II, não dineína")

Com o M-CDK desligado, as fosforilações que ele tinha feito começam a ser desfeitas por fosfatases. Os efeitos se invertem em ordem reversa: cromossomos descondensam (condensinas desfosforiladas), envelope nuclear remonta (laminas desfosforiladas reformam a lâmina), núcleos aparecem em cada polo. Essa é a *telófase* — visualmente, é a "imagem espelhada" da prófase.

Mas a célula ainda está com dois núcleos num único citoplasma. Falta dividir o citoplasma propriamente — a *citocinese*. Em células animais, isso acontece pela formação de um *anel contrátil* no equador da célula, composto principalmente de *#sigla("actina-F", [filamentos de actina polimerizados — formam o citoesqueleto e, junto com miosina II, o anel contrátil que constringe o sulco de clivagem na citocinese animal])* e *miosina II*, formando um #termo-nota[anel contrátil][estrutura de actina-F e miosina II que se monta sob a membrana plasmática no plano equatorial durante a citocinese animal; contrai como músculo, pinçando a célula em duas — em plantas, esse papel é feito pela placa celular por vesículas de Golgi]. O anel contrai progressivamente, pinçando a célula até a separação em duas — como apertar um balão na metade até dividi-lo em dois.

#figura-nebli("/figuras/divisao-celular/slide-66.png",
  largura: 65%,
  legenda: [Citocinese em célula animal: o anel contrátil de actina-F + miosina II posiciona-se sob a membrana, perpendicular ao eixo do fuso, e contrai. O sulco de clivagem aprofunda até a separação física das duas células-filhas.])

#confusao-prevista(
  titulo: "Anel contrátil = actina + miosina II, NÃO microtúbulos com dineína",
  aluno_acha: [aluno frequentemente assume que, como o fuso é feito de microtúbulos, a citocinese também usa microtúbulos e motores associados (dineína, cinesina).],
  mecanismo: [Errado. A citocinese animal usa *filamentos de actina* (não microtúbulos) e *miosina II* (não dineína nem cinesina). O fuso mitótico marca *onde* o anel se forma (no plano equatorial entre os polos) — sinaliza a posição. Mas a contração em si é actomiosina, o mesmo aparato do músculo. Em plantas, nem isso: a citocinese vegetal é por *placa celular*, vesículas de Golgi que se fundem no centro formando uma nova parede. Em prova de UC1: anel = actina + miosina II.],
)

#mini-resumo[Telófase = M-CDK desliga + fosfatases revertem efeitos: cromossomos descondensam, envelope remonta. Citocinese animal = anel contrátil de *actina + miosina II* (não microtúbulos, não dineína) constringe o sulco de clivagem. Citocinese vegetal = placa celular por vesículas de Golgi (não tem anel).]

#subtopico("3.5 — Quando algo dá errado: p53, Rb, HPV e o nascimento do câncer")

Fechando a apostila, vale juntar as peças clínicas em um quadro mais geral. O ciclo celular, como vimos, é um sistema de controle binário com feedback positivo e destruição programada. Quando esse sistema falha, a consequência genérica é uma das duas: ou a célula divide quando não deveria, ou a célula não morre quando deveria. As duas situações fazem câncer.

A peça reguladora mais central da disciplina é a *p53* — chamada por Vogelstein de "o guardião do genoma". Quando há dano no DNA detectado por ATM/ATR, p53 é estabilizada (em condições normais, p53 é continuamente degradada pelo #sigla("MDM2", [mouse double minute 2 — ligase de ubiquitina E3 que mantém p53 em concentração basal baixa em condições normais; o dano no DNA interrompe essa degradação, deixando p53 acumular]); o dano interrompe essa degradação). p53 ativa então três programas em paralelo: (a) *parada do ciclo* — via transcrição da CKI p21, que inibe CDK4/6 e CDK2; (b) *reparo do DNA* — via transcrição de genes de reparo; (c) *apoptose*, se o dano for irreparável — via transcrição de genes pró-apoptóticos da família Bax/Bak.

#figura-nebli("/figuras/divisao-celular/slide-69.png",
  largura: 70%,
  legenda: [p53 como hub central de resposta a dano no DNA: detecção (ATM/ATR) → estabilização (perda de degradação por MDM2) → ativação dos três programas (parada, reparo, apoptose). A escolha entre eles depende da intensidade e duração do dano.])

p53 está mutada ou inativada em mais de 50% de todos os tumores humanos. As consequências da perda de p53 são: o dano no DNA não é reparado → mutações se acumulam; a apoptose não é disparada → células com mutações sobrevivem; a parada do ciclo não acontece → essas células continuam se dividindo. Cada divisão acrescenta novas mutações, gerando heterogeneidade e capacidade de resistência a quimioterápicos.

A síndrome de *Li-Fraumeni* é o exemplo clínico clássico de perda hereditária de p53 — um alelo já vem mutado de família, basta perder o outro em alguma célula para o câncer aparecer. Pacientes com Li-Fraumeni desenvolvem múltiplos cânceres jovens (sarcomas, mama, leucemia, tumor cerebral).

E como o tratamento ataca células tumorais? Quimioterápicos como a *doxorrubicina* funcionam exatamente pela via que vimos: intercalam no DNA, inibem topoisomerase II, e geram quebras de dupla fita. Em uma célula com p53 funcional, esse dano dispara apoptose e a célula tumoral morre. Em uma célula com p53 mutado (50% dos tumores), o dano não é convertido em apoptose, e a célula sobrevive — daí a *resistência* de muitos tumores à doxorrubicina.

#clinica-box("Venetoclax e resgate da apoptose sem p53", [
Para tumores com p53 mutado, drogas que disparam apoptose por via *independente de p53* são uma estratégia poderosa. O *venetoclax* é um inibidor de #sigla("BCL-2", [B-cell lymphoma 2 — proteína anti-apoptótica que sequestra Bax e Bak, mantendo a mitocôndria estável; superexpressa em LLC, é alvo do venetoclax]), proteína anti-apoptótica frequentemente superexpressa em leucemias linfoides crônicas (LLC). Ao bloquear BCL-2, venetoclax libera diretamente a via apoptótica mitocondrial (Bax/Bak → citocromo c → caspase 9), sem precisar de p53. É a base do tratamento moderno de LLC com aproximadamente 80% de resposta inicial.
])

Outro eixo de inativação central é o *Rb*, como já vimos em 2.5. HPV oncogênico degrada Rb (via E7) e p53 (via E6), gerando o duplo nocaute. Mutações herdadas em Rb causam o *retinoblastoma* — tumor da retina em crianças, descoberto e estudado por Alfred Knudson nos anos 70 (origem da "hipótese dos dois golpes" — two-hit hypothesis — em câncer).

E os reguladores acima de tudo isso? A Profa. Cella menciona quatro "master regulators": *Ras*, *Myc*, *Rb* e *p53*. Ras e Myc são *oncogenes* (ganho de função dirige proliferação); Rb e p53 são *supressores tumorais* (perda de função permite proliferação). Quase todo câncer humano tem mutação em pelo menos um desses quatro eixos.

#conclusao-box[
*O princípio unificador.* O ciclo celular não é uma "sequência de fases" — é um *sistema de controle binário irreversível* em que cada transição é tudo-ou-nada, só dispara após verificação, e é "queimada" por destruição programada de proteínas-chave. Isso é o que permite à célula ser fiel em milhões de divisões.

*O mecanismo nuclear.* Ciclinas oscilam (ondas temporais de "qual fase é esta?"), CDKs executam fosforilando substratos específicos (mecanismo), APC/C e SCF destroem proteínas-alvo gerando irreversibilidade (queimar a ponte). Em paralelo, três checkpoints (G1/S, G2/M, fuso) integram condições e ou liberam ou param o motor. O sistema é multilateral porque os sinais a serem monitorados são multilaterais — nutrientes, dano genético, replicação, alinhamento.

*A clínica retomada.* p53 mutada em >50% dos tumores → dano não vira apoptose → mutações acumulam. HPV E6+E7 → degrada p53 e Rb → câncer cervical/orofaríngeo. SAC defeituoso → aneuploidia → instabilidade cromossômica dos tumores sólidos. Doxorrubicina = ataque via topoisomerase II → quebras → apoptose (se p53 funcional). Venetoclax = via independente de p53 (alvo BCL-2) → resgate em tumores com p53 mutada.

*A projeção.* No próximo resumo da UC — *apoptose e morte celular* — você vai ver a outra face desse sistema: quando a célula danificada não pode mais ser salva, como ela é eliminada sem causar inflamação? A apoptose é o programa que p53 dispara como última opção; entender o ciclo é pré-requisito para entender por que e quando esse programa é acionado. A próxima apostila começa exatamente nessa transição.
]
