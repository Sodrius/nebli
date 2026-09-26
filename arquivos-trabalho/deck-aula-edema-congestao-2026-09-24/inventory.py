import json
from pathlib import Path
from urllib.request import Request, urlopen

HERE=Path(__file__).parent
TERMS=['edema','congestion','hyperemia','hydrostatic','oncotic','transudate','exudate','lymphatic obstruction','sodium retention','pulmonary edema','nutmeg liver','heart failure cells','anasarca','ascites','hydrothorax','hydropericardium','Starling','protein losing','nephrotic','cirrhosis']

def call(action,**params):
    data=json.dumps(dict(action=action,version=6,params=params)).encode()
    with urlopen(Request('http://127.0.0.1:8765',data=data,headers={'Content-Type':'application/json'}),timeout=120) as res:r=json.load(res)
    if r['error']:raise RuntimeError(r['error'])
    return r['result']

def main():
    groups={}
    for deck in ['NEBLI','Referências::Anking Step Deck','Referências::Referências Externas']:
        ids=set()
        for term in TERMS:
            ids.update(call('findNotes',query=f'deck:"{deck}" "{term}"'))
        groups[deck]=len(ids)
        if deck=='NEBLI':nebli=ids
        else:external=external|ids if 'external' in locals() else ids
    ids=sorted(nebli|external)
    notes=[n for i in range(0,len(ids),100) for n in call('notesInfo',notes=ids[i:i+100])]
    cids=[c for n in notes for c in n['cards']]
    cards={c['cardId']:c for i in range(0,len(cids),100) for c in call('cardsInfo',cards=cids[i:i+100])}
    out=dict(profile=call('getActiveProfile'),terms=TERMS,groups=groups,notes=[dict(nid=n['noteId'],model=n['modelName'],fields={k:v['value'] for k,v in n['fields'].items()},tags=n['tags'],cards=[dict(cid=c,deck=cards[c]['deckName'],flags=cards[c]['flags'],queue=cards[c]['queue']) for c in n['cards']]) for n in notes])
    (HERE/'inventory.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(profile=out['profile'],groups=groups,notes=len(notes)),ensure_ascii=False))
if __name__=='__main__':main()
