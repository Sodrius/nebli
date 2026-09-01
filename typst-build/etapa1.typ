#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
O corpo humano gasta energia sem parar e come em blocos. Entre uma refeição e a seguinte há um intervalo em que nada entra, e mesmo assim o cérebro continua consumindo cerca de 120 gramas de glicose por dia e a hemácia não sabe usar outra coisa. O organismo resolve esse descompasso guardando quando sobra e desmontando o estoque quando falta — e faz isso sem nunca deixar a glicemia sair de uma faixa estreita.

Esta aula é sobre o interruptor que decide de que lado o metabolismo está trabalhando. Três movimentos. Primeiro o *período absortivo*, as horas depois da refeição em que o fígado sequestra o excesso e o converte em glicogênio e gordura. Depois o *período pós-absortivo*, quando o sinal se inverte e o mesmo fígado passa a devolver glicose ao sangue — primeiro do estoque, depois fabricando-a do zero. E por fim o que acontece quando o intervalo se estica em *jejum prolongado*, e quando o interruptor quebra: no diabetes, o corpo executa o programa do jejum em cima de um sangue cheio de glicose.

O fio que costura tudo é sempre o mesmo, e vale guardá-lo desde já: a célula-alvo não lê a glicemia, lê a *razão insulina/glucagon*. Toda a coreografia que vem a seguir é consequência de qual dos dois hormônios está ganhando.
]

#parte-title("PARTE I — O estado alimentado: guardar o excesso", primeira: true)

#subtopico("1.1 A razão insulina/glucagon é o sinal — não a glicemia sozinha")

A refeição entra e a glicemia sobe de cerca de 4,5 para 7 ou 8 milimolares em pouco mais de meia hora. Esse é o estímulo aparente. O sinal que as células realmente obedecem, porém, é outro: a proporção entre dois hormônios pancreáticos de ação oposta. A célula beta da ilhota responde à glicose secretando *insulina*; a célula alfa, à falta dela, secretando *glucagon*. As duas curvas são espelhadas — a insulina dispara enquanto o glucagon cai — e é a razão entre elas, não a concentração absoluta de açúcar, que os tecidos-alvo interpretam.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-04.png",
  largura: 62%,
  legenda: [Repare que o pico de insulina e o vale de glucagon são simultâneos, e que as curvas se cruzam por volta de três a quatro horas — bem antes de a glicemia voltar ao basal. É o cruzamento hormonal, não a glicemia, que marca a virada para o pós-absortivo.])

Essa distinção tem consequência prática imediata. Uma glicemia de 5 milimolares significa coisas opostas conforme o momento: se está descendo do pico pós-refeição, a insulina ainda predomina e as vias de síntese seguem ligadas; se está subindo do fundo de um jejum, quem predomina é o glucagon, e as mesmas 5 milimolares acompanham glicogenólise ativa. *O número é o mesmo, a instrução celular é inversa.*

O sinal, aliás, chega antes do açúcar. Assim que o nutriente toca a mucosa intestinal, células enteroendócrinas liberam #termo-nota[incretinas][hormônios intestinais, sobretudo GLP-1 e GIP, liberados pela chegada de nutriente ao intestino; amplificam a secreção de insulina estimulada por glicose], que amplificam a resposta da célula beta à glicose que ainda vai chegar. O efeito é mensurável: uma carga de glicose tomada pela boca produz mais insulina do que a mesma carga infundida na veia, porque a via oral aciona esse aviso prévio e a venosa não. O pâncreas é informado da refeição pelo intestino, não apenas pelo sangue.

Um terceiro hormônio entra em outra escala de tempo. O *cortisol*, da suprarrenal, sobe nos intervalos longos entre refeições e no jejum prolongado, mas não age abrindo e fechando enzimas: age induzindo a transcrição de enzimas gliconeogênicas e favorecendo a proteólise muscular. Enquanto insulina e glucagon comutam vias em minutos, o cortisol reconfigura o parque enzimático em horas.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-07.png",
  largura: 58%,
  legenda: [Todas as setas do hepatócito apontam para dentro e para baixo: glicose-6-fosfato distribuída entre glicogênio, pentoses e triacilglicerol. O que a figura não mostra é que nenhuma delas é irreversível — cada uma tem uma enzima oposta esperando o sinal contrário.])

#mini-resumo[Razão insulina/glucagon alta = guardar; razão baixa = mobilizar. A glicemia é a causa do sinal, não o sinal.]

#subtopico("1.2 O fígado retém a glicose: glicoquinase e a translocação que muda tudo")

A intuição natural é que a insulina abre a porta da glicose no fígado, do mesmo modo que abre no músculo. Não é o que acontece, e o mecanismo real é mais interessante. O hepatócito capta glicose por um transportador chamado #sigla("GLUT2", [transportador de glicose tipo 2 — constitutivo, bidirecional e de alto Km, presente em fígado, célula beta, rim e intestino]), que é constitutivo e bidirecional: a glicose entra e sai a favor do gradiente, sem depender de hormônio nenhum. Depois de uma refeição, a glicose entra no fígado simplesmente porque há mais dela fora do que dentro. *O que a insulina controla não é a entrada — é o destino.*

