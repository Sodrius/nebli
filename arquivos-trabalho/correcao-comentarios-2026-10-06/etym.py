"""Frentes independentes para comparações; reaproveita equivalentes existentes."""
from prepare import *
DATA='''
1784300090872|Reunir elementos de uma palavra para construir seu sentido é {{c1::composição}}.
1784310292193|Na Terminologia Anatômica, o adjetivo {{c1::especifica}} a estrutura nomeada pelo substantivo.
1784310292201|Em braquial, braqui/o indica {{c1::braço}}.
1784308067563|Em hipercalemia, cali/o indica {{c1::potássio}}.
1784308068081|Em queratose, querat/o indica {{c1::queratina}}.
1784308070382|Em pediatria, pedi- indica {{c1::criança}}.
1784308070810|Em espermatogênese, espermat/o remete ao {{c1::espermatozoide}}.
1784308070902|Em cérvice uterina, cervic/o indica {{c1::colo do útero}}.
1784308073152|Em hiperidrose, hidr/o indica {{c1::suor}}.
1784308054308|Em poliomielite, poli/o indica {{c1::cinzento}}.
1784300090895|-ectomia indica {{c1::remoção cirúrgica}}.|-stomia indica criação de uma {{c1::abertura}}.
1784300090903|-pexia indica {{c1::fixação cirúrgica}}.|-rafia indica {{c1::sutura}}.
1784300090910|-grama indica o {{c1::registro}} produzido.|-grafo indica o {{c1::instrumento}} que registra.
1784300090918|-metro indica o {{c1::instrumento}} usado para medir.
1784300090926|-scópio indica o {{c1::instrumento}} usado para visualizar.
1784300090935|A biópsia obtém uma amostra de {{c1::tecido}} para exame.|A aspiração retira {{c1::conteúdo}} por sucção.
1784300090944|Em odinofagia, -odinia/odino- indica {{c1::dor}}.
1784300090952|-citose indica {{c1::aumento}} do número de células.
1784300090958|-estenose indica {{c1::estreitamento}}.
1784300090964|-rragia indica {{c1::sangramento intenso}}.
1784300090972|-plegia indica {{c1::paralisia}}.
1784300090979|-úria situa algo na {{c1::urina}}.
1784300090986|-capnia refere-se ao {{c1::dióxido de carbono}}.
1784300090994|Hipertrofia é aumento do {{c1::tamanho}} das células.
1784300091000|-poiese enfatiza {{c1::produção}}.
1784300091007|ad- indica {{c1::aproximação}}.
1784300091013|Em exocitose, exo- indica movimento para {{c1::fora}}.
1784300091021|peri- indica {{c1::ao redor}}.|Em paratireoide, para- indica {{c1::adjacência}}.
1784300091385|Em mielopatia, miel/o indica {{c1::medula espinal}}.
1784300091390|Em pseudocisto, cist/o indica {{c1::cisto}}.
1784300091396|Em termômetro, -metro indica {{c1::instrumento de medição}}.
1784300091415|Em vasectomia, vas/o indica {{c1::ducto deferente}}.
1784308057100|Em pneumotórax, pneum/o indica {{c1::ar}}.
1784308057142|Cerebr/o refere-se ao {{c1::cérebro}}.
1784308073397|Uma via eferente conduz para {{c1::fora}} da estrutura de referência.
1784308073403|Hipoxemia é redução do oxigênio no {{c1::sangue}} arterial.
1784308073411|Anestesia é perda de {{c1::sensibilidade}}.
1784308073419|Anúria é ausência ou produção quase nula de {{c1::urina}}.
1784308073426|Albuminúria é a presença de {{c1::albumina}} na urina.
1784308073454|Sepse é disfunção orgânica ameaçadora à vida causada por resposta desregulada a uma {{c1::infecção}}.
1784308054393|Perinatal refere-se ao período {{c1::ao redor}} do nascimento.|Pós-natal refere-se ao período {{c1::depois}} do nascimento.
1784308054432|Adsorção prende uma substância à {{c1::superfície}} de outra.
1784308054477|Exocitose libera material para {{c1::fora}} da célula.
1784308054487|Pinocitose incorpora {{c1::líquido}} extracelular em vesículas.
1784308054518|Repolarização {{c1::restaura}} a polaridade da membrana após despolarização.|Hiperpolarização torna o interior celular mais {{c1::negativo}} em relação ao repouso.
1784308054537|Desfosforilação {{c1::remove}} um grupo fosfato.
1784308054548|Descarboxilação remove um grupo carboxila na forma de {{c1::CO₂}}.
1784308054558|Desaminação {{c1::remove}} um grupo amino.
1784308054568|Gliconeogênese forma {{c1::glicose}} de precursores não glicídicos.
1784308054579|Glicogenólise degrada {{c1::glicogênio}}.
1784308054590|Lipólise {{c1::degrada}} lipídios.
1784308054598|Cetólise {{c1::utiliza}} corpos cetônicos para obter energia.
1784308054691|Atresia é ausência ou fechamento de uma {{c1::abertura}} normal.
1784308056848|Odinofagia é {{c1::dor}} ao engolir.
1784308056919|Platipneia é falta de ar que piora na posição {{c1::ereta}}.
1784308056951|Hiposmia é {{c1::redução}} do olfato.|Hiperosmia é {{c1::aumento}} da sensibilidade olfatória.
1784308056970|Hemoptise elimina sangue pela {{c1::tosse}}.
1784641082712|No músculo esquelético, o perimísio envolve cada {{c1::fascículo}}.|No músculo esquelético, o epimísio envolve o {{c1::músculo inteiro}}.
1784641082713|No nervo periférico, o perineuro envolve cada {{c1::fascículo}}.|No nervo periférico, o epineuro envolve o {{c1::nervo inteiro}}.
1784641082714|O miocárdio forma a camada {{c1::muscular}} do coração.|O epicárdio recobre a superfície {{c1::externa}} do coração.
1784641082715|O periósteo recobre a superfície {{c1::externa}} do osso.
1784641082716|O osteócito {{c1::mantém}} a matriz óssea.|O osteoclasto {{c1::reabsorve}} osso.
1784641082717|A célula madura da cartilagem é o {{c1::condrócito}}.
1784641082718|Eosinófilo tem afinidade pelo corante {{c1::eosina}}.|Acidófilo tem afinidade por corantes {{c1::ácidos}}.
1784641082719|Em sarcolema, sarc/o indica {{c1::músculo}}.|Em axolema, ax/o indica {{c1::axônio}}.
1784641082720|Em fagolisossomo, lis/o indica {{c1::dissolver}}.|Em fagolisossomo, som/o indica {{c1::corpo}}.
1784641082721|A sinalização parácrina atua sobre células {{c1::próximas}}.|A sinalização endócrina chega a alvos distantes pelo {{c1::sangue}}.|A secreção exócrina é liberada sobre uma superfície {{c1::epitelial}}.
1784641082722|Em homeostase, homeo- indica {{c1::semelhante}}.
1784641082723|Hipoplasia é desenvolvimento {{c1::insuficiente}} de um tecido ou órgão.|Hiperplasia aumenta o {{c1::número}} de células.
1784300091193|Em dacriocistite, cist/o indica {{c1::saco}}.|Em dacriocistite, -ite indica {{c1::inflamação}}.
1784300091207|Hemotórax é acúmulo de {{c1::sangue}} na cavidade pleural.|Quilotórax é acúmulo de {{c1::quilo}} na cavidade pleural.|Piotórax é acúmulo de {{c1::pus}} na cavidade pleural.
1784300091224|Ureterolitíase é cálculo no {{c1::ureter}}.|Coledocolitíase é cálculo no {{c1::colédoco}}.
1784300091238|Em miringotomia, -tomia indica {{c1::incisão}}.
1784300091245|Em estapedectomia, -ectomia indica {{c1::remoção cirúrgica}}.
1784300091260|Em onicomicose, mic/o indica {{c1::fungo}}.|Em onicomicose, -ose indica {{c1::condição}}.
1784300091268|Em xantocromia, crom/o indica {{c1::cor}}.
1784308073506|Em oligomenorreia, men/o indica {{c1::menstruação}}.|Em oligomenorreia, -rreia indica {{c1::fluxo}}.
1784308073607|Em glomerulonefrite, nefr/o indica {{c1::rim}}.|Em glomerulonefrite, -ite indica {{c1::inflamação}}.
1784308075766|Colecistite é inflamação da {{c1::vesícula biliar}}.
1784308075784|Hepatomegalia é aumento do {{c1::fígado}}.|Cardiomegalia é aumento do {{c1::coração}}.
1784308076138|Em amniocentese, -centese indica {{c1::punção}}.
1784308076144|Em artrodese, -dese indica {{c1::fusão cirúrgica}}.
1784308076156|Em gastropexia, -pexia indica {{c1::fixação cirúrgica}}.
1784308076164|Em herniorrafia, -rafia indica {{c1::sutura}}.
1784308076193|Em eletrocardiograma, cardi/o indica {{c1::coração}}.|Em eletrocardiograma, -grama indica {{c1::registro}} produzido.
1784308076211|Em radiculopatia, -patia indica {{c1::doença}}.
1784300091372|Insipidus significa {{c1::sem sabor}}.
'''
# For targets already covered separately, use the existing note (no new history).
REUSE={
'-ectomia':1784308062281,'-stomia':1784308062341,'-pexia':1784308062311,'-rafia':1784308062325,
'-grama':1784308062292,'-metro':1784308062306,'-citose':1784308059865,'-estenose':1784308059905,
'-rragia':1784308060081,'-plegia':1784308060041,'-úria':1784308062173,'-capnia':1784308060020,
'-poiese':1784308062387,'ad-':1784308057165,'exo-':1784308057313,'peri-':1784308057397,
'para-':1784308057390,'pneum/o':1784308065122,'-tomia':1784308062348,'-ite':1784308059958,
'mic/o':1784308073308,'crom/o':1784308062466,'-rreia':1784308060072,'nefr/o':1784300091425,
'-centese':1784308062264,'-dese':1784308062276,'cardi/o':1784308062705,'-patia':1784308060026,
'homeo-':1784308059724,'Gliconeogênese':1784308075908,'Glicogenólise':1784308075897,
}
FIRST={
1784308073397:'Uma via aferente conduz em direção à estrutura de {{c1::referência}}.',
1784308073403:'Hipóxia é falta de oxigênio nos {{c1::tecidos}}.',
1784308073411:'Analgesia é ausência de {{c1::dor}}.',
1784308073419:'Oligúria é produção {{c1::reduzida}} de urina.',
1784308073426:'Proteinúria é a presença de {{c1::proteína}} na urina.',
1784308073454:'Bacteremia é presença de {{c1::bactérias}} no sangue.',
1784641082712:'No músculo esquelético, o endomísio envolve cada {{c1::fibra}} muscular.',
1784641082713:'No nervo periférico, o endoneuro envolve cada {{c1::fibra}} nervosa.',
1784641082714:'O endocárdio reveste a superfície {{c1::interna}} do coração.',
1784641082715:'O endósteo reveste as superfícies {{c1::internas}} do osso.',
1784641082716:'O osteoblasto {{c1::produz}} matriz óssea.',
1784641082717:'O condroblasto {{c1::produz}} matriz cartilaginosa.',
1784641082720:'Em fagolisossomo, fag/o indica {{c1::ingerir}}.',
1784641082721:'A sinalização autócrina atua na célula que {{c1::secretou}} o sinal.',
1784641082723:'Aplasia é {{c1::falha}} de formação de um tecido ou órgão.',
1784300091193:'Em dacriocistite, dacri/o indica {{c1::lágrima}}.',
1784300091207:'Pneumotórax é acúmulo de {{c1::ar}} na cavidade pleural.',
1784300091238:'Em miringotomia, miring/o indica {{c1::membrana timpânica}}.',
1784300091245:'Em estapedectomia, estaped/o indica {{c1::estribo}}.',
1784300091260:'Em onicomicose, onic/o indica {{c1::unha}}.',
1784300091268:'Em xantocromia, xant/o indica {{c1::amarelo}}.',
1784308073506:'Em oligomenorreia, oligo- indica {{c1::poucos}}.',
1784308073607:'Em glomerulonefrite, glomerul/o indica {{c1::glomérulo}}.',
1784308076138:'Em amniocentese, amni/o indica {{c1::âmnio}}.',
1784308076144:'Em artrodese, artr/o indica {{c1::articulação}}.',
1784308076156:'Em gastropexia, gastr/o indica {{c1::estômago}}.',
1784308076164:'Em herniorrafia, herni/o indica {{c1::hérnia}}.',
1784308076193:'Em eletrocardiograma, eletr/o indica {{c1::eletricidade}}.',
1784308076211:'Em radiculopatia, radicul/o indica {{c1::raiz nervosa}}.',
1784641082719:'Em sarcolema e axolema, -lema indica {{c1::envoltório membranoso}}.',
}
new=[]; coverage=[]
for line in DATA.strip().splitlines():
    parts=line.split('|'); nid=int(parts[0]); old=value(nid,'Text')
    first=FIRST.get(nid,clean(old).split(';')[0].strip().rstrip('.')+'.')
    context=re.sub(r'\{\{c\d+::(.*?)(?:::[^}]*)?\}\}',r'<b>\1</b>',old)
    extra=value(nid,'Extra')+'<br><br>'+context
    put(nid,'Uma recuperação por card; comparação completa fica no verso',Text=first,Extra=extra)
    for j,front in enumerate(parts[1:],1):
        reused=next((v for k,v in REUSE.items() if re.search(r'(?<![\w/-])'+re.escape(k)+r'(?![\w/-])',front)),None)
        if reused:
            coverage.append({'parent':nid,'target':front,'existing':reused}); continue
        new.append({'parent':nid,'key':f'NEBLI::feedback-split::20261006-{nid}-{j}','Text':front,'Extra':extra})
        coverage.append({'parent':nid,'target':front,'new_key':new[-1]['key']})
(P/'new-notes.json').write_text(json.dumps(new,ensure_ascii=False,indent=2))
(P/'split-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
finish()
print('Novas notas',len(new),'alvos reaproveitados',len(coverage)-len(new))
