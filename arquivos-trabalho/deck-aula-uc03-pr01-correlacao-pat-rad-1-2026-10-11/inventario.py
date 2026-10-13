"""Inventário atômico de Correlação patológica-radiológica 1 (UC03 P1, Patologia + Radiologia, aula 06), escrito antes da seleção.
Material de base lido inteiro: lâminas Ia (33, caso 1) e Ib (43, casos 1 e 2; só imagens; vistas em visual/folha-01 a 05 e visual/pg),
provas pelo índice pat-rad-01 (12 subquestões 2015–2025), apostilas de veteranos (Guia de Radiologia aula 2, Tudo que você precisa saber de RD,
Guia de Patologia aula 6), Robbins Bases Patológicas cap. 15 (enfisema, pneumonia, pleura) e cap. 21 (seminoma). Não há transcrição,
bibliografia nem palavras-cruzadas na pasta da turma desta aula; a monitoria P1 de Patologia e a de Radiologia não têm seção desta aula.
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina). Menção no verso não conta.
"""
PREFIXO = "pr01"
AULA = "Correlação patológica-radiológica 1 (UC03 P1; Patologia + Radiologia)"
EXC = "EXC: "
JUSTIFICATIVAS = {}
S = lambda n: f"sh-{n}"
INCID, HIPER, PERFIL = S(1791810586046), S(1791844788752), S(1791844792172)
SIL, SILPN, ANEC = S(1791844797227), S(1791844797478), S(1791844801330)
ANTRA, EXSUD, EMPI = S(1791592721894), S(1791169089006), S(1791577164590)
CAPA = EXC + "título/encerramento sem conteúdo"

