import json,re,sys
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
TAGS=['#AK_Step1_v12::#B&B::13_Immunology::01_Basic_Immunology::04_The_Complement_System*',
'#AK_Step1_v12::#Bootcamp::Immunology::08_Complement*',
'#AK_Step1_v12::#FirstAid::02_Immunology::03_Immune_Responses::04_Complement',
'#AK_Step1_v12::#FirstAid::02_Immunology::03_Immune_Responses::05_Complement_disorders*',
'#AK_Step1_v12::#NinjaNerd::02_Immunology::01_Physiology::03_Inflammation:_Complement_Proteins_(Part_3)',
'#AK_Step1_v12::#Physeo::08_Immunology::01_Immunology::05_Complement',
'#AK_Step1_v12::#Pixorize::02_Immunology::02_Complement*',
'#AK_Step1_v12::#SketchyImmunology::02_Innate_Immune_System::01_Complement*',
'#AK_Step1_v12::#SketchyPath::11_Immunology::02_Immunodeficiency::03_Complement_System_Disorders']
q=' OR '.join(f'"tag:{t}"' for t in TAGS)
ids=call('findNotes',query=f'({q}) note:AnKingOverhaul*')
notes=call('notesInfo',notes=ids)
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
out=[]
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
for n in notes:
    f={k:v['value'] for k,v in n['fields'].items()}
    cz=sorted({int(x) for x in re.findall(r'{{c(\d+)::',f.get('Text',''))})
    ci=call('cardsInfo',cards=n['cards'])
    out.append({'nid':n['noteId'],'hy':HY in n['tags'],'yield':[t.split('::')[-1] for t in n['tags'] if 'Low/HighYield' in t],'clozes':cz,'susp':[c['queue']==-1 for c in ci],'decks':sorted({c['deckName'] for c in ci}),'text':strip(f.get('Text','')),'extra':strip(f.get('Extra',''))[:300],'img':len(re.findall('<img',''.join(f.values()))),'srcs':sorted({t.split('::')[1] for t in n['tags'] if t.startswith('#AK_Step1_v12::#') and 'Low/High' not in t})})
out.sort(key=lambda x:x['text'])
(ROOT/'pool.json').write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding='utf-8')
print(len(out), sum(len(o['clozes']) for o in out), sum(o['hy'] for o in out))
for o in out: print(f"{o['nid']} HY={int(o['hy'])} c={o['clozes']} img={o['img']} | {o['text'][:260]}")
