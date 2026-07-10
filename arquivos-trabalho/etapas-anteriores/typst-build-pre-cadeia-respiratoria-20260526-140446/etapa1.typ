#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Você acabou de fechar a glicólise. Saiu do citosol com duas moléculas de #sigla("ATP", [adenosina trifosfato — a "moeda" energética da célula, paga e recebida em cada reação que importa]), duas moléculas de #sigla("NADH", [nicotinamida adenina dinucleotídeo, forma reduzida — carrega 2 elétrons de alta energia até a cadeia respiratória]) e — o que vai dominar este resumo — duas moléculas de piruvato. O piruvato ainda guarda boa parte da energia original da glicose: três carbonos cheios de elétrons que ninguém colheu ainda.

  Daqui pra frente o jogo muda de endereço. A célula vai mover o piruvato do citosol para dentro da mitocôndria, transformar em #termo-nota[acetil-CoA][molécula de 2 carbonos ligada à coenzima A por uma ligação tioéster de alta energia; é o substrato real do ciclo, não o piruvato], e mandar essa molécula entrar numa engrenagem de oito reações em sequência — o *ciclo de Krebs*. A cada volta, o ciclo arranca todos os elétrons que sobravam, joga fora os dois carbonos como #sigla("CO₂", [dióxido de carbono — produto final da oxidação completa de carbono orgânico]) e devolve a engrenagem ao ponto inicial pronta para receber a próxima acetila.

  Este resumo segue uma regra rígida: *toda vez* que mencionarmos uma enzima ou um intermediário, vamos identificar a posição dele dentro do ciclo — "*passo 3*", "entre os *passos 7 e 8*", "*passo 0* (que é a entrada, anterior aos oito)". A ideia é que, ao terminar, você consiga responder qualquer pergunta de identificação sem precisar consultar nada. E, ao final da PARTE II, uma tabela-síntese consolida todas as 8 reações lado a lado.
]

#parte-title("PARTE I — Antes do ciclo: o piruvato precisa entrar", primeira: true)

== 1.1 — Por que existe o ciclo e onde ele roda

Pare por um segundo e pense no piruvato. Ele tem 3 carbonos, ainda totalmente reduzidos, e está flutuando no citosol depois que a glicólise terminou. A célula colheu 2 ATP daquela primeira fase — pouco, comparado ao que existe ali em potencial energético. Para extrair o resto, ela precisa fazer duas coisas em sequência: (a) levar o piruvato para dentro da #termo-nota[mitocôndria][organela com membrana dupla; a interna dobra-se em cristas e abriga toda a maquinaria do Krebs e da cadeia respiratória], onde mora a maquinaria oxidativa, e (b) submetê-lo a uma série de reações que vão arrancar seus elétrons um a um e enviar para uma fila de transportadores que terminam usando #sigla("O₂", [oxigênio molecular — aceptor final dos elétrons na cadeia respiratória]) como aceptor final.

A travessia da membrana mitocondrial interna não é trivial: ela é praticamente impermeável a íons e moléculas polares. O piruvato atravessa por um transportador específico — o transportador de monocarboxilato, #sigla("MPC", [mitochondrial pyruvate carrier — transportador específico que move piruvato do espaço intermembrana para a matriz, em simporte com H⁺]).

#figura-nebli("/figuras/ciclo-krebs/slide-06.png",
  largura: 70%,
  legenda: [Do citosol para a matriz mitocondrial. A glicose virou 2 piruvatos; cada um precisa atravessar duas membranas (externa, livremente permeável; interna, via MPC) para encontrar a maquinaria do ciclo.])

Uma vez na matriz, o piruvato encontra dois universos diferentes: o complexo da piruvato desidrogenase, que vai convertê-lo em acetil-CoA (o "*passo 0*" — anterior aos oito do ciclo propriamente dito), e o próprio ciclo de Krebs, com suas oito enzimas. *Praticamente todas as enzimas do ciclo moram dissolvidas na matriz mitocondrial*. A única exceção — guarde isso desde já, porque a confusão é clássica — é a *succinato desidrogenase*, que catalisa o *passo 6* e está embutida na membrana mitocondrial interna. Ela mora ali porque é, ao mesmo tempo, o Complexo II da cadeia respiratória. Vamos voltar nesse ponto.

== 1.2 — PDH: o "passo 0", a porta de entrada

