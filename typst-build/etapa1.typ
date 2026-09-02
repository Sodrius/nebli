#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Uma população bacteriana precisa resolver, ao mesmo tempo, duas exigências que se contradizem. Precisa se perpetuar idêntica a si mesma, porque é a fidelidade da cópia que faz uma _Escherichia coli_ continuar sendo _E. coli_ geração após geração. E precisa variar, porque uma população que só produz cópias exatas de si mesma morre inteira no primeiro meio hostil que encontrar — um antibiótico, uma temperatura nova, uma fonte de carbono diferente.

A aula inteira sai dessa tensão, e a resposta dela é curta: *só existem dois modos de uma bactéria ficar diferente do que era — mutação ou recombinação*. Mutação é alteração da sequência de bases do próprio material genético. Recombinação é a chegada de material genético que veio de fora. Não há terceira via, e essa dicotomia organiza as três PARTES a seguir.

A PARTE I estabelece o objeto: onde o material genético bacteriano fica, que forma tem, quanto mede e por que existe um segundo tipo de molécula de DNA, o plasmídeo, que carrega funções dispensáveis para a identidade da bactéria e decisivas para o que ela consegue fazer. A PARTE II percorre a rota da mutação — como o erro nasce, quais mecanismos o consertam sem deixar marca, e o momento exato em que consertar deixa de ser possível e a célula escolhe sobreviver mutada. A PARTE III percorre a rota da recombinação: as três maneiras pelas quais um gene atravessa a parede de uma bactéria e entra em outra, e os elementos que, uma vez lá dentro, o movem de molécula em molécula. No fim das duas rotas está o mesmo desfecho clínico: uma bactéria que ontem morria com o antibiótico e hoje não morre mais.
]

#parte-title("PARTE I — O genoma bacteriano: um cromossomo e alguns replicons a mais", primeira: true)

#subtopico("1.1 Sem núcleo: onde fica o DNA bacteriano e que forma ele tem")

O prefixo "pro-cario" quer dizer *antes do núcleo*, e a ausência do envoltório nuclear é o fato estrutural do qual tudo o mais decorre. O #sigla("DNA", [ácido desoxirribonucleico — a molécula que guarda a informação genética]) bacteriano fica solto no citoplasma, condensado numa região sem membrana chamada #termo-nota[nucleoide][região do citoplasma bacteriano onde o cromossomo está condensado; não tem envoltório e não é organela]. No eucarioto, o mesmo material está trancado dentro do núcleo, separado do citoplasma por uma dupla membrana.

Na esmagadora maioria das bactérias esse cromossomo é único, de fita dupla e circular — um anel fechado, sem extremidades livres. A circularidade não é regra absoluta e vale registrar as exceções, porque elas derrubam a definição decorada: _Borrelia burgdorferi_ e _Streptomyces_ têm cromossomo linear, e há espécies com plasmídeos lineares. O que é universal não é a forma do anel, é a ausência de núcleo.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-03.png",
  largura: 58%,
  legenda: [À esquerda, o cromossomo bacteriano condensado direto no citoplasma; à direita, os cromossomos eucarióticos dentro do núcleo. Repare na linha de baixo do quadro: além do cromossomo, cada lado tem DNA extra — plasmídeo na bactéria, mitocôndria e cloroplasto no eucarioto.])

O detalhe que costuma passar em branco é geométrico, e ele acaba sendo o mais útil clinicamente. O cromossomo de _E. coli_ tem cerca de 1,5 milímetro de circunferência; a célula que o abriga tem 2 micrômetros de comprimento. O anel é aproximadamente mil vezes maior que a caixa. Ele só cabe porque está torcido sobre si mesmo, num estado chamado #termo-nota[superenovelamento][torção da dupla-hélice sobre o próprio eixo, que compacta o DNA e é imposta ativamente por enzimas], que não acontece por acaso nem por falta de espaço: é imposto e mantido por enzimas que gastam energia para isso.

A enzima central desse trabalho é a DNA girase, uma topoisomerase que corta as duas fitas, passa um segmento do anel através da abertura e religa o corte — introduzindo torção negativa a cada ciclo. Ela não sintetiza DNA; ela administra a tensão. E é justamente por isso que ela importa fora da genética: como a girase é bacteriana e não tem equivalente exato na nossa célula, uma classe inteira de antibióticos, as quinolonas, foi construída para travá-la. Travada a girase, o cromossomo não relaxa, a forquilha de replicação não avança e a bactéria para de se dividir. Guarde esse alvo — ele volta na PARTE II, quando uma mutação num único aminoácido dessa enzima transformar a quinolona em água.

#mini-resumo[Sem núcleo, o cromossomo bacteriano fica no citoplasma e só cabe ali porque topoisomerases o mantêm torcido — e a enzima que faz essa torção é um alvo de antibiótico.]

#subtopico("1.2 O tamanho do genoma e o preço que ele cobra")

Um genoma bacteriano é um catálogo de tudo o que aquela célula sabe fabricar sozinha, e o tamanho desse catálogo varia mais de dez vezes entre espécies que continuam sendo, todas elas, bactérias. _Mycoplasma genitalium_ tem 0,58 × 10⁶ pares de base e cerca de 480 genes. _Staphylococcus aureus_ tem 2,8 × 10⁶; _E. coli_, 4,67 × 10⁶ com cerca de 4.300 genes; _Streptomyces_, o gênero que fornece boa parte dos antibióticos em uso, chega a 8 × 10⁶. Bactérias de vida livre ficam tipicamente entre dois e cinco mil genes.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-04.png",
  largura: 64%,
  legenda: [Compare as colunas de tamanho e de número de genes e depois a última linha. O ser humano tem quinhentas vezes mais pares de base que _E. coli_, mas não quinhentas vezes mais genes — a diferença está sobretudo no DNA que não codifica proteína.])

A leitura errada desse quadro é hierárquica, como se genoma pequeno significasse bactéria mais primitiva. O mecanismo é o oposto, e ele é elegante. O genoma minúsculo de _Mycoplasma_ é resultado de *perda*: um ancestral de vida livre, ao passar a viver permanentemente dentro de um hospedeiro, encontrou aminoácidos, nucleotídeos e precursores prontos no ambiente. Genes de vias biossintéticas que deixaram de ser usados deixaram de ser mantidos pela seleção e foram eliminados. O resultado é uma bactéria que não consegue mais viver fora — e que, no laboratório, exige meios de cultura enriquecidos justamente porque perdeu a capacidade de fabricar o que outras fabricam. Genoma pequeno é assinatura de dependência, não de simplicidade.

Para dimensionar a escala: _Saccharomyces cerevisiae_ tem 1,2 × 10⁷ pares de base em dezesseis cromossomos lineares dentro de um núcleo — é eucarionte, ainda que unicelular —, e o ser humano tem 3,2 × 10⁹ em quarenta e seis cromossomos lineares, cerca de mil vezes o genoma de _E. coli_.

