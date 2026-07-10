#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O organismo gasta tanto trabalho molecular para matar células no momento certo quanto para fazê-las nascer, e o equilíbrio entre essas duas forças é o que mantém um tecido funcional. Quando o balanço pende para pouca morte, surgem cânceres e doenças autoimunes; para muita morte, surgem neurodegeneração (Alzheimer, Parkinson), AIDS, anemia aplástica e a lesão isquêmica do infarto e do AVC. Por isso morte celular é capítulo de fisiologia, não só de patologia.

  O caminho aqui é em três passos: primeiro entender quais sinais decidem se a célula vive ou morre; depois mergulhar na #sigla("RCD", [_regulated cell death_ — morte celular regulada, conjunto de programas moleculares de morte ativa]) por excelência, a apoptose, com seus dois caminhos para o mesmo destino; por fim conhecer rotas alternativas — autofagia, necroptose, piroptose, ferroptose — que existem porque a apoptose nem sempre é a melhor saída, e porque alguns patógenos aprenderam a bloqueá-la.
]

// ============================================================
#parte-title("PARTE I — Por que uma célula precisaria morrer", primeira: true)
// ============================================================

#subtopico("1.1 — A célula nunca está sozinha")

Uma célula isolada num tubo de ensaio, mantida em condições ideais de nutrientes e temperatura, ainda assim morre depois de algumas horas. Esse fato singelo guarda uma das ideias mais importantes da biologia celular moderna: em um organismo multicelular, a célula é parte de uma comunidade, e ela só permanece viva enquanto recebe sinais positivos das vizinhas dizendo, em essência, "fique". Sem esses sinais, o programa-padrão é morrer.

Isso é exatamente o oposto da intuição de quem está começando. Faz sentido pensar que célula vive até algo dar errado — uma infecção, uma toxina, uma lesão. Mas no tecido real o default é morte ativa, e a sobrevivência é um estado mantido por sinalização contínua. Esse desenho evolutivo tem uma lógica clara: numa comunidade de 30 trilhões de células, é mais seguro exigir uma "permissão para existir" do que confiar que cada célula vai se comportar bem por conta própria.

Os sinais que as células trocam para coordenar proliferação e sobrevivência caem em três grandes categorias, descritas no slide de abertura do tema. Observe na figura abaixo como cada categoria atua em um nível distinto da fisiologia celular.

#figura-nebli(
  "/figuras/morte-celular/slide-04.png",
  largura: 60%,
  legenda: [Os três tipos de sinais extracelulares que as células animais recebem: mitógenos disparam divisão, fatores de crescimento aumentam massa proteica, fatores de sobrevivência suprimem o programa apoptótico. Adaptado de Alberts, _Fundamentos da Biologia Celular_, 3ª ed.],
)

#termo-nota[Mitógeno][substância que estimula a célula a entrar no ciclo de divisão, atuando principalmente em G1] — sinais como #sigla("PDGF", [_platelet-derived growth factor_ — fator de crescimento derivado de plaquetas]) e #sigla("EGF", [_epidermal growth factor_ — fator de crescimento epidérmico]) ativam vias que liberam freios moleculares (a proteína #termo-nota[Rb][_retinoblastoma_, proteína-freio que mantém E2F sequestrado e impede transcrição de genes da fase S]), permitindo a transição G1→S. *Fatores de crescimento* atuam em outro nível: aumentam a síntese e diminuem a degradação de proteínas, fazendo a célula crescer em massa sem necessariamente forçá-la a dividir. Os dois tipos podem coincidir — o próprio PDGF, por exemplo, atua simultaneamente como mitógeno e fator de crescimento — mas conceitualmente são funções distintas, e essa distinção reaparece em vários momentos adiante.

A terceira categoria é a que mais interessa aqui: *fatores de sobrevivência*. São proteínas como o #sigla("NGF", [_nerve growth factor_ — fator de crescimento neural, identificado por Levi-Montalcini]) e várias interleucinas que se ligam a receptores na superfície da célula e mantêm ativa uma sinalização interna que *bloqueia ativamente o programa de apoptose*. Sem o sinal, a apoptose começa. Esse mecanismo está por trás de um princípio elegante do desenvolvimento embrionário: o tecido-alvo libera quantidade limitada de fator de sobrevivência, e o número de neurônios que sobrevivem é exatamente o número que aquele tecido consegue sustentar. As outras células nervosas, que receberam sinal insuficiente, simplesmente morrem.

#figura-nebli(
  "/figuras/morte-celular/slide-09.png",
  largura: 65%,
  legenda: [Fatores de sobrevivência liberados pelas células-alvo combinam o número de neurônios com o número de células-alvo. Esse mecanismo "calibra" populações neurais durante o desenvolvimento.],
)

#sintese-box("1.1")[Em um organismo multicelular, sobreviver é decisão ativa que depende de sinais externos. Sem mitógenos, a célula não divide; sem fatores de crescimento, ela não cresce; sem fatores de sobrevivência, ela ativa o programa interno de morte por apoptose.]

#subtopico("1.2 — Homeostase de tecido: o equilíbrio entre nascimento e morte")

Em qualquer tecido adulto saudável, o número de células permanece aproximadamente constante. Isso parece óbvio até alguém perguntar como. As células do epitélio intestinal, por exemplo, são totalmente renovadas a cada três a cinco dias — todas as células do intestino atual já estão mortas antes do fim do mês. Em valores absolutos, são bilhões de células nascendo e morrendo por dia só nesse epitélio. Esse turnover só funciona porque taxa de divisão e taxa de morte estão acopladas: se uma sobe ou desce, a outra precisa acompanhar.

#figura-nebli(
  "/figuras/morte-celular/slide-11.png",
  largura: 70%,
  legenda: [Homeostase tecidual como balança entre divisão e morte celular. Desbalanço para esquerda (mais morte) gera doenças de perda celular: AIDS, Alzheimer, Parkinson, anemia aplástica, infarto. Desbalanço para direita (menos morte) gera acúmulo: câncer, lúpus, glomerulonefrite, infecções virais persistentes.],
)

A figura acima é a melhor síntese clínica do tema. Quando a balança pende para o lado da morte (esquerda), perdem-se células que deveriam permanecer: linfócitos CD4 destruídos pelo HIV, neurônios da substância negra perdidos no Parkinson, cardiomiócitos mortos por isquemia no infarto. Quando pende para o lado oposto, células que deveriam morrer continuam vivas: clones autoimunes que escaparam da seleção tímica geram lúpus; células com mutações acumuladas que escaparam da apoptose viram tumores. Essa é a moldura clínica de tudo que vem depois — todo mecanismo que será detalhado nesta apostila é, em última análise, um ponto onde essa balança pode pender errado.

