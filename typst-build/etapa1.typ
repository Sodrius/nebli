#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  O corpo humano fabrica mais de um trilhão de anticorpos diferentes com um genoma que tem cerca de vinte e cinco mil genes. Essa frase, sozinha, é o assunto inteiro desta apostila: ela descreve uma impossibilidade aritmética, e o que vem a seguir é a explicação de como a célula B a resolve. A saída não foi guardar um gene para cada alvo — foi guardar *peças* e montar o gene do anticorpo de novo, por corte e religação do próprio DNA, em cada célula B que nasce. O caminho aqui tem três trechos. Primeiro, o problema: o que um anticorpo precisa reconhecer, como ele é feito e por que a conta não fecha com um gene por anticorpo. Depois, a máquina que resolve: a recombinação V(D)J, das sequências que marcam onde cortar até as enzimas que cortam e as que costuram. Por fim, os três mecanismos que ampliam ainda mais a diversidade — a imprecisão da própria junção, a hipermutação somática e a troca de classe — e o preço que o organismo paga por operar uma máquina que quebra o próprio DNA de propósito.
]

#parte-title("PARTE I — O desafio: um repertório maior que o genoma", primeira: true)

#subtopico("1.1 — O que um anticorpo precisa reconhecer")

O sistema imune adaptativo enfrenta um problema de engenharia antes de enfrentar qualquer problema biológico: ele precisa estar pronto para reconhecer moléculas que nunca encontrou, inclusive as de micro-organismos que ainda não existem. Chamamos de #termo-nota[antígeno][qualquer molécula capaz de induzir uma resposta imune adaptativa; na resposta humoral, é o que o anticorpo reconhece] qualquer molécula capaz de disparar essa resposta — em geral uma proteína da superfície de um patógeno. E na resposta imune humoral, quem faz o reconhecimento é o anticorpo, também chamado de #sigla("Ig", [imunoglobulina — o nome proteico do anticorpo; usamos os dois termos como sinônimos]).

O detalhe que reorganiza toda a escala do problema é que o anticorpo não reconhece o antígeno inteiro. Ele toca apenas um pedaço da superfície daquela molécula, chamado #termo-nota[epítopo][a pequena região do antígeno efetivamente reconhecida pelo anticorpo, tipicamente um trecho de 10 a 12 aminoácidos], tipicamente da dimensão de um trecho de dez a doze aminoácidos. Uma proteína grande carrega dezenas de epítopos distintos e é reconhecida por muitos anticorpos diferentes ao mesmo tempo, cada um encaixando numa saliência diferente. E vale registrar desde já que epítopo não é obrigatoriamente uma sequência contígua: com frequência ele é *conformacional*, formado por resíduos distantes na cadeia que o dobramento trouxe para perto — o que explica por que ferver uma proteína pode abolir o reconhecimento sem alterar uma única letra da sua sequência.

Com o epítopo definido nessa escala, dá para medir o tamanho real do problema. A conta que interessa é: quantas superfícies distintas de dez aminoácidos podem existir.

*Primeira etapa.* Cada uma das dez posições do trecho pode ser ocupada por qualquer um dos vinte aminoácidos que as proteínas usam. *Segunda etapa.* As posições são independentes entre si — a escolha da primeira não restringe a segunda —, então o total de combinações é vinte multiplicado por si mesmo dez vezes, ou seja, 20¹⁰. *Terceira etapa.* Esse produto vale aproximadamente 1,0 × 10¹³.

Lido em palavras: existem cerca de *dez trilhões* de superfícies possíveis de dez aminoácidos. Nenhum organismo precisa cobrir todas elas, mas o número diz o que o repertório de anticorpos tem de enfrentar — e é contra essa magnitude que qualquer solução de "um gene para cada alvo" quebra logo no primeiro passo. Guarde a ordem de grandeza; ela volta em 1.4 com o outro lado da conta.

Quem produz os anticorpos é o #termo-nota[linfócito B][célula que se desenvolve na medula óssea, carrega um único tipo de anticorpo na membrana e, quando ativada, secreta esse mesmo anticorpo]. Ele se desenvolve na medula óssea a partir de um progenitor linfoide comum — o mesmo progenitor que, migrando para o timo, dá origem ao linfócito T. Terminado o desenvolvimento, a célula B sai para os órgãos linfoides periféricos, como linfonodo e baço, e é lá que ela encontra antígeno e se torna secretora de anticorpo. Essa geografia importa para o que vem adiante: *tudo o que constrói o repertório acontece na medula, antes de qualquer contato com antígeno; tudo o que o refina acontece na periferia, depois do contato.*

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-linfopoiese.png",
  largura: 62%,
  legenda: [Da célula-tronco hematopoiética ao linfócito maduro. O progenitor linfoide que fica na medula vira célula B; o que migra para o timo vira célula T. O encontro com o antígeno só acontece depois, nos órgãos linfoides periféricos — a diversidade já está pronta quando o antígeno chega.])

#subtopico("1.2 — A imunoglobulina por dentro: onde mora a variabilidade")

A imunoglobulina tem a forma de um Y, e essa forma é a pista mais direta de como ela funciona: as duas pontas superiores agarram o antígeno, e a haste inferior conversa com o resto do sistema imune. Quatro cadeias polipeptídicas compõem o Y — duas #termo-nota[cadeias pesadas][as duas cadeias polipeptídicas maiores da imunoglobulina, idênticas entre si, que formam a haste e metade de cada braço do Y] idênticas entre si, que percorrem a haste e sobem por cada braço, e duas cadeias leves, também idênticas entre si, que se encaixam na parte externa dos braços. Como as duas metades são cópias, as duas pontas do Y têm exatamente a mesma especificidade: um anticorpo prende dois epítopos iguais, não dois diferentes.

Cada cadeia, pesada ou leve, divide-se em duas porções com destinos opostos. A porção que fica na ponta do braço, na extremidade amino-terminal, é a *região variável*: é ela que muda de uma célula B para outra e que faz o contato com o antígeno. O resto da cadeia é a *região constante*, praticamente idêntica em todas as células B que expressam aquela mesma classe de anticorpo. O nome merece cuidado, porque induz erro com facilidade: variável não quer dizer que a região mude ao longo da vida daquela célula em resposta ao antígeno — quer dizer que ela *varia entre clones diferentes*, já na saída da medula óssea.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-cadeias-vc.png",
  largura: 76%,
  legenda: [Cadeia leve e cadeia pesada desenhadas em linha, do grupo amino ao carboxi-terminal. A região variável ocupa só a primeira porção de cada uma; toda a extensão restante é constante — e é o tipo dessa região constante que define κ ou λ na leve e a classe do anticorpo na pesada.])

