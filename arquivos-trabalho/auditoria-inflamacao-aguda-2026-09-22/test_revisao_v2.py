import json, re, unittest
from preparar_v2 import OUT, strip_clozes, yield_label
from aplicar_v2 import desired_tags, fingerprint

class RevisionTests(unittest.TestCase):
    def test_cloze_selection_keeps_numbers(self):
        self.assertEqual(strip_clozes('{{c1::a}} {{c2::b::hint}} {{c3::<b>x</b>}}',[1,3]),'{{c1::a}} b {{c3::<b>x</b>}}')
    def test_unknown_is_not_low(self):
        self.assertEqual(yield_label([]),('não classificado',[]))
    def test_provisional_is_not_confirmed(self):
        self.assertEqual(yield_label(['#AK_Step1_v12::#Low/HighYield::3-HighYield-temporary'])[0],'HY provisório')
    def test_all_entries_have_source_and_recovery(self):
        p=json.loads((OUT/'plan.json').read_text(encoding='utf-8'))
        for e in p['entries']:
            self.assertTrue(e['pages']);self.assertTrue(e['clozes'])
            self.assertEqual(len(set(e['clozes'])),len(e['clozes']))
            self.assertIn('NEBLI::IA::grupo::', ' '.join(desired_tags(e)))
    def test_visual_answer_not_in_prompt(self):
        p=json.loads((OUT/'plan.json').read_text(encoding='utf-8'))
        for e in p['entries']:
            if e['origin']=='NEBLI-visual':
                self.assertIn('<img ',e['fields']['Text']);self.assertIn('{{c1::',e['fields']['Text'])
    def test_snapshot_fingerprint_detects_history_change(self):
        self.assertNotEqual(fingerprint([{'cardId':1,'reps':2}]),fingerprint([{'cardId':1,'reps':3}]))

if __name__=='__main__':unittest.main()
