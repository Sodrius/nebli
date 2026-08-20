#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Quatro máquinas, quatro físicas completamente diferentes, um único objetivo: descobrir o que está dentro do corpo sem abrir o corpo. A radiografia atravessa o paciente com fótons e registra o que sobrou do feixe do outro lado. O ultrassom encosta na pele, grita em frequência inaudível e escuta o eco voltar. A tomografia faz o mesmo que a radiografia, só que girando em torno do paciente e deixando o computador remontar o volume. A ressonância não manda nada atravessar nada: ela alinha os prótons de hidrogênio do próprio corpo num ímã gigante, os desestabiliza com uma onda de rádio e escuta a energia que eles devolvem ao voltar para o lugar. Cada uma dessas físicas define o que a máquina consegue ver, o que ela é cega para ver, quanto tempo demora e a que preço biológico. É por isso que os métodos *não se substituem*: eles se complementam. A vesícula que o ultrassom mostra com clareza é a mesma que a tomografia mal distingue; o osso que a tomografia desenha em detalhe é o mesmo que apaga o ultrassom. Este capítulo percorre os quatro na ordem em que foram inventados — radiografia, ultrassom, tomografia, ressonância —, e a régua é sempre a mesma: entender *o que forma o sinal* para prever *o que a imagem pode e não pode mostrar*.
]

#parte-title("PARTE I — Radiografia: a sombra que soma tudo", primeira: true)

#subtopico("1.1 — O tubo de raios X e a natureza do feixe")

O raio X é uma onda eletromagnética de alta energia, da mesma família da luz visível e das ondas de rádio, mas muito acima delas na escala de frequência. Enquanto a luz visível tem comprimento de onda na casa dos centésimos de milésimo de milímetro, o raio X trabalha na ordem de $10^(-12)$ metro, com frequência da ordem de $10^(16)$ hertz. Essa posição no espectro é o que decide tudo o que vem depois: um pacote de energia tão concentrado atravessa matéria que a luz visível não atravessa, e ao atravessar consegue arrancar elétrons dos átomos que encontra pelo caminho. Guardar a vizinhança ajuda: logo abaixo do raio X, em energia, está o ultravioleta; logo acima está a radiação gama, que costuma vir do núcleo de elementos instáveis. O raio X ocupa a faixa em que a energia é alta o bastante para atravessar o corpo, mas ainda baixa o bastante para ser produzida por um aparelho de bancada.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-08.png",
  largura: 72%,
  legenda: [O espectro eletromagnético lido da direita para a esquerda: ondas de rádio, infravermelho, luz visível (400–750 nm), ultravioleta, raios X, raios gama. Repare que *energia cresce* enquanto o *comprimento de onda encolhe* — as duas setas apontam em sentidos opostos. O raio X está do lado energético o suficiente para ionizar, e é dessa posição no espectro que decorrem tanto a utilidade diagnóstica quanto o risco biológico.])

Essa energia toda precisa ser fabricada, e é aqui que a natureza artificial do raio X médico se separa da radiação natural que nos atinge o tempo todo. Dentro do tubo há dois eletrodos separados por vácuo, com uma diferença de potencial aplicada entre eles. Um dos eletrodos é aquecido até liberar elétrons — o filamento incandescente "ferve" elétrons para fora do metal. Esses elétrons livres são então acelerados violentamente pela diferença de potencial em direção ao outro eletrodo, o alvo. Ao se chocarem contra o alvo, os elétrons freiam de forma abrupta e interagem com os átomos do metal, e a energia cinética que eles perdem nesse freio reaparece como onda eletromagnética. É essa onda que sai do tubo. Repare no encadeamento, porque ele explica uma propriedade prática decisiva: *elétrons acelerados → freio no alvo → fótons de raio X*. Nenhum elétron atravessa o paciente; o que atravessa é o fóton produzido no freio.

Daí decorre a diferença mais importante entre o aparelho de raio X e um material radioativo. O radionuclídeo emite porque seu núcleo é instável e continuará emitindo enquanto existir, independentemente do que se faça com ele. O tubo de raio X emite *apenas enquanto está ligado e acionado*. Desligou o disparo, cessou a emissão — não sobra radiação residual na sala, no aparelho ou no paciente. Um paciente que acabou de fazer uma radiografia não é uma fonte de radiação, e não há sentido em afastar dele visitas ou profissionais.

#confusao-prevista(
  titulo: "O aparelho não fica radioativo",
  aluno_acha: [que o equipamento de raio X, por emitir radiação, guarda alguma radioatividade depois do exame — e que o paciente irradiado "carrega" radiação consigo.],
  mecanismo: [a emissão depende de energia elétrica aplicada em tempo real. Sem diferença de potencial, não há elétron acelerado; sem elétron acelerado, não há freio no alvo; sem freio, não há fóton. A produção é artificial e instantânea, ao contrário do radionuclídeo, cuja instabilidade nuclear independe de qualquer acionamento.],
)

Só que um tubo de vidro emitindo em todas as direções seria um desastre: a maior parte da energia se perderia pelas paredes e irradiaria a sala inteira. Por isso o tubo é montado dentro de uma caixa de #termo-nota[chumbo][metal de número atômico muito alto, usado como blindagem porque absorve fótons de raio X com grande eficiência], que absorve a emissão em todas as direções menos uma: há uma abertura por onde o feixe útil escapa, colimado em direção ao paciente. A geometria do exame é então simples de descrever e vale fixar na ordem certa — *fonte, paciente, detector*. O paciente fica no meio. Do outro lado, o que recebe o feixe residual era historicamente um filme fotográfico dentro de um chassi; hoje é um detector digital que converte o feixe em sinal elétrico e envia a imagem direto ao computador. O que mudou nas últimas décadas foi o detector, não a física do que acontece dentro do paciente.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-12.png",
  largura: 62%,
  legenda: [A geometria canônica do exame: o tubo acima, o feixe colimado descendo em leque, o paciente atravessado e o detector logo abaixo dele. Note que o feixe *diverge* a partir de um ponto — essa divergência é o que vai gerar a magnificação estudada em 1.3. A imagem não é uma projeção de raios paralelos; é a sombra de uma lanterna pontual.])

#mini-resumo[Elétrons são fervidos de um eletrodo, acelerados por diferença de potencial e freados no alvo; a energia do freio vira fóton de raio X. Emissão só com o aparelho acionado — o tubo não é radioativo.]

#subtopico("1.2 — As cinco densidades radiológicas")

O feixe que sai do tubo é razoavelmente uniforme; o que chega ao detector não é. Entre um ponto e outro, o feixe atravessou materiais diferentes e chegou do outro lado com intensidades diferentes — e é exatamente essa diferença que vira imagem. Onde muito fóton chegou, o detector registra muito sinal e o ponto é escuro; onde pouco fóton chegou, o ponto é claro. Toda a leitura de uma radiografia depende dessa convenção, que a rigor é uma escolha e não uma lei: radiotransparente aparece escuro, radiopaco aparece claro. Os equipamentos modernos permitem inverter a escala; o padrão adotado universalmente é este.

Duas coisas decidem quanto um material atenua o feixe: a *espessura* atravessada e a *capacidade de absorção* daquele material. A espessura é intuitiva — mais material no caminho, mais fótons absorvidos. A capacidade de absorção é o ponto que costuma escapar: ela depende fortemente do número atômico dos elementos que compõem o tecido. Átomos com muitos prótons carregam muitos elétrons ao redor, e são os elétrons que interceptam os fótons. Por isso o cálcio do osso, com número atômico bem acima do carbono e do oxigênio dos tecidos moles, atenua desproporcionalmente mais; e por isso o metal de uma prótese, com número atômico ainda maior, atenua mais que qualquer coisa biológica.

Da combinação dessas duas variáveis nasce a escala clássica de cinco degraus, do mais radiotransparente ao mais radiopaco: *ar, gordura, água, cálcio e metal*. O ar quase não atenua e por isso os campos pulmonares são pretos. A gordura atenua um pouco mais. A água — e aqui está a chave prática — engloba muito mais coisa do que parece: músculo, sangue, fígado, rim, baço, líquido e vísceras se comportam essencialmente como água na escala radiográfica, porque têm composição elementar muito parecida. O cálcio dá o branco do osso e das calcificações. O metal satura o branco.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-17.png",
  largura: 74%,
  legenda: [Os cinco degraus demonstrados num único objeto. No ovo radiografado: a câmara de *ar* no polo superior aparece quase preta; a *casca*, de carbonato de cálcio, é o anel branco; a *clara* é praticamente água; e a *gema*, rica em lipídio, é discretamente mais escura que a clara. Repare que o contorno da gema é visível justamente porque gordura e água, apesar de próximas, não são idênticas — é uma diferença pequena, mas suficiente.])

O exemplo do ovo antecipa a limitação central do método. Gordura e água estão a um degrau de distância uma da outra, e o olho só as separa com atenção e em condições favoráveis. Dentro do abdome, onde fígado, baço, pâncreas, alças intestinais, veia cava e músculo psoas se acotovelam com composições quase idênticas, essa diferença some. Não é que a radiografia de abdome seja um exame ruim; é que ela é *cega para diferenças de densidade que não existem*. Onde há contraste natural, ela é excelente — e o tórax é o caso paradigmático, porque ali convivem lado a lado ar (pulmão), água (coração, vasos e mediastino) e cálcio (costelas e coluna), três degraus da escala num só campo de visão. O mesmo raciocínio explica por que o intestino aparece bem quando distendido por gás: o gás cria uma interface artificial dentro de uma região que, de outro modo, seria uma massa homogênea de densidade de água.

#mini-resumo[A atenuação depende da espessura e do número atômico. Cinco degraus: ar, gordura, água, cálcio, metal. Onde os degraus se repetem, a radiografia perde a informação — no tórax eles convivem, no abdome não.]

#subtopico("1.3 — Projeção: sobreposição, magnificação, PA × AP")

A analogia mais honesta para uma radiografia é a fotografia. Ambas pegam um objeto de três dimensões e o registram em duas — e, ao fazê-lo, sacrificam uma dimensão inteira. A diferença é que a fotografia registra a luz refletida pela superfície e a radiografia registra o feixe que atravessou o volume inteiro. Isso tem uma consequência que não existe na fotografia: tudo o que estava alinhado ao longo do trajeto do feixe é somado e impresso no mesmo ponto da imagem. Uma pedra na frente e outra atrás, alinhadas com o feixe, produzem uma única mancha. A radiografia não é uma foto do interior; é uma *soma projetada* do interior.

Pense na caixa que o professor usa como modelo: uma caixa com três eixos — transversal, ântero-posterior e profundidade — contendo pedras, sementes e blocos de resina em posições variadas. Ao radiografar a caixa de cima para baixo, você conserva o eixo transversal e o ântero-posterior, mas perde a profundidade: não dá para dizer se um objeto está no fundo ou perto da tampa. Ao radiografar a mesma caixa de lado, você recupera a profundidade e perde a separação entre frente e trás. Sempre se perde um eixo — e a única forma de recuperar a informação é fazer uma segunda incidência ortogonal à primeira.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-25.png",
  largura: 66%,
  legenda: [A caixa radiografada "de cima": sobram o eixo transversal e o ântero-posterior; a *profundidade* desapareceu. Objetos empilhados em profundidades diferentes se projetam no mesmo plano e se somam. É o mesmo que acontece quando se olha uma radiografia de tórax em incidência única.])

