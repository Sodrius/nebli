"""Inventário de Reconhecimento imune inato (UC03 P1; Imunologia; 23 lâminas = parte III da turma), escrito antes da seleção (14/10).
Material: lâminas, transcrição (lida inteira), palavras-cruzadas (jpg), provas imuno-02 (23 itens; 12 próprios), monitoria P1."""
PREFIXO = "im08"
AULA = "Reconhecimento imune inato (UC03 P1; Imunologia)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Objetivos", [("a1", "PRR, famílias, vias, citocinas", "b-familias")]),
 (3, "conteudo", "Recapitulando: repertório", [("a2", "Repertório aleatório", EXC + "aula 07")]),
 (4, "conteudo", "Recapitulando: seleção", [("a3", "Órgãos linfoides primários", EXC + "aula 07")]),
 (5, "conteudo", "Recapitulando: tolerância × resposta", [("a4", "Memória", EXC + "aula 07")]),
 (6, "conteudo", "Reconhecimento hierárquico", [("a5", "PRR × clonais", ["a-hierarquia", "a-treinada"]), ("a5b", "Estado homeostático decide resposta × tolerância", "a-homeostase-decide")]),
 (7, "conteudo", "Apresentação de antígenos", [("a6", "APC", "a-apc")]),
 (8, "conteudo", "PRR: famílias e localização", [("a7", "Tabela", "b-familias"), ("a8", "DAMP/PAMP", [S(1791780352647), S(1791780342851), S(1791743340457), "sh-1791743348110", "b-pamp-essencial"])]),
 (9, "conteudo", "Da sinalização à efetuação", [("a9", "Estratégias", "c-estrategias"), ("a10", "Febre", ["ak-pirogenio", "sh-1791743347261"])]),
 (10, "conteudo", "Ação protetora dos IFNs", [("a11", "Células vizinhas", S(1791984890700)), ("a12", "Efeitos sistêmicos", "c-ifn-gripe")]),
 (11, "conteudo", "Citotoxicidade celular", [("a13", "Suicídio induzido", ["c-citotox", S(1791984891827)])]),
 (12, "conteudo", "Fagocitose", [("a14", "Etapas", "c-fagocitose"), ("a15", "Opsonização", S(1791667096988)), ("a16", "Explosão respiratória", S(1791743343758))]),
 (13, "conteudo", "Mediadores", [("a17", "Citocinas pleiotrópicas", "d-classes"), ("a18", "Lipídicos", "d-lipidicos"), ("a18b", "Exossomos", "d-exossomos")]),
 (14, "conteudo", "Exemplos de citocinas", [("a19", "Classes", "d-classes"), ("a20", "Quimiocinas", "d-quimiocinas"), ("a20b", "TNF, IL-6, IL-12, IL-10", ["ak-tnf", "sh-1791743347558", "sh-1791625422408", "d-il10"])]),
 (15, "conteudo", "Ehrlich, 1908", [("a21", "Citação", EXC + "histórico; Tab")]),
 (16, "conteudo", "Ligantes dos TLR", [("a22", "TLR4", S(1791743339358)), ("a23", "Endossomais, TLR5", S(1791743339982)), ("a24", "TLR3", "b-tlr3"), ("a25", "TLR9", "b-tlr9"), ("a25b", "TLR2", "b-tlr2")]),
 (17, "conteudo", "Ligantes de outros PRR", [("a26", "RIG-I", "b-rig"), ("a27", "NOD", "b-nod2"), ("a28", "Dectina", "b-dectina"), ("a28b", "Manose, formil-peptídeos, NOD2 e Crohn", ["sh-1791780361306", "sh-1791780360005", "ak-nod2-crohn"])]),
 (18, "conteudo", "Vias dos TLR", [("a29", "MyD88", ["e-myd88", S(1791743339611)]), ("a30", "TRIF", "d-trif"), ("a30b", "Apoptose (caspase-8) e sobrevivência (AKT)", "e-caspase8-akt")]),
 (19, "conteudo", "Vias dos TLR (figura)", [("a31", "Cruzamentos", "d-trif")]),
 (20, "conteudo", "Inflamassoma", [("a32", "Definição", [S(1791743339740), S(1791743339860)]), ("a32b", "Doenças inflamatórias hereditárias", "e-autoinflamatorias"), ("a32c", "Piroptose", "sh-1791780343873")]),
 (21, "conteudo", "NLRP3", [("a33", "Montagem", S(1791780343453)), ("a34", "Dois sinais", "e-dois-sinais"), ("a34b", "Urato, colesterol, ácidos graxos", ["sh-1791743340632", "e-colesterol"])]),
 (22, "conteudo", "Em resumo", [("a35", "Produtos pré-formados, modificados, sintetizados e de degradação", "e-produtos"), ("a35b", "Integração receptor → adaptador → fator → produto", "e-mapa-vias")]),
 (23, "conteudo", "Leitura complementar", [("a36", "Referências", EXC + "lista")]),
]
JUSTIFICATIVAS = {1: "capa"}
CAPITULO = [("Transcrição da aula", [("t1", "Hierarquia", "a-hierarquia"), ("t2", "Febre e lagartos", "ak-pirogenio"), ("t3", "MyD88 e TRIF", ["e-myd88", "d-trif"]), ("t4", "Dois sinais", "e-dois-sinais")])]
EXERCICIOS = [("Provas UC03 (imuno-02)", [("p1", "2017 P1 1.8: PRR, MyD88, TRIF", ["e-myd88", "d-trif"]), ("p2", "2024 P2 2.1: elementos da inata", "c-estrategias"), ("p3", "2025 P3 2.5: antiviral inata", [S(1791984890700), "b-rig"]),
   ("p4", "2024 P1 2.11: inata × adquirida", "a-hierarquia"), ("p5", "2018 P3 5.3: TLR3 no influenza", "b-tlr3"), ("p6", "2018 P2 1.5: β-glucana em fungos", "b-dectina")])]