O sítio que agarra o antígeno não pertence a nenhuma das duas cadeias sozinha. Ele se forma na *interface* entre o domínio variável da cadeia leve e o domínio variável da cadeia pesada, que se emparelham lado a lado na ponta do braço. Duas consequências saem daí. A primeira é que a especificidade de um anticorpo depende de *qual* leve encontrou *qual* pesada — o emparelhamento é, por si só, uma fonte de diversidade, e voltaremos a essa multiplicação em 2.2. A segunda é que uma cadeia leve isolada não reconhece nada de útil; é preciso o par.

#figura-lateral("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-ig-esquema.png",
  lado: "right",
  largura-figura: 40%,
  texto: [Repare que o esquema circula a ponta do braço, não a haste. É naquele encaixe entre a região variável da cadeia leve (rosa) e a da cadeia pesada (azul) que o antígeno se aloja. A haste, feita só de regiões constantes das duas pesadas, não toca o antígeno — ela é a parte que outras células e o complemento vão ler.],
  legenda: [O Y da imunoglobulina: variável nas pontas, constante na haste.])

Dentro da própria região variável a variabilidade também não é uniforme. Ela se concentra em três alças curtas por domínio, chamadas #sigla("CDR", [complementarity-determining region — região determinante de complementaridade; as alças hipervariáveis que fazem o contato físico com o epítopo]), que se projetam para fora e são exatamente o que toca o epítopo; entre elas fica um arcabouço razoavelmente conservado, cuja função é sustentar as alças na posição certa. Somando as três alças da leve com as três da pesada, são seis alças desenhando a superfície de encaixe. *A terceira alça da cadeia pesada, a CDR3, é a mais variável de todas* — e a razão disso não está em nenhum gene: ela nasce exatamente no ponto onde os segmentos gênicos são emendados, como a PARTE III vai detalhar. Guarde essa pista.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-ig-3d.png",
  largura: 46%,
  legenda: [A mesma molécula em estrutura real. Cada bloco de fitas β é um domínio: V#sub[L] e C#sub[L] na cadeia leve (rosa), V#sub[H] e três domínios constantes na pesada (azul). A seta aponta o sítio de ligação, no encaixe entre V#sub[L] e V#sub[H].])

#subtopico("1.3 — A região constante decide a classe, e a classe decide a função")

Já temos a região variável instalada como a parte que reconhece. Falta dar função à outra metade da molécula, aquela que ainda não usamos. A região constante da cadeia pesada existe em cinco versões diferentes, designadas pelas letras gregas μ, δ, γ, α e ε, e é essa versão — e apenas ela — que define a *classe* do anticorpo: IgM, IgD, IgG, IgA e IgE, respectivamente. A cadeia leve, por sua vez, tem duas versões de região constante, κ e λ, mas essa escolha não define classe nenhuma: qualquer classe pode ser montada com leve κ ou com leve λ.

O ponto que vale fixar é que a classe não muda o que o anticorpo reconhece — ela muda *o que acontece depois* do reconhecimento. A haste do Y é a parte que outras células e proteínas do sistema imune leem, e cada versão da região constante é lida de um jeito. A IgM ativa a via clássica do complemento com eficiência e, por circular como pentâmero, oferece dez sítios de ligação de uma vez; cada sítio individualmente tem afinidade modesta, mas a soma dos dez segura o alvo — é por isso que a IgM funciona bem como o primeiro anticorpo de uma resposta, quando ainda não houve tempo de refinar afinidade. A IgG é a mais abundante do sangue, responde por cerca de três quartos das imunoglobulinas circulantes, ativa complemento e é a única classe que atravessa a placenta — o recém-nascido chega ao mundo com o repertório de IgG da mãe já instalado, uma proteção emprestada que dura alguns meses. A IgA domina as secreções e o revestimento das mucosas. E a IgE, praticamente indetectável no sangue, liga-se a mastócitos e basófilos e é a classe que orquestra a resposta alérgica e a defesa contra helmintos.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-classes-ig.png",
  largura: 78%,
  legenda: [As cinco classes lado a lado. Leia a tabela pela primeira linha: é a cadeia pesada (μ, δ, γ, α, ε) que muda de coluna para coluna. A segunda linha mostra que a leve continua sendo κ ou λ em todas — a leve não participa da definição de classe. As linhas de baixo são a função efetora que cada haste habilita.])

Uma nota de terminologia antes de seguir, porque ela confunde de forma previsível. Dizer "o anticorpo mudou de classe" descreve uma troca na região constante da pesada, com a região variável intacta. Dizer "o anticorpo ficou mais específico" descreve uma alteração na região variável, com a constante intacta. São eventos diferentes, com maquinarias diferentes, e o item 3.4 vai mostrar que o organismo faz os dois — mas nunca pelo mesmo mecanismo.

#mini-resumo[Um anticorpo é um Y de duas pesadas e duas leves. A região variável, nas pontas, reconhece o epítopo pela interface entre os domínios variáveis da leve e da pesada. A região constante, na haste, define a classe (μ δ γ α ε) e com ela a função efetora — sem tocar na especificidade.]

#subtopico("1.4 — O paradoxo aritmético e a hipótese que o resolveu")

Aqui a conta trava. Mesmo sem nunca ter encontrado antígeno nenhum, um ser humano é capaz de produzir mais de 10¹² imunoglobulinas diferentes. O genoma humano tem cerca de 25 000 genes codificadores no total — para todas as proteínas do corpo, não só para anticorpos. A distância entre os dois números é de oito ordens de grandeza, e ela elimina de saída a explicação mais intuitiva: *não existe um gene guardado para cada anticorpo*. Se existisse, o genoma da imunoglobulina sozinho teria que ser milhões de vezes maior do que o genoma inteiro.

Antes de mostrar a saída, vale eliminar a segunda explicação intuitiva, porque ela dominou a imunologia por décadas. A teoria *instrutiva* propunha que o antígeno funcionasse como molde: o anticorpo seria uma cadeia flexível que se dobraria ao redor da molécula estranha, adquirindo a forma complementar no ato do encontro. É uma ideia econômica — um único gene bastaria — e está errada. O que a substituiu foi a *seleção clonal*: cada célula B produz um único tipo de anticorpo, escolhido antes e independentemente de qualquer antígeno, e o exibe ancorado na membrana como seu receptor, o #sigla("BCR", [B-cell receptor — receptor de antígeno da célula B; é a própria imunoglobulina daquela célula, ancorada na membrana]). O repertório inteiro já está distribuído entre milhões de células diferentes quando o antígeno chega. Ele não instrui ninguém: apenas encontra a célula cujo receptor já encaixava e a manda proliferar.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-selecao-clonal.png",
  largura: 52%,
  legenda: [Seleção clonal. Cada célula B em repouso carrega um receptor de especificidade única — as três células desenhadas já são diferentes antes de qualquer encontro. O antígeno reconhece uma delas e só ela se multiplica; a progênie inteira herda aquele mesmo receptor.])

