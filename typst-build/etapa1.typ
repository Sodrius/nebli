#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
Todo antibiótico resolve o mesmo problema de mira: matar uma célula alojada no meio de células humanas, sem matar as vizinhas. A saída é sempre atacar uma estrutura que só existe na bactéria, ou que existe em nós com forma diferente o bastante para o fármaco não confundir.

A *PARTE I* percorre as quatro frentes possíveis desse ataque — parede, membrana, ribossomo e ácidos nucleicos — e mostra por que cada classe age onde age. A *PARTE II* muda o ponto de vista para o da bactéria: o que separa parar de matar, e as cinco saídas que ela encontra para deixar de morrer. A *PARTE III* leva tudo isso à bancada, onde suscetibilidade vira número, o número vira letra no laudo e a letra vira decisão.
]

#parte-title("PARTE I — O alvo seletivo: onde o antibiótico ataca e por que só a bactéria sofre", primeira: true)

#subtopico("1.1 — Toxicidade seletiva: atacar o que existe na bactéria e não em nós")

O princípio que organiza a farmacologia antibacteriana inteira chama-se *toxicidade seletiva*: a droga precisa ter afinidade muito maior por uma estrutura do micróbio do que por qualquer equivalente do hospedeiro. Paul Ehrlich chegou a ela em 1909 testando corantes que coravam treponemas e não tecidos humanos, e dela saiu o arsfenamina.

Duas origens diferentes convergem no mesmo efeito, e a nomenclatura separa as duas. *Antibiótico* é metabólito secundário produzido por um microrganismo — a penicilina vem do fungo _Penicillium notatum_, a estreptomicina de _Streptomyces griseus_, a polimixina de _Bacillus polymyxa_. *Quimioterápico antibacteriano* é composto de síntese química integral, sem origem biológica: as quinolonas e as sulfonamidas são os exemplos da aula. A distinção é de procedência, não de potência — a maior parte do arsenal em uso hoje é semissintética, um esqueleto natural quimicamente modificado.

Chamá-lo de *metabólito secundário* diz quando ele aparece: metabólito primário é o que a célula produz para crescer, e secundário é o que ela produz quando crescer já não é prioridade. A produção sobe na *fase estacionária*, com o nutriente escasso — o antibiótico é arma química de disputa entre microrganismos, não subproduto metabólico.

#figura-lateral("/figuras/micro-05-antibioticos-resistencia/slide-14.png",
  lado: "right",
  largura-figura: 33%,
  texto: [Numa cultura de _Pseudomonas aeruginosa_ acompanhada por 48 horas, o pigmento antimicrobiano só se torna detectável muito depois do pico de divisão celular: quem cronometra a produção é o esgotamento do meio, não o relógio da divisão.],
  legenda: [Metabólito secundário aparece na fase estacionária.])

A seletividade é possível porque existem exatamente quatro frentes em que a bactéria difere de nós. A *parede de peptidoglicano* não tem equivalente em célula humana. A *membrana citoplasmática* bacteriana tem composição lipídica e carga próprias, sobretudo no Gram-negativo, cuja membrana externa carrega #sigla("LPS", [lipopolissacarídeo — molécula da membrana externa do Gram-negativo, cuja porção lipídio A é o alvo das polimixinas e o componente tóxico da endotoxina]). O *ribossomo* bacteriano é 70S, montado de subunidades 30S e 50S, contra o 80S humano de 40S e 60S. E a *síntese de ácidos nucleicos* usa enzimas próprias — a DNA-girase não tem homólogo humano, e a via de produção de folato não existe em nós.

Onde essa diferença é grande, a margem terapêutica é larga; onde é estreita, a toxicidade nasce do mesmo mecanismo que dá a atividade. As polimixinas atacam a membrana lipídica, e membrana lipídica nós também temos: são nefrotóxicas e neurotóxicas por essa razão, não por impureza de formulação.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-41.png",
  largura: 44%,
  legenda: [Quatro endereços, e todo antibacteriano em uso ocupa um deles. Guardar a qual frente uma classe pertence já prediz três coisas: o espectro provável, se a ação será bactericida ou bacteriostática, e qual mecanismo de resistência é plausível naquela cepa.])

#subtopico("1.2 — A parede: β-lactâmicos e glicopeptídeos")

O β-lactâmico não fura a parede bacteriana. Ele impede que ela seja *fechada*, e quem a desfaz é a própria bactéria — a distinção parece sutil e explica o comportamento inteiro da classe.

