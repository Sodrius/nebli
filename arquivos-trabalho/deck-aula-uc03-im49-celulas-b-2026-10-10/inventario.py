"""Inventário atômico de Ativação de células B e plasticidade da resposta humoral (UC03 P3, Imunologia; aula 09 da turma, 62 lâminas;
pasta pessoal 49 - Ativação de células B vazia, base = PDF da turma). Escrito em 10/10/2026 antes da seleção, a partir de: lâminas
(visual/folha-01..11, fontes/slides.txt), transcrição oficial (fontes/transcricao.txt, fala da professora), monitoria P2 aula 10
(fontes/monitoria-p2-imuno.txt pp. 25–28; erros notados: "CD25" no B-1, "decamérica", "mutação na adenosina" — não usados),
provas do índice imuno-09 (fontes/provas.txt, 17 subquestões 2015–2025).
"""
PREFIXO = "im49"
AULA = "Ativação de células B e plasticidade da resposta humoral (UC03 P3; Imunologia, aula 09)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "capa", "Divisória: ontogenia do LB", []),
 (3, "conteudo", "Estágios do LB e Ig expressa", [
   ("estagios", "Célula-tronco → pró-B → pré-B (μ citoplasmática) → B imatura (IgM) → B madura (IgM+IgD) → plasmócito",
    ["pro-b", "pre-b", "imatura", "naive-igm-igd", "plasmocito-ig", "memoria-b"])]),
 (4, "conteudo", "Seleção na medula", [
   ("selecao", "Reconhecimento forte do próprio → apoptose; fraco → sobrevive", "selecao-medula"),
   ("edicao", "B, diferente do T, pode reeditar o receptor (transcrição)", "edicao")]),
 (5, "conteudo", "Fases independente e dependente de antígeno", [
   ("saida", "B madura sai da medula e termina a maturação no órgão linfoide secundário", "naive-secundario"),
   ("fase-dep", "Ativação: plasmócito, troca de classe, maturação de afinidade, memória", ["plasmocito-ig", "memoria-b"])]),
 (6, "conteudo", "Estrutura do BCR", [
   ("cadeias", "Duas cadeias pesadas e duas leves", "cadeias"),
   ("fab-fc", "Fab liga antígeno (idiótipo); Fc define isótipo e liga receptor/complemento", ["idiotipo", "isotipo-fc"]),
   ("pesada-leve", "Pesada no Fab e Fc; leve só no Fab", ["pesada", "leve"])]),
 (7, "conteudo", "TCR × Ig", [
   ("tcr-ig", "TCR monovalente, nunca secretado; Ig bivalente", ["tcr-monovalente", "tcr-secretado"]),
   ("independente", "Cada cadeia recombina individualmente", "combinacao")]),
 (8, "conteudo", "Quem faz recombinação", [
   ("quando", "Linfócitos imaturos, timo/medula, antes do antígeno", "antes-antigeno"),
   ("rag", "Recombinases RAG1 e RAG2", "rag")]),
 (9, "conteudo", "Rearranjo da cadeia pesada", [("vdj-h", "D-J e depois V-DJ; splicing para μ ou δ", ["vdj-pesada", "dj-primeiro"])]),
 (10, "conteudo", "Rearranjo da cadeia κ", [("vj-l", "V-J na cadeia leve", "vj-leve")]),
 (11, "conteudo", "Vários segmentos para H e L", [("segmentos", "Segmentos V, D, J (H) e V, J (L)", ["vdj-pesada", "vj-leve"])]),
 (12, "conteudo", "Número de segmentos V/D/J humanos", [("numeros", "κ 40/0/5, λ 30/0/4, H 65/27/6", EXC + "tabela numérica; a ideia útil (D só na pesada) está em vdj-pesada/vj-leve")]),
 (13, "conteudo", "B-1 × B-2", [
   ("b1-origem", "B-1: fetal, autorrenova nas cavidades", "b1-cavidades"),
   ("b1-cd5", "B-1 CD5+", "b1-cd5"),
   ("b1-igm", "B-1: IgM natural polirreativa, polissacarídeos (ABO)", "b1-igm"),
   ("b2", "B-2: da medula, alta diversidade, proteínas, troca de classe", "b2")]),
 (14, "conteudo", "B em repouso × plasmócito", [
   ("repouso-plasmo", "Plasmócito perde Ig de superfície e MHC II; secreta muita Ig", "plasmocito-mhc")]),
 (15, "capa", "Divisória: as imunoglobulinas", []),
 (16, "conteudo", "Síntese de Ig", [("rer", "RER → Golgi → vesículas", "rer")]),
 (17, "conteudo", "Ig: glicoproteína tetramérica", [
   ("dobradica", "Dobradiça dá flexibilidade", "dobradica"),
   ("kappa-lambda", "Cadeia leve κ ou λ, nunca mista; mais κ", ["kappa-lambda", "kappa-ratio"])]),
 (18, "conteudo", "BCR na membrana", [("igab", "sIg + Igα/Igβ; CD19, CD21, CD81", ["igab", "cd19"])]),
 (19, "conteudo", "Correceptores", [
   ("cr2", "CR2/CD21 liga C3d", "cr2-c3d"),
   ("cd22", "CD22 inibitório (ITIM, SHP-1)", "cd22")]),
 (20, "conteudo", "Isótipos", [
   ("igm-pent", "IgM pentâmero com cadeia J", "igm-pentamero"),
   ("iga-dim", "IgA dímero com cadeia J", "iga-dimero"),
   ("igm-mono", "IgM monômero na membrana", "igm-membrana")]),
 (21, "conteudo", "Receptores Fc", [("fcr", "FcγRI, II, III, FcεRI; ativadores e inibitórios", "fcr-nome")]),
 (22, "capa", "Divisória: ativação de LB", []),
 (23, "conteudo", "TI-1 × TD", [("ti-td", "TI: BCR sozinho; TD: Th + CD40/CD40L", ["ti-crosslink", "td-memoria"])]),
 (24, "capa", "Divisória: T independente", []),
 (25, "conteudo", "Antígenos TI-2", [
   ("ti-igm", "TI-2 sozinho → IgM", ["ti-igm", "ti-crosslink", "sh-1791625426282"]),
   ("ti-baff", "Citocinas (BAFF) aumentam a produção e induzem troca de isótipo", "ti-baff"),
   ("lps", "LPS como exemplo (transcrição)", "lps"),
   ("ti-memoria", "TI sem memória", "ti-memoria")]),
 (26, "capa", "Divisória: T dependente", []),
 (27, "conteudo", "Vírus: B internaliza e apresenta ao T", [("b-apc", "B apresenta peptídeo em MHC II; T ajuda", "b-apc-mhc2")]),
 (28, "conteudo", "Polissacarídeo ligado ao toxoide tetânico", [
   ("conjugada", "Epítopo polissacarídico + proteína → Th → anticorpo contra o polissacarídeo", ["conjugada", "hib", "pcv-igg"])]),
 (29, "conteudo", "CD40 constitutivo × CD40L induzível", [
   ("cd40", "CD40 no B; CD40L induzível no T", ["sh-1791625431258", "cd40l-induzivel"]),
   ("requisitos", "Th + CD40/CD40L + citocinas → plasmócito longo, troca, afinidade, memória", ["sh-1791625431383", "hiper-igm"])]),
 (30, "conteudo", "Sinapse B–T", [("sinapse", "Contato prolongado B–T", "b-apc-mhc2")]),
 (31, "conteudo", "Linfonodo", [
   ("foliculos", "Folículos B no córtex; T no paracórtex; plasmócitos na medula", ["sh-1791625425757", "centro-humoral"]),
   ("centro", "Centro germinativo: proliferação e diferenciação B", ["centro-humoral", "sh-1791625425757"])]),
 (32, "conteudo", "Encontro T:B e centro germinativo", [
   ("borda", "T e B ativados se encontram na borda folículo-paracórtex", "borda"),
   ("cg", "Centro germinativo: maturação de afinidade, memória", ["switch-local", "fdc"])]),
 (33, "capa", "Divisória: mudanças induzidas pela ativação", []),
 (34, "conteudo", "Membrana → secretada", [("secretada", "Mesmo reconhecimento; passa de receptor a secretada", "secretada")]),
 (35, "conteudo", "Amadurecimento por afinidade", [("afinidade", "Mutações somáticas na região variável aumentam afinidade", "afinidade")]),
 (36, "conteudo", "Recombinação de troca", [("troca", "Troca da região constante; mesma especificidade", "troca-constante")]),
 (37, "conteudo", "Ordem M–D–G–E–A e citocinas", [
   ("ordem", "Genes constantes μ, δ, γ, ε, α; LPS → IgM; +IL-4 → γ1/ε; +TGF-β → γ2b/α", ["troca-constante", "tgfb-iga"])]),
 (38, "conteudo", "Citocinas e isótipos", [
   ("ifn", "IFN-γ → IgG", "sh-1791625434208"), ("il4", "IL-4 → IgE", "sh-1791625434333"), ("tgf", "TGF-β → IgA", "tgfb-iga"),
   ("prolif", "IL-2/4/5 de proliferação", EXC + "lista de citocinas de proliferação, sem uso na aula")]),
 (39, "conteudo", "Funções por isótipo", [
   ("tabela", "Neutralização, opsonização (IgG), NK (IgG), mastócitos (IgE), complemento (IgM, IgG3)",
    ["opsonizacao-igg", "adcc-igg", "ige-mastocito", "fixa-complemento"])]),
 (40, "conteudo", "Hipermutação somática", [
   ("cg-shm", "Nos centros germinativos, aleatória", "afinidade"),
   ("cdr", "Seleção concentra mutações nos CDR", "cdr"),
   ("aid", "AID", "aid")]),
 (41, "capa", "Divisória: funções efetoras", []),
 (42, "conteudo", "Neutralização, opsonização, complemento", [("resumo", "Visão geral das três funções", ["neutralizacao", "opsonizacao-igg", "fixa-complemento"])]),
 (43, "conteudo", "Neutralização", [("neut", "Bloqueia ligação de micróbio e toxina ao receptor", "neutralizacao")]),
 (44, "conteudo", "Opsonização", [("ops", "FcγRI do fagócito liga micróbio opsonizado", ["opsonizacao-igg", "capsula-igg"])]),
 (45, "conteudo", "Etapas da opsonização", [("ops2", "Opsonização → FcγRI → sinais → fagocitose → morte", "capsula-igg")]),
 (46, "conteudo", "Via clássica: IgG × IgM", [("vc", "CH2 liga complemento; IgM pentamérica", "igm-complemento")]),
 (47, "conteudo", "Complemento por IgM e IgG", [
   ("igm-ligada", "IgM solúvel não ativa; ligada ao antígeno ativa", "igm-complemento"),
   ("igg-adj", "IgG precisa de moléculas adjacentes", "igg-duas")]),
 (48, "conteudo", "Complemento: inflamação", [("c3a", "C3a/C5a recrutam leucócitos", EXC + "conteúdo da aula 31 (Sistema complemento), já no deck dela")]),
 (49, "conteudo", "Complemento: MAC", [("mac", "C3b → MAC → lise osmótica", EXC + "conteúdo da aula 31 (Sistema complemento), já no deck dela")]),
 (50, "conteudo", "ADCC", [
   ("nk", "IgG + FcγRIII de NK", ["adcc-igg", "nk-cd16"]),
   ("eos", "IgE + FcεRI de eosinófilo mata helminto", "ige-helminto")]),
 (51, "conteudo", "Mastócito e IgE", [("masto", "Ligação cruzada de IgE → degranulação", ["ige-mastocito", "ige-crosslink"])]),
 (52, "conteudo", "Resumo das funções", [("resumo2", "Neutralização, opsonização, ADCC, lise, inflamação", ["neutralizacao", "adcc-igg", "fixa-complemento"])]),
 (53, "capa", "Divisória: imunidade sistêmica e localizada", []),
 (54, "conteudo", "Transporte da IgA", [
   ("plasmo-lp", "Plasmócito da lâmina própria produz IgA dimérica", "sh-1790980915277"),
   ("pigr", "Receptor poli-Ig; transcitose; clivagem → componente secretor", ["pigr", "transcitose", "componente-secretor"])]),
 (55, "conteudo", "IgA no lúmen", [("iga-lumen", "IgA no muco neutraliza patógenos e toxinas", ["iga-secrecoes", "iga-mais-produzida"])]),
 (56, "conteudo", "Imunidade passiva", [
   ("placenta", "IgG atravessa a placenta", ["igg-placenta", "passiva-placenta"]),
   ("colostro", "IgG e IgA no colostro", ["iga-leite", "passiva-placenta"])]),
 (57, "conteudo", "IgA no colostro", [("colostro-conc", "IgA alta no colostro (dia 2) × saliva", "colostro")]),
 (58, "conteudo", "Cinética: primária × secundária", [("cinetica", "Secundária mais rápida e mais intensa", "secundaria-rapida")]),
 (59, "conteudo", "IgM e IgG nas respostas", [
   ("igm-primeiro", "IgM primeiro; IgG domina a secundária", ["igm-primeira", "igg-secundaria"]),
   ("sorologia", "IgM × IgG distinguem infecção primária (transcrição; provas 2023, 2015)", ["sorologia-igm", "igm-neonato"])]),
 (60, "conteudo", "Tabela primária × secundária", [("tabela-ps", "Lag, pico, isótipo, afinidade", ["secundaria-rapida", "igg-secundaria"])]),
 (61, "conteudo", "Vacinas e mecanismo", [
   ("polio", "Pólio oral → IgA de mucosa", "polio-oral"),
   ("toxoide", "Tétano/difteria: toxoide → IgG neutralizante", "toxoide"),
   ("hbv", "Hepatite B: proteína recombinante → IgG", "hbv-subunidade"),
   ("pneumo", "Pneumococo/Hib conjugadas → opsonização", ["conjugada", "hib"])]),
 (62, "conteudo", "Células dendríticas foliculares", [("fdc", "FDC retêm antígeno com FcR e CR3; sobrevida da memória B", "fdc")]),
]
JUSTIFICATIVAS = {"capa": "capa ou divisória, sem conteúdo"}

