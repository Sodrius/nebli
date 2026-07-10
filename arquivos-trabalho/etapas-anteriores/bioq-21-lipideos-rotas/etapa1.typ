#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Toda vez que você fica horas sem comer, dorme a noite inteira ou faz um exercício longo, é a gordura estocada que sustenta o corpo funcionando. Este resumo segue o caminho completo dessa gordura: como ela sai do estoque, como é quebrada dentro da mitocôndria para virar energia, quanto de #sigla("ATP", [adenosina trifosfato — a moeda de energia que a célula gasta no dia a dia]) ela realmente rende, e — quando há fartura — como o corpo faz o caminho inverso e fabrica gordura nova. No fim, o que amarra tudo é uma única ideia: o corpo nunca queima e constrói gordura ao mesmo tempo. Entender o interruptor que escolhe entre as duas direções é entender o metabolismo de lipídeos.
]

#parte-title("PARTE I — Da gordura estocada ao acetil-CoA: a β-oxidação", primeira: true)

#subtopico("1.1 — Por que o corpo guarda energia como gordura, e não como açúcar")

Guardar energia como gordura não é um acaso da evolução: é a solução mais eficiente que o corpo tem para o problema de carregar muito combustível sem carregar muito peso. A gordura armazena mais que o dobro de energia por grama que o carboidrato — a oxidação completa de um grama de lipídeo libera cerca de 2,5 vezes mais energia que a de um grama de açúcar. Só isso já seria uma vantagem, mas há um problema escondido que torna a diferença ainda maior.

O carboidrato é uma molécula polar: ele faz pontes de hidrogênio com a água e, por isso, é guardado sempre encharcado. Cada grama de glicogênio carrega junto cerca de três gramas de água. A gordura, ao contrário, é apolar e praticamente anidra — guarda-se "seca". Quando você soma o peso da água, a conta fica drástica: os aproximadamente 15 kg de #termo-nota[triacilglicerol][a forma de estoque da gordura: três ácidos graxos presos a uma molécula de glicerol] que um adulto carrega equivalem, em energia, a cerca de 37,5 kg de carboidrato — que, hidratado, pesaria mais de 100 kg. Um corpo que estocasse sua reserva energética na forma de açúcar seria pesado demais para se mover.

#mini-resumo[Gordura rende mais energia por grama *e* é guardada sem água. Por isso ela é o tanque de longo prazo do corpo; o açúcar é só o caixa rápido.]

Essa gordura fica guardada no #sigla("TAG", [triacilglicerol]) dentro do tecido adiposo, organizada em gotículas dentro dos adipócitos. Para virar energia útil em outro tecido — o músculo, por exemplo — ela precisa primeiro ser desmontada e enviada pelo sangue. É por aí que começa a história.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-04.png",
  largura: 55%,
  legenda: [O tecido adiposo guarda os ácidos graxos esterificados ao glicerol, na forma de triacilgliceróis — o tanque de longo prazo do corpo.])

#subtopico("1.2 — Mobilização: como o adipócito libera o ácido graxo no sangue")

Quando o nível de açúcar no sangue cai — no jejum, no exercício prolongado, sob estresse — o corpo precisa abrir o estoque de gordura. Quem dá a ordem são dois hormônios: o glucagon (liberado quando a glicemia cai) e a adrenalina (liberada no esforço e no estresse). Ambos chegam ao adipócito e disparam dentro dele um segundo mensageiro, o #sigla("AMPc", [AMP cíclico — segundo mensageiro que transmite o sinal hormonal para dentro da célula]), que ativa uma enzima central, a #sigla("PKA", [proteína-quinase A — adiciona fosfato a outras enzimas, ligando ou desligando-as]).

A PKA então fosforila e ativa a #termo-nota[lipase hormônio-sensível][enzima do adipócito que quebra o triacilglicerol em resposta a hormônios; abreviada HSL] — a #sigla("HSL", [lipase hormônio-sensível]) — que, junto com a lipase de triacilglicerol do adipócito (a #sigla("ATGL", [adipose triglyceride lipase — dá o primeiro corte no triacilglicerol estocado])), corta o triacilglicerol e libera os ácidos graxos. O nome "hormônio-sensível" diz exatamente o que importa: essa enzima só trabalha quando um hormônio mandou, e é por isso que a quebra do estoque é um processo controlado, não um vazamento contínuo.

