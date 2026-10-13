"""Figura de livro só com a imagem (F-20261003-CLAUDE-19).

Davi, 03/10: "sinto que as imagens do livro não são boas [...] cortar aquele texto ao lado das imagens, deixando só a
imagem mesmo"; "qualidade da imagem importante e intencionalidade também". As figuras do deck Histology (Junqueira)
trazem uma faixa de título ("FIGURE 15-31 ...") e um bloco de legenda bege embaixo. Este módulo corta os dois e as
margens brancas, mantendo os rótulos que ficam dentro da figura.

    python3 -m nebli.img_figura <corrida>            # recorta as figuras do Histology usadas no plan.json e faz a folha
    python3 -m nebli.img_figura <corrida> --ver      # só refaz a folha de conferência (img/folha-recortes.png)

Saída: <corrida>/img/<nome>-fig.png, <corrida>/imagens-recortadas.json {original: recortada} e a folha para ver.
No spec da aula: `from nebli.img_figura import aplicar; CARDS = aplicar(CARDS, MEDIA, HERE)` troca o src nas frentes/
versos e põe a figura recortada em MEDIA. Cada figura ainda precisa ser vista e julgada em imagens-vistas.json.
"""
from __future__ import annotations

import base64
import json
import re
import subprocess
import sys
from pathlib import Path

import fitz

IMG = re.compile(r'<img[^>]+src="([^"]+)"', re.I)


def _png(data: bytes, name: str, tmp: Path) -> Path:
    src = tmp / name
    src.write_bytes(data)
    if name.lower().endswith(".png"):
        return src
    out = tmp / (Path(name).stem + ".png")
    subprocess.run(["sips", "-s", "format", "png", str(src), "--out", str(out)], capture_output=True, check=True)
    return out


def _beige(c):
    r, g, b = c
    return r >= 205 and 195 <= g <= 240 and 180 <= b <= 225 and r - b >= 14


def _olive(c):
    r, g, b = c
    return 80 <= r <= 170 and 80 <= g <= 170 and b <= 100 and abs(r - g) < 25 and r - b > 40


def _white(c):
    return min(c) >= 232


