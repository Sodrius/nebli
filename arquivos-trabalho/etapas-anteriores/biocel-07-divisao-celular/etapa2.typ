#import "../typst-template/nebli_v2_apostila.typ": *

// etapa2.typ — Hemoglobina, 30 questões objetivas (v3 — helper questao novo)

// ====================== CONSOLIDAÇÃO (Q01-Q10) ======================

#questao("01", "consolidacao",
  [Sobre a composição estrutural da hemoglobina humana adulta normal
   (HbA), é correto afirmar que:],
  ("A", [é uma proteína monomérica formada por uma única cadeia globina
    ligada a um grupo prostético heme com ferro no estado ferroso, o
    que basta para garantir a curva sigmoide característica.]),
  ("B", [é tetramérica, composta por duas cadeias α e duas cadeias β,
    cada uma carregando um grupo heme com ferro no estado ferroso —
    arquitetura que sustenta a cooperatividade entre subunidades.]),
  ("C", [é trimérica, formada por uma cadeia α e duas cadeias β; o
    grupo heme contém ferro no estado férrico Fe³⁺ para estabilizar
    a ligação covalente reversível com o O₂.]),
  ("D", [é dimérica, composta por duas cadeias α idênticas, com um
    único grupo heme central que coordena uma molécula de O₂ por
    tetrâmero funcional na circulação humana.]),
  ("E", [é tetramérica, formada por quatro cadeias α iguais; o ferro
    do heme está no estado férrico, e cada molécula transporta até oito
    moléculas de O₂ por ciclo respiratório completo.]))

#questao("02", "consolidacao",
  [A diferença funcional central entre mioglobina e hemoglobina, que
   torna a primeira armazenadora e a segunda transportadora, está em:],
  ("A", [a mioglobina é tetramérica e cooperativa, enquanto a
    hemoglobina é monomérica e tem afinidade constante ao longo de
    toda a faixa de pressão parcial de oxigênio.]),
  ("B", [a mioglobina liga O₂ pelo ferro férrico e a hemoglobina pelo
    ferro ferroso, o que faz a primeira ter curva sigmoide e a
    segunda hiperbólica em condições fisiológicas.]),
  ("C", [as duas têm a mesma curva e a mesma afinidade pelo O₂; o
    que muda é apenas a localização tecidual e a abundância
    relativa em diferentes compartimentos do organismo adulto.]),
  ("D", [a mioglobina é monomérica e tem alta afinidade constante,
    útil para armazenar O₂ no músculo; a hemoglobina é tetramérica
    e cooperativa, com afinidade ajustável entre pulmão e tecido.]),
  ("E", [a mioglobina tem dois sítios de ligação e a hemoglobina
    tem apenas um por tetrâmero, e essa diferença é o que explica
    a entrega tecidual diferencial entre as duas proteínas.]))

#questao("03", "consolidacao",
  [Considerando a definição de constante de dissociação (K#sub[d]) e
   sua relação com a afinidade entre proteína e ligante, é correto
   afirmar que:],
  ("A", [K#sub[d] alto significa que o complexo proteína-ligante está
    favorecido no equilíbrio, e portanto a afinidade entre as duas
    moléculas é alta no sistema considerado.]),
  ("B", [K#sub[d] baixo indica equilíbrio favorável ao complexo
    proteína-ligante, e portanto afinidade alta; K#sub[d] alto indica
    o inverso, equilíbrio favorável aos reagentes separados.]),
  ("C", [K#sub[d] não depende da concentração de ligante livre, e seu
    valor numérico cresce proporcionalmente à força das ligações
    covalentes formadas entre proteína e substrato.]),
  ("D", [K#sub[d] e K#sub[a] (constante de associação) têm sempre o
    mesmo valor numérico em equilíbrio, porque medem o mesmo evento
    físico em direções complementares no sistema.]),
  ("E", [K#sub[d] alto é equivalente a P#sub[50] baixo na curva de
    dissociação da hemoglobina, e ambos os parâmetros refletem
    afinidade alta pelo oxigênio em sistemas fisiológicos.]))

#questao("04", "consolidacao",
  [A curva de dissociação sigmoide da hemoglobina, em contraste com
   a hiperbólica da mioglobina, é a assinatura visual de qual
   propriedade molecular?],
  ("A", [da maior abundância da hemoglobina em relação à mioglobina
    no organismo adulto, refletindo a diferença de quantidade entre as
    duas proteínas no compartimento intravascular periférico.]),
  ("B", [da presença de um heme adicional na hemoglobina em comparação
    à mioglobina, que permite cooperação entre os hemes no momento
    da ligação do O₂ ao tetrâmero completo.]),
  ("C", [da cooperatividade entre as quatro subunidades — ligar O₂ em
    uma subunidade aumenta a afinidade das outras três, fenômeno
    impossível em proteína monomérica como a mioglobina.]),
  ("D", [da presença de dois tipos de ferro distintos (ferroso e
    férrico) nas diferentes subunidades, que conferem afinidades
    diferenciadas em função da pressão parcial do oxigênio.]),
  ("E", [da diferença de tamanho entre as duas proteínas, que faz a
    hemoglobina ter curva sigmoide por difusão mais lenta do O₂
    através da membrana eritrocitária no transporte.]))

