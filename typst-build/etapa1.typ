#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Uma bactéria isolada não causa doença, não turva um caldo, não forma colônia e não aparece em exame nenhum. O que causa doença, turva o caldo e forma a colônia é uma *população* — e toda esta aula é, no fundo, o estudo de uma única operação repetida: uma célula que vira duas, e depois quatro, e depois oito. Tudo o mais que vem a seguir são condições impostas a essa operação. Nutriente é o que a duplicação consome; pH, temperatura e oxigênio são as faixas em que ela ainda acontece; metabolismo é como a célula paga por ela; meio de cultura é o ambiente que o laboratório fabrica para que ela aconteça onde possamos vê-la.

Guarde essa ordem, porque ela organiza as três PARTES. A PARTE I trata da duplicação em si: como a célula se divide, quanto tempo isso leva, que conta descreve o resultado, por que essa conta sempre deixa de valer em algum momento, e como se acompanha uma cultura ao longo do tempo. A PARTE II percorre as condições — o que a bactéria precisa receber pronto e as faixas de acidez, temperatura e oxigênio dentro das quais ela ainda cresce. A PARTE III mostra como a célula financia tudo isso, e por que o *modo* como ela financia deixa marcas químicas no meio ao redor — marcas que o laboratório aprendeu a traduzir em cor, e que são a base de quase todo meio de cultura usado no diagnóstico.

Uma advertência vale desde já: o número de bactérias cresce por multiplicação, não por soma, e a intuição humana é péssima com multiplicação repetida. Boa parte dos erros deste assunto vem de confiar na intuição num terreno em que ela não funciona.
]

#parte-title("PARTE I — A aritmética de uma população que dobra", primeira: true)

#subtopico("1.1 Divisão binária: duplicar tudo antes de partir em dois")

A bactéria se multiplica por *divisão binária*: uma célula origina duas células equivalentes, cada uma com uma cópia completa do material genético e aproximadamente metade do citoplasma. Equivalentes é a palavra que carrega o conceito. Não há célula-mãe que permanece e célula-filha que sai, como no brotamento de uma levedura; há duas células do mesmo tamanho, com o mesmo conteúdo, e nenhuma das duas é mais antiga que a outra. Uma consequência prática disso vem já na próxima página: se cada célula gera duas, a população multiplica-se por dois a cada rodada, e é daí que sai toda a aritmética do crescimento bacteriano.

Antes de qualquer estrangulamento no meio da célula, porém, é preciso ter o que dividir. A célula passa a maior parte do intervalo entre uma divisão e a seguinte fabricando material: duplica o #sigla("DNA", [ácido desoxirribonucleico — a molécula que guarda a informação genética]), sintetiza proteína, expande a membrana, alonga a parede e acumula polissacarídeo. O cromossomo circular é copiado a partir de um único ponto de origem, em duas frentes que caminham em sentidos opostos, e as duas cópias vão sendo puxadas para polos opostos da célula à medida que se formam. Só quando esse trabalho está adiantado é que a maquinaria de divisão entra em cena.

E aqui vale um detalhe que raramente é dito e que muda a imagem mental do processo. A divisão não acontece por ruptura: acontece por *construção*. Uma proteína chamada #termo-nota[FtsZ][proteína bacteriana aparentada à tubulina do fuso mitótico; polimeriza num anel que define o plano de divisão] polimeriza num anel logo abaixo da membrana, exatamente no meio da célula, e esse anel funciona como andaime — ele recruta para ali as enzimas que sintetizam parede nova. O que se forma no meio da célula é uma parede nova, o septo, erguida de dentro para fora; a constrição que vemos ao microscópio é o resultado dessa construção avançando, e a separação final se dá pela clivagem controlada do septo em duas paredes. *A divisão bacteriana é uma obra de alvenaria, não um corte.* Isso explica, de passagem, por que um agente que impede a síntese de parede é devastador justamente na célula que está se dividindo, e quase inócuo na que está parada.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-04.png",
  largura: 52%,
  legenda: [Divisão binária e o intervalo que a define. A célula duplica ácidos nucleicos, proteínas, lipídeos e polissacarídeos antes de se partir em duas metades equivalentes. O intervalo entre a existência de uma célula e a existência de duas é o tempo de geração — o relógio que governa toda a aritmética das próximas páginas.])

O intervalo entre uma divisão e a seguinte é o #termo-nota[tempo de geração][intervalo necessário para que uma população bacteriana dobre de número; também chamado tempo de duplicação]. Para a *Escherichia coli* em meio rico e a 37 °C, ele é de cerca de 20 minutos; para o agente da tuberculose, de 18 a 24 horas — uma diferença de aproximadamente três ordens de grandeza que, como se verá, é a explicação inteira de por que certas culturas ficam prontas na manhã seguinte e outras levam semanas.

O ponto fino é que o tempo de geração *não é uma propriedade fixa da espécie*. É a velocidade daquela bactéria naquele meio, naquela temperatura e naquele pH. A mesma *E. coli* que dobra em 20 minutos num caldo que lhe entrega aminoácidos prontos leva bem mais tempo num meio que a obriga a sintetizar cada aminoácido a partir de sais e glicose — porque a fábrica precisa produzir muito mais antes de poder se partir ao meio. Sempre que aparecer um número de tempo de geração, ele vem junto com a condição em que foi medido, mesmo quando essa condição fica subentendida.

Há ainda um limite físico interessante por baixo desse número. Copiar o cromossomo inteiro de *E. coli* leva perto de 40 minutos, e mesmo assim ela consegue dobrar em 20 — o que parece impossível. A saída da célula é engenhosa: em crescimento muito rápido, ela inicia uma nova rodada de replicação antes de terminar a anterior, de modo que várias cópias parciais do cromossomo caminham ao mesmo tempo, e cada célula-filha já nasce com a replicação em andamento. *O tempo de geração e o tempo de replicação do cromossomo são grandezas diferentes*, e confundi-las é o que faz o limite parecer paradoxal.

#mini-resumo[Dividir exige duplicar tudo antes; o anel de FtsZ marca o plano e ergue uma parede nova no meio da célula. O intervalo entre uma célula e duas é o tempo de geração — dependente do meio, e não uma constante da espécie.]

#subtopico("1.2 A conta que descreve o crescimento")

Toda a leitura da curva de crescimento, que vem daqui a duas páginas, depende de uma fórmula de uma linha. Vale construí-la devagar, porque construída ela nunca mais precisa ser decorada.

Comece pelo caso mais simples: uma única célula, num meio em que ela se divide a cada 20 minutos. Depois de 20 minutos há duas. Depois de 40, cada uma dessas duas se dividiu, e há quatro. Depois de 60, oito. Não estamos somando duas células a cada rodada — estamos *multiplicando por dois* a população inteira. Uma multiplicação por dois repetida três vezes é o mesmo que multiplicar por dois elevado a três, e daí sai a fórmula:

$ X = x_0 dot 2^n $

Cada símbolo carrega um gesto concreto. *X* é o número de células no fim do período considerado. *x₀* é o inóculo, isto é, o número de células com que a cultura começou — quase nunca uma só, e trocar o valor real por 1 subestima o resultado exatamente no mesmo fator. *2* é a base, e ela é dois porque cada célula gera duas: a base não é convenção de cálculo, é o modo de divisão escrito em forma de número. E *n* é o número de gerações decorridas — não o tempo. Este é o ponto em que quase todo erro de conta acontece.

Obter n é uma divisão simples: o tempo total dividido pelo tempo de geração. Em uma hora de cultivo de *E. coli*, com 20 minutos por geração, cabem 60 ÷ 20 = 3 gerações. Substituindo: X = 1 × 2³ = 8 células. Em duas horas, cabem 6 gerações, e X = 2⁶ = 64. Note o que aconteceu: o tempo apenas dobrou, e a população multiplicou-se por oito.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-05.png",
  largura: 58%,
  legenda: [A árvore da duplicação e a fórmula que a resume. A cada intervalo de 20 minutos, cada célula presente origina duas — de 1 para 2, de 2 para 4, de 4 para 8. Repare que a fórmula não descreve células individuais, e sim quantas vezes a população inteira foi multiplicada por dois.])