A quebra do triacilglicerol gera dois produtos com destinos diferentes. Os ácidos graxos caem no sangue, onde viajam grudados à albumina até os tecidos que vão queimá-los. O glicerol, por sua vez, não serve de combustível ali mesmo: o adipócito quase não tem a enzima que o reaproveita (a glicerol-quinase). O glicerol segue pelo sangue até o fígado, onde entra na gliconeogênese ou na glicólise depois de virar gliceraldeído-3-fosfato. Vale guardar esse detalhe — ele volta na PARTE III, quando perguntarmos de onde sai a glicose no jejum.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-06.png",
  largura: 60%,
  legenda: [Glucagon e adrenalina ativam a lipase hormônio-sensível, que libera os ácidos graxos do estoque. A mobilização é uma decisão hormonal, não um vazamento.])

#subtopico("1.3 — A entrada na mitocôndria: ativação e a lançadeira da carnitina")

O ácido graxo chegou ao tecido-alvo, mas ainda não pode ser queimado: a queima acontece dentro da matriz mitocondrial, e a membrana interna da mitocôndria é uma barreira que o ácido graxo não atravessa por conta própria. Antes de pensar em transporte, porém, há um passo obrigatório de preparação — a ativação.

Ativar significa prender o ácido graxo a uma molécula de #sigla("CoA", [coenzima A — alça que "segura" grupos acila e os carrega de uma reação a outra]), formando o #termo-nota[acil-CoA][ácido graxo ativado, ligado à coenzima A; é a forma "pronta para reagir"]. Essa ligação custa energia, e aqui mora uma das contas mais cobradas do tema. A reação consome um ATP, mas de um jeito especial: o ATP não vira #sigla("ADP", [adenosina difosfato]) + #sigla("Pi", [fosfato inorgânico]), e sim #sigla("AMP", [adenosina monofosfato]) + #sigla("PPi", [pirofosfato — dois fosfatos ligados]). Em seguida, uma enzima chamada pirofosfatase hidrolisa o PPi em dois Pi separados. Quebrar o ATP até AMP e ainda desfazer o pirofosfato equivale, em energia, a gastar *duas* ligações de alta energia — ou seja, dois ATP. Esse "−2" reaparece lá na frente, na hora de fechar o saldo.

#mini-resumo[Ativar o ácido graxo custa o equivalente a 2 ATP, porque o ATP é quebrado até AMP e o pirofosfato ainda é desfeito. Guarde esse 2 — ele é o desconto do saldo final.]

Resolvida a ativação, falta o transporte. O acil-CoA de cadeia longa não passa pela membrana interna, então a célula usa uma lançadeira: o grupo acila é transferido da CoA para a #termo-nota[carnitina][molécula transportadora que "embarca" o grupo acila para dentro da mitocôndria], formando acilcarnitina. Essa troca é feita por uma enzima na face externa, a #sigla("CPT-1", [carnitina palmitoiltransferase 1 — coloca o acila na carnitina, na entrada da mitocôndria]); a acilcarnitina atravessa; e do lado de dentro a #sigla("CPT-2", [carnitina palmitoiltransferase 2 — devolve o acila à CoA, já dentro da matriz]) devolve o acila a uma CoA da matriz. Pense na carnitina como a balsa que leva o passageiro até a outra margem; a CoA é o carro que fica em cada lado.

Guarde um detalhe que será decisivo na PARTE III: a CPT-1, a porta de entrada, é inibida pelo malonil-CoA. Ou seja, a própria célula tem um cadeado na entrada da queima — e quem fecha esse cadeado é uma molécula que só existe quando o corpo está *fabricando* gordura. Esse é o primeiro fio da regulação recíproca.

