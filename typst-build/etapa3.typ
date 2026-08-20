#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Um paciente internado faz radiografia de tórax no leito e o laudo levanta suspeita de cardiomegalia. Explique, pelo mecanismo geométrico, por que essa suspeita precisa ser relativizada antes de qualquer investigação adicional.],
  [O feixe de raios X diverge a partir de uma fonte praticamente pontual, de modo que a sombra de uma estrutura cresce quanto mais afastada ela estiver do detector. No leito, o exame é feito em incidência anteroposterior, com o chassi sob as costas: o coração, que é anterior no mediastino, fica longe do detector e sua silhueta é ampliada. Na incidência posteroanterior o coração encosta quase no detector e a magnificação é mínima. O aumento observado pode ser inteiramente geométrico, e o índice cardiotorácico só é confiável na incidência posteroanterior.])

#discursiva("Q2",
  [Explique por que a aorta é nitidamente visível na radiografia de tórax e desaparece na radiografia de abdome, embora seja o mesmo vaso, com o mesmo calibre e a mesma parede.],
  [Um contorno na radiografia não existe pela estrutura em si, e sim pela diferença de atenuação entre ela e o que está encostado nela. No tórax, a aorta é cercada por pulmão, que é praticamente ar: a diferença entre densidade de água e densidade de ar é enorme, e a interface se desenha com clareza. No abdome, o mesmo vaso passa a ser cercado por gordura, músculo e vísceras, todos na faixa da água. Sem diferença de atenuação, não há interface a registrar, e o vaso se dissolve na vizinhança.])

#discursiva("Q3",
  [Sombra acústica posterior e reforço acústico posterior produzem efeitos opostos na imagem. Explique por que os dois decorrem da mesma variável física e o que cada um informa ao examinador.],
  [A variável é quanto feixe sobra para seguir adiante depois de atravessar uma estrutura. Um cálculo reflete quase todo o feixe incidente: falta energia para gerar ecos atrás dele, e o setor posterior fica preto — a sombra. Um cisto de conteúdo líquido reflete muito pouco: o feixe atravessa quase intacto e chega às estruturas posteriores mais forte que o feixe vizinho, que teve de cruzar parênquima. Elas devolvem ecos mais intensos e aparecem claras — o reforço. Sombra aponta para estrutura muito refletora, como cálculo, osso ou gás; reforço aponta para conteúdo líquido.])

#discursiva("Q4",
  [Ao trocar a janela de partes moles pela janela óssea, uma coleção que parecia hiperatenuante passa a parecer indistinguível do tecido vizinho. Explique por que esse fato não autoriza nenhuma conclusão sobre a atenuação real da coleção.],
  [A unidade Hounsfield de cada voxel é uma medida física registrada na aquisição, calculada a partir do coeficiente de atenuação do tecido em relação ao da água. Esse número não muda depois da aquisição. A janela e o nível são recurso apenas de exibição: eles escolhem qual faixa de atenuações recebe a escala de cinzas disponível, saturando em branco o que está acima e em preto o que está abaixo dela. Trocar a janela redistribui os tons exibidos, não os valores medidos. A decisão diagnóstica se toma pelo valor obtido com o cursor.])

#discursiva("Q5",
  [Explique, pelo mecanismo dos dois relaxamentos, por que a gordura aparece branca nas imagens ponderadas em T1 e a água aparece branca nas imagens ponderadas em T2 — e por que o gadolínio é usado sobretudo em sequências ponderadas em T1.],
  [Desligado o pulso, dois processos independentes correm juntos: o T1 recompõe a magnetização longitudinal entregando energia ao meio, e o T2 desfaz a magnetização transversal por perda de sincronia entre prótons vizinhos. A gordura tem T1 e T2 curtos; a água livre tem os dois longos. Na ponderação em T1, os pulsos se sucedem em intervalo curto: a gordura já se recompôs e devolve muito sinal, enquanto a água mal começou e devolve pouco — gordura branca, água preta. Na ponderação em T2, a leitura é tardia: a gordura já perdeu o sinal transversal e a água ainda o mantém — água branca. O gadolínio encurta acentuadamente o T1 do tecido onde se acumula, e é na ponderação em T1 que um T1 curto se traduz em mais sinal, produzindo o realce.])
