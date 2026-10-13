"""Inventário atômico de Sistema complemento (UC03 P2, Imunologia, aula 31; 60 lâminas, pasta pessoal = PDF da turma). Escrito em 10/10/2026
antes da seleção: lâminas (visual/folha-NN), transcrição da turma (Aula 06), bibliografia (Material Complementar III), provas imuno-06
(2025 P2 1.7, 6.1, 6.2; 2024 P3 3.1; outras eco), monitoria P2 aula 7. Videoaula assíncrona dispensada (F-20261010-CLAUDE-06).
"""
PREFIXO = "im31"
AULA = "Sistema complemento (UC03 P2; Imunologia)"
EXC = "EXC: "
C = "conteudo"
SLIDES = [
 (1, "capa", "Capa", []),
 (2, C, "Mapa do complemento", [("papeis", "Inato, opsonização, inflamação, co-estímulo B, doenças", ["inata", "opsoninas"])]),
 (3, C, "30 proteínas plasmáticas", [("sintese", "Fígado e células imunes", "figado"), ("cascata", "Atividade proteolítica e regulação", "cascata")]),
 (4, C, "Três fases", [("fases", "Reconhecimento, enzimática, destrutiva", "tres-fases")]),
 (5, C, "Três vias e efeitos", [("vias", "Ag-Ac, lectina, superfície; inflamação, opsonização, morte", ["classica", "lectinas", "alternativa"])]),
 (6, C, "Como funciona", [("frag", "Fragmentos a e b; convertase", ["frag-a-b", "cascata"])]),
 (7, C, "Três vias (repetida)", [("vias2", "Repetição da lâmina 5", "todas-c3")]),
 (8, "capa", "Via clássica (divisória)", []),
 (9, C, "Ativação por IgG/IgM", [("ig", "IgG (CH2) e IgM (CH3)", ["classica", "sh-1791629595622", "sh-1791629595747"])]),
 (10, C, "Componentes iniciais", [("c1", "Começa em C1", "comeca-c1")]),
 (11, C, "C1qr2s2 e duas IgG", [("c1qrs", "C1q liga duas IgG; C1r/C1s", ["c1qrs", "sh-1791629595872"])]),
 (12, C, "Figura: C1 ligado", [("fig", "C1 na superfície", "c1qrs")]),
 (13, C, "C4 e C2 clivados", [("c4c2", "C4a solúvel, C4b gruda; C4b2a", ["c4-primeiro", "convertase-classica"])]),
 (14, C, "C3 clivado", [("c3", "C3a solúvel, C3b gruda; C4b2a3b", "c5-convertase-classica")]),
 (15, C, "C5 clivado", [("c5", "C5a solúvel, C5b gruda", "todas-c5")]),
 (16, C, "C5b67, C5b678", [("c5b6", "Montagem do MAC", "mac")]),
 (17, C, "Poli-C9", [("c9", "MAC com poli-C9", ["mac", "mac-lise"])]),
 (18, C, "Poro na membrana", [("poro", "Entrada de fluidos", "mac-lise")]),
 (19, C, "Figura de poros", [("poros", "Poros em micrografia", "mac-lise")]),
 (20, C, "Resumo da via clássica", [("resumo", "C1q → C4 → C2 → C4b2a → C3", ["convertase-classica", "c4-primeiro"])]),
 (21, C, "Ativadores da via alternativa", [("ativ", "Ácido teicoico, LPS, venenos, polímeros, calicreínas", ["alternativa", "ativadores-alt", "lps"])]),
 (22, C, "Hidrólise de C3, B e D", [("hidrolise", "C3(H2O), fator B, fator D, Ba", ["tioester", "fator-d", "comeca-c3", "c3bbb"])]),
 (23, C, "Via alternativa (figura)", [("properdina", "Properdina e alça", ["properdina", "alca-positiva", "c3bbb3b"])]),
 (24, C, "MAC (título)", [("mac", "Complexo de ataque à membrana", ["mac", "todas-c3", "c3-central"])]),
 (25, C, "Poro (figura)", [("poro2", "Poro", "mac-lise")]),
 (26, C, "Alça da via alternativa", [("alca", "C3bBb estabilizado por properdina", ["alca-positiva", "properdina"])]),
 (27, C, "Via terminal", [("terminal", "C5 convertase → C5b-9", "todas-c5")]),
 (28, C, "Via das lectinas", [("mbl", "MBL, MASP-1/2, manose", ["lectinas", "mbl-masp"])]),
 (29, C, "MBP ~ C1q", [("mbp", "MBP ativa MASP, cliva C4 e C2", "mbl-masp")]),
 (30, C, "Lectinas até o MAC", [("lect-mac", "C3 convertase → C5 → MAC", "convertase-classica")]),
 (31, C, "Funções (pergunta)", [("perg", "Quais as funções?", "opsoninas")]),
 (32, C, "Mapa (repetido)", [("mapa", "Repetição da lâmina 2", "inata")]),
 (33, C, "Produtos e funções", [("tab", "Lise C5b-9; opsoninas; anafilatoxinas; imunocomplexos", ["opsoninas", "opsoninas-outras", "anafilatoxinas", "imunocomplexos"])]),
 (34, C, "Lise de patógeno", [("lise", "C3b → MAC → lise osmótica", "mac-lise")]),
 (35, C, "Figura de lise", [("fig-lise", "Bactéria lisada", "mac-lise")]),
 (36, C, "Receptores dos produtos", [("cr", "CR1, CR3/CR4, C3aR, C5aR", ["ic3b-cr3", "c5a"])]),
 (37, C, "Corpos apoptóticos", [("apopt", "C1q, iC3b, C4b, MBL", "apoptoticos")]),
 (38, C, "Imunocomplexos", [("ic", "Solubilização e clearance via CR1", ["imunocomplexos", "cr1-hemacia"])]),
 (39, C, "Opsonização (figura)", [("opso", "Fagócito com CR e FcR", "opsoninas")]),
 (40, C, "Anafilatoxinas", [("anaf", "C3a/C5a, quimiotaxia", ["anafilatoxinas", "anafilatoxina-acoes", "c5a"])]),
 (41, C, "Vasodilatação", [("vaso", "Vasodilatação", "anafilatoxina-acoes")]),
 (42, C, "Permeabilidade", [("perm", "Aumento de permeabilidade", "anafilatoxina-acoes")]),
 (43, C, "Imunidade humoral", [("cr2", "CR2-C3dg co-receptor; FDC", ["coestimulo-b", "sh-1791629591396", "sh-1791629594223"])]),
 (44, C, "Tabela de receptores", [("tab-cr", "CR1, CR2, CR3, CR4, C5aR, C1qRp", ["cr1-hemacia", "ic3b-cr3", "c5a"])]),
 (45, C, "Eventos inflamatórios", [("infl", "Histamina, músculo liso, permeabilidade", "anafilatoxina-acoes")]),
 (46, C, "Inflamação (figura)", [("infl2", "Mastócito, quimiotaxia, adesão", "anafilatoxina-acoes")]),
 (47, C, "Regulação (título)", [("reg", "Regulação", "c1-inibidor")]),
 (48, C, "Inibidor de C1", [("c1inh", "C1-INH", "c1-inibidor")]),
 (49, C, "Reguladores da via clássica", [("reg-cl", "C1-INH, DAF, carboxipeptidase N, fatores H/I", ["daf", "carboxipeptidase"])]),
 (50, C, "Reguladores da via alternativa", [("reg-alt", "Fatores I e H sobre C3b", ["fator-h", "fator-i"])]),
 (51, C, "Fatores I e H", [("hi", "H bloqueia B; I gera iC3b, C3dg", ["fator-h", "fator-i"])]),
 (52, C, "Produtos do fator I", [("prod", "C3c, C3dg; C4c, C4d", "fator-i")]),
 (53, C, "CD59", [("cd59", "CD59 bloqueia MAC na hemácia", ["cd59", "gpi"])]),
 (54, C, "Tabela de deficiências", [("def", "C1q/C2/C4 LES; C3 piogênicas; C5-C9 Neisseria; C1-INH; H/I; CD59 HPN",
                                    ["precoces-les", "c3-def", "terminal-neisseria", "aeh", "fator-h-shu", "gpi"])]),
 (55, C, "Deficiências da via alternativa", [("def-alt", "Infecções por encapsulados; SHU, mácula", ["alternativa-def", "fator-h-shu", "ch50-ah50"])]),
 (56, C, "Deficiências da via clássica", [("def-cl", "Infecções, glomerulonefrite, lúpus", ["precoces-les", "ch50-les"])]),
 (57, C, "Angioedema", [("aeh", "Inibidor de C1", ["aeh", "aeh-bradicinina", "aeh-c4"])]),
 (58, C, "Deficiência de MBL", [("mbl-def", "MBL ~ C1q", "mbl-def")]),
 (59, C, "Via terminal", [("term", "C6–C9 e Neisseria", "terminal-neisseria")]),
 (60, C, "Resumo das vias", [("resumo-vias", "Três vias convergem em C3, anafilatoxinas, MAC", ["c3-central", "tioester"])]),
]
JUSTIFICATIVAS = {"capa": "capa ou divisória, sem conteúdo"}

