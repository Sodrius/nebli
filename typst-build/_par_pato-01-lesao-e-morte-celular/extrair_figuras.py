#!/usr/bin/env python3
"""Reconstrói as 23 figuras da E1 de lesão e morte celular a partir da apresentação da aula.

As figuras vivem em `figuras/pato-01-lesao-e-morte-celular/` e não são versionadas
(ver `.gitignore`). Este script é o registro reproduzível do recorte: para cada
figura guarda a página de origem, a caixa de recorte em fração da página, os
retângulos de higiene (faixa-título, e-mail do rodapé, crédito e logotipo
institucional) e a resolução de saída.

Uso:
    python3 extrair_figuras.py CAMINHO_DA_APRESENTACAO.pdf [--out DIR]

Depende de pymupdf.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pymupdf

LARGURA, ALTURA = 720.0, 540.0          # slide 10 x 7,5 polegadas
FAIXA_TITULO = (0.0, 0.0, 1.0, 0.135)   # barra verde do template, em todas as páginas

# (página, nome, extensão, recorte, retângulos de higiene, dpi, qualidade jpeg)
FIGURAS = [
    (2, "slide-02-organograma-resposta-celular", "png",
     (0.190, 0.170, 0.775, 0.900), [FAIXA_TITULO, (0.0, 0.90, 1.0, 1.0)], 150, None),
    (6, "slide-06-curva-efeito-duracao", "jpg",
     (0.140, 0.140, 0.830, 0.900), [FAIXA_TITULO], 150, 92),
    (9, "slide-09-tubulo-renal-microscopia-luz", "jpg",
     (0.000, 0.240, 1.000, 0.720), [FAIXA_TITULO], 150, 88),
    (10, "slide-10-tubulo-renal-microscopia-eletronica", "jpg",
     (0.140, 0.150, 0.870, 0.930), [FAIXA_TITULO], 150, 88),
    (11, "slide-11-marcadores-cardiacos", "png",
     (0.140, 0.150, 0.820, 0.780), [FAIXA_TITULO], 150, None),
    (12, "slide-12-panorama-mecanismos", "png",
     (0.000, 0.220, 1.000, 0.660), [FAIXA_TITULO], 150, None),
    (13, "slide-13-cascata-isquemia-atp", "png",
     (0.440, 0.130, 1.000, 0.950), [FAIXA_TITULO], 185, None),
    (14, "slide-14-geracao-radicais-livres", "jpg",
     (0.335, 0.142, 0.950, 0.600), [(0.0, 0.0, 1.0, 0.142), (0.333, 0.140, 0.393, 0.272)], 220, 92),
    (15, "slide-15-funcao-apos-reperfusao", "png",
     (0.120, 0.330, 0.870, 0.912), [FAIXA_TITULO, (0.930, 0.860, 1.0, 1.0)], 185, None),
    (16, "slide-16-mitocondria-necrose-apoptose", "jpg",
     (0.490, 0.110, 1.000, 0.9645), [FAIXA_TITULO, (0.900, 0.920, 1.0, 1.0)], 150, 92),
    (17, "slide-17-calcio-citosolico", "jpg",
     (0.500, 0.110, 1.000, 0.965), [FAIXA_TITULO, (0.955, 0.920, 1.0, 1.0), (0.0, 0.965, 1.0, 1.0)], 150, 92),
    (19, "slide-19-dano-de-membrana", "jpg",
     (0.390, 0.360, 1.000, 0.972), [FAIXA_TITULO, (0.880, 0.900, 1.0, 1.0), (0.0, 0.972, 1.0, 1.0)], 150, 92),
    (26, "slide-26-necrose-versus-apoptose", "jpg",
     (0.110, 0.140, 0.880, 0.910), [FAIXA_TITULO, (0.860, 0.880, 1.0, 1.0)], 195, 92),
    (27, "slide-27-picnose-cariorrexe", "jpg",
     (0.370, 0.580, 0.820, 1.000), [FAIXA_TITULO], 300, 88),
    (28, "slide-28-necrose-coagulativa", "jpg",
     (0.135, 0.540, 0.900, 1.000), [FAIXA_TITULO], 180, 88),
    (29, "slide-29-necrose-liquefativa", "jpg",
     (0.000, 0.360, 1.000, 1.000), [FAIXA_TITULO], 150, 88),
    (30, "slide-30-necrose-caseosa", "jpg",
     (0.140, 0.400, 0.820, 1.000), [FAIXA_TITULO], 150, 88),
    (33, "slide-33-necrose-gordurosa", "jpg",
     (0.120, 0.170, 0.870, 0.920), [FAIXA_TITULO], 150, 88),
    (34, "slide-34-necrose-fibrinoide", "jpg",
     (0.140, 0.350, 0.820, 0.950), [FAIXA_TITULO], 150, 88),
    (35, "slide-35-necrose-gangrenosa", "jpg",
     (0.300, 0.310, 0.670, 0.960), [FAIXA_TITULO], 300, 88),
    (38, "slide-38-vias-intrinseca-extrinseca", "jpg",
     (0.030, 0.130, 1.000, 0.900), [FAIXA_TITULO, (0.0, 0.900, 1.0, 1.0)], 200, 92),
    (41, "slide-41-corpos-apoptoticos", "jpg",
     (0.010, 0.150, 0.990, 0.890), [FAIXA_TITULO], 150, 88),
    (45, "slide-45-necroptose", "png",
     (0.300, 0.120, 0.660, 0.995), [FAIXA_TITULO, (0.800, 0.900, 1.0, 1.0)], 150, None),
]

# Restos de logotipo que sobrepõem conteúdo útil e por isso não podem ser apagados
# na página: são removidos em pixels, já no recorte. (nome, x_min, y_min)
LIMPEZA_EM_PIXELS = {
    "slide-13-cascata-isquemia-atp": [(782, 1055), (600, 1095)],
    "slide-38-vias-intrinseca-extrinseca": [(1780, 1105)],
}


def extrair(origem: Path, destino: Path) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    for pagina, nome, ext, (x0, y0, x1, y1), higiene, dpi, qualidade in FIGURAS:
        doc = pymupdf.open(origem)
        folha = doc[pagina - 1]
        for a, b, c, d in higiene:
            folha.draw_rect(
                pymupdf.Rect(a * LARGURA, b * ALTURA, c * LARGURA, d * ALTURA),
                color=None, fill=(1, 1, 1), overlay=True,
            )
        pix = folha.get_pixmap(
            dpi=dpi,
            clip=pymupdf.Rect(x0 * LARGURA, y0 * ALTURA, x1 * LARGURA, y1 * ALTURA),
        )
        for x_min, y_min in LIMPEZA_EM_PIXELS.get(nome, []):
            for y in range(y_min, pix.height):
                for x in range(x_min, pix.width):
                    pix.set_pixel(x, y, (255, 255, 255))
        saida = destino / f"{nome}.{ext}"
        if ext == "jpg":
            pix.save(saida, jpg_quality=qualidade)
        else:
            pix.save(saida)
        print(f"{saida.name}  {pix.width}x{pix.height}")
        doc.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apresentacao", type=Path,
                        help="PDF da apresentação da aula (47 páginas)")
    parser.add_argument("--out", type=Path,
                        default=Path(__file__).resolve().parents[2] / "figuras/pato-01-lesao-e-morte-celular")
    args = parser.parse_args()
    extrair(args.apresentacao, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
