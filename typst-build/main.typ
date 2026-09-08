// ================================================================
// MAIN.TYP -- biomol-05-operon-procariotos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Regulação gênica em bactérias",
  "Biologia Molecular",
  (
    ("Disciplina", "Biologia Molecular"),
    ("Onde estudar", "Lehninger Cap. 28 + Alberts (Biologia Molecular da Célula) Cap. 7"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A gramática da regulação bacteriana", (
      "1.1 Onde o controle acontece",
      "1.2 As quatro combinações lógicas",
      "1.3 Operon, cis e trans",
    )),
    ("PARTE II — O operon lac e a lógica que o revelou", (
      "2.1 Os cinco elementos do operon",
      "2.2 LacI, sensor alostérico",
      "2.3 Mutantes e diploide parcial",
    )),
    ("PARTE III — Promotor, ativador e integração", (
      "3.1 Anatomia e força do promotor",
      "3.2 CAP-cAMP compensa o promotor",
      "3.3 Glicose versus lactose",
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
    ("01", "D"),
    ("02", "A"),
    ("03", "CCEE"),
    ("04", "D"),
    ("05", "C"),
    ("06", "A"),
    ("07", "CCEE"),
    ("08", "D"),
    ("09", "E"),
    ("10", "CECC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "C"),
    ("13", "ECCE"),
    ("14", "D"),
    ("15", "E"),
    ("16", "ECCE"),
    ("17", "C"),
    ("18", "A"),
    ("19", "CEEC"),
    ("20", "C"),
    ("21", "E"),
    ("22", "CECC"),
    ("23", "D"),
    ("24", "C"),
    ("25", "EECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "A"),
    ("28", "CEEC"),
    ("29", "B"),
    ("30", "CCEC"),
  )),
))
