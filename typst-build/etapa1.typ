#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
A inflamação aguda existe para resolver um problema de logística: os recursos que combatem um agressor e limpam um tecido morto — proteínas plasmáticas e leucócitos — circulam dentro do vaso, e o dano acontece fora dele. Toda a sequência que este resumo percorre é a solução desse transporte, e cada sinal clínico é a leitura externa de uma etapa dele.

A *PARTE I* cobre o gatilho: como a célula percebe o dano e o que muda no calibre e no fluxo do vaso. A *PARTE II* acompanha o que sai do vaso — primeiro o líquido com proteína, depois as células, pela cascata de adesão que faz o leucócito parar e atravessar a parede. A *PARTE III* trata do que acontece quando ele chega: como mata, como a resposta se desliga, e por que o resultado assume formas morfológicas distintas conforme o agente e o tecido.
]

#parte-title("PARTE I — O gatilho: reconhecer o dano e abrir o vaso", primeira: true)

#subtopico("1.1 — O que a inflamação aguda faz e por que produz cinco sinais")

Inflamação aguda é a resposta imediata do tecido vascularizado a um agente agressor, e o seu objetivo é restabelecer a homeostase: diluir o agente, destruí-lo, remover o tecido morto e preparar o reparo. A resposta é estereotipada — vasodilatação, aumento de permeabilidade e recrutamento de leucócitos, nessa ordem — porque o repertório de receptores e mediadores que a dispara é limitado e comum a agressores muito diferentes.

Os cinco #termo-nota[sinais flogísticos][os sinais cardinais da inflamação: calor, rubor, tumor, dor e perda funcional — os quatro primeiros descritos por Celso, o quinto acrescentado depois] não são uma descrição decorativa: cada um é a manifestação externa de um evento vascular preciso. O *calor* e o *rubor* vêm da mesma causa, a hiperemia — a arteríola dilata, mais sangue arterial ocupa o leito capilar, e esse sangue traz consigo a temperatura central e a cor da hemoglobina oxigenada. O *tumor* é o edema inflamatório, líquido rico em proteína acumulado no interstício depois que a parede da vênula deixou de reter o plasma. A *dor* tem dois componentes somados: a bradicinina e a prostaglandina E₂ sensibilizam quimicamente a terminação nociceptiva, baixando o limiar de disparo, e o volume acumulado distende mecanicamente o tecido. A *perda funcional* é a consequência da dor com a distensão — o segmento inflamado é poupado voluntariamente e mecanicamente limitado.

Os desencadeantes são cinco, e nem todos envolvem micróbio. As *infecções* disparam a resposta por moléculas próprias do agente. A *necrose tecidual* de qualquer origem — isquemia, trauma, agente físico — dispara sem qualquer micróbio, e é por isso que um infarto do miocárdio produz febre, leucocitose e infiltrado neutrofílico numa área estéril. O *corpo estranho* mantém a resposta porque não pode ser digerido nem removido. As *reações de hipersensibilidade* usam a maquinaria inflamatória contra antígeno inócuo ou contra o próprio tecido. Os *agentes químicos e físicos* — ácido, base, calor, radiação, frio — lesam diretamente a célula e a resposta parte dos restos que ela libera.

Duas consequências desse desenho atravessam a aula: a inflamação responde *ao dano*, não à identidade do agressor, e a mesma resposta que protege lesa — enzimas e oxidantes não distinguem a matriz do hospedeiro.

#subtopico("1.2 — Reconhecer o dano: padrões moleculares, receptores e inflamassoma")

Antes de qualquer alteração de calibre, alguma célula precisa perceber que há um problema. Quem faz esse trabalho no tecido são os *macrófagos residentes*, os *mastócitos* e as próprias células epiteliais e endoteliais, e o que elas leem são duas classes de moléculas. Os #sigla("PAMP", [padrões moleculares associados a patógenos — estruturas conservadas e exclusivas de micro-organismos, como lipopolissacarídeo e peptidoglicano]) são estruturas que só existem em micro-organismos e que não mudam, porque o agente depende delas para viver. Os #sigla("DAMP", [padrões moleculares associados a dano — moléculas normalmente intracelulares que, no interstício, sinalizam morte celular]) são moléculas do próprio hospedeiro que deveriam estar dentro da célula — trifosfato de adenosina, ácido úrico, DNA — e cuja presença no interstício só é possível se uma membrana se rompeu. É o DAMP que explica a inflamação da necrose estéril.

