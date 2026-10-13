"""Busca somente leitura: q.py '<query anki>' [max] -> nid | deck curto | modelo | texto limpo"""
import sys, re, html
sys.path.insert(0, '/Users/davisousa/NEBLI')
from nebli.decks import Anki
A = Anki()
def clean(s): 
    s = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', r'[IMG \1]', s); s = re.sub(r'<br\s*/?>', ' / ', s)
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()
q = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 40
nids = A('findNotes', query=q)
print(f'# {len(nids)} notas: {q}')
for n in A('notesInfo', notes=nids[:mx]):
    f = {k: v['value'] for k, v in n['fields'].items()}
    main = f.get('Text') or f.get('Front') or f.get('Title') or f.get('Header') or f.get('Structure') or next(iter(f.values()))
    deck = A('cardsInfo', cards=n['cards'][:1])[0]['deckName'].split('::')
    extra = clean(f.get('Extra', ''))[:160]
    y = [t.split('::')[-1][:1] for t in n['tags'] if 'Low/HighYield' in t]; hy = f"Y{y[0]} " if y else ''
    print(f"{n['noteId']} | {deck[-1][:22] if len(deck)<3 else deck[2][:22]} | {n['modelName'][:18]} | {hy}{clean(main)[:260]} || {extra}")