A parede é uma malha de *peptidoglicano*, polímero de dois aminoaçúcares alternados — N-acetilglicosamina e ácido N-acetilmurâmico — cujas cadeias paralelas são amarradas por pontes peptídicas. Quem fecha essas pontes é a *transpeptidase*, também chamada #sigla("PBP", [proteína ligadora de penicilina — nome dado à transpeptidase da parede por ela ligar penicilina; é o alvo dos β-lactâmicos, e trocá-la por uma variante de baixa afinidade é o mecanismo do MRSA]), que reconhece a terminação *D-alanil-D-alanina* do precursor e usa a energia dessa ligação para formar a ponte cruzada. O anel β-lactâmico é mimético estrutural desse terminal: a enzima o aceita como substrato, abre o anel e fica acilada de forma irreversível no sítio ativo.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-45.png",
  largura: 40%,
  legenda: [No Gram-negativo o β-lactâmico atravessa a membrana externa por uma porina para alcançar o periplasma, onde a transpeptidase trabalha. Barrar essa entrada — perder a porina — é resistência sem que enzima nenhuma seja produzida.])

A partir daí nada novo se constrói, mas a demolição continua. A bactéria em crescimento mantém *autolisinas* ativas cortando o peptidoglicano para abrir espaço à inserção de material novo; sem reticulação repondo o que foi cortado, a malha perde resistência mecânica, a pressão osmótica interna vence e a célula lisa. Daí a consequência que a bancada confirma: o β-lactâmico é bactericida, mas *só contra bactéria em crescimento ativo* — em população estacionária o efeito praticamente desaparece.

Os glicopeptídeos atacam o mesmo processo por outro ponto. Vancomicina e teicoplanina não tocam na enzima: ligam-se à terminação D-Ala-D-Ala do precursor e a escondem, de modo que a transpeptidase não encontra substrato. É a diferença entre travar o operário e sequestrar o tijolo, e ela deixa de ser detalhe quando se olha a resistência.

#confusao-prevista(
  titulo: "Vancomicina não inibe a transpeptidase",
  aluno_acha: [o aluno encaixa o glicopeptídeo no molde da penicilina e supõe que os dois disputam a mesma enzima],
  mecanismo: [o β-lactâmico liga a *enzima*; o glicopeptídeo liga o *substrato*. Como o alvo da vancomicina é o dipeptídeo terminal do precursor, a bactéria resistente não precisa mutar enzima alguma: basta trocar o terminal D-alanil-D-alanina por D-alanil-D-lactato, e a afinidade despenca cerca de mil vezes enquanto a transpeptidase segue construindo a parede normalmente.],
)

O espectro dos glicopeptídeos é restrito a Gram-positivos, e não por falta de alvo. O Gram-negativo tem peptidoglicano — fino, mas tem —, protegido por uma membrana externa cujas porinas são canais estreitos; a vancomicina é grande demais para passar. O alvo existe, o acesso é que não.

Os β-lactâmicos distribuem-se em quatro famílias de espectros distintos. As *penicilinas* vão das naturais, restritas a Gram-positivos, às aminopenicilinas com alguma cobertura de Gram-negativo e às anti-estafilocócicas estáveis à penicilinase. As *cefalosporinas* percorrem cinco gerações que deslocam o espectro progressivamente para o Gram-negativo — a quinta é a que retoma o Gram-positivo com atividade contra #sigla("MRSA", [_Staphylococcus aureus_ resistente à meticilina — cepa que adquiriu o gene mecA e produz uma transpeptidase alternativa de baixa afinidade por β-lactâmicos]). Os *carbapenêmicos*, os mais estáveis à degradação enzimática, ficam reservados como última linha; o *monobactâmico* aztreonam cobre apenas Gram-negativos aeróbios.

#subtopico("1.3 — Ribossomo, ácidos nucleicos e membrana: as outras três frentes")

A mesma lógica de 1.2 — encontrar uma peça que só a bactéria tem — se repete dentro da célula, e o ribossomo é o alvo mais explorado. O ribossomo bacteriano é *70S*, de subunidades 30S e 50S; o humano é 80S, de 40S e 60S, e é a diferença de sequência do RNA ribossômico que permite o encaixe seletivo.

*Aminoglicosídeos* e *tetraciclinas* ligam-se ao 30S, mas fazem coisas distintas ali. A tetraciclina bloqueia a chegada do RNA transportador ao sítio A e a tradução para — efeito reversível, logo bacteriostático. O aminoglicosídeo liga-se ao RNA ribossômico 16S e causa *erro de leitura do códon*: a bactéria segue traduzindo, mas as proteínas saem com aminoácido trocado e, aberrantes, inserem-se na membrana, tornando-a permeável. É por isso que ele é bactericida e os outros inibidores de síntese proteica não são: ele não interrompe a fábrica, faz a fábrica produzir veneno.

