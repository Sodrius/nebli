"""Prepara a refação de uma aula já em estudo, logo antes do apply da corrida nova (F-20261016-CLAUDE-08/09).

    python3 -m nebli.refacao <corrida nova> [--simular]

Pela tag da aula (plan.json da corrida nova):
- nota da aula que não está em `compartilhados` e só pertence a esta aula → suspensa, tags da aula removidas, `NEBLI::retirado::refacao-v2`
  (depois `nebli.apaga_retirados refacao-v2` apaga com backup, como Davi autorizou);
- nota que também pertence a outra aula → só perde as tags desta aula (ordem, cor, compartilhado);
- nota mantida (em `compartilhados`) → perde as tags antigas de ordem/cor desta aula (o apply recoloca) e, se tinha sido retirada numa enxugada
  antiga, volta: tags `retirado*` removidas e cards dessuspensos;
Registro em <corrida>/refacao.json.
"""
import json
import sys
from pathlib import Path

from nebli.decks import Anki, escrita


def main(argv):
    run = Path(argv[0]); simular = "--simular" in argv
    plan = json.loads((run / "plan.json").read_text())
    L, short = plan["lesson_id"], plan["short"]
    tag = f"NEBLI::{L}"
    keep = {int(k) for k in plan["compartilhados"]}
    A = Anki()
    nids = set(A("findNotes", query=f'"tag:{tag}"')) | set(A("findNotes", query=f'"tag:NEBLI::ordem::{short}-*"'))
    notes = {n["noteId"]: n for n in A("notesInfo", notes=sorted(nids | keep))}
    da_aula = lambda t: t == tag or t.startswith(f"NEBLI::cor::{L}::") or t.startswith(f"NEBLI::ordem::{short}-") or t == f"NEBLI::compartilhado::{short}"
    retirar, desligar, limpar, devolver = [], [], [], []
    for nid in sorted(nids - keep):
        n = notes[nid]
        outras = {t for t in n["tags"] if t.startswith("NEBLI::2026-") and t != tag}
        (desligar if outras else retirar).append(nid)
    for nid in sorted(keep):
        n = notes[nid]
        if any(t.startswith("NEBLI::retirado") for t in n["tags"]):
            devolver.append(nid)
        if any(t.startswith(f"NEBLI::ordem::{short}-") or t.startswith(f"NEBLI::cor::{L}::") for t in n["tags"]):
            limpar.append(nid)
    print(f"retirar {len(retirar)} · desligar (outra aula) {len(desligar)} · limpar tags antigas {len(limpar)} · devolver retiradas antigas {len(devolver)}")
    if simular:
        return
    with escrita(A, f"refação {short}", sync=False):
        for nid in retirar:
            n = notes[nid]
            A("suspend", cards=n["cards"])
            rm = [t for t in n["tags"] if da_aula(t)]
            if rm: A("removeTags", notes=[nid], tags=" ".join(rm))
            A("addTags", notes=[nid], tags=f"NEBLI::retirado::refacao-v2 NEBLI::retirado-de::{short}")
        for nid in desligar:
            rm = [t for t in notes[nid]["tags"] if da_aula(t)]
            if rm: A("removeTags", notes=[nid], tags=" ".join(rm))
        for nid in limpar:
            rm = [t for t in notes[nid]["tags"] if t.startswith(f"NEBLI::ordem::{short}-") or t.startswith(f"NEBLI::cor::{L}::")]
            if rm: A("removeTags", notes=[nid], tags=" ".join(rm))
        for nid in devolver:
            n = notes[nid]
            rm = [t for t in n["tags"] if t.startswith("NEBLI::retirado")]
            if rm: A("removeTags", notes=[nid], tags=" ".join(rm))
            A("unsuspend", cards=n["cards"])
    (run / "refacao.json").write_text(json.dumps({"retiradas": retirar, "desligadas": desligar, "limpas": limpar, "devolvidas": devolver}, indent=1))
    resto = set(A("findNotes", query=f'"tag:{tag}"')) - keep
    print("ok; notas com a tag da aula fora dos mantidos:", len(resto))


if __name__ == "__main__":
    main(sys.argv[1:])
