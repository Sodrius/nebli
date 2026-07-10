#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Antes de mergulhar nos quatro complexos, num punhado de citocromos e numa enzima rotatória, vale parar e perguntar uma coisa quase boba: *por que toda essa máquina existe?* A célula tem #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzida — coenzima carregando 2 elétrons de alta energia oriundos do catabolismo]) e #sigla("FADH₂", [flavina adenina dinucleotídeo reduzida — coenzima carregando 2 elétrons de menor energia, ligada covalentemente à enzima de origem]) recheados de energia depois da glicólise, do ciclo de Krebs e da β-oxidação. Se ela simplesmente jogasse esses elétrons no oxigênio direto, a energia sairia toda de uma vez — em forma de *calor*. O calor não fabrica ligações químicas; ele esquenta a sopa.

  A solução evolutiva foi engenhosa: *fracionar a queima em degraus pequenos*. Cada degrau libera só o suficiente para fazer uma coisa útil — empurrar prótons para fora da matriz mitocondrial. O gradiente de prótons que se acumula funciona como uma represa: quando a água volta pela turbina (a #sigla("ATP", [adenosina trifosfato — moeda energética universal da célula]) sintase), gira o eixo e força a junção de #sigla("ADP", [adenosina difosfato — substrato da ATP sintase]) com #sigla("Pi", [fosfato inorgânico — segundo substrato da ATP sintase]).

  Este resumo segue essa linha de raciocínio. *A PARTE I* mostra por que a cadeia tem que existir do jeito que tem — termodinâmica, potenciais redox, anatomia mitocondrial. *A PARTE II* abre cada um dos quatro complexos e mostra o que cada um faz no detalhe. *A PARTE III* costura tudo: como o gradiente vira ATP, quanto rende, e o que acontece quando alguma coisa interrompe o sistema — cianeto, dinitrofenol, neonato com hipotermia. Se em algum momento você travar, volte à imagem da represa. *Toda a cadeia é uma engrenagem que transforma energia química em energia eletroquímica e, no fim, em ligação química.*
]

#parte-title("PARTE I — Por que existe uma cadeia", primeira: true)

#subtopico("1.1 Da queima térmica ao fracionamento controlado")

A pergunta certa para começar não é "o que faz a cadeia respiratória?", e sim *"por que a célula não pode simplesmente queimar a glicose como uma fogueira?"*. Numa fogueira, glicose + oxigênio viram gás carbônico, água e calor — exatamente os mesmos produtos da respiração celular. A diferença está na *forma* como a energia sai. Na fogueira, o ΔG total da reação (cerca de −2.870 kJ/mol para uma glicose inteira) escapa de uma vez como calor; nada é capturado em ligação química.

A célula não pode pagar esse preço. Ela precisa armazenar essa energia em moléculas que servem de moeda — sobretudo o ATP, cuja hidrólise libera cerca de 30,5 kJ/mol. O problema é estequiométrico: uma única transferência de elétrons do NADH para o O#sub[2] libera cerca de *220 kJ/mol*, energia suficiente para fabricar 7 ATPs em teoria. Mas o salto é alto demais; não existe enzima capaz de absorver 220 kJ num único passo e converter tudo em ligação química. *O excesso vira calor inevitavelmente.* É como tentar usar uma queda d'água de 200 metros para girar uma rodinha de cozinha — a água passa, mas o impacto destrói o equipamento.

A saída elegante foi *fracionar*. Em vez de transferir os elétrons direto do NADH para o O#sub[2], a célula os faz descer por degraus de cerca de 20 kJ/mol cada — um valor que cabe confortavelmente em mecanismos enzimáticos conhecidos. Cada degrau libera energia em quantidade pequena e bem definida, exatamente o suficiente para *bombear* um próton da matriz para o espaço intermembranas. O ΔG total continua o mesmo (220 kJ/mol não some); só que agora ele aparece distribuído em ~10 transferências sequenciais, e em cada uma a energia sai como *trabalho útil* (bombeamento) em vez de calor.

#mini-resumo[O ΔG da oxidação do NADH é fixo (−220 kJ/mol). Soltá-lo de uma vez geraria calor; soltá-lo em ~10 passos de ~20 kJ/mol cada permite capturá-lo como gradiente de prótons.]

#figura-nebli("/figuras/cadeia-respiratoria/slide-11.png",
  largura: 70%,
  legenda: [O cálculo do ΔG° a partir dos potenciais de redução. Repare que o salto de NAD⁺/NADH (−0,32 V) para O₂/H₂O (+0,82 V) gera os −220 kJ/mol totais. A cadeia *fraciona* esse salto em pedaços de ~20 kJ/mol bombeando prótons em cada degrau.])

A consequência clínica desse fracionamento aparece quando o sistema falha. *Quando um desacoplador como o dinitrofenol perfura o sistema de bombeamento*, os elétrons continuam descendo pelos complexos, mas a energia que deveria virar gradiente vaza como *calor*. O paciente entra em hipertermia maligna, sua profusamente, e em doses altas morre de superaquecimento — uma demonstração brutal de que sem fracionamento controlado, a queima do NADH é, literalmente, uma fogueira interna.

Note como o fracionamento *não é controle de velocidade*. A confusão clássica aqui é achar que a célula fraciona para controlar quão rápido a reação acontece, como se o objetivo fosse frear a oxidação. Não é. A oxidação até poderia ser rápida; o que limita é a *captura energética*. O fracionamento é exigência *termodinâmica*, não cinética — caber em quanta menores para que cada um possa virar trabalho útil em vez de calor.

#subtopico("1.2 Reações redox e potenciais")

