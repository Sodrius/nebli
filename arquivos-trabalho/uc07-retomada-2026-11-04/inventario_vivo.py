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
for card in a('cardsInfo', cards=ids):
    row = rows[card['deckName']]
    row['cards'] += 1
    row['notas'].add(card['note'])
    row['suspensos'] += int(card['queue'] == -1)
    row['bandeiras'][str(card.get('flags'))] += 1
output = []
for name, row in sorted(rows.items()):
    row['notas'] = len(row['notas'])
    row['bandeiras'] = dict(row['bandeiras'])
    output.append({'deck': name, **row})
Path(__file__).with_name('decks-vivos.json').write_text(
    json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(output, ensure_ascii=False, indent=2))
