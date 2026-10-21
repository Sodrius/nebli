"""F-20261022-CLAUDE-01: a imagem do card bate com a pergunta/cloze dele? (gate duro `imagens_batem`).

    python3 -m nebli.imagens_cards folha <corrida>     # visual/imagens-cards-NN.png: cada imagem de card ao lado do texto do card
    python3 -m nebli.imagens_cards pendentes <corrida> # chaves de card com imagem ainda sem veredito em imagens-batem.json

imagens-batem.json: {"<chave do card>": {"veredito": "ok", "porque": "o que a imagem mostra e como ela responde ao cloze (≥ 40 caracteres)"}}.
Veredito "ok" só depois de olhar a folha; "trocar" e "retirar" reprovam o gate até o card ser corrigido.
"""
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

MEDIA = Path.home() / "Library/Application Support/Anki2/User 1/collection.media"
IMG = re.compile(r'<img[^>]*src="([^"]+)"')


def cartoes_com_imagem(plan):
    out = []
    for e in plan.get("entries", []):
        if e.get("kind") == "slideio":
            continue
        campos = e.get("fields") or {}
        srcs = []
        for campo in ("Text", "Header", "Extra", "Back Extra"):
            srcs += [(campo, m) for m in IMG.findall(campos.get(campo, "") or "")]
        if srcs:
            frente = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", campos.get("Text", "") or ""))).strip()
            out.append((e["key"], frente, srcs))
    return out


def pendentes(run, plan):
    try:
        v = json.loads((Path(run) / "imagens-batem.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        v = {}
    ok = lambda k: isinstance(v.get(k), dict) and v[k].get("veredito") == "ok" and len(str(v[k].get("porque", "")).strip()) >= 40
    return [k for k, _, _ in cartoes_com_imagem(plan) if not ok(k)], v


def folha(run, plan, cols=2, rows=4):
    import fitz
    run = Path(run)
    itens = []
    for key, frente, srcs in cartoes_com_imagem(plan):
        for campo, f in srcs:
            itens.append((key, frente, campo, f))
    W, H = 640, 330
    tmp = Path(tempfile.mkdtemp())
    por = cols * rows
    saidas = []
    for n in range(0, len(itens), por):
        doc = fitz.open()
        page = doc.new_page(width=W * cols, height=H * rows)
        for k, (key, frente, campo, f) in enumerate(itens[n:n + por]):
            x, y = (k % cols) * W, (k // cols) * H
            page.insert_textbox(fitz.Rect(x + 6, y + 2, x + W - 6, y + 62), f"{key} [{campo}]\n{frente[:230]}", fontsize=9, color=(0.7, 0, 0))
            src = MEDIA / f
            png = tmp / f"{n}-{k}.png"
            subprocess.run(["sips", "-s", "format", "png", str(src), "--out", str(png)], capture_output=True)
            try:
                page.insert_image(fitz.Rect(x + 6, y + 64, x + W - 6, y + H - 4), filename=str(png), keep_proportion=True)
            except Exception as ex:
                page.insert_text((x + 6, y + 100), f"erro {ex}"[:70], fontsize=9)
        out = run / "visual" / f"imagens-cards-{n // por + 1:02d}.png"
        out.parent.mkdir(exist_ok=True)
        page.get_pixmap(dpi=80).save(out)
        saidas.append(out)
    return saidas


def main(argv=None):
    a = argv or sys.argv[1:]
    cmd, run = a[0], Path(a[1])
    plan = json.loads((run / "plan.json").read_text(encoding="utf-8"))
    if cmd == "folha":
        for p in folha(run, plan):
            print(p)
    else:
        falta, _ = pendentes(run, plan)
        print(len(falta), "cards com imagem sem veredito:", " ".join(falta))


if __name__ == "__main__":
    main()
