"""Inventário atômico de Radiografia e ultrassom — Princípios da radiografia convencional e da ultrassonografia (UC03 P1; Radiologia;
Preceptoria, João Vitor Dutra Vieira 2024 / transcrição de Raphael Oliveira 2023), escrito ANTES de escolher cards (16/10, pipeline v4).
Sequência = 41 lâminas de 2026 (fontes/slides.pdf). Lido inteiro nesta sessão: lâminas (visual/folha-01..07), transcrição integral (68 pp.),
lâminas III (2020: tubo, efeito biológico, artefatos), monitoria P1 (pp. 45–46), Grande Resumo P1 (pp. 45–46, mesmo texto), apostila guia de
Radiologia (aula 2, caps. 1–4), apostila ilustrativa, “Tudo que você precisa saber de RD”, apostila UC3 de veteranos (pp. 20–24),
bibliografia da aula 1 (física do RX) e da aula 2 (física do US), Mello cap. 1 (RX e US), e-book ESR caps. 1 e 2 (consulta), provas rad-02 (63).
Fronteira (MEMORY §3): a 02 Diagnóstico radiológico já tem forças/limites do RX e do US, termos por método, contraste por método, planos,
piezoelétrico, Doppler, radiação cumulativa e radioproteção → associados por sh(); aqui ficam física, imagem, densidades, incidências,
magnificação, silhueta, ecogenicidade, artefatos e FAST. TC (05), RM (12) e contrastes (56) ficam nas suas aulas.
"""
PREFIXO = "rd04"
AULA = "Radiografia e ultrassom (UC03 P1; Radiologia; Preceptoria)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Por que ainda usar radiografias? rápido, barato, acessível, leito", [("a1", "Vantagens do RX; triagem", "sh-1792141773857")]),
 (3, "conteudo", "Primórdios: Roentgen 1895, radiação X, Nobel 1901", [("a2", "História da descoberta", EXC + "história sem fato cobrado (nenhuma prova, nenhum acervo)")]),
 (4, "conteudo", "Radiações: energia em trânsito; partículas e ondas; fontes artificiais e naturais", [
   ("a3", "Fonte natural: radionuclídeos (radônio)", "ak-radon"), ("a4", "Fontes artificiais: reatores, radioterapia", "ak-exposicao")]),
 (5, "conteudo", "Raio X: onda eletromagnética de alta energia; λ 10^-12 m; espectro", [
   ("a5", "Espectro eletromagnético", "mc-espectro"), ("a6", "Energia ∝ frequência (alta energia, λ curto)", "mc-foton")]),
 (6, "conteudo", "Tubo de raios X: filamento de tungstênio aquecido, alvo de tungstênio, ânodo de cobre", [("a7", "Produção do RX no tubo", "au-tubo")]),
 (7, "conteudo", "Ampola de raios X (foto)", [("a8", "Ampola", "au-tubo")]),
 (8, "conteudo", "Esquema do aparelho: paciente entre fonte e detector", [("a9", "Fonte, paciente, detector; caixa de chumbo", "au-tubo")]),
 (9, "conteudo", "Analogia da sombra: fonte puntiforme, objeto, anteparo", [("a10", "Imagem é sombra projetada", "au-atenuacao")]),
 (10, "conteudo", "Produção da imagem: espessura e capacidade de absorção; densidades", [("a11", "Atenuação forma a imagem", "au-atenuacao")]),
 (11, "conteudo", "Densidades radiológicas: ar, gordura, água, cálcio, metal (ovo)", [("a12", "Cinco densidades em ordem", "au-densidades"),
   ("a13", "Termos radiopaco/radiotransparente", "sh-1792141774955")]),
 (12, "conteudo", "Densidades no abdome: nível hidroaéreo, prótese metálica", [("a14", "Cálcio e metal visíveis", ["ak-calculo-calcio", "ak-calculo-urico", "ak-ferro-aspirina"]),
   ("a15", "Ar a mais = hipertransparência", "ak-enfisema"), ("a16", "Ar a menos = hemitórax opaco", "ak-hemitorax"), ("a17", "Lesão radiotransparente (lítica)", "ak-mieloma")]),
 (13, "conteudo", "E quando as densidades são iguais? contraste (trânsito, angiografia)", [("a18", "Contraste exógeno: bário (TGI) e iodo (vasos)", ["sh-1792141768903", "sh-1792141769157"])]),
 (14, "conteudo", "Efeito biológico: direto (DNA), indireto (radicais da água), radioterapia, nem sempre dose-dependente, proteção", [
   ("a19", "Efeito indireto: radiólise da água → •OH", ["sh-1792117369271", "ak-radicais"]), ("a20", "Efeito direto no DNA", "ak-radicais"),
   ("a21", "Estocástico: sem limiar", "au-estocastico"), ("a22", "Cumulativo, teratogênico", "sh-1792141771005"),
   ("a23", "Proteção radiológica", ["sh-1792141771761", "sh-1792141772006"])]),
 (15, "conteudo", "Exercício prático: caixa com pedras, sementes e resina", [("a24", "Ilustração do exercício", EXC + "ilustração (o conceito está nas lâminas 16–24)")]),
 (16, "conteudo", "PA = vista de cima", [("a25", "Projeção perde uma dimensão", "ak-duas-incidencias")]),
 (17, "conteudo", "Perfil = vista de lado", [("a26", "Perfil mostra a profundidade", "ak-duas-incidencias")]),
 (18, "conteudo", "Planos e eixos do corpo", [("a27", "Planos", ["sh-1792141767554", "sh-1792141767807", "sh-1792141768057"])]),
 (19, "conteudo", "PA de tórax: paciente de frente ao detector", [("a28", "Incidência PA", "au-pa-ap")]),
 (20, "conteudo", "Perfil de tórax", [("a29", "Duas incidências para localizar", "ak-duas-incidencias")]),
 (21, "conteudo", "Pedras de tamanhos diferentes no RX", [("a30", "Magnificação", "au-magnificacao")]),
 (22, "conteudo", "Esquema: objeto longe do anteparo, sombra maior", [("a31", "Magnificação pela divergência", "au-magnificacao")]),
 (23, "conteudo", "PA × AP", [("a32", "AP aumenta o coração", "au-pa-ap")]),
 (24, "conteudo", "Mesma estrutura, quantidade de cimento diferente", [("a33", "Espessura/quantidade de material", "au-atenuacao")]),
 (25, "conteudo", "Tórax e abdome: aorta vista no tórax, não no abdome", [("a34", "Densidades diferentes lado a lado", "au-silhueta")]),
 (26, "conteudo", "Sinal da silhueta", [("a35", "Sinal da silhueta", "au-silhueta"), ("a36", "Átrio direito forma a borda direita", "ak-atrio-silhueta")]),
 (27, "conteudo", "Orientação: lado direito do paciente", [("a37", "Convenção de lateralidade", "au-orientacao")]),
 (28, "conteudo", "Ultrassonografia (foto)", [("a38", "Abertura do bloco", EXC + "capa de seção")]),
 (29, "conteudo", "Vantagens do US: não invasivo, sem radiação, Doppler, barato, leito", [("a39", "Vantagens", ["sh-1792141768558", "sh-1792141775531"]),
   ("a40", "Doppler", ["sh-1792141769904", "mc-doppler-perto", "mc-doppler-longe", "ext-doppler-cor"])]),
 (30, "conteudo", "Desvantagens: operador-dependente, obesidade, distensão gasosa", [("a41", "Limites", "sh-1792141768558"), ("a42", "Gás e osso atenuam", "ext-bamb")]),
 (31, "conteudo", "Onda mecânica que precisa de meio; infrassom, som, ultrassom", [("a43", "Precisa de meio", "mc-vacuo"), ("a44", "Ultrassom > 20 kHz", "mc-audivel"),
   ("a45", "Velocidade do som por meio", "mc-velocidade")]),
 (32, "conteudo", "Formação da imagem: transdutor piezoelétrico", [("a46", "Piezoelétrico emite e recebe", "sh-1792141768308"), ("a47", "Gel", "ext-gel")]),
 (33, "conteudo", "Pulso-eco: onda vai e reflete", [("a48", "Reflexão depende da impedância", "ext-impedancia")]),
 (34, "conteudo", "Aparelhos e transdutores", [("a49", "Frequência × resolução × penetração", "ext-frequencia"), ("a50", "Atenuação cresce com a frequência", "ext-atenuacao-us")]),
 (35, "conteudo", "Orientação transversal: DIR e ANT", [("a51", "Marcador do transdutor; topo = anterior", "ext-marcador")]),
 (36, "conteudo", "Orientação longitudinal: SUP e ANT", [("a52", "Corte longitudinal → sagital", "ext-marcador")]),
 (37, "conteudo", "Descritores: hiper, iso, hipo, anecogênicas", [("a53", "Termos de ecogenicidade", "sh-1792141774955"), ("a54", "Líquido é anecoico", "ak-cisto-renal")]),
 (38, "conteudo", "Sombra acústica posterior (cálculo na vesícula)", [("a55", "Sombra acústica", "au-sombra"), ("a56", "Cálculo biliar ao US", "sh-1792141766310")]),
 (39, "conteudo", "Reforço acústico posterior (cisto)", [("a57", "Reforço acústico", "au-reforco")]),
 (40, "conteudo", "FAST", [("a58", "FAST no trauma instável", "ak-fast-hemorragia"), ("a59", "FAST em trauma contuso ou penetrante", "ak-fast-trauma"),
   ("a60", "FAST não vê retroperitônio", "ak-fast-retro")]),
 (41, "logistica", "Obrigado", []),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "logistica": "agradecimento e e-mail"}
