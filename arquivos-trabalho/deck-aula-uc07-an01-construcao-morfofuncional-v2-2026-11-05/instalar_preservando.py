"""E8: instalação retomável,backup fresco,reserva e readback; nunca apaga notas."""
from pathlib import Path
import sys,json,base64,sqlite3,hashlib,time
from datetime import datetime,timezone
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita,em_tela
from nebli.rotulos import canonical
from nebli import gates,etapa,revisor_autorais,verificador_casos,auditoria_cobertura
_em_tela=em_tela
def em_tela(a):
 for attempt in range(20):
  try:return _em_tela(a)
  except RuntimeError as exc:
   if 'collection operation is active' not in str(exc).lower():raise
   time.sleep(.5)
 raise RuntimeError('Coleção ocupada; não inferir ausência de nota em tela.')
A=Anki();P=json.loads((R/'plan.json').read_text());D=P['deck'];TAG='NEBLI::'+P['lesson_id'];S=P['compartilhados'];statepath=R/'instalacao-estado.json'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
def multi(actions):
 out=A('multi',actions=actions)
 for a,v in zip(actions,out):
  if isinstance(v,dict) and v.get('error'):raise RuntimeError(str(a['action'])+':'+str(v['error']))
 return [v['result'] if isinstance(v,dict) and 'result' in v else v for v in out]
def snapshot(path):
 src=Path.home()/'Library/Application Support/Anki2/User 1/collection.anki2'
 with sqlite3.connect('file:'+str(src)+'?mode=ro',uri=True) as db:
  with sqlite3.connect(path) as out:db.backup(out)
def rows(path,table,ids,column='id'):
 with sqlite3.connect('file:'+str(path)+'?mode=ro&immutable=1',uri=True) as db:
  db.row_factory=sqlite3.Row
  return [dict(x) for x in db.execute('select * from '+table+' where '+column+' in ('+','.join('?' for _ in ids)+')',ids)]
def preflight():
 gates.RUN['dir']=R
 checks=[]
 for fn in (gates.cobertura_anking,gates.profundidade,gates.linha_e_provas,gates.compreensao_aula,gates.motivacao_autorais,gates.organizadores_com_fonte,gates.imagens_batem,gates.exemplares_lidos,gates.revisao_raciocinio,gates.fidelidade_ao_slide,revisor_autorais.verificar,verificador_casos.verificar):
  checks+=fn(R,P) if fn!=gates.exemplares_lidos else fn(R)
 checks+=gates.source_evidence(R,json.loads((R/'fontes.json').read_text()))
 bad=[k for k,v in checks if not v];missing,wrong=etapa.ordem_ok(R,'E7')
 if bad or missing or wrong:raise RuntimeError('Pré-instalação bloqueada: '+str(bad+missing+wrong))
 save(R/'preflight-instalacao.json',{'checks':checks,'etapas':'E0–E7','em':datetime.now(timezone.utc).isoformat()})
