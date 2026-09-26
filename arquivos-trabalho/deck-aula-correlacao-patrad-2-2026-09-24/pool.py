import json,re,sys
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
FA='#AK_Step1_v12::#FirstAid::09_Gastrointestinal::'
TAGQ=[FA+'02_Anatomy::08_Portosystemic_anastomoses*',FA+'02_Anatomy::10_Liver_tissue_architecture*',FA+'04_Pathology::31_Cirrhosis_and_portal_hypertension*',
      FA+'04_Pathology::35_Alcoholic_liver_disease*',FA+'04_Pathology::36_Nonalcoholic_fatty_liver_disease*',FA+'04_Pathology::39_Liver_tumors*',
      FA+'02_Anatomy::06_Gastrointestinal_blood_supply_and_innervation*','#AK_Step1_v12::#FirstAid::01_Biochemistry::*Ethanol_metabolism*',
      '#AK_Step1_v12::#FirstAid::04_Pathology::03_Neoplasia::07_Common_metastases::*Liver*']
TERMS=['hemangioma','steatosis','fatty liver','stellate cell','Ito cell','caput medusae','esophageal varices','varices','portal hypertension','splenomegaly',
       'hypersplenism','ascites','hepatocellular carcinoma','cirrhosis','regenerative nodule','micronodular','macronodular','space of Disse','sinusoid',
       'zone 3','centrilobular','acinus','portal triad','hepatic artery','portal vein','Hounsfield','hyperechoic','ultrasound liver','washout','angiosarcoma',
       'NADH/NAD','cholestasis','bile plug','Kupffer','perisinusoidal','hepatic venous pressure']
def q(query):
    try: return call('findNotes',query=query)
    except Exception as e: print('ERR',query,e); return []
hits={}
for t in TAGQ:
    for nid in q(f'"tag:{t}"'): hits.setdefault(nid,set()).add('tag')
counts={}
for t in TERMS:
    ids=q(f'"{t}" -"deck:NEBLI*"'); counts[t]=len(ids)
    if len(ids)>300: continue
    for nid in ids: hits.setdefault(nid,set()).add(t)
ids=sorted(hits); rows=[]
for s in range(0,len(ids),200):
    for n in call('notesInfo',notes=ids[s:s+200]):
        rows.append({'nid':n['noteId'],'model':n['modelName'],'tags':n['tags'],'fields':{k:v['value'] for k,v in n['fields'].items()},'cards':n['cards'],'why':sorted(hits[n['noteId']])})
(ROOT/'inventory.json').write_text(json.dumps({'counts':counts,'notes':rows},ensure_ascii=False,indent=1),encoding='utf-8')
print(counts); print(len(rows))
from collections import Counter; print(Counter(r['model'] for r in rows).most_common(12))
def txt(r):
    f=r['fields']; t=f.get('Text') or f.get('Front') or f.get('Header') or next(iter(f.values()))
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)).strip()
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
with open(ROOT/'pool-lines.txt','w',encoding='utf-8') as out:
    for r in rows:
        if r['model'].startswith('AnKingOverhaul') or 'MCAT' in r['model'] or r['model'].startswith('Cloze'):
            dk='NEBLI' if any(t.startswith('NEBLI::') for t in r['tags']) else ''
            sec=[t.split('::')[4] if t.startswith('#AK_Step1_v12::#FirstAid::') and len(t.split('::'))>4 else '' for t in r['tags']]
            sec=next((s for s in sec if s),'')
            out.write(f"{r['nid']} {'H' if HY in r['tags'] else '-'}{len(r['cards'])} {dk} [{sec[:28]}] {r['model'][:14]} | {txt(r)[:230]}\n")
