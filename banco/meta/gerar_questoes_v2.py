"""
Gera q-NNNN.md para os itens ausentes do banco.
Gaps alvo:
  - q-0106 a q-0111  (JSON indices 105-110)
  - q-0171 a q-0211  (JSON indices 170-210)
  - q-0360 a q-0417  (JSON indices 359-416)
"""
import json, os
from pathlib import Path

BASE = Path(r"C:\AI use\Cowork playground\NEBLI - criador de resumos")
JSON_PATH = BASE / "banco/meta/EXCEL_UNICOS.json"
QUESTOES_DIR = BASE / "banco/questoes"
TODAY = "2026-05-13"

# ──────────────────────────────────────────────────────────────────────────────
# Mapeamento tema → tags (keyword em lowercase → lista de tags do banco)
# Primeiro match vence.
# ──────────────────────────────────────────────────────────────────────────────
TEMA_TAGS = [
    # Bioquímica — saldo ATP / beta-oxidação
    ("saldo de atp da beta", ["beta-oxidacao","fosforilacao-oxidativa","metabolismo-integrado"]),
    ("beta-oxidacao",        ["beta-oxidacao","metabolismo-integrado","acetil-coa","cofatores-enzimaticos"]),
    ("saldo de atp",         ["fosforilacao-oxidativa","cadeia-respiratoria","metabolismo-integrado"]),
    # Bioquímica — cadeia respiratória / fosforilação oxidativa
    ("especies reativas de oxigenio", ["cadeia-respiratoria","fosforilacao-oxidativa","desacoplador"]),
    ("ros e cadeia",                   ["cadeia-respiratoria","fosforilacao-oxidativa"]),
    ("inibidores da cadeia respiratoria", ["cadeia-respiratoria","inibidores-enzimaticos","fosforilacao-oxidativa"]),
    ("lancadeiras mitocondriais",      ["fosforilacao-oxidativa","cadeia-respiratoria","metabolismo-integrado"]),
    ("desacoplamento",                 ["desacoplador","fosforilacao-oxidativa","cadeia-respiratoria"]),
    ("fosforilacao oxidativa",         ["fosforilacao-oxidativa","cadeia-respiratoria","metabolismo-integrado"]),
    # Bioquímica — Krebs
    ("ciclo de krebs",                 ["krebs","fosforilacao-oxidativa","cofatores-enzimaticos","acetil-coa"]),
    ("krebs",                          ["krebs","acetil-coa","metabolismo-integrado"]),
    ("cadeia respiratoria",            ["cadeia-respiratoria","fosforilacao-oxidativa"]),
    # Bioquímica — glicólise / gliconeogênese
    ("regulacao por frutose-2,6",      ["f26bp","glicolise","gliconeogenese","regulacao-metabolica"]),
    ("regulacao glicolise e gliconeogenese", ["glicolise","gliconeogenese","regulacao-metabolica","f26bp","inibidores-enzimaticos"]),
    ("regulacao hormonal da sintese",  ["regulacao-metabolica","lipogenese","beta-oxidacao"]),
    ("gliconeogenese a partir de lactato", ["gliconeogenese","ciclo-cori","regulacao-metabolica"]),
    ("gliconeogenese a partir de piruvato", ["gliconeogenese","regulacao-metabolica","acetil-coa"]),
    ("gliconeogenese a partir do glicerol", ["gliconeogenese","regulacao-metabolica"]),
    ("gliconeogenese e equivalentes",  ["gliconeogenese","regulacao-metabolica","nadph"]),
    ("substratos da gliconeogenese",   ["gliconeogenese","metabolismo-integrado","regulacao-metabolica"]),
    ("gliconeogenese e marcacao",      ["gliconeogenese","regulacao-metabolica"]),
    ("nadh e gliconeogenese",          ["gliconeogenese","regulacao-metabolica","cofatores-enzimaticos"]),
    ("gliconeogenese e saldo",         ["gliconeogenese","fosforilacao-oxidativa","metabolismo-integrado"]),
    ("gliconeogenese",                 ["gliconeogenese","regulacao-metabolica","enzimologia"]),
    ("glicolise",                      ["glicolise","regulacao-metabolica","enzimologia","f26bp"]),
    ("processamento de rnam em eucariontes", ["processamento-mrna","splicing","cap5","poliadenilacao"]),
    # Biologia molecular / Biomol
    ("diferencas entre dna e rna",     ["transcricao","dna-recombinante"]),
    ("replicacao do dna",              ["reparo-dna","dna-recombinante","ciclo-celular"]),
    ("transcricao e rna polimerase",   ["transcricao","rna-polimerase"]),
    ("transcricao",                    ["transcricao","rna-polimerase","regulacao-genica"]),
    ("regulacao do operon lac",        ["operon-lac","regulacao-genica"]),
    ("operon lac",                     ["operon-lac","regulacao-genica"]),
    ("operon trp",                     ["operon-trp","regulacao-genica"]),
    ("processamento de rna em eucariotos", ["processamento-mrna","splicing","cap5","poliadenilacao"]),
    ("processamento de rna",           ["processamento-mrna","splicing"]),
    ("splicing",                       ["splicing","processamento-mrna"]),
    ("traducao e aminoacil-trna",      ["traducao","aminoacil-trna","ribossomo"]),
    ("traducao",                       ["traducao","aminoacil-trna","ribossomo"]),
    ("epigenetica",                    ["epigenetica","cromatina","histonas"]),
    ("cromatina",                      ["cromatina","nucleossomo","histonas"]),
    ("dna recombinante",               ["dna-recombinante"]),
    ("reparo de dna",                  ["reparo-dna","mutacao"]),
    # Fisiologia — eletrofisiologia
    ("estados do canal de sodio",      ["canais-na-voltagem","inativacao-canal","potencial-acao"]),
    ("inativacao do canal de sodio",   ["inativacao-canal","canais-na-voltagem","periodo-refratario"]),
    ("estrutura molecular de canais kv", ["canais-k-voltagem","sensor-voltagem","canais-ionicos"]),
    ("canais ionicos",                 ["canais-ionicos","permeabilidade-ionica","potencial-membrana-repouso"]),
    ("tudo-ou-nada e variacao",        ["potencial-acao","limiar","frequencia-disparo"]),
    ("potencial de acao",              ["potencial-acao","canais-na-voltagem","inativacao-canal","periodo-refratario"]),
    ("propagacao do potencial de acao",["propagacao-potencial","conducao-saltatoria","bainha-mielina"]),
    ("propagacao em fibra amielinica", ["fibras-amielinicas","propagacao-potencial","conducao-eletrotonica"]),
    ("independencia do pa",            ["potencial-acao","limiar","potencial-membrana-repouso"]),
    ("periodo refratario relativo",    ["periodo-refratario","inativacao-canal","potencial-acao"]),
    ("permeabilidade durante o pa",    ["permeabilidade-ionica","potencial-acao","canais-na-voltagem"]),
    ("plato e canais de calcio",       ["plato","canais-ca-voltagem","acoplamento-excitacao-secrecao"]),
    ("codificacao de frequencia",      ["frequencia-disparo","potencial-acao","receptor-sensorial"]),
    ("soma espacial e limiar",         ["somacao-temporal-espacial","limiar","integracao-sinaptica"]),
    ("somacao espacial e temporal",    ["somacao-temporal-espacial","integracao-sinaptica","peps"]),
    # Fisiologia — sinapses / neurotransmissão
    ("receptor nmda",                  ["sinapse-quimica","neurotransmissor","calcio-intracelular","receptor-nmda"]),
    ("canal nmda",                     ["sinapse-quimica","neurotransmissor","calcio-intracelular","receptor-nmda"]),
    ("receptor muscarinico",           ["gpcr","receptores-colinergicos","neurotransmissor"]),
    ("receptor com atividade tirosina quinase", ["hormonio-peptidico","sinalizacao-celular","fatores-crescimento"]),
    ("mecanismo de antagonismo farmacologico", ["receptores-ionotropicos","receptores-colinergicos","sinapse-quimica"]),
    ("neurotransmissores e receptores ionotropicos", ["neurotransmissor","receptores-ionotropicos","sinapse-quimica"]),
    ("mecanismos de peps",             ["peps","sinapse-quimica","receptores-ionotropicos","integracao-sinaptica"]),
    ("peps",                           ["peps","integracao-sinaptica","sinapse-quimica"]),
    ("mecanismos de potencializacao sinaptica", ["integracao-sinaptica","calcio-intracelular","sinapse-quimica"]),
    ("integracao sinaptica",           ["integracao-sinaptica","somacao-temporal-espacial","sinapse-quimica"]),
    ("celula pos-sinaptica",           ["sinapse-quimica","receptores-ionotropicos","integracao-sinaptica"]),
    ("encerramento da neurotransmissao", ["neurotransmissor","sinapse-quimica","acetilcolina"]),
    ("plasticidade e neurotransmissores", ["neurotransmissor","sinapse-quimica","sinalizacao-celular"]),
    ("toxina botulinica e bloqueio de exocitose", ["exocitose","acetilcolina","sinapse-quimica"]),
    ("juncao neuromuscular e farmacologia colinergica", ["receptores-colinergicos","acetilcolina","sinapse-quimica"]),
    # Fisiologia — sinalização celular
    ("toxina colerica e mecanismo",    ["toxina-colera","gpcr","camp","adenilato-ciclase"]),
    ("sinalizacao intracelular e segundos mensageiros", ["mensageiro-celular","camp","ip3","gpcr"]),
    ("conceito de receptor",           ["gpcr","receptores-ionotropicos","mensageiro-celular"]),
    # Fisiologia — músculo
    ("acoplamento excitacao-contracao muscular esqueletico", ["acoplamento-excitacao-secrecao","calcio-intracelular","reticulo-endoplasmatico"]),
    ("musculo liso",                   ["acoplamento-excitacao-secrecao","calcio-intracelular"]),
    # Fisiologia — compartimentos / transporte
    ("regulacao de volume",            ["volume-celular","tonicidade","osmose"]),
    ("transporte epitelial",           ["transporte-ativo-secundario","cotransporte","transporte-membrana"]),
    ("transporte renal",               ["transporte-ativo-secundario","cotransporte","osmose"]),
    ("osmose",                         ["osmose","tonicidade","volume-celular"]),
    ("homeostase",                     ["compartimentos-corporais","osmose","tonicidade"]),
    ("termorregulacao e febre",        ["mensageiro-celular","gpcr"]),
    # Anatomia
    ("subdivisoes da anatomia",        ["neuroanatomia-divisoes","planos-anatomicos"]),
    ("termos de orientacao",           ["planos-anatomicos"]),
    ("planos e eixos",                 ["planos-anatomicos"]),
    ("tipos de movimento articular",   ["articulacoes","anatomia-musculo"]),
    ("articulacoes sinoviais",         ["articulacoes"]),
    ("articulacoes",                   ["articulacoes"]),
    ("sistema de alavancas",           ["anatomia-musculo","articulacoes"]),
    ("classificacao de ossos",         ["tecido-osseo-anatomia","articulacoes"]),
    ("nutricao ossea",                 ["tecido-osseo-anatomia"]),
    ("insercoes musculares",           ["anatomia-musculo"]),
    ("acao muscular",                  ["anatomia-musculo"]),
    ("cintura escapular",              ["anatomia-musculo","articulacoes"]),
    ("neuroanatomia",                  ["neuroanatomia-divisoes","substancia-cinzenta-branca"]),
    # Histologia
    ("tecido epitelial de revestimento", ["tecido-epitelial"]),
    ("epitelio glandular",             ["tecido-epitelial","exocitose"]),
    ("tecido epitelial",               ["tecido-epitelial"]),
    ("tecido conjuntivo",              ["tecido-conjuntivo","matriz-extracelular"]),
    ("matriz extracelular",            ["matriz-extracelular","tecido-conjuntivo"]),
    ("tecido adiposo",                 ["tecido-adiposo","tecido-conjuntivo"]),
    ("cartilagem hialina vs pericondrio", ["cartilagem","pericondrio"]),
    ("cartilagem hialina",             ["cartilagem"]),
    ("fibrocartilagem",                ["cartilagem"]),
    ("pericondrio",                    ["pericondrio","cartilagem"]),
    ("crescimento e histogenese da cartilagem", ["cartilagem","ossificacao"]),
    ("ossificacao endocondral",        ["ossificacao","cartilagem","tecido-osseo-histo"]),
    ("ossificacao e tipos de tecido osseo", ["tecido-osseo-histo","ossificacao"]),
    ("tecido osseo",                   ["tecido-osseo-histo","celulas-osseas"]),
    ("celulas osseas",                 ["celulas-osseas","tecido-osseo-histo"]),
    ("periosteo e endosteo",           ["tecido-osseo-histo","celulas-osseas"]),
    ("reticulo sarcoplasmatico e tubulos t", ["reticulo-endoplasmatico","acoplamento-excitacao-secrecao","calcio-intracelular"]),
    ("tecido muscular esqueletico",    ["actino-miosina","acoplamento-excitacao-secrecao"]),
    ("musculo cardiaco e juncoes",     ["juncoes-gap","conexinas","actino-miosina"]),
    ("tecidos musculares",             ["actino-miosina","acoplamento-excitacao-secrecao"]),
]

