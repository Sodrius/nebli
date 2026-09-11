#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
O genoma bacteriano é uma molécula só, circular, sem envoltório que a separe do citoplasma — e essa simplicidade permite à bactéria três coisas que a célula humana não faz: copiar o cromossomo inteiro em dezenas de minutos, reescrevê-lo por mutação a cada divisão e receber #sigla("DNA", [ácido desoxirribonucleico — polímero de nucleotídeos que carrega a informação genética]) pronto de outra célula, viva ou morta, da mesma espécie ou não.

A *PARTE I* monta o objeto: o empacotamento do cromossomo, o que separa plasmídeo de transposon e como a cópia começa numa origem única. A *PARTE II* trata o genoma como algo que muda — a mutação que nasce do erro de cópia ou da lesão química, e duas das três formas pelas quais o DNA atravessa a membrana de uma célula para outra. A *PARTE III* fecha com o que a bactéria faz com esse genoma — troca, regula e defende — e com o que o laboratório faz ao recrutar o mesmo maquinário.
]

#parte-title("PARTE I — O genoma bacteriano: forma, conteúdo e cópia", primeira: true)

#subtopico("1.1 — O nucleóide e a supertorção: um milímetro de DNA em dois micrômetros de célula")

Uma célula de _Escherichia coli_ mede cerca de 2 µm; o cromossomo que ela carrega, esticado, mede aproximadamente 1,5 mm — mais de 500 vezes o comprimento da célula. E ele precisa estar dobrado sem deixar de ser acessível à polimerase que o copia e à RNA-polimerase que o transcreve, as duas trabalhando ao mesmo tempo em pontos diferentes.

O que está sendo dobrado são duas fitas antiparalelas em que o fosfato une o carbono 3′ de um açúcar ao 5′ do seguinte na *ligação fosfodiéster*, o que dá sentido à fita. As bases pareiam por pontes de hidrogênio — duas entre adenina e timina, três entre guanina e citosina —, e essa diferença de duas para três é a razão de uma região rica em A-T ser a primeira a abrir quando a molécula é tensionada.

A solução bacteriana para o empacotamento é o #termo-nota[nucleóide][região sem membrana onde o cromossomo se organiza em alças independentes], em que o cromossomo se dobra em 50 a 100 alças independentes. As proteínas associadas ao nucleóide, sobretudo HU e H-NS, curvam o DNA; cátions divalentes e #termo-nota[poliaminas][moléculas pequenas com várias aminas protonadas, como espermidina e putrescina] neutralizam a carga do esqueleto e permitem que as voltas fiquem próximas sem se repelir. Não há histona nem nucleossomo: por massa, o nucleóide é cerca de 80% DNA, contra aproximadamente 50% na cromatina eucariótica, onde as histonas respondem pela outra metade.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-06.png",
  largura: 50%,
  legenda: [O contorno azul é o cromossomo de uma célula; o tamanho real dela é o círculo à direita.])

A segunda camada de compactação é a *supertorção*: o eixo da dupla hélice se enrola sobre si mesmo. E aqui mora a confusão que trava a leitura do resto: supertorção negativa não significa "mais enrolada" — significa *subenrolada*: faltam voltas de hélice em relação à forma relaxada. A molécula compensa torcendo-se no espaço, e a tensão armazenada é energia disponível para separar as fitas. É por isso que o DNA bacteriano é mantido negativamente supertorcido: replicação e transcrição começam abrindo a dupla hélice, e a torção negativa já paga parte dessa abertura.

Quem a introduz é a *DNA-girase*, topoisomerase do tipo II que corta as duas fitas, passa outro segmento de hélice pela abertura e religa, gastando #sigla("ATP", [adenosina trifosfato — moeda energética da célula]) a cada ciclo; é a única enzima conhecida capaz de aumentar ativamente a supertorção negativa, e por isso é essencial. A topoisomerase I faz o inverso — corta uma fita só, deixa a molécula girar e religa, relaxando o excesso sem gastar ATP.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-05.png",
  largura: 46%,
  legenda: [O grau de torção é o saldo de duas atividades opostas, não propriedade fixa da molécula.])

#clinica-box("Por que a quinolona é bactericida", [
As fluoroquinolonas não param a girase: encaixam-se na interface entre enzima e DNA no momento em que ela já cortou as duas fitas e ainda não religou, estabilizando esse *complexo de clivagem*. O resultado não é uma reação que deixa de acontecer — é uma quebra de fita dupla travada, presa à proteína. Quando a forquilha de replicação colide com esses complexos, as quebras se tornam irreparáveis e a célula morre; daí o efeito ser bactericida.

Em Gram-negativas o alvo preferencial é a girase (_gyrA_ e _gyrB_); em Gram-positivas, a topoisomerase IV (_parC_ e _parE_), que separa os cromossomos-filhos ao fim da replicação. A resistência a quinolona é, quase sempre, uma troca de aminoácido no domínio de ligação ao DNA dessas enzimas.
])

#subtopico("1.2 — Cromossomo, plasmídeo e elementos móveis: o genoma em camadas")