Esse arranjo também explica um fato clínico aparentemente curioso: a hemácia e o tecido nervoso praticamente não oxidam ácidos graxos. A hemácia não tem mitocôndria nenhuma — sem matriz, não há β-oxidação possível. O cérebro tem mitocôndrias, mas os ácidos graxos atravessam mal a barreira hematoencefálica; por isso o neurônio depende de glicose e, no jejum, dos corpos cetônicos que veremos adiante.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-13.png",
  largura: 70%,
  legenda: [A lançadeira da carnitina. O acil-CoA não atravessa a membrana interna: a CPT-1 embarca o acila na carnitina, ele cruza, e a CPT-2 o devolve à CoA na matriz. A CPT-1 é inibida pelo malonil-CoA — a porta da queima que a síntese fecha.])

#subtopico("1.4 — A β-oxidação: cortar o ácido graxo de dois em dois carbonos")

Já dentro da matriz, o acil-CoA entra no processo que dá nome a esta parte. A #termo-nota[β-oxidação][via que encurta o ácido graxo removendo 2 carbonos por volta, na forma de acetil-CoA; também chamada ciclo de Lynen] — também chamada ciclo de Lynen — é uma sequência de quatro reações que se repete em ciclos. Cada volta arranca dois carbonos da ponta do ácido graxo e os entrega como #sigla("acetil-CoA", [unidade de dois carbonos ligada à CoA; é o combustível que entra no ciclo de Krebs]), deixando o ácido graxo dois carbonos mais curto para a volta seguinte.

A lógica das quatro reações é sempre a mesma e vale entender o porquê de cada uma, porque a ordem exata reaparece — espelhada — na síntese. O alvo é o carbono β (o segundo a contar da carbonila): a via precisa transformá-lo num ponto de corte. Primeiro vem a *desidrogenação*: remove-se um par de hidrogênios, criando uma dupla ligação; esses elétrons são recolhidos pelo #sigla("FAD", [flavina adenina dinucleotídeo — coenzima que recebe elétrons]), que vira #sigla("FADH₂", [forma reduzida do FAD, carregada de elétrons para a cadeia respiratória]). Depois vem a *hidratação*: água se adiciona à dupla ligação, colocando uma hidroxila no carbono β. Em seguida, a *oxidação* dessa hidroxila a cetona transfere outro par de elétrons, agora para o #sigla("NAD⁺", [nicotinamida adenina dinucleotídeo — coenzima que recebe elétrons]), formando #sigla("NADH", [forma reduzida do NAD⁺, carregada de elétrons para a cadeia respiratória]). Por fim, a *tiólise*: uma nova CoA entra e corta a molécula no carbono β, soltando um acetil-CoA e devolvendo um acil-CoA com dois carbonos a menos, pronto para recomeçar.

#mini-resumo[Cada volta da β-oxidação rende 1 FADH₂, 1 NADH e 1 acetil-CoA, e devolve o ácido graxo encurtado em 2 carbonos. Desidrogenação → hidratação → oxidação → tiólise.]

Repare que a β-oxidação, sozinha, não fabrica ATP. O que ela produz são *transportadores de elétrons carregados* (FADH₂ e NADH) e *combustível para o Krebs* (acetil-CoA). O ATP de verdade só aparece quando esses elétrons chegam à cadeia respiratória — e é por isso que a β-oxidação não funciona sem oxigênio, um ponto que merece cuidado.

#atencao-box("A β-oxidação NÃO é anaeróbia", [
A tentação é dizer que a β-oxidação dispensa oxigênio "porque o O₂ não aparece nas quatro reações". O erro é fatal para o raciocínio: cada volta gera FADH₂ e NADH, e a via só continua se essas coenzimas forem *reoxidadas* de volta a FAD e NAD⁺. Quem as reoxida é a cadeia respiratória, que entrega os elétrons ao oxigênio no final. Sem O₂, o FAD e o NAD⁺ não se regeneram, a β-oxidação trava na primeira reação que precisa deles — e é por isso que a queima de gordura é estritamente aeróbia.
])

