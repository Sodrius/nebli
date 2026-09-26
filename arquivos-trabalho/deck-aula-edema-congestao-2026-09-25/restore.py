"""Desfaz o piloto de Edema (25/09) a pedido de Davi: volta o deck ao estado de before-apply.json.

Uso: python restore.py check|apply. Guarda antes o estado do piloto (APKG + JSON).
"""
import hashlib, json, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from anki import call

ROOT = Path(__file__).resolve().parent
LOCK = ROOT.parent / "ANKI-ESCRITA.lock"
DECK = "NEBLI::UC03::P2::Patologia::Edema e congestão"
SHARED = 1790253536913
BEFORE = json.loads((ROOT / "before-apply.json").read_text(encoding="utf-8"))
RECEIPT = json.loads((ROOT / "receipt.json").read_text(encoding="utf-8"))
sys.stdout.reconfigure(encoding="utf-8")

def now(): return datetime.now(timezone.utc).isoformat()
def plain(n): return {k: v["value"] for k, v in n["fields"].items()}
before_notes = {n["noteId"]: n for n in BEFORE["notes"]}
before_cards = {(c["note"], c["ord"]): c for c in BEFORE["cards"]}
kept = {r["nid"] for r in RECEIPT["results"] if r["action"] == "update"}
pilot_new = [r["nid"] for r in RECEIPT["results"] if r["action"] in ("create", "recreate")]
readd = [n for nid, n in before_notes.items() if nid != SHARED and nid not in kept]

def check():
    issues = []
    if LOCK.exists(): issues.append(f"lock existente: {LOCK.read_text(encoding='utf-8')}")
    cards = call("cardsInfo", cards=call("findCards", query=f'"deck:{DECK}"'))
    if {c["note"] for c in cards} != kept | set(pilot_new): issues.append("deck mudou desde o piloto")
    if any(c.get("reps", 0) > 0 or c.get("type", 0) != 0 for c in cards): issues.append("há card do piloto já estudado")
    return issues

def apply():
    issues = check()
    if issues: sys.exit("\n".join(issues))
    LOCK.open("x", encoding="utf-8").write(json.dumps({"executor": "Claude", "aula": "edema-restauracao", "at": now()}))
    journal = ROOT / "restore-journal.jsonl"
    def log(a, v):
        with journal.open("a", encoding="utf-8") as f: f.write(json.dumps({"at": now(), "action": a, "value": v}, ensure_ascii=False) + "\n")
    try:
        nids = sorted(kept | set(pilot_new) | {SHARED})
        state = {"notes": call("notesInfo", notes=nids), "cards": call("cardsInfo", cards=[c for n in call("notesInfo", notes=nids) for c in n["cards"]])}
        (ROOT / "estado-do-piloto.json").write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
        pkg = ROOT / "backup-piloto-antes-de-restaurar.apkg"
        if not call("exportPackage", deck=DECK, path=str(pkg.resolve()), includeSched=True): raise RuntimeError("backup do piloto falhou")
        log("backup-piloto", {"apkg": str(pkg), "sha256": hashlib.sha256(pkg.read_bytes()).hexdigest()})
        call("deleteNotes", notes=pilot_new); log("deleted-pilot", pilot_new)
        restored = {}
        for nid in sorted(kept):
            old = before_notes[nid]
            call("updateNoteFields", note={"id": nid, "fields": plain(old)})
            now_tags = set(call("notesInfo", notes=[nid])[0]["tags"])
            extra, missing = now_tags - set(old["tags"]), set(old["tags"]) - now_tags
            if extra: call("removeTags", notes=[nid], tags=" ".join(extra))
            if missing: call("addTags", notes=[nid], tags=" ".join(missing))
            restored[nid] = nid
        for old in readd:
            new = call("addNote", note={"deckName": DECK, "modelName": old["modelName"], "fields": plain(old),
                                        "tags": old["tags"], "options": {"allowDuplicate": True}})
            restored[old["noteId"]] = new; log("readded", {"old": old["noteId"], "new": new})
        sh = before_notes[SHARED]; now_tags = set(call("notesInfo", notes=[SHARED])[0]["tags"])
        extra = now_tags - set(sh["tags"])
        if extra: call("removeTags", notes=[SHARED], tags=" ".join(extra))
        restored[SHARED] = SHARED
        # bandeiras por (nota antiga, ord)
        for old_nid, new_nid in restored.items():
            for c in call("cardsInfo", cards=call("notesInfo", notes=[new_nid])[0]["cards"]):
                want = before_cards[(old_nid, c["ord"])]["flags"]
                if c["flags"] != want: call("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[want], warning_check=True)
        # verificação
        problems = []
        for old_nid, new_nid in restored.items():
            now_n = call("notesInfo", notes=[new_nid])[0]
            if plain(now_n) != plain(before_notes[old_nid]): problems.append(f"campos {old_nid}")
            if set(now_n["tags"]) != set(before_notes[old_nid]["tags"]): problems.append(f"tags {old_nid}")
            if len(now_n["cards"]) != len(before_notes[old_nid]["cards"]): problems.append(f"cards {old_nid}")
        cards = call("cardsInfo", cards=call("findCards", query=f'"deck:{DECK}"'))
        flags = Counter(c["flags"] for c in cards)
        want_flags = Counter(c["flags"] for c in BEFORE["cards"] if c["note"] != SHARED)
        if len(cards) != 36 or flags != want_flags: problems.append(f"deck {len(cards)} cards, flags {dict(flags)} ≠ {dict(want_flags)}")
        if call("findCards", query=f'"deck:{DECK}" is:suspended'): problems.append("suspenso inesperado")
        receipt = {"at": now(), "deck_cards": len(cards), "flags": dict(flags), "mapping_old_to_new": {str(k): v for k, v in restored.items()},
                   "problems": problems, "backup_piloto": str(pkg)}
        (ROOT / "restore-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=1), encoding="utf-8")
        log("verified", {k: v for k, v in receipt.items() if k != "mapping_old_to_new"})
        if problems: raise RuntimeError("; ".join(problems))
        call("sync"); log("sync", "requested")
        print(json.dumps({k: v for k, v in receipt.items() if k != "mapping_old_to_new"}, ensure_ascii=False, indent=1))
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    if (sys.argv[1:] or ["check"])[0] == "apply": apply()
    else:
        i = check(); print("\n".join(i) if i else f"check OK — apagar {len(pilot_new)} notas do piloto, restaurar {len(kept)}, readicionar {len(readd)}")