A consequência da seleção clonal é uma exigência dura sobre a maquinaria genética: *uma célula B, um anticorpo*. Se uma única célula produzisse dois receptores de especificidades diferentes, o antígeno que selecionasse um deles arrastaria junto a produção do outro, de alvo desconhecido — e a lógica inteira desmoronaria. A PARTE III mostra que existe um mecanismo dedicado a garantir essa regra.

#figura-lateral("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-expansao-clonal.png",
  lado: "left",
  largura-figura: 38%,
  texto: [Selecionada, a célula B prolifera e se diferencia em células efetoras que secretam, agora em forma solúvel, o mesmo anticorpo que carregavam na membrana. A quantidade de anticorpo no sangue sobe muito depois do encontro; a *variedade* de anticorpos, porém, já estava lá antes.],
  legenda: [Do receptor de membrana ao anticorpo secretado.])

A saída para o paradoxo foi proposta em 1965 por William Dreyer e Claude Bennett, e ela contrariava frontalmente o princípio de que um gene codifica um polipeptídeo. A hipótese dizia que a cadeia de imunoglobulina seria codificada por *dois* segmentos gênicos separados no genoma herdado — um numeroso, correspondendo à região variável, e um único, correspondendo à região constante — que se aproximariam fisicamente durante o desenvolvimento do linfócito. Foi uma proposta desconfortável, porque exigia admitir que o DNA de uma célula somática pudesse ser reorganizado.

A demonstração veio em 1976, com Susumu Tonegawa. A ideia experimental é simples de acompanhar: se o DNA da célula B tivesse sido reorganizado, os fragmentos gerados por corte enzimático do DNA teriam tamanhos *diferentes* conforme a célula de origem. Tonegawa comparou o DNA de células embrionárias, que nunca rearranjaram nada, com o DNA de um tumor de células produtoras de anticorpo, e viu exatamente isso: os segmentos que apareciam distantes no DNA embrionário estavam vizinhos no DNA da célula produtora. O DNA tinha sido efetivamente cortado e recolado — o achado rendeu o Nobel de 1987 e abriu a PARTE II inteira.

#mini-resumo[Um trilhão de anticorpos não cabe em 25 000 genes. A saída não é o antígeno moldar o anticorpo (teoria instrutiva, refutada) nem um gene por anticorpo: é guardar *peças* separadas no genoma herdado e montá-las por rearranjo do DNA em cada célula B — hipótese de Dreyer e Bennett (1965), demonstrada por Tonegawa (1976).]

E aqui o assunto muda de nível. Até agora falamos de proteína; daqui para frente falamos do DNA que a codifica, e do fato — que não vale para praticamente nenhum outro gene do corpo — de que ele é *diferente em cada célula B*.

#parte-title("PARTE II — A máquina: a recombinação V(D)J")

#subtopico("2.1 — O locus em segmentos: da linhagem germinativa ao DNA da célula B")

O que Tonegawa mostrou tem um desenho concreto. No DNA que herdamos dos nossos pais — o DNA de linhagem germinativa, presente em todas as nossas células, do neurônio ao hepatócito — a região variável da cadeia leve κ não existe como um gene inteiro. Existe como duas coleções de peças, separadas por milhares de pares de base: cerca de trinta e cinco segmentos *V*, enfileirados ao longo do cromossomo, e um pequeno grupo de cinco segmentos *J*, mais adiante, seguidos por um único segmento *C* que codifica a região constante. Nessa configuração o locus não produz anticorpo nenhum — ele guarda potencial, não produto.

Durante o desenvolvimento da célula B na medula óssea, a célula escolhe um segmento V ao acaso e um segmento J ao acaso, corta fisicamente o DNA nos dois pontos, elimina tudo o que estava entre eles e cola as duas peças lado a lado. É a #termo-nota[recombinação V(D)J][o corte e religação do DNA que aproxima um segmento V de um segmento J — e, na cadeia pesada, também de um D — montando a região variável do anticorpo naquela célula]. A partir daí o cromossomo daquela célula é permanentemente diferente do cromossomo de qualquer outra célula do corpo: os segmentos V que ficaram no caminho foram deletados e não voltam.

Só depois desse rearranjo o locus vira um gene funcional. Ele é transcrito, e o transcrito ainda carrega os segmentos J que sobraram e o íntron que separa o bloco J do segmento C. Quem retira esses trechos é o splicing, no RNA, deixando um mensageiro contíguo com V, J e C emendados, que a tradução converte na cadeia leve. Vale reter a divisão de trabalho: *o corte no DNA escolheu quais peças entram; a edição no RNA apenas limpa o que sobrou entre elas.*

#atencao-box("Recombinação V(D)J não é splicing", [Essa é a inversão que mais estraga o raciocínio no tema, e ela é fácil de cometer porque os dois processos "removem trechos e emendam o resto". A diferença é de molécula e de permanência. A recombinação corta o *DNA*, deleta em definitivo os segmentos intermediários e reescreve o cromossomo daquela célula B e de toda a sua descendência — nenhuma outra célula do corpo tem aquele arranjo. O splicing corta o *RNA*, acontece a cada transcrito produzido e não altera uma base sequer do genoma. Um teste rápido: pergunte-se o que aconteceria se a célula parasse de fazer a operação. Sem recombinação, a célula B nunca teria um gene de anticorpo montado. Sem splicing, ela teria o gene montado e produziria um mensageiro com lixo no meio. São perdas de natureza diferente porque são operações de natureza diferente.])

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-vj-fluxo.png",
  largura: 50%,
  legenda: [O caminho completo do locus κ, de cima para baixo. No DNA germinativo, V3 e J3 estão separados por milhares de pares de base. O rearranjo do DNA os aproxima e elimina o que havia entre eles. Só então vêm transcrição, splicing — que remove J4, J5 e o íntron até o C — e tradução. Repare que a região constante nunca é recombinada: ela chega ao produto pelo RNA.])