Um exemplo paradigmático: durante o desenvolvimento embrionário, os dedos da mão e do pé são esculpidos por morte celular dirigida. As células do tecido interdigital recebem sinal pró-apoptótico e morrem em massa, deixando os dedos separados. Onde a apoptose falha (mutações em genes da via), os dedos nascem unidos — sindactilia. É o exemplo mais visualmente claro de que morrer no momento certo constrói forma.

#figura-lateral(
  "/figuras/morte-celular/slide-18.png",
  lado: "right",
  largura-figura: 38%,
  texto: [Na pata embrionária de camundongo, a marcação fluorescente de células apoptóticas (à esquerda, em verde brilhante) coincide exatamente com os interdígitos que serão eliminados. Algumas horas depois (à direita), o tecido apoptótico foi fagocitado e os dedos aparecem separados. Sem essa onda controlada de morte, a mão nasceria com membranas — um defeito chamado sindactilia. O mesmo princípio aplica-se ao tubo neural, ao esôfago em formação, à reabsorção da cauda em anfíbios. Morte celular é, literalmente, ferramenta de escultura embrionária.],
  legenda: [Apoptose interdigital no embrião.],
)

#subtopico("1.3 — Três modos de morrer: a taxonomia moderna")

Por décadas, a morte celular foi dividida em apenas duas caixas: necrose, descrita como acidental e passiva, e apoptose, descrita como programada e ativa. Essa dicotomia ainda aparece em muitos livros-texto, mas foi superada pela pesquisa dos últimos quinze anos. Hoje a divisão é diferente, e vale a pena absorvê-la com cuidado.

A nomenclatura atual, consolidada pelo Comitê de Nomenclatura sobre Morte Celular (Galluzzi e colaboradores, 2018), reconhece três categorias.

A primeira é a #sigla("ACD", [_accidental cell death_ — morte celular acidental, sem programa molecular regulador]), a morte verdadeiramente passiva: uma célula esmagada por trauma físico, queimada por temperatura extrema, dissolvida por solvente. Não há via molecular controlando o processo, não há decisão da célula, simplesmente a integridade é perdida. ACD é o que sobra do conceito antigo de "necrose passiva" — bem menos frequente do que se imaginava.

A segunda é a RCD, que inclui qualquer morte com via molecular dedicada e que pode ser modulada farmacologicamente. Apoptose, autofagia que mata (autosis), necroptose, piroptose, ferroptose, parthanatos — todas são RCDs. Notem que algumas têm morfologia de necrose (incham, lisam, liberam conteúdo) e mesmo assim são reguladas. *A morfologia sob microscópio não é critério: o que define RCD é existir uma via molecular controlando, com proteínas específicas que podem ser inibidas ou ativadas.* Essa é a inversão conceitual mais importante deste tema.

A terceira é a #sigla("PCD", [_programmed cell death_ — morte celular programada, subset estritamente fisiológico da RCD]), um subset da RCD restrito a contextos fisiológicos normais. PCD é a morte que esculpe os dedos do embrião, que renova o epitélio intestinal, que elimina linfócitos autorreativos no timo. Quando a mesma maquinaria é disparada por estresse patológico (DNA danificado, infecção, isquemia), o evento ainda é RCD, mas deixa de ser PCD em sentido estrito.

#confusao-prevista(
  titulo: "Necrose nem sempre é acidental",
  aluno_acha: [aluno acha que necrose visual (célula incha, membrana rompe, libera conteúdo) é sinônimo de morte acidental, sem programa.],
  mecanismo: [necroptose, piroptose, MPT-driven necrosis e ferroptose têm exatamente essa morfologia mas são vias moleculares dedicadas, reguladas por proteínas identificáveis (MLKL, gasdermina D, ciclofilina D, GPX4). A morfologia engana — o critério moderno é a via molecular, não a aparência.],
)

#figura-nebli(
  "/figuras/morte-celular/slide-21.png",
  largura: 65%,
  legenda: [A roda da RCD: ao centro, o conceito-mãe; em cada raio, uma forma de morte regulada. Apoptose (intrínseca, extrínseca, ICD imunogênica) à esquerda, vias com morfologia necrótica (necroptose, ferroptose, piroptose, MPT-driven) à direita. Note as setas duplas no centro — apoptose e necrose são polos morfológicos, não categorias estanques.],
)

#sintese-box("1.3")[Morte verdadeiramente passiva (ACD) é exceção. A regra na biologia é morte regulada (RCD), com vias moleculares dedicadas. Apoptose é a RCD mais estudada, mas não a única; e algumas RCDs têm morfologia de necrose mesmo sendo totalmente programadas.]

#mini-resumo[
  O encerramento da PARTE I deixa três ideias plantadas. Primeiro, célula em organismo multicelular sobrevive por permissão ativa, não por inércia — sem sinais, morre. Segundo, o tecido mantém número estável de células acoplando taxa de nascimento com taxa de morte, e doenças surgem quando esse acoplamento se desfaz. Terceiro, a morte celular não é um único processo: existem vários programas moleculares distintos, e o que importa para classificá-los hoje é a via molecular, não a aparência. A PARTE II entra na via mais central — apoptose — em detalhe mecanístico.
]

// ============================================================
#parte-title("PARTE II — Apoptose: a morte limpa que não inflama")
// ============================================================

#subtopico("2.1 — A morfologia: encolhe, condensa, fragmenta, é fagocitada")

A apoptose tem uma assinatura visual muito característica. A célula apoptótica encolhe (perde volume, ao contrário da célula necrótica que incha), o citoesqueleto colapsa, o envelope nuclear se desfaz, a cromatina condensa em massas densas e é cortada em fragmentos regulares por endonucleases ativadas. A membrana plasmática faz protrusões arredondadas — os _blebs_ — que se destacam carregando porções de citoplasma com organelas dentro. Esses fragmentos são os *corpos apoptóticos*.

Observe na figura abaixo a comparação lado a lado entre os dois processos morfológicos mais importantes deste resumo.

#figura-nebli(
  "/figuras/morte-celular/slide-25.png",
  largura: 70%,
  legenda: [Comparação morfológica clássica. À esquerda: necrose — a célula incha rapidamente (_swelling_), a membrana lesa, organelas se desorganizam, o conteúdo escapa e desencadeia inflamação. À direita: apoptose — a célula encolhe, o DNA é fragmentado por endonucleases, surgem _blebs_ e corpos apoptóticos que são fagocitados antes de qualquer extravasamento.],
)

