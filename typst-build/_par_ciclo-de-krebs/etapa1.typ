#import "../../typst-template/nebli_v2_apostila.typ": *

#set-etapa("Etapa 1 — texto didático")

#intro-box[
  A glicólise quebra a glicose em dois piruvatos e devolve apenas 2 #sigla("ATP", [adenosina trifosfato — moeda energética da célula, libera energia ao perder um fosfato]) por glicose. É pouco. A maior parte da energia química da glicose continua presa nos piruvatos e nos #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzido — carregador de elétrons de alta energia]) gerados.

  Para extrair essa energia restante, a célula precisa de duas coisas: oxigênio e mitocôndria. O oxigênio é o sumidouro final de elétrons; a mitocôndria é o local onde os elétrons vão sendo arrancados dos carbonos e entregues a uma cadeia transportadora que termina no O₂.

  O ciclo de Krebs é o motor central dessa extração. Cada acetil-CoA que entra no ciclo é oxidado por completo — sai como 2 CO₂ — e os elétrons removidos ficam guardados em três #sigla("NAD+", [forma oxidada do NAD; aceita 2 elétrons + 1 próton, vira NADH]) reduzidos a NADH e um #sigla("FAD", [flavina adenina dinucleotídeo — outro carregador de elétrons]) reduzido a #sigla("FADH₂", [forma reduzida do FAD; entrega elétrons à cadeia respiratória]). É a usina onde a oxidação se completa e os carregadores são "carregados" para entregar elétrons à cadeia respiratória.
]

#parte-title("PARTE I — Do piruvato ao acetil-CoA: a entrada do ciclo", primeira: true)

#subtopico("1.1 — Por que a glicólise não basta")

A glicólise é a via mais antiga e universal de extração de energia da glicose. Acontece no citosol, não depende de oxigênio e produz, por glicose, um saldo líquido de 2 ATP, 2 NADH e 2 piruvato. O piruvato é uma molécula de 3 carbonos com muita energia química ainda guardada nas suas ligações C–C e C–H.

A pergunta que ancora todo o restante do metabolismo aeróbio é direta: por que parar aqui se ainda há tanto a extrair? A resposta tem duas partes. Primeira, sem oxigênio o NADH gerado na glicólise não tem para onde despejar seus elétrons, e a célula é obrigada a desviar piruvato para fermentação (lactato, em humanos) só para regenerar o NAD⁺ e manter a glicólise rodando. Segunda, com oxigênio disponível, a célula pode levar o piruvato para a mitocôndria e oxidá-lo até CO₂, recuperando muito mais energia.

#mini-resumo[A glicólise extrai pouco da glicose porque sem O₂ os elétrons removidos não têm para onde ir. Com O₂ disponível, o piruvato entra na mitocôndria e a oxidação continua dentro do ciclo de Krebs.]

#subtopico("1.2 — O transporte do piruvato para a matriz mitocondrial")

A mitocôndria tem duas membranas. A externa é frouxa — porinas a tornam permeável a moléculas pequenas. A interna é a barreira de verdade, fortemente seletiva, e separa o espaço intermembrana da matriz mitocondrial, onde mora o ciclo de Krebs.

#figura-nebli("/figuras/ciclo-de-krebs/slide-06.png",
  largura: 65%,
  legenda: [Glicólise no citosol gera 2 piruvatos a partir de cada glicose. Os 2 piruvatos atravessam a membrana mitocondrial interna pelo transportador de monocarboxilato e chegam à matriz, onde encontram o complexo da piruvato desidrogenase. A partir daqui, tudo acontece dentro da mitocôndria.])

O piruvato atravessa essa membrana interna por um transportador específico, o transportador de monocarboxilato. Ele faz simporte com H⁺ — aproveita o gradiente de prótons já estabelecido pela cadeia respiratória para puxar o piruvato para dentro. Uma vez na matriz, o piruvato encontra a enzima que vai retirar dele o primeiro carbono e prepará-lo para o ciclo: o complexo da piruvato desidrogenase.

#subtopico("1.3 — O complexo da piruvato desidrogenase (PDH): o portão do ciclo")

