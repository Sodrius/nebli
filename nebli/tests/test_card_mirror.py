import copy
import json
import math
from pathlib import Path
import tempfile
import unittest

from nebli import card_mirror as mirror


def card(i, origin="AnKing", text=None, **kwargs):
    return {"id": i, "origin": origin, "family": "mechanism",
            "text": text or "Process %s requires {{c1::protein}}" % i,
            "extra": "", **kwargs}


class NormalizationTests(unittest.TestCase):
    def test_nested_credit_markup_and_file_alt_do_not_leak(self):
        raw = ('<i><u>Photo credit: Named contributor, CC BY-SA</u></i>'
               '<br><i>Image credit(s): Another contributor</i>'
               '<br><img src="x.png" alt="File:Native-deck.jpg">'
               '<br><img src="y.png" alt="Normal epithelium">')
        normalized, _ = mirror.normalize_field(raw)
        self.assertNotIn("contributor", normalized)
        self.assertNotIn("Native-deck", normalized)
        self.assertIn("Normal epithelium", normalized)

    def test_credit_like_cloze_stays_even_with_nested_markup(self):
        normalized, _ = mirror.normalize_field(
            '<i><u>Source: {{c1::mitochondria}}</u></i>')
        self.assertIn("{{c1::mitochondria}}", normalized)

    def test_semantics_and_clozes_survive(self):
        text, audit = mirror.normalize_field(
            '<div>Ca<sup>2+</sup> activates <b>{{c1::kinase::enzyme}}</b>'
            '&nbsp;&amp; A &lt; B</div><ul><li>First</li><li>Second</li></ul>')
        self.assertIn("Ca^{2+}", text)
        self.assertIn("**{{c1::kinase::enzyme}}**", text)
        self.assertIn("& A < B", text)
        self.assertIn("- First\n- Second", text)
        self.assertTrue(audit)

    def test_no_asset_paths_attributes_comments_or_script_leak(self):
        raw = ('<div id="AnKing-note-12" data-origin="AnKing">Answer</div>'
               '<img src="private/anking12.png" alt="Normal epithelium">'
               '<!--NEBLI--><script>secret-path</script>[sound:author.mp3]')
        text, audit = mirror.normalize_field(raw)
        for leak in ("AnKing", "NEBLI", "private/", "secret-path", "author.mp3"):
            self.assertNotIn(leak, text)
        self.assertIn("[image] Normal epithelium", text)
        self.assertIn("[audio]", text)
        self.assertEqual(audit[0]["before"], raw)

    def test_source_rules_only_remove_explicit_provenance_lines(self):
        raw = ("The source of {{c1::ATP}} is metabolism.\n"
               "Source: https://private.example/AnKing\n"
               "Credit: NEBLI\nSource: {{c1::mitochondria}}\n"
               "Visit https://medical.example for context")
        text, audit = mirror.normalize_field(raw)
        self.assertNotIn("private.example", text)
        self.assertNotIn("NEBLI", text)
        self.assertIn("Source: {{c1::mitochondria}}", text)
        self.assertIn("https://medical.example", text)
        self.assertEqual(sum(a["rule"] == "explicit-provenance-line" for a in audit), 2)

    def test_native_credit_lines_removed_and_audited(self):
        text, audit = mirror.normalize_field(
            "Question {{c1::answer}}\nPhoto credit: AnKing\n"
            "Image licensed by AnkiHub\nLast updated: 2026\n© AnkiHub")
        self.assertEqual(text, "Question {{c1::answer}}")
        self.assertEqual(sum(a["rule"] == "explicit-provenance-line" for a in audit), 4)

    def test_inline_photo_credit_does_not_delete_caption(self):
        text, audit = mirror.normalize_field(
            '<img src="asbestos.jpg"><i>Barbell-shaped asbestos bodies. '
            '<em>Photo credit: Photographer [CC BY-SA]</em></i>')
        self.assertIn("Barbell-shaped asbestos bodies", text)
        self.assertNotIn("Photographer", text)
        self.assertTrue(any(a["rule"] == "explicit-provenance-suffix" for a in audit))

    def test_same_normalization_for_both_origins_and_no_extra_truncation(self):
        raw = "<b>{{c1::answer}}</b><br>Context"
        extra = "- " + "long context " * 120
        blind, key = mirror.build_batch([card("a", text=raw, extra=extra),
                                        card("b", "Autoral", raw, extra=extra)], 9)
        self.assertEqual(blind[0]["text"], blind[1]["text"])
        self.assertEqual(blind[0]["extra"], blind[1]["extra"])
        self.assertGreater(len(blind[0]["extra"]), 1000)
        self.assertTrue(all(r["provenance"]["extra"] == extra for r in key["records"]))