Na cadeia pesada o esquema é o mesmo, com uma peça a mais. Entre as coleções V e J existe um terceiro conjunto, os segmentos *D*, de diversidade. Isso obriga a dois rearranjos sucessivos em vez de um: primeiro um segmento D se junta a um J, depois um segmento V se junta ao bloco DJ já formado. O produto é uma região variável codificada por três peças, e não por duas — motivo pelo qual a cadeia pesada contribui mais para a diversidade do que a leve. Logo depois dos segmentos J, o locus da pesada traz em fila os segmentos constantes de todas as classes (Cμ, Cδ, Cγ, Cε, Cα), o que já antecipa como a troca de classe será possível sem tocar na região variável.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-locus-pesada.png",
  largura: 80%,
  legenda: [O locus da cadeia pesada em escala linear: quarenta segmentos V à esquerda, o bloco D e os seis J no meio, e, à direita, a fila ordenada de regiões constantes — Cμ, Cδ, Cγ, Cε, Cα. Uma única montagem VDJ pode, mais tarde, ser expressa com qualquer uma dessas constantes.])

#subtopico("2.2 — Diversidade combinatória: a primeira conta")

Com as peças separadas, a aritmética muda de sinal. Antes, cada anticorpo novo exigiria um gene novo; agora, cada anticorpo novo exige apenas uma *combinação* nova das mesmas peças — e combinações se multiplicam. Vale fazer a conta devagar, porque o resultado dela é o que dimensiona o que ainda falta explicar.

*Primeira etapa — a cadeia leve κ.* Trinta e cinco segmentos V, cinco segmentos J. Como qualquer V pode ser emendado a qualquer J, o total não é a soma e sim o produto: 35 × 5 = 175 regiões variáveis κ possíveis.

*Segunda etapa — a cadeia leve λ.* Um cálculo análogo sobre o outro locus de cadeia leve entrega cerca de 120 regiões variáveis distintas. Somando os dois tipos de leve, chega-se a 175 + 120 = 295 cadeias leves diferentes.

*Terceira etapa — a cadeia pesada.* Aqui são três coleções: quarenta segmentos V, vinte e três D e seis J. Multiplicando as três, 40 × 23 × 6 = 5 520 regiões variáveis de cadeia pesada.

*Quarta etapa — o emparelhamento.* Uma vez montadas, qualquer cadeia leve pode se associar a qualquer cadeia pesada, e o sítio de ligação, como vimos em 1.2, nasce na interface entre as duas. Isso multiplica de novo: 295 × 5 520 ≈ 1,6 × 10⁶.

Lido em palavras: a simples recombinação de peças preexistentes, sem nenhum mecanismo adicional, já produz mais de *um milhão e meio* de anticorpos diferentes a partir de umas poucas centenas de segmentos gênicos. Esse é o ganho da estratégia combinatória, e ele é enorme comparado ao ponto de partida. Mas confronte com o alvo: o repertório humano passa de 10¹². *Falta um fator de aproximadamente um milhão*, e nenhuma quantidade de segmentos V a mais o produziria. A fonte que fecha essa distância não está no número de peças — está na maneira imprecisa como elas são coladas, e é o assunto da PARTE III.

#subtopico("2.3 — RSS e a regra 12/23: a gramática que impede a junção errada")

Recombinar peças ao acaso tem um risco óbvio. Se a maquinaria simplesmente cortasse e colasse pontos quaisquer do locus, ela juntaria V com V, ou J com J, e produziria um gene sem sentido — ou pior, cortaria em regiões do genoma que nada têm a ver com imunoglobulina. Alguma coisa precisa dizer à enzima *onde* cortar e *que tipo* de peça pode se ligar a que tipo.

Essa marcação existe e é física, escrita no próprio DNA. Cada segmento V, D e J é flanqueado por uma #sigla("RSS", [recombination signal sequence — sequência-sinal de recombinação; a marca de DNA que indica à recombinase onde cortar]), e toda RSS tem a mesma arquitetura de três partes: um bloco conservado de sete bases, o heptâmero, colado à borda do segmento codificante; um espaçador; e um bloco conservado de nove bases, o nonâmero. O heptâmero e o nonâmero são as sequências que a enzima efetivamente reconhece. O espaçador, ao contrário, não tem sequência conservada nenhuma — o que importa nele é o *comprimento*, e ele existe em apenas dois tamanhos: 12 pares de base ou 23 pares de base.

A regra que governa todo o processo é curta: *uma RSS de espaçador 12 só recombina com uma RSS de espaçador 23.* É a regra 12/23. Como os segmentos são flanqueados por tipos alternados — nos loci de cadeia leve, o V carrega um tipo e o J carrega o outro —, a regra torna a junção V–J obrigatória e a junção V–V ou J–J impossível. Na cadeia pesada o arranjo é ainda mais restritivo: o D é flanqueado dos dois lados por espaçador 12, enquanto V e J trazem espaçador 23, o que obriga a passar pelo D e proíbe que um V se ligue diretamente a um J.

O detalhe que transforma essa regra de convenção em mecanismo está na geometria da dupla-hélice. Uma volta completa da hélice de DNA tem cerca de 10,5 pares de base; um espaçador de 12 pares corresponde, portanto, a aproximadamente uma volta, e um de 23 pares a aproximadamente duas. Com esses comprimentos, o heptâmero e o nonâmero de cada sinal ficam na *mesma face* do DNA, alinhados para serem agarrados simultaneamente pela mesma enzima. Comprimentos intermediários girariam os blocos para lados opostos e a enzima não conseguiria segurar os dois. A regra 12/23 é, no fundo, uma restrição de encaixe tridimensional disfarçada de contagem de bases.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-rss.png",
  largura: 66%,
  legenda: [As duas versões da sequência-sinal no locus κ. Ambas têm o mesmo heptâmero (CACAGTG) e o mesmo nonâmero (ACAAAAACA); o que as distingue é o espaçador — 12 pares de base do lado do V, 23 do lado do J. A sequência do espaçador é irrelevante; o comprimento é tudo.])

#figura-lateral("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-rss-arranjo.png",
  lado: "right",
  largura-figura: 42%,
  texto: [Os três loci lado a lado mostram por que a gramática funciona. Nos dois loci de cadeia leve (IgK e Igλ), V e J carregam espaçadores de tipos opostos, e a única junção permitida é V–J. No locus da pesada (IgH), o D tem espaçador de 12 nos dois flancos e fica cercado por espaçadores de 23 — nenhum V alcança um J sem passar por ele.],
  legenda: [O arranjo das RSS impõe a ordem das junções.])

