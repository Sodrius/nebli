#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Uma *Escherichia coli* carrega cerca de 4.400 genes e não expressa nem metade deles ao mesmo tempo. Produzir uma enzima que não terá substrato custa nucleotídeo, aminoácido e tempo de ribossomo — e, numa população que dobra a cada vinte minutos, esse desperdício é eliminado pela competição. A regulação da expressão gênica é o mecanismo pelo qual a bactéria transcreve apenas o que o ambiente daquele momento justifica.

A *PARTE I* monta a gramática: onde no fluxo do gene o controle é exercido, quais são as quatro combinações possíveis entre proteína reguladora e sinal químico, e o que define um operon como unidade. A *PARTE II* aplica essa gramática ao operon da lactose — os cinco elementos que o compõem, o repressor como sensor alostérico, e o raciocínio genético com que Jacob e Monod deduziram uma proteína que ninguém tinha visto. A *PARTE III* fecha o circuito com o promotor, o ativador CAP e a integração dos dois açúcares numa única decisão.
]

#parte-title("PARTE I — A gramática da regulação bacteriana", primeira: true)

#subtopico("1.1 — Onde o controle acontece, e por que na largada da transcrição")

O caminho que vai do gene à proteína oferece quatro pontos de intervenção, e a bactéria usa todos. O controle *transcricional* decide se o #sigla("mRNA", [RNA mensageiro — o transcrito que carrega a informação do gene até o ribossomo]) chega a ser sintetizado; o *pós-transcricional* age sobre a estabilidade e o processamento desse transcrito; o *traducional* regula a frequência com que o ribossomo o lê; o *pós-traducional* modifica a proteína já pronta, por fosforilação, clivagem ou degradação dirigida. Quanto mais cedo no fluxo o controle atua, menos recurso se gasta antes de a decisão ser tomada — e é por isso que a iniciação da transcrição é o ponto preferido.

As camadas posteriores não são redundância. Elas são mais *rápidas*: uma enzima já sintetizada pode ser inibida alostericamente em milissegundos, ao passo que desligar a transcrição só reduz a proteína depois que as moléculas existentes forem diluídas ou degradadas. Economia e velocidade são exigências diferentes, e cada camada atende a uma delas.

Regular a iniciação exige endereços fixos no #sigla("DNA", [ácido desoxirribonucleico — o polímero que armazena a informação genética]). Três marcas pontuam a unidade de transcrição: o *promotor*, sequência à montante onde a #sigla("RNAP", [RNA-polimerase — a enzima que sintetiza RNA a partir do molde de DNA]) se posiciona; o *sítio de início*, chamado +1, que é o primeiro nucleotídeo efetivamente transcrito e serve de referência para toda a numeração da região; e o *terminador*, sequência que encerra a síntese. A numeração corre para trás a partir do +1, sem posição zero, de modo que −35 significa trinta e cinco bases à montante do início.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-04.png",
  largura: 55%,
  legenda: [Promotor, +1 e terminador delimitam o transcrito, não o gene. Num operon, o intervalo entre +1 e terminador abriga vários genes de uma vez.])

Duas particularidades bacterianas explicam por que o controle da largada basta. A primeira é a meia-vida do mRNA, da ordem de poucos minutos — contra horas ou dias no mRNA de células eucarióticas. A segunda é o acoplamento entre transcrição e tradução: sem envoltório nuclear separando os compartimentos, o ribossomo se acopla à extremidade 5' do transcrito enquanto a polimerase ainda sintetiza a extremidade 3'. As duas somadas fazem com que fechar a torneira na transcrição derrube a concentração da proteína em minutos, sem necessidade de uma maquinaria dedicada de destruição.

#mini-resumo[mRNA de vida curta + tradução acoplada à transcrição → o que se decide na iniciação vira fenótipo em minutos. Por isso o ponto de controle mais usado é o primeiro.]

Falta desfazer uma leitura binária. A regulação não liga e desliga um gene: ela ajusta a *frequência de iniciação*, o número de polimerases que partem do promotor por unidade de tempo. Existe um nível basal de transcrição mesmo sem estímulo nenhum, e as proteínas reguladoras deslocam essa taxa para baixo ou para cima em ordens de grandeza. Repressão e ativação são desvios em torno de um valor que nunca é zero — e a PARTE II mostra que, no operon lac, essa fração residual não é vazamento inútil: é o que torna o sistema capaz de perceber a lactose.

