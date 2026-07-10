// ================================================================
// MAIN.TYP -- bioq-21-lipideos-rotas | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Metabolismo de Lipídeos",
  "",
  (
    ("Disciplina", "Bioquímica (UC02)"),
    ("Onde estudar", "Slides da Profa. Déborah (IQ-USP) · Lehninger cap. 17 (oxidação de ácidos graxos) + cap. 21 (biossíntese de lipídios) · Stryer cap. 22"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Da gordura estocada ao acetil-CoA: a β-oxidação", (
      "1.1 Por que o corpo guarda energia como gordura, e não como açúcar",
      "1.2 Mobilização: como o adipócito libera o ácido graxo no sangue",
      "1.3 A entrada na mitocôndria: ativação e a lançadeira da carnitina",
      "1.4 A β-oxidação: cortar o ácido graxo de dois em dois carbonos",
    )),
    ("PARTE II — A conta da energia e o destino do acetil-CoA", (
      "2.1 Quanto ATP rende oxidar um palmitato (16 carbonos)",
      "2.2 Por que a gordura rende muito mais que a glicose",
      "2.3 Quando o acetil-CoA não cabe no Krebs: os corpos cetônicos",
    )),
    ("PARTE III — Construir em vez de queimar: síntese e regulação", (
      "3.1 Onde e quando o corpo fabrica ácido graxo",
      "3.2 A lançadeira do citrato e o passo comprometido (malonil-CoA)",
      "3.3 A sintase de ácidos graxos e a montagem do palmitato",
      "3.4 A regulação recíproca: insulina liga uma via e desliga a outra",
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
    ("02", "CCEE"),
    ("03", "D"),
    ("04", "A"),
    ("05", "ECCE"),
    ("06", "C"),
    ("07", "CEEC"),
    ("08", "D"),
  )),
  ("Integração (Q11–Q25)", (
    ("09", "A"),
    ("10", "E"),
    ("11", "EECC"),
    ("12", "C"),
    ("13", "E"),
    ("14", "CECC"),
    ("15", "B"),
    ("16", "A"),
    ("17", "ECEC"),
    ("18", "D"),
    ("19", "C"),
    ("20", "E"),
    ("21", "CCEC"),
    ("22", "A"),
    ("23", "E"),
    ("24", "EECE"),
    ("25", "D"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "C"),
    ("27", "CEEC"),
    ("28", "E"),
    ("29", "A"),
    ("30", "ECCE"),
  )),
))
