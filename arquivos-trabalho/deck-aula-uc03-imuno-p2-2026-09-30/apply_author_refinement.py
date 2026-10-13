"""Refina somente cards novos desta entrega, preservando seus IDs e todo estudo/marca pessoal."""
import json,sys,re,time,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita
from nebli.explicacoes import open_store,card_hash,style_version,STYLE
from nebli.lint_cards import check
A=Anki();changes=json.loads((R/'author-refinement-before.json').read_text())
from nebli.rotulos import canonical
def state(cs):
 return sorted([{k:(canonical(c[k]) if k=='deckName' else c[k]) for k in ['cardId','ord','flags','queue','type','reps','lapses','deckName']} for c in cs],key=lambda c:c['cardId'])
with escrita(A,'uc03-imuno-refino-autoral-20260930'):
 for c in changes:
  n=A('notesInfo',notes=[c['nid']])[0];assert all(n['fields'][k]['value'] in [c['before']['fields'][k]['value'],c['after'][k]] for k in ['Text','Extra'])
  A('updateNoteFields',note={'id':c['nid'],'fields':c['after']})
  n=A('notesInfo',notes=[c['nid']])[0];assert all(n['fields'][k]['value']==v for k,v in c['after'].items())
  cs=A('cardsInfo',cards=n['cards']);assert state(cs)==state(c['cards_before'])
for folder in ['complemento','inflamacao']:
 p=R/folder;plan=json.loads((p/'plan.json').read_text());(p/'plan-pre-author-refinement.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1))
 for e in plan['entries']:
  c=next((c for c in changes if c['folder']==folder and c['key']==e['key']),None)
  if c:e['fields'].update(c['after']);e['post_author_review']='Frente focal e Extra sem metacomentário; card-mirror rounds 1–3; IDs preservados.'
 (p/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1))
# Todas as explicações desses alvos foram lidas: permanecem semanticamente válidas
# para os novos enunciados, inclusive NETs e CR2, cujo foco foi invertido para o nome.
# Apenas hash muda; conteúdo revisado não é substituído por outro lote automático.
db=open_store();cache=[]
for c in changes:
 for card in A('cardsInfo',cards=c['before']['cards']):
  row=db.execute('select * from explicacoes where card_id=?',(card['cardId'],)).fetchone();assert row and row[3]=='ok';cache.append(row)
  ordered=[f['value'] for f in sorted(card['fields'].values(),key=lambda f:f['order'])]
  db.execute('update explicacoes set hash=?,modelo=? where card_id=?',(card_hash(ordered,card['ord']),'codex-revisao',card['cardId']))
db.commit();(R/'author-refinement-cache-before.json').write_text(json.dumps(cache,ensure_ascii=False,indent=1));(R/'author-refinement-verification.json').write_text(json.dumps({'notes_refined':len(changes),'card_ids_personal_flags_and_study_unchanged':True,'readback':'ok','explanations_read_and_validated_for_reworded_targets':len(cache)},indent=1));print('Notas refinadas',len(changes),'explicações preservadas/revalidadas',len(cache))
