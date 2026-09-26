import html,json,re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
p=Path(__file__).parent
plan=json.loads((p/'plan.json').read_text(encoding='utf-8'))
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s or ''))).strip()
for e in plan['entries']:
    print(f"{e['key']} | {e['origin']} | {e['objective']} | {e['expected_cards']}")
    print('  TEXT:',clean(e['fields'].get('Text',''))[:600])
    if e['fields'].get('Extra'): print('  EXTRA:',clean(e['fields']['Extra'])[:500])
