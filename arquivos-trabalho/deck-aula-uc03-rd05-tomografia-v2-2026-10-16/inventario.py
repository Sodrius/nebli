"""Inventário atômico de Tomografia computadorizada — Princípios da TC (UC03 P1; Radiologia; Preceptoria, João Vitor Dutra Vieira 2024 /
transcrição de Mauricio Silva Filho 2023), escrito ANTES de escolher cards (16/10, pipeline v4).
Sequência = 96 lâminas de 2026 (fontes/slides.pdf), vistas inteiras (visual/folha-01..16; estrelas do professor nas lâminas 3, 4, 6, 8, 16,
17, 23, 26, 34, 37, 46, 50, 56, 58, 89, 93). Lido inteiro nesta sessão: transcrição (86 pp.), monitoria P1 (aula de TC), apostila guia de
Radiologia (aula 3), apostila ilustrativa, “Tudo que você precisa saber de RD”, bibliografia da aula, Mello cap. 1 e livro cap. 3 (consulta),
provas rad-03.
Fronteira (MEMORY §3): a 02 Diagnóstico radiológico já tem o princípio da TC, forças e limites, planos, contraste por método, termos por
método (hiper/hipoatenuante), ACR e reconhecer a TC → associados por sh(); a 04 tem lateralidade e duas incidências → sh() depois de
instalada. Aqui ficam resolução, Hounsfield, janelas, fases do contraste, aquisição helicoidal, voxel, reconstrução, artefatos e exemplos
de achados (sangue agudo, AVC, esteatose, apendicite, pneumotórax).
"""
PREFIXO = "rd05"
AULA = "Tomografia computadorizada (UC03 P1; Radiologia; Preceptoria)"
EXC = "EXC: "
SH04_ORIENT = "sh-RD04-ORIENTACAO"   # preenchido no spec com o nid da 04 instalada
SH04_DUAS = "sh-RD04-DUAS"

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "secao", "Semiologia radiológica", []),
 (3, "conteudo", "Lateralidade na radiologia: direita do paciente à esquerda da imagem", [("a1", "Convenção de lateralidade", SH04_ORIENT)]),
 (4, "conteudo", "Resolução espacial (mais pixels) × resolução de contraste (aumenta com meio de contraste)", [
   ("a2", "Resolução espacial × de contraste", "au-resolucao"), ("a3", "Contraste exógeno aumenta a diferença entre tecidos", "sh-1792141768903")]),
 (5, "secao", "Métodos de imagem", []),
 (6, "conteudo", "Métodos de imagem; TC sem e com contraste (arterial, venosa, tardia, angio, cisto)", [
   ("a4", "Lista dos métodos", "sh-1792141766560"), ("a5", "TC com e sem contraste; fases", "au-fases")]),
 (7, "conteudo", "Colagem de métodos (RX, US, TC, RM, PET, elastografia)", [("a6", "Métodos se complementam", EXC + "mensagem sem fato a decorar (repetida na lâmina 93)")]),
 (8, "conteudo", "Objetivo = melhor cuidado do paciente", [("a7", "Objetivo", EXC + "frase motivacional")]),
 (9, "conteudo", "Tomografia computadorizada (foto)", [("a8", "Reconhecer a TC", "sh-1792141772255")]),
 (10, "conteudo", "Gantry, mesa, console, bomba injetora de contraste", [("a9", "Equipamento: tubo que gira no gantry", "sh-1792141770757")]),
 (11, "conteudo", "Gantry e bomba injetora (fotos)", [("a10", "Equipamento", "sh-1792141770757")]),
 (12, "conteudo", "Tubo de raio X e arco de detectores opostos", [("a11", "Tubo e detectores opostos giram", "sh-1792141770757")]),
 (13, "conteudo", "Gantry aberto girando (foto)", [("a12", "Tubo gira", "sh-1792141770757")]),
 (14, "conteudo", "Contraste iodado EV, VO, VR", [("a13", "Iodo na TC", "sh-1792141769157")]),
 (15, "conteudo", "Contraste baritado VO, VR", [("a14", "Bário no tubo digestivo", "sh-1792141769157")]),
 (16, "conteudo", "Dados brutos → reconstrução axial, sagital, coronal, 3D, MIP, MinIP", [("a15", "Aquisição axial reconstruída em outros planos", "au-reconstrucao")]),
 (17, "conteudo", "Axial, sagital, coronal, reformatação 3D", [("a16", "Planos na TC", ["sh-1792141772506", "au-reconstrucao"])]),
 (18, "conteudo", "Anatomia × radiografia × tomografia", [("a17", "TC remove a sobreposição", "sh-1792141770757")]),
 (19, "secao", "Aquisição da imagem", []),
 (20, "conteudo", "Dados brutos (repetida)", [("a18", "Reconstrução", "au-reconstrucao")]),
 (21, "conteudo", "Sombra da mulher com banana e abacaxi", [("a19", "Uma projeção esconde objetos", SH04_DUAS)]),
 (22, "conteudo", "“One view is no view!”", [("a20", "Duas incidências", SH04_DUAS)]),
 (23, "conteudo", "Esquema: objetos sobrepostos no filme; dois feixes separam", [("a21", "TC: muitas projeções separam o que o RX sobrepõe", "sh-1792141770757")]),
 (24, "conteudo", "Radiografia localizadora (scout): planejamento", [("a22", "Scout", EXC + "detalhe operacional do técnico; nenhum acervo nem prova")]),
 (25, "conteudo", "Tubo girando em volta do paciente (esquema)", [("a23", "Rotação do tubo", "sh-1792141770757")]),
 (26, "conteudo", "Tubo girando com mesa avançando (esquema espiral)", [("a24", "Aquisição em espiral", "au-helicoidal")]),
 (27, "conteudo", "Evolução da TC: 1ª a 3ª geração", [("a25", "Gerações", EXC + "história do equipamento; só a helicoidal/multislice importa (lâminas 30–34)")]),
 (28, "conteudo", "4ª e 5ª geração", [("a26", "Gerações", EXC + "idem")]),
 (29, "conteudo", "Slip-rings", [("a27", "Slip-rings permitem rotação contínua", "au-helicoidal")]),
 (30, "conteudo", "6ª geração: helicoidal", [("a28", "Helicoidal", "au-helicoidal"), ("a29", "TC helicoidal sem contraste para cálculo renal", "ak-helicoidal-calculo")]),
 (31, "conteudo", "7ª geração: helicoidal e multislice; 64 fileiras no HC", [("a30", "Multislice", "au-helicoidal")]),
 (32, "conteudo", "Arco e fileira de detectores", [("a31", "Fileiras de detectores", "au-helicoidal")]),
 (33, "conteudo", "Single slice × multislice", [("a32", "Várias fatias por giro", "au-helicoidal")]),
 (34, "conteudo", "Helicoidal = exame contínuo; multislice = várias fatias por acionamento; mais resolução, menos tempo", [("a33", "Helicoidal e multislice", "au-helicoidal")]),
 (35, "secao", "Interpretação dos dados brutos", []),
 (36, "conteudo", "Dados brutos (repetida)", [("a34", "Reconstrução", "au-reconstrucao")]),
 (37, "conteudo", "Voxel: pixel 2D → voxel 3D; matriz 512×512; eixo Z = espessura", [("a35", "Voxel", "au-voxel")]),
 (38, "conteudo", "Esquema: tubo, colimador, detectores, computador, monitor", [("a36", "Detectores mandam dados ao computador", "sh-1792141770757")]),
 (39, "conteudo", "Problema-método-solução da reconstrução (matriz A+B)", [("a37", "Matemática da reconstrução", EXC + "álgebra da retroprojeção: acima do recorte, sem prova")]),
 (40, "conteudo", "Retroprojeção em matriz", [("a38", "Retroprojeção", EXC + "idem")]),
 (41, "conteudo", "Número de projeções melhora a imagem", [("a39", "Projeções", EXC + "idem")]),
 (42, "conteudo", "Voxel no corte (esquema)", [("a40", "Voxel", "au-voxel")]),
 (43, "secao", "Formação da imagem", []),
 (44, "conteudo", "Dados brutos (repetida)", [("a41", "Reconstrução", "au-reconstrucao")]),
 (45, "conteudo", "Quantificar densidades: atenuação relativa à água; fórmula de Hounsfield", [("a42", "Hounsfield relativo à água", "au-hu")]),
 (46, "conteudo", "Escala de unidades Hounsfield", [("a43", "Escala", "au-hu")]),
 (47, "conteudo", "Ar −1000, água 0, osso +1000", [("a44", "Valores de referência", "au-hu")]),
 (48, "conteudo", "Figura Kamalian: UH de osso, substância branca, sangue, líquor, gordura, ar", [
   ("a45", "Sangue agudo mais denso que o encéfalo", ["ak-sangue-agudo", "ak-avc-hemorragico"]), ("a46", "Valores por tecido", "au-hu")]),
 (49, "conteudo", "Janelas: 2000 valores × 256 tons × olho vê ~20", [("a47", "Por que janelar", "au-janela")]),
 (50, "conteudo", "Janela e nível: acima do limite = branco, abaixo = preto", [("a48", "Nível = centro; acima branco, abaixo preto", "au-janela")]),
 (51, "conteudo", "Exemplo: nível 50, janela 200 → −50 a 150", [("a49", "Exemplo numérico", "au-janela")]),
 (52, "conteudo", "Partes moles, parênquima pulmonar, osso", [("a50", "Janela por tecido", "au-janela-ampla")]),
 (53, "conteudo", "Janelas de pulmão, osso e encéfalo (AVC)", [("a51", "Janela ampla × estreita", "au-janela-ampla")]),
 (54, "conteudo", "Isquemia encefálica à direita: mais escuro", [("a52", "Isquemia hipodensa", "sh-1791054020270")]),
 (55, "conteudo", "Janela ampla: atenuações muito diferentes (pulmão, osso); estreita: semelhantes (encéfalo, partes moles)", [("a53", "Ampla × estreita", "au-janela-ampla")]),
 (56, "conteudo", "Hiperatenuante = branco, alta atenuação; hipoatenuante = preto", [("a54", "Termos da TC", "sh-1792141774955")]),
 (57, "secao", "Técnicas do exame", []),
 (58, "conteudo", "Protocolo: sem contraste; angiográfica 15 s, arterial 30 s, portal 70 s, nefrográfica 90 s, equilíbrio 3 min, excretora 7 min", [
   ("a55", "Fases e tempos", "au-fases")]),
 (59, "conteudo", "Contraste iodado (repetida)", [("a56", "Iodo", "sh-1792141769157")]),
 (60, "conteudo", "Contraste baritado (repetida)", [("a57", "Bário", "sh-1792141769157")]),
 (61, "conteudo", "Exame trifásico: sem, arterial, portal, equilíbrio", [("a58", "Várias aquisições no exame contrastado", "au-fases")]),
 (62, "conteudo", "Sem contraste", [("a59", "Fase sem contraste", "au-fases")]),
 (63, "conteudo", "Arterial: nódulo hipervascular, córtex renal", [("a60", "Fase arterial", ["au-fases", "sh-1791022169824"])]),
 (64, "conteudo", "Venosa/portal", [("a61", "Fase portal", "au-fases")]),
 (65, "conteudo", "Tardia", [("a62", "Fase tardia", "au-fases")]),
 (66, "conteudo", "Sem contraste, arterial, portal, equilíbrio, nefrográfica (mesmo corte)", [("a63", "Comparar fases", "au-fases")]),
 (67, "conteudo", "Contraste EV, EV + água VO, EV + VR, EV + VO", [("a64", "Contraste oral e retal", "sh-1792141769157")]),
 (68, "conteudo", "Artefato de endurecimento do feixe (metal dentário)", [("a65", "Endurecimento do feixe", "au-metal")]),
 (69, "conteudo", "Artefatos de movimentação", [("a66", "Movimento borra a imagem", EXC + "só o nome do artefato, sem fato cobrável; citado no verso de au-metal")]),
 (70, "conteudo", "Panorâmica com cães duplicados (analogia do movimento)", [("a67", "Analogia", EXC + "ilustração do artefato de movimento")]),
 (71, "secao", "Anatomia TC", []),
] + [(n, "conteudo", "Anatomia seccional do abdome e pelve (cortes axiais e coronal)", [(f"a{n}", "Anatomia seccional",
     EXC + "anatomia por TC é das aulas de anatomia e correlação; nenhum fato isolado ensinado")]) for n in range(72, 85)] + [
 (85, "secao", "Exemplos de achados", []),
 (86, "conteudo", "Apendicite aguda não complicada: parede espessa, gordura densificada", [("a86", "Densificação da gordura", "au-stranding")]),
 (87, "conteudo", "Esteatose hepática: fígado hipoatenuante (perto da gordura)", [("a87", "Esteatose na TC", "sh-1791022172025")]),
 (88, "conteudo", "Pneumotórax no RX e na TC (janela de pulmão)", [("a88", "Pneumotórax: linha pleural", "ak-pneumotorax")]),
 (89, "conteudo", "Vantagens (rápido, resolução, seccional, sem sobreposição, quantitativo) e desvantagens (radiação, contraste, transporte)", [
   ("a89", "Forças e limites", "sh-1792141770406"), ("a90", "Contraste e rim", ["ak-contraste-nta", "ak-contraste-hidratacao"])]),
 (90, "conteudo", "O que queremos: pedir o exame certo; achados que não esperam o radiologista", [
   ("a91", "TC sem contraste antes de trombolisar", "ak-tc-avc"), ("a92", "Hematoma subdural agudo × crônico", ["ak-sdh-agudo", "ak-sdh-cronico", "ak-sdh-agudizado"])]),
 (91, "conteudo", "ACR Appropriateness Criteria: 1–3, 4–6, 7–9", [("a93", "ACR", "sh-1792141767159")]),
 (92, "conteudo", "Tabela ACR: dor no hipocôndrio direito", [("a94", "US primeiro no hipocôndrio direito", "sh-1792141767159")]),
 (93, "conteudo", "Mensagens finais: volumétrico, radiação ionizante, contraste, resolução, pedido conforme hipótese", [
   ("a95", "Radiação cumulativa", "sh-1792141771005"), ("a96", "Síntese", "sh-1792141770406")]),
 (94, "conteudo", "Hounsfield, Nobel 1979", [("a97", "História", EXC + "curiosidade (a fala diz “só uma curiosidade”)")]),
 (95, "conteudo", "TC de 1971 × 2023", [("a98", "História", EXC + "curiosidade")]),
 (96, "logistica", "Obrigado", []),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "secao": "capa de seção sem conteúdo", "logistica": "agradecimento e e-mail"}
