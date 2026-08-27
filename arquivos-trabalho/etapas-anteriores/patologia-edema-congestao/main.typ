// ================================================================
// MAIN.TYP -- patologia-edema-congestao | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Edema e Congestão",
  "Patologia Geral",
  (
    ("Disciplina", "Patologia Geral — Princípios do Desenvolvimento das Doenças"),
    ("Onde estudar", "Robbins & Cotran · Patologia — Bases Patológicas das Doenças (10ª ed.), Cap. 4 — Distúrbios Hemodinâmicos · Bogliolo · Patologia Geral, cap. de Distúrbios da Circulação"),
  ),
)

// ======= SUMÁRIO =======
#set-etapa("Sumário")
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O interstício, as forças de Starling e o vocabulário das coleções", (
      "1.1 Onde a água do corpo mora",
      "1.2 As quatro forças e o dreno linfático",
      "1.3 Transudato, exsudato, hiperemia e congestão",
    )),
    ("PARTE II — Os cinco mecanismos que produzem edema", (
      "2.1 Pressão hidrostática aumentada",
      "2.2 Pressão oncótica reduzida",
      "2.3 Linfa, sódio e permeabilidade",
    )),
    ("PARTE III — Morfologia, órgãos-alvo e consequência clínica", (
      "3.1 Morfologia do edema e da congestão",
      "3.2 Pulmão: transudato e dano alveolar",
      "3.3 Ascite, cirrose e o preço do edema",
    )),
  )),
))

// ======= ETAPA 1 =======
#pagebreak(weak: true)
#set-etapa("Etapa 1 — Texto didático")
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#pagebreak(weak: true)
#set-etapa("Resumindo")
#include "resumindo.typ"

// ======= DO ZERO (2a parte do Resumindo) =======
#pagebreak(weak: true)
#set-etapa("Do zero")
#include "resumindo-zero.typ"

// ======= ETAPA 2 =======
#pagebreak(weak: true)
#set-etapa("Etapa 2 — 30 objetivas")
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#pagebreak(weak: true)
#set-etapa("Etapa 3 — 5 discursivas")
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#pagebreak(weak: true)
#set-etapa("Gabarito — Etapa 2")
#gabarito-page((
  ("Consolidação (Q01–Q08)", (
    ("01", "B"),
    ("02", "E"),
    ("03", "CECC"),
    ("04", "B"),
    ("05", "A"),
    ("06", "ECCE"),
    ("07", "D"),
    ("08", "C"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "E"),
    ("10", "CCEE"),
    ("11", "A"),
    ("12", "C"),
    ("13", "EECC"),
    ("14", "D"),
    ("15", "D"),
    ("16", "B"),
    ("17", "CEEC"),
    ("18", "A"),
    ("19", "E"),
    ("20", "ECCC"),
    ("21", "C"),
    ("22", "A"),
    ("23", "CCEC"),
    ("24", "D"),
    ("25", "EECE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "CEEE"),
    ("28", "E"),
    ("29", "ECEE"),
    ("30", "C"),
  )),
))