# Tags confirmadas na taxonomia atual
TAGS_OK = {
    "transporte-membrana","difusao-simples","difusao-facilitada","transporte-ativo",
    "transporte-ativo-primario","transporte-ativo-secundario","cotransporte","canais-ionicos",
    "canais-vazamento","endocitose","coeficiente-particao","lipossolubilidade",
    "permeabilidade-ionica","potencial-eletroquimico","energia-livre",
    "bomba-na-k","atpase-e1e2","fosforilacao","gradientes-ionicos","ouabaina",
    "intoxicacao-digitalica","gradiente-ionico",
    "gpcr","proteina-g","ribosilacao","toxina-colera","toxina-pertussis",
    "camp","pka","fosfolipase-c","ip3","adenilato-ciclase","fosfodiesterase",
    "mensageiro-celular","sinapse-metabotropica",
    "potencial-acao","potencial-membrana-repouso","equacao-goldman",
    "canais-na-voltagem","canais-k-voltagem","canais-ca-voltagem","canais-sensiveis-tensao",
    "inativacao-canal","periodo-refratario","bainha-mielina","conducao-saltatoria",
    "capacitancia-membrana","axonio","limiar","repolarizacao","anestesicos-locais",
    "plato","cinetica-canal","potencial-equilibrio","potencial-pos-sinaptico",
    "amortecimento-eletronico","conducao-eletrotonica","propagacao-potencial",
    "resistencia-membrana","voltagem-dependencia","seletividade-ionica","sensor-voltagem",
    "densidade-canais-na","densidade-canais","zona-disparo","cone-insercao-axonio",
    "velocidade-transmissao","velocidade-propagacao","frequencia-disparo",
    "despolarizacao-graduada","bloqueio-neural","fibras-amielinicas",
    "sinapse-quimica","sinapses-eletricas","conexinas","juncoes-gap",
    "receptor-sensorial","potencial-gerador","receptor-mecanico","neurotransmissor",
    "acetilcolina","receptores-colinergicos","receptores-ionotropicos","gaba-receptor",
    "cl-permeabilidade","peps","integracao-sinaptica","somacao-temporal-espacial",
    "peso-sinaptico","numero-sinapses","transmissao-rapida","inibicao-pre-sinaptica",
    "sinalizacao-celular","segundos-mensageiros",
    "acoplamento-excitacao-secrecao","exocitose","calcio-intracelular","calcio",
    "reticulo-endoplasmatico","transducao","estimulo-sensorial","adaptacao-sensorial",
    "codificacao-neuronal","quimiorrecepcao","permeabilidade-seletiva","osmolaridade",
    "compartimentos-corporais","osmose","tonicidade","volume-celular","edema",
    "albumina","pressao-oncotica","equilibrio-starling","endotelio",
    "proteinas-membrana","proteinas-extrinsecas","alfa-helice","folha-beta",
    "glicosilacao","citoesqueleto","estrutura-proteina","aminoacidos-propriedades",
    "polaridade","hidrofobicidade","ligacoes-hidrogeno","dendritos","soma",
    "nervo-misto","conducao","constante-espaco",
    "termodinamica","espontaneidade-reacao","constante-equilibrio","ph",
    "equacao-henderson-hasselbalch","buffers","acidose-metabolica",
    "co2-bicarbonato","hemoglobina","afinidade-oxigenio","modulador-alosterico","efeito-bohr",
    "glut","transporte-glicose","km","sensor-glicose","celulas-beta-pancreaticas",
    "glicolise","gliconeogenese","krebs","fosforilacao-oxidativa","cadeia-respiratoria",
    "desacoplador","via-pentoses","metabolismo-glicogenio","metabolismo-etanol",
    "cetogenese","beta-oxidacao","lipogenese","metabolismo-integrado","regulacao-metabolica",
    "modificacao-covalente","inibidores-enzimaticos","efeito-pasteur","ciclo-cori",
    "enzimologia","doencas-metabolicas","f26bp","nadph","cofatores-enzimaticos","acetil-coa",
    "estrutura-membrana","lipossomos","fosfolipidios","metaloproteina","hormonio-peptidico",
    "transcricao","rna-polimerase","regulacao-genica","operon-lac","operon-trp",
    "splicing","processamento-mrna","cap5","poliadenilacao","traducao",
    "aminoacil-trna","ribossomo","dna-recombinante","reparo-dna","mutacao",
    "fatores-transcricao","epigenetica",
    "ciclo-celular","mitose","ciclinas-cdk","apoptose","oncoproteinas","p53",
    "marcadores-proliferacao","citometria-fluxo","quimioterapia","diferenciacao-celular",
    "celulas-tronco","cromatina","nucleossomo","histonas","eucromatina-heterocromatina",
    "microtubulos","actino-miosina","dineina-axonemal",
    "hematopoiese","granulocitos","leucocitos","fatores-crescimento",
    "anatomia-coracao","valvas-cardiacas","grandes-vasos","sistema-linfatico",
    "neuroanatomia-divisoes","substancia-cinzenta-branca","planos-anatomicos",
}