#subtopico("1.2 — Repressor, ativador, indutor e co-repressor: as quatro combinações")

O erro que mais atrapalha aqui é supor que o sinal químico do ambiente age diretamente sobre o gene. Ele não age. O sinal se liga a uma *proteína reguladora*, muda a conformação dela e altera a afinidade dessa proteína pelo DNA; o efeito sobre a transcrição é sempre indireto, mediado pela proteína.

As proteínas reguladoras vêm em dois tipos. O *repressor* se liga a um sítio no DNA e impede a transcrição — é a regulação *negativa*. O *ativador* se liga a um sítio próprio e facilita a transcrição, recrutando a polimerase — é a regulação *positiva*. Os adjetivos descrevem o que a proteína faz, não o estado atual do gene: um operon sob controle negativo passa a maior parte do tempo ligado se o sinal que desativa o repressor estiver sempre presente.

Os sinais também vêm em dois tipos, definidos pelo efeito alostérico que produzem. O *indutor* é o metabólito cuja ligação faz a proteína reguladora *soltar* o DNA; o *co-repressor* é o metabólito cuja ligação faz a proteína reguladora *aderir* ao DNA. Cruzando os dois eixos, saem quatro arranjos lógicos, e cada um resolve um problema biológico distinto.

#table(
  columns: (auto, auto, 1fr),
  inset: 7pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Arranjo]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Sinal]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[O que acontece no DNA]],
  ),
  [Negativa induzível], [indutor], [repressor ocupa o operador e bloqueia; o indutor o dissocia e libera a transcrição],
  [Negativa repressível], [co-repressor], [repressor sozinho é inativo; o co-repressor o ativa e ele passa a bloquear],
  [Positiva induzível], [indutor], [ativador sozinho não liga ao DNA; o indutor o habilita e ele recruta a polimerase],
  [Positiva repressível], [co-repressor], [ativador está ligado e recrutando; o co-repressor o dissocia e a taxa cai],
)

A lógica encaixa no tipo de via metabólica. Vias *catabólicas*, que degradam um nutriente, costumam ser negativas induzíveis: o próprio nutriente é o indutor, e as enzimas só aparecem quando há o que degradar — é o caso do operon da lactose, tratado na PARTE II. Vias *anabólicas*, que sintetizam um metabólito, costumam ser negativas repressíveis: o produto final é o co-repressor, e a célula desliga a fábrica quando o produto já abunda. No operon do triptofano, o próprio triptofano acumulado se liga ao repressor e o torna capaz de ocupar o operador — a via se desliga por excesso do que ela mesma produz.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-08.png",
  largura: 58%,
  legenda: [Regulação negativa induzível. O indutor não toca no DNA nem na polimerase: ele se liga ao repressor e o retira do operador. Quem transcreve é a RNAP, que estava impedida.])

#atencao-box("Indutor não liga o gene — ele desliga o freio", [
A frase "o indutor ativa o operon" produz um modelo errado que estraga tudo o que vem depois. Numa regulação negativa induzível, o indutor tem *um único alvo*: a proteína repressora. Ele muda a conformação dela, a afinidade pelo operador despenca, o repressor se solta e a polimerase — que já estava no promotor — deixa de ser impedida.

A consequência prática é direta: se o repressor estiver ausente por mutação, o operon fica ligado *sem* indutor nenhum. Um sistema que precisasse do indutor para ser ativado ficaria mudo nesse mutante; um sistema em que o indutor apenas remove o freio fica permanentemente ligado. É esse contraste que a genética de Jacob e Monod explorou.
])

#subtopico("1.3 — Operon, cis e trans: a unidade que a bactéria transcreve de uma vez")

Com a gramática dos reguladores montada, o passo seguinte é o arranjo físico dos genes. Um #termo-nota[operon][conjunto de genes contíguos sob um único promotor, transcritos num mesmo mRNA e codificando proteínas de função relacionada] agrupa, numa mesma unidade de transcrição, genes cujas proteínas trabalham na mesma via. Uma decisão única no promotor governa o conjunto inteiro, e as enzimas aparecem juntas e em proporção aproximadamente fixa — exatamente o que uma via metabólica exige.

