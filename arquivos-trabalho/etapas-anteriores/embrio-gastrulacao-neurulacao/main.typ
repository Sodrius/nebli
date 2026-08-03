// ================================================================
// MAIN.TYP -- embrio-gastrulacao-neurulacao | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Gastrulação e Neurulação",
  "Embriologia",
  (
    ("Disciplina", "Embriologia (UC02)"),
    ("Onde estudar", "Moore — Embriologia Básica (7ª ed.) + Langman/Sadler, Embriologia Médica"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Gastrulação: do disco de duas camadas ao de três", (
      "1.1 Os três folhetos vêm do epiblasto",
      "1.2 Linha primitiva, nó e ingressão (EMT)",
      "1.3 Notocorda: eixo e indutor",
    )),
    ("PARTE II — Neurulação: erguendo e fechando o tubo neural", (
      "2.1 Indução neural e o tubo neural",
      "2.2 Defeitos do tubo neural e ácido fólico",
      "2.3 Crista neural: o quarto folheto",
    )),
    ("PARTE III — Derivados do mesoderma e dobramento do corpo", (
      "3.1 As três faixas do mesoderma",
      "3.2 Dobramento céfalo-caudal",
      "3.3 Dobramento lateral e tubo digestório",
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
    ("03", "CECC"),
    ("04", "D"),
    ("05", "A"),
    ("06", "ECCE"),
    ("07", "E"),
    ("08", "C"),
    ("09", "CCEC"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "E"),
    ("12", "ECCC"),
    ("13", "E"),
    ("14", "C"),
    ("15", "D"),
    ("16", "A"),
    ("17", "CEEC"),
    ("18", "D"),
    ("19", "D"),
    ("20", "CCCE"),
    ("21", "B"),
    ("22", "E"),
    ("23", "CCEE"),
    ("24", "A"),
    ("25", "CECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "D"),
    ("28", "CCEC"),
    ("29", "C"),
    ("30", "B"),
  )),
))
