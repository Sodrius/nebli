// ================================================================
// MAIN.TYP -- anato-05-sistema-linfatico | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Sistema Linfático",
  "Anatomia",
  (
    ("Disciplina", "Anatomia (UC02)"),
    ("Onde estudar", "Slide da Profa. Katiúcia B. S. Paiva (Aula 5 — Sistema Circulatório e Linfático I, Parte 2) · Moore, Anatomia Orientada para a Clínica (sistema linfático) · Netter, Atlas de Anatomia Humana (linfáticos do tronco)"),
    ("Onde aprofundar", [
      #set text(size: 7.3pt)
      #set par(leading: 0.55em, justify: false, first-line-indent: 0em, hanging-indent: 0.9em)
      #text(fill: navy, weight: "bold", "• ") *Assistir/ler* — Ninja Nerd (Lymphatic System: anatomy & physiology) · Boards & Beyond (Immunology › Lymphoid Organs) · Acland's Video Atlas (linfáticos do tronco) · Sketchy: cobre pouca anatomia macro (foco em imuno/patologia) · Pathoma: não cobre (é patologia) \
      #text(fill: navy, weight: "bold", "• ") *Dessuspender no AnKing v12* (decks sob \#AK\_​Step1\_​v12::​) — ordenados por completude; dessuspenda de cima pra baixo: \
      #text(fill: navy, weight: "bold", "• ") *Cobre melhor* · \#FirstAid::​02\_​Immunology::​01\_​Lymphoid\_​Structures::​03\_​Lymphatic\_​drainage\_​associations — 26 cards (cadeias e territórios de drenagem) \
      #text(fill: navy, weight: "bold", "• ") *Cobre melhor* · \#FirstAid::​02\_​Immunology::​01\_​Lymphoid\_​Structures::​02\_​Lymph\_​node — 16 cards (córtex, paracórtex, medula, folículo) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#Bootcamp::​Immunology::​01\_​Lymphoid\_​Tissue::​03\_​Lymph\_​Nodes — 23 cards (estrutura e fluxo do linfonodo) \
      #text(fill: navy, weight: "bold", "• ") *Complementa* · \#FirstAid::​02\_​Immunology::​01\_​Lymphoid\_​Structures::​04\_​Spleen — 10 cards (baço, polpa branca/vermelha) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#Bootcamp::​Immunology::​01\_​Lymphoid\_​Tissue::​01\_​Primary\_​Lymphoid\_​Tissue — 16 cards (medula óssea e timo) \
      #text(fill: navy, weight: "bold", "• ") *Mais distante* · \#FirstAid::​02\_​Immunology::​01\_​Lymphoid\_​Structures::​05\_​Thymus — 4 cards (timo, órgão primário)
    ]),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A rede que recolhe o que o sangue deixa para trás", (
      "As três tarefas do sistema linfático",
      "Os elementos e de onde vem a linfa",
      "O capilar linfático: a porta de mão única",
    )),
    ("PARTE II — Onde os linfócitos nascem, amadurecem e trabalham", (
      "Órgãos primários: medula óssea e timo",
      "O linfonodo por dentro: por que é um filtro",
      "As cadeias regionais e o baço",
      "O tecido linfoide das mucosas",
    )),
    ("PARTE III — Como a linfa volta ao sangue sem um coração", (
      "A linfa sobe sem bomba central",
      "Dos capilares aos troncos: a convergência",
      "Ductos, cisterna do quilo e o retorno à veia",
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
    ("02", "CCEE"),
    ("03", "A"),
    ("04", "D"),
    ("05", "ECCE"),
    ("06", "B"),
    ("07", "E"),
    ("08", "CEEC"),
    ("09", "C"),
    ("10", "B"),
  )),
  ("Integração (Q11–Q25)", (
    ("11", "CEEC"),
    ("12", "D"),
    ("13", "A"),
    ("14", "EECC"),
    ("15", "B"),
    ("16", "C"),
    ("17", "CCEE"),
    ("18", "B"),
    ("19", "D"),
    ("20", "CCEE"),
    ("21", "A"),
    ("22", "E"),
    ("23", "ECCE"),
    ("24", "C"),
    ("25", "B"),
  )),
  ("Aplicação (Q26–Q30)", (
    ("26", "D"),
    ("27", "A"),
    ("28", "CEEC"),
    ("29", "E"),
    ("30", "CCEE"),
  )),
))
