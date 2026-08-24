"""Backend de coleção local — fala com o Anki SEM AnkiConnect.

Opera a coleção diretamente pela lib oficial (`pip install anki`), sincronizada
com o AnkiWeb. É isto que permite curadoria AnKing e deck injection a partir de
uma sessão na nuvem (tablet), com o PC do Davi desligado.

A superfície pública imita o AnkiConnect ação por ação, para que os ~32 scripts
de `flashcards/scripts/` não precisem saber por onde estão falando:

    from anki_collection_backend import call
    call("findNotes", query="tag:NEBLI::*")

Credencial (NUNCA no git — env var do environment, como NEBLI_DRIVE_SA_JSON):
    ANKIWEB_HKEY                 token de sync (preferido; não é a senha)
    ANKIWEB_USER / ANKIWEB_PASS  alternativa; o 1o login imprime o hkey p/ salvar

Controle:
    NEBLI_ANKI_DIR         onde mora a coleção local (default ~/.nebli-anki)
    NEBLI_ANKI_SYNC_MEDIA  1 = baixa mídia (pesado; exigido p/ Image Occlusion)
    NEBLI_ANKI_AUTOSYNC    0 = não sincroniza de volta no fim do processo
    NEBLI_ANKI_OFFLINE     1 = abre a coleção local sem tocar no AnkiWeb (testes)

Regra de segurança dura: um sync que exigiria FULL_UPLOAD ou FULL_SYNC **aborta**.
A sessão na nuvem nunca decide sozinha qual lado da coleção sobrevive.
"""
from __future__ import annotations

import atexit
import base64
import os
import sys
import time
from pathlib import Path

_COL = None          # anki.collection.Collection
_AUTH = None         # SyncAuth
_DIRTY = False       # houve escrita desde o último sync?
_OPENING = False


# --------------------------------------------------------------------------
# infraestrutura: lib, credencial, coleção, sync
# --------------------------------------------------------------------------
def _lib():
    """Importa a lib oficial. anki.collection PRIMEIRO (import circular)."""
    from anki.collection import Collection  # noqa: F401
    import anki.collection as ac
    return ac


def _dir() -> Path:
    d = Path(os.environ.get("NEBLI_ANKI_DIR") or (Path.home() / ".nebli-anki"))
    d.mkdir(parents=True, exist_ok=True)
    return d


def _hkey_cache() -> Path:
    return _dir() / "hkey"


def _auth():
    """SyncAuth a partir de hkey (preferido) ou usuário+senha."""
    global _AUTH
    if _AUTH is not None:
        return _AUTH
    ac = _lib()
    endpoint = os.environ.get("ANKIWEB_ENDPOINT") or None

    hkey = os.environ.get("ANKIWEB_HKEY") or ""
    if not hkey and _hkey_cache().exists():
        hkey = _hkey_cache().read_text().strip()
    if hkey:
        _AUTH = ac.SyncAuth(hkey=hkey, endpoint=endpoint)
        return _AUTH

    user = os.environ.get("ANKIWEB_USER")
    pwd = os.environ.get("ANKIWEB_PASS")
    if user and pwd:
        col = _col_only()
        _AUTH = col.sync_login(user, pwd, endpoint)
        cache = _hkey_cache()
        cache.write_text(_AUTH.hkey)
        os.chmod(cache, 0o600)
        print(
            "[anki] login OK. Guarde este token como env var do environment "
            "e a senha nunca mais é necessária:\n"
            f"       ANKIWEB_HKEY={_AUTH.hkey}",
            file=sys.stderr,
        )
        return _AUTH

    raise RuntimeError(
        "Sem credencial do AnkiWeb. Defina ANKIWEB_HKEY (preferido) ou "
        "ANKIWEB_USER + ANKIWEB_PASS. Nenhum dos dois vai para o git."
    )


def _col_only():
    """Abre a coleção local sem sincronizar (usado pelo próprio login)."""
    global _COL
    if _COL is None:
        ac = _lib()
        _COL = ac.Collection(str(_dir() / "collection.anki2"))
    return _COL


