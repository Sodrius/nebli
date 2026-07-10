#import "../typst-template/nebli_v2_apostila.typ": *

// ===================== CONSOLIDAÇÃO (Q01–Q10) =====================

#questao-mc("01", badge-consolidacao,
  [Uma inserção de uma única base no meio de um gene costuma ser bem mais destrutiva do que a substituição de uma base. O que explica essa diferença?],
  (("A", [A inserção cria sempre, e de imediato, um códon de parada logo após o ponto alterado, enquanto a substituição de base nunca tem como gerar um códon de parada ao longo da sequência.]),
   ("B", [A inserção desloca o quadro de leitura dali em diante, e todos os códons seguintes passam a ser lidos fora de fase; a substituição, no pior caso, troca um único aminoácido na proteína.]),
   ("C", [A substituição altera apenas a fita-molde e a inserção altera somente o mRNA já pronto, de modo que apenas a inserção chega de fato a ser traduzida em uma proteína defeituosa.]),
   ("D", [A inserção impede fisicamente a separação das duas fitas durante a replicação, ao passo que a substituição é sempre corrigida pela própria polimerase muito antes da etapa de tradução.]),
   ("E", [A substituição muda o número total de bases do gene e a inserção preserva esse número, o que mantém intacto o quadro de leitura original a jusante do ponto alterado.])))

#questao-mc("02", badge-consolidacao,
  [Por que uma substituição entre adenina e guanina é classificada como transição, e não como transversão?],
  (("A", [Porque a troca ocorre sempre dentro de um mesmo códon e nunca atravessa o limite entre dois códons vizinhos, mantendo a leitura das trincas seguintes exatamente como estava antes.]),
   ("B", [Porque a substituição de adenina por guanina não muda o aminoácido codificado, e só recebem nome de transição as trocas de base que são silenciosas para a proteína final.]),
   ("C", [Porque adenina e guanina são ambas purinas, e transição é o nome dado à troca entre bases do mesmo tipo químico; trocas entre purina e pirimidina é que são transversões.]),
   ("D", [Porque a adenina pareia com timina e a guanina pareia com citosina, e essa diferença de parceiro de pareamento é o que define se a troca será chamada de transição.]),
   ("E", [Porque a troca entre adenina e guanina só acontece na presença de agentes químicos externos, enquanto as transversões surgem exclusivamente de erros espontâneos da replicação.])))

#questao-ce("03", badge-consolidacao,
  [Julgue os itens a seguir sobre a origem das mutações espontâneas e a fidelidade da replicação do DNA.],
  (("I", [A baixíssima taxa de mutação espontânea se deve apenas à seletividade da polimerase ao escolher a base, sem nenhuma contribuição de mecanismos de revisão posteriores à incorporação.]),
   ("II", [A forma tautomérica de uma base é estável e duradoura, e por isso a célula consegue identificá-la com folga e removê-la antes que ela cause qualquer erro de pareamento.]),
   ("III", [A deaminação espontânea da citosina gera uracila, que tende a parear como se fosse timina e assim semeia uma transição de C para T caso o reparo não chegue antes.]),
   ("IV", [A atividade de revisão (proofreading) remove a base incorreta recém-incorporada e repõe a base correta, reduzindo a taxa de erro final muito abaixo da que a polimerase teria sozinha.]),
   ("V", [Mutações espontâneas são raras, da ordem de uma a cada bilhão de bases replicadas em organismos como a bactéria e a mosca, e não dependem de agentes externos para ocorrer.])))

#questao-mc("04", badge-consolidacao,
  [Como age um análogo de base, como o 5-bromouracil, ao induzir mutação?],
  (("A", [Ele se liga de fora à dupla-hélice e a entorta fisicamente, criando uma distorção que trava a replicação naquele ponto até que um sistema de excisão remova o trecho afetado.]),
   ("B", [Ele é tão parecido com a timina que a polimerase o incorpora no lugar dela; depois, por deslocamento eletrônico, passa a reconhecer guanina e semeia uma troca de base nas cópias seguintes.]),
   ("C", [Ele quebra diretamente as pontes de hidrogênio entre as duas fitas e provoca a perda de um pedaço inteiro do DNA, gerando uma deleção que desloca o quadro de leitura adiante.]),
   ("D", [Ele transfere um grupo metil para a guanina e forma a O6-metilguanina, uma lesão altamente cancerígena que pareia erradamente com timina nas divisões celulares subsequentes.]),
   ("E", [Ele cola duas pirimidinas vizinhas da mesma fita por meio de uma ligação covalente anômala, formando um dímero que impede a leitura correta daquele trecho do gene.])))