#questao("05", "consolidacao",
  [Sobre os estados conformacionais T (tenso) e R (relaxado) da
   hemoglobina, é correto afirmar que:],
  ("A", [T e R são proteínas distintas, codificadas por genes
    diferentes do cromossomo 11, que se expressam alternadamente em
    função da pressão parcial de oxigênio no plasma do indivíduo.]),
  ("B", [T é a forma exclusiva da desoxiemoglobina e R é a forma
    exclusiva da oxiemoglobina, sem possibilidade de coexistência
    em equilíbrio dinâmico no sangue venoso humano.]),
  ("C", [T tem alta afinidade pelo O₂ e R tem baixa afinidade; a
    transição R→T é desencadeada pela ligação do oxigênio aos hemes
    em pressões parciais elevadas no compartimento alveolar.]),
  ("D", [a transição T→R envolve uma modificação covalente
    irreversível na cadeia β, que só pode ser desfeita pela
    degradação completa da molécula no baço por macrófagos
    fagocíticos.]),
  ("E", [T e R são duas conformações alternativas do mesmo
    tetrâmero em equilíbrio probabilístico; ligação de O₂ favorece R,
    e moduladores como H⁺, CO₂ e BPG favorecem T.]))

#questao("06", "consolidacao",
  [O efeito Bohr, que regula a liberação de O₂ pela hemoglobina nos
   tecidos, ocorre porque:],
  ("A", [íons H⁺ se ligam ao ferro do heme, deslocam o O₂
    diretamente do sítio e estabilizam a hemoglobina no estado R, o
    que aumenta a entrega tecidual em situações de acidose local.]),
  ("B", [íons H⁺ se ligam a resíduos de histidina da globina,
    estabilizam o estado T, baixam a afinidade da hemoglobina pelo
    O₂ e deslocam a curva de dissociação para a direita.]),
  ("C", [o CO₂ se liga covalentemente ao ferro ferroso do heme,
    expulsa o O₂ do sítio e cria uma forma de hemoglobina chamada
    carbohemoglobina, responsável pelo tamponamento sanguíneo.]),
  ("D", [aumento de pH no tecido (alcalose tecidual) baixa a
    afinidade da hemoglobina pelo O₂, deslocando a curva para a
    direita e aumentando a entrega de O₂ em locais alcalóticos.]),
  ("E", [o pH é fisiologicamente irrelevante para a hemoglobina, que
    só responde a mudanças de temperatura e à concentração local de
    bicarbonato no plasma extracelular do tecido em atividade.]))

#questao("07", "consolidacao",
  [O 2,3-bisfosfoglicerato (BPG) modula a afinidade da hemoglobina
   pelo oxigênio porque:],
  ("A", [se liga covalentemente ao ferro ferroso de um dos quatro
    hemes, ocupa o sítio do O₂ e força a hemoglobina a operar com
    apenas três sítios funcionais por molécula no transporte.]),
  ("B", [se liga ao ferro férrico (Fe³⁺) e impede a oxidação
    espontânea da hemoglobina a metahemoglobina, ação essencial para
    a manutenção da capacidade transportadora ao longo do tempo.]),
  ("C", [é produzido no fígado, exportado pelas hemácias e ligado
    irreversivelmente à superfície externa do tetrâmero,
    estabilizando o estado R em condições basais sistêmicas.]),
  ("D", [se aloja em uma cavidade central entre as duas cadeias β do
    tetrâmero, faz pontes iônicas e estabiliza o estado T,
    aumentando o P#sub[50] da hemoglobina para a faixa fisiológica.]),
  ("E", [não atua diretamente na hemoglobina; o BPG modula somente a
    enzima anidrase carbônica, que por sua vez ajusta o pH local e
    altera a curva de dissociação por mecanismo indireto.]))

#questao("08", "consolidacao",
  [A hemoglobina fetal (HbF) tem afinidade pelo O₂ maior que a da
   hemoglobina adulta (HbA) porque:],
  ("A", [a cadeia γ substitui a β na composição do tetrâmero, e a γ
    é menos sensível ao BPG, o que mantém a HbF preferencialmente
    no estado R de alta afinidade.]),
  ("B", [a HbF possui um heme adicional por tetrâmero, perfazendo
    cinco sítios de ligação no total, o que aumenta a capacidade de
    captura de O₂ na circulação fetal placentária.]),
  ("C", [o ferro do heme na HbF está em estado Fe⁺¹ em vez de Fe²⁺,
    estado que confere afinidade maior pelo O₂ por motivos
    eletrônicos da coordenação química com o ligante.]),
  ("D", [a HbF é monomérica, composta apenas pela cadeia α, o que a
    torna semelhante à mioglobina e explica sua alta afinidade
    constante ao longo de toda a faixa de pO₂ fisiológica.]),
  ("E", [a HbF tem cadeias β idênticas às da HbA mas em maior número
    por tetrâmero, perfazendo seis subunidades totais no complexo
    funcional encontrado no eritrócito fetal humano em formação.]))

