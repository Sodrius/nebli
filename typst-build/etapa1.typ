#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Uma bactéria não cresce como um bebê cresce. O que aumenta numa cultura não é o tamanho da célula, é o número de células: cada bactéria copia o cromossomo, separa as cópias e se parte em duas por divisão binária, e a população dobra. Toda a fisiologia bacteriana existe para sustentar essa conta. Ela precisa capturar matéria-prima do meio, extrair energia dela por reações de oxidação, e fazer as duas coisas dentro de uma janela estreita de pH, temperatura, sal e oxigênio. Este resumo segue exatamente esse caminho — primeiro o que a bactéria precisa, depois como ela fabrica energia com isso, e por fim o que acontece quando bilhões delas fazem isso ao mesmo tempo dentro de um tubo de cultura.
]

#parte-title("PARTE I — O que a bactéria precisa para crescer", primeira: true)

#subtopico("1.1 — Nutrição: os elementos que viram bactéria")

Quase todo o peso seco de uma bactéria é carbono, nitrogênio, enxofre e fósforo. Esses quatro elementos montam as macromoléculas que a célula precisa duplicar antes de se dividir: o carbono é o esqueleto de proteína, lipídeo e açúcar; o nitrogênio entra em todo aminoácido e em toda base nitrogenada; o enxofre está na cisteína e na metionina e em cofatores como a coenzima A; o fósforo forma a espinha do #sigla("DNA", [ácido desoxirribonucleico — o cromossomo bacteriano, uma molécula circular única]) e as cabeças dos fosfolipídeos. Ao lado deles vêm íons inorgânicos em quantidade muito menor e igualmente obrigatória — potássio, sódio, cálcio, cloro, ferro e magnésio —, que não constroem estrutura mas ativam enzimas: o magnésio estabiliza o ribossomo e é cofator de toda reação que envolve #sigla("ATP", [adenosina trifosfato — a moeda de energia que a célula gasta em qualquer reação que não ocorre espontaneamente]), o ferro carrega elétrons nos citocromos.

Nutrição, em bacteriologia, é o fornecimento dessas substâncias; crescimento é o aumento do número de microrganismos que esse fornecimento permite. Um meio de cultura só funciona se entregar três coisas simultaneamente: uma fonte de energia, uma fonte de carbono e um doador de elétrons — e é justamente por essas três dimensões que se classificam os microrganismos.

#align(center, table(
  columns: (auto, auto, auto, auto),
  stroke: 0.5pt + gray-border,
  inset: (x: 8pt, y: 6pt),
  align: left + horizon,
  fill: (col, row) => if row == 0 { navy } else { none },
  text(fill: white, weight: "bold", size: 8.5pt)[Grupo],
  text(fill: white, weight: "bold", size: 8.5pt)[Energia],
  text(fill: white, weight: "bold", size: 8.5pt)[Carbono],
  text(fill: white, weight: "bold", size: 8.5pt)[Doador de elétrons],
  text(size: 8.5pt)[Fotolitoautotrófica], text(size: 8.5pt)[luz], text(size: 8.5pt)[CO₂], text(size: 8.5pt)[inorgânico (H₂O, H₂S)],
  text(size: 8.5pt)[Fotorganoheterotrófica], text(size: 8.5pt)[luz], text(size: 8.5pt)[orgânico], text(size: 8.5pt)[orgânico],
  text(size: 8.5pt)[Quimiolitoautotrófica], text(size: 8.5pt)[reação química], text(size: 8.5pt)[CO₂], text(size: 8.5pt)[inorgânico (NH₃, NO₂⁻, Fe²⁺)],
  text(size: 8.5pt)[Quimiorganoheterotrófica], text(size: 8.5pt)[reação química], text(size: 8.5pt)[orgânico], text(size: 8.5pt)[orgânico],
))

#v(4pt)

O nome comprido se lê em três pedaços: o prefixo _foto_ ou _quimio_ diz de onde vem a energia — luz ou oxidação de uma substância; o trecho do meio, _lito_ ou _organo_, diz quem doa os elétrons dessa oxidação — composto inorgânico ou orgânico; o sufixo _autotrófico_ ou _heterotrófico_ diz de onde vem o carbono — gás carbônico ou molécula orgânica pronta.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-04.png",
  largura: 72%,
  legenda: [As quatro combinações e seus representantes. Repare que a última linha, a dos patógenos humanos, é a única em que todas as três colunas apontam para "orgânico".])

