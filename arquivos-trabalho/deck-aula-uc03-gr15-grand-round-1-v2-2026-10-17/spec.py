# Especificação curada — Grand Round 1: Esquizofrenia (UC03 P1; 57 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing (seções Bootcamp Schizophrenia, FirstAid Schizophrenia, Psychosis, Schizoaffective, Dopaminergic pathways, Cannabis, Microglia,
# Ex vacuo) → cards da 02 e da 62 por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing)
    "_Bootcamp_Psychiatry_06_Psychotic_and_Mood_Disorders_05_Schizophrenia.txt",
    "_FirstAid_13_Psych_02_Pathology_10_Schizophrenia_spectrum_disorders_01_Schizophrenia_base.txt",
    "_FirstAid_13_Psych_02_Pathology_10_Schizophrenia_spectrum_disorders_02_Schizoaffective_disorder.txt",
    "_FirstAid_13_Psych_02_Pathology_08_Psychosis_Basics.txt",
    "_FirstAid_13_Psych_02_Pathology_08_Psychosis_01_Delusions.txt",
    "_FirstAid_13_Psych_02_Pathology_08_Psychosis_02_Disorganized_thought.txt",
    "_FirstAid_13_Psych_02_Pathology_08_Psychosis_03_Hallucinations.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_15_Dopaminergic_pathways_Synthesis.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_15_Dopaminergic_pathways_Mesocortical.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_15_Dopaminergic_pathways_Mesolimbic.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_15_Dopaminergic_pathways_Nigrostriatal.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_15_Dopaminergic_pathways_Tuberoinfundibular.txt",
    "_FirstAid_13_Psych_02_Pathology_41_Psychoactive_drug_intoxication_and_withdrawal_Hallucinogens_Cannabis.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_01_Cells_of_the_nervous_system_Microglia.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_03_Pathology_22_Hydrocephalus_03_Hydrocephalus_mimics_Ex_Vacuo_Ventriculomegal.txt",
]
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-gr15-20261017a"
SHORT = "gr15n"
LESSON = "2026-uc03-grand-round-01-esquizofrenia"
DECK = "NEBLI::UC03::P1::Grand Round::Grand Round 1 (esquizofrenia)"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"gr15-{n}.png": f"img/gr15-{n}.png" for n in ("curso", "inicio", "ventriculos", "vias", "metabolismo", "neuronio")}
IMG = lambda n, w=460: f'<img src="gr15-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (Bootcamp/FirstAid esquizofrenia, psicose, esquizoafetivo, vias dopaminérgicas, "
         "maconha, micróglia, ex vacuo; busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt: COMT, HVA, 22q11, "
         "clozapina, privilégio imune, linfáticos, PCP, anfetamina, idade paterna); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
_DD = "diagnóstico diferencial por duração/tipo (psicótico breve, esquizofreniforme, delirante) — não está nas lâminas; aula de psiquiatria"
_AL = "tipo de alucinação de doença neurológica, abstinência ou sono — não está nas lâminas; aula de psicopatologia"
EXCLUIDOS = [
 (1484687007437, _DD), (1484687009939, _DD), (1484687012119, _DD), (1484687082109, _DD), (1484687092839, _DD),
 (1484687098561, "folie à deux: transtorno delirante compartilhado, fora das lâminas"),
 (1484687040599, "alucinação no luto: normalidade no luto, fora das lâminas"),
 (1484686959612, _AL), (1484686962016, _AL), (1484686964548, _AL), (1484686970345, _AL), (1484686981848, _AL),
 (1509029241977, "repete ak-alvo-mesolimbico (via-alvo do efeito terapêutico)"),
 (1483845036009, "repete ak-nigro-eps (nigroestriatal → extrapiramidais)"),
 (1483845038905, "repete ak-nigro-eps (nigroestriatal e antipsicóticos)"),
 (1483845052600, "repete ak-tubero-prolactina"),
 (1485313635264, "abstinência de maconha: aula de drogas de abuso, fora das lâminas"),
 (1485313638474, "dronabinol: farmacologia, fora das lâminas"), (1485313640304, "dronabinol antiemético: farmacologia, fora das lâminas"),
 (1485313642194, "dronabinol orexígeno: farmacologia, fora das lâminas"),
 (1479430563185, "micróglia derivada de fagócitos mononucleares: entra a cópia NEBLI da 62 (sh-1791983681660)"),
 (1479430416710, "definição de glia: histologia do SNC, fora das lâminas"),
 (1479430572001, "micróglia e Nissl: histologia, fora das lâminas"), (1479430574466, "origem mesodérmica da micróglia: embriologia, fora das lâminas"),
 (1479430576741, "pericitos e barreira: histologia, fora das lâminas"), (1479430579711, "células gigantes no HIV: aula de infecção viral"),
]
FORA_DO_RECORTE = [
 "Farmacologia detalhada dos antipsicóticos (efeitos adversos, fármacos específicos): aula de farmacologia; aqui só alvo e linha de tratamento.",
 "PANSS item por item, estigma por frase e biografia de Brian Wilson: só ilustração.",
 "Experimentos animais de estresse e imunidade (lâminas 47–48): ilustrativos.",
]
A_, B_, C_, D_, E_, F_ = "A-clinica", "B-curso", "C-imagem", "D-dopamina", "E-celular-imune", "F-estigma"

