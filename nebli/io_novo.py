"""Máscaras de oclusão para imagem limpa (sem rótulos): caixa de pergunta num canto livre + seta até a estrutura.

Para trocar a imagem ruim de um card de oclusão por uma prancha limpa (ex.: Netter sem linhas-guia) sem perder a nota.
A resposta fica em Remarks; o verso mostra a caixa vazia (A) e a seta continua apontando.

    python3 -m nebli.io_novo <imagem> <x,y estrutura> <caixa x,y,w,h> <prefixo-saida> [--recuo 10]
Saída: <prefixo>-Q.svg, -A.svg, -O.svg com o tamanho da imagem.
"""
import sys

import fitz

from nebli.io_seta import MARKER, com_seta


def gerar(imagem, alvo, caixa, prefixo, ident="io-novo"):
    pix = fitz.Pixmap(imagem)
    w, h = pix.width, pix.height
    x, y, bw, bh = caixa
    base = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">\n {MARKER}\n <g>\n  <title>Labels</title>\n </g>\n'
            f' <g>\n  <title>Masks</title>\n')
    q = base + (f'  <rect id="{ident}-t0" x="{x}" y="{y}" width="{bw}" height="{bh}" stroke="#2D2D2D" fill="#FF7E7E" class="qshape"/>\n'
                ' </g>\n</svg>')
    q = com_seta(q, alvo)
    a = q.replace('fill="#FF7E7E" class="qshape"', 'fill="none" stroke-dasharray="6 4" class="qshape"')
    o = base + f'  <rect id="{ident}-t0" x="{x}" y="{y}" width="{bw}" height="{bh}" stroke="#2D2D2D" fill="#FFEBA2"/>\n </g>\n</svg>'
    for suf, s in (("Q", q), ("A", a), ("O", o)):
        open(f"{prefixo}-{suf}.svg", "w", encoding="utf-8").write(s)
    return w, h


def gerar_amarela(imagem, alvo, ang, comp, prefixo, saida_img, largura_caixa=150, altura_caixa=40, ident="io-novo"):
    """F-20261008-CLAUDE-04: seta amarela desenhada na figura (estilo dos cards elogiados) e caixa de pergunta no
    início da seta, sem linha vermelha atravessando a imagem. `alvo` deve vir de fonte (nebli.atlas_guia)."""
    import math
    from nebli.seta import desenhar
    desenhar(imagem, saida_img, [(alvo[0], alvo[1], ang, comp)])
    pix = fitz.Pixmap(saida_img)
    a = math.radians(ang)
    tx, ty = alvo[0] + comp * math.cos(a), alvo[1] + comp * math.sin(a)
    cx, cy = tx + (largura_caixa / 2 + 4) * math.cos(a), ty + (altura_caixa / 2 + 4) * math.sin(a)
    x = min(max(cx - largura_caixa / 2, 2), pix.width - largura_caixa - 2)
    y = min(max(cy - altura_caixa / 2, 2), pix.height - altura_caixa - 2)
    w, h = pix.width, pix.height
    base = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">\n <g>\n  <title>Labels</title>\n </g>\n'
            f' <g>\n  <title>Masks</title>\n')
    rect = f'  <rect id="{ident}-t0" x="{x:.0f}" y="{y:.0f}" width="{largura_caixa}" height="{altura_caixa}" stroke="#2D2D2D"'
    q = base + rect + ' fill="#FF7E7E" class="qshape"/>\n </g>\n</svg>'
    an = base + rect + ' fill="none" stroke-dasharray="6 4" class="qshape"/>\n </g>\n</svg>'
    o = base + rect + ' fill="#FFEBA2"/>\n </g>\n</svg>'
    for suf, s in (("Q", q), ("A", an), ("O", o)):
        open(f"{prefixo}-{suf}.svg", "w", encoding="utf-8").write(s)
    return w, h


if __name__ == "__main__":
    a = sys.argv[1:]
    print(gerar(a[0], tuple(float(v) for v in a[1].split(",")), tuple(float(v) for v in a[2].split(",")), a[3]))
