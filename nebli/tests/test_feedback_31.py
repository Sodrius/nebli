"""Gates de regressão baseados nos comentários reais de 31/10."""
import unittest
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from nebli.lint_cards import check_v10_feedback, from_plan


class Feedback31Test(unittest.TestCase):
    def test_cloze_mal_fechado(self):
        bad = '<b>Virus isolation</b>: {{c1::cell culture}} / {{c1::laboratory animals}'
        self.assertTrue(any('mal fechado' in msg for _, msg in check_v10_feedback(bad)))
        good = '<b>Virus isolation</b>: {{c1::cell culture}} / {{c1::laboratory animals}}'
        self.assertEqual(check_v10_feedback(good), [])

    def test_cloze_generico_apontado(self):
        self.assertTrue(check_v10_feedback('<b>Viral inclusions</b> pile up at the {{c1::scarcest}} component'))
        self.assertTrue(check_v10_feedback('<b>Inclusions</b> contain {{c1::viral material}}'))

    def test_contexto_tem_de_estar_na_frente(self):
        old = 'The peripheral T-cell rim supports macrophages through {{c1::cytokine signaling}}'
        new = 'In <b>granulomas</b>, the peripheral T-cell rim supports macrophages through {{c1::cytokine signaling}}'
        self.assertTrue(check_v10_feedback(old))
        self.assertEqual(check_v10_feedback(new), [])

    def test_plano_v10_usa_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'plan.json'
            path.write_text(json.dumps({'pipeline_versao': 10, 'entries': [
                {'key': 'au-inclusao', 'origin': 'Autoral',
                 'fields': {'Text': '<b>Viral inclusion</b> stops at the {{c1::scarcest}} component', 'Extra': ''}}
            ]}))
            results = list(from_plan(path))
            errors = next(problems for key, _, _, problems in results if key == 'au-inclusao')
            self.assertTrue(any('inferível' in message for _, message in errors))

    def test_imagem_que_e_texto_nao_passa_com_veredito_ok(self):
        from nebli import gates
        src = 'paste-ab1fe31810f535c3b8f8f6228e11440150723366.jpg'
        plan = {'entries': [{'key': 'meia-vida', 'fields': {'Text': '<b>Half-time</b>',
                  'Extra': f'<img src="{src}">'}}]}
        with patch('nebli.imagens_cards.pendentes', return_value=([], {'meia-vida': {'veredito': 'ok'}})):
            result = gates.imagens_batem('.', plan)[0]
        self.assertFalse(result[1])
        self.assertIn('captura de texto', result[0])
        old = 'Uncoating releases the genome after {{c1::endosomal acidification}}'
        new = 'During <b>viral entry</b>, uncoating may follow {{c1::endosomal acidification}}'
        self.assertTrue(check_v10_feedback(old))
        self.assertEqual(check_v10_feedback(new), [])


if __name__ == '__main__':
    unittest.main()
