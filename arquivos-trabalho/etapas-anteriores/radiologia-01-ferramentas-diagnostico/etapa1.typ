#import "../typst-template/nebli_v2_apostila.typ": *

#intro-box[
  Toda imagem médica é uma sombra — o registro de uma única interação física entre um sinal e o corpo. Um aparelho de ultrassom escuta ecos; um tomógrafo mede o quanto um feixe de raios-X foi freado; uma ressonância ouve o sinal que os prótons de água devolvem dentro de um ímã. Cada método enxerga por uma física diferente, e é essa física — não um capricho — que decide o que ele mostra com nitidez, o que ele é simplesmente cego para ver, e quando vale a pena pedi-lo. Este resumo persegue essa ideia por três caminhos. Primeiro, as três físicas que separam os quatro grandes métodos e por que a pergunta clínica vem sempre antes do exame. Depois, cada método visto pelo seu par inseparável de talento e cegueira. Por fim, os recursos que refinam a leitura — o contraste, as fases, as janelas — e como tudo isso reaparece na decisão à beira do leito. A régua de fundo é uma só: entender a física é entender por que aquele exame, e não outro.
]

#parte-title("PARTE I — A pergunta clínica e as três físicas da imagem", primeira: true)

#subtopico("1.1 — A pergunta vem antes do aparelho")

Antes de qualquer máquina existe uma decisão que é clínica, não técnica: qual pergunta eu preciso responder nesta criança, neste trauma, nesta dor abdominal. O exame escolhido no impulso não apenas deixa de responder — ele gasta tempo, dinheiro e, em metade dos métodos, expõe o paciente à radiação sem retorno. Para disciplinar essa escolha existem diretrizes que pontuam, para cada cenário clínico, o quanto cada exame é adequado. O #termo-nota[ACR Appropriateness Criteria][diretrizes do Colégio Americano de Radiologia que pontuam, por cenário clínico, qual exame de imagem é mais adequado] usa uma escala simples de 1 a 9: de 1 a 3 o exame é considerado não apropriado para aquela situação, de 4 a 6 pode ser apropriado, e de 7 a 9 é apropriado. O que a escala materializa é o raciocínio que sustenta toda esta aula — o método certo é o que mostra melhor o que se procura, descontado o risco que ele impõe e a facilidade de obtê-lo.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-03.png",
  largura: 54%,
  legenda: [Os critérios de adequação do ACR pontuam cada exame de 1 a 9 para um dado cenário clínico: 1–3 não apropriado, 4–6 pode ser, 7–9 apropriado. A pergunta clínica escolhe o exame, não o contrário.])

#subtopico("1.2 — Três físicas, quatro métodos")

Há basicamente três maneiras de arrancar uma imagem do interior do corpo, e conhecê-las de saída organiza todo o resto. A primeira usa _som_: um pulso de ultrassom de alta frequência entra pela pele e o aparelho fica à escuta dos ecos que voltam cada vez que o som cruza a fronteira entre dois tecidos diferentes — é a #termo-nota[ultrassonografia][método que forma imagem a partir dos ecos de um pulso de ultrassom refletido nas interfaces entre tecidos] (#sigla("US", [ultrassonografia])). A segunda usa _raios-X_: um feixe atravessa o corpo e é freado — atenuado — em graus diferentes por osso, água, gordura e ar; o que escapa sensibiliza um detector do outro lado. Quando o feixe registra uma única projeção, temos a #termo-nota[radiografia][imagem de uma única projeção de raios-X, em que todas as estruturas no caminho do feixe se somam numa sombra plana] (#sigla("RX", [radiografia convencional])); quando o tubo gira em torno do paciente e um computador reconstrói cortes finos, temos a #sigla("TC", [tomografia computadorizada]). A terceira usa _campo magnético_: os prótons de hidrogênio, abundantíssimos na água e na gordura do corpo, alinham-se dentro de um ímã potente, são cutucados por ondas de rádio e devolvem um sinal enquanto relaxam de volta — é a #sigla("RM", [ressonância magnética]). A síntese que fica para toda a aula é que a imagem é a _sombra_ de uma dessas interações. Troque a física, e muda o que aparece.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-05.png",
  largura: 58%,
  legenda: [Os quatro métodos de base — RX, US, TC e RM — e, ao redor, as variações que derivam deles. Toda a família se organiza pelas três físicas: som, raios-X e campo magnético.])

