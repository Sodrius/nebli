// ================================================================
// MAIN.TYP -- patologia-01-lesao-celular | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Lesão celular",
  "Patologia — mecanismos de lesão e morte celular",
  (
    ("Disciplina", "Patologia — Mecanismos de lesão e morte celular"),
    ("Onde estudar", "Robbins & Cotran — Patologia: Bases Patológicas das Doenças (10ª ed.) cap. 2 · Robbins Patologia Básica (10ª ed.) cap. 1-2 · Kumar, Abbas & Aster — Fundamentos de Patologia"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Do equilíbrio à irreversibilidade", (
      "1.1 Adaptação, lesão e o limiar",
      "1.2 As causas da lesão celular",
      "1.3 Cronologia e morfologia reversível",
      "1.4 O ponto sem retorno",
    )),
    ("PARTE II — A cascata da isquemia", (
      "2.1 Queda de ATP e bombas",
      "2.2 Mitocôndria e poro de transição",
      "2.3 Cálcio citosólico como demolidor",
      "2.4 Dano de membrana: via final",
    )),
    ("PARTE III — Oxigênio, proteínas e destino", (
      "3.1 Radicais livres e defesas",
      "3.2 Lesão de isquemia-reperfusão",
      "3.3 Proteínas mal dobradas e DNA",
      "3.4 Necrose e apoptose",
    )),
  )),
  ("Resumindo", (
    (none, (
    )),
  )),
  ("Etapa 2 — 30 questões objetivas", (
    (none, (
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
    )),
  )),
  ("Gabarito da Etapa 2", (
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
    ("01", "D"),
    ("02", "B"),
    ("03", "CECC"),
    ("04", "D"),
    ("05", "ECEE"),
    ("06", "E"),
    ("07", "B"),
    ("08", "CCCE"),
    ("09", "B"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "ECCC"),
    ("13", "B"),
    ("14", "A"),
    ("15", "CCEC"),
    ("16", "C"),
    ("17", "A"),
    ("18", "E"),
    ("19", "ECCC"),
    ("20", "A"),
    ("21", "C"),
    ("22", "CECC"),
    ("23", "D"),
    ("24", "C"),
    ("25", "ECCE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "A"),
    ("28", "CEEC"),
    ("29", "C"),
    ("30", "CCEC"),
  )),
))
