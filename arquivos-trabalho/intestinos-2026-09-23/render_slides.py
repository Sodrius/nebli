from pathlib import Path
import pymupdf

root = Path(__file__).parent
doc = pymupdf.open(root / 'slides.pdf')
out = root / 'pages'
out.mkdir(exist_ok=True)
for i, page in enumerate(doc):
    page.get_pixmap(matrix=pymupdf.Matrix(1.4, 1.4), alpha=False).save(out / f'{i+1:02d}.png')
    (out / f'{i+1:02d}.txt').write_text(page.get_text(), encoding='utf-8')
print(f'{len(doc)} pages rendered')
