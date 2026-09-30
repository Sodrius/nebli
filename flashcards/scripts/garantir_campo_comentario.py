#!/usr/bin/env python3
"""Garante o campo vazio NEBLI_Comentario em todo tipo de nota usado nos decks NEBLI.

Pedido de Davi (30/09/2026): todo card tem um campo de comentário vazio para ele
escrever durante o estudo (atalho c do add-on nebli_atalhos). Os tipos AnKing
já têm; clones de IO, AnatoKing, Anatomy e MCAT não tinham.

    python3 flashcards/scripts/garantir_campo_comentario.py            # só lista (padrão)
    python3 flashcards/scripts/garantir_campo_comentario.py --aplicar  # acrescenta o campo

Acrescentar campo muda o esquema da coleção: o Anki pede confirmação na tela e o
próximo sync é completo (enviar este computador ao AnkiWeb). Sincronizar os outros
aparelhos ANTES e aplicar com Davi presente. O campo entra no fim, vazio; nenhum
conteúdo, template ou histórico de estudo é alterado. Novos clones de tipo de nota
já devem nascer com o campo (roteiro, seção 5), sem precisar deste script.
"""
import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki  # noqa: E402

FIELD = "NEBLI_Comentario"


def missing(call):
    cards = call("findCards", query="deck:NEBLI*")
    models = Counter()
    for start in range(0, len(cards), 800):
        for card in call("cardsInfo", cards=cards[start:start + 800]):
            models[card["modelName"]] += 1
    return {name: count for name, count in models.items()
            if FIELD not in call("modelFieldNames", modelName=name)}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--aplicar", action="store_true")
    args = parser.parse_args()
    call = Anki()
    todo = missing(call)
    if not todo:
        print(f"Todos os tipos de nota dos decks NEBLI têm {FIELD}.")
        return
    for name, count in sorted(todo.items()):
        print(f"sem {FIELD}: {name} ({count} cards NEBLI)")
    if not args.aplicar:
        print("Nada alterado. --aplicar acrescenta o campo (sync completo depois).")
        return
    for name in todo:
        call("modelFieldAdd", modelName=name, fieldName=FIELD)
    left = missing(call)
    print("Conferido: campo presente em todos." if not left else f"Ainda sem campo: {sorted(left)}")
    sys.exit(1 if left else 0)


if __name__ == "__main__":
    main()
