// ================================================================
// MAIN.TYP -- regulacao-massa-corporea | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Regulação da massa corpórea",
  "Bioquímica",
  (
    ("Disciplina", "Bioquímica — regulação hormonal e integração do metabolismo"),
    ("Onde estudar", "Lehninger, Princípios de Bioquímica (7ª ed.), cap. 23 — Regulação hormonal e integração do metabolismo · Stryer/Berg/Tymoczko, Bioquímica (7ª ed.)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O balanço energético e a orquestra que o comanda", (
      "1.1 A conta da energia diária",
      "1.3 Cascata, amplificação e retroalimentação",
      "1.5 Adiposo como glândula endócrina",
    )),
    ("PARTE II — Adipocinas: leptina, adiponectina e o freio que falha", (
      "2.1 Leptina e o gene ob",
      "2.3 Braço periférico: lipólise e termogênese",
      "2.5 Adiponectina e a AMPK",
    )),
    ("PARTE III — O comando hipotalâmico e a doença metabólica", (
      "3.1 Núcleo arqueado: fome contra saciedade",
      "3.3 Sinais de curto prazo do tubo digestivo",
      "3.5 Do circuito ao remédio",
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
    ("01", "A"),
    ("02", "E"),
    ("03", "CCEE"),
    ("04", "D"),
    ("05", "C"),
    ("06", "B"),
    ("07", "EECC"),
    ("08", "A"),
    ("09", "B"),
    ("10", "CEEC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "ECCC"),
    ("13", "C"),
    ("14", "C"),
    ("15", "D"),
    ("16", "EEEC"),
    ("17", "B"),
    ("18", "D"),
    ("19", "ECCE"),
    ("20", "C"),
    ("21", "D"),
    ("22", "CCEC"),
    ("23", "B"),
    ("24", "E"),
    ("25", "CECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "CEEE"),
    ("28", "C"),
    ("29", "E"),
    ("30", "CCCE"),
  )),
))
