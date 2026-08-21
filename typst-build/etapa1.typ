#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Um organismo com trilhões de células precisa que todas elas concordem sobre o que fazer com o combustível que chega — e ele chega em ondas: muito depois de uma refeição, quase nada na madrugada. A solução encontrada é química. Um punhado de moléculas circula pelo sangue em concentração ínfima, encontra receptores específicos e reorganiza o metabolismo de órgãos inteiros sem tocar em nenhum outro tecido. Este resumo persegue esse arranjo em três movimentos. Primeiro, quais alavancas a célula tem para mexer na velocidade de uma reação, e o que separa um hormônio das outras moléculas que sinalizam. Depois, a maquinaria que converte "o hormônio ligou no receptor" em "a enzima mudou de comportamento" — e por que essa conversão tem duas rotas de velocidades muito diferentes. Por fim, os hormônios que governam o combustível: insulina, glucagon, adrenalina, tireoidianos e cortisol, cada um visto pela cadeia inteira que vai do sinal ao efeito. A régua é sempre a mesma: quem se liga a quê, o que muda de forma por causa disso, e qual reação acelera ou para no fim da linha.
]

#parte-title("PARTE I — Regulação metabólica e a identidade do hormônio", primeira: true)

#subtopico("1.1 As três alavancas da regulação")

Regular o metabolismo é mexer na velocidade de reações químicas que já estão acontecendo. Nenhuma via metabólica é ligada ou desligada como um interruptor; o que existe é aceleração e freio sobre enzimas que estão sempre presentes, e o efeito de mexer numa única enzima se propaga por toda a via a jusante, porque o produto dela é o substrato da próxima. Por isso a regulação se concentra em poucos pontos — as reações irreversíveis, distantes do equilíbrio, que funcionam como torneiras da via inteira. *A célula tem três alavancas para mexer nessas torneiras, e a diferença decisiva entre elas é o tempo que levam para agir.*

A primeira alavanca é a *disponibilidade de substrato e a modulação alostérica*. Uma molécula pequena se encaixa num sítio da enzima fora do sítio ativo, a enzima muda de forma, e essa mudança de forma altera a facilidade com que o substrato entra ou o produto sai. Nada é quimicamente adicionado à enzima: o modulador chega, faz efeito enquanto está encaixado, e vai embora quando sua concentração cai. É a alavanca mais rápida que existe — responde em *segundos* e não custa energia. O #sigla("AMP", [adenosina monofosfato — sinal de que a célula está gastando reserva energética]) acumulado no músculo em esforço ativa a enzima que quebra glicogênio exatamente assim, sem intermediário nenhum.

A segunda alavanca é a *modificação covalente*: uma enzima pendura quimicamente um grupo em outra enzima. A modificação mais usada no metabolismo é a fosforilação — uma cinase transfere o fosfato terminal do #sigla("ATP", [adenosina trifosfato — moeda energética da célula]) para um resíduo de serina, treonina ou tirosina da proteína-alvo. Aquele fosfato carrega duas cargas negativas que antes não estavam ali, e a proteína se reorganiza ao redor delas: fica mais ativa ou menos ativa, conforme o caso. O detalhe que muda tudo é que a modificação *dura* — ela permanece até que uma fosfatase venha retirar o fosfato, o que faz dessa alavanca a única capaz de guardar, por minutos, a lembrança de um sinal que passou. É também a alavanca que os hormônios usam, e é por isso que ela domina o resto deste resumo.

A terceira alavanca é a *expressão gênica*: em vez de mudar o comportamento das enzimas que existem, a célula muda *quantas* enzimas existem, transcrevendo mais (ou menos) o gene correspondente. Como o caminho é longo — ativar transcrição, produzir #sigla("mRNA", [RNA mensageiro — cópia transitória do gene que o ribossomo lê para fabricar a proteína]), traduzir proteína, dobrá-la —, o efeito só aparece em *horas*, e desaparece na mesma lentidão, à medida que a proteína existente é degradada. É a alavanca da adaptação: jejum prolongado, exposição crônica a um hormônio, mudança de dieta que dura semanas.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-03.png",
  largura: 72%,
  legenda: [As três alavancas lado a lado. À esquerda, a modulação alostérica muda a forma da curva de velocidade (compare a sigmoide da enzima alostérica com a hipérbole da michaeliana). No meio, a modificação covalente pendura um fosfato vindo do ATP e uma fosfatase o remove. À direita, o hormônio que altera expressão. Repare que só a do meio deixa uma marca química que persiste depois do estímulo.])

#mini-resumo[Alostérico age em segundos e some com o modulador; covalente age em minutos e persiste até a fosfatase chegar; expressão age em horas e muda o estoque de enzima.]

As três não competem — se somam sobre a mesma enzima. A glicogênio-fosforilase, que vamos reencontrar na PARTE III, é simultaneamente ativada por AMP (alostérica), ativada por fosforilação (covalente) e produzida em quantidade regulada (expressão). *O ponto fino é que cada alavanca resolve um problema de horizonte diferente:* o AMP resolve o segundo seguinte de um sprint, a fosforilação resolve a hora seguinte de jejum, e a expressão resolve a semana seguinte de dieta. Guarde essa escala de tempo — ela vai voltar em 1.3 como critério para separar duas famílias inteiras de hormônios.

#subtopico("1.2 O que faz de uma molécula um hormônio")

Pense num prédio grande sem telefone: para avisar todo mundo de algo, você teria de subir andar por andar. É assim que a difusão simples funciona num organismo — lenta e local demais para coordenar fígado, músculo e tecido adiposo ao mesmo tempo. O hormônio é a solução de telefonia: a mensagem é despejada na corrente sanguínea, que já passa por todos os andares em cerca de um minuto, e só toca nos aparelhos que estão sintonizados naquela frequência. *A sintonia é o receptor* — e é ela, não a mensagem, que decide quem escuta.

Três características definem operacionalmente um hormônio. Ele é produzido numa parte do corpo e *regula função a distância*, num tecido diferente daquele que o fabricou. Ele age em *quantidades minúsculas* — nanomolar ou picomolar, milhões de vezes menos concentrado que a glicose que ele regula. E ele age *através de receptores*, proteínas que reconhecem sua forma com afinidade altíssima. Essas três características andam juntas por necessidade lógica: só é possível operar em concentração ínfima se o receptor tiver afinidade proporcionalmente alta, e só faz sentido despejar a molécula em todo o sangue se a especificidade do reconhecimento garantir que apenas o alvo responda.

