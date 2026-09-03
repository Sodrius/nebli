#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Diabetes mellitus não é uma doença de açúcar alto. É uma doença de *sinal*: um hormônio que deveria dizer à célula "há comida chegando, guarde" para de ser produzido, ou para de ser escutado. Tudo o que vem depois — a sede, o emagrecimento, a úlcera que não fecha, o rim que encolhe, a coronária que entope aos quarenta anos — desce desse mesmo defeito por uma cadeia que dá para acompanhar passo a passo.

Este resumo percorre essa cadeia em três movimentos. A *PARTE I* mostra por que a glicose sobe, e como dois defeitos opostos — a fonte destruída e o sinal ignorado — chegam ao mesmo número no exame. A *PARTE II* pega a glicose alta e mostra o que ela faz quimicamente às proteínas do corpo, transformando um distúrbio metabólico em lesão estrutural que se auto-alimenta. A *PARTE III* vai aos órgãos onde essa lesão aparece — olho, rim, nervo, pé, artéria — e mostra o que o patologista vê no tecido e o que o radiologista vê na imagem do mesmo paciente.
]

#parte-title("PARTE I — O sinal que falta: por que a glicose sobe", primeira: true)

#subtopico("1.1 — O que a insulina manda a célula fazer")

A insulina é o sinal de fartura do organismo. Ela é secretada pela célula beta da ilhota pancreática quando a glicose plasmática sobe, e a mensagem que carrega para os tecidos é curta: *chegou combustível, guarde e pare de produzir*. Entender o diabetes exige entender exatamente o que essa frase manda cada tecido fazer — porque a doença é, do começo ao fim, a ausência dessa ordem.

O caminho começa na membrana. O receptor de insulina não aciona proteína G nem segundo mensageiro: ele *é* a enzima. Duas subunidades externas ligam o hormônio e mudam de conformação; duas subunidades internas, que têm atividade de tirosina-quinase, se autofosforilam e passam a fosforilar substratos próprios, entre eles a proteína #sigla("IRS-1", [substrato 1 do receptor de insulina — a primeira proteína fosforilada pelo receptor, e o ponto onde a via se ramifica]). O IRS-1 fosforilado recruta a #sigla("PI3K", [fosfatidilinositol-3-quinase — enzima que converte o sinal do receptor em um lipídeo de membrana capaz de ancorar a Akt]), que ativa a Akt. É a partir daí que os efeitos aparecem.

O mais visível deles é o transporte de glicose. O transportador #sigla("GLUT-4", [transportador de glicose tipo 4 — isoforma insulino-dependente do músculo esquelético e do tecido adiposo]) já está pronto dentro da célula, estocado em vesículas; a Akt manda essas vesículas se fundirem à membrana plasmática. *A insulina não fabrica o transportador, ela o traz para a superfície* — e é por isso que o efeito acontece em minutos e desaparece em minutos quando o sinal cessa.

O resto do programa é igualmente importante e costuma ser esquecido. A insulina ativa a glicogênio-sintase e liga o armazenamento hepático e muscular; liga a lipogênese no adipócito; e, sobretudo, *desliga freios*: inibe a lipase hormônio-sensível, que quebraria triglicerídeo em ácido graxo; freia a gliconeogênese hepática; e reduz a proteólise muscular. Perder insulina não é perder um efeito, é perder todos esses freios ao mesmo tempo.

Um detalhe carrega meio resumo: *nem toda célula precisa de insulina para captar glicose*. Só músculo esquelético e tecido adiposo dependem do GLUT-4. Neurônio, hemácia, endotélio, célula mesangial do glomérulo, pericito da retina, cristalino e epitélio tubular renal usam transportadores que não obedecem ao hormônio. Na fartura isso não faz diferença. Na hiperglicemia crônica faz toda — e a PARTE II volta a esse ponto.

#figura-lateral("/figuras/gr-02-diabetes-mellitus/slide-14.png",
  lado: "right",
  largura-figura: 42%,
  texto: [Antes de a glicose sequer chegar ao sangue, o intestino já avisou o pâncreas. Hormônios liberados pela chegada do alimento ao lúmen — o principal deles o #sigla("GLP-1", [peptídeo semelhante ao glucagon 1 — hormônio intestinal que amplifica a secreção de insulina dependente de glicose]) — potencializam a secreção de insulina pela célula beta. Esse é o *efeito incretínico*, e ele explica por que a mesma quantidade de glicose eleva mais a insulina quando ingerida do que quando injetada na veia. O GLP-1 ainda age no encéfalo aumentando saciedade e retarda o esvaziamento gástrico.],
  legenda: [O eixo intestino–pâncreas–encéfalo: o alimento avisa antes de ser absorvido.])

#subtopico("1.2 — Tipo 1: a ilhota destruída e o corpo em jejum permanente")

O diabetes tipo 1 costuma ser resumido como "falta insulina", e essa frase esconde o mecanismo. O que desencadeia o quadro clínico não é o valor absoluto da insulina, e sim a *razão insulina/glucagon* despencando. A insulina, além de agir nos tecidos periféricos, freia a célula alfa vizinha dentro da própria ilhota. Sem ela, o glucagon é secretado sem contraposição, e o fígado recebe ordem contínua de produzir glicose enquanto o músculo já não consegue captá-la. A hiperglicemia é gerada nas duas pontas ao mesmo tempo.

A origem do defeito é imunológica. Linfócitos T autorreativos, em indivíduos com haplótipos de #sigla("HLA", [antígeno leucocitário humano — o complexo principal de histocompatibilidade humano, cujos alelos de classe II definem boa parte do risco genético do tipo 1]) de classe II predisponentes, destroem progressivamente a célula beta. Os autoanticorpos que se dosam no laboratório — contra a #termo-nota[descarboxilase do ácido glutâmico][enzima da célula beta contra a qual se formam os anticorpos anti-GAD65, marcador sorológico de autoimunidade contra a ilhota], contra a insulina, contra a tirosina-fosfatase da ilhota — são *marcadores* dessa agressão, não os principais executores dela. O dano é feito sobretudo por célula, e o anticorpo é o rastro que ela deixa.

