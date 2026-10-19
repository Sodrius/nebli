"""Inventário do Caso 5 — Insuficiência metabólica (UC21 DIC-I; 10 páginas do caso), escrito antes da seleção (15/10).
Material: texto do caso (plataforma), lâminas do grupo 11 (44), relatório do grupo 11 (22 pp.), prova DIC P1+P2+P3 (integrada, sem item metabólico)."""
PREFIXO = "dic05"
AULA = "Caso 5 — Insuficiência metabólica (UC21)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
SLIDES = [
 (1, "conteudo", "Orientações e objetivos", [("a1", "Objetivos", "a-caso")]),
 (2, "conteudo", "Competências", [("a2", "Competências", ["e-desencadeantes", "c-anabolica"])]),
 (3, "conteudo", "Identificação e HMA", [("a3", "Poliúria, polidipsia, perda de peso", ["a-caso", S(1791054007644)]), ("a4", "Recusa da insulina", "g-adesao")]),
 (4, "conteudo", "Antecedentes e exame no PS", [("a5", "Kussmaul, desidratação, abscesso", ["a-caso", S(1791054012018)]), ("a6", "Família com autoimunes", S(1791054009172)), ("a7", "Médico culpa a mãe", "g-etica")]),
 (5, "conteudo", "Tabela de exames", [("a8", "Gasometria", "e-gasometria"), ("a9", "K+ 6,5", S(1791054007900)), ("a10", "Creatinina 2,3", "ak-prerrenal")]),
 (6, "conteudo", "Evolução e alta", [("a11", "Hidratação e insulina", S(1791054008272)), ("a12", "S. pyogenes", "e-desencadeantes")]),
 (7, "conteudo", "Perguntas 1–3", [("a13", "Definição e diagnóstico", [S(1791054010222), S(1791054008396)]), ("a14", "Diagnóstico precoce", "b-precoce"), ("a15", "Secreção de insulina", S(1792027894938)),
   ("a16", "Ações", "c-anabolica"), ("a17", "Contrarreguladores", S(1791054013222)), ("a18", "Parácrina", "c-paracrina"), ("a19", "Receptor", S(1792027895739)), ("a20", "Tecidos", "c-dependentes")]),
 (8, "conteudo", "Perguntas 4–7", [("a21", "GLUT-4", S(1791054011372)), ("a22", "GLUT-2 Km", "d-km"), ("a23", "Tm e limiar", ["d-tm", "d-limiar"]), ("a24", "Kussmaul e gasometria", "e-gasometria"),
   ("a25", "Creatinina, K+, osmolaridade", ["ak-prerrenal", "e-k-total", "f-osm"]), ("a26", "DM2 e EHH", [S(1791054012447), "e-insulina-dm2"])]),
 (9, "conteudo", "Perguntas 8–12", [("a27", "Autoimunidade e infecção", [S(1791054010623), "e-desencadeantes"]), ("a28", "Complicações", "g-vias"), ("a29", "Adesão", "g-adesao"), ("a30", "Não farmacológico", "g-exercicio"), ("a31", "Ética", "g-etica")]),
 (10, "conteudo", "Bibliografia", [("a32", "Referências", EXC + "lista")]),
]

# itens finos ligados a cada card (perguntas do caso)
_extra = {7: ['sh-1791054010222', 'sh-1791054010997', 'sh-1791054012847', 'sh-1791054007644', 'sh-1791054007769', 'sh-1791054008396', 'sh-1791054008544', 'sh-1791054008670', 'sh-1791647354296', 'sh-1791729317165', 'sh-1792027894938', 'sh-1791054013222', 'sh-1791054011246', 'sh-1792027895739', 'sh-1792027895991'], 8: ['sh-1791054011372', 'sh-1792027896339', 'sh-1791647346120', 'sh-1791054012018', 'sh-1791054012198', 'sh-1791054011545', 'sh-1791054011671', 'sh-1791729323438', 'sh-1791054012447', 'sh-1791054012596', 'ak-bun', 'sh-1791054007900', 'sh-1791054008019', 'sh-1791054008148', 'sh-1791054012320', 'sh-1791054008272'], 9: ['sh-1791054010623', 'sh-1791054009046', 'sh-1791054009172', 'sh-1791054018897', 'sh-1791054015322', 'sh-1791054016196', 'sh-1791054016847', 'sh-1791054017972', 'sh-1791054016421', 'sh-1791054019147']}
SLIDES = [(n, t, ti, its + [(f"z{n}_{i}", k, k) for i, k in enumerate(_extra.get(n, []))]) for (n, t, ti, its) in SLIDES]
JUSTIFICATIVAS = {}
CAPITULO = [("Relatório do grupo 11 (Davi)", [("r1", "Secreção de insulina", S(1792027894938)), ("r2", "Tm 375 mg/min", "d-tm"), ("r3", "Quatro vias", "g-vias"), ("r4", "Art. 23 do CEM", "g-etica")])]
EXERCICIOS = [("Perguntas oficiais do caso (12)", [("q1", "1: DM", S(1791054010222)), ("q2", "2: insulina", "c-anabolica"), ("q3", "3: tipo", "a-caso"), ("q4", "4: transportadores", "d-km"), ("q5", "5: Kussmaul", "e-gasometria"),
   ("q6", "6: água e eletrólitos", "e-k-total"), ("q7", "7: DM2", S(1791054012447)), ("q8", "8: autoimunidade e infecção", "e-desencadeantes"), ("q9", "9: complicações", "g-vias"), ("q10", "10: MCP", "g-adesao"),
   ("q11", "11: não farmacológico", "g-exercicio"), ("q12", "12: ética", "g-etica")])]
