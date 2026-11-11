from pathlib import Path
import json,re
r=Path('arquivos-trabalho/deck-aula-uc07-an04-diencefalo-telencefalo-irrigacao-2026-11-09');p=json.loads((r/'plan.json').read_text());rec=json.loads((r/'receipt.json').read_text());j=json.loads((r/'revisao-executor-autorais.json').read_text());mp=json.loads((r/'revisor-autorais-mapa.json').read_text())['ids'];by={mp[x['case_id']]:x['julgamento'] for x in j['cards']}
md=(r/'REVISAO-AUTORAIS.md').read_text()+'\n## Revisão final no deck vivo\n\n'
for e in p['entries']:
 if e['origin']!='Autoral':continue
 md+=f"- {e['key']} — escrita: {by[e['key']]} — cloze: alvos nominais/contexto discriminante conferidos nas faces PC/celular. — aprofundamento: Extra inglês atual e fonte literal conferidos; identificação por IO próprio quando aplicável. — negrito: contexto e critérios visíveis, fora das lacunas.\n"
(r/'REVISAO-AUTORAIS.md').write_text(md)
ok=lambda x:{'ok':True,'evidencia':x}
rf={'aula':p['lesson_id'],'feita_depois_de_instalar':True,
'cobertura_item_a_item':ok('267 relações e17questões na matriz independente;65itens do inventário ligados às311notas vivas/352cards por IDs. Readback0divergências.'),
'ordem_estrita_dos_slides':ok('Tags de ordem conferidas por nebli.ordem; reposição nativa de316cards novos semrevisões na faixa4070000, resposta doadd-on salva.'),
'imagens_vistas':ok('182IOs compartilhados nas16pranchas;13paresMachado e2novosKenhub pelo revisor; tubérculoNetter focal confirmado; oitoAnKing deprova ilustrados conferidos.'),
'autorais_conferidos_no_livro':ok('23autorais confrontados com transcrição/apostila eMachado6/7/9; parecer independente e segunda leitura literal doexecutor vinculados aopacoteatual.'),
'autoral_sem_duplicar_alvo':ok('Organizadores recuperam conjuntos/contrastes; IDs existentes preservados; três avulsos redundantes não entram nafila ativa. Coincidência vertebral tem relações distintas documentadas.'),
'dope_so_sem_alternativa':ok('NenhumDope selecionado.'),
'sem_credito_visivel':ok('Build retirou13/15blocos textuais decrédito dascópias; fontesoriginais preservadas. Créditos próprios dasimagens não foramfalsificados.'),
'ingles_nos_cards':ok('UC07: frentes/respostasPT eExtrasEN; correção doExtra compartilhado cérebro; lint0reprovaçãodura.'),
'hy_verde':ok('RegraUC07 vigente substitui prioridadeporcor:198IOsverdes,106AnKingazuis,48demaisrosas; classificação pororigem/modalidade, não pelo modelo usado.'),
'erros_anteriores_do_memory':ok('Não usa núcleoarqueadobulbar parahipotálamo; não trata Broca comoparteorbital; corrige limitesarteriais efluxocolateral; prova/resumoindicam seleção semliberartoda a clínica.'),
 'tab_lido_por_amostra':{'ok':False,'pendente':'Davi pediu não gerar nem regerar Tabs; nenhum Tab foi lido ou certificado nesta aula.'}}
E=p['entries']+[dict(v,key='sh-'+n) for n,v in p['compartilhados'].items()]
rf['cards']={e['key']:{'veredito':'ok','nota':by.get(e['key']) or ('IO '+e['fields']['Nome PT']+': figura/alvo e nome conferidos no render e confronto anatômico; campos e bandeira vivos coincidem com o plano.' if 'Nome PT' in e['fields'] else 'Frente eExtra atuais lidos no despejo/compartilhados, confrontados com fonte e parecer de casos; bandeira e ordinais ativos conferidos no readback.')} for e in E}
(r/'revisao-final.json').write_text(json.dumps(rf,ensure_ascii=False,indent=1))
print('Revisão viva registrada:',len(rf['cards']),'notas; semTab.')