class BuildTests(unittest.TestCase):
    def test_only_allowed_fields_and_reproducible_non_source_ids(self):
        records = [card("source-anking-id", text="{{c1::A}} powers cells", extra="Some context", tags=["AnKing"]),
                   card("source-autoral-id", "Autoral", text="{{c1::B}} inhibits cells", extra="Other context")]
        blind, key = mirror.build_batch(records, 71)
        self.assertEqual((blind, key), mirror.build_batch(records, 71))
        for row in blind:
            self.assertEqual(set(row), {"id", "text", "extra", "family"})
            self.assertRegex(row["id"], r"^[0-9a-f]{32}$")
        self.assertNotIn("source-anking-id", json.dumps(blind))
        self.assertEqual(key["manifest"]["seed"], 71)
        self.assertEqual(len(key["records"]), len(blind))

    def test_front_mode_omission_is_audited(self):
        blind, key = mirror.build_batch([card(1, extra="Useful context")], 1, "front")
        self.assertEqual(blind[0]["extra"], "")
        self.assertEqual(key["records"][0]["normalization"]["extra"][-1],
                         {"rule": "front-mode-omit-extra", "before": "Useful context", "after": ""})

    def test_bad_schema_and_duplicate_ids(self):
        cases = [[], {}, [card(1), card("1")], [card(True)],
                 [card(1, origin="Other")], [card(1, family="")],
                 [card(1, extra=None)], [card(1, group_id=[])],
                 [card(1, text="<script>hidden</script>")]]
        for records in cases:
            with self.subTest(records=records), self.assertRaises(ValueError):
                mirror.build_batch(records, 1)

    def test_cli_refuses_to_overwrite_run_or_score(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_path = root / "input.json"
            input_path.write_text(json.dumps([card(1)]), encoding="utf-8")
            argv = ["build", "--input", str(input_path), "--output", str(root / "run"), "--seed", "12"]
            mirror.main(argv)
            key_path = root / "run" / "private-key.json"
            original = key_path.read_bytes()
            self.assertEqual(key_path.stat().st_mode & 0o777, 0o600)
            with self.assertRaises(SystemExit):
                mirror.main(argv)
            self.assertEqual(key_path.read_bytes(), original)
            key = json.loads(original)
            pred_path = root / "predictions.json"
            pred_path.write_text(json.dumps([{"id": key["records"][0]["id"],
                                             "p_autoral": .2, "tells": []}]), encoding="utf-8")
            args = ["score", "--key", str(key_path), "--predictions", str(pred_path),
                    "--output", str(root / "score.json")]
            mirror.main(args)
            with self.assertRaises(SystemExit):
                mirror.main(args)


class SplitTests(unittest.TestCase):
    def test_transitive_sibling_and_duplicate_leakage(self):
        records = [card("a", text="<b>{{c1::ATP}}</b> powers cells", group_id="note-1"),
                   card("b", text="Sibling is {{c1::ADP}}", group_id="note-1"),
                   card("c", text="{{c2::ATP}} powers cells", group_id="note-2"),
                   card("d", text="Other sibling", group_id="note-2")]
        records += [card(str(i)) for i in range(30)]
        split = mirror.grouped_split(records, 19)
        assignment = {r["id"]: name for name, rs in split.items() for r in rs}
        self.assertEqual(len({assignment[x] for x in ("a", "b", "c", "d")}), 1)
        self.assertEqual(len(assignment), len(records))
        self.assertTrue(all(split.values()))
        self.assertEqual(split, mirror.grouped_split(list(reversed(records)), 19))

    def test_same_front_different_extras_stays_together(self):
        records = [card(1, text="{{c1::Answer}} matters", extra="one"),
                   card(2, "Autoral", "{{c9::Answer}} matters", extra="two")]
        self.assertEqual(len(mirror.leakage_components(records)), 1)

    def test_bad_fractions(self):
        for fractions in ({}, {"train": 2}, {"train": float("nan")}, {"a": 0, "b": 1}):
            with self.assertRaises(ValueError):
                mirror.grouped_split([card(1)], 1, fractions)


class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.key = {"records": [
            {"id": "a", "origin": "AnKing", "family": "causal"},
            {"id": "b", "origin": "AnKing", "family": "causal"},
            {"id": "c", "origin": "Autoral", "family": "causal"},
            {"id": "d", "origin": "Autoral", "family": "contrast"}]}

    def predictions(self, probabilities):
        return [{"id": rid, "p_autoral": p, "tells": ["Observed phrasing"]}
                for rid, p in zip("abcd", probabilities)]

    def test_ties_and_calibration(self):
        report = mirror.score_predictions(self.key, self.predictions([.5] * 4))
        metrics = report["overall"]
        self.assertEqual(metrics["auc"], .5)
        self.assertEqual(metrics["balanced_accuracy"], .5)
        self.assertEqual(metrics["brier"], .25)
        self.assertAlmostEqual(metrics["log_loss"], math.log(2))
        self.assertEqual(metrics["confusion"], {"tp_autoral": 2, "tn_anking": 0,
                                                "fp_autoral": 2, "fn_autoral": 0})
        self.assertLess(metrics["accuracy_wilson_95"][0], .5)
        self.assertGreater(metrics["accuracy_wilson_95"][1], .5)
        self.assertEqual(set(report["by_origin"]), {"AnKing", "Autoral"})
        self.assertEqual(report["by_family"]["contrast"]["auc"], None)

    def test_inverted_detector_is_signal_not_success(self):
        result = mirror.score_predictions(self.key, self.predictions([1, 1, 0, 0]))
        self.assertEqual(result["overall"]["accuracy"], 0)
        self.assertEqual(result["overall"]["auc"], 0)
        self.assertEqual(result["overall"]["inverted_auc"], 1)
        self.assertEqual(result["overall"]["inverted_balanced_accuracy"], 1)
        self.assertIn("does not prove indistinguishability", result["interpretation"])
        self.assertTrue(math.isfinite(result["overall"]["log_loss"]))

    def test_auc_average_tie_ranks(self):
        result = mirror.score_predictions(self.key, self.predictions([.1, .5, .5, .9]))
        self.assertEqual(result["overall"]["auc"], .875)

    def test_all_anking_degenerate_case(self):
        key = copy.deepcopy(self.key)
        for row in key["records"]:
            row["origin"] = "AnKing"
        result = mirror.score_predictions(key, self.predictions([0] * 4))["overall"]
        self.assertEqual(result["accuracy"], 1)
        self.assertIsNone(result["auc"])
        self.assertIsNone(result["balanced_accuracy"])
        self.assertIsNone(result["recall"]["Autoral"])

    def test_strict_prediction_coverage_and_schema(self):
        good = self.predictions([.1, .2, .8, .9])
        cases = [good[:-1], good + [good[0]], good + [{"id": "extra", "p_autoral": .3, "tells": []}], {}]
        for p in (float("nan"), float("inf"), -.01, 1.01, True, "0.5", None):
            bad = copy.deepcopy(good)
            bad[0]["p_autoral"] = p
            cases.append(bad)
        bad = copy.deepcopy(good)
        bad[0]["tells"] = "style"
        cases.append(bad)
        for predictions in cases:
            with self.subTest(predictions=predictions), self.assertRaises(ValueError):
                mirror.score_predictions(self.key, predictions)

    def test_duplicate_key_ids_rejected(self):
        bad = copy.deepcopy(self.key)
        bad["records"].append(bad["records"][0])
        with self.assertRaises(ValueError):
            mirror.score_predictions(bad, self.predictions([.1, .2, .8, .9]))

    def test_contamination_excluded_explicitly_with_complete_coverage(self):
        predictions = self.predictions([.1, .2, .8, .9])
        predictions[0]["contamination"] = True
        report = mirror.score_predictions(self.key, predictions)
        self.assertEqual(report["coverage"], 1)
        self.assertEqual(report["overall"]["n"], 3)
        self.assertEqual(report["overall_all"]["n"], 4)
        self.assertEqual(report["contamination"]["ids"], ["a"])
        with self.assertRaises(ValueError):
            mirror.score_predictions(self.key, predictions[1:])
        for prediction in predictions:
            prediction["contamination"] = True
        report = mirror.score_predictions(self.key, predictions)
        self.assertIsNone(report["overall"])
        self.assertEqual(report["by_family"], {})
        predictions[0]["contamination"] = "false"
        with self.assertRaises(ValueError):
            mirror.score_predictions(self.key, predictions)

    def test_json_loader_rejects_duplicate_properties_and_nan(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            for raw in ('{"p_autoral": 0.2, "p_autoral": 0.9}', '[NaN]', '[Infinity]'):
                path.write_text(raw, encoding="utf-8")
                with self.assertRaises(ValueError):
                    mirror._read(path)


if __name__ == "__main__":
    unittest.main()
