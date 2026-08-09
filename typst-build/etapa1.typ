#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Uma célula do fígado não tem como saber que você acabou de almoçar. Ela não enxerga o prato, não sente o estômago cheio, não conversa com o intestino. Mesmo assim, minutos depois da refeição, essa célula começa a guardar glicose em glicogênio — exatamente o oposto do que fazia às cinco da manhã, quando ainda estava despejando glicose no sangue. Alguma coisa viajou do pâncreas até ela e trocou o programa.

  Essa coisa é o hormônio, e este resumo é sobre como ele funciona. A pergunta central não é qual glândula produz o quê, mas *como uma molécula em concentração ínfima, circulando por todo o corpo, consegue mudar o comportamento de um tecido específico*. A resposta se organiza em três movimentos: como o sinal é construído e reconhecido (PARTE I), o que acontece quando ele para na membrana e delega o recado a mensageiros internos (PARTE II), e o que muda quando ele atravessa a célula inteira e vai negociar direto com o DNA (PARTE III). Ao final, insulina, glucagon, adrenalina, hormônio tireoidiano e cortisol deixam de ser cinco nomes soltos e passam a ser cinco variações de dois mecanismos.
]

#parte-title("PARTE I — O sinal: o que é um hormônio e como ele chega", primeira: true)

#subtopico("1.1 — Regular uma reação e integrar um organismo são problemas diferentes")

A célula tem três maneiras de mudar a velocidade de uma reação, e elas operam em escalas de tempo muito distintas. A primeira é a *regulação alostérica*: uma molécula pequena se encaixa num sítio da enzima diferente do sítio ativo, muda a forma da proteína e, com isso, sua velocidade. É instantânea e reversível — o acúmulo de #sigla("AMP", [adenosina monofosfato — sinaliza carga energética baixa na célula]) numa fibra muscular acelera a quebra de glicogênio no mesmo segundo em que aparece. A segunda é a *modificação covalente*: uma cinase pendura um grupo fosfato num resíduo de serina, treonina ou tirosina da enzima, e a carga negativa desse fosfato reorganiza a proteína inteira. Leva segundos, dura enquanto uma fosfatase não vier removê-lo. A terceira é o *controle da expressão*: a célula simplesmente fabrica mais (ou menos) cópias daquela enzima. Leva horas, e por isso é a alavanca das mudanças que precisam durar.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-03.png",
  largura: 78%,
  legenda: [As três alavancas de regulação metabólica, da mais rápida à mais duradoura. À esquerda, a curva em S da enzima alostérica, que dispara numa faixa estreita de concentração; no meio, o ciclo fosforilação–desfosforilação, em que cinase e fosfatase disputam o mesmo resíduo; à direita, o controle da transcrição, com o hormônio decidindo quantas cópias da enzima existirão. As três aparecem de novo, uma a uma, no resto deste resumo.])

Essas três alavancas resolvem a regulação *dentro* de uma célula. Elas não resolvem o problema seguinte, que é maior: a fartura e a escassez de nutrientes acontecem no organismo inteiro, ao mesmo tempo, e exigem respostas coordenadas em tecidos que estão a metros de distância um do outro. Quando a glicemia cai durante o sono, não adianta o fígado liberar glicose se o músculo continuar consumindo o que encontra pela frente e o tecido adiposo continuar guardando gordura. A resposta ao jejum é uma decisão *do corpo*, não de uma célula — e uma decisão que precisa ser tomada simultaneamente em bilhões de células que não têm contato físico entre si.

#mini-resumo[A regulação alostérica e a covalente resolvem o "quão rápido" dentro da célula; o hormônio resolve o "todo mundo ao mesmo tempo" entre células distantes.]

O hormônio é a solução evolutiva para esse problema de distância. Uma célula especializada fabrica uma molécula, joga na corrente sanguínea, e essa molécula chega a todos os tecidos ao mesmo tempo — mas só é *lida* por quem tem o receptor correspondente. E o hormônio não inventa mecanismos novos: ele opera as mesmas três alavancas de sempre. A adrenalina age por modificação covalente, disparando uma cascata de fosforilações. O cortisol age por expressão gênica, mudando quantas enzimas de gliconeogênese o hepatócito terá. A insulina faz as duas coisas.

Regular um hormônio, portanto, é regular uma cadeia longa, e essa cadeia tem sete pontos de controle independentes: biossíntese, estocagem, secreção, transporte no sangue, reconhecimento pelo receptor, resposta intracelular e degradação. Uma doença endócrina pode nascer em qualquer um dos sete — falta de matéria-prima na síntese, estoque que não é liberado, receptor que não reconhece, resposta intracelular que não acontece mesmo com o hormônio ligado. Guardar essa lista de sete etapas é guardar o mapa de onde as coisas dão errado.

#subtopico("1.2 — A solubilidade da molécula decide todo o resto do mecanismo")

Hormônios são biomoléculas produzidas numa parte do corpo que regulam funções à distância, agem em quantidades minúsculas — nanomolares, às vezes picomolares — e só funcionam onde existe receptor. Essa definição tem três partes e cada uma esconde uma consequência. "À distância" implica transporte pelo sangue. "Quantidades minúsculas" implica receptores de altíssima afinidade e implica amplificação, porque uma molécula não move um tecido sozinha. "Onde existe receptor" implica que a especificidade da resposta não está no hormônio, e sim em quem tem o aparelho de leitura: a mesma adrenalina que faz o coração acelerar faz o vaso da pele contrair, porque os receptores nesses dois lugares são diferentes.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-09.png",
  largura: 72%,
  legenda: [As quatro famílias químicas do slide, com suas estruturas reais. Repare no contraste que organiza a aula inteira: peptídicos são cadeias de aminoácidos, grandes e carregadas; esteroides são derivados do colesterol, com os mesmos quatro anéis em todos eles; catecolaminas e eicosanoides são moléculas pequenas, derivadas de tirosina e de ácido araquidônico respectivamente.])

As famílias químicas são cinco. Os *peptídicos* — insulina, glucagon, hormônio do crescimento — são cadeias de aminoácidos, sintetizadas no ribossomo como qualquer proteína. As *catecolaminas* — adrenalina, noradrenalina, dopamina — vêm da tirosina por modificação química do anel. Os *eicosanoides* — prostaglandinas, tromboxanos, leucotrienos — vêm do ácido araquidônico, um ácido graxo de vinte carbonos arrancado da membrana. Os *esteroides* — cortisol, aldosterona, testosterona, estradiol, progesterona — vêm todos do colesterol e por isso compartilham o mesmo esqueleto de quatro anéis, diferindo só nos grupos pendurados nele. Os *tireoidianos* — T3 e T4 — vêm da tirosina, como as catecolaminas, mas com iodo adicionado ao anel, o que muda tudo.