Nem todo ácido graxo é tão regular. Os de cadeia ímpar terminam a última volta com um fragmento de três carbonos, o #termo-nota[propionil-CoA][produto de 3 carbonos da β-oxidação de ácidos graxos de cadeia ímpar; pode render glicose], em vez de outro acetil-CoA — e esse propionil-CoA, depois de algumas reações, pode alimentar a gliconeogênese (é a única parte de um ácido graxo que vira glicose). Os ácidos graxos insaturados, que já trazem duplas ligações, precisam de uma ou duas enzimas auxiliares para acertar a posição dessas ligações antes de seguir o caminho normal. São exceções que confirmam a regra: o esqueleto da via é sempre o corte de dois em dois carbonos.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-15.png",
  largura: 75%,
  legenda: [As quatro reações da β-oxidação (ciclo de Lynen): desidrogenação (FADH₂), hidratação, oxidação (NADH) e tiólise, que solta o acetil-CoA. A cada volta o ácido graxo encurta em dois carbonos.])

#parte-title("PARTE II — A conta da energia e o destino do acetil-CoA")

#subtopico("2.1 — Quanto ATP rende oxidar um palmitato (16 carbonos)")

Agora vamos fazer a conta que dá sentido a tudo: quanto de ATP rende oxidar completamente um ácido graxo. Usaremos o palmitato, de 16 carbonos, porque é o exemplo clássico — e porque, ao fazer a conta em etapas, o procedimento serve para qualquer ácido graxo de cadeia par. O objetivo é claro: somar todos os transportadores de elétrons produzidos, converter em ATP e descontar o que foi gasto na ativação.

*Primeira etapa — quantas voltas da β-oxidação?* Um cuidado importante: o número de voltas não é igual ao número de carbonos dividido por dois. A última volta parte de um fragmento de quatro carbonos e o corta em *dois* acetil-CoA de uma só vez. Por isso, um ácido graxo de 16 carbonos dá $16/2 - 1 = 7$ voltas, e essas 7 voltas produzem 8 acetil-CoA. Como cada volta rende 1 NADH e 1 FADH₂, são 7 voltas × (1 NADH + 1 FADH₂) = 7 NADH e 7 FADH₂ vindos da β-oxidação.

*Segunda etapa — o que os 8 acetil-CoA rendem no ciclo de Krebs?* Cada acetil-CoA que entra no ciclo de Krebs rende 3 NADH, 1 FADH₂ e 1 #sigla("GTP", [guanosina trifosfato — equivale a 1 ATP]). Multiplicando por 8: $8 times 3 = 24$ NADH, $8 times 1 = 8$ FADH₂ e 8 GTP.

*Terceira etapa — somar os transportadores.* Juntando a β-oxidação e o Krebs: $7 + 24 = 31$ NADH no total, $7 + 8 = 15$ FADH₂ no total, e 8 GTP. Vale organizar essa soma numa tabela, porque ela cruza duas dimensões — a fonte (β-oxidação ou Krebs) e o tipo de transportador:

#figure(
  table(
    columns: (auto, auto, auto, auto),
    align: (left, center, center, center),
    stroke: 0.5pt + gray-border,
    table.header(
      [*Fonte*], [*NADH*], [*FADH₂*], [*GTP*],
    ),
    [β-oxidação (7 voltas)], [7], [7], [—],
    [Ciclo de Krebs (8 acetil-CoA)], [24], [8], [8],
    [*Total*], [*31*], [*15*], [*8*],
  ),
  caption: [Os transportadores de elétrons e o GTP produzidos na oxidação completa do palmitato, antes de converter em ATP.],
)

*Quarta etapa — converter em ATP pela fosforilação oxidativa.* Aqui usamos os valores do nosso material: cada NADH rende 3 ATP e cada FADH₂ rende 2 ATP na cadeia respiratória; cada GTP equivale a 1 ATP. Então: $31 times 3 = 93$ ATP vindos dos NADH; $15 times 2 = 30$ ATP vindos dos FADH₂; e 8 ATP dos GTP. Somando: $93 + 30 + 8 = 131$ ATP brutos.

*Quinta etapa — descontar a ativação.* Lembre do "−2" da PARTE I: ativar o ácido graxo custou o equivalente a 2 ATP (ATP → AMP + PPi, e o PPi ainda foi desfeito). Então o saldo líquido é $131 - 2 = 129$ ATP por palmitato.

Lido em palavras: oxidar um único ácido graxo de 16 carbonos rende ao corpo cerca de 129 moléculas de ATP líquidas. É um número enorme — e é exatamente por isso que a gordura é o combustível de longo prazo. Compare com a glicose, e a diferença salta aos olhos, como faremos no próximo subtópico.

