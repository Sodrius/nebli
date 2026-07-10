#import "../../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O #sigla("DNA", [ácido desoxirribonucleico — a molécula que guarda a informação genética em sequência de bases]) parece, à primeira vista, um arquivo guardado num cofre: estável, isolado, intocável. Não é. Todos os dias, em cada uma das suas células, esse arquivo sofre milhares de pequenos acidentes — uma base que muda de forma na hora errada, um raio de sol que cola duas letras vizinhas, um agente químico que se infiltra no lugar de uma base verdadeira. Se cada um desses acidentes virasse uma alteração permanente, o genoma se desmancharia em poucas gerações de células.

  Este resumo conta a história em três atos que se encaixam. No *primeiro*, vamos entender o que é uma *mutação* — como a sequência de bases muda, de quantos tipos é essa mudança, e de onde vêm os erros (uns nascem por acaso dentro da própria replicação, outros são empurrados de fora por substâncias químicas e pela luz ultravioleta). No *segundo*, veremos que a célula não é vítima passiva: ela tem máquinas de *reparo* que reconhecem o estrago e o desfazem, e o que acontece com uma pessoa quando essas máquinas faltam. No *terceiro*, mudamos de escala: alguns pedaços de DNA não ficam parados — *plasmídeos*, *transposons* e *vírus* se movem, saltam, se integram a genomas alheios e recombinam material genético, espalhando características novas (entre elas, a resistência a antibióticos) de uma célula para outra.

  O fio que costura os três atos é simples: a *sequência de bases é informação, e informação que muda — por erro ou por movimento — muda o organismo*. Ora isso ameaça (câncer), ora isso é a própria matéria-prima da evolução e da engenharia genética.
]

#parte-title("PARTE I — Mutação: o que muda e por que aparece", primeira: true)

#subtopico("1.1 — O que é uma mutação e os três tipos")

Uma mutação é qualquer alteração permanente na sequência de bases do DNA. A palavra "permanente" é o que importa: um dano que a célula conserta antes de copiar o DNA não conta como mutação; só vira mutação quando a alteração é *fixada* — copiada para a fita-filha e, a partir daí, herdada por todas as células descendentes. Como a sequência de bases é lida em trincas (os #termo-nota[códons][trinca de bases do mRNA que especifica um aminoácido; a leitura é feita de três em três, sem espaços, a partir de um ponto fixo]) para montar proteínas, mexer numa única base pode mudar o aminoácido que entra na cadeia — e, com ele, a forma e a função da proteína.

Há três maneiras básicas de a sequência mudar. A primeira é a *substituição*: uma base é trocada por outra, sem alterar o número total de letras. Se a troca é entre bases do mesmo tipo químico — uma purina por outra purina (A↔G), ou uma pirimidina por outra pirimidina (C↔T) —, chamamos de #termo-nota[transição][substituição entre bases quimicamente semelhantes: purina por purina ou pirimidina por pirimidina]; se a troca atravessa os tipos (purina por pirimidina), é uma #termo-nota[transversão][substituição entre bases de tipos químicos diferentes: purina por pirimidina ou vice-versa]. Uma substituição às vezes não muda nada (o novo códon ainda codifica o mesmo aminoácido), às vezes troca um aminoácido por outro, e às vezes cria um códon de parada no meio do gene — encurtando a proteína abruptamente.

#figura-nebli("/figuras/biomol-25-mutacao-reparo-recombinacao/slide-03.png",
  largura: 55%,
  legenda: [A sequência de DNA é transcrita em mRNA e traduzida em proteína. Trocar uma única base no DNA muda um códon do mRNA e, com ele, o aminoácido na posição correspondente — o efeito sobe da molécula até a função da proteína.])

