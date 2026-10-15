"""Inventário atômico de Ativação de linfócitos T e plasticidade da resposta celular (UC03 P3, Imunologia, aula 8 do drive;
Prof. Niels Olsen Saraiva Câmara, ICB; 71 lâminas). Escrito em 10/10/2026 a partir do material de base lido inteiro antes da seleção:
lâminas (visual/folha-01..12, fontes/slides.txt; texto idêntico ao PDF da pasta da turma), transcrição da aula (fontes/transcricao.txt,
141 pp.), monitoria P2 aula 9 (fontes/monitoria-p2-imuno.txt pp. 20–24), apostila de veteranos aula 6 caps. 2–5
(fontes/veterano-imuno.txt pp. 42–46), provas antigas pelo índice UC03 (imuno-08) e Abbas 8ª ed. caps. 9–11 e Treg do cap. 15
(livros/). Cada ideia aponta para o card que a pergunta; menção no verso não conta.
"""
PREFIXO = "im45"
AULA = "Ativação de linfócitos T e plasticidade da resposta celular (UC03 P3; Prof. Niels O. S. Câmara)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Formas clínicas de TB. Why?", [
   ("tb-formas", "Mesma infecção: forma granulomatosa localizada × miliar/disseminada", "subset-forma"),
   ("th1-granuloma", "Th1 forma granuloma; doença disseminada com padrão Th2 (fim da transcrição)", ["granuloma-ifng", "subset-forma"])]),
 (3, "conteudo", "Formas clínicas de Leishmaniose. Why?", [
   ("leish-formas", "Leishmaniose cutânea × visceral frente ao mesmo patógeno", "subset-forma")]),
 (4, "conteudo", "Necessidade de Th específico", [
   ("fungo-neutrofilo", "Contra fungo, o neutrófilo precisa do Th17", "th17-neutrofilo"),
   ("il17", "Th17 produz IL-17, que ativa neutrófilos", "th17-il17")]),
 (5, "conteudo", "Inata e adaptativa", [
   ("apc-ponte", "A APC leva a informação de vírus, bactéria, fungo e parasita às células T", "dc-ponte")]),
 (6, "conteudo", "Modulação da resposta imune adaptativa", [
   ("tlr-citocinas", "TLR na célula dendrítica → citocinas inflamatórias (IL-12) → subtipo", ["il12-th1", "citocinas-decidem"]),
   ("th1-ifng", "Th1 produz IFN-γ", "th1-ifng"),
   ("th2-il4", "Th2 produz IL-4", "il4-th2")]),
 (7, "conteudo", "LT CD4 regentes da orquestra", [
   ("cd4-regente", "CD4 ajuda neutrófilos, macrófagos, DC, NK, linfócito B e CD8 por citocinas", "th1-macrofago-ctl")]),
 (8, "conteudo", "Precursores linfoides migram para o timo", [
   ("timo", "LT terminam a maturação no timo (LB na medula óssea)", "timo")]),
 (9, "conteudo", "Timócitos CD4+CD8+", [
   ("dn", "Chegam ao timo CD4−CD8−TCR−", "rag-tcr"),
   ("rag", "Recombinação do TCR por RAG1/RAG2", "rag-tcr"),
   ("dp-cortex", "Córtex: duplo-positivos CD4+CD8+ TCRlow", "cortex-dp"),
   ("sp-medula", "Medula: simples-positivos CD4 ou CD8 → periferia (helper, citotóxico)", "medula-sp")]),
 (10, "conteudo", "Maturação dos linfócitos T", [
   ("positiva", "Reconhecimento fraco de MHC próprio: seleção positiva", ["selecao-positiva", "positiva-cortex"]),
   ("linhagem", "MHC II → CD4; MHC I → CD8", ["mhc2-cd4", "mhc1-cd8"]),
   ("negligencia", "Sem reconhecimento: apoptose ('death by neglect')", "neglect"),
   ("negativa", "Reconhecimento forte: seleção negativa, apoptose", ["selecao-negativa", "negativa-medula"])]),
 (11, "conteudo", "Principais tipos de células T", [
   ("cd4-cd8-estrutura", "CD4 cadeia única; CD8 dímero α/β", "cd8-dimero"),
   ("auxiliar-citotoxico", "CD4 auxiliares × CD8 citotóxicos", ["mhc2-cd4", "mhc1-cd8"])]),
 (12, "conteudo", "Interação MHC-peptídeo-TCR", [
   ("tcr-ab", "TCR αβ reconhece peptídeo e MHC (reconhecimento duplo)", "tcr-alfabeta"),
   ("mhc1-b2m", "MHC I: α1, α2, α3 e β2-microglobulina", "b2m")]),
 (13, "conteudo", "Timócitos (imunofluorescência)", [
   ("dp-amarelo", "Duplo-positivos (amarelo) predominam no timo", "cortex-dp"),
   ("dez-pct", "Cerca de 5–10% saem do timo para a periferia", "timo-5pct")]),
 (14, "conteudo", "Recirculação e migração da CD", [
   ("naive-recircula", "Naive recircula por órgãos linfoides secundários; ativado vai ao tecido", "recirculacao"),
   ("cd-migra", "CD captura o antígeno no tecido e migra pelo linfático aferente ao linfonodo", "dc-maturacao"),
   ("cd-matura", "Na migração a CD amadurece: mais MHC e coestímulo, menos fagocitose", "dc-maturacao"),
   ("langerhans", "CD imatura na epiderme (célula de Langerhans)", "langerhans-naive")]),
 (15, "conteudo", "Linfonodo", [
   ("hev", "Vênulas de endotélio alto na zona T (paracórtex)", "hev"),
   ("foliculo", "Folículos B (primários/secundários com centro germinativo)", "foliculo-secundario")]),
 (16, "conteudo", "A resposta se adequa ao agressor (M. leprae)", [
   ("tuberculoide", "Hanseníase localizada: resposta celular eficiente (Th1)", "lepra-tuberculoide"),
   ("lepromatosa", "Hanseníase disseminada: resposta ineficiente (Th2)", "lepra-lepromatosa")]),
 (17, "conteudo", "Comprometimento das células T", [
   ("encruzilhada", "A célula naive escolhe Th1, Th2, Th3 ou Th17", "citocinas-decidem")]),
 (18, "conteudo", "Reconhecimento do antígeno na imunidade adquirida", [
   ("nao-nativo", "LT CD4 não reconhece antígeno nativo", "sem-peptideo"),
   ("processado", "Antígeno precisa ser capturado, processado e apresentado por APC", ["sem-peptideo", "mhc2-exogeno"])]),
 (19, "conteudo", "Tipos de APC", [
   ("dc-naive", "CD ativa LT naive (a mais competente)", "dc-naive"),
   ("macrofago-b", "Macrófago e linfócito B apresentam a LT efetor (coestimulador B7)", "b7-apcs")]),
 (20, "conteudo", "MHC I – LT CD8", [
   ("via-mhc1", "Proteína citosólica → proteassoma → TAP → RE → MHC I → CD8", ["proteassoma-tap", "mhc1-endogeno"])]),
 (21, "conteudo", "MHC II – LT CD4", [
   ("via-mhc2", "Endocitose → endossomo → MHC II → CD4", "mhc2-exogeno"),
   ("cadeia-invariante", "Cadeia invariante ocupa o MHC II até o endossomo", ["cadeia-invariante", "invariante-endossomo"]),
   ("cruzada", "Apresentação cruzada: antígeno fagocitado vai ao MHC I (transcrição)", "apresentacao-cruzada")]),
 (22, "conteudo", "Fases da resposta imune celular", [
   ("fases-ativacao", "Reconhecimento → ativação → expansão clonal → efetores", ["sinal1", "sinal2", "il2-autocrina"]),
   ("homeostasia", "Homeostasia: apoptose da maioria dos efetores", "contracao"),
   ("memoria", "Geração de células de memória", "memoria")]),
 (23, "conteudo", "Fases da imunidade adaptativa (curva)", [
   ("tempo", "Pico em ~7–14 dias; memória após 30 dias", "pico")]),
 (24, "conteudo", "Ativação de linfócitos T (Abbas)", [
   ("cd4-cd8-il2", "CD4 e CD8 naive ativados pela APC, IL-2, efetores e memória", ["il2-todos", "memoria"])]),
 (25, "conteudo", "Reconhecimento: receptor da célula T", [
   ("cd3", "TCR associado a CD3 (γ, δ, ε) e ζ, que sinalizam", "cd3"),
   ("pre-tcr", "Receptor da célula pré-T (pTα)", EXC + "estrutura do pré-TCR é detalhe de desenvolvimento sem pergunta própria nesta aula nem nas provas")]),
 (26, "conteudo", "Sinapse imunológica", [
   ("sinapse", "TCR–MHC no centro (cSMAC), LFA-1–ICAM-1 na periferia (pSMAC)", "sinapse")]),
 (27, "conteudo", "Ativação linfocitária", [
   ("sinal1", "1º sinal: TCR × MHC-peptídeo", "sinal1"),
   ("sinal2", "2º sinal: moléculas acessórias (coestímulo)", "sinal2"),
   ("anergia", "Sem 2º sinal, o LT fica anérgico (monitoria)", "anergia")]),
 (28, "conteudo", "Coestimulação: CD80/CD86 × CD28/CTLA-4", [
   ("b7-cd28", "APC: CD80 (B7.1), CD86 (B7.2); LT: CD28 ativador constitutivo", "sinal2"),
   ("ctla4", "CTLA-4 inativador, induzido mais tarde, encerra a resposta", "ctla4")]),
 (29, "conteudo", "Moléculas acessórias e ligantes", [
   ("acessorias", "LFA-1/ICAM-1, CD2/LFA-3, CD28/B7, CD4/MHC II, CD8/MHC I", ["sinapse", "mhc2-cd4", "mhc1-cd8", "sinal2"]),
   ("drogas", "Alvos de fármacos: anti-CD3, anti-CTLA-4, anti-PD-1", "ipilimumab")]),
 (30, "conteudo", "Expansão clonal (curva)", [
   ("curva", "Naive → expansão → efetora → declínio → memória", ["pico", "contracao", "memoria"])]),
 (31, "conteudo", "Expansão clonal – IL-2", [
   ("il2-expansao", "IL-2 é a principal citocina de expansão clonal de CD4 e CD8", "il2-todos"),
   ("autocrina", "Ação autócrina da IL-2", "il2-autocrina"),
   ("helper-cd8", "IL-2 do CD4 ajuda o CD8 a expandir e virar citotóxico", "il2-cd8")]),
 (32, "conteudo", "IL-2 e proliferação", [
   ("il2r", "Ativação induz a cadeia α (CD25): IL-2R de alta afinidade", "cd25")]),
 (33, "conteudo", "IL-2 e AICD", [
   ("aicd", "Estímulo persistente: Fas/FasL, caspase-8, morte induzida por ativação", ["aicd", "fas-extrinseca"]),
   ("passiva", "Antígeno eliminado: morte passiva (citocromo c, caspase-9)", "contracao")]),
 (34, "capa", "Mecanismos efetores celulares (divisória)", []),
 (35, "conteudo", "Mecanismos efetores", [
   ("cd4-efetor", "CD4: citocinas ativam macrófagos, inflamação e LT/LB", "imunidade-celular"),
   ("cd8-efetor", "CD8: destruição da célula infectada", "ctl-apoptose")]),
 (36, "conteudo", "Ativação de macrófagos", [
   ("cd40", "CD40L do Th1 + CD40 do macrófago", "cd40l-macrofago"),
   ("ifng", "IFN-γ ativa o macrófago a matar o fagocitado", "ifng-macrofago"),
   ("mhc-b7", "Macrófago ativado expressa mais MHC e B7", "ifng-mhc2")]),
 (37, "conteudo", "Aumenta fagocitose e opsonização", [
   ("opsonizacao", "IgG produzida com ajuda do Th1 opsoniza", "ifng-igg")]),
 (38, "conteudo", "Síntese do óxido nítrico", [
   ("nos", "NOS: arginina → citrulina + NO", "nos"),
   ("peroxinitrito", "NO + superóxido → peroxinitrito (ERN); iNOS induzida", "inos"),
   ("ero", "Superóxido (phox), SOD, H2O2", "explosao-respiratoria")]),
 (39, "conteudo", "Apresentação de antígenos pelo macrófago", [
   ("mhc2-macrofago", "Fagolisossomo, cadeia invariante, MHC II na membrana", ["mhc2-exogeno", "cadeia-invariante"])]),
 (40, "conteudo", "Ativação de macrófagos: resumo", [
   ("ero-ern", "Produção de ERO e ERN", ["explosao-respiratoria", "inos"]),
   ("mhc", "Aumento de MHC II e I e de moléculas acessórias", "ifng-mhc2"),
   ("lisossomo-pg", "Enzimas lisossomais e prostaglandinas", EXC + "itens de lista-resumo; o alvo recuperável (macrófago ativado mata mais e apresenta melhor) já está em cards próprios")]),
 (41, "conteudo", "Ativação de células T CD8", [
   ("cd8-apc", "CD8 reconhece antígeno de célula infectada fagocitada pela CD (cruzada)", "apresentacao-cruzada"),
   ("cd8-ajuda", "CD4 helper e coestímulo B7–CD28 levam à expansão do CTL", "il2-cd8")]),
 (42, "conteudo", "Morte pelo CTL", [
   ("perforina", "Granzimas entram pelos poros da perforina e ativam caspases", "sh-1791593462592"),
   ("fasl", "FasL do CTL + Fas da célula-alvo", "fasl-ctl")]),
 (43, "conteudo", "Linfócitos T CD8+ citotóxicos: etapas", [
   ("conjugado", "Reconhecimento do mesmo MHC I–peptídeo e formação do conjugado", "ctl-mesmo-mhc"),
   ("desligamento", "Exocitose dos grânulos, desligamento do CTL ('kiss and run')", "ctl-desliga")]),
 (44, "conteudo", "Apoptose", [
   ("apoptose", "Morte celular programada da célula-alvo", "ctl-apoptose")]),
 (45, "conteudo", "Células T e B", [
   ("cd40-b", "CD40L–CD40 ativa o LB (plasmócito)", "cd40-b"),
   ("troca", "Troca de classe depende de CD40L e citocinas", "class-switch")]),
 (46, "capa", "Plasticidade celular (divisória)", []),
 (47, "conteudo", "Sinais do meio ambiente determinam a plasticidade", [
   ("citocinas", "Citocinas da APC e das células inatas decidem o subtipo", "citocinas-decidem"),
   ("equilibrio", "Equilíbrio efetor × Treg (perda de Foxp3, exTreg)", ["treg-supressao", "plasticidade-hibrido"])]),
 (48, "conteudo", "Sinalização, metabolismo e cromatina", [
   ("epigenetica", "Abertura/fechamento da cromatina define o subtipo", "epigenetica"),
   ("metabolismo", "Glicólise × OXPHOS na reprogramação", EXC + "o professor diz que as vias 'não precisa decorar'; ideia geral no card de epigenética")]),
 (49, "conteudo", "Subclasses T CD4+", [
   ("th1", "Th1: IFN-γ, micróbios intracelulares", "th1-ifng"),
   ("th2", "Th2: IL-4, IL-5, IL-13, helmintos e alergia", ["th2-citocinas", "th2-eosinofilo", "th2-ige"]),
   ("th17", "Th17: IL-17, bactérias, doenças inflamatórias", ["th17-il17", "th17-autoimune"])]),
 (50, "conteudo", "Citocinas de diferenciação", [
   ("th1-ind", "IFN-γ, IL-12 → Th1", "th1-inducao"),
   ("th2-ind", "IL-4 → Th2", "th2-inducao"),
   ("th17-ind", "IL-6, TGF-β → Th17", "th17-inducao"),
   ("treg-ind", "TGF-β, ácido retinoico, IL-2 → iTreg", ["treg-inducao", "acido-retinoico"]),
   ("tfh", "IL-21 → Tfh", EXC + "Tfh é assunto da aula seguinte (ativação de células B); aqui só rótulo do esquema")]),
 (51, "conteudo", "Fatores de transcrição", [
   ("tbet", "Th1: T-bet", "fatores-transcricao"),
   ("gata3", "Th2: GATA3", "fatores-transcricao"),
   ("ror", "Th17: RORγt", "fatores-transcricao"),
   ("foxp3", "Treg: Foxp3", "treg-marcadores"),
   ("silencia", "O fator de um subtipo silencia os outros", "epigenetica")]),
 (52, "conteudo", "Subtipos (Boniface 2013)", [
   ("th9-th22", "Th9 (PU.1), Th22 (AHR) e suas funções", EXC + "subtipos menores da figura de revisão; o professor não os explica e o Abbas os trata como nomenclatura em expansão")]),
 (53, "conteudo", "Diferenciação Th1 e Th2", [
   ("balanco", "Th1 inibe Th2 e Th2 inibe Th1", ["th2-inibe-ifng", "th1-inibe"])]),
 (54, "conteudo", "Desenvolvimento Th1", [
   ("il12-macro", "IL-12 do macrófago/CD", "il12-macrofago"),
   ("ifng-nk", "IFN-γ da NK", "ifng-nk-th1")]),
 (55, "conteudo", "Funções Th1", [
   ("macrofago", "IFN-γ ativa macrófago (M1)", ["ifng-macrofago", "m1"]),
   ("igg", "IFN-γ faz o LB produzir IgG opsonizante", "ifng-igg")]),
 (56, "conteudo", "Citocinas Th1 (IL-12)", [
   ("il12-alvos", "IL-12 estimula Th1, NK e CD8 a secretar IFN-γ", "il12-th1")]),
 (57, "conteudo", "Desenvolvimento Th2", [
   ("il4-th2", "IL-4 diferencia Th2", "th2-inducao"),
   ("il4-fonte", "Fonte inicial de IL-4 ('from other cellular sources?')", EXC + "pergunta aberta no próprio slide; a origem (mastócito) é hipótese do professor")]),
 (58, "conteudo", "Funções Th2", [
   ("il4-ige", "IL-4 → IgE", "il4-ige"),
   ("il5", "IL-5 ativa eosinófilos contra helmintos", "th2-eosinofilo")]),
 (59, "conteudo", "Citocinas Th2 (IL-4)", [
   ("il4-inibe-macro", "IL-4 inibe a ativação do macrófago", "m2"),
   ("igg4", "Troca para IgE e IgG4 no homem", "il4-ige")]),
 (60, "capa", "Regulando a resposta (divisória)", []),
 (61, "conteudo", "Treg natural × induzida", [
   ("ntreg", "Treg natural Foxp3+ do timo; induzida na periferia (TGF-β, IL-10)", "treg-natural")]),
 (62, "conteudo", "Tregs naturais", [
   ("marcadores", "CD4, CD25, Foxp3", "treg-marcadores"),
   ("ctla4-treg", "CTLA-4 na Treg; ação por contato", "treg-ctla4"),
   ("gitr", "GITR, CD103, OX-40, 4-1BB, neuropilina", EXC + "lista de marcadores menores; CD25, Foxp3 e CTLA-4 têm cards")]),
 (63, "conteudo", "Funções das Tregs", [
   ("citocinas-treg", "IL-10 inibe APC; TGF-β inibe proliferação T", ["il10-apc", "tgfb-proliferacao", "treg-citocinas", "il10"]),
   ("supressao", "Reduzem ativação, proliferação e função efetora", "treg-supressao"),
   ("autoimunidade", "Deficiência de Treg → autoimunidade (IPEX)", "ipex")]),
 (64, "conteudo", "IL-2, T efetoras e Tregs", [
   ("treg-il2", "Treg depende da IL-2 dos T ativados (CD25)", "treg-il2")]),
 (65, "conteudo", "Treg (Foxp3) × Th17 (RORγt)", [
   ("equilibrio-th17", "Equilíbrio Th17 × Treg", "th17-treg")]),
 (66, "conteudo", "Th17: IL-6 + TGF-β", [
   ("il6-tgfb", "TGF-β + IL-6 → Th17; TGF-β sozinho → Treg", "th17-treg"),
   ("il23", "IL-23 e IL-1 mantêm o Th17", "il23")]),
 (67, "conteudo", "Gradiente IL-6/TGF-β", [
   ("gradiente", "Mais IL-6 → Th17; mais TGF-β → Treg", "th17-treg")]),
 (68, "conteudo", "Visão geral das subclasses", [
   ("funcoes", "Th1 imunidade celular; Th2 humoral/alergia; Th17 inflamação tecidual", ["th1-ifng", "th2-ige", "th17-autoimune"])]),
 (69, "revisao", "Esquema geral (Th0, Tr1/Th3, BAFF)", []),
 (70, "conteudo", "Plasticidade (DuPage 2016)", [
   ("hibridos", "Células intermediárias (Th1/Th17) e reversão", "plasticidade-hibrido")]),
 (71, "conteudo", "Hipersensibilidade tardia", [
   ("dth", "Imunidade celular gerando lesão: hipersensibilidade tipo IV (CD4)", "EXC: aula 64 Hipersensibilidade (comentário de Davi 15/10: card de outro deck)"),
   ("granuloma", "Th1 e granuloma", "granuloma-ifng")]),
]
JUSTIFICATIVAS = {"capa": "capa ou divisória de bloco, sem conteúdo",
                  "revisao": "esquema-resumo de revisão (Th0, Tr1/Th3, BAFF); os subtipos e citocinas já estão nas lâminas 49–68"}

