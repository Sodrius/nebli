#!/usr/bin/env python3
"""Bateria do backend de coleção — roda numa coleção descartável, sem AnkiWeb.

    python flashcards/scripts/testar_backend_anki.py

Exercita todas as ações que os scripts do NEBLI usam, no formato exato do
AnkiConnect. Não toca na coleção real nem na rede (NEBLI_ANKI_OFFLINE=1).
"""
import os
import sys
import tempfile

TMP = tempfile.mkdtemp(prefix="nebli-anki-teste-")
os.environ.update(NEBLI_ANKI_DIR=TMP, NEBLI_ANKI_OFFLINE="1",
                  NEBLI_ANKI_BACKEND="collection", NEBLI_ANKI_AUTOSYNC="0")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nebli_anki import call, backend  # noqa: E402

ok, fail = 0, 0


def check(nome, cond, detalhe=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"  ok   {nome}" + (f" — {detalhe}" if detalhe else ""))
    else:
        fail += 1
        print(f"  FALHA {nome} — {detalhe}")


print(f"backend: {backend()}  |  coleção descartável: {TMP}\n")

check("version", call("version") == 6)
basics = [m for m in call("modelNames") if m.lower().startswith("basic")]
check("modelNames", bool(basics), f"{len(call('modelNames'))} modelos")
MODEL = basics[0]
FIELDS = call("modelFieldNames", modelName=MODEL)
check("modelFieldNames", len(FIELDS) >= 2, str(FIELDS))
check("modelTemplates", bool(call("modelTemplates", modelName=MODEL)))

DECK = "NEBLI::teste::aula-fake"
did = call("createDeck", deck=DECK)
check("createDeck", isinstance(did, int) and DECK in call("deckNames"))

nid = call("addNote", note={"deckName": DECK, "modelName": MODEL,
                            "fields": {FIELDS[0]: "Difusão facilitada",
                                       FIELDS[1]: "GLUT, a favor do gradiente"},
                            "tags": ["NEBLI::teste"]})
check("addNote", isinstance(nid, int), f"nid={nid}")
check("addNote dedup", call("addNote", note={
    "deckName": DECK, "modelName": MODEL,
    "fields": {FIELDS[0]: "Difusão facilitada", FIELDS[1]: "x"}}) is None,
    "duplicata barrada como no AnkiConnect")

nids = call("addNotes", notes=[{"deckName": DECK, "modelName": MODEL,
                                "fields": {FIELDS[0]: f"Conceito {i}",
                                           FIELDS[1]: f"mecanismo {i}"},
                                "tags": ["NEBLI::teste"]} for i in range(3)])
check("addNotes", all(isinstance(x, int) for x in nids), f"{len(nids)} notas")

info = call("notesInfo", notes=[nid])[0]
check("notesInfo formato", info["noteId"] == nid
      and info["fields"][FIELDS[0]]["value"] == "Difusão facilitada"
      and info["fields"][FIELDS[0]]["order"] == 0
      and "NEBLI::teste" in info["tags"] and info["modelName"] == MODEL)
check("notesInfo expõe guid", bool(info.get("guid")),
      "casamento card-a-card vira identidade, não texto bruto")

call("updateNoteFields", note={"id": nid, "fields": {FIELDS[1]: "GLUT1-4, saturável"}})
check("updateNoteFields",
      call("notesInfo", notes=[nid])[0]["fields"][FIELDS[1]]["value"] == "GLUT1-4, saturável")

call("addTags", notes=[nid], tags="NEBLI::glicose extra::tag")
check("addTags", "NEBLI::glicose" in call("notesInfo", notes=[nid])[0]["tags"])
call("removeTags", notes=[nid], tags="extra::tag")
check("removeTags", "extra::tag" not in call("notesInfo", notes=[nid])[0]["tags"])

