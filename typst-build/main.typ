// ================================================================
// MAIN.TYP -- imuno-07-inflamacao-inicio-resolucao | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Inflamação: início e resolução",
  "Imunologia",
  (
    ("Disciplina", "Imunologia"),
    ("Onde estudar", "Abbas — Imunologia Celular e Molecular (cap. 2 e 4) · Robbins — Patologia Básica (cap. 2) · Murphy — Janeway's Imunobiologia (cap. 2 e 3)"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Reconhecer o perigo antes de reagir", (
      "1.1 O que é, e o custo",
      "1.2 Padrões em três endereços",
      "1.4 Inflamassoma, IL-1β e piroptose",
    )),
    ("PARTE II — Abrir a barreira e trazer a célula", (
      "2.1 Sequência vascular e sinais",
      "2.3 Rolar, parar, atravessar",
      "2.4 Fagocitose e ordem de chegada",
    )),
    ("PARTE III — Mediadores, e quem manda parar", (
      "3.2 Fator XII e quatro cascatas",
      "3.4 Araquidônico e os fármacos",
      "3.6 Resolução é programa ativo",
    )),
  )),
  ("Etapa 2 — 30 objetivas", (
    (none, (
      "Consolidação (Q01–Q08) · Integração (Q09–Q25) · Aplicação (Q26–Q30)",
      "Múltipla escolha, certo/errado e assinale a incorreta",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Cinética · estase · inflamassoma · farmacologia · resolução",
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
  ("Consolidação (Q01–Q08)", (
    ("01", "C"),
    ("02", "A"),
    ("03", "CECC"),
    ("04", "D"),
    ("05", "ECCE"),
    ("06", "B"),
    ("07", "CCEC"),
    ("08", "E"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "C"),
    ("10", "CEEC"),
    ("11", "A"),
    ("12", "D"),
    ("13", "CCCE"),
    ("14", "C"),
    ("15", "B"),
    ("16", "ECCC"),
    ("17", "E"),
    ("18", "A"),
    ("19", "CCEE"),
    ("20", "D"),
    ("21", "C"),
    ("22", "EECC"),
    ("23", "A"),
    ("24", "D"),
    ("25", "CEEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "B"),
    ("27", "E"),
    ("28", "EECE"),
    ("29", "A"),
    ("30", "C"),
  )),
))
