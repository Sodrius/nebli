#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Você acabou de comer uma fatia de pão. A glicose entrou na sua corrente sanguínea, foi captada por uma célula muscular, e em pouco tempo virou #sigla("CO_2", [dióxido de carbono]) e #sigla("H_2 O", [água]). A equação parece simples — glicose + oxigênio dão gás carbônico, água e energia — e é a mesma da combustão. Risque um fósforo num pedaço de papel: a química é idêntica, mas tudo vira calor de uma vez só. Na sua célula, a oxidação da glicose libera *exatamente* a mesma quantidade de energia (2.870 kJ por mol) — só que ela vai para outro lugar.

A pergunta que organiza este resumo é: *como a célula extrai energia da queima sem queimar de verdade?* A resposta tem três peças, e cada PARTE pega uma.

Na PARTE I você vai entender por que a cadeia respiratória precisa *existir* — por que a célula fragmenta a oxidação em uma escada de pequenos passos em vez de fazer uma reação só. Vai conhecer as reações redox, os potenciais de oxirredução, e a anatomia básica da mitocôndria onde tudo acontece.

Na PARTE II a gente vai percorrer os quatro complexos da cadeia em ordem, entendendo o que cada um faz e por que NADH e #sigla("FADH_2", [forma reduzida da flavina-adenina dinucleotídeo — coenzima que carrega 2 elétrons]) rendem quantidades diferentes de ATP. Vai ver por que a Coenzima Q e o citocromo c são *carregadores móveis* entre complexos fixos, e por que o Complexo III precisa do "ciclo Q" para desemparelhar elétrons.

Na PARTE III entra o acoplamento — a teoria quimiosmótica de Peter Mitchell, que mostrou que a energia dos elétrons vira gradiente de prótons e o gradiente vira ATP via uma turbina molecular (a ATP sintase). Aí entram os inibidores (rotenona, cianeto, antimicina), os desacopladores (DNP — o emagrecedor que matou pessoas nos anos 30), e finalmente o saldo: por que dizem "38 ATP por glicose", mas o número moderno é mais perto de 30–32. Fechamos com uma tabela de referência rápida com tudo organizado para consulta.
]

#parte-title("PARTE I — Por que existe uma cadeia respiratória", primeira: true)

#subtopico("1.1 — Da queima térmica ao fracionamento controlado")

A pergunta certa aqui não é "como a célula faz ATP" — é uma anterior: *por que ela não pode simplesmente queimar a glicose?* A oxidação completa de 1 mol de glicose libera 2.870 kJ. O custo de fazer 1 mol de ATP é cerca de 30 kJ. Se toda a energia virasse trabalho, sairiam quase 100 ATP por glicose. A realidade biológica é mais perto de 30 — eficiência de aproximadamente 30%.

Não é desperdício; é exigência física. Se a célula liberasse 2.870 kJ de uma vez só, isso seria *fogo* — temperatura subindo centenas de graus, proteínas desnaturando, lipídeos derretendo. A vida não suporta isso. A célula precisa *fracionar* essa energia em pacotes pequenos o suficiente para serem capturados como trabalho útil (síntese de ATP) sem fundir a si mesma.

#figura-nebli("/figuras/cadeia-respiratoria/slide-01.png",
  largura: 80%,
  legenda: [A analogia é direta: a mitocôndria é uma usina de força que extrai energia de combustíveis (glicose, ácidos graxos) por uma sequência de transformações controladas. Não é diferente, em princípio, de uma usina termelétrica — só que cada passo aproveita uma fração da energia em vez de queimar tudo de uma vez.])

A solução evolutiva foi uma *escada* de transferências de elétrons, cada degrau liberando cerca de 20 kJ por mol. Esse é justamente o tamanho da energia necessária para bombear um próton através de uma membrana — o tipo de trabalho que enzimas conseguem fazer. Cada complexo da cadeia respiratória é um degrau dessa escada: aceita elétrons de uma molécula com potencial redox mais negativo, transfere para outra com potencial mais positivo, e usa a diferença para bombear prótons. No fim da escada, todo o gradiente acumulado vira ATP por uma turbina enzimática que a gente vai conhecer na PARTE III.

Antes de seguir, vale recolher uma peça de termodinâmica que apareceu nas reações químicas iniciais. *ΔG mede se uma reação ocorre espontaneamente* — ΔG negativo libera energia (acontece sozinha), ΔG positivo precisa de input para acontecer. Para o conjunto NADH → O₂, ΔG é fortemente negativo (cerca de -220 kJ/mol), e é justamente essa magnitude que torna a cadeia respiratória possível em todos os passos seguintes.

#mini-resumo[Em uma frase: *a célula fraciona a oxidação em degraus de ~20 kJ por mol* porque é a escala que enzimas conseguem aproveitar — e porque o resto seria calor destrutivo.]

#subtopico("1.2 — Reações redox e potenciais")

Imagine água escorrendo de uma cota alta para uma cota baixa. Quanto maior a diferença de altura, mais energia mecânica se pode extrair na descida. Trocar "altura" por "potencial elétrico" dá exatamente a lógica da cadeia respiratória: os elétrons "escorrem" do par com menor potencial padrão de oxirredução para o par com maior potencial, e a energia da descida é capturada como gradiente de prótons.

A regra básica: *oxidação é perda de elétrons; redução é ganho de elétrons*. Quando uma molécula doa elétrons (e se oxida), outra recebe (e se reduz). Sempre em pares — não existe elétron perdido no meio da reação. Para medir quanto cada par "quer" elétrons, usamos o #termo-nota[potencial padrão de oxirredução][medida da afinidade de um par redox por elétrons em condições padrão (1 M, pH 7, 25°C); quanto maior o E', maior a tendência do par a *receber* elétrons] (#sigla("E'", [potencial padrão de oxirredução em condições bioquímicas — pH 7, 25°C])).

O par #sigla("NAD+", [nicotinamida-adenina dinucleotídeo, forma oxidada — aceita 2 elétrons + 1 próton para virar NADH]) / NADH tem E' = -0,32 V. O par #sigla("O_2", [oxigênio molecular — aceptor final de elétrons da cadeia respiratória, recebe 4 elétrons + 4 prótons para formar 2 H_2 O]) / H₂O tem E' = +0,82 V. Quanto mais positivo o E', maior a "fome" por elétrons. Os elétrons fluem espontaneamente do par mais negativo (doador, "alto") para o mais positivo (aceptor, "baixo") — exatamente como a água da analogia.

Vale notar uma confusão comum: *potencial positivo* não significa *carga positiva*. O E' positivo significa que aquele par tem maior afinidade por elétrons — *quer* recebê-los. O elétron, que carrega carga negativa, é puxado para o E' mais positivo. A regra prática: descer a escala de E' (do mais negativo para o mais positivo) é descer energia — flui espontâneo. Subir contra a escala exige energia (não acontece sem input).

