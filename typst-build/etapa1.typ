#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Todo sistema do corpo trabalha para manter a homeostasia, mas quase todos olham só para dentro: o rim mede o sódio do próprio plasma, o pulmão mede o gás carbônico do próprio sangue. Dois sistemas fogem dessa regra e precisam levar em conta o que existe do lado de fora — o nervoso, que lê o mundo por luz, som e pressão, e o imune, que lê o mundo por moléculas. É essa exigência que explica tudo o que vem a seguir. Para reconhecer moléculas que ele nunca viu, o sistema imune constrói um repertório de receptores praticamente infinito, mas distribuído de um jeito peculiar: cada linfócito carrega um único tipo de receptor e reconhece um único antígeno. A consequência prática é imediata — se cada célula sabe uma coisa só, a célula certa precisa estar no lugar certo na hora certa. Este resumo persegue esse problema logístico por quatro caminhos. Primeiro, o que o sistema faz quando a homeostasia se rompe e como ele fica sabendo disso. Depois, onde os linfócitos nascem e por que eles não param quietos. Em seguida, o que acontece dentro do órgão linfoide secundário, o lugar onde uma informação vinda do tecido vira resposta ou vira tolerância. Por fim, as moléculas que escrevem, célula por célula, o endereço de cada viagem.
]

#parte-title("PARTE I — Um sistema que precisa falar a língua do lado de fora", primeira: true)

#subtopico("1.1 — O problema: manter a homeostasia sem conhecer o inimigo")

O sistema imune é, antes de qualquer coisa, um sistema de homeostasia. Ele existe pela mesma razão que existem o sistema renal e o sistema respiratório: manter as variáveis do organismo dentro de uma faixa estreita e devolvê-las a essa faixa quando algo as desloca. A diferença está no que ele monitora. A maioria dos sistemas se ocupa do próprio organismo, e por isso os sinais de desequilíbrio que eles precisam ler são previamente conhecidos — a pressão parcial de oxigênio, a osmolaridade, o pH. Esses sinais são finitos e o corpo pode fabricar de antemão um sensor para cada um.

Dois sistemas, porém, incluem o exterior nessa conta. O sistema nervoso inclui o exterior por meio de luz, som, temperatura e pressão. O sistema imune inclui o exterior por meio de sinais moleculares: ele lê o mundo pela química do que encosta no organismo. O ponto fino é que essa segunda tarefa é logicamente mais difícil, porque o repertório de moléculas que podem aparecer não é finito nem previsível. Uma bactéria nova, um vírus recém-mutado, uma proteína de um alimento que nunca foi comido antes — nada disso estava no catálogo.

E aqui aparece a restrição que organiza o resto da aula: uma célula só consegue interagir com aquilo que os seus receptores preveem. Sinal molecular sem receptor correspondente simplesmente passa despercebido — não é ignorado por decisão, é invisível por construção. Se o sistema imune tivesse apenas os receptores que o genoma herdado codifica, tudo o que fosse verdadeiramente novo escaparia. É desse impasse que nasce a solução mais cara e mais original do sistema imune, e é dela que trata o próximo subtópico.

#mini-resumo[Em uma frase: o sistema imune é homeostático como os outros, mas monitora o exterior por sinais moleculares — e como uma célula só enxerga o que seus receptores preveem, um repertório fixo herdado deixaria o novo invisível.]

#subtopico("1.2 — O tradutor universal e o preço de um repertório clonal")

Imagine uma central de tradução que precisa atender qualquer idioma que apareça na porta, inclusive idiomas que ainda não foram inventados. Contratar um tradutor por idioma conhecido não resolve. A saída é contratar milhões de tradutores gerados ao acaso, cada um fluente em um idioma sorteado, e apostar que a coleção inteira cubra qualquer coisa que chegue. É exatamente isso que o sistema imune faz: ele gera um repertório completo de receptores capazes de reconhecer praticamente qualquer estrutura molecular de tamanho adequado. Aquilo que esses receptores reconhecem chama-se antígeno.

Esse repertório tem uma propriedade que muda toda a logística: ele é distribuído clonalmente. Cada linfócito T ou B expressa um único tipo de receptor e, portanto, reconhece um único antígeno; todas as células descendentes daquele linfócito herdam a mesma especificidade e formam um clone. Dito de outro modo, o sistema como um todo reconhece tudo, mas cada célula reconhece uma coisa só. O sistema imune funciona, nesse sentido, como um tradutor universal montado a partir de milhões de tradutores especializados em um idioma cada.

O preço dessa arquitetura é logístico, e é o que vai ocupar as PARTES II e III. Se a célula capaz de reconhecer determinado antígeno é raríssima — uma em milhões —, não basta que ela exista: ela precisa encontrar o antígeno. Guarde isso, porque toda a anatomia dos órgãos linfoides e todo o vaivém dos linfócitos são engenharia dedicada a aumentar a probabilidade desse encontro.

#mini-resumo[Em cadeia: repertório gerado ao acaso → distribuição clonal (um linfócito, um antígeno) → o sistema reconhece tudo, mas cada célula reconhece uma coisa só → o encontro entre antígeno e clone específico vira um problema de probabilidade.]

#subtopico("1.3 — O alarme: quem grita no tecido e o que cada grito informa")

Agora que está claro o que o sistema precisa reconhecer, vale olhar para o que acontece fisicamente quando algo entra. O organismo é protegido por barreiras anatômicas, funcionais e biológicas — pele e mucosas, muco, pH, peristalse, microbiota. Quando uma dessas barreiras é rompida, a perturbação acontece dentro de um tecido que nunca está vazio: além das células próprias do tecido, ali residem macrófagos, mastócitos, células endoteliais e as #sigla("ILC", [innate lymphoid cells — células linfoides inatas, residentes do tecido]).

O que diferencia esses quatro alarmes é a quantidade de informação que cada um carrega, e essa graduação é o detalhe que importa aqui. As células do próprio tecido dão o alarme mais primitivo: elas são lesadas e, ao serem lesadas, liberam moléculas que normalmente ficam trancadas dentro da célula — os #sigla("DAMP", [damage-associated molecular patterns — padrões moleculares associados a dano, liberados por células lesadas]). Esse sinal diz apenas "há dano aqui", sem dizer de que tipo. O macrófago é mais especializado: ele reconhece a perturbação e produz citocinas e quimiocinas, moléculas cuja função é restrita o bastante para informar mais ou menos *o que* está errado, não apenas que algo está. O mastócito é a bomba de alarme: cutucado, ele degranula de uma vez e despeja mediadores inflamatórios que provocam uma reação rápida e intensa naquele tecido — histamina à frente, com vasodilatação e aumento de permeabilidade imediatos. E a célula endotelial, que parecia apenas o encanamento, é quem executa a decisão: ela muda as moléculas de adesão da sua superfície e, com isso, define quais células do sangue vão poder parar ali.

