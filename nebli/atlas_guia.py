"""Ponto exato que um rótulo do atlas indica: fim da linha-guia vetorial que sai do rótulo (Netter e similares).

Evita estimar a posição da estrutura a olho (F-20261008-CLAUDE-04: "seta não aponta certo").

    python3 -m nebli.atlas_guia <pdf> <pagina0> "<texto do rótulo>"   → pontos (x, y) em coordenadas da página
"""
import sys

import fitz


def segmentos(page):
    return [(it[1], it[2]) for dr in page.get_drawings() for it in dr["items"] if it[0] == "l"]


def alvos(pdf, pagina, rotulo, tol=8):
    """Para cada linha-guia que começa no rótulo, segue os segmentos encadeados até a ponta livre."""
    d = fitz.open(pdf)
    page = d[int(pagina)]
    segs = segmentos(page)
    out = []
    for r in page.search_for(rotulo):
        caixa = fitz.Rect(r.x0 - tol, r.y0 - tol, r.x1 + tol, r.y1 + tol)
        for a, b in segs:
            if caixa.contains(a) and not caixa.contains(b):
                ini, fim = a, b
            elif caixa.contains(b) and not caixa.contains(a):
                ini, fim = b, a
            else:
                continue
            usados = {(round(a.x, 1), round(a.y, 1), round(b.x, 1), round(b.y, 1))}
            while True:  # segmento seguinte que continua do fim atual
                nxt = None
                for c, e in segs:
                    k = (round(c.x, 1), round(c.y, 1), round(e.x, 1), round(e.y, 1))
                    if k in usados:
                        continue
                    if abs(c - fim) < 0.8:
                        nxt = (k, e)
                    elif abs(e - fim) < 0.8:
                        nxt = (k, c)
                    if nxt:
                        break
                if not nxt:
                    break
                usados.add(nxt[0]); fim = nxt[1]
            out.append((rotulo, (round(ini.x, 1), round(ini.y, 1)), (round(fim.x, 1), round(fim.y, 1))))
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    for x in alvos(a[0], a[1], a[2]):
        print(x)