Os receptores que leem esses padrões ocupam três compartimentos, e a distribuição tem lógica. Os #sigla("TLR", [receptores do tipo Toll — família de receptores de reconhecimento de padrão, presentes na membrana plasmática e na membrana endossomal]) de superfície detectam o que está do lado de fora: lipídeo da parede bacteriana, lido em cooperação com a proteína CD14, e polissacarídeo fúngico, lido também por lectinas. Os TLR endossomais detectam ácido nucleico microbiano — DNA bacteriano, RNA viral — que só chega ali depois da internalização da partícula. E receptores citosólicos vigiam o interior da própria célula. Todos convergem para o fator de transcrição nuclear kappa B, que aumenta a expressão de moléculas de adesão no endotélio e a produção de #sigla("TNF", [fator de necrose tumoral — citocina de macrófago ativado, responsável por ativação endotelial e por efeitos sistêmicos]) e interleucina-1.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-05.png",
  largura: 52%,
  legenda: [À esquerda, os três compartimentos de reconhecimento. À direita, o inflamassoma: o gene da pró-interleucina-1β é transcrito por um sinal, e a caspase-1 que a cliva é ativada por outro.])

O #termo-nota[inflamassoma][complexo proteico citosólico que ativa a caspase-1; o mais estudado tem o sensor NLRP3] é o segundo braço, e ele funciona com *dois sinais independentes* — o detalhe que explica por que a interleucina-1β é uma citocina tão bem controlada. O primeiro sinal, vindo de um TLR, apenas transcreve o gene e acumula a forma inativa, a pró-interleucina-1β. O segundo sinal monta o complexo #sigla("NLRP3", [sensor citosólico da família NOD, que monta o inflamassoma quando detecta perturbação da homeostase celular]) e ativa a caspase-1, que cliva a pró-forma na citocina madura. O que aciona esse segundo sinal não é a identidade do agente, e sim um sinal de perturbação: efluxo de potássio, espécies reativas de oxigênio, trifosfato de adenosina extracelular ou cristais fagocitados que rompem a membrana do lisossomo. É por essa via que o cristal de urato monossódico produz a crise aguda de gota e o cristal de colesterol alimenta a inflamação da placa aterosclerótica — sem micróbio nenhum.

#mini-resumo[O tecido não reconhece o agressor, reconhece dano. PAMP e DAMP ativam receptores em três compartimentos → fator nuclear kappa B produz TNF e interleucina-1 → endotélio ativado. O inflamassoma exige um segundo sinal de perturbação para liberar a interleucina-1β madura.]

#subtopico("1.3 — Fluxo, calibre e estase — e os mediadores que dilatam")

Com o endotélio já ativado pelas citocinas do subtópico anterior, a primeira alteração mensurável é hemodinâmica. Há uma vasoconstrição arteriolar fugaz, de segundos, seguida da *vasodilatação arteriolar* que domina o quadro: a arteríola relaxa, leitos capilares antes fechados se abrem, e o fluxo local aumenta várias vezes. Calor e rubor nascem aqui. Os mediadores dessa fase são a *histamina*, pré-formada em grânulos de mastócito, basófilo e plaqueta — por isso age em segundos —, o #sigla("NO", [óxido nítrico — gás produzido pelo endotélio e por macrófagos; relaxa a musculatura lisa vascular e também participa da morte de micróbios]) produzido pelo endotélio, e as prostaglandinas.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-04.png",
  largura: 58%,
  legenda: [O mesmo leito, normal e inflamado: a arteríola dilata e o leito capilar se expande (1), a proteína plasmática escapa pela vênula e leva água consigo (2), e o neutrófilo emigra (3). Os três números são a espinha das PARTES I e II.])

As prostaglandinas e os leucotrienos vêm de uma origem comum, e essa origem é o ponto em que a farmacologia entra no mecanismo. A *fosfolipase A₂* libera o ácido araquidônico do fosfolipídeo de membrana; a partir dele, a *cicloxigenase* gera prostaglandinas e tromboxano, e a *5-lipoxigenase* gera leucotrienos. Os produtos têm efeitos distintos e por vezes opostos: a prostaciclina e a prostaglandina E₂ causam vasodilatação e aumentam a permeabilidade, o tromboxano A₂ faz vasoconstrição e agrega plaquetas, o leucotrieno B₄ é quimiotático, e os leucotrienos C₄, D₄ e E₄ contraem músculo liso e abrem a vênula.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-13.png",
  largura: 60%,
  legenda: [Duas classes de fármaco, dois pontos de bloqueio. O corticoide inibe a fosfolipase e derruba os dois ramos; o anti-inflamatório não esteroidal inibe a cicloxigenase e deixa a lipoxigenase intacta — o que explica o broncoespasmo por leucotrienos em pacientes sensíveis.])

O aumento de fluxo é transitório. Assim que a vênula começa a deixar sair líquido rico em proteína, o sangue retido fica mais concentrado em hemácias, a viscosidade sobe e a velocidade cai: instala-se a *estase*, com vasos dilatados e repletos de hemácias empacotadas — o que o corte histológico mostra como congestão vascular. A estase não é falha do sistema. Em fluxo rápido, o perfil de velocidade mantém as células maiores no eixo central da corrente; quando a velocidade cai, os leucócitos deixam a coluna axial e passam a encostar no endotélio. É a condição física de tudo o que a PARTE II descreve.

