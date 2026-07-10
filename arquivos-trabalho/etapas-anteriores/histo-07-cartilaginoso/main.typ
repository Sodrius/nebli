// ================================================================
// MAIN.TYP -- histo-07-cartilaginoso | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Tecido cartilaginoso",
  "",
  (
    ("Disciplina", "Histologia (UC02)"),
    ("Onde estudar", "Junqueira & Carneiro cap. 7 + Ross & Pawlina cap. 7"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Identidade do tecido cartilaginoso", (
      "1.1 De onde vem e por que importa",
      "1.2 A marca registrada: avascular, abundante matriz",
      "1.3 Como um tecido sem vaso se alimenta",
      "1.4 O pericôndrio: bainha que nutre e renova",
      "1.5 Duas idades da mesma célula: condroblasto e condrócito",
    )),
    ("PARTE II — A matriz que define tudo", (
      "2.1 Por que a matriz é o tecido, não a célula",
      "2.2 Colágeno tipo II: a malha tensional",
      "2.3 Proteoglicanos e GAGs: a esponja que segura água",
      "2.4 Territórios da matriz: ler a lâmina",
    )),
    ("PARTE III — Tipos, crescimento e clínica", (
      "3.1 Dois jeitos de crescer: intersticial e aposicional",
      "3.2 Hialina, elástica e fibrosa: o mesmo princípio em três versões",
      "3.3 Onde cada uma aparece e por quê",
      "3.4 Por que cartilagem lesionada não cicatriza",
    )),
  )),
  ("Resumindo", (
    (none, (
      "Os pontos que precisam estar na ponta da língua",
    )),
  )),
  ("Etapa 2 — 30 objetivas", (
    (none, (
      "10 Consolidação · 15 Integração · 5 Aplicação",
    )),
  )),
  ("Etapa 3 — 5 discursivas", (
    (none, (
      "Mecanismo em até 100 palavras",
    )),
  )),
  ("Gabarito", (
    (none, (
      "Respostas da Etapa 2",
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
    ("02", "B"),
    ("03", "D"),
    ("04", "A"),
    ("05", "E"),
    ("06", "B"),
    ("07", "C"),
    ("08", "D"),
    ("09", "B"),
    ("10", "A"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "B"),
    ("13", "C"),
    ("14", "E"),
    ("15", "B"),
    ("16", "A"),
    ("17", "D"),
    ("18", "C"),
    ("19", "B"),
    ("20", "E"),
    ("21", "D"),
    ("22", "C"),
    ("23", "A"),
    ("24", "B"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "B"),
    ("28", "D"),
    ("29", "E"),
    ("30", "A"),
  )),
))