def get_tags(tema):
    tl = tema.lower()
    matched = []
    for kw, tlist in TEMA_TAGS:
        if kw in tl:
            for t in tlist:
                if t not in matched:
                    matched.append(t)
            break
    if not matched:
        if any(x in tl for x in ("bioquimica","biomol","biologia mol")):
            matched = ["metabolismo-integrado","enzimologia"]
        elif "fisiologia" in tl:
            matched = ["potencial-acao","sinalizacao-celular"]
        elif "anatomia" in tl:
            matched = ["planos-anatomicos"]
        elif "histologia" in tl:
            matched = ["estrutura-membrana"]
        else:
            matched = ["metabolismo-integrado"]
    conf = [t for t in matched if t in TAGS_OK]
    pend = [t for t in matched if t not in TAGS_OK]
    return conf, pend


def nivel_from(item):
    d = item.get("dificuldade","").lower()
    if d == "facil": return "facil"
    if d in ("dificil","muito dificil"): return "dificil"
    if item.get("tipo") == "Discursiva": return "dificil"
    return "medio"


def conceito(item):
    parts = item.get("tema","").split(" - ", 1)
    return parts[1].strip() if len(parts) == 2 else item.get("tema","").strip()


def fix(s):
    if not s: return ‘’
    fixes = [
        (‘â\x80\x94’, ‘—‘),
        (‘â\x80\x99’, ‘’’),
        (‘â\x80\x9c’, ‘“’),
        (‘â\x80\x9d’, ‘”’),
        (‘\xc3\xa9’, ‘\xe9’),
        (‘\xc3\xb3’, ‘\xf3’),
        (‘\xc3\xa7’, ‘\xe7’),
        (‘\xc3\xb5’, ‘\xf5’),
        (‘\xc3\xa3’, ‘\xe3’),
        (‘\xc3\xa0’, ‘\xe0’),
        (‘\xc3\xa1’, ‘\xe1’),
        (‘\xc3\xad’, ‘\xed’),
        (‘\xc3\xba’, ‘\xfa’),
        (‘\xc3\x89’, ‘\xc9’),
        (‘\xc3\x93’, ‘\xd3’),
        (‘plat\xc3\xb4’, ‘plat\xf4’),
        (‘at\xc3\xa9’, ‘at\xe9’),
    ]
    for bad, good in fixes:
        s = s.replace(bad, good)
    return s