CAPITULO = [("Bibliografia da aula, livro cap. 3 (TC) e Mello cap. 1 (confirmam)", [
 ("l1", "Princípio: tubo e detectores giram; projeções → reconstrução", ["sh-1792141770757", "au-reconstrucao"]),
 ("l2", "Hounsfield e janelas", ["au-hu", "au-janela", "au-janela-ampla"]),
 ("l3", "Helicoidal e multislice", "au-helicoidal"),
 ("l5", "Artefatos de metal e movimento", "au-metal")])]
EXERCICIOS = [
 ("Provas UC03 (índice rad-03)", [
   ("p1", "Princípio de formação da TC: tubo gira 360°, detectores opostos, fatias, reconstrução (2024 P1, 2023 P1, 2017 P1)", ["sh-1792141770757", "au-reconstrucao"]),
   ("p2", "Descrever hiper/hipoatenuante (2025 P2/P4, 2018, 2017)", "sh-1792141774955"),
   ("p3", "Aorta hiperatenuante pelo contraste EV (2023 P1, 2017 P3)", ["sh-1792141769157", "au-fases"]),
   ("p4", "Lesão hipoatenuante isquêmica no encéfalo (2019 P1, 2018 P3)", "sh-1791054020270"),
   ("p5", "Hemorragia encefálica hiperatenuante (2018 P3 3.5)", ["ak-sangue-agudo", "ak-avc-hemorragico"]),
   ("p6", "Vidro fosco: atenuação intermediária (2024 P3)", "ak-vidro-contusao"),
   ("p7", "Cuidados com a TC: dose maior que o RX, contraste nefrotóxico (2019 P4, 2017 P2/P3)", ["sh-1792141770406", "sh-1792141771005", "ak-contraste-nta", "ak-contraste-hidratacao"]),
   ("p8", "Janela óssea (2024 P1)", "au-janela-ampla")]),
 ("Monitoria P1 (aula de TC)", [("m1", "Helicoidal e múltiplos cortes por giro", "au-helicoidal"), ("m2", "Centro e largura da janela; janela fechada", ["au-janela", "au-janela-ampla"]),
   ("m3", "Fases: angiográfica, arterial, portal, nefrográfica, tardia, equilíbrio", "au-fases"), ("m4", "Artefatos: metal (strike), movimento, volume parcial", "au-metal")]),
 ("Apostila guia de Radiologia (aula 3) e apostila ilustrativa", [("v1", "Hounsfield e densidades", "au-hu"), ("v2", "Janelas", ["au-janela", "au-janela-ampla"]),
   ("v3", "Termos hiper/hipoatenuante", "sh-1792141774955")]),
 ("“Tudo que você precisa saber de RD”", [("t1", "Nomenclatura por método", "sh-1792141774955"), ("t2", "Contraste iodado e fases", ["sh-1792141769157", "au-fases"])]),
]