CARDS = [
 # ---------- A. Clínica (lâminas 2–6) ----------
 ak("ak-atipicos-1a-linha", 1484687075078, "A-aula", A_, "Atípicos (risperidona) são primeira linha", 2, "caso (risperidona); seção"),
 ak("ak-clozapina", 1485220015721, "V-hy", A_, "Clozapina no refratário", 2, "caso (sem melhora com risperidona); seção"),
 ak("ak-psicose", 1484686918152, "A-aula", A_, "Psicose: delírios, alucinações, desorganização", 4, "lâmina 4; seção"),
 ak("ak-delirio", 1484686921210, "A-aula", A_, "Delírio: crença falsa fixa", 4, "lâmina 4; apostila (delírio × alucinação)"),
 ak("ak-alucinacao", 1484686931716, "A-aula", A_, "Alucinação: percepção sem estímulo", 4, "lâmina 4; apostila"),
 ak("ak-ilusao", 1484686938102, "R-detalhe", A_, "Ilusão: percepção errada de estímulo real", 4, "contraste com alucinação; seção"),
 ak("ak-alucinacao-auditiva", 1484686953118, "A-step", A_, "Alucinação auditiva → psiquiátrica", 4, "apostila (vozes); seção"),
 ak("ak-alucinacao-visual", 1484686943783, "A-step", A_, "Alucinação visual → doença médica", 4, "seção"),
 ak("ak-desorganizado", 1484686929022, "A-aula", A_, "Pensamento desorganizado", 4, "lâmina 4; seção"),
 ak("ak-negativos", 1540248856209, "A-aula", A_, "Sintomas negativos", 4, "lâminas 4 e 6; seção"),
 au("au-cognitivos", "<b>Schizophrenia</b> also causes {{c1::cognitive}} symptoms, such as poor attention, memory and abstraction",
    "A-aula", A_, "Sintomas cognitivos", 4, "lâmina 4; apostila (dificuldade enorme de abstração)",
    extra="- Five groups: psychotic, negative, cognitive, mood and disorganization"),
 ak("ak-criterios", 1484687004511, "A-step", A_, "Critérios diagnósticos", 4, "seção"),
 ak("ak-def-6meses", 1484686987962, "A-step", A_, "Esquizofrenia: ≥ 6 meses", 4, "seção"),
 ak("ak-positivos", 1540248633321, "A-aula", A_, "Sintomas positivos", 5, "lâmina 5 (PANSS positiva)"),
 ak("ak-prevalencia", 1541613492329, "A-step", A_, "Prevalência ≈ 1%", 5, "epidemiologia; busca semântica"),
 ak("ak-raca", 1484687053386, "R-detalhe", A_, "Sem predileção por raça", 5, "seção"),
 # ---------- B. Curso (lâminas 7–12) ----------
 au("au-curso", "<b>Schizophrenia</b> runs through premorbid, {{c1::prodromal}}, progressive and chronic phases",
    "V-pilar", B_, "Fases da esquizofrenia", 7, "lâminas 7–8; apostila (fases)",
    extra="- Prodrome (14–17 years): school decline, isolation, aggressiveness, depressive symptoms<br>"
          "- Chronic phase after 35–40: fewer psychoses, affective and volitional blunting<br>" + IMG("curso")),
 ak("ak-prognostico", 1523368535525, "A-step", B_, "Fatores de bom prognóstico", 8, "seção"),
 ak("ak-sexo", 1484687061129, "A-aula", B_, "Mais comum em homens", 9, "lâmina 9; seção"),
 au("au-inicio", "<b>Schizophrenia</b> begins earlier in {{c1::men}}, with peak onset around 20–24 years",
    "V-pilar", B_, "Início mais cedo nos homens", 9, "lâmina 9 (Häfner); apostila",
    extra="- Women show a second peak around 45, near menopause<br>" + IMG("inicio", 400)),
 au("au-idade-paterna", "Advanced {{c1::paternal}} age, above about 45, is associated with <b>schizophrenia</b> in the offspring",
    "A-aula", B_, "Idade paterna avançada", 10, "lâmina 10; apostila (associação não é causalidade)",
    extra="- An association, not a proven cause; new mutations in older fathers are one proposed link"),
 au("au-neurodesenvolvimento", "Obstetric complications, low birth weight and intrauterine infection raise <b>schizophrenia</b> risk, supporting the {{c1::neurodevelopmental}} hypothesis",
    "V-pilar", B_, "Hipótese do neurodesenvolvimento", 11, "lâminas 11 e 29–30; apostila",
    extra="- Early motor and social delays also precede the disease"),
 # ---------- C. Imagem (lâminas 11–22, 36) ----------
 ak("ak-ventriculomegalia", 1509647553855, "A-aula", C_, "Ventriculomegalia e atrofia cortical", 13, "lâminas 11 e 13; seção"),
 ak("ak-ex-vacuo", 1481858021692, "A-aula", C_, "Hidrocefalia ex vacuo: atrofia", 13, "lâminas 13 e 16; seção"),
 ak("ak-ex-vacuo-pic", 1481858027327, "A-step", C_, "Ex vacuo: PIC normal", 13, "seção"),
 sh(1792141773206, "azul", C_, "Forças e limites da RM", 20, "lâmina 20 (tabela TC × RM); card da 02"),
 sh(1792141775531, "azul", C_, "RM e US não usam radiação ionizante", 20, "lâmina 20; card da 02"),
 sh(1792141769157, "azul", C_, "Contraste de cada método (iodo × gadolínio)", 20, "lâmina 20; card da 02"),
 au("au-volume", "<b>Brain volume</b> in schizophrenia falls {{c1::progressively}} after the first episode, most in poor-outcome patients",
    "A-aula", C_, "Perda progressiva de volume", 22, "lâminas 12, 22 e 36; apostila (processos neurodegenerativos após as psicoses)",
    extra="- Losses predominate in frontal and periventricular regions"),
 # ---------- D. Dopamina (lâminas 23–35) ----------
 ak("ak-sintese-da", 1483844984027, "A-step", D_, "Dopamina: área tegmentar ventral e substância negra", 23, "lâmina 23; seção"),
 ak("ak-anfetamina", 1477089800068, "A-step", D_, "Anfetamina desloca catecolaminas", 23, "lâmina 23 (agonistas); apostila (estimulantes)"),
 ak("ak-antipsicoticos-positivos", 1483845012219, "A-step", D_, "Antipsicóticos tratam positivos", 23, "lâmina 23; seção"),
 ak("ak-tipico-atipico", 1540250274176, "A-step", D_, "Típicos × atípicos", 23, "seção"),
 ak("ak-tipicos-negativos", 1483844994929, "A-step", D_, "Típicos não tratam negativos", 24, "lâmina 8 (resposta parcial); seção"),
 ak("ak-dopamina", 1484686778249, "V-hy", D_, "Dopamina aumentada na esquizofrenia", 24, "lâminas 24 e 35; seção"),
 ak("ak-hipotese-da", 1540248871113, "A-aula", D_, "Hipótese dopaminérgica", 24, "lâminas 24–25; seção"),
 ak("ak-vias-sintomas", 1541613861907, "A-aula", D_, "Vias e sintomas positivos × negativos", 24, "lâminas 24–25"),
 ak("ak-mesolimbica-via", 1483845001624, "A-step", D_, "Via mesolímbica: tegmento → límbico", 24, "lâmina 24; seção"),
 ak("ak-mesolimbica-positivos", 1483845005621, "V-hy", D_, "Mesolímbica → positivos", 24, "lâminas 24–25; seção"),
 ak("ak-alvo-mesolimbico", 1483845020612, "A-step", D_, "Alvo dos antipsicóticos: mesolímbica", 24, "seção"),
 ak("ak-mesocortical-via", 1483844986184, "A-step", D_, "Via mesocortical: tegmento → pré-frontal", 24, "seção"),
 ak("ak-mesocortical-negativos", 1483844989020, "V-hy", D_, "Mesocortical → negativos", 24, "lâminas 24–25 (D1 cortical); seção"),
 ak("ak-nigro-via", 1483845023339, "A-step", D_, "Via nigroestriatal", 24, "lâmina 24; seção"),
 ak("ak-nigro-eps", 1483845029571, "V-hy", D_, "Bloqueio nigroestriatal → extrapiramidais", 24, "seção"),
 ak("ak-tubero-via", 1483845041645, "A-step", D_, "Via tuberoinfundibular", 24, "lâmina 24; seção"),
 ak("ak-tubero-prolactina", 1483845044133, "V-hy", D_, "Bloqueio tuberoinfundibular → prolactina", 24, "seção"),
 ak("ak-comt-3mt", 1485226927627, "A-aula", D_, "COMT degrada dopamina a 3-MT", 26, "lâmina 26"),
 ak("ak-maob-dopac", 1485226964020, "A-step", D_, "MAO-B degrada dopamina a DOPAC", 26, "lâmina 26"),
 ak("ak-hva", 1476416128783, "A-step", D_, "HVA: produto final da dopamina", 26, "lâmina 26"),
 au("au-comt", "The <b>COMT</b> {{c1::Val}} allele degrades prefrontal dopamine faster, worsening prefrontal function and possibly raising schizophrenia risk",
    "A-aula", D_, "Alelo Val da COMT", 27, "lâmina 27 (Egan 2001; a apostila inverte o efeito na fenda, corrigido)",
    extra="- The COMT gene lies on 22q; the Met allele seems protective<br>- Association, not causation"),
 ak("ak-maconha-teens", 1484687045054, "A-aula", D_, "Maconha na adolescência e psicose", 28, "lâminas 28 e 33; seção"),
 ak("ak-maconha-intox", 1485313628099, "A-step", D_, "Intoxicação por maconha: delírios paranoides", 28, "seção"),
 # ---------- E. Célula e imunidade (lâminas 37–46) ----------
 au("au-espinhas", "In <b>schizophrenia</b>, cortical neurons have a smaller soma and fewer {{c1::dendritic spines}}, from focal apoptosis at synapses",
    "V-pilar", E_, "Neurônio esquizofrênico", 37, "lâminas 37–39 (Glantz 2006); apostila (apoptose focal do botão)",
    extra="- An adaptation to excess stimulation that spares the neuron itself<br>" + IMG("neuronio", 420)),
 ak("ak-ramificacao", 1484687002472, "R-detalhe", E_, "Menos ramificação dendrítica", 37, "lâmina 37; seção"),
 ak("ak-serotonina", 1582314040264, "R-detalhe", E_, "Mais serotonina e menos ramificação", 37, "seção"),
 au("au-inflamacao", "Brain volume loss in <b>schizophrenia</b> correlates with inflammatory markers such as {{c1::IL-1β}} and microglial activation",
    "A-aula", E_, "Inflamação e perda de volume", 40, "lâminas 40–42 e 46 (Müller 2014)",
    extra="- Physical exercise lowers IL-6 and improves cognition<br>- Schizophrenia is not an immune disease, but brain and immunity talk both ways"),
 sh(1791983681660, "azul", E_, "Micróglia deriva de fagócitos mononucleares", 41, "lâmina 41; card da 62"),
 ak("ak-microglia-ativada", 1479430568786, "A-step", E_, "Micróglia ativada por dano", 41, "lâmina 41; seção"),
 au("au-microglia-poda", "<b>Microglia</b> prune {{c1::synaptic terminals}}, which may add to synapse loss in schizophrenia",
    "A-aula", E_, "Micróglia poda sinapses", 41, "lâmina 41; apostila (micróglia e apoptose das terminações)",
    extra="- Microglia are the resident macrophages of the CNS"),
 au("au-privilegio", "Grafts placed in the <b>brain</b> survive unless the host was already sensitized, showing CNS {{c1::immune privilege}}",
    "A-aula", E_, "Privilégio imune do SNC", 43, "lâminas 43 e 45 (Medawar 1948; duas etapas)",
    extra="- The response needs sensitization first, then challenge; a graft only in the brain fails to sensitize"),
 au("au-linfaticos", "<b>CNS immune privilege</b> is relative, since the brain drains to cervical nodes through {{c1::meningeal lymphatics}}",
    "A-aula", E_, "Linfáticos meníngeos", 44, "lâmina 44 (Louveau 2017, revisitando o privilégio)",
    extra="- Medawar already suggested that immunity needs lymphatic drainage"),
 # ---------- F. Estigma e Brian Wilson (lâminas 49–57) ----------
 au("au-estigma", "Using <b>schizophrenia</b> as a metaphor for incoherence feeds {{c1::stigma}}, which delays treatment and isolates patients",
    "A-aula", F_, "Estigma", 50, "lâminas 49–52; apostila (estigma compromete o restabelecimento)",
    extra="- Many notable people lived productive lives with mental illness"),
 ak("ak-clozapina-suicidio", 1485220018582, "A-step", F_, "Clozapina na suicidalidade", 54, "lâmina 54 (tentativas de suicídio); seção"),
 ak("ak-esquizoafetivo", 1484687016622, "V-hy", F_, "Transtorno esquizoafetivo", 55, "lâmina 55 (diagnóstico de Brian Wilson); seção"),
 ak("ak-esquizoafetivo-2sem", 1484687018871, "A-step", F_, "Esquizoafetivo: 2 semanas de psicose sem humor", 55, "seção"),
 ak("ak-psicose-humor", 1484687032478, "R-detalhe", F_, "Psicose só no episódio de humor", 55, "seção"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-atipicos-1a-linha": "- The case patient takes risperidone and is not improving",
 "ak-clozapina": "- Indicated after failure of two antipsychotics",
 "ak-psicose": "- Psychotic symptoms are one of five symptom groups in schizophrenia",
 "ak-delirio": "- The patient believes it even without any basis in reality",
 "ak-alucinacao": "- The patient perceives it and is certain it happened",
 "ak-ilusao": "- A hallucination needs no external stimulus",
 "ak-alucinacao-auditiva": "- Voices are typical of schizophrenia",
 "ak-alucinacao-visual": "- Think of delirium or a neurologic cause",
 "ak-desorganizado": "- Interviews feel like an interrogation, with contradictions",
 "ak-negativos": "- Negative symptoms are function below baseline",
 "ak-criterios": "- At least one must be delusions, hallucinations or disorganized speech",
 "ak-def-6meses": "- Shorter durations are other diagnoses",
 "ak-positivos": "- Positive symptoms are function above baseline",
 "ak-prevalencia": "- About 1 in 100 people",
 "ak-raca": "- Similar across populations",
 "ak-prognostico": "- Predominant negative symptoms and early insidious onset predict worse outcome",
 "ak-sexo": "- Men also start earlier",
 "ak-ventriculomegalia": "- Seen already in young patients, compared with age-matched controls<br>" + IMG("ventriculos", 420),
 "ak-ex-vacuo": "- Ventricles enlarge to fill space left by lost tissue",
 "ak-ex-vacuo-pic": "- Unlike obstructive hydrocephalus",
 "ak-sintese-da": "- Tyrosine hydroxylase then DOPA decarboxylase make dopamine",
 "ak-anfetamina": "- Stimulants can push a vulnerable person into psychosis",
 "ak-antipsicoticos-positivos": "- They block D2 receptors",
 "ak-tipico-atipico": "- Atypicals also act on 5-HT2A receptors",
 "ak-tipicos-negativos": "- Partial response is common because several pathways are involved",
 "ak-dopamina": "- Excess D2 activity in the mesolimbic pathway",
 "ak-hipotese-da": "- Serotonergic and glutamatergic hypotheses also exist",
 "ak-vias-sintomas": "- Mesolimbic D2 hyperactivity → positive; cortical D1 hypoactivity → negative<br>" + IMG("vias", 420),
 "ak-mesolimbica-via": "- The limbic system includes the hippocampus and amygdala",
 "ak-mesolimbica-positivos": "- Too much stimulus feeds persecution and hallucinations",
 "ak-alvo-mesolimbico": "- D2 blockade here controls positive symptoms",
 "ak-mesocortical-via": "- The prefrontal cortex governs self-control and social behavior",
 "ak-mesocortical-negativos": "- Low cortical D1 activity also underlies negative symptoms",
 "ak-nigro-via": "- The pathway lost in Parkinson disease",
 "ak-nigro-eps": "- Parkinsonism, dystonia, akathisia",
 "ak-tubero-via": "- Dopamine there inhibits prolactin",
 "ak-tubero-prolactina": "- Galactorrhea, amenorrhea, gynecomastia",
 "ak-comt-3mt": "- COMT is the key enzyme for dopamine in the prefrontal cortex<br>" + IMG("metabolismo", 400),
 "ak-maob-dopac": "- MAO acts inside the presynaptic neuron",
 "ak-hva": "- Both pathways converge on HVA",
 "ak-maconha-teens": "- Dose-dependent: risk rises with the number of uses by age 18",
 "ak-maconha-intox": "- Cannabis is a push toward psychosis, not a sole cause",
 "ak-ramificacao": "- Shorter dendrites and fewer presynaptic terminals",
 "ak-serotonina": "- Atypical antipsychotics also block 5-HT2A",
 "ak-microglia-ativada": "- Activated microglia appear in schizophrenia on PET imaging",
 "ak-clozapina-suicidio": "- Brian Wilson had suicide attempts during his illness",
 "ak-esquizoafetivo": "- Brian Wilson's final diagnosis, 25 years after onset",
 "ak-esquizoafetivo-2sem": "- Psychosis must also occur outside mood episodes",
 "ak-psicose-humor": "- That distinguishes it from schizoaffective disorder",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (curso, início, ventrículos, vias, metabolismo, neurônio) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Lieberman, Häfner, Javitt, Hyman, Glantz), sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "gr15-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "gr15-curso.png": "Lâmina 8: evolução de um caso (pré-mórbido, prodrômico, progressivo, crônico) com sinais em cada fase; verso de au-curso.",
 "gr15-inicio.png": "Lâmina 9: idade de início por sexo (pico masculino 20–24, feminino com 2º pico 45–49); verso de au-inicio.",
 "gr15-ventriculos.png": "Lâmina 13: RM coronal normal × esquizofrenia com ventrículos laterais dilatados; verso de ak-ventriculomegalia.",
 "gr15-vias.png": "Lâmina 24: vias nigroestriatal, mesolímbica (D2, positivos), tuberoinfundibular e cortical (D1, negativos); verso de ak-vias-sintomas.",
 "gr15-metabolismo.png": "Lâmina 26: dopamina degradada por MAO (DOPAC) e COMT (3-MT) até HVA; verso de ak-comt-3mt.",
 "gr15-neuronio.png": "Lâmina 37: neurônio normal × esquizofrênico (soma menor, menos espinhas, dendritos curtos, menos terminais); verso de au-espinhas.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Reconhecer os grupos de sintomas da esquizofrenia, seu curso e epidemiologia, a hipótese do neurodesenvolvimento, os achados "
             "de imagem, a hipótese dopaminérgica com as vias e a COMT, as alterações sinápticas e imunes, e o estigma.",
 "centrais": [
   ("curso e neurodesenvolvimento", "au-curso", "au-inicio", "au-neurodesenvolvimento"),
   ("sinapse", "au-espinhas", "ak-ramificacao"),
 ],
 "exemplos": ["caso do paciente em risperidona", "Brian Wilson", "Medawar", "frases pejorativas"],
 "outras_aulas": [("TC × RM", "02 Diagnóstico radiológico (sh)"), ("micróglia", "62 Inflamação crônica (sh)"),
                  ("farmacologia dos antipsicóticos", "farmacologia"), ("apoptose", "09 Lesão celular")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