def _sync(initial: bool) -> str:
    """Sincroniza com o AnkiWeb. Aborta se o servidor exigir decisão humana."""
    ac = _lib()
    col = _col_only()
    out = col.sync_collection(_auth(), os.environ.get("NEBLI_ANKI_SYNC_MEDIA") == "1")
    req = out.required
    R = ac.SyncOutput.ChangesRequired

    if req in (R.NO_CHANGES, R.NORMAL_SYNC):
        return "ok"

    if req == R.FULL_DOWNLOAD and initial:
        # Coleção local nova/vazia: baixar do servidor é seguro (servidor -> cliente).
        col.full_upload_or_download(
            auth=_auth(), server_usn=out.server_media_usn, upload=False
        )
        return "full_download"

    raise RuntimeError(
        "SYNC BLOQUEADO: o AnkiWeb pediu "
        f"{R.Name(req)}. Isso significa que a coleção daqui e a do servidor "
        "divergiram a ponto de um lado ter que sobrescrever o outro — e esta "
        "sessão não decide isso sozinha.\n"
        "Caminho seguro: sincronize o PC/celular com o AnkiWeb, depois apague a "
        f"coleção local desta sessão ({_dir()}/collection.anki2) para baixar "
        "de novo do zero. Se o servidor é que está desatualizado, faça o upload "
        "pelo Anki do PC, não por aqui."
    )


def col():
    """Coleção aberta e sincronizada (abre na primeira vez que alguém precisa)."""
    global _COL, _OPENING
    if _COL is not None and not _OPENING:
        return _COL
    path = _dir() / "collection.anki2"
    fresh = not path.exists()
    _OPENING = True
    try:
        c = _col_only()
        if os.environ.get("NEBLI_ANKI_OFFLINE") != "1":
            t0 = time.time()
            how = _sync(initial=fresh)
            if how == "full_download" or fresh:
                print(
                    f"[anki] coleção baixada do AnkiWeb em {time.time() - t0:.0f}s",
                    file=sys.stderr,
                )
    finally:
        _OPENING = False
    return c


def _touch():
    global _DIRTY
    _DIRTY = True


@atexit.register
def _flush():
    """Devolve as mudanças ao AnkiWeb no fim do processo."""
    global _COL
    if _COL is None:
        return
    try:
        if _DIRTY and os.environ.get("NEBLI_ANKI_AUTOSYNC") != "0" \
                and os.environ.get("NEBLI_ANKI_OFFLINE") != "1":
            _sync(initial=False)
            print("[anki] mudanças sincronizadas com o AnkiWeb", file=sys.stderr)
    except Exception as e:  # nunca derruba o processo no atexit
        print(f"[anki] AVISO: sync final falhou ({e}) — mudanças seguem locais "
              f"em {_dir()}/collection.anki2", file=sys.stderr)
    finally:
        try:
            _COL.close()
        except Exception:
            pass
        _COL = None


# --------------------------------------------------------------------------
# ações — mesma superfície do AnkiConnect (mesmos nomes, params e retornos)
# --------------------------------------------------------------------------
def _note_dict(n) -> dict:
    nt = n.note_type()
    names = [f["name"] for f in nt["flds"]]
    return {
        "noteId": int(n.id),
        "guid": n.guid,  # o AnkiConnect NÃO expõe isto; aqui o casamento é exato
        "modelName": nt["name"],
        "tags": list(n.tags),
        "fields": {nm: {"value": n.fields[i], "order": i} for i, nm in enumerate(names)},
        "cards": [int(c) for c in n.card_ids()],
        "mod": n.mod,
    }


def _card_dict(c) -> dict:
    n = c.note()
    nt = n.note_type()
    names = [f["name"] for f in nt["flds"]]
    did = c.odid or c.did
    return {
        "cardId": int(c.id),
        "note": int(c.nid),
        "deckName": col().decks.name(did),
        "modelName": nt["name"],
        "fields": {nm: {"value": n.fields[i], "order": i} for i, nm in enumerate(names)},
        "ord": c.ord,
        "type": c.type,
        "queue": c.queue,
        "due": c.due,
        "ivl": c.ivl,
        "factor": c.factor,
        "reps": c.reps,
        "lapses": c.lapses,
        "flags": c.flags,
        "mod": c.mod,
    }


