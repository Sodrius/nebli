import unittest
from unittest.mock import patch

from nebli.auditoria_cobertura import problemas
from nebli.gates import fidelidade_ao_slide


class AuditoriaCoberturaTest(unittest.TestCase):
    def setUp(self):
        self.comp = {
            "blocos": [{"laminas": [1, 2], "papel": "principio", "aprender": ["A causa B", "B leva a C"]}],
            "fidelidade": {"blocos": [{"laminas": [1, 2], "cards_conferidos": ["a", "sh-9"],
                                      "relacoes": [{"aprender": "A causa B", "estado": "recuperavel", "cards": ["a"]},
                                                   {"aprender": "B leva a C", "estado": "recuperavel", "cards": ["sh-9"]}]}]},
        }
        self.plan = {"entries": [{"key": "a"}], "compartilhados": {"9": {}}}

    def test_cobre_os_dois_sentidos(self):
        self.assertEqual(problemas(self.comp, self.plan), [])

    def test_reprova_relacao_so_no_extra_e_card_nao_conferido(self):
        self.comp["fidelidade"]["blocos"][0]["relacoes"][1]["estado"] = "so_no_extra"
        self.comp["fidelidade"]["blocos"][0]["cards_conferidos"] = ["a"]
        erros = problemas(self.comp, self.plan)
        self.assertTrue(any("não recuperável" in e for e in erros))
        self.assertTrue(any("cards sem conferência" in e for e in erros))

    def test_gate_final_da_versao_13_usa_a_auditoria(self):
        self.comp["fidelidade"]["blocos"][0].update(
            {"bate": True, "nota": "Conferi os dois mecanismos contra as frentes e a fonte da aula."})
        self.comp["fidelidade"]["conclusao"] = ("A aula foi conferida no sentido das relações e no sentido dos cartões, "
                                                   "com mecanismos centrais recuperáveis e sem cartões fora do recorte. "
                                                   "A ordem e o peso dos blocos também foram comparados com a apresentação do professor.")
        self.plan["pipeline_versao"] = 13
        with patch("nebli.gates._compreensao", return_value=self.comp):
            self.assertTrue(all(ok for _, ok in fidelidade_ao_slide(".", self.plan)))
            self.comp["fidelidade"]["blocos"][0]["relacoes"].pop()
            self.assertFalse(fidelidade_ao_slide(".", self.plan)[-1][1])


if __name__ == "__main__":
    unittest.main()