#figura-nebli("/figuras/ciclo-de-krebs/slide-09.png",
  largura: 60%,
  legenda: [Microscopia eletrônica do complexo da piruvato desidrogenase de #emph[E. coli]. A estrutura esférica é a montagem dos cerca de 60 polipeptídeos das três enzimas (E1, E2, E3) fisicamente acopladas. Essa proximidade física é o que permite ao intermediário passar de sítio em sítio sem soltar no meio.])

O complexo da #sigla("PDH", [piruvato desidrogenase — complexo multienzimático que converte piruvato em acetil-CoA]) é uma das estruturas moleculares mais elegantes do metabolismo. Não é uma enzima só, são três enzimas diferentes fisicamente acopladas, montadas em um arranjo esférico gigante visível em microscopia eletrônica. O motivo dessa engenharia é direto: o substrato precisa passar por três reações químicas em sequência, e cada intermediário é instável. Mantendo as três enzimas grudadas, o intermediário nunca solta no meio — vai sendo passado de uma para a outra.

As três enzimas são chamadas E1, E2 e E3. A E1 é a piruvato desidrogenase propriamente dita; recebe o piruvato, tira o CO₂ e gera um intermediário ligado a uma coenzima chamada TPP. A E2 é a #termo-nota[diidrolipoil transacetilase][enzima E2 do complexo PDH; carrega o grupo acetil entre os sítios ativos via braço de ácido lipóico]; ela pega esse intermediário, oxida-o e transfere o grupo acetil para a coenzima A, formando o acetil-CoA. A E3 é a diidrolipoil desidrogenase; ela recupera a forma oxidada do ácido lipóico (que ficou reduzido na transferência) e devolve os elétrons ao NAD⁺, gerando o NADH que sai do complexo.

A reação líquida do complexo é compacta e poderosa:

#mini-resumo[piruvato + CoA + NAD⁺ → acetil-CoA + CO₂ + NADH]

Veja o que aconteceu. O piruvato tinha 3 carbonos; saiu um como CO₂. Os elétrons removidos foram parar no NADH. O que restou (2 carbonos, na forma de grupo acetil) foi entregue à coenzima A, formando uma ligação tioéster de alta energia — o acetil-CoA. Essa energia da ligação tioéster é o que vai dirigir a entrada do acetil no ciclo.

Esse tipo de reação tem nome: descarboxilação oxidativa. "Descarboxilação" porque sai CO₂. "Oxidativa" porque elétrons são removidos e entregues ao NAD⁺. O complexo da PDH faz as duas coisas ao mesmo tempo, e essa é a regra geral de como o metabolismo central retira carbonos de moléculas pequenas: tira CO₂ e tira elétrons no mesmo passo.

#confusao-prevista(
  titulo: "PDH não pertence ao ciclo de Krebs",
  aluno_acha: [aluno acha que a PDH é uma das 8 reações do ciclo],
  mecanismo: [a PDH é a ponte que prepara o substrato. O ciclo começa na reação 1 (citrato sintase), com o acetil-CoA já formado. Os 2 NADH gerados pela PDH (1 por piruvato × 2 piruvatos por glicose) entram no balanço total da oxidação aeróbia, mas não contam como "produto do ciclo".],
)

#subtopico("1.4 — As cinco coenzimas e por que vitamina B1 importa")

#figura-nebli("/figuras/ciclo-de-krebs/slide-17.png",
  largura: 80%,
  legenda: [Etapas da reação catalisada pelo complexo da piruvato desidrogenase. O piruvato é descarboxilado em E1 (com TPP), o intermediário hidroxietil é transferido para o ácido lipóico de E2, oxidado a acetil-lipoil e então passado para a CoA, formando o acetil-CoA. E3 recupera o lipoil oxidado e gera NADH. Observe como o braço flexível do ácido lipóico carrega o intermediário entre os 3 sítios sem soltar.])

Para que as três enzimas do complexo PDH funcionem em sequência, são necessárias cinco coenzimas. Cada uma vem de uma vitamina diferente, e por isso a deficiência de qualquer uma delas paralisa o complexo inteiro. As cinco são: #sigla("TPP", [tiamina pirofosfato — coenzima derivada da vitamina B1]) (derivada da vitamina B1), CoA (derivada do ácido pantotênico, vitamina B5), NAD⁺ (derivada da nicotinamida, vitamina B3), FAD (derivada da riboflavina, vitamina B2) e o ácido lipóico (uma vitamina nem sempre listada, pois é sintetizada pelo próprio organismo em quantidades suficientes na maioria dos casos).

