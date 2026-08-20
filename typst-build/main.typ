// ================================================================
// MAIN.TYP -- imuno-20-mhc-processamento-apresentacao | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "MHC e apresentação de antígenos",
  "Imunologia",
  (
    ("Disciplina", "Imunologia"),
    ("Onde estudar", "Abbas · Imunologia Celular e Molecular (10ª ed.), caps. 6 e 7 · Murphy · Janeway's Immunobiology (10ª ed.), cap. 6 · Kuby · Immunology, cap. 8"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Por que o linfócito T precisa que alguém mostre", (
      "1.1 Reconhecer é o primeiro ato",
      "1.2 BCR vê inteiro, TCR vê fragmento",
      "1.3 As três apresentadoras profissionais",
      "1.4 Da periferia ao linfonodo",
    )),
    ("PARTE II — A molécula que mostra", (
      "2.1 A fenda e os dois reconhecimentos",
      "2.2 Classe I e classe II",
      "2.3 Correceptor e restrição ao MHC",
      "2.4 HLA: herança e polimorfismo",
    )),
    ("PARTE III — Processar: as vias que fabricam o peptídeo", (
      "3.1 A origem do antígeno decide a via",
      "3.2 Via citosólica: proteassoma e TAP",
      "3.3 Via endocítica: cadeia invariante e DM",
      "3.4 Apresentação cruzada e os dois sinais",
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
    ("03", "CEEC"),
    ("04", "A"),
    ("05", "D"),
    ("06", "ECCE"),
    ("07", "B"),
    ("08", "E"),
    ("09", "CCEE"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "EECC"),
    ("13", "D"),
    ("14", "B"),
    ("15", "C"),
    ("16", "CCEC"),
    ("17", "E"),
    ("18", "A"),
    ("19", "EECE"),
    ("20", "D"),
    ("21", "B"),
    ("22", "CECC"),
    ("23", "C"),
    ("24", "E"),
    ("25", "ECEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "D"),
    ("28", "ECCC"),
    ("29", "B"),
    ("30", "CEEC"),
  )),
))
