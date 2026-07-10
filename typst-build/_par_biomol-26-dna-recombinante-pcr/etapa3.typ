#import "../../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Por que a PCR só consegue amplificar um alvo se as sequências que o flanqueiam forem conhecidas de antemão? Explique pelo mecanismo.],
  [A PCR não copia DNA do zero: a polimerase só estende a partir de um iniciador já pareado ao molde. Os iniciadores são pequenos trechos de fita simples desenhados para parear, um em cada borda do alvo, e é o par deles que delimita a região amplificada. Para desenhar um iniciador é preciso conhecer a sequência onde ele vai parear — ou seja, as bordas. O miolo entre os iniciadores pode ser totalmente desconhecido, pois a polimerase o atravessa copiando pelo molde; mas sem conhecer os flancos não há como construir os iniciadores, e a reação não inicia.])

#discursiva("Q2",
  [No sistema de restrição-modificação, como a bactéria evita cortar o próprio DNA, já que ele contém as mesmas sequências que a enzima reconhece no DNA invasor?],
  [O sistema tem dois braços. A restrição é a enzima de restrição, que cliva o DNA em sítios de reconhecimento específicos — e degradaria também o cromossomo próprio, que tem esses mesmos sítios. A modificação resolve o problema: a bactéria metila bases específicas dentro de cada sítio do seu próprio DNA. A enzima de restrição não reconhece o sítio metilado e, por isso, não o cliva. O DNA do fago invasor chega sem essa metilação, é reconhecido como estranho e cortado. A metilação funciona, portanto, como um crachá de "próprio" que protege o genoma da bactéria.])

#discursiva("Q3",
  [Por que dois DNAs de espécies diferentes, cortados pela mesma enzima de restrição, conseguem se juntar? Qual é o papel da DNA ligase nessa junção?],
  [Uma enzima de restrição reconhece sempre a mesma sequência. Quando faz corte desalinhado, deixa em cada fragmento uma saliência de fita simples — as pontas coesivas. Como a sequência é a mesma, todo DNA cortado por aquela enzima fica com pontas idênticas e complementares entre si, não importa a espécie de origem. As saliências do fragmento humano pareiam espontaneamente com as do vetor bacteriano por pontes de hidrogênio. Esse pareamento, porém, é frágil. A DNA ligase entra para selar a ligação fosfodiéster no esqueleto de açúcar-fosfato (gastando ATP), unindo um 3'-OH a um 5'-fosfato e tornando a junção covalente e permanente.])

#discursiva("Q4",
  [Explique por que a Taq polimerase é, ao mesmo tempo, termoestável e pouco fiel — e em que situação essa baixa fidelidade se torna um problema sério.],
  [A Taq foi isolada de Thermus aquaticus, bactéria de fontes termais; por viver no calor, sua polimerase mantém a estrutura mesmo a 95 °C. Essa termoestabilidade é o que viabiliza a PCR automatizada: a enzima sobrevive aos ciclos de desnaturação e é adicionada uma só vez. Termoestabilidade, porém, nada diz sobre fidelidade. A Taq não tem atividade exonuclease 3'→5' de revisão, então não corrige a base que incorpora errada e segue em frente. O erro vira problema quando o produto será clonado e expresso ou sequenciado: um erro de cópia se fixa em todas as cópias seguintes, alterando a proteína. Nesses casos usam-se Pfu ou Pwo, que revisam.])

#discursiva("Q5",
  [Descreva os dois estágios da clonagem molecular e explique por que o fragmento de interesse não pode ser simplesmente colocado sozinho dentro da bactéria.],
  [A clonagem tem dois estágios. No primeiro, o fragmento de interesse (inserto) é ligado a um vetor — uma molécula de DNA capaz de se replicar dentro da célula, como um plasmídeo —, formando o DNA recombinante. No segundo, esse recombinante é introduzido numa bactéria competente (transformação); ao se dividir, a bactéria copia o vetor com o inserto a cada geração, e a colônia resultante é o clone. O inserto sozinho não funciona porque lhe falta uma origem de replicação: sem ela, a maquinaria de cópia da bactéria não o reconhece como algo a duplicar, e o fragmento se perde. É o vetor que fornece a origem de replicação e ainda o marcador de seleção que permite identificar as bactérias transformadas.])
