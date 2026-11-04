import json
import tempfile
import unittest
from pathlib import Path

from nebli import formatacao_final as f


class FormatacaoFinalTest(unittest.TestCase):
    def test_parecer_exige_cobertura_hash_e_imagem(self):
        with tempfile.TemporaryDirectory() as directory:
            tmp_path=Path(directory)
            plan={'pipeline_versao':9,'entries':[{'key':'a','origin':'Autoral'}]}
            (tmp_path/'receipt.json').write_text(json.dumps({'notes':[{'key':'a','nid':7}]}))
            note={'noteId':7,'cards':[70], 'fields':{'Text':{'value':'Question'},'Extra':{'value':'<img src="source.png">'}}}
            call=lambda action,**kwargs:[note]
            current=f.preparar(tmp_path,plan,call)
            self.assertFalse(f.verificar(tmp_path,plan,call)[0][1])
            case={**current['a'],'veredito':'aprovado','analise':'Frente e verso legíveis, cloze preciso e imagem conferida.','imagem_vista':True}
            (tmp_path/f.REPORT).write_text(json.dumps({'revisor':{'papel':'independente','execucao':'revisor-1'},'cards':{'a':case}}))
            self.assertTrue(f.verificar(tmp_path,plan,call)[0][1])
            note['fields']['Extra']['value']='<img src="other.png">'
            self.assertFalse(f.verificar(tmp_path,plan,call)[0][1])
