import unittest
from nebli.gates import past_errors

class BlocoCompartilhado(unittest.TestCase):
    def check_bloco(self, field):
        plan={'entries':[{'key':'io','kind':'kenhub','origin':'Kenhub','bloco':'A-1','evid':'Slide 1','fields':{'Nome PT':'Tálamo'},'cards':[{'flag':3}]}], 'compartilhados':{'1':{'bloco':'A-1','evid':'Slide 1','fields':field}}}
        return next(ok for label,ok in past_errors(plan) if label.startswith('cada bloco tem cards de texto'))
    def test_relacao_preservada_conta_no_bloco(self):
        self.assertTrue(self.check_bloco({'Text':'O tálamo forma a parede do {{c1::terceiro ventrículo}}.'}))
    def test_io_sozinho_nao_vira_relacao(self):
        self.assertFalse(self.check_bloco({'Nome PT':'Tálamo'}))
    def test_identificacao_textual_nao_vira_relacao(self):
        self.assertFalse(self.check_bloco({'Text':'ID do vaso: {{c1::basilar}}'}))

    def test_basic_relacional_tambem_conta(self):
        self.assertTrue(self.check_bloco({'Front':'Qual artéria irriga o bulbo lateral?'}))
    def test_front_so_imagem_nao_conta(self):
        self.assertFalse(self.check_bloco({'Front':'<img src="atlas.png">'}))
