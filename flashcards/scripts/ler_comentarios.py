#!/usr/bin/env python3
"""ler_comentarios.py — canal de comentários card-a-card do Davi p/ o Claude.

Um comentário pode chegar de dois jeitos: pelo add-on `nebli_comentarios` (Anki
desktop), que aplica a tag `NEBLI_comentario::pendente`, ou digitado direto no
campo `NEBLI_Comentario` no AnkiDroid — que **não aplica tag nenhuma**.

Este script procura os dois. Antes ele só consultava a tag, e por isso os
comentários escritos no celular ficavam invisíveis ao pipeline: no `.apkg` de
2026-08-17 havia sete comentários reais e nenhum tinha a tag.

  • (default) lista TODO comentário não respondido — frente do card + comentário.
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


def pendentes():
    """Notas com comentário a responder, por tag **ou** por campo preenchido.

    Um comentário só sai da lista quando existe resposta: a tag `respondido`
    sozinha não basta, porque quem digita no AnkiDroid nunca mexe em tag.
    """
    ids = set(call("findNotes", query='tag:"%s"' % PENDING))
    ids |= set(call("findNotes", query='"%s:_*"' % CFIELD))
    if not ids:
        return []
    out = []
    for note in call("notesInfo", notes=sorted(ids)):
        fields = note.get("fields", {})
        comment = plain(fields.get(CFIELD, {}).get("value", ""))
        answered = plain(fields.get(AFIELD, {}).get("value", ""))
        tags = note.get("tags", []) or []
        if not comment:
            continue
        if answered and DONE in tags:
            continue
        note["_comment"] = comment
        note["_answered"] = answered
        note["_untagged"] = PENDING not in tags
        out.append(note)
    return out


def listar():
    notes = pendentes()
    if not notes:
        print("Nenhum comentário pendente. ✔")
        return
    untagged = sum(1 for n in notes if n["_untagged"])
    print("=" * 70)
    print("COMENTÁRIOS PENDENTES: %d (%d sem tag, digitados no AnkiDroid)" % (len(notes), untagged))
    print("=" * 70)
    for n in notes:
        fields = n["fields"]
        front = plain(list(fields.values())[0]["value"])[:160]
        print("\n• noteId=%d  [%s]%s" % (n["noteId"], n["modelName"], "  (sem tag)" if n["_untagged"] else ""))
        print("  CARD : %s" % front)
        print("  DAVI : %s" % n["_comment"])
        if n["_answered"]:
            print("  JÁ RESPONDIDO : %s" % n["_answered"])
    print("\n" + "-" * 70)
    print("Responder: python ler_comentarios.py --responder <noteId> \"sua resposta\"")


def responder(note_id, texto):
    """Grava a resposta **sem nunca apagar o comentário**.

    Pedido explícito do usuário: "não apaga eles, vai mantendo, mesmo que
    estejam corrigidos, porque daí uma hora reúnos e vemos seus erros mais
    frequentes". O comentário é o corpus de padrões — só cresce.
    """
    info = call("notesInfo", notes=[note_id])
    if not info:
        sys.exit("noteId %s não encontrado." % note_id)
    fields = info[0].get("fields", {})
    comentario = fields.get(CFIELD, {}).get("value", "")
    if not plain(comentario):
        sys.exit("noteId %s não tem comentário para responder." % note_id)
    anterior = fields.get(AFIELD, {}).get("value", "")
    resposta = texto if not plain(anterior) else anterior + "<br>" + texto
    call("updateNoteFields", note={"id": note_id, "fields": {AFIELD: resposta}})
    call("addTags", notes=[note_id], tags=DONE)
    call("removeTags", notes=[note_id], tags=PENDING)
    print("Respondido noteId=%d ✔ (comentário preservado, %s acumulado)" % (note_id, AFIELD))


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
