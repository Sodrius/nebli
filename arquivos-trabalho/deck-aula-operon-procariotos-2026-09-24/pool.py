import json,re,sys
from collections import defaultdict
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
DECKS={'AK':'"deck:Referências::Anking Step Deck"','MCAT':'"deck:Referências::Referências Externas::AnKing-MCAT"'}
TERMS=['operon','lac operon','lacI','lacZ','lacY','lacA','allolactose','IPTG','X-gal','beta-galactosidase','β-galactosidase','galactoside permease','repressor','co-repressor','corepressor','inducer','inducible','operator','CAP','catabolite','cAMP receptor','polycistronic','Shine','ribosome binding','sigma factor','σ','-10','Pribnow','TATAAT','TTGACA','-35','promoter','trp operon','tryptophan operon','attenuation','Jacob','Monod','helix-turn-helix','helix-loop-helix','cis-acting','trans-acting','merodiploid','constitutive','gene expression','transcription factor','enhancer','silencer','RNA polymerase','diauxic','allosteric','palindrom','prokaryot']
hits=defaultdict(set)
for d,q in DECKS.items():
    for t in TERMS:
        ids=call('findNotes',query=f'{q} "{t}"')
        print(d,t,len(ids))
        if len(ids)>250: continue
        for nid in ids: hits[nid].add((d,t))
ids=sorted(hits); rows=[]
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
for s in range(0,len(ids),300):
    for n in call('notesInfo',notes=ids[s:s+300]):
        f={k:v['value'] for k,v in n['fields'].items()}
        if 'Text' not in f: continue
        d=sorted(hits[n['noteId']])[0][0]
        rows.append({'nid':n['noteId'],'d':d,'hy':HY in n['tags'],'clozes':sorted({int(x) for x in re.findall(r'{{c(\d+)::',f['Text'])}),'text':strip(f['Text']),'extra':strip(f.get('Extra',''))[:200],'t':sorted(t for _,t in hits[n['noteId']])})
(ROOT/'pool.json').write_text(json.dumps(rows,ensure_ascii=False),encoding='utf-8')
with open(ROOT/'pool-lines.txt','w',encoding='utf-8') as o:
    for r in sorted(rows,key=lambda r:(r['d'],r['text'])):
        o.write(f"{r['nid']} {r['d']} {'H' if r['hy'] else '.'}{len(r['clozes'])} {r['text'][:200]}  [{','.join(r['t'][:3])}]\n")
print(len(rows))
