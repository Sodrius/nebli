# Especificação curada — Reconhecimento pelo sistema imune inato (UC03 P1, Imunologia; Prof. José Alexandre Barbuto; 23 lâminas = parte III da turma).
# Inflamação (pt38, IM31, pt61) já tem PRR, TLR, inflamassoma, IFN tipo I e NK: entram por sh() só notas de corridas entregues; notas exclusivas da IM37 (Codex, em andamento) ficam de fora.
RUN_ID = "uc03-im08-20261014a"
SHORT = "im08"
LESSON = "2026-uc03-imunologia-08-reconhecimento-inato"
DECK = "NEBLI::UC03::P1::Imunologia::Reconhecimento imune inato"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (toll-like receptor, MyD88, flagellin, CpG, TLR3, chemokine, CXCL8, fever IL-1, pyrogen, perforin, natural killer, phagolysosome, IL-1, GM-CSF, "
         "cytokine, NF-κB, interferon-α; busca/anking.txt) e cópias NEBLI vivas de Inflamação aguda (pt38), Complemento (IM31) e Infecção viral (pt61), 14/10: ")
EXCLUIDOS = [
 (1520299451730, "PRR com cloze no adjetivo 'pattern-recognition': sh 1791780342851 cobra PRR e PAMP"),
 (1497440851060, "PRR citosólico e IFN: coberto por d-trif e sh de IFN tipo I"),
 (1467833820283, "NF-κB definido genericamente: sh 1791743339611 cobra TLR → NF-κB"),
]
FORA_DO_RECORTE = ["Recapitulação da aula 07 (lâminas 3–5): repertório clonal e tolerância.", "Nobel de Ehrlich (15): Tab.", "Figura detalhada das vias (19): Tab."]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não tem este fato da aula como card."
EP = [1520299451730, 1471541811425, 1487117308213]
A_, B_, C_, D_, E_ = "A-inato-e-adquirido", "B-PRR", "C-efetores", "D-mediadores", "E-vias"

