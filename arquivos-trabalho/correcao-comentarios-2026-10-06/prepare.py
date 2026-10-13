"""Plano editorial com precondições; não escreve na coleção."""
import html, json, re
from pathlib import Path
P=Path(__file__).resolve().parent
N={n['noteId']:n for n in json.loads((P/'snapshot.json').read_text())}
C={}
def clean(s): return html.unescape(re.sub('<[^>]+>','',s))
def put(nid, reason, **fields):
    c=C.setdefault(nid,{'nid':nid,'fields':{},'reasons':[]})
    c['fields'].update(fields); c['reasons'].append(reason)
def value(nid,k): return C.get(nid,{}).get('fields',{}).get(k,N[nid]['fields'].get(k,{}).get('value',''))
def img(n): return f'<img src="{n}" style="width:100%;max-width:760px;height:auto">'
def crop(name,size,box):
    w,h=size; x,y,x1,y1=box; cw,ch=x1-x,y1-y
    return (f'<div style="width:100%;max-width:760px;margin:12px auto;background:white"><div style="position:relative;height:0;padding-bottom:{100*ch/cw:.4f}%;overflow:hidden">'
      f'<img src="{name}" style="position:absolute;left:{-100*x/cw:.4f}%;top:{-100*y/ch:.4f}%;width:{100*w/cw:.4f}%;max-width:none;height:auto;margin:0"></div></div>')
def replace_media(nid,old,replacement):
    s=value(nid,'Extra')
    s=re.sub(r'<img\b[^>]*src="'+re.escape(old)+r'"[^>]*>',lambda m:replacement,s)
    put(nid,'Imagem focal por alvo; todos os usuários do asset conferidos',Extra=s)
saliva='09b1a4ed4f6059189a53ef4cad0f4753.webp'
gastric='b8647af3199815237f7622aff1f2a0fc.webp'
stomach='82605678fa1ed99d7ea5012425fc98d3.webp'
wall='7622bdccaa72d53bb3fae2ccf397d414.webp'
saliva_micro=crop('64488be5c84f06ac3036fdb6d536e599.webp',(800,743),(25,54,777,596))
gland_map=crop(gastric,(838,806),(479,62,821,540))
gland_neck=crop(gastric,(838,806),(245,65,468,282))
gland_base=crop(gastric,(838,806),(245,315,468,532))
for nid,n in N.items():
    e=value(nid,'Extra'); t=clean(value(nid,'Text')).lower()
    if saliva in e:
        if nid in [1791023354943,1791023355193]: replacement=crop(saliva,(805,1036),(20,50,483,378))
        elif nid in [1791023355444,1791023355691]: replacement=saliva_micro
        else: replacement=crop(saliva,(805,1036),(89,435,752,899))
        replace_media(nid,saliva,replacement)
    if gastric in e:
        if nid in [1791023364242,1791023365216,1791023365342]: replacement=gland_neck+'<br>P = parietal cells; MN = mucous neck cells.'
        elif nid in [1791023366191,1791023364368]: replacement=gland_base+'<br>C = chief cells; P = parietal cells.'
        elif nid==1790979869685:
            replacement='<div style="margin:12px;padding:14px;border:1px solid #888"><b>Inactive pepsinogen</b><br>↓ acidic lumen (H⁺)<br><b>Active pepsin</b><br>↳ activates additional pepsinogen</div>'
        elif nid in [1790979869860,1790979869985]:
            replacement='<div style="margin:12px;padding:14px;border:1px solid #888">Gastric ghrelin-producing cells<br>↓ <b>Ghrelin</b> in blood<br>Hypothalamus → increased hunger</div>'
        else: replacement=gland_map
        replace_media(nid,gastric,replacement)
    if stomach in e:
        if nid==1791023359968: replacement=crop(stomach,(820,1073),(29,57,433,355))
        elif nid==1791023360093: replacement=crop(stomach,(820,1073),(503,65,791,349))+'<br>SSE = stratified squamous epithelium; SCE = simple columnar epithelium.'
        else: replacement=gland_map
        replace_media(nid,stomach,replacement)
    if wall in e: replace_media(nid,wall,img('7622bdccaa72d53bb3fae2ccf397d414-fig.png'))

