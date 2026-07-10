#!/usr/bin/env python3
"""
NEBLI -- gerar_slim.py
Gera banco/indice/banco_slim.json a partir de banco/questoes/*.md.

Frente C2 do plano de economia de tokens (2026-05-16):
  O QUESTIONADOR usa o slim para tomar decisoes de classificacao
  (campo `aula:` da S9b) sem precisar ler o .md inteiro de cada
  candidata. Slim tem ~5x menos tokens que o banco.json completo
  (sem o array `itens:` por alternativa).

Campos do slim por questao:
  id, tags, nivel, formato, conceito_central, gabarito,
  uc_origem, prova, ano, armadilha, aula (se classificada),
  tags_pendentes_aprovacao, fonte, ingestao_data, figura (se houver)

NAO inclui:
  itens: [...]  (alternativas com tags por letra)
  Enunciado / Alternativas / Gabarito / Explicacao (corpo do .md)

Uso:
  python3 banco/gerar_slim.py
  python3 banco/gerar_slim.py --out banco/indice/banco_slim.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

# Campos a manter no slim. Filosofia: SO o minimo necessario para o
# QUESTIONADOR decidir se a questao bate com a aula que esta sendo
# resumida. Tudo o mais (armadilha, fonte, ano, ingestao_data,
# tags_pendentes, uc_origem, prova) sai -- nao informa a decisao de
# classificacao. Se o QUESTIONADOR precisar de detalhe, le o .md
# completo da questao especifica.
SLIM_FIELDS = {
    "id", "tags", "formato", "nivel", "conceito_central",
    "gabarito", "aula", "figura",
}


def parse_frontmatter(text):
    """Parse YAML-lite do frontmatter. Suficiente para o schema do banco
    (sem precisar de PyYAML). Suporta: chave: valor, listas inline
    [a, b, c], strings com aspas, datas, numeros."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm_text = m.group(1)
    data = {}
    # Linhas de chave: valor (suporta `itens:` que abre array YAML,
    # mas a gente pula por nao precisar)
    lines = fm_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        # Pula linha vazia
        if not line.strip():
            i += 1
            continue
        # Detecta `itens:` -- pula o array inteiro
        if line.rstrip().endswith("itens:") or line.strip() == "itens:":
            i += 1
            # Avanca enquanto linhas comecam com espaco (parte do array)
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith(" ") or lines[i].startswith("\t")):
                i += 1
            continue
        # Parse chave: valor
        m_kv = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(.*)$", line)
        if m_kv:
            key = m_kv.group(1)
            val = m_kv.group(2).strip()
            if key not in SLIM_FIELDS:
                i += 1
                continue
            # Lista inline [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                if not inner:
                    data[key] = []
                else:
                    parts = [p.strip().strip("'\"") for p in inner.split(",")]
                    data[key] = [p for p in parts if p]
            # String com aspas
            elif (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                data[key] = val[1:-1]
            # Numero
            elif re.match(r"^-?\d+$", val):
                data[key] = int(val)
            elif re.match(r"^-?\d+\.\d+$", val):
                data[key] = float(val)
            # Null
            elif val.lower() in ("null", "none", "~", ""):
                data[key] = None
            # String simples
            else:
                data[key] = val
        i += 1
    return data


def gerar_slim(questoes_dir, out_path):
    questoes = []
    erros = []
    md_files = sorted(questoes_dir.glob("*.md"))
    for md in md_files:
        try:
            text = md.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if fm is None:
                erros.append(f"  ! {md.name}: sem frontmatter")
                continue
            questoes.append(fm)
        except Exception as e:
            erros.append(f"  x {md.name}: {e}")

    out = {
        "versao_schema": 2,
        "tipo": "slim",
        "descricao": "Frontmatter sem `itens` -- 5x menor que banco.json completo. "
                     "Use para decisao de classificacao; leia .md completo so para "
                     "questoes que vai usar na E4.",
        "total": len(questoes),
        "questoes": questoes,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(questoes), erros


def main():
    parser = argparse.ArgumentParser(description="Gera banco_slim.json")
    parser.add_argument("--questoes", default=None, help="Pasta com .md (default: banco/questoes)")
    parser.add_argument("--out", default=None, help="Arquivo de saida (default: banco/indice/banco_slim.json)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent  # banco/
    questoes_dir = Path(args.questoes) if args.questoes else root / "questoes"
    out_path = Path(args.out) if args.out else root / "indice" / "banco_slim.json"

    if not questoes_dir.exists():
        print(f"x Pasta de questoes nao encontrada: {questoes_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"-> Lendo .md de: {questoes_dir}")
    n, erros = gerar_slim(questoes_dir, out_path)
    print(f"v {n} questoes processadas")
    if erros:
        print(f"! {len(erros)} erro(s)/warning(s):")
        for e in erros[:10]:
            print(e)
        if len(erros) > 10:
            print(f"  ... +{len(erros)-10}")
    print(f"-> Gravado em: {out_path}")
    size = out_path.stat().st_size
    print(f"   Tamanho: {size:,} bytes (~{size//4:,} tokens estimados)")


if __name__ == "__main__":
    main()