Imagine duas esponjas de elétrons mergulhadas na mesma bacia. Uma esponja é cheia (NADH, carregada de elétrons); a outra é seca (O#sub[2], sedento de elétrons). Quando se tocam, os elétrons saem da cheia para a seca — e fazem isso *sozinhos*, sem precisar de empurrão. A magnitude dessa "fome" relativa de elétrons é o que se chama de #termo-nota[potencial de redução][medida em volts da afinidade de um par redox por elétrons; quanto mais positivo o E°', maior a "fome" de receber elétrons], abreviado E°'.

A regra é simples: *elétrons fluem espontaneamente do par redox com E°' mais negativo para o par com E°' mais positivo*. NAD⁺/NADH tem E°' = −0,32 V (esponja muito cheia, doadora boa). O par O#sub[2]/H#sub[2]O tem E°' = +0,82 V (esponja muito seca, aceptor avidíssimo). A diferença entre os dois (ΔE°' = +1,14 V) corresponde aos −220 kJ/mol já citados, pela relação termodinâmica fundamental ΔG°' = −nFΔE°'.

#figura-nebli("/figuras/cadeia-respiratoria/slide-10.png",
  largura: 65%,
  legenda: [Escala de potenciais de redução. Quanto mais para baixo o doador (NADH no topo, mais negativo), maior a "queda" disponível. Os complexos da cadeia respiratória estão posicionados nos degraus dessa escada, em ordem crescente de E°'.])

A ordem dos complexos na membrana não é geográfica — é *termodinâmica*. Cada complexo recebe elétrons de um doador com E°' mais negativo e os passa para um aceptor com E°' mais positivo. Trocar a ordem física dos complexos não funcionaria porque os elétrons simplesmente *não fluiriam* contra o gradiente de potencial. É uma ladeira eletroquímica, e os elétrons rolam para baixo.

Aqui entra a diferença crucial entre NADH e FADH#sub[2]. O NADH tem E°' = −0,32 V; o FADH#sub[2] tem E°' próximo de zero (ligeiramente positivo, depende do contexto enzimático). Isso significa que o FADH#sub[2] "começa mais abaixo" na ladeira — *menos energia disponível para descer*. Por isso ele entra em um complexo posterior (Complexo II) e rende menos ATP no final. Não é uma decisão arbitrária da célula; é consequência direta de onde cada coenzima se encaixa na escada de potenciais.

#mini-resumo[NADH (E°' = −0,32 V) cai mais alto na escada e bombeia mais prótons; FADH₂ (E°' ≈ 0 V) cai mais baixo e bombeia menos. Por isso o saldo de ATP por NADH é maior.]

Uma confusão recorrente é misturar ΔG°' com ΔG real. O ΔG°' é o valor *padrão* — calculado supondo todas as concentrações em 1 M, pH 7, 25 °C. Na célula, as concentrações reais de NAD⁺, NADH, O#sub[2] e seus parceiros são bem diferentes desse padrão, e o ΔG real ajusta-se via a equação de Nernst. Felizmente, mesmo com a correção, o saldo permanece amplamente espontâneo — a queda é tão grande que mesmo concentrações desfavoráveis não conseguem inverter o sinal.

#confusao-prevista(
  titulo: "Os elétrons não fluem do positivo para o negativo",
  aluno_acha: [como em eletricidade básica, parece intuitivo dizer que "a corrente vai do polo positivo para o negativo"],
  mecanismo: [na cadeia respiratória, *os elétrons fluem do par com E°' mais negativo para o mais positivo*. O par mais positivo é o que "puxa" os elétrons (maior afinidade). A intuição da eletricidade convencional engana porque ela descreve fluxo de carga positiva imaginária — aqui falamos do movimento dos elétrons em si, que vão sempre na direção do aceptor mais ávido.],
)

#subtopico("1.3 Anatomia mitocondrial e os seis atores da cadeia")

A cadeia respiratória não acontece num mar solto de citoplasma — ela está cravada num lugar muito específico: a *membrana mitocondrial interna*. Isso não é detalhe decorativo; é exigência funcional. Como a cadeia precisa bombear prótons para *fora* da matriz e mantê-los lá enquanto a ATP sintase os usa, é preciso uma barreira impermeável a prótons. Essa barreira é a membrana interna; sem ela, o gradiente vazaria e o sistema não funcionaria.

#figura-nebli("/figuras/cadeia-respiratoria/slide-13.png",
  largura: 75%,
  legenda: [Os componentes da cadeia organizados na membrana mitocondrial interna. Quatro complexos (I, II, III, IV) cravados como integrais, mais dois transportadores móveis (CoQ na fase lipídica, citocromo c na face externa da membrana). A organização é determinada pelos potenciais de redução crescentes.])

A mitocôndria tem *duas* membranas. A externa é porosa (cheia de porinas — proteínas-canal que deixam passar moléculas até 5 kDa). Do ponto de vista químico, o espaço intermembranas é praticamente *idêntico ao citosol*. É a *interna* que importa: impermeável a prótons, dobrada em cristas para multiplicar a área, e contendo *todos* os complexos da cadeia respiratória mais a ATP sintase.

A confusão clássica é localizar a cadeia na matriz. Ela não está lá — a *matriz* contém as enzimas solúveis do ciclo de Krebs e o DNA mitocondrial. A cadeia está na membrana. *A única exceção* é a succinato desidrogenase: ela faz parte do ciclo de Krebs (descarboxilação oxidativa do succinato) *e* é o Complexo II da cadeia. Por isso é a única enzima de Krebs presa à membrana — ela tem um pé em cada compartimento.

Os atores que precisam ser apresentados são seis. Quatro são *complexos*, ou seja, grandes agregados proteicos com múltiplas subunidades, cravados como integrais na membrana:

- *Complexo I* (NADH:ubiquinona oxidorredutase) — porta de entrada para o NADH.
- *Complexo II* (succinato:ubiquinona oxidorredutase) — porta de entrada para o FADH#sub[2] vindo do succinato.
- *Complexo III* (ubiquinol:citocromo c oxidorredutase) — gargalo central, faz o ciclo Q.
- *Complexo IV* (citocromo c oxidase) — entrega os elétrons ao O#sub[2].

Dois são *transportadores móveis*, e essa mobilidade é essencial: eles fazem a ponte entre os complexos.

- *Coenzima Q* (ubiquinona, ou CoQ) — uma #termo-nota[ubiquinona][benzoquinona com cauda hidrofóbica de unidades isoprênicas; difunde lateralmente dentro da bicamada lipídica e carrega 2 elétrons + 2 prótons] *lipossolúvel*, que se desloca lateralmente *dentro* da bicamada lipídica. Carrega 2 elétrons.
- *Citocromo c* — uma proteína periférica pequena, ligada frouxamente à face externa da membrana interna. É *hidrossolúvel*. Carrega apenas 1 elétron por vez, via o íon Fe do seu grupo heme (Fe³⁺ ↔ Fe²⁺).

#mini-resumo[Membrana interna impermeável a prótons + 4 complexos integrais + 2 transportadores móveis (CoQ lipossolúvel, cit c periférico hidrossolúvel) = a anatomia mínima da cadeia.]

A confusão entre CoQ e citocromo c é frequente e vale travá-la agora. *CoQ é lipossolúvel* — anda dentro da membrana, na fase de fosfolipídios. *Citocromo c é hidrossolúvel* — anda pela superfície aquosa externa da membrana interna. Os dois são móveis (não estão cravados como os complexos), mas se movem em "andares" diferentes. E carregam quantidades diferentes de elétrons: CoQ leva 2 de uma vez; citocromo c leva 1. Essa diferença de estequiometria gera o famoso *ciclo Q* (que veremos na PARTE II) — sem ele, não daria para casar quem leva 2 com quem leva 1.

Os componentes dos complexos merecem nota. Os grupos prostéticos que aparecem repetidamente são: #termo-nota[FMN][flavina mononucleotídeo — grupo prostético do Complexo I, aceita 2 elétrons + 2 prótons do NADH e os repassa aos centros Fe-S] (no Complexo I, recebe os elétrons do NADH), #sigla("FAD", [flavina adenina dinucleotídeo — forma oxidada da FADH₂, grupo prostético da succinato desidrogenase]) (no Complexo II, na succinato desidrogenase), centros *ferro-enxofre* (clusters de Fe e S inorgânico que aceitam apenas elétrons, sem prótons — encontrados em I, II e III), e grupos *heme* nos citocromos (anel porfirínico com Fe central, em III, IV e no citocromo c). Os cobre nos sítios CuA e CuB do Complexo IV completam o quadro — eles são essenciais para a reação final com o O#sub[2].

O ponto que costura a PARTE I e abre a PARTE II é simples: a célula tem dois combustíveis redutores principais (NADH e FADH#sub[2]); a cadeia tem duas portas de entrada correspondentes (Complexo I e Complexo II); e a partir dessas portas, os elétrons descem um caminho fixo até o O#sub[2]. *Vamos abrir cada um desses complexos agora.*

#parte-title("PARTE II — Os quatro complexos")

#subtopico("2.1 Complexo I e Complexo II — duas portas de entrada")

Saímos da PARTE I com NADH e FADH#sub[2] na mão e a pergunta de como cada um entra na cadeia. As respostas são diferentes — e essa diferença é o que explica o famoso saldo desigual de ATP entre eles.

O *Complexo I* (NADH:ubiquinona oxidorredutase) é a porta de entrada do NADH. É uma máquina monstruosa: cerca de 42 cadeias polipeptídicas, com forma de L (uma parte mergulhada na membrana, outra projetando-se para a matriz). O caminho dos elétrons dentro dele segue uma sequência rigorosa: o NADH chega à matriz, doa seus 2 elétrons (e 2 H⁺) ao *FMN* — um grupo prostético tipo flavina; o FMN reduzido (FMNH#sub[2]) entrega esses elétrons em sequência a uma fileira de *centros Fe-S*, que funcionam como uma escada interna; e ao final dessa escada, os elétrons saem para a CoQ, que recebe seus 2 elétrons (e os 2 H⁺ vindos da matriz) e vira CoQH#sub[2] (ubiquinol).

#figura-nebli("/figuras/cadeia-respiratoria/slide-21.png",
  largura: 70%,
  legenda: [Complexo I — NADH:ubiquinona oxidorredutase. O caminho dos elétrons (FMN → cadeia de Fe-S → CoQ) está acoplado mecanicamente ao bombeamento de 4 H⁺ por par de elétrons. A geometria em L permite essa transmissão alostérica.])

O detalhe pedagógico crucial é o *bombeamento*. À medida que os elétrons descem pela escada interna, o Complexo I sofre mudanças conformacionais que abrem canais e empurram *4 prótons* da matriz para o espaço intermembranas, por par de elétrons. Esse é o lance: a transferência eletrônica está mecanicamente acoplada ao bombeamento. Os elétrons descem por dentro; os prótons saem por canais separados.

Existe uma confusão sutil aqui que vale travar. O FMN no início do caminho recebe *2 elétrons e 2 prótons* do NADH (lembre-se: NADH carrega 1 H⁻, que é equivalente a 1 H⁺ + 2 e⁻). Os centros Fe-S, por outro lado, aceitam *apenas elétrons*, sem prótons — o ferro só pode trocar entre Fe³⁺ e Fe²⁺. Então, quando os elétrons descem do FMNH#sub[2] para os Fe-S, os prótons "se desligam" e *não vão junto*. Esses prótons são justamente os que acabam sendo bombeados para o lado externo. *O FMN funciona como uma estação de comutação que separa elétrons de prótons.*

Já o *Complexo II* (succinato desidrogenase, ou succinato:ubiquinona oxidorredutase) é uma figura diferente. Ele tem FAD ligado covalentemente; quando o ciclo de Krebs oxida succinato a fumarato (única reação do ciclo que produz FADH#sub[2] em vez de NADH), os elétrons já saem direto para o FAD do Complexo II. Daí, pelos centros Fe-S internos, vão para a CoQ. Resultado: o FADH#sub[2] *nunca circula como uma molécula livre na matriz*; ele permanece preso ao Complexo II o tempo todo. Por isso o "FADH#sub[2]" mencionado nos saldos é uma abstração; o que existe é a succinato desidrogenase carregando elétrons que vieram do succinato.

#atencao-box("O Complexo II não bombeia prótons", [
  Essa é a diferença mais importante entre I e II. O Complexo I bombeia 4 H⁺ por par de elétrons; *o Complexo II bombeia ZERO*. Por quê? Porque a diferença de potencial entre succinato/fumarato (E°' ≈ +0,03 V) e CoQ/CoQH#sub[2] (E°' ≈ +0,04 V) é pequena demais — o ΔG não dá energia suficiente para empurrar prótons contra o gradiente. Os elétrons descem, mas o degrau é muito raso para mover bomba alguma. *Esta é a raiz mecanística do FADH#sub[2] render menos ATP que o NADH.*
])

#mini-resumo[Complexo I bombeia 4 H⁺ por par; Complexo II bombeia 0 — diferença de E°' explica tudo.]

Vale notar que existem outras enzimas que entregam FADH#sub[2] à CoQ — a glicerol-3-fosfato desidrogenase da face externa da membrana interna (importante na lançadeira do glicerol-3-P, que veremos adiante) e as acil-CoA desidrogenases da β-oxidação. Todas elas usam o mesmo truque mecanístico do Complexo II: entrar com FADH#sub[2] direto na CoQ sem passar pelo Complexo I e *sem bombear prótons*. Por isso a β-oxidação rende relativamente menos ATP por elétron que a glicólise.

A succinato desidrogenase merece uma menção clínica. *Mutações nas suas subunidades (SDHB, SDHD) causam paragangliomas e feocromocitomas hereditários* — tumores das células cromafins que sintetizam catecolaminas. O mecanismo é interessante: a perda da SDH acumula succinato, que inibe enzimas dependentes de α-cetoglutarato (incluindo as que regulam a estabilidade do fator HIF), levando a uma "pseudohipóxia" e estimulando proliferação tumoral. É um dos primeiros exemplos clínicos do que se chama hoje de *oncometabólitos*.

O fechamento desta seção: ambas as portas (I e II) entregam elétrons à *CoQ*. A CoQ é o ponto de convergência da cadeia — ela aceita elétrons do Complexo I, do Complexo II, da glicerol-3-P desidrogenase, das acil-CoA desidrogenases e leva todos para o próximo destino, que é o Complexo III. *Vamos para lá.*

#subtopico("2.2 CoQ, ciclo Q e Complexo III")

A CoQ chega ao Complexo III carregando 2 elétrons (na forma CoQH#sub[2], ubiquinol). O Complexo III precisa repassar esses elétrons ao citocromo c, mas o citocromo c só aceita *1 elétron por vez*. Isto é um problema estequiométrico real: como entregar 2 e⁻ para alguém que só pega 1?

A solução é o *ciclo Q*, descoberto por Peter Mitchell — o mesmo cientista que propôs a teoria quimiosmótica. O ciclo Q é um truque elegante de duas etapas que usa *duas* moléculas de CoQ (uma reduzida e uma oxidada) ligadas a sítios diferentes do Complexo III (chamados Q#sub[o] e Q#sub[i]). O resultado líquido é que o Complexo III bombeia *4 prótons* por par de elétrons — duas vezes o que faria se simplesmente passasse os elétrons direto. *A "bifurcação" entre os dois sítios é o que multiplica o bombeamento.*

#figura-nebli("/figuras/cadeia-respiratoria/slide-33.png",
  largura: 78%,
  legenda: [Ciclo Q em duas etapas. Na primeira etapa, uma CoQH₂ no sítio Q#sub[o] doa 1 e⁻ ao cit c (via centro Fe-S e cit c#sub[1]) e 1 e⁻ a uma CoQ semi-reduzida no sítio Q#sub[i]; libera 2 H⁺ no espaço intermembranas. Na segunda etapa, outra CoQH₂ chega ao Q#sub[o] e repete o processo, e a CoQ no Q#sub[i] vira CoQH₂ pegando 2 H⁺ da matriz. Bombeamento líquido: 4 H⁺ por par de elétrons.])

A confusão clássica aqui é achar que o Complexo III bombeia apenas 2 H⁺. Ele bombearia 2 se passasse os elétrons direto, mas justamente *por causa* da bifurcação do ciclo Q, ele bombeia 4. É uma das eficiências mais altas da cadeia — o Complexo III tira vantagem máxima do degrau termodinâmico entre CoQ (E°' ≈ +0,04 V) e cit c (E°' ≈ +0,25 V).

Vale uma palavra sobre o *citocromo c*. Ele é proteína pequena (cerca de 12 kDa), com um único grupo heme C ligado covalentemente. Não é integral à membrana — é #termo-nota[proteína periférica][proteína associada à superfície da membrana por interações iônicas, sem atravessar a bicamada — facilmente solubilizada por mudanças de pH ou força iônica], ligada frouxamente à face externa (lado intermembranas) da membrana interna. Essa mobilidade é essencial: ele se desloca pela superfície aquosa, recolhendo elétrons do Complexo III e entregando ao Complexo IV.

E aqui entra um dos achados mais surpreendentes da biologia celular: o citocromo c também é *o sinalizador da apoptose intrínseca*. Quando uma célula sofre dano (radiação, falta de fatores tróficos, estresse oxidativo), proteínas da família Bcl-2 (BAX/BAK) abrem poros na membrana mitocondrial externa. O citocromo c, que estava confortavelmente preso à membrana interna, *vaza para o citosol*. Lá, ele se liga ao Apaf-1 e dispara o apoptossomo, ativando a cascata de caspases que mata a célula. *Uma proteína que vive transportando elétrons dentro da mitocôndria é, fora dela, o sinal de morte programada.*

#clinica-box("Quimioterapia e apoptose via citocromo c", [
  Boa parte da eficácia clínica de quimioterápicos clássicos (doxorrubicina, cisplatina, etoposídeo) depende dessa via. Eles induzem dano que ativa BAX/BAK, vazam citocromo c, ativam caspases e a célula tumoral morre por apoptose. Tumores que perdem essa via (mutação de p53, hiperexpressão de Bcl-2) tornam-se resistentes à quimioterapia. Inibidores de Bcl-2 (venetoclax, aprovado em leucemia linfocítica crônica) reativam essa rota de morte.
])

#mini-resumo[Ciclo Q usa 2 CoQH₂ por par de elétrons para casar a estequiometria 2:1 entre CoQ e cit c, e bombeia 4 H⁺ no caminho. Cit c é proteína periférica móvel, e em apoptose vaza para o citosol e ativa caspases.]

#subtopico("2.3 Citocromo c e Complexo IV")

O citocromo c chega ao *Complexo IV* (citocromo c oxidase) entregando 1 elétron por vez. O Complexo IV recebe esse elétron e o passa internamente por uma sequência cuidadosa: dois centros de cobre (CuA, CuB), dois grupos heme (citocromos a e a#sub[3]), até finalmente entregar 4 elétrons coletivamente a uma molécula de *O#sub[2]*, formando *2 moléculas de H#sub[2]O*. Essa é a reação química final da respiração — *o oxigênio é reduzido a água*.

#figura-nebli("/figuras/cadeia-respiratoria/slide-36.png",
  largura: 65%,
  legenda: [Estrutura simplificada do Complexo IV (citocromo c oxidase). Os elétrons entram pelo CuA, passam pelo heme a, depois ao centro binuclear heme a#sub[3]–CuB onde o O₂ é reduzido a 2 H₂O. Bombeia 2 H⁺ por par de elétrons.])

O Complexo IV bombeia *2 prótons* por par de elétrons. Outros 2 prótons da matriz são consumidos quimicamente na formação da H#sub[2]O (4 e⁻ + 4 H⁺ + O#sub[2] → 2 H#sub[2]O), mas isso é "química", não "bombeamento" — esses prótons não atravessam a membrana, apenas saem da matriz para virar parte da água. Mesmo assim, o efeito sobre o gradiente é o mesmo: o lado da matriz fica mais alcalino, e o lado intermembranas mais ácido.

Por que o O#sub[2] é o aceptor final? Porque ele tem o E°' mais positivo entre os pares fisiologicamente relevantes (+0,82 V). Nenhum outro aceptor disponível na célula consegue "puxar" elétrons com a mesma força. Isso garante que a cadeia toda flua espontaneamente até o fim e que toda a energia disponível seja capturada como gradiente. Sem O#sub[2], a cadeia *para inteira* — porque o cit c não consegue entregar seus elétrons, então o Complexo III também para, então a CoQ não pode descarregar, então I e II travam. *Cascata reversa em segundos.*

Aqui entra uma confusão crítica que vale uma caixa vermelha pela gravidade do erro clínico envolvido.

#atencao-box("Cianeto bloqueia o Complexo IV, não o I", [
  O *cianeto* (CN⁻) liga-se com altíssima afinidade ao Fe³⁺ do heme a#sub[3] do Complexo IV, impedindo que ele entregue elétrons ao O#sub[2]. *A cadeia inteira para*, exatamente como descrito acima. O paciente sofre *hipóxia histotóxica*: tem oxigênio disponível no sangue, mas a célula não consegue usá-lo. O sangue venoso retorna *vermelho-cereja* (oxigênio não consumido). Esta é a marca clínica do envenenamento por cianeto — e por monóxido de carbono também (que se liga à hemoglobina em vez do Complexo IV, mas o efeito final na célula é parecido). *Confundir com bloqueio do Complexo I (rotenona) leva a tratamento errado.* O antídoto do cianeto é hidroxocobalamina ou nitrito de sódio + tiossulfato — recursos que sequestram o CN⁻ e o devolvem como cianeto férrico ou tiocianato. Para CO, oxigênio hiperbárico.
])

A reação final no Complexo IV merece um cuidado adicional. O O#sub[2] é uma molécula que adora *roubar* elétrons um a um, e nesse processo gera intermediários reativos perigosos — superóxido (O#sub[2]⁻), peróxido de hidrogênio (H#sub[2]O#sub[2]), radical hidroxila (#sigla("OH", [hidroxila — radical livre extremamente reativo, gerado por redução parcial do O₂; danifica DNA, proteínas e lipídios])). Coletivamente, esses são chamados de #sigla("ROS", [espécies reativas de oxigênio — produtos da redução parcial do O₂, incluindo O₂⁻, H₂O₂ e radical hidroxila]). O Complexo IV evoluiu para reduzir o O#sub[2] *completamente* (4 elétrons de uma vez) e segurar todos os intermediários dentro do sítio ativo até a reação terminar, justamente para evitar que escapem ROS. Mas o escape acontece — uma pequena fração dos elétrons "vaza" da cadeia (especialmente nos Complexos I e III) e reduz parcialmente o O#sub[2], gerando ROS endógeno. A célula mantém antioxidantes (superóxido dismutase, catalase, glutationa peroxidase) justamente para neutralizar esses escapes.

O acúmulo crônico de ROS é o que explica boa parte do *estresse oxidativo* — envelhecimento celular, doenças neurodegenerativas, dano isquêmico após reperfusão. Quando um tecido fica isquêmico (sem fluxo sanguíneo), os intermediários da cadeia se acumulam no estado reduzido; quando o fluxo retorna (reperfusão), o burst súbito de O#sub[2] gera ROS em quantidade massiva. *Por isso o dano de reperfusão pode ser pior que o da isquemia em si.*

#mini-resumo[Complexo IV reduz O₂ a 2 H₂O usando 4 e⁻ + 4 H⁺, bombeia 2 H⁺. Cianeto bloqueia o Complexo IV (não o I) e causa hipóxia histotóxica.]

A ponte para a PARTE III: agora que entendemos como os elétrons descem dos NADH/FADH#sub[2] até o O#sub[2] e como esse trajeto bombeia ~10 prótons por par de elétrons (4 + 0 + 4 + 2, a depender da entrada), a pergunta é *como esse gradiente vira ATP*. A resposta envolve uma das máquinas moleculares mais elegantes da biologia — a ATP sintase F#sub[0]F#sub[1] — e uma das teorias mais geniais (e inicialmente rejeitadas) do século XX: a teoria quimiosmótica de Peter Mitchell.

#parte-title("PARTE III — Acoplamento, ATP sintase e clínica")

#subtopico("3.1 Teoria quimiosmótica e força próton-motriz")

O modo como elétrons descendo geram síntese de ATP foi um mistério feroz por décadas. As primeiras hipóteses eram *químicas* — supunha-se que algum intermediário fosforilado de alta energia se formava no caminho e doava o fosfato ao ADP. Décadas de busca por esse "intermediário" não acharam nada. Em 1961, Peter Mitchell propôs algo totalmente diferente: o intermediário não é químico, é *eletroquímico*. *É o próprio gradiente de prótons.*

A ideia era tão estranha que demorou anos para ser aceita. Mitchell ganhou o Nobel em 1978. Hoje a *teoria quimiosmótica* (do grego "khemia" = química + "osmos" = empurrar) é o paradigma central da bioenergética. Ela funciona assim:

A cadeia respiratória bombeia prótons da matriz (pH ~8) para o espaço intermembranas (pH ~7). Isso cria *duas* fontes de energia armazenadas no gradiente:
- *Componente químico (ΔpH)* — diferença de concentração de H⁺ entre os dois lados (cerca de 0,5 a 1 unidade de pH).
- *Componente elétrico (Δψ)* — diferença de potencial elétrico, porque cada próton bombeado leva uma carga positiva para fora (cerca de 150 a 200 mV, com a matriz mais negativa).

A soma das duas é o que se chama de #termo-nota[força próton-motriz][energia armazenada no gradiente eletroquímico de prótons através da membrana mitocondrial interna; soma do componente químico (ΔpH) e do elétrico (Δψ); típica em humanos ~200 mV totais], abreviado *PMF* (#sigla("PMF", [proton-motive force — força próton-motriz, energia armazenada no gradiente eletroquímico de prótons; ~200 mV em humanos])). Em humanos, a PMF total chega a cerca de 200 mV — o equivalente a uma queda de 20 kJ/mol de prótons. *Essa é a energia que faz a ATP sintase rodar.*

#figura-nebli("/figuras/cadeia-respiratoria/slide-46.png",
  largura: 78%,
  legenda: [A teoria quimiosmótica de Peter Mitchell. Os complexos da cadeia bombeiam prótons da matriz para o espaço intermembranas; o retorno desses prótons pela ATP sintase é o que sintetiza ATP. PMF = 0,1 a 0,2 V, soma do ΔpH e do Δψ.])

A consequência crucial é que *transporte de elétrons e síntese de ATP são processos acoplados, mas não diretamente*. O acoplamento é via gradiente. Isso explica por que substâncias que destroem o gradiente (desacopladores) *param a síntese de ATP* mesmo sem tocar nem na cadeia, nem na sintase. Veremos isso em detalhe no subtópico 3.4.

#mini-resumo[Cadeia bombeia H⁺ para fora → gradiente de pH e carga → PMF ~200 mV → ATP sintase usa essa energia para sintetizar ATP. Cadeia e síntese acoplam via gradiente.]

Uma intuição útil é pensar a PMF como uma *represa hidrelétrica*. A água acumulada (prótons no espaço intermembranas) tem energia potencial; quando volta pela turbina (ATP sintase), gira o eixo e gera trabalho (síntese de ATP). A energia que mantém a água lá em cima é o trabalho que a cadeia respiratória faz bombeando — energia que veio dos NADH e FADH#sub[2], que vieram do catabolismo da glicose e dos ácidos graxos. *Tudo está costurado.*

A confusão clássica é tratar gradiente como mera "concentração". Não é só isso. *O componente elétrico (Δψ) é o maior dos dois*. Em mitocôndria humana, ΔpH contribui com cerca de 60 mV (1 unidade de pH) e Δψ com cerca de 140 mV. Isso significa que mais de 70% da PMF é elétrica, não química — é o desbalanço de carga que mais empurra o próton de volta. *Por isso a mitocôndria é tão sensível a qualquer condutor de íons que perfure a membrana.*

#subtopico("3.2 ATP sintase F#sub[0]F#sub[1] e o binding change")

A ATP sintase é uma das máquinas moleculares mais espetaculares conhecidas. Imagine um motor rotatório de duas peças — uma cravada na membrana, outra projetando-se para a matriz. Quando os prótons fluem da face externa para a matriz através da peça membranar, ela *gira*. A rotação se transmite por um eixo central até a peça da matriz, que sofre mudanças conformacionais que *sintetizam ATP*.

#figura-nebli("/figuras/cadeia-respiratoria/slide-48.png",
  largura: 70%,
  legenda: [A ATP sintase F#sub[0]F#sub[1]. F#sub[0] (membranar, anel de subunidades c) gira ao receber prótons; F#sub[1] (saliente na matriz, com 3 subunidades β catalíticas) muda de conformação a cada 120° de rotação. Oligomicina liga-se a F#sub[0] e bloqueia a rotação.])

Os dois componentes têm nomes históricos.

- *F#sub[0]* (Membrana — "o" de oligomicina-sensível) é um anel de subunidades c na bicamada. Em humanos, são 8 subunidades c por anel. Cada subunidade c tem um aminoácido carregado que precisa ser neutralizado por um próton para a rotação acontecer. Ao receber o próton, a subunidade gira; depois libera o próton para a matriz e volta ao estado original. Como o anel inteiro gira, cada volta completa requer 8 prótons (em humanos).

- *F#sub[1]* (Matriz — "1" de "primeiro descoberto") tem o sítio catalítico. É formado por 3 subunidades α e 3 subunidades β alternadas, organizadas como uma laranja com 6 gomos. As 3 subunidades β são as catalíticas. Um eixo central (subunidade γ) conecta F#sub[0] a F#sub[1] e gira junto com o anel c.

O detalhe genial é como a *rotação física vira síntese química*. Aqui entra o *#termo-nota[binding change][modelo de Paul Boyer (Nobel 1997) que explica a síntese de ATP pela ATP sintase via mudança cíclica de conformação dos sítios catalíticos: aberto (O) → frouxo (L) → apertado (T) → aberto] de Paul Boyer*. Cada uma das 3 subunidades β passa por 3 conformações distintas:

- *Open (O — aberto)* — libera o ATP recém-formado. Nenhum substrato fica retido.
- *Loose (L — frouxo)* — captura ADP e Pi da matriz, mantém-os frouxos.
- *Tight (T — apertado)* — comprime ADP e Pi tão próximos que se ligam *espontaneamente* (ΔG ≈ 0), formando ATP sem necessidade de input direto de energia.

A cada 120° de rotação do eixo γ, as 3 conformações *avançam* em sequência: o sítio que estava O vira L, o L vira T, e o T vira O (liberando ATP). Em uma volta completa (360°), cada sítio passa por todas as três conformações, e *3 ATPs são sintetizados* e liberados.

#mini-resumo[F₀ gira com o fluxo de H⁺; o eixo γ transmite rotação a F₁; cada 120° avança 1 dos 3 sítios catalíticos por O→L→T→O, sintetizando 3 ATPs por volta completa.]

O ponto que confunde quase todo aluno na primeira leitura é *onde está a energia no ciclo de Boyer*. Não é na formação química do ATP — essa é energeticamente neutra dentro do sítio T. *A energia da PMF é usada para forçar a mudança conformacional* que (1) prende ADP+Pi no sítio L, (2) comprime-os no sítio T até reagirem, e (3) abre o sítio O para liberar o ATP — esse último passo é o mais caro, porque o ATP recém-formado tem altíssima afinidade pelo sítio T e relutar para sair. *A rotação custa energia para abrir o sítio, não para ligar os fosfatos.*

Em humanos, com 8 subunidades c por anel F#sub[0], cada volta completa precisa de *8 prótons* e produz *3 ATPs*. Isso dá uma razão de 8/3 ≈ 2,7 H⁺ por ATP gerado no rotor. Quando se contam os custos adicionais de transporte (ADP/ATP translocase e fosfato carrier consomem 1 H⁺ por ATP exportado para o citosol), o total chega a cerca de *3,7 H⁺ por ATP citosólico*. Essa estequiometria é o que vai parametrizar o saldo de ATP no próximo subtópico.

#clinica-box("Oligomicina e o paradoxo do bloqueio que para tudo", [
  Oligomicina é um antibiótico que liga-se à subunidade F#sub[0] da ATP sintase e *bloqueia a passagem dos prótons*. À primeira vista, deveria bloquear *apenas* a síntese de ATP, deixando a cadeia respiratória funcionando livremente. Não é o que acontece: com a ATP sintase travada, os prótons não voltam para a matriz, e a PMF cresce ao máximo. Quando a PMF fica alta demais, os complexos da cadeia respiratória *param de bombear* (custo termodinâmico passa a ser proibitivo) — o gradiente já bombeado fica preso, e a cadeia entra em estagnação. *Bloqueia a sintase, para a cadeia em segundos, e o consumo de O#sub[2] cessa.* Esse é o chamado "controle respiratório" — a célula só respira o quanto precisa, e a precisão dessa regulação vem do ADP disponível para a sintase.
])

A confusão sutil aqui é achar que "a energia dos prótons forma a ligação química do ATP". Não — a *ligação química* forma-se espontaneamente no sítio T (ΔG ≈ 0). A energia da PMF é gasta para *liberar* o ATP do sítio aperto (que tem altíssima afinidade pelo produto). Sem energia para abrir o sítio, o ATP recém-sintetizado ficaria preso lá indefinidamente. Boyer demonstrou isso experimentalmente — a síntese química do ATP no sítio T acontece mesmo em mitocôndrias sem gradiente; o que para é a *liberação*. Foi essa observação contra-intuitiva que fechou a teoria.

#figura-nebli("/figuras/cadeia-respiratoria/slide-51.png",
  largura: 60%,
  legenda: [Modelo do binding change de Boyer. Os três sítios catalíticos (β1, β2, β3) ocupam as três conformações (O, L, T) simultaneamente. A rotação do eixo γ faz cada sítio "rolar" pela sequência O→L→T→O, sintetizando 1 ATP por sítio por volta = 3 ATP por volta completa.])

