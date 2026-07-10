#import "../../typst-template/nebli_v2_apostila.typ": *

#set-etapa("Etapa 3 — questões discursivas")

#discursiva("Q1",
  [Explique, no nível do mecanismo, por que a deficiência grave de tiamina (vitamina B1) bloqueia simultaneamente o complexo da piruvato desidrogenase e a α-cetoglutarato desidrogenase, e por que isso é especialmente devastador para tecidos com alta demanda energética.],
  [A tiamina pirofosfato (TPP) é a coenzima essencial da E1 dos dois complexos. Ambos catalisam descarboxilação oxidativa por mecanismos idênticos — TPP estabiliza o carbânion intermediário, ácido lipóico transfere o grupo acila, FAD recupera o lipoil, NAD⁺ recebe os elétrons. Sem TPP funcional, a E1 não opera. Resultado: piruvato não vira acetil-CoA (PDH parada) e o ciclo trava na reação 4 (α-KG-DH parada), bloqueando o ciclo inteiro. Tecidos como cérebro e miocárdio, que dependem absolutamente da fosforilação oxidativa para sustentar bombas iônicas, falham primeiro — daí a encefalopatia de Wernicke e a cardiomiopatia do beribéri úmido.])

#discursiva("Q2",
  [Descreva como o íon Ca²⁺ funciona como elo de acoplamento entre a contração muscular e o aumento da produção mitocondrial de ATP, citando os pontos onde o Ca²⁺ atua na entrada e dentro do ciclo de Krebs.],
  [Durante a contração, o Ca²⁺ é liberado do retículo sarcoplasmático para o citosol e parte dele entra na mitocôndria via uniporter mitocondrial. Dentro da matriz, o Ca²⁺ ativa três pontos da via: a PDH fosfatase, que desfosforila e ativa o complexo da piruvato desidrogenase; a isocitrato desidrogenase, ponto regulatório-chave do ciclo; e a α-cetoglutarato desidrogenase. As três ativações elevam o fluxo de acetil-CoA e de elétrons para a cadeia respiratória. O Ca²⁺ é, portanto, um sinal mecânico-químico direto que casa o início da contração muscular com o aumento imediato da produção de ATP.])

#discursiva("Q3",
  [Por que a piruvato carboxilase, principal enzima anaplerótica do ciclo de Krebs no fígado, é virtualmente inativa na ausência de acetil-CoA? Qual a lógica fisiológica desse mecanismo regulatório?],
  [A piruvato carboxilase tem o acetil-CoA como ativador alostérico obrigatório — sem ele, fica desligada. A lógica é elegante: acetil-CoA acumulado indica que o ciclo não está conseguindo processá-lo. A causa mais comum é falta de oxaloacetato, consumido por vias biossintéticas (gliconeogênese, síntese de aspartato). O próprio acetil-CoA avisa: "preciso de mais OAA". A enzima então ativa, gera OAA a partir de piruvato + HCO₃⁻ + ATP, e a condensação inicial destrava. É um sensor que casa demanda anaplerótica com sinal real de gargalo metabólico.])

#discursiva("Q4",
  [Nenhuma das 8 reações do ciclo de Krebs utiliza oxigênio molecular diretamente. Explique então por que a interrupção do suprimento de O₂ paralisa o ciclo em poucos minutos.],
  [O ciclo gera 3 NADH e 1 FADH₂ por volta, e depende absolutamente da regeneração de NAD⁺ e FAD oxidados para continuar funcionando. Essa regeneração só acontece na cadeia respiratória, onde os elétrons descem dos carregadores reduzidos até o oxigênio molecular, aceptor final. Sem O₂, a cadeia trava no Complexo IV; o NADH não é reoxidado; o pool de NAD⁺ se esgota em minutos. Sem NAD⁺ disponível, as reações 3, 4 e 8 do ciclo (isocitrato, α-KG e malato desidrogenases) param por falta de cofator. O ciclo congela. A dependência do O₂ é indireta mas absoluta.])

#discursiva("Q5",
  [Em um paciente com infarto agudo do miocárdio causado por oclusão coronária total, a necrose dos cardiomiócitos do território afetado começa em poucos minutos. Descreva a cascata metabólica que liga a interrupção do fluxo coronário à morte celular, integrando ciclo de Krebs, cadeia respiratória, fosforilação oxidativa e equilíbrio iônico das células cardíacas afetadas.],
  [Em segundos após a oclusão, o aporte de O₂ ao tecido cai a zero. A cadeia respiratória trava no Complexo IV por falta de aceptor final; o gradiente de prótons se dissipa e a ATP sintase para. O NADH gerado pela PDH e pelo ciclo não é reoxidado, o NAD⁺ esgota e o ciclo congela por falta de cofator. A célula tenta sobreviver com glicólise anaeróbia, mas o rendimento de 2 ATP/glicose é insuficiente para manter as bombas Na⁺/K⁺-ATPase e a SERCA. Há influxo descontrolado de Ca²⁺ no citoplasma, ativação de proteases e fosfolipases, ruptura de membranas e necrose isquêmica em minutos.])
