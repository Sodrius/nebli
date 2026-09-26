"""Leitura do Anki e das fontes; evidência local da revisão autorizada."""
import json, re, sys
from pathlib import Path
import requests
import fitz

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent

def call(action, **params):
    r = requests.post('http://127.0.0.1:8765', json={'action': action, 'version': 6, 'params': params}, timeout=60)
    r.raise_for_status()
    d = r.json()
    if d['error']: raise RuntimeError(d['error'])
    return d['result']

def main():
    decks = call('deckNames')
    deck = next(d for d in decks if d.startswith('NEBLI::UC03::P2::Patologia::'))
    ids = call('findNotes', query=f'deck:"{deck}"')
    notes = call('notesInfo', notes=ids)
    cards = call('cardsInfo', cards=[c for n in notes for c in n['cards']])
    old = call('notesInfo', notes=[1756729011062,1756729082220,1756729186960,1756729259876,1756729345752,1756729379882])
    models = {}
    for name in {n['modelName'] for n in notes}:
        models[name] = {a: call(a, modelName=name) for a in ('modelFieldNames','modelTemplates','modelStyling')}
    snap = {'deck':deck,'notes':notes,'cards':cards,'old':old,'models':models,'media_dir':call('getMediaDirPath'),'capabilities':call('apiReflect', scopes=['actions'])}
    target = ROOT/'before-v2.json'
    if target.exists(): raise RuntimeError('Snapshot já existe; não sobrescrever')
    target.write_text(json.dumps(snap,ensure_ascii=False,indent=2),encoding='utf-8')
    pdf=fitz.open(ROOT/'slides.pdf')
    out=[]
    for i,p in enumerate(pdf):
        out.append(f'\n## Página {i+1}\n'+p.get_text())
        for a in (p.annots() or []):
            if a.info.get('content'): out.append('Comentário: '+a.info['content'])
    (ROOT/'slides-texto-comentarios.txt').write_text('\n'.join(out),encoding='utf-8')
    print(json.dumps({'deck':deck,'notes':len(notes),'cards':len(cards),'reps':sum(c['reps'] for c in cards),'old_available':[n.get('noteId') for n in old], 'models':list(models),'media_dir':snap['media_dir'],'capabilities':snap['capabilities']},ensure_ascii=False))

if __name__=='__main__': main()