#questao-mc("05", badge-consolidacao,
  [O que torna a radiação UVB o agente físico mais diretamente ligado às mutações induzidas pela luz solar no DNA?],
  (("A", [Seu comprimento de onda longo permite que ela penetre até a hipoderme, onde encontra as células-tronco da pele e altera diretamente o cromossomo delas por aquecimento local.]),
   ("B", [Seu comprimento de onda é absorvido pelas próprias bases nitrogenadas e induz a ligação anômala entre pirimidinas vizinhas, formando o dímero de timina que deforma a hélice.]),
   ("C", [Ela ioniza a água ao redor do DNA e produz radicais livres, que são a única via pela qual a luz solar consegue de fato modificar a sequência das bases nitrogenadas.]),
   ("D", [Ela remove grupos amino das bases, convertendo citosina em uracila de forma maciça, e essa deaminação em cadeia é o que caracteriza a assinatura mutagênica da luz do sol.]),
   ("E", [Ela atua apenas de modo indireto, gerando espécies reativas que oxidam as bases, sem nunca ser absorvida diretamente pelo DNA, ao contrário do que ocorre com a radiação UVA.])))

#questao-mc("06", badge-consolidacao,
  [Por que o reparo realizado pela MGMT (O6-metilguanina-metiltransferase) é descrito como uma reação de uso único?],
  (("A", [Porque a MGMT só funciona uma vez por ciclo celular, sendo bloqueada por fosforilação logo após a primeira reação e só voltando a atuar na divisão seguinte da célula.]),
   ("B", [Porque a MGMT precisa da energia da luz visível para agir e, no escuro, esgota seu único cofator derivado do folato, ficando inativa até que volte a ser iluminada.]),
   ("C", [Porque a MGMT corta a fita dos dois lados da lesão e, ao liberar o oligonucleotídeo, perde a região de reconhecimento, não conseguindo reconhecer um segundo alvo depois.]),
   ("D", [Porque a MGMT depende do repressor LexA para ser produzida, e como esse repressor só é clivado uma vez durante a resposta SOS, a enzima também só é fabricada uma vez.]),
   ("E", [Porque a MGMT transfere o grupo metil da guanina para um resíduo de cisteína dentro de si mesma e, ao fazê-lo, fica permanentemente inativada, sendo gasta uma proteína por lesão.])))

#questao-ce("07", badge-consolidacao,
  [Julgue os itens a seguir sobre o reparo por excisão de nucleotídeo (NER) executado pelo sistema uvrABC em bactérias.],
  (("I", [O sistema reconhece a distorção geométrica que a lesão causa na hélice, e não a identidade química específica do dano, o que lhe permite reparar lesões de tipos bem diferentes.]),
   ("II", [As duas incisões feitas pela excinuclease são simétricas, cortando o mesmo número de nucleotídeos de cada lado da lesão, de modo que o trecho removido fica centrado no dano.]),
   ("III", [Após a remoção do trecho danificado, é a DNA polimerase III replicativa que preenche a lacuna, pois a polimerase I não participa de nenhuma etapa do reparo por excisão.]),
   ("IV", [O sistema não consegue usar a fita complementar como molde, e por isso precisa recorrer a uma cópia-irmã do cromossomo para reconstruir a sequência que foi recortada.]),
   ("V", [A etapa final dispensa a DNA ligase, já que a própria polimerase de preenchimento fecha a última ligação fosfodiéster ao terminar a síntese do trecho que havia sido removido.])))

#questao-mc("08", badge-consolidacao,
  [No reparo por excisão de nucleotídeo bacteriano, as duas incisões feitas na fita danificada são assimétricas. Como elas se distribuem em relação à lesão?],
  (("A", [Os dois cortes caem exatamente sobre a lesão, um em cada base danificada, de modo que apenas o dímero em si é retirado e a fita complementar serve de molde para repô-lo.]),
   ("B", [Um corte cai a 12 nucleotídeos do lado 5′ e o outro a 12 nucleotídeos do lado 3′, retirando um trecho longo e simétrico que garante a remoção completa de qualquer distorção.]),
   ("C", [Um corte ocorre a 8 nucleotídeos do lado 5′ e o outro a 4 nucleotídeos do lado 3′ da lesão, liberando um oligonucleotídeo de cerca de 12 bases que contém o dano.]),
   ("D", [Os cortes são feitos nas duas fitas ao mesmo tempo, gerando uma quebra de fita dupla que depois é religada por recombinação com o cromossomo homólogo da célula vizinha.]),
   ("E", [Um único corte é feito do lado 3′ da lesão, e a partir dele a polimerase desloca a fita danificada à frente, sem necessidade de uma segunda incisão para concluir o reparo.])))

