import json,re,runpy
from pathlib import Path
C=Path(__file__).parent;ctx=runpy.run_path(str(C/'preparar.py'));P=ctx['P'];N=ctx['N'];set_=ctx['set_']
R=json.load(open(C/'revisao-organizadores.json'))
for e in R['cards']:
 if e['nid']==1792175888632:continue
 set_(e['nid'],text=e['proposta']['Text'],extra=e['proposta']['Extra'],keep_images=False,reason=e['causa'])
# Pedido de imagem não autoriza substituir o conjunto aprovado por outro eixo.
set_(1792175888632,reason='Título dizia agente mas as lacunas cobravam doenças. Preservado conjunto aprovado e índice; título passa a cobrar as doenças e as iniciais passam a orientar sem agentes cognatos expostos.',text='<div data-nebli-organizacao="true"><b>Selected subcutaneous mycoses</b><br><b>Nodular lymphatic spread</b>: {{c1::sporotrichosis::s…}}<br><b>Muriform bodies</b>: {{c1::chromoblastomycosis::c…}}<br><b>Fungal grains</b>: {{c1::eumycetoma::e…}}<br><b>Thick-walled yeasts in chains</b>: {{c1::lobomycosis::l…}}<br><b>Pigmented tissue hyphae</b>: {{c1::phaeohyphomycosis::p…}}</div>',extra='Selected examples, not an exhaustive classification. Tissue forms distinguish these infections; many follow traumatic inoculation. Sporotrichosis can also follow cat scratches or bites. Agents include Sporothrix, Fonsecaea, Madurella, the agent of Jorge Lobo disease and other dematiaceous molds, respectively.',keep_images=False)
# Corrigir cinco problemas materiais encontrados pela revisão independente.
P['1793803591426']['fields']['Text']='<b>Mast-cell activation</b> may follow {{c1::IgE}} cross-linking or {{c1::non-IgE mechanisms}}.'
P['1793803583523']['fields']['Text']=P['1793803583523']['fields']['Text'].replace('Fluid inside a cavity: imaging contrast','Cavity imaging by method')
P['1791630176396']['fields']['Text']='<b>RNA-silencing precursors</b><br><b>Long double-stranded RNA</b> can generate {{c2::siRNAs}}.<br><b>Genome-encoded precursors</b> of {{c2::miRNAs}} fold into {{c1::hairpin}} structures.'
P['1791630175095']['fields']['Extra']=P['1791630175095']['fields']['Extra'].replace('outside a coding frame','outside a coding sequence')
P['1791630906367']['fields']['Text']='Oral lesions of <b>disseminated histoplasmosis</b> can involve the {{c1::tongue}} and {{c1::palate}}.'
# Imagem já correta no primeiro deck: manter conteúdo; só responder ao comando depois de conferir ao vivo.
set_(1792588686960,reason='Pedido atendido na refação entregue da AN01: esquema SNC/SNP real da aula instalado, com notas e cards conferidos. Não reescrever o deck recém-entregue.')
# Mantém figuras adequadas, com foco e leitura responsiva, após inspeção explícita.
set_(1791628675323,extra='Traumatic implantation commonly affects exposed limbs. The clinical photographs show verrucous plaques on the lower limb, matching the typical exposure in rural work.',reason='Fotos reais mostram exatamente os membros afetados; ampliadas para remover limite antigo de360px.')
set_(1792081484462,extra='Post-primary TB often affects apical or posterior upper-lobe segments. The radiograph illustrates an upper-zone abnormality; a normal-looking image would not establish the oxygen-related predilection by itself.',image='e84b639cee9b160f510e43230a6cad57.JPG',keep_images=False,reason='Incluída radiografia real do acervo AnKing, com alteração em campo superior, em vez de figura genérica de bactéria.')
set_(1792695052983,extra='Negative-sense viral RNA cannot serve directly as mRNA. It remains associated with nucleoprotein in a ribonucleoprotein complex; the virion also carries RNA-dependent RNA polymerase to begin transcription. The helical nucleocapsid panel illustrates RNA wrapped by repeated capsid-protein subunits.',image='nebli-0511-nucleocapsideo.png',keep_images=False,reason='Incluído painel real da aula de estrutura viral com RNA e subunidades proteicas helicoidais; verso distingue revestimento e polimerase.')
set_(1792786398632,image='nebli-0511-cas9-reparo.png',keep_images=False,reason='Recorte da aula mostra NHEJ→indel e contraste com HDR; o desenho anterior de Cas9 sozinho não mostrava a consequência de reparo.')
set_(1792786400608,image='nebli-bm54-sirna-via-p22-20261025.jpeg',keep_images=False,reason='Esquema textual próprio trocado por figura real de Dicer/Argonaute e alvo clivado; o verso explicita permanência da guia.')
set_(1792788316281,image='nebli-0511-repressor-mascaramento.png',keep_images=False,reason='Painel real da aula mostra repressor cobrindo superfície do ativador sem removê-lo do DNA; separado de competição por sítio.')
set_(1793301693418,reason='Lâmina real mostra infiltrado mononuclear perivascular; preservada imagem alinhada ao alvo e ampliado limite para leitura responsiva.')
# Figuras adicionais para pedidos que não tinham apoio correspondente.
images={1791000312550:'3a35111470df6ac145ebfb635e652424.png',1791627549652:'nebli-0511-gal4-hibrido.png',1791631347892:'nebli-0511-cira-myc.jpg',1791780353397:'nebli-0511-eosinofilo-granulos.png',1792713398630:'nebli-0511-kh-estomago-posterior.jpg',1792713401129:'langman-15-17.png',1792713405053:'nebli-0511-vias-biliares.png',1793476864207:'nebli-0511-entero-tipos.jpg',1791630173920:'nebli-0511-trp-comparacao.png'}
for nid,image in images.items():
 old=P[str(nid)]['fields'].get('Extra',N[nid]['fields'].get('Extra',{}).get('value',''))
 old=re.sub(r'<img\b[^>]*>','',old)
 P[str(nid)]['fields']['Extra']=old+'<br><br><img src="'+image+'" style="width:100%;max-width:950px;height:auto;display:block;margin:18px auto">'
