// ================================================================
// MAIN.TYP -- geriatria-envelhecimento-celular-tecidual | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Envelhecimento Celular e Tecidual",
  "Geriatria — Ciclo da Vida I",
  (
    ("Disciplina", "Geriatria — Ciclo da Vida I (UC-16) · Patologia"),
    ("Onde estudar", "Robbins & Cotran · Patologia — Bases Patológicas das Doenças (cap. Envelhecimento celular) · Jacob Filho & Kikuchi · Geriatria e Gerontologia Básicas (Elsevier) · Kane · Essentials of Clinical Geriatrics (8ª ed.)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Envelhecer é perder margem, não perder função", (
      "1.1 Senescência e senilidade",
      "1.2 A reserva funcional",
      "1.3 Homeostenose e descompensação",
    )),
    ("PARTE II — Os quatro mecanismos celulares", (
      "2.1 Dano ao DNA e radicais livres",
      "2.2 Telômeros e o relógio mitótico",
      "2.3 Proteínas e nutrientes",
    )),
    ("PARTE III — Do mecanismo ao corpo", (
      "3.1 Aspectos gerais e respiratório",
      "3.2 Sistema nervoso",
      "3.3 Cardiovascular, renal e locomotor",
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
    ("01", "B"),
    ("02", "D"),
    ("03", "CEEC"),
    ("04", "A"),
    ("05", "E"),
    ("06", "ECCE"),
    ("07", "C"),
    ("08", "D"),
    ("09", "CCEE"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "E"),
    ("12", "B"),
    ("13", "CCEC"),
    ("14", "C"),
    ("15", "E"),
    ("16", "EECC"),
    ("17", "A"),
    ("18", "D"),
    ("19", "CEEE"),
    ("20", "B"),
    ("21", "C"),
    ("22", "CECC"),
    ("23", "E"),
    ("24", "E"),
    ("25", "EECE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "ECEE"),
    ("28", "D"),
    ("29", "B"),
    ("30", "CCCE"),
  )),
))
