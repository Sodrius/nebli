import unittest
from deduplicar_imagens_intranota import MediaResolver, dedupe_html, normalized_src


class NoMedia(MediaResolver):
    def __init__(self):
        self.dirs = []
        self.cache = {}


class DedupeTests(unittest.TestCase):
    def test_normalizes_query_and_case(self):
        self.assertEqual(normalized_src("https://x/A%20B.PNG?v=1"), "a b.png")

    def test_removes_second_src_only(self):
        value = '<img src="x.png"><br>texto<img width="4" src="x.png">'
        out, removed = dedupe_html(value, NoMedia())
        self.assertEqual(out.count("<img"), 1)
        self.assertEqual(removed[0]["reason"], "same_src")

    def test_does_not_cross_fields_without_visible_face_evidence(self):
        text, removed_text = dedupe_html('<img src="x.png">', NoMedia(), set(), set())
        extra, removed_extra = dedupe_html('<img src="x.png">', NoMedia(), set(), set())
        self.assertIn("<img", text)
        self.assertIn("<img", extra)
        self.assertFalse(removed_text)
        self.assertFalse(removed_extra)


if __name__ == "__main__":
    unittest.main()