Repare que a célula endotelial já aparece aqui como peça ativa, e não como cenário. Ela é o ponto em que a PARTE IV vai se encaixar: o alarme não convoca células apenas produzindo sinais solúveis, ele reescreve a superfície do vaso para que a célula certa consiga aderir. Tudo isso somado — sinais de dano, citocinas, mediadores, endotélio ativado — constitui a resposta imune inata, voltada à restauração da homeostasia.

#figura-nebli("/figuras/imuno-02-organizacao-sistema-imune/slide-06.png",
  largura: 76%,
  legenda: [O tecido em repouso já contém os sensores. Rompida a barreira, cada tipo celular dá um alarme com resolução diferente: dano genérico das células do tecido, informação específica dos macrófagos, reação rápida dos mastócitos e mudança de superfície do endotélio.])

#mini-resumo[Em cadeia: barreira rompida → célula do tecido lesada libera DAMPs (há dano) → macrófago produz citocinas e quimiocinas (o que há) → mastócito degranula (reação rápida) → endotélio muda moléculas de adesão (quem pode entrar) = resposta inata.]

#subtopico("1.4 — O que a inata faz com o alarme — e por que isso não encerra o assunto")

O reflexo é imaginar que a resposta inata é um ciclo fechado: entrou algo, a inata resolve, a homeostasia volta e o caso termina. Antes de desfazer essa impressão, vale ver o que a inata de fato executa. Dois processos concentram a maior parte do trabalho efetor. O primeiro é a fagocitose, um mecanismo antiquíssimo — protozoários já comem por fagocitose — que o organismo aproveitou: a célula engloba a partícula e, depois de ingeri-la, ainda tem trabalho a fazer com ela, porque digerir e processar o que foi comido é justamente o que abre a porta para a apresentação de antígeno na PARTE III. O segundo é a citotoxicidade celular, mais sofisticada: uma célula citotóxica reconhece uma célula-alvo, entrega a ela um sinal, e a célula-alvo executa um programa próprio de morte. A efetora não explode junto — ela se desliga do cadáver e vai procurar outro alvo.

#figura-lateral("/figuras/imuno-02-organizacao-sistema-imune/slide-08.png",
  lado: "right",
  largura-figura: 42%,
  texto: [O ponto fino da citotoxicidade é que quem morre executa a própria morte. A célula efetora não perfura e dissolve o alvo como quem estoura um balão; ela entrega um sinal que aciona um programa de apoptose já escrito dentro da célula-alvo. É por isso que a mesma efetora pode matar várias células em sequência — ela gasta sinal, não gasta a si mesma —, e é por isso que a morte sai contida, sem derramar o conteúdo celular no tecido e sem ampliar a inflamação.],
  legenda: [Citotoxicidade celular: reconhecimento do alvo, entrega do sinal e morte programada do alvo.])

Só que nem sempre a inata restaura a homeostasia sozinha. E — este é o ponto que importa — mesmo quando ela restaura, quase sempre um segundo fenômeno se desenvolve em paralelo. Junto com a resposta ao dano, começa a montar-se uma resposta dirigida às *moléculas* presentes naquele tecido, e cada molécula induz um tipo de resposta. Essa é a resposta imune adquirida. Ela não é o plano B acionado quando a inata falha; ela é uma consequência quase obrigatória do mesmo episódio. Parte do direcionamento dessa resposta é dado justamente pelas células inatas residentes, as ILC entre elas, que interpretam o tipo de agressão e empurram a resposta subsequente para um lado ou para outro.

#confusao-prevista(
  titulo: "Adquirida não é o plano B da inata",
  aluno_acha: [aluno tende a ler as duas respostas como etapas sequenciais e alternativas — a inata tenta, falha, e só então a adquirida entra em cena],
  mecanismo: [na prática as duas correm juntas desde o começo. A inata restaura a homeostasia no tecido enquanto a informação daquele mesmo tecido já está sendo levada ao órgão linfoide para o reconhecimento clonal. Mais adiante veremos o outro lado da mesma moeda: os produtos de uma resposta adquirida passada são recrutados pela inata no episódio seguinte — é exatamente esse acoplamento que uma vacina explora.],
)

#mini-resumo[Em cadeia: alarme → fagocitose e citotoxicidade restauram o tecido (inata) → em paralelo, as moléculas daquele tecido induzem resposta adquirida → as duas não se sucedem, se sobrepõem.]

#mapa-parte(
  parte: "PARTE I",
  centro: [Ler o exterior por sinais moleculares],
  nos: ((id: "1.1–1.2", titulo: "Repertório clonal", texto: [Receptores sorteados ao acaso; cada linfócito reconhece um único antígeno.]),
        (id: "1.3", titulo: "Alarme graduado", texto: [DAMP, citocina, mediador e adesão — cada sinal com sua resolução.]),
        (id: "1.4", titulo: "Inata e adquirida", texto: [Efetores restauram o tecido enquanto a resposta adquirida já se monta.])),
  arestas: (("", "", [torna raro o clone]), ("", "", [que o alarme convoca])),
  fecha-com: [Se cada clone é raro, ele precisa ser encontrado — é disso que trata a PARTE II.],
)

#parte-title("PARTE II — Do lugar onde os linfócitos nascem ao lugar onde eles encontram")

#subtopico("2.1 — Órgãos linfoides primários: fabricar o repertório longe do mundo")

Gerar um repertório aleatório exige um lugar protegido, e é essa a função dos órgãos linfoides primários: o timo, para os linfócitos T, e a medula óssea, para os linfócitos B. Três coisas acontecem ali e não acontecem em nenhum outro lugar. A primeira é a geração dos genes que codificam os receptores clonais. Vale insistir nisso porque é contraintuitivo: esses genes não existem prontos na célula germinativa. Eles são montados somaticamente, dentro do precursor linfocitário, por recombinação de segmentos gênicos — cada célula sorteia a sua combinação, e é desse sorteio que sai a diversidade do repertório.

A segunda é a seleção. Não interessa qualquer receptor: só os receptores considerados úteis pelo sistema podem seguir adiante, e o subtópico seguinte detalha por quais provas eles passam. A terceira é o isolamento — uma espécie de proteção contra o meio externo, para que a geração e a seleção aconteçam com o mínimo de interferência de antígenos vindos de fora. A consequência é elegante: a seleção do repertório é feita essencialmente contra o *próprio*, contra o que está presente ali dentro. O sistema aprende primeiro quem é ele mesmo, e só depois sai para o mundo.