#confusao-prevista(
  titulo: "131 ou 106? Por que os livros divergem",
  aluno_acha: [aluno acha que existe um único valor "certo" para o saldo de ATP],
  mecanismo: [o número depende da convenção de rendimento da cadeia respiratória. O material da disciplina usa os valores clássicos (1 NADH = 3 ATP, 1 FADH₂ = 2 ATP), que dão 131 brutos / 129 líquidos. Livros mais recentes usam medições refinadas (1 NADH ≈ 2,5 ATP, 1 FADH₂ ≈ 1,5 ATP), que dão cerca de 106 líquidos. Não é contradição: é a mesma conta com uma constante diferente. Use os valores do seu material e saiba justificar a divergência.],
)

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-21.png",
  largura: 65%,
  legenda: [O fechamento da conta do palmitato: 31 NADH, 15 FADH₂ e 8 GTP convertem-se em 131 ATP brutos; descontada a ativação, sobram 129 ATP líquidos.])

#subtopico("2.2 — Por que a gordura rende muito mais que a glicose")

Para sentir o peso desse 129, vale refazer a mesma conta para a glicose. A oxidação completa de uma glicose rende, pelos mesmos valores clássicos, cerca de 38 ATP: a glicólise entrega 2 ATP e 2 NADH; a formação de acetil-CoA, mais 2 NADH; e os 2 acetil-CoA no Krebs, 6 NADH, 2 FADH₂ e 2 GTP — tudo convertido pela cadeia respiratória. Note que a glicose, com 6 carbonos, rende cerca de 38 ATP, enquanto o palmitato, com 16 carbonos, rende 129.

A diferença não é só o tamanho da molécula. O segredo está no estado dos carbonos: os do ácido graxo são quase todos cadeias —CH₂— altamente reduzidas, ricas em elétrons para entregar à cadeia respiratória; os da glicose já carregam vários oxigênios, ou seja, já estão parcialmente oxidados e têm menos elétrons a oferecer. Mais elétrons reduzidos por carbono significam mais NADH e FADH₂, e portanto mais ATP. É a mesma razão pela qual a gordura rende mais energia por grama: ela parte de um estado químico mais "carregado".

#mini-resumo[A gordura rende mais não só por ser maior, mas porque seus carbonos estão mais reduzidos — há mais elétrons por carbono para a cadeia respiratória transformar em ATP.]

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-29.png",
  largura: 70%,
  legenda: [Mapa do destino do ácido graxo: a lipólise libera ácido graxo e glicerol; a β-oxidação gera acetil-CoA, que segue para o ciclo de Krebs — ou, em desequilíbrio, para os corpos cetônicos.])

#subtopico("2.3 — Quando o acetil-CoA não cabe no Krebs: os corpos cetônicos")

Toda a conta anterior pressupõe que o acetil-CoA da β-oxidação entra tranquilamente no ciclo de Krebs. Mas isso depende de uma condição que costuma passar despercebida: para o acetil-CoA entrar no ciclo, ele precisa se condensar com o oxaloacetato, a molécula que o recebe na primeira reação do Krebs. E em certas situações o oxaloacetato simplesmente não está disponível.

É o que ocorre no jejum prolongado e no diabetes tipo 1. Nessas condições, o corpo está desesperado por glicose, e o oxaloacetato é desviado da mitocôndria para a gliconeogênese — a fabricação de glicose nova. Sem oxaloacetato para recebê-lo, o acetil-CoA produzido em massa pela β-oxidação se acumula. O fígado, então, dá a esse excesso um destino alternativo: junta as unidades de acetil-CoA e forma os #termo-nota[corpos cetônicos][acetoacetato e β-hidroxibutirato: combustíveis hidrossolúveis feitos no fígado a partir do excesso de acetil-CoA] — o acetoacetato e o β-hidroxibutirato.