Uma advertência sobre o alcance da regra, porque ela é frequentemente sobrestimada: a regra 12/23 não *escolhe* qual segmento entra. Ela apenas define quais tipos podem parear. Qual dos quarenta V e qual dos seis J serão usados continua sendo sorteio — e é justamente esse sorteio que a conta de 2.2 mede.

#subtopico("2.4 — Primeiro passo: as recombinases RAG cortam")

A enzima que executa o corte é um par de proteínas que só funciona em conjunto: #sigla("RAG1", [recombination-activating gene 1 — a proteína que carrega o sítio catalítico da recombinase V(D)J]) e #sigla("RAG2", [recombination-activating gene 2 — parceira obrigatória da RAG1; sem ela o complexo não corta]). A RAG1 carrega o sítio catalítico; a RAG2 não corta sozinha, mas o complexo não funciona sem ela. As duas são expressas em linfócitos em desenvolvimento e praticamente em nenhum outro lugar do corpo — a restrição de expressão é, por si só, um mecanismo de segurança.

A analogia útil aqui é a de uma tesoura que, ao cortar, amarra a ponta que acabou de cortar. Isso não é figura de linguagem: o corte deixa mesmo as extremidades codificantes *fechadas*, e essa peculiaridade química vai gerar diversidade lá na frente. O processo acontece em três movimentos.

No primeiro movimento, o complexo RAG1–RAG2 liga-se a uma sequência-sinal e, em seguida, captura a segunda — uma de espaçador 12 e outra de espaçador 23, conforme a regra — dobrando o DNA intermediário numa alça e reunindo as duas num único complexo, a *sinapse*. Nada é cortado antes que os dois parceiros estejam presos no mesmo complexo, e essa exigência é o que impede a enzima de espalhar quebras soltas pelo genoma.

No segundo movimento, a RAG1 faz um corte em uma única fita, exatamente na fronteira entre o heptâmero e o segmento codificante. Esse corte deixa uma hidroxila livre na extremidade 3' do segmento codificante.

No terceiro movimento, essa mesma hidroxila ataca quimicamente a ligação fosfodiéster da fita oposta, no ponto correspondente. É uma reação de transferência de ligação — uma #termo-nota[transesterificação][reação em que uma hidroxila livre ataca uma ligação fosfodiéster e toma o lugar dela; aqui, a própria fita cortada fecha a extremidade sobre si mesma] — e ela produz duas coisas de uma vez. Rompe a segunda fita, completando a quebra de dupla fita; e, no mesmo gesto, fecha a extremidade do segmento codificante sobre si mesma, formando uma alça em grampo, o *hairpin*. Do outro lado da quebra, as extremidades que carregam os sinais ficam retas e limpas.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-rag-nick-hairpin.png",
  largura: 56%,
  legenda: [O corte em duas etapas. Em cima, V e J com suas sequências-sinal. No meio, o corte de fita única deixa uma hidroxila 3' livre em cada extremidade codificante (setas vermelhas). Embaixo, essa hidroxila ataca a fita oposta e sela o segmento codificante num grampo, enquanto as extremidades de sinal ficam retas.])

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-rag-sinapse.png",
  largura: 72%,
  legenda: [O mesmo processo visto pelo complexo proteico. Em (a), RAG1/RAG2 liga-se a um sinal e faz o corte de fita única. Em (b), a sinapse: o DNA intermediário é dobrado numa alça e os dois sinais são reunidos no mesmo complexo — só aqui o corte se completa. Em (c), formados os grampos, as quatro extremidades permanecem retidas no complexo pós-clivagem até que o reparo chegue.])

Ao fim do primeiro passo a célula está numa situação incômoda: existe uma quebra de dupla fita no meio de um cromossomo, com duas extremidades seladas em grampo e duas extremidades soltas. Nada disso ainda é um gene. A montagem depende inteiramente do que a maquinaria de reparo fizer a seguir.

#subtopico("2.5 — Segundo passo: a junção não homóloga costura a quebra")

A quebra de dupla fita é o dano mais perigoso que o DNA pode sofrer, porque as duas fitas se rompem no mesmo ponto e nenhuma delas sobra como molde para reconstruir a outra. A célula dispõe de duas estratégias para lidar com isso, e a escolha entre elas explica por que a recombinação V(D)J é imprecisa por natureza.

A primeira estratégia é a recombinação homóloga: a célula copia a informação perdida da cromátide-irmã, que é uma cópia idêntica da mesma região. O reparo é fiel, mas só está disponível depois da replicação, quando a irmã existe. A segunda é a #sigla("JNHE", [junção não homóloga de extremidades — reparo que aproxima e cola as duas pontas de uma quebra sem usar molde]), que dispensa molde: ela simplesmente aproxima as duas pontas e as cola. Sem molde para consultar, tipicamente se perdem algumas bases no ponto da emenda — e é por isso que a JNHE frequentemente deixa mutação no lugar do reparo.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/slide-19.png",
  largura: 62%,
  legenda: [As duas rotas de reparo de quebra de dupla fita. À esquerda, a recombinação homóloga troca fitas com a cromátide-irmã e restaura a sequência original. À direita, a junção não homóloga cola as pontas sem consultar molde nenhum.])

Na célula B em desenvolvimento, a JNHE não é o plano B: é a rota escolhida. Duas razões se somam. A célula que rearranja está fora da fase S, sem cromátide-irmã disponível; e, sobretudo, a imprecisão que seria um defeito em qualquer outro contexto é aqui o *produto desejado* — cada base perdida ou acrescentada no ponto de emenda é uma variante nova de anticorpo.

A costura tem atores definidos e uma ordem clara. O primeiro a chegar é o #termo-nota[Ku][heterodímero Ku70/Ku80 que forma um anel em torno das extremidades quebradas, protege-as da degradação e serve de plataforma para recrutar o resto da maquinaria de reparo], um par de proteínas que forma um anel em volta de cada extremidade quebrada, protege-a da degradação e mantém as duas pontas próximas uma da outra. O Ku funciona como plataforma: ele recruta uma quinase gigante, a DNA-PKcs, que por sua vez ativa a nuclease *Artemis*. É a Artemis que abre o grampo formado pela RAG — e ela o abre com frequência fora do centro, o que deixa uma das fitas mais longa que a outra, detalhe que o item 3.1 vai transformar em fonte de diversidade. Aparadas e completadas as extremidades por polimerases de reparo, quem sela a emenda é a DNA ligase IV, trabalhando com seu parceiro XRCC4.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-jnhe-ku.png",
  largura: 62%,
  legenda: [A junção não homóloga em ação. Os dois anéis de Ku prendem as extremidades e fazem a ponte sobre a quebra; a partir dessa plataforma são recrutadas nucleases, polimerases e a ligase que finalmente sela o corte.])