P['1792713398630']['fields']['Extra']='The stomach lies anterior to the pancreas across the lesser sac. In this Kenhub view, the stomach has been opened and lifted to expose its posterior wall and the pancreas behind it.<br><br><img src="nebli-0511-kh-estomago-posterior.jpg" style="width:100%;max-width:950px;height:auto">'
# Comparador sistêmico pedido, em notas de forma/via de micoses sistêmicas, não em dermatófitos.
for nid in [1791630905518,1791630906367,1791630906668,1792065183130]:
 P[str(nid)]['fields']['Extra']+='<br><br><img src="b39abbbf00aa0b03a99911510c118e8c.webp" style="width:100%;max-width:950px;height:auto">'
# Quadro transversal solicitado em várias notas pertinentes. Tabela viva responsiva, não screenshot.
fungus=next(e for e in R['cards'] if e['nid']==1791628675571)['proposta']['Extra']
table=fungus[fungus.index('<table>'):]
for nid in [1791628675198,1791626776253,1791557941758,1792065183130,1792175888632]:
 P[str(nid)]['fields']['Extra']+='<br><br>'+table
# Figura da classificação é quadro original da aula, complemento da tabela viva.
P['1792175888632']['fields']['Extra']+='<br><br><img src="nebli-0511-subcut-comparacao.png" style="width:100%;max-width:950px;height:auto">'
# Marca organizadores como tal para lint/render, sem trocar índices.
for nid,p in P.items():
 for field,v in list(p['fields'].items()):
  if field=='Text' and v.count('<br>')>=2 and 'data-nebli-organizacao' not in v:p['fields'][field]='<div data-nebli-organizacao="true">'+v+'</div>'
  if field=='Extra':
   v=re.sub(r'<small>.*?</small>','',v,flags=re.S)
   # Normalizar cada imagem, sem alterar bytes do original nem esticar além do viewport.
   v=re.sub(r'<img\b([^>]*)>',lambda m:'<img src="'+re.search(r'src=[\"\']([^\"\']+)',m[0])[1]+'" style="width:100%;max-width:950px;height:auto;display:block;margin:18px auto">',v)
   p['fields'][field]=v
new=next(e for e in R['cards'] if e['nid']==1791625424233)['novo_organizador']
new['Extra']+='<br>Catalog of the two SCID groups in IUIS 2024; hypomorphic variants may have different phenotypes. MHC class II deficiency belongs to a separate combined-immunodeficiency group.'
json.dump({'fields':{k:new[k] for k in ('Text','Extra')},'referencia':'IUIS2024 tabelas1; revisao-organizadores.json; busca-scid.json','deck_da_nota':1791625424233},open(C/'novo-scid.json','w'),ensure_ascii=False,indent=1)
json.dump(P,open(C/'propostas.json','w'),ensure_ascii=False,indent=1)
print(len(P),'itens de conteúdo;2interface permanecem pendentes reais')
