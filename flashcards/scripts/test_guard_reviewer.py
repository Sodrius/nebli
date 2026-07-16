import unittest
from unittest.mock import patch

import fechar_flags_visuais_linf_2026_07_15 as flow


class ReviewerGuardTests(unittest.TestCase):
    @patch.object(flow, "call", return_value={"cardId": 123})
    def test_active_reviewer_is_detected(self, _call):
        self.assertEqual(flow.reviewer_card()["cardId"], 123)

    @patch.object(flow, "call", side_effect=RuntimeError("Gui review is not currently active."))
    def test_inactive_reviewer_is_safe(self, _call):
        self.assertIsNone(flow.reviewer_card())

    @patch.object(flow, "call", side_effect=RuntimeError("collection is not available"))
    def test_unexpected_error_is_not_treated_as_idle(self, _call):
        with self.assertRaisesRegex(RuntimeError, "collection is not available"):
            flow.reviewer_card()


if __name__ == "__main__":
    unittest.main()