#figura-lateral("/figuras/pat-07-inflamacao-aguda/slide-14.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O pulmão normal, em A, tem septos finos com poucos núcleos e capilares vazios. Em B, o mesmo septo está alargado e os capilares aparecem repletos de hemácias empilhadas: é a estase, e o achado é o substrato microscópico do rubor observado a olho nu.],
  legenda: [Congestão vascular e estase.])

#confusao-prevista(
  titulo: "Vasodilatação e aumento de permeabilidade não são o mesmo evento",
  aluno_acha: [o aluno costuma tratar "abrir o vaso" como um fenômeno único, que ao mesmo tempo traz mais sangue e deixa sair líquido.],
  mecanismo: [são eventos separados, em vasos diferentes, com mediadores parcialmente distintos. A *dilatação* é relaxamento de músculo liso *arteriolar* e produz calor e rubor. O *aumento de permeabilidade* é abertura de junções entre células endoteliais da *vênula pós-capilar* e produz edema. Um pode existir sem o outro: o rubor da vasodilatação neurogênica não vem acompanhado de exsudato.],
)

#parte-title("PARTE II — Do plasma às células: exsudato e recrutamento")

#subtopico("2.1 — Os quatro mecanismos de aumento de permeabilidade")

A saída de proteína plasmática para o interstício depende de abrir uma barreira que, em condições normais, retém tudo o que for maior que a albumina. Existem quatro modos de abri-la, e eles diferem no vaso acometido, na velocidade de instalação e na duração — um trio de características que permite deduzir o mecanismo a partir da história clínica.

A *contração endotelial* é o mecanismo mais comum. Histamina, bradicinina e leucotrienos ligam-se a receptores da célula endotelial, que reorganiza o citoesqueleto e se retrai, alargando o espaço interendotelial. Ocorre quase exclusivamente na #termo-nota[vênula pós-capilar][segmento venoso imediatamente após o leito capilar; é o vaso onde ocorrem a abertura de junções e a saída dos leucócitos], é imediata e dura de quinze a trinta minutos — a resposta transitória imediata. Há uma variante retardada e prolongada, que começa horas depois e persiste por dias, típica da lesão térmica leve e da radiação ultravioleta, e que explica a bolha da queimadura solar aparecer no dia seguinte.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-09.png",
  largura: 48%,
  legenda: [Em B, células íntegras que se afastam; em C, células mortas que deixam um buraco. A distinção entre retração reversível e necrose da parede decide se o extravasamento dura minutos ou dias.])

A *lesão endotelial direta* é necrose da própria parede. Queimadura extensa, toxina microbiana e agentes químicos matam a célula endotelial, que se desprende e deixa uma falha aberta. Acomete arteríolas, capilares e vênulas, é imediata e persiste por horas a dias, até que a regeneração endotelial feche a brecha — é a resposta sustentada imediata.

A *lesão mediada por leucócitos* é tardia, e depende de um evento que só ocorre depois que o recrutamento aconteceu. O neutrófilo aderido ao endotélio libera enzimas lisossomais e espécies reativas de oxigênio no espaço entre ele e a parede, e esse conteúdo lesa a célula endotelial abaixo. Predomina em vênulas e nos capilares pulmonares, onde a densidade de leucócitos aderidos é alta, e é um dos mecanismos que ligam a inflamação intensa à lesão do próprio hospedeiro.

A *transcitose* aumenta o transporte vesicular através do citoplasma endotelial, por canais formados pela fusão de vesículas. É induzida sobretudo pelo fator de crescimento endotelial vascular e responde por parte do extravasamento sem alargamento de junção — o líquido atravessa a célula, não passa entre as células.

#mini-resumo[Contração endotelial: vênula, imediata, minutos, reversível. Lesão direta: qualquer vaso, imediata, dias, necrose. Lesão por leucócito: vênula e capilar pulmonar, tardia. Transcitose: transporte através da célula, dependente do fator de crescimento endotelial vascular.]

#subtopico("2.2 — Exsudato × transudato e a rota linfática")

Nem todo líquido acumulado no interstício veio de uma barreira aberta, e essa é a distinção que organiza a leitura de qualquer derrame. No capilar normal, a pressão hidrostática empurra líquido para fora e a pressão coloidosmótica exercida pelas proteínas do plasma o puxa de volta, com pequeno excedente drenado pelo linfático. Quando apenas essas forças se desequilibram — pressão hidrostática alta por obstrução venosa, ou pressão coloidosmótica baixa por perda ou falta de síntese de albumina — o endotélio permanece íntegro e o que sai é um *ultrafiltrado*: o #termo-nota[transudato][líquido de baixa concentração proteica, resultante de desequilíbrio de forças com barreira endotelial íntegra].