#questao-mc("09", badge-consolidacao,
  [O que caracteriza um plasmídeo como um replicon?],
  (("A", [O fato de ele só conseguir se replicar quando integrado ao cromossomo bacteriano, copiando-se de forma passiva no mesmo ritmo e sob o mesmo controle do DNA principal da célula.]),
   ("B", [O fato de ele possuir sua própria origem de replicação e, com isso, conseguir se copiar de forma autônoma, independentemente do ciclo de replicação do cromossomo da célula.]),
   ("C", [O fato de ele ser sempre linear e carregar nas pontas sequências repetidas que funcionam como sinais para que a maquinaria do hospedeiro inicie a duplicação do segmento.]),
   ("D", [O fato de ele codificar a sua própria transposase, enzima que recorta o plasmídeo e o reinsere em um novo ponto do genoma a cada rodada de divisão da bactéria hospedeira.]),
   ("E", [O fato de ele depender de um vírus auxiliar para ser empacotado e transferido, sendo incapaz de se duplicar sozinho sem que a maquinaria viral inicie o processo por ele.])))

#questao-mc("10", badge-consolidacao,
  [O que distingue, mecanicamente, um plasmídeo de um transposon?],
  (("A", [O plasmídeo salta de um ponto a outro dentro do mesmo genoma usando transposase, enquanto o transposon é uma molécula circular fechada que apenas se replica junto ao cromossomo.]),
   ("B", [Ambos são moléculas circulares independentes, mas o plasmídeo carrega resistência a antibióticos e o transposon carrega exclusivamente genes ligados à conjugação entre bactérias.]),
   ("C", [O plasmídeo é uma molécula circular que se move entre células por conjugação, ao passo que o transposon é um segmento que salta de um ponto a outro dentro de um mesmo genoma.]),
   ("D", [O transposon precisa de contato físico entre duas bactérias para se mover, enquanto o plasmídeo se desloca livremente pelo citoplasma e se insere onde houver sequência-alvo compatível.]),
   ("E", [O plasmídeo só existe em vírus e o transposon só existe em bactérias, de modo que os dois elementos nunca chegam a coexistir dentro de uma mesma célula hospedeira.])))

// ===================== INTEGRAÇÃO (Q11–Q25) =====================

#questao-mc("11", badge-integracao,
  [Um gene sofre uma inserção de duas bases que desloca o quadro de leitura. Por que os sistemas de reparo por excisão, tão eficientes contra dímeros de UV, não revertem esse tipo de alteração depois de fixada?],
  (("A", [Porque o frameshift gera uma distorção ainda maior na hélice do que o dímero, e o sistema de excisão é desenhado para ignorar deformações grandes e atuar apenas em lesões discretas.]),
   ("B", [Porque, uma vez replicada, a sequência deslocada deixou de ser uma lesão que distorce a hélice: virou uma sequência nova e quimicamente normal, que o reparo por excisão não tem como reconhecer como erro.]),
   ("C", [Porque a inserção converte todas as timinas vizinhas em uracila, e o sistema de excisão é incapaz de processar uracila, ficando travado antes de iniciar a primeira incisão na fita.]),
   ("D", [Porque o reparo por excisão só funciona em bactérias e o frameshift descrito ocorre exclusivamente em células humanas, onde nenhum sistema equivalente de reconhecimento foi conservado.]),
   ("E", [Porque a inserção ativa a resposta SOS, que desliga todos os sistemas de excisão para permitir a replicação de emergência, deixando o frameshift permanentemente sem correção possível.])))

#questao-mc("12", badge-integracao,
  [Um paciente com xeroderma pigmentoso desenvolve múltiplos cânceres de pele ainda na infância. Como o defeito molecular se conecta ao fenótipo clínico?],
  (("A", [O defeito está na enzima fotoliase, e sem ela os dímeros não são quebrados pela luz; o paciente só não tem câncer se evitar toda exposição à luz visível, que é o que ativaria o reparo.]),
   ("B", [O defeito está na MGMT, e sem ela a O6-metilguanina se acumula; como essa lesão vem sobretudo da dieta, o câncer aparece nos órgãos digestivos antes de surgir na pele exposta.]),
   ("C", [O defeito está na polimerase III, que perde a capacidade de revisão; sem proofreading, a taxa de erro sobe em todos os tecidos por igual, sem relação particular com a luz solar.]),
   ("D", [O defeito está na resposta SOS, que fica permanentemente ligada; o excesso de enzimas de reparo de emergência introduz mutações por conta própria, independentemente da exposição ao sol.]),
   ("E", [O defeito está nas proteínas do reparo por excisão, e sem ele os dímeros causados pelo sol não são removidos, acumulam-se, são replicados por cima e viram as mutações que geram o câncer.])))

