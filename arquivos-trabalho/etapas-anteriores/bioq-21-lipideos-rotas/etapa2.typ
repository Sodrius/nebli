#import "../typst-template/nebli_v2_apostila.typ": *

// ===================== CONSOLIDAÇÃO (Q01–Q08) =====================

#questao-mc("01", badge-consolidacao,
  [Por que o corpo guarda sua reserva de energia de longo prazo como gordura, e não como carboidrato?],
  (("A", [O glicogênio rende mais energia por grama, mas a gordura é preferida por ser mobilizada mais rápido durante o exercício intenso.]),
   ("B", [A gordura rende mais energia por grama e é guardada praticamente sem água, enquanto cada grama de glicogênio carrega cerca de três gramas de água.]),
   ("C", [A gordura e o carboidrato rendem a mesma energia por grama, e a escolha se deve apenas ao menor volume ocupado pelos adipócitos.]),
   ("D", [A gordura é estocada hidratada como o glicogênio, mas ocupa menos espaço por ser uma molécula apolar de cadeia longa ramificada.]),
   ("E", [O carboidrato é apolar e anidro, por isso serve de reserva de longo prazo, deixando a gordura para o gasto imediato de energia.])))

#questao-ce("02", badge-consolidacao,
  [Julgue os itens sobre a mobilização e a ativação dos ácidos graxos:],
  (("I", [A lipase hormônio-sensível é ativada por fosforilação após o estímulo de glucagon e adrenalina, via AMPc e PKA.]),
   ("II", [O glicerol liberado na lipólise é exportado ao fígado, porque o adipócito tem pouca glicerol-quinase para reaproveitá-lo.]),
   ("III", [A ativação do ácido graxo consome um ATP que é convertido apenas a ADP e fosfato inorgânico.]),
   ("IV", [Os ácidos graxos de cadeia longa atravessam a membrana mitocondrial interna por difusão simples.])))

#questao-mc("03", badge-consolidacao,
  [Qual é a sequência correta das quatro reações de cada volta da β-oxidação?],
  (("A", [Hidratação, depois desidrogenação, depois tiólise e por fim oxidação, liberando dois acetil-CoA a cada volta do ciclo.]),
   ("B", [Oxidação, depois tiólise, depois desidrogenação e por fim hidratação, com produção de NADPH em cada uma das etapas.]),
   ("C", [Tiólise, depois oxidação, depois hidratação e por fim desidrogenação, removendo quatro carbonos a cada volta completa.]),
   ("D", [Desidrogenação, depois hidratação, depois oxidação e por fim tiólise, liberando um acetil-CoA a cada volta do ciclo.]),
   ("E", [Condensação, depois redução, depois desidratação e nova redução, exatamente como ocorre na síntese de ácidos graxos.])))

#questao-mc("04", badge-consolidacao,
  [Sobre o estoque e a mobilização da gordura, assinale a afirmativa *incorreta*:],
  (("A", [O glicerol liberado na lipólise é oxidado no próprio adipócito como sua principal fonte de ATP durante o jejum.]),
   ("B", [A lipase hormônio-sensível é ativada por glucagon e adrenalina através da via do AMPc e da PKA.]),
   ("C", [O triacilglicerol é a forma de estoque por ser anidro, ocupando menos peso que o glicogênio hidratado.]),
   ("D", [Os ácidos graxos viajam no sangue ligados à albumina até os tecidos que vão oxidá-los.]),
   ("E", [A mobilização do estoque é hormonalmente controlada, não um vazamento contínuo de ácidos graxos.])))

#questao-ce("05", badge-consolidacao,
  [Julgue os itens sobre a β-oxidação propriamente dita:],
  (("I", [A β-oxidação ocorre no citosol, em paralelo às reações da glicólise.]),
   ("II", [Cada volta remove dois carbonos e gera um FADH₂, um NADH e um acetil-CoA.]),
   ("III", [A via depende de oxigênio, pois FADH₂ e NADH precisam ser reoxidados na cadeia respiratória.]),
   ("IV", [A primeira reação de cada volta é a tiólise, que já solta o acetil-CoA.])))

