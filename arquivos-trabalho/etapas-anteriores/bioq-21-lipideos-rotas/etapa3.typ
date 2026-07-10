#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [A ativação do ácido graxo gera AMP e pirofosfato, e o pirofosfato é logo hidrolisado pela pirofosfatase — uma reação da qual o ácido graxo nem participa. Por que essa hidrólise é decisiva para a ativação acontecer?],
  [A ativação (ácido graxo + ATP + CoA → acil-CoA + AMP + PPi) é, por si só, pouco favorável. Quem a empurra para frente é a hidrólise do pirofosfato a dois fosfatos pela pirofosfatase, fortemente exergônica. Ao remover o PPi do meio, ela puxa o equilíbrio no sentido da formação do acil-CoA. É um acoplamento clássico: a reação principal anda porque uma segunda reação consome um de seus produtos. O custo energético total da ativação passa a equivaler a dois ATP.])

#discursiva("Q2",
  [O ciclo de Lynen (β-oxidação) não consome oxigênio em nenhuma de suas quatro reações. Mesmo assim, ele não funciona em anaerobiose. Explique o aparente paradoxo.],
  [Cada volta da β-oxidação reduz uma molécula de FAD a FADH₂ e uma de NAD⁺ a NADH. Para a via continuar, essas coenzimas precisam voltar à forma oxidada (FAD e NAD⁺), e quem as reoxida é a cadeia respiratória, que no fim entrega os elétrons ao oxigênio. Sem O₂, os elétrons não têm para onde ir, FAD e NAD⁺ não se regeneram e a primeira reação de cada volta trava por falta de aceptor. O oxigênio não entra nas reações, mas é ele que mantém o ciclo girando.])

#discursiva("Q3",
  [A hemácia e o tecido nervoso praticamente não obtêm energia da oxidação de ácidos graxos. Explique o motivo em cada caso.],
  [São duas causas distintas. A hemácia madura não tem mitocôndria; como a β-oxidação e o ciclo de Krebs ocorrem na matriz mitocondrial, ela simplesmente não dispõe do compartimento e da maquinaria para queimar ácido graxo — depende da glicólise anaeróbia. O tecido nervoso tem mitocôndrias, mas os ácidos graxos de cadeia longa atravessam mal a barreira hematoencefálica e chegam pouco ao neurônio. Por isso o cérebro depende de glicose e, no jejum prolongado, dos corpos cetônicos, que são hidrossolúveis e cruzam bem essa barreira.])

#discursiva("Q4",
  [Que mecanismo molecular impede que a síntese e a degradação de ácidos graxos ocorram ao mesmo tempo na célula?],
  [O ponto-chave é o malonil-CoA, primeiro produto comprometido da síntese, formado pela acetil-CoA carboxilase. Além de doar carbonos à montagem do ácido graxo, o malonil-CoA inibe a CPT-1, a enzima que embarca o ácido graxo na carnitina para entrar na mitocôndria. Quando a síntese está ligada, há malonil-CoA, e a CPT-1 fica bloqueada: o ácido graxo recém-feito não entra para ser queimado. Assim a célula evita o ciclo fútil de construir e destruir ao mesmo tempo, que só gastaria ATP sem resultado líquido.])

#discursiva("Q5",
  [Um paciente tem uma queda de glicemia e, em resposta, uma descarga de adrenalina. Explique como esses dois sinais convergem sobre o metabolismo do triacilglicerol no tecido adiposo.],
  [A hipoglicemia faz o pâncreas liberar glucagon, enquanto o estresse libera adrenalina; os dois hormônios convergem sobre o adipócito pela mesma via. Ambos ativam receptores que elevam o AMPc, que ativa a PKA. A PKA fosforila e ativa a lipase hormônio-sensível, que quebra o triacilglicerol e libera ácidos graxos e glicerol. Os ácidos graxos vão pelo sangue, ligados à albumina, aos tecidos que os oxidam; o glicerol vai ao fígado alimentar a gliconeogênese. Em paralelo, a queda da insulina reduz o malonil-CoA, abrindo a CPT-1 e liberando a β-oxidação. O resultado é um corpo inteiro voltado a mobilizar e queimar gordura.])
