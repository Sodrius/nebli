"""Inventário atômico de Mecanismos de ação hormonal (UC03 P1; Bioquímica; Deborah Schechtman), escrito ANTES de escolher cards
(17/10, pipeline v4). Sequência = 56 lâminas (fontes/slides.pdf = turma II = pasta pessoal), vistas inteiras nesta sessão (io/g0..g4).
Lido nesta sessão: transcrição integral (74 pp.), provas bq01, apostila de exercícios de Bioquímica, apostila guia e UC3 (texto da corrida
antiga), Lehninger cap. 23 (integração hormonal; consulta). Lâminas I (46) e III (35) da turma conferidas (mesmo roteiro).
Fronteira (MEMORY §3): secreção de insulina, GLUT, glicoquinase, regulação do glicogênio, efeitos de insulina e glucagon, receptores
nucleares e sinalização já têm cópias NEBLI de GR2 (diabetes), integração I e II (25 e 33), biologia molecular e farmacologia → sh().
"""
PREFIXO = "bq10"
AULA = "Mecanismos de ação hormonal (UC03 P1; Bioquímica)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Regulação metabólica: interferir na velocidade das reações; efeito propagado", [("a1", "Mudar a quantidade de enzima é o controle mais lento e decisivo", "sh-1791647344393")]),
 (3, "conteudo", "Regulação: modulação alostérica, modificação covalente, expressão", [
   ("a2", "Fosforilação ativa a fosforilase e inativa a sintase", ["sh-1791647344895", "sh-1791647345145"])]),
 (4, "logistica", "Hormônios", []),
 (5, "conteudo", "Integração metabólica: abundância e escassez, oscilações diárias; feita por hormônios", [("a3", "Integração pelos hormônios", EXC + "introdução; os efeitos de cada hormônio entram nas lâminas 23–54")]),
 (6, "conteudo", "O que são hormônios? (vídeo)", [("a4", "Vídeo", EXC + "vídeo indicado, sem texto")]),
 (7, "conteudo", "Hormônios: agem a distância, em baixa quantidade, por receptores", [("a5", "Sensibilidade do alvo depende dos receptores", "sh-1791762417900")]),
 (8, "conteudo", "Pontos de regulação: biossíntese → … → degradação", [("a6", "Sequência", EXC + "sequência sem fato a decorar; cada etapa aparece nos hormônios específicos")]),
 (9, "conteudo", "Classes por estrutura: eicosanoides, catecolaminas, esteroides, peptídicos", [
   ("a7", "Aminas derivam da tirosina", ["ak-aminas-tirosina", "ak-aminas-classes"]), ("a8", "Esteroides derivam do colesterol", "ak-esteroide-colesterol")]),
 (10, "conteudo", "Endócrino, parácrino, autócrino", [("a9", "Modos de sinalização", ["sh-1791743348861", "sh-1791743348682", "sh-1791743348483"])]),
 (11, "conteudo", "Hormônios × neurotransmissores", [("a10", "Comparação", EXC + "figura comparativa sem fato próprio; catecolaminas nas lâminas 40–41")]),
 (12, "conteudo", "Dosagem por radioimunoensaio (RIA)", [("a11", "RIA", EXC + "técnica laboratorial só ilustrada, sem fala nem prova")]),
 (13, "conteudo", "Tipos de transdutores de sinal", [("a12", "Receptor tirosina quinase", "sh-1791762411098"), ("a13", "Receptores β acoplados a Gs", "sh-1791762410700")]),
 (14, "conteudo", "Tipos de transdutores (canais, GPCR, quinases, nucleares)", [("a14", "Peptídeos na membrana; esteroides dentro", "ak-receptor-membrana")]),
 (15, "conteudo", "Todos agem por receptores de alta afinidade; peptídeo × esteroide", [
   ("a15", "Peptídeo age rápido, esteroide lento", "ak-peptideo-rapido"), ("a16", "Esteroide e tireoide em receptores nucleares", "sh-1791627550027")]),
 (16, "conteudo", "Amplificação por segundo mensageiro (AMPc)", [("a17", "Gs ativa adenilato ciclase; AMPc ativa PKA; PDE degrada", ["ak-gs-ac", "ak-camp-pka", "ak-pde"])]),
 (17, "conteudo", "Classes de hormônios (tabela Lehninger)", [("a18", "Tabela", ["ak-aminas-classes", "ak-receptor-membrana"])]),
 (18, "conteudo", "Classes (estruturas)", [("a19", "Estruturas", "ak-esteroide-colesterol")]),
 (19, "conteudo", "Hormônios peptídicos: insulina e glucagon", [("a20", "Insulina: cadeias A e B com pontes dissulfeto", "ak-insulina-cadeias")]),
 (20, "conteudo", "Insulina e glucagon no ciclo alimentação–jejum", [("a21", "Glicose regula a insulina; hipoglicemia, o glucagon", ["sh-1791647354170", "sh-1791647354044"])]),
 (21, "conteudo", "Descoberta da insulina", [("a22", "História", EXC + "história (Minkowski, Banting e Best)")]),
 (22, "conteudo", "Processamento pós-traducional da insulina", [
   ("a23", "Pré-pró-insulina → pró-insulina → insulina + peptídeo C", ["ak-preproinsulina", "ak-peptideo-sinal", "ak-golgi", "ak-peptideo-c", "ak-granulos-c"]),
   ("a24", "Peptídeo C: equimolar, marca a insulina endógena", ["ak-equimolar", "sh-1791054008921", "ak-insulinoma-c", "ak-exogena-c"])]),
 (23, "conteudo", "Efeito da insulina no fígado e no músculo", [("a25", "Alvos da insulina", ["ak-insulina-locais", "ak-insulina-musculo"])]),
 (24, "conteudo", "Transporte de glicose: GLUT1–4", [("a26", "GLUT4 depende de insulina", ["sh-1791054011372", "sh-1791729320761", "ak-glut4-expressao"]), ("a27", "GLUT2 na célula β", "sh-1791647354296")]),
 (25, "conteudo", "Glicoquinase × hexoquinase", [("a28", "Km e Vmax; onde está a glicoquinase", ["sh-1791647346746", "sh-1791647346871", "ak-gk-orgaos"])]),
 (26, "conteudo", "Secreção de insulina: GLUT2, glicoquinase, ATP fecha K-ATP, despolarização, Ca²⁺", [
   ("a29", "Cadeia da secreção", ["ak-gk-beta", "sh-1791729317038", "sh-1791729317165", "sh-1791731883157", "sh-1791729317515"])]),
 (27, "conteudo", "Sulfonilureias fecham K-ATP", [("a30", "Sulfonilureias", ["sh-1791054014146", "ak-sulfo-classes"])]),
 (28, "conteudo", "Agonistas de K-ATP na hiperinsulinemia (insulinoma); minoxidil", [("a31", "Abrir K-ATP impede a secreção", ["au-diazoxido", "ak-minoxidil"])]),
 (29, "conteudo", "Vias de síntese e degradação de glicogênio", [("a32", "Sintase regulada por insulina, cortisol, G6P", "sh-1791647352121")]),
 (30, "conteudo", "Regulação do metabolismo do glicogênio", [("a33", "Insulina: PKB inibe GSK3; PP1 ativa a sintase", ["sh-1791729317761", "sh-1791647349819", "ak-desfosfo-sintase"])]),
 (31, "conteudo", "Regulação da glicogênio fosforilase (a/b; AMP, ATP, glicose)", [
   ("a34", "Alostéricos da fosforilase", ["sh-1791647351996", "ak-fosforilase-inibe", "sh-1791647348495", "sh-1791647345020"]), ("a35", "Fosforilase desfosforilada é inativa", "ak-desfosfo-fosforilase")]),
 (32, "conteudo", "Cascata da insulina sobre o glicogênio (PP1, GSK3, PDE)", [
   ("a36", "Receptor de insulina: dimeriza, autofosforila, IRS-1, PI3K", ["ak-receptor-dimeriza", "ak-irs", "ak-sh2", "ak-pi3k"]),
   ("a37", "Insulina ativa PDE e desliga PKA", "sh-1791729317887"), ("a38", "AKT e FOXO1", "sh-1791627551127")]),
 (33, "conteudo", "Regulação do metabolismo pela insulina (fígado, músculo, adiposo)", [("a39", "Efeitos da insulina", ["sh-1791729316389", "sh-1791729320088", "sh-1791647352471"])]),
 (34, "conteudo", "Insulina e glucagon (repetida)", [
   ("a40", "Interações entre hormônios das ilhotas", ["sh-1791054011119", "ak-glucagon-insulina", "ak-somatostatina", "ak-amilina", "sh-1790999836955"])]),
 (35, "conteudo", "Glucagon: 29 aa, célula α, estímulos e inibidores, uso na hipoglicemia", [
   ("a41", "Célula α e estímulos", ["sh-1791647353670", "sh-1791647354044"]), ("a42", "Glucagon IM na hipoglicemia", ["sh-1791054010097", "ak-hipoglicemia-iv"])]),
 (36, "conteudo", "Pró-glucagon → glucagon, GLP-1, GLP-2", [("a43", "GLP-1", "sh-1791054014447")]),
 (37, "conteudo", "Sinalização do glucagon: Gs, AMPc, PKA, fosforilase quinase", [("a44", "Via do glucagon", ["sh-1791647349571", "sh-1791647347621", "sh-1791731887453"])]),
 (38, "conteudo", "Regulação do metabolismo pelo glucagon", [
   ("a45", "Efeitos do glucagon", ["sh-1791054011246", "sh-1791729320461", "sh-1791729320636", "ak-glucagon-locais", "ak-glucagon-cetoacidos", "ak-glucagon-ureia", "ak-glucagon-catabolico"]),
   ("a46", "Músculo não tem receptor de glucagon", "sh-1791647350720")]),
 (39, "logistica", "Catecolaminas", []),
 (40, "conteudo", "Síntese: tirosina → DOPA → dopamina → noradrenalina → adrenalina", [("a47", "Enzimas da síntese", ["ak-th", "ak-dbh", "ak-pnmt"])]),
 (41, "conteudo", "Sinalização da epinefrina; efeitos; uso clínico", [
   ("a48", "Epinefrina degrada glicogênio no músculo", ["sh-1791647350546", "sh-1791647349446"]), ("a49", "Estresse: epinefrina e cortisol", ["ak-estresse", "sh-1791054013222"])]),
 (42, "conteudo", "Hormônios tireoidianos T4, T3, rT3; transportador; receptor nuclear", [
   ("a50", "Entram por transportador e agem no núcleo", ["au-mct8", "ak-t3-nucleo", "sh-1791627550153"]), ("a51", "T3 tem maior afinidade", "ak-t3-afinidade")]),
 (43, "conteudo", "Hormônios tireoidianos (fisiologia)", [("a52", "Aumentam o metabolismo basal", "ak-bmr")]),
 (44, "conteudo", "Eixo hipotálamo-hipófise-tireoide", [("a53", "Eixo", EXC + "eixo TRH-TSH é da endocrinologia; aqui o mecanismo de ação (lâmina 42)")]),
 (45, "conteudo", "Efeitos em órgãos-alvo", [("a54", "Efeito catabólico", "ak-tireoide-catabolico")]),
 (46, "conteudo", "Hipotireoidismo × hipertireoidismo (sintomas)", [("a55", "Metabolismo acelerado ou lento", "ak-bmr")]),
 (47, "conteudo", "Hormônios esteroides (estruturas)", [("a56", "Derivados do colesterol", "ak-esteroide-colesterol")]),
 (48, "conteudo", "Hormônios lipossolúveis: receptores nucleares", [("a57", "Dedo de zinco", "sh-1791627550277")]),
 (49, "conteudo", "Receptor de esteroide: ligante, coativador", [("a58", "Dimeriza, liga SRE, faz novas proteínas", ["ak-esteroide-dimeriza", "ak-sre", "ak-novas-proteinas"])]),
 (50, "conteudo", "Cortisol: eixo CRH–ACTH, feedback", [("a59", "Feedback negativo", "ak-cortisol-feedback")]),
 (51, "conteudo", "Síntese do cortisol a partir do colesterol", [("a60", "Desmolase é o primeiro passo; ACTH a estimula", ["ak-desmolase", "ak-acth-desmolase"])]),
 (52, "conteudo", "Receptor de glicocorticoide", [("a61", "GR vai ao núcleo", "sh-1791627550527")]),
 (53, "conteudo", "Efeitos do cortisol", [("a62", "Catabólico: proteólise, lipólise, gliconeogênese, resistência à insulina",
   ["ak-cortisol-catabolico", "sh-1791729316911", "ak-cortisol-lipolise", "ak-cortisol-gng", "ak-cortisol-insulina"])]),
 (54, "conteudo", "Addison (autoimune) × Cushing (excesso de glicocorticoide)", [("a63", "Addison e Cushing", ["ak-addison", "ak-cushing-sindrome", "ak-cushing-doenca"])]),
 (55, "conteudo", "Disruptores endócrinos: imitam ou bloqueiam", [("a64", "Disruptores", "au-disruptores")]),
 (56, "logistica", "Bibliografia", []),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "logistica": "capa de seção ou bibliografia, sem conteúdo"}