CAPITULO = [
 ("Abbas 8ª ed., cap. 9 (Ativação dos linfócitos T)", [
   ("ab-dc-naive", "Ativação de T naive requer DC madura em órgão linfoide", "dc-naive"),
   ("ab-coestimulo", "Sem coestímulo: apoptose ou não responsividade", "anergia"),
   ("ab-ctla4", "CTLA-4 tem maior afinidade por B7 e encerra respostas", "ctla4"),
   ("ab-cd40", "CD40L licencia a APC (mais B7, IL-12)", "cd40l-macrofago"),
   ("ab-il2r", "IL-2Rα (CD25) forma o receptor de alta afinidade", "cd25"),
   ("ab-memoria", "Memória: sobrevive sem antígeno, responde mais rápido", "memoria"),
   ("ab-contracao", ">90% dos efetores morrem quando o antígeno some", "contracao")]),
 ("Abbas 8ª ed., cap. 10 (CD4 efetoras)", [
   ("ab-th1", "IL-12 + IFN-γ → T-bet → Th1; IFN-γ ativa macrófagos", ["th1-inducao", "fatores-transcricao"]),
   ("ab-th2", "IL-4 → GATA3 → Th2; IgE e eosinófilos", ["th2-inducao", "fatores-transcricao"]),
   ("ab-th17", "IL-6/IL-1 + TGF-β → RORγt → Th17; neutrófilos", ["th17-treg", "fatores-transcricao"]),
   ("ab-m1m2", "Ativação clássica (IFN-γ) × alternativa (IL-4/IL-13)", ["m1", "m2"])]),
 ("Abbas 8ª ed., cap. 11 (CD8 efetoras) e cap. 15 (Treg)", [
   ("ab-cruzada", "Apresentação cruzada por DC ativa CD8 naive", "apresentacao-cruzada"),
   ("ab-ctl-especifico", "CTL mata só o alvo com o mesmo MHC I–peptídeo e se desliga", ["ctl-mesmo-mhc", "ctl-desliga"]),
   ("ab-ipex", "Mutação de Foxp3 causa IPEX", "ipex")]),
]

