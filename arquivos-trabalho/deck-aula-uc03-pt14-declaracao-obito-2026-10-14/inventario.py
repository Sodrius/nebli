"""Inventário de Declaração de óbito (UC03 P1; Patologia; 20 lâminas), escrito antes da seleção (14/10).
Material: lâminas da turma (a pasta pessoal está vazia), bibliografia (manual da DO), provas por termo (fontes/provas-do.txt)."""
PREFIXO = "pt14"
AULA = "Declaração de óbito (UC03 P1; Patologia)"
EXC = "EXC: "
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Definição e relevância", [("a1", "Base do SIM", "a-sim"), ("a2", "Usos", "a-usos")]),
 (3, "conteudo", "Quando assinar", [("a3", "Adultos e crianças", "a-fetal"), ("a4", "Óbito fetal ≥ 20 sem/500 g", "a-fetal")]),
 (4, "conteudo", "Quem assina: morte natural", [("a5", "Com e sem assistência", "a-natural")]),
 (5, "conteudo", "Quem assina: morte violenta", [("a6", "IML ou perito designado", "a-violenta")]),
 (6, "conteudo", "Como preencher: causas", [("a7", "Linhas a–d", "b-parte-i"), ("a8", "Parte II", "b-parte-ii"), ("a9", "Causa básica", "b-causa-basica")]),
 (7, "conteudo", "Caso: hipertensão", [("a10", "Cadeia causal", "b-parte-i")]),
 (8, "conteudo", "DO do caso hipertensão", [("a11", "Preenchimento e intervalos", ["b-parte-i", "b-intervalo"])]),
 (9, "conteudo", "Caso: esquistossomose", [("a12", "Exemplo", EXC + "ilustração do mesmo raciocínio")]),
 (10, "conteudo", "DO esquistossomose", [("a13", "Caso: choque hipovolêmico ← varizes ← hipertensão portal ← esquistossomose; diabetes na Parte II", "c-caso-varizes")]),
 (11, "conteudo", "Caso: megacólon chagásico", [("a14", "Exemplo", EXC + "ilustração")]),
 (12, "conteudo", "DO megacólon", [("a15", "Exemplo", EXC + "ilustração")]),
 (13, "conteudo", "Caso: COVID-19", [("a16", "Exemplo", EXC + "ilustração")]),
 (14, "conteudo", "DO COVID-19", [("a17", "Diabetes na Parte II", "b-parte-ii")]),
 (15, "conteudo", "Caso: aneurisma de aorta", [("a18", "Exemplo", EXC + "ilustração")]),
 (16, "conteudo", "DO aneurisma", [("a19", "COVID-19 e diabetes na Parte II; cadeia do aneurisma roto", ["c-caso-aneurisma", "b-parte-ii"])]),
 (17, "conteudo", "Erros mais comuns", [("a20", "Parada cardiorrespiratória, falência de múltiplos órgãos", "c-erros")]),
 (18, "conteudo", "Campo 59", [("a21", "Ausência de sinais de violência", "c-campo-59")]),
 (19, "conteudo", "Pronto-socorro e mortes metatraumáticas", [("a22", "Metatraumáticas", "c-meta-traumatica")]),
 (20, "capa", "Encerramento", []),
]
JUSTIFICATIVAS = {1: "capa", 20: "encerramento"}
CAPITULO = [("Manual de instruções da DO (bibliografia da aula)", [("l1", "Causa básica e cadeia", "b-parte-i"), ("l2", "Quem emite", ["a-natural", "a-violenta"])])]
EXERCICIOS = [("Provas UC03 (busca por termo)", [("p1", "2019 P1 1.12: preencher partes I e II", ["b-parte-i", "b-parte-ii"]),
   ("p2", "2016 P2 2.12: primeira e última linha da parte I", "b-parte-i")])]