Para saber quanta ilhota ainda funciona, mede-se o #termo-nota[peptídeo C][fragmento liberado junto com a insulina quando a pró-insulina é clivada; como a insulina injetada não o contém, ele mede a produção própria do pâncreas]. A pró-insulina é clivada em insulina e peptídeo C em quantidades iguais, mas a insulina aplicada por via subcutânea não traz peptídeo C junto, e o fígado extrai grande parte da insulina já na primeira passagem. Dosar peptídeo C é, portanto, medir produção endógena residual — e é isso que separa um pâncreas que ainda secreta de um que já parou.

O que acontece com o metabolismo daí em diante é reconhecível: *o corpo se comporta como se estivesse em jejum, com o sangue cheio de glicose*. Sem o freio da insulina, a lipase hormônio-sensível libera ácidos graxos do tecido adiposo em torrente. O fígado os oxida, gera acetil-CoA muito além da capacidade do ciclo de Krebs de consumi-lo, e desvia o excedente para acetoacetato e β-hidroxibutirato. São ácidos fortes, e o acúmulo derruba o pH — a cetoacidose. Em paralelo, a proteólise muscular fornece aminoácidos para a gliconeogênese e o balanço nitrogenado fica negativo. Emagrece-se comendo mais, porque se perde caloria na urina, gordura na lipólise e proteína no músculo.

#mini-resumo[Falta de insulina → glucagon sem freio + lipólise sem freio → glicose hepática alta e ácido graxo em excesso → cetoácidos. Hiperglicemia e cetose são dois efeitos do mesmo defeito, não um causando o outro.]

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-12.png",
  largura: 72%,
  legenda: [Repare que o defeito está em andares diferentes: no tipo 1 o pâncreas não entrega o sinal; no tipo 2 o sinal chega em quantidade e a célula-alvo não responde. É a mesma glicemia alta por dois caminhos opostos.])

#clinica-box("O caso que abre a aula", [
Homem de 26 anos, magro, com dez dias de poliúria, polidipsia e perda de 3 kg. Glicemia de 397 mg/dL no pronto-socorro. No ambulatório, hemoglobina glicada de 8,8%, peptídeo C de 1,32 ng/mL e anticorpo anti-descarboxilase do ácido glutâmico de 1082 UI/mL, para um valor de referência abaixo de 10.

Cada número diz uma coisa distinta e as três juntas fecham o raciocínio. O anticorpo em título muito alto identifica a *natureza autoimune* da destruição da ilhota. O peptídeo C ainda mensurável, no limite inferior da normalidade, mostra que há secreção residual — o paciente está no início da história, com parte da massa de célula beta ainda viva, o que explica ele ter chegado sem acidose franca. A hemoglobina glicada de 8,8% informa que a hiperglicemia não começou nos dez dias de sintomas: ela já vinha havia semanas, silenciosa, até a reserva funcional cair abaixo do ponto em que os sintomas aparecem. O pai, que teve diabetes tipo 1 aos 34 anos, ancora a predisposição genética.
])

#subtopico("1.3 — Tipo 2: resistir ao sinal antes de perder a fonte")

Se no tipo 1 a fonte do sinal foi destruída, no tipo 2 o sinal chega e não é escutado. A diferença parece sutil e muda tudo — inclusive a inversão que mais atrapalha o aluno neste tema.

O ponto de partida costuma ser o excesso de ácido graxo. Com oferta calórica alta e pouca atividade, o músculo recebe mais acil-CoA graxo do que consegue oxidar; o excedente é desviado para triacilglicerol intramuscular e, no caminho, acumula dois intermediários lipídicos com atividade de sinalização, o diacilglicerol e a ceramida. Esses intermediários ativam *serina-quinases de estresse*, e aqui está o nó: elas fosforilam o IRS-1 em resíduos de serina em vez de tirosina. O IRS-1 fosforilado no lugar errado não recruta a PI3K, a Akt não é ativada, e menos vesículas de GLUT-4 chegam à membrana. O receptor está intacto; quem falhou foi o degrau seguinte.

O tecido adiposo colabora por uma segunda via. O adipócito hipertrofiado recruta macrófagos e passa a secretar citocinas pró-inflamatórias, entre elas o fator de necrose tumoral alfa e a interleucina-6. Essas citocinas ativam as mesmas serina-quinases e reduzem a expressão de GLUT-4 na superfície — a obesidade funciona como inflamação crônica de baixo grau, e é por essa ponte que ela produz resistência à insulina.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-09.png",
  largura: 60%,
  legenda: [Siga a rota do ácido graxo dentro do miócito: ele não apenas compete com a glicose como combustível — ele *interrompe a sinalização* que traria o GLUT-4 à superfície. A mitocôndria sobrecarregada devolve espécies reativas de oxigênio, que realimentam as serina-quinases.])

Resistir ao sinal não é, por si só, ter diabetes. A célula beta percebe a glicemia subindo e responde secretando mais: instala-se uma *hiperinsulinemia compensatória* que segura a glicose em faixa quase normal por anos. É este o ponto em que a inversão acontece.

#atencao-box("No tipo 2, a insulina pode estar alta", [
Ler "diabetes" e concluir "insulina baixa" custa caro aqui. No tipo 2, durante a maior parte da história natural, a insulina está *normal ou elevada* — e a glicemia sobe apesar disso, porque o tecido não responde. Insulina alta com glicemia alta não é contradição laboratorial; é o retrato exato da resistência. Ela só cai quando, depois de anos de sobrecarga secretora e de exposição a glicose e ácido graxo em excesso, a célula beta entra em apoptose e a massa de ilhota diminui — e é aí que o tipo 2 passa a precisar de insulina exógena.
])