Essa lista parece decoreba de nomenclatura, e seria, se não fosse a consequência: *a estrutura química determina a solubilidade, e a solubilidade determina o mecanismo de ação inteiro*. Peptídicos e catecolaminas são hidrossolúveis. Viajam dissolvidos no plasma sem precisar de ajuda, mas quando chegam à célula-alvo esbarram na membrana — uma bicamada lipídica é intransponível para uma molécula carregada. Logo, precisam de um receptor na superfície e de alguém que leve o recado para dentro. Esteroides e tireoidianos são lipossolúveis. O problema deles é o oposto: não conseguem viajar sozinhos num plasma aquoso e precisam de proteínas carreadoras no sangue, mas atravessam a membrana da célula-alvo sem nenhuma dificuldade, porque a membrana é feita do mesmo material que eles.

#confusao-prevista(
  titulo: "Lipossolúvel não significa \"chega mais fácil\"",
  aluno_acha: [que o hormônio lipossolúvel tem a vida facilitada porque atravessa membranas],
  mecanismo: [cada solubilidade facilita uma etapa e complica a outra. O hidrossolúvel viaja fácil e entra difícil; o lipossolúvel viaja difícil — ligado a carreadores — e entra fácil. E há uma consequência prática nisso: o hormônio ligado ao carreador está protegido da degradação e da filtração renal, então o lipossolúvel dura horas no plasma, enquanto a adrenalina dura menos de dois minutos.],
)

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-17.png",
  largura: 80%,
  legenda: [A tabela do Lehninger organiza as classes por via de síntese e modo de ação. As três primeiras linhas — peptídeo, catecolamina, eicosanoide — compartilham o mesmo destino: receptor de membrana e segundo mensageiro. As quatro seguintes — esteroide, vitamina D, retinoide, tireoidiano — compartilham o outro: receptor nuclear e regulação da transcrição. O óxido nítrico fica sozinho numa terceira categoria, com receptor citosólico.])

#subtopico("1.3 — O mesmo sinal químico muda de nome conforme a distância que percorre")

A classificação por estrutura química é uma maneira de agrupar hormônios. A classificação por *distância percorrida* é outra, e independente da primeira. Quando a molécula é lançada no sangue e age num órgão distante, a sinalização é *endócrina* — é o caso da insulina, produzida no pâncreas e lida no fígado, no músculo e no tecido adiposo. Quando ela apenas se difunde pelo líquido extracelular e age na célula vizinha, sem entrar na circulação, a sinalização é *parácrina* — é assim que a somatostatina, produzida pelas células delta da ilhota pancreática, freia as células beta e alfa que estão ao lado. Quando a célula secreta a molécula e ela volta a se ligar em receptores da própria célula que a produziu, a sinalização é *autócrina*.

#figura-lateral("/figuras/bioq-26-controle-hormonal/slide-10.png",
  lado: "right",
  largura-figura: 42%,
  texto: [Vale a analogia: o sinal endócrino é uma transmissão de rádio, que atinge todo mundo mas só é ouvida por quem tem o aparelho sintonizado; o parácrino é um sussurro para quem está do lado; o autócrino é um bilhete que a célula escreve para si mesma. As três formas usam moléculas do mesmo tipo — o que muda é a distância e, com ela, a diluição.],
  legenda: [Endócrino, parácrino e autócrino. Repare que só o endócrino passa pelo vaso.])

Essa distinção importa porque a distância diluí. O sinal endócrino chega ao alvo numa concentração ridiculamente baixa, justamente porque foi diluído em cinco litros de sangue — e é essa diluição que obriga o receptor a ter afinidade altíssima. O sinal parácrino, que percorre micrômetros, chega concentrado, e por isso costuma ser rápido e local.

A mesma lógica explica a fronteira entre hormônio e #termo-nota[neurotransmissor][molécula liberada na fenda sináptica por um neurônio, que age no neurônio ou na célula muscular imediatamente adjacente]. Não é a molécula que define a categoria, é o modo de entrega. A adrenalina liberada pela medula da suprarrenal no sangue é hormônio; a noradrenalina liberada na fenda sináptica pelo terminal nervoso é neurotransmissor. Mesma família química, mesma capacidade de ativar os mesmos receptores — o que muda é que uma viaja pelo sangue e é diluída, e a outra atravessa vinte nanômetros de fenda e chega concentradíssima. É por isso que uma sinapse age em milissegundos e um hormônio, em segundos a minutos.

#subtopico("1.4 — Todo hormônio age por um receptor de alta afinidade, e o tipo de receptor define a escala de tempo")

Se um hormônio circula a 10⁻⁹ mol/L enquanto o substrato de uma enzima comum circula a 10⁻³ mol/L, o receptor precisa ser um milhão de vezes mais ávido que uma enzima comum para capturar alguma coisa. É exatamente isso que ele é. *Alta afinidade* significa que a ligação acontece mesmo em concentração baixíssima, e essa é a primeira condição para qualquer resposta hormonal existir. A segunda é a especificidade: o receptor reconhece a forma da molécula, o que o impede de responder ao mar de outras moléculas presentes em concentração muito maior.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-13.png",
  largura: 82%,
  legenda: [Os seis tipos de transdutor de sinal. Vale ler pelo destino final de cada um: os transdutores 1 a 4 terminam em mudança da atividade de proteínas que já existem na célula; o 6 termina em mudança da quantidade de proteína que a célula vai fabricar. Essa diferença de destino é a diferença de escala de tempo entre segundos e horas.])

O slide organiza seis tipos. O *receptor acoplado à proteína G* — também chamado de 7TM, porque atravessa a membrana sete vezes — não faz nada sozinho: quando o hormônio se liga, ele muda de forma e ativa uma proteína G intracelular, que troca #sigla("GDP", [guanosina difosfato]) por #sigla("GTP", [guanosina trifosfato — a forma "carregada" da proteína G, que a mantém ativa até ela mesma hidrolisar o fosfato]) e vai ligar uma enzima geradora de segundo mensageiro. O *receptor tirosina-cinase* é ele próprio uma enzima: ao ligar o hormônio, duas moléculas do receptor se aproximam e se fosforilam mutuamente, e os fosfatos criados viram pontos de ancoragem para as proteínas seguintes. O *receptor guanilil-ciclase* fabrica GMP cíclico diretamente. O *canal iônico controlado por ligante* abre ou fecha um poro, mudando o potencial da membrana em milissegundos. O *receptor de adesão* liga a matriz extracelular ao citoesqueleto. E o *receptor nuclear* é o único que não fica na membrana: ele espera o hormônio dentro da célula e o leva até o DNA.

