"""Seleciona a camada ativa da UC07 a partir do corpus real da disciplina.

O acervo integral do Kenhub continua instalado. Este módulo só decide quais
cards ficam ativos para estudo de longo prazo e exige uma evidência textual
por nota. A escrita de suspensão passa exclusivamente por nebli.decks.

Uso:
    python -m nebli.kenhub.seleciona_estudo planejar
    python -m nebli.kenhub.seleciona_estudo conferir
    python -m nebli.kenhub.seleciona_estudo aplicar
"""
from __future__ import annotations

import argparse
import collections
import glob
import html
import json
import math
import re
import unicodedata
from pathlib import Path

from nebli.decks import Anki, apply, em_tela
from nebli.preflight import chunks

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "arquivos-trabalho" / "uc07-selecao-longo-prazo-2026-10-20"
SNAPSHOT = RUN / "anki-antes.json"
MANIFEST = RUN / "selecao.json"
REPORT = RUN / "RELATORIO.md"

STOP = {
    "a", "ao", "aos", "as", "com", "como", "da", "das", "de", "do", "dos", "e", "em", "entre",
    "essa", "esse", "esta", "este", "foi", "mais", "na", "nas", "no", "nos", "o", "os", "ou",
    "para", "pela", "pelo", "por", "qual", "que", "se", "sem", "sua", "suas", "um", "uma",
    "the", "of", "and", "is", "to", "in", "which", "what", "are", "from", "with", "its",
    "estrutura", "estruturas", "indica", "chamado", "chamada", "regiao", "parte", "nivel",
}
PERIPHERAL_TARGETS = {
    "pulmao", "olho", "glandula lacrimal", "estomago", "figado", "vesicula biliar",
    "intestino delgado", "intestino grosso", "reto", "glandula adrenal", "bexiga",
}


def fold(s: str) -> str:
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"\1", s)
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).casefold()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def toks(s: str) -> list[str]:
    return [t for t in fold(s).split() if len(t) > 2 and t not in STOP and not t.isdigit()]


