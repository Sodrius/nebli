#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Diabetes mellitus é um defeito de sinal. A insulina, que informa aos tecidos que há substrato chegando, deixa de ser produzida ou deixa de ser obedecida — e a glicose que se acumula no plasma passa a reagir quimicamente com as proteínas do organismo.

A *PARTE I* percorre por que a glicemia sobe: o que a insulina comanda, os dois defeitos opostos que interrompem esse comando, e como a hiperglicemia vira sintoma. A *PARTE II* trata a glicose alta como reagente e acompanha a glicação não-enzimática até a lesão estrutural que se auto-alimenta. A *PARTE III* localiza essa lesão nos órgãos-alvo e mostra a correspondência entre o substrato que o patologista descreve e o achado que o radiologista enxerga.
]

#parte-title("PARTE I — O sinal que falta: por que a glicose sobe", primeira: true)

#subtopico("1.1 — A insulina e os freios que ela mantém")

A célula beta da ilhota pancreática secreta insulina quando a glicose plasmática sobe. O receptor de insulina é uma *tirosina-quinase*, enzima que fosforila resíduos de tirosina de proteínas-alvo: as duas subunidades α ligam o hormônio, as duas subunidades β se autofosforilam e passam a fosforilar o #sigla("IRS-1", [substrato 1 do receptor de insulina — a primeira proteína fosforilada pelo receptor, e o ponto em que a via se ramifica]), que recruta a #sigla("PI3K", [fosfatidilinositol-3-quinase — converte o sinal do receptor em um lipídeo de membrana capaz de ancorar a Akt]) e ativa a Akt. Não há proteína G nem segundo mensageiro nesse caminho.

O #sigla("GLUT-4", [transportador de glicose tipo 4 — isoforma insulino-dependente do músculo esquelético e do tecido adiposo]) já existe pronto, estocado em vesículas intracelulares, e a Akt comanda a fusão dessas vesículas com a membrana plasmática. *A insulina não sintetiza o transportador, ela o transloca* — daí o efeito surgir em minutos e desaparecer em minutos quando o sinal cessa.

O restante do programa é composto de freios. A insulina ativa a glicogênio-sintase, liga a lipogênese no adipócito e inibe a *lipase hormônio-sensível*, enzima que hidrolisa triacilglicerol em ácido graxo livre; em paralelo, suprime a gliconeogênese hepática e a proteólise muscular. Perder o hormônio é liberar todos esses freios simultaneamente, e é por isso que o quadro clínico do tipo 1 não se resume à glicemia.

Um dado de distribuição sustenta as PARTES II e III: *apenas músculo esquelético e tecido adiposo dependem do GLUT-4*. Neurônio, hemácia, endotélio, célula mesangial do glomérulo, pericito da retina, cristalino e epitélio tubular renal captam glicose por transportadores que não respondem à insulina, e por isso não conseguem reduzir a entrada quando a glicemia sobe.

#figura-lateral("/figuras/gr-02-diabetes-mellitus/slide-14.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O intestino sinaliza ao pâncreas antes de a glicose ser absorvida. O #sigla("GLP-1", [peptídeo semelhante ao glucagon 1 — incretina intestinal que amplifica a secreção de insulina dependente de glicose]), liberado pela chegada do alimento ao lúmen, amplifica a secreção de insulina pela célula beta, retarda o esvaziamento gástrico e aumenta a saciedade por ação hipotalâmica. É o *efeito incretínico*, e ele explica por que uma carga oral de glicose eleva mais a insulina do que a mesma carga por via intravenosa.],
  legenda: [Eixo intestino–pâncreas–encéfalo.])

#subtopico("1.2 — Tipo 1: a ilhota destruída e o corpo em jejum permanente")

O que desencadeia o quadro clínico do tipo 1 não é o valor absoluto da insulina, e sim a queda da *razão insulina/glucagon*. A insulina freia a célula alfa dentro da própria ilhota; sem ela, o glucagon é secretado sem contraposição e o fígado mantém glicogenólise e gliconeogênese enquanto o músculo já não capta glicose. A hiperglicemia é gerada nas duas pontas.

