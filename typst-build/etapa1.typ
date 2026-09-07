#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
O trato gastrointestinal transporta, mistura e retém conteúdo durante dias sem comando consciente, e faz isso com uma musculatura que se contrai por regras próprias e uma rede nervosa que vive dentro da própria parede. O que este resumo monta é o *aparato* que executa a motilidade — o músculo, a rede que o comanda e o interruptor bioquímico que converte sinal em força. Os padrões motores de cada órgão vêm depois, e vêm apoiados neste aparato.

A *PARTE I* apresenta as peças: o músculo liso visceral acoplado como sincício, o marcapasso que impõe o ritmo, a diferença entre a contração que dura segundos e a que dura horas, e os dois plexos do sistema nervoso entérico com sua divisão de trabalho. A *PARTE II* liga essas peças em circuitos — o reflexo curto, que nasce e morre dentro da parede; o reflexo longo, que sobe ao tronco encefálico e volta pelo nervo vago; e os esfíncteres, cuja regra é o relaxamento comandado pela distensão. A *PARTE III* desce à célula e percorre o caminho que transforma um transmissor liberado por uma varicosidade em força mecânica, além da alavanca que ajusta quanta força sai da mesma quantidade de cálcio.
]

#parte-title("PARTE I — O músculo e a rede nervosa que o comanda", primeira: true)

#subtopico("1.1 — Músculo liso visceral: o sincício e o marcapasso")

Cerca de dois terços do tubo digestório são feitos de músculo liso, e o terço restante é músculo esquelético concentrado nas duas pontas: boca, faringe, terço superior do esôfago e esfíncter anal externo. Essa divisão anatômica já entrega a divisão de controle — as pontas admitem comando voluntário, e todo o percurso entre elas é involuntário.

#figura-lateral("/figuras/motilidade-tgi/fig-tubo.png",
  lado: "left",
  largura-figura: 27%,
  texto: [O miócito liso visceral é fusiforme, mede cerca de 5 µm de diâmetro por 200 a 500 µm de comprimento e não trabalha sozinho. Células vizinhas se conectam por #termo-nota[junções comunicantes][canais formados por conexinas que atravessam as duas membranas e deixam passar íons e moléculas pequenas diretamente de um citoplasma ao outro], e a corrente que despolariza uma célula alcança as vizinhas sem precisar de sinapse. O resultado é um #termo-nota[sincício funcional][conjunto de células individuais, com membranas próprias, que se comporta eletricamente como unidade por estar acoplado por junções comunicantes] — e a palavra *funcional* carrega o peso: as células continuam individuais, com suas membranas intactas, e o que se compartilha é corrente elétrica, não citoplasma.

Esse músculo se organiza em duas camadas com efeitos mecânicos opostos. A camada *circular*, interna, estreita a luz e oclui o segmento; a camada *longitudinal*, externa, encurta o segmento e o traz na direção do conteúdo. Nenhuma das duas transporta nada sozinha: o transporte nasce da alternância entre elas ao longo do eixo do tubo.],
  legenda: [Dois terços de músculo liso entre duas pontas de músculo esquelético.])

O ritmo dessa alternância não vem do miócito. Entre as duas camadas musculares, e em contato com o plexo nervoso que ali corre, existe uma população própria de #termo-nota[células intersticiais de Cajal][células marcapasso de origem mesenquimal, identificadas pelo receptor c-Kit, acopladas ao miócito por junções comunicantes] que despolariza e repolariza espontaneamente. Essa oscilação rítmica do potencial de repouso é a *onda lenta*, com amplitude de 10 a 20 mV, e ela se propaga ao músculo pelas junções comunicantes.

A onda lenta, sozinha, não contrai. Ela apenas leva o potencial de membrana periodicamente para mais perto do limiar, e a contração só ocorre nos ciclos em que estímulos excitatórios somam despolarização suficiente para abrir canais de cálcio tipo L — canais que se abrem com a despolarização e deixam entrar cálcio a favor de um gradiente de cerca de dez mil vezes. A onda lenta define *quando* o segmento pode contrair; a excitação nervosa e hormonal define *se* ele contrai e com que força.

#mini-resumo[A célula de Cajal marca o compasso, a onda lenta abre janelas rítmicas de excitabilidade, e o estímulo nervoso decide quais janelas viram contração.]

