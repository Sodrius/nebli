"""Revisão editorial delimitada: prepara mudanças a partir do snapshot vivo, sem escrever no Anki."""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
snap = {s: json.loads((HERE / f'{s}-snapshot.json').read_text()) for s in ('fa01','rd02','pt03','mb34','mb39')}
changes = {}

def change(short, key, text=None, extra=None, color=None, reason=''):
    data = snap[short]
    nid = next(n['nid'] for n in data['receipt']['notes'] if n['key'] == key)
    note = next(n for n in data['notes'] if n['noteId'] == nid)
    m = changes.setdefault(nid, {'nid': nid, 'short': short, 'key': key, 'fields': {}, 'corrigido': False,
        'comentario_visto': note['fields'].get('NEBLI_Comentario',{}).get('value',''), 'familia':'revisao-pontual-2026-10-12', 'motivo': ''})
    if text is not None:
        old = note['fields']['Text']['value']
        assert set(re.findall(r'\{\{c(\d+)::',old)) == set(re.findall(r'\{\{c(\d+)::',text)), (short,key)
        m['fields']['Text'] = text
    if extra is not None: m['fields']['Extra'] = extra
    if color: m['cor'] = {'aula':data['plan']['lesson_id'], 'cor':color}
    m['motivo'] += ('; ' if m['motivo'] else '') + reason

im = lambda name: f'<img src="fa01-g-{name}.png"><br>'
graph = {
 'g-potencia': ('potencia', 'Which drug is <b>most potent</b>? {{c1::A}}', '- A has the lowest EC<sub>50</sub>, read at half of its own maximal response.<br>- A and B reach the same plateau despite different potencies.'),
 'g-eficacia': ('potencia', 'Which drugs have the <b>same maximal efficacy</b>? {{c1::A and B}}', '- A and B reach the same plateau. C reaches a lower maximum.<br>- Compare plateau height for efficacy and EC<sub>50</sub> for potency.'),
 'g-inverso': ('agonismo', 'The <b>red diamonds and purple triangles</b> represent {{c1::inverse agonists}}', '- Both curves fall below the basal response, indicating suppression of constitutive activity.<br>- The flat blue curve represents a neutral antagonist.'),
 'g-neutro': ('agonismo', 'The <b>blue triangles</b> represent a {{c1::neutral antagonist}}', '- Basal activity remains unchanged as concentration increases.<br>- An inverse agonist would lower activity below baseline.'),
 'g-parcial': ('agonismo', 'The <b>green squares</b> represent a {{c1::partial agonist}}', '- The plateau is lower than that of the full agonist shown in black.<br>- The value near 50% belongs to this example; partial agonists do not all have a 50% maximum.'),
 'g-competitivo': ('antagonismo', 'Which type of <b>antagonism</b> is shown in the upper graph? {{c1::Competitive}}', '- The agonist curve shifts right, but its maximum is preserved.<br>- A higher agonist concentration overcomes the blockade.'),
 'g-naocompetitivo': ('antagonismo', 'Which type of <b>antagonism</b> is shown in the lower graph? {{c1::Noncompetitive}}', '- The maximum falls despite increasing the agonist concentration.<br>- The upper graph instead shows a surmountable, competitive blockade.'),
 'g-quantal': ('quantal', 'Which curves determine the <b>therapeutic index</b>? {{c1::Therapeutic and toxic}}', '- Read ED<sub>50</sub> and TD<sub>50</sub> at 50% of individuals, then calculate TD<sub>50</sub>/ED<sub>50</sub>.<br>- This is a population response, not half of the maximal effect in one person.'),
}
for key,(img,t,e) in graph.items(): change('fa01',key,im(img)+t,e,reason='Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no Extra. Mesmos IDs/clozes.')
change('fa01','alvo-sem-endereco','A drug can cause <b>adverse effects</b> by acting on its target in {{c1::other tissues}}', '- Target distribution helps explain why the desired effect may be accompanied by effects elsewhere.', reason='Troca a lacuna genérica choose por relação farmacológica recuperável; lâminas 24/35.')
change('fa01','gpcr','{{c1::<b>G protein–coupled</b>}} receptors transmit extracellular {{c2::ligand}} binding to heterotrimeric G proteins inside the cell', '- Receptor activation couples an extracellular signal to intracellular enzymes or ion channels.',reason='Corrige generalização bind glycoproteins na cópia NEBLI e retira patologias laterais do Extra; IUPHAR Receptors. Original preservado.')
change('fa01','rtk',extra='- Ligand binding activates receptor kinase signaling and phosphorylation of intracellular proteins.',reason='Retira generalização de dimerização que não descreve corretamente todos os receptores do exemplo; mantém princípio da lâmina 25.')
change('fa01','gc',extra='- NO activates soluble guanylyl cyclase → increased cGMP → smooth-muscle relaxation.',reason='Extra passa a explicar a cadeia da aula, sem farmacoterapia de hipertensão pulmonar.')
change('fa01','bupre',extra='- A partial agonist produces a lower maximal receptor response than a full agonist.<br>- Buprenorphine illustrates this property at μ-opioid receptors.',reason='Retira conduta de início de tratamento; conserva conexão com agonismo parcial.')
change('fa01','atropina',extra='- Atropine illustrates competitive antagonism at muscarinic receptors.<br>- The receptor subtype matters: nicotinic effects are not blocked by atropine.',reason='Mantém exemplo cobrado em prova e mecanismo; retira sequência terapêutica lateral.')
for key in ['nitro-prodroga','nitrato-tolerancia','pde5','manitol','h1-inverso','bupre','bupre-abstinencia','varfarina-fenobarbital','it-baixo','anestesico-na','gq','gs','gi']:
    change('fa01',key,color='rosa',reason='Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não impõe proporção de cores.')

