// ================================================================
// MAIN.TYP -- bioq-10-acao-hormonal | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Ação hormonal",
  "Bioquímica e Biologia Molecular",
  (
    ("Disciplina", "Bioquímica e Biologia Molecular"),
    ("Onde estudar", "Lehninger — Princípios de Bioquímica, cap. 12 (sinalização) e cap. 23 (regulação hormonal do metabolismo)"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Do sinal ao segundo mensageiro", (
      "1.1 Três velocidades de regulação",
      "1.2 O que define um hormônio",
      "1.3 Sete pontos de regulação",
      "1.4 Solubilidade e endereço do receptor",
      "1.5 A cascata do AMPc",
    )),
    ("PARTE II — Insulina e glucagon: o interruptor recíproco", (
      "2.1 Processamento da pré-pró-insulina",
      "2.2 A célula beta como sensor de glicemia",
      "2.3 Farmacologia do canal de potássio",
      "2.4 Glucagon, o hormônio da escassez",
      "2.5 Fosforilase e sintase em espelho",
      "2.6 Desligar também é ativo",
    )),
    ("PARTE III — Catecolaminas, tireoidianos e esteroides", (
      "3.1 Catecolaminas e o mesmo sinal em dois tecidos",
      "3.2 Hormônios tireoidianos e o gasto basal",
      "3.3 Esteroides: receptor nuclear e resposta lenta",
      "3.4 Quando o eixo quebra",
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
    ("01", "E"),
    ("02", "EECE"),
    ("03", "A"),
    ("04", "C"),
    ("05", "ECCE"),
    ("06", "E"),
    ("07", "B"),
    ("08", "A"),
    ("09", "EEEC"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "D"),
    ("12", "EEEC"),
    ("13", "B"),
    ("14", "E"),
    ("15", "A"),
    ("16", "CCEE"),
    ("17", "D"),
    ("18", "B"),
    ("19", "CCCE"),
    ("20", "E"),
    ("21", "A"),
    ("22", "ECCC"),
    ("23", "D"),
    ("24", "C"),
    ("25", "EECC"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "A"),
    ("27", "CECC"),
    ("28", "D"),
    ("29", "D"),
    ("30", "CECC"),
  )),
))