O ácido lipóico merece atenção. Ele fica ligado covalentemente à E2 por uma cadeia lateral longa e flexível, que funciona como um braço mecânico. Esse braço alcança os sítios ativos de E1, E2 e E3 sucessivamente, carregando o grupo acetil de um sítio para o seguinte sem soltá-lo no meio. É o que garante que o intermediário não vaze.

A coenzima clinicamente mais relevante é a TPP, derivada da tiamina (vitamina B1). Sem TPP funcional, a E1 do complexo PDH não funciona — o piruvato não consegue ser descarboxilado, e acumula. O mesmo acontece com a α-cetoglutarato desidrogenase, que veremos adiante na reação 4 do ciclo: mesma química, mesma dependência de TPP.

#clinica-box("Deficiência de tiamina: beribéri e Wernicke-Korsakoff", [
  A vitamina B1 não é estocada em quantidade significativa pelo organismo. Reservas se esgotam em poucas semanas de privação alimentar. As duas síndromes clássicas decorrem dessa carência.

  O beribéri tem duas formas. A forma "úmida" cursa com insuficiência cardíaca de alto débito (o coração precisa bombear mais para compensar o metabolismo prejudicado, e descompensa). A forma "seca" cursa com neuropatia periférica simétrica, com fraqueza e perda de sensibilidade. Em ambos os casos, a causa imediata é a paralisação da PDH e da α-KG desidrogenase no tecido afetado.

  A síndrome de Wernicke-Korsakoff é a apresentação neurológica clássica em alcoolistas crônicos. O álcool atrapalha a absorção intestinal de tiamina e ainda aumenta a demanda metabólica que requer B1. O quadro agudo (Wernicke) traz confusão mental, ataxia e oftalmoplegia; se não tratado, evolui para a forma crônica e irreversível (Korsakoff), com amnésia anterógrada e confabulação. Por isso, em qualquer alcoolista descompensado em pronto-socorro, repõe-se tiamina por via intravenosa _antes_ de dar glicose — porque oferecer glicose sem B1 dispara consumo do estoque residual e pode precipitar a Wernicke aguda.
])

#parte-title("PARTE II — As oito reações: a oxidação completa do grupo acetil")

#figura-nebli("/figuras/ciclo-de-krebs/slide-22.png",
  largura: 78%,
  legenda: [Visão geral do ciclo de Krebs. O acetil-CoA entra na reação 1 (citrato sintase), os carbonos vão sendo oxidados ao longo das 8 reações, e o oxaloacetato é regenerado ao final, fechando o ciclo. Repare nos pontos de saída de CO₂ (R3 e R4) e nos pontos onde NADH, FADH₂ e GTP são produzidos.])

O ciclo é uma sequência fechada de oito reações enzimáticas. Cada volta consome um acetil-CoA, produz dois CO₂, recupera três NADH, um FADH₂ e um #sigla("GTP", [guanosina trifosfato — equivalente energético do ATP, fácil de interconverter]), e regenera o oxaloacetato (OAA), pronto para receber o próximo acetil-CoA. A linha geral é: os 2 carbonos do acetil entram, são oxidados, saem como CO₂, e os elétrons removidos a cada passo são entregues a NAD⁺ ou FAD.

A descrição abaixo segue a numeração canônica das 8 reações.

#subtopico("2.1 — Reações 1 e 2: condensação e isomerização")

*Reação 1 — citrato sintase.* O acetil-CoA (2 carbonos) condensa com o oxaloacetato (4 carbonos) formando citrato (6 carbonos). A energia que dirige essa condensação vem da hidrólise da ligação tioéster do acetil-CoA — sem ela, a reação seria desfavorável. Esse passo é altamente exergônico e, na prática, irreversível, o que faz da citrato sintase um dos pontos de controle do ciclo.

