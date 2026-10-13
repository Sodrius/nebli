"""Imagem no verso dos cards de estrutura (F-20261003-CLAUDE-15): "os de imagem, preferência para livros/anking, slide não".

As figuras vêm de notas do acervo: o deck Histology traz as figuras do Junqueira/Mescher no Extra; o AnKing traz figuras
de atlas e livros. No spec da aula:

    from nebli.ilustrar import ilustrar
    from imagens import IMAGENS          # arquivo da corrida: {chave: nid ou [nids]} de onde vêm as figuras
    CARDS = ilustrar(CARDS, IMAGENS)

Cada card recebe `extra_add` com as figuras (o build da corrida acrescenta ao Extra, sem apagar o Extra da fonte).
Nada aqui escolhe a figura sozinho: o mapa é decidido olhando a figura, e a revisão final card a card confere.
"""
from __future__ import annotations

import re

IMG = re.compile(r"<img[^>]+>", re.I)
SRC = re.compile(r'src="([^"]+)"', re.I)
_cache = {}


def _anki():
    from nebli.decks import Anki
    if "A" not in _cache:
        _cache["A"] = Anki()
    return _cache["A"]


def imgs(nid, fields=("Extra", "Text", "Image", "Illustration", "Lecture Notes", "Sketchy", "Pixorize", "Additional Resources")):
    """Tags <img> da nota, na ordem dos campos, sem repetir arquivo; só figuras (sem ícones de vídeo)."""
    key = ("imgs", nid)
    if key not in _cache:
        n = _anki()("notesInfo", notes=[int(nid)])[0]
        seen, out = set(), []
        for f in fields:
            for tag in IMG.findall(n["fields"].get(f, {}).get("value", "") if n.get("fields") else ""):
                m = SRC.search(tag)
                if m and m.group(1) not in seen and not re.search(r"\.(svg|gif)$", m.group(1), re.I):
                    seen.add(m.group(1)); out.append(f'<img src="{m.group(1)}">')
            if out and f == "Extra":  # figuras do Extra bastam; os campos de vídeo só se o Extra não tiver
                break
        _cache[key] = out
    return _cache[key]


SLIDE_TAG = re.compile(r'(<br>\s*)*<img[^>]+src="nebli-uc\d+-[a-z]+\d*-(s|p)\d+[^"]*"[^>]*>', re.I)


def pick(spec):
    """nid -> primeira figura; "nid#i" -> figura i; lista -> várias."""
    out = []
    for item in (spec if isinstance(spec, list) else [spec]):
        if str(item).endswith((".png", ".jpg", ".webp")):  # figura de livro extraída para a corrida (MEDIA do spec)
            out.append(f'<img src="{item}">'); continue
        nid, _, idx = str(item).partition("#")
        figs = imgs(int(nid))
        if not figs:
            raise SystemExit(f"nota {nid} sem figura")
        out.append(figs[int(idx or 0)])
    return out


def ilustrar(cards, mapa, sem=None):
    """sem: {chave: motivo} para card de estrutura que fica sem figura (ex.: dado de pesquisa, número)."""
    sem = sem or {}
    out = []
    for c in cards:
        if c["key"] in sem:
            c = dict(c, sem_imagem=sem[c["key"]])
        src = mapa.get(c["key"])
        if src:
            c = dict(c)
            if src == "sem":
                raise SystemExit(f"{c['key']}: use SEM_IMAGEM para card sem figura")
            c["extra_add"] = "<br>".join(dict.fromkeys(pick(src)))
            c["imagem_de"] = src
            if c.get("extra"):  # figura do livro/AnKing substitui a do slide (F-15: "slide não")
                c["extra"] = SLIDE_TAG.sub("", c["extra"]).strip()
        out.append(c)
    missing = (set(mapa) | set(sem)) - {c["key"] for c in cards}
    if missing:
        raise SystemExit(f"IMAGENS sem card no spec: {sorted(missing)}")
    return out


def anotar(cards, notas):
    """F-15 ("tá faltando comentário"): linha curta de explicação no verso, antes da figura. notas: {chave: texto}."""
    out = []
    for c in cards:
        t = notas.get(c["key"])
        if t:
            c = dict(c)
            if "extra" in c:
                c["extra"] = t + ("<br><br>" + c["extra"] if c["extra"] else "")
            else:
                c["extra_add"] = t + ("<br><br>" + c["extra_add"] if c.get("extra_add") else "")
            c["nota_verso"] = t
        out.append(c)
    missing = set(notas) - {c["key"] for c in cards}
    if missing:
        raise SystemExit(f"NOTAS sem card no spec: {sorted(missing)}")
    return out
