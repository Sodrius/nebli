from pathlib import Path
import fitz,json
r=Path(__file__).parent;d=fitz.open(r/'fontes/slides.pdf');(r/'img').mkdir(exist_ok=True)
# Recortes de figuras reais,sem títulos/legendas de fonte; não altera conteúdo anatômico.
rects={
'neurulacao':(3,(0,.14,.36,.99)),
'vesiculas':(3,(.36,.24,.99,.99)),
'neuronio':(4,(.14,.01,.94,.54)),
'glia':(6,(.06,.02,.60,.60)),
'sinapse':(7,(.59,.46,.94,.99)),
'mielina':(8,(.44,.02,.96,.64)),
'fibras':(9,(.33,.02,.995,.98)),
'morfologias':(10,(.02,.105,.66,.84)),
'divisoes':(11,(.165,.025,.61,.57)),
'funcional':(11,(.16,.56,.61,.98)),
'raizes':(12,(.45,.61,.94,.98)),
'encefalo':(13,(.37,.445,.83,.98)),
'cinzenta':(14,(.14,.40,.62,.96)),
'medula':(14,(.48,.02,.83,.39)),
'nucleos':(15,(.13,.09,.88,.99)),
'cortes':(16,(.41,.03,.96,.88)),
'niveis':(17,(.34,.02,.75,.98)),
'somatotopia':(18,(.66,.14,.91,.96)),
'lesao':(19,(.08,.26,.95,.98)),
'broca':(20,(.06,.20,.46,.65)),
'tracadores':(21,(.01,.37,.99,.96)),
'imagem':(22,(.02,.25,.995,.91)),
'redes':(23,(.03,.12,.94,.99)),
'funcional-imagem':(24,(.08,.12,.89,.99))}
out={}
for name,(page,box) in rects.items():
 p=d[page-1];a=p.rect;rect=fitz.Rect(box[0]*a.width,box[1]*a.height,box[2]*a.width,box[3]*a.height)
 filename='nebli-u7an01-'+name+'.png';p.get_pixmap(matrix=fitz.Matrix(2,2),clip=rect).save(str(r/'img'/filename))
 out[name]=dict(arquivo=filename,slide=page,rect=list(rect),descricao='Figura real recortada da lâmina%d,para comentário explicativo.'%page)
(r/'figuras-preparadas.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(len(out),'figuras reais')