Estenda o mesmo raciocínio e o resultado deixa de caber na intuição. Em 24 horas há 72 gerações, e 2⁷² é aproximadamente 4,7 × 10²¹ células. Lido em palavras: uma única célula, se nada a interrompesse, produziria em um dia mais bactérias do que existem estrelas em bilhões de galáxias. Em 48 horas, com 144 gerações, o número passa de 10⁴³ — e a massa correspondente ultrapassaria a massa do planeta. *O absurdo do resultado é a informação mais útil da conta*, e é por ele que a próxima seção começa.

Falta um último passo, o que transforma essa fórmula em gráfico. Aplicando logaritmo aos dois lados, a multiplicação vira soma: o logaritmo de X é o logaritmo de x₀ mais n vezes o logaritmo de 2. Como n é o tempo dividido por uma constante, o logaritmo do número de células passa a ser uma função *linear* do tempo. É por isso que o eixo vertical da curva de crescimento é logarítmico e a fase de multiplicação intensa aparece como uma reta: a reta não significa crescimento linear, significa crescimento exponencial visto numa escala que o endireita. E a inclinação dessa reta não mede quantas bactérias há — mede a velocidade de duplicação. Duas culturas partindo do mesmo inóculo desenham retas de inclinações diferentes quando as espécies têm tempos de geração diferentes, e a mais inclinada é sempre a de menor tempo de geração.

#mini-resumo[Em uma frase: X = x₀ · 2ⁿ, com n = tempo ÷ tempo de geração — e como o logaritmo transforma multiplicação em soma, a fase exponencial aparece como reta cuja inclinação é a velocidade de duplicação, não o número de células.]

#subtopico("1.3 Onde a conta deixa de valer")

Uma cultura de 24 horas na bancada não tem 10²¹ células: tem entre 10⁸ e 10⁹ por mililitro, treze ordens de grandeza abaixo do previsto. E uma colônia isolada, por maior que pareça, não passa de cerca de 10⁸ células. Levada ao caso concreto, a discrepância fica gritante — semeada uma única célula em meio sólido e descontadas duas horas de adaptação, restam 22 horas de multiplicação intensa, ou 66 gerações, o que dá *matematicamente* 6,86 × 10¹⁰ células por colônia contra as 10⁸ observadas. A distância entre o cálculo e a placa não é erro aritmético: é o fim da fase em que a fórmula descreve a realidade.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-08.png",
  largura: 52%,
  legenda: [O teto real. À esquerda, a conta levada a 24 e 48 horas, com resultados fisicamente impossíveis. À direita, os dois tetos observados: cerca de 10⁸ células por colônia em meio sólido e cerca de 10⁸ células por mililitro em meio líquido. Entre a conta e a placa está tudo o que esta seção explica.])

Três mecanismos interrompem a multiplicação, e vale separá-los porque atuam em situações diferentes. O primeiro é o *esgotamento de nutriente*: cada duplicação consome carbono, nitrogênio, fósforo e energia, e o meio tem uma quantidade finita de cada um. O segundo é o *acúmulo de produto do metabolismo* — ácidos orgânicos, álcoois, amônia — que vai deslocando o pH e tornando o próprio meio inóspito. O terceiro é específico da colônia sobre meio sólido: à medida que o monte de células cresce, o nutriente precisa *difundir* de fora para dentro e o produto precisa difundir de dentro para fora, e a difusão simplesmente não vence a distância. As células do centro de uma colônia madura estão, para todos os efeitos, em jejum.

Há ainda um quarto mecanismo, e ele é de outra natureza — não é escassez, é informação. Bactérias secretam continuamente pequenas moléculas sinalizadoras que se difundem pelo meio. Com poucas células, o sinal se dilui e nada acontece; conforme a densidade populacional sobe, a concentração do sinal sobe junto, e ao ultrapassar um limiar ele volta a ser captado pelas próprias células e altera o programa de expressão gênica do grupo inteiro. É o que se chama #termo-nota[percepção de quórum][leitura da densidade populacional pelo acúmulo de um sinal difusível que, acima de um limiar, muda o programa gênico de todo o grupo]. Uma população passa a se comportar como coletivo: liga genes de formação de biofilme, muda a produção de fatores de virulência e reduz o investimento em divisão. *A população não para só porque acabou a comida — ela também sabe que está cheia*, e essa é uma das descobertas que mais mudaram a microbiologia nas últimas décadas.

À primeira vista, é tentador tratar o resultado da fórmula como a previsão do tamanho da cultura, e depois concluir que a conta está errada quando a placa não confirma.

#confusao-prevista(
  titulo: "A fórmula não está errada — ela só descreve um trecho",
  aluno_acha: [que X = x₀ · 2ⁿ prevê quantas bactérias haverá numa cultura após um tempo qualquer, e que o resultado astronômico é sinal de erro de cálculo],
  mecanismo: [a fórmula descreve exclusivamente a fase de multiplicação sem restrição. Fora dela, três limites entram em cena — nutriente que acaba, produto que se acumula e, na colônia sólida, nutriente que não difunde até o centro — e a população trava perto de 10⁸. Usar a fórmula é correto; usá-la além do trecho em que vale é o erro.],
)

#subtopico("1.4 As quatro fases da curva de crescimento")

Se acompanharmos uma cultura desde a semeadura até a morte da população, e desenharmos o logaritmo do número de bactérias contra o tempo, aparece sempre o mesmo perfil de quatro trechos. Cada trecho é uma situação fisiológica distinta, e vale percorrê-los um a um.

O primeiro é a *fase lag*, ou fase de adaptação. O número de células não sobe — e é justamente por isso que ela é mal compreendida. Não há divisão, mas a atividade metabólica nesse período é a mais intensa de todo o ciclo. A célula recém-transferida encontra um meio diferente daquele de onde veio e precisa se reequipar: fabrica os transportadores capazes de captar a nova fonte de carbono, induz as enzimas da via que aquela fonte exige, repõe reservas e, sobretudo, produz ribossomo — sem parque ribossomal suficiente, nenhuma célula cresce rápido depois. Daí decorre a regra que explica a duração variável dessa fase: *a lag é tão longa quanto grande for a diferença entre o meio antigo e o novo*. Um inóculo transferido em plena multiplicação de um caldo para outro caldo idêntico praticamente não tem lag; um inóculo vindo de uma cultura velha, ou obrigado a usar um açúcar que não usava, tem uma lag longa. E é essa fase, mais do que qualquer outra, que responde por que o resultado de uma cultura não sai no mesmo dia da coleta.

O segundo trecho é a *fase log*, exponencial ou logarítmica. Aqui a célula está em crescimento equilibrado: todos os componentes celulares aumentam na mesma proporção, o tempo de geração é constante, e é exclusivamente neste trecho que X = x₀ · 2ⁿ descreve a população. Na escala logarítmica ela aparece como reta, e a inclinação dessa reta é a assinatura da espécie naquele meio. Duas observações clínicas nascem daqui. A primeira é que a população em fase log é fisiologicamente a mais uniforme, e por isso é dela que se parte para qualquer teste laboratorial padronizado. A segunda é mais importante: é também a fase de *maior vulnerabilidade*. Um agente que bloqueia a síntese de parede precisa de parede sendo sintetizada para causar dano; um agente que trava o ribossomo precisa de proteína sendo fabricada. Multiplicação intensa é exatamente a condição que oferece esses alvos.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-09.png",
  largura: 72%,
  legenda: [As quatro fases, com o eixo vertical em escala logarítmica. Em A, a fase lag: nenhuma divisão, metabolismo máximo, maquinaria sendo construída. Em B, a fase log, único trecho em que a fórmula da multiplicação descreve a população — e onde a inclinação revela o tempo de geração. Em C, a estacionária: o que entra por divisão iguala o que sai por perda de viabilidade. Em D, o declínio, quando a morte passa a exceder a divisão.])

