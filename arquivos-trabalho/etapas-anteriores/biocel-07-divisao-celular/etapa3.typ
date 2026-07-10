#import "../typst-template/nebli_v2_apostila.typ": *

// etapa3.typ — Hemoglobina, 5 discursivas

#discursiva("Q1",
  [Explique mecanisticamente por que a curva de dissociação da hemoglobina
   tem formato sigmoide enquanto a curva da mioglobina é hiperbólica, e
   por que essa diferença é funcionalmente necessária para um
   transportador de oxigênio entre pulmão e tecido.],
  [Mioglobina é monomérica e tem afinidade alta constante pelo O₂ —
   curva hiperbólica satura cedo. Hemoglobina é tetramérica, com
   cooperatividade: ligar O₂ em uma subunidade desencadeia transição
   concertada T→R que aumenta a afinidade das outras três. O resultado
   visual é a sigmoide. Funcionalmente, isso permite à mesma proteína
   operar em dois modos — alta afinidade no pulmão (R, captura quase
   total em pO₂ ~100 mmHg) e baixa afinidade no tecido (T, libera ~25%
   do carregado em pO₂ ~40 mmHg). Sem multímero, não há cooperatividade;
   sem cooperatividade, a afinidade é constante e o transporte se torna
   ineficiente em um dos extremos.])

#discursiva("Q2",
  [Descreva o efeito Bohr e explique por que sua direção (curva
   deslocada para direita em pH baixo) é fisiologicamente coerente com
   a necessidade de entrega de O₂ a um tecido em atividade metabólica
   intensa.],
  [Tecido ativo gera ácido (lactato em hipóxia, CO₂ na oxidação
   aeróbica). H⁺ se liga a resíduos de histidina da hemoglobina
   (sobretudo βHis146), estabiliza o estado T, baixa a afinidade pelo
   O₂ e desloca a curva de dissociação para a direita. Resultado:
   mesmo pO₂ tecidual, mais O₂ é entregue ao tecido. A direção é
   fisiologicamente lógica — quanto mais ativo o tecido (mais ácido
   local), mais O₂ precisa, e mais a hemoglobina é instruída
   molecularmente a liberar. No pulmão, o pH sobe (CO₂ expirado),
   histidinas perdem o próton, T se desestabiliza, R volta a
   predominar e a hemoglobina recarrega.])

#discursiva("Q3",
  [Explique por que a hemoglobina fetal (HbF) tem afinidade pelo O₂
   maior que a HbA, identificando o mecanismo molecular responsável.],
  [HbF tem composição α₂γ₂ — a cadeia γ substitui a β da HbA. A cadeia
   γ tem aminoácidos ligeiramente diferentes na cavidade central do
   tetrâmero, onde se aloja o 2,3-BPG. Especificamente, falta uma das
   histidinas que ancoram fortemente o BPG. Consequência: HbF tem
   sensibilidade reduzida ao BPG, fica preferencialmente no estado R,
   e exibe afinidade maior pelo O₂ (P₅₀ ~19 mmHg vs ~26 mmHg da HbA).
   Funcionalmente, isso permite ao feto extrair O₂ da circulação
   materna na placenta — a HbF do sangue fetal "rouba" o O₂ que a
   HbA materna está justamente entregando. A maior afinidade não vem
   de "mais hemes" nem "ferro diferente"; vem da insensibilidade ao
   modulador alostérico BPG.])

#discursiva("Q4",
  [Em uma intoxicação por monóxido de carbono, explique por que a
   curva de dissociação dos hemes ainda ocupados por O₂ se desloca
   para a esquerda e qual é a consequência clínica desse fato.],
  [CO liga o Fe²⁺ do heme com afinidade ~220x maior que a do O₂,
   ocupando alguns sítios. Mas além de competir pelo sítio, o CO
   ligado em uma subunidade estabiliza a hemoglobina no estado R
   (alta afinidade), como o próprio O₂ faria. Os hemes restantes da
   mesma molécula, que ainda têm O₂, ficam então em conformação de
   alta afinidade — soltam menos O₂ no tecido. A curva de dissociação
   desloca-se para a esquerda. A consequência clínica é dupla: menos
   O₂ é transportado (porque CO ocupa sítios) E o pouco transportado
   é liberado com mais dificuldade no tecido (porque a afinidade dos
   hemes vizinhos subiu). Por isso a hipóxia tecidual na intoxicação
   por CO é tão grave proporcionalmente à fração de Hb afetada.])

#discursiva("Q5",
  [Um paciente com anemia falciforme entra em crise vaso-oclusiva
   durante uma infecção pulmonar com febre. Conecte mecanisticamente
   a infecção, a febre e a hipóxia local com a polimerização da HbS
   e a oclusão capilar, e justifique por que a hidroxiureia é
   eficaz no manejo crônico desses pacientes ao induzir síntese de HbF.],
  [A HbS difere da HbA por uma única troca: Glu6→Val6 na cadeia β,
   criando um ponto adesivo hidrofóbico na superfície da subunidade. Esse
   ponto só consegue se encaixar em uma cavidade complementar de outra
   HbS quando a molécula está no estado T (desoxigenada). Infecção
   pulmonar reduz a oxigenação sistêmica, febre aumenta a demanda
   metabólica do tecido (mais hipóxia local), e desidratação concomitante
   concentra a HbS dentro da hemácia. Os três fatores convergem para
   aumentar a fração de HbS em T e a probabilidade de encontros
   produtivos entre moléculas — polímeros longos e rígidos se formam,
   a hemácia perde flexibilidade, oclui capilares e causa infarto
   tecidual (a crise vaso-oclusiva). A hidroxiureia induz síntese
   reativada de HbF; como a cadeia γ não tem a mutação Val6, moléculas
   de HbF se intercalam entre as de HbS na linha de polimerização e
   interrompem o crescimento do polímero, reduzindo a frequência e
   gravidade das crises.])