A diferença crítica é a integridade da membrana plasmática. Em necrose, a membrana se rompe cedo no processo e o conteúdo citoplasmático — incluindo enzimas, ATP, ácidos nucleicos e moléculas chamadas #sigla("DAMP", [_damage-associated molecular pattern_ — padrão molecular associado a dano, incluindo HMGB1, ATP extracelular, DNA, RNA, cristais de ácido úrico]) — vaza para o meio extracelular. As DAMPs são reconhecidas por receptores do sistema imune inato e disparam inflamação local intensa. Em apoptose, a membrana *permanece íntegra* até os corpos apoptóticos serem fagocitados, e o conteúdo nunca chega ao interstício. Por isso a apoptose é descrita como "morte limpa" — não inflama.

#atencao-box(
  "A apoptose precisa de ATP",
  [Apesar de ser morte, apoptose não é falência energética: ela requer ATP ativamente. Sem energia, a célula não consegue executar o programa (ativar caspases, externalizar fosfatidilserina, fazer _blebbing_) e acaba indo para necrose. Por isso uma célula em isquemia profunda — que perdeu ATP — morre por necrose, não por apoptose, mesmo que tenha recebido sinais pró-apoptóticos. O programa só roda enquanto há combustível.],
)

A duração também surpreende. Da decisão de morrer até a fragmentação completa em corpos apoptóticos passam-se cerca de duas horas; a fagocitose subsequente, mais algumas horas. É rápido o suficiente para que, em tecidos normais, raramente se vejam células apoptóticas em cortes histológicos — quando uma célula entra em apoptose, ela some antes do próximo corte do micrótomo. Isso, paradoxalmente, escondeu o fenômeno dos histopatologistas por décadas.

#subtopico("2.2 — O sinal 'coma-me': fosfatidilserina na face externa")

Como o macrófago sabe que uma célula está apoptótica e precisa ser fagocitada? Por uma alteração química na superfície. A célula viva mantém uma assimetria estrita na bicamada lipídica: fosfolipídios com colina (fosfatidilcolina, esfingomielina) ficam na face externa, e fosfolipídios com grupos amino (fosfatidiletanolamina, e principalmente fosfatidilserina) ficam na face interna, voltados para o citosol.

#termo-nota[Fosfatidilserina][fosfolipídio aniônico restrito à face citoplasmática da membrana em células vivas; sua externalização sinaliza apoptose] não passa para a face externa por acaso. Duas enzimas trabalham continuamente: a #termo-nota[flipase][bomba ATP-dependente que move fosfatidilserina do folheto externo para o interno, mantendo a assimetria] consome ATP para empurrar fosfatidilserina de volta para dentro sempre que ela tentar passar; e a #termo-nota[scramblase][enzima ATP-independente, ativada por cálcio ou por caspases, que embaralha lipídios entre os folhetos sem direção preferencial], normalmente inativa, pode embaralhar lipídios entre os dois folhetos sem direção preferencial. Em apoptose, caspases ativas inativam a flipase *e* ativam a scramblase — o resultado é que fosfatidilserina aparece rapidamente na face externa.

#figura-nebli(
  "/figuras/morte-celular/slide-34.png",
  largura: 60%,
  legenda: [Acima, a célula normal mantém fosfatidilserina (em vermelho) restrita à face citoplasmática pela ação contínua da flipase ATP-dependente. Abaixo, na célula apoptótica, flipase inativada e scramblase ativa fazem fosfatidilserina aparecer também na face externa — sinal "coma-me" para macrófagos.],
)

Macrófagos têm receptores específicos (TIM4, BAI1, estabilinas) que reconhecem fosfatidilserina externalizada e iniciam a fagocitose. E há um detalhe importante: essa fagocitose é *imunossupressora*. Quando o macrófago engole corpos apoptóticos via reconhecimento de fosfatidilserina, ele responde produzindo citocinas anti-inflamatórias (IL-10, TGF-β) e suprimindo as pró-inflamatórias (IL-12). Isso é o oposto do que ele faz ao engolir bactéria ou debris necrótico. A morte limpa permanece limpa em todo o ciclo: a célula não vaza conteúdo, e o macrófago não inflama.

#clinica-box(
  "Detecção de apoptose em laboratório (citometria)",
  [Essa propriedade molecular vira ferramenta diagnóstica. *Anexina V* é uma proteína que se liga com alta afinidade à fosfatidilserina; marcada com fluoróforo, ela coloriu células com fosfatidilserina exposta — ou seja, apoptóticas. Combinada com *iodeto de propídio* (PI, que só entra em células com membrana rompida), permite distinguir quatro estados em citometria de fluxo: anexina V negativo / PI negativo = viva; anexina V positivo / PI negativo = apoptose inicial (membrana íntegra, PS exposta); anexina V positivo / PI positivo = apoptose tardia ou necrose secundária; anexina V negativo / PI positivo = necrose pura. Este kit é rotineiro em laboratórios de pesquisa oncológica e hematológica.],
)

#figura-nebli(
  "/figuras/morte-celular/slide-37.png",
  largura: 70%,
  legenda: [Os quatro quadrantes do ensaio anexina V + PI. Inverter os eixos é a confusão clássica do tema — vale o gesto de redesenhar mentalmente o quadrante até dominar.],
)

#subtopico("2.3 — A maquinaria executora: cascata de caspases")

Toda a destruição organizada da apoptose é executada por uma família de proteases chamadas #termo-nota[caspase][_cysteine-aspartate-specific protease_ — protease com cisteína no sítio ativo que cliva proteínas-alvo logo após resíduos de aspartato]. O nome carrega o mecanismo: têm uma *c*isteína no sítio ativo (cysteine-...) e cortam suas proteínas-alvo logo depois de resíduos de *asp*artato (...-aspartate). A especificidade é tão precisa que a sequência completa de quatro aminoácidos antes do aspartato decide se uma proteína será ou não substrato.

As caspases existem em duas categorias funcionais que vale a pena fixar antes de qualquer detalhe de via.

#figura-nebli(
  "/figuras/morte-celular/slide-39.png",
  largura: 75%,
  legenda: [À esquerda, ativação de uma pró-caspase por clivagem: duas moléculas inativas se aproximam, são clivadas nos sítios marcados, perdem os pró-domínios e formam uma caspase ativa em formato tetramérico (duas subunidades grandes + duas pequenas). À direita, a cascata amplificadora: uma molécula de caspase iniciadora ativa várias caspases executoras, que por sua vez clivam centenas de substratos. Adaptado de Alberts, _Biologia Molecular da Célula_, 5ª ed.],
)

