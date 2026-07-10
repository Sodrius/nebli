// ================================================================
// MAIN.TYP -- diferenciacao-celular | Gerado por gerar_main.py
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
  "Diferenciação Celular",
  "Biologia Celular",
  (
    ("Disciplina", "Biologia Celular — Identidade e potencialidade celular"),
    ("Nota de uso", "Leia a PARTE I devagar — a escala potencialidade × diferenciação é o eixo invertido que apoia tudo. Se travar na PARTE III (4 mecanismos epigenéticos), volte e reancore: o ponto é manter padrão SEM mexer no DNA. O Resumindo só faz sentido depois das três PARTES."),
    ("Onde estudar", "Alberts 5ª ed., Cap. 7 (Controle da expressão gênica) + Cap. 23 (Células-tronco e renovação); Junqueira & Carneiro 10ª ed. (capítulos de hematopoese e epiderme)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O que é diferenciação", (
      "1.1 Especialização: a célula que faz uma coisa muito bem",
      "1.2 Do zigoto aos folhetos",
      "1.3 Potencialidade × diferenciação: a inversa",
      "1.4 Sinais que toda célula animal precisa",
    )),
    ("PARTE II — Célula-tronco", (
      "2.1 Duas propriedades que definem",
      "2.2 Três classes de potencialidade",
      "2.3 Divisão assimétrica",
      "2.4 Renovação tecidual no adulto",
    )),
    ("PARTE III — Como o destino é controlado", (
      "3.1 Mesmos genes, leituras diferentes",
      "3.2 Controle combinatorial",
      "3.3 Herança epigenética: a definição",
      "3.4 Os quatro mecanismos",
      "3.5 iPS e medicina regenerativa",
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
    ("01", "B"),
    ("02", "CCCE"),
    ("03", "C"),
    ("04", "C"),
    ("05", "CCEC"),
    ("06", "B"),
    ("07", "B"),
    ("08", "CECC"),
    ("09", "B"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "CCEC"),
    ("13", "E"),
    ("14", "A"),
    ("15", "CCEE"),
    ("16", "C"),
    ("17", "CCEC"),
    ("18", "D"),
    ("19", "A"),
    ("20", "C"),
    ("21", "CCEC"),
    ("22", "D"),
    ("23", "CCCC"),
    ("24", "A"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "C"),
    ("28", "A"),
    ("29", "E"),
    ("30", "C"),
  )),
))
