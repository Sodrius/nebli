"""Remove links de vídeo (campos Bootcamp/Sketchy) das cópias NEBLI das aulas do Claude. Regra: vídeo nunca no card."""
import json,re,sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent.parent/'deck-aula-operon-procariotos-2026-09-24'))
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent; LOCK=ROOT.parent/'ANKI-ESCRITA.lock'
if LOCK.exists(): sys.exit('lock ocupado: '+LOCK.read_text(encoding='utf-8'))
LOCK.write_text(json.dumps({'executor':'Claude','aula':'limpeza links de vídeo','at':datetime.now(timezone.utc).isoformat()}),encoding='utf-8')
try:
    ids=call('findNotes',query='"deck:NEBLI::*" (Bootcamp:_* OR Sketchy:_*)')
    notes=call('notesInfo',notes=ids)
    notes=[n for n in notes if any(t.startswith('NEBLI::source::') for t in n['tags'])]
    (ROOT/'before-limpar-links.json').write_text(json.dumps(notes,ensure_ascii=False),encoding='utf-8')
    done=0
    for n in notes:
        upd={k:'' for k in ('Bootcamp','Sketchy') if re.sub(r'<[^>]+>','',n['fields'].get(k,{}).get('value','')).strip() or '<a' in n['fields'].get(k,{}).get('value','')}
        if not upd: continue
        call('updateNoteFields',note={'id':n['noteId'],'fields':upd})
        after=call('notesInfo',notes=[n['noteId']])[0]
        if any(after['fields'][k]['value'] for k in upd): raise RuntimeError(f'readback {n["noteId"]}')
        done+=1
    left=call('findNotes',query='"deck:NEBLI::*" (Bootcamp:_* OR Sketchy:_*)')
    print('notas limpas:',done,'| restantes com Bootcamp/Sketchy:',len(left))
finally: LOCK.unlink(missing_ok=True)