Toda bactéria de interesse médico cai na última linha: é #termo-nota[quimiorganoheterotrófica][tira energia da oxidação de compostos orgânicos, e usa esses mesmos compostos como fonte de carbono e como doadores de elétrons]. A consequência prática é imediata e volta na PARTE III: se o patógeno não sabe fixar gás carbônico nem oxidar amônia, o meio de cultura tem que chegar com matéria orgânica pronta, e é por isso que a base de praticamente todo meio é hidrolisado de proteína — peptonas e caseína já quebradas em peptídeos e aminoácidos, que entregam carbono e nitrogênio na mesma colherada.

As outras linhas não são curiosidade de livro: as quimiolitoautotróficas do gênero _Nitrosomonas_ oxidam amônia a nitrito, tiram disso toda a energia de que precisam e fixam gás carbônico como uma planta — são elas que fazem o nitrogênio circular no solo e na água, sem depender de uma única molécula orgânica pronta.

#mini-resumo[A bactéria precisa de energia, carbono e doador de elétrons; o patógeno humano tira os três de matéria orgânica, e por isso o meio de cultura começa sempre por proteína hidrolisada.]

#subtopico("1.2 — pH, temperatura e sal: as janelas que o meio precisa respeitar")

Nenhuma bactéria cresce em qualquer condição, e o motivo é que enzima é proteína dobrada. A forma que segura o sítio ativo depende de pontes de hidrogênio e de interações iônicas entre cadeias laterais, e essas interações se desfazem quando o próton disponível muda, quando o calor agita demais a cadeia ou quando a água some do citoplasma. As três variáveis clássicas do meio — pH, temperatura e concentração de sal — atacam exatamente esse ponto.

A maioria das bactérias de importância médica é #termo-nota[neutrófila][cresce melhor em pH próximo de 7,0, faixa em que a maior parte das enzimas citoplasmáticas mantém a conformação ativa], com faixa útil aproximada de 6 a 8. Acidófilas prosperam abaixo disso e alcalófilas acima, mas em nenhuma delas o citoplasma acompanha o meio: o pH interno é mantido perto da neutralidade por bombas de próton e antiportes que trocam íons contra o gradiente, gastando energia. Essa é a razão de o meio de cultura levar tampão fosfato. À medida que a bactéria fermenta açúcar e despeja ácido, o pH do meio despenca e a cultura se envenena com o próprio produto; o tampão segura essa queda por tempo suficiente para a população crescer.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-05.png",
  largura: 76%,
  legenda: [As três faixas de pH e o que cada grupo faz para manter o interior neutro. O painel da direita mostra o ponto central: o pH intracelular varia muito menos que o extracelular.])

Com a temperatura o desenho da curva conta o mecanismo. A taxa de crescimento sobe devagar conforme o calor acelera as reações enzimáticas, atinge um ótimo e depois cai de forma abrupta — não simétrica. A subida é cinética, obedece ao aumento normal de velocidade de reação com a temperatura; a queda é estrutural, porque poucos graus acima do ótimo as proteínas começam a desnaturar e a membrana perde a fluidez adequada. Pelo ótimo separam-se psicrófilas (frio), mesófilas (temperaturas amenas, ótimo em torno de 37 °C), termófilas e hipertermófilas. Todo patógeno humano é mesófilo, e não por acaso: 37 °C é a temperatura do hospedeiro que ele coloniza.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-06.png",
  largura: 60%,
  legenda: [Cada grupo tem seu pico, e todos compartilham o mesmo formato: subida gradual, queda vertical logo depois do ótimo.])

A concentração de sal age por um caminho diferente — não desnatura proteína, desidrata a célula. Quando a força iônica do meio sobe, a água sai do citoplasma por osmose e as reações param por falta de solvente. A maioria das bactérias é não halófila e tolera pouco mais que a salinidade fisiológica. Algumas são #termo-nota[halotolerantes][crescem em concentrações de sal que inibem a maioria das espécies, sem precisarem de sal alto para crescer] e continuam crescendo em concentrações que travam as demais — _Staphylococcus aureus_ cresce em cloreto de sódio a 7,5%, e é exatamente essa tolerância que o meio de manitol salgado explora para isolá-lo de material contaminado por outras espécies. Já os halófilos extremos das salinas não apenas toleram como exigem sal em torno de 15 a 30%, porque acumulam potássio no citoplasma para equilibrar o meio e suas proteínas só se dobram corretamente nessa força iônica.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-09.png",
  largura: 48%,
  legenda: [Cada curva tem um pico deslocado: o halófilo extremo não cresce em água doce, e o não halófilo não cresce na salina.])