A energia liberada na transferência é proporcional à diferença de potencial, dada pela equação ΔG = -nFΔE, onde n é o número de elétrons (2 para NADH → O₂) e F é a constante de Faraday (96,5 kJ/V·mol). Para a diferença NADH → O₂ (1,14 V), o ΔG é de cerca de -220 kJ/mol — energia mais que suficiente para formar muitos ATPs, *se* fracionada corretamente.

#figura-nebli("/figuras/cadeia-respiratoria/slide-10.png",
  largura: 75%,
  legenda: [A escala de potenciais redox dos pares envolvidos na cadeia respiratória. Cada componente é colocado no degrau correspondente a seu E'. NADH (-0,32 V) lá em cima; O₂ (+0,82 V) lá embaixo. A energia da queda total é 1,14 V — aproveitada em ~20 kJ por bombeamento de próton.])

#subtopico("1.3 — Anatomia mitocondrial e os 6 atores")

Antes de entrar nos complexos, fixe o palco — porque é aqui que o aluno tropeça pela primeira vez. A mitocôndria tem *duas* membranas, e a confusão clássica é tratá-las como equivalentes; não são. A diferença anatômica entre elas é o que torna toda a quimiosmose possível.

A *membrana externa* tem porinas — proteínas formadoras de canais grandes que deixam passar moléculas até cerca de 10 kDa. Resultado: o *espaço intermembrana* é quimicamente equivalente ao citosol em pequenas moléculas e íons. Não há gradiente significativo de prótons entre os dois.

A *membrana interna* é o oposto: impermeável a íons (incluindo H⁺), com transporte seletivo via proteínas específicas. É justamente nessa impermeabilidade que a cadeia respiratória se apoia — bombear prótons para o espaço intermembrana cria um gradiente que *só* pode ser desfeito pela ATP sintase. A membrana interna se dobra em *cristas* para aumentar a área disponível para os complexos da cadeia.

#figura-nebli("/figuras/cadeia-respiratoria/slide-02.png",
  largura: 70%,
  legenda: [Mitocôndria animal de ~0,5 × 1,0 μm (do tamanho de uma bactéria — vestígio da origem endossimbiótica). Uma célula eucariótica típica tem ~2 mil mitocôndrias, ocupando 1/5 do volume celular. As cristas da membrana interna amplificam a superfície disponível para a cadeia respiratória.])

A *matriz* (espaço interno da mitocôndria) contém as enzimas solúveis do #termo-nota[ciclo de Krebs][ciclo dos ácidos tricarboxílicos; oxida acetil-CoA em CO₂ gerando NADH, FADH₂ e GTP — abordado na aula imediatamente anterior], da β-oxidação, mais o DNA mitocondrial e ribossomos próprios — testemunhas da origem endossimbiótica de uma alfa-proteobactéria há cerca de 2 bilhões de anos. Aliás, é desse DNA mitocondrial que vem uma observação clínica importante que vai voltar na conclusão: 13 proteínas da própria cadeia respiratória são codificadas pelo mtDNA, herdadas exclusivamente pela mãe; mutações ali geram doenças como #sigla("MELAS", [encefalomiopatia mitocondrial com acidose lática e episódios stroke-like]) e #sigla("LHON", [neuropatia óptica hereditária de Leber]).

Cravados na membrana interna estão os *seis atores* da cadeia respiratória. Os primeiros quatro são os *complexos* (proteínas integrais grandes, fixas): o *Complexo I* (NADH:ubiquinona oxidorredutase) recebe elétrons do NADH; o *Complexo II* (succinato desidrogenase) recebe elétrons do succinato vindo do Krebs e gera FADH₂; o *Complexo III* (ubiquinol:citocromo c oxidorredutase) opera no meio; o *Complexo IV* (citocromo c oxidase) é o último — reduz O₂ a H₂O.

E os dois carregadores móveis: a *Coenzima Q* (ubiquinona, CoQ) é uma benzoquinona lipossolúvel que flutua dentro da bicamada e leva elétrons do Complexo I ou II para o III. O *citocromo c* é uma proteína periférica pequena e hidrossolúvel que leva elétrons do III para o IV no lado intermembrana.

#atencao-box("CoQ e citocromo c são os taxistas — não confunda com os complexos",
  [O leitor costuma listar 6 complexos quando descreve a cadeia. São apenas *4 complexos* + *2 carregadores móveis*. Os complexos são proteínas integrais grandes, fixas na membrana. CoQ é uma benzoquinona lipossolúvel — flutua dentro da bicamada. Cit c é proteína periférica solúvel — se desloca pela face externa da membrana interna, no espaço intermembrana. A mobilidade desses dois é o que permite o "shopping" de elétrons entre complexos em pontos diferentes da membrana.])

#mini-resumo[O que ficou de pé: *4 complexos fixos + CoQ móvel lipossolúvel + Cit c móvel hidrossolúvel = 6 peças*. NADH entra no I; FADH₂ (succinato) entra no II; ambos descarregam em CoQ; CoQ leva ao III; III passa para Cit c; Cit c entrega ao IV; IV reduz O₂ a H₂O.]

#parte-title("PARTE II — Os quatro complexos", primeira: false)

#subtopico("2.1 — Complexo I e Complexo II: duas portas de entrada")

Agora que a escada e os atores estão fixados, vamos descer cada degrau. O *Complexo I* é o maior da cadeia — uma proteína em forma de "L" com cerca de 42 cadeias polipeptídicas. Sua função é simples: receber 2 elétrons do NADH e transferi-los à Coenzima Q, bombeando prótons no processo. O caminho dos elétrons dentro do complexo é uma sequência: NADH entrega 2 e⁻ + 1 H⁺ a uma molécula de #sigla("FMN", [flavina mononucleotídeo — grupo prostético do Complexo I que aceita os elétrons do NADH]) que vira FMNH₂; os elétrons então descem por uma cadeia de #termo-nota[centros ferro-enxofre][clusters de átomos de Fe e S inorgânico (2Fe-2S, 4Fe-4S) embebidos em proteínas; transferem elétrons via oxidação e redução do Fe sem usar grupo heme] (6 ou 7 centros 2Fe-2S e 4Fe-4S); por fim chegam à CoQ.

#figura-nebli("/figuras/cadeia-respiratoria/slide-21.png",
  largura: 75%,
  legenda: [Complexo I: o NADH entrega 2 elétrons + 1 próton ao FMN, que vira FMNH₂. Os elétrons descem por uma série de centros Fe-S até reduzir a CoQ. Por cada par de elétrons que atravessa, o complexo bombeia 4 H⁺ da matriz para o espaço intermembrana.])

