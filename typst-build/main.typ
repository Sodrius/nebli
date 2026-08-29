// ================================================================
// MAIN.TYP -- imuno-06-sistema-complemento | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Sistema complemento",
  "Imunologia",
  (
    ("Disciplina", "Imunologia"),
    ("Onde estudar", "Abbas — Imunologia Celular e Molecular (10ª ed., cap. 13) · Janeway/Murphy — Immunobiology (10ª ed., cap. 2) · Roitt — Fundamentos de Imunologia (13ª ed., cap. 4)"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#set-etapa("Sumário")
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Reconhecimento: três portas", (
      "1.1 Zimogênio, clivagem e convertase",
      "1.2 Via clássica: dois Fc vizinhos",
      "1.4 Via alternativa: vigilância contínua",
    )),
    ("PARTE II — Fase enzimática e freios", (
      "2.1 O tioéster que cola a etiqueta",
      "2.2 Amplificação e decisão de superfície",
      "2.3 C5 convertase e o poro",
    )),
    ("PARTE III — Fase efetora e clínica", (
      "3.1 Receptores e opsonização",
      "3.3 Imunocomplexos e corpos apoptóticos",
      "3.5 O mapa das deficiências",
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
  ("Consolidação (Q01–Q08)", (
    ("01", "C"),
    ("02", "E"),
    ("03", "ECEE"),
    ("04", "B"),
    ("05", "E"),
    ("06", "CECC"),
    ("07", "E"),
    ("08", "CEEC"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "C"),
    ("10", "C"),
    ("11", "CCEE"),
    ("12", "A"),
    ("13", "A"),
    ("14", "CCEC"),
    ("15", "D"),
    ("16", "ECCE"),
    ("17", "E"),
    ("18", "EECC"),
    ("19", "D"),
    ("20", "E"),
    ("21", "CCCE"),
    ("22", "A"),
    ("23", "A"),
    ("24", "EECE"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "A"),
    ("28", "ECCC"),
    ("29", "C"),
    ("30", "B"),
  )),
))
