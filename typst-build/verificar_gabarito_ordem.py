"""
verificar_gabarito_ordem.py — Verifica integridade do gabarito (versão 2).

Pós-mudança canônica 2026-05-24 (numeração sequencial):
  Cada caderno usa IDs sequenciais 1..N na ordem em que questões aparecem
  no corpo. O gabarito também mostra 1..N.

Verificações:
  1. CORREÇÃO: para cada (seq, resposta) no gabarito do PDF, a resposta
     bate com o gabarito-do-banco da questão correspondente?
  2. ORDEM: o gabarito enumera os IDs em ordem crescente 1, 2, 3, ...?
  3. COMPLETUDE: todas as objetivas têm entrada no gabarito?

Repete a mesma lógica de seleção/ordenação que gerar_caderno.py usa,
para reconstituir o mapeamento seq → questao_banco.
"""
from __future__ import annotations
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
BANCO = ROOT / "banco"
QUESTOES_DIR = BANCO / "questoes"

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)

DISCIPLINA_ORDEM = ["Bioquímica", "Biologia Celular", "Fisiologia",
                    "Biologia Molecular", "Outras"]


def load_question(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = FRONT_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    fm["_file"] = path.name
    return fm


def load_cronograma(uc: str) -> dict:
    uc_num = int(uc.replace("UC", "").lstrip("0") or "1")
    yaml_path = BANCO / f"aulas_uc{uc_num:02d}.yml"
    if not yaml_path.exists():
        yaml_path = BANCO / f"aulas_uc{uc_num}.yml"
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    return {a["slug"]: a for a in data.get("aulas", [])}


def coletar_questoes(uc: str, prova: str, cronograma: dict) -> list:
    out = []
    for p in sorted(QUESTOES_DIR.glob("q-*.md")):
        q = load_question(p)
        if not q:
            continue
        if str(q.get("uc_origem", "")).strip() != uc:
            continue
        aula = str(q.get("aula", "")).strip()
        if prova == "HISTORICO":
            if aula and aula not in cronograma:
                out.append(q)
        else:
            if aula and aula in cronograma and cronograma[aula]["prova"] == prova:
                out.append(q)
    return out


def ordenar_disciplinas(ds):
    return sorted(ds, key=lambda d: DISCIPLINA_ORDEM.index(d)
                  if d in DISCIPLINA_ORDEM else 999)


def ordenar_aulas(slugs, cronograma):
    return sorted(slugs, key=lambda s: cronograma.get(s, {}).get("ordem", 9999))


def ordenar_questoes(qs):
    def ano(q):
        try:
            return -int(str(q.get("ano", "0") or "0"))
        except ValueError:
            return 0
    def qid(q):
        m = re.search(r"\d+", str(q.get("id", "0")))
        return int(m.group(0)) if m else 0
    return sorted(qs, key=lambda q: (ano(q), qid(q)))


def reconstituir_mapeamento(uc: str, prova: str) -> list:
    """Repete a mesma lógica de gerar_caderno.py para mapear seq → questão."""
    cronograma = load_cronograma(uc)
    todas = coletar_questoes(uc, prova, cronograma)
    objetivas = [q for q in todas if str(q.get("formato", "")).upper() in {"MC", "CE"}]
    discursivas = [q for q in todas if str(q.get("formato", "")).upper() in {"DISCURSIVA", "DISC"}]

    grupos = defaultdict(lambda: defaultdict(list))
    for q in objetivas:
        aula = str(q.get("aula", "")).strip()
        disc = cronograma.get(aula, {}).get("disciplina", "Outras")
        grupos[disc][aula].append(q)

    # Mesma pré-passada do gerar_caderno
    ordem_obj = []
    seq = 1
    for disciplina in ordenar_disciplinas(grupos.keys()):
        for slug in ordenar_aulas(grupos[disciplina].keys(), cronograma):
            for q in ordenar_questoes(grupos[disciplina][slug]):
                q["_seq"] = seq
                ordem_obj.append(q)
                seq += 1
    for q in discursivas:
        q["_seq"] = seq
        seq += 1
    return ordem_obj  # só objetivas


def extrair_gabarito(text: str) -> list[tuple[str, str]]:
    """Pega seção GABARITO e retorna lista de (id_str, resposta) na ordem.

    Estratégia line-by-line:
    - Linha tipo "1 E 2 D 3 B 4 C 5 D": pega pares (num, letra)
    - Linha tipo "23 A-F; B-V; C-F; D-F; E-V": pega num + resto
    """
    m = re.search(r"GABARITO\s*\n+(.*)", text, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    sec = m.group(1)
    # Marker class: letra A-Z/a-z, numeral romano I/II/III/IV/V/VI..., ou
    # dígito 1..99. Cobre CE com markers fora de [A-E] (q-0179 usa I..IV;
    # q-0337 usa a..i).
    MARKER = r"(?:[A-Za-z]|[IVXivx]{1,5}|\d{1,2})"
    long_re = re.compile(
        rf"^(\d{{1,5}})\s+({MARKER}\s*-\s*[VFvf](?:\s*;\s*{MARKER}\s*-\s*[VFvf])+)\s*$"
    )
    out = []
    for raw_line in sec.split("\n"):
        line = raw_line.strip()
        if not line:
            continue
        # Linha "longa" (CE): começa com num + espaço + marker-V/F (...; marker-V/F)+
        m_long = long_re.match(line)
        if m_long:
            out.append((m_long.group(1), re.sub(r"\s+", " ", m_long.group(2)).upper()))
            continue
        # Linha "curta" multi-pares: extrai todos pares (num, letra)
        for m_pair in re.finditer(r"(\d{1,5})\s+([A-Ea-e])(?=\s|$)", line):
            out.append((m_pair.group(1), m_pair.group(2).upper()))
    return out


def verificar(pdf_path: Path, uc: str, prova: str) -> dict:
    pdf = PdfReader(str(pdf_path))
    text = "\n".join(p.extract_text() or "" for p in pdf.pages)

    ordem_objetivas_banco = reconstituir_mapeamento(uc, prova)
    gabarito_pdf = extrair_gabarito(text)

    erros = []
    n_obj = len(ordem_objetivas_banco)
    n_gab = len(gabarito_pdf)

    # 1. Contagem deve bater
    if n_obj != n_gab:
        erros.append(f"contagem divergente: {n_obj} objetivas esperadas, "
                     f"{n_gab} entradas no gabarito do PDF")

    # 2. Ordem deve ser 1..N
    for i, (qid_pdf, _) in enumerate(gabarito_pdf):
        esperado = str(i + 1)
        if qid_pdf != esperado:
            erros.append(f"posição {i+1}: gabarito ID='{qid_pdf}' (esperado '{esperado}')")
            if sum(1 for e in erros if e.startswith("posição")) > 5:
                erros.append("...")
                break

    # 3. Cada (seq, resposta) bate com banco
    for i, (qid_pdf, resp_pdf) in enumerate(gabarito_pdf):
        if i >= len(ordem_objetivas_banco):
            break
        q_banco = ordem_objetivas_banco[i]
        resp_banco = str(q_banco.get("gabarito", "")).strip().upper().replace(" ", "")
        resp_pdf_norm = resp_pdf.upper().replace(" ", "")
        if resp_banco != resp_pdf_norm:
            erros.append(
                f"posição {i+1} (id banco {q_banco['_file']}, "
                f"id orig={q_banco.get('id')}): PDF='{resp_pdf}' vs banco='{resp_banco}'")

    return {
        "arquivo": pdf_path.name,
        "n_objetivas_esperadas": n_obj,
        "n_no_gabarito": n_gab,
        "erros": erros,
    }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--apenas", help="restringe a um único PDF (nome do arquivo, ex: CADERNO-UC01-P1.pdf)")
    args = ap.parse_args()

    cadernos = [
        ("CADERNO-UC01-P1.pdf", "UC1", "P1"),
        ("CADERNO-UC01-P2.pdf", "UC1", "P2"),
        ("CADERNO-UC01-P3.pdf", "UC1", "P3"),
        ("CADERNO-UC01-HISTORICO.pdf", "UC1", "HISTORICO"),
        ("CADERNO-UC02-P1.pdf", "UC2", "P1"),
        ("CADERNO-UC02-P2.pdf", "UC2", "P2"),
        ("CADERNO-UC02-P3.pdf", "UC2", "P3"),
        ("CADERNO-UC02-HISTORICO.pdf", "UC2", "HISTORICO"),
    ]
    if args.apenas:
        cadernos = [c for c in cadernos if c[0] == args.apenas]
        if not cadernos:
            print(f"--apenas: nenhum caderno conhecido com nome '{args.apenas}'")
            sys.exit(2)

    out_lines = ["# Verificação de gabarito (numeração sequencial v2)\n"]
    has_problema = False

    for fname, uc, prova in cadernos:
        path = ROOT / "resumos-gerados" / fname
        if not path.exists():
            continue
        r = verificar(path, uc, prova)
        out_lines.append(f"## {fname}")
        out_lines.append(f"- Objetivas esperadas no gabarito: {r['n_objetivas_esperadas']}")
        out_lines.append(f"- Entradas no gabarito do PDF: {r['n_no_gabarito']}")
        if r["erros"]:
            has_problema = True
            out_lines.append(f"\n### ❌ Problemas ({len(r['erros'])})")
            for e in r["erros"]:
                out_lines.append(f"- {e}")
        else:
            out_lines.append("- ✅ Gabarito **correto e em ordem**")
        out_lines.append("")
        marca = "[OK]" if not r["erros"] else f"[{len(r['erros'])} erros]"
        print(f"{fname}: {r['n_no_gabarito']}/{r['n_objetivas_esperadas']} {marca}")

    if args.apenas:
        stem = Path(args.apenas).stem
        out_path = ROOT / "arquivos-trabalho" / f"verificacao-gabarito-{stem}.md"
    else:
        out_path = ROOT / "arquivos-trabalho" / "verificacao-gabarito-ordem.md"
    out_path.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"\nRelatorio: {out_path}")
    sys.exit(2 if has_problema else 0)


if __name__ == "__main__":
    main()
