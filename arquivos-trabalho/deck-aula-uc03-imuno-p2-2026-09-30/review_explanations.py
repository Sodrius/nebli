"""Correções editoriais de explicações, somente no cache externo ao Anki."""
import sys,json,time
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.explicacoes import open_store,item,STYLE,style_version
from nebli.decks import Anki
fixes={
1790781881643:'''Base: o complemento é uma cascata plasmática que marca microrganismos, gera sinais inflamatórios e pode formar poros em suas membranas.
Por quê: superfícies bacterianas contendo LPS favorecem a ativação e amplificação do complemento. A C3 convertase produz C3a e C3b; a etapa seguinte gera C5 convertase, que libera C5a e C5b. C3a e C5a promovem respostas inflamatórias; C5a é o potente sinal quimiotático que recruta neutrófilos.
Na aula: conecta o reconhecimento do microrganismo aos efetores que trazem fagócitos e facilitam sua ação.
Não confundir: C3a não tem o mesmo papel de quimiotaxia direta de neutrófilos que C5a. C3b opsoniza; C5b inicia a montagem do MAC.''',
1790781881644:'''Base: ativar complemento não serve apenas para lisar bactérias: também produz fragmentos solúveis que avisam as células da defesa.
Por quê: o LPS bacteriano favorece a ativação do complemento. As convertases clivam C3 e C5, liberando C3a e C5a. Esses sinais ativam respostas inflamatórias e favorecem alterações vasculares; C5a também recruta e ativa neutrófilos. Assim, o microrganismo dispara uma resposta que traz células e proteínas de defesa ao tecido.
Na aula: é a ligação entre a superfície bacteriana, a cascata proteolítica e a inflamação local.
Não confundir: C3a/C5a são sinais solúveis; C3b marca o alvo para fagocitose e C5b inicia o MAC. Não atribua a C3a a mesma quimiotaxia neutrofílica direta de C5a.''',
1790781882668:'''Base: anafilatoxinas são fragmentos solúveis do complemento que sinalizam para células inflamatórias. C3a e C5a têm esse papel estabelecido.
Por quê: ao clivar C3 e C5, a cascata libera C3a e C5a. Sua ligação a receptores celulares favorece ativação e liberação de mediadores, incluindo histamina por mastócitos. A histamina altera o fluxo e a permeabilidade vascular; C5a também recruta e ativa neutrófilos.
Na aula: explica como uma cascata plasmática comunica o reconhecimento do microrganismo às células do tecido. A lista docente tradicional inclui C4a, cuja atividade como anafilatoxina tem evidência limitada.
Não confundir: C3b opsoniza e C5b inicia o MAC. Não atribua a todos os fragmentos “a” os mesmos receptores ou efeitos.'''
}
db=open_store();A=Anki();before=[]
for cid,text in fixes.items():
 row=db.execute('select * from explicacoes where card_id=?',(cid,)).fetchone();assert row is not None;before.append(row)
 card=A('cardsInfo',cards=[cid])[0];_,digest,nid=item(A,card)
 db.execute('insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)',(cid,nid,digest,'ok',text,None,style_version(STYLE.read_text()),'codex-revisao',time.strftime('%Y-%m-%d %H:%M:%S')))
db.commit();(R/'explicacoes-correcao-before.json').write_text(json.dumps(before,ensure_ascii=False,indent=1));print('Corrigidas',len(fixes),'explicações; hashes atuais')
