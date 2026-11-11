import unittest
from nebli.uc07_prioridades import bandeira, verificar

class UC07Prioridades(unittest.TestCase):
    def test_origem_nao_tipo_anking(self):
        self.assertEqual(bandeira('NEBLI AnKing independente - v3',{},'Autoral'),5)
        self.assertEqual(bandeira('NEBLI AnKing independente - v3',{},'AnKing'),4)
        self.assertEqual(bandeira('NEBLI AnKing independente - v3',{},'AnKing-MCAT'),4)
    def test_identificacao_visual_prevalece(self):
        self.assertEqual(bandeira('NEBLI Kenhub IO v1',{},'Kenhub'),3)
        self.assertEqual(bandeira('NEBLI Kenhub Referência v1',{},'Kenhub'),3)
        self.assertEqual(bandeira('AnKing',{'Text':'Qual estrutura a seta indica? {{c1::ponte}}'},'AnKing'),3)
        self.assertEqual(bandeira('AnKing',{'Text':'Lesão da ponte causa {{c1::déficit}}'},'Kenhub'),5)
    def test_reprova_vazio_e_cor_errada(self):
        self.assertTrue(verificar({}))
        p={'entries':[{'key':'org','model':'AnKing','fields':{},'origin':'Autoral','cards':[{'flag':3}]}]}
        self.assertTrue(verificar(p))
        p['entries'][0]['cards'][0]['flag']=5
        self.assertEqual(verificar(p),[])

    def test_gate_roteia_uc07(self):
        from nebli.gates import cores_rubrica
        p={'deck':'NEBLI::UC07::P1::Anatomia::04', 'entries':[
            {'key':'org','model':'AnKing','fields':{},'origin':'Autoral','cards':[{'flag':3,'cor':'verde'}]}]}
        self.assertFalse(cores_rubrica(p)[0][1])
        p['entries'][0]['cards'][0].update(flag=5,cor='rosa')
        self.assertTrue(cores_rubrica(p)[0][1])
