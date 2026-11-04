"""A leitura do card em tela precisa falhar fechada antes de escrita no Anki."""
import unittest

from nebli.decks import em_tela


class EmTelaSafetyTest(unittest.TestCase):
    def test_sem_revisao_aberta(self):
        def call(action, **params):
            raise RuntimeError('guiCurrentCard: Gui review is not currently active.')
        self.assertEqual(em_tela(call), set())

    def test_erro_de_colecao_nao_parece_tela_vazia(self):
        def call(action, **params):
            raise RuntimeError('guiCurrentCard: A collection operation is active.')
        with self.assertRaisesRegex(RuntimeError, 'collection operation'):
            em_tela(call)

    def test_irmaos_protegidos_pela_nota(self):
        def call(action, **params):
            return {'cardId': 11} if action == 'guiCurrentCard' else [22]
        self.assertEqual(em_tela(call), {22})
