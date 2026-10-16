"""Aplica no Anki a diferença entre o plan.json novo e o recibo de uma aula já instalada (troca de notas, ordem e fila).

    python3 -m nebli.delta arquivos-trabalho/<corrida> [--recibo receipt-antes.json] [--desde <ISO do início, para retomar>]

Generaliza o update3.py da BT03 (03/10). Nota que sai do plano ou cuja chave mudou de texto é apagada e recriada, mas só
se nenhum card tiver revisão, bandeira fora das cores ou comentário em NEBLI_Comentario; senão para sem apagar nada.
A faixa de `due` da aula vem do dicionário BASE do apply.py da corrida. Tudo vai para journal.jsonl; recibo novo no fim.

Correções feitas no Anki vivo (comentários de Davi, levas de 08/10) ficam em `<corrida>/correcoes-vivas.json`
(`nebli.reconcilia`) e prevalecem sobre o plano em qualquer rebuild. Campo vivo diferente do plano e não reconciliado
interrompe a delta antes de escrever: regravar o plano traria de volta imagem/formulação já rejeitada.
"""
from __future__ import annotations

import argparse
import ast
import base64
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from nebli.decks import Anki, escrita



def set_due(A, card, due):
    """Fila de novos na ordem dos slides. AnkiConnect recente recusa `due` ("protected state"): então vale a ordem de criação das notas, que já segue os slides (14/10)."""
    try:
        A("setSpecificValueOfCard", card=card, keys=["due"], newValues=[due], warning_check=True)
    except RuntimeError as err:
        if "Close the affected editor" in str(err):  # 16/10: nota aberta no editor do Anki (Browser de Davi): pular a ordem só dela
            print(f"  ordem não gravada no card {card}: editor aberto (reposicionar depois)")
            return
        if "protected state" not in str(err): raise

def set_flag(A, card, flag):
    """16/10: nota aberta no editor do Anki recusa escrita; pular só ela e avisar (rodar a delta de novo depois)."""
    try:
        A("setSpecificValueOfCard", card=card, keys=["flags"], newValues=[flag], warning_check=True)
    except RuntimeError as err:
        if "Close the affected editor" not in str(err): raise
        print(f"  bandeira não gravada no card {card}: editor aberto (rodar a delta de novo depois)")
        PULADOS.append(card)


PULADOS = []


def base_of(run, short):
    src = (run / "apply.py").read_text()
    m = re.search(r"BASE = (\{[^}]*\})", src)
    if m:
        return ast.literal_eval(m.group(1))[short]
    m = re.search(r'newValues=\[(\d+) \+ e\["order"\]', src)  # apply.py antigo, faixa escrita direto
    if m:
        return int(m.group(1))
    faixas = json.loads((Path(__file__).resolve().parents[1] / "config" / "fila-novos.json").read_text())["faixas"]
    if short in faixas:  # corridas novas: faixa em config/fila-novos.json (F-20261010-CLAUDE-01)
        return faixas[short]
    return {"an01": 0}[short]  # AN01 foi a primeira aula: faixa 0 (MEMORY, BASE das corridas)


