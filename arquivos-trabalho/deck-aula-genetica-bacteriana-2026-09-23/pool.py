import json,re,sys
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
P='#AK_Step1_v12::'
GROUPS={
 'genetics':[P+'#FirstAid::03_Microbiology::01_Basic_Bacteriology::14_Bacterial_genetics*',P+'#Bootcamp::Microbiology::02_Bacterial_Genetics*',P+'#NinjaNerd::03_Microbiology::01_Basics::03_Bacterial_Genetics*',P+'#OME*Bacterial_Genetics*',P+'#Physeo::06_Micro::01_Fundamentals::03_Bacterial_Genetics*'],
 'replication':[P+'#FirstAid::01_Biochem::01_Molecular::06_DNA_replication*',P+'#B&B::07_Cell_Bio::01_Molecular::01_DNA_Replication*',P+'#Bootcamp::Genetics::02_DNA_Replication_Transcription_and_Translation::01_DNA_Replication',P+'#SketchyBiochem::03_Molecular_Biology::01_DNA::02_DNA_Replication*',P+'#Physeo::05_Biochem::01_Molecular_Biology::01_DNA_Replication'],
 'mutation':[P+'#FirstAid::01_Biochem::01_Molecular::08_Mutations_in_DNA*',P+'#B&B::07_Cell_Bio::01_Molecular::02_DNA_Mutations*',P+'#Bootcamp::Genetics::03_DNA_Mutations,_Damage,_and_Repair::01_DNA_Mutations_and_Damage',P+'#SketchyBiochem::03_Molecular_Biology::01_DNA::03_DNA_Mutations',P+'#Physeo::05_Biochem::01_Molecular_Biology::05_DNA_Mutations'],
 'crispr_recomb':[P+'#FirstAid::01_Biochem::03_Laboratory_Techniques::02_CRISPR/Cas9',P+'#Bootcamp::Genetics::05_Laboratory_Techniques::02_CRISPR_Cas9',P+'#Physeo::05_Biochem::03_Lab_Techniques::06_CRISPR_Cas9_&_Molecular_Cloning',P+'#SketchyBiochem::03_Molecular_Biology::04_Recombinant_DNA_&_Biotechnology::01_Recombinant_DNA_(Overview)_Molecular_Cloning_&_PCR'],
}
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
out={}; seen=set()
for g,tags in GROUPS.items():
    q=' OR '.join(f'"tag:{t}"' for t in tags)
    ids=call('findNotes',query=f'({q}) note:AnKingOverhaul*')
    rows=[]
    for n in call('notesInfo',notes=ids):
        if n['noteId'] in seen: continue
        seen.add(n['noteId'])
        f={k:v['value'] for k,v in n['fields'].items()}
        rows.append({'nid':n['noteId'],'hy':HY in n['tags'],'clozes':sorted({int(x) for x in re.findall(r'{{c(\d+)::',f['Text'])}),'text':strip(f['Text']),'extra':strip(f.get('Extra',''))[:250]})
    rows.sort(key=lambda r:r['text'])
    out[g]=rows
(ROOT/'pool.json').write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding='utf-8')
for g,rows in out.items():
    print(f'######## {g} ({len(rows)})')
    for r in rows: print(f"{r['nid']} {'HY' if r['hy'] else '  '} c{r['clozes']} | {r['text'][:210]}")