A *exclusão de prótons* no Complexo I tem mecanismo elegante: os centros Fe-S aceitam apenas elétrons, não prótons. Quando o FMNH₂ entrega elétrons aos centros Fe-S, os 2 H⁺ que estavam ligados ao FMN são *liberados* (excluídos) — e a mudança conformacional resultante bombeia 4 H⁺ totais da matriz para o lado intermembrana por par de elétrons. Esse é o primeiro grande bombeamento da cadeia.

O *Complexo II* (succinato desidrogenase) é uma exceção interessante: é a *única enzima do ciclo de Krebs* que está fixada na membrana interna; as outras são solúveis na matriz. Sua função no Krebs é oxidar succinato a fumarato; nesse processo, o FAD do complexo se reduz a FADH₂. Como o FADH₂ está *dentro* do Complexo II, os elétrons já entram direto na CoQ — sem precisar passar pelo Complexo I.

#confusao-prevista(
  titulo: "Complexo II NÃO bombeia prótons — daí o P/O menor do FADH₂",
  aluno_acha: [aluno generaliza "todo complexo da cadeia bombeia prótons" — afinal, é o que I, III e IV fazem.],
  mecanismo: [o Complexo II bombeia *zero*. A razão é termodinâmica: o ΔG da transferência do FADH₂ para a CoQ é pequeno demais para vencer o gradiente. Por isso elétrons que entram pelo Complexo II (vindos do FADH₂ do succinato, do glicerol-3-fosfato, ou da acil-CoA da β-oxidação) acabam contribuindo com *menos* prótons no total — rendem ~1,5 ATP em vez de 2,5 do NADH.],
)

Uma nota clínica colateral: a *rotenona*, inseticida em desuso e tradicionalmente usada em modelos experimentais de doença de Parkinson, bloqueia justamente o Complexo I. Em sistemas com rotenona e succinato disponível, os elétrons do succinato entram pelo Complexo II e contornam o bloqueio — daí o succinato ser usado como "controle" em experimentos de oximetria. Em humanos, intoxicações por rotenona são raras mas catastróficas: encefalopatia, falência hepática, hipotensão refratária.

#mini-resumo[Em uma frase: *Complexo I bombeia 4 H⁺ por NADH; Complexo II bombeia 0 H⁺ por FADH₂*. Daí o NADH dar 2,5 ATP e o FADH₂ dar 1,5 ATP — diferença de 1 ATP que aparece em quase toda conta de saldo.]

#subtopico("2.2 — CoQ, ciclo Q e Complexo III")

O problema mecânico que aparece no meio da cadeia é específico: como passar 2 elétrons da Coenzima Q (que carrega 2 por vez) para o citocromo c (que carrega apenas 1 por vez)? A resposta é o *ciclo Q* do Complexo III — um mecanismo elegante de bifurcação que vamos destrinchar.

Primeiro o contexto. A *Coenzima Q* (ubiquinona, ou CoQ10 na forma humana com 10 unidades isoprênicas) é uma benzoquinona lipossolúvel — uma "pequena bolinha de óleo eletronicamente ativa" que flutua livremente dentro da bicamada da membrana interna. Sua mobilidade é essencial: ela é o ponto de encontro dos elétrons vindos do Complexo I (oriundos do NADH), do Complexo II (oriundos do FADH₂ do succinato), e ainda do FADH₂ de duas outras vias importantes — a desidrogenase da acil-CoA (β-oxidação de ácidos graxos) e a glicerol-3-fosfato desidrogenase (lançadeira citosólica do NADH, que vamos ver na PARTE III).

#figura-nebli("/figuras/cadeia-respiratoria/slide-27.png",
  largura: 75%,
  legenda: [A CoQ recebe elétrons de quatro fontes diferentes: Complexo I (do NADH), Complexo II (do succinato/Krebs), acil-CoA desidrogenase (da β-oxidação) e glicerol-3-fosfato desidrogenase (da lançadeira citosólica). Ela funciona como hub central, e por isso sua deficiência (CoQ10 deficiente) gera quadros multissistêmicos.])

CoQ acumula 2 elétrons e vira CoQH₂ (ubiquinol). Aí entra a incompatibilidade: o próximo destino dos elétrons é o citocromo c, mas citocromo c — como todos os citocromos — só transporta *1 elétron por vez* via Fe³⁺/Fe²⁺ do grupo heme. Como passar 2 elétrons da CoQ para um carregador que só aceita 1?

A solução é o *ciclo Q* do Complexo III. A CoQH₂ se liga ao Complexo III num sítio chamado #sigla("Q_o", [sítio de oxidação da CoQ no Complexo III, do lado intermembrana]) (lado externo, intermembrana); um dos dois elétrons vai para o citocromo c via uma proteína Fe-S (Rieske) e citocromo c1 — esse vai para fora. O segundo elétron toma um caminho diferente: passa pelos citocromos b e desce de volta para outra molécula de CoQ no sítio #sigla("Q_i", [sítio de redução da CoQ no Complexo III, do lado da matriz]) (lado matriz), regenerando metade do estoque de CoQH₂. Resultado: para cada *par* de elétrons que atravessa o ciclo completo (duas voltas), 4 H⁺ são bombeados.

#figura-nebli("/figuras/cadeia-respiratoria/slide-33.png",
  largura: 85%,
  legenda: [O ciclo Q em duas etapas. Primeira: CoQH₂ entra em Qo, doa 1 e⁻ para Cit c, 1 e⁻ desce pelos citocromos b para Qi, formando semiquinona; 2 H⁺ liberados para fora. Segunda: nova CoQH₂ em Qo, 1 e⁻ para Cit c, 1 e⁻ para Qi onde a semiquinona vira CoQH₂ completa; mais 2 H⁺ para fora. Saldo: 2 e⁻ passam para Cit c, 4 H⁺ bombeados, CoQ regenerada parcialmente.])

Vale notar onde o ciclo Q *não* acontece — confusão recorrente. O mecanismo de bifurcação é específico do Complexo III, porque é só ali que existe a transição CoQ (2 elétrons) ↔ cit c (1 elétron). No Complexo I, o FMN aceita os 2 elétrons juntos do NADH e a transição para os centros Fe-S é gradual mas não bifurcada. Estender "ciclo Q" para outros complexos é generalização errada.

A *antimicina A*, antibiótico naturalmente produzido por Streptomyces, bloqueia justamente o sítio Qi do Complexo III. O resultado é dramático em oximetria: consumo de O₂ cai a zero, porque não há rota alternativa — todos os elétrons da cadeia precisam passar pelo Complexo III antes de chegar ao IV. Em medicina, antimicina não tem uso clínico em humanos (toxicidade alta) mas é ferramenta padrão em bancadas de pesquisa.

