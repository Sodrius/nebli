"""Estudo descritivo somente leitura; não classifica/edita a coleção."""
import html
import hashlib
import json
import random
import re
import statistics
import sqlite3
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent
QUERY = 'deck:"Referências::Anking Step Deck" -deck:"Referências::AnKing Step Deck::Instructions"'
SNAPSHOT = BASE.parent / "ajustes-anki-2026-09-28/collection-before.anki2"
SNAP_NOTES = None


def snapshot_read(action, params):
    global SNAP_NOTES
    if SNAP_NOTES is None:
        db = sqlite3.connect(SNAPSHOT.resolve().as_uri() + "?mode=ro", uri=True)
        db.create_collation("unicase", lambda a,b: (a.casefold()>b.casefold())-(a.casefold()<b.casefold()))
        db.execute("PRAGMA query_only=ON")
        deck_ids = [did for did, name in db.execute("SELECT id,name FROM decks")
                    if name.replace("\x1f", "::").casefold() == "Referências::Anking Step Deck".casefold()]
        assert len(deck_ids) == 1
        nt = dict(db.execute("SELECT id,name FROM notetypes"))
        fields = {}
        for mid, ordinal, name in db.execute("SELECT ntid,ord,name FROM fields ORDER BY ntid,ord"):
            fields.setdefault(mid, []).append(name)
        note_cards = {}
        for cid, nid in db.execute("SELECT id,nid FROM cards WHERE did=? OR odid=?", (deck_ids[0], deck_ids[0])):
            note_cards.setdefault(nid, []).append(cid)
        SNAP_NOTES = {}
        for nid, mid, flds in db.execute("SELECT id,mid,flds FROM notes"):
            if nid in note_cards:
                SNAP_NOTES[nid] = {"noteId": nid, "modelName": nt[mid], "cards": note_cards[nid],
                                   "fields": {name:{"value": val} for name,val in zip(fields[mid],flds.split("\x1f"))}}
        db.close()
    if action == "getActiveProfile":
        return "Snapshot Mac User 1 de 28/09; não estado vivo"
    if action == "notesInfo":
        return [SNAP_NOTES[nid] for nid in params["notes"]]
    if action == "findNotes":
        terms = re.findall(r"Text:\*?(\w+)", params["query"])
        return [nid for nid,n in SNAP_NOTES.items() if not terms or any(
            term.casefold() in n["fields"].get("Text", {}).get("value", "").casefold() for term in terms)]
    raise ValueError(action)


def anki(action, **params):
    assert action in {"findNotes", "notesInfo", "getActiveProfile"}
    if "--snapshot" in sys.argv:
        return snapshot_read(action, params)
    request = urllib.request.Request("http://127.0.0.1:8765", data=json.dumps({"action": action, "version": 6, "params": params}).encode())
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result["error"]:
        raise RuntimeError(result["error"])
    return result["result"]


def plain(value):
    value = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", value, flags=re.S | re.I)
    for _ in range(12):
        new = re.sub(r"\{\{c[\d,]+::([^{}]*?)\}\}", lambda m: m[1].split("::", 1)[0], value)
        if new == value:
            break
        value = new
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value))).strip()


def words(value):
    return re.findall(r"\b\w+(?:[-'’]\w+)*\b", plain(value))


def distribution(values):
    values = sorted(values)
    return {"n": len(values), "mean": round(statistics.mean(values), 2), "median": statistics.median(values),
            "p10": values[int((len(values)-1)*.1)], "p90": values[int((len(values)-1)*.9)], "max": max(values)}


