"""Rodada 01/11, segunda leva: quatro pendências que chegaram durante a rodada (comando escrita)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki, escrita, em_tela
AQUI = Path(__file__).resolve().parent
CAMPOS = {
 1792788314452: {"Text": "<b>Eukaryotic activators</b> bound at distant enhancers reach RNA polymerase II mainly through the {{c1::Mediator}} complex, brought close by DNA looping",
                 "Extra": "Mediator bridges the activator and the general transcription factors at the promoter.<br>Without it, enhancer signals barely change transcription."},
 1791625431133: {"Text": "After releasing <b>perforin</b> and <b>granzymes</b> into the synapse, a <b>CTL</b> detaches and kills other targets, a behavior called {{c1::serial killing}}",
                 "Extra": "The target dies by apoptosis hours later, even after the CTL has left.<br>One CTL can therefore clear many infected cells."},
 1792695022241: {"Text": "<div data-nebli-organizacao=\"true\">Viruses with an <b>early/late gene program</b>:<br>- early mRNAs make nonstructural proteins, such as the viral {{c1::polymerase}}<br>- late mRNAs make structural proteins of the {{c2::capsid}} and envelope</div>",
                 "Extra": "The genome must be copied before there is anything to package, so replication enzymes come first.<br>Many RNA viruses do not separate the phases and express their genes together."},
 1792695057292: {"Text": "<div data-nebli-organizacao=\"true\"><b>Why antivirals are limited</b>:<br>- viruses use host enzymes, so there are few virus-specific {{c1::targets}}<br>- each viral family has its own enzymes, so a drug rarely has a broad {{c1::spectrum}}<br>- {{c2::latent}} virus is not replicating, so the drug cannot reach it<br>- benefit depends on starting {{c2::early}}, before tissue injury</div>",
                 "Extra": "That is why antivirals are mostly specific to one virus, as oseltamivir for influenza or acyclovir for herpesviruses.<br>Oseltamivir helps most within 48 h of symptom onset."},
}
FLAG = {"verde": 3, "azul": 4, "rosa": 5}; RANK = {3: 3, 4: 2, 5: 1}
A = Anki(); antes = A("notesInfo", notes=list(CAMPOS))
(AQUI / "backup-antes-aplicar2.json").write_text(json.dumps(antes, ensure_ascii=False, indent=1))
rec = []
with escrita(A, "rodada de comentários 01/11, leva 2", sync=False):
    tela = set(em_tela(A))
    for n in antes:
        nid = n["noteId"]
        if nid in tela: rec.append({"nid": nid, "pulado": True}); continue
        A("updateNoteFields", note={"id": nid, "fields": CAMPOS[nid]})
        cores = [FLAG[t.split("::")[-1]] for t in n["tags"] if t.startswith("NEBLI::cor::") and t.split("::")[-1] in FLAG]
        volta = max(cores, key=RANK.get) if cores else 0
        for c in A("cardsInfo", cards=n["cards"]):
            if c["flags"] == 1: A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[volta], warning_check=True)
        cmd = [t for t in n["tags"] if t.startswith("NEBLI::comando::")]
        if cmd: A("removeTags", notes=[nid], tags=" ".join(cmd))
        atual = n["fields"]["NEBLI_Comentario"]["value"].rstrip()
        A("updateNoteFields", note={"id": nid, "fields": {"NEBLI_Comentario": atual + ("<br>" if atual else "") + "CORRIGIDO, 01, 11, 26."}})
        rec.append({"nid": nid, "flag": volta, "comandos": cmd})
(AQUI / "recibo-aplicar2.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1)); print(rec)