change('rd02','mais-barato','Among <b>clinically appropriate imaging tests</b> that answer the same question, prefer the {{c1::less costly}} option', '- Diagnostic adequacy and patient safety come before cost.<br>- A more expensive or technologically complex test is not automatically better.',reason='Conserva princípio econômico da aula, condicionado à adequação clínica; elimina cheapest como critério absoluto.')
change('rd02','ruq-us','For suspected <b>biliary disease</b> causing right upper quadrant pain, the usual first imaging test is {{c1::ultrasound::modality}}','- The initial choice follows the diagnostic hypothesis.<br>- Further imaging depends on the ultrasound findings and the clinical scenario.',reason='Restringe cópia NEBLI ao caso da aula; retira regra falsa other quadrants use CT. ACR Right Upper Quadrant Pain.')
change('rd02','radiacao-gravidez','During <b>pregnancy</b>, ultrasound or MRI is preferred when it can answer the clinical question without {{c1::ionizing radiation}}','- A necessary radiograph or CT may still be appropriate when its diagnostic benefit outweighs the risk.<br>- Risk depends on the examination, fetal dose and stage of pregnancy.',reason='Evita ensinar gestação como contraindicação absoluta a RX/TC; ACR/RSNA CT safety during pregnancy.')
change('rd02','rx-contraste-baixo',extra='- Soft tissues may have similar X-ray attenuation and overlap in a projection image.<br>- CT separates structures into cross-sectional images.',reason='Retira comparação absoluta incorreta entre resolução espacial de RX e TC; explica limitação por contraste/sobreposição.')
change('rd02','angio-radiacao-iodo','Catheter <b>angiography</b> uses X-rays and {{c1::iodinated}} contrast injected into the vessel being examined','- Contrast outlines the vessel lumen.<br>- The injection route depends on the vessel and procedure.',reason='Corrige intravenous como rota universal da angiografia por cateter; coerência com card angio-def da própria aula.')
change('rd02','rx-primeira-linha','Low cost and wide {{c1::availability}} make <b>plain radiography</b> useful as an initial test for suitable clinical questions','- The initial test depends on the suspected condition; radiography is not first-line for every region or complaint.',reason='Elimina generalização first exam in most situations; preserva vantagem logística ensinada.')