def same(a, b):
    """Igualdade de campo ignorando a normalização de HTML que o Anki faz ao gravar (/>, </div>, espaços)."""
    import html as _html  # 12/10: o Anki grava & como &amp; (e &nbsp;); entidade não é correção viva
    n = lambda x: re.sub(r"\s+|</[a-z0-9]+>|<div>|<br\s*/?>", "", re.sub(r"\s*/>", ">", _html.unescape(x or "").replace("\xa0", " ")))
    return n(a) == n(b)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("corrida"); ap.add_argument("--recibo", default="receipt.json"); ap.add_argument("--desde", default="")
    ap.add_argument("--substituir-estudada", action="append", default=[],
                    help="chave de nota já estudada que sai do plano: em vez de apagar, suspende, marca NEBLI::substituido e tira da aula (estudo preservado)")
    ap.add_argument("--sobrescrever-vivo", action="append", default=[], help="chave cujo campo vivo divergente pode ser regravado pelo plano (correção nova substitui a anterior)")
    ap.add_argument("--comentario-atendido", action="append", default=[], help="chave cuja nota tem comentário de Davi que esta troca atende (registrar em FEEDBACKS antes)")
    a = ap.parse_args(argv)
    run = Path(a.corrida)
    from nebli.gates import require_sources
    require_sources(run)
    A = Anki()
    plan = json.loads((run / "plan.json").read_text())
    from nebli.reconcilia import aplicar_correcoes, conflitos
    aplicar_correcoes(run, plan)
    old = json.loads((run / a.recibo).read_text())
    DECK, LESSON_TAG, SHORT = plan["deck"], f'NEBLI::{plan["lesson_id"]}', plan["short"]
    BASE = base_of(run, SHORT)
    nid = {n["key"]: n["nid"] for n in old["notes"]}
    old_flag = {(n["key"], v["ord"]): v["flag"] for n in old["notes"] for v in n.get("cards", {}).values()}
    jpath = run / "journal.jsonl"
    if a.desde and jpath.exists():  # retomada: o que esta delta já criou/apagou
        for l in (json.loads(x) for x in jpath.read_text().splitlines() if x.strip()):
            if l.get("at", "") > a.desde and l["op"] == "addNote": nid[l["key"]] = l["nid"]
            if l.get("at", "") > a.desde and l["op"] == "deleteNotes": [nid.pop(k, None) for k in l["notas"]]
    if jpath.exists():  # execução anterior interrompida (sem delta-fim): reaproveita as notas que ela já criou
        ops = [json.loads(x) for x in jpath.read_text().splitlines() if x.strip()]
        last_end = max((i for i, l in enumerate(ops) if l["op"] == "delta-fim"), default=-1)
        last_start = max((i for i, l in enumerate(ops) if l["op"] == "delta-inicio"), default=-1)
        # 12/10: só uma DELTA interrompida (delta-inicio sem delta-fim depois) conta; os addNote do apply.py inicial não,
        # senão as notas retiradas por nebli.retira voltavam ao nid e eram apagadas
        if last_start > last_end:
            for l in ops[last_start + 1:]:
                if l["op"] == "addNote" and l["key"] not in nid: nid[l["key"]] = l["nid"]
    keys = {e["key"] for e in plan["entries"]}
    journal = jpath.open("a")

    def log(**k):
        k["at"] = datetime.now(timezone.utc).isoformat(); journal.write(json.dumps(k, ensure_ascii=False) + "\n"); journal.flush()

    ap_path = run / "plan-aplicado.json"
    aplicado = json.loads(ap_path.read_text()) if ap_path.exists() else None
    if aplicado: aplicar_correcoes(run, aplicado)
    conf = [c for c in conflitos(A, plan, nid, aplicado) if c[0] not in a.sobrescrever_vivo]
    if conf:
        raise SystemExit("Campos corrigidos no Anki e ausentes do plano (rode python3 -m nebli.reconcilia "
                         f"{run}):\n" + "\n".join(f"  {k} {f}" for k, f in conf[:40]))
    log(op="delta-inicio", plano=plan["selection_hash"])
    with escrita(A, f"{SHORT.upper()} delta {plan['run_id']}"):
        plan_text = {e["key"]: e["fields"].get("Text") for e in plan["entries"]}
        live = {n["noteId"]: n for n in A("notesInfo", notes=list(nid.values())) if n}
        nid = {k: v for k, v in nid.items() if v in live}
        cz = lambda t: sorted(set(re.findall(r"\{\{c(\d+)::", t or "")))
        # texto novo com outros clozes: apagar e recriar (os cards mudam); mesmos clozes: atualizar no lugar (estudo preservado)
        carry_keep_store = {}
        changed = {k: v for k, v in nid.items() if k in plan_text and "Text" in live[v]["fields"] and not same(live[v]["fields"]["Text"]["value"], plan_text[k])
                   and cz(live[v]["fields"]["Text"]["value"]) != cz(plan_text[k])}
        gone = {k: v for k, v in nid.items() if k not in keys and not any(t.startswith("NEBLI::retirado::") for t in live[v]["tags"])}  # retirada fica
        gone.update(changed)
        for k in changed: nid.pop(k)
        keep = {}
        for k, v in gone.items():
            cards = A("cardsInfo", cards=live[v]["cards"])
            comentado = live[v]["fields"].get("NEBLI_Comentario", {}).get("value") and k not in a.comentario_atendido
            studied = any(c["reps"] or c["flags"] not in (3, 4, 5) for c in cards)
            if studied and k in a.substituir_estudada and k not in changed:
                keep[k] = v; continue
            if studied or comentado:
                raise SystemExit(f"{k}: já estudado, marcado ou comentado; não apagar (use --substituir-estudada)")
        for k, v in keep.items():  # estudo preservado: a nota antiga fica suspensa fora da aula
            gone.pop(k)
            old_tags = [t for t in live[v]["tags"] if t.startswith(f"NEBLI::{plan['lesson_id']}") or t.startswith(f"NEBLI::ordem::{SHORT}-")]
            if old_tags: A("removeTags", notes=[v], tags=" ".join(old_tags))
            A("addTags", notes=[v], tags="NEBLI::substituido::delta"); A("suspend", cards=live[v]["cards"])
            c = live[v]["fields"].get("NEBLI_Comentario", {}).get("value", "")
            if c: carry_keep = carry_keep_store.setdefault(k, c)
            log(op="substituida-suspensa", key=k, nid=v)
        for k in gone: nid.pop(k, None)
        # F-15: comentário de Davi nunca se perde; vai para as notas que substituem a apagada (mesma chave ou recortes)
        carry = {k: live[v]["fields"].get("NEBLI_Comentario", {}).get("value", "") for k, v in gone.items()}
        carry = {k: c for k, c in carry.items() if c}
        carry.update(carry_keep_store)
        if carry: log(op="comentarios", de=carry)
        if gone:
            A("deleteNotes", notes=list(gone.values())); log(op="deleteNotes", notas=gone)
        for name, rel in plan.get("media", {}).items():
            data = base64.b64encode((run / rel).read_bytes()).decode()
            if A("retrieveMediaFile", filename=name) != data:
                A("storeMediaFile", filename=name, data=data); log(op="media", file=name)
        results = []
        for e in plan["entries"]:
            new_note = e["key"] not in nid
            if new_note:
                fields = dict(e["fields"])
                herd = [c for k, c in carry.items() if e["key"] == k or e["key"].startswith(k + "-")]
                if herd and "NEBLI_Comentario" in fields: fields["NEBLI_Comentario"] = "<br>".join(herd)
                e_nid = A("addNote", note={"deckName": DECK, "modelName": e["model"], "fields": fields, "tags": e["tags"] + (["NEBLI_comentario::pendente"] if herd else []), "options": {"allowDuplicate": True}})
                log(op="addNote", key=e["key"], nid=e_nid)
            else:
                e_nid = nid[e["key"]]
                ninfo = A("notesInfo", notes=[e_nid])[0]
                upd = {f: v for f, v in e["fields"].items() if f != "NEBLI_Comentario" and f in ninfo["fields"] and not same(ninfo["fields"][f]["value"], v)}
                if upd:
                    A("updateNoteFields", note={"id": e_nid, "fields": upd}); log(op="campos", key=e["key"], campos=sorted(upd))
                tags = ninfo["tags"]
                stale = [t for t in tags if t.startswith(f"NEBLI::ordem::{SHORT}-")]
                want = next(t for t in e["tags"] if t.startswith(f"NEBLI::ordem::{SHORT}-"))
                if stale != [want]:
                    if stale: A("removeTags", notes=[e_nid], tags=" ".join(stale))
                    A("addTags", notes=[e_nid], tags=want); log(op="ordem", key=e["key"], de=stale, para=want)
                cor_old = [t for t in tags if t.startswith(f"NEBLI::cor::{plan['lesson_id']}::") and t not in e["tags"]]
                if cor_old: A("removeTags", notes=[e_nid], tags=" ".join(cor_old))
                missing = [t for t in e["tags"] if t not in tags and not t.startswith(f"NEBLI::ordem::{SHORT}-")]
                if missing or cor_old:
                    A("addTags", notes=[e_nid], tags=" ".join(missing)); log(op="tags", key=e["key"], sai=cor_old, entra=missing)
            cards = A("cardsInfo", cards=A("findCards", query=f"nid:{e_nid}"))
            shared_note = any(t.startswith("NEBLI::compartilhado::") for t in A("notesInfo", notes=[e_nid])[0]["tags"])
            if sorted(c["ord"] for c in cards) != sorted(x["ord"] for x in e["cards"]): raise RuntimeError(f"{e['key']}: ords divergentes")
            for c in cards:
                flag = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                if new_note:
                    set_flag(A, c["cardId"], flag)
                elif (c["flags"] != flag and c["flags"] == old_flag.get((e["key"], c["ord"]))
                      and not (shared_note and c["flags"] in (3, 4, 5) and c["flags"] < flag)):  # cor recalibrada; marca de Davi e cor maior de compartilhado ficam
                    set_flag(A, c["cardId"], flag)
                    log(op="cor", key=e["key"], ord=c["ord"], de=c["flags"], para=flag)
                if c["type"] == 0:
                    set_due(A, c["cardId"], BASE + e["order"] * 10 + c["ord"])
            results.append({"key": e["key"], "nid": e_nid})
        for n, sdata in plan.get("compartilhados", {}).items():
            tags = A("notesInfo", notes=[int(n)])[0]["tags"]
            stale = [t for t in tags if t.startswith(f"NEBLI::ordem::{SHORT}-")]
            if stale != [sdata["ordem_tag"]]:
                if stale: A("removeTags", notes=[int(n)], tags=" ".join(stale))
                A("addTags", notes=[int(n)], tags=sdata["ordem_tag"]); log(op="ordem-compartilhado", nid=n, para=sdata["ordem_tag"])
            # compartilhado novo na delta (11/10): associar como o apply faz — tag da aula, marca de compartilhado e cor desta aula
            lesson = plan["lesson_id"]
            want = [f"NEBLI::{lesson}", f"NEBLI::compartilhado::{SHORT}", f"NEBLI::cor::{lesson}::{sdata['cor']}"]
            missing = [t for t in want if t not in tags]
            if missing:
                A("addTags", notes=[int(n)], tags=" ".join(missing)); log(op="associa-compartilhado", nid=n, tags=missing)
                rank, flag = {3: 3, 4: 2, 5: 1, 0: 0}, {"verde": 3, "azul": 4, "rosa": 5}[sdata["cor"]]
                for c in A("cardsInfo", cards=A("notesInfo", notes=[int(n)])[0]["cards"]):
                    if c["flags"] in (0, 3, 4, 5) and rank[flag] > rank[c["flags"]]:  # bandeira sobe só para cor maior; marca de Davi fica
                        set_flag(A, c["cardId"], flag)
        problems, suspended = [], []
        for r, e in zip(results, plan["entries"]):
            n = A("notesInfo", notes=[r["nid"]])[0]
            if set(e["tags"]) - set(n["tags"]): problems.append(f"tags {e['key']}")  # tags de outra aula (compartilhado) são esperadas
            ci = A("cardsInfo", cards=n["cards"])
            for c in ci:
                want = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                shared = any(t.startswith("NEBLI::compartilhado::") for t in n["tags"])
                if c["flags"] != want and not (shared and c["flags"] in (3, 4, 5) and c["flags"] < want):  # compartilhado: vale a maior cor
                    problems.append(f"flag {e['key']}")
                # due não é mais conferido: AnkiConnect recente recusa escrevê-lo (14/10); a ordem vem da criação e da tag de ordem
                if c["queue"] == -1: suspended.append(e["key"])  # suspensão é marca de Davi, não erro
            r["cards"] = {str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in ci}
        flags = [c["flag"] for r in results for c in r["cards"].values()]
        rec = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": DECK, "notes": results, "apagadas": gone,
               "cards_tag_aula": len(A("findCards", query=f'"tag:{LESSON_TAG}"')), "cards_new_lesson": len(flags), "expected": plan["totais"]["cards"],
               "green": flags.count(3), "blue": flags.count(4), "pink": flags.count(5), "problems": problems, "suspensos_por_davi": sorted(set(suspended)), "at": datetime.now(timezone.utc).isoformat()}
        (run / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        if not problems: (run / "plan-aplicado.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
        log(op="delta-fim", cards=len(flags), problemas=len(problems))
        print(json.dumps({k: rec[k] for k in ("cards_new_lesson", "expected", "green", "blue", "pink", "cards_tag_aula", "problems")}, ensure_ascii=False))
        if problems or rec["cards_new_lesson"] != rec["expected"]: raise SystemExit("Readback divergente")


if __name__ == "__main__":
    main()