#figura-lateral("/figuras/bioq-26-acao-hormonal/slide-10.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O critério da distância separa três modos de sinalizar com a mesma molécula. Na sinalização *endócrina*, a célula secretora joga o sinal no vaso e ele viaja pelo sangue até um alvo remoto — é o caso da insulina saindo do pâncreas e agindo no músculo da perna. Na *parácrina*, o sinal difunde pelo líquido intersticial e atinge a célula vizinha, sem entrar na circulação; é assim que a somatostatina de uma ilhota freia as células vizinhas dela mesma. Na *autócrina*, a célula responde ao sinal que ela própria secretou, o que serve para reforçar uma decisão já tomada — mecanismo fisiológico normal que só vira problema quando um tumor fecha essa alça e passa a estimular o próprio crescimento.],
  legenda: [Endócrino, parácrino e autócrino: a diferença é a distância percorrida, não a molécula.])

Um mesmo composto pode ocupar papéis diferentes conforme onde é liberado. A noradrenalina secretada por um terminal nervoso na fenda sináptica é neurotransmissor — atua a nanômetros de distância, em milissegundos, e é removida quase imediatamente. A mesma noradrenalina lançada no sangue pela medula da suprarrenal é hormônio — viaja, dura mais e atinge tecidos que nervo nenhum inerva. *A molécula não mudou; mudou o endereçamento.*

Regular um hormônio, então, não é regular um evento só. São sete pontos encadeados, e a fisiologia (assim como a farmacologia) intervém em qualquer um deles: *biossíntese*, *estocagem* em grânulo, *secreção*, *transporte* no plasma, *reconhecimento* pelo receptor, *resposta* intracelular e *degradação*. Um hormônio pode estar sendo produzido normalmente e mesmo assim faltar seu efeito, porque o receptor não o reconhece — é exatamente essa dissociação que sustenta o conceito de resistência hormonal, e voltaremos a ela na PARTE III.

#termo-nota[radioimunoensaio][método de dosagem em que hormônio marcado com isótopo e hormônio da amostra competem por um número fixo de anticorpos: quanto menos sinal radioativo ligado, mais hormônio havia na amostra] resolveu, nos anos 1960, o problema prático que essa lista cria. Medir algo em concentração nanomolar no meio do plasma exigia um método com sensibilidade absurda e especificidade suficiente para não confundir moléculas parecidas — e a competição por anticorpo entrega as duas coisas de uma vez. Foi ele que transformou "esse paciente parece ter pouco hormônio" em número, e por consequência transformou a endocrinologia numa disciplina quantitativa.

#subtopico("1.3 Classe química decide a rota")

Uma classificação de hormônios por estrutura química parece, à primeira vista, catalogação de livro-texto — o tipo de tabela que se decora e se esquece. Ela não é. *A estrutura química determina a solubilidade, a solubilidade determina onde fica o receptor, e onde fica o receptor determina se a resposta leva segundos ou horas.* Toda a lógica do resto do resumo cabe nessa cadeia de três consequências, e vale construí-la de cima para baixo.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-09.png",
  largura: 62%,
  legenda: [As quatro classes químicas do slide. Note que eicosanoides (derivados de ácido graxo) e esteroides (derivados do colesterol) têm cara de lipídio; catecolaminas e peptídicos, de molécula polar. Essa aparência é o que decide a rota.])

Os *peptídicos e proteicos* — insulina, glucagon, hormônio do crescimento — são cadeias de aminoácidos, cheias de grupos carregados e polares. As *catecolaminas* — adrenalina, noradrenalina, dopamina — derivam da tirosina e carregam hidroxilas e uma amina protonada. Ambos os grupos são hidrossolúveis: circulam dissolvidos no plasma, sem carona, e são *incapazes* de atravessar o interior oleoso da bicamada lipídica. Um hormônio peptídico jamais entra na célula-alvo; toda a sua ação nasce de um receptor voltado para fora.

Os *esteroides* — cortisol, aldosterona, testosterona, estradiol — vêm todos do colesterol e mantêm o esqueleto de quatro anéis fundidos, apolar. Os *hormônios tireoidianos* são a exceção que confunde: derivam da tirosina, como as catecolaminas, mas o acréscimo de iodo e o anel extra os tornam lipossolúveis. Esses dois grupos atravessam a membrana por difusão, e por isso seus receptores estão *dentro* da célula — no citosol ou já no núcleo. Como consequência de circularem num meio aquoso sendo apolares, precisam viajar ligados a proteínas transportadoras do plasma, e apenas a pequena fração livre é biologicamente ativa. Os *eicosanoides*, derivados do araquidonato, são lipídicos mas agem localmente, de modo parácrino, com receptores de membrana — a família que a aspirina inibe.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-15.png",
  largura: 56%,
  legenda: [Os dois mecanismos gerais. À esquerda, o hormônio peptídico ou amina fica fora e gera segundo mensageiro, que altera a atividade de enzimas que já existem. À direita, o esteroide ou tireoidiano entra, encontra o receptor e altera a *quantidade* de proteína recém-sintetizada. Rápido em cima, lento embaixo.])

A consequência funcional fecha o raciocínio, e é aqui que o aluno costuma derrapar. Como o hormônio lipossolúvel entra sozinho e não precisa de intermediário, parece natural concluir que ele age mais rápido. Acontece o contrário: quem entra vai mexer na transcrição de genes, e transcrever, traduzir e acumular proteína nova leva horas a dias. Quem fica de fora usa um segundo mensageiro para modificar covalentemente enzimas que já estão prontas no citosol, e isso leva segundos a minutos. *Entrar é rápido; o efeito de quem entra é lento.*

