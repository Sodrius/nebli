"""Instala somente o complemento aprovado,sem apagar/recriar notas estudadas."""
from pathlib import Path
import sys,json,sqlite3,base64,hashlib,time
from datetime import datetime,timezone
D=Path(__file__).resolve().parent;R=D.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita,em_tela
from nebli.rotulos import canonical
from nebli.delta import same
from nebli import gates,etapa,revisor_autorais,verificador_casos,uc07_cobertura
A=Anki();P=json.loads((R/'plan.json').read_text());OLD=json.loads((D/'antes-receipt.json').read_text());TAG='NEBLI::'+P['lesson_id'];DECK=P['deck']
def get(p):return json.loads(p.read_text())
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
def snap(path):
 src=Path.home()/'Library/Application Support/Anki2/User 1/collection.anki2'
 with sqlite3.connect('file:'+str(src)+'?mode=ro',uri=True) as db:
  with sqlite3.connect(path) as dst:db.backup(dst)
def dbrows(path,table,ids,col='id'):
 with sqlite3.connect('file:'+str(path)+'?mode=ro&immutable=1',uri=True) as db:
  db.row_factory=sqlite3.Row
  return [dict(x) for x in db.execute('select * from '+table+' where '+col+' in ('+','.join('?' for _ in ids)+')',list(ids))]
def multi(actions):
 if not actions:return []
 vals=A('multi',actions=actions)
 for a,v in zip(actions,vals):
  if isinstance(v,dict) and v.get('error'):raise RuntimeError(a['action']+': '+v['error'])
 return [v['result'] if isinstance(v,dict) and 'result' in v else v for v in vals]
def check_pre():
 gates.RUN['dir']=R;checks=[]
 for f in (gates.cobertura_anking,gates.profundidade,gates.linha_e_provas,gates.compreensao_aula,gates.motivacao_autorais,gates.organizadores_com_fonte,gates.imagens_batem,gates.imagens_legiveis,gates.revisao_raciocinio,gates.fidelidade_ao_slide,revisor_autorais.verificar,verificador_casos.verificar,uc07_cobertura.verificar):checks+=f(R,P)
 checks+=gates.exemplares_lidos(R)+gates.source_evidence(R,get(R/'fontes.json'))
 bad=[k for k,v in checks if not v];missing,wrong=etapa.ordem_ok(R,'E7')
 put(D/'preflight-aplicacao.json',{'checks':checks,'at':datetime.now(timezone.utc).isoformat()})
 if bad or missing or wrong:raise RuntimeError('Pré-instalação bloqueada: '+str(bad+missing+wrong))
def valid_cards(n,info,fields):
 if 'Text' not in fields:return n['cards']
 import re
 ords={int(x)-1 for x in re.findall(r'\{\{c(\d+)::',fields['Text'])}
 return [cid for cid in n['cards'] if info[cid]['ord'] in ords]
