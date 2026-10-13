"""Seta de foco em máscara de oclusão: liga a caixa vermelha (qshape) à estrutura, quando o slide não tem linha-guia.

Davi (05–08/10): "faltou o cloze ter uma seta apontando para onde era pra ver"; "card não indica nada";
"seta para o local errado" (a seta antiga apontava para a própria caixa). A ponta fica na estrutura.

    python3 -m nebli.io_seta <mascara-Q.svg (na mídia)> <x,y da estrutura> <saida-Q-rN.svg>
"""
from __future__ import annotations

import math
import os
import re
import sys

MEDIA = os.path.expanduser("~/Library/Application Support/Anki2/User 1/collection.media")
MARKER = ('<defs><marker id="focus-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">'
          '<path d="M0,0 L0,6 L9,3 z" fill="#C62828"/></marker></defs>')


def com_seta(svg: str, alvo: tuple[float, float], recuo=10) -> str:
    r = re.search(r'<rect [^>]*x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*class="qshape"', svg)
    x, y, w, h = map(float, r.groups())
    tx, ty = alvo
    # sai da borda da caixa mais próxima do alvo
    sx = min(max(tx, x), x + w); sy = min(max(ty, y), y + h)
    if x < tx < x + w and y < ty < y + h:
        raise ValueError("alvo dentro da caixa")
    d = math.hypot(tx - sx, ty - sy)
    ex, ey = tx - (tx - sx) * recuo / d, ty - (ty - sy) * recuo / d
    line = (f'<line x1="{sx:.0f}" y1="{sy:.0f}" x2="{ex:.0f}" y2="{ey:.0f}" stroke="#C62828" stroke-width="6" '
            f'marker-end="url(#focus-arrow)"/>')
    svg = re.sub(r'<line [^>]*focus-arrow[^>]*/>', "", svg)
    if "focus-arrow" not in svg:
        svg = re.sub(r"(<svg[^>]*>)", r"\1\n " + MARKER, svg, count=1)
    return svg.replace("</g>\n</svg>", f" {line}\n </g>\n</svg>") if "</g>\n</svg>" in svg else svg.replace("</svg>", line + "</svg>")


def main(argv):
    src, alvo, out = argv[0], tuple(float(v) for v in argv[1].split(",")), argv[2]
    svg = open(os.path.join(MEDIA, src), encoding="utf-8").read()
    open(out, "w", encoding="utf-8").write(com_seta(svg, alvo))
    print(out)


if __name__ == "__main__":
    main(sys.argv[1:])
