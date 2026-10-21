import json
import tempfile
import unittest
from pathlib import Path

from nebli.kenhub.fallbacks_locais import gerar, validar


class FallbacksLocaisTest(unittest.TestCase):
    def test_gate_rejeita_enumeracao_e_tautologia(self):
        self.assertIn("frase enumerativa proibida", validar(
            "Os ramos incluem A, B e {{c1::C}}."))
        self.assertIn("frase sem relação anatômica recuperável", validar(
            "Esta estrutura é a {{c1::artéria angular}}."))

    def test_extrai_sentenca_pt_relacional(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); src = root / "fonte"; src.mkdir()
            (src / "itens.json").write_text(json.dumps({"itens": [{
                "slug": "arteria-angular", "nome_en": "Angular artery",
                "nome_pt": "artéria angular", "sem_figura": True}],
                "texto": [{"chave": "cap:1", "tipo": "cap",
                           "pt": "A artéria angular acompanha a veia junto ao ângulo medial do olho."}]}))
            cat = root / "lote-005" / "catalogo.json"; cat.parent.mkdir()
            cat.write_text(json.dumps({"units": [{"slug": "face", "source_dir": str(src)}]}))
            out = cat.parent / "catalogo-50.json"
            r = gerar(cat, out, usar_modelo_local=False)
            self.assertEqual(r["resolvidos"], 1)
            card = json.loads(out.read_text())["units"][0]["written_cards"][0]
            self.assertEqual(card["text"], "A {{c1::artéria angular}} acompanha a veia junto ao ângulo medial do olho.")

    def test_nao_inventa_sem_evidencia(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); src = root / "fonte"; src.mkdir()
            (src / "itens.json").write_text(json.dumps({"itens": [{
                "slug": "x", "nome_en": "X", "nome_pt": "xis", "sem_figura": True}], "texto": []}))
            cat = root / "lote-005" / "catalogo.json"; cat.parent.mkdir()
            cat.write_text(json.dumps({"units": [{"slug": "u", "source_dir": str(src)}]}))
            r = gerar(cat, cat.parent / "saida.json", usar_modelo_local=False)
            self.assertEqual(r["pendentes"], 1)


if __name__ == "__main__":
    unittest.main()
