import json,re,sys
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
P='#AK_Step1_v12::'
TAGS=[P+'#FirstAid::03_Microbiology::01_Basic_Bacteriology::*Properties_of_Growth_Media',P+'#FirstAid::03_Microbiology::01_Basic_Bacteriology::04_Special_culture_requirements',P+'#FirstAid::03_Microbiology::01_Basic_Bacteriology::05_Anaerobes',P+'#B&B::14_Infectious_Disease::01_Basics_of_Microbiology::03_Bacterial_Culture*',P+'#B&B::14_Infectious_Disease::01_Basics_of_Microbiology::04_Special_Growth_Requirements*',P+'#B&B::14_Infectious_Disease::01_Basics_of_Microbiology::06_Growth_and_Genetics*',P+'#Bootcamp::Microbiology::01_Fundamentals_of_Bacteriology::06_MacConkey_Agar_and_Eosin_Methylene_Blue_Agar',P+'#Bootcamp::Microbiology::01_Fundamentals_of_Bacteriology::08_Additional_Culture_Associations']
HY=P+'#Low/HighYield::1-HighYield'
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
q=' OR '.join(f'"tag:{t}"' for t in TAGS)
ids=call('findNotes',query=f'({q}) note:AnKingOverhaul*')
rows=[]
for n in call('notesInfo',notes=ids):
    f={k:v['value'] for k,v in n['fields'].items()}
    rows.append({'nid':n['noteId'],'hy':HY in n['tags'],'clozes':sorted({int(x) for x in re.findall(r'{{c(\d+)::',f['Text'])}),'text':strip(f['Text']),'extra':strip(f['Extra'])[:200],'img':len(re.findall('<img',f['Extra']+f['Text']))})
rows.sort(key=lambda r:r['text'])
(ROOT/'pool.json').write_text(json.dumps(rows,ensure_ascii=False,indent=1),encoding='utf-8')
print(len(rows))
for r in rows: print(f"{r['nid']} {'HY' if r['hy'] else '  '} c{r['clozes']} i{r['img']} | {r['text'][:200]}")
