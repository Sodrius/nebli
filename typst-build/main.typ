// ================================================================
// MAIN.TYP -- correlacao-radio-pato-2 | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Correlação radiopatológica do fígado",
  "Radiologia e Patologia",
  (
    ("Disciplina", "Correlação Radiológica-Patológica — Preceptoria"),
    ("Onde estudar", "Robbins & Cotran — Patologia (cap. Fígado e vias biliares) · Brant & Helms — Fundamentos de Radiologia (abdome) · Bogliolo — Patologia · Herring — Radiologia Básica"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O fígado normal e a régua da imagem", (
      "1.1 A arquitetura que a imagem enxerga",
      "1.2 Ecogenicidade e densidade no fígado normal",
      "1.3 As três fases do contraste",
    )),
    ("PARTE II — Caso 1: o nódulo achado por acaso", (
      "2.1 O achado incidental e a pergunta que ele obriga",
      "2.2 O padrão dinâmico que fecha o diagnóstico",
      "2.3 A macroscopia e a histologia do hemangioma",
    )),
    ("PARTE III — Caso 2: o fígado que endureceu", (
      "3.1 Do álcool à esteatose",
      "3.2 Fibrose e nódulos de regeneração",
      "3.3 Hipertensão portal e suas colaterais",
      "3.4 Colestase, falência e carcinoma",
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
    ("02", "A"),
    ("03", "CECC"),
    ("04", "D"),
    ("05", "B"),
    ("06", "ECCE"),
    ("07", "E"),
    ("08", "CCEC"),
    ("09", "C"),
    ("10", "ECCC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "CCCE"),
    ("13", "D"),
    ("14", "B"),
    ("15", "CCEE"),
    ("16", "E"),
    ("17", "B"),
    ("18", "CEEC"),
    ("19", "A"),
    ("20", "C"),
    ("21", "CCEC"),
    ("22", "B"),
    ("23", "E"),
    ("24", "ECCC"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "A"),
    ("28", "CCCE"),
    ("29", "B"),
    ("30", "E"),
  )),
))
