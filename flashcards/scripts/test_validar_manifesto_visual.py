#!/usr/bin/env python3
import unittest
import tempfile
from pathlib import Path

from validar_manifesto_visual import validate


class ManifestoVisualTests(unittest.TestCase):
    def test_required_context_fails(self):
        row = {"note_id": 1, "visual_need": "required", "image_role": "context", "image_status": "approved", "visual_task": "decorar", "card_mode": "explanatory_image", "placement": "extra", "image_score": 3, "answer_leakage": False, "asset": {"file": "x.png"}}
        errors = validate(row, Path("."))
        self.assertTrue(any("context nunca resolve" in x for x in errors))

    def test_required_pending_fails_closed(self):
        row = {"note_id": 2, "visual_need": "required", "image_role": "recognition", "image_status": "pending_review", "visual_task": "identificar", "card_mode": "image_occlusion", "target_count": 1, "all_duplicate_labels_masked": True}
        errors = validate(row, Path("."))
        self.assertTrue(any("required ainda bloqueado" in x for x in errors))

    def test_none_without_asset_passes(self):
        row = {"note_id": 3, "visual_need": "none", "image_role": "none", "image_status": "missing", "card_mode": "explanatory_image"}
        self.assertEqual(validate(row, Path(".")), [])

    def test_approved_multi_label_io_masks_labels_and_has_two_previews(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            for name in ("question.png", "answer.png"):
                (root / name).write_bytes(b"preview")
            row = {
                "note_id": 4, "visual_need": "required", "image_role": "localization",
                "image_status": "approved", "visual_task": "identificar partes",
                "didactic_value_reviewed": True,
                "card_mode": "image_occlusion", "behavior": "hide_two_guess_two",
                "pair_rationale": "as duas partes formam uma unidade anatômica",
                "mask_policy": "cover_answer_label_not_visual_target",
                "masks": [
                    {"label": "part A", "covers": "answer_label"},
                    {"label": "part B", "covers": "answer_label"},
                ],
                "qa": {"masks_cover_answer_labels": True,
                       "visual_clues_remain_visible": True,
                       "all_answers_hidden": True,
                       "all_duplicate_labels_masked": True,
                       "question_preview_reviewed": True,
                       "answer_preview_reviewed": True},
                "question_preview": "question.png", "answer_preview": "answer.png",
                "image_score": 3, "answer_leakage": False,
                "asset": {"file": "image.png", "source_type": "institutional",
                          "credit": "Example", "license_status": "open_ok",
                          "retrieved_at": "2026-08-10", "hash": "sha256"},
            }
            self.assertEqual(validate(row, root), [])


if __name__ == "__main__":
    unittest.main()
