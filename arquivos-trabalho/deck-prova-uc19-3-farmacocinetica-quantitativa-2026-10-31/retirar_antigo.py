"""Notas de cinética que o lote 2 deixou no deck antigo Farmacocinética I (LOTE3) → deck-prova lote 3 (F-20261029-CLAUDE-04: "quero descartar o que já
temos, tá ruim" e "pode suspender e marcar").

    /usr/bin/python3 retirar_antigo.py --simular   # só conta
    /usr/bin/python3 retirar_antigo.py             # ANTES do apply: retira o que não volta
    /usr/bin/python3 retirar_antigo.py --mover     # DEPOIS do apply: cartas das notas reaproveitadas vão para o deck-prova (histórico intacto)

Antes do apply, só para as 17 notas LOTE3 (as demais já foram decididas no lote 2):
- reaproveitada no plano do deck-prova (compartilhados) → fica (o apply põe as tags novas);
- cinética quantitativa (LOTE3) → fica intocada no deck antigo até o lote 3 decidir;
- já retirada antes (NEBLI::retirado::*, as de CYP de 27/10) → fica como está;
- também de outra aula → só perde as tags das aulas antigas;
- o resto → cartas suspensas, tags das aulas antigas removidas, NEBLI::retirado::deck-prova e NEBLI::retirado-de::fc02|fc03.
Backup integral (notesInfo + estado das cartas) em backup-antigo-fc-lote3.json antes de escrever. Nada é apagado.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita  # noqa: E402

VELHAS = {"NEBLI::2026-uc19-farmacologia-02-farmacocinetica-i": "fc02", "NEBLI::2026-uc19-farmacologia-03-farmacocinetica-ii": "fc03"}
LOTE3 = {1792624457204, 1792624457454, 1792624457762, 1792624458027, 1792624458275, 1792624458975, 1792624463024, 1792624463275,
         1792624463844, 1792624464099, 1792624466325, 1792657537231, 1792657541196, 1792657541958, 1792657544384, 1792657545614,
         1793274287022}  # bolus, ke, t½, ordem, infusão, doses e Cmáx: cinética quantitativa do deck-prova 3
plan = json.loads((HERE / "plan.json").read_text())
manter = {int(k) for k in plan["compartilhados"]}


def da_aula(t):
    return any(t == L or t.startswith(f"NEBLI::cor::{L[7:]}::") for L in VELHAS) or any(
        t.startswith(f"NEBLI::ordem::{s}-") or t == f"NEBLI::compartilhado::{s}" for s in VELHAS.values())


def main(argv):
    A = Anki()
    if "--mover" in argv:
        # lição do lote 1 (30/10): dentro da janela os nomes são canônicos; mover sempre para plan["deck"], lido do plano
        if "--simular" in argv:
            return
        with escrita(A, "deck-prova dp3: mover reaproveitadas", sync=False):
            cards = [c for n in A("notesInfo", notes=sorted(manter)) for c in n["cards"]]
            velhos = [c["cardId"] for c in A("cardsInfo", cards=cards) if "Farmacocinética I" in c["deckName"]]
            print(f"mover {len(velhos)} cartas para {plan['deck']}")
            if velhos:
                A("changeDeck", cards=velhos, deck=plan["deck"])
        return
    nids = sorted(LOTE3)
    notes = A("notesInfo", notes=nids)
    retirar, desligar, ficar, lote3, ja = [], [], [], [], []
    for n in notes:
        outras = {t for t in n["tags"] if t.startswith("NEBLI::2026-") and t not in VELHAS}
        if n["noteId"] in manter:
            ficar.append(n)
        elif any(t.startswith("NEBLI::retirado::") for t in n["tags"]):
            ja.append(n)
        else:
            (desligar if outras else retirar).append(n)
    print(f"ficam {len(ficar)} · lote 3 {len(lote3)} · já retiradas {len(ja)} · só perdem a tag {len(desligar)} · retiradas {len(retirar)}")
    if "--simular" in argv:
        return
    estado = A("cardsInfo", cards=[c for n in notes for c in n["cards"]])
    (HERE / "backup-antigo-fc-lote3.json").write_text(json.dumps({"notes": notes, "cards": estado}, ensure_ascii=False, indent=1), encoding="utf-8")
    with escrita(A, "deck-prova dp3: retirar cinética antiga", sync=False):
        for n in retirar:
            A("suspend", cards=n["cards"])
            rm = [t for t in n["tags"] if da_aula(t)]
            de = " ".join(f"NEBLI::retirado-de::{s}" for L, s in VELHAS.items() if L in n["tags"])
            if rm:
                A("removeTags", notes=[n["noteId"]], tags=" ".join(rm))
            A("addTags", notes=[n["noteId"]], tags=f"NEBLI::retirado::deck-prova {de}")
        for n in desligar:
            rm = [t for t in n["tags"] if da_aula(t)]
            if rm:
                A("removeTags", notes=[n["noteId"]], tags=" ".join(rm))
    (HERE / "retirados-antigo.json").write_text(json.dumps({"retiradas": [n["noteId"] for n in retirar], "desligadas": [n["noteId"] for n in desligar],
                                                            "ficam": [n["noteId"] for n in ficar], "lote3": [n["noteId"] for n in lote3],
                                                            "ja_retiradas": [n["noteId"] for n in ja]}, indent=1), encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main(sys.argv[1:])