Traduzindo para o paciente: numa radiografia de tórax em incidência frontal, uma opacidade branca no campo pulmonar pode estar na pele do dorso, dentro do parênquima ou na pele anterior — a imagem não distingue. Só a incidência em perfil, que acrescenta o eixo ântero-posterior, permite localizar a lesão em profundidade. Por isso o padrão de solicitação em situação ambulatorial é *duas incidências*, e por isso o pedido de uma incidência só, comum na urgência, precisa ser feito com consciência de que ele responde menos. Em ossos, a regra é ainda mais explícita: certas fraturas só aparecem em angulações específicas, e o pedido precisa descrever qual incidência se quer.

Há um segundo efeito da geometria projetiva, mais sutil e clinicamente carregado. O feixe sai de um ponto e diverge, como a luz de uma lanterna. Uma sombra projetada por lanterna cresce quando o objeto se afasta do anteparo e encolhe quando encosta nele. O mesmo vale aqui: quanto mais longe do detector estiver a estrutura, maior ela é desenhada na imagem. Isso se chama #termo-nota[magnificação][ampliação aparente de uma estrutura na radiografia, proporcional à sua distância do detector, causada pela divergência do feixe a partir de uma fonte pontual], e duas pedras do mesmo tamanho em alturas diferentes dentro da caixa saem com tamanhos diferentes na imagem.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-33.png",
  largura: 70%,
  legenda: [A mesma caixa em perfil. As três esferas têm tamanho real semelhante, mas na incidência frontal apareceram com diâmetros diferentes: a que estava mais próxima do detector saiu menor, a mais afastada saiu ampliada. Guardar a regra na forma causal: *distância maior até o detector → sombra maior*.])

É essa física que decide a convenção da radiografia de tórax. Na incidência #termo-nota[posteroanterior][incidência em que o feixe entra pelo dorso e sai pelo tórax anterior, com o paciente de pé e o peito encostado no detector] o feixe entra pelas costas e o paciente encosta a parede anterior do tórax no detector. Como o coração é uma estrutura anterior no mediastino, ele fica quase colado ao detector e magnifica pouco: a silhueta cardíaca sai com dimensões próximas das reais. Se a mesma radiografia for feita em incidência anteroposterior — feixe entrando pela frente, detector nas costas —, o coração se afasta do detector e sua sombra cresce artificialmente.

#atencao-box("Coração aumentado que não está aumentado", [
  A radiografia de tórax feita no leito é, por necessidade, anteroposterior: o paciente acamado não consegue ficar de pé com o peito no detector, e o chassi é colocado sob as costas. Nessa geometria, o coração se afasta do detector e sua silhueta é ampliada. Ler o índice cardiotorácico de um exame de leito como se fosse um exame ortostático leva ao diagnóstico falso de cardiomegalia — e, a partir dele, a uma investigação de insuficiência cardíaca que não precisava existir. Antes de comentar o tamanho do coração, verifique a incidência: em incidência anteroposterior, o aumento pode ser inteiramente geométrico.
])

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-35.png",
  largura: 76%,
  legenda: [À esquerda, incidência posteroanterior: coração próximo ao detector, silhueta fiel, escápulas projetadas para fora dos campos pulmonares. À direita, incidência anteroposterior: a mesma silhueta cardíaca aparece mais larga, e a magnificação é geométrica, não patológica. A diferença entre as duas imagens não está no paciente — está na distância do coração ao detector.])

Uma última convenção, que vale para todos os métodos daqui em diante: a imagem é apresentada como se o observador estivesse de frente para o paciente. O lado *direito do paciente* aparece à *esquerda da tela*. Isso vale para radiografia, tomografia e ressonância, e é o primeiro reflexo a automatizar diante de qualquer exame.

#subtopico("1.4 — Sinal da silhueta e o contraste exógeno")

Fixadas as cinco densidades, falta o princípio que transforma essa escala em leitura de imagem: um contorno só existe quando há diferença de densidade *entre estruturas vizinhas*. Um objeto não se torna visível porque é grande, nem porque é denso em termos absolutos — ele se torna visível porque o que está encostado nele atenua o feixe de maneira diferente. Perde-se o contorno no instante em que a vizinhança se iguala.

A demonstração mais limpa disso é o experimento das pedras em cimento. Três compartimentos da caixa contêm exatamente a mesma pedra; o que varia é a quantidade de cimento em volta. No compartimento com pouco cimento a pedra é nítida; à medida que o cimento aumenta e envolve a pedra com material de atenuação parecida, o contorno vai se apagando até a pedra desaparecer — sem que a pedra tenha mudado de tamanho, forma ou composição.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-39.png",
  largura: 76%,
  legenda: [À esquerda, a caixa aberta: os compartimentos contêm pedras equivalentes com quantidades crescentes de cimento em volta. À direita, a radiografia: a pedra que está cercada de material de densidade semelhante *perde o contorno*, enquanto a que faz interface com ar continua nítida (destaque em ciano). A regra a levar: densidades semelhantes encostadas apagam o contorno; densidades semelhantes separadas o mantêm.])

O corpo repete esse experimento o tempo todo. A aorta é o exemplo do professor e vale reconstruí-lo: no tórax, ela é desenhada com clareza como uma sombra tubular, porque está cercada de pulmão — ou seja, de ar. A mesma aorta continua abaixo do diafragma, com o mesmo calibre e a mesma parede; e no raio X de abdome ela simplesmente não aparece. Não mudou o vaso; mudou a vizinhança, que passou a ser gordura, músculo e vísceras, todos na faixa de densidade da água.

Levado à clínica, esse princípio recebe nome próprio: #termo-nota[sinal da silhueta][perda do contorno de uma estrutura quando um processo de densidade semelhante encosta anatomicamente nela; permite localizar a lesão pelo contorno que desaparece]. Na pneumonia, os alvéolos que continham ar passam a conter exsudato. A área que era preta fica clara, porque o líquido atenua como água. E aí o achado ganha valor topográfico: se essa consolidação está em contato anatômico com a borda do coração, a borda desaparece; se está em outro plano, sem contato, a borda cardíaca permanece nítida mesmo com a consolidação bem visível ao lado.

#clinica-box("Onde está a pneumonia, lida pelo contorno que sumiu", [
  Um paciente com febre, tosse e radiografia de tórax mostrando opacidade no terço inferior do hemitórax direito. Se a *borda direita do coração* estiver apagada, o processo está em contato com o átrio direito — ou seja, no lobo médio, que é anterior. Se a borda cardíaca estiver preservada e o que desaparecer for a *cúpula diafragmática*, o processo está no lobo inferior, que é posterior. A cadeia é inteiramente mecanística: exsudato substitui ar → densidade sobe de "ar" para "água" → a interface com a estrutura vizinha de densidade de água some → o contorno desaparece exatamente onde há contato anatômico. Localizar a pneumonia por qual contorno sumiu é mais confiável, numa incidência única, do que estimar profundidade a olho.
])

Quando a natureza não fornece a diferença de densidade, ela pode ser criada. É essa a função do meio de contraste: introduzir num compartimento um material de número atômico alto, que atenue muito mais que o tecido em volta, e assim fabricar uma interface onde não havia. Dois materiais dominam o uso radiográfico, e a diferença entre eles é farmacocinética, não óptica. O *bário* é uma suspensão que o organismo não absorve nem metaboliza; ele percorre a luz do tubo digestório e é eliminado intacto. Justamente por não ser absorvido, seu uso é restrito à luz intestinal — e foi ali que, por décadas, ele revelou a mucosa do estômago e do intestino, delineando úlceras, tumores e alterações de parede da doença inflamatória intestinal. O *iodo*, ao contrário, é metabolizado e eliminado pelo rim, o que permite injetá-lo dentro do vaso. Daí sua aplicação central: opacificar a luz vascular e desenhar a árvore arterial numa angiografia.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-19.png",
  largura: 68%,
  legenda: [Contraste criando interface onde não havia. À esquerda, bário preenchendo a luz do tubo digestório: o que era uma massa homogênea de densidade de água vira um molde branco da mucosa. À direita, iodo intravascular numa angiografia cerebral: os vasos, invisíveis no exame simples, aparecem desenhados um a um. Em ambos os casos o contraste não revelou uma estrutura nova — ele emprestou atenuação a um compartimento.])

#mini-resumo[Contorno é fenômeno de vizinhança: densidades iguais encostadas se apagam. O contraste exógeno fabrica a diferença que faltava — bário fica na luz do tubo digestório, iodo pode entrar no vaso.]

#subtopico("1.5 — Radiação ionizante: efeito direto, indireto e proteção")

A mesma energia que torna o raio X útil é a que o torna perigoso, e as duas coisas vêm exatamente do mesmo mecanismo. Um fóton com energia suficiente, ao atravessar a matéria, pode arrancar um elétron de um átomo — e é isso, literalmente, que a palavra *ionizante* descreve. O átomo que perde um elétron deixa de ter suas ligações químicas estáveis, e a molécula da qual ele fazia parte pode se romper. Quando essa molécula é o #sigla("DNA", [ácido desoxirribonucleico — molécula que guarda a informação genética da célula]), as consequências ganham escala biológica.

O dano acontece por dois caminhos, e a proporção entre eles surpreende. O *efeito direto* é o fóton interagindo com a própria molécula biológica de interesse, quebrando a fita de DNA na hora. O *efeito indireto* é o fóton interagindo com uma molécula de água — a mais abundante da célula —, quebrando-a e gerando radicais livres, que por sua vez atacam quimicamente o DNA. Como o conteúdo celular é majoritariamente água, o efeito indireto responde pela maior parte do dano em tecido vivo. Diante da lesão, a célula tem três destinos possíveis: reparar corretamente e seguir; reparar de modo imperfeito, fixando uma mutação que altera o comportamento celular; ou acumular dano suficiente para morrer.

Esse mesmo conjunto de eventos pode ser desejado. Na radioterapia, a dose é deliberadamente concentrada sobre um tumor exatamente para provocar dano irreparável em células que se dividem muito e reparam mal. A física é a mesma; muda a intenção e muda a dose. No exame de imagem, ao contrário, o dano é puro efeito colateral: quer-se apenas a informação, e todo dano é perda líquida.

Um ponto costuma ser mal compreendido e vale explicitar. Nem todo efeito da radiação é proporcional à dose. Há efeitos que só aparecem acima de um limiar e cuja gravidade cresce com a dose — queimadura de pele, depilação, catarata. Mas existem também os *efeitos estocásticos*, dos quais a indução de neoplasia é o exemplo maior: neles não há limiar conhecido, e o que a dose aumenta é a *probabilidade* do evento, não a sua gravidade. Como essa probabilidade se acumula ao longo da vida de forma silenciosa, cada exame acrescenta um risco pequeno que se soma aos anteriores. Daí a lógica da proteção radiológica não ser apenas o avental de chumbo: a primeira e mais poderosa medida de proteção é *não realizar o exame desnecessário*, e essa decisão pertence a quem solicita. Depois dela vêm a otimização técnica, a blindagem e a limitação do campo irradiado. O raciocínio se resume a uma pergunta prática: a informação que este exame vai acrescentar muda a conduta o suficiente para justificar a dose que ele entrega.