A frequência dessas janelas é fixa para cada região e cai no sentido oral-aboral: cerca de 3 por minuto no corpo do estômago, 12 por minuto no duodeno, 8 por minuto no íleo e novamente 3 por minuto no cólon. Como o segmento de trás oscila mais rápido que o da frente, o conteúdo tende a ser deslocado adiante — o gradiente de frequência é, por si, um mecanismo de propulsão. Na gastroparesia de longa evolução do diabetes, a perda dessas células marcapasso desorganiza a onda lenta gástrica e o estômago esvazia devagar mesmo com musculatura íntegra e sem qualquer obstrução mecânica.

#subtopico("1.2 — Contração fásica e contração tônica: dois modos de ocupar o tempo")

Os dois registros de contração do músculo liso partem de um transiente de cálcio quase idêntico e terminam em curvas de força completamente diferentes — e é essa dissociação, e não a intensidade do estímulo, que separa os dois modos.

#figura-nebli("/figuras/motilidade-tgi/fig-fasico-tonico.png",
  largura: 58%,
  legenda: [Em ambos os traçados o cálcio sobe em pico e retorna quase à linha de base em segundos. Na contração fásica (A) a força acompanha essa queda e desaparece; na tônica (B) a força se instala num platô e permanece enquanto durar o estímulo, apesar de o cálcio já ter caído e de a fosforilação das pontes cruzadas ter recuado junto.])

Na *contração fásica*, um estímulo breve produz um pico de cálcio, uma onda de fosforilação das pontes cruzadas e uma força que sobe e decai em segundos. É o registro do antro gástrico e das alças intestinais, onde o trabalho é misturar e propelir em ciclos repetidos, e cada ciclo precisa terminar para que o próximo comece.

Na *contração tônica*, o estímulo é mantido e a força se estabiliza num platô que pode durar minutos ou horas. O cálcio e a velocidade de fosforilação retornam para perto da linha de base logo após o início, mas a força não retorna — sinal de que o mecanismo que sustenta o platô não é o mesmo que o iniciou. É o registro dos esfíncteres e do fundo gástrico, onde a função é manter pressão constante, e não gerar eventos.

A explicação desse platô barato está no #termo-nota[estado latch][condição em que pontes cruzadas de miosina permanecem ligadas à actina após terem sido desfosforiladas, com taxa de desprendimento muito lenta]: as cabeças de miosina que já se ligaram à actina perdem o fosfato mas não se soltam, e passam a ciclar em velocidade muito baixa. Força alta é mantida com pouca fosforilação nova e pouco consumo de ATP — o esfíncter anal interno mantém sua pressão de repouso o dia inteiro sem exaurir a célula.

#confusao-prevista(
  titulo: "Tônico descreve duração, não intensidade",
  aluno_acha: [tônico soa como "contração máxima", e fásico como "contração fraca"],
  mecanismo: [os dois adjetivos classificam o *perfil temporal* da força. Uma contração fásica do antro pode gerar pressão muito maior que o tônus de repouso do esfíncter esofágico inferior; a diferença é que a fásica termina em segundos e a tônica se sustenta. Um mesmo segmento pode alternar entre os dois modos conforme o padrão de estímulo que recebe.],
)

#mini-resumo[O maquinário molecular é o mesmo nos dois modos. O que muda é a duração do estímulo e o balanço entre a quinase que fosforila e a fosfatase que desfosforila — e é do lado desfosforilado, no estado latch, que nasce o tônus econômico.]

#subtopico("1.3 — O sistema nervoso entérico: o plexo que move e o plexo que secreta")

A parede do tubo digestório carrega sua própria rede nervosa, com 200 a 600 milhões de neurônios — número da ordem de grandeza da medula espinhal inteira. Esse #sigla("SNE", [sistema nervoso entérico — a divisão do sistema nervoso autônomo cujos corpos neuronais residem na parede do tubo digestório]) não é um cabo de transmissão de ordens vindas de cima: é um circuito completo, com neurônio sensitivo, interneurônio e motoneurônio, capaz de gerar o programa motor sozinho.

