"""Busca somente leitura em acervos externos, todos os campos textuais. qx.py '<query>' [max]"""
import sys, re, html
sys.path.insert(0, '/Users/davisousa/NEBLI')
from nebli.decks import Anki
A = Anki()
def clean(s):
    s = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', r'[IMG]', s); s = re.sub(r'<br\s*/?>|</div>', ' / ', s)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()
q = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 40
nids = A('findNotes', query=q)
print(f'# {len(nids)} notas: {q}')
for n in A('notesInfo', notes=nids[:mx]):
    f = {k: clean(v['value']) for k, v in n['fields'].items()}
    deck = A('cardsInfo', cards=n['cards'][:1])[0]['deckName'].split('::')
    keys = [k for k in f if f[k] and k not in ('ankihub_id', 'ID (hidden)', 'Question Mask', 'Answer Mask', 'Original Mask', 'NoteID', 'Image', 'Cadaver', 'Imaging', 'Model', 'Illustration', 'OccludedImage')]
    body = ' | '.join(f'{k}: {f[k][:140]}' for k in keys)
    print(f"{n['noteId']} [{deck[2][:10] if len(deck)>2 else deck[-1][:10]}|{n['modelName'][:14]}|{len(n['cards'])}c] {body[:420]}")