#mini-resumo[Órgão linfoide primário faz três coisas: monta somaticamente os genes do receptor clonal, seleciona os receptores úteis e faz as duas coisas isolado do meio externo — por isso a referência da seleção é o próprio organismo.]

#subtopico("2.2 — A seleção tímica: duas provas, três destinos")

Como o timo é a fonte do linfócito T, e como quase toda resposta imune depende de linfócito T, vale abrir a caixa da seleção tímica. O timócito precisa passar por duas provas encadeadas, e é o resultado combinado das duas que decide o seu destino.

A primeira prova é a capacidade de interagir com células apresentadoras de antígeno. Um receptor de linfócito T não reconhece antígeno solto: ele só reconhece antígeno exibido por uma molécula apresentadora na superfície de outra célula. Um timócito cujo receptor não consegue encostar minimamente nessas moléculas é inútil por definição, e morre por falta de sinal — é a seleção positiva, que ocorre no córtex tímico e resgata apenas quem tem alguma afinidade pelo #sigla("MHC", [major histocompatibility complex — complexo principal de histocompatibilidade, as moléculas que apresentam antígeno aos linfócitos T]) próprio.

A segunda prova é a autorreatividade, e ela ocorre na medula tímica. Um timócito que reconhece com força um antígeno próprio é perigoso, e o timo tem dois caminhos para ele. O caminho mais comum é a deleção clonal: a célula autorreativa recebe ordem de morrer, e um número enorme de timócitos termina exatamente assim. O outro caminho é o desvio funcional — em vez de morrer, a célula adquire função reguladora e sai do timo como linfócito T regulador, cuja tarefa passa a ser conter respostas contra aquele mesmo antígeno próprio. É uma solução econômica: o mesmo reconhecimento que seria destrutivo vira ferramenta de controle.

#clinica-box("Quando o timo não consegue mostrar o próprio: AIRE e a APECED")[
  Para deletar timócitos autorreativos, a medula tímica precisa exibir antígenos que, no corpo, só existem em tecidos distantes — insulina, tireoglobulina, antígenos de paratireoide e de adrenal. Quem força essa exibição é o fator de transcrição AIRE, expresso pelas células epiteliais medulares do timo: ele liga, dentro do timo, genes que seriam exclusivos de outros órgãos. Mutações em AIRE causam a síndrome poliendócrina autoimune tipo 1 (APECED): sem a vitrine completa do próprio, escapam clones autorreativos e o paciente desenvolve candidíase mucocutânea crônica, hipoparatireoidismo e insuficiência adrenal. É a prova clínica de que a tolerância central não é um conceito abstrato — ela é um inventário que precisa ser exibido peça por peça.
]

#mini-resumo[Em cadeia: prova 1, interagir com MHC próprio (seleção positiva, córtex) → prova 2, autorreatividade (medula) → autorreativo forte morre por deleção clonal, ou desvia e vira T regulador.]

#subtopico("2.3 — Órgãos linfoides secundários: o mapa dos endereços possíveis")

Terminada a fábrica, começa o comércio. No órgão linfoide primário nada acontece em termos de resposta — as células geradas precisam sair dali e se dirigir aos órgãos linfoides secundários, porque é neles que o reconhecimento do antígeno acontece. A lista é conhecida: linfonodos, baço, placas de Peyer, apêndice cecal, anel de Waldeyer e aglomerados linfoides transitórios que se organizam onde houver estímulo persistente.

Vale olhar essa lista com atenção, porque ela esconde uma divisão funcional. Linfonodo e baço são órgãos encapsulados e individualizados; todo o resto — placas de Peyer, apêndice, anel de Waldeyer, agregados transitórios — está associado a mucosas, e o conjunto recebe o nome de #sigla("MALT", [mucosa-associated lymphoid tissue — tecido linfoide associado às mucosas]). No trato respiratório esse tecido tem até nome próprio, #sigla("BALT", [bronchus-associated lymphoid tissue — tecido linfoide associado aos brônquios]). E aqui vai a sutileza que costuma se perder: embora se saiba muito mais sobre a resposta imune no linfonodo e no baço, é na mucosa que o sistema imune gasta mais energia e faz mais trabalho, simplesmente porque é ali que a superfície de contato com o mundo é maior.

#mini-resumo[Primário gera e seleciona; secundário reconhece. Linfonodo e baço são encapsulados; placas de Peyer, apêndice e anel de Waldeyer compõem o MALT — e é na mucosa que o sistema trabalha mais.]

#subtopico("2.4 — A circulação do linfócito naïve e a porta chamada HEV")

Pense num vendedor que precisa cobrir um país inteiro e não pode ficar parado numa cidade. O linfócito recém-formado — o linfócito naïve, ingênuo, que ainda não encontrou o seu antígeno — está exatamente nessa situação, e o circuito que ele percorre é fixo. Ele sai do órgão primário, cai no sangue, é distribuído e se localiza nos órgãos linfoides secundários. Passa um tempo ali, e sai pela linfa; a linfa é recolhida e devolvida ao sangue, e o ciclo recomeça. Duas regras do circuito merecem ser gravadas. A primeira é que ele é de mão única na origem: fisiologicamente nenhum linfócito volta para o órgão linfoide primário. A segunda é que a saída do órgão linfoide secundário se faz pela linfa, não pelo sangue — o linfócito que se vê no sangue saindo de um linfonodo, na verdade, nunca entrou nele; ele apenas não achou a porta de saída do vaso e seguiu adiante. Não é à toa que essas células se chamam linfócitos: são as células da linfa.

Por que tanto vaivém? Porque cada linfócito reconhece um único antígeno. Para que um órgão linfoide tenha representantes capazes de reconhecer qualquer antígeno que chegue, seria preciso guardar ali dentro o repertório inteiro — o que é impossível. Em qualquer instante, um dado linfonodo abriga apenas uma fração do repertório. A recirculação contínua é o que compensa essa amostragem incompleta: se o clone certo não está aqui agora, ele passa por aqui em breve.

Falta a peça que fecha o mecanismo, e ela é a mais bonita: como o linfócito sabe que aquele ponto do vaso é um órgão linfoide secundário? Ele está dentro de um vaso sanguíneo; tudo o que ele enxerga é endotélio. A resposta é que os órgãos linfoides secundários possuem vênulas especiais, de endotélio alto — as #sigla("HEV", [high endothelial venules — vênulas de endotélio alto, porta de entrada do linfócito do sangue para o órgão linfoide secundário]). Enquanto o endotélio comum é achatado, o dessas vênulas é cúbico e alto, e expõe moléculas de adesão que funcionam como uma placa: aqui é o ponto de saída. O linfócito naïve carrega a chave correspondente — a L-selectina, ou CD62L, que reconhece as adressinas periféricas expostas na HEV — e a quimiocina apresentada ali, agindo sobre o receptor CCR7 do linfócito, converte esse toque em parada firme e entrada no órgão. É por isso que a HEV é o endereço: ela é o único trecho do vaso que exibe simultaneamente o ligante da selectina e a quimiocina de entrada.