O defeito também não é de um órgão só. O fígado resiste ao freio da gliconeogênese e mantém produção de glicose mesmo com insulina alta. O adipócito resiste ao freio da lipólise e continua exportando ácido graxo. O intestino perde parte do efeito incretínico. E a própria ilhota contribui com hiperglucagonemia, além da queda de secreção. É um defeito distribuído, e é por isso que nenhuma intervenção isolada resolve o quadro.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-11.png",
  largura: 66%,
  legenda: [Cinco endereços do mesmo defeito. Guarde a leitura do fígado — produção hepática de glicose que não desliga — porque é ela que explica a hiperglicemia de jejum, quando não houve refeição nenhuma para justificá-la.])

#subtopico("1.4 — Da glicose alta ao sintoma: diurese osmótica e as duas descompensações")

Pense no túbulo renal como uma esteira que recolhe de volta o que o glomérulo filtrou. A glicose é filtrada livremente e reabsorvida quase por inteiro no túbulo proximal — enquanto houver transportador disponível. Esses transportadores têm capacidade máxima, e ela é atingida quando a glicemia passa de aproximadamente 180 mg/dL. Acima desse limiar, a esteira satura e a glicose excedente segue no lúmen.

O que acontece em seguida é física de solução. *Soluto que não é reabsorvido retém água consigo*: a glicose no lúmen exerce pressão osmótica e impede que a água acompanhe o sódio de volta ao interstício. O volume urinário sobe — é a #termo-nota[diurese osmótica][perda aumentada de água na urina causada por um soluto não reabsorvido que a retém no lúmen tubular]. A poliúria, portanto, não é causada pela sede: ela vem primeiro, desidrata o paciente, eleva a osmolaridade plasmática, e só então os osmorreceptores hipotalâmicos disparam a polidipsia. Junto com a água partem sódio e potássio.

A perda de peso soma três parcelas. Perde-se caloria diretamente na urina, sob a forma de glicose que nunca foi aproveitada; perde-se gordura pela lipólise desinibida; e perde-se massa muscular pela proteólise que alimenta a gliconeogênese. Em paralelo, a célula continua sinalizando fome porque a glicose não entrou nela — daí a polifagia. O paciente come mais e emagrece, e isso é coerente, não paradoxal.

Quando o quadro descompensa de vez, o caminho depende de quanta insulina ainda existe, e é aqui que os dois tipos se separam com clareza. No tipo 1, com insulina praticamente ausente, a lipólise fica livre e a via segue até os cetoácidos: instala-se a *cetoacidose diabética*, com pH baixo, #termo-nota[hiato aniônico][diferença entre os cátions e os ânions medidos no plasma; aumenta quando um ácido não medido, como o cetoácido, se acumula] aumentado e respiração ampla e profunda — que não é doença pulmonar, e sim compensação respiratória, com o organismo eliminando gás carbônico para tamponar a acidez. No tipo 2, a insulina residual, embora insuficiente para normalizar a glicemia, ainda basta para segurar a lipase hormônio-sensível; sem lipólise maciça não há cetose, e a descompensação toma o outro rumo: glicemias muito mais altas, diurese osmótica prolongada e o *estado hiperosmolar*, com desidratação profunda e rebaixamento de consciência.

#confusao-prevista(
  titulo: "Hiperosmolaridade e acidose não são o mesmo distúrbio",
  aluno_acha: [o aluno trata as duas descompensações como graus de gravidade da mesma coisa],
  mecanismo: [são distúrbios de naturezas diferentes que apenas coexistem na cetoacidose. A hiperosmolaridade é um distúrbio de *água*, produzido pela diurese osmótica; a acidose é um distúrbio de *ácido*, produzido pelos cetoácidos da lipólise. No estado hiperosmolar do tipo 2, a primeira aparece sozinha — e é ela que ameaça a vida.],
)

Um detalhe do potássio merece atenção porque inverte a leitura do exame. A diurese osmótica arrasta potássio para fora do corpo, esvaziando o estoque total. Ao mesmo tempo, a acidose e a falta de insulina deslocam potássio de dentro das células para o plasma. O resultado é um potássio sérico normal ou até elevado num paciente profundamente depletado — e o valor despenca assim que a insulina começa a empurrar o íon de volta para dentro da célula.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-10.png",
  largura: 70%,
  legenda: [A história natural do tipo 2 lida da esquerda para a direita: a resistência muscular vem primeiro, a hiperinsulinemia compensa por anos, e o diagnóstico só chega quando a célula beta descompensa. O paciente já conviveu com hiperglicemia antes de qualquer sintoma — e é esse tempo silencioso que a PARTE II transforma em lesão.])

#parte-title("PARTE II — Do açúcar ao dano: glicação, AGEs e as rotas que perpetuam")

#subtopico("2.1 — Glicação não-enzimática: base de Schiff, Amadori e AGE")

A glicose é um açúcar redutor: ela tem um grupo carbonil livre, e grupos carbonil reagem espontaneamente com grupos amino. Essa reação acontece o tempo todo, em qualquer pessoa, sem enzima nenhuma para catalisá-la ou dirigi-la. A única variável que a governa é o produto entre *quanta* glicose há e por *quanto tempo* ela ficou lá. É por isso que a hiperglicemia crônica lesa quimicamente — e é aqui que o diabetes deixa de ser um distúrbio metabólico e vira uma doença estrutural.

A primeira coisa a separar é o nome. *Glicosilação* é enzimática, dirigida a sítios específicos, parte normal da maturação de glicoproteínas. *Glicação* é a reação espontânea de que estamos tratando: sem enzima, sem sítio preferencial, sem controle. Confundir as duas apaga justamente a característica que faz da glicação um marcador fiel da glicemia.

