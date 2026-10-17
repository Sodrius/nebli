"""Figuras de outras fontes para o mesmo card de oclusão do Kenhub (seta + IO, nome em PT no lugar da pergunta).

- Netter (PDF com rótulos em texto): o rótulo em inglês é coberto; a seta segue a linha-guia vetorial até a estrutura
  (`nebli.atlas_guia`, ponto exato, sem estimar a olho).
- AnKing com “ID” na figura: a máscara cobre o “ID” (achado pelo reconhecimento de texto do macOS, local) e o nome em PT
  aparece no mesmo lugar (F-20261017-CLAUDE-04: “quero que o IO fique já onde está ID”).
"""
import io
import os

import fitz
import numpy as np
from PIL import Image

from nebli import atlas_guia

NETTER = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-dpbdes@gmail.com/Mon Drive/MEGA DRIVE/Medicina/Não compartilhar/"
                            "Menores/Bibliografia principal - medicina/Atlas of Human Anatomy by Frank H. Netter (z-lib.org).pdf")
LADO = 1000


def netter(pagina: int, rotulo: str, destino: str):
    """Recorta a região do rótulo + estrutura, salva em `destino` (JPEG) e devolve (região_do_rótulo, ponta, cauda)."""
    doc = fitz.open(NETTER)
    page = doc[pagina]
    caixas = page.search_for(rotulo)
    if not caixas:
        raise ValueError(f"Netter p.{pagina}: rótulo {rotulo!r} não encontrado")
    guias = [g for g in atlas_guia.alvos(NETTER, pagina, rotulo)]
    if not guias:
        raise ValueError(f"Netter p.{pagina}: rótulo {rotulo!r} sem linha-guia")
    _, ini, fim = max(guias, key=lambda g: (g[1][0] - g[2][0]) ** 2 + (g[1][1] - g[2][1]) ** 2)
    r = min(caixas, key=lambda c: (c.x0 - ini[0]) ** 2 + (c.y0 - ini[1]) ** 2)
    # o rótulo pode ter duas linhas (ex.: “Medullary / striae”): junta só as palavras da mesma coluna logo acima/abaixo
    altura = r.height
    for w in page.get_text("words"):
        wr = fitz.Rect(w[:4])
        mesma_coluna = wr.x0 < r.x1 + 2 and wr.x1 > r.x0 - 2
        vizinha = abs(wr.y0 - r.y0) <= 1.6 * altura or abs(wr.y1 - r.y1) <= 1.6 * altura
        if mesma_coluna and vizinha and abs(wr.x0 - r.x0) < 3 * altura:
            r = r | wr
    cx, cy = (r.x0 + fim[0]) / 2, (r.y0 + fim[1]) / 2
    # recorte de tamanho adequado (F-20261017-CLAUDE-05): rótulo + estrutura com folga, sem virar a prancha inteira
    lado = min(520.0, max(260.0, 2.6 * max(abs(r.x1 - fim[0]), abs(r.x0 - fim[0]), abs(r.y1 - fim[1]), abs(r.y0 - fim[1]))))
    clip = fitz.Rect(cx - lado / 2, cy - lado / 2, cx + lado / 2, cy + lado / 2) & page.rect
    zoom = LADO / max(clip.width, clip.height)
    for carimbo in ("mebooksfree", "z-lib", "www."):   # carimbo de site no rodapé do PDF (não é crédito do Netter)
        for cr in page.search_for(carimbo):
            page.add_redact_annot(cr + (-2, -2, 60, 2), fill=(1, 1, 1))
    page.apply_redactions(images=0, graphics=0)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    im.save(destino, quality=90)
    px = lambda x, y: ((x - clip.x0) * zoom, (y - clip.y0) * zoom)
    # O PDF é imagem digitalizada + camada de texto (OCR) que pode estar deslocada do desenho: a posição real do rótulo vem do
    # reconhecimento de texto na própria figura; o mesmo deslocamento vale para a linha-guia. Sem achar o rótulo, reprova.
    achados = _caixas_texto(destino, rotulo)
    if not achados:
        raise ValueError(f"Netter p.{pagina}: rótulo {rotulo!r} não foi lido na figura (camada de texto não confiável)")
    esperado = px((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)
    real = min(achados, key=lambda b: ((b[0] + b[2]) / 2 - esperado[0]) ** 2 + ((b[1] + b[3]) / 2 - esperado[1]) ** 2)
    dx, dy = (real[0] + real[2]) / 2 - esperado[0], (real[1] + real[3]) / 2 - esperado[1]
    m = np.zeros((im.height, im.width), bool)
    for b in achados:  # o rótulo apontado e qualquer outra ocorrência dele no recorte (senão a resposta vaza — gate G12)
        m[max(0, int(b[1]) - 4):int(b[3]) + 5, max(0, int(b[0]) - 4):int(b[2]) + 5] = True
    ponta, cauda = px(*fim), px(*ini)
    return m, (ponta[0] + dx, ponta[1] + dy), (cauda[0] + dx, cauda[1] + dy)


def _caixas_texto(imagem: str, rotulo: str):
    """Caixas (x0, y0, x1, y1) em pixels onde o reconhecimento de texto lê `rotulo` (ou a linha que o contém)."""
    from ocrmac import ocrmac
    w, h = Image.open(imagem).size
    alvo = rotulo.lower().split()
    out = []
    for txt, _, (bx, by, bw, bh) in ocrmac.OCR(imagem, recognition_level="accurate", language_preference=["en-US"]).recognize():
        t = txt.lower()
        if all(a in t for a in alvo):
            out.append((bx * w, (1 - by - bh) * h, (bx + bw) * w, (1 - by) * h))
    return out


def rotulo_id(imagem: str):
    """Caixa (x0, y0, x1, y1) em pixels do texto “ID” numa figura do AnKing, ou None."""
    from ocrmac import ocrmac
    w, h = Image.open(imagem).size
    melhor = None
    for nivel in ("fast", "accurate"):
        for txt, conf, (bx, by, bw, bh) in ocrmac.OCR(imagem, recognition_level=nivel, language_preference=["en-US"]).recognize():
            t = txt.strip().upper()
            if t == "ID" or t.startswith("ID ") or t.startswith("ID—") or t.startswith("ID -"):
                larg = bw if t == "ID" else bw * min(1.0, 2.4 / max(2, len(t)))
                caixa = (bx * w, (1 - by - bh) * h, (bx + larg) * w, (1 - by) * h)
                if melhor is None or t == "ID":
                    melhor = caixa
        if melhor:
            break
    return melhor


def textos(imagem) -> list:
    """Textos que o reconhecimento do macOS lê na figura (caminho ou PIL.Image) — para provar que a frente não entrega a resposta."""
    import tempfile
    from ocrmac import ocrmac
    if not isinstance(imagem, str):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as t:
            imagem.convert("RGB").save(t.name)
            imagem = t.name
    return [txt for txt, _, _ in ocrmac.OCR(imagem, recognition_level="accurate", language_preference=["en-US", "pt-BR"]).recognize()]
