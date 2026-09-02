// ================================================================
// MAIN.TYP -- micro-06-genetica-bacteriana | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Genética bacteriana",
  "Microbiologia",
  (
    ("Disciplina", "Microbiologia"),
    ("Onde estudar", "Trabulsi & Alterthum — Microbiologia (7ª ed.) · Murray — Microbiologia Médica · Brock — Biologia dos Micro-organismos (cap. 9–11) · Snyder & Champness — Molecular Genetics of Bacteria"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O genoma bacteriano", (
      "1.1 Onde fica o DNA bacteriano",
      "1.3 Plasmídeo: replicon acessório",
      "1.4 Replicação e partição",
    )),
    ("PARTE II — Mutação e reparo", (
      "2.1 O erro que a química impõe",
      "2.3 Destinos do DNA lesado",
      "2.4 Quando reparar deixa de servir",
    )),
    ("PARTE III — Recombinação", (
      "3.1 Transformação: DNA nu",
      "3.2 Conjugação: contato e Hfr",
      "3.4 Transposons e ilhas",
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
    ("02", "CEEC"),
    ("03", "B"),
    ("04", "B"),
    ("05", "E"),
    ("06", "CCEE"),
    ("07", "A"),
    ("08", "C"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "E"),
    ("10", "CEEE"),
    ("11", "CECC"),
    ("12", "D"),
    ("13", "D"),
    ("14", "ECCE"),
    ("15", "A"),
    ("16", "CCCE"),
    ("17", "C"),
    ("18", "B"),
    ("19", "ECEE"),
    ("20", "E"),
    ("21", "E"),
    ("22", "ECCC"),
    ("23", "A"),
    ("24", "CCEC"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "B"),
    ("28", "EECE"),
    ("29", "C"),
    ("30", "E"),
  )),
))