A segunda e a terceira maneiras são mais drásticas porque mudam o *número* de letras: a *deleção* (perda de uma ou mais bases) e a *inserção* (ganho de uma ou mais bases). Quando a quantidade perdida ou ganha não é múltipla de três, acontece a consequência mais grave de todas — o #termo-nota[frameshift][deslocamento do quadro de leitura: inserção ou deleção de um número de bases não-múltiplo de 3 reposiciona todos os códons seguintes, trocando toda a sequência de aminoácidos a partir dali]. Como a tradução lê de três em três a partir de um ponto fixo, tirar ou pôr uma base desloca *todas* as trincas seguintes. A partir do ponto da mutação, cada códon passa a ser lido "fora de fase", e a proteína inteira a jusante sai trocada — em geral terminando cedo, num códon de parada que apareceu por acaso no novo quadro.

#mini-resumo[Substituição troca uma letra (efeito local); inserção e deleção mudam a contagem de letras e, se não forem múltiplas de 3, deslocam todo o quadro de leitura adiante (frameshift, efeito catastrófico).]

#subtopico("1.2 — Mutações espontâneas e a fidelidade da replicação")

Voltando ao que você já viu na replicação do DNA: cada vez que a célula copia seu genoma, ela precisa encaixar, uma a uma, bilhões de bases na fita nova. Seria de esperar um mar de erros — e, no entanto, mutações espontâneas são *raríssimas*. Em organismos como a bactéria _E. coli_ e a mosca _Drosophila_, ocorre cerca de uma mutação a cada bilhão de bases replicadas. Esse número minúsculo não é sorte: é o resultado de duas linhas de defesa embutidas na própria replicação.

A primeira linha é a *seletividade* da DNA polimerase III, que faz o grosso da cópia e quase nunca coloca a base errada. A segunda é a *revisão* (a atividade de edição, ou _proofreading_): quando uma base errada escapa e é incorporada, uma atividade exonuclease — associada à polimerase III durante a síntese e reforçada pela DNA polimerase I — volta atrás, remove a base incorreta e repõe a certa, antes de seguir adiante. É a combinação de colocar certo quase sempre e corrigir o quase-nunca que derruba a taxa de erro para a casa de um em um bilhão.

Mesmo assim, alguns erros nascem não de a polimerase "errar a mira", mas de a *própria base mudar de forma por um instante*. As bases nitrogenadas existem, em sua imensa maioria, numa forma química estável; raramente, porém, um próton se desloca dentro da molécula e a base assume um #termo-nota[tautômero][forma química alternativa e instável de uma base, em que um átomo de hidrogênio mudou de posição; nessa forma transitória, a base pareia com o parceiro errado] — uma forma rara e fugaz que pareia com a base errada. Se a replicação flagra a base exatamente nesse instante, encaixa o parceiro incorreto, e o erro fica. Outra fonte espontânea é a *deaminação*: a citosina perde espontaneamente um grupo amino e vira uracila, que pareia como se fosse timina — uma transição C→T pronta para acontecer se o reparo não chegar antes.

#clinica-box("Por que as células não acumulam erros sem parar", [Cada uma das suas células copia 3 bilhões de bases a cada divisão. Sem revisão, a taxa de erro da polimerase sozinha já encheria o genoma de mutações em poucas gerações. A edição (proofreading) e os sistemas de reparo que veremos na PARTE II baixam a taxa final em mais de mil vezes. Defeitos hereditários nesses sistemas — como veremos no câncer de cólon hereditário e no xeroderma pigmentoso — disparam a frequência de tumores justamente porque o erro deixa de ser corrigido.])

#subtopico("1.3 — Mutações induzidas: química e radiação UV")

Há um ponto em que a intuição falha: nem toda mutação vem de erro interno. Boa parte é *induzida* — empurrada de fora por agentes que atacam o DNA. Esses agentes (chamados *mutagênicos*) se dividem, de modo útil, em químicos e físicos, e entender o mecanismo de cada um já antecipa o tipo de reparo que vai ser preciso.

