# Especificação curada — Inflamação crônica (UC03 P3, Patologia; lâminas I Prof.ª Thais Mauad (30) e II Prof. Luiz F. Ferraz da Silva (20)).
# Mapa de escopo no fim do arquivo (ESCOPO). Ordem = lâminas I; o que só a versão II traz (tríade, polimorfonucleares, ciclo macrófago–linfócito) entra
# na lâmina I mais próxima. Granuloma/células epitelioides e gigantes = 47; Th1/Th2/Th17 e gatilhos de M1/M2 = 45; reparo e fibrose em detalhe = 65;
# hipersensibilidade tipo I = 64; MALT = 07 (Imunologia). P3: entra dessuspenso.
RUN_ID = "uc03-pt62-20261013a"
SHORT = "pt62"
LESSON = "2026-uc03-patologia-62-inflamacao-cronica"
DECK = "NEBLI::UC03::P3::Patologia::Inflamação crônica"
CRITERIOS = "MEMORY.md (reorganizado 13/10) + FEEDBACKS até F-20261013-CLAUDE-03, 13/10/2026"
_IMG = ("aguda-vs-cronica", "infiltrado-misto", "monocito-macrofago", "m1-m2", "macrofago-linfocito", "plasmocitos", "folículo-linfoide")
MEDIA = {f"pt62-{n.replace('í', 'i')}.png": f"img/pt62-{n.replace('í', 'i')}.png" for n in _IMG}
F = lambda n, w=460: f'<img src="pt62-{n.replace("í", "i")}.png" width="{w}">'
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 27 consultas sobre inflamação crônica, macrófago, M1/M2, plasmócito, "
         "folículo linfoide, eosinófilo, mastócito, bronquiectasia, silicose; busca/ext.txt, 5 consultas), cópias NEBLI vivas das aulas 23, 24, 37, 38, 45 e 47 conferidas, 13/10: ")
FALTA = "AnKing e externos não têm este alvo da aula (só a doença ou a célula em outro contexto)."
EXCLUIDOS = [
 (1473638467997, "silicose: card próprio da aula 47 (granulomatosa); aqui sílica só no Extra da causa tóxica"),
 (1473627826312, "definição clínica de bronquite crônica (tosse ≥ 3 meses): clínica, fora do ciclo básico desta aula"),
 (1473627847403, "índice de Reid: semiologia/patologia da DPOC, aula de patologia respiratória"),
 (1520717070355, "M2 por Th2: já vivo na aula 45 (entra por sh)"),
]
FORA_DO_RECORTE = [
 "Granuloma, células epitelioides e gigantes (lâmina 23 e prova 2015 P2 1.1): aula 47 Inflamação granulomatosa.",
 "Reparo, cicatrização e fibrose em detalhe (prova 2015 P2 3.4 e 2015 P2sub 3.2): aula 65 Reparo tecidual; aqui só a ligação macrófago M2 → TGF-β → fibrose.",
 "Subtipos de Th (Th1/Th2/Th17) e diferenciação: aula 45; aqui só o que cada um faz na inflamação crônica.",
 "Tecidos linfoides associados às mucosas (exercício 7): aula 07 Organização do sistema imune.",
 "Ilustrações: sericita no Paraná, bronquite pelo cigarro, bronquiolite folicular, foto da mão da artrite reumatoide, hepatite crônica, linfonodo.",
 "Vias de sinalização do asma (lâmina 28): hipersensibilidade tipo I, aula 64.",
]


def ak(key, src, cor, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=cor if isinstance(cor, dict) else {1: cor}, bloco=bloco, alvo=alvo,
             evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, cor, bloco, alvo, slide, autoria, espelhos, motivo, extra="", dup=""):
    import re
    n = sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", text)})
    return dict(key=key, kind="autoral", text=text, extra=extra, flags={i: cor for i in n}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}",
                autoria=autoria, busca=BUSCA + FALTA, espelhos=espelhos, motivo=motivo, duplicacao_ok=dup)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


EP_IC = [1487642816623, 1479267376848, 1520717070355]
EP_MAC = [1520717070355, 1487116928027, 1479267376848]
EP_EOS = [1479267436105, 1473628119069, 1479267439118]
EP_CAUSA = [1473628182439, 1488247925489, 1487642816623]

