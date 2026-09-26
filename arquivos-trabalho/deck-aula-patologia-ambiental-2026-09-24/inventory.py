"""Read-only candidate search for the environmental pathology lecture."""
import json
from pathlib import Path
from urllib.request import Request,urlopen

HERE=Path(__file__).parent
TERMS=['air pollution','particulate','PM2.5','PM10','biomass','smoke','ozone','nitrogen dioxide','sulfur dioxide','carbon monoxide','atherosclerosis','oxidized LDL','mucociliary','alveolar macrophage','diesel','anthracosis','environmental','pollutant','smog','air quality','climate change','indoor air','oxidative stress']

def call(action,**params):
 data=json.dumps(dict(action=action,version=6,params=params)).encode()
 with urlopen(Request('http://127.0.0.1:8765',data=data,headers={'Content-Type':'application/json'}),timeout=120) as res:r=json.load(res)
 if r['error']:raise RuntimeError(r['error'])
 return r['result']

def main():
 groups={};all_ids=set()
 for deck in ['NEBLI','Referências::Anking Step Deck','Referências::Referências Externas']:
  ids=set()
  for term in TERMS:ids.update(call('findNotes',query=f'deck:"{deck}" "{term}"'))
  groups[deck]=len(ids);all_ids|=ids
 notes=[n for i in range(0,len(all_ids),100) for n in call('notesInfo',notes=sorted(all_ids)[i:i+100])]
 cids=[c for n in notes for c in n['cards']]
 cards={c['cardId']:c for i in range(0,len(cids),100) for c in call('cardsInfo',cards=cids[i:i+100])}
 out=dict(profile=call('getActiveProfile'),terms=TERMS,groups=groups,notes=[dict(nid=n['noteId'],model=n['modelName'],fields={k:v['value'] for k,v in n['fields'].items()},tags=n['tags'],cards=[dict(cid=c,deck=cards[c]['deckName'],flags=cards[c]['flags'],queue=cards[c]['queue']) for c in n['cards']]) for n in notes])
 (HERE/'inventory.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(dict(profile=out['profile'],groups=groups,notes=len(notes)),ensure_ascii=False))
if __name__=='__main__':main()
