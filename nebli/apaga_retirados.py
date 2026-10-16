"""Apaga as notas retiradas de uma refação, com backup recuperável antes (F-20261016-CLAUDE-09: “pode apagar as notas retiradas”).

    python3 -m nebli.apaga_retirados <motivo> [--simular]      # ex.: refacao-v2

Backup em arquivos-trabalho/backups-apagadas/<motivo>-<data-hora>.json: campos, tags, modelo, deck, cards com agendamento e
histórico de revisões (getReviewsOfCards). Recusa apagar nota em tela, nota ainda ligada a alguma aula (tag NEBLI::2026-*) e
nota com comentário de Davi não vazio sem registro no backup.
"""
import json
import sys
import time
from pathlib import Path

from nebli.decks import Anki, escrita, em_tela

ROOT = Path(__file__).resolve().parents[1]


def main(argv):
    motivo = argv[0]
    simular = "--simular" in argv
    A = Anki()
    nids = A("findNotes", query=f'"tag:NEBLI::retirado::{motivo}"')
    notes = A("notesInfo", notes=nids)
    ligadas = [n["noteId"] for n in notes if any(t.startswith("NEBLI::2026-") for t in n["tags"])]
    if ligadas:
        raise SystemExit(f"notas retiradas ainda ligadas a uma aula (não apago): {ligadas[:8]}")
    tela = em_tela(A) or set()
    alvo = [n for n in notes if n["noteId"] not in tela and not (set(n["cards"]) & tela)]
    cards = [c for n in alvo for c in n["cards"]]
    info = A("cardsInfo", cards=cards) if cards else []
    revs = A("getReviewsOfCards", cards=[str(c) for c in cards]) if cards else {}
    print(f"{len(alvo)} notas / {len(cards)} cards a apagar ({len(notes) - len(alvo)} adiadas por estarem em tela)")
    if simular or not alvo:
        return
    pasta = ROOT / "arquivos-trabalho" / "backups-apagadas"
    pasta.mkdir(parents=True, exist_ok=True)
    out = pasta / f"{motivo}-{time.strftime('%Y%m%d-%H%M%S')}.json"
    out.write_text(json.dumps({"motivo": motivo, "em": time.strftime("%Y-%m-%d %H:%M:%S"), "notas": alvo, "cards": info, "revisoes": revs},
                              ensure_ascii=False, indent=1))
    with escrita(A, f"apaga retirados {motivo}", sync=False):
        A("deleteNotes", notes=[n["noteId"] for n in alvo])
    resta = A("findNotes", query=f'"tag:NEBLI::retirado::{motivo}"')
    print(f"backup: {out}\napagadas {len(alvo)}; restam {len(resta)} com a tag")


if __name__ == "__main__":
    main(sys.argv[1:])
