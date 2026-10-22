import unittest

from nebli import nomenclatura as nm

AULA = ["Vias biliares: ducto Colédoco, ducto cístico, papila maior do duodeno, Trígono císto-hepático"]
LIVROS = {"moore": "o ducto pancreático acessório abre-se na papila menor do duodeno"}


class NomenclaturaTest(unittest.TestCase):
    def test_nome_da_aula_passa(self):
        self.assertEqual(nm.conferir([("k", "Ducto colédoco", [])], AULA, LIVROS), [])

    def test_sinonimo_do_kenhub_quando_a_aula_usa_outro_nome_reprova(self):
        p = nm.conferir([("k", "Papila duodenal maior", [])], AULA, LIVROS)
        self.assertTrue(p and "a aula diz" in p[0])
        p = nm.conferir([("k", "Ducto biliar comum", ["Ducto colédoco"])], AULA, LIVROS)
        self.assertTrue(p and "a aula diz" in p[0])

    def test_nome_so_do_livro_passa_e_inventado_reprova(self):
        self.assertEqual(nm.conferir([("k", "Papila menor do duodeno", [])], AULA, LIVROS), [])
        p = nm.conferir([("k", "Bolbo raquidiano", [])], AULA, LIVROS)
        self.assertTrue(p and "livro brasileiro" in p[0])

    def test_qualificador_e_plural(self):
        self.assertEqual(nm.conferir([("k", "Ductos císticos do fígado", [])], AULA + ["fígado"], LIVROS), [])
        p = nm.conferir([("k", "Pirâmides do bulbo raquidiano", [])], ["pirâmides do bulbo"], LIVROS)
        self.assertTrue(p and "raquidiano" in p[0])


if __name__ == "__main__":
    unittest.main()