Feita a radiografia por inteiro — como o feixe nasce, o que decide o cinza, o que a projeção perde e o que ela custa —, o passo natural é examinar um método que resolve dois desses problemas de uma vez. O ultrassom não usa radiação ionizante e não projeta: ele corta. Como ele faz isso é o assunto da próxima parte.

#parte-title("PARTE II — Ultrassonografia: a imagem feita de ecos")

#subtopico("2.1 — Onda mecânica, transdutor piezoelétrico e o eco que volta")

O ultrassom pertence a uma categoria física inteiramente diferente da do raio X, e essa diferença é a origem de todas as suas vantagens e de todos os seus limites. Som não é onda eletromagnética: é *onda mecânica*, isto é, uma vibração que se propaga empurrando e comprimindo as partículas do meio, uma passando o movimento à seguinte. Consequência imediata e não negociável: sem meio material, não há propagação. O raio X atravessa o vácuo; o som não atravessa. O prefixo "ultra" apenas indica que a frequência empregada está acima de vinte mil hertz, o teto da audição humana — os transdutores médicos trabalham na casa dos milhões de hertz. Não há fóton, não há ionização, não há dano ao ácido nucleico por esse mecanismo. É por isso que o ultrassom é o método de escolha na gestante e na criança, e que o exame pode ser repetido quantas vezes for clinicamente útil.

O dispositivo que gera e escuta esse som é o *transdutor*, e ele ocupa no ultrassom o mesmo lugar central que o tubo ocupa no raio X. Na sua extremidade há um material #termo-nota[piezoelétrico][cerâmica ou cristal que se deforma quando recebe corrente elétrica e, inversamente, gera corrente quando é deformado por uma onda mecânica]. A palavra descreve exatamente a propriedade: pressão vira eletricidade e eletricidade vira pressão. Aplicado um estímulo elétrico, o cristal se deforma bruscamente e essa deformação empurra o meio adiante, criando a onda sonora. E o mesmo material faz o caminho inverso: quando uma onda que voltou o atinge, ele se deforma de novo e gera um pulso elétrico que a máquina lê. É uma conversão de mão dupla, e é essa reversibilidade que torna o transdutor emissor e receptor ao mesmo tempo.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-53.png",
  largura: 60%,
  legenda: [O transdutor convexo, com a face de contato onde ficam os elementos piezoelétricos. A cadeia a memorizar percorre dois sentidos: *estímulo elétrico → deformação do cristal → onda sonora que entra no paciente*; e, no retorno, *eco que chega → deformação do cristal → corrente elétrica → sinal para o computador*.])

Na prática, não há um único cristal, e sim um arranjo com muitos elementos organizados em fila ou em matriz. Parte deles emite enquanto outra parte escuta, e a função pode alternar entre eles — o que nenhum elemento consegue é emitir e receber no mesmo instante, porque a deformação da emissão sobrepujaria o sinal minúsculo do eco. O ciclo, portanto, é sempre pulsar e esperar.

O que acontece entre pulsar e escutar define a imagem. A onda entra no corpo e, em cada interface entre meios de propriedades acústicas diferentes, parte dela é refletida de volta e parte segue adiante. Não é uma reflexão única no fim do trajeto: é uma sequência de reflexões parciais, em muitos níveis de profundidade, e cada uma retorna ao transdutor num tempo próprio. O aparelho usa esse tempo de retorno para calcular a que distância está a interface que gerou o eco, e usa a intensidade do eco para decidir o brilho do ponto correspondente. Distância pelo tempo, brilho pela intensidade — a imagem é montada ponto a ponto a partir desses dois dados.

Falta nomear a propriedade que decide *quanto* de cada onda volta, porque ela vai reaparecer em todos os fenômenos da parte. Cada meio tem uma #termo-nota[impedância acústica][resistência que um meio oferece à passagem da onda sonora; produto da densidade do meio pela velocidade do som nele] própria, e o que determina a intensidade da reflexão numa interface não é o valor absoluto de nenhum dos dois lados, e sim a *diferença* entre eles. Interfaces entre meios parecidos — fígado e rim, músculo e gordura — refletem uma fração pequena do feixe e deixam a maior parte seguir adiante, o que permite formar imagem em profundidade. Interfaces com diferença extrema, como tecido contra ar ou tecido contra osso, refletem quase tudo e barram o feixe ali mesmo. Guardar isso resolve de uma vez três fatos que pareceriam desconexos: por que o gel é indispensável, por que o pulmão aerado e as alças distendidas são barreira intransponível, e por que um cálculo projeta sombra atrás de si.

#confusao-prevista(
  titulo: "O gel não é lubrificante",
  aluno_acha: [que o gel serve para o transdutor deslizar com conforto sobre a pele.],
  mecanismo: [entre a face do transdutor e a pele existiria uma película de ar, e a diferença de propriedades acústicas entre ar e tecido é tão grande que praticamente todo o feixe seria refletido logo na entrada, sem chegar a estrutura nenhuma. O gel preenche esse espaço com um meio de propriedades próximas às do tecido e permite que a onda entre no corpo. Sem gel não há imagem ruim: não há imagem.],
)

#mini-resumo[Onda mecânica precisa de meio — daí o gel. O cristal piezoelétrico converte eletricidade em som e som em eletricidade. A profundidade vem do tempo de retorno do eco; o brilho, da intensidade.]

#subtopico("2.2 — Frequência do transdutor: resolução contra penetração")

Uma experiência cotidiana antecipa o princípio inteiro. Quando um vizinho ouve música alta, o que atravessa a parede e chega até você é o grave — os agudos ficam do outro lado. O som de frequência baixa penetra mais; o de frequência alta é absorvido logo. No ultrassom acontece exatamente o mesmo, e essa é a única troca que o operador não consegue burlar.

Frequência alta produz comprimento de onda curto, e comprimento de onda curto é o que permite separar dois pontos próximos — ou seja, dá *resolução*. Uma imagem feita com frequência alta é mais nítida, mais detalhada, mais fácil de interpretar. Só que a mesma frequência alta é atenuada rapidamente pelo tecido e perde energia antes de alcançar profundidade. Frequência baixa faz o contrário: atravessa mais tecido e alcança estruturas profundas, ao preço de um detalhe mais grosseiro. Não existe transdutor que seja ótimo nas duas pontas, e escolher o transdutor é escolher em qual das duas pontas se quer estar.

Daí a correspondência prática entre formato, frequência e uso. O transdutor *linear*, de face reta e frequência alta, é o de estruturas superficiais: tireoide, mama, testículo, vasos do pescoço, partes moles, punção guiada. O transdutor *convexo*, de face curva e frequência mais baixa, é o do abdome, porque precisa alcançar fígado, rim e retroperitônio a vários centímetros da pele. E o transdutor *endocavitário*, usado por via transvaginal ou transretal, é um caso instrutivo: apesar do formato curvo, ele opera em frequência mais alta que o abdominal — porque, ao ser introduzido, encurta drasticamente a distância até o órgão-alvo e pode se dar ao luxo de trocar penetração por detalhe.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-57.png",
  largura: 78%,
  legenda: [Três transdutores e as imagens que produzem. Repare no acoplamento entre geometria, frequência e alvo: o formato da face define o campo de visão (setorial, curvo ou retangular), e a frequência define até onde o feixe chega e com quanto detalhe. A escolha do transdutor é, na prática, a escolha do compromisso entre resolução e profundidade.])

Vale registrar que essa mesma troca explica duas limitações clínicas relevantes. Em pacientes com muito tecido adiposo, o feixe precisa atravessar mais centímetros até o órgão de interesse, e a atenuação acumulada degrada a imagem; a saída é baixar a frequência, e com ela cai o detalhe. Em regiões com gás abundante — alças distendidas, tórax aerado —, o problema é de outra natureza e não se resolve trocando a frequência, como veremos a seguir.

#subtopico("2.3 — Descritores: hiper, hipo e anecogênico")

Mudou o método, mudou o vocabulário — e a tentação mais comum é traduzir um vocabulário no outro. Na radiografia, os termos descrevem quanta radiação o material *absorveu*: radiotransparente e radiopaco. No ultrassom, os termos descrevem quanto eco a estrutura *devolveu*: hiperecogênico, hipoecogênico e anecogênico. Como as duas escalas medem fenômenos físicos diferentes, elas não são traduzíveis uma na outra. A gordura é o contraexemplo que desmonta qualquer tentativa: escura na radiografia, ela aparece *clara* no ultrassom, porque tem muitas interfaces internas que devolvem eco.

Estrutura *hiperecogênica* é a que reflete grande parte do feixe e devolve muitos ecos ao transdutor — aparece branca. Os exemplos típicos são interfaces com alta diferença de propriedades acústicas: cálculo, calcificação, osso, gordura, seio pleural. Estrutura *hipoecogênica* reflete pouco e aparece em cinza escuro, ainda com alguma granulação interna visível — muitos nódulos sólidos se apresentam assim, mais escuros que o parênquima ao redor. Estrutura *anecogênica* não devolve praticamente nada: o feixe atravessa sem encontrar interfaces internas e a região aparece preta, homogênea, sem textura. É o padrão do líquido puro — bexiga cheia, cisto simples, líquido livre, conteúdo de vesícula.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-59.png",
  largura: 76%,
  legenda: [Os três descritores lado a lado. À esquerda, parênquima hepático com um nódulo *hiperecogênico* (mais branco que o fígado ao redor). No centro, uma lesão *hipoecogênica* — mais escura que o parênquima, mas ainda com textura. À direita, a bexiga: conteúdo *anecogênico*, preto e sem granulação. Note que os três termos são comparativos: sempre em relação ao tecido vizinho de referência.])

Duas cautelas fecham o subtópico e evitam erros de raciocínio. A primeira é que os descritores são *relativos*, não absolutos: dizer que um nódulo é hipoecogênico só significa alguma coisa quando se declara em relação a quê — hipoecogênico em relação ao parênquima hepático, ao córtex renal, à tireoide. A segunda é que o descritor informa sobre *interfaces acústicas*, não sobre composição química nem sobre natureza da lesão. Conteúdo anecogênico diz que ali há líquido com poucas interfaces internas — o que é compatível com urina, bile, sangue recente, transudato ou o conteúdo de um cisto simples. Do descritor à hipótese diagnóstica há um passo que exige o contexto clínico inteiro.

#subtopico("2.4 — Sombra acústica posterior e reforço acústico posterior")

Há dois fenômenos no ultrassom que a intuição classifica como defeito da imagem e que a prática usa como pista diagnóstica. Ambos nascem da mesma variável — quanto do feixe uma estrutura deixa passar adiante — e apontam em sentidos opostos.

Quando o feixe encontra uma estrutura que reflete quase tudo, a energia que segue adiante é irrisória. Sem feixe para atravessar, não há eco a ser gerado nas estruturas situadas atrás dela — e o setor posterior da imagem fica preto. Isso é a #termo-nota[sombra acústica posterior][faixa anecogênica atrás de uma estrutura muito refletora, causada pela ausência de feixe remanescente para gerar ecos além dela]. O exemplo canônico é o cálculo dentro da vesícula biliar: uma imagem hiperecogênica bem definida seguida de uma faixa escura que se estende até o fundo da tela. Osso e gás produzem o mesmo efeito, pela mesma razão física — e é por isso que o pulmão aerado e o intestino distendido barram o exame, e por que o ultrassom não avalia bem estruturas atrás de costelas.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-61.png",
  largura: 68%,
  legenda: [Vesícula biliar preenchida por bile *anecogênica*. Junto à parede, uma imagem *hiperecogênica* — o cálculo — e, imediatamente atrás dela, a faixa escura que se prolonga até o limite da imagem: a sombra acústica. A sombra não é falha do aparelho; ela é a assinatura de uma estrutura que refletiu quase todo o feixe.])