def chunks_corpus() -> list[dict]:
    out = []
    fontes = ROOT / "arquivos-trabalho" / "uc07-fontes-veteranos-2026-10-19"
    for path, prefix, marker in (
        (fontes / "apostila-guia-neuroanatomia-paginas.txt", "guia-veteranos", r"===== PÁGINA PDF (\d+) ====="),
        (fontes / "apostila-neuroanato-veteranos-ocr.txt", "resumo-veteranos", r"===== PÁGINA (\d+) ====="),
    ):
        text = path.read_text(encoding="utf-8")
        parts = re.split(marker, text)
        for i in range(1, len(parts), 2):
            body = parts[i + 1].strip()
            if body:
                out.append({"fonte": prefix, "ref": f"p.{parts[i]}", "texto": body})
    trans = ROOT / "aulas UC07" / "transcricoes"
    for path in sorted(trans.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        segs = data.get("segments", [])
        # Janelas de cerca de dois minutos preservam contexto e timestamp citável.
        for pos in range(0, len(segs), 24):
            group = segs[pos:pos + 24]
            if not group:
                continue
            start = int(group[0].get("start", 0)); mm, ss = divmod(start, 60)
            out.append({"fonte": "aula", "arquivo": path.stem, "ref": f"{mm:02d}:{ss:02d}",
                        "texto": " ".join(s.get("text", "") for s in group)})
    if not out:
        raise SystemExit("Corpus vazio")
    for c in out:
        c["tokens"] = collections.Counter(toks(c["texto"]))
        c["normalizado"] = fold(c["texto"])
    return out


def receipts() -> tuple[dict[int, dict], dict[int, list[str]]]:
    meta, decks = {}, collections.defaultdict(list)
    for raw in glob.glob(str(ROOT / "arquivos-trabalho" / "uc07-kenhub-*" / "receipt.json")):
        d = json.loads(Path(raw).read_text(encoding="utf-8"))
        for n in d["notas"]:
            meta.setdefault(int(n["nid"]), n)
            decks[int(n["nid"])].append(d["deck"])
    return meta, decks


def note_text(n: dict) -> str:
    f = n["fields"]
    for key in ("Nome PT", "Text", "Header"):
        if key in f and fold(f[key]["value"]):
            base = f[key]["value"]
            break
    else:
        base = next(iter(f.values()))["value"]
    extra = f.get("Extra", {}).get("value", "")
    return f"{base} {extra}"


def best_evidence(query: str, corpus: list[dict], df: collections.Counter, n_docs: int) -> tuple[float, dict]:
    q = collections.Counter(toks(query))
    if not q:
        return 0.0, {}
    # Termos raros do próprio card importam mais; palavras genéricas não fabricam relação.
    weights = {t: math.log(1 + n_docs / (1 + df[t])) for t in q}
    denom = sum(weights.values()) or 1
    best = (0.0, {})
    phrase = fold(query)
    for c in corpus:
        common = sum(w for t, w in weights.items() if t in c["tokens"])
        coverage = common / denom
        exact = bool(len(phrase) >= 8 and phrase in c["normalizado"])
        score = min(1.0, coverage + (0.22 if exact else 0.0))
        if score > best[0]:
            best = (score, c)
    return best


def classify(n: dict, r: dict, score: float, ev: dict) -> tuple[bool, str]:
    tags = n["tags"]
    model = n["modelName"]
    kind = r.get("tipo", "acervo")
    color = r.get("cor", "azul")
    hy = next((t.split("::")[-1] for t in tags if "HighYield" in t), "")
    lecture = ev.get("fonte") == "aula"

    if fold(note_text(n)) in PERIPHERAL_TARGETS and model == "NEBLI Kenhub IO v1":
        return False, "órgão-alvo periférico; função autonômica mantida sem decorar cada órgão"

    if model == "NEBLI Kenhub IO v1":
        threshold = {"verde": 0.34, "azul": 0.52, "rosa": 0.72}[color]
        selected = score >= threshold
        reason = "estrutura ensinada" if selected else "estrutura secundária/reserva"
    elif kind in {"anking", "anking_io", "acervo", "netter"} or hy:
        top_hy = hy in {"1-HighYield", "2-RelativelyHighYield", "3-HighYield-temporary"}
        threshold = 0.42 if top_hy else 0.66
        selected = score >= threshold and (top_hy or lecture or score >= 0.78)
        reason = "Step/AnKing HY do assunto exato" if selected and top_hy else "complemento de acervo exato" if selected else "complemento lateral/reserva"
    else:
        threshold = 0.62 if color != "rosa" else 0.80
        selected = score >= threshold
        reason = "fato ensinado nas fontes" if selected else "detalhe/redundância de quiz em reserva"
    return selected, reason


def plan() -> dict:
    RUN.mkdir(parents=True, exist_ok=True)
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    corpus = chunks_corpus()
    df = collections.Counter(t for c in corpus for t in c["tokens"])
    rec, decks = receipts()
    cards_by_note = collections.defaultdict(list)
    for c in snap["cards"]:
        cards_by_note[int(c["note"])].append(int(c["cardId"]))
    rows = []
    for n in snap["notes"]:
        nid = int(n["noteId"]); r = rec.get(nid, {})
        text = note_text(n)
        score, ev = best_evidence(text, corpus, df, len(corpus))
        selected, reason = classify(n, r, score, ev)
        snippet = re.sub(r"\s+", " ", ev.get("texto", "")).strip()[:420]
        rows.append({
            "nid": nid, "card_ids": sorted(cards_by_note[nid]), "selecionado": selected,
            "tipo": r.get("tipo", "acervo"), "cor": r.get("cor", ""), "texto": re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text))).strip()[:500],
            "motivo": reason, "score": round(score, 3), "fonte": ev.get("fonte", ""),
            "referencia": " · ".join(x for x in (ev.get("arquivo", ""), ev.get("ref", "")) if x),
            "trecho": snippet, "decks": sorted(set(decks.get(nid, []))),
            "estrutura": next((t.split("::", 2)[2] for t in n["tags"] if t.startswith("NEBLI::estrutura::")), ""),
            "hy": next((t.split("::")[-1] for t in n["tags"] if "HighYield" in t), ""),
        })
    # Núcleos numéricos perdem sinal no casamento lexical. Curadoria explícita:
    # áreas corticais canônicas e marcos clínicos de dermátomos/miótomos, sem
    # transformar as duas unidades em uma enumeração exaustiva.
    core_brodmann = {1, 2, 3, 4, 6, 8, 17, 22, 41, 42, 44, 45}
    core_segment_patterns = (
        "area de pele com inervacao", "conjunto de musculos esqueleticos", "c4 ombros", "c6 polegar",
        "t4 mamilo", "t10 umbigo", "l1 ligamento inguinal", "l4 patelas", "l5 halux",
        "s1 dedo minimo", "s2 s3 s4", "c5 produz abducao", "c6 produz supinacao",
        "c7 produzem extensao", "t1 produz aducao", "l2 e l3 produzem a flexao",
        "l3 e l4 produzem a extensao", "dorsiflexao do tornozelo", "flexao plantar do pe",
    )
    for row in rows:
        deck_text = " ".join(row["decks"])
        clean = fold(row["texto"])
        if "Áreas de Brodmann" in deck_text:
            nums = {int(x) for x in re.findall(r"\b(?:area )?(\d{1,2})\b", clean)}
            if nums & core_brodmann and row["score"] > 0:
                row["selecionado"] = True
                row["motivo"] = "área cortical canônica explicitamente resumida pelos veteranos"
        elif "Dermátomos e miótomos" in deck_text and row["score"] > 0:
            if any(p in clean for p in core_segment_patterns):
                row["selecionado"] = True
                row["motivo"] = "marco clínico de dermátomo/miótomo ensinado na aula ou no resumo"
    # Estrutura secundária não leva todos os irmãos. Mantém a melhor imagem e,
    # quando agrega, um complemento; pilares podem ter até dois complementos.
    grouped = collections.defaultdict(list)
    for row in rows:
        if row["selecionado"] and row["estrutura"]:
            grouped[row["estrutura"]].append(row)
    hy_order = {"1-HighYield": 4, "2-RelativelyHighYield": 3, "3-HighYield-temporary": 2,
                "4-LowerYield": 1, "5-LowYield": 0}
    for group in grouped.values():
        color = next((r["cor"] for r in group if r["tipo"] == "kenhub"), group[0]["cor"])
        limit = {"verde": 3, "azul": 2, "rosa": 1}.get(color, 2)
        rank = lambda r: (r["tipo"] == "kenhub", hy_order.get(r["hy"], -1), r["score"])
        for row in sorted(group, key=rank, reverse=True)[limit:]:
            row["selecionado"] = False
            row["motivo"] = f"redundância de estrutura {color}; melhor card/complemento mantido"
    manifest = {"versao": 1, "feedback": "F-20261020-CODEX-02", "corpus_chunks": len(corpus), "notas": rows}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    write_report(manifest)
    return manifest


