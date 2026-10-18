"""Máscara de oclusão a partir da marcação verde do atlas Kenhub.

A figura do Kenhub já traz a estrutura-alvo pintada de verde; o card de oclusão esconde essa área (inclusive a cópia
dentro da lupa) e a resposta a revela. A máscara é um PNG embutido no SVG, exato ao pixel, no tamanho da imagem.
"""
import base64
import io

import numpy as np
from PIL import Image

COR_PERGUNTA = (255, 126, 126)   # mesmo vermelho das máscaras IO do NEBLI
COR_ORIGINAL = (255, 235, 162)
AREA_MINIMA = 12                 # px; descarta ruído de anti-aliasing fora da marcação


def verde(rgb: np.ndarray) -> np.ndarray:
    """Pixels do verde de marcação do Kenhub (≈ #3BB45A), incluindo o verde escuro das áreas sombreadas."""
    r, g, b = (rgb[..., i].astype(int) for i in range(3))
    return (g > 70) & (g - r > 22) & (g - b > 8)


def dilatar(m: np.ndarray, n: int) -> np.ndarray:
    out = m.copy()
    for _ in range(n):
        p = np.pad(out, 1)
        out = p[1:-1, 1:-1] | p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]
    return out


def regiao(imagem: str, margem: int = 3) -> np.ndarray:
    """Máscara booleana (altura × largura) da marcação verde, dilatada."""
    m = verde(np.asarray(Image.open(imagem).convert("RGB")))
    if m.sum() < AREA_MINIMA:
        raise ValueError(f"sem marcação verde em {imagem}")
    return dilatar(m, margem)


def _png(m: np.ndarray, cor, alpha=255) -> str:
    rgba = np.zeros((*m.shape, 4), np.uint8)
    rgba[m] = (*cor, alpha)
    buf = io.BytesIO()
    Image.fromarray(rgba).save(buf, "PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


def svgs(imagem: str, margem: int = 3) -> dict:
    """{'Q','A','O'} -> texto SVG. Q cobre a estrutura; A mostra só o contorno; O é o original."""
    m = regiao(imagem, margem)
    h, w = m.shape
    borda = m & ~_erodir(m, 3)

    def svg(b64):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}">'
                f'<image width="{w}" height="{h}" href="data:image/png;base64,{b64}" xlink:href="data:image/png;base64,{b64}"/></svg>')
    return {"Q": svg(_png(m, COR_PERGUNTA)), "A": svg(_png(borda, (45, 45, 45))), "O": svg(_png(m, COR_ORIGINAL))}


def _erodir(m: np.ndarray, n: int) -> np.ndarray:
    return ~dilatar(~m, n)


def conferir(imagem: str, destino: str, margem: int = 3) -> float:
    """Salva a figura com a máscara de pergunta por cima; devolve a fração de verde que sobrou (deve ser 0)."""
    im = Image.open(imagem).convert("RGB")
    m = regiao(imagem, margem)
    arr = np.asarray(im).copy()
    arr[m] = COR_PERGUNTA
    Image.fromarray(arr).save(destino, quality=88)
    return float(verde(arr).sum()) / max(1, int(verde(np.asarray(im)).sum()))


def png_pergunta(imagem: str, margem: int = 3) -> bytes:
    """PNG transparente com a estrutura-alvo coberta; sobrepõe a figura na frente do card (funciona em qualquer app do Anki)."""
    m = regiao(imagem, margem)
    rgba = np.zeros((*m.shape, 4), np.uint8)
    rgba[m] = (*COR_PERGUNTA, 255)
    buf = io.BytesIO()
    Image.fromarray(rgba).save(buf, "PNG", optimize=True)
    return buf.getvalue()


# ---------------------------------------------------------------------------------------------------------------
# Seta + IO (F-20261017-CLAUDE-04): a frente mostra a máscara com uma seta apontando para ela e um "?" na ponta; o verso
# mostra a mesma seta com o nome em português no lugar do "?" — a resposta aparece onde a pergunta estava.
from PIL import ImageDraw, ImageFont

COR_SETA = (255, 212, 0)        # amarelo vivo, contorno preto: aparece sobre tecido, osso, nervo e fundo branco
FONTE = "/System/Library/Fonts/Helvetica.ttc"
MARCA_KENHUB = (0.80, 0.86)      # canto inferior direito (fração de largura/altura) onde fica a marca do Kenhub