A destruição da célula beta é autoimune, mediada sobretudo por linfócitos T citotóxicos, em indivíduos com alelos predisponentes de #sigla("HLA", [antígeno leucocitário humano — o complexo principal de histocompatibilidade humano, cujos alelos de classe II definem boa parte do risco genético do tipo 1]) de classe II. Os autoanticorpos dosados no laboratório — anti-#termo-nota[descarboxilase do ácido glutâmico][enzima citoplasmática da célula beta; o anticorpo anti-GAD65 contra ela é o marcador sorológico mais usado de autoimunidade contra a ilhota], anti-insulina, anti-tirosina-fosfatase da ilhota — são marcadores dessa agressão, não os seus executores principais.

A massa funcionante remanescente é estimada pelo #termo-nota[peptídeo C][fragmento liberado em quantidade equimolar à insulina na clivagem da pró-insulina; ausente na insulina exógena e pouco extraído pelo fígado, mede a secreção endógena]: ele sai da pró-insulina junto com a insulina, mas não acompanha a insulina exógena aplicada e escapa da extração hepática de primeira passagem, que retira boa parte da insulina antes da circulação sistêmica.

O metabolismo assume então o padrão do jejum com o plasma cheio de glicose. Sem o freio da insulina, a lipase hormônio-sensível libera ácidos graxos em quantidade que excede a capacidade oxidativa hepática: a acetil-CoA gerada ultrapassa a capacidade de consumo do ciclo de Krebs e o excedente é desviado para acetoacetato e β-hidroxibutirato, ácidos fortes cujo acúmulo derruba o pH. A proteólise muscular fornece aminoácidos à gliconeogênese e o balanço nitrogenado fica negativo. A perda ponderal ocorre com ingesta aumentada, porque se perde caloria na urina, triacilglicerol no adipócito e proteína no músculo.

#mini-resumo[Falta de insulina → glucagon sem freio e lipólise sem freio → glicose hepática alta e ácido graxo em excesso → cetoácidos. Hiperglicemia e cetose são efeitos paralelos do mesmo defeito.]

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-12.png",
  largura: 60%,
  legenda: [O defeito está em andares diferentes: no tipo 1 o pâncreas não entrega o sinal; no tipo 2 o sinal chega em quantidade e a célula-alvo não responde.])

#clinica-box("O caso que abre a aula", [
Homem de 26 anos, magro, com dez dias de poliúria, polidipsia e perda de 3 kg; glicemia de 397 mg/dL, hemoglobina glicada de 8,8%, peptídeo C de 1,32 ng/mL e anti-descarboxilase do ácido glutâmico de 1082 UI/mL para valor de referência abaixo de 10.

Os três exames respondem perguntas distintas. O autoanticorpo em título cem vezes acima do limite identifica a natureza autoimune da destruição. O peptídeo C mensurável, no limite inferior da normalidade, indica secreção residual preservada em parte — o paciente está no início da história natural, o que explica a ausência de acidose franca à apresentação. A hemoglobina glicada de 8,8% data o início da hiperglicemia semanas antes dos dez dias de sintomas: o sintoma marca a queda da reserva de célula beta, não o início da doença.
])

#subtopico("1.3 — Tipo 2: o sinal que chega e não é escutado")

No tipo 2 o receptor está íntegro e a falha é pós-receptor. Com oferta calórica alta e sedentarismo, o músculo recebe mais acil-CoA graxo do que oxida, e o excedente acumula dois intermediários lipídicos com atividade de sinalização: *diacilglicerol* e *ceramida*. Ambos ativam *serina-quinases de estresse*, que fosforilam o IRS-1 em resíduos de serina em vez de tirosina. O IRS-1 fosforilado no resíduo errado não recruta a PI3K, a Akt não é ativada, e menos vesículas de GLUT-4 alcançam a membrana.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-09.png",
  largura: 55%,
  legenda: [O ácido graxo não apenas compete com a glicose como combustível: ele interrompe a sinalização que traria o GLUT-4 à superfície. A mitocôndria sobrecarregada devolve espécies reativas de oxigênio, que realimentam as serina-quinases.])

O tecido adiposo contribui por uma segunda via. O adipócito hipertrofiado recruta macrófagos e secreta fator de necrose tumoral alfa e interleucina-6, citocinas que ativam as mesmas serina-quinases e reduzem o GLUT-4 de superfície. A obesidade opera como inflamação crônica de baixo grau, e é por essa ponte que produz resistência à insulina.

