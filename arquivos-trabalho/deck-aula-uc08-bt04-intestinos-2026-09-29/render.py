"""render.py key1 key2 ... — renderiza frente/verso (1º card) das notas indicadas em render/ e monta pranchas R*.png."""
import sys,json,subprocess,glob,os,fitz; sys.path.insert(0,'/Users/davisousa/NEBLI')
from nebli.decks import Anki; A=Anki()
media=A('getMediaDirPath'); rec=json.load(open('receipt.json')); keys=sys.argv[1:]
os.makedirs('render/ql',exist_ok=True); [os.remove(f) for f in glob.glob('render/ql/*')+glob.glob('render/*.html')]
fix='<style>#io-original{visibility:visible !important}</style>'; files=[]
for r in rec['notes']:
    if r['key'] not in keys: continue
    c=A('cardsInfo',cards=[int(x) for x in r['cards']])[0]
    for side in ('question','answer'):
        fn=f"render/{r['key']}-{side[0]}.html"; open(fn,'w').write(f'<html><head><base href="file://{media}/"><meta charset="utf-8"><style>{c.get("css","")}</style>{fix}</head><body class="card" style="width:900px">{c[side]}</body></html>'); files.append(fn)
subprocess.run(['qlmanage','-t','-s','900','-o','render/ql']+files,capture_output=True)
fs=sorted(glob.glob('render/ql/*.png')); cols=4; W=2000; cw=W/cols; ch=cw
for k in range(0,len(fs),12):
    sel=fs[k:k+12]; rows=(len(sel)+cols-1)//cols; d=fitz.open(); p=d.new_page(width=W,height=rows*ch)
    for i,f in enumerate(sel):
        p.insert_image(fitz.Rect((i%cols)*cw+2,(i//cols)*ch+16,(i%cols+1)*cw-2,(i//cols+1)*ch-2),filename=f)
        p.insert_text(((i%cols)*cw+4,(i//cols)*ch+13),f.split('/')[-1].replace('.html.png',''),fontsize=12,color=(1,0,0))
    p.get_pixmap(dpi=70).save(f'render/R{k//12+1}.png')
print(len(fs))
