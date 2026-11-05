from pathlib import Path
from PIL import Image,ImageDraw
import fitz,json
C=Path(__file__).parent;I=C/'img';M=Path.home()/'Library/Application Support/Anki2/User 1/collection.media';manifest={}
def crop(name,source,box):
 im=Image.open(source);w,h=im.size;im.crop(tuple(round(z*v)for z,v in zip(box,(w,h,w,h)))).save(I/name);manifest[name]={'fonte':str(source),'recorte_fracao':box}
crop('nebli-0511-gal4-hibrido.png',I/'nebli-0511-gal4full-p28.png',(.51,.33,.97,.90))
crop('nebli-0511-repressor-mascaramento.png',I/'nebli-0511-repressor.png',(.03,.22,.55,.91))
crop('nebli-0511-cas9-reparo.png',I/'nebli-0511-cas9-p16.png',(.375,.385,.802,.785))
crop('nebli-0511-nucleocapsideo.png',M/'mb57-estruturas.jpg',(.12,.57,.43,.95))
crop('nebli-0511-eosinofilo-granulos.png',M/'291b8c70b9c5dfada250869e36f7d937.webp',(.36,.07,.83,.76))
crop('nebli-0511-vias-biliares.png',I/'nebli-0511-an11-p12.png',(.12,.09,.89,.45))
# Comparação completa da aula, ambos estados do operon trp.
p='arquivos-trabalho/deck-aula-uc03-bm54-rnas-nao-codificadores-v2-2026-10-23/fontes/slides.pdf';d=fitz.open(p);pg=d[8];pg.get_pixmap(matrix=fitz.Matrix(2,2)).save(I/'nebli-0511-trp-comparacao.png');manifest['nebli-0511-trp-comparacao.png']={'pdf':p,'pagina':9}
# Quadro original de classificação de micoses da aula, lido e inspecionado.
crop('nebli-0511-subcut-comparacao.png',I/'nebli-0511-mb48-p3.png',(0,0,1,1))
json.dump(manifest,open(C/'fontes-recortes.json','w'),ensure_ascii=False,indent=1)
out=Image.new('RGB',(1600,1600),'#eee');dr=ImageDraw.Draw(out)
for i,n in enumerate(manifest):
 im=Image.open(I/n).convert('RGB');im.thumbnail((790,360));x=i%2*800;y=i//2*400;out.paste(im,(x,y+25));dr.text((x,y),n,fill='black')
out.save(C/'recortes.jpg')