#figura-nebli("/figuras/motilidade-tgi/fig-inervacao.png",
  largura: 66%,
  legenda: [A inervação intrínseca reside na parede e executa o programa; a extrínseca chega de fora e regula ganho. O plexo mioentérico responde por contração e relaxamento, tônico e fásico; o submucoso, por secreção. A ingestão dispara os três desfechos ao mesmo tempo: motilidade, secreção e vasodilatação local.])

O SNE se organiza em dois plexos, e a posição anatômica de cada um prediz sua função. O *plexo mioentérico*, ou de Auerbach, corre exatamente entre a camada circular e a longitudinal — cercado pelo músculo que comanda — e governa contração e relaxamento, tanto fásicos quanto tônicos. O *plexo submucoso*, ou de Meissner, fica sob a mucosa, junto ao epitélio e à rede capilar, e governa secreção e fluxo sanguíneo local. Um plexo está onde precisa estar para mover; o outro, onde precisa estar para secretar.

Os motoneurônios do plexo mioentérico vêm em duas populações antagônicas. Os *excitatórios* liberam acetilcolina e substância P e produzem contração; os *inibitórios* liberam #sigla("VIP", [peptídeo intestinal vasoativo — cotransmissor inibitório do plexo mioentérico, que relaxa músculo liso e aumenta a secreção intestinal]), #sigla("NO", [óxido nítrico — gás sinalizador de meia-vida de segundos, principal mediador do relaxamento do músculo liso digestório]) e #sigla("ATP", [adenosina trifosfato — aqui não como moeda energética, mas como neurotransmissor liberado em vesículas]) e produzem relaxamento. A consequência conceitual é grande: no tubo digestório o relaxamento é um *evento ativo*, com neurônio próprio e transmissor próprio, e não a simples ausência de estímulo excitatório.

A demonstração biológica dessa arquitetura aparece quando ela falha durante a formação. Na aganglionose congênita do cólon, os precursores neuronais da crista neural interrompem a migração craniocaudal antes de completar o trajeto, e o segmento distal — em geral o retossigmoide — fica sem os dois plexos. Sem motoneurônio inibitório, esse segmento não relaxa e permanece contraído; o intestino a montante, inervado e funcionante, empurra contra uma obstrução funcional e se dilata. O segmento dilatado, que é o que chama atenção na imagem, é justamente o *saudável*.

#parte-title("PARTE II — Reflexos: o tubo que decide sozinho e o tubo que consulta o encéfalo")

#subtopico("2.1 — O reflexo curto: o circuito inteiro dentro da parede")

O plexo mioentérico apresentado no subtópico anterior não é apenas uma via de saída motora: ele fecha o arco reflexo completo sem sair da parede. O receptor, o interneurônio e o motoneurônio estão todos intramurais, e é por isso que esse circuito é chamado de *reflexo curto*, ou reflexo intramural.

O estímulo que abre o circuito é mecânico. A chegada de conteúdo distende a parede, e *mecanorreceptores* — terminações que respondem a estiramento, e não à composição química do que passa — despolarizam o #termo-nota[neurônio aferente primário intrínseco][neurônio sensitivo cujo corpo celular fica no próprio plexo mioentérico, sem qualquer projeção para fora da parede do tubo]. Esse aferente ativa interneurônios que distribuem o sinal ao longo do eixo do tubo, e são os interneurônios que decidem qual motoneurônio recrutar de cada lado do bolo.

Essa decisão é assimétrica, e a assimetria é o que dá direção ao transporte. No segmento *oral* ao bolo, os interneurônios recrutam motoneurônios excitatórios: a acetilcolina e a substância P contraem a camada circular, e a luz se estreita atrás do conteúdo. No segmento *aboral*, recrutam motoneurônios inibitórios: o VIP e o óxido nítrico relaxam a circular à frente, e a luz se abre. Contrai atrás, relaxa adiante — o conteúdo é empurrado para o único lugar de menor resistência. Essa polarização estereotipada é conhecida como *lei do intestino*.

#figura-nebli("/figuras/motilidade-tgi/fig-reflexos.png",
  largura: 72%,
  legenda: [Dois arcos partem do mesmo estímulo. À esquerda, o reflexo curto se resolve dentro da parede: mecanorreceptor, neurônio sensitivo intrínseco e motoneurônio excitatório (acetilcolina) ou inibitório (VIP). À direita, o mesmo enchimento recruta o aferente vagal, que sobe ao tronco encefálico e retorna pela fibra parassimpática — o reflexo longo, ou vago-vagal. Os dois operam ao mesmo tempo sobre o mesmo músculo.])