#questao-mc("13", badge-integracao,
  [A deaminação espontânea da citosina gera uracila no DNA. Por que essa lesão específica é facilmente reconhecida e corrigida pela célula, em vez de passar despercebida?],
  (("A", [Porque a uracila é quimicamente idêntica à timina, e como a timina é a base correta do DNA, a célula simplesmente a aceita e nenhuma correção chega a ser necessária naquele ponto.]),
   ("B", [Porque a uracila distorce tanto a hélice que ela trava a replicação imediatamente, forçando uma quebra de fita dupla que só pode ser resolvida por recombinação com o cromossomo irmão.]),
   ("C", [Porque a uracila ativa a fotoliase, que a remove usando a energia da luz, do mesmo modo como essa enzima desfaz os dímeros de pirimidina causados pela radiação ultravioleta.]),
   ("D", [Porque a uracila só aparece quando a célula é exposta a agentes alquilantes, situação rara em que a maquinaria de reparo já está toda mobilizada e remove a base sem dificuldade.]),
   ("E", [Porque a uracila normalmente não existe no DNA — ela pertence ao RNA — e essa presença estranha funciona como um sinal claro de que houve dano, marcando a base para remoção e troca por citosina.])))

#questao-mc("14", badge-integracao,
  [A O6-metilguanina pareia erradamente com timina e é considerada altamente cancerígena. Como esse pareamento errado conecta a lesão a uma mutação permanente do tipo transição?],
  (("A", [Como a guanina metilada deixa de parear com qualquer base, a replicação para naquele ponto e introduz uma deleção; a perda de bases é o que caracteriza a transição associada à lesão.]),
   ("B", [Como a guanina metilada pareia com timina, uma replicação coloca timina onde haveria citosina, e o par G-C acaba substituído por A-T nas cópias seguintes — uma transição fixada se a MGMT não agir antes.]),
   ("C", [Como a metila desloca o quadro de leitura a partir daquele códon, todos os aminoácidos seguintes mudam, e esse deslocamento generalizado é o que torna a O6-metilguanina tão perigosa.]),
   ("D", [Como a guanina metilada se liga covalentemente à timina vizinha da mesma fita, forma-se um dímero que, ao ser replicado por cima, gera a transversão característica dessa lesão alquilante.]),
   ("E", [Como a metila atrai a excinuclease, o trecho é cortado e ressintetizado com erro pela polimerase I, e é esse erro de preenchimento, e não o pareamento, que fixa a transição no gene.])))

#questao-ce("15", badge-integracao,
  [Considere a relação entre a fidelidade da replicação e o reparo por excisão. Julgue os itens.],
  (("I", [A polimerase III é a única responsável pela fidelidade da replicação, e a polimerase I não tem qualquer papel nem na revisão durante a cópia nem em sistemas de reparo posteriores.]),
   ("II", [A atividade de revisão da replicação e o reparo por excisão atuam exatamente no mesmo momento e sobre o mesmo substrato, sendo apenas dois nomes diferentes para um único processo.]),
   ("III", [Como a revisão da polimerase já garante taxa de erro de um por bilhão, a existência de sistemas de reparo por excisão é redundante e não altera a frequência final de mutações.]),
   ("IV", [No reparo por excisão bacteriano, é a DNA polimerase I que sintetiza o trecho removido, a mesma enzima cuja atividade reforça a revisão durante a replicação do cromossomo.]),
   ("V", [O reparo por excisão depende de a lesão ainda distorcer a hélice; uma vez que a sequência errada já foi fixada e normalizada pela replicação, esse reparo perde a capacidade de reconhecê-la.])))

#questao-mc("16", badge-integracao,
  [O 5-bromouracil precisa de mais de uma rodada de replicação para fixar uma mutação. Por que o efeito não aparece já na primeira incorporação?],
  (("A", [Porque na primeira rodada o análogo é imediatamente removido pela excinuclease, e só escapa do reparo a partir da segunda divisão, quando os sistemas de excisão já estão saturados.]),
   ("B", [Porque o análogo precisa primeiro ser metilado pela célula para então mudar seu pareamento, e essa metilação só ocorre depois que a primeira fita-filha já foi inteiramente sintetizada.]),
   ("C", [Porque na primeira rodada ele entra no lugar da timina pareando com adenina; só na rodada seguinte, na forma que reconhece guanina, é que puxa a base errada e consolida a troca.]),
   ("D", [Porque a primeira rodada apenas insere o análogo sem replicá-lo, e qualquer mutação exige que a base esteja presente em ambas as fitas, o que só acontece após duas cópias completas.]),
   ("E", [Porque o bromo precisa ser perdido por hidrólise espontânea antes que a base mude de comportamento, e essa perda leva, em média, exatamente um ciclo celular para se completar.])))