#confusao-prevista(
  titulo: "Lipossolúvel não quer dizer resposta rápida",
  aluno_acha: [aluno acha que, por atravessar a membrana sem ajuda, o esteroide age mais depressa que o peptídico],
  mecanismo: [a velocidade da resposta não depende de quanto tempo o hormônio leva para chegar ao receptor, e sim do *tipo de alavanca* que o receptor aciona. Receptor de membrana aciona modificação covalente de enzima pronta — segundos a minutos. Receptor nuclear aciona expressão gênica — horas a dias. É a segunda e a terceira alavanca de 1.1 reaparecendo, agora divididas entre duas famílias de hormônios.],
)

Repare no que acabou de acontecer: a tabela de classes químicas deixou de ser catálogo e virou previsão. Diante de um hormônio novo, saber apenas se ele é polar ou apolar já permite antecipar onde está seu receptor, que tipo de alavanca metabólica ele aciona e em quanto tempo o efeito aparece. *É essa maquinaria que a PARTE II abre por dentro* — primeiro os tipos de receptor de membrana, depois a cascata que eles disparam, e por fim o receptor nuclear que faz o oposto.

#parte-title("PARTE II — A máquina da transdução do sinal")

#subtopico("2.1 Cinco jeitos de atravessar a membrana")

Ficou estabelecido em 1.3 que o hormônio hidrossolúvel para na porta e precisa de alguém do lado de dentro para continuar o recado. Esse alguém é o receptor de membrana — uma proteína que atravessa a bicamada de lado a lado, com uma parte voltada para o líquido extracelular e outra para o citosol. Quando o hormônio se encaixa na parte de fora, a proteína inteira muda de conformação, e essa mudança de forma *é* a passagem da informação: nada material atravessou a membrana, apenas uma torção mecânica propagada ao longo da mesma molécula. O que muda de uma família de receptores para outra é o que essa torção libera do lado de dentro.

O jeito mais direto é o *canal iônico controlado por ligante*. O receptor já é o canal: o ligante se encaixa, o poro abre, íons descem seu gradiente e o potencial de membrana muda. Não há intermediário químico nenhum, e por isso a resposta é a mais rápida de todas — *milissegundos*. É como o receptor nicotínico de acetilcolina funciona na junção neuromuscular.

O segundo jeito é o *receptor acoplado à proteína G*, o mais numeroso do organismo. Ele atravessa a membrana sete vezes e, ao mudar de forma, ativa uma proteína intracelular que troca #sigla("GDP", [guanosina difosfato — forma "desligada" da proteína G]) por #sigla("GTP", [guanosina trifosfato — nucleotídeo cuja ligação liga a proteína G e cuja hidrólise a desliga]). Essa proteína ativada, por sua vez, liga uma enzima que fabrica um mensageiro pequeno e difusível — o famoso segundo mensageiro. A resposta leva *segundos*, e é a via de glucagon, adrenalina e da maioria dos hormônios peptídicos.

O terceiro jeito é o *receptor com atividade enzimática própria*, tipicamente uma tirosina-cinase. O ligante faz duas moléculas do receptor se aproximarem, e cada uma fosforila a outra — a autofosforilação cria docas para proteínas do citosol, que se acoplam ali e disparam cascatas de fosforilação. A resposta leva *minutos*, e é assim que a insulina age. Uma variante importante é o *receptor guanilil-ciclase*: aqui o próprio receptor produz #sigla("GMPc", [guanosina monofosfato cíclico — segundo mensageiro que relaxa músculo liso vascular]), sem intermediário nenhum entre reconhecimento e síntese do mensageiro.

O quinto jeito é o *receptor nuclear*, que nem fica na membrana — ele espera o hormônio lipossolúvel dentro da célula e age sobre o DNA, com resposta em *horas*. Ele fecha a lista por contraste, e é o assunto de 2.3.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-14.png",
  largura: 74%,
  legenda: [Os quatro grandes tipos de transdutor com a escala de tempo embaixo — milissegundos no canal iônico, segundos no acoplado à proteína G, horas nos que dependem de transcrição. A linha de baixo é a informação que mais rende: a arquitetura do receptor prevê a velocidade da resposta.])

Um detalhe organiza toda essa variedade e explica boa parte da farmacologia: *o mesmo ligante pode ter receptores de tipos diferentes em tecidos diferentes*. A acetilcolina abre um canal iônico no músculo esquelético (receptor nicotínico, contração em milissegundos) e ativa uma proteína G no nó sinoatrial do coração (receptor muscarínico, redução de frequência em segundos). A adrenalina, que vamos ver em 3.2, tem subtipos de receptor que ativam proteínas G opostas — uns aumentam o segundo mensageiro, outros o diminuem. *A especificidade da resposta, portanto, não mora no hormônio: mora no repertório de receptores que cada tecido expressa.* É o que permite que uma única molécula lançada no sangue acelere o coração e relaxe o brônquio ao mesmo tempo.

#subtopico("2.2 A cascata do AMPc e a amplificação")

Imagine um sistema de alavancas em série: você empurra a primeira com o dedo, ela empurra dez outras, cada uma dessas empurra dez, e no fim uma parede se move. Nenhuma alavanca isolada é forte; a força vem do arranjo em série, porque cada estágio é *catalítico* — não gasta a si mesmo ao ativar o próximo, e por isso ativa muitos. A cascata hormonal é exatamente esse arranjo, e é ela que explica como um hormônio em concentração nanomolar consegue mobilizar milimoles de glicose.

Vale seguir a cadeia inteira, com o glucagon no fígado como exemplo. O hormônio se encaixa no receptor de sete hélices; o receptor muda de forma e passa a funcionar como trocador de nucleotídeo sobre a #termo-nota[proteína G][conjunto de três subunidades — alfa, beta e gama — ancorado à face interna da membrana, que funciona como interruptor temporizado do sinal] que está logo abaixo, fazendo sua subunidade alfa soltar GDP e pegar GTP. A subunidade alfa com GTP se desprende das outras duas, desliza pela face interna da membrana e ativa a *adenilil-ciclase*, que converte ATP em #sigla("AMPc", [adenosina monofosfato cíclico — segundo mensageiro que transmite ao citosol a chegada do hormônio]). O AMPc se acumula no citosol e encontra a *proteína-cinase A*, ou #sigla("PKA", [proteína-cinase A — enzima ativada pelo AMPc que fosforila alvos em serina e treonina]), que no repouso é um bloco de quatro subunidades: duas catalíticas travadas por duas regulatórias. Quatro moléculas de AMPc se ligam às regulatórias, elas soltam as catalíticas, e as catalíticas livres saem fosforilando. Uma delas fosforila a *fosforilase-cinase*, que por sua vez fosforila a *glicogênio-fosforilase*, que finalmente arranca glicose do glicogênio.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-37.png",
  largura: 63%,
  legenda: [A cascata completa, do receptor de sete hélices à fosforilase ativa. Siga as setas contando os degraus: receptor, proteína G, adenilil-ciclase, AMPc, PKA, fosforilase-cinase, fosforilase. Cada degrau é um ponto de multiplicação — e também um ponto onde a célula pode intervir para desligar.])

