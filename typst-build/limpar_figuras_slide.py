#!/usr/bin/env python3
"""Renderiza os slides de uma aula já limpos para virarem figura.

Implementa `docs/canon/VISUAL-E-IO.md` §"Higiene do ativo": remove o retângulo de
placeholder do template, corta no conteúdo e registra a caixa de corte de cada
slide. A caixa é o que permite recalcular coordenadas de Image Occlusion medidas
sobre a página inteira — sem ela, máscara herdada de recorte anterior passa nos
gates e quebra no runtime (ERROS.md #58).

Uso:
  python3 typst-build/limpar_figuras_slide.py SLIDES.pdf <slug>
  python3 typst-build/limpar_figuras_slide.py SLIDES.pdf <slug> --dpi 200

Saída:
  figuras/<slug>/slide-NN.png
  figuras/<slug>/_crop-boxes.json   (x0, y0, x1, y1, W, H por slide)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import numpy as np
    import pypdfium2 as pdfium
    from PIL import Image
except ImportError as exc:  # pragma: no cover - dependência de ambiente
    sys.exit(f"x dependência ausente ({exc}). Rode: pip install pypdfium2 pillow numpy")

# Azul de accent padrão do PowerPoint e sua borda escura.
PLACEHOLDER_FILL = (68, 114, 196)
PLACEHOLDER_EDGE = (47, 82, 143)
INK_THRESHOLD = 720          # soma RGB abaixo disso conta como conteúdo
MARGIN = 18                  # respiro em pixels ao redor do conteúdo
EDGE_BLEED = 10              # engole a borda escura do placeholder


def _placeholder_mask(pixels: np.ndarray) -> np.ndarray:
    fill = np.abs(pixels - np.array(PLACEHOLDER_FILL)).sum(axis=2) < 90
    edge = np.abs(pixels - np.array(PLACEHOLDER_EDGE)).sum(axis=2) < 60
    return fill | edge


def _strip_placeholder(pixels: np.ndarray) -> bool:
    """Branqueia o retângulo sólido ancorado no canto superior esquerdo."""
    height, width, _ = pixels.shape
    mask = _placeholder_mask(pixels)
    if not mask[5, 5]:
        return False
    row, col = mask[5], mask[:, 5]
    run_w = int(np.argmin(row)) if not row.all() else width
    run_h = int(np.argmin(col)) if not col.all() else height
    if run_w <= width * 0.03 or run_h <= height * 0.03:
        return False
    if mask[:run_h, :run_w].mean() <= 0.90:
        return False
    pixels[: min(height, run_h + EDGE_BLEED), : min(width, run_w + EDGE_BLEED)] = 255
    return True


def limpar(pdf: Path, slug: str, figuras_root: Path, dpi: int) -> dict:
    out_dir = figuras_root / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(str(pdf))
    boxes: dict[str, dict] = {}
    stripped = 0

    for index in range(len(doc)):
        pixels = np.array(doc[index].render(scale=dpi / 72).to_pil().convert("RGB")).astype(int)
        height, width, _ = pixels.shape
        stripped += int(_strip_placeholder(pixels))

        ink = pixels.sum(axis=2) < INK_THRESHOLD
        rows, cols = np.where(ink)
        if len(rows) == 0:
            continue
        y0 = max(0, int(rows.min()) - MARGIN)
        y1 = min(height, int(rows.max()) + MARGIN + 1)
        x0 = max(0, int(cols.min()) - MARGIN)
        x1 = min(width, int(cols.max()) + MARGIN + 1)

        name = f"slide-{index + 1:02d}.png"
        Image.fromarray(pixels.astype("uint8")).crop((x0, y0, x1, y1)).save(out_dir / name)
        boxes[name] = {"x0": x0, "y0": y0, "x1": x1, "y1": y1, "W": width, "H": height}

    (out_dir / "_crop-boxes.json").write_text(
        json.dumps(boxes, indent=1) + "\n", encoding="utf-8")
    print(f"v {len(boxes)} slides em {out_dir} | placeholder removido em {stripped}")
    return boxes


def recortar_mascara(box: dict, mask: dict) -> dict:
    """Converte máscara normalizada da página inteira para a imagem recortada."""
    new_w, new_h = box["x1"] - box["x0"], box["y1"] - box["y0"]
    x = max(0.0, (mask["x"] * box["W"] - box["x0"]) / new_w)
    y = max(0.0, (mask["y"] * box["H"] - box["y0"]) / new_h)
    return {
        "x": round(x, 4),
        "y": round(y, 4),
        "w": round(min(mask["w"] * box["W"] / new_w, 1.0 - x), 4),
        "h": round(min(mask["h"] * box["H"] / new_h, 1.0 - y), 4),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("slug")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--figuras-root", type=Path, default=Path("figuras"))
    args = ap.parse_args()
    if not args.pdf.is_file():
        sys.exit(f"x PDF não encontrado: {args.pdf}")
    limpar(args.pdf, args.slug, args.figuras_root, args.dpi)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
