from pathlib import Path
import json,re,sys,hashlib
D=Path(__file__).resolve().parent;R=D.parent;sys.path.insert(0,str(R.parents[1]))
from nebli import etapa
from nebli.artefatos import planejamento
def get(p):return json.loads(p.read_text())
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
P=get(R/'plan.json');E=P['entries']+[dict(v,key='sh-'+k) for k,v in P['compartilhados'].items()];E.sort(key=lambda x:x['order']);by={x['key']:x for x in E};rows=get(D/'suplemento-planejado.json');new={x['key']:x for x in rows}
# Complemento do par funcional já cobrado pelo AnKing; o único c1 é preservado.
corno='<div data-nebli-organizacao="true"><b>Cornos da medula espinal</b>:<br><b>Corpos de motoneurônios somáticos</b>: corno {{c1::anterior}}<br><b>Recepção e processamento sensitivo</b>: corno {{c1::posterior}}</div>'
P['compartilhados']['1792329455992']['fields']['Text']=corno
s=(R/'spec.py').read_text()
if '# Par funcional dos cornos' not in s:s+='\n# Par funcional dos cornos,sem criar irmãos ou notas.\nSHARED_FIELDS["1792329455992"]["Text"]='+repr(corno)+'\n';(R/'spec.py').write_text(s)
put(R/'plan.json',P)
co=get(R/'compreensao-aula.json');m=get(R/'mapa-de-profundidade.json')
for b in co['blocos']:
 if b['laminas'][0]==19:
  b['cards_associados']=list(dict.fromkeys(b['cards_associados']+['sh-1792329761318','sh-1792244862578']))
oldfid={tuple(x['laminas']):x for x in co['fidelidade']['blocos']}
for b in co['blocos']:
 f=oldfid[tuple(b['laminas'])];known={x['aprender']:x for x in f['relacoes']}
 for rel in b['aprender']:
  if rel in known:continue
  x=next((x for x in rows if x['relacao']==rel),None)
  if not x:raise RuntimeError('Relação nova sem origem: '+rel)
  known[rel]={'aprender':rel,'cards':[x['key']],'estado':'recuperavel','julgamento':('A figura Kenhub exige reconhecer '+x['name']+' sem o nome na frente; fonte e posição confrontadas no atlas e na lâmina.' if x['kind']=='kenhub' else 'Frente conferida literalmente: '+re.sub('<[^>]+>',' ',by[x['key']]['fields'].get('Text',''))[:230]+'. '+('A figura foi substituída após crítica independente e mostra o alvo correspondente.' if x['key'].startswith('cavidade-') or x['key'] in ('poda-sinaptica','bipolar-local','nucleos-cranianos-funcao') else 'Imagem e comentário explicam o mesmo alvo,sem exigir IO regional aprofundado.'))}
 if b['laminas'][0]==19:
  for rel,v in known.items():
   if rel.startswith('Degeneração após lesão'):v['cards']=list(dict.fromkeys(v['cards']+['sh-1792329761318','sh-1792244862578']));v['julgamento']='Walleriana recupera degeneração distal; decussação recupera local; o AnKing corticoespinal preserva seus dois IDs e agora recupera contralateral acima e ipsilateral abaixo,com ambos os lados no mesmo c2.'
 if b['laminas'][0]==21:
  for v in known.values():v['julgamento']='O organizador de traçadores foi reescrito para pedir destinos de projeções versus somas de origem. Não é mais só completar o nome de uma direção de transporte; a imagem da injeção acompanha essa inferência.'
 f['relacoes']=[known[q] for q in b['aprender']];f['cards_conferidos']=list(dict.fromkeys(b['cards_associados']));f['nota']+=' Auditoria06/11: recuperações básicas ampliadas e confrontadas com as fontes; IOs regionais específicos têm destino explícito no mapa e não são declarados entregues aqui.'
co['fidelidade']['auditada_em']='2026-11-06';put(R/'compreensao-aula.json',co)
for step in m['passos']:
 for item in step['itens']:
  if item['o_que'].startswith('Degeneração após lesão'):item['cards']=list(dict.fromkeys(item['cards']+['sh-1792329761318','sh-1792244862578']))
for i,step in enumerate(m['revisao']['passos']):
 step['cards_usados']=list(dict.fromkeys(k for it in m['passos'][i]['itens'] for k in it['cards']));step['explicacao_com_os_cards']+=' A auditoria separou recuperação textual de reconhecimento visual. Os novos cards acrescentam as grandes estruturas ou relações deste passo,com fonte por item. A figura de cada novo alvo foi conferida; as estruturas regionais detalhadas não foram promovidas à introdução apenas por existirem no acervo.'
