// ================================================================
// MAIN.TYP -- ciclo-krebs | Gerado por gerar_main.py
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
  "Ciclo de Krebs",
  "Bioquímica",
  (
    ("Disciplina", "Bioquímica — Metabolismo de carboidratos (UC01)"),
    ("Onde estudar", "Lehninger 7ª ed., Cap. 16 (Ciclo do ácido cítrico) — pp. 633–670"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Antes do ciclo: o piruvato precisa entrar", (
      "1.1 Por que existe o ciclo e onde ele roda",
      "1.2 PDH: o passo 0, a porta de entrada",
      "1.3 O acetil-CoA é o substrato real do ciclo",
    )),
    ("PARTE II — As 8 reações em sequência", (
      "2.1 Passos 1 e 2: condensação e isomerização",
      "2.2 Passos 3 e 4: as duas descarboxilações",
      "2.3 Passo 5: GTP em nível de substrato",
      "2.4 Passo 6: FADH₂ na membrana",
      "2.5 Passos 7 e 8: fechando o ciclo",
      "2.6 Tabela-síntese das 8 reações",
    )),
    ("PARTE III — Saldo, regulação e anfibolismo", (
      "3.1 Saldo energético",
      "3.2 Regulação",
      "3.3 Anfibolismo",
      "3.4 Conclusão integradora",
    )),
  )),
  ("Resumindo", (
    (none, (
      "Síntese em 1–2 páginas, com numeração de passo embutida",
    )),
  )),
  ("Etapa 2 — 30 objetivas", (
    (none, (
      "Consolidação · Integração · Aplicação",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Modelo de resposta mecanístico",
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
    ("02", "C"),
    ("03", "B"),
    ("04", "C"),
    ("05", "C"),
    ("06", "C"),
    ("07", "B"),
    ("08", "C"),
    ("09", "ECEC"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "B"),
    ("13", "A"),
    ("14", "C"),
    ("15", "CCEC"),
    ("16", "A"),
    ("17", "D"),
    ("18", "B"),
    ("19", "A"),
    ("20", "E"),
    ("21", "B"),
    ("22", "B"),
    ("23", "CECC"),
    ("24", "C"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "B"),
    ("28", "A"),
    ("29", "D"),
    ("30", "A"),
  )),
))
