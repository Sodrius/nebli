"""Inventário atômico de Inflamação crônica (UC03 P3, Patologia; lâminas I Mauad (30) e II Ferraz da Silva (20)), escrito antes da seleção (14/10).
Material de base lido inteiro: lâminas I e II (visual/folha-01..05, II-01..02), exercícios (7) e palavras-cruzadas (20), provas pat-10
(7 subquestões 2015–2025), monitoria P3 de Patologia aula 10 e apostila cap. 8, Robbins cap. 2 pp. 70–73. A “transcrição” da pasta pessoal
e o Material Complementar II são o texto das próprias lâminas II (sem fala). Cada ideia aponta para chave do spec, "sh-<nid>" ou "EXC: motivo".
"""
PREFIXO = "pt62"
AULA = "Inflamação crônica (UC03 P3; Patologia; Mauad e Ferraz da Silva)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"

SLIDES = [
 (1, "capa", "Capa (Thais Mauad, 2020)", []),
 (2, "conteudo", "O problema da inflamação é não cessar (Nathan & Ding)", [
   ("a1", "Inflamação não resolvida é o problema central", "ic-nao-resolvida"),
   ("a2", "Contribui para aterosclerose, obesidade, câncer, DPOC, asma, DII, AR", EXC + "lista de doenças ilustrativa; Extra/Tab do princípio")]),
 (3, "conteudo", "Esquema: lesão tecidual → produtos → detecção → inflamação", [
   ("a3", "Produtos do tecido lesado realimentam a inflamação", "ic-nao-resolvida"),
   ("a4", "Morte apoptótica inibe a detecção (linha verde)", EXC + "detalhe do esquema; resolução é da aula 37")]),
 (4, "conteudo", "Duração prolongada, destruição, tentativa de reparo, nem sempre após aguda", [
   ("a5", "Duração prolongada (tempo exato?)", "ic-duracao"), ("a6", "Destruição tissular e tentativa de reparo coexistem", "ic-duracao"),
   ("a7", "Pode ser insidiosa (virais)", "ic-insidiosa")]),
 (5, "conteudo", "Causas mais comuns", [
   ("a8", "Infecções persistentes (TB, fungos, sífilis, vírus)", "ak-causa-infeccao"),
   ("a9", "Hipersensibilidade tardia → granulomas; citotoxicidade T", S(1791716405167)),
   ("a10", "Exposição prolongada a tóxicos (sílica; aterosclerose)", "ic-causas"),
   ("a11", "Autoimunidade: reação perpetuante (AR)", "ic-causas"), ("a12", "Doenças imunomediadas: alérgicos, asma", "ic-causas")]),
 (6, "conteudo", "Histologia: mononucleares, destruição, cicatrização (vasos e fibrose)", [
   ("a13", "Tríade da inflamação crônica", "ic-cid"), ("a14", "Infiltrado de linfócitos e macrófagos", "ak-celulas")]),
 (7, "conteudo", "Inflamação aguda × crônica (Robbins)", [("a15", "Padrões histológicos comparados", "ak-celulas")]),
 (8, "conteudo", "Artrite reumatoide (mão; sinóvia com folículos)", [("a16", "AR como exemplo de inflamação crônica com folículos", "terciario"),
   ("a17", "Foto da mão", EXC + "foto clínica ilustrativa")]),
 (9, "conteudo", "Bronquiectasias (histologia e peça)", [("a18", "Destruição e fibrose dilatando brônquios", "ak-bronquiectasia")]),
 (10, "conteudo", "Minas de sericita, Paraná", [("a19", "Exposição ocupacional à sílica", EXC + "exemplo ilustrativo; Extra de ic-causas (silicose é da 47)")]),
 (11, "conteudo", "Bronquite crônica pelo cigarro", [("a20", "Inflamação crônica pelo cigarro", "neutro-cronico")]),
 (12, "conteudo", "Infiltrado misto: plasmócitos, macrófagos, eosinófilos", [("a21", "Células do infiltrado misto", "ak-celulas")]),
 (13, "conteudo", "Macrófago: principal célula; origem na medula", [("a22", "Principal célula", "mac-principal"), ("a23", "Origem medular (monócito)", "ak-monocito")]),
 (14, "conteudo", "Macrófago: migra na aguda; ativado por TLR, IFN-γ, fibronectina; ↑tamanho, enzimas, metabolismo, fagocitose", [
   ("a24", "Ativadores (produtos bacterianos/TLR, IFN-γ)", S(1791625430208)), ("a25", "Efeitos da ativação", S(1791716411025)),
   ("a26", "Fibronectina como ativador", "mac-fibronectina")]),
 (15, "conteudo", "Sistema fagocítico mononuclear; vida média 1 dia × meses", [("a27", "Sistema fagocítico mononuclear", "mac-sfm"), ("a28", "Vida média", "mac-vida")]),
 (16, "conteudo", "Localizações anatômicas dos macrófagos", [("a29", "Kupffer no fígado", "ak-kupffer"), ("a30", "Micróglia", "ak-microglia"),
   ("a31", "Demais (alveolar, osteoclasto, histiócito)", ["sh-1791147097386", "mac-osteoclasto"])]),
 (17, "conteudo", "Ativação clássica (M1) × alternativa (M2)", [("a32", "Indutores M1 × M2", "mac-m1m2"), ("a33", "M1 pró-inflamatório", S(1791625434032)),
   ("a34", "M2 anti-inflamatório", S(1791625434457)), ("a35", "M1: ROS, NO, enzimas", "mac-m1-no"), ("a36", "M2: fatores de crescimento, TGF-β → reparo/fibrose", "mac-m2-tgf")]),
 (18, "conteudo", "Substâncias secretadas pelos macrófagos", [("a37", "Elastases, proteases, colagenase: destruição", "mac-destroi"),
   ("a38", "Metabólitos do oxigênio", S(1791716414575)), ("a39", "Citocinas, quimiocinas, complemento: recrutamento", "mac-recruta"),
   ("a40", "Fatores de crescimento", ["ak-tgf", "ak-pdgf"]), ("a41", "Fatores de coagulação, lipase, NO", EXC + "itens da lista sem papel próprio na aula; Extra de mac-destroi")]),
 (19, "conteudo", "Destino do macrófago", [("a42", "Limitada: morte e drenagem linfática", "mac-limitada"),
   ("a43", "Persistente: recrutamento, proliferação local, imobilização (MIF)", "mac-persiste")]),
 (20, "conteudo", "Linfócitos B e T ativados via macrófagos; IFN-γ", [("a44", "Apresentação e coestimulação", S(1791625428533)), ("a45", "IFN-γ dos linfócitos ativa macrófagos", "lin-circuito")]),
 (21, "conteudo", "Imunidade inata e adaptativa na inflamação crônica (Th1–macrófago)", [("a46", "Interação bidirecional por citocinas", "lin-circuito")]),
 (22, "conteudo", "Tipos de linfócitos: Th1, Th2, Th17", [("a47", "Th1 ativa macrófagos", S(1791625422657)), ("a48", "Th2: alérgico/antiparasitário", S(1791625432007)),
   ("a49", "Th17: neutrófilos e autoimunidade", [S(1791625422039), S(1791625432257)])]),
 (23, "conteudo", "Th1, macrófago ativado e granuloma", [("a50", "Granuloma como forma de inflamação crônica", S(1791716405167))]),
 (24, "conteudo", "Plasmócitos", [("a51", "Células B terminais onde o antígeno persiste", "plasmocito"), ("a52", "Reconhecer o plasmócito", "ak-plasmocito"),
   ("a53", "Tecido linfoide em órgãos não linfoides", "terciario")]),
 (25, "conteudo", "Tecido linfoide: linfonodo × hepatite crônica", [("a54", "Folículos na hepatite crônica", "terciario")]),
 (26, "conteudo", "Bronquiolite folicular", [("a55", "Folículos no pulmão", "terciario")]),
 (27, "conteudo", "Mastócito", [("a56", "Mastócito e IgE", "ak-mastocito")]),
 (28, "conteudo", "Asma: Th2, IgE, mastócito, eosinófilo; remodelamento", [("a57", "Mastócito sustenta e atrai eosinófilos", "ak-mastocito-tardio"),
   ("a58", "Remodelamento", "asma-remodelamento")]),
 (29, "conteudo", "Eosinófilos: eotaxina (CCR3), MBP", [("a59", "Eotaxina", S(1791743343634)), ("a60", "CCR3", "eos-ccr3"), ("a61", "MBP tóxica a parasitas e epitélio", S(1791780353397))]),
 (30, "conteudo", "Neutrófilos na inflamação crônica persistente (fumo)", [("a62", "Neutrófilos persistem (fumo)", "neutro-cronico")]),
]
JUSTIFICATIVAS = {}
CAPITULO = [("Robbins, Bases Patológicas, cap. 2, pp. 70–73", [
 ("l1", "Definição: semanas a meses; inflamação, lesão e reparo coexistem", "ic-duracao"), ("l2", "Início insidioso", "ic-insidiosa"),
 ("l3", "Causas: infecção persistente, imunomediadas, tóxicos", ["ak-causa-infeccao", "ic-causas"]),
 ("l4", "Morfologia: mononucleares, destruição, angiogênese e fibrose", ["ic-cid", "ak-celulas"]),
 ("l5", "Sistema mononuclear fagocítico; vida de monócito e macrófago", ["mac-sfm", "mac-vida"]),
 ("l6", "Ativação por TLR e IFN-γ; produtos tóxicos, quimiotáticos e fibrogênicos", [S(1791625430208), "mac-destroi", "mac-recruta", "ak-tgf"]),
 ("l7", "Desaparecimento × acúmulo do macrófago", ["mac-limitada", "mac-persiste"]),
 ("l8", "Interação bidirecional T–macrófago (IL-12, IFN-γ)", "lin-circuito"),
 ("l9", "Plasmócitos e órgãos linfoides terciários", ["plasmocito", "terciario"]),
 ("l10", "Eosinófilos: eotaxina, MBP", [S(1791743343634), S(1791780353397)]), ("l11", "Mastócitos: FcεRI, citocinas", "ak-mastocito"),
 ("l12", "Neutrófilos na inflamação crônica (osteomielite, tabagismo)", "neutro-cronico"),
 ("l13", "Granuloma", EXC + "aula 47 Inflamação granulomatosa"),
])]
EXERCICIOS = [
 ("Provas UC03 (índice pat-10-inflamacao-cronica)", [
   ("p1", "2025 P3 3.5: alterações estruturais (tríade nas vias aéreas)", ["ic-cid", "asma-remodelamento"]),
   ("p2", "2019 P3 4.4: células e mecanismos", ["mac-principal", "lin-circuito", "ak-celulas"]),
   ("p3", "2018 P3 4.2: inflamação crônica e fibrose (M2, TGF-β)", ["mac-m2-tgf", "ak-tgf"]),
   ("p4", "2017 P3 4.1: células mononucleares na hepatite viral crônica", "ak-celulas"),
   ("p5", "2015 P2 1.1: células do granuloma", S(1791716405167)),
   ("p6", "2015 P2 3.4: desfecho por cicatrização", "ic-cid"),
   ("p7", "2015 P2sub 3.2: inflamação crônica → destruição + fibrose", ["ic-cid", "mac-destroi"])]),
 ("Exercícios da aula (Material Complementar IV)", [
   ("e1", "Por que a não resolução é deletéria", "ic-nao-resolvida"), ("e2", "Doenças não infecciosas", "ic-causas"),
   ("e3", "Doenças infecciosas", "ak-causa-infeccao"), ("e4", "Tipos de linfócitos e patologias", [S(1791625422657), S(1791625432007), S(1791625432257)]),
   ("e5", "Inflamação pelo cigarro: células", "neutro-cronico"), ("e6", "Subtipos de macrófagos", ["mac-m1m2", "mac-m1-no", "mac-m2-tgf"]),
   ("e7", "O que é MALT", "malt")]),
 ("Palavras-cruzadas da aula", [
   ("x1", "Parasitas (Th2)", S(1791625432007)), ("x2", "Th17 autoimune", S(1791625432257)), ("x3", "Reparo coexiste com dano", "ic-duracao"),
   ("x4", "Mastócito", "ak-mastocito"), ("x5", "Fagocitose", S(1791716411025)), ("x6", "Linfócitos", "ak-celulas"), ("x7", "Alternativa (M2)", "mac-m1m2"),
   ("x8", "Infecções persistentes", "ak-causa-infeccao"), ("x9", "Macrófago orquestra", "mac-principal"), ("x10", "Eosinófilos", S(1791780353397)),
   ("x11", "Clássica (M1)", "mac-m1m2"), ("x12", "Neutrófilo na osteomielite", "neutro-cronico"), ("x13", "Semanas", "ic-duracao"),
   ("x14", "Monócito", "ak-monocito"), ("x15", "Bidirecional", "lin-circuito"), ("x16", "CD4 auxiliar", S(1791625422657)),
   ("x17", "Hipersensibilidade", EXC + "aula 64"), ("x18", "Prostaglandinas/febre e leucocitose", EXC + "efeitos sistêmicos da aguda, aula 37/38")]),
 ("Monitoria P3 Patologia, aula 10", [("m1", "Definição, causas, tríade, células, M1/M2, folículos", ["ic-cid", "ic-causas", "mac-m1m2", "terciario"])]),
 ("Apostila de veteranos, cap. 8", [("v1", "Tríade, macrófago, linfócitos, plasmócitos", ["ic-cid", "mac-principal", "plasmocito"])]),
]