*Caspases iniciadoras* (caspase-2, -8, -9, -10) começam a cascata. São sintetizadas como zimogênios inativos (pró-caspases) com pró-domínios longos contendo domínios de interação proteína-proteína — #sigla("DED", [_death effector domain_ — domínio efetor de morte, presente em FADD e pró-caspase-8/10]) ou #sigla("CARD", [_caspase recruitment domain_ — domínio de recrutamento de caspases, presente em Apaf-1 e pró-caspase-9]). Quando estímulos apropriados chegam, esses domínios fazem as pró-caspases se agruparem em *plataformas de ativação*, e a proximidade forçada é suficiente para que elas se cortem mutuamente, gerando caspases ativas. Isso se chama "ativação por proximidade induzida".

*Caspases executoras* (caspase-3, -6, -7) não se ativam por proximidade. Elas existem como pró-caspases no citosol até serem cortadas por uma caspase iniciadora — daí em diante, ficam ativas e degradam centenas de substratos celulares: lâminas nucleares (envelope nuclear se desfaz), citoesqueleto (célula colapsa), ICAD (inibidor de uma DNAse — quando cortado, libera CAD que fragmenta o DNA), proteínas que mantêm a flipase ativa, e assim por diante. A caspase-3 é a executora-mor e o marcador laboratorial mais usado de apoptose.

O sistema é em cascata e amplifica: poucas caspases iniciadoras geram muitas caspases executoras, que geram danos massivos. Por isso, em determinado ponto, o processo se torna *irreversível* — quantas executoras existem ativas, em quantos substratos elas já agiram, simplesmente passa do que a célula consegue reparar.

#subtopico("2.4 — Via extrínseca: a ordem vem de fora")

Existem duas grandes rotas para chegar até as caspases executoras. A primeira começa fora da célula — daí o nome *extrínseca* — e usa receptores específicos da família TNF chamados receptores de morte.

O exemplo mais clássico é o par Fas/FasL. Um linfócito T citotóxico identifica uma célula que precisa morrer (infectada por vírus, transformada em câncer, autorreativa) e exibe na sua membrana o ligante de Fas (FasL). A célula-alvo tem em sua membrana o receptor Fas. O encontro entre os dois agrupa três moléculas de Fas, e esse agrupamento expõe, na cauda citoplasmática, três domínios de morte (#sigla("DD", [_death domain_ — domínio de morte, motivo de interação proteína-proteína de receptores como Fas/TNFR1 e do adaptador FADD])). A esses DDs se acopla a proteína adaptadora #sigla("FADD", [_Fas-associated death domain_ — adaptadora citoplasmática que conecta receptor de morte à pró-caspase-8]), que por sua vez recruta pró-caspase-8 por interação DED-DED. O complexo formado é o #sigla("DISC", [_death-inducing signaling complex_ — complexo de sinalização indutor de morte, plataforma da via extrínseca]).

#figura-nebli(
  "/figuras/morte-celular/slide-44.png",
  largura: 75%,
  legenda: [Sequência da via extrínseca. O linfócito matador exibe FasL na superfície (esquerda). FasL liga Fas na célula-alvo, agrupando três receptores. Os domínios de morte (DD) intracelulares recrutam FADD via interação DD-DD, e FADD recruta pró-caspase-8/10 via interação DED-DED. O complexo DISC fica montado. Caspase-8 ativa por proximidade cliva caspases executoras, e a célula-alvo segue para apoptose.],
)

No DISC, várias pró-caspase-8 se aproximam, se clivam mutuamente e ficam ativas. A caspase-8 ativa cliva diretamente caspase-3 — em algumas células, isso basta para disparar apoptose completa (essas são chamadas células "tipo I", como linfócitos). Em outras células, ditas "tipo II" (hepatócitos, células beta pancreáticas, muitos epitélios), a quantidade de caspase-8 ativa gerada no DISC é insuficiente; é preciso amplificar pela via intrínseca — o que será detalhado em 2.6.

A célula tem freios contra a via extrínseca, e vale conhecer dois para entender a regulação. *Receptores armadilha* (DcR1, DcR2) ligam FasL exatamente como o Fas verdadeiro, mas têm o domínio de morte intracelular truncado ou ausente — capturam o ligante e não sinalizam. *FLIP* (FLICE-inhibitory protein) é uma cópia de pró-caspase-8 com os DEDs funcionais (entra no DISC normalmente) mas sem o sítio ativo proteolítico — ocupa lugar no DISC sem cortar nada, diluindo a sinalização. Ambos são pontos de regulação fina aproveitados terapeuticamente (e por vírus que querem manter a célula viva).

#subtopico("2.5 — Via intrínseca: a mitocôndria como sensor")

A segunda rota não precisa de ligante externo. Ela monitora o estado interno da célula — danos ao DNA, estresse de retículo, falta de nutrientes, perda de aderência, infecção viral percebida internamente — e usa a *mitocôndria* como centro decisor. Por isso essa via é chamada de *intrínseca* ou *mitocondrial*.

O evento-chave é a #sigla("MOMP", [_mitochondrial outer membrane permeabilization_ — permeabilização da membrana mitocondrial externa, ponto de não-retorno da via intrínseca]) — permeabilização da membrana mitocondrial externa. Quando MOMP ocorre, proteínas que ficam normalmente no espaço entre as duas membranas mitocondriais escapam para o citosol. A mais famosa é o *citocromo c*, que todos conhecem do contexto da cadeia respiratória.

#confusao-prevista(
  titulo: "O citocromo c que mata é o mesmo que respira",
  aluno_acha: [aluno acha que há um citocromo c "apoptótico" diferente do citocromo c da cadeia respiratória.],
  mecanismo: [é exatamente a mesma proteína, no mesmo compartimento (espaço intermembranar). Em condições normais, ela transporta elétrons entre os complexos III e IV. Quando BAK/BAX permeabilizam a membrana externa, ela escapa para o citosol e ganha uma segunda função: nuclear o apoptossomo. A função depende da localização, não da identidade molecular.],
)

#figura-nebli(
  "/figuras/morte-celular/slide-46.png",
  largura: 80%,
  legenda: [Sequência da via intrínseca. (1) Estímulo apoptótico abre o poro na membrana mitocondrial externa. (2) Citocromo c (vermelho) escapa para o citosol. (3) Apaf-1, normalmente citosólico, liga citocromo c, hidrolisa dATP e muda de conformação. (4) Sete moléculas de Apaf-1 se oligomerizam em uma roda — o apoptossomo. (5) Cada raio recruta uma pró-caspase-9 via interação CARD-CARD. (6) A proximidade ativa caspase-9, que cliva caspase-3.],
)

