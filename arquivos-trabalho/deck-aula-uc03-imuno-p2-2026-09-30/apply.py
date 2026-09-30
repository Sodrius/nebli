"""Instala planos revisados com escrita(), snapshot, diário, precondições e readback."""
import hashlib,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
HERE=Path(__file__).parent;ROOT=HERE.parents[1];sys.path.insert(0,str(ROOT))
from nebli.decks import Anki,escrita
from nebli.rotulos import canonical
A=Anki()
def h(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def values(n):return {k:v['value'] for k,v in n['fields'].items()}
def batch(action,key,ids):return [v for i in range(0,len(ids),100) for v in A(action,**{key:ids[i:i+100]})]
def save(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=1))
def install(folder):
 p=HERE/folder;plan=json.loads((p/'plan.json').read_text());tag='NEBLI::'+plan['lesson_id'];DECK=plan['deck']
 if plan['issues']:raise RuntimeError('Dry-run com problemas')
 if (p/'receipt.json').exists():raise RuntimeError('Recibo existente: reconciliar, não reaplicar')
 if A('getActiveProfile')!=plan['profile']:raise RuntimeError('Perfil mudou')
 shared=dict(plan['shared'])
 # Reuso entre as duas aulas novas: só os alvos de Complemento presentes nos slides de Inflamação.
 if folder=='inflamacao':
  comp=json.loads((HERE/'complemento/receipt.json').read_text()); cp=json.loads((HERE/'complemento/plan.json').read_text())
  keys={'classica-igg-igm','alternativa-espontanea','lectinas-manose','lps-complemento','c3-convertase','c5-convertase','mac','anafilatoxinas'}
  for r in comp['notes']:
   if r['key'] not in keys:continue
   n=A('notesInfo',notes=[r['nid']])[0]
   shared[str(r['nid'])]={'reason':'Complemento já instalado nesta corrida; slides 54–59 de Inflamação.',
                        'card_ids':[int(cid) for cid in r['cards']],'fields_hash':h(values(n)),'tags_before':n['tags']}
 srcids=sorted({e['src'] for e in plan['entries'] if e.get('src')})
 sources={n['noteId']:n for n in batch('notesInfo','notes',srcids)}
 sn={n['noteId']:n for n in batch('notesInfo','notes',list(map(int,shared)))}
 def precheck():
  if A('findCards',query='"deck:'+DECK+'"'):raise RuntimeError('Deck possui cards: não recriar ou sobrescrever')
  if set(A('findNotes',query='"tag:'+tag+'"'))-set(map(int,shared)):raise RuntimeError('Notas novas/concorrentes na aula')
  fields=A('modelFieldNames',modelName=plan['entries'][0]['model'])
  if fields!=plan['model_snapshot']['fields'] or 'NEBLI_Comentario' not in fields:raise RuntimeError('Modelo mudou/campo ausente')
  for e in plan['entries']:
   if e.get('src'):
    n=A('notesInfo',notes=[e['src']])[0]
    if h(values(n))!=e['source_fields_hash']:raise RuntimeError('Fonte editada desde o plano: '+e['key'])
    if A('findNotes',query='"tag:NEBLI::source::nid-'+str(e['src'])+'"'):raise RuntimeError('Cópia passou a existir '+e['key'])
   else:
    author=next(t for t in e['tags'] if t.startswith('NEBLI::author::'))
    if A('findNotes',query='"tag:'+author+'"'):raise RuntimeError('Autoral passou a existir '+e['key'])
  for nid,s in shared.items():
   n=A('notesInfo',notes=[int(nid)])[0]
   if h(values(n))!=s['fields_hash']:raise RuntimeError('Compartilhado editado: reconciliar '+nid)
 precheck()
 snapshot={'profile':plan['profile'],'deck_names':A('deckNames'),'sources':sources,'shared_notes':sn,
           'shared_cards':batch('cardsInfo','cards',[cid for s in shared.values() for cid in s['card_ids']]),
           'at':datetime.now(timezone.utc).isoformat()}
 save(p/'before.json',snapshot)
 journal=(p/'journal.jsonl').open('a')
 def log(**v):v['at']=datetime.now(timezone.utc).isoformat();journal.write(json.dumps(v,ensure_ascii=False)+'\n');journal.flush()
 results=[]
 with escrita(A,plan['run_id']):
  precheck()
  A('createDeck',deck=DECK);log(op='createDeck',deck=DECK)
  conf=A('getDeckConfig',deck='NEBLI')
  chain=['::'.join(DECK.split('::')[:i]) for i in range(2,len(DECK.split('::'))+1)]
  wrong=[d for d in chain if A('getDeckConfig',deck=d)['id']!=conf['id']]
  if wrong:A('setDeckConfigId',decks=wrong,configId=conf['id']);log(op='align-preset',decks=wrong)
  for i,e in enumerate(plan['entries'],1):
   nid=A('addNote',note={'deckName':DECK,'modelName':e['model'],'fields':e['fields'],'tags':e['tags'],'options':{'allowDuplicate':True}})
   log(op='addNote',key=e['key'],nid=nid)
   cards=A('cardsInfo',cards=A('findCards',query=f'nid:{nid}'))
   if sorted(c['ord'] for c in cards)!=sorted(c['ord'] for c in e['cards']):raise RuntimeError('Irmãos divergentes '+e['key'])
   for c in cards:
    flag=next(x['flag'] for x in e['cards'] if x['ord']==c['ord'])
    A('setSpecificValueOfCard',card=c['cardId'],keys=['flags'],newValues=[flag],warning_check=True)
   results.append({'key':e['key'],'nid':nid,'cards':{str(c['cardId']):{'ord':c['ord'],'flag':next(x['flag'] for x in e['cards'] if x['ord']==c['ord'])} for c in cards}})
   if i%10==0:print(folder,f'{i}/{len(plan["entries"])} notas',flush=True)
  if shared:A('addTags',notes=list(map(int,shared)),tags=f'{tag} NEBLI::compartilhado::{plan["short"]}');log(op='associate',notes=list(shared))
  problems=[];actual=[]
  for e,r in zip(plan['entries'],results):
   n=A('notesInfo',notes=[r['nid']])[0]
   if values(n)!=e['fields']:problems.append('Campos '+e['key'])
   if set(n['tags'])!=set(e['tags']):problems.append('Tags '+e['key'])
   cards=A('cardsInfo',cards=n['cards']);actual.extend(cards)
   for c in cards:
    if c['flags']!=r['cards'][str(c['cardId'])]['flag'] or c['queue']==-1 or canonical(c['deckName'])!=DECK:problems.append('Estado '+e['key'])
    if c['reps'] or c['type']!=0:problems.append('Novo com estudo '+e['key'])
   if n['fields']['NEBLI_Comentario']['value'] or n['fields']['ankihub_id']['value']:problems.append('Campo pessoal/vínculo herdado '+e['key'])
  for nid,s in shared.items():
   n=A('notesInfo',notes=[int(nid)])[0]
   if h(values(n))!=s['fields_hash']:problems.append('Campo compartilhado '+nid)
   if set(n['tags'])!=set(sn[int(nid)]['tags'])|{tag,f'NEBLI::compartilhado::{plan["short"]}'}:problems.append('Tag compartilhado '+nid)
  for n in batch('notesInfo','notes',srcids):
   if values(n)!=values(sources[n['noteId']]) or n['tags']!=sources[n['noteId']]['tags']:problems.append('Original alterado '+str(n['noteId']))
  # Flags/deck/suspensões dos compartilhados devem permanecer; estudo pode avançar durante a sessão.
  before_cards={c['cardId']:c for c in snapshot['shared_cards']}
  for c in batch('cardsInfo','cards',list(before_cards)):
   b=before_cards[c['cardId']]
   if c['flags']!=b['flags'] or canonical(c['deckName'])!=canonical(b['deckName']) or (c['queue']==-1)!=(b['queue']==-1):problems.append('Marca/deck/suspensão compartilhado '+str(c['cardId']))
  exact=sorted({c['cardId'] for c in actual}|{cid for s in shared.values() for cid in s['card_ids']})
  query='cid:'+','.join(map(str,exact))
  if set(A('findCards',query=query))!=set(exact):problems.append('Busca exata da aula')
  receipt={'run_id':plan['run_id'],'deck':DECK,'selection_hash':plan['selection_hash'],'notes':results,'shared':shared,
           'new_cards':len(actual),'exact_card_ids':exact,'query':query,'problems':problems,'at':datetime.now(timezone.utc).isoformat()}
  save(p/'receipt.json',receipt);save(p/'verification.json',{'problems':problems,'all_fields_checked':True,'new_cards':len(actual),'original_notes_unchanged':len(srcids),'shared_checked':len(shared),'exact_query_verified':True})
  save(p/'rendered-cards.json',actual)
  if problems:raise RuntimeError('Readback divergente '+str(problems))
  print(folder,'readback OK',len(actual),'novos,',len(exact)-len(actual),'associados',flush=True)
 receipt['sync']='solicitado e aceito pelo AnkiConnect; chegada aos aparelhos não conferida';save(p/'receipt.json',receipt)
 journal.close()
if __name__=='__main__':
 for folder in sys.argv[1:] or ['complemento','inflamacao']:install(folder)