A reação avança em três estágios, e cada um tem uma escala de tempo e um grau de reversibilidade próprios.

O primeiro estágio é a *base de Schiff*: o carbonil da glicose se condensa com um grupo amino livre da proteína — tipicamente a lisina, ou a valina terminal de uma cadeia — formando uma ligação instável. Isso leva horas e é francamente reversível: se a glicemia cai, a ligação se desfaz e a proteína volta ao normal.

O segundo estágio é o *produto de Amadori*: a base de Schiff sofre um rearranjo molecular que a estabiliza numa cetoamina. Leva dias e é muito menos reversível, embora ainda o seja lentamente. A hemoglobina glicada e a frutosamina que se dosam no laboratório são produtos de Amadori.

O terceiro estágio é o #sigla("AGE", [produto final de glicação avançada — do inglês *advanced glycation end product*, a forma irreversível da glicação]) propriamente dito: ao longo de semanas a meses, o produto de Amadori sofre desidratações, oxidações e rearranjos e acaba por formar *ligações cruzadas* entre dois radicais protéicos diferentes. Aqui a reação deixa de voltar. A proteína modificada não retorna ao estado original nem quando a glicemia normaliza.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-15.png",
  largura: 76%,
  legenda: [A régua de tempo no alto da figura é o que carrega o mecanismo: horas, dias, semanas a meses. Note onde a barra "reversível" termina — o ponto sem volta não é a ligação inicial nem o rearranjo, é a ligação cruzada entre duas cadeias protéicas na etapa final.])

Uma consequência decorre direto da escala de tempo: *quem acumula AGE é a proteína de meia-vida longa*. Colágeno, elastina, cristalino e membrana basal são renovados mais devagar do que a reação avança, e por isso reticulam. Proteína de turnover rápido é degradada e substituída antes de chegar ao terceiro estágio. O alvo do dano, portanto, não é escolhido pela química — é escolhido pela permanência.

#mini-resumo[Schiff em horas e reversível → Amadori em dias e pouco reversível → AGE em meses e irreversível. O tempo que a glicose passa alta define até onde a reação avança, e a proteína que fica muito tempo no lugar é a que paga.]

#subtopico("2.2 — Hemoglobina glicada e frutosamina: dois relógios, duas janelas")

O estágio de Amadori descrito acima não serve só para lesar: ele é a base dos dois exames que traduzem controle glicêmico em número. Ambos medem a mesma reação química; o que muda entre eles é *qual proteína* foi glicada — e, com ela, quanto tempo de história o exame guarda.

A #sigla("HbA1c", [hemoglobina glicada — fração da hemoglobina A que sofreu glicação, expressa em porcentagem da hemoglobina total]) mede a fração da hemoglobina que sofreu glicação dentro da hemácia. Como a hemácia circula de 90 a 120 dias e não tem maquinaria para reverter a modificação, a molécula acumula glicação ao longo de toda a sua vida. O exame é, portanto, uma *integral* da exposição à glicose ao longo de 8 a 12 semanas, com peso maior para as últimas quatro. Não é uma glicemia média medida com mais precisão: é uma medida de outra grandeza.

Vale ler o número do caso da PARTE I em palavras. Uma HbA1c de 8,8% corresponde a uma exposição média em torno de 205 mg/dL ao longo de três meses. O paciente relatava sintomas havia dez dias — mas a hemoglobina dele registra hiperglicemia sustentada muito antes disso. *O sintoma marca o momento em que a reserva de célula beta ficou insuficiente; o exame marca quando a glicose começou a subir.* Não é a mesma data.

Daí decorre a limitação do exame, que é sempre a mesma: ele depende de quanto tempo a hemácia viveu. Qualquer condição que encurte a sobrevida eritrocitária — hemólise, sangramento recente, transfusão — derruba a HbA1c com a mesma glicemia; condições que a prolongam ou que alteram a hemoglobina podem elevá-la falsamente. A HbA1c se interpreta com o hemograma ao lado, nunca sozinha.

É exatamente aí que entra a #termo-nota[frutosamina][conjunto das proteínas plasmáticas glicadas, sobretudo a albumina; como a albumina vive de 14 a 20 dias, o exame reflete as últimas 2 a 3 semanas]. A albumina circula de 14 a 20 dias, e o exame lê uma janela de 2 a 3 semanas. Ele serve justamente quando a HbA1c não serve: hemoglobinopatia, anemia hemolítica, gestação, ou mudança recente de tratamento em que se quer saber se as duas últimas semanas melhoraram, sem esperar três meses.

No caso da aula, os dois exames caminharam juntos e contam a mesma história em escalas diferentes: em abril, HbA1c de 8,8% e frutosamina de 575 μmol/L, ambas muito acima da faixa de referência; em agosto, quatro meses depois de iniciada a insulinização, HbA1c de 5,2% e frutosamina de 289 μmol/L. A frutosamina teria mostrado a melhora semanas antes da HbA1c — e a HbA1c, ao chegar a 5,2%, demonstra que a melhora se sustentou por meses e não foi um bom mês isolado.

#subtopico("2.3 — O que o AGE faz nas proteínas de vida longa")

O erro fácil aqui é imaginar que o AGE apenas enrijece o que reticula. A rigidez existe, mas o dano relevante é outro e vale a pena nomeá-lo com precisão: *a proteína reticulada resiste à digestão proteolítica e deixa de ser substituída*. A matriz extracelular do diabético não é só mais dura — ela é uma matriz que envelhece sem trocar, porque o remodelamento normal, que depende de degradar o colágeno velho para depositar colágeno novo, encontra um substrato que as proteases não conseguem cortar. É esta a razão bioquímica de a ferida do diabético cicatrizar mal mesmo quando a perfusão está preservada.