Antes de qualquer das oito reações começarem, o piruvato precisa virar acetil-CoA. Essa conversão é feita por uma máquina complicadíssima, o *complexo da piruvato desidrogenase* — #sigla("PDH", [piruvato desidrogenase — complexo multienzimático mitocondrial que catalisa a descarboxilação oxidativa do piruvato em acetil-CoA, NADH e CO₂]). Chamamos de "passo 0" porque ele *prepara* o substrato do ciclo, mas não é uma das 8 reações canônicas.

A PDH é um #termo-nota[complexo multienzimático][agregado de três ou mais enzimas que catalisam uma sequência de reações sem liberar os intermediários — eles passam de um sítio ativo para o vizinho sem se desprender]: três enzimas diferentes (E1, E2 e E3) e cinco coenzimas (tiamina pirofosfato, ácido lipoico, FAD, NAD⁺ e CoA-SH). A vantagem do arranjo é cinética: o intermediário que sai do sítio de E1 já é "abocanhado" por E2, sem dispersar pela matriz. Funciona como uma esteira de montagem.

#figura-nebli("/figuras/ciclo-krebs/slide-08.png",
  largura: 75%,
  legenda: [Descarboxilação oxidativa do piruvato — o "passo 0". A PDH retira um carbono do piruvato como CO₂, transfere os dois carbonos restantes para a coenzima A formando acetil-CoA, e reduz 1 NAD⁺ a NADH.])

A reação líquida é:

#align(center, text(size: 11pt)[
  piruvato + CoA-SH + NAD⁺ → acetil-CoA + CO₂ + NADH + H⁺
])

Três coisas importantes acontecem aqui. *Primeira*: perdemos um carbono na forma de CO₂ — saímos de 3 carbonos (piruvato) e vamos entrar no ciclo com 2 carbonos (acetila). *Segunda*: já ganhamos 1 NADH, antes mesmo de o ciclo começar. *Terceira*: a acetila é "ativada" pela ligação tioéster ao enxofre da coenzima A; essa ligação carrega energia comparável à do ATP, e essa energia será aproveitada no *passo 1* do ciclo.

#figura-nebli("/figuras/ciclo-krebs/slide-17.png",
  largura: 70%,
  legenda: [Detalhe das três enzimas da PDH (E1 com TPP, E2 com lipoato, E3 com FAD) e do trânsito dos intermediários sem liberação. Cinco coenzimas atuam em sequência.])

A PDH é regulada com firmeza: fosforilação por #sigla("PDK", [piruvato desidrogenase quinase — fosforila e inativa a PDH quando a célula está bem alimentada]) a inativa quando há excesso de ATP ou NADH (sinal de "não precisa de mais combustível"); desfosforilação por #sigla("PDP", [piruvato desidrogenase fosfatase — remove o fosfato e reativa a PDH em resposta a Ca²⁺ e insulina]) a reativa quando o estoque cai. Insulina ativa indiretamente (estímulo anabólico), e cálcio (sinal de contração muscular) também ativa. A reação é *irreversível* — uma vez feita acetila, não dá pra voltar a piruvato. É por isso que o organismo não consegue fazer glicose a partir de acetil-CoA, e por isso que ácidos graxos puros não viram glicose. Esse ponto vai ser fundamental quando você estudar gliconeogênese.

== 1.3 — O acetil-CoA é o substrato real do ciclo (não o piruvato)

Quero esclarecer agora um ponto que confunde *todo mundo* na primeira leitura: o ciclo de Krebs *não oxida piruvato*. Ele oxida acetil-CoA. O piruvato fica do lado de fora do ciclo, "pendurado" no PDH. Quem entra na engrenagem do *passo 1* é a acetila de 2 carbonos.

Por que isso importa? Porque acetil-CoA *não vem só do piruvato*. Ele também aparece quando você degrada ácidos graxos (β-oxidação, tema futuro), aminoácidos cetogênicos e até corpos cetônicos no jejum prolongado. Qualquer combustível, vindo de qualquer lugar, *se converge para acetil-CoA* antes de entrar no ciclo. Por isso o ciclo de Krebs é o *hub central do metabolismo*: tudo passa por aqui.

#confusao-prevista(
  titulo: "O ciclo não 'queima glicose' — queima acetila",
  aluno_acha: [muitos alunos acham que o ciclo de Krebs trabalha em cima do piruvato ou da glicose diretamente.],
  mecanismo: [o substrato é *acetil-CoA*, que veio do piruvato via PDH (*passo 0*), mas pode vir de qualquer fonte — gordura, aminoácido, corpo cetônico. O ciclo é cego para a origem; só vê os 2 carbonos da acetila.],
)

