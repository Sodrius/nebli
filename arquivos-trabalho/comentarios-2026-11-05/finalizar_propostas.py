import runpy,json,re
from pathlib import Path
C=Path(__file__).parent;ctx=runpy.run_path(str(C/'complementar.py'));P=ctx['P'];N=ctx['N'];set_=ctx['set_']
for n in json.load(open(C/'familia-bm52.json')):N.setdefault(n['noteId'],n)
for nid,extra in {
1791631343342:'H1 binds linker DNA near the nucleosome entry and exit sites, stabilizing local DNA organization and promoting compaction. It is a linker histone, not part of the core histone octamer.',
1791631343467:'Lysine and arginine side chains are positively charged at physiological pH and interact with the negatively charged DNA phosphate backbone. This helps explain sequence-independent DNA packaging.',
1791631343592:'Exposed histone tails are accessible to modifying enzymes. Acetylation neutralizes lysine charge and can recruit acetyl-lysine readers, altering both physical contacts and regulatory protein binding.',
1791631343715:'Pioneer factors can recognize selected sites in nucleosomal DNA and help recruit chromatin-modifying machinery. Replication also creates a temporary opportunity to compete with nucleosome assembly.',
1791631345367:'Recruiting HDACs removes histone acetyl groups and can favor a less accessible local chromatin state. Repression can therefore work through chromatin rather than direct competition with RNA polymerase.',
1791631346366:'An unmethylated CpG-rich promoter can remain accessible to regulatory proteins. Methylation at such a promoter can interfere with factor binding and recruit methyl-CpG readers and corepressors.',
1791631346967:'During replication, maintenance methylation restores methylation on the new DNA strand, while reader–writer interactions help propagate some histone-mark patterns. These mechanisms support cellular identity without changing nucleotide sequence.',
1791631347767:'Defined transcription factors can reset a fibroblast gene-regulatory network toward pluripotency. Reprogramming changes which genes are active, rather than replacing the fibroblast genome with a new DNA sequence.',
1792082177137:'A bromodomain is a protein module that recognizes acetylated lysines. It helps recruit associated transcription or chromatin-regulating proteins to marked nucleosomes, linking a chemical modification to a regulatory effect.',
}.items():
 set_(nid,extra=extra,reason='Similar da família apontada em BM52: verso curto demais nomeava efeito sem explicar o passo causal. Acrescentado substrato/ação/consequência sem mudar alvo ou índice.')
# Não alterar silenciosamente a nota recém-entregue nem notas em tela; isso será conferido no apply.
P['1793301693418']['fields']['Extra']=N[1793301693418]['fields']['Extra']['value'].replace('max-width:676px','max-width:950px')
P['1791630906668']['fields']['Extra']+='<br><br><img src="nebli-0511-histo-cultura-foco.png" style="width:100%;max-width:950px;height:auto">'
P['1791625424233']['fields']['Extra']+='<br><br><img src="8246e29ed402d1087af107a0c864d6c1.webp" style="width:100%;max-width:950px;height:auto">'
# A preferência local por ausência de iniciais é persistida para não ser anulada por outro executor.
for nid,pref in {1793784423639:'Davi: tirar iniciais nesse caso (comentário05/11).',1793476864207:'Davi: não precisa das iniciais também, entrega mt (04/11).',1793784421465:'Siglas IgE/IgG não recebem inicial; manter quatro efetores concisos,05/11.'}.items():P[str(nid)]['dicas_preferencia_davi']=pref
new=json.load(open(C/'novo-scid.json'))
new['fields']['Text']='<div data-nebli-organizacao="true"><b>SCID: core mechanisms</b><br><b>Common cytokine receptor chain</b>: {{c1::IL2RG}}<br><b>Toxic purine metabolites</b>: {{c1::ADA}}<br><b>Failed receptor recombination</b>: {{c1::RAG1/2}}</div>'
# Deixar a amplitude pedida no próprio apoio da nota de origem, não só em uma nota nova distante.
P['1791625424233']['fields']['Extra']+='<br><br><b>SCID reference, IUIS 2024</b>'+new['fields']['Extra'][new['fields']['Extra'].index('<table>'):]
json.dump(new,open(C/'novo-scid.json','w'),ensure_ascii=False,indent=1)
json.dump(P,open(C/'propostas.json','w'),ensure_ascii=False,indent=1)
# Manifesto inclui os nove similares adicionais em seu estado original integral.
json.dump(list(N.values()),open(C/'notas-antes-com-similares.json','w'),ensure_ascii=False,indent=1)
print(len(P),'notas preparadas, incluindo9similares; novoorganizadorSCID separado')
