import json,re,sys
from collections import defaultdict
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
P='#AK_Step1_v12::'
FA=P+'#FirstAid::03_Microbiology::01_Basic_Bacteriology::'
BB=P+'#B&B::14_Infectious_Disease::01_Basics_of_Microbiology::'
BC=P+'#Bootcamp::Microbiology::01_Fundamentals_of_Bacteriology::'
TAGS=[FA+x+'*' for x in ['01_','02_','03_','07_','11_','12_']]+[BB+x+'*' for x in ['01_','02_']]+[BC+x+'*' for x in ['01_','02_','03_','04_','05_']]+[P+'#NinjaNerd::03_Microbiology::01_Basics*']
TEXT=['flagellin','teichoic','lipoteichoic','lipid A','O antigen','K antigen','H antigen','Ziehl','acid-fast','mycolic','dark-field','darkfield','silver stain','Giemsa','Mycoplasma','endospore','dipicolinic','capsule','glycocalyx','biofilm','70S','16S','spirochete','periplasm','peptidoglycan','Gram stain','crystal violet','safranin','pili','fimbriae','sex pilus','nucleoid','three domains','Archaea','coccobacill','comma-shaped','Quellung','India ink']
HY=P+'#Low/HighYield::1-HighYield'
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
D='"deck:Referências::Anking Step Deck"'
hits=defaultdict(set)
for t in TAGS:
    for nid in call('findNotes',query=f'{D} "tag:{t}"'): hits[nid].add('tag')
for t in TEXT:
    ids=call('findNotes',query=f'{D} "Text:*{t}*"')
    if len(ids)>250: print('skip',t,len(ids)); continue
    for nid in ids: hits[nid].add('txt:'+t)
ids=sorted(hits); rows=[]
for s in range(0,len(ids),300):
    for n in call('notesInfo',notes=ids[s:s+300]):
        f={k:v['value'] for k,v in n['fields'].items()}
        if 'Text' not in f: continue
        tt=[t for t in n['tags'] if ('01_Basic_Bacteriology::' in t or '01_Basics_of_Microbiology::' in t or '01_Fundamentals_of_Bacteriology::' in t)]
        rows.append({'nid':n['noteId'],'hy':HY in n['tags'],'src':sorted(hits[n['noteId']]),'topic':(tt[0].split('::')[-1] if tt else 'zz-'+sorted(hits[n['noteId']])[0]),
          'clozes':sorted({int(x) for x in re.findall(r'{{c(\d+)::',f['Text'])}),'text':strip(f['Text']),'img':'<img' in f.get('Extra','')})
(ROOT/'pool.json').write_text(json.dumps(rows,ensure_ascii=False,indent=1),encoding='utf-8')
rows.sort(key=lambda r:(r['topic'],r['text']))
with open(ROOT/'pool-lines.txt','w',encoding='utf-8') as o:
    cur=None
    for r in rows:
        if r['topic']!=cur: cur=r['topic']; o.write(f'\n## {cur}\n')
        o.write(f"{r['nid']} {'H' if r['hy'] else '.'}{len(r['clozes'])}{'i' if r['img'] else ''} {r['text'][:200]}\n")
print(len(rows))