Esse destino se decide numa única enzima. Para que a glicose fique, ela precisa ser fosforilada a glicose-6-fosfato, e o fosfato carregado negativamente é o que a impede de sair: nenhum GLUT transporta açúcar fosforilado. Fosforilar, aqui, é aprisionar. O fígado usa para isso a #termo-nota[glicoquinase][hexoquinase IV, isoforma do hepatócito e da célula beta — Km alto, não inibida por glicose-6-fosfato], e a comparação com a hexoquinase dos outros tecidos explica o desenho inteiro. A hexoquinase tem constante de Michaelis em torno de 0,1 milimolar: está saturada em qualquer glicemia fisiológica e é inibida pelo próprio produto. A glicoquinase tem Km próximo de 10 milimolares e não sofre inibição pelo produto. Cem vezes de diferença.

O aluno costuma ler Km alto como enzima de baixa qualidade. É o contrário: é especificação de projeto. Com Km alto, o fígado só trabalha a sério quando a glicose está em excesso — em glicemia normal, ele deixa o açúcar passar para o cérebro e a hemácia, que precisam mais. O fígado é o último a se servir, e é por isso que funciona como tampão.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-09.png",
  largura: 70%,
  legenda: [Os três pares circulados são os pontos irreversíveis da glicólise, cada um com sua enzima oposta da gliconeogênese ao lado. Guarde a geometria: é sobre esses três pares que todos os sinais desta aula vão agir.])

Falta o detalhe que o próprio material do professor destaca: a glicoquinase *transloca do núcleo para o citoplasma*. Ela não está sendo produzida naquele momento — já existe, sequestrada dentro do núcleo por uma proteína reguladora que a mantém inativa. A frutose-6-fosfato, alta no jejum, favorece esse sequestro; a glicose alta desfaz o complexo e libera a enzima para o citoplasma, onde há substrato. É liberação de um estoque pronto, não síntese nova — e é o que dá ao fígado uma resposta em minutos, sem esperar transcrição.

Uma vez fosforilada, a glicose-6-fosfato tem três saídas simultâneas, e a insulina abre as três: glicogênio, via das pentoses-fosfato e glicólise rumo à síntese de gordura. As duas primeiras aparecem nos próximos subtópicos; a terceira fecha esta PARTE.

#subtopico("1.3 Glicogênio: uma fosfatase liga a síntese e desliga a quebra ao mesmo tempo")

Imagine um interruptor de duas posições que comanda dois motores acoplados: girar para a esquerda liga o motor que enche o tanque e, pelo mesmo movimento, desliga o que esvazia. Não há como ligar os dois. O metabolismo do glicogênio é exatamente isso, e a peça que faz o papel do interruptor é uma fosfatase — a fosfoproteína #sigla("PP1", [fosfoproteína fosfatase 1 — remove grupos fosfato de enzimas do metabolismo do glicogênio]).

A cadeia começa no receptor de insulina, uma tirosina-quinase que se autofosforila e recruta proteínas adaptadoras até ativar a #sigla("PKB", [proteína quinase B, também chamada Akt — quinase central da via de sinalização da insulina]). A PKB ativa faz quatro coisas de uma vez, e vale seguir cada uma: fosforila a PP1 e a *ativa*; fosforila a #sigla("GSK-3", [glicogênio sintase quinase 3 — quinase que mantém a glicogênio sintase fosforilada e inativa]) e a *inativa*; fosforila e inativa a #sigla("PKA", [proteína quinase A — quinase dependente de cAMP, executora do sinal do glucagon]); e ativa a fosfodiesterase, que degrada o cAMP restante.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-08.png",
  largura: 66%,
  legenda: [Quatro ramos saindo da mesma PKB. Note que o mesmo grupo fosfato adicionado pela via chega a resultados opostos em cada alvo — ativa a PP1, inativa a GSK-3.])

Com a PP1 ativa e a GSK-3 fora do caminho, a fosfatase desfosforila os dois alvos finais: a *glicogênio sintase*, que fica ativa, e a *glicogênio fosforilase*, que fica inativa. Um único evento químico — a remoção do fosfato — comuta os dois lados na direção certa, e é aqui que mora a inversão mais destruidora do tema.

#atencao-box("Fosforilar não significa desligar", [O aluno sai da aula de sinalização com a regra silenciosa de que fosforilação inativa e desfosforilação ativa. Aqui essa regra quebra em cima da mesma cascata: a fosforilação *desliga* a glicogênio sintase e *liga* a glicogênio fosforilase. O fosfato não carrega polaridade nenhuma — quem tem polaridade é o sítio de cada enzima. A leitura correta é funcional, não química: no estado alimentado o conjunto está desfosforilado e o saldo é síntese; no jejum está fosforilado e o saldo é quebra. Sempre que aparecer uma enzima nova neste resumo, pergunte o que a fosforilação faz *naquela* enzima — nunca presuma.])

Há ainda um controle local, independente de hormônio, que o material do professor sinaliza: a própria glicose inibe a glicogênio fosforilase. O mecanismo é elegante e costuma ser mal contado. A glicose não compete pelo sítio catalítico: liga-se a um sítio alostérico da fosforilase ativa, desloca a enzima para a conformação tensa e, ao fazê-lo, *expõe* o resíduo fosforilado que estava escondido. Exposto, ele vira alvo fácil da PP1, que o remove. A glicose não desliga a enzima — ela entrega a enzima à fosfatase. O hepatócito que acabou de encher de açúcar para a degradação do próprio estoque antes mesmo de a insulina completar sua ação.

#subtopico("1.4 O excesso vira gordura: citrato, malonil-CoA e a porta que se fecha")

