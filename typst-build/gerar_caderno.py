"""
gerar_caderno.py — Gera o .typ de um caderno de questões.

Filtra questões por UC + prova (slug + cronograma vigente), agrupa
por aula/disciplina, separa objetivas de discursivas, emite Typst
pronto para compilar.

Comando de compilação:
  cd typst-build/_cadernos
  typst compile --root ../.. --font-path ../../fonts caderno-XXX.typ caderno-XXX.pdf

Uso:
  python typst-build/gerar_caderno.py --uc UC1 --prova P1
  python typst-build/gerar_caderno.py --uc UC1 --prova HISTORICO
"""

from __future__ import annotations
import argparse
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BANCO = ROOT / "banco"
QUESTOES = BANCO / "questoes"
OUT_DIR = ROOT / "typst-build" / "_cadernos"

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)

DISCIPLINA_ORDEM = ["Bioquímica", "Biologia Celular", "Fisiologia",
                    "Biologia Molecular", "Outras"]

DESCRICAO_DEFAULT = {
    "Bioquímica": "Questões sobre estrutura e função de biomoléculas, metabolismo energético e regulação enzimática.",
    "Biologia Celular": "Questões sobre organelas, citoesqueleto, membranas e tráfego intracelular.",
    "Fisiologia": "Questões sobre transporte transmembrana, excitabilidade celular e sinalização.",
    "Biologia Molecular": "Questões sobre ácidos nucleicos, replicação, transcrição, tradução e regulação gênica.",
    "Outras": "Questões adicionais.",
}


# ============================== escapes Typst ==============================

def typst_escape(text: str) -> str:
    """Escapa caracteres especiais do Typst markup.

    Em ordem (importante!): \\ primeiro, depois os outros.
    Mantém Unicode intacto.
    """
    if not text:
        return ""
    # ordem: backslash primeiro pra não duplicar escapes posteriores
    text = text.replace("\\", "\\\\")
    # Caracteres que Typst trata como sigil em markup:
    for ch in ["#", "$", "@", "<", ">", "[", "]"]:
        text = text.replace(ch, "\\" + ch)
    # Asterisco e underscore: escapa se isolados (evita virar bold/sub)
    # Markdown bold ** vira typst * (que é bold em typst)
    # Detecta **xxx** e converte para *xxx*
    text = re.sub(r"\*\*([^*\n]+?)\*\*", r"*\1*", text)
    # Asteriscos isolados que sobraram (ex: nomes científicos) — escapa
    # mas só fora de pares de bold já marcados. Heurística: escapa se
    # vier de início/fim de palavra solto.
    # Para simplificar e ser seguro, escapamos `*` solitário (sem par).
    # Pega ocorrências que não estão entre pares casados:
    # estratégia: contar — se número total ímpar, escapar todas.
    if text.count("*") % 2 == 1:
        text = text.replace("*", "\\*")
    # underscore: escapa quando seguido/precedido de letra (subscript Typst)
    text = re.sub(r"(?<=\w)_(?=\w)", r"\\_", text)
    # underscore depois de ] (bracket escapado) — armadilha CHEATSHEET #7
    text = re.sub(r"(?<=\])_", r"\\_", text)
    return text


_TABLE_SEP_RE = re.compile(r"^\|?[\s\-:|]+\|?$")


def _is_md_table(p: str) -> bool:
    """Detecta bloco markdown table: 2+ linhas com '|', linha 2 é separadora."""
    lines = [ln for ln in p.splitlines() if ln.strip()]
    if len(lines) < 2:
        return False
    sep = lines[1].strip()
    if not (_TABLE_SEP_RE.fullmatch(sep) and "-" in sep):
        return False
    return "|" in lines[0]


def _md_table_to_typst(p: str) -> str:
    """Converte bloco markdown table em #table() Typst. Header em negrito."""
    rows_raw = []
    for ln in p.splitlines():
        s = ln.strip()
        if not s:
            continue
        if _TABLE_SEP_RE.fullmatch(s) and "-" in s:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        rows_raw.append(cells)
    if not rows_raw:
        return ""
    n_cols = max(len(r) for r in rows_raw)
    for r in rows_raw:
        while len(r) < n_cols:
            r.append("")
    parts = [
        "#table(",
        f"  columns: {n_cols},",
        "  inset: 6pt,",
        "  align: left + horizon,",
        "  stroke: 0.5pt + rgb(\"#CCCCCC\"),",
    ]
    header = rows_raw[0]
    for c in header:
        parts.append(f"  [*{typst_escape(c)}*],")
    for r in rows_raw[1:]:
        for c in r:
            parts.append(f"  [{typst_escape(c)}],")
    parts.append(")")
    return "\n".join(parts)