#subtopico("1.3 — O eixo que atravessa tudo: radiação ionizante ou não")

Uma única propriedade divide os quatro métodos em dois campos e reaparece em cada decisão adiante: se o método usa ou não radiação ionizante. Raios-X são #termo-nota[radiação ionizante][radiação com energia suficiente para arrancar elétrons de átomos, podendo danificar o DNA e, a longo prazo, aumentar risco de câncer] — carregam energia bastante para arrancar elétrons das moléculas e, com isso, lesar o DNA. Por isso RX e TC têm um custo biológico que se acumula com a dose, e esse custo pesa muito mais na criança, cujas células em divisão são mais radiossensíveis e que tem a vida inteira pela frente para expressar um dano tardio, e na gestante, pelo feto. O ultrassom (som) e a ressonância (campo magnético e ondas de rádio) não empregam radiação ionizante — são, nesse eixo, seguros para repetir e para populações vulneráveis. Guardar de qual campo cada método vem é o primeiro filtro de segurança que o clínico aplica antes mesmo de pensar em qual mostra melhor.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-06.png",
  largura: 60%,
  legenda: [Os quatro métodos lado a lado. Cada um resolve bem uma faixa de densidades e é limitado justamente onde outro método brilha — a razão pela qual eles se complementam em vez de competir.])

#mini-resumo[A pergunta clínica precede o exame (ACR, escala 1–9). Três físicas geram os quatro métodos: som (US), raios-X (RX e TC) e campo magnético (RM). RX e TC usam radiação ionizante — custo que pesa em criança e gestante; US e RM, não.]

#parte-title("PARTE II — Os quatro métodos, cada um pelo seu talento e sua cegueira")

#subtopico("2.1 — Ultrassonografia: a imagem feita de ecos")

O transdutor do ultrassom faz duas coisas em rápida alternância: emite um pulso curtíssimo de som e, no intervalo, escuta o que volta. Cada vez que o pulso cruza a fronteira entre dois tecidos de densidades diferentes, parte dele é refletida de volta como eco. O tempo que o eco leva para retornar diz ao aparelho a _profundidade_ daquela interface; a intensidade do eco diz o quanto aquela estrutura reflete — sua #termo-nota[ecogenicidade][o quanto uma estrutura reflete o ultrassom; o que reflete muito aparece claro (hiperecoico), o líquido puro não reflete e aparece preto (anecoico)]. Estruturas que refletem muito aparecem claras (hiperecoicas); um líquido puro, como o conteúdo de um cisto ou a urina na bexiga, quase não reflete e aparece preto (anecoico). Daí saem os talentos do método. Como a imagem se forma em tempo real, o US é _dinâmico_ — vê o coração batendo, a alça peristaltando, e, pelo #termo-nota[Doppler][técnica de ultrassom que detecta a mudança de frequência do eco causada pelo movimento do sangue, mapeando fluxo e vasos], o sangue fluindo, porque o movimento do sangue muda a frequência do eco. É portátil e vai até o leito, não usa radiação e é imbatível para caracterizar líquidos e partes moles superficiais.

A mesma física que dá os talentos impõe a cegueira. Quando a diferença de densidade na interface é enorme — tecido contra _ar_, ou tecido contra _osso_ —, praticamente todo o som é refletido de uma vez, e nada chega ao que está atrás: forma-se uma #termo-nota[sombra acústica][zona escura atrás de uma estrutura que reflete ou absorve quase todo o som, como osso, cálculo ou gás intestinal] posterior. É por isso que gás em alça intestinal, pulmão cheio de ar e osso são barreiras para o ultrassom, e por que uma camada espessa de gordura, que atenua o som no caminho, degrada a imagem de pacientes obesos. A cegueira do US não é fraqueza do aparelho — é a impedância acústica das interfaces fazendo exatamente o que a física manda.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-11.png",
  largura: 64%,
  legenda: [US de abdome: fígado, pâncreas e veia cava inferior distinguidos pela ecogenicidade. Estruturas sólidas dão ecos organizados; vasos e líquidos aparecem escuros.])