Encher o glicogênio hepático leva poucas horas e o depósito é pequeno — algo em torno de 100 gramas. O que sobra de glicose depois disso tem um destino de capacidade praticamente ilimitada: gordura. E o caminho até lá esbarra num obstáculo topológico que organiza todo o subtópico. A glicose vira piruvato no citosol, o piruvato entra na mitocôndria e vira acetil-#sigla("CoA", [coenzima A — transportadora de grupos acila em reações do metabolismo intermediário]), mas a síntese de ácido graxo acontece *no citosol* — e a membrana mitocondrial interna não tem transportador para acetil-CoA.

A solução é disfarçar o carbono. O acetil-CoA condensa com oxaloacetato formando citrato, e o citrato tem transportador. Já no citosol, a ATP-citrato liase o reclivava de volta em acetil-CoA e oxaloacetato, entregando o carbono onde ele é necessário. O mesmo citrato que serve de veículo funciona como sinal: ativa alostericamente a acetil-CoA carboxilase, a enzima que abre a síntese, e inibe a fosfofrutoquinase-1, avisando à glicólise que já há carbono suficiente rio abaixo. Substrato e mensagem na mesma molécula.

A acetil-CoA carboxilase converte acetil-CoA em *malonil-CoA*, e essa é a etapa comprometida da via — a partir dela, o carbono só vai para gordura. A insulina a ativa por desfosforilação; o cAMP e o #sigla("AMP", [adenosina monofosfato — sinal de carga energética baixa]) a inibem por fosforilação. Mas o malonil-CoA tem uma segunda função, e é ela que fecha a lógica do estado alimentado.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-15.png",
  largura: 72%,
  legenda: [Siga a seta vermelha que sai do malonil-CoA e cruza o desenho até o acil-CoA graxo do lado direito: é o mesmo produto da síntese fechando a entrada da degradação, num único traço.])

O malonil-CoA inibe a carnitina-palmitoil transferase I, a enzima que carrega o ácido graxo de cadeia longa para dentro da mitocôndria. Sem essa passagem, não há beta-oxidação. Ou seja: enquanto o fígado está fabricando ácido graxo, o produto da primeira etapa tranca a porta pela qual esse ácido graxo seria queimado. Síntese e degradação de lipídeo nunca correm ao mesmo tempo, e o mecanismo que garante isso é uma única molécula com duas funções.

Falta a moeda redutora. Construir ácido graxo consome #sigla("NADPH", [nicotinamida adenina dinucleotídeo fosfato reduzido — poder redutor das vias de síntese]), e não NADH. A fonte principal é a via das pentoses-fosfato, ligada pela mesma glicose-6-fosfato do subtópico anterior; mas há uma segunda fonte embutida na própria volta do citrato — o oxaloacetato liberado no citosol é reduzido a malato e descarboxilado pela enzima málica, reação que gera NADPH. O ciclo do citrato não só traz o carbono: paga parte do poder redutor necessário para montá-lo.

O produto final não fica no fígado. Com exceção do glicogênio, tudo o que o hepatócito sintetiza no período absortivo — triacilglicerol, fosfolipídeo, colesterol — é embalado com apoproteínas em #sigla("VLDL", [lipoproteína de densidade muito baixa — veículo de exportação do triacilglicerol hepático]) e exportado para o tecido adiposo. Fígado que retém esse triacilglicerol em vez de exportá-lo é fígado doente, e essa observação volta na PARTE III.

#mini-resumo[O que ficou de pé: citrato leva o carbono ao citosol e avisa que há excesso; malonil-CoA constrói a gordura e, ao mesmo tempo, fecha a porta da queima.]

#parte-title("PARTE II — O pós-absortivo: manter a glicemia")

#subtopico("2.1 A inversão do sinal: glucagon, cAMP e a trava dupla do glicogênio")

Costuma-se resumir o pós-absortivo como "a insulina caiu". A descrição está incompleta e a metade que falta é a que faz o sistema funcionar. Duas coisas acontecem em paralelo: a insulina cai, tirando o freio das vias de síntese, *e* o glucagon sobe, aplicando o acelerador das vias de mobilização. A razão entre os dois muda de lado, e é a mudança de lado — não a queda isolada de um deles — que inverte o metabolismo hepático.

O glucagon encontra seu receptor no hepatócito, e não no miócito: o músculo simplesmente não tem receptor de glucagon, o que já explica por que o estoque muscular não obedece ao mesmo comando. O receptor hepático é acoplado a proteína G, ativa a adenilato ciclase, e a ciclase converte #sigla("ATP", [adenosina trifosfato — moeda energética da célula]) em #sigla("cAMP", [monofosfato cíclico de adenosina — segundo mensageiro do sinal do glucagon]). O cAMP libera as subunidades catalíticas da PKA, e daí em diante a cascata é toda de fosforilação.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-24.png",
  largura: 68%,
  legenda: [Conte os degraus entre o receptor e o glicogênio: são quatro. Cada degrau multiplica o número de moléculas ativadas, e é por isso que poucos picomolares de glucagon esvaziam um depósito de gramas.])

Vale seguir a cadeia inteira uma vez, porque ela tem um degrau que o aluno costuma pular. A PKA *não* fosforila a glicogênio fosforilase diretamente. Ela fosforila a *fosforilase quinase*; a fosforilase quinase ativada é que fosforila a glicogênio fosforilase *b*, convertendo-a na forma *a*, ativa; e a fosforilase *a* então cliva o glicogênio, liberando glicose-1-fosfato. O degrau intermediário existe para amplificar: cada molécula de PKA ativa muitas fosforilase quinases, cada uma das quais ativa muitas fosforilases.

