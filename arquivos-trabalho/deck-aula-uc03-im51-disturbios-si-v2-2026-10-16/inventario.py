"""Inventário atômico de 51 Distúrbios do sistema imune (UC03 P3; Imunologia), escrito ANTES da seleção (16/10, pipeline v4).
Aula SEM lâminas (F-20261016-CLAUDE-05): as “lâminas” são os itens de fontes/roteiro-aula.md, montado de Abbas caps. 9 e 12,
Janeway caps. 13 (13.7–13.20) e 15 (15.1–15.28), provas imuno-10 (14 subquestões), Mapa Imunológico 1 da monitoria e UC3.pdf.
Apostila guia, monitoria P3 e Grande Resumo P3 não têm seção desta aula (aula nova em 2026).
"""
PREFIXO = "im51"
AULA = "Distúrbios do sistema imune (UC03 P3; Imunologia; aula sem lâminas)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa / objetivo: classificar pelo mecanismo que falhou", []),
 (2, "conteudo", "Três grupos de falha", [("a1", "Imunodeficiência, autoimunidade, autoinflamação", "au-tres-grupos"),
   ("a2", "Hipersensibilidade é outra aula", EXC + "aula 64; fica no Extra")]),
 (3, "conteudo", "Autoimune × autoinflamatória", [("a3", "Adaptativo × inato", "au-autoimune-x-autoinflamatoria")]),
 (4, "conteudo", "Tolerância central × periférica", [("a4", "Onde a tolerância é induzida", "au-tolerancia")]),
 (5, "conteudo", "Tolerância central T", [("a5", "Seleção negativa na medula tímica", ["sh-1791625423808", "sh-1791625423683"]), ("a6", "AIRE", "sh-1791625423932")]),
 (6, "conteudo", "Tolerância central B", [("a7", "Deleção na medula óssea", "ak1486952612312"), ("a8", "Edição de receptor", "sh-1791629587897")]),
 (7, "conteudo", "Tolerância periférica: três mecanismos", [("a9", "Anergia, Treg, deleção", "au-periferica")]),
 (8, "conteudo", "Anergia", [("a10", "Sem coestimulação", ["sh-1791625428657", "ak1487117363961", "ak1486952615115"]),
   ("a11", "CTLA-4 e PD-1", ["sh-1791625428782", "ak1495599255138"])]),
 (9, "conteudo", "Treg", [("a12", "Função", "sh-1791625435108"), ("a13", "CD25 e FOXP3", ["sh-1791625434757", "ak1489970994844"]),
   ("a14", "Citocinas e indução", ["sh-1791625435233", "ak1520300460306", "sh-1791625432907"])]),
 (10, "conteudo", "Deleção", [("a15", "Fas–FasL", "sh-1791625429533")]),
 (11, "conteudo", "Genes", [("a16", "HLA", ["ak1487983926461", "sh-1791054010623", "ak1487983915856", "ak1487983933302", "ak1487983947972",
   "ak1487983954783", "ak1487983968953", "ak1582315762546"]), ("a17", "Polimorfismos não HLA", ["ak1487815300280", "ak1487812660177"])]),
 (12, "conteudo", "Ambiente", [("a18", "Mimetismo molecular", ["sh-1791746130130", "ak1503089543399"]), ("a19", "Sexo feminino", "ak1487815294185"),
   ("a20", "Antígeno sequestrado", EXC + "oftalmia simpática só no AnKing clínico; fica no Tab")]),
 (13, "conteudo", "Autoimunidade monogênica", [("a21", "AIRE → APS-1", "sh-1791625424057"), ("a22", "FOXP3 → IPEX", ["sh-1791625435783", "ak1487815285101"]),
   ("a23", "FAS → ALPS", "ak1487470217383")]),
 (14, "conteudo", "Bloqueio de checkpoint", [("a24", "Anti-PD-1 → autoimunidade", "ak1495629799342")]),
 (15, "conteudo", "Órgão-específica × sistêmica", [("a25", "Classificação", "au-orgao-sistemica")]),
 (16, "conteudo", "Mecanismo efetor por cima", [("a26", "Anticorpo estimulador", "ak1462038188179"), ("a27", "Anticorpo bloqueador", "ak1488418525490"),
   ("a28", "Imunocomplexos (LES)", ["ak1581890934727", "ak1487815347337"]), ("a29", "Célula T (DM1)", "sh-1791054010997")]),
 (17, "conteudo", "Complemento precoce → LES", [("a30", "C1q, C2, C4", ["sh-1791667099713", "ak1487815316366", "ak1487727814679"])]),
 (18, "conteudo", "Primárias × secundárias", [("a31", "Herdada × adquirida", "au-primaria-secundaria"), ("a32", "Riscos", ["ak1544832356705", "ak1577804124702"])]),
 (19, "conteudo", "Tipo de infecção aponta o componente", [("a33", "B × T", ["ak1539873617585", "ak1487727769430", "ak1487727777884", "ak1487727785545", "sh-1791626779153"]),
   ("a34", "B, anticorpo, complemento → encapsuladas", "ak1500404833072")]),
 (20, "conteudo", "SCID", [("a35", "γc/IL-2R", ["ak1487727534510", "ak1487727537386"]), ("a36", "ADA", ["ak1476498858782", "ak1487727526313", "ak1476498854265",
   "ak1476498861750", "ak1487727529450", "ak1487727532142"]), ("a37", "RAG", "ak1582321770897"), ("a38", "MHC II", "sh-1791625424233"),
   ("a39", "Achados imunológicos", ["ak1487727559962", "ak1487727562925", "ak1487727566026", "ak1487727568569"])]),
 (21, "conteudo", "DiGeorge", [("a40", "Timo ausente", ["ak1487727477833", "ak1487727483197", "ak1487727508642", "ak1486945186009", "ak1577801724794"])]),
 (22, "conteudo", "Célula B / anticorpo", [("a41", "XLA", ["ak1487727571098", "ak1487727578609", "ak1487727581060", "ak1487727583313", "ak1487727589236",
   "ak1487727591641", "ak1487727596629", "ak1487727603426", "ak1577803662725"]), ("a42", "CVID", ["ak1487727606729", "ak1487727609159", "ak1487727615686", "ak1487727618491"]),
   ("a43", "IgA", ["ak1487727624742", "ak1487727627992", "ak1487727631557", "ak1487121978005", "ak1487727634083"]),
   ("a44", "Hiper-IgM", ["sh-1791629593673", "ak1487727647861", "ak1487727650568", "ak1487727658056", "ak1487727660381", "ak1487727666057"])]),
 (23, "conteudo", "Fagócitos", [("a45", "DGC", ["sh-1791743343884", "ak1487642739271", "ak1487642736949", "ak1500234392681", "ak1506204165300", "ak1506212687876", "ak1581896616838"]),
   ("a46", "LAD", ["sh-1791743343209", "sh-1791780358431", "sh-1791743343383", "sh-1791743343509", "sh-1791780359109", "ak1487642628188", "ak1581896116295"]),
   ("a47", "Chédiak-Higashi", ["sh-1791780362329", "sh-1791780362456", "ak1487642678318", "ak1487642685688", "ak1487642693791", "ak1487642705376", "ak1487642707794"])]),
 (24, "conteudo", "Complemento", [("a48", "Terminal → Neisseria", ["sh-1791667100513", "ak1487727812574"]), ("a49", "Inibidor de C1", "sh-1791667099963")]),
 (25, "conteudo", "HIV", [("a50", "gp120–CD4", "ak1502066834360"), ("a51", "AIDS", "ak1502068052536")]),
 (26, "conteudo", "Inflamassoma", [("a52", "Sensor e IL-1β", ["sh-1791743339740", "sh-1791743339860", "sh-1791780343453"])]),
 (27, "conteudo", "Síndromes autoinflamatórias", [("a53", "Pirina e NLRP3", "au-autoinflam-sindromes"),
   ("a54", "FMF", ["ak1487550507064", "ak1487550517104", "ak1487550504664", "ak1487550515135"]), ("a55", "Bloqueio de IL-1", ["ak1497215831699", "ak1497215299862"]),
   ("a56", "TRAPS", EXC + "sem card de acervo; vai no Extra do organizador (síndrome por cima)")]),
]
JUSTIFICATIVAS = {1: "capa do roteiro: objetivo da aula"}
CAPITULO = [
 ("Abbas, Imunologia Básica, cap. 9", [("l1", "Tolerância central e periférica", ["au-tolerancia", "au-periferica"]),
   ("l2", "Genes e ambiente", ["ak1487983926461", "ak1503089543399"])]),
 ("Abbas, Imunologia Básica, cap. 12", [("l3", "Primária × secundária", "au-primaria-secundaria"), ("l4", "Defeitos de maturação e ativação", ["ak1487727534510", "ak1487727571098"])]),
 ("Janeway caps. 13 e 15", [("l5", "Doença autoinflamatória", ["au-autoimune-x-autoinflamatoria", "au-autoinflam-sindromes"]),
   ("l6", "Órgão-específica × sistêmica", "au-orgao-sistemica")]),
]
EXERCICIOS = [
 ("Provas UC03 (imuno-10)", [
   ("p1", "2025 P3 4.1: timo, Treg FOXP3 e tolerância periférica", ["au-tolerancia", "sh-1791625434757"]),
   ("p2", "2024 P1 2.12: inflamação de baixo grau × autoimune", "au-autoimune-x-autoinflamatoria"),
   ("p3", "2024 P1 2.4: Hashimoto, resposta Th1", "au-orgao-sistemica"),
   ("p4", "2024 P3 2.11: quebra de tolerância em sítio privilegiado", "au-tolerancia"),
   ("p5", "2024 P3 3.1: imunodeficiência ligada a autoimunidade (complemento precoce, hipoplasia tímica)", ["sh-1791667099713", "ak1487727477833"]),
   ("p6", "2024 P3 3.2: anti-Sm e anti-DNA", "ak1487815347337"),
   ("p7", "2024 P4 1.8: anti-PD-L1 e CTLA-4 → autoimunidade", ["ak1495629799342", "sh-1791625428782"]),
   ("p8", "2018 P1 2.3: quebra de tolerância e mecanismos que a previnem", ["au-periferica", "ak1503089543399"]),
   ("p9", "2016 P1 3.3: deficiências do complemento", ["sh-1791667100513", "ak1487815316366"]),
   ("p10", "2015 P2 6.2: seleção tímica (MHC I/II, AIRE, FOXP3)", ["sh-1791625424233", "sh-1791625424057", "sh-1791625435783"])]),
 ("Monitoria, Mapa Imunológico 1", [("m1", "Seleção negativa e AIRE", "sh-1791625423932"), ("m2", "Doenças autoimunes têm a hipersensibilidade como mecanismo", "ak1581890934727")]),
 ("UC3.pdf (organização do SI)", [("u1", "Falha → autoagressão, hipersensibilidade ou imunodeficiência", "au-tres-grupos")]),
]
