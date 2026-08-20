#import "../typst-template/nebli_v2_apostila.typ": *

#questao-mc("01", badge-consolidacao,
  [Por que um aparelho de raios X deixa de emitir radiação no instante em que é desligado, enquanto um radionuclídeo continua emitindo indefinidamente.],
  (("A", [Porque o tubo armazena os fótons produzidos numa câmara interna revestida de chumbo, liberando-os apenas enquanto o disparo está acionado e retendo o restante depois do desligamento.]),
   ("B", [Porque o alvo metálico do tubo é composto por isótopos de meia-vida muito curta, que decaem completamente em frações de segundo assim que a corrente elétrica deixa de percorrê-los.]),
   ("C", [Porque a emissão depende de elétrons acelerados por diferença de potencial que freiam no alvo; sem tensão aplicada não há elétron acelerado, e sem freio no alvo nenhum fóton é produzido.]),
   ("D", [Porque o feixe é gerado pela colisão entre fótons cósmicos e o filamento aquecido, processo que exige aquecimento contínuo do catodo e cessa quando o filamento esfria abaixo do limiar.]),
   ("E", [Porque o revestimento de chumbo absorve integralmente a radiação residual produzida pelo alvo após o desligamento, de modo que a emissão continua ocorrendo mas não escapa da ampola.])))

#questao-mc("02", badge-consolidacao,
  [O que explica o cálcio do osso atenuar muito mais o feixe que o músculo adjacente, sendo ambos tecidos do mesmo corpo e atravessados pelo mesmo feixe.],
  (("A", [O cálcio tem número atômico bem mais alto que os elementos predominantes no músculo, e átomos com mais elétrons interceptam proporcionalmente mais fótons ao longo do mesmo trajeto.]),
   ("B", [O osso é atravessado por um feixe de energia diferente, porque o colimador ajusta automaticamente a tensão aplicada conforme o tecido encontrado em cada ponto da projeção.]),
   ("C", [O músculo contém água em abundância, e a água transmite os fótons por refração interna, desviando o feixe lateralmente antes que ele alcance a superfície do detector.]),
   ("D", [A matriz óssea reflete os fótons de volta em direção ao tubo, como faz uma interface acústica, e por isso pouco feixe remanescente chega até o detector posterior.]),
   ("E", [O cálcio é magnético e desvia o feixe de raios X pelo campo que gera, ao passo que o músculo é neutro e permite a passagem retilínea dos fótons até o detector.])))

#questao-ce("03", badge-consolidacao,
  [Julgue os itens sobre a formação da imagem radiográfica como projeção.],
  (("I",   [Uma única incidência não permite dizer se uma opacidade no campo pulmonar está na pele do dorso, no parênquima ou na parede anterior do tórax.]),
   ("II",  [Estruturas alinhadas ao longo do trajeto do feixe são registradas em pontos separados da imagem, o que dispensa a segunda incidência quando o campo examinado é pequeno.]),
   ("III", [A incidência em perfil recupera o eixo ântero-posterior e, em contrapartida, perde a separação entre o lado direito e o lado esquerdo do paciente.]),
   ("IV",  [Por convenção de apresentação, o lado direito do paciente é exibido à esquerda da imagem, tanto na radiografia quanto na tomografia.])))

#questao-mc("04", badge-consolidacao,
  [Por que a ausência de gel entre o transdutor e a pele impede por completo a formação da imagem ultrassonográfica.],
  (("A", [Porque o gel funciona como meio de baixa viscosidade que reduz o atrito e permite ao operador varrer a região com velocidade constante, condição exigida pelo cálculo da profundidade.]),
   ("B", [Porque o gel contém partículas refletoras calibradas que devolvem um eco de referência, usado pelo aparelho para ajustar automaticamente o ganho de cada linha da imagem formada.]),
   ("C", [Porque o gel resfria os cristais piezoelétricos, que sem refrigeração aqueceriam a ponto de perder a propriedade de converter estímulo elétrico em deformação mecânica útil.]),
   ("D", [Porque o gel conduz a corrente elétrica gerada pelos cristais até a pele do paciente, fechando o circuito necessário para que a onda mecânica seja emitida dentro do tecido.]),
   ("E", [Porque a película de ar entre transdutor e pele refletiria quase todo o feixe logo na entrada, e o gel a substitui por um meio de propriedades acústicas próximas às do tecido.])))