O transcrito que sai é #termo-nota[policistrônico][um único mRNA contendo vários cístrons, isto é, várias regiões codificantes independentes], e a tradução dele não gera uma proteína gigante depois cortada em pedaços. Cada cístron carrega seu próprio *sítio de ligação do ribossomo*, a sequência de poucos nucleotídeos à montante do códon de início que posiciona o ribossomo; cada um tem códon de início e códon de parada próprios. De um transcrito saem proteínas separadas, e a eficiência de cada sítio determina quanto de cada uma.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-07.png",
  largura: 55%,
  legenda: [Mapa geral. Sítio do ativador, promotor e operador são endereços no DNA — atuam em cis. Repressor e ativador são proteínas difusíveis — atuam em trans. Os genes estruturais A, B e C saem num mRNA policistrônico único.])

A distinção decisiva do subtópico separa dois tipos de elemento regulatório. Elementos que atuam em *cis* são sequências de DNA — promotor, operador, sítio do ativador — e influenciam apenas os genes situados na *mesma molécula* de DNA em que se encontram, porque não são difusíveis: existem como endereço, não como objeto que circula. Elementos que atuam em *trans* são produtos gênicos difusíveis — as proteínas reguladoras — e alcançam qualquer cópia do sítio-alvo, esteja ela onde estiver na célula.

O gene que codifica a proteína reguladora é o *gene regulador*, e ele tem promotor próprio, independente do operon que controla. Sua posição no genoma é indiferente ao funcionamento: no operon lac ele calha de estar imediatamente ao lado, mas poderia estar em qualquer outro ponto do cromossomo sem alterar o resultado, justamente porque seu produto atua em trans.

#mini-resumo[Cis é endereço e só vale na própria molécula de DNA; trans é produto difusível e vale em todas. A posição de um gene regulador não importa; a de um operador importa inteiramente.]

Essa diferença tem consequência experimental imediata, e é ela que a PARTE II explora: numa célula construída com *duas cópias* da mesma região, a lesão em elemento cis segue se manifestando na cópia defeituosa, enquanto a lesão em gene regulador é corrigida pelo produto difusível da cópia boa. Jacob e Monod construíram essa célula e leram nela a arquitetura do operon.

#parte-title("PARTE II — O operon lac: a máquina e a lógica genética que a revelou")

#subtopico("2.1 — Os cinco elementos do operon lac e o açúcar que eles processam")

O operon lac funciona como uma linha de produção com um único interruptor na entrada: um comando governa três máquinas que só fazem sentido juntas. As máquinas são os *genes estruturais*. O *lacZ* codifica a #termo-nota[β-galactosidase][enzima que hidrolisa a ligação β-1,4 da lactose, liberando glicose e galactose, e que também transgalactosila parte do substrato em alolactose], com cerca de 3.510 pares de base — de longe o maior dos três. O *lacY* codifica a *permease*, transportador de membrana que traz lactose para dentro em simporte com um próton, aproveitando a força próton-motriz acumulada na membrana. O *lacA* codifica a *transacetilase*, que transfere um grupo acetil da acetil-CoA para galactosídeos que a célula não consegue metabolizar, marcando-os para excreção — função de destoxificação, não de catabolismo.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-15.png",
  largura: 72%,
  legenda: [O operon lac com tamanhos reais em pares de base. lacI tem promotor próprio (P) e terminador próprio; o conjunto PO governa lacZ, lacY e lacA, que saem num único transcrito.])

Os outros dois elementos são regulatórios e atuam em cis. O *promotor lac*, ou P#sub[lac], é onde a RNAP se posiciona; o *operador*, sequência de vinte e um #sigla("pb", [pares de base — unidade de comprimento de uma sequência de DNA de fita dupla]) que sobrepõe o sítio de início da transcrição, é onde o repressor se liga. Somando o gene regulador *lacI*, com promotor próprio e expressão constitutiva baixa, fecham-se os cinco componentes que descrevem o sistema: lacI, promotor, operador, sítio CAP — apresentado na PARTE III — e os genes estruturais.

