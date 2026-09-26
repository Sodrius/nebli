"""Correção pós-inspeção visual: duas imagens de verso inadequadas nas cópias NEBLI (origens intactas)."""
import json,sys
from datetime import datetime,timezone
from inventory import call
from prepare import ROOT
sys.stdout.reconfigure(encoding='utf-8')
FIXES={
 1790166175204:('AKA high-frequency recombination cell (Hfr)<br><br><div><img src="7945d371628f5694f65cd0390be225fd.webp"></div>',
                'AKA high-frequency recombination cell (Hfr)<br><br><div><img src="8b36e81878cc01caaaf0df403c7b137b.webp"></div>'),
 1790166169397:('AT has 2 bonds vs 3 in GC-easier to break apart<br><br><img src="69460e6e59ee1532f6ea69b41b859177.webp"><br><i><span style="font-size: 10pt;">Photo credit: <a href="https://openstax.org/books/biology-ap-courses/pages/15-3-eukaryotic-transcription">OpenStax</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></span></i>',
                'AT has 2 bonds vs 3 in GC-easier to break apart'),
}
def log(action,value):
    with (ROOT/'journal.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':action,'value':value},ensure_ascii=False)+'\n')
for nid,(old,new) in FIXES.items():
    n=call('notesInfo',notes=[nid])[0]
    if any(c['reps'] for c in call('cardsInfo',cards=n['cards'])): raise RuntimeError(f'Já estudado {nid}')
    cur=n['fields']['Extra']['value']
    if cur==new: print('já corrigido',nid); continue
    if cur!=old: raise RuntimeError(f'Extra inesperado {nid}')
    call('updateNoteFields',note={'id':nid,'fields':{'Extra':new}})
    if call('notesInfo',notes=[nid])[0]['fields']['Extra']['value']!=new: raise RuntimeError(f'Readback falhou {nid}')
    log('fix_image',{'nid':nid,'before':old,'after':new}); print('ok',nid)
