"""Inventário atômico da Correlação patológica-radiológica 2 (33 lâminas só imagem, vistas em 09/10; F-20261009-CLAUDE-02).
Fontes: lâminas (fontes/slides.pdf; scratchpad pr02-*.png), monitoria P1 'Aula 5 – Discussão Radio/Pato II' (fontes/monitoria-P1.txt
p. 54), Robbins cap. 18 (livros/robbins-cap18-figado.txt), E1 antiga NEBLI desta aula (fontes/e1-antiga.txt; fonte permitida pelo
CLAUDE.md, montada sobre estas lâminas). Para python3 -m nebli.inventario."""
PREFIXO = "pr02"
AULA = "Correlação patológica-radiológica 2 (UC03, fígado)"
EXC = "EXC: "
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Caso 1: mulher, 20 anos, assintomática", [("caso1", "Achado incidental em jovem assintomática", ["hemangioma-assintomatico", "hemangioma-mulheres"])]),
 (3, "conteudo", "US: nódulo hiperecogênico", [("us", "Nódulo hiperecogênico bem delimitado", "hemangioma-us")]),
 (4, "conteudo", "TC trifásica", [("tc", "Realce periférico globular e centrípeto (arterial, portal, equilíbrio)", "hemangioma-tc")]),
 (5, "conteudo", "Peça cirúrgica (fígado)", [("peca", "Hemangioma cavernoso no fígado", ["hemangioma-pele-figado", "hemangioma-cavernoso"])]),
 (6, "conteudo", "Fígado normal: macro e espaço porta", [("normal", "Fígado normal liso, marrom; espaço porta", "triade-portal")]),
 (7, "conteudo", "Histologia: zonas 1-2-3", [
   ("fluxo", "Sangue do espaço porta para a centrolobular", "fluxo-portal-central"),
   ("zonas", "Zona 3 centrolobular, mais vulnerável", ["zona-3", "zona-3-isquemia", "zona-3-alcool"])]),
 (8, "conteudo", "Macro do hemangioma", [("macro", "Lesão vinhosa, esponjosa, bem delimitada", "hemangioma-macro")]),
 (9, "conteudo", "Histologia do hemangioma", [("histo", "Espaços vasculares dilatados com hemácias", ["hemangioma-histologia", "hemangioma-biopsia"])]),
 (10, "conteudo", "Caso 2: 30 anos, dor abdominal, etilista e tabagista", [("caso2", "Álcool como causa de doença hepática", "alcool-causa")]),
 (11, "conteudo", "US: esteatose", [("us-esteatose", "Fígado mais brilhante que o rim", "esteatose-us")]),
 (12, "conteudo", "US: cirrose e nódulo", [("us-cirrose", "Bordas serrilhadas, ecotextura heterogênea; nódulo hipoecogênico", "us-cirrose")]),
 (13, "conteudo", "TC: tórax e fígado", [("tc-torax", "Aumento do diâmetro AP (enfisema)", "enfisema-tc"), ("tc-esteatose", "Fígado menos denso que o baço", "esteatose-tc")]),
 (14, "conteudo", "TC", [("tc14", "Progressão das alterações hepáticas", "esteatose-tc")]),
 (15, "conteudo", "TC", [("tc15", "Fígado heterogêneo, esplenomegalia", "hp-tc")]),
 (16, "conteudo", "TC", [("tc16", "Fígado nodular, ascite", "hp-tc")]),
 (17, "conteudo", "Peça: fígado gorduroso", [("esteatose", "Esteatose macrovesicular, fígado pesado e reversível", ["esteatose-macro", "esteatose-peso", "esteatose-reversivel"]), ("hepatite", "Hepatite alcoólica e acetaldeído", ["hepatite-alcoolica", "acetaldeido"])]),
 (18, "conteudo", "Cirrose micronodular", [("micro", "Superfície granular, nódulos < 3 mm", ["cirrose-definicao", "micro-macronodular"])]),
 (19, "conteudo", "Cirrose macronodular", [("macro", "Nódulos > 3 mm", "macronodular")]),
 (20, "conteudo", "Cirrose verde", [("verde", "Bile retida, icterícia", "cirrose-verde")]),
 (21, "conteudo", "Cirrose verde (detalhe)", [("verde2", "Nódulos impregnados de bile", "cirrose-verde")]),
 (22, "conteudo", "Histologia da cirrose", [("septos", "Septos fibrosos e nódulos; células estreladas", ["estreladas-tgfb", "estreladas-mec"])]),
 (23, "conteudo", "Reticulina", [("reticulina", "Reticulina delimita os nódulos", "reticulina")]),
 (24, "conteudo", "CHC em fígado cirrótico", [("chc", "Carcinoma hepatocelular sobre cirrose", ["chc-mais-comum", "chc-risco-cirrose", "chc-rastreio"])]),
 (25, "conteudo", "Vamos analisar este fígado (TC)", [("tc25", "TC do fígado cirrótico", "hp-tc")]),
 (26, "conteudo", "Sistema porta", [("porta", "Esplênica + mesentérica formam a porta", "sh-1790981519128")]),
 (27, "conteudo", "Colaterais portossistêmicas", [("colaterais", "Varizes esofágicas, cabeça de medusa, hemorroidárias", ["hp-shunts", "cabeca-medusa", "sh-1790981518578", "sh-1790981527126"])]),
 (28, "conteudo", "Hipertensão portal na TC", [("hp", "Cirrose causa hipertensão portal; ascite", ["hp-cirrose-causa", "hp-cirrose", "hp-ascite", "hp-tc"])]),
 (29, "conteudo", "TC: esplenomegalia", [("baco-tc", "Baço aumentado", "hp-esplenomegalia")]),
 (30, "conteudo", "Baço congesto", [("baco", "Esplenomegalia congestiva, hiperesplenismo", ["hp-esplenomegalia", "hp-plaquetas"])]),
 (31, "conteudo", "Varizes esofágicas", [("varizes", "Veias submucosas dilatadas; hematemese; causa de morte", ["varizes-terco-inferior", "varizes-hp", "varizes-hematemese", "varizes-morte"])]),
 (32, "capa", "Dúvidas", []),
 (33, "capa", "Encerramento", []),
]
CAPITULO = [("Robbins cap. 18", [("cirrose", "Cirrose: fibrose e nódulos; hipertensão portal", ["cirrose-definicao", "hp-cirrose"]), ("hemangioma", "Hemangioma cavernoso", "hemangioma-histologia")])]
EXERCICIOS = [("Monitoria P1, Aula 5 – Discussão Radio/Pato II", [
   ("m-hemangioma", "US hiperecogênico; TC realce periférico centrípeto; macro vinhoso; proliferação vascular", ["hemangioma-us", "hemangioma-tc", "hemangioma-macro", "hemangioma-histologia"]),
   ("m-us-cirrose", "US: bordas serrilhadas, heterogeneidade; nódulo hipoecogênico (CHC)", "us-cirrose"),
   ("m-tc", "TC: enfisema, varizes, esplenomegalia", ["enfisema-tc", "varizes-hp", "hp-esplenomegalia"]),
   ("m-macro", "Superfície granular; bile e icterícia", ["cirrose-definicao", "cirrose-verde"])])]
