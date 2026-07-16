#!/usr/bin/env python3
"""Remove a mesma mídia repetida no mesmo card/nota, com snapshot e auditoria.

Não mede nem poda reuso entre cards. A unidade do defeito é uma nota/campo:
duas tags <img> com o mesmo src (ou bytes idênticos) em Text/Extra.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from anki import call

IMG_RE = re.compile(r"<img\b[^>]*\bsrc\s*=\s*(['\"])(.*?)\1[^>]*>", re.I | re.S)
FIELDS = ("Text", "Texto", "Front", "Question", "Pergunta", "Extra", "Back Extra", "Remarks", "Explicacao", "Explicação")


def normalized_src(src: str) -> str:
    value = html.unescape(src or "").strip()
    path = urlsplit(value).path if "://" in value else value.split("?", 1)[0]
    return Path(unquote(path)).name.casefold()


def media_dirs() -> list[Path]:
    root = Path(os.environ.get("APPDATA", "")) / "Anki2"
    return [p for p in root.glob("*/collection.media") if p.is_dir()]


class MediaResolver:
    def __init__(self) -> None:
        self.dirs = media_dirs()
        self.cache: dict[str, str | None] = {}

    def digest(self, src: str) -> str | None:
        key = normalized_src(src)
        if key in self.cache:
            return self.cache[key]
        for directory in self.dirs:
            path = directory / Path(unquote(src.split("?", 1)[0])).name
            if path.is_file():
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                self.cache[key] = digest
                return digest
        self.cache[key] = None
        return None


def dedupe_html(value: str, resolver: MediaResolver, seen_src: set[str] | None = None,
                seen_hash: set[str] | None = None) -> tuple[str, list[dict]]:
    seen_src = seen_src if seen_src is not None else set()
    seen_hash = seen_hash if seen_hash is not None else set()
    removed: list[dict] = []

    def repl(match: re.Match) -> str:
        src = match.group(2)
        key = normalized_src(src)
        digest = resolver.digest(src)
        reason = None
        if key and key in seen_src:
            reason = "same_src"
        elif digest and digest in seen_hash:
            reason = "same_sha256"
        if reason:
            removed.append({"src": src, "normalized_src": key, "sha256": digest, "reason": reason})
            return ""
        if key:
            seen_src.add(key)
        if digest:
            seen_hash.add(digest)
        return match.group(0)

    cleaned = IMG_RE.sub(repl, value or "")
    cleaned = re.sub(r"(?:\s*<br\s*/?>\s*){3,}", "<br><br>", cleaned, flags=re.I)
    return cleaned, removed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", default="deck:NEBLI::* -deck:NEBLI::STAGING::*")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.apply:
        try:
            current = call("guiCurrentCard")
        except RuntimeError as exc:
            if "not currently active" not in str(exc):
                raise
            current = None
        if current:
            raise SystemExit(f"Reviewer ativo no card {current.get('cardId')}; aplicacao adiada")
    ids = call("findNotes", query=args.query)
    notes = call("notesInfo", notes=ids)
    resolver = MediaResolver()
    changes = []
    for note in notes:
        # IO/Anatomy usam a imagem como fonte do note type; não normalizar seus
        # campos especiais. Ainda auditamos Text/Extra se existirem.
        updates, removed_all = {}, []
        before = {}
        for name in FIELDS:
            if name not in note.get("fields", {}):
                continue
            value = note["fields"][name].get("value", "")
            # Campos diferentes podem ocupar faces distintas. Sem evidência do
            # DOM visível, não apagar automaticamente uma imagem Text+Extra.
            cleaned, removed = dedupe_html(value, resolver, set(), set())
            if removed:
                before[name] = value
                updates[name] = cleaned
                removed_all += [{"field": name, **item} for item in removed]
        if not updates:
            continue
        row = {"note_id": note["noteId"], "model": note.get("modelName", ""),
               "before_fields": before, "after_fields": updates,
               "tags_before": note.get("tags", []), "removed": removed_all}
        changes.append(row)
        if args.apply:
            call("updateNoteFields", note={"id": note["noteId"], "fields": updates})
            call("addTags", notes=[note["noteId"]], tags="NEBLI::image_deduped::2026-07-15")
    payload = {"generated_at": dt.datetime.now().astimezone().isoformat(),
               "query": args.query, "mode": "apply" if args.apply else "dry-run",
               "notes_changed": len(changes),
               "image_occurrences_removed": sum(len(x["removed"]) for x in changes),
               "changes": changes}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("mode", "notes_changed", "image_occurrences_removed")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