# Extend the same correction to the other uncropped Histology plates.
other_figures={
 '6e1e3b85249102df0664479f1efb5aeb.webp':((830,609),(423,49,821,421)),
 '1b3fc87ec26531c1902e37a90ab4ff4e.webp':((824,602),(24,49,433,406)),
 'b0851a2140d498e6d50ed510872ea463.webp':((805,728),(405,45,780,524)),
 'd53e657d95d2f6b96fe890a968e35433.webp':((831,1048),(25,51,444,795)),
 'af33d44aedf39b5bcaf1b000e33152e2.webp':((838,555),(238,60,506,348)),
 'a202aeb70c2f6e8e031a95973bc68dcd.webp':((424,831),(24,62,390,603)),
 '554c8d3da0529d0bc996acd9274cce28.webp':((818,1071),(30,56,436,352)),
 '0ea69ec09ba66f649f6492be0f15b691.webp':((838,542),(42,53,516,423)),
 'bab2cd252996a82212da70cf3d90e068.webp':((826,915),(29,51,798,687)),
}
for nid,n in N.items():
    for asset,(size,box) in other_figures.items():
        if asset in value(nid,'Extra'):
            replace_media(nid,asset,crop(asset,size,box))
put(1791023353192,'Mucosa mastigatória exige mucosa queratinizada, não visão geral do sistema',Extra='- Gingiva and hard palate have abrasion-resistant <b>masticatory mucosa</b>.<br>- In this periodontal section, <b>FG</b> marks the gingival epithelium next to the tooth.'+crop('af33d44aedf39b5bcaf1b000e33152e2.webp',(838,555),(25,60,220,348)))
put(1791023357791,'Camada da glândula identificável no mapa em vez de panorama sem glândula nítida',Extra='- <b>Esophageal glands proper</b> lie in the submucosa and lubricate the lumen.<div style="padding:14px;border:1px solid #888">Lumen<br>Stratified squamous epithelium<br>Lamina propria<br>Muscularis mucosae<hr><b>Submucosa → esophageal glands proper → duct to lumen</b><hr>Muscularis externa</div>')
put(1791023357017,'Indicar explicitamente as setas da muscular da mucosa',Extra=value(1791023357017,'Extra')+'<br>- The <b>arrows</b> mark muscularis mucosae, between mucosa (M) and submucosa (SM).')
put(1791023354569,'Ler a relação entre cemento e osso no recorte',Extra=value(1791023354569,'Extra')+'<br>- <b>L</b> = ligament; <b>C</b> = cementum; <b>B</b> = alveolar bone.')

axon=value(1791023270317,'Extra')
put(1791023270196,'Figura anterior mostrava contração, não varicosidades',Extra=axon)
put(1791023270450,'Mostrar propagação por junções, não foto genérica de contração',Extra='- <b>Gap junctions</b> let electrical current pass directly between neighboring smooth muscle cells.<div style="padding:14px;border:1px solid #888">Depolarized muscle cell<br>↓ gap junctions<br>Neighboring muscle cells depolarize<br>↓<br>Coordinated contraction</div>')
put(1791023357394,'Explicitar a camada microscópica que o panorama não resolve',Extra='- <b>Mesothelium</b> is the thin outer epithelial sheet of the serosa.<div style="padding:14px;border:1px solid #888">Peritoneal cavity<br>──────── <b>Mesothelium</b> (simple squamous cells)<br>Loose connective tissue<br>──────── Muscularis externa</div>')
for nid in [1790999833204,1790999833329]: replace_media(nid,'nebli-uc08-fi09-p03f.png',img('8c95b6838315e860024bc9caae2bcae1.png'))
put(1790999832528,'Imagem AnKing da relação entre ondas, spikes e contração',Extra=value(1790999832528,'Extra')+'<br>'+img('8c95b6838315e860024bc9caae2bcae1.png'))
put(1790999835379,'Esquema focal do fluxo retrógrado, substitui slide ilegível',Extra='- When an antral contraction reaches the closed pylorus, chyme is driven backward and ground into smaller particles.<div style="padding:14px;border:1px solid #888"><b>Stomach body ← chyme ← contracting antrum │ closed pylorus</b><br>Backward jet = retropulsion</div>')
for nid in [1790999837929,1790999838053,1790999838179]:
    replace_media(nid,'nebli-uc08-fi09-p12f.png','<div style="padding:14px;border:1px solid #888"><b>Haustral contractions</b><br>Local back-and-forth mixing → water absorption<hr><b>Mass movements</b><br>Long colonic segment → rectum<br>Often increased after a meal (gastrocolic response)</div>')