#subtopico("1.3 — Oxigênio e ferro: dois recursos, duas guerras")

O oxigênio é o recurso mais mal compreendido da fisiologia bacteriana porque é veneno e combustível ao mesmo tempo. Quando o oxigênio molecular recebe um elétron avulso de uma enzima qualquer, ele não se reduz por inteiro a água; forma o ânion superóxido, e daí peróxido de hidrogênio e radical hidroxila, que atacam lipídeo de membrana, proteína e DNA. Toda célula que convive com ar precisa de duas enzimas para neutralizar essa cascata: a #sigla("SOD", [superóxido dismutase — converte dois ânions superóxido em peróxido de hidrogênio e oxigênio]) e a catalase, que quebra o peróxido em água e oxigênio.

Essa dupla explica a classificação por aeração inteira. O aeróbio estrito tem as duas enzimas e precisa de oxigênio como aceptor final de elétrons — sem ele, não fecha a cadeia respiratória e não fabrica ATP. O anaeróbio estrito, como _Clostridium tetani_, não tem superóxido dismutase nem catalase em quantidade útil: exposto ao ar, morre oxidado pelos próprios derivados reativos. O anaeróbio facultativo, de que _Escherichia coli_ é o exemplo padrão, tem as duas enzimas e as duas rotas — respira quando há oxigênio, fermenta quando não há. O microaerófilo precisa de oxigênio em tensão reduzida, porque sua defesa antioxidante não dá conta da concentração atmosférica.

#confusao-prevista(
  titulo: "Anaeróbio estrito não é quem \"não usa\" oxigênio",
  aluno_acha: [o aluno lê "anaeróbio" como indiferença ao ar — a bactéria simplesmente ignoraria o oxigênio e cresceria com ou sem ele],
  mecanismo: [a relação é de letalidade, não de indiferença. O oxigênio gera superóxido e peróxido espontaneamente dentro de qualquer célula; sem superóxido dismutase e catalase, esses derivados oxidam a própria maquinaria. Por isso material suspeito de anaeróbio exige transporte que exclua o ar, sob pena de a cultura vir negativa por morte, não por ausência.],
)

O ferro trava uma guerra de natureza oposta: não é tóxico ao patógeno, é escasso por decisão do hospedeiro. Ele é micronutriente crítico porque compõe os citocromos da cadeia respiratória e o sítio catalítico da ribonucleotídeo redutase, a enzima que fabrica os desoxirribonucleotídeos do DNA novo — sem ferro a célula não respira nem replica, e por isso a oferta de ferro dita o ritmo de crescimento da população. O hospedeiro explora exatamente essa dependência e mantém quase todo o seu ferro preso em proteínas: transferrina no plasma, lactoferrina nas mucosas, ferritina dentro das células e hemoglobina nas hemácias. A concentração de ferro livre resultante fica na ordem de 10⁻¹⁸ molar, muito abaixo do que qualquer bactéria precisa. Esse sequestro deliberado é a imunidade nutricional: o recurso existe em abundância, mas não circula.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-10.png",
  largura: 72%,
  legenda: [Os quatro movimentos da disputa pelo ferro: por que a bactéria precisa dele, como o hospedeiro o esconde, como o patógeno o arranca e como o nível de ferro acaba regulando a virulência.])

As bactérias patogênicas responderam com três estratégias de arrombamento. Os sideróforos são moléculas pequenas, secretadas, com afinidade pelo ferro férrico maior que a da própria transferrina: arrancam o metal da proteína do hospedeiro e voltam por receptores específicos de membrana. As hemolisinas rompem a hemácia e liberam a hemoglobina, capturada inteira por transportadores de heme. E há receptores diretos, que encostam na transferrina ou na lactoferrina e retiram o ferro sem intermediário.

O detalhe que fecha o raciocínio é regulatório. A proteína Fur funciona como sensor: quando o ferro intracelular está alto, ela se liga ao metal, ocupa os promotores dos genes de virulência e os reprime; quando o ferro cai — exatamente o que acontece dentro do hospedeiro —, Fur se desliga do DNA e esses genes são transcritos. A escassez de ferro é, portanto, o sinal ambiental que avisa a bactéria de que ela entrou num corpo, e a resposta a esse sinal é produzir sideróforos, hemolisinas e toxinas. É esse mecanismo que faz a produção da toxina diftérica depender do ferro do meio.

#parte-title("PARTE II — Como a bactéria transforma nutriente em ATP")

