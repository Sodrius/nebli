"""Separa três notas novas sem trocar IDs ou estado dos oito cards existentes."""
import json,sys,copy
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita
from nebli.explicacoes import open_store,card_hash
from nebli.rotulos import canonical
A=Anki();p=R/'complemento';plan=json.loads((p/'plan.json').read_text());receipt=json.loads((p/'receipt.json').read_text());splits=json.loads((R/'split-focal-candidates.json').read_text());extra=json.loads((R/'extra-refinement-candidates.json').read_text());journal=[];replacements={}
for e,r in zip(plan['entries'],receipt['notes']):
 if e['key'] not in splits:continue
 n=A('notesInfo',notes=[r['nid']])[0];cs=A('cardsInfo',cards=n['cards']);assert all(c['reps']==0 and c['type']==0 for c in cs)
 assert n['fields']['Text']['value']==e['fields']['Text'] and not n['fields']['NEBLI_Comentario']['value']
 journal.append({'entry':e,'receipt':r,'note_before':n,'cards_before':cs,'new':[]})
(R/'split-focal-before.json').write_text(json.dumps(journal,ensure_ascii=False,indent=1))
def save(): (R/'split-focal-journal.json').write_text(json.dumps(journal,ensure_ascii=False,indent=1))
with escrita(A,'uc03-imuno-separacao-focal-20260930'):
 for j in journal:
  e=j['entry'];key=e['key'];newentries=[];newreceipts=[]
  for c in sorted(j['cards_before'],key=lambda c:c['ord']):
   i=c['ord'];ne=copy.deepcopy(e);ne['key']=key+'-foco'+str(i+1);ne['fields']['Text']=splits[key][i];ne['fields']['Extra']=extra.get(key,e['fields']['Extra']);ne['text']=ne['fields']['Text'];ne['extra']=ne['fields']['Extra'];ne['cards']=[{'ord':0,'n':1,'flag':c['flags']}];ne['flags']={'1':c['flags']};ne['tags']=[t+('-foco'+str(i+1)) if t.startswith('NEBLI::author::') else t for t in n['tags']] if False else [t+('-foco'+str(i+1)) if t.startswith('NEBLI::author::') else t for t in j['note_before']['tags']]
   nid=A('addNote',note={'deckName':next(d for d in A('deckNames') if canonical(d)==canonical(c['deckName'])),'modelName':e['model'],'fields':ne['fields'],'tags':ne['tags'],'options':{'allowDuplicate':True}});assert nid
   placeholder=A('notesInfo',notes=[nid])[0]['cards'];assert len(placeholder)==1
   item={'old_card':c['cardId'],'old_ord':i,'new_note':nid,'placeholder':placeholder[0]};j['new'].append(item);save()
   # Vacate the new note's ordinal before transferring the original card.
   assert A('setSpecificValueOfCard',card=placeholder[0],keys=['nid','ord'],newValues=[j['receipt']['nid'],900+i],warning_check=True)==[True]
   assert A('setSpecificValueOfCard',card=c['cardId'],keys=['nid','ord'],newValues=[nid,0],warning_check=True)==[True]
   now=A('cardsInfo',cards=[c['cardId']])[0]
   assert now['note']==nid and now['ord']==0
   assert all(now[k]==c[k] for k in ['flags','queue','type','reps','lapses','due','interval'])
   assert canonical(now['deckName'])==canonical(c['deckName'])
   newentries.append(ne);newreceipts.append({'key':ne['key'],'nid':nid,'cards':{str(c['cardId']):{'ord':0,'flag':c['flags']}}});save()
  old=A('notesInfo',notes=[j['receipt']['nid']])[0];assert set(old['cards'])==set(x['placeholder'] for x in j['new'])
  A('deleteNotes',notes=[j['receipt']['nid']]);assert all(A('cardsInfo',cards=[x['old_card']])[0]['note']==x['new_note'] for x in j['new'])
  replacements[key]=(newentries,newreceipts);j['verified']=True;save()
(p/'plan-pre-focal-split.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1));(p/'receipt-pre-focal-split.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=1))
pe=[];rr=[]
for e,r in zip(plan['entries'],receipt['notes']):
 if e['key'] in replacements:ne,nr=replacements[e['key']];pe.extend(ne);rr.extend(nr)
 else:pe.append(e);rr.append(r)
plan['entries']=pe;receipt['notes']=rr;(p/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1));(p/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=1))
db=open_store()
for j in journal:
 for x in j['new']:
  c=A('cardsInfo',cards=[x['old_card']])[0];fields=[v['value'] for v in sorted(c['fields'].values(),key=lambda f:f['order'])]
  db.execute('update explicacoes set note_id=?,hash=?,modelo=? where card_id=?',(x['new_note'],card_hash(fields,0),'codex-revisao',x['old_card']))
db.commit();print('3 notas separadas em 8; 8 IDs e estados preservados.')
