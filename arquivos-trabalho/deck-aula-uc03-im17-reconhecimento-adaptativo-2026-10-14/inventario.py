"""Inventário de Reconhecimento imune adaptativo (UC03 P1; Imunologia; 18 lâminas = Anb.pdf, versão 2026; o ppsx pessoal só acrescenta a lâmina de leitura), escrito antes da seleção (14/10).
Material: lâminas, transcrição (lida inteira), bibliografia histórica (Mackaness; Burnet), provas imuno-03 (22 itens; 10 próprios)."""
PREFIXO = "im17"
AULA = "Reconhecimento imune adaptativo (UC03 P1; Imunologia)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Objetivos", [("a1", "Anticorpos e troca de classes", "c-tipos")]),
 (3, "conteudo", "Recapitulando: seleção", [("a2", "Seleção, AIRE, Treg, edição, RAG (monitoria aula 3)", ["sh-1791625425082", "sh-1791625423932", "sh-1791625434632", "sh-1791629587897", "sh-1791629589372"])]),
 (4, "conteudo", "Reconhecimento composto", [("a3", "APC, T e B", "a-b-direto")]),
 (5, "conteudo", "Especificidade e memória", [("a4", "Bactérias atenuadas", ["a-memoria", "a-selecao-clonal"])]),
 (6, "conteudo", "Humoral × celular", [("a5", "Soro × células", "a-humoral")]),
 (7, "conteudo", "Eletroforese e gamaglobulinas", [("a6", "Hiperimunização", "b-gama")]),
 (8, "conteudo", "Mieloma: pico monoclonal", [("a7", "Pico", S(1792029316961))]),
 (9, "conteudo", "Dreyer e Bennett", [("a8", "Porção comum e variável", "b-dreyer")]),
 (10, "conteudo", "Troca de classes", [("a9", "IgM → IgG", ["b-troca", S(1792029321811), "b-cinetica", "sh-1791629598047"])]),
 (11, "conteudo", "Estrutura básica", [("a10", "Papaína/pepsina", ["ak-papaina", "ak-pepsina"]), ("a11", "Cadeias", [S(1791629588145), "c-leves"]), ("a12", "Domínios, dobradiça", ["c-dominio-ig", "sh-1791629590722", "c-isotipo"])]),
 (12, "conteudo", "Isotipos, alotipos, idiotipos", [("a13", "Tipos", ["c-tipos", S(1791629588272), S(1791629588447)])]),
 (13, "conteudo", "Propriedades biológicas", [("a14", "CDR", "d-cdr"), ("a15", "Fab", "d-fc"), ("a16", "Fc", "d-fc"), ("a17", "Ativação celular", "d-graves"), ("a17b", "Membrana × secretado; Igα/Igβ; CDR3; epítopos", ["c-membrana", "c-igab", "c-cdr3", "sh-1792029316710", "c-conformacional"])]),
 (14, "conteudo", "Papel de cada classe", [("a18", "IgM", [S(1791629591646), "d-igm"]), ("a19", "IgG", ["d-igg", S(1791629597298), "ak-igg-soro"]), ("a20", "IgE", "d-ige"), ("a21", "IgA", ["d-iga", S(1791629596747), "sh-1791629591820"])]),
 (15, "conteudo", "Tipo não afeta especificidade", [("a22", "Avidez, afinidade, valência, reação cruzada", ["d-avidez", "ak-afinidade", "ak-valencia", "d-reacao-cruzada"]), ("a23", "IgD", S(1791629587397))]),
 (16, "conteudo", "Geração da diversidade: história", [("a24", "Jerne e Tonegawa", "e-jerne")]),
 (17, "conteudo", "TCR", [("a25", "Restrição ao MHC", "ak-tcr-mhc"), ("a26", "Mesmo mecanismo", "e-tcr")]),
 (18, "conteudo", "Em resumo", [("a27", "Resumo", ["a-humoral", "e-tcr"])]),
]
JUSTIFICATIVAS = {1: "capa"}
CAPITULO = [("Transcrição da aula", [("t1", "Avidez × afinidade", "d-avidez"), ("t2", "IgA anti-inflamatória", "d-iga"), ("t3", "Alotipos e transfusão", "c-tipos"), ("t4", "Graves", "d-graves")]),
            ("Bibliografia histórica (Mackaness; Burnet)", [("l1", "Imunidade celular transferida por células", "a-humoral")])]
EXERCICIOS = [("Provas UC03 (imuno-03)", [("p1", "2024 P1 1.7: Fab × Fc", "ak-papaina"), ("p2", "2017 P3 1.6: troca de isotipo", ["b-troca", S(1792029321811)]), ("p3", "2017 P3 5.2: efetores Fab e Fc", "d-fc"),
   ("p4", "2024 P3 3.2: Fab/Fc do BCR e secretado", "d-fc")])]
