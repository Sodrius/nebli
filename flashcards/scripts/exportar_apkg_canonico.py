#!/usr/bin/env python3
"""Exporta deck-data validado para APKG canônico usando apenas a stdlib."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sqlite3
import tempfile
import time
import zipfile
from pathlib import Path
from typing import Any

CLOZE_MODEL_ID = 1708171301
IO_MODEL_ID = 1708171302
DEFAULT_CONF_ID = 1
FIELD_SEP = "\x1f"


def _stable_int(value: str, *, floor: int = 1_000_000_000) -> int:
    raw = int.from_bytes(hashlib.sha256(value.encode("utf-8")).digest()[:7], "big")
    return floor + raw % 8_000_000_000_000


def _guid(card_key: str) -> str:
    return hashlib.sha256(("nebli:" + card_key).encode("utf-8")).hexdigest()[:20]


def _csum(text: str) -> int:
    plain = re.sub(r"<[^>]+>", " ", text or "")
    return int(hashlib.sha1(plain.encode("utf-8")).hexdigest()[:8], 16)


def canonical_deck_name(data: dict[str, Any]) -> str:
    metadata = data.get("metadata") or {}
    parts = [metadata.get("uc"), metadata.get("prova"), metadata.get("componente"), metadata.get("nome_curto")]
    clean = [str(part or "").strip().replace("::", "-") for part in parts]
    if any(not part for part in clean):
        raise ValueError("metadata precisa de uc, prova, componente e nome_curto para nome canônico")
    return "NEBLI::" + "::".join(clean)


def _field(name: str, ord_: int) -> dict[str, Any]:
    return {"name": name, "ord": ord_, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []}


def _cloze_model(now: int, did: int) -> dict[str, Any]:
    names = ["Text", "Extra", "NEBLI_Comentario", "NEBLI_Resposta", "NEBLI_Historico", "CardKey", "ConceptId", "DerivationRationale"]
    return {
        "id": CLOZE_MODEL_ID, "name": "NEBLI Cloze v13", "type": 1, "mod": now, "usn": -1,
        "sortf": 0, "did": did,
        "tmpls": [{"name": "Cloze", "ord": 0, "qfmt": "{{cloze:Text}}", "afmt": "{{cloze:Text}}<hr id=answer>{{Extra}}"}],
        "flds": [_field(name, i) for i, name in enumerate(names)],
        "css": ".card{font-family:Arial;font-size:20px;text-align:left;color:#111;background:#fff}",
        "latexPre": "", "latexPost": "", "req": []
    }


def _io_model(now: int, did: int) -> dict[str, Any]:
    names = ["Question", "Answer", "Extra", "Source", "Answers", "NEBLI_Comentario", "NEBLI_Resposta", "NEBLI_Historico", "CardKey", "ConceptId"]
    return {
        "id": IO_MODEL_ID, "name": "NEBLI Image Occlusion v13", "type": 0, "mod": now, "usn": -1,
        "sortf": 0, "did": did,
        "tmpls": [{"name": "Image Occlusion", "ord": 0, "qfmt": "{{Question}}", "afmt": "{{Answer}}<hr id=answer>{{Extra}}"}],
        "flds": [_field(name, i) for i, name in enumerate(names)],
        "css": ".card{font-family:Arial;font-size:20px;text-align:center;color:#111;background:#fff}.nebli-io-wrap{position:relative;display:inline-block;max-width:100%}.nebli-io-wrap img{max-width:100%;height:auto}.nebli-mask{position:absolute;background:#111;border:1px solid #fff}.nebli-io-prompt{margin:12px auto;text-align:left;max-width:760px}",
        "latexPre": "", "latexPost": "", "req": [[0, "any", [0]]]
    }


def _deck(did: int, name: str, now: int) -> dict[str, Any]:
    return {"id": did, "name": name, "mod": now, "usn": -1, "desc": "", "dyn": 0, "collapsed": False, "extendNew": 10, "extendRev": 50, "conf": DEFAULT_CONF_ID}


def _dconf() -> dict[str, Any]:
    return {"1": {"id": 1, "name": "Default", "mod": 0, "usn": 0, "maxTaken": 60, "autoplay": True, "timer": 0, "replayq": True,
        "new": {"bury": True, "delays": [1, 10], "initialFactor": 2500, "ints": [1, 4], "order": 1, "perDay": 25},
        "rev": {"bury": True, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1, "maxIvl": 36500, "perDay": 9999},
        "lapse": {"delays": [10], "leechAction": 0, "leechFails": 8, "minInt": 1, "mult": 0}}}


def _schema(db: sqlite3.Connection) -> None:
    db.executescript("""