Contar os degraus não é exercício de decoreba: cada um deles multiplica. Um único receptor ocupado ativa dezenas de proteínas G enquanto o hormônio está ligado; cada adenilil-ciclase ativada produz milhares de moléculas de AMPc por segundo; cada PKA liberada fosforila muitas fosforilase-cinases, e cada fosforilase-cinase muitas fosforilases. O ganho total chega a algo entre dez mil e cem milhões de vezes. *A amplificação não vem da quantidade de hormônio que chega — vem de cada estágio ser um catalisador que age sobre muitas cópias do estágio seguinte.*

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-16.png",
  largura: 58%,
  legenda: [A pirâmide da amplificação: um sinal no topo, muitos canais e enzimas afetados na base. É a mesma cascata da figura anterior, desenhada pelo número de moléculas em cada degrau.])

O contrafactual ajuda a fixar por que a natureza escolheu esse arranjo. Se o hormônio agisse diretamente sobre a enzima final, seria preciso uma molécula de hormônio para cada molécula de fosforilase a ser ativada — concentração plasmática de hormônio na mesma ordem da concentração de enzima no fígado, o que é fisiologicamente impossível e metabolicamente caríssimo. A cascata compra amplificação em troca de alguns milissegundos de atraso, e ainda ganha de brinde vários pontos de controle independentes ao longo do caminho.

Ligar com esse ganho todo exige um desligamento igualmente robusto, e a célula tem três freios. A subunidade alfa da proteína G é ela mesma uma enzima que hidrolisa lentamente o próprio GTP a GDP e se autodesliga — um temporizador embutido. O AMPc é destruído pela #termo-nota[fosfodiesterase][enzima que hidrolisa o anel do AMPc gerando 5'-AMP inativo, encerrando o sinal do segundo mensageiro], e não simplesmente diluído. E as fosforilações são revertidas por fosfatases. Esses freios são alvos farmacológicos diretos — a cafeína prolonga o efeito do AMPc inibindo fosfodiesterase, e a toxina da cólera trava a subunidade alfa na forma ligada a GTP, deixando o AMPc permanentemente alto no enterócito com a diarreia maciça que daí decorre.

#mini-resumo[O hormônio torce o receptor, o receptor liga a proteína G, a proteína G liga a ciclase que fabrica AMPc, e o AMPc solta a PKA, que fosforila os alvos. O ganho chega a cem milhões de vezes, e três freios independentes encerram o sinal: a proteína G se autodesliga, a fosfodiesterase destrói o AMPc e as fosfatases retiram os fosfatos.]

Nem todo hormônio que usa proteína G aumenta o AMPc. Há subtipos de proteína G *inibitórios*, que ao serem ativados freiam a adenilil-ciclase em vez de estimulá-la — de modo que dois hormônios podem chegar à mesma célula, usar a mesma enzima como alvo e produzir efeitos opostos, apenas por acoplarem a proteínas G de sinal contrário. E a cascata não termina no citosol: a PKA que sobrou entra no núcleo e fosforila fatores de transcrição, ligando a segunda alavanca de 1.1 na terceira. *Um estímulo hormonal sustentado começa mexendo em enzimas prontas e termina mexendo em quantas enzimas existem.*

#subtopico("2.3 O receptor que reescreve o programa")

A modificação covalente tem um limite estrutural: por mais que fosforile, ela só consegue mexer no que já está lá. Se a célula precisa de dez vezes mais de uma enzima que quase não possui, nenhuma cascata resolve — é preciso fabricar. *Esse é o problema que o receptor nuclear existe para resolver*, e por isso ele opera numa lógica completamente diferente da que acabamos de percorrer.

O hormônio lipossolúvel atravessa a membrana por difusão e encontra seu receptor no citosol. Fora da presença do hormônio, esse receptor está segurado por #termo-nota[chaperonas][proteínas acompanhantes, entre elas a proteína de choque térmico de 90 kDa, que mantêm o receptor dobrado, inativo e retido no citosol até a chegada do hormônio] — o que o impede de ir ao núcleo. A ligação do hormônio muda a conformação do receptor, as chaperonas se soltam, e fica exposto o sinal que o endereça ao núcleo. Lá dentro, dois complexos hormônio-receptor se emparelham formando um dímero, e o dímero reconhece uma sequência curta e específica de DNA: o #termo-nota[elemento responsivo][trecho de poucos pares de base, situado na região reguladora do gene, que funciona como endereço de acoplamento para um receptor hormonal específico]. Acoplado ali, o receptor recruta coativadores que afrouxam a cromatina e facilitam a montagem da maquinaria de transcrição. O gene passa a ser copiado em mRNA, o mRNA é traduzido, e só então — horas depois — a proteína nova aparece em quantidade suficiente para mudar o metabolismo.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-49.png",
  largura: 58%,
  legenda: [Três instantes do mesmo receptor sobre o DNA: sozinho, com o hormônio ligado, e finalmente recrutando o coativador. Repare que o receptor já está encostado na dupla-hélice — o hormônio não o leva até o DNA, ele autoriza o recrutamento do que vem depois.])

Dois refinamentos evitam a leitura ingênua de que receptor nuclear "liga gene". Primeiro, o mesmo complexo pode recrutar *correpressores* em vez de coativadores, e nesse caso o efeito do hormônio é reduzir a transcrição de determinado gene — o receptor de glicocorticoide faz isso quando bloqueia fatores de transcrição inflamatórios, e é daí que vem o efeito anti-inflamatório do cortisol e dos corticoides usados na clínica. Segundo, alguns receptores dessa família — o de hormônio tireoidiano é o exemplo — já vivem grudados ao DNA *reprimindo* o gene, e a chegada do hormônio troca o correpressor por coativador. Nesses casos, a ausência de hormônio não é neutra: é repressão ativa.