Entre os químicos, um grupo elegante é o dos *análogos de base*: moléculas tão parecidas com uma base verdadeira que a polimerase as incorpora por engano. O exemplo clássico é o *5-bromouracil* (5-BrU), um sósia da timina. Ele deveria parear com adenina, como a timina faz; mas o átomo de bromo desloca a nuvem de elétrons da molécula e faz o 5-BrU passar boa parte do tempo numa forma que reconhece a *guanina*. Resultado: numa rodada de replicação ele entra no lugar da timina pareando com A; na rodada seguinte, na sua forma alterada, puxa uma G — e a base original A foi trocada por G poucas divisões depois. Outros químicos, como a *2-aminopurina* e a *hipoxantina* (produto da deaminação da adenina), agem pelo mesmo princípio: imitam uma base e enganam o pareamento.

#figura-nebli("/figuras/biomol-25-mutacao-reparo-recombinacao/slide-12.png",
  largura: 50%,
  legenda: [O 5-bromouracil (à esquerda) é um análogo da timina (à direita). Quase idêntico — mas o bromo desloca elétrons e faz a molécula reconhecer guanina em vez de adenina, semeando uma troca de base nas replicações seguintes.])

O agente físico mais importante é a *radiação ultravioleta* (UV) — a mesma do sol. Dos tipos de UV, o #sigla("UVB", [radiação ultravioleta B, de comprimento de onda intermediário; é absorvida diretamente pelas bases do DNA e o principal responsável pelos dímeros de pirimidina]) é o vilão direto: seu comprimento de onda é absorvido pelas próprias bases nitrogenadas e induz uma ligação química anômala entre *duas pirimidinas vizinhas na mesma fita* — tipicamente duas timinas adjacentes, formando o #termo-nota[dímero de pirimidina][ligação covalente anômala entre duas pirimidinas vizinhas na mesma fita (em geral duas timinas), causada por UV; deforma a hélice e trava a replicação]. Esse dímero (o famoso "dímero de timina") entorta a dupla-hélice e trava a maquinaria que tenta copiar ou ler aquele trecho. O #sigla("UVA", [radiação ultravioleta A, de comprimento de onda mais longo; penetra mais fundo na pele e lesa o DNA sobretudo de modo indireto, via radicais livres]), de onda mais longa, penetra mais fundo na pele e age mais por vias indiretas (radicais livres), mas o dano-assinatura da luz solar no DNA é o dímero de pirimidina.

#figura-nebli("/figuras/biomol-25-mutacao-reparo-recombinacao/slide-16.png",
  largura: 55%,
  legenda: [UVB e UVA penetram a pele a profundidades diferentes. O UVB, mais energético, é absorvido direto pelas bases na epiderme e gera os dímeros de pirimidina — o dano que abre a PARTE II sobre reparo.])

#confusao-prevista(
  titulo: "Mutagênico não é o mesmo que o erro já fixado",
  aluno_acha: [muitos alunos tratam o dímero de timina ou o 5-BrU recém-incorporado como se já fosse a mutação definitiva.],
  mecanismo: [o dímero e o análogo são *lesões* — alterações ainda corrigíveis. Viram mutação só se a célula *replicar por cima* delas sem reparar antes. É por isso que existe a PARTE II: entre a lesão e a mutação permanente há uma janela em que o reparo pode salvar a sequência.],
)

A PARTE II inteira nasce dessa última frase: a célula tem essa janela porque desenvolveu máquinas que reconhecem o estrago e o desfazem antes da próxima cópia. Vamos a elas.

#parte-title("PARTE II — Reparo: desfazer o erro antes que fixe")

#subtopico("2.1 — Reparo direto: fotoliase e MGMT")

Pense no reparo como uma oficina com várias estratégias para o mesmo objetivo: devolver a sequência original. A estratégia mais econômica é o *reparo direto* — desfazer quimicamente a lesão sem precisar cortar nem remover pedaço nenhum da fita. É como apagar uma rasura a borracha, em vez de arrancar e reescrever a linha inteira. Dois exemplos mostram o princípio.

