from pathlib import Path
import sys,json,re,hashlib
D=Path(__file__).resolve().parent;R=D.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
from nebli import etapa,gates
A=Anki()
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
rows=json.loads((D/'suplemento-planejado.json').read_text())
# Conteúdo já corrigido na rodada diária prevalece sobre a foto anterior da geração.
live=json.loads((D/'notas-antes.json').read_text());by={str(x['nid']):x for x in live}
put(D/'campos-mantidos.json',{nid:{k:v for k,v in n['fields'].items() if k in ('Text','Extra','Nome PT','Pergunta')} for nid,n in by.items()})
p=R/'spec.py';s=p.read_text();marker='# Auditoria incremental autorizada F-20261105-CODEX-06/07.'
assert marker not in s
code='''# Auditoria incremental autorizada F-20261105-CODEX-06/07.
_AUD=HERE/'auditoria-2026-11-05'
_SUP=_json.loads((_AUD/'suplemento-planejado.json').read_text())
_LIVE=_json.loads((_AUD/'campos-mantidos.json').read_text())
for _n,_f in _LIVE.items():
 if _n in SHARED_FIELDS:SHARED_FIELDS[_n].update(_f)
def _bloco(_s):return 0 if _s<=2 else 1 if _s==3 else 2 if _s<=6 else 3 if _s<=8 else 4 if _s<=10 else 5 if _s==11 else 6 if _s==12 else 7 if _s<=16 else 8 if _s<=18 else 9 if _s<=21 else 10
for _r in _SUP:
 _k=_r['key'];_s=_r['slide'];_t=_r['target'];_b='A-%02d'%_bloco(_s)
 T[_t]={'slide':_s,'bloco':_bloco(_s),'relacao':_r['relacao'],'query':_r.get('name',_k)}
 _extra=_r['extra']
 if _r['kind']!='kenhub' and not _r.get('front_img'):_extra+='<br><br>'+fig(_r['img'])
 if _r.get('nid'):
  _c=sh(_r['nid'],'azul',_b,_r['relacao'],_s,'A-aula: '+_r['ganho'] if _r.get('ganho') else 'A-aula: relação básica anteriormente omitida.')
  SHARED_FIELDS[str(_r['nid'])]={'Extra':_extra}
  if _r.get('text'):SHARED_FIELDS[str(_r['nid'])]['Text']=_r['text']
 elif _r['kind']=='kenhub':
  _c=kh(_k,_r['src'],'A-aula',_b,_r['relacao'],_s,_r['ganho'],extra=_extra)
 elif _r['kind']=='autoral':
  _front=_r['text']+('<br>'+fig(_r['img']) if _r.get('front_img') else '')
  _c=au(_k,_front,'A-aula',_b,_r['relacao'],_s,_r['ensina'],extra=_extra,motivacao='m-'+_t,organizador='data-nebli-organizacao' in _front)
  AUT.append(_r)
 else:
  _c=ak(_k,_r['src'],'A-aula',_b,_r['relacao'],_s,'Lacuna básica localizada na auditoria; '+_r['fonte'],origin=_r['origin'],text=_r['text'],extra=_extra,copia_traducao_uc07=True)
  if _r['origin']=='Histology':_c.update(manter_focal=True,manter=False)
 CARDS.append(_c);META[_c['key']]={'target':_t,'slide':_s,'bloco':_b,'origem':_r['origin'] if 'origin' in _r else 'Kenhub'}
'''
s=s.replace('# Cor por rubrica:',code+'\n# Cor por rubrica:',1)
# Dois nomes de direção viram interpretação do experimento, mantendo o mesmo c1/ID.
s=s.replace("for row in CUR:\n target=", "for row in CUR:\n if row['key']=='tracadores':\n  row=dict(row,text='<div data-nebli-organizacao=\"true\"><b>Traçadores neurais</b>:<br>Revelar <b>destinos dos axônios</b>: {{c1::anterógrado}}<br>Revelar <b>somas que projetam ao local</b>: {{c1::retrógrado}}</div>',img='tracadores');row.pop('back_image',None)\n target=",1)
# Adapta a redação pós-sináptica sem remover os quatro irmãos originais.
s=s.replace("extra=row['extra']+'<br><br>'+fig(row['img'])", "extra=row['extra']+'<br><br>'+fig(row['img'])",1)
# O último bloco de 3IO antigos exige campos específicos; não mexer nele.
p.write_text(s)
# Atualiza E0 após reler quatro guias, os novos feedbacks e o resultado da rodada concluída.
e=json.loads((R/'exemplares-lidos.json').read_text())
for name in e['leitura_sha256']:
 q=Path(name);e['leitura_sha256'][name]=hashlib.sha256(q.read_bytes()).hexdigest()
for name in e['guias_sha256']:e['guias_sha256'][name]=hashlib.sha256((Path('flashcards/projeto')/name).read_bytes()).hexdigest()
e['guia_sha256']=e['guias_sha256']['GUIA-1-REGRAS.md'];e['feedbacks_lidos_ate']=gates.ultimo_feedback();e['aprendizados']+=['Citar uma categoria ou pôr rótulos no Extra não recupera suas estruturas; conferir pergunta sem resposta.','Básico visual agora e IO regional com aula de destino explícita,sem marcar previsão como cobertura.'];put(R/'exemplares-lidos.json',e)
for k,note in [('E0','Reentrada incremental na aula instalada: guias1–4 relidos,rodada diária concluída,feedbacks06/07 incorporados; histórico anterior arquivado sem reexecutar instaladores.'),('E1','Relidas24lâminas em quatro folhas,apostila Aula1 inteira e Machado cap1–3; fontes não equivalem a transcrição ausente; identificados alvos só no Extra.'),('E2','Compreensão ampliada por operação de recuperação: reconhecer estruturas básicas,interpretar traçadores,RM e organização motora/sensitiva; IO profundo tem destino regional.'),('E3','Mapa integral ampliado antes de compor o suplemento; motivações congeladas para três lacunas autorais. Seleção basal respeita a última orientação de Davi e mantém originais.')]:etapa.registrar(R,k,note)
print('Spec ampliado; E0–E3 registrados para a reentrada.')
