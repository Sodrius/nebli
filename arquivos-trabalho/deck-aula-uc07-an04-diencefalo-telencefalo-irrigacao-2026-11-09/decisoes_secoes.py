"""E4/E5: decisão de TODA nota das seções da aula (busca/secoes/*.txt): entra (AK_NOVOS ou já viva na reserva/AN01) ou EXCLUIDOS com motivo.
Ordem: (1) entra por chave; (2) duplica nota viva NEBLI; (3) Kenhub primeiro nas identificações; (4) motivo por categoria."""
import re

# AnKing que entra (nid → chave do plano). Critério: ensina o princípio da aula 04 (topografia + função básica que o professor cita)
AK_NOVOS = {
 1481513119712: "pre-central-motor",          # giro pré-central = córtex motor primário
 1481513127112: "pos-central-somestesica",    # giro pós-central = somestésico primário
 1481513311304: "broca-giro",                 # Broca = centro motor da fala
 1481513164343: "aca-territorio",             # face medial dos giros pré/pós-central = ACA
 1481513158967: "acm-territorio",             # face lateral dos giros pré/pós-central = ACM
 1481513222026: "acp-territorio",             # ACP irriga o lobo occipital
 1481513227002: "acp-territorio-temporal",    # ACP irriga a face inferior do lobo temporal
 1481562744652: "aca-deficit",                # AVC de ACA: membro inferior contralateral (HY1)
 1481562751403: "acm-deficit",                # AVC de ACM: face e membro superior contralaterais (HY1)
 1481244840641: "acp-visao",                  # ACP: hemianopsia homônima com preservação macular (HY2)
 1481244690823: "calcarino-visao",            # córtex visual dividido em cúneo e giro lingual pelo calcarino
 1481162303980: "lentiforme",                 # lentiforme = putâmen + globo pálido
 1481162002789: "nucleos-base-movimento",     # núcleos da base modulam o movimento
 1481162464655: "hemibalismo",                # núcleo subtalâmico → hemibalismo contralateral (HY2)
 1481857900096: "huntington-caudado",         # Huntington: caudado e putâmen (clínica imediata dos núcleos da base)
 1480389641277: "capsula-interna-perna-posterior",  # corticoespinal na perna posterior da cápsula interna
 1481418712049: "geniculado-lateral-visao",   # GL recebe a informação visual
 1481418725172: "geniculado-medial-audicao",  # GM recebe a informação auditiva
 1481418766004: "supraquiasmatico-ritmo",     # supraquiasmático = ritmo circadiano
 1481418757045: "supraoptico-adh",            # supraóptico = ADH
 1481418763459: "paraventricular-ocitocina",  # paraventricular = ocitocina
 1481418777586: "ventromedial-saciedade",     # ventromedial = saciedade
 1461884702127: "infundibulo-hipofise",       # ADH e ocitocina: hipotálamo → neuro-hipófise pelo infundíbulo
 1481418839841: "epitalamo-org",              # epitálamo = pineal + habênula
 1481418842065: "pineal-melatonina",          # pineal = melatonina
 1522347007612: "vertebral-trajeto",          # vertebrais nos forames transversos
 1521261423614: "vertebral-subclavia",        # vertebral = primeiro ramo da subclávia (VIT CD)
 1480995212247: "pica-wallenberg",            # PICA irriga o bulbo lateral (HY1)
 1550673159267: "oculomotor-sca-acp",         # III passa entre a cerebelar superior e a cerebral posterior
 1481772047979: "aneurisma-acom",             # aneurisma da comunicante anterior comprime o quiasma
 1481772053364: "aneurisma-pcom",             # aneurisma da comunicante posterior comprime o III
 1481596917147: "id-sulco-parietoccipital",   # sem identificação Kenhub do sulco parietoccipital
 1481596931776: "id-sulco-cingulo",           # sem identificação Kenhub do sulco do cíngulo
}

# AnKing já presente como cópia viva NEBLI (reserva UC07 ou AN01) que cobre a mesma relação
DUPLICA = {
 1481513318381: 1793966747239,   # Broca no giro frontal inferior (AN01)
 1481514003114: 1793889229460,   # Broca não fluente (AN01)
 1481513092382: 1792261811748,   # sulco lateral separa temporal (reserva, 12 revisões de Davi)
 1481513193377: 1792350077635,   # ACA face medial (reserva)
 1481513198423: 1792350077936,   # ACA ~2,5 cm superiores (reserva)
 1481513212688: 1792350083811,   # ACM face lateral (reserva)
 1474511979294: 1792350134160,   # carótida comum bifurca em C4 (reserva)
 1479351810861: 1793966747210,   # diencéfalo → tálamo e hipotálamo (AN01)
 1550695810634: 1481162303980,   # lentiforme (cópia Only_Step_2)
 1550694966430: 1481162298898,   # estriado (cópia Only_Step_2)
 1461870015336: 1461884702127,   # neuro-hipófise com axônios hipotalâmicos
 1480389629812: 1481513119712,   # neurônio motor superior no giro pré-central
 1481244670461: 1481418712049,   # trato óptico → geniculado lateral
 1540593668516: 1481418766004,   # supraquiasmático circadiano (cópia Only_Step_2)
 1481418772358: 1481418766004, 1481418775282: 1481418842065,
 1481562763561: 1481513311304,   # ACM + afasia: Broca já ligado ao giro e à ACM pelo território
 1481513308424: 1481513158967,
}