O primeiro é a *fotoliase*, a enzima da #termo-nota[fotorreativação][reparo direto em que a fotoliase usa a energia da luz visível para quebrar o dímero de pirimidina e devolver as duas bases separadas]. Ela se encaixa exatamente sobre um dímero de pirimidina e, usando a energia da própria luz (luz visível, captada por um cofator derivado do ácido fólico), quebra a ligação anômala entre as duas timinas e as devolve separadas, como eram antes. Repare na ironia elegante: a luz solar UV causa o dímero, e a fotoliase usa outra faixa de luz para desfazê-lo. Essa enzima está bem caracterizada em bactérias e em muitos organismos — mas, atenção, os seres humanos *não* a possuem de forma funcional, e dependem para os dímeros do reparo por excisão (subtópico 2.2).

#figura-nebli("/figuras/biomol-25-mutacao-reparo-recombinacao/slide-28.png",
  largura: 50%,
  legenda: [A fotoliase reconhece o dímero de ciclobutano entre duas timinas e usa a energia da luz absorvida para regenerar as duas pirimidinas separadas — reparo direto, sem cortar a fita.])

O segundo exemplo é a *MGMT*, a #sigla("MGMT", [O6-metilguanina-DNA-metiltransferase — enzima de reparo direto que remove o grupo metil da O6-metilguanina, transferindo-o para si mesma e se inativando no processo]). Certos agentes alquilantes colam um grupo metil na guanina, formando a *O6-metilguanina* — uma lesão altamente cancerígena, porque essa guanina metilada pareia erradamente com timina e semeia transições. A MGMT resolve o problema de modo peculiar: ela arranca o grupo metil da guanina e o transfere para um resíduo de cisteína dentro de si mesma. Ao fazê-lo, a *própria enzima se inativa de vez* — cada molécula de MGMT só conserta uma lesão e depois é descartada. Por isso ela costuma ser chamada de enzima "suicida" ou "de uso único": gasta-se uma proteína inteira para apagar uma única metila, o que mostra o quanto a célula valoriza limpar essa lesão específica.

#mini-resumo[Reparo direto = desfazer a lesão no lugar, sem cortar a fita. Fotoliase reverte o dímero de pirimidina com luz; MGMT remove a metila da O6-metilguanina e se sacrifica no processo.]

#subtopico("2.2 — Reparo por excisão de nucleotídeo")

Quando a lesão deforma fisicamente a hélice — e o dímero de pirimidina é o caso típico —, a estratégia muda: em vez de consertar no lugar, a célula *recorta o trecho danificado e o reconstrói* a partir da fita-molde intacta. É o reparo por excisão de nucleotídeo, ou #sigla("NER", [nucleotide excision repair — reparo por excisão de nucleotídeo: reconhece distorções da hélice, recorta um oligonucleotídeo contendo a lesão e ressintetiza usando a fita-molde]). A lógica geral é poderosa: como a informação genética é redundante (cada base tem seu par complementar na outra fita), dá para jogar fora a fita estragada e copiar de volta pela boa.

Em bactérias, o NER é executado por um complexo codificado pelos genes *uvrABC*. O mecanismo tem uma sequência fixa de passos que vale a pena fixar em ordem. Primeiro, o complexo *reconhece* a distorção causada pelo dímero. Em seguida, a #termo-nota[excinuclease][atividade do complexo uvrABC que faz duas incisões na fita danificada, uma de cada lado da lesão, liberando o trecho lesado como um oligonucleotídeo] faz *duas incisões* na fita danificada, uma de cada lado da lesão — e essas incisões são *assimétricas*: o corte cai a 8 nucleotídeos do lado 5′ e a 4 nucleotídeos do lado 3′ da lesão, liberando um oligonucleotídeo de 12 bases que contém o dímero. Removido o trecho, a *DNA polimerase I* preenche a lacuna sintetizando DNA novo sobre a fita-molde intacta, e a *DNA ligase* sela a última emenda, reconstituindo a continuidade da fita. A figura abaixo mostra a sequência inteira.