change('pt03','etiologia-multipla',extra='- Genetic susceptibility and environmental exposures can contribute together to a disease.',reason='Evita misturar mecanismos de formas diferentes de diabetes no mesmo exemplo.')
change('pt03','fna-tireoide','Which sampling method obtains <b>isolated cells</b> from a thyroid nodule? {{c1::Fine-needle aspiration (FNA)}}','- The aspirate supports cytological evaluation.<br>- A tissue biopsy also preserves architecture, which isolated cells cannot fully show.',color='azul',reason='Recupera a ferramenta/citologia, não um algoritmo clínico de todo nódulo; retira must do because highly vascularized.')
change('pt03','he-primeiro','In routine <b>histopathology</b>, H&E provides the morphological context for selecting {{c1::special stains and ancillary tests}}','- H&E shows the overall tissue pattern.<br>- Additional methods answer a more specific diagnostic question.',reason='Remove always e torna explícita a função organizadora do H&E; lâminas 15/23.')
change('pt03','terapia-alvo','Selection of a <b>targeted cancer therapy</b> depends on identifying a suitable {{c1::molecular target}} in the tumor','- A relevant biomarker may involve protein expression or a genetic alteration.<br>- Receptor overexpression is one example, not a universal requirement.',reason='Corrige only overexpresses para o princípio geral de seleção por alvo; NCI Biomarker Testing.')
change('pt03','oil-red',extra='- Lipid stains answer a specific compositional question that routine morphology may not resolve.',reason='Retira comparação McArdle/MCAD alheia ao objetivo introdutório.')
change('pt03','pas-glicogenio',extra='- PAS highlights carbohydrate-rich structures; interpret the staining pattern in its tissue context.',reason='Retira comparação de doenças metabólicas usada como expansão lateral.')
for key in ['pneumonia-patogenese','picrosirius','elastica','bh','melanina','ihq-24h','hormonioterapia']:
    change('pt03',key,color='rosa',reason='Detalhe ou aplicação específica; não substitui recuperação do princípio da ferramenta. Harmoniza com a revisão de escopo.')
for key in ['biopsia-def','histoquimica-def','ihq-vs-histo','he-principal']:
    change('pt03',key,color='verde',reason='Conceito organizador duradouro das ferramentas diagnósticas explicitamente ensinado, antes das listas de corantes.')

change('mb34','tn3',color='rosa',reason='Associação nominal Tn3–ampicilina é detalhe, como Tn5/Tn9/Tn10; mecanismo geral permanece.')
change('mb34','planar-etidio','Planar <b>DNA mutagens</b> can {{c1::intercalate}} between adjacent base pairs','- Ethidium bromide is an example.<br>- Insertion between base pairs distorts the DNA structure and can disrupt accurate replication.',reason='Troca nome específico do exemplo por mecanismo ensinável; exemplo passa ao Extra.')

change('mb39','conjuntiva-esteril','The healthy <b>conjunctiva</b> has a {{c1::low}} bacterial biomass, limited by tears and local defenses','- Low bacterial abundance does not mean absolute sterility.<br>- Tears and lysozyme help limit colonization.',reason='Corrige contradição esterilidade/microbiota no slide 8; estudo primário PMC5054734. Divergência com fonte docente registrada.')
change('mb39','vias-inferiores','Microbes in healthy <b>lower airways</b> reflect a balance between immigration and {{c1::elimination}}','- Healthy lungs can contain low-biomass microbial communities.<br>- Detection of microbes alone does not establish infection.',reason='Corrige esterilidade absoluta do slide 8; estudo primário Dickson et al. 2015, PMC4590020.')
change('mb39','esofago','The <b>esophageal microbiota</b> is closely linked to microorganisms from the {{c1::oral cavity}}','- Swallowed saliva contributes organisms, and bacteria can also associate with the esophageal mucosa.<br>- It is not accurate to describe the healthy esophagus as lacking a microbiota.',reason='Remove ausência absoluta de microbiota; estudo primário PNAS 2004, PMC384727.')
for key in ['pele-oito-horas','estabilidade-2anos','intestino-orgao-imune','typhoid-mary','typhi-vesicula']:
    change('mb39',key,color='rosa',reason='Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de recolonização, maturação, imunidade e portador.')

rows=list(changes.values())
for m in rows:
    n=next(n for n in snap[m['short']]['notes'] if n['noteId']==m['nid'])
    m['before']={k:n['fields'][k]['value'] for k in m['fields']}
    m['fields']={k:v for k,v in m['fields'].items() if v!=n['fields'][k]['value']}
(HERE/'mudancas.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('Notas:',len(rows),'com campos:',sum(bool(m['fields']) for m in rows),'com cor:',sum('cor' in m for m in rows))
