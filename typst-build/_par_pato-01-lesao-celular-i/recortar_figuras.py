#!/usr/bin/env python3
"""Recorta as figuras da E1 a partir dos slides embutidos no PDF da aula.

As imagens ficam fora do git (ver .gitignore), então este script é o registro
reproduzível de cada recorte: caixa usada, marca d'água removida e reamostragem.

Uso:
  python3 typst-build/extrair_imagens_pdf.py <pdf-da-aula> pato-01-lesao-celular-i
  python3 typst-build/_par_pato-01-lesao-celular-i/recortar_figuras.py

Os slides originais são 1280x720 com moldura institucional: cabeçalho verde no
topo, miniatura do professor à direita, e-mail no rodapé esquerdo e marca
d'água MEDICINA/USP no rodapé direito. Cada recorte isola o objeto visual e
apaga em branco só o que sobra da moldura, sem tocar em rótulo da figura.
"""
from pathlib import Path

from PIL import Image, ImageDraw

BASE = Path(__file__).resolve().parents[2] / "figuras" / "pato-01-lesao-celular-i"

# e-mail do rodapé: presente em todos os slides
RODAPE = (132, 594, 220, 614)

# nome -> (slide de origem, caixa de recorte, retângulos apagados em branco)
SPECS = {
    "slide-03-organograma":            ("img-p003-01.jpeg", (252, 178, 700, 570), []),
    "slide-11-curva-tempo":            ("img-p011-01.jpeg", (222, 175, 700, 575), []),
    "slide-13-ultraestrutura":         ("img-p013-01.jpeg", (608, 178, 838, 505), []),
    "slide-15-criterios":              ("img-p015-01.jpeg", (145, 172, 815, 570), []),
    "slide-17-histologia":             ("img-p017-01.jpeg", (120, 225, 835, 478), []),
    "slide-19-microscopia-eletronica": ("img-p019-01.jpeg", (228, 178, 740, 588), []),
    "slide-21-marcadores":             ("img-p021-01.jpeg", (240, 178, 700, 502), []),
    "slide-23-quatro-mecanismos":      ("img-p023-01.jpeg", (120, 218, 838, 440), []),
    # marca d'água encosta em "chromatin"; os dois retângulos preservam o rótulo
    "slide-25-cascata-isquemia":       ("img-p025-01.jpeg", (425, 172, 838, 604),
                                        [(700, 583, 850, 660), (745, 566, 850, 660)]),
    # miniaturas de navegação do slide aparecem à esquerda da mitocôndria
    "slide-27-radicais-livres":        ("img-p027-01.jpeg", (240, 168, 838, 400),
                                        [(122, 160, 358, 278), (122, 160, 345, 196)]),
    "slide-33-reperfusao":             ("img-p033-01.jpeg", (207, 272, 730, 588), []),
    "slide-35-mitocondria":            ("img-p035-01.jpeg", (470, 162, 838, 612),
                                        [(750, 588, 845, 650)]),
    "slide-37-calcio":                 ("img-p037-01.jpeg", (495, 158, 806, 608), []),
    "slide-39-venn-mecanismos":        ("img-p039-01.jpeg", (262, 174, 690, 600), []),
    "slide-43-chaperona":              ("img-p043-01.jpeg", (122, 258, 548, 482), []),
}


def main() -> None:
    for nome, (origem, caixa, apagados) in SPECS.items():
        imagem = Image.open(BASE / origem).convert("RGB")
        pincel = ImageDraw.Draw(imagem)
        pincel.rectangle(list(RODAPE), fill=(255, 255, 255))
        for retangulo in apagados:
            pincel.rectangle(list(retangulo), fill=(255, 255, 255))
        recorte = imagem.crop(caixa)
        recorte = recorte.resize((recorte.width * 2, recorte.height * 2), Image.LANCZOS)
        recorte.save(BASE / f"{nome}.png")
        print(f"{nome}.png {recorte.size}")


if __name__ == "__main__":
    main()