#align(center, block(width: 80%, stroke: 0.5pt + gray-border, inset: 10pt, radius: 4pt, fill: gray-bg,
  stack(spacing: 7pt,
    text(size: 9pt, weight: "bold", fill: navy)[Reparo por excisão de nucleotídeo (sistema uvrABC)],
    rect(width: 100%, inset: 7pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border,
      text(size: 9pt)[*1. Reconhecimento* — o complexo uvr detecta a distorção da hélice causada pelo dímero de timina.]),
    align(center, text(size: 12pt, fill: navy)[↓]),
    rect(width: 100%, inset: 7pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border,
      text(size: 9pt)[*2. Dupla incisão (excinuclease)* — corta a 8 nt do lado 5′ e a 4 nt do lado 3′, liberando um oligonucleotídeo de 12 bases com a lesão.]),
    align(center, text(size: 12pt, fill: navy)[↓]),
    rect(width: 100%, inset: 7pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border,
      text(size: 9pt)[*3. Síntese* — a DNA polimerase I preenche a lacuna usando a fita-molde intacta como guia.]),
    align(center, text(size: 12pt, fill: navy)[↓]),
    rect(width: 100%, inset: 7pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border,
      text(size: 9pt)[*4. Selagem* — a DNA ligase une as extremidades e restaura a fita contínua, sem cicatriz.]),
  )))

Note o que torna o NER tão versátil: ele não reconhece uma lesão química específica, e sim a *deformação geométrica* que muitas lesões diferentes causam na hélice. Por isso o mesmo sistema dá conta de dímeros de pirimidina, de bases volumosas grudadas por químicos e de outras distorções — é um reparo de amplo espectro. Nos seres humanos existe um NER análogo, mais complexo, com várias proteínas; é justamente nele que mora o defeito do xeroderma pigmentoso, no subtópico seguinte.

#mini-resumo[NER = recorta e reconstrói. Reconhecimento da distorção → dupla incisão assimétrica (8 nt na 5′, 4 nt na 3′) → Pol I preenche → ligase sela. Conserta qualquer lesão que entorte a hélice.]

#subtopico("2.3 — Quando o reparo falha: xeroderma, câncer e resposta SOS")

A melhor evidência de que o reparo importa é ver o que acontece quando ele falta. O *xeroderma pigmentoso* é uma doença genética, transmitida de modo #termo-nota[autossômico recessivo][padrão de herança em que a doença só aparece quando a pessoa recebe a cópia defeituosa do gene de ambos os pais], em que as proteínas do NER humano são defeituosas. Sem NER funcional, os dímeros de pirimidina causados pela luz do sol *não são removidos*: acumulam-se, são replicados por cima, e viram mutações. O fenótipo é dramático — a pele é extremamente sensível ao sol, surgem múltiplos cânceres de pele já na infância, e os pacientes frequentemente morrem de metástases antes dos 30 anos. O xeroderma é a demonstração clínica direta da frase central da PARTE I: lesão não-reparada → mutação fixada → câncer.

#clinica-box("Por que falha de reparo vira câncer", [O câncer nasce quando uma célula acumula mutações em genes que controlam sua própria divisão. Cada dímero de timina não-reparado é uma chance de mutação; cada mutação é um dado a mais na roleta. No xeroderma, o sistema que apagaria esses danos está quebrado — então a conta de mutações sobe rápido sob exposição solar, e o câncer de pele aparece cedo e em muitos pontos. O mesmo princípio vale para outros sistemas de reparo: quando o reparo de erros de pareamento falha por herança, dispara o câncer colorretal hereditário. O elo é sempre o mesmo: menos reparo, mais mutação, mais tumor.])