O terceiro trecho é a *fase estacionária*, e é o mais mal lido de todos. O número total de células para de subir, e a leitura apressada conclui que a divisão cessou. Pode ocorrer assim — células viáveis que simplesmente não se dividem —, mas a situação mais comum é dinâmica: a divisão continua, e o número de células novas iguala o número de células que perdem viabilidade. *O platô é equilíbrio, não paralisia.* O que muda de fato, nessa transição, é o programa de expressão gênica. Diante de nutriente escasso, a célula desliga a produção maciça de ribossomo — que só faz sentido para quem vai crescer — e liga um conjunto de genes de sobrevivência: espessamento da parede, acúmulo de reservas, reparo de DNA, resistência a estresse osmótico e oxidativo. O sinal interno que faz essa chave girar é um nucleotídeo alarmônico acumulado quando falta aminoácido, que redireciona a #sigla("RNA", [ácido ribonucleico — cópia de trabalho da informação genética]) polimerase dos genes de crescimento para os genes de sobrevivência. A célula da estacionária é uma célula diferente da célula da fase log, com a mesma genética e outro fenótipo.

O quarto trecho é a *fase de declínio*, ou de morte. A taxa de perda de viabilidade supera a de divisão e a população cai — em geral também de forma exponencial, o que na escala logarítmica desenha uma reta descendente. Declínio não significa que todas as células morreram: significa que a soma está negativa. Subpopulações pequenas podem persistir por muito tempo em estado de atividade mínima, e essas células têm nome e importância própria.

#atencao-box("Célula quiescente não é célula resistente — e o desfecho é o mesmo",
[A célula da fase estacionária, com metabolismo reduzido, sobrevive a concentrações de antimicrobiano que matam a mesma bactéria em fase log. Isso não é resistência: não há gene novo, não há enzima que destrua a droga, e a descendência dessa célula volta a ser sensível quando cresce. É *tolerância* — a droga não encontra o processo que precisa atacar. A consequência prática é direta: infecção associada a biofilme, a abscesso ou a material implantado, onde grande parte da população está em baixa atividade, responde mal a tratamentos curtos ainda que o teste de sensibilidade indique droga adequada. Quem lê o teste sem considerar o estado fisiológico da população conclui que o agente é sensível e não entende por que o quadro volta.])

Vale confrontar duas curvas reais para fechar a seção, porque a diferença entre elas explica a rotina de dois laboratórios distintos. *E. coli*, com tempo de geração de cerca de 20 minutos, tem lag curta, fase log de inclinação acentuada e entra em estacionária em poucas horas — cresce da noite para o dia. O agente da tuberculose, com tempo de geração de 18 a 24 horas, tem lag prolongada, fase log de inclinação suavíssima e alongada, e uma fase estacionária que pode se estender indefinidamente, com subpopulações de baixíssima atividade. As duas curvas têm exatamente o mesmo formato; o que muda é a escala do eixo do tempo, de horas para semanas. #mini-resumo[O que ficou de pé: as quatro fases não descrevem células individuais e sim a população — lag é construção de maquinaria, log é o único trecho onde a fórmula vale e o de maior vulnerabilidade, estacionária é equilíbrio com troca de programa gênico, declínio é saldo negativo.]

#subtopico("1.5 Como se acompanha uma cultura")

Desenhar a curva das páginas anteriores exige medir a população repetidamente ao longo do tempo, e essa medida pode ser feita de várias maneiras. Pense em como se avaliaria uma multidão numa praça: dá para contar cabeça por cabeça em fotografia aérea, dá para estimar pela área ocupada, e dá para medir indiretamente pelo lixo produzido. Cada método responde uma pergunta um pouco diferente — e no laboratório essa diferença é a informação mais útil.

O caminho mais direto é contar as células ao microscópio, em câmara de volume conhecido: dá o número *total* e não depende de a bactéria crescer, mas é trabalhoso, exige carga alta e — o ponto decisivo — não distingue célula viva de morta, porque as duas têm a mesma aparência.

Na rotina laboratorial, o caminho é outro: a *turvação*. Uma suspensão de bactérias espalha a luz que a atravessa, e quanto mais partículas em suspensão, menos luz chega do outro lado. Um espectrofotômetro mede exatamente isso, em geral por volta de 600 a 660 nanômetros, e o valor obtido acompanha a massa de células em suspensão. O método é rápido, não destrói a amostra e permite medir a mesma cultura de meia em meia hora — foi assim que se levantaram as tabelas de absorbância ao longo do tempo que geram a curva. O que ele mede, porém, é *matéria que espalha luz*: célula viva e célula morta contribuem igualmente, e restos celulares também.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-11.png",
  largura: 54%,
  legenda: [Acompanhamento por turvação. O tubo com a cultura, o espectrofotômetro, o princípio óptico — fonte de luz, amostra, detector — e a tabela de absorbância a 660 nm ao longo dos minutos de incubação. Cada linha da tabela é um ponto da curva de crescimento; a coluna que sobe mais rápido pertence ao meio que sustenta o menor tempo de geração.])

Já a contagem em placa é o único que responde "quantas células vivas". Dilui-se a amostra em série, semeia-se um volume conhecido em meio sólido, incuba-se e contam-se as colônias formadas. Cada colônia veio de uma unidade capaz de se multiplicar, e por isso o resultado se expressa em #termo-nota[unidade formadora de colônia][a partícula que originou uma colônia; pode ser uma célula isolada ou um agregado de várias células que cresceram juntas] por mililitro, e não em células por mililitro. A distinção não é preciosismo: bactérias que crescem em cachos ou em cadeias originam uma única colônia a partir de várias células, e nesses casos o método subestima sistematicamente a população.

Existe ainda a via indireta — acompanhar o *consumo de oxigênio* da cultura ou a *produção de metabólito*, tipicamente #sigla("CO₂", [dióxido de carbono — produto final da oxidação completa de compostos de carbono]). Parece o caminho mais frouxo dos quatro e é, na prática, o mais sensível para detectar crescimento incipiente: uma população pequena demais para turvar o caldo já libera produto mensurável.

O detalhe que amarra a seção é o que acontece quando se comparam os métodos ao longo de toda a curva. Enquanto a cultura só cresce, os três sobem juntos e parecem equivalentes. A partir da fase estacionária eles se separam: a turvação se mantém ou até sobe um pouco, porque a matéria continua lá, enquanto a contagem de viáveis despenca. *A divergência entre os dois métodos é a medida da morte celular* — e um caldo turvo não significa, por si só, população viva.

#clinica-box("Hemocultura: por que a máquina avisa antes de o frasco turvar",
[Um frasco de hemocultura contém, no início, pouquíssimas bactérias — em bacteriemia de adulto a carga pode ser de uma a dez unidades formadoras de colônia por mililitro de sangue. Nessa densidade não há turvação, não há sedimento, não há nada visível, e esperar que apareça custaria dias. Os sistemas automatizados contornam isso medindo a via indireta: no fundo do frasco existe um sensor cuja cor ou fluorescência responde à concentração de CO₂, e o metabolismo daquelas poucas células já produz CO₂ suficiente para ser detectado. O aparelho lê cada frasco a cada poucos minutos e dispara o alerta quando a curva de CO₂ inflete — em geral entre 8 e 24 horas para agentes de crescimento rápido, muito antes de qualquer sinal visível. O tempo até a positivação carrega informação própria: positivação muito precoce sugere carga alta, o que se associa a foco endovascular. No outro extremo, frasco de agente lento pode levar semanas — e é a hipótese clínica que diz por quanto tempo incubar antes de liberar o resultado como negativo.])