#questao-mc("06", badge-consolidacao,
  [Um ácido graxo saturado de 18 carbonos sofre β-oxidação completa. Quantas voltas do ciclo e quantos acetil-CoA são produzidos?],
  (("A", [Dez voltas e nove acetil-CoA, porque cada volta libera um acetil-CoA e o ciclo recomeça dez vezes.]),
   ("B", [Nove voltas e nove acetil-CoA, já que o número de voltas é sempre igual ao número de acetil-CoA formados.]),
   ("C", [Oito voltas e nove acetil-CoA, pois são (18/2 − 1) voltas e a última libera dois acetil-CoA de uma vez.]),
   ("D", [Oito voltas e oito acetil-CoA, porque cada uma das oito voltas libera exatamente um acetil-CoA.]),
   ("E", [Nove voltas e oito acetil-CoA, descontando uma volta inicial que não chega a liberar acetil-CoA.])))

#questao-ce("07", badge-consolidacao,
  [Julgue os itens sobre o transporte pela carnitina e os tecidos que oxidam ácidos graxos:],
  (("I", [A CPT-1, na face externa, transfere o grupo acila da coenzima A para a carnitina.]),
   ("II", [A hemácia oxida ácidos graxos avidamente para poupar a glicose do plasma.]),
   ("III", [O malonil-CoA ativa a CPT-1, acelerando a entrada de ácidos graxos na mitocôndria.]),
   ("IV", [O tecido nervoso depende pouco da β-oxidação porque os ácidos graxos atravessam mal a barreira hematoencefálica.])))

#questao-mc("08", badge-consolidacao,
  [Sobre os corpos cetônicos, é correto afirmar:],
  (("A", [São produtos de excreção sem valor energético, eliminados na urina para livrar o corpo do excesso de gordura.]),
   ("B", [São sintetizados no cérebro a partir da glicose e exportados ao fígado nos períodos de jejum prolongado.]),
   ("C", [São lipídios insolúveis que precisam da albumina para circular, como os ácidos graxos livres do plasma.]),
   ("D", [São feitos no fígado a partir do excesso de acetil-CoA e servem de combustível ao cérebro durante o jejum.]),
   ("E", [São produzidos apenas quando há excesso de carboidrato, que satura o ciclo de Krebs com acetil-CoA.])))

// ===================== INTEGRAÇÃO (Q09–Q25) =====================

#questao-mc("09", badge-integracao,
  [Por que a β-oxidação não funciona em condições anaeróbias, mesmo o oxigênio não participando de nenhuma de suas quatro reações?],
  (("A", [Porque cada volta gera FADH₂ e NADH que só se reoxidam na cadeia respiratória; sem O₂, FAD e NAD⁺ não se regeneram.]),
   ("B", [Porque a reação de tiólise consome oxigênio diretamente ao clivar a ligação entre o carbono α e o carbono β.]),
   ("C", [Porque a carnitina precisa de oxigênio para transferir o grupo acila através da membrana mitocondrial interna.]),
   ("D", [Porque o acetil-CoA produzido só é estável na presença de oxigênio, decompondo-se rapidamente sem ele.]),
   ("E", [Porque a ativação do ácido graxo a acil-CoA depende de oxigênio para a hidrólise do pirofosfato liberado.])))

#questao-mc("10", badge-integracao,
  [A ativação do ácido graxo a acil-CoA costuma ser contabilizada como gasto de dois ATP. Qual a justificativa correta?],
  (("A", [São necessárias duas moléculas de ATP para ligar a coenzima A ao grupo carboxila do ácido graxo.]),
   ("B", [O ATP é hidrolisado a ADP e fosfato inorgânico duas vezes seguidas antes de o acil-CoA se formar.]),
   ("C", [A carnitina exige um ATP na entrada e outro ATP na saída do grupo acila da mitocôndria.]),
   ("D", [Cada volta da β-oxidação devolve dois ATP que precisam ser pagos antecipadamente na etapa de ativação.]),
   ("E", [O ATP é quebrado até AMP e o pirofosfato liberado ainda é hidrolisado a dois fosfatos inorgânicos.])))

