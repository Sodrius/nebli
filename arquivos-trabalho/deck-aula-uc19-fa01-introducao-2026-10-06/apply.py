"""Instala o plano UC19/P1 e confere cada nota criada."""
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path
HERE=Path(__file__).parent; sys.path.insert(0,str(HERE.parents[1]))
from nebli.decks import Anki, escrita
A=Anki(); plan=json.loads((HERE/'plan.json').read_text()); BASE=1900000
canon=lambda x: re.sub(r" \(\d+\)","",x)
with escrita(A, 'UC19 P1 FA01'):
 if A('findNotes',query=f'"tag:NEBLI::{plan["lesson_id"]}"'):
  raise SystemExit('Aula UC19/P1/FA01 já instalada; nada duplicado.')
 A('createDeck',deck=plan['deck'])
 root=A('getDeckConfig',deck='NEBLI')
 chain=['::'.join(plan['deck'].split('::')[:i]) for i in range(2,plan['deck'].count('::')+2)]
 wrong=[d for d in chain if A('getDeckConfig',deck=d)['id'] != root['id']]
 if wrong: A('setDeckConfigId',decks=wrong,configId=root['id'])
 receipt=[]; problems=[]
 for e in plan['entries']:
  nid=A('addNote',note={'deckName':plan['deck'],'modelName':e['model'],'fields':e['fields'],'tags':e['tags'],'options':{'allowDuplicate':True}})
  cards=A('cardsInfo',cards=A('findCards',query=f'nid:{nid}'))
  for c in cards:
   match=next((x for x in e['cards'] if x['ord']==c['ord']),None)
   if not match: problems.append(e['key']+' ord'); continue
   A('setSpecificValueOfCard',card=c['cardId'],keys=['flags','due'],newValues=[match['flag'],BASE+e['order']*10+c['ord']],warning_check=True)
  now=A('notesInfo',notes=[nid])[0]
  if now['fields'].get('NEBLI_Comentario',{}).get('value',''): problems.append(e['key']+' comentario')
  if set(now['tags']) != set(e['tags']): problems.append(e['key']+' tags')
  receipt.append({'key':e['key'],'nid':nid,'cards':[c['cardId'] for c in cards]})
 (HERE/'receipt.json').write_text(json.dumps({'run_id':plan['run_id'],'deck':plan['deck'],'notes':receipt,'expected':plan['totais']['cards'],'problems':problems,'at':datetime.now(timezone.utc).isoformat()},ensure_ascii=False,indent=2))
 print(json.dumps({'notes':len(receipt),'cards':sum(len(x['cards']) for x in receipt),'problems':problems},ensure_ascii=False))
 if problems: raise SystemExit('Readback divergente')