CAPITULO = [("Bibliografia da aula (física do RX e do US), Mello cap. 1, e-book ESR caps. 1–2 (confirmam)", [
 ("l1", "Tubo: tungstênio, emissão termoiônica, chumbo, óleo, vácuo, calor", "au-tubo"),
 ("l2", "Três processos: característica, frenagem, choque nuclear", "au-tubo"),
 ("l3", "Efeitos fotoelétrico e Compton, filme de prata, grade, dosimetria", EXC + "física acima do recorte da aula (nem lâmina, nem fala, nem prova)"),
 ("l4", "Impedância, atenuação, gel, frequência, 1540 m/s", ["ext-impedancia", "ext-atenuacao-us", "ext-gel", "ext-frequencia", "mc-velocidade"]),
 ("l5", "Ecogenicidade e artefatos (sombra, reforço; espelho, fantasma)", ["au-sombra", "au-reforco"]),
 ("l6", "Doppler colorido", ["sh-1792141769904", "ext-doppler-cor"])])]
EXERCICIOS = [
 ("Provas UC03 (índice rad-02)", [
   ("p1", "Mecanismo de formação do RX: filamento de tungstênio, atenuação, radiopaco (2024, 2023, 2018, 2017)", ["au-tubo", "au-atenuacao", "sh-1792141774955"]),
   ("p2", "Mecanismo do US: transdutor piezoelétrico emissor e receptor (2024, 2023, 2019, 2018)", "sh-1792141768308"),
   ("p3", "Doppler: mudança de frequência, velocidade e direção do fluxo (2024 P1)", ["sh-1792141769904", "mc-doppler-perto", "mc-doppler-longe"]),
   ("p4", "Por que PA e não AP (2015 P1)", ["au-pa-ap", "au-magnificacao"]),
   ("p5", "Sinal da silhueta para localizar a lesão (2019 P1)", ["au-silhueta", "ak-atrio-silhueta"]),
   ("p6", "Cálculo hiperecogênico com sombra (2015, 2023)", "au-sombra"),
   ("p7", "Cisto anecoico com reforço (2016 P1)", ["au-reforco", "ak-cisto-renal"]),
   ("p8", "Lesões radiotransparentes do mieloma (2024 P1)", "ak-mieloma"),
   ("p9", "Hiperinsuflação: hipertransparência, retificação, espaços intercostais (2025 P3)", "ak-enfisema"),
   ("p10", "Radioproteção: justificação, otimização, limitação (2017 P4)", ["sh-1792141771761", "sh-1792141772006"]),
   ("p11", "Vantagens do US e escolha da modalidade (2025, 2018, 2016, 2015)", ["sh-1792141768558", "sh-1792141775531", "sh-1792141766310"]),
   ("p12", "Termos por modalidade (2016, 2015)", "sh-1792141774955")]),
 ("Monitoria P1 e Grande Resumo P1 (aula 1)", [("m1", "Tungstênio, chumbo, óleo, vácuo, três processos", "au-tubo"), ("m2", "Cinco densidades; contraste", ["au-densidades", "sh-1792141769157"]),
   ("m3", "Efeito letal, teratogênico, cumulativo; feixe divergente", ["sh-1792141771005", "au-magnificacao"]), ("m4", "Mamografia comprime a mama", EXC + "aplicação lateral; mamografia não é objeto da aula"),
   ("m5", "Ecogenicidade e artefatos", ["sh-1792141774955", "au-sombra", "au-reforco"])]),
 ("Apostila guia de Radiologia (aula 2) e apostila UC3 de veteranos", [("v1", "Física do RX e do US", ["au-tubo", "sh-1792141768308", "mc-velocidade"]),
   ("v2", "Qualidade técnica do RX (penetração, inspiração, rotação) e hemitórax opaco", EXC + "interpretação de tórax: aulas de correlação; aqui só a ideia de opacidade (ak-hemitorax)"),
   ("v3", "Gel, isoecoico, sombra suja do gás", ["ext-gel", "au-sombra"])]),
 ("Apostila ilustrativa e “Tudo que você precisa saber de RD”", [("t1", "Nomenclatura obrigatória por método", "sh-1792141774955"), ("t2", "PA × AP; sombra e reforço", ["au-pa-ap", "au-sombra", "au-reforco"])]),
]
