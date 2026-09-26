"""Read-only Anki snapshot; writes audit evidence only in this directory."""
import json, sys
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.preflight import ReadOnlyAnki, chunks

out = Path(__file__).parent
call = ReadOnlyAnki()
ids = call('findCards', query='deck:NEBLI::UC*')
cards = [c for batch in chunks(ids) for c in call('cardsInfo', cards=batch)]
nids = sorted({c['note'] for c in cards})
notes = [n for batch in chunks(nids) for n in call('notesInfo', notes=batch)]
flags = {i: call('findCards', query=f'deck:NEBLI::UC* flag:{i}') for i in range(8)}
end = call('findCards', query='deck:NEBLI::UC*')
snapshot = dict(at=datetime.now(timezone.utc).isoformat(), read_only=True,
    same_ids_start_end=set(ids)==set(end), cards=cards, notes=notes, flags=flags)
with (out/'snapshot.json').open('x', encoding='utf-8') as f:
    json.dump(snapshot,f,ensure_ascii=False)
print(json.dumps(dict(cards=len(cards),notes=len(notes),stable=snapshot['same_ids_start_end'],
    sample_tags=notes[0]['tags']),ensure_ascii=True))
