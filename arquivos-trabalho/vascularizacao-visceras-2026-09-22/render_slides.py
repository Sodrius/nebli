"""Renderiza o PDF de slides em páginas e folhas de contato para revisão visual."""
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "rendered"
OUT.mkdir(exist_ok=True)
doc = fitz.open(ROOT / "slides.pdf")
page_paths = []
for index, page in enumerate(doc):
    path = OUT / f"page-{index + 1:02d}.png"
    page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False, annots=False).save(path)
    page_paths.append(path)

thumb_w, thumb_h = 320, 240
for sheet_index in range(0, len(page_paths), 12):
    batch = page_paths[sheet_index:sheet_index + 12]
    sheet = Image.new("RGB", (thumb_w * 4, (thumb_h + 30) * 3), "white")
    draw = ImageDraw.Draw(sheet)
    for local_index, path in enumerate(batch):
        image = Image.open(path).convert("RGB")
        image.thumbnail((thumb_w - 10, thumb_h - 10))
        x = (local_index % 4) * thumb_w + (thumb_w - image.width) // 2
        y = (local_index // 4) * (thumb_h + 30) + (thumb_h - image.height) // 2
        sheet.paste(image, (x, y))
        draw.text((local_index % 4 * thumb_w + 8, local_index // 4 * (thumb_h + 30) + thumb_h + 5), f"p. {sheet_index + local_index + 1}", fill="black")
    sheet.save(OUT / f"contact-{sheet_index // 12 + 1}.png")
print({"pages": len(page_paths), "contact_sheets": (len(page_paths) + 11) // 12})