Há ainda uma resposta de emergência que merece menção: a *resposta SOS* das bactérias. Quando o DNA sofre dano extenso, a célula precisa decidir entre travar tudo ou seguir replicando mesmo com lesões. A SOS é o programa que liga, de uma vez, dezenas de genes de reparo. O gatilho é mecanístico e bonito: em condições normais, a proteína #sigla("LexA", [repressor que mantém desligados os genes da resposta SOS bacteriana; é clivado quando há dano extenso ao DNA, liberando a transcrição desses genes]) fica grudada na região reguladora desses genes, mantendo-os desligados. Quando o dano gera fitas simples de DNA expostas, a proteína #sigla("RecA", [proteína bacteriana que, ativada por DNA de fita simples exposto no dano, estimula a autoclivagem do repressor LexA e dispara a resposta SOS]) se ativa e estimula a *autoclivagem* do LexA. Sem o repressor, os genes SOS são transcritos em massa e a maquinaria de reparo de emergência entra em cena. É um interruptor que só liga quando o estrago é grande o bastante para justificar.

A lição que atravessa a PARTE II e nos leva à PARTE III é esta: a célula investe pesado para *manter* sua sequência estável. E, no entanto — eis a virada —, certos pedaços de DNA fazem exatamente o oposto: vivem para *se mover e mudar de lugar*. É para esses elementos móveis que vamos agora.

#parte-title("PARTE III — DNA móvel e recombinação")

#subtopico("3.1 — Plasmídeos, fator F e conjugação")

Nem todo DNA de uma célula está no cromossomo. As bactérias carregam, além do cromossomo principal, pequenas moléculas de DNA *circular* e independentes chamadas *plasmídeos*. Eles variam de tamanho (de uns 2 mil a 100 mil pares de base) e têm uma propriedade decisiva: são #termo-nota[replicons][moléculas de DNA com sua própria origem de replicação, capazes de se replicar de forma autônoma, independentemente do cromossomo da célula] — possuem sua própria origem de replicação e se copiam com autonomia, sem depender do ciclo do cromossomo. A célula pode até dispensá-los em certas condições; mas, quando presentes, os plasmídeos costumam carregar genes que dão vantagens extras — e a mais célebre delas é a *resistência a antibióticos*.

O que torna os plasmídeos perigosos do ponto de vista clínico não é só carregarem resistência, e sim conseguirem *passar de uma bactéria para outra*. Esse processo de troca de material genético entre duas bactérias chama-se #termo-nota[conjugação][transferência de material genético de uma bactéria doadora para uma receptora através de contato direto, mediada por um plasmídeo conjugativo como o fator F]. O *fator F* (de "fertilidade", um plasmídeo de cerca de 93 mil pares de base) é o exemplo padrão: a bactéria que o possui (F⁺) constrói uma ponte de contato com uma bactéria que não o possui (F⁻) e transfere uma cópia do plasmídeo através dela. A receptora, que era F⁻, torna-se F⁺ — e, se o plasmídeo carregava genes de resistência, ela acaba de adquirir resistência *sem nunca ter encontrado o antibiótico*.

#figura-nebli("/figuras/biomol-25-mutacao-reparo-recombinacao/slide-37.png",
  largura: 65%,
  legenda: [Conjugação. Acima: uma bactéria F⁺ transfere o fator F a uma F⁻, que se torna F⁺. Abaixo: o fator F pode recombinar-se com o cromossomo de _E. coli_, integrando-se a ele — a base da troca de informação genética entre bactérias.])

#clinica-box("Conjugação e resistência a antibióticos", [A disseminação de resistência em hospitais não depende só de cada bactéria sofrer sua própria mutação. Plasmídeos de resistência saltam, por conjugação, entre bactérias — às vezes entre espécies diferentes. Uma única bactéria resistente pode "doar" o plasmídeo a vizinhas sensíveis, que se tornam resistentes em minutos. É por isso que o uso indiscriminado de antibióticos seleciona e espalha resistência tão depressa: o gene não precisa surgir de novo em cada célula, ele *viaja*.])

#subtopico("3.2 — Transposons: genes que saltam")