def _model(name):
    m = col().models.by_name(name)
    if m is None:
        raise RuntimeError(f"model was not found: {name}")
    return m


A = {}


def _act(fn):
    A[fn.__name__.lstrip("_")] = fn
    return fn


# --- leitura ---
@_act
def version(**_):
    return 6


@_act
def findNotes(query="", **_):
    return [int(i) for i in col().find_notes(query)]


@_act
def findCards(query="", **_):
    return [int(i) for i in col().find_cards(query)]


@_act
def notesInfo(notes=(), **_):
    c = col()
    return [_note_dict(c.get_note(int(i))) for i in notes]


@_act
def cardsInfo(cards=(), **_):
    c = col()
    return [_card_dict(c.get_card(int(i))) for i in cards]


@_act
def cardsToNotes(cards=(), **_):
    c = col()
    return sorted({int(c.get_card(int(i)).nid) for i in cards})


@_act
def cardsFromNotes(notes=(), **_):
    c = col()
    out = []
    for i in notes:
        out.extend(int(x) for x in c.get_note(int(i)).card_ids())
    return out


@_act
def areSuspended(cards=(), **_):
    c = col()
    return [c.get_card(int(i)).queue == -1 for i in cards]


@_act
def deckNames(**_):
    return [d.name for d in col().decks.all_names_and_ids()]


@_act
def modelNames(**_):
    return [m.name for m in col().models.all_names_and_ids()]


@_act
def modelFieldNames(modelName="", **_):
    return col().models.field_names(_model(modelName))


@_act
def modelTemplates(modelName="", **_):
    return {t["name"]: {"Front": t["qfmt"], "Back": t["afmt"]}
            for t in _model(modelName)["tmpls"]}


@_act
def getDeckConfig(deck="", **_):
    c = col()
    did = c.decks.id(deck, create=False)
    if did is None:
        raise RuntimeError(f"deck was not found: {deck}")
    return c.decks.config_dict_for_deck_id(did)


@_act
def getNumCardsReviewedByDay(**_):
    c = col()
    rollover = c.get_config("rollover", 4) or 4
    rows = c.db.all(
        "select strftime('%Y-%m-%d', (id/1000 - ?), 'unixepoch') d, count() "
        "from revlog group by d order by d desc", rollover * 3600)
    return [[d, n] for d, n in rows]


# --- escrita: notas ---
@_act
def addNote(note=None, **_):
    return addNotes(notes=[note])[0]


@_act
def addNotes(notes=(), **_):
    c = col()
    out = []
    for spec in notes:
        try:
            nt = _model(spec["modelName"])
            n = c.new_note(nt)
            for k, v in (spec.get("fields") or {}).items():
                n[k] = v
            for t in (spec.get("tags") or []):
                n.add_tag(t)
            opts = spec.get("options") or {}
            if not opts.get("allowDuplicate") and n.duplicate_or_empty() == 2:
                out.append(None)
                continue
            did = c.decks.id(spec["deckName"])
            c.add_note(n, did)
            _touch()
            out.append(int(n.id))
        except Exception:
            out.append(None)
    return out


@_act
def updateNoteFields(note=None, **_):
    c = col()
    n = c.get_note(int(note["id"]))
    for k, v in (note.get("fields") or {}).items():
        n[k] = v
    c.update_note(n)
    _touch()
    return None


@_act
def deleteNotes(notes=(), **_):
    col().remove_notes([int(i) for i in notes])
    _touch()
    return None


@_act
def addTags(notes=(), tags="", **_):
    col().tags.bulk_add([int(i) for i in notes], tags)
    _touch()
    return None


@_act
def removeTags(notes=(), tags="", **_):
    col().tags.bulk_remove([int(i) for i in notes], tags)
    _touch()
    return None


# --- escrita: cards ---
@_act
def suspend(cards=(), **_):
    col().sched.suspend_cards([int(i) for i in cards])
    _touch()
    return True


@_act
def unsuspend(cards=(), **_):
    col().sched.unsuspend_cards([int(i) for i in cards])
    _touch()
    return True


@_act
def changeDeck(cards=(), deck="", **_):
    c = col()
    c.set_deck([int(i) for i in cards], c.decks.id(deck))
    _touch()
    return None


