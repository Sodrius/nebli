// ================================================================
// MAIN.TYP -- radiologia-01-ferramentas-diagnostico | Gerado por gerar_main.py
// ================================================================

#import "../../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Ferramentas do Diagnóstico Radiológico",
  "Radiologia — Métodos de Imagem",
  (
    ("Disciplina", "Radiologia (UC-03) — Preceptoria FMUSP"),
    ("Onde estudar", "Brant & Helms · Fundamentos de Radiologia (Herring) · ACR Appropriateness Criteria (acr.org) · Paul & Juhl — Interpretação Radiológica"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A pergunta clínica e as três físicas", (
      "1.1 A pergunta antes do exame",
      "1.2 Três físicas, quatro métodos",
      "1.3 Radiação ionizante ou não",
    )),
    ("PARTE II — Cada método por talento e cegueira", (
      "2.1 Ultrassom: imagem de ecos",
      "2.2 Tomografia: densidade em cinza",
      "2.3 Ressonância: sinal dos prótons",
      "2.4 Radiografia: sombra somada",
    )),
    ("PARTE III — Contraste, fases e prática", (
      "3.1 Meios de contraste",
      "3.2 Fases lidas no tempo",
      "3.3 Sequências que resolvem",
      "3.4 A física na decisão clínica",
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
    ("01", "A"),
    ("02", "B"),
    ("03", "ECCC"),
    ("04", "D"),
    ("05", "B"),
    ("06", "CECC"),
    ("07", "E"),
    ("08", "C"),
    ("09", "CCEC"),
    ("10", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "CCCE"),
    ("13", "A"),
    ("14", "C"),
    ("15", "CCEC"),
    ("16", "B"),
    ("17", "CECC"),
    ("18", "D"),
    ("19", "E"),
    ("20", "CCEE"),
    ("21", "E"),
    ("22", "D"),
    ("23", "B"),
    ("24", "E"),
    ("25", "ECCC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "A"),
    ("28", "CCEC"),
    ("29", "CCEC"),
    ("30", "D"),
  )),
))
