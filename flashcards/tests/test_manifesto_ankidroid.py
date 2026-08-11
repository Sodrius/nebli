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


def test_manifest_requires_nebli_target(tmp_path):
    concepts = tmp_path / "concepts.json"
    concepts.write_text('["portal vein"]', encoding="utf-8")
    out = tmp_path / "bad.json"
    proc = run("--slug", "x", "--deck", "AnKing", "--conceitos", str(concepts), "--out", str(out))
    assert proc.returncode != 0
    assert not out.exists()


def test_v2_manifest_is_concept_driven_and_source_safe(tmp_path):
    concepts = tmp_path / "concepts.json"
    concepts.write_text(
        json.dumps({"concepts": [
            {"id": "c1", "query": "portal vein", "aliases": ["hepatic portal vein"]},
            {"conceito": "marginal artery of Drummond", "nuclear": True},
        ]}), encoding="utf-8")
    out = tmp_path / "manifest.json"
    proc = run("--slug", "anato-10-intestino-grosso", "--deck",
               "NEBLI::UC02::P3::Anatomia::Intestino grosso", "--conceitos", str(concepts), "--out", str(out))
    assert proc.returncode == 0, proc.stderr
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["schema"] == "nebli-ankidroid-lesson-v2"
    assert data["copy_mode"] == "exact_fields"
    assert data["mutate_source"] is False
    assert data["preserve_note_type"] is True
    assert data["preserve_media_refs"] is True
    assert data["selected_sibling_policy"] == "suspend_unselected"
    assert data["search"]["min_score"] == 0.82
    assert data["search"]["prefer_anking"] is True
    assert data["concepts"][0]["query"] == "portal vein"
    assert data["concepts"][0]["aliases"] == ["hepatic portal vein"]
    assert data["concepts"][1]["query"] == "marginal artery of Drummond"
    assert len(data["manifest_sha256"]) == 64


def test_v2_accepts_simple_string_list(tmp_path):
    concepts = tmp_path / "concepts.json"
    concepts.write_text('["portal vein", "duodenum"]', encoding="utf-8")
    out = tmp_path / "manifest.json"
    proc = run("--slug", "x", "--deck", "NEBLI::Aula", "--conceitos", str(concepts), "--out", str(out))
    assert proc.returncode == 0, proc.stderr
    data = json.loads(out.read_text(encoding="utf-8"))
    assert [c["query"] for c in data["concepts"]] == ["portal vein", "duodenum"]


def test_curated_ids_are_carried_without_card_content_rewrite(tmp_path):
    curated = tmp_path / "curado.json"
    curated.write_text(json.dumps({"kept": [{
        "nid": 123, "cid": 456, "ord": 2, "guid": "source-guid",
        "conceito": "arcada marginal", "raw0": "Original <b>AnKing</b> text",
    }]}), encoding="utf-8")
    out = tmp_path / "manifest.json"
    proc = run("--slug", "anato-x", "--deck", "NEBLI::Aula", "--curado", str(curated), "--out", str(out))
    assert proc.returncode == 0, proc.stderr
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["schema"] == "nebli-ankidroid-v1"
    item = data["items"][0]
    assert item["source_note_id"] == 123
    assert item["source_card_id"] == 456
    assert item["selected_ordinals"] == [2]
    assert item["source_guid"] == "source-guid"
    assert "Original" not in json.dumps(item)
    assert len(item["first_field_fingerprint"]) == 64


def test_manifest_requires_exactly_one_input_mode(tmp_path):
    out = tmp_path / "manifest.json"
    proc = run("--slug", "x", "--deck", "NEBLI::Aula", "--out", str(out))
    assert proc.returncode != 0
    assert not out.exists()


def authored(text="The hepatic portal vein drains into the {{c1::liver}}."):
    return {
        "source": "authored",
        "text": text,
        "extra": "A veia porta leva sangue do tubo digestório ao fígado.",
        "front_language": "en",
        "extra_language": "pt-BR",
        "anking_search_complete": True,
        "anking_rejection_reason": "No exact AnKing retrieval remained after candidate review.",
    }


def io_card(image_path):
    return {
        "source": "io",
        "image_path": image_path,
        "mode": "hide_all_guess_all",
        "masks": [{"x": 0.1, "y": 0.2, "w": 0.2, "h": 0.08}],
        "answers": ["hepatic flexure"],
        "masks_labels_not_structures": True,
        "question_preview_validated": True,
        "answer_preview_validated": True,
        "visual_ok": True,
        "real_source": True,
        "answer_leak": False,
        "coherent_set": True,
        "source_credit": "Lecture source",
        "extra": "Reconheça a relação topográfica antes de memorizar o nome.",
    }


