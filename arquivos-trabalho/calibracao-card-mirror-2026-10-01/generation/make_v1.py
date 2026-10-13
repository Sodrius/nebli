import json
from collections import Counter
from pathlib import Path
from nebli.lint_cards import check

HERE = Path(__file__).resolve().parent
sources = {n['id']: n for n in json.loads((HERE.parent / 'authoring-reference.json').read_text())}
# source, front, Extra, factual target, exact supporting source excerpt, retrieval change
drafts = [
('1524247235026', 'How does <b>hypoglossal nerve stimulation</b> move the tongue in obstructive sleep apnea?<br><br>{{c1::Forward}}', '- Enlarges the <b>oropharyngeal airway</b>.', 'Direção do movimento da língua após estimular hipoglosso', 'stimulation of hypoglossal nerve causes the tongue to move forward slightly', 'Do nome do nervo/diâmetro para seu efeito motor explícito no Extra.'),
('1521423729086', 'Renal atrophy following <b>renal artery stenosis</b> results from chronic {{c1::ischemia}}.', '- Reduced oxygen and nutrient delivery.', 'Isquemia como causa da atrofia renal', 'This is due to ischemia to the kidney', 'Do desfecho atrofia para o mecanismo causal descrito no Extra.'),
('1550600491028', 'Which <b>spinal roots</b> are tested by the <b>biceps reflex</b>?<br><br>{{c1::C5–C6}}', '- The <b>musculocutaneous nerve</b> itself receives C5–C7 fibers.', 'Raízes avaliadas pelo reflexo bicipital', 'Biceps reflex = C5-C6 roots of the musculocutaneous nerve', 'Da inervação do músculo para a recuperação clínica do arco reflexo no Extra.'),
('1463526310251', 'The <b>ureter</b> passes {{c1::under::over or under}} the uterine vessels, placing it at risk during hysterectomy.', '', 'Relação ureter–vasos uterinos', 'the ureters travel <u>under</u> the uterine vessels', 'Da origem das artérias para a relação cirúrgica descrita no Extra.'),
('1468549172824', 'Which nucleases cleave <b>within</b> a DNA strand rather than at its ends?<br><br>{{c1::Endonucleases}}', '- <b>Exonucleases</b> act at the ends.', 'Endonucleases e clivagem interna', 'Whereas <b>endonucleases</b> cleave nucleotides <u>in the middle</u> of a DNA strand', 'Do alvo exonucleases para o contraste endonucleases presente no Extra.'),
('1496626848604', 'Volume restoration in <b>saline-responsive metabolic alkalosis</b> suppresses the {{c1::RAAS}}, reducing renal H<sup>+</sup> and K<sup>+</sup> loss.', '', 'Supressão de RAAS pela reposição de volume', 'Restoring volume stops the RAAS and decreases', 'Do limiar de cloreto urinário para o mecanismo da resposta ao tratamento no Extra.'),
('1487470244885', 'Free radical damage to <b>DNA</b> is implicated in {{c1::aging}} and {{c1::oncogenesis}}.', '', 'Consequências de dano oxidativo ao DNA', '<b>DNA</b> <b>damage</b> is implicated in <b>aging</b> and <b>oncogenesis</b>', 'De oxidação/peroxidação para duas consequências relacionadas explícitas no Extra.'),
('1500740499801', 'A plasmid carrying an <b>antibiotic resistance transposon</b> can pass to another bacterium by {{c1::conjugation}}.', '- The transposon can then enter the recipient’s <b>bacterial DNA</b>.', 'Conjugação transfere plasmídio portador de transposon', 'this plasmid can be transferred to another bacterium via <b>conjugation</b>', 'Do nome transposição para a etapa de transferência entre bactérias no Extra.'),
('1474763686814', 'What is the <b>filtration fraction</b> if GFR is 120 mL/min and RPF is 600 mL/min?<br><br>{{c1::20%}}', '- FF = <b>GFR / RPF</b>.', 'Aplicar FF = GFR/RPF a valores hipotéticos', '<b>FF</b> = {{c1::GFR / RPF}}', 'Da fórmula para aplicação aritmética nova, com unidades iguais e valores hipotéticos explicitados.'),
('1502564723231', 'For glucose of <b>600 mg/dL</b> and Na<sup>+</sup> of <b>130 mEq/L</b>, what is the corrected sodium?<br><br>{{c1::140 mEq/L}}', '- Add <b>2 mEq/L</b> per 100 mg/dL glucose above 100 mg/dL.', 'Aplicar a correção de sódio do exemplo fornecido', 'if glucose is 600 mg/dL and Na<sup>+</sup> is 130 mEq/L, corrected sodium is 140 mEq/L', 'Da fórmula para o resultado numérico do exemplo explícito no Extra.'),
('1556062743351', 'Which test measures vary with <b>disease prevalence</b>, unlike sensitivity and specificity?<br><br>{{c1::Positive and negative predictive values}}', '', 'Identificar valores preditivos como medidas dependentes da prevalência', '<b>Positive / negative predictive value</b> = {{c1::vary::fixed / vary}} depending on <u>prevalence</u>', 'Da decisão fixed/vary para identificar as medidas a partir da propriedade.'),
('1556808850149', 'In <b>asymmetric fetal growth restriction</b>, growth of the {{c1::brain}} is preserved relative to the abdomen.', '- Associated with <b>uteroplacental insufficiency</b> or malnutrition in later pregnancy.', 'Preservação cerebral relativa na restrição assimétrica', '<b>Asymmetric</b>: normal in vital brain, shunted away from abdomen', 'Da classificação por causa/trimestre para o órgão preservado no Extra.'),
('1532546709574', '<b>Muscle-invasive bladder cancer</b> is managed with chemotherapy and {{c1::radical cystectomy}}.', '- <b>Non-muscle-invasive</b> disease is managed with TURBT and intravesical therapy.', 'Cirurgia da neoplasia vesical músculo-invasiva', '<u>Muscle invasive</u> bladder cancer = chemotherapy + <b>radical cystectomy</b>', 'Da doença não invasiva para seu contraste terapêutico explícito no Extra.'),
('1496181891349', 'In <b>COPD</b>, a flattened diaphragm has difficulty generating {{c1::negative}} intrathoracic pressure during contraction.', '- Hyperinflation increases the <b>work of breathing</b>.', 'Pressão intratorácica cuja geração fica prejudicada', 'difficulty contracting</b> to expand the thoracic cavity and generate a negative intrathoracic pressure', 'Do achado radiológico para a consequência mecânica no Extra.'),
('1535304077148', 'Why is <b>IV contrast</b> preferred for CT in suspected pancreatitis?<br><br>To detect {{c1::pancreatic necrosis}}', '', 'Necrose pancreática como razão para contraste', 'Contrast-enhanced (IV contrast) is the preferred modality because it allows detection of pancreatic necrosis', 'Da escolha do exame à razão para sua modalidade contrastada no Extra.'),
('1520972770539', 'Stridor from <b>laryngomalacia</b> typically improves in the {{c1::prone::supine or prone}} position.', '- Worse with <b>feeding</b>, crying, or lying supine.', 'Posição em que estridor da laringomalácia melhora', '<u>Improves</u> in the <u>prone</u> position', 'Do tecido/fase respiratória para modificação posicional do sintoma no Extra.'),
('1462327309654', 'Which major <b>ketone body</b> is more prevalent in T1DM?<br><br>{{c1::β-Hydroxybutyrate}}', '- The other major ketone body is <b>acetoacetate</b>.', 'Maior prevalência de beta-hidroxibutirato', 'β-hydroxybutyrate is more prevalent', 'Da lista de dois corpos cetônicos para a comparação hierárquica no Extra.'),
('1471824884869', 'Which two <b>mediastinal structures</b> may be compressed by a thoracic aortic aneurysm?<br><br>{{c1::Esophagus and airway}}', '', 'Estruturas comprimidas por aneurisma torácico', 'compression of mediastinal structures (e.g., esophagus, airway)', 'Da insuficiência valvar para outra complicação anatômica explicitada no Extra.'),
('1573573340666', '<b>Rhabdomyolysis</b> may cause nephrotoxic acute tubular necrosis through release of {{c1::heme pigments}} into the bloodstream.', '- <b>Intravascular volume depletion</b> can worsen the kidney injury.', 'Pigmentos responsáveis pela nefrotoxicidade', 'releases <i>heme pigments</i> into the bloodstream, which may cause {{c1::<b>acute tubular necrosis</b>', 'Do desfecho renal para o agente liberado que o produz.'),
('1518989205267', '<b>Extranodal lymphoma</b> may arise in the {{c1::skin}} or {{c1::GI tract}}.', '- Lymphomas are malignancies of <b>B or T lymphocytes</b>.', 'Exemplos de localizações extranodais', 'can be "extranodal" (skin, GI tract)', 'Da identificação de lymphoma pela massa nodal para exemplos extranodais no Extra.'),
('1463098751199', 'Unlike the ectocervix, the <b>endocervix</b> is lined by {{c1::simple columnar}} epithelium.', '- <b>Ectocervix</b> has non-keratinized stratified squamous epithelium.', 'Contraste epitelial endocervix/ectocervix', 'Endocervix</td><td style="height: 23.5px;">Simple columnar epithelium', 'Do epitélio vaginal para contraste de estruturas na tabela textual do Extra.'),
('1496165362901', '<b>Astrocytomas</b> and <b>glioblastomas</b> are tumors of {{c1::neuroglia}}.', '- <b>GFAP</b> can identify these tumors on immunohistochemistry.', 'Linhagem de astrocytomas e glioblastomas', 'These are tumors of <u>neuroglia', 'Do marcador imuno-histoquímico para a linhagem celular explicitada no Extra.'),
('1516129632942', 'What are <b>bacteria-coated vaginal epithelial cells</b> called?<br><br>{{c1::Clue cells}}', '- Classically seen with <i>Gardnerella vaginalis</i> in <b>bacterial vaginosis</b>.', 'Nome da célula descrita', 'CLUE cells', 'Do agente/diagnóstico para o nome morfológico no Extra.'),
('1556731073581', '<b>Epithelial ovarian carcinoma</b> may cause bloating and early satiety secondary to {{c1::ascites}}.', '', 'Ascite como causa de sintomas de compressão', 'May also present with <b>bloating</b> and/or<b> early satiety </b>secondary to ascites', 'Do diagnóstico por apresentação para a relação sintomas–ascite no Extra.'),
('1515539356519', 'At the <b>pelvic inlet</b>, the ureter crosses over the bifurcation of the {{c1::common iliac artery}}.', '', 'Relação vascular na constrição do ureter', 'As the ureter enters the pelvis and crosses over the common iliac artery bifurcation', 'Da lista das três constrições para a relação vascular no Extra.'),
('1580921185599', 'Decreased gallbladder motility during <b>fasting</b> allows increased reabsorption of {{c1::water}} from bile.', '- Favors <b>cholesterol gallstones</b>.', 'Substância reabsorvida da bile com menor motilidade', 'Allows increased reabsorption of water from bile', 'Do tipo de cálculo para etapa intermediária do mecanismo no Extra.'),
('1497374236198', 'Rapid depolarization throughout a muscle fiber via <b>T-tubules</b> synchronizes {{c1::calcium release}} and myofibril contraction.', '', 'Evento sincronizado pela propagação pelo túbulo T', 'ensuring synchronized calcium release and contraction of myofibrils', 'Da estrutura/receptor para o efeito funcional da propagação elétrica no Extra.'),
('1474763535790', '<b>Glomerular capillary oncotic pressure</b> rises as filtration increases the concentration of {{c1::protein}} in the remaining plasma.', '', 'Aumento da concentração proteica explica pressão oncótica', 'Due to increased protein concentration as fluid is filtered out', 'Da direção da mudança para a causa explícita no Extra.'),
('1506032880639', '<b>Aminoglycosides</b> cause mRNA misreading by binding the {{c1::30S}} ribosomal subunit.', '- Irreversibly inhibit the <b>initiation complex</b>.', 'Subunidade ribossomal ligada pelos aminoglicosídeos', 'Binds <b>30S ribosomal subunit</b>', 'Do nome da classe para sua localização molecular no Extra.'),
('1516473945645', 'Which receptors does <b>rabies virus</b> bind at the motor endplate?<br><br>{{c1::Nicotinic acetylcholine receptors}}', '- Infection occurs within <b>striated muscle</b> cells.', 'Receptor no qual vírus da raiva se liga', 'the virus binds the <b>nicotinic ACh receptors</b> at the <u>motor endplate</u>', 'Da célula infectada para o receptor descrito no Extra.'),
('1578671289004', '<b>IFN-α</b> is contraindicated in autoimmune disease because immune upregulation can cause {{c1::exacerbation}} of the disease.', '- Includes <b>systemic lupus erythematosus</b>.', 'Exacerbação como motivo de contraindicação', 'immune system upregulators such as interferon can cause an exacerbation of autoimmune disease', 'Do subtipo de interferon para a razão da contraindicação no Extra.'),
('1462223862805', 'In <b>Hashimoto thyroiditis</b>, antithyroglobulin and anti-TPO antibodies are a {{c1::sign::sign or cause}} of thyroid damage.', '- <b>Anti-microsomal</b> antibodies = anti-TPO antibodies.', 'Anticorpos como sinal e não causa do dano', 'These are a <b>sign</b> of thyroid damage, <u><b>not</b></u> the <b>cause</b> of damage', 'Dos nomes dos anticorpos para a interpretação causal explicitada no Extra.'),
]

