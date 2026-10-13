import json,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.explicacoes import open_store
fixes={
1790781880918:'''Base: a via alternativa vigia o plasma continuamente, sem esperar anticorpos. O C3 sofre hidrólise espontânea lenta, formando C3(H2O).
Por quê: C3(H2O) liga fator B; fator D cliva B e produz uma convertase em fase fluida. Ela cliva outras moléculas de C3 e gera C3b. Quando C3b se deposita numa superfície microbiana, liga B, que é clivado por D, formando C3bBb. Essa convertase amplifica a deposição de C3b. Reguladores do hospedeiro limitam a cascata nas células próprias.
Na aula: explica por que essa via pode agir imediatamente, antes da resposta adaptativa.
Não confundir: a hidrólise inicial gera C3(H2O), não C3b. O C3b surge da clivagem enzimática subsequente.''',
1790781881018:'''Base: as três vias do complemento diferem no ponto de partida. A alternativa começa no C3 e não depende de C1, C4, C2 ou anticorpos.
Por quê: parte do C3 sofre hidrólise espontânea e vira C3(H2O). Com fatores B e D, forma-se uma convertase solúvel que cliva mais C3. O C3b produzido pode depositar-se em microrganismos e montar C3bBb na superfície. Isso amplia a cascata sem esperar a produção de anticorpos específicos.
Na aula: o C3 é tanto o início da via alternativa quanto o ponto de convergência das três vias.
Não confundir: C1 inicia a via clássica; C3 inicia a alternativa. Hidrólise de C3 e geração de C3b por clivagem são etapas diferentes.''',
1790781881968:'''Base: uma C3 convertase é uma enzima que cliva C3 e gera C3a, inflamatório, e C3b, opsonizante. Na via alternativa, a convertase de superfície é C3bBb.
Por quê: o C3b depositado no microrganismo liga fator B. Fator D cliva o B ligado; Bb permanece associado ao C3b. Esse complexo cliva mais C3, ampliando a marcação da superfície. A properdina estabiliza a enzima e prolonga sua ação.
Na aula: a fórmula mostra como a mesma cascata usa o produto C3b para montar uma enzima que produz ainda mais C3b.
Não confundir: a hidrólise inicial gera C3(H2O), que monta uma convertase fluida; ela não gera C3b diretamente. C3bBb é a convertase da superfície.''',
1790781884893:'''Base: a via alternativa amplifica C3b por meio da convertase C3bBb. Fator H acelera sua desmontagem e ajuda fator I a inativar C3b.
Por quê: em deficiências graves desses reguladores, a amplificação perde o freio e consome C3 continuamente. A concentração sérica de C3 pode cair, comprometendo a opsonização. Como C4 não participa dessa via, pode permanecer normal apesar do consumo de C3.
Na aula: o padrão de exame se reconstrói identificando qual etapa perdeu regulação e quais proteínas ela consome.
Não confundir: C3 baixo com C4 preservado sugere consumo pela via alternativa, mas não identifica sozinho a proteína defeituosa. No déficit de C1-INH, a alteração habitual envolve C4 baixo.''',
1790781885018:'''Base: C4 participa das vias clássica e da lectina; C3 é usado pelas três vias. Por isso, suas concentrações ajudam a localizar o consumo de complemento.
Por quê: imunocomplexos ativam C1 e a sequência C4/C2, consumindo C4 e depois C3. Na amplificação pela via alternativa, forma-se C3bBb sem utilizar C4. Assim, C3 baixo com C4 preservado sugere consumo pela alternativa; queda de ambos pode acompanhar ativação clássica por imunocomplexos.
Na aula: usa a organização das vias para interpretar um resultado laboratorial, em vez de decorar números isolados.
Não confundir: o padrão orienta a investigação, não prova uma deficiência específica. A hidrólise espontânea inicial de C3 também é diferente da clivagem pela convertase.'''
}
db=open_store();before=[]
for cid,text in fixes.items():
 row=db.execute('select * from explicacoes where card_id=?',(cid,)).fetchone();assert row;before.append(row)
 db.execute('update explicacoes set texto=?,modelo=?,gerado_em=? where card_id=?',(text,'codex-revisao',time.strftime('%Y-%m-%d %H:%M:%S'),cid))
for cid in [1790781884119,1790781885593]:
 row=db.execute('select * from explicacoes where card_id=?',(cid,)).fetchone();assert row;before.append(row);text=row[4].replace('Llig a com:','Liga com:').replace('Isso ativa o complexo C1-like, que cliva C4 e C2','Isso ativa as proteases MASP associadas à MBL, que clivam C4 e C2')
 db.execute('update explicacoes set texto=?,modelo=? where card_id=?',(text,'codex-revisao',cid))
db.commit();(R/'explicacoes-tickover-before.json').write_text(json.dumps(before,ensure_ascii=False,indent=1));print('Refinadas',len(before),'explicações')
