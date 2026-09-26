import json,re,sys
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('inventory.json',encoding='utf-8'))
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
def txt(r):
    f=r['fields']; t=f.get('Text') or f.get('Front') or f.get('Header') or next(iter(f.values()))
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)).strip()
def sec(r):
    for t in r['tags']:
        if t.startswith('#AK_Step1_v12::#FirstAid::'): return '::'.join(t.split('::')[3:5])[:40]
    return ''
mode=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else ''
rows=[r for r in d['notes'] if not any(t.startswith('NEBLI') for t in r['tags'])]
if mode=='tag': rows=[r for r in rows if 'tag' in r['why'] and re.search(pat,sec(r))]
elif mode=='term': rows=[r for r in rows if 'tag' not in r['why'] and re.search(pat,' '.join(r['why']))]
elif mode=='nebli': rows=[r for r in d['notes'] if any(t.startswith('NEBLI') for t in r['tags'])]
rows.sort(key=lambda r:(sec(r),r['nid']))
for r in rows: print(r['nid'],'H' if HY in r['tags'] else '-',len(r['cards']),r['model'][:10],sec(r)[-22:],'|',txt(r)[:210])
