"""Snapshot somente leitura para a calibração solicitada por Davi."""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from nebli.decks import Anki
from nebli.preflight import chunks, deck_query
from nebli.rotulos import canonical

out = Path(__file__).parent
anki = Anki()
decks = anki('deckNames')
roots = [d for d in decks if canonical(d) == 'NEBLI']
assert len(roots) == 1, roots
query = deck_query(roots[0])
ids = anki('findCards', query=query)
cards = [c for b in chunks(ids) for c in anki('cardsInfo', cards=b)]
nids = sorted({c['note'] for c in cards})
notes = [n for b in chunks(nids) for n in anki('notesInfo', notes=b)]
flags = {str(f): anki('findCards', query=f'{query} flag:{f}') for f in range(8)}
leech_all = anki('findCards', query='tag:leech')
models = {}
for name in sorted({n['modelName'] for n in notes}):
    models[name] = {'fields': anki('modelFieldNames', modelName=name),
                    'templates': anki('modelTemplates', modelName=name),
                    'styling': anki('modelStyling', modelName=name)}
configs = {}
for name in sorted({c['deckName'] for c in cards}):
    configs[name] = anki('getDeckConfig', deck=name)
snapshot = {'at': datetime.now(timezone.utc).isoformat(),
            'profile': anki('getActiveProfile'), 'decks': decks,
            'cards': cards, 'notes': notes, 'flags': flags,
            'leech_all': leech_all, 'models': models, 'configs': configs}
dest = out / 'snapshot.json'
with dest.open('x') as f:
    json.dump(snapshot, f, ensure_ascii=False, indent=1)
print(json.dumps({'profile':snapshot['profile'],'cards':len(cards),'notes':len(notes),
    'flags':{k:len(v) for k,v in flags.items()},'leech_all':len(leech_all),
    'leech_nebli':len(set(leech_all)&set(ids)),
    'suspended':sum(c['queue']==-1 for c in cards),
    'reviewed':sum(c['reps']>0 for c in cards),
    'models':dict(Counter(n['modelName'] for n in notes)),
    'comments':[{ 'nid':n['noteId'],'comment':n['fields']['NEBLI_Comentario']['value']} for n in notes
       if n['fields'].get('NEBLI_Comentario',{}).get('value','').strip()]},ensure_ascii=False,indent=1))
