"""Rodada 01/11 (b): comentários e comandos de Davi; mesmo padrão do aplicar.py da rodada anterior, sem tocar no Tab."""
import base64, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki, escrita, em_tela
AQUI = Path(__file__).resolve().parent
IMG = Path("/private/tmp/claude-501/-Users-davisousa/e83cc7a6-ca8e-4f3e-bd70-793b69cb23f9/scratchpad/img")
ORG = '<div data-nebli-organizacao="true">'
CAMPOS = {
 1792695019915: {"Text": ORG + "<b>Influenza</b> and sialic acid:<br>{{c1::Hemagglutinin::H…}}: <b>binds</b> it to enter<br>{{c1::Neuraminidase::N…}}: <b>cleaves</b> it to leave</div>",
                 "Extra": "Neutralizing antibodies block hemagglutinin.<br>Oseltamivir blocks neuraminidase, so new virions stay stuck to the cell."},
 1792695022241: {"Text": ORG + "Viruses with an <b>early/late gene program</b>:<br>Early mRNAs: {{c1::polymerase::p…}}, <b>copies</b> the genome<br>Late mRNAs: {{c1::capsid::c…}} proteins, <b>package</b> it</div>",
                 "Extra": "The genome must be copied before there is anything to package.<br>Many RNA viruses express their genes all at once."},
 1792695033836: {"Text": ORG + "<b>(+) RNA virus cycle</b>, in the cytoplasm:<br>- genome translated as one {{c1::polyprotein::p…}}<br>- viral {{c1::protease::p…}} frees the RNA-dependent RNA polymerase<br>- polymerase copies a {{c1::negative::n…}} strand<br>- that strand templates new genomes</div>",
                 "Extra": "The same (+) RNA is mRNA and genome, so purified genome alone is infectious.<br>Protease inhibitors for hepatitis C act on the second step."},
 1792695055945: {"Text": "The <b>envelope</b> of a budding virus is a patch of host {{c1::membrane}} carrying viral glycoproteins",
                 "Extra": "Most viruses bud from the plasma membrane; herpesviruses take their envelope from the nuclear membrane.<br>Enveloped viruses leave as they bud, so they do not accumulate inside the cell."},
 1792695057292: {"Text": ORG + "<b>Why antivirals are limited</b>:<br>Host enzymes do the work: few {{c1::targets::t…}}<br>Each family differs: narrow {{c1::spectrum::s…}}<br>{{c2::Latent::L…}} virus: nothing to block<br>Tissue injury builds fast: start {{c2::early::e…}}</div>",
                 "Extra": "So most antivirals act on one virus, as oseltamivir for influenza and acyclovir for herpes.<br>Oseltamivir helps most within 48 h of symptoms."},
 1793199678427: {"Extra": "Without virus, red cells sink into a button. With virus, they form a lattice.<br>The titer is the highest dilution that still agglutinates; it counts infectious and noninfectious particles alike.<br><img src=\"mb60-titulo-ha-slide44-20261101.png\" style=\"width:100%;max-width:720px;height:auto;display:block;margin:18px auto\">"},
}
VISTO = {1791628675571}
SOBRA = {1792695019915: [1], 1792695022241: [1], 1792695033836: [1, 2]}  # ords que ficaram sem lacuna
FLAG = {"verde": 3, "azul": 4, "rosa": 5}; RANK = {3: 3, 4: 2, 5: 1}
A = Anki()
R = json.loads((AQUI / "RODADA.json").read_text())
nids = sorted({i["nid"] for i in R["itens"]} | set(CAMPOS))
antes = A("notesInfo", notes=nids)
(AQUI / "backup-antes-aplicar.json").write_text(json.dumps(antes, ensure_ascii=False, indent=1))
rec = []
with escrita(A, "rodada de comentários 01/11 (b)", sync=False):
    tela = set(em_tela(A))
    A("storeMediaFile", filename="mb60-titulo-ha-slide44-20261101.png", data=base64.b64encode((IMG / "mb60-titulo-ha-slide44-20261101.png").read_bytes()).decode())
    for n in antes:
        nid = n["noteId"]
        if nid in tela: rec.append({"nid": nid, "pulado": True}); continue
        if nid in CAMPOS: A("updateNoteFields", note={"id": nid, "fields": CAMPOS[nid]})
        cards = A("cardsInfo", cards=n["cards"])
        sobra = [c["cardId"] for c in cards if c["ord"] in SOBRA.get(nid, [])]
        if sobra: A("suspend", cards=sobra); A("addTags", notes=[nid], tags="NEBLI::lacuna-fundida::2026-11-01")
        cores = [FLAG[t.split("::")[-1]] for t in n["tags"] if t.startswith("NEBLI::cor::") and t.split("::")[-1] in FLAG]
        volta = max(cores, key=RANK.get) if cores else 0
        for c in cards:
            if c["flags"] == 1: A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[volta], warning_check=True)
        cmd = [t for t in n["tags"] if t.startswith("NEBLI::comando::")]
        if cmd: A("removeTags", notes=[nid], tags=" ".join(cmd))
        atual = n["fields"]["NEBLI_Comentario"]["value"].rstrip()
        marca = "VISTO" if nid in VISTO else "CORRIGIDO"
        A("updateNoteFields", note={"id": nid, "fields": {"NEBLI_Comentario": atual + ("<br>" if atual else "") + f"{marca}, 01, 11, 26."}})
        rec.append({"nid": nid, "campos": nid in CAMPOS, "sobra_suspensa": sobra, "comandos": cmd})
(AQUI / "recibo-aplicar.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1)); print(rec)
