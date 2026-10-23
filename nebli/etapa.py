"""Diário das etapas do pipeline de deck (F-20261023-CLAUDE-02: “coloca gate para seguir o passo a passo e fazer o planejamento e revisão
de verdade, sem só fazer um deck com base no que vc acha que é a aula”).

    python3 -m nebli.etapa <corrida> E2 "o que fiz nesta etapa"     # registra a etapa ao concluí-la (E0…E8)
    python3 -m nebli.etapa <corrida> --ver

Cada linha de <corrida>/etapas.jsonl guarda a etapa, a hora e o hash dos artefatos dela. Registrar uma etapa exige o artefato da etapa
e a etapa anterior já registrada; a busca (E4) e o build recusam rodar sem a compreensão (E2) e o mapa (E3) prontos (`exigir_planejamento`).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ORDEM = ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"]
ARTEFATOS = {"E0": ["exemplares-lidos.json"], "E1": ["fontes-decl.json"], "E2": ["compreensao-aula.json"],
             "E3": ["mapa-de-profundidade.json", "escopo.json", "inventario.py"], "E4": ["busca/semantica.jsonl"],
             "E5": ["spec.py", "plan.json", "busca/cobertura.tsv"], "E6": ["receipt.json", "revisao-despejo.txt"],
             "E7": ["compreensao-aula.json"], "E8": []}


def _sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16] if p.is_file() else None


def registros(run: Path):
    arq = Path(run) / "etapas.jsonl"
    return [json.loads(l) for l in arq.read_text(encoding="utf-8").splitlines() if l.strip()] if arq.exists() else []


def problemas_compreensao(run: Path):
    """O que falta para a compreensão (E2) valer: o que a aula ensina, e em cada bloco de conteúdo o processo e o que se aprende."""
    try:
        d = json.loads((Path(run) / "compreensao-aula.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ["compreensao-aula.json ausente"]
    probs = []
    if "<" in str(d.get("o_que_a_aula_ensina", "")) or len(str(d.get("o_que_a_aula_ensina", ""))) < 150:
        probs.append("o_que_a_aula_ensina não escrito")
    for b in d.get("blocos", []):
        if b.get("papel") in ("principio", "exemplo"):
            apr = [x for x in b.get("aprender", []) if len(str(x).strip()) >= 15]
            if not apr:
                probs.append(f"bloco {b.get('laminas')} sem 'aprender' (o que o professor quer que se aprenda ali, conferido no slide)")
            if b.get("papel") == "exemplo" and not b.get("ilustra"):
                probs.append(f"bloco de exemplo {b.get('laminas')} sem 'ilustra' (a lâmina inicial do bloco de princípio que ele ilustra)")
    return probs


def versao(run: Path) -> int:
    m = re.search(r"^PIPELINE_VERSAO\s*=\s*(\d+)", (Path(run) / "spec.py").read_text(encoding="utf-8"), re.M) if (Path(run) / "spec.py").exists() else None
    return int(m.group(1)) if m else 0


def exigir_planejamento(run: Path, etapa: str = "a busca"):
    """Chamada pelas ferramentas de busca: sem compreensão e mapa prontos (E2 e E3 registradas), não roda (corridas v7)."""
    run = Path(run)
    if versao(run) < 7:
        return
    feitas = {r["etapa"] for r in registros(run)}
    falta = [e for e in ("E0", "E1", "E2", "E3") if e not in feitas]
    probs = problemas_compreensao(run)
    if falta or probs:
        raise SystemExit(f"{etapa} só roda depois de compreender e planejar a aula (pipeline v7): "
                         + (f"etapas não registradas {falta}; " if falta else "") + "; ".join(probs[:4]))


def registrar(run: Path, etapa: str, nota: str):
    run = Path(run)
    if etapa not in ORDEM:
        raise SystemExit(f"etapa desconhecida: {etapa}")
    feitas = [r["etapa"] for r in registros(run)]
    anterior = ORDEM[ORDEM.index(etapa) - 1] if etapa != "E0" else None
    if anterior and anterior not in feitas:
        raise SystemExit(f"{etapa} antes de {anterior}: siga o passo a passo")
    arts = {a: _sha(run / a) for a in ARTEFATOS[etapa]}
    if any(v is None for v in arts.values()):
        raise SystemExit(f"{etapa} sem artefato: {[a for a, v in arts.items() if v is None]}")
    if etapa == "E2":
        probs = problemas_compreensao(run)
        if probs:
            raise SystemExit("compreensão incompleta: " + "; ".join(probs[:5]))
    if len(nota.strip()) < 40:
        raise SystemExit("nota da etapa curta demais: diga o que foi feito e decidido (≥ 40 caracteres)")
    linha = {"etapa": etapa, "em": datetime.now(timezone.utc).isoformat(timespec="seconds"), "nota": nota.strip(), "artefatos": arts}
    with (run / "etapas.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(linha, ensure_ascii=False) + "\n")
    print(f"{etapa} registrada")


def ordem_ok(run: Path, ate: str):
    """Para o gate: etapas E0..ate registradas, cada uma uma vez antes da seguinte."""
    regs = registros(run)
    primeiro = {}
    for i, r in enumerate(regs):
        primeiro.setdefault(r["etapa"], i)
    precisa = ORDEM[: ORDEM.index(ate) + 1]
    falta = [e for e in precisa if e not in primeiro]
    fora = [e for a, e in zip(precisa, precisa[1:]) if a in primeiro and e in primeiro and primeiro[e] < primeiro[a]]
    return falta, fora


def main(argv):
    run = Path(argv[0])
    if "--ver" in argv:
        for r in registros(run):
            print(r["em"], r["etapa"], r["nota"][:100])
        return
    registrar(run, argv[1], " ".join(argv[2:]))


if __name__ == "__main__":
    main(sys.argv[1:])