Agora a engrenagem está pronta. Acetil-CoA na mão, oito reações pela frente. Vamos numerar passo a passo.

#parte-title("PARTE II — As 8 reações em sequência: o ciclo passo a passo")

Antes de entrarmos nos passos individuais, fique com esta imagem do slide do professor. Ela é a planta-baixa do ciclo inteiro — vamos voltar nela mentalmente toda vez que falarmos de um passo específico.

#figura-nebli("/figuras/ciclo-krebs/slide-04.png",
  largura: 80%,
  legenda: [Os 8 passos do ciclo de Krebs, com indicação de cofatores reduzidos e CO₂ liberado em cada um. Esta figura é o "mapa" do resumo inteiro — toda menção a "*passo N*" se refere a uma posição aqui.])

== 2.1 — Passos 1 e 2: condensação e isomerização

*Passo 1 — citrato sintase.* A acetila (2 carbonos) bate na #termo-nota[oxaloacetato][intermediário de 4 carbonos que recebe a acetila no passo 1 e é regenerado no passo 8 — sem ele, o ciclo para] (4 carbonos), e a enzima cataliza a condensação. O resultado é o *citrato*, uma molécula de 6 carbonos. A energia para essa condensação vem da quebra da ligação tioéster da acetil-CoA — lembra que a gente disse que ela carregava energia como um ATP? Pois é, aqui se gasta. A reação é fortemente *exergônica* e *irreversível*; é o primeiro ponto regulado do ciclo, inibida por ATP, NADH, succinil-CoA e citrato (todos sinais de "tem combustível sobrando").

#figura-nebli("/figuras/ciclo-krebs/slide-18.png",
  largura: 60%,
  legenda: [Passo 1: acetil-CoA + OAA → citrato + CoA-SH. A ligação tioéster da acetila se quebra; sua energia paga a condensação.])

*Passo 2 — aconitase.* O citrato é uma molécula simétrica com hidroxila no carbono *terciário*. O problema: carbono terciário não pode ser oxidado (não tem hidrogênio no carbono que carrega a OH). Para o ciclo conseguir extrair elétrons mais à frente, a hidroxila precisa migrar para um carbono *secundário*. É isso que a *aconitase* faz: ela isomeriza citrato em *isocitrato*, passando por um intermediário desidratado (cis-aconitato) que é re-hidratado em posição diferente. Sem cofator, sem oxidação — apenas um rearranjo geométrico que prepara o terreno para o *passo 3*.

#figura-nebli("/figuras/ciclo-krebs/slide-20.png",
  largura: 55%,
  legenda: [Passo 2: a aconitase remove uma água do citrato e devolve em posição diferente — citrato vira isocitrato, com a hidroxila agora no carbono que pode ser oxidado.])

Inibidor clássico da aconitase: *fluoroacetato*. Veneno usado em rodenticidas. Uma vez no organismo, é convertido a fluorocitrato, que se liga irreversivelmente à aconitase e *trava o ciclo no passo 2*. Sem o passo 2, todo o resto pára — Krebs em parada cardíaca metabólica. Dose letal: 2–10 mg/kg em humanos.

== 2.2 — Passos 3 e 4: as duas descarboxilações

Aqui chegam as duas reações que perdem carbono. *Lembrem-se*: você entrou no *passo 1* com 6 carbonos (acetila 2C + OAA 4C → citrato 6C). Você precisa sair com 4 carbonos no fim do ciclo (regenerar OAA). Onde foram os 2 carbonos perdidos? Aqui, nos *passos 3 e 4*. Cada um joga 1 carbono fora como CO₂.

*Passo 3 — isocitrato desidrogenase (IDH).* Isocitrato → α-cetoglutarato + #sigla("NAD⁺", [nicotinamida adenina dinucleotídeo, forma oxidada — recebe 2 elétrons e 1 H⁺ formando NADH]) reduz a NADH + CO₂. *Primeiro NADH do ciclo. Primeiro CO₂ do ciclo.* Esta é a reação que define a velocidade do ciclo inteiro — o "marco-passo". Ativada alostericamente por *ADP* e *Ca²⁺* (sinais de demanda energética), inibida por ATP e NADH. Quando você corre, o cálcio que sai do retículo sarcoplasmático ativa a IDH em tempo real, acelerando o ciclo para fornecer cofatores reduzidos à cadeia respiratória.

