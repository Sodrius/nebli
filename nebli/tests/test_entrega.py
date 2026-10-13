import tempfile
import unittest
from pathlib import Path

from nebli import entrega


class EntregaTests(unittest.TestCase):
    def test_copies_with_standard_names_and_renames_slides(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); folder = root / "UC08" / "Fisiologia" / "05 - Aula"; folder.mkdir(parents=True)
            (folder / "Aula-3.pdf").write_text("s"); e1 = root / "main.pdf"; e1.write_text("e"); deck = root / "x.apkg"; deck.write_text("d")
            entrega.deliver("UC08/Fisiologia/05 - Aula", "Digestão", str(e1), str(deck), "Aula-3.pdf", str(deck), root=root)
            self.assertEqual(sorted(p.name for p in folder.iterdir()), ["Digestão - E1.pdf", "Digestão - slides.pdf", "Digestão.apkg"])
            self.assertTrue((root / "UC08" / "NEBLI - UC08.apkg").exists())
            entrega.deliver("UC08/Fisiologia/05 - Aula", "Digestão", str(e1), slides="Aula-3.pdf", root=root)  # repetir é seguro

    def test_refuses_to_overwrite_existing_slides(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); folder = root / "UC08" / "A"; folder.mkdir(parents=True)
            (folder / "novo.pdf").write_text("n"); (folder / "X - slides.pdf").write_text("s")
            with self.assertRaises(SystemExit):
                entrega.deliver("UC08/A", "X", slides="novo.pdf", root=root)


if __name__ == "__main__":
    unittest.main()