Essa lista vira mecanismo quando se olha para a escala de tempo de cada um. Canal iônico responde em milissegundos, porque o efeito é o próprio íon atravessando o poro. Receptor acoplado à proteína G responde em segundos, porque precisa gerar um mensageiro e ativar cinases. Receptor tirosina-cinase e receptor nuclear respondem em horas, porque o efeito final passa por transcrição e síntese de proteína. Um hormônio que precisa reagir a um susto não pode usar receptor nuclear; um hormônio que precisa reconfigurar o metabolismo por dias não ganha nada respondendo em milissegundos.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-14.png",
  largura: 80%,
  legenda: [A mesma classificação, agora com a escala de tempo explícita na linha de baixo — milissegundos, segundos, horas, horas. A coluna de exemplos mostra que o mesmo mensageiro, a acetilcolina, aparece nos dois primeiros tipos: no receptor nicotínico ela abre um canal, no muscarínico ela ativa uma proteína G. O tempo de resposta é do receptor, não do mensageiro.])

#subtopico("1.5 — A amplificação é o que permite governar um tecido com poucas moléculas")

Um hormônio em concentração nanomolar não tem massa suficiente para mover uma via metabólica por ação direta. Se cada molécula de adrenalina precisasse encostar numa molécula de glicogênio-fosforilase para ativá-la, o efeito seria desprezível. O que resolve isso é a *amplificação em cascata*: cada etapa da via é uma enzima, e uma enzima faz muitas cópias do produto seguinte antes de parar.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-16.png",
  largura: 62%,
  legenda: [A pirâmide da amplificação, desenhada de cima para baixo. Uma molécula ativa um receptor; um receptor ativa várias proteínas G; cada adenilil-ciclase produz milhares de AMPc; cada cinase fosforila muitos substratos. A largura de cada faixa é a ordem de grandeza da etapa.])

O cálculo ajuda a sentir o tamanho do efeito. *Primeira etapa:* uma molécula de hormônio ocupa um receptor, e esse único receptor, enquanto está ocupado, ativa dezenas de proteínas G, uma depois da outra — já são cerca de 10² eventos. *Segunda etapa:* cada proteína G ativa uma adenilil-ciclase, que é uma enzima e portanto produz milhares de moléculas de AMPc enquanto está ligada — a conta sobe para algo perto de 10⁴. *Terceira etapa:* cada duas moléculas de AMPc liberam uma subunidade catalítica de #sigla("PKA", [proteína cinase A — a cinase ativada pelo AMPc, executora final da via do glucagon e da adrenalina]), e cada uma dessas fosforila muitos substratos por segundo. Lendo o número final em palavras: *uma única molécula de hormônio na superfície da célula pode se traduzir em cerca de um milhão de moléculas de glicose liberadas do glicogênio*. É essa razão absurda entre sinal e efeito que torna possível governar um tecido inteiro com uma pitada de molécula.

Amplificação dessa magnitude cria, porém, um problema simétrico: um sistema que multiplica por um milhão precisa de freios igualmente rápidos, senão nunca desliga. Os freios existem em cada degrau. A própria proteína G hidrolisa seu GTP e se desliga sozinha em segundos. A #termo-nota[fosfodiesterase][enzima que quebra o AMPc em 5'-AMP, encerrando o sinal — a cafeína inibe fracamente essa enzima, e é por isso que prolonga o efeito de catecolaminas] destrói o AMPc continuamente. E as fosfatases removem os fosfatos que as cinases penduraram. O estado de qualquer proteína regulada por fosforilação é, portanto, um empate dinâmico entre cinase e fosfatase — e o hormônio vence esse cabo de guerra puxando para um dos lados.

#clinica-box("Por que a dosagem de hormônio no sangue é feita por imunoensaio")[
  A concentração plasmática típica de um hormônio é da ordem de nanogramas por mililitro, milhões de vezes menor que a de glicose ou de albumina. Nenhum método químico convencional enxerga tão pouco no meio de tanta proteína. A saída, desenvolvida por Yalow e Berson e mostrada no slide como radioimunoensaio, foi usar a alta afinidade e a especificidade de um anticorpo como se fosse uma lupa: coloca-se uma quantidade fixa de anticorpo e uma quantidade fixa de hormônio marcado, e o hormônio do paciente compete com o marcado pelos sítios do anticorpo. Quanto mais hormônio o paciente tiver, menos marcado sobra ligado — o sinal medido é inversamente proporcional à concentração real. Os imunoensaios modernos trocaram a marcação radioativa por enzimas ou quimioluminescência, mas o princípio competitivo continua o mesmo, e é ele que permite dosar TSH, cortisol e insulina na rotina.
]

#mini-resumo[Hormônio age em concentração ínfima porque o receptor tem afinidade altíssima; produz efeito grande porque a cascata amplifica; e não fica ligado para sempre porque cada degrau tem um mecanismo próprio de desligamento.]

Fechada a lógica geral do sinal, a divisão que organiza o resto do resumo é a que a solubilidade impôs. As duas próximas PARTES são as duas metades dessa divisão: primeiro os hormônios que param na membrana e delegam o recado a mensageiros internos, depois os que atravessam a célula e vão negociar diretamente com o DNA.

#parte-title("PARTE II — Hormônios que ficam na membrana: insulina, glucagon e adrenalina")

#subtopico("2.1 — A insulina é fabricada em três versões, e duas delas são descartadas")

Um hormônio peptídico é uma proteína, e nasce como qualquer proteína: transcrito no núcleo, traduzido num ribossomo do retículo endoplasmático rugoso, empacotado no Golgi, guardado em vesícula. O detalhe que interessa é que a molécula que sai do ribossomo *não é* o hormônio ativo. Ela é um precursor maior, que precisa ser cortado — e cada corte é um ponto de controle.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-22.png",
  largura: 80%,
  legenda: [As três formas da insulina. À esquerda, a pré-pró-insulina, com a sequência-sinal em vermelho na ponta amino. No meio, a pró-insulina já dobrada, com as três pontes dissulfeto em amarelo travando a estrutura. À direita, a insulina madura: cadeias A e B unidas pelas pontes, com o peptídeo C removido e liberado à parte. Embaixo, o percurso pelas organelas — retículo, vesícula de transporte, Golgi, vesícula secretora.])

A sequência começa com a *pré-pró-insulina*. O prefixo "pré" é a #termo-nota[sequência-sinal][trecho de aminoácidos hidrofóbicos na ponta amino que serve de endereço, levando o ribossomo a acoplar no retículo endoplasmático e o peptídeo nascente a entrar no lúmen], removida assim que a cadeia entra no retículo. O que sobra é a *pró-insulina*, uma cadeia única que se dobra sobre si mesma e forma três pontes dissulfeto. Essa etapa de dobramento é o ponto crucial: as pontes se formam enquanto a molécula ainda é contínua, porque a continuidade da cadeia é o que aproxima as cisteínas certas umas das outras.