#parte-title("PARTE II — O que a bactéria consome e as condições que ela tolera")

#subtopico("2.1 Macronutrientes: a lista de compras da duplicação")

Duplicar uma célula significa fabricar uma segunda cópia de tudo o que ela é, e tudo o que ela é vem de átomos que precisam entrar de fora. É por isso que a discussão sobre nutrição bacteriana não é acessória à discussão sobre crescimento: é a mesma discussão, olhada pelo lado do insumo. Um meio de cultura, no fundo, é uma lista de compras.

Duas perguntas independentes organizam essa lista, e confundi-las é um erro comum. A primeira é *de onde vem a energia*; a segunda é *de onde vem o carbono*. Há bactérias que retiram energia da oxidação de compostos orgânicos, outras que a retiram da oxidação de compostos inorgânicos — enxofre, ferro, amônia — e outras que a captam da luz. Quanto ao carbono, a divisão é mais limpa: quem parte de moléculas orgânicas prontas, como açúcares e proteínas, é *heterotrófico*; quem constrói tudo a partir do CO₂ é *autotrófico*. As duas escolhas se combinam livremente, e a combinação que interessa à medicina é uma só — praticamente todas as bactérias de importância clínica tiram energia e carbono de matéria orgânica, porque vivem à custa da matéria orgânica de um hospedeiro.

Depois de carbono, hidrogênio e oxigênio, o elemento que a célula mais consome é o *nitrogênio*, e a razão é aritmética: nitrogênio está em todo aminoácido e em toda base nitrogenada, ou seja, em toda proteína e em todo ácido nucleico. Ele pode entrar como composto orgânico do meio, como íon inorgânico simples — amônio, nitrito, nitrato — ou, em poucas espécies do ambiente, diretamente como N₂ atmosférico, num processo caro em energia. O detalhe que importa é que a forma efetivamente incorporada ao esqueleto de carbono é sempre o amônio: nitrito e nitrato precisam ser reduzidos antes, e essa redução tem custo. Fósforo e enxofre completam o grupo dos macronutrientes com destinos igualmente concretos — o fósforo compõe o esqueleto do DNA e do RNA, a molécula de #sigla("ATP", [adenosina trifosfato — a moeda energética da célula]) e os fosfolipídeos da membrana; o enxofre entra em dois aminoácidos e nos centros de ferro-enxofre que transportam elétrons nas proteínas respiratórias.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-13.png",
  largura: 58%,
  legenda: [A lista completa, do mais abundante ao mais raro. Acima, os macronutrientes, separados por eixo: fonte de energia, fonte de carbono, de nitrogênio, de fósforo e enxofre. Na faixa amarela, os micronutrientes — sais em quantidade pequena, e traços de metais em quantidade menor ainda. Na faixa rosa, os fatores de crescimento, que a bactéria exige prontos. Abaixo, as duas condições físico-químicas que a PARTE fecha: pH e osmolaridade próxima da solução fisiológica.])

#subtopico("2.2 Micronutrientes e fatores de crescimento: o que a célula não sabe fabricar")

A tabela acima termina com duas linhas que parecem detalhes e não são. A primeira é a dos *micronutrientes* — sódio, potássio, magnésio, ferro, e traços de zinco, manganês, cobalto, molibdênio e selênio. Micro descreve a quantidade, não a importância: um metal em quantidade mínima ocupa o sítio ativo de uma enzima, e sem ele aquela enzima não funciona, por mais que todo o resto esteja disponível. Magnésio estabiliza o ribossomo e a membrana; ferro é o átomo que muda de valência dentro dos citocromos; zinco está em polimerases.

O ferro merece um parágrafo próprio, porque é o único micronutriente que vira campo de batalha. Ferro livre praticamente não existe no corpo humano: ele é mantido sequestrado dentro de proteínas transportadoras e de armazenamento, e essa retenção é uma forma ativa de defesa — negar o metal ao invasor. Bactérias respondem secretando #termo-nota[sideróforos][moléculas secretadas pela bactéria que capturam ferro com afinidade altíssima, arrancando-o das proteínas do hospedeiro], capazes de retirar o ferro dessas proteínas e devolvê-lo à célula por transportadores próprios. *A disputa por ferro é um eixo real da infecção*, e não uma curiosidade bioquímica: um paciente com sobrecarga de ferro tem risco aumentado para certos agentes exatamente porque a defesa por privação foi anulada.

A segunda linha é a dos *fatores de crescimento*, e o nome engana. Não é estimulante de crescimento: é uma molécula essencial que aquela espécie perdeu a capacidade de sintetizar e precisa, portanto, receber pronta — vitaminas, aminoácidos, bases nitrogenadas, fatores presentes no sangue. As vitaminas entram nessa lista porque quase todas são precursoras de coenzimas: o ácido nicotínico dá origem ao transportador de elétrons que a glicólise usa; a riboflavina origina os transportadores flavínicos; a tiamina, a coenzima que descarboxila cetoácidos; o ácido *p*-aminobenzoico é precursor do folato, que a célula usa para transferir unidades de um carbono na síntese de bases e de vários aminoácidos. Essa última linha da tabela tem consequência prática grande: nós não sintetizamos folato, importamos folato pronto da dieta, enquanto a bactéria fabrica o seu a partir do #sigla("PABA", [ácido p-aminobenzoico — precursor da via bacteriana de síntese de folato]). Uma via que só um dos dois possui é exatamente o tipo de alvo que a farmacologia procura, e drogas que imitam o PABA e enganam a enzima bacteriana exploram essa assimetria.

Uma bactéria com muitas exigências desse tipo é chamada #termo-nota[fastidiosa][que exige nutrientes específicos e prontos, não crescendo em meios de rotina] — e exigência nutricional nada diz sobre virulência. O caso das duas placas do material é o melhor exemplo. *Ágar sangue* é meio completo ao qual se acrescentou 5% de sangue desfibrinado quando a base já estava abaixo de 40 °C, temperatura em que o ágar ainda não solidificou mas já não cozinha a hemácia — o sangue entra com as hemácias íntegras. *Ágar chocolate*, apesar do nome, não tem chocolate nenhum: é o mesmo sangue acrescentado com a base ainda quente, o que rompe as hemácias e dá ao meio a cor marrom que batiza a placa. E aqui está o ponto: ao romper a hemácia, o calor libera para o meio dois fatores que estavam trancados dentro dela — o grupo heme e o transportador de elétrons derivado do ácido nicotínico. Espécies incapazes de sintetizar esses dois fatores crescem na placa marrom e não crescem na placa vermelha, sem que nada tenha sido acrescentado. *A diferença entre as duas placas não é o que se pôs nelas, é a temperatura em que se pôs.*

#mini-resumo[Se você só lembrar de uma coisa: fator de crescimento não estimula nada — é o que a bactéria perdeu a capacidade de fabricar e precisa receber pronto, e o calor que rompe a hemácia é o que libera dois desses fatores no ágar chocolate.]

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-14.png",
  largura: 58%,
  legenda: [As duas placas e a mesma matéria-prima. À esquerda, ágar sangue, com hemácias íntegras porque o sangue foi acrescentado abaixo de 40 °C. À direita, ágar chocolate, com hemácias rompidas pelo calor e, por isso, com heme e nucleotídeo de nicotinamida livres no meio. Espécies fastidiosas que não fabricam esses dois fatores só crescem na placa da direita.])

#subtopico("2.3 pH: o que importa é o pH de dentro")

Uma bactéria mergulhada num meio ácido é como uma casa com porão abaixo do nível do rio: o que decide a habitabilidade não é o nível do rio, é a capacidade da bomba de manter o porão seco. O citoplasma da imensa maioria das bactérias é mantido próximo da neutralidade, mesmo quando o meio externo está longe disso — e a manutenção desse gradiente custa energia, na forma de bombeamento contínuo de prótons através da membrana.

