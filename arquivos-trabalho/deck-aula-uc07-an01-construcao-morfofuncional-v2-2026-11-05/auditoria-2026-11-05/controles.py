"""Materializa decisões da auditoria; não aprova pareceres nem escreve no Anki."""
from pathlib import Path
import json,re,sys,hashlib
D=Path(__file__).resolve().parent;R=D.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
from nebli import etapa,gates
A=Anki()
def get(p):return json.loads(p.read_text())
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
rows=get(D/'suplemento-planejado.json');P=get(R/'plan.json');E=P['entries']+[dict(v,key='sh-'+k) for k,v in P['compartilhados'].items()];E.sort(key=lambda x:x['order']);by={x['key']:x for x in E}
chosen={'somatotopia-definicao':[1481513133224,1481513150417,1609111831754], 'rm-estruturas':[1481163962977,1560884644072,1481130891600], 'nucleos-cranianos-funcao':[1480389622314,1480612351879,1561043470778]}
notes=A('notesInfo',notes=sorted({n for ids in chosen.values() for n in ids}));N={n['noteId']:n for n in notes};put(D/'candidatos-lidos-completos.json',notes)
why={
'somatotopia-definicao':'O acervo cobra posições de face/membros e tipos de dor,mas não o nome do princípio de correspondência topográfica que permite compreender todos esses exemplos da lâmina18.',
'rm-estruturas':'A busca retorna atlas,embriologia e identificação de caudado em outra imagem. Não recupera estes três alvos na RM sagital da aula. O ganho é transferir reconhecimento de atlas para imagem real,sem importar IO regional.',
'nucleos-cranianos-funcao':'Os candidatos encontrados cobram motoneurônio inferior,posição medial e via corticobulbar. Não recuperam o par funcional geral aferente/sensitivo versus eferente/motor aplicado aos núcleos cranianos da lâmina15.'}
exemplars={'somatotopia-definicao':('E','fato-chave situado',1790972069911,1792339386764),'rm-estruturas':('D','leitura visual',1790981521328,1792713393203),'nucleos-cranianos-funcao':('B','contraste por critério comum',1792166970014,1792677734151)}
# Acrescenta inventário sem refazer a seleção anterior por um script histórico.
p=R/'inventario.py';s=p.read_text();mark='# Auditoria incremental: básicos ausentes e destino regional.'
if mark not in s:
 s+='\n'+mark+'''\nfrom pathlib import Path as _Path
import json as _json
_sup=_json.loads((_Path(__file__).parent/'auditoria-2026-11-05/suplemento-planejado.json').read_text())
SLIDES=[(n,cl,t,it+[("audit-"+x['key'],x['relacao'],[x['key']]) for x in _sup if x['slide']==n]) for n,cl,t,it in SLIDES]
''';p.write_text(s)
# Matriz: a busca/cobertura dos autorais usa candidatos realmente lidos desta consulta.
lines=(R/'busca/cobertura.tsv').read_text().splitlines();existing={l.split('\t')[0]:l for l in lines[1:]}
dec=get(R/'decisoes.json');ctx=get(R/'revisor-autorais-contexto.json');org=get(R/'organizadores-fontes.json')
labels=R/'fontes/legendas-conferidas.txt';lt=labels.read_text()
if 'Lâmina15:' not in lt:lt+='\nLâmina15: Núcleos de Nervos Cranianos no Tronco Encefálico. Núcleos e fibras eferentes (motores). Núcleos e fibras aferentes (sensitivos).\n';labels.write_text(lt)
fonte_rm=next(l for l in lt.splitlines() if l.startswith('Lâmina22:'))
fonte_nc=next(l for l in lt.splitlines() if l.startswith('Lâmina15:'))
vet=(R/'fontes/veteranos-introducao.txt').read_text();start=vet.index('Há uma correlação topográfica');fonte_soma=vet[start:vet.index('O arco-reflexo',start)]
local={'somatotopia-definicao':('fontes/veteranos-introducao.txt',fonte_soma),'rm-estruturas':('fontes/legendas-conferidas.txt',fonte_rm),'nucleos-cranianos-funcao':('fontes/legendas-conferidas.txt',fonte_nc)}
rev=(R/'REVISAO-AUTORAIS.md').read_text()
for x in rows:
 key=x['key'];entry=by[key];text=entry['fields'].get('Text','');answers=[re.sub('<[^>]+>','',z.split('::')[0]) for z in re.findall(r'\{\{c\d+::(.*?)\}\}',text)];answer=answers[0] if answers else entry['fields'].get('Nome PT',x.get('name',''))
 ids=chosen[key] if x['kind']=='autoral' else [x.get('src',x.get('nid'))]
 existing[key]='\t'.join([key,x['relacao'].replace('\t',' '),x['fonte'],'lacuna' if x['kind']=='autoral' else 'coberto',','.join(map(str,ids)),answer,why.get(key,x.get('ganho','Reuso de acervo conferido com a fonte; recuperação básica ausente na primeira seleção.'))])
 if x['kind']=='autoral':
  dec[key]=dict(acao='autoral',por_que=why[key],motivo=why[key],fonte=x['fonte'],decora=answer)
  file,trecho=local[key];ctx['cards'][key]={'origin':'Autoral','motivacao':'m-'+x['target'],'fontes':[{'arquivo':file,'trecho':trecho,'localizador':x['fonte']}],'busca':{'descricao':'Seções introdutórias já lidas; busca complementar por palavra e significado em11acervos+NEBLI-vivo,catálogo reindexado53265notas.','candidatos':[{'fields':{k:v['value'] for k,v in N[n]['fields'].items() if k in ('Text','Extra','Header')},'decisao':why[key]} for n in ids],'decisao':why[key]},'contexto':{'relacao':x['relacao'],'aula':P['lesson_id'],'imagens_locais':[str((R/'img'/('nebli-u7an01-'+x['img']+'.png')).resolve())]}}
  par,tipo,ex,anti=exemplars[key]
  line=f"- {key} — par: §{par}; tipo-informacao: {tipo}; ensina: {x['ensina']}; EXEMPLAR {ex}; semelhança: {'recuperar um nome específico a partir de seu contexto' if par=='E' else 'identificar o alvo efetivo da figura' if par=='D' else 'recuperar dois conceitos pelo mesmo eixo discriminante'}; adaptação: {x['relacao']}; ANTI {anti}; decora: {answer} — conferido no plano,render vivo ainda pendente.\n"
  if '- '+key+' — par:' not in rev:rev=rev.replace('## Revisão final no deck vivo','## Auditoria incremental — revisão anterior à instalação\n\n'+line+'\n## Revisão final no deck vivo',1)
  if 'data-nebli-organizacao' in text:org[key]={'arquivo':file,'trecho':trecho}
