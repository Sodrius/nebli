// ================================================================
// MAIN.TYP -- patologia-01-lesao-morte-celular | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Lesão e morte celular",
  "Patologia",
  (
    ("Disciplina", "Patologia"),
    ("Onde estudar", "Robbins & Cotran — Patologia: Bases Patológicas das Doenças (9ª ed.) cap. 1–2 + Robbins Patologia Básica (10ª ed.) cap. 2"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Da agressão à linha de não-retorno", (
      "1.1 Homeostase, adaptação e lesão",
      "1.2 As causas da agressão celular",
      "1.3 Lesão reversível: edema e esteatose",
      "1.4 A linha de irreversibilidade",
    )),
    ("PARTE II — Os mecanismos que convergem", (
      "2.1 Depleção de ATP e falência das bombas",
      "2.2 Dano mitocondrial e o desfecho",
      "2.3 Influxo de cálcio como gatilho enzimático",
      "2.4 Radicais livres: geração e defesa",
      "2.5 Membrana, proteínas mal dobradas e DNA",
    )),
    ("PARTE III — Necrose e apoptose", (
      "3.1 Duas mortes, dois mecanismos",
      "3.2 Necrose: digestão enzimática e inflamação",
      "3.3 Os padrões morfológicos de necrose",
      "3.4 Apoptose: causas e morfologia",
      "3.5 As duas vias e a família Bcl-2",
      "3.6 Necroptose e correlações clínicas",
    )),
  )),
  ("Resumindo", (
    (none, (
    )),
  )),
  ("Etapa 2 — 30 questões objetivas", (
    (none, (
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
    )),
  )),
  ("Gabarito da Etapa 2", (
    (none, (
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
    ("02", "C"),
    ("03", "EECC"),
    ("04", "C"),
    ("05", "E"),
    ("06", "EEEC"),
    ("07", "E"),
    ("08", "B"),
    ("09", "ECEE"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "EECC"),
    ("13", "A"),
    ("14", "B"),
    ("15", "EECC"),
    ("16", "C"),
    ("17", "D"),
    ("18", "CCCE"),
    ("19", "A"),
    ("20", "E"),
    ("21", "CEEE"),
    ("22", "D"),
    ("23", "C"),
    ("24", "CECC"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "D"),
    ("28", "EEEC"),
    ("29", "D"),
    ("30", "ECCE"),
  )),
))
