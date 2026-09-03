// ================================================================
// MAIN.TYP -- gr-02-diabetes-mellitus | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Diabetes mellitus",
  "Da hiperglicemia às complicações de órgão-alvo",
  (
    ("Disciplina", "Patologia · Bioquímica · Imunologia · Radiologia"),
    ("Onde estudar", "Robbins & Cotran, Patologia — capítulo do Sistema Endócrino, § Diabetes mellitus · Lehninger, Princípios de Bioquímica — Regulação hormonal e integração metabólica · Brant & Helms, Fundamentos de Radiologia — tórax cardiovascular e musculoesquelético"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O sinal que falta", (
      "1.1 O que a insulina manda fazer",
      "1.2 Tipo 1: ilhota destruída",
      "1.3 Tipo 2: sinal não escutado",
    )),
    ("PARTE II — Do açúcar ao dano", (
      "2.1 Schiff, Amadori e AGE",
      "2.2 Dois relógios do controle",
      "2.3 RAGE e as quatro rotas",
    )),
    ("PARTE III — Onde o dano aparece", (
      "3.1 Retina e glomérulo",
      "3.2 Nervo e pé diabético",
      "3.3 Aterosclerose e imagem",
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
    ("02", "ECCE"),
    ("03", "B"),
    ("04", "E"),
    ("05", "CCEE"),
    ("06", "A"),
    ("07", "CCCE"),
    ("08", "D"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "B"),
    ("10", "CCEC"),
    ("11", "E"),
    ("12", "A"),
    ("13", "CECC"),
    ("14", "B"),
    ("15", "D"),
    ("16", "ECCC"),
    ("17", "B"),
    ("18", "C"),
    ("19", "CEEC"),
    ("20", "E"),
    ("21", "A"),
    ("22", "EECC"),
    ("23", "D"),
    ("24", "A"),
    ("25", "CEEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "E"),
    ("28", "A"),
    ("29", "D"),
    ("30", "EECE"),
  )),
))
