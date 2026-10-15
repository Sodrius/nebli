"""Inventário de Organização e funcionamento do sistema imune (UC03 P1; Imunologia; 26 lâminas), escrito antes da seleção (15/10), por informação.
Material: lâminas, transcrição inteira (7.060 palavras), palavras-cruzadas (jpg) e gabarito, provas imuno-01 (19 itens)."""
PREFIXO = "im07"
AULA = "Organização e funcionamento do sistema imune (UC03 P1; Imunologia)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "capa", "Abertura", []),
 (3, "conteudo", "Objetivos", [("a1", "Órgãos linfoides, recirculação, resposta × tolerância, adesão", ["c-primarios", "d-secundarios", "i-adesao"])]),
 (4, "conteudo", "Papel: homeostasia que inclui o exterior", [("a2", "Sistemas nervoso e imune olham o exterior; sinais moleculares", "a-exterior")]),
 (5, "conteudo", "Tradutor universal", [("a3", "Repertório completo, clonal; antígeno", "a-antigeno")]),
 (6, "conteudo", "O sistema em ação: inata", [("a4", "Barreiras; células residentes e seus alarmes (DAMPs, citocinas, mediadores, adesão)", "b-alarmes")]),
 (7, "conteudo", "Fagocitose", [("a5", "Etapas", S(1792029611637))]),
 (8, "conteudo", "Citotoxicidade", [("a6", "Morte induzida", S(1792054600579))]),
 (9, "conteudo", "Inata → adquirida; ILC", [("a7", "Adquirida em paralelo, dirigida pela inata", S(1792055399868)), ("a7b", "ILC direcionam", "b-alarmes")]),
 (10, "conteudo", "Órgãos primários: seleção", [("a8", "Geração e seleção do repertório", "c-primarios"), ("a9", "Interação com APC; autorreatividade: deleção ou Treg", ["c-selecao-timo", S(1791625434632)])]),
 (11, "conteudo", "Primários → secundários", [("a10", "Timo T, medula B; linfonodo, baço, Peyer, apêndice, Waldeyer", ["c-primarios", "d-secundarios", "ak-secundarios"])]),
 (12, "conteudo", "Interação → ação", [("a11", "Reconhecimento no secundário, ação no tecido", "d-naive")]),
 (13, "conteudo", "Circulação dos naive", [("a12", "Primário → sangue → secundário (HEV) → linfa → sangue", ["d-naive", S(1791625425583), "d-por-que"])]),
 (14, "conteudo", "Circulação dos T ativados", [("a13", "Mudam adesão; vigilância dos tecidos", "d-ativados")]),
 (15, "conteudo", "Características do sistema", [("a14", "Geração aleatória, distribuição, redistribuição, fluidez", "d-fluidez")]),
 (16, "conteudo", "Esquema do sistema em ação", [("a15", "Alarme → recrutamento → paisagem molecular → órgão linfoide → resposta/tolerância", ["e-paisagem", S(1792065578750), "e-coexistem"])]),
 (17, "conteudo", "Secundários: condições estruturais", [("a16", "Fluxo contínuo, muitas APCs, probabilidade do encontro", "e-vacina")]),
 (18, "conteudo", "Secundários: APCs", [("a17", "DC, macrófago, B", [S(1792044192107), S(1791625426408)]), ("a18", "Apresentação cruzada", S(1791625427531)), ("a19", "B: apresentação seletiva", "f-b-seletiva")]),
 (19, "conteudo", "Secundários: aferência", [("a20", "Linfonodo (linfa), baço (sangue), MALT (luz, célula M)", "f-aferencia")]),
 (20, "conteudo", "Expansão clonal regionalizada", [("a21", "Áreas T e B", ["f-areas", "ak-pals"]), ("a22", "Centro germinativo", S(1791625425757)), ("a23", "FDC", "f-fdc")]),
 (21, "conteudo", "Eferência", [("a24", "Plasmócitos: cordões, polpa vermelha, medula", "h-plasmocitos"), ("a25", "T ativados para os tecidos", "d-ativados"), ("a26", "Tempo da resposta", "h-duas-semanas")]),
 (22, "conteudo", "Moléculas de adesão", [("a27", "Selectinas, integrinas, superfamília Ig, mucinas", "i-adesao")]),
 (23, "conteudo", "Moléculas quimiotáticas", [("a28", "Quimiocinas, C3a/C5a, lipídicos", "i-quimiotaticas")]),
 (24, "conteudo", "Revendo o sistema em ação", [("a29", "Repetição da 16", ["e-paisagem", S(1792065578750)])]),
 (25, "conteudo", "Resumo dos secundários", [("a30", "Fluxo, APCs, aferência, expansão, eferência", ["f-aferencia", "f-areas", "h-plasmocitos"])]),
 (26, "conteudo", "Leitura complementar", [("a31", "Artigos", EXC + "lista de referências")]),
]
JUSTIFICATIVAS = {1: "capa", 2: "abertura sem texto"}
CAPITULO = [("Transcrição da aula", [("t1", "Seleção na medula menos estrita (T controla B)", "c-medula-menos-estrita"), ("t2", "Vacina e probabilidade", "e-vacina"),
   ("t3", "FDC e memória", "f-fdc"), ("t4", "Plasmócitos na medula; mieloma", "h-plasmocitos"), ("t5", "Duas semanas; janela imunológica", "h-duas-semanas"),
   ("t6", "Resposta e tolerância simultâneas", "e-coexistem")])]
EXERCICIOS = [("Provas UC03 (imuno-01)", [("p1", "2024 P1 2.11: inata × adquirida", S(1792055399868)), ("p2", "2024 P2 2.1: elementos da inata", "b-alarmes"),
   ("p3", "2024 P1: folículos na tireoidite (órgão linfoide terciário)", S(1791983685631)), ("p4", "2025: timo e tolerância periférica (Treg)", ["c-selecao-timo", S(1791625434632)]),
   ("p5", "Critérios de seleção no timo", "c-selecao-timo"), ("p6", "Seleção na medula menos estrita", "c-medula-menos-estrita"),
   ("p7", "Linfonodo aumentado: regiões e resposta celular", "f-areas"), ("p8", "Mucosa digestiva e MALT", "f-aferencia")])]
