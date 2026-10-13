"""Zera o histórico de estudo da coleção (pedido de Davi em 02/10/2026).

Roda só com o Anki fechado. Apaga o revlog, devolve ao estado de novo todo card com
agendamento ou memória FSRS (mantendo suspensão, bandeiras, deck e conteúdo), zera os
contadores diários dos decks e marca a coleção para envio completo ao AnkiWeb.
"""
import json
import shutil
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

COL = Path.home() / "Library/Application Support/Anki2/User 1/collection.anki2"
HERE = Path(__file__).parent
SNAPSHOT = HERE / "collection-pos-sync-antes-do-reset.anki2"
ALVO = "type != 0 or reps > 0 or lapses > 0 or data not in ('', '{}')"
CONTADORES = {4, 5, 6, 7}  # DeckCommon: new/review/learning/milliseconds studied


def varint(buf, i):
    value = shift = 0
    while True:
        byte = buf[i]
        i += 1
        value |= (byte & 0x7F) << shift
        shift += 7
        if byte < 0x80:
            return value, i


def sem_contadores(common):
    """Copia o protobuf DeckCommon byte a byte, sem os campos de estudo do dia."""
    out, i = bytearray(), 0
    while i < len(common):
        start = i
        key, i = varint(common, i)
        field, wire = key >> 3, key & 7
        if wire == 0:
            _, i = varint(common, i)
        elif wire == 2:
            size, i = varint(common, i)
            i += size
        elif wire == 5:
            i += 4
        elif wire == 1:
            i += 8
        else:
            raise ValueError(f"wire type {wire} inesperado")
        if field not in CONTADORES:
            out += common[start:i]
    return bytes(out)


def conectar(path):
    con = sqlite3.connect(path, isolation_level=None)
    con.create_collation("unicase", lambda a, b: (a.lower() > b.lower()) - (a.lower() < b.lower()))
    return con


def retrato(con):
    one = lambda sql: con.execute(sql).fetchone()[0]
    return {
        "revlog": one("select count(*) from revlog"),
        "cards": one("select count(*) from cards"),
        "notes": one("select count(*) from notes"),
        "suspensos": one("select count(*) from cards where queue = -1"),
        "com_bandeira": one("select count(*) from cards where flags & 7 != 0"),
        "com_agendamento": one(f"select count(*) from cards where {ALVO}"),
        "novos": one("select count(*) from cards where type = 0"),
        "scm": one("select scm from col"),
    }


def main():
    if subprocess.run(["pgrep", "-f", "Anki.app/Contents/MacOS/Anki"], capture_output=True).returncode == 0:
        sys.exit("Anki aberto: nada foi escrito.")
    if COL.with_name(COL.name + "-wal").exists():
        sys.exit("WAL pendente: nada foi escrito.")
    if SNAPSHOT.exists():
        sys.exit(f"{SNAPSHOT.name} já existe: nada foi escrito.")
    shutil.copy2(COL, SNAPSHOT)

    con = conectar(COL)
    antes = retrato(con)
    identidade = con.execute("select count(*), sum(id), sum(nid), sum(did), sum(flags) from cards").fetchone()
    agora = int(time.time())
    con.execute("begin immediate")
    try:
        con.execute("delete from revlog")
        linhas = con.execute(f"select id, queue, due, data from cards where {ALVO} order by due, id").fetchall()
        prox = int(con.execute("select val from config where key = 'nextPos'").fetchone()[0])
        for cid, queue, due, data in linhas:
            pos = (json.loads(data) if data else {}).get("pos")
            if pos is None:
                pos, prox = prox, prox + 1
            con.execute(
                "update cards set type = 0, queue = ?, due = ?, ivl = 0, factor = 0, reps = 0, lapses = 0,"
                " left = 0, odue = 0, data = '', mod = ?, usn = -1 where id = ?",
                (-1 if queue == -1 else 0, pos, agora, cid),
            )
        con.execute("update config set val = ?, mtime_secs = ?, usn = -1 where key = 'nextPos'",
                    (str(prox).encode(), agora))
        decks = 0
        for did, common in con.execute("select id, common from decks").fetchall():
            limpo = sem_contadores(common)
            if limpo != common:
                con.execute("update decks set common = ?, mtime_secs = ?, usn = -1 where id = ?",
                            (limpo, agora, did))
                decks += 1
        con.execute("update col set scm = ?, mod = ?", (agora * 1000, agora * 1000))

        depois = retrato(con)
        assert depois["revlog"] == 0 and depois["com_agendamento"] == 0
        assert depois["novos"] == depois["cards"] == antes["cards"]
        assert depois["notes"] == antes["notes"]
        assert depois["suspensos"] == antes["suspensos"]
        assert depois["com_bandeira"] == antes["com_bandeira"]
        assert identidade == con.execute(
            "select count(*), sum(id), sum(nid), sum(did), sum(flags) from cards").fetchone()
        assert con.execute("pragma integrity_check").fetchone()[0] == "ok"
        con.execute("commit")
    except BaseException:
        con.execute("rollback")
        raise
    con.close()
    registro = {"antes": antes, "depois": depois, "cards_resetados": len(linhas),
                "decks_com_contador_zerado": decks, "snapshot": SNAPSHOT.name, "aplicado_em": agora}
    (HERE / "registro.json").write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(registro, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
