// ================================================================
// MAIN.TYP -- micro-06-genetica-bacteriana | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Genética bacteriana",
  "Microbiologia · UC03",
  (
    ("Disciplina", "Microbiologia (UC03)"),
    ("Onde estudar", "Trabulsi & Alterthum, Microbiologia — genética bacteriana e elementos genéticos móveis · Murray, Microbiologia Médica — genética bacteriana · Brock, Biology of Microorganisms — replicação, mutação e transferência horizontal"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Forma, conteúdo e cópia", (
      "1.1 Nucleóide e supertorção",
      "1.2 Cromossomo, plasmídeo e transposon",
      "1.3 Replicação e polimerases",
    )),
    ("PARTE II — Como o genoma muda", (
      "2.1 Mutação e fenótipo",
      "2.2 Mutagênicos e reparo",
      "2.3 Transformação e transdução",
    )),
    ("PARTE III — Trocar, regular, defender", (
      "3.1 Conjugação e resistência",
      "3.2 Operon lac",
      "3.3 e 3.4 Defesa antifágica e DNA recombinante",
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
    ("02", "CCEE"),
    ("03", "B"),
    ("04", "E"),
    ("05", "ECCE"),
    ("06", "A"),
    ("07", "C"),
    ("08", "EECC"),
    ("09", "E"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "D"),
    ("13", "ECCE"),
    ("14", "B"),
    ("15", "E"),
    ("16", "CCEE"),
    ("17", "A"),
    ("18", "C"),
    ("19", "CEEC"),
    ("20", "D"),
    ("21", "A"),
    ("22", "EECC"),
    ("23", "E"),
    ("24", "B"),
    ("25", "CCCE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "D"),
    ("28", "CCEC"),
    ("29", "A"),
    ("30", "CECC"),
  )),
))
