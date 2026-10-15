# Especificação curada — MHC: captura, processamento e apresentação de antígenos (UC03 P1, Imunologia; Prof. Niels Câmara; 75 lâminas).
# A aula 45 (Ativação de linfócitos T) já tem MHC–CD4/CD8, β2m, cadeia invariante, proteassomo/TAP, apresentação cruzada, 1º/2º sinal e DC madura: entram por sh().
RUN_ID = "uc03-im20-20261014a"
SHORT = "im20"
LESSON = "2026-uc03-imunologia-20-mhc-apresentacao"
DECK = "NEBLI::UC03::P1::Imunologia::MHC e apresentação de antígenos"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (MHC I, HLA-A, all nucleated, haplotype, plasmacytoid, peptide-binding, interferon-α; busca/anking.txt) e cópias NEBLI vivas das aulas 45, 49, pt38 e 08, 14/10: ")
EXCLUIDOS = [
 (1486952644614, "MHC I '1 cadeia longa e 1 curta': repete o card de β2-microglobulina"),
 (1486952677289, "MHC II '2 cadeias iguais': coberto por c-estrutura"),
 (1482359355658, "gliadina na doença celíaca: UC de gastro"),
]
FORA_DO_RECORTE = ["Obesidade, HAS e IRA como síndromes inflamatórias (6–8): só o experimento do RAG1 entra (rosa); o resto no Tab.",
                   "PRR e inflamassoma (14–19): aula 08; só compartilhados.", "Diferenciação Th1/Th2/Th17 (64, 74–75): aula 45."]


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
EP = [1486952630150, 1486952649215, 1487117336631]
A_, B_, C_, D_, E_ = "A-reconhecimento", "B-APC", "C-MHC", "D-processamento", "E-ativacao-T"