#figura-nebli("/figuras/imuno-02-organizacao-sistema-imune/slide-13.png",
  largura: 74%,
  legenda: [O circuito do linfócito naïve. Do órgão primário para o sangue, do sangue para o órgão linfoide secundário atravessando a HEV, e do órgão de volta ao sangue pela linfa. A entrada é pelo sangue, a saída é pela linfa — e nenhuma seta retorna ao órgão primário.])

#clinica-box("Fingolimode: trancar o linfócito dentro do linfonodo")[
  A saída do linfócito para a linfa não é passiva. Ela depende de um gradiente: a esfingosina-1-fosfato (S1P) é abundante na linfa e no sangue e escassa dentro do órgão linfoide, e o linfócito que reexpõe o receptor S1PR1 é puxado para fora seguindo esse gradiente. O fingolimode, usado na esclerose múltipla, é um modulador de S1PR1 que internaliza o receptor: sem ele, o linfócito perde a capacidade de ler o gradiente e fica retido no linfonodo. O resultado laboratorial é uma linfopenia periférica marcante, sem destruição de linfócitos — as células estão vivas, apenas presas. O fármaco confirma o mecanismo pelo avesso: quem sai, sai porque foi puxado.
]

#mini-resumo[Em cadeia: órgão primário → sangue → HEV → órgão linfoide secundário → linfa → sangue de novo. Entrada pelo sangue via HEV, saída pela linfa, sem retorno ao primário — e a recirculação existe porque nenhum órgão guarda o repertório inteiro.]

#subtopico("2.5 — O que muda quando o linfócito é ativado")

Seria natural supor que o linfócito ativado passe a circular pelos mesmos endereços, só que mais rápido. É o contrário: ele troca de endereço. Quando uma perturbação da homeostasia num tecido gera sinais que chegam ao órgão linfoide secundário, aquele órgão sofre alterações que levam à ativação do linfócito específico. Esse linfócito ativado sai pela linfa e cai no sangue — até aí, o mesmo caminho. Mas ele não volta para o órgão linfoide secundário, e a razão é molecular: ele mudou o padrão de moléculas de adesão que expressava. Perdeu a chave da HEV e ganhou chaves novas.

Com as chaves novas, ele passa a procurar no organismo os pontos em que as células endoteliais anunciam "aqui houve uma perturbação da homeostasia" — exatamente as moléculas de adesão que o endotélio ativado expõe, como vimos em 1.3. É isso que permite a vigilância imunológica dos tecidos: há estágios de ativação em que o linfócito entra em praticamente qualquer tecido, patrulhando. Ele deixou de ser ingênuo e virou patrulheiro.

Há ainda um refinamento que o professor faz questão de marcar: a redistribuição não é tão aleatória quanto parece. O linfócito aprende com o órgão linfoide em que foi ativado. Quem foi ativado no MALT tende a recircular pelo MALT; quem foi ativado num linfonodo tende a recircular por linfonodos. Faz sentido funcional — o tipo de agressão esperada na mucosa não é o mesmo esperado em outros territórios, e é bom que a célula treinada para um cenário volte a patrulhar aquele cenário. O saldo estrutural do sistema é uma geração somática e aleatória do repertório, uma distribuição inicial quase aleatória pelos órgãos linfoides e uma redistribuição contínua, que dá ao sistema imune uma fluidez histológica e funcional. Nenhum órgão linfoide é uma peça fixa: ele é um ponto de passagem com composição mutável, e é por isso que prever com exatidão onde e quando uma resposta vai acontecer é tão difícil.

#figura-nebli("/figuras/imuno-02-organizacao-sistema-imune/slide-14.png",
  largura: 74%,
  legenda: [A circulação do linfócito ativado. O trajeto de saída é o mesmo — linfa e depois sangue —, mas o destino muda: em vez de voltar ao órgão linfoide secundário, ele procura tecidos onde o endotélio sinaliza perturbação.])

#mini-resumo[Em cadeia: ativação no órgão linfoide → troca do padrão de moléculas de adesão → perde o endereço da HEV → ganha endereço de endotélio inflamado → vigilância dos tecidos, com preferência pelo território onde foi ativado.]

#mapa-parte(
  parte: "PARTE II",
  centro: [Nascer isolado, encontrar circulando],
  nos: ((id: "2.1–2.2", titulo: "Órgãos primários", texto: [Timo e medula geram e selecionam o repertório longe do meio externo.]),
        (id: "2.3–2.4", titulo: "Secundários e HEV", texto: [Entrada pelo sangue através da HEV, saída sempre pela linfa.]),
        (id: "2.5", titulo: "Troca de endereço", texto: [Ativado, muda a adesão e passa a patrulhar tecidos perturbados.])),
  arestas: (("", "", [exportam para]), ("", "", [depois da ativação])),
  fecha-com: [Chegar ao órgão linfoide é metade do problema; o resto é a PARTE III.],
)

#parte-title("PARTE III — Dentro do órgão linfoide: como uma informação vira resposta")

#subtopico("3.1 — As condições estruturais: probabilidade tratada como estratégia")

O órgão linfoide secundário precisa cumprir duas condições estruturais antes de qualquer outra coisa. A primeira é fluxo contínuo de linfócitos: tem que haver entrada e saída o tempo todo, e tem que haver muito linfócito ali dentro a cada instante. A segunda é presença de células apresentadoras de antígeno em grande quantidade — o que faz sentido imediato, já que a própria seleção do repertório T dependeu da interação com essas células, e a função também vai depender.

Por que tanta gente? Porque isso aumenta a probabilidade de encontro entre o antígeno e o receptor clonal que o reconhece. Muito da resposta imune é, no fundo, estatística: qual é a chance de a célula rara certa esbarrar na molécula certa dentro de um prazo útil. É por isso que a arquitetura do órgão linfoide se parece com um mercado apinhado, e não com um arquivo organizado. E é também por isso que a vacinação funciona antes mesmo de qualquer consideração sobre memória: ao aumentar a frequência dos clones específicos, ela aumenta a probabilidade do encontro, e o encontro mais rápido produz resposta mais rápida.

#mini-resumo[Em uma frase: fluxo contínuo de linfócitos mais concentração alta de células apresentadoras existem para uma finalidade única — elevar a probabilidade de encontro entre um antígeno e o clone raro que o reconhece.]

#subtopico("3.2 — As três células apresentadoras e o que cada uma sabe fazer")