A resistência isolada não configura diabetes. A célula beta responde à glicemia crescente aumentando a secreção, e a *hiperinsulinemia compensatória* mantém a glicose em faixa quase normal por anos.

#atencao-box("No tipo 2, a insulina pode estar alta", [
Durante a maior parte da história natural do tipo 2 a insulina está *normal ou elevada*, e a glicemia sobe apesar disso porque o tecido não responde. Insulina alta com glicemia alta não é contradição laboratorial: é o retrato da resistência. A insulina só cai quando, após anos de sobrecarga secretora e de exposição a glicose e ácido graxo em excesso, a célula beta entra em apoptose e a massa de ilhota diminui — e é nessa fase que o tipo 2 passa a exigir insulina exógena.
])

O defeito é distribuído por vários órgãos. O fígado resiste ao freio da gliconeogênese e mantém produção hepática de glicose mesmo sob insulina alta, o que explica a hiperglicemia de jejum. O adipócito resiste ao freio da lipólise e continua exportando ácido graxo. O intestino perde parte do efeito incretínico. A ilhota acrescenta hiperglucagonemia à queda de secreção.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-11.png",
  largura: 56%,
  legenda: [Cinco endereços do mesmo defeito. A produção hepática de glicose que não desliga é a que sustenta a glicemia de jejum, quando nenhuma refeição a justifica.])

#subtopico("1.4 — Diurese osmótica e as duas descompensações")

A glicose é filtrada livremente no glomérulo e reabsorvida no túbulo proximal por transportadores de capacidade máxima finita, saturados em torno de 180 mg/dL de glicemia. Acima desse limiar a glicose excedente permanece no lúmen tubular.

Soluto não reabsorvido retém água por osmose e impede que ela acompanhe o sódio de volta ao interstício: instala-se a #termo-nota[diurese osmótica][perda aumentada de água na urina causada por um soluto não reabsorvido que a retém no lúmen tubular], e o volume urinário sobe. A poliúria precede a sede — a perda de água eleva a osmolaridade plasmática e só então os osmorreceptores hipotalâmicos disparam a polidipsia. Sódio e potássio são arrastados junto.

A perda ponderal soma três parcelas: caloria eliminada como glicose urinária, triacilglicerol mobilizado pela lipólise e proteína muscular consumida pela gliconeogênese. A polifagia coexiste porque a glicose não entrou na célula.

A forma da descompensação depende da insulina residual. No tipo 1, com secreção praticamente ausente, a lipólise segue livre até os cetoácidos e instala-se a *cetoacidose diabética*, com pH baixo, #termo-nota[hiato aniônico][diferença entre os cátions e os ânions medidos no plasma; aumenta quando um ácido não medido, como o cetoácido, se acumula] aumentado e respiração ampla e profunda — compensação respiratória que elimina gás carbônico para tamponar a acidez, não doença pulmonar. No tipo 2, a insulina residual é insuficiente para normalizar a glicemia mas basta para conter a lipase hormônio-sensível; sem lipólise maciça não há cetose, e a descompensação assume a forma de *estado hiperosmolar*, com glicemias mais altas, diurese osmótica prolongada e rebaixamento de consciência.

#confusao-prevista(
  titulo: "Hiperosmolaridade e acidose não são o mesmo distúrbio",
  aluno_acha: [as duas descompensações são lidas como graus de gravidade de um mesmo processo],
  mecanismo: [são distúrbios de naturezas distintas que apenas coexistem na cetoacidose. A hiperosmolaridade é distúrbio de *água*, produzido pela diurese osmótica; a acidose é distúrbio de *ácido*, produzido pelos cetoácidos da lipólise. No estado hiperosmolar do tipo 2 a primeira ocorre isolada, e é ela que ameaça a vida.],
)

O potássio inverte a leitura esperada do exame. A diurese osmótica esvazia o estoque corporal total, enquanto a acidose e a ausência de insulina deslocam potássio do intracelular para o plasma. O resultado é potássio sérico normal ou elevado em paciente profundamente depletado — valor que despenca assim que a insulina reconduz o íon para dentro da célula.

