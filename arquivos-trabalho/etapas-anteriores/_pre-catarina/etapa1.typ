#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  No Krebs a gente fechou cada acetil-CoA gerando 3 NADH, 1 FADH₂ e 1 GTP. Mas se você parar pra pensar, o NADH e o FADH₂ não são energia ainda — são carregadores. Eles guardam dois elétrons de alta energia cada, e enquanto esses elétrons estiverem presos ali, a célula não conseguiu fazer ATP de verdade com eles.

  Este resumo é sobre o que a mitocôndria faz com esses elétrons. Em uma frase: ela passa cada elétron por uma fila de proteínas que vai descendo em energia, usa o que cai pra bombear próton, e depois deixa o próton voltar por um rotor que monta ATP. Tem nome: cadeia respiratória e fosforilação oxidativa. Vamos entender por que isso resolve o problema do Krebs, quais são as peças do circuito, e o que acontece quando alguma trava.
]

#parte-title("PARTE I — Por que existe uma cadeia", primeira: true)

#subtopico("1.1 — O problema que veio do Krebs")

O Krebs deixou a célula com um estoque enorme de NADH e FADH₂. Cada um desses #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzido — coenzima que carrega dois elétrons de alta energia para a cadeia respiratória]) carrega dois elétrons que estão "querendo cair" — querendo achar uma molécula com mais afinidade por elétron pra entregar essa carga. O alvo final, lá no fim da fila, é o O₂. Quando o elétron finalmente chega no oxigênio, ele se acomoda em uma energia muito mais baixa, e a diferença entre onde ele estava (no NADH) e onde ele terminou (na água) é gigante — algo na faixa de 220 kJ por mol.

Esse é o problema. Se a célula deixasse o NADH reagir direto com o O₂ — tipo queimar gasolina em chama aberta — toda essa energia viraria calor de uma vez. Bom pra aquecer, péssimo pra fazer ATP. Lembra que a ligação de fosfato no ATP guarda cerca de 30 kJ por mol? Se você libera 220 kJ de uma vez, sobra um buraco enorme: tudo aquilo vira calor e a célula não conseguiu capturar quase nada como trabalho útil.

A solução evolutiva foi parcelar. Em vez de o elétron pular direto do NADH pro O₂, ele desce uma escada — cada degrau libera um pedacinho da energia, e cada pedacinho serve pra fazer um trabalho específico. Esse trabalho é bombear próton de um lado da membrana mitocondrial interna pro outro. O que era "energia química de elétron" vira "energia de concentração de próton". E essa energia de próton, no fim, vai fazer o ATP. É de manso, com aproveitamento alto.

#figura-nebli("/figuras/cadeia-respiratoria/slide-13.png",
  largura: 70%,
  legenda: [A cadeia respiratória é literalmente uma escada de potencial de redução. O elétron entra no topo (NADH, E°' = -0,32 V) e desce, parando em cada complexo, até chegar no O₂ (E°' = +0,82 V). Cada queda libera energia suficiente pra bombear próton — só não toda de uma vez.])

#subtopico("1.2 — Potencial de redução, na prática")

Tem um termo técnico aqui que vale destrinchar antes de seguir: #termo-nota[potencial de redução][medida da afinidade de uma molécula por elétron — quanto mais positivo, mais "fome" de elétron]. Mede em volt (V), simbolizado E°'. A regra é simples: elétron sempre flui de quem tem E°' menor (negativo) pra quem tem E°' maior (positivo). Como se fosse água caindo — só desce.

O NADH tem E°' = -0,32 V. O O₂ tem E°' = +0,82 V. A diferença é 1,14 V, e essa diferença vira a energia disponível pela equação ΔG°' = -nFΔE°'. Sem decorar a equação: o que importa é que *a diferença de potencial entre o doador e o aceptor define quanta energia o elétron libera ao passar*. Quanto maior a queda, mais energia. E a cadeia é montada justamente em ordem de potencial crescente: cada componente tem E°' um pouco maior que o anterior, então o elétron desce confortavelmente do começo ao fim.