O genoma de uma bactéria não é uma peça única, e o termo que organiza o resto é *replicon*: molécula de DNA com origem de replicação própria, que por isso se mantém copiada a cada divisão sem depender de estar inserida em outra. O cromossomo é um replicon; o plasmídeo é outro; e há um terceiro nível de elementos que não são replicons e ainda assim se movem.

O cromossomo bacteriano é tipicamente circular, de dupla fita, com as extremidades ligadas covalentemente, e carrega os genes essenciais. Em _E. coli_ são 4,6 #sigla("Mb", [megabase — um milhão de pares de base]) e cerca de 4.300 genes, quase um gene por quilobase: praticamente não há íntron, e genes de função relacionada ficam agrupados em operons transcritos juntos. A faixa entre as espécies vai de 0,16 Mb em endossimbiontes obrigatórios, que perderam por evolução redutiva tudo o que o hospedeiro fornece pronto, a mais de 13 Mb em bactérias de solo: genoma grande é o preço da versatilidade metabólica.

O *plasmídeo* é uma molécula de DNA em geral circular, de uma a mais de cem quilobases, com origem de replicação própria e número de cópias regulado. Nada nele é essencial em condições ideais, e é isso que o torna interessante: ele carrega o genoma contingente — resistência a antimicrobianos (o plasmídeo R), fatores de virulência, enzimas de degradação de compostos incomuns. Alguns carregam ainda os genes que promovem a própria transferência, assunto da PARTE III.

O terceiro nível são os *elementos transponíveis*, sem origem de replicação e capazes de persistir apenas dentro de um replicon. O mais simples é a #sigla("IS", [sequência de inserção]), de 700 a 2.500 pares de base, contendo só o gene da #termo-nota[transposase][enzima do próprio elemento, que reconhece as repetições invertidas das pontas e o reinsere em outro sítio] e, nas pontas, as repetições invertidas que essa enzima reconhece. Quando duas IS flanqueiam genes acessórios, o conjunto passa a se mover como bloco — é o *transposon composto*. O Tn10 tem 9.300 #sigla("pb", [pares de base]) no total: IS10L e IS10R nas extremidades e 6.500 pb centrais que incluem o gene de resistência à tetraciclina.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-31.png",
  largura: 58%,
  legenda: [As IS das pontas tornam o bloco móvel; o gene de resistência no meio é carga intercambiável.])

Acima dos transposons está o *integron*, que também não se move sozinho: plataforma de captura formada por um gene de integrase, um sítio de recombinação e um promotor. A integrase insere nesse sítio *cassetes gênicos* — unidades mínimas com um gene e um sítio de recombinação próprio — em série, e todos passam a ser transcritos pelo mesmo promotor. A arquitetura explica por que a resistência raramente chega gene a gene: um integron com quatro cassetes, alojado num transposon, alojado num plasmídeo transferível, move quatro resistências num evento só.

#atencao-box("Plasmídeo é replicon; transposon não é", [
Tratar os dois como "DNA extra" apaga a diferença que governa o comportamento de cada um. O plasmídeo tem origem de replicação própria: mantém-se sozinho, é herdado pelas filhas sem estar ligado ao cromossomo e pode ser perdido se a pressão seletiva desaparecer. O transposon não tem origem própria e, solto no citoplasma, é DNA condenado — o que ele sabe fazer é mudar de endereço, do cromossomo para um plasmídeo ou de um plasmídeo para outro.

A consequência prática: quem carrega a resistência *entre* células é o plasmídeo; quem a colocou lá dentro foi, quase sempre, um transposon.
])

#subtopico("1.3 — Replicação: uma origem, duas forquilhas e três polimerases")

Em meio rico, _E. coli_ se divide a cada 20 minutos. Copiar 4,6 milhões de pares de base à velocidade medida de 50.000 pb por minuto em cada forquilha, com duas forquilhas partindo da mesma origem, leva cerca de 40 minutos. Os números não fecham, e a forma como a bactéria resolve isso diz mais sobre sua replicação do que qualquer definição.

Tudo começa numa origem única, o *oriC*, com cerca de 245 pb e duas famílias de sequência: três repetições de 13 pb ricas em A-T e quatro caixas de 9 pb. A proteína DnaA carregada com ATP ocupa as caixas de 9 pb e oligomeriza; a torção que o complexo impõe funde as repetições de 13 pb — as primeiras a ceder, porque cada par A-T é sustentado por apenas duas pontes de hidrogênio.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-21.png",
  largura: 56%,
  legenda: [A origem é sequência: as caixas de 9 pb são o endereço da DnaA, as de 13 pb o ponto projetado para romper primeiro.])

A partir daí a cadeia é rígida. A helicase DnaB, carregada sobre a fita simples pela DnaC, avança separando as fitas; proteínas de ligação a fita simples impedem o reanelamento; a girase trabalha à frente removendo a torção positiva acumulada. Como nenhuma DNA-polimerase inicia cadeia do zero — todas apenas estendem uma extremidade 3′-OH existente —, a primase DnaG sintetiza um curto iniciador de #sigla("RNA", [ácido ribonucleico]). Na fita orientada 3′→5′ em relação à forquilha basta um iniciador e a síntese é contínua; na outra, a polimerase recomeça a cada trecho desenrolado, e o produto são os *fragmentos de Okazaki*, de 1.000 a 2.000 nucleotídeos em bactérias contra 100 a 200 em eucariotos.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-22.png",
  largura: 66%,
  legenda: [A fita tardia é descontínua porque a polimerase só sintetiza 5′→3′ enquanto a forquilha abre nos dois sentidos.])

