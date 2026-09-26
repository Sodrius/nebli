# X11 Correlação patológica-radiológica 2 (UC03, conteúdo 19, Patologia/Radiologia). Assumido pelo Claude (Codex sem tokens).
# Aula de caso: caso 1 hemangioma cavernoso (US/TC trifásica/macro/micro); caso 2 etilista (esteatose -> cirrose -> hipertensão portal,
# colestase, CHC); fígado normal, sistema porta e anastomoses. Fontes: E1 antiga (legendas das 17 lâminas usadas) + MAPA_CONTEUDO.
# Slide original indisponível nesta sessão (conector do Drive ausente, extensão do Chrome desconectada): imagens dos autorais vêm de cards AnKing.
# rosa = da aula, sem valor a longo prazo.
SEL={  # AnKing Step 1
 # fígado normal: lóbulo, tríade, sinusoide, Disse, estrelada, zonas
 1486775502282:('N-arquitetura',0,[]), 1486776235726:('N-arquitetura',0,[]), 1486776242882:('N-arquitetura',0,[]),
 1486776254440:('N-arquitetura',0,[]), 1486776257809:('N-arquitetura',0,[]), 1486776339459:('N-arquitetura',0,[]),
 1486776347708:('C-fibrose',0,[('resub','Extra',r'^Hypervitaminosis A \(excess vitamin A\) may lead to liver enlargement \(hepatomegaly\)<br><br>','')]), 1486776358379:('C-fibrose',0,[]), 1486522654540:('C-fibrose',0,[]),
 1486776364876:('N-zonas',0,[]), 1486776370260:('N-zonas',1,[]), 1486776374938:('N-zonas',0,[]), 1486776390497:('N-zonas',0,[]),
 1580917307640:('E-esteatose',0,[]),
 # caso 1: hemangioma
 1486591267339:('H-hemangioma',0,[]), 1525564242390:('H-hemangioma',0,[('resub','Extra',r'<div>- In the <b>brain</b>, may cause neurologic deficits and seizures</div><br><div>- Express <b>CD31/PECAM1</b></div><br>','<br>'),('resub','Extra',r'<div><div> Cavernous hemangioma in the soleus muscle:.*$','')]), 1580585590157:('H-hemangioma',0,[]),
 1486591272185:('H-hemangioma',0,[]), 1580590159680:('H-hemangioma',1,[]), 1496111041884:('H-hemangioma',0,[]),
 # caso 2: álcool, esteatose, cirrose
 1486522786197:('E-esteatose',0,[]), 1486522804267:('E-esteatose',0,[('resub','Extra',r'^- vs\. Reye syndrome, which presents with <u>microvesicular</u> fatty change<br><br>','')]),
 1486522811003:('E-esteatose',0,[]),
 1486522637384:('C-cirrose',0,[]),
 # hipertensão portal
 1486522667060:('P-hipertensao',0,[]), 1486522673379:('P-hipertensao',0,[]), 1486522681611:('P-hipertensao',0,[]),
 1486522690115:('P-baco',0,[]), 1567467129106:('P-baco',0,[]), 1486591413282:('P-baco',0,[]),
 1486522684741:('P-anastomoses',0,[]), 1486770898373:('P-anastomoses',0,[]), 1486771285047:('P-anastomoses',0,[]),
 1486771299461:('P-anastomoses',0,[]), 1521156441953:('P-anastomoses',1,[('resub','Extra',r' Purchase full access <a href="https://physeo\.com/#sign-up">here</a>\.','')]), 1521156796178:('P-anastomoses',1,[('resub','Extra',r' Purchase full access <a href="https://physeo\.com/#sign-up">here</a>\.','')]),
 1482203751576:('P-varizes',0,[]), 1482203769705:('P-varizes',0,[('resub','Extra',r'^Important distinguishing feature from <u>Mallory-Weiss syndrome</u> which typically has <b>painful</b> hematemesis<br><br>','')]), 1482203779331:('P-varizes',0,[]),
 # CHC
 1486591276598:('T-chc',0,[('resub','Extra',r'^<div>Presents with jaundice, tender hepatomegaly, ascites, polycythemia, and anorexia </div><br>','')]), 1486591287399:('T-chc',0,[]),
}
OTHER={  # outros acervos: Lightyear (anestesia) cobre dupla irrigação e os quatro sítios colaterais
 1610567782318:('N-irrigacao',0,[]), 1611946820385:('P-anastomoses',0,[]),
}
MCAT={}
# notas NEBLI já existentes (X1 Vascularização, Codex): mesma pergunta -> associar por tag
ASSOCIATE={1790247520609:'N-irrigacao', 1790247521015:'P-anastomoses'}