Um segmento de intestino retirado do organismo, colocado em banho fisiológico e sem nenhuma conexão nervosa com o exterior, ainda propaga conteúdo na direção correta quando distendido. Esse experimento é a demonstração direta de que o programa motor é intrínseco e de que o comando externo, quando existe, modula intensidade — não cria o movimento.

O repertório químico da parede vai além dos dois pares clássicos. A serotonina liberada pelas células enterocromafins da mucosa sinaliza distensão e presença de nutriente aos aferentes intrínsecos; catecolaminas, ATP e ácido gama-aminobutírico participam da modulação sináptica dentro dos plexos; e o óxido nítrico, por ser um gás de meia-vida de segundos que difunde direto pela membrana, age apenas nas células imediatamente vizinhas ao terminal que o produziu — o que dá ao relaxamento uma precisão espacial que um transmissor circulante não teria.

#clinica-box("Quando o plexo mioentérico é destruído", [
O #termo-nota[Trypanosoma cruzi][protozoário causador da doença de Chagas, transmitido por triatomíneos, cuja fase crônica pode destruir os plexos intramurais do tubo digestório] provoca, na fase crônica, destruição inflamatória progressiva dos neurônios do plexo mioentérico. A perda não é uniforme entre as duas populações motoras: os neurônios *inibitórios*, produtores de VIP e óxido nítrico, são desproporcionalmente atingidos.

A consequência mecânica segue direto do que este subtópico montou. Sem o ramo inibitório, o segmento perde a capacidade de relaxar à frente do bolo e os esfíncteres perdem a capacidade de se abrir, enquanto o tônus excitatório permanece. O esôfago não consegue vencer um esfíncter esofágico inferior que não relaxa, e se dilata progressivamente acima dele — o megaesôfago. No cólon, o mesmo defeito produz retenção fecal crônica e dilatação do segmento a montante — o megacólon. As duas apresentações são a mesma lesão em dois endereços, e ambas ilustram que a rede intramural, uma vez perdida, não é substituída pelo comando extrínseco que continua intacto.
])

#subtopico("2.2 — O reflexo longo vago-vagal e o comando extrínseco")

O reflexo longo percorre o mesmo estímulo por um trajeto muito maior. A distensão da parede ativa terminações vagais aferentes, cujos corpos celulares estão no gânglio nodoso; a informação sobe ao núcleo do trato solitário, no bulbo, e é retransmitida ao núcleo motor dorsal do vago, de onde parte a resposta eferente pelo mesmo nervo. Por entrar e sair pelo vago, o circuito recebe o nome de *reflexo vago-vagal*.

Dois detalhes anatômicos explicam por que esse arco é regulador, e não executor. O primeiro é a proporção de fibras: cerca de 80% das fibras do vago abdominal são *aferentes*, o que faz do nervo muito mais um relator do estado do tubo do que um emissor de ordens. O segundo é onde a via eferente termina. A fibra parassimpática pré-ganglionar é longa, colinérgica, e não alcança o miócito: ela faz sinapse em um neurônio do plexo mioentérico, que é quem inerva o músculo. O comando extrínseco entra no circuito intrínseco e ajusta seu ganho.

O ramo simpático chega por outro caminho e com o sinal invertido. Fibras pós-ganglionares oriundas dos gânglios celíaco e mesentéricos liberam noradrenalina, e boa parte do efeito inibitório não é exercida sobre a fibra muscular: a noradrenalina age em receptores adrenérgicos alfa-2 pré-sinápticos do neurônio entérico e *reduz a liberação de acetilcolina*. A inibição simpática opera principalmente cortando o suprimento excitatório na origem.

#mini-resumo[Parassimpático estimula, simpático inibe — mas nenhum dos dois fala diretamente com o músculo. Ambos terminam no neurônio entérico, que é o executor final comum.]

O efeito simpático, porém, não é uniformemente inibitório ao longo da parede. O mesmo comando relaxa a musculatura das camadas circular e longitudinal, *contrai* os esfíncteres e produz vasoconstrição na mucosa. Os três efeitos são coerentes com a mesma finalidade: durante uma resposta de estresse, interromper o transporte, fechar as passagens e desviar fluxo sanguíneo para músculo esquelético e encéfalo. Sinais opostos em tecidos vizinhos servem a um objetivo único.