Ao mesmo tempo, e pela mesma PKA, a glicogênio sintase é fosforilada e desligada. É o interruptor de duas posições do subtópico 1.3 girando para o outro lado. E há uma segunda trava, mais fina, que fecha o sistema: *a PKA também fosforila o inibidor-1, e o inibidor-1 fosforilado bloqueia a PP1*. Sem esse detalhe a cascata seria inútil — a fosfatase que estava ativa no estado alimentado desfaria em seguida tudo o que o glucagon acabou de fazer. O glucagon liga a quebra e, no mesmo gesto, impede que ela seja desligada.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-22.png",
  largura: 60%,
  legenda: [Observe onde a curva verde cruza a vermelha, entre 16 e 24 horas: é o momento em que a gliconeogênese assume a manutenção da glicemia. A glicogenólise já vinha caindo muito antes de acabar.])

O estoque hepático de glicogênio não dura muito — algo entre 12 e 24 horas conforme a demanda. Por isso a gliconeogênese não espera o glicogênio acabar para começar: as duas curvas se sobrepõem, e a segunda já está subindo enquanto a primeira ainda decai. É essa sobreposição que evita qualquer degrau na glicemia, e é para ela que o próximo subtópico abre a porta.

#atencao-box("Glicogênio muscular não sustenta a glicemia", [O músculo guarda mais glicogênio em massa absoluta do que o fígado, e daí nasce a conclusão errada de que ele ajuda a manter o açúcar do sangue nos intervalos. Não ajuda, e o motivo é uma enzima ausente: o miócito não tem *glicose-6-fosfatase*. A glicose-1-fosfato liberada do glicogênio muscular vira glicose-6-fosfato e para aí — fosforilada, ela não atravessa a membrana e é obrigada a seguir pela glicólise dentro da própria fibra. O estoque muscular é combustível privado, para a contração daquele músculo. Quem tem a fosfatase, e portanto quem consegue devolver glicose livre ao sangue, é o fígado — e, no jejum prolongado, o córtex renal.])

#subtopico("2.2 Frutose-2,6-bifosfato: a enzima bifuncional que escolhe a direção")

Glicólise e gliconeogênese usam a mesma estrada em sentidos opostos, e se as duas rodassem juntas o resultado seria queimar ATP sem produzir nada. O organismo precisa, então, de um sinal que informe a direção — e ele o fabricou como uma molécula dedicada, que não participa de nenhuma das duas vias. Chama-se *frutose-2,6-bifosfato*, e existe apenas para dizer em que sentido o fluxo deve correr.

A confusão a desarmar antes de seguir é justamente essa: a frutose-2,6-bifosfato parece um intermediário da glicólise, já que a frutose-1,6-bifosfato é um. Não é. Ela é um beco sem saída deliberado — um sinal alostérico puro, produzido num ramo lateral, cuja única função é regular. O que ela faz é duplo e coerente: *ativa* a fosfofrutoquinase-1, empurrando a glicólise, e *inibe* a frutose-1,6-bifosfatase, travando a gliconeogênese. Uma molécula, dois alvos opostos, mesmo sentido de resultado.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-26.png",
  largura: 64%,
  legenda: [A mesma proteína aparece duas vezes na figura, em cima e embaixo, com um fosfato de diferença. Não são duas enzimas: é uma só, e o fosfato decide qual dos dois sítios trabalha.])

A peça que produz e destrói esse sinal é uma curiosidade bioquímica que vale entender bem, porque ela resolve o problema de coordenação de uma vez. A fosfofrutoquinase-2 e a frutose-2,6-bifosfatase são *dois sítios catalíticos da mesma cadeia polipeptídica* — uma enzima bifuncional. Uma única fosforilação, feita pela PKA, desliga o sítio quinase e liga o sítio fosfatase. Como as duas atividades moram na mesma proteína e respondem ao mesmo fosfato, é impossível que estejam ativas ao mesmo tempo.

Junte as peças. Glucagon alto no pós-absortivo, cAMP alto, PKA ativa, enzima bifuncional fosforilada: o sítio fosfatase trabalha, a frutose-2,6-bifosfato despenca, a fosfofrutoquinase-1 perde seu ativador e a frutose-1,6-bifosfatase perde seu inibidor. O fluxo líquido inverte para gliconeogênese. Depois da refeição, com a insulina ativando a fosfatase que remove aquele fosfato, tudo se passa ao contrário. *O ponto fino é que a concentração do sinal muda, não o efeito dele* — a frutose-2,6-bifosfato estimula glicólise em qualquer situação; no jejum ela apenas some.

Um detalhe que separa quem entendeu o princípio de quem decorou a regra: essa resposta à fosforilação é uma propriedade da isoforma hepática, não uma lei universal. A isoforma do músculo cardíaco responde na direção oposta, e por isso a mesma adrenalina que faz o fígado exportar glicose faz o coração acelerar a glicólise para queimá-la. O sinal é o mesmo; a leitura depende de quem lê.

#subtopico("2.3 Quem come o quê: a hierarquia de combustível entre tecidos")

O que a PARTE anterior mostrou dentro do hepatócito só faz sentido junto com uma decisão que acontece fora dele: com pouca insulina, nem todos os tecidos param de captar glicose — apenas alguns. Essa separação é o que permite ao organismo poupar açúcar sem matar de fome os órgãos que não sabem viver sem ele.

