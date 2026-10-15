# Especificação curada — Inflamação crônica (UC03 P3, Patologia; lâminas I Thais Mauad, 30; lâminas II Luiz F. Ferraz da Silva, 20).
# Reconstrução de 14/10/2026 após Davi apagar a versão de 13/10 (PLANO-CONTINUACAO-DECKS §1/§4). Percurso e capacidades: percurso-aula.md.
# Ordem = lâminas I; o que só a II traz entra na lâmina I correspondente. Granuloma = 47; diferenciação de Th = 45; reparo em detalhe = 65;
# hipersensibilidade tipo I = 64; MALT em si = 07. P3: entra disponível (não suspender).
RUN_ID = "uc03-pt62-20261014a"
SHORT = "pt62"
LESSON = "2026-uc03-patologia-62-inflamacao-cronica"
DECK = "NEBLI::UC03::P3::Patologia::Inflamação crônica"
CRITERIOS = "MEMORY.md + FEEDBACKS até F-20261014-CLAUDE-01 + PLANO-CONTINUACAO-DECKS (C1–C7) + PLANO-CARDS-TABS, 14/10/2026"
_IMG = ("aguda-vs-cronica", "m1-m2", "macrofago-linfocito", "monocito-macrofago", "plasmocitos", "foliculo-linfoide")
MEDIA = {f"pt62-{n}.png": f"img/pt62-{n}.png" for n in _IMG}
F = lambda n, w=460: f'<img src="pt62-{n}.png" width="{w}">'
V, Z, R = 3, 4, 5
BUSCA = ("AnKing e Referências Externas por frases e sinônimos (busca/anking.txt, 39 consultas; busca/anking2.txt, 8), seções AnKing "
         "Pathoma 02 Chronic Inflammation, FirstAid Chronic inflammation, Bootcamp Chronic Inflammatory Response e B&B Acute and Chronic "
         "Inflammation lidas inteiras (busca/tags-secao.txt), cópias NEBLI vivas das aulas 37, 38, 45 e 47 conferidas, 14/10: ")
EXCLUIDOS = [
 (1583372985929, "remodelamento como pista para o diagnóstico de asma (cloze no nome da doença): a aula pede o processo, coberto por asma-remodelamento"),
 (1487639081947, "padrão agudo (edema e neutrófilos): alvo da aula 38; aqui só como contraste no Extra"),
 (1487981568284, "VEGF e angiogênese: reparo em detalhe é da aula 65; citado no Tab do reparo"),
 (1487116849895, "segundo sinal B7–CD28: já vivo na aula 45 (entra por sh 1791625428533)"),
 (1701944904845, "definição e composição do MALT: aula 07 Organização do sistema imune; aqui só a distinção do terciário"),
 (1487643792482, "IL-12 no granuloma: vivo na 47; o circuito geral é lin-circuito"),
 (1473628107938, "histamina do mastócito na fase precoce da asma: hipersensibilidade tipo I, aula 64"),
]
FORA_DO_RECORTE = [
 "Granuloma, células epitelioides e gigantes (lâmina 23; prova 2015 P2 1.1): aula 47; aqui só a ponte sh 1791716405167.",
 "Reparo e cicatrização em detalhe (tecido de granulação, VEGF, maturação do colágeno; prova 2015 P2 3.4): aula 65.",
 "Diferenciação dos Th (indutores, fatores de transcrição): aula 45; aqui só o que cada subtipo faz na inflamação crônica.",
 "Hipersensibilidade tipo I (sensibilização, fases precoce/tardia, IgE): aula 64.",
 "MALT (composição, placas de Peyer): aula 07; aqui só a distinção com o tecido linfoide terciário (exercício 7).",
 "Ilustrações: mão e sinóvia da artrite reumatoide, bronquiectasia, minas de sericita, bronquite pelo cigarro, bronquiolite folicular, fragmentos virais persistentes (II-11).",
]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


