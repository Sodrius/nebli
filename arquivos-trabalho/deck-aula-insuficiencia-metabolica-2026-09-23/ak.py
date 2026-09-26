import json,sys,urllib.request,re
def call(action, **params):
    body=json.dumps({'action':action,'version':6,'params':params}).encode()
    req=urllib.request.Request('http://127.0.0.1:8765',body,{'Content-Type':'application/json'})
    with urllib.request.urlopen(req, timeout=300) as f: data=json.load(f)
    if data['error']: raise RuntimeError(f'{action}: {data["error"]}')
    return data['result']
def strip(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s.replace('&nbsp;',' '))).strip()
