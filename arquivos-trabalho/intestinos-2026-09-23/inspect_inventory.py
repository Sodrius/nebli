import json,re,sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
p=Path(__file__).parent
notes=json.loads((p/'inventory.json').read_text(encoding='utf-8'))['notes']
terms=['villi','villus','microvilli','brush border','plicae','crypts of lieberkuhn','enterocyte','goblet cell','paneth','enteroendocrine','transit amplifying','brunner','peyer','ki67','tunel','villin','lactase','muscularis mucosae','myenteric plexus']
for term in terms:
    selected=[n for n in notes if term in n['queries']]
    print('\n##',term,len(selected))
    for n in selected[:45]:
        f=n['fields']; front=f.get('Text') or f.get('Front') or next(iter(f.values()),'')
        front=re.sub(r'<[^>]*>',' ',front); front=re.sub(r'\s+',' ',front)
        print(n['nid'],n['model'][:18],front[:220])
