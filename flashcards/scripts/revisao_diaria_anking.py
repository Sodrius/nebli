#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""revisao_diaria_anking.py -- puxa os cards que o Davi ERROU hoje (monitor).

Fundacao do ciclo de monitoria: consulta o AnkiConnect pelos cards reprovados
hoje (ease=1 / "Again") dentro dos blocos curados NEBLI::, extrai frente/verso
legiveis e devolve um JSON. A sessao NEBLI le esse JSON e redige a explicacao
de mecanismo de cada erro (voz de monitor) -- que pode virar email diario.

Reprovado hoje no Anki = query "rated:1:1" (revisado hoje, nota 1 = Again).
Restringe a "tag:NEBLI::*" para so olhar o que faz parte da curadoria NEBLI.

Uso:
    python flashcards/scripts/revisao_diaria_anking.py                # hoje, todos NEBLI::
    python flashcards/scripts/revisao_diaria_anking.py --slug anato-06-circulatorio-linfatico-II
    python flashcards/scripts/revisao_diaria_anking.py --dias 1 --json errei-hoje.json
"""
import json, sys, os, argparse, datetime, html, re, urllib.request, urllib.error

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKICONNECT = "http://localhost:8765"
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

_TAG_HTML = re.compile(r"<[^>]+>")
_CLOZE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.DOTALL)
_IMG = re.compile(r"<img[^>]*>", re.IGNORECASE)
_WS = re.compile(r"\s+")


def limpar(campo):
    if not campo:
        return ""
    txt = _IMG.sub(" [img] ", campo)
    txt = _CLOZE.sub(r"[\1]", txt)
    txt = txt.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    txt = _TAG_HTML.sub(" ", txt)
    return _WS.sub(" ", html.unescape(txt)).strip()


def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def _anki_vivo():
    try:
        _invoke("version")
        return True
    except (urllib.error.URLError, OSError, RuntimeError):
        return False


def errei(dias=1, slug=None):
    escopo = f"tag:NEBLI::{slug}" if slug else "tag:NEBLI::*"
    query = f'({escopo}) rated:{dias}:1'   # nota 1 = Again = errei
    card_ids = _invoke("findCards", query=query)
    if not card_ids:
        return []
    info = _invoke("cardsInfo", cards=card_ids)
    out = []
    for c in info:
        campos = c.get("fields", {})
        # 1o campo = frente; procura um "Extra"/"Back" pro verso
        nomes = list(campos.keys())
        front = limpar(campos.get(nomes[0], {}).get("value", "")) if nomes else ""
        back = ""
        for chave in ("Extra", "Back", "Answer", "Text"):
            if chave in campos and chave != (nomes[0] if nomes else None):
                back = limpar(campos[chave]["value"])
                if back:
                    break
        tags = [t for t in c.get("tags", []) if t.startswith("NEBLI::")]
        out.append({
            "cardId": c.get("cardId"),
            "front": front,
            "back": back,
            "nebli_tags": tags,
            "lapses": c.get("lapses"),
        })
    return out


def main():
    ap = argparse.ArgumentParser(description="Puxa cards errados hoje nos blocos NEBLI:: (monitor).")
    ap.add_argument("--slug", help="restringe a uma aula (tag NEBLI::<slug>)")
    ap.add_argument("--dias", type=int, default=1, help="janela em dias (1 = hoje)")
    ap.add_argument("--json", help="grava o resultado neste arquivo (default: arquivos-trabalho/errei-<data>.json)")
    args = ap.parse_args()

    if not _anki_vivo():
        print("AnkiConnect fora do ar. Abra o Anki com o add-on 2055492159 para o monitor rodar.")
        sys.exit(3)

    erros = errei(args.dias, args.slug)
    print(f"# {len(erros)} card(s) errado(s) na janela de {args.dias} dia(s)"
          + (f" em NEBLI::{args.slug}" if args.slug else " em NEBLI::*"))

    destino = args.json or os.path.join(
        RAIZ, "arquivos-trabalho", f"errei-{datetime.date.today().isoformat()}.json")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        json.dump({"gerado_em": datetime.datetime.now().isoformat(timespec="minutes"),
                   "dias": args.dias, "slug": args.slug, "n": len(erros), "cards": erros},
                  f, ensure_ascii=False, indent=2)
    print(f"-> {os.path.relpath(destino, RAIZ)}")
    for i, c in enumerate(erros[:15], 1):
        print(f"\n[{i}] (lapses={c['lapses']}) {c['front'][:160]}")
        if c["back"]:
            print(f"    V: {c['back'][:140]}")


if __name__ == "__main__":
    main()
