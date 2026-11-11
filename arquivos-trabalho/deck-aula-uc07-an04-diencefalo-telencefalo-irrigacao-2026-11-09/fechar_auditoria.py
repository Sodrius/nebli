"""Sincroniza os artefatos com a auditoria real de11/11; não aprova pareceres."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parent;P=json.loads((R/'plan.json').read_text())
def load(n):return json.loads((R/n).read_text())
def save(n,v):(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=1))
M=load('matriz-fontes.json');es=load('escopo.json');provas=[x for x in M['linhas'] if x['fonte']=='prova']
es['uso_das_fontes']['prova']=list(dict.fromkeys(k for x in provas for k in x['cards']))
es['provas']=[{'id':x['ref'],'cards':x['cards'],'conferencia':x['recuperacao']} for x in provas]
es.pop('provas_ausentes',None);save('escopo.json',es)
cov=load('cobertura.json');cov['itens'] += [{'id':'prova-'+x['ref'],'fonte':'exercício/prova '+x['ref'],'cards':x['cards']} for x in provas];save('cobertura.json',cov)
fd=load('fontes-decl.json');fd['familias']['provas']={'estado':'consultada','arquivo':'fontes/provas-an04.txt','leitura':'recorte de17questões AN04 dos4PDFs recebidos11/11; originais integrais preservados em ../uc07-resumos-2026-11-11','contribuicao':'Vias direta/indireta, D1/D2, parkinsonismo, lesão talâmica, Meyer, Papez/fórnix, cápsula interna e Willis.'};save('fontes-decl.json',fd)
f=load('fontes.json');f['provas']=fd['familias']['provas'];save('fontes.json',f)
# Só imagens efetivamente abertas:13pares Machado pelo revisor,2novosKenhub,
# e182IOs compartilhados nas16pranchas que o executor abriu integralmente.
seen=load('imagens-vistas.json');allnotes=P['entries']+[dict(v,key='sh-'+n) for n,v in P['compartilhados'].items()]
for e in allnotes:
 if 'Nome PT' not in e['fields']:continue
 nome=e['fields']['Nome PT']
 for name in re.findall(r'src="([^"]+)"',' '.join(e['fields'].values())):
  seen[name]={'qualidade':'boa' if not e['key'].startswith('io-') else 'aceitável','intencao':f'Identificar {nome}; seta/linha-guia e resposta correspondem ao alvo, conferidas no render ou no par Q/R.','evidencia':'visual/io-shared/ (182 IOs); revisao-complementos-io-provas-1111.json; revisao-tuberculo-anterior-1111.json; auditoria-revisor-2026-11-11.md'}
save('imagens-vistas.json',seen)
# Este texto registra pré-instalação; a revisão do vivo é acrescentada depois.
md='''# Revisão de qualidade AN04 —11/11

Recorte: quatro transcrições e núcleos da base pela apostila, com62unidades. Não é um deck geral de neurofisiologia ou de todas as questões daUC07. A matriz editorial independente cruza267relações e17questões pertinentes com cards recuperáveis; detalhes de meninges/líquor/drenagem venosa ficam naAN06, e tronco/cerebelo/nervos pertencem àAN03.

As provas acrescentaram relações recuperáveis de vias direta/indireta, D1/D2, parkinsonismo, déficit sensitivo talâmico, alça deMeyer e Papez/fórnix. Recuperadas cópias existentes quando havia histórico. Corrigidos hipotálamo anterior/posterior, ramo ascendente, lóbulos parietais, labirinto, Broca, territórios daACP e conceito deestriado. Não se adotaram erros de gabarito sobre cápsula interna ou fibras dofórnix. Sulco central não é descrito como chegando obrigatoriamente ao sulco lateral.

Prioridade de imagens: Kenhub;13alvos semIOKenhub adequado usam figuras reais doMachado com rótulo oculto e linha-guia mantida. O arqueado é hipotalâmico. A seta herdada do tubérculo anterior caiu abaixo do término original na pranchaNetter: corrigida com recorte focal, sem resposta inglesa visível nafrente. Os182IOs compartilhados foram abertos nas16pranchas de render; as13duplasMachado e a correçãoNetter foram julgadas pelo revisor independente. Isso é inspeção visual, não inferência de correção apenas porcor/slug.

O deck completo e a fila deestudo têm conferências separadas: selecao-estudo.json guarda ordinais e fontes de prova/resumo para cada decisão ativa. Não se libera toda clínica porque o órgão foi nomeado. Giros/sulcos internos daínsula, redes capilares/partes finas da hipófise, ramos arteriais pequenos e síndromes não cobradas permanecem suspensos. Dor talâmica tardia c3/c4 também fica suspensa; c1/c2 entram pelaquestão6. Três avulsos redundantes preservados porID não ganham prioridade sobre IO/organizador/AnKing.

Pré-instalação:23autorais e85casos julgados pelo revisor único. A pré-checagem mecânica foi incorporada antes do pacote final; foram corrigidos vazamentos e negrito em critérios dos organizadores. Conferência viva, agendamento, suspensão e pacote serão registrados depois da instalação; este documento não os dá por feitos.
'''
(R/'REVISAO-DE-QUALIDADE.md').write_text(md)
print('Fontes/provas/cobertura/imagens e revisão sincronizados; sem aprovação automática.')
