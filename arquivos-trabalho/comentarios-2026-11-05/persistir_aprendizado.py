from pathlib import Path
import json,re,html
C=Path(__file__).parent;ROOT=C.parents[1];G=ROOT/'flashcards/projeto';P=json.load(open(C/'propostas.json'));N={n['noteId']:n for n in json.load(open(C/'notas-antes-com-similares.json'))};R=json.load(open(C/'RODADA.json'))
POS={
1791627547052:'O X aprova uma explicação espacial concreta: dobrar o DNA aproxima enhancer e promotor, com figura mostrando a alça. Copiar causa→relação espacial→consequência. A lacuna histórica longa e o número de palavras não são autorização para repetir clozes longos nos novos cards.',
1791630173420:'O X aprova contraste funcional cis/trans: um RNA separado reconhece outra molécula por pareamento. O alvo trans é induzido pelo mecanismo. Negrito histórico dentro do cloze não substitui a norma de contexto visível; ainda não houve revisão espaçada suficiente para avaliar retenção.',
1791630905344:'O X aprova ecologia→exposição: Histoplasma em solo com excretas explica risco de caverna ou galinheiro. A relação liga nome, ambiente e clínica. Não copiar automaticamente toda a extensão do Extra nem tratar uma primeira resposta como prova de memória duradoura.',
1792141769157:'O X aprova um quadro por método com contrastes exógenos correspondentes: CT/iodo, MRI/gadolínio e ultrassom/microbolhas. Preservar os índices deliberadamente editados por Davi; não impor c1 único por estética. O eixo método→agente torna os vizinhos comparáveis.',
1792170508430:'O X aprova um conjunto natural do mesmo eixo: temperatura, umidade e pH como condições de crescimento fúngico. Recuperar em conjunto faz sentido pela relação, não apenas por haver três palavras. Valores e exceções do verso ainda precisam de fonte específica ao serem reutilizados.',
1793199679755:'O X aprova o contraste ELISA direto→antígeno e indireto→anticorpo acompanhado de duas figuras reais correspondentes. O ganho é comparar o objeto detectado, não decorar nomes isolados. Existem poucas revisões e um irmão histórico sem estudo; não inferir superioridade de retenção a partir desse X.'}
# A chave positiva usa o nid real, diferente do cid X em ELISA.
positive_notes=json.load(open(C/'novos-gosteis-notas.json'));actual={n['noteId'] for n in positive_notes}
if 1793199679755 not in actual and 1793199679755 in POS:POS[1793199679755+0 if 1793199679755 in actual else 1793199679755]=POS[1793199679755]
# Corrigir identificador pelo conteúdo vivo, sem atribuir X ao card errado.
for n in positive_notes:
 if 'ELISA'in n['fields'].get('Text',{}).get('value',''):
  a=POS.pop(1793199679755);POS[n['noteId']]=a;break