Uma quebra, porém, tem quatro extremidades, e elas não recebem o mesmo destino. As duas extremidades *codificantes* — as que estavam em grampo — são abertas, aparadas e coladas uma na outra, formando a *junta codificante*, que permanece no cromossomo e passa a ser a região variável daquela célula B. As duas extremidades de *sinal*, que ficaram retas, também são coladas entre si, formando uma *junta-sinal* precisa, sem perda de bases; só que o fragmento que elas fecham é o DNA intermediário, que se torna um círculo sem origem de replicação. Esse círculo não é copiado nas divisões seguintes e se dilui até desaparecer. A assimetria vale ser guardada em uma linha: *a junção que a célula conserva é a imprecisa; a que ela descarta é a precisa.*

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-junta-codificante.png",
  largura: 52%,
  legenda: [Os dois destinos. À esquerda, os grampos são abertos e os segmentos codificantes se fundem no cromossomo — essa junta fica e ainda pode participar de novos rearranjos. À direita, as extremidades de sinal se unem num círculo de DNA, que é descartado nas divisões celulares seguintes.])

#clinica-box("Quando a máquina de cortar ou a de colar falha", [O arranjo acima explica dois quadros clínicos que parecem distantes e são vizinhos no mecanismo. Mutações que inativam a RAG1 ou a RAG2 impedem que a quebra seja feita: sem quebra não há rearranjo, sem rearranjo não há receptor, e sem receptor o linfócito não completa o desenvolvimento. O resultado é uma imunodeficiência combinada grave em que faltam linfócitos B e T maduros, enquanto as células natural killer — que não dependem de recombinação para montar seu receptor — permanecem presentes. Quando a mutação apenas reduz a atividade da RAG em vez de aboli-la, alguns poucos rearranjos ocorrem e nasce um repertório minúsculo e distorcido, que produz o quadro de linfócitos autorreativos descrito por Omenn. Do outro lado da linha de montagem, mutações na Artemis deixam a quebra ser feita mas impedem a abertura do grampo: o desenvolvimento trava no mesmo ponto funcional, com um acréscimo revelador — como a Artemis também participa do reparo geral de quebras de dupla fita, esses pacientes são anormalmente sensíveis à radiação ionizante. O padrão a extrair é que a imunidade adaptativa inteira é refém de uma maquinaria de reparo de DNA.])

#mini-resumo[As recombinases RAG1 e RAG2 reúnem duas sequências-sinal na sinapse, cortam uma fita e deixam a hidroxila liberada fechar o segmento codificante num grampo. O reparo por junção não homóloga — Ku, DNA-PKcs, Artemis, ligase IV — abre o grampo e cola as pontas. A junta codificante, imprecisa, fica no cromossomo; a junta-sinal, precisa, sai num círculo e se perde.]

#parte-title("PARTE III — Ampliar a diversidade, e pagar por ela")

#subtopico("3.1 — Diversidade juncional: a imprecisão é o produto")

A conta de 2.2 deixou um buraco de um fator de um milhão, e ele é preenchido pelo lugar mais improvável: pelos erros que a maquinaria comete ao emendar as peças. A junção entre um segmento V e um segmento J quase nunca é feita exatamente na fronteira original dos dois. Nucleotídeos são perdidos de uma ponta e da outra, e nucleotídeos novos são acrescentados no meio — de modo que a sequência exata do ponto de emenda é diferente em cada célula B que faz o mesmo rearranjo V–J. É a *diversificação juncional*, e ela multiplica a diversidade por várias ordens de grandeza, até cerca de 10⁸ vezes. Vale a inversão de perspectiva: aqui o erro não é ruído em cima do produto — o erro *é* o produto.

Três mecanismos distintos se somam nessa junção, e separá-los evita a confusão mais comum do tema.

O primeiro é o *aparo*: nucleases removem um número variável de bases das extremidades codificantes antes da colagem. Quantas serão removidas não é determinado por nada — varia de célula para célula.

O segundo são os *nucleotídeos P*, e eles vêm diretamente do grampo formado pela RAG. Quando a Artemis abre o grampo fora do centro, uma das fitas fica mais longa que a outra, e o trecho excedente é a cópia invertida da sequência vizinha — daí serem palindrômicos, o que dá o P ao nome. Preenchida a fita curta por uma polimerase, esses nucleotídeos ficam incorporados à junção. Repare que eles não vieram de lugar nenhum: são consequência inevitável de a RAG selar a extremidade em grampo lá atrás, no primeiro passo.

O terceiro são os *nucleotídeos N*, e esses vêm do nada, literalmente. Uma enzima chamada #sigla("TdT", [terminal deoxynucleotidyl transferase — desoxinucleotidil-transferase terminal; adiciona nucleotídeos à extremidade do DNA sem usar molde]) acrescenta bases à extremidade livre do DNA *sem consultar molde nenhum*, escolhendo-as ao acaso. É a única polimerase do corpo que faz isso, e ela é expressa justamente nos linfócitos em desenvolvimento. Cada célula recebe um punhado diferente de nucleotídeos aleatórios exatamente no ponto que codifica o centro do sítio de ligação.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-diversidade-juncional.png",
  largura: 62%,
  legenda: [As duas colunas mostram os dois lados da imprecisão. À esquerda, o aparo remove bases das extremidades e a abertura assimétrica do grampo gera os nucleotídeos P (palindrômicos, destacados). À direita, a TdT insere nucleotídeos N sem molde antes de as pontas serem preenchidas e coladas. O resultado é uma junção diferente em cada célula.])

Agora a pista deixada em 1.2 fecha. A alça mais variável do anticorpo, a CDR3 da cadeia pesada, é exatamente a alça codificada *pela região da emenda*. Ela é a mais variável não porque exista algum segmento gênico especialmente diverso, mas porque é a única parte da proteína cuja sequência não está escrita em lugar nenhum do genoma — ela é criada na hora, célula por célula.

O preço dessa liberdade é aritmético e alto. O ribossomo lê o mensageiro de três em três bases, e as adições e remoções na junção não respeitam múltiplos de três. Sempre que o saldo de bases ganhas e perdidas não for múltiplo de três, todos os códons seguintes saem deslocados e a cadeia produzida é inútil. Em números redondos, apenas cerca de *um terço* dos rearranjos mantém a fase de leitura. Dois em cada três esforços de montagem são desperdiçados — e a célula precisa de um plano para lidar com isso, que é o assunto imediatamente a seguir.

