"""Instalação AN04: fonte congelada, backup, proteção de tela, lotes e readback.
Não inicia sem aprovação pré-instalação e seleção de estudo vinculadas ao plano.
"""
from pathlib import Path
import sys,json,base64,hashlib,re,time
from collections import defaultdict,Counter
from datetime import datetime,timezone
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita,em_tela
from nebli.rotulos import canonical
A=Anki();P=json.loads((R/'plan.json').read_text());DECK=P['deck'];LESSON=P['lesson_id'];TAG='NEBLI::'+LESSON
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda v:hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:16]
def save(name,value):(R/name).write_text(json.dumps(value,ensure_ascii=False,indent=1))
def log(**kw):
 with (R/'journal.jsonl').open('a') as f:f.write(json.dumps(dict(at=now(),**kw),ensure_ascii=False)+'\n')
def tela():
 for _ in range(10):
  try:return set(em_tela(A))
  except RuntimeError as e:
   if 'collection operation is active' not in str(e).lower():raise
   time.sleep(.2)
 raise RuntimeError('Não foi possível determinar a nota em tela')
def multi(actions):
 if not actions:return []
 result=A('multi',actions=actions)
 assert len(result)==len(actions)
 assert not any(isinstance(x,dict) and x.get('error') for x in result),result
 return result
def chunk(xs,n=50):
 for i in range(0,len(xs),n):yield xs[i:i+n]
def sub(e):
 u=int(re.search(r'\d+',e['evid']).group())
 return DECK+'::'+('01 Diencéfalo' if u<=21 else '02 Telencéfalo' if u<=42 else '03 Núcleos da base' if u<=46 else '04 Irrigação')
def safe_actions(rows,make):
 for batch in chunk(rows,25):
  protected=tela();safe=[x for x in batch if int(x['nid']) not in protected]
  if len(safe)!=len(batch):raise RuntimeError('Nota em tela protegida; reaplicar quando Davi sair dela, sem alterar irmãos.')
  multi([a for x in safe for a in make(x)])