#block(breakable: false)[
#align(center)[
#table(
  columns: (auto, 1fr, 1fr),
  inset: 7pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    [*Enzima*], [*Atividades*], [*Função*]
  ),
  [DNA-polimerase III],
  [Síntese 5′→3′; exonuclease 3′→5′ de revisão; grampo deslizante β],
  [Replicase principal, de alta processividade],
  [DNA-polimerase I],
  [Síntese 5′→3′; exonuclease 3′→5′; exonuclease 5′→3′, exclusiva dela],
  [Troca o iniciador de RNA por DNA; preenche trechos curtos no reparo],
  [DNA-polimerase II],
  [Síntese 5′→3′; exonuclease 3′→5′],
  [Reparo alternativo; reinicia a forquilha travada em molde lesado],
)
]
]

A exonuclease 5′→3′ da polimerase I é o que fecha a fita tardia: remove o RNA iniciador nucleotídeo a nucleotídeo e, no mesmo movimento, preenche com DNA, até restar só uma interrupção que a DNA-ligase sela. A replicação avança nos dois sentidos, a molécula assume a forma de um theta, e as forquilhas param na região oposta ao oriC, onde sítios _ter_ ligam a proteína Tus e funcionam como armadilhas de sentido único.

#mini-resumo[DnaA abre o oriC → helicase separa as fitas → primase põe iniciador de RNA → Pol III sintetiza → Pol I troca o RNA por DNA → ligase fecha. Cada enzima existe porque a anterior deixou um problema específico.]

Um detalhe químico organiza o controle. A metiltransferase Dam metila a adenina de toda sequência GATC; logo após a passagem da forquilha a fita antiga está metilada e a nova ainda não — o DNA fica *hemimetilado* —, e essa assimetria tem dois usos: a proteína SeqA se liga ao oriC hemimetilado e o sequestra, impedindo reinício imediato, e o sistema de reparo de malpareamento usa a mesma marca para saber qual fita é a nova e, portanto, qual base de um par incorreto trocar. O segundo uso volta no início da PARTE II.

Resolvida a aritmética inicial: em crescimento rápido a bactéria reinicia a replicação numa origem que ainda está sendo replicada, e a filha nasce com o cromossomo parcialmente copiado. Dividir a cada 20 minutos não exige replicar em 20 minutos; exige que uma rodada *termine* a cada 20 minutos.

#parte-title("PARTE II — Como o genoma muda")

#subtopico("2.1 — Mutação: o que muda na sequência e o que aparece no fenótipo")

Mutação é qualquer alteração herdável na sequência de bases, e em bactéria ela pesa pela frequência com que surge somada ao tamanho da população em que surge. A DNA-polimerase III incorpora a base errada cerca de uma vez a cada 100 mil nucleotídeos. A revisão exonucleolítica 3′→5′ da própria enzima remove a maioria desses erros no ato e derruba a taxa para cerca de um em 10 milhões. O reparo de malpareamento pós-replicativo — MutS reconhece a distorção, MutL recruta, MutH corta a fita nova identificada pela hemimetilação GATC do subtópico anterior — leva o resultado a algo entre 10#super[-9] e 10#super[-10] por par de base por geração. Parece desprezível, e não é: uma cultura com 10#super[9] bactérias, cada uma com 4,6 milhões de pares de base, contém rotineiramente milhares de células com alguma mutação pontual — a população já chega mutada.

Na sequência, as alterações são de dois tipos: a *substituição* troca uma base por outra — transição quando purina vira purina ou pirimidina vira pirimidina, transversão quando a troca cruza as duas classes — e a *inserção ou deleção* acrescenta ou remove nucleotídeos. No produto, o efeito depende de como o ribossomo lê o resultado. A mutação *silenciosa* não muda o aminoácido, quase sempre porque atinge a terceira base do códon, onde o código é degenerado. A *missense* troca um aminoácido: numa alça de superfície pode não alterar nada, no sítio ativo abole a função. A *nonsense* cria códon de parada prematuro e trunca a proteína. E a inserção ou deleção que não seja múltiplo de três desloca a fase de leitura a partir dali — a *mutação de mudança de fase* —, de modo que todos os códons seguintes são outros.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-25.png",
  largura: 68%,
  legenda: [Só a mudança de fase corrompe toda a sequência a jusante; as demais ficam contidas no códon atingido.])

