# Especificação curada — Mecanismos efetores do sistema imune (UC03 P1, Imunologia; Prof. Niels Câmara; 64 lâminas).
# PRR e inflamassoma = aula 08; fagocitose, ROS, M1/M2, NK, ADCC, Th e memória já vivos (pt38, 45, 49, 61, 62, IM31): entram por sh(). Notas só da IM37 (Codex, em andamento) não são compartilhadas.
RUN_ID = "uc03-im22-20261015a"
SHORT = "im22"
LESSON = "2026-uc03-imunologia-22-mecanismos-efetores"
DECK = "NEBLI::UC03::P1::Imunologia::Mecanismos efetores imunes"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 15/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing e cópias NEBLI vivas por frases (NETs, myeloperoxidase, nitric oxide, ADCC, natural killer, M1/M2, Kupffer, microglia, defensins, lysozyme, CD16, memory, Th17, pus, "
         "L-selectin, homing, NADPH oxidase, peroxynitrite, leprosy), 15/10: ")
EXCLUIDOS = []
FORA_DO_RECORTE = ["PRR, NOD e inflamassoma (lâminas 5–11): aula 08.", "Sinalização da fagocitose (24–25): Tab.", "Apresentação de antígenos (49–50): aula 20.", "Mediadores metabólicos (succinato): Tab."]


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não tem este fato da aula como card."
EP = [1487117308213, 1487117314403, 1486867503989]
A_, B_, C_, D_, E_ = "A-reconhecimento-e-barreiras", "B-fagocitos", "C-NK", "D-macrofagos", "E-linfocitos-T"

