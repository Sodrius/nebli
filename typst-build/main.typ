// ================================================================
// MAIN.TYP -- bioq-26-controle-hormonal | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Controle Hormonal do Metabolismo: do Sinal na Membrana ao Gene no Núcleo",
  "Bioquímica",
  (
    ("Disciplina", "Bioquímica (UC02)"),
    ("Onde estudar", "Slides da aula Controle Hormonal (UC02, Bioquímica, Profa. Deborah Schechtman) · Lehninger, Princípios de Bioquímica, cap. 23 (Regulação Hormonal e Integração do Metabolismo) · Berg/Stryer, cap. 14 (Vias de Transdução de Sinal)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O sinal: o que é um hormônio e como ele chega", (
      "Integração metabólica e o problema da distância",
      "Classes químicas e solubilidade",
      "Receptores e tipos de transdutor",
    )),
    ("PARTE II — Hormônios que ficam na membrana", (
      "Insulina: da pré-pró-insulina ao grânulo",
      "A célula beta como sensor de glicose",
      "Glicogênio e a cascata do AMPc",
    )),
    ("PARTE III — Hormônios que entram na célula", (
      "Receptor nuclear e latência de horas",
      "Tireoidianos: T4 como pró-hormônio",
      "Cortisol, eixo HPA e disruptores",
    )),
  )),
))

// ======= ETAPA 1 =======
#set-etapa("Etapa 1 — Texto didático")
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#set-etapa("Resumindo")
#include "resumindo.typ"

// ======= ETAPA 2 =======
#set-etapa("Etapa 2 — 30 objetivas")
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#set-etapa("Etapa 3 — 5 discursivas")
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#set-etapa("Gabarito — Etapa 2")
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "C"),
    ("02", "CEEC"),
    ("03", "A"),
    ("04", "E"),
    ("05", "ECCE"),
    ("06", "B"),
    ("07", "D"),
    ("08", "CECC"),
    ("09", "A"),
    ("10", "EECE"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "EECC"),
    ("13", "D"),
    ("14", "A"),
    ("15", "CCEE"),
    ("16", "C"),
    ("17", "E"),
    ("18", "ECEC"),
    ("19", "B"),
    ("20", "D"),
    ("21", "CEEE"),
    ("22", "A"),
    ("23", "C"),
    ("24", "ECCC"),
    ("25", "E"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "CCEC"),
    ("28", "B"),
    ("29", "E"),
    ("30", "C"),
  )),
))
