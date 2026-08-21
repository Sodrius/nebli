// ================================================================
// MAIN.TYP -- imuno-01-organizacao-sistema-imune | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Organização do sistema imune",
  "Imunologia",
  (
    ("Disciplina", "Imunologia — organização e funcionamento do sistema imune"),
    ("Onde estudar", "Abbas, Imunologia Celular e Molecular — cap. 1 (propriedades gerais) e cap. 2 (órgãos e células linfoides) + Janeway, Immunobiology cap. 1 e 9"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Por que existe um sistema imune", (
      "1.1 Homeostasia e o exterior",
      "1.2 Repertório clonal de receptores",
      "1.3 Barreiras, alarme e resposta inata",
    )),
    ("PARTE II — Onde as células nascem e por onde andam", (
      "2.1 Órgãos linfoides primários",
      "2.2 Da geração ao encontro",
      "2.3 Recirculação e endereçamento",
    )),
    ("PARTE III — O órgão linfoide secundário", (
      "3.1 Condições estruturais do encontro",
      "3.2 Aferência e expansão regionalizada",
      "3.3 Eferência, resposta e tolerância",
    )),
  )),
  ("Etapa 2 — 30 objetivas", (
    (none, (
      "10 de consolidação · 15 de integração · 5 de aplicação",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Mecanismo em prosa, com modelo de resposta",
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
    ("02", "CCEC"),
    ("03", "E"),
    ("04", "B"),
    ("05", "ECCE"),
    ("06", "D"),
    ("07", "A"),
    ("08", "CEEC"),
    ("09", "E"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "EECC"),
    ("13", "A"),
    ("14", "C"),
    ("15", "CCEE"),
    ("16", "B"),
    ("17", "E"),
    ("18", "ECCC"),
    ("19", "A"),
    ("20", "C"),
    ("21", "CEEE"),
    ("22", "E"),
    ("23", "D"),
    ("24", "EECE"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "CCCE"),
    ("28", "C"),
    ("29", "A"),
    ("30", "ECEE"),
  )),
))