Aqui aparece um ponto que confunde muito aluno. O FADH₂ — outro carregador que vem do Krebs (lembra do succinato → fumarato?) — entra mais tarde na cadeia, num degrau mais baixo, porque o E°' dele é maior que o do NADH. Tradução: o FADH₂ tem menos energia pra entregar. E é por isso, e não por outra razão, que ele rende menos ATP no fim das contas. Você vai ouvir muita gente dizer que "FADH₂ rende 1,5 ATP e NADH rende 2,5 ATP" como se fosse decoreba — não é. É só consequência de onde cada um entra na cadeia.

#subtopico("1.3 — A ideia central: gradiente como moeda intermediária")

Vou repetir porque é o coração do resumo: a célula não usa a energia do elétron pra fazer ATP diretamente. Ela usa pra bombear próton. E o gradiente de próton resultante — H⁺ concentrado fora da matriz, H⁺ diluído dentro — é que vai virar ATP depois.

Esse princípio tem nome: #termo-nota[teoria quimiosmótica][proposta por Peter Mitchell em 1961 — a energia do transporte de elétrons é convertida em gradiente eletroquímico de prótons, e só depois esse gradiente faz ATP]. Quando Mitchell propôs isso, ninguém aceitou — soava esquisito. Hoje é canônico. A energia do gradiente combinado (diferença de concentração + diferença de carga elétrica) chama #termo-nota[força próton-motriz][soma da diferença química de H⁺ e da diferença de potencial elétrico através da membrana mitocondrial interna — gira em torno de 0,2 V no total].

Por que isso funciona? Porque a membrana mitocondrial interna é impermeável a próton. O próton não atravessa de volta sozinho — ele só tem um caminho liberado, e esse caminho é por dentro da ATP sintase. Então toda a energia que foi gasta pra bombear o próton fica "armazenada" no gradiente, esperando o próton voltar pelo caminho certo. Quando ele volta, a ATP sintase usa a passagem dele pra construir ATP. Genial.

#parte-title("PARTE II — As peças que carregam o elétron")

#subtopico("2.1 — Quatro complexos, dois carregadores móveis")

A cadeia respiratória mora na membrana mitocondrial interna — aquela enrugada, com as cristas. Os componentes estão organizados em quatro grupos fixos, chamados complexo I, II, III e IV, que são proteínas integrais da membrana. Entre eles circulam dois carregadores menores, móveis: a coenzima Q (também chamada ubiquinona) e o citocromo c. A função desses dois é transportar elétron de um complexo pro próximo, como um carrinho entre estações.

Antes de detalhar cada complexo, repare numa lógica geral: três dos quatro complexos (I, III e IV) bombeiam próton da matriz pro espaço intermembranas. O complexo II é exceção — ele transfere elétron, mas a queda de energia ali é pequena demais pra justificar bombeamento. Então o II é meio "passador silencioso". Vamos ver cada um.

#subtopico("2.2 — Complexo I (NADH-CoQ oxidorredutase)")

Esse é o ponto de entrada do NADH. Quando o NADH chega na matriz, ele descarrega seus dois elétrons no complexo I. A primeira proteína dentro do complexo a receber é a #termo-nota[FMN][flavina mononucleotídeo — grupo prostético derivado da riboflavina que aceita elétrons do NADH no complexo I], que pega os dois elétrons do NADH e fica reduzida (vira FMNH₂). De lá os elétrons vão escorregando por uma série de #termo-nota[centros ferro-enxofre][agrupamentos Fe-S que carregam elétron um de cada vez, presentes em vários complexos da cadeia — funcionam como mini-trilhos de elétron] até chegar na ubiquinona, que é o carregador móvel que sai do complexo I e leva os elétrons pro complexo III.