A potência desse ramo inibitório fica visível depois de uma laparotomia. A manipulação do peritônio dispara aferentes que ativam, por arco espinhal, uma descarga simpática intensa e prolongada sobre todo o tubo, e a motilidade cessa — é o íleo paralítico pós-operatório. Não há lesão estrutural do intestino, e a recuperação segue uma ordem previsível que reflete a sensibilidade de cada segmento: o intestino delgado retoma em horas, o estômago em cerca de um a dois dias, e o cólon em três a cinco dias.

#subtopico("2.3 — Esfíncteres: tônus de repouso e o relaxamento comandado pela distensão")

O esfíncter não é um anel que se fecha quando o conteúdo chega — ele já está fechado. Seu estado basal é contração tônica sustentada, e o evento fisiológico que a chegada do conteúdo produz é o *relaxamento*. Inverter esses dois estados desorganiza a leitura de toda a fisiologia dos esfíncteres.

#figura-nebli("/figuras/motilidade-tgi/fig-esfincteres.png",
  largura: 56%,
  legenda: [Cinco zonas de alta pressão dividem o tubo em compartimentos com pH, flora e pressões próprios. A distensão a montante relaxa o esfíncter seguinte; no piloro, a regulação é dupla e as duas fontes de sinal têm efeitos opostos.])

#atencao-box("O estado basal do esfíncter é contração", [
Um esfíncter em repouso está *contraído*, e essa contração tônica é o que mantém compartimentos vizinhos separados: ela impede que o ácido do estômago suba ao esôfago, que o quimo desça ao duodeno antes de processado, que o conteúdo colônico reflua ao íleo e que as fezes escapem do reto.

O erro de leitura tem consequência direta na interpretação da doença. Um esfíncter que "não funciona" pode falhar de dois modos opostos: por perder o tônus, e então há refluxo do compartimento de trás; ou por não conseguir relaxar, e então há obstrução funcional com dilatação a montante. São defeitos contrários, e só se distinguem se o estado basal correto estiver claro.
])

O tubo tem cinco desses controles. O *esfíncter esofágico superior* é esquelético e mantém o esôfago fechado à entrada de ar durante a respiração. O #sigla("EEI", [esfíncter esofágico inferior — zona de alta pressão na transição esofagogástrica, sem espessamento muscular macroscópico distinto, identificada por manometria]) é liso e separa o esôfago do ambiente ácido gástrico. O *piloro* controla a saída do estômago; a *valva ileocecal* separa o íleo do ceco; e o complexo anal reúne um esfíncter interno, liso e involuntário, e um externo, esquelético e voluntário, inervado pelo nervo pudendo.

O sinal que abre esses controles é a distensão do segmento imediatamente a montante, e o mediador do relaxamento é o mesmo já conhecido: os motoneurônios inibitórios do plexo mioentérico, com VIP e óxido nítrico. A deglutição relaxa o EEI antes que o bolo chegue; a distensão do reto relaxa o esfíncter anal interno; a distensão do íleo terminal relaxa a valva ileocecal, enquanto a distensão do ceco a contrai, o que impede refluxo de conteúdo colônico rico em bactérias para o íleo.

O piloro recebe as duas informações de lados opostos, e responde a cada uma com o sinal contrário. A distensão do antro gera regulação *anterógrada*, que o relaxa e favorece o esvaziamento gástrico. A chegada de quimo ácido, hipertônico ou rico em gordura ao duodeno gera regulação *retrógrada*, que o contrai e freia o esvaziamento. O estômago não entrega conteúdo na velocidade em que o produz: entrega na velocidade em que o duodeno consegue neutralizar e absorver.

O EEI mostra a mesma economia funcionando na direção do erro. Fora da deglutição, ele apresenta episódios de *relaxamento transitório* — quedas espontâneas de pressão, mediadas por reflexo vago-vagal disparado pela distensão do fundo gástrico, cuja função fisiológica é permitir a eructação de gás. Quando esses episódios se tornam frequentes ou o tônus basal é baixo, é por essa mesma porta que o conteúdo ácido alcança o esôfago na doença do refluxo gastroesofágico.

