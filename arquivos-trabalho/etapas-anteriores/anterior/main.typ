// ================================================================
// MAIN.TYP -- biomol-21-replicacao-dna | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Replicação do DNA",
  "Biologia Molecular",
  (
    ("Disciplina", "Biologia Molecular (UC01)"),
    ("Onde estudar", "Alberts cap. 6 · Lehninger cap. 25"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O problema que a célula resolve", (
      "1.1 A estrutura que tudo complica: antiparalelidade e 5'→3'",
      "1.2 A origem de replicação: oriC",
      "1.3 Abrindo a forquilha: helicase, SSB e girase",
    )),
    ("PARTE II — As polimerases: especialistas com papéis distintos", (
      "2.1 DNA-Pol I: a enzima de revisão e reparo",
      "2.2 Por que a polimerase precisa de primer",
      "2.3 DNA-Pol III: a máquina principal",
    )),
    ("PARTE III — A orquestra completa na forquilha", (
      "3.1 Fita líder e fita retardada",
      "3.2 Fragmentos de Okazaki: síntese e resolução",
      "3.3 DNA ligase: fechando o nick",
      "3.4 Eucariotos: mesma lógica, escala maior",
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
    ("03", "E"),
    ("04", "A"),
    ("05", "CEEC"),
    ("06", "D"),
    ("07", "B"),
    ("08", "ECCE"),
    ("09", "C"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "A"),
    ("12", "D"),
    ("13", "CEEC"),
    ("14", "C"),
    ("15", "B"),
    ("16", "ECCE"),
    ("17", "E"),
    ("18", "A"),
    ("19", "CEEC"),
    ("20", "D"),
    ("21", "B"),
    ("22", "ECCE"),
    ("23", "C"),
    ("24", "A"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "CEEC"),
    ("28", "B"),
    ("29", "E"),
    ("30", "A"),
  )),
))
