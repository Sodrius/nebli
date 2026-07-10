"""
Classificador de questões do banco NEBLI → aula UC01/UC02.

Uso:
    python3 banco/classifier.py            # processa só questões com `aula:` vazio
    python3 banco/classifier.py --all      # reclassifica todas
    python3 banco/classifier.py --dry-run  # só gera relatório, não escreve

Saída:
    banco/indice/classificacao_proposta.json  — top-3 candidatas + score por questão
    banco/indice/classificacao_revisao.md     — tabela legível para revisão humana
"""
from __future__ import annotations
import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SLIM = ROOT / "banco" / "indice" / "banco_slim.json"
AULAS_UC01 = ROOT / "banco" / "aulas_uc01.yml"
AULAS_UC02 = ROOT / "banco" / "aulas_uc02.yml"
OUT_JSON = ROOT / "banco" / "indice" / "classificacao_proposta.json"
OUT_MD = ROOT / "banco" / "indice" / "classificacao_revisao.md"

# Limiares
THRESHOLD_OK = 0.30        # abaixo disso: deixa aula vazia (UC03+ futuras)
THRESHOLD_AMBIG = 0.15     # diferença 1º↔2º abaixo disso: ambíguo

# -----------------------------------------------------------------------------
# Vocabulário de aula: título + sinônimos curados
# -----------------------------------------------------------------------------
# Cada slug aponta para um set de keywords (já normalizadas: minúsculas, sem
# acento, sem hífen). O classificador faz overlap entre essas keywords e o
# texto da questão (tags + conceito_central, normalizado igual).
#
# Sinônimos foram extraídos de:
#  - títulos das aulas (UC01 + UC02)
#  - jargão médico recorrente nas questões do banco
#  - sigla ↔ por extenso (ATP, NADH, Km, Vmax, PA, MEC, etc.)