UI={1791630905957:'Coração de gostei ainda exige inspeção na janela real do Anki. Código mede largura e desloca12px; captura do display indisponível, portanto não houve validação visual de interface nem CORRIGIDO.',1792787231967:'Pedido de indicador gostei já tem implementação instalada. Falta observar sua posição na janela real junto da bandeira; teste de DOM não substitui esta inspeção.'}
notes={int(k):v['motivo']for k,v in P.items()};notes.update(UI)
p=G/'exemplares_analise.py';s=p.read_text();marker='# Rodada diária 05/11: análises específicas, não aprovação das correções.'
if marker in s:s=s[:s.index(marker)]
s+='\n'+marker+'\nEXEMPLARES.update('+repr(POS)+')\nNOTAS.update('+repr(notes)+')\n';p.write_text(s)
# Regras vigentes reescritas; não manter duas instruções de dicas em conflito.
p=G/'GUIA-1-REGRAS.md';s=p.read_text();s=s.replace('3+ itens no mesmo índice levam a 1ª letra como dica (`::A…`).','3+ itens no mesmo índice recebem dicas apenas quando não revelam o alvo. Siglas curtas nunca recebem inicial. Respeitar retirada de iniciais pedida por Davi, registrando a fala em `dicas_preferencia_davi` (≥30 caracteres); gerador e gates preservam essa exceção local.')
RULES=[
'Negrito de organizador deve permanecer visível no critério de cada linha, além do título; `qualidade_comentarios.negrito_contexto` bloqueia destaque ausente ou escondido no cloze. O significado discriminante do destaque ainda exige leitura humana.',
'Organizador tem eixo comum e alvo essencial em cada linha; reduzir carga retirando qualificadores repetidos, sem esconder detalhe secundário nem expor nome cognato da resposta. Exemplos: HST1793784421465 e GLP-1/PYY1793476864207.',
'Não recolocar iniciais retiradas por Davi nem usar inicial de sigla curta como dica; `spec_lib.dicas`, `gates.inducao_clozes` e `verificador_casos.forma_das_lacunas` respeitam a preferência literal local, sem dispensar revisão de indução.',
'Novas seleções não incluem fontes marcadas Only_Step_2; a presença de uma tag Step2 junto de Step1 não prova exclusividade. `qualidade_comentarios.step2_only` é gate duro antes da instalação. A retirada de1793803589750 foi expressamente pedida; não chamar uma palavra de conduta de critério automático para qualquer card.',
'Imagem precisa mostrar o objeto ou mecanismo cobrado, e seus rótulos precisam continuar legíveis no render real em390px. Nome de arquivo não prova anatomia. Verificar também o CSS do modelo: tabela a6,63px reprova mesmo que o HTML declare16px sem!important.',
'Analisar X pela função e pela dimensão aprovada; índice editado pelo usuário e organização que ele escolheu prevalecem sobre uniformização estética. Correção do executor não vira exemplar positivo sem X/elogio novo.',
'Estatística por formato é descritiva: comparar UC/assunto, fase, intervalo, idade e exposição, registrar tamanho da amostra e reconhecer que formato atual pode diferir do usado em revisões antigas. Não converter tempo ou retenção bruta em lei causal nem mexer no FSRS.'
]
head='## Rodada diária de 05/11 — prevenção vigente\n\n'+'\n'.join('- '+r for r in RULES)+'\n\n'
if '## Rodada diária de 05/11'not in s:s=s.replace('\n\n','\n\n'+head,1)
p.write_text(s)
p=ROOT/'MEMORY.md';s=p.read_text();s=s.replace('considerando exposição,idade e conteúdo; estatística observacional','considerando exposição,idade,conteúdo e o fato de o formato atual poder diferir do histórico; estatística observacional');s=s.replace('especialmente o negrito','especialmente o negrito')
# Atualizar precisamente as regras, sem substituir o restante do arquivo compartilhado.
s=s.replace('negrito no contexto/ação e ao eixo dos organizadores.','negrito visível no critério de cada linha e ao eixo/alvo essencial dos organizadores. Não recolocar iniciais retiradas por Davi; siglas curtas ficam sem inicial. As novas seleções excluem fontes `#AK_Other::Only_Step_2`, sem confundir com tags Step2 compartilhadas com Step1. Conferir tabelas e rótulos em390px com CSS real, não só o valor declarado no HTML.')
p.write_text(s)
# Guia positivo com análise de cada gosto novo.
p=G/'GUIA-2-EXEMPLARES.md';s=p.read_text();block='## Gostei novos de 05/11 — dimensão aprovada\n\n'+'\n'.join(f'- **{nid}:** {a}'for nid,a in POS.items())+'\n\nNão há prova de que um desses formatos causou melhor retenção: cinco notas novas ainda têm zero revisões espaçadas ou exposição muito curta. Ver relatório da rodada.\n\n'
if '## Gostei novos de 05/11'not in s:s=s.replace('\n\n','\n\n'+block,1)
p.write_text(s)
def plain(t):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',t))).strip()
# Índice rastreável de cada pedido; antes/depois integral fica na corrida e no corpus gerado.
p=G/'GUIA-3-ANTI.md';s=p.read_text();block='## Rodada de 05/11 — pedidos examinados e causas\n\n'
for i in R['itens']:
 nid=i['nid'];old=N[nid]['fields'].get('Text',{}).get('value','');new=P.get(str(nid),{}).get('fields',{}).get('Text',old);cause=notes[nid]
 block+=f'- **{nid}:** '+(('Davi: “'+i['fala']+'”. ')if i['fala']else('Comando '+','.join(i['tipos'])+'. '))+cause+'\n'
