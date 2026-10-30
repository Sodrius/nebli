"""Deck antigo da UC19 aula 01 (Introdução e mecanismos de ação) → deck-prova lote 1 (F-20261029-CLAUDE-04: "quero descartar o que já
temos, tá ruim" e "pode suspender e marcar").

    /usr/bin/python3 retirar_antigo.py --simular   # só conta
    /usr/bin/python3 retirar_antigo.py             # ANTES do apply: retira o que não volta
    /usr/bin/python3 retirar_antigo.py --mover     # DEPOIS do apply: cartas das notas reaproveitadas vão para o deck-prova (histórico intacto)

Antes do apply, para cada nota com a tag da aula 01:
- reaproveitada no plano do deck-prova (compartilhados) → fica (o apply põe as tags novas);
- também de outra aula → só perde as tags da aula 01;
- o resto → cartas suspensas, tags da aula 01 removidas, NEBLI::retirado::deck-prova e NEBLI::retirado-de::fa01.
Backup integral (notesInfo + estado das cartas) em backup-antigo-fa01.json antes de escrever. Nada é apagado.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita  # noqa: E402

L_OLD, SHORT_OLD = "NEBLI::2026-uc19-farmacologia-01-introducao-mecanismos", "fa01"
plan = json.loads((HERE / "plan.json").read_text())
manter = {int(k) for k in plan["compartilhados"]}
da_aula = lambda t: t == L_OLD or t.startswith(f"NEBLI::cor::{L_OLD[7:]}::") or t.startswith(f"NEBLI::ordem::{SHORT_OLD}-") or t == f"NEBLI::compartilhado::{SHORT_OLD}"


def main(argv):
    A = Anki()
    if "--mover" in argv:
        # 30/10: o nome lido fora da janela vem com os totais do add-on; usá-lo dentro da janela criou uma árvore NEBLI paralela.
        # Dentro da janela os nomes são canônicos: mover sempre para plan["deck"], lido do plano.
        if "--simular" in argv:
            return
        with escrita(A, "deck-prova dp1: mover reaproveitadas", sync=False):
            cards = [c for n in A("notesInfo", notes=sorted(manter)) for c in n["cards"]]
            velhos = [c["cardId"] for c in A("cardsInfo", cards=cards) if "Introdução à farmacologia" in c["deckName"]]
            print(f"mover {len(velhos)} cartas para {plan['deck']}")
            if velhos:
                A("changeDeck", cards=velhos, deck=plan["deck"])
        return
    nids = A("findNotes", query=f'"tag:{L_OLD}"')
    notes = A("notesInfo", notes=nids)
    retirar, desligar, ficar = [], [], []
    for n in notes:
        outras = {t for t in n["tags"] if t.startswith("NEBLI::2026-") and t != L_OLD}
        (ficar if n["noteId"] in manter else desligar if outras else retirar).append(n)
    print(f"ficam {len(ficar)} · só perdem a tag da aula 01 {len(desligar)} · retiradas {len(retirar)}")
    if "--simular" in argv:
        return
    estado = A("cardsInfo", cards=[c for n in notes for c in n["cards"]])
    (HERE / "backup-antigo-fa01.json").write_text(json.dumps({"notes": notes, "cards": estado}, ensure_ascii=False, indent=1), encoding="utf-8")
    with escrita(A, "deck-prova dp1: retirar aula 01 antiga", sync=False):
        for n in retirar:
            A("suspend", cards=n["cards"])
            rm = [t for t in n["tags"] if da_aula(t)]
            if rm:
                A("removeTags", notes=[n["noteId"]], tags=" ".join(rm))
            A("addTags", notes=[n["noteId"]], tags=f"NEBLI::retirado::deck-prova NEBLI::retirado-de::{SHORT_OLD}")
        for n in desligar:
            rm = [t for t in n["tags"] if da_aula(t)]
            if rm:
                A("removeTags", notes=[n["noteId"]], tags=" ".join(rm))
    (HERE / "retirados-antigo.json").write_text(json.dumps({"retiradas": [n["noteId"] for n in retirar], "desligadas": [n["noteId"] for n in desligar],
                                                            "ficam": [n["noteId"] for n in ficar]}, indent=1), encoding="utf-8")
    print("ok")


def _canon(d):
    import re
    return "::".join(re.sub(r"\s*\(\d+\|\d+\|\d+\)$", "", p) for p in d.split("::"))


if __name__ == "__main__":
    main(sys.argv[1:])