#figura-nebli("/figuras/ciclo-krebs/slide-22.png",
  largura: 65%,
  legenda: [Passo 3: primeira oxidação. Isocitrato desidrogenase remove 2 elétrons (vão para NAD⁺) e descarboxila (sai 1 CO₂). Produto: α-cetoglutarato, 5 carbonos.])

*Passo 4 — α-cetoglutarato desidrogenase (α-KG-DH).* α-cetoglutarato + NAD⁺ + CoA-SH → succinil-CoA + CO₂ + NADH. *Segundo NADH. Segundo CO₂.* E aqui mora uma das armadilhas mais comuns: a α-KG-DH *não é uma enzima única*. É um *complexo multienzimático*, com exatamente o mesmo arranjo da PDH do *passo 0* (três enzimas, cinco coenzimas — TPP, lipoato, FAD, NAD⁺, CoA). Mecanisticamente, é PDH com substrato diferente. Inibida por NADH e succinil-CoA (sinais de que o ciclo já produziu bastante).

#figura-nebli("/figuras/ciclo-krebs/slide-25.png",
  largura: 65%,
  legenda: [Passo 4: segunda oxidação. α-KG-DH é arquiteturalmente idêntica à PDH; transfere 2 elétrons ao NAD⁺ e prende o que sobrou em uma nova ligação tioéster com CoA, gerando succinil-CoA.])

#atencao-box("α-cetoglutarato desidrogenase é um COMPLEXO, não uma enzima",
  [No PDH (*passo 0*) e na α-KG-DH (*passo 4*) os alunos tendem a marcar "enzima única". Ambos são *complexos multienzimáticos* com 3 enzimas e 5 coenzimas idênticas. A diferença é só o substrato (piruvato vs α-cetoglutarato). Deficiência de *tiamina* paralisa os dois ao mesmo tempo — quadro clínico do *beriberi* e da encefalopatia de Wernicke.])

Saímos do *passo 4* com *succinil-CoA*, uma molécula de 4 carbonos (já perdemos os 2 carbonos como CO₂) com uma ligação tioéster de alta energia.

== 2.3 — Passo 5: GTP em nível de substrato

*Passo 5 — succinil-CoA sintetase.* Succinil-CoA + GDP + Pi → succinato + #sigla("GTP", [guanosina trifosfato — equivalente energético do ATP, intercambiável por nucleosídeo difosfato quinase]) + CoA-SH. Aqui acontece um fenômeno especial: a energia da quebra da ligação tioéster (que veio lá do *passo 4*, ou ainda mais de trás, da carga original da acetil-CoA no *passo 0*) é usada para fosforilar GDP em GTP. Isso é #termo-nota[fosforilação em nível de substrato][formação de ATP ou GTP diretamente da quebra de um substrato fosforilado ou de alta energia, *sem* envolver a cadeia respiratória ou O₂ — independente da fosforilação oxidativa].

#figura-nebli("/figuras/ciclo-krebs/slide-26.png",
  largura: 65%,
  legenda: [Passo 5: fosforilação em nível de substrato. A energia da ligação tioéster paga a fosforilação de GDP em GTP. GTP é depois convertido em ATP por nucleosídeo difosfato quinase (NDP-K).])

O GTP é rapidamente convertido a ATP pela nucleosídeo difosfato quinase:

#align(center, text(size: 11pt)[GTP + ADP ⇌ GDP + ATP])

Este é o *único* ATP "puro" gerado dentro do ciclo de Krebs — todos os outros vão sair indiretamente, quando NADH e FADH₂ chegarem na cadeia respiratória. E porque é em nível de substrato, este GTP/ATP do *passo 5* *continua sendo gerado* mesmo se a cadeia respiratória estiver bloqueada (por desacoplador como o 2,4-DNP, ou por inibidor de ATP-sintase como oligomicina). Esse ponto é frequentemente cobrado — vamos voltar nele.

== 2.4 — Passo 6: FADH₂ na membrana (e a confusão clássica do FAD)

*Passo 6 — succinato desidrogenase (SDH).* Succinato + #sigla("FAD", [flavina adenina dinucleotídeo — coenzima que recebe 2 elétrons e 2 H⁺ formando FADH₂; usado por desidrogenases ligadas à membrana]) → fumarato + #sigla("FADH₂", [forma reduzida do FAD — carrega elétrons direto para a ubiquinona da cadeia respiratória]). Esta é a única reação do ciclo que *não* usa NAD⁺. Por quê? Porque a *succinato desidrogenase é também o Complexo II da cadeia respiratória*: ela é uma proteína embutida na membrana mitocondrial interna, com FAD ligado covalentemente, que entrega os elétrons direto à ubiquinona — sem precisar de um transportador solúvel intermediário.