O que o laboratório enxerga é o fenótipo: auxotrofia, quando a enzima inativada é de via biossintética e a bactéria passa a exigir o produto pronto no meio; morfologia de colônia alterada; mutantes termossensíveis, cuja proteína dobra a 30 °C e não a 42 °C; e a resistência a antimicrobianos, que vale seguir do nucleotídeo ao antibiograma. Na resistência às quinolonas, a mutação mais comum troca a serina da posição 83 da subunidade A da girase por leucina: essa serina participa do contato que a fluoroquinolona usa para estabilizar o complexo de clivagem de 1.1, e sem ela a droga perde afinidade enquanto a enzima segue funcional. O mesmo desenho aparece em outros alvos — mutação em _rpoB_ altera a subunidade β da RNA-polimerase e afasta a rifampicina; mutação em _ftsI_ altera a proteína ligadora de penicilina 3 e reduz a afinidade do β-lactâmico.

#atencao-box("O antibiótico seleciona a mutação; não a encomenda", [
A leitura intuitiva é que a bactéria, exposta ao antimicrobiano, "desenvolve" a alteração que a salva. Ela inverte causa e consequência e destrói o raciocínio epidemiológico inteiro.

A mutação é anterior ao antibiótico e independente dele: surge ao acaso durante a replicação, numa célula entre milhões, e o antimicrobiano apenas elimina as demais e deixa visível o clone que já a possuía. Luria e Delbrück demonstraram isso pela *variância* entre culturas independentes — se a resistência fosse induzida pela exposição, todas dariam números parecidos de sobreviventes; como é anterior, o número depende de quão cedo a mutação surgiu em cada tubo. O antibiótico faz, sim, algo relacionado: ao induzir a resposta ao dano no DNA do próximo subtópico, eleva a taxa *geral* de mutação — não escreve a mutação certa, afrouxa a fidelidade de todas.
])

#subtopico("2.2 — Mutagênicos e reparo: o que lesa o DNA e o que conserta")

As taxas do subtópico anterior pressupõem DNA quimicamente intacto. Agentes mutagênicos quebram essa premissa: alteram a base ou o esqueleto, e a mutação nasce menos da lesão do que do modo como a célula lida com ela.

Entre os agentes físicos, a radiação ultravioleta é o exemplo canônico. Fótons de #sigla("UV", [ultravioleta]) em torno de 254 nm são absorvidos por pirimidinas adjacentes da mesma fita e induzem ligação covalente entre elas, formando o #termo-nota[dímero de ciclobutano-pirimidina][duas pirimidinas vizinhas da mesma fita unidas por um anel de quatro carbonos, tipicamente duas timinas], que dobra a hélice e trava a polimerase; o reparo por excisão de nucleotídeo resolve, com o complexo UvrABC cortando o esqueleto dos dois lados da lesão para que a polimerase I preencha o vão e a ligase feche. A radiação ionizante age por outra física — ioniza a água ao redor e gera radical hidroxila, que produz quebras de fita simples e dupla. A quebra dupla é a perigosa, porque não sobra molde na mesma molécula: resolve-se por recombinação homóloga com a cópia irmã do cromossomo, conduzida pela RecA. O calor acelera a #termo-nota[depurinação][perda espontânea de adenina ou guanina por hidrólise da ligação N-glicosídica], que deixa um sítio sem base para a AP-endonuclease remendar.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-26.png",
  largura: 58%,
  legenda: [A radiação ionizante corta o esqueleto em pontos aleatórios; o ultravioleta solda duas timinas vizinhas e entorta a hélice.])

Entre os agentes químicos, cada classe produz um erro característico. Os *alquilantes*, como o metilmetanossulfonato, acrescentam grupo metil à guanina; a O#super[6]-metilguanina resultante pareia com timina, e a replicação seguinte fixa a transição de G:C para A:T. As *moléculas planares*, como o brometo de etídio e as acridinas, não alteram base alguma: intercalam-se entre pares empilhados e aumentam a distância entre eles, de modo que a polimerase escorrega no ponto distorcido e insere ou omite um nucleotídeo, produzindo mudança de fase de leitura. A água oxigenada representa o dano oxidativo — gera 8-oxoguanina, que pareia com adenina e produz transversão de G:C para T:A, corrigida por excisão de base. Já o dodecilsulfato de sódio, citado na mesma lista de agentes de bancada, é detergente que solubiliza membrana e desnatura proteína: pertence ao protocolo de lise para extração de DNA, não à mutagênese.

Quando a lesão é extensa, a célula muda de estratégia. Trechos de fita simples se acumulam, a RecA se polimeriza sobre eles e adquire atividade de coprotease, que estimula a autoclivagem do repressor LexA; cai o repressor, e cerca de 40 genes são desreprimidos ao mesmo tempo — é a resposta #sigla("SOS", [resposta coordenada ao dano no DNA em bactérias, controlada pelo repressor LexA]). Entram enzimas de reparo e, com elas, as polimerases de translesão IV e V, capazes de sintetizar por cima de um molde ilegível justamente porque não exigem pareamento correto: a célula troca fidelidade por continuidade.

Esse é o elo com o subtópico anterior. Quinolonas produzem quebras de fita dupla, e β-lactâmicos, estresse de parede que também converge no SOS: o antimicrobiano que deveria conter a população eleva, na fração que sobrevive, a taxa de mutação e a expressão dos genes que promovem transferência de DNA entre células — o assunto a partir daqui.