@_act
def setFlag(cards=(), flag=0, **_):
    col().set_user_flag_for_cards(int(flag), [int(i) for i in cards])
    _touch()
    return None


_SETTABLE = {"flags", "due", "ivl", "factor", "reps", "lapses", "queue", "type", "mod"}


@_act
def setSpecificValueOfCard(card=None, keys=(), newValues=(), **_):
    c = col()
    cd = c.get_card(int(card))
    for k, v in zip(keys, newValues):
        if k not in _SETTABLE:
            raise RuntimeError(f"campo de card não permitido aqui: {k}")
        setattr(cd, k, int(v) if str(v).lstrip("-").isdigit() else v)
    c.update_card(cd)
    _touch()
    return [True] * len(list(keys))


# --- decks e modelos ---
@_act
def createDeck(deck="", **_):
    did = col().decks.id(deck)
    _touch()
    return int(did)


@_act
def deleteDecks(decks=(), cardsToo=False, **_):
    if not cardsToo:
        raise RuntimeError(
            "deleteDecks sem cardsToo=True não é suportado: o Anki moderno não "
            "sabe mais apagar um deck preservando os cards.")
    c = col()
    dids = [d for d in (c.decks.id(n, create=False) for n in decks) if d is not None]
    c.decks.remove(dids)
    _touch()
    return None


@_act
def saveDeckConfig(config=None, **_):
    col().decks.update_config(config)
    _touch()
    return True


@_act
def updateModelTemplates(model=None, **_):
    c = col()
    m = _model(model["name"])
    for tname, sides in (model.get("templates") or {}).items():
        for t in m["tmpls"]:
            if t["name"] == tname:
                if "Front" in sides:
                    t["qfmt"] = sides["Front"]
                if "Back" in sides:
                    t["afmt"] = sides["Back"]
    c.models.update_dict(m)
    _touch()
    return None


@_act
def updateModelStyling(model=None, **_):
    c = col()
    m = _model(model["name"])
    m["css"] = model["css"]
    c.models.update_dict(m)
    _touch()
    return None


# --- mídia, export, sync ---
@_act
def storeMediaFile(filename="", data="", **_):
    raw = base64.b64decode(data)
    name = col().media.write_data(filename, raw)
    _touch()
    return name


@_act
def retrieveMediaFile(filename="", **_):
    p = Path(col().media.dir()) / filename
    if not p.exists():
        return False
    return base64.b64encode(p.read_bytes()).decode()


@_act
def exportPackage(deck="", path="", includeSched=False, **_):
    ac = _lib()
    c = col()
    did = c.decks.id(deck, create=False)
    if did is None:
        raise RuntimeError(f"deck was not found: {deck}")
    if os.environ.get("NEBLI_ANKI_SYNC_MEDIA") != "1":
        print("[anki] AVISO: exportando .apkg sem mídia sincronizada — cards de "
              "Image Occlusion sairão sem imagem. Rode com "
              "NEBLI_ANKI_SYNC_MEDIA=1 se o deck tiver figuras.", file=sys.stderr)
    c.export_anki_package(
        out_path=path,
        options=ac.ExportAnkiPackageOptions(
            with_scheduling=bool(includeSched), with_deck_configs=False,
            with_media=True, legacy=True),
        limit=ac.DeckIdLimit(deck_id=did),
    )
    return True


@_act
def sync(**_):
    col()
    _sync(initial=False)
    global _DIRTY
    _DIRTY = False
    return None


@_act
def multi(actions=(), **_):
    out = []
    for a in actions:
        try:
            out.append(call(a["action"], **(a.get("params") or {})))
        except Exception as e:
            out.append({"error": str(e)})
    return out


@_act
def guiCurrentCard(**_):
    raise RuntimeError(
        "guiCurrentCard não existe sem o Anki aberto na tela — esta sessão opera "
        "a coleção headless. Use findCards/cardsInfo para chegar no card.")


def call(action, **params):
    fn = A.get(action)
    if fn is None:
        raise RuntimeError(
            f"ação '{action}' ainda não implementada no backend de coleção. "
            f"Implementadas: {', '.join(sorted(A))}")
    return fn(**params)