Uma vez no citosol, citocromo c encontra *Apaf-1* (apoptotic protease-activating factor 1), que estava lá inativo. Apaf-1 tem um domínio CARD na ponta. O encontro com citocromo c, na presença de dATP, faz Apaf-1 mudar de conformação e expor o CARD. Sete moléculas de Apaf-1 se juntam, formando uma estrutura em forma de roda com sete raios — o #termo-nota[apoptossomo][complexo heptamérico de Apaf-1 + citocromo c + dATP que recruta e ativa pró-caspase-9, plataforma central da via intrínseca]. Cada raio recruta uma pró-caspase-9 via interação CARD-CARD. As sete pró-caspase-9 ficam próximas, se ativam e formam a versão intrínseca da plataforma de ativação. Caspase-9 ativa cliva caspase-3 — e a partir daí, a fase executora é a mesma.

Note o paralelismo entre as duas vias. Em ambas, o ponto crítico é montar uma plataforma onde pró-caspases iniciadoras se agrupam e se ativam por proximidade. No DISC, a plataforma é construída por FADD; no apoptossomo, por Apaf-1 + citocromo c. Diferentes sensores, mesma lógica.

#subtopico("2.6 — A família Bcl-2 decide se a mitocôndria libera o sinal")

Como a célula controla se MOMP ocorre ou não? Aqui entra uma das famílias proteicas mais estudadas em biologia celular: a família *Bcl-2*. O nome vem do primeiro membro identificado, descoberto em um linfoma de células B humano (_B-cell lymphoma 2_) onde uma translocação cromossômica fazia essa proteína ser superexpressa, e as células do linfoma não morriam quando deveriam.

A família tem três classes funcionais, e confundi-las é o erro clássico do tema. A tabela abaixo organiza:

#table(
  columns: (1.1fr, 1.5fr, 1.3fr, 1.2fr),
  align: (left, left, left, left),
  stroke: 0.5pt + gray-border,
  fill: (col, row) => if row == 0 { navy } else if calc.rem(row, 2) == 0 { gray-bg } else { none },
  table.header(
    [#text(fill: white, weight: "bold")[Classe]],
    [#text(fill: white, weight: "bold")[Função na mitocôndria]],
    [#text(fill: white, weight: "bold")[Domínios BH]],
    [#text(fill: white, weight: "bold")[Exemplos]],
  ),
  [Efetoras pró-morte], [Oligomerizam na membrana mitocondrial externa e formam o poro do MOMP], [BH1, BH2, BH3], [BAX, BAK, BOK],
  [Antiapoptóticas], [Sequestram efetoras e ativadoras BH3-only, impedem MOMP], [BH1, BH2, BH3, BH4], [Bcl-2, Bcl-X#sub[L], Mcl-1, A1],
  [BH3-only ativadoras], [Ligam diretamente BAX/BAK e os ativam], [BH3 apenas], [Bid, Bim, Puma],
  [BH3-only sensibilizadoras], [Ocupam antiapoptóticas, liberando indiretamente BAX/BAK], [BH3 apenas], [Bad, Noxa, Bik, Bmf],
)

O que decide se MOMP ocorre é a *razão* entre antiapoptóticas e pró-apoptóticas dentro daquela célula, naquele momento. Em repouso, as antiapoptóticas (Bcl-2, Bcl-X#sub[L], Mcl-1) ficam na membrana mitocondrial externa segurando BAX/BAK e sequestrando qualquer BH3-only que apareça. A célula está viva.

Quando um estímulo apoptótico chega, ele ativa transcrição de BH3-only ou modifica BH3-only pós-traducionalmente (por exemplo, dano de DNA → p53 → transcreve Puma e Noxa; estresse de retículo → Bim aumentada). As BH3-only ativadoras (Bid, Bim, Puma) ligam diretamente em BAX/BAK e os ativam, enquanto as sensibilizadoras (Bad, Noxa) competem com BAX/BAK pelos sítios das antiapoptóticas, liberando as efetoras. Quando o equilíbrio pende para o lado pró-morte, BAX/BAK oligomerizam, abrem o poro, citocromo c escapa, e o apoptossomo se forma.

#figura-nebli(
  "/figuras/morte-celular/slide-51.png",
  largura: 80%,
  legenda: [À esquerda, lógica espacial na mitocôndria: em via inativa, antiapoptóticas (laranja) seguram as efetoras BAX/BAK (verde). Estímulo apoptótico ativa BH3-only, que liberam ou ativam BAX/BAK, formando o poro do MOMP. À direita, organograma funcional: BH3-only sensitizadoras alvejam antiapoptóticas; BH3-only ativadoras alvejam efetoras; o ponto final é MOMP, liberação de citocromo c, ativação de caspase-9 e apoptose.],
)

#clinica-box(
  "Venetoclax — atacando Bcl-2 em leucemia",
  [O venetoclax é uma droga oral aprovada para leucemia linfocítica crônica e leucemia mielóide aguda. Ele é um "BH3-mimético" — uma pequena molécula que imita a face funcional de uma BH3-only sensibilizadora e ocupa o sítio de Bcl-2. Em células leucêmicas que dependem de Bcl-2 superexpressa para evitar apoptose, o venetoclax libera BAX/BAK das antiapoptóticas, MOMP acontece, e as células leucêmicas entram em apoptose. É o primeiro exemplo clínico de manipular diretamente a família Bcl-2 — e a base para uma nova classe de "drogas pró-apoptóticas" em oncologia.],
)

#subtopico("2.7 — Conversa entre vias: caspase-8, Bid e a amplificação")

As duas vias não funcionam isoladas. Existe um elo direto, descoberto há cerca de duas décadas, que conecta a via extrínseca à intrínseca: a clivagem de *Bid* pela *caspase-8*.

Quando a caspase-8 é ativada no DISC, ela tem dois substratos preferenciais. Em células tipo I, ela cliva diretamente caspase-3 em quantidade suficiente para terminar o serviço. Em células tipo II, a quantidade de caspase-3 ativada não basta; o trabalho real é feito por caspase-8 clivando outra proteína — Bid, uma BH3-only. Bid em sua forma íntegra está no citosol, inativa. Quando caspase-8 a cliva, o fragmento gerado (tBid, _truncated Bid_) migra para a mitocôndria e ativa BAX/BAK como um BH3-only ativador clássico. Resultado: o sinal extrínseco vira sinal intrínseco, MOMP ocorre, citocromo c escapa, e a via intrínseca amplifica massivamente o que a extrínseca começou.

#figura-nebli(
  "/figuras/morte-celular/slide-53.png",
  largura: 70%,
  legenda: [A ponte entre vias. TNF/Fas ativam DISC e caspase-8. Caspase-8 cliva Bid, formando tBid. tBid migra à mitocôndria, ativa BAX/BAK, dispara MOMP e a via intrínseca segue como em qualquer apoptose mitocondrial. A direção é uma só: extrínseca → intrínseca, nunca o contrário.],
)

Essa é a razão para a aparente redundância. Hepatócitos, que têm pouca caspase-8 disponível, dependem da amplificação pela via intrínseca; sem Bid, eles ficam resistentes à apoptose mediada por Fas. Camundongos com deleção de Bid sobrevivem a doses de FasL que matam camundongos selvagens — confirmando experimentalmente a função da ponte.

#subtopico("2.8 — Freios moleculares: IAPs e Smac/Diablo")

Há ainda uma segunda camada de regulação, depois das caspases já terem sido ativadas. Proteínas chamadas #sigla("IAP", [_inhibitor of apoptosis protein_ — proteína inibidora de apoptose, ex.: XIAP, cIAP1, cIAP2; inibe caspases ativas diretamente]) (XIAP, cIAP1, cIAP2) ligam-se diretamente a caspases ativas (especialmente caspase-3, -7 e -9) e bloqueiam o sítio ativo. É como um freio extra: mesmo que algumas caspases tenham sido ativadas inadvertidamente, IAPs evitam que disparem a cascata até o final.

Para que a apoptose realmente aconteça, esse freio precisa ser removido. Quando MOMP ocorre, além de citocromo c, escapam outras proteínas do espaço intermembranar — *Smac/Diablo* e *Omi/HtrA2*. Essas proteínas se ligam às IAPs com altíssima afinidade e as deslocam das caspases. Resultado: as caspases são liberadas, e a cascata segue.

#figura-nebli(
  "/figuras/morte-celular/slide-57.png",
  largura: 75%,
  legenda: [O sistema IAP/anti-IAP funciona como dupla checagem. Em repouso, mesmo que pequenas quantidades de caspase ativa apareçam, IAPs (laranja) as bloqueiam. Quando MOMP ocorre (painel B), Smac/Diablo escapa junto com citocromo c, neutraliza IAPs, e as caspases executoras ficam livres para atuar.],
)

Esse design serve a um propósito claro: garantir que apoptose não ocorra por ativação espontânea ou acidental de poucas caspases. Só quando o conjunto de sinais (BH3-only ativos, MOMP, Smac/Diablo liberado) confirma a decisão é que o processo se torna irreversível. É um sistema de duas chaves: BAX/BAK abrem a primeira (citocromo c, montagem do apoptossomo), Smac/Diablo abre a segunda (libera caspases das IAPs).

#subtopico("2.9 — Fatores de sobrevivência: três alavancas paralelas")

Voltando ao começo — a célula precisa de sinais externos para não morrer. Como, mecanicamente, um fator de sobrevivência impede a apoptose? Por três mecanismos paralelos, que atuam em níveis diferentes da via.

#figura-nebli(
  "/figuras/morte-celular/slide-56.png",
  largura: 80%,
  legenda: [Três rotas pelas quais um fator de sobrevivência bloqueia apoptose. (A) Transcrição: receptor ativa fator transcricional que aumenta produção de Bcl-2/Bcl-X#sub[L]. (B) Fosforilação: Akt fosforila Bad, inativando-o — Bad não pode mais sequestrar antiapoptóticas. (C) Inativação de Hid (em moscas; em mamíferos a paralela são modificações nas IAPs): MAP-cinase fosforila Hid, IAPs ficam livres para inibir caspases.],
)

O primeiro mecanismo é *transcricional*. O receptor do fator de sobrevivência ativa uma via que termina ligando fatores de transcrição (como NF-κB ou CREB) que aumentam a produção de proteínas Bcl-2 e Bcl-X#sub[L]. Em horas, a célula tem mais antiapoptóticas — a razão pró/anti se desloca para o lado da sobrevivência.

O segundo é *pós-traducional rápido*. A via #sigla("PI3K", [_phosphoinositide 3-kinase_ — quinase que fosforila inositol da membrana, gerando PIP3 que recruta Akt])/Akt, ativada pelo receptor, fosforila a BH3-only Bad em um resíduo específico. Bad fosforilada é sequestrada no citosol por proteínas 14-3-3 e não consegue mais ir à mitocôndria sequestrar antiapoptóticas. É a mesma molécula com função opcional, controlada por uma fosforilação.

O terceiro atua nas IAPs. Sinais da via MAP-cinase modificam Hid (em invertebrados, e proteínas funcionalmente análogas em mamíferos), neutralizando antagonistas das IAPs. As IAPs ficam livres para bloquear caspases acidentalmente ativadas.

Os três mecanismos somam efeitos. Por isso uma célula bem nutrida e bem sinalizada é extremamente resistente a estímulos pró-apoptóticos: ela tem antiapoptóticas em alta concentração, BH3-only sequestradas, e IAPs ativas. Para matá-la, é preciso superar todas as três barreiras simultaneamente.

#mini-resumo[
  Fecha a PARTE II. A apoptose tem morfologia limpa porque a membrana não rompe; tem sinalização sem inflamação porque o macrófago lê fosfatidilserina externalizada como sinal anti-inflamatório; tem maquinaria executora baseada em caspases organizadas em cascata (iniciadoras → executoras); tem duas rotas de disparo (extrínseca por receptores de morte, intrínseca por MOMP mitocondrial) que conversam via tBid; é regulada por uma família proteica de três classes (efetoras, antiapoptóticas, BH3-only), por uma segunda camada de freios (IAPs e Smac/Diablo), e por uma terceira camada extracelular (fatores de sobrevivência ativando três rotas paralelas de proteção). Toda essa complexidade existe porque a decisão de morrer precisa ser segura — uma vez tomada, é irreversível.
]

// ============================================================
#parte-title("PARTE III — Quando a apoptose não é a saída")
// ============================================================

#subtopico("3.1 — Autofagia: amiga sob fome, executora em excesso")

A apoptose resolve a maioria dos cenários, mas não todos. Existem situações em que a célula precisa de uma rota diferente — ou porque a apoptose não dá conta sozinha, ou porque foi sabotada por um patógeno, ou porque o tipo de estímulo pede uma resposta inflamatória deliberada. A PARTE III olha para essas alternativas, começando pela mais ambígua: a autofagia.

Autofagia, literalmente "comer a si mesmo", é um processo de reciclagem interna. Uma membrana dupla (o fagóforo) se forma no citosol, envolve uma porção de citoplasma — que pode incluir mitocôndrias velhas, proteínas mal-dobradas, agregados, ou simplesmente porções aleatórias — e fecha-se em uma vesícula chamada *autofagossomo*. O autofagossomo então se funde com lisossomos, formando o autofagolisossomo, e seu conteúdo é digerido por enzimas lisossômicas. Os monômeros gerados (aminoácidos, açúcares, ácidos graxos) voltam ao citosol para serem reutilizados.