A diferença está na família de transportadores. O #sigla("GLUT4", [transportador de glicose tipo 4 — o único da família guardado em vesículas e recrutado à membrana pela insulina]), presente no músculo esquelético e no tecido adiposo, fica guardado em vesículas intracelulares e só vai para a membrana quando a insulina o manda ir. Sem insulina, ele volta para dentro e a captação despenca. Os outros membros da família são constitutivos: estão sempre na membrana e transportam conforme o gradiente, sem pedir permissão hormonal — é o caso do #sigla("GLUT1", [transportador de glicose tipo 1 — constitutivo, de baixo Km, na hemácia e no endotélio da barreira hematoencefálica]) da hemácia e do #sigla("GLUT3", [transportador de glicose tipo 3 — constitutivo, de baixo Km, característico do neurônio]) do neurônio.

#table(
  columns: (auto, auto, auto, auto),
  inset: 6pt,
  align: left,
  table.header([*Transportador*], [*Onde*], [*Km aproximado*], [*Depende de insulina*]),
  [GLUT1], [Hemácia, barreira hematoencefálica], [~1 mM], [Não],
  [GLUT2], [Fígado, célula beta, rim, intestino], [~15–20 mM], [Não],
  [GLUT3], [Neurônio], [~1 mM], [Não],
  [GLUT4], [Músculo esquelético, tecido adiposo], [~5 mM], [Sim],
)

A tabela explica a hierarquia inteira quando lida pela coluna do Km. Neurônio e hemácia têm transportadores de Km baixo: estão saturados em qualquer glicemia normal, de modo que a captação deles é praticamente constante e só cai em hipoglicemia franca. O GLUT2 hepático, com Km muito acima da glicemia fisiológica, nunca satura — transporta em proporção direta à concentração, nos dois sentidos, e funciona como sensor. Na célula beta é essa mesma propriedade que converte glicemia em taxa de secreção de insulina.

#confusao-prevista(
  titulo: "Transportador não é receptor",
  aluno_acha: [aluno trata GLUT e receptor de insulina como a mesma proteína, e diz que o tecido "tem receptor de glicose"],
  mecanismo: [o GLUT é um carreador passivo: move glicose a favor do gradiente, não gasta ATP e não sinaliza coisa alguma. O receptor de insulina é outra proteína, uma tirosina-quinase, que sinaliza mas não transporta uma única molécula de açúcar. A insulina não abre o GLUT4 — ela manda a vesícula que o contém fundir com a membrana. São dois objetos com funções que não se sobrepõem.],
)

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-27.png",
  largura: 62%,
  legenda: [A mão vermelha marca o único ramo que a falta de insulina interrompe: o tráfego da vesícula de GLUT4 até a membrana. Todo o resto da via segue funcionando.])

Duas restrições completam o quadro e voltam a ser decisivas na PARTE III. O ácido graxo de cadeia longa circula ligado à albumina e não atravessa a barreira hematoencefálica em quantidade útil — o cérebro, portanto, não pode simplesmente migrar para gordura. E a hemácia madura não tem mitocôndria: depende de glicólise anaeróbia e devolve lactato ao plasma, obrigatoriamente. São esses dois limites que forçam o fígado a fabricar glicose, e é o lactato da hemácia que vai reaparecer no ciclo de Cori.

#subtopico("2.4 A gordura paga a conta da glicose: beta-oxidação, PDK4 e piruvato carboxilase")

Pense num painel com duas lâmpadas ligadas ao mesmo sensor: quando o sensor detecta gordura queimando, a lâmpada da oxidação do piruvato apaga e a da gliconeogênese acende. O sensor, neste caso, é uma molécula só — o acetil-CoA vindo da beta-oxidação — e ela aciona as duas lâmpadas em sentidos opostos ao mesmo tempo.

A cadeia começa no adipócito. Com insulina baixa e glucagon alto, a PKA fosforila e *ativa* a lipase hormônio-sensível — mais um caso em que fosforilar liga —, disparando a #termo-nota[lipólise][hidrólise do triacilglicerol estocado no adipócito, liberando ácidos graxos livres e glicerol para o plasma]. Ácido graxo livre e glicerol entram na circulação; o ácido graxo vai para fígado e músculo, e o glicerol volta ao fígado como substrato gliconeogênico. No hepatócito, sem malonil-CoA para trancar a carnitina-palmitoil transferase I, o ácido graxo entra na mitocôndria e é degradado a acetil-CoA.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-30.png",
  largura: 74%,
  legenda: [Do lado esquerdo, a enzima verde ativa e a vermelha inativa diferem por um fosfato; do lado direito, o mesmo acetil-CoA que causou essa fosforilação empurra o piruvato para cima. Uma molécula, duas consequências opostas.])

Esse acetil-CoA acumulado faz duas coisas. Primeiro, inibe a piruvato desidrogenase, o complexo que converteria piruvato em acetil-CoA. A inibição vem por duas vias com tempos diferentes, e distinguir as duas é o degrau de profundidade deste subtópico: acetil-CoA e #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzido — carregador de elétrons e sinal de que há energia sobrando]) inibem o complexo *alostericamente*, em segundos, e também estimulam a quinase que o fosforila; em paralelo, o jejum prolongado *induz a transcrição* da isoforma #sigla("PDK4", [piruvato desidrogenase quinase 4 — isoforma hepática induzida no jejum, que mantém a piruvato desidrogenase fosforilada e inativa]) dessa quinase no fígado, o que leva horas e consolida o desligamento de forma duradoura. Resposta rápida e resposta lenta, para o mesmo fim.

