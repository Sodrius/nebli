// ================================================================
// MAIN.TYP -- biomol-04-integracao-metabolica-i | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Especialização metabólica dos tecidos",
  "Bioquímica",
  (
    ("Disciplina", "Bioquímica"),
    ("Onde estudar", "Lehninger — Princípios de Bioquímica, cap. 23 · Berg & Stryer — Bioquímica, cap. 27 · Marks — Bioquímica Médica Básica, seção IV · Devlin — Manual de Bioquímica, cap. 20"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Quem guarda, quem gasta, quem manda", (
      "1.1 Reservas desiguais por tecido",
      "1.3 A circulação porta",
      "1.4 Glicose-6-fosfato, a encruzilhada",
    )),
    ("PARTE II — O fígado decide a glicemia", (
      "2.1 GLUT-2 e glicoquinase",
      "2.3 Frutose 2,6-bifosfato",
      "2.4 A fosforilase que escuta glicose",
    )),
    ("PARTE III — Os outros tecidos e o sensor", (
      "3.1 Músculo e o ciclo de Cori",
      "3.4 Tecido adiposo e calor",
      "3.6 O pâncreas fecha o circuito",
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
    ("03", "B"),
    ("04", "E"),
    ("05", "EECC"),
    ("06", "A"),
    ("07", "CEEC"),
    ("08", "C"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "E"),
    ("10", "CCEE"),
    ("11", "B"),
    ("12", "D"),
    ("13", "CCEC"),
    ("14", "A"),
    ("15", "C"),
    ("16", "CECC"),
    ("17", "D"),
    ("18", "E"),
    ("19", "ECCC"),
    ("20", "D"),
    ("21", "A"),
    ("22", "CEEC"),
    ("23", "C"),
    ("24", "ECEE"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "E"),
    ("28", "CEEE"),
    ("29", "E"),
    ("30", "C"),
  )),
))
