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
  "Cadeia Respiratória e Fosforilação Oxidativa",
  "Bioquímica",
  (
    ("Disciplina", "Bioquímica — Metabolismo aeróbico, transporte de elétrons e síntese de ATP"),
    ("Nota de uso", "Leia a PARTE I devagar — entender a *lógica termodinâmica* (por que fracionar a queima) é o que faz o resto fazer sentido. Se travar na PARTE III com inibidores e desacopladores, volte para a figura do gradiente e da força próton-motriz; tudo decorre dela."),
    ("Onde estudar", "Lehninger 7ª ed., Cap. 19 (Fosforilação oxidativa) pp. 731–786 + Voet Cap. 22 (Transporte de elétrons e fosforilação oxidativa)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Por que existe uma cadeia", (
      "1.1 Da queima térmica ao fracionamento controlado",
      "1.2 Reações redox e potenciais",
      "1.3 Anatomia mitocondrial e os 6 atores",
    )),
    ("PARTE II — Os quatro complexos", (
      "2.1 Complexo I e Complexo II — duas portas de entrada",
      "2.2 CoQ, ciclo Q e Complexo III",
      "2.3 Citocromo c e Complexo IV",
    )),
    ("PARTE III — Acoplamento, ATP sintase e clínica", (
      "3.1 Teoria quimiosmótica e força próton-motriz",
      "3.2 ATP sintase F0F1 e binding change",
      "3.3 P/O, saldo final e lançadeiras",
      "3.4 Inibidores, desacopladores e quadros clínicos",
    )),
  )),
  ("Resumindo", (
    (none, (
      "Síntese de 1–2 páginas com os pontos-chave",
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
    ("01", "C"),
    ("02", "CCCE"),
    ("03", "D"),
    ("04", "B"),
    ("05", "CECC"),
    ("06", "A"),
    ("07", "E"),
    ("08", "CCEC"),
    ("09", "B"),
    ("10", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "CECC"),
    ("13", "A"),
    ("14", "D"),
    ("15", "CECC"),
    ("16", "B"),
    ("17", "CCEC"),
    ("18", "E"),
    ("19", "C"),
    ("20", "A"),
    ("21", "CCCE"),
    ("22", "D"),
    ("23", "CECE"),
    ("24", "B"),
    ("25", "E"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "D"),
    ("28", "B"),
    ("29", "E"),
    ("30", "A"),
  )),
))
