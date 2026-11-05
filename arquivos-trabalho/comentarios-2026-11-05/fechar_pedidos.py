import json,sys
from pathlib import Path
from datetime import datetime,timezone
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki,escrita,em_tela
from nebli.rodada_comentarios import fala_pendente
A=Anki();R=json.load(open(C/'RODADA.json'));P=json.load(open(C/'propostas.json'));V=json.load(open(C/'render-vivo-conferencia.json'));assert not V['falhas'];rec=[];pending=[];new=json.load(open(C/'novo-scid-recibo.json'))
with escrita(A,'comentários05/11:marcadores após readback e render real',sync=False):
 for item in R['itens']:
  nid=item['nid']
  if nid in [1791630905957,1792787231967]:continue
  if nid in em_tela(A):pending.append({'nid':nid,'motivo':'em tela'});continue
  n=A('notesInfo',notes=[nid])[0];orig=n['fields'].get('NEBLI_Comentario',{}).get('value','')
  if fala_pendente(orig)!=item['fala']:pending.append({'nid':nid,'motivo':'comentário mudou durante a rodada','fala':fala_pendente(orig)});continue
  assert all(n['fields'][k]['value']==v for k,v in P[str(nid)]['fields'].items()),nid
  response=P[str(nid)]['motivo']
  if nid==1791625424233:response+=' Organizador complementar SCID instalado na aula Distúrbios do sistema imune, nota '+str(new['nid'])+'. Frente recupera três mecanismos centrais; apoio cataloga os20genes dos dois grupos IUIS2024, não afirma20genes memorizados.'
  fields={'NEBLI_Comentario':orig+'<br><br>CORRIGIDO, 05, 11, 26.'}
  if 'NEBLI_Resposta'in n['fields']:fields['NEBLI_Resposta']=response
  A('updateNoteFields',note={'id':nid,'fields':fields})
  cmd=[t for t in n['tags']if t.startswith('NEBLI::comando::')]
  if cmd:A('removeTags',notes=[nid],tags=' '.join(cmd))
  after=A('notesInfo',notes=[nid])[0];assert all(after['fields'][k]['value']==v for k,v in fields.items());assert not any(t in after['tags']for t in cmd)
  item['corrigido']=True;rec.append(nid)
(C/'RODADA.json').write_text(json.dumps(R,ensure_ascii=False,indent=1));(C/'fechamento-pedidos.json').write_text(json.dumps({'concluido_em':datetime.now(timezone.utc).isoformat(),'corrigidos':rec,'mudancas_concorrentes':pending},ensure_ascii=False,indent=1));print(len(rec),'pedidos corrigidos;',len(pending),'mudanças concorrentes;2interfacependentes')
