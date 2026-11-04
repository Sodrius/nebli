import json
import tempfile
import unittest
from pathlib import Path
from nebli.contexto_tab import index

class ContextTests(unittest.TestCase):
    def test_shared_legacy_receipt_and_missing_plan(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); run=root/'a';run.mkdir()
            (run/'receipt.json').write_text(json.dumps({'notes':7}))
            plan={'entries':[],'compartilhados':{'42':{'alvo':'recognize the transition'}},'escopo':{'objetivo':'follow the process'}}
            (run/'plan-aplicado.json').write_text(json.dumps(plan))
            (run/'motivacoes.json').write_text(json.dumps({'motivacoes':[{'atendida_por':['sh-42'],'reconstruir':'explain cause and effect'}]}))
            result=index(root)
            self.assertEqual(result[42]['reconstruir'],['explain cause and effect'])
            self.assertIn('não tomar',result[42]['natureza'])
            self.assertNotIn(43,result)

if __name__=='__main__':unittest.main()
