"""Helper de Anki do NEBLI — escolhe sozinho por onde falar com a coleção.

Dois transportes, mesma função `call(action, **params)`:

  * **connect**    — HTTP para o AnkiConnect (`localhost:8765`), o Anki aberto no
                     PC do Davi. É o caminho de sempre; nada mudou para ele.
  * **collection** — a coleção pela lib oficial `anki`, sincronizada com o
                     AnkiWeb (`anki_collection_backend.py`). É o que faz curadoria
                     AnKing e deck injection funcionarem de uma sessão na nuvem,
                     pelo tablet, com o PC desligado.

`auto` (default) usa o AnkiConnect quando ele responde e cai no backend de
coleção quando não. Force com NEBLI_ANKI_BACKEND=connect|collection.

Este módulo se chamava `anki.py`. Foi renomeado porque um arquivo com esse nome
ao lado dos scripts **sombreia a lib oficial `anki`** e torna o backend de
coleção impossível de importar.
"""
import json
import os
import sys
import urllib.error
import urllib.request

ANKICONNECT_URL = os.environ.get("ANKICONNECT_URL", "http://localhost:8765")
_BACKEND = None


def _post(action, params, timeout):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(ANKICONNECT_URL, payload,
                                 {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=timeout))
    if r.get("error"):
        raise RuntimeError(f"AnkiConnect error [{action}]: {r['error']}")
    return r["result"]


def _connect_alive():
    try:
        _post("version", {}, 1.5)
        return True
    except Exception:
        return False


def backend():
    """'connect' ou 'collection' — decidido uma vez por processo."""
    global _BACKEND
    if _BACKEND:
        return _BACKEND
    want = (os.environ.get("NEBLI_ANKI_BACKEND") or "auto").lower()
    if want in ("connect", "collection"):
        _BACKEND = want
    else:
        _BACKEND = "connect" if _connect_alive() else "collection"
        if _BACKEND == "collection":
            print("[anki] AnkiConnect não respondeu — operando a coleção via "
                  "AnkiWeb (modo nuvem/tablet).", file=sys.stderr)
    return _BACKEND


def call(action, **params):
    if backend() == "collection":
        from anki_collection_backend import call as _c
        return _c(action, **params)

    last = None
    for _ in range(4):
        try:
            return _post(action, params, 25)
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
    raise last


if __name__ == "__main__":
    print("backend:", backend(), "| version:", call("version"))
    print("decks:", len(call("deckNames")))