# Espelhos AnKing por função da pergunta (C3e)
EP_TERMO = [1487642816623, 1487642929698, 1487639081947]        # termo/definição de padrão inflamatório
EP_MAC = [1489970364081, 1487643795892, 1487981558376]          # produto/ativação do macrófago
EP_CELULA = [1479267376848, 1479267515372, 1486776332176]       # identidade/origem de uma célula
EP_CIRCUITO = [1487643792482, 1487643795892, 1487116928027]     # citocina que liga duas células
EP_EOS = [1479267436105, 1473628119069, 1487116873670]          # eosinófilo/alergia
NAO = "AnKing e externos não têm este alvo geral (só a doença específica ou o granuloma)."

A_, B_, C_, D_, E_ = "A-por-que-persiste", "B-como-se-reconhece", "C-macrofago", "D-linfocitos-plasmocitos", "E-outras-celulas"
CID = ('<div data-nebli-organizacao="true" data-nebli-pista="CID">A tríade característica da <b>inflamação crônica</b> é constituída por:<br>'
       'C {{c2::cicatriz}}<br>I {{c1::infiltrado mononuclear}}<br>D {{c2::destruição tissular}}</div>')

CARDS = [
 # ---------- A. Por que persiste (lâminas 2–5) ----------
 au("ic-nao-resolvida", "In <b>chronic inflammation</b>, molecules released by dead cells and damaged matrix ({{c1::DAMPs}}) are sensed like microbes and keep re-igniting inflammation",
    {1: V}, A_, "Princípio: a lesão realimenta a inflamação (não resolução)", "2–3; Robbins p. 70", "central", NAO, EP_TERMO,
    "Verde: princípio da aula (lâminas 2–3; exercício 1); cloze no nome concreto (F-20261014-CLAUDE-04).",
    extra="- DAMPs = damage-associated molecular patterns<br>- This loop of injury and inflammation is why chronic inflammation fails to resolve",
    duplicacao_ok="ganho: DAMPs como motor da cronicidade; o card da 37 (suspensa) trata o disparo agudo pela necrose"),
 au("ic-duracao", "<b>Chronic inflammation</b> is inflammation that lasts {{c1::weeks to months}}",
    {1: Z}, A_, "Duração e coexistência de inflamação, lesão e reparo", "4; Robbins p. 70; cruzadas 15", "central", NAO, EP_TERMO,
    "Azul: definição da lâmina 4; a coexistência é cobrada pela tríade.",
    extra="- There is no exact cutoff: the coexistence of inflammation, injury and repair (C/I/D) defines chronicity"),
 au("ic-insidiosa", "<b>Chronic inflammation</b> may follow an acute episode or begin {{c1::insidiously}}, as in some viral and fungal infections",
    {1: Z}, A_, "Nem sempre começa por uma inflamação aguda", "4; II-4", "central", NAO, EP_TERMO,
    "Azul: pergunta explícita da lâmina 4 (“sempre após uma inflamação aguda?”).",
    extra="- A low-grade, silent response can damage tissue for a long time before symptoms"),
 ak("ak-causa-infeccao", 1487642929698, {1: Z}, A_, "Causa mais comum: infecção persistente", 5,
    "Azul: primeira causa da lâmina 5 (exercício 3); HY 4. Extra AnKing já lista os agentes."),
 au("ic-causas", '<div data-nebli-organizacao="true">Main causes of <b>chronic inflammation</b>:<br>- persistent {{c1::infections}}<br>- prolonged exposure to {{c2::toxic agents}}<br>- {{c3::immune-mediated}} diseases (autoimmunity, allergy)</div>',
    {1: V, 2: V, 3: V}, A_, "Organizador das causas: agente que fica × resposta que se perpetua", "5; II-5; Robbins p. 70", "central", NAO, EP_TERMO,
    "Verde: organiza todas as causas da lâmina 5 (exercícios 2 e 3); em tópicos com cloze em cada causa (F-20261014-CLAUDE-03).", duplicacao_ok="ganho: organizador do conjunto; o AnKing pergunta só a causa mais comum",
    extra="- Toxic: exogenous <b>silica</b>, endogenous lipids in <b>atherosclerosis</b><br>- Immune-mediated: <b>autoimmunity</b> (rheumatoid arthritis) and <b>allergy</b> (asthma)"),

 # ---------- B. Como se reconhece (lâminas 6–12) ----------
 au("ic-cid", CID, {1: V, 2: V}, B_, "Tríade C/I/D (organizador pedido por Davi)", "6; II-6; prova 2025 P3 3.5", "prova", NAO, EP_TERMO,
    "Verde: tríade da lâmina 6, cobrada na prova 2025 (três elementos valem a questão). Formato e agrupamento de Davi (F-20261014-CODEX-01).",
    extra="- C: repair attempt by <b>fibrosis</b> and new vessels (angiogenesis), not necessarily a mature scar",
    duplicacao_ok="ganho: card organizador pedido por Davi; a 38 tem a tríade só como desfecho da inflamação aguda (deck suspenso)"),
 ak("ak-celulas", 1487642816623, {1: V, 2: V}, B_, "Células do infiltrado mononuclear", "6; II-6; prova 2017 P3 4.1", "Verde: HY 2; infiltrado da tríade (prova 2017).",
    extra_add="- Left: chronic (lymphoid aggregate, fibrotic septa); right: acute (alveoli filled with neutrophils)<br>" + F("aguda-vs-cronica")),

 ak("ak-bronquiectasia", 1473628182439, {1: Z, 2: Z}, B_, "Bronquiectasia: fibrose e destruição dilatam a via aérea", 9,
    "Azul: lâmina 9 (histologia e peça) e monitoria P3 aula 10 (colágeno cicatricial retrai e abre o brônquio); HY 1. Ajuste 15/10 noite.",
    clinica_lateral="doença usada pela aula como exemplo da tríade; o núcleo verde é ic-cid"),

 # ---------- C. O macrófago (lâminas 13–19) ----------
 au("mac-principal", "The dominant cell of <b>chronic inflammation</b>, which orchestrates the response, is the {{c1::macrophage}}",
    {1: V}, C_, "Macrófago é a célula central", "13; II-12; Robbins p. 71; cruzadas 8", "central", NAO, EP_CELULA,
    "Verde: abre o bloco do macrófago (lâminas 13 e II-12).",
    extra="- It destroys tissue, recruits other cells and drives repair: the three parts of the triad",
    duplicacao_ok="ganho: hierarquia (célula principal); ak-celulas pergunta a composição do infiltrado"),
 ak("ak-monocito", 1479267376848, {1: V}, C_, "Origem: monócito → macrófago", 13, "Verde: HY 1; origem da lâmina 13 (cruzadas 16).",
    extra_add="- Monocytes leave the blood early in acute inflammation and become the dominant cell within about 48 h"),
 au("mac-sfm", "Bone marrow–derived <b>blood monocytes</b> and <b>tissue macrophages</b> form the {{c1::mononuclear phagocyte system}}",
    {1: Z}, C_, "Sistema fagocítico mononuclear", "15; II-13; Robbins p. 71", "central", NAO, EP_CELULA, "Azul: nome do sistema na lâmina 15.",
    extra="- Bone marrow → blood monocyte → tissue macrophage<br>" + F("monocito-macrofago")),
 au("mac-vida", "<b>Blood monocytes</b> live about {{c1::1 day}}, whereas tissue macrophages survive for {{c1::months}}",
    {1: Z}, C_, "Vida média: monócito × macrófago", "15; II-13; Robbins p. 71", "central", NAO, EP_CELULA,
    "Azul: números da lâmina 15; a sobrevida longa explica a persistência.",
    extra="- Long-lived macrophages can sustain a response for as long as the stimulus remains"),
 ak("ak-kupffer", 1486776332176, {1: V, 2: V}, C_, "Macrófago por órgão: Kupffer", 16, "Verde: HY 2; tabela de localizações da lâmina 16."),
 ak("ak-microglia", 1479430563185, {1: V}, C_, "Macrófago por órgão: micróglia", 16, "Verde: HY 2; tabela de localizações da lâmina 16."),
 sh(1791147097386, "azul", C_, "Macrófago por órgão: alveolar", 16, "Azul: tabela de localizações da lâmina 16 (monitoria P3 aula 10); vivo na 24 e na 47. Ajuste 15/10 noite (F-20261015-CLAUDE-05)."),
 au("mac-osteoclasto", "Blood <b>monocytes</b> give rise to tissue macrophages, microglia and bone {{c1::osteoclasts}}",
    {1: Z}, C_, "Derivados do monócito: osteoclasto", 16, "central", "Único acervo com o alvo (Histology 1701534444115) mistura percentual de leucócitos e texto colado; recusado 15/10 noite.", EP_CELULA,
    "Azul: lâmina 16 lista o osteoclasto entre os fagócitos mononucleares (inventário a31 estava excluído); Kupffer, micróglia e alveolar têm cards próprios. Ajuste 15/10 noite.",
    duplicacao_ok="ganho: osteoclasto como fagócito mononuclear; os outros derivados têm card próprio"),
 au("mac-fibronectina", "Besides microbial products and IFN-γ, <b>macrophages</b> are activated by the matrix protein {{c1::fibronectin}}",
    {1: R}, C_, "Terceiro ativador do macrófago", "14; monitoria P3 aula 10; apostila guia cap. 8", "central", "AnKing e externos sem fibronectina como ativador de macrófago (busca 15/10 noite).", EP_MAC,
    "Rosa: listado na lâmina 14, na monitoria e na apostila (inventário a26 estava excluído); atômico, sem virar organizador (F-20261015-CLAUDE-05).",
    duplicacao_ok="ganho: o terceiro ativador; IFN-γ e produtos microbianos têm cards próprios"),
 sh(1791625430208, "verde", C_, "IFN-γ ativa o macrófago", 14, "Verde: ativador principal da lâmina 14; vivo na 45."),
 sh(1791716411025, "azul", C_, "Ativação aumenta tamanho e enzimas lisossômicas", 14, "Azul: efeitos da ativação na lâmina 14; vivo na 47."),
 au("mac-m1m2", "<b>Microbial products</b> and IFN-γ drive classical (M1) macrophage activation, whereas {{c1::IL-4 and IL-13}} drive <b>alternative (M2)</b> activation",
    {1: V}, C_, "Organizador M1 × M2 pelos indutores", "17; II-3; cruzadas 2 e 13", "central", NAO, EP_MAC,
    "Verde: organiza as duas vias da lâmina 17 (exercício 6).", extra="- Th1 cells supply IFN-γ; Th2 cells supply IL-4 and IL-13<br>" + F("m1-m2")),
 sh(1791625434032, "verde", C_, "Th1 → M1 pró-inflamatório", 17, "Verde: fenótipo M1 (lâmina 17); vivo na 45."),
 sh(1791625434457, "verde", C_, "Th2 → M2 anti-inflamatório", 17, "Verde: fenótipo M2 (lâmina 17); vivo na 45."),
 au("mac-m1-no", "<b>M1 macrophages</b> kill ingested microbes using reactive oxygen species and {{c1::nitric oxide}}",
    {1: Z}, C_, "Ação do M1", "17; II-3; Robbins p. 71", "central", NAO, EP_MAC, "Azul: produto microbicida do M1 na lâmina 17 (exercício 6).",
    extra="- The same products leak out and injure host tissue"),
 au("mac-m2-tgf", "<b>M2 macrophages</b> drive repair and fibrosis mainly by secreting growth factors and {{c1::TGF-β}}",
    {1: V}, C_, "Ação do M2: TGF-β → fibrose", "17; prova 2018 P3 4.2", "prova", NAO, EP_MAC,
    "Verde: prova 2018 (M2 → TGF-β → fibroblastos → colágeno).", extra="- M2 also secretes <b>IL-10</b>, which dampens inflammation"),
 au("mac-destroi", "<b>Macrophage</b> {{c1::proteases}}, such as elastase and collagenase, degrade extracellular matrix and destroy tissue",
    {1: V}, C_, "Braço destruição: proteases", "18; Robbins p. 71", "central", NAO, EP_MAC, "Verde: liga os produtos da lâmina 18 ao D da tríade.",
    extra="- Lipases and coagulation factors are also secreted"),
 sh(1791716414575, "azul", C_, "ROS do macrófago lesam o tecido", 18, "Azul: metabólitos do oxigênio da lâmina 18; vivo na 47."),
 au("mac-recruta", "<b>Macrophage</b> TNF, IL-1 and {{c1::chemokines}} recruit more leukocytes, sustaining chronic inflammation",
    {1: V}, C_, "Braço recrutamento: citocinas e quimiocinas", "18; Robbins p. 72", "central", NAO, EP_MAC, "Verde: liga os produtos da lâmina 18 ao I da tríade.", duplicacao_ok="ganho: produtor e função diferentes (macrófago recrutando leucócitos); o AnKing do mastócito pergunta quimiocinas na resposta tardia alérgica",
    extra="- Complement fragments made by macrophages also attract cells"),
 ak("ak-tgf", 1487981558376, {1: V, 2: V, 3: V}, C_, "Braço reparo: TGF-β", 18, "Verde: HY 1; fatores de crescimento da lâmina 18 (C da tríade).",
    extra_add="- Made by M2 macrophages in chronic inflammation"),
 ak("ak-pdgf", 1487981564266, {1: R, 2: R}, C_, "Braço reparo: PDGF", "18; 19", "Rosa: HY 4; PDGF aparece nas lâminas 18–19 como fator de crescimento e de recrutamento."),
 au("mac-limitada", "When the <b>stimulus is eliminated</b>, macrophages die or leave the tissue through {{c1::lymphatics}}",
    {1: Z}, C_, "Destino do macrófago na inflamação limitada", "19; II-15; Robbins p. 71", "central", NAO, EP_CELULA, "Azul: primeiro ramo da lâmina 19.",
    extra="- This is how acute inflammation clears its macrophages"),
 au("mac-persiste", "In <b>persistent inflammation</b>, macrophages accumulate by recruitment, local proliferation and immobilization by {{c1::MIF}}",
    {1: Z}, C_, "Destino do macrófago na inflamação persistente", "19; II-15; Robbins p. 71", "central", NAO, EP_CELULA,
    "Verde/azul: segundo ramo da lâmina 19; MIF é o nome cobrado.",
    extra="- Recruitment signals: <b>C5a</b>, <b>MCP-1</b>, PDGF, TGF-β<br>- MIF = migration inhibitory factor",
    duplicacao_ok="ganho: mecanismo geral com MIF; a 47 pergunta só a proliferação dentro do granuloma"),

 # ---------- D. Linfócitos e plasmócitos (lâminas 20–26) ----------
 au("lin-circuito", "In <b>chronic inflammation</b>, macrophages stimulate T cells with antigen and {{c1::IL-12}}, and T cells activate macrophages with {{c2::IFN-γ}}",
    {1: V, 2: V}, D_, "Circuito bidirecional T–macrófago", "20–21; II-17; Robbins p. 72; cruzadas 17", "central", NAO, EP_CIRCUITO,
    "Verde: mecanismo que torna a resposta persistente (lâminas 20–21).", extra="- Each cell keeps the other active, so immune-driven inflammation tends to be persistent and severe<br>" + F("macrofago-linfocito"),
    duplicacao_ok="ganho: circuito geral nos dois sentidos; a 47 tem a versão do granuloma"),
 sh(1791625428533, "azul", D_, "Coestimulação B7–CD28 (macrófago como APC)", 20, "Azul: moléculas coestimuladoras da lâmina 20 e figura da 21; vivo na 45."),
 sh(1791625422657, "verde", D_, "Th1 ativa macrófagos", 22, "Verde: Th1 na lâmina 22 (exercício 4); vivo na 45."),
 sh(1791625432007, "azul", D_, "Th2 recruta eosinófilos", 22, "Azul: Th2 na lâmina 22 (exercício 4); vivo na 45."),
 sh(1791625422039, "azul", D_, "Th17 recruta neutrófilos", 22, "Azul: Th17 na lâmina 22; vivo na 45."),
 sh(1791625432257, "azul", D_, "Th17 e lesão autoimune", 22, "Azul: “autoimmune responses” na lâmina 22 (exercício 4); vivo na 45."),
 sh(1791716405167, "azul", D_, "Ponte: estímulo persistente → granuloma", 23, "Azul: lâmina 23 (granuloma com Th1); aula própria 47."),
 au("plasmocito", "<b>Plasma cells</b>, terminally differentiated {{c1::B cells}}, accumulate where antigen persists and secrete antibodies against it",
    {1: Z}, D_, "Plasmócitos na inflamação crônica", "24; II-18; Robbins p. 72", "central", NAO, EP_CELULA, "Azul: lâmina 24.",
    extra="- Targets: persistent foreign antigens, self antigens or altered tissue components"),
 ak("ak-plasmocito", 1479267515372, {1: V}, D_, "Reconhecer o plasmócito", 24, "Verde: HY 1; imagem de plasmócitos da lâmina 24.",
    extra_add="- Abundant in chronic infiltrates where antigen persists<br>" + F("plasmocitos")),
 au("terciario", "Strong <b>chronic inflammation</b> can organize lymphocytes and plasma cells into {{c1::tertiary lymphoid organs}} with germinal centers",
    {1: Z}, D_, "Tecido linfoide terciário", "24–26; II-18–20; Robbins p. 72", "central", NAO, EP_CELULA,
    "Azul: “tecido linfoide-like” das lâminas 24–26.",
    extra="- Seen in nonlymphoid tissue: rheumatoid synovium, chronic hepatitis, lung<br>" + F("foliculo-linfoide")),
 au("malt", "Unlike <b>tertiary follicles</b> induced by inflammation, {{c1::MALT}} is constitutive lymphoid tissue beneath mucosal surfaces",
    {1: R}, D_, "MALT × terciário", "26; exercício 7", "prova", NAO, EP_CELULA,
    "Rosa: exercício 7; o MALT em si é da aula 07.", extra="- MALT = mucosa-associated lymphoid tissue (e.g., Peyer patches)"),

 # ---------- E. Outras células (lâminas 27–30) ----------
 ak("ak-mastocito", 1479267463438, {1: V, 2: V}, E_, "Mastócito liga IgE pelo Fc", 27, "Verde: HY 1; mastócito da lâmina 27 e asma da 28.",
    extra_add="- Antigen cross-linking the bound IgE triggers degranulation"),
 ak("ak-mastocito-tardio", 1487207091819, {2: V}, E_, "Mastócito mantém a inflamação e atrai eosinófilos", 28, "Verde: HY 1; esquema da asma (lâmina 28)."),
 sh(1791743343634, "azul", E_, "Eotaxina recruta eosinófilos", 29, "Azul: lâmina 29; vivo na 37."),
 au("eos-ccr3", "<b>Eotaxin</b> attracts eosinophils by binding the chemokine receptor {{c1::CCR3}}",
    {1: R}, E_, "Receptor da eotaxina", 29, "lateral", NAO, EP_EOS, "Rosa: detalhe nomeado na lâmina 29.",
    extra="- Th2 cytokines (IL-5) also expand and activate eosinophils"),
 sh(1791780353397, "verde", E_, "MBP do eosinófilo: parasitas e epitélio", 29, "Verde: lâmina 29; vivo na 38."),
 au("asma-remodelamento", "In <b>chronic asthma</b>, repeated injury and repair cause airway {{c1::remodeling}}, with subepithelial collagen and smooth muscle hypertrophy",
    {1: Z}, E_, "Tríade aplicada: remodelamento da asma", "28; prova 2025 P3 3.5", "prova", NAO, EP_EOS,
    "Azul: prova 2025 (alterações estruturais das vias aéreas).",
    extra="- Mononuclear and eosinophilic infiltrate, epithelial damage and fibrosis: the triad in the airway"),
 au("neutro-cronico", "Which <u>granulocyte</u> persists in <b>smoke-induced</b> chronic airway inflammation and in chronic osteomyelitis? {{c1::Neutrophils}}",
    {1: Z}, E_, "Neutrófilos na inflamação crônica persistente", "30; II-6; exercício 5; cruzadas 14", "central", NAO, EP_TERMO,
    "Azul: lâmina 30 e exercício 5.",
    extra="- In a chronic infiltrate they signal ongoing acute activity or persistent injury"),
]

