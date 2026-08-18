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

# Recortes por card do deck. Regra A12: a imagem do Extra tem de treinar o alvo
# daquele cloze, não o tema da aula. Por isso um mesmo slide vira vários
# recortes distintos, um por ramo do mecanismo — nunca a mesma figura colada em
# cards diferentes.
SPECS_CARD = {
    # slide 17, painéis A+B: normal contra tumefeito (alvo de c006, edema)
    "card-c006-edema":            ("img-p017-01.jpeg", (120, 225, 598, 478), []),
    # slide 17, painéis B+C: núcleo presente contra núcleo ausente (alvo de c004)
    "card-c004-nucleo":           ("img-p017-01.jpeg", (356, 225, 835, 478), []),
    # cascata do slide 25, topo: isquemia até a queda de ATP (alvo de c009)
    "card-c009-queda-atp":        ("img-p025-01.jpeg", (425, 172, 838, 400), []),
    # cascata, ramo da bomba de sódio até edema e blebs (alvo de c010)
    "card-c010-bomba-sodio":      ("img-p025-01.jpeg", (428, 398, 612, 604), []),
    # cascata, ramo da glicólise anaeróbica até a cromatina (alvo de c011)
    "card-c011-cromatina":        ("img-p025-01.jpeg", (545, 398, 782, 604),
                                   [(700, 583, 850, 660), (745, 566, 850, 660)]),
    # slide 35, saída esquerda: permeabilidade de transição até necrose (c018)
    "card-c018-necrose":          ("img-p035-01.jpeg", (478, 420, 690, 612), []),
    # slide 35, saída direita: citocromo c até apoptose (c019)
    "card-c019-apoptose":         ("img-p035-01.jpeg", (612, 388, 828, 600),
                                   [(750, 588, 845, 650)]),
    # slide 37, topo: origens do cálcio e subida do cálcio citosólico (c020)
    "card-c020-calcio-origens":   ("img-p037-01.jpeg", (495, 158, 806, 340), []),
    # slide 37, base: enzimas ativadas e o dano que produzem (c021)
    "card-c021-calcio-enzimas":   ("img-p037-01.jpeg", (495, 336, 806, 608), []),
    # slide 27, painel esquerdo: efeitos do radical livre sobre lipídio,
    # proteína e DNA (alvo de c015, peroxidação lipídica)
    "card-c015-alvos-ros":        ("img-p027-01.jpeg", (332, 438, 668, 600), []),
}
SPECS.update(SPECS_CARD)


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
        # O deck usa a versão JPEG: a fonte já é JPEG, então o PNG só inflaria o
        # manifesto, que vai embutido em base64 e é aberto no tablet. A E1
        # continua apontando para o PNG.
        recorte.save(BASE / f"{nome}.jpg", quality=85, optimize=True, progressive=True)
        print(f"{nome} {recorte.size}")


if __name__ == "__main__":
    main()
