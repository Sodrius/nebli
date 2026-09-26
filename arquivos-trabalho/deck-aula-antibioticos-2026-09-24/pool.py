import json,re,sys
from collections import defaultdict
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
P='#AK_Step1_v12::'
FA=P+'#FirstAid::03_Microbiology::07_Antimicrobials::'
BC=P+'#Bootcamp::Microbiology::36_Antibiotics::'
BB=P+'#B&B::14_Infectious_Disease::03_Antibiotics::'
NN=P+'#NinjaNerd::03_Microbiology::04_Pharmacology::'
TAGS={'FA':[FA+x+'*' for x in ['01_','02_','03_','04_','05_','06_','07_','08_','09_','10_','11_','12_','13_','14_','15_','16_','17_','18_','19_','20_','22_','23_','24_']],
      'BC':[BC+f'{i:02d}_*' for i in list(range(1,18))+[19,21]],
      'BB':[BB+'*'],
      'NN':[NN+x+'*' for x in ['03_','04_','05_','06_','07_']]}
TEXT=['antibiogram','disk diffusion','Kirby-Bauer','minimum inhibitory concentration','MIC','bacteriostatic','bactericidal','extended-spectrum','ESBL','carbapenemase','KPC','NDM','efflux pump','porin','mecA','PBP2a','D-Ala-D-Lac','biofilm','PABA','polymyxin','colistin','gray baby','grey baby','kernicterus','transpeptidase','penicillin-binding','beta-lactamase','β-lactamase','DNA gyrase','topoisomerase','multidrug resistant','conjugation','R plasmid','Mueller-Hinton','E-test','clavulan','Qnr','mcr-1']
HY=P+'#Low/HighYield::1-HighYield'
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
D='"deck:Referências::Anking Step Deck"'
hits=defaultdict(set)
for src,ts in TAGS.items():
    for t in ts:
        for nid in call('findNotes',query=f'{D} "tag:{t}"'): hits[nid].add(src)
for t in TEXT:
    ids=call('findNotes',query=f'{D} "Text:*{t}*"')
    if len(ids)>300: print('skip',t,len(ids)); continue
    for nid in ids: hits[nid].add('txt:'+t)
ids=sorted(hits); rows=[]
for s in range(0,len(ids),300):
    for n in call('notesInfo',notes=ids[s:s+300]):
        f={k:v['value'] for k,v in n['fields'].items()}
        if 'Text' not in f: continue
        rows.append({'nid':n['noteId'],'model':n['modelName'],'hy':HY in n['tags'],'src':sorted(hits[n['noteId']]),
          'clozes':sorted({int(x) for x in re.findall(r'{{c(\d+)::',f['Text'])}),'text':strip(f['Text']),'extra':strip(f.get('Extra',''))[:300],
          'img':len(re.findall('<img',f.get('Extra','')+f['Text'])),'tags':[t for t in n['tags'] if 'Antibiotic' in t or 'Antimicrob' in t or 'Pharmacology' in t][:4]})
(ROOT/'pool.json').write_text(json.dumps(rows,ensure_ascii=False,indent=1),encoding='utf-8')
from collections import Counter
print(len(rows), Counter(s.split(':')[0] for r in rows for s in r['src']))