O segundo alvo é a lipoproteína. A glicação da #sigla("LDL", [lipoproteína de baixa densidade — partícula que transporta colesterol do fígado para os tecidos]) atrapalha o reconhecimento da partícula pelo seu receptor hepático, prolonga o tempo que ela passa na circulação e favorece que ela seja oxidada. A partícula assim modificada deixa de ser captada pela via regulada e passa a ser reconhecida por *receptores scavenger* de macrófago — receptores que, ao contrário do receptor de LDL, não são inibidos pelo colesterol já acumulado dentro da célula. O macrófago come sem freio e vira #termo-nota[célula espumosa][macrófago repleto de gotículas lipídicas, elemento fundador da estria gordurosa e da placa de ateroma]. Esse é o elo direto entre hiperglicemia e placa de ateroma, e a PARTE III vai buscá-lo.

O terceiro alvo é a membrana basal, e ele produz o achado mais contraintuitivo do tema.

#confusao-prevista(
  titulo: "Membrana basal mais espessa não filtra melhor",
  aluno_acha: [o aluno raciocina que engrossar a barreira deveria retê-la mais e reduzir a passagem de proteína],
  mecanismo: [o que muda não é só a espessura, é a *composição*. A membrana basal glomerular do diabético ganha matriz desorganizada e perde proteoglicanos aniônicos, que são a barreira de carga que repelia a albumina — também aniônica. O resultado é uma membrana mais espessa e, ao mesmo tempo, mais permeável a proteína. Espessura maior com barreira pior é o paradoxo central da nefropatia diabética.],
)

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-17.png",
  largura: 58%,
  legenda: [À esquerda, a membrana basal normal: fina, homogênea, com os pedicelos regularmente espaçados sobre ela. À direita, a mesma barreira no diabético — espessada e desorganizada, com o processo epitelial apoiado sobre uma matriz que já não retém a albumina.])

Há ainda um efeito que não depende de estrutura nenhuma: os AGEs *inativam o óxido nítrico*. Menos óxido nítrico disponível significa menos vasodilatação, mais adesão de leucócito e plaqueta ao endotélio e mais proliferação de músculo liso na parede. É disfunção endotelial instalada antes que exista qualquer placa visível em qualquer exame — o primeiro dano vascular do diabetes é funcional, não anatômico.

#subtopico("2.4 — RAGE e as outras rotas: como o dano passa a se perpetuar")

Tudo o que a seção anterior descreveu é dano químico direto: uma proteína modificada que passa a funcionar mal. Se a história parasse aí, ela seria proporcional à glicemia e cessaria quando ela normalizasse. Não é o que se observa, e a razão é que o AGE não é apenas um produto — ele é um *ligante*.

Existe na superfície de monócitos, macrófagos, células endoteliais e células mesangiais um receptor para produtos de glicação avançada, o #sigla("RAGE", [receptor para produtos finais de glicação avançada — receptor de membrana que converte a presença de AGE em sinal inflamatório intracelular]). Quando o AGE se liga a ele, a célula ativa o fator de transcrição #sigla("NF-κB", [fator nuclear kappa B — fator de transcrição que comanda a expressão de genes pró-inflamatórios]) e transcreve um programa inteiro: citocinas, fatores de crescimento, moléculas de adesão, fator tecidual. As consequências que a aula lista — migração de monócitos, aumento de permeabilidade vascular, atividade pró-coagulante aumentada, proliferação celular e produção de matriz extracelular — são todas saídas desse programa.

O ponto que transforma o quadro é a alça de retroalimentação. A sinalização via RAGE aumenta a expressão do próprio RAGE e eleva o estresse oxidativo local; espécies reativas de oxigênio, por sua vez, aceleram a formação de novos AGEs. *O dano passa a produzir as condições que o produzem* — e é isto que o esquema da aula chama de processo auto-perpetuador, aquele que continua rodando mesmo quando o estímulo inicial diminui.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-30.png",
  largura: 66%,
  legenda: [Leia o esquema como uma linha do tempo com uma bifurcação no fim: a alteração metabólica vem primeiro e é reversível; a alteração funcional ainda o é; a partir das modificações progressivas, um dos ramos passa a se alimentar sozinho. É esse ramo que faz a manifestação clínica surgir anos depois e não regredir com o controle.])

A glicação não é a única rota, e as outras três merecem ser nomeadas porque explicam alvos específicos. A *via dos polióis* converte glicose em sorbitol pela aldose-redutase, consumindo NADPH — e menos NADPH significa menos glutationa reduzida, isto é, menos defesa antioxidante; o sorbitol, que não atravessa membrana, ainda acumula e puxa água por osmose, o que é o mecanismo da catarata e parte do dano ao nervo. A ativação da *proteína quinase C* pelo excesso de diacilglicerol aumenta permeabilidade vascular, expressão de fator de crescimento endotelial e deposição de matriz. A *via da hexosamina* modifica fatores de transcrição por adição de açúcar e altera a expressão de fator de crescimento transformador beta e do inibidor do ativador de plasminogênio — fibrose e trombogenicidade.

As quatro não competem: convergem. Todas aumentam a produção mitocondrial de espécies reativas de oxigênio, e o estresse oxidativo realimenta as quatro. E, porque todas dependem de glicose *intracelular* alta, elas atingem preferencialmente as células que não conseguem fechar a própria porta — endotélio, pericito, célula mesangial, neurônio, cristalino, epitélio tubular. É o detalhe plantado em 1.1 fechando o circuito: os órgãos-alvo do diabetes são exatamente os tecidos que captam glicose sem pedir licença à insulina. A PARTE III vai a cada um deles.

#parte-title("PARTE III — Onde o dano aparece: órgãos-alvo e o que a imagem enxerga")

