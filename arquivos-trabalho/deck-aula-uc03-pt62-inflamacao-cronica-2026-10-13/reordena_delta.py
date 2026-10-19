"""Atualiza apenas a tag de ordem após inserir um compartilhado no plano já instalado."""
import json
import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita, em_tela

A = Anki()
plan = json.loads((HERE / 'plan.json').read_text())
receipt = json.loads((HERE / 'receipt.json').read_text())
ids = {n['key']: n['nid'] for n in receipt['notes']}
targets = list(ids.values())
shown = set(em_tela(A))
if shown & set(targets):
    raise SystemExit('Nota da aula em estudo; nenhuma ordem foi alterada.')
with escrita(A, 'PT62 renumerar após compartilhado', sync=False):
    for e in plan['entries']:
        nid = ids[e['key']]
        n = A('notesInfo', notes=[nid])[0]
        stale = [t for t in n['tags'] if t.startswith('NEBLI::ordem::pt62-')]
        if stale:
            A('removeTags', notes=[nid], tags=' '.join(stale))
        tag = next(t for t in e['tags'] if t.startswith('NEBLI::ordem::pt62-'))
        A('addTags', notes=[nid], tags=tag)
    for raw, shared in plan['compartilhados'].items():
        nid = int(raw)
        n = A('notesInfo', notes=[nid])[0]
        stale = [t for t in n['tags'] if t.startswith('NEBLI::ordem::pt62-')]
        if stale:
            A('removeTags', notes=[nid], tags=' '.join(stale))
        A('addTags', notes=[nid], tags=shared['ordem_tag'])
print(f'{len(targets)} notas renumeradas')
