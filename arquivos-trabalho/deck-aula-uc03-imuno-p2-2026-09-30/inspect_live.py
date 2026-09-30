"""Leitura pontual do Anki: candidatos, identidades e modelos; nenhuma mutação externa."""
import sys,json,re,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from nebli.decks import Anki
A=Anki(); HERE=Path(__file__).parent
def dump(name,data): (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=1))
def bat(action,key,ids):
 return [v for i in range(0,len(ids),150) for v in A(action,**{key:ids[i:i+150]})]
if '--extra' in sys.argv:
 terms=['dendritic','natural killer','autocrine','paracrine','"nitric oxide"','endocrine','"histamine receptor"','C5aR','C4BP','factor H','factor I','lipoxin','resolvin']
 found={t:A('findNotes',query=f'("deck:Referências::*" or "deck:NEBLI*") {t}') for t in terms}
 dump('busca/extra-queries.json',found)
 dump('busca/extra-notes.json',bat('notesInfo','notes',sorted({nid for ids in found.values() for nid in ids})))
 print('extra', {t:len(ids) for t,ids in found.items()});sys.exit(0)
ids=set(map(int,re.findall(r'\b1\d{12}\b',(HERE/'ESTADO.md').read_text()+(HERE/'complemento/spec.py').read_text())))
for name in ['complemento-fa','inflamacao-fa']:
 for n in json.loads((HERE/f'busca/{name}.json').read_text()): ids.add(n['nid'])
live=A('findNotes',query='"tag:NEBLI::*"')
notes=bat('notesInfo','notes',sorted(ids|set(live)))
dump('live-notes.json',notes)
cards=bat('cardsInfo','cards',[c for n in notes if n for c in n['cards']])
dump('live-cards.json',cards)
models={n['modelName'] for n in notes if n}
dump('models.json',{m:{'fields':A('modelFieldNames',modelName=m),'templates':A('modelTemplates',modelName=m),'css':A('modelStyling',modelName=m)} for m in models})
terms=['properdin','"factor B"','"factor D"','"factor H"','"factor I"','CH50','AH50','C1q','CR1','CD35','CR3','CD59','MASP','NOD','RIG','dectin','DAMP','NLRP3','urate','resolvin','lipoxin','extracellular trap','"substance P"','CGRP','eotaxin','effero','scavenger','TLR5','caspase-1']
search={}; candidates=set()
for term in terms:
 q=f'("deck:Referências::*" or "deck:NEBLI*") "{term.strip(chr(34))}"'
 found=A('findNotes',query=q); search[term]={'query':q,'ids':found}; candidates.update(found)
dump('busca/alternativos.json',search)
dump('busca/alternativos-notes.json',bat('notesInfo','notes',sorted(candidates)))
print(json.dumps({'profile':A('getActiveProfile'),'notes':len(notes),'cards':len(cards),'search_candidates':len(candidates)}))
