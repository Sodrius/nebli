"""UC07: a ausência autorizada não pode fingir uso de provas nem ocultar questões."""
import json,tempfile,unittest
from pathlib import Path
from nebli.gates import _provas_ausentes_autorizadas,linha_e_provas

class ProvasAusentesTest(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.run=Path(self.tmp.name);(self.run/'fontes').mkdir()
  self.esc={'provas_ausentes':{'autorizado_por':'Davi confirmou que ainda não tem provas e autorizou seguir com aula e bibliografia.'}}
  self.fonte={'familias':{'provas':{'estado':'não localizada','busca':'Busca na pasta da aula e nos materiais da UC sem provas ou gabaritos.','impacto':'Não estimar recorrência; aula e bibliografia constituem a base disponível.'}}}
  self.write()
 def write(self):
  (self.run/'fontes-decl.json').write_text(json.dumps(self.fonte));(self.run/'escopo.json').write_text(json.dumps(self.esc))
 def test_ausencia_com_busca_e_autorizacao(self):
  self.assertTrue(_provas_ausentes_autorizadas(self.run,self.esc))
  self.assertTrue(linha_e_provas(self.run,{'entries':[]})[-1][1])
 def test_sem_autorizacao_nao_dispensa(self):
  self.assertFalse(_provas_ausentes_autorizadas(self.run,{}))
 def test_fonte_lida_nao_e_ausente(self):
  self.fonte['familias']['provas']['estado']='lido';self.write();self.assertFalse(_provas_ausentes_autorizadas(self.run,self.esc))
 def test_questao_disponivel_nao_pode_ser_ocultada(self):
  (self.run/'fontes/provas-indice.txt').write_text('── [P1] Q01 questão disponível\n');self.assertFalse(_provas_ausentes_autorizadas(self.run,self.esc));self.assertFalse(linha_e_provas(self.run,{'entries':[]})[-1][1])