#atencao-box("Resposta lenta não é resposta fraca", [O leitor tende a hierarquizar as duas rotas pela velocidade e concluir que a transcricional é a coadjuvante. É o contrário em potência: a cascata de fosforilação muda o *comportamento* das enzimas existentes e se desfaz assim que as fosfatases agem, enquanto a via nuclear muda *quantas* enzimas existem — um efeito que persiste enquanto a proteína nova durar, dias inclusive. Por isso o hormônio tireoidiano define a taxa metabólica basal do organismo inteiro e o corticoide altera a resposta imune por semanas, coisas que nenhuma cascata de AMPc conseguiria sustentar.])

Com as duas rotas abertas — a rápida, que modifica enzima pronta, e a lenta, que muda o estoque de enzima —, o vocabulário está completo. *A PARTE III passa a usá-lo:* cada hormônio do metabolismo a seguir será descrito pela mesma sequência de perguntas, e a resposta a elas é toda a diferença entre insulina, glucagon, adrenalina, tireoidiano e cortisol.

#parte-title("PARTE III — Os hormônios do metabolismo em ação")

#subtopico("3.1 Insulina: sensor, secreção e efeito")

A insulina é o hormônio da abundância: ela é secretada quando há mais combustível circulando do que o necessário no momento, e sua mensagem para o organismo inteiro é *guarde*. Toda a sua história — como é fabricada, o que dispara sua saída e o que ela faz ao chegar — decorre dessa função única, e vale segui-la do gene até o efeito, porque cada etapa tem consequência clínica direta.

A célula beta da ilhota pancreática transcreve e traduz uma cadeia única, a pré-pró-insulina. A sequência-sinal da ponta a endereça ao retículo endoplasmático e é removida ali, sobrando a pró-insulina — uma cadeia dobrada sobre si mesma, com três pontes dissulfeto já formadas. No complexo de Golgi e no grânulo de secreção, uma #termo-nota[pró-hormônio convertase][protease que corta o precursor em sítios específicos de aminoácidos básicos, liberando o hormônio maduro a partir de uma cadeia inativa maior] recorta o pedaço do meio. O que sai são duas coisas em quantidade rigorosamente igual: a insulina madura, com suas cadeias A e B unidas pelas pontes, e o #termo-nota[peptídeo C][segmento de conexão descartado na maturação da insulina e secretado junto com ela em proporção de um para um] descartado do meio da cadeia.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-22.png",
  largura: 62%,
  legenda: [Da pré-pró-insulina à insulina madura. As pontes dissulfeto se formam *antes* do corte — é por isso que as duas cadeias continuam juntas depois que o peptídeo C sai. À direita, o mesmo trajeto pelo retículo, Golgi e grânulo.])

Essa proporção de um para um parece detalhe de bioquímica e é, na prática, um exame. Insulina fabricada em laboratório e injetada não vem acompanhada de peptídeo C. Então, diante de uma hipoglicemia com insulina alta, medir o peptídeo C responde uma pergunta que a dosagem de insulina sozinha não responde: se ele está alto, a insulina veio da própria célula beta do paciente; se está baixo, a insulina veio de fora.

O gatilho da secreção é o que torna a célula beta um sensor, e a cadeia é bonita de acompanhar. A glicose entra na célula beta por um transportador de #sigla("GLUT", [glucose transporter — família de transportadores que levam glicose por difusão facilitada, a favor do gradiente]) do tipo 2, que tem afinidade baixa e por isso só carrega bastante glicose quando a glicemia sobe. Dentro, ela é fosforilada pela #termo-nota[glicoquinase][isoforma da hexoquinase presente no fígado e na célula beta, com afinidade baixa pela glicose e sem inibição pelo próprio produto], que também tem afinidade baixa — de modo que a velocidade da via depende da glicemia em vez de estar sempre saturada. A glicose fosforilada segue pela glicólise e pela mitocôndria, e a razão entre ATP e #sigla("ADP", [adenosina difosfato — forma "descarregada" do ATP]) sobe dentro da célula. Esse ATP fecha um canal de potássio da membrana que, no repouso, ficava aberto deixando K⁺ vazar para fora. Com o vazamento interrompido, cargas positivas se acumulam dentro e a célula despolariza; a despolarização abre canais de cálcio dependentes de voltagem; o cálcio que entra faz os grânulos se fundirem à membrana. *A célula beta transformou concentração de glicose em quantidade de insulina secretada, e o intermediário dessa conversão é o ATP.*

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-26.png",
  largura: 70%,
  legenda: [O acoplamento completo, em seis passos: GLUT2, glicoquinase, oxidação mitocondrial, fechamento do canal de K⁺, despolarização com entrada de Ca²⁺, e exocitose. Cada seta é um ponto onde uma droga ou uma mutação pode agir — e agem, nos dois sentidos.])

#atencao-box("O ATP fecha o canal de potássio, não abre", [A leitura intuitiva erra o sinal: como o ATP é combustível, parece que ele *abre* algo. Não é o que acontece. O canal de potássio da célula beta está *aberto* no repouso, mantendo o interior bem negativo e a célula quieta; o ATP é o que o *fecha*. Fechar o canal é o que despolariza. A consequência prática é imediata e vale nos dois sentidos: droga que fecha o canal força secreção de insulina (as sulfonilureias), e droga que o mantém aberto bloqueia a secreção (usada quando há insulina em excesso). Trocar o sinal aqui inverte o tratamento inteiro.])

#clinica-box("Duas doenças pelo mesmo canal", [As *sulfonilureias*, usadas no diabetes tipo 2, ligam-se ao canal de potássio sensível ao ATP e o fecham independentemente do estado energético da célula. A célula beta despolariza, o cálcio entra e a insulina sai — o que funciona justamente porque, nesse tipo de diabetes, a célula beta ainda existe e ainda tem insulina estocada; o problema principal é a resposta insuficiente dos tecidos periféricos. O reverso da moeda é o *insulinoma*, tumor de células beta que secreta insulina sem obedecer à glicemia: o paciente tem hipoglicemia com insulina e peptídeo C altos, o tratamento definitivo é cirúrgico, e o controle medicamentoso enquanto isso usa exatamente o oposto da sulfonilureia — um fármaco que mantém o canal de potássio aberto e impede a despolarização.])

