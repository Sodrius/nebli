// ================================================================
// MAIN.TYP -- digest-01-esofago-estomago-intestino | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Esôfago, estômago e intestino delgado",
  "Anatomia — Digestório (UC-8)",
  (
    ("Disciplina", "Anatomia — Digestório (UC-8 · Med5043)"),
    ("Onde estudar", "Moore · Anatomia Orientada para a Clínica (7ª ed.) · Drake, Vogl & Mitchell · Gray's Anatomia para Estudantes · Netter · Atlas de Anatomia Humana (3ª ed.) · Sobotta · Atlas de Anatomia Humana (23ª ed.) · Dangelo & Fattini · Anatomia humana sistêmica e segmentar (3ª ed.)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Esôfago", (
      "1.1 Um tubo entre a faringe e o estômago",
      "1.2 Porções cervical, torácica e abdominal",
      "1.3 As três constrições — onde tudo trava",
      "1.4 A passagem pelo hiato esofágico",
      "1.5 O que a doença de Chagas revela",
    )),
    ("PARTE II — Estômago", (
      "2.1 As regiões do estômago",
      "2.2 Faces anterior e posterior",
      "2.3 A musculatura em três camadas",
      "2.4 A úlcera perfurada",
    )),
    ("PARTE III — Intestino delgado", (
      "3.1 Duodeno — a porta em C ao redor do pâncreas",
      "3.2 Jejuno e íleo — dois nomes, dois comportamentos",
      "3.3 O mesentério e sua raiz",
      "3.4 Vasos jejunais, ileais e vasos retos",
      "3.5 Isquemia mesentérica + Meckel",
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
    ("01", "D"),
    ("02", "CCEC"),
    ("03", "B"),
    ("04", "E"),
    ("05", "ECCE"),
    ("06", "E"),
    ("07", "A"),
    ("08", "CECC"),
    ("09", "C"),
    ("10", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "EECC"),
    ("13", "A"),
    ("14", "CEEC"),
    ("15", "E"),
    ("16", "A"),
    ("17", "D"),
    ("18", "ECCE"),
    ("19", "B"),
    ("20", "C"),
    ("21", "CCEE"),
    ("22", "A"),
    ("23", "E"),
    ("24", "CEEC"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "C"),
    ("28", "CCEC"),
    ("29", "D"),
    ("30", "ECCE"),
  )),
))
