"""Inventário do Grand Round 1, Esquizofrenia (UC03 P1; 57 lâminas = pptx pessoal = PDF da turma), escrito antes da seleção (14/10).
Material: lâminas (sem transcrição nem exercícios na pasta), provas por termo (sem item de esquizofrenia; fontes/provas-gr01.txt e provas-esquizofrenia.txt)."""
PREFIXO = "gr15"
AULA = "Grand Round 1, Esquizofrenia (UC03 P1)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
P = ("Psicose (modelo)", "c-modelo")
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Caso clínico #1", [("a1", "Surto psicótico", "ak-psicose"), ("a2", "Risperidona sem melhora", "ak-clozapina"), ("a3", "Isolado", "a-sintomas"), ("a3b", "Delírio, alucinação, delirium", ["ak-delirio", "a-alucinacao", "ak-delirium"])]),
 (3, "conteudo", "Caso (vídeo)", [("a4", "Paciente", EXC + "vídeo")]),
 (4, "conteudo", "Grupos de sintomas", [("a5", "Positivos, negativos, cognitivos", ["a-sintomas", "a-avolicao"])]),
 (5, "conteudo", "PANSS positiva", [("a6", "Escala", EXC + "nome de escala clínica; Tab (revisão 15/10)")]),
 (6, "conteudo", "PANSS negativa", [("a7", "Escala", EXC + "nome de escala clínica; Tab (revisão 15/10)")]),
 (7, "conteudo", "Evolução", [("a8", "Estágios", "a-estagios")]),
 (8, "conteudo", "Evolução de um caso", [("a9", "Pré-mórbido a crônico", "a-estagios")]),
 (9, "conteudo", "Idade de início e sexo", [("a10", "Homens mais cedo", ["a-sexo", "a-mulheres"])]),
 (10, "conteudo", "Idade paterna", [("a11", "Risco", ["a-neurodesenvolvimento", "a-idade-paterna", "a-herdabilidade"])]),
 (11, "conteudo", "Neurodesenvolvimento", [("a12", "Riscos pré e perinatais", "a-neurodesenvolvimento"), ("a13", "Dilatação ventricular", "ak-ventriculos")]),
 (12, "conteudo", "RM após primeiro episódio", [("a14", "Perda progressiva", "ak-ventriculos")]),
 (13, "conteudo", "Anormalidades estruturais", [("a15", "Ventrículos", "ak-ventriculos")]),
 (14, "conteudo", "TC de crânio: planos", [("a16", "Revisão", EXC + "Radiologia 05")]),
 (15, "conteudo", "TC sem contraste", [("a17", "Revisão", EXC + "Radiologia 05")]),
 (16, "conteudo", "Hidrocefalia", [("a18", "Ventrículos dilatados", "ak-ventriculos")]),
 (17, "conteudo", "TC × RM (T1, T2, FLAIR)", [("a19", "FLAIR", S(1792028343886))]),
 (18, "conteudo", "TC × RM coronal", [("a20", "Revisão", EXC + "Radiologia 12")]),
 (19, "conteudo", "Aparelhos", [("a21", "Revisão", EXC + "Radiologia 02")]),
 (20, "conteudo", "Tabela TC × RM", [("a22", "Radiação", S(1791810579895))]),
 (21, "conteudo", "Homer", [("a23", "Humor", EXC + "ilustração")]),
 (22, "conteudo", "Volume cerebral", [("a24", "Perda", "ak-ventriculos")]),
 (23, "conteudo", "Agonistas e antagonistas", [("a25", "Antipsicóticos bloqueiam D2", "ak-alvo")]),
 (24, "conteudo", "Vias dopaminérgicas", [("a26", "Mesolímbica, nigroestriatal, tuberoinfundibular", ["ak-vias", "ak-nigro", "ak-tubero"])]),
 (25, "conteudo", "Hipótese dopaminérgica", [("a27", "D2 e D1", ["c-d1-d2", "ak-negativos", "c-glutamato", "c-anfetamina"])]),
 (26, "conteudo", "Metabolismo da dopamina", [("a28", "COMT, MAO", ["ak-comt", "ak-hva"])]),
 (27, "conteudo", "COMT Val/Met", [("a29", "Alelos", "c-comt-val")]),
 (28, "conteudo", "Maconha", [("a30", "Dose-resposta", "ak-maconha")]),
] + [(n, "conteudo", "Modelo do desenvolvimento (animação)", [(f"a{n+2}", "Fatores precoces e proximais", "c-modelo")]) for n in range(29, 36)] + [
 (36, "conteudo", "Atrofia após clozapina", [("a38", "Clozapina", "ak-clozapina")]),
 (37, "conteudo", "Patologia sináptica", [("a39", "Espinhas", "d-espinhas")]),
 (38, "conteudo", "Vias de apoptose", [("a40", "Revisão", EXC + "aula 09")]),
 (39, "conteudo", "Apoptose na sinapse", [("a41", "Sinapse", "d-espinhas")]),
 (40, "conteudo", "Volume e imunidade", [("a42", "IL-1β", "d-il1")]),
 (41, "conteudo", "Neuroinflamação (artigos)", [("a43", "Microglia", ["d-il1", "d-cadeia-sinapse", "d-microglia"])]),
 (42, "conteudo", "Imunidade e cognição", [("a44", "IL-6, exercício", ["d-il1", "d-exercicio"])]),
 (43, "conteudo", "Medawar", [("a45", "Privilégio", ["d-privilegio", "d-sitios"])]),
 (44, "conteudo", "Linfáticos", [("a46", "Drenagem", "d-linfaticos")]),
 (45, "conteudo", "Duas etapas", [("a47", "Sensibilização e resposta", "d-privilegio")]),
 (46, "conteudo", "Comunicação bidirecional", [("a48", "Bidirecional", "d-linfaticos")]),
 (47, "conteudo", "DC e estresse emocional", [("a49", "Estudo", "d-estresse-dc")]),
 (48, "conteudo", "Infecção virtual", [("a50", "Estudo", EXC + "pesquisa; Tab")]),
 (49, "conteudo", "Estigma", [("a51", "Abertura", "a-estigma")]),
 (50, "conteudo", "Frases", [("a52", "Estigma", "a-estigma")]),
 (51, "conteudo", "Llosa", [("a53", "Estigma", EXC + "Tab")]),
 (52, "conteudo", "Pessoas célebres", [("a54", "Estigma", EXC + "Tab")]),
 (53, "conteudo", "Brian Wilson", [("a55", "Carreira", EXC + "Tab")]),
 (54, "conteudo", "Brian Wilson: doença", [("a56", "Curso", EXC + "Tab")]),
 (55, "conteudo", "Brian Wilson: tratamento", [("a57", "Esquizoafetivo", "ak-esquizoafetivo")]),
 (56, "conteudo", "Vídeo", [("a58", "Vídeo", EXC + "vídeo")]),
 (57, "conteudo", "Morte de Brian Wilson", [("a59", "Notícia", EXC + "Tab")]),
]
JUSTIFICATIVAS = {1: "capa"}
CAPITULO = [("Lâminas do GR (sem bibliografia própria)", [("l1", "Hipótese dopaminérgica (Javitt & Laruelle)", "ak-vias"), ("l2", "Modelo (Di Forti/Murray)", "c-modelo")])]
EXERCICIOS = [("Provas UC03", [("p1", "gr-01: só itens eco de outros GRs; nenhum de esquizofrenia", "ak-psicose")])]
