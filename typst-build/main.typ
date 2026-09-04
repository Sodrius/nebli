// ================================================================
// MAIN.TYP -- pat-07-inflamacao-aguda | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Inflamação aguda",
  "Patologia geral",
  (
    ("Disciplina", "Patologia geral"),
    ("Onde estudar", "Robbins & Cotran, Patologia — Bases Patológicas das Doenças, capítulo Inflamação e Reparo, § Inflamação aguda · Robbins, Patologia Básica, capítulo 3"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O gatilho: reconhecer o dano e abrir o vaso", (
      "1.1 Definição, sinais e desencadeantes",
      "1.2 Reconhecimento, receptores e inflamassoma",
      "1.3 Fluxo, calibre, estase e mediadores",
    )),
    ("PARTE II — Do plasma às células: exsudato e recrutamento", (
      "2.1 Os quatro mecanismos de permeabilidade",
      "2.2 Exsudato, transudato e linfáticos",
      "2.3 Rolamento, adesão e diapedese",
      "2.4 Quimiotaxia e citocinas do recrutamento",
    )),
    ("PARTE III — Executar, desligar e a marca que fica", (
      "3.1 Fagocitose, burst oxidativo e dano",
      "3.2 Cinética, desligamento e desfechos",
      "3.3 Padrões morfológicos e seus porquês",
    )),
  )),
  ("Etapa 2 — 30 questões objetivas", (
    (none, (
      "Consolidação, integração e aplicação",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Mecanismo, líquido, padrão morfológico e alvo",
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
    ("01", "C"),
    ("02", "CCEC"),
    ("03", "CECE"),
    ("04", "E"),
    ("05", "B"),
    ("06", "A"),
    ("07", "CCEE"),
    ("08", "D"),
    ("09", "D"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "CEEC"),
    ("13", "E"),
    ("14", "B"),
    ("15", "CECC"),
    ("16", "E"),
    ("17", "D"),
    ("18", "B"),
    ("19", "ECEC"),
    ("20", "CCCE"),
    ("21", "CCEC"),
    ("22", "A"),
    ("23", "D"),
    ("24", "CECC"),
    ("25", "A"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "E"),
    ("28", "CCEC"),
    ("29", "B"),
    ("30", "D"),
  )),
))