SEM_IMAGEM = "relação ou nome sem estrutura própria a reconhecer; as figuras que ensinam estão nos Extras de ak-celulas, mac-sfm, mac-m1m2, lin-circuito e terciario"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Robbins/Mellors), sem equivalente no AnKing; ensina o esquema ou o padrão"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pt62-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {}
DUPLICACAO = {}

IMAGENS_VISTAS = {
 "pt62-aguda-vs-cronica.png": "Lâmina II-8/I-7 (Robbins fig. 2-22): esquerda pulmão com agregado linfoide e septos fibrosados; direita alvéolos cheios de neutrófilos. Legível; letras A/B sem legenda.",
 "pt62-m1-m2.png": "Lâmina II-3 (Robbins): M1 × M2 com indutores e produtos; no Extra de mac-m1m2 (mostra a resposta, por isso não vai na frente).",
 "pt62-macrofago-linfocito.png": "Lâmina II-17 (Robbins): ciclo T–macrófago com IL-12 e IFN-γ; no Extra de lin-circuito.",
 "pt62-monocito-macrofago.png": "Lâmina II-13 (Robbins): medula → sangue → tecido, macrófagos por órgão; no Extra de mac-sfm.",
 "pt62-plasmocitos.png": "Lâmina II-19: plasmócitos em pequeno e grande aumento (núcleo excêntrico); Extra do AnKing de plasmócito.",
 "pt62-foliculo-linfoide.png": "Lâmina II-20/I-25: agregado linfoide em hepatite crônica; Extra de terciario.",
}

