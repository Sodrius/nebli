// ================================================================
// MAIN.TYP -- anato-04-musculos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Generalidades dos músculos",
  "Anatomia",
  (
    ("Disciplina", "Anatomia"),
    ("Onde estudar", "Moore — Introdução à Anatomia (sistema muscular); Drake (Gray) — Sistema muscular e classificação dos músculos"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O que o músculo faz", (
      "1.1 Unidade motora e modos de contração",
      "1.2 Alavancas: força e movimento",
      "1.3 Trabalho em equipe e adaptação",
    )),
    ("PARTE II — Três tipos de músculo", (
      "2.1 Estriado, liso e cardíaco",
      "2.2 O músculo liso em ação",
      "2.3 O esquelético: a peça",
    )),
    ("PARTE III — A arquitetura conjuntiva", (
      "3.1 Do epimísio ao endomísio",
      "3.2 Tendões: a corda inextensível",
      "3.3 Retináculos e aponeuroses",
    )),
    ("PARTE IV — A forma anuncia a função", (
      "4.1 Fascículo × tendão",
      "4.2 Força contra amplitude",
      "4.3 Os nomes e o cruzamento articular",
    )),
  )),
  ("Etapa 2 — 30 questões objetivas", (
    (none, (
    )),
  )),
  ("Etapa 3 — 5 questões discursivas", (
    (none, (
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
    ("01", "A"),
    ("02", "C"),
    ("03", "D"),
    ("04", "B"),
    ("05", "E"),
    ("06", "C"),
    ("07", "A"),
    ("08", "D"),
    ("09", "B"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "A"),
    ("13", "D"),
    ("14", "B"),
    ("15", "E"),
    ("16", "A"),
    ("17", "B"),
    ("18", "D"),
    ("19", "B"),
    ("20", "E"),
    ("21", "A"),
    ("22", "C"),
    ("23", "D"),
    ("24", "C"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "A"),
    ("28", "D"),
    ("29", "B"),
    ("30", "D"),
  )),
))
