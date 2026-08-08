// ================================================================
// MAIN.TYP -- digest-01-esofago-estomago-intestino | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Esôfago, estômago e intestino delgado",
  "Anatomia do Sistema Digestório",
  (
    ("Disciplina", "Anatomia"),
    ("Onde estudar", "Slides e roteiro da Profa. Patrícia Castelucci · Moore — Anatomia Orientada para a Clínica · Netter"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Esôfago e estômago", (
      "1.1 Trajeto, porções e parede do esôfago",
      "1.2 Constrições e transição esofagogástrica",
      "1.3 Regiões, curvaturas e marcos do estômago",
      "1.4 Faces e relações do estômago",
    )),
    ("PARTE II — Duodeno e papila maior", (
      "2.1 Quatro porções e relações do duodeno",
      "2.2 Papila maior e encontro das vias biliar e pancreática",
      "2.3 Flexura duodenojejunal e ligamento de Treitz",
    )),
    ("PARTE III — Jejuno e íleo", (
      "3.1 Continuidade, posição e mesentério",
      "3.2 Parede, pregas e aspecto macroscópico",
      "3.3 Arcadas e vasos retos distinguem jejuno de íleo",
      "3.4 Junção ileocecal e fechamento do trajeto",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"

// ======= ETAPA 2 =======
#set-etapa("Etapa 2 — 30 objetivas")
#pagebreak()
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#set-etapa("Etapa 3 — 5 discursivas")
#pagebreak()
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "C"),
    ("02", "B"),
    ("03", "CEEC"),
    ("04", "D"),
    ("05", "A"),
    ("06", "ECCC"),
    ("07", "E"),
    ("08", "B"),
    ("09", "CCEE"),
    ("10", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "CCEE"),
    ("13", "C"),
    ("14", "E"),
    ("15", "CCEC"),
    ("16", "B"),
    ("17", "D"),
    ("18", "ECCE"),
    ("19", "A"),
    ("20", "C"),
    ("21", "D"),
    ("22", "CECC"),
    ("23", "B"),
    ("24", "E"),
    ("25", "CEEC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "B"),
    ("28", "CCEE"),
    ("29", "C"),
    ("30", "ECCE"),
  )),
))
