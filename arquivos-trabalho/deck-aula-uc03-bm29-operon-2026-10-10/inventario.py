"""Inventário atômico de Regulação da expressão gênica em procariotos: o modelo do operon (UC03 P2, Biologia Molecular, aula 29;
Prof. Alexandre Bruni-Cardoso; 46 lâminas da pasta pessoal = versão I da turma). Escrito em 10/10/2026 antes da seleção: lâminas
(visual/folha-NN), versão II da turma (fontes/turma2.txt, objetivos), transcrições I–IV (fontes/transcricao.txt), exercícios da aula 29,
provas do índice biomol-05 (2019 P2 2.6–2.9, 2024 P2 1.12–1.13, 2025 P2 1.9), monitoria P2 aula 3 (fontes/monitoria-p2.txt; erro notado:
chama o promotor de "primer"), apostila guia de veteranos aula 3 (fontes/guia-veteranos-bm.txt), Lehninger cap. 28 (livros/lehninger-28.txt).
"""
PREFIXO = "bm29"
AULA = "Regulação da expressão gênica em procariotos: o modelo do operon (UC03 P2; Prof. Alexandre Bruni-Cardoso)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Dogma central", [("dogma", "Revisão: replicação, transcrição, tradução", EXC + "revisão de UC01/UC02")]),
 (3, "conteudo", "Níveis de regulação", [("iniciacao", "Iniciação da transcrição é o controle mais importante", "niveis"),
                                         ("camadas", "Regulação pós-transcricional, traducional, pós-traducional", "outros-niveis"),
                                         ("rearranjo", "Rearranjo do DNA (inversão do promotor de fímbrias; transcrição)", "rearranjo")]),
 (4, "conteudo", "Pontuação da transcrição", [("mais-um", "+1, promotor a montante, terminador a jusante", "pontuacao")]),
 (5, "conteudo", "Reguladores da expressão", [("basal-rep-ativ", "Nível basal, repressão por repressor, ativação por ativador", ["neg-pos", "lac-fraco"])]),
 (6, "conteudo", "Elementos cis e trans", [("cis-trans", "cis = DNA (promotor, operador); trans = proteínas", ["cis", "trans"])]),
 (7, "conteudo", "Esquema do operon", [("esquema", "Promotor, operador, sítio do ativador, gene regulador, genes estruturais",
                                         ["io-operador", "io-promotor", "io-sitio-ativador", "io-gene-regulador"]),
                                        ("cis-trans-2", "Sequências em cis; produtos em trans", ["cis", "trans"])]),
 (8, "conteudo", "Regulação negativa induzível", [("neg-ind", "Indutor solta o repressor", ["mcat-inducer", "mcat-lac-inducible"])]),
 (9, "conteudo", "Regulação negativa repressível", [("neg-rep", "Co-repressor liga o repressor ao operador", ["corepressor", "mcat-repressible"])]),
 (10, "conteudo", "Regulação positiva induzível", [("pos-ind", "Indutor faz o ativador ligar (CAP–cAMP)", "camp-cap")]),
 (11, "conteudo", "Regulação positiva repressível", [("pos-rep", "Co-repressor solta o ativador", "pos-repressivel")]),
 (12, "conteudo", "Síntese dos termos", [("termos", "Negativa/repressores, positiva/ativadores, indução/indutores, repressão/co-repressores",
                                          ["neg-pos", "mcat-inducer", "corepressor"])]),
 (13, "conteudo", "O operon", [("operon", "Genes sob um promotor, mRNA policistrônico, mesma via", ["mcat-operon", "operon-funcao"])]),
 (14, "conteudo", "mRNA policistrônico", [("poli", "RNA bacteriano policistrônico", "policistronico"), ("rbs", "Um RBS por cistron", "rbs"),
                                           ("mono", "Eucariotos monocistrônicos: cap e varredura (transcrição)", "monocistronico")]),
 (15, "conteudo", "Mapa do operon lac", [("genes", "lacI, P, O, lacZ, lacY, lacA e produtos", ["laci", "lacz", "lacy", "laca"])]),
 (16, "conteudo", "Jacob, Monod e o Nobel", [("historia", "Modelo proposto em 1960; Nobel 1965", "jacob-monod")]),
 (17, "conteudo", "Metabolismo da lactose", [("permease", "Permease importa lactose", "lacy"), ("bgal", "β-galactosidase cliva em glicose + galactose", "lacz"),
                                             ("alolactose", "Alolactose formada pela β-galactosidase", "allolactose-isomero"),
                                             ("condicao", "Lactose presente e glicose ausente", "glicose-preferida")]),
 (18, "conteudo", "Indutibilidade", [("induz", "Enzima só com lactose; lactose é indutor", ["por-que-induzir", "mcat-lac-inducible"])]),
 (19, "conteudo", "Regulação negativa induzível do lac", [("repressor", "Repressor no operador reprime", ["operador-bloqueia", "mcat-operator", "repressao-1000x"])]),
 (20, "conteudo", "Lactose presente", [("solta", "Lactose (alolactose) solta o repressor", ["lac-repressor-sai", "mcat-allolactose"])]),
 (21, "conteudo", "Classes de mutantes", [("classes", "Não induzíveis × constitutivos", ["laci-menos", "laci-s"])]),
 (22, "conteudo", "Que mutações?", [("pergunta", "Que mutações levam a esses fenótipos", ["laci-menos", "laci-s"])]),
 (23, "conteudo", "Mutações possíveis", [("lacis", "lacIS não liga indutor", "laci-s"), ("lacz", "lacZ− não induzível", "lacz-menos"),
                                          ("laci", "lacI− constitutivo", "laci-menos"), ("oc", "Oc constitutivo", "oc"),
                                          ("lacy-p", "lacY− e promotor (transcrição)", ["lacy-menos", "promotor-mutacao"])]),
 (24, "conteudo", "Ferramentas", [("iptg", "Análogo não metabolizável (IPTG)", ["iptg", "iptg-porque"]), ("xgal", "X-gal monitora β-galactosidase", ["xgal", "xgal-nao-indutor"]),
                                   ("merozigoto", "Merozigotos por conjugação", "merozigoto")]),
 (25, "conteudo", "Placa com colônias azuis e brancas", [("placa", "Triagem de mutantes pela cor", "colonias")]),
 (26, "conteudo", "Pergunta: segunda cópia com lacI−", [("p-laci", "Diploide I−/I+ fica induzível", "dip-laci")]),
 (27, "conteudo", "Diploide parcial lacI−", [("trans", "lacI− recessivo; repressor atua em trans", ["dip-laci", "dip-trans-teste", "dip-is"])]),
 (28, "conteudo", "Pergunta: segunda cópia com lacO−", [("p-oc", "Diploide Oc/O+ fica constitutivo", "dip-oc")]),
 (29, "conteudo", "Diploide parcial Oc", [("cis", "Oc dominante; operador atua em cis", ["dip-oc", "dip-oc-cis", "dip-cis-teste"])]),
 (30, "conteudo", "Repressor tetrâmero", [("tetramero", "Tetrâmero de dois dímeros", "tetramero")]),
 (31, "conteudo", "Ligação ao DNA", [("hth", "HTH N-terminal; dímero no sítio palindrômico", ["hth", "tetramero"])]),
 (32, "conteudo", "Indutor muda a conformação", [("alosterico", "Proteína alostérica sensora", ["alosterico", "mcat-allolactose"])]),
 (33, "conteudo", "Sobreposição repressor × RNA polimerase", [("sobrepoe", "DNA coberto pelo repressor sobrepõe o da polimerase", ["operador-bloqueia", "mcat-operator"])]),
 (34, "conteudo", "Problema: expressão basal", [("basal", "Expressão basal permite a entrada de lactose", ["basal", "feedback"])]),
 (35, "conteudo", "Regulação integrada", [("tabela", "Glicose × lactose: basal, repressão, ativação",
                                            ["cond-basal", "cond-forte", "cond-sem-lactose", "cond-nada", "mcat-duas-condicoes", "repressao-catabolica"])]),
 (36, "conteudo", "CAP", [("cap", "CAP a montante do promotor; CAP = CRP", ["cap", "crp", "cap-perda"]), ("actd", "Contato com αCTD (figura)", "alfa-ctd")]),
 (37, "conteudo", "CAP liga DNA só com cAMP", [("camp", "cAMP alto com glicose baixa", ["glicose-camp", "camp-cap", "glicose-indireta"])]),
 (38, "conteudo", "Anatomia do promotor", [("elementos", "−10 e −35, ~17 pb", ["menos10-35", "consenso-seq"])]),
 (39, "conteudo", "Matriz consenso", [("matriz", "Frequência de bases por posição", ["consenso-def", "consenso-seq"])]),
 (40, "conteudo", "Promotores de E. coli", [("fortes", "Promotores fortes (rRNA, tRNA)", "promotor-genes")]),
 (41, "conteudo", "σ reconhece o promotor", [("sigma", "Subunidade σ liga −35 e −10", "sigma")]),
 (42, "conteudo", "Conformidade ao consenso", [("forca", "Promotor fraco, ativador recruta RNAP", ["promotor-forte", "cap-recruta"])]),
 (43, "conteudo", "Promotor lac × consenso", [("lac", "TTTACA e TATGTT", "lac-fraco")]),
 (44, "conteudo", "CAP a 5′ do promotor", [("sitio", "Sítio CAP a montante", "cap")]),
 (45, "conteudo", "CAP–RNAP compensa o promotor", [("recruta", "Energia livre da interação mantém a RNAP", ["cap-recruta", "alfa-ctd"])]),
 (46, "conteudo", "Síntese", [("sintese", "Lactose via repressor, glicose via CAP", "dois-sensores")]),
]
JUSTIFICATIVAS = {"capa": "capa, sem conteúdo"}

