"""Diagnostico read-only; grava somente evidencias locais, nunca altera Anki."""
import collections
import html
import json
import re
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent
QUERIES = {
    'fluxo': '(stasis OR hemoconcentration OR margination OR estase OR viscosidade)',
    'fluidos': '(exudate OR transudate OR exsudato OR transudato)',
    'permeabilidade': '("endothelial contraction" OR "endothelial injury" OR transcytosis OR "vascular permeability" OR permeabilidade OR transcitose)',
    'linfa': '(lymphadenitis OR lymphangitis OR "lymphatic drainage" OR "lymph flow" OR linfadenite OR linfangite)',
    'efetores': '(phagocytosis OR phagolysosome OR opsonization OR fagocitose OR fagolisossomo OR opsoniza*)',
    'resolucao': '(lipoxin* OR resolvin* OR efferocytosis OR "resolution of inflammation" OR "acute inflammation" OR "inflamação aguda")',
    'morfologia': '(phlegmon* OR flegm* OR "abscess formation" OR "suppurative inflammation" OR "purulent inflammation" OR ulceration OR "mucosal defect")',
    'mediadores': '("platelet activating factor" OR "platelet-activating factor" OR "nitric oxide" OR histamine OR cyclooxygenase OR lipoxygenase OR "phospholipase A2")',
}

def call(action, **params):
    assert action in {'findNotes', 'notesInfo', 'cardsInfo', 'deckNames'}
    r = requests.post('http://127.0.0.1:8765', json={'action': action, 'version': 6, 'params': params}, timeout=60)
    r.raise_for_status()
    data = r.json()
    if data['error']:
        raise RuntimeError(data['error'])
    return data['result']

def clean(s):
    s = re.sub(r'<style.*?</style>|<script.*?</script>', '', s, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s))).strip()

def main():
    matches = {label: call('findNotes', query=query) for label, query in QUERIES.items()}
    ids = sorted({nid for group in matches.values() for nid in group})
    notes = []
    for pos in range(0, len(ids), 100):
        for note in call('notesInfo', notes=ids[pos:pos+100]):
            fields = note['fields']
            preferred = ['Text', 'Frente', 'Front', 'Question', 'Header', 'Back', 'Verso', 'Answer', 'Extra']
            chosen = {key: clean(fields[key]['value']) for key in preferred if key in fields and fields[key]['value']}
            if not chosen:
                chosen = {key: clean(value['value']) for key, value in list(fields.items())[:3]}
            notes.append({'nid': note['noteId'], 'model': note['modelName'], 'cards': note['cards'], 'tags': note['tags'], 'fields': chosen})
    cards = [cid for note in notes for cid in note['cards']]
    card_decks = {}
    for pos in range(0, len(cards), 100):
        for card in call('cardsInfo', cards=cards[pos:pos+100]):
            card_decks[card['cardId']] = card['deckName']
    for note in notes:
        note['decks'] = sorted({card_decks[cid] for cid in note['cards']})
    result = {'queries': QUERIES, 'matches': matches, 'notes': notes}
    (ROOT / 'busca-acervo.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps({'matched_notes': len(notes), 'by_query': {key: len(value) for key,value in matches.items()}, 'by_deck': dict(collections.Counter(deck for note in notes for deck in note['decks']))}, ensure_ascii=False))

if __name__ == '__main__':
    main()