Quando a barreira é aberta pelos mecanismos do subtópico anterior, sai plasma quase completo, com as proteínas grandes que a permeabilidade normal retinha e com as células que a acompanham: é o *exsudato*. A composição, por isso, não é um detalhe laboratorial: ela identifica qual mecanismo operou.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-06.png",
  largura: 48%,
  legenda: [As três situações lado a lado. Em B a seta hidrostática cresce e o endotélio segue fechado; em C o espaço interendotelial se abre e a proteína sai junto com a água.])

#table(
  columns: (auto, 1fr, 1fr),
  inset: 7pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Característica]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Exsudato]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Transudato]],
  ),
  [Concentração de proteínas], [Elevada, acima de 3 g/dL], [Normal, abaixo de 3 g/dL],
  [Densidade], [Acima de 1020], [Abaixo de 1020],
  [Células], [Frequentes, abundantes], [Ausentes ou raras],
  [#sigla("DHL", [desidrogenase láctica — enzima citoplasmática abundante; no líquido, sua concentração reflete quantidade de células e destruição celular])], [Acima de 200], [Abaixo de 200],
  [Mecanismo que o gerou], [Permeabilidade aumentada, barreira aberta], [Desequilíbrio de forças, barreira íntegra],
)

Os quatro critérios não são independentes: a densidade acompanha a concentração de proteína, e a desidrogenase láctica acompanha a quantidade de células e a destruição celular no líquido. Todos medem, por caminhos diferentes, o quanto do conteúdo do vaso passou para fora.

A proteína extravasada tem uma segunda consequência mecânica. Ao chegar ao interstício, ela eleva a pressão coloidosmótica local e reduz a diferença que puxava o líquido de volta, o que faz o edema inflamatório se autossustentar enquanto a permeabilidade estiver aumentada. Entre essas proteínas vem o fibrinogênio, que no interstício é convertido em fibrina — o material que define um dos padrões morfológicos da PARTE III.

O excedente é escoado pelo *sistema linfático*, que responde de forma ativa: os vasos proliferam na área inflamada e aumentam a drenagem, carregando junto agente, restos e antígeno. Quando o próprio vaso se inflama, surgem as estrias avermelhadas da linfangite; quando o linfonodo de drenagem responde com hiperplasia de folículos e seios, surge a linfadenite reacional, aumentada e dolorosa. A linfadenopatia de uma infecção local não é sinal obrigatório de disseminação — é o funcionamento da via que leva o antígeno ao órgão onde a resposta adaptativa é montada.

#atencao-box("A inversão que muda o diagnóstico", [
Trocar exsudato por transudato inverte a causa do quadro. Proteína acima de 3 g/dL, densidade acima de 1020 e células abundantes indicam *barreira aberta* — processo inflamatório, infeccioso ou neoplásico *local*. Proteína baixa, densidade baixa e poucas células indicam *barreira fechada* com forças desequilibradas — insuficiência cardíaca, cirrose, síndrome nefrótica, condições *sistêmicas*. O mesmo derrame pleural, com a mesma aparência macroscópica, aponta para investigações opostas conforme a dosagem.
])

#subtopico("2.3 — Marginação, rolamento, adesão e diapedese")

Segurar um objeto que passa em alta velocidade exige dois movimentos, não um: primeiro um contato frouxo que freia sem prender, depois um encaixe firme que imobiliza. O recrutamento leucocitário resolve o mesmo problema físico com duas famílias de moléculas de adesão, e essa é a razão de existirem etapas distintas onde poderia haver uma só.

A *marginação* é o passo hemodinâmico já descrito: com a estase, os leucócitos abandonam a coluna central e se acumulam junto ao endotélio. Não há molécula envolvida — é redistribuição por queda de velocidade.

O *rolamento* é o primeiro contato molecular. O leucócito exibe constitutivamente um glicoproteína modificada, o #termo-nota[Sialyl-Lewis X][oligossacarídeo sialilado e fucosilado presente em glicoproteínas de superfície do leucócito; é o ligante das selectinas], e o endotélio ativado passa a expor selectinas que o reconhecem. A ligação é de baixa afinidade e se desfaz com facilidade: forma-se na frente, rompe-se atrás, e o leucócito rola pela superfície em vez de parar. As duas selectinas endoteliais têm tempos diferentes. A P-selectina já existe pré-formada em grânulos citoplasmáticos e chega à membrana em minutos, mobilizada por histamina e trombina. A E-selectina precisa ser transcrita, e por isso só aparece horas depois, sob estímulo de TNF e interleucina-1 — as citocinas produzidas no reconhecimento da PARTE I.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-17.png",
  largura: 66%,
  legenda: [A sequência inteira em uma linha. Repare que a quimiocina não move o leucócito nesta etapa: ela muda a conformação da integrina, e é essa mudança que converte rolamento em parada.])

