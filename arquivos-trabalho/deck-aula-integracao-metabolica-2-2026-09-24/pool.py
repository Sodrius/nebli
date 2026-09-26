import json,re,sys
from collections import defaultdict
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
P='#AK_Step1_v12::'
FA=P+'#FirstAid::01_Biochem::06_Metabolism::'
BC=P+'#Bootcamp::Biochemistry::'
BB=P+'#B&B::'
GROUPS={
 'FUEL':[FA+'42_Metabolic_fuel_use*',BC+'09_Lipid_Metabolism::18_Fed_vs._Fasting_State*',BB+'*02_Metabolism::13_Exercise_and_Starvation*'],
 'GK':[FA+'07_Hexokinase_vs_glucokinase*'],
 'GLYREG':[FA+'35_Glycogen_regulation*',BC+'08_Glycogen::03_Regulation*'],
 'GLYCOL':[FA+'09_Regulation_by_fructose*',FA+'10_Pyruvate_dehydrogenase_complex*',FA+'15_Gluconeogenesis_irreversible*'],
 'LIP':[FA+'39_Fatty_acid_metabolism*',BC+'09_Lipid_Metabolism::11_Adipocytes*',BC+'09_Lipid_Metabolism::15_Fatty_Acid_Synthesis*'],
 'KET':[FA+'40_Ketone_bodies*',BC+'09_Lipid_Metabolism::16_Ketones*'],
 'AA':[BC+'10_Protein_Metabolism::14_Ammonia*',BC+'10_Protein_Metabolism::15_Ammonia*'],
 'INS':[BB+'*03_Pancreas::01_Insulin*',BB+'*03_Pancreas::02_Glucagon*'],
 'DM':[BB+'*03_Pancreas::03_Type_I_Diabetes*',BB+'*03_Pancreas::04_Type_II_Diabetes*'],
}
HY=P+'#Low/HighYield::1-HighYield'
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
D='"deck:Referências::Anking Step Deck"'
hits=defaultdict(list)
for g,ts in GROUPS.items():
    for t in ts:
        for nid in call('findNotes',query=f'{D} "tag:{t}"'):
            if g not in hits[nid]: hits[nid].append(g)
ids=sorted(hits); rows=[]
for s in range(0,len(ids),300):
    for n in call('notesInfo',notes=ids[s:s+300]):
        f={k:v['value'] for k,v in n['fields'].items()}
        if 'Text' not in f: continue
        rows.append({'nid':n['noteId'],'hy':HY in n['tags'],'g':hits[n['noteId']][0],'clozes':sorted({int(x) for x in re.findall(r'{{c(\d+)::',f['Text'])}),'text':strip(f['Text']),'extra':strip(f.get('Extra',''))[:300]})
(ROOT/'pool.json').write_text(json.dumps(rows,ensure_ascii=False),encoding='utf-8')
from collections import Counter
print(len(rows),Counter(r['g'] for r in rows))
for g in GROUPS:
    with open(ROOT/f'pool-{g}.txt','w',encoding='utf-8') as o:
        for r in sorted([r for r in rows if r['g']==g],key=lambda r:r['text']):
            o.write(f"{r['nid']} {'H' if r['hy'] else '.'}{len(r['clozes'])} {r['text'][:175]}\n")
