"""Identificações do Machado para alvos sem IO Kenhub no acervo consultado.
Máscara cobre somente o rótulo impresso, mantendo a linha-guia original do atlas.
Coordenadas foram lidas nas figuras 7.5/7.6/7.7/22.1, não inferidas pelo slug.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
R=Path(__file__).resolve().parent
# unidade, chave, nome, página PDF, retângulo do rótulo na prévia 1.3x, recorte focal
ALVOS=[
(30,'io-parte-opercular','Parte opercular do giro frontal inferior',70,(110,204,295,230),(100,178,605,435)),
(30,'io-parte-orbital','Parte orbital do giro frontal inferior',70,(123,375,223,405),(110,280,550,455)),
(25,'io-sulco-semilunar','Sulco semilunar (lunatus)',70,(884,306,978,331),(660,235,990,440)),
(36,'io-rostro-corpo-caloso','Rostro do corpo caloso','66-rot',(97,291,211,316),(85,215,535,445)),
(28,'io-sulco-precentral','Sulco pré-central',70,(398,32,486,58),(280,0,650,430)),
(34,'io-sulco-temporal-inferior','Sulco temporal inferior',70,(117,504,242,531),(95,295,660,552)),
(35,'io-giros-curtos-insula','Giros curtos da ínsula',71,(71,157,187,182),(55,115,465,365)),
(35,'io-giro-longo-insula','Giro longo da ínsula',71,(109,435,233,465),(105,195,475,470)),
(35,'io-sulco-central-insula','Sulco central da ínsula',71,(64,268,140,307),(52,180,450,355)),
(37,'io-sulco-cingulo','Sulco do cíngulo',73,(83,82,172,107),(70,65,660,380)),
(39,'io-sulco-parietoccipital','Sulco parietoccipital',73,(845,262,975,290),(470,130,983,440)),
(41,'io-sulco-hipocampo','Sulco do hipocampo',73,(589,590,715,617),(310,310,735,625)),
(16,'io-nucleo-arqueado','Núcleo arqueado',218,(318,523,375,557),(135,175,555,565)),
]
def construir():
    cards=[]; media={}
    for u,key,nome,pdf,rect,crop in ALVOS:
        im=Image.open(R/'visual'/f'machado-pdf{pdf}.png').convert('RGB')
        q=im.copy();draw=ImageDraw.Draw(q);draw.rectangle(rect,fill='#ffb4b4',outline='#a00000',width=2)
        q=q.crop(crop);a=im.crop(crop)
        # Mesma geometria nas duas faces; nome legível sem depender do rótulo miúdo do scan.
        def painel(pic, resposta=False):
            out=Image.new('RGB',(pic.width,pic.height+52),'white');out.paste(pic,(0,0))
            if resposta:
                size=28
                while True:
                    font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',size)
                    if ImageDraw.Draw(out).textbbox((0,0),nome,font=font)[2]<pic.width-12 or size<=17: break
                    size-=1
                ImageDraw.Draw(out).text((6,pic.height+10),nome,font=font,fill='#005ca8')
            return out
        q=painel(q);a=painel(a,True)
        qname=f'u7an04-{key}-Q.png';aname=f'u7an04-{key}-R.png'
        q.save(R/'img'/qname);a.save(R/'img'/aname)
        media.update({qname:'img/'+qname,aname:'img/'+aname})
        cards.append({'u':u,'key':key,'nome':nome,'pagina':pdf,
          'fields':{'Nome PT':nome,'Imagem':f'<img src="{qname}">','MascaraP':f'<img src="{qname}">','MascaraR':f'<img src="{aname}">','ID (hidden)':f'nebli-uc07-an04-machado-{key}' }})
    return cards,media
if __name__=='__main__':
    cards,media=construir();print(len(cards),'identificações focais; conferir máscaras antes de incluir')