É essa capacidade que separa os três grupos. *Acidófilos* crescem em faixas muito abaixo do neutro; *neutrófilos*, entre aproximadamente 5 e 9, com ótimo perto de 7 — e é aqui que se encaixam praticamente todas as bactérias de interesse médico; *alcalófilos*, em faixas acima de 8. Cada grupo tem uma faixa de cerca de três unidades de pH em torno do ótimo, com queda progressiva de velocidade nas bordas. Fora dessa faixa o crescimento cessa; cessar não é o mesmo que morrer, e é justamente essa diferença que a conservação de alimentos por acidificação explora — o meio ácido impede a multiplicação sem necessariamente eliminar quem já está lá.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-16.png",
  largura: 52%,
  legenda: [Velocidade de crescimento contra pH nos três tipos. Repare em duas coisas: cada curva é razoavelmente simétrica em torno do seu ótimo — diferente do que se verá com temperatura — e as faixas se sobrepõem parcialmente, de modo que um mesmo pH pode servir, com velocidades diferentes, a mais de um grupo.])

O caso que interessa clinicamente é o do estômago, cujo pH em jejum fica em torno de 2 — um valor letal para quase toda bactéria ingerida, e uma das barreiras inespecíficas mais eficientes que temos. A exceção mais conhecida resolve o problema não por tolerar o ácido, e sim por *fabricar a própria vizinhança*: a bactéria hidrolisa a ureia presente na mucosa e libera amônia, que neutraliza o ácido no microambiente imediatamente ao redor da célula, permitindo que ela atravesse o muco e alcance a superfície epitelial, onde o pH já é próximo do neutro. O detalhe importa porque a mesma enzima que garante a sobrevivência é também o que a denuncia — testes diagnósticos baseados em detectar essa hidrólise da ureia existem justamente por isso. Um último ponto operacional: o metabolismo bacteriano desloca o pH do meio em que cresce, e por isso todo meio de cultura é tamponado. Sem tampão, a cultura interromperia o próprio crescimento por acidificação bem antes de esgotar o nutriente.

#subtopico("2.4 Temperatura: a subida é química, a queda é ruína")

A curva de crescimento contra temperatura tem uma assimetria gritante, e essa assimetria é a chave para entender tudo o que vem depois. De um lado, a velocidade sobe lentamente conforme a temperatura aumenta, pela razão trivial de que toda reação química acelera com o calor. Do outro lado, passado o ótimo, a velocidade despenca em poucos graus. Não é a mesma física operando em sentido inverso: é *desnaturação de proteína*, um fenômeno abrupto que destrói a função enzimática em vez de apenas desacelerá-la. Daí a consequência que se lê direto no gráfico — a temperatura ótima fica sempre colada ao limite superior, e nunca no meio da faixa.

Os três grupos clássicos distribuem-se ao longo do eixo. *Psicrófilos* crescem melhor em temperaturas baixas, próximas de 15 °C; *mesófilos* ocupam a faixa intermediária, aproximadamente de 20 a 45 °C, com ótimo em torno de 37 °C — não por coincidência, é onde estão as bactérias de interesse médico, adaptadas à temperatura do corpo que habitam; *termófilos* crescem acima de 45 °C, e alguns bem acima disso.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-18.png",
  largura: 54%,
  legenda: [Velocidade de crescimento contra temperatura. Cada curva sobe devagar e cai depressa — a subida é aceleração de reação, a queda é desnaturação de proteína. Abaixo, o termófilo cujo ótimo, entre 70 e 72 °C, forneceu à biologia molecular a enzima que tornou a amplificação de DNA um procedimento de rotina.])

Vale antecipar a leitura errada mais comum antes de nomeá-la: o frio é usado o tempo todo para conservar, e o reflexo é concluir que ele elimina o problema microbiológico.

#confusao-prevista(
  titulo: "Refrigerar retarda; não elimina",
  aluno_acha: [que manter o alimento ou a amostra sob refrigeração interrompe o risco microbiológico, porque "bactéria não cresce no frio"],
  mecanismo: [a temperatura baixa reduz drasticamente a velocidade das reações e, portanto, alonga o tempo de geração — mas não desnatura proteína nem lesa a célula. A população continua viável e, algumas espécies, continuam se multiplicando lentamente a 4 °C. Refrigeração é medida de retardo, e o risco cresce com o tempo de armazenamento, não com a temperatura.],
)

O organismo que fecha a figura merece registro, porque a temperatura ótima dele mudou a medicina inteira. Um termófilo isolado de fonte termal cresce entre 70 e 72 °C, o que exige que suas enzimas permaneçam funcionais nessa faixa. A polimerase de DNA desse organismo resiste a ciclos repetidos de aquecimento a quase 100 °C — e é justamente isso que a #sigla("PCR", [reação em cadeia da polimerase — técnica que produz milhões de cópias de um trecho definido de DNA]) exige, já que cada ciclo começa aquecendo a amostra para separar as fitas. Antes dessa enzima, era preciso repor polimerase a cada ciclo, à mão. *Uma adaptação a fonte termal virou infraestrutura de diagnóstico molecular*, e o caminho até lá passou por alguém estudar a fisiologia de crescimento de uma bactéria sem qualquer interesse clínico aparente.

#subtopico("2.5 Oxigênio: usar sem se envenenar")

O oxigênio fecha esta PARTE porque é a condição que mais separa comportamentos, e porque a explicação dele encadeia diretamente com a PARTE III. A célula que usa O₂ como aceptor final de elétrons extrai muito mais energia de cada molécula de glicose — esse é o benefício. O custo vem do mesmo processo: a redução do oxigênio ao longo da cadeia respiratória gera, como subproduto inevitável, intermediários parcialmente reduzidos, altamente reativos, que oxidam lipídeo de membrana, proteína e DNA da própria célula que os produziu.

Duas enzimas desarmam essa linha, em sequência. A *superóxido-dismutase* pega dois radicais superóxido e os converte em peróxido de hidrogênio e oxigênio molecular; a *catalase* decompõe esse peróxido em água e oxigênio. Uma terceira, a *peroxidase*, faz o mesmo serviço do peróxido por outro caminho, gastando poder redutor para produzir apenas água. As três não são intercambiáveis, e a combinação que cada espécie possui decide a relação dela com o ar.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-19.png",
  largura: 50%,
  legenda: [A linha de desintoxicação. O superóxido gerado pelo metabolismo aeróbio é convertido pela dismutase em peróxido de hidrogênio; o peróxido é então eliminado pela catalase, que o quebra em água e oxigênio, ou pela peroxidase, que o reduz a água consumindo poder redutor. A ausência dessas enzimas — e não a ausência de uma enzima que consuma O₂ — é o que torna o oxigênio letal para os anaeróbios estritos.])

Com esse mecanismo na mão, as cinco classes deixam de ser lista para decorar. O *aeróbio obrigatório* precisa de O₂ como aceptor final e possui o repertório completo de enzimas protetoras. O *anaeróbio facultativo* possui as enzimas e cresce dos dois modos — usa O₂ quando há, rendendo muito mais, e fermenta quando não há. O *anaeróbio estrito* não possui dismutase nem catalase e é morto pelo oxigênio, não por lhe faltar algo que o consuma. O *microaerófilo* precisa de oxigênio, mas em tensão menor que a atmosférica: tem defesa parcial, e a concentração do ar já o lesa. E o *aerotolerante* não usa oxigênio em momento nenhum, obtendo energia sempre por fermentação, mas possui dismutase suficiente para não ser destruído por ele — cresce igual com ar ou sem ar.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-20.png",
  largura: 62%,
  legenda: [Os cinco padrões num meio semissólido, onde o oxigênio difunde de cima para baixo e forma um gradiente. O aeróbio obrigatório concentra-se na superfície; o anaeróbio, no fundo; o facultativo cresce em toda a coluna, mais denso em cima; o microaerófilo forma uma faixa a alguma distância da superfície, na tensão intermediária que tolera; o aerotolerante distribui-se homogeneamente, indiferente ao gradiente.])