A_, B_, C_, D_, E_, G_ = "A-conceito-e-causas", "B-histologia", "C-macrofago", "D-linfocitos-e-plasmocitos", "E-outras-celulas", "F-exemplos"
CARDS = [
 # ---------- A. Conceito e causas (lâminas 2–5) ----------
 au("ic-nao-resolvida", "<b>Non-resolving</b> inflammation is harmful because it keeps {{c1::destroying}} tissue while repair replaces it with scar",
    Z, A_, "Por que a inflamação crônica é deletéria", 2, "prova", EP_IC, "Azul: exercício 1 da aula e lâmina 2 (Nathan & Ding).",
    extra="- It contributes to atherosclerosis, cancer, COPD, asthma, bowel disease and rheumatoid arthritis"),
 au("ic-def", "<b>Chronic inflammation</b> is inflammation of {{c1::prolonged}} duration, with tissue destruction and attempted repair",
    V, A_, "Definição de inflamação crônica", 4, "central", EP_IC, "Verde: definição da aula (lâmina 4; apostila e monitoria).",
    extra="- No exact time cutoff defines it; the histology does"),
 au("ic-persiste", "Inflammation becomes <b>chronic</b> when the injurious stimulus {{c1::persists}} or the immune response perpetuates itself",
    V, A_, "Princípio: estímulo persistente ou resposta que se perpetua", 4, "central", EP_IC,
    "Verde: princípio que organiza as quatro causas; sem ele as causas viram lista.",
    extra="- Acute inflammation ends when the stimulus is removed"),
 au("ic-sem-aguda", "Chronic inflammation does not always follow an acute one, since some viral and fungal infections are {{c1::insidious}} from the start",
    Z, A_, "Nem toda inflamação crônica vem de uma aguda", 4, "prova", EP_IC, "Azul: pergunta da lâmina 4 (“sempre após uma inflamação aguda?”)."),
 au("ic-causa-infec", "Persistent infections such as tuberculosis, fungal infections and {{c1::syphilis}} keep the stimulus present and cause chronic inflammation",
    Z, A_, "Causa: infecções persistentes", 5, "prova", EP_CAUSA, "Azul: primeira causa da lâmina 5 (exercício 3 pede doenças infecciosas).",
    extra="- Type IV hypersensitivity to them can form granulomas (granulomatous inflammation)"),
 au("ic-causa-toxico", "Prolonged exposure to toxic agents causes chronic inflammation, as with exogenous {{c1::silica}} and endogenous {{c2::atherosclerosis}} lipids",
    Z, A_, "Causa: exposição prolongada a agentes tóxicos", 5, "prova", EP_CAUSA, "Azul: segunda causa da lâmina 5.",
    extra="- Silicosis is detailed in the granulomatous inflammation lesson"),
 au("ic-causa-auto", "In <b>autoimmunity</b>, such as rheumatoid arthritis, the reaction against the body's own tissue is {{c1::self-perpetuating}}",
    Z, A_, "Causa: autoimunidade", 5, "prova", EP_CAUSA, "Azul: terceira causa da lâmina 5 (exercício 2 pede doenças não infecciosas).",
    extra="- The destructive autoimmune process is usually slow and progressive"),
 au("ic-causa-alergia", "In allergic individuals, immune-mediated disease such as {{c1::asthma}} (type I hypersensitivity) can become chronic inflammation",
    Z, A_, "Causa: doenças imunomediadas (alergia, asma)", 5, "prova", EP_CAUSA, "Azul: quarta causa da lâmina 5; asma na prova 2025 P3.",
    extra="- Type I hypersensitivity is detailed in the hypersensitivity lesson", dup="ganho: a causa (alergia) cobrada na lâmina 5; o card de Th2 pergunta o linfócito"),

 # ---------- B. Histologia (lâminas 6–7, 12) ----------
 au("ic-triade", "The triad of chronic inflammation is a {{c1::lymphomononuclear}} infiltrate, tissue {{c2::destruction}} and attempted healing with {{c3::fibrosis}} and vessel proliferation",
    V, B_, "Tríade histológica da inflamação crônica", 6, "prova", EP_IC,
    "Verde: pergunta direta da prova 2025 P3 3.5 e 2019 P3 4.4; núcleo da aula.",
    extra="- Fibrosis and angiogenesis are the healing attempt that the macrophage growth factors drive",
    dup="ganho: a tríade completa com destruição; o card da aula 38 cobre só infiltrado, angiogênese e fibrose"),
 au("ic-img", F("aguda-vs-cronica") + "<br>Panel A shows {{c1::chronic}} inflammation with a lymphoid aggregate, and panel B shows {{c2::acute}} inflammation with neutrophils in the alveoli",
    Z, B_, "Reconhecer inflamação crônica × aguda na histologia", 7, "prova", EP_IC,
    "Azul: lâmina 7, comparar os dois padrões no mesmo órgão.", extra="- Chronic: lymphocytes and macrophages, parenchymal destruction and fibrosis"),
 au("ic-pmn", "In chronic inflammation, <b>neutrophils</b> indicate {{c1::acute}} activity or persistent injury",
    Z, B_, "Polimorfonucleares na inflamação crônica", 7, "prova", EP_IC, "Azul: lâmina 6 da versão II."),
 ak("ic-infiltrado", 1487642816623, Z, B_, "Infiltrado: macrófagos, linfócitos e plasmócitos", 12, "Azul: HY que repete a tríade; o infiltrado misto da lâmina 12.",
    extra_add=F("infiltrado-misto", 380), hy_repete="ic-triade"),

 # ---------- C. Macrófago (lâminas 13–19) ----------
 au("mac-principal", "The {{c1::macrophage}} is the main cell of chronic inflammation, orchestrating and organizing the response",
    V, C_, "Macrófago = célula principal", 13, "central", EP_MAC, "Verde: lâmina 13 (“principal célula envolvida”).",
    extra="- It arises from monocytes made in the bone marrow", dup="ganho: a célula central da inflamação crônica; os demais cards de macrófago cobrem origem, função e destino"),
 ak("mac-origem", 1479267376848, V, C_, "O monócito vira macrófago no tecido", 13, "Verde: origem da célula principal da inflamação crônica.",
    extra_add=F("monocito-macrofago", 440)),
 au("mac-sfm", "Monocytes and tissue macrophages make up the {{c1::mononuclear phagocyte}} system",
    Z, C_, "Sistema fagocítico mononuclear", 15, "prova", EP_MAC, "Azul: lâmina 15."),
 au("mac-vida", "Blood monocytes live about {{c1::1 day}}, while tissue macrophages live for months",
    R, C_, "Vida média do monócito e do macrófago", 15, "lateral", EP_MAC, "Rosa: números da lâmina 15; explicam por que o macrófago persiste.",
    extra="- Long tissue survival lets macrophages sustain the chronic response"),
 sh(1791625430208, "azul", C_, "Associação: IFN-γ ativa o macrófago", 14, "Azul: ativação por citocinas (IFN-γ), lâmina 14."),
 au("mac-ativacao", "Activated macrophages grow larger and raise {{c1::lysosomal enzyme}} production, metabolism and phagocytosis",
    Z, C_, "Efeitos da ativação do macrófago", 14, "prova", EP_MAC, "Azul: lâmina 14.",
    extra="- Activators: bacterial products (TLR), cytokines such as IFN-γ and fibronectin"),
 sh(1791625434032, "verde", C_, "Associação: M1 vem de Th1/IFN-γ", 17, "Verde: M1 como macrófago da inflamação crônica, lâmina 17."),
 au("mac-m1", "<b>Classically activated (M1)</b> macrophages kill microbes with ROS, NO and lysosomal enzymes, a {{c1::microbicidal}} action",
    V, C_, "Função do macrófago M1", 17, "central", EP_MAC, "Verde: lâmina 17; exercício 6 pede os subtipos e sua atuação.",
    extra=F("m1-m2", 440) + "<br>- M1 also makes IL-1, IL-12, IL-23 and chemokines, which sustain inflammation"),
 sh(1791625434457, "verde", C_, "Associação: M2 vem de Th2/IL-4", 17, "Verde: M2, lâmina 17."),
 au("mac-m2", "<b>Alternatively activated (M2)</b> macrophages release growth factors and TGF-β, promoting tissue repair and {{c1::fibrosis}}",
    V, C_, "Função do macrófago M2", 17, "prova", EP_MAC,
    "Verde: prova 2018 P3 4.2 (relação entre inflamação crônica e fibrose, M2 e TGF-β).",
    extra="- M2 also makes IL-10 and TGF-β with anti-inflammatory effect"),
 au("mac-destroi", "Macrophage products kill microbes but also cause {{c1::tissue damage}}, which is why destruction is a hallmark of chronic inflammation",
    V, C_, "Produtos do macrófago destroem tecido", 18, "central", EP_MAC,
    "Verde: liga o macrófago à destruição da tríade (lâmina 18 e Robbins).",
    extra="- Elastases, neutral proteases, collagenase, lipase, reactive oxygen species and NO"),
 au("mac-recruta", "Macrophages secrete cytokines, chemokines and complement factors that {{c1::recruit}} more cells to the tissue",
    Z, C_, "Macrófago recruta células", 18, "prova", EP_MAC, "Azul: lâmina 18."),
 au("mac-cresc", "Macrophage growth factors stimulate {{c1::fibroblast}} proliferation, collagen deposition and angiogenesis",
    Z, C_, "Fatores de crescimento do macrófago", 18, "prova", EP_MAC, "Azul: lâmina 18; explica fibrose e proliferação vascular da tríade."),
 au("mac-limitada", "In limited inflammation, macrophages die or are cleared by {{c1::lymphatic}} drainage",
    Z, C_, "Destino do macrófago: inflamação limitada", 19, "prova", EP_MAC, "Azul: lâmina 19."),
 au("mac-persiste", "In persistent inflammation, macrophages accumulate through continuous {{c1::recruitment}}, local proliferation and immobilization",
    V, C_, "Destino do macrófago: inflamação persistente", 19, "central", EP_MAC,
    "Verde: mecanismo que mantém a inflamação crônica (lâmina 19).", extra="- Recruiters: C5a, MCP-1, PDGF, TGF-β"),
 au("mac-mif", "The cytokine {{c1::MIF}} immobilizes macrophages at the site of chronic inflammation",
    R, C_, "MIF imobiliza o macrófago", 19, "lateral", EP_MAC, "Rosa: detalhe da lâmina 19."),

 # ---------- D. Linfócitos e plasmócitos (lâminas 20–25) ----------
 au("lin-loop", "In chronic inflammation, T cells and macrophages activate each other in a {{c1::positive feedback}} loop that lasts while the stimulus remains",
    V, D_, "Ciclo macrófago–linfócito", 20, "central", EP_IC,
    "Verde: lâminas 20 e 21; explica por que a inflamação crônica se mantém.", extra=F("macrofago-linfocito", 420) + "<br>- IFN-γ from T cells activates macrophages; macrophages present antigen and release cytokines"),
 sh(1791625422657, "azul", D_, "Associação: Th1 ativa o macrófago", 22, "Azul: exercício 4 (tipos de linfócitos)."),
 au("lin-th2", "Th2 cells drive chronic allergic inflammation such as {{c1::asthma}}, with eosinophils",
    Z, D_, "Th2 na inflamação crônica alérgica", 22, "prova", EP_IC, "Azul: lâmina 22 e exercício 4.", extra="- Th2 cytokines IL-4, IL-5 and IL-13 recruit eosinophils and promote IgE", dup="ganho: o linfócito da inflamação alérgica; a causa está no card da lâmina 5"),
 au("lin-th17", "Th17 cells predominate in chronic {{c1::autoimmune}} inflammation",
    R, D_, "Th17 na inflamação autoimune", 22, "lateral", EP_IC, "Rosa: lâmina 22; o detalhe dos Th fica na aula 45."),
 au("plasmocitos", "<b>Plasma cells</b> are terminally differentiated B cells that accumulate where the antigen {{c1::persists}}",
    Z, D_, "Plasmócitos", 24, "prova", EP_IC, "Azul: lâmina 24.",
    extra=F("plasmocitos", 420) + "<br>- They make antibodies against persistent antigens or altered tissue components"),
 au("terciario", "In chronic inflammation, lymphoid follicles form in non-lymphoid organs, acting as {{c1::tertiary}} lymphoid tissue",
    Z, D_, "Folículos linfoides terciários", 25, "prova", EP_IC, "Azul: lâminas 24 e 25 (pulmão, sinóvia, fígado).",
    extra=F("folículo-linfoide", 360) + "<br>- Seen in lung, synovium, gut and liver; they copy a lymph node locally"),

 # ---------- E. Outras células (lâminas 27–30) ----------
 ak("mastocito", 1473628107938, R, E_, "Mastócito na asma", 27, "Rosa: lâmina 27 (mastócito) e 28 (asma); histamina pré-formada já é da aula 37.", clinica_lateral=True),
 au("eos-eotaxina", "<b>Eotaxin</b> recruits eosinophils through its single receptor, {{c1::CCR3}}",
    R, E_, "Eotaxina e CCR3", 29, "lateral", EP_EOS, "Rosa: detalhe da lâmina 29."),
 sh(1791780353397, "azul", E_, "Associação: eosinófilo secreta MBP", 29, "Azul: MBP tóxica a parasitas e epitélio respiratório."),
 au("neutro-fumo", "Neutrophils usually mark acute inflammation, but persist in the chronic inflammation of {{c1::smokers'}} airways",
    R, E_, "Neutrófilos na inflamação crônica do fumante", 30, "lateral", EP_IC, "Rosa: lâmina 30 e exercício 5 (inflamação crônica pelo cigarro).",
    extra="- Neutrophil elastase-positive cells in the airway"),

 # ---------- F. Exemplos de quadros crônicos (lâminas 8–9, 28) ----------
 au("ra-foliculos", "<b>Rheumatoid arthritis</b> is a chronic synovitis rich in {{c1::lymphoid follicles}}",
    R, G_, "Artrite reumatoide como inflamação crônica", 8, "lateral", EP_CAUSA, "Rosa: exemplo característico (lâmina 8; apostila e monitoria)."),
 ak("bronquiectasia", 1473628182439, R, G_, "Bronquiectasia: inflamação crônica necrosante", 9, "Rosa: exemplo característico (lâmina 9; apostila).",
    clinica_lateral=True),
 ak("asma-remodelamento", 1583372985929, R, G_, "Remodelamento brônquico da asma crônica", 28, "Rosa: prova 2025 P3 3.5 (alterações estruturais nas vias aéreas)."),
]