def _fonte(tam):
    try:
        return ImageFont.truetype(FONTE, tam, index=1)   # Helvetica Bold
    except OSError:
        return ImageFont.load_default()


def _quebrar(texto, fonte, largura_max, draw):
    linhas, atual = [], ""
    for p in texto.split():
        t = (atual + " " + p).strip()
        if draw.textlength(t, font=fonte) <= largura_max or not atual:
            atual = t
        else:
            linhas.append(atual)
            atual = p
    return linhas + [atual]


def _caixa_texto(texto, tam, largura_max):
    f = _fonte(tam)
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    linhas = _quebrar(texto, f, largura_max, d)
    alt = int(tam * 1.18)
    w = int(max(d.textlength(l, font=f) for l in linhas)) + 2 * 12
    h = alt * len(linhas) + 2 * 8
    return f, linhas, w, h, alt


def _componentes(m):
    """Componentes conexos (4-vizinhança) sem scipy; devolve lista de arrays (ys, xs), maior primeiro."""
    h, w = m.shape
    vis = np.zeros_like(m)
    comps = []
    ys, xs = np.nonzero(m)
    for y0, x0 in zip(ys, xs):
        if vis[y0, x0]:
            continue
        pilha = [(y0, x0)]
        vis[y0, x0] = True
        cy, cx = [], []
        while pilha:
            y, x = pilha.pop()
            cy.append(y); cx.append(x)
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and not vis[ny, nx]:
                    vis[ny, nx] = True
                    pilha.append((ny, nx))
        comps.append((np.array(cy), np.array(cx)))
    return sorted(comps, key=lambda c: -len(c[0]))


def planejar_seta(m, rotulo_wh, comprimento=(170, 220, 130, 270)):
    """Escolhe direção e comprimento da seta até a maior parte da máscara `m`, com a caixa do rótulo (w, h) na cauda,
    dentro da figura, sem cobrir a máscara nem a marca do Kenhub. Devolve (ponta, cauda, caixa) ou levanta ValueError."""
    h, w = m.shape
    ys, xs = _componentes(m)[0]
    cy, cx = ys.mean(), xs.mean()
    bw, bh = rotulo_wh
    melhor = None
    for comp in comprimento:
        for k in range(24):
            ang = 2 * np.pi * k / 24
            dx, dy = np.cos(ang), np.sin(ang)
            # ponta: último pixel da máscara saindo do centroide nessa direção (+3 px fora)
            t, ponta = 0, None
            while True:
                x, y = int(cx + dx * t), int(cy + dy * t)
                if not (0 <= x < w and 0 <= y < h):
                    break
                if m[y, x]:
                    ponta = (x + dx * 4, y + dy * 4)
                t += 1
            if ponta is None:
                continue
            cauda = (ponta[0] + dx * comp, ponta[1] + dy * comp)
            # caixa do rótulo encostada na cauda, do lado oposto à ponta
            bx = cauda[0] - bw / 2 + dx * bw / 2
            by = cauda[1] - bh / 2 + dy * bh / 2
            caixa = (int(bx), int(by), int(bx + bw), int(by + bh))
            if caixa[0] < 6 or caixa[1] < 6 or caixa[2] > w - 6 or caixa[3] > h - 6:
                continue
            mx0, my0 = int(MARCA_KENHUB[0] * w), int(MARCA_KENHUB[1] * h)
            if caixa[2] > mx0 and caixa[3] > my0:
                continue
            if m[caixa[1]:caixa[3], caixa[0]:caixa[2]].any():
                continue
            # a haste não pode atravessar a máscara (exceto na ponta)
            passos = np.linspace(0.15, 1.0, 40)
            if any(m[int(ponta[1] + dy * comp * s), int(ponta[0] + dx * comp * s)] for s in passos
                   if 0 <= int(ponta[1] + dy * comp * s) < h and 0 <= int(ponta[0] + dx * comp * s) < w):
                continue
            # preferir direções que deixam folga das bordas e da máscara; desempate: setas mais curtas
            folga = min(caixa[0], caixa[1], w - caixa[2], h - caixa[3])
            nota = folga
            if melhor is None or nota > melhor[0]:
                melhor = (nota, ponta, cauda, caixa)
        if melhor:
            break
    if not melhor:
        raise ValueError("não há lugar para a seta e o rótulo")
    return melhor[1], melhor[2], melhor[3]