KENHUB = "Identificação AnKing de estrutura que já tem identificação Kenhub nesta aula (Kenhub primeiro, uma verde por estrutura)."
CAT = [
 (r"ID (Structure|Vessel|Gyrus|Sulcus) :|ID letter", KENHUB),
 (r"Brodmann|premotor|prefrontal|frontal eye|association cortex|astereognosis|Gerstmann|neglect|Hemineglect|primitive reflexes|[Pp]rimitive|disinhibition|Cortical Area|Red-Curvy|micturition|homonymous (inferior|superior)|Meyer|optic radiation|dorsal optic|Upside down|watershed|border zone|Alexia|Wernicke area|Conduction aphasia|Global aphasia|Wernicke aphasia|aphasia|language|motor/sensory areas corresponding|verbal memory|temporal lobe may result|override", "Mapa funcional do córtex, afasias e déficits corticais: aula 09 Organização morfofuncional do córtex (18/11)."),
 (r"limbic|Limbic|Papez|hippocamp|amygdala|Kluver|Klüver|amnesia|Korsakoff|Wernicke encephalopathy|Wernicke-Korsakoff|thiamine|Vitamin B|seizure|aura|hallucination|Hallucination", "Sistema límbico, memória e Wernicke-Korsakoff: aula 08 Sistema límbico (18/11)."),
 (r"direct|indirect|D 1|D 2|GABA|Glutamate|neurotransmitter|dopamin|Dopamin|tuberoinfundibular|Meynert|acetylcholine|internus|externus|internal and external segment|Parkinson|Wilson|deep brain|chorea|Chorea|Huntington disease is a neurological|inheritance of Huntington|movement-related|Symptoms of Huntington|presents initially with chorea|ventral tegmentum|movement disorders", "Circuitos, neurotransmissores e doenças dos núcleos da base: fisiologia e neurologia; a aula 04 é a topografia dos núcleos (Huntington entra como a associação clínica imediata do caudado)."),
 (r"VPL|VPM|ventral posterolateral|ventral posteromedial|Ventral anterior|ventral lateral|VA\) / Ventral|2nd-order|3rd-order|inferior colliculus sends|auditory information from the medial|thalamic relay|olfactory nerve|CN I|Cranial nerve I|cribriform|Thalamic pain|central poststroke|posterolateral thalamus|Friedreich|Nystagmus", "Núcleos talâmicos específicos e vias sensitivas: aula de vias/fisiologia; a aula 04 dá os grupos de núcleos com função geral."),
 (r"lateral area of the hypothalamus|anterior hypothalamus|posterior hypothalamus|[Pp]reoptic|dorsomedial|leptin|Leptin|ghrelin|Pyrogens|IL-1|osmolarity|TRH|CRH|Cortisol|GnRH|Kallmann|prolactin|Prolactin|antipsychotics|Typical antipsychotics|gynecomastia|Hypopituitarism|hypopituitarism|craniopharyngioma|Craniopharyngioma|Rathke|diabetes insipidus|Hypothalamic hormones|Dysfunction of the hypothalamus|Heat stroke|Fever|thermoregulation|Destruction of the hypothalamus|Bitemporal|bitemporal|optic chiasm \(|Exposure to cold", "Funções hormonais, térmicas e alimentares do hipotálamo e tumores da hipófise: fisiologia/endócrino; a aula 04 dá o nome e a região dos núcleos (entram só os núcleos que o professor nomeia, com a função clássica)."),
 (r"PICA|Wallenberg|Lateral medullary|nucleus ambiguus|vestibular portion|Weber|Medial midbrain|paramedian|lenticulostriate|[Ll]acunar|Pure motor|Putaminal|Subclavian steal|subclavian steal|dissection|Traumatic vascular|carotid sheath|external carotid|Branches of the subclavian artery may be remembered with the mnemonic \" V|deep branches of the posterior cerebral|splenium|anterior four-fifths|anterior limb of the internal capsule|genu/ posterior limb|Strokes involving the middle cerebral artery may cause hemineglect|Which anterior circulation stroke|Strokes involving the lenticulostriate", "Síndromes vasculares específicas e ramos profundos: neurologia clínica; a aula 04 dá o tronco arterial e o território cortical de cada artéria cerebral (uma associação clínica por artéria cerebral entra)."),
 (r"striatum , which consists|components of the basal ganglia that are located in the diencephalon|substantia nigra , which is located|substantia nigra appears|Substantia nigra|One component of the basal ganglia is the substantia", "Nomenclatura divergente da aula: o professor e a apostila chamam de corpo estriado o lentiforme + caudado e não incluem substância negra e subtalâmico nos núcleos da base (Machado concorda); o card segue a aula."),
 (r"forebrain|prosencephalon|Alzheimer|lower limbs are located in the medial", "Embriologia e mapa somatotópico: AN01 e aula 09; não é a topografia da aula 04."),
]
EXPLICITO = {}


