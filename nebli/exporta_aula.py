"""Exporta o deck de uma aula (nome vivo, com o total que o add-on acrescenta) para entregar no Drive.

    python3 -m nebli.exporta_aula arquivos-trabalho/<corrida> "<saída>.apkg"

Confere que o deck do primeiro card do recibo é o deck do plano (sem o total) antes de exportar.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from nebli.rotulos import canonical


def main(argv=None):
    argv = argv or sys.argv[1:]
    from nebli.decks import Anki
    A = Anki()
    run, out = Path(argv[0]), Path(argv[1]).resolve()
    plan = json.loads((run / "plan.json").read_text())
    rec = json.loads((run / "receipt.json").read_text())
    card = int(next(iter(rec["notes"][0]["cards"])))
    deck = A("cardsInfo", cards=[card])[0]["deckName"]
    if canonical(deck) != plan["deck"]:
        raise SystemExit(f"deck vivo {deck!r} difere do plano {plan['deck']!r}")
    ok = A("exportPackage", deck=deck, path=str(out), includeSched=False)
    print(deck, ok, out.stat().st_size)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
