// ================================================================
// MAIN.TYP -- pat-01-ferramentas-diagnostico-patologico | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Ferramentas do diagnóstico patológico",
  "Patologia",
  (
    ("Disciplina", "Patologia"),
    ("Onde estudar", "Robbins & Cotran — Patologia: Bases Patológicas das Doenças (cap. 1) · Bogliolo — Patologia Geral (cap. 1 e 2) · Rosai and Ackerman's Surgical Pathology (cap. 1) · Manual de procedimentos do laboratório de anatomia patológica"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A doença como cadeia", (
      "1.1 Etiologia e patogênese",
      "1.2 Morfologia: presença, grau e tempo",
      "1.3 Frentes da patologia e causa da morte",
    )),
    ("PARTE II — Do corpo à lâmina", (
      "2.1 Macroscopia e amostragem",
      "2.2 Fixação e processamento",
      "2.3 Citopatologia e punção guiada",
    )),
    ("PARTE III — As cinco ferramentas", (
      "3.1 Hematoxilina e eosina: química das cores",
      "3.2 Histoquímica: reações por classe",
      "3.3–3.4 Anticorpo, elétron e sonda",
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
    ("02", "CCEE"),
    ("03", "D"),
    ("04", "A"),
    ("05", "CCEC"),
    ("06", "B"),
    ("07", "E"),
    ("08", "CECC"),
    ("09", "D"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "E"),
    ("12", "CCCE"),
    ("13", "ECCC"),
    ("14", "C"),
    ("15", "ECEE"),
    ("16", "A"),
    ("17", "D"),
    ("18", "EECC"),
    ("19", "B"),
    ("20", "E"),
    ("21", "CEEC"),
    ("22", "C"),
    ("23", "A"),
    ("24", "ECCE"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "E"),
    ("28", "CEEE"),
    ("29", "C"),
    ("30", "D"),
  )),
))