SEM_IMAGEM = "conceito ou relação sem estrutura própria a identificar; as imagens da aula estão nos cards de reconhecimento e nos Extras"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "sem_imagem" not in c and "<img" not in c.get("text", "") and "<img" not in c.get("extra", "") \
            and "<img" not in c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM

VERSO = {
 "ic-sem-aguda": "- Examples: some viral and fungal infections that start silently",
 "ic-causa-infec": "- Organisms that are hard to eliminate keep driving the response",
 "ic-causa-auto": "- The destructive autoimmune process is usually slow and progressive",
 "ic-pmn": "- Acute activity or persistent injury on top of the chronic process",
 "ic-causa-toxico": "- Atherosclerosis: oxidized lipids in the arterial wall",
 "mac-sfm": "- Bone marrow precursor → blood monocyte → tissue macrophage",
 "mac-vida": "- Long survival in the tissue lets macrophages sustain the response",
 "mac-ativacao": "- Activators: bacterial products (TLR), IFN-γ and fibronectin",
 "mac-recruta": "- Cytokines, chemokines and complement factors bring more cells",
 "mac-cresc": "- This is the repair attempt of the triad: fibrosis and new vessels",
 "mac-limitada": "- Macrophages leave or die when the stimulus is controlled",
 "mac-mif": "- Immobilized macrophages stay and keep the inflammation going",
 "lin-th17": "- Th17 cells make IL-17 and IL-22 and recruit neutrophils",
 "neutro-fumo": "- Neutrophil elastase-positive cells in the airway wall",
 "ra-foliculos": "- The synovium is destroyed while follicles form, a local tertiary lymphoid tissue",
 "eos-eotaxina": "- Eosinophils then release major basic protein, toxic to parasites and epithelium",
 "mastocito": "- Mast cells and eosinophils sustain chronic allergic inflammation",
}
DUPLICACAO = {}
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Robbins/Janeway/Mellors); é o objetivo mostrar o padrão ou o esquema, sem figura equivalente no AnKing"
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = VERSO[k] + ("<br>" + c["extra"] if c.get("extra") else "")
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
    if "pt62-" in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT


BOLD = {
 "ic-sem-aguda": ["Chronic inflammation"], "ic-causa-infec": ["Persistent infections"], "ic-causa-toxico": ["toxic agents"], "ic-causa-alergia": ["allergic individuals"],
 "ic-triade": ["triad of chronic inflammation"], "ic-img": ["lymphoid aggregate"], "mac-principal": ["main cell of chronic inflammation"], "mac-ativacao": ["Activated macrophages"],
 "mac-sfm": ["Monocytes and tissue macrophages"], "mac-vida": ["Blood monocytes"], "mac-destroi": ["Macrophage products"], "mac-recruta": ["Macrophages secrete"],
 "mac-cresc": ["growth factors"], "mac-limitada": ["limited inflammation"], "mac-persiste": ["persistent inflammation"], "mac-mif": ["chronic inflammation"],
 "lin-loop": ["T cells and macrophages"], "lin-th2": ["Th2 cells"], "lin-th17": ["Th17 cells"], "terciario": ["lymphoid follicles"], "neutro-fumo": ["Neutrophils"],
 "ic-pmn": ["neutrophils"],
}
for c in CARDS:
    for ph in BOLD.get(c["key"], []):
        if c["kind"] == "autoral" and f"<b>{ph}</b>" not in c["text"] and ph in c["text"]:
            c["text"] = c["text"].replace(ph, f"<b>{ph}</b>", 1)

