#!/usr/bin/env python3
"""verificar_gabarito_resumo.py — Cruza o gabarito do tema-card YAML com o
conteúdo de etapa2.typ, validando consistência estrutural e flagando
possíveis erros editoriais.

Canônico 2026-05-26. Diferente do `verificar_gabarito_ordem.py` (que opera
sobre cadernos onde cada questão carrega `gabarito` no frontmatter), aqui o
gabarito vem do `tema_card_<slug>.yml`. O verificador não consegue *adivinhar*
qual é a correta — mas consegue checar:

1. Toda Q do gabarito existe em etapa2.typ.
2. Toda Q em etapa2.typ tem gabarito declarado no tema-card.
3. Letra do gabarito (MC: A-E; CE: combinação de C/E de tamanho igual ao número
   de itens da questão) é válida para o formato declarado.
4. Para CE: número de chars do gabarito = número de itens da questão.
5. Alternativa apontada não é trivialmente curta/placeholder (heurística).
6. Distribuição do gabarito (sorteio): A-E balanceadas, sequências
   monotonicas detectadas.

Uso:
    python3 typst-build/verificar_gabarito_resumo.py <slug>
    python3 typst-build/verificar_gabarito_resumo.py --tema-card path.yml --etapa2 etapa2.typ

Retorna exit 0 se ok, exit 1 em discrepância bloqueante.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
TEMA_CARDS_DIR = ROOT / "arquivos-trabalho" / "tema-cards"
BUILD_DIR = Path(__file__).resolve().parent

# --- Parsers ---

QMC_RE = re.compile(
    r'#questao-mc\("(\d+)",\s*badge-(\w+),\s*\[([\s\S]*?)\],\s*'
    r'\(\(([\s\S]*?)\)\)\)',
    re.MULTILINE
)
QCE_RE = re.compile(
    r'#questao-ce\("(\d+)",\s*badge-(\w+),\s*\[([\s\S]*?)\],\s*'
    r'\(\(([\s\S]*?)\)\)\)',
    re.MULTILINE
)
ALT_RE = re.compile(r'\("([A-E]|I|II|III|IV)",\s*\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\)')


def parse_etapa2(path: Path):
    """Retorna lista de dicts: {'num': '01', 'tipo': 'mc'|'ce',
    'badge': str, 'enunciado': str, 'alts': [(letra, texto), ...]}."""
    if not path.exists():
        return [], [f"x etapa2.typ não encontrado em {path}"]
    content = path.read_text(encoding="utf-8")
    questoes = []
    erros = []
    for m in QMC_RE.finditer(content):
        num, badge, enunciado, alts_blob = m.groups()
        alts = ALT_RE.findall("((" + alts_blob + "))")
        questoes.append({
            "num": num, "tipo": "mc", "badge": badge,
            "enunciado": enunciado.strip(),
            "alts": [(l, t.strip()) for l, t in alts],
        })
    for m in QCE_RE.finditer(content):
        num, badge, enunciado, alts_blob = m.groups()
        alts = ALT_RE.findall("((" + alts_blob + "))")
        questoes.append({
            "num": num, "tipo": "ce", "badge": badge,
            "enunciado": enunciado.strip(),
            "alts": [(l, t.strip()) for l, t in alts],
        })
    # Sort by num
    questoes.sort(key=lambda q: int(q["num"]))
    return questoes, erros


def parse_tema_card(path: Path):
    """Retorna dict { '01': 'B', '02': 'CCCE', ... }."""
    if not path.exists():
        return None, [f"x Tema card não encontrado: {path}"]
    if yaml is None:
        return None, ["x PyYAML não instalado. `pip install pyyaml`"]
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    gabarito = data.get("gabarito", {})
    flat = {}
    for cat, items in gabarito.items():
        for item in items:
            num, letra = item
            flat[str(num).zfill(2)] = str(letra).upper()
    return flat, []


# --- Validações ---

def validate(questoes, gabarito):
    erros = []
    warnings = []
    nums_etapa2 = {q["num"] for q in questoes}
    nums_card = set(gabarito.keys())

    # (1) Cobertura cruzada
    so_card = nums_card - nums_etapa2
    so_etapa2 = nums_etapa2 - nums_card
    if so_card:
        erros.append(f"  x Q no tema-card mas ausentes em etapa2.typ: {sorted(so_card)}")
    if so_etapa2:
        erros.append(f"  x Q em etapa2.typ mas sem gabarito no tema-card: {sorted(so_etapa2)}")

    # (2)-(4) Validação por questão
    for q in questoes:
        num = q["num"]
        gab = gabarito.get(num)
        if gab is None:
            continue  # já reportado acima
        if q["tipo"] == "mc":
            letras_validas = {l for l, _ in q["alts"]}
            if gab not in letras_validas:
                erros.append(
                    f"  x Q{num} (MC): gabarito declarado '{gab}' não existe nas alternativas "
                    f"({sorted(letras_validas)})"
                )
                continue
            # Texto da correta
            correta_txt = next((t for l, t in q["alts"] if l == gab), "")
            n_words = len(correta_txt.split())
            if n_words < 4:
                erros.append(
                    f"  x Q{num} (MC): alternativa correta '{gab}' tem só {n_words} palavras "
                    f"— provável placeholder ou erro de parsing"
                )
            elif n_words < 8:
                warnings.append(
                    f"  ! Q{num} (MC): correta '{gab}' tem {n_words} palavras (curta demais "
                    f"para Aplicação; verificar se carrega mecanismo didático)"
                )
        elif q["tipo"] == "ce":
            n_itens = len(q["alts"])
            if not re.fullmatch(r"[CE]+", gab):
                erros.append(
                    f"  x Q{num} (CE): gabarito '{gab}' deve ser combinação de C/E "
                    f"(ex.: CCEC). Encontrado: '{gab}'"
                )
                continue
            if len(gab) != n_itens:
                erros.append(
                    f"  x Q{num} (CE): gabarito '{gab}' tem {len(gab)} letras mas "
                    f"a questão tem {n_itens} itens (esperado {n_itens} letras)"
                )

    # (6) Distribuição do gabarito (apenas MC com letras isoladas)
    letras_mc = [g for q in questoes if q["tipo"] == "mc"
                 and (g := gabarito.get(q["num"])) and g in "ABCDE"]
    if letras_mc:
        dist = Counter(letras_mc)
        total = len(letras_mc)
        for letra, n in dist.items():
            if n / total > 0.45:
                warnings.append(
                    f"  ! Distribuição do gabarito MC: letra '{letra}' em {n}/{total} "
                    f"({100*n/total:.0f}%) — possível sorteio falho (>45%). "
                    f"Reembaralhar."
                )
        # Sequências monótonas
        for i in range(len(letras_mc) - 4):
            seq = letras_mc[i:i+5]
            if len(set(seq)) == 1:
                warnings.append(
                    f"  ! Distribuição do gabarito MC: 5 letras '{seq[0]}' consecutivas "
                    f"em torno de Q{questoes[i]['num']} — provavelmente sorteio falho"
                )
                break

    return erros, warnings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", nargs="?", help="Slug do tema (infere paths)")
    parser.add_argument("--tema-card", help="Path do YAML do tema card")
    parser.add_argument("--etapa2", help="Path de etapa2.typ")
    args = parser.parse_args()

    if args.slug:
        tema_card_path = TEMA_CARDS_DIR / f"tema_card_{args.slug}.yml"
        etapa2_path = BUILD_DIR / "etapa2.typ"
    elif args.tema_card and args.etapa2:
        tema_card_path = Path(args.tema_card)
        etapa2_path = Path(args.etapa2)
    else:
        parser.print_help()
        return 1

    print(f"=== NEBLI verificar_gabarito_resumo ===")
    print(f"Tema card: {tema_card_path}")
    print(f"Etapa 2:   {etapa2_path}")
    print()

    questoes, e1 = parse_etapa2(etapa2_path)
    gabarito, e2 = parse_tema_card(tema_card_path)
    if e1 or e2:
        for m in e1 + e2:
            print(m)
        return 1

    print(f"Questões em etapa2.typ: {len(questoes)} "
          f"(MC: {sum(1 for q in questoes if q['tipo']=='mc')}, "
          f"CE: {sum(1 for q in questoes if q['tipo']=='ce')})")
    print(f"Itens no gabarito: {len(gabarito)}")
    print()

    erros, warnings = validate(questoes, gabarito)
    if erros:
        print("ERROS:")
        for m in erros:
            print(m)
    if warnings:
        print("AVISOS:")
        for m in warnings:
            print(m)
    print()
    if erros:
        print(f"x FALHA — {len(erros)} erro(s) bloqueante(s)")
        return 1
    print(f"v OK — gabarito consistente com etapa2.typ ({len(warnings)} aviso(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
