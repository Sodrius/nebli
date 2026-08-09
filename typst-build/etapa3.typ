#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Explique por que a glicoquinase da célula beta funciona como sensor de glicemia enquanto a hexoquinase dos demais tecidos não funcionaria nesse papel.],
  [A glicoquinase tem Km alto, em torno de 10 mM, e não é inibida pela glicose-6-fosfato. Na glicemia fisiológica ela trabalha em torno de metade da velocidade máxima, ou seja, na parte inclinada da curva: se a glicose sobe, a velocidade sobe junto. A hexoquinase tem Km baixo e já está saturada nessa mesma glicemia, então sua velocidade não muda quando a glicose aumenta. Uma enzima saturada informa sempre o mesmo valor, e por isso não serve de termômetro. Como a célula beta mede a glicemia pela quantidade de ATP que a oxidação gera, ela precisa de uma enzima cuja velocidade acompanhe o substrato.])

#discursiva("Q2",
  [Descreva a cadeia que liga a chegada da glicose à célula beta até a liberação do grânulo de insulina, indicando o efeito do ATP sobre o canal de potássio.],
  [A glicose entra pelo GLUT2 e é fosforilada pela glicoquinase em quantidade proporcional à glicemia. O piruvato gerado é oxidado na mitocôndria e o ATP se acumula. Esse ATP fecha o canal de potássio sensível ao ATP, que estava aberto no repouso. Com o potássio retido dentro da célula, a face interna da membrana perde negatividade e a membrana despolariza. A despolarização abre canais de cálcio dependentes de voltagem, o cálcio entra, e o cálcio dispara a fusão das vesículas de insulina com a membrana. Em paralelo, a glicemia alta aumenta a transcrição do gene da insulina.])

#discursiva("Q3",
  [Explique como uma única proteína cinase consegue interromper a síntese de glicogênio e ao mesmo tempo disparar sua degradação.],
  [As duas enzimas do glicogênio leem a mesma modificação covalente com sinais invertidos. A glicogênio-sintase é ativa quando desfosforilada e perde atividade ao receber fosfato; a glicogênio-fosforilase é o oposto, inativa na forma b desfosforilada e ativa na forma a fosforilada. Quando a proteína cinase A fosforila as duas, ela desliga a síntese e liga a quebra no mesmo movimento. A fosfoproteína fosfatase 1, ativada pela via da insulina, produz exatamente o efeito inverso. Esse arranjo impede que as duas vias funcionem juntas, o que consumiria ATP num ciclo fútil.])

#discursiva("Q4",
  [Justifique por que o hormônio tireoidiano mais abundante no plasma não é o que ocupa o receptor, e qual a vantagem fisiológica desse arranjo.],
  [A tireoide secreta cerca de vinte vezes mais T4 do que T3, mas o T4 tem baixa afinidade pelo receptor nuclear e funciona como pró-hormônio, uma reserva circulante de meia-vida longa. A conversão ocorre nos tecidos periféricos, por desiodases: retirar um iodo do anel externo gera T3 ativo, e do anel interno gera T3 reverso, inativo. A vantagem é que cada tecido decide localmente quanto hormônio ativo terá, sem depender de a glândula mudar sua secreção. Em doença grave ou jejum prolongado, a conversão pende para o T3 reverso e o gasto metabólico cai.])

#discursiva("Q5",
  [Compare o mecanismo de ação da adrenalina com o do cortisol, explicando a diferença de latência e de duração dos efeitos, e relacione essa diferença ao papel fisiológico de cada um.],
  [A adrenalina é hidrossolúvel e para na membrana. Ela ativa um receptor acoplado à proteína G, que liga a adenilil-ciclase; o AMPc gerado libera a proteína cinase A, que fosforila enzimas já existentes. Como o efeito é mudança de atividade de proteínas prontas, a resposta vem em segundos, e termina em segundos quando a GTPase, a fosfodiesterase e as fosfatases desligam cada degrau. O cortisol é lipossolúvel, atravessa a membrana e encontra o receptor de glicocorticoide preso à HSP90 no citoplasma. O complexo entra no núcleo e regula a transcrição, então o efeito exige horas e persiste por dias, porque a proteína sintetizada permanece. Por isso a adrenalina serve ao susto imediato e o cortisol, ao estresse que dura.])
