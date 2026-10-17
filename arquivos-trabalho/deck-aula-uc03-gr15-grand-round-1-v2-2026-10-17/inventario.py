"""Inventário atômico do Grand Round 1 — Esquizofrenia (UC03 P1; Elkis, Ferraz da Silva, Leite, Barbuto), escrito ANTES de escolher cards
(17/10, pipeline v4). Sequência = 57 lâminas (fontes/slides.pdf; mesmo texto do PDF da turma; o pptx pessoal é a mesma aula com vídeo),
vistas inteiras nesta sessão (io/g0..g4). Lido nesta sessão: apostila de veteranos “Grand Round 1” (resumo da fala, 5 pp.), índice de
provas gr-01 (2 itens comparativos de outros GR, sem item próprio) e busca por termo esquizofrenia (eco de AVC, não desta aula).
Atenção: a apostila diz que o alelo Val “resulta em mais dopamina na fenda”; a literatura da lâmina 27 (Egan 2001) diz o contrário
(Val = COMT mais ativa = menos dopamina pré-frontal) — seguida a literatura.
Fronteira (MEMORY §3): TC × RM (lâminas 14–20) é da 02 → sh(); micróglia derivada de fagócito mononuclear tem cópia viva da 62 → sh().
"""
PREFIXO = "gr15"
AULA = "Grand Round 1 — Esquizofrenia (UC03 P1)"
EXC = "EXC: "
_RD = EXC + "imagem de TC/RM para comparar métodos; a comparação TC × RM entra pelos cards da 02 (lâmina 20)"
_DF = "modelo multifatorial de Di Forte (lâminas 29–35)"

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Caso: 30 anos, esquizofrenia desde os 25, surto, risperidona sem melhora, isolado",
  [("a1", "Atípico (risperidona) é primeira linha", "ak-atipicos-1a-linha"), ("a2", "Refratário → clozapina", "ak-clozapina")]),
 (3, "conteudo", "Foto do paciente (vídeo)", [("a3", "Foto", EXC + "foto do paciente sem fato")]),
 (4, "conteudo", "Grupos de sintomas: psicóticos, negativos, cognitivos, humor, desorganização",
  [("a4", "Psicose: delírios, alucinações, desorganização", ["ak-psicose", "ak-delirio", "ak-alucinacao", "ak-desorganizado", "ak-ilusao", "ak-alucinacao-auditiva", "ak-alucinacao-visual"]),
   ("a5", "Negativos: embotamento, avolição", "ak-negativos"), ("a6", "Cognitivos: atenção, memória, abstração", "au-cognitivos"),
   ("a7", "Critérios diagnósticos", ["ak-criterios", "ak-def-6meses"])]),
 (5, "conteudo", "PANSS positiva (P1–P7)", [("a8", "Sintomas positivos", "ak-positivos")]),
 (6, "conteudo", "PANSS negativa (N1–N7)", [("a9", "Sintomas negativos", "ak-negativos")]),
 (7, "conteudo", "Evolução: pré-mórbido, pródromo, progressivo, crônico; neurodesenvolvimento → neurodegeneração", [("a10", "Fases", "au-curso")]),
 (8, "conteudo", "Evolução longitudinal de um caso (Lieberman)", [("a11", "Pródromo 14–17 anos; primeira internação aos 17", "au-curso"),
  ("a12", "Resposta parcial a antipsicóticos; evolução boa × má", ["ak-tipicos-negativos", "ak-prognostico"])]),
 (9, "conteudo", "Idade de início e gênero (Häfner)", [("a13", "Homens começam mais cedo; mulheres com 2º pico", ["au-inicio", "ak-sexo", "ak-prevalencia", "ak-raca"])]),
 (10, "conteudo", "Idade paterna avançada", [("a14", "Idade paterna", "au-idade-paterna")]),
 (11, "conteudo", "Evidências de neurodesenvolvimento (Howes & Murray)", [("a15", "Riscos perinatais", "au-neurodesenvolvimento"),
  ("a16", "Dilatação ventricular, menos substância cinzenta", ["ak-ventriculomegalia", "au-volume"])]),
 (12, "conteudo", "RM longitudinal após o primeiro episódio", [("a17", "Perda progressiva de volume", "au-volume")]),
 (13, "conteudo", "RM coronal: normal × esquizofrenia", [("a18", "Ventrículos dilatados", ["ak-ventriculomegalia", "ak-ex-vacuo", "ak-ex-vacuo-pic"])]),
 (14, "conteudo", "TC de crânio em três planos", [("a19", "Planos", _RD)]),
 (15, "conteudo", "TC de crânio sem contraste", [("a20", "TC", _RD)]),
 (16, "conteudo", "TC: ventrículos normais × dilatados (hidrocefalia)", [("a21", "Dilatação ventricular", "ak-ex-vacuo")]),
 (17, "conteudo", "TC × RM (T1, T2, FLAIR)", [("a22", "Sequências", _RD)]),
 (18, "conteudo", "TC × RM coronal", [("a23", "Comparação", _RD)]),
 (19, "conteudo", "Aparelhos de TC e RM", [("a24", "Aparelhos", _RD)]),
 (20, "conteudo", "Tabela TC × RM: radiação, campo, contraste, tempo, custo",
  [("a25", "Forças e limites", ["sh-1792141773206", "sh-1792141775531", "sh-1792141769157"])]),
 (21, "conteudo", "Homer", [("a26", "Humor", EXC + "imagem de humor")]),
 (22, "conteudo", "Volume cerebral: má × boa evolução (Khan)", [("a27", "Volume cai mais na má evolução", "au-volume")]),
 (23, "conteudo", "Agonistas e antagonistas dopaminérgicos (IMAO, reserpina, antipsicóticos)",
  [("a28", "Síntese da dopamina", "ak-sintese-da"), ("a29", "Anfetamina libera dopamina", "ak-anfetamina"),
   ("a30", "Antipsicóticos bloqueiam D2", ["ak-antipsicoticos-positivos", "ak-tipico-atipico"])]),
 (24, "conteudo", "Hipótese dopaminérgica: vias nigroestriatal, mesolímbica, tuberoinfundibular; D2 × D1",
  [("a31", "Vias e sintomas", ["ak-vias-sintomas", "ak-hipotese-da", "ak-dopamina"]),
   ("a32", "Mesolímbica → positivos", ["ak-mesolimbica-via", "ak-mesolimbica-positivos", "ak-alvo-mesolimbico"]),
   ("a33", "Mesocortical → negativos", ["ak-mesocortical-via", "ak-mesocortical-negativos", "ak-tipicos-negativos"]),
   ("a34", "Nigroestriatal → extrapiramidais", ["ak-nigro-via", "ak-nigro-eps"]),
   ("a35", "Tuberoinfundibular → prolactina", ["ak-tubero-via", "ak-tubero-prolactina"])]),
 (25, "conteudo", "Hiperatividade D2 mesolímbica × hipoatividade D1 cortical", [("a36", "D2 × D1", ["ak-mesolimbica-positivos", "ak-mesocortical-negativos"])]),
 (26, "conteudo", "Metabolismo da dopamina: MAO, COMT, 3-MT, DOPAC, HVA", [("a37", "COMT → 3-MT", "ak-comt-3mt"), ("a38", "MAO-B → DOPAC", "ak-maob-dopac"),
  ("a39", "HVA", "ak-hva")]),
 (27, "conteudo", "COMT em 22q, alelos Val e Met", [("a40", "Val × Met", "au-comt")]),
 (28, "conteudo", "Maconha aos 18 anos e risco de esquizofrenia (dose-resposta)", [("a41", "Maconha na adolescência", ["ak-maconha-teens", "ak-maconha-intox"])]),
 (29, "conteudo", "Modelo multifatorial: desenvolvimento precoce → ansiedade social → desregulação dopaminérgica → psicose",
  [("a42", "Modelo", ["au-neurodesenvolvimento", "ak-hipotese-da"])]),
 (30, "conteudo", "Destaque: complicações obstétricas e genes", [("a43", "Fatores precoces", "au-neurodesenvolvimento")]),
 (31, "conteudo", "Destaque: déficit cognitivo, motor e social", [("a44", "Déficit precoce", "au-curso")]),
 (32, "conteudo", "Destaque: ansiedade social crônica", [("a45", "Ansiedade social", EXC + "etapa do " + _DF + ", sem fato próprio")]),
 (33, "conteudo", "Destaque: drogas de abuso", [("a46", "Maconha", "ak-maconha-teens")]),
 (34, "conteudo", "Destaque: neurotransmissores e genes (COMT)", [("a47", "COMT", "au-comt")]),
 (35, "conteudo", "Destaque: desregulação dopaminérgica", [("a48", "Dopamina", "ak-dopamina")]),
 (36, "conteudo", "Atrofia cortical progressiva após clozapina (Ahmed 2015)", [("a49", "Perda progressiva", "au-volume")]),
 (37, "conteudo", "Neurônio esquizofrênico: soma menor, menos espinhas, dendritos curtos, menos terminais",
  [("a50", "Menos espinhas e ramificação", ["au-espinhas", "ak-ramificacao", "ak-serotonina"])]),
 (38, "conteudo", "Vias da apoptose (Glantz)", [("a51", "Apoptose sináptica", "au-espinhas")]),
 (39, "conteudo", "Apoptose focal no terminal sináptico", [("a52", "Apoptose focal", "au-espinhas")]),
 (40, "conteudo", "Volume cerebral × marcadores inflamatórios (Müller)", [("a53", "IL-1β e micróglia", "au-inflamacao")]),
 (41, "conteudo", "Artigos: neuroinflamação, micróglia, citocinas, TLR4", [("a54", "Micróglia ativada", ["ak-microglia-ativada", "sh-1791983681660", "au-microglia-poda"])]),
 (42, "conteudo", "Artigos: IgM natural, complemento, IL-6 e exercício", [("a55", "Exercício reduz IL-6", "au-inflamacao")]),
 (43, "conteudo", "Medawar 1948: enxerto no cérebro sobrevive (privilégio imunológico)", [("a56", "Privilégio imune do SNC", "au-privilegio")]),
 (44, "conteudo", "Papel dos linfáticos; drenagem do SNC", [("a57", "Linfáticos meníngeos", "au-linfaticos")]),
 (45, "conteudo", "Duas etapas: sensibilização → resposta", [("a58", "Sensibilização prévia quebra o privilégio", "au-privilegio")]),
 (46, "conteudo", "Mas a comunicação é bidirecional!", [("a59", "Cérebro ↔ imunidade", "au-inflamacao")]),
 (47, "conteudo", "DC reconhecem estresse emocional (camundongos)", [("a60", "Estresse ativa DC", EXC + "experimento animal ilustrativo; a ideia bidirecional está em au-inflamacao")]),
 (48, "conteudo", "Antecipação de infecção virtual ativa resposta imune", [("a61", "Experimento", EXC + "estudo ilustrativo sem fato cobrado")]),
 (49, "secao", "O estigma da esquizofrenia", []),
 (50, "conteudo", "Frases com uso pejorativo de esquizofrenia", [("a62", "Uso pejorativo", "au-estigma")]),
 (51, "conteudo", "Llosa chama de esquizofrênico", [("a63", "Uso pejorativo", "au-estigma")]),
 (52, "conteudo", "Pessoas notáveis com doença mental", [("a64", "Contribuição", "au-estigma")]),
 (53, "conteudo", "Brian Wilson (Beach Boys)", [("a65", "Caso ilustrativo", EXC + "biografia ilustrativa; diagnóstico em ak-esquizoafetivo")]),
 (54, "conteudo", "Brian Wilson: início, tentativas de suicídio, drogas", [("a66", "Suicídio e clozapina", "ak-clozapina-suicidio")]),
 (55, "conteudo", "Brian Wilson: tratamento, transtorno esquizoafetivo", [("a67", "Esquizoafetivo", ["ak-esquizoafetivo", "ak-esquizoafetivo-2sem", "ak-psicose-humor"])]),
 (56, "conteudo", "Vídeo (quadro preto)", [("a68", "Vídeo", EXC + "quadro de vídeo sem conteúdo")]),
 (57, "conteudo", "Morte de Brian Wilson (Reuters)", [("a69", "Notícia", EXC + "notícia sem fato")]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "secao": "título de seção"}
CAPITULO = [("Apostila de veteranos “Grand Round 1” (resumo da fala)", [
 ("l1", "Delírio × alucinação; delirium é outra coisa", ["ak-delirio", "ak-alucinacao"]),
 ("l2", "Positivos = acima do basal; negativos = abaixo", ["ak-positivos", "ak-negativos"]),
 ("l3", "Fases e associações pré-mórbidas", "au-curso"), ("l4", "Mulheres: 2º pico aos 45", "au-inicio"),
 ("l5", "D2 mesolímbico × D1 frontal", ["ak-mesolimbica-positivos", "ak-mesocortical-negativos"]), ("l6", "COMT", "au-comt"),
 ("l7", "Atrofia, ventrículos, perda de botões por apoptose focal", ["ak-ventriculomegalia", "au-espinhas"]),
 ("l8", "Micróglia e exercício", ["au-microglia-poda", "au-inflamacao"]), ("l9", "Estigma", "au-estigma")])]
EXERCICIOS = []  # índice gr-01: só itens comparativos de outros GR (2025 P4 1.4, 2024 P2 1.17); nenhum item próprio desta aula
