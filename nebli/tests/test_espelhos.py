import unittest

from nebli import espelhos


class EspelhosTests(unittest.TestCase):
    def test_rank_prefers_notes_matching_more_terms_then_rarer_terms(self):
        hits = [(2.0, [1, 2]), (0.5, [2, 3]), (0.1, [3, 4])]
        self.assertEqual(espelhos.rank(hits, 3), [2, 3, 1])

    def test_search_excludes_and_returns_fields(self):
        notes = {"aldose": [10, 11], "sorbitol": [11, 12]}
        def call(action, **params):
            if action == "findNotes":
                return next(v for k, v in notes.items() if k in params["query"])
            return [{"noteId": n, "fields": {"Text": {"value": f"t{n}"}, "Extra": {"value": ""}}} for n in params["notes"]]
        found = espelhos.search(call, ["aldose", "sorbitol"], exclude=[10], n=2)
        self.assertEqual([m["nid"] for m in found], [11, 12])
        self.assertEqual(found[0]["text"], "t11")


if __name__ == "__main__":
    unittest.main()
