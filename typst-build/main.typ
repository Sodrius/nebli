// ================================================================
// MAIN.TYP -- imuno-02-mecanismos-efetores | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Mecanismos efetores do sistema imune",
  "Imunologia",
  (
    ("Disciplina", "Imunologia"),
    ("Onde estudar", "Abbas — Imunologia Celular e Molecular, caps. 4, 6, 10 e 11 · Barbuto, Wastowski, Carneiro-Sampaio e Donadi — Imunologia Básica para o Clínico"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Reconhecer antes de agir", (
      "1.1 O arco do reconhecimento",
      "1.2 PAMPs, DAMPs e os três endereços do receptor",
      "1.3 NOD, inflamassoma e piroptose",
      "1.4 Citocinas, quimiocinas e a saída do vaso",
    )),
    ("PARTE II — Os efetores da imunidade inata", (
      "2.1 Barreiras e peptídeos antimicrobianos",
      "2.2 Fagocitose e opsonização",
      "2.3 Burst oxidativo e óxido nítrico",
      "2.4 O neutrófilo, do rolamento à NETose",
      "2.5 Células NK e citotoxicidade por anticorpo",
      "2.6 Macrófagos: um tipo, três programas",
    )),
    ("PARTE III — Os efetores da imunidade adaptativa", (
      "3.1 Do linfonodo aos três sinais",
      "3.2 Polarização do CD4: Th1, Th2, Th17",
      "3.3 O CD4 que reprograma o macrófago",
      "3.4 O linfócito T citotóxico",
      "3.5 Equilíbrio, homeostasia e memória",
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
    ("02", "CECC"),
    ("03", "A"),
    ("04", "D"),
    ("05", "ECCC"),
    ("06", "E"),
    ("07", "B"),
    ("08", "CCEC"),
    ("09", "D"),
    ("10", "EECC"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "E"),
    ("13", "CEEC"),
    ("14", "B"),
    ("15", "C"),
    ("16", "CCEE"),
    ("17", "E"),
    ("18", "A"),
    ("19", "CCCE"),
    ("20", "D"),
    ("21", "C"),
    ("22", "CEEE"),
    ("23", "B"),
    ("24", "E"),
    ("25", "EECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "D"),
    ("28", "ECEE"),
    ("29", "B"),
    ("30", "C"),
  )),
))