#questao-mc("17", badge-integracao,
  [Na resposta SOS bacteriana, um dano extenso ao DNA — por exemplo, por UV — dispara a transcrição de dezenas de genes de reparo. Qual é a sequência correta de eventos no interruptor molecular?],
  (("A", [O dano ativa diretamente o repressor LexA, que então se liga com mais força à região reguladora e aumenta a transcrição dos genes SOS, acelerando a produção de enzimas de reparo.]),
   ("B", [O dano destrói a proteína RecA, e sua ausência é o sinal que libera os genes SOS, antes mantidos ativos justamente pela presença contínua de RecA sobre a região promotora.]),
   ("C", [O dano metila o repressor LexA, e a forma metilada passa a recrutar a polimerase para os genes SOS, num mecanismo idêntico ao usado pela MGMT no reparo direto da guanina.]),
   ("D", [O dano expõe fitas simples de DNA que ativam a RecA; esta estimula a autoclivagem do repressor LexA, e sem o repressor os genes SOS passam a ser transcritos em massa.]),
   ("E", [O dano corta fisicamente o operador dos genes SOS, separando-os do repressor; como o LexA não tem mais onde se ligar, a transcrição ocorre de forma desregulada e contínua.])))

#questao-mc("18", badge-integracao,
  [Uma bactéria repara dímeros de timina por fotorreativação, usando luz visível. Um paciente humano com a mesma lesão não dispõe desse recurso. O que explica a diferença e como o humano lida com o dímero?],
  (("A", [O humano possui fotoliase, mas ela só funciona no escuro; por isso o reparo do dímero ocorre durante o sono, quando a ausência de luz permite que a enzima quebre a ligação anômala.]),
   ("B", [O humano usa a MGMT para os dímeros, transferindo a ligação anômala para uma cisteína interna; é por isso que pacientes sem MGMT acumulam dímeros e desenvolvem câncer de pele precoce.]),
   ("C", [Não há diferença real: tanto a bactéria quanto o humano dependem da mesma fotoliase, e o que muda é apenas a intensidade de luz necessária para que a enzima complete a reação.]),
   ("D", [O humano não possui fotoliase funcional e, em vez de reverter o dímero com luz, depende do reparo por excisão de nucleotídeo, que recorta o trecho lesado e o reconstrói pela fita-molde.]),
   ("E", [O humano elimina o dímero ativando a resposta SOS, que cliva o repressor LexA e liga genes de reparo de emergência, num sistema herdado das bactérias e conservado em nossas células.])))

#questao-mc("19", badge-integracao,
  [Uma bactéria sensível a antibiótico torna-se resistente poucos minutos depois de entrar em contato com uma bactéria resistente, sem nunca ter sido exposta ao antibiótico. Como isso é possível?],
  (("A", [A bactéria sensível sofreu uma mutação espontânea no gene-alvo do antibiótico exatamente no momento do contato, e a coincidência temporal com a vizinha resistente é apenas casual.]),
   ("B", [O contato com a vizinha estressou a bactéria sensível e disparou sua resposta SOS, cujas enzimas de reparo introduziram, ao acaso, a mutação de resistência no gene apropriado.]),
   ("C", [A vizinha resistente liberou o antibiótico no meio, e a exposição súbita selecionou de imediato as poucas células sensíveis que já portavam resistência latente em seu cromossomo.]),
   ("D", [A vizinha resistente transferiu, por conjugação, uma cópia de um plasmídeo que carrega o gene de resistência; a bactéria receptora passou a portar o gene sem nunca ter encontrado o antibiótico.]),
   ("E", [Um bacteriófago retirou o gene de resistência do cromossomo da vizinha e, ao integrar-se como prófago na sensível, ativou nela a transcrição desse gene a partir do sítio attB.])))