#subtopico("2.1 — Glicólise e fermentação: ATP sem aceptor externo")

A bactéria que chega ao meio de cultura traz consigo a mesma via central que a célula humana usa: a glicólise, que quebra uma glicose de seis carbonos em dois piruvatos de três, com saldo de dois ATP e dois #sigla("NADH", [nicotinamida adenina dinucleotídeo reduzido — o transportador que carrega os elétrons arrancados do substrato]). Vale a pena separar essa via em três estágios, porque cada um resolve um problema diferente.

No primeiro estágio a célula gasta ATP para fosforilar a glicose. Parece contraintuitivo investir energia logo na entrada, mas a fosforilação cumpre duas funções ao mesmo tempo: a glicose fosforilada perde a capacidade de atravessar a membrana de volta, ficando presa dentro da célula, e a carga negativa do fosfato desestabiliza a molécula, preparando-a para ser cortada ao meio. No segundo estágio vem a colheita: a oxidação do gliceraldeído-3-fosfato reduz o NAD⁺ a NADH e cria o 1,3-bifosfoglicerato, um intermediário de ligação rica em energia, cuja hidrólise libera energia suficiente para transferir o fosfato diretamente a uma molécula de #sigla("ADP", [adenosina difosfato — o ATP já gasto, que volta a ser carregado quando recebe um fosfato]). Esse é o mecanismo da fosforilação em nível de substrato: o fosfato salta de um intermediário energizado direto para o ADP, sem membrana, sem gradiente e sem oxigênio em passo nenhum.

Há, porém, um problema de contabilidade. A oxidação do estágio dois consumiu NAD⁺ e devolveu NADH, e a célula tem um estoque pequeno e fixo desse transportador. Se ninguém devolver os elétrons do NADH a algum lugar, o NAD⁺ acaba, a oxidação para e a glicólise trava em duas ou três voltas. O terceiro estágio existe só para resolver isso: na ausência de aceptor externo, o próprio piruvato — ou um derivado dele — é reduzido pelo NADH ali mesmo no citoplasma, regenerando o NAD⁺. Isso é fermentação, e a definição precisa é essa: um processo de oxirredução em que o aceptor final de elétrons é uma molécula orgânica produzida pela própria via, não um composto externo.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-15.png",
  largura: 55%,
  legenda: [O mesmo piruvato, três destinos. Repare que o ramo fermentativo devolve o elétron ao carbono, enquanto o ramo aeróbio entrega o carbono ao ciclo e o elétron à cadeia.])

O produto varia com a espécie, e essa variação é a base de meia bacteriologia diagnóstica. As bactérias láticas homofermentativas reduzem o piruvato a lactato e param aí; as heterofermentativas produzem lactato mais etanol e gás carbônico; enterobactérias fabricam mistura de ácidos, com produção de gás em algumas espécies e não em outras. O rendimento é sempre baixo — os mesmos dois ATP líquidos da glicólise, porque nenhum ATP adicional aparece no estágio três —, mas o processo é rápido e independe de qualquer aceptor do ambiente. É o que sustenta o crescimento no fundo de um abscesso, na luz intestinal e dentro de um tubo fechado.

#mini-resumo[Fermentar não é deixar de produzir ATP: é produzir só o ATP da glicólise e gastar o piruvato para devolver os elétrons do NADH ao NAD⁺, mantendo a via girando.]

#subtopico("2.2 — Respiração: a cadeia mora na membrana plasmática")

Se houver um aceptor de elétrons externo disponível, a bactéria muda de estratégia e o piruvato deixa de ser lixeira para virar combustível. Descarboxilado a acetil-coenzima A, ele entra no ciclo dos ácidos tricarboxílicos, que arranca o restante dos elétrons dos seus carbonos e os entrega a mais NADH e a #sigla("FADH₂", [flavina adenina dinucleotídeo reduzido — transportador que entrega elétrons num ponto mais tardio da cadeia, rendendo menos ATP que o NADH]), liberando gás carbônico. Até aqui a diferença em relação à célula humana é nenhuma. A diferença aparece no endereço da etapa seguinte.

O eucarioto faz respiração na membrana interna da mitocôndria. A bactéria não tem mitocôndria — e a solução dela é montar a mesma maquinaria na própria membrana plasmática. Os complexos que recebem os elétrons do NADH, as quinonas que os transportam pelo interior lipídico e os citocromos que os passam adiante ficam encravados na membrana que envolve o citoplasma, e a ATP sintase fica ao lado deles.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-18.png",
  largura: 68%,
  legenda: [O desenho é o da mitocôndria, mas na bactéria essa membrana é a plasmática e o espaço para onde os prótons são bombeados é o periplasma ou o meio externo.])