#subtopico("3.2 — Exclusão alélica: uma célula B, um anticorpo")

Em 1.4 ficou estabelecido que a seleção clonal exige uma célula B por especificidade. Mas cada célula tem *dois* alelos de cada locus, herdados de pai e de mãe, e cada alelo é capaz de rearranjar por conta própria. Se os dois rearranjassem com sucesso, a célula exibiria dois receptores diferentes e a lógica da seleção clonal se romperia. O mecanismo que impede isso chama-se *exclusão alélica*, e ele é elegantemente simples: *o sucesso desliga a máquina*.

A célula rearranja um alelo de cada vez. Se aquele rearranjo for produtivo — isto é, se mantiver a fase de leitura e produzir uma cadeia funcional —, a própria proteína resultante é montada na membrana e emite um sinal para dentro da célula. Esse sinal encerra a expressão das recombinases, e o segundo alelo permanece na configuração germinativa, intocado, pelo resto da vida daquela célula e de toda a sua descendência. Se o rearranjo for improdutivo, nenhuma proteína aparece, nenhum sinal é emitido e a maquinaria continua ligada — a célula então tenta o segundo alelo. Falhando também esse, não há receptor possível e a célula morre. Dado que apenas um terço das junções mantém a fase, essa é a sorte de boa parte dos linfócitos B que começam a se desenvolver.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-exclusao-alelica.png",
  largura: 54%,
  legenda: [Os dois caminhos a partir de dois alelos germinativos. À esquerda, o primeiro rearranjo é produtivo, a imunoglobulina é expressa e o sinal bloqueia qualquer novo rearranjo — o segundo alelo fica intacto. À direita, o rearranjo é improdutivo, nada é expresso, e a célula libera o segundo alelo para tentar.])

A ordem em que isso acontece também é fixa e vale reter, porque explica por que o processo é escalonado em vez de simultâneo. A cadeia pesada rearranja primeiro, em duas etapas — D com J, depois V com o bloco DJ. Assim que uma cadeia pesada funcional aparece, ela se associa a uma cadeia leve substituta e forma um receptor provisório na membrana; é esse receptor provisório que sinaliza "pesada resolvida", desliga o rearranjo da pesada e autoriza o início do rearranjo da leve. Só então a célula tenta o locus κ e, se falhar nos dois alelos κ, parte para o λ. Cada etapa serve de ponto de checagem para a seguinte, e o resultado final é uma única combinação leve-pesada por célula.

#subtopico("3.3 — Hipermutação somática: mudar a região variável depois do encontro")

Todos os mecanismos vistos até aqui operam na medula óssea, antes de qualquer contato com antígeno, e produzem um repertório amplo mas de afinidade apenas razoável. Um segundo processo entra em cena bem mais tarde, nos órgãos linfoides periféricos, e só nas células B que já foram ativadas por antígeno: durante a expansão clonal, a sequência da região variável — aquela mesma já rearranjada — começa a acumular mutações pontuais numa taxa cerca de um milhão de vezes maior que a do resto do genoma. É a *hipermutação somática*.

A enzima responsável é a #sigla("AID", [activation-induced deaminase — desaminase induzida por ativação; expressa apenas em células B ativadas, converte citosina em uracila no DNA]), expressa apenas em células B ativadas. E o que ela faz é enganosamente modesto: ela apenas *desamina uma citosina*, convertendo-a em uracila. Nenhuma mutação foi introduzida ainda nesse instante — a mutação nasce do que a maquinaria de reparo faz com essa uracila fora de lugar, e o processo se ramifica em dois caminhos.

No primeiro caminho, nada é reparado a tempo. A uracila permanece pareada com a guanina da fita oposta, formando um par U:G que não deveria existir. Quando a replicação passa por ali, a polimerase lê a uracila como se fosse timina e insere adenina à frente — o par G:C original virou A:T. É uma transição, e ela é definitiva.

No segundo caminho, o reparo *tenta* consertar e amplia o estrago. A uracila-DNA-glicosilase reconhece a base intrusa e a remove, deixando no lugar um açúcar sem base — um sítio abásico. Esse buraco é passado a polimerases translesão, enzimas capazes de sintetizar por cima de lesões que travariam uma polimerase normal, mas que o fazem inserindo bases praticamente ao acaso. O resultado é que aquela posição pode terminar com qualquer uma das quatro bases.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-aid-cascata.png",
  largura: 88%,
  legenda: [À esquerda, a reação isolada: a desaminase remove o grupo amina da citosina e produz uracila. À direita, os dois destinos do par U:G. Pela rota de cima, a replicação converte o par em A:T. Pela rota de baixo, a glicosilase remove a uracila, o sítio abásico é preenchido por polimerases translesão e qualquer base pode entrar.])

Um ponto costuma escapar e desfaz o entendimento do processo inteiro: a maioria dessas mutações *piora* o anticorpo ou não muda nada. A hipermutação, sozinha, degrada o receptor tanto quanto o melhora. O que transforma mutação aleatória em ganho de afinidade é a seleção que vem depois — as células cujo receptor mutado passa a se ligar melhor ao antígeno recebem mais sinal de sobrevivência e proliferam; as que pioraram morrem. Essa combinação de mutação cega com seleção implacável, repetida em ciclos, é o que chamamos de *maturação de afinidade*, e é a razão de os anticorpos de uma segunda exposição a um mesmo agente serem muito melhores que os da primeira.

#subtopico("3.4 — Mudança de classe: trocar o cabo, manter a ponta")

Existe um terceiro processo de recombinação nesse mesmo locus, e ele parece diversidade sem ser. A imagem que ajuda é a de uma ferramenta com cabos intercambiáveis: a ponta que trabalha continua exatamente a mesma, e o que se troca é o cabo pelo qual o resto do sistema a segura. A célula B que já tem uma montagem VDJ pronta e vinha produzindo IgM pode passar a produzir IgG, IgA ou IgE — com a *mesma* região variável, portanto com a mesma especificidade, e uma função efetora inteiramente nova.

O mecanismo aproveita a arquitetura do locus da cadeia pesada que vimos em 2.1, com as regiões constantes enfileiradas depois da VDJ. Antes de cada uma delas existe um trecho repetitivo de DNA chamado *região switch*. A mesma AID da hipermutação somática age agora nessas regiões switch, desaminando citosinas e disparando quebras de dupla fita em duas delas — a que precede a constante em uso e a que precede a constante desejada. O DNA entre as duas quebras é excisado como um círculo e descartado, e a JNHE cola a VDJ diretamente à nova região constante. Como a região variável não é tocada em momento algum, o anticorpo continua reconhecendo o mesmo epítopo.