SINONIMOS: dict[str, list[str]] = {
    # ----- UC01 — BIOQUÍMICA -----
    "bioq-01-reacoes-quimicas": [
        "reacao", "reacoes", "espontaneidade", "cinetica", "termodinamica",
        "energia livre", "gibbs", "delta g", "entalpia", "entropia",
        "endergonica", "exergonica", "equilibrio quimico",
    ],
    "bioq-02-ph-tampoes": [
        "ph", "tampao", "tampoes", "buffer", "henderson hasselbalch",
        "pka", "acidez", "basicidade", "acido base", "bicarbonato",
        "fosfato tampao", "ionizacao",
    ],
    "bioq-03-lipideos": [
        "lipideo", "lipideos", "lipidio", "lipidios", "acido graxo",
        "triglicerideo", "fosfolipideo", "colesterol", "esfingolipideo",
        "surfactante", "sindrome desconforto respiratorio", "sdr",
        "esterificacao", "saponificacao", "saturado", "insaturado",
    ],
    "bioq-04-aminoacidos": [
        "aminoacido", "aminoacidos", "ligacao peptidica", "zwitterion",
        "ponto isoeletrico", "pi", "cadeia lateral", "polar apolar",
        "carga aminoacido", "essencial", "ramificada",
    ],
    "bioq-05-proteinas-estrutura": [
        "proteina", "proteinas", "estrutura secundaria", "estrutura terciaria",
        "estrutura quaternaria", "alfa helice", "folha beta", "dobramento",
        "enovelamento", "chaperona", "desnaturacao", "renaturacao",
    ],
    "bioq-06-agregacao-proteinas": [
        "agregacao proteina", "amiloide", "fibrila", "doenca priônica",
        "alzheimer", "parkinson", "huntington", "misfolding",
        "encefalopatia espongiforme",
    ],
    "bioq-07-purificacao-proteinas": [
        "purificacao", "cromatografia", "afinidade", "troca ionica",
        "exclusao molecular", "eletroforese", "sds page",
        "diálise", "salting out", "western blot",
    ],
    "bioq-08a-hemoglobina-I": [
        "hemoglobina", "hb", "heme", "globina", "porfirina",
        "ligacao oxigenio", "cooperatividade", "curva sigmoide",
        "p50", "alostérico", "alostérica",
    ],
    "bioq-08b-hemoglobina-II": [
        "hemoglobina", "bohr", "efeito bohr", "bpg", "2 3 bisfosfoglicerato",
        "co2 hemoglobina", "carbaminohemoglobina", "monoxido carbono",
        "anemia falciforme", "talassemia", "hbf", "hba",
    ],
    "bioq-10-enzimas-I-cinetica": [
        "enzima", "enzimas", "cinetica enzimatica", "michaelis menten",
        "km", "vmax", "lineweaver burk", "estado estacionario",
        "constante catalitica", "kcat", "turnover", "atividade enzimatica",
    ],
    "bioq-11-enzimas-II-regulacao": [
        "inibicao", "inibidor", "competitivo", "nao competitivo",
        "acompetitivo", "alostérico", "regulacao enzimatica",
        "modulador", "fosforilacao enzima", "irreversivel reversivel",
    ],
    "bioq-12-cinetica-enzimatica-lab": [
        "laboratorio cinetica", "ensaio enzimatico", "espectrofotometria",
        "atividade especifica",
    ],
    "bioq-13-carboidratos": [
        "carboidrato", "carboidratos", "monossacarideo", "dissacarideo",
        "polissacarideo", "glicose estrutura", "frutose", "galactose",
        "sacarose", "lactose", "amido", "glicogenio estrutura",
        "ligacao glicosidica", "anomero", "epimero",
    ],
    "bioq-14-introducao-metabolismo": [
        "metabolismo introducao", "anabolismo", "catabolismo",
        "atp moeda energetica", "via metabolica", "regulacao metabolismo",
        "estado alimentado", "estado jejum",
    ],
    "bioq-15-glicolise": [
        "glicolise", "hexoquinase", "glicoquinase", "fosfofrutoquinase",
        "pfk", "piruvato quinase", "piruvato", "fosfoenolpiruvato", "pep",
        "frutose 1 6 bisfosfato", "gliceraldeido 3 fosfato",
        "g6p", "f6p", "lactato desidrogenase", "fermentacao lactica",
    ],
    "bioq-16-gliconeogenese": [
        "gliconeogenese", "piruvato carboxilase", "pep carboxiquinase",
        "frutose 1 6 bisfosfatase", "glicose 6 fosfatase", "g6pase",
        "ciclo cori", "deficiencia g6pase", "doenca von gierke",
        "lactato gliconeogenese", "alanina gliconeogenese",
    ],
    "bioq-17-ciclo-krebs-TE-I": [
        "krebs", "ciclo krebs", "acidos tricarboxilicos", "tca",
        "citrato", "isocitrato", "alfa cetoglutarato",
        "succinato", "fumarato", "malato", "oxaloacetato",
        "acetil coa", "citrato sintase", "isocitrato desidrogenase",
        "transporte eletrons", "cadeia respiratoria", "complexo i",
        "complexo iii", "ubiquinona", "citocromo c",
    ],
    "bioq-18-transporte-eletrons-II": [
        "transporte eletrons", "fosforilacao oxidativa", "atp sintase",
        "complexo iv", "complexo v", "gradiente protonico",
        "forca proton motriz", "desacoplador", "dnp", "rotenona",
        "antimicina", "cianeto", "coenzima q10", "deficiencia coq10",
    ],
    "bioq-19-simulacao-mitocondrial": [
        "simulacao mitocondrial", "respiracao mitocondrial",
        "consumo oxigenio", "controle respiratorio",
    ],

    # ----- UC01 — FISIOLOGIA -----
    "fisio-01-introducao": [
        "homeostase", "compartimentos", "liquido extracelular", "lec",
        "liquido intracelular", "lic", "tonicidade", "isotonico",
        "hipotonico", "hipertonico", "osmolaridade", "osmose volume",
        "volume celular", "cannon", "retrorregulacao",
        "retrorregulacao negativa", "feedback negativo homeostase",
        "compartimento corporal", "agua corporal total", "sistema integracao fisiologica",
    ],
    "fisio-02-transporte-membrana": [
        "transporte membrana", "difusao simples", "difusao facilitada",
        "transporte ativo", "transporte ativo primario", "transporte ativo secundario",
        "bomba na k", "bomba sodio potassio", "atpase", "simporte",
        "antiporte", "uniporte", "carregador", "transportador",
        "canal ionico", "glut", "sglt", "potencial eletroquimico",
    ],
    "fisio-03-potencial-repouso": [
        "potencial repouso", "potencial membrana", "equilibrio nernst",
        "equacao nernst", "goldman", "ghk", "constante goldman",
        "permeabilidade potassio", "permeabilidade sodio",
        "canal vazamento", "canais vazamento", "leak channel",
        "potencial equilibrio",
    ],
    "fisio-04-propriedades-passivas": [
        "propriedades passivas", "constante tempo", "tau",
        "constante espaco", "lambda", "resistencia membrana",
        "capacitancia", "rm", "cm", "ri", "cabo",
        "conducao eletrotonica", "decaimento exponencial",
    ],
    "fisio-05-potencial-acao": [
        "potencial acao", "pa", "despolarizacao", "repolarizacao",
        "hiperpolarizacao", "limiar", "canal sodio voltagem",
        "canal potassio voltagem", "periodo refratario",
        "absoluto refratario", "relativo refratario",
        "propagacao potencial", "conducao saltatoria", "mielina",
        "no ranvier", "velocidade conducao",
    ],
    "fisio-06-transmissao-sinaptica": [
        "sinapse", "transmissao sinaptica", "neurotransmissor",
        "acetilcolina", "noradrenalina", "glutamato sinapse", "gaba",
        "juncao neuromuscular", "jnm", "placa motora",
        "vesicula sinaptica", "snare", "exocitose vesicula",
        "ach", "fenda sinaptica", "receptor nicotinico",
        "pps", "peps", "epsp", "ipsp", "soma temporal", "soma espacial",
        "ltp", "ltd", "potenciacao longa", "depressao sinaptica",
        "long term potentiation", "plasticidade sinaptica",
        "ionotropico", "metabotropico", "nmda", "ampa", "kainato",
        "excitotoxicidade", "neuromodulacao", "neuromodulador",
        "sinapse eletrica", "sinapse quimica", "conexina", "gap junction",
        "junçao gap", "co transmissor", "neuropeptideo",
        "quanta vesicula", "liberacao multivesicular",
        "adenosina neuromodulador",
        "inibicao pre sinaptica", "retrogrado sinapse",
    ],
    "fisio-07-sinalizacao-I": [
        "sinalizacao", "receptor", "gpcr",
        "receptor acoplado proteina g", "proteina g", "amp ciclico",
        "camp", "amp", "adenilato ciclase", "ip3", "dag", "fosfolipase c",
        "segundo mensageiro", "primeiro mensageiro", "ligante",
        "afinidade receptor", "agonista", "antagonista",
        "receptor tirosina quinase", "rtk",
        "adrenergica", "adrenergico", "noradrenalina sinalizacao",
        "dopamina receptor", "receptor d1", "receptor d2",
        "muscarinico", "nicotinico sinalizacao",
        "histamina receptor", "serotonina receptor",
    ],
    "fisio-08-sinalizacao-II": [
        "sinalizacao ii", "sinalizacao intracelular", "cascata sinalizacao",
        "mapk", "pka", "pkc", "calmodulina", "cam", "calcio sinalizacao",
        "dessensibilizacao", "regulacao receptor", "internalizacao receptor",
        "receptor nuclear", "esteroide receptor",
    ],
    "fisio-09-transporte-agua": [
        "transporte agua", "aquaporina", "aquaporinas", "aqp",
        "osmose tecido", "pressao osmotica", "pressao oncotica",
        "permeabilidade agua", "fluxo agua", "tubulo renal agua",
    ],

    # ----- UC01 — BIOLOGIA CELULAR -----
    "biocel-01-membrana-bicamada": [
        "membrana plasmatica", "bicamada lipidica", "fluidez membrana",
        "modelo mosaico fluido", "balsas lipidicas", "lipid raft",
        "proteina membrana", "proteina integral", "proteina periferica",
        "glicocalice",
    ],
    "biocel-02-tecnicas-citoesqueleto": [
        "citoesqueleto", "actina", "microtubulo", "microtubulos",
        "filamento intermediario", "miosina", "cinesina", "dineina",
        "microscopia", "imunofluorescencia", "centríolo",
        "centro organizador microtubulos", "moc",
    ],
    "biocel-03-compartimentos-I": [
        "compartimento intracelular", "reticulo endoplasmatico",
        "re", "rer", "rel", "sinal peptideo", "srp", "translocacao",
        "proteina co traducional",
    ],
    "biocel-04-compartimentos-II": [
        "golgi", "complexo golgi", "vesicula transporte", "copi", "copii",
        "clatrina", "trafego vesicular", "secrecao constitutiva",
        "secrecao regulada", "endossomo",
    ],
    "biocel-05-compartimentos-III": [
        "lisossomo", "peroxissomo", "mitocondria estrutura",
        "matriz mitocondrial", "membrana mitocondrial",
        "importacao mitocondrial", "tom tim", "autofagia", "autofagossomo",
    ],
    "biocel-06-nucleo-interfasico": [
        "nucleo", "envelope nuclear", "poro nuclear", "lamina nuclear",
        "cromatina", "heterocromatina", "eucromatina", "nucleolo",
        "importacao nuclear", "nls", "transporte nucleo",
    ],
    "biocel-07-divisao-celular": [
        "divisao celular", "mitose", "meiose", "ciclo celular",
        "g1", "s fase", "g2", "fuso mitotico", "cinetocoro",
        "ciclina", "cdk", "checkpoint", "ponto controle ciclo",
        "interfase",
    ],
    "biocel-08-morte-celular": [
        "morte celular", "apoptose", "necrose", "necroptose",
        "caspase", "bcl 2", "bax", "citocromo c apoptose",
        "via intrinseca", "via extrinseca", "fas", "tnf",
        "autofagia morte", "piroptose",
    ],

    # ----- UC01 — BIOLOGIA MOLECULAR -----
    "biomol-20-acidos-nucleicos": [
        "acido nucleico", "dna estrutura", "rna estrutura", "nucleotideo",
        "base nitrogenada", "purina", "pirimidina", "watson crick",
        "dupla helice", "antiparalelo", "ligacao fosfodiester",
        "estrutura primaria dna", "denaturacao dna",
    ],
    "biomol-21-replicacao-dna": [
        "replicacao dna", "polimerase dna", "primer", "primase",
        "okazaki", "topoisomerase", "helicase", "telomere",
        "telomerase", "leading strand", "lagging strand",
        "fragmento okazaki", "ligase",
    ],
    "biomol-22-transcricao": [
        "transcricao", "rna polimerase", "promotor", "fator transcricao",
        "tata box", "splicing", "intron", "exon", "capping",
        "poliadenilacao", "pre mrna", "mrna maduro",
    ],
    "biomol-23-traducao": [
        "traducao", "codigo genetico", "codon", "anticodon",
        "trna", "ribossomo", "iniciacao traducao", "alongamento",
        "terminacao", "fator iniciacao", "aminoacil trna sintetase",
        "wobble",
    ],
    "biomol-24-regulacao-expressao": [
        "regulacao expressao genica", "operon", "lac operon", "trp operon",
        "epigenetica", "metilacao dna", "acetilacao histona",
        "fator transcricao especifico", "silenciamento gene",
        "remodelamento cromatina",
    ],

    # ----- UC02 — BIOLOGIA MOLECULAR (continuação) -----
    "biomol-25-mutacao-reparo-recombinacao": [
        "mutacao", "lesao dna", "reparo dna", "ner", "ber", "mmr",
        "recombinacao homologa", "transposon", "elemento movel",
        "raio uv dna", "agente mutagenico", "frameshift",
        "missense", "nonsense", "silenciosa mutacao",
    ],
    "biomol-26-dna-recombinante-pcr": [
        "dna recombinante", "clonagem molecular", "pcr",
        "reacao cadeia polimerase", "sequenciamento dna", "sanger",
        "plasmideo vetor", "enzima restricao", "ligase clonagem",
        "primer pcr", "taq polimerase", "eletroforese gel",
    ],
    "biomol-27-bacterias-patogenicas": [
        "bacteria patogenica", "identificacao bacteria",
        "16s rrna", "ribotipagem", "diagnostico molecular",
        "gram positiva", "gram negativa", "patogeno",
    ],

    # ----- UC02 — BIOLOGIA CELULAR (continuação) -----
    "biocel-09-diferenciacao-celular": [
        "diferenciacao celular", "celula tronco", "stem cell",
        "pluripotencia", "totipotencia", "compromisso celular",
        "linhagem celular", "fator transcricao diferenciacao",
        "reprogramacao",
    ],

    # ----- UC02 — HISTOLOGIA -----
    "histo-01-intro-tecidos-sangue": [
        "introducao histologia", "tecidos basicos", "celulas sangue",
        "eritrocito", "leucocito", "plaqueta", "esfregaco sangue",
        "hemacia", "neutrofilo histologia", "linfocito histologia",
        "monocito", "basofilo", "eosinofilo",
    ],
    "histo-02-hematopoese": [
        "hematopoese", "medula ossea hematopoese", "celula tronco hematopoetica",
        "linhagem mieloide", "linhagem linfoide", "eritropoese",
        "trombopoese", "granulopoese", "eritropoetina",
        "granulocito", "granulopoetico", "granulopoetica", "granulopoiese",
        "g csf", "gm csf", "fator estimulador colonia",
        "desvio esquerda neutrofilo", "neutrofilo imaturo", "metamielocito",
        "bastonete neutrofilo", "promielocito", "mieloblasto",
    ],
    "histo-03-tecidos-epiteliais": [
        "epitelio", "tecido epitelial", "epitelio simples",
        "epitelio estratificado", "pseudo estratificado", "junçao apertada",
        "tight junction", "desmossomo", "hemidesmossomo", "gap junction",
        "membrana basal epitelio", "polaridade epitelial", "microvilo",
        "cilio epitelio",
    ],
    "histo-04-tecido-conjuntivo": [
        "tecido conjuntivo", "matriz extracelular", "mec",
        "fibroblasto", "colageno", "elastina", "proteoglicano",
        "glicosaminoglicano", "gag", "fibronectina", "laminina",
        "substancia fundamental", "fibra elastica", "fibra reticular",
        "conjuntivo frouxo", "conjuntivo denso",
    ],
    "histo-05-tecido-adiposo": [
        "tecido adiposo", "adipocito", "gordura branca", "gordura marrom",
        "lipogenese histologia", "leptina histologia", "ucp1",
        "adiposo unilocular", "adiposo multilocular",
    ],
    "histo-06-metastase-epitelio-conjuntivo": [
        "metastase", "interacao epitelio conjuntivo",
        "transicao epitelio mesenquimal", "emt", "invasao tumoral",
        "metaloproteinase", "mmp",
    ],
    "histo-07-cartilaginoso-osseo": [
        "cartilagem", "condrocito", "tecido osseo", "osteocito",
        "osteoblasto", "osteoclasto", "matriz ossea", "hidroxiapatita",
        "osso compacto", "osso esponjoso", "osteoide",
        "cartilagem hialina", "cartilagem elastica", "fibrocartilagem",
        "pericondrio", "endosteo", "periosteo histo",
        "ossificacao", "ossificacao endocondral", "ossificacao intramembranosa",
        "celulas osseas", "histogenese cartilagem", "nutricao ossea",
        "lacuna osteocito", "canaliculo osseo", "haversiano", "havers",
    ],
    "histo-08-tecido-muscular": [
        "tecido muscular", "musculo esqueletico", "musculo liso",
        "musculo cardiaco", "sarcomero", "actina miosina contracao",
        "linha z", "banda a", "banda i", "disco intercalar",
        "fibra muscular", "actino miosina", "acoplamento excitacao contracao",
        "tubulo t", "reticulo sarcoplasmatico", "diade", "triade",
        "tropomiosina", "troponina", "filamento espesso", "filamento fino",
        "musculatura", "musculos",
    ],
    "histo-09-vasos-sanguineos-linfaticos": [
        "vaso sanguineo", "arteria histologia", "veia histologia",
        "capilar", "tunica intima", "tunica media", "tunica adventicia",
        "vaso linfatico",
    ],
    "histo-10-tecido-nervoso": [
        "tecido nervoso", "neuronio histologia", "neuroglia",
        "astrocito", "oligodendrocito", "microglia", "celula schwann",
        "bainha mielina", "axonio histologia", "dendrito",
    ],
    "histo-11-orgaos-linfaticos": [
        "orgao linfatico", "linfonodo", "baço", "timo histologia",
        "tonsila", "amigdala", "placa peyer", "malt", "balt",
        "centro germinativo",
    ],

    # ----- UC02 — ANATOMIA -----
    "anato-01-intro-planos-eixos": [
        "introducao anatomia", "plano sagital", "plano coronal",
        "plano transverso", "eixo anatomico", "posicao anatomica",
        "termos direcao anatomica",
    ],
    "anato-02-ossos-generalidades": [
        "osso anatomia", "esqueleto axial", "esqueleto apendicular",
        "tipos ossos", "osso longo", "osso curto", "osso plano",
        "periosteo", "endosteo", "cintura escapular", "cintura pelvica",
        "epifise", "diafise", "metafise", "ossos cranio",
    ],
    "anato-03-articulacoes": [
        "articulacao", "sinartrose", "anfiartrose", "diartrose",
        "articulacao sinovial", "capsula articular",
        "ligamento articular", "menisco",
    ],
    "anato-04-musculos": [
        "musculo anatomia", "origem insercao", "agonista antagonista",
        "musculo esqueletico anatomia", "tendao", "fascia",
        "insercoes musculares", "sistema alavancas", "acao muscular",
        "movimento articular", "flexor", "extensor",
    ],
    "anato-05-circulatorio-linfatico-I": [
        "sistema circulatorio anatomia", "coracao anatomia",
        "grande circulacao", "pequena circulacao", "arteria aorta",
        "atrio ventriculo", "valva cardiaca",
    ],
    "anato-06-circulatorio-linfatico-II": [
        "sistema linfatico anatomia", "ducto toracico",
        "linfonodo anatomia", "ramo circulatorio",
    ],

    # ----- UC02 — BIOQUÍMICA (continuação) -----
    "bioq-20-pentoses-radicais-livres": [
        "via pentoses", "pentose fosfato", "g6pd",
        "glicose 6 fosfato desidrogenase", "nadph",
        "ribose 5 fosfato", "radical livre", "ros",
        "especie reativa oxigenio", "estresse oxidativo",
        "superoxido dismutase", "sod", "catalase",
        "glutationa peroxidase", "anti oxidante",
    ],
    "bioq-21-lipideos-rotas": [
        "metabolismo lipideos", "beta oxidacao", "sintese acido graxo",
        "lipogenese", "lipolise", "carnitina", "acil coa",
        "malonil coa", "acido graxo sintase", "fas",
        "cetogenese", "corpo cetonico", "acetoacetato",
        "beta hidroxibutirato",
    ],
    "bioq-22-lipideos-regulacao": [
        "regulacao lipideos", "regulacao lipogenese", "regulacao beta oxidacao",
        "srebp", "insulina lipideos", "glucagon lipideos",
        "acc fosforilacao", "hsl", "lipase hormonio sensivel",
    ],
    "bioq-23-aminoacidos-ureia": [
        "metabolismo aminoacido", "ciclo ureia", "transaminase",
        "ast", "alt", "glutamato desidrogenase", "amonia",
        "carbamoil fosfato", "ornitina", "citrulina", "arginina ureia",
        "transaminacao", "desaminacao oxidativa",
    ],
    "bioq-24-glicogenio": [
        "glicogenio", "glicogenese", "glicogenolise",
        "glicogenio sintase", "glicogenio fosforilase",
        "udp glicose", "enzima ramificadora", "enzima desramificadora",
        "doença armazenamento glicogenio", "von gierke glicogenio",
        "pompe", "mcardle",
    ],
    "bioq-25-depuracao": [
        "depuracao", "funcoes depuracao", "filtracao glomerular",
        "clearance", "metabolismo xenobiotico", "citocromo p450",
        "biotransformacao",
    ],

    # ----- UC02 — EMBRIOLOGIA -----
    "embrio-01-gametogenese-fertilizacao": [
        "gametogenese", "espermatogenese", "ovogenese", "fertilizacao",
        "fecundacao", "zigoto", "espermatozoide", "ovocito",
        "reacao acrossomica",
    ],
    "embrio-02-blastocisto-gastrulacao": [
        "blastocisto", "gastrulacao", "morula", "implantacao embriao",
        "trofoblasto", "embrioblasto", "epiblasto", "hipoblasto",
        "linha primitiva", "tres folhetos germinativos",
        "ectoderma", "mesoderma", "endoderma",
    ],
    "embrio-03-neurulacao": [
        "neurulacao", "tubo neural", "placa neural",
        "crista neural", "defeito tubo neural",
    ],

    # ----- UC02 — IMUNOLOGIA -----
    "imuno-01-disturbios-imunidade": [
        "distúrbio imunidade", "imunodeficiencia", "alergia",
        "autoimunidade", "hipersensibilidade",
        "comunicacao quimica defesa", "citocina defesa",
        "anticorpo", "linfocito b", "linfocito t",
        "imunoglobulina", "antigeno",
    ],
}