O mecanismo em si é o mesmo em qualquer domínio da vida. Conforme os elétrons descem a cadeia de um transportador para o seguinte, cada passo libera energia, e essa energia é usada para bombear prótons para fora da membrana. Acumula-se então uma diferença de concentração de próton e de carga entre os dois lados — a #termo-nota[força próton-motriz][energia armazenada no gradiente de próton através da membrana, convertida em ATP quando esse próton retorna pela ATP sintase]. Os prótons tendem a voltar, e o único caminho de volta é o canal da ATP sintase, cuja rotação, movida por esse fluxo, fosforila o ADP. Isso é fosforilação oxidativa, e ela produz muito mais ATP que a fermentação: da ordem de trinta ATP por glicose contra os dois da via fermentativa, porque cada NADH entregue à cadeia rende vários prótons bombeados em vez de um único fosfato transferido.

O que define se a via é aeróbia ou anaeróbia não é a cadeia, é quem recebe o elétron no fim dela. Na respiração aeróbia o aceptor final é o oxigênio molecular, que ao receber quatro elétrons e quatro prótons vira água; é a rota de maior rendimento porque o oxigênio é o aceptor mais ávido disponível na natureza. Na respiração anaeróbia a cadeia continua funcionando, mas o aceptor final é um composto inorgânico oxidado — nitrato, sulfato ou carbonato —, reduzido a nitrito, sulfeto ou metano. O rendimento fica intermediário, maior que o da fermentação e menor que o da respiração aeróbia, porque esses aceptores puxam o elétron com menos força que o oxigênio e a queda de energia ao longo da cadeia é menor.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-19.png",
  largura: 66%,
  legenda: [A bifurcação está no piruvato: à esquerda o ramo anaeróbio fermentativo, à direita a entrada no ciclo com o rendimento muito maior.])

Essa hierarquia energética explica um comportamento que reaparece na PARTE III. O anaeróbio facultativo, tendo as três rotas, escolhe sempre a mais rentável disponível: respira oxigênio se houver, respira nitrato se não houver oxigênio, e só fermenta em último caso. A consequência prática é que uma mesma _E. coli_ cresce mais rápido e atinge densidade maior numa cultura aerada do que num tubo fechado.

#subtopico("2.3 — O metabolismo vira assinatura: do açúcar fermentado à cor da placa")

O rendimento energético que acabamos de comparar tem um subproduto que a bacteriologia transformou em ferramenta: cada espécie fermenta um conjunto próprio de açúcares e despeja um conjunto próprio de resíduos. Como espécies diferentes carregam enzimas diferentes, o padrão de resíduos funciona como impressão digital bioquímica — e é ele, não a aparência da célula, que dá o nome da bactéria no laboratório.

A leitura mais usada é a do ácido. Um #termo-nota[meio diferencial][deixa todas as espécies crescerem e as separa pela reação química entre um produto do metabolismo e um indicador do meio] que contenha um único açúcar fermentável e um indicador de pH separa em duas cores quem fermenta aquele açúcar e quem não fermenta: quem fermenta despeja ácido, o pH local cai e o indicador vira; quem não fermenta usa outra fonte de carbono, não acidifica e a colônia fica na cor do meio. É por isso que a lactose aparece como açúcar único em vários meios seletivos — ela separa de uma vez as enterobactérias fermentadoras de lactose das não fermentadoras, e essa divisão orienta a conduta antes mesmo da identificação de espécie.

A segunda leitura é a do enxofre. Algumas espécies reduzem tiossulfato a gás sulfídrico durante o metabolismo de aminoácidos sulfurados; se o meio contiver citrato férrico, o sulfeto produzido precipita como sulfeto de ferro, que é preto. O centro escuro da colônia de _Salmonella_ em meio apropriado não é pigmento bacteriano: é o precipitado de um gás que a bactéria produziu reagindo com um sal que o meio trouxe de propósito.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-44.png",
  largura: 55%,
  legenda: [Uma bateria bioquímica lê vários resíduos ao mesmo tempo — ácido na base, gás sulfídrico, gás preso no meio, urease, indol e motilidade — e cada combinação aponta um gênero.])

