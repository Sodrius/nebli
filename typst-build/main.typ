// ================================================================
// MAIN.TYP -- motilidade-tgi | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Motilidade do trato gastrointestinal",
  "Do sinal nervoso à contração do músculo liso",
  (
    ("Disciplina", "Fisiologia do sistema digestório"),
    ("Onde estudar", "Berne & Levy, Fisiologia — capítulo de motilidade do trato gastrointestinal · Guyton & Hall, Tratado de Fisiologia Médica — princípios gerais da função gastrointestinal · Boron & Boulpaep, Fisiologia Médica — músculo liso e sistema nervoso entérico"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O músculo e a rede", (
      "1.1 Sincício e marcapasso",
      "1.2 Contração fásica e tônica",
      "1.3 Os dois plexos entéricos",
    )),
    ("PARTE II — Reflexos e esfíncteres", (
      "2.1 Reflexo curto intramural",
      "2.2 Reflexo longo vago-vagal",
      "2.3 Esfíncteres e distensão",
    )),
    ("PARTE III — Da membrana à força", (
      "3.1 Junção neuroefetora",
      "3.2 Cálcio, calmodulina e MLCK",
      "3.3 Sensibilização ao cálcio",
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
    ("01", "B"),
    ("02", "CCEC"),
    ("03", "B"),
    ("04", "D"),
    ("05", "B"),
    ("06", "CEEC"),
    ("07", "E"),
    ("08", "B"),
    ("09", "CECC"),
    ("10", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "E"),
    ("13", "CCEE"),
    ("14", "A"),
    ("15", "B"),
    ("16", "CCCE"),
    ("17", "B"),
    ("18", "C"),
    ("19", "ECEE"),
    ("20", "E"),
    ("21", "C"),
    ("22", "E"),
    ("23", "ECCE"),
    ("24", "C"),
    ("25", "ECEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "B"),
    ("28", "CCEE"),
    ("29", "C"),
    ("30", "CEEC"),
  )),
))
