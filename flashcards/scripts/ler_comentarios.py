#!/usr/bin/env python3
"""ler_comentarios.py — canal de comentários card-a-card do Davi p/ o Claude.

O add-on `nebli_comentarios` (Anki desktop) e/ou a digitação direta no campo
`NEBLI_Comentario` (AnkiDroid) marcam cada card comentado com a tag
`NEBLI_comentario::pendente`. Este script:

  • (default) lista TODOS os comentários pendentes — frente do card + o comentário —
    pra o Claude ler e responder no chat.
  • --responder <noteId> "<texto>"  grava a resposta no campo `NEBLI_Resposta`,
    troca a tag `pendente`→`respondido`. (Também vai pro card, então o Davi vê a
    resposta ao revisar / no Browser.)
  • --sync  puxa do AnkiWeb antes de ler (comentários feitos no celular/desktop).

Rode depois de `--sync` pra pegar o que o Davi comentou desde a última vez.
"""
import argparse
import json
import re
import sys
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PENDING = "NEBLI_comentario::pendente"
DONE = "NEBLI_comentario::respondido"
CFIELD = "NEBLI_Comentario"
AFIELD = "NEBLI_Resposta"


def call(action, **params):
    req = urllib.request.Request(
        "http://localhost:8765",
        data=json.dumps({"action": action, "version": 6, "params": params}).encode(),
        headers={"Content-Type": "application/json"},
    )
    r = json.load(urllib.request.urlopen(req))
    if r.get("error"):
        sys.exit("ERRO %s: %s" % (action, r["error"]))
    return r["result"]


def plain(html):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", html or "")).strip()


def listar():
    ids = call("findNotes", query='tag:"%s"' % PENDING)
    if not ids:
        print("Nenhum comentário pendente. ✔")
        return
    info = call("notesInfo", notes=ids)
    print("=" * 70)
    print("COMENTÁRIOS PENDENTES: %d" % len(ids))
    print("=" * 70)
    for n in info:
        fields = n["fields"]
        front = plain(list(fields.values())[0]["value"])[:160]
        comment = plain(fields.get(CFIELD, {}).get("value", ""))
        print("\n• noteId=%d  [%s]" % (n["noteId"], n["modelName"]))
        print("  CARD : %s" % front)
        print("  DAVI : %s" % comment)
    print("\n" + "-" * 70)
    print("Responder: python ler_comentarios.py --responder <noteId> \"sua resposta\"")


def responder(note_id, texto):
    info = call("notesInfo", notes=[note_id])
    if not info:
        sys.exit("noteId %s não encontrado." % note_id)
    call("updateNoteFields", note={"id": note_id, "fields": {AFIELD: texto}})
    call("addTags", notes=[note_id], tags=DONE)
    call("removeTags", notes=[note_id], tags=PENDING)
    print("Respondido noteId=%d ✔ (tag pendente→respondido, campo %s gravado)" % (note_id, AFIELD))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sync", action="store_true", help="sync AnkiWeb antes de ler")
    ap.add_argument("--responder", nargs=2, metavar=("noteId", "texto"))
    a = ap.parse_args()
    if a.sync:
        call("sync")
        print("Sync feito.\n")
    if a.responder:
        responder(int(a.responder[0]), a.responder[1])
    else:
        listar()


if __name__ == "__main__":
    main()
