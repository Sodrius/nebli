// ================================================================
// MAIN.TYP -- patologia-02-acumulos-celulares | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Acúmulos Celulares e Teciduais",
  "Patologia Geral",
  (
    ("Disciplina", "Patologia — Departamento de Patologia FMUSP"),
    ("Onde estudar", "Robbins & Cotran · Patologia — Bases Patológicas das Doenças (cap. Lesão e adaptação celular · Acúmulos intracelulares · Calcificação patológica) · Bogliolo · Patologia Geral (Degenerações e Pigmentações)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A lógica do acúmulo e a gordura no fígado", (
      "1.1 Acúmulo é balanço quebrado",
      "1.2 O trânsito da gordura no hepatócito",
      "1.3 Esteatose: onde o trânsito quebra",
      "1.4 Colesterol fora do fígado",
    )),
    ("PARTE II — Proteína, glicogênio e cálcio", (
      "2.1 Proteínas e o controle de qualidade",
      "2.2 Glicogênio: duas causas, um estoque",
      "2.3 Calcificação distrófica",
      "2.4 Calcificação metastática",
    )),
    ("PARTE III — Pigmentos: a memória colorida da célula", (
      "3.1 Pigmentos exógenos",
      "3.2 Lipofuscina e melanina",
      "3.3 Hemossiderina e o ferro",
      "3.4 Bilirrubina e icterícia",
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
    ("03", "EEEC"),
    ("04", "E"),
    ("05", "EECC"),
    ("06", "C"),
    ("07", "C"),
    ("08", "CECC"),
    ("09", "E"),
    ("10", "CEEE"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "CCEC"),
    ("13", "B"),
    ("14", "D"),
    ("15", "CEEE"),
    ("16", "E"),
    ("17", "A"),
    ("18", "EECE"),
    ("19", "B"),
    ("20", "C"),
    ("21", "ECEE"),
    ("22", "E"),
    ("23", "B"),
    ("24", "CCEE"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "EEEC"),
    ("28", "B"),
    ("29", "A"),
    ("30", "E"),
  )),
))
