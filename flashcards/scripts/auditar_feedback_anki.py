#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audita flags e comentarios NEBLI via AnkiConnect, sem mutar a colecao."""
import argparse
import datetime as dt
import html
import json
import re
import urllib.request
from pathlib import Path

ANKI = "http://localhost:8765"
FIELD_PRIORITY = ("Text", "Front", "Question", "Pergunta", "Cloze", "Header")


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKI, payload, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as response:
        data = json.load(response)
    if data.get("error"):
        raise RuntimeError(f"{action}: {data['error']}")
    return data["result"]


def plain(value):
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"[\1]", value)
    return re.sub(r"\s+", " ", value).strip()


def front(fields):
    for name in FIELD_PRIORITY:
        if name in fields and plain(fields[name].get("value")):
            return plain(fields[name]["value"])
    for item in fields.values():
        if plain(item.get("value")):
            return plain(item["value"])
    return "[sem frente textual]"


def audit():
    rows = []
    for flag, meaning in ((1, "revisar/explicar"), (2, "re-julgar escopo"), (3, "bom card")):
        ids = call("findCards", query=f"tag:NEBLI::* flag:{flag}")
        for card in call("cardsInfo", cards=ids) if ids else []:
            rows.append({"flag": flag, "meaning": meaning, "card": card["cardId"],
                         "note": card["note"], "deck": card["deckName"],
                         "model": card["modelName"], "front": front(card.get("fields", {}))[:240]})
    pending = call("findNotes", query='tag:"NEBLI_comentario::pendente"')
    comments = []
    for note in call("notesInfo", notes=pending) if pending else []:
        fields = note.get("fields", {})
        comments.append({"note": note["noteId"], "model": note["modelName"],
                         "front": front(fields)[:240],
                         "comment": plain(fields.get("NEBLI_Comentario", {}).get("value", ""))})
    return rows, comments


def render(rows, comments):
    counts = {flag: sum(r["flag"] == flag for r in rows) for flag in (1, 2, 3)}
    out = [f"# Auditoria de feedback Anki — {dt.date.today().isoformat()}", "",
           f"- Vermelhas: **{counts[1]}**", f"- Laranjas: **{counts[2]}**",
           f"- Verdes: **{counts[3]}**", f"- Comentarios pendentes: **{len(comments)}**", ""]
    for flag, title in ((1, "Vermelhas"), (2, "Laranjas"), (3, "Verdes")):
        out += [f"## {title}", ""]
        selected = [r for r in rows if r["flag"] == flag]
        if not selected:
            out.append("Nenhuma.")
        for row in selected:
            out += [f"- card `{row['card']}` · note `{row['note']}` · {row['deck']}",
                    f"  - {row['front']}"]
        out.append("")
    out += ["## Comentarios pendentes", ""]
    if not comments:
        out.append("Nenhum.")
    for item in comments:
        out += [f"- note `{item['note']}` · {item['front']}",
                f"  - Comentario: {item['comment']}"]
    return "\n".join(out) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="grava Markdown; sem isto imprime")
    args = parser.parse_args()
    report = render(*audit())
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(args.output)
    else:
        print(report)


if __name__ == "__main__":
    main()
