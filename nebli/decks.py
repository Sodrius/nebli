"""Mexer nos decks NEBLI por ramo: a ação num deck vale para ele e para todos os subdecks.

Uso (Anki aberto com AnkiConnect):
    python -m nebli.decks status                        # árvore: cards, suspensos, novos, preset
    python -m nebli.decks status micro
    python -m nebli.decks dessuspender microbiologia    # deck + todos os subdecks
    python -m nebli.decks suspender "controle micro" --simular
    python -m nebli.decks desfazer arquivos-trabalho/deck-ops/<registro>.json
    python -m nebli.decks liberar microbiologia         # todos os novos do ramo, sem limite diário
    python -m nebli.decks liberar microbiologia --encerrar
    python -m nebli.decks liberar microbiologia --treino  # cram dos novos sem reagendar
    python -m nebli.decks liberar microbiologia --treino --encerrar
    python -m nebli.decks instalar-addon                # add-on que põe o total no nome

O trecho casa sem acento nem maiúscula com qualquer parte do caminho canônico do
deck (sem o total entre parênteses); se casar com vários ramos, age em todos e diz
quais. Só atua em NEBLI:: e NEBLI-deck:: (AnKing e Referências ficam fora).

Escrita no Anki passa por escrita(): cria ANKI-ESCRITA.lock, espera o add-on
nebli_decks tirar os totais dos nomes (quem escreve procura pelo nome canônico),
libera, espera os totais voltarem e sincroniza. Suspender grava antes os IDs em
arquivos-trabalho/deck-ops/ e confere depois; não toca agendamento, flags nem conteúdo.

Opções do baralho: todos os decks NEBLI usam um preset só, então mudar em qualquer
deck muda em todos. O teto diário do NEBLI vale também dentro das aulas, por isso
liberar um ramo (config/anki-decks.json) cria no nível de cima o filtrado
"NEBLI · <ramo>: todos os novos", mantido pelo add-on. O status acusa deck fora do
preset; o conserto é `flashcards/scripts/nebli_novos.py --alinhar`.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import time
import unicodedata
import urllib.request
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from nebli import rotulos
from nebli.preflight import chunks, deck_query

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "arquivos-trabalho" / "ANKI-ESCRITA.lock"
OPS_DIR = ROOT / "arquivos-trabalho" / "deck-ops"
LIMITS = ROOT / "config" / "anki-decks.json"
ADDON_SRC = ROOT / "anki-addon" / "nebli_decks"
ROOTS = ("NEBLI", "NEBLI-deck")
ESPERA = 30


class Anki:
    def __init__(self, endpoint="http://127.0.0.1:8765"):
        self.endpoint = endpoint

    def __call__(self, action, **params):
        body = json.dumps({"action": action, "version": 6, "params": params}).encode()
        req = urllib.request.Request(self.endpoint, body, {"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as response:
            data = json.load(response)
        if data.get("error"):
            raise RuntimeError(f"{action}: {data['error']}")
        return data["result"]


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def fold(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text)
                   if not unicodedata.combining(c)).casefold()


def in_scope(deck):
    return rotulos.canonical(deck).split("::")[0] in ROOTS


def inside(deck, branches):
    return any(deck == b or deck.startswith(b + "::") for b in branches)


def resolve(decks, patterns):
    """Ramos vivos mais altos que casam com algum trecho; subdeck de ramo já escolhido é redundante."""
    scoped = {d: fold(rotulos.canonical(d)) for d in decks if in_scope(d)}
    missing = [p for p in patterns if not any(fold(p) in c for c in scoped.values())]
    hits = {d for p in patterns for d, c in scoped.items() if fold(p) in c}
    return sorted(d for d in hits if not inside(d, hits - {d})), missing


def branch_query(branches):
    return "(" + " or ".join(deck_query(b) for b in branches) + ")"


def _wait(call, done, seconds):
    end = time.monotonic() + seconds
    while True:
        names = [n for n in call("deckNames") if rotulos.in_tree(n)]
        if done(names):
            return True
        if time.monotonic() >= end:
            return False
        time.sleep(0.5)


@contextmanager
def escrita(call, label, sync=True):
    """Lock de escrita com a árvore NEBLI em nomes canônicos; sincroniza ao sair sem erro."""
    try:
        handle = LOCK.open("x", encoding="utf-8")
    except FileExistsError:
        raise SystemExit(f"Outra escrita no Anki em andamento ({LOCK}): "
                         f"{LOCK.read_text(encoding='utf-8')}") from None
    with handle:
        handle.write(json.dumps({"executor": "nebli.decks", "aula": label, "at": now()},
                                ensure_ascii=False))
    try:
        if not _wait(call, lambda names: not any(map(rotulos.labeled, names)), ESPERA):
            raise SystemExit("Os decks NEBLI continuam com o total no nome: o add-on nebli_decks "
                             "não está rodando neste Anki. Nada foi escrito.")
        yield
    finally:
        LOCK.unlink(missing_ok=True)
    if sync:
        _wait(call, lambda names: bool(names) and all(map(rotulos.labeled, names)), ESPERA)
        call("sync")


def apply(call, card_ids, suspend, label, branches, sync=True):
    """Muda só os IDs dados; registro gravado antes da escrita permite desfazer exatamente."""
    action = "suspender" if suspend else "dessuspender"
    OPS_DIR.mkdir(parents=True, exist_ok=True)
    path = OPS_DIR / f"{datetime.now():%Y%m%d-%H%M%S}-{action}.json"
    record = {"acao": action, "motivo": label, "ramos": [rotulos.canonical(b) for b in branches],
              "card_ids": card_ids, "inicio": now(), "estado": "iniciado"}
    with escrita(call, f"{action}: {label}", sync=sync):
        path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
        for batch in chunks(card_ids, 500):
            call("suspend" if suspend else "unsuspend", cards=batch)
        states = [s for batch in chunks(card_ids, 500)
                  for s in call("areSuspended", cards=batch)]
        wrong = [cid for cid, s in zip(card_ids, states) if s is not suspend]
        record.update(fim=now(), divergentes=wrong,
                      estado="conferido" if not wrong else "divergente")
        path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    if sync and not wrong:
        record["sync"] = "solicitado ao AnkiWeb; chegada nos aparelhos não conferida"
        path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    return path, record


def change(call, patterns, suspend, simulate=False, sync=True):
    branches, missing = resolve(call("deckNames"), patterns)
    if missing:
        raise SystemExit("Nenhum deck NEBLI casa com: " + ", ".join(missing))
    filtro = "-is:suspended" if suspend else "is:suspended"
    targets = call("findCards", query=f"{branch_query(branches)} {filtro}")
    verbo = "suspender" if suspend else "dessuspender"
    for b in branches:
        n = len(call("findCards", query=f"{deck_query(b)} {filtro}"))
        print(f"  {n:5} a {verbo} | {rotulos.canonical(b)} (e subdecks)")
    if simulate or not targets:
        print("Nada alterado." if targets else f"Nenhum card a {verbo}.")
        return None
    path, record = apply(call, targets, suspend, " + ".join(patterns), branches, sync)
    print(f"{len(targets)} cards: {record['estado']}; registro em {path}")
    if record.get("sync"):
        print("Sync " + record["sync"] + ".")
    return record


def undo(call, record_path, sync=True):
    old = json.loads(Path(record_path).read_text(encoding="utf-8"))
    suspend = old["acao"] == "dessuspender"
    alive = call("areSuspended", cards=old["card_ids"])
    ids = [cid for cid, s in zip(old["card_ids"], alive) if s is not None and s is not suspend]
    print(f"Desfazendo {old['acao']} de {old['inicio']}: {len(ids)} cards ainda no estado alterado.")
    if not ids:
        return None
    path, record = apply(call, ids, suspend, f"desfazer {Path(record_path).name}", old["ramos"], sync)
    print(f"{record['estado']}; registro em {path}")
    return record


def read_config():
    return json.loads(LIMITS.read_text(encoding="utf-8")) if LIMITS.exists() else {"liberar_novos": []}


def count_on_click(canonical_name, wait=None):
    """Pede ao add-on quantos novos/aprender/revisar aparecem ao clicar no deck (None se ele não responder)."""
    request = ROOT / "arquivos-trabalho" / "anki-contagem-pedido.json"
    answer = ROOT / "arquivos-trabalho" / "anki-contagem-resposta.json"
    answer.unlink(missing_ok=True)
    request.write_text(json.dumps({"deck": canonical_name}, ensure_ascii=False), encoding="utf-8")
    end = time.monotonic() + (ESPERA if wait is None else wait)
    while time.monotonic() < end:
        if answer.exists():
            return json.loads(answer.read_text(encoding="utf-8"))
        time.sleep(0.5)
    request.unlink(missing_ok=True)
    return None


def release(call, patterns, stop=False, train=False):
    """Liga/desliga o filtrado "NEBLI · <ramo>: todos os novos", mantido pelo add-on.

    train: "NEBLI · <ramo>: treino dos novos", cram sem reagendar (os cards continuam novos).
    """
    branches, missing = resolve(call("deckNames"), patterns)
    if missing:
        raise SystemExit("Nenhum deck NEBLI casa com: " + ", ".join(missing))
    config = read_config()
    key_name = "treino_novos" if train else "liberar_novos"
    current = config.setdefault(key_name, [])
    for b in branches:
        key = rotulos.canonical(b)
        if stop and key in current:
            current.remove(key)
        elif not stop and key not in current:
            current.append(key)
        print(f"  {key}: {'filtrado encerrado, cards voltam às aulas' if stop else 'treino sem reagendar' if train else 'todos os novos liberados'}")
    LIMITS.parent.mkdir(parents=True, exist_ok=True)
    LIMITS.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if stop:
        return
    for b in branches:
        leaf = rotulos.canonical(b).rsplit("::", 1)[-1]
        name = f"{rotulos.ROOT} · {leaf}: {'treino dos novos' if train else 'todos os novos'}"
        available = len(call("findCards", query=f"{deck_query(b)} is:new -is:suspended -is:buried"))
        end = time.monotonic() + ESPERA
        counts = None
        while time.monotonic() < end:
            counts = count_on_click(name, wait=5)
            if counts and counts.get("encontrado") and counts.get("novos") == available:
                break
            time.sleep(1)
        ok = bool(counts) and counts.get("novos") == available
        print(f"Conferido no Anki: \"{name}\" mostra {counts.get('novos') if counts else '?'} novos "
              f"de {available} disponíveis." if ok else
              f"O Anki ainda não mostra os {available} novos em \"{name}\": conferir o add-on nebli_decks.")


def install_addon():
    base = Path(os.environ.get("APPDATA", "")) / "Anki2" if sys.platform == "win32" else \
        Path.home() / ("Library/Application Support/Anki2" if sys.platform == "darwin" else ".local/share/Anki2")
    target = base / "addons21" / "nebli_decks"
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ADDON_SRC / "__init__.py", target / "__init__.py")
    if not (target / "meta.json").exists():
        shutil.copy2(ADDON_SRC / "meta.json", target / "meta.json")
    config_path = target / "config.json"
    config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
    config["repo"] = str(ROOT)
    config_path.write_text(json.dumps(config, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Add-on em {target}. Na primeira instalação, reiniciar o Anki; depois ele se atualiza sozinho.")
    shortcuts = base / "addons21" / "nebli_atalhos"
    shortcuts.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ADDON_SRC.parent / "nebli_atalhos" / "__init__.py", shortcuts / "__init__.py")
    if not (shortcuts / "meta.json").exists():
        shutil.copy2(ADDON_SRC.parent / "nebli_atalhos" / "meta.json", shortcuts / "meta.json")
    print(f"Atalhos de revisão em {shortcuts}. Reiniciar o Anki para carregar mudanças.")
    from nebli import explicacoes
    explicacoes.install()


def status(call, patterns=()):
    decks = sorted((d for d in call("deckNames") if in_scope(d)), key=rotulos.canonical)
    presets = {d: call("getDeckConfig", deck=d) for d in decks}
    if patterns:
        branches, missing = resolve(decks, patterns)
        if missing:
            raise SystemExit("Nenhum deck NEBLI casa com: " + ", ".join(missing))
        decks = [d for d in decks if inside(d, branches)]
    print(f"{'cards':>6} {'susp':>5} {'novos':>6}  deck")
    canon = {rotulos.canonical(d): d for d in presets}
    for d in decks:
        q = deck_query(d)
        total = len(call("findCards", query=q))
        susp = len(call("findCards", query=q + " is:suspended"))
        new = len(call("findCards", query=q + " is:new -is:suspended"))
        parts = rotulos.canonical(d).split("::")
        line = f"{total:6} {susp:5} {new:6}  {'  ' * (len(parts) - 1)}{parts[-1]}"
        # Referência é o deck mais alto existente do ramo: é ele que decide o preset de todos.
        top = next(canon["::".join(parts[:i])] for i in range(1, len(parts) + 1)
                   if "::".join(parts[:i]) in canon)
        cfg = presets[d]
        if presets[top]["id"] != cfg["id"]:
            line += (f"   <- fora do preset de {rotulos.canonical(top)}: \"{cfg['name']}\" "
                     f"(id {cfg['id']}, {cfg['new']['perDay']} novos/dia)")
        print(line)
    names = {}
    for cfg in presets.values():
        names.setdefault(cfg["name"], set()).add(cfg["id"])
    for name, ids in names.items():
        if len(ids) > 1:
            print(f"Atenção: {len(ids)} presets diferentes com o mesmo nome \"{name}\"; "
                  "rodar flashcards/scripts/nebli_novos.py --alinhar.")
    for branch in read_config().get("liberar_novos", []):
        print(f"Liberado ({LIMITS.name}): todos os novos de {branch} no filtrado "
              f"\"{rotulos.ROOT} · {branch.rsplit('::', 1)[-1]}: todos os novos\".")
    for branch in read_config().get("treino_novos", []):
        print(f"Treino sem reagendar ({LIMITS.name}): novos de {branch} no filtrado "
              f"\"{rotulos.ROOT} · {branch.rsplit('::', 1)[-1]}: treino dos novos\".")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8765")
    sub = parser.add_subparsers(dest="cmd", required=True)
    st = sub.add_parser("status", help="árvore com contagens e presets")
    st.add_argument("trechos", nargs="*")
    for name in ("suspender", "dessuspender"):
        p = sub.add_parser(name, help=f"{name} o deck e todos os subdecks")
        p.add_argument("trechos", nargs="+")
        p.add_argument("--simular", action="store_true", help="só mostra o que mudaria")
        p.add_argument("--sem-sync", action="store_true")
    un = sub.add_parser("desfazer", help="reverte exatamente os IDs de um registro")
    un.add_argument("registro", type=Path)
    un.add_argument("--sem-sync", action="store_true")
    li = sub.add_parser("liberar", help="todos os novos do ramo num filtrado sem limite diário")
    li.add_argument("trechos", nargs="+")
    li.add_argument("--encerrar", action="store_true", help="desfaz o filtrado; os cards voltam às aulas")
    li.add_argument("--treino", action="store_true", help="cram sem reagendar: os cards continuam novos")
    sub.add_parser("instalar-addon", help="copia o add-on nebli_decks para o Anki deste computador")
    args = parser.parse_args()
    if args.cmd == "instalar-addon":
        install_addon()
        return 0
    call = Anki(args.endpoint)
    if args.cmd == "status":
        status(call, args.trechos)
    elif args.cmd == "desfazer":
        undo(call, args.registro, sync=not args.sem_sync)
    elif args.cmd == "liberar":
        release(call, args.trechos, stop=args.encerrar, train=args.treino)
    else:
        change(call, args.trechos, args.cmd == "suspender",
               simulate=args.simular, sync=not args.sem_sync)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