#subtopico("2.3 — Citocromo c e Complexo IV")

Este subtópico encerra a cadeia: o citocromo c entrega os elétrons ao Complexo IV, que finalmente reduz o O₂ a H₂O. E é justamente aqui que aparece a vulnerabilidade clínica mais perigosa de toda a cadeia, que vai voltar na PARTE III quando discutirmos inibidores.

O *citocromo c* é uma proteína extraordinariamente conservada — sequência quase idêntica entre humanos e leveduras, organismos separados por bilhões de anos. É pequena (cerca de 104 aminoácidos), tem um único grupo heme c (com Fe central), e fica frouxamente ligada à face externa da membrana interna mitocondrial. Sua função na cadeia é simples: pegar 1 elétron do Complexo III (via cit c1) e entregar 1 elétron ao Complexo IV. Para que 4 elétrons cheguem ao Complexo IV (necessários para reduzir 1 O₂), o citocromo c precisa fazer 4 ciclos completos — uma "ponte aérea" entre os dois complexos.

Uma propriedade colateral notável: em condições normais o cit c fica preso entre as membranas mitocondriais. Mas em estresse celular grave (dano por radiação, ROS excessivo, sinalização pró-apoptótica), poros se abrem na membrana e *cit c vaza para o citosol*. Lá ele se liga ao Apaf-1 e forma o apoptossomo — que ativa a caspase-9, iniciando a cascata da apoptose intrínseca. A mesma molécula que normalmente carrega elétrons para fazer ATP, quando deslocada do lugar, sinaliza morte celular programada. Esse é um dos exemplos mais elegantes da biologia de "função pela localização".

O *Complexo IV* (citocromo c oxidase) é o último elo. Recebe 4 elétrons (um de cada vez, do cit c), 4 prótons da matriz, e 1 molécula de O₂ — produzindo 2 H₂O. Tem 2 citocromos do tipo a (citocromos a e a3) e 2 íons cobre (CuA e CuB) como cofatores. Por cada par de elétrons (metade do necessário para reduzir 1 O₂), o Complexo IV bombeia 2 H⁺ adicionais para o espaço intermembrana. Para 1 O₂ inteiramente reduzido (4 elétrons), 4 H⁺ são bombeados no total.

#figura-nebli("/figuras/cadeia-respiratoria/slide-35.png",
  largura: 70%,
  legenda: [Complexo IV (citocromo c oxidase): recebe 4 elétrons (um de cada vez do cit c), 4 H⁺ da matriz, e 1 O₂. Saída: 2 H₂O + 4 H⁺ bombeados para o lado intermembrana. É o ponto final do consumo de oxigênio — daí o nome "respiração celular" para essa via.])

#atencao-box("Cianeto e CO bloqueiam o Complexo IV — letais imediatos",
  [Cianeto (CN⁻) e monóxido de carbono (CO) se ligam ao Fe do citocromo a3 do Complexo IV com afinidade muito maior que o O₂. Resultado: o O₂ não consegue ser reduzido, a cadeia para inteira, e em segundos a célula entra em colapso energético. Cianeto causa *hipóxia histotóxica* — o paciente tem O₂ disponível no sangue (vermelho-cereja, não consumido pelos tecidos), mas a célula não consegue usá-lo. Tratamento: nitrito de sódio (cria metemoglobina, que sequestra cianeto) + tiossulfato (acelera conversão a tiocianato eliminado pelo rim); hidroxicobalamina é alternativa moderna que sequestra cianeto formando cianocobalamina (B12).])

#mini-resumo[Resumindo aritmético: *Complexo I bombeia 4 H⁺ + Complexo III bombeia 4 H⁺ + Complexo IV bombeia 2 H⁺ = 10 H⁺ por par de elétrons vindo de NADH*. FADH₂: pula o I, então só 4 + 2 = 6 H⁺ por par. A razão 10:6 ≈ 1,67 é o que sustenta o P/O 2,5:1,5 na conta dos ATPs.]

#parte-title("PARTE III — Acoplamento, ATP sintase e clínica", primeira: false)

#subtopico("3.1 — Teoria quimiosmótica e força próton-motriz")

Até os anos 60, ninguém entendia *como* a energia dos elétrons virava ATP. Suspeitava-se de uma molécula intermediária ("X~P") que receberia a energia das oxidações e a passaria para o ADP — mas ninguém conseguia encontrá-la. Em 1961, Peter Mitchell propôs uma ideia radical: *não existe intermediário químico — o intermediário é o gradiente eletroquímico através da membrana*. Os experimentalistas resistiram por anos; Mitchell ganhou o Nobel sozinho em 1978 quando a evidência se acumulou.

A *teoria quimiosmótica* diz: a cadeia respiratória bombeia prótons da matriz para o espaço intermembrana, criando dois gradientes simultâneos. Um *químico* (a concentração de H⁺ é maior do lado de fora — ΔpH ≈ 0,5 unidades, lado externo mais ácido) e um *elétrico* (o lado externo fica positivo em relação à matriz — diferença de potencial ΔΨ ≈ 150 mV, lado externo positivo).

A soma desses dois é a #termo-nota[força próton-motriz][energia armazenada como gradiente combinado químico (ΔpH) e elétrico (ΔΨ) de prótons através da membrana mitocondrial interna; força que move H⁺ de volta para a matriz pela ATP sintase] (#sigla("PMF", [proton motive force — força próton-motriz, soma do gradiente químico e elétrico de H⁺])). Em ordens de grandeza: cerca de 0,2 V de energia armazenada por próton — equivalente a ~20 kJ/mol de H⁺. Total armazenado por mitocôndria funcional: suficiente para sintetizar dezenas de ATP por segundo.

#figura-nebli("/figuras/cadeia-respiratoria/slide-46.png",
  largura: 80%,
  legenda: [Teoria quimiosmótica de Mitchell. A cadeia respiratória bombeia prótons para fora; a membrana interna impermeável retém o gradiente. PMF = ΔpH (químico) + ΔΨ (elétrico). Os prótons só podem voltar pela ATP sintase, descarregando o gradiente como rotação mecânica que catalisa ATP.])

A consequência conceitual importante: o gradiente é o *intermediário energético*, não há molécula chamada X~P. Antes de Mitchell, a busca por uma molécula que carregasse a energia da cadeia para a síntese de ATP dominou a área por décadas. A resposta foi: *não existe*. O intermediário é físico (gradiente eletroquímico através de uma membrana), não químico (uma ligação fosfoanidrido qualquer). Essa foi a revolução conceitual — aceitar que biologia podia armazenar energia em algo que não fosse uma ligação química. Cloroplastos (fotossíntese) e bactérias usam o mesmo princípio.

#subtopico("3.2 — ATP sintase F0F1 e o binding change")