#questao-mc("20", badge-integracao,
  [O transposon Tn5 carrega resistência à canamicina e pode mover-se dentro do genoma. O que o diferencia de um plasmídeo de resistência, mesmo quando ambos acabam espalhando o mesmo gene?],
  (("A", [O Tn5 salta de um ponto a outro do DNA usando sua própria transposase, enquanto o plasmídeo é uma molécula circular autônoma que se transfere inteira entre células por conjugação.]),
   ("B", [O Tn5 é uma molécula circular com origem de replicação própria, e o plasmídeo é um segmento linear que depende inteiramente da maquinaria do cromossomo para conseguir se duplicar.]),
   ("C", [O Tn5 só atua em vírus e o plasmídeo só atua em bactérias, de modo que os dois nunca chegam a cooperar na disseminação de um mesmo gene de resistência a antibióticos.]),
   ("D", [O Tn5 precisa de contato direto entre duas células para se mover, ao passo que o plasmídeo salta sozinho de um ponto a outro do mesmo genoma sem nunca deixar a célula de origem.]),
   ("E", [O Tn5 carrega resistência apenas a um antibiótico e o plasmídeo, por ser maior, carrega sempre resistência a vários ao mesmo tempo, sendo essa a única diferença real entre eles.])))

#questao-mc("21", badge-integracao,
  [Um prófago lambda permanece latente, integrado ao cromossomo de uma bactéria por muitas gerações. Um episódio de irradiação com UV faz a célula começar a produzir partículas virais. Como isso se conecta ao que vimos sobre dano ao DNA?],
  (("A", [O UV apaga o sítio attB do cromossomo, e sem esse ponto de ancoragem o prófago é fisicamente expelido do DNA, sendo essa expulsão mecânica o único gatilho possível para o ciclo lítico.]),
   ("B", [O UV insere dímeros dentro do próprio genoma viral integrado, e o vírus precisa sair para reparar essas lesões fora da célula, retornando ao cromossomo assim que o reparo termina.]),
   ("C", [O UV metila o repressor que mantém o prófago quieto, e a forma metilada passa a estimular a replicação viral, num processo idêntico ao usado pela MGMT para reparar a guanina.]),
   ("D", [O UV transfere o prófago para um plasmídeo por conjugação, e é a mudança de endereço, do cromossomo para o plasmídeo, que reativa os genes líticos antes silenciados pela integração.]),
   ("E", [O dano extenso ao DNA causado pelo UV funciona como sinal de estresse que induz o prófago: ele deixa a latência, retoma o ciclo lítico, replica-se e rompe a célula liberando progênie.])))

#questao-ce("22", badge-integracao,
  [Sobre a integração do fago lambda no sítio attB e sua relação com outros elementos móveis, julgue os itens.],
  (("I", [A integração do lambda ocorre em qualquer ponto do cromossomo bacteriano, de modo aleatório, exatamente como se dá a inserção de um transposon ao saltar para um novo sítio.]),
   ("II", [O prófago integrado fabrica partículas virais continuamente enquanto está no cromossomo, e é essa produção constante que define o estado de lisogenia da célula hospedeira.]),
   ("III", [A recombinação sítio-específica do lambda depende de longas regiões de identidade de sequência entre o fago e o cromossomo, do mesmo modo que a recombinação homóloga clássica.]),
   ("IV", [A integração do lambda ocorre em um ponto definido e reconhecível do cromossomo, o sítio attB, próximo ao gene de utilização da galactose — daí o nome recombinação sítio-específica.]),
   ("V", [Um transposon e o fago lambda compartilham a ideia de inserir DNA em um genoma, mas o transposon salta dentro do mesmo genoma, enquanto o lambda traz DNA de fora para dentro da célula.])))

#questao-mc("23", badge-integracao,
  [O reparo por excisão de nucleotídeo dá conta de lesões químicas muito diferentes entre si — dímeros de UV, bases volumosas grudadas por agentes químicos e outras. O que explica essa versatilidade?],
  (("A", [O sistema possui um sítio de reconhecimento distinto para cada tipo de lesão química, e a soma desses muitos sítios especializados é o que lhe dá a aparência de reparar tudo.]),
   ("B", [O sistema só repara dímeros de timina de fato; as demais lesões são na verdade convertidas em dímeros por enzimas auxiliares antes de serem apresentadas à excinuclease para corte.]),
   ("C", [O sistema age sobre o RNA mensageiro defeituoso em vez do DNA, e como qualquer lesão acaba gerando o mesmo tipo de mensageiro truncado, basta reconhecer esse produto comum a todas.]),
   ("D", [O sistema reconhece a distorção geométrica que a lesão impõe à hélice, e não a química específica do dano; como lesões diversas deformam a hélice de modo parecido, todas são detectadas.]),
   ("E", [O sistema depende da resposta SOS para identificar cada lesão individualmente, e é a variedade de genes ligados nessa resposta que permite cobrir um espectro tão amplo de danos.])))