#subtopico("3.3 P/O, saldo final e lançadeiras")

Chegou a hora de fechar a conta. Quantos ATPs cada NADH gera? E cada FADH#sub[2]? E a glicose inteira, no fim?

A relação que sintetiza isso é o *P/O ratio* — quantos ATPs (P) são sintetizados por cada par de elétrons que reduz um átomo de O (1/2 O#sub[2]). Por décadas o número usado em livros didáticos foi *3 para NADH e 2 para FADH#sub[2]*. Esses são valores *clássicos*, calculados antes de se conhecer a estequiometria real de prótons por ATP. Hoje sabemos que os valores corretos são:

- *P/O do NADH = 2,5* (não 3).
- *P/O do FADH#sub[2] = 1,5* (não 2).

O cálculo é o seguinte. Um par de elétrons descendo pelo Complexo I bombeia 4 H⁺, pelo Complexo III bombeia 4 H⁺, e pelo Complexo IV bombeia 2 H⁺ — total *10 H⁺ por par* para o NADH. Dividindo por 3,7 H⁺ por ATP citosólico, dá *2,7 ATP*, que arredonda para *2,5* nos cálculos canônicos modernos. Já o FADH#sub[2], entrando pelo Complexo II, *pula o Complexo I*: bombeia só 4 + 2 = *6 H⁺ por par*, dividindo por 3,7 = *1,6*, arredonda para *1,5*.

A confusão clássica é insistir nos valores antigos. Em alguns livros mais conservadores, ainda se lê "3 ATP por NADH". Não está errado historicamente, mas hoje *o valor de referência é 2,5*. O importante para o aluno é entender *por que* a redução aconteceu: porque o número 3,7 H⁺/ATP (e não 3,0) refinou o cálculo. *O mecanismo continua o mesmo; o que mudou foi a estequiometria precisa do rotor F#sub[0].*

#figura-nebli("/figuras/cadeia-respiratoria/slide-55.png",
  largura: 55%,
  legenda: [Os valores modernos do P/O: 2,5 ATP por NADH (entrando pelo Complexo I) e 1,5 ATP por FADH₂ (entrando pelo Complexo II e bypassando o I). Diferença explicada pela ausência de bombeamento no Complexo II.])

