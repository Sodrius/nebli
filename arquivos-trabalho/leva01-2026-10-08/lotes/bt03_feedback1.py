from comum import img, mud, salvar
L = [
 mud(1791023365216, "In the <u>neck</u> of gastric glands, scattered among parietal cells, {{c1::<b>mucous neck</b>}} cells secrete a less alkaline mucus",
     img("st-mucneck.jpg"), media=["st-mucneck.jpg"], corrigido=True, familia="D",
     motivo="'escrita estranha / sem storytelling': frase passa a contar onde estão e o que fazem, cobrando o nome"),
 mud(1791023360217, retirar="redundante", familia="G",
     motivo="'card estranho / não ensina algo': repete o AnKing bt03-75 (fossetas, onde as glândulas desembocam)"),
]
salvar("bt03-feedback1", L)
