// ================================================================
// MAIN.TYP -- imuno-01-reconhecimento-inato | pipeline e1-deck-v9
// Somente Etapa 1 + Resumindo (E2/E3/RemNote desligados no canônico).
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Reconhecimento inato no sistema imune",
  "Imunologia",
  (
    ("Disciplina", "Imunologia"),
    ("Onde estudar", "Abbas — Imunologia Celular e Molecular, cap. 4 · Janeway's Immunobiology, cap. 3"),
    ("Onde aprofundar", [
      • Takeuchi O, Akira S. _Pattern recognition receptors and inflammation._ Cell 140:805–820 (2010) \
      • Gay NJ et al. _Assembly and localization of Toll-like receptor signalling complexes._ Oncogene 14(8):546–58 (2014) \
      • Schroder K, Tschopp J. _The inflammasomes._ Cell 140(6):821–32 (2010)
    ]),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Os PRR e a perda da homeostasia", (
      "1.1 Repertório aleatório e seleção",
      "1.2 Tolerância ou resposta",
      "1.3 Reconhecimento hierárquico",
      "1.4 PAMP e DAMP",
      "1.5 Famílias de PRR e localização",
    )),
    ("PARTE II — Da ativação do receptor à decisão da célula", (
      "2.1 Como o TLR percebe o ligante",
      "2.2 MyD88 e TRIF",
      "2.3 AKT, caspase-8 e inflamassoma",
      "2.4 O inflamassoma e o priming",
    )),
    ("PARTE III — As quatro estratégias", (
      "3.1 Interferons do tipo I",
      "3.2 Citotoxicidade celular",
      "3.3 Fagocitose",
      "3.4 Mediadores e febre",
    )),
    ("PARTE IV — Citocinas e outros mediadores", (
      "4.1 O que é uma citocina",
      "4.2 Interleucinas, CSF e interferons",
      "4.3 Mediadores lipídicos e exossomos",
      "4.4 Plasticidade da resposta inata",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"
