"""sheet.py out.png nid[:campo] ... — baixa imagens das notas e monta prancha rotulada (somente leitura)."""
import sys, re, base64, fitz
sys.path.insert(0, '/Users/davisousa/NEBLI')
from nebli.decks import Anki
A = Anki(); out = sys.argv[1]; items = []
for arg in sys.argv[2:]:
    nid, _, fld = arg.partition(':'); n = A('notesInfo', notes=[int(nid)])[0]
    txt = re.sub(r'<[^>]+>', '', n['fields'].get('Text', {'value': ''})['value'] or n['fields'].get('Title', {'value': ''})['value'])[:60]
    for k, v in n['fields'].items():
        if fld and k != fld: continue
        for img in re.findall(r'src="([^"]+)"', v['value']):
            if img.endswith('.svg'): continue
            d = A('retrieveMediaFile', filename=img)
            if d:
                p = f"visual/_{img}"; open(p, "wb").write(base64.b64decode(d))
                if open(p, "rb").read(4) == b"RIFF":
                    import subprocess; q = f"visual/cv_{img}.png"; subprocess.run(["sips", "-s", "format", "png", p, "--out", q], capture_output=True); p = q
                items.append((p, f"{nid} {k} {txt}"))
cols = 4; W = 2000; cw = W / cols; ch = cw * 0.85; rows = (len(items) + cols - 1) // cols
doc = fitz.open(); pg = doc.new_page(width=W, height=max(rows, 1) * ch)
for i, (p, lab) in enumerate(items):
    r = fitz.Rect((i % cols) * cw, (i // cols) * ch + 16, (i % cols + 1) * cw - 6, (i // cols + 1) * ch - 4)
    try: pg.insert_image(r, filename=p, keep_proportion=True)
    except Exception as e: print('ERR', p, e)
    pg.insert_text(((i % cols) * cw + 3, (i // cols) * ch + 13), lab[:70], fontsize=12, color=(1, 0, 0))
pg.get_pixmap(dpi=60).save(out); print(len(items), 'imagens')