Já que a densidade de células apresentadoras é uma exigência estrutural, vale distinguir quem são elas, porque as três não são intercambiáveis. A #sigla("DC", [dendritic cell — célula dendrítica, a apresentadora profissional que ativa o linfócito T naïve]) é a principal, e o nome vem da forma: *dendrion*, em grego, é árvore, e a célula é um tronco cheio de ramos que se enfia entre as outras células e amplia enormemente a superfície de contato. Ela tem duas capacidades que nenhuma outra célula tem. A primeira é ativar o linfócito T naïve: se um linfócito saiu do timo, entrou num linfonodo e nunca viu antígeno, a única célula capaz de dar nele o pontapé inicial é a célula dendrítica. Depois desse primeiro contato, outras células podem reativá-lo e modular a resposta — mas o primeiro empurrão é dela.

A segunda capacidade é a apresentação cruzada, e ela merece ser destrinchada porque o nome esconde o mecanismo. Normalmente há dois canais separados: o que a célula *capturou de fora* é exibido num canal que diz "achei isto no meio extracelular", enquanto o que a célula *fabrica dentro de si* é exibido num canal que diz "isto está sendo produzido aqui dentro" — o segundo canal é o que denuncia uma célula infectada por vírus. A célula dendrítica quebra essa separação: ela captura um antígeno de fora, processa e o exibe no canal de dentro, isto é, em MHC de classe I, ativando linfócitos T citotóxicos. Para tornar concreto: o vírus da hepatite B infecta apenas o hepatócito. Sem apresentação cruzada, nenhuma célula dendrítica jamais estaria infectada e nenhuma resposta citotóxica poderia ser iniciada contra ele. Com ela, a dendrítica captura o vírus de fora, apresenta como se o fabricasse, e o linfócito T citotóxico sai dali calibrado para procurar hepatócitos infectados.

E há uma terceira propriedade que não é uma capacidade isolada, mas uma consequência do modo de captura: a dendrítica não captura só o antígeno, ela captura a paisagem molecular inteira em volta dele. Quando apresenta, ela apresenta também o contexto — e é esse contexto que empurra a resposta adquirida para um tipo ou outro. A plasticidade da resposta imune depende bastante disso.

O macrófago é a segunda apresentadora, e a divisão de trabalho entre ele e a dendrítica é geográfica. A apresentação inicial é feita no órgão linfoide pela dendrítica; quando o linfócito ativado sai e chega ao tecido onde está o problema, quem reapresenta o antígeno para ele é o macrófago, que é muito mais abundante nos tecidos. Além disso o macrófago é efetor: em estados ativados ele destrói com eficiência o que fagocita e modula vários fenômenos locais.

O linfócito B é a terceira, e é o caso curioso — uma célula que tem receptor clonal e ainda assim apresenta antígeno. A apresentação dele é seletiva, e a palavra é precisa. Dendrítica e macrófago são fagocíticos: capturam de forma inespecífica o que passa na frente deles. O linfócito B não fagocita; ele tem uma âncora de altíssima afinidade para segurar antígeno, que é a imunoglobulina de membrana. A constante de afinidade desse receptor pelo seu antígeno é cerca de dez mil vezes maior do que a afinidade com que a dendrítica ou o macrófago capturam coisas em geral. A consequência é decisiva: com muito antígeno disponível, a dendrítica captura melhor; com pouquíssimo antígeno, quem pega é o linfócito B específico. Ele captura, processa, apresenta — e essa apresentação é o que permite que ele converse intimamente com o linfócito T que enxerga o mesmo antígeno. Dessa conversa saem dois sinais: um que ativa o linfócito T e outro que ativa o próprio linfócito B a fazer aquilo que ele sabe fazer, que é anticorpo. Sem essa apresentação, a resposta humoral nunca seria específica nem dependente de T.

#figura-lateral("/figuras/imuno-02-organizacao-sistema-imune/slide-18.png",
  lado: "left",
  largura-figura: 40%,
  texto: [O elo molecular dessa conversa tem nome. Ao reconhecer o antígeno apresentado pelo linfócito B em MHC de classe II, o linfócito T auxiliar expressa CD40L, que se liga ao CD40 do linfócito B; junto com as citocinas que o T secreta, esse par é o sinal que autoriza o B a trocar a classe do anticorpo e a formar centro germinativo. É por isso que defeitos em CD40L produzem a síndrome de hiper-IgM — o B até produz IgM, mas nunca recebe a licença para trocar de classe.],
  legenda: [Célula dendrítica em cultura, interagindo com linfócitos: tronco e ramos, a forma que deu o nome.])

#mini-resumo[Em cadeia: dendrítica ativa o T naïve e faz apresentação cruzada → macrófago reapresenta no tecido e destrói → linfócito B captura antígeno escasso pela Ig de membrana e acopla a resposta humoral ao linfócito T.]

#subtopico("3.3 — A aferência: como a informação chega ao linfonodo, ao baço e ao MALT")

Ter muitas células não adianta se a informação não chegar. E a informação, aqui, não é só o antígeno: são as células apresentadoras que saíram do tecido, os antígenos em solução e os mediadores produzidos lá — o pacote inteiro que já chamamos de paisagem molecular. Cada órgão linfoide secundário resolve a aferência de um jeito, e a diferença tem consequência clínica direta.

O linfonodo recebe a informação pela linfa aferente, que chega do tecido drenado. A linfa entra, distribui a informação dentro do órgão e sai pelo vaso eferente. Os linfócitos, ao contrário, entram pelo sangue e atravessam a HEV. Isso vale a pena repetir porque é a fonte de confusão mais comum do tema: a informação entra pela linfa, os linfócitos entram pelo sangue, e ambos saem pela linfa.

O baço recebe a informação diretamente pelo sangue — não tem linfa aferente. Uma resposta imune montada no baço é, em geral, resposta a algo que já está circulando, o que costuma ser uma situação mais perigosa, porque o sangue espalha muito mais depressa do que a linfa, que precisa vencer estação por estação.

O MALT recebe a informação da luz da mucosa, e a solução anatômica é bonita. No epitélio que recobre o tecido linfoide associado à mucosa existe uma célula especializada, a célula M, cuja função é servir de porta: ela capta o material da luz e o transporta através de si mesma por transcitose, entregando-o ao tecido linfoide logo abaixo. E há um segundo caminho: em microscopia intravital de placas de Peyer vê-se células dendríticas emitindo prolongamentos que atravessam as junções entre as células epiteliais e amostram diretamente o conteúdo da luz, sem romper a barreira.

#figura-nebli("/figuras/imuno-02-organizacao-sistema-imune/slide-19.png",
  largura: 82%,
  legenda: [Três portas de entrada para a informação. No linfonodo ela vem pela linfa aferente; no baço, pelo sangue; no MALT, da luz da mucosa, via célula M e amostragem por células dendríticas.])