texts={
1791000311952:'Dietary {{c1::<b>heme</b>}} contains iron within a {{c2::<b>porphyrin</b>}} ring and can be absorbed intact by enterocytes.',
1791014714399:'The {{c1::<b>gastric</b>}} phase accounts for about 60% of meal-stimulated HCl secretion.',
1791014714525:'During the {{c1::<b>gastric</b>}} phase, stomach distension and nutrients stimulate acid secretion through neural reflexes and gastrin.',
1784308062596:'O elemento morf/o indica {{c1::<b>forma</b>}}.',
1791054014447:'GLP-1 stimulates {{c1::<b>insulin</b>}} secretion and inhibits {{c1::<b>glucagon</b>}} secretion.',
1791142466364:'Pulmonary congestion from {{c3::<b>left</b>}} ventricular failure produces {{c1::<b>hemosiderin-laden macrophages</b>}}, also called {{c2::<b>heart failure</b>}} cells.',
1790974697781:'Above the pectinate line, superior rectal venous drainage reaches the {{c1::<b>portal</b>}} circulation.',
1790974698282:'Below the pectinate line, inferior rectal venous drainage reaches the {{c1::<b>systemic</b>}} circulation.',
1791000305327:'Pancreatic α-amylase is secreted in its {{c1::<b>active</b>}} form.',
1791022169456:'Cavernous hepatic hemangiomas are usually {{c1::<b>asymptomatic</b>}} and discovered incidentally.',
1791023355444:'Salivary cells with <u>round nuclei and protein-rich apical granules</u> are {{c1::<b>serous</b>}} cells.',
1791023819869:'During peristalsis, circular muscle immediately <u>behind the bolus</u> {{c1::<b>contracts</b>}}.',
1790999833204:'At the crest of a GI slow wave, crossing the <b>electrical threshold</b> triggers {{c1::<b>spike potentials</b>}}.',
1790999838053:'Strong colonic contractions that propel contents over long distances toward the rectum are called {{c1::<b>mass movements</b>}}.',
1791054012719:'Chronic <b>hyperinsulinemia</b> can {{c1::<b>downregulate</b>}} insulin receptors.',
1791054011545:'In type 1 diabetes, insulin deficiency permits unopposed {{c1::<b>glucagon</b>}} action and promotes breakdown of stored fuels.',
1791054007644:'Polyuria, polydipsia and unexplained weight loss suggest {{c1::<b>diabetes mellitus</b>}}.',
1791054012320:'In diabetes, glucose retained in the renal tubules causes {{c1::<b>osmotic diuresis</b>}}, producing polyuria and thirst.',
1791054012596:'As pancreatic β-cell function declines in advanced type 2 diabetes, insulin secretion {{c1::<b>decreases</b>}}.',
1791054012447:'In hyperosmolar hyperglycemic state, residual {{c1::<b>insulin</b>}} usually suppresses substantial ketone production.',
1791054012198:'Diabetic ketoacidosis causes metabolic acidosis with an {{c1::<b>increased</b>}} anion gap.',
1791054012972:'Insulin resistance is particularly associated with excess {{c1::<b>visceral</b>}} adipose tissue.',
1791054007769:'With classic hyperglycemic symptoms, random plasma glucose ≥ {{c1::<b>200</b>}} mg/dL establishes diabetes.',
1791054010347:'Compared with type 2 diabetes, type 1 diabetes has a {{c1::<b>weaker</b>}} genetic predisposition.',
1791054010470:'Compared with type 1 diabetes, type 2 diabetes has a {{c1::<b>stronger</b>}} genetic predisposition.',
1791163038218:'In ordinary F⁺ × F⁻ conjugation, the donor transfers its {{c1::<b>F plasmid</b>}}.',
1791147099604:'Airway mucus helps clear inhaled particles by {{c2::<b>trapping</b>}} them.',
1791147110810:'Cilia transport airway mucus toward the pharynx through the {{c2::<b>mucociliary escalator</b>}}.',
1791147096336:'Alveolar macrophages engulf inhaled {{c2::<b>particles</b>}} that reach the alveoli.',
1791147111912:'{{c2::<b>Alveolar macrophages</b>}}, also called {{c1::<b>dust</b>}} cells, remove particles from alveolar air spaces.',
1791147113641:'Macrophages remove cellular debris and microbes through {{c1::<b>phagocytosis</b>}}.',
1791023360742:'Compared with fundic glands, typical mucous pyloric glands contain fewer {{c1::<b>parietal</b>}} and {{c2::<b>chief</b>}} cells.',
1791023256867:'Gastric acid secretion is stimulated locally by ECL-cell {{c1::<b>histamine</b>}} and hormonally by G-cell {{c2::<b>gastrin</b>}}.',
1790972066759:'Identify the highlighted gastric region.<br>{{c1::<b>Pylorus</b>}}',
1790974691531:'Colonic diverticula containing mucosa and submucosa but not the full muscular wall are {{c1::<b>false</b>}} diverticula.',
1790972068785:'The SMA can compress the {{c1::<b>third</b>}} part of the duodenum against the aorta.',
1790974697657:'Above the pectinate line, the rectum is supplied mainly by the {{c1::<b>superior rectal</b>}} artery.',
1790974698156:'Below the pectinate line, the anal canal is supplied by the {{c1::<b>inferior rectal</b>}} artery.',
1790981518578:'{{c2::<b>Esophageal varices</b>}} form at the portosystemic connection between the {{c1::<b>left gastric</b>}} and {{c1::<b>azygos</b>}} venous systems.',
1791000312427:'Duodenal uptake of non-heme Fe²⁺ uses the transporter {{c1::<b>DMT1</b>}}.',
1791000316027:'After a meal, SGLT1-mediated absorption can increase paracellular permeability by activating {{c1::<b>MLCK</b>}}.',
1790979863287:'The esophagus is lined by {{c1::<b>nonkeratinized stratified squamous</b>}} epithelium.',
1791054009046:'An autoimmune marker of <b>type 1 diabetes</b> is the presence of {{c3::<b>anti-GAD</b>}} antibodies.',
1784308059865:'Em leucocitose, -citose indica {{c1::<b>aumento</b>}} do número de células.',
1784308073461:'Na pancitopenia, estão reduzidas {{c1::<b>todas</b>}} as principais linhagens celulares do sangue.',
1784308073600:'Em pielonefrite, piel/o identifica a {{c1::<b>pelve renal</b>}}.',
1784308073615:'Hidrouréter é a {{c1::<b>dilatação</b>}} do ureter por acúmulo de urina.',
1784308073622:'Hidronefrose é a {{c1::<b>dilatação</b>}} do sistema coletor renal.',
1784308075908:'Gliconeogênese produz {{c1::<b>glicose</b>}} a partir de precursores não glicídicos.',
}
for nid,t in texts.items():
    old=value(nid,'Text')
    # Preserve any visual prompt embedded in the original front.
    if nid==1790972066759: t+=''.join(re.findall(r'<img[^>]+>',old))
    put(nid,'Recuperação focal, contexto discriminante, sem oposição que entregue a resposta',Text=t)