def write_report(m: dict) -> None:
    rows = m["notas"]; active = [r for r in rows if r["selecionado"]]
    by_type = collections.Counter(r["tipo"] for r in active)
    by_source = collections.Counter(r["fonte"] for r in active)
    by_hy = collections.Counter(r["hy"] for r in active if r["hy"])
    lines = ["# Seleção ativa UC07 — longo prazo", "", f"- Notas avaliadas: {len(rows)}",
             f"- Notas selecionadas: {len(active)}", f"- Cards selecionados: {sum(len(r['card_ids']) for r in active)}",
             f"- Reserva suspensa: {sum(len(r['card_ids']) for r in rows if not r['selecionado'])} cards",
             f"- Corpus: {m['corpus_chunks']} trechos citáveis", "",
             "## Selecionados por tipo", ""]
    lines += [f"- {k}: {v}" for k, v in sorted(by_type.items())]
    lines += ["", "## Evidência principal", ""] + [f"- {k}: {v}" for k, v in sorted(by_source.items())]
    lines += ["", "## Step/AnKing por prioridade", ""] + [f"- {k}: {v}" for k, v in sorted(by_hy.items())]
    lines += ["", "O JSON ao lado registra, por nota e card ID, decisão, fonte, página/timestamp, trecho e motivo.", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def gate(manifest: dict, live=False) -> dict:
    rows = manifest.get("notas", [])
    errors = []
    ids = [cid for r in rows for cid in r.get("card_ids", [])]
    if not rows or not ids:
        errors.append("manifesto vazio")
    if len(ids) != len(set(ids)):
        errors.append("card ID duplicado")
    for r in rows:
        if r.get("selecionado") and not all(r.get(k) for k in ("motivo", "fonte", "referencia", "trecho")):
            errors.append(f"selecionado sem evidência: {r.get('nid')}")
        if r.get("selecionado") and r.get("score", 0) <= 0:
            errors.append(f"selecionado sem correspondência: {r.get('nid')}")
    result = {"notas": len(rows), "cards": len(ids), "selecionados": sum(len(r["card_ids"]) for r in rows if r["selecionado"]), "erros": errors}
    if live and not errors:
        A = Anki(); selected = {cid for r in rows if r["selecionado"] for cid in r["card_ids"]}
        states = {}
        for b in chunks(ids, 500):
            states.update(zip(b, A("areSuspended", cards=b)))
        wrong_active = sorted(cid for cid in selected if states.get(cid) is not False)
        wrong_reserve = sorted(cid for cid in set(ids) - selected if states.get(cid) is not True)
        result.update(ativos_divergentes=wrong_active, reserva_divergente=wrong_reserve)
        if wrong_active or wrong_reserve:
            errors.append("estado vivo diverge do manifesto")
    if errors:
        raise SystemExit("GATE F-20261020-CODEX-02 REPROVADO: " + "; ".join(errors[:20]))
    return result


def execute(manifest: dict) -> None:
    gate(manifest)
    A = Anki()
    current = em_tela(A)
    selected = [cid for r in manifest["notas"] if r["selecionado"] and r["nid"] not in current for cid in r["card_ids"]]
    reserve = [cid for r in manifest["notas"] if not r["selecionado"] and r["nid"] not in current for cid in r["card_ids"]]
    to_unsuspend = [cid for cid, state in zip(selected, A("areSuspended", cards=selected)) if state is True]
    to_suspend = [cid for cid, state in zip(reserve, A("areSuspended", cards=reserve)) if state is False]
    records = []
    if to_suspend:
        path, rec = apply(A, to_suspend, True, "UC07 reserva pelo corpus 2026-10-20", ["NEBLI::UC07"], sync=False)
        records.append(str(path))
    if to_unsuspend:
        path, rec = apply(A, to_unsuspend, False, "UC07 guia ativo pelo corpus 2026-10-20", ["NEBLI::UC07"], sync=False)
        records.append(str(path))
    result = gate(manifest, live=True)
    (RUN / "aplicacao.json").write_text(json.dumps({"registros": records, "notas_em_tela_puladas": sorted(current), "gate": result}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("acao", choices=("planejar", "conferir", "aplicar")); args = p.parse_args()
    manifest = plan() if args.acao == "planejar" else json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.acao == "planejar":
        print(json.dumps(gate(manifest), ensure_ascii=False))
    elif args.acao == "conferir":
        print(json.dumps(gate(manifest, live=True), ensure_ascii=False))
    else:
        execute(manifest)


if __name__ == "__main__":
    main()
