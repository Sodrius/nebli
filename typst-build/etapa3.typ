#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Explique por que a DNA-girase é um alvo antimicrobiano eficaz e por que a resistência às quinolonas costuma decorrer de uma única troca de aminoácido nessa enzima.],
  [A girase é a única enzima que introduz supertorção negativa, e essa torção paga a abertura das fitas na replicação e na transcrição. A fluoroquinolona não a inibe no sentido de pará-la: estabiliza o complexo de clivagem, estado em que a girase já cortou as duas fitas e ainda não religou, transformando cada complexo numa quebra dupla travada. A colisão da forquilha com essas quebras mata a célula. A troca da serina 83 por leucina elimina o contato que a droga usa nesse complexo: a enzima segue funcional, a droga perde afinidade.])

#discursiva("Q2",
  [Diferencie plasmídeo, transposon e integron quanto à autonomia de replicação e à mobilidade, e explique como os três se combinam para produzir multirresistência.],
  [O plasmídeo é replicon: tem origem de replicação própria e por isso se mantém e viaja entre células. O transposon não tem origem própria e só persiste inserido num replicon; o que faz é mudar de endereço, levando genes acessórios do cromossomo para o plasmídeo. O integron não se move nem replica sozinho: usa integrase para encaixar cassetes gênicos em série sob um único promotor. A combinação explica o achado clínico — cassetes dentro de integron, integron dentro de transposon, transposon dentro de plasmídeo conjugativo, várias resistências num só evento de transferência.])

#discursiva("Q3",
  [Compare a transdução generalizada e a especializada quanto ao mecanismo que as origina e ao conjunto de genes que cada uma pode transferir.],
  [Nascem de erros de máquinas diferentes. Na generalizada o erro é de empacotamento, no ciclo lítico: o cromossomo bacteriano é fragmentado e a maquinaria enche o capsídeo com um fragmento bacteriano em vez do DNA viral, de modo que qualquer gene pode ser transferido. Na especializada o erro é de excisão e pressupõe lisogenia: o prófago integrado num sítio específico se recorta deslocado e leva o DNA bacteriano adjacente. Como o sítio é fixo, o conteúdo é sempre o mesmo — só os genes vizinhos àquele ponto.])

#discursiva("Q4",
  [Justifique, a partir do mecanismo molecular da conjugação, por que a disseminação de resistência por plasmídeo é muito mais rápida que a seleção de mutantes resistentes.],
  [Na conjugação a relaxase corta uma fita na origem de transferência e a conduz pelo canal do sistema de secreção do tipo IV, enquanto a fita que fica na doadora serve de molde para replicação por círculo rolante. Ao final, cada célula tem um plasmídeo completo, e a receptora convertida passa a ser doadora: o número de doadoras cresce geometricamente sem depender de divisão celular. A mutação é rara por par de base e só se propaga por descendência, o que exige gerações sob pressão seletiva.])

#discursiva("Q5",
  [O sequenciamento de um isolado clínico revela um gene de β-lactamase do tipo TEM e uma substituição de aminoácido no produto de _gyrA_. Explique o que cada achado informa sobre a origem do mecanismo de resistência e justifique por que o resultado não dispensa o teste de sensibilidade.],
  [Os achados apontam origens distintas. O gene de β-lactamase é determinante adquirido: chegou por transferência horizontal, tipicamente em cassete de integron dentro de transposon alojado em plasmídeo conjugativo, e atravessa espécies sem parentesco entre os isolados. A substituição no produto de _gyrA_ é mutação de alvo, surgida na linhagem e propagada verticalmente sob pressão seletiva, que reduz a afinidade da quinolona pelo complexo de clivagem sem abolir a função da girase. O sequenciamento, porém, prevê o fenótipo em vez de medi-lo: o gene pode estar pouco expresso ou neutralizado por inibidor, e mutações não catalogadas escapam da comparação com banco de dados. Expressão, permeabilidade e efluxo só aparecem no teste de sensibilidade.])