#questao("09", "consolidacao",
  [A anemia falciforme é causada por:],
  ("A", [deficiência de ferro na dieta materna durante a gestação,
    que compromete a síntese do grupo heme nas hemácias fetais e
    leva a hemoglobina disfuncional no recém-nascido afetado.]),
  ("B", [oxidação espontânea e progressiva do ferro do heme do
    estado Fe²⁺ para Fe³⁺ por falta da enzima metHb redutase em
    uma fração significativa das hemácias circulantes do paciente.]),
  ("C", [mutação pontual na cadeia β da hemoglobina, com substituição
    do glutamato da posição 6 por valina, criando ponto adesivo
    hidrofóbico que polimeriza HbS desoxigenada e enrijece a hemácia.]),
  ("D", [defeito de síntese da cadeia α com produção reduzida de
    hemoglobina total, condição conhecida como α-talassemia maior
    em sua forma de apresentação mais grave em adultos jovens.]),
  ("E", [hemólise autoimune crônica em que anticorpos contra antígenos
    da membrana eritrocitária destroem hemácias precocemente,
    causando anemia e crises vaso-oclusivas em pequenos vasos.]))

#questao("10", "consolidacao",
  [Na metahemoglobinemia, o paciente apresenta cianose porque:],
  ("A", [a hemoglobina está reduzida em quantidade total pela hemólise
    crônica, levando à redução geral da capacidade de transporte
    e à diminuição da oferta tecidual de oxigênio dissolvido.]),
  ("B", [o ferro do heme está oxidado a Fe³⁺, que não liga O₂; a
    molécula está estruturalmente intacta mas inerte para transporte,
    e a fração afetada não responde a O₂ suplementar.]),
  ("C", [há acúmulo de monóxido de carbono ligado ao Fe²⁺ dos hemes
    do paciente, com bloqueio competitivo do sítio do oxigênio e
    deslocamento da curva de dissociação para a direita.]),
  ("D", [a hemoglobina polimerizou em estruturas longas dentro da
    hemácia, modelo idêntico ao observado na anemia falciforme em
    crise vaso-oclusiva por hipóxia tecidual prolongada.]),
  ("E", [houve substituição em massa da HbA por HbF na vida adulta,
    fenômeno raro que reduz a entrega tecidual por aumento patológico
    da afinidade global da hemoglobina ao oxigênio.]))

// ====================== INTEGRAÇÃO (Q11-Q25) ======================

#questao("11", "integracao",
  [Durante o exercício intenso, o músculo esquelético recebe mais O₂
   da hemoglobina que passa pelo capilar do que em repouso. Isso
   ocorre porque a combinação de fatores locais inclui:],
  ("A", [pH alcalino, pCO₂ baixa, temperatura reduzida e BPG diminuído,
    fatores que estabilizam o estado R da hemoglobina e aumentam a
    afinidade pelo O₂ na microcirculação do músculo em contração.]),
  ("B", [aumento de bicarbonato plasmático e queda concomitante de
    pCO₂ tecidual, mecanismo de origem renal que reduz a afinidade
    da hemoglobina e libera mais oxigênio em tecidos hiperativos.]),
  ("C", [pH neutro estável, pCO₂ regulada por buffer bicarbonato
    pulmonar, temperatura constante de 37°C e BPG não alterado,
    sem mudança significativa na curva durante atividade intensa.]),
  ("D", [pH baixo (lactato e CO₂), pCO₂ alta e temperatura elevada
    pelo metabolismo — o efeito Bohr e a temperatura estabilizam T,
    deslocam a curva para a direita e a entrega aumenta.]),
  ("E", [aumento isolado de BPG sintetizado pelo músculo em contração,
    que se difunde para a hemácia, estabiliza o estado R da
    hemoglobina e aumenta a captura tecidual de O₂ em segundos.]))

