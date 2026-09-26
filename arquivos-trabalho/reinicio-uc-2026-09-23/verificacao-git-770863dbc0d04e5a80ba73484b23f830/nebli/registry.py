"""Registro local com migrations idempotentes; nenhum acesso à coleção Anki."""
from __future__ import annotations

import sqlite3
from pathlib import Path

MIGRATIONS = (
    """
    CREATE TABLE IF NOT EXISTS schema_migration (
      version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS lesson (
      lesson_id TEXT PRIMARY KEY, year INTEGER NOT NULL, uc TEXT NOT NULL,
      component TEXT NOT NULL, content_number INTEGER, title TEXT NOT NULL,
      source_folder_id TEXT, output_folder_id TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS source (
      source_id TEXT PRIMARY KEY, lesson_id TEXT NOT NULL REFERENCES lesson(lesson_id),
      drive_file_id TEXT NOT NULL UNIQUE, title TEXT NOT NULL, mime_type TEXT NOT NULL,
      drive_url TEXT NOT NULL, modified_time TEXT, byte_size INTEGER,
      role TEXT NOT NULL, downloaded_at TEXT, sha256 TEXT, access_status TEXT NOT NULL DEFAULT 'metadata_only'
    );
    CREATE TABLE IF NOT EXISTS publication (
      artifact_key TEXT PRIMARY KEY, lesson_id TEXT NOT NULL REFERENCES lesson(lesson_id),
      local_path TEXT NOT NULL, sha256 TEXT NOT NULL, drive_file_id TEXT,
      drive_folder_id TEXT NOT NULL, status TEXT NOT NULL,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, published_at TEXT
    );
    CREATE TABLE IF NOT EXISTS run (
      run_id TEXT PRIMARY KEY, lesson_id TEXT NOT NULL REFERENCES lesson(lesson_id),
      target TEXT NOT NULL, status TEXT NOT NULL,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, note TEXT
    );
    """,
)

def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("CREATE TABLE IF NOT EXISTS schema_migration (version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)")
    for version, sql in enumerate(MIGRATIONS, 1):
        if not db.execute("SELECT 1 FROM schema_migration WHERE version = ?", (version,)).fetchone():
            db.executescript(sql)
            db.execute("INSERT INTO schema_migration(version) VALUES (?)", (version,))
    db.commit()
    return db
