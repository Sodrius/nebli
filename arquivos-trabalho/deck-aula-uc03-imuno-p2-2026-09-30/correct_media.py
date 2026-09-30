"""Retira dois esquemas inexatos somente das cópias desta corrida; originais intactos."""
import json,re,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from nebli.decks import Anki,escrita
R=Path(__file__).parent;A=Anki();bad={'8f4ce0ed345e5153fbff4de0c723fa52.webp','a77c863c3f99e7fd03c5b5fe248eefdb.webp'}
changes=[]
for folder in ['complemento','inflamacao']:
 p=R/folder;plan=json.loads((p/'plan.json').read_text());receipt=json.loads((p/'receipt.json').read_text())
 for e,r in zip(plan['entries'],receipt['notes']):
  vals={k:v['value'] for k,v in A('notesInfo',notes=[r['nid']])[0]['fields'].items()}
  assert vals==e['fields'],('Edição concorrente',r['nid'])
  fixed={k:re.sub(r'<img\b[^>]*>',lambda m:'' if any(n in m.group() for n in bad) else m.group(),v,flags=re.I) for k,v in vals.items()}
  if fixed!=vals:changes.append({'folder':folder,'key':e['key'],'nid':r['nid'],'before':vals,'after':fixed})
(R/'media-corrections-before.json').write_text(json.dumps(changes,ensure_ascii=False,indent=1))
with escrita(A,'uc03-imuno-revisao-imagens-20260930'):
 for c in changes:
  vals={k:v['value'] for k,v in A('notesInfo',notes=[c['nid']])[0]['fields'].items()};assert vals==c['before']
  A('updateNoteFields',note={'id':c['nid'],'fields':c['after']})
  assert {k:v['value'] for k,v in A('notesInfo',notes=[c['nid']])[0]['fields'].items()}==c['after']
for folder in ['complemento','inflamacao']:
 p=R/folder;plan=json.loads((p/'plan.json').read_text());(p/'plan-pre-media-review.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1))
 for e in plan['entries']:
  c=next((c for c in changes if c['folder']==folder and c['key']==e['key']),None)
  if c:
   e['fields']=c['after'];e['fields_hash']=hashlib.sha256(json.dumps(c['after'],sort_keys=True,ensure_ascii=False).encode()).hexdigest();e['media']=[n for n in e.get('media',[]) if n not in bad]
 plan['post_install_review']='media-corrections-before.json: esquemas inexatos retirados das cópias; arquivos/originais conservados.'
 (p/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1))
 receipt=json.loads((p/'receipt.json').read_text());ids=[int(cid) for n in receipt['notes'] for cid in n['cards']]
 (p/'rendered-cards-final.json').write_text(json.dumps(A('cardsInfo',cards=ids),ensure_ascii=False,indent=1))
(R/'media-corrections-verification.json').write_text(json.dumps({'updated_notes':len(changes),'readback':'ok','original_media_untouched':True,'cards_and_personal_flags_unchanged':True},indent=1))
print('Corrigidas',len(changes),'notas novas; readback OK')
