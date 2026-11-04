"""Empacota a revisão semântica de autorais e verifica seu recibo, sem acessar Anki.

O módulo não decide se um card ensina bem. O revisor separado escreve o parecer;
este validador verifica cobertura, evidência literal e vínculo à versão revisada.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUBRICA = ROOT / "config/revisor-autorais.md"
SCHEMA_VERSION = 1
RUBRIC_VERSION = "2026-10-25.2"
INPUT = "revisor-autorais-entrada.json"
REPORT = "revisor-autorais-parecer.json"
CONTEXT = "revisor-autorais-contexto.json"
MAP = "revisor-autorais-mapa.json"
MIN_APROVACAO = 0.90  # F-20261028-CLAUDE-02
VERDICTS = {"aprovado", "revisar", "evidencia_insuficiente"}
FORBIDDEN_KEYS = {"comentario", "comentarios", "nebli_comentario", "nebli_resposta", "gostei", "likes", "x",
                  "label", "labels", "gold", "expected", "expected_verdict", "veredito", "feedback", "tags",
                  "noteid", "cardid", "note_id", "card_id", "nid", "source_nid", "origin", "origem",
                  "reps", "lapses", "suspended", "aprovado", "reprovado", "avaliacao_anterior"}
EVIDENCE_FILES = ("compreensao-aula.json", "mapa-de-profundidade.json", "motivacoes.json", "fontes-decl.json",
                  "busca/cobertura.tsv", "busca/semantica.jsonl", "busca/secoes.jsonl", "busca/anking.txt",
                  "busca/acervos.json", "busca/palavra-chave.jsonl", CONTEXT)


def sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode()).hexdigest()


def _read(path, default=None):
    if not path.exists():
        return copy.deepcopy(default)
    return json.loads(path.read_text(encoding="utf-8"))


def _fields(value):
    return {str(k): (v.get("value", "") if isinstance(v, dict) else v)
            for k, v in (value or {}).items()}


def _clean(value):
    """Remove rótulos e IDs de estruturas; textos científicos não são reescritos."""
    if isinstance(value, dict):
        return {k: _clean(v) for k, v in value.items() if k.casefold() not in FORBIDDEN_KEYS
                and not k.casefold().startswith(("coment", "feedback", "expected_", "gold_"))}
    if isinstance(value, list):
        return [_clean(x) for x in value]
    return value


def _content_fields(value):
    fields = _fields(value)
    return {k: fields[k] for k in ("Text", "Front", "Extra", "Back", "Back Extra", "Imagem", "Imagem Verso", "Nome PT")
            if k in fields}


def _is_author(entry):
    return (str(entry.get("origin", entry.get("origem", ""))).casefold() == "autoral"
            or str(entry.get("kind", "")).casefold() == "autoral"
            or "NEBLI::origem::Autoral" in entry.get("tags", []))


def _all_entries(plan, context):
    entries = []
    issues = []
    overrides = context.get("cards", {})
    for e in plan.get("entries", []):
        if not isinstance(e, dict) or not e.get("key"):
            issues.append("entrada sem chave")
            continue
        enriched = {**e, **overrides.get(e["key"], {})}
        if e.get("fields"):
            enriched["fields"] = e["fields"]
        # A origem do sidecar nunca pode esconder autoria declarada no plano.
        if _is_author(e):
            enriched["origin"] = "Autoral"
        if not enriched.get("origin") and not enriched.get("origem") and not _is_author(enriched):
            issues.append(f"{e['key']}: origem da entrada não declarada")
        entries.append(enriched)
    for nid, raw in (plan.get("compartilhados") or {}).items():
        key = f"sh-{nid}"
        e = {**raw, **overrides.get(key, {}), "key": key}
        if _is_author(raw):
            e["origin"] = "Autoral"
        if not e.get("origin") and not e.get("origem") and not e.get("source_nid"):
            issues.append(f"{key}: origem do compartilhado não materializada; não presumir acervo")
        if _is_author(e) and not _content_fields(e.get("fields")):
            issues.append(f"{key}: autoral compartilhado sem campos materializados")
        entries.append(e)
    keys = [x["key"] for x in entries]
    if len(keys) != len(set(keys)):
        issues.append("chaves de cards duplicadas")
    if not entries:
        issues.append("plano vazio")
    return entries, issues


def _rubric():
    text = RUBRICA.read_text(encoding="utf-8")
    if not re.search(rf"(?m)^Rubrica: {re.escape(RUBRIC_VERSION)}\s*$", text):
        raise ValueError("versão da rubrica inválida ou ausente")
    return hashlib.sha256(text.encode()).hexdigest()


def _support(run):
    manifest = {}
    for name in EVIDENCE_FILES:
        p = run / name
        if p.is_file():
            manifest[name] = hashlib.sha256(p.read_bytes()).hexdigest()
    # Alteração nos resultados efetivos invalida recibos mesmo com manifesto igual.
    for p in sorted((run / "busca/secoes").glob("*.txt")):
        manifest[str(p.relative_to(run))] = hashlib.sha256(p.read_bytes()).hexdigest()
    def paths(value):
        if isinstance(value, dict):
            for k, v in value.items():
                if k in ("arquivo", "texto", "transcricao") and isinstance(v, str):
                    yield v
                else:
                    yield from paths(v)
        elif isinstance(value, list):
            for v in value:
                yield from paths(v)
    for name in (CONTEXT, "fontes-decl.json"):
        for relative in paths(_read(run / name, {})):
            p = (run / relative).resolve()
            # External resources require frozen excerpts in the context, never
            # arbitrary filesystem reads driven by untrusted card text.
            if p.is_relative_to(run.resolve()):
                manifest[relative] = hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else "AUSENTE"
    return manifest


def preparar(run, plan=None, blind=False, write=True):
    """Retorna pacote atual, opcionalmente gravando pacote + mapa privado.

    Fontes devem conter trechos suficientes para julgamento. Falta de trecho não é
    inventada pelo empacotador: fica explícita e impede aprovação integral.
    """
    run = Path(run)
    plan = plan if plan is not None else _read(run / "plan.json", {})
    context = _read(run / CONTEXT, {})
    if not isinstance(context, dict) or not isinstance(context.get("cards", {}), dict):
        raise ValueError("contexto inválido")
    entries, issues = _all_entries(plan, context)
    ordered = sorted(entries, key=lambda e: (e.get("order", 0), e["key"]))
    motives = _read(run / "motivacoes.json", {}).get("motivacoes", [])
    comprehension = _read(run / "compreensao-aula.json", {})
    rubric_hash = _rubric()
    cases, mapping = [], {}
    evidence = _support(run)
    for index, entry in enumerate(ordered):
        if not _is_author(entry):
            continue
        key = entry["key"]
        # An ID cannot expose the target, source deck, original note ID or label.
        case_id = "A-" + hashlib.sha256(key.encode()).hexdigest()[:16]
        mapping[case_id] = key
        fields = _content_fields(entry.get("fields"))
        motive = entry.get("motivacao", "")
        if isinstance(motive, str):
            motive = next((m for m in motives if m.get("id") == motive), {"necessidade": motive})
        # Source references and prior judgments never become reviewer labels.
        motive = {k: v for k, v in motive.items() if k in ("reconstruir", "por_que_dura", "necessidade")}
        neighbors = []
        for n in ordered[max(0, index-1):index] + ordered[index+1:index+2]:
            neighbors.append({"fields": _content_fields(n.get("fields")), "bloco": n.get("bloco", "")})
        body = {
            "fields": fields,
            "clozes": [{"indice": int(i), "conteudo": text} for i, text in re.findall(
                r"\{\{c(\d+)::(.*?)\}\}", str(fields.get("Text", "")), re.S)],
            "contexto": _clean(entry.get("contexto") or {
                "aula": comprehension.get("o_que_a_aula_ensina", ""),
                "bloco": entry.get("bloco", ""), "objetivo": entry.get("alvo", ""),
                "localizador": entry.get("evid", "")}),
            "vizinhos": neighbors,
            "motivacao": _clean(motive),
            "restricoes_locais": _clean(entry.get("restricoes_locais") or entry.get("organizacao_preferencia_davi") or {}),
            "fontes": _clean(entry.get("fontes", [])),
            "busca": _clean(entry.get("busca", "")),
        }
        missing = []
        if not (fields.get("Text") or fields.get("Front")):
            missing.append("frente")
        if not body["motivacao"] or not any(body["motivacao"].values()):
            missing.append("motivacao")
        if not body["fontes"] or not all(isinstance(x, dict) and isinstance(x.get("trecho"), str)
                                         and x["trecho"].strip() and isinstance(x.get("localizador"), str)
                                         and x["localizador"].strip()
                                         for x in body["fontes"]):
            missing.append("fontes_com_trecho_e_localizador")
        if not body["busca"]:
            missing.append("busca")
        if not any(s.strip() for s in _strings(body["contexto"])):
            missing.append("contexto")
        body["evidencia_ausente"] = missing
        fingerprint = sha({"conteudo": body, "rubrica_sha256": rubric_hash, "suporte_sha256": evidence})
        cases.append({"case_id": case_id, "input_sha256": fingerprint, **body})
    package = {"schema_version": SCHEMA_VERSION, "rubrica_versao": RUBRIC_VERSION,
               "rubrica_sha256": rubric_hash, "modo": "cego" if blind else "producao",
               "total_plano": len(entries), "total_autorais": len(cases), "problemas_preparacao": issues,
               "cards": cases}
    # Raw local paths/IDs live only in a private map, including in blind mode.
    package["pacote_sha256"] = sha(package)
    if write:
        run.mkdir(parents=True, exist_ok=True)
        (run / INPUT).write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (run / MAP).write_text(json.dumps({"ids": mapping, "suporte_sha256": evidence}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return package


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v)


def _quoted(quote, case):
    content = {k: v for k, v in case.items() if k not in ("case_id", "input_sha256", "evidencia_ausente")}
    return isinstance(quote, str) and bool(quote.strip()) and any(quote in s for s in _strings(content))


def verificar(run, plan=None):
    """Formato de gate existente: lista de pares (descrição, aprovado).

    Aprovar estrutura/recibo não prova qualidade; o julgamento pertence ao revisor
    identificado e deve ser auditado com testes cegos fora desta função.
    """
    run = Path(run)
    label = "[duro] revisão independente de TODOS os autorais, vinculada ao conteúdo e à rubrica atuais"
    try:
        previous = _read(run / INPUT, {})
        if not isinstance(previous, dict):
            raise ValueError("pacote inválido")
        current = preparar(run, plan, blind=previous.get("modo") == "cego", write=False)
        report = _read(run / REPORT, {})
        if not isinstance(report, dict):
            raise ValueError("parecer inválido")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        return [(label + f": {exc}", False)]
    issues = list(current["problemas_preparacao"])
    if not current["cards"] and not issues:
        return [(label + ": plano não vazio, sem autorais identificados (não se aplica)", True)]
    if previous != current:
        issues.append("pacote ausente ou desatualizado; preparar novamente")
    if report.get("schema_version") != SCHEMA_VERSION:
        issues.append("schema do parecer inválido")
    if report.get("rubrica_sha256") != current["rubrica_sha256"]:
        issues.append("parecer de outra rubrica")
    if report.get("pacote_sha256") != current["pacote_sha256"]:
        issues.append("parecer de outro pacote")
    reviewer = report.get("revisor", {})
    if not isinstance(reviewer, dict) or not all(isinstance(reviewer.get(k), str) and reviewer[k].strip()
                                               for k in ("identidade", "execucao", "concluido_em")):
        issues.append("identificação da execução independente ausente")
    if report.get("independente_do_autor") is not True:
        issues.append("revisão não declarada independente do autor")
    reviews = report.get("cards", [])
    if not isinstance(reviews, list) or any(not isinstance(x, dict) for x in reviews):
        issues.append("cards do parecer inválidos")
        reviews = []
    if any(not isinstance(x.get("case_id"), str) for x in reviews):
        issues.append("case_id precisa ser texto")
        reviews = [x for x in reviews if isinstance(x.get("case_id"), str)]
    ids = [x.get("case_id") for x in reviews]
    expected = {x["case_id"] for x in current["cards"]}
    if not reviews or set(ids) != expected or len(ids) != len(set(ids)):
        issues.append("parecer vazio, incompleto, com IDs extras ou duplicados")
    by_id = {x.get("case_id"): x for x in reviews}
    nao_aprovados = []
    for case in current["cards"]:
        cid = case["case_id"]
        result = by_id.get(cid, {})
        if result.get("input_sha256") != case["input_sha256"]:
            issues.append(f"{cid}: hash de conteúdo divergente")
        verdict = result.get("veredito")
        if verdict not in VERDICTS:
            issues.append(f"{cid}: veredito inválido")
        elif verdict != "aprovado":
            nao_aprovados.append(f"{cid}: {verdict}")
        if case["evidencia_ausente"] and verdict == "aprovado":
            issues.append(f"{cid}: aprovou apesar de evidência ausente {case['evidencia_ausente']}")
        for field in ("alvo", "ambiguidade_alternativa", "ganho", "encaixe", "justificativa_formato", "teste_reconstrucao"):
            if not isinstance(result.get(field), str) or not result[field].strip():
                issues.append(f"{cid}: falta julgamento {field}")
        evidence = result.get("evidencias", [])
        if not isinstance(evidence, list) or not evidence:
            issues.append(f"{cid}: sem evidências literais")
        else:
            for e in evidence:
                if not isinstance(e, dict) or not _quoted(e.get("trecho"), case) or not e.get("analise"):
                    issues.append(f"{cid}: evidência não corresponde ao pacote ou não foi analisada")
        problems = result.get("problemas")
        if not isinstance(problems, list):
            issues.append(f"{cid}: lista de problemas ausente")
        elif verdict == "aprovado" and problems:
            issues.append(f"{cid}: aprovado com problemas pendentes")
        elif verdict in ("revisar", "evidencia_insuficiente") and not problems:
            issues.append(f"{cid}: reprovação sem motivo")
        elif problems:
            for p in problems:
                if not isinstance(p, dict) or not all(p.get(k) for k in ("criterio", "motivo", "acao")):
                    issues.append(f"{cid}: problema sem critério, motivo ou ação")
                elif p.get("trecho") and not _quoted(p["trecho"], case):
                    issues.append(f"{cid}: trecho do problema não existe no pacote")
    # F-20261028-CLAUDE-02 (Davi, 28/10): "o revisor tem que aprovar 90%": o gate exige 90% dos autorais aprovados; os demais ficam
    # registrados (revisar/evidencia_insuficiente com problema acionável) e o executor os julga na segunda leitura.
    total = max(1, len(expected))
    if (total - len(nao_aprovados)) / total < MIN_APROVACAO:
        issues.append(f"aprovação {(total - len(nao_aprovados)) / total:.0%} < {MIN_APROVACAO:.0%}: " + "; ".join(nao_aprovados[:6]))
    elif nao_aprovados:
        label += f" ({len(nao_aprovados)} de {total} não aprovados, dentro de {1 - MIN_APROVACAO:.0%}: " + "; ".join(nao_aprovados) + ")"
    # A reserva de 25/10 ainda não sustenta uso autônomo: segunda leitura do executor.
    if int((plan or {}).get("pipeline_versao") or 1) >= 9:
        supervision = _read(run / "revisao-executor-autorais.json", {})
        if not isinstance(supervision, dict) or supervision.get("pacote_sha256") != current["pacote_sha256"]:
            issues.append("falta revisão do executor vinculada ao pacote atual; revisor ainda não é aprovador autônomo")
        else:
            results = supervision.get("cards", [])
            if not isinstance(results, list): results = []
            valid = {r.get("case_id"): r for r in results if isinstance(r, dict)}
            if set(valid) != expected or len(valid) != len(results):
                issues.append("revisão do executor incompleta/duplicada")
            for case in current["cards"]:
                result = valid.get(case["case_id"], {})
                if (result.get("input_sha256") != case["input_sha256"] or result.get("veredito") != "aprovado"
                        or not result.get("julgamento") or not _quoted(result.get("trecho"), case)):
                    issues.append(f"{case['case_id']}: revisão do executor sem conclusão/evidência atual")
    return [(label + (": " + "; ".join(issues[:10]) if issues else f": {len(expected)} pareceres válidos"), not issues)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("acao", choices=("preparar", "verificar"))
    parser.add_argument("corrida", type=Path)
    parser.add_argument("--cego", action="store_true")
    args = parser.parse_args(argv)
    if args.acao == "preparar":
        p = preparar(args.corrida, blind=args.cego)
        print(json.dumps({"arquivo": str(args.corrida / INPUT), "autorais": p["total_autorais"],
                          "problemas": p["problemas_preparacao"], "pacote_sha256": p["pacote_sha256"]}, ensure_ascii=False))
        return 1 if p["problemas_preparacao"] else 0
    checks = verificar(args.corrida)
    for message, ok in checks:
        print(("OK " if ok else "FALHA ") + message)
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