def main():
 proof=json.loads((R/'pre-install-checks.json').read_text());sel=json.loads((R/'selecao-estudo.json').read_text())
 assert proof['selection_hash']==P['selection_hash'] and proof['apto_instalar'] is True
 assert sel['selection_hash']==P['selection_hash']
 allkeys={e['key'] for e in P['entries']}|{'sh-'+k for k in P['compartilhados']}
 assert set(sel['cards'])==allkeys
 if (R/'receipt.json').exists():raise SystemExit('Instalação já existe: usar reconciliação/delta, nunca duplicar.')
 shared_ids=[int(k) for k in P['compartilhados']]
 with escrita(A,'UC07 AN04: instalar e selecionar por provas/resumos',sync=False):
  live={n['noteId']:n for n in A('notesInfo',notes=shared_ids)}
  cards={c['cardId']:c for c in A('cardsInfo',cards=[c for n in live.values() for c in n['cards']])}
  assert not (set(live)&tela()),'Há nota desta operação na tela: protegida, nada escrito.'
  assert not A('findNotes',query='"tag:'+TAG+'"'),'Aula já instalada; não duplicar.'
  for nid,n in live.items():
   assert sha({k:v['value'] for k,v in n['fields'].items()})==P['compartilhados'][str(nid)]['before_fields_hash'],f'Nota {nid} mudou depois do plano; conferir antes de escrever.'
  save('before.json',{'at':now(),'notes':list(live.values()),'cards':list(cards.values()),'decks':A('deckNames'),'selection_hash':P['selection_hash']})
  # Arquivos de nomes novos; colisão com conteúdo divergente aborta.
  for name,rel in P['media'].items():
   payload=base64.b64encode((R/rel).read_bytes()).decode();old=A('retrieveMediaFile',filename=name)
   if old and old!=payload:raise RuntimeError('Colisão de mídia: '+name)
   if not old:A('storeMediaFile',filename=name,data=payload);log(op='media',file=name)
  existing=set(A('modelNames'))
  for model,old in P.get('clones',{}).items():
   if model not in existing:raise RuntimeError('Modelo ainda não preparado: '+model)
  for d in sorted({sub(e) for e in P['entries']}|{sub(e) for e in P['compartilhados'].values()}):A('createDeck',deck=d)
  root=A('getDeckConfig',deck='NEBLI');A('setDeckConfigId',decks=[DECK]+sorted({sub(e) for e in P['entries']}),configId=root['id'])
  results=[]
  for batch in chunk(P['entries'],10):
   # Novas notas não têm irmãos na tela; originals de referência não são alterados.
   added=A('addNotes',notes=[{'deckName':sub(e),'modelName':e['model'],'fields':e['fields'],'tags':e['tags'],'options':{'allowDuplicate':True}} for e in batch])
   assert len(added)==len(batch) and all(isinstance(n,int) and n>0 for n in added),added
   for e,nid in zip(batch,added):results.append({'key':e['key'],'nid':nid});log(op='addNote',key=e['key'],nid=nid)
   save('instalacao-parcial.json',results)
  rows=[{'nid':nid,'e':P['compartilhados'][str(nid)],'n':n} for nid,n in live.items()]
  def edit(x):
   e,n=x['e'],x['n'];fields={k:v for k,v in e['fields'].items() if k not in ('NEBLI_Comentario','NEBLI_Resposta','ankihub_id') and k in n['fields'] and n['fields'][k]['value']!=v}
   acts=[]
   if fields:acts.append({'action':'updateNoteFields','params':{'note':{'id':x['nid'],'fields':fields}}})
   old=[t for t in n['tags'] if t.startswith('NEBLI::cor::'+LESSON+'::') or t.startswith('NEBLI::ordem::'+P['short']+'-')]
   if old:acts.append({'action':'removeTags','params':{'notes':[x['nid']],'tags':' '.join(old)}})
   acts.append({'action':'addTags','params':{'notes':[x['nid']],'tags':' '.join([TAG,'NEBLI::compartilhado::'+P['short'],'NEBLI::cor::'+LESSON+'::'+e['cor'],e['ordem_tag']])}})
   return acts
  safe_actions(rows,edit)
  mapping={x['key']:x['nid'] for x in results}|{'sh-'+str(n):n for n in live}
  allnotes={n['noteId']:n for n in A('notesInfo',notes=list(mapping.values()))}
  ci={c['cardId']:c for c in A('cardsInfo',cards=[c for n in allnotes.values() for c in n['cards']])}
  E={e['key']:e for e in P['entries']}|{'sh-'+k:v for k,v in P['compartilhados'].items()}
  actions=[];pending_order=[]
  for key,nid in mapping.items():
   e=E[key];n=allnotes[nid];expected={c['ord']:c['flag'] for c in e.get('cards',[])}
   flag={'verde':3,'azul':4,'rosa':5}.get(e.get('cor'))
   for cid in n['cards']:
    c=ci[cid];flagwant=expected.get(c['ord'],flag);assert flagwant in (3,4,5)
    active=c['ord'] in sel['cards'][key]['ativos_ords']
    ops=[]
    if c['flags']!=flagwant:ops.append({'action':'setSpecificValueOfCard','params':{'card':cid,'keys':['flags'],'newValues':[flagwant],'warning_check':True}})
    if (c['queue']!=-1)!=active:ops.append({'action':'unsuspend' if active else 'suspend','params':{'cards':[cid]}})
    # Reutilizar IDs de estudo; atuais AN01/03 continuam associados em seu deck.
    if not canonical(c['deckName']).startswith('NEBLI::UC07::P1::Anatomia::') or key in {x['key'] for x in results}:
     if canonical(c['deckName'])!=sub(e):ops.append({'action':'changeDeck','params':{'cards':[cid],'deck':sub(e)}})
     if c['type']==0:pending_order.append((e['order'],c['ord'],cid))
    actions.append({'nid':nid,'ops':ops})
  safe_actions(actions,lambda x:x['ops'])
  finalnotes={n['noteId']:n for n in A('notesInfo',notes=list(mapping.values()))}
  finalcards={c['cardId']:c for c in A('cardsInfo',cards=[c for n in finalnotes.values() for c in n['cards']])}
  problems=[]
  for key,nid in mapping.items():
   e=E[key];n=finalnotes[nid]
   for f,v in e['fields'].items():
    if f in ('NEBLI_Comentario','NEBLI_Resposta','ankihub_id'):continue
    if n['fields'][f]['value']!=v:problems.append(key+': campo '+f)
   for cid in n['cards']:
    c=finalcards[cid];flags={x['ord']:x['flag'] for x in e.get('cards',[])}
    if c['flags']!=flags.get(c['ord'],{'verde':3,'azul':4,'rosa':5}.get(e.get('cor'))):problems.append(key+': bandeira')
    if (c['queue']!=-1)!=(c['ord'] in sel['cards'][key]['ativos_ords']):problems.append(key+': suspensão')
    if cid in cards:
     old=cards[cid]
     for f in ('reps','lapses','due','interval','factor','type'):
      if c[f]!=old[f]:problems.append(key+': histórico '+f)
   if nid in live:
    for f in ('NEBLI_Comentario','NEBLI_Resposta'):
     if f in n['fields'] and n['fields'][f]['value']!=live[nid]['fields'][f]['value']:problems.append(key+': comentário pessoal')
  for x in results:x['cards']={str(cid):{'ord':finalcards[cid]['ord'],'flag':finalcards[cid]['flags']} for cid in finalnotes[x['nid']]['cards']}
  rec={'run_id':P['run_id'],'selection_hash':P['selection_hash'],'deck':DECK,'notes':results,'compartilhados_tag':shared_ids,'cards_new_lesson':sum(len(x['cards']) for x in results),'expected':P['totais']['cards'],'cards_tag_aula':len(finalcards),'green':sum(c['flags']==3 for x in results for cid in finalnotes[x['nid']]['cards'] for c in [finalcards[cid]]),'blue':sum(c['flags']==4 for x in results for cid in finalnotes[x['nid']]['cards'] for c in [finalcards[cid]]),'pink':sum(c['flags']==5 for x in results for cid in finalnotes[x['nid']]['cards'] for c in [finalcards[cid]]),'problems':problems,'at':now(),'ativos':sum(c['queue']!=-1 for c in finalcards.values()),'suspensos':sum(c['queue']==-1 for c in finalcards.values())}
  save('receipt.json',rec);save('after.json',{'notes':list(finalnotes.values()),'cards':list(finalcards.values())});save('plan-aplicado.json',P)
  save('reposicao-planejada.json',{'cards':[c for _,_,c in sorted(pending_order)],'short':P['short'],'deck':DECK})
  assert not problems,problems
  assert rec['cards_new_lesson']==rec['expected']
  print(json.dumps({k:rec[k] for k in ('cards_new_lesson','cards_tag_aula','ativos','suspensos','problems')},ensure_ascii=False))
if __name__=='__main__':main()
