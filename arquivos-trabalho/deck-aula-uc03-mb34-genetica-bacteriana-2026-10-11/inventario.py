"""Inventário atômico de Genética bacteriana (UC03 P2, Microbiologia; Profa. Carla Romano Taddei, ICB II-USP; 44 lâminas de 2026 da pasta pessoal
(`Genetica 2026.pdf`; a pasta da turma tem a versão I/II da mesma aula) + transcrição oficial da aula). Escrito em 11/10/2026 antes da seleção.
Fontes: lâminas (visual/folha-NN), transcrição (fontes/transcricao.txt), Trabulsi cap. 5 (livros/trabulsi-cap5-genetica.txt), provas micro-06
(fontes/provas.txt), guia de veteranos aula 5 e monitoria P2 aula 5 (fontes/guia-veteranos-mb.txt, monitoria-p2.txt), apostila NEBLI (só apoio).
"""
PREFIXO = "mb34"
AULA = "Genética bacteriana (UC03 P2; Microbiologia)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Genética bacteriana", []),
 (2, "conteudo", "Genoma bacteriano: nucleoide", [("nucleoide", "Nucleoide: DNA com HU, H-NS, cátions, poliaminas, RNA", "nucleoide"),
   ("dna-perc", "Genoma ocupa grande fração do volume celular (~80% DNA contra 50% nos eucariotos)", EXC + "afirmação imprecisa de percentual de DNA, sem alvo de prova")]),
 (3, "conteudo", "Formas do DNA e supertorção", [("formas", "Linear nos eucariotos; circular em plasmídeos, mitocondrial, fagos", "sh-1791576675592"),
   ("super", "Forma supertorcida; torção positiva e negativa; forma relaxada", "supertorcido")]),
 (4, "conteudo", "Plasmídeo relaxado e supertorcido em gel", [("gel", "Eletroforese distingue o DNA relaxado do supertorcido", "supertorcido")]),
 (5, "conteudo", "Formas de DNA e supertorção", [("gir", "Girase e topoisomerase interconvertem relaxado e supertorcido", ["girase", "topoisomerase", "sh-1791668521839"])]),
 (6, "conteudo", "DNA maior que a célula", [("tam", "O DNA é muito maior que a célula", "dna-tamanho")]),
 (7, "conteudo", "DNA: estrutura", [("dupla", "Dupla hélice antiparalela de nucleotídeos", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (8, "conteudo", "Nucleotídeo", [("nuc", "Fosfato, pentose e base nitrogenada (A, T, G, C)", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (9, "conteudo", "Pareamento A–T", [("at", "A–T com 2 pontes de hidrogênio", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (10, "conteudo", "Pareamento C–G", [("cg", "C–G com 3 pontes; nucleotídeo invertido", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (11, "conteudo", "Ribose e desoxirribose", [("acucar", "Estrutura do açúcar: desoxirribose do DNA", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (12, "conteudo", "Ligação entre bases", [("lig", "Pontes de hidrogênio G–C (3) e A–T (2)", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (13, "conteudo", "Bases nitrogenadas", [("bases", "Purinas (A, G) e pirimidinas (C, T)", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (14, "conteudo", "Ligação fosfodiéster", [("fosfo", "Ligação fosfodiéster entre nucleotídeos", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (15, "conteudo", "Dupla hélice (figura)", [("fig", "Representação da dupla hélice com pontes e esqueleto", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (16, "conteudo", "Desnaturação e renaturação", [("den", "Pontes de hidrogênio se separam por calor ou substância química; reanelamento", EXC + "estrutura do DNA é conteúdo de Biologia Molecular (comentários de Davi, 11/10: 'fugiu do conteúdo da aula, isso é aula de biomol')")]),
 (17, "conteudo", "Fotografia de tubo com DNA", [("foto", "Tubo com DNA extraído", EXC + "fotografia sem alvo de aprendizado")]),
 (18, "conteudo", "Cromossomo e plasmídeo; divisão celular", [
   ("plas", "Plasmídeo é DNA circular extracromossômico, replicon, dividido entre as filhas", ["sh-1791163035024", "plasmideo-replicon", "plasmideo-perda", "sh-1791576667593"]),
   ("ident", "A bactéria é identificada pelo DNA cromossomal", "genoma-cromossomal"),
   ("sem", "Replicação semiconservativa e bidirecional", ["replicacao-semiconservativa", "replicacao-bidirecional"])]),
 (19, "conteudo", "Comparação de genomas", [("genoma", "Mycoplasma 0,58 Mb e 480 genes; E. coli 4,6 Mb; Streptomyces 8 Mb linear; levedura 12 Mb; homem 3 Gb", ["genoma-micoplasma", "genoma-streptomyces"])]),
 (20, "conteudo", "Replicação em θ", [("teta", "Estrutura θ, forquilhas, terminação Ter, velocidade 50.000 pb/min", ["replicacao-teta", "replicacao-bidirecional", "replicacao-velocidade", "origem-replicacao"])]),
 (21, "conteudo", "Origem de replicação oriC", [("oric", "OriC conservada; 9 e 13 pb ricas em A–T; GATC metilado", ["oric-sequencias", "oric-gatc", "origem-replicacao"])]),
 (22, "conteudo", "Forquilha de replicação", [("garfo", "Fita líder e descontínua, primer de RNA, fragmentos de Okazaki, helicase, SSB, ligase", ["helicase", "ssb", "primase", "pol3-alonga", "ligase", "okazaki"])]),
 (23, "conteudo", "DNA polimerases de procariotos", [("pols", "Pol I, II e III: funções", ["pol1-exonuclease", "pol2-reparo", "pol3-alonga", "pol3-revisao"])]),
 (24, "conteudo", "Mutação", [
   ("def", "Alteração química ou física do DNA; mutagênicos ou genotóxicos; espontâneas por erro de replicação", ["mutagenico", "mutacao-tautomero", "pol3-revisao"]),
   ("pos", "Mutações dão resistência a drogas, variação de temperatura e morfológicas", ["auxotrofico", "mutantes-aplicacao"])]),
 (25, "conteudo", "Tipos de mutação pontual", [("tipos", "Silenciosa, sentido errado, sem sentido, inserção/deleção (fase de leitura)", ["silenciosa", "sentido-errado", "sem-sentido", "fase-leitura"])]),
 (26, "conteudo", "Mutagênicos físicos", [("fis", "UV (dímeros de pirimidina), radiação ionizante (quebras), calor", ["sh-1791666344741", "uv-bloqueia", "uv-penetracao", "ionizante-quebras"])]),
 (27, "conteudo", "Mutagênicos químicos", [("quim", "Moléculas planares (EB, SDS), alquilantes (EMS), água oxigenada", ["planar-etidio", "alquilantes", "peroxido"])]),
 (28, "conteudo", "Modificação do DNA (esquema)", [("mod", "Esquema: fago, plasmídeo e fragmentos de DNA chegando à bactéria", ["transformacao-def", "plasmideo-exotoxina", "transducao-def", "tres-mecanismos"])]),
 (29, "conteudo", "Transformação", [("transf", "DNA livre captado por célula competente muda o genótipo", ["transformacao-def", "griffith", "avery", "transf-especies", "transf-fita"])]),
 (30, "conteudo", "Zona de adesão e cálcio", [("ca", "DNA e íons cálcio na zona de adesão da membrana", "transf-calcio")]),
 (31, "conteudo", "Transposons: Tn10", [("tn10", "IS10L e IS10R invertidas flanqueiam o gene de resistência à tetraciclina", ["transposase", "is-classe1", "tn10", "sh-1791630179144"])]),
 (32, "conteudo", "Transposons e plasmídeos", [("plas", "Elementos transponíveis na evolução de plasmídeos; Tn3, Tn4, Tn5, Tn9", ["transposon-plasmideo", "tn3", "tn5", "tn9", "transposon-estabilidade", "ilha-patogenicidade", "is-classe1"])]),
 (33, "conteudo", "Transdução", [("td", "Transdução generalizada e especializada; fago como veículo", ["transducao-def", "transducao-generalizada", "transducao-especializada", "fago-engano", "lisogenico", "conversao-lisogenica", "difteria-profago", "plasmideo-exotoxina"])]),
 (34, "conteudo", "Conjugação", [("conj", "Fator F, F⁺, F⁻, Hfr, transferência de uma fita", ["sh-1791576677366", "fator-f", "conj-fita", "conj-plasmideo", "hfr-def", "hfr-genoma", "hfr-mapa", "hfr-tempo", "lederberg-tatum", "destino-receptor", "epissomo"])]),
 (35, "conteudo", "Pilus de conjugação", [("pilus", "Mecanismo de transferência: pilus de conjugação; plasmídeos R, Col, promíscuos", ["sh-1791576677366", "conj-gram", "plasmideo-r", "plasmideo-col", "plasmideo-promiscuo", "plasmideo-ti", "plasmideo-exotoxina"])]),
 (36, "conteudo", "Recombinação gênica (esquema de clonagem)", [("rec", "Plasmídeo + gene de interesse → DNA recombinante → bactéria", ["ligase-recombinante", "clonagem-vetor", "clonagem-transformacao", "recombinacao-reca"])]),
 (37, "conteudo", "Tecnologia do DNA recombinante", [("rest", "Clivagem no eixo de simetria: extremidades abruptas; simétrica ao redor: coesivas", ["palindromo", "endonuclease", "extremidades"])]),
 (38, "conteudo", "Enzimas de restrição", [("tab", "Tabela de microrganismo, enzima e sequência-alvo", "ecori")]),
 (39, "conteudo", "Plasmídeo híbrido", [("hib", "Plasmídeo e DNA humano cortados com a mesma enzima, ligados pela ligase", ["recombinante", "ligase-recombinante", "clonagem-transformacao"])]),
 (40, "conteudo", "Vetor pUC18", [("puc", "pUC18 (2686 pb): resistência à ampicilina, lacZ e sítios de clonagem", ["puc18", "clonagem-vetor"])]),
 (41, "conteudo", "Operon lac", [("lac", "Estrutura e funcionamento do operon lac", ["sh-1791664581182", "sh-1791664580657", "sh-1791664580774", "sh-1791664581049", "sh-1791664582020", "sh-1791664581433", "sh-1791664579655"])]),
 (42, "conteudo", "Estruturas secundárias de RNA", [("rna", "Figura de estruturas secundárias de RNA", EXC + "figura sem texto; o tema é de RNAs não codificadores e Operon")]),
 (43, "conteudo", "Sistema CRISPR-Cas9", [("def", "Defesas da bactéria contra fago; CRISPR como uma delas", ["sh-1791630174170", "sh-1791630174671", "restricao-modificacao"])]),
 (44, "conteudo", "Etapas do CRISPR", [("etapas", "Aquisição de espaçador, biogênese de crRNA, interferência", ["crispr-etapas", "cas1-cas2", "sh-1791630174296", "sh-1791630174420"])]),
]
JUSTIFICATIVAS = {"capa": "capa, sem conteúdo"}

CAPITULO = [("Trabulsi, cap. 5 — Genética bacteriana", [
   ("tr-replic", "DNA bacteriano circular, superenrolado, bidirecional; Pol III replica, Pol I e II reparam; OriC, primase e ligase", ["supertorcido", "replicacao-bidirecional", "pol3-alonga", "pol1-exonuclease", "pol2-reparo", "primase", "ligase", "origem-replicacao"]),
   ("tr-mut", "Mutação espontânea e induzida; transição e transversão; sem sentido, sentido errado e fase de leitura; auxotróficos", ["mutacao-tautomero", "transicao", "transversao", "sem-sentido", "sentido-errado", "fase-leitura", "auxotrofico"]),
   ("tr-reparo", "Resposta SOS (RecA/LexA), reparo por excisão no escuro e fotorreativação", ["sos", "fotoliase", "ner"]),
   ("tr-recomb", "Recombinação geral depende de RecA; sítio-específica não", "recombinacao-reca"),
   ("tr-transf", "Transformação: competência, fita única, complexo eclipse", ["transformacao-def", "transf-fita"]),
   ("tr-transd", "Transdução generalizada e especializada", ["transducao-generalizada", "transducao-especializada"]),
   ("tr-conj", "Conjugação, F e Hfr, 100 min; plasmídeos conjugativos e mobilizáveis; R e RTF; Col; Ti", ["fator-f", "hfr-def", "hfr-tempo", "plasmideo-r", "plasmideo-col", "plasmideo-ti"]),
   ("tr-tn", "Transposons classe I e II, IS, Tn3; independem de RecA; integrons", ["is-classe1", "tn3", "transposicao-reca", "transposase"]),
   ("tr-dnar", "DNA recombinante e enzimas de restrição", ["extremidades", "ligase-recombinante", "palindromo"])])]

EXERCICIOS = [
 ("Provas UC03 (índice micro-06)", [
   ("p2025", "2025 P2 1.4 e 4.2: β-lactamase em plasmídeo, mutações em gyrA/parC, genes de resistência por bioinformática", ["sh-1791668521839", "plasmideo-r", "transposon-plasmideo"]),
   ("p2018", "2018 P2 2.3 e 2017: resistência por mutação do alvo, β-lactamase, efluxo e plasmídeo de resistência", ["plasmideo-r", "transposon-plasmideo", "tn3"]),
   ("p2017", "2017 P1 3.3: o plasmídeo explica a resistência", ["plasmideo-replicon", "plasmideo-r"])]),
 ("Guia de veteranos e monitoria P2, aula 5", [
   ("vet-gen", "DNA circular no citoplasma; plasmídeo com funções extras; replicação bidirecional semiconservativa", ["sh-1791576675592", "genoma-cromossomal", "replicacao-bidirecional", "replicacao-semiconservativa"]),
   ("vet-mut", "Mutação ao acaso; agentes físicos e químicos; transição/transversão; fotoliase e reparo recombinacional; Ames e cromoteste", ["variacao-genetica", "fotoliase", "reparo-recombinacional", "ames", "cromoteste"]),
   ("vet-rec", "Transformação (Griffith, Avery), conjugação, transdução e elementos transponíveis", ["griffith", "avery", "plasmideo-promiscuo", "transducao-def", "transposase"]),
   ("vet-tn", "Tn3 ampicilina, Tn5 canamicina; transposase em looping; interferência em genes", ["tn3", "tn5", "transposase"])]),
 ("Transcrição da aula", [
   ("tr-ident", "A identificação da bactéria depende do DNA cromossomal; plasmídeo traz funções extras", "genoma-cromossomal"),
   ("tr-var", "Variação só por mutação ou recombinação", "variacao-genetica"),
   ("tr-mut", "Eventos possíveis após a lesão; tolerância às lesões; mutantes para aplicação", ["lesao-destino", "mutantes-aplicacao", "mutagenico-cancer"]),
   ("tr-reparo", "Reparo por excisão-ressíntese no escuro, fotorreativação e reparo recombinacional; o ser humano também tem esses sistemas", ["ner", "excisao-endonuclease", "xeroderma", "fotoliase", "reparo-recombinacional"]),
   ("tr-grif", "Griffith (1928), Avery, MacLeod e McCarty (1944)", ["griffith", "avery"]),
   ("tr-lt", "Lederberg e Tatum (1946); fator F; Hfr; mapeamento; plasmídeos promíscuos", ["lederberg-tatum", "hfr-mapa", "plasmideo-promiscuo"]),
   ("tr-tn", "Transposons: McClintock; Tn10, Tn9; estabilidade; ilhas de patogenicidade", ["mcclintock", "tn10", "tn9", "transposon-estabilidade", "ilha-patogenicidade"]),
   ("tr-td", "Transdução e conversão lisogênica (difteria)", ["fago-engano", "conversao-lisogenica", "difteria-profago"])]),
]
