// ================================================================
// MAIN.TYP -- pat-05-edema-congestao | Gerado por gerar_main.py
// ================================================================

#import "../../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Edema e congestão",
  "Patologia",
  (
    ("Disciplina", "Patologia"),
    ("Onde estudar", "Slides da aula (Prof. Luiz Fernando Ferraz da Silva) · Robbins & Cotran, Patologia — capítulo de Distúrbios hemodinâmicos, seções de edema e congestão"),
  ),
)

// ======= ANTES DA AULA =======
#include "pre-aula.typ"

// ======= SUMÁRIO =======
#sumario((
  ("Texto didático", (
    ("PARTE I — O balanço que mantém o líquido no lugar", (
      "1.1 Edema, hiperemia e congestão",
      "1.2 As forças de Starling e o dreno linfático",
      "1.3 Transudato, exsudato e o nome das coleções",
    )),
    ("PARTE II — As maneiras de romper o balanço", (
      "2.1 Pressão hidrostática e insuficiência cardíaca",
      "2.2 Pressão oncótica baixa e retenção de sódio",
      "2.3 Linfa obstruída e parede permeável",
    )),
    ("PARTE III — O que o patologista vê", (
      "3.1 A morfologia do edema e da congestão",
      "3.2 O fígado: noz-moscada e a ascite da cirrose",
      "3.3 O pulmão: edema hemodinâmico e dano alveolar difuso",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"

