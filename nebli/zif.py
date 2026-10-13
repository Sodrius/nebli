"""Recorte de lâmina virtual Zoomify (.zif) do Histology Guide por HTTP Range.

Davi indicou o Histology Guide para imagens de histologia (MEMORY, F-20261003-CLAUDE-19). As lâminas são BigTIFF
com uma pirâmide de níveis em tiles JPEG; as anotações da página dão o centro (x, y) no nível máximo e o zoom
(`zZoomAndPanToView(x, y, z)`, z em % do tamanho total). Este módulo baixa só os tiles da região pedida.

    python3 -m nebli.zif <slide> <x> <y> <largura> <altura> <saida.png> [--escala 0.5]
        slide: nome (MH-118-small-intestine) ou URL .zif; x/y: centro em pixels do nível máximo;
        largura/altura: tamanho da região no nível máximo; --escala: fração da resolução máxima (escolhe o nível).
    python3 -m nebli.zif <slide> --anotacoes <url-da-pagina>   # lista as anotações da página do slideview
    python3 -m nebli.zif --buscar "serous demilune"             # índice do site: termo → lâmina, x, y, zoom

Guardar slide, região e escala no registro da corrida (imagens-vistas.json). Sem crédito visível no card.
"""
from __future__ import annotations

import re
import struct
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import fitz

BASE = "https://histologyguide.com/slides/"


def _get(url: str, start: int, length: int) -> bytes:
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{start + length - 1}",
                                               "User-Agent": "Mozilla/5.0"})
    for tentativa in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read()
        except OSError:
            if tentativa == 3:
                raise
            time.sleep(2 + 3 * tentativa)


class Zif:
    def __init__(self, slide: str):
        self.url = slide if slide.startswith("http") else BASE + slide.removesuffix(".zif") + ".zif"
        head = _get(self.url, 0, 16)
        assert head[:4] == b"II+\x00", "não é BigTIFF little-endian"
        off = struct.unpack("<Q", head[8:16])[0]
        self.levels = []
        while off:
            n = struct.unpack("<Q", _get(self.url, off, 8))[0]
            raw = _get(self.url, off + 8, n * 20 + 8)
            tags = {}
            for i in range(n):
                tag, typ, cnt = struct.unpack("<HHQ", raw[i * 20:i * 20 + 12])
                val = raw[i * 20 + 12:i * 20 + 20]
                tags[tag] = (typ, cnt, val)
            off = struct.unpack("<Q", raw[n * 20:n * 20 + 8])[0]
            self.levels.append(self._level(tags))
        self.levels.sort(key=lambda lv: -lv["w"])

    def _scalar(self, t):
        typ, cnt, val = t
        return struct.unpack("<H", val[:2])[0] if typ == 3 else struct.unpack("<I", val[:4])[0] \
            if typ == 4 else struct.unpack("<Q", val[:8])[0]

    def _array(self, t):
        typ, cnt, val = t
        size = {3: 2, 4: 4, 16: 8}[typ]
        fmt = {3: "H", 4: "I", 16: "Q"}[typ]
        if cnt * size <= 8:
            data = val[:cnt * size]
        else:
            data = _get(self.url, struct.unpack("<Q", val)[0], cnt * size)
        return list(struct.unpack(f"<{cnt}{fmt}", data))

    def _level(self, tags):
        return {"w": self._scalar(tags[256]), "h": self._scalar(tags[257]),
                "tw": self._scalar(tags[322]), "th": self._scalar(tags[323]),
                "offs": tags[324], "cnts": tags[325], "_arr": None}

    def crop(self, cx: float, cy: float, w: float, h: float, escala: float = 1.0) -> fitz.Pixmap:
        full = self.levels[0]
        # nível mais pequeno que ainda tem resolução >= escala pedida
        lv = min((lv for lv in self.levels if lv["w"] >= full["w"] * escala - 1), key=lambda lv: lv["w"])
        f = lv["w"] / full["w"]
        x0, y0 = max(0, (cx - w / 2) * f), max(0, (cy - h / 2) * f)
        x1, y1 = min(lv["w"], (cx + w / 2) * f), min(lv["h"], (cy + h / 2) * f)
        if lv["_arr"] is None:
            lv["_arr"] = (self._array(lv["offs"]), self._array(lv["cnts"]))
        offs, cnts = lv["_arr"]
        cols = -(-lv["w"] // lv["tw"])
        page_doc = fitz.open()
        page = page_doc.new_page(width=x1 - x0, height=y1 - y0)
        tiles = [(tx, ty) for ty in range(int(y0 // lv["th"]), int((y1 - 1) // lv["th"]) + 1)
                 for tx in range(int(x0 // lv["tw"]), int((x1 - 1) // lv["tw"]) + 1)]
        with ThreadPoolExecutor(8) as pool:
            datas = pool.map(lambda t: _get(self.url, offs[t[1] * cols + t[0]], cnts[t[1] * cols + t[0]]), tiles)
            for (tx, ty), data in zip(tiles, datas):
                rx, ry = tx * lv["tw"] - x0, ty * lv["th"] - y0
                page.insert_image(fitz.Rect(rx, ry, rx + lv["tw"], ry + lv["th"]), stream=data)
        return page.get_pixmap(matrix=fitz.Matrix(1, 1))


def anotacoes(page_url: str) -> list[tuple[str, int, int, float]]:
    html = urllib.request.urlopen(urllib.request.Request(page_url, headers={"User-Agent": "Mozilla/5.0"}),
                                  timeout=60).read().decode("utf-8", "replace")
    out = []
    for m in re.finditer(r"zZoomAndPanToView\((\d+),\s*(\d+),\s*([\d.]+)\)\">([^<]+)</button>\s*-?\s*([^<]*)", html):
        out.append((m.group(4).strip(), int(m.group(1)), int(m.group(2)), float(m.group(3)), m.group(5).strip()))
    return out


def buscar(termo: str) -> list[tuple[str, str, int, int, float, str]]:
    """Índice A–Z do Histology Guide: cada <h3> é um termo; os links logo abaixo trazem lâmina e posição."""
    letra = termo.strip()[0].upper()
    html = urllib.request.urlopen(urllib.request.Request(f"https://histologyguide.com/index/index-{letra}.html",
                                  headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace")
    out = []
    for bloco in re.split(r"<h3>", html)[1:]:
        nome = bloco.split("</h3>")[0].strip()
        if termo.lower() not in nome.lower():
            continue
        for m in re.finditer(r'href="/slideview/([^/]+)/[^"?]+\?x=(\d+)&(?:amp;)?y=(\d+)&(?:amp;)?z=([\d.]+)[^"]*"'
                             r'[^>]*><img[^>]*alt="([^"]*)"', bloco):
            out.append((nome, m.group(1), int(m.group(2)), int(m.group(3)), float(m.group(4)), m.group(5)))
    return out


def main(argv: list[str]) -> None:
    if argv and argv[0] == "--buscar":
        for r in buscar(" ".join(argv[1:])):
            print(r)
        return
    if "--anotacoes" in argv:
        z = Zif(argv[0])
        print("níveis:", [(lv["w"], lv["h"]) for lv in z.levels])
        for a in anotacoes(argv[argv.index("--anotacoes") + 1]):
            print(a)
        return
    escala = float(argv[argv.index("--escala") + 1]) if "--escala" in argv else 1.0
    slide, x, y, w, h, out = argv[:6]
    pix = Zif(slide).crop(float(x), float(y), float(w), float(h), escala)
    pix.save(out)
    print(out, pix.width, pix.height)


if __name__ == "__main__":
    main(sys.argv[1:])