def _desenhar_seta(d, ponta, cauda, larg=7, cabeca=26):
    px, py = ponta
    qx, qy = cauda
    ang = np.arctan2(py - qy, px - qx)
    base = (px - cabeca * np.cos(ang), py - cabeca * np.sin(ang))
    esq = (base[0] + cabeca * 0.55 * np.sin(ang), base[1] - cabeca * 0.55 * np.cos(ang))
    dir_ = (base[0] - cabeca * 0.55 * np.sin(ang), base[1] + cabeca * 0.55 * np.cos(ang))
    for cor, extra in (((0, 0, 0), 4), (COR_SETA, 0)):
        d.line([cauda, base], fill=cor, width=larg + extra)
        tri = [(px + extra * np.cos(ang) * 0.6, py + extra * np.sin(ang) * 0.6), esq, dir_]
        d.polygon(tri, fill=cor)


def _rotulo(d, caixa, linhas, fonte, alt, fundo, cor_txt):
    d.rounded_rectangle(caixa, radius=8, fill=fundo, outline=(0, 0, 0), width=3)
    y = caixa[1] + 8
    for l in linhas:
        lw = d.textlength(l, font=fonte)
        d.text(((caixa[0] + caixa[2]) / 2 - lw / 2, y), l, font=fonte, fill=cor_txt)
        y += alt


COR_SETA_ANKING = (229, 38, 30)   # vermelho de anotação (como as setas/linhas do AnKing e do AnatoKing), com halo branco
BORDA_MASCARA = (45, 45, 45)       # #2D2D2D, a borda das máscaras do Image Occlusion do AnKing


VISIVEL_MIN = 0.0035   # fração da figura: menor que isso o retângulo não se vê de relance


def retangulos(regiao, pad=5, area_min=AREA_MINIMA, grande=0.04):
    """Máscara no padrão AnKing: um retângulo (com folga) por parte da estrutura. Parte GRANDE (> `grande` da figura), cujo
    retângulo esconderia muito do que não é a estrutura, fica com a forma da própria estrutura (mesma cor e borda) — senão
    o lobo/cérebro vira um bloco que apaga o contexto. Devolve (máscara booleana, caixas retangulares, máscara das formas)."""
    h, w = regiao.shape
    caixas, formas = [], np.zeros_like(regiao)
    comps = [c for c in _componentes(regiao) if len(c[0]) >= area_min]
    if len(comps) > 4:
        # nervo/vaso cortado em muitos pedaços por estruturas por cima: 30 retângulos espalhados ficam toscos — pinta o
        # traçado da própria estrutura, engrossado para se ver (F-20261017-CLAUDE-05)
        for ys, xs in comps:
            formas[ys, xs] = True
        formas = dilatar(formas, 6)
        return formas.copy(), [], formas
    for ys, xs in comps:
        x0, y0, x1, y1 = max(0, xs.min() - pad), max(0, ys.min() - pad), min(w - 1, xs.max() + pad), min(h - 1, ys.max() + pad)
        area, caixa = len(ys), (x1 - x0 + 1) * (y1 - y0 + 1)
        # grande (lobo, cérebro) ou alongada/diagonal (giro): o retângulo apagaria o contexto → forma da própria estrutura.
        # Pequena ou linha fina (sulco, núcleo): retângulo, que se vê melhor.
        if area > grande * w * h or (caixa > 3 * area and area > 0.003 * w * h):
            formas[ys, xs] = True
        else:   # estrutura minúscula (ex.: o nervo C8): retângulo mínimo para se ver de relance (G17)
            lado = (VISIVEL_MIN * w * h) ** 0.5
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            larg, alt = max(x1 - x0 + 1, lado), max(y1 - y0 + 1, lado)
            x0, x1 = int(max(0, cx - larg / 2)), int(min(w - 1, cx + larg / 2))
            y0, y1 = int(max(0, cy - alt / 2)), int(min(h - 1, cy + alt / 2))
            caixas.append((x0, y0, x1, y1))
    m = formas.copy()
    for x0, y0, x1, y1 in caixas:
        m[y0:y1 + 1, x0:x1 + 1] = True
    return m, caixas, formas