#subtopico("2.3 — Transformação e transdução: DNA que entra sem divisão celular")

Bactérias não fazem meiose nem fecundação, e mesmo assim um gene de resistência detectado numa _Klebsiella_ pode reaparecer, semanas depois, numa _E. coli_ do mesmo paciente. Isso não é descendência: é *transferência horizontal*, a passagem de DNA entre células sem relação de mãe e filha, por três mecanismos — transformação, transdução e conjugação. Os dois primeiros ficam aqui.

Na *transformação*, a célula capta DNA livre do meio, liberado por outras que se lisaram, e para isso precisa estar em #termo-nota[competência][estado fisiológico transitório em que a bactéria expressa a maquinaria de captação de DNA externo]. Em _Streptococcus pneumoniae_ o controle é por densidade populacional: um peptídeo estimulador de competência, secretado pela própria população, atinge concentração limiar e liga o programa — a bactéria só se abre ao DNA quando há muitas iguais a ela por perto, e portanto DNA aproveitável no meio. A maquinaria é um pseudopilus que puxa a dupla fita até um canal de membrana; uma das fitas é degradada por nuclease e só a fita simples entra, revestida por proteínas protetoras, até ser integrada ao cromossomo por recombinação homóloga conduzida pela RecA. Como essa integração exige semelhança de sequência, a transformação favorece DNA de espécies próximas — foi o fenômeno que Griffith descreveu em 1928 e que Avery identificou como DNA em 1944.

#figura-lateral("/figuras/micro-06-genetica-bacteriana/slide-29.png",
  lado: "right",
  largura-figura: 36%,
  texto: [A consequência clínica é independente de plasmídeo: o pneumococo capta DNA de estreptococos comensais da orofaringe e substitui trechos dos próprios genes de proteínas ligadoras de penicilina por versões estrangeiras, formando genes em mosaico cuja proteína tem menos afinidade pelo β-lactâmico. É resistência adquirida por recombinação, num patógeno que não produz β-lactamase.],
  legenda: [Transformação: o DNA livre entra como fita simples.])

Na *transdução*, o vetor é um vírus, e as duas formas nascem de erros distintos de máquinas distintas. A *generalizada* é falha de empacotamento: durante o ciclo lítico o cromossomo bacteriano é fragmentado, e a maquinaria que enche o capsídeo ocasionalmente carrega um fragmento bacteriano do tamanho certo em vez do DNA viral. A partícula é infecciosa e não replicativa — injeta DNA bacteriano na próxima célula, que pode integrá-lo por recombinação —, e qualquer gene pode viajar. A *especializada* é falha de excisão e pressupõe lisogenia: o fago está integrado ao cromossomo como prófago, num sítio específico, e ao se excisar realiza às vezes um corte deslocado, levando o DNA bacteriano *vizinho* no lugar de parte do próprio genoma — só os genes adjacentes àquele sítio viajam, no fago lambda os do metabolismo da galactose e da biotina. Um mecanismo sorteia; o outro repete sempre o mesmo conteúdo.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-33.png",
  largura: 62%,
  legenda: [Fragmentos do cromossomo da doadora, empacotados no capsídeo e fixados por recombinação na receptora.])

#clinica-box("Quando o gene da toxina vem no genoma do fago", [
O prófago não precisa errar para alterar o hospedeiro: muitos fagos temperados carregam, no próprio genoma, genes expressos enquanto o vírus permanece integrado — é a #termo-nota[conversão lisogênica][aquisição de novo fenótipo pela bactéria em razão da expressão de genes trazidos pelo prófago integrado]. A toxina diftérica é codificada pelo fago beta de _Corynebacterium diphtheriae_, e cepas não lisogenizadas colonizam a faringe sem produzir a toxina que causa a doença sistêmica. A toxina Shiga de _E. coli_ O157:H7 vem de prófago semelhante, com consequência prática direta: o antimicrobiano que induz a resposta SOS induz também o ciclo lítico do prófago e aumenta a produção de toxina — razão pela qual antibioticoterapia nessa infecção se associa a maior risco de síndrome hemolítico-urêmica.
])

#parte-title("PARTE III — Trocar, regular, defender e manipular")

#subtopico("3.1 — Conjugação: o contato que espalha resistência")

Transformação e transdução transportam DNA sem que as células se toquem. A *conjugação* exige contato físico, move blocos grandes de genes com eficiência muito maior, e é a principal via de disseminação de resistência a antimicrobianos.

O elemento central é o fator F, plasmídeo de cerca de 100 kb cuja região _tra_, com aproximadamente 33 genes, constrói duas estruturas: o *pilus sexual*, apêndice proteico extracelular, e um #sigla("T4SS", [sistema de secreção do tipo IV — canal proteico que atravessa as membranas e conduz o DNA de uma célula à outra]). A célula que o possui é F⁺, doadora; a que não o possui é F⁻, receptora.

