// ================================================================
// MAIN.TYP -- biomol-05-operon-procariotos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Regulação gênica em procariotos",
  "Biologia Molecular",
  (
    ("Disciplina", "Biologia Molecular"),
    ("Onde estudar", "Watson, Baker, Bell, Gann, Levine & Losick — Molecular Biology of the Gene, 7ª ed., cap. 18 (Transcriptional Regulation in Prokaryotes), pgs. 615-635 · Alberts, Biologia Molecular da Célula, cap. Controle da Expressão Gênica (seção de procariotos) · Lehninger, Princípios de Bioquímica, cap. Regulação da Expressão Gênica (operon lac e trp)"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A lógica do operon", (
      "Por que a bactéria regula",
      "Operon e mRNA policistrônico",
      "Cis, trans e as peças do lac",
    )),
    ("PARTE II — Controle negativo", (
      "O repressor e o indutor",
      "X-Gal, IPTG e mutantes constitutivos",
      "Diploide parcial e alelos do lacI",
    )),
    ("PARTE III — Controle positivo", (
      "Promotor bacteriano e consenso",
      "CAP-cAMP como sensor de glicose",
      "Quatro estados, diauxia e o mapa geral",
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
    ("01", "A"),
    ("02", "A"),
    ("03", "CEEC"),
    ("04", "A"),
    ("05", "C"),
    ("06", "ECCE"),
    ("07", "B"),
    ("08", "C"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "C"),
    ("10", "E"),
    ("11", "B"),
    ("12", "CCEE"),
    ("13", "E"),
    ("14", "A"),
    ("15", "ECCE"),
    ("16", "E"),
    ("17", "B"),
    ("18", "CCEC"),
    ("19", "D"),
    ("20", "D"),
    ("21", "CECC"),
    ("22", "E"),
    ("23", "CCCE"),
    ("24", "C"),
    ("25", "EECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "CCEE"),
    ("28", "D"),
    ("29", "CEEC"),
    ("30", "E"),
  )),
))