(R/'REVISAO-AUTORAIS.md').write_text(rev);(R/'busca/cobertura.tsv').write_text(lines[0]+'\n'+'\n'.join(existing.values())+'\n');put(R/'decisoes.json',dec);put(R/'revisor-autorais-contexto.json',ctx);put(R/'organizadores-fontes.json',org)
# Tipos explícitos; a recuperação visual tem ganho diferente da teoria sobre a mesma estrutura.
types=(R/'tipos.tsv').read_text().splitlines();typed={l.split('\t')[0]:l for l in types[1:]}
for x in rows:
 if x['key'] not in {e['key'] for e in P['entries']}:continue
 tipo='comparacao' if 'data-nebli-organizacao' in x.get('text','') else 'fato-chave' if x['kind']=='kenhub' or 'visual' in x['key'] or 'cavidade-' in x['key'] or x['kind']=='autoral' else 'mecanismo'
 typed[x['key']]='\t'.join([x['key'],tipo,x['relacao'].replace('\t',' '),'sim','fio' if x['kind']=='autoral' else 'lacuna'])
(R/'tipos.tsv').write_text(types[0]+'\n'+'\n'.join(typed.values())+'\n')
m=get(R/'mapa-de-profundidade.json');mo=get(R/'motivacoes.json');co=get(R/'compreensao-aula.json')
for x in rows:
 for step in m['passos']:
  for item in step['itens']:
   if item['id']==x['item_id']:
    item['termos']=[x['name']] if x['kind']=='kenhub' else [re.sub('<[^>]+>','',z.split('::')[0]) for z in re.findall(r'\{\{c\d+::(.*?)\}\}',x['text'])]
 for mot in mo['motivacoes']:
  if x['kind']=='autoral' and mot['id']=='m-'+x['target']:
   pos=next(i for i,e in enumerate(E) if e['key']==x['key']);mot['depois_de']=E[pos-1]['key']
