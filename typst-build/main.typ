// ================================================================
// MAIN.TYP -- bioq-mecanismo-acao-hormonal | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Controle Hormonal",
  "",
  (
    ("Disciplina", "Bioquímica"),
    ("Onde estudar", "Slides da Profa. Déborah (IQ-USP) · Lehninger cap. 23 (regulação hormonal e integração do metabolismo dos mamíferos) · Berg/Stryer cap. 14 (transdução de sinal) e cap. 21 (metabolismo do glicogênio) · Devlin cap. 21"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Como um sinal químico vira ordem metabólica", (
      "1.1 As três alavancas da regulação",
      "1.2 O que define um hormônio",
      "1.3 A cadeia regulável e as classes químicas",
      "1.4 Receptor de superfície e receptor nuclear",
    )),
    ("PARTE II — Insulina e glucagon: guardar ou gastar", (
      "2.1 A insulina nasce cortada",
      "2.2 Como a célula beta mede a glicemia",
      "2.3 O que a insulina faz no fígado e no músculo",
      "2.4 O glucagon e a cascata do AMPc",
    )),
    ("PARTE III — Adrenalina, tireoidianos e esteroides", (
      "3.1 Catecolaminas: o metabolismo em alerta",
      "3.2 Tireoidianos: pró-hormônio e ativação no tecido",
      "3.3 Cortisol: do colesterol ao gene",
      "3.4 Quando o receptor é enganado",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"

// ======= ETAPA 2 =======
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "C"),
    ("02", "ECCC"),
    ("03", "E"),
    ("04", "B"),
    ("05", "ECCE"),
    ("06", "D"),
    ("07", "A"),
    ("08", "CCEE"),
    ("09", "C"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "ECEC"),
    ("13", "D"),
    ("14", "A"),
    ("15", "CEEC"),
    ("16", "E"),
    ("17", "C"),
    ("18", "ECCE"),
    ("19", "B"),
    ("20", "D"),
    ("21", "CCEC"),
    ("22", "A"),
    ("23", "E"),
    ("24", "EECC"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "C"),
    ("28", "ECEC"),
    ("29", "A"),
    ("30", "E"),
  )),
))