A sequência é rígida. O pilus da doadora toca a receptora e se retrai, aproximando as células até que o T4SS forme um canal contínuo. No plasmídeo, a relaxase corta uma das fitas num ponto definido dentro da *origem de transferência*, permanece ligada à extremidade cortada e a conduz pelo canal. Enquanto essa fita sai, a fita circular que ficou na doadora serve de molde e é copiada por #termo-nota[replicação por círculo rolante][modo de replicação em que a fita circular intacta gira servindo de molde contínuo]; na receptora, a fita recebida é convertida em dupla fita e recirculariza. Ao final, cada célula tem um plasmídeo completo — a doadora não perdeu nada, e a receptora passou a ser F⁺.

Esse último detalhe produz a cinética que interessa clinicamente: cada célula convertida torna-se ela própria doadora, e o número de doadoras cresce geometricamente enquanto houver receptoras. Num ambiente denso como o lúmen intestinal ou um biofilme de cateter, um plasmídeo atravessa a população em horas, sem depender de nenhuma célula se dividir.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-34.png",
  largura: 62%,
  legenda: [Acima, a receptora F⁻ terminando F⁺. Abaixo, o fator F integrado produzindo a célula Hfr, que arrasta genes cromossômicos.])

O fator F pode também se integrar ao cromossomo, por recombinação homóloga entre sequências de inserção presentes nos dois. A célula passa a ser *Hfr*, de alta frequência de recombinação: a transferência ainda começa na origem do fator F, mas a fita que sai arrasta o cromossomo atrás de si, em ordem linear e sempre do mesmo ponto. Como o contato se rompe em poucos minutos e a segunda metade do fator F é a última a passar, a receptora recebe genes cromossômicos e permanece F⁻ — regularidade que produziu o primeiro mapa genético de _E. coli_, em minutos de conjugação interrompida.

#clinica-box("O plasmídeo de carbapenemase num surto de terapia intensiva", [
O plasmídeo R tem duas regiões funcionalmente distintas: a de transferência, com os genes _tra_ que constroem o pilus e o canal, e a determinante de resistência, em geral um mosaico de transposons e integrons acumulados ao longo do tempo. Quem conjuga transfere o bloco inteiro — e é por isso que a resistência clínica raramente aparece a um antimicrobiano isolado.

As carbapenemases dos tipos KPC e NDM são β-lactamases codificadas em transposons alojados em plasmídeos conjugativos de amplo espectro de hospedeiro: numa terapia intensiva, a _Klebsiella pneumoniae_ de um paciente e a _E. coli_ de outro podem compartilhar o mesmo plasmídeo sem compartilhar ancestral recente. Isolamento de contato e higiene de mãos atacam a transmissão de célula inteira, mas não impedem que o plasmídeo já disseminado reapareça em outra espécie — por isso a vigilância de surto sequencia o plasmídeo, em vez de apenas tipificar a bactéria.
])

#subtopico("3.2 — Operon lac: o genoma decide o que transcrever")

Sintetizar uma enzima cujo substrato não está presente custa aminoácido, ATP e tempo de ribossomo. A bactéria evita esse custo regulando a transcrição no ponto de partida, e o arranjo que torna isso econômico é o *operon*: genes contíguos transcritos a partir de um único promotor, num mRNA policistrônico lido em série.

No operon lac de _E. coli_ os genes estruturais são _lacZ_, que codifica a β-galactosidase (hidrolisa lactose em glicose e galactose), _lacY_, a permease que importa lactose, e _lacA_, uma transacetilase. Antes deles ficam o promotor e, entre ele e o primeiro gene, o *operador*. Separado e transcrito continuamente, o gene _lacI_ produz o repressor.

A primeira camada de controle é negativa. O repressor LacI, um tetrâmero, ocupa o operador e impede o avanço da RNA-polimerase — a transcrição fica em nível basal muito baixo, mas não nulo, e essa fração residual é essencial ao mecanismo. Quando entra lactose, a pouca β-galactosidase existente converte parte dela em *alolactose*, isômero que se liga ao repressor e reduz sua afinidade pelo operador; o repressor solta, a polimerase avança. O indutor verdadeiro não é a lactose, e sim o isômero produzido a partir dela — por isso o análogo sintético IPTG, que não é hidrolisado, é o indutor de bancada: induz sem ser consumido.

A segunda camada é positiva e responde a outra pergunta. O promotor lac é intrinsecamente fraco: mesmo com o operador livre, a RNA-polimerase se liga mal. Quem resolve isso é o ativador #sigla("CAP", [proteína ativadora de catabólito — ativador transcricional dependente de cAMP]), que só se liga ao DNA associado a cAMP e, ligado, dobra a hélice e recruta a polimerase. O nível de cAMP é inverso à disponibilidade de glicose — enquanto a glicose está sendo importada, o sistema de transporte mantém a adenilato-ciclase pouco ativa e o cAMP baixo; falta glicose, cAMP sobe, CAP liga, transcrição dispara.

#align(center)[
#table(
  columns: (auto, auto, auto, auto, 1fr),
  inset: 7pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    [*Glicose*], [*Lactose*], [*cAMP*], [*Operador*], [*Transcrição*]
  ),
  [presente], [ausente], [baixo], [ocupado], [desligada],
  [presente], [presente], [baixo], [livre], [basal: operador abriu, promotor fraco sem reforço],
  [ausente], [ausente], [alto], [ocupado], [desligada],
  [ausente], [presente], [alto], [livre], [máxima: repressor fora e CAP-cAMP recrutando],
)
]