A leitura desse tubo é um dos testes mais elegantes da microbiologia, e a lógica dele é a mesma que separa dois gêneros no dia a dia: uma gota de peróxido de hidrogênio sobre a colônia produz borbulhamento imediato quando há catalase, e nada quando não há — é assim que se distinguem, em segundos, dois grupos de cocos Gram-positivos morfologicamente parecidos. *O que se está lendo, nos dois casos, é a mesma coisa: qual parcela da linha de desintoxicação aquela bactéria possui.*

#mini-resumo[Em uma frase: o oxigênio não mata o anaeróbio estrito por lhe faltar uma enzima que o consuma, e sim por lhe faltarem a dismutase e a catalase que neutralizam o superóxido e o peróxido gerados espontaneamente na presença dele.]

#clinica-box("Anaeróbio estrito: a coleta decide o resultado antes do laboratório",
[Infecções por anaeróbios estritos nascem onde a tensão de oxigênio caiu — tecido desvitalizado por trauma ou isquemia, coleção purulenta encapsulada, mordedura profunda, cavidade com necrose. O consumo de O₂ pelo próprio tecido lesado e pela microbiota acompanhante derruba o potencial de oxirredução local até a faixa em que uma célula sem catalase consegue crescer, e é por isso que essas infecções são caracteristicamente polimicrobianas: o aeróbio prepara o terreno para o anaeróbio. A consequência prática é implacável e acontece antes de a amostra chegar ao laboratório. Material colhido em swab exposto ao ar, ou transportado sem meio adequado, chega com o agente morto — e o resultado sai negativo apesar de a infecção existir. Por isso a coleta de sítio suspeito de anaeróbio é feita por aspiração com seringa, com expulsão do ar, ou em meio de transporte específico. Um resultado negativo obtido com coleta inadequada não é informação: é ausência de informação com aparência de informação.])

#parte-title("PARTE III — O metabolismo e o meio que o torna visível")

#subtopico("3.1 Catabolismo e anabolismo: a mesma via serve às duas mãos")

Uma célula que dobra de tamanho a cada vinte minutos tem dois problemas simultâneos: precisa de energia e precisa de peças. O *catabolismo* resolve o primeiro — quebra moléculas complexas em moléculas simples, e essas reações liberam energia, que a célula guarda sobretudo como ATP. O *anabolismo* resolve o segundo — constrói moléculas complexas a partir de simples, e essas reações consomem energia. Não são etapas alternadas de um ciclo: acontecem ao mesmo tempo, acopladas, e o que sai de uma alimenta a outra no mesmo instante.

O que raramente se explica é o quanto essas duas mãos compartilham o mesmo maquinário. A via central que degrada a glicose não é apenas uma linha de produção de ATP: ela é também o entreposto de onde saem quase todos os esqueletos de carbono que a célula usa para construir o resto. Um intermediário de três carbonos é ponto de partida para vários aminoácidos; um derivado de dois carbonos ligado à coenzima A é ponto de partida para os ácidos graxos da membrana; hexoses fosforiladas alimentam a síntese de parede; pentoses fosforiladas alimentam a síntese de nucleotídeo, e portanto de DNA e RNA. *Cada molécula desviada para construção é uma molécula que não vai gerar ATP* — e é essa disputa permanente que faz o metabolismo central ser o eixo da fisiologia bacteriana, e não apenas a sua caldeira.

A diversidade metabólica das bactérias, como grupo, é maior que a de todo o resto dos seres vivos somados, e ela se organiza em poucos eixos: qual a fonte de energia, qual a fonte de carbono, qual o aceptor final de elétrons e que enzimas hidrolíticas o organismo possui. Essa última variável tem consequência clínica direta — a capacidade de hidrolisar compostos diferentes, de produzir enzimas induzíveis, de secretar toxinas e fatores de adesão e invasão são todas expressões do repertório metabólico. E, como se verá em duas páginas, é justamente essa variação que o laboratório converte em identificação.

#subtopico("3.2 Fermentação e respiração: quem decide é o aceptor final")

A diferença entre fermentar e respirar costuma ser resumida em dois números — 2 contra 38 moléculas de ATP por glicose —, e o resumo é verdadeiro e enganoso ao mesmo tempo. É verdadeiro porque a diferença de rendimento existe e é enorme. É enganoso porque sugere que a fermentação existe como uma versão pior da respiração, quando o problema que ela resolve é outro, e mais urgente.

O problema aparece na glicólise. Ao quebrar a glicose até piruvato, a célula retira elétrons do açúcar e os entrega a um transportador, o #sigla("NAD", [nicotinamida adenina dinucleotídeo — transportador de elétrons que alterna entre a forma oxidada, NAD⁺, e a reduzida, NADH]) na forma oxidada, que sai reduzido. O estoque de transportador dentro da célula é pequeno e fixo. Se ninguém devolver esses transportadores à forma oxidada, a glicólise trava em poucos segundos — não por falta de açúcar, mas por falta de aceitador de elétrons. *Todo o resto do metabolismo energético é uma resposta a esse gargalo.*

A respiração resolve entregando os elétrons a uma cadeia de proteínas na membrana, que os passa adiante e usa a energia liberada para bombear prótons para fora. O retorno desses prótons, por um canal específico, é o que move a síntese da maior parte do ATP. No fim da fila, alguém precisa receber os elétrons: quando esse aceptor final é o oxigênio, temos *respiração aeróbia*, com o maior rendimento possível e água como produto; quando é nitrato ou sulfato, temos *respiração anaeróbia*, que ocorre em bactérias e rende menos que a aeróbia, porque esses aceptores puxam elétrons com menos força. A fermentação resolve o mesmo gargalo pelo caminho mais curto e mais pobre: sem cadeia nenhuma, ela entrega os elétrons a um derivado do próprio piruvato, regenerando o transportador oxidado ali mesmo. O único ATP que sobra é o produzido dentro da glicólise, por #termo-nota[fosforilação no nível do substrato][transferência direta de um grupo fosfato de um intermediário da via para o ADP, sem participação da cadeia respiratória].

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-24.png",
  largura: 54%,
  legenda: [As três saídas para a glicose e o que cada uma rende. Na fermentação, o piruvato é o destino e o saldo é de 2 ATP. Na respiração com oxigênio, a oxidação vai até CO₂ e água, e o saldo salta para a casa dos 36 a 38 ATP. Na respiração sem oxigênio, o aceptor final é nitrato ou sulfato, e o rendimento fica entre os dois extremos.])

Fica então clara uma distinção que confunde muita gente: *anaerobiose e fermentação não são sinônimos*. Um anaeróbio pode perfeitamente respirar, desde que disponha de um aceptor final que não seja oxigênio. E um facultativo, colocado no ar, respira; retirado o ar, fermenta — mesma célula, mesmo genoma, duas fisiologias, e um crescimento visivelmente mais rápido na primeira condição.

#mini-resumo[O que ficou de pé: o gargalo que a fermentação resolve é a regeneração do transportador de elétrons, não a produção de ATP; quem define respiração aeróbia, respiração anaeróbia ou fermentação é qual molécula recebe os elétrons no fim da linha.]

#subtopico("3.3 O produto final é assinatura — e transforma o meio")

Se as etapas até o piruvato são as mesmas em toda parte, a diferença entre os grupos bacterianos aparece depois dele. Um gênero reduz o piruvato a lactato e para por aí; outro produz uma mistura de ácidos e formato, que decompõe em CO₂ e hidrogênio; outro segue por uma rota que termina em acetoína e butanodiol; outro produz ácido propiônico; outro ainda, ácidos butírico e acético, acetona e butanol. Uma levedura reduz o mesmo piruvato a acetaldeído e depois a etanol, liberando CO₂ no caminho. *As vias são idênticas até o piruvato; o que muda é como cada organismo se livra dos elétrons depois dele* — e o conjunto de produtos finais funciona como assinatura química do gênero.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-28.png",
  largura: 58%,
  legenda: [O piruvato no centro e as rotas que dele partem, com o gênero responsável ao lado de cada uma. Lactato de um lado, mistura de ácidos e formato de outro, butanodiol num terceiro ramo, ácidos butírico e propiônico num quarto. O laboratório de identificação lê exatamente este esquema de trás para frente: dado o produto encontrado, qual grupo o produziu.])