Por que isso bombeia próton? Porque a passagem do elétron pelos centros Fe-S muda a conformação da proteína, e essa mudança literalmente empurra próton da matriz pra fora. É um motor molecular: elétron entra de um lado, próton sai pelo outro. Para cada par de elétrons que passa pelo complexo I, 4 prótons saem da matriz.

#figura-nebli("/figuras/cadeia-respiratoria/slide-21.png",
  largura: 65%,
  legenda: [Complexo I em corte. O NADH descarrega elétrons na FMN; eles percorrem os centros Fe-S e terminam reduzindo a CoQ. A energia liberada nessa passagem bombeia 4 H⁺ para o espaço intermembranas.])

#subtopico("2.3 — Complexo II (succinato-CoQ redutase)")

Lembra do passo do Krebs em que o succinato vira fumarato? A enzima que faz essa reação chama succinato desidrogenase, e ela é a única enzima do Krebs que está ancorada na membrana mitocondrial interna. Adivinha o nome dela quando a olhamos pela ótica da cadeia respiratória? Complexo II. É a mesma proteína, vista de outro ângulo.

O succinato entrega dois elétrons via FAD (que vira FADH₂), e o FADH₂ — preso dentro do complexo — passa esses elétrons pra centros Fe-S, que entregam pra CoQ. Tudo isso sem bombear próton, porque a queda de potencial é pequena. Por isso o FADH₂ rende menos ATP no fim: ele entrou tarde, num ponto baixo da escada, pulando a bombeação do complexo I.

Esse mesmo complexo II, ou melhor, esse mesmo ponto de entrada de FADH₂ na CoQ, recebe elétron de outras fontes também — beta-oxidação de ácidos graxos joga FADH₂ aqui, e o glicerol-3-fosfato (que vamos ver no fim) também despeja elétron na CoQ por uma via paralela.

#subtopico("2.4 — Complexo III (CoQ-cit c redutase) e o ciclo Q")

A CoQ reduzida (chama QH₂) chega no complexo III, que é um dos lugares mais barrocos da cadeia. Aqui acontece o que se chama ciclo Q: a CoQ não simplesmente entrega elétron e sai — ela passa por um vai-e-vem em duas etapas. O resultado líquido é que 2 elétrons saem do QH₂, vão pro citocromo c (um por vez, porque o cit c só carrega um), e nesse processo 4 prótons são bombeados pra fora da matriz.

A complicação aqui não vem porque é difícil, vem porque a estequiometria do ciclo Q é meio contraintuitiva — alguns prótons que aparecem fora vêm da matriz, outros vêm da própria QH₂ sendo deprotonada. Pra fim de prova, o que importa é a contabilidade líquida: a cada par de elétrons passando pelo complexo III, 4 H⁺ vão pro espaço intermembranas.

#subtopico("2.5 — Citocromo c, o mensageiro entre III e IV")

O citocromo c é uma proteína pequena, livre na face externa da membrana mitocondrial interna. Ela tem um grupo heme (igual ao da hemoglobina) com ferro que oscila entre Fe²⁺ e Fe³⁺ a cada elétron transportado. A função é só essa: pegar elétron do complexo III e entregar no IV. Um carrinho mensageiro, do III ao IV, um elétron por viagem.

#termo-nota[citocromo][proteína com grupo heme contendo ferro que transporta elétrons mudando o estado de oxidação do ferro entre Fe²⁺ e Fe³⁺]. Existem vários citocromos na cadeia (b, c1 no complexo III, c entre III e IV, a e a3 no complexo IV) — cada um tem um E°' ligeiramente diferente, e essa diferença é o que faz o elétron andar de um pro próximo na ordem certa.

#subtopico("2.6 — Complexo IV (citocromo c oxidase) e a entrega final")