#mini-resumo[Em uma frase: o tamanho do genoma mede quanto a bactéria fabrica sozinha, e genoma curto costuma indicar uma vida dependente do hospedeiro, não uma bactéria mais rudimentar.]

#subtopico("1.3 O plasmídeo: um replicon a mais, funções a mais")

Se toda a informação necessária estivesse no cromossomo, uma bactéria não teria como adquirir uma capacidade nova sem alterar o próprio cromossomo — o que é lento e arriscado. O plasmídeo é a solução para esse limite: uma molécula de DNA circular, de fita dupla, muito menor que o cromossomo, fisicamente separada dele e com origem de replicação própria. Ter origem própria é o que faz dele um #termo-nota[replicon][qualquer molécula de DNA que se replica como unidade autônoma, a partir de uma origem de replicação própria] independente, capaz de se duplicar no seu próprio ritmo.

O conteúdo do plasmídeo é sempre acessório, e a lista do que ele carrega é praticamente a lista dos problemas clínicos da microbiologia: resistência a antibióticos, resistência a metais pesados, adesão à mucosa, invasão de tecidos, produção de toxinas, capacidade de fermentar açúcares que a espécie normalmente não fermenta. O caminho é o de sempre — a sequência plasmidial é transcrita em #sigla("RNA", [ácido ribonucleico — a cópia de trabalho da informação genética]) mensageiro, traduzida em proteína, e essa proteína tem função enzimática ou estrutural. No caso da resistência a um beta-lactâmico, a proteína é uma beta-lactamase que a bactéria exporta e que quebra o anel do antibiótico antes que ele alcance seu alvo na parede.

#figura-lateral("/figuras/micro-06-genetica-bacteriana/slide-06.png",
  lado: "right",
  largura-figura: 44%,
  texto: [A separação física entre os dois DNAs tem uma consequência de identidade que é fácil de enunciar e fácil de esquecer. O que define que uma bactéria é _E. coli_, e não _Salmonella_ ou _Shigella_, está escrito no cromossomo. Se ela perde o plasmídeo numa divisão, continua exatamente a mesma espécie — apenas deixou de saber fazer uma coisa. O plasmídeo acrescenta ferramenta, não identidade.],
  legenda: [Cromossomo e plasmídeo dentro da mesma célula, e à direita a mesma molécula plasmidial vista ao #sigla("TEM", [microscopia eletrônica de transmissão — técnica que usa feixe de elétrons para ver estruturas abaixo do limite da luz]).])

Nem todo plasmídeo é igual, e três distinções vão ser cobradas o tempo todo na PARTE III. Um plasmídeo é *conjugativo* se codifica a maquinaria que o transfere para outra célula, e há muitos que não codificam — esses ficam onde estão. Um plasmídeo é *epissomal* se é capaz de se integrar ao cromossomo e sair dele; integrado, ele deixa de se replicar sozinho e passa a ser copiado junto com o cromossomo hospedeiro. E há a distinção de *número de cópias*: alguns existem em poucas unidades por célula, outros em dezenas. Como regra prática, plasmídeos conjugativos são grandes — carregam muitos genes de maquinaria — e por serem grandes existem em baixo número de cópias.

Um refinamento que explica um fenômeno de bancada: dois plasmídeos podem ser incompatíveis. Cada plasmídeo controla o próprio número de cópias por um sistema de moléculas reguladoras que contam quantas origens existem. Dois plasmídeos que usam o *mesmo* sistema de contagem são lidos pela célula como um só, e a cada divisão um dos dois tende a ser perdido. É por isso que uma bactéria não acumula indefinidamente plasmídeos parecidos: eles se excluem.

#subtopico("1.4 Replicação bidirecional e partição: por que um plasmídeo se perde")

O plasmídeo do subtópico anterior só é útil à população se chegar às células filhas, e é aí que ele encontra um problema que o cromossomo não tem. Vale primeiro ver como o cromossomo resolve. A replicação começa num ponto único do anel, a origem, e dali partem *duas* forquilhas em sentidos opostos, que percorrem cada uma metade do círculo e se encontram do lado oposto. Por isso a replicação bacteriana se chama bidirecional: não é uma forquilha dando a volta inteira, são duas dividindo o trajeto pela metade — o que corta o tempo de duplicação ao meio.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-05.png",
  largura: 64%,
  legenda: [Do lado esquerdo, a célula alonga, a membrana invagina e a parede transversal fecha entre as duas cópias. Do lado direito, o mesmo processo visto na molécula: uma origem, duas forquilhas correndo em sentidos opostos, encontro no ponto de terminação.])

Duas consequências merecem ser separadas. A primeira é que a replicação é semiconservativa: cada anel-filho tem uma fita antiga e uma fita recém-sintetizada, e isso vale para *ambas* as filhas — não existe a filha que ficou com o DNA velho e a que ficou com o novo. A segunda é que a segregação do cromossomo é ativa e confiável: as duas cópias são ancoradas em pontos opostos da célula antes de o septo fechar, de modo que cada filha recebe exatamente uma.

O plasmídeo não tem essa garantia. Ele se replica por conta própria e depois se distribui com o citoplasma que se reparte. Se existem trinta cópias na célula, o acaso da partição entrega uma boa fração para cada lado e nenhuma filha fica sem. Se existem duas cópias, há uma chance real de as duas irem para o mesmo lado — e a outra filha nasce sem o plasmídeo, geneticamente diferente da irmã.

Esse é um fenômeno mensurável, e o modo de medir é instrutivo. Suponha um plasmídeo que carrega resistência à ampicilina. Semeie a mesma cultura em duas placas, uma com o antibiótico e outra sem. Na placa sem ampicilina crescem todas as células; na placa com ampicilina crescem apenas as que ainda têm o plasmídeo. A diferença no número de colônias é a fração da população que o perdeu — a perda deixa de ser suposição e vira número.

Diante desse vazamento, muitos plasmídeos de baixo número de cópias carregam um sistema que corrige o problema de um jeito brutal: um par de genes que codifica uma toxina estável e um antídoto instável. Enquanto o plasmídeo está presente, a célula repõe o antídoto e nada acontece. Se a célula-filha nasce sem o plasmídeo, o antídoto que ela herdou se degrada em minutos, a toxina herdada permanece e a mata. Não é que o plasmídeo deixe de se perder — é que a célula que o perde não sobrevive para contar, e a população continua inteiramente resistente.

#clinica-box("Por que a resistência se espalha mais rápido do que a bactéria resistente",
[Quando um gene de resistência está no cromossomo, ele só chega a outra bactéria se a bactéria que o carrega se dividir: a resistência avança na velocidade da multiplicação celular, dentro de uma espécie.

Quando o mesmo gene está num plasmídeo conjugativo, ele muda de veículo. Passa horizontalmente para células vizinhas que já estão ali, inclusive de outras espécies, sem depender de divisão alguma — e os módulos toxina-antídoto acima garantem que, uma vez adquirido, ele não se perca. É por isso que um surto hospitalar de resistência pode aparecer em enterobactérias diferentes na mesma enfermaria em poucos dias, e é por isso que a pergunta clínica correta diante de um antibiograma inesperado não é apenas "esta bactéria mutou", mas "esta bactéria recebeu alguma coisa". A PARTE III é sobre esse recebimento.])

