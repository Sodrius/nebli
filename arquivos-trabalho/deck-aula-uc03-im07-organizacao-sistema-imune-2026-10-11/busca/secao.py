import json,urllib.request,re,html,sys
def call(a,**p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765",json.dumps({"action":a,"version":6,"params":p}).encode())))["result"]
def clean(s): return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",s or ""))).strip()
tags=sys.argv[1:]
seen={}
for t in tags:
    ns=call("findNotes",query=f'"deck:Referências::Anking Step Deck*" "tag:{t}"')
    for n in call("notesInfo",notes=ns): seen[n['noteId']]=n
# live check
for nid,n in sorted(seen.items()):
    f=n['fields']; fr=clean(next((f[k]['value'] for k in ('Text','Front','Header') if k in f and f[k]['value'].strip()),next(iter(f.values()))['value']))
    hy=[x.split('::')[-1][:1] for x in n['tags'] if 'Low/HighYield' in x]
    live=call("findNotes",query=f'"tag:NEBLI::source::nid-{nid}"')
    L=''
    if live:
        ln=call("notesInfo",notes=live)[0]; L=' LIVE '+','.join(re.sub(r'NEBLI::2026-uc\d+-','',x.replace('NEBLI::','')) for x in ln['tags'] if re.match(r'NEBLI::20\d\d-',x))
    img='[img]' if '<img' in str(f) else ''
    print(nid,hy[0] if hy else '-',img,fr[:200],L)