A *adesão firme* depende de uma mudança de estado. As #termo-nota[integrinas][heterodímeros de superfície do leucócito que alternam entre conformação de baixa e de alta afinidade; ligam-se a moléculas de adesão da superfamília das imunoglobulinas no endotélio] estão na superfície do leucócito em conformação de baixa afinidade e não seguram nada. As quimiocinas produzidas no foco são apresentadas ancoradas em proteoglicanos na superfície endotelial e, ao ligar o seu receptor no leucócito que rola, disparam a mudança conformacional para o estado de alta afinidade. No endotélio, paralelamente, TNF e interleucina-1 induziram os ligantes correspondentes — a #sigla("ICAM-1", [molécula de adesão intercelular 1 — ligante endotelial das integrinas da família β2, entre elas LFA-1 e Mac-1]) e a #sigla("VCAM-1", [molécula de adesão de célula vascular 1 — ligante endotelial da integrina VLA-4]). Integrina ativada mais ligante expresso resultam em aderência firme, e o leucócito para e se espalha sobre a superfície.

A *transmigração*, ou #termo-nota[diapedese][passagem do leucócito através da parede vascular, entre células endoteliais e depois através da membrana basal], ocorre nas junções interendoteliais, guiada por moléculas presentes nos dois lados do contato, das quais a mais conhecida é a #sigla("PECAM-1", [molécula de adesão de plaqueta e célula endotelial 1, também chamada CD31 — presente no leucócito e na junção endotelial]). O leucócito reorganiza o citoesqueleto e se insinua pela junção, favorecido pelo próprio aumento de permeabilidade; ao encontrar a membrana basal, secreta metaloproteinases que digerem o colágeno IV e alcança o interstício.

#clinica-box("Deficiência de adesão leucocitária: o mecanismo provado pela falta", [
Duas doenças genéticas raras confirmam a arquitetura de duas afinidades. Na deficiência de adesão leucocitária do tipo 1, o defeito está na cadeia β2 comum às integrinas do leucócito: o rolamento acontece normalmente, mas a adesão firme não, e o leucócito nunca sai do vaso. Na do tipo 2, o defeito está na fucosilação que constrói o Sialyl-Lewis X: falha o rolamento, e o leucócito sequer desacelera.

O fenótipo é o mesmo nas duas e é contraintuitivo: infecções bacterianas graves e de repetição *sem formação de pus*, cicatrização lenta, queda tardia do coto umbilical — e *neutrofilia acentuada no sangue*, porque os neutrófilos circulam e não chegam ao tecido. O pus é feito de neutrófilos que emigraram.
])

#subtopico("2.4 — Quimiotaxia e as citocinas que comandam o recrutamento")

Atravessada a parede, o leucócito precisa encontrar o alvo dentro de um interstício de estrutura complexa. A *quimiotaxia* é a locomoção orientada por um gradiente de concentração: o leucócito detecta diferenças de concentração entre a frente e a traseira da própria célula, polimeriza actina no polo voltado para a concentração maior, emite um pseudópode nessa direção e traciona o corpo celular atrás dele. O movimento é progressivo, não aleatório.

Quatro classes de agentes quimiotáticos operam no foco. Os *produtos bacterianos*, sobretudo peptídeos que começam por N-formil-metionina — assinatura da síntese proteica bacteriana, que o receptor do leucócito reconhece como sinal de que há micro-organismo. Os *fragmentos do complemento*, C3a e C5a, gerados pela cascata ativada na superfície do agente; o C5a é o mais potente e, além de atrair, ativa a via da lipoxigenase no próprio leucócito. O *leucotrieno B₄*, produzido pelos leucócitos já presentes, que amplifica o recrutamento a partir de dentro. E as *quimiocinas*, das quais a #sigla("IL-8", [interleucina-8 — quimiocina produzida por macrófagos ativados e pelo endotélio; recruta e ativa neutrófilos]) é o exemplo canônico, produzidas por macrófagos e endotélio, e não pelo neutrófilo que elas atraem.

Acima dessa camada estão as duas citocinas que comandam o processo inteiro. O TNF e a interleucina-1 são produzidos principalmente por macrófagos ativados, com contribuição de mastócitos, linfócitos T e do próprio endotélio, e têm três alvos locais. No *endotélio*, aumentam a expressão de moléculas de adesão, induzem a produção de quimiocinas e deslocam o equilíbrio hemostático para o lado procoagulante, reduzindo a atividade anticoagulante da superfície — é o que explica a trombose de pequenos vasos em áreas de inflamação intensa. Nos *leucócitos*, promovem ativação e produção de mais citocinas. Nos *fibroblastos*, estimulam proliferação e síntese de colágeno, o que já é a preparação do reparo.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-32.png",
  largura: 50%,
  legenda: [O mesmo par de citocinas responde por três destinos: inflamação local, reparo e manifestações sistêmicas. A dose e a extensão da produção decidem qual coluna predomina.])