#figura-nebli("/figuras/biomol-recombinacao-vdj-imunoglobulinas/fig-switch-classe.png",
  largura: 62%,
  legenda: [Troca de classe de IgM para IgA. As regiões switch (círculos pretos) precedem cada constante. A AID dispara quebras em duas delas; o DNA intermediário — com Cμ, Cδ, Cγ e Cε — sai como círculo e é perdido. A VDJ, à esquerda, permanece idêntica antes e depois.])

Duas consequências merecem registro. A primeira é que a troca é *irreversível*: as constantes que estavam entre a antiga e a nova foram fisicamente deletadas, e uma célula que passou para IgA não tem como voltar a IgM. A segunda é que a escolha da classe de destino não é aleatória — ela é ditada pelas citocinas que os linfócitos T auxiliares liberam no microambiente, o que permite ao organismo dirigir a resposta para o tipo de defesa apropriado ao agente encontrado.

#confusao-prevista(
  titulo: "Hipermutação somática e mudança de classe não são o mesmo processo",
  aluno_acha: [aluno acha que, por dependerem os dois da AID e ocorrerem os dois na célula B ativada, são faces do mesmo mecanismo — e que ambos geram diversidade],
  mecanismo: [a AID é a mesma, o alvo e a consequência são opostos. A hipermutação atua na *região variável* já rearranjada e troca bases uma a uma: a especificidade e a afinidade mudam, a classe não. A mudança de classe atua nas *regiões switch*, que ficam antes das regiões constantes, e deleta um bloco inteiro de DNA: a função efetora muda, a especificidade fica intacta. Daí a formulação que o próprio material da aula destaca em negrito — a mudança de classe *não gera diversidade*, porque a VDJ que reconhece o antígeno é rigorosamente a mesma antes e depois.],
)

#subtopico("3.5 — O preço de uma máquina que quebra o próprio DNA")

Fechado o inventário dos mecanismos, sobra a contabilidade dos danos, e ela não é pequena. Um sistema que gera receptores ao acaso produz, necessariamente, dois tipos de resultado indesejado: células B que não conseguem produzir anticorpo funcional e células B que produzem anticorpo funcional contra o próprio organismo.

O primeiro tipo já foi quantificado: com apenas um terço das junções em fase de leitura, a maior parte dos linfócitos B que iniciam o desenvolvimento nunca chega a exibir um receptor completo. Essas células simplesmente morrem na medula, por falta do sinal de sobrevivência que só um receptor montado consegue emitir. É desperdício em escala industrial, e o organismo o compensa produzindo linfócitos B continuamente ao longo de toda a vida.

O segundo tipo é mais perigoso e exige filtro ativo. Como os segmentos são combinados sem qualquer consulta ao que existe no próprio corpo, uma fração dos receptores gerados reconhece moléculas do próprio organismo. Antes de sair da medula, cada célula B imatura é testada contra os antígenos próprios ali presentes, e o reconhecimento forte dispara um de três desfechos. A célula pode ser eliminada por apoptose, na *deleção clonal*. Pode reativar as recombinases e rearranjar de novo o locus da cadeia leve, trocando aquela metade do receptor por outra — a *edição de receptor*, que é a única situação em que a exclusão alélica é deliberadamente suspensa. Ou pode sobreviver num estado de não-resposta permanente, a *anergia*, em que permanece circulando mas não é mais ativável.

Há ainda um terceiro preço, que não é imunológico e sim oncológico. RAG e AID existem para produzir quebras de dupla fita em pontos específicos do genoma, e nenhuma das duas é perfeitamente precisa. Quando uma quebra programada no locus de imunoglobulina é reparada junto com uma quebra acidental em outro cromossomo, o resultado é uma translocação que põe um gene qualquer sob o controle dos elementos regulatórios do locus de anticorpo — que, numa célula B, são potentíssimos. É assim que nascem alguns dos linfomas mais característicos: um gene que promove proliferação, ou um que bloqueia a apoptose, passa a ser transcrito com a mesma intensidade com que a célula transcreveria seu próprio anticorpo. O mesmo mecanismo que garante a imunidade adaptativa é, em uma minoria de eventos, o que inicia o tumor.

#conclusao-box[
  O princípio que costura esta apostila inteira é que a diversidade não foi *armazenada*, foi *fabricada*. O genoma herdado guarda algumas centenas de peças, e cada linfócito B em desenvolvimento monta com elas um gene que não existia antes e que nenhuma outra célula do corpo possui — depois de montado, esse gene é reescrito por mutação dirigida e, mais tarde, tem sua metade final trocada por outra. O anticorpo é, nesse sentido, a única proteína humana cujo gene é diferente em cada célula que a produz.

  O mecanismo nuclear que sustenta tudo isso é a quebra de dupla fita deliberada. As recombinases RAG1 e RAG2 reúnem duas sequências-sinal obedecendo à regra 12/23, cortam uma fita e deixam a hidroxila liberada selar o segmento codificante num grampo; a junção não homóloga abre esse grampo de forma assimétrica, apara as pontas, deixa a TdT inserir bases sem molde e cola tudo. Da soma sai o número que abriu o assunto: cerca de 1,6 × 10⁶ combinações de peças, multiplicadas por até 10⁸ pela imprecisão da própria emenda. Depois do encontro com o antígeno, a AID desamina citosinas na região variável e a seleção converte mutação cega em afinidade crescente; nas regiões switch, a mesma enzima troca a região constante sem tocar na especificidade.

  A clínica retomada é a de dois lados da mesma moeda mecanística. Quando a máquina não funciona — RAG inativa, Artemis incapaz de abrir o grampo —, não há repertório e o paciente fica sem imunidade adaptativa, com sensibilidade aumentada à radiação quando o defeito atinge um componente compartilhado com o reparo geral do DNA. Quando ela funciona no lugar errado, as mesmas quebras programadas geram translocações que colocam genes de proliferação sob o comando regulatório do locus de imunoglobulina, e daí nascem linfomas característicos da linhagem B. Não são exceções ao sistema: são o sistema operando nos seus extremos.

  O que fica em aberto para adiante é a outra metade do problema. Toda esta apostila tratou de como o repertório é *gerado*; ficou fora de escopo como ele é *depurado* — os pontos de checagem que testam cada célula B contra antígenos próprios e decidem entre deleção, edição de receptor e anergia, e o papel do linfócito T em autorizar a expansão clonal, a hipermutação e a troca de classe nos centros germinativos. É por aí que a lógica molecular vista aqui se transforma em resposta imune organizada.
]
