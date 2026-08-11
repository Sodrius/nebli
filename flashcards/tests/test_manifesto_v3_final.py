import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "gerar_manifesto_ankidroid.py"


def run(*args):
    argv = list(args)
    if "--deck-data" in argv and "--legacy-unreviewed-v3" not in argv:
        argv.append("--legacy-unreviewed-v3")
    return subprocess.run([sys.executable, str(SCRIPT), *argv], capture_output=True, text=True)


def authored(text="The colon contains {{c1::haustra}}."):
    return {
        "source": "authored",
        "text": text,
        "extra": "As haustrações resultam da organização da parede do cólon.",
        "front_language": "en",
        "extra_language": "pt-BR",
        "anking_search_complete": True,
        "anking_rejection_reason": "No exact AnKing retrieval remained after candidate review.",
    }


def test_authored_extra_image_is_embedded_and_local_path_removed(tmp_path):
    image = tmp_path / "mechanism.png"
    image.write_bytes(b"\x89PNG\r\n\x1a\nAUTHORED_EXTRA_IMAGE")
    card = {
        "card_key": "auth-image",
        "concept_id": "c1",
        "atomic": True,
        "relevant": True,
        **authored(),
        "extra_images": [{
            "path": "mechanism.png",
            "source_credit": "Lecture atlas, p. 10",
            "alt": "Haustral anatomy",
        }],
    }
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps({
        "metadata": {"uc": "UC02", "prova": "P3", "componente": "Anatomia", "nome_curto": "Cólon"},
        "cards": [card],
    }), encoding="utf-8")
    out = tmp_path / "out.json"
    proc = run("--slug", "colon", "--deck-data", str(spec), "--out", str(out))
    assert proc.returncode == 0, proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    installed_card = manifest["cards"][0]
    assert "extra_images" not in installed_card
    assert "mechanism.png" not in json.dumps(installed_card)
    assert len(installed_card["media_keys"]) == 1
    key = installed_card["media_keys"][0]
    assert f"nebli-media://{key}" in installed_card["extra"]
    assert "Lecture atlas, p. 10" in installed_card["extra"]
    assert len(manifest["media"]) == 1
    assert manifest["media"][0]["key"] == key
    assert manifest["media"][0]["source_credit"] == "Lecture atlas, p. 10"
    assert manifest["media"][0]["data_base64"]


def test_authored_extra_image_requires_real_source_credit(tmp_path):
    image = tmp_path / "mechanism.png"
    image.write_bytes(b"image")
    card = {
        "card_key": "bad-image",
        "concept_id": "c1",
        "atomic": True,
        "relevant": True,
        **authored(),
        "extra_images": [{"path": "mechanism.png"}],
    }
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps({"metadata": {"uc": "UC01", "prova": "P1", "componente": "Teste", "nome_curto": "Aula"}, "cards": [card]}), encoding="utf-8")
    proc = run("--slug", "x", "--deck-data", str(spec), "--out", str(tmp_path / "out.json"))
    assert proc.returncode != 0
    assert "source_credit" in (proc.stderr + proc.stdout)


def test_external_deck_is_supported_with_filter_and_validated_fallback(tmp_path):
    card = {
        "card_key": "external-1",
        "concept_id": "c1",
        "source": "external_deck",
        "query": "inferior mesenteric artery",
        "aliases": ["IMA"],
        "source_filter": 'deck:"Anatomy Atlas"',
        "atomic": True,
        "relevant": True,
        "fallback": authored("The inferior mesenteric artery supplies the {{c1::hindgut}}."),
    }
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps({
        "metadata": {"uc": "UC02", "prova": "P3", "componente": "Anatomia", "nome_curto": "Vascularização"},
        "cards": [card],
    }), encoding="utf-8")
    out = tmp_path / "out.json"
    proc = run("--slug", "vascular", "--deck-data", str(spec), "--out", str(out))
    assert proc.returncode == 0, proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    c = manifest["cards"][0]
    assert c["source"] == "external_deck"
    assert c["source_filter"] == 'deck:"Anatomy Atlas"'
    assert c["fallback"]["source"] == "authored"
    assert c["aliases"] == ["IMA"]


def test_io_requires_source_credit(tmp_path):
    image = tmp_path / "io.png"
    image.write_bytes(b"io")
    card = {
        "card_key": "io-no-credit",
        "concept_id": "c1",
        "source": "io",
        "atomic": True,
        "relevant": True,
        "image_path": "io.png",
        "mode": "hide_all_guess_all",
        "masks": [{"x": 0.1, "y": 0.1, "w": 0.2, "h": 0.1}],
        "answers": ["appendix"],
        "masks_labels_not_structures": True,
        "question_preview_validated": True,
        "answer_preview_validated": True,
        "visual_ok": True,
        "real_source": True,
        "answer_leak": False,
        "coherent_set": True,
    }
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps({"metadata": {"uc": "UC01", "prova": "P1", "componente": "Teste", "nome_curto": "Aula"}, "cards": [card]}), encoding="utf-8")
    proc = run("--slug", "x", "--deck-data", str(spec), "--out", str(tmp_path / "out.json"))
    assert proc.returncode != 0
    assert "source_credit" in (proc.stderr + proc.stdout)