#parte-title("PARTE II — Do açúcar ao dano: glicação e as rotas que se perpetuam")

#subtopico("2.1 — Glicação não-enzimática e os dois relógios do controle")

A glicose é um açúcar redutor: possui grupo carbonil livre, que reage espontaneamente com grupos amino de proteínas. A reação é *glicação* — não-enzimática, sem sítio preferencial, governada apenas pelo produto entre concentração de glicose e tempo de exposição. Distingue-se da *glicosilação*, que é enzimática, dirigida a sítios específicos e parte da maturação normal de glicoproteínas. É essa dependência de concentração e tempo que faz da glicação, ao mesmo tempo, o mecanismo da lesão e a base dos exames que medem controle.

A reação avança em três estágios de reversibilidade decrescente. A *base de Schiff* é a condensação inicial entre o carbonil da glicose e um grupo amino da proteína, tipicamente da lisina ou da valina N-terminal; forma-se em horas e desfaz-se se a glicemia cai. O *produto de Amadori* é o rearranjo da base de Schiff numa cetoamina estável, formado em dias e apenas lentamente reversível. O #sigla("AGE", [produto final de glicação avançada — do inglês *advanced glycation end product*, a forma irreversível da glicação]) resulta de desidratações e oxidações sucessivas ao longo de semanas a meses e estabelece *ligações cruzadas* entre dois radicais protéicos: aqui a reação deixa de reverter.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-15.png",
  largura: 70%,
  legenda: [A régua de tempo no alto — horas, dias, semanas a meses — carrega o mecanismo. A barra "reversível" termina antes da ligação cruzada entre duas cadeias protéicas, e é essa etapa final que a normalização da glicemia já não desfaz.])

Da escala de tempo decorre a seleção do alvo: acumula AGE a proteína de meia-vida longa — colágeno, elastina, cristalino, membrana basal —, renovada mais devagar do que a reação avança. Proteína de turnover rápido é degradada antes de reticular.

Os dois exames de controle são produtos de Amadori em proteínas diferentes, e a diferença entre eles é a janela de tempo que cada proteína guarda. A #sigla("HbA1c", [hemoglobina glicada — fração da hemoglobina A que sofreu glicação, expressa em porcentagem da hemoglobina total]) mede a fração glicada da hemoglobina; como a hemácia circula de 90 a 120 dias sem reverter a modificação, o exame integra a exposição à glicose ao longo de 8 a 12 semanas, com peso maior nas últimas quatro. Uma HbA1c de 8,8% corresponde a glicemia média em torno de 205 mg/dL nesse período — no caso da PARTE I, hiperglicemia sustentada muito antes dos dez dias de sintomas. A limitação do exame é a mesma variável que o define: hemólise, sangramento recente ou transfusão encurtam a sobrevida eritrocitária e reduzem a HbA1c para a mesma glicemia média.

A #termo-nota[frutosamina][conjunto das proteínas plasmáticas glicadas, sobretudo a albumina; como a albumina vive de 14 a 20 dias, o exame reflete as últimas 2 a 3 semanas] resolve exatamente esses casos. A albumina circula de 14 a 20 dias e o exame lê 2 a 3 semanas, o que o torna útil em hemoglobinopatia, anemia hemolítica, gestação e mudança recente de tratamento. No caso da aula os dois caminharam juntos em escalas distintas: HbA1c de 8,8% e frutosamina de 575 μmol/L em abril; 5,2% e 289 μmol/L em agosto, quatro meses após a insulinização.

#subtopico("2.2 — O que o AGE faz nas proteínas de vida longa")

A reticulação do colágeno não produz apenas rigidez: a proteína reticulada *resiste à digestão proteolítica e deixa de ser substituída*. O remodelamento da matriz extracelular depende de degradar colágeno velho para depositar colágeno novo, e as proteases não cortam o substrato reticulado. Esta é a razão bioquímica de a ferida do diabético cicatrizar mal mesmo com perfusão preservada.

