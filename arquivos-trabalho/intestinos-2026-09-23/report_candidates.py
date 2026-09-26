import json,re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
notes=json.loads((Path(__file__).parent/'inventory.json').read_text(encoding='utf-8'))['notes']
for n in notes:
    if n['model'].startswith('Cloze-AnKingMaster') and (1701979000000<n['nid']<1701982000000 or 1702220000000<n['nid']<1702235000000):
        f=n['fields']; t=f.get('Text') or next(iter(f.values()),'')
        t=re.sub(r'<[^>]+>',' ',t);t=re.sub(r'\s+',' ',t)
        cl=sorted({int(x) for x in re.findall(r'{{c(\d+)::',t)})
        print(n['nid'],cl,t[:300])
