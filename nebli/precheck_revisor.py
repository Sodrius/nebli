"""Pré-checagem antes de mandar a corrida ao revisor único (F-20261111-CLAUDE-02: menos rodadas).

Davi (11/11): "pensa como o corretor pode ser mais eficiente, para termos menos rodadas". Nas corridas 67 e 75 a maioria das
rodadas do revisor apontou defeito mecânico que o executor podia ver sozinho. Este comando junta essas checagens:

    python3 -m nebli.precheck_revisor arquivos-trabalho/<corrida>

- lint duro dos autorais (negrito de contexto, critério negritado nas linhas do organizador, metacomentário, símbolo solto);
- forma das lacunas de TODO card (≤ 3 palavras, resposta visível na frente, negrito dentro da lacuna);
- resposta repetida entre cards sem `duplicacao_ok`;
- AnKing marcado só Step 2;
- organizador com trecho literal curto (< 35 caracteres).
Sai com código 1 se houver qualquer problema: só mandar ao revisor com a saída limpa.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def _norm(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t or "")).strip().casefold()


def problemas(run: Path):
    from nebli import lint_cards, verificador_casos
    plan = json.loads((run / "plan.json").read_text())
    probs = []
    v = int(plan.get("pipeline_versao") or 1)
    for key, text, extra, ep in lint_cards.from_plan(run / "plan.json"):
        duros = [m for lvl, m in (lint_cards.check(key, text, extra, version=v, front_language=plan.get("idioma_frente", "en")) if text else []) + ep if lvl == "dura"]
        probs += [f"lint {key}: {m}" for m in duros]
    respostas = defaultdict(list)
    for e in plan.get("entries", []):
        for m in verificador_casos.forma_das_lacunas(e) or []:
            probs.append(f"forma {e['key']}: {m}")
        txt = (e.get("fields") or {}).get("Text", "")
        alvo = tuple(sorted({_norm(a.split("::")[0]) for a in re.findall(r"\{\{c\d+::(.*?)\}\}", txt, re.S)}))
        if alvo and not e.get("duplicacao_ok"):
            respostas[alvo].append(e["key"])
        if e.get("origin") == "Autoral" and e.get("organizador") and len(_norm(e.get("organizacao_trecho"))) < 35:
            probs.append(f"organizador {e['key']}: trecho literal com menos de 35 caracteres")
    for alvo, ks in respostas.items():
        if len(ks) > 1 and alvo not in {("no",), ("yes",)}:
            probs.append(f"resposta repetida {ks}: {alvo}")
        elif len(ks) > 1:
            probs.append(f"resposta sim/não repetida {ks}: justificar com duplicacao_ok ou retirar")
    try:
        from nebli.spec_lib import _call
        srcs = [e["src"] for e in plan.get("entries", []) if e.get("kind") == "text" and e.get("src")]
        for n in _call("notesInfo", notes=srcs):
            tags = " ".join(n.get("tags", []))
            if "Only_Step_2" in tags or ("Step2" in tags and "Step1" not in tags):
                probs.append(f"fonte só Step 2: ak{n['noteId']}")
    except Exception as exc:  # sem Anki, avisa
        probs.append(f"(Anki indisponível para checar Step 2: {exc})")
    return probs


def main(argv=None):
    run = Path((argv or sys.argv[1:])[0])
    probs = problemas(run)
    for p in probs:
        print(p)
    print(f"{len(probs)} problema(s) mecânicos" + ("" if probs else ": pode mandar ao revisor"))
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