A ATP sintase é uma máquina molecular literalmente rotativa — uma das poucas estruturas conhecidas na biologia que gira como uma turbina mecânica. Tem duas partes principais ligadas por uma haste central, e o melhor jeito de visualizá-la é como um moinho d'água invertido: o "rio" são os prótons fluindo pelo gradiente; a "roda" é a ATP sintase; o "trabalho útil" é a síntese de ATP.

A subunidade *F0* (lê-se "F-zero" — a letra "o" vem de *oligomicina*, antibiótico que bloqueia essa parte) está embebida na membrana interna. É um canal de prótons em forma de roda — em humanos, 8 subunidades c formam um anel rotor. Cada próton que atravessa o anel força o rotor a girar 1/8 de volta.

A subunidade *F1* fica saliente para dentro da matriz, conectada a F0 por uma haste central (subunidade γ). F1 tem 3 sítios catalíticos (subunidades α e β alternadas). À medida que γ gira (impulsionado pela rotação de F0), os 3 sítios passam por 3 conformações diferentes (#sigla("L", [loose — sítio em conformação que liga ADP e Pi frouxamente]) loose → #sigla("T", [tight — sítio em conformação apertada onde ADP + Pi formam ATP espontaneamente]) tight → #sigla("O", [open — sítio em conformação aberta que libera o ATP recém-formado]) open).

#figura-nebli("/figuras/cadeia-respiratoria/slide-48.png",
  largura: 65%,
  legenda: [ATP sintase F0F1. F0 (na membrana) é o rotor de prótons; F1 (na matriz) é a estrutura catalítica. A haste γ central transmite a rotação de F0 para F1. Os 3 sítios catalíticos no F1 passam por L (loose, liga ADP+Pi) → T (tight, forma ATP) → O (open, libera ATP). Oligomicina liga-se ao F0 e impede a rotação.])

A descoberta de Paul Boyer (Nobel 1997) foi o *binding change mechanism*: a energia da rotação não forma a ligação do ATP — a ligação se forma *espontaneamente* no sítio T (apertado), porque ali ADP e Pi estão tão próximos que se ligam sozinhos. A energia da rotação é usada para *liberar* o ATP do sítio (abrindo o sítio para a conformação O). Em outras palavras, a ATP sintase não "faz" ATP no sentido literal — ela faz o ambiente onde ATP se forma e depois o expulsa. A analogia que ajuda: você não gasta energia juntando ímãs (eles se atraem); gasta energia para *separar* o ímã da chapa. A ATP sintase é o trabalho de separação.

#subtopico("3.3 — P/O, saldo final e lançadeiras")

Agora que temos os números dos prótons bombeados (10 H⁺ por NADH, 6 H⁺ por FADH₂) e o mecanismo da ATP sintase, podemos fechar a conta. A razão *P/O* (fosforilações por átomo de oxigênio reduzido) mede a eficiência da síntese de ATP por par de elétrons.

Em humanos: P/O ≈ 2,5 para NADH e ≈ 1,5 para FADH₂. A diferença sai dos prótons bombeados que vimos na PARTE II: 10 H⁺ por NADH ÷ 4 H⁺ por ATP (custo médio, contando transporte de ADP/ATP/Pi) ≈ 2,5. Para FADH₂: 6 H⁺ ÷ 4 H⁺/ATP ≈ 1,5.

O *saldo final por glicose* depende de duas variáveis: quantos NADH e FADH₂ chegam à cadeia, e qual *lançadeira* é usada para o NADH gerado no citosol. A membrana interna mitocondrial é impermeável ao NADH. Como o NADH é gerado pela glicólise no citosol, ele precisa entregar seus elétrons para o interior mitocondrial sem atravessar a membrana — por isso existem as #termo-nota[lançadeiras][sistemas de transporte que movem os equivalentes redutores do NADH citosólico para a matriz mitocondrial sem mover o NADH em si; existem duas em humanos] mitocondriais.

A *lançadeira malato-aspartato* (no fígado, rim, coração) transfere os elétrons gerando NADH matricial — preserva os 2,5 ATP por NADH. Resultado: cerca de 32 ATP por glicose. A *lançadeira glicerol-3-fosfato* (no músculo esquelético e cérebro) entrega os elétrons como FADH₂ no Complexo II — perde 1 ATP por NADH citosólico, rendendo só 1,5 cada. Resultado: cerca de 30 ATP por glicose.

#figura-nebli("/figuras/cadeia-respiratoria/slide-67.png",
  largura: 75%,
  legenda: [Lançadeira malato-aspartato (fígado, rim, coração). O NADH citosólico reduz OAA a malato; malato atravessa a membrana interna; na matriz, malato é re-oxidado a OAA gerando NADH mitocondrial. Mantém o P/O em 2,5 — saldo total ~32 ATP/glicose.])

#confusao-prevista(
  titulo: "O saldo de 38 ATP/glicose é número antigo, não atual",
  aluno_acha: [aluno decorou em livros mais antigos (ou tabelas resumidas) o número 38 ATP por glicose, e usa esse valor como saldo "moderno".],
  mecanismo: [o número 38 vinha de P/O = 3 para NADH e P/O = 2 para FADH₂ — valores clássicos *sem* contar o custo de transporte de ADP/ATP/Pi pela membrana. O valor moderno é P/O = 2,5 para NADH e P/O = 1,5 para FADH₂ (o ATP transport custa 1 H⁺ extra por molécula). Recalculando: cerca de 32 ATP com lançadeira malato-aspartato, cerca de 30 com lançadeira glicerol-3-fosfato. A diferença de 38 → 30-32 *não* é erro do cálculo antigo — é correção pela contagem real de prótons.],
)

#mini-resumo[Resumindo aritmético: *NADH = 2,5 ATP; FADH₂ = 1,5 ATP*. Saldo glicose ≈ 30–32 ATP (depende da lançadeira). Saldo glicose com lançadeira malato-aspartato = 2 ATP glicólise + 2 GTP Krebs + 8 NADH × 2,5 + 2 FADH₂ × 1,5 + 2 NADH citosólico × 2,5 ≈ 32.]

#subtopico("3.4 — Inibidores, desacopladores e quadros clínicos")

A cadeia respiratória é alvo de muitas moléculas tóxicas, alguns medicamentos e diversos agentes ambientais. Conhecer onde cada um atua é a chave para entender (e muitas vezes diferenciar diagnóstico de) os quadros clínicos correspondentes.

Os *inibidores* da cadeia bloqueiam complexos específicos. A *rotenona* (inseticida) bloqueia o Complexo I — pode ser "contornada" se houver succinato disponível (elétrons entram pelo Complexo II). O *amital*, um barbitúrico, também bloqueia o Complexo I. A *antimicina A* (antibiótico antiparasitário) bloqueia o Complexo III — não há contorno; consumo de O₂ cai a zero. O *cianeto* e o *CO* (monóxido de carbono) bloqueiam o Complexo IV — letais em segundos a minutos.