#clinica-box("O baço filtra o sangue — e quem perde o baço perde essa filtragem")[
  Como o baço é o órgão linfoide que amostra o sangue, ele é o principal responsável por depurar e responder a micro-organismos circulantes, especialmente os encapsulados, cuja cápsula de polissacarídeo dificulta a fagocitose sem opsonização. Ali residem, além disso, os linfócitos B de memória IgM que controlam pneumococo — descritos justamente em um dos artigos indicados como leitura complementar desta aula. O asplênico, cirúrgico ou funcional como na anemia falciforme, perde as duas coisas e passa a correr risco de sepse fulminante por #emph[Streptococcus pneumoniae], #emph[Haemophilus influenzae] tipo b e #emph[Neisseria meningitidis] — daí a vacinação obrigatória contra esses três antes da esplenectomia eletiva.
]

#mini-resumo[Linfonodo recebe informação pela linfa e linfócitos pelo sangue; baço recebe informação pelo sangue; MALT recebe da luz por célula M e por dendritos de DC que atravessam o epitélio.]

#subtopico("3.4 — A geografia interna: áreas T, folículos B e o centro germinativo")

Dentro de qualquer órgão linfoide secundário existem dois tipos de área, e o nome delas guarda a história do experimento que as revelou. Ao se fazer timectomia em um camundongo e olhar depois os órgãos linfoides secundários, certas regiões esvaziam de linfócitos — sobra o estroma, a rede reticular e os macrófagos, mas o linfócito some. Essas são as áreas timo-dependentes. Outras regiões continuam povoadas: são as áreas timo-independentes, que dependem dos linfócitos B — e cujo nome, historicamente, vem da bursa de Fabrício das aves, o órgão equivalente à nossa medula óssea.

A tradução anatômica é direta e vale memorizar por órgão. A área timo-dependente é a região paracortical no linfonodo, a bainha periarteriolar no baço e a área interfolicular no MALT. As áreas timo-independentes se organizam como bolinhas, os folículos linfoides, e é ali que moram os linfócitos B. Nos folículos existe ainda um tipo celular que confunde muita gente: a célula dendrítica folicular, ou #sigla("FDC", [follicular dendritic cell — célula dendrítica folicular, que retém antígeno intacto para os linfócitos B]).

#confusao-prevista(
  titulo: "Célula dendrítica folicular não é célula dendrítica",
  aluno_acha: [aluno junta as duas pelo nome e supõe que a FDC seja a mesma apresentadora profissional que ativa linfócito T, só que morando no folículo],
  mecanismo: [são células de origem, ontogenia e função diferentes; o nome só reflete a forma ramificada. A célula dendrítica processa o antígeno e o apresenta em MHC ao linfócito T — sem essa apresentação o receptor do T simplesmente não reconhece o antígeno. A FDC não apresenta em MHC: ela retém antígeno intacto na superfície, muitas vezes já ligado a anticorpo, e o oferece ao linfócito B, que reconhece antígeno nativo com ou sem intermediário. E ela vai liberando esse depósito por anos, funcionando como cápsula de liberação lenta — um dos mecanismos que sustentam a memória.],
)

Quando o órgão linfoide recebe o estímulo correto, cada compartimento responde à sua maneira. No folículo, o linfócito B que reconheceu o antígeno começa a proliferar e forma-se o centro germinativo: uma expansão clonal tão grande que o folículo estimulado fica muito maior que o folículo em repouso. É ali que a resposta de anticorpo é construída — e não apenas em quantidade: é no centro germinativo que ocorrem a hipermutação somática, que aumenta a afinidade do anticorpo, e a troca de classe, que muda o isotipo. Outros estímulos ativam preferencialmente as áreas timo-dependentes e produzem expansão clonal de linfócitos T. Quase sempre há um pouco das duas, mas costuma haver predomínio de uma — e saber qual predomina é informação clinicamente relevante, porque expansão de linfócito B significa produção de anticorpo, enquanto predomínio de expansão de T significa uma resposta de tipo celular.

Uma última nota sobre o folículo: há linfócitos T dentro dele, e não por acaso. A resposta do linfócito B ao antígeno proteico depende de ajuda de linfócito T — são os T foliculares auxiliares que, pelo par CD40L–CD40 e por citocinas, autorizam a hipermutação e a troca de classe.

#figura-nebli("/figuras/imuno-02-organizacao-sistema-imune/slide-20.png",
  largura: 80%,
  legenda: [A regionalização da expansão clonal. À esquerda, o folículo em repouso com a célula dendrítica folicular entre os linfócitos B; à direita, o mesmo folículo depois do estímulo correto, com o centro germinativo instalado.])

#mini-resumo[Em cadeia: timectomia esvazia certas áreas → áreas timo-dependentes (paracortical no linfonodo, periarteriolar no baço, interfolicular no MALT) → o resto são folículos B, com FDC retendo antígeno → estímulo correto no folículo → centro germinativo, hipermutação, troca de classe, anticorpo.]

#subtopico("3.5 — A eferência e o relógio da resposta")

Terminada a expansão, o produto precisa sair. O linfócito B ativado passa por uma série de transformações até virar plasmócito, a célula que efetivamente secreta anticorpo — e, curiosamente, ele já migra enquanto se transforma. Três destinos concentram esse trânsito: os cordões medulares do próprio linfonodo, a polpa vermelha do baço, ou a circulação, que o leva à medula óssea. É por isso que a medula óssea, embora seja um órgão linfoide primário, funciona também como órgão linfoide secundário: ela é uma das principais moradas dos plasmócitos de vida longa. A consequência clínica aparece na oncologia — o tumor maligno de plasmócitos quase sempre se manifesta como tumor de medula em vários pontos ao mesmo tempo, o mieloma múltiplo, e o nome descreve exatamente essa multiplicidade. Vale registrar a inversão que costuma passar batido: quem circula não é o plasmócito maduro, é o linfócito B ativado ainda em diferenciação; o plasmócito, quando pronto, já está instalado.

O linfócito T ativado segue o caminho já descrito na PARTE II: sai pela linfa, cai no sangue e procura o tecido perturbado.

Falta o relógio, e ele é surpreendentemente lento. A expansão clonal dentro do órgão linfoide secundário leva cerca de duas semanas até produzir uma resposta cheia e mensurável. Mais que isso: quando o sinal de alarme chega e o órgão é ativado, ele essencialmente fecha a porta de saída — entra linfa, mas por um a dois dias praticamente não sai linfócito. Depois desse período volta a sair muito linfócito, só que nenhum dos que estão saindo reconhece o antígeno que chegou; os clones específicos continuam retidos, em expansão, e só depois de cerca de duas semanas começam a ser liberados. É esse atraso que produz a janela imunológica — o intervalo em que o indivíduo já está infectado mas ainda não tem anticorpo detectável. Quanto mais sensível o método, mais cedo se detecta; mas sempre existe uma janela, e foi exatamente por isso que a segurança transfusional na epidemia de AIDS dependeu de testes cada vez mais sensíveis.

