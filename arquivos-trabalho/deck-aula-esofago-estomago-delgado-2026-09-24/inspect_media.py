import json,re
from pathlib import Path
from PIL import Image,ImageDraw,ImageOps
from inventory import call,OUT

I=json.loads((OUT/'inventory.json').read_text(encoding='utf-8'))
ids=[1542146925579,1548047359393,1548957822372,1543512875540,1542146936648,1542146962028,1542146968329,1542146981325,1542146989512,1542147001992,1542147006993,1542147011020,1542147017558,1548959124455,1562607277712,1542147025458,1542147032139,1546960965736,1542147052236,1542147060583,1542147086703,1542147154111,1542147164351,1542147117997,1542147170288,1542147178958,1542147185761,1546961446430,1542147594239,1562607411862,1562608101719]
by={x['nid']:x for x in I['notes']}; media=Path(call('getMediaDirPath'))
rows=[]
for nid in ids:
    n=by[nid]
    images=re.findall(r'<img[^>]+src="([^"]+)"',' '.join(n['fields'].get(f,'') for f in ('Cadaver','Model','Illustration','Imaging','Extra')))
    missing=[x for x in images if not (media/x).is_file()]
    rows.append(dict(nid=nid,text=n['fields']['Text'],images=images,missing=missing))
(OUT/'media-audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
thumbs=[]
for row in rows:
    if not row['images']: continue
    first=media/row['images'][0]
    if not first.exists():continue
    try:
        im=Image.open(first).convert('RGB'); im.thumbnail((260,180))
        box=Image.new('RGB',(280,225),'white'); box.paste(im,((280-im.width)//2,0))
        ImageDraw.Draw(box).text((6,185),f"{row['nid']} {re.sub('<[^>]+>','',row['text'])[:28]}",fill='black')
        thumbs.append(box)
    except Exception: pass
width=4*280; height=((len(thumbs)+3)//4)*225
sheet=Image.new('RGB',(width,height),'white')
for j,im in enumerate(thumbs):sheet.paste(im,((j%4)*280,(j//4)*225))
sheet.save(OUT/'contact-sheet.jpg',quality=85)
print(json.dumps(dict(selected=len(rows),images=sum(len(r['images']) for r in rows),missing=sum(len(r['missing']) for r in rows),contact=str(OUT/'contact-sheet.jpg')),ensure_ascii=False))
