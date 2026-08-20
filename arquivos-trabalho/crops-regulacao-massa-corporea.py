#!/usr/bin/env python3
"""
Regenera os recortes de figura usados na E1 de `regulacao-massa-corporea`.

Motivo: os slides do professor trazem a figura útil cercada de moldura
decorativa, painel de título e margem branca. O recorte foi decidido caso a
caso (regra de largura deliberada, CLAUDE.md § Figuras) e vive aqui para ser
reprodutível — os PNGs em si não são versionados (convenção do repo:
`figuras/<slug>/` guarda só o MAPA_CONTEUDO.txt no git).

Uso:
    python3 arquivos-trabalho/crops-regulacao-massa-corporea.py <slide.pdf>
"""
import sys, pathlib
import pymupdf
import numpy as np

SLUG = "regulacao-massa-corporea"
# recorte manual (fração da página): usado onde o auto-trim pegaria decoração
OVERRIDES = {
    4:  (0.27, 0.13, 0.70, 0.82),   # cascata hormonal: só o diagrama
    6:  (0.02, 0.13, 0.61, 0.86),   # estresse agudo x prolongado: sem painel roxo
    29: (0.00, 0.37, 1.00, 0.86),   # peptídeos GI: sem a barra preta do título
    32: (0.01, 0.12, 0.42, 0.88),   # arqueado: só o circuito (painel esquerdo)
    33: (0.34, 0.20, 1.00, 0.80),   # fluxogramas ↑/↓ massa gorda (sem repetir 32)
    34: (0.36, 0.33, 1.00, 0.86),   # MC4R / α-MSH / receptor de leptina
}
# demais: auto-trim de margem branca
AUTO = [7, 11, 15, 17, 18, 20, 24, 26, 27, 35, 38]


def main(pdf):
    doc = pymupdf.open(pdf)
    out = pathlib.Path("figuras") / SLUG
    out.mkdir(parents=True, exist_ok=True)
    for n in sorted(set(list(OVERRIDES) + AUTO)):
        pg = doc[n - 1]
        W, H = pg.rect.width, pg.rect.height
        if n in OVERRIDES:
            f = OVERRIDES[n]
            clip = pymupdf.Rect(f[0] * W, f[1] * H, f[2] * W, f[3] * H)
        else:
            pix = pg.get_pixmap(dpi=50)
            a = np.frombuffer(pix.samples, dtype=np.uint8)
            a = a.reshape(pix.height, pix.width, pix.n)[:, :, :3]
            ys, xs = np.where((a < 245).any(axis=2))
            if len(xs) == 0:
                continue
            m = 4
            clip = pymupdf.Rect(
                max(0, xs.min() - m) / pix.width * W,
                max(0, ys.min() - m) / pix.height * H,
                min(pix.width, xs.max() + m) / pix.width * W,
                min(pix.height, ys.max() + m) / pix.height * H,
            )
        pm = pg.get_pixmap(dpi=300, clip=clip)
        pm.save(str(out / f"slide-{n:02d}-crop.png"))
        print(f"slide-{n:02d}-crop.png  {pm.width}x{pm.height}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
