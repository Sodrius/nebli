"""Inventário atômico de RNAs não codificadores (UC03 P3, Biologia Molecular; Prof. Alexandre Bruni-Cardoso; pasta pessoal 54 vazia).
Escrito em 10/10/2026 antes da seleção. Lâminas 1–42 = "RNAs Não Codificantes I" (aula atual); 43–86 = "RNAs Não Codificantes II"
(versão anterior com objetivos, mamíferos/interferon, RISC, P-bodies, miR-31 e X aos 32–64 blastômeros). A "transcrição" da turma é o
texto da versão II. Exercícios da turma (RNAi bicóide/dicer, CRISPR e reparo, XIST na trissomia 21) e provas biomol-09 (6 subquestões).
"""
PREFIXO = "bm54"
AULA = "RNAs não codificadores (UC03 P3; Prof. Alexandre Bruni-Cardoso)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "RNAs têm funções além de codificar", [("ncrna", "RNAs não codificadores regulam genes", "mirna-def")]),
 (3, "conteudo", "Estruturas terciárias funcionais", [("estrutura", "RNA dobra em estrutura funcional", "riboswitch")]),
 (4, "conteudo", "Visão geral", [
   ("pareamento", "RNA reconhece RNA/DNA complementar por pareamento", "pareamento"),
   ("cromatina", "RNA recruta proteínas para a cromatina", "lnc-scaffold")]),
 (5, "conteudo", "Tópicos", [("topicos", "Procariotos, RNAi, lncRNAs", ["cis", "trans"])]),
 (6, "conteudo", "Cis × trans", [("cis-trans", "Atenuação e riboswitch em cis; CRISPR em trans", ["cis", "trans"])]),
 (7, "conteudo", "trp: repressor e atenuador", [("trp-dupla", "Operon trp regulado por repressor e atenuação", "trp-atenuacao")]),
 (8, "conteudo", "Líder e atenuador", [("lider", "Peptídeo líder e regiões 1–4", ["trp-alto", "trp-baixo"])]),
 (9, "conteudo", "Trp alto × baixo", [
   ("alto", "Trp alto: ribossomo completa o líder, grampo 3:4 termina", "trp-alto"),
   ("baixo", "Trp baixo: ribossomo para nos códons Trp, grampo 2:3 deixa continuar", "trp-baixo"),
   ("acoplamento", "Depende de transcrição e tradução acopladas", "acoplamento")]),
 (10, "capa", "Divisória: riboswitches", []),
 (11, "conteudo", "Riboswitches", [
   ("rs-def", "Na 5'-UTR; mudam estrutura ao ligar pequena molécula", "riboswitch"),
   ("rs-alvo", "Regulam transcrição (terminador) ou tradução (RBS)", "riboswitch-rbs")]),
 (12, "capa", "Divisória: CRISPR", []),
 (13, "conteudo", "CRISPR como imunidade bacteriana", [
   ("imune", "Sistema imune adaptativo bacteriano", "crispr-imune"),
   ("espacadores", "DNA viral integrado entre repetições; crRNA guia Cas", "espacadores")]),
 (14, "conteudo", "crRNA + tracrRNA + Cas9", [("tracr", "crRNA pareia com tracrRNA; Cas9 corta", "tracrrna")]),
 (15, "conteudo", "Natural × laboratório", [("sgrna", "Fusão crRNA+tracrRNA = gRNA", "sgrna")]),
 (16, "conteudo", "Edição com Cas9", [
   ("cas9", "Cas9 + guia em qualquer organismo", ["crispr-ferramenta", "cas9-guia"]),
   ("pam", "PAM", "pam"),
   ("nhej", "NHEJ → indel → knockout", ["nhej-knockout", "nhej-erro"]),
   ("hdr", "HDR com molde → corrigir/adicionar", "molde-knockin")]),
 (17, "conteudo", "Anemia falciforme editada", [("falciforme", "Terapia aprovada em 2023", "falciforme")]),
 (18, "conteudo", "Nobel 2020", [("nobel-crispr", "Charpentier e Doudna", EXC + "histórico de prêmio")]),
 (19, "conteudo", "Tópicos: eucariotos em trans", [("euc", "RNAi, siRNA, miRNA, lncRNA", "trans")]),
 (20, "conteudo", "RNAi: definição e Nobel 2006", [
   ("rnai-def", "dsRNA complementar interfere com expressão", "rnai"),
   ("nobel-rnai", "Fire e Mello, 2006", EXC + "histórico de prêmio; o experimento está em fire-mello")]),
 (21, "conteudo", "Experimento em C. elegans", [("fire-mello", "Só a dupla-fita silenciou", "fire-mello")]),
 (22, "conteudo", "Via do siRNA", [
   ("dicer", "Dicer corta dsRNA em siRNA de 21 pb", "dicer"),
   ("risc", "RISC descarta a fita senso", "risc-fita"),
   ("argonauta", "Argonauta cliva o mRNA", "argonauta")]),
 (23, "conteudo", "RNAi para estudar genes", [("knockdown", "Knockdown", "rnai")]),
 (24, "conteudo", "Patisiran", [("patisiran", "siRNA contra TTR na amiloidose", "patisiran")]),
 (25, "conteudo", "RNAi endógena: miRNA", [
   ("mirna-genoma", "miRNAs codificados no próprio genoma, grampos", "sirna-mirna"),
   ("lin4", "lin-4 → lin-14 em C. elegans (1993)", "lin4"),
   ("alvos", "~3000 miRNAs; regulam >60% dos mRNAs", "muitos-alvos")]),
 (26, "conteudo", "Genes de miRNA", [("loc", "Intrônicos, intergênicos, clusters; pri-miRNA em grampo", "sirna-mirna")]),
 (27, "conteudo", "Drosha e exportina 5", [
   ("drosha", "Drosha → pré-miRNA ~70 nt", "drosha"),
   ("exportina", "Exportina 5 leva ao citoplasma", "exportina")]),
 (28, "conteudo", "Dicer e RISC no miRNA", [("dicer-mirna", "Dicer → dúplex ~22 nt; RISC silencia", ["dicer", "mirna-silencia"])]),
 (29, "conteudo", "miRNA pós-transcricional", [
   ("imperfeito", "Pareamento imperfeito (exceto plantas); reprime tradução", "imperfeito"),
   ("3utr", "Sítios na 3'-UTR (lin-14)", "utr3"),
   ("muitos", "Muitos alvos", "muitos-alvos")]),
 (30, "conteudo", "Via comum Dicer/RISC", [("comum", "siRNA e miRNA compartilham Dicer e RISC", ["mirna-def", "sirna-mirna"])]),
 (31, "conteudo", "Nobel do miRNA", [("nobel-mirna", "Ambros e Ruvkun", EXC + "histórico de prêmio; a descoberta está em lin4")]),
 (32, "conteudo", "Link da aula de Ruvkun", [("link", "Vídeo", EXC + "link externo")]),
 (33, "conteudo", "Tópicos: lncRNAs", [("lnc-top", "Xist como exemplo", "xist")]),
 (34, "conteudo", "lncRNAs", [
   ("lnc-tam", ">200 nt, sofrem splicing, às vezes antissenso", "lnc-200"),
   ("lnc-scaf", "Arcabouço para proteínas e DNA; cis e trans", "lnc-scaffold")]),
 (35, "conteudo", "Desbalanço de dose", [("dose", "Fêmeas com dois X", "dose")]),
 (36, "conteudo", "Inativação aleatória e mosaico", [
   ("aleatoria", "Um X inativado ao acaso no embrião, herdado", "aleatoria"),
   ("mosaico", "Fêmeas são mosaicos", "mosaico")]),
 (37, "conteudo", "Portadoras assintomáticas", [("portadoras", "Heterozigotas podem ser assintomáticas", "portadoras")]),
 (38, "conteudo", "Gato calico", [("calico", "Calico são fêmeas", "calico")]),
 (39, "conteudo", "Xist", [
   ("xist-def", "lncRNA Xist, ~20 kb", "xist"),
   ("xist-recobre", "Transcrito do X a inativar; recobre o X", "xist-recobre"),
   ("xist-recruta", "Recruta modificadores da cromatina", ["xi-histonas", "barr-heterocromatina"])]),
 (40, "conteudo", "Pergunta: marcas no Xi", [("pergunta", "Quais marcas altas e baixas?", "xi-histonas")]),
 (41, "conteudo", "Marcas do X inativo", [("marcas", "Baixa acetilação, alta metilação de histonas", ["xi-histonas", "lionizacao", "metilacao-citosina"])]),
 (42, "capa", "Bibliografia", []),
 (43, "capa", "Versão anterior: capa/bibliografia", []),
 (44, "conteudo", "Objetivos (versão anterior)", [("objetivos", "RNAi, siRNA × miRNA, prever experimentos, Xist", ["rnai", "sirna-mirna", "xist"])]),
 (45, "conteudo", "Visão geral (versão anterior)", [("visao2", "Funções do RNA", "pareamento")]),
 (46, "conteudo", "Procariotos (versão anterior)", [("proc2", "Atenuação e riboswitch em cis", "cis")]),
 (47, "conteudo", "Figura sem texto", [("fig47", "Figura de atenuação/riboswitch", "trp-atenuacao")]),
 (48, "conteudo", "CRISPR em trans (versão anterior)", [("trans2", "sgRNA em trans", "trans")]),
 (49, "conteudo", "CRISPR bacteriano (versão anterior)", [("crispr2", "Imunidade bacteriana", "crispr-imune")]),
 (50, "conteudo", "CRISPR para manipulação (versão anterior)", [("crispr3", "Ferramenta", "crispr-ferramenta")]),
 (51, "conteudo", "CRISPR: links", [("links", "Vídeos e linha do tempo", EXC + "links externos")]),
 (52, "conteudo", "Tópicos (versão anterior)", [("top2", "Eucariotos em trans", "trans")]),
 (53, "conteudo", "Fire e Mello (versão anterior)", [("fm2", "dsRNA injetado suprime gene", "fire-mello")]),
 (54, "conteudo", "Definição de RNAi (versão anterior)", [("rnai2", "Definição", "rnai")]),
 (55, "conteudo", "C. elegans (versão anterior)", [("cel2", "Experimento", "fire-mello")]),
 (56, "conteudo", "Via do siRNA (versão anterior)", [("via2", "Dicer, RISC, Argonauta", ["dicer", "risc-fita", "argonauta"])]),
 (57, "conteudo", "Figura sem texto", [("fig57", "Via de RNAi", "dicer")]),
 (58, "conteudo", "siRNA degrada mRNA", [("degrada", "RNAi degrada mRNA complementar", "argonauta")]),
 (59, "conteudo", "RNAi como ferramenta", [("ferramenta", "Bloqueio dirigido de genes", "rnai")]),
 (60, "conteudo", "Knockdown (versão anterior)", [("kd2", "Knockdown", "rnai")]),
 (61, "conteudo", "Figura sem texto", [("fig61", "Knockdown", "rnai")]),
 (62, "conteudo", "dsRNA longo × siRNA", [("moscas", "Moscas e vermes: dsRNA longo; mamíferos: siRNA", "interferon")]),
 (63, "conteudo", "Interferon em mamíferos", [("ifn", "dsRNA longo → interferon, bloqueio geral da tradução", "interferon")]),
 (64, "conteudo", "Triagem e siRNAs endógenos raros", [("triagem", "Triagem de genomas; siRNAs endógenos raros", "rnai")]),
 (65, "conteudo", "Origem dos siRNAs naturais", [("origem", "Vírus e transposons; Dicer gera 21–23 nt", "sirna-origem")]),
 (66, "conteudo", "Convergência com miRNAs", [("conv", "RNAi convergiu com miRNAs", "sirna-mirna")]),
 (67, "conteudo", "RNAi natural = miRNAs", [("natural", "miRNAs em grampo; centenas em mamíferos", ["sirna-mirna", "mirna-def"])]),
 (68, "conteudo", "Genes de miRNA (versão anterior)", [("loc2", "Localização e pri-miRNA", "sirna-mirna")]),
 (69, "conteudo", "Drosha (versão anterior)", [("drosha2", "Drosha e exportina 5", ["drosha", "exportina"])]),
 (70, "conteudo", "Dicer e RISC (versão anterior)", [("dicer2", "Dúplex ~22 nt", "dicer")]),
 (71, "conteudo", "RISC: pareamento perfeito", [("perfeito", "Argonauta cliva só com pareamento perfeito", "argonauta")]),
 (72, "conteudo", "RISC: pareamento imperfeito", [("imperfeito2", "Imperfeito → supressão da tradução", "imperfeito")]),
 (73, "conteudo", "miRNA pós-transcricional (versão anterior)", [("pos2", "Mesmo conteúdo da lâmina 29", ["imperfeito", "utr3", "muitos-alvos"])]),
 (74, "conteudo", "Dicer em precursor e dúplex", [("ab", "miRNA de precursor; siRNA de dúplex", "sirna-mirna")]),
 (75, "conteudo", "RISC reciclado × associado", [("recicla", "RISC/siRNA reciclado; RISC/miRNA fica no mRNA", "recicla")]),
 (76, "conteudo", "Corpos P", [("pbody", "DCP1a e Argonauta em P-bodies", "p-bodies")]),
 (77, "conteudo", "miRNAs e metástase", [("met", "miRNAs alterados na metástase", "mirna-cancer")]),
 (78, "conteudo", "miR-31 inverso à metástase", [("mir31-niveis", "miR-31 cai nas linhagens metastáticas", "mir31")]),
 (79, "conteudo", "miR-31 impede metástase in vivo", [("mir31-vivo", "Expressão de miR-31 reduz metástase pulmonar", "mir31-supressor")]),
 (80, "conteudo", "Alvos do miR-31", [("mir31-3utr", "Busca de 3'-UTR complementar; repórter", ["utr3", "mir31-supressor"])]),
 (81, "conteudo", "miR-31 bloqueia metástase", [("mir31-genes", "ITGA5, RhoA, RDX; alvo terapêutico", "mir31-supressor")]),
 (82, "conteudo", "Tópicos (versão anterior)", [("top3", "Xist", "xist")]),
 (83, "conteudo", "Inativação do X (versão anterior)", [("x-32", "Embrião de 32–64 células; mosaico; portadoras", ["aleatoria", "mosaico", "portadoras"])]),
 (84, "conteudo", "Xist (versão anterior)", [("xist2", "Transcrito do Xi, recobre e recruta", ["xist", "xist-recobre"])]),
 (85, "conteudo", "Pergunta (versão anterior)", [("perg2", "Marcas do Xi", "xi-histonas")]),
 (86, "conteudo", "Marcas do Xi (versão anterior)", [("marcas2", "Baixa acetilação, alta metilação", "xi-histonas")]),
]
JUSTIFICATIVAS = {"capa": "capa, divisória ou bibliografia, sem conteúdo"}