#figura-nebli("/figuras/ciclo-krebs/slide-29.png",
  largura: 60%,
  legenda: [Passo 6: o único na membrana. SDH = Complexo II. FAD aceita 2 elétrons na forma de 2 átomos de hidrogênio, vira FADH₂, e passa os elétrons direto para a ubiquinona da cadeia.])

#atencao-box("O passo 6 produz FADH₂, não NADH",
  [Esta é a armadilha de contagem mais frequente. O aluno conta "tem 4 desidrogenases, então 4 NADH". Erro. O *passo 6* (SDH) usa FAD, não NAD⁺. O ciclo gera *3 NADH* (passos 3, 4 e 8) + *1 FADH₂* (passo 6). Quem contar 4 NADH errou a totalização do saldo energético — confusão clássica do conteúdo.])

Por que o *passo 6* foi escolhido para usar FAD em vez de NAD⁺? Termodinâmica. A oxidação de succinato → fumarato tem ΔG° próximo de zero. NAD⁺ é um oxidante "forte demais" — não consegue arrancar elétrons aqui. FAD aceita elétrons em potencial menor, viabilizando a reação. Como bônus, o FAD já está pendurado na membrana, no Complexo II, perto da ubiquinona — entrega expressa.

== 2.5 — Passos 7 e 8: fechando o ciclo

*Passo 7 — fumarase.* Fumarato + H₂O → malato. Simples hidratação, sem cofator, sem perda de carbono. Adiciona uma molécula de água através da dupla ligação do fumarato. A enzima é estereoespecífica: produz apenas L-malato.

*Atenção a esta armadilha*: quando o aluno lista os intermediários do ciclo de cabeça, é comum pular o malato — escrever "succinato → fumarato → oxaloacetato" e esquecer que o malato está entre os *passos 7 e 8*. A sequência correta dos quatro últimos intermediários é *succinato → fumarato → malato → OAA*.

*Passo 8 — malato desidrogenase (MDH).* Malato + NAD⁺ → oxaloacetato + NADH. *Terceiro NADH do ciclo.* O ciclo fechou — voltamos ao OAA, pronto para receber a próxima acetila no *passo 1*.

Curiosidade termodinâmica: esta reação tem ΔG° *positivo* (+29 kJ/mol). Em condições padrão, ela rodaria *ao contrário*. Por que roda no sentido direto na célula? Porque o OAA é *consumido em tempo real* pela citrato sintase do *passo 1* — sua concentração intracelular é mantida muito baixa, e o princípio de Le Chatelier puxa a MDH para frente. É um exemplo lindo de como uma via metabólica pode "forçar" uma reação termodinamicamente desfavorável pelo simples expediente de remover o produto à medida que ele se forma.

== 2.6 — Tabela-síntese: as 8 reações no raio-X

Toda informação dos passos 1 a 8 (mais o *passo 0* da PDH) consolidada em uma tabela. Esta é a folha que você consulta direto na hora de revisar.