#clinica-box("Por que o aminoglicosídeo falha no abscesso", [
A entrada do aminoglicosídeo depende de transporte ativo acoplado ao gradiente de prótons da membrana, e esse gradiente só se mantém com respiração aeróbia — em anaeróbio estrito o fármaco não é captado, por mais alto que seja o nível sérico. O interior de um abscesso reúne as condições que anulam a classe: hipóxia, pH ácido e flora anaeróbia. Daí a drenagem ser parte do tratamento, não complemento dele.
])

*Macrolídeos*, *lincosamidas* e *oxazolidinonas* ocupam o 50S: o macrolídeo trava a translocação do ribossomo no túnel de saída do polipeptídeo, e a linezolida impede a montagem do complexo de iniciação. Como os três compartilham a mesma região, uma única metilação desse trecho — pela enzima do gene _erm_ — derruba as três classes de uma vez.

Na frente dos ácidos nucleicos, as *quinolonas* inibem a *DNA-girase* e a *topoisomerase IV*, que desfazem o super-enrolamento gerado à frente da forquilha de replicação. Sem elas a forquilha trava, e o complexo enzima-DNA-fármaco libera extremidades quebradas — a quebra de fita dupla torna a classe bactericida. Guarde _gyrA_ e _gyrB_: a resistência à quinolona é, na maioria das cepas, mutação pontual em _gyrA_ ou no homólogo _parC_, nunca enzima que degrade o fármaco.

#figura-lateral("/figuras/micro-05-antibioticos-resistencia/slide-57.png",
  lado: "right",
  largura-figura: 40%,
  texto: [As *sulfonamidas* e a *trimetoprima* atacam a via do folato, e o par mostra o que é sinergia de verdade. A sulfonamida é análoga do #sigla("PABA", [ácido para-aminobenzoico — precursor que a bactéria usa para fabricar folato; a sulfonamida imita a sua estrutura]) e inibe a di-hidropteroato sintase; a trimetoprima inibe a di-hidrofolato redutase, dois passos adiante. Dois bloqueios *em série* derrubam o tetra-hidrofolato muito mais do que a soma dos bloqueios isolados.],
  legenda: [A célula humana não sintetiza folato: capta folato pronto da dieta por transportador. A via inteira que o fármaco bloqueia não existe em nós — é a seletividade mais limpa da farmacologia antibacteriana.])

As *polimixinas* fecham a lista atacando a membrana: peptídeos catiônicos que se ligam à carga negativa do lipídio A, deslocam os cátions que estabilizam a membrana externa e desorganizam a interna até a célula extravasar conteúdo. São detergentes, e por isso matam bactéria parada.

#table(
  columns: (0.95fr, 1.4fr, 0.72fr, 1.28fr),
  inset: 1.7pt,
  align: left + horizon,
  stroke: 0.5pt + gray-border,
  fill: (x, y) => if y == 0 { navy } else { none },
  text(fill: white, weight: "bold", size: 6.8pt)[Classe],
  text(fill: white, weight: "bold", size: 6.8pt)[Alvo molecular],
  text(fill: white, weight: "bold", size: 6.8pt)[Ação],
  text(fill: white, weight: "bold", size: 6.8pt)[Espectro],
  text(size: 6.8pt)[β-lactâmicos], text(size: 6.8pt)[Transpeptidase (PBP)], text(size: 6.8pt)[Bactericida], text(size: 6.8pt)[Varia com a família],
  text(size: 6.8pt)[Glicopeptídeos], text(size: 6.8pt)[Terminal D-Ala-D-Ala], text(size: 6.8pt)[Bactericida], text(size: 6.8pt)[Gram-positivos],
  text(size: 6.8pt)[Aminoglicosídeos], text(size: 6.8pt)[Subunidade 30S], text(size: 6.8pt)[Bactericida], text(size: 6.8pt)[Aeróbios],
  text(size: 6.8pt)[Tetraciclinas], text(size: 6.8pt)[Subunidade 30S], text(size: 6.8pt)[Bacteriostática], text(size: 6.8pt)[Amplo],
  text(size: 6.8pt)[Macrolídeos], text(size: 6.8pt)[Subunidade 50S], text(size: 6.8pt)[Bacteriostática], text(size: 6.8pt)[Gram-positivos e atípicos],
  text(size: 6.8pt)[Quinolonas], text(size: 6.8pt)[DNA-girase, topoisomerase IV], text(size: 6.8pt)[Bactericida], text(size: 6.8pt)[Gram-positivos e negativos],
  text(size: 6.8pt)[Sulfa + trimetoprima], text(size: 6.8pt)[Duas enzimas da via do folato], text(size: 6.8pt)[Bactericida], text(size: 6.8pt)[Amplo],
  text(size: 6.8pt)[Polimixinas], text(size: 6.8pt)[Lipídio A do LPS], text(size: 6.8pt)[Bactericida], text(size: 6.8pt)[Gram-negativos],
)