#questao("12", "integracao",
  [Um alpinista permanece três semanas em altitude (~4500 m). Sua
   hemoglobina circulante apresenta, ao final desse período, em
   comparação com o nível do mar:],
  ("A", [P#sub[50] reduzido por aumento crônico de BPG eritrocitário,
    estado em que a hemoglobina capta menos O₂ no pulmão como
    estratégia de poupar oxigênio para o sistema nervoso central.]),
  ("B", [P#sub[50] aumentado por elevação crônica do BPG nas hemácias,
    que estabiliza o estado T e desloca a curva de dissociação para
    a direita, melhorando a entrega de O₂ aos tecidos.]),
  ("C", [P#sub[50] inalterado, porque a adaptação à altitude é
    ventilatória pura — aumento da frequência e profundidade
    respiratória basta para manter a oxigenação tecidual estável.]),
  ("D", [redução do número total de hemácias por hemodiluição
    adaptativa, com queda de hematócrito e aumento compensatório de
    P#sub[50] mediado pela diminuição local de BPG nas hemácias.]),
  ("E", [substituição parcial de HbA por HbF reativada por hipóxia
    crônica, com P#sub[50] reduzido e ganho funcional de afinidade
    semelhante ao da circulação fetal humana intrauterina.]))

#questao("13", "integracao",
  [Sobre o transporte de CO₂ do tecido para o pulmão pelo sangue
   humano, é correto afirmar que:],
  ("A", [a maior parte do CO₂ viaja covalentemente ligada ao ferro
    ferroso do heme da hemoglobina, em forma análoga à ligação do
    oxigênio na captura alveolar de gases respiratórios fisiológicos.]),
  ("B", [praticamente todo o CO₂ é transportado dissolvido no plasma
    sem participação eritrocitária, e o gás chega ao alvéolo apenas
    por difusão direta através da membrana respiratória pulmonar.]),
  ("C", [aproximadamente metade do CO₂ é convertida em carbamato na
    própria mioglobina muscular antes de ser entregue ao plasma
    para transporte sistêmico passivo até o pulmão por difusão.]),
  ("D", [todo o CO₂ tecidual liga-se irreversivelmente à hemoglobina
    como carbamato, e a regeneração do gás no pulmão depende
    exclusivamente da degradação enzimática dessa molécula.]),
  ("E", [a maior fração viaja como bicarbonato plasmático (~70%)
    gerado pela anidrase carbônica eritrocitária; ~23% viaja como
    carbamato na globina e ~7% dissolvido livre no plasma.]))

#questao("14", "integracao",
  [Sobre a relação entre o efeito Bohr e o tamponamento sanguíneo
   pela hemoglobina, é correto afirmar que:],
  ("A", [Bohr e tamponamento são processos moleculares independentes
    — o primeiro opera no heme, o segundo nas histidinas; a
    hemoglobina executa cada um em momentos diferentes do ciclo.]),
  ("B", [tamponamento é função renal pura, sem participação da
    hemoglobina; o efeito Bohr é função respiratória e se restringe
    à modulação alostérica da curva de dissociação tecidual.]),
  ("C", [os dois fenômenos são o mesmo mecanismo molecular olhado
    em direções opostas — captura de H⁺ pelas histidinas estabiliza
    T e libera O₂ no tecido; o inverso ocorre no pulmão.]),
  ("D", [Bohr atua apenas na captura de O₂ no pulmão, enquanto o
    tamponamento atua apenas na liberação tecidual; os dois ocorrem
    em momentos sequencialmente exclusivos do ciclo respiratório.]),
  ("E", [tamponamento pela hemoglobina depende exclusivamente da
    ligação do CO₂ ao ferro ferroso para formar carbamato, sem
    participação dos resíduos de histidina da cadeia globina.]))

#questao("15", "integracao",
  [Em um recém-nascido com cianose persistente que não responde a
   oxigênio suplementar e cujo sangue arterial tem cor chocolate na
   gasometria, a hipótese mais provável é:],
  ("A", [metahemoglobinemia congênita por deficiência da metHb
    redutase eritrocitária, com fração elevada de ferro férrico Fe³⁺
    incapaz de ligar O₂ apesar de gasometria com pO₂ normal.]),
  ("B", [intoxicação aguda por monóxido de carbono adquirida pela
    mãe durante o parto, com formação de carboxihemoglobina fetal
    estável e bloqueio competitivo do sítio do O₂ no Fe²⁺.]),
  ("C", [anemia falciforme em crise vaso-oclusiva neonatal precoce,
    com polimerização de HbS em hipóxia placentária e formação de
    hemácias rígidas que oclui capilares pulmonares.]),
  ("D", [α-talassemia maior com produção insuficiente de cadeia α
    e acúmulo de tetrâmeros γ₄ (hemoglobina de Bart), levando à
    incapacidade de captação alveolar adequada de O₂.]),
  ("E", [persistência patológica de HbF além dos 6 meses pós-natais,
    com elevação extrema de afinidade pelo O₂ e bloqueio total da
    entrega tecidual em todos os capilares periféricos sistêmicos.]))

#questao("16", "integracao",
  [Uma paciente com pneumonia grave em UTI desenvolve acidose
   respiratória aguda por hipoventilação. Sobre o efeito imediato
   na hemoglobina, é correto dizer que:],
  ("A", [a queda de pH local desloca a curva para a esquerda e
    diminui a entrega tecidual de O₂, agravando a hipóxia em todos
    os territórios distais ao foco infeccioso pulmonar primário.]),
  ("B", [a queda de pH desloca a curva para a direita (Bohr),
    aumenta a entrega tecidual de O₂, mas a captura pulmonar fica
    prejudicada pela hipoventilação concomitante na via aérea.]),
  ("C", [a hemoglobina perde a capacidade de tamponar prótons em
    quadros de acidose respiratória, e o pH sanguíneo cai
    proporcionalmente à pCO₂ sem amortecimento bioquímico nenhum.]),
  ("D", [aumento da pCO₂ desloca a curva para a esquerda por
    carbamato direto no heme, aumentando a afinidade pelo O₂ e
    melhorando paradoxalmente a entrega tecidual nesses quadros.]),
  ("E", [a curva permanece inalterada porque hemoglobina só responde
    a mudanças crônicas de pH; o efeito Bohr exige semanas de
    adaptação para se manifestar funcionalmente em condições agudas.]))

