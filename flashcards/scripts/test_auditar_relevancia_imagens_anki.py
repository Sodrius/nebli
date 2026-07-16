import unittest

from auditar_relevancia_imagens_anki import infer_visual_need


class VisualNeedTests(unittest.TestCase):
    def note(self, text, tags=(), model="AnKingOverhaul"):
        return {"modelName": model, "tags": list(tags),
                "fields": {"Text": {"value": text}}}

    def test_anatomy_slug_alone_is_not_required(self):
        got = infer_visual_need(self.note("The heart pumps blood.", ["NEBLI::anato-05-x"]))
        self.assertEqual(got, ("optional", "context"))

    def test_io_is_required(self):
        got = infer_visual_need(self.note("", model="IO-one by one"))
        self.assertEqual(got, ("required", "recognition"))

    def test_explicit_visual_prompt_is_recommended(self):
        got = infer_visual_need(self.note("Identify in this micrograph the tunica media."))
        self.assertEqual(got, ("recommended", "recognition"))


if __name__ == "__main__":
    unittest.main()