Só depois de as pontes estarem fechadas é que proteases do Golgi cortam o segmento do meio, o *peptídeo C*. Sobram duas cadeias, A e B, agora separadas na sequência mas amarradas pelas pontes dissulfeto — essa é a insulina madura. O peptídeo C não é lixo: é liberado no sangue junto com a insulina, molécula por molécula, na proporção exata de um para um.

#clinica-box("O peptídeo C separa a insulina que o pâncreas fez da insulina que veio da seringa")[
  A insulina farmacêutica é fabricada pronta, sem peptídeo C. Quem se aplica insulina tem, portanto, insulina alta no sangue e peptídeo C baixo. Quem tem um tumor de célula beta produzindo insulina em excesso tem os dois altos, porque o tumor secreta a molécula pela via normal. Diante de um paciente com hipoglicemia inexplicada, dosar o peptídeo C distingue o tumor da aplicação exógena — e essa distinção não seria possível se o peptídeo C fosse simplesmente degradado no Golgi. Pela mesma lógica, o peptídeo C serve para medir quanta insulina própria ainda resta em quem já usa insulina injetável.
]

#mini-resumo[A pró-insulina se dobra e forma as pontes enquanto ainda é uma cadeia única; o corte do peptídeo C vem depois, e é por isso que a insulina madura consegue ser duas cadeias sem se desmontar.]

#subtopico("2.2 — A célula beta usa a própria glicólise como termômetro da glicemia")

O pâncreas não tem um sensor químico dedicado à glicose. Ele faz algo mais elegante: metaboliza a glicose que chega e usa a *quantidade de ATP produzida* como medida da glicemia. Para isso funcionar, o influxo de glicose para dentro da célula beta precisa acompanhar fielmente a concentração no sangue — e duas peças garantem isso.

A primeira é o #sigla("GLUT2", [transportador de glicose tipo 2, presente na célula beta, no hepatócito e no epitélio intestinal — alta capacidade e baixa afinidade]), o transportador da célula beta e do hepatócito. Sua baixa afinidade é uma vantagem aqui: como ele só satura em concentrações muito altas, a entrada de glicose continua proporcional à glicemia em toda a faixa fisiológica, em vez de empacar. A segunda é a *glicoquinase*, a hexoquinase da célula beta e do fígado.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-25.png",
  largura: 55%,
  legenda: [As duas curvas explicam o sensor. A hexoquinase (verde) já está praticamente saturada na glicemia basal de 5 mM: se a glicose subir, ela não acelera. A glicoquinase (azul) trabalha em torno de metade da velocidade máxima nessa mesma glicemia, na parte inclinada da curva — o que faz sua velocidade subir e descer junto com a glicemia. Um sensor precisa estar na parte inclinada da curva, nunca no platô.])

A hexoquinase dos outros tecidos tem Km baixo, na casa de 0,1 mM, e é inibida pelo próprio produto, a glicose-6-fosfato. Isso é ótimo para um músculo, que quer captar glicose mesmo quando ela está escassa e parar quando já tem o suficiente. Mas é péssimo para um sensor: uma enzima saturada trabalha na velocidade máxima independentemente da glicemia, e portanto não informa nada. A glicoquinase tem Km alto, em torno de 10 mM, e *não* é inibida pela glicose-6-fosfato — sua velocidade sobe e desce acompanhando a glicemia. É essa proporcionalidade que transforma a glicólise da célula beta num termômetro.

Daí em diante a cadeia é mecânica. Mais glicose fosforilada significa mais piruvato, mais oxidação mitocondrial e mais ATP. O ATP se liga ao *canal de potássio sensível ao ATP* e o *fecha*. Com o canal fechado, o potássio que normalmente vazava para fora fica retido, e a face interna da membrana perde negatividade: a célula *despolariza*. A despolarização abre canais de cálcio dependentes de voltagem, o cálcio entra, e o cálcio é o gatilho universal de exocitose — as vesículas carregadas de insulina se fundem à membrana e despejam o conteúdo. Em paralelo, a glicemia alta também aumenta a *transcrição* do gene da insulina, repondo o estoque que acabou de sair.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-26.png",
  largura: 82%,
  legenda: [A cadeia completa da secreção, do GLUT2 à vesícula. Repare no ponto que costuma ser lido ao contrário: a seta do ATP para o canal de K⁺ é de *inibição*. O canal está aberto no repouso e é o fechamento dele que despolariza a membrana.])

#atencao-box("O ATP fecha o canal de potássio — não abre")[
  A leitura intuitiva é que "energia abre as coisas", e ela inverte o mecanismo inteiro. O canal K⁺-ATP fica *aberto* quando a célula está com pouca energia, deixando o potássio escapar e mantendo a membrana polarizada, ou seja, quieta. O ATP é o que o *fecha*. Se você inverter esse passo, todos os efeitos seguintes se invertem junto: você concluirá que a hiperglicemia hiperpolariza a célula beta e inibe a secreção de insulina, que é o oposto do que acontece. Guarde pela consequência final, que é inequívoca: glicose alta termina em insulina secretada.
]

Duas classes de medicamento agem exatamente nesse canal, em sentidos opostos, e demonstram que o mecanismo é esse mesmo. As *sulfonilureias*, usadas no diabetes tipo 2, fecham o canal K⁺-ATP diretamente, sem depender da glicose: a célula despolariza e secreta insulina de qualquer maneira. Isso ajuda no diabetes tipo 2 justamente porque nele a célula beta ainda funciona — o problema é resistência periférica à insulina, e forçar mais secreção contorna parcialmente essa resistência. Do outro lado, no *insulinoma* — tumor de célula beta que secreta insulina sem freio e causa hipoglicemia grave —, o tratamento definitivo é cirúrgico, mas o controle medicamentoso usa ativadores do canal K⁺-ATP, como o diazóxido, que o mantêm aberto e impedem a despolarização.

#figura-lateral("/figuras/bioq-26-controle-hormonal/slide-24.png",
  lado: "right",
  largura-figura: 45%,
  texto: [Os transportadores de glicose merecem uma comparação lado a lado porque cada um resolve um problema diferente. GLUT1 abastece hemácia e barreira hematoencefálica; GLUT2 serve fígado, pâncreas e intestino, com alta capacidade e baixa afinidade; GLUT3 tem afinidade altíssima e garante que o neurônio capte glicose mesmo na hipoglicemia; GLUT4 é o único *dependente de insulina*, e vive no músculo e no tecido adiposo#sigla("GLUT4", [transportador de glicose tipo 4 — o único que só vai à membrana quando a insulina manda]).],
  legenda: [Só o GLUT4 espera ordem da insulina para ir à membrana.])