SLIDES = [
 (1, "capa", "Capa (Correlação radiologia + patologia, parte I)", []),
 (2, "conteudo", "Caso 1: homem de 60 anos, tabagista 30 anos-maço, tosse com expectoração amarelada e febre", [
   ("c1", "Tabagismo como causa do enfisema do caso", "enfisema-tabaco")]),
 (3, "conteudo", "Radiografia de tórax (título)", [("c2", "Radiografia em PA e perfil como primeiro exame", INCID)]),
 (4, "conteudo", "Zonas de leitura da radiografia (campos, mediastino, hilos, seios)", [
   ("c3", "Áreas brancas = hiperatenuantes", HIPER), ("c4", "Seios costofrênicos livres no normal", "costofrenico")]),
 (5, "conteudo", "PA normal com contornos do mediastino rotulados", [
   ("c5", "Borda direita = átrio direito; borda esquerda = ventrículo esquerdo", "bordas-cardiacas"),
   ("c6", "Faixa paratraqueal, recesso ázigo-esofágico, linhas paravertebrais", EXC + "anatomia radiológica fina da aula 04 Radiografia; sem uso no caso")]),
 (6, "conteudo", "Perfil normal: hemidiafragmas e pulmão mais radiotransparente embaixo", [
   ("c7", "Coluna fica mais escura em direção ao diafragma", "perfil-coluna"),
   ("c8", "Porção anterior do hemidiafragma esquerdo apagada pelo coração", "perfil-hemidiafragma")]),
 (7, "conteudo", "Hilos direito e esquerdo no perfil", [("c9", "Forma dos hilos no perfil", EXC + "anatomia radiológica da aula 04; não usada nos casos")]),
 (8, "conteudo", "Radiografia de 6 meses antes: enfisema", [
   ("c10", "Aumento do diâmetro AP e diafragma retificado", "enfisema-rx"), ("c11", "Hipertransparência", "enfisema-lucencia"),
   ("c12", "Hipertransparência = paredes destruídas, mais ar", "enfisema-correlacao")]),
 (9, "conteudo", "TC sem contraste: enfisema com bolhas", [("c13", "Bolhas na TC", "tc-bolhas"), ("c14", "Predomínio em lobos superiores", "enfisema-tabaco")]),
 (10, "conteudo", "Peça: pulmões hiperinsuflados e pigmentados", [("c15", "Pigmento antracótico", ANTRA)]),
 (11, "conteudo", "Peça: bolhas de enfisema", [("c16", "Bolha > 1 cm", "bolha-def")]),
 (12, "conteudo", "Peça: bolhas subpleurais", [("c17", "Bolhas na superfície pleural", "bolha-def")]),
 (13, "conteudo", "Peça: corte do pulmão com hemorragia/consolidação", [("c18", "Repete a peça do caso", EXC + "mesma peça das lâminas 10–12 com outro corte; coberta pelos cards de enfisema e pneumonia")]),
 (14, "conteudo", "Histologia do pulmão normal", [("c19", "Referência normal para comparar", "histo-enfisema")]),
 (15, "conteudo", "Histologia do enfisema", [("c20", "Espaços aumentados, septos rotos", ["histo-enfisema", "enfisema-aumento", "enfisema-destruicao"])]),
 (16, "conteudo", "Esquema de alvéolos dilatados", [("c21", "Ilustração", EXC + "esquema ilustrativo do enfisema; coberto pela histologia")]),
 (17, "conteudo", "Radiografia na entrada do PA: opacidade retrocardíaca esquerda", [("c22", "Consolidação", "consolidacao-def")]),
 (18, "conteudo", "Comparação 6 meses antes × atual", [("c23", "Comparar com exame anterior", "comparar-previo")]),
 (19, "conteudo", "Ultrassom: derrame pleural", [("c24", "Derrame anecoico acima do diafragma", ["us-derrame", ANEC])]),
 (20, "conteudo", "TC: derrame pleural esquerdo com pulmão colabado", [("c25", "Derrame posterior", "tc-derrame"), ("c26", "Atelectasia compressiva", "atelectasia-compressiva")]),
 (21, "conteudo", "Citologia do líquido pleural: neutrófilos", [("c27", "Exsudato infectado", ["derrame-neutrofilos", EXSUD, EMPI])]),
 (22, "conteudo", "Citologia: aglomerados de células epiteliais", [("c28", "Natureza dos aglomerados", EXC + "sem transcrição não é possível afirmar se são células malignas ou mesoteliais; pergunta ao Davi")]),
 (23, "conteudo", "Sinal do menisco", [("c29", "Sinal do menisco", "menisco"), ("c30", "Velamento do seio costofrênico", "costofrenico")]),
 (24, "conteudo", "Comparação 6 meses antes × atual (derrame)", [("c31", "Novo derrame ao comparar", "comparar-previo")]),
 (25, "conteudo", "Sinal da silhueta (esquema: lobo inferior × língula)", [("c32", "Definição", [SIL, SILPN]), ("c33", "Lobo inferior apaga o diafragma", "silhueta-lobo-inferior")]),
 (26, "conteudo", "Anatomia dos lobos e da língula", [("c34", "Língula no pulmão esquerdo", "lingula"), ("c35", "Lobo médio direito", "silhueta-lobo-medio")]),
 (27, "conteudo", "Opacidade da língula: apaga a borda cardíaca esquerda", [("c36", "Língula", "silhueta-lingula"), ("c37", "Perfil localiza", PERFIL)]),
 (28, "conteudo", "Opacidade do lobo inferior esquerdo: apaga o diafragma", [("c38", "Lobo inferior", "silhueta-lobo-inferior")]),
 (29, "conteudo", "Peça: pneumonia lobar (hepatização)", [("c39", "Hepatização cinzenta", "pn-hep-cinzenta")]),
 (30, "conteudo", "Histologia: alvéolos com exsudato (fases)", [
   ("c40", "Consolidação = alvéolos com neutrófilos", "pn-exsudato"), ("c41", "Hepatização vermelha", "pn-hep-vermelha")]),
 (31, "conteudo", "Histologia: neutrófilos no alvéolo", [("c42", "Exsudato intra-alveolar", "pn-exsudato")]),
 (32, "conteudo", "Caso 2: homem de 20 anos com aumento testicular há 6 meses", [("c43", "Massa testicular no jovem", "nodulo-hipoecoico")]),
 (33, "conteudo", "Ultrassom do testículo normal e anatomia do epidídimo", [
   ("c44", "Ecotextura homogênea", "us-testiculo-normal"), ("c45", "Anatomia do epidídimo", EXC + "anatomia da UC de reprodução; referência para o ultrassom")]),
 (34, "conteudo", "Doppler do testículo", [("c46", "Fluxo no parênquima", "doppler-nodulo")]),
 (35, "conteudo", "Ultrassom: nódulo hipoecoico intratesticular", [("c47", "Nódulo sólido hipoecoico suspeito", "nodulo-hipoecoico")]),
 (36, "conteudo", "Doppler colorido do nódulo", [("c48", "Fluxo = lesão sólida vascularizada", "doppler-nodulo")]),
 (37, "conteudo", "Peça: testículo com tumor", [("c49", "Seminoma é o mais comum", "seminoma-comum")]),
 (38, "conteudo", "Peça: corte do seminoma", [("c50", "Massa homogênea sem hemorragia", "seminoma-macro")]),
 (39, "conteudo", "Histologia do testículo normal", [("c51", "Túbulos seminíferos", EXC + "histologia normal (UC02) para comparar; o alvo é o seminoma")]),
 (40, "conteudo", "Histologia do seminoma", [("c52", "Células claras em lâminas, septos com linfócitos", "seminoma-histo")]),
 (41, "conteudo", "Por que radiografia de tórax?", [("c53", "Pesquisar metástase pulmonar", "rx-metastase")]),
 (42, "capa", "Dúvidas", []),
 (43, "capa", "Obrigado", []),
]
CAPITULO = [("Robbins, Bases Patológicas das Doenças, cap. 15 (enfisema, pneumonia, pleura) e cap. 21 (seminoma)", [
  ("l1", "Enfisema: aumento permanente dos espaços aéreos distais com destruição das paredes, sem fibrose", ["enfisema-aumento", "enfisema-destruicao"]),
  ("l2", "Tabagismo → enfisema centroacinar, dois terços superiores", "enfisema-tabaco"),
  ("l3", "Enfisema bolhoso: bolhas subpleurais > 1 cm", "bolha-def"),
  ("l4", "Microscopia: alvéolos grandes separados por septos delgados", "histo-enfisema"),
  ("l5", "Pneumonia lobar: congestão, hepatização vermelha, hepatização cinzenta, resolução", ["pn-hep-vermelha", "pn-hep-cinzenta"]),
  ("l6", "Exsudato intra-alveolar de neutrófilos", ["pn-exsudato", "consolidacao-def"]),
  ("l7", "Derrames pleurais inflamatórios (exsudato, empiema) e não inflamatórios", [EXSUD, EMPI]),
  ("l8", "Seminoma: o tumor de células germinativas mais comum; massa homogênea cinza-esbranquiçada sem hemorragia ou necrose", ["seminoma-comum", "seminoma-macro"]),
  ("l9", "Seminoma: lâminas de células uniformes claras, septos com linfócitos", "seminoma-histo"),
  ("l10", "Patogenia do enfisema (proteases, α1-antitripsina, TH17)", EXC + "mecanismo molecular fora desta aula de correlação; o caso é de tabagista"),
  ("l11", "Agentes e formas clínicas das pneumonias", EXC + "microbiologia e clínica das pneumonias pertencem às aulas de Patogenicidade e às UCs clínicas"),
  ("l12", "Marcadores, estadiamento e vias de metástase dos tumores testiculares", EXC + "aulas 17–24 de tumores (P3)")])]
EXERCICIOS = [
 ("Provas UC03 (índice pat-rad-01, 12 subquestões 2015–2025)", [
  ("p1", "Descrever a lesão: opacidade/condensação no campo pulmonar", "consolidacao-def"),
  ("p2", "Nome das áreas mais brancas na radiografia: hiperatenuantes", HIPER),
  ("p3", "Derrame pleural puncionado no caso de pneumonia", ["derrame-neutrofilos", EXSUD]),
  ("p4", "Pneumonia secundária ao enfisema", ["enfisema-rx", "consolidacao-def"]),
  ("p5", "Pneumonia do caso em contexto de poluição/idade (mecanismos nas aulas de Patologia ambiental e Envelhecimento)", "pn-exsudato")]),
 ("Apostilas de veteranos (Guia de Radiologia aula 2; Tudo que você precisa saber de RD; Guia de Patologia aula 6)", [
  ("v1", "Opacidade, hipertransparência e consolidação", ["consolidacao-def", "enfisema-lucencia"]),
  ("v2", "Ângulo costofrênico opaco e forma de menisco no derrame", ["costofrenico", "menisco"]),
  ("v3", "Transudato × exsudato; empiema rico em neutrófilos", [EXSUD, EMPI])])]