#parte-title("PARTE II — Matar ou parar, e as cinco saídas que a bactéria encontra")

#subtopico("2.1 — Bacteriostático × bactericida: uma razão, não um rótulo")

Duas medidas saem da mesma bateria de tubos. A #sigla("CIM", [concentração inibitória mínima — menor concentração do antimicrobiano capaz de impedir o crescimento visível do microrganismo após 18 a 24 horas de incubação]) é a menor concentração que impede o crescimento macroscópico. A #sigla("CBM", [concentração bactericida mínima — menor concentração capaz de matar praticamente todo o inóculo; obtida subcultivando em meio livre de antibiótico os tubos que não turvaram]) é a menor que não deixa sobrevivente: obtém-se semeando em meio sem antibiótico o conteúdo dos tubos límpidos e vendo qual deles não cresce mais.

A classificação nasce da relação entre as duas. Quando a CBM é próxima da CIM — na prática, até quatro vezes maior —, a concentração que inibe é praticamente a que mata, e o fármaco é *bactericida*. Quando a CBM está muito acima, inibir custa pouco e matar custa concentração inatingível: o fármaco é *bacteriostático*, e a eliminação fica por conta do sistema imune. Segue daí que a classificação não é identidade fixa da molécula — ela depende do par fármaco-microrganismo, e o cloranfenicol é bacteriostático para a maioria das bactérias e bactericida para _Haemophilus influenzae_.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-47.png",
  largura: 36%,
  legenda: [O conteúdo citoplasmático extravasando pela parede rompida é o desfecho da inibição da transpeptidase — e ele só ocorre porque a bactéria estava crescendo e as autolisinas seguiram cortando uma malha que ninguém repunha.])

Onde a imunidade funciona e o sítio é acessível, o bacteriostático resolve: congela a população e o hospedeiro faz o resto. Onde a defesa não chega — vegetação de válvula na endocardite, liquor com pouca opsonina e poucos fagócitos, paciente neutropênico —, exige-se bactericida, porque não há quem termine o serviço.

Isso define também a *fase da curva de crescimento* em que cada um rende mais. A cultura passa por fase lag, sem divisão; fase log, de duplicação exponencial; e fase estacionária, com o nutriente esgotado. O bacteriostático impede proliferação, e por isso rende ao máximo na fase log e quase nada na estacionária; o β-lactâmico depende da mesma fase log pela razão oposta, porque precisa da parede em remodelação para que a autólise apareça.

#atencao-box("Somar dois antibióticos pode subtrair efeito", [
Associar um bacteriostático a um β-lactâmico tende ao *antagonismo*: o bacteriostático trava a fase log, e é exatamente do crescimento ativo que o β-lactâmico depende para desencadear autólise — a população parada fica protegida da lise, e o resultado combinado é pior que o do β-lactâmico sozinho.

A sinergia previsível está noutro par: o β-lactâmico desorganiza a parede e facilita a travessia do aminoglicosídeo até a membrana, onde ele será captado. A regra que sai daí é que combinar faz sentido quando um fármaco *abre caminho* para o outro, ou quando dois alvos independentes reduzem a chance de uma mutação única conferir resistência aos dois — que é a lógica do esquema múltiplo e prolongado da tuberculose, imposto pelo tempo de duplicação longo e pelo nicho intracelular do bacilo.
])

#subtopico("2.2 — As cinco saídas: como a bactéria deixa de morrer")

O antibiótico *não induz* resistência: ele seleciona. A mutação ou o gene já existiam numa fração da população, e o fármaco elimina o restante, deixando a subpopulação resistente ocupar o espaço vazio. É por isso que subdose e tempo curto selecionam com tanta eficiência — matam o suficiente para abrir o nicho e de menos para esterilizá-lo.

A resistência pode ser *intrínseca*, propriedade da espécie anterior a qualquer exposição — a vancomicina que não atravessa a membrana externa do Gram-negativo é o exemplo canônico —, ou *adquirida*, surgida por mutação pontual ou pela chegada de um gene de fora. O veículo desse gene é tipicamente o *plasmídeo*, molécula circular de DNA com replicação autônoma que passa de uma bactéria a outra e costuma carregar vários genes de resistência de uma vez.