As duas camadas respondem a perguntas diferentes, e nenhuma é dispensável: o repressor pergunta se há substrato e evita produzir enzima inútil; o complexo CAP-cAMP pergunta se vale a pena usar esse substrato e evita gastar com a fonte de carbono pior enquanto a melhor está disponível. A consequência observável é o crescimento diáuxico — numa cultura com glicose e lactose, a bactéria consome primeiro a glicose, para de crescer enquanto sintetiza as enzimas do operon, e só então retoma o crescimento à custa da lactose.

#subtopico("3.3 — Restrição-modificação e CRISPR-Cas: o sistema imune da bactéria")

Bactérias vivem sob predação viral constante — na maioria dos ambientes há mais partículas de bacteriófago do que células bacterianas. A pressão selecionou defesas em camadas: alteração do receptor de superfície, que impede a adsorção; bloqueio da injeção do DNA; infecção abortiva, em que a célula infectada se mata antes de completar o ciclo e poupa as vizinhas idênticas; e dois sistemas que reconhecem o DNA invasor pela sequência.

O primeiro é o sistema de *restrição-modificação*. A endonuclease de restrição corta uma sequência curta e palindrômica — palíndromo aqui significa que a fita lida no sentido 5′→3′ tem a mesma sequência que a complementar lida também 5′→3′, como em GAATTC. Sozinha, essa enzima destruiria o próprio cromossomo, que contém as mesmas sequências; o que impede isso é a segunda metade do sistema, uma metiltransferase que metila exatamente a mesma sequência no DNA da célula. A marca metílica é a credencial: DNA próprio chega metilado e é ignorado, DNA de fago chega sem a marca e é cortado. A nomenclatura registra a origem — EcoRI é a primeira enzima isolada da cepa RY13 de _Escherichia coli_.

O segundo é o sistema #sigla("CRISPR", [repetições palindrômicas curtas agrupadas e regularmente interespaçadas])-Cas, que não reconhece marca química genérica, e sim sequência específica guardada da vez anterior. O arranjo no cromossomo alterna repetições curtas idênticas com *espaçadores*, cada um deles um pedaço de cerca de 30 pb do genoma de um invasor já enfrentado. Na *adaptação*, o complexo Cas1-Cas2 recorta do DNA invasor um #termo-nota[protospacer][o trecho do invasor que será copiado para o arranjo e passará a ser chamado espaçador] e o insere na extremidade do arranjo, entre duas repetições — memória escrita no cromossomo e herdada pelas filhas. Na *biogênese*, o arranjo é transcrito num precursor longo e processado em #sigla("crRNA", [RNA CRISPR — a molécula-guia madura, com um espaçador e parte da repetição adjacente]) individuais; a repetição transcrita pareia consigo mesma e forma uma haste-alça, estrutura secundária que a maquinaria de processamento reconhece. Na *interferência*, o crRNA carrega a nuclease Cas9, que varre o DNA procurando um #sigla("PAM", [motivo adjacente ao protospacer — sequência curta exigida ao lado do alvo para que a nuclease corte]), abre localmente a hélice onde o encontra e testa o pareamento com o espaçador; pareamento suficiente, corte de dupla fita alguns pares antes do PAM.

A exigência do PAM resolve o mesmo problema que a metilação resolve no sistema de restrição: distinguir o próprio do estranho. O arranjo CRISPR do cromossomo contém as mesmas sequências dos espaçadores, mas *sem* o PAM ao lado — e é por isso que a Cas9 não digere o genoma que a produziu. O aproveitamento biotecnológico decorre de um único passo: trocar o crRNA natural por um RNA-guia sintético dirige a Cas9 a qualquer sequência com PAM adjacente, e a quebra resultante é reparada por junção imprecisa das extremidades, que inativa o gene, ou por recombinação com um molde fornecido, que instala a sequência desejada.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-44.png",
  largura: 62%,
  legenda: [O espaçador novo entra no arranjo, o arranjo vira guias individuais, e o guia dirige o corte na reinfecção.])

#subtopico("3.4 — DNA recombinante e sequenciamento: ler e reescrever o genoma")

A tecnologia do DNA recombinante é microbiologia recrutada: a tesoura é enzima de restrição bacteriana, a cola é ligase de fago, o veículo é plasmídeo de _E. coli_ e a polimerase termoestável vem de bactéria termófila — cada ferramenta já apareceu antes como mecanismo natural.

O corte define o encaixe. Quando a enzima cliva as duas fitas exatamente no eixo de simetria do palíndromo, os fragmentos ficam com *extremidades abruptas*; quando cliva de forma escalonada em torno do eixo, sobram *extremidades coesivas* — saliências de fita simples de poucos nucleotídeos, complementares entre si. Dois DNAs cortados pela mesma enzima, um plasmídeo bacteriano e um fragmento humano por exemplo, geram saliências idênticas que pareiam por pontes de hidrogênio, e a ligase apenas sela as ligações fosfodiéster que faltam: a compatibilidade não é de espécie, é de extremidade.

