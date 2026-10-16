"""Inventário atômico de 48 Micoses subcutâneas (UC03 P3; Microbiologia; Prof. Benedito Corrêa; 42 lâminas), escrito antes da seleção (16/10, refação v2).
Base lida nesta sessão: lâminas (visual/folha-01..07), transcrição da aula (fontes/transcricao.txt, inteira), material da turma (fontes/turma/turma.pdf = lâminas
da turma), apostila guia (aula 10), monitoria (resumo de 2025, aula 11), UC3.pdf, provas (micro-10: sem questões) e Trabulsi cap. 68.
"""
PREFIXO = "mb48"
AULA = "Micoses subcutâneas (UC03 P3; Microbiologia; Corrêa)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Micoses subcutâneas: implantação, localizadas, linfática", [("i1", "Implantação traumática de sapróbios", "sh-1791628672372")]),
 (3, "conteudo", "Classificação: superficiais, cutâneas, subcutâneas", [("i2", "Subcutâneas e agentes", "au-subcutaneas")]),
 (4, "conteudo", "Classificação: sistêmicas", [("i3", "Sistêmicas", EXC + "aula 50; o contraste de profundidade está na 44")]),
 (5, "conteudo", "Esporotricose: histórico", [("i4", "Sporothrix e esporotricose", "ak1500054558583"), ("i5", "Schenck, Smith, Beurmann, África do Sul", EXC + "histórico: Tab (§4)")]),
 (6, "conteudo", "Epidemia no Brasil", [("i6", "Rio de Janeiro, gatos", "sh-1791628672623")]),
 (7, "conteudo", "Complexo S. schenckii", [("i7", "S. brasiliensis", "sh-1791628672748")]),
 (8, "conteudo", "Epidemiologia: agente, reservatório, porta de entrada", [("i8", "Solo e plantas; via direta/indireta", "sh-1791628672874")]),
 (9, "conteudo", "População de risco", [("i9", "Manipuladores de plantas, gatos", ["sh-1791628672623", "ak1503960067023"])]),
 (10, "conteudo", "Contágio por inoculação", [("i10", "Espinho", "sh-1791628672874")]),
 (11, "conteudo", "Esporotricose: agente, dimorfismo, formas clínicas", [("i11", "Dimórfico 25/37 °C", ["ak1500054777136", "sh-1791628674574"]), ("i12", "Formas clínicas", "au-formas-esporotricose")]),
 (12, "conteudo", "Lesão inicial", [("i13", "Úlcera no local", "sh-1791628673798")]),
 (13, "conteudo", "Forma cutânea localizada", [("i14", "Fixa", "au-formas-esporotricose")]),
 (14, "conteudo", "Forma cutânea localizada (polegar)", [("i15", "Fixa", "au-formas-esporotricose")]),
 (15, "conteudo", "Forma linfocutânea", [("i16", "Nódulos ascendentes", ["ak1500055367426", "ak1500056181436"])]),
 (16, "conteudo", "Forma linfocutânea (braço)", [("i17", "Nódulos em cadeia", "au-formas-esporotricose")]),
 (17, "conteudo", "Forma localizada (face)", [("i18", "Lesão verrucosa", "au-formas-esporotricose")]),
 (18, "conteudo", "Forma linfocutânea", [("i19", "Nódulos abertos e fechados", "ak1500055367426")]),
 (19, "conteudo", "Esporotricose disseminada", [("i20", "Imunodeprimidos", "au-formas-esporotricose")]),
 (20, "conteudo", "Esporotricose em cão", [("i21", "Animais", EXC + "Tab; o gato como transmissor está em sh-1791628672623")]),
 (21, "conteudo", "Esporotricose em gatos", [("i22", "Felinos", "sh-1791628672623")]),
 (22, "conteudo", "Exame direto", [("i23", "Levedura em charuto", ["sh-1791628674273", "ak1500056181436"])]),
 (23, "conteudo", "Cultivo a 25 °C", [("i24", "Colônia; cultura confirma", "sh-1791628674824")]),
 (24, "conteudo", "Microscopia do cultivo a 25 °C", [("i25", "Hifas e conídios em margarida", ["sh-1791628673298", "ak1500055049050"])]),
 (25, "conteudo", "Fase Y no tecido", [("i26", "Leveduras; granuloma", ["ak1500055726473", "ak1500151965518"]),
   ("i27", "Tratamento (apostila, monitoria)", ["sh-1791628674948", "sh-1791628675073", "ak1509746332128"])]),
 (26, "conteudo", "Cromomicose: etiologia e epidemiologia", [("i28", "Demáceos, Fonsecaea; ocupacional", "sh-1791628675198")]),
 (27, "conteudo", "Cromomicose (imagens)", [("i29", "Lesões verrucosas nos membros inferiores", "sh-1791628675323")]),
 (28, "conteudo", "Diagnóstico laboratorial", [("i30", "Coleta, KOH, biópsia, cultivo", "sh-1791628675571")]),
 (29, "conteudo", "Exame direto: corpos escleróticos", [("i31", "Corpos escleróticos", "sh-1791628675571")]),
 (30, "conteudo", "Cultivo: Fonsecaea pedrosoi", [("i32", "Colônia escura", EXC + "identificação: aula 55")]),
 (31, "conteudo", "Tipos de conidiação", [("i33", "Acrógena, acropleurógena, fialófora", EXC + "identificação: aula 55; Tab")]),
 (32, "conteudo", "Histopatológico", [("i34", "Corpos escleróticos no tecido", "sh-1791628675571")]),
 (33, "conteudo", "Maduromicose podal", [("i35", "Pé", "sh-1791628675824")]),
 (34, "conteudo", "Micetomas: actinomicose, nocardiose, maduromicose", [("i36", "Bacterianos × fúngico", ["sh-1791628676074", "sh-1791628676247", "ak1510012087056", "ak1510011869046"])]),
 (35, "conteudo", "Tríade do micetoma", [("i37", "Tumor, fístula, grãos", "sh-1791628675824")]),
 (36, "conteudo", "Grãos parasitários", [("i38", "Madurella grisea: grãos negros", "sh-1791628672497")]),
 (37, "conteudo", "Maduromicose podal (radiografia)", [("i39", "Lesão óssea", EXC + "Tab")]),
 (38, "conteudo", "Lobomicose: etiologia", [("i40", "Lacazia loboi", "sh-1791628676373")]),
 (39, "conteudo", "Epidemiologia", [("i41", "Homens da Amazônia; golfinhos", EXC + "Tab da nota da Lacazia")]),
 (40, "conteudo", "Doença de Jorge Lobo", [("i42", "Lesões queloidianas", "sh-1791628676621")]),
 (41, "conteudo", "Diagnóstico", [("i43", "Não cultivável; exame direto", EXC + "Tab; imagem das cadeias no verso de sh-1791628676373")]),
 (42, "conteudo", "Exame direto e histopatológico", [("i44", "Células refringentes em cadeia", "sh-1791628676373")]),
]
JUSTIFICATIVAS = {"capa": "capa (título e professor)"}
CAPITULO = [("Trabulsi cap. 68 (micoses subcutâneas)", [
   ("t1", "Implantação traumática; lista das cinco micoses", ["sh-1791628672372", "au-subcutaneas"]),
   ("t2", "Esporotricose: complexo, linfocutânea, gatos, diagnóstico, iodeto", ["sh-1791628672748", "au-formas-esporotricose", "sh-1791628672623", "sh-1791628675073"]),
   ("t3", "Cromoblastomicose: demáceos, couve-flor, corpos escleróticos", ["sh-1791628675198", "sh-1791628675571"]),
   ("t4", "Feo-hifomicose: hifas escuras no tecido", "au-subcutaneas"),
   ("t5", "Eumicetoma: tríade, cor dos grãos", ["sh-1791628675824", "sh-1791628672497"]),
   ("t6", "Lobomicose: Lacazia, queloides, não cultivável", ["sh-1791628676373", "sh-1791628676621"])])]
EXERCICIOS = [
 ("Provas UC03 (micro-10-micoses-subcutaneas)", []),
 ("Monitoria (resumo de 2025), aula 11", [("m1", "Esporotricose: vias saprofítica e zoonótica, formas", ["sh-1791628672623", "au-formas-esporotricose"]), ("m2", "Cromoblastomicose: demáceos", "sh-1791628675198")]),
 ("Apostila guia, aula 10", [("a1", "Micoses subcutâneas e esporotricose", ["au-subcutaneas", "sh-1791628674574"])]),
]