CARDS = [
 # A — resposta e barreiras (3–22)
 au("a-imediata", ORG("<b>Effector functions</b> after a danger signal:<br>- immediate: release of {{c1::preformed}} contents (e.g. mast cell degranulation)<br>- late: need {{c2::gene transcription}} (cytokines, chemokines, reactive species)"),
    {1: Z, 2: Z}, A_, "Função efetora imediata × tardia", "3", "central", NAO, EP, "Azul: lâmina 3; transcrição."),
 au("a-peptideos", "<b>Epithelial cells</b> and neutrophils make antimicrobial peptides such as {{c1::defensins}}, which insert into microbial membranes and destroy them",
    G(1), A_, "Peptídeos antimicrobianos", "22", "central", NAO, EP, "Verde: lâmina 22; prova 2024 P2 2.1 (elementos inatos).",
    extra="- Other noncellular defenses: mucus, cilia, flow, acid pH, lysozyme in secretions"),
 # B — fagócitos (23–34)
 au("b-opsonizacao", "Coating a <b>microbe</b> with antibody or C3b so that phagocyte receptors grab it better is called {{c1::opsonization}}",
    G(1), B_, "Opsonização", "26; 27; provas 2015 P1 1.4 e 2.3", "prova", NAO, EP, "Verde: lâminas 26–27; provas 2015.",
    extra="- Phagocytes bind them through Fc receptors and complement receptors (CR1, CR3)"),
 sh(1791667096988, "verde", B_, "C3b e IgG como opsoninas", "26", "Verde: lâmina 26; viva na IM31."),
 sh(1791780361432, "verde", B_, "NADPH oxidase → superóxido", "28", "Verde: lâmina 28; viva na pt38."),
 sh(1791780361607, "verde", B_, "Mieloperoxidase → HOCl", "28", "Verde: lâmina 28; viva na pt38."),
 sh(1791625430456, "azul", B_, "NOS: arginina → NO", "29", "Azul: lâmina 29; viva na aula 45."),
 sh(1791780362080, "azul", B_, "Peroxinitrito", "29", "Azul: lâmina 29; viva na pt38."),
 au("b-pus", "<b>Pus</b> is made largely of {{c1::neutrophils}} that died after killing microbes with their oxidative burst",
    G(1), B_, "Pus", "31", "central", NAO, EP, "Verde: transcrição ('indicativo de que o sistema funcionou').",
    extra="- Neutrophils are 45–70% of blood leukocytes"),
 au("b-nets", "Activated <b>neutrophils</b> can expel their DNA with histones and granule enzymes as extracellular webs called {{c1::NETs}}, which trap microbes",
    G(1), B_, "NETs", "33; 32", "central", NAO, EP, "Verde: lâmina 33.",
    extra="- NET = neutrophil extracellular trap; the process is NETosis<br>- Histone H3 is citrullinated during it"),
 sh(1791629596121, "verde", B_, "ADCC por CD16", "34", "Verde: lâmina 34; viva na aula 49; prova 2017 P1 4.3."),
 au("b-adcc", ORG("Cells that perform <b>ADCC</b>:<br>- NK cells (main)<br>- {{c1::neutrophils}}<br>- {{c2::macrophages}}<br>- {{c3::eosinophils}}"),
    {1: Z, 2: Z, 3: Z}, B_, "Quem faz ADCC", "34; prova 2015 P2 2.6", "prova", NAO, EP, "Azul: lâmina 34 ('presente também em').",
    extra="- An innate cell uses an adaptive molecule (the antibody) as a bridge"),
 # C — NK (35–37)
 au("c-nk", "<b>NK cells</b> are lymphocytes without a {{c1::TCR}}, making up 5–20% of blood mononuclear cells, that kill virus-infected and tumor cells",
    G(1), C_, "NK sem TCR", "35; prova 2024 P1 2.11", "prova", NAO, EP, "Verde: lâmina 35; prova 2024.",
    extra="- They also produce IFN-γ"),
 sh(1791984891454, "verde", C_, "NK mata célula sem MHC I", "36", "Verde: lâmina 36; viva na pt61."),
 au("c-kir", "Inhibitory {{c1::KIR}} receptors on <b>NK cells</b> recognize self MHC class I and stop the killing of healthy cells",
    {1: Z}, C_, "KIR", "36", "central", NAO, EP, "Azul: lâmina 36.",
    extra="- Losing MHC I is like losing an identity card"),
 sh(1791984891827, "verde", C_, "Perforina e granzima", "37", "Verde: lâmina 37; viva na pt61."),
 # D — macrófagos (38–43)
 au("d-residentes", "<b>Tissue-resident macrophages</b> derive from the embryonic {{c1::yolk sac}} and renew themselves locally, unlike infiltrating macrophages that come from blood monocytes",
    {1: Z}, D_, "Macrófagos residentes × infiltrantes", "38", "central", NAO, EP, "Azul: lâmina 38; transcrição."),
 au("d-nomes", ORG("Names of <b>tissue macrophages</b>:<br>- bone: {{c1::osteoclast}}<br>- central nervous system: {{c2::microglia}}<br>- liver: {{c3::Kupffer}} cell<br>- connective tissue: histiocyte"),
    G(1, 2, 3), D_, "Macrófagos por órgão", "39", "central", NAO, EP, "Verde: lâmina 39; transcrição.",
    extra="- Lung: alveolar macrophage; kidney: mesangial cell", duplicacao_ok="ganho: tabela de nomes por órgão; Kupffer e micróglia da 62 cobram uma célula cada"),
 sh(1791625434032, "verde", D_, "Macrófago M1", "40", "Verde: lâmina 40; viva na aula 45."),
 sh(1791625434457, "verde", D_, "Macrófago M2", "41", "Verde: lâmina 41; viva na aula 45."),
 au("d-mreg", "Macrophages exposed to Treg cytokines, glucocorticoids and apoptotic cells become anti-inflammatory {{c1::regulatory}} <b>macrophages</b>",
    {1: Z}, D_, "Macrófago regulador", "42; 43", "central", NAO, EP, "Azul: lâminas 42–43."),
 # E — linfócitos T (44–64)
 sh(1791625425207, "verde", E_, "Naive recircula; efetor vai ao tecido", "45; 47", "Verde: lâminas 45–47; viva na aula 45."),
 au("e-homing", "After activation, <b>effector T cells</b> switch the {{c1::chemokine receptors}} they express, which guide them to the infected tissue",
    {1: Z}, E_, "Endereçamento do T efetor", "48", "central", NAO, EP, "Azul: lâmina 48 (CCR4 pele, CCR9 intestino).",
    extra="- For example, CCR9 for the gut and CCR4 for the skin"),
 au("e-cd4-cd8", "<b>CD4+ T cells</b> act mainly by helping other cells through cytokines, whereas {{c1::CD8+}} T cells kill target cells directly",
    G(1), E_, "CD4 ajuda, CD8 mata", "51; 61; 64", "central", NAO, EP, "Verde: lâminas 51, 57–64; transcrição.",
    extra="- CD4 help activates macrophages, B cells and CD8 cells"),
 au("e-th1", "<b>Th1 cells</b> activate macrophages through {{c1::IFN-γ}} and CD40L, boosting phagocytosis and the oxidative burst",
    G(1), E_, "Th1 ativa macrófago", "52; 53; 61", "central", NAO, EP, "Verde: lâminas 52–53 e 61.",
    extra="- Activated macrophages also raise MHC and B7"),
 sh(1791625430632, "azul", E_, "IFN-γ induz iNOS", "52", "Azul: lâmina 52; viva na aula 45."),
 au("e-th2", "The helper subset that drives eosinophil- and mast cell-rich inflammation while limiting <b>macrophage activation</b> is {{c1::Th2}}",
    {1: Z}, E_, "Th2 limita o macrófago", "54; 62", "central", NAO, EP, "Azul: lâminas 54 e 62."),
 sh(1791625432733, "azul", E_, "Indução de Th17", "55", "Azul: lâmina 55; viva na aula 45."),
 sh(1791625422039, "verde", E_, "Th17 recruta neutrófilos", "56", "Verde: lâmina 56 (Candida); viva na aula 45."),
 au("e-candida", "Against <b>Candida</b>, Dectin-1 signaling in monocytes induces IL-6 and IL-23, steering T cells toward {{c1::Th17}}, which recruits neutrophils",
    {1: Z}, E_, "Th17 contra fungos", "56", "central", NAO, EP, "Azul: lâmina 56; transcrição.",
    duplicacao_ok="ganho: o caminho do reconhecimento do fungo até o subtipo; sh cobra a função"),
 au("e-ctl", "<b>Cytotoxic T cells</b> recognize peptide on MHC class I and kill the target through perforin and {{c1::granzymes}}, inducing apoptosis",
    G(1), E_, "Mecanismo do CTL", "57; 58; prova 2015 P2 2.7", "prova", NAO, EP, "Verde: lâminas 57–58; prova 2015.",
    extra="- A long-lasting immunological synapse is needed"),
 sh(1791625425933, "azul", E_, "Hanseníase tuberculoide: Th1", "63", "Azul: lâmina 63; viva na aula 45."),
 sh(1791625426108, "azul", E_, "Hanseníase virchowiana: Th2", "63", "Azul: lâmina 63; viva na aula 45."),
 au("e-memoria", "After the <b>infection</b> is cleared the response contracts, and only {{c1::lymphocytes::cell type}} leave memory cells",
    G(1), E_, "Memória só na adquirida", "60", "central", NAO, EP, "Verde: lâmina 60; transcrição; prova 2024 P2 2.2.",
    extra="- Innate cells do not form memory<br>- Memory cells stay in secondary lymphoid organs or bone marrow"),
]
SEM_IMAGEM = "fato imunológico sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] == "autoral" and "<img" not in c.get("text", "") + c.get("extra", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"a-imediata": "- Late functions involve activation, differentiation and migration", "d-residentes": "- Monocytes in the blood become macrophages once they enter tissues",
         "d-mreg": "- They secrete IL-10<br>- The same macrophage can shift between profiles as the infection resolves", "e-th2": "- Through IL-4, IL-10 and IL-13<br>- Th1 and Th2 balance each other",
         "e-candida": "- IL-17 also raises antimicrobial peptides and neutrophil production", "c-kir": "- KIR = killer-cell immunoglobulin-like receptor"}