Do lado do tecido-alvo, o receptor de insulina é um receptor com atividade tirosina-cinase, como visto em 2.1: a ligação aproxima as duas metades, elas se autofosforilam e recrutam proteínas do citosol, que ativam a proteína-cinase B — a #sigla("PKB", [proteína-cinase B, também chamada Akt — cinase central da via da insulina]). A partir dela, três efeitos merecem ser separados. No músculo e no tecido adiposo, vesículas carregadas de transportadores GLUT4 já prontos são levadas até a membrana e se fundem a ela, multiplicando a captação de glicose — *a insulina não manda fabricar transportador, ela manda o transportador que já existe subir para a superfície*. No fígado e no músculo, a PKB ativa a #sigla("PP1", [proteína-fosfatase 1 — fosfatase que remove fosfatos das enzimas do metabolismo do glicogênio]), que retira fosfato da glicogênio-sintase (ativando-a) e da glicogênio-fosforilase (inativando-a) — uma única fosfatase virando a chave nos dois sentidos ao mesmo tempo. E a mesma via inibe a glicogênio-sintase-cinase 3, que no jejum mantinha a sintase fosforilada e desligada.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-32.png",
  largura: 62%,
  legenda: [O leque da insulina saindo da PKB. Siga os dois ramos de baixo: a mesma fosfatase ativada torna a sintase ativa e a fosforilase inativa. Na direita, a fosfodiesterase ativada derruba o AMPc — a insulina apaga o sinal do glucagon além de acionar o seu próprio.])

Repare no acabamento fino desse arranjo: a via da insulina também ativa a fosfodiesterase, que destrói o AMPc acumulado. Ela não se limita a empurrar o metabolismo para a estocagem — ela *desliga a mensagem contrária* que estava em curso. Por isso insulina e glucagon não precisam brigar molécula a molécula: quem chega por último apaga o recado do outro.

A família de transportadores que a insulina mobiliza é um bom retrato de como afinidade define papel fisiológico. Todos os GLUT têm a mesma arquitetura e o mesmo mecanismo — difusão facilitada, a favor do gradiente, sem gasto de ATP —, e o que muda entre eles é a concentração de glicose em que trabalham bem. Como a glicemia normal gira em torno de 5 mM, é em relação a esse valor que a tabela organiza a família.

#table(
  columns: (auto, auto, 1fr, 1fr),
  inset: 7pt,
  align: (left, center, left, left),
  stroke: 0.5pt + gray-border,
  table.header(
    [*Transportador*], [*Afinidade*], [*Onde está*], [*Papel*]
  ),
  [GLUT1], [alta], [hemácia, barreira hematoencefálica], [captação basal contínua, funciona saturado em qualquer glicemia],
  [GLUT2], [baixa], [fígado, célula beta, intestino, rim], [sensor: só carrega bastante quando a glicemia sobe],
  [GLUT3], [alta], [neurônio], [garante suprimento mesmo na hipoglicemia leve],
  [GLUT4], [intermediária], [músculo esquelético, adipócito, coração], [único dependente de insulina para chegar à membrana],
)

O padrão salta aos olhos quando lido pela coluna do meio: os tecidos que não toleram interrupção — hemácia e cérebro — usam transportadores de afinidade alta, que trabalham praticamente saturados o tempo todo e não dependem de hormônio nenhum. Fígado e célula beta usam o de afinidade baixa justamente porque precisam *perceber* a variação da glicemia, não ignorá-la. E só músculo e adipócito, que podem esperar, ficam na dependência da insulina. *É por isso que o cérebro de um diabético sem insulina continua recebendo glicose enquanto o músculo passa fome no meio da hiperglicemia.*

#subtopico("3.2 Glucagon e adrenalina na escassez")

Se a insulina diz *guarde*, o glucagon diz *libere* — e a simetria vai além do slogan, porque as duas células que os produzem são vizinhas na mesma ilhota e leem o mesmo sangue. O glucagon é um peptídeo de 29 aminoácidos secretado pelas células alfa; sua secreção sobe na hipoglicemia, com aumento de aminoácidos no plasma (uma refeição proteica exige contrarregulação para a glicemia não despencar com a insulina que a proteína também estimula) e sob adrenalina. E é freada pela própria insulina, pelos corpos cetônicos e pela ureia — ou seja, pelos sinais de que a mobilização já está funcionando.

O precursor do glucagon mostra um princípio que vale para muitos hormônios peptídicos: *o mesmo gene rende produtos diferentes conforme a protease predominante no tecido*. O pró-glucagon é uma cadeia longa com vários segmentos em fila. Na célula alfa do pâncreas predomina uma convertase que corta liberando glucagon. No intestino e no encéfalo predomina outra, que corta em sítios distintos e libera #sigla("GLP-1", [peptídeo semelhante ao glucagon 1 — hormônio intestinal liberado com a refeição]), uma #termo-nota[incretina][hormônio secretado pelo intestino durante a absorção que amplifica a secreção de insulina antes mesmo de a glicemia subir muito]. A consequência é elegante: a mesma sequência de DNA origina o hormônio que *sobe* a glicemia no pâncreas e o hormônio que ajuda a *baixá-la* quando fabricado no intestino.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-36.png",
  largura: 60%,
  legenda: [O pró-glucagon e seus dois destinos. À esquerda, a convertase dominante na célula alfa; à direita, a dominante no intestino e no encéfalo. Mesmo precursor, produtos com efeitos opostos sobre a glicemia.])

