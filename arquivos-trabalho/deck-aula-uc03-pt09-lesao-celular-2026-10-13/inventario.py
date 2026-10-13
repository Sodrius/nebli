"""Inventário atômico de <AULA>, escrito ANTES de escolher cards, a partir do material de base lido inteiro:
lâminas (visual/folha-NN), transcrição/material docente, monitoria e apostila de veteranos da aula, provas (índice da UC), livro da UC.
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina). Menção no verso não conta.
"""
PREFIXO = "<curto>"
AULA = "<Aula (UC Pn; professor)>"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 # (2, "conteudo", "<título>", [("chave", "ideia ensinada", "chave-do-card")]),
]
JUSTIFICATIVAS = {}
CAPITULO = [("<Livro, cap.>", [])]
EXERCICIOS = [("Provas <UC> (índice <slug>)", []), ("Monitoria <Pn>, aula <n>", []), ("Apostila de veteranos, aula <n>", [])]