#questao-mc("05", badge-consolidacao,
  [Sobre a frequência do transdutor e a escolha do aparelho conforme a profundidade do alvo, assinale a alternativa *incorreta*:],
  (("A", [O transdutor linear, de frequência mais alta, é adequado a estruturas superficiais como tireoide, mama e vasos do pescoço, porque o ganho de detalhe compensa a menor penetração.]),
   ("B", [Elevar a frequência do transdutor em paciente com muito tecido adiposo recupera o detalhe perdido, porque frequências altas atravessam a gordura com menos atenuação que as baixas.]),
   ("C", [O transdutor convexo, de frequência mais baixa, é o escolhido para o abdome, porque precisa alcançar fígado, rim e retroperitônio a vários centímetros de profundidade da pele.]),
   ("D", [Frequências altas produzem comprimento de onda curto e por isso separam melhor dois pontos vizinhos, entregando imagem mais nítida que a obtida com frequências baixas.]),
   ("E", [O transdutor endocavitário opera em frequência mais alta que o abdominal, porque a introdução aproxima sua face do órgão-alvo e reduz muito a distância a percorrer.])))

#questao-ce("06", badge-consolidacao,
  [Julgue os itens sobre a escala Hounsfield e o que ela mede.],
  (("I",   [A escala atribui à gordura valores positivos, porque o tecido adiposo atenua mais o feixe que a água tomada como referência.]),
   ("II",  [O líquor tem valor próximo de zero, ao passo que o sangue coagulado se situa entre sessenta e cinco e noventa e cinco unidades.]),
   ("III", [A água vale zero por definição da fórmula, que subtrai do coeficiente do tecido o coeficiente da água e divide o resultado por este último.]),
   ("IV",  [Um voxel que contenha metade osso e metade tecido mole registra dois valores distintos, um para cada componente presente no seu interior.])))

#questao-mc("07", badge-consolidacao,
  [Como o ajuste de janela e nível permite ao observador extrair mais informação de um mesmo conjunto de dados tomográficos já adquiridos.],
  (("A", [Aumentando a resolução espacial da aquisição, o que reduz a espessura efetiva do corte e revela estruturas que estavam diluídas na média de volume de cada voxel.]),
   ("B", [Recalculando os coeficientes de atenuação a partir dos dados brutos com um algoritmo diferente, o que corrige valores distorcidos por endurecimento do feixe e por movimento.]),
   ("C", [Aplicando um filtro que multiplica a atenuação dos tecidos de interesse por um fator fixo, elevando o contraste entre eles sem alterar o restante da imagem exibida.]),
   ("D", [Restringindo a faixa de atenuações que recebe a escala de cinzas, o que amplia o contraste dentro dessa faixa e satura em branco e preto tudo o que ficou fora dela.]),
   ("E", [Convertendo a escala de cinzas em escala de cores, o que contorna o limite de discriminação do olho humano e permite distinguir simultaneamente todas as atenuações registradas.])))

#questao-ce("08", badge-consolidacao,
  [Julgue os itens sobre os fundamentos físicos do sinal na ressonância magnética.],
  (("I",   [O hidrogênio é usado na formação da imagem porque está distribuído por todos os tecidos e porque sua proporção varia entre tecido normal e tecido doente.]),
   ("II",  [O momento magnético do próton decorre de sua rotação: carga em movimento gera corrente elétrica, e corrente elétrica gera campo magnético.]),
   ("III", [Dentro do campo magnético do aparelho, os prótons se alinham exclusivamente em sentido paralelo a ele, sem qualquer população orientada em sentido oposto.]),
   ("IV",  [O pulso de radiofrequência tem energia insuficiente para arrancar elétrons dos átomos e, portanto, não produz ionização nos tecidos atravessados.])))