#figura-lateral("/figuras/biomol-05-operon-procariotos/slide-17.png",
  lado: "right",
  largura-figura: 40%,
  texto: [A lactose é um dissacarídeo que a célula não consegue oxidar diretamente. A permease a traz para o citoplasma; a β-galactosidase corta a ligação glicosídica e entrega *glicose*, que entra na glicólise, e *galactose*, que é convertida a glicose-1-fosfato pela via de Leloir antes de seguir o mesmo destino. Numa fração das reações, em vez de hidrolisar, a enzima transfere a galactose para outra posição da glicose e produz *alolactose*.],
  legenda: [Metabolismo da lactose em *E. coli*.])

Essa reação lateral é o ponto que costuma passar despercebido e que sustenta o sistema inteiro: *o indutor fisiológico do operon lac não é a lactose, é a alolactose* — isômero produzido pela própria β-galactosidase. O sinal que liga o operon é, portanto, fabricado por uma das enzimas que o operon codifica.

Daí decorre uma exigência que fecha o subtópico. Para que exista alolactose, é preciso que já haja alguma permease trazendo lactose e alguma β-galactosidase convertendo parte dela. É por isso que o nível basal de transcrição da seção 1.1 não é desperdício: as poucas moléculas produzidas sob repressão são o sensor que permite ao sistema perceber que a lactose chegou. Um operon reprimido a zero absoluto nunca seria induzido, porque o indutor jamais apareceria.

#subtopico("2.2 — LacI: um sensor alostérico que solta o DNA quando encontra o indutor")

O produto de lacI é uma proteína de 36 kDa por subunidade que se organiza como *tetrâmero* — dois dímeros unidos por um domínio de tetramerização em hélice. A arquitetura tem três regiões com funções distintas: um domínio de ligação ao DNA na porção N-terminal, uma dobradiça que o conecta ao resto, e um *core* que carrega o sítio de ligação do indutor.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-30.png",
  largura: 52%,
  legenda: [Monômero e tetrâmero de LacI. Os dois domínios de ligação ao DNA no topo pertencem a um dímero; o sítio do indutor (estrela) fica no core, distante deles.])

O domínio de ligação ao DNA é do tipo #termo-nota[hélice-volta-hélice][motivo de duas α-hélices separadas por uma volta curta, em que a segunda hélice se encaixa no sulco maior do DNA e lê as bases por contatos diretos], abreviado #sigla("HTH", [helix-turn-helix — o motivo hélice-volta-hélice de ligação ao DNA]). Como quem lê o operador é um dímero, com dois HTH simétricos entrando em voltas sucessivas do sulco maior, a sequência do operador é um #termo-nota[palíndromo][sequência que se lê igual nas duas fitas quando ambas são lidas no sentido 5'→3', o que permite a ligação simétrica de um dímero proteico]. A simetria da proteína e a simetria da sequência são o mesmo fato, visto de dois lados.

A ligação do indutor ocorre no core, longe do DNA — não há competição por sítio. A alolactose se encaixa, o core muda de conformação, a mudança se propaga pela dobradiça e desalinha os dois HTH, que deixam de encaixar simultaneamente no sulco maior. A afinidade pelo operador cai cerca de mil vezes e o repressor se solta em segundos.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-32.png",
  largura: 60%,
  legenda: [À esquerda, os dois domínios de ligação encaixados em voltas sucessivas do sulco maior. À direita, o indutor ocupa o core e desorganiza o encaixe. O repressor é uma proteína alostérica que funciona como sensor do ambiente.])

Com o repressor no operador, a RNAP ainda consegue se ligar ao promotor: o que ela não consegue é escapar para a fase de alongamento, porque o operador cobre justamente a região que ela precisaria atravessar logo após o +1. A repressão é *estérica*, e é por isso que ela reduz a transcrição em cerca de mil vezes sem levá-la a zero.