REVISAO = {
 "mac-m1m2": "C3: versão com classical/alternative ocultos vazava por contraste; agora oculta IL-4 e IL-13 (cruzadas 2), nomes das vias visíveis como organização",
 "ic-cid": "C2/C3: formato e agrupamento de Davi; C = tentativa de reparo (fibrose + vasos), esclarecido no Extra; prova 2025 cobra os três",
 "ak-celulas": "Núcleo AnKing (HY 2) que faltava na versão apagada; figura aguda × crônica no Extra",
 "lin-circuito": "C3: dois nomes (IL-12, IFN-γ) em sentidos opostos; nenhum deduzível do outro",
 "mac-destroi": "C3: resposta é a classe de enzima (proteases), não 'tissue damage'; versão apagada ocultava 'collateral tissue damage'",
 "mac-recruta": "C3: resposta 'chemokines' (classe nomeada); versão apagada ocultava 'recruit more leukocytes'",
}

ESCOPO = {
 "objetivo": "Explicar por que uma inflamação não se resolve, reconhecer a tríade e as células, e entender como o macrófago e o circuito com os linfócitos produzem destruição, recrutamento e reparo, aplicável às várias causas.",
 "centrais": [
   ("não resolução e causas", "ic-nao-resolvida", "ic-duracao", "ic-insidiosa", "ak-causa-infeccao", "ic-causas"),
   ("padrão histológico", "ic-cid", "ak-celulas"),
   ("macrófago: identidade", "mac-principal", "ak-monocito", "mac-sfm", "mac-vida", "ak-kupffer", "ak-microglia"),
   ("macrófago: ativação e polarização", "sh-1791625430208", "sh-1791716411025", "mac-m1m2", "sh-1791625434032", "sh-1791625434457", "mac-m1-no", "mac-m2-tgf"),
   ("macrófago: três braços dos produtos", "mac-destroi", "sh-1791716414575", "mac-recruta", "ak-tgf", "ak-pdgf"),
   ("macrófago: destino", "mac-limitada", "mac-persiste"),
   ("circuito T–macrófago e subtipos", "lin-circuito", "sh-1791625428533", "sh-1791625422657", "sh-1791625432007", "sh-1791625422039", "sh-1791625432257"),
   ("resposta humoral local", "plasmocito", "ak-plasmocito", "terciario", "malt"),
   ("inflamação crônica alérgica", "ak-mastocito", "ak-mastocito-tardio", "sh-1791743343634", "eos-ccr3", "sh-1791780353397", "asma-remodelamento"),
   ("neutrófilos na lesão persistente", "neutro-cronico"),
 ],
 "exemplos": ["artrite reumatoide", "bronquiectasia", "silicose/minas de sericita", "bronquite pelo cigarro", "hepatite crônica", "bronquiolite folicular", "fragmentos virais persistentes"],
 "outras_aulas": [("granuloma e células gigantes", "47 Inflamação granulomatosa"), ("diferenciação dos Th", "45 Ativação de linfócitos T"),
                  ("reparo e cicatrização", "65 Reparo tecidual"), ("hipersensibilidade tipo I", "64 Hipersensibilidade"), ("MALT", "07 Organização do sistema imune"),
                  ("padrão agudo", "38 Inflamação aguda")],
}

import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
