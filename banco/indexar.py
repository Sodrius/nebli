#!/usr/bin/env python3
"""
indexar.py — Gera o índice JSON do banco de questões NEBLI.

Lê todos os arquivos questoes/q-*.md, extrai o frontmatter YAML, e gera
indice/banco.json com os campos relevantes para busca rápida.

O JSON gerado NÃO contém o enunciado completo — só metadados de busca
(id, tags, nível, formato, conceito, UC, prova, ano, fonte, armadilha).
Quem precisa do enunciado lê o arquivo .md correspondente.

Uso:
    python indexar.py

Saída:
    indice/banco.json
    indice/estatisticas.json (cobertura por tag, distribuição de níveis, etc.)

Dependências:
    pip install pyyaml
"""

from pathlib import Path
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime

try:
    import yaml
except ImportError:
    print("ERRO: pyyaml não instalado. Rode: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


BANCO_DIR = Path(__file__).parent
QUESTOES_DIR = BANCO_DIR / "questoes"
INDICE_DIR = BANCO_DIR / "indice"
META_DIR = BANCO_DIR / "meta"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def ler_frontmatter(caminho_md: Path) -> dict | None:
    """Extrai o frontmatter YAML de um arquivo markdown. Retorna dict ou None."""
    texto = caminho_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(texto)
    if not match:
        print(f"AVISO: {caminho_md.name} não tem frontmatter — ignorado", file=sys.stderr)
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"ERRO ao parsear YAML de {caminho_md.name}: {e}", file=sys.stderr)
        return None


def campos_de_busca(fm: dict) -> dict:
    """Extrai só os campos relevantes para o índice (sem enunciado)."""
    return {
        "id": fm.get("id"),
        "tags": fm.get("tags", []) or [],
        "nivel": fm.get("nivel"),
        "formato": fm.get("formato"),
        "conceito_central": fm.get("conceito_central"),
        "uc_origem": fm.get("uc_origem") or None,
        "prova": fm.get("prova") or None,
        "ano": fm.get("ano") or None,
        "fonte": fm.get("fonte") or None,
        "armadilha": fm.get("armadilha") or None,
        "figura": fm.get("figura") or None,
        "tags_pendentes": fm.get("tags_pendentes_aprovacao", []) or [],
        "itens": fm.get("itens", []) or [],
    }


def calcular_estatisticas(questoes: list[dict]) -> dict:
    """Estatísticas do banco — cobertura, distribuição, lacunas."""
    total = len(questoes)
    if total == 0:
        return {"total": 0, "vazio": True}

    todas_tags = []
    for q in questoes:
        todas_tags.extend(q["tags"])
        for item in q.get("itens", []):
            todas_tags.extend(item.get("tags", []))

    cobertura_tag = Counter(todas_tags)
    nivel_dist = Counter(q["nivel"] for q in questoes if q["nivel"])
    formato_dist = Counter(q["formato"] for q in questoes if q["formato"])
    uc_dist = Counter(q["uc_origem"] for q in questoes if q["uc_origem"])

    pendentes_total = sum(len(q.get("tags_pendentes", [])) for q in questoes)

    tags_raras = [tag for tag, n in cobertura_tag.items() if n <= 2]
    tags_dominantes = [tag for tag, n in cobertura_tag.items() if n >= 30]

    sem_uc = sum(1 for q in questoes if not q["uc_origem"])
    sem_armadilha = sum(1 for q in questoes if not q["armadilha"])

    return {
        "total_questoes": total,
        "tags_unicas": len(cobertura_tag),
        "cobertura_por_tag": dict(cobertura_tag.most_common()),
        "distribuicao_nivel": dict(nivel_dist),
        "distribuicao_formato": dict(formato_dist),
        "distribuicao_uc": dict(uc_dist.most_common()),
        "tags_pendentes_total": pendentes_total,
        "tags_com_baixa_cobertura": tags_raras,
        "tags_dominantes": tags_dominantes,
        "questoes_sem_uc": sem_uc,
        "questoes_sem_armadilha": sem_armadilha,
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
    }


def main() -> int:
    if not QUESTOES_DIR.exists():
        print(f"ERRO: pasta {QUESTOES_DIR} não existe", file=sys.stderr)
        return 1

    INDICE_DIR.mkdir(exist_ok=True)

    arquivos = sorted(QUESTOES_DIR.glob("q-*.md"))
    questoes = []
    erros = 0

    for arq in arquivos:
        fm = ler_frontmatter(arq)
        if fm is None:
            erros += 1
            continue
        if "id" not in fm:
            print(f"AVISO: {arq.name} sem campo 'id' — ignorado", file=sys.stderr)
            erros += 1
            continue
        questoes.append(campos_de_busca(fm))

    # Normalizar id para int e ordenar
    for q in questoes:
        try:
            q["id"] = int(q["id"])
        except (ValueError, TypeError):
            pass
    questoes.sort(key=lambda q: q["id"] if isinstance(q["id"], int) else 99999)

    # banco.json — índice principal
    saida_banco = {
        "versao_schema": 1,
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "total": len(questoes),
        "questoes": questoes,
    }
    (INDICE_DIR / "banco.json").write_text(
        json.dumps(saida_banco, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # estatisticas.json — saúde do banco
    stats = calcular_estatisticas(questoes)
    (INDICE_DIR / "estatisticas.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"OK: {len(questoes)} questões indexadas em {INDICE_DIR}/banco.json")
    if erros:
        print(f"AVISO: {erros} arquivo(s) com problema, ver mensagens acima")
    print(f"Estatísticas: {INDICE_DIR}/estatisticas.json")
    if stats.get("tags_unicas"):
        print(f"  - {stats['tags_unicas']} tags únicas")
        if stats.get("tags_com_baixa_cobertura"):
            print(f"  - {len(stats['tags_com_baixa_cobertura'])} tags com <=2 questoes (candidatas a fusao)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