Com esses valores na mão, o saldo da oxidação completa de 1 glicose fica assim. Da *glicólise* saem 2 ATP líquidos + 2 NADH (citosólicos). Da *conversão piruvato → acetil-CoA* saem 2 NADH (mitocondriais). Do *ciclo de Krebs* (2 voltas, uma por acetil-CoA) saem 6 NADH + 2 FADH#sub[2] + 2 GTP (= 2 ATP). Total: 4 ATP diretos + 10 NADH (8 mitocondriais + 2 citosólicos) + 2 FADH#sub[2].

Multiplicando: 4 ATP + (10 × 2,5) + (2 × 1,5) = 4 + 25 + 3 = *32 ATP por glicose*. Esse é o saldo moderno, supondo a lançadeira malato-aspartato (preserva os 2 NADH citosólicos como NADH mitocondriais).

Mas existe um detalhe que muda o número final: *o NADH citosólico não atravessa a membrana mitocondrial interna*. Ela é impermeável a ele. Para que esses elétrons cheguem à cadeia, a célula usa um truque chamado *lançadeira*. Há duas:

A *lançadeira malato-aspartato* (em fígado, rim e coração) transfere os elétrons do NADH citosólico para *outro NADH mitocondrial* via um par de transaminações que cruzam a membrana usando malato como veículo. O resultado é que o NADH citosólico chega à cadeia *como NADH*, rendendo 2,5 ATP — saldo total *32 ATP*.