#questao-ce("11", badge-integracao,
  [Julgue os itens sobre a relação entre a β-oxidação e o ciclo de Krebs:],
  (("I", [O acetil-CoA da β-oxidação entra no ciclo de Krebs independentemente da disponibilidade de oxaloacetato.]),
   ("II", [A β-oxidação produz ATP diretamente em cada uma de suas quatro reações.]),
   ("III", [O acetil-CoA precisa se condensar com o oxaloacetato para iniciar o ciclo de Krebs.]),
   ("IV", [Quando o oxaloacetato falta, o acetil-CoA acumulado é desviado para a formação de corpos cetônicos.])))

#questao-mc("12", badge-integracao,
  [Considerando 1 NADH = 3 ATP, 1 FADH₂ = 2 ATP e 1 GTP = 1 ATP, qual é o saldo líquido da oxidação completa de um palmitato (16C)?],
  (("A", [106 ATP, somando 31 NADH, 15 FADH₂ e 8 GTP pelos valores modernos de rendimento da cadeia respiratória.]),
   ("B", [131 ATP, somando todos os transportadores produzidos sem descontar o custo da ativação do ácido graxo.]),
   ("C", [129 ATP, somando os 131 brutos e descontando os dois ATP gastos na ativação do ácido graxo.]),
   ("D", [120 ATP, considerando oito voltas da β-oxidação e oito acetil-CoA enviados ao ciclo de Krebs.]),
   ("E", [147 ATP, contando nove acetil-CoA no ciclo de Krebs e somando a ativação como ganho energético.])))

#questao-mc("13", badge-integracao,
  [Na oxidação do palmitato, os 8 acetil-CoA formados entram no ciclo de Krebs. Quantos NADH e FADH₂ o Krebs gera a partir deles?],
  (("A", [16 NADH e 8 FADH₂, contando dois NADH e um FADH₂ por acetil-CoA que entra no ciclo.]),
   ("B", [31 NADH e 15 FADH₂, que é o total da via somando também os produzidos na β-oxidação.]),
   ("C", [8 NADH e 8 FADH₂, um de cada por acetil-CoA, mais os oito GTP correspondentes às voltas.]),
   ("D", [7 NADH e 7 FADH₂, idêntico ao que as sete voltas da β-oxidação produziram anteriormente.]),
   ("E", [24 NADH e 8 FADH₂, pois cada acetil-CoA rende três NADH e um FADH₂ no ciclo de Krebs.])))

#questao-ce("14", badge-integracao,
  [Julgue os itens sobre o controle da entrada de ácidos graxos na mitocôndria:],
  (("I", [A CPT-1 é o ponto de controle da β-oxidação e é inibida pelo malonil-CoA.]),
   ("II", [O malonil-CoA é produzido durante a β-oxidação para acelerar a própria via.]),
   ("III", [Com a CPT-1 bloqueada, o ácido graxo não chega à matriz e a queima cessa.]),
   ("IV", [Esse bloqueio evita queimar e sintetizar ácido graxo ao mesmo tempo, um ciclo fútil.])))

#questao-mc("15", badge-integracao,
  [No jejum prolongado, por que o acetil-CoA da β-oxidação é desviado para corpos cetônicos em vez de entrar no ciclo de Krebs?],
  (("A", [Porque o jejum inibe diretamente todas as enzimas do ciclo de Krebs, impedindo a entrada de acetil-CoA.]),
   ("B", [Porque o oxaloacetato é consumido pela gliconeogênese e falta para se condensar com o acetil-CoA no Krebs.]),
   ("C", [Porque a β-oxidação produz tanto FADH₂ que satura a cadeia respiratória e paralisa o ciclo de Krebs.]),
   ("D", [Porque o cérebro envia um sinal hormonal que redireciona o acetil-CoA hepático para os corpos cetônicos.]),
   ("E", [Porque o acetil-CoA do jejum vem dos aminoácidos, e apenas esse tipo pode formar corpos cetônicos.])))