O fenômeno inverso ocorre quando o feixe atravessa uma estrutura que reflete muito pouco. Um cisto de conteúdo líquido puro atenua bem menos que o parênquima ao lado; o feixe que passa por dentro dele chega às estruturas posteriores com mais energia do que o feixe vizinho, que teve de atravessar tecido. Como essas estruturas posteriores recebem mais energia, elas devolvem ecos mais intensos e aparecem mais claras — uma faixa branca logo atrás do cisto. Isso é o *reforço acústico posterior*, e ele é a marca registrada de conteúdo líquido. Importante entender o que exatamente mudou: o tecido posterior é o mesmo de antes e não passou a refletir melhor; ele apenas recebeu mais feixe.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-63.png",
  largura: 68%,
  legenda: [Lesão anecogênica arredondada em parênquima hepático, com uma faixa mais clara logo atrás dela (seta). O conteúdo líquido atenuou pouco, o feixe chegou mais forte ao tecido posterior e ele devolveu ecos mais intensos. Sombra e reforço são os dois lados de uma mesma variável: quanto feixe sobrou para adiante.])

#clinica-box("Sombra e reforço como argumento diagnóstico", [
  Uma paciente com dor no hipocôndrio direito após alimentação gordurosa faz ultrassom de abdome. Duas imagens arredondadas aparecem no fígado e na vesícula. A da vesícula é hiperecogênica, móvel com a mudança de decúbito e *projeta sombra* — o padrão de um cálculo, porque só uma estrutura muito refletora impede o feixe de seguir adiante. A do fígado é anecogênica, de paredes finas e *apresenta reforço posterior* — o padrão de um cisto simples, porque só conteúdo com pouquíssimas interfaces internas deixa o feixe passar quase intacto. As duas lesões têm forma parecida na tela, e o que as separa não é a forma: é o que aconteceu com o feixe *depois* de cada uma.
])

#subtopico("2.5 — Método seccional: orientação, limites e o exame dirigido")

Aqui está a diferença estrutural entre o ultrassom e tudo o que foi visto na PARTE I. A radiografia é uma *projeção*: ela soma num plano tudo o que o feixe atravessou. O ultrassom é um método *seccional*: ele produz o corte de um plano, uma fatia da região examinada, e nada do que está fora dessa fatia entra na imagem. Não há sobreposição a desfazer com uma segunda incidência — há um plano de cada vez, escolhido pela orientação do transdutor. Esse conceito é o mesmo que a tomografia levará ao extremo na próxima parte.

Dois planos organizam a rotina. Com o transdutor no eixo transversal, paralelo ao chão no paciente deitado, obtém-se uma imagem *axial*. Girando o transdutor noventa graus, no sentido cabeça-pés, obtém-se uma imagem *sagital*. Quanto à convenção de leitura, o lado direito da tela continua sendo o lado direito do paciente, como na radiografia; e o topo da tela corresponde ao que está *mais próximo do transdutor* — o que costuma significar anterior, mas depende inteiramente de onde o transdutor foi encostado. Não se trata de decorar "topo é anterior", e sim de saber que o topo é a origem do feixe.

As vantagens do método decorrem diretamente da física. Não usa radiação ionizante, o que o libera para uso repetido e para gestante e criança. É o mais barato e o mais portátil dos aparelhos de imagem, e vai ao leito com facilidade. É *dinâmico*: mostra a estrutura se movendo em tempo real, o que permite avaliar peristalse, motilidade diafragmática e contração cardíaca. E oferece o Doppler, cujo mecanismo vale desdobrar porque acrescenta uma dimensão inteira ao exame. Quando a onda emitida atinge um alvo que está se aproximando do transdutor, os ecos voltam com frequência ligeiramente *maior* que a emitida; se o alvo se afasta, voltam com frequência *menor*. É o mesmo efeito que faz a sirene de uma ambulância soar mais aguda enquanto ela se aproxima e mais grave depois que passa. No sangue, os alvos móveis são as hemácias, e a diferença entre a frequência emitida e a recebida é proporcional à velocidade com que elas se deslocam. O aparelho converte essa diferença em número e em cor — por convenção, um tom para o fluxo que se aproxima do transdutor e outro para o que se afasta. Duas consequências práticas seguem daí. A primeira é que o Doppler mede *velocidade e direção* de fluxo, informação funcional que nem a radiografia nem a tomografia simples fornecem, e que permite flagrar uma estenose pelo salto de velocidade no ponto estreitado ou uma trombose pela ausência de fluxo num vaso. A segunda é que o ângulo importa: quando o feixe incide perpendicular ao vaso, não há componente de movimento na direção do feixe e a variação de frequência tende a zero — por isso quem examina angula deliberadamente o transdutor em vez de posicioná-lo perpendicular ao vaso. Como tudo isso é feito em tempo real e com a mão de quem examina sobre o paciente, o método também serve para guiar procedimentos, como punções e drenagens.

As desvantagens são igualmente derivadas da física, com uma exceção. Gordura em excesso atenua o feixe e degrada a imagem. Gás e osso a barram, pelo mecanismo de sombra visto acima — e por isso o ultrassom não estuda o parênquima pulmonar aerado nem estruturas atrás de alças distendidas. A exceção é de outra ordem e é a mais importante de todas: o exame é *operador-dependente*. Diferentemente de uma radiografia, que gera um registro completo passível de revisão por qualquer médico depois, no ultrassom o que se documenta é o que o operador escolheu documentar. Uma região não varrida não deixa vestígio na imagem final; um achado duvidoso não registrado não pode ser reavaliado. Isso não torna o exame pior — torna a interpretação inseparável de quem o realizou.

#clinica-box("O exame dirigido à beira do leito no trauma", [
  Um politraumatizado chega instável à sala de emergência, e a decisão urgente é se existe sangramento intracavitário que justifique laparotomia imediata. O #sigla("FAST", [Focused Assessment with Sonography for Trauma — protocolo ultrassonográfico dirigido à pesquisa de líquido livre no trauma]) responde a essa única pergunta em poucos minutos, sem tirar o paciente da sala. A varredura segue sequência fixa pelos recessos onde o líquido se acumula por gravidade: região subxifoide para o saco pericárdico, espaço hepatorrenal, espaço esplenorrenal e pelve. O achado positivo é uma faixa *anecogênica* entre dois órgãos que, em condições normais, se tocam sem nada visível entre eles — sangue livre, com poucas interfaces internas, é preto no ultrassom. Repare que o protocolo não procura a laceração do órgão; ele procura a consequência dela onde ela se deposita, o que é uma pergunta de conduta, não de diagnóstico anatômico.
])

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rx-usg/slide-67.png",
  largura: 78%,
  legenda: [Os pontos de varredura do exame dirigido no trauma e o achado-alvo. À direita, o espaço hepatorrenal: acima, o exame normal, com fígado e rim justapostos sem interface líquida; abaixo, a faixa anecogênica entre os dois órgãos que caracteriza líquido livre. Os pontos foram escolhidos por gravidade — são os recessos mais baixos para onde o sangue escorre com o paciente em decúbito.])

O ultrassom resolveu dois problemas herdados da radiografia: eliminou a radiação e trocou a projeção pelo corte. Em compensação, criou dois limites novos: não atravessa gás nem osso, e depende de quem segura o transdutor. O método da próxima parte mantém o corte, resolve o problema do gás e do osso e produz um registro completo e reprodutível — cobrando de volta, em radiação, o que o ultrassom havia poupado.

#parte-title("PARTE III — Tomografia: densidade que vira número")

#subtopico("3.1 — Do feixe único ao anel helicoidal multislice")

A tomografia nasce de uma pergunta feita à radiografia: se o problema é que uma projeção soma tudo o que está no trajeto do feixe, e se duas projeções já ajudam a separar as coisas, o que aconteceria com centenas de projeções. A resposta é que, com projeções suficientes tiradas de ângulos suficientes, um computador consegue calcular quanto cada pequeno pedaço de volume atenuou o feixe, individualmente — e, com isso, desfazer a sobreposição em vez de conviver com ela. A física do feixe é a mesma da PARTE I: tubo, fótons de raio X, atenuação por espessura e número atômico. O que muda é a geometria da aquisição e o processamento posterior.

O equipamento traduz essa ideia em três peças. O #termo-nota[gantry][anel do tomógrafo que aloja o tubo de raios X e a coroa de detectores, girando em torno do paciente durante a aquisição] é o anel por onde o paciente passa, e dentro dele o tubo gira continuamente, com uma coroa de detectores acompanhando do lado oposto. A mesa desliza o paciente através do anel. E o console, numa sala separada, recebe os dados brutos e reconstrói a imagem. Junto à mesa costuma haver ainda uma bomba injetora, que administra contraste em velocidade controlada — detalhe que fará diferença no subtópico 3.5.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-13.png",
  largura: 76%,
  legenda: [O equipamento real, com as peças nomeadas: o *gantry* (o anel), a *mesa* que desliza o paciente para dentro dele, a *bomba injetora* de contraste ao lado, e o *computador do console*, na sala de comando. O tubo e os detectores ficam ocultos dentro do anel, girando em torno do eixo do paciente.])

A evolução técnica desse arranjo explica por que o exame ficou rápido. Nas primeiras gerações, o tubo e uma única fileira de detectores giravam uma volta, paravam e voltavam — porque os cabos que alimentavam o conjunto não permitiam rotação contínua. A mesa avançava um passo, o conjunto girava outra vez, e assim sucessivamente. Um exame demorava. A primeira ruptura veio da engenharia: um sistema de contatos deslizantes permitiu que o conjunto girasse indefinidamente numa direção, sem enrolar fios. Com o tubo girando sem parar e a mesa avançando ao mesmo tempo, o feixe passa a descrever uma *hélice* em torno do paciente — daí o nome aquisição helicoidal, e daí a possibilidade de varrer um segmento inteiro do corpo em uma única passagem contínua.

A segunda ruptura foi multiplicar as fileiras de detectores. Uma máquina de fileira única captava um corte por rotação; uma máquina *multislice* tem dezenas ou centenas de fileiras alinhadas no eixo do paciente e capta muitos cortes simultaneamente a cada volta do tubo. O ganho não é apenas de velocidade: como cada rotação cobre mais extensão, o exame inteiro termina em segundos, o que reduz artefato de movimento e permite estudar o coração e os vasos entre um batimento e outro.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-19.png",
  largura: 66%,
  legenda: [À esquerda, o esquema de fileira única: uma volta do tubo cobre uma fatia de espessura fixa. À direita, o arranjo multislice: várias fileiras de detectores em paralelo captam várias fatias na mesma rotação. Mais fileiras significa mais volume por giro, exame mais curto e cortes mais finos disponíveis.])

