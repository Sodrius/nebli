"""Inventário da Prática 3: identificação bacteriana (UC03 P2; Microbiologia; 42 lâminas, versão A 2023), escrito antes da seleção (15/10).
Material: lâminas (A 2023 ⊃ B 2023), roteiro de aula prática (Identificação III), diagnóstico molecular (Identificação IV), questões de revisão (lâmina 41)."""
PREFIXO = "mb40"
AULA = "Prática 3: identificação bacteriana (UC03 P2; Microbiologia)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Roteiro do diagnóstico", [("a1", "Etapas", "a-etapas")]),
 (3, "conteudo", "Importância do diagnóstico; amostras", [("a2", "Amostras", "b-lepra")]),
 (4, "conteudo", "Comunicação médico–laboratório", [("a3", "Diagnóstico presuntivo", "a-antes-atb")]),
 (5, "conteudo", "Regras de coleta", [("a4", "Antes do antibiótico", "a-antes-atb"), ("a5", "Representativa", "a-representativa"), ("a6", "Sítio estéril", "a-esteril")]),
 (6, "conteudo", "Acondicionamento", [("a7", "Identificação", EXC + "regra administrativa; Tab")]),
 (7, "conteudo", "Coloração e microscopia", [("a8", "Gram", [S(1791576665617), "b-mapa-coloracao"]), ("a9", "Campo escuro", S(1791576674741))]),
 (8, "conteudo", "Ziehl-Neelsen", [("a10", "TB", S(1791576674542)), ("a11", "Hanseníase", "b-lepra")]),
 (9, "conteudo", "T. pallidum", [("a12", "Subespécies", "b-bejel")]),
 (10, "conteudo", "Virulência do T. pallidum", [("a13", "Adesinas, pouco LPS", "b-tp-virulencia")]),
 (11, "conteudo", "Sífilis primária", [("a14", "Cancro duro", "ak-cancro")]),
 (12, "conteudo", "Sífilis secundária", [("a15", "Exantema", "ak-secundaria")]),
 (13, "conteudo", "Sífilis terciária", [("a16", "Gomas", "ak-goma")]),
 (14, "conteudo", "Bejel", [("a17", "Endêmica", "b-bejel")]),
 (15, "conteudo", "Bouba", [("a18", "Bouba", "b-bejel")]),
 (16, "conteudo", "Meios de cultura", [("a19", "Sangue, chocolate, MacConkey, manitol", ["sh-1791648194368", "c-macconkey-seletivo", "sh-1791648195041", "c-mapa-meios", S(1791647817820), S(1791647818320), S(1791647817219), S(1791648194793)]), ("a20", "LJ", "c-lj"), ("a21", "Anaeróbios", "c-anaerobios")]),
 (17, "conteudo", "Fluxograma: morfologia e Gram", [("a22", "Fluxo", "a-etapas")]),
 (18, "conteudo", "Árvore dos Gram-negativos", [("a23", "Diplococos, cocobacilos, curvos, bacilos (lactose)", "c-arvore-gn")]),
 (19, "conteudo", "Provas para BGN: MacConkey, citrato, MILi, EPM", [("a24", "Lac−", S(1791648194669)), ("a24b", "MacConkey, citrato, MILi, EPM", "c-provas-bgn")]),
 (20, "conteudo", "Tabela do meio Rugai", [("a25", "Tabela de reações do Rugai", EXC + "leitura de bancada tubo a tubo; as provas que ela resume estão em c-provas-bgn")]),
 (21, "capa", "Abertura: cocos Gram-positivos", []),
 (22, "conteudo", "Principais CGP", [("a26", "Micrococcus etc.", "d-micrococcus")]),
 (23, "conteudo", "Fluxo de provas para CGP", [("a27", "Fluxo", [S(1791763646494), "d-fluxo-cgp"])]),
 (24, "conteudo", "Catalase", [("a28", "Catalase", [S(1791763646494), S(1791763646344)])]),
 (25, "conteudo", "O/F, coagulase, hemólise, bacitracina, optoquina", [("a29", "O/F", "d-micrococcus"), ("a30", "Coagulase/novobiocina", [S(1791746129003), S(1791763650819)]), ("a31", "Estreptococos", ["sh-1791647818070", "ak-viridans", "ak-gas", "ak-gbs", "ak-pneumo"])]),
 (26, "conteudo", "Provas sorológicas", [("a32", "Aglutinação, ELISA, hipersensibilidade", ["ak-elisa", "f-mapa-metodos", "sh-1791625436533"])]),
 (27, "conteudo", "ELISA", [("a33", "Não cultiváveis", "e-sorologia")]),
 (28, "conteudo", "Sorologia: anticorpos, exotoxinas", [("a34", "Exotoxinas", "e-sorologia")]),
 (29, "conteudo", "Antibiograma", [("a35", "Disco; Mueller-Hinton", [S(1791647818945), "sh-1791648194118"])]),
 (30, "conteudo", "MIC", [("a36", "MIC", S(1791668526789))]),
 (31, "conteudo", "PCR", [("a37", "Pequenas amostras; falso-positivo", ["f-pcr", "f-falso-positivo"])]),
 (32, "conteudo", "Aplicações da PCR", [("a38", "Virulência", "f-pcr")]),
 (33, "conteudo", "Sequenciamento", [("a39", "Não cultiváveis", "f-sequenciamento")]),
 (34, "conteudo", "BACTEC", [("a40", "Automação de provas", EXC + "equipamento; Tab")]),
 (35, "conteudo", "Antígenos e látex", [("a41", "Látex", "f-latex")]),
 (36, "conteudo", "MALDI-TOF", [("a42", "Espectrometria", "f-maldi")]),
 (37, "conteudo", "TB: clássico × Xpert", [("a43", "Xpert", ["f-xpert", "f-rpob", "c-lj"])]),
 (38, "conteudo", "Tratamento e resistência", [("a44", "Seleção; MDR-TB", ["f-resistencia", "f-mdr"])]),
 (39, "conteudo", "Prevenção: vacinas, higiene", [("a45", "Prevenção: pentavalente", "f-pentavalente")]),
 (40, "conteudo", "Calendário vacinal", [("a46", "Calendário", "f-pentavalente")]),
 (41, "conteudo", "Questões para revisão", [("a47", "Questões", "a-etapas")]),
 (42, "capa", "Encerramento", []),
]
JUSTIFICATIVAS = {1: "capa", 21: "abertura", 42: "encerramento"}
CAPITULO = [("Identificação IV — diagnóstico molecular", [("l1", "Xpert e rpoB", "f-rpob"), ("l2", "PCR", "f-pcr")]),
            ("Identificação III — roteiro prático", [("l3", "Gram e meios seletivos/diferenciais", S(1791647817219))])]
EXERCICIOS = [("Questões para revisão (lâmina 41)", [("q1", "Etapas", "a-etapas"), ("q2", "Sorologia", "e-sorologia"), ("q3", "MIC", S(1791668526789)), ("q4", "PCR", "f-pcr"), ("q5", "Métodos automáticos", "f-maldi")])]
