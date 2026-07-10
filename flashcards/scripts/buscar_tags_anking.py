#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""buscar_tags_anking.py -- busca tags do AnKing v12 por palavra-chave.

Lê o export de notas (flashcards/scripts/anking-v12-export.txt, coluna 22 =
tags) e devolve as tags do Step 1 que casam com os termos, com contagem de
cards e agrupadas por deck-recurso (B&B, Bootcamp, Physeo, SketchyBiochem,
FirstAid, ...). Serve o bloco "Onde aprofundar" da capa -- ver
referencias-externas/onde-aprofundar.md.

Uso:
    python flashcards/scripts/buscar_tags_anking.py glycogen
    python flashcards/scripts/buscar_tags_anking.py "krebs|citric|tca" --step 1
"""
import csv, collections, re, sys, argparse, os

# console do Windows (cp1252) quebra em beta/mu/etc; forcar UTF-8 na saida
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

EXPORT = os.path.join(os.path.dirname(__file__), "anking-v12-export.txt")
TAGCOL = 21  # 0-indexed (coluna 22, conforme cabeçalho #tags column:22)

def _datarows(f):
    for line in f:
        if not line.startswith("#"):
            yield line

def carregar_tags(path=EXPORT):
    tags = collections.Counter()
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.reader(_datarows(f), delimiter="\t", quotechar='"'):
            if len(row) > TAGCOL:
                for t in row[TAGCOL].split():
                    tags[t] += 1
    return tags

def buscar(termo, step="1", path=EXPORT):
    pfx = f"#AK_Step{step}_v12"
    rx = re.compile(termo, re.IGNORECASE)
    tags = carregar_tags(path)
    achados = [(t, c) for t, c in tags.items()
               if t.startswith(pfx) and rx.search(t)]
    # agrupa por recurso (nível 2, ex.: #B&B, #SketchyBiochem)
    por_recurso = collections.defaultdict(list)
    for t, c in achados:
        partes = t.split("::")
        recurso = partes[1] if len(partes) > 1 else "(raiz)"
        por_recurso[recurso].append((t, c))
    return por_recurso

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("termo", help="regex/termo (ex.: glycogen, 'krebs|tca')")
    ap.add_argument("--step", default="1")
    ap.add_argument("--full", action="store_true", help="mostra tag completa")
    args = ap.parse_args()
    por_recurso = buscar(args.termo, args.step)
    if not por_recurso:
        print(f"(nenhuma tag Step{args.step} casa '{args.termo}')")
        return
    total = sum(c for items in por_recurso.values() for _, c in items)
    print(f"# '{args.termo}' em #AK_Step{args.step}_v12 — {total} cards em "
          f"{len(por_recurso)} decks-recurso\n")
    for recurso in sorted(por_recurso, key=lambda r: -sum(c for _, c in por_recurso[r])):
        soma = sum(c for _, c in por_recurso[recurso])
        print(f"## {recurso} — {soma} cards")
        for t, c in sorted(por_recurso[recurso], key=lambda x: -x[1]):
            mostra = t if args.full else "::".join(t.split("::")[2:])
            print(f"   {c:4d}  {mostra}")
        print()

if __name__ == "__main__":
    main()
