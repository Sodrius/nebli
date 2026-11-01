import json
import tempfile
import unittest
from pathlib import Path

from nebli import puxar_suspensos as p


class FakeAnki:
    def __init__(self):
        self.notes = {1792000000001: {"noteId": 1792000000001, "tags": ["NEBLI::2026-uc03-velha", "AnKing::source::nid::1490000000001"], "cards": [11]},
                      1792000000002: {"noteId": 1792000000002, "tags": ["NEBLI::2026-uc03-velha", "NEBLI::retirado::refacao-v2"], "cards": [12]},
                      1792000000003: {"noteId": 1792000000003, "tags": ["NEBLI::2026-uc03-velha"], "cards": [13]}}
        self.cards = {11: {"cardId": 11, "queue": -1, "deckName": "NEBLI::Velha"}, 12: {"cardId": 12, "queue": -1, "deckName": "NEBLI::Velha"},
                      13: {"cardId": 13, "queue": 0, "deckName": "NEBLI::Velha"}}
        self.ops = []

    def __call__(self, a, **k):
        self.ops.append(a)
        if a == "notesInfo":
            return [self.notes[n] for n in k["notes"]]
        if a == "cardsInfo":
            return [self.cards[c] for c in k["cards"]]


class PuxarTests(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory(); self.run = Path(self.d.name); (self.run / "busca").mkdir()
        top = [{"acervo": "NEBLI-vivo", "nid": n, "sim": 0.9, "rank_sem": 1} for n in (1792000000001, 1792000000002, 1792000000003)]
        (self.run / "busca" / "semantica.jsonl").write_text(json.dumps({"chave": "k1", "top": top}) + "\n")

    def tearDown(self):
        self.d.cleanup()

    def test_so_suspensa_por_davi_e_candidata(self):
        c = p.candidatos(self.run, {"lesson_id": "2026-uc03-nova"}, FakeAnki())
        self.assertEqual([x["nid"] for x in c], [1792000000001])

    def test_gate_exige_sh_e_recusa_copia_nova(self):
        plan = {"lesson_id": "2026-uc03-nova", "entries": [{"key": "ak1", "src": "1490000000001"}]}
        r = p.verificar(self.run, plan, FakeAnki())
        self.assertFalse(r[0][1]); self.assertFalse(r[1][1])
        plan = {"lesson_id": "2026-uc03-nova", "entries": [], "compartilhados": {"1792000000001": {}}}
        self.assertTrue(all(ok for _, ok in p.verificar(self.run, plan, FakeAnki())))

    def test_puxar_move_dessuspende_e_marca(self):
        A = FakeAnki(); log = []
        n = A.notes[1792000000001]
        self.assertTrue(p.puxar(A, n, [A.cards[11]], "NEBLI::Nova", "2026-uc03-nova", lambda **k: log.append(k)))
        self.assertEqual(A.ops, ["changeDeck", "unsuspend", "addTags"])
        self.assertFalse(p.puxar(A, A.notes[1792000000002], [A.cards[12]], "NEBLI::Nova", "x", lambda **k: None))


if __name__ == "__main__":
    unittest.main()