#parte-title("PARTE III — Da membrana à força: o acoplamento excitação-contração")

#subtopico("3.1 — A junção neuroefetora: a sinapse sem endereço fixo")

O terminal autônomo que inerva o músculo liso não termina em botão sobre uma célula: ele atravessa o tecido como um colar de contas. Ao longo do axônio pós-ganglionar, dilatações espaçadas chamadas *varicosidades* acumulam vesículas e mitocôndrias e liberam transmissor por toda a extensão do trajeto.

#figura-lateral("/figuras/motilidade-tgi/fig-juncao.png",
  lado: "right",
  largura-figura: 36%,
  texto: [A comparação com a placa motora do músculo esquelético mede a diferença. No esquelético, a acetilcolina cai numa fenda de cerca de 50 nm sobre uma membrana pós-sináptica pregueada e densa em receptores, e cada axônio comanda apenas as fibras da sua unidade motora. Na junção neuroefetora visceral não existe especialização pós-sináptica alguma: não há placa, não há concentração local de receptor, e a distância entre a varicosidade e o miócito varia de 20 nm a mais de 100 nm.],
  legenda: [Varicosidades ao longo do axônio, sem placa motora.])

Três consequências saem dessa geometria. A resposta é *lenta*, porque o transmissor precisa difundir por uma fenda ampla até encontrar receptores dispersos. É *graduada*, porque a quantidade que alcança cada célula depende da distância, e não de um evento tudo-ou-nada. E é *difusa*, porque uma única varicosidade banha muitas células ao mesmo tempo — e o sincício elétrico montado no subtópico 1.1 espalha ainda mais a resposta, recrutando células que sequer receberam transmissor.

O contraste rende uma imagem útil: a placa motora funciona como uma seringa, que entrega dose exata a um destinatário único; a varicosidade funciona como um regador, que molha uma área e atinge quem estiver nela. O músculo esquelético precisa de precisão porque move ossos contra a gravidade; o músculo visceral precisa de coordenação em massa porque move conteúdo dentro de um tubo.

A mesma varicosidade não é fiel a um único transmissor. Acetilcolina, VIP, óxido nítrico, ATP, serotonina, catecolaminas e ácido gama-aminobutírico saem de terminais do mesmo circuito, e é essa variedade química que permite ao plexo produzir contração em um ponto e relaxamento em outro poucos milímetros adiante, com o mesmo arco reflexo.

#subtopico("3.2 — Cálcio, calmodulina e a cadeia leve da miosina")

O cálcio que a excitação faz entrar precisa agora virar força, e o caminho que ele percorre no músculo liso não é o do músculo estriado. O íon chega de duas fontes: entra do meio extracelular pelos canais tipo L abertos pela despolarização, e sai do retículo sarcoplasmático, que o mantém estocado. A concentração citosólica sobe de cerca de 100 nM em repouso para a faixa de 1 µM.

#figura-nebli("/figuras/motilidade-tgi/fig-calmodulina.png",
  largura: 62%,
  legenda: [Quatro íons cálcio ocupam a calmodulina e mudam sua conformação. O complexo cálcio-calmodulina liga-se à quinase da cadeia leve da miosina e a ativa; ela transfere fosfato do ATP para a cadeia leve reguladora, e a cabeça de miosina passa de inativa a ativa — apta a ligar actina e ciclar.])

O músculo liso *não tem troponina*. Quem recebe o cálcio é a #termo-nota[calmodulina][proteína citosólica ligante de cálcio, presente em praticamente toda célula eucariótica, que atua como sensor e transmite o sinal ativando enzimas-alvo], que liga quatro íons e, por isso, ativa de forma abrupta dentro da faixa fisiológica de concentração. O complexo cálcio-calmodulina ativa a #sigla("MLCK", [quinase da cadeia leve da miosina — enzima que fosforila a serina 19 da cadeia leve reguladora e habilita a cabeça de miosina]), e a MLCK transfere um fosfato do ATP para a serina 19 da cadeia leve reguladora da miosina.