Longe de serem lixo metabólico, os corpos cetônicos são um combustível inteligente: são hidrossolúveis (viajam no sangue sem precisar de albumina) e atravessam bem a barreira hematoencefálica. No jejum prolongado, eles se tornam a principal fonte de energia do cérebro, poupando glicose. Há um detalhe elegante: o fígado *fabrica* corpos cetônicos mas não os *consome*, porque lhe falta a enzima que os reativa — assim, ele produz exclusivamente para exportar aos outros tecidos.

O problema aparece quando a produção dispara sem freio, como no diabetes tipo 1 descompensado. O acetoacetato e o β-hidroxibutirato são ácidos; em grande quantidade, baixam o pH do sangue e instalam a #termo-nota[cetoacidose][queda perigosa do pH do sangue pelo acúmulo de corpos cetônicos ácidos, típica do diabetes tipo 1 descompensado]. O organismo tenta compensar eliminando esses ácidos na urina e produzindo amônia para neutralizá-los, mas a reserva alcalina se esgota — e a cetoacidose diabética é uma emergência médica real.

#clinica-box("Cetoacidose diabética", [
No diabetes tipo 1 sem insulina, as células não captam glicose e "leem" o corpo como se estivesse em jejum extremo: a lipólise dispara, a β-oxidação inunda o fígado de acetil-CoA e a produção de corpos cetônicos sai de controle. O resultado é a tríade clássica — hiperglicemia (glicose alta no sangue que não entra nas células), cetonemia (corpos cetônicos altos) e acidose (pH baixo). O paciente respira fundo e rápido (respiração de Kussmaul) tentando expelir CO₂ para corrigir o pH, e o hálito tem cheiro adocicado de acetona. É a demonstração clínica de que cetose fisiológica e cetoacidose descompensada são pontos diferentes da mesma escala.
])

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-31.png",
  largura: 60%,
  legenda: [No jejum e no diabetes, o oxaloacetato vai para a gliconeogênese e falta para receber o acetil-CoA, que é desviado para a formação de corpos cetônicos.])

#parte-title("PARTE III — Construir em vez de queimar: síntese e regulação")

#subtopico("3.1 — Onde e quando o corpo fabrica ácido graxo")

Até aqui o corpo só desmontou gordura. Mas quando há fartura — uma refeição rica, excesso de calorias de carboidrato ou proteína — o fígado e o tecido adiposo fazem o caminho oposto: pegam o acetil-CoA que sobra e montam ácidos graxos novos, que serão guardados como triacilglicerol. Esse é o sinal da abundância, e é comandado pela insulina, o hormônio do "tem comida sobrando".

Antes de entrar no mecanismo, vale fixar duas diferenças de cenário que separam a síntese da degradação, porque confundi-las é o erro mais comum do tema. A β-oxidação acontece na *matriz mitocondrial*; a síntese acontece no *citosol*. A β-oxidação usa FAD e NAD⁺ para *receber* elétrons; a síntese usa #sigla("NADPH", [forma reduzida do NADP⁺; doa elétrons nas reações de biossíntese]) para *doar* elétrons. São processos em compartimentos diferentes, com coenzimas diferentes — espelhados na lógica, mas não idênticos.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-10.png",
  largura: 50%,
  legenda: [Degradação e síntese de ácidos graxos ocorrem em compartimentos diferentes: a β-oxidação na matriz mitocondrial, a síntese no citosol.])

#subtopico("3.2 — A lançadeira do citrato e o passo comprometido (malonil-CoA)")

A síntese começa com um obstáculo logístico parecido com o da carnitina, só que invertido. O material de construção é o acetil-CoA, que é produzido *dentro* da mitocôndria — mas a síntese acontece *no citosol*, e a membrana mitocondrial é impermeável ao acetil-CoA. Como tirá-lo de lá?

A solução é a lançadeira do citrato. Dentro da mitocôndria, o acetil-CoA se condensa com o oxaloacetato formando citrato (a mesma primeira reação do Krebs). Quando há fartura de energia, o citrato se acumula e sai para o citosol, onde a enzima citrato-liase o recliva de volta em acetil-CoA e oxaloacetato. O acetil-CoA fica disponível no citosol para a síntese; o oxaloacetato retorna, e nesse retorno a enzima málica gera NADPH — parte do poder redutor que a síntese vai precisar.