def main():
 check_pre();oldmap={n['key']:n['nid'] for n in OLD['notes']};state=get(D/'aplicacao-estado.json') if (D/'aplicacao-estado.json').exists() else {'criados':{}}
 known={**oldmap,**state['criados']};nids=set(known.values())|set(map(int,P['compartilhados']));notes=A('notesInfo',notes=sorted(nids));live={n['noteId']:n for n in notes};ci=A('cardsInfo',cards=[c for n in notes for c in n['cards']]);ciby={c['cardId']:c for c in ci}
 baseline={nid:{k:v['value'] for k,v in n['fields'].items()} for nid,n in live.items()};put(D/'notas-pre-aplicacao.json',notes);put(D/'cards-pre-aplicacao.json',ci)
 backup=D/'collection-pre-aplicacao.anki2'
 if not backup.exists():snap(backup)
 oldcids={c['cardId'] for c in ci};rawbefore={x['id']:x for x in dbrows(backup,'cards',oldcids)};revbefore=dbrows(backup,'revlog',oldcids,'cid')
 if any(rawbefore[c]['odid'] for c in rawbefore):raise RuntimeError('Há cards afetados em estudo filtrado; preparar migração sem interromper esse estudo antes de aplicar.')
 E={e['key']:e for e in P['entries']};wanted={known[k]:e['fields'] for k,e in E.items() if k in known};wanted.update({int(n):s['fields'] for n,s in P['compartilhados'].items()});control=('Text','Extra','Nome PT','Pergunta','Imagem','MascaraP','MascaraR')
 media=Path(A('getMediaDirPath'));newmedia=[]
 for name,rel in P['media'].items():
  src=R/rel
  if not (media/name).exists() or (media/name).read_bytes()!=src.read_bytes():newmedia.append((name,base64.b64encode(src.read_bytes()).decode()))
 with escrita(A,'UC07 Anatomia01: complemento de cobertura e Kenhub',sync=False):
  if em_tela(A)&nids:raise RuntimeError('Uma nota afetada está em tela; nenhuma escrita iniciada.')
  fresh=A('notesInfo',notes=sorted(nids))
  for n in fresh:
   for f in control:
    now=n['fields'].get(f,{}).get('value')
    if now is not None and not same(now,baseline[n['noteId']].get(f,'')):raise RuntimeError('Edição concorrente no campo '+f+' da nota '+str(n['noteId']))
  # O preset existente tem de preservar os passos de aprendizagem; não alterar opções de Davi.
  cfg=A('getDeckConfig',deck=DECK)
  if cfg is False:raise RuntimeError('Deck de destino não encontrado na janela canônica.')
  target_cfg=cfg['id'];learning_decks={canonical(c['deckName']) for c in ci if c['queue'] in (1,3) and canonical(c['deckName'])!=DECK}
  for dn in learning_decks:
   if A('getDeckConfig',deck=dn)['id']!=target_cfg:raise RuntimeError('Preset de aprendizagem divergente: preparar migração preservadora para '+dn)
  multi([{'action':'storeMediaFile','params':{'filename':name,'data':data}} for name,data in newmedia])
  todo=[e for e in P['entries'] if e['key'] not in known]
  if todo:
   created=A('addNotes',notes=[{'deckName':DECK,'modelName':e['model'],'fields':e['fields'],'tags':e['tags']+['NEBLI::auditoria-uc07-20261106::'+e['key']],'options':{'allowDuplicate':True}} for e in todo])
   for e,nid in zip(todo,created):
    if nid:state['criados'][e['key']]=nid
   put(D/'aplicacao-estado.json',state)
   if any(not n for n in created):raise RuntimeError('Criação parcial registrada; reconciliar antes de retomar.')
   known.update(state['criados'])
  actions=[]
  for nid,fields in wanted.items():
   upd={f:v for f,v in fields.items() if f in control and f in baseline[nid] and not same(v,baseline[nid][f])}
   if upd:actions.append({'action':'updateNoteFields','params':{'note':{'id':nid,'fields':upd}}})
  multi(actions)
  allnids=set(known.values())|set(map(int,P['compartilhados']));after=A('notesInfo',notes=sorted(allnids));by={n['noteId']:n for n in after};cs=A('cardsInfo',cards=[c for n in after for c in n['cards']]);cc={c['cardId']:c for c in cs};selected=[];actions=[]
  for e in P['entries']:
   nid=known[e['key']];n=by[nid];fs={k:v['value'] for k,v in n['fields'].items()};selected+=valid_cards(n,cc,fs)
   if e['key'] in state['criados']:
    for cid in n['cards']:
     flag=next(c['flag'] for c in e['cards'] if c['ord']==cc[cid]['ord']);actions.append({'action':'setSpecificValueOfCard','params':{'card':cid,'keys':['flags'],'newValues':[flag],'warning_check':True}})
  for nid,s in P['compartilhados'].items():
   n=by[int(nid)];selected+=valid_cards(n,cc,{k:v['value'] for k,v in n['fields'].items()})
  multi(actions)
  moves=[c for c in selected if canonical(cc[c]['deckName'])!=DECK]
  if moves:A('changeDeck',cards=moves,deck=DECK)
  # Ordem é metadado da aula; não tocar bandeiras ou suspensões dos reusos.
  actions=[]
  for e in P['entries']+[dict(s,key='sh-'+nid,nid=int(nid)) for nid,s in P['compartilhados'].items()]:
   nid=e.get('nid',known.get(e['key']));oldtags=by[nid]['tags'];stale=[t for t in oldtags if t.startswith('NEBLI::ordem::'+P['short']+'-')];want=e.get('ordem_tag') or next(t for t in e['tags'] if t.startswith('NEBLI::ordem::'+P['short']+'-'))
   if stale!=[want]:
    if stale:actions.append({'action':'removeTags','params':{'notes':[nid],'tags':' '.join(stale)}})
    actions.append({'action':'addTags','params':{'notes':[nid],'tags':want}})
   if 'nid' in e:actions.append({'action':'addTags','params':{'notes':[nid],'tags':TAG+' NEBLI::compartilhado::'+P['short']+' NEBLI::cor::'+P['lesson_id']+'::'+e['cor']}})
  multi(actions)
  khnotes=[known[e['key']] for e in P['entries'] if 'nebli-u7an01-cavidade-' in str(e['fields']) or e.get('origin')=='Kenhub']
  if khnotes:A('addTags',notes=khnotes,tags='NEBLI::fonte::kenhub')
  read=A('notesInfo',notes=sorted(allnids));readby={n['noteId']:n for n in read};probs=[]
  for nid,fields in wanted.items():
   for f,v in fields.items():
    if f in control and f in readby[nid]['fields'] and not same(v,readby[nid]['fields'][f]['value']):probs.append(str(nid)+':'+f)
  for nid,fs in baseline.items():
   for f in ('NEBLI_Comentario','NEBLI_Resposta'):
    if f in fs and readby[nid]['fields'][f]['value']!=fs[f]:probs.append(str(nid)+': pessoal '+f)
  snap(D/'collection-pos-aplicacao.anki2');rawafter={x['id']:x for x in dbrows(D/'collection-pos-aplicacao.anki2','cards',oldcids)};logafter={x['id']:x for x in dbrows(D/'collection-pos-aplicacao.anki2','revlog',oldcids,'cid')}
  for cid,b in rawbefore.items():
   for f in ('type','queue','due','ivl','factor','reps','lapses','left','odue','odid','flags','data'):
    if f=='due' and b['type']==0 and b['reps']==0 and cid in selected:continue
    if rawafter[cid][f]!=b[f]:probs.append(str(cid)+': agendamento '+f)
  if any(logafter.get(v['id'])!=v for v in revbefore):probs.append('histórico anterior divergente')
  receipt=[]
  finalcards=A('cardsInfo',cards=selected);fc={c['cardId']:c for c in finalcards}
  for e in P['entries']:
   nid=known[e['key']];receipt.append({'key':e['key'],'nid':nid,'cards':{str(c):{'ord':fc[c]['ord'],'flag':fc[c]['flags']} for c in readby[nid]['cards'] if c in fc}})
  rec={'run_id':P['run_id'],'selection_hash':P['selection_hash'],'deck':DECK,'notes':receipt,'expected':len(selected),'cards_new_lesson':sum(len(x['cards']) for x in receipt),'compartilhados_tag':list(P['compartilhados']),'cards_tag_aula':len(A('findCards',query='tag:'+TAG)),'problems':probs,'historico_preservado':not probs,'at':datetime.now(timezone.utc).isoformat()}
  put(D/'integridade-aplicacao.json',{'problemas':probs,'cards_anteriores':len(oldcids),'revisoes_anteriores':len(revbefore),'novas_notas':len(state['criados']),'movidos':moves});put(R/'receipt.json',rec);put(R/'plan-aplicado.json',P);put(D/'notas-pos-aplicacao.json',read)
  if probs:raise RuntimeError(str(probs))
  state.update(concluido=True,selection_hash=P['selection_hash']);put(D/'aplicacao-estado.json',state)
  print(json.dumps({'novas_notas':len(state['criados']),'cards_deck':len(selected),'movidos':len(moves),'historico_preservado':True}))
if __name__=='__main__':main()