Voltando à ideia de que o DNA deveria ser estável: nos anos 1950, Barbara McClintock observou, no milho, genes que *mudavam de lugar dentro do próprio genoma*. A ideia era tão herética para a época que ela foi praticamente excluída da comunidade científica — e só décadas depois, com a biologia molecular madura, recebeu o reconhecimento (e o Nobel). Esses elementos que saltam são os *transposons* (em inglês, _jumping genes_): segmentos de DNA capazes de se deslocar de uma posição a outra no genoma.

O salto é catalisado por uma enzima que o próprio transposon costuma carregar, a #termo-nota[transposase][enzima codificada pelo próprio transposon que reconhece suas extremidades, recorta-o (ou copia-o) e o insere em um novo sítio do genoma]. Os transposons vêm em graus de complexidade: os mais simples são as *sequências de inserção* (#sigla("IS", [insertion sequence — sequência de inserção: o transposon mais simples, carrega essencialmente apenas o gene da transposase e suas extremidades de reconhecimento])), que carregam pouco mais que o gene da transposase; os mais complexos, os transposons compostos (designados *Tn*, como Tn3, Tn5 e Tn2571), carregam genes adicionais — frequentemente, de novo, *resistência a antibióticos*. O Tn3 confere resistência à ampicilina, o Tn5 à canamicina, e o Tn2571 a múltiplos antibióticos de uma vez.

O detalhe que dá a dimensão do fenômeno: elementos transponíveis compõem uma fração enorme do nosso próprio genoma — bem maior do que a fração que de fato codifica proteínas. A maioria está hoje "domesticada" (não salta mais), mas a marca evolutiva dos saltos está espalhada por todo o DNA humano.

#confusao-prevista(
  titulo: "Transposon não é o mesmo que plasmídeo",
  aluno_acha: [como ambos se movem e ambos podem carregar resistência, o aluno tende a juntar os dois numa coisa só.],
  mecanismo: [o *plasmídeo* é uma molécula circular independente que se move *entre células* (por conjugação); o *transposon* é um segmento que se move *dentro de um genoma*, saltando de um ponto a outro do mesmo DNA (ou para um plasmídeo). Um viaja entre células; o outro muda de endereço dentro da célula. Eles podem cooperar: um transposon de resistência que pula para um plasmídeo conjugativo passa a viajar de bactéria em bactéria.],
)

#subtopico("3.3 — Vírus, fago lambda e recombinação sítio-específica")

O terceiro tipo de DNA móvel chega de fora: o *vírus*. Um vírus não tem maquinaria própria para se reproduzir; sua única estratégia é colocar seu material genético dentro de uma célula hospedeira e sequestrar a maquinaria dela. Os vírus que infectam bactérias chamam-se *bacteriófagos* (ou simplesmente fagos), e o fago lambda (λ), que infecta _E. coli_, é o modelo onde tudo isso foi desvendado. A partir da infecção, o fago pode seguir por *dois caminhos* distintos — e a comparação entre eles é o coração deste subtópico.

No *ciclo lítico*, o fago vai direto ao ataque: usa a maquinaria da bactéria para fabricar centenas de cópias de si mesmo, monta novas partículas virais e, no fim, *rompe (lisa) a célula*, liberando a progênie para infectar vizinhas. É rápido e mata o hospedeiro. No *ciclo lisogênico*, o fago faz o oposto: em vez de se replicar logo, ele *integra seu DNA ao cromossomo bacteriano* e fica quieto, passando a se chamar #termo-nota[prófago][DNA de um fago integrado ao cromossomo da bactéria hospedeira, que se replica junto com ela e permanece latente até ser eventualmente induzido ao ciclo lítico]. Nesse estado de #termo-nota[lisogenia][estado em que o fago permanece latente, integrado como prófago ao genoma do hospedeiro, replicando-se passivamente com a célula], o DNA viral é copiado passivamente toda vez que a bactéria se divide, herdado por todas as descendentes — até que um sinal de estresse (por exemplo, dano ao DNA por UV) o "desperta" e o empurra de volta para o ciclo lítico.

