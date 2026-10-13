"""Preserva fontes, extrai texto e gera folhas visuais para leitura pelo executor."""
from pathlib import Path
import hashlib, json, shutil
import fitz

HERE = Path(__file__).resolve().parent
ROOT = Path('/Users/davisousa/Library/CloudStorage/GoogleDrive-dpbdes@gmail.com/Mon Drive/MEGA DRIVE')
UC = ROOT / 'Medicina/Material de estudo/A - Primeiro ano (2026)/UC19'
SOURCES = {
    'slides': UC / '01 - Introdução à Farmacologia e mecanismos de ação dos fármacos/Introdução à Farmacologia - slides - ES.pdf',
    'rang': ROOT / 'Outros/Livros/Bibliografia principal - medicina/Rang _ Dale Farmacologia 7 Ed.pdf',
    **{p.stem:p for p in (UC/'Outros').glob('*.pdf')},
}
fitz.TOOLS.mupdf_display_errors(False)
(HERE/'fontes').mkdir(exist_ok=True)
(HERE/'visual').mkdir(exist_ok=True)
inventory = []
for name, src in SOURCES.items():
    dst = HERE/'fontes'/f'{name}.pdf'
    if not dst.exists(): shutil.copy2(src,dst)
    doc = fitz.open(dst)
    # Rang caps. 1–3: pp. impressas 1–48, PDF 27–74.
    pages = range(26,74) if name == 'rang' else range(len(doc))
    (HERE/'fontes'/f'{name}.txt').write_text('\n\n'.join(f'=== PDF {i+1} ===\n'+doc[i].get_text() for i in pages))
    inventory.append({'id':name,'original':str(src),'arquivo':str(dst.relative_to(HERE)), 'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'paginas_pdf':[i+1 for i in pages], 'leitura':'extraído; leitura ainda não certificada'})
    if name == 'slides':
        for start in range(0,len(doc),6):
            sheetdoc=fitz.open(); sheet=sheetdoc.new_page(width=1600,height=1560)
            for offset in range(min(6,len(doc)-start)):
                p=doc[start+offset]
                pix=p.get_pixmap(matrix=fitz.Matrix(1.4,1.4).prerotate(90),clip=fitz.Rect(135,135,460,708),alpha=False)
                x=(offset%2)*800; y=(offset//2)*520
                sheet.insert_image(fitz.Rect(x,y+30,x+790,y+515),stream=pix.tobytes('png'))
                sheet.insert_text((x+8,y+20),f'Slide {start+offset+1}',fontsize=17)
            sheet.get_pixmap().save(HERE/'visual'/f'slides-{start+1:02}.jpg')
(HERE/'fontes-inventario.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
print([(r['id'],len(r['paginas_pdf'])) for r in inventory])
