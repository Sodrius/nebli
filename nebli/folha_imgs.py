"""Folha de contato das figuras de notas do acervo, para escolher imagem olhando. python3 -m nebli.folha_imgs <saida.png> nid [nid...]"""
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz

from nebli.ilustrar import imgs, SRC

MEDIA = Path.home() / "Library/Application Support/Anki2/User 1/collection.media"


def sheet(out, nids, cell=(420, 320), cols=3):
    items = []
    for n in nids:
        for i, tag in enumerate(imgs(n)[:3]):
            items.append((f"{n}#{i}", MEDIA / SRC.search(tag).group(1)))
    tmp = Path(tempfile.mkdtemp())
    W, H = cell; rows = (len(items) + cols - 1) // cols
    doc = fitz.open(); page = doc.new_page(width=W * cols, height=(H + 20) * max(rows, 1))
    for k, (label, f) in enumerate(items):
        x, y = (k % cols) * W, (k // cols) * (H + 20)
        png = tmp / f"{k}.png"
        subprocess.run(["sips", "-s", "format", "png", str(f), "--out", str(png)], capture_output=True)
        try:
            page.insert_image(fitz.Rect(x + 4, y + 18, x + W - 4, y + H + 16), filename=str(png), keep_proportion=True)
        except Exception as ex:
            page.insert_text((x + 6, y + 60), f"erro {ex}"[:60], fontsize=9)
        page.insert_text((x + 4, y + 12), label, fontsize=11, color=(1, 0, 0))
    page.get_pixmap(dpi=60).save(out)
    print(out, len(items))


if __name__ == "__main__":
    sheet(sys.argv[1], [int(x) for x in sys.argv[2:]])
