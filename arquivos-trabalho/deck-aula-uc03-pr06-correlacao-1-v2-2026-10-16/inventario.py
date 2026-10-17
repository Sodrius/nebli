"""Inventário atômico de Correlação patológica-radiológica 1 (UC03 P1; Patologia + Radiologia; casos: tabagista com enfisema, pneumonia
lobar e derrame; jovem com massa testicular), escrito ANTES de escolher cards (16/10, pipeline v4).
Sequência = 43 lâminas de 2026 (fontes/slides.pdf = turma Ib), vistas inteiras nesta sessão (io/g0..g3). Lido: lâminas Ia (33 pp., versão
anterior, mesmos casos), apostilas de veteranos (Apostila Guia de Radiologia pp. 14–15 e 26; “Tudo que você precisa saber de RD”; Apostila
Guia de Patologia, edema), apostila UC3 pp. 23–24 (os dois casos), Grande Resumo P1 pp. 52–53 (Discussão Radio/Pato 1), provas pat-rad-01,
Robbins (pulmão e testículo).
Fronteira (MEMORY §3): física, termos, contrastes, incidências, silhueta e atenuação são das aulas 02/04/05 → sh(); antracose e biomassa
da 24 Patologia ambiental, exsudato/transudato e derrame da 23 Edema → sh(). Aqui ficam o enfisema (imagem e peça), a pneumonia lobar
(imagem, fases e exsudato), o derrame (sinais, US, citologia), o sinal da silhueta aplicado e o seminoma (US, peça, histologia, conduta).
Sem transcrição nem vídeo nesta aula (a pasta da turma só tem as lâminas Ia e Ib).
"""
PREFIXO = "pr06"
AULA = "Correlação patológica-radiológica 1 (UC03 P1; Patologia + Radiologia)"
EXC = "EXC: "
SH04_SILHUETA, SH04_ATRIO, SH04_DUAS, SH04_ENFISEMA, SH04_HEMITORAX = (
    "sh-RD04-SILHUETA", "sh-RD04-ATRIO", "sh-RD04-DUAS", "sh-RD04-ENFISEMA", "sh-RD04-HEMITORAX")

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Caso 1: homem 60 a, tosse com expectoração amarelada e febre há 3 dias; tabagista 30 anos-maço", [
   ("a1", "Tabagismo é a principal causa de enfisema", ["ak-enf-tabaco", "ak-enf-centriacinar"]), ("a2", "Quadro agudo: pneumonia", "ak-febre-consolidacao")]),
 (3, "secao", "Radiografia de tórax", []),
 (4, "conteudo", "Zonas de leitura do RX de tórax (vias aéreas, pulmões, coração, diafragma)", [("a3", "Leitura sistemática ABCDE", EXC + "roteiro de leitura sem fato a decorar; os achados entram nos cards de cada lâmina")]),
 (5, "conteudo", "PA normal anotado: átrio direito, botão aórtico, tronco pulmonar, ventrículo esquerdo", [("a4", "Bordas da silhueta cardíaca", SH04_ATRIO)]),
 (6, "conteudo", "Perfil normal: coluna escurece para baixo, hemidiafragmas", [("a5", "PA e perfil", SH04_DUAS)]),
 (7, "conteudo", "Hilos direito e esquerdo no PA e no perfil", [("a6", "Anatomia dos hilos", EXC + "anatomia radiológica dos hilos, sem fato cobrado nem prova")]),
 (8, "conteudo", "RX de 6 meses atrás: hiperinsuflação (PA e perfil)", [("a7", "Enfisema no RX", ["ak-enf-rx", "ak-enf-lucencia", SH04_ENFISEMA])]),
 (9, "conteudo", "TC sem contraste: bolhas", [("a8", "Bolhas na TC", ["au-bolhas-tc", "sh-1791593313366"])]),
 (10, "conteudo", "Peça: pulmão negro (antracose)", [("a9", "Antracose", "sh-1791592721894")]),
 (11, "conteudo", "Peça: superfície de corte com espaços aéreos aumentados", [("a10", "Destruição alveolar", ["ak-enf-destruicao", "ak-enf-protease"])]),
 (12, "conteudo", "Peça: bolhas subpleurais", [("a11", "Bolha rompe → pneumotórax", "ak-bolha-pneumotorax")]),
 (13, "conteudo", "Peça: bolha aberta", [("a12", "Bolhas nos lobos superiores", "ak-enf-centriacinar")]),
 (14, "conteudo", "Histologia de pulmão normal", [("a13", "Referência normal", "ak-enf-aumento")]),
 (15, "conteudo", "Histologia do enfisema: septos rotos, espaços grandes", [("a14", "Espaços aéreos aumentados", ["ak-enf-aumento", "ak-enf-destruicao", "ak-enf-neutrofilos"])]),
 (16, "conteudo", "Ilustração 3D de alvéolos", [("a15", "Ilustração", EXC + "ilustração sem conteúdo novo")]),
 (17, "conteudo", "RX na entrada do PS: opacidade no campo médio/inferior esquerdo", [
   ("a16", "Consolidação", ["au-consolidacao", "ak-pn-rx"]), ("a17", "Febre + consolidação = pneumonia", ["ak-febre-consolidacao", "sh-1792141774459"])]),
 (18, "conteudo", "RX 6 meses atrás × atual", [("a18", "Velamento do seio costofrênico", "au-costofrenico")]),
 (19, "conteudo", "US: derrame pleural anecoico acima do diafragma", [("a19", "Derrame ao US", "au-us-derrame")]),
 (20, "conteudo", "TC com contraste: derrame à esquerda com pulmão colapsado", [
   ("a20", "Derrame grande desvia a traqueia para o lado oposto", "ak-traqueia-derrame"), ("a21", "Atelectasia puxa a traqueia", "ak-traqueia-atelectasia"),
   ("a22", "Hemitórax opaco", SH04_HEMITORAX)]),
 (21, "conteudo", "Citologia do derrame: neutrófilos", [
   ("a23", "Derrame parapneumônico", ["ak-parapneumonico", "sh-1791577164590"]), ("a24", "Exsudato", ["sh-1791141194538", "sh-1791592954543", "sh-1791169089006", "sh-1791780346752"])]),
 (22, "conteudo", "Citologia: grupos de células de adenocarcinoma", [("a25", "Derrame maligno", ["ak-adenoca-derrame", "ak-derrame-maligno", "ak-derrame-hemorragico"])]),
 (23, "conteudo", "Sinal do menisco", [("a26", "Menisco", ["au-menisco", "ak-derrame-rx"]), ("a27", "Derrame é acúmulo em cavidade", "sh-1791577166763")]),
 (24, "conteudo", "6 meses atrás × atual (repetida)", [("a28", "Opacidade nova", "au-consolidacao")]),
 (25, "conteudo", "Sinal da silhueta (esquema)", [("a29", "Sinal da silhueta", SH04_SILHUETA)]),
 (26, "conteudo", "Lobos pulmonares; língula", [("a30", "Língula é do pulmão esquerdo", "ak-lingula")]),
 (27, "conteudo", "Opacidade da língula apaga a borda cardíaca (PA e perfil)", [("a31", "Língula × borda esquerda", SH04_SILHUETA)]),
 (28, "conteudo", "Opacidade do lobo inferior esquerdo preserva a borda cardíaca", [("a32", "Lobo inferior × diafragma", "au-lobo-inferior")]),
 (29, "conteudo", "Peça: pneumonia lobar em hepatização cinzenta", [("a33", "Consolidação de um lobo inteiro", "ak-pn-lobar"), ("a34", "Hepatização cinzenta", "ak-hep-cinzenta")]),
 (30, "conteudo", "Histologia: alvéolos com exsudato e congestão", [("a35", "Congestão e hepatização vermelha", ["ak-pn-congestao", "ak-hep-vermelha"]), ("a36", "Resolução", "ak-pn-resolucao")]),
 (31, "conteudo", "Histologia: exsudato de neutrófilos nos alvéolos", [("a37", "Exsudato neutrofílico intra-alveolar", "ak-pn-exsudato"),
   ("a38", "Agentes da pneumonia lobar", "ak-pn-agente"), ("a39", "Broncopneumonia × lobar", "ak-broncopneumonia")]),
 (32, "conteudo", "Caso 2: homem 20 a, aumento testicular há 6 meses, sem trauma, sem febre", [
   ("a40", "Massa firme que não transilumina; quase todo tumor testicular é germinativo", ["ak-tumor-transiluminacao", "ak-gct-classe"]), ("a41", "Fator de risco: criptorquidia", "ak-criptorquidia")]),
 (33, "conteudo", "US de testículos normais e epidídimo; esquema do testículo", [("a42", "Testículo normal homogêneo", "au-us-nodulo")]),
 (34, "conteudo", "Doppler colorido dos dois testículos", [("a43", "Fluxo simétrico; afasta torção", EXC + "torção é da urologia; aqui o Doppler só mostra a lesão vascularizada (au-us-nodulo)")]),
 (35, "conteudo", "US: nódulo hipoecoico intratesticular", [("a44", "Nódulo hipoecoico sólido", "au-us-nodulo")]),
 (36, "conteudo", "Doppler: nódulo vascularizado", [("a45", "Lesão sólida vascularizada", "au-us-nodulo")]),
 (37, "conteudo", "Peça: massa testicular homogênea", [("a46", "Seminoma é o tumor testicular mais comum", "ak-seminoma-comum"), ("a47", "Massa homogênea", "ak-seminoma-macro")]),
 (38, "conteudo", "Peça: corte com massa branco-acastanhada", [("a48", "Sem hemorragia nem necrose", "ak-seminoma-macro")]),
 (39, "conteudo", "Histologia de testículo normal (túbulos seminíferos)", [("a49", "Túbulos substituídos pelo tumor", "ak-seminoma-histo")]),
 (40, "conteudo", "Histologia do seminoma: células claras e linfócitos", [("a50", "Células em ovo frito", "ak-seminoma-histo")]),
 (41, "conteudo", "E agora? Por que RX de tórax?", [("a51", "Metástase pulmonar e retroperitoneal", ["ak-metastase-pulmao", "ak-retroperitoneo"]),
   ("a52", "Prognóstico do seminoma × não seminoma", ["ak-seminoma-prognostico", "ak-nao-seminoma"]), ("a53", "Conduta: orquiectomia inguinal", "ak-orquiectomia"),
   ("a54", "Marcadores", ["ak-marcadores-seminoma", "ak-plap", "ak-hcg-seminoma"])]),
 (42, "logistica", "Dúvidas", []),
 (43, "logistica", "Obrigado", []),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "secao": "capa de seção sem conteúdo", "logistica": "dúvidas e agradecimento"}