O elétron, agora carregado pelo cit c, finalmente chega no complexo IV. Esse é o complexo que faz o trabalho mais perigoso da célula: pegar 4 elétrons, juntá-los com 4 H⁺ da matriz, e entregar pro O₂ formando 2 H₂O. Por que perigoso? Porque se o O₂ pegar elétron de um em um, ele vira radical livre (superóxido, peróxido, hidroxila) — espécies reativas que destroem tudo que estiver perto. O complexo IV é uma armadilha bioquímica que segura o O₂ ali com íons de cobre (Cu_A e Cu_B) e citocromos a/a3, e só libera quando os 4 elétrons já estão prontos pra entregar de uma vez.

Para cada par de elétrons passando pelo complexo IV, 2 H⁺ adicionais são bombeados pra fora. Somando: complexo I bombeia 4, complexo III bombeia 4, complexo IV bombeia 2 — total 10 prótons por par de elétrons vindo do NADH. Quando o elétron vem do FADH₂, ele pula o complexo I, então a conta dá 4 + 2 = 6 prótons. Essa diferença é a origem do P/O 2,5 vs 1,5.

#figura-nebli("/figuras/cadeia-respiratoria/slide-36.png",
  largura: 60%,
  legenda: [Complexo IV (citocromo oxidase). Os cobres Cu_A e Cu_B e os citocromos a/a3 prendem o O₂ até receberem os 4 elétrons necessários — só então a redução pra água é liberada. Esse mecanismo evita formação de radicais livres intermediários.])

#atencao-box("Cianeto bloqueia o IV — não o I",
  [Confusão clínica letal: o aluno tende a falar que cianeto "para a cadeia respiratória" sem especificar onde. Cianeto se liga ao Fe do citocromo a3 do complexo IV e bloqueia a entrega de elétron ao O₂. Por que isso importa? Porque o tratamento depende disso. Em intoxicação por cianeto a gente dá nitritos pra gerar metemoglobina, que sequestra o cianeto. Se você confundir com inibidor de complexo I (rotenona) ou de III (antimicina), o raciocínio terapêutico desanda. Pior: o paciente com cianeto tem sangue venoso vermelho-vivo (porque o O₂ não está sendo consumido) — sinal clínico distintivo só faz sentido se você sabe que o IV foi bloqueado.])

#parte-title("PARTE III — Do gradiente ao ATP, e quando a cadeia trava")

#subtopico("3.1 — A ATP sintase é um motor mecânico")

Chegamos no momento em que o gradiente de próton vira ATP. E aqui mora uma das coisas mais bonitas da bioquímica: a ATP sintase é literalmente um motor rotatório molecular. Não é figura de linguagem.

A enzima tem duas partes. Uma fica embebida na membrana, chamada F₀, e funciona como um canal por onde o próton passa. A outra projeta pra dentro da matriz, chamada F₁, e contém três sítios catalíticos que pegam ADP e Pi e juntam virando ATP. As duas partes estão conectadas por uma haste central.

#figura-lateral("/figuras/cadeia-respiratoria/slide-48.png",
  lado: "right",
  largura-figura: 38%,
  texto: [Quando o próton entra no F₀ vindo do espaço intermembranas, ele empurra um anel de subunidades — e esse anel gira fisicamente. A rotação do anel força a haste central a girar junto. E como a haste é assimétrica, ao girar dentro do F₁ ela obriga cada um dos três sítios catalíticos a mudar de conformação em sequência. É a mudança de conformação que faz o ATP — não a passagem direta do próton.],
  legenda: [ATP sintase: F₀ é o motor de membrana, F₁ é a "cabeça" catalítica.])

Esse modelo chama-se de mudança de ligação (binding change). Cada sítio passa por três estados — aberto (O, ATP escapa), frouxo (L, ADP e Pi entram), apertado (T, ATP é montado). A cada giro de 120° da haste central, cada sítio avança um estado. Em uma volta completa, três ATP são feitos.