Quando essas citocinas alcançam a circulação, aparecem os *efeitos sistêmicos* — a resposta de fase aguda. No hipotálamo, elevam a produção de prostaglandina E₂ e com ela o ponto de ajuste térmico: é a *febre*. Na medula óssea, aceleram a liberação de neutrófilos, e o hemograma mostra *leucocitose com desvio à esquerda*. No fígado, aumentam a síntese das *proteínas de fase aguda* — proteína C reativa, fibrinogênio, amiloide sérico A —, e o fibrinogênio elevado é o que acelera a velocidade de hemossedimentação. Somam-se anorexia e sonolência. Em produção maciça, como na sepse por bactérias gram-negativas, o TNF derruba a resistência vascular sistêmica e a contratilidade miocárdica e ativa a coagulação de forma difusa: o choque séptico é a mesma resposta útil, em escala destrutiva.

#parte-title("PARTE III — Executar, desligar e a marca que fica")

#subtopico("3.1 — Fagocitose, burst oxidativo e o dano que sobra no tecido")

Chegar ao alvo é metade do trabalho. A fagocitose se organiza em três passos — reconhecimento e ligação, englobamento, e morte com degradação —, e a eficiência de cada um depende do quanto o alvo foi previamente marcado.

O reconhecimento direto usa receptores que leem estruturas do micro-organismo — o receptor de manose, que liga açúcares terminais da parede microbiana ausentes nas glicoproteínas do hospedeiro, e os receptores scavenger — e é ineficiente. A eficiência vem da #termo-nota[opsonização][revestimento do alvo por moléculas que o fagócito reconhece com alta afinidade, aumentando muito a fagocitose]: a imunoglobulina G ligada ao antígeno é reconhecida pelo receptor para a porção Fc, e o C3b depositado pelo complemento, pelos receptores de complemento, entre eles a integrina Mac-1. A opsonina funciona como alça — sem ela o fagócito escorrega no alvo.

No *englobamento*, a membrana do fagócito flui em torno da partícula até se fechar, formando um *fagossomo* que se destaca para o citoplasma. O fagossomo funde-se com o lisossomo e forma o *fagolisossomo*, e é essa fusão que entrega ao compartimento as enzimas ácidas que farão a degradação.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-33.png",
  largura: 58%,
  legenda: [Os três passos e o destaque do canto: a fagócito-oxidase montada na membrana do fagossomo despeja espécies reativas dentro do compartimento, e não no citoplasma.])

A morte do micro-organismo é feita principalmente por espécies reativas de oxigênio, geradas numa sequência que vale conhecer por etapas nomeadas. A #sigla("NADPH", [fosfato de dinucleotídeo de nicotinamida e adenina reduzido — doador de elétrons da fagócito-oxidase]) oxidase, também chamada fagócito-oxidase, monta-se na membrana do fagossomo e transfere elétrons para o oxigênio molecular, produzindo *ânion superóxido* — o consumo abrupto de oxigênio nesse momento é o #termo-nota[burst respiratório][aumento súbito do consumo de oxigênio pelo fagócito ativado, destinado à produção de espécies reativas, e não à respiração mitocondrial]. O superóxido é dismutado a *peróxido de hidrogênio*, e o peróxido, na presença de cloreto, é convertido pela *mieloperoxidase* dos grânulos azurófilos do neutrófilo em *hipoclorito*, o agente antimicrobiano mais potente do sistema. Em paralelo, a sintase induzível de óxido nítrico gera NO a partir da arginina, e a reação do NO com o superóxido produz peroxinitrito, também microbicida.

Há ainda a morte independente de oxigênio, por *defensinas*, *lisozima*, *lactoferrina* e *elastase* dos grânulos, e a extrusão de redes de cromatina que aprisionam bactérias fora da célula, ao custo da vida do neutrófilo.

O mesmo arsenal explica a lesão do hospedeiro. Quando o alvo é grande demais para ser englobado — um complexo imune depositado numa membrana basal — o leucócito descarrega os grânulos no meio extracelular, na fagocitose frustrada; e mesmo na fagocitose bem-sucedida há regurgitação de enzimas antes do fechamento do fagossomo. Enzima proteolítica e oxidante no interstício degradam matriz e matam células vizinhas — o dano que o patologista descreve é, em boa parte, obra do efetor.

