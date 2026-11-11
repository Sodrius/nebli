"""Corrige seta herdada que caía abaixo do tubérculo na prancha Netter.
Alvo é o término da linha ORIGINAL 'Anterior tubercle': (349,481) na imagem1001x933.
Recorte exclui os nomes impressos; não usa inferência por cor/centroide.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import math
R=Path(__file__).resolve().parent
MEDIA=Path('/Users/davisousa/Library/Application Support/Anki2/User 1/collection.media')
def construir():
 im=Image.open(MEDIA/'u7-netter-anterior-thalamic-tubercle.jpg').convert('RGB').crop((150,300,480,660))
 q=Image.new('RGB',(330,410),'white');q.paste(im,(0,0));d=ImageDraw.Draw(q)
 a=(310,50);b=(199,181);d.line([a,b],fill='white',width=7);d.line([a,b],fill='#d40000',width=4)
 dx,dy=b[0]-a[0],b[1]-a[1];l=math.hypot(dx,dy);ux,uy=dx/l,dy/l
 d.polygon([b,(b[0]-ux*16-uy*7,b[1]-uy*16+ux*7),(b[0]-ux*16+uy*7,b[1]-uy*16-ux*7)],fill='#d40000')
 ans=q.copy();font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',18)
 ImageDraw.Draw(ans).text((10,375),'Tubérculo anterior do tálamo',fill='#005ca8',font=font)
 names=['u7an04-tuberculo-anterior-focal-Q.png','u7an04-tuberculo-anterior-focal-R.png']
 for name,pic in zip(names,[q,ans]):pic.save(R/'img'/name)
 return {'Imagem':f'<img src="{names[0]}">','MascaraP':f'<img src="{names[0]}">','MascaraR':f'<img src="{names[1]}">'},{n:'img/'+n for n in names}
if __name__=='__main__':construir()
