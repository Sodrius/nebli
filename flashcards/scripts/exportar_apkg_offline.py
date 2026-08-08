#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEBLI -- exportar_apkg_offline.py

Empacota um lote de NEBLIcards (`flashcards/cards-nebli/<slug>.json`) num
`.apkg` importavel, SEM depender do AnkiConnect.

Por que existe: o pipeline canonico monta o deck-aula por AnkiConnect
(`montar_deck_aula.py`), que exige o Anki vivo em localhost. Numa sessao
remota isso e inalcancavel, e o `.apkg` e o unico caminho de entrega -- o
Davi importa com dois cliques e a arvore de deck ja vem correta.

O modelo replica o AnKingOverhaul no essencial: cloze unico, campo Extra,
cloze em azul/negrito, corpo grande. Nao substitui o note type real do Davi;
ao importar, os cards entram com este modelo proprio e podem ser
normalizados depois por `normalizar_modelos_nebli_anking.py`.

Uso:
  python3 flashcards/scripts/exportar_apkg_offline.py <slug> --deck "NEBLI::..."
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

try:
    import genanki
except ImportError:
    sys.exit("genanki ausente -- rode: pip install genanki")

ROOT = Path(__file__).resolve().parents[2]


def stable_id(texto: str) -> int:
    """ID deterministico: reexportar o mesmo lote nao duplica o deck/modelo."""
    h = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    return 1 << 30 | (int(h[:8], 16) % (1 << 30))


CSS = """
.card {
  font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  font-size: 26px;
  text-align: center;
  color: #1F2E3D;
  background-color: #FFFFFF;
  line-height: 1.5;
}
.cloze { font-weight: bold; color: #1E88E5; }
#extra {
  font-size: 19px;
  color: #445;
  margin-top: 18px;
  padding-top: 12px;
  border-top: 1px solid #DDD;
  text-align: left;
  max-width: 640px;
  margin-left: auto;
  margin-right: auto;
}
#topico { font-size: 13px; color: #8A94A0; margin-top: 14px; }
"""


def build_model():
    return genanki.Model(
        stable_id("NEBLI::modelo::cloze-mecanismo-unico::v2"),
        "NEBLI Cloze (mecanismo único)",
        fields=[{"name": "Text"}, {"name": "Extra"}, {"name": "Topico"}],
        templates=[{
            "name": "Cloze",
            "qfmt": "{{cloze:Text}}",
            "afmt": "{{cloze:Text}}"
                    "<div id=extra>{{Extra}}</div>"
                    "<div id=topico>{{Topico}}</div>",
        }],
        css=CSS,
        model_type=genanki.Model.CLOZE,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--deck", required=True, help="Arvore-alvo NEBLI::...")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    src = ROOT / "flashcards" / "cards-nebli" / f"{args.slug}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    cards = data["cards"]

    model = build_model()
    deck = genanki.Deck(stable_id(args.deck), args.deck)
    for c in cards:
        deck.add_note(genanki.Note(
            model=model,
            fields=[c["text"], c.get("extra", ""), c.get("topico", "")],
            tags=[t.replace(" ", "_") for t in c.get("tags", [])],
            guid=genanki.guid_for(c["id"]),
        ))

    out = Path(args.out) if args.out else (
        ROOT / "flashcards" / "decks-apkg" / f"{data.get('aula', args.slug)}.apkg")
    out.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(deck).write_to_file(str(out))
    print(f"ok {out}")
    print(f"   deck: {args.deck}")
    print(f"   notas: {len(cards)} (1 cloze por nota = {len(cards)} cards)")


if __name__ == "__main__":
    main()
