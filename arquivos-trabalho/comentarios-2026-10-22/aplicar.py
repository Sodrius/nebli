#!/usr/bin/env python3
"""Comentários pendentes de 22/10/2026 (UC03, UC08, UC19) + negrito em todo autoral NEBLI (gate F-20261022-CLAUDE-04).
Os comentários da UC07 entram no trabalho de completar a UC07; os pedidos de deck inteiro vão para a fila (NEBLI_Resposta)."""
import base64, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki, escrita, em_tela

A = Anki()
S = Path("/private/tmp/claude-501/-Users-davisousa-NEBLI/6e130a2f-b295-429e-907c-f0758923fe66/scratchpad/com")
MARK = "CORRIGIDO, 22, 10, 26."
img = lambda f, w=None: f'<img src="{f}"' + (f' width="{w}"' if w else "") + ">"

NEW = {
    1790981518578: {"Extra": "- Esophageal branch of azygos → azygos → IVC / SVC<br>- Left gastric → portal vein<br>- If ruptured, manifests as painless bleeding, can cause massive hematemesis<br>" + img("paste-35381940584451.jpg", 520)},
    1790999272782: {"Text": "In smooth muscle, {{c1::<b>Rho kinase</b>}} inhibits myosin light-chain phosphatase, so the same Ca<sup>2+</sup> produces more force",
                    "Extra": "- This is Ca<sup>2+</sup> sensitization: myosin stays phosphorylated longer and keeps tone without more Ca<sup>2+</sup><br>- PKC does the same by phosphorylating CPI-17, an inhibitor of the phosphatase<br>" + img("nebli-uc08-fi08-p06f.png", 460)},
    1791629590097: {"Extra": "- B-1 cells are innate-like B cells of the peritoneal and pleural cavities that make natural IgM against polysaccharides without T-cell help<br>- Conventional B-2 cells are CD5 negative and form germinal centers with T-cell help"},
    1791629592997: {"Extra": "- Signal 1 is TCR–MHC II; signal 2 is costimulation<br>- CD28: costimulatory receptor of T cells<br>- CD80/CD86 (B7): ligands of CD28, expressed by APCs<br>- CD40: receptor on B cells and other APCs<br>- CD40L (CD154): ligand of CD40, mainly on activated CD4+ T cells"},
    1791629593971: {"Extra": "- Chemokine receptors guide both cells to the same region: the T cell toward the follicle, the B cell toward the T-cell zone<br>" + img("a10fc17517aad74736e4bb8bd3204683.webp", 460)},
    1791630905768: {"Extra": "- Small yeasts (2–4 µm) packed inside macrophages, smaller than a red blood cell<br>- Seen with Giemsa or Gomori-Grocott silver stain<br>" + img("7b3d0402fd492edfab022f362531dc53.jpg", 460)},
    1791762419700: {"Text": "<b>Loratadine</b> acts as an {{c1::<b>inverse agonist</b>}} at H1 receptors, which signal even without histamine",
                    "Extra": "- An inverse agonist lowers the constitutive (ligand-free) activity of the receptor below baseline<br>- A neutral antagonist only blocks the agonist and leaves the baseline unchanged"},
    1791762421022: {"Text": "Through the same receptor, a {{c1::<b>biased</b>}} agonist activates G-protein signaling more than β-arrestin signaling",
                    "Extra": "- A receptor can signal through more than one pathway; a biased agonist selects one, which may separate the wanted effect from side effects<br>- β-arrestin also drives receptor desensitization and internalization"},
    1791826292220: {"Text": img("fa01-g-antagonismo-nao-competitivo.png") + "<br>Which type of antagonism lowers the maximal response even at high agonist doses? {{c1::<b>Noncompetitive</b>}}",
                    "Extra": "- The antagonist removes functional receptors, so adding agonist cannot restore the maximum (Emax falls)<br>- A competitive antagonist instead shifts the curve to the right and the maximum is reached again"},
    1791826294319: {"Text": img("fa01-g-quantal.png", 460) + "<br>On population dose curves, the therapeutic index is {{c1::<b>TD50</b>}} / {{c2::<b>ED50</b>}}",
                    "Extra": "- ED50: dose that gives the therapeutic effect in half of the individuals; TD50: dose that is toxic in half<br>- The farther apart the curves, the larger the index and the safer the drug"},
    1792083296387: {"Text": "In paracoccidioidomycosis, protection depends on {{c1::<b>cell-mediated</b>}} immunity",
                    "Extra": "- Th1 IFN-γ activates macrophages that form granulomas and kill the yeast; antibodies do not reach the fungus inside cells<br>- A weak Th1 response allows the severe juvenile form"},
    1792175890985: {"Extra": "- Few yeasts are seen; silver (Grocott) stain shows them best<br>" + img("b42863726b6f038acfb7d737d5313991.webp", 420)},
    1792176896207: {"Extra": "- Inhaled arthroconidia become spherules full of endospores in the lung<br>" + img("e026c380fb9c3cc6a2c51fdeb7b23d4d.jpg", 420)},
}
RESP = {
    1791627546552: "Na fila (22/10): refazer a 46 Expressão gênica em eucariotos I com o gate de profundidade e autorais revisados contra os exemplares.",
    1791762418150: "Na fila (22/10): auditar repetição na FA01 e unir os cards que cobram a mesma coisa.",
    1792117360419: "Na fila (22/10): usar a 09 como referência para refazer os decks da P1 da UC03 com o gate de profundidade, começando pela Imuno.",
    1792166988890: "Na fila (22/10): retirar o excesso de clínica do deck 51 (teto 7%), mantendo a base.",
    1792240186582: "Na fila (22/10): completar a 08 Reconhecimento imune inato e conferir os outros decks da P1.",
    1790999833029: "O card 2 sumiu porque a edição deixou as duas lacunas em c1: o c2 ficou vazio. Removido o cartão vazio (22/10).",
    1790981525201: "Versão editada anotada nos exemplares (22/10).", 1791023298343: "Versão editada anotada nos exemplares (22/10).",
    1791762415623: "Versão editada anotada nos exemplares (22/10).",
}
CLOZE = re.compile(r"\{\{(c\d+)::(.*?)(::[^}]*)?\}\}", re.S)
def bold(m):
    if re.search(r"<(?:b|strong)>", m.group(2), re.I): return m.group(0)
    corpo = m.group(2).strip()
    return "{{" + m.group(1) + "::<b>" + corpo + "</b>" + (m.group(3) or "") + "}}"

