// ================================================================
// MAIN.TYP -- imuno-17-reconhecimento-adaptativa | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Reconhecimento na resposta adaptativa",
  "Imunologia",
  (
    ("Disciplina", "Imunologia"),
    ("Onde estudar", "Abbas · Imunologia Celular e Molecular (10ª ed.), caps. 5 e 12 · Murphy · Janeway's Immunobiology (10ª ed.), caps. 4 e 5"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A resposta adquirida: o que é, onde mora, quem participa", (
      "1.1 Repertório sorteado e podado",
      "1.2 Reconhecimento composto: APC, T e B",
      "1.3 Especificidade, memória e transferência",
    )),
    ("PARTE II — O anticorpo: da mancha no gel à molécula em Y", (
      "2.1 Gama-globulina e eletroforese",
      "2.2 Mieloma e o paradoxo constante-variável",
      "2.3 Estrutura em Y, isotipos e alotipos",
    )),
    ("PARTE III — O que o anticorpo faz e de onde vem a diversidade", (
      "3.1 Sítio de ligação e funções do Fc",
      "3.2 Divisão de trabalho entre as classes",
      "3.3 Recombinação somática e TCR restrito",
    )),
  )),
))

// ======= ETAPA 1 =======
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
#set-etapa("Gabarito — Etapa 2")
#gabarito-page((
  ("Consolidação (Q01–Q10)", (
    ("01", "C"),
    ("02", "E"),
    ("03", "CEEC"),
    ("04", "A"),
    ("05", "ECCE"),
    ("06", "D"),
    ("07", "CCEE"),
    ("08", "B"),
    ("09", "EECC"),
    ("10", "E"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "C"),
    ("12", "A"),
    ("13", "CECC"),
    ("14", "D"),
    ("15", "E"),
    ("16", "ECEE"),
    ("17", "B"),
    ("18", "A"),
    ("19", "CCEC"),
    ("20", "D"),
    ("21", "C"),
    ("22", "EEEC"),
    ("23", "E"),
    ("24", "B"),
    ("25", "CEEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "A"),
    ("28", "ECCC"),
    ("29", "C"),
    ("30", "E"),
  )),
))
