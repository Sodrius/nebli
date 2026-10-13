from comum import img, mud, salvar, IMG_DIR
IO = str(IMG_DIR.parent / "io")
def ionovo(nid, prefixo, imagem, **k):
    f = {"Image": img(imagem), **{m: f'<img src="{prefixo}-{s}.svg">' for m, s in (("Question Mask", "Q"), ("Answer Mask", "A"), ("Original Mask", "O"))}}
    d = mud(nid, outros=f, **k); d["media"] = [str(IMG_DIR / imagem)] + [f"{IO}/{prefixo}-{s}.svg" for s in "QAO"]; return d
L = [
 ionovo(1790974697004, "nebli-uc08-an02-io-netter-valvula-anal-r4", "io-anal-valve.jpg", corrigido=True, familia="B",
        motivo="'IO estranha': seta amarela na figura até a válvula (ponto da linha-guia do Netter), caixa no início da seta"),
 ionovo(1790974697406, "nebli-uc08-an02-io-netter-esfincter-interno-r4", "io-anal-internal.jpg", familia="B",
        motivo="mesmo padrão do irmão criticado; ponto da linha-guia do Netter"),
 ionovo(1790981524777, "nebli-uc08-an07-io-peca-sigmoideas-r4", "io-sigmoid2.jpg", corrigido=True, familia="B",
        motivo="'seta não aponta certo': ponto = fim da linha-guia 'Sigmoid arteries' do Netter pr. 295"),
 mud(1791023364492, "The deep, microvilli-lined channel that runs <u>inside</u> the <b>parietal cell</b> and receives its H⁺ is the {{c1::<b>intracellular canaliculus</b>}}",
     "- Inward fold of the apical membrane, open to the gland lumen<br>- Its microvilli carry the <b>H⁺/K⁺ ATPase</b><br><br>" + img("par-canal.jpg"),
     media=["par-canal.jpg"], corrigido=True, familia="C,D,E",
     motivo="'não induz a resposta, nem explica bem': frente dá as pistas (canal dentro da célula) e Extra explica o que é"),
 *[mud(n, outros={"Header": "Part of duodenum"}, corrigido=(n == 1790972068360), familia="B", motivo="dica pedida (an01-68), aplicada às partes do duodenum")
   for n in (1790972068159, 1790972068261, 1790972068360, 1790972068462, 1790973218007, 1790973218132, 1790973218257)],
]
salvar("feedback2", L)