#mini-resumo[O acetil-CoA não atravessa a membrana sozinho: ele sai da mitocôndria disfarçado de citrato e é recuperado no citosol pela citrato-liase. Citrato alto = sinal de fartura = "pode construir".]

Com o acetil-CoA no citosol, vem o passo que decide tudo. A enzima #termo-nota[acetil-CoA carboxilase][enzima que adiciona CO₂ ao acetil-CoA formando malonil-CoA; é o passo regulado e comprometido da síntese] (a #sigla("ACC", [acetil-CoA carboxilase])) adiciona um CO₂ ao acetil-CoA — usando biotina e gastando ATP — e forma o #termo-nota[malonil-CoA][unidade ativada de 3 carbonos que a sintase usa como doadora; também inibe a CPT-1, travando a β-oxidação]. Esse é o passo comprometido da via: uma vez formado o malonil-CoA, o destino é a síntese de ácido graxo. Por ser o ponto de decisão, é também o ponto mais regulado — e é aqui que o segundo fio da regulação recíproca aparece.

Lembre da PARTE I: o malonil-CoA inibe a CPT-1, a porta de entrada da β-oxidação. Agora a lógica fecha. Quando o corpo está construindo gordura, ele produz malonil-CoA; o malonil-CoA, além de servir de tijolo, fecha a porta da queima. Assim a célula garante que não está desmontando e montando ácido graxo ao mesmo tempo — o que seria um ciclo fútil, gastando ATP sem resultado nenhum.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-43.png",
  largura: 65%,
  legenda: [A lançadeira do citrato: o acetil-CoA sai da mitocôndria como citrato e é recuperado no citosol, onde alimenta a síntese. O oxaloacetato retorna, gerando NADPH no caminho.])

#subtopico("3.3 — A sintase de ácidos graxos e a montagem do palmitato")

Montados os tijolos, a obra é tocada por uma única máquina: a #termo-nota[sintase de ácidos graxos][complexo multienzimático que monta o palmitato; abreviada FAS] — a #sigla("FAS", [fatty acid synthase — complexo que reúne todas as enzimas da síntese numa só estrutura]). É um complexo que reúne todas as enzimas da via numa estrutura só, com um braço móvel — a proteína carreadora de acila, ou #sigla("ACP", [acyl carrier protein — o "braço" que segura a cadeia em crescimento e a passa de enzima a enzima]) — que segura a cadeia em crescimento e a leva de uma reação à seguinte, como numa linha de montagem.

A cada ciclo, a FAS adiciona dois carbonos à cadeia. Quem doa esses dois carbonos é o malonil-CoA (que tem três carbonos, mas perde um como CO₂ na entrada — e é essa perda que torna a reação favorável). A sequência de quatro reações é o espelho da β-oxidação, mas invertida e com outras coenzimas: *condensação* (junta a unidade nova), *redução* (usa NADPH), *desidratação* (sai água) e nova *redução* (usa NADPH outra vez). O ciclo se repete até a cadeia chegar a 16 carbonos — o palmitato. Para alongar além disso ou criar duplas ligações, o corpo usa enzimas adicionais no retículo endoplasmático.

Vale colocar as duas vias lado a lado, porque a comparação cruza várias dimensões que se referenciam e é onde mora a confusão clássica:

#figure(
  table(
    columns: (auto, auto, auto),
    align: (left, left, left),
    stroke: 0.5pt + gray-border,
    table.header(
      [*Dimensão*], [*β-oxidação*], [*Síntese*],
    ),
    [Compartimento], [matriz mitocondrial], [citosol],
    [Direção], [remove 2C por volta], [adiciona 2C por volta],
    [Carreador], [coenzima A], [proteína ACP],
    [Coenzima redox], [FAD, NAD⁺ (recebem e⁻)], [NADPH (doa e⁻)],
    [Doador de 2C], [—], [malonil-CoA],
    [Hormônio que ativa], [glucagon, adrenalina], [insulina],
    [Ponto de controle], [CPT-1], [acetil-CoA carboxilase],
  ),
  caption: [β-oxidação e síntese são espelhadas na lógica, mas separadas em compartimento, carreador, coenzima e hormônio. Inverter a direção das reações de redox é o erro mais comum do tema.],
)