Vale separar dois termos que costumam ser usados como se fossem um só, porque eles descrevem avanços independentes que hoje andam juntos. *Helicoidal* diz respeito ao modo de aquisição: tubo em rotação contínua com a mesa avançando, produzindo varredura ininterrupta. *Multislice* diz respeito ao número de fileiras de detectores, isto é, a quantos cortes se obtém por rotação. Um aparelho pode ser helicoidal de fileira única; os atuais são helicoidais e multislice ao mesmo tempo, o que explica a combinação de exame rápido com alta resolução.

#subtopico("3.2 — Voxel, dados brutos e reconstrução multiplanar")

O que a máquina entrega ao computador não é uma imagem: são *dados brutos*, um conjunto imenso de medidas de atenuação tomadas de muitos ângulos. A imagem é calculada a partir deles. E o objeto elementar desse cálculo não é um ponto plano, e sim um pequeno bloco de volume.

Na tela de um computador comum, a unidade é o pixel: um quadradinho com posição em dois eixos, X e Y. Na tomografia, cada elemento da matriz corresponde a um pedaço real do corpo que tem também espessura — o eixo Z, definido pela espessura do corte. Esse elemento tridimensional é o *voxel*, e vale pensá-lo como um tijolinho, não como um ladrilho. Os eixos X e Y são determinados pela matriz computacional, tipicamente de 512 por 512, o que dá cerca de 260 mil elementos por corte. O eixo Z é escolhido no protocolo: cortes de milímetro ou de fração de milímetro nos exames finos, cortes mais espessos quando se quer menos ruído.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-29.png",
  largura: 72%,
  legenda: [Do plano ao volume. À esquerda, o corte axial como o vemos; à direita, o mesmo corte entendido como uma camada de blocos: a matriz de 512 × 512 define X e Y, e a espessura do corte define Z. Cada voxel guarda um único número — a *atenuação média* de tudo o que estiver dentro daquele bloco.])

Essa última frase da legenda carrega uma consequência prática que vale desdobrar. Como o voxel guarda a média do que há dentro dele, um corte espesso que apanhe metade osso e metade tecido mole devolve um número intermediário, que não corresponde a nenhum dos dois. É o chamado efeito de média de volume, e ele explica por que estruturas pequenas ficam mal representadas em cortes grossos e por que se pedem cortes finos quando se procura algo diminuto — um cálculo ureteral, uma lesão milimétrica.

O ganho mais visível dessa arquitetura é a reconstrução. Como a aquisição é volumétrica, o computador não fica preso ao plano em que os dados foram colhidos: ele pode reorganizar o mesmo conjunto de voxels em qualquer plano. O plano *axial* é o que a máquina de fato adquire; a partir dele são calculados o *sagital*, o *coronal*, reconstruções tridimensionais e representações especiais que privilegiam voxels de alta ou de baixa atenuação. Tudo isso vem de uma única passagem do paciente pelo anel.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-25.png",
  largura: 80%,
  legenda: [Quatro apresentações do *mesmo* conjunto de dados: axial, sagital, coronal e reconstrução tridimensional. O paciente entrou no anel uma única vez. Nenhuma dessas imagens contém informação que as outras não contenham — o que muda é o arranjo espacial escolhido para exibir os mesmos voxels.])

#confusao-prevista(
  titulo: "Reconstrução não é nova aquisição",
  aluno_acha: [que cada plano exibido corresponde a uma passagem adicional do paciente pelo aparelho, e portanto a mais radiação.],
  mecanismo: [a aquisição é volumétrica e única. Sagital, coronal e tridimensional são cálculos feitos sobre o mesmo conjunto de voxels já registrado, e não custam um fóton a mais. O que de fato exige nova passagem é mudar o *momento* da aquisição — como nas fases após injeção de contraste, no subtópico 3.5 —, porque aí o que se quer registrar é um estado diferente do paciente, não um arranjo diferente dos mesmos dados.],
)

#subtopico("3.3 — Unidades Hounsfield: a água como zero")

Medir só faz sentido contra uma referência, e toda régua precisa de um zero. A tomografia adota a água como esse zero — decisão arbitrária no sentido em que qualquer padrão é arbitrário, mas conveniente, porque a água é o componente majoritário do corpo e tem propriedades estáveis e reprodutíveis. A escala resultante mede o coeficiente de atenuação de cada voxel *em relação ao da água*, multiplicado por mil para dar números manejáveis. A unidade recebeu o nome do engenheiro que construiu o primeiro tomógrafo e é abreviada como #sigla("UH", [unidade Hounsfield — medida do coeficiente de atenuação de um voxel em relação ao da água, que vale zero por definição]).

$ "UH" = 1000 times (mu_"tecido" - mu_"água") / mu_"água" $

A fórmula merece ser lida em palavras, porque assim ela deixa de ser símbolo e vira raciocínio. Primeira etapa: subtrai-se do coeficiente de atenuação do tecido o coeficiente da água. Se o tecido atenua exatamente como a água, essa diferença é zero — e a água vale zero por construção. Segunda etapa: divide-se pelo coeficiente da água, o que transforma a diferença absoluta numa fração relativa e faz a escala independer das unidades físicas originais. Terceira etapa: multiplica-se por mil, apenas para espalhar os valores numa faixa de números inteiros fáceis de comparar. O sinal do resultado responde a uma pergunta direta: o tecido atenua mais que a água, e o número é positivo; atenua menos, e o número é negativo.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-33.png",
  largura: 74%,
  legenda: [Os três pontos de calibração da escala. O feixe sai do tubo, atravessa o paciente e chega aos detectores; o ar atenua quase nada e fica em torno de −1000 UH, a água por definição em 0 UH, e o osso denso em torno de +1000 UH. Note que a escala é *ancorada*, não relativa à imagem: um voxel de líquor vale zero num exame de crânio e zero num exame de abdome.])

Essa ancoragem é a diferença qualitativa entre a tomografia e a radiografia. Na radiografia, o cinza é uma impressão comparativa — mais claro ou mais escuro que o vizinho. Na tomografia, cada voxel carrega um *número*, e esse número pode ser medido com o cursor e comparado com valores de referência. A imagem deixa de ser apenas qualitativa e passa a ser quantitativa, o que abre a porta para diagnósticos feitos por medida.

#table(
  columns: (1.5fr, 1fr, 2.6fr),
  inset: 7pt,
  align: (left + horizon, center + horizon, left + horizon),
  stroke: 0.5pt + gray-border,
  fill: (x, y) => if y == 0 { navy } else if calc.odd(y) { gray-bg } else { white },
  table.header(
    text(fill: white, weight: 700, font: titulo-fam, size: 9pt)[Estrutura],
    text(fill: white, weight: 700, font: titulo-fam, size: 9pt)[Faixa (UH)],
    text(fill: white, weight: 700, font: titulo-fam, size: 9pt)[Por que esse valor],
  ),
  [Ar], [≈ −1000], [Praticamente não atenua: quase nenhum átomo no caminho do feixe.],
  [Gordura], [−100 a −30], [Atenua menos que a água — carbono e hidrogênio, pouca massa por volume.],
  [Água e líquor], [0], [Zero por definição da escala; é o padrão de referência.],
  [Substância branca], [20 a 30], [Rica em lipídio da mielina, atenua um pouco menos que a cinzenta.],
  [Músculo e vísceras], [20 a 40], [Composição próxima à da água, com discreto acréscimo proteico.],
  [Sangue coagulado], [65 a 95], [Concentração de proteína e ferro da hemoglobina eleva a atenuação.],
  [Osso denso], [≈ +1000], [Cálcio tem número atômico alto e intercepta muito mais fótons.],
)

A tabela não é para decorar linha a linha; ela é para fixar a *ordem* e alguns pontos de ancoragem. Dois deles têm rendimento clínico imediato. O primeiro é a distância entre líquor e sangue: o líquor está em zero e o sangue coagulado, entre sessenta e cinco e noventa e cinco, o que faz uma hemorragia recente aparecer nitidamente branca no exame de crânio sem contraste — motivo pelo qual esse é o exame de primeira linha no trauma craniano e na suspeita de acidente vascular hemorrágico. O segundo é a posição da gordura em valores negativos, que permite identificar tecido adiposo com segurança e é a base do diagnóstico do subtópico seguinte.

#clinica-box("Esteatose hepática medida com o cursor", [
  O parênquima hepático normal atenua *mais* que o baço e mais que o sangue dentro dos vasos, e por isso o fígado normal aparece discretamente mais claro que as veias hepáticas que o cruzam. Quando o hepatócito acumula triglicerídeo, o conteúdo de gordura do tecido aumenta e a atenuação média do voxel cai — porque a gordura mora na faixa negativa da escala. O resultado é um fígado *hipoatenuante*, mais escuro que o normal, ao ponto de inverter a relação habitual: os vasos passam a parecer mais claros que o parênquima ao redor. O achado pode ser objetivado com o cursor, medindo a atenuação do parênquima e comparando com a do baço. Repare que não se trata de um sinal aprendido de cor: ele decorre diretamente de onde a gordura se situa na escala de Hounsfield.
])

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-71.png",
  largura: 74%,
  legenda: [À esquerda, fígado normal: parênquima homogêneo, mais claro que os vasos que o atravessam. À direita, esteatose: o parênquima ficou *mais escuro*, deslocando-se na escala em direção à faixa da gordura (destaque no eixo inferior). O baço, que não acumula gordura, serve de referência interna dentro do próprio exame.])

#subtopico("3.4 — Janela e nível: o gargalo é o olho humano")

A tomografia mede pelo menos duas mil atenuações distintas, mas um monitor exibe no máximo duzentos e cinquenta e seis tons de cinza — e o olho humano, na melhor das hipóteses, distingue algo em torno de sessenta e quatro, com média prática bem menor. O gargalo, portanto, não está no aparelho nem na tela: está na retina de quem observa. Se toda a faixa de atenuações fosse comprimida de uma vez nos poucos cinzas visíveis, tecidos com valores próximos ficariam indistinguíveis, e a vantagem quantitativa do método se perderia na exibição.

A solução é computacional e se chama ajuste de *janela* e *nível*. O nível é o valor de atenuação que fica no *centro* da faixa exibida; a janela é a *largura* dessa faixa. Escolhidos os dois, o computador distribui todos os tons de cinza disponíveis apenas dentro daquele intervalo: tudo o que estiver acima do limite superior é pintado de branco puro, tudo o que estiver abaixo do limite inferior vira preto puro, e o miolo recebe a escala inteira. É uma lente: aumenta-se o contraste dentro de uma faixa ao custo de saturar o que está fora dela.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-39.png",
  largura: 78%,
  legenda: [O eixo de atenuações de −1000 a +1000 e a faixa selecionada sobre ele. O *nível* marca o centro da faixa; a *janela*, sua largura. Pixels com atenuação acima do limite superior são exibidos em branco; abaixo do limite inferior, em preto. Só o intervalo escolhido recebe a gradação de cinzas.])

