// ================================================================
// MAIN.TYP -- micro-02-fisiologia-crescimento-bacteriano | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Fisiologia e crescimento bacteriano",
  "Microbiologia",
  (
    ("Disciplina", "Microbiologia"),
    ("Onde estudar", "Trabulsi & Alterthum — Microbiologia (7ª ed.) · Murray — Microbiologia Médica · Brock — Biologia dos Microrganismos (caps. 3–5) · Tortora — Microbiologia (caps. 5–6)"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O que a bactéria precisa para crescer", (
      "1.1 Nutrição e classificação trófica",
      "1.2 pH, temperatura e sal",
      "1.3 Oxigênio e ferro",
    )),
    ("PARTE II — Como a bactéria transforma nutriente em ATP", (
      "2.1 Glicólise e fermentação",
      "2.2 Respiração na membrana plasmática",
      "2.3 Metabolismo vira assinatura",
    )),
    ("PARTE III — Da célula à população", (
      "3.1 Divisão binária e curva",
      "3.2 Tempo de geração na clínica",
      "3.3 Meios de cultura e isolamento",
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
    ("02", "D"),
    ("03", "CECC"),
    ("04", "C"),
    ("05", "A"),
    ("06", "D"),
    ("07", "CCEC"),
    ("08", "E"),
    ("09", "B"),
    ("10", "CCEE"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "CEEC"),
    ("13", "EECC"),
    ("14", "E"),
    ("15", "CCCE"),
    ("16", "A"),
    ("17", "D"),
    ("18", "ECCC"),
    ("19", "B"),
    ("20", "A"),
    ("21", "ECEE"),
    ("22", "E"),
    ("23", "C"),
    ("24", "EECE"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "A"),
    ("28", "ECCE"),
    ("29", "E"),
    ("30", "C"),
  )),
))
