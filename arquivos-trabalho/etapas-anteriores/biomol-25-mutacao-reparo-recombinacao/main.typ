// ================================================================
// MAIN.TYP -- biomol-25-mutacao-reparo-recombinacao | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Mutação, reparo e DNA móvel",
  "Biologia Molecular",
  (
    ("Disciplina", "Biologia Molecular (UC02)"),
    ("Onde estudar", "Slides do Prof. PC · Lehninger cap. 25 (reparo do DNA) · Alberts cap. 5 (mecanismos de reparo e recombinação)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Mutação: o que muda e por que aparece", (
      "1.1 O que é mutação e os três tipos",
      "1.2 Mutações espontâneas e a fidelidade da replicação",
      "1.3 Mutações induzidas: química e radiação UV",
    )),
    ("PARTE II — Reparo: desfazer o erro antes que fixe", (
      "2.1 Reparo direto: fotoliase e MGMT",
      "2.2 Reparo por excisão de nucleotídeo",
      "2.3 Quando o reparo falha: xeroderma e SOS",
    )),
    ("PARTE III — DNA móvel e recombinação", (
      "3.1 Plasmídeos, fator F e conjugação",
      "3.2 Transposons: genes que saltam",
      "3.3 Vírus, fago lambda e recombinação sítio-específica",
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
    ("01", "B"),
    ("02", "C"),
    ("03", "EECCC"),
    ("04", "B"),
    ("05", "B"),
    ("06", "E"),
    ("07", "CEEEE"),
    ("08", "C"),
    ("09", "B"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "B"),
    ("12", "E"),
    ("13", "E"),
    ("14", "B"),
    ("15", "EEECE"),
    ("16", "C"),
    ("17", "D"),
    ("18", "D"),
    ("19", "D"),
    ("20", "A"),
    ("21", "E"),
    ("22", "EEECC"),
    ("23", "D"),
    ("24", "A"),
    ("25", "C"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "A"),
    ("28", "B"),
    ("29", "B"),
    ("30", "D"),
  )),
))