A partir daí a lógica se repete com outros resíduos. A produção de gás é lida como bolha ou deslocamento da coluna de ágar; a urease é detectada pela alcalinização que a amônia provoca; a produção de indol denuncia a quebra de triptofano; a motilidade aparece como turvação difusa em torno da picada. Reunindo meia dúzia dessas leituras num único tubo com camadas, o laboratório chega ao gênero sem precisar de nenhum equipamento sofisticado.

Duas consequências merecem ficar claras. A primeira é que toda identificação bioquímica é fenotípica: ela lê o que a bactéria faz, não o gene que ela carrega, e por isso exige que a bactéria esteja viva, crescendo e em quantidade suficiente para acidificar o meio de forma visível — o que amarra o resultado ao tempo de crescimento da população, tema da PARTE III. A segunda é que a cor lida na placa nunca é a cor do microrganismo. Ela é o produto de uma reação química entre um metabólito e um reagente que o meio trouxe; a bactéria em si é incolor.

#parte-title("PARTE III — Da célula à população: crescimento e cultivo")

#subtopico("3.1 — Divisão binária e as quatro fases da curva")

Uma cultura bacteriana cresce como juros compostos, não como um organismo. A célula duplica o cromossomo, segrega as cópias para os polos, constrói um septo de parede no meio e se parte em duas células-filhas idênticas — divisão binária simples. O intervalo entre uma divisão e a seguinte é o #termo-nota[tempo de geração][intervalo que a espécie leva para dobrar de número em dadas condições; é ele que fixa a inclinação da fase log], e como cada célula gerada volta a se dividir, a população não cresce somando, cresce dobrando: partindo de N₀ células, depois de _n_ gerações há N₀ × 2#super[n] células. Por isso o eixo vertical da curva de crescimento é logarítmico. Numa escala linear, a fase mais informativa apareceria comprimida contra o eixo e depois disparando fora do papel.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-22.png",
  largura: 66%,
  legenda: [As quatro fases em escala logarítmica. O trecho reto da fase log é reto justamente porque o crescimento é exponencial — em log, uma exponencial vira reta, e a inclinação dessa reta é o tempo de geração.])

A curva tem quatro trechos, e cada um tem uma explicação fisiológica própria. Na *fase lag* praticamente não ocorre divisão celular, mas há aumento de massa: a bactéria acaba de cair num meio novo e está construindo o que vai precisar — ribossomos em quantidade, transportadores para os nutrientes daquele meio específico, e as enzimas de assimilação das fontes de carbono e nitrogênio disponíveis. É fase de adaptação e de intensa atividade metabólica, não de repouso, e sua duração depende de quão diferente o meio novo é do anterior: uma bactéria transferida para um meio idêntico ao de origem quase não faz lag.

Na *fase logarítmica* a maquinaria está pronta e a divisão ocorre em velocidade máxima e constante, limitada apenas pelo tempo de geração da espécie naquelas condições. É a fase em que a população é mais homogênea e em que cada célula está com todos os processos ligados — parede sendo sintetizada, DNA sendo replicado, ribossomo traduzindo —, e isso terá consequência direta no subtópico seguinte.

Na *fase estacionária* a velocidade de multiplicação diminui gradualmente até que o número de células por unidade de volume pare de mudar. A causa é dupla: o nutriente limitante se esgota e os produtos do metabolismo se acumulam a ponto de intoxicar a cultura — ácido da fermentação, principalmente. O ponto que costuma escapar é que a divisão não parou; o número de células novas formadas apenas passou a contrabalançar o número das que morrem. E a bactéria estacionária não é uma bactéria logarítmica mais lenta: a queda de nutriente dispara a #termo-nota[resposta estringente][programa disparado pela falta de aminoácido ou de nutriente, que redireciona a célula de crescer para sobreviver], com síntese do nucleotídeo alarmônio ppGpp, que desliga a produção de ribossomos e liga um programa genético alternativo de sobrevivência — parede mais espessa, defesas antioxidantes, tolerância a estresse. É nessa fase que muitas espécies produzem toxinas e, nas que têm essa capacidade, é aqui que começa a esporulação.

Na *fase de declínio* a morte supera a formação e o número de células viáveis cai, até que a cultura se esterilize.

#subtopico("3.2 — Tempo de geração na clínica: por que a cultura demora e onde o antibiótico morde")

O tempo de geração é o número que traduz a curva para a prática clínica, e a diferença entre espécies é de ordens de grandeza. _Escherichia coli_ duplica a cada 20 minutos em condições ideais; _Mycobacterium tuberculosis_ leva de 18 a 24 horas para fazer o mesmo. Essa diferença muda a forma inteira da curva: a enterobactéria tem lag curta e uma fase log íngreme, entrando rapidamente em estacionária por esgotamento de nutriente; a micobactéria tem lag prolongada, log de inclinação baixa e muito alongada, e uma fase estacionária longa povoada de células em estado de latência.