#questao("17", "integracao",
  [Um paciente com anemia falciforme apresenta crise vaso-oclusiva
   após uma infecção febril. Sobre a cadeia mecanística que liga
   infecção a oclusão capilar, é correto que:],
  ("A", [a infecção causa síntese aumentada de HbS pela medula
    óssea, e o excesso de tetrâmeros mutados nas hemácias novas
    deflagra a polimerização e oclusão capilar consecutiva.]),
  ("B", [a febre aumenta a temperatura sistêmica e isso oxida o
    ferro do heme das hemácias HbS a Fe³⁺, gerando metahemoglobina
    funcional que precipita dentro do eritrócito periférico.]),
  ("C", [a infecção reduz a contagem total de hemácias HbS em
    circulação, e o estresse oxidativo destas hemácias residuais
    leva à polimerização espontânea e oclusão da microcirculação.]),
  ("D", [hipóxia (consumo aumentado, possível pneumonia), febre
    (demanda metabólica) e desidratação (concentração de HbS) somam-se
    para aumentar a fração de HbS em T e a polimerização em capilares.]),
  ("E", [a febre converte HbS em HbF de forma reversível dentro das
    hemácias, e a HbF acumulada gera depósitos amiloides em
    capilares pequenos que causam vaso-oclusão por obstrução física.]))

#questao("18", "integracao",
  [Sobre a base molecular da maior afinidade da hemoglobina fetal
   (HbF) pelo O₂ em relação à HbA, é correto que:],
  ("A", [a HbF contém um quinto sítio adicional de ligação ao O₂ por
    tetrâmero, perfazendo cinco hemes ativos e maior capacidade de
    captura do oxigênio na microcirculação placentária materna.]),
  ("B", [o ferro do heme da HbF está em estado Fe⁺¹, o que confere
    afinidade extra pelo O₂ por mecanismos eletrônicos especiais
    da coordenação química na bolsa hidrofóbica da subunidade γ.]),
  ("C", [a cadeia γ substitui a β e perde a histidina que ancora o
    BPG na cavidade central; sem BPG estabilizando T, a HbF fica em
    R com afinidade aumentada pelo O₂ em condições fisiológicas.]),
  ("D", [a HbF é exclusivamente monomérica, formada por uma única
    cadeia γ; isso a torna funcionalmente análoga à mioglobina e
    com curva hiperbólica em vez de sigmoide na placenta materna.]),
  ("E", [a placenta materna sintetiza um cofator alostérico
    específico que se liga à HbF estabilizando o estado R por
    horas, processo mediado por hormônios placentários secretados.]))

#questao("19", "integracao",
  [Comparando a intoxicação por monóxido de carbono e a
   metahemoglobinemia, é correto que:],
  ("A", [os dois quadros são clinicamente idênticos, e o tratamento
    é o mesmo — administração de oxigênio 100% por máscara
    facial até a normalização gasométrica completa do paciente.]),
  ("B", [CO eleva o ferro do heme a Fe³⁺, e metaHb é o estado em que
    o CO está ligado ao Fe²⁺; tratamento de ambos converge para a
    administração intravenosa de azul de metileno como cofator.]),
  ("C", [CO ocupa o sítio do O₂ no Fe²⁺ e desloca a curva para a
    direita, enquanto metaHb tem Fe³⁺ inativo e curva para a esquerda,
    e os dois respondem igualmente a oxigênio hiperbárico de rotina.]),
  ("D", [a metaHb se distingue pela cianose responsiva a O₂ 100%
    em alto fluxo, e o tratamento dos dois quadros se baseia no
    mesmo princípio bioquímico de redução do ferro para Fe²⁺.]),
  ("E", [CO ocupa o sítio do O₂ no Fe²⁺ e desloca a curva para a
    ESQUERDA (aumenta afinidade dos hemes vizinhos); metaHb tem
    Fe³⁺ inerte. Antídotos: O₂ 100% para CO, azul de metileno para metaHb.]))