#questao-mc("24", badge-integracao,
  [O xeroderma pigmentoso é transmitido de forma autossômica recessiva. Como esse padrão de herança se conecta ao mecanismo que leva o paciente ao câncer?],
  (("A", [Só com as duas cópias do gene de reparo defeituosas o NER falha por completo; sem ele, os dímeros do sol se acumulam, são replicados por cima e geram as mutações que disparam o câncer.]),
   ("B", [Como basta uma cópia defeituosa para a doença surgir, o reparo nunca chega a falhar de todo; o câncer aparece apenas porque o paciente herda, em separado, um oncogene já ativado.]),
   ("C", [O padrão recessivo indica que a doença vem do cromossomo do fago lambda integrado, e o câncer surge quando esse prófago é induzido pelo sol e passa a replicar-se nas células da pele.]),
   ("D", [A herança recessiva afeta a MGMT, e sem ela a O6-metilguanina se acumula; o sol metila a guanina diretamente, e é esse acúmulo, não o dímero, que leva o paciente ao câncer precoce.]),
   ("E", [O padrão recessivo significa que metade das enzimas de reparo funciona, o que basta para impedir mutações; o câncer, nesse caso, decorre apenas de fatores ambientais sem ligação com o gene.])))

#questao-mc("25", badge-integracao,
  [Um transposon de resistência salta de um cromossomo bacteriano para um plasmídeo conjugativo presente na mesma célula. Por que essa combinação é especialmente preocupante do ponto de vista clínico?],
  (("A", [Porque o transposon, ao entrar no plasmídeo, perde a transposase e se torna incapaz de voltar ao cromossomo, ficando preso e impedindo que a resistência se espalhe para outras células.]),
   ("B", [Porque o plasmídeo, ao receber o transposon, deixa de ser conjugativo e passa a depender de um vírus para se mover, o que torna a disseminação da resistência mais lenta e improvável.]),
   ("C", [Porque o gene de resistência, antes preso ao cromossomo, agora viaja num plasmídeo que se transfere entre bactérias por conjugação — a resistência passa a saltar de célula em célula com facilidade.]),
   ("D", [Porque a presença do transposon no plasmídeo ativa a resposta SOS de forma permanente, e as enzimas de reparo de emergência acabam gerando ainda mais genes de resistência ao acaso.]),
   ("E", [Porque o transposon converte o plasmídeo num prófago, que se integra ao cromossomo das bactérias vizinhas pelo sítio attB e só então expressa o gene de resistência que carregava.])))

// ===================== APLICAÇÃO (Q26–Q30) =====================

#questao-mc("26", badge-aplicacao,
  [Uma criança apresenta sensibilidade extrema ao sol, com sardas intensas e tumores de pele surgindo antes dos 10 anos. Os pais, saudáveis, são primos. A investigação aponta falha na remoção de dímeros de pirimidina. Qual a explicação mais consistente?],
  (("A", [Deficiência de MGMT, que impede a remoção da O6-metilguanina acumulada na pele exposta ao sol e leva ao surgimento precoce dos tumores observados na criança.]),
   ("B", [Excesso de atividade da fotoliase, que ao reverter dímeros em excesso acaba introduzindo erros na sequência e desencadeia os tumores cutâneos descritos no caso.]),
   ("C", [Resposta SOS permanentemente ligada, cujas enzimas de reparo de emergência produzem mutações ao acaso na pele, sobretudo nas regiões mais expostas à luz solar.]),
   ("D", [Mutação no fator F, que ao se integrar ao cromossomo das células da pele dispara a proliferação tumoral nas áreas que recebem maior intensidade de radiação ultravioleta.]),
   ("E", [Xeroderma pigmentoso: herança autossômica recessiva (coerente com o parentesco dos pais) com NER defeituoso, de modo que os dímeros do sol não são removidos e geram os tumores.])))

#questao-mc("27", badge-aplicacao,
  [Em uma unidade de terapia intensiva, uma cepa bacteriana resistente a vários antibióticos se espalha rapidamente entre pacientes que nunca compartilharam medicação. O laboratório encontra o mesmo plasmídeo em bactérias de espécies diferentes. Qual processo melhor explica o surto?],
  (("A", [Conjugação: o plasmídeo de resistência, com origem de replicação própria, transfere-se de uma bactéria a outra por contato direto, espalhando os genes inclusive entre espécies distintas.]),
   ("B", [Fotorreativação: a luz do ambiente hospitalar ativou fotoliases que, ao reparar o DNA, introduziram a mesma resistência simultaneamente em várias espécies de bactérias diferentes.]),
   ("C", [Mutação espontânea: cada bactéria adquiriu a resistência de forma independente, e a coincidência de aparecer o mesmo plasmídeo em espécies diferentes é apenas obra do acaso estatístico.]),
   ("D", [Reparo por excisão: ao recortar trechos do cromossomo, o sistema uvrABC liberou genes de resistência que foram captados do meio por todas as bactérias presentes na unidade.]),
   ("E", [Resposta SOS: o estresse do ambiente hospitalar disparou nas bactérias a clivagem do repressor LexA, e as enzimas resultantes criaram a resistência de forma idêntica em cada célula.])))