#parte-title("PARTE II — Mutação: como o erro nasce, é consertado ou fica")

#subtopico("2.1 Mutação espontânea: o erro que a química da água impõe")

A palavra "espontânea" sugere um evento sem causa, e é exatamente essa a leitura a desfazer. Espontânea significa *sem agente externo* — a causa continua sendo física e química, e conhecê-la explica por que a taxa de erro tem o valor que tem.

Comece pela enzima. A DNA polimerase é processiva: avança pela fita-molde encaixando, a cada passo, a base complementar à que está lendo. E ela é revisora — a cada nucleotídeo colocado, verifica o pareamento; se estiver errado, uma atividade exonucleásica que trabalha no sentido contrário ao da síntese retira o nucleotídeo recém-colocado e a enzima tenta de novo. Com esse duplo mecanismo, sobra aproximadamente *um erro a cada 10⁸ bases incorporadas*.

O motivo de sobrar alguma coisa está na água. As bases nitrogenadas são moléculas hidratadas em equilíbrio químico, e cada uma pode existir em duas formas que diferem pela posição de um átomo de hidrogênio — um fenômeno chamado #termo-nota[tautomeria][equilíbrio químico entre duas formas de uma mesma molécula, que diferem pela posição de um hidrogênio]. A forma rara de uma base tem geometria de pontes de hidrogênio diferente da forma comum, e nessa forma ela pareia com o parceiro errado. A polimerase encontra uma citosina momentaneamente tautomerizada, lê nela o padrão de outra base e insere adenina onde deveria ir guanina. Na replicação seguinte, aquela adenina indevida é copiada como se fosse legítima, e a troca se fixa.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-10.png",
  largura: 60%,
  legenda: [A definição operacional que a aula usa: mutação é modificação súbita e hereditária do conjunto gênico que não se explica por recombinação. Espontânea vem de funções celulares normais; induzida vem de um agente aplicado de fora.])

Há uma segunda fonte espontânea que a fala não desenvolve e que vale acrescentar, porque ela explica um padrão de mutação que aparece repetidamente. A citosina sofre desaminação espontânea em água e vira uracila — uma base que não pertence ao DNA. Como não pertence, é reconhecida como intrusa por uma enzima específica, removida e substituída por citosina; o dano é corriqueiro e o conserto é eficiente. Mas quando a citosina está metilada, a desaminação produz *timina*, que é uma base legítima do DNA. O sistema de vigilância não tem como saber que aquela timina é intrusa, e o erro passa. Posições metiladas do genoma acumulam, por isso, mutações C→T em frequência muito acima da média.

O último passo é interpretativo. Uma taxa de erro de 10⁻⁸ parece um defeito de fabricação, mas é o contrário. Numa cultura com 10⁹ células por mililitro, essa taxa garante que exista, naquele tubo, um punhado de variantes em qualquer gene. A maioria é neutra ou prejudicial. Uma delas, eventualmente, tem uma enzima que funciona melhor no ambiente do momento — e essa cresce mais rápido e domina a população. A fidelidade da cópia é alta o bastante para preservar a espécie e baixa o bastante para alimentar a seleção.

#confusao-prevista(
  titulo: "O antibiótico não cria o mutante resistente",
  aluno_acha: [aluno acha que a bactéria "desenvolve" resistência em resposta ao antibiótico, como se o antibiótico ensinasse],
  mecanismo: [o mutante já existia na população antes de qualquer antibiótico chegar, produzido pela taxa espontânea de erro. O antibiótico não cria — ele *seleciona*: mata os sensíveis e libera espaço e nutriente para o raro variante que já era resistente. Um único mutante em 10⁸ células vira a população inteira em poucas horas. A exceção que confirma a regra aparece em 2.4, onde alguns antibióticos de fato elevam a taxa de mutação.],
)

#subtopico("2.2 Mutação induzida: o que os agentes físicos e químicos fazem com a molécula")

Um agente mutagênico — também chamado genotóxico — é qualquer coisa que incida sobre o DNA e produza nele uma alteração química. Convém uma observação de escopo antes de listar: esses agentes atingem também proteínas e lipídios da célula, e o dano ali é reversível, porque a célula ressintetiza a proteína a partir do gene. O DNA é o único componente que não tem molde de onde ser refeito, e é por isso que o dano nele tem estatuto diferente.

Entre os agentes físicos, o mais bem caracterizado é a radiação #sigla("UV", [ultravioleta — faixa do espectro com comprimento de onda entre 100 e 400 nanômetros]). O fóton ultravioleta é absorvido por pirimidinas vizinhas *na mesma fita* e força entre elas uma ligação covalente, formando um #termo-nota[dímero de pirimidina][par de pirimidinas adjacentes da mesma fita unidas covalentemente por absorção de UV; deforma a hélice] — timina-timina, timina-citosina ou citosina-citosina. O ponto mecanístico central é que essa lesão não troca informação: ela cria um cotovelo na hélice. As duas bases fundidas deixam de parear com a fita oposta, a geometria local se perde e a polimerase, ao chegar ali, não encontra molde legível e trava.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-12.png",
  largura: 64%,
  legenda: [À esquerda, o antes e o depois da incidência do fóton. À direita, o detalhe químico: o anel ciclobutano destacado em rosa é a ligação covalente nova entre as duas timinas vizinhas — e é essa fusão que dobra a fita e trava a replicação.])

Vale acrescentar que o dímero em anel ciclobutano é o produto mais comum, mas não o único: a mesma absorção gera também um segundo tipo de ligação entre pirimidinas vizinhas, mais raro e mais distorcivo, que a fotoliase do subtópico seguinte não desfaz. É uma pista de que nenhum sistema de reparo cobre sozinho todo o repertório de dano.

A radiação ionizante — raios X, raios gama — opera por mecanismo diferente e mais destrutivo. Ela arranca elétrons das moléculas por onde passa, gerando radicais livres que atacam o esqueleto de açúcar-fosfato. O resultado é quebra: de uma fita só, ou das duas no mesmo ponto. A quebra de dupla fita é a lesão mais grave que existe, porque desfaz a continuidade física da molécula e não deixa fita íntegra para servir de referência. Calor elevado produz um conjunto misto de lesões, incluindo perda de bases.

Entre os agentes químicos, três famílias têm mecanismos distintos que vale separar. As *moléculas planares* — o brometo de etídio é o exemplo de bancada — têm formato de placa e se encaixam entre dois pares de base empilhados, afastando-os. A polimerase que passa por ali perde o registro da fase de leitura e insere ou omite um nucleotídeo; o dano não é troca de base, é deslocamento de todo o quadro de leitura a partir dali, o que costuma destruir a proteína inteira. Os *agentes alquilantes*, como o metilmetanossulfonato, ligam covalentemente um radical metila ou etila a uma base. A guanina metilada no oxigênio 6 muda de preferência de pareamento e passa a aceitar timina no lugar de citosina — uma troca G:C→A:T fixada na replicação seguinte. E a *água oxigenada* oxida bases e açúcares, produzindo um espectro largo de danos.