#questao-mc("09", badge-integracao,
  [Comparando a escala de densidades da radiografia com a escala Hounsfield da tomografia, a diferença mecanística decisiva entre as duas é que:],
  (("A", [a radiografia entrega um cinza comparativo, dependente do vizinho, enquanto a tomografia atribui a cada voxel um valor ancorado na água, mensurável e comparável entre exames diferentes.]),
   ("B", [a radiografia mede atenuação e a tomografia mede reflexão do feixe, de modo que uma escala descreve absorção de fótons e a outra descreve interfaces entre meios distintos.]),
   ("C", [a escala radiográfica tem cinco degraus fixos e a escala Hounsfield tem exatamente duzentos e cinquenta e seis, correspondentes aos tons de cinza que o monitor consegue exibir.]),
   ("D", [a tomografia dispensa a correção pela espessura atravessada, porque o giro do tubo compensa automaticamente a distância percorrida pelo feixe em cada direção de projeção.]),
   ("E", [a radiografia depende do número atômico do material atravessado e a tomografia depende apenas da densidade física, em gramas por centímetro cúbico, do tecido examinado.])))

#questao-ce("10", badge-integracao,
  [Julgue os itens que comparam a formação da imagem na radiografia e na tomografia computadorizada.],
  (("I",   [Na radiografia, estruturas situadas em profundidades diferentes ao longo do feixe se somam num mesmo ponto da imagem; na tomografia, a aquisição volumétrica desfaz essa soma.]),
   ("II",  [As reconstruções sagital e coronal da tomografia exigem novas passagens do paciente pelo gantry e, portanto, acrescentam dose de radiação ao exame.]),
   ("III", [Adquirir uma fase arterial e uma fase portal equivale a reconstruir o mesmo conjunto de dados brutos em dois planos diferentes.]),
   ("IV",  [Cortes mais espessos aumentam o efeito de média de volume, o que prejudica a representação de estruturas pequenas dentro do voxel.])))

#questao-mc("11", badge-integracao,
  [A gordura aparece escura na radiografia e clara na ultrassonografia do mesmo paciente. O que explica essa aparente contradição:],
  (("A", [a gordura muda de composição química quando submetida a ondas mecânicas, adquirindo temporariamente propriedades de reflexão que não possui diante de fótons de alta energia.]),
   ("B", [o ultrassom mede a densidade física do tecido e a radiografia mede sua densidade eletrônica, grandezas que, no caso do tecido adiposo, apontam em sentidos exatamente opostos.]),
   ("C", [a convenção de exibição do ultrassom é invertida em relação à da radiografia, de modo que qualquer estrutura aparece com o tom oposto quando se troca um método pelo outro.]),
   ("D", [a gordura tem número atômico alto o suficiente para atenuar fortemente o feixe de raios X, mas baixo demais para refletir a onda mecânica emitida pelo transdutor.]),
   ("E", [as duas escalas medem fenômenos distintos: a radiografia mede quanto o tecido absorve fótons, e o ultrassom mede quanto ele reflete onda mecânica nas suas muitas interfaces internas.])))

