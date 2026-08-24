#!/usr/bin/env python3
"""Servidor AnkiConnect headless para o pipeline NEBLI.

Fala o mesmo protocolo do add-on AnkiConnect (POST JSON em localhost:8765),
mas em vez de conversar com o Anki desktop do Davi, opera direto numa coleção
local aberta pela biblioteca `anki`. Serve para rodar os scripts de
`flashcards/scripts/` em ambiente sem GUI (container, CI, sessão remota) sem
tocar em nada de produção.

    pip install anki
    python flashcards/scripts/ankiconnect_local.py &

Coleção padrão: ~/.local/share/nebli-anki/collection.anki2 (criada vazia na
primeira execução). Para semear a partir de um .apkg do repo:

    python flashcards/scripts/ankiconnect_local.py \
        --import "flashcards/decks-apkg/P3 - UC02 completo.apkg"

Duas escolhas deliberadas, para o comportamento local bater com a instalação
real do Davi:

* `notesInfo` NÃO devolve `guid` (o AnkiConnect dele também não — ver MEMORY.md
  § piloto ANATO-06). Assim o casamento card-a-card continua pelo texto bruto
  do campo 1 aqui e lá. `--expose-guid` liga o campo, se algum dia precisar.
* `sync` fica desligado: sincronizar daqui escreveria na coleção AnkiWeb de
  verdade. Só roda com `--allow-sync` + ANKIWEB_USERNAME/ANKIWEB_PASSWORD.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import signal
import sys
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# `flashcards/scripts/anki.py` (helper do repo) sombreia o pacote `anki` porque o
# diretório do script entra no sys.path — tirar ele daqui antes de importar.
_HERE = str(Path(__file__).resolve().parent)
sys.path[:] = [p for p in sys.path if p not in ("", ".", _HERE)]

import anki.collection  # noqa: E402,F401  (o módulo antes dos submódulos evita o circular import)
from anki.collection import Collection, DeckIdLimit  # noqa: E402
from anki.import_export_pb2 import (  # noqa: E402
    ExportAnkiPackageOptions,
    ImportAnkiPackageOptions,
    ImportAnkiPackageRequest,
)
from anki.notes import NoteFieldsCheckResult  # noqa: E402

API_VERSION = 6
DEFAULT_COLLECTION = Path.home() / ".local" / "share" / "nebli-anki" / "collection.anki2"

COL: Collection | None = None
LOCK = threading.RLock()
OPTS = argparse.Namespace(expose_guid=False, allow_sync=False)
ACTIONS: dict[str, callable] = {}


def action(fn):
    ACTIONS[fn.__name__] = fn
    return fn


class AnkiConnectError(RuntimeError):
    """Erro devolvido no campo `error` da resposta, como o add-on faz."""


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def _fields_dict(note) -> dict:
    return {name: {"value": value, "order": i}
            for i, (name, value) in enumerate(note.items())}


def _note_info(note) -> dict:
    info = {
        "noteId": note.id,
        "profile": "nebli-local",
        "modelName": note.note_type()["name"],
        "tags": list(note.tags),
        "fields": _fields_dict(note),
        "mod": note.mod,
        "cards": list(note.card_ids()),
    }
    if OPTS.expose_guid:
        info["guid"] = note.guid
    return info


def _card_info(card) -> dict:
    note = card.note()
    did = card.odid or card.did
    info = {
        "cardId": card.id,
        "note": card.nid,
        "nid": card.nid,
        "deckName": COL.decks.name(did),
        "modelName": note.note_type()["name"],
        "fields": _fields_dict(note),
        "fieldOrder": card.ord,
        "ord": card.ord,
        "type": card.type,
        "queue": card.queue,
        "due": card.due,
        "interval": card.ivl,
        "ivl": card.ivl,
        "factor": card.factor,
        "reps": card.reps,
        "lapses": card.lapses,
        "left": card.left,
        "mod": card.mod,
        "flags": card.flags,
    }
    try:  # renderização pode falhar em nota malformada; o resto do card ainda serve
        info["question"] = card.question()
        info["answer"] = card.answer()
        info["css"] = card.css()
    except Exception as exc:  # noqa: BLE001
        info["question"] = info["answer"] = ""
        info["css"] = ""
        info["renderError"] = str(exc)
    return info


def _deck_id(name: str, create: bool = False) -> int:
    deck = COL.decks.by_name(name)
    if deck:
        return deck["id"]
    if create:
        return COL.decks.id(name)
    raise AnkiConnectError(f"deck was not found: {name}")


def _notetype(name: str):
    nt = COL.models.by_name(name)
    if nt is None:
        raise AnkiConnectError(f"model was not found: {name}")
    return nt


def _build_note(spec: dict):
    nt = _notetype(spec["modelName"])
    note = COL.new_note(nt)
    valid = set(note.keys())
    for field, value in (spec.get("fields") or {}).items():
        if field in valid:
            note[field] = value
    note.tags = [t for t in (spec.get("tags") or []) if t.strip()]
    return note


def _check_addable(note, spec: dict) -> None:
    if (spec.get("options") or {}).get("allowDuplicate"):
        return
    state = note.fields_check()
    if state == NoteFieldsCheckResult.EMPTY:
        raise AnkiConnectError("cannot create note because it is empty")
    if state == NoteFieldsCheckResult.DUPLICATE:
        raise AnkiConnectError("cannot create note because it is a duplicate")


# --------------------------------------------------------------------------
# meta
# --------------------------------------------------------------------------

@action
def version(**_):
    return API_VERSION


@action
def multi(actions=None, **_):
    out = []
    for item in actions or []:
        out.append(_dispatch(item.get("action"), item.get("params") or {}))
    return out


@action
def sync(**_):
    if not OPTS.allow_sync:
        raise AnkiConnectError(
            "sync desligado neste servidor local (escreveria na coleção AnkiWeb real). "
            "Rode com --allow-sync + ANKIWEB_USERNAME/ANKIWEB_PASSWORD para habilitar.")
    user = os.environ.get("ANKIWEB_USERNAME")
    pwd = os.environ.get("ANKIWEB_PASSWORD")
    if not (user and pwd):
        raise AnkiConnectError("ANKIWEB_USERNAME/ANKIWEB_PASSWORD não definidos")
    auth = COL.sync_login(user, pwd, os.environ.get("ANKIWEB_ENDPOINT") or None)
    COL.sync_collection(auth, True)
    return None


@action
def guiCurrentCard(**_):
    return None  # headless: nunca há reviewer aberto


# --------------------------------------------------------------------------
# decks
# --------------------------------------------------------------------------

@action
def deckNames(**_):
    return [d.name for d in COL.decks.all_names_and_ids()]


@action
def deckNamesAndIds(**_):
    return {d.name: d.id for d in COL.decks.all_names_and_ids()}


@action
def createDeck(deck=None, **_):
    return COL.decks.id(deck)


@action
def deleteDecks(decks=None, cardsToo=False, **_):
    if not cardsToo:
        raise AnkiConnectError("cardsToo precisa ser true nesta versão do protocolo")
    ids = [_deck_id(name) for name in decks or []]
    COL.decks.remove(ids)
    return None


@action
def changeDeck(cards=None, deck=None, **_):
    COL.set_deck(cards or [], _deck_id(deck, create=True))
    return None


@action
def getDeckConfig(deck=None, **_):
    return COL.decks.config_dict_for_deck_id(_deck_id(deck))


@action
def saveDeckConfig(config=None, **_):
    COL.decks.update_config(config)
    return True


@action
def getDeckConfigs(**_):
    return COL.decks.all_config()


@action
def getDeckStats(decks=None, **_):
    stats = {}
    for name in decks or []:
        did = _deck_id(name)
        stats[str(did)] = {
            "deck_id": did,
            "name": name,
            "total_in_deck": len(COL.find_cards(f'deck:"{name}"')),
        }
    return stats


# --------------------------------------------------------------------------
# busca
# --------------------------------------------------------------------------

@action
def findNotes(query="", **_):
    return list(COL.find_notes(query))


@action
def findCards(query="", **_):
    return list(COL.find_cards(query))


@action
def notesInfo(notes=None, query=None, **_):
    ids = list(COL.find_notes(query)) if notes is None and query is not None else (notes or [])
    out = []
    for nid in ids:
        try:
            out.append(_note_info(COL.get_note(nid)))
        except Exception:  # noqa: BLE001  (o add-on devolve {} para nota inexistente)
            out.append({})
    return out


@action
def cardsInfo(cards=None, **_):
    out = []
    for cid in cards or []:
        try:
            out.append(_card_info(COL.get_card(cid)))
        except Exception:  # noqa: BLE001
            out.append({})
    return out


@action
def cardsToNotes(cards=None, **_):
    seen, out = set(), []
    for cid in cards or []:
        try:
            nid = COL.get_card(cid).nid
        except Exception:  # noqa: BLE001
            continue
        if nid not in seen:
            seen.add(nid)
            out.append(nid)
    return out


@action
def cardsFromNotes(notes=None, **_):
    out = []
    for nid in notes or []:
        try:
            out.extend(COL.get_note(nid).card_ids())
        except Exception:  # noqa: BLE001
            continue
    return out


@action
def areSuspended(cards=None, **_):
    out = []
    for cid in cards or []:
        try:
            out.append(COL.get_card(cid).queue == -1)
        except Exception:  # noqa: BLE001
            out.append(None)
    return out


@action
def getNumCardsReviewedByDay(**_):
    rollover = COL.get_config("rollover", 4) or 0
    rows = COL.db.all(
        "select strftime('%Y-%m-%d', id/1000 - ?, 'unixepoch', 'localtime') as d, count() "
        "from revlog group by d order by d desc", rollover * 3600)
    return [[d, n] for d, n in rows]


# --------------------------------------------------------------------------
# notas
# --------------------------------------------------------------------------

@action
def addNote(note=None, **_):
    built = _build_note(note)
    _check_addable(built, note)
    COL.add_note(built, _deck_id(note["deckName"], create=True))
    return built.id


@action
def addNotes(notes=None, **_):
    out = []
    for spec in notes or []:
        try:
            out.append(addNote(note=spec))
        except Exception:  # noqa: BLE001  (o add-on devolve null por nota que falhou)
            out.append(None)
    return out


@action
def updateNoteFields(note=None, **_):
    target = COL.get_note(note["id"])
    valid = set(target.keys())
    for field, value in (note.get("fields") or {}).items():
        if field in valid:
            target[field] = value
    COL.update_note(target)
    return None


@action
def updateNote(note=None, **_):
    if note.get("fields"):
        updateNoteFields(note=note)
    if note.get("tags") is not None:
        target = COL.get_note(note["id"])
        target.tags = list(note["tags"])
        COL.update_note(target)
    return None


@action
def deleteNotes(notes=None, **_):
    COL.remove_notes(notes or [])
    return None


@action
def addTags(notes=None, tags="", **_):
    COL.tags.bulk_add(notes or [], tags)
    return None


@action
def removeTags(notes=None, tags="", **_):
    COL.tags.bulk_remove(notes or [], tags)
    return None


@action
def getTags(**_):
    return COL.tags.all()


# --------------------------------------------------------------------------
# cards
# --------------------------------------------------------------------------

@action
def suspend(cards=None, **_):
    COL.sched.suspend_cards(cards or [])
    return True


@action
def unsuspend(cards=None, **_):
    COL.sched.unsuspend_cards(cards or [])
    return True


@action
def setFlag(cards=None, flag=0, **_):
    COL.set_user_flag_for_cards(int(flag), cards or [])
    return None


@action
def setSpecificValueOfCard(card=None, keys=None, newValues=None, **_):
    target = COL.get_card(card)
    for key, value in zip(keys or [], newValues or []):
        if not hasattr(target, key):
            raise AnkiConnectError(f"card não tem o atributo {key}")
        setattr(target, key, type(getattr(target, key))(value))
    COL.update_card(target)
    return [True] * len(keys or [])


@action
def forgetCards(cards=None, **_):
    COL.sched.reset_cards(cards or [])
    return None


# --------------------------------------------------------------------------
# modelos
# --------------------------------------------------------------------------

@action
def modelNames(**_):
    return COL.models.all_names()


@action
def modelNamesAndIds(**_):
    return {nt["name"]: nt["id"] for nt in COL.models.all()}


@action
def modelFieldNames(modelName=None, **_):
    return COL.models.field_names(_notetype(modelName))


@action
def modelTemplates(modelName=None, **_):
    return {t["name"]: {"Front": t["qfmt"], "Back": t["afmt"]}
            for t in _notetype(modelName)["tmpls"]}


@action
def modelStyling(modelName=None, **_):
    return {"css": _notetype(modelName)["css"]}


@action
def updateModelTemplates(model=None, **_):
    nt = _notetype(model["name"])
    by_name = {t["name"]: t for t in nt["tmpls"]}
    for tmpl_name, sides in (model.get("templates") or {}).items():
        tmpl = by_name.get(tmpl_name)
        if tmpl is None:
            raise AnkiConnectError(f"template was not found: {tmpl_name}")
        if "Front" in sides:
            tmpl["qfmt"] = sides["Front"]
        if "Back" in sides:
            tmpl["afmt"] = sides["Back"]
    COL.models.update_dict(nt)
    return None


@action
def updateModelStyling(model=None, **_):
    nt = _notetype(model["name"])
    nt["css"] = model["css"]
    COL.models.update_dict(nt)
    return None


# --------------------------------------------------------------------------
# mídia e pacotes
# --------------------------------------------------------------------------

@action
def storeMediaFile(filename=None, data=None, path=None, deleteExisting=True, **_):
    if data is not None:
        raw = base64.b64decode(data)
    elif path is not None:
        raw = Path(path).read_bytes()
    else:
        raise AnkiConnectError("storeMediaFile precisa de data (base64) ou path")
    return COL.media.write_data(filename, raw)


@action
def retrieveMediaFile(filename=None, **_):
    target = Path(COL.media.dir()) / filename
    if not target.is_file():
        return False
    return base64.b64encode(target.read_bytes()).decode("ascii")


@action
def getMediaFilesNames(pattern="*", **_):
    return sorted(p.name for p in Path(COL.media.dir()).glob(pattern))


@action
def exportPackage(deck=None, path=None, includeSched=False, **_):
    COL.export_anki_package(
        out_path=path,
        options=ExportAnkiPackageOptions(
            with_scheduling=bool(includeSched),
            with_deck_configs=False,
            with_media=True,
            legacy=True,
        ),
        limit=DeckIdLimit(deck_id=_deck_id(deck)),
    )
    return True


@action
def importPackage(path=None, **_):
    COL.import_anki_package(ImportAnkiPackageRequest(
        package_path=str(Path(path).expanduser().resolve()),
        options=ImportAnkiPackageOptions(merge_notetypes=True, with_scheduling=True),
    ))
    return True


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

def _dispatch(name: str, params: dict) -> dict:
    handler = ACTIONS.get(name)
    if handler is None:
        return {"result": None, "error": f"unsupported action: {name}"}
    try:
        with LOCK:
            return {"result": handler(**(params or {})), "error": None}
    except AnkiConnectError as exc:
        return {"result": None, "error": str(exc)}
    except Exception as exc:  # noqa: BLE001
        traceback.print_exc()
        return {"result": None, "error": f"{type(exc).__name__}: {exc}"}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _send(self, payload: bytes, status: int = 200, ctype: str = "application/json") -> None:
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):  # noqa: N802
        self._send(b"", status=200, ctype="text/plain")

    def do_GET(self):  # noqa: N802
        self._send(b"AnkiConnect v.6 (nebli local shim)", ctype="text/plain")

    def do_POST(self):  # noqa: N802
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else b"{}"
        try:
            request = json.loads(body or b"{}")
        except json.JSONDecodeError as exc:
            self._send(json.dumps({"result": None, "error": f"invalid JSON: {exc}"}).encode())
            return
        response = _dispatch(request.get("action"), request.get("params") or {})
        if request.get("version", API_VERSION) < 6:
            response = response["result"]  # protocolo antigo: só o resultado cru
        self._send(json.dumps(response, ensure_ascii=False).encode("utf-8"))

    def log_message(self, fmt, *args):  # silencia o log por requisição
        pass


def main() -> int:
    global COL

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--collection", default=os.environ.get("NEBLI_ANKI_COLLECTION",
                                                           str(DEFAULT_COLLECTION)),
                    help="caminho do .anki2 (criado se não existir)")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--import", dest="imports", action="append", default=[], metavar="APKG",
                    help="semeia a coleção com um .apkg (repetível)")
    ap.add_argument("--expose-guid", action="store_true",
                    help="inclui guid no notesInfo (o AnkiConnect do Davi não inclui)")
    ap.add_argument("--allow-sync", action="store_true",
                    help="libera a ação sync (escreve na AnkiWeb de verdade)")
    args = ap.parse_args()

    OPTS.expose_guid = args.expose_guid
    OPTS.allow_sync = args.allow_sync

    path = Path(args.collection).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    fresh = not path.exists()
    COL = Collection(str(path))
    print(f"[ankiconnect_local] coleção: {path}{' (nova)' if fresh else ''}", flush=True)

    for apkg in args.imports:
        print(f"[ankiconnect_local] importando {apkg} ...", flush=True)
        importPackage(path=apkg)

    print(f"[ankiconnect_local] notas: {COL.note_count()} | cards: {COL.card_count()} | "
          f"decks: {len(COL.decks.all_names_and_ids())}", flush=True)

    server = ThreadingHTTPServer((args.host, args.port), Handler)
    server.daemon_threads = True
    print(f"[ankiconnect_local] ouvindo em http://{args.host}:{args.port} "
          f"({len(ACTIONS)} ações; sync {'ON' if OPTS.allow_sync else 'OFF'})", flush=True)

    def shutdown(*_):
        threading.Thread(target=server.shutdown, daemon=True).start()

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    try:
        server.serve_forever()
    finally:
        with LOCK:
            COL.close()
        print("[ankiconnect_local] coleção fechada.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