A glicação da #sigla("LDL", [lipoproteína de baixa densidade — partícula que transporta colesterol do fígado para os tecidos]) prejudica o reconhecimento da partícula pelo receptor hepático, prolonga o tempo de circulação e favorece a oxidação. A partícula modificada passa a ser captada por *receptores scavenger* do macrófago, que — ao contrário do receptor de LDL — não são inibidos pelo colesterol já acumulado na célula. O macrófago capta sem regulação e se converte em #termo-nota[célula espumosa][macrófago repleto de gotículas lipídicas, elemento fundador da estria gordurosa e da placa de ateroma]. É o elo direto entre hiperglicemia e placa de ateroma, retomado na PARTE III.

#confusao-prevista(
  titulo: "Membrana basal mais espessa não filtra melhor",
  aluno_acha: [engrossar a barreira deveria retê-la mais e reduzir a passagem de proteína],
  mecanismo: [o que muda não é só a espessura, é a *composição*. A membrana basal glomerular do diabético ganha matriz desorganizada e perde proteoglicanos aniônicos, que constituem a barreira de carga que repelia a albumina — também aniônica. O resultado é uma membrana mais espessa e simultaneamente mais permeável a proteína.],
)

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-17.png",
  largura: 50%,
  legenda: [À esquerda, membrana basal normal: fina e homogênea, com pedicelos regularmente espaçados. À direita, a mesma barreira espessada e desorganizada no diabético.])

Há ainda um efeito independente de estrutura: os AGEs *inativam o óxido nítrico*. A menor disponibilidade de óxido nítrico reduz a vasodilatação dependente do endotélio, aumenta a adesão de leucócitos e plaquetas e favorece a proliferação de músculo liso na parede vascular. O primeiro dano vascular do diabetes é funcional e antecede qualquer placa detectável por imagem.

#subtopico("2.3 — RAGE e as outras rotas: como o dano passa a se perpetuar")

O AGE não é apenas produto: é ligante. Monócitos, macrófagos, células endoteliais e células mesangiais expressam o #sigla("RAGE", [receptor para produtos finais de glicação avançada — receptor de membrana que converte a presença de AGE em sinal inflamatório intracelular]); a ligação ativa o #sigla("NF-κB", [fator nuclear kappa B — fator de transcrição que comanda a expressão de genes pró-inflamatórios]) e transcreve um programa que inclui citocinas, fatores de crescimento, moléculas de adesão e fator tecidual. Migração de monócitos, aumento de permeabilidade vascular, atividade pró-coagulante e deposição de matriz extracelular são saídas desse programa.

A alça é positiva: a sinalização por RAGE aumenta a expressão do próprio receptor e o estresse oxidativo local, e as espécies reativas de oxigênio aceleram a formação de novos AGEs. *O dano passa a produzir as condições que o produzem* — o processo auto-perpetuador do esquema da aula, que continua operando quando o estímulo inicial já diminuiu.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-30.png",
  largura: 55%,
  legenda: [Alteração metabólica e alteração funcional ainda revertem; a partir das modificações progressivas um dos ramos passa a se alimentar sozinho. É esse ramo que faz a manifestação clínica surgir anos depois e não regredir com o controle.])

Três rotas adicionais explicam alvos específicos. A *via dos polióis* converte glicose em sorbitol pela aldose-redutase consumindo NADPH; menos NADPH significa menos glutationa reduzida e menor defesa antioxidante, e o sorbitol acumulado — incapaz de atravessar a membrana — puxa água por osmose no cristalino e no nervo. A ativação da *proteína quinase C* pelo excesso de diacilglicerol aumenta permeabilidade vascular, expressão de fator de crescimento endotelial e deposição de matriz. A *via da hexosamina* modifica fatores de transcrição por adição de N-acetilglicosamina e altera a expressão de fator de crescimento transformador beta e do inibidor do ativador de plasminogênio, com fibrose e trombogenicidade como saída.

As quatro rotas convergem: todas aumentam a produção mitocondrial de espécies reativas de oxigênio, e o estresse oxidativo as realimenta. Como todas dependem de glicose *intracelular* alta, atingem preferencialmente as células que captam glicose sem depender de insulina — endotélio, pericito, célula mesangial, neurônio, cristalino, epitélio tubular. Os órgãos-alvo do diabetes são exatamente esses tecidos.

#parte-title("PARTE III — Onde o dano aparece: órgãos-alvo e o que a imagem enxerga")