import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))

IMAGENS_VISTAS = {
 "pt62-aguda-vs-cronica.png": "Lâmina II 8 (Robbins): A pulmão com agregado linfoide e septos fibrosados (crônica), B alvéolos cheios de neutrófilos (aguda); recorte sem logotipo.",
 "pt62-infiltrado-misto.png": "Lâmina I 12: infiltrado com plasmócitos, macrófagos e eosinófilos em grande aumento; sem legenda no recorte, o rótulo está na frente do AnKing.",
 "pt62-monocito-macrofago.png": "Lâmina II 13 (Robbins): medula → sangue → tecido com monócito e macrófago ativado; esquema legível.",
 "pt62-m1-m2.png": "Lâmina II 3 (Robbins): ativação clássica (M1) × alternativa (M2) com estímulos e produtos; figura completa, no Extra.",
 "pt62-macrofago-linfocito.png": "Lâmina II 17 (Robbins): ciclo T–macrófago com IFN-γ, TNF, IL-1; recorte sem o título do slide.",
 "pt62-plasmocitos.png": "Lâmina II 19: baixo e alto aumento de plasmócitos (núcleo excêntrico); legível.",
 "pt62-foliculo-linfoide.png": "Lâmina II 20: folículo linfoide em órgão não linfoide, em grande aumento; legível, sem legenda.",
}