def motivo(nid, texto):
    if nid in EXPLICITO:
        return EXPLICITO[nid]
    if nid in DUPLICA:
        return f"duplica {DUPLICA[nid]}: a mesma relação já entra por outra nota (viva NEBLI ou AnKing escolhido), com histórico."
    for rx, m in CAT:
        if re.search(rx, texto):
            return m
    return None


RES_FORA = {}
SUSPENSOS_OUTRAS = []

# 09/11 — conjunto final de AnKing que entra (ak_textos.py, traduzidos); o resto das seções fica com motivo
import ak_textos as _akt
AK_NOVOS = {n: f"ak-{n}" for n in _akt.AK}
for _n in list(DUPLICA):
    if _n in AK_NOVOS: DUPLICA.pop(_n)

# 09/11 — cópias NEBLI vivas (suspensas em outra aula) usadas no lugar da tradução nova; repetidos e Only_Step_2 fora
for _n, _viva in ((1481513119712, 1792261811050), (1481596917147, 1792348022615), (1481513164343, 1792350078186)):
    AK_NOVOS.pop(_n, None); DUPLICA[_n] = _viva
for _n in (1550673159267, 1480995218951, 1480995234166, 1481513227002):
    AK_NOVOS.pop(_n, None)
EXPLICITO.update({1550673159267: "Fonte Only_Step_2 (gate F-20261105-CODEX-05): a relação III × artérias entra pelo aneurisma da comunicante posterior (1481772053364).",
 1480995218951: "Repete a resposta 'basilar' do card da síndrome do encarceramento; a irrigação da ponte medial fica no organizador vertebrobasilar.",
 1480995234166: "Repete a resposta 'cerebral posterior' do card do lobo occipital; o mesencéfalo pela ACP entra na síndrome de Weber.",
 1481513227002: "Repete a resposta 'cerebral posterior'; o território inferior da ACP está no organizador de territórios."})
SUSPENSOS_OUTRAS = [(1792348874065, "Identificação do sulco calcarino em texto (AnKing ID), suspensa: o sulco já tem IO Kenhub nesta aula (uma estrutura = um card)."),
 (1792350078435, "ACA no ramo anterior da cápsula interna: ramo profundo, detalhe além da aula (o professor dá só o território cortical); fica na reserva.")]

_ID = "Identificação em texto (ID do vaso), suspensa na reserva: a estrutura já tem IO do Kenhub nesta aula (uma estrutura = um card)."
_ORG = "Frase da reserva (22/10) que repete o que um organizador ou IO desta aula já cobra; fica na reserva com o histórico."
_FORA = "Assunto de outra aula ou detalhe além do que o professor ensina (seios venosos: aula 06; ramos corticais nomeados e posição do cerebelo: fora)."
SUSPENSOS_OUTRAS += [(n, _ID) for n in (1792350079185, 1792350089409, 1792350092237, 1792350094637, 1792350097361)]
SUSPENSOS_OUTRAS += [(n, _ORG) for n in (1792588687043, 1792588687044, 1792588687052, 1792588687054, 1792588687055, 1792588687056, 1792588687060, 1792588687063, 1792588687064, 1792588687069, 1792588687072, 1792588687088, 1792588687094)]
SUSPENSOS_OUTRAS += [(n, _FORA) for n in (1792351070557, 1792588687018, 1792588687096, 1792588687097, 1792588687098, 1792588687100, 1792588687102)]
for _n in (1481418800702, 1481418808669):
    AK_NOVOS.pop(_n, None)
    EXPLICITO[_n] = "Repete a resposta (anterior/posterior) dos aneurismas das comunicantes; a termorregulação do hipotálamo fica nos cards da reserva (anterior parassimpático, posterior simpático)."

SUSPENSOS_OUTRAS += [(1792351070557,'outro assunto: drenagem venosa e seios da dura, conteúdo da aula06, não da transcrição desta aula04.'),(1792350078435,'outro assunto: território perfurante do braço anterior da cápsula interna; a transcrição04 delimita aqui territórios corticais, não os ramos profundos.'),(1792588687097,'outro assunto: nomenclatura de ramos temporais inferiores específicos da cerebral posterior; a transcrição04 não ensina estes nomes, apenas território occipital/inferomedial.')]
