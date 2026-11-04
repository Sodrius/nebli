import hashlib,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from nebli.correcoes_vigentes import verificar
class RegressionTests(unittest.TestCase):
 def test_split_siblings_block_reapply_to_one_deck(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);run=root/'run';run.mkdir();registry=root/'registry.json'
   content=root/'content.json';content.write_text(json.dumps({'status':'aplicado_verificado','notas':[]}))
   position=root/'position.json';position.write_text(json.dumps({'status':'aplicado_verificado'}))
   sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
   registry.write_text(json.dumps({'revisoes':[{'recibo':'content.json','sha256':sha(content)}],
     'posicoes':[{'nid':9,'recibo':'position.json','sha256':sha(position),
                  'cards':{'91':'deck A','92':'deck B'}}]}))
   (run/'receipt.json').write_text(json.dumps({'notes':[{'key':'a','nid':9}]}))
   plan={'deck':'deck B','entries':[{'key':'a','fields':{}}],'compartilhados':{}}
   with patch('nebli.correcoes_vigentes.ROOT',root):
    result=verificar(run,plan,registry)
    self.assertFalse(result[0][1]);self.assertIn('irmãos em decks diferentes',result[0][0])
    plan['entries']=[];self.assertTrue(verificar(run,plan,registry)[0][1])
 def test_stale_content_and_retired_shared_fail(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);run=root/'run';run.mkdir();receipt=root/'aplicado.json';registry=root/'registry.json'
   receipt.write_text(json.dumps({'status':'aplicado_verificado','notas':[{'nid':1,'campos':{'Text':'correct'}},{'nid':2,'retirado':True}]}))
   registry.write_text(json.dumps({'revisoes':[{'recibo':'aplicado.json','sha256':hashlib.sha256(receipt.read_bytes()).hexdigest()}]}))
   (run/'receipt.json').write_text(json.dumps({'notes':[{'key':'a','nid':1}]}))
   plan={'entries':[{'key':'a','fields':{'Text':'old'}}],'compartilhados':{}}
   with patch('nebli.correcoes_vigentes.ROOT',root):
    self.assertFalse(verificar(run,plan,registry)[0][1]);plan['entries'][0]['fields']['Text']='correct';self.assertTrue(verificar(run,plan,registry)[0][1]);plan['compartilhados']['2']={};self.assertFalse(verificar(run,plan,registry)[0][1]);receipt.write_text('{}');self.assertFalse(verificar(run,plan,registry)[0][1])
if __name__=='__main__':unittest.main()
