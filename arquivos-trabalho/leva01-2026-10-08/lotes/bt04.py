from comum import img, mud, salvar
L = [
 mud(1791023302118, retirar="outra-aula", familia="G", motivo="'mais de anato': haustros cobertos na AN02 (an02-09/12/16)"),
 mud(1791023296668, corrigido=True, familia="C", motivo="cloze já encurtado em 05/10 e validado agora; dessuspender"),
 mud(1790980910230, corrigido=True, familia="C", motivo="cloze 'surface area' já curto; correção de 05/10 validada; dessuspender"),
 mud(1790980916154, "This H&amp;E mucosa belongs to the {{c1::<b>small intestine</b>}}<br>" + img("bt4-jejunum.jpg"),
     "- Tall <b>villi</b> above the crypts (colon: crypts only, no villi)", media=["bt4-jejunum.jpg"], corrigido=True, familia="A,B",
     motivo="duas imagens e texto demais; figura colada não aparecia no AnkiDroid → uma lâmina HG do jejuno, Extra de 1 linha"),
 mud(1790980912277, None, None, media=["bt4-paneth.jpg"], corrigido=True, familia="A",
     outros={"Image": img("bt4-paneth.jpg"), "Remarks": "<b>Paneth cells</b><br>Granules hold <b>lysozyme</b> and <b>defensins</b>"},
     motivo="imagem ruim para identificação → lâmina HG do íleo com seta nos grânulos vermelhos"),
 mud(1791023299366, retirar="sem-ganho", familia="G",
     motivo="'não aprendo nada, só decoro': cor dos grânulos já é cobrada no card de identificação (bt04-24) e a função no bt04-47"),
 mud(1791023299492, "By secreting <b>lysozyme</b> and <b>defensins</b>, Paneth cells provide {{c1::<b>innate</b>}} immunity in the crypt",
     "- Protects the neighboring <b>stem cells</b><br><br>" + img("bt4-paneth.jpg"), media=["bt4-paneth.jpg"], familia="A",
     motivo="mesma figura fraca de Paneth (família)"),
 mud(1790980916280, "The colon has no Paneth cells, so its crypt-base stem cells are supported by {{c1::<b>deep crypt secretory</b>}} cells",
     "- Same niche role as <b>Paneth</b> cells in the small intestine", corrigido=True, familia="C,D,E",
     motivo="'não compreendi o que o card quer lembrar': frase conta o porquê; Extra sem nota de pesquisa"),
 mud(1790980909978, corrigido=True, familia="B", motivo="pedido de cloze só 'duodeno' já atendido (pergunta + resposta Duodenum); validado"),
]
salvar("bt04", L)
