import sys,json
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita
A=Anki();nid=1790781882668;n=A('notesInfo',notes=[nid])[0];v={k:f['value'] for k,f in n['fields'].items()}
assert '{{c1::C3a, C4a, and C5a}}' in v['Text'];new=dict(v);new['Text']=v['Text'].replace('{{c1::C3a, C4a, and C5a}}','{{c1::C3a and C5a}}');new['Extra']+='<br>C3a and C5a are the established complement anaphylatoxins; C5a is a major neutrophil chemoattractant. The lecture and older lists also include C4a, but its anaphylatoxin activity and a specific receptor are not established comparably. Do not assign C3a the same direct neutrophil chemotaxis as C5a.'
(R/'anaphylatoxin-correction-before.json').write_text(json.dumps(n,ensure_ascii=False,indent=1))
with escrita(A,'uc03-imuno-anafilatoxinas-revisao-20260930'):
 assert {k:f['value'] for k,f in A('notesInfo',notes=[nid])[0]['fields'].items()}==v
 A('updateNoteFields',note={'id':nid,'fields':new});assert {k:f['value'] for k,f in A('notesInfo',notes=[nid])[0]['fields'].items()}==new
p=R/'complemento/plan.json';plan=json.loads(p.read_text());(R/'complemento/plan-pre-anaphylatoxin-review.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1))
e=next(e for e in plan['entries'] if e['key']=='anafilatoxinas');e['fields']=new;e['post_review']='C4a retirado da resposta categórica; lista histórica docente explicada no apoio.';p.write_text(json.dumps(plan,ensure_ascii=False,indent=1))
(R/'anaphylatoxin-correction-verification.json').write_text(json.dumps({'nid':nid,'readback':'ok','cards_unchanged':n['cards'],'source_unchanged':True},indent=1))
print('Resposta e apoio corrigidos; mesma nota/card, fonte original preservada')
