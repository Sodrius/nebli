#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""montar_apkg_offline.py — monta o .apkg do deck-aula NEBLI sem AnkiConnect.

Usa o note type REAL do AnKing (AnKingOverhaul, model id 1659130414530) extraído
de um .apkg do próprio Davi, para que a importação caia no note type existente
da coleção dele (mesmo CSS, mesmo comportamento, sem duplicar modelo).

Uso:
  python flashcards/scripts/montar_apkg_offline.py <slug> "<Deck::Completo>" <saida.apkg>
"""
import json, os, sys, html
import genanki

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_JSON = os.path.join(ROOT, "arquivos-trabalho", "anking-model-overhaul.json")


def build_model():
    m = json.load(open(MODEL_JSON, encoding="utf-8"))
    return genanki.Model(
        int(m["id"]),
        m["name"],
        fields=[{"name": f["name"]} for f in m["flds"]],
        templates=[{"name": t["name"], "qfmt": t["qfmt"], "afmt": t["afmt"]} for t in m["tmpls"]],
        css=m["css"],
        model_type=genanki.Model.CLOZE,
    ), [f["name"] for f in m["flds"]]


def main():
    slug = sys.argv[1]
    deck_name = sys.argv[2]
    out = sys.argv[3]
    data = json.load(open(os.path.join(ROOT, "flashcards", "cards-nebli", slug + ".json"), encoding="utf-8"))
    media_dir = os.path.join(ROOT, "arquivos-trabalho", "media-" + slug.split("-")[0] + "26")
    if not os.path.isdir(media_dir):
        media_dir = os.path.join(ROOT, "arquivos-trabalho", "media-bioq26")
    mapping = json.load(open(os.path.join(media_dir, "_map.json"), encoding="utf-8"))

    model, field_names = build_model()
    deck = genanki.Deck(abs(hash(deck_name)) % (10 ** 10), deck_name)
    media = set()
    tags = [t.replace(" ", "_") for t in data.get("tags_padrao", [])]

    for c in data["cards"]:
        extra = html.escape(c["extra"], quote=False)
        img = c.get("image")
        if img and img in mapping:
            fn = mapping[img]
            extra += f'<br><img src="{fn}">'
            extra += ('<div style="font-size:11px;color:#888;">Image credit: '
                      'course lecture slide (Controle Hormonal), used for personal study.</div>')
            media.add(os.path.join(media_dir, fn))
        extra += ('<div style="margin-top:10px;font-size:11px;color:#b08a3e;">&#10022; NEBLIcard</div>')
        vals = [""] * len(field_names)
        vals[0] = c["text"]
        vals[1] = extra
        note = genanki.Note(model=model, fields=vals, tags=tags + ["NEBLI::" + c["conceito"].replace(".", "_")])
        deck.add_note(note)

    pkg = genanki.Package(deck)
    pkg.media_files = sorted(media)
    pkg.write_to_file(out)
    print(f"OK -> {out}  ({len(data['cards'])} notas, {len(media)} imagens)")


if __name__ == "__main__":
    main()