REVISAO = {
 "ic-triade": "Prova 2025 P3 3.5: três elementos (infiltrado linfomononuclear, dano tecidual, fibrose) conferem com o gabarito",
 "mac-m2": "Robbins cap. 2 e prova 2018 P3 4.2: M2 → TGF-β → fibroblastos e colágeno",
 "ic-img": "Painel A = agregado linfoide com fibrose; B = neutrófilos; conferido na figura do Robbins",
}

ESCOPO = {
 "objetivo": "Entender a inflamação crônica como inflamação prolongada em que dano, resposta imune e reparo coexistem, quais células a sustentam e por que persiste",
 "centrais": [("definição de inflamação crônica", "ic-def", "ic-sem-aguda"),
              ("princípio: estímulo que persiste ou resposta que se perpetua", "ic-persiste", "ic-causa-infec", "ic-causa-toxico", "ic-causa-auto", "ic-causa-alergia"),
              ("tríade histológica", "ic-triade", "ic-img", "ic-pmn"),
              ("macrófago como célula principal e sua origem", "mac-principal", "mac-origem", "mac-ativacao"),
              ("M1 × M2 e destruição × reparo", "mac-m1", "mac-m2", "mac-destroi", "mac-cresc"),
              ("destino do macrófago: limitado × persistente", "mac-limitada", "mac-persiste", "mac-mif"),
              ("ciclo macrófago–linfócito que mantém a inflamação", "lin-loop", "lin-th2", "lin-th17"),
              ("plasmócitos e tecido linfoide terciário", "plasmocitos", "terciario")],
 "exemplos": ["sericita no Paraná (silicose)", "bronquite crônica do fumante (histologia)", "bronquiolite folicular", "hepatite crônica e linfonodo (fotos)",
              "mão da artrite reumatoide (só o cartão rosa de folículos)"],
 "outras_aulas": [("granuloma, células epitelioides e gigantes", "47 Inflamação granulomatosa"), ("Th1/Th2/Th17 e gatilhos de M1/M2", "45 Ativação de linfócitos T"),
                  ("reparo, cicatrização e fibrose em detalhe", "65 Reparo tecidual"), ("hipersensibilidade tipo I e vias da asma", "64 Hipersensibilidade"),
                  ("MALT", "07 Organização do sistema imune")],
}