#questao("20", "integracao",
  [Sobre a relação entre o estado conformacional T da hemoglobina e a
   polimerização da HbS na anemia falciforme, é correto que:],
  ("A", [a polimerização da HbS é o exemplo paradigmático de
    polimerização que depende criticamente do estado T (desoxigenada)
    — só em T a cavidade hidrofóbica complementar fica exposta e
    permite o encaixe entre moléculas mutadas vizinhas.]),
  ("B", [a polimerização ocorre exclusivamente no estado R
    (oxigenada), pois a oxigenação amplia a superfície hidrofóbica
    da mutação Val6 e facilita o reconhecimento mútuo entre as
    moléculas de HbS na hemácia periférica em circulação venosa.]),
  ("C", [a HbS em T e em R polimeriza igualmente, porque a mutação
    Glu6→Val está exposta o tempo todo na superfície externa da
    cadeia β independentemente do estado conformacional ocupado.]),
  ("D", [o estado T da HbS impede a polimerização e o estado R a
    favorece, e por isso o tratamento crônico inclui agentes que
    estabilizam o tetrâmero em T para evitar a crise vaso-oclusiva.]),
  ("E", [a polimerização independe da conformação T ou R e depende
    exclusivamente do pH local; pH baixo favorece a precipitação da
    HbS por mecanismo análogo à precipitação de proteínas in vitro.]))

#questao("21", "integracao",
  [Sobre a participação da anidrase carbônica eritrocitária no
   transporte sanguíneo de CO₂ e na função tamponante da
   hemoglobina, é correto que:],
  ("A", [a enzima converte CO₂ em metano dentro da hemácia, gás
    expirado livremente pelos alvéolos sem participação da
    hemoglobina e sem efeito direto no pH sanguíneo arterial humano.]),
  ("B", [a anidrase carbônica atua só no pulmão, convertendo
    bicarbonato em CO₂ para expiração; no tecido, o CO₂ apenas se
    dissolve no plasma e não interage com a hemoglobina diretamente.]),
  ("C", [a anidrase carbônica hidrata CO₂ a H₂CO₃ (e este se dissocia
    em H⁺ + HCO₃⁻); H⁺ gerado liga-se à hemoglobina via Bohr e o
    HCO₃⁻ sai da hemácia em troca por Cl⁻ pelo transportador AE1.]),
  ("D", [a enzima decompõe carbamato da hemoglobina diretamente,
    liberando CO₂ no plasma para difusão alveolar, sem geração de
    bicarbonato como intermediário no transporte sanguíneo gasoso.]),
  ("E", [a anidrase carbônica não tem função no transporte de CO₂;
    sua única ação fisiológica é a regulação do pH gástrico através
    de secreção parietal de ácido clorídrico pela mucosa.]))

#questao("22", "integracao",
  [Um paciente com hipóxia crônica por DPOC grave tende a
   apresentar, ao longo de meses:],
  ("A", [diminuição progressiva da concentração eritrocitária de BPG
    como mecanismo adaptativo, reduzindo o P#sub[50] da hemoglobina
    para aumentar a captura pulmonar do pouco O₂ disponível.]),
  ("B", [substituição gradual de HbA por HbF sintetizada na medula
    como mecanismo evolutivo de proteção, com aumento global da
    afinidade da hemoglobina pelo O₂ em todos os compartimentos.]),
  ("C", [conversão progressiva da hemoglobina em metahemoglobina
    pela oxidação acelerada do ferro, com perda funcional gradual
    da capacidade de transporte ao longo da progressão da doença.]),
  ("D", [aumento crônico de BPG eritrocitário com elevação do
    P#sub[50] e deslocamento da curva para a direita, otimizando a
    entrega tecidual do O₂ disponível na microcirculação periférica.]),
  ("E", [substituição da hemoglobina por mioglobina circulante
    como mecanismo de compensação, fenômeno raro descrito em
    pacientes com hipóxia crônica não responsiva a oxigenoterapia.]))

#questao("23", "integracao",
  [Sobre o transporte de óxido nítrico (NO) pela hemoglobina e seu
   papel modulatório, é correto que:],
  ("A", [NO se liga somente ao Fe³⁺ da metahemoglobina e por isso
    é o tratamento de escolha para a metahemoglobinemia adquirida
    em ambientes contaminados por óxidos de nitrogênio industrial.]),
  ("B", [NO pode se ligar covalentemente a resíduos de cisteína da
    cadeia β (formando S-nitrosohemoglobina) e ser liberado em
    tecidos hipóxicos, contribuindo para vasodilatação local.]),
  ("C", [NO é o mesmo composto que CO e atua exatamente da mesma
    forma, ligando o ferro ferroso e deslocando a curva para a
    direita, com clínica idêntica nas duas intoxicações combinadas.]),
  ("D", [NO se liga ao BPG no plasma e o impede de penetrar na
    hemácia, deslocando a curva para a esquerda por inibição
    indireta do principal modulador alostérico fisiológico humano.]),
  ("E", [NO não tem interação biologicamente relevante com a
    hemoglobina humana adulta — atua exclusivamente sobre a
    guanilato ciclase solúvel das células musculares lisas vasculares.]))

