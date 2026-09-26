"""Read-only X3 search across live Anki corpora, including visual fields."""
import json, re
from collections import Counter
from pathlib import Path
from urllib.request import Request, urlopen

OUT = Path(__file__).parent
TERMS = ["esophagus", "oesophagus", "esophageal", "esophagogastric", "cricopharyngeal", "aortic constriction", "esophageal hiatus", "z line", "pharyngoesophageal", "stomach", "gastric rugae", "pylorus", "pyloric", "cardia", "fundus", "greater curvature", "lesser curvature", "angular incisure", "gastric canal", "duodenum", "duodenal", "major papilla", "hepatopancreatic ampulla", "ligament of treitz", "duodenojejunal", "jejunum", "jejunal", "ileum", "ileal", "ileocecal", "vasa recta", "arterial arcade", "circular folds", "mesentery", "mesenteric fat", "antimesenteric"]

def call(action, **params):
    payload=json.dumps({"action":action,"version":6,"params":params}).encode()
    with urlopen(Request("http://127.0.0.1:8765",data=payload,headers={"Content-Type":"application/json"}),timeout=120) as response:
        result=json.load(response)
    if result['error']: raise RuntimeError(f"{action}: {result['error']}")
    return result['result']

def main():
    hits={}; counts={}
    for term in TERMS:
        ids=call('findNotes',query='"'+term+'"')
        counts[term]=len(ids)
        for nid in ids: hits.setdefault(nid,[]).append(term)
    rows=[]
    nids=list(hits)
    for at in range(0,len(nids),100):
        for n in call('notesInfo',notes=nids[at:at+100]):
            fields={k:v['value'] for k,v in n['fields'].items()}
            rows.append(dict(nid=n['noteId'],model=n['modelName'],fields=fields,tags=n['tags'],card_ids=n['cards'],terms=hits[n['noteId']]))
    cids=[cid for r in rows for cid in r['card_ids']]
    cards=[]
    for at in range(0,len(cids),100): cards+=call('cardsInfo',cards=cids[at:at+100])
    bynid={}
    for c in cards: bynid.setdefault(c['note'],[]).append({k:c[k] for k in ('cardId','deckName','ord','queue','flags')})
    for r in rows:
        r['cards']=bynid.get(r['nid'],[])
        r['preview']=re.sub(r'\s+',' ',re.sub(r'<[^>]*>',' ',' '.join(r['fields'].values())))[:600]
    (OUT/'inventory.json').write_text(json.dumps({'profile':call('getActiveProfile'),'queries':counts,'notes':rows},ensure_ascii=False,indent=2),encoding='utf-8')
    with (OUT/'candidates.tsv').open('w',encoding='utf-8') as f:
        f.write('nid\tdeck\tmodel\tterms\ttext\n')
        for r in rows:
            deck=r['cards'][0]['deckName'] if r['cards'] else ''
            f.write(f"{r['nid']}\t{deck}\t{r['model']}\t{','.join(r['terms'])}\t{r['preview'][:320]}\n")
    print(json.dumps({'notes':len(rows),'cards':len(cards),'corpora':Counter(c['deckName'].split('::')[0] for c in cards),'queries':counts},ensure_ascii=False))

if __name__=='__main__':main()
