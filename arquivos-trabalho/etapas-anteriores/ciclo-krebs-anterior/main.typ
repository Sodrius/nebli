// ================================================================
// MAIN.TYP -- biocel-07-divisao-celular | Gerado por gerar_main.py
// Canonico 2026-05-15/16:
//   - Sem Etapa 5 (NEBLIcards removida)
//   - Resumindo LOGO APOS E1
//   - Sem secao de glossario no fim (siglas em footnote no rodape)
//   - Cores E4 por formato
//   - Taxonomia E2 parametrizada pelo guia editorial
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Divisão celular, células interfásicas e mitóticas",
  "",
  (
    ("Disciplina", "Biologia Celular (UC01)"),
    ("Onde estudar", "Junqueira & Carneiro (Biologia Celular e Molecular, 10ª ed.) cap. 17 · Alberts (Molecular Biology of the Cell) cap. 17 · Morgan, The Cell Cycle: Principles of Control"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O ciclo celular e como se estuda", (
      "1.1 Por que dividir, crescimento vs proliferação",
      "1.2 Quatro fases e quantidade de DNA",
      "1.3 BrdU, citometria, Ki67",
      "1.4 Tudo-ou-nada e checkpoints",
    )),
    ("PARTE II — O motor: ciclinas, CDKs e controladores", (
      "2.1 Descoberta e lógica do par",
      "2.2 Regulação multicamadas das CDKs",
      "2.3 Quatro complexos por fase (TIMER)",
      "2.4 APC/C, SCF e Pre-RC",
      "2.5 Mitógenos, Rb e E2F",
    )),
    ("PARTE III — Mitose pelo motor + câncer", (
      "3.1 Entrada em M e cascata do M-CDK",
      "3.2 Cinetócoro e checkpoint do fuso",
      "3.3 Anáfase, APC/C, separase, coesina",
      "3.4 Telófase e citocinese (actina+miosina II)",
      "3.5 p53, Rb, HPV e câncer",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO (logo apos E1, canonico 2026-05-15) =======
#include "resumindo.typ"

// ======= ETAPA 2 =======
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
// E4 removida do pipeline canônico em 2026-05-22 (banco vira calibração, não inclusão).
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "D"),
    ("02", "B"),
    ("03", "A"),
    ("04", "C"),
    ("05", "C"),
    ("06", "A"),
    ("07", "B"),
    ("08", "D"),
    ("09", "B"),
    ("10", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "D"),
    ("13", "B"),
    ("14", "A"),
    ("15", "D"),
    ("16", "E"),
    ("17", "B"),
    ("18", "C"),
    ("19", "A"),
    ("20", "D"),
    ("21", "D"),
    ("22", "E"),
    ("23", "B"),
    ("24", "A"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "A"),
    ("28", "B"),
    ("29", "B"),
    ("30", "D"),
  )),
))
