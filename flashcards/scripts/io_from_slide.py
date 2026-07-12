#!/usr/bin/env python
"""
io_from_slide.py — gera caixas de image occlusion (campo I0 do note type
"IO-one by one (AnKing Step Deck / AnKingMed)") a partir de uma figura rotulada.

Fluxo: recorta a sub-figura da pagina de handout -> OCR (tesseract por+eng) ->
agrupa palavras por linha em rotulos -> caixas justas (uma linha por caixa,
assinatura AnKing) -> emite campo I0 + preview PNG p/ validacao visual.

NAO cria a nota sozinho: emite I0 + manifest + preview. A criacao da nota
(storeMediaFile + addNote) fica no io_apply.py, apos o card-mirror aprovar.

Uso:
  python io_from_slide.py <pagina.png> --crop x1,y1,x2,y2 --slug <slug> \
        --header "..." [--min-conf 45] [--pad 3] [--only "aorta,valva"]
"""
import argparse, json, os, re, sys
from PIL import Image, ImageDraw

TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = os.path.expanduser(r"~\tessdata")  # user-writable (por+eng+osd)

def load_tess():
    import pytesseract
    if os.path.exists(TESS):
        pytesseract.pytesseract.tesseract_cmd = TESS
    if os.path.isdir(TESSDATA):
        os.environ["TESSDATA_PREFIX"] = TESSDATA
    return pytesseract

# rotulos que nao interessam: datas, numeros de slide, urls, letras soltas
JUNK = re.compile(r"^(?:\d{1,3}|\d{2}/\d{2}/\d{2,4}|https?\S*|www\.\S*|[a-zA-Z])$")

def is_label(word):
    w = word.strip()
    if len(w) < 3:
        return False
    if JUNK.match(w):
        return False
    if not re.search(r"[A-Za-zÀ-ÿ]{3,}", w):
        return False
    return True

def ocr_labels(img, min_conf, only, upscale=3):
    pt = load_tess()
    work = img
    if upscale != 1:
        work = img.resize((img.width * upscale, img.height * upscale),
                          Image.LANCZOS)
    data = pt.image_to_data(work, lang="por+eng",
                            output_type=pt.Output.DICT)
    only_set = set(s.strip().lower() for s in only.split(",")) if only else None
    # 1) coleta palavras validas (box em px da imagem original)
    words = []
    n = len(data["text"])
    for i in range(n):
        txt = data["text"][i].strip()
        try:
            conf = float(data["conf"][i])
        except ValueError:
            conf = -1
        if conf < min_conf or not is_label(txt):
            continue
        if only_set and txt.lower() not in only_set:
            continue
        b = [data["left"][i] // upscale, data["top"][i] // upscale,
             data["width"][i] // upscale, data["height"][i] // upscale]
        words.append({"t": txt, "b": b})
    if not words:
        return []
    # 2) agrupa por PROXIMIDADE horizontal na mesma linha (gap grande = rotulos distintos)
    med_h = sorted(w["b"][3] for w in words)[len(words) // 2]
    words.sort(key=lambda w: (w["b"][1], w["b"][0]))
    segs = []
    for w in words:
        x, y, ww, hh = w["b"]
        placed = False
        for s in segs:
            sx, sy, sxe, sye = s["x"], s["y"], s["xe"], s["ye"]
            same_line = not (y > sye - med_h * 0.4 or y + hh < sy + med_h * 0.4)
            gap = x - sxe
            if same_line and -med_h * 0.6 <= gap <= med_h * 1.1:
                s["words"].append(w["t"]); s["x"] = min(sx, x)
                s["y"] = min(sy, y); s["xe"] = max(sxe, x + ww)
                s["ye"] = max(sye, y + hh); placed = True; break
        if not placed:
            segs.append({"words": [w["t"]], "x": x, "y": y,
                         "xe": x + ww, "ye": y + hh})
    # 3) funde segmentos empilhados verticalmente e alinhados em x (rotulo multi-linha)
    merged = True
    while merged:
        merged = False
        for a in segs:
            for b in segs:
                if a is b:
                    continue
                overlap_x = min(a["xe"], b["xe"]) - max(a["x"], b["x"])
                vgap = b["y"] - a["ye"]
                if overlap_x > 0.4 * min(a["xe"] - a["x"], b["xe"] - b["x"]) \
                        and 0 <= vgap <= med_h * 0.6:
                    a["words"] += b["words"]; a["x"] = min(a["x"], b["x"])
                    a["xe"] = max(a["xe"], b["xe"]); a["ye"] = b["ye"]
                    segs.remove(b); merged = True; break
            if merged:
                break
    labels = [{"text": " ".join(s["words"]),
               "box": [s["x"], s["y"], s["xe"] - s["x"], s["ye"] - s["y"]]}
              for s in segs]
    labels.sort(key=lambda L: (L["box"][1], L["box"][0]))
    return labels

def emit_i0(labels, pad):
    rects = []
    for L in labels:
        x, y, w, h = L["box"]
        x, y = max(0, x - pad), max(0, y - pad)
        w, h = w + 2 * pad, h + 2 * pad
        rects.append(f"[[rect0::{x},{y},{w},{h}]]")
    return "[#!occlusions " + "<br>".join(rects) + " #]<br>active"

def draw_preview(img, labels, pad, out):
    im = img.convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    for L in labels:
        x, y, w, h = L["box"]
        d.rectangle([x - pad, y - pad, x + w + pad, y + h + pad],
                    fill=(255, 90, 90, 110), outline=(200, 0, 0, 255), width=2)
    im.save(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--crop", help="x1,y1,x2,y2 na pagina original")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--header", default="")
    ap.add_argument("--min-conf", type=float, default=45)
    ap.add_argument("--pad", type=int, default=3)
    ap.add_argument("--only", default="")
    ap.add_argument("--upscale", type=int, default=3)
    ap.add_argument("--outdir", default="arquivos-trabalho/io")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    img = Image.open(args.image)
    if args.crop:
        x1, y1, x2, y2 = map(int, args.crop.split(","))
        img = img.crop((x1, y1, x2, y2))

    labels = ocr_labels(img, args.min_conf, args.only, args.upscale)
    i0 = emit_i0(labels, args.pad)
    base = os.path.join(args.outdir, args.slug)
    # nome de arquivo = hash de conteudo (assinatura AnKing; mata o tell nº1)
    import hashlib, io as _io
    buf = _io.BytesIO(); img.convert("RGB").save(buf, "PNG")
    md5 = hashlib.md5(buf.getvalue()).hexdigest()
    media_name = f"{md5}.png"                 # nome que vai para Image e Extra
    cropfile = os.path.join(args.outdir, media_name)
    preview = base + "-preview.png"
    img.save(cropfile)
    draw_preview(img, labels, args.pad, preview)

    manifest = {"slug": args.slug, "header": args.header,
                "image_size": img.size, "n_boxes": len(labels),
                "labels": labels, "I0": i0,
                "media_name": media_name,
                "image_field": f'<img src="{media_name}">',
                "crop_png": cropfile, "preview_png": preview}
    with open(base + "-manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    heights = [L["box"][3] for L in labels]
    print(f"labels detectados: {len(labels)}")
    for L in labels:
        print(f"  {L['box']}  {L['text']!r}")
    if heights:
        print(f"altura mediana caixa: {sorted(heights)[len(heights)//2]}px "
              f"(min {min(heights)}, max {max(heights)})")
    print(f"preview -> {preview}")
    print(f"manifest -> {base}-manifest.json")

if __name__ == "__main__":
    main()
