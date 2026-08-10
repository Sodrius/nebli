import importlib.util
import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "gerar_manifesto_ankidroid.py"


def test_manifest_requires_nebli_target(tmp_path):
    out = tmp_path / "bad.json"
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--slug", "x", "--deck", "AnKing", "--out", str(out)],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert not out.exists()


def test_manifest_defaults_are_source_safe(tmp_path):
    out = tmp_path / "manifest.json"
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--slug",
            "anato-10-intestino-grosso",
            "--deck",
            "NEBLI::UC02::P3::Anatomia::Intestino grosso",
            "--out",
            str(out),
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["schema"] == "nebli-ankidroid-v1"
    assert data["copy_mode"] == "exact_fields"
    assert data["mutate_source"] is False
    assert data["preserve_note_type"] is True
    assert data["preserve_media_refs"] is True
    assert data["reset_scheduling"] is True
    assert data["selected_sibling_policy"] == "suspend_unselected"
    assert data["source_query"].startswith("tag:NEBLI::anato-10-intestino-grosso")
    assert len(data["manifest_sha256"]) == 64


def test_curated_ids_are_carried_without_card_content_rewrite(tmp_path):
    curated = tmp_path / "curado.json"
    curated.write_text(
        json.dumps(
            {
                "kept": [
                    {
                        "nid": 123,
                        "cid": 456,
                        "ord": 2,
                        "guid": "source-guid",
                        "conceito": "arcada marginal",
                        "raw0": "Original <b>AnKing</b> text",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    out = tmp_path / "manifest.json"
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--slug",
            "anato-x",
            "--deck",
            "NEBLI::Aula",
            "--curado",
            str(curated),
            "--out",
            str(out),
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    item = json.loads(out.read_text(encoding="utf-8"))["items"][0]
    assert item["source_note_id"] == 123
    assert item["source_card_id"] == 456
    assert item["selected_ordinals"] == [2]
    assert item["source_guid"] == "source-guid"
    assert "Original" not in json.dumps(item)
    assert len(item["first_field_fingerprint"]) == 64