Segundo, o acetil-CoA *ativa* alostericamente a piruvato carboxilase, que carboxila piruvato a oxaloacetato. Some as duas: com a porta da acetil-CoA fechada e a do oxaloacetato aberta, todo piruvato que chega ao fígado é desviado para a gliconeogênese. Não é desperdício de piruvato — é redirecionamento do mesmo carbono.

#atencao-box("Ácido graxo não vira glicose", [Esta é a inversão mais cara do tema, porque parece razoável: se a gordura sustenta o jejum e o fígado está fabricando glicose, é natural supor que o carbono da gordura esteja virando açúcar. Não está. A beta-oxidação de um ácido graxo de cadeia par produz apenas acetil-CoA, e no mamífero não existe via líquida de acetil-CoA para piruvato — os dois carbonos que entram no ciclo de Krebs saem como dois CO₂. O que a oxidação da gordura fornece à gliconeogênese é *ATP para pagá-la e sinal para autorizá-la*, não matéria-prima. O carbono da glicose nova vem de outro lugar: lactato, glicerol e aminoácido — e é exatamente por isso que o jejum longo consome músculo, assunto do próximo subtópico.])

#parte-title("PARTE III — Jejum prolongado e a sinalização quebrada")

#subtopico("3.1 O músculo entrega carbono: alanina, glutamina e o ciclo de Cori")

O subtópico anterior fechou com uma dívida: a gliconeogênese precisa de carbono, e a gordura não o fornece. Passadas as primeiras 24 horas, o glicogênio hepático acabou e restam três fontes reais — glicerol da lipólise, lactato dos tecidos glicolíticos e aminoácido do músculo. As duas primeiras apenas reciclam carbono que já era glicose; só a terceira traz carbono novo, e é por isso que o jejum longo custa massa muscular.

O músculo, porém, não despeja no sangue os vinte aminoácidos na proporção em que os degradou. Quase todo o nitrogênio sai empacotado em duas moléculas: *alanina* e *glutamina*. Os esqueletos de carbono dos demais aminoácidos são redistribuídos internamente até formar essas duas, que são então exportadas. A razão da escolha é mecanística. Amônia livre é neurotóxica e não pode circular; a transaminação transfere o grupo amino para piruvato, gerando alanina, ou para glutamato, gerando glutamina — dois carregadores atóxicos. E a alanina tem uma vantagem adicional: uma única transaminação no fígado a devolve a piruvato, pronto para a gliconeogênese.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-34.png",
  largura: 55%,
  legenda: [Siga as duas setas verticais em sentidos opostos: alanina descendo com nitrogênio, glicose subindo sem ele. O nitrogênio não faz o caminho de volta — sai como ureia, no canto inferior direito.])

O circuito tem nome — *ciclo alanina-glicose* — e um parente próximo, o *ciclo de Cori*, em que o músculo em anaerobiose e a hemácia devolvem lactato, o fígado o reconverte a glicose e a glicose volta. Os dois carregam o mesmo carbono na mesma direção; a diferença é que o da alanina traz nitrogênio junto e termina no ciclo da ureia.

Aqui entra uma conta que muda a compreensão do ciclo. O músculo, ao converter uma glicose em dois lactatos, ganha 2 ATP. O fígado, para refazer aquela glicose a partir dos dois lactatos, gasta 6 ATP. O saldo do organismo é negativo em 4 ATP por volta. *O ciclo de Cori não produz energia — ele transfere carga metabólica*, tirando do músculo em anaerobiose a obrigação de lidar com o lactato e passando-a ao fígado, que tem ácido graxo abundante para pagar a conta. É divisão de trabalho custeada pela gordura.

Um último órgão entra em cena quando o jejum passa de alguns dias, e ele costuma ficar de fora do desenho. O córtex renal também tem glicose-6-fosfatase e também faz gliconeogênese, usando preferencialmente glutamina — chegando a responder por uma fração substancial da produção total de glicose no jejum prolongado. E a mesma reação que consome glutamina libera amônio na urina, o que ajuda a excretar o excesso de ácido produzido pela cetose. O rim resolve dois problemas com uma via só, e essa observação prepara o próximo subtópico.

#subtopico("3.2 Corpos cetônicos: o combustível que poupa proteína")

Se a proteólise continuasse no ritmo dos primeiros dias, um adulto perderia cerca de 75 gramas de proteína por dia e não sobreviveria a algumas semanas de jejum. O que impede isso é uma mudança de combustível: por volta do terceiro dia, o organismo passa a fabricar em escala uma alternativa que o cérebro aceita, e o consumo de proteína cai para algo em torno de 20 gramas diários. A queda é o resultado, e vale entender o mecanismo que a produz.

O fígado está recebendo ácido graxo em excesso e oxidando-o rápido. O acetil-CoA gerado supera a capacidade do ciclo de Krebs de absorvê-lo — em parte porque o oxaloacetato disponível está sendo desviado para a gliconeogênese. Com acetil-CoA sobrando e oxaloacetato escasso, a mitocôndria hepática condensa as moléculas de acetil-CoA entre si: a #termo-nota[cetogênese][conversão hepática do excesso de acetil-CoA em acetoacetato e beta-hidroxibutirato, combustíveis hidrossolúveis exportáveis] passa por acetoacetil-CoA e #sigla("HMG-CoA", [beta-hidroxi-beta-metilglutaril-CoA — intermediário de seis carbonos da via de formação dos corpos cetônicos]) até liberar acetoacetato, parte do qual é reduzida a beta-hidroxibutirato.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-37.png",
  largura: 76%,
  legenda: [O painel rosa de cima é o fígado montando; o de baixo é o músculo desmontando. Compare as duas enzimas de entrada: elas não são as mesmas, e essa assimetria é o assunto do parágrafo seguinte.])

