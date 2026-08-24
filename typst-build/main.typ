// ================================================================
// MAIN.TYP -- fisio-tgi-01-motilidade | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Motilidade do Tubo Digestório",
  "Fisiologia do Sistema Digestório",
  (
    ("Disciplina", "Fisiologia — Sistema Digestório"),
    ("Onde estudar", "Berne & Levy · Fisiologia (7ª ed.), cap. 26 · Guyton & Hall · Tratado de Fisiologia Médica (14ª ed.), cap. 63 · Koeppen & Stanton · Berne and Levy Physiology (6ª ed.), Fig. 9-17 e 27-2 · Barrett · Ganong Fisiologia Médica (26ª ed.), cap. 25"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A parede que se move", (
      "1.1 Esquelético nas pontas, liso no meio",
      "1.2 Circular estreita, longitudinal encurta",
      "1.3 Contração fásica e contração tônica",
      "1.4 Esfíncteres — tônus que vira porta",
    )),
    ("PARTE II — Quem dá as ordens", (
      "2.1 Plexos mioentérico e submucoso",
      "2.2 Reflexo curto, resolvido na parede",
      "2.3 Reflexo longo vago-vagal",
      "2.4 Acetilcolina, VIP e óxido nítrico",
    )),
    ("PARTE III — Do nervo à força", (
      "3.1 Junção neuroefetora sem placa motora",
      "3.2 Cálcio, calmodulina e MLCK",
      "3.3 Relaxamento por miosina fosfatase",
      "3.4 Sensibilização ao cálcio via RhoA",
    )),
  )),
))

// ======= ETAPA 1 =======
#set-etapa("Etapa 1 — Texto didático")
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#set-etapa("Resumindo")
#include "resumindo.typ"

// ======= ETAPA 2 =======
#set-etapa("Etapa 2 — 30 objetivas")
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#set-etapa("Etapa 3 — 5 discursivas")
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "B"),
    ("02", "CECC"),
    ("03", "C"),
    ("04", "CECC"),
    ("05", "A"),
    ("06", "E"),
    ("07", "E"),
    ("08", "E"),
    ("09", "D"),
    ("10", "EECC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "CCEC"),
    ("12", "A"),
    ("13", "EECC"),
    ("14", "C"),
    ("15", "A"),
    ("16", "C"),
    ("17", "D"),
    ("18", "EEEC"),
    ("19", "E"),
    ("20", "ECCE"),
    ("21", "A"),
    ("22", "A"),
    ("23", "D"),
    ("24", "EEEC"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "ECEE"),
    ("27", "D"),
    ("28", "D"),
    ("29", "E"),
    ("30", "CCEC"),
  )),
))