#questao-mc("16", badge-integracao,
  [Sobre o papel dos corpos cetônicos no jejum, assinale a afirmativa *incorreta*:],
  (("A", [O fígado produz e também consome os corpos cetônicos, usando-os como seu principal combustível durante o jejum.]),
   ("B", [Os corpos cetônicos são hidrossolúveis e circulam livremente no sangue sem precisar se ligar à albumina.]),
   ("C", [No jejum prolongado, o cérebro passa a usar corpos cetônicos como combustível, poupando a glicose disponível.]),
   ("D", [A formação de corpos cetônicos depende do excesso de acetil-CoA produzido pela β-oxidação dos ácidos graxos.]),
   ("E", [O acetoacetato e o β-hidroxibutirato derivam da condensação de unidades de acetil-CoA no fígado.])))

#questao-ce("17", badge-integracao,
  [Julgue os itens comparando a síntese e a β-oxidação de ácidos graxos:],
  (("I", [Ambas ocorrem na matriz mitocondrial e usam a coenzima A como carreador da cadeia.]),
   ("II", [A síntese usa NADPH como doador de elétrons; a β-oxidação usa FAD e NAD⁺ como receptores.]),
   ("III", [A síntese é exatamente a β-oxidação revertida, com as mesmas enzimas e coenzimas.]),
   ("IV", [A síntese adiciona dois carbonos por ciclo, doados pelo malonil-CoA.])))

#questao-mc("18", badge-integracao,
  [Como o acetil-CoA, produzido na mitocôndria, chega ao citosol para servir de matéria-prima à síntese de ácidos graxos?],
  (("A", [Atravessa a membrana mitocondrial diretamente por um transportador específico de acetil-CoA na membrana interna.]),
   ("B", [É convertido em corpos cetônicos, que saem para o citosol e são reconvertidos a acetil-CoA pela tioforase.]),
   ("C", [É carregado pela carnitina, a mesma lançadeira que leva os ácidos graxos para dentro da mitocôndria.]),
   ("D", [Sai da mitocôndria como citrato e é reclivado no citosol pela citrato-liase em acetil-CoA e oxaloacetato.]),
   ("E", [Difunde-se livremente porque o acetil-CoA é uma molécula pequena e apolar que cruza membranas facilmente.])))

#questao-mc("19", badge-integracao,
  [Qual evento caracteriza o passo comprometido da síntese de ácidos graxos e como a insulina o afeta?],
  (("A", [A condensação do malonil-CoA pela sintase de ácidos graxos, que a insulina inibe em estado de fartura.]),
   ("B", [A clivagem do citrato pela citrato-liase no citosol, que a insulina desliga para conservar acetil-CoA.]),
   ("C", [A carboxilação do acetil-CoA a malonil-CoA pela acetil-CoA carboxilase, que a insulina ativa na fartura.]),
   ("D", [A redução do acetoacetil-ACP pelo NADPH, que a insulina acelera fornecendo mais poder redutor à célula.]),
   ("E", [A entrada do acil-CoA na mitocôndria pela CPT-1, que a insulina estimula para iniciar a síntese.])))

#questao-mc("20", badge-integracao,
  [Além de doar carbonos à síntese, qual é o papel regulatório do malonil-CoA?],
  (("A", [Ativa a sintase de ácidos graxos, acelerando a montagem do palmitato durante a fartura energética.]),
   ("B", [Estimula a lipase hormônio-sensível no adipócito, liberando mais ácidos graxos para a síntese hepática.]),
   ("C", [Inibe a citrato-liase, reduzindo a saída de acetil-CoA da mitocôndria quando há excesso de citrato.]),
   ("D", [Ativa a CPT-1, acelerando a entrada de ácidos graxos na mitocôndria para serem queimados rapidamente.]),
   ("E", [Inibe a CPT-1, bloqueando a β-oxidação e evitando queimar e sintetizar ácido graxo ao mesmo tempo.])))