#mini-resumo[O que ficou de pé: UV deforma sem trocar informação, ionizante quebra o esqueleto, intercalante desloca a fase de leitura e alquilante troca a preferência de pareamento — quatro mecanismos diferentes que exigirão sistemas de reparo diferentes.]

#subtopico("2.3 Os três destinos de um DNA lesado — e os reparos que não erram")

O subtópico anterior terminou com um DNA lesado dentro de uma célula viva. O que acontece a partir dali não é uma coisa só: são três desfechos possíveis, e a mutação é apenas um deles. Todo ser vivo, de bactéria a humano, possui conjuntos multienzimáticos de reparo, e o destino da célula depende de o que esses conjuntos conseguem fazer.

O primeiro desfecho é a *reparação correta*: as enzimas reconhecem a lesão, corrigem e a sequência original é restaurada por completo. Não sobra mutação. O segundo é a *ausência de reparação*, seja porque aquela célula não tem o sistema, seja porque a quantidade de lesão esgotou a capacidade dele. A replicação não avança sobre uma fita ilegível, e a célula morre. O terceiro é a *reparação incorreta*, tema do subtópico 2.4: a célula intervém para não morrer e, no processo, deixa erros na sequência.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-15.png",
  largura: 52%,
  legenda: [Os três caminhos a partir do DNA lesado. Note que dois deles resolvem o problema da célula — restaurar ou tolerar — e apenas um dos dois preserva a informação. A mutação é o preço do galho da direita.])

O primeiro sistema de reparo fiel opera apenas com luz visível e desfaz apenas uma lesão. A enzima DNA fotoliase circula pelo DNA e reconhece a deformação criada pelo dímero de pirimidina; liga-se a ele, absorve energia de um fóton de luz visível e usa essa energia para romper a ligação covalente entre as duas pirimidinas, devolvendo cada uma ao pareamento normal. Chama-se fotorreativação, é o mecanismo mais econômico que existe — nenhuma base é removida, nenhuma é ressintetizada — e é rigorosamente específico: dímero de pirimidina, mais nada.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-17.png",
  largura: 62%,
  legenda: [O ciclo completo da fotorreativação e, ao lado, as três faixas do ultravioleta. Quanto menor o comprimento de onda, maior a energia: o UVC de 260 nanômetros é o mais energético e é o usado nas lâmpadas germicidas de laboratório.])

Duas observações práticas decorrem disso. Como o UV tem baixo poder de penetração — atravessa poucos milímetros de tecido —, o dano que ele causa em nós é de superfície: eritema, fotoenvelhecimento e câncer de pele, nunca câncer de estômago. E, no laboratório, uma cultura irradiada com UV precisa ser mantida no escuro até a leitura, porque a luz ambiente reativa a fotoliase e desfaz o experimento.

No escuro, ou no interior do corpo, dois sistemas assumem. O *reparo por excisão* reconhece a distorção, corta a fita danificada dos dois lados da lesão, remove o trecho e uma DNA polimerase específica ressintetiza usando a fita oposta como molde; uma ligase fecha. Há duas versões: a excisão de base retira uma única base quimicamente alterada, e a excisão de nucleotídeo retira um oligonucleotídeo inteiro em torno de uma lesão volumosa — o dímero é substrato desta segunda. O *reparo recombinacional* é para o caso mais difícil, a quebra de dupla fita, em que não há fita íntegra local para servir de molde. Ele exige que a região já tenha sido duplicada, para que exista uma segunda cópia; a proteína RecA promove a invasão da cópia íntegra pela extremidade quebrada, e a informação é copiada de lá. Excisão e recombinacional, quando dão conta, restauram a sequência integralmente.

#clinica-box("Xeroderma pigmentoso: o que acontece quando falta a excisão de nucleotídeo",
[O mesmo reparo por excisão de nucleotídeo descrito acima existe em nós, com outras proteínas e a mesma lógica: reconhecer distorção, cortar dos dois lados, ressintetizar. Crianças com xeroderma pigmentoso nascem com mutação em um dos genes desse sistema.

A consequência é uma demonstração do subtópico inteiro. Elas produzem dímeros de pirimidina na pele como qualquer pessoa exposta ao sol, mas não os removem. Cada exposição deixa lesões que a replicação seguinte encontra, e onde o reparo falha entra a tolerância a lesões do subtópico 2.4 — que insere bases ao acaso. As mutações se acumulam em queratinócitos e melanócitos, e o resultado é câncer de pele múltiplo antes dos dez anos de idade, em áreas fotoexpostas. A doença mostra que o reparo não é um detalhe bioquímico: ele é o que separa exposição solar de carcinogênese.])

#subtopico("2.4 Tolerância a lesões: quando reparar direito deixa de ser opção")

Os sistemas do subtópico anterior partilham um limite que só aparece sob dano intenso: todos exigem tempo e capacidade enzimática disponível. Quando a dose de agente genotóxico é alta, o número de lesões supera o número de complexos de reparo, a replicação começa mesmo assim e a forquilha encontra fita ilegível. Cada encontro desses interrompe a síntese naquele ponto; a polimerase retoma adiante e deixa uma lacuna para trás. A célula acumula lacunas mais rápido do que consegue fechá-las, e a partir de certo ponto o cromossomo deixa de poder ser terminado. Sem cromossomo completo, não há divisão — e a morte é certa.

É contra esse desfecho que a célula aciona o último recurso, e o nome dele diz o que ele faz: *tolerância a lesões*. Um programa de emergência suprime a atividade revisora da polimerase e permite que ela insira uma base qualquer na posição ilegível, apenas para que a forquilha avance. A base inserida tem uma chance em quatro de estar certa. Nas outras três, ficou registrada uma mutação — e a célula sobreviveu.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-19.png",
  largura: 58%,
  legenda: [Os dois caminhos diante de uma forquilha travada. À esquerda, a síntese por translesão passa por cima da lesão inserindo base ao acaso — sobrevive e erra. À direita, o reparo dependente de homologia usa a cópia irmã e não erra. As etiquetas na base da figura resumem o preço de cada rota.])

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-18.png",
  largura: 62%,
  legenda: [Os dois sistemas fiéis que operam sem luz, lado a lado. À esquerda, a excisão corta e ressintetiza a fita danificada usando a oposta como molde. À direita, o recombinacional resolve a quebra de dupla fita buscando a informação na cópia irmã já replicada.])

Vale abrir o mecanismo, porque ele explica um fenômeno clínico incômodo. O sinal que dispara o programa é a fita simples exposta na forquilha travada; a proteína RecA se liga a essa fita simples e passa a estimular a autoclivagem de um repressor que, até então, mantinha desligados dezenas de genes de emergência. Desligado o repressor, os genes acendem em bloco — e entre eles estão polimerases especiais, chamadas de translesão, que conseguem copiar por cima de uma lesão porque têm sítio catalítico frouxo e não fazem revisão. Elas atuam apenas no trecho danificado e cedem lugar de volta à polimerase replicativa; se permanecessem, o genoma inteiro sairia crivado de erros.

