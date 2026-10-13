"""Instala esta corrida em lotes retomáveis. --check faz somente leituras.

Não atualiza conteúdo de notas existentes nem presets; notas em revisão ficam
pendentes. Executar novamente retoma somente o que falta (sem recriar apagadas).
"""
import argparse
import base64
import hashlib
import json
import os
import re
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, LOCK, SYNC_PENDENTE, escrita
from nebli.gates import require_sources
from nebli.rotulos import canonical

canon = canonical


def now():
    return datetime.now(timezone.utc).isoformat()


def save(path, data):
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.flush()
        os.fsync(f.fileno())
    temp.replace(path)


def log(**record):
    record["at"] = now()
    with (HERE / "journal.jsonl").open("a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def current_note(A):
    # Falha de consulta não equivale a usuário ocioso: não escrever às cegas.
    try:
        card = A("guiCurrentCard")
    except RuntimeError as exc:
        if "Gui review is not currently active" in str(exc):
            return None
        raise
    if not card:
        return None
    nids = A("cardsToNotes", cards=[card["cardId"]])
    if len(nids) != 1:
        raise RuntimeError("Não foi possível identificar a nota em revisão")
    return int(nids[0])


class Deferred(Exception):
    pass


def mutate_note(A, nid, action, **params):
    if current_note(A) == nid:
        raise Deferred(str(nid))
    return A(action, **params)


@contextmanager
def batch_lock(A, label):
    # Outro executor pode manter o lock por alguns segundos. Não o remover.
    deadline = time.monotonic() + 60
    while LOCK.exists() and time.monotonic() < deadline:
        time.sleep(0.5)
    with escrita(A, label, sync=False):
        yield
    SYNC_PENDENTE.write_text(now())


def faixa(short):
    """Chamar exclusivamente dentro de escrita(), compartilhada com Claude."""
    path = HERE.parents[1] / "config" / "fila-novos.json"
    cfg = json.loads(path.read_text())
    if short not in cfg["faixas"]:
        cfg["faixas"][short] = max(cfg["faixas"].values(), default=0) + 20000
        save(path, cfg)
    return cfg["faixas"][short]


def note(A, nid):
    ns = A("notesInfo", notes=[nid])
    if len(ns) != 1 or not ns[0] or int(ns[0].get("noteId", -1)) != nid:
        raise RuntimeError(f"Nota {nid} ausente; não será recriada")
    return ns[0]


def snapshot(A, nids, label):
    """Backup dos campos/tags/IDs e estado dos cards que este lote pode tocar."""
    ns = [note(A, n) for n in sorted(set(nids))]
    cs = A("cardsInfo", cards=[c for n in ns for c in n["cards"]]) if ns else []
    path = HERE / "backups" / f"{time.time_ns()}-{label}.json"
    path.parent.mkdir(exist_ok=True)
    save(path, {"at": now(), "notes": ns, "cards": cs})
    log(op="backup-lote", path=str(path.relative_to(HERE)))


def identity(plan, key):
    token = hashlib.sha256(f"{plan['run_id']}:{key}".encode()).hexdigest()[:24]
    return f"NEBLI::instalacao::{token}"


def resolve(A, plan, entry, state):
    key = entry["key"]
    known = state["notes"].get(key, {}).get("nid")
    found = A("findNotes", query=f'"tag:{identity(plan, key)}"')
    if known is not None:
        note(A, int(known))  # Apagada depois da criação: nunca ressuscitar.
        if found and found != [known]:
            raise RuntimeError(f"Identidade duplicada: {key}, {found}")
        return int(known)
    if len(found) > 1:
        raise RuntimeError(f"Identidade duplicada: {key}, {found}")
    return int(found[0]) if found else None


def check_entry(A, plan, e, nid, initialized=False):
    n = note(A, nid)
    if n["modelName"] != e["model"]:
        raise RuntimeError(f"Modelo divergente: {e['key']}")
    for k, v in e["fields"].items():
        # Comentários e Tab posteriores pertencem à revisão do usuário/pipeline.
        if k in {"NEBLI_Comentario", "NEBLI_Tab"}:
            continue
        if n["fields"][k]["value"] != v:
            raise RuntimeError(f"Campo vivo alterado: {e['key']} / {k}; reconciliar")
    if not set(e["tags"]) <= set(n["tags"]):
        raise RuntimeError(f"Tags planejadas ausentes: {e['key']}; reconciliar")
    cs = A("cardsInfo", cards=n["cards"])
    if sorted(c["ord"] for c in cs) != sorted(c["ord"] for c in e["cards"]):
        raise RuntimeError(f"Irmãos divergentes: {e['key']}")
    if any(canon(c["deckName"]) != plan["deck"] for c in cs):
        raise RuntimeError(f"Nota movida: {e['key']}; não mover de volta")
    return cs


def prepare(A, plan):
    # Snapshot global só uma vez, antes da primeira escrita da corrida.
    before = HERE / "before.json"
    if not before.exists():
        ns = [note(A, int(n)) for n in plan["compartilhados"]]
        save(before, {"at": now(), "deck_names": A("deckNames"),
                      "compartilhados": {str(n["noteId"]): n for n in ns},
                      "cards": A("cardsInfo", cards=[c for n in ns for c in n["cards"]]),
                      "deck_config_nebli": A("getDeckConfig", deck="NEBLI")})
    for new, old in plan.get("clones", {}).items():
        if new not in A("modelNames"):
            templates = A("modelTemplates", modelName=old)
            fields = A("modelFieldNames", modelName=old)
            fields += [] if "NEBLI_Comentario" in fields else ["NEBLI_Comentario"]
            A("createModel", modelName=new, inOrderFields=fields,
              css=A("modelStyling", modelName=old)["css"],
              isCloze=any("{{cloze:" in t["Front"] for t in templates.values()),
              cardTemplates=[{"Name": k, **v} for k, v in templates.items()])
            if A("modelTemplates", modelName=new) != templates:
                raise RuntimeError(f"Templates do clone {new} divergem")
            log(op="createModel", model=new, clone_of=old)
    names = {canon(d) for d in A("deckNames")}
    chain = ["::".join(plan["deck"].split("::")[:i])
             for i in range(2, len(plan["deck"].split("::")) + 1)]
    new_decks = [d for d in chain if d not in names]
    if new_decks:
        A("createDeck", deck=plan["deck"])
        root_id = A("getDeckConfig", deck="NEBLI")["id"]
        A("setDeckConfigId", decks=new_decks, configId=root_id)
        if any(A("getDeckConfig", deck=d)["id"] != root_id for d in new_decks):
            raise RuntimeError("Configuração de deck novo divergente")
        log(op="createDeck", deck=plan["deck"], config_inherited_by=new_decks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--batch-size", type=int, default=5)
    args = parser.parse_args()
    if not 1 <= args.batch_size <= 10:
        parser.error("--batch-size deve ficar entre 1 e 10")
    require_sources(HERE)  # Antes de qualquer escrita, inclusive mídia/modelos.
    raw = (HERE / "plan.json").read_bytes()
    plan = json.loads(raw)
    digest = hashlib.sha256(raw).hexdigest()
    A = Anki()
    state_path = HERE / "apply-state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {
        "plan_sha256": digest, "selection_hash": plan["selection_hash"], "notes": {}, "shared": []}
    if state["plan_sha256"] != digest:
        raise SystemExit("Plano mudou desde o início da aplicação; reconciliar antes de continuar")
    # Reconcilia respostas perdidas de addNote e journal antigo sem duplicar.
    if (HERE / "journal.jsonl").exists():
        for line in (HERE / "journal.jsonl").read_text().splitlines():
            event = json.loads(line)
            if event.get("op") == "addNote":
                known = state["notes"].setdefault(event["key"], {"nid": event["nid"], "done": []})
                if known["nid"] != event["nid"]:
                    raise RuntimeError(f"Journal com identidades conflitantes: {event['key']}")
    keys = [e["key"] for e in plan["entries"]]
    if len(keys) != len(set(keys)) or set(state["notes"]) - set(keys):
        raise SystemExit("Chaves duplicadas/removidas; reconciliar")
    known_ids = set()
    for e in plan["entries"]:
        nid = resolve(A, plan, e, state)
        if nid is not None:
            check_entry(A, plan, e, nid)
            state["notes"].setdefault(e["key"], {"nid": nid, "done": []})
            known_ids.add(nid)
        if not e["cards"] or any(c["ord"] >= 10 for c in e["cards"]):
            raise RuntimeError(f"Fila inválida: {e['key']}")
    existing = set(A("findNotes", query=f'"tag:NEBLI::{plan["lesson_id"]}"'))
    if existing - known_ids - {int(n) for n in plan["compartilhados"]}:
        raise SystemExit("Notas de aula sem identidade reconciliada; não duplicar")
    for nid in plan["compartilhados"]:
        note(A, int(nid))
    current_note(A)
    for name, rel in plan["media"].items():
        data = (HERE / rel).read_bytes()
        got = A("retrieveMediaFile", filename=name)
        if got and base64.b64decode(got) != data:
            raise RuntimeError(f"Colisão de mídia: {name}; não sobrescrever")
    if args.check:
        print(json.dumps({"read_only": True, "entries": len(keys), "recovered": len(known_ids),
                          "shared": len(plan["compartilhados"])}))
        return 0

    with batch_lock(A, f"{plan['run_id']} preparar"):
        prepare(A, plan)
        base = faixa(plan["short"])
        save(state_path, state)
    # Mídia em lotes separados; não mantém lock durante toda a instalação.
    media = list(plan["media"].items())
    for offset in range(0, len(media), args.batch_size):
        with batch_lock(A, f"{plan['run_id']} mídia {offset}"):
            for name, rel in media[offset:offset + args.batch_size]:
                data = (HERE / rel).read_bytes()
                got = A("retrieveMediaFile", filename=name)
                if got and base64.b64decode(got) != data:
                    raise RuntimeError(f"Colisão de mídia concorrente: {name}")
                if not got:
                    A("storeMediaFile", filename=name, data=base64.b64encode(data).decode())
                    log(op="media", file=name)
                if base64.b64decode(A("retrieveMediaFile", filename=name)) != data:
                    raise RuntimeError(f"Readback de mídia: {name}")

    pending = []
    for offset in range(0, len(plan["entries"]), args.batch_size):
        entries = plan["entries"][offset:offset + args.batch_size]
        with batch_lock(A, f"{plan['run_id']} notas {offset}"):
            if hashlib.sha256((HERE / "plan.json").read_bytes()).hexdigest() != digest:
                raise RuntimeError("Plano alterado durante aplicação")
            snapshot(A, [state["notes"][e["key"]]["nid"] for e in entries if e["key"] in state["notes"]], f"notas-{offset}")
            for e in entries:
                key = e["key"]
                nid = resolve(A, plan, e, state)
                if nid is None:
                    # Nova nota não pode ser a nota atualmente em exibição.
                    current_note(A)
                    log(op="addNote-intent", key=key, identity=identity(plan, key), fields=e["fields"], tags=e["tags"])
                    nid = A("addNote", note={"deckName": plan["deck"], "modelName": e["model"],
                            "fields": e["fields"], "tags": list(dict.fromkeys(e["tags"] + [identity(plan, key)])),
                            "options": {"allowDuplicate": True}})
                    if not nid:
                        raise RuntimeError(f"addNote não retornou ID: {key}")
                    log(op="addNote", key=key, nid=nid)
                    state["notes"][key] = {"nid": nid, "done": []}
                    save(state_path, state)
                record = state["notes"][key]
                cs = check_entry(A, plan, e, nid)
                if record.get("verified"):
                    continue  # Preserva marcas/suspensão/agendamento posteriores.
                try:
                    for c in cs:
                        wanted = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                        for field, value in (("flags", wanted), ("due", base + e["order"] * 10 + c["ord"])):
                            operation = f"{c['cardId']}:{field}"
                            if operation in record["done"]:
                                continue
                            live = A("cardsInfo", cards=[c["cardId"]])[0]
                            if field == "flags" and live[field] not in (0, wanted):
                                raise RuntimeError(f"Marca pessoal durante inicialização: {key}; preservar/reconciliar")
                            if field == "due" and (live["type"] != 0 or live["queue"] != 0):
                                # Já estudado/suspenso: preservar estado, não restaurar fila.
                                log(op="preservar-fila", key=key, card=c["cardId"], type=live["type"], queue=live["queue"])
                            elif live[field] != value:
                                mutate_note(A, nid, "setSpecificValueOfCard", card=c["cardId"], keys=[field], newValues=[value], warning_check=True)
                                read = A("cardsInfo", cards=[c["cardId"]])[0]
                                if read[field] != value:
                                    raise RuntimeError(f"Readback {key} {field} divergente")
                                log(op="set-card", key=key, card=c["cardId"], field=field, before=live[field], after=value)
                            record["done"].append(operation)
                            save(state_path, state)
                    check_entry(A, plan, e, nid)
                    record["verified"] = True
                    save(state_path, state)
                except Deferred:
                    pending.append(key)
                    log(op="adiado-em-tela", key=key, nid=nid)
            log(op="readback-lote", kind="notas", offset=offset)

    shared_ids = [int(n) for n in plan["compartilhados"]]
    for offset in range(0, len(shared_ids), args.batch_size):
        batch = shared_ids[offset:offset + args.batch_size]
        with batch_lock(A, f"{plan['run_id']} compartilhados {offset}"):
            snapshot(A, batch, f"shared-{offset}")
            for nid in batch:
                s = plan["compartilhados"][str(nid)]
                tags = {f"NEBLI::{plan['lesson_id']}", f"NEBLI::compartilhado::{plan['short']}",
                        f"NEBLI::cor::{plan['lesson_id']}::{s['cor']}", s["ordem_tag"]}
                n = note(A, nid)
                incompatible = {t for t in n["tags"] if t.startswith(f"NEBLI::cor::{plan['lesson_id']}::")} - tags
                if incompatible:
                    raise RuntimeError(f"Cor da aula já atribuída difere: {nid}; reconciliar")
                try:
                    if not tags <= set(n["tags"]):
                        mutate_note(A, nid, "addTags", notes=[nid], tags=" ".join(sorted(tags)))
                    after = note(A, nid)
                    if after["fields"] != n["fields"] or not tags <= set(after["tags"]) or not set(n["tags"]) <= set(after["tags"]):
                        raise RuntimeError(f"Readback compartilhado divergente: {nid}")
                    # Não toca bandeiras globais nem agendamento de compartilhados.
                    if nid not in state["shared"]:
                        state["shared"].append(nid)
                    save(state_path, state)
                    log(op="addTags-compartilhado", nid=nid, cor=s["cor"], ordem=s["ordem_tag"])
                except Deferred:
                    pending.append(f"sh-{nid}")
                    log(op="adiado-em-tela", nid=nid)
            log(op="readback-lote", kind="compartilhados", offset=offset)

    results = []
    for e in plan["entries"]:
        record = state["notes"][e["key"]]
        cs = check_entry(A, plan, e, record["nid"])
        results.append({"key": e["key"], "nid": record["nid"], "cards": {
            str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in cs}})
    flags = [c["flag"] for r in results for c in r["cards"].values()]
    rec = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": plan["deck"],
           "notes": results, "cards_tag_aula": len(A("findCards", query=f'"tag:NEBLI::{plan["lesson_id"]}"')),
           "cards_new_lesson": len(flags), "expected": plan["totais"]["cards"],
           "green": flags.count(3), "blue": flags.count(4), "pink": flags.count(5),
           "compartilhados_tag": sorted(state["shared"]), "pending": pending,
           "problems": [f"Adiado em revisão: {key}" for key in pending], "at": now()}
    if len(flags) != rec["expected"]:
        rec["problems"].append("Contagem de cards divergente")
    save(HERE / "receipt.json", rec)
    if not rec["problems"]:
        save(HERE / "plan-aplicado.json", plan)
    print(json.dumps({k: rec[k] for k in ("cards_new_lesson", "expected", "green", "blue", "pink", "pending", "problems")}, ensure_ascii=False))
    # Sync apenas com lock próprio e consulta estrita de ociosidade. Nunca usa GUI.
    if not rec["problems"]:
        with batch_lock(A, f"{plan['run_id']} sync final"):
            if current_note(A) is None:
                A("sync")
                log(op="sync", status="solicitado")
                synced = True
            else:
                synced = False
                log(op="sync-adiado", motivo="revisão ativa")
        if synced:
            SYNC_PENDENTE.unlink(missing_ok=True)
    return 2 if rec["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