A independência dos três primeiros e a dependência do quarto explicam uma assimetria clínica importante: no diabetes descompensado, o cérebro continua captando glicose normalmente — GLUT1 e GLUT3 não precisam de insulina —, enquanto músculo e tecido adiposo ficam de fora do banquete, porque sem insulina o GLUT4 permanece guardado em vesículas dentro da célula.

#subtopico("2.3 — A insulina age por tirosina-cinase e sua assinatura é a desfosforilação")

O receptor de insulina é um receptor tirosina-cinase, e o mecanismo dele tem uma consequência que costuma passar batida. Quando a insulina se liga, o receptor se autofosforila em resíduos de tirosina, e esses fosfatos servem de plataforma para proteínas adaptadoras que disparam a via da #sigla("PKB", [proteína cinase B, também chamada Akt — a cinase central da via da insulina]). Até aqui, tudo são fosforilações. A partir da PKB, porém, o efeito predominante se inverte: a PKB *ativa a fosfoproteína fosfatase 1* e *inativa* cinases como a GSK-3.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-32.png",
  largura: 72%,
  legenda: [A via da insulina desenhada pelo que ela liga e desliga. A PKB ativa (no topo) ativa a PP1 e a fosfodiesterase, e inativa a GSK-3 e a PKA. O resultado líquido, na base, é enzima desfosforilada — glicogênio-sintase ativa, glicogênio-fosforilase inativa. Uma cinase no topo produzindo desfosforilação embaixo não é contradição: é o que acontece quando a cinase do topo ativa uma fosfatase.])

O resultado é que a assinatura bioquímica do estado alimentado é a *desfosforilação* das enzimas do metabolismo do combustível, enquanto a assinatura do jejum e do estresse é a *fosforilação*. Vale como regra de leitura para o resto da PARTE: se você não lembrar o que a insulina faz com uma enzima específica, comece perguntando se essa enzima é ativada por fosforilação — se for, a insulina a desliga.

Os efeitos por tecido decorrem disso com bastante economia. No *músculo* e no *tecido adiposo*, a insulina leva o GLUT4 às vesículas até a membrana, aumentando a captação de glicose. No *fígado*, ela não mexe em transportador — o GLUT2 é permanente — e sim no destino da glicose: ativa a glicogênio-sintase, aumenta a expressão de glicoquinase, estimula a glicólise e a síntese de ácidos graxos, e freia a gliconeogênese. No *tecido adiposo*, além da captação, ativa a lipoproteína-lipase, que libera ácidos graxos das lipoproteínas circulantes para serem estocados, e inibe a lipase intracelular, travando a saída de gordura. E em todos os tecidos ela empurra o balanço de nitrogênio para o lado da síntese de proteína.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-33.png",
  largura: 88%,
  legenda: [O mapa de tecidos com a tabela de enzimas-alvo ao lado. Percorra os órgãos na ordem em que a glicose os encontra: intestino, fígado, sangue, músculo, adiposo, cérebro. A insulina age em todos menos no cérebro, cuja captação independe dela.])

#subtopico("2.4 — O glicogênio é o caso-modelo do controle recíproco")

Um mesmo sinal precisa ligar a estocagem e desligar a mobilização — se as duas vias funcionassem juntas, a célula gastaria ATP sintetizando e quebrando o mesmo polímero, num ciclo fútil. O metabolismo do glicogênio resolve isso com um arranjo que vale a pena entender uma vez e reaproveitar sempre: *a mesma modificação química controla as duas enzimas, com sinais opostos*.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-30.png",
  largura: 68%,
  legenda: [O ciclo da glicogênio-sintase. Fosforilada por GSK-3 e CKII, ela fica na forma b, inativa. A PP1 retira os fosfatos e a devolve à forma a, ativa. Embaixo, quem controla a PP1: insulina a ativa; glucagon, adrenalina e glicose-6-fosfato entram na mesma disputa em sentidos diferentes.])

A *glicogênio-sintase* é ativa quando desfosforilada e inativa quando fosforilada. A *glicogênio-fosforilase* é o oposto exato: inativa (forma b) quando desfosforilada, ativa (forma a) quando fosforilada. Como consequência, uma única cinase, a PKA, produz simultaneamente parada da síntese e disparo da quebra — e uma única fosfatase, a PP1, produz simultaneamente disparo da síntese e parada da quebra. O metabolismo do glicogênio nunca fica com as duas vias abertas porque as duas enzimas leem o mesmo interruptor com sinais invertidos.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-31.png",
  largura: 76%,
  legenda: [Os dois níveis de controle da glicogênio-fosforilase. Na horizontal, o controle covalente: a fosforilase-cinase converte b em a, a fosfatase desfaz. Na vertical, o controle alostérico: no músculo, AMP empurra a forma b para o estado ativo mesmo sem fosfato, enquanto ATP e glicose-6-fosfato a puxam de volta; no fígado, a glicose livre inativa a forma a.])

Sobre esse controle covalente existe uma segunda camada, alostérica, que é local e imediata — e ela é *tecido-específica*, o que revela para que serve cada estoque. No músculo, o AMP acumulado num exercício intenso ativa a fosforilase mesmo sem nenhum hormônio ter chegado: a fibra que está gastando ATP libera sua própria glicose na hora, sem esperar recado do pâncreas. No fígado, ao contrário, a *glicose livre* se liga à fosforilase a e a inativa — o hepatócito para de quebrar glicogênio assim que a glicemia se normaliza, porque o estoque hepático existe para abastecer os outros órgãos, não a si mesmo.

#confusao-prevista(
  titulo: "O glicogênio do músculo não sustenta a glicemia",
  aluno_acha: [que o glicogênio muscular, sendo maior em massa total, é a principal reserva de glicose para o sangue],
  mecanismo: [o músculo não tem glicose-6-fosfatase, a enzima que retira o fosfato e permite a glicose sair da célula. A glicose-6-fosfato gerada lá dentro é carregada e não atravessa a membrana, então só pode ser queimada no próprio músculo. Quem exporta glicose é o fígado, que tem a fosfatase — e é por isso que o glucagon age no fígado e não no músculo.],
)

#subtopico("2.5 — Glucagon e adrenalina compartilham a cascata do AMPc")

