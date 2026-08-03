#!/usr/bin/env python3
"""Aplica o padrão permanente de rótulo temático em inglês nos decks-aula."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

build = ROOT / "flashcards/scripts/build_card.py"
text = build.read_text(encoding="utf-8")
old = '''    "anato": "Anatomia", "biocel": "Biologia celular", "biomol": "Biologia molecular",\n    "bioq": "Bioquímica", "embrio": "Embriologia", "fisio": "Fisiologia",\n    "histo": "Histologia", "etim": "Etimologia",'''
new = '''    "anato": "Anatomy", "biocel": "Cell Biology", "biomol": "Molecular Biology",\n    "bioq": "Biochemistry", "embrio": "Embryology", "fisio": "Physiology",\n    "histo": "Histology", "etim": "Etymology",'''
if old not in text:
    raise SystemExit("build_card.py: mapa temático inesperado")
build.write_text(text.replace(old, new), encoding="utf-8")

helper = '''\n\nTHEME_BY_SLUG = {\n    "anato": "Anatomy", "biocel": "Cell Biology", "biomol": "Molecular Biology",\n    "bioq": "Biochemistry", "embrio": "Embryology", "fisio": "Physiology",\n    "histo": "Histology", "etim": "Etymology",\n}\n\ndef _theme_label(slug):\n    return THEME_BY_SLUG.get((slug or "").split("-", 1)[0], "Medicine")\n\ndef _with_english_theme(value, slug):\n    if not value or value.lstrip().startswith("<b>"):\n        return value\n    return f"<b>{_theme_label(slug)}.</b> " + value\n'''

for rel, needle in [
    ("flashcards/scripts/copiar_curadoria_para_deck.py", 'def _build_index(pool_tags):'),
    ("flashcards/scripts/montar_deck_aula.py", 'def main():'),
]:
    path = ROOT / rel
    body = path.read_text(encoding="utf-8")
    if "THEME_BY_SLUG" not in body:
        body = body.replace(needle, helper + "\n" + needle)
    target = 'fields = {name: v["value"] for name, v in n["fields"].items()}'
    if target in body:
        body = body.replace(target, target + '\n        if "Text" in fields:\n            fields["Text"] = _with_english_theme(fields["Text"], args.slug)', 1)
    else:
        target = 'fields = {k: v["value"] for k, v in n["fields"].items()\n                  if k not in ("ankihub_id",)}'
        if target not in body:
            raise SystemExit(f"{rel}: ponto de cópia não encontrado")
        body = body.replace(target, target + '\n        if "Text" in fields:\n            fields["Text"] = _with_english_theme(fields["Text"], a.slug)', 1)
    path.write_text(body, encoding="utf-8")

print("OK: rótulo temático inglês obrigatório em autorais e cópias de AnKing")