EXERCICIOS = [
 ("Provas UC03 (índice imuno-08)", [
   ("p2025-treg", "2025 P3 4.1: papel do timo nas Tregs Foxp3+ e manipulação de Foxp3", ["treg-natural", "treg-marcadores", "il10-apc"]),
   ("p2018-cd8", "2018 P1 1.11 e 2017 P2 2.9: ativação de CD8 (apresentação cruzada, ajuda do CD4, IL-12/Th1)", ["apresentacao-cruzada", "il2-cd8", "il12-th1"]),
   ("p2015-ctl", "2015 P2 2.7: citotoxicidade do CTL (MHC I, desgranulação na sinapse, granzimas/perforina, apoptose)", ["sh-1791593462592", "ctl-mesmo-mhc", "ctl-desliga"]),
   ("p2015-selecao-clinica", "2015 P2 6.2: imunodeficiências da seleção tímica (falta de MHC, AIRE/APECED, Foxp3/IPEX)", ["mhc2-def", "aire", "aps1", "ipex"]),
   ("p2015-falha", "2015 P2 6.3: timócito que falha morre ou vira Treg; equivalentes periféricos", ["selecao-negativa", "contracao", "treg-natural"]),
   ("p2023-cd4", "2023 P1 2.9: ativação do CD4 (TCR–MHC II e coestímulo, proliferação, diferenciação)", ["sinal1", "sinal2", "citocinas-decidem"])]),
 ("Monitoria P2, aula 9", [
   ("mon-anergia", "Sem coestímulo: anergia", "anergia"),
   ("mon-cd3", "TCR acoplado ao CD3, fosforilado na ativação", "cd3"),
   ("mon-ctla4", "CTLA-4/B7 inativa; anti-CTLA-4 no câncer", ["ctla4", "ipilimumab"]),
   ("mon-fas", "Apoptose por Fas–FasL ao fim da resposta", "aicd"),
   ("mon-cd25", "CD25 aumenta a afinidade do IL-2R", "cd25"),
   ("mon-dth", "Teste de hipersensibilidade tardia mede memória Th1", "EXC: aula 64 Hipersensibilidade (comentário de Davi 15/10)"),
   ("mon-memoria", "Memória central (linfonodo, IL-7, L-selectina) × efetora", "memoria-central"),
   ("mon-ctl", "LFA-1/ICAM-1 no conjugado; um CTL mata vários alvos", ["sinapse", "ctl-desliga"])]),
 ("Apostila de veteranos, aula 6 caps. 2–5", [
   ("vet-selecao", "Seleção positiva no córtex (~95% morrem) e negativa na medula", ["selecao-positiva", "negativa-medula", "timo-5pct"]),
   ("vet-lfa1", "LFA-1 (baixa afinidade em repouso) estabiliza a ligação com ICAM-1", "sinapse"),
   ("vet-treg-il2", "IL-2 mantém Treg (CD25 alto); Treg consome IL-2", "treg-il2"),
   ("vet-th17", "Th17: IL-17 e IL-22, bactérias e fungos", ["th17-il17", "th17-neutrofilo"])]),
]
