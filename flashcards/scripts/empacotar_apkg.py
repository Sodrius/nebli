#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEBLI -- empacotar_apkg.py
Empacota NEBLIcards autorais de um slug num .apkg self-contained via genanki.

Modo tablet/sem-PC (canon 2026-08-07): quando o AnkiConnect não está
alcançável (Davi sem PC, só tablet + AnkiDroid), este script gera o
.apkg pronto pra importar via AnkiDroid + sync AnkiWeb. A árvore
`NEBLI::<UC>::<Prova>::<Matéria>::<Aula>` vai embutida no arquivo;
quando o Davi importa, o deck aparece direto no lugar certo.

Entrada:
    flashcards/cards-nebli/<slug>.json  -- estrutura documentada abaixo

Saída:
    resumos-gerados/<Aula curta>.apkg   -- self-contained, importável no
                                          AnkiDroid / Anki desktop, com
                                          todas as imagens embutidas.

Uso:
    python3 flashcards/scripts/empacotar_apkg.py <slug>

Formato esperado do JSON (flashcards/cards-nebli/<slug>.json):
{
  "meta": {
    "uc": "UC-8",
    "prova": "P1",
    "materia": "Anatomia",
    "aula_curta": "Esôfago, estômago e intestino delgado",
    "slug": "digest-01-esofago-estomago-intestino",
    "deck_id": 1234567890,          # opcional; se ausente, deriva do slug
    "model_id": 1607392319          # opcional; default = NEBLI cloze model
  },
  "cards": [
    {
      "id": "digest-01-c001",       # opcional; usado como guid estável
      "type": "cloze",              # único tipo suportado (canon R9)
      "front": "<b>Anatomia.</b> A porção {{c1::cervical}} do esôfago...",
      "extra": "1-2 frases em voz NEBLI...",
      "image": "figuras/digest-01/slide-05.png",   # opcional; path relativo à raiz do repo
      "tags": ["NEBLI::digest-01", "NEBLI::gerado"]
    },
    ...
  ]
}

