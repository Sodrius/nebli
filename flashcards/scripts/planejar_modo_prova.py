#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera um plano de cram sem tocar no Anki, no FSRS ou no Drive.

O resultado traz duas filas temporarias para criar no Anki:
  - devidos/erros, com rescheduling ligado;
  - novos vistos apenas para a prova, com rescheduling desligado.

O script e deliberadamente offline: nao abre localhost, nao sincroniza e nao
altera preset. Assim funciona para qualquer UC/prova e e seguro por padrao.
"""
import argparse


def quote(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', r'\"')


def build_queries(deck: str, tag: str | None, erros_dias: int) -> list[tuple[str, str, str]]:
    base = f'deck:"{quote(deck)}"'
    tag_filter = f' tag:"{quote(tag)}"' if tag else ""
    return [
        ("DEVIDOS E ERROS", f'{base} (is:due OR rated:{erros_dias}:1) -is:suspended', "reschedule ON"),
        ("PREVIEW DE NOVOS EXAM-ONLY", f'{base} is:new -is:suspended{tag_filter}', "reschedule OFF"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Planeja o modo prova sem alterar o agendamento.")
    parser.add_argument("--deck", required=True, help="ex.: NEBLI::UC02::P3")
    parser.add_argument("--tag", help="tag opcional da prova, ex.: NEBLI::scope::exam")
    parser.add_argument("--erros-dias", type=int, default=7, help="janela de Again (default: 7)")
    parser.add_argument("--limit", type=int, default=9999, help="limite do filtered deck")
    args = parser.parse_args()
    if not args.deck.startswith("NEBLI::"):
        parser.error('o deck deve ficar sob "NEBLI::"')
    if args.erros_dias < 1 or args.limit < 1:
        parser.error("--erros-dias e --limit devem ser positivos")

    print(f"MODO PROVA — {args.deck}")
    print("Crie dois Filtered Decks temporarios no Anki:")
    for name, query, scheduling in build_queries(args.deck, args.tag, args.erros_dias):
        print(f"\n{name}\n  Search: {query}\n  Limit: {args.limit}\n  {scheduling}")
    print("\nOrdem: devidos -> erros -> questoes da faculdade -> preview indispensavel.")
    print("Again = esqueceu. Hard = lembrou corretamente, mas com esforco.")
    print("Depois da prova, esvazie os filtered decks; o longitudinal continua intacto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
