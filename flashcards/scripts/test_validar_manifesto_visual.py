#!/usr/bin/env python3
import unittest
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


if __name__ == "__main__":
    unittest.main()
