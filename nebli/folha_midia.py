"""Folha de contato de arquivos da mídia do Anki por prefixo. python3 -m nebli.folha_midia <saida.png> prefixo [prefixo...]"""
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz

M = Path.home() / "Library/Application Support/Anki2/User 1/collection.media"


def main(out, prefs, W=420, H=300, cols=4):
    tmp = Path(tempfile.mkdtemp())
    doc = fitz.open(); page = doc.new_page(width=W * cols, height=(H + 20) * ((len(prefs) + cols - 1) // cols))
    for k, p in enumerate(prefs):
        f = next(iter(M.glob(p + "*")), None); x, y = (k % cols) * W, (k // cols) * (H + 20)
        png = tmp / f"{k}.png"; subprocess.run(["sips", "-s", "format", "png", str(f), "--out", str(png)], capture_output=True)
        try:
            page.insert_image(fitz.Rect(x + 4, y + 18, x + W - 4, y + H + 16), filename=str(png), keep_proportion=True)
        except Exception as ex:
            page.insert_text((x + 6, y + 60), str(ex)[:50], fontsize=9)
        page.insert_text((x + 4, y + 12), p[:12], fontsize=11, color=(1, 0, 0))
    page.get_pixmap(dpi=55).save(out); print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