#align(center)[
  #table(
    columns: (auto, 1fr, 1.4fr, 1.1fr, 1.5fr),
    align: (center + horizon, left + horizon, left + horizon, left + horizon, left + horizon),
    stroke: 0.5pt + gray-border,
    fill: (col, row) => if row == 0 { navy },
    table.header(
      text(fill: white, weight: "bold", size: 9pt)[Passo],
      text(fill: white, weight: "bold", size: 9pt)[Enzima],
      text(fill: white, weight: "bold", size: 9pt)[Substrato → Produto],
      text(fill: white, weight: "bold", size: 9pt)[Energia/Cofator],
      text(fill: white, weight: "bold", size: 9pt)[Nota],
    ),
    text(size: 8.5pt)[*0*],
    text(size: 8.5pt)[Complexo PDH],
    text(size: 8.5pt)[piruvato → acetil-CoA],
    text(size: 8.5pt)[+1 NADH, −1 CO₂],
    text(size: 8.5pt)[entrada; complexo multienzimático; irreversível],

    text(size: 8.5pt)[*1*],
    text(size: 8.5pt)[Citrato sintase],
    text(size: 8.5pt)[acetil-CoA + OAA → citrato],
    text(size: 8.5pt)[—],
    text(size: 8.5pt)[irreversível; regulada (ATP, NADH, citrato inibem)],

    text(size: 8.5pt)[*2*],
    text(size: 8.5pt)[Aconitase],
    text(size: 8.5pt)[citrato → isocitrato],
    text(size: 8.5pt)[—],
    text(size: 8.5pt)[isomerização; inibida por fluoroacetato (veneno)],

    text(size: 8.5pt)[*3*],
    text(size: 8.5pt)[Isocitrato desidrog. (IDH)],
    text(size: 8.5pt)[isocitrato → α-cetoglutarato],
    text(size: 8.5pt)[+1 NADH, −1 CO₂],
    text(size: 8.5pt)[*marco-passo*; ativada por ADP/Ca²⁺],

    text(size: 8.5pt)[*4*],
    text(size: 8.5pt)[α-KG desidrog. (α-KG-DH)],
    text(size: 8.5pt)[α-cetoglutarato → succinil-CoA],
    text(size: 8.5pt)[+1 NADH, −1 CO₂],
    text(size: 8.5pt)[complexo multienzimático (= PDH em mecanismo)],

    text(size: 8.5pt)[*5*],
    text(size: 8.5pt)[Succinil-CoA sintetase],
    text(size: 8.5pt)[succinil-CoA → succinato],
    text(size: 8.5pt)[+1 GTP (≈ATP)],
    text(size: 8.5pt)[*fosforilação em nível de substrato* — única do ciclo],

    text(size: 8.5pt)[*6*],
    text(size: 8.5pt)[Succinato desidrog. (SDH)],
    text(size: 8.5pt)[succinato → fumarato],
    text(size: 8.5pt)[+1 *FADH₂*],
    text(size: 8.5pt)[*única na membrana* = Complexo II da cadeia],

    text(size: 8.5pt)[*7*],
    text(size: 8.5pt)[Fumarase],
    text(size: 8.5pt)[fumarato → malato],
    text(size: 8.5pt)[—],
    text(size: 8.5pt)[hidratação; produz L-malato],

    text(size: 8.5pt)[*8*],
    text(size: 8.5pt)[Malato desidrog. (MDH)],
    text(size: 8.5pt)[malato → OAA],
    text(size: 8.5pt)[+1 NADH],
    text(size: 8.5pt)[ΔG > 0; puxada pelo consumo de OAA no *passo 1*],
  )
]

#mini-resumo[
  *Saldo por volta do ciclo (passos 1 a 8, sem contar o passo 0):* 3 NADH (passos 3, 4 e 8) + 1 FADH₂ (passo 6) + 1 GTP (passo 5) + 2 CO₂ (passos 3 e 4). Se incluirmos a PDH (passo 0), o piruvato como um todo gera mais 1 NADH e mais 1 CO₂ — fechando 4 NADH + 1 FADH₂ + 1 GTP + 3 CO₂ por piruvato. Como cada glicose vira *2 piruvatos*, multiplique tudo por 2 para ter o saldo por glicose.
]

#parte-title("PARTE III — Saldo, regulação e anfibolismo: o ciclo no contexto")

== 3.1 — Saldo energético: por volta e por glicose

Agora vamos transformar os cofatores reduzidos em ATP. Lembre-se: NADH e FADH₂ não são ATP — eles vão *alimentar* a cadeia respiratória, que faz a fosforilação oxidativa propriamente dita. As equivalências aceitas hoje (baseadas em estequiometria de bombeamento de prótons) são:

#align(center, text(size: 11pt)[1 NADH ≈ 2.5 ATP · · · · 1 FADH₂ ≈ 1.5 ATP])

Aplicando ao saldo por volta do ciclo:
- 3 NADH × 2.5 = 7.5 ATP
- 1 FADH₂ × 1.5 = 1.5 ATP
- 1 GTP (direto, passo 5) = 1 ATP
- *Total por volta: 10 ATP*

Por *piruvato* completo (incluindo o passo 0, PDH): + 1 NADH × 2.5 = 12.5 ATP por piruvato. Por glicose (= 2 piruvatos): 25 ATP só desta etapa. Somando glicólise (2 ATP diretos + 2 NADH citosólicos que viram 3–5 ATP dependendo da lançadeira): saldo total da oxidação completa da glicose oscila entre *30 e 32 ATP*. A oscilação vem das duas lançadeiras possíveis para os NADH gerados no citosol pela glicólise — *malato-aspartato* (rende 2.5 ATP, usada em fígado/coração) ou *glicerol-3-fosfato* (rende 1.5 ATP, usada em músculo esquelético/cérebro).