Daí decorrem as janelas de rotina, cada uma calibrada para uma faixa de interesse. A *janela de partes moles* centra o nível perto da água com largura moderada, e separa bem músculo, gordura, vísceras e coleções — mas achata o osso num branco uniforme e o pulmão num preto uniforme. A *janela de parênquima pulmonar* baixa muito o nível, para a faixa do ar, e alarga a janela: passa a mostrar a textura do pulmão, os septos, os vasos finos e as áreas de aprisionamento aéreo. A *janela óssea* sobe o nível para valores altos e permite distinguir a cortical da medular óssea, revelando traços de fratura que a janela de partes moles esconderia.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-41.png",
  largura: 82%,
  legenda: [O *mesmo corte axial de tórax*, exibido em três janelas. Em partes moles, os músculos e o mediastino são legíveis, mas o pulmão é preto e o osso é branco chapado. Em parênquima pulmonar, aparecem os vasos e a textura do pulmão. Em janela óssea, distinguem-se cortical e medular das costelas e vértebras. Nenhum dado mudou entre as três — só o mapeamento de números para cinzas.])

#atencao-box("A janela não altera o número medido", [
  É tentador concluir que, ao trocar a janela e ver o tecido escurecer, a atenuação daquele tecido mudou. Ela não mudou. A unidade Hounsfield de cada voxel é uma medida física registrada na aquisição, e permanece a mesma independentemente de como é exibida. Isso tem consequência direta na prática: uma coleção que "parece" hiperatenuante numa janela estreita pode estar em faixa perfeitamente normal quando medida com o cursor, e uma lesão discreta pode desaparecer visualmente numa janela inadequada sem deixar de existir. Sempre que a diferença entre duas hipóteses depender de quanto o tecido atenua — sangue ou líquido, gordura ou tecido mole, calcificação ou contraste —, a decisão se toma pelo *número medido*, não pelo tom de cinza percebido.
])

Fica também o vocabulário próprio do método, que segue a mesma lógica dos descritores das partes anteriores sem ser traduzível neles: estrutura *hiperatenuante* é a que tende ao branco por atenuar muito, e *hipoatenuante* é a que tende ao preto por atenuar pouco — sempre em comparação com o tecido de referência ao lado.

#subtopico("3.5 — Contraste iodado, fases temporais e artefatos")

Mesmo com escala quantitativa e cortes finos, muita coisa dentro do abdome atenua de forma parecida. Um nódulo hepático pode ter praticamente a mesma atenuação do fígado ao redor; uma trombose dentro da veia porta pode não se distinguir do sangue circulante. A saída é a mesma da radiografia — introduzir contraste iodado —, mas com um recurso que a radiografia não tem: a tomografia é tão rápida que pode fotografar o *mesmo território em instantes diferentes* da distribuição do contraste. E é essa dimensão temporal que carrega grande parte da informação.

Vale fixar o princípio antes das fases: o contraste injetado é sempre o mesmo. O que distingue uma fase da outra é apenas *quando* se adquire a imagem depois do início da injeção. Cerca de trinta segundos depois, o contraste está concentrado nas artérias — é a *fase arterial*, e nela se destacam lesões hipervascularizadas, que recebem sangue arterial em abundância e ficam mais claras que o parênquima. Em torno de setenta segundos, o contraste já atravessou o leito capilar e retornou pelo sistema venoso; na *fase portal* o parênquima hepático realça de modo homogêneo e as veias estão opacificadas, o que é o melhor momento para avaliar o fígado como um todo e para flagrar falhas de enchimento venoso. Perto de noventa segundos, na *fase nefrográfica*, o córtex e a medula renais realçam juntos. Após alguns minutos, na *fase de equilíbrio*, o contraste já se distribuiu pelo interstício, e lesões que retêm contraste no interstício continuam claras enquanto o resto começou a lavar. Por volta de sete minutos, o rim já está eliminando o contraste e a *fase excretora* desenha pelve renal, ureteres e bexiga por dentro.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-45.png",
  largura: 72%,
  legenda: [O protocolo em duas colunas: à esquerda, as vias de administração — endovenosa, oral e retal; à direita, os tempos de aquisição que definem cada fase. O ponto a levar é que o eixo à direita é *tempo*, não tipo de contraste: uma mesma injeção, várias leituras.])

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-53.png",
  largura: 84%,
  legenda: [O mesmo corte de abdome superior em cinco momentos. *Sem contraste*: aorta e vísceras com atenuação semelhante. *Arterial*: a aorta fica intensamente branca e o córtex renal se destaca. *Portal*: a veia porta e as veias hepáticas se opacificam e o parênquima hepático realça por inteiro. *Nefrográfica*: córtex e medula renais realçam juntos. *Equilíbrio*: o contraste começa a se distribuir e aparece na pelve renal, a caminho da eliminação.])

As vias oral e retal cumprem função diferente da endovenosa e vale não confundi-las. O contraste endovenoso realça vasos e parênquimas, porque circula pelo sangue. O contraste administrado por boca ou por via retal — e, em alguns protocolos, simplesmente água em volume — não realça órgão nenhum: ele *distende e delimita a luz* do tubo digestório, separando alças que, colabadas e encostadas umas nas outras, formariam um bloco indistinguível na imagem. É o mesmo raciocínio do sinal da silhueta da PARTE I, aplicado em sentido inverso: em vez de perder o contorno por vizinhança semelhante, cria-se a diferença de propósito.

Nenhum método está livre de #termo-nota[artefato][alteração da imagem que não corresponde a estrutura real do paciente, produzida por características do objeto ou por falha no processo de aquisição], e reconhecer os dois mais comuns da tomografia evita erro grosseiro. O *artefato de endurecimento do feixe* aparece diante de material muito atenuante, tipicamente implantes metálicos e próteses dentárias: o metal absorve preferencialmente os fótons de menor energia do feixe, de modo que o feixe remanescente fica com energia média mais alta — mais "duro" — e o cálculo de reconstrução, que pressupõe um feixe homogêneo, produz faixas escuras e claras irradiando a partir do material. O *artefato de movimento* aparece quando o paciente se mexe, respira ou até coça o rosto durante a aquisição: as projeções deixam de corresponder à mesma posição anatômica e a reconstrução gera borramento e linhas de descontinuidade que imitam fratura ou lesão.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-59.png",
  largura: 70%,
  legenda: [Artefato de endurecimento do feixe por restaurações metálicas. As faixas escuras e claras que cruzam o corte não existem no paciente: são o resultado de o algoritmo de reconstrução receber medidas incompatíveis com a premissa de feixe homogêneo. O reflexo prático é sempre o mesmo — antes de nomear um achado, perguntar se ele pode ter sido produzido pelo processo de formação da imagem.])

Do lado das vantagens, a tomografia é rápida, tem excelente resolução espacial, resolve a sobreposição, entrega qualquer plano a partir de uma aquisição só e fornece medida quantitativa. Do lado dos custos, ela usa radiação ionizante — com todo o raciocínio de justificação visto em 1.5, e com peso especial em pacientes jovens e em exames repetidos —, frequentemente depende de contraste iodado, e exige transportar o paciente até o aparelho, o que a torna má escolha para o instável que não pode sair do leito.

#clinica-box("Pneumotórax: por que a tomografia enxerga o que a radiografia deixa passar", [
  Um paciente com dor torácica súbita faz radiografia de tórax, que mostra apenas uma discreta hipertransparência no ápice. Na tomografia, a diferença fica evidente por dois motivos somados. Primeiro, não há sobreposição: o ar da cavidade pleural ocupa uma região definida do corte, em vez de se somar ao parênquima na projeção. Segundo, a escala é ancorada — o ar livre da cavidade pleural fica próximo de −1000 UH, enquanto o pulmão colabado, que ainda contém sangue e interstício permeando o ar alveolar, fica visivelmente acima disso. A linha da pleura visceral aparece então como fronteira entre dois valores de atenuação diferentes, e o pulmão colabado se distingue do ar livre por ser *mais hiperatenuante que o ar puro*. Na janela de parênquima, a separação é imediata.
])

#figura-nebli("/figuras/radiologia-02-principios-fisicos/tc/slide-73.png",
  largura: 76%,
  legenda: [À esquerda, a radiografia de tórax, em que a lâmina de ar precisa ser procurada com atenção. À direita, o mesmo caso em tomografia com janela de parênquima pulmonar: a cavidade pleural com ar livre aparece francamente escura e o parênquima remanescente, mais claro, com seus vasos preservados. O destaque no eixo inferior marca a posição do ar na escala de Hounsfield.])

A tomografia resolveu a sobreposição e trouxe a medida. Mas ela ainda separa tecidos por uma única propriedade física — quanto cada um atenua o raio X —, e tecidos moles diferentes atenuam de maneira parecida. O método da próxima parte troca essa propriedade por outra completamente distinta: em vez de medir o que o tecido absorve, ele escuta o que os prótons do tecido devolvem.

#parte-title("PARTE IV — Ressonância: o sinal que o próton devolve")

#subtopico("4.1 — Por que hidrogênio: spin, momento magnético e prótons ímpares")

A ressonância magnética abandona por completo a lógica dos três métodos anteriores. Não há feixe atravessando o paciente, nem eco voltando de uma interface. A fonte do sinal é o próprio corpo: são os núcleos de hidrogênio dos tecidos que, adequadamente estimulados, devolvem energia — e é essa energia devolvida que vira imagem. O aparelho não ilumina o paciente; ele faz o paciente emitir.

A escolha do hidrogênio como elemento de trabalho se apoia em três razões que convém separar, porque cada uma responde a uma pergunta diferente. A primeira é de *abundância*: o corpo humano é essencialmente água e gordura, e as duas são moléculas ricas em hidrogênio, o que garante sinal vindo de praticamente qualquer tecido. A segunda é de *variabilidade*: a proporção de água muda muito entre um tecido e outro, e muda ainda mais entre tecido normal e tecido doente — edema, inflamação, necrose e tumor alteram o conteúdo de água —, e é justamente essa variação que vira contraste na imagem. A terceira é *física*, e é a que exige explicação: o hidrogênio tem momento magnético alto.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-08.png",
  largura: 64%,
  legenda: [O núcleo do átomo de hidrogênio é, em quase toda a sua abundância natural, um único próton. Sem nêutron e sem outro próton para lhe fazer par, ele fica com uma resultante magnética própria — condição de partida para tudo o que vem a seguir.])

Para entender o que é momento magnético, é preciso um passo atrás, até a descoberta que fundou o método. Em 1939, Isidor Rabi mostrou que os prótons não são partículas paradas: eles giram em torno do próprio eixo, e esse giro recebeu o nome de #termo-nota[spin][rotação intrínseca do próton em torno do próprio eixo; por se tratar de carga em movimento, gera corrente e, com ela, um campo magnético]. Aqui entra a física básica que costura o raciocínio: carga elétrica em movimento gera corrente, e corrente gera campo magnético. Como o próton tem carga positiva e gira, ele gera um campo magnético próprio — e é a esse campo que se dá o nome de *momento magnético*. A consequência conceitual é a imagem que vale carregar por toda a parte: cada núcleo de hidrogênio do corpo se comporta como um ímã minúsculo, com norte e sul, capaz de ser orientado por um campo magnético externo.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-06.png",
  largura: 62%,
  legenda: [A cadeia causal completa em um esquema: *próton → spin → corrente elétrica → campo magnético*. O resultado prático está desenhado embaixo — o próton em rotação se comporta como uma barra imantada, com polos definidos. É por isso que ele responde ao campo do aparelho.])

