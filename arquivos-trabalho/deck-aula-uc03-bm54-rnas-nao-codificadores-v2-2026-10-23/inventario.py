"""Inventário atômico da 54 RNAs não codificadores (UC03 P3; Biologia Molecular; Prof. Alexandre Bruni-Cardoso; 86 lâminas), escrito em
23/10 (refação v8) a partir do material lido: lâminas I (1–42, aula de 2026) e II (43–86, versão anterior, a que a fala acompanha) vistas em
visual/folha-01..15; a fala inteira (anotações do PDF da turma, fontes/transcricao-fala.txt); exercícios 4–6; provas biomol-09; Alberts cap. 7.
Blocos e papéis: compreensao-aula.json. Destinos preenchidos depois da busca (E4).
"""
PREFIXO = "bm54"
AULA = "RNAs não codificadores (UC03 P3; Biologia Molecular; Prof. Alexandre Bruni-Cardoso)"
EXC = "EXC: "
_C = "conteudo"
D = {"p1-1": ["au-rna-regula"], "p2-1": ["au-trp-alto", "ak1467833424428"], "p2-2": ["au-trp-baixo"], "p2-3": ["au-trp-acoplada"], "p3-1": ["au-riboswitch"], "p4-1": ["au-crispr-memoria"], "p4-2": ["ak1519849576725", "ak1519849478653", "au-crispr-pam"], "p5-1": ["ak1519849762394", "ak1516938350345", "au-crispr-nhej"], "p5-2": ["ak1519850675647", "sh-1792241904671"], "p6-1": ["ak1468605745938", "au-fire-mello"], "p6-2": ["au-sirna-via", "ak1728260304903"], "p6-3": ["au-sirna-recicla"], "p6-4": ["au-dicer-mutante"], "p6-5": ["au-interferon-dsrna", "ak1497450277629"], "p6-6": ["au-knockdown"], "p6-7": ["au-rnai-defesa"], "p7-1": ["ak1467927177492", "au-mirna-biogenese"], "p7-2": ["ak1467927184068", "au-mirna-imperfeito", "ak1467927104082"], "p7-3": ["au-mirna-sirna", "ak1467927192491"], "p7-4": ["au-mirna-biogenese"], "p8-1": ["au-x-mosaico", "ak1469146766774", "ak1469146770793"], "p8-2": ["au-x-portadora"], "p8-3": ["au-xist"], "p8-4": ["au-xi-marcas", "ak1467682194916"], "p8-5": ["au-xist-posicional"]}  # item do mapa → chaves dos cards (preenchido depois da busca, 23/10)

def _d(k):
    v = D.get(k, [])
    return v if len(v) != 1 else v[0]

