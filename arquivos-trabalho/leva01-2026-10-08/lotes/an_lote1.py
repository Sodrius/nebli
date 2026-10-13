from comum import img, mud, salvar, IMG_DIR
IO = str(IMG_DIR.parent / "io")
def masks(prefix_new, q_only=False):
    import shutil, os
    out = []
    for s in (("Q",) if q_only else ("Q", "A", "O")):
        src = f"{IO}/{prefix_new}-{s}.svg" if not q_only else f"{IO}/{prefix_new}"
        out.append(src)
    return out
def ioq(nid, qfile, **k):
    return mud(nid, media=[], outros={"Question Mask": f'<img src="{qfile}">'}, **k) | {"media": [f"{IO}/{qfile}"]}
def ionovo(nid, prefixo, imagem, **k):
    f = {"Image": img(imagem), **{m: f'<img src="{prefixo}-{s}.svg">' for m, s in (("Question Mask", "Q"), ("Answer Mask", "A"), ("Original Mask", "O"))}}
    d = mud(nid, outros=f, **k); d["media"] = [str(IMG_DIR / imagem)] + [f"{IO}/{prefixo}-{s}.svg" for s in "QAO"]; return d
L = [
 # constrições do esôfago: seta da caixa até o número no desenho
 ioq(1790973210184, "nebli-uc08-an01-io-constricao-cervical-Q-r3.svg", corrigido=True, familia="B", motivo="seta antiga apontava para a caixa; agora liga a caixa ao n.º 1"),
 ioq(1790973210308, "nebli-uc08-an01-io-constricao-broncoaortica-Q-r3.svg", corrigido=True, familia="B", motivo="'seta para o local errado': agora aponta o n.º 2"),
 ioq(1791003000000 if False else 1790973210308, "nebli-uc08-an01-io-constricao-broncoaortica-Q-r3.svg") if False else None,
 # dicas curtas na frente (Header) para oclusão de resposta ambígua
 mud(1790973218382, outros={"Header": "Part of duodenum + vertebral level"}, corrigido=True, familia="B",
     motivo="dica pedida 'duas ou três palavras' sobre o que responder"),
 mud(1790981524526, outros={"Header": "Artery"}, familia="B", motivo="dica pedida: 'vaso'"),
 # celíaco e esplênica: seta até a estrutura
 ioq(1790981514202, "nebli-uc08-an07-io-esplenica-Q-r3.svg", corrigido=True, familia="B", motivo="'cloze não tem seta apontando'"),
 ioq(1790981514326, "nebli-uc08-an07-io-hepatica-comum-Q-r3.svg", corrigido=True, familia="B", motivo="mesma família do slide"),
 ioq(1790981514702, "nebli-uc08-an07-io-gastrica-direita-Q-r3.svg", familia="B", motivo="irmão do mesmo slide sem linha-guia"),
 ioq(1790981515925, "nebli-uc08-an07-io-pd-postero-superior-Q-r3.svg", corrigido=True, familia="B", motivo="'não há indicação da estrutura'"),
 ionovo(1790981524777, "nebli-uc08-an07-io-peca-sigmoideas-r3", "io-sigmoid.jpg", corrigido=True, familia="A,B",
        motivo="peça escura e ilegível → Netter pr. 295 limpo, seta nas sigmoides"),
 ionovo(1790974697004, "nebli-uc08-an02-io-netter-valvula-anal-r3", "io-anal.jpg", corrigido=True, familia="A,B",
        motivo="prancha inteira com dezenas de caixas → recorte limpo do canal anal, só a pergunta"),
 ionovo(1790974697406, "nebli-uc08-an02-io-netter-esfincter-interno-r3", "io-anal.jpg", corrigido=True, familia="A,B",
        motivo="excesso de informação/imagem pequena → recorte limpo"),
 # texto: imagem focal, Extra antes da imagem, tamanho que cabe na tela
 mud(1790972067861, None, "- Also the <b>diaphragm</b> and anterior abdominal wall<br><br>" + img("an-stomach-ant.jpg"), media=["an-stomach-ant.jpg"],
     corrigido=True, familia="J,A", motivo="imagem grande demais (rolar): Netter recortado com seta no lobo esquerdo"),
 mud(1790972067961, "The <b>posterior</b> surface of the <b>stomach</b> forms most of the anterior wall of the {{c1::<b>omental bursa</b>}}",
     "- Also called the <b>lesser sac</b>, a space behind the stomach<br><br>" + img("an-bursa.jpg"), media=["an-bursa.jpg"], corrigido=True,
     familia="A,E", motivo="imagem estranha: corte transversal com seta na bolsa omental, logo atrás do estômago"),
 mud(1790972068062, None, "- Runs along the upper border of the <b>pancreas</b>, in the stomach bed<br><br>" + img("an-splenic.jpg"), media=["an-splenic.jpg"],
     corrigido=True, familia="A", motivo="'imagem não explica': Netter com seta na artéria esplênica"),
 mud(1790972069412, None, "- Jaundice plus <b>gallstone pancreatitis</b><br><br>" + img("an-ampulla.jpg"), media=["an-ampulla.jpg"], corrigido=True,
     familia="A,E", motivo="imagem genérica e texto abaixo da imagem: Netter focal com seta na ampola; texto antes"),
 mud(1790972069711, None, "- <b>Skeletal</b> muscle from the right crus plus <b>smooth</b> muscle from the duodenum<br><br>" + img("an-treitz.jpg"),
     media=["an-treitz.jpg"], corrigido=True, familia="A", motivo="imagem ruim (CORRIGIDO 05/10 revalidado): Netter com seta no músculo suspensor"),
 mud(1790972070612, None, "- Ileum: many short arcades, short vasa recta<br><br>" + img("jej-ile.jpg"), media=["jej-ile.jpg"], corrigido=True,
     familia="A", motivo="'poderia ter imagem': esquema jejuno × íleo"),
 mud(1790972070958, None, "- Also taller plicae and redder color<br>- Ileum: thinner, paler, more mesenteric fat", corrigido=True,
     familia="A,E", motivo="imagem com muita informação; Extra com ; e :"),
 mud(1790973222856, ordem="an01-104", familia="H", motivo="vasos retos curtos logo após os longos (an01-103)"),
 mud(1790972070863, ordem="an01-105", familia="H", motivo="desloca 1 posição"),
 mud(1790972070958, ordem="an01-106", familia="H", motivo="desloca 1 posição") if False else None,
 mud(1790972071061, ordem="an01-107", familia="H", motivo="desloca 1 posição"),
 mud(1790972071160, ordem="an01-108", familia="H", motivo="desloca 1 posição"),
 mud(1790974689756, retirar="outra-aula", familia="G", motivo="Davi: não veio desta aula; cronograma tem aula própria"),
 mud(1790974691958, "Behind the apex of the <b>sigmoid mesocolon</b>, on the left common iliac vessels, lies the {{c1::<b>left ureter</b>}}",
     "- Surgical landmark when mobilizing the sigmoid colon<br><br>" + img("nebli-moore-fig-6-31.png"), corrigido=True, familia="D,J",
     motivo="escrita estranha + imagem grande: frase direta e imagem limitada à tela"),
 mud(1790978724448, None, "- <b>Rectovaginal septum</b> between them<br>- <b>Rectouterine pouch</b> (of Douglas) above<br><br>" + img("an-female.jpg"),
     media=["an-female.jpg"], corrigido=True, familia="A", motivo="card sobre mulher com imagem masculina → corte sagital feminino com setas"),
 mud(1790978739486, None, "- <b>Puborectalis</b> sling makes the anorectal angle here<br><br>" + img("an-anorectal.jpg"), media=["an-anorectal.jpg"],
     corrigido=True, familia="A", motivo="'imagem com mt info': recorte limpo do canal anal com seta"),
 mud(1790981519924, "From the <i>lymph</i>, <b>chylomicrons</b> reach the blood through the {{c1::<b>thoracic duct</b>}}",
     "- Drains at the junction of the left <b>subclavian</b> and <b>internal jugular</b> veins", corrigido=True, familia="C",
     motivo="cloze no termo fácil (blood) → no ducto torácico, como Davi sugeriu"),
 mud(1790981522079, "The {{c1::<b>ileocolic</b>::SMA branch}} artery supplies the terminal ileum, the cecum and, through its appendicular branch, the appendix",
     None, corrigido=True, familia="C", motivo="dica pedida: 'branch of the SMA'"),
 mud(1790981526502, None, "- Superior rectal: <b>IMA</b><br>- Middle rectal: <b>internal iliac</b><br>- Inferior rectal: <b>internal pudendal</b><br><br>" + img("an-midrectal.jpg"),
     media=["an-midrectal.jpg"], corrigido=True, familia="A,E", motivo="imagem com muita info; Extra com ; : ,"),
 mud(1790981526625, None, "- Supplies the anal canal <u>below</u> the pectinate line<br><br>" + img("an-infrectal.jpg"), media=["an-infrectal.jpg"],
     corrigido=True, familia="A", motivo="'imagem nada a ver': Netter com seta na retal inferior"),
]
salvar("an-lote1", [x for x in L if x])
