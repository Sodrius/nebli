"""Inventário de Recombinação V(D)J (UC03 P1; Biologia molecular; 25 lâminas), escrito antes da seleção (14/10).
Material: lâminas, 4 transcrições (lidas inteiras), exercícios (8 questões), provas biomol-02 (3 itens)."""
PREFIXO = "bm18"
AULA = "Recombinação V(D)J (UC03 P1; Biologia molecular)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "capa", "Aulas do professor", []),
 (3, "conteudo", "Título e bibliografia", [("a1", "Bibliografia", EXC + "lista")]),
 (4, "conteudo", "Objetivos", [("a2", "Objetivos", "a-diversidade")]),
 (5, "conteudo", "Antígenos e anticorpos", [("a3", "Epítopo", "a-epitopo")]),
 (6, "conteudo", "Desenvolvimento de B e T", [("a4", "Medula, timo", S(1791629589247))]),
 (7, "conteudo", "Expansão clonal", [("a5", "Um clone, um anticorpo", "ak-mieloma")]),
 (8, "conteudo", "Estrutura da Ig", [("a6", "Pesada e leve", S(1791629588145)), ("a7", "Variável", S(1791629588272))]),
 (9, "conteudo", "10¹² Igs com 25 mil genes", [("a8", "O problema", "a-diversidade")]),
 (10, "conteudo", "Regiões variável e constante; classes", [("a9", "Constante define classe", S(1791629588447))]),
 (11, "conteudo", "Recombinação V(D)J", [("a10", "Kappa", "b-d"), ("a11", "Cadeia pesada", [S(1791629589497), S(1791629589672)]), ("a12", "Enhancer", "b-enhancer"), ("a13", "Cμ", "b-cmu")]),
 (12, "conteudo", "Diversificação combinatória", [("a14", "Contas", ["b-d", S(1791629589120)])]),
 (13, "conteudo", "Sequências sinal; regra 12/23", [("a15", "Heptâmero/nonâmero", "b-rss"), ("a16", "12/23", "b-12-23")]),
 (14, "conteudo", "Exclusão alélica", [("a17", "Um alelo", "b-exclusao"), ("a18", "Kappa primeiro", "b-kappa")]),
 (15, "conteudo", "Primeiro passo: RAG", [("a19", "RAG1/2", [S(1791629589372), "b-rag2"]), ("a20", "Grampo", "b-grampo"), ("a21", "Nocaute", "b-scid")]),
 (16, "conteudo", "RAG: sinapse e clivagem", [("a22", "Sinapse", "b-rag2")]),
 (17, "conteudo", "Diversidade juncional", [("a23", "Nucleotídeos P e N", ["c-artemis", "ak-tdt"]), ("a24", "Imprecisão", "c-quadro")]),
 (18, "conteudo", "Segundo passo: JNHE", [("a25", "Reparo", S(1791630175220))]),
 (19, "conteudo", "Reparando quebras", [("a26", "Recombinação homóloga × JNHE", "c-homologa")]),
 (20, "conteudo", "JNHE e Ku", [("a27", "Ku", "c-ku"), ("a28", "Mutações", S(1791630175220))]),
 (21, "conteudo", "Segundo passo (esquema)", [("a29", "Sinal descartado", "b-grampo")]),
 (22, "conteudo", "Hipermutação somática", [("a30", "AID", [S(1791629595072), "d-uracila"]), ("a31", "Translesão", "d-translesao"), ("a32", "Expansão clonal", S(1791629594472))]),
 (23, "conteudo", "Troca de classe", [("a33", "Não gera diversidade", "d-troca")]),
 (24, "conteudo", "Mecanismos de diversidade", [("a34", "Resumo", "a-diversidade")]),
 (25, "conteudo", "Consequências indesejadas", [("a35", "Não produtivos", "c-quadro"), ("a36", "Autorreativos", "d-tolerancia")]),
]
JUSTIFICATIVAS = {1: "capa", 2: "lista de aulas"}
CAPITULO = [("Transcrições I–IV", [("t1", "Mieloma e especialização", "ak-mieloma"), ("t2", "Enhancer e Cμ", ["b-enhancer", "b-cmu"]), ("t3", "Exclusão alélica e kappa", ["b-exclusao", "b-kappa"]),
   ("t4", "RAG, Artemis, TdT", ["b-rag2", "c-artemis", "ak-tdt"]), ("t5", "AID, glicosilase, translesão", ["d-uracila", "d-translesao"]), ("t6", "Quadro de leitura, tolerância", ["c-quadro", "d-tolerancia"])])]
EXERCICIOS = [
 ("Exercícios de BM — Recombinação", [("e1", "Antígeno, epítopo, anticorpo", "a-epitopo"), ("e2", "Estrutura da Ig", S(1791629588145)), ("e3", "Passos da V(D)J", [S(1791629589672), "b-d"]),
   ("e4", "RAG e 12/23", ["b-12-23", "b-rag2"]), ("e5", "Contas combinatórias", "b-d"), ("e6", "Diversidade juncional", ["c-artemis", "ak-tdt"]), ("e7", "Hipermutação", "d-uracila"), ("e8", "Resposta policlonal", "ak-mieloma")]),
 ("Provas UC03 (biomol-02)", [("p1", "2024 P1 1.6: mecanismo da recombinação", ["b-rss", "b-12-23", "b-rag2"]), ("p2", "2023 P1 2.8: hipermutação", ["d-uracila", S(1791629594472)]),
   ("p3", "2018 P1 1.14: estrutura e mecanismos de diversidade", "a-diversidade")]),
]
