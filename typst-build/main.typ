// ================================================================
// MAIN.TYP -- pat-08-inflamacao-granulomatosa | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Inflamação granulomatosa",
  "Do agente que não se destrói à arquitetura que o isola",
  (
    ("Disciplina", "Patologia"),
    ("Onde estudar", "Robbins & Cotran, Patologia — Inflamação e reparo, § Inflamação crônica e inflamação granulomatosa · Abbas, Imunologia Celular e Molecular — Imunidade mediada por células T e resposta a microrganismos intracelulares"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O agente que não se destrói", (
      "1.1 Granuloma como arquitetura",
      "1.2 O bacilo dentro do macrófago",
      "1.3 Da inata ao linfonodo",
    )),
    ("PARTE II — A montagem do granuloma", (
      "2.1 Eixo IL-12, TH1 e interferon-gama",
      "2.2 De onde vêm os macrófagos",
      "2.3 A arquitetura pronta",
    )),
    ("PARTE III — Na lâmina e no paciente", (
      "3.1 Caseoso, duro, antigo",
      "3.2 Primária, secundária, miliar",
      "3.3 Granuloma sem bacilo",
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
    ("02", "CECC"),
    ("03", "B"),
    ("04", "D"),
    ("05", "CCEC"),
    ("06", "E"),
    ("07", "A"),
    ("08", "D"),
    ("09", "ECCC"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "E"),
    ("12", "CCCE"),
    ("13", "B"),
    ("14", "D"),
    ("15", "CCEE"),
    ("16", "C"),
    ("17", "D"),
    ("18", "A"),
    ("19", "ECCE"),
    ("20", "B"),
    ("21", "A"),
    ("22", "CEEC"),
    ("23", "C"),
    ("24", "B"),
    ("25", "EECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "C"),
    ("28", "EECE"),
    ("29", "E"),
    ("30", "CEEE"),
  )),
))
