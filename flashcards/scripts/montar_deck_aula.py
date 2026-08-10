#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Monta o destino do deck-aula.

Backends:
  ankidroid (padrão): gera manifesto para o Nebli Companion no tablet. Não exige
    AnkiConnect, Drive, Colab ou APKG.
  desktop: fallback legado via AnkiConnect; copia notas para o deck-alvo e pode
    exportar APKG.

A cópia AnKing é fiel: nenhum campo é prefixado/rewrite. Proveniência entra apenas
como tag/metadata do lote.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

AC = "http://localhost:8765"
_WS = re.compile(r"\s+")
_TAG = re.compile(r"<[^>]+>")


def call(action, **params):
    req = urllib.request.Request(
        AC,
        json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8"),
        {"Content-Type": "application/json"},
    )
    response = json.load(urllib.request.urlopen(req, timeout=90))
    if response.get("error"):
        raise RuntimeError(f"{action}: {response['error']}")
    return response["result"]


def norm(value: str) -> str:
    return _WS.sub(" ", _TAG.sub("", value or "").replace("​", "")).strip()


def first_field_val(fields):
    return next(iter(fields.values()), {}).get("value", "") if fields else ""


def build_ankidroid_manifest(args) -> int:
    script = Path(__file__).with_name("gerar_manifesto_ankidroid.py")
    cmd = [
        sys.executable,
        str(script),
        "--slug",
        args.slug,
        "--deck",
        args.deck,
    ]
    if args.curado:
        cmd += ["--curado", args.curado]
    if args.manifest:
        cmd += ["--out", args.manifest]
    if args.source_query:
        cmd += ["--source-query", args.source_query]
    print("[ankidroid] gerando manifesto local; nenhuma coleção fonte será modificada")
    return subprocess.call(cmd)


def build_desktop(args) -> int:
    call("createDeck", deck=args.deck)
    existing = set()
    target_ids = call("findNotes", query=f'deck:"{args.deck}"')
    if target_ids:
        for note in call("notesInfo", notes=target_ids):
            existing.add(norm(first_field_val(note["fields"])))

    source_query = args.source_query or f'tag:NEBLI::{args.slug} -deck:"{args.deck}"'
    source_ids = call("findNotes", query=source_query)
    copied = skipped = 0

    for note in call("notesInfo", notes=source_ids) if source_ids else []:
        key = norm(first_field_val(note["fields"]))
        if key in existing:
            skipped += 1
            continue
        fields = {name: data["value"] for name, data in note["fields"].items()}
        # Fidelidade literal: não alterar Text/Extra nem remover campos da fonte.
        tags = list(dict.fromkeys(note["tags"] + [f"NEBLI::{args.slug}", "NEBLI::source::copy"]))
        new_note = {
            "deckName": args.deck,
            "modelName": note["modelName"],
            "fields": fields,
            "tags": tags,
            "options": {"allowDuplicate": True},
        }
        if args.dry:
            copied += 1
            continue
        try:
            call("addNote", note=new_note)
            copied += 1
            existing.add(key)
        except Exception as exc:
            print("  ERRO copy:", key[:50], "::", str(exc)[:120])

    total = len(call("findNotes", query=f'deck:"{args.deck}"'))
    print(f"[{args.slug}] copiados {copied}, pulados {skipped} | deck-aula total: {total}")

    if args.export and not args.dry:
        out = os.path.abspath(args.export)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        ok = call("exportPackage", deck=args.deck, path=out, includeSched=False)
        print(f"  export {'OK' if ok else 'FALHOU'} -> {out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--deck", required=True)
    ap.add_argument("--backend", choices=("ankidroid", "desktop"), default="ankidroid")
    ap.add_argument("--curado", help="JSON de curadoria a embutir no manifesto quando houver IDs locais")
    ap.add_argument("--manifest", help="caminho do manifesto AnkiDroid")
    ap.add_argument("--source-query", help="query local da fonte; padrão tag NEBLI::<slug>")
    ap.add_argument("--export", help="somente backend desktop")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    if not args.deck.startswith("NEBLI::"):
        raise SystemExit("ERRO: deck-aula gravável deve começar por NEBLI::")

    if args.backend == "ankidroid":
        return build_ankidroid_manifest(args)
    return build_desktop(args)


if __name__ == "__main__":
    raise SystemExit(main())
