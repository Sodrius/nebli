"""Leitura obrigatória por diferença (F-20261110-CLAUDE-01, sugestão 2 aprovada por Davi).

    python3 -m nebli.leitura diff              # mostra só o que mudou desde a última leitura registrada
    python3 -m nebli.leitura registrar <corrida>   # depois de ler: guarda as cópias e grava os hashes em exemplares-lidos.json

Cada arquivo de `gates.LEITURA_OBRIGATORIA` (e as FEEDBACKS) tem uma cópia da versão lida em `.cache/leitura/`
(fora do git). Arquivo sem cópia, ou reescrito em mais de 40% das linhas, é marcado LER INTEIRO. O gate continua o
mesmo (`exemplares_lidos`: sha256 vigente + ≥ 2 aprendizados por arquivo); o executor registra aprendizados novos
quando a diferença trouxe regra nova. Ler a diferença é leitura de verdade: nada é registrado sem ter sido lido.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CACHE = RAIZ / ".cache" / "leitura"
FEED = "flashcards/projeto/FEEDBACKS.md"


def _arquivos():
    from nebli import gates
    return list(gates.LEITURA_OBRIGATORIA) + [FEED]


def _copia(rel):
    return CACHE / rel.replace("/", "__")


def diff(out=sys.stdout):
    for rel in _arquivos():
        atual = (RAIZ / rel).read_text(encoding="utf-8").splitlines()
        c = _copia(rel)
        if not c.exists():
            print(f"### {rel}: LER INTEIRO (sem leitura registrada)", file=out)
            continue
        antes = c.read_text(encoding="utf-8").splitlines()
        if antes == atual:
            print(f"### {rel}: igual à última leitura", file=out)
            continue
        linhas = [l for l in difflib.unified_diff(antes, atual, lineterm="", n=1) if not l.startswith(("---", "+++"))]
        mudou = sum(1 for l in linhas if l[:1] in "+-")
        if mudou > 0.4 * max(len(atual), 1):
            print(f"### {rel}: LER INTEIRO (reescrito: {mudou} linhas mudaram)", file=out)
            continue
        print(f"### {rel}: {mudou} linhas mudaram", file=out)
        print("\n".join(linhas), file=out)


def registrar(run):
    from nebli import gates
    run = Path(run)
    CACHE.mkdir(parents=True, exist_ok=True)
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    for rel in _arquivos():
        _copia(rel).write_bytes((RAIZ / rel).read_bytes())
    p = run / "exemplares-lidos.json"
    d = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    d["leitura_sha256"] = {r: sha(RAIZ / r) for r in gates.LEITURA_OBRIGATORIA}
    d["guias_sha256"] = {g: sha(RAIZ / "flashcards/projeto" / g) for g in gates.GUIAS}
    d["guia_sha256"] = sha(RAIZ / "flashcards/projeto/GUIA_CARDS.md")
    d["feedbacks_lidos_ate"] = gates.ultimo_feedback()
    d.setdefault("leitura_aprendizados", {})
    d.setdefault("guias_aprendizados", {})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    faltam = [r for r in gates.LEITURA_OBRIGATORIA if len(d["leitura_aprendizados"].get(r, [])) < 2]
    print("registrado;", "faltam aprendizados em: " + ", ".join(faltam) if faltam else "aprendizados completos")


if __name__ == "__main__":
    if sys.argv[1:2] == ["diff"]:
        diff()
    elif sys.argv[1:2] == ["registrar"] and len(sys.argv) > 2:
        registrar(sys.argv[2])
    else:
        print(__doc__)
