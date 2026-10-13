"""Inventário atômico de Regulação da expressão gênica em eucariotos I (UC03 P3, Biologia Molecular; Prof. Alexandre Bruni Cardoso,
aula de 2026, 39 lâminas, Drive pessoal 46 - Expressão gênica em eucariotos I). Escrito em 10/10/2026 antes da seleção, a partir de:
lâminas 2026 (visual/folha-01..07, fontes/slides.txt; objetivos na lâmina 6); PDF Ib da turma (mesma aula, +3 lâminas) e Ia/"transcrição"
(aula antiga baseada no Watson cap. 19, usada só para aprofundar itens da aula de 2026); monitoria P3 aula 4 (fontes/monitoria-p3.txt
pp. 19–23); provas do índice biomol-07 (fontes/provas.txt); Alberts 5ª ed. cap. 7 (livros/alberts5-cap7-controle-expressao.txt).
"""
PREFIXO = "bm46"
AULA = "Regulação da expressão gênica em eucariotos I (UC03 P3; Prof. Alexandre Bruni Cardoso, 2026)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Fígado × neurônio: genes diferentes ligados", [("celulas", "Mesmos genes, expressão diferente por tipo celular", "mesmo-genoma")]),
 (3, "conteudo", "O genoma permanece o mesmo", [("genoma", "Muda o conjunto de genes expressos", "mesmo-genoma")]),
 (4, "conteudo", "Níveis de regulação", [
   ("niveis", "Transcricional, pós-transcricional, traducional, pós-traducional", "niveis"),
   ("iniciacao", "A iniciação da transcrição é o ponto mais importante", "iniciacao")]),
 (5, "conteudo", "30–60% dos genes expressos", [("fracao", "Uma célula expressa 30–60% dos genes, em níveis variáveis", EXC + "número de artigo (atlas de proteínas), sem uso posterior na aula")]),
 (6, "conteudo", "Objetivos", [("objetivos", "Bactérias × eucariotos; enhancer; Gal4 (universalidade, modularidade); sinais",
   ["indireto", "enhancer-def", "universalidade", "modularidade", "sinal-direto"])]),
 (7, "conteudo", "Por que regular", [("porque", "Economia de energia, resposta ao ambiente, diferenciação", "porque-regular")]),
 (8, "conteudo", "Genes constitutivos × regulados", [
   ("housekeeping", "Housekeeping: actina, tubulina, laminas, GAPDH", "housekeeping"),
   ("regulados", "Regulados: álcool desidrogenase (fígado), caseína (mama)", "regulados")]),
 (9, "conteudo", "Procariotos × eucariotos", [
   ("cis-trans", "Sequências em cis reconhecidas por fatores em trans", "cis-trans"),
   ("indireto", "Ativadores/repressores interagem indiretamente com a Pol II", "indireto"),
   ("dezenas", "Dezenas de fatores controlam um único gene", "combinatorio"),
   ("alcas", "Alças de DNA aproximam sequências distantes", "dna-dobra"),
   ("cromatina", "Cromatina inibe o acesso e é ponto de regulação", ["heterocromatina", "acetilacao"])]),
 (10, "conteudo", "Maquinaria mais complexa", [
   ("pol2-gtf-mediador", "Pol II + GTFs + Mediador (>60 proteínas) × cerne + sigma", "maquinaria"),
   ("sigma", "Em bactérias o sigma reconhece o promotor", "maquinaria")]),
 (11, "conteudo", "Regiões regulatórias extensas", [
   ("promotor", "Promotor onde se ligam Pol II e GTFs", "promotor"),
   ("proximal", "Elementos regulatórios proximais", EXC + "só rótulo da figura; o contraste promotor × enhancer distante está nos cards"),
   ("enhancers-longe", "Enhancers a milhares/centenas de milhares de pb, montante ou jusante", "enhancer-distancia")]),
 (12, "conteudo", "Fatores gerais × específicos", [
   ("gerais", "Gerais: todos os genes da Pol II; recrutam a Pol II", ["gtf-promotor", "promotor"]),
   ("especificos", "Específicos: expressão regulada (ativadores e repressores)", "especificos-enhancer")]),
 (13, "conteudo", "Promotor da Pol II", [
   ("tata", "TATA box, elemento mais fundamental (≠ −10 bacteriano)", ["tata", "tbp"]),
   ("bre-inr-dpe", "BRE (TFIIB), INR e DPE (TFIID)", "bre")]),
 (14, "conteudo", "Estrutura de um enhancer", [
   ("enhancer", "Enhancer curto (100–500 pb) com vários sítios; efeito = saldo de ativadores e repressores", ["enhancer-def", "silencer"])]),
 (15, "conteudo", "Hubs de enhancers", [("hubs", "Um enhancer → vários genes; um gene ← vários enhancers", EXC + "figura de artigo sem explicação na aula; a ideia de vários enhancers por gene está em combinatorio")]),
 (16, "conteudo", "Sinergia", [("sinergia", "Ativadores agem em sinergia: integração de sinais", "sinergia")]),
 (17, "conteudo", "Alça e ação a distância", [
   ("loop", "Formação de alça permite ação do enhancer a distância", "dna-dobra"),
   ("indireto2", "Ativadores não tocam diretamente a Pol II", "indireto"),
   ("cromatina-ativ", "Ativadores recrutam modificadores de cromatina", ["gal4-ativacao", "acetilacao"])]),
 (18, "capa", "Divisória: sistema Gal", []),
 (19, "conteudo", "O sistema Gal", [("gal", "Genes da galactose em leveduras, análogo ao operon lac; Gal4 governa GAL1", "gal4")]),
 (20, "conteudo", "UAS com 1–4 sítios para Gal4", [("uas", "UAS (upstream activating sequence)", "uas")]),
 (21, "conteudo", "Domínios separados", [("dominios", "Ligação ao DNA e ativação em domínios distintos (≠ CAP)", "dois-dominios")]),
 (22, "conteudo", "Domínio de ativação de Gal4", [("ativacao", "Liga TFIID, Mediador e recruta modificadores de cromatina", "gal4-ativacao")]),
 (23, "conteudo", "Universalidade: pergunta", [("univ-q", "Gal4 ativa em outras células eucarióticas?", "universalidade")]),
 (24, "conteudo", "Universalidade: TATA + UAS", [("univ", "Gal4 ativa em qualquer célula com promotor TATA e UAS", "universalidade")]),
 (25, "conteudo", "UAS:GFP em organismos", [("gfp", "Gal4–UAS dirige transgenes tecido-específicos", "gal4-uas-ferramenta")]),
 (26, "conteudo", "Interface conservada", [("conservada", "Interface ativador–maquinaria conservada em leveduras, plantas e humanos", "universalidade")]),
 (27, "conteudo", "Modularidade", [("modulo", "Domínio de ligação só ancora; não ativa", "modularidade")]),
 (28, "conteudo", "Experimentos de modularidade", [("lexa", "Sem domínio de ativação: OFF; LexA + ativação de Gal4: ON", "modularidade")]),
 (29, "capa", "Divisória: sinais", []),
 (30, "conteudo", "Bactérias: sinal liga direto no fator", [("direto", "Sinal liga o ativador/repressor e muda ligação ao DNA", "sinal-direto")]),
 (31, "conteudo", "Formas de regular fatores eucarióticos", [("formas", "Síntese, ligante, modificação covalente, subunidade, desmascaramento, entrada no núcleo, liberação da membrana", "formas-ativar")]),
 (32, "conteudo", "Hormônios lipossolúveis", [("lipossoluveis", "Esteroides e tireoidianos atravessam a membrana e ligam receptores nucleares", ["receptor-nuclear", "t3"])]),
 (33, "conteudo", "Receptores nucleares", [
   ("nr-tf", "São ativadores que dependem do hormônio para ligar o DNA", "receptor-nuclear"),
   ("superfamilia", "Superfamília (ER, PR, GR, TR, RAR) com domínio de ligação ao DNA", "zinco")]),
 (34, "conteudo", "Hormônio esteroide e NR", [("hre", "Complexo NR–Hsp, dímero, HRE, coativador", ["gr-citoplasma", "gr-nucleo"])]),
 (35, "conteudo", "GR–GFP e cortisol", [("gr-localizacao", "Cortisol leva o GR do citoplasma ao núcleo", ["gr-citoplasma", "gr-nucleo"])]),
 (36, "conteudo", "Fosforilação de ativadores", [
   ("fosforilacao", "Fosforilação controla ligação ao DNA e localização", "fosforilacao"),
   ("jak-stat", "Citocina → JAK → STAT → núcleo", "jak-stat")]),
 (37, "conteudo", "FOXO1 e glicemia", [("foxo", "AKT fosforila FOXO1 e o retira do núcleo", "foxo1")]),
 (38, "conteudo", "GFP–FOXO1 com insulina", [("foxo-gfp", "Insulina tira FOXO1 do núcleo", "foxo1")]),
 (39, "capa", "Bibliografia", []),
]
JUSTIFICATIVAS = {"capa": "capa, divisória ou bibliografia, sem conteúdo"}