#figura-lateral("/figuras/radiologia-01-ferramentas-diagnostico/slide-13.png",
  lado: "right",
  largura-figura: 40%,
  texto: [O osso barra o som — mas no recém-nascido a fontanela ainda é uma janela membranosa, sem osso fechado. Por ela o ultrassom alcança o cérebro sem radiação nem sedação, e por isso a ultrassonografia transfontanela é o primeiro exame do encéfalo do neonato.],
  legenda: [US transfontanela: a fontanela aberta como janela acústica.])

#subtopico("2.2 — Tomografia computadorizada: densidade virada tom de cinza")

Na tomografia, o tubo de raios-X gira em volta do paciente disparando feixes de vários ângulos, e detectores medem quanto de cada feixe sobrou depois de atravessar o corpo. Um computador cruza essas medidas e reconstrói cortes finos, atribuindo a cada pontinho da imagem um número que traduz o quanto aquele tecido _freou_ o feixe — a atenuação, medida em #termo-nota[unidades Hounsfield][escala de atenuação da TC: a água vale 0, o ar cerca de −1000, a gordura é negativa e o osso, muito positivo; cada valor vira um tom de cinza]. Por convenção, a água vale zero, o ar fica perto de −1000, a gordura é negativa e o osso, fortemente positivo. Cada número desses é então convertido num tom de cinza. Como o olho não distingue mil tons de uma vez, o radiologista escolhe uma #termo-nota[janela][faixa de valores de atenuação exibida como a escala de cinzas; a janela de parênquima realça partes moles, a janela óssea realça o osso]: a janela de parênquima espalha os cinzas na faixa das partes moles, a janela óssea os espalha na faixa do osso — a mesma aquisição, lida de dois jeitos.

Os talentos vêm dessa engenharia. A TC é rápida — uma varredura leva segundos, o que a torna o exame do trauma e da urgência, em que o paciente não coopera muito tempo. Tem altíssima resolução espacial, resolve detalhes finos e, por reconstruir volume, permite ver o mesmo corte nos planos axial, coronal e sagital. O custo é duplo e coerente com a física: por usar raios-X, entrega radiação ionizante — a TC é hoje a maior fonte de exposição médica —, e boa parte de suas aplicações depende de injetar contraste, que traz seus próprios riscos, como veremos.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-21.png",
  largura: 72%,
  legenda: [A mesma TC de crânio em duas janelas. À esquerda, a janela de parênquima realça o tecido cerebral; à direita, a janela óssea realça a calota. Trocar a janela é reler os mesmos números de atenuação.])

#subtopico("2.3 — Ressonância magnética: o sinal dos prótons de água")

A ressonância não usa raios nenhum. Ela aproveita que o corpo é feito majoritariamente de água e gordura, ambas ricas em prótons de hidrogênio, e que cada próton se comporta como uma minúscula bússola. Dentro do ímã potente do aparelho, essas bússolas se alinham; um pulso de ondas de rádio as inclina para fora do alinhamento; e, quando o pulso cessa, elas relaxam de volta devolvendo um sinal de rádio que a máquina capta. O detalhe decisivo é que a _velocidade_ desse relaxamento difere entre os tecidos, e é dessa diferença que nasce o contraste da imagem. Duas constantes descrevem o relaxamento e dão nome às duas sequências básicas. A regra prática vale mais que a física fina no primeiro contato: nas imagens ponderadas em #termo-nota[T1][sequência de RM em que a gordura aparece clara e a água/líquido aparece escuro; boa para detalhe anatômico], a gordura aparece clara e a água escura — excelente para anatomia; nas ponderadas em #termo-nota[T2][sequência de RM em que a água/líquido aparece claro; boa para detectar edema e lesões, que retêm água], a água aparece clara — e como quase toda lesão inflama e retém água, a T2 é a sequência que faz a doença brilhar. Quando a gordura clara da T1 atrapalha, aplica-se a supressão de gordura (#termo-nota[fat sat][supressão do sinal da gordura na RM, para que uma lesão não fique escondida pelo brilho do tecido gorduroso]), que apaga o sinal do tecido gorduroso e revela o que ele escondia.

