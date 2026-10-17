"""Prova que os gates reprovam o caso ruim e nunca passam no vazio (MEMORY §15). Uso: python -m nebli.kenhub.teste_gates

Cada feedback de Davi (nebli/kenhub/feedbacks.json) precisa de: o gate existir no código e um caso ruim reprovado aqui.
"""
import json
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from nebli.kenhub import deck, modelo, render

RAIZ = Path(__file__).resolve().parents[2]


def _io(chave, nome, **meta):
    return {"chave": chave, "tipo": "netter", "modelo": modelo.NOME, "meta": {"seta": True, "guia": True, **meta},
            "campos": {"Nome PT": nome, "Nome EN": "Pons"}, "ocr_frente": []}


def main():
    falhas = []

    def espera(cond, msg):
        if not cond:
            falhas.append(msg)

    # registro: todo gate citado em feedbacks.json existe no código
    reg = json.loads((Path(__file__).parent / "feedbacks.json").read_text())
    for f in reg["feedbacks"]:
        for g in f["gates"]:
            espera(g["codigo"] in (RAIZ / g["arquivo"]).read_text(), f"{f['id']}: gate {g['codigo']!r} sumiu de {g['arquivo']}")
    cur = {"nome_igual_ok": []}
    # G8: nome com inglês ou com duas línguas reprova; nome em PT passa
    espera(any("G8" in p for p in deck.gates_pre([_io("a", "Pyramid of the medulla / Pirâmide do bulbo")], cur)), "G8 aceitou nome com duas línguas")
    espera(not any("G8" in p for p in deck.gates_pre([_io("b", "Pirâmide do bulbo")], cur)), "G8 reprovou nome correto")
    clz = {"chave": "c", "tipo": "acervo", "modelo": modelo.CLOZE, "campos": {"Text": "Qual estrutura? {{c1::Optic canal - Exit for CN II}}", "Imagens": "<img src=x>"}}
    espera(any("G8" in p for p in deck.gates_pre([clz], cur)), "G8 aceitou cloze longo em inglês")
    # G12: a frente que mostra o nome reprova
    e = _io("d", "Ponte")
    e["ocr_frente"] = ["Pons", "Medulla"]
    espera(any("G12" in p for p in deck.gates_pre([e], cur)), "G12 aceitou frente com a resposta")
    # G13: ponta da seta no fundo branco reprova
    espera(any("G13" in p for p in deck.gates_pre([_io("e", "Ponte", ponta_fundo=1.0)], cur)), "G13 aceitou seta no branco")
    with tempfile.TemporaryDirectory() as d:
        im = Image.new("RGB", (100, 100), "white")
        ImageDraw.Draw(im).rectangle((40, 40, 60, 60), fill=(150, 100, 80))
        im.save(Path(d) / "x.png")
        espera(deck._ponta_no_fundo(str(Path(d) / "x.png"), (50, 50)) < 0.1, "G13 errou a medida no tecido")
        espera(deck._ponta_no_fundo(str(Path(d) / "x.png"), (5, 5)) > 0.9, "G13 errou a medida no fundo")
        # G6: nunca passa no vazio
        f, _ = render.renderizar('"tag:NEBLI::nao-existe-xyz"', Path(d), [])
        espera(any("G6" in x for x in f), "G6 passou no vazio")
        f, _ = render.renderizar('"tag:NEBLI::nao-existe-xyz"', Path(d), [1, 2, 3])
        espera(any("G6" in x for x in f), "G6 passou com plano não vazio e nada renderizado")
    # F-05: Fonte preenchida reprova; máscara padrão AnKing é retângulo
    e = _io("f", "Ponte")
    e["campos"]["Fonte"] = "Kenhub"
    espera(any("G14" in p for p in deck.gates_pre([e], cur)), "G14 aceitou campo Fonte preenchido")
    from nebli.kenhub import mascara
    reg_ = np.zeros((50, 50), bool)
    reg_[10:20, 10:15] = True
    reg_[11, 30:40] = True
    m_, cx_ = mascara.retangulos(reg_, pad=1, area_min=5)
    espera(len(cx_) == 2 and m_[9:21, 9:16].all(), "máscara não virou retângulos do padrão AnKing")
    # entrada sem campos (tipo desconhecido) reprova
    espera(any("[montagem]" in p for p in deck.gates_pre([{"chave": "z", "tipo": "id"}], cur)), "entrada sem campos passou")
    # F-03: navegador do Kenhub invisível
    espera("headless=True" in (RAIZ / "nebli/kenhub/navegador.py").read_text(), "navegador do Kenhub voltou a abrir janela")
    if falhas:
        print("TESTE DOS GATES REPROVADO:", *falhas, sep="\n  ")
        raise SystemExit(1)
    print(f"teste dos gates ok: {len(reg['feedbacks'])} feedbacks com gate no código e caso ruim reprovado")


if __name__ == "__main__":
    main()