#questao-mc("12", badge-integracao,
  [Um cálculo biliar projeta sombra acústica no ultrassom e uma prótese metálica produz estriamento na tomografia. Comparando os dois artefatos:],
  (("A", [ambos resultam da mesma causa física, que é a reflexão especular do feixe incidente na superfície do material, e por isso desaparecem quando se altera o ângulo de incidência.]),
   ("B", [ambos decorrem de movimento do paciente durante a aquisição, e por isso são eliminados quando o exame é feito em apneia ou sob sedação adequada do paciente examinado.]),
   ("C", [na sombra falta feixe remanescente para gerar ecos atrás do cálculo; no estriamento, o metal absorve os fótons de menor energia e o feixe remanescente chega endurecido à reconstrução.]),
   ("D", [ambos são causados por saturação do detector, que recebe energia acima da sua faixa de leitura e devolve valores nulos para toda a região situada além do material atravessado.]),
   ("E", [na sombra o feixe é integralmente absorvido pelo cálculo, e no estriamento o metal emite radiação secundária que se soma ao feixe primário e satura os detectores vizinhos.])))

#questao-ce("13", badge-integracao,
  [Julgue os itens sobre os tempos de relaxamento e o comportamento dos tecidos na ressonância magnética.],
  (("I",   [O relaxamento T2 começa apenas depois de completado o relaxamento T1, e por isso os dois nunca são observados simultaneamente.]),
   ("II",  [A gordura recupera depressa a magnetização longitudinal e perde depressa a transversal, o que a caracteriza como tecido de T1 curto e T2 curto.]),
   ("III", [A água livre demora a recompor o eixo longitudinal e mantém a coerência de fase por mais tempo, o que a caracteriza como tecido de T1 e T2 longos.]),
   ("IV",  [O hidrogênio serve à formação da imagem porque seu núcleo tem número ímpar de prótons, o que deixa um momento magnético resultante que não se anula.])))

#questao-mc("14", badge-integracao,
  [Por que a preferência pelo ultrassom em criança com dor abdominal se apoia em radiobiologia, e não apenas em custo e disponibilidade:],
  (("A", [porque o tecido pediátrico repara o dano ao material genético com eficiência menor que o do adulto, o que torna determinística uma lesão que no adulto seria apenas estocástica.]),
   ("B", [porque a indução de neoplasia é efeito estocástico, sem limiar conhecido, e a probabilidade acumulada ao longo de décadas é maior quanto mais cedo na vida a dose for recebida.]),
   ("C", [porque o ultrassom, ao usar onda mecânica de alta frequência, promove reparo do dano previamente acumulado nos tecidos irradiados em exames anteriores do mesmo paciente.]),
   ("D", [porque a criança apresenta limiar de dose mais baixo para efeitos determinísticos como catarata e queimadura, que são as complicações esperadas de um exame radiográfico simples.]),
   ("E", [porque o efeito indireto da radiação depende do conteúdo de água tecidual, que é praticamente nulo na criança e por isso não gera radicais livres em quantidade relevante.])))

#questao-mc("15", badge-integracao,
  [Sobre a exibição da escala de cinzas nos métodos que usam raios X, assinale a alternativa *incorreta*:],
  (("A", [Na radiografia, por convenção, o material radiotransparente é exibido escuro e o radiopaco é exibido claro, embora os equipamentos atuais permitam inverter essa escala.]),
   ("B", [Na tomografia, o nível define o centro da faixa de atenuações exibida e a janela define a largura dessa faixa, ambos expressos em unidades Hounsfield.]),
   ("C", [Pixels com atenuação acima do limite superior da janela são exibidos em branco puro, e os situados abaixo do limite inferior aparecem em preto puro.]),
   ("D", [Ao trocar a janela de partes moles pela janela óssea, os valores de atenuação registrados nos voxels da região examinada são recalculados pelo console do aparelho.]),
   ("E", [O olho humano distingue algo em torno de sessenta e quatro tons de cinza, número muito inferior à faixa de atenuações que o exame de fato registra.])))

