// ================================================================
// MAIN.TYP -- bioq-26-acao-hormonal | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Ação hormonal",
  "Bioquímica",
  (
    ("Disciplina", "Bioquímica"),
    ("Onde estudar", "Lehninger · Princípios de Bioquímica, cap. 23 (regulação hormonal e integração do metabolismo) · Berg & Stryer · Biochemistry (transdução de sinal) · Marzzoco & Torres · Bioquímica Básica"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Regulação metabólica e a identidade do hormônio", (
      "1.1 As três alavancas da regulação",
      "1.2 O que faz de uma molécula um hormônio",
      "1.3 Classe química decide a rota",
    )),
    ("PARTE II — A máquina da transdução do sinal", (
      "2.1 Cinco jeitos de atravessar a membrana",
      "2.2 A cascata do AMPc e a amplificação",
      "2.3 O receptor que reescreve o programa",
    )),
    ("PARTE III — Os hormônios do metabolismo em ação", (
      "3.1 Insulina: sensor, secreção e efeito",
      "3.2 Glucagon e adrenalina na escassez",
      "3.3 Tireoidianos, cortisol e impostores",
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
    ("02", "CEEC"),
    ("03", "B"),
    ("04", "E"),
    ("05", "ECCE"),
    ("06", "A"),
    ("07", "C"),
    ("08", "CCEE"),
    ("09", "E"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "EECC"),
    ("13", "A"),
    ("14", "C"),
    ("15", "CECC"),
    ("16", "D"),
    ("17", "ECCC"),
    ("18", "CEEE"),
    ("19", "B"),
    ("20", "E"),
    ("21", "CCEC"),
    ("22", "A"),
    ("23", "E"),
    ("24", "EECE"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "C"),
    ("28", "ECEE"),
    ("29", "A"),
    ("30", "B"),
  )),
))