Os mecanismos formam uma lista fechada de cinco. O primeiro é a *inativação enzimática*: a bactéria produz uma enzima que destrói o fármaco antes que ele chegue ao alvo. A *β-lactamase* hidrolisa o anel β-lactâmico e o inutiliza; variantes de espectro estendido, as #sigla("ESBL", [β-lactamases de espectro estendido — variantes que ampliam a hidrólise às cefalosporinas de terceira e quarta gerações, deixando os carbapenêmicos como saída]), ampliam a hidrólise às cefalosporinas modernas; carbapenemases como a KPC atingem a última linha. Contra aminoglicosídeos o princípio é o mesmo com outra química: enzimas acetilam, adenilam ou fosforilam a molécula, e o produto modificado não se liga mais ao 30S.

O segundo é a *alteração do alvo*, o mais importante da aula. No MRSA o gene _mecA_ codifica a *PBP2a*, transpeptidase alternativa de afinidade baixíssima por β-lactâmicos: ela constrói a parede enquanto todas as PBPs normais estão bloqueadas. Como o que mudou foi o alvo, e não a estabilidade do fármaco, nenhum inibidor de β-lactamase recupera a atividade, e a resistência se estende a toda a classe. A lógica reaparece noutras frentes — mutação em _gyrA_ e _parC_ reduz a afinidade da quinolona, e a metilase codificada por _erm_ altera o 50S e derruba macrolídeo, lincosamida e estreptogramina juntos.

#clinica-box("MRSA: uma troca de peça que fecha a classe inteira", [
_Staphylococcus aureus_ carrega dois mecanismos de resistência a β-lactâmicos que costumam ser confundidos. A *penicilinase*, presente na quase totalidade das cepas, é uma β-lactamase que hidrolisa a penicilina G — e é contornável, seja por uma penicilina anti-estafilocócica estável à enzima, seja pela associação com um inibidor.

A resistência à meticilina é outra coisa. O gene _mecA_ chega dentro de um elemento genético móvel e codifica a PBP2a; o alvo passa a existir em duas versões, e a nova ignora o fármaco. Como não há enzima a inibir, a cepa é considerada resistente a *todos* os β-lactâmicos, com a exceção das cefalosporinas de quinta geração, desenhadas para ligar a própria PBP2a. Daí a vancomicina ocupar historicamente o lugar de tratamento padrão: ela ataca o substrato, não a enzima, e a troca de PBP não a afeta.
])

Os três últimos são de rota e de acesso. A *via alternativa* contorna o alvo em vez de mudá-lo: os genes _van_ fazem a bactéria sintetizar precursores terminados em D-alanil-D-lactato, o que remove uma ligação de hidrogênio do sítio de encaixe da vancomicina e derruba a afinidade cerca de mil vezes, sem prejuízo para a transpeptidase. A *redução da permeabilidade* fecha a entrada — perder uma porina específica basta para o carbapenêmico não alcançar o periplasma. E o *efluxo* usa bombas transmembrana que exportam o fármaco tão rápido quanto ele entra; como muitas têm especificidade larga, uma só produz resistência simultânea a classes sem parentesco químico.

#mini-resumo[Destruir o fármaco, trocar o alvo, contornar a via, barrar a entrada, bombear para fora. Cada uma dessas cinco saídas deixa uma marca própria no perfil do laudo — e é essa marca que o subtópico seguinte aprende a ler.]

#subtopico("2.3 — Ler o padrão como assinatura, e a contramedida do inibidor suicida")

Se cada mecanismo de resistência atinge um conjunto previsível de fármacos, o conjunto de resultados de um laudo pode ser lido ao contrário, do efeito para a causa. É a habilidade mais útil que a aula entrega, e ela começa por um par de resultados aparentemente contraditório.

Uma cepa *resistente à amoxicilina e sensível à amoxicilina com clavulanato* não é erro de bancada: é a assinatura da β-lactamase. A mesma molécula funciona quando acompanhada porque o acompanhante neutralizou a enzima que a destruía. O *ácido clavulânico* — como o sulbactam e o tazobactam — é um β-lactâmico praticamente sem atividade antibacteriana própria, desenhado para ser reconhecido pela β-lactamase e ligar-se a ela de forma irreversível. Ele é consumido no processo, e por isso se chama *substrato suicida*.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-60.png",
  largura: 42%,
  legenda: [Acima, a aminopenicilina sozinha é hidrolisada no periplasma antes de alcançar a PBP. Abaixo, o inibidor suicida ocupa e destrói a β-lactamase, e a mesma aminopenicilina chega intacta ao alvo. O que a associação restaura é o acesso, não a potência.])