O grau de repressão real é ainda maior do que um único sítio explicaria, e a razão é geométrica. Além do operador principal, o operon carrega dois operadores auxiliares, um à montante e outro dentro de lacZ. Um tetrâmero pode ocupar dois deles ao mesmo tempo, com um dímero em cada, dobrando o DNA intermediário numa *alça*. A alça aumenta a concentração local do repressor sobre o operador principal e multiplica a repressão muito além do que a soma dos sítios isolados daria — mecanismo de cooperatividade que reaparece em praticamente todos os sistemas regulatórios com sítios múltiplos.

#mini-resumo[Indutor entra no core → conformação muda → HTH desalinha → afinidade pelo operador cai mil vezes → RNAP escapa do promotor. O DNA nunca é tocado pelo açúcar.]

#subtopico("2.3 — Jacob e Monod: mutantes, diploide parcial e o repressor deduzido")

Quando o modelo do operon foi proposto, em 1960, ninguém tinha isolado repressor nenhum. Jacob e Monod chegaram à arquitetura inteira por genética e lógica, partindo de um fenômeno de bancada: a β-galactosidase só aparecia em cultura quando havia lactose no meio. O fenômeno recebeu o nome de *inducibilidade*, e a molécula que o desencadeava, o nome de indutor.

O passo decisivo foi isolar mutantes que perdiam essa resposta, em duas direções opostas. Os *não induzíveis* não produziam β-galactosidase nem com lactose presente. Os *constitutivos* produziam sempre, com ou sem lactose. Cada fenótipo é compatível com mais de uma lesão molecular, e é essa ambiguidade que o experimento seguinte resolveu.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-21.png",
  largura: 55%,
  legenda: [A curva selvagem: β-galactosidase praticamente ausente até a lactose entrar, e produção crescente depois. A linha superior é o mutante constitutivo, alto desde o início; a inferior, o não induzível, que nunca sobe.])

Duas ferramentas químicas separaram os candidatos. O #termo-nota[IPTG][isopropil-β-D-tiogalactosídeo — análogo estrutural da alolactose que induz o operon e não é hidrolisado pela β-galactosidase] induz o sistema sem ser consumido, mantendo a indução constante e desacoplando o papel de indutor do papel de substrato. O #termo-nota[X-Gal][5-bromo-4-cloro-3-indolil-β-D-galactosídeo — substrato cromogênico que, ao ser clivado pela β-galactosidase, libera um indol que se oxida em pigmento azul insolúvel] revela a atividade enzimática pela cor da colônia: azul quando há β-galactosidase ativa, branca quando não há.

A peça final foi o #termo-nota[diploide parcial][célula bacteriana que recebe, por conjugação, um segundo exemplar apenas de uma região do genoma, ficando com duas cópias dessa região e uma só do restante], também chamado merozigoto. Introduzindo uma segunda cópia intacta do operon numa célula mutante, o comportamento da mutação revela sua natureza. Numa célula lacI⁻, a cópia selvagem restaura a repressão: o repressor produzido por ela difunde e ocupa os dois operadores. A mutação é *recessiva* e atua em *trans*. Numa célula com operador mutante O#super[c], que não reconhece mais o repressor, a cópia selvagem não resolve nada: o operon defeituoso continua constitutivo, porque o operador só governa a molécula em que está. A mutação é *dominante* e atua em *cis*.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-29.png",
  largura: 62%,
  legenda: [No diploide parcial, o repressor produzido pelas duas cópias reprime a molécula de operador íntegro, mas não a de O#super[c] — que segue expressando lacZ, lacY e lacA. A mutação se manifesta com o gene selvagem presente: é dominante, e age só em cis.])

Um terceiro genótipo completa o quadro. O alelo lacI#super[S] produz um repressor que se liga bem ao operador mas perdeu afinidade pelo indutor: ele nunca solta, e o fenótipo é não induzível. Ele é *dominante* porque as subunidades mutantes se misturam às selvagens ao formar tetrâmeros, e basta uma subunidade defeituosa para comprometer o complexo — o mecanismo geral do efeito dominante-negativo.

#clinica-box("Do operon à bancada de diagnóstico e à produção de fármacos", [
Os dois reagentes de Jacob e Monod continuam em uso diário. O rastreio *azul-branco* de clonagem molecular insere o fragmento de DNA de interesse dentro do gene lacZ de um plasmídeo: quando a inserção ocorre, lacZ é interrompido, não há β-galactosidase e a colônia cresce branca; quando não ocorre, a enzima é produzida sobre o X-Gal e a colônia cresce azul. A leitura da cor identifica, sem sequenciar nada, quais bactérias receberam o inserto — e essa é a etapa de triagem em painéis de diagnóstico molecular e na construção de vetores.

O IPTG sustenta o outro uso. Vetores de expressão colocam o gene de uma proteína humana sob controle do promotor lac ou de suas versões híbridas; a cultura cresce até alta densidade com o operon reprimido, e só então se adiciona IPTG para disparar a produção em massa. Insulina humana recombinante, hormônio de crescimento e diversas enzimas terapêuticas são fabricados por esse esquema, que depende de uma propriedade específica do IPTG: por não ser hidrolisado, sua concentração não cai durante a indução, e a expressão se mantém estável até o fim do cultivo.
])

