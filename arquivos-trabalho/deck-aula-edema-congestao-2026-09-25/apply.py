"""Aplica plan.json do piloto Edema (Claude, 25/09/2026). Uso: python apply.py check|apply"""
import hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from anki import call

ROOT = Path(__file__).resolve().parent
LOCK = ROOT.parent / "ANKI-ESCRITA.lock"
V3 = "NEBLI AnKing independente - v3"
PLAN = json.loads((ROOT / "plan.json").read_text(encoding="utf-8"))
DECK, LESSON = PLAN["target_deck"], PLAN["lesson_id"]
TAG = f"NEBLI::{LESSON}"
sys.stdout.reconfigure(encoding="utf-8")

def now(): return datetime.now(timezone.utc).isoformat()
def digest(o): return hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
def plain(n): return {k: v["value"] for k, v in n["fields"].items()}
def studied(c): return c.get("reps", 0) > 0 or c.get("type", 0) != 0
def idtag(e): return f"NEBLI::source::nid-{e['source_nid']}" if e["source_nid"] else f"NEBLI::author::edema-{e['key']}"

def full_fields(model, e):
    f = {name: "" for name in call("modelFieldNames", modelName=model)}
    f.update(e["fields"]); return f

def check():
    issues = []
    if call("getActiveProfile") != PLAN["profile"]: issues.append("perfil mudou")
    if LOCK.exists(): issues.append(f"lock existente: {LOCK.read_text(encoding='utf-8')}")
    deck_cards = call("cardsInfo", cards=call("findCards", query=f'"deck:{DECK}"'))
    deck_notes = {c["note"] for c in deck_cards}
    expected = {r["nid"] for r in PLAN["remove"]} | {e["existing_nid"] for e in PLAN["entries"] if e["action"] == "update"}
    if deck_notes != expected: issues.append(f"deck mudou desde o plano: {sorted(deck_notes ^ expected)}")
    if any(studied(c) for c in deck_cards): issues.append("há card estudado no deck")
    for e in PLAN["entries"]:
        if e["source_nid"]:
            src = call("notesInfo", notes=[e["source_nid"]])[0]
            if digest(plain(src)) != e["source_fields_hash"]: issues.append(f"fonte mudou: {e['key']}")
        found = [n for n in call("findNotes", query=f'tag:"{idtag(e)}"') if n not in expected]
        if found: issues.append(f"cópia fora do deck já existe: {e['key']} → {found}")
    for a in PLAN["associate"]:
        cs = call("cardsInfo", cards=a["cards"])
        if len(cs) != len(a["cards"]) or any(studied(c) for c in cs): issues.append(f"associada mudou: {a['nid']}")
        if any(c["flags"] not in (0, a["flag"]) for c in cs): issues.append(f"associada com marca pessoal: {a['nid']}")
    return issues

