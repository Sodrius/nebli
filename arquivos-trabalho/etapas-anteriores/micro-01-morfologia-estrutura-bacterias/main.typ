// ================================================================
// MAIN.TYP -- micro-01-morfologia-estrutura-bacterias | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Morfologia e estrutura bacteriana",
  "Microbiologia",
  (
    ("Disciplina", "Microbiologia"),
    ("Onde estudar", "Trabulsi & Alterthum — Microbiologia (7ª ed.) · Murray — Microbiologia Médica · Microbiologia de Brock (cap. 2) · Tortora — Microbiologia (cap. 4)"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A bactéria e o que ela mostra", (
      "1.1 Procarioto: viver sem núcleo",
      "1.2 Da amostra ao grupo",
      "1.3 Colônia: o clone visível",
    )),
    ("PARTE II — Membrana e parede", (
      "2.2 Peptidoglicano e pressão osmótica",
      "2.4 Gram-negativas: LPS e periplasma",
      "2.5 A coloração de Gram e suas fugas",
    )),
    ("PARTE III — Estruturas que definem o comportamento", (
      "3.1 Nucleoide, plasmídeo e 70S",
      "3.3 Flagelo, pili e adesão",
      "3.5 Cápsula, biofilme e esporo",
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
    ("02", "B"),
    ("03", "CCEE"),
    ("04", "E"),
    ("05", "EECC"),
    ("06", "A"),
    ("07", "CCEC"),
    ("08", "C"),
    ("09", "C"),
    ("10", "EECC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "CEEC"),
    ("13", "A"),
    ("14", "D"),
    ("15", "CEEE"),
    ("16", "C"),
    ("17", "E"),
    ("18", "ECCE"),
    ("19", "B"),
    ("20", "E"),
    ("21", "CECC"),
    ("22", "A"),
    ("23", "E"),
    ("24", "ECCE"),
    ("25", "E"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "D"),
    ("28", "EECC"),
    ("29", "E"),
    ("30", "C"),
  )),
))