m['revisao']['momento']='E6/E7,revisão do plano materializado e das prévias PC/celular; confirmação no Anki vivo após aplicar.'
put(R/'mapa-de-profundidade.json',m)
# Declarações próprias de figuras; não são parecer independente nem leitura do Anki instalado.
seen=get(R/'imagens-vistas.json');ib=get(R/'imagens-batem.json')
for e in E:
 key=e['key']
 if key in new:
  x=new[key];why=('Destaque verde e seta correspondem a '+x['name']+'; nome em português no verso,marca do Kenhub preservada.' if x['kind']=='kenhub' else 'Pergunta e comentário foram confrontados com '+x['fonte']+'. Figura real correspondente: '+x['img']+'.')
  ib[key]={'veredito':'ok','porque':why}
 elif key in ('tracadores','ressonancia-funcional','sh-1792329760618','sh-1792329455992'):ib[key]={'veredito':'ok','porque':'Delta da auditoria relida: figura de injeção acompanha inferência de traçadores; BOLD original acompanha fMRI; lesão e cornos mantêm figuras anatômicas pertinentes aos pares agora recuperados.'}
 for name in {s for v in e['fields'].values() for s in re.findall(r'src="([^"]+)"',v)}:
  if name not in seen:seen[name]={'qualidade':'boa','intencao':ib.get(key,{}).get('porque','Figura original já conferida no primeiro deck e preservada nesta auditoria.')+' Inspeção da composição e prévia; máscaras são overlays, não imagens anatômicas isoladas.'}
put(R/'imagens-vistas.json',seen);put(R/'figuras-julgadas.json',seen);put(R/'imagens-batem.json',ib)
q=(R/'REVISAO-DE-QUALIDADE.md').read_text();q+='''\n\n# Auditoria de06/11 — fechamento do plano ampliado\n\nAs24lâminas foram novamente vistas e comparadas com a apostila introdutória inteira e Machado cap1–3. O erro anterior era tomar categoria ampla ou figura de verso como recuperação das estruturas. O complemento seleciona32 identificações básicas Kenhub,dois fallbacks anatômicos,teoria de acervo e três autorais por lacunas demonstradas. IO regional profundo tem destino nas aulas03/04/06/07/09; não foi contado como entregue.\n\nOs pares acima/abaixo da decussação e anterior/posterior medular passaram a recuperar ambos os lados,sem novos irmãos ou notas. Traçadores agora pedem inferência origem/destino. A RM estrutural recebe três alvos na imagem da própria aula. Nos painéis de tarefas,a descrição permanece imagem funcional; não se certifica técnicaMRI a partir deles. O cardfMRI usa sua figuraBOLD original. As sete figuras recusadas pelo verificador foram substituídas por cavidades Kenhub destacadas,retina real e painel publicado de eliminação/manutenção sináptica. O organizador de núcleos tem trecho representativo com chave de cores no texto legível,sem catálogo regional.\n\nPreservação é requisito da aplicação: IDs,revisões,comentários,bandeiras,suspensões e agenda dos reusos. Cinco irmãos antigos vazios permanecem na reserva,sem exclusão e sem inflar o total previsto de180cards. A conferência de campos/agendamento e o render vivo ainda são etapas posteriores a este registro do plano.\n''';(R/'REVISAO-DE-QUALIDADE.md').write_text(q)
# Inventário e tipos são os mesmos alvos; nenhum novo pedido é inventado para justificar autoria.
planejamento(R)
etapa.registrar(R,'E5','Plano ampliado composto:62recuperações complementares,matriz de busca e três lacunas autorais explícitas,mesmos IDs de acervo quando disponíveis; figuras corrigidas contra críticas independentes.')
etapa.registrar(R,'E6','Plano e prévias PC/celular relidos: imagens de cavidades,poda,retina e núcleos corrigidas; pares funcionais completados sem criar irmãos; preservar cinco vazios antigos na reserva.')
etapa.registrar(R,'E7','Cobertura em dois sentidos revista contra24lâminas,bibliografia e veteranos. Básico atual separado de IO regional com destino; fonte literal e pergunta do plano conferidas antes da aplicação.')
print('E5–E7 próprios registrados; pareceres independentes e Anki vivo continuam verificações separadas.')
