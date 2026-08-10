#!/usr/bin/env python3
"""pdf_figura_io.py — recorta figuras de um PDF de slides e constrói Image
Occlusion a partir dos rótulos reais da figura.

Existe porque o gargalo manual do pipeline era desenhar caixas de IO à mão. Os
slides trazem os rótulos como texto vetorial; o PDF sabe a caixa exata de cada
linha. Este script lê essas caixas e as converte em máscaras que cobrem o
*rótulo-resposta*, nunca a estrutura anatômica (docs/canon/VISUAL-E-IO.md).

Três modos:

  dump   — lista as linhas de texto dentro de um recorte, com índice e bbox.
           É o passo de inspeção: o operador escolhe quais linhas viram máscara.
  crop   — grava o recorte como PNG (figura para E1 ou base do IO).
  build  — grava o recorte + campo I0 + previews de pergunta e de resposta.

Coordenadas de recorte são sempre em pontos de PDF (72 pt = 1 in), na origem
superior-esquerda da página, no formato x0,y0,x1,y1.

Exemplos:
  python pdf_figura_io.py dump  slides.pdf --page 22 --crop 90,150,700,500
  python pdf_figura_io.py crop  slides.pdf --page 22 --crop 90,150,700,500 \
      --dpi 200 --out figuras/aula/canal-anal.png
  python pdf_figura_io.py build slides.pdf --page 22 --crop 90,150,700,500 \
      --dpi 200 --out-dir arquivos-trabalho/aula/io/canal-anal \
      --label "Coluna anal:3,4,5" --label "Seio anal:9,10"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw

MASK_FILL = (92, 101, 112)
MASK_EDGE = (26, 32, 38)
REVEAL_EDGE = (14, 122, 92)


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", text).strip().casefold()


def parse_rect(raw: str) -> tuple[float, float, float, float]:
    parts = [float(v.strip()) for v in raw.split(",")]
    if len(parts) != 4:
        raise ValueError(f"recorte precisa de 4 números: {raw!r}")
    return tuple(parts)  # type: ignore[return-value]


def parse_label(raw: str) -> dict:
    """`Nome:3,4,5` -> {'text': 'Nome', 'lines': [3, 4, 5]}."""
    name, _, indexes = raw.rpartition(":")
    if not name:
        raise ValueError(f"rótulo precisa de 'Nome:indices': {raw!r}")
    return {"text": name.strip(), "lines": [int(v) for v in indexes.split(",") if v.strip()]}


def parse_pixel_label(raw: str) -> dict:
    """`Nome:x,y,w,h` para rótulos rasterizados dentro da própria figura.

    Slides de atlas trazem rótulos já impressos na imagem; eles não têm caixa de
    texto no PDF, mas continuam sendo rótulos-resposta e precisam ser cobertos —
    caso contrário o mesmo nome fica visível em outro ponto do mapa.
    """
    name, _, coords = raw.rpartition(":")
    if not name:
        raise ValueError(f"rótulo em pixels precisa de 'Nome:x,y,w,h': {raw!r}")
    box = [int(v.strip()) for v in coords.split(",")]
    if len(box) != 4:
        raise ValueError(f"rótulo em pixels precisa de 4 números: {raw!r}")
    return {"text": name.strip(), "source_lines": ["<rótulo rasterizado na figura>"], "box": box}


def page_lines(page: pymupdf.Page, crop: tuple[float, float, float, float]) -> list[dict]:
    """Linhas de texto inteiramente dentro do recorte, em pontos de PDF."""
    x0, y0, x1, y1 = crop
    found = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            text = "".join(span["text"] for span in line.get("spans", []))
            if not text.strip():
                continue
            bx0, by0, bx1, by1 = line["bbox"]
            if bx0 < x0 - 1 or by0 < y0 - 1 or bx1 > x1 + 1 or by1 > y1 + 1:
                continue
            found.append({"text": text.strip(), "bbox": [bx0, by0, bx1, by1]})
    found.sort(key=lambda item: (round(item["bbox"][1], 1), item["bbox"][0]))
    return found


def render_crop(page: pymupdf.Page, crop: tuple[float, float, float, float], dpi: int) -> Image.Image:
    pix = page.get_pixmap(dpi=dpi, clip=pymupdf.Rect(*crop))
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def to_pixels(bbox, crop, dpi, pad) -> list[int]:
    """bbox em pontos de PDF -> [x, y, w, h] em pixels do recorte."""
    scale = dpi / 72.0
    x = int(round((bbox[0] - crop[0]) * scale)) - pad
    y = int(round((bbox[1] - crop[1]) * scale)) - pad
    w = int(round((bbox[2] - bbox[0]) * scale)) + 2 * pad
    h = int(round((bbox[3] - bbox[1]) * scale)) + 2 * pad
    return [max(x, 0), max(y, 0), w, h]


def union(boxes: list[list[float]]) -> list[float]:
    return [
        min(b[0] for b in boxes),
        min(b[1] for b in boxes),
        max(b[2] for b in boxes),
        max(b[3] for b in boxes),
    ]


def occlusion_field(masks: list[dict]) -> str:
    """Campo I0 do note type 'IO-one by one (AnKing Step Deck / AnKingMed)'."""
    rects = [
        f"[[rect{index}::{mask['box'][0]},{mask['box'][1]},{mask['box'][2]},{mask['box'][3]}]]"
        for index, mask in enumerate(masks)
    ]
    return "[#!occlusions " + "<br>".join(rects) + " #]<br>active"


def draw_question(image: Image.Image, masks: list[dict], out: Path) -> None:
    canvas = image.copy()
    draw = ImageDraw.Draw(canvas)
    for mask in masks:
        x, y, w, h = mask["box"]
        draw.rectangle([x, y, x + w, y + h], fill=MASK_FILL, outline=MASK_EDGE, width=2)
    canvas.save(out)


def draw_answer(image: Image.Image, masks: list[dict], out: Path) -> None:
    canvas = image.copy()
    draw = ImageDraw.Draw(canvas)
    for mask in masks:
        x, y, w, h = mask["box"]
        draw.rectangle([x, y, x + w, y + h], outline=REVEAL_EDGE, width=2)
    canvas.save(out)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("dump", "crop", "build"))
    ap.add_argument("pdf")
    ap.add_argument("--page", type=int, required=True, help="1-indexado")
    ap.add_argument("--crop", required=True, help="x0,y0,x1,y1 em pontos de PDF")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--pad", type=int, default=3, help="folga da máscara, em pixels")
    ap.add_argument("--out", help="modo crop: PNG de saída")
    ap.add_argument("--out-dir", help="modo build: pasta de saída")
    ap.add_argument("--name", help="modo build: nome-base dos arquivos")
    ap.add_argument("--header", default="", help="modo build: campo Header do IO")
    ap.add_argument("--label", action="append", default=[], help="modo build: 'Nome:idx,idx'")
    ap.add_argument(
        "--blank",
        action="append",
        default=[],
        help="modo build: 'x,y,w,h' pintado de branco antes das máscaras "
        "(remove do recorte figura secundária ou rótulo que vazaria a resposta)",
    )
    ap.add_argument(
        "--pixel-label",
        action="append",
        default=[],
        help="modo build: 'Nome:x,y,w,h' para rótulo já rasterizado na figura",
    )
    args = ap.parse_args()

    doc = pymupdf.open(args.pdf)
    page = doc[args.page - 1]
    crop = parse_rect(args.crop)
    lines = page_lines(page, crop)

    if args.mode == "dump":
        print(f"# página {args.page} · recorte {crop} · {len(lines)} linhas")
        for index, line in enumerate(lines):
            bbox = [round(v, 1) for v in line["bbox"]]
            print(f"{index:3d}  {bbox}  {line['text']}")
        return 0

    image = render_crop(page, crop, args.dpi)

    if args.mode == "crop":
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        image.save(out)
        print(json.dumps({"out": str(out), "size": image.size, "sha256": sha256(out)}, ensure_ascii=False))
        return 0

    blanked = []
    if args.blank:
        painter = ImageDraw.Draw(image)
        for raw in args.blank:
            x, y, w, h = [int(v.strip()) for v in raw.split(",")]
            painter.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
            blanked.append([x, y, w, h])

    name = args.name or Path(args.out_dir).name
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    masks = []
    for raw in args.label:
        label = parse_label(raw)
        boxes = [lines[i]["bbox"] for i in label["lines"]]
        masks.append(
            {
                "text": label["text"],
                "source_lines": [lines[i]["text"] for i in label["lines"]],
                "box": to_pixels(union(boxes), crop, args.dpi, args.pad),
            }
        )
    for raw in args.pixel_label:
        masks.append(parse_pixel_label(raw))

    base = out_dir / f"{name}.png"
    image.save(base)
    question = out_dir / f"{name}-pergunta.png"
    answer = out_dir / f"{name}-resposta.png"
    draw_question(image, masks, question)
    draw_answer(image, masks, answer)

    manifest = {
        "name": name,
        "source_pdf": Path(args.pdf).name,
        "page": args.page,
        "crop_pt": list(crop),
        "dpi": args.dpi,
        "image": base.name,
        "image_sha256": sha256(base),
        "image_size": list(image.size),
        "header": args.header,
        "blanked_regions": blanked,
        "behavior": "hide_all_guess_all",
        "coherent_visual_map": True,
        "masks": masks,
        "mask_covers_answer_label": True,
        "previews": {"question": question.name, "answer": answer.name},
        "i0_field": occlusion_field(masks),
    }
    (out_dir / f"{name}.manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"name": name, "masks": len(masks), "size": image.size}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