#parte-title("PARTE III — Ligar de verdade: promotor, ativador e a integração dos dois açúcares")

#subtopico("3.1 — A anatomia do promotor bacteriano e a força que ele carrega")

Tirar o repressor do operador é condição necessária para transcrever, mas não é condição suficiente — e o motivo está na sequência do promotor. O promotor bacteriano é composto de dois blocos curtos e conservados, situados à montante do +1 e nomeados pela posição: a região *−35*, de seis bases, e a região *−10*, também de seis. Entre elas há um espaçador de cerca de dezessete pb cuja sequência varia livremente, mas cujo *comprimento* é crítico: ele posiciona os dois blocos na mesma face da dupla-hélice, e alterá-lo em poucas bases reduz a iniciação mesmo com os dois blocos perfeitos.

Quem reconhece esses blocos não é o core da polimerase, mas a subunidade *σ*, fator dissociável que se associa ao core e converte a enzima em holoenzima capaz de distinguir promotor de DNA qualquer. Cada σ reconhece um conjunto próprio de promotores, e a bactéria mantém vários: o σ⁷⁰ atende aos genes de manutenção, enquanto fatores alternativos, ativados em choque térmico ou privação de nutriente, redirecionam a mesma polimerase para programas gênicos inteiramente diferentes. Trocar o leitor equivale a trocar o repertório transcrito, sem tocar em nenhum gene.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-33.png",
  largura: 75%,
  legenda: [A pegada das duas proteínas sobre a mesma região. A RNAP cobre de cerca de −45 a pouco depois do +1; o repressor cobre a partir do +1 para a frente. Os dois sítios se sobrepõem, e é essa sobreposição que torna a repressão estérica.])

As sequências ideais de cada bloco não são as de um promotor real, e sim uma #termo-nota[sequência consenso][a base mais frequente em cada posição, calculada sobre o conjunto de promotores conhecidos; nenhum promotor individual precisa coincidir com ela] — TTGACA em −35 e TATAAT em −10. Promotores reais divergem do consenso, e a divergência é o que gradua a *força*: quanto mais próxima do consenso, maior a afinidade pela holoenzima e maior a frequência de iniciação.

O promotor lac diverge nas duas regiões. Onde o consenso pede TTGACA, ele tem TTTACA; onde pede TATAAT, ele tem TATGTT. O resultado é um promotor *fraco*: mesmo com o operador livre, a polimerase inicia com frequência baixa.

#confusao-prevista(
  titulo: "Promotor fraco não é promotor defeituoso",
  aluno_acha: [que a divergência do promotor lac em relação ao consenso é uma imperfeição que a bactéria não conseguiu corrigir],
  mecanismo: [a fraqueza é a condição de possibilidade da regulação. Um promotor idêntico ao consenso iniciaria em taxa máxima assim que o repressor saísse, e a célula perderia o segundo eixo de controle. É exatamente porque o promotor lac inicia mal sozinho que um ativador tem espaço para fazer diferença — e é isso que permite ao operon obedecer, ao mesmo tempo, à lactose e à glicose.],
)

#subtopico("3.2 — CAP-cAMP: o ativador que compensa um promotor fraco de propósito")

