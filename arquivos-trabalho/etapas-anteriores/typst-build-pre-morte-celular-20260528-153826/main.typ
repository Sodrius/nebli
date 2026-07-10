// ================================================================
// MAIN.TYP -- biocel-08-morte-celular | Gerado por gerar_main.py
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
  "Morte celular regulada",
  "Biologia Celular · UC01",
  (
    ("Disciplina", "Biologia Celular (UC01)"),
    ("Onde estudar", "Alberts (Fundamentos) Cap. 18 + Alberts (Molecular) Cap. 18"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Por que uma célula precisaria morrer", (
      "1.1 A célula nunca está sozinha",
      "1.2 Homeostase: nascimento × morte",
      "1.3 ACD, RCD, PCD — taxonomia moderna",
    )),
    ("PARTE II — Apoptose, a morte limpa", (
      "2.1 Morfologia: encolhe, condensa, fagocita",
      "2.2 Fosfatidilserina, o sinal 'coma-me'",
      "2.3 Caspases: iniciadoras × executoras",
      "2.4 Via extrínseca: DISC e caspase-8",
      "2.5 Via intrínseca: MOMP e apoptossomo",
      "2.6 Família Bcl-2 em três classes",
      "2.7 Crosstalk via tBid",
      "2.8 IAPs e Smac/Diablo",
      "2.9 Fatores de sobrevivência",
    )),
    ("PARTE III — Quando a apoptose não basta", (
      "3.1 Autofagia e autosis",
      "3.2 Necroptose: o plano B inflamatório",
      "3.3 Piroptose, ferroptose, NETose",
      "3.4 Clínica: p53 e a balança da homeostase",
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
    ("02", "A"),
    ("03", "CECC"),
    ("04", "A"),
    ("05", "C"),
    ("06", "B"),
    ("07", "CECE"),
    ("08", "B"),
    ("09", "B"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "C"),
    ("13", "C"),
    ("14", "CECE"),
    ("15", "C"),
    ("16", "D"),
    ("17", "E"),
    ("18", "C"),
    ("19", "CCEC"),
    ("20", "D"),
    ("21", "C"),
    ("22", "D"),
    ("23", "A"),
    ("24", "CCEC"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "D"),
    ("28", "C"),
    ("29", "B"),
    ("30", "C"),
  )),
))
