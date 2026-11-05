import json,sys,sqlite3
from pathlib import Path
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki,escrita,em_tela
from nebli.qualidade_comentarios import badge_layout_ok
from nebli import explicacoes
A=Anki();R=json.load(open(C/'RODADA.json'));checked=[]
for f in [0,4]:
 for liked in ['false','true']:
  r=json.load(open(C/f'interface-flag{f}-gostei-{liked}.json'));assert r['salvo']and badge_layout_ok(r['badge']);checked.append(r)
ids=[1791630905957,1792787231967];ns=A('notesInfo',notes=ids);cids=[c for n in ns for c in n['cards']];db=explicacoes.open_store();tabs=db.execute('select card_id,texto,status from explicacoes where card_id in ('+','.join('?'for _ in cids)+')',cids).fetchall();assert len(tabs)==3
for cid,text,status in tabs:assert status=='ok'and not explicacoes.problema_estilo(text)
# Os três textos foram lidos pelo executor e permanecem corretos para as frentes/Extras,
# que não mudaram. Só os campos de comentário/resposta serão alterados.
with escrita(A,'fechar2pedidos de interface após captura real Qt',sync=False):
 for n in ns:
  nid=n['noteId'];assert nid not in em_tela(A)
  t=n['fields']['NEBLI_Comentario']['value'];fields={'NEBLI_Comentario':t+'<br><br>CORRIGIDO, 05, 11, 26.'}
  if 'NEBLI_Resposta'in n['fields']:fields['NEBLI_Resposta']='Corrigido e conferido na janela real do Anki: seletor nativo #_flag,12px entre coração e bandeira; sem bandeira o coração permanece visível. Quatro estados capturados em card técnico,sem respostas nem gosteis registrados. Código instalado para o próximo reinício e função atual testada.'
  A('updateNoteFields',note={'id':nid,'fields':fields})
  it=next(i for i in R['itens']if i['nid']==nid);it['corrigido']=True;it['causa']='O seletor antigo não encontrava #_flag nativo e caía numa posição sobre a bandeira. Quando a bandeira estava oculta,o retângulo zero colocava o coração fora da tela. Agora a geometria visível determina a âncora e há posição alternativa segura.'
  it['prevencao']={'gate':'qualidade_comentarios.badge_layout_ok','indicacao':'Coração de gostei usa #_flag nativo, mede sua geometria visível e mantém posição segura sem bandeira; testar oito combinações de largura/bandeira/gostei e conferir a janela real.','exemplo':'Antes: sobreposição na bandeira oux negativo sem bandeira → depois:12px com bandeira e coração visível sem ela.'}
for c in A('cardsInfo',cards=cids):
 ordered=[v['value']for v in sorted(c['fields'].values(),key=lambda f:f['order'])];db.execute('update explicacoes set hash=? where card_id=?',(explicacoes.card_hash(ordered,c['ord']),c['cardId']))
db.commit();db.close();R['sync']=False;(C/'RODADA.json').write_text(json.dumps(R,ensure_ascii=False,indent=1));(C/'interface-final-recibo.json').write_text(json.dumps({'capturas':checked,'pedidos_fechados':ids,'tabs_preservados_apos_leitura':cids,'sem_respostas_ou_gosteis_novos':True},ensure_ascii=False,indent=1));print('2pedidos fechados;3Tabs auditados preservados;4capturas reais aprovadas')