CAPITULO = [("Alberts 5ª ed., cap. 7 (pdf pp. 509–534): inativação do X, ribocontrole/atenuação, miRNA e RNAi", [
   ("ab-x", "Inativação do X por Xist; X inativo com histonas hipoacetiladas e metiladas", ["xist", "xist-recobre", "xi-histonas"]),
   ("ab-atenuacao", "Atenuação da transcrição e riboswitches", ["trp-alto", "riboswitch"]),
   ("ab-mirna", "Processamento do miRNA (Drosha, Dicer), RISC; pareamento perfeito cliva, imperfeito reprime", ["drosha", "dicer", "imperfeito"]),
   ("ab-rnai", "RNAi como defesa contra vírus/transposons e ferramenta experimental", ["sirna-origem", "rnai"])])]

EXERCICIOS = [
 ("Exercícios da turma (RNAs não codificadores)", [
   ("ex4", "dsRNA bicóide fenocopia o mutante; no mutante dicer só siRNAs curtos funcionam", ["fire-mello", "dicer"]),
   ("ex5", "Reparo NHEJ e homólogo são essenciais ao CRISPR", ["nhej-knockout", "molde-knockin"]),
   ("ex6", "XIST para compensar a trissomia 21; marcas mantidas", ["xist-down", "xi-histonas"])]),
 ("Provas UC03 (índice biomol-09)", [
   ("p2025", "2025 P3 1.6: mecanismos do miRNA (degradação, tradução, RISC)", ["imperfeito", "argonauta", "mirna-silencia"]),
   ("p2024-lnc", "2024 P3 2.8: como ncRNAs regulam (lncRNA na cromatina; miRNA)", ["lnc-scaffold", "mirna-def"]),
   ("p2024-mir", "2024 P3 2.9: validar miR-A com repórter", "utr3"),
   ("p2019", "2019 P4 1.2–1.3: biogênese do miR-31; supressor tumoral", ["drosha", "mir31-supressor"])]),
]