#questao-mc("16", badge-integracao,
  [Um mesmo tecido examinado em dois aparelhos de campo magnético diferente precessa em frequências diferentes. A consequência prática direta disso é que:],
  (("A", [cada aparelho precisa emitir o pulso na frequência de precessão correspondente ao seu próprio campo, sob pena de não haver ressonância e nenhuma energia ser absorvida pelos prótons.]),
   ("B", [o tempo de relaxamento T1 de cada tecido é recalculado pelo console conforme a intensidade do campo, de modo que a ponderação depende do aparelho e não do tecido examinado.]),
   ("C", [o hidrogênio deixa de ser o núcleo utilizado em campos mais intensos, cedendo lugar ao sódio, cuja razão giromagnética é mais estável diante de variações da intensidade do campo.]),
   ("D", [a magnetização longitudinal passa a ser mensurável diretamente em campos altos, o que dispensa a aplicação do pulso e a transferência do vetor para o plano transversal.]),
   ("E", [o contraste entre gordura e água se inverte acima de determinada intensidade de campo, o que exige inverter também a interpretação das imagens ponderadas em T1.])))

#questao-ce("17", badge-integracao,
  [Julgue os itens sobre a escolha do transdutor conforme a profundidade e o detalhe desejados.],
  (("I",   [Um transdutor linear de alta frequência é adequado ao estudo da tireoide, porque o alvo é superficial e o ganho de resolução compensa a perda de penetração.]),
   ("II",  [O transdutor endocavitário opera em frequência mais alta que o abdominal porque, introduzido, fica muito próximo do órgão-alvo e pode trocar penetração por detalhe.]),
   ("III", [Frequências mais altas penetram mais profundamente nos tecidos, o que as torna preferíveis para o estudo do retroperitônio em pacientes adultos.]),
   ("IV",  [A dificuldade de examinar regiões com gás abundante se resolve escolhendo um transdutor de frequência mais baixa, capaz de atravessar a interface gasosa.])))

#questao-mc("18", badge-integracao,
  [Em que se apoia a escolha da fase portal, e não da arterial, para avaliar o parênquima hepático como um todo:],
  (("A", [na fase portal o contraste já foi eliminado pelos rins, o que reduz o ruído de fundo e permite ao console elevar o contraste exibido sem saturar a imagem obtida.]),
   ("B", [a fase portal emprega um contraste de maior concentração de iodo, capaz de realçar simultaneamente o parênquima e as vias biliares intra-hepáticas do paciente examinado.]),
   ("C", [na fase arterial o fígado ainda não recebeu contraste algum, porque a artéria hepática só se opacifica depois que a veia porta já drenou todo o sangue esplâncnico.]),
   ("D", [a fase arterial exige apneia prolongada e por isso produz artefato de movimento no fígado, o que inviabiliza a avaliação do parênquima nesse momento da aquisição.]),
   ("E", [o fígado recebe a maior parte de seu aporte pela veia porta, de modo que o realce homogêneo do parênquima só se completa quando o contraste retorna pelo território venoso.])))

#questao-mc("19", badge-integracao,
  [Por que uma lesão encefálica realça após a injeção de gadolínio, enquanto o parênquima cerebral normal ao redor praticamente não realça:],
  (("A", [porque o gadolínio é atraído pelo tecido neoplásico devido à sua carga elétrica e se concentra ativamente nas células de metabolismo aumentado, emitindo sinal próprio nessas regiões.]),
   ("B", [porque o parênquima normal contém mielina, cujo alto teor lipídico impede quimicamente a ligação do gadolínio às proteínas plasmáticas que o transportam até o interstício encefálico.]),
   ("C", [porque a barreira hematoencefálica retém o gadolínio dentro do vaso no tecido íntegro; onde ela está rompida, ele alcança o interstício, encurta o T1 local e a área devolve mais sinal.]),
   ("D", [porque o gadolínio livre atravessa a barreira apenas em regiões de fluxo sanguíneo aumentado, e o realce mede portanto perfusão, sem relação com a integridade do endotélio.]),
   ("E", [porque a lesão apresenta tempo de relaxamento T2 mais longo, e o gadolínio amplifica seletivamente o sinal transversal dos tecidos que já eram hiperintensos antes da injeção.])))