#questao("24", "integracao",
  [Sobre a relação entre a temperatura corporal e a afinidade da
   hemoglobina pelo O₂, é correto que:],
  ("A", [a temperatura é fisiologicamente irrelevante para a curva
    de dissociação da hemoglobina, que responde exclusivamente a
    pH, pCO₂ e BPG em todas as condições clínicas humanas usuais.]),
  ("B", [elevação da temperatura local desloca a curva para a esquerda
    e aumenta a afinidade pelo O₂, mecanismo útil em estados febris
    pois ajuda a preservar o oxigênio em compartimentos hipoperfundidos.]),
  ("C", [o efeito da temperatura é apenas indireto via metabolismo
    aumentado (mais CO₂, mais H⁺) e portanto idêntico ao efeito Bohr,
    sem participação física direta da molécula de hemoglobina nele.]),
  ("D", [a hipotermia (cirurgia cardíaca) eleva a afinidade da
    hemoglobina ao O₂, dificulta a entrega tecidual e por isso requer
    estratégias específicas para garantir oxigenação dos tecidos.]),
  ("E", [elevação da temperatura desloca a curva para a direita
    (diminui afinidade, aumenta entrega tecidual); a hipotermia faz o
    oposto, deslocando para a esquerda — coerente com a demanda metabólica.]))

#questao("25", "integracao",
  [Em um paciente em ventilação com FiO₂ 100% por intoxicação
   suspeita por monóxido de carbono, o objetivo terapêutico do
   oxigênio em alta concentração é:],
  ("A", [reverter a oxidação do ferro do heme de Fe³⁺ para Fe²⁺,
    restaurando a capacidade de ligação ao O₂ por reação redox direta
    no sítio do heme dentro da hemácia circulante do paciente.]),
  ("B", [induzir a síntese de hemoglobina fetal pelas células-tronco
    medulares, deslocando a HbA carboxilada por HbF não afetada nas
    primeiras horas de tratamento intensivo em pacientes graves.]),
  ("C", [polimerizar a hemoglobina carboxilada em formas inativas
    que serão fagocitadas no baço, removendo a fração de hemoglobina
    afetada pelo CO da circulação periférica em poucas horas.]),
  ("D", [aumentar a pressão parcial alveolar de O₂ para deslocar
    competitivamente o CO ligado ao Fe²⁺ do heme, reduzindo o
    tempo de meia-vida da carboxihemoglobina circulante.]),
  ("E", [substituir o CO ligado ao Fe²⁺ por azul de metileno, que
    libera o ferro para nova ligação fisiológica com o oxigênio após
    a remoção do gás tóxico pela respiração pulmonar normal.]))

// ====================== APLICAÇÃO (Q26-Q30) ======================

#questao("26", "aplicacao",
  [Um trabalhador é resgatado inconsciente de um galpão fechado onde
   funcionava um gerador a gasolina por horas. Na sala de emergência,
   está em coma, com pele de cor rosada e SpO₂ no oxímetro de dedo
   marcando 99%. A gasometria arterial revela pO₂ normal de 95 mmHg.
   A explicação fisiopatológica mais provável e a conduta inicial são:],
  ("A", [intoxicação por gás carbônico com narcose hipercápnica;
    administrar bicarbonato endovenoso e iniciar suporte ventilatório
    invasivo para controle imediato do pH e da pCO₂ arteriais.]),
  ("B", [hipoglicemia profunda por jejum prolongado durante o turno
    de trabalho; administrar glicose 50% endovenosa e reavaliar nível
    de consciência após 30 minutos no leito de observação clínica.]),
  ("C", [metahemoglobinemia adquirida por exposição a nitritos
    industriais presentes no combustível; administrar azul de
    metileno endovenoso para reduzir o ferro férrico aos níveis
    funcionais usuais e estabilizar a saturação periférica.]),
  ("D", [intoxicação por monóxido de carbono — SpO₂ é falsamente
    normal porque o oxímetro não distingue HbO₂ de HbCO; tratar
    com O₂ a 100% (alto fluxo) para deslocar o CO do Fe²⁺ do heme.]),
  ("E", [intoxicação por óxido nítrico industrial com vasodilatação
    sistêmica e síncope vasovagal; administrar noradrenalina em
    bomba de infusão contínua e iniciar reposição volêmica rápida.]))

#questao("27", "aplicacao",
  [Uma criança de 3 meses é levada ao pronto-socorro pela mãe por
   "cor azulada" persistente nos lábios. Estava em uso recente de um
   anestésico tópico (gel de benzocaína) para alívio de dor de
   dentição. A SpO₂ marca 85% e o sangue da gasometria tem cor
   chocolate. A causa provável e o tratamento são:],
  ("A", [crise vaso-oclusiva precoce de anemia falciforme
    inesperada para a idade; iniciar reposição volêmica agressiva,
    analgesia parenteral, oxigenoterapia em máscara facial e
    avaliação imediata de troca transfusional por equipe pediátrica.]),
  ("B", [metahemoglobinemia adquirida pela benzocaína (oxidante do
    Fe²⁺ a Fe³⁺) somada à imaturidade da metHb redutase nessa idade;
    administrar azul de metileno endovenoso e suspender a benzocaína.]),
  ("C", [intoxicação por monóxido de carbono em ambiente doméstico,
    possivelmente por aquecedor a gás defeituoso; iniciar O₂ a 100%,
    investigar família e considerar transferência para câmara hiperbárica.]),
  ("D", [cardiopatia congênita cianogênica subdiagnosticada até este
    momento por progressão silenciosa; encaminhar imediatamente para
    cateterismo cardíaco e avaliação cirúrgica em centro de referência.]),
  ("E", [hipoglicemia neonatal tardia por aleitamento materno
    exclusivo insuficiente; administrar solução glicosada por sonda
    nasogástrica e orientar reforço da amamentação ao longo do dia.]))