def main():
 preflight()
 if (R/'receipt.json').exists() and not json.loads((R/'receipt.json').read_text()).get('problems'):raise RuntimeError('Já instalado: revisar recibo,não reaplicar.')
 state=json.loads(statepath.read_text()) if statepath.exists() else {'notes':[],'movidos':False}
 with escrita(A,'UC07 Anatomia01: instalação com preservação',sync=False):
  old=json.loads((R/'backup-uc07/cards.json').read_text());ids=[x['cardId'] for x in old];nids={x['note'] for x in old};sharedids=set(map(int,S))
  if em_tela(A)&nids:raise RuntimeError('Nota UC07 em tela; aguardar sua saída e retomar com segurança.')
  fresh=R/'backup-uc07/pre-instalacao';fresh.mkdir(exist_ok=True)
  if not (fresh/'collection.anki2').exists():
   snapshot(fresh/'collection.anki2');save(fresh/'cards.json',A('cardsInfo',cards=ids));save(fresh/'notes.json',A('notesInfo',notes=sorted(nids)));save(fresh/'revlog.json',rows(fresh/'collection.anki2','revlog',ids,'cid'))
  if not (fresh/'revlog.json').exists():save(fresh/'revlog.json',rows(fresh/'collection.anki2','revlog',ids,'cid'))
  baseline=json.loads((fresh/'cards.json').read_text());save(R/'before.json',{'compartilhados':{str(n):{'decks':sorted({canonical(c['deckName']) for c in baseline if c['note']==n}),'cards':{str(c['cardId']):c['flags'] for c in baseline if c['note']==n}} for n in sharedids}})
  for name,rel in P['media'].items():
   A('storeMediaFile',filename=name,data=base64.b64encode((R/rel).read_bytes()).decode())
  A('createDeck',deck=D)
  cfg=A('getDeckConfig',deck='NEBLI');chain=['::'.join(D.split('::')[:i]) for i in range(2,len(D.split('::'))+1)];A('setDeckConfigId',decks=chain,configId=1)  # Preset original UC07: conserva passos de aprendizagem.
  done={x['key'] for x in state['notes']}
  todo=[e for e in P['entries'] if e['key'] not in done]
  if todo:
   new=A('addNotes',notes=[{'deckName':D,'modelName':e['model'],'fields':e['fields'],'tags':e['tags'],'options':{'allowDuplicate':True}} for e in todo])
   for e,nid in zip(todo,new):
    if nid:state['notes'].append({'key':e['key'],'nid':nid})
   save(statepath,state)
   if any(not x for x in new):raise RuntimeError('Criação parcial registrada; não repetir sem reconciliar.')
  planned={e['key']:e for e in P['entries']};live=A('notesInfo',notes=[x['nid'] for x in state['notes']]);liveby={n['noteId']:n for n in live};ci=A('cardsInfo',cards=[c for n in live for c in n['cards']]);ciby={c['cardId']:c for c in ci};actions=[]
  for x in state['notes']:
   n=liveby[x['nid']];e=planned[x['key']]
   if sorted(ciby[c]['ord'] for c in n['cards'])!=sorted(c['ord'] for c in e['cards']):raise RuntimeError('Irmãos divergentes:'+e['key'])
   for c in n['cards']:
    flag=next(v['flag'] for v in e['cards'] if v['ord']==ciby[c]['ord']);actions.append({'action':'setSpecificValueOfCard','params':{'card':c,'keys':['flags'],'newValues':[flag],'warning_check':True}})
  multi(actions)
  if em_tela(A)&nids:raise RuntimeError('Nota em tela mudou; instalação nova salva,reserva aguardando.')
  # Não sobrescrever comentários pessoais nem alterações posteriores de outro executor.
  shared=A('notesInfo',notes=sorted(sharedids));updates=[]
  for n in shared:
   s=S[str(n['noteId'])];current={k:v['value'] for k,v in n['fields'].items()};wanted={k:v for k,v in s['fields'].items() if k in ('Text','Extra','Nome PT','Pergunta') and k in current};updates.append({'action':'updateNoteFields','params':{'note':{'id':n['noteId'],'fields':wanted}}})
  multi(updates)
  multi([{'action':'addTags','params':{'notes':[int(n)],'tags':TAG+' NEBLI::compartilhado::'+P['short']+' '+s['ordem_tag']+' NEBLI::cor::'+P['lesson_id']+'::'+s['cor']}} for n,s in S.items()])
  groups={};manifest=[]
  for c in baseline:
   dest=D if c['note'] in sharedids else 'Referências::Referências Externas::Reserva histórica UC07 antes da refação 2026-11-05::'+canonical(c['deckName']).removeprefix('NEBLI::UC07::')
   groups.setdefault(dest,[]).append(c['cardId']);manifest.append({'card':c['cardId'],'nid':c['note'],'origem':c['deckName'],'destino':dest})
  save(R/'movimentacao-uc07.json',manifest)
  for dest,cards in ([] if state.get("movidos") else groups.items()):
   if em_tela(A)&{c['note'] for c in baseline if c['cardId'] in cards}:raise RuntimeError('Nota em tela protegida; retomar reserva depois.')
   A('createDeck',deck=dest)
   A('changeDeck',cards=cards,deck=dest)
  # Reusos antigos já estavam na reserva histórica anterior; reunir também os seus cards.
  sc=A('notesInfo',notes=sorted(sharedids));extraids=sorted({c for n in sc for c in n['cards']}-set(ids))
  if extraids:
   extras=A('cardsInfo',cards=extraids);save(fresh/'compartilhados-reserva-anterior.json',extras)
   if em_tela(A)&{c['note'] for c in extras}:raise RuntimeError('Compartilhado em tela protegido.')
   A('changeDeck',cards=extraids,deck=D)
  state['movidos']=True;save(statepath,state)
  after=A('cardsInfo',cards=ids);by={c['cardId']:c for c in after};problems=[]
  for c in baseline:
   for k in ('queue','type','due','interval','factor','reps','lapses','left','flags'):
    if k=='due' and c.get('type')==0:continue  # Posição de novo muda com reorganização; não é vencimento de revisão.
    if k in c and by[c['cardId']].get(k)!=c[k]:problems.append(str(c['cardId'])+':'+k)
  for n in A('notesInfo',notes=sorted(sharedids)):
   wanted=S[str(n['noteId'])]['fields']
   if any(n['fields'][k]['value']!=wanted[k] for k in ('Text','Extra','Nome PT','Pergunta') if k in wanted and k in n['fields']):problems.append('compartilhado:'+str(n['noteId']))
  # Todas as revisões anteriores continuam presentes,sem recriar notas estudadas.
  snapshot(fresh/'collection-depois.anki2');beforelog=json.loads((fresh/'revlog.json').read_text());afterlog={v['id']:v for v in rows(fresh/'collection-depois.anki2','revlog',ids,'cid')}
  if any(afterlog.get(v['id'])!=v for v in beforelog):problems.append('histórico de revisões divergente')
  for x in state['notes']:
   n=liveby[x['nid']];e=planned[x['key']]
   if any(n['fields'][k]['value']!=v for k,v in e['fields'].items()):problems.append('campos:'+e['key'])
   x['cards']={str(c):{'ord':ciby[c]['ord'],'flag':next(v['flag'] for v in e['cards'] if v['ord']==ciby[c]['ord'])} for c in n['cards']}
  flags=[v['flag'] for x in state['notes'] for v in x['cards'].values()]
  rec={'run_id':P['run_id'],'selection_hash':P['selection_hash'],'deck':D,'notes':state['notes'],'cards_new_lesson':len(flags),'expected':P['totais']['cards'],'green':flags.count(3),'blue':flags.count(4),'pink':flags.count(5),'compartilhados_tag':sorted(sharedids),'cards_tag_aula':len(A('findCards',query='tag:'+TAG)),'problems':problems,'historico_preservado':not problems,'at':datetime.now(timezone.utc).isoformat()};save(R/'receipt.json',rec);save(R/'plan-aplicado.json',P)
  if problems:raise RuntimeError(str(problems))
  print(json.dumps({k:rec[k] for k in ('cards_new_lesson','cards_tag_aula','problems','historico_preservado')}))
if __name__=='__main__':main()
