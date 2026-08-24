#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adiciona imagem de contexto aos NEBLIcards P3 que ainda nao tem imagem no Extra.

Camada 1: por slug/aula, usa uma fonte visual coerente (Anki externo ou slide)
e anexa essa imagem no Extra. Isso resolve o problema grosseiro "card sem imagem",
mas deixa tag de auditoria para troca fina quando a imagem precisar ser especifica.

Uso:
  python flashcards/scripts/enriquecer_p3_neblicards_com_imagens.py --dry-run
  python flashcards/scripts/enriquecer_p3_neblicards_com_imagens.py --apply
"""
import argparse
import atexit
import base64
import hashlib
import io as _io
import os
import re
import sys
from pathlib import Path

from PIL import Image
from nebli_anki import call

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[2]
NEEDS = "NEBLI::needs_image"
HAS = "NEBLI::image_extra"
CTX = "NEBLI::image_context_needs_specific_review"
LOCK = ROOT / "arquivos-trabalho" / ".enriquecer_p3_neblicards_com_imagens.lock"


SLUG_SOURCES = {
    "NEBLI::histo-09-vasos": {
        "anki_query": 'tag:H::* artery',
        "credit": "Image from imported Histology deck.",
    },
    "NEBLI::histo-10-tecido-nervoso": {
        "anki_query": 'tag:H::NervousSystem neuron',
        "credit": "Image from imported Histology deck.",
    },
    "NEBLI::histo-11-orgaos-linfaticos": {
        "anki_query": 'tag:H::* thymus',
        "credit": "Image from imported Histology deck.",
    },
    "NEBLI::anato-05-circ-linf-I": {
        "anki_query": 'tag:BlueLink::Heart',
        "credit": "Image from BlueLink Atlas, University of Michigan.",
    },
    "NEBLI::anato-06-circ-linf-II": {
        "anki_query": 'tag:BlueLink::SuperiorMediastinum+RootOfNeck',
        "credit": "Image from BlueLink Atlas, University of Michigan.",
    },
    "NEBLI::anato-05-sistema-linfatico": {
        "anki_query": 'tag:Dope::Anatomy::Abdomen lymph',
        "credit": "Image from imported Dope Anatomy deck.",
    },
    "NEBLI::embrio-01-gametogenese-fertilizacao": {
        "file": "figuras/embrio-01-gametogenese-fertilizacao/slide-01.png",
        "credit": "Fonte visual: slide da aula.",
    },
    "NEBLI::embrio-02-03-gastrulacao-neurulacao": {
        "file": "figuras/embrio-gastrulacao-neurulacao/slide-01.png",
        "credit": "Fonte visual: slide da aula.",
    },
}


def first_img_from_note(note):
    for field in note.get("fields", {}).values():
        val = field.get("value", "")
        m = re.search(r'<img[^>]+src="([^"]+)"[^>]*>', val, re.I)
        if m:
            return m.group(0)
    return None


def image_from_anki(query):
    ids = call("findNotes", query=query)
    if not ids:
        return None
    for note in call("notesInfo", notes=ids[:30]):
        img = first_img_from_note(note)
        if img:
            return img
    return None


def image_from_file(path):
    p = ROOT / path
    if not p.exists():
        return None
    im = Image.open(p).convert("RGB")
    maxw = 700
    if im.width > maxw:
        im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    buf = _io.BytesIO()
    im.save(buf, "PNG")
    data = buf.getvalue()
    name = hashlib.md5(data).hexdigest() + ".png"
    call("storeMediaFile", filename=name, data=base64.b64encode(data).decode())
    return f'<img src="{name}" width="{min(im.width, 520)}">'


def get_extra(note):
    return note.get("fields", {}).get("Extra", {}).get("value", "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True
    if args.apply:
        LOCK.parent.mkdir(parents=True, exist_ok=True)
        try:
            with LOCK.open("x", encoding="ascii") as f:
                f.write(str(os.getpid()))
        except FileExistsError:
            raise SystemExit(f"apply já em execução: {LOCK}")
        atexit.register(lambda: LOCK.unlink(missing_ok=True))

    total_changed = 0
    for slug, src in SLUG_SOURCES.items():
        ids = call("findNotes", query=f'tag:{slug} tag:{NEEDS}')
        if not ids:
            continue
        img = image_from_anki(src["anki_query"]) if "anki_query" in src else image_from_file(src["file"])
        if not img:
            print(f"{slug}: {len(ids)} cards, mas nao achei imagem fonte")
            continue
        credit = src.get("credit", "")
        block = f'<br><br>{img}<br><i style="font-size:10pt;">{credit}</i>'
        print(f"{slug}: {len(ids)} cards receberiam imagem de contexto")
        if args.apply:
            for note in call("notesInfo", notes=ids):
                # Refetch imediatamente antes do update: não concatenar sobre
                # snapshot stale de outra execução.
                current = call("notesInfo", notes=[note["noteId"]])[0]
                extra = get_extra(current)
                if "<img" in extra.lower():
                    continue
                call("updateNoteFields", note={"id": note["noteId"], "fields": {"Extra": extra + block}})
                after = get_extra(call("notesInfo", notes=[note["noteId"]])[0])
                src = re.search(r'\bsrc="([^"]+)"', img, re.I)
                if src and len(re.findall(re.escape(src.group(1)), after, re.I)) != 1:
                    raise RuntimeError(f"pós-condição de imagem falhou na nota {note['noteId']}")
            call("addTags", notes=ids, tags=f"{HAS} {CTX}")
            call("removeTags", notes=ids, tags=NEEDS)
        total_changed += len(ids)
    print("total alvo:", total_changed, "| modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
