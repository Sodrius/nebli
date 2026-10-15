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
 au("b-ccr7", "Maturing <b>dendritic cells</b> express the chemokine receptor {{c1::CCR7}}, which guides them through lymphatics to the lymph node",
    {1: Z}, B_, "CCR7 leva a DC ao linfonodo", "37; monitoria P1 aula 5", "central", "consulta CCR7 sem card de dendrítica (15/10 noite).", EP,
    "Azul: monitoria P1 aula 5 (migração guiada por quimiocinas, receptor CCR7). Ajuste 15/10 noite (F-20261015-CLAUDE-05).",
    extra="- Naive T cells use the same receptor to enter the lymph node, so both meet in the T-cell zone"),
 au("b-linfocito-b-apc", "<b>B cells</b> present antigen they capture through their {{c1::BCR}} and take in by endocytosis, not phagocytosis, on MHC II",
    {1: Z}, B_, "Linfócito B como APC", "37; monitoria P1 aula 5", "central", "consultas 'B cells antigen presenting' só no Histology genérico (15/10 noite).", EP,
    "Azul: monitoria P1 aula 5 (“APC incapaz de fagocitar, somente de endocitar”). Ajuste 15/10 noite.",
    extra="- This lets a B cell show its specific antigen to the helper T cell that will activate it"),
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
    {1: Z}, E_, "Reconhecimento define o subtipo", "64; 65; 21", "central", NAO, EP, "Azul: lâminas 21, 64–65; os subtipos são da aula 45 (revisão 15/10).",
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
   ("reconhecimento", "sh-1791743340632", "a-bcr-tcr", "sh-1791625424481", "sh-1791625424657"),
   ("APC", "b-cd4-regente", "b-apc", "sh-1791625426408", "b-drenagem", "sh-1791625425333", "b-imatura", "b-pdc"),
   ("MHC", "ak-hla", "ak-hla-i", "ak-hla-ii", "ak-nucleadas", "ak-apc-ii", "c-codominante", "c-polimorfismo", "ak-fenda-i", "ak-fenda-ii", "c-estrutura", "c-ancoras", "sh-1791625424832", "ak-superantigeno"),
   ("processamento", "sh-1791625426657", "sh-1791625426833", "d-sem-peptideo", "d-tumor", "sh-1791625427059", "sh-1791625427233", "d-clip", "sh-1791625427358", "sh-1791625427531", "d-cruzada-por-que"),
   ("ativação do T", "sh-1791625428408", "sh-1791625428533", "e-terceiro", "e-adesao", "e-dc-th"),
 ],
 "exemplos": ["gota", "silicose", "obesidade e microbiota", "COVID-19 e DC plasmocitoide", "transplante de medula"],
 "outras_aulas": [("ativação de T", "45"), ("reconhecimento inato", "08"), ("inflamação", "38")],
}
_M = "Completude 15/10 (auditoria): bloco 9–27 reaberto por informação; mapa das vias do MHC."
CARDS.append(au("a-prr-soluveis", "Soluble <b>pattern recognition molecules</b> in plasma include C-reactive protein, C1q and {{c1::mannose-binding lectin}}",
    {1: Z}, A_, "PRR solúveis", "14", "central", NAO, EP, "Azul: lâminas 14–15 (não estava na aula 08). " + _M,
    extra="- Like other PRRs they are germline-encoded with limited specificity; they activate complement"))
_A_RECEPTORES = (au("a-receptores", ORG("<b>Recognition receptors</b> by location:<br>- soluble: complement, CRP and {{c1::antibodies}}<br>- membrane: TLRs, dectin, {{c2::BCR}} and TCR<br>- cytosolic: {{c3::NOD-like receptors}} and inflammasome"),
    G(1, 2, 3), A_, "Receptores por localização (inato × adquirido)", "23", "central", NAO, EP, "Verde: lâmina 23 (quadro inato × adquirido). " + _M,
    extra="- Antibodies and the BCR/TCR are the adaptive ones; the rest are innate"))