def armadilha(item):
    t = item.get("tema","").lower()
    if "beta-oxidacao" in t and "saldo" in t:
        return "Esquecer de subtrair o custo de ativação do ácido graxo (−2 ATP equivalentes) no saldo final"
    if "gliconeogenese" in t and "piruvato" in t:
        return "Confundir a via piruvato→OAA→PEP com reação direta; esquecer do custo de GTP da PEPCK"
    if "gliconeogenese" in t and "lactato" in t:
        return "Esquecer que lactato→piruvato consome NAD+ e que o custo total é 6 ATP por glicose sintetizada"
    if "fosforilacao oxidativa" in t or "cadeia respiratoria" in t or "inibidores da cadeia" in t:
        return "Misturar local de ação dos inibidores: antimicina bloqueia Complexo III, oligomicina bloqueia ATP-sintase"
    if "krebs" in t:
        return "Confundir GTP com ATP no Krebs (succinil-CoA sintetase → GTP) e esquecer que PDH não é etapa do Krebs"
    if "regulacao glicolise" in t or "regulacao por frutose" in t:
        return "Confundir efeito alostérico do ATP em [alta] (inibe PFK-1) com seu papel de substrato no sítio ativo"
    if "operon lac" in t:
        return "Confundir o indutor (alolactose, não lactose direta) com o substrato; CAP ativa o operon (não inibe)"
    if "canal nmda" in t or "receptor nmda" in t:
        return "Pensar que o bloqueio por Mg²⁺ é permanente — ele é voltagem-dependente e se desprende com despolarização"
    if "potencial de acao" in t:
        return "Confundir período refratário absoluto (inativação de Na+) com relativo (hiperpolarização por K+)"
    if "toxina botulinica" in t:
        return "Confundir toxina botulínica (bloqueia exocitose de ACh) com toxina tetânica (bloqueia inibição medular)"
    if "toxina colerica" in t:
        return "A toxina colérica ADP-ribosila Gs (não Gi), travando-a em GTP-bound e elevando cAMP permanentemente"
    if "processamento de rna" in t or "processamento de rnam" in t:
        return "Confundir splicing alternativo (múltiplas isoformas) com edição de RNA (alteração de nucleotídeos)"
    if "traducao" in t and "aminoacil" in t:
        return "Pensar que o aminoacil-tRNA determina o aminoácido — o anticódon especifica o códon, o AA pode ser trocado pós-carregamento"
    if "ossificacao endocondral" in t:
        return "Confundir endocondral (modelo cartilaginoso→osso) com intramembranosa (osso formado diretamente)"
    if "musculo cardiaco" in t:
        return "Confundir discos intercalados (músculo cardíaco) com tríades (esquelético); Ca²⁺ externo dispara CICR no cardíaco"
    if "reticulo sarcoplasmatico" in t:
        return "No esquelético o Ca²⁺ vem puramente do RS; no cardíaco a entrada extracelular (DHPR) dispara o RS (CICR)"
    if "articulacoes sinoviais" in t or "articulacoes" in t:
        return "Classificar articulações por função (anfiartroses) em vez de estrutura (sinoviais), gerando sobreposição"
    if "celulas osseas" in t or "ossificacao e tipos" in t:
        return "Confundir osteoblasto (síntese) com osteoclasto (reabsorção); osteócito é osteoblasto enredado na matriz"
    if "gliconeogenese" in t:
        return "Esquecer que o músculo não pode exportar glicose (sem glicose-6-fosfatase): gliconeogenese hepática/renal"
    if item.get("tipo") == "CE":
        return "Em questões C/E, avaliar cada assertiva de forma independente — a falsidade de uma não implica as demais"
    if item.get("tipo") == "Discursiva":
        return "Questão discursiva: cada mecanismo deve ser explicitado — conclusão correta sem raciocínio não pontua"
    return "Confundir mecanismo com consequência; analisar todos os distratores antes de responder"


