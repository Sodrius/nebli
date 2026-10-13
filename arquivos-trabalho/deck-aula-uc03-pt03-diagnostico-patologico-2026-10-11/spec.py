# Especificação curada — Diagnóstico patológico (UC03 P1, Patologia; Prof. Luiz Fernando Ferraz da Silva; 31 lâminas).
# Ordem = lâminas; o que só está na transcrição, nas palavras-cruzadas, nas bibliografias ou na apostila fica ancorado na lâmina do mesmo assunto.
import json, re, urllib.request
RUN_ID = "uc03-pt03-20261012a"
SHORT = "pt03"
LESSON = "2026-uc03-patologia-03-diagnostico-patologico"
DECK = "NEBLI::UC03::P1::Patologia::Diagnóstico patológico"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261011-CLAUDE-06) + plano vigente, 12/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, anking2.txt, anking3.txt; busca/ext.txt: Histology, MCAT, AnatoKing) "
         "e tags de seção FirstAid/Bootcamp (aterosclerose, evolução do infarto, febre reumática), cópias NEBLI vivas conferidas, 12/10: ")
EXCLUIDOS = [
    (1475966877989, "foam cells no subendotélio: repete 1471811989477, já escolhido"),
    (1471899256655, "infarto: sem alteração macroscópica nas primeiras 4 h; detalhe fora do dado da aula"),
    (1471899319397, "infarto 4 a 24 h macroscópico: a lâmina mostra horas, dias e semanas, sem esta divisão"),
    (1471899409106, "granulação de 3 a 14 dias: fora da aula (agudo, subagudo, cicatrizado)"),
    (1471541811425, "febre por pirogênios: o cartão vivo 1791743347261 já cobre IL-1/IL-6/TNF e é associado"),
    (1468250119090, "dineína axonemal: biologia celular de cílios, fora do alvo diagnóstico"),
    (1468101697168, "células permanentes: o alvo da aula é só que o miocárdio não regenera (card autoral)"),
    (1472058647432, "endocardite reumática com vegetações: patogenia da febre reumática, fora da aula"),
    (1471914925586, "insuficiência esquerda como causa de direita: repete a cadeia do fluxograma já coberta"),
    (1496165337190, "vimentina: marcador sem menção na aula (exemplos da aula: PSA, ER, HER2, queratina)"),
    (1496165353331, "desmina: marcador sem menção na aula"),
    (1496165362901, "GFAP: marcador sem menção na aula"),
    (1481335988953, "S-100: marcador sem menção na aula"),
    (1473638557173, "corpos de asbesto e azul da Prússia: detalhe lateral de outra aula"),
    (1468605700819, "translocação por FISH: citogenética (Biologia Molecular), fora do alvo"),
    (1468605679141, "FISH × cariótipo: repete 1468605672126"),
    (1500418458789, "Ziehl-Neelsen e fucsina fenicada: cartão vivo de Morfologia bacteriana, só detalhe de corante"),
    (1475364152379, "vermelho do Congo: amiloidose, fora da aula"),
]
FORA_DO_RECORTE = []

_cache = {}
def _nums(src):
    if src not in _cache:
        r = json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps(
            {"action": "notesInfo", "version": 6, "params": {"notes": [src]}}).encode())))["result"][0]
        _cache[src] = sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", r["fields"]["Text"]["value"])})
    return _cache[src]


