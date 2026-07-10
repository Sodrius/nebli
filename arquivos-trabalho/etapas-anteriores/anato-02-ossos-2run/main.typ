// ================================================================
// MAIN.TYP -- anato-02-ossos-generalidades | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Generalidades dos ossos",
  "Anatomia",
  (
    ("Disciplina", "Anatomia"),
    ("Onde estudar", "Moore Anatomia Orientada Cap. Introdução + Sobotta Atlas Vol. 1 (ossos)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O osso como órgão vivo", (
      "1.1 As cinco funções do osso",
      "1.2 Duas rotas para fabricar osso",
      "1.3 Mineralização é um equilíbrio",
    )),
    ("PARTE II — Arquitetura serve à carga", (
      "2.1 Cortical e esponjoso, dois problemas",
      "2.2 Ósteon: nutrir uma matriz dura",
      "2.3 Periósteo, endósteo e cartilagem",
    )),
    ("PARTE III — Forma serve à função", (
      "3.1 Cinco morfologias, cinco soluções",
      "3.2 Ossos pneumáticos e fora de série",
      "3.3 Vascularização: 4 territórios",
      "3.4 Acidentes ósseos: leitura da superfície",
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
  ("Etapa 3 — 5 discursivas mecanísticas", (
    (none, (
    )),
  )),
  ("Apêndice — Semi-glossário osteológico", (
    (none, (
    )),
  )),
  ("Gabarito consolidado da Etapa 2", (
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

// ======= APÊNDICE — SEMI-GLOSSÁRIO (custom desta corrida) =======
#etapa-header("Apêndice — Semi-glossário osteológico")
#include "etapa4.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "B"),
    ("02", "D"),
    ("03", "A"),
    ("04", "C"),
    ("05", "CECE"),
    ("06", "B"),
    ("07", "A"),
    ("08", "D"),
    ("09", "C"),
    ("10", "ECCE"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "A"),
    ("13", "E"),
    ("14", "B"),
    ("15", "D"),
    ("16", "CCEE"),
    ("17", "A"),
    ("18", "E"),
    ("19", "B"),
    ("20", "D"),
    ("21", "A"),
    ("22", "C"),
    ("23", "ECEC"),
    ("24", "B"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "E"),
    ("28", "A"),
    ("29", "C"),
    ("30", "D"),
  )),
))
