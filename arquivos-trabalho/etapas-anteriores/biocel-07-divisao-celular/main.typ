// ================================================================
// MAIN.TYP -- hemoglobina | Gerado por gerar_main.py
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
  "Hemoglobina",
  "",
  (
    ("Disciplina", "Bioquímica (UC01)"),
    ("Onde estudar", "Lehninger Cap. 5 + slides da aula"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — As peças", (
      "1.1 Heme e globina",
      "1.2 Kd, ligante e curva",
      "1.3 Por que um transportador precisa de sigmoide",
    )),
    ("PARTE II — A alostería ao vivo", (
      "2.1 Os dois estados T e R",
      "2.2 Bohr, CO₂ e o tecido que pede",
      "2.3 BPG, o ajuste fino",
    )),
    ("PARTE III — Hemoglobina no mundo", (
      "3.1 Tamponamento sanguíneo",
      "3.2 HbA, HbF e HbS",
      "3.3 CO e metahemoglobina",
    )),
  )),
  ("Resumindo", (
    (none, (
      "Os pontos que precisam estar na ponta da língua",
    )),
  )),
  ("Etapa 2 — 30 objetivas", (
    (none, (
      "10 Consolidação · 15 Integração · 5 Aplicação",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Mecanismo em até 100 palavras",
    )),
  )),
  ("Gabarito", (
    (none, (
      "Respostas da Etapa 2",
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
    ("01", "B"),
    ("02", "D"),
    ("03", "B"),
    ("04", "C"),
    ("05", "E"),
    ("06", "B"),
    ("07", "D"),
    ("08", "A"),
    ("09", "C"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "B"),
    ("13", "E"),
    ("14", "C"),
    ("15", "A"),
    ("16", "B"),
    ("17", "D"),
    ("18", "C"),
    ("19", "E"),
    ("20", "A"),
    ("21", "C"),
    ("22", "D"),
    ("23", "B"),
    ("24", "E"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "B"),
    ("28", "E"),
    ("29", "C"),
    ("30", "A"),
  )),
))
