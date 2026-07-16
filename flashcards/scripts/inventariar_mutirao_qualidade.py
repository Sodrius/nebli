#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera snapshot somente leitura dos decks NEBLI para o mutirao de qualidade.

O inventario preserva IDs, estado de agendamento, flags, campos e tags em JSON
e produz um resumo Markdown reproduzivel. Nenhuma chamada mutante e feita.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from anki import call


CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::[^}]*)?\}\}", re.S)
TAG_RE = re.compile(r"<[^>]+>")
IMG_RE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)", re.I)
FIELD_ORDER = ("Text", "Texto", "Front", "Question", "Pergunta", "Cloze", "Header")


def plain(value: str) -> str:
    value = CLOZE_RE.sub(lambda m: m.group(2), value or "")
    value = TAG_RE.sub(" ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def front(fields: dict) -> str:
    for name in FIELD_ORDER:
        raw = fields.get(name, {}).get("value", "")
        if plain(raw):
            return plain(raw)
    return ""


def source_of(tags: list[str]) -> str:
    joined = " ".join(tags).lower()
    if "nebli::externo" in joined:
        return "external_deck"
    if "nebli::neblicard-autoral" in joined or "nebli::gerado" in joined:
        return "nebli_authorial"
    if "anking" in joined or "nebli::curado" in joined:
        return "anking_copy"
    return "unclassified"


def slug_of(tags: list[str]) -> str:
    prefixes = ("NEBLI::anato-", "NEBLI::histo-", "NEBLI::embrio-", "NEBLI::bioq-", "NEBLI::biomol-", "NEBLI::imuno-")
    return next((tag for tag in tags if tag.startswith(prefixes)), "sem_slug")


def visual_state(tags: list[str], model: str, images: list[str]) -> tuple[str, str, str]:
    tagged_need = next((t.rsplit("::", 1)[-1] for t in tags if t.startswith("NEBLI::visual_need::")), None)
    tagged_role = next((t.rsplit("::", 1)[-1] for t in tags if t.startswith("NEBLI::image_role::")), None)
    if tagged_need:
        need = tagged_need
    elif "IO" in model or "Image Occlusion" in model:
        need = "required"
    elif slug_of(tags).startswith(("NEBLI::anato-", "NEBLI::histo-")):
        need = "required"
    elif slug_of(tags).startswith("NEBLI::embrio-"):
        need = "recommended"
    else:
        need = "optional"
    role = tagged_role or ("recognition" if need == "required" else "schema" if need == "recommended" else "context")
    if not images:
        status = "missing"
    elif any("context" in t or "needs_specific_review" in t for t in tags):
        status = "needs_specific_review"
    elif any(t.endswith("::approved") or t == "img::ok" for t in tags):
        status = "approved"
    else:
        status = "pending_review"
    return need, role, status


def suggested_action(tags: list[str], flags: list[int], comments: list[str], visual_need: str, image_status: str, raw_front: str) -> tuple[str, list[str]]:
    reasons: list[str] = []
    action = "manter"
    if flags or comments:
        action = "revisao_manual"
        reasons.append("feedback_usuario")
    clozes = [plain(m.group(2)).split() for m in CLOZE_RE.finditer(raw_front)]
    if any(len(words) > 3 for words in clozes):
        if action == "manter":
            action = "reescrever"
        reasons.append("cloze_longo")
    if len(clozes) > 1:
        reasons.append("multi_cloze_revisar_atomicidade")
    if visual_need == "required" and image_status != "approved":
        if action == "manter":
            action = "imagem_pendente"
        reasons.append("visual_required_nao_aprovado")
    elif image_status == "needs_specific_review":
        if action == "manter":
            action = "imagem_pendente"
        reasons.append("imagem_contextual_ou_generica")
    return action, reasons


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--label", default="baseline")
    ap.add_argument("--query", default="deck:NEBLI::*", help="consulta Anki usada no snapshot")
    args = ap.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    note_ids = call("findNotes", query=args.query)
    notes = call("notesInfo", notes=note_ids) if note_ids else []
    card_ids = call("findCards", query=args.query)
    cards = call("cardsInfo", cards=card_ids) if card_ids else []
    cards_by_note: dict[int, list[dict]] = defaultdict(list)
    for card in cards:
        cards_by_note[card["note"]].append(card)

    comment_ids = set(call("findNotes", query='tag:"NEBLI_comentario::pendente"'))
    rows = []
    for note in notes:
        nid = note["noteId"]
        fields = note.get("fields", {})
        raw_front = next((fields[n]["value"] for n in FIELD_ORDER if n in fields and fields[n].get("value")), "")
        images = sorted({src for field in fields.values() for src in IMG_RE.findall(field.get("value", ""))})
        note_cards = cards_by_note.get(nid, [])
        flags = sorted({int(c.get("flags", 0)) for c in note_cards if int(c.get("flags", 0))})
        comments = []
        if nid in comment_ids:
            comments.append(plain(fields.get("NEBLI_Comentario", {}).get("value", "")))
        need, role, image_status = visual_state(note.get("tags", []), note.get("modelName", ""), images)
        action, reasons = suggested_action(note.get("tags", []), flags, comments, need, image_status, raw_front)
        rows.append({
            "note_id": nid,
            "card_ids": [c["cardId"] for c in note_cards],
            "deck_names": sorted({c["deckName"] for c in note_cards}),
            "model": note.get("modelName", ""),
            "slug": slug_of(note.get("tags", [])),
            "source": source_of(note.get("tags", [])),
            "front": front(fields),
            "fields": {name: value.get("value", "") for name, value in fields.items()},
            "tags": note.get("tags", []),
            "images": images,
            "flags": flags,
            "comments": comments,
            "visual_need": need,
            "image_role": role,
            "image_status": image_status,
            "importance": "unclassified",
            "cognitive_role": "unclassified",
            "e1_anchor": None,
            "suggested_action": action,
            "action_reasons": reasons,
            "cards": [{
                "card_id": c["cardId"], "deck": c["deckName"], "queue": c.get("queue"),
                "type": c.get("type"), "due": c.get("due"), "interval": c.get("interval"),
                "reps": c.get("reps"), "lapses": c.get("lapses"), "flags": c.get("flags", 0),
            } for c in note_cards],
        })

    deck_counts = Counter(c["deckName"] for c in cards)
    queue_counts = Counter("suspended" if c.get("queue") == -1 else "new" if c.get("type") == 0 else "learning" if c.get("type") in (1, 3) else "review" for c in cards)
    payload = {
        "schema_version": 1,
        "generated_at": dt.datetime.now().astimezone().isoformat(),
        "label": args.label,
        "query": args.query,
        "counts": {
            "notes": len(notes), "cards": len(cards), "decks": len(deck_counts),
            "queues": dict(queue_counts),
            "flags": dict(Counter(str(f) for r in rows for f in r["flags"])),
            "sources": dict(Counter(r["source"] for r in rows)),
            "actions": dict(Counter(r["suggested_action"] for r in rows)),
            "visual_need": dict(Counter(r["visual_need"] for r in rows)),
            "image_status": dict(Counter(r["image_status"] for r in rows)),
        },
        "deck_counts": dict(sorted(deck_counts.items())),
        "notes": rows,
    }
    raw = json.dumps(payload, ensure_ascii=False, indent=2)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    payload["snapshot_sha256"] = digest
    json_path = args.output_dir / f"INVENTARIO-{args.label}.json"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"# Inventário do mutirão — {args.label}", "",
        f"- Gerado em: `{payload['generated_at']}`", f"- SHA-256 do conteúdo: `{digest}`",
        f"- Notes: **{len(notes)}**", f"- Cards: **{len(cards)}**", "",
        "## Filas", "",
    ]
    lines += [f"- `{k}`: {v}" for k, v in sorted(queue_counts.items())]
    lines += ["", "## Fontes", ""] + [f"- `{k}`: {v}" for k, v in sorted(Counter(r["source"] for r in rows).items())]
    lines += ["", "## Ações sugeridas", ""] + [f"- `{k}`: {v}" for k, v in sorted(Counter(r["suggested_action"] for r in rows).items())]
    lines += ["", "## Estado visual", ""] + [f"- `{k}`: {v}" for k, v in sorted(Counter(r["image_status"] for r in rows).items())]
    lines += ["", "## Decks", ""] + [f"- `{k}`: {v} cards" for k, v in sorted(deck_counts.items())]
    lines += ["", "## Fila prioritária", ""]
    priority = sorted((r for r in rows if r["suggested_action"] != "manter"), key=lambda r: (not bool(r["flags"] or r["comments"]), r["slug"], r["note_id"]))
    for r in priority:
        lines.append(f"- note `{r['note_id']}` · `{r['suggested_action']}` · `{r['slug']}` · {', '.join(r['action_reasons'])}")
    md_path = args.output_dir / f"INVENTARIO-{args.label}.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json_path)
    print(md_path)
    print(json.dumps(payload["counts"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
