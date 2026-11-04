import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from nebli.lint_cards import check, check_v9
from nebli.gates import organizadores_com_fonte

class QualityV9(unittest.TestCase):
    def test_extra_longo_reprova_sem_cortar_frente(self):
        front='<b>Drug</b> is cleared by {{c1::the liver}}'
        long_extra=' '.join(['mechanism'] * 52)
        self.assertTrue(any(level=='dura' and 'Extra com' in message for level,message in check('x',front,long_extra,version=9)))

    def test_category_hint_and_no_manual_bold(self):
        self.assertEqual(check_v9('<b>Vmax</b> indicates {{c1::efficacy::drug property}}'), [])
        self.assertTrue(check_v9('<b>Vmax</b> indicates {{c1::efficacy::potency or efficacy}}'))
        self.assertTrue(check_v9('<b>Vmax</b> indicates {{c1::<b>efficacy</b>}}'))

    def test_context_is_not_cut_to_word_limit(self):
        front = '<b>T cells</b> require a signal from an antigen presenting cell that binds a receptor on their surface to initiate a sustained process of {{c1::activation}}'
        old = [x for x in check('x', front, version=8) if 'palavras' in x[1]]
        new = [x for x in check('x', front, version=9) if 'palavras' in x[1]]
        self.assertTrue(any(x[0]=='dura' for x in old))
        self.assertTrue(new)
        self.assertTrue(all(x[0]=='aviso' for x in new))

    def test_generic_target_requires_judgment_not_rejection(self):
        front = '<b>Reverse transcriptase</b> makes {{c1::DNA}} from an RNA template'
        self.assertTrue(any(level=='dura' and 'genérica' in msg for level,msg in check('x',front,version=8)))
        self.assertFalse(any(level=='dura' and 'genérica' in msg for level,msg in check('x',front,version=9)))

    def test_organizer_source_must_contain_the_claimed_sequence(self):
        with TemporaryDirectory() as folder:
            source = Path(folder) / 'slide.txt'
            source.write_text('A apresentação ocorre em captura, processamento e exibição do antígeno.')
            entry = {'key':'org','origin':'Autoral','organizador':True,
                     'organizacao_fonte':'slide.txt',
                     'organizacao_trecho':'A apresentação ocorre em captura, processamento e exibição do antígeno.'}
            self.assertTrue(organizadores_com_fonte(folder,{'entries':[entry]})[0][1])
            entry['organizacao_trecho']='A apresentação ocorre em exibição, captura e processamento do antígeno.'
            self.assertFalse(organizadores_com_fonte(folder,{'entries':[entry]})[0][1])
            entry['organizacao_fonte']='../outro.txt'
            self.assertFalse(organizadores_com_fonte(folder,{'entries':[entry]})[0][1])

if __name__ == '__main__':
    unittest.main()
