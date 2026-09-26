"""Extract the original embedded rectal arterial figure without altering it."""
from pathlib import Path
import pymupdf

here = Path(__file__).parent
doc = pymupdf.open(here / "slides.pdf")
for xref in (166, 167):
    value = doc.extract_image(xref)
    target = here / f"slide22-{xref}.{value['ext']}"
    target.write_bytes(value["image"])
    print(target.name, target.stat().st_size)