CREATE TABLE col (id integer primary key, crt integer not null, mod integer not null, scm integer not null, ver integer not null, dty integer not null, usn integer not null, ls integer not null, conf text not null, models text not null, decks text not null, dconf text not null, tags text not null);
CREATE TABLE notes (id integer primary key, guid text not null, mid integer not null, mod integer not null, usn integer not null, tags text not null, flds text not null, sfld integer not null, csum integer not null, flags integer not null, data text not null);
CREATE TABLE cards (id integer primary key, nid integer not null, did integer not null, ord integer not null, mod integer not null, usn integer not null, type integer not null, queue integer not null, due integer not null, ivl integer not null, factor integer not null, reps integer not null, lapses integer not null, left integer not null, odue integer not null, odid integer not null, flags integer not null, data text not null);
CREATE TABLE revlog (id integer primary key, cid integer not null, usn integer not null, ease integer not null, ivl integer not null, lastIvl integer not null, factor integer not null, time integer not null, type integer not null);
CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);
CREATE INDEX ix_notes_usn ON notes (usn); CREATE INDEX ix_cards_usn ON cards (usn); CREATE INDEX ix_cards_nid ON cards (nid); CREATE INDEX ix_cards_sched ON cards (did, queue, due); CREATE INDEX ix_revlog_usn ON revlog (usn); CREATE INDEX ix_revlog_cid ON revlog (cid);
""")


def _resolve_media(card: dict[str, Any], base: Path) -> Path | None:
    raw = card.get("image_path")
    if not raw: return None
    path = Path(str(raw))
    return path if path.is_absolute() else (base / path).resolve()


def _io_html(card: dict[str, Any], filename: str) -> tuple[str, str]:
    escaped = html.escape(filename, quote=True)
    masks = []
    for mask in card.get("masks") or []:
        x, y, w, h = (float(mask[key]) * 100 for key in ("x", "y", "w", "h"))
        masks.append(f'<span class="nebli-mask" style="left:{x:.4f}%;top:{y:.4f}%;width:{w:.4f}%;height:{h:.4f}%"></span>')
    prompt = html.escape(str(card.get("prompt") or ""))
    question = f'<div class="nebli-io-wrap"><img src="{escaped}">{"".join(masks)}</div><div class="nebli-io-prompt">{prompt}</div>'
    answer = f'<div class="nebli-io-wrap"><img src="{escaped}"></div>'
    return question, answer


def export_apkg(data: dict[str, Any], deck_data_path: Path, out: Path) -> dict[str, Any]:
    cards = [card for card in data.get("cards", []) if isinstance(card, dict)]
    if not cards: raise ValueError("deck sem cards")
    deck_name = canonical_deck_name(data)
    did = _stable_int("deck:" + deck_name); optional_name = deck_name + "::Optional"; optional_did = _stable_int("deck:" + optional_name)
    now = int(time.time()); base = deck_data_path.resolve().parent
    media_files: list[Path] = []; media_names: dict[str, str] = {}
    with tempfile.TemporaryDirectory(prefix="nebli-apkg-") as raw:
        temp = Path(raw); collection = temp / "collection.anki2"; db = sqlite3.connect(collection)
        try:
            _schema(db)
            models = {str(CLOZE_MODEL_ID): _cloze_model(now, did), str(IO_MODEL_ID): _io_model(now, did)}
            decks = {str(did): _deck(did, deck_name, now), str(optional_did): _deck(optional_did, optional_name, now)}
            conf = {"nextPos": len(cards)+1, "estTimes": True, "activeDecks": [did], "curDeck": did, "newSpread": 0, "collapseTime": 1200, "timeLim": 0}
            db.execute("INSERT INTO col VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (1, now, now*1000, now*1000, 11, 0, 0, 0, json.dumps(conf), json.dumps(models, ensure_ascii=False), json.dumps(decks, ensure_ascii=False), json.dumps(_dconf(), ensure_ascii=False), "{}"))
            for position, card in enumerate(cards, 1):
                key = str(card.get("card_key") or "").strip()
                if not key: raise ValueError("card sem card_key")
                source = str(card.get("source") or ""); tier = str(card.get("tier") or "nucleo"); concept = str(card.get("concept_id") or "")
                note_id = _stable_int("note:"+key); card_id = _stable_int("card:"+key); target_did = optional_did if tier == "optional" else did
                tags = f" NEBLI::tier::{tier} NEBLI::concept::{concept} {('opcional' if tier == 'optional' else 'nucleo')} "
                if source == "authored":
                    text = str(card.get("text") or ""); fields = [text, str(card.get("extra") or ""), "", "", "", key, concept, str(card.get("derivation_rationale") or "")]; mid = CLOZE_MODEL_ID; sfld = text
                elif source == "io":
                    media = _resolve_media(card, base)
                    if media is None or not media.is_file(): raise ValueError(f"{key}: image_path inexistente")
                    digest = hashlib.sha256(media.read_bytes()).hexdigest(); safe_name = f"nebli_{digest[:16]}_{media.name}"
                    media_files.append(media); media_names[str(media)] = safe_name; question, answer = _io_html(card, safe_name)
                    fields = [question, answer, str(card.get("extra") or ""), str(card.get("source_credit") or ""), json.dumps(card.get("answers") or [], ensure_ascii=False), "", "", "", key, concept]; mid = IO_MODEL_ID; sfld = str(card.get("prompt") or key)
                else: raise ValueError(f"{key}: source inválido para APKG: {source}")
                db.execute("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)", (note_id, _guid(key), mid, now, -1, tags, FIELD_SEP.join(fields), sfld, _csum(str(sfld)), 0, ""))
                db.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (card_id, note_id, target_did, 0, now, -1, 0, 0, position, 0, 2500, 0, 0, 0, 0, 0, 0, ""))
            db.commit()
        finally: db.close()
        out.parent.mkdir(parents=True, exist_ok=True); mapping: dict[str, str] = {}
        with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as package:
            package.write(collection, "collection.anki2"); seen: set[str] = set()
            for media in media_files:
                filename = media_names[str(media)]
                if filename in seen: continue
                index = str(len(mapping)); mapping[index] = filename; package.write(media, index); seen.add(filename)
            package.writestr("media", json.dumps(mapping, ensure_ascii=False))
    return {"apkg": str(out), "deck_name": deck_name, "card_count": len(cards), "media_count": len(mapping)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--deck-data", type=Path, required=True); ap.add_argument("--out", type=Path, required=True); args = ap.parse_args()
    data = json.loads(args.deck_data.read_text(encoding="utf-8")); print(json.dumps(export_apkg(data, args.deck_data, args.out), ensure_ascii=False, indent=2)); return 0


if __name__ == "__main__": raise SystemExit(main())