def alts_block(item):
    alts = item.get("alternativas", {})
    lines = []
    for k in ["A","B","C","D","E"]:
        v = alts.get(k,"")
        if v:
            lines.append(f"({k}) {fix(v)}")
    return "\n\n".join(lines)


def gabarito_display(item):
    g = item.get("gabarito_claude","").strip()
    t = item.get("tipo","")
    if t == "MC" and len(g) == 1:
        return g
    if t == "CE":
        return g
    return "Ver Explicação"


def gabarito_yaml(item):
    g = item.get("gabarito_claude","").strip()
    t = item.get("tipo","")
    if t == "MC" and len(g) == 1:
        return g
    if t == "CE":
        # Keep it quoted if has semicolons/spaces
        return f'"{g}"'
    return "Ver Explicação"


def explicacao(item):
    t = item.get("tipo","")
    g = fix(item.get("gabarito_claude",""))
    if t == "Discursiva":
        return g
    if t == "MC" and len(g) > 2:
        return g
    return ""


def make_file(item, q_num):
    conf, pend = get_tags(item.get("tema",""))
    nivel = nivel_from(item)
    tipo = item.get("tipo","MC")
    fmt = "CE" if tipo == "CE" else ("Discursiva" if tipo == "Discursiva" else "MC")
    uc = item.get("uc","SEM-UC")
    cc = conceito(item)
    enun = fix(item.get("enunciado",""))
    ab = alts_block(item)
    gd = gabarito_display(item)
    gy = gabarito_yaml(item)
    arm = armadilha(item)
    exp = explicacao(item)

    tags_str = "[" + ", ".join(conf) + "]" if conf else "[]"

    lines = ["---", f"id: {q_num}", f"tags: {tags_str}"]
    if pend:
        lines.append(f"tags_pendentes_aprovacao: [{', '.join(pend)}]")
    lines += [
        f"nivel: {nivel}",
        f"formato: {fmt}",
        f'conceito_central: "{cc}"',
        f"gabarito: {gy}",
        f"uc_origem: {uc}",
        f'armadilha: "{arm}"',
        f"ingestao_data: {TODAY}",
        "---",
        "",
        "## Enunciado",
        "",
        enun,
    ]
    if ab:
        lines += ["", "## Alternativas", "", ab]
    lines += ["", "## Gabarito", "", gd]
    if exp:
        lines += ["", "## Explicação", "", exp]

    return "\n".join(lines) + "\n"


def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    gaps = list(range(105, 111)) + list(range(170, 211)) + list(range(359, 417))

    created = 0
    skipped = 0
    errors = []

    for idx in gaps:
        q_num = idx + 1
        fpath = QUESTOES_DIR / f"q-{q_num:04d}.md"
        if fpath.exists():
            skipped += 1
            continue
        try:
            content = make_file(data[idx], q_num)
            fpath.write_text(content, encoding="utf-8")
            created += 1
        except Exception as e:
            errors.append(f"idx={idx} q-{q_num:04d}: {e}")
            print(f"  ERRO idx={idx}: {e}")

    print(f"\nCriados: {created} | Ja existiam: {skipped} | Erros: {len(errors)}")
    print(f"Gaps processados: {len(gaps)} | Alvo: nenhum erro, {len(gaps)} arquivos")

    # Verify final count
    all_files = list(QUESTOES_DIR.glob("q-*.md"))
    print(f"Total de arquivos q-*.md no banco: {len(all_files)}")
    assert len(all_files) > 350, f"Esperado >350, encontrado {len(all_files)}"
    print("OK: assert >350 passou.")


if __name__ == "__main__":
    main()