DUPLICACAO = {}
for c in CARDS:
    if VERSO.get(c["key"]):
        c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[c["key"]]
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Descrever os mecanismos efetores celulares e acelulares: barreiras e peptídeos, fagocitose e opsonização, espécies reativas, neutrófilos (pus, NETs), ADCC, NK, plasticidade dos macrófagos e funções efetoras de CD4 (Th1, Th2, Th17) e CD8, até a memória.",
 "centrais": [
   ("reconhecimento e barreiras", "a-imediata", "a-peptideos"),
   ("fagócitos", "b-opsonizacao", "sh-1791667096988", "sh-1791780361432", "sh-1791780361607", "sh-1791625430456", "sh-1791780362080", "b-pus", "b-nets", "sh-1791629596121", "b-adcc"),
   ("NK", "c-nk", "sh-1791984891454", "c-kir", "sh-1791984891827"),
   ("macrófagos", "d-residentes", "d-nomes", "sh-1791625434032", "sh-1791625434457", "d-mreg"),
   ("linfócitos T", "sh-1791625425207", "e-homing", "e-cd4-cd8", "e-th1", "sh-1791625430632", "e-th2", "sh-1791625432733", "sh-1791625422039", "e-candida", "e-ctl",
    "sh-1791625425933", "sh-1791625426108", "e-memoria"),
 ],
 "exemplos": ["E. coli e neutrófilos", "Candida e Th17", "Leishmania e hanseníase"],
 "outras_aulas": [("PRR", "08"), ("ativação de T", "45"), ("ativação de B", "49"), ("inflamação", "38")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