O ativador que ocupa esse espaço é a *CAP*, sigla de #sigla("CAP", [catabolite activator protein — proteína ativadora por catabólito, também chamada CRP, cyclic AMP receptor protein]), um dímero que se liga a um sítio próprio situado à montante do promotor lac, na direção oposta à do operador. A geometria importa: o operador fica à jusante, sobre o +1, e bloqueia; o sítio CAP fica à montante, adjacente ao −35, e recruta.

O mecanismo de ativação é contato proteína–proteína. A CAP ligada ao seu sítio toca o domínio C-terminal da subunidade α da RNA-polimerase, e a energia livre favorável dessa interação se soma à ligação fraca da holoenzima ao promotor imperfeito. O que faltava em afinidade de sequência é fornecido por afinidade de proteína — e a transcrição sobe cerca de cinquenta vezes acima do nível que o promotor alcançaria sozinho.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-36.png",
  largura: 62%,
  legenda: [O sítio CAP fica à montante das regiões −35 e −10. A alça do domínio C-terminal da subunidade α alcança a CAP ligada, e é esse contato que compensa a imperfeição do promotor lac.])

A CAP, porém, não se liga ao DNA sozinha. Ela só assume a conformação competente quando complexada ao #sigla("cAMP", [adenosina monofosfato cíclico — nucleotídeo sinalizador sintetizado pela adenilato-ciclase]); sem o nucleotídeo, circula inerte pelo citoplasma. O nível de cAMP é, portanto, o sinal que a CAP lê — e em *E. coli* esse nível é inversamente proporcional à disponibilidade de glicose: glicose baixa produz cAMP alto, glicose alta produz cAMP baixo.

O mecanismo dessa inversão está no transporte da glicose. A glicose entra pelo #termo-nota[sistema fosfotransferase][PTS — cadeia de proteínas que fosforila a glicose durante a própria travessia da membrana, usando fosfoenolpiruvato como doador do grupo fosfato] e, ao atravessar, consome o fosfato da proteína EIIA#super[Glc], que fica desfosforilada enquanto houver glicose entrando. A EIIA#super[Glc] fosforilada é o que estimula a adenilato-ciclase; desfosforilada, ela deixa de estimular, e o cAMP despenca. O mesmo intermediário produz um segundo efeito: a EIIA#super[Glc] desfosforilada se liga à permease lacY e inibe a entrada de lactose — fenômeno conhecido como *exclusão do indutor*. A glicose, assim, ataca o operon lac por dois flancos, sem jamais tocar no repressor.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-37.png",
  largura: 55%,
  legenda: [A CAP só adquire a conformação capaz de reconhecer o sítio quando o cAMP se encaixa. Como o cAMP sobe apenas na ausência de glicose, a CAP funciona como um sensor indireto do açúcar preferido.])

#mini-resumo[Glicose entra pelo PTS → EIIA#super[Glc] fica desfosforilada → adenilato-ciclase não é estimulada → cAMP cai → CAP não liga ao DNA → promotor lac fraco não é compensado. Essa cadeia é a repressão por catabólito.]

#subtopico("3.3 — Glicose × lactose: quatro ambientes, uma porta lógica")

Os dois eixos de controle são independentes e leem sinais diferentes: o repressor lê a lactose, a CAP lê a falta de glicose. Combinados, produzem uma decisão que se comporta como uma porta lógica — a saída só é alta quando *as duas* condições são satisfeitas ao mesmo tempo.

#table(
  columns: (auto, auto, auto, 1fr),
  inset: 7pt,
  align: left,
  stroke: 0.5pt + gray-border,
  table.header(
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Glicose]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Lactose]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Estado]],
    table.cell(fill: navy)[#text(fill: white, weight: "bold")[Por quê]],
  ),
  [alta], [ausente], [basal], [repressor no operador; cAMP baixo e CAP inativa],
  [alta], [presente], [basal], [operador livre, mas sem CAP o promotor fraco inicia pouco],
  [baixa], [ausente], [basal], [CAP ativa e pronta, mas o repressor continua bloqueando],
  [baixa], [presente], [máximo], [operador livre e CAP recrutando a polimerase],
)

