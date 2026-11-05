from pathlib import Path
import fitz,json
R=Path(__file__).parent;out=R/'img';out.mkdir(exist_ok=True)
S={
'bm46':Path('arquivos-trabalho/deck-aula-uc03-bm46-eucariotos-i-v2-2026-10-23/fontes/slides.pdf'),
'bm52':Path('arquivos-trabalho/deck-aula-uc03-bm52-eucariotos-ii-2026-10-10/fontes/slides.pdf'),
'bm54':Path('arquivos-trabalho/deck-aula-uc03-bm54-rnas-nao-codificadores-v2-2026-10-23/fontes/slides.pdf'),
'mb50':Path('arquivos-trabalho/deck-aula-uc03-mb50-micoses-sistemicas-v2-2026-10-16/fontes/slides.pdf'),
'fi05':Path('arquivos-trabalho/deck-aula-uc08-fi05-digestao-absorcao-2026-10-03/fontes/slides.pdf'),
'rd56':Path('arquivos-trabalho/deck-aula-uc03-rd56-contrastes-v3-2026-11-04/fontes/slides.pdf')}
pages={'bm46':[17,21,28,36,38],'bm52':[29,45,52],'bm54':[7,9,25,27,29,76],'mb50':[32,117,141,143],'rd56':[6,9,10]}
for k in ('fi05',):
 d=fitz.open(S[k]);pages[k]=[i+1 for i,p in enumerate(d) if any(w in p.get_text().lower() for w in ('ferritina','ferro','gastrina','secretina','colecisto'))][:6]
manifest={}
for k,nums in pages.items():
 d=fitz.open(S[k])
 for num in nums:
  p=d[num-1];ims=sorted(p.get_image_info(xrefs=True),key=lambda im:fitz.Rect(im['bbox']).width*fitz.Rect(im['bbox']).height,reverse=True)
  if not ims:continue
  im=ims[0];rect=fitz.Rect(im['bbox'])&p.rect
  if rect.is_empty:continue
  name='nebli-0511-'+k+'-p'+str(num)+'.png';p.get_pixmap(matrix=fitz.Matrix(2,2),clip=rect).save(out/name)
  manifest[name]={'pdf':str(S[k]),'pagina':num,'bbox':list(rect),'origem':'figura real extraída da maior imagem incorporada,não esquema novo; requer inspeção'}
(R/'fontes-figuras.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));print(len(manifest),'figuras candidatas')