CAPITULO = [("Lehninger cap. 23 (regulação hormonal e integração) (confirma)", [
 ("l1", "Classes de hormônios e receptores", ["ak-aminas-classes", "ak-receptor-membrana"]),
 ("l2", "Insulina: receptor, IRS, PI3K, GLUT4", ["ak-receptor-dimeriza", "ak-pi3k", "sh-1791054011372"]),
 ("l3", "Glucagon e epinefrina por AMPc", ["sh-1791647349571", "sh-1791647350546"]), ("l4", "Cortisol", "ak-cortisol-gng")])]
EXERCICIOS = [
 ("Provas UC03 (índice bq01)", [
   ("p1", "Mecanismo de ação de T3/T4: transportador, receptor nuclear, TRE; mutação de MCT8 (2024 P1 2.2; 2017 P1 3.7)", ["au-mct8", "ak-t3-nucleo", "sh-1791627550153", "ak-bmr"]),
   ("p2", "PPAR como receptor nuclear (2024 P4 1.3)", ["sh-1791627550027", "sh-1791627550277"]),
   ("p3", "Transdução da insulina: receptor tirosina quinase, IRS-1, cascata, GLUT (2017 P1 4.1)", ["ak-receptor-dimeriza", "ak-irs", "ak-pi3k", "sh-1791054011372"])]),
 ("Apostila de exercícios de Bioquímica (Mecanismos de ação hormonal)", [
   ("e1", "Solubilidade × local do receptor × modo de ação", ["ak-receptor-membrana", "ak-peptideo-rapido", "sh-1791627550027"]),
   ("e2", "Insulinoma: hiperinsulinemia, hipoglicemia, peptídeo C", ["ak-insulinoma-c", "au-diazoxido", "sh-1791729316389"]),
   ("e3", "Epinefrina: glicose no fígado, piruvato no músculo", ["sh-1791647349446", "sh-1791647350546", "sh-1791647350720"]),
   ("e4", "Receptores de membrana dos peptídeos e cascatas", ["ak-gs-ac", "ak-camp-pka", "sh-1791762411098"]),
   ("e5", "Hormônio tireoidiano e termogênese", "ak-bmr"), ("e6", "Caso: hipoglicemia e ganho de peso (insulinoma)", ["ak-insulinoma-c", "au-diazoxido"]),
   ("e7", "Depois das reservas, glicose por gliconeogênese (glucagon, cortisol)", ["sh-1791729320461", "ak-cortisol-gng"]),
   ("e8", "AMPc permeável no músculo: PKA, fosforilase", ["ak-camp-pka", "sh-1791731887453"])]),
]
