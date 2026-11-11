import json
from pathlib import Path
r=Path('arquivos-trabalho/deck-aula-uc07-an04-diencefalo-telencefalo-irrigacao-2026-11-09');p=json.loads((r/'revisor-autorais-entrada.json').read_text());mp=json.loads((r/'revisor-autorais-mapa.json').read_text())['ids']
J={
'sh-1792697125350':'Distingue cérebro de encéfalo e recupera as duas divisões cerebrais. O Extra agora está em inglês e inclui tronco/cerebelo sem os confundir com telencéfalo.',
'diencefalo-escondido':'A frente limita a não visualização à vista lateral e recupera a estrutura que recobre o diencéfalo. Corrigi o Extra: o tronco também pode ser visto lateralmente.',
'diencefalo-partes-org':'Os critérios espaciais recuperam as quatro partes do diencéfalo em conjunto; subtálamo lateral não é falsamente mostrado como estrutura exposta no corte mediano.',
'talamo-limites-org':'Cinco vizinhos organizados pelo corte coronal, distinguindo faces inferior medial e lateral. Extra explica a topografia, sem a antiga moldura sobre desenho do professor.',
'nucleo-x-ganglio':'Contraste complementar no mesmo índice impede que um termo entregue o outro; critério SNC diferencia núcleo e gânglio e prepara os núcleos profundos.',
'talamo-nucleos-org':'Grupos topográficos e funções gerais correspondem ao recorte da fala; nomes geniculados/funções específicas têm AnKing próprios e não ficam apenas no Extra.',
'hipotalamo-limites-org':'Limites e marcos do assoalho são recuperados sem vazamento, em sequência cobrada na prova. Números destacados representam a ordem, não nomes de estruturas inventadas.',
'hipotalamo-nucleos-org':'Agrupa supraópticos, tuberais e mamilares conforme a divisão usada pelo resumo. IO do arqueado foi conferido no hipotálamo, evitando o homônimo bulbar.',
'subtalamo-limites-org':'Quatro limites distinguem subtálamo de hipotálamo e mesencéfalo. Relação com motricidade e hemibalismo é explicação coerente e possui card clínico AnKing.',
'faces-hemisferio':'Recupera conjuntamente faces superolateral, medial e inferior por condição de visualização. Extra atual orienta fissura, base e abóbada craniana em vez de descrever a aula.',
'giro-x-sulco':'Uma oposição simples recupera saliência e depressão cortical, essencial antes da identificação de giros. O mesmo índice evita fornecer a metade complementar.',
'lobos-limites-org':'Sulcos central/lateral/parietoccipital ligam aos lobos certos. Semilunar fica explicitamente variável; não se transforma num limite universal do occipital.',
'corpo-caloso-partes-org':'Sequência anterior-posterior de rostro, joelho, tronco e esplênio é recuperada por posição, complementando IO de cada parte sem depender de uma legenda no verso.',
'face-inferior-org':'Recupera a sequência regional medial da face inferior usada na aula, com IOs de occipitotemporal medial, parahipocampal e úncus para discriminação visual.',
'achar-sulco-central':'Pré e pós-central são exigidos para localizar o sulco na face superolateral; removida exclusividade falsa sobre todos os giros transversais do encéfalo.',
'corte-horizontal-org':'A sequência ínsula/extrema/claustro/externa/putâmen/pálido/interna é útil para reconstruir o corte. Ordinais têm função explícita e os IOs permitem localizar cada termo.',
'estriado-org':'A frente especifica nomenclatura macroscópica, sem metatexto de aula; Extra diferencia estriado funcional e pálido, evitando tomar amígdala por corpo estriado.',
'capsula-interna-partes-org':'Vizinhos distinguem braços anterior e posterior, com joelho entre ambos. A linha de projeção corrige gabarito ruim do fórnix; Extra atual preserva a distinção com sua comissura.',
'sh-1792696998756':'Recupera união de vertebrais em basilar com topografia pontina, sem encaminhar a uma aula futura. Imagem do sulco ilustra a localização mencionada na frente.',
'vertebrobasilar-org':'Origem da PICA, formação da basilar e suas terminações aparecem como relações distintas num conjunto; Extra inclui outros ramos sem trocar AICA por PICA.',
'aci-ramos-org':'Trajeto, ausência de ramos cervicais e ramos intracranianos estão titulados corretamente. Canal e sifão são alvos inteiros; território orbitário não cobra só adjetivo óbvio.',
'territorios-org':'Territórios corticais principais são recuperados pelas faces, com qualificação da ACP em occipital/temporal inferomedial. Não afirma que toda face inferior pertence à ACP.',
'willis-org':'Distingue as duas comunicantes e deixa ACM fora do anel, conforme a prova. Extra enumera componentes reais e evita a composição falsa do gabarito antigo.'}
assert set(mp.values())==set(J)
out={'pacote_sha256':p['pacote_sha256'],'executor':'Codex /root','momento':'Segunda leitura literal das23frentes/Extras e fontes; antes de instalar','cards':[{'case_id':c['case_id'],'input_sha256':c['input_sha256'],'veredito':'aprovado','julgamento':J[mp[c['case_id']]],'trecho':c['fields']['Text']} for c in p['cards']]}
(r/'revisao-executor-autorais.json').write_text(json.dumps(out,ensure_ascii=False,indent=1));print('23 julgamentos próprios do executor registrados')