#subtopico("3.1 — Microangiopatia I: a retina")

A retina é um tecido de consumo altíssimo servido por vasos terminais finos, sem circulação colateral que a socorra. Compare-a com um bairro atendido por uma única linha de água, sem interligação com as vizinhas: qualquer estreitamento em qualquer trecho tira água de uma área inteira, e não há de onde puxar reforço. É essa arquitetura que faz da retina o primeiro lugar onde a microangiopatia se torna visível — e, convenientemente para a medicina, o único leito capilar do corpo que pode ser examinado diretamente, sem cortar nada.

A sequência de eventos tem ordem, e trocá-la é o erro mais comum do tema. O primeiro alvo é o #termo-nota[pericito][célula contrátil que envolve o capilar e regula o seu calibre], e ele capta glicose independentemente de insulina, sofre pelas quatro rotas da PARTE II e morre. O capilar perde o suporte da parede, dilata focalmente e forma #termo-nota[microaneurismas][dilatações focais da parede capilar, formadas onde o suporte do pericito se perdeu; são as primeiras lesões detectáveis ao exame de fundo de olho]. A permeabilidade aumentada deixa escapar plasma e lipoproteína, que se depositam como *exsudatos duros*; a fragilidade da parede permite *hemorragias* puntiformes. Só depois de anos de oclusão capilar progressiva, com áreas de retina isquêmica, é que a fase proliferativa começa.

E a fase proliferativa não é recuperação. A retina isquêmica libera fator de crescimento endotelial, e o organismo responde fabricando vasos novos. Só que esses neovasos são frágeis, permeáveis, e crescem no plano errado — para dentro do vítreo, e não dentro da retina. Eles sangram, produzindo hemorragia vítrea, e o tecido fibroso que os acompanha traciona a retina e a descola. *A angiogênese aqui é a complicação, não a solução.* Quando os neovasos crescem sobre a íris e o ângulo de drenagem da câmara anterior, bloqueiam a saída do humor aquoso e produzem glaucoma neovascular — uma segunda complicação nascida da primeira.

#figura-lateral("/figuras/gr-02-diabetes-mellitus/slide-24.png",
  lado: "right",
  largura-figura: 36%,
  texto: [A catarata do diabético tem mecanismo próprio, e não é apenas a catarata do idoso antecipada. No cristalino, a glicose em excesso é convertida em sorbitol pela aldose-redutase — a via dos polióis da seção 2.4. O sorbitol não atravessa a membrana celular, acumula dentro da fibra do cristalino e puxa água por osmose; a lente incha e perde transparência. Como o mecanismo é osmótico e não estrutural, ele explica também as *oscilações de refração*: variações de glicemia mudam o conteúdo de água da lente e, com ele, o grau do paciente, que volta ao anterior quando a glicemia se estabiliza.],
  legenda: [Preparação de retina digerida: os pontos escuros arredondados sobre o trajeto dos capilares são microaneurismas.])

#subtopico("3.2 — Microangiopatia II: o glomérulo, e o rim que cresce antes de encolher")

O glomérulo é um filtro submetido a pressão, e no diabetes ele é submetido a pressão *maior* logo no começo. A hiperglicemia dilata a arteríola aferente mais do que a eferente; a pressão dentro do capilar glomerular sobe e a taxa de filtração aumenta. Esse aumento é frequentemente lido como sinal de rim saudável, e é o contrário disso: a hiperfiltração é a primeira alteração funcional da doença, e a sobrecarga mecânica que ela impõe ao glomérulo é o que produz a esclerose de anos depois.

O que se deposita nesse glomérulo sob pressão é matriz. A membrana basal espessa e muda de composição, como visto em 2.3, e a matriz mesangial se expande, primeiro difusamente e depois formando os nódulos arredondados que caracterizam a glomeruloesclerose nodular. Importa que *não há infiltrado inflamatório proeminente*: é acúmulo de matriz, não glomerulonefrite — a distinção decide a leitura da biópsia. Em paralelo, as arteríolas aferente e eferente sofrem #termo-nota[hialinização][depósito de material proteico homogêneo e eosinofílico na parede do vaso, que a enrijece e estreita a luz], que enrijece a parede e estreita a luz. Hialinização arteriolar e aterosclerose não são a mesma coisa: uma acontece na arteríola, a outra na artéria de médio e grande calibre, e no diabético as duas convivem em vasos diferentes.

A tradução laboratorial vem em ordem. Primeiro aparece albumina na urina, porque a barreira de carga do glomérulo se perdeu — a albumina passa pelo *glomérulo*, não por falha do túbulo. A creatinina só sobe muito depois, e por um motivo mecanístico: a hiperfiltração dos néfrons remanescentes mascara a perda dos que já esclerosaram. *Creatinina normal não exclui nefropatia; ela apenas informa que a compensação ainda funciona.*

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-33.png",
  largura: 62%,
  legenda: [As duas pontas da história no mesmo exame: rim *aumentado* na hiperfiltração inicial; rim reduzido, com córtex afilado e hiperecogênico no fim — fibrose devolve mais som que parênquima normal.])

#clinica-box("Por que o diabético faz pielonefrite", [
A predisposição à infecção urinária ascendente soma três mecanismos que já apareceram neste resumo. A glicosúria da seção 1.4 oferece substrato no próprio lúmen urinário. A neuropatia autonômica — a mesma família de lesão que a próxima seção descreve no pé — compromete o esvaziamento vesical, e urina residual fica tempo suficiente para ser colonizada. E a hiperglicemia reduz quimiotaxia, adesão e explosão respiratória do neutrófilo, além de os AGEs se ligarem a imunoglobulinas e a componentes do complemento, comprometendo a opsonização.

A infecção sobe mais fácil e é combatida pior. Repare que esclerose glomerular e infecção agem sobre o mesmo órgão por caminhos independentes — e somam perda de função.
])

