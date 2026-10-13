"""Prévia de oclusões vivas (imagem + máscara da pergunta e da resposta), para conferir no deck instalado.

    python3 -m nebli.io_previa <saida.png> nid [nid...]
"""
import re
import sys
from pathlib import Path

import fitz

from nebli.decks import Anki

M = Path.home() / "Library/Application Support/Anki2/User 1/collection.media"
SRC = re.compile(r'src="([^"]+)"')


def main(out, nids):
    A = Anki(); W, H = 520, 380
    notes = A("notesInfo", notes=[int(n) for n in nids])
    doc = fitz.open(); page = doc.new_page(width=W * 2, height=(H + 24) * len(notes))
    for r, n in enumerate(notes):
        f = {k: v["value"] for k, v in n["fields"].items()}
        img = M / SRC.search(f["Image"]).group(1)
        for c, mk in enumerate(("Question Mask", "Answer Mask")):
            rect = fitz.Rect(c * W + 4, r * (H + 24) + 20, (c + 1) * W - 4, r * (H + 24) + H + 20)
            page.insert_image(rect, filename=str(img), keep_proportion=True)
            m = SRC.search(f.get(mk, ""))
            if m:
                svg = fitz.open(str(M / m.group(1)))
                pdf = fitz.open("pdf", svg.convert_to_pdf())
                page.show_pdf_page(rect, pdf, 0, keep_proportion=True)
        rem = re.sub(r"<[^>]+>", " ", f.get("Remarks", ""))[:80]
        page.insert_text((6, r * (H + 24) + 14), f"{n['noteId']} {rem}", fontsize=11, color=(1, 0, 0))
    page.get_pixmap(dpi=70).save(out); print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