O que essa assinatura faz com o meio ao redor é a ponte para toda a próxima seção. Uma célula que fermenta obtém dois ATP por glicose; uma que respira obtém cerca de trinta e oito. Para produzir a mesma quantidade de energia, a fermentadora precisa consumir dezenas de vezes mais açúcar — e despejar no meio dezenas de vezes mais produto ácido. O resultado é uma *acidificação acentuada do meio* toda vez que há fermentação ativa de açúcar. Já a célula que respira oxida o açúcar completamente até CO₂, que se dissipa, e quando o açúcar termina passa a catabolizar aminoácidos; a desaminação libera amônia, e o meio *alcaliniza*.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-29.png",
  largura: 58%,
  legenda: [O efeito do metabolismo sobre o meio de cultura. À esquerda, o destino da glicose conforme haja ou não oxigênio. À direita, a consequência que interessa ao laboratório: a via fermentativa, de baixo rendimento, consome muito açúcar e acidifica o meio; a via respiratória oxida o açúcar até o fim e, esgotado ele, alcaliniza o meio pela degradação de proteína.])

Guarde essa frase porque ela é a chave da última seção da aula: um indicador de pH acrescentado ao meio traduz essa diferença em cor. *O meio de cultura diferencial não enxerga a bactéria — ele enxerga o rastro químico que o metabolismo dela deixou.*

#subtopico("3.4 Meio líquido, meio sólido e o que cada um responde")

Um meio de cultura é uma tentativa de reproduzir, numa placa ou num tubo, a lista de compras da PARTE II. A primeira escolha é de estado físico, e ela não é estética: cada estado responde a uma pergunta diferente.

O *meio líquido*, ou caldo, mantém todas as células em suspensão, com nutriente alcançando cada uma delas por convecção. É por isso que a curva de crescimento se levanta em caldo, e não em placa: só nele existe uma população homogênea cuja densidade se pode medir de hora em hora. Caldo é também o formato usado quando se quer produzir biomassa para extrair alguma molécula.

O *meio sólido* tem exatamente a mesma composição química, acrescida de cerca de 2% de #termo-nota[ágar][polissacarídeo extraído de algas, que funde perto de 100 °C, solidifica em torno de 40 °C e não é degradado pela grande maioria das bactérias]. As três propriedades do ágar explicam por que ele é insubstituível. Não ser degradado significa que a placa permanece firme enquanto a bactéria cresce sobre ela. Fundir a 100 °C e solidificar só perto de 40 °C cria uma janela de temperatura em que o meio ainda está líquido e já não cozinha o que se lhe acrescenta — foi exatamente essa janela que separou o ágar sangue do ágar chocolate na PARTE II, onde a diferença entre as duas placas era só a temperatura em que o sangue entrou.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-30.png",
  largura: 56%,
  legenda: [As duas apresentações e seus usos. À esquerda, o caldo, formato em que se acompanha a curva de crescimento e se produz biomassa. À direita, o meio sólido e a semeadura por esgotamento: a alça é arrastada em estrias sucessivas, diluindo o inóculo no espaço até que, nas últimas estrias, células fiquem suficientemente separadas para originar colônias isoladas.])

Sobre o meio sólido faz-se a manobra que fundou a bacteriologia: a *semeadura por esgotamento*. A alça é arrastada sobre a placa em séries sucessivas de estrias, e a cada série sobra menos material sobre ela, de modo que nas últimas estrias as células se depositam isoladas umas das outras. Cada uma delas origina uma colônia — e essa colônia, como a PARTE I mostrou, é um clone de até cerca de 10⁸ células descendentes de uma única. Sem esse gesto não existiria cultura pura, e sem cultura pura não existiria identificação.

A segunda escolha é de composição. O *meio mínimo*, ou mineral, contém apenas sais e uma única fonte de carbono definida. Ele é pobre de propósito: só cresce nele quem consegue sintetizar, a partir daquele carbono e daqueles sais, todos os aminoácidos, bases e vitaminas de que precisa. Por isso o meio mínimo não serve para isolar agente de amostra clínica, e serve muito bem para responder o que uma bactéria sabe fabricar. O *meio completo*, ou complexo, faz o oposto: entrega proteína já hidrolisada, com ou sem açúcar acrescentado, e por isso sustenta o crescimento do maior número possível de espécies — inclusive as que perderam vias biossintéticas. É o meio de partida da rotina diagnóstica, e a base sobre a qual todos os meios da próxima seção são construídos.

#subtopico("3.5 Meios diferenciais e seletivos: inibir é diferente de revelar")

Uma amostra de sítio com microbiota abundante, semeada em meio completo, produz uma placa coberta de colônias de espécies acompanhantes — e o agente procurado pode simplesmente não ser encontrado no meio da multidão. Os dois recursos que resolvem esse impasse são frequentemente tratados como um só, e são mecanicamente opostos.

O *meio seletivo* contém uma substância que *impede o crescimento* de parte das bactérias. Sal biliar e cristal violeta desorganizam a membrana externa — e como a Gram-positiva não tem membrana externa por fora da parede, é justamente ela quem sofre, o que faz desses meios um filtro para Gram-negativas. Concentração alta de cloreto de sódio, da ordem de 7,5%, impõe um estresse osmótico que poucas espécies suportam, e seleciona as que suportam. Antimicrobianos acrescentados ao meio selecionam o gênero que lhes é intrinsecamente insensível. Em todos os casos, o meio seletivo reduz o número de espécies presentes na placa.

O *meio diferencial*, ao contrário, não impede ninguém de crescer. Ele contém um substrato definido e um indicador, e a colônia que metaboliza aquele substrato fica de uma cor, enquanto a que não metaboliza fica de outra. É aqui que a seção anterior se cobra: o indicador é quase sempre um indicador de pH, e o que ele registra é a acidificação produzida pela fermentação. Colônia que fermentou a lactose acidifica o entorno e vira o indicador; colônia que não fermentou permanece incolor. Ágar sangue é outro exemplo de meio diferencial — nada é inibido, e o que se lê é o padrão de hemólise ao redor da colônia.

Nada impede que um mesmo meio faça as duas coisas, e vários dos mais usados fazem: contêm o inibidor que restringe quem cresce e o indicador que separa por cor quem cresceu.

#mini-resumo[Em uma frase: o inibidor age antes, decidindo quem entra na placa; o indicador age depois, traduzindo em cor o que aquela colônia fez com o substrato oferecido.]

#table(
  columns: (auto, 1fr, 1fr),
  inset: 7pt,
  align: left,
  table.header([*Meio*], [*O que ele inibe (seletivo)*], [*O que ele revela (diferencial)*]),
  [MacConkey], [sais biliares e cristal violeta impedem o crescimento de Gram-positivas], [fermentação de lactose: colônia rosa quando fermenta, incolor quando não fermenta],
  [Manitol salgado], [7,5% de cloreto de sódio impede quase todas as espécies], [fermentação de manitol vira o indicador para amarelo],
  [Ágar sangue], [nada — meio completo enriquecido], [padrão de hemólise em torno da colônia],
  [Ágar chocolate seletivo], [antimicrobianos suprimem a microbiota acompanhante], [permite crescer espécie fastidiosa que exige fatores liberados pela hemácia rompida],
  [Cetrimide], [detergente catiônico impede a maioria das espécies], [pigmento difusível produzido pelo gênero selecionado],
)

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-31.png",
  largura: 70%,
  legenda: [Os cinco tipos de meio lado a lado. Mineral e completo diferem por quanto entregam pronto; diferenciais separam por cor sem inibir ninguém; seletivos inibem sem necessariamente colorir; e os últimos reúnem as duas propriedades. Repare que a mesma placa de MacConkey aparece duas vezes, como diferencial e como seletiva — porque ela é, de fato, as duas coisas.])