CAPITULO = [("Lehninger 6ª ed., cap. 28 (regulação da expressão gênica, pdf pp. 1187–1199)", [
   ("lh-modos", "Regulação negativa e positiva; sinal molecular liga/solta o regulador", ["neg-pos", "pos-repressivel"]),
   ("lh-operon", "Óperon e mRNA policistrônico com sítio de ribossomo por gene", ["mcat-operon", "rbs"]),
   ("lh-lac", "Genes Z, Y, A; repressor tetramérico codificado por I, difusível", ["lacz", "lacy", "laca", "tetramero", "trans"]),
   ("lh-basal", "Repressão reduz 10^3 vezes; nível basal essencial", ["repressao-1000x", "basal"]),
   ("lh-alolactose", "Indutor é a alolactose; IPTG não metabolizável", ["allolactose-isomero", "iptg"]),
   ("lh-cap", "CRP–cAMP e repressão por catabólito", ["camp-cap", "repressao-catabolica"])])]

EXERCICIOS = [
 ("Exercícios da aula 29", [
   ("ex1", "Esquema do operon e elementos regulatórios; negativa × positiva", ["io-operador", "io-promotor", "io-sitio-ativador", "io-gene-regulador", "neg-pos"]),
   ("ex2", "β-galactosidase em lactose, glicose, + cAMP", ["cond-forte", "cond-basal", "cond-nada", "camp-exogeno"]),
   ("ex3", "Oc dominante, cis, experimento com Z", ["dip-oc", "dip-oc-cis", "dip-cis-teste"]),
   ("ex4", "lacY− não induz", "lacy-menos"),
   ("ex5", "Tabela de merodiploides P/O/I/Z/Y", ["dip-cis-teste", "dip-trans-teste", "promotor-mutacao", "merozigoto"]),
   ("ex6", "Lactose + glicose sem ativação", ["cond-basal", "repressao-catabolica"])]),
 ("Provas UC03 (índice biomol-05)", [
   ("p2025", "2025 P2 1.9: componentes e controle com/sem lactose, CAP–cAMP", ["laci", "repressao-catabolica", "dois-sensores", "iptg"]),
   ("p2024a", "2024 P2 1.12: funcionamento do operon lac", ["lacz", "lacy", "laca", "lac-repressor-sai"]),
   ("p2024b", "2024 P2 1.13: diploide I+ Oc Z+ / I− O+ Z+ com IPTG; dominante, constitutivo, cis", ["dip-cis-teste", "dip-oc", "dip-oc-cis", "iptg"]),
   ("p2019a", "2019 P2 2.6: esquema com Pi, Plac, O, sítio CAP, lacZ", ["laci", "io-sitio-ativador"]),
   ("p2019b", "2019 P2 2.7–2.9: IPTG, X-gal, mutantes por cor de colônia (lacI, CAP, sítio CAP, O, lacZ)",
    ["xgal", "xgal-nao-indutor", "colonias", "cap-perda", "laci-menos"])]),
 ("Monitoria P2, aula 3", [
   ("mon-niveis", "Níveis de regulação (rearranjo, transcrição, tradução, pós-tradução)", ["niveis", "rearranjo"]),
   ("mon-basal", "Repressor não fica ligado o tempo todo", "basal"),
   ("mon-mutantes", "Não induzíveis (Z, Y, promotor) e constitutivos (Ic, Oc)", ["laci-menos", "oc", "lacy-menos"]),
   ("mon-sobrepoe", "Repressor no operador se sobrepõe à CAP", "cond-sem-lactose"),
   ("mon-camp", "Glicose alta reduz cAMP; CAP contata subunidade α", ["glicose-indireta", "alfa-ctd"])]),
 ("Apostila guia de veteranos, aula 3", [
   ("gv-cenarios", "Quatro cenários de glicose e lactose", ["cond-forte", "cond-basal", "cond-sem-lactose", "cond-nada"]),
   ("gv-promotor", "Genes constitutivos com promotores fortes; regulados com fracos", "promotor-genes"),
   ("gv-diploides", "Ic recessivo (trans), Oc dominante (cis)", ["dip-laci", "dip-oc"])]),
 ("Transcrições I–IV", [
   ("tr-competicao", "Indução grande dá vantagem competitiva", "por-que-induzir"),
   ("tr-iptg", "IPTG não é consumido; X-gal não induz", ["iptg-porque", "xgal-nao-indutor"]),
   ("tr-feedback", "Ciclo positivo da permease e volta à repressão", "feedback"),
   ("tr-indireta", "Glicose regula a CAP indiretamente via cAMP", "glicose-indireta")]),
]