# Palavras vazias que aparecem em títulos mas não devem pontuar isoladamente
STOPWORDS = {
    "a", "ao", "as", "da", "das", "de", "do", "dos", "e", "em", "no",
    "na", "nos", "nas", "o", "os", "para", "por", "que", "se", "sobre",
    "um", "uma", "uns", "umas", "com", "sem", "ou", "i", "ii", "iii",
    "introducao", "estrutura", "estudos", "estudo", "funcao", "principios",
    "principio", "tipos", "tipo", "geral", "generalidades",
    "regulacao", "metabolismo",  # genéricos demais
    # Letras gregas isoladas — α-hélice/β-folha vs receptor α/β cruzam falsamente
    "alfa", "beta", "gama", "gamma", "delta", "epsilon", "zeta", "teta",
    "lambda", "sigma", "tau", "omega", "kappa",
    # Tokens genéricos que aparecem em quase toda questão biomédica
    "celular", "celulares", "celula", "celulas",
    "intracelular", "extracelular", "membrana", "via", "tecido", "tecidos",
    "sistema", "sistemas", "molecular", "molecula", "moleculas",
}

# Sinônimos de equivalência grafia (questão ↔ índice)
# Substituídos no texto da questão ANTES da tokenização
NORMALIZACOES = {
    "hematopoiese": "hematopoese",
    "hematopoietica": "hematopoese",
    "hematopoieticas": "hematopoese",
    "hematopoietico": "hematopoese",
    "adrenergico": "adrenergica adrenergico noradrenalina",
    "adrenergica": "adrenergica adrenergico noradrenalina",
    "adrenergicos": "adrenergica adrenergico noradrenalina",
}