A consequência prática é que a taxa de mutação da população deixa de ser fixa. Sob estresse ao DNA, ela sobe uma ou duas ordens de grandeza — e isso, numa cultura de 10⁹ células, significa produzir variantes em cada gene, inclusive nos genes que determinam sensibilidade a antibiótico.

#atencao-box("O antibiótico que fabrica a própria resistência",
[Duas classas muito usadas atingem diretamente o DNA. A quinolona trava a girase e a topoisomerase IV e produz quebras; a sulfa e o trimetoprim esvaziam o suprimento de precursores de nucleotídeo e travam a forquilha. Nos dois casos, o sinal que dispara o programa de emergência é gerado *pelo próprio tratamento*.

O encadeamento é direto: o antibiótico gera o dano, o dano dispara a resposta de emergência, a resposta liga as polimerases sem revisão, a taxa de mutação sobe, e entre as mutações produzidas aparecem trocas de aminoácido na própria girase que reduzem a afinidade da quinolona. A bactéria sob tratamento fabrica, dentro do paciente, o mutante que sobrevive ao tratamento.

*Por que isso muda conduta:* a dose e a duração não são detalhes administrativos. Dose subterapêutica mantém o estresse sem esterilizar, e é exatamente a condição que maximiza a produção de mutantes. Tratamento incompleto de infecção urinária com quinolona é o cenário clássico dessa falha.])

#subtopico("2.5 Duas aplicações: obter mutante e flagrar mutágeno")

Todo o percurso do dano ao reparo deixa de ser abstrato quando se olha para o que se faz com ele em laboratório. As duas aplicações são simétricas: numa, produz-se mutante de propósito; na outra, usa-se o aparecimento de mutantes como sinalizador.

A primeira é a *obtenção de mutantes*. Submete-se uma população a um agente mutagênico em dose que mate a maioria e deixe sobreviventes alterados, e depois seleciona-se, entre os sobreviventes, o que interessa. O exemplo histórico mais consequente é a penicilina: a cepa original de _Penicillium_ isolada por Fleming produzia uma quantidade irrisória do antibiótico, e o que existe hoje é o produto de sucessivos ciclos de irradiação, cultivo e isolamento dos indivíduos mais produtivos. A linhagem industrial atual rende mais de dez mil vezes a original. O mesmo procedimento gera mutantes auxotróficos — incapazes de sintetizar um aminoácido — que são as ferramentas de todo experimento genético, e é a base de programas de melhoramento vegetal.

A segunda é a *detecção de substâncias mutagênicas*, e ela é obrigatória antes de qualquer fármaco novo chegar a testes em animais.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-23.png",
  largura: 66%,
  legenda: [À esquerda, o teste de Ames: a bactéria auxotrófica é semeada em meio sem histidina, e só cresce a que reverteu. À direita, o cromoteste: o mesmo dano lido como cor amarela, quantificada em espectrofotômetro ao longo do tempo de incubação.])

O teste de Ames usa uma linhagem de _Salmonella_ portadora de uma mutação que a impede de sintetizar histidina. Semeada em meio mineral sem histidina, ela não cresce. Se a substância testada for mutagênica, algumas células sofrerão uma segunda mutação que restaura o gene, e essas voltam a crescer: as colônias que aparecem são *revertentes*, e o número delas, comparado ao controle sem substância, mede a potência mutagênica. Repare que o teste não conta sobreviventes — conta reversões.

Um refinamento indispensável, ausente da versão simplificada: muitas substâncias não são mutagênicas como chegam ao organismo, e só se tornam reativas depois de metabolizadas pelo fígado. Testá-las diretamente sobre a bactéria produziria falso-negativo. Por isso o protocolo inclui uma fração de enzimas hepáticas de mamífero na mistura, simulando essa ativação metabólica antes do contato com a bactéria.

O cromoteste é o mesmo raciocínio com leitura mais direta. Usa uma _E. coli_ construída por engenharia genética, na qual o gene da beta-galactosidase foi fundido a um promotor que só liga quando a resposta de emergência ao dano do subtópico 2.4 é disparada. Havendo dano ao DNA, o promotor acende, a enzima é produzida e converte um substrato incolor em produto amarelo. A intensidade do amarelo, lida em espectrofotômetro ao longo do tempo, quantifica o genotóxico.

Resta justificar por que uma triagem de carcinogenicidade humana começa numa bactéria, já que ela é unicelular e nós não. A justificativa está no alvo: a molécula de DNA e a química que a danifica são as mesmas nos dois. Se uma substância troca bases numa bactéria, ela troca bases numa célula humana; e numa célula somática essa troca pode cair num gene que controla a divisão celular, de modo que, perdido o controle, a célula prolifera sem freio. É esse encadeamento que sustenta a regra operacional de que *todo agente mutagênico é potencialmente carcinogênico*.

O peso prático disso é econômico e ético ao mesmo tempo. Reprovar no Ames encerra o desenvolvimento da molécula ali, antes de qualquer animal e a custo baixíssimo — e um falso-negativo, produzido por omitir a fração hepática, deixa passar para ensaio humano uma substância cuja toxicidade só apareceria depois de metabolizada.

#mini-resumo[Se você só lembrar de uma coisa: o mesmo dano que faz aparecer colônia revertente na placa faria, numa célula humana, a mutação que inicia um tumor — e é por isso que a bactéria serve de sentinela.]

#parte-title("PARTE III — Recombinação: como o DNA anda de bactéria em bactéria")

#subtopico("3.1 Transformação: DNA nu que entra pela membrana")

A PARTE II mostrou que a mutação é uma alteração produzida *dentro* da célula, a partir do que ela já tinha. A recombinação é a outra metade da dicotomia da introdução: material genético que chega de fora e se incorpora. A primeira das três rotas foi também a primeira a ser descrita — e a descrição veio dezesseis anos antes de alguém saber o que estava sendo transferido.

Em 1928, Frederick Griffith trabalhava com pneumococo em duas apresentações. A cepa lisa tem cápsula, resiste à fagocitose e mata o camundongo injetado; a cepa rugosa não tem cápsula e é inofensiva. Griffith matou a cepa lisa pelo calor e injetou o lisado: o camundongo sobreviveu, como esperado. Então misturou o lisado da cepa lisa morta com a cepa rugosa viva e injetou a mistura — e o camundongo morreu. Da autópsia ele recuperou pneumococo *liso*, vivo. Alguma coisa no lisado tinha convertido a rugosa em lisa de modo hereditário. Griffith chamou aquilo de princípio transformante, e o nome pegou porque ninguém sabia o que era.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-24.png",
  largura: 66%,
  legenda: [À esquerda, os quatro braços do experimento de Griffith, e o resultado que não fecha com nenhuma explicação disponível em 1928. À direita, a resolução de 1944: o lisado é fracionado, cada fração é oferecida separadamente à cepa rugosa, e só a fração de ácido nucleico transforma.])