A relação aproximada é: cerca de 10 prótons precisam atravessar a ATP sintase pra fazer 3 ATP, ou seja, cerca de 3 H⁺ por ATP. Some isso aos 10 H⁺ bombeados por par de elétrons vindo do NADH, e você chega ao P/O ≈ 2,5 ATP por NADH. Para FADH₂, 6 H⁺ ÷ 3 ≈ 2 ATP, mas tem um custo extra de transporte de Pi e ADP que derruba pra 1,5.

#subtopico("3.2 — Acoplamento: a cadeia só anda se a ATP sintase deixa")

Aqui chega outro conceito importante. O transporte de elétron e a síntese de ATP estão acoplados — um depende do outro. Se a ATP sintase para, o próton bombeado fica preso fora, o gradiente cresce até ficar grande demais, e a força necessária pra bombear mais próton vira impossível. Resultado: a cadeia respiratória trava. NADH para de ser oxidado, e o Krebs também trava porque o NAD⁺ não regenera.

O contrário também vale. Quando a célula está consumindo ATP em ritmo alto (ex.: exercício), a ATP sintase opera no máximo, o gradiente é dissipado rápido, e a cadeia respiratória acelera pra repor o gradiente. Esse mecanismo se chama controle respiratório, e é o que mantém o consumo de O₂ proporcional à demanda energética.

Tem um truque farmacológico que explora exatamente esse acoplamento: o #termo-nota[desacoplador][molécula lipossolúvel que carrega próton diretamente através da membrana, dissipando o gradiente sem passar pela ATP sintase — desacopla transporte de elétrons da síntese de ATP]. O exemplo clássico é o 2,4-dinitrofenol (#sigla("DNP", [2,4-dinitrofenol — desacoplador clássico que dissipa o gradiente de próton sem síntese de ATP, gerando calor; usado experimentalmente e, num passado obscuro, como emagrecedor com mortes registradas])).

O DNP é lipossolúvel, atravessa a membrana, pega próton fora, leva pra dentro, larga. Resultado: o gradiente não se mantém, mas a cadeia respiratória continua andando livremente — afinal, o gradiente não está mais represando o bombeamento. O que acontece com a energia? Vira calor. Todo o investimento do elétron descendo a cadeia, em vez de virar ATP, vira aquecimento puro.

Pode parecer só curiosidade, mas é o mecanismo fisiológico da #termo-nota[termogênese][produção de calor mediada por desacopladores naturais, como a UCP1 no tecido adiposo marrom — gradiente de próton é dissipado e a energia vira calor para manter temperatura corporal] no tecido adiposo marrom: o bebê recém-nascido tem uma proteína chamada UCP1 (termogenina) que faz exatamente o que o DNP faz — desacopla a cadeia, gera calor. É como ele se mantém aquecido sem tremor muscular.

#figura-nebli("/figuras/cadeia-respiratoria/slide-43.png",
  largura: 65%,
  legenda: [Mapa dos inibidores e desacopladores na cadeia. Rotenona trava o I; antimicina trava o III; cianeto e CO travam o IV; oligomicina trava a ATP sintase; DNP desacopla. Repare que inibir um complexo é diferente de desacoplar — no primeiro caso a cadeia para; no segundo ela acelera, sem fazer ATP.])

#subtopico("3.3 — Lançadeiras: o NADH do citosol não entra direto")

Última peça importante. Lembra que a glicólise gerou NADH lá fora, no citosol? Esse NADH precisa entregar elétron pra cadeia respiratória, que está na matriz da mitocôndria. Só que a membrana mitocondrial interna é impermeável a NADH. Então a célula tem dois esquemas pra transferir esses elétrons pra dentro — chamados lançadeiras.

A lançadeira do malato-aspartato funciona no fígado, no rim e no coração. O NADH citosólico reduz oxaloacetato a malato; o malato atravessa a membrana, e dentro da matriz é reoxidado, regenerando NADH na matriz. Esse NADH entra no complexo I normalmente, e rende os 2,5 ATP normais.

