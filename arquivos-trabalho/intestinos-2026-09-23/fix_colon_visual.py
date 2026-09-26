import hashlib,json,re,sys
from pathlib import Path
from inventory import call
from prepare import ROOT,DECK,digest

sys.stdout.reconfigure(encoding='utf-8')
plan=json.loads((ROOT/'plan.json').read_text(encoding='utf-8'))
receipt=json.loads((ROOT/'receipt.json').read_text(encoding='utf-8'))
source=1668633106589
entry=next(e for e in plan['entries'] if e['source_nid']==source)
result=next(r for r in receipt['results'] if r['source_nid']==source)
nid=result['new_nid']
before=call('notesInfo',notes=[nid])[0]
old=before['fields']['Text']['value']
bad='paste-94df37928236e1d152250c0cea6d9b197e90c961.png'
if bad not in old: raise RuntimeError('Expected ambiguous image not found')
new,count=re.subn(r'<br><img src="'+re.escape(bad)+r'"[^>]*>', '',old)
if count!=1: raise RuntimeError(f'Image count {count}')
if before['cards']!=result['cards']: raise RuntimeError('Card identity mismatch')
cards=call('cardsInfo',cards=before['cards'])
if any(c['reps']!=0 for c in cards): raise RuntimeError('Card already reviewed')
call('updateNoteFields',note={'id':nid,'fields':{'Text':new}})
after=call('notesInfo',notes=[nid])[0]
if after['fields']['Text']['value']!=new or after['cards']!=before['cards']: raise RuntimeError('Readback mismatch')
entry['fields']['Text']=new
entry['visual_exclusion']='Second LLU colon image appears to show villi; retained first verified colon image.'
(ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
package=ROOT/'Intestinos.apkg'
if not call('exportPackage',deck=DECK,path=str(package.resolve()),includeSched=True): raise RuntimeError('Re-export failed')
receipt['plan_sha256']=digest(plan)
receipt['package_sha256']=hashlib.sha256(package.read_bytes()).hexdigest()
receipt['visual_correction']={'source_nid':source,'new_nid':nid,'removed_image':bad,'source_untouched':True}
(ROOT/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt['visual_correction'],ensure_ascii=False))