A diferença conceitual com o estriado está exatamente aqui. No músculo estriado a regulação é feita sobre o *filamento fino*: o cálcio liga-se à troponina C e desloca a tropomiosina, liberando sítios da actina. No liso a regulação é feita sobre o *filamento grosso*: a fosforilação libera a atividade ATPásica da própria cabeça de miosina, que só então consegue ligar actina e ciclar pontes cruzadas. Não há troponina para desviar tropomiosina alguma — a actina já está disponível, e quem estava desligado era o motor.

#figura-nebli("/figuras/motilidade-tgi/fig-cascata-ca.png",
  largura: 68%,
  legenda: [O mesmo esquema lido nos dois sentidos. À esquerda, o cálcio sobe, ativa a calmodulina e a quinase, e a cadeia leve fosforilada produz contração. À direita, a extrusão devolve o cálcio ao meio extracelular e ao retículo, a quinase perde atividade — e é a miosina fosfatase, no canto, que efetivamente remove o fosfato e encerra a contração.])

O caminho de volta tem duas etapas, e omitir a segunda é o erro mais caro deste subtópico. A primeira é retirar o cálcio do citosol: a Ca²⁺-ATPase da membrana plasmática o bombeia para fora, o trocador sódio-cálcio o expulsa aproveitando o gradiente de sódio que a Na⁺/K⁺-ATPase mantém, e a Ca²⁺-ATPase do retículo sarcoplasmático o recolhe de volta ao estoque interno. Com cálcio baixo, a calmodulina se desocupa e a MLCK deixa de fosforilar.

#atencao-box("Cálcio baixo não é relaxamento", [
Cessar a fosforilação *nova* não desfaz a fosforilação *existente*. Enquanto a serina 19 permanecer fosforilada, a cabeça de miosina continua apta a ciclar e a força se mantém — foi exatamente isso que o traçado da contração tônica mostrou no subtópico 1.2, com o cálcio já de volta à linha de base e a força ainda em platô.

Quem encerra a contração é a #sigla("MLCP", [fosfatase da cadeia leve da miosina — enzima que remove o fosfato da serina 19 e devolve a cabeça de miosina ao estado inativo]), removendo o fosfato. Contração e relaxamento não são "cálcio alto" e "cálcio baixo": são o resultado da disputa entre a MLCK e a MLCP pelo estado de fosforilação da mesma serina. Essa é a razão pela qual o próximo subtópico consegue mudar a força sem mudar o cálcio.
])

#subtopico("3.3 — O receptor acoplado à proteína G e a sensibilização ao cálcio")

A disputa entre quinase e fosfatase que fechou o subtópico anterior tem um regulador, e ele chega pelo mesmo receptor que faz o cálcio subir. Um #sigla("GPCR", [receptor acoplado à proteína G — proteína de sete domínios transmembrana que, ao ligar o agonista, troca GDP por GTP na subunidade alfa da proteína G associada]) ativado por acetilcolina no receptor muscarínico M3 recruta duas proteínas G distintas, com desfechos diferentes.

#figura-nebli("/figuras/motilidade-tgi/fig-gpcr.png",
  largura: 70%,
  legenda: [Dois braços a partir do mesmo receptor. À esquerda, Gq ativa a fosfolipase C beta, e o IP₃ liberta cálcio do retículo — o braço que *aumenta o sinal*. À direita, G12/13 ativa RhoA e a Rho-quinase, que inibem a miosina fosfatase — o braço que *retira o freio*. A soma é mais força para a mesma quantidade de cálcio.])

A proteína Gq ativa a fosfolipase C beta, que parte o PIP₂ da membrana em dois mensageiros: o #sigla("IP₃", [inositol 1,4,5-trifosfato — mensageiro solúvel que abre canais de cálcio no retículo sarcoplasmático]), solúvel, que abre os canais de cálcio do retículo sarcoplasmático; e o #sigla("DAG", [diacilglicerol — mensageiro que permanece na membrana e ativa a proteína quinase C]), que fica na membrana e ativa a proteína quinase C. Esse braço eleva o cálcio e, pelo caminho do subtópico anterior, a fosforilação e a força.

O segundo braço não toca no cálcio. A proteína G12/13 ativa um fator de troca de nucleotídeo de guanina, que troca GDP por GTP na pequena GTPase RhoA; a RhoA ativa a *Rho-quinase*, que fosforila a subunidade reguladora da MLCP, inibindo-a. Em paralelo, tanto a Rho-quinase quanto a proteína quinase C ativam a proteína CPI-17, inibidor endógeno da mesma fosfatase. O resultado é uma fosfatase desligada por duas frentes.

