import collections,html,json,re,sys
from pathlib import Path
from ak import call,strip
from prepare import ROOT
sys.stdout.reconfigure(encoding='utf-8')
plan=json.loads((ROOT/'plan.json').read_text(encoding='utf-8'))
receipt=json.loads((ROOT/'receipt.json').read_text(encoding='utf-8'))
ids=[r['new_nid'] for r in receipt['results']]
notes=[]
for s in range(0,len(ids),200): notes+=call('notesInfo',notes=ids[s:s+200])
cids=[c for n in notes for c in n['cards']]
cards=[]
for s in range(0,len(cids),200): cards+=call('cardsInfo',cards=cids[s:s+200])
errors=[]
exp={r['new_nid']:r for r in receipt['results']}
if len(notes)!=plan['totals']['notes'] or len(cards)!=plan['totals']['cards']: errors.append('Contagem viva difere')
for c in cards:
    r=exp[c['note']]
    if c['deckName']!=r['deck']: errors.append(f'Deck errado {c["cardId"]}')
    if c['queue']==-1: errors.append(f'Suspenso {c["cardId"]}')
    if c['flags']!=r['flag']: errors.append(f'Flag {c["cardId"]} {c["flags"]}!={r["flag"]}')
    q,a=c.get('question',''),c.get('answer','')
    TAGDIV=re.compile(r'<div id="tags-container">.*?</div>',re.S)
    q,a=TAGDIV.sub('',q),TAGDIV.sub('',a)
    SCRIPT=re.compile(r'<(script|style)[^>]*>.*?</(?:script|style)>',re.S|re.I)
    _unused=re.compile(r'<(script|style)[^>]*>.*?</>',re.S|re.I)
    q,a=SCRIPT.sub('',q),SCRIPT.sub('',a)
    if '{{c' in q+a: errors.append(f'Cloze não renderizado {c["cardId"]}')
    if '[...]' not in q and 'cloze' not in q: errors.append(f'Pergunta sem lacuna {c["cardId"]}')
    for w in ('Faculdade:','High yield:','Low yield:','NEBLI::','youtube.com','youtu.be'):
        if w in strip(q+a): errors.append(f'Meta/vídeo visível {c["cardId"]} {w}')
media=set()
for n in notes:
    for f in n['fields'].values():
        media.update(html.unescape(x) for x in re.findall(r'<img[^>]+src=["\x27]([^"\x27]+)',f['value'],re.I) if not x.startswith(('http:','https:','data:')))
missing=sorted(x for x in media if not (Path(plan['profile_evidence'])/x).exists())
if missing: errors.append({'midia_ausente':missing})
by_deck=collections.Counter(c['deckName'].split('::')[-1] for c in cards)
by_flag=collections.Counter(c['flags'] for c in cards)
sample={}
for key in ('authored-pkc-dag','authored-age-rage'):
    nid=next(r['new_nid'] for r in receipt['results'] if r['key']==key)
    sample[key]=[strip(c['answer'])[-400:] for c in cards if c['note']==nid]
out={'status':'passed' if not errors else 'failed','notes':len(notes),'cards':len(cards),'by_deck':by_deck,'flags':by_flag,'media_required':len(media),'errors':errors[:50],'authored_answers':sample}
(ROOT/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=1,default=dict),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=1,default=dict))
if errors: raise SystemExit(1)
