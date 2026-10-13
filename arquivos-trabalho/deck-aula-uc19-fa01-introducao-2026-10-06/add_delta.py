import json, re, sys
from pathlib import Path
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE.parents[1]))
from nebli.decks import Anki, escrita
A=Anki();p=json.loads((HERE/'plan.json').read_text()); e=next(x for x in p['entries'] if x['key']=='pde_camp')
with escrita(A,'UC19 P1 FA01 delta pde_camp'):
 if A('findNotes',query='"tag:NEBLI::source::nid-1461857288204"'): raise SystemExit('pde_camp já existe')
 nid=A('addNote',note={'deckName':p['deck'],'modelName':e['model'],'fields':e['fields'],'tags':e['tags'],'options':{'allowDuplicate':True}})
 for c in A('cardsInfo',cards=A('findCards',query=f'nid:{nid}')):
  x=next(x for x in e['cards'] if x['ord']==c['ord']); A('setSpecificValueOfCard',card=c['cardId'],keys=['flags','due'],newValues=[x['flag'],1900000+e['order']*10+c['ord']],warning_check=True)
 print(nid)