check("findNotes", len(call("findNotes", query="tag:NEBLI::teste")) == 4)
check("findNotes acentuado", call("findNotes", query="Difusão") == [nid])
cids = call("findCards", query=f"nid:{nid}")
check("findCards", len(cids) == 1)
check("cardsFromNotes", call("cardsFromNotes", notes=[nid]) == cids)
check("cardsToNotes", call("cardsToNotes", cards=cids) == [nid])

c = call("cardsInfo", cards=cids)[0]
check("cardsInfo formato", c["cardId"] == cids[0] and c["note"] == nid
      and c["deckName"] == DECK and "queue" in c and "flags" in c)

call("suspend", cards=cids)
check("suspend", call("areSuspended", cards=cids) == [True])
call("unsuspend", cards=cids)
check("unsuspend/areSuspended", call("areSuspended", cards=cids) == [False])

call("setFlag", cards=cids, flag=1)
check("setFlag", call("cardsInfo", cards=cids)[0]["flags"] & 7 == 1)
call("setSpecificValueOfCard", card=cids[0], keys=["flags"], newValues=[0],
     warning_check=True)
check("setSpecificValueOfCard", call("cardsInfo", cards=cids)[0]["flags"] == 0,
      "zerar bandeira com inteiro (o bug de 2026-07-04)")

DST = "NEBLI::UC02::P3::Bioquímica::Aula Teste"
call("createDeck", deck=DST)
call("changeDeck", cards=cids, deck=DST)
check("changeDeck", call("cardsInfo", cards=cids)[0]["deckName"] == DST)

png = (b"\x89PNG\r\n\x1a\n" + b"\x00" * 40)
import base64  # noqa: E402
nome = call("storeMediaFile", filename="nebli-teste.png",
            data=base64.b64encode(png).decode())
check("storeMediaFile", isinstance(nome, str), nome)
check("retrieveMediaFile",
      base64.b64decode(call("retrieveMediaFile", filename=nome)) == png)
check("retrieveMediaFile ausente",
      call("retrieveMediaFile", filename="nao-existe.png") is False)

cfg = call("getDeckConfig", deck=DST)
check("getDeckConfig", isinstance(cfg, dict) and "new" in cfg)
cfg["new"]["perDay"] = 15
check("saveDeckConfig", call("saveDeckConfig", config=cfg) is True)
check("saveDeckConfig persistiu",
      call("getDeckConfig", deck=DST)["new"]["perDay"] == 15, "ritmo NEBLI 15/dia")

res = call("multi", actions=[{"action": "version"},
                             {"action": "deckNames"},
                             {"action": "acaoQueNaoExiste"}])
check("multi", res[0] == 6 and isinstance(res[1], list)
      and isinstance(res[2], dict) and "error" in res[2])

apkg = os.path.join(TMP, "Aula Teste.apkg")
check("exportPackage", call("exportPackage", deck=DST, path=apkg) is True
      and os.path.getsize(apkg) > 0, f"{os.path.getsize(apkg)} bytes")

check("getNumCardsReviewedByDay", isinstance(call("getNumCardsReviewedByDay"), list))

try:
    call("guiCurrentCard")
    check("guiCurrentCard barrado", False)
except RuntimeError as e:
    check("guiCurrentCard barrado", "sem o Anki aberto" in str(e))
try:
    call("acaoInventada")
    check("ação desconhecida barrada", False)
except RuntimeError as e:
    check("ação desconhecida barrada", "não implementada" in str(e))
try:
    call("deleteDecks", decks=[DECK])
    check("deleteDecks exige cardsToo", False)
except RuntimeError as e:
    check("deleteDecks exige cardsToo", "cardsToo" in str(e))

call("deleteNotes", notes=nids)
check("deleteNotes", len(call("findNotes", query="tag:NEBLI::teste")) == 1)
call("deleteDecks", decks=[DECK], cardsToo=True)
check("deleteDecks", DECK not in call("deckNames"))

print(f"\n{ok} ok, {fail} falha(s)")
sys.exit(1 if fail else 0)
