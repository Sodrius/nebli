#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extrair_cards_anking.py -- despeja o TEXTO REAL dos cards do AnKing v12.

Irmao fino do buscar_tags_anking.py: aquele so CONTA cards por tag; este puxa
frente/verso legiveis de cada card que casa uma tag, pra permitir curadoria
CARD-A-CARD (Camada 2 do metodo -- ver flashcards/CURADORIA-ANKING.md).

Le o export (anking-v12-export.txt): col 1 = GUID, col 3 = deck, campos da nota
a partir da col 4, col 22 = tags. Filtra pelo prefixo #AK_Step{step}_v12 e por
uma OU mais tags/regex. Limpa HTML, entidades e cloze pra virar texto plano.

Uso:
    # uma tag (subarvore incluida por padrao):
    python flashcards/scripts/extrair_cards_anking.py \
        "SketchyAnatomy::02_Thorax::03_Vasculature"

    # varias tags, saida pra um pool de aula:
    python flashcards/scripts/extrair_cards_anking.py \
        "SketchyAnatomy::02_Thorax::02_Heart::02_Coronary_Circulation" \
        "FirstAid::07_Cardiovascular::02_Anatomy" \
        --slug anato-06-circulatorio-linfatico-II

    # regex livre sobre a tag, so imprime (sem gravar):
    python flashcards/scripts/extrair_cards_anking.py --regex "azygos|vena_cava" --print
"""
import csv, re, sys, os, json, html, argparse, datetime

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

EXPORT = os.path.join(os.path.dirname(__file__), "anking-v12-export.txt")
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
GUIDCOL, DECKCOL, TAGCOL = 0, 2, 21   # 0-indexed
CAMPO_INI = 3                          # campos da nota comecam na col 4
FRONT_COL = 3                          # 1o campo = conteudo principal (Text)
EXTRA_COLS = (4, 5, 6)                 # campos seguintes = Extra/complemento

_TAG_HTML = re.compile(r"<[^>]+>")
_CLOZE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.DOTALL)
_IMG = re.compile(r"<img[^>]*>", re.IGNORECASE)
_WS = re.compile(r"\s+")


def limpar(campo):
    """HTML -> texto plano legivel; cloze {{c1::x::hint}} -> [x]; <img> -> [img]."""
    if not campo:
        return ""
    txt = _IMG.sub(" [img] ", campo)
    txt = _CLOZE.sub(r"[\1]", txt)
    txt = txt.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    txt = _TAG_HTML.sub(" ", txt)
    txt = html.unescape(txt)
    txt = _WS.sub(" ", txt).strip()
    return txt


def _datarows(f):
    for line in f:
        if not line.startswith("#"):
            yield line


def extrair(matchers, step="1", path=EXPORT):
    """matchers: lista de regex compiladas aplicadas a CADA tag da nota.
    Retorna [{guid, deck, front, back, tags}], um por nota que casa."""
    pfx = f"#AK_Step{step}_v12"
    out = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.reader(_datarows(f), delimiter="\t", quotechar='"'):
            if len(row) <= TAGCOL:
                continue
            tags = [t for t in row[TAGCOL].split() if t.startswith(pfx)]
            if not tags:
                continue
            # a nota casa se ALGUMA tag Step1 casa ALGUM matcher
            casa = [t for t in tags if any(m.search(t) for m in matchers)]
            if not casa:
                continue
            raw0 = row[FRONT_COL] if len(row) > FRONT_COL else ""
            front = limpar(raw0)
            back_parts = [limpar(row[c]) for c in EXTRA_COLS if len(row) > c]
            back = " | ".join(p for p in back_parts if p)
            out.append({
                "guid": row[GUIDCOL],
                "deck": row[DECKCOL],
                "front": front,
                # campo 1 BRUTO (HTML+cloze) -- chave de casamento com a coleção,
                # ja que este AnkiConnect nao expoe guid no notesInfo
                "raw0": raw0,
                "back": back,
                "tags": casa,           # so as tags que casaram (as relevantes)
            })
    return out


def _matchers(tags, regex):
    ms = []
    for t in tags:
        # tag literal: casa a propria tag e a subarvore. Escapa metacaracteres.
        ms.append(re.compile(re.escape(t), re.IGNORECASE))
    if regex:
        ms.append(re.compile(regex, re.IGNORECASE))
    return ms


def main():
    ap = argparse.ArgumentParser(description="Despeja texto real dos cards AnKing por tag.")
    ap.add_argument("tags", nargs="*", help="tags/fragmentos de tag (subarvore incluida)")
    ap.add_argument("--regex", help="regex livre extra sobre a tag")
    ap.add_argument("--step", default="1")
    ap.add_argument("--slug", help="grava pool em arquivos-trabalho/anking-pool-<slug>.json")
    ap.add_argument("--print", dest="imprimir", action="store_true",
                    help="imprime os cards no terminal (default se sem --slug)")
    ap.add_argument("--max-print", type=int, default=40, help="teto de cards impressos")
    ap.add_argument("--forcar", action="store_true",
                    help="re-extrai mesmo se o pool do dia ja existe (default: usa cache)")
    args = ap.parse_args()

    if not args.tags and not args.regex:
        ap.error("informe ao menos uma tag posicional ou --regex")

    # cache: se o pool <slug> ja existe e foi gerado hoje, nao rele os 92 MB.
    if args.slug and not args.forcar:
        destino = os.path.join(RAIZ, "arquivos-trabalho", f"anking-pool-{args.slug}.json")
        if os.path.exists(destino):
            try:
                with open(destino, encoding="utf-8") as f:
                    antigo = json.load(f)
            except (ValueError, OSError):
                antigo = None
            if antigo and antigo.get("gerado_em") == datetime.date.today().isoformat():
                print(f"# cache: {os.path.relpath(destino, RAIZ)} ja e de hoje "
                      f"({antigo.get('n_cards','?')} cards). Use --forcar pra re-extrair.")
                return

    cards = extrair(_matchers(args.tags, args.regex), args.step)
    print(f"# {len(cards)} card(s) casam {args.tags or ''} {('/ '+args.regex) if args.regex else ''}".strip())

    if args.slug:
        os.makedirs(os.path.join(RAIZ, "arquivos-trabalho"), exist_ok=True)
        destino = os.path.join(RAIZ, "arquivos-trabalho", f"anking-pool-{args.slug}.json")
        payload = {
            "slug": args.slug,
            "gerado_em": datetime.date.today().isoformat(),
            "tags_consulta": args.tags,
            "regex": args.regex,
            "n_cards": len(cards),
            "cards": cards,
        }
        with open(destino, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"-> gravado {os.path.relpath(destino, RAIZ)}")

    if args.imprimir or not args.slug:
        for i, c in enumerate(cards[:args.max_print], 1):
            leaf = "::".join(c["tags"][0].split("::")[2:]) if c["tags"] else "?"
            print(f"\n[{i}] {leaf}")
            print(f"    F: {c['front'][:220]}")
            if c["back"]:
                print(f"    V: {c['back'][:180]}")
        if len(cards) > args.max_print:
            print(f"\n... (+{len(cards) - args.max_print} cards; use --slug pra gravar tudo)")


if __name__ == "__main__":
    main()
