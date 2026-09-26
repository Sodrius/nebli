import json,re,sys
from collections import defaultdict
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
P='#AK_Step1_v12::'
FA=P+'#FirstAid::03_Microbiology::'
BC=P+'#Bootcamp::Microbiology::'
BB=P+'#B&B::14_Infectious_Disease::'
GROUPS={
 'VIR':[FA+'01_Basic_Bacteriology::13_*',FA+'01_Basic_Bacteriology::15_*',FA+'01_Basic_Bacteriology::16_*',FA+'01_Basic_Bacteriology::17_*',BB+'01_Basics_of_Microbiology::05_Virulence*',BC+'03_Bacterial_Toxins*'],
 'STA':[FA+'02_Clinical_Bacteriology::03_*',FA+'02_Clinical_Bacteriology::04_*',FA+'02_Clinical_Bacteriology::05_*',BC+'04_Staphylococcus*',BB+'02_Bacteria::01_Staphylococci*'],
 'STR':[FA+'02_Clinical_Bacteriology::06_*',FA+'02_Clinical_Bacteriology::07_*',FA+'02_Clinical_Bacteriology::08_*',FA+'02_Clinical_Bacteriology::09_*',FA+'02_Clinical_Bacteriology::11_*',BC+'05_Streptococcus*',BB+'02_Bacteria::02_Streptococci*'],
 'BGP':[FA+'02_Clinical_Bacteriology::12_*',FA+'02_Clinical_Bacteriology::13_*',FA+'02_Clinical_Bacteriology::15_*',FA+'02_Clinical_Bacteriology::16_*',FA+'02_Clinical_Bacteriology::17_*',BC+'06_Enterococcus_and_Bacillus*',BC+'07_Clostridium*',BC+'09_Non_-Spore*'],
 'BGN':[FA+'02_Clinical_Bacteriology::29_*',FA+'02_Clinical_Bacteriology::30_*',FA+'02_Clinical_Bacteriology::33_*',FA+'02_Clinical_Bacteriology::22_*',BC+'10_Lactose*',BC+'11_Non_-Lactose*'],
}
HY=P+'#Low/HighYield::1-HighYield'
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
D='"deck:Referências::Anking Step Deck"'
hits=defaultdict(set)
for g,ts in GROUPS.items():
    for t in ts:
        for nid in call('findNotes',query=f'{D} "tag:{t}"'): hits[nid].add(g)
ids=sorted(hits); rows=[]
for s in range(0,len(ids),300):
    for n in call('notesInfo',notes=ids[s:s+300]):
        f={k:v['value'] for k,v in n['fields'].items()}
        if 'Text' not in f: continue
        rows.append({'nid':n['noteId'],'hy':HY in n['tags'],'g':sorted(hits[n['noteId']])[0],'clozes':sorted({int(x) for x in re.findall(r'{{c(\d+)::',f['Text'])}),'text':strip(f['Text'])})
(ROOT/'pool.json').write_text(json.dumps(rows,ensure_ascii=False),encoding='utf-8')
from collections import Counter
print(len(rows),Counter(r['g'] for r in rows))
for g in GROUPS:
    with open(ROOT/f'pool-{g}.txt','w',encoding='utf-8') as o:
        for r in sorted([r for r in rows if r['g']==g],key=lambda r:r['text']):
            o.write(f"{r['nid']} {'H' if r['hy'] else '.'}{len(r['clozes'])} {r['text'][:170]}\n")