#clinica-box("Doença granulomatosa crônica", [
O defeito genético em uma das subunidades da NADPH oxidase impede a produção de superóxido. O neutrófilo reconhece, engloba e forma o fagolisossomo normalmente — só não consegue matar o que engoliu por via oxidativa. O resultado é infecção de repetição por micro-organismos *catalase-positivos*, como o estafilococo áureo e algumas espécies de aspergilo: micro-organismos catalase-negativos produzem o próprio peróxido de hidrogênio e acabam fornecendo ao fagócito defeituoso o substrato que lhe falta, enquanto os catalase-positivos degradam esse peróxido e sobrevivem dentro da célula.

Como a bactéria persiste viva no interior do macrófago, a resposta migra para o padrão crônico e organiza granulomas — daí o nome da doença.
])

#subtopico("3.2 — A cinética dos leucócitos, o desligamento e os quatro desfechos")

O infiltrado inflamatório muda de composição com o tempo, e a curva é tão previsível que a própria composição do infiltrado data o processo. O *edema* aparece primeiro, em horas. O *neutrófilo* domina nas primeiras 24 horas e desaparece entre 24 e 48. O *monócito*, que no tecido se diferencia em macrófago, assume a partir de 48 horas e permanece por dias.

#figura-lateral("/figuras/pat-07-inflamacao-aguda/slide-29.png",
  lado: "right",
  largura-figura: 45%,
  texto: [Três curvas que não coincidem. O neutrófilo chega antes porque é o leucócito mais abundante do sangue, responde mais rapidamente às selectinas e às quimiocinas e adere primeiro; some porque tem meia-vida de horas no tecido e morre por apoptose. O macrófago chega depois e fica, porque sobrevive dias e recebe estímulo continuado.],
  legenda: [Cinética do infiltrado agudo.])

O desligamento é, em parte, propriedade de projeto: os mediadores saem em rajadas, têm meia-vida curta e são degradados assim que o estímulo cessa — retirado o agente, a cascata perde sustentação em horas. A isso soma-se uma troca dentro da própria via do ácido araquidônico: os leucócitos passam a produzir *lipoxinas*, que inibem adesão e quimiotaxia de neutrófilos, revertendo o sentido do sinal que a mesma via emitia no início.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-36.png",
  largura: 48%,
  legenda: [O monócito recém-chegado escolhe entre dois programas. O ambiente decide: ligantes microbianos e interferon-γ empurram para o lado esquerdo; interleucinas 4 e 13 empurram para o direito.])

O macrófago participa desse controle porque não tem um programa único. Ativado classicamente, por ligantes microbianos e por interferon-γ, ele produz espécies reativas, óxido nítrico e as citocinas que mantêm a inflamação. Ativado por via alternativa, sob interleucinas 4 e 13, ele produz interleucina-10, fator transformador de crescimento beta e arginase, e passa a sustentar reparo e fibrose. A mesma célula, portanto, aparece nos dois lados do processo, e é a composição do ambiente que decide qual programa predomina.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-38.png",
  largura: 56%,
  legenda: [Quatro saídas para o mesmo começo. O que decide é a combinação de três variáveis: agente removido ou persistente, extensão do dano, e capacidade de regeneração do tecido.])

Os desfechos possíveis são quatro. Na *resolução completa*, o agente foi removido, o dano ficou limitado e o tecido tem capacidade regenerativa: o exsudato é digerido e drenado, os neutrófilos apoptóticos são fagocitados pelos macrófagos, os restos necróticos são removidos e a arquitetura volta ao normal. Na *formação de abscesso*, o agente piogênico persiste num foco e a necrose liquefativa se acumula como pus loculado. Na *fibrose*, o dano foi extenso, ou o tecido não regenera, ou o exsudato fibrinoso não foi removido — o material persistente é invadido por fibroblastos e vasos e substituído por tecido conjuntivo denso, com perda funcional definitiva. E na *progressão para inflamação crônica*, o agente não é eliminado e o infiltrado troca de população: mononucleares no lugar de neutrófilos, com angiogênese e fibrose simultâneas ao dano continuado.

#subtopico("3.3 — Padrões morfológicos: o que o patologista vê e por quê")

O padrão morfológico é a forma que a inflamação aguda assume num tecido específico, e ele não é um rótulo arbitrário: cada padrão é consequência previsível de três variáveis — a natureza do agente, a intensidade da resposta e o tecido em que ela ocorre.

A *inflamação serosa* é o extremo pobre do espectro: exsudato de baixa concentração proteica e poucas células, vindo do plasma e da secreção das células mesoteliais, acumulado numa cavidade ou entre camadas de tecido — a bolha da queimadura e o derrame de uma pleurite viral. Nenhum micro-organismo precisa estar no líquido.