A primeira consequência é o tempo de resultado. Uma colônia só se torna visível a olho nu quando reúne algo em torno de 10⁸ células empilhadas no mesmo ponto do ágar. Partindo de uma única célula, uma bactéria que duplica em 20 minutos alcança essa marca em torno de nove horas de fase log, e por isso o laboratório entrega a leitura da placa em 18 a 24 horas — margem que cobre a lag e o crescimento a partir de inóculo escasso. Com duplicação de um dia, a mesma conta leva semanas, e é essa aritmética, não a dificuldade técnica, que explica por que a cultura de micobactéria demora tanto.

A segunda consequência é onde o antibiótico morde. Um bacteriostático impede a proliferação, e o efeito dele é máximo exatamente onde a proliferação é máxima: na fase log. Vários bactericidas dependem da mesma janela por um motivo mecanístico mais estreito — o beta-lactâmico bloqueia a enzima que faz as ligações cruzadas do peptidoglicano, de modo que só mata a célula que está construindo parede naquele momento; uma célula parada, com parede pronta, não oferece alvo. Daí decorre a razão de associar um bacteriostático a um beta-lactâmico ser em geral desaconselhado: o primeiro trava a divisão e, ao fazê-lo, retira do segundo o alvo de que ele precisa, com antagonismo em vez de soma.

#atencao-box("Tolerância não é resistência", [
Uma subpopulação da fase estacionária entra em estado metabolicamente quase parado: são as células persistentes, e elas sobrevivem a concentrações de antibiótico que matam toda a população em fase log. A tentação é chamar isso de resistência — e o erro tem custo. A persistente é *geneticamente sensível*: seu genoma não carrega mutação nem gene de resistência, e o antibiograma da cepa dá sensível. Ela sobrevive por não estar fazendo nada que o antibiótico possa interromper, e volta a morrer com a mesma droga assim que retoma o crescimento. Por isso o problema que a tolerância gera é *recidiva após suspender o tratamento*, e a resposta é duração adequada de terapia — não troca de esquema.
])

Há ainda uma terceira leitura da curva, que liga crescimento a virulência. Em _Staphylococcus aureus_, os fatores que servem para *aderir* ao tecido — proteína ligadora de fibronectina, proteína ligadora de colágeno, fator de agregação, coagulase — são expressos predominantemente durante a fase exponencial, quando a bactéria está colonizando; já as toxinas que *destroem* tecido aparecem na fase estacionária, quando a população chega a alta densidade. A troca de programa é comandada por densidade populacional, o mecanismo de quórum: as células secretam continuamente um peptídeo sinalizador, e quando a concentração dele no meio ultrapassa um limiar — o que só acontece quando há bactéria suficiente — o sistema regulador liga os genes de toxina.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-23.png",
  largura: 62%,
  legenda: [Adesinas na subida da curva, toxinas no platô: a virulência não é um traço fixo da espécie, é um programa ligado em função da fase de crescimento.])

#subtopico("3.3 — Meios de cultura e isolamento: a química que escolhe quem cresce")

Toda a fisiologia das PARTES I e II está embutida na formulação de um meio de cultura, e a composição básica se lê como uma lista de respostas às exigências já levantadas. Hidrolisados de proteína entregam carbono e nitrogênio na forma orgânica que o quimiorganoheterotrófico exige; carboidratos oferecem substrato fermentável; tampões de fosfato seguram o pH contra o ácido da fermentação; indicadores como o vermelho de fenol e o vermelho neutro tornam essa acidificação visível; o citrato férrico revela o gás sulfídrico produzido; corantes e metais pesados inibem quem não interessa; e o ágar dá consistência sólida sem ser metabolizado por praticamente nenhuma bactéria de interesse médico, o que mantém as colônias separadas na superfície.

Combinando esses ingredientes obtêm-se três categorias funcionais. Meios *não seletivos* deixam crescer tudo o que for cultivável — o #sigla("TSA", [ágar tripticase-soja — meio rico não seletivo, base de vários outros meios]) e o ágar sangue, base rica acrescida de 5% de sangue de carneiro. Meios *seletivos e diferenciais* combinam inibidor e indicador. Meios de *enriquecimento*, como os caldos tetrationato e selenito, favorecem a multiplicação de um patógeno pouco numeroso antes da semeadura, aumentando a chance de encontrá-lo em material com flora abundante.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-30.png",
  largura: 56%,
  legenda: [MacConkey resolvido: sais biliares e cristal violeta como inibidores, lactose como único açúcar e vermelho neutro como indicador — colônia rosa fermenta lactose, colônia incolor não fermenta.])