basicos=[]
for x in rows:
 basic=dict(alvo=x.get('name',x['relacao']),fonte=x['fonte'],cards=[x['key']],estado='agora',modalidade='identificacao' if x['kind']=='kenhub' or x['key'] in ('hipotalamo-visual','raiz-posterior-visual') else 'relacao',kenhub_disponivel=x['kind']=='kenhub')
 if basic['modalidade']=='identificacao' and not basic['kenhub_disponivel']:basic['motivo_fallback']=x['fonte']
 basicos.append(basic)
adiados=get(D/'io-aulas-proprias.json')
for x in adiados:x.update(alvo=x['nome'],estado='previsto')
m['uc07_basico_e_destino']={'basicos':basicos,'adiados':adiados,'nota':'O mapa ampliado não transforma figuras do Extra em recuperação. Básico agora; IO aprofundado previsto nas aulas próprias não é declarado entregue.'}
put(R/'mapa-de-profundidade.json',m);put(R/'motivacoes.json',mo)
esc=get(R/'escopo.json')
if 'rm-estruturas' not in esc.get('cards_de_conexao',[]):esc.setdefault('cards_de_conexao',[]).append('rm-estruturas')
put(R/'escopo.json',esc)
for b in co['blocos']:
 if b.get('papel')=='exemplo':
  used={k for group in b.get('principios_ilustrados',[]) for k in group.get('cards',[])}
  for key in b['cards_associados']:
   if key not in used:b.setdefault('principios_ilustrados',[]).append({'principio':('Degeneração e cruzamento revelam a organização e o lado de uma via motora.' if b['laminas'][0]==19 else 'Uma lesão localizada pode associar uma região cerebral à perda de uma função específica.'),'cards':[key]})
put(R/'compreensao-aula.json',co)
# O GUIA-1 e o pipeline tiveram regra escrita no lugar nesta auditoria; conteúdo novo foi lido ao redigir.
e=get(R/'exemplares-lidos.json')
for name in e['leitura_sha256']:e['leitura_sha256'][name]=hashlib.sha256(Path(name).read_bytes()).hexdigest()
for name in e['guias_sha256']:e['guias_sha256'][name]=hashlib.sha256((Path('flashcards/projeto')/name).read_bytes()).hexdigest()
e['guia_sha256']=e['guias_sha256']['GUIA-1-REGRAS.md'];e['feedbacks_lidos_ate']=gates.ultimo_feedback();put(R/'exemplares-lidos.json',e)
etapa.registrar(R,'E3','Mapa e fontes consolidados após confrontar nomes oficiais e frentes novas: três lacunas autorais motivadas,escopo básico/regional explícito e sequência conferida. Não há IO regional avançado promovido por disponibilidade.')
print('Controles preparados;9 candidatos completos para releitura; nenhuma aprovação independente fabricada.')
for n in notes:
 print(n['noteId'])
 for f in ('Text','Extra'):print(f,re.sub('<[^>]+>',' ',n['fields'].get(f,{}).get('value',''))[:1600])