#subtopico("3.3 — Neuropatia e pé diabético: três falhas somadas num só pé")

A neuropatia diabética nasce das duas rotas da PARTE II agindo juntas sobre o mesmo nervo. Pelo lado vascular, os *vasa nervorum* — os capilares finos que nutrem o tronco nervoso — sofrem a mesma microangiopatia da retina e do glomérulo, e o nervo isquemia. Pelo lado metabólico, o acúmulo de sorbitol e a glicação de proteínas estruturais do axônio e da mielina lesam a fibra diretamente. O achado funcional que resulta é a *queda da velocidade de condução*, e o padrão clínico é o de comprometimento em bota e luva, começando pelas fibras mais longas — os pés antes das mãos.

O pé diabético é o encontro de três falhas independentes no mesmo território, e explicá-lo por uma só delas é o erro que empobrece o raciocínio.

A primeira é a *neuropatia sensitiva*: sem dor protetora, o trauma repetido — um sapato apertado, uma pedra no calçado, um calo que vira ferida — não é percebido e não é interrompido. A segunda é a *neuropatia autonômica*: a perda de inervação simpática das glândulas sudoríparas resseca a pele, que fissura e abre porta de entrada. A terceira é a *doença arterial periférica*, aterosclerose acelerada nos vasos da perna, que reduz o aporte de oxigênio, de nutrientes, de células de defesa e do próprio antibiótico administrado. Somem-se a isso o colágeno reticulado por AGEs, que trava o remodelamento da matriz, e a disfunção do neutrófilo em hiperglicemia: a ferida abre sem aviso, infecta com facilidade e não fecha.

Quando a isquemia é suficiente, o tecido morre. O padrão morfológico é a *gangrena* — necrose, tipicamente isquêmica, comprometendo pele, subcutâneo, músculo e osso ao mesmo tempo. Chama-se seca quando não há infecção superposta e úmida quando há, e vale separar os termos: gangrena descreve a morte tecidual, não a infecção.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-28.png",
  largura: 54%,
  legenda: [A úlcera se instala nos pontos de maior pressão plantar, exatamente onde o trauma se repete sem ser sentido. A borda hiperceratótica ao redor da lesão registra o calo que precedeu a ferida.])

Dois processos ósseos disputam o diagnóstico no mesmo pé, e distingui-los muda a conduta inteira.

#atencao-box("Charcot não é osteomielite", [
A *artropatia de Charcot* é destruição mecânica. A articulação que perdeu propriocepção e dor recebe microtraumas repetidos sem correção postural, e a arquitetura do médio-pé se desmonta progressivamente: erosão das superfícies articulares, fragmentação, subluxação e o colapso do arco plantar. Não há infecção — há trauma acumulado sobre um pé que não avisa.

A *osteomielite* é infecção da medular óssea, em geral por contiguidade a partir de uma úlcera plantar profunda, e exige antibioticoterapia prolongada e frequentemente desbridamento.

As duas coexistem com frequência no mesmo pé, e a confusão custa caro nos dois sentidos: tratar Charcot com antibiótico não imobiliza o pé que continua se destruindo; tratar osteomielite apenas com imobilização deixa a infecção progredir para o osso vizinho e para a corrente sanguínea.
])

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-42.png",
  largura: 68%,
  legenda: [Radiografias do antepé, do médio-pé e do retropé na artropatia de Charcot. As setas marcam erosão das superfícies articulares e desalinhamento — perda da arquitetura, sem reação periosteal de infecção.])

Na imagem, a escolha do método segue o tempo do achado. A *radiografia* só demonstra alteração depois que uma fração significativa da matriz óssea já se perdeu, o que atrasa o diagnóstico de osteomielite em uma a duas semanas. A #sigla("RM", [ressonância magnética — método de imagem baseado no comportamento dos núcleos de hidrogênio em campo magnético, com alta resolução para partes moles e medula óssea]) detecta bem antes, porque enxerga o edema da medular óssea: baixo sinal em T1, alto sinal em T2 com saturação de gordura, e realce após contraste no tecido inflamado e perfundido.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-43.png",
  largura: 68%,
  legenda: [A radiografia à esquerda mostra a lesão óssea já estabelecida. À direita, as três sequências de ressonância do mesmo pé: repare que a mesma região aparece escura em T1, clara em T2 com saturação de gordura e realçada após contraste — a assinatura do edema e da inflamação da medular óssea.])

#subtopico("3.4 — Macroangiopatia: aterosclerose acelerada e como se procura por ela")

Nas complicações anteriores o vaso lesado era microscópico. Aqui ele é grande, e o mecanismo é outro: não é o capilar que se ocluiu, é a artéria que acumulou placa em ritmo acelerado. O diabetes contribui para essa aceleração por quatro caminhos que já foram construídos ao longo do resumo — a LDL glicada captada sem freio pelo macrófago, a inativação do óxido nítrico com disfunção endotelial, o estado pró-inflamatório mantido pelo eixo AGE–RAGE, e um estado pró-coagulante com mais fator tecidual, mais inibidor do ativador de plasminogênio e menos fibrinólise.

O evento agudo, porém, não costuma vir do crescimento lento da placa até fechar o vaso. Vem da *ruptura*: uma placa com núcleo lipídico grande e capa fibrosa fina se fissura, expõe colágeno e fator tecidual ao sangue, e a trombose que se segue oclui a luz em minutos. Uma placa pouco estenosante pode matar; uma placa muito estenosante e estável pode dar apenas angina previsível durante anos. É por isso que a tríade de Virchow aplicada ao diabético destaca *lesão endotelial* e *alteração de fluxo por turbulência sobre a placa*, somadas à hipercoagulabilidade — e não a estase, que é o eixo da trombose venosa por imobilidade.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-34.png",
  largura: 68%,
  legenda: [Siga os dois ramos a partir do mesmo ponto de partida: a placa estável estreita a luz e produz angina previsível; a placa vulnerável se instabiliza e o desfecho passa a depender do trombo — suboclusivo dá síndrome coronariana aguda sem elevação persistente, oclusivo dá infarto ou morte súbita.])