#subtopico("3.1 — Microangiopatia: retina e glomérulo")

A retina é servida por vasos terminais sem circulação colateral, e é o único leito capilar do corpo examinável diretamente. O primeiro alvo é o #termo-nota[pericito][célula contrátil que envolve o capilar e regula o seu calibre], que capta glicose independentemente de insulina, sofre pelas quatro rotas da PARTE II e morre. O capilar perde suporte de parede e dilata focalmente em #termo-nota[microaneurismas][dilatações focais da parede capilar, formadas onde o suporte do pericito se perdeu; são as primeiras lesões detectáveis ao exame de fundo de olho]; a permeabilidade aumentada deposita *exsudatos duros* — plasma e lipoproteína extravasados — e a fragilidade da parede produz hemorragias puntiformes.

A fase proliferativa não é recuperação. A retina isquêmica libera fator de crescimento endotelial e o organismo fabrica neovasos frágeis que crescem para dentro do vítreo: eles sangram, produzindo hemorragia vítrea, e o tecido fibroso que os acompanha traciona e descola a retina. Quando crescem sobre a íris e o ângulo camerular, bloqueiam a drenagem do humor aquoso e produzem glaucoma neovascular. A catarata tem mecanismo próprio e osmótico: a aldose-redutase converte glicose em sorbitol, que não atravessa a membrana da fibra do cristalino, acumula, puxa água e opacifica a lente — o mesmo mecanismo explica as oscilações de refração do paciente descompensado.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-31.png",
  largura: 58%,
  legenda: [Os órgãos marcados no esquema são os que captam glicose sem depender de insulina, mais os leitos arteriais atingidos pela aterosclerose acelerada.])

No glomérulo, a hiperglicemia dilata a arteríola aferente mais do que a eferente: a pressão no capilar glomerular sobe e a filtração aumenta. Essa *hiperfiltração* é a primeira alteração funcional da doença, e a sobrecarga mecânica que ela impõe produz a esclerose de anos depois — o aumento da filtração inicial não é sinal de rim preservado.

O que se deposita é matriz. A membrana basal espessa e muda de composição, como em 2.2, e a matriz mesangial se expande, primeiro difusamente e depois em nódulos arredondados — a glomeruloesclerose nodular de Kimmelstiel-Wilson. *Não há infiltrado inflamatório proeminente*: é acúmulo de matriz, não glomerulonefrite. As arteríolas aferente e eferente sofrem #termo-nota[hialinização][depósito de material proteico homogêneo e eosinofílico na parede do vaso, que a enrijece e estreita a luz], que é lesão de arteríola e não se confunde com a aterosclerose das artérias de médio e grande calibre.

A tradução laboratorial tem ordem. A albuminúria aparece primeiro, porque a barreira de carga glomerular se perdeu — a albumina passa pelo glomérulo, não por falha tubular. A creatinina sobe muito depois, porque a hiperfiltração dos néfrons remanescentes mascara a perda dos já esclerosados: creatinina normal não exclui nefropatia. A glicosúria, a retenção urinária por neuropatia autonômica e a redução da quimiotaxia e da explosão respiratória do neutrófilo em hiperglicemia somam-se para explicar a predisposição à pielonefrite.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-33.png",
  largura: 58%,
  legenda: [As duas pontas da história no mesmo exame: rim *aumentado* na hiperfiltração inicial; rim reduzido, com córtex afilado e ecogenicidade aumentada no estágio final — fibrose devolve mais som que parênquima funcionante.])

#subtopico("3.2 — Neuropatia e pé diabético")

A neuropatia diabética resulta de dois mecanismos somados. Os *vasa nervorum*, capilares que nutrem o tronco nervoso, sofrem a mesma microangiopatia da retina e do glomérulo e isquemiam o nervo; em paralelo, o sorbitol acumulado e a glicação de proteínas do axônio e da mielina lesam a fibra diretamente. O achado funcional é a queda da velocidade de condução, e o padrão clínico é o comprometimento em bota e luva, que começa pelas fibras mais longas.

