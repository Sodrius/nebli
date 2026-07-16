#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audita cards NEBLI potencialmente redundantes por slug.

Nao remove nem edita cards. Gera relatorio e, com --apply, marca notas
suspeitas com NEBLI::possible_redundancy.
"""
import argparse
import html
import itertools
import re
import sys
from collections import defaultdict
from pathlib import Path

from anki import call

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "flashcards" / "auditorias"
TAG = "NEBLI::possible_redundancy"
QUERY = "(tag:NEBLI::neblicard-autoral OR tag:NEBLI::gerado)"
STOP = {
    "the", "and", "or", "from", "into", "with", "that", "this", "which",
    "are", "is", "was", "were", "uma", "para", "que", "com", "por", "das",
    "dos", "nas", "nos", "mais", "card", "image", "img",
}


def plain(value):
    value = re.sub(r"<img[^>]*>", " ", value or "", flags=re.I)
    value = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"\1", value, flags=re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def terms(text):
    words = re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ\-]{3,}", text.lower())
    return {w.strip("-") for w in words if w not in STOP}


def slug(note):
    for t in note.get("tags", []):
        if t.startswith(("NEBLI::histo-", "NEBLI::anato-", "NEBLI::embrio-", "NEBLI::bioq-", "NEBLI::biomol-", "NEBLI::imuno-")):
            return t
    return "sem_slug"


def text_of(note):
    fields = note.get("fields", {})
    vals = []
    for name in ("Text", "Texto", "Header"):
        if name in fields:
            vals.append(plain(fields[name].get("value", "")))
    return " ".join(vals)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--threshold", type=float, default=0.72)
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True

    ids = call("findNotes", query=QUERY)
    notes = call("notesInfo", notes=ids)
    groups = defaultdict(list)
    for n in notes:
        txt = text_of(n)
        groups[slug(n)].append((n["noteId"], txt, terms(txt)))

    suspects = []
    for sg, items in groups.items():
        for (a, ta, ka), (b, tb, kb) in itertools.combinations(items, 2):
            if not ka or not kb:
                continue
            j = len(ka & kb) / len(ka | kb)
            if j >= args.threshold:
                suspects.append((sg, a, b, j, ta[:180], tb[:180]))

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "AUDITORIA-REDUNDANCIA-NEBLI-2026-07-14.md"
    lines = [
        "# Auditoria de redundancia NEBLI",
        "",
        f"Threshold Jaccard: {args.threshold}",
        f"Pares suspeitos: {len(suspects)}",
        "",
    ]
    for sg, a, b, j, ta, tb in suspects:
        lines += [
            f"## {sg} - {a} x {b} ({j:.2f})",
            "",
            f"- A: {ta}",
            f"- B: {tb}",
            "",
        ]
    path.write_text("\n".join(lines), encoding="utf-8")

    if args.apply and suspects:
        note_ids = sorted({x[1] for x in suspects} | {x[2] for x in suspects})
        call("addTags", notes=note_ids, tags=TAG)

    print("notes:", len(ids))
    print("pares suspeitos:", len(suspects))
    print("relatorio:", path)
    print("modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