Como a aterosclerose tem um período assintomático longo e o tratamento rende mais quanto mais cedo começa, a imagem é usada para procurá-la antes do evento — e cada método responde a uma pergunta distinta.

#align(center, table(
  columns: (auto, 1fr, auto, 1fr),
  inset: 7pt,
  align: left + horizon,
  stroke: 0.4pt + gray-border,
  fill: (_, y) => if y == 0 { navy } else { white },
  table.header(
    text(fill: white, weight: "bold", size: 8.5pt)[Método],
    text(fill: white, weight: "bold", size: 8.5pt)[O que mede],
    text(fill: white, weight: "bold", size: 8.5pt)[Custo],
    text(fill: white, weight: "bold", size: 8.5pt)[Quando escolher],
  ),
  text(size: 8.5pt)[Escore de cálcio],
  text(size: 8.5pt)[Carga de placa calcificada, quantificada acima de 130 unidades Hounsfield em área mínima de 1 mm²],
  text(size: 8.5pt)[Radiação baixa, sem contraste],
  text(size: 8.5pt)[Estratificar risco em assintomático; não mostra a luz do vaso],
  text(size: 8.5pt)[Angiotomografia de coronárias],
  text(size: 8.5pt)[A luz do vaso, com especificidade alta e valor preditivo negativo próximo de 100%],
  text(size: 8.5pt)[Radiação e contraste iodado],
  text(size: 8.5pt)[Excluir doença em probabilidade pré-teste baixa a intermediária],
  text(size: 8.5pt)[Cateterismo],
  text(size: 8.5pt)[Grau de estenose com precisão, e permite tratar no mesmo tempo],
  text(size: 8.5pt)[Invasivo, risco baixo mas real],
  text(size: 8.5pt)[Alta probabilidade pré-teste, ou lesão grave detectada antes],
))

A lógica da tabela é uma só e vale mais que a memorização das linhas: *um exame só é útil quando o resultado dele pode mudar a conduta*. Com probabilidade pré-teste alta, uma angiotomografia negativa não convenceria ninguém e uma positiva levaria ao cateterismo de qualquer forma — o exame não muda nada e apenas adiciona radiação e contraste. Com probabilidade baixa a intermediária, um resultado negativo encerra a investigação, e é aí que o valor preditivo negativo alto vale ouro.

O mesmo raciocínio de leitura por densidade vale nos outros territórios que a aterosclerose atinge. Na tomografia de crânio sem contraste, a área isquêmica aparece *hipoatenuante* — mais escura — porque o edema citotóxico aumenta o conteúdo de água do tecido; sangue agudo faz o oposto, é hiperatenuante. Na aorta, a calcificação parietal extensa e o alargamento do vaso registram a mesma doença num calibre maior.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-40.png",
  largura: 46%,
  legenda: [Comparação direta: à direita, o parênquima normal com diferenciação entre substância cinzenta e branca; à esquerda, a área hipoatenuante que perdeu essa diferenciação — mais água no tecido, menos atenuação do feixe.])

#clinica-box("Do mecanismo à estratégia terapêutica", [
Quando um paciente infarta por trombose sobre placa rota, cada estratégia disponível ataca um elo diferente da cadeia que este resumo montou.

O *antiagregante plaquetário* age na hemostasia primária: reduz a adesão e a agregação sobre o colágeno exposto, dificultando que o trombo se forme ou cresça. O *trombolítico* age depois que ele já se formou, ativando o plasminogênio em plasmina, que degrada a rede de fibrina. A *desobstrução mecânica com implante de stent* resolve o problema geométrico — restabelece a luz e reduz a turbulência que realimenta a ativação endotelial.

O que unifica as três é o alvo comum: o endotélio ativado, que perdeu o perfil antitrombótico e passou a expressar fator tecidual e fator de von Willebrand e a reduzir a produção de óxido nítrico e de ativador de plasminogênio. Controlar a glicemia atua *antes* disso — sobre a glicação que produziu a disfunção endotelial em primeiro lugar.
])

#conclusao-box[
O princípio que atravessa este resumo inteiro cabe numa frase: *diabetes é um defeito de sinal cujo produto — glicose intracelular alta e prolongada — é quimicamente reativo*. Todo o resto é consequência dessa reatividade encontrando tecidos que não conseguem se proteger dela.

O mecanismo nuclear é a glicação não-enzimática avançando por etapas com reversibilidade decrescente, e o eixo AGE–RAGE convertendo dano químico em programa inflamatório com retroalimentação positiva. Foi essa distinção entre etapas reversíveis e irreversíveis que explicou, de uma só vez, por que a hemoglobina glicada mede controle e por que a lesão do diabetes tem memória.

A clínica se organiza em torno da mesma ideia. Adoecem os tecidos que captam glicose sem depender de insulina e não conseguem fechar a porta quando a glicemia sobe — e cada um deles tem uma assinatura de imagem que corresponde ao substrato que o patologista descreve, do rim que aumenta antes de encolher ao parênquima hipoatenuante do infarto cerebral.

Duas portas ficam abertas. A primeira é a inflamação crônica e o reparo: quase tudo o que a PARTE III chamou de auto-perpetuador é, no vocabulário da patologia, inflamação crônica com fibrose — e o pé que não cicatriza é um estudo de caso de reparo travado. A segunda é a trombose: a placa que rompe e o trombo que se forma sobre ela são hemostasia funcionando como deveria, no lugar errado.
]
