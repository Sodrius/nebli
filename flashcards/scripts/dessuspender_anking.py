#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dessuspender_anking.py -- dessuspende cards do AnKing v12 por tag.

Duas formas, mesma chamada:
  * Se o AnkiConnect (add-on 2055492159) estiver de pe em http://localhost:8765,
    o script conta e DESSUSPENDE os cards das tags dadas, e reporta por tag.
  * Se nao estiver, cai no fallback: imprime, por tag, a busca pronta pro
    Browse do Anki + a instrucao manual (Ctrl+A, Ctrl+J).

Uma tag "casa" ela mesma E toda a subarvore dela (ex.: passar
"#B&B::16_Neuro" pega tudo abaixo de Neuro). Tags sem "#" inicial recebem
o prefixo "#AK_Step1_v12::" automaticamente.

Uso:
    # tags explicitas (curadas de onde-aprofundar.md ou buscar_tags_anking.py):
    python flashcards/scripts/dessuspender_anking.py \
        "#B&B::16_Neuro::01_Introduction_to_Neurology::01_Cells_of_the_Nervous_System"

    # de um arquivo, uma tag por linha (linhas com # no inicio da LINHA = comentario):
    python flashcards/scripts/dessuspender_anking.py --file tags.txt

    # so contar, sem mexer (recomendado antes de dessuspender de verdade):
    python flashcards/scripts/dessuspender_anking.py --dry-run "<tag>"
"""
import json, sys, argparse, urllib.request, urllib.error

ANKICONNECT = "http://localhost:8765"
PREFIXO = "#AK_Step1_v12"


def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=8) as resp:
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


def _normalizar(tag):
    tag = tag.strip().strip('"')
    if not tag:
        return None
    # tags de recurso ja comecam com # (ex.: #Bootcamp::...), mas o caminho
    # completo e #AK_Step1_v12::#Bootcamp::... -- prefixar se faltar a raiz
    if not tag.startswith(PREFIXO):
        tag = f"{PREFIXO}::{tag}"
    return tag


def _busca(tag):
    # a propria tag OU qualquer subtag dela
    return f'"tag:{tag}" OR "tag:{tag}::*"'


def _carregar_tags(args):
    tags = []
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            for linha in f:
                linha = linha.rstrip("\n")
                # comentario = # no comeco da LINHA (a tag tambem comeca com #,
                # entao distinguimos por espaco depois do # de comentario)
                if linha.strip().startswith("# "):
                    continue
                t = _normalizar(linha)
                if t:
                    tags.append(t)
    tags.extend(_normalizar(t) for t in args.tags if _normalizar(t))
    # dedup preservando ordem
    vistas, out = set(), []
    for t in tags:
        if t not in vistas:
            vistas.add(t)
            out.append(t)
    return out


def main():
    ap = argparse.ArgumentParser(description="Dessuspende cards do AnKing v12 por tag.")
    ap.add_argument("tags", nargs="*", help="tags exatas (subarvore incluida)")
    ap.add_argument("--file", help="arquivo com uma tag por linha")
    ap.add_argument("--dry-run", action="store_true", help="so conta, nao dessuspende")
    args = ap.parse_args()

    tags = _carregar_tags(args)
    if not tags:
        ap.error("nenhuma tag informada (posicional ou --file)")

    vivo = _anki_vivo()
    if not vivo:
        print("AnkiConnect nao respondeu (Anki fechado ou add-on 2055492159 ausente).")
        print("Fallback manual -- no Browse do Anki, para cada bloco: cole a busca,")
        print("Ctrl+A (selecionar tudo), Ctrl+J (alternar suspensao).\n")
        for t in tags:
            print(f"# {t}")
            print(f"  {_busca(t)}\n")
        print("Instale o AnkiConnect e deixe o Anki aberto pra eu fazer isso direto.")
        sys.exit(3)

    total = 0
    total_dessusp = 0
    print(f"AnkiConnect OK. {len(tags)} tag(s).{'  [DRY-RUN]' if args.dry_run else ''}\n")
    for t in tags:
        try:
            card_ids = _invoke("findCards", query=_busca(t))
        except RuntimeError as e:
            print(f"  ! {t}: erro na busca ({e})")
            continue
        n = len(card_ids)
        total += n
        if n == 0:
            print(f"  0     {t}   (nenhum card casa -- confira a tag)")
            continue
        if args.dry_run:
            print(f"  {n:5d} {t}")
        else:
            _invoke("unsuspend", cards=card_ids)
            total_dessusp += n
            print(f"  {n:5d} {t}   -> dessuspenso")
    print()
    if args.dry_run:
        print(f"Total que SERIA dessuspenso: {total} cards. Rode sem --dry-run para aplicar.")
    else:
        print(f"Dessuspenso: {total_dessusp} cards de {len(tags)} tag(s).")


if __name__ == "__main__":
    main()
