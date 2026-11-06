import copy
import unittest
from nebli.uc07_cobertura import problemas


class CoberturaUC07(unittest.TestCase):
    def setUp(self):
        self.plan = {'entries': [{'key': 'ponte', 'src': 12, 'origin': 'Kenhub', 'model': 'NEBLI Kenhub IO v1'}]}
        self.data = {'basicos': [{'alvo': 'Ponte', 'fonte': 'Lâmina13', 'cards': ['ponte'],
                                 'estado': 'agora', 'modalidade': 'identificacao', 'kenhub_disponivel': True}],
                     'adiados': [{'alvo': 'NúcleoIII', 'src': 30, 'aula_destino': 'Anatomia03',
                                  'estado': 'previsto', 'motivo': 'IO regional aprofundado'}]}

    def test_vazio_reprova(self):
        self.assertTrue(problemas({}, self.plan))

    def test_basico_faltante_reprova(self):
        self.assertTrue(problemas(self.data, {'entries': []}))

    def test_texto_nao_substitui_kenhub_disponivel(self):
        p = copy.deepcopy(self.plan)
        p['entries'][0].update(origin='AnKing', model='Cloze')
        self.assertTrue(problemas(self.data, p))

    def test_adiado_nao_pode_ser_contado_como_entregue(self):
        d = copy.deepcopy(self.data)
        d['adiados'][0]['estado'] = 'entregue'
        self.assertTrue(problemas(d, self.plan))

    def test_adiado_precisa_destino(self):
        self.data['adiados'][0].pop('aula_destino')
        self.assertTrue(problemas(self.data, self.plan))

    def test_escopo_rastreavel_passa(self):
        self.assertEqual(problemas(self.data, self.plan), [])
