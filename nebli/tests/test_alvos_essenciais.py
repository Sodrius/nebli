import copy
import unittest
from nebli.verificador_casos import alvos_essenciais, _cards


class AlvosTest(unittest.TestCase):
    def setUp(self):
        self.plan = {"pipeline_versao": 15, "entries": [{"key": "iv", "fields": {
            "Text": '<div data-nebli-organizacao="true">IV: {{c1::T cells}}</div>'}}]}
        self.review = {"cards": {"iv": {"alvos_essenciais": [{
            "cloze": "{{c1::T cells}}", "resposta_esperada": "T cells",
            "essencial": True, "inducao_sem_vazamento": True,
            "porque_dura": "Células T definem o efetor principal desta classe de hipersensibilidade."}],
            "avulsos_cobertos": {"busca": "deck:NEBLI* hypersensitivity", "decisoes": [],
                "nenhum_porquê": "Os candidatos encontrados aprofundam mecanismos diferentes e não repetem este alvo."}}}}

    def test_complete_and_current_passes(self):
        self.assertEqual(alvos_essenciais(self.plan, self.review), [])
        self.assertIn("{{c1::T cells}}", _cards(self.plan, {})[0]["frente_html"])

    def test_missing_secondary_leaked_and_stale_fail(self):
        self.assertTrue(alvos_essenciais(self.plan, {}))
        for field, value in [("essencial", False), ("inducao_sem_vazamento", False),
                             ("cloze", "{{c1::macrophages}}"), ("resposta_esperada", "macrophages")]:
            review = copy.deepcopy(self.review)
            review["cards"]["iv"]["alvos_essenciais"][0][field] = value
            self.assertTrue(alvos_essenciais(self.plan, review), field)

    def test_each_occurrence_and_duplicate_search_required(self):
        self.plan["entries"][0]["fields"]["Text"] += " {{c1::IgE}}"
        self.assertTrue(alvos_essenciais(self.plan, self.review))
        self.setUp()
        del self.review["cards"]["iv"]["avulsos_cobertos"]
        self.assertTrue(alvos_essenciais(self.plan, self.review))

    def test_old_runs_keep_contract(self):
        self.plan["pipeline_versao"] = 14
        self.assertEqual(alvos_essenciais(self.plan, {}), [])
        self.assertNotIn("frente_html", _cards(self.plan, {})[0])
