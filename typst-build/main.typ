// ================================================================
// MAIN.TYP -- digest-anato-01-esofago-estomago-delgado | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Esôfago, estômago e intestino delgado",
  "Anatomia do sistema digestório",
  (
    ("Disciplina", "Anatomia do Sistema Digestório"),
    ("Onde estudar", "Netter · Atlas de Anatomia (3ª ed.) · Sobotta · Atlas de Anatomia Humana (23ª ed.) · Moore · Anatomia Orientada para a Clínica (6ª ed.) · Gray's Anatomia para Estudantes (2ª ed.)"),
  ),
)

// ======= SUMÁRIO =======
#set-etapa("Sumário")
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O esôfago: o tubo que atravessa três territórios", (
      "1.1 Tubo de transporte, músculo que troca de comando",
      "1.2 Três porções, três estreitamentos",
      "1.3 A travessia do diafragma: hiato, cárdia e linha Z",
    )),
    ("PARTE II — O estômago: o reservatório em forma de J", (
      "2.1 Forma, função e as três camadas musculares",
      "2.2 Porções e curvaturas: o mapa cirúrgico",
      "2.3 Onde mora e em quem encosta",
    )),
    ("PARTE III — O intestino delgado: do duodeno fixo ao jejuno-íleo móvel", (
      "3.1 Três segmentos e o duodeno em C",
      "3.2 Papila maior e ligamento de Treitz",
      "3.3 Jejuno e íleo: o mesentério entrega a diferença",
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
    ("04", "D"),
    ("05", "B"),
    ("06", "ECCE"),
    ("07", "E"),
    ("08", "C"),
    ("09", "CCEE"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "EECC"),
    ("13", "B"),
    ("14", "E"),
    ("15", "CECC"),
    ("16", "A"),
    ("17", "C"),
    ("18", "ECEE"),
    ("19", "D"),
    ("20", "E"),
    ("21", "CCEC"),
    ("22", "E"),
    ("23", "B"),
    ("24", "EECE"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "ECCC"),
    ("28", "D"),
    ("29", "CCCE"),
    ("30", "E"),
  )),
))