#figura-nebli(
  "/figuras/morte-celular/slide-64.png",
  largura: 70%,
  legenda: [Autofagia em contexto comparativo. Diferente da endocitose mediada por receptor (em vermelho, traz material externo) e da fagocitose de patógenos (em azul, traz bactéria), a autofagia (em verde) opera sobre conteúdo próprio: uma membrana isolante (_isolation membrane_) envolve mitocôndria velha e citoplasma, fecha-se em autofagossomo e funde-se com lisossomo.],
)

O propósito primário da autofagia é *sobrevivência*. Quando a célula está em jejum (privada de aminoácidos, glicose, ou fatores de crescimento), ela ativa autofagia para reciclar componentes não essenciais e manter o que importa — proteínas vitais, mitocôndrias funcionais, ATP. É um mecanismo extraordinariamente conservado evolutivamente: leveduras o fazem, plantas o fazem, todos os animais o fazem. As proteínas envolvidas chamam-se #sigla("ATG", [_autophagy-related_ — família de proteínas da maquinaria de autofagia, ex.: Atg5, Atg7, Atg12, e LC3 que é Atg8 em mamíferos]). Em mamíferos, a Atg8 (chamada LC3 nesse contexto) é o marcador experimental clássico: quando conjugada à fosfatidiletanolamina e ancorada à membrana do autofagossomo, ela aparece em pontos brilhantes no citoplasma — fácil de quantificar.

O paradoxo da autofagia é que ela também aparece em células morrendo. Por décadas, isso gerou um debate: a autofagia mata, ou apenas tenta salvar a célula e fracassa? A resposta atual, formalizada pelo Comitê de Nomenclatura, é "ambas, dependendo do contexto". Em condições de estresse moderado e transitório, autofagia é citoprotetora — recicla, sobrevive, melhora. Em estresse persistente e severo, ou quando vias de apoptose estão bloqueadas, pode levar a uma forma de morte chamada *autosis*, dependente da Na⁺/K⁺-ATPase e bloqueável por glicosídeos cardíacos como ouabaína.

#figura-nebli(
  "/figuras/morte-celular/slide-69.png",
  largura: 70%,
  legenda: [O modelo conceitual de "resposta primária × resposta de fallback". Um estresse (jejum, hipoxia, sinal de morte) ativa primeiro autofagia como tentativa de sobrevivência (reversível enquanto o estresse for transitório). Se a apoptose puder ser disparada, a célula vai para apoptose clássica (resposta primária, tipo 1). Se as vias apoptóticas estiverem bloqueadas (-Bak/Bax, -caspases), a autofagia leva à morte tipo 2 (autosis).],
)

#confusao-prevista(
  titulo: "Mais autofagossomos não significa morte por autofagia",
  aluno_acha: [aluno acha que ver muitas vesículas autofágicas em microscopia eletrônica é diagnóstico de morte por autofagia.],
  mecanismo: [na maior parte das vezes, é o oposto — autofagossomos visíveis indicam que a célula está reciclando ativamente para sobreviver. Distinguir morte autofágica de tentativa de sobrevivência exige testes funcionais: bloquear genes Atg (Atg5, Atg7) e ver se a célula vive mais (sugere que autofagia matava) ou morre mais (sugere que autofagia protegia). O marcador morfológico, isolado, não decide.],
)

#subtopico("3.2 — Necroptose: o plano B inflamatório")

Algumas células precisam morrer fazendo barulho. A apoptose silenciosa funciona quando a célula precisa sumir limpa — um neurônio supranumerário no desenvolvimento, um linfócito autorreativo no timo, uma célula epitelial substituída. Mas quando a ameaça é infecciosa, especialmente um patógeno intracelular, morrer em silêncio significa permitir que o patógeno se espalhe sem que o sistema imune perceba. Aqui entra a *necroptose*.

A necroptose foi reconhecida nos anos 2000 e mudou o entendimento de necrose. Morfologicamente, ela parece necrose clássica — célula incha, membrana plasmática rompe, conteúdo extravasa, inflama. Mas molecularmente é um programa dedicado, com proteínas-chave identificáveis: #sigla("RIPK1", [_receptor-interacting protein kinase 1_ — quinase associada a TNFR1 que decide entre sobrevivência, apoptose e necroptose]), RIPK3, e #sigla("MLKL", [_mixed lineage kinase domain-like_ — pseudoquinase fosforilada por RIPK3 que oligomeriza e fura a membrana plasmática na necroptose]).

A via mais estudada parte do mesmo TNFR1 que pode disparar apoptose. Quando TNF se liga a TNFR1, o receptor monta um complexo intracelular contendo RIPK1. Dependendo do contexto (presença ou ausência de ubiquitinação, atividade de caspase-8, expressão de RIPK3), o complexo decide entre três destinos. Se caspase-8 está ativa e disponível, ela cliva RIPK1 e RIPK3 — o complexo dispara apoptose ou sobrevivência via NF-κB. Se caspase-8 está bloqueada (por inibidor químico, deleção genética, ou mais relevante clinicamente, por proteínas virais), RIPK1 e RIPK3 se associam, fosforilam-se mutuamente, e RIPK3 fosforila MLKL. MLKL fosforilada oligomeriza, vai à membrana plasmática e abre poros lá. A célula explode, libera DAMPs, inflama.

#figura-nebli(
  "/figuras/morte-celular/slide-77.png",
  largura: 70%,
  legenda: [A bifurcação molecular do TNFR1. À direita, quando caspase-8 está ativa, o complexo IIa monta-se com caspase-8 funcional — clivagem ativa apoptose. À esquerda, quando caspase-8 está inibida, RIPK1 e RIPK3 ficam livres, formam o complexo IIb (necrossomo), fosforilam MLKL — necroptose. O mesmo receptor, dois destinos opostos, decididos pela presença ou ausência de caspase-8 funcional.],
)

Por que existe esse design? A resposta está em uma corrida evolutiva fascinante. Muitos patógenos intracelulares aprenderam a inibir caspases — porque, da perspectiva do patógeno, é vantajoso manter a célula-hospedeira viva (e fornecedora de recursos) o máximo possível. Vírus como CMV expressam inibidores de caspase-8. Mas a célula adaptou-se: se caspase-8 não funciona, a necroptose toma o lugar, e o patógeno é eliminado junto com a célula numa morte ruidosa que alerta o sistema imune. É um sistema de duas portas: o invasor pode trancar a apoptose, mas não consegue trancar a necroptose ao mesmo tempo.

#clinica-box(
  "Necroptose em isquemia-reperfusão",
  [Além do contexto infeccioso, necroptose tem papel em lesões de isquemia-reperfusão (infarto, AVC, transplante de órgão). Quando o tecido reperfunde após período sem oxigênio, células danificadas que ainda não morreram ativam necroptose em massa, e a inflamação subsequente expande a área lesada para além do núcleo isquêmico original. Inibidores de RIPK1 (necrostatinas) estão em ensaios clínicos justamente para limitar esse "halo" inflamatório. É um exemplo direto de manipular morte regulada como estratégia terapêutica.],
)

