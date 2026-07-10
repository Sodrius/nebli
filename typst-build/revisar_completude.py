#!/usr/bin/env python3
"""
revisar_completude.py — Tier 1 da rubrica de qualidade NEBLI
Critérios mecânicos/visuais (T1.1 a T1.8), sem LLM.
Canônico: arquivos-trabalho/rubrica-qualidade-didatica.md

Uso:
    python3 typst-build/revisar_completude.py <slug>
    python3 typst-build/revisar_completude.py gliconeogenese

Exit codes:
    0 — tudo ok
    1 — pelo menos 1 ERROR (bloqueia movimentação do PDF)
    2 — só warnings (passa, mas reporta)
"""
from __future__ import annotations
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIGLAS_ARMADILHA = [
    "NADH", "NAD⁺", "NADP⁺", "NADPH", "ADP", "Pi",
    "cAMP", "AMPc", "CoA", "FAD", "FADH₂", "GDP", "AMP",
]

class Report:
    def __init__(self):
        self.errors = []
        self.warns = []
        self.infos = []

    def err(self, cid, msg):
        self.errors.append((cid, msg))
        print(f"  x {cid}: {msg}", file=sys.stderr)

    def warn(self, cid, msg):
        self.warns.append((cid, msg))
        print(f"  ! {cid}: {msg}")

    def ok(self, cid, msg):
        print(f"  v {cid}: {msg}")

    def info(self, cid, msg):
        self.infos.append((cid, msg))
        print(f"  . {cid}: {msg}")

    def exit_code(self):
        if self.errors:
            return 1
        if self.warns:
            return 2
        return 0


def t1_1_figuras_existem(typ_text, report):
    """T1.1 — Toda figura citada existe no disco"""
    paths = re.findall(r'#figura-(?:nebli|lateral)\("([^"]+)"', typ_text)
    missing = []
    for p in paths:
        if p.startswith("/"):
            disk_path = ROOT / p.lstrip("/")
        else:
            disk_path = (ROOT / "typst-build" / p).resolve()
        if not disk_path.exists():
            missing.append(p)
    if missing:
        report.err("T1.1", f"figuras quebradas ({len(missing)}): {', '.join(missing[:3])}")
    else:
        report.ok("T1.1", f"{len(paths)} figuras, todas existem")


def t1_2_legendas_nao_vazias(typ_text, report):
    """T1.2 — Toda figura tem legenda não-vazia"""
    matches = re.findall(
        r'#figura-(?:nebli|lateral)\([^)]*legenda:\s*(\[[^\]]*\]|""|"[^"]*")',
        typ_text, re.DOTALL
    )
    empty = sum(1 for m in matches if m in ("[]", '""'))
    if empty:
        report.err("T1.2", f"{empty} figura(s) com legenda vazia")
    else:
        report.ok("T1.2", f"{len(matches)} figuras com legenda preenchida")


def t1_3_siglas_declaradas(typ_text, report):
    """T1.3 — Toda sigla usada no corpo tem #sigla() declarado"""
    # Quais armadilhas aparecem no corpo
    aparece_no_corpo = set()
    for sigla in SIGLAS_ARMADILHA:
        if sigla in typ_text:
            aparece_no_corpo.add(sigla)
    # Quais foram declaradas
    declaradas = set(re.findall(r'#sigla\("([^"]+)"', typ_text))
    # Faltantes = aparecem mas não declaradas
    faltantes = aparece_no_corpo - declaradas
    if faltantes:
        report.err("T1.3", f"siglas usadas sem #sigla() declarado: {', '.join(sorted(faltantes))}")
    else:
        report.ok("T1.3", f"todas {len(aparece_no_corpo)} siglas-armadilha estão declaradas")


def t1_4_mapa_confusoes_cobre(slug, typ_text, report):
    """T1.4 — Mapa-confusões cobre todos os subtópicos"""
    mapa_path = ROOT / "mapa-confusoes" / f"{slug}.md"
    if not mapa_path.exists():
        report.err("T1.4", f"mapa-confusoes/{slug}.md não existe")
        return
    mapa_text = mapa_path.read_text(encoding="utf-8")
    subtopicos = re.findall(r'#subtopico\("([^"]+)"', typ_text)
    nums_subt = [re.match(r'(\d+\.\d+)', s).group(1) for s in subtopicos if re.match(r'(\d+\.\d+)', s)]
    nums_mapa = re.findall(r'###\s+(\d+\.\d+)', mapa_text)
    nao_cobertos = [n for n in nums_subt if n not in nums_mapa]
    if nao_cobertos:
        report.err("T1.4", f"subtópicos sem cobertura no mapa: {', '.join(nao_cobertos)}")
    else:
        report.ok("T1.4", f"todos os {len(nums_subt)} subtópicos cobertos")


