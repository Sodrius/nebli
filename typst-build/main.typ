// ================================================================
// MAIN.TYP -- micro-05-antibioticos-resistencia | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Antibióticos e resistência bacteriana",
  "Do alvo molecular ao laudo do antibiograma",
  (
    ("Disciplina", "Microbiologia"),
    ("Onde estudar", "Murray, Microbiologia Médica — capítulos de agentes antibacterianos e de mecanismos de resistência · Levinson, Microbiologia Médica e Imunologia — antimicrobianos, testes de suscetibilidade e antibiograma"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — O alvo seletivo", (
      "1.1 Toxicidade seletiva e os quatro alvos",
      "1.2 A parede: β-lactâmicos e glicopeptídeos",
      "1.3 Ribossomo, ácidos nucleicos e membrana",
    )),
    ("PARTE II — Matar, parar e escapar", (
      "2.1 Bacteriostático × bactericida",
      "2.2 As cinco saídas da resistência",
      "2.3 O padrão do laudo como assinatura",
    )),
    ("PARTE III — O laboratório decide", (
      "3.1 A CIM e como se chega ao número",
      "3.2 Difusão em disco e o halo",
      "3.3 De S/I/R à escolha do fármaco",
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
    ("01", "D"),
    ("02", "CCEE"),
    ("03", "C"),
    ("04", "ECCE"),
    ("05", "A"),
    ("06", "A"),
    ("07", "E"),
    ("08", "B"),
    ("09", "CCEC"),
    ("10", "C"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "EECC"),
    ("13", "E"),
    ("14", "D"),
    ("15", "CEEC"),
    ("16", "A"),
    ("17", "B"),
    ("18", "ECEE"),
    ("19", "D"),
    ("20", "C"),
    ("21", "CEEE"),
    ("22", "A"),
    ("23", "E"),
    ("24", "EECE"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "CECC"),
    ("28", "A"),
    ("29", "C"),
    ("30", "ECCE"),
  )),
))