CARDS = [
 # A — sistema imune como reconhecimento (7–26)
 au("a-rag-has", "Mice lacking <b>RAG1</b>, and therefore T and B cells, develop less hypertension after angiotensin II infusion, implicating {{c1::adaptive immunity}} in hypertension",
    {1: R}, A_, "HAS como síndrome inflamatória", "7", "lateral", NAO, EP, "Rosa: lâmina 7; transcrição.",
    extra="- Similarly, mice without CD4 and CD8 T cells suffer less acute kidney injury"),
 sh(1791743340632, "azul", A_, "Urato ativa NLRP3", "13; 19", "Azul: lâminas 13 e 19 (gota); viva na pt38."),
 au("a-bcr-tcr", "The <b>BCR</b> recognizes whole native antigens, whereas the TCR recognizes only {{c1::processed peptides}} presented on MHC",
    G(1), A_, "BCR × TCR", "23; 26", "central", NAO, EP, "Verde: lâminas 23 e 26 ('precisa que alguém mostre para ele').",
    extra="- That is why T cells need antigen-presenting cells"),
 sh(1791625424481, "verde", A_, "MHC II → CD4", "26", "Verde: lâmina 26; viva na aula 45."),
 sh(1791625424657, "verde", A_, "MHC I → CD8", "26", "Verde: lâmina 26; viva na aula 45."),
 # B — APC e células dendríticas (27–38)
 au("b-cd4-regente", "<b>CD4+ T cells</b> act as the conductor of the immune response, so their activation is restricted to cells expressing MHC class {{c1::II::I/II}}",
    {1: Z}, B_, "CD4 regente; ativação restrita", "28; 34", "central", NAO, EP, "Azul: lâmina 28; transcrição.",
    extra="- Limiting MHC II to professional APCs lowers the risk of autoimmunity"),
 au("b-apc", ORG("The three <b>professional antigen-presenting cells</b>:<br>- {{c1::dendritic cells}} (the best)<br>- {{c2::macrophages}}<br>- {{c3::B cells}}"),
    G(1, 2, 3), B_, "APCs profissionais", "34; 35; prova 2017 P4 1.6", "prova", NAO, EP, "Verde: lâminas 34–35.",
    extra="- They express MHC II and costimulatory molecules"),
 sh(1791625426408, "verde", B_, "DC ativa T naive", "34", "Verde: lâmina 34; viva na aula 45."),
 au("b-drenagem", "Antigens from <b>skin, gut and airways</b> are carried by dendritic cells to {{c1::secondary lymphoid organs}}, where naive T cells are activated",
    G(1), B_, "Antígeno vai ao órgão linfoide secundário", "31; 32", "central", NAO, EP, "Verde: lâminas 31–32.",
    extra="- Blood-borne antigens are captured in the spleen"),
 sh(1791625425333, "verde", B_, "DC amadurece ao migrar", "37; 38", "Verde: lâminas 37–38; viva na aula 45."),
 au("b-imatura", "<b>Immature dendritic cells</b> in tissues specialize in {{c1::antigen capture}}, with many Fc and mannose receptors but little costimulation",
    {1: Z}, B_, "DC imatura", "38", "central", NAO, EP, "Azul: tabela da lâmina 38.",
    extra="- Mature DCs keep MHC II on the surface for over 100 hours"),
 au("b-pdc", "{{c1::Plasmacytoid}} dendritic cells sense <b>viral nucleic acids</b> through TLR7 and TLR9 and produce large amounts of type I interferon",
    {1: Z}, B_, "DC plasmocitoide", "36", "central", NAO, EP, "Azul: lâmina 36; transcrição (SARS-CoV-2 reduz esse IFN).", extra="- SARS-CoV-2 dampens this interferon to escape"),
 # C — MHC (39–49)
 ak("ak-hla", 1486952620697, G(1), C_, "MHC = HLA", "41", "Verde: lâmina 41."),
 ak("ak-hla-i", 1486952623418, G(1), C_, "HLA-A, B, C", "45; 41", "Verde: lâmina 45."),
 ak("ak-hla-ii", 1486952657292, G(1), C_, "HLA-DP, DQ, DR", "45; 41", "Verde: lâmina 45."),
 ak("ak-nucleadas", 1486952630150, G(1), C_, "MHC I em todas as nucleadas", "46", "Verde: transcrição; prova 2015."),
 ak("ak-apc-ii", 1486952664370, G(1), C_, "MHC II só em APC", "47", "Verde: lâmina 47; transcrição."),
 au("c-codominante", "<b>HLA genes</b> are inherited as two {{c1::haplotypes}}, one from each parent, and both are expressed codominantly",
    G(1), C_, "Haplótipos e codominância", "42", "central", NAO, EP, "Verde: lâmina 42; prova 2015 P2sub 3.3 (HLA).",
    extra="- A sibling has a 25% chance of being fully HLA-identical"),
 au("c-polimorfismo", "The <b>MHC</b> is the most {{c1::polymorphic}} gene system in the body, which makes matched unrelated transplant donors hard to find",
    G(1), C_, "Polimorfismo", "43", "central", NAO, EP, "Verde: lâmina 43; transcrição (banco de medula).",
    extra="- Polygeny (several genes) adds to the diversity"),
 ak("ak-fenda-i", 1486952649215, G(1), C_, "Fenda do MHC I: 8–10 aa", "45; 68", "Verde: lâminas 45 e 68."),
 ak("ak-fenda-ii", 1486952681913, G(1), C_, "Fenda do MHC II: 13–17 aa", "45; 68", "Verde: lâminas 45 e 68."),
 au("c-estrutura", ORG("Structure of <b>MHC molecules</b>:<br>- class I: α chain + {{c1::β2-microglobulin}}<br>- class II: an α and a {{c2::β}} chain"),
    {1: Z, 2: Z}, C_, "Estrutura de MHC I e II", "45; 68", "central", NAO, EP, "Azul: lâminas 45, 46, 47 e 68.",
    duplicacao_ok="ganho: estrutura das duas classes lado a lado; sh de β2m cobra só a proteína associada", extra="- Class I cleft is closed at both ends; class II cleft is open"),
 au("c-ancoras", "One <b>MHC molecule</b> can present many different peptides, as long as they fit its {{c1::anchor residues}} into the cleft pockets",
    {1: Z}, C_, "Resíduos-âncora", "44; 39", "central", NAO, EP, "Azul: lâminas 39 e 44; transcrição."),
 sh(1791625424832, "verde", C_, "Restrição ao MHC", "48", "Verde: lâmina 48; viva na aula 45."),
 ak("ak-superantigeno", 1487117336631, G(1, 2), C_, "Superantígeno", "49", "Verde: lâmina 49; transcrição."),
 # D — processamento (50–61)
 sh(1791625426657, "verde", D_, "MHC I: antígenos endógenos", "50; 51", "Verde: lâminas 50–51; viva na aula 45."),
 sh(1791625426833, "verde", D_, "Proteassomo e TAP", "52; 53", "Verde: lâminas 51–55; viva na aula 45."),
 au("d-sem-peptideo", "A <b>class I MHC</b> molecule reaches the cell surface only when its cleft holds a {{c1::peptide}}",
    {1: Z}, D_, "MHC I precisa de peptídeo", "54", "central", NAO, EP, "Azul: lâmina 54; transcrição.",
    extra="- Calnexin, calreticulin and tapasin hold it near TAP until then"),
 au("d-tumor", "Viral proteins and overexpressed or mutant <b>tumor proteins</b> are processed in the cytosol and presented on MHC class {{c1::I::I/II}} to cytotoxic CD8+ T cells",
    {1: Z}, D_, "Vírus e tumor → CD8", "51; 70", "central", NAO, EP, "Azul: transcrição; prova 2015 P2 7.1.", extra="- That is why CD8+ T cells kill virus-infected and tumor cells"),
 sh(1791625427059, "verde", D_, "MHC II: antígenos exógenos", "56", "Verde: lâmina 56; viva na aula 45."),
 sh(1791625427233, "verde", D_, "Cadeia invariante", "58", "Verde: lâmina 58; viva na aula 45."),
 au("d-clip", "Digestion of the <b>invariant chain</b> leaves the {{c1::CLIP}} fragment in the class II cleft until HLA-DM swaps it for a peptide",
    {1: Z}, D_, "CLIP e HLA-DM", "58; 59", "central", NAO, EP, "Azul: lâminas 58–59.",
    extra="- HLA-DO regulates HLA-DM"),
 sh(1791625427358, "azul", D_, "Carga do MHC II em vesícula ácida", "57; 58", "Azul: lâmina 57 (pH); viva na aula 45."),
 sh(1791625427531, "verde", D_, "Apresentação cruzada", "60; 61", "Verde: lâminas 60–61; viva na aula 45."),
 au("d-cruzada-por-que", "<b>Cross-presentation</b> matters because cytotoxic T cells need help from {{c1::CD4+}} T cells activated by the same dendritic cell",
    {1: Z}, D_, "Por que a apresentação cruzada importa", "61", "central", NAO, EP, "Azul: transcrição.",
    duplicacao_ok="ganho: o porquê da apresentação cruzada; sh cobra o mecanismo", extra="- Ingested viral proteins leak from the phagosome into the cytosol and reach MHC I"),
 # E — ativação do T (62–66)
 sh(1791625428408, "verde", E_, "1º sinal: TCR–MHC/peptídeo", "62; 63", "Verde: lâminas 62–63; viva na aula 45."),
 sh(1791625428533, "verde", E_, "2º sinal: B7–CD28", "62; 63", "Verde: lâminas 62–63; viva na aula 45."),
 au("e-terceiro", "The third signal for <b>T-cell activation</b> comes from {{c1::cytokines}} (e.g. IL-2), which drive clonal expansion and differentiation",
    {1: Z}, E_, "3º sinal", "62", "central", NAO, EP, "Azul: lâmina 62 (teoria dos sinais)."),
 au("e-adesao", "In the <b>immunological synapse</b>, adhesion pairs such as {{c1::LFA-1}}–ICAM-1 hold the APC and T cell together long enough to signal",
    {1: R}, E_, "Sinapse imunológica", "63", "lateral", NAO, EP, "Rosa: lâmina 63.",
    extra="- Also CD2–LFA-3 and CD40–CD40L"),
 au("e-dc-th", "When a <b>dendritic cell</b> senses a worm, it steers naive CD4+ T cells toward the {{c1::Th2}} subset, which makes IL-4",
    G(1), E_, "Reconhecimento define o subtipo", "64; 65; 21", "central", NAO, EP, "Verde: lâminas 21, 64–65; transcrição.",
    extra="- Bacteria instead drive Th1 (IFN-γ), through dendritic IL-12"),
]
SEM_IMAGEM = "fato imunológico sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"ak-hla": "- HLA = human leukocyte antigen", "ak-hla-i": "- Class I presents to CD8+ T cells", "ak-hla-ii": "- Class II presents to CD4+ T cells",
         "ak-nucleadas": "- So any infected or tumor cell can show its proteins to CD8+ T cells", "ak-apc-ii": "- Dendritic cells, macrophages and B cells",
         "ak-fenda-i": "- The cleft is closed at both ends", "ak-fenda-ii": "- The cleft is open, so longer peptides fit", "c-ancoras": "- Anchor residues are fixed positions (e.g. P2 and the C-terminal)",
         "ak-superantigeno": "- They bypass processing and activate many T cells at once, causing rapid, massive cytokine release",
         "e-terceiro": "- IL-2 acts on the T cell itself (autocrine)"}
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
 "objetivo": "Explicar como as APCs (sobretudo células dendríticas) capturam, processam e apresentam antígenos no MHC; diferenciar MHC I e II (HLA, expressão, estrutura, fenda, vias de processamento, apresentação cruzada) e os sinais de ativação do linfócito T.",
 "centrais": [
   ("reconhecimento", "a-rag-has", "sh-1791743340632", "a-bcr-tcr", "sh-1791625424481", "sh-1791625424657"),
   ("APC", "b-cd4-regente", "b-apc", "sh-1791625426408", "b-drenagem", "sh-1791625425333", "b-imatura", "b-pdc"),
   ("MHC", "ak-hla", "ak-hla-i", "ak-hla-ii", "ak-nucleadas", "ak-apc-ii", "c-codominante", "c-polimorfismo", "ak-fenda-i", "ak-fenda-ii", "c-estrutura", "c-ancoras", "sh-1791625424832", "ak-superantigeno"),
   ("processamento", "sh-1791625426657", "sh-1791625426833", "d-sem-peptideo", "d-tumor", "sh-1791625427059", "sh-1791625427233", "d-clip", "sh-1791625427358", "sh-1791625427531", "d-cruzada-por-que"),
   ("ativação do T", "sh-1791625428408", "sh-1791625428533", "e-terceiro", "e-adesao", "e-dc-th"),
 ],
 "exemplos": ["gota", "silicose", "obesidade e microbiota", "COVID-19 e DC plasmocitoide", "transplante de medula"],
 "outras_aulas": [("ativação de T", "45"), ("reconhecimento inato", "08"), ("inflamação", "38")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
