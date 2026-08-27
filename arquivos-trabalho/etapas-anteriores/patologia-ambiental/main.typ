// ================================================================
// MAIN.TYP -- patologia-ambiental | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Patologia Ambiental",
  "Patologia Geral",
  (
    ("Disciplina", "Patologia Geral — Princípios do Desenvolvimento das Doenças"),
    ("Onde estudar", "Robbins & Cotran · Patologia — Bases Patológicas das Doenças (10ª ed.), Cap. 9 — Doenças Ambientais e Nutricionais · Bogliolo · Patologia Geral, cap. de Patologia Ambiental"),
  ),
)

// ======= SUMÁRIO =======
#set-etapa("Sumário")
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O ambiente como causa de doença", (
      "1.1 Da Revolução Industrial ao nevoeiro de 1952",
      "1.2 O iceberg dos efeitos",
      "1.3 Do xenobiótico à lesão celular",
    )),
    ("PARTE II — O ar poluído e o pulmão", (
      "2.1 Poluentes primários e secundários",
      "2.2 O tamanho decide o destino",
      "2.3 Do macrófago à inflamação crônica",
    )),
    ("PARTE III — Além do pulmão: artéria, população e método", (
      "3.1 Do alvéolo à parede arterial",
      "3.2 Aterosclerose e desfecho cardiovascular",
      "3.3 Dose-resposta e o experimento natural",
    )),
  )),
))

// ======= ETAPA 1 =======
#pagebreak(weak: true)
#set-etapa("Etapa 1 — Texto didático")
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#pagebreak(weak: true)
#set-etapa("Resumindo")
#include "resumindo.typ"

// ======= DO ZERO (2a parte do Resumindo) =======
#pagebreak(weak: true)
#set-etapa("Do zero")
#include "resumindo-zero.typ"

// ======= ETAPA 2 =======
#pagebreak(weak: true)
#set-etapa("Etapa 2 — 30 objetivas")
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#pagebreak(weak: true)
#set-etapa("Etapa 3 — 5 discursivas")
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#pagebreak(weak: true)
#set-etapa("Gabarito — Etapa 2")
#gabarito-page((
  ("Consolidação (Q01–Q08)", (
    ("01", "D"),
    ("02", "CCEC"),
    ("03", "A"),
    ("04", "C"),
    ("05", "E"),
    ("06", "B"),
    ("07", "ECEE"),
    ("08", "D"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "C"),
    ("10", "A"),
    ("11", "EECC"),
    ("12", "E"),
    ("13", "B"),
    ("14", "CEEC"),
    ("15", "C"),
    ("16", "CCEE"),
    ("17", "D"),
    ("18", "ECCE"),
    ("19", "A"),
    ("20", "B"),
    ("21", "CEEE"),
    ("22", "E"),
    ("23", "C"),
    ("24", "EECE"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "ECCC"),
    ("28", "B"),
    ("29", "CECC"),
    ("30", "E"),
  )),
))
