"""Backup consistente e manifesto UC07; não escreve na coleção Anki."""
from pathlib import Path
import sys
import json
import sqlite3
import hashlib
from datetime import datetime, timezone

RUN = Path(__file__).resolve().parent
ROOT = RUN.parents[1]
sys.path.insert(0, str(ROOT))
from nebli.decks import Anki
from nebli.rotulos import canonical

def main():
    destination = RUN / 'backup-uc07'
    destination.mkdir(exist_ok=True)
    if (destination / 'manifesto.json').exists():
        print('Backup inicial já existe; preservado sem sobrescrita.')
        return
    a = Anki()
    decks = a('deckNamesAndIds')
    branch = {name: did for name, did in decks.items()
              if canonical(name) == 'NEBLI::UC07' or canonical(name).startswith('NEBLI::UC07::')}
    if not branch:
        raise RuntimeError('UC07 não encontrada; backup vazio recusado')
    query = '(' + ' or '.join('did:' + str(did) for did in branch.values()) + ')'
    ids = a('findCards', query=query)
    cards = a('cardsInfo', cards=ids)
    notes = a('notesInfo', notes=sorted({c['note'] for c in cards}))
    if not cards or not notes:
        raise RuntimeError('Backup vazio recusado')
    collection = Path.home() / 'Library/Application Support/Anki2/User 1/collection.anki2'
    backup = destination / 'collection-antes-uc07.anki2'
    with sqlite3.connect('file:' + str(collection) + '?mode=ro', uri=True) as source:
        with sqlite3.connect(backup) as target:
            source.backup(target)
    with sqlite3.connect('file:' + str(backup) + '?mode=ro', uri=True) as db:
        db.create_collation('unicase', lambda a, b: (a.casefold() > b.casefold()) - (a.casefold() < b.casefold()))
        db.row_factory = sqlite3.Row
        wanted = ','.join('?' for _ in ids)
        reviews = [dict(row) for row in db.execute('select * from revlog where cid in (' + wanted + ') order by id', ids)]
        card_rows = [dict(row) for row in db.execute('select * from cards where id in (' + wanted + ')', ids)]
        integrity = db.execute('pragma quick_check').fetchone()[0]
    for name, value in [('cards.json', cards), ('notes.json', notes), ('revlog.json', reviews), ('cards-sql.json', card_rows), ('decks.json', branch)]:
        (destination / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    manifest = {'created_at': datetime.now(timezone.utc).isoformat(),
                'cards': len(cards), 'notes': len(notes), 'reviews': len(reviews),
                'suspended': sum(c['queue'] == -1 for c in cards),
                'studied': sum(c['reps'] > 0 for c in cards),
                'sqlite_quick_check': integrity, 'hashes': {}}
    for path in destination.iterdir():
        if path.is_file():
            with path.open('rb') as handle:
                h = hashlib.sha256()
                for data in iter(lambda: handle.read(1024 * 1024), b''):
                    h.update(data)
            manifest['hashes'][path.name] = h.hexdigest()
    (destination / 'manifesto.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print({key: value for key, value in manifest.items() if key != 'hashes'})

if __name__ == '__main__':
    main()