Os *inibidores da ATP sintase* bloqueiam não a cadeia diretamente, mas a síntese de ATP. A *oligomicina* é o protótipo — liga-se ao F0 e impede a rotação. Efeito secundário: como a sintase para, o gradiente cresce demais e *retroinibe* os complexos da cadeia. Consumo de O₂ também cai.

#figura-nebli("/figuras/cadeia-respiratoria/slide-43.png",
  largura: 80%,
  legenda: [Pontos de bloqueio da cadeia respiratória. Rotenona/amital no Complexo I; antimicina A no Complexo III; cianeto/CO no Complexo IV. Cada inibidor tem perfil clínico próprio dependendo de onde para o fluxo de elétrons.])

Os *desacopladores* são qualitativamente diferentes — eles não inibem nada, *furam* a membrana para os prótons. O *DNP* (2,4-dinitrofenol) é o protótipo. É lipossolúvel, pega 1 H⁺ no lado externo, atravessa a membrana, libera o H⁺ na matriz, volta. O resultado é catastrófico para a célula: o gradiente é dissipado tão rapidamente que a cadeia respiratória acelera ao máximo tentando recompor — *consumo de O₂ aumenta*, mas como os H⁺ não passam pela ATP sintase, *nenhum ATP é gerado*. Toda a energia da oxidação vira *calor*.

#atencao-box("Inibidor versus desacoplador: efeito oposto sobre consumo de O₂",
  [Distinção cobrada em todo experimento de oximetria. *Inibidor* (rotenona, antimicina, cianeto, oligomicina): consumo de O₂ vai a zero (cadeia parada ou ATP sintase parada com retroinibição). *Desacoplador* (DNP, FCCP, UCP1 fisiológica em adiposo marrom): consumo de O₂ vai ao máximo (cadeia tentando recompor gradiente que vaza). Em ambos os casos *não há síntese de ATP*, mas a diferença prática salva vidas: paciente com cianeto morre por colapso energético; paciente com DNP morre por hipertermia. Tratamentos completamente diferentes — não dá pra trocar.])

#clinica-box("DNP — o emagrecedor que matou pessoas",
  [Nos anos 1930, o DNP foi vendido como emagrecedor sem prescrição médica. Funcionava: pacientes perdiam peso rapidamente porque o metabolismo "queimava" gordura sem produzir ATP — toda a energia virava calor. O problema: a doses um pouco mais altas, a hipertermia atingia 42–43°C, levando à desnaturação proteica e morte. Centenas de mortes foram documentadas antes da retirada do mercado em 1938. Curiosamente, o DNP voltou ao mercado *ilegal* nos anos 2010 vendido por internet a fisiculturistas — com mortes continuando a aparecer em emergências de cardiotoxicidade e hipertermia. Mecanismo idêntico: desacoplamento da fosforilação oxidativa.])

Existem desacopladores *fisiológicos*: a *UCP1* (proteína desacopladora 1, ou termogenina) no #termo-nota[tecido adiposo marrom][tecido especializado em produção de calor por desacoplamento controlado da cadeia respiratória; abundante em neonatos para termorregulação e em hibernadores; presente também em humanos adultos em quantidades menores, identificado por PET-CT em 2009] gera calor controlado, especialmente importante em neonatos e mamíferos hibernadores.

#conclusao-box[
A cadeia respiratória existe porque a célula precisa extrair energia da queima da glicose *sem queimar de verdade* — *fracionando* a liberação de 220 kJ por NADH em degraus de cerca de 20 kJ cada, cada um aproveitado para bombear um próton através da membrana mitocondrial interna. Esse é o princípio unificador que atravessa as três PARTES: termodinâmica obriga o fracionamento; o fracionamento permite o bombeamento; o bombeamento permite o gradiente; o gradiente permite o ATP.

O mecanismo nuclear é o acoplamento *via gradiente*, descrito pela teoria quimiosmótica de Mitchell. NADH entra no Complexo I e gera 10 H⁺ bombeados (P/O ≈ 2,5). FADH₂ pula o I, entra direto na CoQ pelo Complexo II, e gera 6 H⁺ (P/O ≈ 1,5). CoQ e citocromo c são os carregadores móveis que conectam os 4 complexos fixos. O gradiente acumulado é consumido pela ATP sintase F0F1, que opera como turbina rotativa — F0 é o rotor de prótons na membrana, F1 é a estrutura catalítica saliente; Boyer mostrou que o trabalho é em *liberar* o ATP do sítio apertado, não em formá-lo.

Clinicamente, o conhecimento da cadeia explica quadros dramáticos — o *cianeto* bloqueia o Complexo IV gerando hipóxia histotóxica (sangue vermelho-cereja, paciente em colapso energético com O₂ disponível mas inutilizável); o *DNP* desacopla a cadeia gerando hipertermia letal (mecanismo do emagrecedor mortal dos anos 30, ainda mata fisiculturistas hoje). A distinção entre inibidores e desacopladores é decisão clínica concreta: dois pacientes em emergência com falência metabólica, sintomas parecidos, diagnósticos opostos e tratamentos completamente diferentes.

O próximo resumo da UC (Estrutura dos Ácidos Nucleicos) começa em um cenário aparentemente desconectado — mas o gancho está aqui. O DNA mitocondrial, vestígio da origem endossimbiótica que mencionamos na PARTE I, codifica 13 proteínas da própria cadeia respiratória que acabamos de estudar. Mutações nesse DNA (transmitidas exclusivamente pela mãe) geram doenças como MELAS e LHON. Ler ácidos nucleicos passa a ser ler, também, a história das mitocôndrias — e a história das proteínas que fazem cada um desses 10 + 4 + 2 + 2 = 16 prótons bombeados por molécula de glicose oxidada.
]