#questao-ce("21", badge-integracao,
  [Julgue os itens sobre a relação entre os ácidos graxos e a síntese de glicose:],
  (("I", [O ácido graxo de cadeia par não gera síntese líquida de glicose em mamíferos.]),
   ("II", [O glicerol liberado na lipólise pode ser convertido em glicose no fígado.]),
   ("III", [O acetil-CoA da β-oxidação gera oxaloacetato líquido que alimenta a gliconeogênese.]),
   ("IV", [O propionil-CoA dos ácidos graxos de cadeia ímpar pode contribuir para a gliconeogênese.])))

#questao-mc("22", badge-integracao,
  [No jejum, qual é a contribuição do glicerol liberado pela lipólise para a manutenção da glicemia?],
  (("A", [Vai ao fígado e entra na gliconeogênese via gliceraldeído-3-fosfato, contribuindo para a produção de glicose nova.]),
   ("B", [É oxidado no adipócito a piruvato, fornecendo o ATP necessário para a própria lipólise continuar.]),
   ("C", [Converte-se em acetil-CoA no fígado e alimenta o ciclo de Krebs, poupando a glicose circulante.]),
   ("D", [Liga-se à albumina e é levado aos músculos, onde é queimado junto com os ácidos graxos livres.]),
   ("E", [Permanece no adipócito como esqueleto para reesterificar novos ácidos graxos quando o jejum terminar.])))

#questao-mc("23", badge-integracao,
  [Sobre a sintase de ácidos graxos e a montagem do palmitato, assinale a afirmativa *incorreta*:],
  (("A", [A FAS reúne todas as enzimas da via numa estrutura única, com o braço ACP carregando a cadeia em crescimento.]),
   ("B", [O malonil-CoA doa dois carbonos por ciclo e perde um carbono como CO₂ na reação de condensação.]),
   ("C", [A sequência é condensação, redução, desidratação e nova redução, usando NADPH nas duas reduções.]),
   ("D", [A síntese pela FAS termina no palmitato de 16 carbonos; alongar além disso exige enzimas adicionais.]),
   ("E", [A FAS usa FADH₂ e NADH como doadores de elétrons, exatamente como ocorre na β-oxidação dos ácidos graxos.])))

#questao-ce("24", badge-integracao,
  [Julgue os itens sobre o poder redutor exigido pela síntese de ácidos graxos:],
  (("I", [A síntese de ácidos graxos usa NADH como doador de elétrons em suas reduções.]),
   ("II", [A enzima málica consome NADPH para reduzir o piruvato a malato no citosol.]),
   ("III", [A enzima málica e a glicose-6-P-desidrogenase geram o NADPH usado pela síntese.]),
   ("IV", [O NADPH e o NADH são intercambiáveis nas reações de oxirredução da célula.])))

#questao-mc("25", badge-integracao,
  [Por que apenas os ácidos graxos de cadeia ímpar podem contribuir, em parte, para a síntese de glicose?],
  (("A", [Porque sua cadeia ímpar gera mais acetil-CoA, e o excesso de acetil-CoA é convertido em oxaloacetato.]),
   ("B", [Porque a cadeia ímpar é oxidada no citosol, onde o acetil-CoA tem acesso direto à gliconeogênese.]),
   ("C", [Porque a cadeia ímpar dispensa a carnitina e libera intermediários de três carbonos no citosol hepático.]),
   ("D", [Porque a última volta gera propionil-CoA, que entra na gliconeogênese, ao contrário do acetil-CoA.]),
   ("E", [Porque a cadeia ímpar produz glicerol na última volta, e o glicerol é um substrato gliconeogênico.])))

