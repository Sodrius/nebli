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
      "1.1 A insulina e seus freios",
      "1.2 Tipo 1: ilhota destruída",
      "1.3 Tipo 2: sinal não escutado",
      "1.4 Diurese osmótica e descompensações",
    )),
    ("PARTE II — Do açúcar ao dano", (
      "2.1 Glicação e os dois relógios",
      "2.2 O AGE nas proteínas de vida longa",
      "2.3 RAGE e as outras rotas",
    )),
    ("PARTE III — Onde o dano aparece", (
      "3.1 Retina e glomérulo",
      "3.2 Neuropatia e pé diabético",
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
    ("01", "D"),
    ("02", "ECCE"),
    ("03", "C"),
    ("04", "A"),
    ("05", "CCCE"),
    ("06", "E"),
    ("07", "CCEE"),
    ("08", "C"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "B"),
    ("10", "CCEC"),
    ("11", "D"),
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
    ("24", "B"),
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