#mindmap-fechamento(
  tema: "CADEIA RESPIRATÓRIA",
  mensagem: "a célula fraciona a oxidação em ~20 kJ por passo — cada degrau bombeia um próton, e o gradiente vira ATP via uma turbina molecular",
  com-setas: true,
  estacoes: (
    (rotulo: "Premissa · termodinâmica", titulo: "Por que fracionar",
     fala: [220 kJ/mol de uma vez vira calor destrutivo — fracionar em ~20 kJ/mol é a única forma de extrair como trabalho], cor: "a"),
    (rotulo: "Mecanismo · 4 complexos + 2 carregadores móveis", titulo: "Cadeia bombeia prótons",
     fala: [NADH entra no Complexo I, FADH₂ no II; CoQ e cit c levam os elétrons; juntos bombeiam 10 H⁺ por NADH ou 6 por FADH₂], cor: "neutra", destaque: true),
    (rotulo: "Conversão · ATP sintase F₀F₁", titulo: "Gradiente vira ATP",
     fala: [prótons descem pela turbina F₀; o eixo γ gira F₁; binding change libera o ATP do sítio apertado — Boyer Nobel 1997], cor: "b"),
  ),
  rodape-titulo: "Saldo · quem bloqueia · onde se aplica",
  cartoes: (
    (titulo: "Quanto ATP por glicose", frase: [2 + 2 + 8 × 2,5 + 2 × 1,5 ≈ 30–32 ATP — depende da lançadeira do NADH citosólico (malato-asp = 32; glicerol-3-P = 30)]),
    (titulo: "Inibidor x desacoplador", frase: [inibidor para O₂ a zero (cianeto = morte súbita); desacoplador maximiza O₂ mas gera só calor (DNP = hipertermia letal)]),
    (titulo: "Mutações no DNA mitocondrial", frase: [13 proteínas da cadeia vêm do mtDNA — herança materna; MELAS e LHON são exemplos clássicos de doenças mitocondriais]),
  ),
)

// ============================================================
// TABELA MECANÍSTICA — referência rápida, 1 página inteira
// Canônico 2026-05-26: tema mecanístico ganha tabela final
// ============================================================
#pagebreak()

#block(width: 100%, fill: navy, inset: (x: 14pt, y: 10pt), radius: 4pt,
  text(font: titulo-fam, size: 14pt, weight: "bold", fill: white, tracking: 0.4pt,
    "TABELA MECANÍSTICA — CADEIA RESPIRATÓRIA"))

#v(8pt)
#text(font: corpo-fam, size: 8.5pt, style: "italic", fill: text-light,
  "Referência consolidada — 4 complexos + 2 carregadores móveis + ATP sintase, inibidores/desacopladores e saldos energéticos. Use como cola visual durante revisão.")
#v(10pt)

// ============================
// Tabela 1: Componentes da cadeia
// ============================
#text(font: titulo-fam, size: 10.5pt, weight: "bold", fill: teal, tracking: 0.3pt, "1. Os componentes da cadeia")
#v(4pt)

#table(
  columns: (1.1fr, 1.4fr, 1.3fr, 0.6fr, 0.9fr, 1.3fr),
  align: (left + horizon, left + horizon, left + horizon, center + horizon, left + horizon, left + horizon),
  stroke: 0.4pt + gray-border,
  inset: 5pt,
  fill: (col, row) => if row == 0 { navy } else { none },
  table.header(
    text(fill: white, weight: "bold", size: 8.5pt, "Componente"),
    text(fill: white, weight: "bold", size: 8.5pt, "Substrato/entrada"),
    text(fill: white, weight: "bold", size: 8.5pt, "Função"),
    text(fill: white, weight: "bold", size: 8.5pt, "H⁺"),
    text(fill: white, weight: "bold", size: 8.5pt, "Inibidor"),
    text(fill: white, weight: "bold", size: 8.5pt, "Cofatores"),
  ),
  text(size: 8.5pt, weight: "bold", "Complexo I"),
  text(size: 8.5pt, "NADH (matriz)"),
  text(size: 8.5pt, "NADH → CoQ via FMN e Fe-S"),
  text(size: 8.5pt, "4"),
  text(size: 8.5pt, "rotenona, amital"),
  text(size: 8.5pt, "FMN, 6-7 Fe-S"),

  text(size: 8.5pt, weight: "bold", "Complexo II"),
  text(size: 8.5pt, "succinato (Krebs)"),
  text(size: 8.5pt, "Succinato → fumarato; FAD → FADH₂ → CoQ"),
  text(size: 8.5pt, "*0*"),
  text(size: 8.5pt, "malonato (compete)"),
  text(size: 8.5pt, "FAD, Fe-S"),

  text(size: 8.5pt, weight: "bold", "Complexo III"),
  text(size: 8.5pt, "CoQH₂"),
  text(size: 8.5pt, "Ciclo Q: CoQH₂ → 2 cit c (bifurcação)"),
  text(size: 8.5pt, "4"),
  text(size: 8.5pt, "antimicina A"),
  text(size: 8.5pt, "cit b, c1, Fe-S (Rieske)"),

  text(size: 8.5pt, weight: "bold", "Complexo IV"),
  text(size: 8.5pt, "cit c reduzido"),
  text(size: 8.5pt, "4 cit c + O₂ → 2 H₂O (aceptor final)"),
  text(size: 8.5pt, "2"),
  text(size: 8.5pt, "cianeto, CO, sulfeto"),
  text(size: 8.5pt, "cit a, a3, CuA, CuB"),

  text(size: 8.5pt, weight: "bold", "CoQ (móvel)"),
  text(size: 8.5pt, "I, II, β-oxidação, G3P-DH"),
  text(size: 8.5pt, "Carregador lipossolúvel I/II → III"),
  text(size: 8.5pt, "—"),
  text(size: 8.5pt, "—"),
  text(size: 8.5pt, "benzoquinona com cauda isoprênica"),

  text(size: 8.5pt, weight: "bold", "Cit c (móvel)"),
  text(size: 8.5pt, "Complexo III"),
  text(size: 8.5pt, "Carregador hidrossolúvel III → IV"),
  text(size: 8.5pt, "—"),
  text(size: 8.5pt, "—"),
  text(size: 8.5pt, "heme c (Fe³⁺/Fe²⁺)"),

  text(size: 8.5pt, weight: "bold", fill: gold, "ATP sintase"),
  text(size: 8.5pt, "gradiente H⁺"),
  text(size: 8.5pt, "F₀ rotor + F₁ catalítico (binding change)"),
  text(size: 8.5pt, "—"),
  text(size: 8.5pt, "oligomicina (F₀)"),
  text(size: 8.5pt, "subunidades α, β, γ, c-ring"),
)

#v(10pt)

// ============================
// Tabela 2: Inibidores e desacopladores
// ============================
#text(font: titulo-fam, size: 10.5pt, weight: "bold", fill: teal, tracking: 0.3pt, "2. Inibidores e desacopladores — efeito clínico-experimental")
#v(4pt)

