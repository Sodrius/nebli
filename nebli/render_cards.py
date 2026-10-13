"""Renderiza frente/verso de cards vivos em PNG (PyMuPDF Story), para revisão visual sem depender de WebKit/Swift.

    python3 -m nebli.render_cards <busca-anki> <pasta-saida> [--largura 390] [--por-folha 6]

Gera <pasta>/card-<cid>.png (verso completo: frente + Extra, como o Anki mostra ao virar) e folhas folha-NN.png para ver
vários de uma vez. CSS dos modelos é descartado: é prévia de conteúdo (texto, cloze, negrito, imagem e tamanho relativo),
não teste do AnkiDroid.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import fitz

MEDIA = os.path.expanduser("~/Library/Application Support/Anki2/User 1/collection.media")


def call(a, **p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action": a, "version": 6, "params": p}).encode())))["result"]


def limpa(h):
    h = re.sub(r"<style.*?</style>|<script.*?</script>", "", h, flags=re.S | re.I)
    h = re.sub(r'<span class="cloze"[^>]*>', '<span style="color:#1565c0;font-weight:bold">', h)
    h = re.sub(r'<img([^>]*?)src="([^"]+)"[^>]*>', lambda m: f'<img src="{m.group(2)}" style="width:100%">', h)
    h = re.sub(r"\s(class|id|onclick|style)=\"[^\"]*\"", lambda m: m.group(0) if m.group(1) == "style" and "color" in m.group(0) else "", h)
    return h


def render(cid, html, largura, saida):
    doc = fitz.open()
    page = doc.new_page(width=largura, height=6000)
    spare, scale = page.insert_htmlbox(fitz.Rect(8, 8, largura - 8, 5992),
                                      f'<div style="font-family:sans-serif;font-size:13px">{html}</div>',
                                      archive=fitz.Archive(MEDIA), scale_low=1)
    usado = 5992 - spare if spare >= 0 else 6000
    page.set_cropbox(fitz.Rect(0, 0, largura, min(6000, usado + 16)))
    page.get_pixmap(dpi=110).save(saida)


def main(argv):
    busca, pasta = argv[0], Path(argv[1])
    largura = int(argv[argv.index("--largura") + 1]) if "--largura" in argv else 390
    pasta.mkdir(parents=True, exist_ok=True)
    cards = sorted(call("cardsInfo", cards=call("findCards", query=busca)), key=lambda c: c["due"])
    feitos = []
    for c in cards:
        out = pasta / f"card-{c['cardId']}.png"
        f = {k: v["value"] for k, v in c["fields"].items()}
        if "Text" in f:
            n = c["ord"] + 1
            frente = re.sub(r"\{\{c(\d+)::(.*?)(::[^}]*)?\}\}", lambda m: (f'<span style="color:#1565c0;font-weight:bold">[{m.group(2)}]</span>' if int(m.group(1)) == n else m.group(2)), f["Text"], flags=re.S)
            corpo = frente + "<hr>" + f.get("Extra", "")
        else:  # oclusão: cabeçalho, imagem e observações
            corpo = f.get("Header", "") + f.get("Image", "") + "<hr>" + f.get("Remarks", "")
        render(c["cardId"], f'<small>{c["cardId"]} · c{c["ord"] + 1} · flag {c["flags"]}</small><br>' + limpa(corpo), largura, str(out))
        feitos.append(out)
    por = int(argv[argv.index("--por-folha") + 1]) if "--por-folha" in argv else 6
    for f in range(0, len(feitos), por):
        doc = fitz.open(); W = largura * 3
        page = doc.new_page(width=W, height=2400)
        x = y = rowh = 0
        for i, p in enumerate(feitos[f:f + por]):
            pix = fitz.Pixmap(str(p)); s = largura / pix.width; h = pix.height * s
            if i % 3 == 0 and i: y += rowh + 6; rowh = 0
            x = (i % 3) * largura
            page.insert_image(fitz.Rect(x, y, x + largura, y + h), filename=str(p)); rowh = max(rowh, h)
        page.set_cropbox(fitz.Rect(0, 0, W, min(2400, y + rowh + 4)))
        page.get_pixmap(dpi=72).save(str(pasta / f"folha-{f // por + 1:02d}.png"))
    print(len(feitos), "cards;", (len(feitos) + por - 1) // por, "folhas em", pasta)


if __name__ == "__main__":
    main(sys.argv[1:])