#questao-ce("20", badge-integracao,
  [Julgue os itens sobre magnificação e a silhueta cardíaca na radiografia de tórax.],
  (("I",   [Numa radiografia em incidência anteroposterior, a silhueta cardíaca aparece menor que na posteroanterior, porque o coração se aproxima do detector.]),
   ("II",  [A magnificação depende do tamanho real da estrutura, de modo que órgãos maiores são proporcionalmente mais ampliados que os menores na mesma projeção.]),
   ("III", [O coração é uma estrutura anterior no mediastino, e é essa posição que torna a incidência posteroanterior mais fiel às suas dimensões reais.]),
   ("IV",  [Uma radiografia de tórax feita no leito é em incidência anteroposterior, e o índice cardiotorácico medido nela pode superestimar o tamanho do coração.])))

#questao-mc("21", badge-integracao,
  [Ultrassom e tomografia produzem imagens seccionais, mas só a tomografia permite reconstruir livremente qualquer plano. O que sustenta essa diferença:],
  (("A", [o ultrassom registra apenas duas dimensões por corte e a tomografia registra três, porque o feixe de raios X atravessa o paciente por inteiro e a onda mecânica não atravessa.]),
   ("B", [o ultrassom entrega o plano que o transdutor está varrendo naquele instante, enquanto a tomografia armazena um volume de voxels que o computador pode reorganizar em qualquer plano.]),
   ("C", [o ultrassom trabalha com frequências muito altas, cujo comprimento de onda impede o cálculo de posições fora do plano varrido, limitação que os fótons não impõem à tomografia.]),
   ("D", [a tomografia adquire sequencialmente os planos axial, sagital e coronal em três rotações distintas do tubo, e o ultrassom dispõe de apenas uma varredura por exame realizado.]),
   ("E", [o ultrassom depende do operador para definir o plano, e o operador não consegue manter a mão estável o bastante para que o computador some os cortes num volume coerente.])))

#questao-mc("22", badge-integracao,
  [Sobre os meios de contraste usados em radiografia e tomografia, assinale a alternativa *incorreta*:],
  (("A", [O bário não é absorvido nem metabolizado pelo organismo, o que restringe seu uso à luz do tubo digestório e permite sua eliminação intacta junto com as fezes.]),
   ("B", [O contraste iodado é metabolizado e eliminado pelo rim, o que viabiliza sua administração dentro do vaso para opacificar a luz arterial e venosa do paciente.]),
   ("C", [O contraste administrado por via oral ou retal não realça parênquima algum; sua função é distender e delimitar a luz das alças intestinais que se pretende examinar.]),
   ("D", [O contraste torna visível uma estrutura porque altera a composição do tecido examinado, e não porque empresta atenuação a um compartimento onde antes não havia diferença.]),
   ("E", [A escolha entre as fases arterial, portal e excretora depende apenas do intervalo entre a injeção e a aquisição, e não do tipo de contraste que foi utilizado.])))

#questao-ce("23", badge-integracao,
  [Julgue os itens sobre o voxel e a espessura do corte na tomografia computadorizada.],
  (("I",   [O voxel registra separadamente a atenuação de cada tecido contido em seu volume, o que elimina o efeito de média em cortes espessos.]),
   ("II",  [Cortes finos reduzem o efeito de média de volume e por isso são preferidos quando se procura estrutura de poucos milímetros, como um cálculo ureteral.]),
   ("III", [A matriz computacional de quinhentos e doze por quinhentos e doze define a espessura do corte no eixo Z do volume adquirido.]),
   ("IV",  [Numa aquisição helicoidal multislice, cada fileira adicional de detectores exige uma rotação extra do tubo para cobrir o mesmo segmento do corpo.])))

