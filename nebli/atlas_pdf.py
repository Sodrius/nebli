"""Recorte de região de página de PDF (atlas/livro) em alta resolução, para virar imagem focal de card.

    python3 -m nebli.atlas_pdf <pdf> <pagina0> <x0,y0,x1,y1 em pontos> <saida.png> [--dpi 200]

--limpo: extrai só a ilustração de fundo (sem linhas-guia/rótulos vetoriais, ex.: Netter).
Pontos = coordenadas da página renderizada a 72 dpi. Depois, `nebli.seta` põe a seta; guardar origem/página/caixa no
registro da corrida, sem crédito visível no card.
"""
import sys

import fitz


def recortar(pdf, pagina, caixa, saida, dpi=200, limpo=False):
    """limpo=True: só a imagem de fundo da página (ilustração sem linhas-guia e rótulos vetoriais), na resolução nativa."""
    d = fitz.open(pdf)
    page = d[int(pagina)]
    if not limpo:
        pix = page.get_pixmap(dpi=dpi, clip=fitz.Rect(*caixa))
        pix.save(saida)
        return pix.width, pix.height
    info = max(page.get_image_info(xrefs=True), key=lambda i: fitz.Rect(i["bbox"]).width * fitz.Rect(i["bbox"]).height)
    bb = fitz.Rect(info["bbox"])
    tmp = fitz.open(); pg = tmp.new_page(width=page.rect.width, height=page.rect.height)
    pg.insert_image(bb, stream=d.extract_image(info["xref"])["image"])  # só a ilustração, sem vetores
    pix = pg.get_pixmap(dpi=dpi, clip=fitz.Rect(*caixa) & bb)
    pix.save(saida)
    return pix.width, pix.height


if __name__ == "__main__":
    a = sys.argv[1:]
    dpi = int(a[a.index("--dpi") + 1]) if "--dpi" in a else 200
    print(recortar(a[0], a[1], [float(v) for v in a[2].split(",")], a[3], dpi, "--limpo" in a))