#questao-mc("28", badge-aplicacao,
  [Um pesquisador acompanha um fago lambda que infectou _E. coli_. Por muitas gerações nada acontece: o DNA viral é copiado junto com o cromossomo e as bactérias seguem vivas. Após irradiar a cultura com UV, surgem partículas virais e as células se rompem. Como interpretar a sequência?],
  (("A", [O fago estava no ciclo lítico desde o início, e o UV apenas acelerou uma produção viral que já vinha ocorrendo de forma lenta e silenciosa ao longo de todas aquelas gerações.]),
   ("B", [O fago estava em lisogenia, integrado como prófago e replicado passivamente; o dano do UV funcionou como sinal de estresse que o induziu ao ciclo lítico, rompendo as células.]),
   ("C", [O UV transferiu o fago de uma bactéria para outra por conjugação, e foi essa troca de hospedeiro, e não a saída da latência, que disparou a produção das novas partículas virais.]),
   ("D", [O UV reparou o genoma do fago por fotorreativação, e o vírus restaurado finalmente conseguiu se replicar, algo que a presença de lesões vinha impedindo ao longo das gerações.]),
   ("E", [O fago nunca se integrou: ele permaneceu como plasmídeo autônomo no citoplasma, e o UV apenas estimulou sua origem de replicação a copiá-lo até a célula estourar pelo excesso.])))

#questao-mc("29", badge-aplicacao,
  [Um agente quimioterápico alquilante adiciona grupos metil à guanina do DNA de células tumorais, formando O6-metilguanina e empurrando-as à morte por excesso de mutação. Observa-se que tumores com muita MGMT resistem mais ao tratamento. Como explicar essa resistência?],
  (("A", [A MGMT em excesso ativa a resposta SOS do tumor, e as enzimas de reparo de emergência reparam todas as lesões da quimioterapia, neutralizando o efeito do agente alquilante.]),
   ("B", [A MGMT remove o grupo metil da O6-metilguanina antes que a lesão se fixe como mutação; quanto mais MGMT o tumor tem, mais lesões ele apaga, sobrevivendo melhor ao alquilante.]),
   ("C", [A MGMT em alta quantidade impede a entrada do fármaco na célula tumoral, funcionando como uma bomba de efluxo que expulsa o agente alquilante antes que ele alcance o DNA.]),
   ("D", [A MGMT converte a guanina metilada em dímero de timina, lesão que o tumor repara por fotorreativação usando a luz dos exames de imagem a que o paciente é submetido.]),
   ("E", [A MGMT desloca o quadro de leitura dos genes pró-morte do tumor, e sem esses genes funcionais a célula tumoral deixa de responder ao sinal de apoptose disparado pela quimioterapia.])))

#questao-mc("30", badge-aplicacao,
  [Em um experimento, uma linhagem de _E. coli_ recebe um plasmídeo F⁻ marcado e é misturada a outra linhagem F⁺. Horas depois, quase todas as células da cultura passam a portar o fator F. Bloqueando-se fisicamente o contato entre as células com uma membrana, a transferência cessa. O que o experimento demonstra?],
  (("A", [Que o fator F se espalha por mutação espontânea simultânea em todas as células, já que a membrana apenas reduz a densidade da cultura e diminui a velocidade do acaso mutacional.]),
   ("B", [Que o fator F é transmitido por um bacteriófago que atravessa o meio livremente, e a membrana cessa a transferência por reter as partículas virais responsáveis pelo transporte do gene.]),
   ("C", [Que o fator F se difunde sozinho pelo meio líquido e entra nas células por suas origens de replicação, sendo a membrana apenas uma barreira física que torna essa difusão mais lenta.]),
   ("D", [Que o fator F se transfere por conjugação, processo que exige contato direto entre as células; impedido o contato pela membrana, a passagem do plasmídeo de uma célula a outra é interrompida.]),
   ("E", [Que o fator F precisa primeiro se integrar ao cromossomo para ser transferido, e a membrana impede a transferência por bloquear a recombinação sítio-específica no sítio attB do hospedeiro.])))