*Reação 2 — aconitase.* O citrato é isomerizado em isocitrato. Olhando os dois lado a lado, parece quase a mesma molécula: a aconitase apenas remove a hidroxila do carbono central e a reinsere no carbono adjacente. O intermediário transitório dessa troca é o cis-aconitato, que dá nome à enzima. Esse rearranjo aparentemente trivial é necessário porque o citrato, com a hidroxila no carbono terciário, não pode ser oxidado eficientemente; o isocitrato, com a hidroxila no carbono secundário, pode.

#figura-nebli("/figuras/ciclo-de-krebs/slide-20.png",
  largura: 75%,
  legenda: [Isomerização do citrato. A aconitase move a hidroxila do carbono central para o carbono adjacente, passando pelo intermediário cis-aconitato. Pequena mudança estrutural, mas decisiva — só o isocitrato pode ser oxidado na próxima reação.])

#atencao-box("Fluoracetato: o veneno que paralisa o ciclo", [
  O fluoracetato é um composto usado historicamente como rodenticida (e, infelizmente, em casos de envenenamento criminoso). Sozinho ele é inerte. O problema é que dentro da célula ele é convertido pela própria citrato sintase em fluorocitrato — um análogo do citrato que se encaixa no sítio ativo da aconitase mas não pode ser processado, ficando preso lá.

  Resultado: aconitase bloqueada → o ciclo trava em citrato → não há mais regeneração de NADH/FADH₂ → cadeia respiratória sem substrato → falência energética celular. Em humanos, doses de 2–10 mg/kg são letais. Os sintomas aparecem em 30 a 100 minutos: náusea, vômito, dor abdominal, taquicardia, fibrilação ventricular, hipotensão, falência renal, convulsões, coma e morte. Não há antídoto específico; o tratamento é de suporte.

  O caso ilustra uma lição geral do metabolismo: travar um único passo de uma via central destrói tudo o que depende dela. Tecidos com alta demanda energética (cérebro, coração) são os primeiros a falhar.
])

#subtopico("2.2 — Reações 3 e 4: as duas descarboxilações oxidativas")

*Reação 3 — isocitrato desidrogenase (IDH).* O isocitrato é oxidado e descarboxilado em α-cetoglutarato (5 carbonos). Sai o primeiro CO₂ do ciclo. Os elétrons removidos vão para o NAD⁺, gerando o primeiro NADH. A IDH é outro ponto-chave de regulação: é ativada por ADP e Ca²⁺ (sinais de "preciso de mais energia") e inibida por ATP e NADH (sinais de "tenho energia sobrando").

*Reação 4 — α-cetoglutarato desidrogenase.* O α-cetoglutarato é oxidado e descarboxilado em succinil-CoA (4 carbonos). Sai o segundo CO₂. Sai o segundo NADH. E aqui aparece uma simetria importante: a α-cetoglutarato desidrogenase é um complexo multienzimático com a mesma arquitetura da PDH — três enzimas (E1, E2, E3), as mesmas cinco coenzimas (TPP, ácido lipóico, CoA, FAD, NAD⁺), o mesmo mecanismo de descarboxilação oxidativa. A diferença é só o substrato: lá era piruvato, aqui é α-cetoglutarato. Por isso a deficiência de tiamina afeta os dois ao mesmo tempo. Essa reação também é irreversível e regulatória.

Ao fim de R4, dois carbonos já saíram do ciclo (os dois CO₂), e o que resta é uma molécula de 4 carbonos com uma ligação tioéster de alta energia — o succinil-CoA. O ciclo agora vai usar essa energia da ligação tioéster antes de simplesmente jogá-la fora.

#confusao-prevista(
  titulo: "Os 2 CO₂ liberados não vêm dos carbonos que acabaram de entrar",
  aluno_acha: [aluno acha que os 2 CO₂ liberados no ciclo são os 2 carbonos do acetil que acabou de entrar],
  mecanismo: [estudos com isótopos mostram que os 2 carbonos perdidos como CO₂ na primeira volta do ciclo vêm do _oxaloacetato_, não do acetil que acabou de entrar. Os carbonos do acetil ficam dentro do ciclo e só saem em voltas posteriores. Para o balanço energético global isso não muda nada (no longo prazo, cada acetil é oxidado completamente), mas a contabilidade carbono a carbono não é linear como parece à primeira vista.],
)