SLIDES = [
 (1, "capa", "Capa", []),
 (2, _C, "RNAs com funções além de codificar", [("2a", "RNAs regulatórios além de mRNA, tRNA e rRNA", _d("p1-1"))]),
 (3, _C, "RNA assume estruturas terciárias", [("3a", "Fita simples dobra em estrutura funcional", _d("p1-1"))]),
 (4, _C, "Dobra, pareamento, recrutar proteínas", [("4a", "Dobra, pareamento e arcabouço", _d("p1-1"))]),
 (5, "logistica", "Tópicos", []),
 (6, "logistica", "Roteiro: atenuação", []),
 (7, _C, "Operon trp: repressor e atenuador", [("7a", "Além do repressor, a atenuação", _d("p2-1"))]),
 (8, _C, "Líder com quatro regiões", [("8a", "Líder com códons de Trp e regiões 1–4", _d("p2-1")), ("8b", "Transcrição e tradução acopladas", _d("p2-3"))]),
 (9, _C, "Trp alto × baixo", [("9a", "Trp alto: 3:4 termina", _d("p2-1")), ("9b", "Trp baixo: 2:3 e continua", _d("p2-2"))]),
 (10, "logistica", "Roteiro: riboswitch", []),
 (11, _C, "Riboswitch na transcrição e na tradução", [("11a", "Molécula pequena muda a dobra e esconde RBS ou forma terminador", _d("p3-1"))]),
 (12, "logistica", "Roteiro: CRISPR", []),
 (13, _C, "CRISPR como imunidade bacteriana", [("13a", "Espaçador de fago → crRNA → Cas corta", _d("p4-1"))]),
 (14, _C, "crRNA + tracrRNA + Cas9", [("14a", "Cas9 guiada corta o DNA alvo", _d("p4-1"))]),
 (15, _C, "CRISPR natural × de laboratório (sgRNA)", [("15a", "sgRNA funde crRNA e tracrRNA", _d("p4-2"))]),
 (16, _C, "Edição: PAM, NHEJ × HDR", [("16a", "PAM limita o corte", _d("p4-2")), ("16b", "NHEJ → indel → nocaute", _d("p5-1")), ("16c", "HDR com molde → edição precisa", _d("p5-2"))]),
 (17, _C, "Anemia falciforme editada", [("17a", "Corrigir a mutação com molde", _d("p5-2"))]),
 (18, "fora_do_recorte", "Nobel 2020 e livro", []),
 (19, "logistica", "Roteiro: RNAi", []),
 (20, _C, "RNAi: definição; Nobel 2006", [("20a", "dsRNA complementar interfere com o gene", _d("p6-1"))]),
 (21, _C, "Fire e Mello em C. elegans", [("21a", "Só a dupla fita silencia", _d("p6-1"))]),
 (22, _C, "Via do siRNA", [("22a", "Dicer → siRNA → RISC → Argonauta corta", _d("p6-2")), ("22b", "mRNA degradado e RISC reciclado", _d("p6-3")), ("22c", "Mutante dicer (exercício 4)", _d("p6-4"))]),
 (23, _C, "RNAi para estudar função: knockdown", [("23a", "Knockdown por siRNA em lipossomo", _d("p6-6"))]),
 (24, "fora_do_recorte", "Patisiran (2018)", []),
 (25, _C, "miRNA como processo endógeno", [("25a", "miRNAs de genes próprios; lin-4; >60% dos mRNAs", _d("p7-1"))]),
 (26, _C, "Genes de miRNA: intrônicos, intergênicos, policistrônicos", [("26a", "Policistrônico porque não codifica proteína", _d("p7-4"))]),
 (27, _C, "Drosha no núcleo; pré-miRNA exportado", [("27a", "Drosha corta o pri-miRNA no núcleo", _d("p7-1"))]),
 (28, _C, "Dicer no citoplasma; RISC; repressão ou degradação", [("28a", "Dicer gera o duplex e entra no RISC", _d("p7-1")), ("28b", "Repressão da tradução", _d("p7-2"))]),
 (29, _C, "Pareamento imperfeito; muitos alvos", [("29a", "Imperfeito: bloqueia tradução", _d("p7-2")), ("29b", "Muitos alvos (lin-14 com 7 sítios)", _d("p7-3"))]),
 (30, _C, "miRNA e siRNA na mesma via", [("30a", "Mesma via; siRNA corta e recicla, miRNA reprime e vai ao corpo P", _d("p7-3"))]),
 (31, "fora_do_recorte", "E o Nobel do miRNA?", []),
 (32, "fora_do_recorte", "Nobel 2024", []),
 (33, "logistica", "Roteiro: lncRNA", []),
 (34, _C, "lncRNAs: arcabouço, cis e trans", [("34a", "lncRNA serve de arcabouço entre proteínas e DNA", _d("p8-3"))]),
 (35, _C, "Desbalanço de dose", [("35a", "Duas cópias do X em fêmeas", _d("p8-1"))]),
 (36, _C, "Inativação aleatória e herdada; mosaico", [("36a", "Escolha aleatória, herdada, mosaico", _d("p8-1"))]),
 (37, _C, "Portadoras heterozigotas assintomáticas", [("37a", "Mosaico protege a portadora", _d("p8-2"))]),
 (38, _C, "Gata calico", [("38a", "Calico é fêmea porque é mosaico", _d("p8-2"))]),
 (39, _C, "Xist recobre e recruta", [("39a", "Xist do X a inativar recobre e recruta repressores", _d("p8-3")), ("39b", "Efeito posicional", _d("p8-5"))]),
 (40, _C, "Pergunta: que marcas no Xi?", [("40a", "Prever marcas do Xi", _d("p8-4"))]),
 (41, _C, "Xi: pouca acetilação, muita metilação", [("41a", "acH3/acH4 baixos, meK9H3 alto", _d("p8-4"))]),
 (42, "capa", "Bibliografia", []),
 (43, "capa", "Versão anterior: capa e bibliografia (Watson cap. 20)", []),
 (44, _C, "Objetivos (versão anterior)", [("44a", "RNAi, siRNA × miRNA, prever experimentos, Xist", _d("p6-2"))]),
 (45, _C, "Visão geral (versão anterior)", [("45a", "Dobra, pareamento, arcabouço", _d("p1-1"))]),
 (46, "logistica", "Roteiro", []),
 (47, _C, "Atenuação (versão anterior)", [("47a", "Trp alto × baixo", _d("p2-2"))]),
 (48, "logistica", "Roteiro", []),
 (49, _C, "CRISPR: matriz, espaçadores, crRNAs", [("49a", "Espaçadores parecidos com fagos", _d("p4-1"))]),
 (50, _C, "sgRNA, alvo de 20 nt e PAM", [("50a", "Guia de 20 nt ao lado do PAM", _d("p4-2"))]),
 (51, _C, "NHEJ × HDR", [("51a", "Indel × edição precisa", _d("p5-1"))]),
 (52, "logistica", "Roteiro", []),
 (53, _C, "Fire e Mello", [("53a", "dsRNA suprime o gene", _d("p6-1"))]),
 (54, "fora_do_recorte", "Nobel 2006", []),
 (55, _C, "Experimento em C. elegans", [("55a", "Senso e antissenso sem efeito; dsRNA silencia", _d("p6-1"))]),
 (56, _C, "A via de RNAi", [("56a", "Dicer, RISC, Argonauta", _d("p6-2"))]),
 (57, "fora_do_recorte", "Vídeo", []),
 (58, _C, "RNAi por siRNA", [("58a", "Degradação do mRNA complementar", _d("p6-3"))]),
 (59, _C, "RNAi como ferramenta", [("59a", "Bloquear função de genes de modo dirigido", _d("p6-6"))]),
 (60, _C, "Knockdown por lipossomo", [("60a", "Knockdown transitório", _d("p6-6"))]),
 (61, _C, "shRNA por lentivírus", [("61a", "shRNA integrado: knockdown permanente", _d("p6-6"))]),
 (62, _C, "Vermes × mamíferos", [("62a", "Mamíferos: siRNA curto", _d("p6-5"))]),
 (63, _C, "dsRNA longo em mamíferos: interferon", [("63a", "PKR/eIF2α e RNase L param tudo", _d("p6-5"))]),
 (64, _C, "Triagem de genomas; siRNA endógeno raro", [("64a", "siRNA endógeno é raro", _d("p6-7"))]),
 (65, _C, "Origem dos siRNAs naturais", [("65a", "Vírus e transposons", _d("p6-7"))]),
 (66, _C, "RNAi convergiu com os miRNAs", [("66a", "Mesma maquinaria dos miRNAs", _d("p7-3"))]),
 (67, _C, "RNAi como processo natural: miRNAs", [("67a", "miRNAs em grampo, processados pela Dicer", _d("p7-1"))]),
 (68, _C, "Genes de miRNA", [("68a", "Intrônicos, intergênicos, clusters", _d("p7-4"))]),
 (69, _C, "Drosha", [("69a", "Drosha no núcleo; pré-miRNA exportado", _d("p7-1"))]),
 (70, _C, "Dicer e RISC", [("70a", "Dicer no citoplasma", _d("p7-1"))]),
 (71, _C, "RISC: corte com pareamento perfeito", [("71a", "Argonauta corta só com complementaridade perfeita", _d("p7-2"))]),
 (72, _C, "RISC: pareamento imperfeito inibe tradução", [("72a", "Imperfeito: supressão da tradução", _d("p7-2"))]),
 (73, _C, "miRNA pós-transcricional; muitos alvos", [("73a", "Muitos alvos", _d("p7-3"))]),
 (74, _C, "Mesma via (Dicer e RISC)", [("74a", "Degradação × inibição", _d("p7-3"))]),
 (75, _C, "RISC/siRNA reciclado × RISC/miRNA preso", [("75a", "Reciclado × preso ao mRNA", _d("p7-3"))]),
 (76, _C, "Corpos P", [("76a", "Argonauta e DCP1a no corpo P", _d("p7-2"))]),
 (77, "fora_do_recorte", "miRNAs e metástase (versão anterior)", []),
 (78, "fora_do_recorte", "miR-31 × capacidade metastática", []),
 (79, "fora_do_recorte", "miR-31 impede metástase", []),
 (80, "fora_do_recorte", "Alvos do miR-31", []),
 (81, "fora_do_recorte", "miR-31 bloqueia metástases", []),
 (82, "logistica", "Roteiro", []),
 (83, _C, "Xist e inativação do X (versão anterior)", [("83a", "32–64 células; mosaico; portadoras", _d("p8-1"))]),
 (84, _C, "Xist recobre e recruta", [("84a", "Arcabouço para repressores", _d("p8-3"))]),
 (85, _C, "Pergunta das marcas", [("85a", "Prever marcas", _d("p8-4"))]),
 (86, _C, "Marcas do Xi", [("86a", "Hipoacetilação e metilação", _d("p8-4"))]),
]
JUSTIFICATIVAS = {"capa": "capa ou bibliografia, sem conteúdo", "logistica": "roteiro ou divisória que repete os tópicos",
 "fora_do_recorte": "prêmio, livro, vídeo ou exemplo que saiu das lâminas de 2026 (miR-31); o conceito está no card vizinho ou em mapa.fora"}
CAPITULO = [("Alberts 5ª ed., cap. 7 (RNAs reguladores; inativação do X)", [
 ("l1", "Argonauta corta com pareamento extenso; sem corte, repressão e corpo P", _d("p7-2")),
 ("l2", "RNAi como defesa contra vírus e transposons", _d("p6-7")),
 ("l3", "X inativo herdado, mosaico, Polycomb", _d("p8-1"))])]
EXERCICIOS = [
 ("Exercícios de BM - RNAs não codificantes", [
  ("e4", "dsRNA de bicóide; mutante dicer", _d("p6-4")), ("e5", "Reparo essencial ao CRISPR", _d("p5-1")),
  ("e6", "XIST no cromossomo 21; marcas e manutenção", _d("p8-5"))]),
 ("Provas biomol-09", [
  ("q1", "Mecanismos do miRNA (2025 P3 1.6)", _d("p7-2")), ("q2", "Como ncRNAs regulam (2024 P3 2.8)", _d("p1-1")),
  ("q3", "Geração e ação do miR-31 (2019 P4 1.2)", _d("p7-1"))])]