def caixa(path: Path):
    """Retângulo (x0, y0, x1, y1) em pixels com só a figura, ou None se não achar título/legenda."""
    px = fitz.Pixmap(str(path))
    if px.alpha:
        px = fitz.Pixmap(px, 0)
    if px.n < 3:
        px = fitz.Pixmap(fitz.csRGB, px)
    w, h, n, s = px.width, px.height, px.n, px.samples
    step = max(1, w // 200)

    def frac(y, test):
        xs = range(0, w, step)
        return sum(test(tuple(s[(y * w + x) * n:(y * w + x) * n + 3])) for x in xs) / len(xs)

    top = 0
    for y in range(min(h, 80)):  # faixa de título oliva no topo
        if frac(y, _olive) > 0.35:
            top = y + 1
    bottom, gap, start = h, 0, None
    for y in range(h - 1, int(h * 0.35), -1):  # legenda bege: bloco contínuo de linhas com fundo bege, de baixo para cima
        if frac(y, _beige) > 0.08:
            start, gap = y, 0
        else:
            gap += 1
            if gap > 4 and start is not None or gap > 30:
                break
    if start is not None and h - start >= 30:
        bottom = start
    if top:
        top += 2  # filete antialiasado sob a faixa de título

    def cfrac(x, test):
        ys = range(top, bottom, max(1, (bottom - top) // 200))
        return sum(test(tuple(s[(y * w + x) * n:(y * w + x) * n + 3])) for y in ys) / len(ys)

    right_cap, gap, start = w, 0, None
    for x in range(w - 1, int(w * 0.45), -1):  # legenda bege ao lado, à direita
        if cfrac(x, _beige) > 0.15:
            start, gap = x, 0
        else:
            gap += 1
            if gap > 4 and start is not None or gap > 30:
                break
    if start is not None and w - start >= 40:
        right_cap = start
    found = top > 0 or bottom < h or right_cap < w
    # margens brancas
    def uniform(colors):  # filete de moldura ou faixa de cor única também é borda, não figura
        q = [tuple(v // 24 for v in c) for c in colors]
        return max(q.count(c) for c in set(q)) / len(q) > 0.99

    def blank_row(y):
        cols = [tuple(s[(y * w + x) * n:(y * w + x) * n + 3]) for x in range(0, w, step)]
        return frac(y, _white) > 0.985 or uniform(cols)
    while top < bottom - 1 and blank_row(top):
        top += 1
    while bottom - 1 > top and blank_row(bottom - 1):
        bottom -= 1
    left, right = 0, right_cap
    def blank_col(x):
        ys = range(top, bottom, max(1, (bottom - top) // 200))
        cols = [tuple(s[(y * w + x) * n:(y * w + x) * n + 3]) for y in ys]
        return sum(_white(c) for c in cols) / len(cols) > 0.985 or uniform(cols)
    while left < right - 1 and blank_col(left):
        left += 1
    while right - 1 > left and blank_col(right - 1):
        right -= 1
    if not found or bottom - top < h * 0.3:
        return None
    return (left, top, right, bottom), (w, h)


def recortar(path: Path, out: Path):
    box = caixa(path)
    if not box:
        return None
    (x0, y0, x1, y1), (w, h) = box
    doc = fitz.open(str(path))
    page = doc[0]
    k = page.rect.width / w
    clip = fitz.Rect(x0 * k, y0 * k, x1 * k, y1 * k)
    page.get_pixmap(matrix=fitz.Matrix(1 / k, 1 / k), clip=clip).save(str(out))
    return {"original": [w, h], "caixa": [x0, y0, x1, y1]}


def aplicar(cards, media, run):
    """Troca, nos campos de texto das entradas do spec, cada figura original pela recortada."""
    path = Path(run) / "imagens-recortadas.json"
    if not path.exists():
        return cards
    mapa = json.loads(path.read_text())
    out = []
    for c in cards:
        c = dict(c)
        for k in ("text", "extra", "extra_add"):
            v = c.get(k)
            if isinstance(v, str):
                for orig, new in mapa.items():
                    if orig in v:
                        v = v.replace(f'src="{orig}"', f'src="{new}"')
                        media[new] = f"img/{new}"
                c[k] = v
        out.append(c)
    return out


def folha(run: Path, pares):
    doc = fitz.open()
    cols, cw, ch = 4, 420, 330
    for i in range(0, len(pares), cols * 2):
        page = doc.new_page(width=cols * cw, height=2 * ch)
        for j, (orig, new) in enumerate(pares[i:i + cols * 2]):
            r = fitz.Rect((j % cols) * cw + 6, (j // cols) * ch + 6, (j % cols + 1) * cw - 6, (j // cols + 1) * ch - 22)
            try:
                page.insert_image(r, filename=str(new))
            except Exception:
                pass
            page.insert_text((r.x0, r.y1 + 14), Path(orig).name[:40], fontsize=9)
    for k, page in enumerate(doc):
        page.get_pixmap(dpi=60).save(str(run / "img" / f"folha-recortes-{k + 1}.png"))
    return len(doc)


def main(argv=None):
    argv = argv or sys.argv[1:]
    run = Path(argv[0])
    from nebli.decks import Anki
    A = Anki()
    plan = json.loads((run / "plan.json").read_text())
    hx = set()
    for e in plan["entries"]:
        if e.get("origin") in ("AnKing",) or e.get("kind") == "slideio":
            continue  # AnKing traz figura própria, já vista na seleção; oclusão é o próprio slide
        for f in (e.get("fields") or {}).values():
            hx.update(m for m in IMG.findall(f or "") if m.lower().endswith(".webp") or m.startswith("nebli-"))
    (run / "img").mkdir(exist_ok=True)
    tmp = run / "img" / "_orig"
    tmp.mkdir(exist_ok=True)
    mapa_path = run / "imagens-recortadas.json"
    mapa = json.loads(mapa_path.read_text()) if mapa_path.exists() else {}
    pares, registro = [], {}
    for name in sorted(hx):
        local = None
        for d in (run, run.parent / "livros" / "robbins-figs", run.parent / "livros" / "moore-figs"):
            if (d / name).exists() or list(d.glob(f"**/{name}")):
                local = (d / name) if (d / name).exists() else list(d.glob(f"**/{name}"))[0]
                break
        data = local.read_bytes() if local else base64.b64decode(A("retrieveMediaFile", filename=name) or "")
        if not data:
            continue
        src = _png(data, name, tmp)
        new = Path(name).stem.replace("-fig", "") + "-fig.png"
        info = None if "--ver" in argv else recortar(src, run / "img" / new)
        if info or (run / "img" / new).exists():
            mapa[name] = new
            pares.append((src, run / "img" / new))
            registro[name] = info or "já recortada"
        else:
            registro[name] = "sem faixa/legenda: usar como está ou trocar"
            pares.append((src, src))
    mapa_path.write_text(json.dumps(mapa, ensure_ascii=False, indent=1))
    n = folha(run, pares)
    print(json.dumps(registro, ensure_ascii=False, indent=1))
    print(f"{len(mapa)} figuras recortadas; folhas: img/folha-recortes-1..{n}.png (ver todas antes de aplicar)")


if __name__ == "__main__":
    main()