Falta explicar por que o hidrogênio, e não qualquer núcleo. Núcleos com número *par* de prótons têm seus momentos magnéticos organizados aos pares de sentido oposto, que se cancelam mutuamente: a resultante é nula e não há nada que um campo externo possa orientar. Núcleos com número *ímpar* sempre têm um próton desemparelhado, cujo momento magnético não é anulado por nenhum outro — e é essa sobra que constitui a resultante magnética utilizável. O hidrogênio é o caso mais simples possível dessa condição, com um único próton, e soma a ela a abundância e a variabilidade já mencionadas. Outros núcleos de número ímpar, como sódio e fósforo, também geram sinal e são objeto de pesquisa; na prática diária, o hidrogênio é o elemento usado.

#mini-resumo[Hidrogênio é escolhido por três motivos somados: está em toda parte (água e gordura), varia entre tecido normal e doente, e tem número ímpar de prótons — o que deixa uma resultante magnética que um campo externo consegue orientar.]

#subtopico("4.2 — Dentro do campo principal: paralelo, antiparalelo e magnetização longitudinal")

No dia a dia, esses bilhões de ímãs minúsculos apontam para direções aleatórias. O campo magnético da Terra, da ordem de três centésimos de milésimo de tesla, é fraco demais para organizá-los: cada spin faz o que quer, e a soma vetorial de todos eles é praticamente nula. É por isso que o corpo não emite sinal magnético útil em condições normais.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-14.png",
  largura: 60%,
  legenda: [Sob o campo magnético terrestre, os momentos magnéticos dos prótons apontam em direções desordenadas (à esquerda). Não há orientação preferencial e, portanto, não há resultante mensurável. À direita, o campo do aparelho aguardando — a ordem só aparece quando o corpo entra nele.])

Dentro do magneto do aparelho, cujo campo é dezenas de milhares de vezes mais intenso que o terrestre, a situação muda. Os momentos magnéticos passam a se orientar segundo a direção do campo principal, chamado B#sub[0] — e aqui um detalhe importa. Eles não se alinham todos no mesmo sentido: parte se alinha *paralela* ao campo e parte se alinha *antiparalela*, em sentido oposto. A configuração paralela exige menos energia e, por isso, é a mais populosa. A diferença entre as duas populações é pequena — alguns prótons a mais em cada milhão —, mas é real, e é dela que nasce todo o sinal do exame. Como os pares opostos se cancelam, o que sobra é uma resultante magnética líquida, alinhada com B#sub[0], chamada *magnetização longitudinal*.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-16.png",
  largura: 68%,
  legenda: [Dentro de B#sub[0], os spins se dividem em duas populações: *paralela* (setas azuis, estado de menor energia, mais numerosa) e *antiparalela* (setas vermelhas, estado de maior energia, menos numerosa). Os pares opostos se anulam; o pequeno excesso de paralelos é a magnetização longitudinal, e é a única coisa que sobra para ser trabalhada.])

Está montado, então, o problema central do método. A magnetização longitudinal existe, é a origem de todo o sinal — e não pode ser medida. A razão é de escala: ela aponta exatamente na mesma direção de B#sub[0] e é infinitamente menor que ele. Tentar detectá-la ali seria como tentar medir a quantidade de água que caiu numa chuva olhando para o nível do oceano. Para transformar essa resultante em algo mensurável, é preciso *tirá-la da direção de B#sub[0]* — colocá-la num plano perpendicular, onde ela não esteja mais camuflada pelo campo principal e onde sua variação possa induzir corrente numa bobina receptora.

É essa tarefa — deslocar a magnetização do eixo longitudinal para o transversal — que cabe às bobinas de radiofrequência. Como elas fazem isso é o assunto do próximo subtópico, e a resposta envolve uma condição bem mais específica do que simplesmente "aplicar energia".

#subtopico("4.3 — Precessão, frequência de Larmor e o pulso de radiofrequência")

Energia aplicada de qualquer jeito não move a magnetização. Ela precisa chegar numa frequência muito específica, e essa exigência é o coração do fenômeno que dá nome ao método. Para entender de onde vem essa frequência, é preciso reconhecer que o próton dentro do campo faz *dois* movimentos ao mesmo tempo, e não apenas um.

O primeiro já foi visto: o spin, a rotação em torno do próprio eixo. O segundo é a *precessão*, o movimento pelo qual o eixo de rotação do próton descreve um cone em torno da direção do campo magnético — exatamente como um pião que gira depressa em torno de si mesmo enquanto seu eixo bamboleia em torno da vertical. O que interessa é a velocidade desse bamboleio, porque ela define uma frequência característica, chamada #termo-nota[frequência de Larmor][frequência de precessão do próton em torno da direção do campo magnético, proporcional à intensidade desse campo]. Ela não é uma constante universal: é proporcional à intensidade do campo aplicado, de modo que a mesma população de prótons precessa mais depressa num aparelho de campo mais alto.

$ omega_0 = gamma dot B_0 $

Lendo a expressão em palavras: a frequência de precessão é o produto de uma constante própria de cada núcleo — chamada razão giromagnética — pela intensidade do campo magnético em que ele está. A leitura prática é direta: dobrado o campo, dobra a frequência de precessão; e como o hidrogênio tem sua constante própria, ele precessa numa frequência diferente da de qualquer outro núcleo no mesmo campo. É isso que permite conversar com o hidrogênio e apenas com ele.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-26.png",
  largura: 66%,
  legenda: [A precessão ilustrada pelo pião: o corpo gira em torno do próprio eixo enquanto o eixo descreve um cone em torno da vertical. A expressão relaciona a frequência de precessão à intensidade do campo. A frequência é a "identidade" do elemento dentro daquele campo — e é o endereço que o pulso precisa acertar.])

Bloch e Purcell mostraram o que acontece quando se acerta esse endereço. Emitindo um pulso de radiofrequência com frequência *igual* à de precessão do hidrogênio, o próton absorve essa energia — e absorve porque as duas frequências coincidem. Esse acoplamento entre uma perturbação externa e a frequência natural do sistema é o que a física chama de *ressonância*, e é literalmente de onde vem o nome do exame. Um pulso em qualquer outra frequência passa sem efeito; um pulso na frequência de Larmor é integralmente absorvido.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-28.png",
  largura: 68%,
  legenda: [O princípio da ressonância expresso em palavras e em desenho: o objeto exposto a uma perturbação oscilatória de frequência próxima à sua natural ganha energia do meio externo. Aplicado ao exame, o pulso de radiofrequência deve ter a frequência de Larmor do hidrogênio para excitá-lo, e o vetor de magnetização é então derrubado do eixo longitudinal para o plano transversal.])

A absorção produz dois efeitos simultâneos, e vale contá-los separadamente porque eles reaparecerão em 4.4 como fenômenos independentes. O primeiro é que a magnetização é *derrubada* do eixo longitudinal para o plano transversal — o vetor que apontava na direção de B#sub[0] passa a girar num plano perpendicular a ele, onde pode induzir corrente numa bobina receptora. O segundo é que os prótons, que precessavam cada um em sua fase, passam a precessar *em fase*, sincronizados — o que faz seus pequenos vetores se somarem em vez de se cancelarem, produzindo uma resultante transversal robusta.

Quando a bobina é desligada, o sistema volta ao estado que o campo B#sub[0] impõe: a magnetização transversal se desfaz e a longitudinal se recompõe. Nesse retorno, os prótons liberam a energia absorvida, e essa liberação é captada por uma bobina receptora, que a converte em corrente elétrica e a envia ao computador. O circuito completo do método cabe em três atos: o campo alinha, o pulso derruba, o retorno gera sinal.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-12.png",
  largura: 66%,
  legenda: [Os três atos num único esquema. O *campo magnético* alinha os prótons de hidrogênio; a *bobina emissora* aplica o pulso de radiofrequência que os desestabiliza; a *bobina receptora* capta a energia devolvida no retorno e a entrega ao computador, que constrói a imagem.])

#atencao-box("Radiofrequência não ioniza — mas o campo magnético é um risco real", [
  Duas conclusões opostas costumam ser tiradas ao mesmo tempo, e as duas erram. A primeira é supor que a ressonância irradia como o raio X: não irradia. A energia de um fóton de radiofrequência é ordens de grandeza inferior à necessária para arrancar um elétron de um átomo, e portanto não há ionização, não há radicais livres e não há quebra de fita de DNA por esse mecanismo. A segunda é concluir daí que o exame não oferece risco. O magneto é *sempre* de alta intensidade e está *sempre* ligado, mesmo com o aparelho ocioso. Qualquer objeto ferromagnético levado à sala é atraído com força e velocidade suficientes para atravessar o ambiente e atingir quem estiver dentro do anel — cilindros de oxigênio, macas, tesouras, grampos. A triagem antes do exame é indispensável e cobre também o que está dentro do paciente: marca-passos, clipes de aneurisma, implantes cocleares e fragmentos metálicos intraoculares. Não há radiação, o que não é o mesmo que não haver perigo.
])

#subtopico("4.4 — T1 e T2: dois relógios que andam em velocidades diferentes")

Se todos os tecidos devolvessem a mesma energia no mesmo instante, a imagem seria uniforme e inútil. O contraste da ressonância nasce de os tecidos voltarem ao estado de repouso em *velocidades diferentes* — e, mais do que isso, de haver duas voltas distintas acontecendo ao mesmo tempo, cada uma com seu próprio relógio.

O primeiro relógio mede a recomposição da magnetização longitudinal. Desligado o pulso, o vetor que havia sido derrubado começa a crescer de volta na direção de B#sub[0], e ele só consegue fazer isso entregando energia ao ambiente molecular ao redor. O tempo que esse processo leva é o *relaxamento T1* — o tempo de recuperar o eixo longitudinal, perdendo energia para o meio.

O segundo relógio mede algo diferente: a perda da magnetização transversal. Logo após o pulso, os prótons giravam em fase e seus vetores se somavam. Assim que o pulso cessa, cada próton começa a sentir microcampos ligeiramente distintos, produzidos pelos prótons vizinhos, e passa a precessar numa velocidade um pouquinho diferente da dos outros. Eles se *defasam*, e vetores fora de fase se cancelam em vez de se somar: a resultante transversal encolhe. Esse é o *relaxamento T2* — o tempo de perder a coerência de fase no plano transversal, por interação entre os próprios prótons.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-36.png",
  largura: 60%,
  legenda: [Os dois eixos do problema. No vertical, o *relaxamento T1*: a magnetização longitudinal crescendo de volta na direção do campo. No horizontal, o *relaxamento T2*: a magnetização transversal encolhendo. O vetor resultante percorre os dois eixos ao mesmo tempo — não em sequência.])

#confusao-prevista(
  titulo: "T1 e T2 não são etapas em sequência",
  aluno_acha: [que primeiro ocorre o relaxamento T2 e, terminado ele, começa o T1 — como se fossem duas fases de um mesmo processo linear.],
  mecanismo: [os dois começam no mesmo instante, assim que o pulso é desligado, e correm em paralelo por mecanismos independentes: T1 é a entrega de energia ao meio ao redor, T2 é a perda de sincronia entre prótons vizinhos. O que os diferencia é a *velocidade*: o T2 é tipicamente muito mais rápido, de modo que um tecido pode já ter perdido quase toda a magnetização transversal enquanto ainda está longe de recuperar a longitudinal.],
)

