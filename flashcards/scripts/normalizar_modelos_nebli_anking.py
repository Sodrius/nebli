#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Normaliza note types legados dos NEBLIcards para visual AnKing-like.

Nao altera o note type AnKingOverhaul original. O alvo principal e o modelo
legado "Cloze Medicina - Mecanismo Unico", que deixava cards autorais com
aparencia de card NEBLI/prototipo em vez de AnKing.

Uso:
  python flashcards/scripts/normalizar_modelos_nebli_anking.py --dry-run
  python flashcards/scripts/normalizar_modelos_nebli_anking.py --apply
"""
import argparse
import sys

from anki import call

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

LEGACY_MODELS = [
    "Cloze Medicina - Mecanismo Único",
]

ANKING_LIKE_CSS = r"""
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  font-size: 28px;
  line-height: 1.45;
  text-align: center;
  color: #111827;
  background: #ffffff;
  padding: 18px;
}

.prompt, .extra, .media {
  max-width: 760px;
  margin-left: auto;
  margin-right: auto;
}

.cloze {
  font-weight: 700;
  color: #2563eb;
}

#answer {
  border: 0;
  border-top: 1px solid #d1d5db;
  margin: 22px auto;
  max-width: 760px;
}

.extra {
  margin-top: 14px;
  font-size: 20px;
  line-height: 1.45;
  text-align: left;
  color: #1f2937;
}

.extra b, .extra strong {
  font-weight: 700;
}

.media {
  margin-top: 16px;
  text-align: center;
}

img {
  max-width: 100%;
  max-height: 520px;
  height: auto;
  width: auto;
}

.nightMode .card,
.night_mode .card {
  color: #e5e7eb;
  background: #111827;
}

.nightMode .extra,
.night_mode .extra {
  color: #d1d5db;
}
"""

ANKING_LIKE_TEMPLATES = {
    "Cloze": {
        "Front": '<div class="prompt">{{cloze:Text}}</div>',
        "Back": (
            '<div class="prompt">{{cloze:Text}}</div>\n'
            '<hr id="answer">\n'
            '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}\n'
            '{{#Image}}<div class="media">{{Image}}</div>{{/Image}}'
        ),
    }
}


def existing_legacy_models():
    names = set(call("modelNames"))
    return [m for m in LEGACY_MODELS if m in names]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True

    found = existing_legacy_models()
    if not found:
        print("Nenhum modelo legado NEBLI encontrado.")
        return

    for model in found:
        n_notes = len(call("findNotes", query=f'note:"{model}" tag:NEBLI::*'))
        print(f"{model}: {n_notes} notas NEBLI afetadas")
        if args.apply:
            call("updateModelStyling", model={"name": model, "css": ANKING_LIKE_CSS})
            call("updateModelTemplates", model={"name": model, "templates": ANKING_LIKE_TEMPLATES})
            call(
                "addTags",
                notes=call("findNotes", query=f'note:"{model}" tag:NEBLI::*'),
                tags="NEBLI::legacy_model_anking_like",
            )
    print("modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
