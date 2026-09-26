import json,re,sys,urllib.request
sys.stdout.reconfigure(encoding='utf-8')
out={}
for vid in sys.argv[1:]:
    req=urllib.request.Request(f'https://www.youtube.com/watch?v={vid}&hl=en',headers={'User-Agent':'Mozilla/5.0','Accept-Language':'en'})
    h=urllib.request.urlopen(req,timeout=60).read().decode('utf-8','replace')
    m=re.search(r'"shortDescription":("(?:[^"\\]|\\.)*")',h)
    desc=json.loads(m.group(1)) if m else ''
    ln=re.search(r'"lengthSeconds":"(\d+)"',h)
    chapters=[l.strip() for l in desc.split('\n') if re.match(r'^\s*\(?\d{1,2}:\d{2}',l)]
    out[vid]={'minutes':int(ln.group(1))//60 if ln else None,'chapters':chapters}
    print('==',vid,out[vid]['minutes'],'min')
    for c in chapters: print('  ',c[:110])
json.dump(out,open('yt-chapters.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