#table(
  columns: (1fr, 0.9fr, 0.7fr, 0.7fr, 1.8fr),
  align: (left + horizon, left + horizon, center + horizon, center + horizon, left + horizon),
  stroke: 0.4pt + gray-border,
  inset: 5pt,
  fill: (col, row) => if row == 0 { navy } else { none },
  table.header(
    text(fill: white, weight: "bold", size: 8.5pt, "Agente"),
    text(fill: white, weight: "bold", size: 8.5pt, "Alvo molecular"),
    text(fill: white, weight: "bold", size: 8.5pt, "Consumo O₂"),
    text(fill: white, weight: "bold", size: 8.5pt, "Síntese ATP"),
    text(fill: white, weight: "bold", size: 8.5pt, "Quadro clínico / contexto"),
  ),
  text(size: 8.5pt, "Rotenona / amital"),
  text(size: 8.5pt, "Complexo I"),
  text(size: 8.5pt, "↓ (contornável)"),
  text(size: 8.5pt, "↓"),
  text(size: 8.5pt, "Inseticida; modelo de Parkinson em animais; intoxicação rara"),

  text(size: 8.5pt, "Antimicina A"),
  text(size: 8.5pt, "Complexo III (Qi)"),
  text(size: 8.5pt, "0"),
  text(size: 8.5pt, "0"),
  text(size: 8.5pt, "Antibiótico Streptomyces; uso só em bancada"),

  text(size: 8.5pt, weight: "bold", fill: red-alert, "Cianeto / CO"),
  text(size: 8.5pt, weight: "bold", "Complexo IV (cit a3)"),
  text(size: 8.5pt, weight: "bold", "0"),
  text(size: 8.5pt, weight: "bold", "0"),
  text(size: 8.5pt, "Hipóxia histotóxica letal — incêndios, intoxicações; tratamento: nitrito + tiossulfato OU hidroxicobalamina"),

  text(size: 8.5pt, "Oligomicina"),
  text(size: 8.5pt, "ATP sintase (F₀)"),
  text(size: 8.5pt, "↓ (retroinibição)"),
  text(size: 8.5pt, "0"),
  text(size: 8.5pt, "Ferramenta de bancada; sem uso clínico"),

  text(size: 8.5pt, weight: "bold", fill: red-alert, "DNP"),
  text(size: 8.5pt, weight: "bold", "Membrana (perfura para H⁺)"),
  text(size: 8.5pt, weight: "bold", "↑↑ (máx)"),
  text(size: 8.5pt, weight: "bold", "0"),
  text(size: 8.5pt, "Hipertermia letal — emagrecedor proibido; ainda mata fisiculturistas no mercado ilegal"),

  text(size: 8.5pt, "UCP1 (termogenina)"),
  text(size: 8.5pt, "Membrana (canal H⁺ regulado)"),
  text(size: 8.5pt, "↑"),
  text(size: 8.5pt, "↓"),
  text(size: 8.5pt, "Fisiológica! Tecido adiposo marrom — termogênese em neonatos e hibernadores"),
)

#v(10pt)

// ============================
// Tabela 3: Saldo energético
// ============================
#text(font: titulo-fam, size: 10.5pt, weight: "bold", fill: teal, tracking: 0.3pt, "3. Saldo energético — P/O e ATP por glicose")
#v(4pt)

#grid(columns: (1fr, 1fr), column-gutter: 14pt,
  // Bloco esquerdo: P/O
  [
    #table(
      columns: (1fr, 0.6fr, 1.3fr),
      align: (left + horizon, center + horizon, left + horizon),
      stroke: 0.4pt + gray-border,
      inset: 5pt,
      fill: (col, row) => if row == 0 { teal } else { none },
      table.header(
        text(fill: white, weight: "bold", size: 8.5pt, "Equivalente"),
        text(fill: white, weight: "bold", size: 8.5pt, "P/O"),
        text(fill: white, weight: "bold", size: 8.5pt, "Por que"),
      ),
      text(size: 8.5pt, "NADH (matriz)"),
      text(size: 8.5pt, "2,5"),
      text(size: 8.5pt, "10 H⁺ ÷ 4 H⁺/ATP"),

      text(size: 8.5pt, "FADH₂ (succinato)"),
      text(size: 8.5pt, "1,5"),
      text(size: 8.5pt, "6 H⁺ ÷ 4 H⁺/ATP"),

      text(size: 8.5pt, "NADH (lançadeira MA)"),
      text(size: 8.5pt, "2,5"),
      text(size: 8.5pt, "vira NADH matricial"),

      text(size: 8.5pt, "NADH (lançadeira G3P)"),
      text(size: 8.5pt, "1,5"),
      text(size: 8.5pt, "vira FADH₂ no II"),
    )
  ],
  // Bloco direito: Saldo por glicose
  [
    #table(
      columns: (1fr, 0.6fr),
      align: (left + horizon, center + horizon),
      stroke: 0.4pt + gray-border,
      inset: 5pt,
      fill: (col, row) => if row == 0 { teal } else { none },
      table.header(
        text(fill: white, weight: "bold", size: 8.5pt, "Etapa"),
        text(fill: white, weight: "bold", size: 8.5pt, "ATP"),
      ),
      text(size: 8.5pt, "Glicólise (substrato-nível)"),
      text(size: 8.5pt, "+2"),

      text(size: 8.5pt, "Krebs (GTP)"),
      text(size: 8.5pt, "+2"),

      text(size: 8.5pt, "8 NADH × 2,5 (Krebs + PDH)"),
      text(size: 8.5pt, "+20"),

      text(size: 8.5pt, "2 FADH₂ × 1,5 (Krebs)"),
      text(size: 8.5pt, "+3"),

      text(size: 8.5pt, "2 NADH citosólico (MA)"),
      text(size: 8.5pt, "+5"),

      text(size: 8.5pt, weight: "bold", fill: navy, "TOTAL (lançadeira MA)"),
      text(size: 8.5pt, weight: "bold", fill: navy, "≈ 32"),

      text(size: 8.5pt, "TOTAL (lançadeira G3P)"),
      text(size: 8.5pt, "≈ 30"),
    )
  ]
)

#v(8pt)

#block(width: 100%, fill: rgb("#FDF8E8"), stroke: (left: 3pt + gold),
  inset: (x: 12pt, y: 8pt), radius: 3pt,
  [
    #set par(first-line-indent: 0em)
    #text(font: titulo-fam, size: 9pt, weight: "bold", fill: rgb("#8B6914"),
      "Memória de bolso — números que merecem ser decorados:")
    #v(3pt)
    #text(size: 8.5pt,
      "• ΔE total NADH → O₂ = 1,14 V → ΔG = -220 kJ/mol."
      + "  • Bombeamentos: I=4, II=0, III=4, IV=2 → 10 H⁺/NADH, 6 H⁺/FADH₂."
      + "  • Custo: ~4 H⁺ por ATP (3 na sintase + 1 no transporte ADP/ATP/Pi)."
      + "  • P/O: 2,5 para NADH, 1,5 para FADH₂."
      + "  • Glicose: 30-32 ATP."
      + "  • Boyer 1997 (binding change); Mitchell 1978 (quimiosmótica).")
  ]
)
