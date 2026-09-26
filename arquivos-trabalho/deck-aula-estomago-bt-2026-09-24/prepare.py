"""X5 plan: lecture-bounded gastric histology, current-source copies, visual practice."""
import hashlib,json,re
from collections import Counter
from pathlib import Path

HERE=Path(__file__).parent
INV=json.loads((HERE/'inventory.json').read_text(encoding='utf-8'))
BY={n['nid']:n for n in INV['notes']}
LESSON='2026-uc08-biologia-tecidual-03-estrutura-estomago'
DECK='NEBLI::UC08::P1::Biologia Tecidual::Estrutura geral do estômago'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
ANKING=[1482021549752,1482021556058,1482021561377,1482021584289,
         1482021589803,1482021594676,1482021603417,1482021680972,
         1486608728772,1486608734803,1482030311506,1482030315536,
         1482030319798,1482115272152,1482022013033,1486608389324]
HIST=[1702213752722,1702214216607,1702214416325,1702215136161,1702215619877,1702217278951,1702220517802]
LLU=[1667460205460,1667460370853]
PINK={1702220517802}
FIG_GL='b8647af3199815237f7622aff1f2a0fc.webp'
FIG_WALL='82605678fa1ed99d7ea5012425fc98d3.webp'
FUNDIC='paste-5fd70752adbdef98c597af64c2c4cc55bf70fcd3.png'

OVERRIDE={
1702213752722:('At the esophagogastric junction, squamous lining changes abruptly to {{c1::simple columnar}} gastric epithelium.','The gastric side has pits leading into mucosal glands.<br><img src="'+FIG_WALL+'" width="600">'),
1702214216607:('In a gastric pit, surface {{c1::mucous}} cells produce the protective mucus layer.','Bicarbonate trapped in mucus protects the surface epithelium.<br><img src="'+FIG_GL+'" width="650">'),
1702214416325:('In a body-stomach gland, epithelial stem cells cluster near the {{c1::isthmus/neck}}.','Their progeny renew surface and glandular cells.<br><img src="'+FIG_GL+'" width="650">'),
1702215136161:('Among parietal cells in a body-stomach gland, {{c1::mucous neck cells}} produce mucus.','These cells are in the gland neck, below the surface mucous epithelium.<br><img src="'+FIG_GL+'" width="650">'),
1702215619877:('In H&E, the large {{c1::eosinophilic}} cells in the upper body gland are parietal cells.','Numerous mitochondria account for the pink cytoplasm.<br><img src="'+FIG_GL+'" width="650">'),
1702217278951:('In the gland base, chief cells are {{c1::basophilic}} because they contain abundant rough ER.','They synthesize pepsinogen; parietal cells nearby are more eosinophilic.<br><img src="'+FIG_GL+'" width="650">'),
1702220517802:('Compared with body glands, cardiac and pyloric glands mainly secrete {{c1::mucus}}.','Cardiac glands can be tortuous; pyloric pits are deep and glands relatively short.'),
}
AUTHORIAL=[
('visual-parietal','In this body-stomach gland, the large pink cells are {{c1::parietal cells}}.<br><img src="'+FUNDIC+'" width="600">','Their eosinophilia reflects numerous mitochondria.'),
('visual-chief','In this body-stomach gland, darker cells near the base are {{c1::chief cells}}.<br><img src="'+FUNDIC+'" width="600">','Their basophilia reflects rough ER for pepsinogen synthesis.'),
]

def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def main():
 assert len(ANKING+HIST+LLU)==len(set(ANKING+HIST+LLU)) and set(ANKING+HIST+LLU)<=BY.keys()
 entries=[]
 for nid in ANKING+HIST+LLU:
  n=BY[nid];origin='AnKing' if nid in ANKING else 'Histology' if nid in HIST else 'LLU Histology'
  f={k:(v if k in ('Text','Extra') else '') for k,v in n['fields'].items()}
  if nid in OVERRIDE:f['Text'],f['Extra']=OVERRIDE[nid]
  if nid in LLU:
   # Preserve only one inspected diagnostic image per card, avoiding several redundant reveals.
   image=(re.findall(r'<img[^>]+>',f['Text']))[-1 if nid==1667460205460 else 0]
   f['Text']=('This H&E section with long body glands is {{c1::fundic/oxyntic stomach}}.' if nid==1667460205460 else 'This H&E section with deep pits and pale glands is {{c1::antral/pyloric stomach}}.')+'<br><br>'+image
  if nid==1482021549752:f['Extra']='<img src="'+FIG_WALL+'" width="600">'
  count=len(set(re.findall(r'\{\{c(\d+)::',f['Text'])))
  assert count>0 and (nid in HIST or count==len(n['cards'])),(nid,count,len(n['cards']))
  entries.append(dict(source_nid=nid,source_model=n['model'],source_fields_hash=digest(n['fields']),source_deck=n['cards'][0]['deck'],source_tags=n['tags'],origin=origin,fields=f,expected_cards=count,pink=nid in PINK,high_yield=nid in ANKING and HY in n['tags']))
 template=BY[ANKING[0]]
 for key,text,extra in AUTHORIAL:
  f={k:'' for k in template['fields']};f['Text']=text;f['Extra']=extra
  entries.append(dict(source_nid=None,key=key,source_model=template['model'],source_fields_hash=None,source_deck=None,source_tags=[],origin='Autoral',fields=f,expected_cards=1,pink=False,high_yield=False))
 totals=dict(notes=len(entries),cards=sum(e['expected_cards'] for e in entries),by_origin=dict(Counter({o:sum(e['expected_cards'] for e in entries if e['origin']==o) for o in {'AnKing','Histology','LLU Histology','Autoral'}})),pink=sum(e['expected_cards'] for e in entries if e['pink']),green=sum(e['expected_cards'] for e in entries if e['high_yield'] and not e['pink']))
 out=dict(lesson_id=LESSON,target_deck=DECK,profile=INV['profile'],source_folder='https://drive.google.com/drive/folders/1ujdOnueUeBz9uVGzmBRFwCLSX08a_rCG',source_inventory='inventory.json',entries=entries,totals=totals)
 (HERE/'plan.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(totals,ensure_ascii=False))
if __name__=='__main__':main()
