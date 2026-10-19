"""Associa à 62 o cartão compartilhado exigido pela prova, sem copiar ou editar a nota."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita, em_tela

A = Anki()
plan = json.loads((HERE / 'plan.json').read_text())
nid = 1791716424523
if nid in em_tela(A):
    raise SystemExit('Nota compartilhada em estudo; associação adiada sem escrita.')
s = plan['compartilhados'][str(nid)]
lesson = plan['lesson_id']
with escrita(A, 'PT62 associar princípio de gigantócito', sync=False):
    n = A('notesInfo', notes=[nid])[0]
    stale = [t for t in n['tags'] if t.startswith('NEBLI::ordem::pt62-') or t.startswith(f'NEBLI::cor::{lesson}::')]
    if stale:
        A('removeTags', notes=[nid], tags=' '.join(stale))
    A('addTags', notes=[nid], tags=f'NEBLI::{lesson} NEBLI::compartilhado::{plan["short"]} NEBLI::cor::{lesson}::{s["cor"]} {s["ordem_tag"]}')
    after = A('notesInfo', notes=[nid])[0]
    assert f'NEBLI::{lesson}' in after['tags'] and s['ordem_tag'] in after['tags']
rec = json.loads((HERE / 'receipt.json').read_text())
rec['compartilhados_tag'] = sorted(set(rec.get('compartilhados_tag', []) + [nid]))
rec['cards_tag_aula'] = len(A('findCards', query=f'"tag:NEBLI::{lesson}"'))
(HERE / 'receipt.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1))
(HERE / 'plan-aplicado.json').write_text(json.dumps(plan, ensure_ascii=False, indent=1))
print(f'associado; {rec["cards_tag_aula"]} cards com a tag da aula')