def t1_5_termo_notas(typ_text, report):
    """T1.5 — Termo-notas no alvo (6–8)"""
    n = len(re.findall(r'#termo-nota\[', typ_text))
    if n < 4 or n > 12:
        report.err("T1.5", f"{n} termo-notas (alvo 6–8, fora da faixa 4–12)")
    elif n < 6 or n > 8:
        report.warn("T1.5", f"{n} termo-notas (alvo 6–8, mas aceitável 4–10)")
    else:
        report.ok("T1.5", f"{n} termo-notas no alvo")


def t1_6_tabelas_alinhadas(typ_text, report):
    """T1.6 — Tabelas com número de células múltiplo do número de colunas"""
    desalinhadas = 0
    for m in re.finditer(r'#table\(\s*columns:\s*\(([^)]*)\)(.*?)\n\s*\)', typ_text, re.DOTALL):
        cols_decl = m.group(1)
        ncols = len([c for c in cols_decl.split(",") if c.strip()])
        body = m.group(2)
        ncells = len(re.findall(r'\[(?:[^\[\]]|\[[^\]]*\])*\]', body))
        if ncells == 0 or ncols == 0:
            continue
        if ncells % ncols != 0:
            desalinhadas += 1
    if desalinhadas:
        report.warn("T1.6", f"{desalinhadas} tabela(s) com células possivelmente desalinhadas (verificar manualmente)")
    else:
        report.ok("T1.6", "tabelas bem-formadas")


def t1_7_mindmap(typ_text, report):
    """T1.7 — Mindmap de fechamento presente e bem-formado"""
    if "#mindmap-fechamento(" not in typ_text:
        report.err("T1.7", "ausente — toda E1 deve ter #mindmap-fechamento antes do Resumindo")
        return
    estacoes = re.search(r'estacoes:\s*\((.*?)\),\s*(?:rodape|cartoes)', typ_text, re.DOTALL)
    cartoes = re.search(r'cartoes:\s*\((.*?)\),?\s*\)', typ_text, re.DOTALL)
    n_estacoes = estacoes.group(1).count("rotulo:") if estacoes else 0
    n_cartoes = cartoes.group(1).count("titulo:") if cartoes else 0
    if n_estacoes != 3 or n_cartoes != 3:
        report.err("T1.7", f"estacoes={n_estacoes}, cartoes={n_cartoes} (esperado 3+3)")
    else:
        report.ok("T1.7", "mindmap presente, 3 estações + 3 cartões")


def t1_8_negrito_balanceado(typ_text, report):
    """T1.8 — Marcadores de negrito balanceados em cada parágrafo"""
    # Remove diretivas, ficar só com texto de prosa
    paragrafos = re.split(r'\n\s*\n', typ_text)
    desbalanceados = 0
    exemplos = []
    for i, p in enumerate(paragrafos):
        # Pula linhas que começam com # (chamadas Typst)
        if p.lstrip().startswith("#"):
            continue
        # Conta * que não são parte de ** (markdown bold proibido)
        # Remove ** primeiro para não contar
        clean = p.replace("**", "")
        # Conta * remanescentes
        n_star = clean.count("*")
        if n_star % 2 != 0:
            desbalanceados += 1
            if len(exemplos) < 2:
                exemplos.append(p[:80].replace("\n", " "))
    if desbalanceados:
        report.err("T1.8", f"{desbalanceados} parágrafos com * desbalanceado. Ex: {' | '.join(exemplos)}")
    else:
        report.ok("T1.8", "todos os parágrafos com negrito balanceado")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="Slug do resumo (ex: gliconeogenese)")
    parser.add_argument("--etapa1", default=None, help="Caminho do etapa1.typ (default: typst-build/etapa1.typ)")
    args = parser.parse_args()

    etapa1_path = Path(args.etapa1) if args.etapa1 else ROOT / "typst-build" / "etapa1.typ"
    if not etapa1_path.exists():
        print(f"x etapa1.typ não encontrado: {etapa1_path}", file=sys.stderr)
        sys.exit(1)

    typ_text = etapa1_path.read_text(encoding="utf-8")
    print(f"=== NEBLI revisar_completude (Tier 1) — slug: {args.slug} ===")
    print(f"Arquivo: {etapa1_path}\n")

    report = Report()
    t1_1_figuras_existem(typ_text, report)
    t1_2_legendas_nao_vazias(typ_text, report)
    t1_3_siglas_declaradas(typ_text, report)
    t1_4_mapa_confusoes_cobre(args.slug, typ_text, report)
    t1_5_termo_notas(typ_text, report)
    t1_6_tabelas_alinhadas(typ_text, report)
    t1_7_mindmap(typ_text, report)
    t1_8_negrito_balanceado(typ_text, report)

    print(f"\nResumo: {len(report.errors)} erro(s), {len(report.warns)} warning(s)")
    code = report.exit_code()
    if code == 0:
        print("v Tier 1 OK — pode seguir para Tier 2.")
    elif code == 1:
        print("x Tier 1 FALHA — bloqueia movimentação do PDF.")
    else:
        print("! Tier 1 com warnings — passa mas Davi deve revisar.")
    sys.exit(code)


if __name__ == "__main__":
    main()