== 3.2 — Regulação: onde se aperta e por quê

O ciclo é regulado em três pontos principais — e adivinha quais são? Os três passos *irreversíveis*: *1, 3 e 4*. Faz sentido: você regula onde a reação não tem volta, porque controlar uma reação reversível seria como fechar uma porta giratória.

- *Passo 1 (citrato sintase):* inibida por ATP, NADH, succinil-CoA, citrato. Todos sinais de "estoque cheio".
- *Passo 3 (IDH):* o regulador-chave. Inibida por ATP e NADH; *ativada por ADP e Ca²⁺*. O cálcio é o sinal de demanda muscular em tempo real — quando o músculo contrai, o cálcio que sai do retículo sarcoplasmático ativa a IDH instantaneamente, acelerando o ciclo.
- *Passo 4 (α-KG-DH):* inibida por NADH e succinil-CoA. Sensível a Ca²⁺ também.

A lógica é unificada: *carga energética alta freia, carga baixa solta, cálcio acelera*. O ciclo "sente" o estado da célula através das razões ATP/ADP e NADH/NAD⁺ — exatamente as moléculas que ele produz.

== 3.3 — Anfibolismo: Krebs não é só catabólico

Aqui está uma das ideias mais bonitas do metabolismo. O ciclo de Krebs *não serve só para degradar* — ele também é *fonte de matéria-prima para construir*. Por isso chamamos de via #termo-nota[anfibolismo][propriedade de uma via metabólica de funcionar tanto na degradação (catabolismo) quanto na construção (anabolismo) de moléculas — Krebs é o exemplo paradigmático].

#figura-nebli("/figuras/ciclo-krebs/slide-39.png",
  largura: 78%,
  legenda: [Funções anfibólicas do ciclo. Intermediários saem (cataplerose) para biossíntese; outros entram (anaplerose) para repor o que saiu.])

Intermediários *saem* do ciclo (#termo-nota[cataplerose][saída de intermediários do ciclo para vias biossintéticas; depleta o pool de intermediários]) em vários pontos:
- *α-cetoglutarato* (saindo entre *passos 3 e 4*) → glutamato → muitos aminoácidos.
- *Succinil-CoA* (saindo após *passo 4*) → heme (síntese de hemoglobina).
- *OAA* (após *passo 8*) → aspartato; também desvia para *gliconeogênese* via fosfoenolpiruvato.
- *Citrato* (saindo após *passo 1*) → exportado para o citosol → síntese de ácidos graxos.

Se intermediários saem o tempo todo, o ciclo precisa de um mecanismo para *repor* — caso contrário, ele se esvaziaria de OAA e pararia. Essa reposição se chama #termo-nota[anaplerose][reações que repõem intermediários removidos do ciclo, mantendo-o em funcionamento]. A reação anaplerótica mais importante é catalisada pela *piruvato carboxilase*:

#align(center, text(size: 11pt)[piruvato + HCO₃⁻ + ATP → OAA + ADP + Pi])

#figura-nebli("/figuras/ciclo-krebs/slide-41.png",
  largura: 65%,
  legenda: [Reação anaplerótica da piruvato carboxilase: piruvato + CO₂ + ATP → OAA. Enzima do fígado e rim, usa biotina como coenzima.])

A piruvato carboxilase é regulada alostericamente pela própria *acetil-CoA*: quando a acetil-CoA acumula (sinal de que está sobrando combustível e o ciclo precisa de mais OAA para receber), ela ativa a piruvato carboxilase, que produz mais OAA. Linda lógica feedback-forward: "estou chegando demais; faz mais quem me recebe".

#figura-nebli("/figuras/ciclo-krebs/slide-40.png",
  largura: 60%,
  legenda: [Regulação da piruvato carboxilase: ativada alostericamente por acetil-CoA. Sem esse efetor positivo, virtualmente inativa.])

*Conexão clínica: jejum prolongado.* No jejum, a gliconeogênese hepática "rouba" OAA do ciclo de Krebs para fazer glicose. O pool de OAA cai. Resultado: acetil-CoA da β-oxidação acumula (porque não tem OAA suficiente para receber no *passo 1*), e o fígado começa a desviar essa acetila para a produção de *corpos cetônicos* (acetoacetato, β-hidroxibutirato). Por isso jejum prolongado e diabetes descompensada produzem cetose — é o Krebs estrangulado por falta de OAA.