def apply():
    issues = check()
    if issues: sys.exit("\n".join(issues))
    LOCK.open("x", encoding="utf-8").write(json.dumps({"executor": "Claude", "aula": LESSON, "at": now()}))
    journal = ROOT / "journal.jsonl"
    def log(action, value):
        with journal.open("a", encoding="utf-8") as f: f.write(json.dumps({"at": now(), "action": action, "value": value}, ensure_ascii=False) + "\n")
    try:
        # 1. backup
        deck_nids = sorted({c["note"] for c in call("cardsInfo", cards=call("findCards", query=f'"deck:{DECK}"'))})
        before = {"notes": call("notesInfo", notes=deck_nids + [a["nid"] for a in PLAN["associate"]]),
                  "cards": call("cardsInfo", cards=call("findCards", query=f'"deck:{DECK}"') + [c for a in PLAN["associate"] for c in a["cards"]]),
                  "sources": call("notesInfo", notes=[e["source_nid"] for e in PLAN["entries"] if e["source_nid"]])}
        (ROOT / "before-apply.json").write_text(json.dumps(before, ensure_ascii=False), encoding="utf-8")
        pkg = ROOT / "backup-edema-antes-do-piloto.apkg"
        if not call("exportPackage", deck=DECK, path=str(pkg.resolve()), includeSched=True): raise RuntimeError("backup APKG falhou")
        log("backup", {"apkg": str(pkg), "sha256": hashlib.sha256(pkg.read_bytes()).hexdigest(), "notes": len(deck_nids)})
        # 2. mídia
        for src, name in PLAN["media"].items():
            call("storeMediaFile", filename=name, path=str((ROOT / src).resolve()))
        log("media", PLAN["media"])
        # 3. remoções (backup acima)
        rm = [r["nid"] for r in PLAN["remove"]]
        call("deleteNotes", notes=rm); log("deleted", rm)
        if call("notesInfo", notes=rm) and any(n.get("noteId") for n in call("notesInfo", notes=rm)): raise RuntimeError("remoção incompleta")
        # 4. criação/atualização
        results = []
        for e in PLAN["entries"]:
            tags = [TAG, f"NEBLI::objetivo::{e['objective']}", f"NEBLI::origem::{e['origin']}", idtag(e)]
            if e["action"] == "update":
                nid = e["existing_nid"]; model = call("notesInfo", notes=[nid])[0]["modelName"]
                fields = full_fields(model, e)
                call("updateNoteFields", note={"id": nid, "fields": fields}); call("addTags", notes=[nid], tags=" ".join(tags))
            else:
                fields = full_fields(V3, e)
                tags = list(dict.fromkeys(e.get("source_tags", []) + tags))
                nid = call("addNote", note={"deckName": DECK, "modelName": V3, "fields": fields, "tags": tags, "options": {"allowDuplicate": True}})
            note = call("notesInfo", notes=[nid])[0]
            if plain(note) != fields: raise RuntimeError(f"campos divergentes: {e['key']}")
            cards = call("cardsInfo", cards=note["cards"])
            if len(cards) != e["expected_cards"]: raise RuntimeError(f"contagem divergente {e['key']}: {len(cards)}")
            if any(c["deckName"] != DECK for c in cards): call("changeDeck", cards=[c["cardId"] for c in cards], deck=DECK)
            for c in cards: call("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[e["flag"]], warning_check=True)
            r = {"key": e["key"], "nid": nid, "cards": [c["cardId"] for c in cards], "flag": e["flag"], "action": e["action"], "origin": e["origin"]}
            results.append(r); log("entry", r)
        for a in PLAN["associate"]:
            call("addTags", notes=[a["nid"]], tags=f"{TAG} NEBLI::objetivo::{a['objective']}")
            for c in a["cards"]: call("setSpecificValueOfCard", card=c, keys=["flags"], newValues=[a["flag"]], warning_check=True)
            log("associated", a["nid"])
        # 5. verificação por leitura
        cards = call("cardsInfo", cards=call("findCards", query=f'"deck:{DECK}"'))
        exp = {c for r in results for c in r["cards"]}
        if {c["cardId"] for c in cards} != exp: raise RuntimeError("conjunto do deck ≠ plano")
        if call("findCards", query=f'"deck:{DECK}" is:suspended'): raise RuntimeError("suspenso inesperado")
        flags = {c["cardId"]: c["flags"] for c in cards}
        for r in results:
            if any(flags[c] != r["flag"] for c in r["cards"]): raise RuntimeError(f"flag divergente {r['key']}")
        lesson_sel = set(call("findCards", query=f'tag:"{TAG}"'))
        shared = {c for a in PLAN["associate"] for c in a["cards"]}
        if lesson_sel != exp | shared: raise RuntimeError(f"seleção por tag ≠ esperado: {sorted(lesson_sel ^ (exp | shared))}")
        for s in before["sources"]:
            if plain(call("notesInfo", notes=[s["noteId"]])[0]) != plain(s): raise RuntimeError(f"fonte alterada {s['noteId']}")
        missing = [n for n in PLAN["media"].values() if not call("retrieveMediaFile", filename=n)]
        if missing: raise RuntimeError(f"mídia ausente {missing}")
        receipt = {"at": now(), "lesson": LESSON, "deck": DECK, "plan_sha256": digest(PLAN), "results": results,
                   "deck_cards": len(cards), "shared_cards": sorted(shared), "selection_query": f'tag:"{TAG}"',
                   "green": sum(1 for c in cards if c["flags"] == 3) + len(shared), "blue": sum(1 for c in cards if c["flags"] == 4),
                   "removed_notes": rm, "backup_apkg": str(pkg), "sources_unchanged": True}
        (ROOT / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=1), encoding="utf-8")
        log("verified", {k: v for k, v in receipt.items() if k != "results"})
        call("sync"); log("sync", "requested")
        print(json.dumps({k: v for k, v in receipt.items() if k not in ("results", "removed_notes")}, ensure_ascii=False, indent=1))
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    if mode == "check":
        i = check(); print("\n".join(i) if i else "check OK")
    elif mode == "apply": apply()