O glucagon é um peptídeo de 29 aminoácidos produzido pelas células alfa da ilhota, e nasce por processamento pós-traducional de um precursor maior — o mesmo pró-glucagon que, no intestino, é cortado em pontos diferentes e gera peptídeos com outras funções. Sua secreção é estimulada pela hipoglicemia, pela adrenalina e pelo aumento de aminoácidos no sangue, e é inibida pela insulina, pelos corpos cetônicos e pela ureia. Essa lista descreve, em uma linha, o estado que o glucagon serve: pouco açúcar circulando, mas matéria-prima disponível para fabricar mais.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-37.png",
  largura: 70%,
  legenda: [A cascata do glucagon, do receptor 7TM à fosforilase a. Repare no cabeçalho da figura: "epinefrina (músculo) ou glucagon (fígado)" — a mesma cascata, com receptores diferentes em tecidos diferentes. É por isso que aprender uma dessas vias é aprender as duas.])

A cascata tem cinco degraus e vale percorrer nomeando o que muda em cada um. O glucagon se liga ao receptor 7TM no hepatócito; o receptor ativa a proteína G, que troca GDP por GTP; a subunidade alfa ativa a *adenilil-ciclase*, que converte ATP em *AMPc*; o AMPc se liga às subunidades regulatórias da PKA e libera as catalíticas; a PKA fosforila a *fosforilase-cinase*, que por sua vez fosforila a *glicogênio-fosforilase b*, convertendo-a em *a*. Cada degrau é uma enzima agindo sobre muitas cópias do degrau seguinte — é aqui que a pirâmide de amplificação da PARTE I acontece de fato.

E a mesma PKA que liga a quebra do glicogênio desliga a síntese, fosforilando a glicogênio-sintase, e ainda fosforila enzimas da glicólise e da gliconeogênese hepáticas no sentido de fabricar glicose. O efeito integrado do glucagon é o fígado deixando de consumir glicose e passando a exportá-la: quebra de glicogênio, gliconeogênese a partir de aminoácidos e glicerol, mobilização de ácidos graxos no tecido adiposo e produção de corpos cetônicos, que servem de combustível alternativo para o cérebro quando o jejum se prolonga.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-38.png",
  largura: 88%,
  legenda: [O efeito do glucagon tecido a tecido, com a tabela de enzimas-alvo. Compare mentalmente com o mapa da insulina duas páginas atrás: as setas apontam para os lados opostos nas mesmas enzimas. Essa oposição é o eixo insulina–glucagon.])

A adrenalina usa a mesma maquinaria em outro contexto. Sintetizada na medula da suprarrenal a partir da tirosina — pela sequência tirosina, DOPA, dopamina, noradrenalina, adrenalina —, ela é liberada diante de um estresse agudo e prepara o corpo para gastar energia imediatamente. No *fígado*, ativa a quebra de glicogênio como o glucagon faz. No *músculo*, faz o mesmo, mas ali a glicose gerada é consumida localmente, porque falta a glicose-6-fosfatase. No *tecido adiposo*, mobiliza ácidos graxos. E, por cima disso, aumenta a frequência cardíaca, a pressão arterial e o calibre das vias aéreas, entregando mais oxigênio ao músculo. A adrenalina também inibe a secreção de insulina e estimula a de glucagon, reforçando por via hormonal aquilo que já está fazendo por via direta.

#clinica-box("Adrenalina na anafilaxia: três efeitos ao mesmo tempo")[
  O uso da adrenalina na anafilaxia não é escolha arbitrária: cada um dos seus efeitos combate um braço da reação. A vasoconstrição periférica sobe a pressão que despencou por vasodilatação generalizada; a broncodilatação abre as vias aéreas fechadas pelo broncoespasmo; e o aumento da força e da frequência cardíacas mantém o débito diante de um sistema circulatório dilatado. Os mesmos efeitos justificam seu uso na parada cardíaca e no choque. Nenhum outro fármaco reúne essa combinação exata, porque nenhum outro age em toda a família de receptores adrenérgicos ao mesmo tempo.
]

#mini-resumo[Insulina e glucagon movem as mesmas enzimas em sentidos opostos: a insulina desfosforila via PP1, o glucagon fosforila via AMPc e PKA. Quem entende esse par entende quase todo o metabolismo do jejum e da refeição.]

Todos os hormônios desta PARTE param na membrana e mudam a *atividade* de proteínas que já existiam na célula — por isso respondem em segundos e param igualmente rápido. A próxima PARTE trata dos que não param na membrana e, em vez de mudar a atividade das proteínas, mudam quantas proteínas existirão.

#parte-title("PARTE III — Hormônios que entram na célula: tireoidianos e esteroides")

#subtopico("3.1 — Quando o receptor está dentro, o efeito deixa de ser atividade e passa a ser quantidade")

A membrana plasmática é uma barreira para moléculas carregadas e uma porta aberta para moléculas apolares. Esteroides e hormônios tireoidianos são apolares o bastante para atravessá-la por difusão simples, e essa única propriedade física reorganiza toda a lógica da resposta. Não há receptor de superfície, não há segundo mensageiro, não há cascata de cinases. O hormônio encontra seu receptor *dentro* da célula — no citoplasma ou já no núcleo —, e o complexo hormônio-receptor é ele próprio um fator de transcrição.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-15.png",
  largura: 62%,
  legenda: [Os dois mecanismos gerais, lado a lado, na figura clássica do slide. À esquerda, o hormônio peptídico ou amínico que age sem entrar, por segundo mensageiro, alterando a atividade de enzimas preexistentes. À direita, o hormônio esteroide ou tireoidiano que entra, liga-se ao receptor e altera a quantidade de proteína recém-sintetizada. Toda a diferença de velocidade e de duração está nessas duas palavras: atividade e quantidade.])

Uma vez ligado, o receptor muda de conformação, dimeriza, e o dímero se prende a uma sequência específica de DNA chamada *elemento responsivo*, situada na região reguladora dos genes-alvo. Preso ali, ele recruta *coativadores* — proteínas que afrouxam a cromatina e aproximam a maquinaria de transcrição — ou *correpressores*, que fazem o contrário. O gene passa a ser transcrito mais (ou menos), o mRNA é traduzido, e a célula acaba com uma quantidade diferente daquela proteína.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-49.png",
  largura: 72%,
  legenda: [As três etapas do receptor nuclear sobre o DNA: o receptor já ancorado, o ligante chegando e mudando sua conformação, e o coativador sendo recrutado. O ligante não coloca o receptor no DNA — ele muda a superfície do receptor, e é essa superfície nova que atrai o coativador.])