def _seta_limpa(d, ponta, cauda, larg=8, cabeca=32):
    px, py = ponta
    qx, qy = cauda
    ang = np.arctan2(py - qy, px - qx)
    base = (px - cabeca * np.cos(ang), py - cabeca * np.sin(ang))
    esq = (base[0] + cabeca * 0.5 * np.sin(ang), base[1] - cabeca * 0.5 * np.cos(ang))
    dir_ = (base[0] - cabeca * 0.5 * np.sin(ang), base[1] + cabeca * 0.5 * np.cos(ang))
    for cor, extra in (((30, 30, 30), 8), ((255, 255, 255), 4), (COR_SETA_ANKING, 0)):   # contorno escuro + halo branco: aparece em músculo, osso e fundo
        d.line([cauda, base], fill=cor, width=larg + extra)
        d.polygon([(px + extra * np.cos(ang) * 0.7, py + extra * np.sin(ang) * 0.7), esq, dir_], fill=cor)


def overlays(tamanho, regiao_mascara, nome_pt, ponta=None, cauda=None, cobrir=True, seta=True, ancora=None):
    """Gera (frente, verso, meta) como PNGs RGBA do tamanho da figura — padrão AnKing (F-20261017-CLAUDE-05):
    frente = retângulo(s) vermelho(s) com borda cobrindo a estrutura + seta vermelha limpa até eles, SEM “?” e sem frase;
    verso = a mesma seta com o nome em português na ponta oposta (a estrutura volta a aparecer).
    `ancora` (x, y): sem seta própria (a figura já aponta, ex.: “ID” do AnKing) — o nome aparece ali no verso.
    Se `ponta`/`cauda` vierem (linha-guia do atlas), a seta segue a linha."""
    w, h = tamanho
    tam = max(20, int(w / 34))
    f, linhas, bw, bh, alt = _caixa_texto(nome_pt, tam, int(w * 0.36))
    regiao, caixas_m, formas = retangulos(regiao_mascara) if cobrir else (regiao_mascara, [], np.zeros_like(regiao_mascara))
    if ancora is not None:
        seta = False
        ponta = cauda = ancora
        bx = int(max(6, min(w - bw - 6, ancora[0] - bw / 2)))
        by = int(max(6, min(h - bh - 6, ancora[1] - bh / 2)))
        caixa = (bx, by, bx + bw, by + bh)
    elif ponta is None:
        ponta, cauda, caixa = planejar_seta(regiao, (bw, bh))
    else:
        dx, dy = cauda[0] - ponta[0], cauda[1] - ponta[1]
        n = max(1e-6, (dx * dx + dy * dy) ** 0.5)
        bx = cauda[0] - bw / 2 + dx / n * bw / 2
        by = cauda[1] - bh / 2 + dy / n * bh / 2
        caixa = (int(max(6, min(w - bw - 6, bx))), int(max(6, min(h - bh - 6, by))), 0, 0)
        caixa = (caixa[0], caixa[1], caixa[0] + bw, caixa[1] + bh)
    out = []
    for lado in ("frente", "verso"):
        im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        if lado == "frente" and cobrir:
            if formas.any():   # forma da estrutura grande, com borda #2D2D2D de 2 px como os retângulos
                arr = np.array(im)
                arr[formas] = (*COR_PERGUNTA, 255)
                arr[formas & ~_erodir(formas, 3)] = (*BORDA_MASCARA, 255)
                im = Image.fromarray(arr)
                d = ImageDraw.Draw(im)
            for x0, y0, x1, y1 in caixas_m:
                d.rectangle((x0, y0, x1, y1), fill=(*COR_PERGUNTA, 255), outline=BORDA_MASCARA, width=3)
        if seta:
            _seta_limpa(d, ponta, cauda)
        if lado == "verso":
            _rotulo(d, caixa, linhas, f, alt, (255, 255, 255), (0, 0, 0))
        buf = io.BytesIO()
        im.save(buf, "PNG", optimize=True)
        out.append(buf.getvalue())
    py, px = int(round(ponta[1])), int(round(ponta[0]))
    viz = regiao[max(0, py - 12):py + 13, max(0, px - 12):px + 13]
    meta = {"ponta": [round(float(ponta[0]), 1), round(float(ponta[1]), 1)], "cauda": [round(float(cauda[0]), 1), round(float(cauda[1]), 1)],
            "caixa": list(map(int, caixa)), "ponta_na_mascara": bool(viz.any()), "seta": seta, "estilo": "anking",
            "retangulos": len(caixas_m), "formas": int(formas.sum()), "area_mascara": int(regiao.sum()), "ancora": None if ancora is None else [round(float(ancora[0]), 1), round(float(ancora[1]), 1)]}
    return out[0], out[1], meta