def ak(key, src, cor, bloco, alvo, slide, motivo, origin=None, **kw):
    flags = {n: (cor[n] if isinstance(cor, dict) else cor) for n in _nums(src)}
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, cor, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    n = sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", text)})
    return dict(key=key, kind="autoral", text=text, extra=extra, flags={i: cor for i in n}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


def io(key, page, name, cor, bloco, alvo, motivo, rects, mask_rects=()):
    return dict(key=key, kind="slideio", page=page, half="full", title_size=99, lines=[], search=[], rects=list(rects),
                mask_rects=list(mask_rects), name=name, remarks="", aponta="estrutura", flags={1: cor}, bloco=bloco, alvo=alvo,
                evid=f"Slide {page}", motivo=motivo,
                busca=BUSCA + "sem figura equivalente com rótulos nos acervos (a imagem é da professora e traz os rótulos dentro dela).")


A_, B_, C_, D_, E_, F_, G_ = ("A-conceitos", "B-aterosclerose", "C-alteracoes-morfologicas", "D-manifestacoes-clinicas",
                              "E-patologia-na-assistencia", "F-macroscopia-e-processamento", "G-ferramentas")
DEF = [1471811875076, 1471809055703, 1468605672126]          # definições curtas "X é Y"
PROC = [1471811979298, 1471811989477, 1471811997810]          # processos em cadeia (aterosclerose)
MI = [1471899328126, 1471899362336, 1471899412796]            # evolução do infarto
COR = [1475982859127, 1475982852075, 1500419413812]          # corantes: o que cora
IHQ = [1496165181235, 1496165216576, 1496165396128]          # imuno-histoquímica
PROCED = [1462228531057, 1463106055950, 1536685206969]       # procedimentos diagnósticos
CIL = [1468250126050, 1468250119090, 1468605672126]

# rótulos desenhados dentro das figuras (pontos da página 720 x 540): o card esconde todos e pergunta um
M9 = {"agudo": (44.0, 117.5, 150.0, 161.0), "subagudo": (295.0, 116.0, 411.0, 167.5), "cicatrizado": (298.5, 341.5, 406.0, 385.0)}
M28 = {"primario": (35.0, 345.0, 130.0, 358.0), "secundario": (180.0, 296.0, 295.0, 330.0), "proteina": (184.0, 359.0, 231.0, 373.0),
       "produto": (54.0, 241.0, 98.0, 268.0), "hrpo": (181.0, 264.0, 218.0, 277.0), "dab": (73.0, 291.0, 98.0, 304.0)}
CARDS = [
 # ---------- A. Conceitos (lâminas 2 a 6, transcrição, Robbins) ----------
 au("patologia-def", "{{c1::<b>Pathology</b>}} studies the structural, biochemical and functional changes that underlie disease", Z, A_,
    "Patologia estuda alterações estruturais, bioquímicas e funcionais", "2", "central", "AnKing não define patologia.", DEF, "Azul: lâmina 2 e Robbins.",
    extra="- Structural changes are seen, whereas biochemical changes are measured"),
 au("bioquimica-antes", "In disease, <b>biochemical</b> and functional changes usually come before the {{c1::structural}} changes", Z, A_,
    "Alterações bioquímicas precedem as estruturais", "2", "central", "sem card nos acervos.", DEF, "Azul: lâmina 2 e transcrição.",
    extra="- In myocardial infarction, contractile dysfunction appears before any visible lesion"),
 au("patologia-vs-doenca", "<b>Pathology</b> is the study of disease and should not be used as a synonym for {{c1::disease}}", R, A_,
    "Patologia não é sinônimo de doença", "3", "lateral", "sem card nos acervos.", DEF, "Rosa: observação da professora."),
 au("sequencia-doenca", "A disease progresses from <b>etiology</b> to {{c1::pathogenesis}}, then {{c2::morphological}} and functional changes, then {{c3::clinical}} manifestations", V, A_,
    "Sequência etiologia, patogênese, alterações e manifestações", "3", "central", "AnKing não traz a sequência da doença.", DEF, "Verde: lâmina 3 e Robbins.",
    extra="- Each step explains the next one"),
 au("etiologia-def", "The <b>cause</b> of a disease is called its {{c1::etiology}}", V, A_,
    "Etiologia: o que causa a doença", "4", "central", "AnKing só traz a etiologia de doenças específicas.", DEF, "Verde: lâmina 4.",
    extra="- An etiologic agent is a specific external cause, such as pneumococcus in pneumonia"),
 au("etiologia-grupos", "<b>Etiologies</b> are divided into two main groups, {{c1::genetic}} and {{c2::acquired}}", V, A_,
    "Grupos de etiologia", "4", "central", "sem card nos acervos.", DEF, "Verde: lâmina 4."),
 au("genetica-def", "A <b>genetic</b> disease arises from a mutation that is inherited or occurs during {{c1::development}}", Z, A_,
    "Etiologia genética", "4", "central", "sem card nos acervos.", DEF, "Azul: lâmina 4 e transcrição."),
 au("adquirida-def", "An <b>acquired</b> disease results from the interaction of the person with the {{c1::environment}}, as in smoking-related emphysema", Z, A_,
    "Etiologia adquirida", "4", "central", "sem card nos acervos.", DEF, "Azul: lâmina 4 e transcrição.",
    extra="- Acquired causes are not always microorganisms, pollution counts too"),
 au("etiologia-multipla", "A disease can have a {{c1::single}} or multiple <b>etiologies</b>, as diabetes does with genetic and acquired components", Z, A_,
    "Etiologia única ou múltipla", "4", "central", "sem card nos acervos.", DEF, "Azul: lâmina 4 e Robbins.",
    extra="- Diabetes combines HLA-related genes with diet and obesity<br>- Atherosclerosis and cancer are multifactorial"),
 au("pneumonia-etiologias", "<b>Pneumonia</b> is always lung inflammation, but its etiologic agent may be pneumococcus, a {{c1::virus}} or inhaled smoke", R, A_,
    "Mesma doença, agentes diferentes", "4", "lateral", "sem card nos acervos.", DEF, "Rosa: exemplo da transcrição."),
 au("agente-etiologico", "An <b>etiologic agent</b> is an {{c1::external}} cause of disease, such as a microorganism", R, A_,
    "Agente etiológico", "4", "lateral", "sem card nos acervos.", DEF, "Rosa: nuance da professora.",
    extra="- A genetic alteration is an etiology, but DNA is not called an etiologic agent"),
 au("doenca-def", "<b>Disease</b> is a loss of {{c1::homeostasis}} that compensatory mechanisms fail to correct", V, A_,
    "Definição de doença", "4", "central", "AnKing não define doença.", DEF, "Verde: transcrição, conceito central.",
    extra="- A fright raises heart rate and blood pressure, but adaptation restores balance, so it is not disease"),
 au("nem-todo-agente", "An etiologic agent does not always cause disease, because {{c1::compensatory}} mechanisms may restore <b>homeostasis</b>", Z, A_,
    "Nem todo agente causa doença", "4", "central", "sem card nos acervos.", DEF, "Azul: transcrição."),
 au("subclinica", "In <b>subclinical</b> disease, homeostasis is lost without {{c1::clinical}} manifestations, as in early pneumonia or cancer", Z, A_,
    "Doença subclínica", "4", "central", "sem card nos acervos.", DEF, "Azul: transcrição.",
    extra="- It becomes symptomatic when the lesion grows and occupies more space"),
 au("patogenese-def", "The <b>mechanism</b> by which an etiologic agent causes disease is called {{c1::pathogenesis}}", V, A_,
    "Patogênese: como o agente causa a doença", "5", "central", "AnKing só traz a patogênese de doenças específicas.", DEF, "Verde: lâmina 5 e Robbins.",
    extra="- It is the sequence of events from the initial stimulus to the final expression of disease"),
 au("patogenese-mecanismos", "The mechanisms of <b>pathogenesis</b> are {{c1::genetic}} or {{c2::biochemical}}", Z, A_,
    "Mecanismos genéticos e bioquímicos", "5", "central", "sem card nos acervos.", DEF, "Azul: lâmina 5.",
    extra="- A defective gene product is a genetic mechanism<br>- Altered cell and agent interaction is a biochemical mechanism"),
 au("genetica-bioquimica", "A genetic cause may also act through a <b>biochemical</b> mechanism, for example by altering an {{c1::enzyme}}", R, A_,
    "Causa genética com mecanismo bioquímico", "5", "lateral", "sem card nos acervos.", DEF, "Rosa: transcrição."),
 au("farmacos-patogenese", "Many <b>drugs</b> act on the mechanism of disease, that is, on its {{c1::pathogenesis}}, rather than on the etiologic agent", Z, A_,
    "Importância médica da patogênese", "5", "central", "sem card nos acervos.", DEF, "Azul: lâmina 5."),
 sh(1791743347261, "verde", A_, "Febre mediada por IL-1, IL-6 e TNF", "5", "Verde: exemplo da aula (gripe), cartão vivo da Inflamação aguda."),
 au("antibiotico-virus", "<b>Antibiotics</b> do not treat influenza because they do not interfere with viral entry and {{c1::replication}}", Z, A_,
    "Tratar o mecanismo: antibiótico não age em virose", "5", "central", "AnKing não liga antibiótico ao mecanismo da gripe.", DEF, "Azul: transcrição.",
    extra="- Antipyretics and anti-inflammatory drugs act on the inflammatory mechanism instead"),
 au("fibrose-cistica", "Even a known genetic cause, as in <b>cystic fibrosis</b>, is several {{c1::pathogenesis}} steps away from the final lesions", R, A_,
    "Causa conhecida está distante da lesão", "5", "lateral", "sem card nos acervos.", DEF, "Rosa: Robbins, Introdução à Patologia."),
 au("somam-se", "In many diseases, acquired factors such as smoking and diet {{c1::add up}} with <b>genetic</b> effects", R, A_,
    "Fatores adquiridos e genéticos se somam", "6", "lateral", "sem card nos acervos.", DEF, "Rosa: lâmina 6."),
 au("pneumonia-patogenese", "Pneumococcus invades the respiratory epithelium, and the resulting {{c1::inflammatory}} response adds further <b>tissue destruction</b>", Z, A_,
    "Patogênese da pneumonia bacteriana", "3", "central", "AnKing não traz a patogênese da pneumonia.", DEF, "Azul: exemplo da transcrição e das palavras-cruzadas.",
    extra="- Alveoli become destroyed or filled, which impairs respiration"),
 au("pneumonia-niveis", "In pneumonia, reduced blood oxygenation is a functional change, whereas {{c1::dyspnea}} is a <b>clinical manifestation</b>", R, A_,
    "Níveis da doença na pneumonia", "3", "lateral", "sem card nos acervos.", DEF, "Rosa: exemplo da transcrição.",
    extra="- Consolidation on chest radiograph is a morphological change seen on imaging"),
 au("ponte-basicas", "<b>Pathology</b> is the bridge between {{c1::basic sciences}} and clinical medicine", R, A_,
    "Patologia liga ciência básica e clínica", "2", "lateral", "sem card nos acervos.", DEF, "Rosa: Robbins."),
 au("virchow", "{{c1::<b>Rudolf Virchow</b>}}, the father of modern pathology, held that all disease begins with alterations in {{c2::cells}}", R, A_,
    "Virchow", "2", "lateral", "sem card nos acervos.", DEF, "Rosa: Robbins e palavras-cruzadas.",
    extra="- He also systematized the performance and use of autopsy"),

 # ---------- B. Aterosclerose como exemplo de patogênese (lâminas 7) ----------
 ak("ateroma-endotelio", 1471811968814, V, B_, "Disfunção endotelial deixa lipídeos entrarem na íntima", "7", "Verde: HY1, primeira etapa do fluxograma."),
 au("ateroma-hipertensao", "<b>Hypertension</b> damages the endothelium through increased {{c1::shear}} force, favoring atherosclerosis", Z, B_,
    "Hipertensão causa dano endotelial", "7", "central", "AnKing não liga hipertensão ao dano endotelial.", PROC, "Azul: transcrição.",
    extra="- Hyperglycemia also increases lipid uptake by the endothelium"),
 sh(1791147101592, "verde", B_, "LDL oxidado captado por macrófagos", "7", "Verde: etapa do fluxograma, cartão vivo da Patologia ambiental."),
 ak("ateroma-espumosas", 1471811989477, V, B_, "Macrófagos formam células espumosas", "7", "Verde: HY1, lâmina 7."),
 au("ateroma-monocitos", "In <b>atherosclerosis</b>, circulating {{c1::monocytes}} migrate into the intima and become macrophages", Z, B_,
    "Migração de monócitos para a íntima", "7", "central", "AnKing não traz a migração dos monócitos.", PROC, "Azul: lâmina 7."),
 au("ateroma-plaquetas", "Platelet adhesion to the damaged endothelium releases {{c1::PDGF}}, which stimulates proliferation of intimal <b>smooth muscle</b> cells", Z, B_,
    "Adesão plaquetária e PDGF", "7", "central", "AnKing cita PDGF só no Extra.", PROC, "Azul: lâmina 7."),
 ak("ateroma-musculo-liso", 1471811997810, V, B_, "Proliferação do músculo liso e matriz extracelular", "7", "Verde: HY1, etapa do fluxograma."),
 au("ateroma-ciclo", "Activated macrophages release cytokines that activate the {{c1::endothelium}}, increasing <b>LDL</b> uptake in a vicious cycle", Z, B_,
    "Ciclo de ativação endotelial", "7", "central", "sem card nos acervos.", PROC, "Azul: lâmina 7 e transcrição.",
    extra="- This cycle explains why the plaque keeps growing"),
 ak("ateroma-placa", 1471812008532, Z, B_, "Placa fibrosa", "7", "Azul: repete o alvo da proliferação do músculo liso.", hy_repete=True),
 ak("ateroma-def", 1471811875076, Z, B_, "Aterosclerose é acúmulo de colesterol na íntima", "7", "Azul: definição de apoio."),
 au("ateroma-esclerose", "The sclerosis in <b>atherosclerosis</b> refers to {{c1::fibrosis}}, which makes the vessel wall stiffer", R, B_,
    "Esclerose é fibrose", "7", "lateral", "AnKing define só endurecimento.", PROC, "Rosa: transcrição."),
 au("ateroma-farmacos", "Drugs for <b>atherosclerosis</b> can target cholesterol uptake or {{c1::platelet}} adhesion, steps of its pathogenesis", R, B_,
    "Fármacos agem na patogênese", "7", "lateral", "sem card nos acervos.", PROC, "Rosa: transcrição."),

 # ---------- C. Alterações morfológicas e moleculares (lâminas 8 a 10) ----------
 au("morfologicas-secundarias", "<b>Morphological</b> and molecular changes are {{c1::secondary}} to, and result from, pathogenesis", Z, C_,
    "Alterações morfológicas são secundárias", "8", "central", "sem card nos acervos.", DEF, "Azul: lâmina 8."),
 au("macro-imagem", "<b>Imaging</b> exams such as CT or MRI still count as {{c1::macroscopic}} evaluation of the organ", Z, C_,
    "Imagem é avaliação macroscópica", "8", "central", "sem card nos acervos.", DEF, "Azul: transcrição.",
    extra="- Pneumonia appears on chest radiograph as consolidation"),
 au("micro-ultra", "Light microscopy separates nucleus from cytoplasm, whereas <b>electron</b> microscopy shows cell {{c1::ultrastructure}}", Z, C_,
    "Microscopia óptica e ultraestrutura", "8", "central", "sem card nos acervos.", DEF, "Azul: lâmina 8 e transcrição."),
 au("grau-doenca", "<b>Morphological</b> changes define not only the presence but also the {{c1::degree}} of disease", Z, C_,
    "Alterações definem presença e grau", "8", "central", "sem card nos acervos.", DEF, "Azul: lâmina 8.",
    extra="- In chronic hepatitis, the activity grade on biopsy guides treatment"),
 au("primeira-deteccao", "<b>Morphological</b> and molecular changes are usually the {{c1::first}} way a disease is detected", Z, C_,
    "Primeira forma de detecção", "8", "central", "sem card nos acervos.", DEF, "Azul: lâmina 8.",
    extra="- Check-ups look for them in blood tests and imaging"),
 ak("mi-agudo", 1471899328126, V, C_, "Infarto agudo: necrose de coagulação", "9", "Verde: HY2, infarto agudo da lâmina 9."),
 ak("mi-neutrofilos", 1471899339995, R, C_, "Infiltrado neutrofílico de 1 a 3 dias", "9", "Rosa: detalhe de intervalo, o subagudo da aula é de dias.", hy_repete=True),
 ak("mi-amarelo", 1471899362336, V, C_, "Infarto subagudo: palidez amarelada", "9", "Verde: aspecto amarelado do subagudo na lâmina 9."),
 ak("mi-macrofagos", 1471899371687, V, C_, "Infarto subagudo: células inflamatórias", "9", "Verde: HY2, histologia do subagudo."),
 ak("mi-cicatriz-branca", 1471899412796, V, C_, "Infarto cicatrizado: cicatriz branca", "9", "Verde: aspecto do infarto antigo."),
 ak("mi-fibrose", 1471899419610, V, C_, "Infarto cicatrizado: fibrose", "9", "Verde: HY1, histologia do infarto antigo."),
 au("mi-regeneracao", "A healed <b>infarct</b> is replaced by fibrous scar because cardiac muscle cannot {{c1::regenerate}}", V, C_,
    "Miocárdio não regenera: fibrose", "9", "central", "AnKing não liga a falta de regeneração à cicatriz.", MI, "Verde: lâmina 9 e transcrição.",
    extra="- An organ with regenerative capacity could repair the loss with new cells"),
 io("io-mi-agudo", 9, "Acute infarct (hours old)", Z, C_, "Reconhecer o infarto agudo na peça", "Azul: figura da lâmina 9 sem legenda.",
    rects=[M9["agudo"]], mask_rects=[M9["subagudo"], M9["cicatrizado"]]),
 io("io-mi-subagudo", 9, "Subacute infarct (days old)", Z, C_, "Reconhecer o infarto subagudo na peça", "Azul: figura da lâmina 9 sem legenda.",
    rects=[M9["subagudo"]], mask_rects=[M9["agudo"], M9["cicatrizado"]]),
 io("io-mi-cicatrizado", 9, "Healed infarct (weeks to years old)", Z, C_, "Reconhecer o infarto cicatrizado na peça", "Azul: figura da lâmina 9 sem legenda.",
    rects=[M9["cicatrizado"]], mask_rects=[M9["agudo"], M9["subagudo"]]),
 sh(1791054019772, "verde", C_, "Trombo sobre placa obstrui a coronária e causa infarto", "10", "Verde: HY1, lâmina 10, cartão vivo do Grand Round 2."),
 au("ct-trombo", "A coronary <b>thrombus</b> seen at autopsy corresponds to the coronary {{c1::obstruction}} seen on contrast CT", R, C_,
    "Correlação imagem e peça: trombo coronariano", "10", "lateral", "sem card nos acervos.", MI, "Rosa: lâmina 10.",
    extra="- Without blood and oxygen beyond the obstruction, the myocardium dies"),

 # ---------- D. Manifestações clínicas (lâminas 11 e 12) ----------
 au("manifestacoes-def", "The way pathogenesis and morphological changes appear at the bedside is called {{c1::<b>clinical manifestations</b>}}", Z, D_,
    "Manifestações clínicas", "11", "central", "sem card nos acervos.", DEF, "Azul: lâmina 11."),
 au("fisiopatologia", "{{c1::<b>Pathophysiology</b>}} describes how disease alters physiological mechanisms, whereas pathogenesis describes how it develops", Z, D_,
    "Fisiopatologia × patogênese", "11", "central", "sem card nos acervos.", DEF, "Azul: transcrição."),
 ak("rhd-mitral", 1472058738488, R, D_, "Valva mitral é a mais afetada na febre reumática", "12", "Rosa: nó do fluxograma, doença de outra aula.", clinica_lateral=True),
 ak("rhd-estenose", 1472058753870, Z, D_, "Estenose mitral em boca de peixe", "12", "Azul: dupla lesão mitral do fluxograma.", clinica_lateral=True),
 ak("ms-atrio", 1472058992255, Z, D_, "Estenose mitral dilata o átrio esquerdo", "12", "Azul: cadeia do fluxograma.", clinica_lateral=True),
 ak("ms-congestao", 1472058995902, Z, D_, "Pressão atrial esquerda alta causa congestão pulmonar", "12", "Azul: cadeia do fluxograma.", clinica_lateral=True),
 ak("ms-trombo-atrio", 1472059003077, R, D_, "Fibrilação atrial e trombo mural", "12", "Rosa: trombose de átrio esquerdo do fluxograma.", clinica_lateral=True),
 ak("ms-hp", 1472058998627, Z, D_, "Hipertensão pulmonar e insuficiência cardíaca direita", "12", "Azul: câmaras direitas do fluxograma.", clinica_lateral=True),
 sh(1791142464566, "azul", D_, "Insuficiência esquerda causa congestão pulmonar", "12", "Azul: nó do fluxograma, cartão vivo do Edema e congestão."),
 au("dilatacao-estiramento", "Acute chamber dilation activates <b>stretch receptors</b>, which stimulate the cell to add sarcomeres in {{c1::series}}", Z, D_,
    "Dilatação ativa receptores de estiramento", "12", "central", "AnKing traz só o resultado (hipertrofia excêntrica).", [1472078731516, 1471811979298, 1471811989477],
    "Azul: transcrição, cadeia do fluxograma.", extra="- Sarcomeres in series produce a dilated rather than hypertrophic cardiomyopathy"),
 ak("dilatada-excentrica", 1472078731516, Z, D_, "Cardiomiopatia dilatada: hipertrofia excêntrica", "12", "Azul: mecanismo explicado pela professora.", clinica_lateral=True),
 ak("arterias-ateroma", 1471811955341, R, D_, "Artérias mais afetadas pela aterosclerose", "12", "Rosa: aorta, coronárias e cerebrais do fluxograma."),

 # ---------- E. Patologia na assistência (lâminas 13 e 14, palavras-cruzadas, bibliografia) ----------
 au("patologia-geral", "Pathology is divided into {{c1::<b>general</b>}} pathology, which covers the great mechanisms, and organ and system pathology", Z, E_,
    "Patologia geral × de órgãos e sistemas", "13", "central", "sem card nos acervos.", DEF, "Azul: lâmina 13.",
    extra="- General pathology includes cell injury, inflammation and repair, vascular disorders, neoplasia, and environmental, immune and genetic diseases"),
 au("inflamacao-qualquer-orgao", "<b>Inflammation</b> and repair can occur in any organ, so they belong to {{c1::general}} pathology", R, E_,
    "Inflamação e reparo ocorrem em qualquer órgão", "13", "lateral", "sem card nos acervos.", DEF, "Rosa: transcrição."),
 au("autopsia", "{{c1::<b>Autopsy</b>}} gives the pathologist the whole body, with all organs available for a global evaluation", Z, E_,
    "Autópsia", "14", "central", "AnKing cita autópsia só como confirmação de doenças.", PROCED, "Azul: lâmina 14."),
 au("cirurgica", "{{c1::<b>Surgical pathology</b>}} evaluates specimens removed by procedures such as biopsy, gastrectomy or hysterectomy", Z, E_,
    "Patologia cirúrgica", "14", "central", "sem card nos acervos.", PROCED, "Azul: lâmina 14."),
 au("citopatologia", "{{c1::<b>Cytopathology</b>}} evaluates isolated cells, such as those obtained by puncture of a thyroid nodule", Z, E_,
    "Citopatologia", "14", "central", "sem card nos acervos.", PROCED, "Azul: lâmina 14."),
 au("patologia-clinica", "{{c1::<b>Clinical pathology</b>}} is the area that handles laboratory tests", R, E_,
    "Patologia clínica", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: lâmina 14."),
 au("forense", "{{c1::<b>Forensic pathology</b>}} evaluates deaths from external causes", Z, E_,
    "Patologia forense", "14", "central", "sem card nos acervos.", PROCED, "Azul: lâmina 14."),
 au("bastidor", "The pathologist's report goes to the patient's {{c1::physician}}, who communicates the <b>diagnosis</b> to the patient", R, E_,
    "Patologista nos bastidores, interface com outras especialidades", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: lâmina 14."),
 au("autopsia-qualidade", "A main purpose of <b>autopsy</b> is quality control, by comparing clinical and {{c1::pathological}} diagnoses", Z, E_,
    "Autópsia como controle de qualidade", "14", "prova", "sem card nos acervos.", PROCED, "Azul: palavras-cruzadas e apostila de veteranos.",
    extra="- Other uses include epidemiology and the discovery of atypical findings"),
 au("autopsia-discrepancia", "In a São Paulo university hospital, about {{c1::16%}} of autopsies showed a major <b>clinico-pathological</b> discrepancy", R, E_,
    "Discordância clínico-patológica maior", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: bibliografia da aula 1 (Kotovicz 2008)."),
 au("autopsia-erros", "The diagnosis most often missed in clinico-pathological studies is {{c1::pulmonary embolism}}, followed by pneumonia and <b>myocardial infarction</b>", R, E_,
    "Diagnósticos mais perdidos antes da autópsia", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: bibliografia da aula 1 (Kotovicz 2008)."),
 au("autopsia-declinio", "<b>Autopsy</b> rates have fallen from about 50% of deaths in the 1940s to under {{c1::10%}} in the 1990s", R, E_,
    "Queda das taxas de autópsia", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: bibliografias das aulas 1 e 2.",
    extra="- In US hospitals the fall was from about 60% in the 1950s to under 6%"),
 au("autopsia-declinio-causas", "The decline in <b>autopsy</b> is driven by low financial return, workload and {{c1::family}} refusal", R, E_,
    "Causas da queda das autópsias", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: apostila de veteranos.",
    extra="- In Brazil, hospital autopsy stopped being mandatory in 1971"),
 au("autopsia-imagem", "Advances in <b>imaging</b> have led many physicians to wrongly consider {{c1::autopsy}} unnecessary", R, E_,
    "Imagem não torna a autópsia desnecessária", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: palavras-cruzadas."),
 au("monobloco", "In the {{c1::en bloc}} (monobloc) technique, several organs and vascular structures are removed together for dissection at <b>autopsy</b>", R, E_,
    "Retirada em monobloco", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: palavras-cruzadas."),
 au("svoc", "The largest <b>autopsy</b> service in Brazil, with about 14,000 autopsies a year, is the {{c1::SVOC}}", R, E_,
    "Maior serviço de autópsia do Brasil", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: palavras-cruzadas."),
 ak("fna-tireoide", 1462228531057, V, E_, "Biópsia do nódulo de tireoide por punção aspirativa", "14", "Verde: HY2, citopatologia por punção (lâmina 14 e 20)."),
 au("biopsia-def", "A {{c1::<b>biopsy</b>}} is a small fragment of tissue removed for anatomopathological analysis", R, E_,
    "Biópsia", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: palavras-cruzadas."),
 ak("core-biopsia", 1536685206969, R, E_, "Biópsia com agulha grossa (core) em mama", "14", "Rosa: palavras-cruzadas (core em fígado e mama).",
    extra_add="- Core needle biopsy is widely used in liver and breast"),
 au("congelacao", "The intraoperative pathology exam is known as {{c1::<b>frozen section</b>}}", R, E_,
    "Exame de congelação", "14", "lateral", "sem card nos acervos.", PROCED, "Rosa: palavras-cruzadas."),
 ak("pap-raspagem", 1463106055950, R, E_, "Papanicolaou: raspagem da zona de transformação", "21", "Rosa: palavras-cruzadas e prova 2016 P3 (citologia de colo).", clinica_lateral=True),
 au("puncao-guiada", "<b>Ultrasound</b> guides the needle during {{c1::fine-needle aspiration}} of a thyroid nodule, an interface of pathology and radiology", Z, E_,
    "Punção guiada por imagem", "20", "central", "AnKing cita a punção sem a interação com a imagem.", PROCED, "Azul: lâmina 20."),

 # ---------- F. Macroscopia e processamento (lâminas 16 a 22) ----------
 au("macro-fresco", "<b>Macroscopic</b> examination is done on fresh specimens or on specimens fixed in {{c1::formalin}}", Z, F_,
    "Macroscopia a fresco ou fixada", "16", "central", "sem card nos acervos.", PROCED, "Azul: lâmina 16.",
    extra="- Formalin is also the fixative used for H&E"),
 au("macro-etapas", "During <b>macroscopy</b> the specimen is weighed, measured and {{c1::cut}} to identify lesions, which are then photographed", R, F_,
    "Pesar, medir, cortar, fotografar", "16", "lateral", "sem card nos acervos.", PROCED, "Rosa: lâmina 16."),
 au("representacao", "<b>Histological representation</b> means sampling the {{c1::lesion}} for slides, because sectioning the whole organ is unfeasible", Z, F_,
    "Representação histológica", "16", "central", "sem card nos acervos.", PROCED, "Azul: lâmina 16 e transcrição."),
 au("cassete", "The sampled fragment is placed in a {{c1::cassette}} that becomes a <b>paraffin block</b>", R, F_,
    "Fragmento em cassete", "18", "lateral", "sem card nos acervos.", PROCED, "Rosa: lâmina 18."),
 au("processador", "A <b>tissue processor</b> infiltrates the tissue with {{c1::paraffin}} overnight, producing small blocks", Z, F_,
    "Processador de tecidos", "18", "central", "sem card nos acervos.", PROCED, "Azul: lâminas 18 e 19."),
 au("microtomo", "Paraffin blocks are sliced with a {{c1::microtome}} and the sections are placed on <b>slides</b>", Z, F_,
    "Micrótomo e lâminas", "19", "central", "sem card nos acervos.", PROCED, "Azul: lâmina 19."),
 au("citologia-esfregaco", "In <b>cytology</b>, the aspirated material is smeared on the slide as a {{c1::monolayer}} to avoid overlap of cells", Z, F_,
    "Esfregaço em monocamada", "21", "central", "sem card nos acervos.", PROCED, "Azul: lâmina 21."),
 au("olho-cerebro", "The two fundamental tools of pathological diagnosis are the eye and the {{c1::<b>brain</b>}}", R, F_,
    "Olho e cérebro", "22", "lateral", "sem card nos acervos.", PROCED, "Rosa: lâmina 22."),

 # ---------- G. Ferramentas (lâminas 15 e 23 a 31) ----------
 au("complementares", "<b>Special stains</b>, immunohistochemistry and molecular tests are {{c1::complementary}} to H&E", Z, G_,
    "Ferramentas complementares", "15", "central", "sem card nos acervos.", IHQ, "Azul: lâmina 15."),
 au("histoquimica-def", "<b>Histochemistry</b> uses dyes with chemical {{c1::affinity}} for a specific component of the tissue", Z, G_,
    "Histoquímica", "15", "central", "sem card nos acervos.", IHQ, "Azul: lâmina 15 e transcrição."),
 au("ihq-vs-histo", "<b>Immunohistochemistry</b> uses {{c1::antibodies}} where histochemistry relies on chemical affinity between dye and component", Z, G_,
    "Imuno-histoquímica × histoquímica", "15", "central", "sem card nos acervos.", IHQ, "Azul: lâmina 15 e transcrição."),
 au("molecular-def", "<b>Molecular pathology</b> identifies mutations or mutated proteins and supports {{c1::targeted}} therapy", Z, G_,
    "Patologia molecular", "15", "central", "sem card nos acervos.", IHQ, "Azul: lâmina 15 e prova 2015 P3."),
 au("he-primeiro", "<b>H&E</b> is always performed first, because tissue morphology must be known before {{c1::special}} tests", Z, G_,
    "HE sempre é feita primeiro", "23", "central", "sem card nos acervos.", IHQ, "Azul: transcrição."),
 au("he-cores", "In <b>H&E</b>, hematoxylin stains nuclei blue-purple and eosin stains the {{c1::cytoplasm}} pink", V, G_,
    "Cores da HE", "23", "central", "AnKing não traz a HE.", IHQ, "Verde: lâmina 23, base da histopatologia."),
 au("he-principal", "<b>H&E</b> is the main stain because it is fast and shows {{c1::morphological patterns}}", Z, G_,
    "HE: principal método", "23", "central", "sem card nos acervos.", IHQ, "Azul: lâmina 23."),
 au("me-selecao", "<b>Electron microscopy</b> needs prior {{c1::selection}} of the specimen and is used only for specific diseases", Z, G_,
    "Microscopia eletrônica: seleção prévia", "24", "central", "sem card nos acervos.", CIL, "Azul: lâmina 24.",
    extra="- Few centers offer it"),
 au("me-fixador", "Tissue for electron microscopy is fixed in {{c1::glutaraldehyde}} instead of the formalin used for <b>H&E</b>", Z, G_,
    "Fixador da microscopia eletrônica", "24", "central", "sem card nos acervos.", CIL, "Azul: transcrição."),
 au("discinesia", "<b>Primary ciliary dyskinesia</b> is invisible on H&E but shows {{c1::microtubule}} defects on electron microscopy", Z, G_,
    "Discinesia ciliar vista na microscopia eletrônica", "24", "central", "AnKing traz a síndrome, não o diagnóstico por microscopia.", CIL, "Azul: lâmina 24.",
    extra="- The cilium is present but does not work properly"),
 ak("kartagener", 1468250126050, {1: V, 2: V, 3: R}, G_, "Síndrome de Kartagener: braço de dineína", "24", "Verde: HY1, doença da lâmina 24."),
 au("masson", "In <b>Masson</b> trichrome, collagen stains {{c1::blue}}, making it a good stain to evaluate fibrosis", Z, G_,
    "Tricrômico de Masson", "25", "central", "AnKing não traz o tricrômico.", COR, "Azul: lâmina 25."),
 au("picrosirius", "<b>Picro-Sirius</b> stains collagen red and becomes bright under {{c1::polarized}} light", Z, G_,
    "Picro-Sirius", "25", "central", "sem card nos acervos.", COR, "Azul: lâmina 25."),
 au("elastica", "{{c1::Verhoeff}} and resorcin-fuchsin stains show <b>elastic fibers</b>", Z, G_,
    "Coloração de fibra elástica", "25", "central", "sem card nos acervos.", COR, "Azul: lâmina 25.",
    extra="- Useful for the elastic laminae of vessels and for emphysema"),
 au("membrana-basal", "The <b>basement membrane</b> is highlighted by {{c1::PAS}}", Z, G_,
    "Membrana basal pelo PAS", "25", "central", "AnKing traz PAS só para glicogênio.", COR, "Azul: lâmina 25."),
 au("bh", "<b>Brown-Hopps</b> (BH) is the Gram stain for tissue and identifies {{c1::bacteria}} in sections", Z, G_,
    "BH, Gram da histologia", "26", "central", "sem card nos acervos.", COR, "Azul: lâmina 26."),
 ak("prata", 1500419514988, V, G_, "Prata metenamina cora fungos", "26", "Verde: HY2, Grocott para fungos."),
 sh(1791576674292, "verde", G_, "Ziehl-Neelsen para micobactérias", "26", "Verde: BAAR da lâmina 26, cartão vivo de Morfologia."),
 ak("zn-usos", 1500419413812, Z, G_, "Ziehl-Neelsen em micobactérias e Nocardia", "26", "Azul: repete o alvo do cartão vivo e traz a imagem.", hy_repete=True),
 au("muco", "<b>Mucus</b> is demonstrated by PAS and {{c1::Alcian blue}} stains", Z, G_,
    "Muco: PAS e Alcian blue", "27", "central", "AnKing cita mucicarmina, não Alcian blue.", COR, "Azul: lâmina 27."),
 ak("oil-red", 1475982852075, Z, G_, "Oil red O cora lipídeos", "27", "Azul: gordura da lâmina 27."),
 ak("perls", 1478834342914, Z, G_, "Azul da Prússia para ferro", "27", "Azul: ferro (Perls) da lâmina 27."),
 ak("pas-glicogenio", 1475982859127, V, G_, "PAS cora glicogênio", "27", "Verde: HY1, glicogênio × gordura no hepatócito."),
 ak("hemossiderina", 1486590976651, R, G_, "Hemossiderina na hemocromatose", "27", "Rosa: depósito de ferro no fígado citado pela professora.", clinica_lateral=True),
 au("melanina", "{{c1::Fontana-Masson}} stain demonstrates <b>melanin</b>", Z, G_,
    "Fontana-Masson para melanina", "27", "central", "sem card nos acervos.", COR, "Azul: lâmina 27."),
 au("ihq-24h", "<b>Immunohistochemistry</b> adds at least {{c1::24 hours}} to the time of the report", Z, G_,
    "Imuno-histoquímica acrescenta 24 horas ao laudo", "28", "central", "sem card nos acervos.", IHQ, "Azul: lâmina 28."),
 au("ihq-in-situ", "<b>Immunohistochemistry</b> identifies proteins {{c1::in situ}}, preserving where they are in the tissue", V, G_,
    "Imuno-histoquímica identifica proteínas in situ", "28", "central", "AnKing não define o método.", IHQ, "Verde: lâmina 28."),
 ak("ihq-tumores", 1496165181235, Z, G_, "IHQ caracteriza tumores difíceis de classificar", "28", "Azul: lâmina 15 e 28, tipo e origem do câncer."),
 au("ihq-passos", "The <b>primary antibody</b> binds the target protein and a labeled {{c1::secondary}} antibody then binds the primary antibody", Z, G_,
    "Anticorpos primário e secundário", "28", "central", "AnKing não traz o método indireto.", IHQ, "Azul: lâmina 28.",
    extra="- The label produces a visible color where the protein is"),
 au("ihq-secundario", "The <b>secondary antibody</b> binds the constant {{c1::Fc}} region of the primary, so a single secondary works for any target", Z, G_,
    "Anticorpo secundário reconhece o Fc", "28", "central", "sem card nos acervos.", IHQ, "Azul: transcrição.",
    extra="- Producing one secondary in large scale is cheaper than labeling every primary"),
 au("ihq-lavagem", "Washes between antibody steps leave only {{c1::high-affinity}} binding in <b>immunohistochemistry</b>", R, G_,
    "Lavagens deixam só ligações de alta afinidade", "28", "lateral", "sem card nos acervos.", IHQ, "Rosa: transcrição."),
 au("dab", "The most common chromogen in <b>immunohistochemistry</b> is {{c1::DAB}}, which stains brown", R, G_,
    "DAB, cromógeno marrom", "28", "lateral", "AnKing não traz o cromógeno.", IHQ, "Rosa: transcrição e lâmina 28."),
 io("io-ihq-primario", 28, "Primary antibody", Z, G_, "Reconhecer o anticorpo primário no esquema", "Azul: esquema da lâmina 28.",
    rects=[M28["primario"]], mask_rects=[v for k, v in M28.items() if k != "primario"]),
 io("io-ihq-secundario", 28, "Labeled secondary antibody", Z, G_, "Reconhecer o anticorpo secundário marcado no esquema", "Azul: esquema da lâmina 28.",
    rects=[M28["secundario"]], mask_rects=[v for k, v in M28.items() if k != "secundario"]),
 io("io-ihq-proteina", 28, "Target protein", Z, G_, "Reconhecer a proteína-alvo no esquema", "Azul: esquema da lâmina 28.",
    rects=[M28["proteina"]], mask_rects=[v for k, v in M28.items() if k != "proteina"]),
 io("io-ihq-produto", 28, "Colored product", Z, G_, "Reconhecer o produto colorido no esquema", "Azul: esquema da lâmina 28.",
    rects=[M28["produto"]], mask_rects=[v for k, v in M28.items() if k != "produto"]),
 ak("ihq-citoqueratina", 1496165216576, V, G_, "Citoqueratina marca tumores epiteliais", "29", "Verde: HY2, IHQ para tipo de tumor."),
 ak("ihq-psa", 1496165396128, V, G_, "PSA marca câncer de próstata", "29", "Verde: HY2, exemplo da professora.",
    extra_add="- It helps tell a metastasis from a second primary tumor"),
 ak("ihq-er", 1463442982359, Z, G_, "Receptor de estrógeno: marcação nuclear", "29", "Azul: padrão nuclear."),
 ak("ihq-her2", 1463443025598, Z, G_, "HER2: marcação de membrana", "29", "Azul: padrão de membrana."),
 ak("ihq-er-mama", 1496165443492, Z, G_, "IHQ para receptor de estrógeno identifica tumor de mama", "29", "Azul: repete o alvo do receptor de estrógeno.", hy_repete=True),
 au("ihq-padrao", "<b>Membrane</b> staining suggests a growth factor {{c1::receptor}}, whereas nuclear staining suggests a transcription factor", Z, G_,
    "Padrão de coloração e localização", "29", "central", "AnKing mostra os padrões em cards separados.", IHQ, "Azul: lâmina 29."),
 au("ihq-origem", "<b>Immunohistochemistry</b> helps define the {{c1::origin}} of a tumor, since cells of different organs express different proteins", Z, G_,
    "Tipo e origem do câncer", "29", "central", "AnKing traz marcadores isolados.", IHQ, "Azul: lâmina 15 e transcrição."),
 au("if-def", "<b>Immunofluorescence</b> uses a {{c1::fluorescent}} revealer and is viewed in a fluorescence microscope", Z, G_,
    "Imunofluorescência", "30", "central", "sem card nos acervos.", IHQ, "Azul: lâmina 30."),
 au("if-fundo", "In <b>immunofluorescence</b> the background is {{c1::dark}}, so the pathologist must know what is being observed", R, G_,
    "Fundo escuro da imunofluorescência", "30", "lateral", "sem card nos acervos.", IHQ, "Rosa: transcrição."),
 au("if-multiplex", "<b>Immunofluorescence</b> allows several markers at once, revealed in {{c1::different colors}}", Z, G_,
    "Múltiplos marcadores", "30", "central", "sem card nos acervos.", IHQ, "Azul: transcrição."),
 au("if-renal", "<b>Immunofluorescence</b> is widely used in {{c1::renal}} diseases", Z, G_,
    "Imunofluorescência em doenças renais", "30", "central", "AnKing traz os padrões renais, não o uso do método.", IHQ, "Azul: transcrição e palavras-cruzadas."),
 ak("if-linear", 1475376552582, R, G_, "Goodpasture: padrão linear na imunofluorescência", "30", "Rosa: exemplo renal citado pela professora.", clinica_lateral=True),
 ak("if-granular", 1475376486636, R, G_, "Glomerulonefrite pós-estreptocócica: padrão granular", "30", "Rosa: exemplo renal citado pela professora.", clinica_lateral=True),
 au("ish-def", "In <b>in situ hybridization</b>, a labeled {{c1::complementary}} DNA probe lights up where it binds the target sequence", Z, G_,
    "Hibridização in situ", "31", "central", "AnKing traz o FISH, não o princípio geral.", [1468605672126, 1468605422972, 1468549288868], "Azul: lâmina 31 e transcrição."),
 ak("fish", 1468605672126, V, G_, "FISH: sonda fluorescente liga um gene", "31", "Verde: HY2, hibridização in situ."),
 au("ish-copias", "<b>In situ hybridization</b> can show multiple {{c1::copies}} of a gene, guiding specific tumor therapy", Z, G_,
    "Cópias gênicas guiam terapia", "31", "central", "sem card nos acervos.", [1468605672126, 1468605422972, 1463442924234], "Azul: transcrição."),
 ak("pcr", 1468605422972, V, G_, "PCR amplifica um fragmento de DNA", "31", "Verde: HY2, teste molecular da lâmina 31."),
 ak("western", 1468549288868, Z, G_, "Western blot usa anticorpo marcado", "31", "Azul: Western blot da lâmina 15."),
 au("terapia-alvo", "<b>Targeted therapy</b> is worthwhile only when the tumor {{c1::overexpresses}} the target receptor", Z, G_,
    "Terapia-alvo exige hiperexpressão", "31", "central", "AnKing traz drogas, não o critério.", [1495735525371, 1463442924234, 1468605672126], "Azul: transcrição.",
    extra="- Molecular characterization shows whether the receptor drives the tumor"),
 ak("her2-trastuzumab", 1495735525371, R, G_, "Trastuzumabe liga HER2", "31", "Rosa: exemplo clássico de receptor de fator de crescimento alvo.", clinica_lateral=True),
 ak("er-pr-her2", 1463442924234, Z, G_, "Receptores que predizem resposta no câncer de mama", "31", "Azul: prova 2018 P4, aula de câncer de mama.", clinica_lateral=True),
 au("hormonioterapia", "A tumor that expresses {{c1::estrogen}} and progesterone receptors can be treated with <b>hormone therapy</b>", Z, G_,
    "Receptores hormonais e terapia hormonal", "31", "prova", "AnKing traz o tamoxifeno em outros contextos.", [1463442924234, 1463442982359, 1496165443492], "Azul: prova 2015 P3sub 2.2."),
 au("mama-molecular", "Morphologically similar <b>breast cancers</b> can differ in prognosis and therapy response, which {{c1::molecular}} analysis reveals", R, G_,
    "Cânceres semelhantes diferem na análise molecular", "31", "lateral", "sem card nos acervos.", [1463442924234, 1463442982359, 1463443025598], "Rosa: Robbins."),
 au("translocacao-alvo", "Confirming a specific {{c1::translocation}} in tumor cells guides targeted therapy in some <b>lymphomas</b>", R, G_,
    "Translocação confirmada guia terapia", "31", "lateral", "sem card nos acervos.", [1468605672126, 1463442924234, 1495735525371], "Rosa: transcrição."),
]

# Linha curta no verso dos cards que chegavam sem explicação; AnKing preservado (extra_add), autoral em extra.
VERSO = {
 "ponte-basicas": "- It explains the causes of signs and symptoms and gives a rational basis for therapy",
 "patologia-vs-doenca": "- A disease may be called a pathological entity",
 "etiologia-grupos": "- Genetic causes are inherited or arise in development<br>- Acquired causes come from interaction with the environment",
 "genetica-def": "- It may come from the parents' gametes or arise as a new mutation",
 "pneumonia-etiologias": "- Same disease, different etiologic agents",
 "nem-todo-agente": "- A fright raises heart rate, but adaptation restores balance without consequences",
 "genetica-bioquimica": "- Genetic and biochemical mechanisms do not correspond one to one",
 "farmacos-patogenese": "- Knowing the mechanism makes treatment logical instead of memorized",
 "fibrose-cistica": "- The mutated gene and its product are only the first steps toward cysts and fibrosis",
 "somam-se": "- Smoking and an industrialized diet are acquired factors",
 "ateroma-endotelio": "- Damage can be primary or secondary, as in hypertension or diabetes",
 "ateroma-monocitos": "- Inside the intima they take up oxidized lipids",
 "ateroma-plaquetas": "- Myointimal proliferation then adds collagen synthesis",
 "ateroma-placa": "- The plaque has a lipid core and a fibrous cap",
 "ateroma-def": "- It affects the intima of large and medium arteries",
 "ateroma-esclerose": "- Atherosclerosis is fat accumulation plus fibrosis",
 "ateroma-farmacos": "- Antiplatelet and cholesterol-lowering drugs act at these steps",
 "morfologicas-secundarias": "- The pathogenesis itself runs silently, without visible change",
 "micro-ultra": "- Under light microscopy the ultrastructure inside cells is not resolved",
 "mi-neutrofilos": "- Inflammatory cells arrive after the muscle cells die",
 "mi-amarelo": "- The yellow color reflects the associated inflammation",
 "mi-cicatriz-branca": "- The white color is fibrous replacement of dead muscle",
 "mi-fibrose": "- Fibrosis replaces the dead muscle cells",
 "manifestacoes-def": "- Examples are dyspnea and abnormal lung sounds in pneumonia",
 "fisiopatologia": "- In practice the two terms are used almost as synonyms",
 "ms-atrio": "- Blood backs up behind the stenotic valve",
 "ms-congestao": "- Pulmonary congestion follows the rise in pressure behind the left atrium",
 "dilatada-excentrica": "- Acute dilation activates stretch receptors that add contractile filaments in series",
 "inflamacao-qualquer-orgao": "- Organ and system pathology builds on these general mechanisms",
 "autopsia": "- A global evaluation of all organs is its main advantage",
 "cirurgica": "- A skin lesion removed to exclude melanoma is an example",
 "citopatologia": "- It answers whether the process is inflammatory, neoplastic, benign or malignant",
 "patologia-clinica": "- In Brazil it has its own residency, separate from anatomic pathology",
 "forense": "- It is usually practiced in the medical-legal institute",
 "bastidor": "- The pathologist works behind the scenes, in contact with other physicians",
 "autopsia-discrepancia": "- Major discrepancy rates in general hospitals range from 11% to 48%",
 "autopsia-erros": "- Massive pulmonary embolism is often not suspected clinically",
 "autopsia-imagem": "- Autopsy still corrects the presumed cause of death",
 "monobloco": "- It allows dissection of organs together with their vessels",
 "svoc": "- It is the death verification service of the capital",
 "biopsia-def": "- Examples are core, excisional and punch biopsies",
 "congelacao": "- It guides the surgeon while the patient is still in the operating room",
 "complementares": "- H&E comes first, and the other tools answer specific questions",
 "histoquimica-def": "- Examples are Ziehl for mycobacteria, Masson for collagen and PAS for glycogen",
 "ihq-vs-histo": "- A labeled antibody finds one specific protein",
 "molecular-def": "- Techniques include PCR and Western blot",
 "macro-etapas": "- Photographs document the lesion before sampling",
 "representacao": "- The pathologist samples where the lesion is",
 "cassete": "- Cassettes go to the tissue processor",
 "processador": "- The process runs overnight",
 "microtomo": "- The procedure is the same as in histology",
 "puncao-guiada": "- The aspirate is smeared on a slide and examined under the microscope",
 "citologia-esfregaco": "- The smear is then stained and viewed under the microscope",
 "olho-cerebro": "- Observation and interpretation need each other",
 "he-primeiro": "- Special stains are chosen after seeing the H&E pattern",
 "he-cores": "- It is called the world in purple and pink",
 "he-principal": "- It also distinguishes nucleus from cytoplasm",
 "me-fixador": "- That is why electron microscopy has to be planned before fixing",
 "masson": "- Blue areas are collagen, so fibrosis",
 "picrosirius": "- Polarized light makes collagen birefringent and bright",
 "membrana-basal": "- The glomerulus is a classic example",
 "bh": "- It is the histology counterpart of the Gram stain",
 "prata": "- Grocott shows fungal hyphae",
 "muco": "- PAS also stains glycogen",
 "perls": "- Iron deposits appear blue in hemosiderosis and hemochromatosis",
 "melanina": "- Melanin granules appear black",
 "ihq-24h": "- Specificity costs report time",
 "ihq-in-situ": "- Where the protein stains matters as much as whether it stains",
 "ihq-lavagem": "- Unbound antibody is washed away",
 "dab": "- Other chromogen colors, such as red or green, are possible",
 "ihq-er": "- Staining location tells the type of protein",
 "ihq-her2": "- Membrane staining suggests a receptor",
 "ihq-er-mama": "- The marker also predicts response to hormone therapy",
 "ihq-padrao": "- Staining location tells where the protein works",
 "ihq-origem": "- A PSA-positive adenocarcinoma suggests prostate origin",
 "if-def": "- Same principle as immunohistochemistry, with a fluorescent label",
 "if-fundo": "- Immunohistochemistry usually shows the counterstained background",
 "if-multiplex": "- Multiplex labeling is easier here than in immunohistochemistry",
 "if-renal": "- Skin is another common use",
 "if-linear": "- Renal biopsies are routinely studied by immunofluorescence",
 "ish-def": "- The principle is the same: bind, wash, and the labeled probe reveals the alteration",
 "fish": "- It can be done on interphase nuclei in tissue",
 "ish-copias": "- It can also show expression of a specific gene",
 "hormonioterapia": "- Hormone therapy blocks the stimulus the tumor takes from the patient's own hormones",
 "mama-molecular": "- Hormone receptors and HER2 guide treatment",
 "translocacao-alvo": "- The search is done in the neoplastic cells",
}
DUPLICACAO = {
 "ateroma-esclerose": "ganho: etimologia de esclerose (fibrose) na aterosclerose, distinta da histologia da cicatriz do infarto",
 "morfologicas-secundarias": "ganho: relação alterações morfológicas ← patogênese, distinta da definição de anticorpo secundário",
 "ihq-passos": "ganho: ordem dos anticorpos no método indireto, distinta do card do Fc",
 "ihq-padrao": "ganho: interpretar localização da marcação (membrana × núcleo), distinta dos cards de ER e HER2",
 "hormonioterapia": "ganho: consequência terapêutica da expressão de receptor (prova 2015), distinta da localização nuclear do ER",
}
# figuras recortadas da lâmina 25 (professora); o verso mostra o resultado da coloração
IMGS = {"masson": "masson", "picrosirius": "picrosirius", "elastica": "elastica", "membrana-basal": "pas-membrana"}
VERSO["elastica"] = None
for c in CARDS:
    k = c["key"]
    if k in IMGS:
        name = f"nebli-pt03-{IMGS[k]}.png"
        MEDIA[name] = f"img/{name}"
        tag = f'<img src="{name}">'
        base = c["extra"] if c["kind"] == "autoral" else ""
        line = VERSO.get(k)
        c["extra"] = "<br>".join(x for x in (base, line, tag) if x)
        c["slide_sem_alternativa"] = "recorte da lâmina 25: nenhum card do AnKing ou externo mostra este corante, e o livro não ilustra a coloração"
        continue
    if k in VERSO and VERSO[k]:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = (c.get("extra_add", "") + "<br>" if c.get("extra_add") else "") + VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
    if c["kind"] in ("text", "autoral") and not any("<img" in str(c.get(f, "")) for f in ("text", "extra", "extra_add")) and not c.get("src"):
        c.setdefault("sem_imagem", "conceito, definição ou etapa de processo sem estrutura a reconhecer; figura não isola o alvo" if k not in ("muco", "melanina", "bh") else "sem figura inequívoca do corante nos acervos nem na lâmina (mapeamento imagem-corante incerto)")

SEM_IMG_ANK = "a figura do acervo é ilustração mnemônica de outro recurso, que não mostra o alvo; mecanismo sem estrutura a reconhecer"
for c in CARDS:
    if c["kind"] == "text" and c["key"] in ['ms-atrio', 'ms-congestao', 'ms-trombo-atrio', 'ms-hp', 'ihq-citoqueratina', 'western']:
        c.setdefault("sem_imagem", SEM_IMG_ANK)


# ---- escopo da aula (F-20261012-CLAUDE-01): introdução da Patologia = conceitos, áreas e ferramentas; exemplos (aterosclerose,
# infarto, estenose mitral, pneumonia, estatísticas de autópsia, marcadores tumorais, glomerulonefrites) saem — têm aula própria ou
# são ilustração (nebli.retira, lista em retirar-escopo.txt) ----
_RETIRAR = set(open(__import__("pathlib").Path(__file__).with_name("retirar-escopo.txt")).read().split())
_SH_FORA = {1791743347261, 1791147101592, 1791054019772, 1791142464566}
CARDS[:] = [c for c in CARDS if c["key"] not in _RETIRAR and not (c["kind"] == "compartilhado" and c["nid"] in _SH_FORA)]
def _cc(key):
    return next(c for c in CARDS if c["key"] == key)
for _k in ("prata", "ihq-citoqueratina"):
    _cc(_k)["flags"] = {n: Z for n in _cc(_k)["flags"]}; _cc(_k)["clinica_lateral"] = True  # exemplo de coloração/marcador na introdução

# Revisão pontual Codex 12/10/2026 — evidência em revisao-pontual-claude-2026-10-12
_AJUSTES_CODEX_1210 = {'etiologia-multipla': {'fields_override': {'Extra': '- Genetic susceptibility and environmental exposures can '
                                                     'contribute together to a disease.'},
                        'motivo': 'Evita misturar mecanismos de formas diferentes de diabetes no mesmo exemplo.'},
 'fna-tireoide': {'fields_override': {'Text': 'Which sampling method obtains <b>isolated cells</b> from a thyroid '
                                              'nodule? {{c1::Fine-needle aspiration (FNA)}}',
                                      'Extra': '- The aspirate supports cytological evaluation.<br>- A tissue '
                                               'biopsy also preserves architecture, which isolated cells cannot '
                                               'fully show.'},
                  'motivo': 'Recupera a ferramenta/citologia, não um algoritmo clínico de todo nódulo; retira '
                            'must do because highly vascularized.',
                  'metadata': {'sem_imagem': 'Recuperação do método que obtém células; fluxograma herdado traz '
                                             'algoritmo de conduta de nódulo tireoidiano alheio ao objetivo e foi '
                                             'excluído após inspeção visual.'},
                  'flags': {1: 4},
                  'clinica_lateral': True},
 'he-primeiro': {'fields_override': {'Text': 'Routine <b>H&E</b> provides the morphological context for choosing '
                                             '{{c1::ancillary tests}}',
                                     'Extra': '- H&E shows the overall tissue pattern.<br>- Additional methods '
                                              'answer a more specific diagnostic question.'},
                 'motivo': 'Remove always e torna explícita a função organizadora do H&E; lâminas 15/23.; '
                           'Focaliza a relação morfologia → testes complementares, sem expressão longa na cloze.'},
 'terapia-alvo': {'fields_override': {'Text': 'Selection of a <b>targeted cancer therapy</b> depends on '
                                              'identifying a suitable {{c1::molecular target}} in the tumor',
                                      'Extra': '- A relevant biomarker may involve protein expression or a '
                                               'genetic alteration.<br>- Receptor overexpression is one example, '
                                               'not a universal requirement.'},
                  'motivo': 'Corrige only overexpresses para o princípio geral de seleção por alvo; NCI Biomarker '
                            'Testing.'},
 'oil-red': {'fields_override': {'Extra': '- Lipid stains answer a specific compositional question that routine '
                                          'morphology may not resolve.<br><img '
                                          'src="143ca9b446258c89d24154845b37ea0f.jpg" height="250">'},
             'motivo': 'Retira comparação McArdle/MCAD alheia ao objetivo introdutório.; Conserva a micrografia '
                       'de lipídios relevante; exclui a tabela de doenças metabólicas e a comparação clínica.'},
 'pas-glicogenio': {'fields_override': {'Extra': '- PAS highlights carbohydrate-rich structures; interpret the '
                                                 'staining pattern in its tissue context.'},
                    'motivo': 'Retira comparação de doenças metabólicas usada como expansão lateral.',
                    'metadata': {'sem_imagem': 'Alvo é a afinidade do corante. Imagens herdadas incluem tabela '
                                               'completa de glicogenoses e micrografia sem confirmação específica '
                                               'de PAS/glicogênio; não usar imagem ambígua como comprovação '
                                               'visual.'}},
 'pneumonia-patogenese': {'fields_override': {},
                          'motivo': 'Detalhe ou aplicação específica; não substitui recuperação do princípio da '
                                    'ferramenta. Harmoniza com a revisão de escopo.',
                          'flags': {1: 5}},
 'picrosirius': {'fields_override': {},
                 'motivo': 'Detalhe ou aplicação específica; não substitui recuperação do princípio da '
                           'ferramenta. Harmoniza com a revisão de escopo.',
                 'flags': {1: 5}},
 'elastica': {'fields_override': {},
              'motivo': 'Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. '
                        'Harmoniza com a revisão de escopo.',
              'flags': {1: 5}},
 'bh': {'fields_override': {},
        'motivo': 'Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. '
                  'Harmoniza com a revisão de escopo.',
        'flags': {1: 5}},
 'melanina': {'fields_override': {},
              'motivo': 'Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. '
                        'Harmoniza com a revisão de escopo.',
              'flags': {1: 5}},
 'ihq-24h': {'fields_override': {},
             'motivo': 'Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. '
                       'Harmoniza com a revisão de escopo.',
             'flags': {1: 5}},
 'hormonioterapia': {'fields_override': {},
                     'motivo': 'Detalhe ou aplicação específica; não substitui recuperação do princípio da '
                               'ferramenta. Harmoniza com a revisão de escopo.',
                     'flags': {1: 5}},
 'biopsia-def': {'fields_override': {},
                 'motivo': 'Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, '
                           'antes das listas de corantes.',
                 'flags': {1: 3}},
 'histoquimica-def': {'fields_override': {},
                      'motivo': 'Conceito organizador duradouro das ferramentas diagnósticas explicitamente '
                                'ensinado, antes das listas de corantes.',
                      'flags': {1: 3}},
 'ihq-vs-histo': {'fields_override': {},
                  'motivo': 'Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, '
                            'antes das listas de corantes.',
                  'flags': {1: 3}},
 'he-principal': {'fields_override': {},
                  'motivo': 'Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, '
                            'antes das listas de corantes.',
                  'flags': {1: 3}},
 'puncao-guiada': {'fields_override': {'Text': 'During <b>fine-needle aspiration</b>, {{c1::ultrasound}} helps '
                                               'guide the needle into the lesion'},
                   'motivo': 'Recupera a função do guia de imagem; o card FNA recupera o método de amostragem, '
                             'evitando duas perguntas pela mesma resposta.'}}
for _c in CARDS:
    if _c["key"] in _AJUSTES_CODEX_1210:
        _fix = _AJUSTES_CODEX_1210[_c["key"]]
        _c.setdefault("fields_override", {}).update(_fix["fields_override"])
        _c["motivo"] = _fix["motivo"]
        if "flags" in _fix: _c["flags"] = _fix["flags"]
        if _fix.get("clinica_lateral"): _c["clinica_lateral"] = True
        if _fix.get("metadata"): _c.update(_fix["metadata"])


# Análise do deck-prova 2026-10-13 (F-20261013-CLAUDE-03): cards tirados desta aula, com motivo.
RETIRADOS_ANALISE = {
 "pneumonia-patogenese": "exemplo",
 "autopsia-discrepancia": "detalhe-numerico",
 "autopsia-erros": "clinica",
 "autopsia-declinio": "detalhe-numerico",
 "autopsia-declinio-causas": "detalhe",
 "autopsia-imagem": "detalhe",
 "monobloco": "detalhe-tecnico",
 "svoc": "detalhe",
 "fna-tireoide": "repetido",
 "core-biopsia": "clinica",
 "macro-etapas": "detalhe",
 "cassete": "detalhe",
 "puncao-guiada": "detalhe",
 "olho-cerebro": "detalhe",
 "picrosirius": "detalhe",
 "bh": "detalhe",
 "zn-usos": "repetido",
 "melanina": "detalhe",
 "ihq-24h": "detalhe-numerico",
 "if-fundo": "detalhe",
 "ish-copias": "clinica",
}
CARDS = [c for c in CARDS if c['key'] not in RETIRADOS_ANALISE]

# Linha de verso para o card AnKing devolvido sem Extra (análise 13/10).
for c in CARDS:
    if c["key"] == "pap-raspagem" and not c.get("extra_add"):
        c["extra_add"] = "- The scraped cells are stained and screened for dysplasia, a cytopathology exam"
