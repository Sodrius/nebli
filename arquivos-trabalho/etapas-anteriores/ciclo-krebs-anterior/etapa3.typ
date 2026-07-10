#import "../typst-template/nebli_v2_apostila.typ": *

#discursiva("Q1",
  [Descreva, mecanisticamente, como o sinal mitogênico extracelular ativa a transição G1/S, passando obrigatoriamente pela proteína Rb e por seu fator de transcrição associado.],
  [Mitógenos ligam-se a receptores de superfície e ativam a cascata Ras-MAPK, que culmina na transcrição da ciclina D. Ciclina D se associa a CDK4/6 e fosforila parcialmente Rb. Rb hipofosforilada estava sequestrando E2F; com a fosforilação, E2F é liberada e transcreve a ciclina E. CDK2+ciclina E fosforila ainda mais Rb, liberando mais E2F — feedback positivo. A transição G1/S vira abrupta e irreversível. Sem mitógeno, ciclina D cai, Rb fica não-fosforilada, E2F sequestrada, célula em G0.])

#discursiva("Q2",
  [Explique por que o gatilho da anáfase é molecular (e não mecânico), descrevendo a sequência APC/C → securina → separase → coesina e justificando a irreversibilidade do processo.],
  [Na metáfase, os microtúbulos já aplicam tensão sobre as cromátides — quem segura são as coesinas em torno do par. Quando o SAC libera APC/C (cinetócoros com tensão bipolar), APC/C ubiquitina securina e ciclina B. Securina destruída libera separase, que cliva a subunidade Scc1 da coesina. A tensão preexistente dos microtúbulos então separa as cromátides — gatilho químico, força mecânica antecipada. Ciclina B destruída desliga M-CDK, encerra mitose. Irreversibilidade: degradação proteolítica não tem volta sem nova síntese.])

#discursiva("Q3",
  [Descreva o mecanismo molecular pelo qual o Pre-RC (complexo pré-replicativo) garante que cada origem de replicação dispare uma única vez por ciclo, e explique por que esse controle é essencial.],
  [Pre-RC carrega nas origens apenas quando as CDKs estão baixas — situação que só ocorre em G1 (ciclinas degradadas pelo APC/C ao final da mitose anterior). Quando CDK2+ciclina E sobe em G1/S, o Pre-RC é fosforilado e dissocia; novos Pre-RC não conseguem carregar enquanto as CDKs estiverem altas (S/G2/M). Cada origem dispara uma vez por ciclo. Re-replicação seria mutagênica: amplificação gênica, instabilidade cromossômica. Apenas na próxima G1 (após APC/C zerar ciclinas) as origens podem ser licenciadas novamente.])

#discursiva("Q4",
  [Explique, em termos de mecanismo molecular, por que a doxorrubicina é frequentemente ineficaz em tumores com p53 mutada, e por que o venetoclax pode resgatar esses pacientes.],
  [Doxorrubicina intercala o DNA e inibe topoisomerase II, gerando quebras de dupla fita. Em célula p53-funcional, ATM detecta o dano, estabiliza p53, que transcreve genes pró-apoptóticos (Bax) — apoptose. Sem p53 funcional, o dano se acumula sem disparar apoptose: resistência. Venetoclax age abaixo de p53 na via mitocondrial: inibe BCL-2 (anti-apoptótica, superexpressa em LLC), libera Bax/Bak, que permeabilizam a mitocôndria, liberam citocromo c, ativam caspase 9 → caspase 3. Apoptose independente de p53. Eficaz mesmo em tumores p53-mutados.])

#discursiva("Q5",
  [Descreva o mecanismo molecular completo pelo qual o HPV oncogênico (tipos 16 e 18) causa câncer cervical, articulando as funções de E6 e E7 com as vias supressoras tumorais Rb-E2F e p53. Explique também por que a vacinação previne esse tipo de câncer.],
  [HPV oncogênico expressa duas proteínas virais que sequestram supressores tumorais celulares. E7 liga-se a Rb e recruta o proteassoma para degradá-la — Rb destruída libera E2F constitutivamente, que transcreve continuamente ciclina E, ciclina A e a maquinaria da fase S. A célula entra em ciclo sem precisar de mitógenos. E6 liga-se a p53 e recruta E6AP, uma ligase E3 que ubiquitina p53 — p53 degradada, sem parada do ciclo e sem apoptose mesmo com dano genético. As duas juntas geram célula que prolifera sem parar e não morre quando deveria. Mutações se acumulam, virando câncer cervical (ou de orofaringe). A vacina contém VLPs (virus-like particles) da capsídeo de L1 do HPV — induz anticorpos neutralizantes que impedem a infecção inicial. Sem infecção, não há expressão de E6/E7, e o câncer associado a HPV não se desenvolve.])