entries = []
for i, (sid, text, extra, target, evidence, change) in enumerate(drafts, 1):
    entries.append(dict(id=f'draft-{i:03}', origin='Autoral', family=sources[sid]['family'], text=text, extra=extra,
                        group_id=f'source-{sid}', source_id=sid, target=target, evidence=evidence, change_from_source=change))

reserved = [
('1524014002691', 'Identificar o ligamento largo como a estrutura cujo peritônio recebe o ligamento redondo durante a histerectomia.'),
('1486605712112', 'Recuperar origem do omento menor no mesentério ventral, explicitada no Extra.'),
('1480640382358', 'Recuperar corda do tímpano como ramo responsável pela salivação submandibular/sublingual.'),
('1463526337153', 'Recuperar lábios maiores como ponto de ancoragem do ligamento redondo uterino.'),
('1474164969397', 'Recuperar diminuição de atividade da glucoquinase como etapa que reduz aprisionamento hepático de glicose.'),
('1502302298317', 'Comparar metabolismo por CYP450 de clonidina e guanfacina, recuperando clonidina como fármaco do contraste.'),
('1502064066857', 'Recuperar os sentidos positivo/negativo como categorias da polaridade dos vírus RNA.'),
('1516321085226', 'Recuperar genoma RNA de fita dupla a partir do nome Reoviridae.'),
('1485917667823', 'Recuperar queda de sensibilidade quando se eleva o ponto de corte, conforme contraste do Extra.'),
('1484774485137', 'Recuperar benzodiazepínicos como grupo comparativamente mais propenso a tolerância.'),
('1550696451455', 'Recuperar T12–L2 como níveis de lesão descritos para síndrome do cone medular no Extra.'),
('1547242128412', 'Recuperar inibição da ovulação como característica comum de gestação e anticoncepcionais no Extra.'),
('1530402119061', 'Reconhecer ataxia de Friedreich pelo conjunto focal de achados clínicos e alvo genético explícitos.'),
('1462206436898', 'Recuperar glicose oral como estímulo usado para testar supressão de GH em suspeita de adenoma secretor.'),
('1517255729542', 'Recuperar limite típico de sobrevida de 1 ano na síndrome de Zellweger descrito no Extra.'),
('1488502643324', 'Recuperar estrato granuloso como camada espessada na hipergranulose.'),
('1476584161540', 'Recuperar preservação de crescimento linear em desnutrição proteico-energética aguda, com qualificador temporal.'),
('1523154017600', 'Recuperar exclusão do valor nulo como relação com IC de um resultado significativo.'),
('1538596474196', 'Recuperar parede intestinal como trajeto de passagem de AFP ao líquido amniótico na gastrosquise.'),
('1484188992648', 'Recuperar hormônios dos tireotrofos e gonadotrofos, cujo adenoma funcional é raro.'),
('1475353678694', 'Recuperar tecido entre túbulos como localização do infiltrado na nefrite intersticial aguda.'),
('1463101154172', 'Recuperar terço inferior do canal vaginal como localização do epitélio fetal escamoso descrito.'),
('1475376498638', 'Recuperar PSGN a partir de humps subepiteliais na microscopia eletrônica.'),
('1499810504793', 'Recuperar Cryptosporidia a partir das propriedades intracelular, unicelular e parcialmente álcool-ácido resistente.'),
('1462995810306', 'Recuperar manutenção endometrial como efeito da elevação de estrogênio e progesterona na gestação.'),
('1463101150767', 'Recuperar seio urogenital como estrutura cuja falha pode causar ausência de abertura vaginal.'),
('1584909513781', 'Recuperar hepatócitos e pequenos dúctulos biliares como estruturas lesadas na hepatite alcoólica.'),
('1462146011884', 'Recuperar calcitriol como outro nome de 1,25-di-hidroxicolecalciferol.'),
('1503254970224', 'Recuperar estreptomicina como alternativa à droga E no esquema histórico RIPE presente na fonte, sem ampliar recomendação.'),
('1584731244356', 'Recuperar ceratoconjuntivite como manifestação de Microsporidium tratada com fumagilina tópica.'),
('1509919246615', 'Recuperar enrolamento em bastão como método de remoção de Dracunculus medinensis.'),
('1403149942402', 'Recuperar infecção latente como fase associada a EBNA.'),
]
briefs = [dict(id=f'reserve-{i:03}', family=sources[sid]['family'], source_id=sid, group_id=f'source-{sid}', target=target,
               source_text=sources[sid]['text'], source_extra=sources[sid]['extra']) for i, (sid, target) in enumerate(reserved, 1)]
assert len(entries) == len(briefs) == 32
assert set(Counter(e['family'] for e in entries).values()) == {4}
assert set(Counter(e['family'] for e in briefs).values()) == {4}
assert len({e['source_id'] for e in entries + briefs}) == 64
lint = [{'id': e['id'], 'issues': check(e['id'], e['text'], e['extra'])} for e in entries]
assert not any(level == 'dura' for r in lint for level, _ in r['issues'])
for name, value in [('v1.json', entries), ('brief-v2.json', briefs), ('lint-v1.json', lint)]:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'v1':len(entries), 'reserved_v2':len(briefs), 'families':Counter(e['family'] for e in entries), 'lint': [x for x in lint if x['issues']]},ensure_ascii=False))