CARDS.append(au("a-sequencia", ORG("From antigen to effector <b>lymphocyte</b>:<br>1. {{c1::uptake}} by dendritic cells<br>2. {{c2::processing}}<br>3. presentation to lymphocytes<br>4. {{c3::clonal expansion}}<br>5. differentiation into effectors"),
    G(1, 2, 3), A_, "Reconhecimento → ativação → função efetora", "27", "central", NAO, EP, "Verde: lâmina 27, esqueleto da aula. " + _M))
CARDS.append(au("d-mapa-vias", ORG("<b>Antigen location</b> and MHC pathway:<br>- cytosol: {{c1::proteasome}} → TAP → MHC I → {{c2::CD8+}}<br>- vesicles: CLIP → HLA-DM → {{c3::MHC II}} → CD4+"),
    G(1, 2, 3), D_, "Mapa das duas vias de processamento", "50", "prova", NAO, EP, "Verde: lâminas 50–59; prova 2015 P2 7.2 e imuno-04 (vias I × II). " + _M,
    duplicacao_ok="organizador que liga os cards de proteassomo, TAP, Ii/CLIP e DM"))
_M2 = "Completude 15/10: transcrição inteira inventariada (F-20261015-CLAUDE-04)."
CARDS.append(au("a-inata-adquirida", "Activated <b>T and B cells</b> feed back on innate immunity, as their cytokines and {{c1::antibodies}} make phagocytes and complement far more effective",
    G(1), A_, "Inata ↔ adquirida dependem uma da outra", "22", "central", NAO, EP, "Verde: lâmina 22 e transcrição (‘não existe uma sem a outra’); card de conexão. " + _M2,
    extra="- In turn, innate recognition tells the lymphocyte what was found and steers its subtype"))
CARDS.append(sh(1791625423282, "azul", C_, "Seleção positiva: reconhecer MHC próprio", "48", "Azul: transcrição (restrição ao MHC nasce no timo); viva na aula 45. " + _M2))
CARDS.append(sh(1791625423683, "azul", C_, "Seleção negativa: autorreativos eliminados", "48", "Azul: transcrição; viva na aula 45. " + _M2))
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    _x_ = {"a-sequencia": "- Clonal expansion makes many identical copies of the few T cells that recognized the antigen",
           "d-mapa-vias": "- Cross-presentation lets dendritic cells send ingested antigen to MHC I as well"}.get(_c_["key"])
    if _x_: _c_["extra"] = _x_