def test_v3_builds_complete_self_contained_deck_and_canonical_name(tmp_path):
    image = tmp_path / "colon.png"
    image.write_bytes(b"\x89PNG\r\n\x1a\nNEBLI_TEST_IMAGE")
    data = {
        "metadata": {"uc": "UC02", "prova": "P3", "componente": "Anatomia", "nome_curto": "Intestino grosso"},
        "cards": [
            {
                "card_key": "c1-anking", "concept_id": "c1", "source": "anking",
                "query": "marginal artery of Drummond", "aliases": ["marginal artery"],
                "atomic": True, "relevant": True, "tier": "nucleo", "requires_visual": False,
                "fallback": authored("The marginal artery of Drummond runs along the {{c1::colon}}."),
            },
            {
                "card_key": "c2-authored", "concept_id": "c2", "atomic": True, "relevant": True,
                **authored("The tenia libera is one of the {{c1::teniae coli}}."),
            },
            {
                "card_key": "c3-io", "concept_id": "c3", "atomic": True, "relevant": True,
                **io_card("colon.png"),
            },
        ],
    }
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps(data), encoding="utf-8")
    out = tmp_path / "lesson.ankidroid.json"
    proc = run("--slug", "anato-colon", "--deck-data", str(spec), "--out", str(out))
    assert proc.returncode == 0, proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    assert manifest["schema"] == "nebli-ankidroid-deck-v3"
    assert manifest["target_deck"] == "NEBLI::UC02::P3::Anatomia::Intestino grosso"
    assert manifest["deck_identity"] == {
        "uc": "UC02", "prova": "P3", "componente": "Anatomia", "nome_curto": "Intestino grosso"
    }
    assert manifest["optional_subdeck"].endswith("::Optional")
    assert manifest["expected_card_count"] == 3
    assert manifest["search"]["require_anking_marker"] is True
    assert manifest["search"]["ambiguous_policy"] == "use_validated_fallback"
    assert manifest["cards"][0]["fallback"]["source"] == "authored"
    assert manifest["cards"][0]["source_filter"] == 'deck:"AnKing Step Deck"'
    assert manifest["cards"][0]["expected_answers"] == ["colon"]
    assert manifest["cards"][0]["search_queries"] == [
        "marginal artery of Drummond", "marginal artery"
    ]
    assert len(manifest["media"]) == 1
    assert manifest["cards"][2]["media_key"] == manifest["media"][0]["key"]
    assert "image_path" not in manifest["cards"][2]
    assert len(manifest["cards"][0]["card_sha256"]) == 64
    assert len(manifest["manifest_sha256"]) == 64


def test_v3_visual_anking_requires_io_fallback(tmp_path):
    data = {
        "metadata": {"uc": "UC01", "prova": "P1", "componente": "Teste", "nome_curto": "Aula"},
        "cards": [{
            "card_key": "visual", "concept_id": "v", "source": "anking", "query": "hepatic flexure",
            "atomic": True, "relevant": True, "requires_visual": True,
            "fallback": authored(),
        }],
    }
    spec = tmp_path / "deck.json"; spec.write_text(json.dumps(data), encoding="utf-8")
    proc = run("--slug", "x", "--deck-data", str(spec), "--out", str(tmp_path / "out.json"))
    assert proc.returncode != 0
    assert "fallback IO" in (proc.stderr + proc.stdout)


def test_v3_rejects_long_or_multiple_authored_cloze(tmp_path):
    for bad_text in [
        "The answer is {{c1::one two three four}}.",
        "{{c1::Portal}} blood enters the {{c1::liver}}.",
        "The answer is {{c2::portal vein}}.",
    ]:
        data = {
            "metadata": {"uc": "UC01", "prova": "P1", "componente": "Teste", "nome_curto": "Aula"},
            "cards": [{"card_key": "bad", "concept_id": "b", "atomic": True, "relevant": True, **authored(bad_text)}],
        }
        spec = tmp_path / "deck.json"; spec.write_text(json.dumps(data), encoding="utf-8")
        proc = run("--slug", "x", "--deck-data", str(spec), "--out", str(tmp_path / "out.json"))
        assert proc.returncode != 0


def test_v3_rejects_duplicate_card_keys(tmp_path):
    a = {"card_key": "same", "concept_id": "a", "atomic": True, "relevant": True, **authored()}
    b = {"card_key": "same", "concept_id": "b", "atomic": True, "relevant": True, **authored("The colon contains {{c1::haustra}}.")}
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps({"metadata": {"uc": "UC01", "prova": "P1", "componente": "Teste", "nome_curto": "Aula"}, "cards": [a, b]}), encoding="utf-8")
    proc = run("--slug", "x", "--deck-data", str(spec), "--out", str(tmp_path / "out.json"))
    assert proc.returncode != 0
    assert "duplicado" in (proc.stderr + proc.stdout)


def test_v3_rejects_target_deck_override_that_differs_from_metadata(tmp_path):
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps({
        "metadata": {"uc": "uc3", "prova": "p01", "componente": "Imunologia", "nome_curto": "Reconhecimento inato"},
        "target_deck": "NEBLI::nome::errado",
        "cards": [{"card_key": "a", "concept_id": "a", "atomic": True, "relevant": True, **authored()}],
    }), encoding="utf-8")
    proc = run("--slug", "x", "--deck-data", str(spec), "--out", str(tmp_path / "out.json"))
    assert proc.returncode != 0
    assert "divergente" in (proc.stderr + proc.stdout)


def test_v3_direct_authored_requires_completed_anking_search(tmp_path):
    card = {"card_key": "a", "concept_id": "a", "atomic": True, "relevant": True, **authored()}
    card.pop("anking_search_complete")
    spec = tmp_path / "deck.json"
    spec.write_text(json.dumps({
        "metadata": {"uc": "UC03", "prova": "P1", "componente": "Imunologia", "nome_curto": "Reconhecimento inato"},
        "cards": [card],
    }), encoding="utf-8")
    proc = run("--slug", "x", "--deck-data", str(spec), "--out", str(tmp_path / "out.json"))
    assert proc.returncode != 0
    assert "anking_search_complete" in (proc.stderr + proc.stdout)
