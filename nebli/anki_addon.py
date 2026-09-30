"""Roda dentro do Anki, carregado pelo add-on nebli_decks e recarregado quando muda.

A cada tique: com arquivos-trabalho/ANKI-ESCRITA.lock presente, deixa a árvore
NEBLI com os nomes canônicos (quem escreve procura por eles) e não faz mais nada;
sem lock, põe o total de cards no nome de cada deck e mantém os decks filtrados
"<ramo>: todos os novos" pedidos em config/anki-decks.json.

Por que filtrado, e fora da árvore NEBLI: no Anki desta coleção o limite diário do
deck de cima (preset NEBLI) vale também quando se clica numa aula ou num filtrado
dentro dela, então nem um limite "Este baralho" maior nem um filtrado aninhado
liberam nada (medido em 25/09). Um filtrado no nível de cima reúne todos os novos
do ramo sem mexer no preset do resto do NEBLI.
"""
from __future__ import annotations

import json
from pathlib import Path

from nebli import rotulos

REPO = Path(__file__).resolve().parents[1]
LOCK = REPO / "arquivos-trabalho" / "ANKI-ESCRITA.lock"
CONFIG = REPO / "config" / "anki-decks.json"
ORDER_ADDED = 5  # DYN_ADDED: novos na ordem em que as aulas foram instaladas
SUFFIX = ": todos os novos"
TRAIN_SUFFIX = ": treino dos novos"
# Treino: só Fácil (f) tira o card; Bom (d) volta mais tarde na sessão (Davi, 30/09).
TRAIN_DELAYS = {"previewAgainSecs": 60, "previewHardSecs": 600, "previewGoodSecs": 1800}
_delays_failed = set()


def relabel(col, strip, log):
    decks = {d.id: d.name for d in col.decks.all_names_and_ids()}
    home = dict(col.db.all(
        "select case when odid then odid else did end, count() from cards group by 1"))
    filtered = {did: n for did, n in col.db.all("select did, count() from cards group by did")
                if did in decks and col.decks.is_filtered(did)}
    steps, conflicts = rotulos.plan(decks, home, filtered, strip=strip)
    for path in conflicts:
        log(f"conflito: mais de um deck com o nome {path}; ramo sem contagem")
    changed = 0
    for did, leaf in steps:
        live = col.decks.get(did)["name"]
        parent, _, current = live.rpartition("::")
        if current == leaf:
            continue
        new = f"{parent}::{leaf}" if parent else leaf
        other = col.decks.id_for_name(new)
        if other and other != did:
            log(f"conflito: {new} já existe; {live} não renomeado")
            continue
        col.decks.rename(did, new)
        changed += 1
    return changed


def filtered_name(branch):
    """Fora da árvore NEBLI: dentro dela o teto diário do preset também limitaria o filtrado."""
    return f"NEBLI · {branch.rsplit('::', 1)[-1]}{SUFFIX}"


def _branch_ids(col, branch):
    return [d.id for d in col.decks.all_names_and_ids()
            if not col.decks.is_filtered(d.id)
            and (rotulos.canonical(d.name) == branch or rotulos.canonical(d.name).startswith(branch + "::"))]


def _filtered_id(col, name):
    return next((d.id for d in col.decks.all_names_and_ids()
                 if col.decks.is_filtered(d.id) and rotulos.canonical(d.name) == name), None)


def train_name(branch):
    return f"NEBLI · {branch.rsplit('::', 1)[-1]}{TRAIN_SUFFIX}"


def _train_delays(col, did, log):
    """Atrasos do treino direto na configuração do filtrado: sem reconstruir, nada volta."""
    deck = col.decks.get(did)
    if did in _delays_failed or all(deck.get(k) == v for k, v in TRAIN_DELAYS.items()):
        return 0
    deck.update(TRAIN_DELAYS)
    col.decks.save(deck)
    saved = col.decks.get(did)
    if not all(saved.get(k) == v for k, v in TRAIN_DELAYS.items()):
        _delays_failed.add(did)
        log(f"atrasos do treino não gravaram em {deck['name']}: conferir versão do Anki")
        return 0
    log(f"atrasos do treino: {deck['name']} (Bom volta em 30 min; só Fácil tira)")
    return 1


