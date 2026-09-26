"""Busca adicional por lacuna; nenhuma escrita no Anki."""
import json, re, html
from inspecionar_v2 import call, ROOT

QUERIES = {
 'vascular': 'deck:"AnKing Step Deck" ("Text:*exudat*" OR "Text:*transudat*" OR "Text:*hemoconcentr*" OR "Text:*stasis*" OR "Text:*endothelial contraction*" OR "Text:*transcytosis*")',
 'mediadores': 'deck:"AnKing Step Deck" ("Text:*histamine*" OR "Text:*nitric oxide*" OR "Text:*platelet.activating*" OR "Text:*platelet activating*" OR "Text:*lipoxin*")',
 'sistemico': 'deck:"AnKing Step Deck" ("Text:*acute.phase*" OR "Text:*leukocytosis*" OR "Text:*lymphaden*" OR "Text:*lymph flow*" OR "Text:*lymphatic drainage*")',
 'farmacos': 'deck:"AnKing Step Deck" ("Text:*cyclooxygenase*" OR "Text:*phospholipase*" OR "Text:*leukotriene*" OR "Text:*NSAID*ulcer*")',
 'finais': 'deck:"AnKing Step Deck" ("Text:*resolution*" OR "Text:*phlegmon*" OR "Text:*ulcer*erosion*" OR "Text:*inflammation*fibrosis*" OR "Text:*lysosom*enzym*" OR "Text:*reactive oxygen*tissue*")',
 'externos': '-deck:"AnKing Step Deck" -deck:"NEBLI" ("lymphatic drainage" OR "vascular permeability" OR "phlegmon" OR "platelet activating" OR "endothelial injury" OR "transudate" OR "collagenase")',
}
def clean(x): return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',x))).strip()
def main():
 matches={k:call('findNotes',query=q) for k,q in QUERIES.items()}
 ids=sorted({n for v in matches.values() for n in v})
 notes=[]
 for i in range(0,len(ids),100): notes.extend(call('notesInfo',notes=ids[i:i+100]))
 (ROOT/'candidatos-v2.json').write_text(json.dumps({'queries':QUERIES,'matches':matches,'notes':notes},ensure_ascii=False,indent=2),encoding='utf-8')
 print({k:len(v) for k,v in matches.items()})
 for k in matches:
  print('\n###',k)
  for n in notes:
   if n['noteId'] not in matches[k]: continue
   f=n['fields']; t=f.get('Text',f.get('Front',next(iter(f.values()))))['value']
   print(n['noteId'],clean(t)[:900])
if __name__=='__main__':main()
