from comum import img, mud, salvar
GAS = "088d1869ef3e541e74f413ba4928a07c.png"  # AnKing: regulação da secreção gástrica (ACh, gastrina, histamina)
L = [
 mud(1790972067662, None, "- Inner oblique, middle circular, outer longitudinal<br><br>" + img("st-oblique.jpg"), media=["st-oblique.jpg"],
     familia="A", motivo="recorte CSS → Netter com seta (mesma imagem do irmão da BT03)"),
 mud(1791023256746, None, "- Vagal <b>ACh</b> acts on parietal M3 receptors and also drives G and ECL cells<br><br>" + img(GAS),
     familia="A", motivo="desenho das células da glândula não mostra estímulo; figura AnKing da regulação"),
 mud(1791023256867, None, "- <b>ECL → histamine</b>: local (paracrine), H₂ receptors<br>- <b>G cells → gastrin</b>: through the blood<br><br>" + img(GAS),
     familia="A,E", motivo="idem"),
 mud(1790972070612, "The {{c1::<b>jejunum</b>}} has <u>few, large</u> arterial arcades and <u>long</u> vasa recta", None, familia="D", motivo="sem negrito"),
 mud(1790972070863, "The {{c1::<b>ileum</b>}} has <u>more mesenteric fat</u> than the jejunum",
     "- Fat reaches the bowel wall and hides the vessels", familia="A,D", motivo="sem negrito; figura do Moore em português genérica retirada"),
 mud(1790980910230, "{{c1::<b>Villi</b>}} are small finger-like projections that increase the intestinal {{c2::<b>surface area</b>}}",
     "- <b>Capillaries</b> absorb water-soluble nutrients<br>- <b>Lacteal</b> absorbs fat into lymph<br><br>" + img("50c5a616a8bf0f52dfaeb2f05ef163b9-8f58ff0f5178bf77595cd5b5ed9fa05af3afa26d.png"),
     familia="D,E", motivo="negrito; Extra limpo em bullets"),
 mud(1790980914230, "<b>Villi</b> plus submucosal <b>Brunner glands</b> identify this H&amp;E section as {{c1::<b>duodenum</b>}}<br>" + img("bt4-duodeno.jpg"),
     "- Brunner glands secrete alkaline mucus against gastric acid", media=["bt4-duodeno.jpg"], familia="A,D,E",
     motivo="negrito; lâmina HG nítida; Extra de anotações soltas reescrito"),
 mud(1790980914355, "The <b>villi</b> and <b>plicae</b> in this H&amp;E section identify the {{c1::<b>small intestine</b>}}<br><img src=\"paste-3d75c628a54f5825cea895dd00967de1fd6489e7.png\" style=\"max-width:100%;max-height:52vh\">",
     "- Plica = fold of mucosa + submucosa<br>- Villi = mucosa only", familia="D,E", motivo="negrito; Extra 'Middle pink = plica' reescrito"),
 mud(1790980916029, "<u>Straight crypts</u>, abundant goblet cells and <u>no villi</u> identify this H&amp;E section as {{c1::<b>colon</b>}}<br>" + img("bt4-colon.jpg"),
     None, media=["bt4-colon.jpg"], familia="A,D", motivo="recorte por span (quebra no AnkiDroid) → lâmina HG do cólon"),
]
salvar("familias1", L)