== 3.4 — Conclusão integradora

#conclusao-box[
  *Princípio unificador.* O ciclo de Krebs é uma máquina cíclica de extração de elétrons: pega uma acetila de 2 carbonos, gira 8 reações, joga fora os 2 carbonos como CO₂, captura todos os elétrons disponíveis em 3 NADH + 1 FADH₂, paga um GTP por nível de substrato, e devolve o oxaloacetato no fim para receber a próxima acetila. Tudo isso acontece na matriz mitocondrial — exceto o *passo 6*, que mora na membrana porque é também o Complexo II da cadeia respiratória.

  *Mecanismo nuclear.* Por volta: 4 oxidações (passos 3, 4, 6 e 8) + 1 fosforilação em nível de substrato (passo 5). Numerar é tudo: a ordem importa porque ela define qual cofator vem de qual passo, e a contagem clássica (3 NADH + 1 FADH₂ + 1 GTP) só faz sentido se você souber onde cada um nasce. Os pontos regulados são os 3 passos irreversíveis (1, 3 e 4), sempre na lógica "carga alta freia, ADP/Ca²⁺ solta".

  *Clínica retomada.* Deficiência de tiamina (vitamina B1) paralisa simultaneamente o *passo 0* (PDH) e o *passo 4* (α-KG-DH), porque ambos usam TPP. Quadro clínico: beriberi cardiovascular (úmido) ou neurológico (seco), encefalopatia de Wernicke nos etilistas crônicos. Inibidor de aconitase (*passo 2*): fluoroacetato, veneno de rato. No jejum prolongado, o ciclo é estrangulado pelo desvio de OAA para gliconeogênese, e o acumulo de acetil-CoA gera cetose.

  *Projeção para o próximo tema.* Os 3 NADH e 1 FADH₂ que saem de cada volta do ciclo são *energia em trânsito* — eles ainda precisam ser convertidos em ATP. Esse é o trabalho da *cadeia respiratória* e da *fosforilação oxidativa*, o próximo resumo da UC. Lá você vai entender como a SDH (que aqui é "*passo 6*") aparece de novo, com outro nome: Complexo II. E vai entender por que o GTP do *passo 5* continua sendo gerado mesmo quando a cadeia está bloqueada — um dos pontos mais elegantes da integração metabólica.
]

#mindmap-fechamento(
  tema: "CICLO DE KREBS",
  mensagem: "8 reações em sequência que oxidam acetil-CoA a 2 CO₂ e devolvem OAA — 3 NADH, 1 FADH₂, 1 GTP por volta",
  com-setas: true,
  estacoes: (
    (rotulo: "Entrada · passo 0", titulo: "PDH transforma piruvato em acetil-CoA",
     fala: [perdemos 1 carbono como CO₂, ganhamos 1 NADH e a acetila ativada por tioéster — agora sim pronto pra entrar no ciclo], cor: "a"),
    (rotulo: "Engrenagem · passos 1–8", titulo: "Quatro oxidações + uma fosforilação",
     fala: [passos 3, 4 e 8 geram NADH; passo 6 gera FADH₂; passo 5 paga o único GTP em nível de substrato; passos 3 e 4 jogam os 2 CO₂ fora], cor: "neutra", destaque: true),
    (rotulo: "Saída · cofatores", titulo: "NADH e FADH₂ vão pra cadeia respiratória",
     fala: [3 NADH × 2.5 + 1 FADH₂ × 1.5 + 1 GTP = 10 ATP por volta; e o ciclo recomeça com OAA fresco no passo 1], cor: "b"),
  ),
  rodape-titulo: "Regulação · clínica · anfibolismo",
  cartoes: (
    (titulo: "Quem manda na velocidade", frase: [passos 1, 3 e 4 são os irreversíveis — carga energética alta freia, ADP e Ca²⁺ aceleram a IDH]),
    (titulo: "Tiamina é a coenzima da vida", frase: [B1 entra no PDH (passo 0) e na α-KG-DH (passo 4); sem ela vem beriberi e Wernicke]),
    (titulo: "Krebs não é só catabólico", frase: [intermediários saem (heme, aminoácidos, glicose) e voltam pela piruvato carboxilase, ativada por acetil-CoA]),
  ),
)