#confusao-prevista(
  titulo: "Clavulanato não é o antibiótico da associação",
  aluno_acha: [o aluno lê "amoxicilina + clavulanato" como dois antibióticos somando espectro],
  mecanismo: [o clavulanato é inibidor de enzima, não antibacteriano. Ele só faz diferença quando o mecanismo de resistência *é* enzimático: não protege contra carbapenemase e não faz nada quando a resistência vem de alteração de alvo, como no MRSA, ou de efluxo. Inibidor de β-lactamase resolve resistência por β-lactamase — e apenas ela.],
)

Os demais padrões se organizam em degraus. Resistência às penicilinas e às cefalosporinas de terceira e quarta gerações, com carbapenêmico sensível, aponta β-lactamase de espectro estendido — e a saída é o carbapenêmico. Quando ele também cai, o mecanismo subiu para carbapenemase e o arsenal se reduz a polimixina, tigeciclina e combinações recentes. Resistência isolada às quinolonas, com β-lactâmicos preservados, aponta mutação em topoisomerase, porque nenhuma enzima bacteriana degrada quinolona. E resistência simultânea a classes sem parentesco químico levanta bomba de efluxo de espectro largo.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-123.png",
  largura: 36%,
  legenda: [Na mesma placa, o disco de ampicilina não produz halo e o de amoxicilina-clavulanato produz — leitura direta de β-lactamase. Repare também nas colônias crescendo dentro da zona de inibição do disco à direita: colônia satélite levanta cultura polimicrobiana, identificação equivocada ou heterorresistência, e obriga a reisolar antes de liberar o resultado.])

Cada degrau tem contramedida própria: o *avibactam*, com a ceftazidima, inibe carbapenemases fora do alcance do clavulanato, e o *cefiderocol* — cefalosporina ligada a um quelante de ferro — entra pelos sistemas de captação de ferro da bactéria, contornando porina e efluxo de uma vez.

#parte-title("PARTE III — O laboratório: de suscetibilidade a número, e de número a decisão")

#subtopico("3.1 — A CIM e como se chega ao número")

A CIM não é propriedade da bactéria como o formato da colônia. É o resultado de uma corrida padronizada entre a difusão do fármaco e a duplicação do microrganismo, e o valor só significa alguma coisa porque todas as variáveis dessa corrida foram fixadas de antemão por um comitê de normatização.

O método de referência é a *diluição em caldo*. Prepara-se uma série de tubos com *diluições duplas* do antimicrobiano — 1, 2, 4, 8, 16, 32 µg/mL —, semeia-se em cada um o mesmo inóculo padronizado e incuba-se a 35 ± 2 °C por 18 a 24 horas. A leitura é por turbidez: o primeiro tubo límpido, de menor concentração, é a CIM. A escala é geométrica e não decimal, o que significa que a resolução do método é de um degrau — um valor de 16 é vizinho imediato de um valor de 32.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-74.png",
  largura: 44%,
  legenda: [Os primeiros tubos estão turvos e o seguinte já está límpido: a CIM desta cepa de _E. coli_ para ampicilina é a concentração do primeiro tubo sem crescimento visível. O tubo-controle, sem antibiótico, atesta que o inóculo era viável — sem ele o resultado não pode ser liberado.])

Três padronizações sustentam o número, e cada uma tem razão mecanística. O *inóculo* é ajustado pela *escala 0,5 de McFarland*, suspensão de referência de cerca de 1,5 × 10⁸ unidades formadoras de colônia por mililitro, conferida por turbidez ou absorbância a 625 nm e diluída até o inóculo de trabalho, da ordem de 5 × 10⁵ por mililitro: inóculo denso demais consome o antibiótico e eleva falsamente a CIM. O *meio* é o Mueller-Hinton, pobre em timidina e em PABA, que antagonizariam as sulfonamidas, e com teor controlado de cálcio e magnésio, cátions que alteram a atividade de aminoglicosídeos e polimixinas. *Tempo e temperatura* são fixos porque a leitura compara populações que tiveram a mesma janela para crescer.

#mini-resumo[Inóculo padronizado, meio definido, tempo e temperatura fixos → o único fator que varia entre os tubos é a concentração do fármaco. É essa restrição que transforma turbidez em número comparável.]

