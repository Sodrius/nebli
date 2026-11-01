"""Banco de casos que deram certo (F-20261101-CLAUDE-01).

Davi: "deixa tudo isso como gate e com um agente para verificar tudo baseado em casos que deram certo".
Um caso deu certo quando Davi o aprovou de forma observável:
  - X (gostei) ativo no card;
  - elogio literal no comentário, sem crítica depois do elogio;
  - modelo citado no GUIA-2 (exemplares);
  - verde estudado: bandeira verde ("levar para a vida"), 4+ revisões, não suspenso, sem comentário, até 1 lapso.

    python3 -m nebli.casos            # regrava flashcards/projeto/CASOS-QUE-DERAM-CERTO.json lendo o Anki (só leitura)
"""
import html
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BANCO = RAIZ / "flashcards" / "projeto" / "CASOS-QUE-DERAM-CERTO.json"
COMENTARIOS = RAIZ / "flashcards" / "projeto" / "comentarios-cards.jsonl"
GUIA2 = RAIZ / "flashcards" / "projeto" / "GUIA-2-EXEMPLARES.md"

ELOGIO = re.compile(r"(?i)\bbom\b|ótim|otim|gostei|\btop\b|exemplar|melhorei|perfeit|realmente ensina|referência|bela imagem")
CRITICA = re.compile(r"(?i)ruim|estranh|zuad|faltou|falta|excesso|confus|errad|não ensina|nao ensina|melhorar|péssim|pessim|away|repet|poderia|deveria|tem que|\bmas\b|não ficou|nao ficou|não gostei|nao gostei|problem|cadê|cade |entrega|\?")
MAX_VERDES = 300


def _txt(h):
    h = re.sub(r"\{\{c\d+::((?:(?!\}\}).)*?)\}\}", lambda m: "[" + m.group(1).split("::")[0] + "]", h or "")
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def _ultima_fala(comentario):
    """Trecho de Davi depois do último marcador CORRIGIDO do executor."""
    partes = re.split(r"CORRIGIDO[^.]*\.", comentario or "")
    return _txt(partes[-1]) if partes else ""


def elogios():
    out = {}
    if not COMENTARIOS.exists():
        return out
    for linha in COMENTARIOS.read_text(encoding="utf-8").splitlines():
        try:
            x = json.loads(linha)
        except ValueError:
            continue
        fala = _ultima_fala(x.get("comentario"))
        if fala and ELOGIO.search(fala) and not CRITICA.search(fala):
            out[int(x["nid"])] = fala[:200]
    return out


def guia2():
    return {int(n) for n in re.findall(r"\b(1\d{12})\b", GUIA2.read_text(encoding="utf-8"))} if GUIA2.exists() else set()


def construir(A):
    from nebli import explicacoes
    fontes = {}
    try:
        cids = [int(e["card"]) for e in explicacoes.liked_cards(verbose=False)]
    except Exception:
        cids = []
    if cids:
        for c in A("cardsInfo", cards=cids):
            if c.get("note"):
                fontes.setdefault(c["note"], {})["X"] = "gostei (x)"
    for nid, fala in elogios().items():
        fontes.setdefault(nid, {})["elogio"] = fala
    for nid in guia2():
        fontes.setdefault(nid, {})["guia2"] = "modelo no GUIA-2"
    verdes = A("findCards", query='"deck:NEBLI*" flag:3 -is:suspended prop:reps>=4 prop:lapses<=1')
    info = []
    for i in range(0, len(verdes), 2000):
        info += A("cardsInfo", cards=verdes[i:i + 2000])
    n_verde = 0
    for c in sorted(info, key=lambda c: -c["reps"]):
        if n_verde >= MAX_VERDES:
            break
        if c["note"] not in fontes:
            fontes[c["note"]] = {"verde": f"verde, {c['reps']} revisões, {c['lapses']} lapso(s), ativo"}
            n_verde += 1
    nids = sorted(fontes)
    notas = []
    for i in range(0, len(nids), 500):
        notas += A("notesInfo", notes=nids[i:i + 500])
    casos = []
    for n in notas:
        if not n:
            continue
        f = {k: v["value"] for k, v in n["fields"].items()}
        com = f.get("NEBLI_Comentario", "")
        if "verde" in fontes[n["noteId"]] and _txt(com):
            continue  # verde só conta sem nenhum comentário
        frente = f.get("Text") or f.get("Front") or ""
        tags = n["tags"]
        aula = next((t[7:] for t in tags if t.startswith("NEBLI::2026-")), "")
        if not aula or any("retirado" in t for t in tags):
            continue
        casos.append({
            "nid": n["noteId"],
            "por_que_deu_certo": fontes[n["noteId"]],
            "aula": aula,
            "uc": (aula.split("-")[1] if "-" in aula else ""),
            "origem": next((t.split("::")[-1] for t in tags if t.startswith("NEBLI::origem::")), "AnKing" if any("source::nid" in t for t in tags) else ""),
            "frente": _txt(frente)[:400],
            "verso": _txt(f.get("Extra") or f.get("Back Extra") or f.get("Back") or "")[:400],
            "tem_imagem": bool(re.search(r"<img", "".join(f.values()))),
            "organizador": "data-nebli-organizacao" in frente,
        })
    return casos


def carregar():
    return json.loads(BANCO.read_text(encoding="utf-8")) if BANCO.exists() else {"casos": []}


def main(argv=None):
    from nebli.decks import Anki
    casos = construir(Anki())
    BANCO.write_text(json.dumps({"gerado_por": "python3 -m nebli.casos", "casos": casos}, ensure_ascii=False, indent=1), encoding="utf-8")
    por = {}
    for c in casos:
        for k in c["por_que_deu_certo"]:
            por[k] = por.get(k, 0) + 1
    print(f"{len(casos)} casos que deram certo → {BANCO.relative_to(RAIZ)}; por fonte: {por}")


if __name__ == "__main__":
    sys.exit(main())
