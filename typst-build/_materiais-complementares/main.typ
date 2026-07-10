// ================================================================
// MAIN.TYP -- osso-articulacoes (materiais complementares)
// ================================================================

#import "../../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Osso vivo e articulações sinoviais",
  "Anatomia",
  (
    ("Disciplina", "Anatomia"),
    ("Onde estudar", "Material complementar — Generalidade dos ossos e Generalidade das articulações; Moore e Drake (Gray) — sistema esquelético e articulações"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O osso vivo", (
      "1.1 Osso é tecido em obra permanente",
      "1.2 A equipe celular",
      "1.3 Formação contra reabsorção",
      "1.4 O osso como banco de minerais",
      "1.5 O osso como glândula",
    )),
    ("PARTE II — Articulações sinoviais", (
      "2.1 Onde a sinovial se encaixa",
      "2.2 A regra: forma, eixos, movimento",
      "2.3 As uniaxiais",
      "2.4 As biaxiais",
      "2.5 A triaxial e a plana",
    )),
  )),
  ("Etapa 2 — 30 questões objetivas", (
    (none, ()),
  )),
  ("Etapa 3 — 5 questões discursivas", (
    (none, ()),
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
    ("01", "B"), ("02", "D"), ("03", "A"), ("04", "E"), ("05", "C"),
    ("06", "B"), ("07", "D"), ("08", "A"), ("09", "C"), ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"), ("12", "A"), ("13", "E"), ("14", "C"), ("15", "B"),
    ("16", "D"), ("17", "A"), ("18", "E"), ("19", "C"), ("20", "A"),
    ("21", "B"), ("22", "D"), ("23", "E"), ("24", "A"), ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"), ("27", "E"), ("28", "C"), ("29", "A"), ("30", "D"),
  )),
))