O ponto decisivo é que T1 e T2 são *propriedades intrínsecas de cada tecido*, e não parâmetros do aparelho. Cada tecido tem seu par de tempos, determinado pela mobilidade de suas moléculas e pelo modo como seus prótons interagem com a vizinhança. Duas referências organizam o resto do assunto e vale ancorá-las bem:

A *gordura* recupera a magnetização longitudinal depressa — tem *T1 curto* — porque suas moléculas de cadeia longa se movem em velocidade próxima à frequência de precessão, o que torna a entrega de energia ao meio muito eficiente. Pela mesma razão de vizinhança densa e interativa, ela também perde a coerência transversal rápido: tem *T2 curto*.

A *água livre* faz o oposto em ambos os relógios. Suas moléculas são pequenas e se movem rápido demais para trocar energia com eficiência, de modo que ela demora a recompor o eixo longitudinal — *T1 longo* — e, por ter poucas interações entre prótons vizinhos, mantém a sincronia de fase por muito mais tempo — *T2 longo*.

#mini-resumo[Gordura: T1 curto e T2 curto — recupera depressa o eixo longitudinal e perde depressa o transversal. Água: T1 longo e T2 longo — demora nos dois. É a diferença entre esses tempos que vira contraste.]

#subtopico("4.5 — Ponderação, gadolínio e o equipamento")

Tendo dois tecidos com relógios diferentes, o operador escolhe *quando* ler o sinal — e essa escolha decide qual dos dois relógios governa o contraste da imagem. É isso, e nada mais, que a palavra ponderação significa: o exame é ponderado em T1 quando o esquema de pulsos é montado de modo que a diferença de T1 entre os tecidos seja a que mais pesa no sinal; e ponderado em T2 quando o que pesa é a diferença de T2.

Na *ponderação em T1*, os pulsos se sucedem em intervalos curtos. Nesse intervalo apertado, a gordura, que tem T1 curto, já recompôs boa parte de sua magnetização longitudinal e chega ao pulso seguinte com um vetor grande, que gera muito sinal — aparece branca. A água, com T1 longo, mal começou a se recompor e chega ao próximo pulso com pouco vetor disponível: gera pouco sinal e aparece preta. Daí a regra que se lê nas imagens: em T1, gordura branca e água preta.

Na *ponderação em T2*, o intervalo entre os pulsos e o momento da leitura são longos. Nesse tempo estendido, a gordura, com T2 curto, já perdeu quase toda a coerência transversal e praticamente não contribui mais para o sinal — aparece escura. A água, com T2 longo, ainda mantém boa parte da magnetização transversal e devolve sinal forte — aparece branca. Daí a regra espelhada: em T2, água branca e gordura escura.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-44.png",
  largura: 74%,
  legenda: [Por que o momento da leitura decide o contraste. Depois do primeiro pulso, os dois elementos têm o mesmo vetor transversal. Ao serem desligados, cada um retorna na sua velocidade — e, quando chega o segundo pulso, um deles já recuperou o eixo longitudinal enquanto o outro não. É essa diferença acumulada no intervalo entre pulsos que aparece na imagem como contraste.])

Há ainda um terceiro tipo de imagem, útil para entender por eliminação. Na *densidade de prótons*, os parâmetros são escolhidos de modo a anular o peso dos dois relógios: espera-se tempo suficiente para que todos os tecidos tenham recuperado o eixo longitudinal, e lê-se cedo o bastante para que nenhum tenha perdido o transversal. Neutralizados T1 e T2, o que resta a diferenciar os tecidos é simplesmente *quantos prótons de hidrogênio* cada um tem por volume.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-62.png",
  largura: 78%,
  legenda: [As três ponderações no mesmo encéfalo. Em *T1* (A), o líquor é preto e a substância branca aparece clara — imagem de aspecto anatômico, boa para desenhar estruturas. Em *densidade de prótons* (B), o contraste entre cinzenta e branca é sutil. Em *T2* (C), o líquor é branco e o parênquima escurece — imagem sensível a água, e portanto a edema, inflamação e a maioria das lesões.])

Essa correspondência tem uma tradução clínica que vale enunciar de uma vez: como quase todo processo patológico do sistema nervoso central envolve aumento de água tecidual — edema citotóxico, edema vasogênico, inflamação, desmielinização, gliose —, as sequências ponderadas em T2 são as mais sensíveis para *detectar* lesão, enquanto as ponderadas em T1 são as melhores para *localizar* a lesão em relação à anatomia. Os dois tipos de imagem se complementam dentro do mesmo exame, pela mesma lógica com que os quatro métodos se complementam entre si.

O contraste da ressonância é o gadolínio, e seu funcionamento não tem paralelo com o iodo. O #termo-nota[gadolínio][metal de terra rara paramagnético usado como meio de contraste em ressonância; encurta os tempos de relaxamento dos tecidos onde se distribui] é altamente tóxico na forma livre e por isso nunca é administrado assim: ele circula quelado a uma molécula que o mantém preso e o conduz até a eliminação renal sem se dissociar. Uma vez distribuído, ele age sobre os tecidos alterando-lhes os tempos de relaxamento — encurta acentuadamente o T1 e alonga o T2 do tecido em que se acumula. Como o exame é feito em ponderação por T1 depois da injeção, o efeito visível é o realce: o tecido que recebeu gadolínio passa a ter T1 curto, recompõe depressa a magnetização longitudinal e devolve muito sinal, aparecendo mais brilhante que o vizinho.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-64.png",
  largura: 62%,
  legenda: [O gadolínio preso ao quelante — a molécula é administrada sempre nessa forma ligada, nunca livre. O efeito sobre o tecido está escrito abaixo: *encurtamento dos tempos de relaxamento*. Repare que o metal não emite sinal; ele muda a propriedade do tecido, e é o tecido que passa a devolver mais sinal.])

#clinica-box("Realce como marcador de barreira rompida", [
  Injetado na veia, o gadolínio circula pelos vasos e alcança o encéfalo — mas o endotélio cerebral tem junções oclusivas que formam a #sigla("BHE", [barreira hematoencefálica — endotélio cerebral com junções oclusivas que restringe a passagem de moléculas do sangue ao parênquima]), e ela impede o contraste de sair do vaso para o parênquima. Num encéfalo íntegro, portanto, o parênquima praticamente não realça. Quando um processo rompe essa barreira — um tumor com neovasos malformados, um abscesso, uma placa de desmielinização em atividade, uma área de inflamação —, o gadolínio extravasa para o interstício daquela região, encurta o T1 local e a área passa a devolver muito mais sinal que o tecido vizinho. Aí está a cadeia inteira: *barreira rompida → gadolínio no interstício → T1 encurtado naquele ponto → hipersinal em T1 pós-contraste*. Vale notar o que o realce diz e o que não diz: ele identifica *onde a barreira falhou*, não qual é a doença — tumor, infecção e inflamação ativa produzem o mesmo achado, e é o contexto clínico somado ao padrão do realce que os separa. É também por isso que estruturas que naturalmente não têm barreira, como a hipófise e os plexos coroides, realçam em qualquer exame normal.
])

Resta o equipamento, que explica por que o exame é caro, demorado e pouco portátil. O campo B#sub[0] é produzido por uma bobina *supercondutora*: um enrolamento de liga de nióbio e titânio que, abaixo de uma temperatura crítica próxima de quatro kelvin, perde praticamente toda a resistência elétrica. Sem resistência, uma corrente enorme circula indefinidamente sem dissipar energia e sustenta um campo intenso e homogêneo com consumo mínimo. O preço é manter essa temperatura, o que se consegue imergindo a bobina em hélio líquido — e é essa exigência criogênica que fixa o aparelho no lugar, encarece a instalação e explica por que não existe ressonância portátil de beira de leito equivalente ao ultrassom.

#figura-nebli("/figuras/radiologia-02-principios-fisicos/rm/slide-68.png",
  largura: 70%,
  legenda: [O magneto supercondutor e suas condições de funcionamento: baixa resistência abaixo da temperatura crítica, liga de nióbio e titânio, banho criogênico de hélio líquido. O ganho está listado ao lado — campo de alta potência, maior homogeneidade e baixo custo operacional depois de instalado.])

Em torno do magneto trabalham três famílias de bobinas, e vale distingui-las porque têm funções diferentes. As *bobinas de radiofrequência* emitem os pulsos que derrubam a magnetização e, em muitos arranjos, também captam o sinal de volta — por isso precisam ficar próximas da região examinada, o que explica os dispositivos específicos que se colocam sobre o crânio, o joelho ou o abdome. As *bobinas de gradiente* aplicam variações controladas de intensidade ao campo principal ao longo dos eixos do corpo: como a frequência de precessão depende da intensidade do campo, criar um gradiente faz cada posição do corpo precessar numa frequência ligeiramente distinta, e é assim que o aparelho descobre *de onde* veio cada sinal recebido. E as bobinas de correção ajustam pequenas heterogeneidades do campo, que nunca é perfeitamente uniforme na prática.

#conclusao-box[
  Um único princípio organiza os quatro métodos: *toda imagem médica é a leitura de uma propriedade física do tecido, e o que a máquina consegue ver é exatamente o que essa propriedade consegue diferenciar*. A radiografia e a tomografia leem quanto o tecido atenua fótons de raio X — e por isso separam bem ar, gordura, água, cálcio e metal, e mal separam vísceras entre si. O ultrassom lê quanto o tecido reflete uma onda mecânica — e por isso distingue líquido de sólido com clareza e é barrado por gás e osso. A ressonância lê como os prótons de hidrogênio do tecido devolvem energia depois de excitados — e por isso enxerga diferenças entre tecidos moles que nenhum dos outros três enxerga.

  O mecanismo nuclear que atravessa o capítulo inteiro é o *contraste*: nenhuma imagem mostra estruturas, ela mostra *diferenças*. É por isso que a aorta desaparece no abdome ao ser cercada de gordura, que a pneumonia apaga a borda do coração quando encosta nela, que o cisto se declara pelo reforço acústico atrás de si, que o cursor separa esteatose de fígado normal na escala de Hounsfield, e que o gadolínio só marca o que já tinha a barreira rompida. Toda vez que uma estrutura some de uma imagem, a pergunta certa é qual diferença deixou de existir.

  Na clínica, isso se traduz numa sequência de decisões encadeadas. A criança com dor abdominal vai para o ultrassom porque a informação necessária é conteúdo líquido e mobilidade, e porque a dose de radiação em tecido jovem se acumula por décadas em efeitos sem limiar. O traumatizado de crânio vai para a tomografia sem contraste porque sangue coagulado está sessenta a noventa unidades acima do líquor e aparece de imediato, e porque o exame termina em segundos. A suspeita de lesão desmielinizante vai para a ressonância porque o que muda na doença é o conteúdo de água, e só a ponderação em T2 lê essa mudança. Escolher o exame é escolher a física que responde à pergunta feita.

  O passo seguinte é aprender a ler cada uma dessas imagens em anatomia normal, antes de procurar doença nelas — reconhecer o mediastino na radiografia de tórax, percorrer os cortes axiais do abdome na tomografia, identificar as estruturas encefálicas nas duas ponderações. É esse repertório de normalidade que transforma o entendimento da física em capacidade de perceber o que está fora do lugar.
]