O talento da RM é sua resolução de _contraste_ entre partes moles, insuperável — ela distingue substância branca de cinzenta no cérebro, enxerga a medula, a cartilagem, os detalhes do fígado —, e faz isso sem radiação ionizante. Os custos, de novo, saem da física. O exame é demorado, de vários minutos parado e sensível a movimento, o que obriga a sedar crianças pequenas e pacientes claustrofóbicos. E o campo magnético é intenso o bastante para _deslocar ou aquecer_ estruturas ferromagnéticas: um marca-passo, certos clipes e implantes metálicos são contraindicações que precisam ser rastreadas antes de o paciente entrar na sala. O contraste próprio da RM, o gadolínio, será visto adiante.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-24.png",
  largura: 74%,
  legenda: [O mesmo abdome superior em várias sequências de RM. Repare como a água (bile, líquor, urina) inverte de escura em T1 para clara em T2, e como o fat sat apaga o brilho da gordura — cada sequência conta uma parte da história.])

#subtopico("2.4 — Radiografia convencional: a sombra que se soma")

A radiografia é o método mais antigo e mais simples, e entendê-lo como _projeção única_ explica tudo. O feixe atravessa o corpo numa direção só e sensibiliza o detector do outro lado; todas as estruturas que estiverem no caminho — pele, músculo, osso, órgão — somam suas sombras numa imagem plana. Daí vêm os talentos: é rápida, barata, disponível à beira-leito, e resolve muito bem os extremos de densidade — o osso, que freia muito o feixe e aparece branco, e o _ar_, que quase não o freia e aparece preto. Por isso o RX brilha no tórax, na detecção de gás livre na cavidade (o #termo-nota[pneumoperitônio][ar livre na cavidade peritoneal, sinal de perfuração de víscera oca; no RX em ortostase aparece como crescente de ar sob o diafragma]) e nos níveis hidroaéreos das alças. O limite é o reverso da mesma moeda: como as sombras se somam, uma lesão pode ficar _escondida_ atrás de outra estrutura — é a sobreposição —, a resolução de contraste entre partes moles é pobre, e não há cortes; tudo é um plano só. É exatamente essa sobreposição que a TC resolve, ao seccionar o corpo em fatias.

Reunindo os quatro, o quadro abaixo condensa o par talento–limitante de cada método — o cruzamento de dimensões que justifica sair da prosa para uma tabela.

#table(
  columns: (7em, 1fr, 1fr, 6em),
  inset: 7pt,
  align: left + horizon,
  stroke: 0.5pt + gray-border,
  fill: (_, row) => if row == 0 { navy } else { white },
  table.header(
    text(fill: white, weight: "bold", font: titulo-fam)[Método],
    text(fill: white, weight: "bold", font: titulo-fam)[Talento],
    text(fill: white, weight: "bold", font: titulo-fam)[Limitante],
    text(fill: white, weight: "bold", font: titulo-fam)[Radiação],
  ),
  [*US*], [Tempo real, dinâmico, leito, sem radiação; líquidos e partes moles], [Gás, gordura e osso barram o som (sombra acústica)], [Não],
  [*TC*], [Rápida, alta resolução espacial, cortes em qualquer plano], [Radiação; depende de contraste iodado (risco renal)], [Sim],
  [*RM*], [Resolução de contraste de partes moles insuperável], [Demorada; sedação; contraindicação ferromagnética], [Não],
  [*RX*], [Rápida, barata, leito; osso e ar], [Sobreposição; baixa resolução de moles; sem cortes], [Sim],
)