#mini-resumo[Em cadeia: B ativado migra enquanto vira plasmócito → cordões medulares, polpa vermelha ou medula óssea → T ativado sai pela linfa rumo ao tecido → e o relógio inteiro leva cerca de duas semanas, com o órgão retendo os clones específicos no início.]

#subtopico("3.6 — Resposta ou tolerância: o que a paisagem molecular decide")

Chegamos ao terceiro objetivo da aula, e ele exige desfazer uma dicotomia. O reconhecimento clonal dentro do órgão linfoide pode gerar dois desfechos: uma resposta efetora, que tenta eliminar aquilo, ou tolerância imunológica, que permite que aquela molécula persista sem ser atacada. A tentação é ler isso como uma chave de duas posições. Não é. Os dois fenômenos acontecem simultaneamente: mesmo quando o organismo responde contra uma bactéria, ele gera células que tentarão frear essa resposta; mesmo quando fica tolerante a um antígeno, ele gera alguns clones que tentariam eliminá-lo. O que se vê no paciente é o saldo desse equilíbrio, e não a vitória de uma das posições.

O que inclina o saldo é a paisagem molecular que chegou junto com o antígeno. Havendo lesão tecidual, a paisagem que chega ao órgão linfoide contém sinais de dano, e a tendência é resposta. Não havendo lesão, a paisagem continua chegando — porque sempre há fluxo de linfa, mesmo de um tecido saudável —, mas o que chega tende a gerar tolerância. Em uma frase: não é o antígeno sozinho que decide, é o antígeno mais o contexto em que ele chegou. Como o organismo detecta que houve lesão é assunto da próxima aula.

#mini-resumo[Em uma frase: antígeno com sinais de dano tende a gerar resposta, antígeno sem lesão tende a gerar tolerância — e as duas coisas são produzidas ao mesmo tempo, sendo o saldo o que se manifesta clinicamente.]

#mapa-parte(
  parte: "PARTE III",
  centro: [Informação vira resposta ou tolerância],
  nos: ((id: "3.1–3.3", titulo: "Encontro e aferência", texto: [Muitas apresentadoras; informação vinda da linfa, do sangue ou da luz.]),
        (id: "3.4", titulo: "Compartimentos", texto: [Áreas T, folículos B e centro germinativo após o estímulo correto.]),
        (id: "3.5–3.6", titulo: "Saída e saldo", texto: [Plasmócito e linfócito ativado saem; a paisagem decide o desfecho.])),
  arestas: (("", "", [distribuída em]), ("", "", [que produz])),
  fecha-com: [Falta explicar como cada célula acerta o endereço, e isso é a PARTE IV.],
)

#parte-title("PARTE IV — As moléculas que escrevem o endereço")

#subtopico("4.1 — Moléculas de adesão: uma conversa em etapas obrigatórias")

Toda a logística das PARTES II e III depende de uma pergunta prática: como uma célula que corre dentro de um vaso decide parar num ponto e não em outro? A resposta é que existem famílias de moléculas de adesão funcionando em sincronia, engajadas em sequência, e é a sequência que endereça.

A primeira conversa é feita pelas selectinas. O nome já diz o mecanismo: lectina é proteína com afinidade por carboidrato, e as selectinas se ligam a carboidratos do glicocálix — tanto no leucócito quanto no endotélio. São três, e a divisão é útil: a L-selectina fica no leucócito, a P-selectina é armazenada em grânulos do endotélio e da plaqueta e vai para a superfície em minutos, e a E-selectina é sintetizada pelo endotélio ativado por citocinas ao longo de horas. Como a ligação proteína-carboidrato é de baixa afinidade e se rompe com facilidade, o resultado físico não é a parada: é o rolamento. A célula desacelera aos trancos ao longo da parede.

A segunda conversa é feita pelas integrinas — heterodímeros de uma cadeia alfa e uma cadeia beta, que também mantêm a integridade dos tecidos e não servem apenas para distribuir células. As que usam a cadeia beta-2, cujo outro nome é CD18, são as integrinas leucocitárias, essenciais na migração de células do sangue para qualquer situação. Ativadas por quimiocina, elas mudam de conformação e passam de baixa para alta afinidade, e é aí que a célula rolando finalmente para de vez.

A terceira família é a superfamília das imunoglobulinas, e ela ganha esse nome por compartilhar o domínio da imunoglobulina — aquele arranjo de folhas beta pregueadas que protege a estrutura e ao mesmo tempo tolera variação, uma solução tão boa que outras moléculas que não são anticorpos a adotaram. Aqui entram #sigla("ICAM", [intercellular adhesion molecule — molécula de adesão intercelular, ligante endotelial das integrinas leucocitárias]), VCAM-1 e MAdCAM-1. Elas ficam no endotélio e são os ligantes com que as integrinas leucocitárias travam. Há ainda uma quarta família, de moléculas semelhantes a mucina — CD34, GlyCAM-1 e novamente MAdCAM-1 —, que são os ligantes carregados de carboidrato reconhecidos pelas selectinas; o termo adressina, de endereço, aparece justamente para elas.

Juntando as três primeiras em ordem, sai a cascata de extravasamento leucocitário: marginação, rolamento pelas selectinas, adesão firme pela integrina beta-2 sobre ICAM-1, e diapedese entre as células endoteliais, mediada por PECAM-1 — o que a palavra transmigração descreve.

#clinica-box("Deficiência de adesão leucocitária tipo 1: quando o rolamento não vira parada")[
  Um defeito na cadeia beta-2, o CD18, produz leucócitos que rolam normalmente mas nunca conseguem a adesão firme, e portanto não atravessam o endotélio. O quadro é caracteristicamente paradoxal: infecções bacterianas graves e de repetição, queda tardia do coto umbilical, e uma neutrofilia altíssima no sangue — os neutrófilos estão todos ali, apenas não conseguem sair do vaso. E como não chegam ao tecido, as lesões não formam pus. É a demonstração clínica de que rolar e parar são etapas moleculares distintas: perder só a segunda já basta para quebrar toda a defesa tecidual.
]

#mini-resumo[Em cadeia: selectina + carboidrato → rolamento → quimiocina ativa a integrina beta-2 (CD18) → adesão firme sobre ICAM-1 → diapedese via PECAM-1 = transmigração.]

#subtopico("4.2 — Quimiocinas: o gradiente que diz para onde ir")