O alvo do glucagon é praticamente só o fígado, e isso não é acaso: é o único órgão que pode devolver glicose ao sangue, porque é o único que tem a enzima capaz de retirar o fosfato da glicose-6-fosfato. A cascata é a que já percorremos em 2.2 — receptor de sete hélices, proteína G, AMPc, PKA —, e a PKA aciona três frentes ao mesmo tempo: acelera a degradação de glicogênio (fosforilando a fosforilase-cinase), trava a síntese de glicogênio (fosforilando a sintase, que se inativa quando fosforilada), e desloca o fígado da glicólise para a gliconeogênese. Em jejum mais prolongado, o mesmo estímulo aumenta a produção de corpos cetônicos a partir dos ácidos graxos, fornecendo ao encéfalo um combustível alternativo à glicose.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-38.png",
  largura: 62%,
  legenda: [O mapa do glucagon sobre o fígado: glicogenólise e gliconeogênese ligadas, glicólise e síntese de glicogênio desligadas, cetogênese em curso. Repare que músculo e adipócito aparecem como fornecedores de matéria-prima, não como alvos do hormônio.])

#confusao-prevista(
  titulo: "Glucagon não age no músculo",
  aluno_acha: [aluno acha que o glicogênio muscular também é mobilizado pelo glucagon para sustentar a glicemia],
  mecanismo: [o músculo não expressa receptor de glucagon, e mesmo se quebrasse glicogênio não conseguiria exportar glicose — falta-lhe a glicose-6-fosfatase, de modo que a glicose fosforilada fica presa lá dentro e é queimada localmente. O glicogênio muscular é reserva *privada*, mobilizada pela adrenalina para uso do próprio músculo. Quem sustenta a glicemia é o fígado.],
)

A adrenalina resolve um problema parecido com urgência diferente. Ela é sintetizada na medula da suprarrenal a partir da tirosina, numa sequência curta: tirosina, #sigla("DOPA", [di-hidroxifenilalanina — primeiro intermediário da via das catecolaminas]), dopamina, noradrenalina, adrenalina. A primeira enzima da via, a tirosina-hidroxilase, é a mais lenta e por isso governa a velocidade de toda a sequência — é nela que a célula controla a produção, e não nas seguintes.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-40.png",
  largura: 60%,
  legenda: [A via da tirosina à adrenalina, com a etapa limitante marcada logo no primeiro passo. Cada enzima adiciona uma modificação pequena — uma hidroxila, uma descarboxilação, um grupo metil — e é essa última metilação que separa noradrenalina de adrenalina.])

Diferente do glucagon, a adrenalina age em vários tecidos ao mesmo tempo, porque quase todos expressam algum subtipo de seu receptor. No fígado, sobe o AMPc e mobiliza glicogênio como o glucagon faria. No músculo, mobiliza o glicogênio local para consumo próprio. No tecido adiposo, ativa a lipólise e libera ácidos graxos. No coração, aumenta frequência e força de contração; no brônquio, relaxa a musculatura lisa. E na própria ilhota ela inclina a balança: estimula glucagon e freia insulina, reforçando o sentido mobilizador de tudo o mais. *Uma única molécula produz esse conjunto porque cada tecido tem um repertório de receptores diferente* — exatamente o princípio anunciado em 2.1.

#clinica-box("Adrenalina na anafilaxia", [O uso clínico mais dramático da adrenalina reúne quase todos esses efeitos numa injeção só. Na anafilaxia, a liberação maciça de mediadores dilata arteríolas (pressão desaba), contrai brônquios (o ar não passa) e aumenta a permeabilidade capilar (líquido sai do vaso e a via aérea superior incha). A adrenalina reverte os três pelo mesmo hormônio em receptores diferentes: contrai a arteríola e recupera a pressão, relaxa o músculo liso brônquico e abre a via aérea, e estabiliza a liberação de mediadores pelos mastócitos. É também por reunir esses efeitos que ela entra na parada cardíaca e no choque — não é "estimulante" genérico, é a soma de ações vasculares e cardíacas previsíveis a partir de qual receptor existe em cada tecido.])

#subtopico("3.3 Tireoidianos, cortisol e impostores")

Os dois hormônios que fecham este resumo trabalham pela rota lenta de 2.3, e por isso não servem para responder a uma queda de glicemia em minutos — servem para *definir o patamar* em que o metabolismo inteiro opera nos próximos dias. Vale começar pelos tireoidianos, porque neles a distinção entre hormônio circulante e hormônio ativo é o ponto que organiza tudo o mais.

A tireoide produz predominantemente tiroxina, ou T4, com quatro iodos, e uma fração bem menor de tri-iodotironina, o T3. O que circula em quantidade, portanto, é o T4 — e é justamente ele que tem afinidade baixa pelo receptor. No tecido-alvo, uma #termo-nota[deiodinase][enzima que retira um átomo de iodo do T4, convertendo-o no T3, que é a forma com afinidade alta pelo receptor nuclear] faz a conversão. A consequência é que *cada tecido regula localmente quanta hormonalidade recebe*, ajustando a atividade da própria deiodinase, enquanto o plasma mantém um reservatório estável de T4. O T3 formado entra no núcleo, liga-se ao receptor tireoidiano que já está sobre o DNA emparelhado com o receptor de retinoide X, o #sigla("RXR", [receptor de retinoide X — parceiro obrigatório de vários receptores nucleares na ligação ao DNA]), e troca o correpressor por coativador, ligando a transcrição de genes que estavam ativamente reprimidos.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-45.png",
  largura: 72%,
  legenda: [À esquerda, os órgãos-alvo com o efeito de cada um; à direita, o mecanismo molecular: T4 chega, a deiodinase gera T3, o T3 encontra o receptor já pousado no elemento responsivo junto com o RXR, e a transcrição começa. O detalhe importante é que o receptor não sai do DNA — o hormônio só troca a companhia que ele recruta.])

Os efeitos do T3 fazem sentido como um único tema: *acelerar o metabolismo basal e amplificar a resposta a outros sinais*. Ele aumenta o consumo de oxigênio e a produção de calor em quase todos os tecidos, acelera a degradação de colesterol pelo fígado, mobiliza proteína muscular e glicose, e é indispensável ao crescimento ósseo e à maturação do sistema nervoso na infância. No coração, o mecanismo é particularmente instrutivo: o T3 aumenta a *expressão* de receptores adrenérgicos — de modo que a mesma adrenalina circulante produz taquicardia maior. É o hormônio lento regulando a sensibilidade ao hormônio rápido, e explica por que palpitação e tremor dominam o quadro do excesso de hormônio tireoidiano.