Naming do .apkg: usa exatamente `meta.aula_curta` (mesmo nome curto do
Drive e do PDF). Espaços permitidos; caracteres proibidos em FS
(`/`, `\\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`) são substituídos por `-`.
"""

from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import genanki
except ImportError:
    print("x genanki nao instalado. Rode: pip install genanki --break-system-packages", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent.parent  # /home/user/nebli
CARDS_DIR = ROOT / "flashcards" / "cards-nebli"
SAIDA_DIR = ROOT / "resumos-gerados"

# ID de modelo estável para o NEBLI cloze -- mudar rompe reviews existentes.
NEBLI_CLOZE_MODEL_ID = 1607392319

# CSS AnKing-like: cloze azul negrito, fonte 28px, imagem centralizada
NEBLI_CSS = """
.card {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 20px;
  text-align: left;
  color: #1f2033;
  background-color: #fdfaf3;
  padding: 20px 24px;
  line-height: 1.5;
}
.cloze {
  font-weight: bold;
  color: #1f4e79;
}
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 12px auto;
}
hr#answer {
  margin: 18px 0 12px 0;
  border: 0;
  border-top: 2px solid #1f4e79;
}
.extra {
  font-size: 17px;
  color: #4a4a4a;
  margin-top: 10px;
  padding: 12px 14px;
  background-color: #fef7e0;
  border-left: 3px solid #cba135;
  border-radius: 4px;
}
.tags {
  font-size: 12px;
  color: #8a8a8a;
  margin-top: 12px;
}
"""

NEBLI_CLOZE_MODEL = genanki.Model(
    NEBLI_CLOZE_MODEL_ID,
    "NEBLI Cloze",
    fields=[
        {"name": "Text"},
        {"name": "Extra"},
        {"name": "Image"},
    ],
    templates=[
        {
            "name": "NEBLI Cloze Card",
            "qfmt": "{{cloze:Text}}<br>{{Image}}",
            "afmt": "{{cloze:Text}}<br>{{Image}}"
                    "{{#Extra}}<hr id=\"answer\"><div class=\"extra\">{{Extra}}</div>{{/Extra}}",
        },
    ],
    css=NEBLI_CSS,
    model_type=genanki.Model.CLOZE,
)


def deck_id_from_slug(slug: str) -> int:
    """Deriva deck_id estável do slug (mesmo slug → mesmo id → merge no import)."""
    h = hashlib.sha256(slug.encode("utf-8")).digest()
    # genanki deck_ids são inteiros ~10 dígitos
    return int.from_bytes(h[:6], "big") % (2 ** 31 - 1) + 1


def guid_from_card_id(card_id: str) -> str:
    """Guid estável do card, resistente a re-import."""
    return hashlib.sha256(card_id.encode("utf-8")).hexdigest()[:16]


def sanitizar_filename(nome: str) -> str:
    """Remove/substitui caracteres proibidos em nome de arquivo."""
    proibidos = r'[/\\:*?"<>|]'
    return re.sub(proibidos, "-", nome).strip()


def montar_deck(json_path: Path) -> tuple[genanki.Deck, list[Path]]:
    """Lê o JSON, monta o Deck genanki + lista de arquivos de mídia."""
    data = json.loads(json_path.read_text(encoding="utf-8"))
    meta = data["meta"]
    cards = data["cards"]

    if not cards:
        raise SystemExit(f"x JSON sem cards: {json_path}")

    # nome hierárquico da árvore NEBLI
    uc = meta["uc"]
    prova = meta["prova"]
    materia = meta["materia"]
    aula_curta = meta["aula_curta"]
    slug = meta["slug"]

    deck_name = f"NEBLI::{uc}::{prova}::{materia}::{aula_curta}"
    deck_id = meta.get("deck_id") or deck_id_from_slug(slug)

    deck = genanki.Deck(deck_id, deck_name)

    media_files: list[Path] = []
    media_names_seen: set[str] = set()

    for c in cards:
        if c.get("type", "cloze") != "cloze":
            print(f"! card {c.get('id','?')} tem type={c.get('type')} != cloze -- pulando (canon R9)", file=sys.stderr)
            continue

        text = c["front"]
        extra = c.get("extra", "").strip()
        img_field = ""

        img_rel = c.get("image", "").strip()
        if img_rel:
            img_path = (ROOT / img_rel).resolve()
            if not img_path.exists():
                print(f"! imagem nao encontrada: {img_rel} (card {c.get('id','?')})", file=sys.stderr)
            else:
                img_name = img_path.name
                # se colisão de nome, renomear pra evitar overwrite no import
                if img_name in media_names_seen and img_path not in media_files:
                    stem = img_path.stem
                    suf = img_path.suffix
                    dupe_count = sum(1 for m in media_files if m.stem == stem)
                    img_name = f"{stem}_{dupe_count}{suf}"
                media_names_seen.add(img_name)
                if img_path not in media_files:
                    media_files.append(img_path)
                img_html = f'<img src="{img_name}">'
                image_side = str(c.get("image_side", "both")).lower()
                if image_side == "answer":
                    extra = f"{extra}<div>{img_html}</div>".strip()
                elif image_side == "both":
                    img_field = img_html
                else:
                    raise SystemExit(
                        f"x image_side invalido no card {c.get('id','?')}: {image_side} "
                        "(use both|answer)"
                    )

        tags = c.get("tags", [f"NEBLI::{slug}", "NEBLI::gerado"])
        guid = c.get("id") and guid_from_card_id(c["id"])

        note = genanki.Note(
            model=NEBLI_CLOZE_MODEL,
            fields=[text, extra, img_field],
            tags=tags,
            guid=guid,
        )
        deck.add_note(note)

    return deck, media_files, aula_curta


def empacotar(slug: str) -> Path:
    json_path = CARDS_DIR / f"{slug}.json"
    if not json_path.exists():
        raise SystemExit(f"x cards nao encontrados: {json_path}")

    deck, media_files, aula_curta = montar_deck(json_path)

    SAIDA_DIR.mkdir(parents=True, exist_ok=True)
    apkg_path = SAIDA_DIR / f"{sanitizar_filename(aula_curta)}.apkg"

    pkg = genanki.Package(deck)
    pkg.media_files = [str(p) for p in media_files]
    pkg.write_to_file(str(apkg_path))

    n = len(deck.notes)
    tamanho_kb = apkg_path.stat().st_size / 1024
    print(f"v deck '{deck.name}' com {n} cards + {len(media_files)} imagem(ns) → {apkg_path.relative_to(ROOT)}")
    print(f"  tamanho: {tamanho_kb:.1f} KB")
    return apkg_path


def main():
    ap = argparse.ArgumentParser(description="Empacota NEBLIcards de um slug num .apkg self-contained.")
    ap.add_argument("slug", help="slug da aula (arquivo em flashcards/cards-nebli/<slug>.json)")
    args = ap.parse_args()
    empacotar(args.slug)


if __name__ == "__main__":
    main()