Grudar, sozinho, não resolve — a célula precisa saber para onde ir depois de parar, e quem informa isso são as moléculas quimiotáticas. Historicamente as primeiras conhecidas foram os mediadores inflamatórios: proteínas do complemento, especialmente os fragmentos C3a e C5a; fatores lipídicos gerados na destruição de membranas, como leucotrienos, PAF e prostaglandinas; e fragmentos de proteínas da coagulação gerados a partir do plasma. As células têm receptores para tudo isso e migram no sentido da maior concentração.

Mais recentemente descreveu-se uma família dedicada: as quimiocinas, citocinas de baixo peso molecular, glicoproteínas cuja função é direcionar a migração celular. A nomenclatura parece confusa e fica simples quando se olha o critério: as famílias são definidas pelo arranjo das cisteínas na extremidade da molécula. Duas cisteínas separadas por um aminoácido qualquer definem a família CXC; duas cisteínas adjacentes definem a família CC; duas cisteínas separadas por três aminoácidos definem CX3C; e uma única cisteína define XC. As duas últimas têm pouquíssimos membros conhecidos. Ao nome da família acrescenta-se L para o ligante e R para o receptor — CXCL8 é uma quimiocina, CXCR1 é um receptor. O detalhe que costuma escapar é que a correspondência não é um-para-um: quimiocinas e receptores são degenerados, um ligante serve a vários receptores e vice-versa, e é a combinação em que aparecem, e não uma chave única, que endereça a migração. Alguns exemplos fixam a lógica: CXCL8, também chamada interleucina-8 por ter sido descrita antes como citocina, é o recrutador clássico de neutrófilo; CCL2, ou MCP-1, recruta monócito; CX3CL1 é a fractalquina; XCL1 é a linfotactina. E vale notar que direcionar migração não é a única função — as quimiocinas também organizam a arquitetura do tecido, porque vão dando outros sinais enquanto guiam a célula.

#mini-resumo[Em cadeia: cisteínas na extremidade definem a família (CXC, CC, CX3C, XC) → L é ligante, R é receptor → interação degenerada, não um-para-um → CXCL8 recruta neutrófilo, CCL2 recruta monócito, e o gradiente aponta a direção.]

#subtopico("4.3 — Revendo o sistema inteiro em um só esquema")

Com adesão e quimiotaxia na mão, dá para reler o sistema todo em uma única passagem, e é isso que o esquema de fechamento da aula faz. Reconhecimento do rompimento da homeostasia gera alarme. O alarme produz recrutamento para o tecido lesado, e o socorro vem do sangue em duas formas: substâncias plasmáticas, que extravasam com o aumento da permeabilidade vascular, e células, que migram pela cascata de adesão que acabamos de ver. Substâncias mais células caracterizam a resposta inata, que tenta restaurar a homeostasia ali mesmo.

Ao mesmo tempo, o extravasamento de plasma e o aumento da pressão tecidual empurram para os vasos linfáticos tudo o que estava naquele tecido — não apenas o antígeno estranho, mas a paisagem molecular inteira. Esse material chega ao órgão linfoide que drena aquela região, onde ocorre o reconhecimento clonal, e dele saem resposta efetora e tolerância, nas proporções que a paisagem determinar. Isso é a resposta adquirida.

O fecho do circuito é o detalhe mais bonito do esquema: os produtos da resposta adquirida — anticorpos que vão para o plasma e células que vão para o sangue — passam a integrar aquilo que será recrutado no próximo episódio de lesão. Ou seja, numa segunda agressão a resposta inata já chega misturada com produtos da adquirida anterior. É exatamente isso que uma vacina fabrica: fazer com que, no primeiro alarme, já existam células e produtos plasmáticos capazes de lidar com aquele agente de maneira específica e mais eficiente.

#figura-nebli("/figuras/imuno-02-organizacao-sistema-imune/slide-24.png",
  largura: 84%,
  legenda: [O esquema completo. À esquerda o eixo do tecido, com alarme e recrutamento; embaixo o eixo do órgão linfoide, com aferência da paisagem molecular e reconhecimento clonal; à direita, as setas tracejadas que devolvem os produtos da resposta adquirida ao recrutamento inato do episódio seguinte.])

#mini-resumo[Em cadeia: reconhecimento → alarme → recrutamento de substâncias plasmáticas e células (inata) → paisagem molecular drenada ao órgão linfoide → reconhecimento clonal → resposta e tolerância (adquirida) → produtos da adquirida realimentam o recrutamento do próximo episódio.]

#mapa-parte(
  parte: "PARTE IV",
  centro: [O endereço escrito em moléculas],
  nos: ((id: "4.1", titulo: "Adesão em etapas", texto: [Selectina faz rolar; integrina beta-2 trava firme sobre ICAM-1.]),
        (id: "4.2", titulo: "Quimiocinas", texto: [Gradiente das famílias CXC, CC, CX3C e XC aponta a direção.]),
        (id: "4.3", titulo: "Circuito fechado", texto: [Produtos da adquirida realimentam o recrutamento do próximo episódio.])),
  arestas: (("", "", [seguida de]), ("", "", [tudo isso fecha])),
  fecha-com: [Do alarme no tecido ao anticorpo no plasma, um circuito endereçado molecularmente.],
)

// Conclusão integradora — 4 camadas: (1) princípio unificador; (2) mecanismo nuclear;
// (3) clínica retomada (LAD-1); (4) projeção para a próxima aula.
#conclusao-box[
  Um único princípio atravessa as quatro PARTES: como o sistema imune gera seu repertório ao acaso e o distribui clonalmente, ele resolve por logística um problema que não pode resolver por previsão. Nenhuma célula sabe de antemão o que vai encontrar, então o sistema constrói lugares de encontro e mantém suas células em movimento perpétuo entre eles. O mecanismo nuclear que sustenta essa logística é o endereçamento molecular: o linfócito naïve entra no órgão linfoide secundário pela HEV porque expressa L-selectina e CCR7, sai pela linfa porque lê o gradiente de S1P, e depois de ativado troca esse conjunto de moléculas por outro, que o faz parar apenas onde o endotélio anuncia perturbação — e é a mesma cascata de rolamento e adesão firme que leva neutrófilo e monócito ao tecido inflamado. A deficiência de adesão leucocitária tipo 1 mostra o preço de perder um único degrau dessa escada: com o CD18 defeituoso, o neutrófilo rola mas não adere, acumula-se aos milhares no sangue, não chega ao tecido, e o paciente faz infecções graves sem formar pus. Fica de pé, para a próxima aula, a pergunta que este resumo deixou explicitamente em aberto: a paisagem molecular decide entre resposta e tolerância conforme haja ou não lesão — mas como, molecularmente, o organismo reconhece que houve lesão? É por aí que a imunidade inata será destrinchada a seguir.
]
