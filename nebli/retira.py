"""Retira notas de uma aula antes de uma delta: suspende, tira as tags da aula/ordem/cor e marca NEBLI::retirado::<motivo>.

    python3 -m nebli.retira arquivos-trabalho/<corrida> --recibo receipt-antes.json chave:motivo [chave:motivo ...]

A nota (e o comentário de Davi) fica preservada, só sai da aula; o recibo informado perde a chave, para a delta não tentar apagá-la.
"""
import json
import sys
from pathlib import Path

from nebli.decks import Anki, escrita


def main(argv):
    run = Path(argv[0]); i = argv.index("--recibo"); recibo = run / argv[i + 1]
    pairs = [a.split(":", 1) for a in argv[i + 2:]]
    plan = json.loads((run / "plan.json").read_text()); L = plan["lesson_id"]; short = plan["short"]
    r = json.loads(recibo.read_text()); nid = {x["key"]: x["nid"] for x in r["notes"]}
    A = Anki(); feitos = []
    with escrita(A, f"retira {short}", sync=False):
        for key, motivo in pairs:
            if key not in nid: continue
            n = A("notesInfo", notes=[nid[key]])[0]
            if not n: continue
            A("suspend", cards=n["cards"])
            rm = [t for t in n["tags"] if L in t or f"::ordem::{short}-" in t or f"compartilhado::{short}" in t]
            if rm: A("removeTags", notes=[nid[key]], tags=" ".join(rm))
            A("addTags", notes=[nid[key]], tags=f"NEBLI::retirado::{motivo} NEBLI::retirado-de::{short}")
            feitos.append({"key": key, "nid": nid[key], "motivo": motivo})
    r["notes"] = [x for x in r["notes"] if x["key"] not in {k for k, _ in pairs}]
    recibo.write_text(json.dumps(r, ensure_ascii=False, indent=1))
    log = run / "retirados.json"
    old = json.loads(log.read_text()) if log.exists() else []
    log.write_text(json.dumps(old + feitos, ensure_ascii=False, indent=1))
    print(len(feitos), "retiradas")


if __name__ == "__main__":
    main(sys.argv[1:])
