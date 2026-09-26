"""Render the authenticated lecture PDF for source visual audit."""
from pathlib import Path
import pymupdf

here = Path(__file__).parent
pdf = pymupdf.open(here / "slides.pdf")
out = here / "slides-pages"
out.mkdir(exist_ok=True)
for i, page in enumerate(pdf, 1):
    page.get_pixmap(matrix=pymupdf.Matrix(1.35, 1.35), alpha=False).save(out / f"p{i:02}.png")
print(len(pdf), "pages rendered")
