"""Gera EXEMPLARES-CARDS.md e ANTI-EXEMPLARES-CARDS.md só a partir das marcas de Davi (F-20261022-CLAUDE-05).

    python3 -m nebli.exemplares            # regrava os dois arquivos

Davi (22/10): “os cards que dei gostei sempre devem entrar para os exemplares (quando tivermos mts exemplares vamos estudar o que
deu certo neles) os que não gostei (deixo um comentário ruim) vira anti-exemplar / precisamos limpar o que desses documentos for fora
disso”. Exemplar = card com X/gostei ativo (tab-log do add-on), com o texto vivo. Anti-exemplar = nota com comentário de Davi que não é
elogio, com o texto do card como estava quando ele comentou (primeiro registro em comentarios-cards.jsonl) e o comentário literal.
Nada é escrito à mão nesses arquivos: eles são regenerados por este comando.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from nebli.decks import Anki
from nebli.explicacoes import liked_cards

ROOT = Path(__file__).resolve().parents[1]
PROJ = ROOT / "flashcards" / "projeto"
LOG = PROJ / "comentarios-cards.jsonl"
# Comentário só de elogio não vira anti-exemplar (e não é exemplar sem o X).
ELOGIO = re.compile(r"^(gostei|bom card|imagem top|exemplo de bom card|isso é um bom card|esse deck é referência|card ficou muito bom)", re.I)
MARCA = re.compile(r"CORRIGIDO,?\s*[\d/ ,.]+\d{2}\.?", re.I)


def limpo(s):
    s = re.sub(r"<img[^>]*src=\"([^\"]+)\"[^>]*>", r"[IMG \1]", s or "")
    s = html.unescape(re.sub(r"<br\s*/?>", " / ", s))
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def comentario_limpo(c):
    return re.sub(r"\s+", " ", MARCA.sub(" ", c or "")).strip(" .")


def main():
    A = Anki()
    liked = liked_cards() or []
    cids = [int(e["card"]) for e in liked]
    info = {c["cardId"]: c for c in (A("cardsInfo", cards=cids) if cids else []) if c and "cardId" in c}
    nids = sorted({c["note"] for c in info.values()})
    notes = {n["noteId"]: n for n in (A("notesInfo", notes=nids) if nids else []) if n}
    L = ["# Exemplares de cards", "",
         "Gerado por `python3 -m nebli.exemplares` a partir dos cards que Davi marcou com **X/gostei** (F-20261022-CLAUDE-05). "
         "Só entram cards marcados; nada é escrito à mão aqui. Antes de escrever autoral, ler este arquivo e o ANTI-EXEMPLARES, "
         "achar os casos parecidos e ficar semelhante a estes.", ""]
    for e in sorted(liked, key=lambda x: x.get("em", "")):
        c = info.get(int(e["card"]))
        if not c:
            continue
        n = notes.get(c["note"], {})
        f = n.get("fields", {})
        frente = limpo((f.get("Text") or f.get("Front") or {}).get("value", "")) or limpo(c.get("question", ""))[:300]
        verso = limpo((f.get("Extra") or f.get("Back Extra") or f.get("Back") or {}).get("value", ""))
        aula = next((t.split("::")[1] for t in n.get("tags", []) if t.startswith("NEBLI::2026-")), c.get("deckName", "").split("::")[-1])
        L.append(f"- card {c['cardId']} / note {c['note']} ({aula}; {e.get('em', '')[:10]})")
        L.append(f"  - Frente: {frente[:500]}")
        if verso:
            L.append(f"  - Verso: {verso[:400]}")
    (PROJ / "EXEMPLARES-CARDS.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    primeiro, ultimo = {}, {}
    for l in LOG.read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        primeiro.setdefault(r["nid"], r)
        ultimo[r["nid"]] = r
    M = ["# Anti-exemplares de cards", "",
         "Gerado por `python3 -m nebli.exemplares` a partir dos comentários negativos de Davi (F-20261022-CLAUDE-05). Cada item traz "
         "o card como estava quando ele comentou e o comentário literal. Só entra card comentado; nada é escrito à mão aqui. "
         "A versão boa, quando houver, aparece nos EXEMPLARES só se Davi a marcar com X.", ""]
    n_anti = 0
    for nid, r in sorted(ultimo.items(), key=lambda kv: primeiro[kv[0]].get("visto_em", "")):
        com = comentario_limpo(r["comentario"])
        if not com or ELOGIO.match(com):
            continue
        card = limpo(primeiro[nid].get("card", ""))
        M.append(f"- note {nid} ({r.get('aula') or '?'}; {primeiro[nid].get('visto_em', '')[:10]})")
        if card:
            M.append(f"  - Card: {card[:400]}")
        M.append(f"  - Davi: “{com[:600]}”")
        n_anti += 1
    (PROJ / "ANTI-EXEMPLARES-CARDS.md").write_text("\n".join(M) + "\n", encoding="utf-8")
    print(f"{len(liked)} exemplares; {n_anti} anti-exemplares")


if __name__ == "__main__":
    main()