CAPITULO = [("Robbins: pulmão (enfisema, pneumonia, derrame) e testículo (seminoma) (confirmam)", [
 ("l1", "Enfisema centroacinar no fumante; protease-antiprotease", ["ak-enf-centriacinar", "ak-enf-protease"]),
 ("l2", "Fases da pneumonia lobar", ["ak-pn-congestao", "ak-hep-vermelha", "ak-hep-cinzenta", "ak-pn-resolucao"]),
 ("l3", "Derrame exsudativo, empiema, derrame maligno", ["sh-1791577164590", "ak-derrame-maligno"]),
 ("l4", "Seminoma: macro, micro, disseminação linfática", ["ak-seminoma-macro", "ak-seminoma-histo", "ak-retroperitoneo"])])]
EXERCICIOS = [
 ("Provas UC03 (índice pat-rad-01)", [
   ("p1", "Descrever a opacidade/condensação no campo pulmonar (2024 P2 1.4, 2019 P1 1.10)", "au-consolidacao"),
   ("p2", "Nome das áreas mais brancas (2015 P1sub 3.1)", "sh-1792141774955"),
   ("p3", "Pneumonia secundária ao enfisema no idoso (2015 P1sub 3.6)", ["ak-febre-consolidacao", "ak-enf-tabaco"]),
   ("p4", "Derrame com Klebsiella na punção (2017 P1 3.1)", ["ak-pn-agente", "ak-parapneumonico"]),
   ("p5", "Biomassa e pneumonia (2025 P2 4.3)", "sh-1791592724520"),
   ("p6", "Cavitação no lobo superior (2025 P3 1.4)", EXC + "cavitação é da tuberculose (aulas de micobactérias e GR3)")]),
 ("Grande Resumo P1 e apostila UC3 (Discussão Radio/Pato 1)", [
   ("m1", "Hiperinsuflação, retificação do diafragma, bolhas hipoatenuantes na TC", ["ak-enf-rx", "au-bolhas-tc"]),
   ("m2", "Pulmão do fumante negro (carbono)", "sh-1791592721894"), ("m3", "Estouro de bolha → pneumotórax", "ak-bolha-pneumotorax"),
   ("m4", "Opacidade com sinal do menisco; US anecoico; derrame na TC", ["au-menisco", "au-us-derrame"]),
   ("m5", "Neutrófilos e células neoplásicas no líquido", ["ak-parapneumonico", "ak-adenoca-derrame"]),
   ("m6", "Silhueta: língula apaga o coração, lobo inferior não", [SH04_SILHUETA, "au-lobo-inferior"]),
   ("m7", "US testicular heterogêneo; RX de tórax para metástase", ["au-us-nodulo", "ak-metastase-pulmao"])]),
 ("Apostila Guia de Radiologia (hemitórax opaco, derrame) e “Tudo que você precisa saber de RD”", [
   ("v1", "Atelectasia puxa, derrame empurra, pneumonia não desvia", ["ak-traqueia-atelectasia", "ak-traqueia-derrame"]),
   ("v2", "Velamento do seio costofrênico e menisco", ["au-costofrenico", "au-menisco"]),
   ("v3", "Consolidação = preenchimento alveolar", "au-consolidacao")]),
]
