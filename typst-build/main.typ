// ================================================================
// MAIN.TYP -- biomol-06-integracao-metabolica-ii | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Integração metabólica II",
  "Bioquímica",
  (
    ("Disciplina", "Bioquímica — estados alimentares"),
    ("Onde estudar", "Marzzoco & Torres — Bioquímica Básica (integração do metabolismo) · Stryer — Bioquímica (integração metabólica e diabetes) · Lehninger — Princípios de Bioquímica (regulação hormonal do metabolismo de combustíveis)"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O estado alimentado", (
      "1.1 A razão insulina/glucagon",
      "1.2 Glicoquinase e retenção hepática",
      "1.4 Citrato, malonil-CoA e gordura",
    )),
    ("PARTE II — O período pós-absortivo", (
      "2.1 Glucagon, cAMP e trava dupla",
      "2.2 Frutose-2,6-bifosfato decide",
      "2.4 Gordura autoriza a gliconeogênese",
    )),
    ("PARTE III — Jejum e sinalização quebrada", (
      "3.1 Alanina, glutamina e Cori",
      "3.2 Corpos cetônicos poupam proteína",
      "3.3 Diabetes: o jejum permanente",
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
  ("Consolidação (Q01–Q08)", (
    ("01", "C"),
    ("02", "E"),
    ("03", "ECCE"),
    ("04", "B"),
    ("05", "D"),
    ("06", "CCEC"),
    ("07", "A"),
    ("08", "D"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "E"),
    ("10", "CECC"),
    ("11", "B"),
    ("12", "A"),
    ("13", "CEEC"),
    ("14", "C"),
    ("15", "D"),
    ("16", "CCEE"),
    ("17", "A"),
    ("18", "E"),
    ("19", "ECCC"),
    ("20", "C"),
    ("21", "A"),
    ("22", "CCEE"),
    ("23", "E"),
    ("24", "B"),
    ("25", "CEEC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "CEEE"),
    ("28", "A"),
    ("29", "C"),
    ("30", "ECCE"),
  )),
))
