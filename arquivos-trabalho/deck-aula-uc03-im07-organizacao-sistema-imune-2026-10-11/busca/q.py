import json,urllib.request,re,html,sys
def call(a,**p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765",json.dumps({"action":a,"version":6,"params":p}).encode())))["result"]
def clean(s): return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",s or ""))).strip()
deck=sys.argv[1]  # ak|ext
D={"ak":'"deck:Referências::Anking Step Deck*"',"ext":'"deck:Referências::Referências Externas*"'}[deck]
mx=int(sys.argv[2])
for q in sys.argv[3:]:
    ns=call("findNotes",query=f'{D} ({q})')
    print("###",q,len(ns))
    for n in call("notesInfo",notes=ns[:mx]):
        nid=n['noteId'];f=n['fields']
        fr=clean(next((f[k]['value'] for k in ('Text','Front','Header','Remarks','Title') if k in f and f[k]['value'].strip()),next(iter(f.values()))['value']))
        hy=[x.split('::')[-1][:1] for x in n['tags'] if 'Low/HighYield' in x]
        live=call("findNotes",query=f'"tag:NEBLI::source::nid-{nid}"')
        L=''
        if live:
            ln=call("notesInfo",notes=live)[0]; L=' LIVE '+','.join(re.sub(r'NEBLI::2026-uc\d+-','',x.replace('NEBLI::','')) for x in ln['tags'] if re.match(r'NEBLI::20\d\d-',x))
        print(nid,n['modelName'][:6],hy[0] if hy else '-','[img]' if '<img' in str(f) else '',fr[:190],L)
