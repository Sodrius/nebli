"""
Aplica a classificação proposta em `banco/indice/classificacao_proposta.json`
ao frontmatter YAML de cada `banco/questoes/q-XXXX.md`.

Regras:
- decisao = preservar  → não toca (aula já correta)
- decisao = ok         → grava aula: <top-1 slug>
- decisao = ambigua    → grava aula: <top-1 slug> (Davi aprovou em lote)
- decisao = vazia      → não grava (aula fica vazia para UC03+ futuras)

Antes de qualquer escrita: backup integral de `banco/questoes/` em
`backups/tecnicos/banco_pre-classificacao-uc02_<data>/`.

Depois de aplicar: regenera `banco/indice/banco_slim.json` via `gerar_slim.py`.

Uso:
    python3 banco/aplicar_classificacao.py            # aplica
    python3 banco/aplicar_classificacao.py --dry-run  # só lista o que faria
"""
from __future__ import annotations
import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTOES_DIR = ROOT / "banco" / "questoes"
PROPOSTA = ROOT / "banco" / "indice" / "classificacao_proposta.json"
BACKUP_BASE = ROOT / "backups" / "tecnicos"
GERAR_SLIM = ROOT / "banco" / "gerar_slim.py"

# Regex: captura bloco de frontmatter entre `---` no início do arquivo
RE_FRONTMATTER = re.compile(r"^(---\n)(.*?)(\n---\n)", re.DOTALL)
# Regex: linha `aula: ...` no frontmatter (com ou sem valor)
RE_AULA_LINE = re.compile(r"^aula:.*$", re.MULTILINE)


def encontrar_arquivo_questao(qid) -> Path | None:
    """Encontra q-XXXX.md a partir do id (int ou str estilo 'q-0149')."""
    if isinstance(qid, int):
        nome = f"q-{qid:04d}.md"
    else:
        s = str(qid)
        if s.startswith("q-"):
            nome = f"{s}.md"
        else:
            nome = f"q-{int(s):04d}.md"
    p = QUESTOES_DIR / nome
    return p if p.exists() else None


def aplicar_aula_no_frontmatter(conteudo: str, slug: str) -> tuple[str, str]:
    """
    Retorna (novo_conteudo, acao) onde acao é 'inserido'|'atualizado'|'inalterado'.
    """
    m = RE_FRONTMATTER.match(conteudo)
    if not m:
        return conteudo, "frontmatter-nao-encontrado"

    abre, miolo, fecha = m.group(1), m.group(2), m.group(3)

    # já existe linha aula:?
    aula_match = RE_AULA_LINE.search(miolo)
    if aula_match:
        atual = aula_match.group(0).split(":", 1)[1].strip()
        if atual == slug:
            return conteudo, "inalterado"
        novo_miolo = RE_AULA_LINE.sub(f"aula: {slug}", miolo, count=1)
        acao = "atualizado"
    else:
        # insere logo após `tags:` (linha 1-2 do frontmatter) se existir, senão no fim
        if re.search(r"^tags:", miolo, re.MULTILINE):
            novo_miolo = re.sub(
                r"^(tags:.*?)(\n)",
                rf"\1\naula: {slug}\2",
                miolo,
                count=1,
                flags=re.MULTILINE | re.DOTALL,
            )
        else:
            novo_miolo = miolo.rstrip() + f"\naula: {slug}"
        acao = "inserido"

    novo_conteudo = abre + novo_miolo + fecha + conteudo[m.end():]
    return novo_conteudo, acao


def backup(destino: Path) -> None:
    if destino.exists():
        print(f"[!] Backup ja existe: {destino} — abortando para nao sobrescrever")
        sys.exit(1)
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(QUESTOES_DIR, destino)
    print(f"[ok] Backup criado: {destino.relative_to(ROOT)}")


def regenerar_slim() -> None:
    if not GERAR_SLIM.exists():
        print(f"[!] {GERAR_SLIM} nao encontrado — pulando regeneracao do slim")
        return
    print(f"[i] Regenerando slim via {GERAR_SLIM.name}...")
    r = subprocess.run(
        [sys.executable, str(GERAR_SLIM)],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    if r.returncode != 0:
        print(f"[!] gerar_slim.py falhou (exit {r.returncode}):")
        print(r.stderr)
        return
    print(f"[ok] slim regenerado")
    if r.stdout.strip():
        print("    " + r.stdout.strip().replace("\n", "\n    "))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="lista o que seria feito, nao escreve nada")
    args = parser.parse_args()

    with open(PROPOSTA, encoding="utf-8") as f:
        d = json.load(f)

    # backup ANTES de qualquer escrita
    if not args.dry_run:
        data = datetime.now().strftime("%Y-%m-%d")
        destino = BACKUP_BASE / f"banco_pre-classificacao-uc02_{data}"
        backup(destino)

    contadores = {"escritas": 0, "inseridos": 0, "atualizados": 0,
                  "inalterados": 0, "pulados": 0, "nao_encontrados": 0,
                  "erros": []}

    for p in d["propostas"]:
        decisao = p["decisao"]
        if decisao in ("preservar", "vazia"):
            contadores["pulados"] += 1
            continue

        # ok ou ambigua → top-1
        if not p["candidatas"]:
            contadores["pulados"] += 1
            continue
        slug = p["candidatas"][0]["slug"]

        arquivo = encontrar_arquivo_questao(p["id"])
        if arquivo is None:
            contadores["nao_encontrados"] += 1
            contadores["erros"].append(f"q{p['id']}: arquivo nao encontrado")
            continue

        conteudo = arquivo.read_text(encoding="utf-8")
        novo, acao = aplicar_aula_no_frontmatter(conteudo, slug)

        if acao == "frontmatter-nao-encontrado":
            contadores["erros"].append(f"q{p['id']}: frontmatter nao encontrado em {arquivo.name}")
            continue
        if acao == "inalterado":
            contadores["inalterados"] += 1
            continue

        if not args.dry_run:
            arquivo.write_text(novo, encoding="utf-8")
        contadores[acao + "s"] += 1
        contadores["escritas"] += 1

    print()
    print("=== RESULTADO ===")
    print(f"  Decisao preservar/vazia (pulados): {contadores['pulados']}")
    print(f"  Inseridos (campo aula nao existia): {contadores['inseridos']}")
    print(f"  Atualizados (campo aula tinha outro valor): {contadores['atualizados']}")
    print(f"  Inalterados (campo aula ja batia): {contadores['inalterados']}")
    print(f"  Nao encontrados: {contadores['nao_encontrados']}")
    print(f"  Total escritas: {contadores['escritas']}{' (DRY RUN)' if args.dry_run else ''}")
    if contadores["erros"]:
        print(f"  ERROS ({len(contadores['erros'])}):")
        for e in contadores["erros"][:10]:
            print(f"    - {e}")

    if not args.dry_run and contadores["escritas"] > 0:
        regenerar_slim()


if __name__ == "__main__":
    main()