#questao("28", "aplicacao",
  [Um paciente de 25 anos com diagnóstico prévio de anemia falciforme
   chega ao PS com dor torácica intensa, febre de 39°C e dispneia.
   Refere quadro infeccioso respiratório iniciado três dias antes,
   com diminuição da ingesta hídrica. A explicação mecanística que
   conecta os achados à crise atual é:],
  ("A", [a febre induz síntese acelerada de HbS pela medula óssea,
    e o excesso súbito de tetrâmeros mutados nas hemácias novas
    deflagra crise vaso-oclusiva precoce na vasculatura sistêmica.]),
  ("B", [a infecção bloqueia diretamente a anidrase carbônica
    eritrocitária e impede o tamponamento de prótons, causando
    acidose grave que precipita a falência multissistêmica do paciente.]),
  ("C", [a desidratação reduz o número total de hemácias circulantes
    e o estresse oxidativo das remanescentes oxida o ferro do heme a
    Fe³⁺, gerando metahemoglobinemia e cianose secundária do quadro.]),
  ("D", [a febre desnatura termicamente a HbS no compartimento
    intravascular, formando agregados proteicos amorfos que oclui os
    capilares pulmonares por embolia de proteína desnaturada solúvel.]),
  ("E", [hipóxia pulmonar (infecção), febre (maior demanda metabólica
    tecidual) e desidratação (maior concentração intracelular de HbS)
    somam-se para aumentar a fração de HbS em T e a polimerização.]))

#questao("29", "aplicacao",
  [Uma gestante no 3º trimestre realiza gasometria fetal por cordocentese
   indicada. O sangue fetal mostra saturação de O₂ aceitável apesar
   de o pO₂ medido ser bem mais baixo que o esperado no compartimento
   materno comparável. O mecanismo molecular que explica essa diferença é:],
  ("A", [o sangue fetal tem hematócrito muito maior que o do adulto,
    compensando integralmente o pO₂ baixo do compartimento placentário
    pela quantidade total elevada de hemoglobina por mililitro de plasma.]),
  ("B", [a circulação fetal possui um sistema enzimático adicional de
    captura forçada de O₂ na placenta, baseado em transportadores
    ativos da membrana eritrocitária dependentes de ATP intracelular.]),
  ("C", [a HbF tem afinidade maior pelo O₂ que a HbA por insensibilidade
    relativa ao BPG (cadeia γ no lugar da β); a curva é deslocada para
    a esquerda, e o feto satura bem mesmo em pO₂ baixa na placenta.]),
  ("D", [o pO₂ medido na cordocentese é falsamente baixo por artefato
    técnico universal do método; o pO₂ real no feto é equivalente ao
    do adulto e a saturação simplesmente acompanha o valor verdadeiro.]),
  ("E", [a hemoglobina fetal tem um número adicional de hemes por
    tetrâmero que aumenta a capacidade total de carga de oxigênio na
    molécula, compensando o pO₂ baixo no ambiente placentário materno.]))

#questao("30", "aplicacao",
  [Uma mulher de 45 anos é encontrada inconsciente em casa após uma
   tentativa de suicídio com ingestão de cápsula desconhecida. Chega
   ao PS cianótica, com SpO₂ 78% que não melhora com O₂ 100% em
   máscara, gasometria com pO₂ 110 mmHg e sangue cor chocolate. A
   hipótese e a conduta são:],
  ("A", [metahemoglobinemia adquirida por oxidante exógeno (nitritos,
    dapsona, anilinas, etc.); administrar azul de metileno
    endovenoso, que reduz Fe³⁺ a Fe²⁺ e restaura a função da hemoglobina.]),
  ("B", [intoxicação por monóxido de carbono inalado em ambiente
    fechado; transferir imediatamente para câmara hiperbárica de O₂
    pressurizado e manter sedação intensiva para suporte avançado.]),
  ("C", [crise vaso-oclusiva de anemia falciforme não diagnosticada
    em vida adulta tardia; iniciar transfusão de troca emergencial e
    suporte com cristaloides aquecidos para reverter o quadro neurológico.]),
  ("D", [coma diabético cetoacidótico com cianose periférica intensa;
    administrar insulina endovenosa em bomba e iniciar reposição
    volêmica vigorosa com solução salina 0,9% guiada por pH arterial.]),
  ("E", [intoxicação por cianeto, bloqueio total da cadeia respiratória
    mitocondrial; administrar hidroxicobalamina endovenosa e manter
    suporte ventilatório intensivo até a recuperação da consciência.]))