A *lançadeira glicerol-3-P* (em músculo esquelético e cérebro) transfere os elétrons do NADH citosólico para *FADH#sub[2]* através de uma glicerol-3-P desidrogenase citoplasmática (usa NADH) acoplada a uma glicerol-3-P desidrogenase mitocondrial (gera FADH#sub[2] cravado na face externa da membrana interna). Os elétrons descem direto para a CoQ, *bypassando o Complexo I*. O NADH citosólico chega à cadeia *como FADH#sub[2]*, rendendo só 1,5 ATP — saldo total *30 ATP*.

#figura-nebli("/figuras/cadeia-respiratoria/slide-67.png",
  largura: 70%,
  legenda: [Lançadeira malato-aspartato — em fígado, rim e coração. NADH citosólico vira oxaloacetato + malato; malato cruza a membrana, é reoxidado a oxaloacetato dentro da matriz gerando NADH mitocondrial. Preserva equivalência redox total. Rendimento: 2,5 ATP por NADH original.])

#figura-nebli("/figuras/cadeia-respiratoria/slide-68.png",
  largura: 70%,
  legenda: [Lançadeira glicerol-3-P — em músculo esquelético e cérebro. NADH citosólico reduz diidroxiacetona-fosfato a glicerol-3-P; este é reoxidado por uma desidrogenase da membrana mitocondrial, que entrega elétrons direto à CoQ via FADH₂. Bypassa o Complexo I. Rendimento: 1,5 ATP por NADH original.])

