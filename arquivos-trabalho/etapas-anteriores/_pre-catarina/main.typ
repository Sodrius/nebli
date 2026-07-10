// ================================================================
// MAIN.TYP -- cadeia-respiratoria | Gerado por gerar_main.py
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
  "Cadeia respiratória e fosforilação oxidativa",
  "",
  (
    ("Disciplina", "Bioquímica"),
    ("Onde estudar", "Lehninger Cap. 19 + Marks Cap. 24"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Por que existe uma cadeia", (
      "1.1 O problema do Krebs",
      "1.2 Potencial de redução",
      "1.3 Gradiente como moeda",
    )),
    ("PARTE II — As peças que carregam o elétron", (
      "2.1 Quatro complexos, dois móveis",
      "2.2 Complexo I",
      "2.3 Complexo II",
      "2.4 Complexo III e ciclo Q",
      "2.5 Citocromo c",
      "2.6 Complexo IV",
    )),
    ("PARTE III — Do gradiente ao ATP", (
      "3.1 ATP sintase como motor",
      "3.2 Acoplamento e desacopladores",
      "3.3 Lançadeiras de NADH",
      "3.4 Saldo final",
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
  ("Etapa 3 — 5 discursivas", (
    (none, (
    )),
  )),
  ("Gabarito da Etapa 2", (
    (none, (
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
    ("01", "C"),
    ("02", "B"),
    ("03", "A"),
    ("04", "D"),
    ("05", "B"),
    ("06", "EECC"),
    ("07", "B"),
    ("08", "A"),
    ("09", "CECC"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "A"),
    ("13", "D"),
    ("14", "CCEE"),
    ("15", "B"),
    ("16", "E"),
    ("17", "CCEC"),
    ("18", "A"),
    ("19", "C"),
    ("20", "B"),
    ("21", "C"),
    ("22", "D"),
    ("23", "CCEE"),
    ("24", "A"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "B"),
    ("28", "E"),
    ("29", "A"),
    ("30", "C"),
  )),
))
