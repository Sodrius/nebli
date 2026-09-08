// ================================================================
// MAIN.TYP -- pat-09-patologia-infeccao-viral | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Patologia da infecção viral",
  "Patologia",
  (
    ("Disciplina", "Patologia"),
    ("Onde estudar", "Robbins & Cotran, Patologia — Bases Patológicas das Doenças, capítulo de Doenças Infecciosas (§ mecanismos de lesão viral) e capítulo do Fígado e Vias Biliares (§ hepatites virais) · Brasileiro Filho, Bogliolo Patologia, capítulo de doenças causadas por vírus · Abbas, Imunologia Celular e Molecular, § imunidade aos vírus (interferon tipo I, célula NK e linfócito T citotóxico)"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O que o vírus faz com a célula", (
      "1.1 Sete efeitos, três destinos",
      "1.2 Inclusões e o compartimento de montagem",
      "1.3 Sincício e coilócito",
    )),
    ("PARTE II — A resposta esculpe a lesão", (
      "2.1 Cronologia e infiltrado",
      "2.2 Interferon tipo I",
      "2.3 Célula NK e linfócito T CD8",
    )),
    ("PARTE III — Hepatite viral", (
      "3.1 O vírus B no hepatócito",
      "3.2 Necrose e apoptose hepatocitária",
      "3.3 Do infiltrado à cirrose",
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
    ("02", "E"),
    ("03", "ECCE"),
    ("04", "A"),
    ("05", "D"),
    ("06", "C"),
    ("07", "CEEC"),
    ("08", "E"),
    ("09", "CCEE"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "CCEC"),
    ("13", "D"),
    ("14", "C"),
    ("15", "EECC"),
    ("16", "E"),
    ("17", "A"),
    ("18", "CECC"),
    ("19", "B"),
    ("20", "D"),
    ("21", "ECEE"),
    ("22", "C"),
    ("23", "E"),
    ("24", "CCCE"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "B"),
    ("28", "EECE"),
    ("29", "C"),
    ("30", "ECCC"),
  )),
))