O ágar MacConkey ilustra a lógica inteira. Sais biliares e cristal violeta inibem as Gram-positivas, cuja parede espessa e exposta é vulnerável a detergente e a corante catiônico; a lactose entra como único açúcar; o vermelho neutro reporta a acidificação. Sobram apenas Gram-negativas, já divididas por cor em fermentadoras e não fermentadoras de lactose. O ágar de _Salmonella_ e _Shigella_ leva a mesma lógica adiante — mais sais biliares e citrato de sódio para inibir também os coliformes, e tiossulfato com citrato férrico para marcar de preto quem produz gás sulfídrico.

O ágar chocolate resolve uma exigência nutricional mais fina: é ágar sangue aquecido a cerca de 80 °C, e o calor rompe as hemácias liberando dois fatores indisponíveis no sangue íntegro — o fator X, que é a hemina necessária para montar os citocromos, e o fator V, que é o próprio NAD, destruído por enzimas do ágar sangue comum. Bactérias incapazes de sintetizá-los, como _Haemophilus influenzae_, crescem no chocolate e não no sangue.

Nada disso funciona sem separar as células fisicamente. A técnica de esgotamento do inóculo arrasta a alça em quadrantes sucessivos, diluindo a suspensão até que no último quadrante cada célula depositada esteja longe o bastante das outras para gerar colônia isolada — o clone que vai para os testes bioquímicos. A incubação, por fim, reproduz as janelas da PARTE I: atmosfera compatível com a exigência de oxigênio da espécie, 35 a 37 °C, e 24 a 48 horas ditadas pelo tempo de geração.

#figura-nebli("/figuras/micro-02-fisiologia-crescimento-bacteriano/slide-40.png",
  largura: 44%,
  legenda: [Cada quadrante recomeça a partir de uma raspagem do anterior; a diluição em série é mecânica, feita com a alça.])

O passo mais recente da mesma ideia são os meios cromogênicos: em vez de ler acidificação, o meio traz um substrato incolor acoplado a um corante que só é clivado por uma enzima presente em determinada espécie, e a colônia adquire cor própria quando essa enzima existe. Numa única placa de urocultura, _E. coli_, _Klebsiella pneumoniae_, _Enterococcus faecalis_ e _Staphylococcus aureus_ saem em cores distintas, o que dispensa a bateria de confirmação.

#clinica-box("Urocultura: por que 24 horas e não duas", [
A paciente com disúria e febre inicia antibiótico empírico antes de o resultado sair, e a razão é aritmética: mesmo com duplicação de 20 minutos, a placa precisa acumular cerca de 10⁸ células por ponto para que a colônia apareça, o que consome a lag mais várias horas de fase log. Só então chegam juntas a contagem de colônias, que separa infecção de contaminação, a cor no meio cromogênico, que aponta a espécie, e o antibiograma. O tratamento empírico cobre exatamente esse intervalo imposto pelo tempo de geração.
])

#conclusao-box[
Uma única ideia atravessa este resumo: a bactéria converte recurso do meio em mais cópias de si mesma, e tudo o que se mede em bacteriologia é consequência dessa conversão. O mecanismo nuclear é a oxirredução — a célula arranca elétrons de um substrato e precisa entregá-los a alguém. Entregando ao próprio piruvato, fermenta e rende pouco; entregando a uma cadeia na membrana plasmática terminada em oxigênio ou nitrato, respira e rende muito; e é o aceptor disponível, somado às janelas de pH, temperatura, sal e ferro, que decide onde cada espécie vive. No plano da população essa conversão aparece como as quatro fases da curva, e a fase vira decisão: a lag explica a demora da cultura, a log é onde morde o antibiótico que exige célula em divisão, a estacionária produz as toxinas e as persistentes que fazem a infecção recidivar, e o tempo de geração fixa a escala de horas ou de semanas. A bancada materializa essa fisiologia — o meio entrega o que a PARTE I listou, o indicador lê o resíduo da PARTE II, a incubação respeita o relógio da PARTE III. O passo seguinte é natural: se a droga precisa encontrar a bactéria em determinado estado metabólico, o próximo tema é como essas drogas agem e como as bactérias escapam delas.
]