#subtopico("2.3 — Reação 5: fosforilação em nível de substrato")

#figura-nebli("/figuras/ciclo-de-krebs/slide-26.png",
  largura: 70%,
  legenda: [Fosforilação em nível de substrato. A succinil-CoA sintetase cliva a ligação tioéster de alta energia do succinil-CoA e usa a energia liberada para fosforilar diretamente o GDP em GTP. O GTP é depois convertido em ATP pela nucleosídeo difosfato quinase. É o único ATP gerado dentro do ciclo sem passar pela cadeia respiratória.])

*Reação 5 — succinil-CoA sintetase.* A energia da ligação tioéster do succinil-CoA é aproveitada de forma direta: a enzima cliva essa ligação e usa a energia liberada para fosforilar GDP em GTP. Forma-se succinato (4 carbonos, sem CoA) e libera-se GTP.

Esse mecanismo tem nome: _fosforilação em nível de substrato_. A diferença para a fosforilação oxidativa (que veremos no fechamento da Parte II) é que aqui a formação de GTP não depende da cadeia respiratória nem do gradiente de prótons. É uma transferência química direta, ligação a ligação.

O GTP gerado é convertido em ATP pela nucleosídeo difosfato quinase (GTP + ADP → GDP + ATP). Na prática, contamos esse passo como "1 ATP" no balanço do ciclo. É o único ATP gerado diretamente dentro do ciclo de Krebs — todos os outros virão indiretamente, da reoxidação do NADH e do FADH₂ na cadeia respiratória.

#subtopico("2.4 — Reações 6, 7 e 8: regenerando o oxaloacetato")

A tarefa final do ciclo é converter succinato (4 carbonos, totalmente reduzido nos átomos centrais) de volta em oxaloacetato (4 carbonos, com uma carbonila). Isso significa oxidar duas vezes, com uma hidratação no meio.

#figura-nebli("/figuras/ciclo-de-krebs/slide-29.png",
  largura: 70%,
  legenda: [Reação 6 — oxidação do succinato a fumarato pela succinato desidrogenase. O FAD aceita os 2 elétrons na forma de 2 átomos de hidrogênio (1 de cada carbono central), virando FADH₂. Essa é a única reação do ciclo onde o aceptor de elétrons é o FAD em vez do NAD⁺, e a única enzima do ciclo ancorada na membrana mitocondrial interna — é também o Complexo II da cadeia respiratória.])

*Reação 6 — succinato desidrogenase (SDH).* O succinato é oxidado a fumarato, com remoção de dois hidrogênios. Os elétrons vão para o FAD, gerando FADH₂. Duas particularidades importantes aqui. Primeira: a SDH é a única enzima do ciclo que não está livre na matriz — ela está ancorada na membrana mitocondrial interna. Segunda: a SDH é exatamente o _Complexo II_ da cadeia respiratória. Os elétrons do FADH₂ gerado por essa reação entram direto na ubiquinona (CoQ) da cadeia respiratória, sem passar pelo Complexo I. Por isso o FADH₂ "rende menos ATP" que o NADH no balanço final: ele pula um dos pontos onde prótons são bombeados.

*Reação 7 — fumarase.* O fumarato é hidratado, formando L-malato. É uma reação simples, sem oxidação, sem redução. Apenas a adição estereoespecífica de uma molécula de água através da dupla ligação do fumarato.

*Reação 8 — malato desidrogenase.* O malato é oxidado a oxaloacetato, com os elétrons indo para o NAD⁺ — gerando o terceiro e último NADH do ciclo. O oxaloacetato regenerado está pronto para receber outro acetil-CoA e iniciar nova volta.

#subtopico("2.5 — Balanço energético do ciclo e integração com a cadeia respiratória")

Cada volta do ciclo consome um acetil-CoA e produz: 3 NADH, 1 FADH₂, 1 GTP, 2 CO₂. Em termos de ATP equivalente, usando os valores modernos de rendimento da cadeia respiratória (2,5 ATP por NADH; 1,5 ATP por FADH₂), uma volta corresponde a aproximadamente:

#mini-resumo[3 NADH × 2,5 + 1 FADH₂ × 1,5 + 1 GTP = 7,5 + 1,5 + 1 = 10 ATP por volta do ciclo.]

Como cada glicose gera 2 piruvatos e, portanto, 2 acetil-CoA, o ciclo roda duas vezes por glicose, produzindo cerca de 20 ATP só nessa etapa. Somando glicólise (2 ATP, 2 NADH), PDH (2 NADH), Krebs (20 ATP-equivalentes) e a cadeia respiratória, a oxidação completa de uma glicose rende algo entre 30 e 32 ATP.

O valor histórico de 38 ATP por glicose, que aparece em muitos slides e livros, vem de cálculos antigos que assumiam 3 ATP por NADH e 2 ATP por FADH₂. Hoje sabemos que esses números são superestimativas — a estequiometria real da ATP sintase e o custo de transporte de NADH do citosol para a mitocôndria reduzem o rendimento. Os 30-32 ATP são o número aceito atualmente. Cite o valor moderno na hora da prova, mas reconheça que o valor antigo pode aparecer como distrator.

#confusao-prevista(
  titulo: "O ciclo de Krebs não consome oxigênio",
  aluno_acha: [aluno acha que o O₂ entra dentro de alguma reação do ciclo],
  mecanismo: [nenhuma das 8 reações do ciclo usa O₂ diretamente. O O₂ é consumido apenas na cadeia respiratória, como aceptor final de elétrons. A dependência do ciclo em relação ao O₂ é _indireta_: sem O₂, a cadeia respiratória trava, o NADH não consegue ser reoxidado a NAD⁺, falta NAD⁺ para as reações 3, 4 e 8, e o ciclo para por escassez de cofator. Por isso hipóxia mata: não por falta de oxigênio dentro do ciclo, mas por paralisação da via que regenera os cofatores que o ciclo precisa.],
)

#parte-title("PARTE III — A face dupla do ciclo: anfibólico e regulado")

#subtopico("3.1 — Função anfibólica: o ciclo é também via biossintética")

Até aqui o ciclo foi tratado como um forno catabólico — moléculas grandes são quebradas, carbonos saem como CO₂, energia é capturada. Mas o ciclo tem uma segunda função, igualmente central: vários de seus intermediários são desviados para fora do ciclo e servem como precursores de biossíntese. Essa propriedade de ser ao mesmo tempo catabólico e anabólico é chamada de _anfibólica_.

Os principais desvios são os seguintes. O α-cetoglutarato sai para virar glutamato (que é precursor de glutamina, prolina e outros aminoácidos); o succinil-CoA sai para a síntese de heme (o grupo prostético da hemoglobina, mioglobina e citocromos); o oxaloacetato sai para virar aspartato (precursor de outros aminoácidos e bases nitrogenadas) e também para a gliconeogênese no fígado durante o jejum; o citrato sai da mitocôndria para o citosol, onde é usado na síntese de ácidos graxos.

Essa "fuga" de intermediários cria um problema. Se o ciclo só perde carbonos e não os repõe, o oxaloacetato vai diminuindo. Sem oxaloacetato em quantidade suficiente, o acetil-CoA que chega não tem com quem condensar, e o ciclo para. A célula precisa, portanto, de um mecanismo para repor intermediários que saíram. Esse mecanismo se chama _anaplerose_.

#figura-nebli("/figuras/ciclo-de-krebs/slide-39.png",
  largura: 78%,
  legenda: [Função anfibólica do ciclo do ácido cítrico. As setas que saem do ciclo levam intermediários para vias biossintéticas: α-cetoglutarato e oxaloacetato alimentam síntese de aminoácidos; succinil-CoA vai para o heme; o citrato sai para o citosol e alimenta a síntese de ácidos graxos. As setas que entram são reações anapleróticas, que repõem o que saiu.])

#subtopico("3.2 — Anaplerose: a piruvato carboxilase reabastece o oxaloacetato")

A reação anaplerótica mais importante no fígado e no rim é catalisada pela _piruvato carboxilase_. Ela toma uma molécula de piruvato e, com gasto de 1 ATP e um íon bicarbonato (HCO₃⁻) como fonte de carbono, produz oxaloacetato:

