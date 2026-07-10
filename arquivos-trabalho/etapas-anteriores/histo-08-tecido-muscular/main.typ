// ================================================================
// MAIN.TYP -- histo-08-tecido-muscular | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Tecido Muscular",
  "Histologia",
  (
    ("Disciplina", "Histologia (UC02)"),
    ("Onde estudar", "Slides do Prof. FS (teórica + aula prática) · Junqueira & Carneiro, Histologia Básica, cap. 10 · Ross & Pawlina, cap. 11"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A célula muscular e sua organização", (
      "Três tecidos, uma tarefa: virar química em força",
      "O vocabulário próprio da fibra · as bainhas de conjuntivo",
      "Miofibrila, sarcômero e os filamentos",
    )),
    ("PARTE II — Como o músculo contrai e por que os três tipos diferem", (
      "Deslizamento dos filamentos · acoplamento excitação-contração",
      "Cardíaco e liso pelo contraste com o esquelético",
      "Os três tipos lado a lado · regeneração e hipertrofia",
    )),
    ("PARTE III — Reconhecer o tecido muscular ao microscópio (prática)", (
      "As três perguntas do microscópio · estriado esquelético no HE",
      "Estriado cardíaco: o disco intercalar como marcador",
      "Liso no HE · o exercício integrador do intestino",
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
    ("02", "CCE"),
    ("03", "A"),
    ("04", "E"),
    ("05", "ECCE"),
    ("06", "D"),
    ("07", "C"),
    ("08", "CEC"),
    ("09", "A"),
    ("10", "EECC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "CEE"),
    ("13", "B"),
    ("14", "E"),
    ("15", "CECC"),
    ("16", "C"),
    ("17", "A"),
    ("18", "ECE"),
    ("19", "D"),
    ("20", "B"),
    ("21", "CCEE"),
    ("22", "E"),
    ("23", "C"),
    ("24", "ECC"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "B"),
    ("28", "CEEC"),
    ("29", "E"),
    ("30", "C"),
  )),
))