#confusao-prevista(
  titulo: "O ultrassom não é barrado por osso e gás por ser fraco",
  aluno_acha: [o aluno tende a achar que o US falha em osso e gás porque o aparelho é pouco potente, e que bastaria aumentar a força],
  mecanismo: [a barreira é a diferença brutal de densidade na interface tecido–ar ou tecido–osso, que reflete quase todo o som de volta de uma vez. Nada sobra para alcançar o que está atrás, e forma-se a sombra acústica. É física da reflexão, não potência — por isso o remédio é mudar de método (TC, RM), não turbinar o ultrassom.],
)

#mini-resumo[US: imagem por ecos, ótima para líquidos e tempo real, cega para gás/gordura/osso. TC: atenuação em unidades Hounsfield virada cinza, rápida e detalhada, mas com radiação. RM: sinal dos prótons de água, contraste de moles imbatível e sem radiação, porém lenta e com risco ferromagnético. RX: projeção somada, ótima para osso e ar, limitada pela sobreposição.]

#parte-title("PARTE III — Contraste, fases e a leitura na prática")

#subtopico("3.1 — Meios de contraste: por que uma estrutura passa a acender")

Contraste é qualquer substância introduzida no corpo que muda localmente a física do exame, destacando uma estrutura que, sem ela, se confundiria com a vizinhança. Na TC, o contraste é iodado e injetado na veia: o iodo é muito denso aos raios-X, então atenua fortemente o feixe e faz os vasos e os órgãos bem vascularizados _acenderem_ em branco. Esse mesmo iodo, porém, é eliminado pelos rins e pode precipitar uma #termo-nota[nefropatia por contraste][queda aguda da função renal desencadeada pelo contraste iodado, mais provável em quem já tem rim comprometido — motivo de checar a função renal antes] em quem já tem função renal comprometida, além de reações alérgicas — por isso a função renal é checada antes de injetá-lo. Na RM, o contraste é o gadolínio, também endovenoso, que age por outra via: ele encurta o T1 dos tecidos onde se acumula, fazendo-os brilhar nas imagens ponderadas em T1. Há ainda os contrastes que opacificam a _luz_ do tubo digestivo — o contraste via oral, que preenche e delimita as alças, e o via retal —, úteis para separar uma alça intestinal de uma coleção ou de um órgão adjacente.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-16.png",
  largura: 62%,
  legenda: [As formas de contraste na TC: sem contraste, com iodado endovenoso (que ainda se divide por fases) e com contraste na luz intestinal (oral ou retal). Cada opção responde a uma pergunta diferente.])

#subtopico("3.2 — Fases: o contraste é lido no tempo")

Depois de injetado na veia, o contraste iodado não ilumina tudo de uma vez — ele percorre a circulação, e o tomógrafo pode capturar a imagem em momentos distintos dessa viagem. Cada momento é uma _fase_, e escolher a fase é escolher o que se quer flagrar. Na fase arterial, adquirida logo após a injeção, o contraste ainda está nas artérias, e lesões muito vascularizadas se destacam. Na fase portal ou venosa, o contraste já banhou o parênquima — é a fase em que o fígado aparece mais homogêneo e a maioria das lesões hepáticas é avaliada. Na fase de equilíbrio, contraste e tecido se igualam; e na fase excretora, mais tardia, o contraste já foi filtrado e aparece dentro do sistema urinário. A ideia a fixar é simples: a fase não é um botão mágico, é apenas o _instante_ da aquisição depois da injeção, e cada instante conta uma parte diferente da circulação daquele contraste.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-19.png",
  largura: 70%,
  legenda: [As fases após o contraste iodado endovenoso — arterial, portal, excretora e tardia. É o mesmo paciente e o mesmo contraste, capturados em momentos diferentes da circulação.])

#subtopico("3.3 — Sequências que resolvem problemas específicos na RM")