def normalizar(texto: str) -> str:
    """Minúsculas, sem acento, sem pontuação não-alfanumérica, com normalizações de grafia."""
    if not texto:
        return ""
    n = unicodedata.normalize("NFD", texto)
    n = "".join(c for c in n if unicodedata.category(c) != "Mn")
    n = n.lower()
    n = re.sub(r"[^a-z0-9\s]+", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    # aplica equivalências
    palavras = n.split()
    expandidas = []
    for p in palavras:
        if p in NORMALIZACOES:
            expandidas.extend(NORMALIZACOES[p].split())
        else:
            expandidas.append(p)
    return " ".join(expandidas)


def tokens_de_titulo(titulo: str) -> set[str]:
    """Extrai tokens significativos do título da aula."""
    norm = normalizar(titulo)
    palavras = [p for p in norm.split() if len(p) > 2 and p not in STOPWORDS]
    return set(palavras)


def construir_indice_aula(aula: dict) -> set[str]:
    """Une tokens do título + sinônimos curados."""
    slug = aula["slug"]
    kws = tokens_de_titulo(aula["titulo"])
    sins = SINONIMOS.get(slug, [])
    for s in sins:
        kws.update(normalizar(s).split())
    # remove stopwords residuais
    kws = {k for k in kws if k not in STOPWORDS and len(k) > 2}
    return kws


def carregar_aulas() -> list[dict]:
    aulas = []
    for path in [AULAS_UC01, AULAS_UC02]:
        with open(path, encoding="utf-8") as f:
            d = yaml.safe_load(f)
        for a in d["aulas"]:
            a["uc"] = d["uc"]
            aulas.append(a)
    return aulas


def carregar_banco() -> dict:
    with open(SLIM, encoding="utf-8") as f:
        return json.load(f)


def texto_questao(q: dict) -> tuple[set[str], list[str]]:
    """Retorna (tokens, tags_originais) da questão para scoring."""
    tags = q.get("tags", []) or []
    tag_tokens: set[str] = set()
    for t in tags:
        tag_tokens.update(normalizar(t).split())
    conceito_tokens = set(normalizar(q.get("conceito_central", "")).split())
    conceito_tokens.update(normalizar(q.get("armadilha", "")).split())
    return (tag_tokens | conceito_tokens), tags


def scorear(q_tokens: set[str], aula_kws: set[str]) -> tuple[float, list[str]]:
    """Score = sobreposição normalizada + lista de keywords casadas."""
    if not aula_kws:
        return 0.0, []
    casadas = [k for k in aula_kws if k in q_tokens]
    if not casadas:
        return 0.0, []
    # Score: nº casamentos / sqrt(tamanho do vocabulário da aula)
    # — penaliza aulas com vocabulário muito grande sem virar zero
    import math
    score = len(casadas) / math.sqrt(len(aula_kws))
    return score, casadas


def classificar(banco: dict, aulas: list[dict], reclassificar_tudo: bool) -> dict:
    indices = {a["slug"]: construir_indice_aula(a) for a in aulas}
    aula_por_slug = {a["slug"]: a for a in aulas}

    resultado: dict = {"propostas": [], "estatisticas": {}}
    contadores = Counter()

    for q in banco["questoes"]:
        aula_atual = q.get("aula") or ""
        if aula_atual and not reclassificar_tudo:
            resultado["propostas"].append({
                "id": q["id"],
                "aula_atual": aula_atual,
                "decisao": "preservar",
                "candidatas": [],
                "conceito_central": q.get("conceito_central", "")[:120],
                "tags": q.get("tags", []),
            })
            contadores["preservadas"] += 1
            continue

        q_tokens, _ = texto_questao(q)
        scores = []
        for slug, kws in indices.items():
            s, casadas = scorear(q_tokens, kws)
            if s > 0:
                scores.append((s, slug, casadas))
        scores.sort(reverse=True, key=lambda x: x[0])
        top3 = scores[:3]

        if not top3:
            decisao = "vazia"
            contadores["sem_match"] += 1
        elif top3[0][0] < THRESHOLD_OK:
            decisao = "vazia"
            contadores["score_baixo"] += 1
        elif len(top3) >= 2 and (top3[0][0] - top3[1][0]) < THRESHOLD_AMBIG:
            decisao = "ambigua"
            contadores["ambigua"] += 1
        else:
            decisao = "ok"
            contadores["ok"] += 1

        resultado["propostas"].append({
            "id": q["id"],
            "aula_atual": aula_atual,
            "decisao": decisao,
            "candidatas": [
                {"slug": s, "score": round(sc, 3), "casadas": list(km)[:8]}
                for sc, s, km in top3
            ],
            "conceito_central": q.get("conceito_central", "")[:140],
            "tags": q.get("tags", []),
        })

    resultado["estatisticas"] = dict(contadores)
    resultado["estatisticas"]["total"] = len(banco["questoes"])
    return resultado


def gerar_md(prop: dict, aulas: list[dict]) -> str:
    aula_titulo = {a["slug"]: a["titulo"] for a in aulas}
    stats = prop["estatisticas"]
    linhas = [
        "# Revisão da classificação proposta — banco NEBLI",
        "",
        f"**Total:** {stats.get('total',0)} questões",
        f"- Preservadas (já tinham `aula:`): **{stats.get('preservadas',0)}**",
        f"- Match confiante (ok): **{stats.get('ok',0)}**",
        f"- Ambíguas (revisar): **{stats.get('ambigua',0)}**",
        f"- Score baixo / sem match (aula vazia → UC03+): **{stats.get('score_baixo',0) + stats.get('sem_match',0)}**",
        "",
        "## Como revisar",
        "1. Veja as seções abaixo na ordem: `ok` → `ambigua` → `vazia` → `preservar`.",
        "2. Para cada questão, confira se o top-1 faz sentido. Se não, anote o slug correto.",
        "3. Devolva ajustes para o orquestrador aplicar.",
        "",
    ]

    grupos = {"ok": [], "ambigua": [], "vazia": [], "preservar": []}
    for p in prop["propostas"]:
        grupos[p["decisao"]].append(p)

    for nome, titulo in [
        ("ok", "✅ OK — match confiante"),
        ("ambigua", "⚠️  AMBÍGUA — top-1 e top-2 próximos"),
        ("vazia", "🔍 VAZIA — score baixo (provável UC03+)"),
        ("preservar", "🔒 PRESERVADAS (já classificadas)"),
    ]:
        items = grupos[nome]
        if not items:
            continue
        linhas.append(f"\n## {titulo} ({len(items)} questões)\n")
        if nome == "preservar":
            # listagem compacta
            linhas.append("| ID | Aula atual |")
            linhas.append("|----|------------|")
            for p in items[:30]:
                linhas.append(f"| {p['id']} | `{p['aula_atual']}` |")
            if len(items) > 30:
                linhas.append(f"| ... | (+{len(items)-30} omitidas) |")
            continue

        linhas.append("| ID | Top-1 (score) | Top-2 (score) | Top-3 (score) | Conceito |")
        linhas.append("|----|---------------|---------------|---------------|----------|")
        for p in items:
            c = p["candidatas"]
            def fmt(i):
                if i >= len(c): return ""
                slug = c[i]["slug"]
                t = aula_titulo.get(slug, "?")[:35]
                return f"`{slug}` ({c[i]['score']}) — {t}"
            linhas.append(
                f"| {p['id']} | {fmt(0)} | {fmt(1)} | {fmt(2)} | {p['conceito_central'][:90]} |"
            )

    return "\n".join(linhas)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true",
                        help="reclassifica todas (inclusive as que já têm aula)")
    parser.add_argument("--dry-run", action="store_true",
                        help="não usado por enquanto; este script só propõe, não escreve no banco")
    args = parser.parse_args()

    aulas = carregar_aulas()
    banco = carregar_banco()
    print(f"[i] {len(aulas)} aulas carregadas (UC01+UC02)")
    print(f"[i] {len(banco['questoes'])} questões no banco")

    prop = classificar(banco, aulas, reclassificar_tudo=args.all)

    OUT_JSON.write_text(
        json.dumps(prop, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    OUT_MD.write_text(gerar_md(prop, aulas), encoding="utf-8")

    print(f"[ok] proposta: {OUT_JSON.relative_to(ROOT)}")
    print(f"[ok] revisão:  {OUT_MD.relative_to(ROOT)}")
    print(f"[stats] {prop['estatisticas']}")


if __name__ == "__main__":
    main()
