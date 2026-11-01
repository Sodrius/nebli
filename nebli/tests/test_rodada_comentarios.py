import unittest

from nebli.rodada_comentarios import fala_pendente


class FalaTests(unittest.TestCase):
    def test_pendente_depois_do_ultimo_marcador(self):
        self.assertEqual(fala_pendente("imagem ruim CORRIGIDO, 24, 10, 26. cloze grande"), "cloze grande")
        self.assertEqual(fala_pendente("imagem ruim CORRIGIDO, 24, 10, 26."), "")
        self.assertEqual(fala_pendente("melhorei VISTO, 01, 11, 26."), "")
        self.assertEqual(fala_pendente("bom card"), "bom card")
        self.assertEqual(fala_pendente("faltou organizador CORRIGIDO 22/10/26 (Claude): organizador criado (ce-camadas)"), "")


if __name__ == "__main__":
    unittest.main()
