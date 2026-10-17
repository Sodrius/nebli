"""Inventário atômico de Declaração de óbito: conceitos gerais (UC03 P1; Patologia; Prof. Luiz F. Ferraz da Silva), escrito ANTES de
escolher cards (17/10, pipeline v4). Sequência = 20 lâminas (fontes/slides.pdf; mesmo texto da versão da turma; a pasta pessoal da aula
está vazia), vistas inteiras nesta sessão (io/g0..g1). Lido nesta sessão: provas por termo (2019 P1 1.12, 2016 P2 2.12, 2016 P1 5.3),
monitoria P1 aula 4, apostila guia de Patologia Aula 5, apostila UC3 e o Manual de instruções da DO (Ministério da Saúde, bibliografia).
Sem transcrição (só vídeo, dispensado).
O AnKing não tem as regras da DO brasileira; os elos das cadeias causais dos casos (lâminas 7–16) entram com AnKing ou cópias NEBLI.
"""
PREFIXO = "pt14"
AULA = "Declaração de óbito: conceitos gerais (UC03 P1; Patologia)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Definição e relevância: base do SIM, certidão, estatísticas, vigilância",
  [("a1", "DO = documento base do SIM", "au-sim"), ("a2", "Base da certidão, das estatísticas e da vigilância", "au-sim")]),
 (3, "conteudo", "Quando assinar: adultos, nascidos vivos, óbito fetal ≥ 20 semanas e/ou ≥ 500 g",
  [("a3", "Óbito fetal ≥ 20 semanas ou ≥ 500 g", "au-quando"), ("a4", "Nascido vivo, qualquer peso ou idade gestacional", "au-quando")]),
 (4, "conteudo", "Quem assina na morte natural: com assistência (médico assistente/plantonista) × sem assistência (SVO)",
  [("a5", "Natural sem assistência → SVO", "au-natural"), ("a6", "Natural com assistência → médico que acompanhava", "au-natural")]),
 (5, "conteudo", "Quem assina na morte violenta: legista (IML) ou perito indicado", [("a7", "Morte violenta → IML", "au-violenta")]),
 (6, "conteudo", "Parte I (a imediata, b–c intermediárias, d básica) e Parte II", [("a8", "Causa básica na última linha", "au-parte-i"),
  ("a9", "Parte II: contribuintes fora da cadeia", "au-parte-ii")]),
 (7, "conteudo", "Caso 1: hipertensão sem tratamento → cardiopatia → ICC → edema agudo; câncer de próstata",
  [("a10", "Hipertensão crônica → insuficiência cardíaca", "ak-has-icfep"), ("a11", "IC esquerda → edema pulmonar", "sh-1791169086563")]),
 (8, "conteudo", "DO do caso 1 preenchida (com tempos)", [("a12", "Câncer de próstata na Parte II; tempos em cada linha", ["au-parte-ii", "au-parte-i"])]),
 (9, "conteudo", "Caso 2: esquistossomose → varizes → hematêmese → choque; diabetes",
  [("a13", "S. mansoni → hipertensão portal", "ak-schisto-portal"), ("a14", "Hipertensão portal → varizes", "sh-1791022175126"),
   ("a15", "Rotura das varizes → hematêmese", ["sh-1791022175254", "sh-1791022175426"]), ("a16", "Hemorragia → choque hipovolêmico", "ak-choque-hipovolemico")]),
 (10, "conteudo", "DO do caso 2 preenchida", [("a17", "PCR não entra; diabetes na Parte II", ["au-erros", "au-parte-ii"])]),
 (11, "conteudo", "Caso 3: Chagas com megacólon → volvo → peritonite → choque séptico",
  [("a18", "Chagas: megacólon e cardiopatia", "sh-1790972065836"), ("a19", "Volvo do sigmoide", "sh-1790974691357"),
   ("a20", "Ruptura intestinal → sepse por Gram-negativos", "ak-sepse-intestino")]),
 (12, "conteudo", "DO do caso 3 preenchida", [("a21", "Cardiopatia chagásica na Parte II", "au-parte-ii")]),
 (13, "conteudo", "Caso 4: diabético com COVID-19 → insuficiência respiratória", [("a22", "Coronavírus → SDRA", "ak-corona-sdra")]),
 (14, "conteudo", "DO do caso 4: SDRA ← COVID-19; diabetes na Parte II", [("a23", "SDRA como causa imediata", ["ak-corona-sdra", "ak-sdra"])]),
 (15, "conteudo", "Caso 5: COVID-19 prévio e aneurisma de aorta de 10 cm roto → choque", [("a24", "Aneurisma > 5 cm rompe", "ak-aaa-rotura"),
  ("a25", "Rotura: hipotensão, massa pulsátil, dor", "ak-aaa-triade")]),
 (16, "conteudo", "DO do caso 5: choque ← hemorragia ← aneurisma; COVID-19 na Parte II", [("a26", "COVID-19 não está na cadeia → Parte II", "au-parte-ii")]),
 (17, "conteudo", "Erros mais comuns: parada cardiorrespiratória, falência múltipla de órgãos", [("a27", "Modos de morrer não são causa", "au-erros")]),
 (18, "conteudo", "Campo 59: registrar ausência de sinais de violência", [("a28", "Campo 59", "au-natural")]),
 (19, "conteudo", "PS sem diagnóstico prévio; morte metatraumática (queda → fratura → broncopneumonia)",
  [("a29", "PS sem diagnóstico → SVO", "au-natural"), ("a30", "Morte metatraumática é violenta", "au-metatraumatica")]),
 (20, "logistica", "Imagem de humor", []),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "logistica": "imagem de humor sem conteúdo"}
CAPITULO = [("Manual de instruções para preenchimento da DO (Ministério da Saúde; bibliografia da aula)", [
 ("l1", "DO: base do SIM e da certidão", "au-sim"), ("l2", "Quando não emitir: feto < 20 semanas e < 500 g", "au-quando"),
 ("l3", "Causa básica: doença ou lesão que iniciou a cadeia", "au-parte-i"), ("l4", "Parte II", "au-parte-ii"),
 ("l5", "Morte violenta → IML; sem assistência → SVO", ["au-violenta", "au-natural"])])]
EXERCICIOS = [
 ("Provas UC03 (busca por termo)", [
   ("p1", "Preencher Parte I e II de um caso (2019 P1 1.12)", ["au-parte-i", "au-parte-ii"]),
   ("p2", "Primeira e última linha da Parte I após autópsia: AVC ← … ← diabetes (2016 P2 2.12)", "au-parte-i"),
   ("p3", "Autópsia: causa de morte, controle de qualidade, DO (2016 P1 5.3)", "au-natural")]),
 ("Monitoria P1 aula 4 e apostilas", [("m1", "Quem assina e quando", ["au-quando", "au-natural", "au-violenta"]),
                                     ("m2", "PCR e falência não entram", "au-erros")]),
]