#mini-resumo[P/O moderno: NADH = 2,5 ATP, FADH₂ = 1,5 ATP. Glicose = 32 ATP (malato-aspartato) ou 30 ATP (glicerol-3-P). A lançadeira muda o saldo porque define se o NADH citosólico chega como NADH ou como FADH₂.]

Vale a pena saber por que cada tecido usa uma lançadeira diferente. *Músculo esquelético em exercício* precisa de turnover rápido — não importa muito perder 2 ATPs por glicose se isso vier com a velocidade da glicerol-3-P (irreversível, rápida). *Fígado, rim e coração* têm metabolismo mais regulado e preferem a eficiência da malato-aspartato. *Cérebro* fica num meio-termo — usa principalmente glicerol-3-P em condições normais. Essas escolhas teciduais explicam por que, na clínica, o consumo de O#sub[2] por glicose varia tanto entre órgãos.

A confusão clássica aqui é dizer que o saldo é *sempre 38 ATP*. Esse número antigo combina valores P/O = 3 e P/O = 2 *sem* descontar custos de transporte. Hoje o saldo *real* fica entre 30 e 32. O importante não é decorar 30 ou 32; é entender que o número depende (1) dos valores P/O atualizados e (2) de qual lançadeira o tecido usa.

#subtopico("3.4 Inibidores, desacopladores e quadros clínicos")

