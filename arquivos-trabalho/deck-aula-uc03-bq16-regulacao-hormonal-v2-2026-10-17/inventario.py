"""Inventário atômico de Regulação hormonal do metabolismo e da massa corpórea (UC03 P1; Bioquímica; Profa. Deborah Schechtman), escrito
ANTES de escolher cards (17/10, pipeline v4). Sequência = 62 lâminas (fontes/slides.pdf = turma I 39 + II 23; a pasta pessoal tem só a
parte I, mesmo texto), vistas inteiras nesta sessão (io/g0..g5). Lido nesta sessão: transcrição integral (28 pp.), provas biomol-03
(4 itens), apostila guia de Biologia Molecular (seção da aula), apostila UC3, apostila de exercícios, Lehninger cap. 23 (massa corporal,
leptina, AMPK, adiponectina). Atenção: a transcrição troca “diminui a insulinemia” por “aumenta os níveis de insulina” na parabiose —
seguidas as lâminas (Coleman 1969: insulina cai).
A parte II (lâminas 40–62) repete a parte I (cascata, estresse, lipostática, leptina, parabiose, apetite) e acrescenta AMPK.
Fronteira (MEMORY §3): eixo hipotálamo-hipófise, estresse e receptores são da 10 (Ação hormonal); resistência à insulina e inflamação do
tecido adiposo têm cópias vivas no GR2 e na Integração metabólica → sh(); grelina e GLP-1 têm cópias na UC08 → sh().
"""
PREFIXO = "bq16"
AULA = "Regulação hormonal do metabolismo e da massa corpórea (UC03 P1; Bioquímica)"
EXC = "EXC: "
_10 = EXC + "eixo neuroendócrino e estresse: conteúdo da aula 10 (Ação hormonal), revisão"
_VID = EXC + "link de vídeo"
_R = "repete a parte I"

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Homeostasia: manter estoque de energia adequado, não excessivo", [("a1", "Homeostasia energética", "au-lipostatica")]),
 (3, "conteudo", "Tabela de IMC; doenças da obesidade", [("a2", "IMC ≥ 25 sobrepeso, ≥ 30 obesidade", "ak-imc")]),
 (4, "conteudo", "Cascata hormonal (frio → TRH → TSH → T3/T4)", [("a3", "Cascata", _10)]),
 (5, "conteudo", "Hipófise e hormônios; sistema neuroendócrino", [("a4", "Hipófise", _10)]),
 (6, "conteudo", "Estresse curto (adrenalina) × prolongado (cortisol)", [("a5", "Estresse", _10)]),
 (7, "conteudo", "Sistema neuroendócrino: alvos primários, secundários e finais", [("a6", "Sistema neuroendócrino", _10)]),
 (8, "conteudo", "Doenças endócrinas: hipo, hiper, tumores", [("a7", "Classificação", EXC + "lista de doenças sem mecanismo; cada uma tem aula própria")]),
 (9, "logistica", "Regulação hormonal da massa corpórea", []),
 (10, "conteudo", "Como sabemos quando comer e parar?", [("a8", "Fome e saciedade", ["ak-lateral-fome", "ak-vmh-saciedade"])]),
 (11, "conteudo", "Homeostase calórica: teoria lipostática", [("a9", "Teoria lipostática", "au-lipostatica")]),
 (12, "conteudo", "Por que a obesidade aumenta: estoque, recompensa, genética, microbiota", [("a10", "Endocanabinoides e recompensa", "ak-endocanabinoides")]),
 (13, "conteudo", "Vídeo", [("a11", "Vídeo", _VID)]),
 (14, "conteudo", "Doenças relacionadas à obesidade", [("a12", "Riscos", ["ak-sm-riscos", "ak-obesidade-ri"])]),
 (15, "conteudo", "Excesso calórico → TAG → resistência à insulina → síndrome metabólica",
  [("a13", "Síndrome metabólica", ["ak-sm-criterios", "ak-sm-x", "ak-sm-familia", "sh-1791054012972"])]),
 (16, "conteudo", "Resistência à insulina: fígado, músculo, gordura", [("a14", "Obesidade e receptores de insulina", ["sh-1791054012719", "ak-tg-ffa-insulina"])]),
 (17, "conteudo", "Obesidade → inflamação (macrófagos, TNF-α, IL-6, ↓ adiponectina) → disfunção endotelial",
  [("a15", "Inflamação do tecido adiposo", ["sh-1791593465414", "sh-1791593465568", "sh-1791054013396"])]),
 (18, "conteudo", "Estresse energético: DAG, ceramida, serina-quinases bloqueiam o receptor de insulina",
  [("a16", "Lipotoxicidade", ["ak-tg-ffa-insulina", "sh-1791054013222"])]),
 (19, "logistica", "Como o organismo mantém o controle lipídico?", []),
 (20, "conteudo", "Teoria lipostática com leptina", [("a17", "Leptina sinaliza o estoque", ["au-lipostatica", "ak-leptina"])]),
 (21, "logistica", "Hormônios secretados pelo tecido adiposo", []),
 (22, "conteudo", "Leptina, produto do gene OB; camundongo ob/ob", [("a18", "ob/ob", "au-ob")]),
 (23, "conteudo", "Parabiose ob/db", [("a19", "Parabiose", ["au-ob", "au-db"])]),
 (24, "conteudo", "Resultados da parabiose (Coleman)", [("a20", "db/db sem receptor", "au-db")]),
 (25, "conteudo", "Leptina: solução para a obesidade? Obesos têm excesso de leptina", [("a21", "Resistência à leptina", ["au-resistencia-leptina", "ak-leptina-obesos"])]),
 (26, "conteudo", "Leptina: efeitos periféricos (simpático, β3, UCP)", [("a22", "Termogênese", "sh-1791647352594")]),
 (27, "conteudo", "Adiponectina: menor nos obesos, ativa AMPK, inibe ACC", [("a23", "Adiponectina", ["au-adiponectina", "ak-pparg-adiponectina"])]),
 (28, "conteudo", "Adiponectina: efeitos em endotélio, macrófagos, fígado", [("a24", "Efeitos", "au-adiponectina")]),
 (29, "conteudo", "Saciedade: peptídeos gastrointestinais (CCK, GLP-1, grelina)",
  [("a25", "GLP-1", ["sh-1791054014570", "sh-1791052302525"]), ("a26", "Grelina estimula o apetite", "sh-1790979869860")]),
 (30, "conteudo", "Vídeo", [("a27", "Vídeo", _VID)]),
 (31, "conteudo", "Controle neural do apetite: leptina × grelina",
  [("a28", "Grelina no jejum", ["ak-grelina-jejum", "ak-grelina-sono", "ak-prader", "ak-bypass"]), ("a29", "Leptina e sono", "ak-leptina-sono")]),
 (32, "conteudo", "Núcleo arqueado: NPY/AgRP × POMC/CART; MCH lateral",
  [("a30", "POMC/CART → α-MSH", ["au-arqueado", "ak-pomc"]), ("a31", "NPY/AgRP → fome", "au-agrp")]),
 (33, "conteudo", "Mais leptina inibe NPY/AgRP e ativa POMC", [("a32", "Leptina no arqueado", ["au-arqueado", "ak-vmh-leptina", "ak-lateral-leptina"])]),
 (34, "conteudo", "Controle neural do apetite (MC4R)", [("a33", "MC4R", "au-arqueado")]),
 (35, "conteudo", "Optogenética", [("a34", "Optogenética", "au-arqueado")]),
 (36, "conteudo", "Estímulo de terminais GABAérgicos DMH sobre AgRP", [("a35", "Circuito AgRP", "au-agrp")]),
 (37, "conteudo", "Vídeo", [("a36", "Vídeo", _VID)]),
 (38, "conteudo", "Novos fármacos: Ozempic, Wegovy, Mounjaro",
  [("a37", "Agonistas de GLP-1", ["ak-glp1-exemplos", "ak-glp1-glucagon-esvaziamento"])]),
 (39, "logistica", "Bibliografia (Lehninger, Stryer)", []),
 (40, "conteudo", "Cascata hormonal (parte II)", [("a38", "Cascata", _10)]),
 (41, "conteudo", "Neuroendócrino (parte II)", [("a39", "Hipófise", _10)]),
 (42, "conteudo", "Estresse com efeitos de adrenalina e cortisol", [("a40", "Estresse", _10)]),
 (43, "conteudo", "Neuroendócrino figura (parte II)", [("a41", "Neuroendócrino", _10)]),
 (44, "conteudo", "Doenças endócrinas (parte II)", [("a42", "Classificação", EXC + _R)]),
 (45, "conteudo", "Teoria lipostática (parte II)", [("a43", "Lipostática", "au-lipostatica")]),
 (46, "logistica", "Como o organismo mantém o controle do tecido adiposo?", []),
 (47, "conteudo", "Vídeo", [("a44", "Vídeo", _VID)]),
 (48, "conteudo", "AMPK, principal regulador das vias catabólicas (LKB1, AMP)", [("a45", "AMPK", ["au-ampk", "ak-metformina-ampk"])]),
 (49, "conteudo", "AMPK fosforila e inibe a ACC → menos malonil-CoA", [("a46", "ACC", ["au-ampk", "ak-acc", "sh-1791729319038"])]),
 (50, "conteudo", "AMPK ativa PFK-2 → F2,6BP → PFK-1", [("a47", "PFK-2", ["ak-pfk2", "sh-1791647347495", "sh-1791647347996"])]),
 (51, "conteudo", "Adiponectina (parte II)", [("a48", "Adiponectina", "au-adiponectina")]),
 (52, "conteudo", "Camundongo ob/ob × selvagem", [("a49", "ob/ob", "au-ob")]),
 (53, "conteudo", "ob/ob 67 g → 35 g com leptina", [("a50", "Leptina emagrece o ob/ob", "au-ob")]),
 (54, "conteudo", "db/db × selvagem", [("a51", "db/db", "au-db")]),
 (55, "conteudo", "Parabiose (parte II)", [("a52", "Parabiose", "au-db")]),
 (56, "conteudo", "Resultados da parabiose (parte II)", [("a53", "Parabiose", "au-db")]),
 (57, "conteudo", "Leptina: solução? (parte II)", [("a54", "Resistência", "au-resistencia-leptina")]),
 (58, "conteudo", "Vídeo", [("a55", "Vídeo", _VID)]),
 (59, "conteudo", "Controle neural do apetite (parte II)", [("a56", "Arqueado", ["au-arqueado", "au-agrp"])]),
 (60, "conteudo", "Controle neural do apetite, MC4R (parte II)", [("a57", "MC4R", "au-arqueado")]),
 (61, "conteudo", "Optogenética (parte II)", [("a58", "Optogenética", "au-arqueado")]),
 (62, "conteudo", "Fome: fatores (sede, estresse, hábito)", [("a59", "Fatores da fome", ["ak-lateral-lesao", "ak-vmh-lesao", "ak-lateral-grelina"])]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "logistica": "título de seção ou bibliografia, sem conteúdo"}
CAPITULO = [("Lehninger cap. 23 (regulação hormonal e integração; massa corporal)", [
 ("l1", "Teoria lipostática e leptina", ["au-lipostatica", "ak-leptina"]), ("l2", "ob/ob e db/db", ["au-ob", "au-db"]),
 ("l3", "Leptina no arqueado (POMC, NPY)", ["au-arqueado", "au-agrp"]), ("l4", "AMPK e adiponectina", ["au-ampk", "au-adiponectina"]),
 ("l5", "Grelina e PYY", "ak-grelina-jejum")])]
EXERCICIOS = [
 ("Provas UC03 (índice biomol-03)", [
   ("p1", "Obesos secretam muita leptina e seguem obesos; GLP-1 (2023 P1 2.3)", ["au-resistencia-leptina", "ak-leptina-obesos", "sh-1791054014570"]),
   ("p2", "Resistência à insulina por TNF-α/IL-6 (2025 P2 1.8, eco)", "sh-1791593465568"),
   ("p3", "Leptina e resistência à insulina no emagrecimento tumoral (2024 P4 2.2, eco)", "ak-leptina"),
   ("p4", "Obesidade e resistência periférica à insulina (2023 P1 2.2, eco)", "ak-obesidade-ri")]),
]
