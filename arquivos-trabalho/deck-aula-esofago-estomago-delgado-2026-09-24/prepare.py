"""Curated X3 plan from this run's live inventory and inspected atlas media."""
import json,re,hashlib
from pathlib import Path
from collections import Counter

HERE=Path(__file__).parent
INV=json.loads((HERE/'inventory.json').read_text(encoding='utf-8'))
BY={n['nid']:n for n in INV['notes']}
LESSON='2026-uc08-anatomia-01-esofago-estomago-delgado'
DECK='NEBLI::UC08::P1::Anatomia::Esôfago, estômago e intestino delgado'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
ANKING=[1474511934874,1482022116564,1482022121968,1482022126258,1482022129277,1521071357761,1486605738754,1486605763821,1486605773525,1486596689685,1486777651171,1543169132935]
ANATOKING=[1542146925579,1548047359393,1548957822372,1543512875540,1542146936648,1542146962028,1542146968329,1542146981325,1542146989512,1542147001992,1542147006993,1542147011020,1542147017558,1548959124455,1562607277712,1542147025458,1542147032139,1546960965736,1542147052236,1542147060583,1542147086703,1542147154111,1542147164351,1542147117997,1542147170288,1542147178958,1542147185761,1546961446430,1542147594239,1562607411862,1562608101719]
DOPE=[1461962456152,1461962475986]
DORIAN=[1527616316221]
ATLAS={1349477488509:['1a','2a','3a','4a'],1349477488609:['1a','5a','8a'],1349477488593:['2a','3a','4a']}
PINK={1474511934874,1542147025458,1542147032139,1546960965736,1548959124455,1562607277712,1562607411862,1562608101719}
SELECTED=ANKING+ANATOKING+DOPE+DORIAN+list(ATLAS)

def digest(x): return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def main():
    assert len(SELECTED)==len(set(SELECTED))
    assert not (set(SELECTED)-BY.keys())
    entries=[]
    for nid in SELECTED:
        n=BY[nid]; f=dict(n['fields']); model=n['model']; tags=n['tags']; origin=('AnKing' if nid in ANKING else 'AnatoKing' if nid in ANATOKING else 'Dope Anatomy' if nid in DOPE or nid in ATLAS else 'Dorian')
        if nid in ANATOKING:
            # The front auto-reveals Cadaver. Keep only the inspected first image;
            # remove extra hint panels, linked metadata and remote resources.
            imgs=re.findall(r'<img[^>]+>',f.get('Cadaver','') or f.get('Illustration','') or f.get('Model','') or f.get('Imaging',''))
            if not imgs: raise ValueError(f'No visual on {nid}')
            f={key:('Identify the highlighted structure' if key=='Header' else imgs[0] if key=='Cadaver' else f[key] if key=='Text' else '') for key in f}
        elif nid in ATLAS:
            for i in range(1,21):
                if f'{i}a' not in ATLAS[nid]:f[f'{i}a']=''
            for field in ('Clinical','Comment'):f[field]=''
        else:
            f={key:(f[key] if key in ('Text','Extra') else '') for key in f}
            f['Extra']='' if nid not in (1482022121968,1461962456152,1461962475986) else f['Extra']
            if nid==1482022121968:
                f['Text']='The <b>distal third</b> of the esophagus is composed of {{c1::smooth}} muscle.'
                f['Extra']='The middle third contains both striated and smooth muscle, as shown in the lecture.'
            if nid==1474511934874:
                f['Text']='The esophagus passes through the diaphragm at {{c1::T10}}.'
            if nid==1527616316221:
                f['Text']='During upper endoscopy, the esophagus narrows at the cricopharyngeus, the {{c1::aortic arch/left bronchus}} crossing, and the {{c2::diaphragmatic hiatus}}.'
                f['Extra']='The lecture groups the aortic and bronchial indentations as one bronchoaortic level.'
        expected=len(ATLAS[nid]) if nid in ATLAS else len(set(re.findall(r'\{\{c(\d+)::',f.get('Text',''))))
        if expected<1:raise ValueError(nid)
        entries.append(dict(source_nid=nid,source_model=model,source_fields_hash=digest(n['fields']),source_deck=n['cards'][0]['deckName'],source_tags=tags,origin=origin,fields=f,expected_cards=expected,selected_fields=ATLAS.get(nid,[]),pink=nid in PINK,high_yield=origin=='AnKing' and HY in tags))
    template=BY[1482022116564]
    authored=[
        ('abdominal-esophagus','After crossing the T10 hiatus, the esophagus briefly continues as its {{c1::abdominal}} part before the cardia.','The other two named parts are cervical and thoracic.<br><img src="paste-29a1e9ef3137a29f750e02f8f35df519.jpg" width="430">'),
        ('posterior-stomach-pancreas','Behind the stomach, the lesser sac separates its posterior wall from the {{c1::pancreas}}.','The reflected-stomach atlas plate makes this surgical relation visible.<br><img src="MSA-Omental_Bursa-Stomach_Reflected21.jpg" width="430">'),
    ]
    # Replace first authored image with the actual first image of the inspected hiatus note.
    hiatus=re.search(r'src="([^"]+)"',BY[1543512875540]['fields']['Cadaver']).group(1)
    authored[0]=(authored[0][0],authored[0][1],authored[0][2].replace('paste-29a1e9ef3137a29f750e02f8f35df519.jpg',hiatus))
    for key,text,extra in authored:
        f={k:'' for k in template['fields']};f['Text']=text;f['Extra']=extra
        entries.append(dict(source_nid=None,key=key,source_model=template['model'],source_fields_hash=None,source_deck=None,source_tags=[],origin='Autoral',fields=f,expected_cards=1,selected_fields=[],pink=False,high_yield=False))
    totals=dict(notes=len(entries),cards=sum(e['expected_cards'] for e in entries),by_origin=dict(Counter({o:sum(e['expected_cards'] for e in entries if e['origin']==o) for o in set(e['origin'] for e in entries)})),pink=sum(e['expected_cards'] for e in entries if e['pink']),green=sum(e['expected_cards'] for e in entries if e['high_yield'] and not e['pink']),shared_notes=1)
    plan=dict(lesson_id=LESSON,target_deck=DECK,profile=INV['profile'],source_folder='https://drive.google.com/drive/folders/1sg4WMtpGzA3LhdZg9M8sXXM0MJkP0llG',source_inventory='inventory.json',shared_note_id=1790247520212,entries=entries,totals=totals)
    (HERE/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(totals,ensure_ascii=False))
if __name__=='__main__':main()