A cadeia respiratória é tão central para a vida que substâncias capazes de interrompê-la são fortes venenos — ou, em alguns casos, ferramentas terapêuticas com janela terapêutica estreitíssima. Vamos organizar isso em duas categorias mecanísticas distintas: *inibidores* (que param a cadeia) e *desacopladores* (que deixam a cadeia rodar mas perdem o gradiente).

Os *inibidores* bloqueiam pontos específicos da cadeia. Os mais didáticos são:

- *Rotenona* (inseticida natural extraído de raízes) — bloqueia o Complexo I (sítio de transferência para a CoQ). Quando há rotenona, o NADH não consegue descarregar; os elétrons do FADH#sub[2] entrando pelo Complexo II ainda fluem (porque a CoQ ainda recebe deles), então o saldo de ATP cai drasticamente mas não a zero.
- *Antimicina A* (antibiótico de Streptomyces) — bloqueia o Complexo III, no sítio Q#sub[i]. Trava o ciclo Q. Para a transferência de elétrons da CoQ para o cit c.
- *Cianeto (CN⁻) e monóxido de carbono (CO)* — bloqueiam o Complexo IV, ligando-se ao heme a#sub[3]. Param toda a cadeia (efeito-cascata reverso descrito em 2.3).
- *Azida (N#sub[3]⁻)* — também bloqueia o Complexo IV, mecanismo similar ao cianeto.
- *Oligomicina* (antibiótico de Streptomyces) — não é tecnicamente um inibidor da cadeia, mas da *ATP sintase* (liga-se à subunidade F#sub[0]). Como já discutido, indiretamente para a cadeia ao saturar o gradiente.

#figura-nebli("/figuras/cadeia-respiratoria/slide-43.png",
  largura: 78%,
  legenda: [Locais de bloqueio dos principais inibidores: rotenona (Complexo I), antimicina (Complexo III), cianeto/CO (Complexo IV), oligomicina (ATP sintase). Cada inibidor cria uma assinatura experimental distinta de acúmulo de intermediários antes do ponto de bloqueio.])

Já os *desacopladores* são uma criatura diferente. Em vez de parar o transporte de elétrons, eles *destroem o gradiente* — criam um caminho alternativo para os prótons voltarem à matriz *sem passar pela ATP sintase*. O resultado é dramático: a cadeia respiratória continua bombeando (e até acelera, porque o gradiente não a freia mais), o O#sub[2] continua sendo consumido, mas a energia *vira calor* em vez de ATP. *Tudo o que era trabalho útil vira dissipação térmica.*

Os desacopladores clássicos são moléculas lipofílicas que carregam prótons. O *2,4-dinitrofenol (DNP)* foi usado nos anos 1930 como emagrecedor — funciona porque acelera o metabolismo (cadeia roda sem produzir ATP, então a célula queima mais combustível para repor o ATP que falta). Foi banido após mortes por hipertermia maligna; as doses terapêuticas e tóxicas estavam separadas por uma janela mínima. *Casos de uso ilegal recente continuam aparecendo em PS — paciente com sudorese profusa, taquicardia, hipertermia >40 °C, óbito em horas.*

O *#sigla("FCCP", [carbonilcianeto-p-trifluormetoxifenilhidrazona — desacoplador sintético usado em pesquisa para colapsar o gradiente de prótons na mitocôndria]) (carbonilcianeto-p-trifluormetoxifenilhidrazona)* é um desacoplador sintético usado em pesquisa para colapsar o gradiente experimentalmente.

#clinica-box("DNP — quando o desacoplamento mata", [
  O 2,4-dinitrofenol foi aprovado como emagrecedor nos EUA em 1933 e retirado em 1938 após relatos de hipertermia letal, cataratas (toxicidade do cristalino), agranulocitose e neuropatia. Ainda hoje aparece em sites obscuros de fisiculturismo. O paciente intoxicado chega com hipertermia >40 °C, taquicardia, sudorese profusa, hiperventilação compensatória (para tentar perder calor), e progride para falência multi-orgânica. *Não há antídoto específico* — manejo é resfriamento agressivo, suporte hemodinâmico, dantroleno em alguns casos. Mortalidade alta mesmo com tratamento.
])

Mas existe um desacoplador *fisiológico* — e ele é crucial. A *#sigla("UCP1", [uncoupling protein 1, ou termogenina — desacoplador fisiológico do tecido adiposo marrom; cria caminho regulado para retorno de prótons, gerando calor sob ativação simpática]) (uncoupling protein 1)*, também chamada *#termo-nota[termogenina][nome alternativo da UCP1; proteína desacopladora do tecido adiposo marrom que gera calor por desacoplamento controlado da cadeia respiratória, ativada por norepinefrina via β3-adrenérgico]*, é uma proteína da membrana mitocondrial interna que cria um canal regulado para prótons voltarem à matriz *sem* passar pela ATP sintase. Está presente no *tecido adiposo marrom*, abundante em neonatos e (descoberta surpreendente da última década) também em humanos adultos.

