"""Exporta uma UC viva e prepara APKG comprimido sem bandeiras, sem editar Anki.

Suporta o formato SQLite legado produzido por exportPackage do AnkiConnect.
Formatos modernos .anki21b são recusados, nunca convertidos por adivinhação.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import tempfile
import urllib.request
import zipfile
from contextlib import closing
from pathlib import Path

from nebli.preflight import ReadOnlyAnki, deck_query


def sha256(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def db_state(connection):
    """Fingerprint lógico completo exceto os três bits de bandeira visível."""
    digest = hashlib.sha256()
    tables = connection.execute(
        "select name from sqlite_master where type='table' order by name").fetchall()
    for (table,) in tables:
        quoted = '"' + table.replace('"', '""') + '"'
        columns = [r[1] for r in connection.execute(f"pragma table_info({quoted})")]
        flag_index = columns.index("flags") if table == "cards" else None
        rows = []
        for row in connection.execute(f"select * from {quoted}"):
            values = list(row)
            if flag_index is not None:
                values[flag_index] &= ~7
            rows.append(repr(tuple(values)))
        digest.update((table + "\n" + "\n".join(sorted(rows))).encode())
    return digest.hexdigest()


def prepare_package(source, output, expected_card_ids=None, target_deck=None):
    source, output = Path(source).resolve(), Path(output).resolve()
    if source == output or output.exists():
        raise ValueError("Fonte e saída precisam ser distintas; não sobrescrever pacote existente.")
    if output.suffix.lower() != ".apkg" or output.name.lower() == "collection.apkg":
        raise ValueError("Use nome de deck UC terminado em .apkg, nunca collection.apkg.")
    original_hash = sha256(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="nebli-package-", dir=output.parent) as temp_dir:
        temporary = Path(temp_dir)
        with zipfile.ZipFile(source) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise ValueError("Pacote com entradas duplicadas.")
            if "collection.anki21b" in names or not ({"collection.anki2", "collection.anki21"} & set(names)):
                raise ValueError("Formato não suportado: exporte APKG legado pelo AnkiConnect.")
            bad = archive.testzip()
            if bad:
                raise ValueError(f"ZIP inválido: {bad}")
            media = json.loads(archive.read("media"))
            if not isinstance(media, dict) or any(key not in names for key in media):
                raise ValueError("Mapa de mídia inválido/incompleto.")
            main_db = "collection.anki21" if "collection.anki21" in names else "collection.anki2"
            states = {}
            replacements = {}
            for name in ("collection.anki2", "collection.anki21"):
                if name not in names:
                    continue
                path = temporary / name
                with path.open("wb") as handle:
                    handle.write(archive.read(name))
                with closing(sqlite3.connect(path)) as connection:
                    if connection.execute("pragma integrity_check").fetchone()[0] != "ok":
                        raise ValueError("Coleção exportada inválida.")
                    before = db_state(connection)
                    ids = {row[0] for row in connection.execute("select id from cards")}
                    flagged = connection.execute("select count(*) from cards where flags & 7 != 0").fetchone()[0]
                    if name == main_db:
                        if not ids:
                            raise ValueError("UC vazia: não publicar pacote vazio.")
                        if expected_card_ids is not None and ids != set(expected_card_ids):
                            raise ValueError("Cards do pacote diferem da seleção viva da UC.")
                        if target_deck:
                            decks = json.loads(connection.execute("select decks from col").fetchone()[0])
                            allowed = {int(did) for did, deck in decks.items()
                                       if deck["name"] == target_deck or deck["name"].startswith(target_deck + "::")}
                            actual = {r[0] for r in connection.execute("select distinct did from cards")}
                            if not actual.issubset(allowed):
                                raise ValueError("Pacote contém cards fora da UC solicitada.")
                    connection.execute("update cards set flags = flags & ~7")
                    connection.commit()
                    if db_state(connection) != before:
                        raise ValueError("Conteúdo/agendamento alterado além das bandeiras.")
                    if connection.execute("select count(*) from cards where flags & 7 != 0").fetchone()[0]:
                        raise ValueError("Bandeiras remanescentes.")
                    states[name] = {"cards": len(ids), "cleared_flags": flagged, "logical_fingerprint": before}
                replacements[name] = path
            candidate = temporary / "candidate.apkg"
            with zipfile.ZipFile(candidate, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as destination:
                for item in archive.infolist():
                    with destination.open(item.filename, "w", force_zip64=True) as target:
                        if item.filename in replacements:
                            with replacements[item.filename].open("rb") as stream:
                                shutil.copyfileobj(stream, target)
                        else:
                            with archive.open(item) as stream:
                                shutil.copyfileobj(stream, target)
            with zipfile.ZipFile(candidate) as check:
                if check.testzip() or set(check.namelist()) != set(names):
                    raise ValueError("Pacote final inválido.")
                if any(i.compress_type != zipfile.ZIP_DEFLATED for i in check.infolist()):
                    raise ValueError("Compressão não aplicada.")
                for name in names:
                    if name not in replacements and check.read(name) != archive.read(name):
                        raise ValueError(f"Mídia/metadado alterado: {name}")
            if sha256(source) != original_hash:
                raise ValueError("Fonte mudou durante a operação.")
            with output.open("xb") as target, candidate.open("rb") as stream:
                shutil.copyfileobj(stream, target)
    return {"status": "verified", "source_sha256": original_hash,
            "output": str(output), "output_sha256": sha256(output),
            "source_bytes": source.stat().st_size, "output_bytes": output.stat().st_size,
            "compression": "ZIP_DEFLATED level 9", "visible_flags": 0,
            "media_files": len(media), "databases": states,
            "preserved": "fields, GUIDs, IDs, templates, media, scheduling present in source"}


def live_snapshot(call, deck):
    query = deck_query(deck)
    ids = sorted(call("findCards", query=query))
    flags = {str(flag): sorted(call("findCards", query=f"{query} flag:{flag}")) for flag in range(8)}
    return {"card_ids": ids, "flags": flags}


def export_uc(uc, output, endpoint="http://127.0.0.1:8765"):
    if not re.fullmatch(r"UC\d{2}", uc):
        raise ValueError("UC deve ter formato UC03; nunca exportar a coleção inteira.")
    output = Path(output).resolve()
    receipt = output.with_suffix(".publication-ready.json")
    if output.exists() or receipt.exists():
        raise ValueError("Use uma pasta de execução nova; saída/recibo já existem.")
    call = ReadOnlyAnki(endpoint)
    profile = call("getActiveProfile")  # se ausente, falhar; confirmar por outro caminho antes de usar
    deck = "NEBLI::" + uc
    before = live_snapshot(call, deck)
    if not before["card_ids"]:
        raise ValueError("UC vazia: nada a publicar; não restaurar pacotes históricos.")
    existing_decks = call("deckNames")
    candidates = sorted((name for name in existing_decks
                         if name == deck or name.startswith(deck + "::")), key=len)
    export_deck = next((name for name in candidates
                        if sorted(call("findCards", query=deck_query(name))) == before["card_ids"]), None)
    if not export_deck:
        raise ValueError("Não há deck-pai real que reúna a UC; criar a hierarquia correta na geração, sem exportar subconjunto.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="nebli-export-", dir=output.parent) as directory:
        raw = Path(directory) / f"{uc}-raw.apkg"
        body = json.dumps({"action": "exportPackage", "version": 6, "params": {
            "deck": export_deck, "path": str(raw), "includeSched": True}}).encode()
        request = urllib.request.Request(endpoint, body, {"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=300) as response:
            data = json.load(response)
        if data.get("error") or not data.get("result") or not raw.exists():
            raise RuntimeError(f"Exportação falhou: {data.get('error')}")
        result = prepare_package(raw, output, before["card_ids"], deck)
    after = live_snapshot(call, deck)
    result.update({"uc": uc, "deck": deck, "exported_parent": export_deck, "profile": profile,
                   "live_card_ids_and_flags_unchanged": before == after,
                   "live_snapshot": after, "published": False, "import_test": "not_performed"})
    if before != after:
        result["status"] = "blocked_live_collection_changed"
    with receipt.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    if result["status"] != "verified":
        raise RuntimeError("Coleção mudou durante exportação; não publicar este arquivo.")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--uc", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8765")
    args = parser.parse_args()
    print(json.dumps(export_uc(args.uc, args.output, args.endpoint), ensure_ascii=False))


if __name__ == "__main__":
    main()
