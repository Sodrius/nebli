"""Recorte das notas longas do acervo Histology em cards curtos (F-20261003-CLAUDE-14).

Davi, 03/10: "cards enormes pra algumas coisas, péssimo. melhor recortar e fazer vários menores" e "esses cards do histology
vc pode cortar, porque são mt grandes... daí não tem repetição espaçada". A nota original (formato apostila, muitos clozes,
dicas "::s"/"::x") vira várias notas de uma frase, um fato e um cloze de palavra inteira, com o mesmo `src` (crédito ao
acervo) e o mesmo slide. O texto é o do Histology/Junqueira, só recortado; não conta como autoral.

No spec da aula:
    from nebli.hx_cortes import recortar
    from hx_cortes import CORTES          # arquivo da corrida: {chave_original: [(sufixo, texto, flags, alvo), ...]}
    CARDS = recortar(CARDS, CORTES)

`python3 -m nebli.hx_cortes <corrida>` troca as chaves antigas pelas novas em cobertura.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

MOTIVO = "Recorte de nota longa do Histology em card de uma frase (F-20261003-CLAUDE-14)."


def recortar(cards, cortes):
    out = []
    for c in cards:
        pieces = cortes.get(c["key"])
        if not pieces:
            out.append(c)
            continue
        for piece in pieces:
            suf, text, flags, alvo = piece[:4]
            fig = piece[4] if len(piece) > 4 else 0  # figura: índice no Extra da própria nota, ou "nid#i" de outra nota (F-15)
            d = {k: v for k, v in c.items() if k not in ("manter", "flags", "alvo", "key", "text", "motivo")}
            # Extra do Histology é um glossário longo: o verso fica só com as figuras do livro que ele traz (F-15), sem o texto
            from nebli.ilustrar import imgs, pick
            d.update(key=f"{c['key']}-{suf}", kind="text", origin="Histology", text=text, extra=(pick(fig)[0] if isinstance(fig, str) else (imgs(c["src"])[fig] if imgs(c["src"]) else "")), flags=dict(flags), alvo=alvo,
                     motivo=f"{c.get('motivo', '')} {MOTIVO}".strip(), recorte_de=c["key"])
            out.append(d)
    missing = set(cortes) - {c["key"] for c in cards}
    if missing:
        raise SystemExit(f"CORTES sem nota no spec: {sorted(missing)}")
    return out


def remap_cobertura(run):
    run = Path(run)
    sys.path.insert(0, str(run))
    from hx_cortes import CORTES  # noqa: E402
    new = {k: [f"{k}-{p[0]}" for p in v] for k, v in CORTES.items()}
    cov = json.loads((run / "cobertura.json").read_text())
    n = 0
    for it in cov["itens"]:
        cards = []
        for k in it.get("cards", []):
            if k in new:
                cards += new[k]; n += 1
            else:
                cards.append(k)
        it["cards"] = cards
    (run / "cobertura.json").write_text(json.dumps(cov, ensure_ascii=False, indent=1))
    print(f"cobertura: {n} referências trocadas")


if __name__ == "__main__":
    remap_cobertura(sys.argv[1])