A resposta veio em 1944, quando a bioquímica de separação amadureceu. Avery, MacLeod e McCarty fracionaram o lisado em lipídios, polissacarídeos, proteínas e ácidos nucleicos, e ofereceram cada fração isoladamente à cepa rugosa. Apenas a fração de ácido nucleico transformou. O passo decisivo foi de eliminação: tratar essa fração com enzimas que destroem proteína não aboliu a transformação; tratá-la com a enzima que destrói DNA aboliu. O princípio transformante era o DNA — e essa é a demonstração de que o material genético é o DNA e não a proteína, contra o consenso da época.

Transformação, portanto, define-se pelo veículo: *DNA nu, livre no meio, atravessando a membrana*. Nenhum intermediário, nenhum contato entre células. Na natureza esse DNA vem de bactérias que morreram e se romperam ali por perto.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-25.png",
  largura: 60%,
  legenda: [O trajeto de entrada. Complexos de superfície capturam o fragmento livre, uma nuclease degrada uma das fitas, e apenas a fita restante entra no citoplasma — onde precisa encontrar sequência homóloga para se integrar.])

Entrar não é automático, e três restrições explicam por que não. A primeira é a *competência*: a capacidade de captar DNA é um estado fisiológico transitório, com genes próprios, que muitas espécies ativam apenas em condições específicas. No pneumococo esse estado é coordenado por um peptídeo que as células secretam e detectam umas nas outras — quando a densidade populacional é alta o bastante, a concentração do peptídeo cruza um limiar e a população inteira entra em competência ao mesmo tempo. A segunda é que a captação satura: aumentando a concentração de DNA oferecido, o número de transformantes cresce até um teto e para, porque os sítios de captação são finitos. A terceira é a preferência de substrato — _Streptococcus pneumoniae_ capta fragmentos lineares com eficiência, enquanto _E. coli_ é transformada preferencialmente por plasmídeos.

Falta a restrição que responde à objeção mais natural, a de que uma bactéria captando DNA sem parar acabaria virando outra espécie. Duas barreiras impedem isso. Um fragmento linear que entra *não tem origem de replicação*: ele não se duplica sozinho e desaparece na próxima divisão, a menos que se recombine com o cromossomo — e a recombinação exige homologia de sequência, o que na prática limita a troca a parentes próximos. Além disso, a célula carrega enzimas de restrição que cortam DNA que não traz o padrão de metilação da casa. É por isso que o pneumococo troca genes com pneumococos e continua pneumococo: a porta existe, mas só abre para o que se parece com quem já está dentro.

#subtopico("3.2 Conjugação: o contato que move um genoma inteiro")

Se a transformação é uma carta deixada na rua e recolhida por quem passa, a conjugação é entrega em mãos. Ela é a transferência de material genético de uma bactéria doadora para uma receptora *em contato físico*, mediada, nas Gram-negativas, por um apêndice especializado: o pilus de conjugação. As Gram-positivas dispensam o apêndice e resolvem por aproximação direta.

Em 1946, Lederberg e Tatum tinham duas linhagens auxotróficas de _E. coli_ — a cepa A não sintetizava metionina, a cepa B não sintetizava leucina —, e nenhuma das duas cresce em meio mínimo. Cultivadas juntas de um dia para o outro e semeadas em meio mínimo, apareceram colônias: células que sabiam fazer as duas coisas.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-28.png",
  largura: 62%,
  legenda: [O tubo em U com a membrana semipermeável no meio: DNA atravessa, células não. É o controle que separa transformação de conjugação — sem contato entre as células, nada cresce em meio mínimo.])

O experimento decisivo testa a hipótese alternativa: se o fenômeno fosse transformação, DNA livre bastaria. Montaram um tubo em U com membrana semipermeável no meio, que deixa passar DNA mas não células, e cultivaram A de um lado e B do outro. Nada cresceu. Como o DNA podia atravessar e mesmo assim nada aconteceu, o fenômeno exige as duas células em contato — e a esse contato eles deram o nome de conjugação.

O mecanismo molecular, um degrau acima da descrição da aula, é o seguinte. O plasmídeo conjugativo tem um sítio próprio de origem de transferência, distinto da origem de replicação. Uma enzima corta uma das fitas exatamente nesse sítio, prende-se à extremidade livre e conduz essa fita simples através do canal formado na junção entre as duas células — enquanto isso, ambas as células ressintetizam a fita complementar sobre o molde que lhes restou. O saldo é que ao final da conjugação *as duas* células têm o plasmídeo completo: a doadora não perde nada. O pilus, note-se, faz o contato e aproxima as membranas; a passagem ocorre pelo canal de secreção montado na junção.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-31.png",
  largura: 62%,
  legenda: [Em cima, a transferência do plasmídeo livre: uma fita passa, cada lado ressintetiza a complementar. Embaixo, a situação Hfr — o fator de fertilidade integrado ao cromossomo puxa atrás de si o cromossomo inteiro.])

Falta o caso que mais rende. Alguns plasmídeos conjugativos são epissomais, isto é, integram-se ao cromossomo. Uma célula com o fator de fertilidade integrado passa a se chamar Hfr, de alta frequência de recombinação — e Hfr não é uma espécie nem um tipo de bactéria, é um *estado* dessa célula. Na conjugação de uma Hfr, o corte inicial ocorre dentro do fator integrado, e o que começa a atravessar é o fator seguido do cromossomo inteiro atrás dele. A travessia completa leva cerca de noventa minutos, e quase nunca termina: a ponte se rompe antes.

Foi justamente esse rompimento que virou instrumento. Interrompendo a conjugação em tempos crescentes — agitando os tubos aos dez, vinte, cinquenta minutos — e verificando quais marcadores já haviam chegado à receptora, os pesquisadores ordenaram os genes ao longo do cromossomo pelo tempo de entrada. O primeiro mapa completo do genoma de _E. coli_ foi construído assim, em minutos de conjugação, décadas antes de existir sequenciamento.

#clinica-box("Plasmídeos promíscuos e o paciente da enfermaria ao lado",
[A maioria dos plasmídeos conjugativos tem faixa estreita de hospedeiro. Alguns, chamados promíscuos, transferem-se para praticamente qualquer Gram-negativa. O RP4 é o exemplo canônico: carrega resistência a carbenicilina, neomicina, canamicina e tetraciclina num único pacote.

O encadeamento clínico é direto. Uma _E. coli_ intestinal portadora do RP4 entra em contato com uma _Pseudomonas aeruginosa_ que coloniza o trato respiratório de um paciente entubado. A conjugação não exige parentesco — apenas proximidade e contato. Depois dela, a _Pseudomonas_ que era sensível carrega quatro resistências de uma vez, adquiridas sem nenhuma mutação e sem nenhuma exposição prévia àquelas drogas.

*Por que isso importa na prática:* o antibiograma de admissão descreve o isolado daquele dia, não uma propriedade estável do paciente. E explica por que higiene de mãos e isolamento de contato reduzem resistência: eles interrompem exatamente a etapa de aproximação física de que a conjugação depende.])