O pé diabético soma três falhas independentes no mesmo território. A *neuropatia sensitiva* remove a dor protetora, e o trauma repetido — calçado apertado, corpo estranho, calo que ulcera — não é percebido nem interrompido. A *neuropatia autonômica* reduz a sudorese, resseca a pele e abre fissuras que servem de porta de entrada. A *doença arterial periférica* limita o aporte de oxigênio, de células de defesa e do antibiótico administrado. Somam-se a reticulação do colágeno por AGEs, que trava o remodelamento da matriz, e a disfunção do neutrófilo em hiperglicemia.

Quando a isquemia é suficiente, o tecido morre com padrão de *gangrena*: necrose, tipicamente isquêmica, comprometendo pele, subcutâneo, músculo e osso simultaneamente. Diz-se seca sem infecção superposta e úmida com ela — o termo descreve a morte tecidual, não a infecção.

#atencao-box("Charcot não é osteomielite", [
A *artropatia de Charcot* é destruição mecânica: a articulação sem propriocepção nem dor recebe microtraumas repetidos sem correção postural, e a arquitetura do médio-pé se desmonta com erosão das superfícies articulares, fragmentação, subluxação e colapso do arco plantar. Não há infecção — há trauma acumulado sobre um pé que não avisa.

A *osteomielite* é infecção da medular óssea, em geral por contiguidade a partir de úlcera plantar profunda, e exige antibioticoterapia prolongada e com frequência desbridamento.

As duas coexistem no mesmo pé, e a confusão custa nos dois sentidos: antibiótico não imobiliza a articulação que continua se destruindo, e imobilização não contém a infecção que progride para o osso vizinho e para a corrente sanguínea.
])

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-42.png",
  largura: 58%,
  legenda: [Antepé, médio-pé e retropé na artropatia de Charcot: erosão das superfícies articulares e desalinhamento, sem reação periosteal de infecção.])

A escolha do método de imagem segue o tempo do achado. A radiografia só demonstra alteração após perda óssea significativa, com atraso de uma a duas semanas — insuficiente para excluir osteomielite aguda. A #sigla("RM", [ressonância magnética — método baseado no comportamento dos núcleos de hidrogênio em campo magnético, com alta resolução para partes moles e medula óssea]) detecta o edema da medular óssea muito antes: baixo sinal em T1, alto sinal em T2 com saturação de gordura, e realce após contraste no tecido inflamado e perfundido.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-43.png",
  largura: 58%,
  legenda: [A mesma região aparece escura em T1, clara em T2 com saturação de gordura e realçada após contraste — a assinatura do edema e da inflamação da medular óssea.])

#subtopico("3.3 — Macroangiopatia: aterosclerose acelerada e como se procura por ela")

O diabetes acelera a aterosclerose por quatro caminhos já construídos: a LDL glicada captada sem regulação pelo macrófago, a inativação do óxido nítrico com disfunção endotelial, o estado pró-inflamatório do eixo AGE–RAGE, e um estado pró-coagulante com mais fator tecidual, mais inibidor do ativador de plasminogênio e menos fibrinólise.

O evento agudo vem da *ruptura* da placa, não do seu crescimento até ocluir. Uma placa com núcleo lipídico grande e capa fibrosa fina se fissura, expõe colágeno e fator tecidual ao sangue, e a trombose resultante oclui a luz em minutos — placa pouco estenosante pode matar, enquanto placa muito estenosante e estável dá angina previsível por anos. Aplicada ao diabético, a tríade de Virchow destaca *lesão endotelial* e *alteração de fluxo por turbulência* sobre a placa, somadas à hipercoagulabilidade; a estase é o eixo da trombose venosa por imobilidade, cenário distinto.

#figura-nebli("/figuras/gr-02-diabetes-mellitus/slide-34.png",
  largura: 58%,
  legenda: [Dois ramos a partir do mesmo ponto: a placa estável estreita a luz e dá angina previsível; a placa vulnerável se instabiliza e o desfecho passa a depender do trombo — suboclusivo dá síndrome coronariana aguda, oclusivo dá infarto ou morte súbita.])

Como a aterosclerose tem período assintomático longo, a imagem é usada para procurá-la antes do evento, e cada método responde a uma pergunta distinta.