# Ajuste 15/10 noite, parte 2 (F-20261015-CLAUDE-05): lâminas 14–18, 34–36, 41–47, 51–58 e 63–64 relidas contra a apostila
# guia (Aula 5) e a monitoria P1 (aula 5). Cards de reconhecimento inato da 08 e de Th1/Th2 da 45 associados (mesma nota).
_M3 = "Ajuste 15/10 noite: lâmina retomada na aula; card vivo associado (F-20261015-CLAUDE-05)."
_AP = "Azul: apostila guia Aula 5 (cap. 4–5) e lâmina; ajuste 15/10 noite (F-20261015-CLAUDE-05)."
CARDS += [
 sh(1791780342851, "verde", A_, "PRR reconhecem PAMP", "14", "Verde: lâmina 14 (linhagem germinativa, especificidade limitada). " + _M3),
 sh(1792029609563, "azul", A_, "Famílias de PRR e localização", "14", "Azul: lâmina 14 (solúveis, membrana, citoplasma). " + _M3),
 sh(1791743339358, "azul", A_, "TLR4 + CD14 reconhecem LPS", "16", "Azul: lâminas 14 e 16. " + _M3),
 sh(1791743339740, "verde", A_, "Inflamassoma", "17", "Verde: lâmina 17. " + _M3),
 sh(1792029615110, "azul", A_, "Inflamassoma: sinal 1 de priming", "18", "Azul: lâmina 18 (sinal 1 e 2). " + _M3),
 sh(1791743339860, "verde", A_, "Inflamassoma → IL-1β e IL-18", "18", "Verde: lâmina 18. " + _M3),
 au("b-apc-resposta", ORG("What each <b>APC</b> starts when it presents to a T cell:<br>1. dendritic cell: activation of {{c1::naive}} T cells<br>2. macrophage: {{c2::cell-mediated}} immunity<br>3. B cell: {{c3::humoral}} immunity"),
    G(1, 2, 3), B_, "Tipos de APC × resposta", "35", "central", "consulta APC macrophage B cell response sem quadro (15/10 noite).", EP,
    "Verde: quadro da lâmina 35 (captação → apresentação → resposta) e apostila guia Aula 5 cap. 3; ajuste 15/10 noite.",
    duplicacao_ok="b-apc dá as três APCs; este dá o que cada uma provoca",
    extra="- Effector T cells activate the macrophage that presented to them, and help the B cell make antibodies"),
 sh(1791625425478, "rosa", B_, "Langerhans = DC da epiderme", "32", "Rosa: lâmina 32 (CD imatura na epiderme) e apostila; viva na 45. " + _M3),
 au("b-dc-convencional", "Most <b>dendritic cells</b> in tissues and lymphoid organs are {{c1::conventional}} dendritic cells, which capture antigen and present it to T cells",
    {1: Z}, B_, "DC convencional × plasmocitoide", "36", "central", "consulta 'conventional dendritic' sem card (15/10 noite).", EP, _AP,
    extra="- Plasmacytoid DCs are fewer and specialize in type I interferon"),
 au("c-cromossomo", "Human <b>MHC (HLA)</b> genes lie on chromosome {{c1::6}}",
    {1: R}, C_, "HLA no cromossomo 6", "41", "lateral", "consulta 'chromosome 6' MHC sem card (15/10 noite).", EP, "Rosa: apostila guia Aula 5 cap. 1.",
    extra="- The class I, II and III regions sit side by side in this locus"),
 au("c-classe-iii", "Between the class I and class II loci, the <b>MHC class III</b> region encodes {{c1::complement}} proteins (C2, C4, factor B) and TNF",
    {1: R}, C_, "Região classe III", "41", "lateral", "consulta 'class III' complement sem card (15/10 noite).", EP, "Rosa: mapa do locus na lâmina 41 e apostila cap. 1.",
    extra="- The class II region also holds genes for TAP and proteasome subunits"),
 au("c-poligenia", "Each person expresses several different class I molecules (HLA-A, -B, -C) because the <b>MHC</b> is {{c1::polygenic}}",
    {1: Z}, C_, "Poligenia", "43", "central", "consulta polygenic sem card de MHC (15/10 noite).", EP, "Azul: lâmina 43 (polimorfismo × poligenia) e monitoria P1 aula 5 (‘polimórfico, poligênico e codominante’).",
    extra="- Polymorphism (many alleles in the population) and polygeny (several genes) together widen the peptides a person can present"),
 au("c-polimorfismo-porque", "Because <b>MHC alleles</b> vary so much, some members of a population can always present a given microbial {{c1::peptide}}",
    {1: Z}, C_, "Por que o MHC é polimórfico", "43", "central", NAO, EP, "Azul: apostila guia cap. 4 (o polimorfismo protege a população).",
    extra="- Polymorphic residues sit in the cleft floor and walls, so they change which peptides bind and how the TCR sees them"),
 au("c-fenda-dominios", "The <b>peptide cleft</b> is formed by the α1 and α2 domains in class I MHC and by the {{c1::α1 and β1}} domains in class II",
    {1: Z}, C_, "Domínios que formam a fenda", "45", "central", "consulta 'α1 and β1' cleft sem card (15/10 noite).", EP, "Azul: lâmina 45 e apostila cap. 4.",
    extra="- These domains carry the polymorphic residues; the α3 and β2 domains are constant"),
 au("c-cd8-alfa3", "<b>CD8</b> binds the invariant {{c1::α3}} domain of class I MHC, which is why CD8+ T cells respond only to class I",
    {1: R}, C_, "CD8 liga α3; CD4 liga β2", "46; 47", "lateral", "consulta CD8 α3 sem card (15/10 noite).", EP, "Rosa: lâminas 46–47 e apostila cap. 4.",
    extra="- CD4 binds the β2 domain of class II in the same way"),
 au("d-ubiquitina", "<b>Cytosolic proteins</b> are tagged with {{c1::ubiquitin}} before the proteasome cuts them into peptides for class I MHC",
    {1: Z}, D_, "Ubiquitina marca para o proteassomo", "51; 53", "central", "consulta ubiquitin proteasome MHC sem card (15/10 noite).", EP, _AP,
    extra="- The same ubiquitin–proteasome pathway clears the cell's own misfolded proteins"),
 au("d-tapasina", "In the ER, {{c1::tapasin}} tethers empty <b>class I MHC</b> molecules to TAP so they load the peptides it pumps in",
    {1: Z}, D_, "Tapasina", "54", "central", "consultas tapasin/calnexin sem card (15/10 noite).", EP, "Azul: lâmina 54 e apostila cap. 5.",
    extra="- Calnexin and calreticulin are chaperones that fold the α chain and join it to β2-microglobulin"),
 au("d-evasao-viral", "Many <b>viruses</b> evade CD8+ T cells by blocking {{c1::TAP}} or retaining class I MHC in the ER",
    {1: Z}, D_, "Evasão viral da via classe I", "54", "central", "AnKing só tem Nef do HIV (específico); 15/10 noite.", [1502069364234, 1518053116398],
    "Azul: apostila cap. 5 (estratégias virais) e monitoria P1 aula 5 (vírus inibe a estabilização do MHC I).",
    extra="- A cell that loses class I MHC becomes a target for NK cells"),
 au("d-hla-do", "{{c1::HLA-DO}} inhibits <b>HLA-DM</b>, restraining the exchange of CLIP for peptides in class II MHC",
    {1: R}, D_, "HLA-DO", "58; 59", "lateral", NAO, EP, "Rosa: lâminas 58–59.",
    extra="- HLA-DM is the exchanger; DO is its brake"),
 sh(1791625430082, "azul", E_, "CD40–CD40L na sinapse", "63", "Azul: lâmina 63 e monitoria P1 aula 5 (CD40/CD40L); viva na 45. " + _M3),
 sh(1791625422408, "verde", E_, "IL-12 → Th1", "64", "Verde: lâmina 64 (IL-12). " + _M3),
 sh(1791625422657, "verde", E_, "Th1 ativa macrófago", "64", "Verde: lâmina 64 (IFN-γ ativa macrófago). " + _M3),
 sh(1791625432007, "verde", E_, "Th2 recruta eosinófilos", "64", "Verde: lâmina 64 (IL-4, IL-5; eosinófilo, mastócito, IgE). " + _M3),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
CARDS += [
 au("c-so-peptideos", "<b>MHC molecules</b> bind only {{c1::peptides}}, so MHC-restricted T cells respond only to protein antigens",
    {1: Z}, C_, "MHC só liga peptídeos", "44", "central", NAO, EP, "Azul: Abbas Básica cap. 3 (ligação de peptídeos ao MHC); lâminas 39 e 44.",
    extra="- B cells, by contrast, recognize polysaccharides, lipids and nucleic acids too"),
 au("d-imunodominancia", "Of the many <b>peptides</b> cut from a protein, only the few that fit a person's MHC are presented, the {{c1::immunodominant}} peptides",
    {1: R}, D_, "Peptídeos imunodominantes", "44", "lateral", NAO, EP, "Rosa: Abbas Básica cap. 3 e apostila guia cap. 5 (só um ou dois peptídeos ligam).",
    extra="- A person whose MHC binds no peptide of an antigen does not respond to it"),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