#mini-resumo[piruvato + HCO₃⁻ + ATP → oxaloacetato + ADP + Pi]

Repare na elegância da regulação dessa enzima. A piruvato carboxilase é virtualmente _inativa_ na ausência de acetil-CoA. Acetil-CoA funciona como ativador alostérico positivo obrigatório — sem ele, a enzima fica desligada.

A lógica é cristalina. Se o acetil-CoA está acumulando, isso significa que o ciclo de Krebs não está conseguindo processá-lo na velocidade necessária. E a razão mais comum para isso é falta de oxaloacetato. Então o próprio acetil-CoA acumulado avisa a piruvato carboxilase: "preciso de mais OAA". A enzima se ativa, gera OAA a partir de piruvato, e o ciclo destrava.

#figura-nebli("/figuras/ciclo-de-krebs/slide-41.png",
  largura: 75%,
  legenda: [Piruvato carboxilase — a principal reação anaplerótica do fígado e do rim. O piruvato é carboxilado a oxaloacetato usando ATP e HCO₃⁻ como doador de carbono. A enzima é virtualmente inativa sem acetil-CoA: o próprio acúmulo de acetil-CoA é o sinal de que falta OAA para a condensação do ciclo, e essa retroalimentação positiva mantém o equilíbrio entre entrada de combustível e disponibilidade de OAA.])

#clinica-box("Por que jejum prolongado causa cetose", [
  Durante jejum prolongado, o oxaloacetato hepático é desviado em massa para a gliconeogênese — a síntese de glicose nova para alimentar cérebro e hemácias. Isso esvazia o ciclo de Krebs no fígado.

  Enquanto isso, a lipólise no tecido adiposo manda ácidos graxos para o fígado, que os converte em acetil-CoA em grande quantidade. O acetil-CoA acumula, mas não tem oxaloacetato para condensar (porque o OAA está sendo todo desviado para gliconeogênese). A piruvato carboxilase tenta reabastecer, mas o piruvato disponível também está escasso (afinal, a glicólise está reduzida no estado de jejum).

  Resultado: o acetil-CoA que sobra é desviado para a síntese de _corpos cetônicos_ (acetoacetato, β-hidroxibutirato, acetona). É a cetose fisiológica do jejum. Em quantidades fisiológicas é adaptativa — o cérebro pode usar corpos cetônicos como combustível. Em quantidades excessivas (cetoacidose diabética), ela ameaça a vida pela acidose metabólica grave que produz.
])

#subtopico("3.3 — Regulação fina: como o ciclo sabe quando acelerar e quando frear")

A regulação do ciclo de Krebs tem dois níveis. O primeiro é a regulação da entrada — o complexo PDH. O segundo são os três pontos de controle dentro do ciclo: citrato sintase, isocitrato desidrogenase e α-cetoglutarato desidrogenase. A lógica comum nesses dois níveis é simples: quando ATP e NADH estão altos, a célula tem energia sobrando, e o ciclo desacelera; quando ADP, AMP e Ca²⁺ estão altos, a célula precisa de energia, e o ciclo acelera.

O complexo PDH é regulado por fosforilação covalente. Existe uma _PDH quinase_, que fosforila o complexo e o inativa, e uma _PDH fosfatase_, que remove o fosfato e o reativa. A PDH quinase é estimulada quando há acetil-CoA, NADH e ATP em excesso (a saída do ciclo está sobrecarregada, então não adianta entrar mais substrato); é inibida pelo piruvato (se há piruvato acumulando, o complexo precisa funcionar). A PDH fosfatase é estimulada por Ca²⁺ — sinal direto de contração muscular, ou seja, demanda energética imediata.

Dentro do ciclo, a citrato sintase é inibida por ATP, NADH, succinil-CoA e pelo próprio citrato (inibição por produto). A isocitrato desidrogenase é o ponto regulatório mais importante: ativada por ADP e Ca²⁺, inibida por ATP e NADH. A α-cetoglutarato desidrogenase fecha o trio: ativada por Ca²⁺, inibida por succinil-CoA e NADH.