#align(center, table(
  columns: (auto, 1fr, auto, 1fr),
  inset: 6pt,
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
  text(size: 8.5pt)[Carga de placa calcificada, acima de 130 unidades Hounsfield em área mínima de 1 mm²],
  text(size: 8.5pt)[Radiação baixa, sem contraste],
  text(size: 8.5pt)[Estratificar risco em assintomático; não mostra a luz],
  text(size: 8.5pt)[Angiotomografia de coronárias],
  text(size: 8.5pt)[A luz do vaso, com especificidade alta e valor preditivo negativo próximo de 100%],
  text(size: 8.5pt)[Radiação e contraste iodado],
  text(size: 8.5pt)[Excluir doença em probabilidade pré-teste baixa a intermediária],
  text(size: 8.5pt)[Cateterismo],
  text(size: 8.5pt)[Grau de estenose com precisão, e permite tratar no mesmo tempo],
  text(size: 8.5pt)[Invasivo, risco baixo mas real],
  text(size: 8.5pt)[Alta probabilidade pré-teste, ou lesão grave já detectada],
))

A regra que organiza a tabela: *um exame só é útil quando o resultado pode mudar a conduta*. Com probabilidade pré-teste alta, uma angiotomografia negativa não seria aceita e uma positiva levaria ao cateterismo de qualquer modo — o exame acrescenta radiação e contraste sem alterar a decisão. Com probabilidade baixa a intermediária, o resultado negativo encerra a investigação, e é aí que o valor preditivo negativo alto tem valor.

A mesma leitura por densidade vale nos outros territórios. Na tomografia de crânio sem contraste, a área isquêmica é *hipoatenuante* porque o edema citotóxico aumenta o conteúdo de água do tecido; sangue agudo é hiperatenuante. Na aorta, a calcificação parietal extensa e o alargamento do vaso registram a mesma doença em calibre maior.

#clinica-box("Do mecanismo à estratégia terapêutica", [
No infarto por trombose sobre placa rota, cada estratégia ataca um elo da cadeia deste resumo. O *antiagregante plaquetário* age na hemostasia primária, reduzindo adesão e agregação sobre o colágeno exposto. O *trombolítico* age depois do trombo formado, ativando o plasminogênio em plasmina, que degrada a rede de fibrina. A *desobstrução mecânica com implante de stent* restabelece a luz e reduz a turbulência que realimenta a ativação endotelial.

As três convergem no mesmo alvo: o endotélio ativado, que perdeu o perfil antitrombótico e passou a expressar fator tecidual e fator de von Willebrand enquanto reduz óxido nítrico e ativador de plasminogênio. Controlar a glicemia atua antes disso, sobre a glicação que produziu a disfunção endotelial.
])

#conclusao-box[
O princípio que atravessa o resumo: *diabetes é um defeito de sinal cujo produto — glicose intracelular alta e prolongada — é quimicamente reativo*. O restante é consequência dessa reatividade encontrando tecidos incapazes de se proteger dela.

O mecanismo nuclear é a glicação não-enzimática avançando em etapas de reversibilidade decrescente — base de Schiff em horas, produto de Amadori em dias, ligação cruzada irreversível em meses — e o eixo AGE–RAGE convertendo dano químico em programa inflamatório com retroalimentação positiva. A mesma distinção entre etapas reversíveis e irreversíveis explica por que a hemoglobina glicada mede controle e por que a lesão do diabetes tem memória.

Adoecem os tecidos que captam glicose sem depender de insulina e não conseguem fechar a porta quando a glicemia sobe — pericito, célula mesangial, endotélio, neurônio periférico, cristalino. Cada um tem uma assinatura de imagem que corresponde ao substrato descrito pelo patologista: o rim que aumenta antes de encolher, a erosão articular sem reação periosteal do Charcot, o edema de medular óssea da osteomielite, a calcificação coronariana medida em unidades Hounsfield, o parênquima hipoatenuante do infarto cerebral.

Duas portas ficam abertas. A inflamação crônica e o reparo tecidual: o que a PARTE III chamou de auto-perpetuador é, no vocabulário da patologia, inflamação crônica com fibrose, e o pé que não cicatriza é reparo travado. E a trombose: a placa que rompe e o trombo que se forma sobre ela são hemostasia funcionando como deveria, no lugar errado.
]
