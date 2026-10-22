import unittest

from nebli import uc07_aula as u

BOM = {"tipo": "au", "chave": "x", "cor": "azul", "busca": "Kenhub 29 e AnKing: sem card", "motivo": "regra da aula",
       "text": "Entre as vértebras <b>C2 e T10</b>, o segmento medular é o da vértebra {{c1::+ 2}}",
       "extra": "- Fratura da vértebra T5 lesa o segmento T7: a medula cresceu menos que a coluna", "img": "a.jpg"}


def aula(*itens):
    return {"prefixo": "02", "tag": "t", "secoes": [("S", list(itens))]}


class Uc07AulaGates(unittest.TestCase):
    def test_autoral_bom_passa(self):
        self.assertEqual(u.checar_autoral(BOM), [])

    def test_autoral_sem_busca_generico_e_verso_repetido_reprovam(self):
        ruim = dict(BOM, busca="", text="A <b>raiz</b> forma o {{c1::nervo}} espinal", extra="- A raiz forma o nervo espinal")
        p = " | ".join(u.checar_autoral(ruim))
        self.assertIn("busca", p)
        self.assertIn("genérica", p)
        self.assertIn("repete a frente", p)

    def test_autoral_sem_negrito_e_sem_figura_reprova(self):
        p = " | ".join(u.checar_autoral(dict(BOM, text="O cone termina em {{c1::L2}}", img=None)))
        self.assertIn("negrito", p)
        self.assertIn("figura", p)

    def test_duas_verdes_na_mesma_estrutura_reprova(self):
        a = aula({"tipo": "keep", "nid": 1, "cor": "verde", "est": "cone"}, {"tipo": "kh", "src": 2, "cor": "verde", "est": "cone"})
        self.assertTrue(any("duas verdes" in x for x in u.checar_plano(a)))

    def test_sem_cor_e_vazio_reprovam(self):
        self.assertTrue(any("cor" in x for x in u.checar_plano(aula({"tipo": "kh", "src": 2}))))
        self.assertTrue(any("vazio" in x for x in u.checar_plano({"secoes": [("S", [])]})))

    def test_termo_sem_card_reprova_e_termo_coberto_passa(self):
        textos = [u.norm("A medula termina no {{c1::cone medular}}")]
        self.assertEqual(u.checar_termos(["cone medular", "cauda equina"], textos), ["cauda equina"])


if __name__ == "__main__":
    unittest.main()