def markdown_to_typst(text: str) -> str:
    """Converte markdown simples do banco para markup Typst com escapes.

    Detecta blocos markdown table e converte para #table() Typst nativo;
    demais parágrafos passam pelo escape padrão.
    """
    if not text:
        return ""
    text = text.strip()
    # Parágrafos: preserva \n\n como separador.
    paragraphs = re.split(r"\n\s*\n", text)
    out_paras = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if _is_md_table(p):
            out_paras.append(_md_table_to_typst(p))
            continue
        # quebras de linha simples dentro do parágrafo viram espaço
        p = re.sub(r"\n+", " ", p)
        out_paras.append(typst_escape(p))
    # parágrafos separados por linha em branco (Typst entende como par break)
    return "\n\n".join(out_paras)


def typst_content(text: str) -> str:
    """Envelopa em [..] e converte markdown."""
    return "[" + markdown_to_typst(text) + "]"


def typst_string(s) -> str:
    """String literal Typst (entre aspas)."""
    if s is None:
        s = ""
    s = str(s).replace("\\", "\\\\").replace("\"", "\\\"")
    return "\"" + s + "\""


# ============================== parsing .md ==============================

def load_question(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = FRONT_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    fm["_body"] = m.group(2)
    fm["_file"] = path.name
    return fm


def section(body: str, name: str) -> str:
    pat = rf"##\s*{name}\s*\n(.*?)(?=\n##\s|\Z)"
    m = re.search(pat, body, re.DOTALL | re.IGNORECASE)
    return (m.group(1).strip() if m else "").strip()


def parse_alternativas(body: str) -> list[tuple[str, str]]:
    sec = section(body, "Alternativas")
    if not sec:
        return []
    pattern = re.compile(r"^\(?([A-Ea-e])\)\s+(.*?)(?=^\(?[A-Ea-e]\)|\Z)",
                         re.MULTILINE | re.DOTALL)
    return [(m.group(1).upper(), m.group(2).strip()) for m in pattern.finditer(sec)]


def parse_ce_itens(body: str) -> list[tuple[str, str]]:
    sec = section(body, "Alternativas")
    if not sec:
        sec = section(body, "Enunciado")
    pattern = re.compile(
        r"^\s*(?:\(?([A-Ia-i]|[IVX]+|\d+)\)?\.?\s*-?\s+)(.*?)"
        r"(?=^\s*(?:\(?(?:[A-Ia-i]|[IVX]+|\d+)\)?\.?\s*-?\s+)|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    out = []
    for m in pattern.finditer(sec):
        marker = m.group(1)
        if marker.isalpha():
            marker = marker.upper()
        texto = m.group(2).strip()
        if texto:
            out.append((marker, texto))
    return out


# ============================== cronograma + coleta ==============================

def load_cronograma(uc: str) -> dict[str, dict]:
    uc_num = int(uc.replace("UC", "").lstrip("0") or "1")
    yaml_path = BANCO / f"aulas_uc{uc_num:02d}.yml"
    if not yaml_path.exists():
        yaml_path = BANCO / f"aulas_uc{uc_num}.yml"
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    return {a["slug"]: a for a in data.get("aulas", [])}


def coletar_questoes(uc: str, prova_alvo: str, cronograma: dict) -> list[dict]:
    out = []
    for path in sorted(QUESTOES.glob("q-*.md")):
        q = load_question(path)
        if not q:
            continue
        if str(q.get("uc_origem", "")).strip() != uc:
            continue
        aula = str(q.get("aula", "")).strip()
        if prova_alvo == "HISTORICO":
            if aula and aula not in cronograma:
                out.append(q)
            continue
        if not aula or aula not in cronograma:
            continue
        if cronograma[aula]["prova"] != prova_alvo:
            continue
        out.append(q)
    return out


def agrupar(questoes: list[dict], cronograma: dict) -> dict:
    g = defaultdict(lambda: defaultdict(list))
    for q in questoes:
        aula = str(q.get("aula", "")).strip()
        disciplina = cronograma.get(aula, {}).get("disciplina", "Outras")
        g[disciplina][aula].append(q)
    return g


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


# ============================== emissão Typst ==============================

def emit_capa(prova, uc_label, total, periodo, blocos):
    blocos_str = ", ".join(typst_string(b) for b in blocos)
    return (
        f"#capa-caderno(\n"
        f"  prova: {typst_string(prova)},\n"
        f"  uc_label: {typst_string(uc_label)},\n"
        f"  total: {total},\n"
        f"  periodo: {typst_string(periodo)},\n"
        f"  blocos: ({blocos_str},),\n"
        f")\n"
    )


def emit_sumario(grupos, cronograma):
    lines = ["#sumario(("]
    for disciplina in ordenar_disciplinas(grupos.keys()):
        lines.append("  (")
        lines.append(f"    bloco: {typst_string(disciplina)},")
        lines.append("    aulas: (")
        for slug in ordenar_aulas(grupos[disciplina].keys(), cronograma):
            titulo = cronograma.get(slug, {}).get("titulo", slug)
            n = len(grupos[disciplina][slug])
            lines.append(f"      (titulo: {typst_string(titulo)}, n_questoes: {n}),")
        lines.append("    ),")
        lines.append("  ),")
    lines.append("))\n")
    return "\n".join(lines)


def emit_abertura(disciplina):
    desc = DESCRICAO_DEFAULT.get(disciplina, "Questões da disciplina.")
    return f"#abertura-bloco({typst_string(disciplina)}, {typst_string(desc)})\n"


def aula_label_curto(slug, cronograma):
    titulo = cronograma.get(slug, {}).get("titulo", slug)
    return titulo.split(":")[0][:40].strip()


def normaliza_qid(raw) -> str:
    """Converte 'q-0157' / '0157' / 157 -> '157' (string sem zeros à esquerda)."""
    s = str(raw)
    m = re.search(r"(\d+)", s)
    if not m:
        return s
    return str(int(m.group(1)))


def emit_figura_args(q) -> str:
    """Devolve os args Typst de figura (3 campos) a partir do frontmatter."""
    figura = str(q.get("figura", "") or "").strip()
    precisa = bool(q.get("precisa_figura", False))
    descricao = str(q.get("figura_descricao", "") or "").strip()
    args = []
    if figura:
        args.append(f"  figura: {typst_string(figura)},")
    if precisa:
        args.append(f"  precisa-figura: true,")
    if descricao:
        args.append(f"  figura-descricao: {typst_string(descricao)},")
    return ("\n" + "\n".join(args)) if args else ""


def _qid_display(q) -> str:
    """qid sequencial com asterisco prefixado quando a questão precisa de figura."""
    qid = str(q.get("_seq")) if "_seq" in q else normaliza_qid(q.get("id", "?"))
    if bool(q.get("precisa_figura", False)):
        qid = "*" + qid
    return qid


def emit_mc(q, prova, cronograma):
    # numeração sequencial dentro do caderno (resolve IDs duplicados do banco).
    # asterisco prefixado quando precisa_figura: true.
    qid = _qid_display(q)
    ano = str(q.get("ano") or "—")
    aula_label = aula_label_curto(str(q.get("aula", "")), cronograma)
    enunciado_raw = section(q["_body"], "Enunciado")
    alts = parse_alternativas(q["_body"])
    total_len = len(enunciado_raw) + sum(len(t) for _, t in alts)
    permite = "true" if total_len > 1600 else "false"

    alts_lines = []
    for letra, texto in alts:
        alts_lines.append(f"    ({typst_string(letra)}, {typst_content(texto)}),")
    alts_str = "\n".join(alts_lines)

    return (
        f"#questao-mc(\n"
        f"  id: {typst_string(qid)},\n"
        f"  prova: {typst_string(prova)},\n"
        f"  ano: {typst_string(ano)},\n"
        f"  aula: {typst_string(aula_label)},\n"
        f"  enunciado: {typst_content(enunciado_raw)},\n"
        f"  alternativas: (\n{alts_str}\n  ),"
        f"{emit_figura_args(q)}\n"
        f"  permite-quebra: {permite},\n"
        f")\n"
    )


def emit_ce(q, prova, cronograma):
    qid = _qid_display(q)
    ano = str(q.get("ano") or "—")
    aula_label = aula_label_curto(str(q.get("aula", "")), cronograma)
    enunciado_raw = section(q["_body"], "Enunciado")
    itens = parse_ce_itens(q["_body"])
    total_len = len(enunciado_raw) + sum(len(t) for _, t in itens)
    permite = "true" if total_len > 1600 else "false"

    itens_lines = []
    for marker, texto in itens:
        itens_lines.append(f"    ({typst_string(marker)}, {typst_content(texto)}),")
    itens_str = "\n".join(itens_lines)

    return (
        f"#questao-ce(\n"
        f"  id: {typst_string(qid)},\n"
        f"  prova: {typst_string(prova)},\n"
        f"  ano: {typst_string(ano)},\n"
        f"  aula: {typst_string(aula_label)},\n"
        f"  enunciado: {typst_content(enunciado_raw)},\n"
        f"  itens: (\n{itens_str}\n  ),"
        f"{emit_figura_args(q)}\n"
        f"  permite-quebra: {permite},\n"
        f")\n"
    )


def emit_discursivas(discursivas, prova, cronograma):
    if not discursivas:
        return ""
    lines = ["#secao-discursivas(("]
    for q in discursivas:
        qid = _qid_display(q)
        ano = str(q.get("ano") or "—")
        aula_label = aula_label_curto(str(q.get("aula", "")), cronograma)
        enunciado_raw = section(q["_body"], "Enunciado")
        permite = "true" if len(enunciado_raw) > 800 else "false"
        lines.append("  (")
        lines.append(f"    id: {typst_string(qid)},")
        lines.append(f"    prova: {typst_string(prova)},")
        lines.append(f"    ano: {typst_string(ano)},")
        lines.append(f"    aula: {typst_string(aula_label)},")
        lines.append(f"    enunciado: {typst_content(enunciado_raw)},")
        lines.append(f"    linhas: 12,")
        lines.append(f"    \"permite-quebra\": {permite},")
        # figura
        figura = str(q.get("figura", "") or "").strip()
        precisa = bool(q.get("precisa_figura", False))
        descricao = str(q.get("figura_descricao", "") or "").strip()
        if figura:
            lines.append(f"    figura: {typst_string(figura)},")
        if precisa:
            lines.append(f"    \"precisa-figura\": true,")
        if descricao:
            lines.append(f"    \"figura-descricao\": {typst_string(descricao)},")
        lines.append("  ),")
    lines.append("))\n")
    return "\n".join(lines)


def emit_gabarito(objetivas):
    if not objetivas:
        return ""
    tem_asterisco = any(bool(q.get("precisa_figura", False)) for q in objetivas)
    lines = ["#gabarito-consolidado(("]
    for q in objetivas:
        qid = _qid_display(q)
        gab = str(q.get("gabarito", "—"))
        lines.append(f"  (id: {typst_string(qid)}, resposta: {typst_string(gab)}),")
    lines.append("))\n")
    out = "\n".join(lines)
    if tem_asterisco:
        out += (
            "\n#v(1em)\n"
            "#text(size: 8pt, weight: \"light\", fill: rgb(\"#666666\"), "
            "style: \"italic\")[\\* questão depende de figura referenciada na "
            "prova original — consultar fonte para resolver.]\n"
        )
    return out


def emit_apendice(objetivas, prova, cronograma):
    if not objetivas:
        return ""
    lines = ["#apendice-explicacoes(("]
    for q in objetivas:
        qid = str(q.get("_seq")) if "_seq" in q else normaliza_qid(q.get("id", "?"))
        ano = str(q.get("ano") or "—")
        aula_label = aula_label_curto(str(q.get("aula", "")), cronograma)
        explicacao_raw = (section(q["_body"], "Explicação")
                          or section(q["_body"], "Explicacao")
                          or section(q["_body"], "Justificativa")
                          or "(sem explicação registrada no banco)")
        resumo = str(q.get("conceito_central", ""))[:200] or "—"
        armadilha = str(q.get("armadilha", "")) or "—"
        gabarito = str(q.get("gabarito", "—"))
        lines.append("  (")
        lines.append(f"    id: {typst_string(qid)},")
        lines.append(f"    prova: {typst_string(prova)},")
        lines.append(f"    ano: {typst_string(ano)},")
        lines.append(f"    aula: {typst_string(aula_label)},")
        lines.append(f"    resumo: {typst_string(resumo)},")
        lines.append(f"    armadilha: {typst_string(armadilha)},")
        lines.append(f"    explicacao: {typst_content(explicacao_raw)},")
        lines.append(f"    gabarito: {typst_string(gabarito)},")
        lines.append("  ),")
    lines.append("))\n")
    return "\n".join(lines)


# ============================== main ==============================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--uc", default="UC1")
    ap.add_argument("--prova", required=True, help="P1 | P2 | P3 | HISTORICO")
    args = ap.parse_args()

    cronograma = load_cronograma(args.uc)
    todas = coletar_questoes(args.uc, args.prova, cronograma)
    print(f"Coletadas {len(todas)} questões para {args.uc} · {args.prova}")

    objetivas = [q for q in todas if str(q.get("formato", "")).upper() in {"MC", "CE"}]
    discursivas = [q for q in todas if str(q.get("formato", "")).upper() in {"DISCURSIVA", "DISC"}]
    print(f"  Objetivas: {len(objetivas)}  Discursivas: {len(discursivas)}")

    grupos = agrupar(objetivas, cronograma)
    anos = sorted({str(q.get("ano", "")).strip() for q in todas if q.get("ano")})
    periodo = (f"{anos[0]}–{anos[-1]}" if len(anos) > 1 else
               (anos[0] if anos else "—"))
    blocos = ordenar_disciplinas(grupos.keys())
    uc_label = ("Unidade Curricular 01" if args.uc == "UC1"
                else f"Unidade Curricular {args.uc[2:].zfill(2)}")

    # ===== Pré-passada: numeração sequencial dentro do caderno =====
    # IDs do banco têm colisões (66 em UC1: q-0014.md e q-0016.md ambos têm
    # id: 14 etc). Solução adotada (Davi 2026-05-24): numerar 1..N na ordem
    # em que entram no caderno. Objetivas primeiro (na ordem do corpo),
    # depois discursivas (continua a sequência).
    seq = 1
    for disciplina in ordenar_disciplinas(grupos.keys()):
        for slug in ordenar_aulas(grupos[disciplina].keys(), cronograma):
            for q in ordenar_questoes(grupos[disciplina][slug]):
                q["_seq"] = seq
                seq += 1
    for q in discursivas:
        q["_seq"] = seq
        seq += 1
    # objetivas precisa estar ordenada pra emit_gabarito usar a mesma ordem
    # que vai aparecer no corpo
    objetivas_ordenadas = []
    for disciplina in ordenar_disciplinas(grupos.keys()):
        for slug in ordenar_aulas(grupos[disciplina].keys(), cronograma):
            for q in ordenar_questoes(grupos[disciplina][slug]):
                objetivas_ordenadas.append(q)
    objetivas = objetivas_ordenadas  # sobrescreve pra gabarito usar mesma ordem

    # Monta o documento
    partes = []
    partes.append('#import "/typst-template/caderno_v2_brutalista.typ": *\n')
    partes.append(f"#show: caderno-doc.with(\n"
                  f"  prova: {typst_string(args.prova)},\n"
                  f"  uc_label: {typst_string(uc_label)},\n"
                  f"  total: {len(todas)},\n"
                  f"  periodo: {typst_string(periodo)},\n"
                  f"  blocos: ({', '.join(typst_string(b) for b in blocos)},),\n"
                  f")\n")
    partes.append(emit_capa(args.prova, uc_label, len(todas), periodo, blocos))
    partes.append(emit_sumario(grupos, cronograma))

    for disciplina in ordenar_disciplinas(grupos.keys()):
        partes.append(emit_abertura(disciplina))
        for slug in ordenar_aulas(grupos[disciplina].keys(), cronograma):
            for q in ordenar_questoes(grupos[disciplina][slug]):
                formato = str(q.get("formato", "")).upper()
                if formato == "MC":
                    partes.append(emit_mc(q, args.prova, cronograma))
                elif formato == "CE":
                    partes.append(emit_ce(q, args.prova, cronograma))

    partes.append(emit_discursivas(discursivas, args.prova, cronograma))
    partes.append(emit_gabarito(objetivas))
    # Brutalista v2 não tem apêndice — gabarito é a última seção.
    # (apendice removido por decisão Davi 2026-05-24; emit_apendice
    # preservado no código pra reuso futuro se quisermos voltar).

    typ_final = "\n".join(partes)

    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"caderno-{args.uc.lower()}-{args.prova.lower()}.typ"
    out.write_text(typ_final, encoding="utf-8")
    print(f"Typst gravado: {out} ({len(typ_final):,} bytes)")


if __name__ == "__main__":
    main()
