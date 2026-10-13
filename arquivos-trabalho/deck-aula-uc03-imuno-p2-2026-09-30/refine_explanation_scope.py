import json,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.explicacoes import open_store
fixes={1790781884793:'''Base: C3 é o ponto em que convergem as três vias do complemento. Sua clivagem fornece C3b para opsonização e para montar C5 convertases.
Por quê: sem C3, microrganismos recebem menos marcação por C3b e são fagocitados com dificuldade, sobretudo os encapsulados. Também ficam comprometidas a geração de C5a, importante quimioatraente, e a montagem do MAC. A falha central explica infecções piogênicas graves e recorrentes e prejuízo à remoção de imunocomplexos.
Na aula: a gravidade se reconstrói pela posição do defeito na cascata, não apenas pelo nome da proteína.
Não confundir: perder C5a não elimina outros quimioatraentes, como IL-8. Defeitos terminais têm como associação clássica Neisseria; C6–C9 não impedem a opsonização por C3b.''',1790781881517:'''Base: a via clássica pode ser direcionada por IgM ou IgG ligados ao antígeno, que permitem ao C1q iniciar a cascata.
Por quê: numa primeira infecção, a produção de anticorpos específicos leva tempo. As vias alternativa e da lectina já podem atuar, pois não dependem dessa produção: usam a amplificação de C3 e o reconhecimento de açúcares microbianos. Conforme surgem IgM e IgG específicos, aumenta a contribuição da via clássica dirigida ao antígeno.
Na aula: o complemento participa da defesa inata imediata e depois também é orientado pela resposta adaptativa.
Não confundir: isso não significa ausência completa da clássica no início. IgM natural e proteína C reativa podem ativá-la antes da resposta específica.'''}
replacements={1790781880444:[('a via clássica é a que depende da imunidade adaptativa (anticorpos)','a ativação clássica por anticorpos específicos conecta o complemento à imunidade adaptativa')],1790781884894:[('O C4, que não participa da via alternativa, fica normal.','O C4, que não participa da via alternativa, pode permanecer normal.'),('C3 baixo com C4 normal indica problema na via alternativa.','C3 baixo com C4 normal sugere consumo pela via alternativa.')],1790781885019:[('os dois ficam baixos no sangue','os dois podem ficar baixos no sangue')],1790781885593:[('que clivam C4 e C2 e forma a C3 convertase','que clivam C4 e C2, permitindo formar a C3 convertase')],1790781913769:[('líquido só sai dos vasos para o tecido se houver espaço entre as células do endotélio.','a abertura de espaços entre células endoteliais é um mecanismo importante de vazamento vascular na inflamação.')],1790781916543:[('a inflamação começa quando o estímulo liga a COX-2 induzível.','o estímulo inflamatório aumenta a expressão da COX-2 induzível, sustentando a produção de mediadores lipídicos.')],1790781920520:[('combate microrganismos de duas formas:','pode combater microrganismos por fagocitose ou por mecanismos extracelulares:')]}
db=open_store();before=[]
for cid in set(fixes)|set(replacements):
 row=db.execute('select * from explicacoes where card_id=?',(cid,)).fetchone();assert row;before.append(row);text=fixes.get(cid,row[4])
 for old,new in replacements.get(cid,[]):
  if old not in text:print('Trecho já diferente, conferir:',cid)
  else:text=text.replace(old,new)
 db.execute('update explicacoes set texto=?,modelo=?,gerado_em=? where card_id=?',(text,'codex-revisao',time.strftime('%Y-%m-%d %H:%M:%S'),cid))
db.commit();(R/'explicacoes-scope-before.json').write_text(json.dumps(before,ensure_ascii=False,indent=1));print('Refinadas',len(before),'explicações')