#subtopico("3.3 Transdução: o fago como veículo do gene alheio")

A terceira rota usa um intermediário que não é bactéria: um vírus. Bacteriófagos são vírus que infectam bactérias, e o ciclo lítico deles tem uma etapa que abre a porta para o acidente. O fago adere à superfície bacteriana por atração eletrostática, injeta o próprio material genético, desliga o metabolismo do hospedeiro e *pica o cromossomo bacteriano em fragmentos*. Em seguida, monta novas cápsulas e empacota, em cada uma, uma cópia do genoma viral.

O acidente está no empacotamento. A maquinaria que enche a cápsula reconhece sequências do genoma viral, mas o reconhecimento não é perfeito, e ocasionalmente ela fecha a cápsula sobre um fragmento do cromossomo *bacteriano* picado que estava no citoplasma. A partícula resultante é um fago em tudo — capaz de aderir e injetar — exceto no conteúdo: ela injeta DNA da bactéria anterior. Esse é o mecanismo da transdução generalizada, e "generalizada" descreve o fato de que qualquer trecho do cromossomo pode ser empacotado, porque o corte que gerou os fragmentos foi indiscriminado.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-34.png",
  largura: 64%,
  legenda: [O ciclo do fago transdutor. Repare no passo em azul: o material empacotado não é viral, é o fragmento do cromossomo da bactéria destruída — e é ele que será injetado na próxima célula infectada.])

A transdução especializada nasce de outro ciclo. Muitos fagos, ao entrar, não partem para a lise: integram o próprio genoma num sítio determinado do cromossomo bacteriano e ficam ali silenciosos, replicando-se passivamente junto com o hospedeiro por gerações. Nesse estado o vírus se chama #termo-nota[profago][genoma viral integrado ao cromossomo bacteriano, replicado passivamente com ele e sem produzir partículas]. Diante de um estresse — dano ao DNA, escassez —, o profago se excisa e retoma o ciclo lítico. A excisão às vezes é imprecisa e leva junto um pedaço da sequência bacteriana vizinha ao sítio de integração. Daí "especializada": não é uma transdução mais eficiente, é uma transdução que só transfere os genes que ficavam *ao lado* do ponto onde aquele fago se integra.

O estado de profago tem uma consequência que vai muito além da genética, e ela se chama conversão lisogênica: a bactéria passa a expressar genes do vírus integrado e adquire, com isso, propriedades novas. _Corynebacterium diphtheriae_ é habitante comum da orofaringe e, sozinha, não causa difteria. O gene da toxina diftérica não é dela — vem no genoma de um bacteriófago. Apenas a linhagem que foi infectada e carrega o profago produz a toxina, e apenas essa causa a doença. O que separa o comensal do patógeno é a presença de um vírus integrado.

#atencao-box("Antibiótico em infecção por Escherichia coli produtora de toxina Shiga",
[A toxina Shiga segue exatamente a mesma lógica da difteria: o gene vem num profago integrado ao cromossomo da _E. coli_ êntero-hemorrágica. Enquanto o profago está quieto, a produção de toxina é baixa.

O elo com a PARTE II é o que torna isso perigoso. O sinal que faz o profago se excisar e entrar em ciclo lítico é o *mesmo* programa de emergência disparado por dano ao DNA. Uma quinolona, administrada a esse paciente, gera dano, dispara o programa, induz a excisão em massa do profago — e a lise das bactérias despeja de uma vez toda a toxina acumulada na luz intestinal.

*A consequência é clínica e grave:* em diarreia sanguinolenta com suspeita desse agente, o antibiótico aumenta o risco de síndrome hemolítico-urêmica — anemia hemolítica, plaquetopenia e insuficiência renal aguda, sobretudo em crianças. É um dos poucos quadros infecciosos em que tratar com antibiótico piora o desfecho, e o mecanismo que explica isso é a indução do profago.])

#subtopico("3.4 Transposons, integrons e ilhas de patogenicidade")

As três rotas anteriores movem DNA *entre* células. Falta o movimento que ocorre *dentro* de uma célula, entre moléculas — e ele é o que transforma uma aquisição temporária em patrimônio permanente.

A descoberta foi de Barbara McClintock, nos anos 1940, com milho. Ela observava espigas cujos grãos apresentavam padrões de cor instáveis, que reapareciam de forma imprevisível entre gerações. O padrão não se explicava por mutação, porque era reversível demais, nem por recombinação, porque o pé de milho não estava cruzando com nada. A proposta dela — que existem elementos genéticos que mudam de posição no genoma — contrariava o princípio de que cada gene ocupa um lugar fixo no cromossomo, e ficou décadas sem explicação molecular. Ela veio nos anos 1960, com bactérias, cujo genoma é pequeno o bastante para ser dissecado.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-39.png",
  largura: 60%,
  legenda: [Dois transposons reais. Em cada um, o gene de resistência ocupa o centro e as sequências de inserção o ladeiam em orientação oposta — as setas curvas embaixo marcam as repetições invertidas que a transposase reconhece nas duas pontas.])

A estrutura revelada é simples e explica tudo o que o elemento faz. Um transposon é um segmento de DNA que carrega, no centro, um ou mais genes — tipicamente resistência a antibiótico — e, nas duas extremidades, sequências curtas idênticas em orientação oposta, as repetições invertidas. Entre os genes centrais está o gene da #termo-nota[transposase][enzima codificada pelo próprio transposon, que reconhece as repetições invertidas das pontas e catalisa o corte e a inserção do elemento], que reconhece as duas pontas, aproxima-as formando uma alça, corta o elemento fora do lugar e o insere em outro sítio. As repetições invertidas são, portanto, os *sítios de reconhecimento*, não o gene da enzima — confundir as duas coisas apaga o mecanismo.

O destino do salto pode ser outro ponto do mesmo plasmídeo, um segundo plasmídeo da mesma célula, ou o cromossomo. E em muitos casos o elemento não sai de fato do lugar de origem: ele é copiado, deixando a versão original onde estava e inserindo uma cópia no destino — o que multiplica o número de cópias do gene de resistência dentro da célula.

#table(
  columns: (auto, 1fr, auto),
  inset: 7pt,
  align: (left, left, left),
  stroke: 0.5pt + gray-border,
  table.header([*Transposon*], [*Resistência que carrega*], [*Comprimento (pb)*]),
  [Tn1 / Tn2 / Tn3], [ampicilina], [\~5.000],
  [Tn4], [ampicilina, estreptomicina, sulfonamida], [20.500],
  [Tn5], [canamicina], [5.400],
  [Tn9], [cloranfenicol], [2.638],
  [Tn10], [tetraciclina], [9.300],
  [Tn1681], [enterotoxina termoestável], [2.088],
)