#figura-lateral("/figuras/micro-06-genetica-bacteriana/slide-37.png",
  lado: "right",
  largura-figura: 38%,
  texto: [O vetor mostra o princípio numa molécula só. O pUC18 tem 2.686 pb, origem de replicação de alto número de cópias, o gene _bla_ de β-lactamase e um sítio de clonagem múltipla encaixado dentro de um fragmento do gene _lacZ_. O inserto interrompe o _lacZ_: a colônia deixa de hidrolisar o substrato cromogênico e cresce branca, não azul. A seleção é dupla — a ampicilina elimina quem não recebeu plasmídeo, a cor separa plasmídeo vazio de plasmídeo com inserto.],
  legenda: [Corte no eixo de simetria gera extremidade abrupta; corte escalonado, coesiva.])

Transformar a bactéria com o plasmídeo construído usa o mecanismo de 2.3, forçado por cloreto de cálcio com choque térmico ou por eletroporação. O passo seguinte depende de uma propriedade física da hélice: aquecer rompe as pontes de hidrogênio entre as bases sem tocar no esqueleto covalente, e as fitas se separam — é a *desnaturação*. A temperatura em que metade das moléculas está separada depende do comprimento, da força iônica e, sobretudo, do conteúdo de guanina e citosina, porque são três pontes por par G≡C contra duas por A=T. Resfriar devolve o pareamento onde houver complementaridade — a *renaturação* —, e toda hibridação e toda reação em cadeia da polimerase vivem desse par de transições.

A #sigla("PCR", [reação em cadeia da polimerase — amplificação de um trecho definido de DNA por ciclos térmicos repetidos]) organiza esse ciclo em três temperaturas: 94 a 95 °C desnatura; 50 a 60 °C permite que dois iniciadores sintéticos aneiem nas bordas do trecho de interesse; 72 °C é a temperatura de trabalho da polimerase de _Thermus aquaticus_, que sobrevive às passagens repetidas por 95 °C. Cada ciclo duplica as cópias do trecho delimitado pelos iniciadores, e trinta ciclos amplificam da ordem de um bilhão de vezes.

Amplificar, sequenciar e alinhar contra bancos de dados responde a duas perguntas clínicas. A primeira é de identidade: genes espécie-específicos, como as regiões variáveis do gene do RNA ribossômico 16S, confirmam qual bactéria está ali mesmo com cultura negativa, crescimento lento ou antimicrobiano já iniciado. A segunda é de resistência: a mesma leitura detecta genes adquiridos — β-lactamases dos tipos TEM, ROB e KPC — e mutações pontuais nos alvos já discutidos, como as de _gyrA_ e _parC_ para quinolonas e as de _ftsI_ para β-lactâmicos, permitindo prever o fenótipo, orientar a terapia e rastrear um clone ou um plasmídeo.

#confusao-prevista(
  titulo: "Gene de resistência detectado não é resistência medida",
  aluno_acha: [que encontrar o gene da β-lactamase no sequenciamento equivale a um antibiograma resistente],
  mecanismo: [o achado genotípico *prevê*, não mede. O gene pode estar presente e pouco expresso, ou neutralizado por inibidor associado ao β-lactâmico, e mutações ainda desconhecidas não são detectadas por comparação com banco de dados. A medida de fenótipo, que integra expressão, permeabilidade e bombas de efluxo, continua vindo do teste de sensibilidade.],
)

#conclusao-box[
O princípio que atravessa o resumo: *o genoma bacteriano é um replicon aberto*. É copiado depressa, reescrito a cada rodada por erro e por lesão, e permeável a DNA que vem de fora — de outra célula, de um vírus ou do meio.

O mecanismo nuclear é a soma de duas fontes de variação com destinos diferentes. A *mutação* gera diversidade lentamente e verticalmente, e depende de a população ser grande o bastante para que o raro seja frequente. A *transferência horizontal* importa função pronta e testada num salto só, e converge sempre no mesmo passo final — a recombinação conduzida pela RecA, que fixa no cromossomo o DNA entrado por transformação, transdução ou conjugação.

Na clínica isso se lê em duas colunas. A resistência por mutação de alvo — a serina 83 da girase trocada por leucina, a subunidade β da RNA-polimerase alterada — é de linhagem e se propaga por descendência. A resistência adquirida — a β-lactamase codificada em cassete dentro de integron dentro de plasmídeo conjugativo — não respeita parentesco e atravessa gêneros em horas. Entre as duas colunas há uma ponte incômoda: o próprio antimicrobiano, ao induzir a resposta SOS, eleva a taxa de mutação e favorece a transferência.

Fica aberta a porta da patogenicidade: os mesmos mecanismos que movem resistência movem virulência — a toxina que chega no genoma de um prófago, a ilha de patogenicidade que salta como elemento móvel, a adesina codificada em plasmídeo. Estudar como a bactéria adoece o hospedeiro é, em boa parte, continuar a estudar o que ela adquiriu e de quem.
]