#subtopico("3.3 — Piroptose, ferroptose e outras rotas")

A roda da RCD que aparece em 1.3 tem ainda outras formas, cada uma com bioquímica própria. Vale conhecer pelo menos três pela relevância clínica.

A *piroptose* depende de uma caspase diferente — a #termo-nota[caspase-1][caspase inflamatória, parte do inflamassoma, cliva pró-IL-1β/pró-IL-18 e gasdermina D para disparar piroptose] — que faz parte de plataformas chamadas inflamassomas. Quando macrófagos detectam padrões de patógenos (LPS no citosol, flagelina, cristais), o inflamassoma monta-se, ativa caspase-1, e ela faz duas coisas: cliva gasdermina D (cujo fragmento N-terminal vai à membrana e forma poros) e cliva pró-IL-1β e pró-IL-18, gerando citocinas inflamatórias maduras. A célula morre fazendo barulho ao ponto de chamar a resposta imune adaptativa — é o "fogo" da morte inflamatória, daí o nome ("pyro").

A *ferroptose* é químicamente distinta de tudo. Não envolve caspases, RIPK, nem maquinaria de autofagia. Depende de *ferro* intracelular e de peroxidação de lipídios. Quando a enzima GPX4 (glutationa peroxidase 4) está inibida ou faltam glutationas, peróxidos lipídicos acumulam-se na membrana. O ferro acelera reações de Fenton que propagam radicais lipídicos. A membrana se desorganiza, a célula morre. Drogas como erastina disparam ferroptose seletivamente em células tumorais com alta demanda de glutationa — interesse oncológico crescente.

A *NETose* é específica de neutrófilos. Em vez de morrer silenciosa, o neutrófilo extrude redes de cromatina decoradas com enzimas antimicrobianas — as #sigla("NET", [_neutrophil extracellular trap_ — rede extracelular de cromatina extrudada por neutrófilo, decorada com elastase, MPO e outras enzimas]). As NETs prendem bactérias extracelulares como teia de aranha. O neutrófilo morre nesse processo, mas só ele faz isso — outras células imunes morrem por apoptose ou necroptose.

A *parthanatos* depende de hiperativação da #sigla("PARP-1", [_poly(ADP-ribose) polymerase 1_ — enzima que detecta quebras de DNA e adiciona cadeias de poli-ADP-ribose; sua hiperativação consome NAD⁺ e ATP]) após dano massivo ao DNA. PARP-1 consome NAD⁺ em quantidades catastróficas, o que leva à exaustão de ATP e a uma morte por falência energética, mas com sinalização específica que distingue de necrose acidental.

#figura-nebli(
  "/figuras/morte-celular/slide-21.png",
  largura: 60%,
  legenda: [A roda da RCD revisitada agora com nomes molecularmente conhecidos. Cada raio é uma via dedicada com proteínas-chave próprias, executando morte em contextos celulares específicos. A apoptose (intrínseca e extrínseca à esquerda) domina, mas as outras rotas existem porque a apoptose é vulnerável a sabotagem viral e nem sempre é o desfecho ideal.],
)

#subtopico("3.4 — Integração clínica: por que tudo isso importa")

Voltando ao quadro da PARTE I. Doenças por excesso de morte celular (degenerativas, isquêmicas, AIDS) e doenças por déficit (câncer, autoimunes) são, hoje, alvos farmacológicos diretos da maquinaria de morte regulada. Drogas como venetoclax ativam apoptose em leucemias dependentes de Bcl-2; necrostatinas inibem necroptose em isquemia-reperfusão; inhibidores de ferroptose protegem células beta pancreáticas em diabetes tipo 1. A próxima geração de oncoterapia incluirá indutores de morte imunogênica deliberada, que matam células tumorais de forma a alertar o sistema imune.

#clinica-box(
  "p53, o guardião do genoma — e por que mutações dele dominam o câncer",
  [Cerca de 50% dos cânceres humanos têm mutações no gene #termo-nota[TP53][gene que codifica p53; mutado em ~50% dos cânceres humanos, com perda da função de pausar ciclo ou induzir apoptose após dano de DNA]. Em condições normais, p53 é uma proteína de meia-vida curta, degradada rapidamente por MDM2. Quando há dano de DNA, p53 é fosforilada por proteína-cinases (ATM, ATR), escapa da degradação, acumula-se e age como fator de transcrição. Aciona dois grupos de genes: o gene p21 (que inibe Cdks e para o ciclo em G1, dando tempo para reparo) e os genes Puma/Noxa/Bax (que disparam a via intrínseca da apoptose se o dano for grande demais). Sem p53 funcional, células com DNA quebrado continuam dividindo, acumulam mais mutações, e progridem para câncer. Não é coincidência que a perda de p53 esteja associada a quase todos os tumores agressivos — sem ela, o sistema de qualidade celular fica cego e desarmado.],
)

#figura-nebli(
  "/figuras/morte-celular/slide-61.png",
  largura: 65%,
  legenda: [O eixo p53→p21→parada do ciclo (à direita) e o eixo p53→Bcl-2/caspases→apoptose (à esquerda). Mesma proteína sentinela, duas saídas dependendo da gravidade do dano. Ponto de verificação G1 é onde a célula decide se vai reparar ou morrer.],
)

#conclusao-box[
  Morte celular é trabalho. Não é o que sobra quando a vida termina — é um processo ativo, controlado, gastador de energia, com vias dedicadas que evoluíram tão minuciosamente quanto as vias de proliferação. A apoptose, com sua morfologia limpa, suas duas rotas (extrínseca por receptores, intrínseca por mitocôndria), sua maquinaria de caspases organizada em cascata e sua família Bcl-2 decidindo quando MOMP ocorre, é a forma dominante. Ao redor dela orbitam alternativas que existem por razões evolutivas claras: autofagia que recicla em fome e mata em excesso; necroptose que dispara quando patógenos bloqueiam apoptose; piroptose que alerta o sistema imune contra invasores intracelulares; ferroptose que opera quimicamente sem caspases; parthanatos que sucumbe à exaustão metabólica do reparo de DNA hiperativado.

  A clínica está toda aqui. Quase toda doença degenerativa é morte de mais; quase todo câncer é morte de menos. Os medicamentos do futuro próximo manipulam diretamente esses programas — não é mais ficção dizer que oncologia se torna engenharia de morte celular. Entender estes mecanismos não é, portanto, aula avulsa de biologia celular: é a moldura sobre a qual a próxima geração de terapias está sendo construída.
]