#questao-mc("24", badge-integracao,
  [Por que as sequências ponderadas em T2 são as mais sensíveis para detectar lesão do sistema nervoso central:],
  (("A", [porque quase todo processo patológico aumenta o conteúdo de água tecidual, e é justamente a água que mantém sinal transversal por mais tempo, aparecendo brilhante nessa ponderação.]),
   ("B", [porque a ponderação em T2 usa intervalos curtos entre os pulsos, o que privilegia tecidos de recuperação longitudinal rápida, como a mielina lesada nas placas de desmielinização.]),
   ("C", [porque a ponderação em T2 é obtida sempre após a injeção de gadolínio, e o contraste se acumula preferencialmente nas regiões em que a barreira hematoencefálica está preservada.]),
   ("D", [porque o líquor aparece preto nessa ponderação, o que aumenta o contraste entre os ventrículos e o parênquima adjacente e evidencia qualquer desvio da linha média.]),
   ("E", [porque a ponderação em T2 anula simultaneamente o efeito dos dois tempos de relaxamento, restando apenas a densidade de prótons de hidrogênio de cada tecido examinado.])))

#questao-ce("25", badge-integracao,
  [Julgue os itens sobre o campo magnético, o pulso de radiofrequência e a segurança na ressonância magnética.],
  (("I",   [O pulso de radiofrequência não ioniza os tecidos, ao contrário do feixe de raios X, cuja energia é suficiente para arrancar elétrons dos átomos atravessados.]),
   ("II",  [Como não há radiação ionizante, a sala de ressonância dispensa triagem de objetos metálicos, bastando afastá-los do interior do anel durante a aquisição.]),
   ("III", [A magnetização longitudinal pode ser medida diretamente pela bobina receptora, sem necessidade de deslocá-la para o plano transversal.]),
   ("IV",  [O efeito indireto da radiação ionizante decorre da interação do fóton com moléculas de proteína, sendo a radiólise da água um mecanismo desprezível no tecido vivo.])))

#questao-mc("26", badge-aplicacao,
  [Homem de 28 anos chega instável após colisão automobilística, com dor abdominal difusa e queda progressiva da pressão arterial. O ultrassom feito à beira do leito mostra uma faixa anecogênica entre o fígado e o rim direito. A interpretação correta é:],
  (("A", [o achado corresponde a reforço acústico posterior do fígado sobre o rim, artefato esperado nessa janela e sem valor diagnóstico no contexto do trauma abdominal fechado.]),
   ("B", [trata-se de gordura perirrenal, que aparece anecogênica por conter poucas interfaces internas, achado anatômico normal e que não justifica alteração de conduta neste paciente.]),
   ("C", [o achado indica cálculo no recesso hepatorrenal, cuja sombra acústica se projeta sobre o polo superior do rim e simula uma coleção líquida entre os dois órgãos vizinhos.]),
   ("D", [a faixa corresponde a alça intestinal distendida por gás, que reflete o feixe incidente e produz imagem escura e homogênea entre o fígado e o rim direito do paciente.]),
   ("E", [há líquido livre no recesso hepatorrenal, e num paciente instável após trauma esse achado sustenta a indicação cirúrgica sem esperar por qualquer exame de imagem adicional.])))

#questao-mc("27", badge-aplicacao,
  [Mulher de 52 anos, obesa e diabética, faz tomografia de abdome sem contraste. O parênquima hepático está mais escuro que o baço, e as veias hepáticas aparecem mais claras que o fígado ao redor. O mecanismo que explica esse padrão é:],
  (("A", [acúmulo de ferro no hepatócito, que eleva o número atômico médio do parênquima e desloca sua atenuação para valores negativos na escala Hounsfield medida pelo cursor.]),
   ("B", [congestão venosa passiva, que aumenta o volume de sangue retido no parênquima e reduz a atenuação hepática abaixo da atenuação do sangue circulante dentro das veias.]),
   ("C", [acúmulo de triglicerídeo no hepatócito, que puxa a atenuação média do voxel em direção à faixa negativa da gordura e inverte a relação habitual entre parênquima e vasos.]),
   ("D", [realce vascular residual de um exame contrastado prévio, que mantém as veias hepáticas opacificadas e cria contraste artificial com um parênquima de atenuação inteiramente normal.]),
   ("E", [fibrose hepática avançada, cujo conteúdo de colágeno atenua menos que o hepatócito normal e reduz a leitura de atenuação do parênquima em cerca de trinta unidades.])))