block+='\nAntes/depois completos: `arquivos-trabalho/comentarios-2026-11-05/propostas.json`; notas originais e revisão independente preservadas. Nove similares de BM52 também receberam versos causais. Os dois casos de interface permanecem pendentes, sem marcador de conclusão.\n\n'
if '## Rodada de 05/11 — pedidos examinados'not in s:s=s.replace('\n\n','\n\n'+block,1)
p.write_text(s)
# Registro das buscas efetivamente realizadas, sem simular pesquisa global em cada card.
family=json.load(open(C/'familia-bm52.json'));familyids=[n['noteId']for n in family]
for item in R['itens']:
 nid=item['nid'];tags={t for t in N[nid]['tags']if t.startswith('NEBLI::2026')};same=[k for k,n in N.items()if tags.intersection(n['tags'])]
 item['familia']='interface'if nid in UI else ('verso-causal-BM52'if nid in familyids else 'recuperacao-e-figura-da-aula')
 item['similares']={'busca':'Busca local por tags da mesma aula entre as pendências lidas; '+('consulta Anki tag:NEBLI::2026-uc03-biologia-molecular-52-expressao-eucariotos-ii e leitura das41notas.'if nid in familyids else 'cruzamento de frentes e versos na mesma rodada, com busca de acervo de imagens registrada em busca-figuras*.json.'),'nids':sorted(set(same+([k for k in familyids]if nid in familyids else[])))or[nid],'corrigidos':[k for k in same if str(k)in P]}
 item['causa']=notes[nid]
 item['prevencao']={'gate':'','nao_mecanizavel':'A relação científica entre pista, alvo e figura depende de julgamento de conteúdo e leitura real da fonte, além de medidas de layout. Não é demonstrada só por regex.','indicacao':RULES[1]if nid not in UI else RULES[4],'exemplo':plain(N[nid]['fields'].get('Text',{}).get('value',''))[:180]+' → '+plain(P.get(str(nid),{}).get('fields',{}).get('Text',N[nid]['fields'].get('Text',{}).get('value','')))[:180]+'; '+notes[nid]}
 item['corrigido']='pendente: inspeção do coração na interface real do Anki; captura indisponível, código instalado.'if nid in UI else False
R['sync']=False;(C/'RODADA.json').write_text(json.dumps(R,ensure_ascii=False,indent=1))
# Evidência dos positivos e comparação controlada por uma UC/faixa de intervalo.
stats=json.load(open(C/'stats/resumo.json'));groups=[r for r in stats['grupos']if r['uc']=='UC03'and r['fase']=='revisao'and r['intervalo_previo']=='1-6-dias'];
(C/'APRENDIZADO-STATS.md').write_text('# Preferências e revisões,05/11\n\nSnapshot somente leitura:15.007cards com tagsNEBLI,13.659notas,15.083eventos. Isto inclui notas de referência e cards sem estudo; não significa15.007cards revisados.\n\n'+ '\n'.join(f"- UC03,{r['formato']},intervalo1–6dias: {r['cards']}cards,{r['revisoes_espacadas']}revisões,{r['acerto_revisoes']:.1%}acerto,mediana{r['tempo_mediano_ms']/1000:.2f}s."for r in groups)+'\n\nMesmo nessa faixa os intervalos medianos diferem (cloze2dias,organizador1dia). Conteúdo,idade,carga,seleção e exposição confundem as taxas. O formato descrito é o da nota no snapshot, não um registro do formato em cada evento antigo. Não concluir que organizador causa pior memória.\n\nOs novos gosteis favorecem explicação espacial causal,contraste,ecologia→exposição e quadros com eixo único. Isto é aprovação explícita da função; as revisões recentes ainda não comprovam retenção. Cinco notas novas não têm revisão espaçada suficiente. O enhancer tem4revisõesespaçadas sem falha; o ELISA tem3 com2acertos,amostra insuficiente para generalizar. Nenhuma agenda/FSRS foi ajustada por estas métricas.\n')
# Preferências locais duráveis para a próxima curadoria.
(C/'preferencias-locais.json').write_text(json.dumps({k:p['dicas_preferencia_davi']for k,p in P.items()if p.get('dicas_preferencia_davi')},ensure_ascii=False,indent=1))
print('6gosteis e77pedidos anotados;84notas com análises específicas;regrasvigentes atualizadas')
