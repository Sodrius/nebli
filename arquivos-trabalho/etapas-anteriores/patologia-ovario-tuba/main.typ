// ================================================================
// MAIN.TYP -- patologia-ovario-tuba | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Patologia do ovário e da tuba uterina",
  "Patologia · Ciclo clínico",
  (
    ("Disciplina", "Patologia — Aparelho reprodutor feminino"),
    ("Onde estudar", "Robbins Cap. 22 + Respostas do Relatório e dos Casos da prof."),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O ovário: da peça ao diagnóstico", (
      "1.1 Da massa ao laudo e a lógica do O-RADS",
      "1.2 Cistos não neoplásicos e endometrioma",
      "1.3 Tumores epiteliais (seroso, mucinoso, endometrioide, Brenner)",
      "1.4 Tumores germinativos (dermoide, disgerminoma, marcadores)",
      "1.5 Cordão sexual–estroma e metástases (Krukenberg)",
    )),
    ("PARTE II — A tuba uterina", (
      "2.1 Salpingite e doença inflamatória pélvica",
      "2.2 Gravidez ectópica tubária",
      "2.3 Lesões benignas e imitadoras da tuba",
    )),
    ("PARTE III — Os cinco casos da prática, comentados", (
      "3.1 Caso 1 — endometrioma e a torção",
      "3.2 Caso 2 — cistadenoma seroso torcido",
      "3.3 Caso 3 — carcinoma seroso de alto grau",
      "3.4 Caso 4 — disgerminoma e marcadores",
      "3.5 Caso 5 — abscesso ovariano",
    )),
  )),
  ("Etapa 2 — 30 objetivas comentadas", (
    (none, (
      "Objetivas estilo prova, com Resolução logo abaixo de cada questão",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Discursivas ancoradas em macro/micro do relatório, com modelo de resposta",
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
    ("02", "B"),
    ("03", "D"),
    ("04", "A"),
    ("05", "C"),
    ("06", "B"),
    ("07", "D"),
    ("08", "C"),
    ("09", "A"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "C"),
    ("13", "B"),
    ("14", "A"),
    ("15", "D"),
    ("16", "C"),
    ("17", "B"),
    ("18", "A"),
    ("19", "D"),
    ("20", "B"),
    ("21", "B"),
    ("22", "A"),
    ("23", "D"),
    ("24", "C"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "D"),
    ("28", "C"),
    ("29", "B"),
    ("30", "A"),
  )),
))
