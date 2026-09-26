# Integração metabólica II: estados alimentares (UC03, conteúdo 33, Bioquímica).
# Fonte do recorte: slide de 49 lâminas (o arquivo "transcrição" é o slide), E1 antiga e 8 questões de prova.
# rosa = da aula, sem valor a longo prazo.
SEL={
 # hormônios e visão geral
 1462128178981:('H-insulina',0,[]), 1462809460228:('H-insulina',0,[]), 1462809734046:('H-glucagon',0,[]),
 1462131701878:('H-glucagon',0,[]), 1462131799037:('H-glucagon',0,[]), 1461857273344:('H-glucagon',0,[]),
 1462131726115:('H-glucagon',0,[('set','Extra','')]), 1462123239655:('H-insulina',0,[('set','Extra','A liberação de insulina acompanha a glicemia (proporcional até ~300 mg/dL).')]), 1462131783153:('H-insulina',0,[]),
 1462061167732:('H-cortisol',0,[]),
 # célula beta (lâmina 6)
 1462127745460:('B-secrecao',0,[]), 1462127759504:('B-secrecao',0,[]), 1462127805913:('B-secrecao',0,[('resub','Extra',r'<br><div>- Certain patients.*?</div><br><div>- Conversely.*?</div>','')]),
 1462127846011:('B-secrecao',0,[]), 1462127869624:('B-secrecao',0,[]),
 # estado alimentado: fígado retém glicose
 1474164741147:('A-glicoquinase',0,[]), 1474164674426:('A-glicoquinase',0,[]), 1474164693118:('A-glicoquinase',1,[]),
 1474164720011:('A-glicoquinase',1,[]), 1474164748214:('A-glicoquinase',0,[]), 1474164751245:('A-glicoquinase',0,[]),
 1462809621604:('A-glicoquinase',0,[]),
 # glicogênio
 1462128205014:('A-glicogenio',0,[]), 1462845596752:('A-glicogenio',0,[]), 1462849092193:('A-glicogenio',1,[]),
 1474253648328:('A-glicogenio',0,[]), 1474253651773:('A-glicogenio',0,[]),
 1474253707546:('A-glicogenio',0,[]), 1474253702427:('A-glicogenio',0,[]),
 1472435698856:('A-glicogenio',0,[]), 1472435688940:('A-glicogenio',0,[]), 1472435681635:('A-glicogenio',1,[]),
 # glicólise × gliconeogênese: PFK-2 / F2,6BP
 1474164553998:('A-glicolise',0,[]), 1474253986881:('P-gliconeo',0,[]), 1474164853411:('A-glicolise',0,[]),
 1474164784750:('A-glicolise',0,[]), 1474164845352:('A-glicolise',1,[]), 1474164831303:('P-gliconeo',0,[]),
 1462128231420:('A-glicolise',0,[]), 1462131823875:('P-gliconeo',0,[]), 1474209244126:('A-glicolise',1,[]),
 1474253975760:('P-gliconeo',1,[]),
 # lipogênese no alimentado
 1475896519521:('A-lipogenese',0,[]), 1475896543773:('A-lipogenese',1,[]), 1475896526687:('A-lipogenese',0,[]),
 1475894369854:('A-lipogenese',0,[]), 1475896559049:('A-lipogenese',0,[]), 1475896509771:('A-lipogenese',0,[]),
 1475896504605:('A-lipogenese',1,[]), 1475982778100:('A-lipogenese',0,[]), 1475896514243:('A-lipogenese',1,[]),
 1475966787801:('A-lipogenese',0,[]), 1462128277353:('A-proteinas',0,[]),
 # tecido adiposo e músculo: GLUT4, HSL
 1462128186045:('A-glut4',0,[]), 1462809498251:('P-tecidos',0,[]), 1462809636467:('P-tecidos',0,[]),
 1462849100249:('A-adiposo',0,[]), 1475982732554:('P-lipolise',0,[]), 1475982737323:('P-lipolise',0,[]),
 1475982741557:('P-lipolise',0,[]), 1462131831506:('P-lipolise',0,[]), 1462131849821:('P-lipolise',0,[]),
 # jejum: glicogenólise → gliconeogênese → corpos cetônicos
 1476502557231:('P-fases',0,[]), 1476502582683:('P-fases',0,[]), 1476502641042:('P-fases',0,[]),
 1476502637223:('P-fases',0,[]), 1476502674112:('P-fases',0,[]), 1476502678906:('P-fases',0,[]),
 1476502551897:('P-fases',0,[]), 1462131802276:('P-gliconeo',0,[]),
 1474253934255:('P-gliconeo',0,[]), 1474253956755:('P-gliconeo',1,[]), 1474253912958:('P-gliconeo',0,[]),
 1474253990056:('P-gliconeo',0,[]), 1475982746310:('P-gliconeo',0,[]), 1474253997005:('P-gliconeo',0,[]),
 1475982771690:('P-lipolise',0,[]), 1475982812947:('P-cetonicos',0,[]),
 1476241277886:('P-aminoacidos',0,[]), 1502927648775:('P-aminoacidos',0,[]), 1476241344675:('P-aminoacidos',0,[]),
 1476154069517:('P-cetonicos',0,[]), 1476154095169:('P-cetonicos',0,[]), 1476154085131:('P-cetonicos',1,[]),
 1476154090457:('P-cetonicos',0,[]), 1476154190117:('P-cetonicos',0,[]), 1476154185261:('P-cetonicos',0,[]),
 1476502591395:('P-cetonicos',0,[]), 1462128264089:('P-cetonicos',0,[]),
 # diabetes (lâminas 39-47)
 1462326105448:('D-tipos',0,[]), 1462326951145:('D-tipos',0,[]), 1462327127564:('D-tipos',0,[]),
 1462326961450:('D-dm1',0,[('uncloze',[3])]), 1487983956917:('D-dm1',1,[]), 1516202686282:('D-dm1',0,[]),
 1462327073683:('D-dm1',0,[('append','Extra','Na aula: o DM1 se parece com um jejum exagerado, com cetoacidose e balanço nitrogenado negativo.')]),
 1474164969397:('D-dm1',0,[]),
 1462327211125:('D-dm1',0,[]), 1462128449086:('D-dm1',0,[]), 1462327320519:('D-dm1',0,[]), 1552217717357:('D-dm1',0,[]),
 1462327133002:('D-dm2',0,[]), 1462327053167:('D-dm2',0,[]), 1584135730369:('D-dm2',0,[]),
 1462327389480:('D-dm2',0,[]), 1462327461738:('D-dm2',0,[]),
 1462327481691:('D-glicacao',0,[]), 1462327641370:('D-glicacao',0,[]),
}
MCAT={
 1560089607774:('H-estados',0,[]), 1560090694699:('H-estados',0,[]), 1556917253663:('P-gliconeo',0,[]),
}
ASSOCIATE={}