Duas consequências vêm de graça desse desenho, e explicam a divisão de trabalho entre as duas metades da endocrinologia. A primeira é a *latência*: transcrever, traduzir e acumular proteína leva horas, não segundos. A segunda é a *duração*: uma proteína recém-sintetizada permanece na célula por horas a dias, então o efeito persiste muito depois de o hormônio ter sumido do sangue. Hormônio de membrana serve para responder ao que está acontecendo agora; hormônio nuclear serve para configurar como a célula vai se comportar amanhã.

#subtopico("3.2 — O T4 é abundante e quase inativo; quem decide é a enzima do tecido")

Os hormônios tireoidianos partem da tirosina, como as catecolaminas, mas incorporam iodo aos anéis — e é o iodo que constrói a molécula ativa. A tireoide secreta cerca de vinte vezes mais *T4* (tiroxina, com quatro iodos) do que *T3* (tri-iodotironina, com três). A intuição sugeriria que o mais abundante é o principal, e aqui a intuição erra: o T4 tem afinidade baixa pelo receptor nuclear e funciona como *pró-hormônio*, uma reserva circulante de meia-vida longa. O hormônio que efetivamente ocupa o receptor é o T3.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-42.png",
  largura: 82%,
  legenda: [As estruturas mostram por que a posição do iodo importa. Retirando um iodo do anel externo do T4, obtém-se T3 — ativo. Retirando um iodo do anel interno, obtém-se o T3 reverso, que tem exatamente os mesmos três iodos e é inativo. À direita, o percurso: transportador de membrana, conversão intracelular, dímero com o RXR sobre o elemento responsivo do DNA.])

A conversão acontece *nos tecidos periféricos*, por enzimas chamadas desiodases, e é aí que mora a inteligência do sistema. Cada tecido pode retirar um iodo do anel externo, gerando T3 ativo, ou do anel interno, gerando *T3 reverso*, que é inativo. O mesmo T4 circulante pode, portanto, ser convertido em hormônio ativo no coração e em hormônio inerte no músculo, conforme a necessidade local. Em situações de doença grave, jejum prolongado ou estresse, a conversão se desloca para o lado do T3 reverso, e o organismo reduz seu gasto metabólico sem que a tireoide tenha mudado nada — um freio periférico, independente da glândula.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-45.png",
  largura: 82%,
  legenda: [À esquerda, os órgãos-alvo: coração (frequência e hipertrofia), músculo esquelético (catabolismo proteico e uso de glicose), osso (crescimento e maturação), fígado (síntese de colesterol e metabolismo de gordura), cérebro (crescimento neuronal). À direita, o mecanismo dentro da célula: T4 entra, as desiodases DIO1 e DIO2 o convertem em T3, o T3 se liga ao receptor TR que dimeriza com o RXR sobre o TRE, e a transcrição acontece.])

Sobre o DNA, o receptor de hormônio tireoidiano forma um par com o *receptor de retinoide X*, e é esse heterodímero que ocupa o elemento responsivo. O efeito líquido é o aumento do metabolismo basal: mais enzimas oxidativas, mais consumo de oxigênio, mais produção de calor, mais receptores adrenérgicos no coração — o que explica por que a taquicardia e o tremor do hipertireoidismo se parecem tanto com excesso de adrenalina, sem que a adrenalina esteja aumentada. No sistema nervoso em desenvolvimento, o hormônio tireoidiano é indispensável para a maturação neuronal, e sua falta no início da vida produz dano cognitivo irreversível — razão pela qual o rastreamento neonatal existe.

#clinica-box("Hipo e hipertireoidismo lidos como excesso ou falta de metabolismo basal")[
  Quase todos os sintomas das duas doenças se deduzem de uma única variável. No *hipotireoidismo*, tudo desacelera: frequência cardíaca baixa, intolerância ao frio porque se produz menos calor, ganho de peso, lentidão de raciocínio, constipação, pele seca e colesterol alto — este último porque o hormônio tireoidiano estimula a depuração hepática do colesterol, e sem ele a depuração cai. No *hipertireoidismo*, tudo acelera: taquicardia e palpitação, intolerância ao calor e sudorese, perda de peso apesar de apetite aumentado, tremor, ansiedade, insônia e diarreia. O bócio aparece nas duas condições porque o aumento da glândula responde ao estímulo do TSH ou à própria doença de base, não ao nível de hormônio no sangue.
]

#subtopico("3.3 — O cortisol nasce do colesterol e é governado por um eixo com freio próprio")

Todo hormônio esteroide começa no *colesterol* e a primeira reação é sempre a mesma: a enzima desmolase corta a cadeia lateral e produz *pregnenolona*. Esse é o passo limitante da via inteira e o ponto onde o controle hormonal entra — o #sigla("ACTH", [hormônio adrenocorticotrófico, secretado pela adeno-hipófise, que estimula a produção de cortisol no córtex da suprarrenal]) age justamente acelerando essa conversão. Da pregnenolona em diante, a via se ramifica, e o conjunto de enzimas presentes em cada zona do córtex adrenal decide qual produto final sai: aldosterona na zona mais externa, cortisol na intermediária, androgênios na mais interna.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-51.png",
  largura: 86%,
  legenda: [A árvore de síntese dos esteroides adrenais. Tudo parte do colesterol e passa pela pregnenolona; as hidroxilases sucessivas conduzem a via até aldosterona, cortisol ou androgênios. Perceba que as três famílias compartilham os primeiros passos — é por isso que o bloqueio de uma enzima intermediária desvia o fluxo para os outros ramos, em vez de simplesmente reduzir tudo.])

O cortisol é controlado por um eixo de três andares. O hipotálamo secreta #sigla("CRH", [hormônio liberador de corticotrofina, produzido no hipotálamo — no slide aparece como CRF]), que faz a hipófise secretar ACTH, que faz o córtex da suprarrenal produzir cortisol. O cortisol, por sua vez, volta pelo sangue e *inibe* tanto o hipotálamo quanto a hipófise. Essa retroalimentação negativa é o que mantém a concentração estável: quando o cortisol sobe, o estímulo cai; quando o cortisol cai, o estímulo sobe.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-50.png",
  largura: 70%,
  legenda: [O eixo hipotálamo-hipófise-adrenal com as duas alças de retroalimentação negativa em verde. O estresse entra por cima, no hipotálamo. Embaixo, a observação que explica a pele de Addison: o ACTH compartilha os primeiros aminoácidos com o MSH, o hormônio estimulante de melanócito.])

Dentro da célula-alvo, o receptor de glicocorticoide espera no citoplasma preso a proteínas de choque térmico, entre elas a HSP90. Elas o mantêm numa conformação inativa e impedem sua entrada no núcleo. Quando o cortisol chega e se liga, essas chaperonas se soltam, o receptor expõe o sinal de localização nuclear, entra no núcleo, dimeriza e se prende ao elemento responsivo a glicocorticoide, ativando ou reprimindo a transcrição de centenas de genes.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-52.png",
  largura: 78%,
  legenda: [O percurso do glicocorticoide: atravessa a membrana, encontra o receptor ancorado à proteína de choque térmico 90, o complexo entra no núcleo e se liga aos elementos responsivos. À direita, os três resultados possíveis, todos em nível de transcrição — mais ou menos mRNA, mais ou menos proteína.])