Já a lançadeira do glicerol-3-fosfato funciona no músculo esquelético e no cérebro. Aqui o NADH citosólico reduz diidroxiacetona-fosfato a glicerol-3-fosfato, e o glicerol-3-fosfato entrega seu elétron direto pra CoQ — via uma enzima da face externa da membrana mitocondrial interna, gerando FADH₂. Ou seja, o elétron pulou o complexo I. Resultado: rende só 1,5 ATP em vez de 2,5.

Por que existe essa diferença? Velocidade. A lançadeira do glicerol-3-fosfato é unidirecional e mais rápida — vale a pena no músculo, que prefere ATP rápido a ATP eficiente. A do malato-aspartato é reversível e mais lenta, mas conserva o rendimento — perfeito pro fígado, que tem todo o tempo do mundo pra ser eficiente.

#figura-lateral("/figuras/cadeia-respiratoria/slide-67.png",
  lado: "left",
  largura-figura: 42%,
  texto: [No malato-aspartato, o NADH citosólico vira malato (via MDH citosólica), entra na mitocôndria, e dentro vira NADH de novo. Saldo: NADH citosólico → NADH mitocondrial, sem perda de rendimento.],
  legenda: [Lançadeira malato-aspartato.])

#subtopico("3.4 — Saldo final, e por que esse número varia em livros")

Vamos amarrar tudo. A oxidação completa de uma glicose, em condições aeróbicas, com lançadeira eficiente (malato-aspartato), dá aproximadamente 30 a 32 ATP. Glicólise contribui com 2 ATP diretos e 2 NADH (que viram 5 ATP via cadeia, se a lançadeira preserva); piruvato → acetil-CoA contribui com 2 NADH (5 ATP); o Krebs contribui com 6 NADH (15 ATP), 2 FADH₂ (3 ATP) e 2 GTP (2 ATP). Soma: 2 + 5 + 5 + 15 + 3 + 2 = 32 ATP.

Por que livros antigos falam em 38 ATP? Porque a estequiometria histórica considerava P/O = 3 pro NADH e P/O = 2 pro FADH₂ — números redondos baseados em medições antigas. Hoje sabemos que os valores reais são 2,5 e 1,5, e por isso o saldo cai pra 30–32. Não é o seu livro que está errado — é a versão dele que está velha. Se a prova pedir saldo, presuma 30–32 a menos que o enunciado seja explicitamente baseado na convenção antiga.

#conclusao-box[
  A cadeia respiratória resolve um problema termodinâmico: como capturar 220 kJ de energia por NADH sem perder em calor. A solução é parcelar a queda em quatro complexos, cada um aproveitando um pedaço da energia pra bombear próton através da membrana mitocondrial interna.

  O gradiente de próton resultante é a moeda intermediária — não é energia química de ligação ainda, é energia eletroquímica armazenada. A ATP sintase converte esse gradiente em ATP por um mecanismo mecânico de rotação: próton entra no F₀, faz o motor girar, e a rotação força os sítios do F₁ a montarem ATP em três etapas conformacionais.

  Quando a cadeia trava num ponto específico — cianeto no complexo IV, rotenona no I, oligomicina na ATP sintase — todo o fluxo para, o NAD⁺ não regenera, o Krebs trava, a célula morre. Quando a cadeia é desacoplada — DNP, UCP1 — a energia vira calor em vez de ATP. Esse último caso é menos catastrófico mas igualmente importante: é assim que o recém-nascido se aquece, e é por isso que o DNP foi proibido como emagrecedor — gente morria de hipertermia.

  No próximo resumo da UC, vamos seguir pra integração metabólica geral — como cadeia respiratória, Krebs, glicólise, beta-oxidação e gliconeogênese conversam entre si dependendo do estado fisiológico. Cadeia respiratória é o ponto onde quase tudo desemboca: entender ela é entender por que cada via existe e quando cada uma é desligada.
]
