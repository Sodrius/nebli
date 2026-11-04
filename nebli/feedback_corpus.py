"""Snapshot somente de leitura para auditar comentários e aprendizagem.

Não interpreta suspensão como reprovação e não atribui edições a Davi sem evidência.
"""
from __future__ import annotations
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from nebli.decks import Anki
from nebli.explicacoes import liked_cards, store_path

ROOT = Path(__file__).resolve().parents[1]
MARK = re.compile(r"CORRIGIDO\s*,?\s*\d{1,2}\s*[,/]\s*\d{1,2}\s*[,/]\s*\d{2,4}\s*\.?", re.I)

def pending(raw):
    matches = list(MARK.finditer(raw or ""))
    tail = raw[matches[-1].end():] if matches else (raw or "")
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", " ", tail)).strip()

def snapshot(output, call=None):
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    if (out / "notes.json").exists():
        raise SystemExit("Snapshot já existe; use outro destino para preservar a evidência.")
    a = call or Anki()
    comment_ids = a("findNotes", query="NEBLI_Comentario:_*")
    scope_ids = a("findNotes", query='"deck:NEBLI*"')
    likes = liked_cards(verbose=False)
    liked_info = a("cardsInfo", cards=[int(x["card"]) for x in likes]) if likes else []
    ids = sorted(set(comment_ids + scope_ids + [x["note"] for x in liked_info if x]))
    notes = []
    for i in range(0, len(ids), 250):
        notes.extend(n for n in a("notesInfo", notes=ids[i:i+250]) if n and n.get("noteId"))
    cids = sorted({cid for n in notes for cid in n["cards"]})
    cards, reviews = [], {}
    for i in range(0, len(cids), 300):
        batch = cids[i:i+300]
        cards.extend(a("cardsInfo", cards=batch))
        reviews.update(a("getReviewsOfCards", cards=batch))
    data = {"notes": notes, "cards": cards, "reviews": reviews, "likes": likes,
            "deck_names": a("deckNames"), "comment_ids": comment_ids}
    for name, value in data.items():
        (out / f"{name}.json").write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
    log = ROOT / "flashcards/projeto/comentarios-cards.jsonl"
    shutil.copy2(log, out / "comment-history.jsonl")
    shutil.copy2(store_path().parent / "tab-log.jsonl", out / "tab-log.jsonl")
    active = [{"nid": n["noteId"], "comment": pending(n["fields"].get("NEBLI_Comentario", {}).get("value", "")),
               "front": next((n["fields"][k]["value"] for k in ("Text", "Front", "Nome PT", "Header") if k in n["fields"]), ""),
               "model": n["modelName"]} for n in notes]
    active = [n for n in active if n["comment"]]
    (out / "pending.json").write_text(json.dumps(active, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = {"at": datetime.now(timezone.utc).isoformat(), "notes": len(notes), "cards": len(cards),
               "commented_notes": len(comment_ids), "pending_tails": len(active), "likes": len(likes),
               "review_events": sum(len(v) for v in reviews.values()), "read_only": True}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    import sys
    snapshot(sys.argv[1])
