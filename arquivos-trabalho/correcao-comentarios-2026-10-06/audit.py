import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki
P = Path(__file__).resolve().parent
A = Anki()
ids = A('findNotes', query='deck:NEBLI*')
notes = []
for i in range(0,len(ids),300):
    notes += A('notesInfo', notes=ids[i:i+300])
out=P/'snapshot.json'
if not out.exists(): out.write_text(json.dumps(notes,ensure_ascii=False,indent=2))
print('Notas',len(notes),'cards',sum(len(n['cards']) for n in notes))
for n in notes:
    f={k:v['value'] for k,v in n['fields'].items()}
    c=f.get('NEBLI_Comentario','')
    if c and 'CORRIGIDO' not in c:
        print(json.dumps({'nid':n['noteId'],'fields':{k:v for k,v in f.items() if v and k in ['Text','Extra','Front','Back','Remarks','NEBLI_Comentario']}},ensure_ascii=False))
