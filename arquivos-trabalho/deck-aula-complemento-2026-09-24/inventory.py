import json, re, sys, urllib.request
from collections import defaultdict
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).parent
QUERIES = {
 'general': ['complement', 'complemento'],
 'pathways': ['classical pathway', 'alternative pathway', 'lectin pathway', 'mannose-binding lectin', 'mannose binding lectin', 'MBL', 'MASP'],
 'components': ['C1q', 'C1r', 'C1s', 'C3b', 'C4b', 'C3a', 'C5a', 'C5b', 'C2a', 'C2b', 'iC3b', 'C3d', 'C3 convertase', 'C5 convertase', 'Bb', 'factor B', 'factor D', 'properdin'],
 'effectors': ['membrane attack complex', 'MAC', 'C5b-9', 'anaphylatoxin', 'opsonin', 'opsonization', 'immune complex clearance'],
 'receptors': ['CR1', 'CR2', 'CR3', 'CD35', 'CD21', 'Mac-1', 'CD11b'],
 'regulation': ['C1 esterase inhibitor', 'C1-INH', 'C1 inhibitor', 'DAF', 'CD55', 'CD59', 'factor H', 'factor I', 'decay-accelerating'],
 'disease': ['hereditary angioedema', 'paroxysmal nocturnal hemoglobinuria', 'Neisseria', 'C3 deficiency', 'C5-C9', 'C2 deficiency', 'CH50', 'AH50', 'atypical hemolytic uremic', 'eculizumab'],
}
def call(action, **params):
    body=json.dumps({'action':action,'version':6,'params':params}).encode()
    req=urllib.request.Request('http://127.0.0.1:8765',body,{'Content-Type':'application/json'})
    with urllib.request.urlopen(req, timeout=120) as f: data=json.load(f)
    if data['error']: raise RuntimeError(f'{action}: {data["error"]}')
    return data['result']
def main():
    hits=defaultdict(set); counts={}
    for g,terms in QUERIES.items():
        for t in terms:
            ids=call('findNotes',query=f'"{t}" -deck:NEBLI*' if False else f'"{t}"')
            counts[t]=len(ids)
            if len(ids)>400: continue  # too generic; skip (e.g. MAC/Bb)
            for nid in ids: hits[nid].add(t)
    ids=sorted(hits); rows=[]
    for s in range(0,len(ids),200):
        for n in call('notesInfo',notes=ids[s:s+200]):
            rows.append({'nid':n['noteId'],'model':n['modelName'],'tags':n['tags'],'fields':{k:v['value'] for k,v in n['fields'].items()},'cards':n['cards'],'queries':sorted(hits[n['noteId']])})
    (ROOT/'inventory.json').write_text(json.dumps({'counts':counts,'notes':rows},ensure_ascii=False,indent=1),encoding='utf-8')
    from collections import Counter
    print(json.dumps(counts,ensure_ascii=False)); print(len(rows)); print(Counter(r['model'] for r in rows).most_common())
if __name__=='__main__': main()
