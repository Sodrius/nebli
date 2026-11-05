"""Somente leitura: composição e suspensão dos decks UC07."""
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from nebli.decks import Anki
from nebli.rotulos import canonical

a = Anki()
decks = a('deckNamesAndIds')
deck_ids = [did for name, did in decks.items()
            if canonical(name) == 'NEBLI::UC07' or canonical(name).startswith('NEBLI::UC07::')]
if not deck_ids:
    raise SystemExit('Árvore UC07 não encontrada')
ids = a('findCards', query='(' + ' or '.join(f'did:{did}' for did in deck_ids) + ')')
if not ids:
    raise SystemExit('Consulta vazia: não declarar inventário concluído')
rows = defaultdict(lambda: {'cards': 0, 'notas': set(), 'suspensos': 0,
                            'bandeiras': Counter()})
cards = a('cardsInfo', cards=ids)
for card in cards:
    row = rows[card['deckName']]
    row['cards'] += 1
    row['notas'].add(card['note'])
    row['suspensos'] += int(card['queue'] == -1)
    row['bandeiras'][str(card.get('flags'))] += 1
output = []
for name, row in sorted(rows.items()):
    row['notas'] = len(row['notas'])
    row['bandeiras'] = dict(row['bandeiras'])
    output.append({'deck': canonical(name), **row})
Path(__file__).with_name('decks-vivos.json').write_text(
    json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(f'{len(output)} decks; {len(cards)} cards; '
      f'{sum(row["suspensos"] for row in output)} suspensos')
if '--detalhar' in sys.argv:
    # Campos completos são material privado de trabalho; não versionar.
    Path(__file__).with_name('notas-vivas.json').write_text(
        json.dumps(cards, ensure_ascii=False, indent=2) + '\n')
if '--candidatos' in sys.argv:
    snapshots = json.loads(Path(__file__).with_name('candidatos-snapshot.json').read_text())
    nids = sorted({row['nid'] for rows in snapshots.values() for row in rows})
    candidates = a('notesInfo', notes=nids)
    available = [row for row in candidates if row.get('noteId')]
    Path(__file__).with_name('candidatos-vivos.json').write_text(
        json.dumps(available, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(available)}/{len(nids)} candidatos do snapshot encontrados no Anki vivo')
