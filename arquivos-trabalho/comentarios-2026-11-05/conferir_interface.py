"""Teste na janela real Qt, só no card técnico; nenhuma resposta/X é registrada."""
import sys,json,time
from pathlib import Path
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki,escrita,em_tela
BASE=Anki()
def A(action,**params):
 for _ in range(60):
  try:return BASE(action,**params)
  except RuntimeError as exc:
   if 'collection operation'not in str(exc).lower()and 'collection lifecycle'not in str(exc).lower():raise
   time.sleep(.25)
 raise RuntimeError('operação da coleção não liberou')
testflag=int(sys.argv[1])if len(sys.argv)>1 else 4
cid=1793630055890;before=A('cardsInfo',cards=[cid])[0];assert not em_tela(A),'Não interromper revisão de Davi';req=C.parents[0]/'anki-acao-pedido.json';resp=C.parents[0]/'anki-acao-resposta.json';assert not req.exists()
def pedir(action):
 data={'acao':action,'deck':'NEBLI Teste gestos','teste':'interface05/11'}
 with escrita(A,'interface: operação apenas no deck técnico',sync=False):
  req.write_text(json.dumps(data))
  for _ in range(70):
   if resp.exists():
    r=json.load(open(resp))
    if r.get('pedido')==data:return r
   time.sleep(.25)
  raise RuntimeError('operação técnica sem resposta')
created=False
try:
 A('guiDeckBrowser')
 with escrita(A,'bandeira técnica para conferir coração',sync=False):A('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[testflag],warning_check=True)
 r=pedir('estudar');created=True
 A('guiDeckReview',name=r['nome'])
 for _ in range(30):
  try:
   if A('guiCurrentCard')['cardId']==cid:break
  except RuntimeError:pass
  time.sleep(.25)
 assert A('guiCurrentCard')['cardId']==cid
 for liked in [False,True]:
  out=C/('interface-flag'+str(testflag)+'-gostei-'+str(liked).lower()+'.png');meta=out.with_suffix('.json');meta.unlink(missing_ok=True)
  req.write_text(json.dumps({'acao':'capturar_interface','arquivo':str(out),'simular_gostei':liked,'recarregar_funcao_badge':True}))
  for _ in range(60):
   if meta.exists():break
   time.sleep(.25)
  assert meta.exists(),'Captura Qt não respondeu';print(meta.read_text(),flush=True)
finally:
 A('guiDeckBrowser');time.sleep(.5)
 if created:pedir('encerrar')
 with escrita(A,'restaurar bandeira técnica',sync=False):A('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[before['flags']],warning_check=True)
after=A('cardsInfo',cards=[cid])[0];assert all(before[k]==after[k]for k in ['reps','lapses','due','queue','type','flags','factor','interval','left'])
print('Técnico restaurado;nenhuma resposta ouX registrado')