#align(center, block(width: 92%, stroke: 0.5pt + gray-border, inset: 10pt, radius: 4pt, fill: gray-bg,
  stack(spacing: 7pt,
    text(size: 9pt, weight: "bold", fill: navy)[Dois destinos do fago lambda após infectar a bactéria],
    grid(columns: (1fr, 1fr), column-gutter: 9pt,
      stack(spacing: 6pt,
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + red-alert, text(size: 8.5pt, weight: "bold", fill: red-alert)[CICLO LÍTICO]),
        align(center, text(size: 11pt, fill: navy)[↓]),
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border, text(size: 8.5pt)[fago usa a maquinaria da célula e fabrica centenas de cópias]),
        align(center, text(size: 11pt, fill: navy)[↓]),
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border, text(size: 8.5pt)[monta novas partículas virais]),
        align(center, text(size: 11pt, fill: navy)[↓]),
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border, text(size: 8.5pt)[*lisa a bactéria* e libera a progênie]),
      ),
      stack(spacing: 6pt,
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + teal, text(size: 8.5pt, weight: "bold", fill: teal)[CICLO LISOGÊNICO]),
        align(center, text(size: 11pt, fill: navy)[↓]),
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border, text(size: 8.5pt)[DNA do fago se integra ao cromossomo (sítio attB)]),
        align(center, text(size: 11pt, fill: navy)[↓]),
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border, text(size: 8.5pt)[vira *prófago* e replica-se junto com a célula]),
        align(center, text(size: 11pt, fill: navy)[↓ (estresse / UV)]),
        rect(width: 100%, inset: 6pt, radius: 3pt, fill: white, stroke: 0.5pt + gray-border, text(size: 8.5pt)[é *induzido* e pode entrar no ciclo lítico]),
      ),
    ),
  )))

A integração do lambda não acontece em qualquer lugar do cromossomo: ela ocorre num ponto específico, próximo ao gene de utilização da galactose, chamado *sítio attB*. Esse tipo de inserção, que reconhece uma sequência-alvo precisa, é a #termo-nota[recombinação sítio-específica][troca/integração de DNA que ocorre entre sequências específicas e reconhecíveis, como a integração do fago lambda no sítio attB — diferente da recombinação homóloga, que depende de longas regiões de similaridade]. É aqui que o título da aula fecha: *recombinação* é o nome geral para o rearranjo de material genético — e a integração precisa do lambda no attB é o exemplo mais limpo dela, ligando o tema dos elementos móveis ao da recombinação propriamente dita.

#conclusao-box[
  Os três atos contam uma só história sobre a *sequência de bases como informação que pode mudar*. Na PARTE I, vimos a informação ser *corrompida* — por erro espontâneo (tautômeros, deaminação) ou por agentes externos (análogos de base, UV gerando dímeros de pirimidina) —, e como substituição, inserção e deleção alteram a proteína final, sendo o frameshift o mais destrutivo. Na PARTE II, vimos a célula *defender* essa informação: reparo direto (fotoliase, MGMT) que desfaz a lesão no lugar, e reparo por excisão (NER/uvrABC) que recorta e reconstrói pela fita-molde; e vimos o preço da falha — xeroderma pigmentoso e câncer, quando o reparo não existe.

  Na PARTE III, a informação deixou de ser estática e passou a *viajar*: plasmídeos que pulam entre bactérias por conjugação, transposons que saltam dentro do genoma, vírus que se integram como prófagos — todos espalhando características novas, a resistência a antibióticos à frente delas, e todos remetendo à recombinação, o rearranjo do material genético. O princípio unificador: *mutação e mobilidade são as duas formas de a informação genética mudar* — uma ameaça (câncer, infecção resistente) e, ao mesmo tempo, o motor da variabilidade que a evolução e a biotecnologia exploram. Esse mesmo mecanismo de mover e recombinar DNA de forma controlada é o que a próxima aula transforma em ferramenta: a *tecnologia do DNA recombinante*, em que cortamos, colamos e clonamos sequências à vontade.
]