Note que o Ca²⁺ aparece como ativador em três pontos diferentes (PDH fosfatase, IDH, α-KG desidrogenase). Não é coincidência. Quando o músculo contrai, libera-se Ca²⁺ no citoplasma e parte dele entra na mitocôndria; o Ca²⁺ mitocondrial avisa o ciclo de que a demanda energética acabou de subir. É um sinal direto, mecânico, que casa contração com produção de ATP.

#subtopico("3.4 — Onde Krebs se encaixa no quadro maior")

O ciclo de Krebs ocupa o centro do metabolismo energético. Carboidratos chegam ao ciclo via piruvato e PDH. Lipídios chegam diretamente como acetil-CoA, gerado pela β-oxidação dos ácidos graxos na própria matriz mitocondrial. Proteínas chegam principalmente como α-cetoglutarato, succinil-CoA, fumarato e oxaloacetato, dependendo do aminoácido. Todos os combustíveis convergem para o ciclo, e todos os elétrons extraídos saem em NADH ou FADH₂.

O destino desses NADH e FADH₂ é a cadeia respiratória, na membrana mitocondrial interna. Lá, os elétrons descem por uma série de complexos (I, III, IV, com a SDH como Complexo II para o FADH₂), e em três desses pontos a passagem dos elétrons bombeia prótons da matriz para o espaço intermembrana. Isso cria um gradiente eletroquímico que é dissipado pela ATP sintase para produzir ATP. Esse processo é a fosforilação oxidativa, e é onde a maior parte do ATP da oxidação aeróbia é produzido.

#atencao-box("Hipóxia é falência energética em minutos", [
  Tecidos com alta demanda energética e baixa reserva de glicogênio dependem absolutamente do funcionamento conjunto de Krebs + cadeia respiratória. Cérebro e miocárdio são os dois exemplos canônicos.

  Quando uma artéria coronária oclui (infarto agudo do miocárdio), o aporte de O₂ ao tecido downstream cai a zero em segundos. A cadeia respiratória trava em segundos. O NADH para de ser reoxidado. O NAD⁺ se esgota. O ciclo de Krebs para. A célula tenta sobreviver à custa de glicólise anaeróbia, mas o rendimento de 2 ATP por glicose não basta para manter as bombas iônicas e a integridade da membrana. Em minutos, a célula entra em necrose isquêmica.

  O AVC isquêmico segue a mesma lógica, no cérebro. A janela terapêutica de poucas horas para reperfundir o tecido (trombólise, trombectomia) reflete diretamente esse cronograma metabólico: antes desse limite, parte do tecido ainda é recuperável; depois dele, a maioria das células já entrou em morte irreversível.
])

#conclusao-box[
  O ciclo de Krebs é o ponto onde os carbonos do acetil-CoA terminam sua viagem oxidativa. Cada volta retira 2 CO₂, armazena energia em 3 NADH, 1 FADH₂ e 1 GTP, e regenera o oxaloacetato para a próxima volta. Esses carregadores reduzidos entregam seus elétrons à cadeia respiratória, que produz ATP em quantidade — cerca de 20 dos 30-32 ATP por glicose vêm daqui.

  Mas o ciclo não é só catabolismo. Vários de seus intermediários alimentam vias biossintéticas — heme, aminoácidos, ácidos graxos, gliconeogênese. Por isso ele é anfibólico. E por isso precisa de reações anapleróticas, em primeiro lugar a piruvato carboxilase, que repõe o oxaloacetato consumido.

  A regulação do ciclo segue uma lógica simples e onipresente: ATP/NADH altos travam (a célula está saciada); ADP/Ca²⁺ altos aceleram (a célula precisa). O Ca²⁺ mitocondrial é o elo que casa contração muscular com demanda energética. E a deficiência de tiamina, que paraliza PDH e α-KG desidrogenase ao mesmo tempo, é a lição clínica recorrente.

  Krebs é mais do que uma sequência de 8 reações. É o eixo onde catabolismo e anabolismo se encontram, onde a célula equilibra a entrada de combustível com a demanda de ATP, e onde o oxigênio — embora não participe de nenhuma reação do ciclo — comanda à distância se a engrenagem gira ou para.
]

// Mindmap de fechamento removido do pipeline em 2026-05-28 (canônico).
