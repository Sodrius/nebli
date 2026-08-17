// ================================================================
// MAIN.TYP -- pato-01-lesao-celular-i
// ================================================================

#import "../../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Lesão Celular — Mecanismos de Lesão",
  "Patologia",
  (
    ("Disciplina", "Patologia — Departamento de Patologia, FMUSP"),
    ("Onde estudar", "Robbins & Cotran · Patologia — Bases Patológicas das Doenças, cap. Lesão e Morte Celular"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Do equilíbrio ao ponto sem retorno", (
      "1.1 A célula normal e as três saídas possíveis",
      "1.2 O que decide entre adaptar-se e lesar-se",
      "1.3 Lesão reversível e lesão irreversível",
      "1.4 As causas de lesão celular",
    )),
    ("PARTE II — O que se enxerga, e quando se enxerga", (
      "2.1 A ordem em que os achados aparecem",
      "2.2 A morfologia da lesão reversível",
      "2.3 O túbulo renal como caso de leitura",
      "2.4 Os dois critérios de irreversibilidade",
      "2.5 A enzima intracelular no sangue",
    )),
    ("PARTE III — Os mecanismos que empurram a célula", (
      "3.1 Os quatro alvos da agressão",
      "3.2 A queda de ATP e a cascata isquêmica",
      "3.3 Radicais livres: produção, defesas e alvos",
      "3.4 A lesão de reperfusão",
      "3.5 Dano mitocondrial: duas saídas para duas mortes",
      "3.6 O cálcio como amplificador da lesão",
      "3.7 O dano de membrana como ponto de convergência",
      "3.8 Uma rota à parte: proteínas mal dobradas e dano ao DNA",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"