// ===================== APLICAÇÃO (Q26–Q30) =====================

#questao-mc("26", badge-aplicacao,
  [Uma paciente perdeu 45 kg de gordura ao longo de meses, com dieta restrita e exercício regular. O que aconteceu metabolicamente?],
  (("A", [A gordura foi convertida diretamente em glicose, que foi excretada na urina junto com a água perdida.]),
   ("B", [O déficit calórico ativou a síntese de ácidos graxos, consumindo o estoque para produzir mais triacilglicerol.]),
   ("C", [O déficit calórico ativou a lipólise e a β-oxidação, queimando o triacilglicerol estocado no tecido adiposo.]),
   ("D", [O exercício transformou a gordura em músculo por meio da síntese de proteínas a partir do acetil-CoA.]),
   ("E", [A restrição inibiu a lipólise, e o emagrecimento veio apenas da perda de água e de glicogênio muscular.])))

#questao-ce("27", badge-aplicacao,
  [Um homem está em jejum há 48 horas. Julgue os itens sobre o seu metabolismo de lipídeos:],
  (("I", [A lipólise está aumentada, liberando ácidos graxos para os tecidos periféricos.]),
   ("II", [O cérebro passou a oxidar ácidos graxos diretamente como seu combustível principal.]),
   ("III", [A síntese de ácidos graxos está ativada para estocar o excesso energético da reserva.]),
   ("IV", [O fígado produz corpos cetônicos que o cérebro passa a usar como combustível.])))

#questao-mc("28", badge-aplicacao,
  [Um corredor de maratona, após duas horas de prova, depende fortemente da oxidação de gordura. O que sustenta esse processo?],
  (("A", [A insulina alta do exercício prolongado ativa a CPT-1 e acelera a entrada de ácidos graxos na mitocôndria.]),
   ("B", [O malonil-CoA acumulado abre a CPT-1 e permite a entrada maciça de ácidos graxos para a queima.]),
   ("C", [A β-oxidação roda em anaerobiose nos músculos, dispensando oxigênio durante o esforço de longa duração.]),
   ("D", [O glicogênio muscular é convertido em ácidos graxos, que são então oxidados para sustentar a corrida.]),
   ("E", [A adrenalina ativa a lipólise e reduz o malonil-CoA, liberando a CPT-1 para a queima de ácidos graxos.])))

#questao-mc("29", badge-aplicacao,
  [Uma criança com deficiência genética da CPT-1 apresenta hipoglicemia e fraqueza após o jejum noturno. Qual a explicação mecanística?],
  (("A", [Sem CPT-1, os ácidos graxos de cadeia longa não entram na mitocôndria, e os tecidos não conseguem queimá-los no jejum.]),
   ("B", [Sem CPT-1, o excesso de malonil-CoA acelera a síntese de gordura, consumindo toda a glicose disponível.]),
   ("C", [Sem CPT-1, os corpos cetônicos são produzidos em excesso, causando cetoacidose grave nas primeiras horas.]),
   ("D", [Sem CPT-1, o glicerol não chega ao fígado, impedindo a gliconeogênese e causando a hipoglicemia observada.]),
   ("E", [Sem CPT-1, a β-oxidação acelera demais e esgota o estoque de gordura, levando à fraqueza muscular.])))

#questao-ce("30", badge-aplicacao,
  [Paciente com diabetes tipo 1 sem insulina chega com hálito adocicado e respiração rápida e profunda. Julgue os itens:],
  (("I", [A ausência de insulina bloqueia a lipólise, reduzindo a oferta de ácidos graxos aos tecidos.]),
   ("II", [A β-oxidação intensa inunda o fígado de acetil-CoA, aumentando a produção de corpos cetônicos.]),
   ("III", [O acúmulo de corpos cetônicos ácidos baixa o pH do sangue e causa a cetoacidose.]),
   ("IV", [A respiração rápida e profunda agrava a acidose ao reter mais CO₂ no sangue.])))