A vantagem do produto é física antes de ser química: acetoacetato e beta-hidroxibutirato são hidrossolúveis, circulam sem albumina e atravessam a barreira hematoencefálica em transportadores próprios — coisa que o ácido graxo de cadeia longa não faz. O organismo converteu gordura, que o cérebro não consegue usar, num derivado que ele consegue. A acetona, terceiro corpo cetônico, vem da descarboxilação espontânea do acetoacetato, não é aproveitada e sai pela respiração — daí o hálito característico de quem está em cetose intensa.

#confusao-prevista(
  titulo: "O fígado fabrica corpo cetônico e não o queima",
  aluno_acha: [aluno supõe que, produzindo o combustível, o fígado seja o primeiro a usá-lo],
  mecanismo: [o hepatócito não expressa a transferase que reativa acetoacetato a acetoacetil-CoA — a enzima existe em músculo, coração, rim e, com adaptação, no encéfalo, mas não no fígado. Essa ausência não é acidente: é ela que garante que toda a produção seja exportada, em vez de consumida na origem. O fígado sustenta o jejum queimando ácido graxo, e entrega o corpo cetônico inteiro para quem não pode queimar gordura.],
)

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-35.png",
  largura: 58%,
  legenda: [A glicose cai pouco, e é esse "pouco" que importa: a cetonemia sobe cerca de dez vezes justamente para que a glicemia possa cair tão devagar.])

O encéfalo não abandona a glicose por completo — permanece dependente dela para uma parte do consumo, o que mantém a gliconeogênese funcionando em ritmo reduzido. Mas, ao terem os corpos cetônicos cobrindo a maior fração da demanda, a necessidade de glicose nova despenca, e com ela a proteólise. *A cetogênese é, no fundo, um mecanismo de preservação de músculo* — o que explica por que ela é adaptativa no jejum e catastrófica quando surge sem freio, como no subtópico seguinte.

#subtopico("3.3 Diabetes tipo 1: um jejum que não termina")

Tudo o que as duas PARTES anteriores descreveram depende de um único pressuposto: que a razão insulina/glucagon consiga informar corretamente o estado nutricional. O #sigla("DM", [diabetes mellitus — grupo de doenças metabólicas caracterizadas por hiperglicemia por defeito de secreção de insulina, de sua ação, ou de ambos]) tipo 1 é o que acontece quando esse pressuposto cai: a destruição autoimune das células beta abole a insulina, a razão despenca e o fígado passa a executar o programa do jejum — permanentemente, e em cima de um sangue já saturado de glicose.

A consequência é que os dois lados do balanço são empurrados na mesma direção errada. Do lado do consumo, músculo e tecido adiposo não recrutam GLUT4 e param de captar glicose. Do lado da produção, e este é o lado que costuma escapar, o fígado *continua despejando glicose no sangue*: glicogenólise e gliconeogênese seguem ativas porque não há insulina para desligá-las. A hiperglicemia do tipo 1 não é apenas glicose que não entra — é sobretudo glicose que não para de sair.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-32.png",
  largura: 78%,
  legenda: [O painel de cima é o que deveria acontecer depois de uma refeição; o de baixo, o que acontece no jejum. No tipo 1 o organismo executa o painel de baixo mesmo depois de comer.])

Há ainda um agravante de sinalização. A insulina, além de agir nos tecidos periféricos, freia por via parácrina a célula alfa vizinha na própria ilhota. Sem esse freio, a secreção de glucagon fica desinibida, e a hiperglucagonemia resultante empurra ainda mais a produção hepática de glicose. O paciente tem simultaneamente o acelerador preso e o freio cortado.

#clinica-box("Cetoacidose diabética: os dois braços do mesmo defeito", [A ausência de insulina libera a lipase hormônio-sensível sem qualquer contrapeso: a lipólise segue máxima, o fígado é inundado de ácido graxo e a cetogênese roda sem o teto que a insulina residual impõe no jejum fisiológico. Acetoacetato e beta-hidroxibutirato são ácidos; acumulados, consomem o bicarbonato do plasma e produzem acidose metabólica com #termo-nota[ânion gap][diferença entre os cátions e os ânions habitualmente medidos no plasma; aumenta quando um ácido novo, não medido, entra na circulação] aumentado. Em paralelo, e de forma independente, a glicose plasmática ultrapassa a capacidade de reabsorção do túbulo proximal — em torno de 180 miligramas por decilitro — e a fração não reabsorvida permanece na luz tubular arrastando água por #termo-nota[diurese osmótica][perda de água urinária arrastada por um soluto que excede a capacidade de reabsorção tubular]. Daí a poliúria, a desidratação e a sede intensa. São dois braços do mesmo defeito, não um consequência do outro: é possível ter cetoacidose com glicemia apenas moderadamente elevada, e é por isso que corrigir só o açúcar não resolve o quadro.])

Fecha o desenho o catabolismo proteico. Sem insulina, o músculo degrada proteína para abastecer a gliconeogênese hepática, o nitrogênio sai como ureia e o balanço nitrogenado fica negativo mesmo com ingestão preservada. O emagrecimento do tipo 1 não é falta de comida: é o corpo desmontando a si próprio porque não consegue ler que comeu.

#subtopico("3.4 Diabetes tipo 2: resistência, compensação e falência")

