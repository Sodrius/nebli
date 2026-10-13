"""Roda dentro do Anki, carregado pelo add-on nebli_decks e recarregado quando muda.

A cada tique: com arquivos-trabalho/ANKI-ESCRITA.lock presente, deixa a árvore
NEBLI com os nomes canônicos (quem escreve procura por eles) e não faz mais nada;
sem lock, põe total|dessuspensos|novos disponíveis no nome de cada deck e mantém os decks filtrados
"<ramo>: todos os novos" pedidos em config/anki-decks.json.

Por que filtrado, e fora da árvore NEBLI: no Anki desta coleção o limite diário do
deck de cima (preset NEBLI) vale também quando se clica numa aula ou num filtrado
dentro dela, então nem um limite "Este baralho" maior nem um filtrado aninhado
liberam nada (medido em 25/09). Um filtrado no nível de cima reúne todos os novos
do ramo sem mexer no preset do resto do NEBLI.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from nebli import rotulos

REPO = Path(__file__).resolve().parents[1]
LOCK = REPO / "arquivos-trabalho" / "ANKI-ESCRITA.lock"
CONFIG = REPO / "config" / "anki-decks.json"
ORDER_ADDED = 5  # DYN_ADDED: novos na ordem em que as aulas foram instaladas
SUFFIX = ": todos os novos"
TRAIN_SUFFIX = ": treino dos novos"
STUDY_SUFFIX = ": estudo para prova"
# Treino: só Fácil (f) tira o card; Bom (d) volta mais tarde na sessão (Davi, 30/09).
TRAIN_DELAYS = {"previewAgainSecs": 60, "previewHardSecs": 600, "previewGoodSecs": 1800}
_delays_failed = set()


def relabel(col, strip, log):
    decks = {d.id: d.name for d in col.decks.all_names_and_ids()}
    home = dict(col.db.all(
        "select case when odid then odid else did end, count() from cards group by 1"))
    home_stats = {did: (available, new) for did, available, new in col.db.all(
        "select case when odid then odid else did end, "
        "sum(case when queue != -1 then 1 else 0 end), "
        "sum(case when type = 0 and queue in (0, -3) then 1 else 0 end) "
        "from cards group by 1")}
    filtered = {did: n for did, n in col.db.all("select did, count() from cards group by did")
                if did in decks and col.decks.is_filtered(did)}
    filtered_stats = {did: (available, new) for did, available, new in col.db.all(
        "select did, sum(case when queue != -1 then 1 else 0 end), "
        "sum(case when type = 0 and queue in (0, -3) then 1 else 0 end) "
        "from cards group by did") if did in filtered}
    steps, conflicts = rotulos.plan(decks, home, filtered, strip=strip,
                                    home_stats=home_stats, filtered_stats=filtered_stats)
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



# Estudo completo de um deck com um clique (F-20261011-CLAUDE-02/03): filtrado com todos os cards não suspensos do ramo,
# reagendando pelo FSRS (Davi: "reagenda tb"), sem mexer em configuração. Fora da árvore NEBLI, como os outros filtrados.

def study_name(branch):
    return f"NEBLI · {branch.rsplit('::', 1)[-1]}{STUDY_SUFFIX}"


def study_deck(col, mw, deck_id, log):
    """Cria ou reconstrói o filtrado de estudo do ramo clicado e abre a visão geral. Devolve (nome, cards)."""
    deck = col.decks.get(deck_id)
    branch = rotulos.canonical(deck["name"])
    ids = _branch_ids(col, branch)
    name = study_name(branch)
    fid = _filtered_id(col, name)
    cards = col.find_cards("(" + " or ".join(f"did:{i}" for i in ids) + ") -is:suspended")
    filtered = col.sched.get_or_create_filtered_deck(deck_id=fid or 0)
    if fid is None:
        filtered.name = name
    del filtered.config.search_terms[:]
    filtered.config.search_terms.add(search="(" + " or ".join(f"did:{i}" for i in ids) + ") -is:suspended",
                                     limit=9999, order=ORDER_ADDED)
    filtered.config.reschedule = True
    out = col.sched.add_or_update_filtered_deck(filtered)
    col.decks.select(fid or out.id)
    log(f"estudo para prova: {name} ({len(cards)} cards não suspensos, reagenda pelo FSRS)")
    mw.moveToState("overview")
    return name, len(cards)


def recompute_memory(col, deck_id, log):
    """Recalcula o estado de memória FSRS (estabilidade/dificuldade) dos cards revisados do ramo, a partir do histórico."""
    cids = col.decks.cids(deck_id, children=True)
    done = failed = 0
    for cid in cids:
        card = col.get_card(cid)
        if card.type == 0:
            continue
        try:
            state = col.compute_memory_state(cid)
            if failed == 0 and done == 0:
                log(f"memória FSRS: campos {[a for a in dir(state) if not a.startswith('_')]}; card.memory_state={card.memory_state!r}")
            return_state = getattr(state, "state", None) or state
            stability, difficulty = getattr(return_state, "stability", None), getattr(return_state, "difficulty", None)
            if stability is None or difficulty is None:
                continue
            from anki.cards import FSRSMemoryState
            card.memory_state = FSRSMemoryState(stability=stability, difficulty=difficulty)
            col.update_card(card)
            done += 1
        except Exception as exc:  # versão do Anki sem a API ou FSRS desligado
            failed += 1
            if failed == 1:
                log(f"memória FSRS: {type(exc).__name__}: {exc}")
    log(f"memória FSRS recalculada em {done} cards ({failed} falhas)")
    return done, failed


def _memory_for(col, cids, log):
    """Recalcula a memória FSRS de cards específicos a partir do histórico; devolve quantos mudaram."""
    from anki.cards import FSRSMemoryState
    done = 0
    for cid in cids:
        try:
            card = col.get_card(cid)
            state = col.compute_memory_state(cid)
            state = getattr(state, "state", None) or state
            stability, difficulty = getattr(state, "stability", None), getattr(state, "difficulty", None)
            if stability is None or difficulty is None:
                continue
            card.memory_state = FSRSMemoryState(stability=stability, difficulty=difficulty)
            col.update_card(card)
            done += 1
        except Exception as exc:
            log(f"memória FSRS automática: {type(exc).__name__}: {exc}")
            break
    return done


def auto_memory(mw, store, log):
    """Depois do "estudar tudo" (F-20261011-CLAUDE-06, Davi: "quero que já recalcule o FSRS sem eu pedir"), fora da revisão:
    recalcula pelo histórico a memória FSRS dos cards respondidos num filtrado de estudo desde a última passada.
    O filtrado já reagenda a cada resposta com o intervalo real decorrido (revisão adiantada conta como adiantada);
    esta passada garante o estado coerente sem clique, mesmo para cards que voltaram às aulas."""
    if mw.state == "review":
        return 0
    col = mw.col
    path = store / "memoria-auto.json"
    try:
        last = json.loads(path.read_text(encoding="utf-8"))["revlog"]
    except Exception:
        last = None
    newest = col.db.scalar("select max(id) from revlog") or 0
    if last is None or newest <= last:
        if last is None:
            store.mkdir(exist_ok=True)
            path.write_text(json.dumps({"revlog": newest}), encoding="utf-8")
        return 0
    study = [d.id for d in col.decks.all_names_and_ids() if d.name.endswith(STUDY_SUFFIX)]
    cids = col.db.list(f"select distinct cid from revlog where id > {int(last)}")
    targets = []
    for cid in cids:
        try:
            card = col.get_card(cid)
        except Exception:
            continue
        # revisões feitas no filtrado de estudo: card ainda nele, ou resposta tipo "filtrado/cram" (type 3) no revlog
        cram = col.db.scalar(f"select count() from revlog where cid={cid} and id>{int(last)} and type=3")
        if card.did in study or cram:
            targets.append(cid)
    done = _memory_for(col, targets, log) if targets else 0
    path.write_text(json.dumps({"revlog": newest}), encoding="utf-8")
    if done:
        log(f"memória FSRS automática: {done} card(s) do estudo para prova")
    return 0


def deck_menu(menu, deck_id, mw, log):
    """Itens no menu de engrenagem do deck (tela de baralhos)."""
    from aqt.utils import tooltip
    menu.addSeparator()

    def study():
        name, n = study_deck(mw.col, mw, deck_id, log)
        tooltip(f"{name}: {n} cards (reagenda pelo FSRS)")

    def memory():
        done, failed = recompute_memory(mw.col, deck_id, log)
        tooltip(f"Memória FSRS recalculada em {done} cards" + (f" ({failed} falhas, ver log)" if failed else ""))

    menu.addAction("NEBLI: estudar tudo deste deck (prova)").triggered.connect(study)
    menu.addAction("NEBLI: recalcular memória FSRS deste deck").triggered.connect(memory)


def action_request(mw, log):
    """Gatilho por arquivo para testar sem clicar: arquivos-trabalho/anki-acao-pedido.json {"acao": "estudar"|"memoria", "deck": nome canônico}."""
    request = REPO / "arquivos-trabalho" / "anki-acao-pedido.json"
    if not request.exists() or mw.state == "review":
        return
    data = json.loads(request.read_text(encoding="utf-8"))
    request.unlink()
    col = mw.col
    did = next((d.id for d in col.decks.all_names_and_ids() if rotulos.canonical(d.name) == data["deck"]), None)
    result = {"pedido": data, "encontrado": did is not None}
    if did is not None:
        if data["acao"] == "estudar":
            result["nome"], result["cards"] = study_deck(col, mw, did, log)
        elif data["acao"] == "encerrar":  # esvazia e apaga o filtrado de estudo do ramo; os cards voltam às aulas
            fid = _filtered_id(col, study_name(data["deck"]))
            if fid:
                col.sched.empty_filtered_deck(fid)
                col.decks.remove([fid])
            result["encerrado"] = bool(fid)
        elif data["acao"] == "memoria":
            result["feitos"], result["falhas"] = recompute_memory(col, did, log)
    (REPO / "arquivos-trabalho" / "anki-acao-resposta.json").write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")


def tick(mw, store, log):
    browser_setup_open(mw)
    answer_count_request(mw)
    action_request(mw, log)
    auto_memory(mw, store, log)
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


# Coluna "Ordem da aula" no Browser: mostra e ordena pela tag NEBLI::ordem::<curto>-<NN>.

def browser_setup(browser):
    """Enter suspende e Delete/Backspace apagam, só na tabela; as ações nativas conservam seleção, desfazer e atualização.

    Delete (F-20261011-CLAUDE-06, Davi: "quero que o botão de excluir do teclado exclua o card no browse"): apaga a nota
    selecionada como o Ctrl+Delete nativo (desfazer em Editar), e a ordem da aula se renumera (renumber_after_delete).
    """
    from aqt.qt import QKeySequence, Qt
    from nebli import ordem
    if getattr(browser, "_nebli_browser_v4", False):
        return
    table = browser.table
    browser_columns(table._model.columns)
    action = browser.form.actionToggle_Suspend
    action.setShortcuts([QKeySequence("Return"), QKeySequence("Enter")])
    action.setShortcutContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
    table._view.addAction(action)
    delete = browser.form.actionDelete
    keys = [QKeySequence(k) for k in ("Delete", "Backspace")]
    keys += [k for k in delete.shortcuts() if k.toString() not in ("Del", "Backspace")]
    delete.setShortcuts(keys)
    delete.setShortcutContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
    table._view.addAction(delete)
    for key in (ordem.KEY, "nebliSuspenso"):
        if table._model.active_column_index(key) is None:
            table._on_column_toggled(True, key)
    if table._state.sort_column in ("noteFld", "noteCrt", "cardDue", "deck", "noteMod", "cardMod", "template"):
        table._state.sort_column = ordem.KEY
        table._state.sort_backwards = False
        table._set_sort_indicator()
        if table._model._items:
            browser.search()
    browser._nebli_browser_v4 = True


def browser_setup_open(mw):
    from aqt import dialogs, gui_hooks
    if not getattr(mw, "_nebli_browser_setup_hook", False):
        # Indireção conserva o hot reload da implementação.
        gui_hooks.browser_will_show.append(lambda browser: browser_setup(browser))
        mw._nebli_browser_setup_hook = True
    entry = dialogs._dialogs.get("Browser")
    if entry and entry[1] is not None:
        browser_setup(entry[1])
        b = entry[1]
        if b.isVisible() and not getattr(b, "_nebli_columns_visible", False):
            header = b.table._view.horizontalHeader()
            for position, (key, width) in enumerate((("nebliOrdem", 165), ("nebliSuspenso", 80))):
                index = b.table._model.active_column_index(key)
                header.showSection(index)
                header.moveSection(header.visualIndex(index), position)
                header.resizeSection(index, width)
            b.table._view.horizontalScrollBar().setValue(0)
            b._nebli_columns_visible = True



def browser_columns(columns):
    from anki.collection import BrowserColumns
    from nebli import ordem
    wanted = dict(
        key=ordem.KEY, cards_mode_label=ordem.LABEL, notes_mode_label=ordem.LABEL,
        sorting_cards=BrowserColumns.SORTING_ASCENDING, sorting_notes=BrowserColumns.SORTING_ASCENDING,
        sorting=BrowserColumns.SORTING_ASCENDING, uneditable=True, alignment=BrowserColumns.ALIGNMENT_START,
        cards_mode_tooltip="Posição do card na sequência da aula", notes_mode_tooltip="Posição da nota na sequência da aula")
    # os campos da coluna mudam entre versões do Anki: usar só os que esta versão tem
    known = BrowserColumns.Column.DESCRIPTOR.fields_by_name
    columns[ordem.KEY] = BrowserColumns.Column(**{k: v for k, v in wanted.items() if k in known})
    wanted.update(key="nebliSuspenso", cards_mode_label="Suspenso", notes_mode_label="Suspensos",
                  sorting_cards=BrowserColumns.SORTING_NONE, sorting_notes=BrowserColumns.SORTING_NONE,
                  sorting=BrowserColumns.SORTING_NONE,
                  cards_mode_tooltip="Suspensão real do card, independente da bandeira",
                  notes_mode_tooltip="Quantidade de cards suspensos nesta nota")
    columns["nebliSuspenso"] = BrowserColumns.Column(**{k: v for k, v in wanted.items() if k in known})


def browser_row(col, item_id, is_note, row, columns):
    from nebli import ordem
    if "nebliSuspenso" in columns:
        if is_note:
            queues = col.db.list("select queue from cards where nid = ?", item_id)
            text = f"{queues.count(-1)}/{len(queues)}" if queues else "—"
        else:
            text = "Sim" if col.db.scalar("select queue from cards where id = ?", item_id) == -1 else "Não"
        row.cells[list(columns).index("nebliSuspenso")].text = text
    if ordem.KEY not in columns:
        return
    nid = item_id if is_note else col.db.scalar("select nid from cards where id = ?", item_id)
    tags = col.db.scalar("select tags from notes where id = ?", nid) or ""
    row.cells[list(columns).index(ordem.KEY)].text = ordem.label(
        tags.split(), getattr(col, "_nebli_browser_order_main", None))


def browser_search(col, ctx):
    """Ordenação própria: o backend não conhece a coluna, então a busca é feita e ordenada aqui."""
    from nebli import ordem
    chave = getattr(ctx.order, "key", None)
    col._nebli_browser_order_main = None
    # O cabeçalho reflete a ordenação real. Um clique noutra coluna é respeitado.
    if chave != ordem.KEY:
        return
    notes_mode = ctx.browser.table.is_notes_mode()
    ids = list(col.find_notes(ctx.search, order=False) if notes_mode else col.find_cards(ctx.search, order=False))
    rows = col.db.all("select n.id, n.tags from notes n" if notes_mode else
                      "select c.id, n.tags, c.ord, n.id from cards c join notes n on n.id = c.nid")
    wanted = set(ids)
    rows = [r for r in rows if r[0] in wanted]
    main = ordem.dominant(r[1].split() for r in rows)
    col._nebli_browser_order_main = main
    def key(r):
        return ordem.sort_key(r[1].split(), main) + ((r[0],) if notes_mode else (r[3], r[2]))
    ctx.ids = [r[0] for r in sorted(rows, key=key, reverse=bool(ctx.reverse))]


# Tela de baralhos (F-20261011-CLAUDE-04/05): nome da aula em negrito, números sem negrito; deck todo suspenso em vermelho.
_DECK_LINK = re.compile(r"(<a[^>]*class=\"?deck\"?[^>]*>)([^<]+?)( \((\d+)(?:\|(\d+)\|(\d+))?\))?(</a>)")


def deck_browser_html(html):
    """Reescreve os links de deck: <b>Nome</b> <span>(total|ativos|novos)</span>; vermelho se ativos == 0 e total > 0."""
    def fix(m):
        name, label, total, active = m.group(2), m.group(3) or "", m.group(4), m.group(5)
        red = total is not None and active is not None and int(total) > 0 and int(active) == 0
        style = ' style="color:#d32f2f"' if red else ""
        lab = f'<span style="font-weight:normal">{label}</span>' if label else ""
        return f"{m.group(1)}<b{style}>{name}</b>{lab}{m.group(7)}"
    return _DECK_LINK.sub(fix, html)


# Apagar no Browser (F-20261011-CLAUDE-04): a nota sai e as posições seguintes da mesma aula descem uma casa.
_pending_gaps = []


def note_deletion(col, note_ids):
    """Chamado antes de apagar: guarda (curto, número) de cada posição que vai sumir."""
    from nebli import ordem
    for nid in note_ids:
        try:
            note = col.get_note(nid)
        except Exception:
            continue
        for tag in note.tags:
            m = ordem.ORDER.match(tag)
            if m:
                _pending_gaps.append((m.group(1), int(m.group(2))))


def renumber_after_delete(col, log):
    """Depois de apagar: fecha os buracos na numeração de cada aula afetada (sem mexer em agendamento)."""
    from nebli import ordem
    if not _pending_gaps:
        return 0
    gaps = {}
    for short, n in _pending_gaps:
        gaps.setdefault(short, set()).add(n)
    _pending_gaps.clear()
    changed = 0
    for short, removed in gaps.items():
        nids = col.find_notes(f'"tag:NEBLI::ordem::{short}-*"')
        moves = []
        for nid in nids:
            note = col.get_note(nid)
            for tag in note.tags:
                m = ordem.ORDER.match(tag)
                if m and m.group(1) == short:
                    n = int(m.group(2))
                    shift = sum(1 for r in removed if r < n)
                    if shift:
                        moves.append((note, tag, ordem.tag(short, n - shift)))
        for note, old, new in moves:
            note.tags = [t for t in note.tags if t != old] + [new]
            col.update_note(note)
            changed += 1
        log(f"ordem {short}: {len(removed)} posição(ões) apagada(s), {changed} nota(s) renumerada(s)")
    return changed