def release_new(col, mw, store, log):
    """Filtrados de novos por ramo; encerra os que saíram do config.

    "todos os novos" (liberar_novos) conta para o agendamento e é reconstruído a cada
    tique. "treino dos novos" (treino_novos) é cram sem reagendar: os cards continuam
    novos; é montado uma vez só, e recomeçar o treino ou apagar o deck fica com Davi
    (botão Reconstruir/Excluir do Anki).

    Apagar à mão encerra (Davi, 30/09: "eles devem poder ser deletados a mão"): filtrado
    já criado que sumiu sai do config e não é recriado; os cards já voltaram às aulas.
    """
    config = json.loads(CONFIG.read_text(encoding="utf-8")) if CONFIG.exists() else {}
    wanted = {filtered_name(branch): (branch, True) for branch in config.get("liberar_novos", [])}
    wanted.update({train_name(branch): (branch, False) for branch in config.get("treino_novos", [])})
    state_file = store / "filtrados.json"
    managed = set(json.loads(state_file.read_text(encoding="utf-8"))) if state_file.exists() else set()
    kept = set(managed)
    changed = 0
    for name in sorted(managed - set(wanted)):
        did = _filtered_id(col, name)
        if did:
            col.sched.empty_filtered_deck(did)
            col.decks.remove([did])
            log(f"filtrado encerrado, cards de volta às aulas: {name}")
            changed += 1
        kept.discard(name)
    dropped = []
    for name, (branch, reschedule) in wanted.items():
        if name in managed and _filtered_id(col, name) is None:
            dropped.append((branch, "liberar_novos" if reschedule else "treino_novos"))
            kept.discard(name)
            log(f"filtrado apagado à mão, sai do config e não é recriado: {name}")
            changed += 1
            continue
        if not reschedule and name in managed:
            did = _filtered_id(col, name)
            changed += _train_delays(col, did, log) if did else 0
            continue
        ids = _branch_ids(col, branch)
        if not ids:
            log(f"ramo não encontrado para filtrar: {branch}")
            continue
        did = _filtered_id(col, name)
        pending = col.db.scalar(
            f"select count() from cards where did in ({','.join(map(str, ids))}) and type = 0 and queue = 0")
        if not pending or mw.state == "review":
            continue  # nada a reunir, ou revisão em andamento: não mexer no filtrado agora
        deck = col.sched.get_or_create_filtered_deck(deck_id=did or 0)
        if did is None:
            deck.name = name
        del deck.config.search_terms[:]
        deck.config.search_terms.add(search="(" + " or ".join(f"did:{i}" for i in ids) + ") is:new",
                                     limit=9999, order=ORDER_ADDED)
        deck.config.reschedule = reschedule
        out = col.sched.add_or_update_filtered_deck(deck)
        if not reschedule:
            _train_delays(col, did or out.id, log)
        kept.add(name)
        log(f"filtrado {'criado' if did is None else 'reconstruído'}: {name} ({pending} novos a reunir"
            f"{'' if reschedule else ', sem reagendar'})")
        changed += 1
    if dropped:
        for branch, key in dropped:
            config[key] = [b for b in config.get(key, []) if b != branch]
        CONFIG.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if kept != managed:
        store.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(sorted(kept), ensure_ascii=False), encoding="utf-8")
    return changed


def undo_deck_limits(col, store, log):
    """Remove o limite "Este baralho" da primeira versão, que o teto do preset tornava inócuo."""
    old = store / "limites-aplicados.json"
    if not old.exists():
        return 0
    for did in json.loads(old.read_text(encoding="utf-8")):
        deck = col.decks.get(did, default=False)
        if deck and (deck.get("newLimit") is not None or deck.get("newLimitToday") is not None):
            deck["newLimit"] = None
            deck["newLimitToday"] = None
            col.decks.save(deck)
    old.unlink()
    log("limites por deck da primeira versão removidos")
    return 1


def answer_count_request(mw):
    """Conferência para o repositório: quantos novos/aprender/revisar aparecem ao clicar num deck."""
    request = REPO / "arquivos-trabalho" / "anki-contagem-pedido.json"
    if not request.exists():
        return
    name = json.loads(request.read_text(encoding="utf-8"))["deck"]
    col = mw.col
    did = next((d.id for d in col.decks.all_names_and_ids() if rotulos.canonical(d.name) == name), None)
    result = {"deck": name, "encontrado": did is not None}
    if did is not None and mw.state != "review":
        current = col.decks.get_current_id()
        col.decks.select(did)
        result["novos"], result["aprender"], result["revisar"] = col.sched.counts()
        col.decks.select(current)
    request.unlink()
    (REPO / "arquivos-trabalho" / "anki-contagem-resposta.json").write_text(
        json.dumps(result, ensure_ascii=False), encoding="utf-8")


def tick(mw, store, log):
    answer_count_request(mw)
    locked = LOCK.exists()
    changed = relabel(mw.col, strip=locked, log=log)
    if not locked:
        changed += undo_deck_limits(mw.col, store, log)
        changed += release_new(mw.col, mw, store, log)
    if changed and mw.state == "deckBrowser":
        mw.deckBrowser.refresh()
    elif changed and mw.state == "overview":
        mw.overview.refresh()
    return changed