Duas linhas dessa tabela merecem leitura. O Tn4 mostra que um único elemento pode carregar três resistências entre as suas pontas e movê-las como bloco. E o Tn1681 mostra que o conteúdo não é só resistência: fatores de virulência viajam pelo mesmo mecanismo.

O arranjo que empilha resistências não é, porém, o transposon sozinho. Existe uma plataforma dedicada a isso, o integron — e vale distingui-la, porque o integron *não se move por conta própria*. Ele é um sítio de recombinação acompanhado de uma enzima integrase e de um único promotor. A integrase captura pequenas unidades circulares que contêm um gene de resistência sem promotor próprio, os cassetes gênicos, e as insere em fila nesse sítio; o promotor único transcreve todos de uma vez. O resultado é um arranjo que cresce por acréscimo, cassete a cassete. O integron costuma estar *dentro* de um transposon, que por sua vez está num plasmídeo conjugativo — e é essa combinação em três níveis que produz os isolados hospitalares resistentes a seis ou sete classes simultaneamente.

#figura-nebli("/figuras/micro-06-genetica-bacteriana/slide-41.png",
  largura: 60%,
  legenda: [Um plasmídeo R real. O segmento de determinantes de resistência é um mosaico de transposons encaixados uns nos outros, cada um delimitado por suas sequências de inserção; o segmento de transferência ao lado é o que faz o conjunto conjugativo.])

A consequência final do salto é a mais importante. Um gene que está no plasmídeo pode se perder numa divisão, como a PARTE I mostrou. O mesmo gene, transposto para o cromossomo, passa a ser segregado ativamente com ele e se torna permanente. E como um plasmídeo pode ter vindo de outra espécie, o que o transposon fixa no cromossomo é DNA estrangeiro: forma-se uma região chamada ilha de patogenicidade, que reúne genes de toxina, adesina e invasina que a espécie não tinha.

Essa origem estrangeira deixa uma assinatura detectável, e aqui a genética vira ferramenta diagnóstica. Cada espécie tem uma proporção característica de guanina e citosina no genoma. Uma região adquirida de outra espécie carrega a proporção *da espécie de origem*, e destoa da vizinhança. Ao sequenciar o genoma de um isolado, o desvio local dessa proporção denuncia o trecho importado — e o mesmo sequenciamento, comparado a bancos de dados, identifica a espécie por genes conservados e localiza diretamente os genes de resistência presentes, antes mesmo de o antibiograma ficar pronto.

#subtopico("3.5 CRISPR: a memória imunológica da bactéria")

Todas as rotas da PARTE III descrevem entrada de DNA estrangeiro, e nenhuma delas seria sustentável se a bactéria não tivesse como recusar parte do que chega. As enzimas de restrição do subtópico 3.1 são a defesa genérica: cortam qualquer DNA sem o padrão de metilação da casa. O que faltava era uma defesa *específica*, capaz de reconhecer um invasor pela sequência, e ela foi encontrada num arranjo que estava à vista nos genomas sequenciados sem que ninguém soubesse ler.

O nome do sistema descreve literalmente o que se vê no genoma: #sigla("CRISPR", [do inglês _clustered regularly interspaced short palindromic repeats_ — repetições palindrômicas curtas, agrupadas e regularmente intercaladas]). O arranjo consiste em repetições curtas e palindrômicas, agrupadas e separadas por espaçadores de tamanho semelhante. A observação que destravou tudo foi a de que as sequências dos espaçadores correspondem a trechos de genomas de bacteriófagos e plasmídeos. O arranjo é um arquivo: cada espaçador é o registro de uma infecção sobrevivida.

O sistema funciona em três tempos, e vale nomeá-los porque cada um responde a uma pergunta diferente. Na *adaptação*, a bactéria que sobrevive a uma infecção recorta um fragmento do genoma do invasor e o insere como novo espaçador no arranjo — e como o arranjo está no cromossomo, esse registro passa a todos os descendentes. Na *expressão*, o arranjo é transcrito e processado em pequenos RNAs, cada um contendo um espaçador; cada RNA desses se acopla a uma nuclease da família Cas. Na *interferência*, o complexo varre o DNA que entra na célula e, ao encontrar sequência complementar ao espaçador que carrega, corta a dupla-fita. O invasor é destruído antes de se replicar.

Um refinamento resolve a objeção evidente. Como o próprio arranjo CRISPR contém as sequências do invasor, o complexo deveria cortar o cromossomo da própria bactéria. O que impede é um motivo de dois ou três nucleotídeos que precisa estar imediatamente adjacente ao alvo para autorizar o corte: ele existe no genoma do fago e não existe no arranjo. Reconhecimento sem esse motivo não dispara a clivagem, e a autoimunidade não acontece.

Duas consequências fecham a PARTE. A primeira é ecológica e diz respeito diretamente ao tema desta aula: um sistema CRISPR ativo corta plasmídeos conjugativos tanto quanto corta fagos, e funciona como freio à aquisição horizontal de genes — inclusive genes de resistência. Linhagens que perdem o sistema tendem a acumular plasmídeos com mais facilidade. A segunda é tecnológica: como o alvo do corte é determinado por um RNA guia curto, trocar esse RNA é trocar o endereço. Foi essa programabilidade que transformou um mecanismo de defesa bacteriana na ferramenta de edição genômica em uso hoje em bactérias, leveduras, plantas e células humanas.

#conclusao-box[
O princípio que atravessa as três PARTES é a tensão anunciada na abertura: fidelidade suficiente para preservar a espécie, infidelidade suficiente para produzir variantes — e apenas dois mecanismos para gerar essas variantes, mutação e recombinação.

O mecanismo nuclear é que os dois caminhos convergem para o mesmo lugar. Na mutação, a variação nasce da própria química da molécula: a base tautomerizada engana a polimerase, o agente genotóxico deforma a fita, e quando o dano supera a capacidade dos sistemas fiéis a célula troca fidelidade por sobrevivência e sai mutada. Na recombinação, a variação chega pronta de fora — DNA nu do meio, uma fita entregue por contato, um fragmento embalado numa cápsula viral — e, uma vez dentro, transposons e integrons a movem entre plasmídeo e cromossomo até fixá-la. A primeira rota produz o gene novo; a segunda o distribui.

Clinicamente essas duas rotas têm assinaturas distintas e reconhecíveis. Resistência que aparece durante o tratamento, em uma classe só, com alteração no alvo da droga — mutação em girase diante da quinolona — é a rota da PARTE II, e é a rota que o próprio antibiótico acelera ao disparar a resposta ao dano. Resistência que aparece de uma vez, a várias classes não relacionadas, numa bactéria sem exposição prévia, é a rota da PARTE III: um plasmídeo conjugativo trazendo um transposon que carrega um integron cheio de cassetes. Ler um antibiograma é, no fundo, decidir entre essas duas histórias.

O próximo passo é justamente aquele em que esses genes deixam de ser sequência e viram doença: os produtos que a bactéria expressa a partir do que adquiriu — adesinas, invasinas, toxinas — e o modo como eles determinam se um encontro com o hospedeiro termina em colonização silenciosa ou em infecção.
]