O mecanismo é elegante. Norepinefrina liberada por terminais simpáticos no frio liga-se a receptores β#sub[3]-adrenérgicos do adipócito marrom; isso ativa lipólise, gera ácidos graxos livres que ativam UCP1; UCP1 abre o canal; prótons voltam dissipando o gradiente; cadeia acelera consumindo O#sub[2]; *energia química vira calor*. Esse processo é chamado *termogênese sem tremor* (ou termogênese não-shivering), e é vital para neonatos, que não tremem como adultos e dependem do tecido adiposo marrom para se manterem aquecidos nos primeiros dias de vida.

Em adultos, a redescoberta de tecido adiposo marrom funcional (em pescoço, ombros, adjacente à coluna torácica) abriu uma nova fronteira terapêutica — *ativar UCP1 para queimar calorias*. Estudos com exposição ao frio mostram aumento de gasto energético basal em até 15%. Drogas que ativam β#sub[3]-adrenérgicos seletivamente estão em desenvolvimento para obesidade, embora os primeiros candidatos tenham esbarrado em efeitos cardiovasculares.

#mini-resumo[Inibidores param a cadeia (CN, CO, rotenona, antimicina, oligomicina). Desacopladores deixam a cadeia rodar mas dissipam o gradiente como calor (DNP tóxico, FCCP de pesquisa, UCP1 fisiológica em adiposo marrom).]

Vale separar bem inibidor de desacoplador, porque o quadro clínico é radicalmente diferente. *Inibidor*: cadeia para, consumo de O#sub[2] cai a zero, sem ATP, sem calor extra — o paciente entra em hipóxia tecidual aguda (cianeto, CO). *Desacoplador*: cadeia acelera, consumo de O#sub[2] sobe muito, sem ATP, calor enorme — o paciente entra em hipertermia maligna (DNP, "ecstasy" em superdose também tem componente desacoplador via mitocondria neuronal).

Por fim, o *controle respiratório*. A cadeia não roda no máximo o tempo todo — ela é regulada pelo ADP disponível. Se há ADP livre na matriz, a ATP sintase usa-o, prótons voltam, gradiente diminui ligeiramente, cadeia bombeia para repor. Se ADP acaba (porque a célula está em repouso e o ATP não está sendo gasto), a sintase trava, o gradiente cresce, e a cadeia *para por retroinibição termodinâmica*. *O sinal-chave da regulação é o ADP*, não enzimas alostéricas complicadas. Auto-regulação pelo estado energético, direta. Por isso a célula em exercício respira mais (mais ATP gasto → mais ADP livre → cadeia acelera) e em repouso respira menos.

#clinica-box("Miopatias mitocondriais e o limite de ATP", [
  Doenças por mutações em proteínas da cadeia (NADH desidrogenase, citocromos, ATP sintase) ou no DNA mitocondrial (mtDNA) levam a *miopatias mitocondriais*: fraqueza muscular progressiva, intolerância ao exercício, ptose, oftalmoplegia, cardiomiopatia. Como músculo e neurônio são os tecidos mais dependentes de ATP, são os mais afetados. Exemplos: MELAS (encefalomiopatia, acidose lática, episódios stroke-like), MERRF (epilepsia mioclônica, ragged-red fibers), Leber (neuropatia óptica). Biópsia muscular mostra *ragged-red fibers* — mitocôndrias subsarcolemais empilhadas em compensação. Acidose lática crônica reflete o fluxo aumentado pela glicólise tentando suprir o déficit de ATP da cadeia.
])

#conclusao-box[
  *O princípio unificador* atravessa as três PARTES: a célula não consegue capturar a energia da oxidação completa de NADH/FADH#sub[2] num único passo, então fraciona — em ~10 transferências sequenciais, cada uma de magnitude termodinâmica controlada, cada uma acoplada ao bombeamento de prótons. O resultado dessa engenharia é a *força próton-motriz*, que finalmente vira ATP por meio de uma máquina rotatória.

  *O mecanismo nuclear* é o acoplamento via gradiente: a cadeia respiratória bombeia prótons da matriz para o espaço intermembranas; a ATP sintase usa o retorno desses prótons para girar e sintetizar ATP por mudança conformacional dos seus três sítios catalíticos. Os dois processos não tocam um no outro diretamente — a ponte entre eles é, literalmente, o desbalanço eletroquímico através da membrana interna.

  *Na clínica*, a consequência dessa arquitetura aparece em todas as suas vulnerabilidades. Cianeto liga-se ao Complexo IV e mata em minutos por hipóxia histotóxica — o sangue volta vermelho-cereja porque o O#sub[2] não foi consumido. O 2,4-dinitrofenol, desacoplador histórico, dissipa o gradiente como calor e mata por hipertermia maligna. A UCP1 do tecido adiposo marrom usa o mesmo mecanismo — só que regulado — para manter o neonato aquecido sem tremer.

  *O que segue daqui* é a integração com o restante do metabolismo. A cadeia respiratória é o destino final dos elétrons de toda via catabólica aeróbica — glicólise (via lançadeiras), ciclo de Krebs, β-oxidação, oxidação de aminoácidos. Cada NADH e cada FADH#sub[2] produzidos rendem ATP nessa estação terminal. Entender a cadeia é entender por que a respiração celular é tão mais eficiente que a fermentação, e por que tecidos altamente metabólicos (coração, cérebro, músculo em exercício) são tão dependentes dessa máquina molecular.
]

#mindmap-fechamento(
  tema: "CADEIA RESPIRATÓRIA",
  mensagem: "fracionar a oxidação em ~10 passos pequenos cria gradiente de prótons, que gira a ATP sintase e produz ATP — sem fracionamento, só calor",
  com-setas: true,
  estacoes: (
    (rotulo: "Combustível redutor · NADH e FADH₂",
     titulo: "Portas de entrada I e II",
     fala: [NADH entra no Complexo I (bombeia 4 H⁺), FADH₂ entra no II (não bombeia) — daí a diferença de saldo],
     cor: "a"),
    (rotulo: "Quimiosmose · PMF ~200 mV",
     titulo: "Bombeamento e gradiente",
     fala: [III bombeia 4 H⁺ pelo ciclo Q, IV bombeia 2 H⁺ reduzindo O₂ a H₂O — gradiente acumula como represa],
     cor: "neutra", destaque: true),
    (rotulo: "Síntese · ATP sintase F₀F₁",
     titulo: "Rotação e binding change",
     fala: [F₀ gira com fluxo de H⁺, F₁ alterna sítios O→L→T→O sintetizando 3 ATPs por volta — 8 H⁺ por volta],
     cor: "b"),
  ),
  rodape-titulo: "Saldo · controle · clínica",
  cartoes: (
    (titulo: "Quanto ATP rende",
     frase: [P/O moderno: 2,5 por NADH, 1,5 por FADH₂. Glicose = 32 (malato-aspartato) ou 30 (glicerol-3-P)]),
    (titulo: "Quem manda na velocidade",
     frase: [ADP é o sinal — sem ADP, sintase trava, gradiente sobe, cadeia para por retroinibição]),
    (titulo: "Onde mata ou aquece",
     frase: [cianeto trava IV (hipóxia histotóxica), DNP desacopla (hipertermia), UCP1 desacopla regulado (calor no neonato)]),
  ),
)
