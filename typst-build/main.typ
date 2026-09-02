// ================================================================
// MAIN.TYP -- micro-04-controle-microbiologico | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Controle do crescimento microbiano",
  "Microbiologia",
  (
    ("Disciplina", "Microbiologia"),
    ("Onde estudar", "Trabulsi & Alterthum — Microbiologia (7ª ed.) · Murray — Microbiologia Médica · Microbiologia de Brock · Tortora — Microbiologia · Anvisa — Manual de Processamento de Produtos para Saúde"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A régua: o que cada palavra promete", (
      "1.1 Quatro promessas diferentes",
      "1.3 Valor D e a morte logarítmica",
      "1.4 A escada de resistência",
    )),
    ("PARTE II — Agentes físicos", (
      "2.2 Autoclave e forno",
      "2.4 Radiação ionizante e ultravioleta",
      "2.5 Filtração e o limite de 0,22 µm",
    )),
    ("PARTE III — Agentes químicos e a decisão", (
      "3.2 Níveis e destino do artigo",
      "3.3 Como cada classe química mata",
      "3.5 Esterilizar o termossensível",
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
    ("01", "C"),
    ("02", "CECC"),
    ("03", "B"),
    ("04", "CEEC"),
    ("05", "E"),
    ("06", "D"),
    ("07", "CCEC"),
    ("08", "A"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "C"),
    ("10", "CCEE"),
    ("11", "E"),
    ("12", "B"),
    ("13", "CCEC"),
    ("14", "D"),
    ("15", "A"),
    ("16", "EECC"),
    ("17", "E"),
    ("18", "B"),
    ("19", "ECCE"),
    ("20", "C"),
    ("21", "D"),
    ("22", "ECCC"),
    ("23", "B"),
    ("24", "E"),
    ("25", "CEEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "B"),
    ("28", "CCEE"),
    ("29", "D"),
    ("30", "A"),
  )),
))
