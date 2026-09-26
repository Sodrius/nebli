import json
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
QUERIES = {
    'intestinal': ['intestin', 'small bowel', 'small intestine', 'large intestine', 'colon histology'],
    'surface': ['villi', 'villus', 'microvilli', 'brush border', 'plicae', 'crypts of Lieberkuhn'],
    'cells': ['enterocyte', 'goblet cell', 'Paneth', 'enteroendocrine', 'intestinal stem cell', 'transit amplifying'],
    'niche': ['Lgr5', 'Ascl2', 'Olfm4', 'Bmi1', 'Hopx', 'Wnt', 'BMP', 'Notch', 'ATOH1'],
    'segments': ['Brunner', 'Peyer', 'duodenum', 'jejunum', 'ileum', 'colon crypt'],
    'markers': ['Ki67', 'TUNEL', 'MUC2', 'villin', 'lactase', 'lysozyme'],
    'mucosa': ['muscularis mucosae', 'submucosa', 'lamina propria', 'myenteric plexus'],
}

def call(action, **params):
    body=json.dumps({'action':action,'version':6,'params':params}).encode()
    req=urllib.request.Request('http://127.0.0.1:8765',body,{'Content-Type':'application/json'})
    with urllib.request.urlopen(req, timeout=90) as f: data=json.load(f)
    if data['error']: raise RuntimeError(f'{action}: {data["error"]}')
    return data['result']

def main():
    hits=defaultdict(set)
    counts={}
    for group, terms in QUERIES.items():
        for term in terms:
            ids=call('findNotes',query=f'"{term}"')
            counts[term]=len(ids)
            for nid in ids: hits[nid].add(term)
    ids=sorted(hits)
    rows=[]
    for start in range(0,len(ids),200):
        for note in call('notesInfo',notes=ids[start:start+200]):
            fields={k:v['value'] for k,v in note['fields'].items()}
            rows.append({'nid':note['noteId'],'model':note['modelName'],'tags':note['tags'],'fields':fields,'cards':note['cards'],'queries':sorted(hits[note['noteId']])})
    (ROOT/'inventory.json').write_text(json.dumps({'counts':counts,'notes':rows},ensure_ascii=False,indent=2),encoding='utf-8')
    slim=[]
    for n in rows:
        text=' '.join(re.sub('<[^>]+>',' ',v) for v in n['fields'].values())
        slim.append({'nid':n['nid'],'model':n['model'],'tags':[t for t in n['tags'] if any(w in t.lower() for w in ('hist','anking','highyield','lowyield','nebli','firstaid'))][:12], 'queries':n['queries'],'text':re.sub(r'\s+',' ',text)[:400]})
    (ROOT/'inventory-slim.json').write_text(json.dumps(slim,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'notes':len(rows),'counts':counts,'models':sorted(set(n['model'] for n in rows))},ensure_ascii=False))

if __name__=='__main__': main()
