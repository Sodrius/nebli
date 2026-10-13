"""masks.py out.png img1 img2 ... — renderiza cada nota IOE com a máscara de pergunta e o nid (somente leitura)."""
import sys,re,base64,fitz; sys.path.insert(0,'/Users/davisousa/NEBLI')
from nebli.decks import Anki; A=Anki()
tiles=[]
for img in sys.argv[2:]:
    nids=A('findNotes',query=f'"Image:*{img}*"'); raw=A('retrieveMediaFile',filename=img)
    if not raw: print('SEM IMAGEM',img); continue
    base=fitz.Pixmap(base64.b64decode(raw))
    for nid in nids:
        n=A('notesInfo',notes=[nid])[0]; q=re.findall(r'src="([^"]+)"',n['fields']['Question Mask']['value'])[0]
        sv=A("retrieveMediaFile",filename=q)
        if not sv: print("SEM MASCARA",nid,q); continue
        page=fitz.open(stream=base64.b64decode(sv),filetype="svg")[0]
        sx=base.width/page.rect.width; pm=page.get_pixmap(matrix=fitz.Matrix(sx,sx),alpha=True)
        out=fitz.open(); p=out.new_page(width=base.width,height=base.height); p.insert_image(p.rect,pixmap=base); p.insert_image(p.rect,pixmap=pm)
        p.insert_text((10,50),str(nid),fontsize=44,color=(1,0,0)); fn=f'visual/m_{nid}.png'; p.get_pixmap(dpi=40).save(fn); tiles.append(fn)
cols=5; W=2500; cw=W/cols; ch=cw*0.75; rows=(len(tiles)+cols-1)//cols
d=fitz.open(); pg=d.new_page(width=W,height=rows*ch)
for i,f in enumerate(tiles): pg.insert_image(fitz.Rect((i%cols)*cw,(i//cols)*ch,(i%cols+1)*cw-4,(i//cols+1)*ch-4),filename=f)
pg.get_pixmap(dpi=50).save(sys.argv[1]); print(len(tiles))