#mini-resumo[Inibir a fosfatase produz mais força sem exigir mais cálcio: com menos remoção de fosfato, a mesma taxa de fosforilação acumula mais cadeias leves fosforiladas.]

Esse deslocamento da relação entre cálcio e força chama-se #termo-nota[sensibilização ao cálcio][aumento da força gerada para uma dada concentração de cálcio citosólico, obtido por inibição da fosfatase da cadeia leve em vez de elevação do próprio cálcio], e é o que torna sustentável o tônus dos esfíncteres: manter cálcio alto por horas seria tóxico e caro em ATP, enquanto manter a fosfatase inibida custa pouco.

O mesmo eixo funciona na direção oposta e fecha o circuito aberto na PARTE II. O óxido nítrico dos motoneurônios inibitórios difunde para o miócito e ativa a guanilato-ciclase solúvel, que produz #sigla("GMPc", [monofosfato cíclico de guanosina — segundo mensageiro que ativa a proteína quinase G e medeia o relaxamento do músculo liso]); este ativa a proteína quinase G, que reduz o cálcio e *favorece* a miosina fosfatase. O transmissor que a rede entérica usa para relaxar age sobre a mesma alavanca que a Rho-quinase usa para contrair.

#clinica-box("A alavanca molecular na acalásia", [
Na acalásia, a perda dos motoneurônios inibitórios do plexo mioentérico esofágico retira o VIP e o óxido nítrico que relaxariam o EEI. O esfíncter permanece hipertônico, o esôfago não vence a resistência e se dilata acima dela.

As três abordagens atacam elos distintos da mesma cadeia. O *bloqueador de canal de cálcio* impede a entrada do íon pelos canais tipo L e reduz o substrato da calmodulina. O *nitrato* doa óxido nítrico e repõe o mediador que falta, ativando a guanilato-ciclase solúvel e a proteína quinase G — reforça, portanto, a fosfatase responsável pelo relaxamento. A *toxina botulínica* cliva proteínas SNARE e bloqueia a liberação de acetilcolina pelos terminais excitatórios remanescentes. Nenhuma das três recupera o neurônio perdido, e por isso o efeito é temporário.
])

#conclusao-box[
A motilidade do tubo digestório resulta de três decisões tomadas em níveis diferentes. *Quando* o segmento pode contrair é decidido pelo oscilador das células intersticiais de Cajal, cuja onda lenta abre janelas rítmicas de excitabilidade com frequência própria de cada região. *Onde e em que direção* a contração acontece é decidido pela rede intramural, que fecha arcos reflexos completos dentro da parede e os polariza — excitatório atrás do bolo, inibitório à frente. *Quanta força* sai de cada contração é decidido na célula muscular, pelo balanço entre a quinase e a fosfatase que disputam a cadeia leve da miosina. O comando extrínseco não substitui nenhuma das três: entra em cada uma ajustando ganho, e termina sempre no neurônio entérico.

O ponto de convergência mecanística é uma única serina. A onda lenta, o cálcio que entra pelo canal tipo L, o IP₃ que o liberta do retículo, a calmodulina com seus quatro sítios e a Rho-quinase que desliga a fosfatase convergem todos para o estado de fosforilação da serina 19 da cadeia leve reguladora. E porque a fosfatase é regulável de forma independente do cálcio, o mesmo aparato produz tanto a contração fásica que dura segundos quanto o tônus de esfíncter que dura horas, sem que o custo energético acompanhe a força.

As doenças percorridas confirmam a arquitetura ao quebrá-la em endereços distintos: Chagas e aganglionose removem os motoneurônios inibitórios da rede, a acalásia faz o mesmo restrito ao esôfago, e a gastroparesia atinge o oscilador poupando músculo e inervação. Em todas, o segmento doente é o que não relaxa, e o dilatado é o vizinho íntegro empurrando contra ele.

O passo seguinte é ver esse aparato produzir repertório — deglutição, relaxamento receptivo, moagem antral, segmentação, peristalse, complexo motor migratório e defecação. Nenhum desses padrões acrescenta peça nova: todos são arranjos das peças entregues aqui.
]
