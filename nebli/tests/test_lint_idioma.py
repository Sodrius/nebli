"""F-20261105-CODEX-01: UC07 frentePT,ExtraEN; outras corridas continuamEN."""
import unittest
from nebli.lint_cards import check

class IdiomaFrenteTest(unittest.TestCase):
    pt='Na <b>medula espinal</b>,os corpos dos neurônios estão na substância {{c1::cinzenta}}.'
    en='The <b>resident immune cell</b> of the CNS is the {{c1::microglial cell}}.'

    def mensagens(self,front,extra='',idioma='en'):
        return [m for severity,m in check('exemplo',front,extra,front_language=idioma) if severity=='dura']

    def test_padrao_ingles_preservado(self):
        self.assertTrue(any('frente em português' in m for m in self.mensagens(self.pt)))
        self.assertEqual(self.mensagens(self.en),[])

    def test_plano_portugues_aceita_frente_portuguesa(self):
        self.assertEqual(self.mensagens(self.pt,idioma='pt'),[])

    def test_plano_portugues_rejeita_frente_inglesa(self):
        self.assertTrue(any('frente em inglês' in m for m in self.mensagens(self.en,idioma='pt')))

    def test_extra_continua_ingles(self):
        self.assertIn('Extra em português',self.mensagens(self.pt,'As células da glia são responsáveis pela defesa do tecido.',idioma='pt'))