#questao-ce("28", badge-aplicacao,
  [Homem de 64 anos com febre, tosse produtiva e dor pleurítica. A radiografia de tórax em incidência posteroanterior mostra opacidade no terço inferior do hemitórax direito, com apagamento da borda direita do coração e cúpula diafragmática preservada. Julgue os itens.],
  (("I",   [O apagamento da borda cardíaca indica que o processo está em contato anatômico com o coração, o que situa a consolidação no lobo médio.]),
   ("II",  [A preservação da cúpula diafragmática torna menos provável o acometimento do lobo inferior direito.]),
   ("III", [O mecanismo do achado é a substituição do ar alveolar por exsudato, o que iguala a densidade da região à do coração e apaga a interface entre eles.]),
   ("IV",  [A incidência em perfil seria dispensável, porque a radiografia frontal já permite localizar a lesão em profundidade com precisão.])))

#questao-mc("29", badge-aplicacao,
  [Idoso de 78 anos em uso de anticoagulante cai da própria altura e bate a cabeça. Está sonolento, sem déficit focal. O plantonista, num serviço sem radiologista disponível, precisa decidir o exame inicial. Considerando a física dos métodos:],
  (("A", [a ressonância é preferível porque suas sequências ponderadas em T2 são mais sensíveis a alterações do parênquima encefálico e detectam qualquer lesão intracraniana precocemente.]),
   ("B", [a tomografia sem contraste é a escolha, porque sangue coagulado atenua entre sessenta e cinco e noventa e cinco unidades contra zero do líquor, e o exame termina em segundos.]),
   ("C", [a radiografia de crânio em duas incidências basta, porque a fratura óssea é o achado que determina a conduta e o cálcio se destaca com clareza no exame simples do crânio.]),
   ("D", [o ultrassom transcraniano deve ser tentado primeiro, por ser portátil, não usar radiação e permitir avaliação dinâmica do fluxo pelas janelas ósseas temporais do paciente.]),
   ("E", [a tomografia com contraste iodado em fase arterial é preferível, porque o realce vascular delimita o hematoma e distingue sangramento ativo de coágulo já formado.])))

#questao-mc("30", badge-aplicacao,
  [Mulher de 41 anos com dor em hipocôndrio direito após refeição gordurosa, sem febre e sem icterícia. Discute-se qual método solicitar primeiro. O argumento físico que sustenta a escolha do ultrassom é:],
  (("A", [o ultrassom mede a atenuação do feixe pelas paredes da vesícula, grandeza que a tomografia não consegue quantificar por falta de escala ancorada num padrão de referência.]),
   ("B", [a tomografia é incapaz de mostrar a vesícula biliar, porque o gás das alças adjacentes produz artefato de endurecimento de feixe que apaga a região do hipocôndrio direito.]),
   ("C", [o cálculo biliar apresenta atenuação muito próxima da bile na escala Hounsfield, e por isso a tomografia sempre falha em identificá-lo, qualquer que seja a fase de contraste.]),
   ("D", [o cálculo reflete quase todo o feixe e se declara pela sombra acústica posterior, achado que o ultrassom fornece sem radiação, sem contraste e com o aparelho ao lado do paciente.]),
   ("E", [a bile é anecogênica e o ultrassom precisa de meio líquido para propagar a onda, condição que apenas a vesícula distendida oferece entre os órgãos do abdome superior.])))
