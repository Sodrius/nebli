"""Acrescenta à cobertura.json os itens do livro da UC (F-20261003-CLAUDE-13), ligados aos cards por palavras-chave.

    python3 -m nebli.livro_cov arquivos-trabalho/<corrida> <itens.json> [--grava]

itens.json: [[ "<Livro cap.: seção>", ["termo|sinônimo", "outro termo"], "<motivo se ficar fora>"? ], ...]
Cada elemento da lista de termos é obrigatório; alternativas separadas por '|'. Procura no alvo, nome, texto, Remarks e
Extra de cada entrada e no alvo dos compartilhados. Sem card, o item fica com 'excluido' (o motivo, obrigatório no gate).
Sem --grava só mostra o mapeamento: OK (com cards), EX (fora com motivo), XX (sem card e sem motivo, corrigir).
"""
from __future__ import annotations

import html
import json
import re
import sys
import unicodedata


def norm(s):
    s = unicodedata.normalize("NFKD", html.unescape(re.sub(r"<[^>]+>", " ", s or "")))
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def main(argv=None):
    argv = argv or sys.argv[1:]
    run, src = argv[0], argv[1]
    plan = json.load(open(run + "/plan.json"))
    docs = {e["key"]: norm(" ".join([e.get("alvo", ""), e.get("name", ""), e["fields"].get("Text", ""), e["fields"].get("Remarks", ""),
                                      e["fields"].get("Extra", "")])) for e in plan["entries"]}
    for nid, sh in plan.get("compartilhados", {}).items():
        docs[f"sh-{nid}"] = norm(sh.get("alvo", ""))
    cov = json.load(open(run + "/cobertura.json"))
    cov["itens"] = [i for i in cov["itens"] if not str(i.get("fonte", "")).lower().startswith("livro")]
    bad = 0
    for it in json.load(open(src)):
        item, words = it[0], it[1]
        excl = it[2] if len(it) > 2 else ""
        cards = [k for k, d in docs.items() if all(any(norm(w) in d for w in alt.split("|")) for alt in words)] if words else []
        rec = {"fonte": "livro " + item.split(":")[0], "item": item, "cards": cards}
        if not cards:
            rec["excluido"] = excl
            bad += not excl
        cov["itens"].append(rec)
        print(("OK " if cards else ("EX " if excl else "XX ")) + item, cards[:6])
    if "--grava" in argv:
        json.dump(cov, open(run + "/cobertura.json", "w"), ensure_ascii=False, indent=1)
        print("gravado")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