put(1791054012719,'Não reduzir resistência insulínica exclusivamente ao número de receptores',Extra='- Obesity alters insulin signaling at receptor and post-receptor steps.<br>- Lipid excess and inflammatory signals interfere with insulin action in muscle, liver and adipose tissue.<br>- Receptor downregulation alone does not explain the full defect.')
put(1791000316027,'Expandir sigla no verso',Extra=value(1791000316027,'Extra')+'<br>- <b>MLCK</b> = myosin light chain kinase, which regulates the perijunctional actomyosin ring.')
put(1791054012596,'Preservar a sequência precoce/tardia no apoio',Extra='- <b>Early</b> insulin resistance can be compensated by increased insulin secretion.<br>- <b>Later</b> β-cell dysfunction limits this compensation, worsening hyperglycemia.')
put(1790972066759,'Verso curto para identificação visual',Extra='- The <b>pyloric region</b> is the distal stomach, leading toward the duodenum.<br>- The pyloric sphincter regulates passage through the pyloric opening.'+value(1790972066759,'Extra'))
put(1791054007769,'Limiar correto, sintomas necessários e sem classificar o tipo só pela glicemia',Extra='- Classic symptoms include polyuria, polydipsia and unexplained weight loss.<br>- Without unequivocal symptomatic hyperglycemia, confirm the diagnosis with appropriate repeat testing.<br>- This glucose criterion establishes diabetes, not its type.')
put(1790999833204,'Relacionar os dois limiares sem absoluto falso sobre ondas lentas',Extra='- A <b>slow wave</b> is a graded oscillation in membrane potential.<br>- Sufficient depolarization triggers spikes, increasing Ca²⁺ entry and contraction strength.<br>- Electrical and contractile activity are related, but slow waves are not themselves spikes.'+img('8c95b6838315e860024bc9caae2bcae1.png'))
put(1791023256867,'Histamina parácrina versus gastrina endócrina',Extra='- <b>ECL cells → histamine</b>: local paracrine signal to H₂ receptors.<br>- <b>G cells → gastrin</b>: hormone carried through blood, also stimulating ECL cells.'+gland_map)
put(1791023360742,'Evitar ausência absoluta incorreta em histologia humana',Extra='- The typical pyloric gland is predominantly mucous.<br>- Human antral mucosa can include mixed glands containing parietal and chief cells; absolute absence is too strong.'+gland_map)