A linha que mais engana é a segunda. Com os dois açúcares disponíveis, o repressor sai do operador — há alolactose — e o aluno espera expressão. Mas o cAMP está baixo, a CAP não se ligou, o promotor imperfeito inicia com frequência baixa, e a transcrição fica próxima do nível basal. Retirar o freio não equivale a pisar no acelerador.

#figura-nebli("/figuras/biomol-05-operon-procariotos/slide-35.png",
  largura: 65%,
  legenda: [Os três estados que o operon assume. Em cima, nível basal; no meio, repressão pelo repressor no operador; embaixo, ativação plena, com CAP recrutando a polimerase e o operador vazio.])

O fenótipo de crescimento que essa lógica produz tem nome. Numa cultura com glicose e lactose, a bactéria consome primeiro a glicose e cresce; quando a glicose acaba, o crescimento estaciona por algum tempo, e só depois recomeça sobre a lactose. A curva bifásica é a #termo-nota[diauxia][padrão de crescimento em duas fases separadas por um platô, observado quando a bactéria esgota o açúcar preferido antes de reprogramar a expressão para o segundo], e o platô é o intervalo em que o cAMP sobe, a CAP se liga e as enzimas do operon são sintetizadas do zero. O tempo perdido no platô é o preço de não manter enzimas prontas para um substrato que talvez não apareça.

#clinica-box("A mesma lógica em genes que decidem uma infecção", [
O arranjo que o operon lac ilustra não é uma curiosidade de laboratório: é a forma padrão pela qual bactérias patogênicas ajustam o que expressam ao ambiente que encontram no hospedeiro. Genes de aquisição de ferro, de adesinas e de toxinas ficam sob operons reprimidos enquanto o sinal correspondente está ausente, e são desreprimidos quando a bactéria alcança o tecido em que aquele programa é útil — a mesma arquitetura de sítio operador e proteína reguladora difusível.

O caso com consequência terapêutica mais direta é o das β-lactamases induzíveis de certas enterobactérias. O gene da enzima que hidrolisa o antibiótico permanece sob repressão até que fragmentos de parede celular, gerados pela própria ação do β-lactâmico, funcionem como indutores e dissociem o repressor. O resultado é um isolado que se comporta como sensível no teste inicial e passa a resistente durante o tratamento — não por mutação nova, mas por indução de um operon que sempre esteve lá. Reconhecer que resistência pode ser um fenômeno *regulatório*, e não apenas genético, muda a leitura do resultado de laboratório.
])

#conclusao-box[
*O princípio que unifica a aula* é que a bactéria não decide por gene, decide por *unidade transcricional* — e a decisão é tomada por proteínas difusíveis que leem metabólitos e se ligam a endereços fixos no DNA. Toda a complexidade do operon lac se reduz a essa frase: dois sensores proteicos, dois sítios de DNA, um promotor.

*O mecanismo nuclear* é a alosteria aplicada à afinidade por DNA. A alolactose entra no core de LacI e derruba mil vezes a afinidade do tetrâmero pelo operador; o cAMP entra na CAP e cria a conformação que reconhece o sítio ativador. Nos dois casos, um metabólito pequeno é convertido em decisão transcricional pela mudança de forma de uma proteína — e a separação entre o sítio do ligante e o sítio do DNA é o que permite ao mesmo mecanismo funcionar nos dois sentidos, dissociando um regulador e associando o outro.

*A clínica retomada* mostra a mesma máquina em dois papéis. Na bancada, o operon virou ferramenta: X-Gal lê atividade de lacZ na triagem azul-branco, e IPTG dispara a produção de proteína recombinante em vetores sob promotor lac. No paciente, a mesma arquitetura opera contra o tratamento, quando um β-lactâmico induz o operon da β-lactamase e converte, ao longo dos dias, um isolado sensível em resistente.

*A projeção* aponta para o eucarioto. Lá, os genes não se agrupam em operons, o mRNA é monocistrônico, a cromatina precisa ser aberta antes de qualquer polimerase chegar, e os elementos cis podem estar a dezenas de milhares de pares de base do promotor. O que permanece idêntico é o núcleo do que se aprendeu aqui: sequência reguladora no DNA, proteína difusível que a lê, ligante que muda a forma dessa proteína.
]