CARDS = [
 # A — hierarquia do reconhecimento (3–7)
 au("a-hierarquia", ORG("Two levels of <b>immune recognition</b>:<br>- innate: germline-encoded {{c1::pattern recognition receptors}} sense loss of homeostasis<br>- adaptive: randomly generated {{c2::clonal}} receptors (TCR, BCR) recognize antigens"),
    G(1, 2), A_, "Reconhecimento hierárquico", "6; prova 2024 P1 2.11", "prova", NAO, EP, "Verde: lâmina 6; prova 2024.",
    extra="- Innate signals decide whether the adaptive response becomes immunity or tolerance"),
 au("a-apc", "{{c1::Dendritic cells}}, the main <b>antigen-presenting cells</b>, carry tissue antigens to lymph nodes and present them to naive T cells",
    G(1), A_, "Ponte: apresentação de antígenos (DC)", "7; prova 2016 P2 1.1", "prova", NAO, EP, "Verde: lâmina 7; prova 2016 (tipo celular que liga inata e adquirida). Revisão 15/10: cloze saiu de 'antigens' para o nome a decorar."),
 au("a-treinada", "<b>BCG</b> can epigenetically reprogram monocytes to respond more strongly to later, unrelated infections, a nonspecific memory called {{c1::trained immunity}}",
    {1: Z}, A_, "Inato sem memória clássica; imunidade treinada", "6; provas 2024 P2 2.2 e 2025 P2 7.1", "prova", NAO, EP, "Azul: provas 2024 (inato não gera memória) e 2025 (BCG → resposta à vacina). Revisão 15/10.",
    extra="- Innate receptors are germline-encoded and innate cells do not form antigen-specific memory clones"),
 # B — PRR (8; 16–17)
 sh(1791780352647, "verde", B_, "Sentinelas residentes carregam os PRR", "8; provas 2015 P1 1.2 e 2017 P1 2.5/3.4", "Verde: provas (células de alarme residentes disparam o recrutamento); viva na pt38. Revisão 15/10."),
 sh(1791780342851, "verde", B_, "PRR reconhecem PAMP", "8", "Verde: lâmina 8; viva na pt38."),
 sh(1791743340457, "verde", B_, "DAMP no tecido necrótico", "8", "Verde: lâmina 8; viva na pt38."),
 au("b-familias", ORG("Families of <b>pattern recognition receptors</b> and where they sit:<br>- Toll-like and C-type lectin receptors: {{c1::membranes}}<br>- NOD-like receptors: membranes and cytoplasm<br>- RIG-I-like receptors: {{c2::cytoplasm}}<br>- AIM2-like receptors: {{c3::nucleus}}"),
    {1: Z, 2: Z, 3: R}, B_, "Famílias de PRR e localização", "8; 2", "central", NAO, EP, "Azul: tabela da lâmina 8; objetivo 2.",
    extra="- Scavenger receptors (CD36) are also membrane PRRs"),
 sh(1791743339358, "verde", B_, "TLR4 e LPS", "16", "Verde: tabela da lâmina 16; viva na pt38."),
 sh(1791743339982, "verde", B_, "TLR endossomais e TLR5", "16", "Verde: tabela da lâmina 16; viva na pt38."),
 au("b-tlr3", "<b>Endosomal TLR3</b> recognizes viral {{c1::double-stranded RNA}}",
    {1: Z}, B_, "TLR3", "16; prova 2018 P3 5.3", "prova", NAO, EP, "Azul: lâmina 16; gabarito 2018 (influenza → TLR3)."),
 au("b-tlr9", "<b>Endosomal TLR9</b> recognizes unmethylated {{c1::CpG}} DNA from bacteria and viruses",
    {1: R}, B_, "TLR9", "16", "lateral", NAO, EP, "Rosa: lâmina 16."),
 au("b-nod2", "Cytosolic <b>NOD2</b> recognizes bacterial {{c1::muramyl dipeptide}}, a peptidoglycan fragment",
    {1: R}, B_, "NOD2", "17", "lateral", NAO, EP, "Rosa: lâmina 17.",
    extra="- NOD1 recognizes iE-DAP; NODs activate NF-κB"),
 au("b-rig", "Cytosolic {{c1::RIG-I}} detects short double-stranded <b>viral RNA</b> with a 5′ triphosphate and triggers type I interferon",
    {1: Z}, B_, "RIG-I", "17", "central", NAO, EP, "Azul: lâmina 17; prova 2025 P3 2.5 (antiviral inata)."),
 au("b-dectina", "Fungal <b>β-glucans</b> are recognized by {{c1::Dectin-1}}, a C-type lectin receptor on phagocytes",
    {1: Z}, B_, "Dectina-1", "17; 8; prova 2018 P2 1.5", "prova", NAO, EP, "Azul: lâminas 8 e 17; prova 2018 (fungos)."),
 # C — efetores (9–12)
 au("c-estrategias", ORG("Innate strategies to <b>restore homeostasis</b>:<br>- protect neighbors: type I {{c1::interferons}}<br>- kill diseased cells: {{c2::cytotoxicity}}<br>- clean the area: {{c3::phagocytosis}}<br>- call for help: mediators"),
    G(1, 2, 3), C_, "Estratégias da resposta inata", "9; provas 2024 P2 2.1 e 2025 P3 2.5", "prova", NAO, EP, "Verde: lâmina 9; provas 2024 e 2025.",
    extra="- Fever is the systemic manifestation"),
 ak("ak-pirogenio", 1471541811425, G(1, 2), C_, "IL-1 e febre", "9", "Verde: HY 1; febre na lâmina 9."),
 sh(1791984890700, "verde", C_, "IFN tipo I: estado antiviral", "10", "Verde: lâmina 10; viva na pt61."),
 au("c-ifn-gripe", "Many systemic <b>flu</b> symptoms, such as fever and body aches, are caused by {{c1::interferon}} more than by the virus itself",
    {1: Z}, C_, "Sintomas da gripe", "10", "central", NAO, EP, "Azul: transcrição (efeitos sistêmicos do IFN)."),
 au("c-citotox", ORG("Two ways <b>cytotoxic cells</b> induce apoptosis of their target:<br>- release of {{c1::cytotoxic granules}} (perforin, granzymes)<br>- membrane signaling through {{c2::Fas–FasL}}"),
    G(1, 2), C_, "Citotoxicidade = suicídio induzido; dois mecanismos", "11", "central", NAO, EP, "Verde: lâmina 11. Revisão 15/10: cloze em 'apoptosis' era entregue pela frase; agora os dois mecanismos da lâmina.",
    extra="- The target dies by its own apoptosis, an induced suicide, and the killer moves on to other targets"),
 sh(1791984891827, "verde", C_, "Perforinas e granzimas", "11", "Verde: lâmina 11; viva na pt61."),
 au("c-fagocitose", ORG("Steps of <b>phagocytosis</b>:<br>1. {{c1::chemotaxis}} toward the target<br>2. adhesion, helped by {{c2::opsonization}}<br>3. zipper-like engulfment into a phagosome<br>4. fusion with {{c3::lysosomes}} and killing (enzymes, oxygen radicals)"),
    G(1, 2, 3), C_, "Etapas da fagocitose", "12", "central", NAO, EP, "Verde: lâmina 12.", extra="- Oxygen radicals come from the respiratory burst"),
 sh(1791667096988, "azul", C_, "Opsoninas C3b e IgG", "12", "Azul: lâmina 12; viva na IM31."),
 sh(1791743343758, "azul", C_, "Explosão respiratória", "12", "Azul: lâmina 12; viva na pt38."),
 # D — mediadores (13–14)
 au("d-classes", ORG("Classes of <b>cytokines</b>:<br>- {{c1::interleukins}}: between leukocytes<br>- {{c2::colony-stimulating factors}}: G-CSF, GM-CSF<br>- interferons: α, β, γ<br>- {{c3::chemokines}}: attract cells"),
    G(1, 2, 3), D_, "Classes de citocinas", "13; 14", "central", NAO, EP, "Verde: lâminas 13–14.",
    extra="- Cytokines are pleiotropic: one cytokine has many effects, depending on the target cell and its receptors<br>- TNF-α is the main cytotoxic factor<br>- Names often reflect history, not function"),
 au("d-quimiocinas", "In the <b>chemokine</b> families named by cysteine spacing (CC, CXC, CX3C, XC), IL-8 is {{c1::CXCL8}}",
    {1: R}, D_, "Famílias de quimiocinas", "14", "lateral", NAO, EP, "Rosa: lâmina 14.",
    extra="- CCL2 (MCP-1), CX3CL1 (fractalkine), XCL1 (lymphotactin)"),
 au("d-lipidicos", "<b>Activated cells</b> release lipid mediators from arachidonic acid, prostaglandins and leukotrienes, and also {{c1::PAF}}",
    {1: R}, D_, "Mediadores lipídicos", "13", "lateral", NAO, EP, "Rosa: lâmina 13; os eicosanoides são da pt38 (revisão 15/10).",
    extra="- PAF = platelet-activating factor<br>- Exosomes are another, newer class of messengers"),
 # E — vias (18–22)
 au("e-myd88", "Most <b>TLRs</b> signal through the adaptor {{c1::MyD88}}, leading to NF-κB and AP-1 and the production of inflammatory cytokines",
    G(1), E_, "MyD88", "18; prova 2017 P1 1.8", "prova", NAO, EP, "Verde: lâmina 18; prova 2017 (MyD88 e TRIF).",
    extra="- TLR binding works by dimerizing the receptor or changing the shape of a preformed dimer"),
 sh(1791743339611, "verde", E_, "TLR ativa NF-κB", "18", "Verde: lâmina 18; viva na pt38."),
 au("d-trif", "The <b>TLR</b> adaptor {{c1::TRIF}} activates IRFs and the production of type I interferons, giving antiviral activity",
    {1: Z}, E_, "TRIF", "18; prova 2017 P1 1.8", "prova", NAO, EP, "Azul: lâmina 18; prova 2017.",
    extra="- The pathways cross: one TLR can lead to both outcomes"),
 sh(1791743339740, "verde", E_, "Inflamassoma", "20", "Verde: lâmina 20; viva na pt38."),
 sh(1791780343453, "azul", E_, "NLRP3 + ASC + caspase-1", "21", "Azul: lâmina 21; viva na pt38."),
 sh(1791743339860, "verde", E_, "IL-1β e IL-18", "20", "Verde: lâmina 20; viva na pt38."),
 au("e-dois-sinais", "The <b>inflammasome</b> needs a first, {{c1::priming}} signal (e.g. a TLR via NF-κB) to make pro-IL-1β, before caspase-1 can cleave it",
    {1: Z}, E_, "Dois sinais do inflamassoma", "21", "central", NAO, EP, "Azul: lâmina 21; transcrição."),
]
SEM_IMAGEM = "fato imunológico sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"a-apc": "- They also sense whether the tissue is in homeostasis<br>- Dendritic cells are the main APCs", "b-tlr3": "- TLR3 signals through TRIF, inducing interferon", "b-tlr9": "- Unmethylated CpG motifs are common in microbial DNA",
         "b-rig": "- MDA5 recognizes long dsRNA", "b-dectina": "- Dectin-1 also drives Th17 responses to fungi", "c-ifn-gripe": "- Interferon-α given as a drug causes the same flu-like symptoms",
         "ak-pirogenio": "- Antipyretics act by blocking prostaglandin synthesis<br>- Infected lizards kept from basking cannot raise their temperature and die more often, so fever is a defense", 
         "e-dois-sinais": "- Signal 2 (e.g. crystals, ATP) assembles NLRP3, ASC and caspase-1"}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if VERSO.get(k):
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Identificar os PRR como sensores de homeostase (famílias, localização, ligantes), as estratégias efetoras inatas (IFN, citotoxicidade, fagocitose, mediadores), as vias MyD88/TRIF e o inflamassoma, e as classes de citocinas.",
 "centrais": [
   ("inato e adquirido", "a-hierarquia", "a-apc"),
   ("PRR", "sh-1791780342851", "sh-1791743340457", "b-familias", "sh-1791743339358", "sh-1791743339982", "b-tlr3", "b-tlr9", "b-nod2", "b-rig", "b-dectina"),
   ("efetores", "c-estrategias", "c-febre", "ak-pirogenio", "sh-1791984890700", "c-ifn-gripe", "c-citotox", "sh-1791984891827", "c-fagocitose", "sh-1791667096988", "sh-1791743343758"),
   ("mediadores", "d-pleiotropia", "d-classes", "d-quimiocinas", "d-lipidicos"),
   ("vias", "e-myd88", "sh-1791743339611", "d-trif", "sh-1791743339740", "sh-1791780343453", "sh-1791743339860", "e-dois-sinais"),
 ],
 "exemplos": ["lagartos e febre", "IL-6 como alvo na COVID-19", "Ehrlich (1908)"],
 "outras_aulas": [("inflamação aguda", "38"), ("complemento", "31"), ("infecção viral", "61")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