Por fim, o ácido graxo recém-sintetizado é esterificado a uma molécula de glicerol-3-fosfato para formar o triacilglicerol de estoque. O glicerol-3-fosfato vem da glicólise (a partir da di-hidroxiacetona-fosfato) no tecido adiposo, ou também do glicerol no fígado. Fecha-se o círculo: o que foi quebrado no início da PARTE I é remontado aqui, quando há fartura.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-49.png",
  largura: 70%,
  legenda: [O complexo da sintase de ácidos graxos (FAS): todas as enzimas da via reunidas numa estrutura, com o braço ACP carregando a cadeia de uma reação à seguinte até o palmitato.])

#subtopico("3.4 — A regulação recíproca: insulina liga uma via e desliga a outra")

Tudo o que vimos converge para uma única pergunta: como o corpo escolhe entre queimar e construir gordura, sem fazer as duas coisas ao mesmo tempo? A resposta é a regulação recíproca, comandada pelo par de hormônios opostos — insulina de um lado, glucagon e adrenalina do outro.

Quando há fartura, a *insulina* domina. Ela ativa a acetil-CoA carboxilase, que produz malonil-CoA. O malonil-CoA faz duas coisas de uma vez: serve de tijolo para a síntese *e* fecha a CPT-1, bloqueando a entrada de ácido graxo na mitocôndria. Resultado: a síntese liga e a β-oxidação desliga, ao mesmo tempo, por uma única molécula.

Quando há escassez, o *glucagon* (e a adrenalina) domina. Via AMPc e PKA, ele ativa a lipólise no adipócito e inibe a acetil-CoA carboxilase — derrubando o malonil-CoA. Sem malonil-CoA, a CPT-1 se abre e os ácidos graxos voltam a entrar na mitocôndria para serem queimados. Resultado: a β-oxidação liga e a síntese desliga.

#mini-resumo[Uma molécula é o interruptor central: o malonil-CoA. Insulina o produz (constrói e tranca a queima); glucagon o derruba (queima e destranca). É assim que o corpo nunca faz as duas vias ao mesmo tempo.]

Essa é também a chave de um ponto que volta de subtópicos anteriores: por que o ácido graxo de cadeia par não vira glicose. O acetil-CoA da β-oxidação não consegue gerar oxaloacetato líquido — a piruvato-desidrogenase é irreversível e os mamíferos não têm o ciclo do glioxalato. Por isso, no jejum, a gordura sustenta o corpo com energia e corpos cetônicos, mas quem repõe a glicose é o glicerol (do próprio triacilglicerol) e os aminoácidos, não o ácido graxo. Reconhecer esse limite é entender por que o jejum prolongado precisa quebrar músculo: a gordura, sozinha, não fabrica açúcar.

#figura-nebli("/figuras/bioq-21-lipideos-rotas/slide-87.png",
  largura: 65%,
  legenda: [Regulação recíproca: a insulina ativa a síntese (acetil-CoA carboxilase ↑, malonil-CoA ↑) e, pelo mesmo malonil-CoA, trava a β-oxidação. O glucagon faz o oposto.])

#conclusao-box[
Olhando o tema inteiro de cima, um único princípio organiza tudo: o corpo guarda gordura porque ela é o combustível mais denso e mais leve que existe, e gerencia esse estoque com um interruptor que nunca deixa queima e construção rodarem juntas. O *mecanismo nuclear* desse interruptor é o malonil-CoA — produzido pela insulina quando há fartura, ele constrói ácido graxo e simultaneamente tranca a CPT-1, a porta da queima; derrubado pelo glucagon quando há escassez, ele libera a β-oxidação. A *clínica* mostra o que acontece quando esse equilíbrio se rompe: no diabetes tipo 1, a falta de insulina faz o corpo queimar gordura sem freio, e o excesso de acetil-CoA vira corpos cetônicos em quantidade tóxica — a cetoacidose. E essa história *se conecta para frente*: a mesma escassez que aciona a β-oxidação também desvia o oxaloacetato para a gliconeogênese, o assunto que mostra de onde vem a glicose quando a comida acaba — e por que a gordura, sozinha, não dá conta de repô-la.
]