# Synonyms and explanatory parentheses belong in Extra, not in the recall target.
short={
1790972065186:('inferior vena cava (IVC)','inferior vena cava'),
1790972064937:('Instrumental perforation (namely endoscopy)','Instrumentation'),
1790972067760:('Lesser curvature of stomach','Lesser curvature'),
1790972069313:('Hepatopancreatic sphincter (Sphincter of Oddi)','Sphincter of Oddi'),
1790972069412:('hepatopancreatic ampulla (ampulla of Vater)','hepatopancreatic ampulla'),
1790980913728:('Brunner glands (in submucosa)','Brunner glands'),
1790981525201:('inferior mesenteric artery (IMA)','inferior mesenteric artery'),
1790999834379:('Vagus nerve (CN X)','Vagus nerve'),
1790999833579:('Mandibular branch of trigeminal (V3)','V3'),
1790999837629:('migrating motor complexes (MMCs)','migrating motor complexes'),
1790999835004:('Vasoactive intestinal peptide (VIP)','VIP'),
1791000304527:('Tight junctions (zonula occludens)','Tight junctions'),
1791000314677:('proximal convoluted tubule (PCT)','proximal convoluted tubule'),
1791014717724:('gastrin-releasing peptide (GRP, bombesin)','gastrin-releasing peptide'),
1791022169576:('females of reproductive age','reproductive-age women'),
1791054009046:('anti-glutamic acid decarboxylase (anti-GAD)','anti-GAD'),
1791054010873:('hyperosmolar hyperglycemic state (HHS)','hyperosmolar hyperglycemic state'),
1791054016721:('amylin (islet amyloid polypeptide)','amylin'),
1791054020545:('Charcot joint (neurogenic arthropathy)','Charcot joint'),
1791069774161:('Polyenes (e.g. nystatin, amphotericin B)','Polyenes'),
1791141203017:('Congestive heart failure (CHF)','Heart failure'),
1791141202410:('decompensated right heart failure','right-sided heart failure'),
1791147097386:('alveolar macrophages (dust cells)','alveolar macrophages'),
}
for nid,(old,new) in short.items():
    t=value(nid,'Text')
    def sub(m):
        body=clean(m[2]).strip()
        return '{{c'+m[1]+'::<b>'+new+'</b>}}' if body==old else m[0]
    updated=re.sub(r'\{\{c(\d+)::(.*?)(?:::[^}]*)?\}\}',sub,t)
    if updated!=t:
        put(nid,'Cloze curto; sinônimo/detalhe permanece no verso',Text=updated,Extra=value(nid,'Extra')+'<br>- '+old+'.')

# Economical answer emphasis in all unformatted authored/adapted cards.
for nid,n in N.items():
    t=value(nid,'Text')
    if nid not in {1791169086906,1791169090157,1791199623249,1791169090497,1791169090650} and any(x in n['tags'] for x in ['NEBLI::origem::Autoral','NEBLI::origem::Histology']) and t and not re.search(r'<(?:b|strong|u)\b',t):
        t=re.sub(r'(\{\{c\d+::)([^{}]*?)(\}\})',lambda m:m[1]+'<b>'+m[2]+'</b>'+m[3],t)
        put(nid,'Ênfase econômica no termo recuperado, como nos exemplos AnKing',Text=t)

def finish():
    for nid,c in C.items():
        comment=N[nid]['fields'].get('NEBLI_Comentario',{}).get('value','')
        if comment and 'CORRIGIDO' not in comment and 'gostei' not in comment and 'imagem top' not in comment:
            c['fields']['NEBLI_Comentario']=comment+'<br>CORRIGIDO, 06/10/2026.'
        c['fields']={k:v for k,v in c['fields'].items() if v!=N[nid]['fields'][k]['value']}
        c['before']={k:N[nid]['fields'][k]['value'] for k in c['fields']}
    changes=[c for c in C.values() if c['fields']]
    (P/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
    print('Mudanças',len(changes))
if __name__=='__main__': finish()
