// ================================================================
// MAIN.TYP -- radiologia-02-principios-fisicos | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Física dos métodos de imagem",
  "Radiologia",
  (
    ("Disciplina", "Radiologia — Preceptoria FMUSP"),
    ("Onde estudar", "Brant & Helms — Fundamentos de Radiologia Diagnóstica · Herring — Radiologia Básica · Bushberg — The Essential Physics of Medical Imaging · Westbrook — MRI in Practice"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Radiografia: a sombra que soma tudo", (
      "1.1 O tubo e o feixe",
      "1.2 As cinco densidades",
      "1.3 Projeção e magnificação",
      "1.4 Silhueta e contraste",
      "1.5 Efeito biológico",
    )),
    ("PARTE II — Ultrassonografia: a imagem feita de ecos", (
      "2.1 Som, transdutor e eco",
      "2.2 Frequência contra penetração",
      "2.3 Descritores ecogênicos",
      "2.4 Sombra e reforço",
      "2.5 Corte, orientação e FAST",
    )),
    ("PARTE III — Tomografia: densidade que vira número", (
      "3.1 Do feixe ao helicoidal",
      "3.2 Voxel e reconstrução",
      "3.3 Unidades Hounsfield",
      "3.4 Janela e nível",
      "3.5 Contraste, fases e artefatos",
    )),
    ("PARTE IV — Ressonância: o sinal que o próton devolve", (
      "4.1 Por que hidrogênio",
      "4.2 Dentro do campo principal",
      "4.3 Precessão e radiofrequência",
      "4.4 T1 e T2",
      "4.5 Ponderação e gadolínio",
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
  ("Consolidação (Q01–Q08)", (
    ("01", "C"),
    ("02", "A"),
    ("03", "CECC"),
    ("04", "E"),
    ("05", "B"),
    ("06", "ECCE"),
    ("07", "D"),
    ("08", "CCEC"),
  )),
  ("Integração (Q09–Q25)", (
    ("09", "A"),
    ("10", "CEEC"),
    ("11", "E"),
    ("12", "C"),
    ("13", "ECCC"),
    ("14", "B"),
    ("15", "D"),
    ("16", "A"),
    ("17", "CCEE"),
    ("18", "E"),
    ("19", "C"),
    ("20", "EECC"),
    ("21", "B"),
    ("22", "D"),
    ("23", "ECEE"),
    ("24", "A"),
    ("25", "CEEE"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "E"),
    ("27", "C"),
    ("28", "CCCE"),
    ("29", "B"),
    ("30", "D"),
  )),
))
