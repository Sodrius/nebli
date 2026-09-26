import unittest
from unittest.mock import patch

from nebli.preflight import FLAGS, READ_ACTIONS, ReadOnlyAnki, collect, deck_query, discover_corpora


class PreflightTests(unittest.TestCase):
    def test_rejects_mutations_before_network(self):
        with patch("urllib.request.urlopen") as network:
            for action in ("addNote", "deleteNotes", "unsuspend", "setSpecificValueOfCard"):
                with self.assertRaises(ValueError):
                    ReadOnlyAnki()(action)
            network.assert_not_called()

    def test_blue_mapping_and_legacy_pink(self):
        self.assertEqual(FLAGS[0], "avaliacao_incerta")
        self.assertEqual(FLAGS[3], "recomendo_manter_longo_prazo")
        self.assertEqual(FLAGS[4], "aprender_menor_custo_de_esquecer")
        self.assertEqual(FLAGS[5], "rosa_legado_ou_pessoal")
        self.assertNotIn(6, FLAGS)

    def test_discovers_anking_after_case_change(self):
        name = "Referências::Anking Step Deck"
        self.assertIn(name, discover_corpora([name, name + "::Instructions"]))

    def test_quotes(self):
        self.assertEqual(deck_query('A "B"'), 'deck:"A \\"B\\""')

    def test_diagnostic_is_not_quality_approval(self):
        calls = []

        def fake(action, **params):
            self.assertIn(action, READ_ACTIONS)
            calls.append(action)
            if action == "version":
                return 6
            if action == "getActiveProfile":
                return "test"
            return []

        result = collect(fake)
        self.assertEqual(result["semantic_quality"], "não auditada")
        self.assertEqual(len(result["corpora"]), 0)
        self.assertTrue(all(not c["available"] for c in result["corpora"]))
        self.assertEqual(result["medical"]["cards"], 0)

    def test_discovers_moved_and_new_external_corpora(self):
        decks = ["AnKing Step Deck", "Referências::Referências Externas",
                 "Referências::Referências Externas::AnKing-MCAT::Biochemistry",
                 "Referências::Referências Externas::AnKing-MCAT::Biology",
                 "Referências::Referências Externas::Novo::A",
                 "NEBLI::UC03::Aula"]
        self.assertEqual(set(discover_corpora(decks)), {
            "AnKing Step Deck", "Referências::Referências Externas::AnKing-MCAT",
            "Referências::Referências Externas::Novo"})

    def test_flags_come_from_search_not_missing_card_field(self):
        def fake(action, **params):
            if action == "version":
                return 6
            if action == "getActiveProfile":
                raise RuntimeError("unsupported action")
            if action == "deckNames":
                return ["NEBLI (1)", "NEBLI (1)::UC03 (1)", "NEBLI (1)::UC03 (1)::Test (1)"]
            if action == "findCards":
                return [100] if params["query"] in (
                    '(deck:"NEBLI (1)::UC03 (1)")', '(deck:"NEBLI (1)::UC03 (1)") flag:2') else []
            if action == "cardsInfo":
                return [{"cardId": 100, "note": 10, "deckName": "NEBLI (1)::UC03 (1)::Test (1)",
                         "queue": 0, "reps": 0}]
            if action == "notesInfo":
                return [{"noteId": 10, "cards": [100], "fields": {
                    "NEBLI_Comentario": {"value": "imagem"}}}]
            raise AssertionError(action)

        result = collect(fake)
        self.assertEqual(result["status"], "partial")
        self.assertIsNone(result["profile"])
        self.assertEqual(result["medical"]["flags"]["2"], 1)
        self.assertEqual(result["medical"]["flags"]["0"], 0)
        self.assertEqual(result["medical"]["red_or_orange_ids"], [100])
        self.assertEqual(result["medical"]["comments"][0]["comment"], "imagem")
        self.assertEqual(result["medical"]["by_deck"], {"NEBLI::UC03::Test": 1})


if __name__ == "__main__":
    unittest.main()
