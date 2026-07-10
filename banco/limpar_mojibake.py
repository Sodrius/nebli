"""
limpar_mojibake.py - Remove sequencias mojibake (UTF-8 lido como Latin-1)
do banco. Tenta recuperar caracteres acentuados quando o padrao e
inequivoco.

Padroes comuns no banco NEBLI (originados de ingestao antiga via OCR):
  a^TM " (em-dash mojibake)
  a^TM ' (apostrofo)
  a^TM aspas
  A   NBSP
  A-tilde+caractere = duplo encode UTF-8

Uso:
  python banco/limpar_mojibake.py            (dry-run)
  python banco/limpar_mojibake.py --apply
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUESTOES = ROOT / "questoes"

# Substituicoes usando Unicode escapes (seguro contra mojibake no proprio source)
# â = a-circunflexo
# € = euro sign (vira nos pares mojibake)
SUBSTITUICOES = [
    # a^euro + variantes do quote/dash
    ("â€”", "—"),  # â€" -> em-dash
    ("â€“", "—"),  # â€" -> en-dash (unificamos)
    ("â€™", "’"),  # â€™ -> '
    ("â€œ", "“"),  # â€œ -> "
    ("â€", "”"),  # â€  -> "
    ("â€¦", "…"),  # â€¦ -> ...
    ("â€¢", "•"),  # â€¢ -> bullet
    # A-til + caractere = duplo encode UTF-8
    ("Ã©", "é"),  # Ã© -> é
    ("Ã¡", "á"),  # Ã¡ -> á
    ("Ã£", "ã"),  # Ã£ -> ã
    ("Ã§", "ç"),  # Ã§ -> ç
    ("Ã­", "í"),  # Ã­ -> í
    ("Ã³", "ó"),  # Ã³ -> ó
    ("Ãµ", "õ"),  # Ãµ -> õ
    ("Ãº", "ú"),  # Ãº -> ú
    ("Ãª", "ê"),  # Ãª -> ê
    ("Ã¢", "â"),  # Ã¢ -> â
    ("Ã´", "ô"),  # Ã´ -> ô
    # NBSP corrompido
    ("Â ", " "),
]

# residual: qualquer â€X que sobrou vira em-dash
RESIDUAL_RE = re.compile("â€[\\s\\S]")


def limpar(text: str) -> tuple[str, int]:
    n = 0
    for src, dst in SUBSTITUICOES:
        c = text.count(src)
        if c:
            text = text.replace(src, dst)
            n += c
    resid = RESIDUAL_RE.findall(text)
    if resid:
        text = RESIDUAL_RE.sub("—", text)
        n += len(resid)
    return text, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="grava (default dry-run)")
    args = ap.parse_args()

    total_subs = 0
    arquivos = 0
    for p in sorted(QUESTOES.glob("q-*.md")):
        original = p.read_text(encoding="utf-8")
        novo, n = limpar(original)
        if n > 0:
            arquivos += 1
            total_subs += n
            print(f"{p.name}: {n} substituicoes")
            if args.apply:
                p.write_text(novo, encoding="utf-8")
    modo = "APLICADO" if args.apply else "DRY-RUN"
    print(f"\n[{modo}] {arquivos} arquivos, {total_subs} substituicoes totais")


if __name__ == "__main__":
    main()
