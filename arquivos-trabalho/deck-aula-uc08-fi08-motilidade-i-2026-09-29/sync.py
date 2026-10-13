"""Sincroniza a aula instalada com plan.json (mesma identidade por tag de origem/autor).
Uso: sync.py <pasta-da-corrida> [--dry-run]. Atualiza notas existentes, cria as novas, remove (com backup)
apenas notas da própria aula ausentes do plano e SEM revisões; confere cards/ordinais/flags/deck; sincroniza."""
import base64, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
RUN = Path(sys.argv[1]).resolve(); DRY = "--dry-run" in sys.argv
sys.path.insert(0, str(RUN.parents[1]))
from nebli.decks import Anki, escrita

A = Anki(); plan = json.loads((RUN / "plan.json").read_text())
DECK, LESSON_TAG = plan["deck"], f'NEBLI::{plan["lesson_id"]}'
MEDIA = {"nebli-uc08-fi08-juncao-neuroefetora.jpeg": RUN.parent / "deck-aula-uc08-fi08-motilidade-i-2026-09-29" / "fontes" / "p5_img0.jpeg"}
canon = lambda d: re.sub(r" \(\d+\)", "", d)
idtag = lambda e: f'NEBLI::source::nid-{e["src"]}' if e["src"] else f'NEBLI::author::{e["tags_author"]}'
for e in plan["entries"]:
    e["tags_author"] = next((t.split("::", 2)[2] for t in e["tags"] if t.startswith("NEBLI::author::")), None)


def find(e):
    return A("findNotes", query=f'"tag:{idtag(e)}" "tag:{LESSON_TAG}"')


def main():
    live = set(A("findNotes", query=f'"tag:{LESSON_TAG}" -"deck:Referências*"'))
    wanted = {}
    for e in plan["entries"]:
        f = find(e); wanted[e["key"]] = f[0] if f else None
    stale = live - {n for n in wanted.values() if n}
    stale_info = A("notesInfo", notes=list(stale)) if stale else []
    studied = [n["noteId"] for n in stale_info if any(c["reps"] for c in A("cardsInfo", cards=n["cards"]))]
    print(f"existentes {sum(1 for v in wanted.values() if v)}, novas {sum(1 for v in wanted.values() if not v)}, remover {len(stale)} (estudadas {len(studied)})")
    if studied: raise SystemExit("Nota estudada fora do plano — reconciliar manualmente")
    if DRY: return
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = {"at": stamp, "existing": A("notesInfo", notes=[v for v in wanted.values() if v]), "removed": stale_info}
    (RUN / f"backup-sync-{stamp}.json").write_text(json.dumps(backup, ensure_ascii=False))
    j = (RUN / "journal.jsonl").open("a")
    log = lambda **k: (j.write(json.dumps({**k, "at": datetime.now(timezone.utc).isoformat()}, ensure_ascii=False) + "\n"), j.flush())
    with escrita(A, f"sync {plan['run_id']} {plan.get('version', '')}"):
        for name, path in MEDIA.items():
            if not A("retrieveMediaFile", filename=name):
                A("storeMediaFile", filename=name, data=base64.b64encode(path.read_bytes()).decode()); log(op="media", file=name)
        results = []
        for e in plan["entries"]:
            nid = wanted[e["key"]]
            if nid:
                cur = A("notesInfo", notes=[nid])[0]
                if cur["modelName"] != e["model"]:
                    A("updateNoteModel", note={"id": nid, "modelName": e["model"], "fields": e["fields"], "tags": e["tags"]}); log(op="updateNoteModel", key=e["key"], nid=nid)
                else:
                    A("updateNoteFields", note={"id": nid, "fields": e["fields"]})
                    A("removeTags", notes=[nid], tags=" ".join(t for t in cur["tags"] if t not in e["tags"])) if set(cur["tags"]) - set(e["tags"]) else None
                    A("addTags", notes=[nid], tags=" ".join(e["tags"]))
                    log(op="update", key=e["key"], nid=nid)
            else:
                nid = A("addNote", note={"deckName": DECK, "modelName": e["model"], "fields": e["fields"], "tags": e["tags"], "options": {"allowDuplicate": True}})
                log(op="addNote", key=e["key"], nid=nid)
            cards = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
            wrong = [c["cardId"] for c in cards if canon(c["deckName"]) != DECK]
            if wrong: A("changeDeck", cards=wrong, deck=DECK); log(op="changeDeck", key=e["key"], cards=wrong)
            want = {x["ord"]: x["flag"] for x in e["cards"]}
            extra = [c["cardId"] for c in cards if c["ord"] not in want]
            if extra: A("deleteCards", cards=extra) if False else log(op="WARN-extra-cards", key=e["key"], cards=extra)
            for c in cards:
                if c["ord"] in want and c["flags"] != want[c["ord"]]:
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[want[c["ord"]]], warning_check=True)
            results.append({"key": e["key"], "nid": nid})
        if stale:
            A("deleteNotes", notes=list(stale)); log(op="deleteNotes", notes=list(stale))
        # readback
        problems = []
        for r, e in zip(results, plan["entries"]):
            n = A("notesInfo", notes=[r["nid"]])[0]
            if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
            if set(n["tags"]) != set(e["tags"]): problems.append(f"tags {e['key']}")
            ci = A("cardsInfo", cards=n["cards"])
            if sorted(c["ord"] for c in ci) != sorted(x["ord"] for x in e["cards"]): problems.append(f"ords {e['key']} {sorted(c['ord'] for c in ci)}")
            for c in ci:
                exp = next((x["flag"] for x in e["cards"] if x["ord"] == c["ord"]), None)
                if c["flags"] != exp: problems.append(f"flag {e['key']} ord{c['ord']}")
                if canon(c["deckName"]) != DECK: problems.append(f"deck {e['key']}")
                if c["queue"] == -1: problems.append(f"suspenso {e['key']}")
            r["cards"] = {str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in ci}
        q = f'"tag:{LESSON_TAG}" -"deck:Referências*"'
        rec = {"run_id": plan["run_id"], "version": plan.get("version"), "selection_hash": plan["selection_hash"], "deck": DECK,
               "notes": results, "cards_in_lesson": len(A("findCards", query=q)), "expected": plan["totais"]["cards"],
               "green": len(A("findCards", query=q + " flag:3")), "blue": len(A("findCards", query=q + " flag:4")),
               "removed": list(stale), "problems": problems, "at": datetime.now(timezone.utc).isoformat()}
        (RUN / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        print(json.dumps({k: rec[k] for k in ("cards_in_lesson", "expected", "green", "blue", "problems")}, ensure_ascii=False))
        if problems: raise SystemExit("Readback divergente — ver receipt.json (sem sync)")


main()
