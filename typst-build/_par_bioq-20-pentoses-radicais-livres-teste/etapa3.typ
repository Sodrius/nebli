#import "../../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Explique por que a via das pentoses-fosfato é a única fonte de NADPH da hemácia e qual a consequência dessa dependência.],
  [A hemácia não tem mitocôndria, então não dispõe das reações mitocondriais que geram NADPH em outras células; sua única maneira de produzir esse poder redutor é a fase oxidativa da via das pentoses, comandada pela G6PD. Como ela também carrega oxigênio — fonte contínua de espécies reativas — e não fabrica enzimas novas para repor as danificadas, depende inteiramente desse NADPH para manter a glutationa reduzida e proteger a hemoglobina e a membrana. Se o NADPH falha, a defesa antioxidante cai e a célula hemolisa.])

#discursiva("Q2",
  [Diferencie a fase oxidativa da fase não-oxidativa quanto à reversibilidade, à produção de NADPH e à função de cada uma.],
  [A fase oxidativa é irreversível: a G6PD e a 6-fosfogliconato desidrogenase oxidam a glicose-6-fosfato, produzindo dois NADPH, um CO#sub[2] e uma pentose. É a fase que fabrica poder redutor. A fase não-oxidativa é reversível e não produz NADPH; por meio da transcetolase e da transaldolase, ela apenas rearranja açúcares de três a sete carbonos, interconvertendo pentoses com frutose-6-fosfato e gliceraldeído-3-fosfato. Sua função é ajustar a oferta de ribose à demanda e conectar a via à glicólise nos dois sentidos, permitindo que a célula acione só o ramo de que precisa.])

#discursiva("Q3",
  [Explique como a G6PD se autorregula e por que esse mecanismo é eficiente para a célula.],
  [A G6PD é o passo controlador da via e responde ao próprio produto: o NADP#super[+] a ativa e o NADPH a inibe. O sensor real é a razão NADPH/NADP#super[+]. Quando a célula está cheia de poder redutor, o NADPH acumulado trava a enzima e a via desacelera, evitando fabricar o que não está sendo usado. Assim que uma via de construção ou a defesa antioxidante consome NADPH, o NADP#super[+] sobe, a inibição é aliviada e a via reacelera. É eficiente porque ajusta a produção ao consumo em tempo real, sem depender de nenhum sinal externo.])

#discursiva("Q4",
  [Descreva a cadeia causal que liga a atividade da G6PD à neutralização do peróxido de hidrogênio na hemácia.],
  [A G6PD gera NADPH na fase oxidativa da via. Esse NADPH é usado pela glutationa redutase para converter a glutationa oxidada (GSSG) de volta em glutationa reduzida (GSH). A GSH, por sua vez, doa elétrons ao peróxido de hidrogênio por meio da glutationa peroxidase, neutralizando-o em água. A cadeia é, portanto, direta: G6PD produz NADPH, o NADPH recarrega a glutationa, e a glutationa reduzida desarma o peróxido. Cada elo depende do anterior — se a G6PD falha, o NADPH não é reposto, a glutationa fica oxidada e o peróxido passa a corroer a célula.])

#discursiva("Q5",
  [Um paciente com deficiência de G6PD hemolisa após tomar primaquina, mas passava bem antes. Explique por que a crise só ocorre sob estresse oxidativo e por que a mesma mutação confere resistência à malária.],
  [Em repouso, a G6PD deficiente ainda produz NADPH suficiente para manter a glutationa reduzida, e a hemácia se sustenta. A primaquina é um oxidante: ela eleva bruscamente a produção de peróxidos, e a enzima insuficiente não repõe NADPH no ritmo necessário. A glutationa fica presa na forma oxidada, a hemoglobina se oxida e precipita em corpos de Heinz, a membrana é danificada e vem a hemólise — por isso a crise depende do gatilho. Quanto à malária, a mesma fragilidade da hemácia atrapalha o ciclo do Plasmodium falciparum dentro dela, dando resistência parcial; essa vantagem seletiva explica por que a mutação é frequente em áreas endêmicas.])