A *inflamação fibrinosa* aparece quando a permeabilidade deixa passar moléculas grandes e o *fibrinogênio* extravasado é convertido em fibrina no interstício. É o padrão das superfícies serosas — pericárdio, pleura, peritônio —, onde a fibrina entre as duas folhas gera atrito e, no pericárdio, o aspecto rugoso descrito como pão com manteiga. O destino é dicotômico: dissolvido pela fibrinólise, resolve; persistente, é invadido por fibroblastos e vasos e sofre *organização*, deixando aderências fibrosas permanentes.

A *inflamação supurativa ou purulenta* é definida pela produção de #termo-nota[pus][exsudato composto de neutrófilos, restos celulares liquefeitos e líquido de edema], e é a assinatura dos agentes piogênicos. O *abscesso* é a sua forma localizada: necrose liquefativa central, cercada por neutrófilos preservados e, com o tempo, por uma parede de tecido conjuntivo e vasos que contém a coleção. Essa parede é a razão de o abscesso não resolver só com antibiótico — a droga não alcança concentração no centro avascular e liquefeito, e a resolução exige drenagem.

#figura-nebli("/figuras/pat-07-inflamacao-aguda/slide-41.png",
  largura: 50%,
  legenda: [Macroscopia e microscopia do mesmo padrão: cavidade com conteúdo liquefeito, e o campo microscópico tomado por neutrófilos densamente agrupados sobre tecido destruído.])

O *flegmão* é o oposto do abscesso na mesma família purulenta. Aqui a inflamação é difusa e disseca planos teciduais em vez de se delimitar, e a razão é o agente: micro-organismos que produzem enzimas capazes de degradar a matriz — hialuronidase, que despolimeriza o ácido hialurônico do interstício, e estreptoquinase, que dissolve a barreira de fibrina que conteria o processo — impedem a formação da parede. O mesmo tecido, com um agente que não produz essas enzimas, faria um abscesso.

#figura-lateral("/figuras/pat-07-inflamacao-aguda/slide-40.png",
  lado: "right",
  largura-figura: 42%,
  texto: [Na peça, o subcutâneo não mostra cavidade delimitada, e sim comprometimento contínuo que atravessa planos. No corte, o infiltrado neutrofílico permeia os feixes conjuntivos em vez de se concentrar num foco — a diferença que define o padrão.],
  legenda: [Flegmão.])

A *úlcera* é a perda de continuidade de um epitélio de revestimento, por necrose do tecido inflamado e desprendimento do material necrótico. Ocorre onde uma superfície epitelial exposta perde irrigação ou barreira: mucosa gastrointestinal, pele dos membros inferiores com insuficiência vascular. Na fase aguda a base mostra infiltrado neutrofílico intenso e vasodilatação; na crônica, infiltrado mononuclear e proliferação fibroblástica nas bordas.

#atencao-box("Abscesso e flegmão não são graus do mesmo quadro", [
Os dois são supurativos e podem partir do mesmo agente, mas descrevem arquiteturas opostas com condutas opostas. O *abscesso* é delimitado, tem centro liquefeito e parede — é drenável, e a drenagem é parte do tratamento. O *flegmão* é difuso, disseca planos e não tem parede: não há o que drenar, e a gravidade vem da progressão sem barreira. Quando atinge a fáscia e o subcutâneo com necrose extensa e trombose de pequenos vasos, o quadro é a fascite necrosante, que avança em horas e exige desbridamento cirúrgico amplo.
])

#conclusao-box[
O princípio que atravessa as três PARTES é o de uma resposta única, disparada por reconhecimento de dano e não de agente, cuja finalidade é levar plasma e leucócitos para fora do vaso. Todo o resto é consequência: a arteríola dilata e produz calor e rubor; a vênula abre junções e deixa sair proteína, que produz o edema e leva junto o fibrinogênio; a estase resultante empurra o leucócito contra a parede, onde a cascata de duas afinidades — selectina para capturar, integrina para prender — o retém e o faz atravessar.

O mecanismo nuclear é o par TNF e interleucina-1, produzido no reconhecimento e responsável por quase tudo que vem depois: moléculas de adesão, quimiocinas, endotélio procoagulante, estímulo ao fibroblasto e, ao alcançar a circulação, febre, leucocitose e proteínas de fase aguda — o mesmo eixo que, em produção maciça, sustenta o choque séptico.

Na clínica, a cadeia explica achados que parecem desconexos. A composição do líquido de um derrame diz se a barreira estava aberta ou apenas desequilibrada, e com isso separa investigação local de sistêmica. A ausência de pus numa criança com infecções graves e neutrofilia alta aponta defeito de adesão, não falta de neutrófilo. E o padrão morfológico da biópsia é leitura direta de qual agente atuou sobre qual tecido.

Fica aberto o passo seguinte: quando o agente não é eliminado, o infiltrado troca de população e a angiogênese e a fibrose passam a ocorrer junto ao dano continuado — a arquitetura da inflamação crônica, cuja forma mais organizada é o granuloma.
]