#confusao-prevista(
  titulo: "Seletivo restringe quem cresce; diferencial mostra quem cresceu",
  aluno_acha: [que meio seletivo e meio diferencial são nomes distintos para a mesma ideia de "separar bactérias na placa"],
  mecanismo: [o seletivo age antes do crescimento, com uma substância que impede parte das espécies de se multiplicar — o resultado é uma placa com menos espécies. O diferencial age depois, com um substrato e um indicador que traduzem uma diferença metabólica em cor — o resultado é uma placa com o mesmo número de espécies, agora distinguíveis a olho nu. Um reduz a população da placa; o outro não reduz nada, apenas revela.],
)

#clinica-box("A escolha do meio começa no sítio de coleta",
[Um mesmo agente pode exigir meios completamente diferentes conforme o local de onde veio a amostra, e a razão é a microbiota acompanhante. Líquor e sangue são sítios normalmente estéreis: qualquer crescimento tem valor, e o meio de escolha é o mais rico possível, sem inibidor nenhum, para não perder um agente fastidioso ou já parcialmente inibido por antimicrobiano prévio. Fezes e secreção de mucosa colonizada são o extremo oposto: o agente procurado convive com uma população acompanhante que o supera em ordens de grandeza, e semear isso em meio completo produz uma placa inútil — por isso a amostra vai obrigatoriamente para meio seletivo, e frequentemente para mais de um em paralelo. A urina fica no meio-termo: como a bexiga é estéril mas a uretra distal não é, o resultado só tem sentido junto com a contagem — daí a urocultura semear volume calibrado e relatar unidade formadora de colônia por mililitro, e não apenas "cresceu". Em todos os casos é a informação clínica do pedido que permite escolher a placa certa; sem ela, escolhe-se a mais provável, e o agente incomum passa.])

#subtopico("3.6 Quando o meio não resolve")

Existe um grupo de agentes para os quais toda a engenharia de meios da seção anterior não basta, e vale entender por que — porque o motivo é diferente em cada caso, e a estratégia diagnóstica muda com ele.

O primeiro motivo é o *tempo*, e ele volta diretamente à PARTE I. O agente da tuberculose tem parede rica em lipídeos que retarda a entrada de nutrientes, e um tempo de geração de 18 a 24 horas. Aplicando a mesma aritmética das primeiras páginas: para chegar às cerca de 10⁸ células que tornam uma colônia visível a olho nu são necessárias em torno de 27 duplicações, o que a 20 minutos por geração levaria menos de dez horas, e a 20 horas por geração leva mais de vinte dias. O meio existe, é enriquecido e sustenta bem o crescimento — mas a cultura leva de três a seis semanas. Nesse intervalo o paciente precisa ser tratado, e é por isso que o diagnóstico se apoia primeiro em coloração específica da parede e em métodos de amplificação de ácido nucleico, deixando a cultura para confirmar a espécie e testar a sensibilidade.

O segundo motivo é a *dependência do hospedeiro*. Alguns agentes não crescem em meio artificial nenhum, por mais rico que seja. O agente da hanseníase e o da sífilis são os exemplos clássicos, e o mecanismo por trás é o mesmo em ambos: ao longo da evolução como parasitas obrigatórios, essas espécies perderam grandes trechos de genoma — inclusive vias biossintéticas e partes do metabolismo energético — e passaram a depender de moléculas que só a célula hospedeira fornece. Não é falta de vitalidade: dentro do hospedeiro essas bactérias são metabolicamente ativas e causam doença grave. É especialização levada ao ponto de não haver mais como reproduzir o ambiente na bancada. Por isso a propagação laboratorial delas é feita em modelo animal, e o diagnóstico de rotina se apoia em exame direto, detecção de material genético e resposta imune do hospedeiro.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-32.png",
  largura: 56%,
  legenda: [Três situações distintas sob o mesmo rótulo. A micobactéria cora por técnica específica e cresce em meio próprio, mas leva semanas. O agente da hanseníase e o da sífilis não crescem em meio artificial nenhum, por dependerem de fatores do hospedeiro, e sua propagação laboratorial é feita em modelo animal.])

#atencao-box("Cultura negativa não é ausência de agente",
[Um resultado de cultura sem crescimento admite pelo menos quatro leituras, e apenas uma delas é "não há infecção bacteriana". As outras três são: o agente é fastidioso e o meio usado não o sustentava; o agente é de crescimento lento e o tempo de incubação foi insuficiente; ou o paciente já recebeu antimicrobiano antes da coleta, e a população viável caiu abaixo do limiar de detecção sem que a infecção tenha sido resolvida. Some-se a isso a possibilidade de coleta em sítio inadequado ou de transporte que matou o agente, como no caso dos anaeróbios. A consequência é que uma cultura negativa só tem valor de exclusão quando se sabe que o método empregado seria capaz de detectar o agente suspeito — e essa informação vem da hipótese clínica, não do laboratório.])

#conclusao-box[
Feche esta aula com uma única frase organizadora: *tudo o que se estudou aqui são condições impostas a uma operação só, a duplicação de uma célula em duas.* A divisão binária define a forma da multiplicação; o tempo de geração define a sua velocidade; e a fórmula X = x₀ · 2ⁿ descreve exatamente o trecho em que nada a limita — e apenas esse trecho.

O mecanismo nuclear que amarra o resto é o encontro entre essa aritmética e os seus limites. A célula precisa receber carbono, nitrogênio, fósforo, enxofre, metais e aquilo que ela não sabe fabricar; precisa de uma faixa de pH em que consiga manter o citoplasma neutro, de uma faixa de temperatura abaixo da desnaturação das suas proteínas, e de uma relação viável com o oxigênio, determinada pelas enzimas que possui para neutralizar os derivados reativos. Quando algum desses insumos falta, ou quando o produto do próprio metabolismo satura o ambiente, a exponencial termina — e a curva de quatro fases é o registro gráfico desse encontro. O modo como a célula financia a duplicação fecha o círculo: fermentar ou respirar depende do aceptor final de elétrons disponível, o rendimento decorre dessa escolha, e o rastro químico deixado no meio — acidificação pela fermentação intensa, alcalinização pelo catabolismo de proteína — é precisamente o que o meio diferencial converte em cor.

A clínica aparece em cada uma dessas dobras pelo mesmo mecanismo. A demora de uma cultura não é lentidão do laboratório: é o tempo de geração do agente multiplicado pelas cerca de 27 duplicações necessárias para tornar uma colônia visível. A célula da estacionária tolera concentrações que matariam a mesma bactéria em multiplicação, não por carregar gene de resistência, mas por não oferecer o processo que a droga ataca — e é isso que explica a recidiva de infecções ligadas a biofilme e a material implantado. E uma cultura negativa é, com frequência, o registro de um agente exigente, lento ou já suprimido por antimicrobiano prévio.

O passo seguinte é a consequência natural de tudo isto: sabendo em que condições uma população cresce e em que fase ela é vulnerável, torna-se possível fazer o inverso de propósito — impedir o crescimento onde ele não deve acontecer. É o assunto imediatamente à frente: os agentes que descontaminam ambiente e superfície, os que se aplicam sobre pele e mucosa e os que combatem a bactéria já instalada. Cada um ataca um ponto que esta aula descreveu — a parede que se constrói na divisão, a proteína que se desnatura com o calor, a via que depende de um fator que a célula não fabrica. Quem entendeu a curva já sabe, de antemão, por que a fase em que a população se encontra muda o resultado do tratamento.
]