A produção é comandada de cima: o hipotálamo libera #sigla("TRH", [hormônio liberador de tireotrofina — peptídeo hipotalâmico que comanda a hipófise]), a hipófise libera #sigla("TSH", [hormônio tireoestimulante — hormônio hipofisário que estimula a tireoide a produzir e liberar T3 e T4]), e a tireoide produz. O T3 e o T4 circulantes freiam hipotálamo e hipófise — alça de retroalimentação negativa. Como o freio é sensível, o TSH se move na direção contrária à do hormônio da glândula: tireoide preguiçosa deixa o freio frouxo e o TSH sobe; tireoide em excesso aperta o freio e o TSH despenca. *Ler o TSH, portanto, é ler indiretamente quanto hormônio a hipófise está enxergando* — e é por isso que ele é a primeira dosagem pedida na suspeita de doença tireoidiana.

O cortisol repete a arquitetura com outro conteúdo. Ele é sintetizado no córtex da suprarrenal a partir do colesterol, numa cadeia de hidroxilações sucessivas cuja primeira etapa — a conversão de colesterol em pregnenolona — é a limitante e o alvo do estímulo hipofisário. O eixo é o mesmo em desenho: o hipotálamo libera #sigla("CRH", [hormônio liberador de corticotrofina — peptídeo hipotalâmico que responde ao estresse]), a hipófise libera #sigla("ACTH", [hormônio adrenocorticotrófico — hormônio hipofisário que estimula o córtex da suprarrenal]), e o cortisol produzido freia os dois andares acima.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-52.png",
  largura: 60%,
  legenda: [O cortisol atravessa a membrana, encontra o receptor preso à chaperona no citosol, o complexo se solta e entra no núcleo, liga-se ao elemento responsivo e altera a transcrição — para mais ou para menos, conforme o gene. Compare com a figura da PARTE II: é a mesma coreografia, agora com o hormônio da suprarrenal.])

No metabolismo, o cortisol é o hormônio da escassez prolongada, e é útil lê-lo como fornecedor de matéria-prima para a gliconeogênese: ele degrada proteína muscular liberando aminoácidos, mobiliza glicerol do tecido adiposo, e no fígado induz a *síntese* das enzimas gliconeogênicas — a terceira alavanca de 1.1, agora em ação. Ao mesmo tempo, reduz a captação de glicose no músculo e no adiposo, o que se soma para elevar a glicemia. Em excesso e por tempo longo, esse mesmo conjunto redistribui gordura para o tronco, afina a musculatura dos membros e produz intolerância à glicose. E, por recrutar correpressores sobre genes inflamatórios, ele suprime a resposta imune — o efeito que a clínica usa deliberadamente.

#clinica-box("Addison e Cushing: o eixo lido nos dois sentidos", [Na *doença de Addison*, a destruição autoimune do córtex da suprarrenal derruba a produção de cortisol. Como o freio sobre a hipófise desaparece, o ACTH sobe muito — e aqui vem o detalhe mecanístico que costura o quadro: os primeiros aminoácidos do ACTH são os mesmos do hormônio estimulante de melanócitos, de modo que o excesso de ACTH estimula a produção de melanina e escurece a pele. O paciente tem fraqueza, hipoglicemia, perda de peso e hiperpigmentação — *e é o hormônio de cima, não o de baixo, que explica a cor da pele*. No *excesso* de glicocorticoide (síndrome de Cushing, seja por tumor produtor ou por uso prolongado de corticoide como medicamento), o quadro é o espelho metabólico: hiperglicemia, gordura central, fraqueza muscular proximal por catabolismo proteico, pele fina e imunossupressão. Nesse caso, se a fonte é externa, o ACTH está *baixo* — o freio está sendo pisado por um hormônio que não veio da suprarrenal.])

Fecha o quadro um problema contemporâneo que só existe por causa de tudo o que foi dito: se a resposta hormonal depende do encaixe de uma forma num receptor, então qualquer molécula com forma parecida pode se meter no meio. É o que fazem os *disruptores endócrinos* — compostos ambientais, muitos deles derivados de plásticos e pesticidas, que ou imitam o hormônio ativando o receptor na hora errada, ou ocupam o receptor sem ativá-lo e bloqueiam o hormônio verdadeiro. Como são lipossolúveis, acumulam-se no tecido adiposo e agem em concentrações comparáveis às dos próprios hormônios.

#figura-nebli("/figuras/bioq-26-acao-hormonal/slide-55.png",
  largura: 50%,
  legenda: [À esquerda, o hormônio normal e sua resposta. No meio, o mimético ocupa o receptor e dispara resposta fora de hora. À direita, o bloqueador ocupa e não dispara — o hormônio verdadeiro não encontra vaga.])

#conclusao-box[
  Um princípio unificador percorreu as três PARTES: *a informação hormonal só existe como mudança de forma de proteínas em série*. O hormônio não faz nada por si — ele encaixa, o receptor torce, e essa torção é convertida em atividade enzimática alterada. O mecanismo nuclear que sustenta tudo é a divisão em duas rotas, e ela vem inteira da solubilidade da molécula: o hidrossolúvel para na membrana, gera segundo mensageiro e modifica covalentemente enzimas que já existem — segundos a minutos, com amplificação de até cem milhões de vezes na cascata do AMPc; o lipossolúvel entra, encontra receptor nuclear e muda quantas enzimas existem — horas a dias, com efeito que persiste enquanto a proteína nova durar. Insulina, glucagon e adrenalina são a primeira rota em ação sobre glicogênio, glicose e gordura; tireoidianos e cortisol são a segunda, definindo o patamar em que o metabolismo opera. A clínica retomada mostra que cada elo é um ponto de falha nomeável: fechar o canal de potássio da célula beta com sulfonilureia força a secreção de insulina; mantê-lo aberto trava a secreção no insulinoma; perder o córtex da suprarrenal solta o freio sobre o ACTH e escurece a pele; converter T4 em T3 no tecido-alvo decide quanta ação hormonal cada órgão recebe. Daqui em diante, a integração metabólica entre jejum e alimentação deixa de ser lista de vias e passa a ser uma disputa entre dois recados químicos sobre as mesmas enzimas — e quem já sabe qual receptor cada hormônio usa consegue prever, sem decorar, o que acontece com o glicogênio, com a gordura e com a glicemia em cada estado.
]
