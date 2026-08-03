// ================================================================
// MAIN.TYP -- pediatria-01-desenvolvimento-primeira-infancia | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Crescimento e Desenvolvimento na Primeira Infância",
  "Pediatria — Ciclo da Vida I",
  (
    ("Disciplina", "Pediatria — Ciclo da Vida I (UC-16)"),
    ("Onde estudar", "SBP · Tratado de Pediatria (6ª ed.) · Grisi · Desenvolvimento da Criança (Atheneu) · Escobar · A Promoção da Saúde na Infância (Manole)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O que é desenvolvimento e as lentes para enxergá-lo", (
      "1.1 Do adulto em miniatura à maturação",
      "1.2 As quatro lentes teóricas",
      "1.3 Definição e domínios do desenvolvimento",
    )),
    ("PARTE II — O motor biológico: cérebro plástico e a janela", (
      "2.1 Habilidades em camadas",
      "2.2 Plasticidade e a janela",
      "2.3 Gene, ambiente e experiência",
    )),
    ("PARTE III — Risco, estresse tóxico e o papel do pediatra", (
      "3.1 Fatores de risco",
      "3.2 Estresse tóxico e o eixo HPA",
      "3.3 Vigilância, triagem e o novo papel",
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
    ("02", "A"),
    ("03", "CCEE"),
    ("04", "D"),
    ("05", "B"),
    ("06", "E"),
    ("07", "CEEC"),
    ("08", "B"),
    ("09", "ECCE"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "D"),
    ("13", "CECE"),
    ("14", "B"),
    ("15", "CEEC"),
    ("16", "E"),
    ("17", "C"),
    ("18", "A"),
    ("19", "EECC"),
    ("20", "D"),
    ("21", "CCEE"),
    ("22", "B"),
    ("23", "CEEC"),
    ("24", "A"),
    ("25", "ECCE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "E"),
    ("28", "CECE"),
    ("29", "B"),
    ("30", "D"),
  )),
))
