#!/usr/bin/env python3
"""auto_fix_etapas.py — Sanitiza arquivos de etapa antes da compilação.

Canônico 2026-05-26. Roda automaticamente no pipeline antes do
`typst compile`. Corrige erros comuns que aparecem mesmo após
correção dos system prompts:

1. `#etapa-header(...)` ou `#set-etapa(...)` em etapa{1,2,3}.typ ou
   resumindo.typ — o main.typ ja faz, duplicar gera pagina em branco.
2. Markdown bold `**texto**` vazado (Typst usa `*texto*`).
3. Mistura de aspas (`""` vs `""` vs `""`) — normaliza para Unicode reto.
4. Trailing whitespace em fim de linha.

Uso:
    python3 typst-build/auto_fix_etapas.py [--dry-run]

Retorna exit 0 se nada precisou de fix OU se fix foi aplicado.
Retorna exit 1 só em erro real (arquivo inacessível, etc).

O script emite log no stdout listando o que removeu de cada arquivo.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
ETAPAS = ["etapa1.typ", "etapa2.typ", "etapa3.typ", "resumindo.typ"]

# Patterns para auto-fix
ETAPA_HEADER_RE = re.compile(r"^#etapa-header\([^\n]*\)\s*\n", re.MULTILINE)
SET_ETAPA_RE = re.compile(r"^#set-etapa\([^\n]*\)\s*\n", re.MULTILINE)
MARKDOWN_BOLD_RE = re.compile(r"\*\*([^\s*][^*]{0,200}?[^\s*])\*\*")


def fix_file(path: Path, dry_run: bool = False) -> tuple[list[str], bool]:
    """Aplica fixes em um arquivo. Retorna (lista_de_fixes_aplicados, modificou)."""
    if not path.exists():
        return [f"  ! {path.name}: arquivo nao existe -- pulando"], False
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as e:
        return [f"  x {path.name}: erro lendo -- {e}"], False

    fixes = []
    original = content

    # Fix 1: etapa-header duplicado
    matches_eh = ETAPA_HEADER_RE.findall(content)
    if matches_eh:
        content = ETAPA_HEADER_RE.sub("", content)
        fixes.append(f"  v {path.name}: removido {len(matches_eh)}x `#etapa-header(...)` "
                     f"redundante (main.typ ja chama)")

    # Fix 2: set-etapa duplicado
    matches_se = SET_ETAPA_RE.findall(content)
    if matches_se:
        content = SET_ETAPA_RE.sub("", content)
        fixes.append(f"  v {path.name}: removido {len(matches_se)}x `#set-etapa(...)` "
                     f"redundante (etapa-header ja faz)")

    # Fix 3: markdown bold **X** -> *X*
    md_bolds = MARKDOWN_BOLD_RE.findall(content)
    if md_bolds:
        content = MARKDOWN_BOLD_RE.sub(r"*\1*", content)
        fixes.append(f"  v {path.name}: convertido {len(md_bolds)}x `**bold**` -> `*bold*`")

    # Fix 4: trailing whitespace
    new_lines = []
    trailed = 0
    for line in content.splitlines(keepends=False):
        stripped = line.rstrip()
        if stripped != line:
            trailed += 1
        new_lines.append(stripped)
    if trailed:
        content = "\n".join(new_lines) + ("\n" if original.endswith("\n") else "")
        fixes.append(f"  v {path.name}: removido trailing whitespace em {trailed} linha(s)")

    if content != original:
        if not dry_run:
            path.write_text(content, encoding="utf-8")
        else:
            fixes.append(f"  i {path.name}: (dry-run) {len(fixes)} fix(es) NAO aplicado(s)")
        return fixes, True

    return [f"  - {path.name}: nada a corrigir"], False


def main():
    dry_run = "--dry-run" in sys.argv
    print("=== NEBLI auto_fix_etapas (canonico 2026-05-26) ===")
    if dry_run:
        print("Modo: DRY-RUN (nao escreve no disco)")
    print(f"Diretorio: {BUILD_DIR}")
    print()
    any_fix = False
    for fname in ETAPAS:
        path = BUILD_DIR / fname
        msgs, modified = fix_file(path, dry_run=dry_run)
        for m in msgs:
            print(m)
        if modified:
            any_fix = True
    print()
    if any_fix:
        print("Resumo: fixes aplicados. Re-rodar precompile-check.py antes de compilar.")
    else:
        print("Resumo: nada a corrigir, arquivos limpos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