# diafragma: organizador novo (pedido no comentário de 1790972065310)
DIAF = {"Text": "<b>Structures crossing the diaphragm</b>:<br>- T8: {{c1::<b>IVC</b>}}<br>- T10: {{c2::<b>esophagus</b>}} and vagus nerves<br>- T12: {{c3::<b>aorta</b>}}, thoracic duct and azygos vein",
        "Extra": "- “I ate ten eggs at twelve”: IVC T8, esophagus T10, aorta T12<br>- Each passes through its own opening: caval foramen, esophageal hiatus and aortic hiatus"}
DECK_AN01 = "NEBLI::UC08::P1::Anatomia::Esôfago, estômago e intestino delgado"

data = base64.b64encode((S / "fa01-g-antagonismo-nao-competitivo.png").read_bytes()).decode()
current = em_tela(A); feitos, pulados, negrito = [], [], []
with escrita(A, "comentários 22/10 + negrito nos autorais", sync=False):
    A("storeMediaFile", filename="fa01-g-antagonismo-nao-competitivo.png", data=data)
    for nid, fields in NEW.items():
        if nid in current: pulados.append(nid); continue
        A("updateNoteFields", note={"id": nid, "fields": fields}); A("addTags", notes=[nid], tags="NEBLI::feedback::comentarios-20261022")
        feitos.append(nid)
    nid_diaf = A("addNote", note={"deckName": DECK_AN01, "modelName": "NEBLI AnKing independente - v3", "fields": DIAF,
                                  "tags": ["NEBLI::2026-uc08-anatomia-01-esofago-estomago-delgado", "NEBLI::origem::Autoral", "NEBLI::escopo::aula",
                                           "NEBLI::objetivo::C-hiato-juncao", "NEBLI::feedback::comentarios-20261022"],
                                  "options": {"allowDuplicate": False}})
    cids = A("findCards", query=f"nid:{nid_diaf}"); A("suspend", cards=cids)
    # negrito em todo autoral NEBLI que ainda não tem (gate novo)
    ids = A("findNotes", query='tag:NEBLI::origem::Autoral "deck:NEBLI*"')
    for n in A("notesInfo", notes=ids):
        nid = n["noteId"]
        if nid in current or "Text" not in n["fields"]: continue
        old = n["fields"]["Text"]["value"]; new = CLOZE.sub(bold, old)
        if new != old:
            A("updateNoteFields", note={"id": nid, "fields": {"Text": new}}); negrito.append(nid)
    if negrito: A("addTags", notes=negrito, tags="NEBLI::feedback::negrito-20261022")
    # marcar comentários
    for nid in list(NEW) + [1790972065310]:
        if nid in pulados: continue
        n = A("notesInfo", notes=[nid])[0]; old = n["fields"]["NEBLI_Comentario"]["value"].rstrip()
        A("updateNoteFields", note={"id": nid, "fields": {"NEBLI_Comentario": old + "<br>" + MARK,
                                                           "NEBLI_Resposta": "Corrigido em 22/10/2026." + (f" Organizador novo: nota {nid_diaf} (suspensa)." if nid == 1790972065310 else "")}})
        A("addTags", notes=[nid], tags="NEBLI_comentario::respondido"); A("removeTags", notes=[nid], tags="NEBLI_comentario::pendente")
    for nid, r in RESP.items():
        if nid in current: pulados.append(nid); continue
        A("updateNoteFields", note={"id": nid, "fields": {"NEBLI_Resposta": r}})
print(json.dumps({"alterados": feitos, "diafragma": nid_diaf, "negrito": len(negrito), "pulados_em_tela": pulados}))