A lógica das sequências da RM, vista na PARTE II, ganha aplicações elegantes quando combinada com o comportamento da água. A imagem em fase e fora de fase explora o fato de água e gordura, dentro de um mesmo ponto, ora somarem ora subtraírem seus sinais — o que denuncia gordura microscópica dentro de um tecido, como na esteatose hepática. E a #termo-nota[colangiorressonância][sequência de RM fortemente ponderada em T2 que mostra o líquido parado das vias biliares e pancreáticas como estradas claras, sem precisar injetar contraste] leva a ponderação em T2 ao extremo: como a bile é líquido praticamente parado, ela brilha intensamente, e as vias biliares e o ducto pancreático desenham-se como estradas claras sobre um fundo escuro — um mapa das vias sem uma gota de contraste e sem radiação. Cada uma dessas sequências é a mesma física de sempre, ajustada para fazer uma pergunta clínica precisa.

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-26.png",
  largura: 52%,
  legenda: [Colangiorressonância: a T2 pesada faz a bile parada brilhar, revelando as vias biliares como um mapa claro — sem contraste, sem radiação.])

#subtopico("3.4 — Como a física reaparece na decisão clínica")

Tudo o que foi visto se recolhe em algumas escolhas típicas, e é aí que a aula mostra sua utilidade. Diante de uma suspeita de obstrução intestinal, a radiografia simples de abdome em ortostase basta para muito: as alças distendidas e cheias de gás formam #termo-nota[níveis hidroaéreos][interfaces horizontais entre líquido e ar dentro de alças intestinais distendidas, vistas no RX em ortostase e típicas de obstrução], as interfaces horizontais entre líquido e ar que denunciam a parada do trânsito — exatamente porque o RX é imbatível para ar e é rápido. Diante de um paciente com déficit neurológico súbito, o exame de urgência é a TC de crânio sem contraste, porque é veloz e porque sangue agudo é espontaneamente hiperdenso, aparecendo branco sem precisar de contraste — decisivo para separar um AVC hemorrágico de um isquêmico. E para investigar as vias biliares sem invasão nem radiação, a colangiorressonância entrega o mapa. Em cada caso, a escolha não foi decorada: ela caiu por gravidade a partir da física do método e da pergunta que se precisava responder.

#clinica-box("Obstrução intestinal na radiografia de abdome", [
  Numa obstrução intestinal, o conteúdo para de progredir e se acumula antes do ponto obstruído; gás e líquido se separam por gravidade dentro das alças distendidas. Na radiografia feita com o paciente de pé (ortostase), essa separação aparece como níveis hidroaéreos — traços horizontais em degraus — e alças dilatadas. A imagem funciona justamente porque o RX resolve bem o ar e é obtido em segundos à beira do leito, sem preparo. É o método simples entregando um diagnóstico de urgência antes que qualquer exame mais sofisticado seja cogitado — e o exemplo mais direto de como conhecer a física guia a escolha certa.
])

#figura-nebli("/figuras/radiologia-01-ferramentas-diagnostico/slide-29.png",
  largura: 60%,
  legenda: [Radiografia de abdome em decúbito e em ortostase numa obstrução intestinal alta. Em pé, o ar e o líquido se separam nas alças distendidas e formam os níveis hidroaéreos.])

#conclusao-box[
  Um só princípio costura toda esta aula: _cada método de imagem enxerga o corpo por uma física distinta, e é essa física que decide, de uma vez, o que ele mostra, o que ele não pode ver e quando pedi-lo_. O ultrassom escuta ecos e por isso é dinâmico e sem radiação, mas cego para gás e osso; a tomografia mede a atenuação de raios-X e por isso é rápida e detalhada, ao preço da radiação; a ressonância ouve o sinal dos prótons de água e por isso distingue partes moles como nenhum outro, ao preço do tempo e do campo magnético; a radiografia soma sombras num plano e por isso é imediata para ar e osso, mas trai a sobreposição. Sobre essa base assentam os refinamentos — o contraste que faz uma estrutura acender, as fases que leem esse contraste no tempo, as janelas e sequências que reinterpretam os mesmos dados —, e é dela que descem as decisões da urgência: o RX na obstrução, a TC sem contraste no déficit neurológico agudo, a colangiorressonância nas vias biliares. Aprender radiologia começa, portanto, não por decorar aparelhos, mas por entender a interação física que cada imagem representa — porque é ela que, no fim, escolhe o exame.
]
