#!/usr/bin/env python3
"""Small, dependency-free helpers for inspecting Anki packages offline."""
from __future__ import annotations

import json
import re
import sqlite3
import tempfile
import zipfile
from contextlib import contextmanager
from pathlib import Path


COLLECTION_CANDIDATES = ("collection.anki21b", "collection.anki21", "collection.anki2")
MEDIA_RE = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']", re.I)


def _zstd_decompress(raw: bytes) -> bytes:
    try:
        import io
        import zstandard
    except ImportError as exc:
        raise ValueError("pacote Anki moderno exige o módulo Python zstandard") from exc
    with zstandard.ZstdDecompressor().stream_reader(io.BytesIO(raw)) as reader:
        return reader.read()


def collection_bytes(package: zipfile.ZipFile) -> tuple[str, bytes]:
    """Return the newest readable SQLite collection and its decoded bytes."""
    names = set(package.namelist())
    for name in COLLECTION_CANDIDATES:
        if name not in names:
            continue
        raw = package.read(name)
        if raw.startswith(b"SQLite format 3\x00"):
            return name, raw
        if raw.startswith(b"(\xb5/\xfd"):
            decoded = _zstd_decompress(raw)
            if decoded.startswith(b"SQLite format 3\x00"):
                return name, decoded
    raise ValueError("APKG não contém uma coleção SQLite legível")


def _varint(raw: bytes, position: int) -> tuple[int, int]:
    value = shift = 0
    while position < len(raw):
        byte = raw[position]; position += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return value, position
        shift += 7
    raise ValueError("protobuf truncado")


def _protobuf_fields(raw: bytes):
    position = 0
    while position < len(raw):
        key, position = _varint(raw, position)
        number, wire = key >> 3, key & 7
        if wire == 0:
            value, position = _varint(raw, position)
        elif wire == 2:
            size, position = _varint(raw, position)
            value = raw[position:position + size]
            position += size
        elif wire == 1:
            value = raw[position:position + 8]; position += 8
        elif wire == 5:
            value = raw[position:position + 4]; position += 4
        else:
            raise ValueError(f"wire protobuf não suportado: {wire}")
        yield number, wire, value


def media_mapping(package: zipfile.ZipFile) -> dict[str, str]:
    if "media" not in package.namelist():
        return {}
    raw = package.read("media")
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        if raw.startswith(b"(\xb5/\xfd"):
            raw = _zstd_decompress(raw)
        entries = []
        for field, wire, entry in _protobuf_fields(raw):
            if field != 1 or wire != 2:
                continue
            filename = None
            for inner_field, inner_wire, value in _protobuf_fields(entry):
                if inner_field == 1 and inner_wire == 2:
                    filename = value.decode("utf-8")
                    break
            if filename is not None:
                entries.append(filename)
        return {str(index): filename for index, filename in enumerate(entries)}


@contextmanager
def open_collection(apkg: Path):
    """Yield (connection, zip, media_map, collection_member) for an APKG."""
    package = zipfile.ZipFile(apkg)
    try:
        member, decoded = collection_bytes(package)
        with tempfile.NamedTemporaryFile(suffix=".sqlite") as temp:
            temp.write(decoded)
            temp.flush()
            connection = sqlite3.connect(temp.name)
            connection.row_factory = sqlite3.Row
            try:
                media_map = media_mapping(package)
                yield connection, package, media_map, member
            finally:
                connection.close()
    finally:
        package.close()


def col_json(connection: sqlite3.Connection, field: str) -> dict:
    raw = connection.execute(f"SELECT {field} FROM col LIMIT 1").fetchone()[0]
    return json.loads(raw or "{}")


def _has_table(connection: sqlite3.Connection, name: str) -> bool:
    return connection.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def models_map(connection: sqlite3.Connection) -> dict[int, dict]:
    legacy = col_json(connection, "models")
    if legacy:
        return {int(key): value for key, value in legacy.items()}
    if _has_table(connection, "notetypes"):
        # No schema novo o `col.models` está vazio e os campos moram em tabelas
        # próprias. Sem preenchê-los, todo consumidor enxerga um note type sem
        # campo nenhum e desiste de analisar a nota.
        models = {
            int(row[0]): {"name": row[1], "flds": [], "tmpls": []}
            for row in connection.execute("SELECT id, name FROM notetypes")
        }
        if _has_table(connection, "fields"):
            for ntid, ord_, name in connection.execute("SELECT ntid, ord, name FROM fields ORDER BY ntid, ord"):
                model = models.get(int(ntid))
                if model is not None:
                    model["flds"].append({"name": name, "ord": int(ord_)})
        if _has_table(connection, "templates"):
            for ntid, ord_, name in connection.execute("SELECT ntid, ord, name FROM templates ORDER BY ntid, ord"):
                model = models.get(int(ntid))
                if model is not None:
                    # qfmt/afmt vivem num blob de configuração binário; o nome
                    # basta para contar templates.
                    model["tmpls"].append({"name": name, "ord": int(ord_)})
        return models
    return {}


def decks_map(connection: sqlite3.Connection) -> dict[int, dict]:
    legacy = col_json(connection, "decks")
    if legacy:
        return {int(key): value for key, value in legacy.items()}
    if _has_table(connection, "decks"):
        return {int(row[0]): {"name": row[1]} for row in connection.execute("SELECT id, name FROM decks")}
    return {}


def note_fields(raw: str) -> list[str]:
    return (raw or "").split("\x1f")


def media_references(fields: list[str]) -> set[str]:
    refs: set[str] = set()
    for field in fields:
        refs.update(value.strip() for value in MEDIA_RE.findall(field or "") if value.strip())
    return refs