def main():
    if (BASE / "anking-estudo.json").exists():
        raise SystemExit("Snapshot já existe; não sobrescrever estudo anterior.")
    rng = random.Random(20260928)
    population = sorted(anki("findNotes", query=QUERY))
    sample = rng.sample(population, min(1000, len(population)))
    cohorts = {
        "edema": '(Text:edema Text:albumin Text:hydrostatic Text:oncotic)',
        "fisiologia": '(Text:peristalsis Text:motility Text:depolarization Text:feedback)',
        "anatomia": '(Text:mesenteric Text:duodenum Text:hepatic Text:esophagus)',
        "imunologia": '(Text:complement Text:opsonization Text:inflammation Text:neutrophils)',
        "microbiologia": '(Text:virulence Text:peptidoglycan Text:exotoxin Text:plasmid)',
        "histo": '(Text:enterocyte Text:goblet Text:epithelium Text:crypts)',
    }
    selected = {}
    for key, terms in cohorts.items():
        terms = re.sub(r"Text:(\w+)", r"Text:*\1*", terms)
        terms = terms.replace(" Text:", " or Text:")
        ids = sorted(anki("findNotes", query=QUERY + " " + terms))
        selected[key] = {"pool": len(ids), "ids": rng.sample(ids, min(8, len(ids))), "query": terms}
    wanted = list(dict.fromkeys(sample + [nid for c in selected.values() for nid in c["ids"]]))
    notes = []
    for start in range(0, len(wanted), 100):
        notes.extend(anki("notesInfo", notes=wanted[start:start+100]))
    byid = {n["noteId"]: n for n in notes}
    rows = []
    for nid in sample:
        n = byid[nid]
        field = n["fields"].get("Text", {}).get("value", "")
        extra = n["fields"].get("Extra", {}).get("value", "")
        rows.append({"note_id": nid, "text_words": len(words(field)), "extra_words": len(words(extra)),
                     "text_images": len(re.findall(r"<img\b", field, re.I)), "bold": bool(re.search(r"<(b|strong)\b", field)),
                     "cloze_ids": sorted(set(re.findall(r"\{\{c([\d,]+)::", field))),
                     "unparsed_cloze": "{{c" in plain(field), "cards": len(n["cards"]), "model": n["modelName"]})
    nonempty = [r for r in rows if r["text_words"] and not r["unparsed_cloze"]]
    stats = {
        "at": datetime.now(timezone.utc).isoformat(), "profile": anki("getActiveProfile"),
        "population_notes": len(population), "sample_notes": len(sample), "query": QUERY, "seed": 20260928,
        "method": "Amostra aleatória uniforme por nota, Text completado (resposta visível), HTML removido para medição; não frente renderizada nem auditoria científica.",
        "source": str(SNAPSHOT) if "--snapshot" in sys.argv else "AnkiConnect vivo",
        "source_sha256": hashlib.sha256(SNAPSHOT.read_bytes()).hexdigest() if "--snapshot" in sys.argv else None,
        "text_words": distribution([r["text_words"] for r in nonempty]),
        "extra_words_nonempty": distribution([r["extra_words"] for r in rows if r["extra_words"]]),
        "generated_cards_observed": sum(r["cards"] for r in rows),
        "models": dict(Counter(r["model"] for r in rows)),
        "notes_with_bold": sum(r["bold"] for r in rows), "notes_with_text_image": sum(r["text_images"]>0 for r in rows),
        "notes_without_text_words": sum(r["text_words"]==0 for r in rows),
        "notes_with_multiple_cloze_ids": sum(len(r["cloze_ids"])>1 for r in rows),
        "notes_with_unparsed_cloze": sum(r["unparsed_cloze"] for r in rows),
        "cohorts": selected,
    }
    (BASE / "anking-estudo.json").write_text(json.dumps({"stats": stats, "rows": rows, "notes": notes}, ensure_ascii=False, indent=1))
    (BASE / "anking-estatisticas.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2))
    lines = []
    # Exemplos adicionais aleatórios para não estudar só os temas atuais.
    selected["aleatorios"] = {"ids": sample[:24]}
    for group, cohort in selected.items():
        for nid in cohort["ids"]:
            n = byid[nid]
            field = n["fields"].get("Text", {}).get("value", "")
            extra = n["fields"].get("Extra", {}).get("value", "")
            lines.extend([f"{group} | {nid} | words={len(words(field))} | cards={len(n['cards'])}",
                          "Text: " + re.sub(r"<[^>]+>", "", html.unescape(field)),
                          "Extra: " + plain(extra), ""])
    (BASE / "anking-leitura.txt").write_text("\n".join(lines))
    print(json.dumps({k:v for k,v in stats.items() if k != "cohorts"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
