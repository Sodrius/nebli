"""Renderiza um card de oclusão (imagem + máscara SVG de pergunta/resposta) como PNG, para inspeção visual.

    python3 -m nebli.io_render <nid> <saida.png> [--lado Q|A]
"""
import json, os, re, sys, urllib.request
import fitz

MEDIA = os.path.expanduser("~/Library/Application Support/Anki2/User 1/collection.media")


def call(a, **p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action": a, "version": 6, "params": p}).encode())))["result"]


def render(nid, saida, lado="Q", fields=None):
    f = fields or {k: v["value"] for k, v in call("notesInfo", notes=[int(nid)])[0]["fields"].items()}
    src = re.search(r'src="([^"]+)"', f["Image"]).group(1)
    mask = re.search(r'src="([^"]+)"', f["Question Mask" if lado == "Q" else "Answer Mask"]).group(1)
    img = fitz.open(os.path.join(MEDIA, src))
    pdfimg = fitz.open("pdf", img.convert_to_pdf())
    r = pdfimg[0].rect
    doc = fitz.open(); page = doc.new_page(width=r.width, height=r.height)
    page.show_pdf_page(page.rect, pdfimg, 0)
    svg = fitz.open(os.path.join(MEDIA, mask))
    page.show_pdf_page(page.rect, fitz.open("pdf", svg.convert_to_pdf()), 0, keep_proportion=False)
    page.get_pixmap(dpi=72 * min(1, 1400 / r.width) if r.width > 0 else 72).save(saida)
    return saida


if __name__ == "__main__":
    a = sys.argv[1:]
    print(render(a[0], a[1], a[a.index("--lado") + 1] if "--lado" in a else "Q"))