CAPITULO = [("Alberts 5ª ed., cap. 7 (controle da expressão gênica)", [
   ("ab-modular", "Ativadores têm desenho modular (ligação ao DNA + ativação), mostrado por proteínas híbridas", ["dois-dominios", "modularidade"]),
   ("ab-mediador", "Mediador é intermediário entre reguladores e Pol II", ["maquinaria", "indireto"]),
   ("ab-integracao", "Múltiplos reguladores integram informação no promotor", ["sinergia", "combinatorio"]),
   ("ab-cromatina", "Ativadores recrutam histona acetiltransferases", "acetilacao")])]

EXERCICIOS = [
 ("Provas UC03 (índice biomol-07)", [
   ("p2025", "2025 P3 1.5: mecanismos transcricionais (fatores de transcrição) e epigenéticos (cromatina) na troca de fase", ["formas-ativar", "acetilacao", "heterocromatina"]),
   ("p2024", "2024 P3 2.10: cromatina esperada para expressar um gene repórter", ["acetilacao", "heterocromatina"]),
   ("p2019", "2019 P3 5.2: quinase que fosforila um fator de transcrição e o inibe (ligação ao DNA, saída do núcleo)", ["fosforilacao", "pho4"])]),
 ("Monitoria P3, aula 4", [
   ("mon-enhancer", "Enhancer atua a distância, independe da orientação; alças", ["enhancer-distancia", "dna-dobra"]),
   ("mon-tfiid", "TFIID (TBP + TAFs) reconhece o TATA; TFIIB reconhece o BRE", ["tbp", "bre"]),
   ("mon-mediador", "Mediador é coativador; contato regulador–Pol II é indireto", ["maquinaria", "indireto"]),
   ("mon-gal4", "Gal4 regula cada gene individualmente; universalidade e modularidade (proteína híbrida)", ["gal4", "universalidade", "modularidade"]),
   ("mon-pho", "PHO: Pho4 fosforilado (fosfato alto) inativo e fora do núcleo", "pho4"),
   ("mon-nr", "Hormônios esteroides regulam ativadores diretamente (receptores nucleares)", "receptor-nuclear")]),
]