CAPITULO = [("Material Complementar III — bibliografia da aula (texto de imunologia sobre complemento)", [
   ("bib-vias", "Três vias, convertases, MAC", ["classica", "alternativa", "lectinas", "mac"]),
   ("bib-funcoes", "Opsonização, inflamação, imunocomplexos, imunidade humoral", ["opsoninas", "anafilatoxinas", "imunocomplexos", "coestimulo-b"]),
   ("bib-regulacao", "Reguladores e deficiências", ["c1-inibidor", "daf", "fator-h", "cd59", "precoces-les"])])]

EXERCICIOS = [
 ("Transcrição da turma (Aula 06)", [
   ("tr-ab", "Regra dos fragmentos a/b; C2 exceção", "frag-a-b"),
   ("tr-properdina", "Properdina, única positiva; alça e consumo de C3", ["properdina", "alca-positiva"]),
   ("tr-lupus", "Corpos apoptóticos e lúpus", "apoptoticos"),
   ("tr-cd59", "CD59 protege células próprias", "cd59")]),
 ("Provas UC03 (índice imuno-06)", [
   ("p2025a", "2025 P2 1.7: CH50 normal, AH50 indetectável", ["ch50-ah50", "properdina", "alternativa-def"]),
   ("p2025b", "2025 P2 6.1–6.2: C3 baixo, C4 normal, SHU atípica; Neisseria", ["fator-h-shu", "alternativa-def", "terminal-neisseria"]),
   ("p2024", "2024 P3 3.1: deficiência de C1q/C2/C4 e autoimunidade", ["precoces-les", "apoptoticos"])]),
 ("Monitoria P2, aula 7", [
   ("mon-c3", "C3 seria a pior deficiência", ["c3-central", "c3-def"]),
   ("mon-c5a", "C5a mais eficiente que C3a", "c5a"),
   ("mon-cr1", "Imunocomplexos levados por hemácias ao baço", "cr1-hemacia"),
   ("mon-reg", "DAF, MCP/CR1 cofator do fator I, C1-INH", ["daf", "fator-i", "c1-inibidor"])]),
]