#subtopico("3.4 — O cortisol é o hormônio do estresse prolongado, e seus extremos têm nome")

O cortisol prepara o corpo para uma agressão que dura, e faz isso convertendo tecido em glicose. No *fígado*, aumenta a gliconeogênese e o estoque de glicogênio. No *músculo esquelético*, faz o oposto do que a insulina faria: reduz a captação de glicose e degrada proteína, liberando aminoácidos que servirão de matéria-prima para a gliconeogênese hepática. No *tecido adiposo*, reduz a captação de glicose e ativa a lipólise, liberando glicerol — outro precursor de glicose. No *pâncreas*, inibe a secreção de insulina pelas células beta e estimula a de glucagon pelas alfa. Todos esses efeitos apontam para o mesmo lugar: glicose disponível no sangue para o cérebro, às custas de músculo e gordura.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-53.png",
  largura: 88%,
  legenda: [À esquerda, os efeitos sistêmicos do cortisol elevado por tempo longo. À direita, a leitura tecido a tecido — fígado, músculo, tecido adiposo e pâncreas — que mostra o mesmo objetivo em quatro lugares: manter a glicemia. Repare que o efeito no músculo e no adiposo é literalmente o inverso do da insulina.])

Sobre esse eixo metabólico existe um segundo, imunológico: o cortisol reprime a transcrição de genes de citocinas inflamatórias e reduz a proliferação de linfócitos. É essa propriedade que faz dos glicocorticoides sintéticos os anti-inflamatórios mais potentes da medicina — e é a mesma propriedade que explica seus efeitos adversos, porque um sinal que atua na transcrição de centenas de genes não tem como ser seletivo.

#clinica-box("Addison e Cushing: a mesma via, dois sentidos")[
  Na *doença de Addison*, o córtex da suprarrenal é destruído, em geral por autoimunidade, e falta cortisol. Sem cortisol, o freio da retroalimentação desaparece e a hipófise dispara ACTH. Como o ACTH nasce do mesmo precursor que o hormônio estimulante de melanócito e compartilha com ele os primeiros aminoácidos, o excesso de ACTH escurece a pele — a hiperpigmentação de Addison é consequência da *falta* de cortisol, não do excesso. Some-se a isso hipotensão, fadiga, hipoglicemia e perda de peso.

  Na *síndrome de Cushing*, o cortisol sobra, seja por tumor, seja pelo uso prolongado de corticoide. O resultado é a soma dos efeitos metabólicos amplificados: hiperglicemia, perda de massa muscular nos membros, redistribuição de gordura para o tronco e a face, pele fina e imunossupressão. Vale reparar no detalhe fisiológico da redistribuição: o cortisol aumenta a lipólise na gordura periférica e ao mesmo tempo favorece a diferenciação de adipócitos no depósito central, e é a combinação dos dois que produz o padrão característico.
]

O último assunto da aula fecha o círculo de volta na PARTE I. *Disruptores endócrinos* são moléculas ambientais — plastificantes, pesticidas, componentes de embalagens — cuja forma se parece o suficiente com a de um hormônio para interagir com seus receptores. Elas agem de duas maneiras. Como *miméticos*, ligam-se ao receptor e o ativam, produzindo resposta hormonal sem que o hormônio exista. Como *bloqueadores*, ocupam o receptor sem ativá-lo e impedem o hormônio verdadeiro de se ligar.

#figura-nebli("/figuras/bioq-26-controle-hormonal/slide-55.png",
  largura: 76%,
  legenda: [Os três cenários lado a lado: o hormônio normal ativando o receptor; o mimético, com forma parecida, ativando o receptor sem ser hormônio; e o bloqueador, ocupando o receptor e impedindo a resposta. Os disruptores atingem preferencialmente as vias de receptor nuclear, cujos ligantes são pequenos e lipossolúveis — exatamente o perfil químico dos poluentes que se acumulam na gordura.])

#mini-resumo[Se a especificidade da resposta hormonal está no receptor, e não no hormônio, então qualquer molécula com a forma certa consegue falar com o receptor. O disruptor endócrino é a evidência incômoda dessa regra.]

#conclusao-box[
  *O princípio que unifica tudo.* Um hormônio não carrega instruções: ele carrega apenas presença. Toda a informação da resposta está do lado de quem recebe — no receptor que existe naquele tecido, na cascata que ele aciona, nas enzimas que estão lá para serem ligadas ou desligadas. É por isso que a mesma adrenalina acelera o coração e contrai a pele, e que a mesma insulina abre a captação de glicose no músculo e reprograma o destino do carbono no fígado.

  *O mecanismo nuclear.* A propriedade física da molécula determina tudo o que vem depois. Hidrossolúvel para na membrana, delega o recado a um segundo mensageiro, amplifica a cascata em ordens de grandeza e muda a *atividade* de proteínas que já existiam — resposta em segundos, término em segundos. Lipossolúvel atravessa a membrana, encontra o receptor dentro da célula, ocupa um elemento responsivo no DNA e muda a *quantidade* de proteína que a célula terá — resposta em horas, duração em dias. Insulina, glucagon e adrenalina são a primeira metade; tireoidianos e cortisol, a segunda.

  *A clínica, retomada pelo mecanismo.* As doenças que apareceram aqui não são exceções ao sistema: são o sistema visto pelo ponto onde quebrou. O peptídeo C distingue insulina própria de insulina injetada porque a insulina madura nasce de um corte. A sulfonilureia funciona porque o canal de potássio é o gatilho da secreção, e o diazóxido funciona pelo motivo simétrico. O T3 reverso permite ao corpo baixar o metabolismo sem mexer na tireoide, porque a conversão é periférica. A pele escura de Addison denuncia ACTH alto, porque a retroalimentação negativa perdeu o freio. Cada sinal clínico é uma etapa do mecanismo aparecendo por fora.

  *Para onde isso vai.* Este resumo tratou de como o sinal chega e o que ele muda dentro da célula. O passo seguinte é ver o organismo inteiro respondendo a esses sinais ao longo do tempo — a integração metabólica do jejum curto, do jejum prolongado, do exercício e do estado alimentado, em que fígado, músculo, tecido adiposo e cérebro trocam combustíveis segundo a razão insulina/glucagon. Todo esse comportamento é executado pelas cascatas desta aula.
]