CAPITULO = [("Abbas, Imunologia Básica: respostas humorais, mecanismos efetores e maturação B", [
   ("ab-edicao", "Edição do receptor resgata B imatura autorreativa", "edicao"),
   ("ab-ti", "B-1 e zona marginal respondem a antígenos TI", ["ti-crosslink", "b1-cavidades"]),
   ("ab-baff", "BAFF pode participar da troca para IgA", "ti-baff"),
   ("ab-fdc", "FDC exibem antígeno no centro germinativo; seleção por afinidade", ["fdc", "cdr"]),
   ("ab-pigr", "Receptor poli-Ig transporta IgA pelo epitélio", ["pigr", "transcitose"])])]

EXERCICIOS = [
 ("Provas UC03 (índice imuno-09)", [
   ("p2017-switch", "2017 P1 4.4: troca IgM → IgG com mesma especificidade; mecanismo e vantagem", ["troca-constante", "sh-1791625431383"]),
   ("p2017-ko", "2017 P3 5.2: LPS × proteína em AID KO, CD40 KO", ["aid", "hiper-igm", "ti-igm"]),
   ("p2018-vacina", "2018 P2 2.7: polissacarídica × conjugada", ["conjugada", "ti-memoria"]),
   ("p2015-iga", "2015 P2 5.2–5.3: IgA, TGF-β, receptor poli-Ig", ["tgfb-iga", "pigr", "componente-secretor"]),
   ("p2023-sorologia", "2023 P2 2.2: IgM+ IgG−", "sorologia-igm"),
   ("p2017-placenta", "2017 P3 1.5: IgG materna pela placenta", "igg-placenta")]),
 ("Monitoria P2, aula 10", [
   ("mon-b1", "B-1 cavidades, polissacarídeos; B-2 folicular IgM+IgD", ["b1-cavidades", "naive-igm-igd"]),
   ("mon-ti", "TI: sem memória, só IgM; CR2/C3d", ["ti-memoria", "ti-igm", "cr2-c3d"]),
   ("mon-fdc", "Centro germinativo, FDC, AID", ["fdc", "aid"])]),
]