#figura-lateral("/figuras/micro-05-antibioticos-resistencia/slide-91.png",
  lado: "left",
  largura-figura: 32%,
  texto: [As variantes trocam praticidade por custo. A *microdiluição em caldo* leva a mesma lógica para uma microplaca de 96 poços, testando doze antimicrobianos com oito diluições cada e leitura fotométrica. A *diluição em ágar* permite dezenas de isolados na mesma placa e resolve bactérias exigentes que não crescem bem em caldo. O *E-test* é uma fita com gradiente contínuo já calibrado: a elipse de inibição cruza a escala impressa exatamente no valor da CIM, unindo a praticidade da difusão ao resultado quantitativo da diluição.],
  legenda: [E-test: a elipse marca a CIM na escala.])

#subtopico("3.2 — Difusão em disco: o halo é a CIM lida ao contrário")

O método de Kirby-Bauer mede a mesma grandeza de 3.1 em outra unidade. Um disco de papel impregnado com massa conhecida de antimicrobiano é aplicado sobre o ágar recém-semeado; o fármaco difunde radialmente e forma um *gradiente de concentração* decrescente a partir do disco. A bactéria cresce por toda a placa, exceto onde a concentração local ainda estava acima da CIM — e a borda do halo marca justamente o ponto em que a concentração que difundiu igualou a CIM da cepa.

É por isso que diâmetro do halo e CIM são grandezas inversamente relacionadas: quanto menor a concentração necessária para inibir, mais longe do disco a inibição alcança. O halo mede inibição, exatamente como a CIM — não mede morte.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-116.png",
  largura: 50%,
  legenda: [O corte transversal explica por que a leitura tem de ser do halo *mais interno*. Perto do disco há inibição completa; adiante, crescimento retardado; depois, inibição apenas parcial. Só a primeira faixa corresponde à concentração acima da CIM, e é a única que a tabela de interpretação prevê.])

As variáveis de 3.1 reaparecem com efeito geométrico. A *profundidade do ágar* é fixada em torno de 4 mm — cerca de 25 mL em placa de 90 mm — porque camada mais rasa concentra o fármaco num volume menor e alarga o halo. O *inóculo* segue a escala de McFarland: suspensão densa demais devolve halo falsamente pequeno e pode converter cepa sensível em laudo resistente.

#confusao-prevista(
  titulo: "Halo maior não significa antibiótico melhor",
  aluno_acha: [o aluno compara diâmetros entre discos diferentes da mesma placa e conclui qual fármaco é mais potente],
  mecanismo: [o diâmetro depende de três coisas ao mesmo tempo: a CIM da cepa, a massa de fármaco no disco e a velocidade com que aquela molécula difunde no ágar. Moléculas grandes difundem mal e produzem halos pequenos mesmo com excelente atividade. A comparação entre discos só é legítima depois de cada diâmetro ser traduzido pela tabela de pontos de corte específica daquele par disco-espécie.],
)

Dois achados interrompem a liberação do resultado. *Halo duplo* significa zona interna de inibição completa e anel externo de crescimento parcial — mede-se o interno. *Colônias satélites* dentro da zona de inibição levantam cultura polimicrobiana, identificação incorreta ou heterorresistência, e obrigam a reisolar a partir da satélite, reidentificar e repetir. Semanalmente, o *controle de qualidade* com cepas de coleção de suscetibilidade conhecida — _E. coli_ ATCC 25922, _P. aeruginosa_ ATCC 27853 — confere se os halos ainda caem na faixa esperada, validando discos, meio e técnica.

#subtopico("3.3 — De S/I/R à escolha: o laudo é previsão, não veredito")

O laudo não afirma que o antibiótico mata a bactéria: afirma que a concentração alcançável no sítio, com a dose habitual, deve superar a CIM medida. É previsão farmacológica, e as premissas dela podem não valer no paciente da frente.

A tradução de milímetros e de µg/mL em letras é feita pelo *ponto de corte*, fixado por comitês como o #sigla("CLSI", [Clinical and Laboratory Standards Institute — comitê norte-americano que publica os pontos de corte de interpretação do antibiograma; no Brasil o equivalente é o BrCAST]) e, no Brasil, o BrCAST. O corte não é propriedade do fármaco: nasce do cruzamento da distribuição de CIM naquela espécie, da farmacocinética no sítio de interesse e do desfecho clínico observado — e por isso muda entre espécies, entre sítios e ao longo dos anos.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-120.png",
  largura: 57%,
  legenda: [A tabela é a peça que fecha a PARTE. Para cada par fármaco-espécie ela dá a massa do disco, a faixa de diâmetro em milímetros e o ponto de corte equivalente em µg/mL — as duas unidades convivem porque medem a mesma coisa. Repare que ampicilina e amoxicilina-clavulanato têm cortes distintos: são interpretações separadas, não o mesmo fármaco em duas doses.])

