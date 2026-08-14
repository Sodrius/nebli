// ================================================================
// MAIN.TYP -- pato-01-lesao-e-morte-celular
// Modo canônico e1-deck-v11: generate_e1=true, generate_e2=false,
// generate_e3=false. Só Etapa 1 + Resumindo.
// ================================================================

#import "../../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Lesão e morte celular",
  "Patologia",
  (
    ("Disciplina", "Patologia"),
    ("Onde estudar", "Robbins, Patologia — Bases Patológicas das Doenças, capítulo de lesão celular, morte celular e adaptações"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Da homeostase à morte: o mapa da resposta celular", (
      "1.1 Homeostase, estresse e as três saídas possíveis",
      "1.2 As causas que tiram a célula do equilíbrio",
      "1.3 A ordem em que o dano aparece",
      "1.4 O que se vê na lesão reversível",
      "1.5 Os dois critérios de irreversibilidade",
      "1.6 Enzima intracelular no sangue: a leitura clínica da irreversibilidade",
    )),
    ("PARTE II — Os mecanismos bioquímicos da lesão", (
      "2.1 Quatro alvos, um mesmo desfecho",
      "2.2 Queda de ATP: a cascata da isquemia",
      "2.3 Radicais livres: produção, defesa e alvos",
      "2.4 Lesão de reperfusão",
      "2.5 A mitocôndria decide entre necrose e apoptose",
      "2.6 Cálcio citosólico: o amplificador",
      "2.7 Dano de membrana: onde tudo converge",
      "2.8 Dobramento anômalo de proteínas e dano direto ao DNA",
    )),
    ("PARTE III — Necrose: a morte com digestão e inflamação", (
      "3.1 O que é necrose e como ela difere da apoptose",
      "3.2 A cadeia da necrose e a diferença entre célula e arcabouço",
      "3.3 Morfologia da necrose",
      "3.4 Os tipos de necrose",
    )),
    ("PARTE IV — Apoptose, comparação e necroptose", (
      "4.1 Por que existe uma morte celular programada",
      "4.2 As quatro etapas do programa",
      "4.3 A via intrínseca, ou mitocondrial",
      "4.4 A via extrínseca, ou dos receptores de morte",
      "4.5 A morfologia da apoptose",
      "4.6 Necrose e apoptose lado a lado",
      "4.7 Quando a apoptose falta e quando sobra",
      "4.8 Necroptose, a fronteira entre os dois mundos",
    )),
  )),
  ("Resumindo", (
    (none, (
      "Cápsulas de fechamento da Etapa 1",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"