O tipo 2 responde por mais de nove em cada dez casos de diabetes e nasce de um defeito oposto ao do tipo 1. Aqui a insulina está presente — no começo, em concentração normal ou até elevada. O que falha é a resposta do tecido a ela, e o defeito é predominantemente pós-receptor: a cascata que vai do receptor à PKB e à translocação do GLUT4 transmite mal o sinal, de modo que músculo e adiposo captam menos glicose apesar de o hormônio estar ali.

A célula beta reage do único jeito que sabe: secretando mais. Durante anos a hiperinsulinemia compensatória mantém a glicemia dentro da faixa, e é por isso que o quadro se instala em silêncio — a resistência precede em muito tempo o diagnóstico. A estimulação crônica, porém, tem preço: a célula beta acaba falindo, a secreção cai, e só então a glicemia sobe de forma persistente. Ao contrário do tipo 1, cuja instalação é abrupta, o tipo 2 é uma curva longa.

#figura-nebli("/figuras/biomol-06-integracao-metabolica-ii/slide-45.png",
  largura: 62%,
  legenda: [Três setas convergem para o mesmo centro. Trate a figura como uma soma, não como uma escolha: a hiperglicemia do tipo 2 exige os três defeitos operando juntos.])

Os três defeitos que sustentam a hiperglicemia são, portanto, somados: captação reduzida no músculo e no adiposo, produção hepática de glicose aumentada — o fígado resistente também não desliga a gliconeogênese — e secreção pancreática que deixa de compensar. O excesso de ácido graxo que chega ao fígado pelo adiposo resistente à insulina contribui para os dois primeiros, num fenômeno de #termo-nota[lipotoxicidade][acúmulo de metabólitos lipídicos em tecidos não adiposos, que interfere na transmissão do sinal da insulina] que costura obesidade, hipertensão e dislipidemia na mesma síndrome.

#clinica-box("Por que o tipo 2 descompensa sem cetoacidose", [A insulina residual do tipo 2 é insuficiente para promover a captação de glicose no músculo, mas costuma bastar para uma tarefa bem mais sensível: frear a lipase hormônio-sensível do adipócito. Como a lipólise fica contida, não há inundação de ácido graxo no fígado e a cetogênese não dispara. A descompensação típica é, então, o *estado hiperosmolar*: a produção hepática de glicose segue sem freio, a glicemia atinge valores muito superiores aos da cetoacidose, a diurese osmótica se prolonga por dias e o paciente chega gravemente desidratado, com hiperosmolaridade plasmática e rebaixamento de consciência — mas sem acidose importante. A diferença entre as duas descompensações não está na gravidade: está em quanto resta de insulina para segurar o adipócito.])

Sobra a lesão que corre em silêncio nos dois tipos. A #termo-nota[glicação][ligação não enzimática de glicose a grupos amino de proteínas, proporcional à concentração de glicose e ao tempo de exposição] é uma reação espontânea, sem enzima e sem regulação: quanto mais glicose e quanto mais tempo, mais proteína modificada — e proteína glicada perde função. É esse mecanismo que fundamenta a hemoglobina glicada como exame. Como a hemácia vive cerca de 120 dias e não repõe suas proteínas, a fração glicada da hemoglobina registra a exposição acumulada das últimas semanas, e não a glicemia da manhã da coleta. O mesmo processo, aplicado a colágeno, cristalino e membrana basal, é o que produz, ao longo de anos, as complicações crônicas.

#conclusao-box[
Um princípio unificador atravessou as três PARTES: *o metabolismo não decide pela concentração de nutriente, decide pela razão insulina/glucagon* — e essa razão é traduzida dentro da célula por um punhado de interruptores químicos que comutam vias opostas em um único movimento.

O mecanismo nuclear é sempre o mesmo gesto, repetido em escalas diferentes. Um fosfato posto ou removido comuta a glicogênio sintase e a fosforilase em sentidos contrários; o mesmo fosfato, na enzima bifuncional, apaga o sítio quinase e acende o sítio fosfatase, fazendo a frutose-2,6-bifosfato subir ou sumir e com ela a direção do fluxo entre glicólise e gliconeogênese; e uma molécula sozinha, o malonil-CoA de um lado e o acetil-CoA do outro, abre uma via enquanto fecha a via oposta. Nenhum desses pontos ativa duas coisas contraditórias — todos garantem exclusividade, e é essa exclusividade que impede o organismo de queimar e construir o mesmo composto ao mesmo tempo.

A clínica retomada é a demonstração do princípio por ausência. No tipo 1, sem insulina, o fígado lê jejum permanente e executa o programa inteiro sobre um sangue hiperglicêmico: gliconeogênese que não desliga, lipólise sem contrapeso, cetogênese sem teto, e a acidose que decorre disso. No tipo 2, a insulina chega mas não é ouvida pelo músculo, embora ainda seja ouvida pelo adipócito — resta insulina bastante para segurar a lipólise e não para abrir o GLUT4, e é essa dose intermediária que explica por que a descompensação é hiperosmolar em vez de cetoacidótica. Nos dois casos, a glicação vai acumulando o registro do descontrole nas proteínas de vida longa.

A projeção é direta: as próximas etapas do curso vão pedir esse mesmo raciocínio aplicado a tecidos que fogem da regra — a célula que consome glicose desproporcionalmente mesmo com oxigênio disponível, o organismo que emagrece apesar de comer, o fármaco que interfere de propósito em um dos pontos de controle desta aula. Todos são variações sobre a mesma pergunta que você já sabe responder: qual sinal esse tecido está lendo, e qual interruptor ele comuta.
]