*Sensível* indica que a dose habitual alcança concentração suficiente no sítio; *Resistente*, que nem a dose máxima chega lá. *Intermediário* não é "meio sensível": é a faixa em que o sucesso depende de dose maximizada ou de sítio onde o fármaco se concentra, e é também a zona-tampão que absorve a variação técnica do método, impedindo que um milímetro de leitura mude a cepa de categoria.

#clinica-box("O mesmo número, dois laudos diferentes", [
O pico sérico em dose plena fica entre quatro e oito vezes acima da CIM da cepa sensível; no liquor exige-se perto de dez vezes; e na urina muitos fármacos se concentram dezenas de vezes acima do plasma, porque o rim os despeja concentrados na luz tubular. O mesmo valor de CIM pode então ser Sensível numa cistite e Resistente numa meningite — e a nitrofurantoína é o extremo disso: concentração urinária alta e sérica baixa a tornam boa em cistite e inútil em pielonefrite.
])

Entre os fármacos sensíveis, restam critérios que o laudo não mede: o *espectro mais estreito* poupa a microbiota comensal e reduz a pressão seletiva, a *penetração no sítio* elimina candidatos que o antibiograma aprovou, e a *imunidade do hospedeiro* decide se um bacteriostático basta. A *toxicidade de órgão* desempata — eritromicina é hepatotóxica, gentamicina é oto e nefrotóxica, tetraciclina deposita-se em dente e osso em formação, sulfonamida desloca bilirrubina da albumina e causa kernicterus no recém-nascido, cloranfenicol produz a síndrome do bebê cinzento no neonato que ainda não glicuroniza.

#atencao-box("Sensível no laudo não garante cura no paciente", [
O antibiograma testa bactéria em crescimento livre, em meio rico e sem barreira física. O paciente oferece o oposto em situações previsíveis: coleção purulenta não drenada, onde pH ácido e baixa tensão de oxigênio anulam classes inteiras; biofilme em cateter ou prótese, cuja matriz reduz a penetração; patógeno intracelular; tecido necrótico sem perfusão; imunossupressão. Falha terapêutica com laudo integralmente Sensível é, portanto, achado esperado — e o primeiro passo diante dela não é trocar o antibiótico, é procurar o foco a drenar ou o corpo estranho a retirar.
])

Prevenir resistência decorre do mecanismo de 2.2: como o antibiótico seleciona em vez de induzir, o que reduz a seleção é o espectro mais estreito possível, em dose plena e pelo tempo adequado — subdose e curso interrompido abrem o nicho sem esterilizá-lo. Reservar as classes de última linha preserva a alternativa para quando ela for a única.

#figura-nebli("/figuras/micro-05-antibioticos-resistencia/slide-126.png",
  largura: 58%,
  legenda: [Os três métodos lendo a mesma cepa. Diluição em ágar e em caldo entregam a CIM em µg/mL e a difusão entrega o halo em milímetros; a linha tracejada é o ponto de corte, e é ele que converte qualquer uma das três medidas na mesma letra do laudo.])

#conclusao-box[
Um princípio organiza a aula inteira: *toxicidade seletiva*. Quatro estruturas da bactéria diferem das nossas o bastante para servirem de alvo — parede, membrana, ribossomo 70S e maquinaria de ácidos nucleicos —, e cada classe ocupa uma delas. Saber a qual frente uma classe pertence prediz o espectro, a ação e a resistência plausível.

O mecanismo nuclear a levar embora é que *alvo e acesso são coisas distintas*, e a bactéria ataca qualquer um dos dois: destrói o fármaco com uma enzima, troca o alvo por uma versão que não o reconhece, contorna a via, fecha a porta de entrada ou bombeia para fora o que entrou. Cada uma dessas cinco saídas produz um perfil característico no laudo — o que torna o antibiograma legível ao contrário, do efeito para a causa.

Na clínica isso vira três leituras. Amoxicilina resistente com amoxicilina-clavulanato sensível é β-lactamase, e a associação resolve o caso. Resistência a toda a classe β-lactâmica sem reversão pelo inibidor é troca de PBP, como no MRSA, e a associação não resolve nada. E laudo Sensível com paciente que não melhora aponta problema de acesso — abscesso, biofilme, tecido necrótico —, não de escolha de molécula.

Fica em aberto a rota pela qual o gene de resistência viaja: ele quase nunca surge na cepa que o carrega — chega em plasmídeo, transposon ou integron, vindo de outra bactéria e às vezes de outra espécie. É essa mobilidade, e não a taxa de mutação, que explica a velocidade com que a resistência se espalha.
]
