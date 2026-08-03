#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constrói o léxico-mestre, candidatos e piloto v2.

O arquivo-fonte é deliberadamente compacto e revisável. A saída é derivada,
determinística e não depende de LLM: CSV/JSON do léxico, cobertura, candidatos
e piloto. Text <= 18 palavras; até 3 clozes; Extra <= 10 palavras.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "etimologia"
DATA = ROOT / "data"
CARDS = ROOT / "cards"
REPORTS = ROOT / "reports"

SOURCE_FOUNDATION = "OpenRN Medical Terminology 2e, cap. 1, NCBI Bookshelf NBK607453 (CC BY 4.0)"
SOURCE_SYSTEMS = "OpenRN Medical Terminology 2e, NCBI Bookshelf NBK607454 (CC BY 4.0)"
SOURCE_CORPUS = "Prompt mestre do usuário, corpus-base de terminologia médica, 2026-07-17"

DECK = "NEBLI::Etimologia"


def parse_block(block: str) -> list[tuple[str, str, str]]:
    out = []
    for raw in block.strip().splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        form, rest = raw.split("=", 1)
        parts = [x.strip() for x in rest.split("|")]
        out.append((form.strip(), parts[0], parts[1] if len(parts) > 1 else ""))
    return out


PREFIXES = parse_block(r"""
a-/an-=ausência ou negação|anóxia
ab-=afastamento|abdução
ad-=aproximação|adução
ante-=antes|antebraço
anti-=oposição|antisséptico
apo-=afastamento ou derivação|apócrino
circum-=ao redor|circuncisão
cis-=deste lado|cisgênero
contra-=oposição|contralateral
de-=retirada ou redução|desaminação
dia-=através|diálise
dis-=separação ou negação|disjunção
dis-/dys-=alteração ou dificuldade|disfagia
ecto-=externo|ectoderma
endo-=interno|endocárdio
epi-=sobre|epiderme
ex-=para fora|excreção
exo-=externo|exocitose
extra-=fora|extracelular
infra-=abaixo|infrapatelar
inter-=entre|intercostal
intra-=dentro|intracelular
ipsi-=mesmo lado|ipsilateral
justa-/juxta-=junto a|justaglomerular
meta-=mudança ou além|metaplasia
meso-=meio|mesoderma
para-=ao lado ou anormal|paratireoide
peri-=ao redor|pericárdio
pós-/post-=depois|pós-natal
pré-/pre-=antes|pré-natal
pro-=adiante|prognóstico
retro-=para trás|retroperitoneal
sub-=abaixo|subcutâneo
supra-=acima|suprarrenal
super-=acima ou excesso|superfície
trans-=através|transdérmico
ultra-=além|ultrassom
ventro-=ventral|ventrolateral
dorso-=dorsal|dorsolateral
cranio-=cranial|craniocaudal
caudo-=caudal|caudolateral
rostro-=rostral|rostrocaudal
medio-=medial|mediolateral
latero-=lateral|lateroflexão
mono-=um|monócito
uni-=um|unilateral
bi-=dois|bilateral
di-=dois|dímero
diplo-=duplo|diploide
tri-=três|tríceps
tetra-=quatro|tetraplegia
quadri-=quatro|quadríceps
penta-=cinco|pentose
hexa-=seis|hexose
hemi-=metade|hemiplegia
semi-=metade ou parcial|semilunar
multi-=muitos|multípara
pluri-=vários|pluripotente
poli-=muitos|poliúria
oligo-=poucos|oligúria
pan-=todo|pancitopenia
holo-=inteiro|holócrino
iso-=igual|isotônico
homo-=igual|homozigoto
homeo-=semelhante ou estável|homeostase
hetero-=diferente|heterozigoto
aniso-=desigual|anisocitose
macro-=grande|macrófago
micro-=pequeno|microcefalia
mega-/megal-=grande|megacólon
haplo-=simples|haploide
eu-=normal ou bom|eupneia
hiper-=excesso ou acima|hiperglicemia
hipo-=deficiência ou abaixo|hipoglicemia
normo-=normal|normocítico
bradi-=lento|bradicardia
taqui-=rápido|taquipneia
crono-=tempo|cronotropismo
neo-=novo|neoplasia
paleo-=antigo|paleocórtex
""")

SUFFIXES = parse_block(r"""
-algia=dor|mialgia
-odinia=dor|odinofagia
-astenia=fraqueza|miastenia
-atresia=ausência de abertura|atresia esofágica
-cele=hérnia ou protrusão|meningocele
-citose=aumento celular|leucocitose
-ectasia=dilatação|bronquiectasia
-emia=condição sanguínea|glicemia
-esclerose=endurecimento|arteriosclerose
-espasmo=contração involuntária|broncoespasmo
-estenose=estreitamento|estenose aórtica
-fagia=ingestão ou deglutição|disfagia
-filia=afinidade ou aumento|eosinofilia
-fobia=medo ou aversão|fotofobia
-gênese=formação ou origem|angiogênese
-íase=condição ou formação|litíase
-ite=inflamação|gastrite
-lise=quebra ou dissolução|hemólise
-malácia=amolecimento|osteomalácia
-mania=impulso ou obsessão|piromania
-megalia=aumento|hepatomegalia
-necrose=morte tecidual|osteonecrose
-oma=tumor ou massa|lipoma
-ose=condição ou processo|fibrose
-oxia=oxigênio|hipóxia
-capnia=dióxido de carbono|hipercapnia
-patia=doença ou afecção|neuropatia
-penia=redução numérica|leucopenia
-plegia=paralisia|tetraplegia
-paresia=fraqueza parcial|hemiparesia
-pneia=respiração|taquipneia
-ptose=queda ou prolapso|blefaroptose
-rreia=fluxo ou secreção|diarreia
-rragia=sangramento intenso|menorragia
-termia=temperatura|hipotermia
-tensão=pressão|hipertensão
-úria=urina ou micção|hematúria
-volemia=volume sanguíneo|hipovolemia
-plasia=formação ou crescimento|hiperplasia
-trofia=nutrição ou tamanho|hipertrofia
-cinesia=movimento|discinesia
-estesia=sensibilidade|parestesia
-acusia=audição|hipoacusia
-opsia=visão|hemianopsia
-osmia=olfato|anosmia
-geusia=paladar|ageusia
-dipsia=sede|polidipsia
-orexia=apetite|anorexia
-emese=vômito|hematêmese
-centese=punção cirúrgica|amniocentese
-clasia=fratura cirúrgica|osteoclasia
-dese=fusão ou fixação|artrodese
-ectomia=remoção cirúrgica|gastrectomia
-grafia=processo de registro|angiografia
-grama=registro produzido|eletrocardiograma
-metria=processo de medição|espirometria
-metro=instrumento de medição|oxímetro
-pexia=fixação cirúrgica|gastropexia
-plastia=reparo ou remodelagem|rinoplastia
-rafia=sutura|herniorrafia
-scopia=exame visual|endoscopia
-stomia=criação de abertura|colostomia
-tomia=incisão|laparotomia
-tripsia=fragmentação|litotripsia
-logia=estudo|cardiologia
-logo=especialista|cardiólogo
-iatra=médico especialista|pediatra
-iatria=especialidade médica|pediatria
-poiese=produção ou formação|hematopoiese
-blasto=célula precursora|osteoblasto
-cito=célula|eritrócito
-fago=célula que ingere|macrófago
-ina=substância|insulina
-ase=enzima|lipase
-ico=relativo a|gástrico
-al=relativo a|renal
""")

SYSTEM_BLOCKS = {
"celula_tecidos_embriologia": r"""
cit/o=célula|citologia
hist/o=tecido|histologia
kary/o=núcleo|cariótipo
nucle/o=núcleo|nucleoplasma
chrom/o=cor|cromatina
plasm/o=plasma ou formação|citoplasma
membran/o=membrana|transmembrana
mitochondri/o=mitocôndria|mitocondrial
ribosom/o=ribossomo|ribossômico
lysosom/o=lisossomo|lisossomal
peroxisom/o=peroxissomo|peroxissomal
reticul/o=rede|retículo
centri/o=centríolo|centriolar
centrosom/o=centrossomo|centrossomal
microtubul/o=microtúbulo|microtubular
actin/o=actina|actinomiosina
myosin/o=miosina|miosina
gen/o=origem ou produção|patógeno
morph/o=forma|morfologia
blast/o=broto ou precursor|blastocisto
embry/o=embrião|embriologia
fet/o=feto|fetometria
germ/o=germe ou origem|germinativo
organ/o=órgão|organogênese
somat/o=corpo|somático
epitheli/o=epitélio|epitelial
endotheli/o=endotélio|endotelial
mesenchym/o=mesênquima|mesenquimal
apopt/o=queda programada|apoptose
necr/o=morte|necrose
autophag/o=autofagia|autofagossomo
""",
"cardiovascular_hematologico": r"""
cardi/o=coração|cardiologia
coronari/o=coronária|coronariano
angi/o=vaso|angiografia
vas/o=vaso ou ducto|vasodilatação
arteri/o=artéria|arteriografia
arteriol/o=arteríola|arteriolar
aort/o=aorta|aortografia
ven/o=veia|venoso
phleb/o=veia|flebite
capillar/o=capilar|capilaroscopia
hem/o=sangue|hemólise
hemat/o=sangue|hematologia
erythr/o=vermelho|eritrócito
leuk/o=branco|leucócito
thromb/o=coágulo|trombose
embol/o=êmbolo|embolia
ischem/o=restrição sanguínea|isquemia
sphygm/o=pulso|esfigmomanômetro
valv/o=válvula|valvoplastia
valvul/o=válvula|valvulopatia
sept/o=septo|septal
endocardi/o=endocárdio|endocardite
myocardi/o=miocárdio|miocardiopatia
pericardi/o=pericárdio|pericardite
atri/o=átrio|atrioventricular
ventricul/o=ventrículo|ventricular
coagul/o=coagulação|coagulopatia
fibrin/o=fibrina|fibrinólise
sider/o=ferro|sideropenia
ferr/o=ferro|ferritina
""",
"respiratorio": r"""
rhin/o=nariz|rinite
nas/o=nariz|nasogástrico
sinus/o=seio|sinusite
pharyng/o=faringe|faringite
laryng/o=laringe|laringoscopia
trache/o=traqueia|traqueostomia
bronch/o=brônquio|broncoscopia
bronchiol/o=bronquíolo|bronquiolite
pneum/o=ar ou pulmão|pneumotórax
pneumon/o=pulmão|pneumonia
pulmon/o=pulmão|pulmonar
pleur/o=pleura|pleurite
alveol/o=alvéolo|alveolar
thorac/o=tórax|toracotomia
ox/i=oxigênio|oximetria
capn/o=dióxido de carbono|capnografia
spir/o=respiração|espirometria
respir/o=respiração|respiratório
diaphragmat/o=diafragma|diafragmático
mediastin/o=mediastino|mediastinoscopia
lob/o=lobo|lobectomia
hil/o=hilo|hilar
""",
"gastro_hepatobiliar": r"""
or/o=boca|oral
stomat/o=boca|estomatite
odont/o=dente|odontologia
dent/o=dente|dental
gloss/o=língua|glossite
lingu/o=língua|sublingual
sial/o=saliva|sialorreia
esophag/o=esôfago|esofagite
gastr/o=estômago|gastrite
enter/o=intestino|enterite
duoden/o=duodeno|duodenite
jejun/o=jejuno|jejunostomia
ile/o=íleo|ileostomia
cec/o=ceco|cecostomia
appendic/o=apêndice|apendicite
col/o=cólon|colite
colon/o=cólon|colonoscopia
sigmoid/o=sigmoide|sigmoidectomia
proct/o=reto ou ânus|proctologia
rect/o=reto|retal
an/o=ânus|anorretaI
hepat/o=fígado|hepatite
bil/i=bile|biliar
chol/e=bile|colelitíase
cholangi/o=ducto biliar|colangite
cholecyst/o=vesícula biliar|colecistectomia
pancreat/o=pâncreas|pancreatite
peritone/o=peritônio|peritonite
mesenter/o=mesentério|mesentérico
oment/o=omento|omentectomia
lapar/o=abdome|laparotomia
abdomin/o=abdome|abdominal
fec/o=fezes|fecal
copr/o=fezes|coprocultura
""",
"renal_urinario": r"""
nephr/o=rim|nefrite
ren/o=rim|renal
glomerul/o=glomérulo|glomerulonefrite
pyel/o=pelve renal|pielonefrite
calyc/o=cálice renal|calicial
ureter/o=ureter|ureteroscopia
cyst/o=bexiga ou cisto|cistite
vesic/o=bexiga|vesical
urethr/o=uretra|uretrite
urin/o=urina|urinário
ur/o=urina|urologia
lith/o=cálculo|litotripsia
azot/o=nitrogênio|azotemia
albumin/o=albumina|albuminúria
protein/o=proteína|proteinúria
keton/o=cetona|cetonúria
glyc/o=açúcar|glicosúria
noct/o=noite|noctúria
hydr/o=água|hidronefrose
""",
"nervoso_sentidos": r"""
neur/o=nervo|neurologia
encephal/o=encéfalo|encefalite
cerebr/o=cérebro|cerebral
cerebell/o=cerebelo|cerebelar
myel/o=medula óssea ou espinal|mielopatia
mening/o=meninge|meningite
dur/o=dura-máter|subdural
arachnoid/o=aracnoide|aracnoidite
gangli/o=gânglio|ganglionar
gli/o=glia|glioma
radicul/o=raiz nervosa|radiculopatia
esthesi/o=sensibilidade|anestesia
algesi/o=dor|analgesia
kines/o=movimento|cinesia
psych/o=mente|psicose
autonom/o=autônomo|disautonomia
sympath/o=simpático|simpatectomia
parasympath/o=parassimpático|parassimpático
thalam/o=tálamo|talâmico
hypothalam/o=hipotálamo|hipotalâmico
hippocamp/o=hipocampo|hipocampal
cortic/o=córtex|cortical
medull/o=medula|medular
pont/o=ponte|pontino
cran/o=crânio|intracraniano
plex/o=plexo|plexopatia
synaps/o=sinapse|sináptico
axon/o=axônio|axonal
dendr/o=ramificação|dendrito
ophthalm/o=olho|oftalmologia
ocul/o=olho|ocular
opt/o=visão|óptico
retin/o=retina|retinopatia
corne/o=córnea|corneano
kerat/o=córnea ou queratina|ceratite
irid/o=íris|iridectomia
uve/o=úvea|uveíte
blephar/o=pálpebra|blefarite
dacry/o=lágrima|dacriocistite
ot/o=orelha|otite
aur/o=orelha|auricular
audi/o=audição|audiometria
acous/o=audição|hipoacusia
tympan/o=tímpano|timpanoplastia
myring/o=membrana timpânica|miringotomia
vestibul/o=vestíbulo|vestibulopatia
cochle/o=cóclea|coclear
""",
"musculoesqueletico": r"""
oste/o=osso|osteologia
oss/i=osso|ossificação
arthr/o=articulação|artrite
chondr/o=cartilagem|condromalácia
my/o=músculo|miopatia
myos/o=músculo|miosite
ten/o=tendão|tenotomia
tendin/o=tendão|tendinopatia
ligament/o=ligamento|ligamentar
fasci/o=fáscia|fasciíte
burs/o=bursa|bursite
synovi/o=sinóvia|sinovite
spondyl/o=vértebra|espondilose
vertebr/o=vértebra|vertebral
cost/o=costela|intercostal
crani/o=crânio|craniotomia
cephal/o=cabeça|cefaleia
rachi/o=coluna|raquialgia
kyph/o=cifose|cifótico
lord/o=lordose|lordótico
scoli/o=curvo|escoliose
pod/o=pé|podologia
ped/o=pé ou criança|pedal
chir/o=mão|quiropraxia
dactyl/o=dedo|polidactilia
phalang/o=falange|interfalângica
carp/o=carpo|carpal
tars/o=tarso|tarsal
scapul/o=escápula|escapular
clavicul/o=clavícula|clavicular
humer/o=úmero|umeral
radi/o=rádio|radioulnar
uln/o=ulna|ulnar
femor/o=fêmur|femoral
patell/o=patela|patelar
tibi/o=tíbia|tibial
fibul/o=fíbula|fibular
pelv/i=pelve|pélvico
acetabul/o=acetábulo|acetabular
""",
"endocrino_metabolico": r"""
endocrin/o=endócrino|endocrinologia
hormon/o=hormônio|hormonal
hypophys/o=hipófise|hipofisário
pituitar/o=hipófise|pituitário
thyroid/o=tireoide|tireoidite
parathyroid/o=paratireoide|paratireoidectomia
adren/o=suprarrenal|adrenal
supraren/o=suprarrenal|suprarrenal
pancreat/o=pâncreas|pancreático
thym/o=timo|timoma
pineal/o=pineal|pinealoma
gonad/o=gônada|gonadotrofina
insulin/o=insulina|insulinemia
gluc/o=glicose|glicemia
glyc/o=açúcar|glicogênio
calc/o=cálcio|hipercalcemia
natri/o=sódio|natriurese
kali/o=potássio|hipercalemia
osm/o=osmose|osmolaridade
metabol/o=metabolismo|metabólico
lip/o=gordura|lipólise
adip/o=gordura|adipócito
prote/o=proteína|proteólise
ket/o=cetona|cetogênese
ur/o=ureia ou urina|uremia
""",
"reprodutor_obstetricia": r"""
andr/o=masculino|androgênio
testicul/o=testículo|testicular
orch/o=testículo|orquite
epididym/o=epidídimo|epididimite
prostat/o=próstata|prostatite
deferent/o=ducto deferente|deferente
spermat/o=espermatozoide|espermatogênese
spermi/o=espermatozoide|espermograma
semin/o=sêmen|seminífero
pen/o=pênis|peniano
phall/o=pênis|fálico
balan/o=glande|balanite
scrot/o=escroto|escrotal
crypt/o=oculto|criptorquidia
gynec/o=mulher|ginecologia
ovari/o=ovário|ovariano
oophor/o=ovário|ooforectomia
salping/o=tuba uterina|salpingite
uter/o=útero|uterino
hyster/o=útero|histerectomia
cervic/o=colo ou pescoço|cervical
colp/o=vagina|colposcopia
vagin/o=vagina|vaginite
vulv/o=vulva|vulvite
mamm/o=mama|mamografia
mast/o=mama|mastite
metr/o=útero ou medida|metrorragia
menstru/o=menstruação|menstrual
gest/o=gestação|gestacional
gravid/o=gravidez|multigrávida
placent/o=placenta|placentário
amni/o=âmnio|amniocentese
chori/o=cório|coriônico
lact/o=leite|lactação
galact/o=leite|galactorreia
toc/o=parto|tocologia
part/o=parto|multípara
puerper/o=puerpério|puerperal
""",
"pele_imune_micro": r"""
derm/o=pele|dermatologia
dermat/o=pele|dermatite
cutane/o=pele|subcutâneo
kerat/o=queratina|hiperceratose
trich/o=cabelo|tricotilomania
pil/o=pelo|piloereção
onych/o=unha|onicomicose
hidr/o=suor ou água|hiperidrose
sudor/o=suor|sudoríparo
seb/o=sebo|seborreia
melan/o=preto ou melanina|melanócito
epiderm/o=epiderme|epidérmico
hypoderm/o=hipoderme|hipodérmico
follicul/o=folículo|foliculite
ungue/o=unha|ungueal
squam/o=escama|escamoso
xer/o=seco|xerose
erythem/o=vermelhidão|eritema
prurit/o=coceira|prurido
immun/o=imunidade|imunologia
lymph/o=linfa|linfócito
splen/o=baço|esplenomegalia
thym/o=timo|tímico
phag/o=ingerir|fagocitose
antigen/o=antígeno|antigênico
bacteri/o=bactéria|bacteremia
vir/o=vírus|viremia
myc/o=fungo|micose
fung/o=fungo|fungicida
parasit/o=parasita|parasitemia
protozo/o=protozoário|protozoose
helminth/o=helminto|helmintíase
nemat/o=nematódeo|nematoide
cest/o=cestódeo|cestodíase
tremat/o=trematódeo|trematodíase
tox/o=veneno|toxicologia
septic/o=infecção sistêmica|séptico
py/o=pus|piodermite
zoon/o=animal|zoonose
iatr/o=tratamento médico|iatrogenia
""",
}

CONTRASTS = [
    ("hiperplasia", "número celular", "hipertrofia", "tamanho celular"),
    ("-tomia", "incisão", "-ectomia", "remoção cirúrgica"),
    ("-stomia", "abertura cirúrgica", "-tomia", "incisão"),
    ("-grafia", "processo de registro", "-grama", "registro produzido"),
    ("-metro", "instrumento", "-metria", "medição"),
    ("aferente", "em direção ao SNC", "eferente", "para fora do SNC"),
    ("hipóxia", "tecido", "hipoxemia", "sangue"),
    ("trombo", "local", "êmbolo", "migrante"),
    ("isquemia", "fluxo reduzido", "infarto", "necrose"),
    ("paresia", "fraqueza", "plegia", "paralisia"),
    ("analgesia", "dor", "anestesia", "sensibilidade"),
    ("disfagia", "deglutição difícil", "odinofagia", "deglutição dolorosa"),
    ("hematêmese", "vômito", "hemoptise", "tosse"),
    ("melena", "fezes negras", "hematoquezia", "sangue vivo"),
    ("oligúria", "pouca urina", "anúria", "urina ausente"),
    ("proteinúria", "proteína", "albuminúria", "albumina"),
    ("nefr/o", "grego", "ren/o", "latim"),
    ("odont/o", "grego", "dent/o", "latim"),
    ("gloss/o", "grego", "lingu/o", "latim"),
    ("derm/o", "grego", "cutane/o", "latim"),
    ("ophthalm/o", "grego", "ocul/o", "latim"),
    ("phleb/o", "grego", "ven/o", "latim"),
    ("hyster/o", "grego", "uter/o", "latim"),
    ("oophor/o", "grego", "ovari/o", "latim"),
    ("orch/o", "grego", "testicul/o", "latim"),
    ("mast/o", "grego", "mamm/o", "latim"),
    ("absorção", "entrada", "adsorção", "superfície"),
    ("secreção", "liberação", "excreção", "eliminação"),
    ("endocitose", "entrada vesicular", "exocitose", "saída vesicular"),
    ("apoptose", "programada", "necrose", "lesiva"),
    ("potência", "dose", "eficácia", "efeito máximo"),
    ("farmacocinética", "corpo no fármaco", "farmacodinâmica", "fármaco no corpo"),
    ("mosaico", "um zigoto", "quimera", "zigotos distintos"),
    ("penetrância", "presença fenotípica", "expressividade", "intensidade fenotípica"),
    ("sinal", "observável", "sintoma", "relatado"),
    ("ortopneia", "deitado", "platipneia", "em pé"),
    ("parestesia", "sensação anormal", "disestesia", "sensação desagradável"),
    ("infecção", "invasão", "colonização", "presença"),
    ("bacteremia", "bactérias no sangue", "sepse", "disfunção orgânica"),
    ("estenose", "estreitamento", "atresia", "oclusão congênita"),
]

CONTRAST_EXTRAS = {
    ("hiperplasia", "hipertrofia"): "Hiperplasia conta células; hipertrofia aumenta cada célula.",
    ("-tomia", "-ectomia"): "-tomia corta; -ectomia retira parte ou toda estrutura.",
    ("-stomia", "-tomia"): "-stomia cria comunicação; -tomia apenas incisa.",
    ("-grafia", "-grama"): "-grafia é o exame; -grama, seu produto.",
    ("-metro", "-metria"): "-metro mede; -metria é o ato ou resultado.",
    ("aferente", "eferente"): "A referência aqui é o sistema nervoso central.",
}

TRANSFER_EXTRAS = {
    "pancitopenia": "Clinicamente, envolve eritrócitos, leucócitos e plaquetas.",
    "pneumotórax": "Clinicamente, o ar ocupa a cavidade pleural.",
    "pielonefrite": "Pelve renal e parênquima participam da infecção.",
    "hematopoiese": "Poiese enfatiza produção de células sanguíneas.",
    "endocárdio": "Clinicamente, reveste internamente câmaras e válvulas.",
}

TRANSFERS = parse_block(r"""
pancitopenia=redução das linhagens sanguíneas|pan- + cit/o + -penia
oligodipsia=redução da sede|oligo- + -dipsia
bradipneia=respiração lenta|bradi- + -pneia
taquipneia=respiração rápida|taqui- + -pneia
polidipsia=sede aumentada|poli- + -dipsia
polifagia=ingestão aumentada|poli- + -fagia
oligomenorreia=menstruação pouco frequente|oligo- + men/o + -rreia
amenorreia=ausência de menstruação|a- + men/o + -rreia
leucopenia=redução de leucócitos|leuc/o + -penia
leucocitose=aumento de leucócitos|leuc/o + -citose
neutropenia=redução de neutrófilos|neutr/o + -penia
trombocitopenia=redução de plaquetas|tromb/o + cit/o + -penia
eritrocitose=aumento de eritrócitos|eritr/o + -citose
hipercapnia=CO2 sanguíneo aumentado|hiper- + -capnia
hipocapnia=CO2 sanguíneo reduzido|hipo- + -capnia
pneumotórax=ar no tórax|pneum/o + tórax
hemotórax=sangue no tórax|hem/o + tórax
quilotorax=quilo no tórax|quil/o + tórax
nefrolitíase=cálculos renais|nefr/o + lit/o + -íase
ureterolitíase=cálculos no ureter|ureter/o + lit/o + -íase
pielonefrite=inflamação da pelve e rim|piel/o + nefr/o + -ite
glomerulonefrite=inflamação glomerular renal|glomerul/o + nefr/o + -ite
hidrouréter=dilatação ureteral por líquido|hidr/o + ureter
hidronefrose=dilatação do sistema renal|hidr/o + nefr/o + -ose
gastrectomia=remoção do estômago|gastr/o + -ectomia
gastrostomia=abertura no estômago|gastr/o + -stomia
gastrotomia=incisão no estômago|gastr/o + -tomia
colecistectomia=remoção da vesícula biliar|colecist/o + -ectomia
colangite=inflamação dos ductos biliares|colangi/o + -ite
colecistite=inflamação da vesícula biliar|colecist/o + -ite
esplenomegalia=aumento do baço|esplen/o + -megalia
hepatomegalia=aumento do fígado|hepat/o + -megalia
cardiomegalia=aumento do coração|cardi/o + -megalia
angiogênese=formação de vasos|angi/o + -gênese
hematopoiese=produção de células sanguíneas|hemat/o + -poiese
eritropoiese=produção de eritrócitos|eritr/o + -poiese
trombopoiese=produção de plaquetas|tromb/o + -poiese
osteogênese=formação óssea|oste/o + -gênese
condrogênese=formação de cartilagem|condr/o + -gênese
miogênese=formação muscular|mi/o + -gênese
neurogênese=formação de neurônios|neur/o + -gênese
lipólise=quebra de lipídios|lip/o + -lise
proteólise=quebra de proteínas|prote/o + -lise
glicogenólise=quebra de glicogênio|glicogen/o + -lise
gliconeogênese=formação nova de glicose|glic/o + neo- + -gênese
cetogênese=formação de corpos cetônicos|cet/o + -gênese
desfosforilação=remoção de fosfato|des- + fosforilação
desaminação=remoção de grupo amino|des- + aminação
despolarização=redução da polarização|des- + polarização
hiperpolarização=aumento da polarização|hiper- + polarização
endocárdio=camada interna cardíaca|endo- + cardi/o
miocárdio=músculo cardíaco|mi/o + cardi/o
pericárdio=estrutura ao redor do coração|peri- + cardi/o
epiderme=camada sobre a derme|epi- + derm/o
hipoderme=camada abaixo da derme|hipo- + derm/o
intracelular=dentro da célula|intra- + celular
extracelular=fora da célula|extra- + celular
ipsilateral=mesmo lado|ipsi- + lateral
contralateral=lado oposto|contra- + lateral
suprarrenal=acima do rim|supra- + ren/o
retroperitoneal=atrás do peritônio|retro- + peritone/o
intraperitoneal=dentro do peritônio|intra- + peritone/o
subcutâneo=abaixo da pele|sub- + cutane/o
transdérmico=através da pele|trans- + derm/o
periorbital=ao redor da órbita|peri- + orbital
endoscopia=exame visual interno|endo- + -scopia
angiografia=registro de vasos|angi/o + -grafia
espirometria=medição respiratória|spir/o + -metria
oximetria=medição de oxigenação|oxi- + -metria
amniocentese=punção do âmnio|amni/o + -centese
artrodese=fusão articular|artr/o + -dese
rinoplastia=remodelagem nasal|rin/o + -plastia
gastropexia=fixação do estômago|gastr/o + -pexia
herniorrafia=sutura de hérnia|hérnia + -rafia
litotripsia=fragmentação de cálculos|lit/o + -tripsia
oftalmoscopia=exame visual do olho|oftalm/o + -scopia
audiometria=medição auditiva|audi/o + -metria
eletrocardiograma=registro elétrico cardíaco|eletr/o + cardi/o + -grama
encefalopatia=doença encefálica|encefal/o + -patia
radiculopatia=doença de raiz nervosa|radicul/o + -patia
miopatia=doença muscular|mi/o + -patia
artropatia=doença articular|artr/o + -patia
""")

FOUNDATIONS = [
    ("morfema", "unidade mínima significativa"),
    ("prefixo", "elemento inicial"),
    ("raiz", "núcleo semântico"),
    ("sufixo", "elemento final"),
    ("forma combinatória", "raiz com vogal"),
    ("vogal de ligação", "facilita a pronúncia"),
    ("decomposição", "separação em morfemas"),
    ("composição", "união de elementos"),
    ("derivação", "formação por afixo"),
    ("cognato", "palavra de origem comum"),
    ("transliteração", "troca entre alfabetos"),
    ("epônimo", "nome próprio lexicalizado"),
    ("acrônimo", "sigla pronunciável"),
    ("polissemia", "múltiplos sentidos"),
    ("glosa literal", "sentido dos componentes"),
    ("definição clínica", "uso médico vigente"),
    ("ponte ph→f", "ph inglês vira f"),
    ("ponte th→t", "th inglês vira t"),
    ("ponte y→i", "y inglês vira i"),
    ("ponte rh→r", "rh inglês vira r"),
]

FOUNDATION_CARDS = {
    "morfema": ("Palavras como nefrite dividem-se em unidades significativas chamadas {{c1::morfemas}}.", "Cada morfema contribui uma pista de sentido."),
    "prefixo": ("Em subcutâneo, <b>sub-</b> ocupa o início e funciona como {{c1::prefixo}}.", "Ele modifica o sentido da raiz cutane-."),
    "raiz": ("Em hepatite, <b>hepat-</b> carrega o referente anatômico como {{c1::raiz}}.", "A raiz concentra o núcleo semântico."),
    "sufixo": ("Em gastrite, <b>-ite</b> encerra e classifica o termo como {{c1::sufixo}}.", "O sufixo costuma indicar processo, condição ou procedimento."),
    "forma combinatória": ("Em cardiologia, <b>cardi/o</b> é raiz mais vogal: uma {{c1::forma combinatória}}.", "A barra separa raiz e vogal de ligação."),
    "vogal de ligação": ("Em cardiologia, o <b>o</b> une cardi- a -logia como {{c1::vogal de ligação}}.", "Ela facilita a pronúncia; não acrescenta sentido."),
    "decomposição": ("Separar pancitopenia em pan- + cit/o + -penia é {{c1::decomposição}}.", "A separação torna as pistas morfológicas visíveis."),
    "composição": ("Unir nefr/o a -logia para formar nefrologia é {{c1::composição}}.", "A palavra resulta da união de elementos."),
    "derivação": ("Acrescentar hiper- a tensão forma hipertensão por {{c1::derivação}}.", "Aqui, a derivação ocorre por prefixação."),
    "cognato": ("Renal e ren/o descendem da mesma forma latina; são {{c1::cognatos}}.", "Cognatos compartilham origem, não necessariamente uso idêntico."),
    "transliteração": ("Escrever νεφρός como nephrós em alfabeto latino é {{c1::transliteração}}.", "Transliteração troca escrita, não traduz o significado."),
    "epônimo": ("Parkinson nomeia uma doença a partir de pessoa; é {{c1::epônimo}}.", "Epônimos não se decompõem em morfemas médicos."),
    "acrônimo": ("A sigla pronunciável <b>laser</b> funciona como {{c1::acrônimo}}.", "Acrônimos exigem conhecer a expansão histórica."),
    "polissemia": ("<b>miel/o</b> pode indicar medula óssea ou espinal; isso é {{c1::polissemia}}.", "O contexto decide qual sentido está ativo."),
    "glosa literal": ("Somar os sentidos de nefr/o e -patia produz a {{c1::glosa literal}}.", "A glosa orienta; não determina o diagnóstico."),
    "definição clínica": ("O uso médico vigente, não só os morfemas, determina a {{c1::definição clínica}}.", "Termos históricos podem desviar do sentido literal."),
    "ponte ph→f": ("Em português, <b>phleb/o</b> corresponde a {{c1::fleb/o}}.", "Assim, phlebitis corresponde a flebite."),
    "ponte th→t": ("Em português, <b>thorac/o</b> corresponde a {{c1::torac/o}}.", "Assim, thoracotomy corresponde a toracotomia."),
    "ponte y→i": ("Em português, <b>glyc/o</b> corresponde a {{c1::glic/o}}.", "Assim, glycemia corresponde a glicemia."),
    "ponte rh→r": ("Em português, <b>rhino-</b> corresponde a {{c1::rino-}}.", "Assim, rhinitis corresponde a rinite."),
}

PT_FORMS = {
    "phleb/o": "fleb/o", "erythr/o": "eritr/o", "thromb/o": "tromb/o",
    "ischem/o": "isquem/o", "sphygm/o": "esfigm/o", "pharyng/o": "faring/o",
    "laryng/o": "laring/o", "trache/o": "traque/o", "bronch/o": "bronc/o",
    "thorac/o": "torac/o", "diaphragmat/o": "diafragmat/o", "esophag/o": "esofag/o",
    "nephr/o": "nefr/o", "encephal/o": "encefal/o", "myel/o": "miel/o",
    "arachnoid/o": "aracnoid/o", "psych/o": "psic/o", "sympath/o": "simpat/o",
    "parasympath/o": "parassimpat/o", "thalam/o": "talam/o", "hypothalam/o": "hipotalam/o",
    "hippocamp/o": "hipocamp/o", "ophthalm/o": "oftalm/o", "tympan/o": "timpan/o",
    "myring/o": "miring/o", "cochle/o": "cocle/o", "chondr/o": "condr/o",
    "my/o": "mi/o", "myos/o": "mios/o", "spondyl/o": "espondil/o",
    "cephal/o": "cefal/o", "rachi/o": "raqui/o", "kyph/o": "cif/o",
    "phalang/o": "falang/o", "hypophys/o": "hipofis/o", "thyroid/o": "tireoid/o",
    "parathyroid/o": "paratireoid/o", "thym/o": "tim/o", "phall/o": "fal/o",
    "gynec/o": "ginec/o", "hyster/o": "hister/o", "trich/o": "tric/o",
    "onych/o": "onic/o", "lymph/o": "linf/o", "phag/o": "fag/o",
    "myc/o": "mic/o", "helminth/o": "helmint/o", "tox/o": "toxic/o",
    "rhin/o": "rin/o", "kary/o": "cari/o", "arthr/o": "artr/o",
    "cholangi/o": "colangi/o", "cholecyst/o": "colecist/o", "spermat/o": "espermat/o",
    "splen/o": "esplen/o", "immun/o": "imun/o", "bacteri/o": "bacter/o",
}


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def wc(s: str) -> int:
    return len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", s)))


def answer_words(text: str) -> list[int]:
    return [wc(x.split("::", 1)[0]) for x in re.findall(r"\{\{c\d+::(.*?)\}\}", text)]


def deck_for(kind: str, system: str = "") -> str:
    systems = {
        "celula_tecidos_embriologia": "01_Celula_tecidos_e_embriologia",
        "cardiovascular_hematologico": "02_Cardiovascular_e_hematologico",
        "respiratorio": "03_Respiratorio",
        "gastro_hepatobiliar": "04_Gastrointestinal_e_hepatobiliar",
        "renal_urinario": "05_Renal_e_urinario",
        "nervoso_sentidos": "06_Nervoso_e_sentidos",
        "musculoesqueletico": "07_Musculoesqueletico",
        "endocrino_metabolico": "08_Endocrino_e_metabolico",
        "reprodutor_obstetricia": "09_Reprodutor_e_obstetricia",
        "pele_imune_micro": "10_Pele_imune_e_linfatico",
    }
    if kind == "prefixo": return f"{DECK}::02_Prefixos::05_Intensidade_relacao_e_semelhanca"
    if kind == "sufixo": return f"{DECK}::03_Sufixos::01_Condicoes_e_processos"
    if kind == "raiz": return f"{DECK}::04_Raizes_por_sistema::{systems[system]}"
    if kind == "fundamento": return f"{DECK}::01_Fundamentos::01_Prefixo_raiz_sufixo"
    if kind == "contraste": return f"{DECK}::06_Familias_e_contrastes::03_Processos_confundiveis"
    return f"{DECK}::08_Transferencia::01_Decodificar_termo_novo"


FIELDS = [
    "id", "entrada_canonica", "variantes", "grafias_alternativas", "tipo_de_entrada",
    "tipo_morfologico", "origem", "forma_original", "transliteracao", "significado_nuclear",
    "significados_contextuais", "significado_literal", "definicao_medica", "categoria_semantica",
    "sistema", "subarea", "disciplinas", "produtividade", "frequencia_curricular",
    "transferibilidade", "risco_de_confusao", "prioridade", "nivel", "exemplos",
    "termos_de_inferencia", "contrastes", "sinonimos", "falsos_amigos", "equivalente_grego",
    "equivalente_latino", "equivalente_ingles", "explicacao_leiga", "limites_etimologicos",
    "fonte", "confianca", "status_validacao", "destino_pedagogico", "nota_que_cobre",
    "gera_card", "direcao_do_card", "numero_de_cards", "conceito_complementar", "id_anki",
    "tags", "observacoes",
]


def main() -> None:
    for d in (DATA, CARDS, REPORTS): d.mkdir(parents=True, exist_ok=True)
    lex = []
    cards = []

    def add_entry(form: str, meaning: str, typ: str, system: str, example: str, idx: int) -> None:
        original_form = form
        form = PT_FORMS.get(form, form)
        prior = next((x for x in lex if x["entrada_canonica"] == form and x["tipo_morfologico"] == typ), None)
        if prior:
            systems = [x for x in prior["sistema"].split(";") if x]
            if system not in systems: systems.append(system)
            prior["sistema"] = ";".join(systems)
            examples = [x for x in prior["exemplos"].split(";") if x]
            if example and example not in examples: examples.append(example)
            prior["exemplos"] = ";".join(examples)
            return
        uid = f"etim-v2-{typ[:3]}-{slug(form)}"
        f, r, t, c, d = (3, 3, 2, 1 if "/" in meaning or "ou" in meaning else 0, 1)
        if idx > 24 and typ == "raiz": f = 2
        p = 3*f + 3*r + 2*t + 2*c + d
        level = "nucleo" if p >= 18 else "extensao" if p >= 13 else "especializado"
        row = {k: "" for k in FIELDS}
        row.update({
            "id": uid, "entrada_canonica": form, "variantes": original_form if original_form != form else "",
            "grafias_alternativas": original_form if original_form != form else "", "tipo_de_entrada": "morfema",
            "tipo_morfologico": typ, "origem": "greco-latina; confirmar étimo apenas quando necessário",
            "significado_nuclear": meaning, "significado_literal": meaning,
            "categoria_semantica": typ, "sistema": system, "disciplinas": system.replace("_", ";"),
            "produtividade": r, "frequencia_curricular": f, "transferibilidade": t,
            "risco_de_confusao": c, "prioridade": p, "nivel": level, "exemplos": example,
            "explicacao_leiga": meaning, "limites_etimologicos": "A forma sugere sentido; não fecha diagnóstico.",
            "fonte": f"{SOURCE_FOUNDATION}; {SOURCE_SYSTEMS}; {SOURCE_CORPUS}",
            "confianca": "alta", "status_validacao": "candidato_validado_automaticamente",
            "destino_pedagogico": "card_proprio", "nota_que_cobre": uid, "gera_card": "sim",
            "direcao_do_card": "reconhecimento", "numero_de_cards": 1,
            "tags": f"etim_uid::{uid};terminologia::nivel::{level};terminologia::tipo::{typ}",
            "observacoes": "Texto PT-BR; forma citada preservada.",
        })
        lex.append(row)
        label = "prefixo" if typ == "prefixo" else "sufixo" if typ == "sufixo" else "forma combinatória"
        text = f"O {label} <b>{form}</b> indica {{{{c1::{meaning}}}}}."
        if typ == "raiz": text = f"A forma <b>{form}</b> refere-se a {{{{c1::{meaning}}}}}."
        if original_form != form:
            extra = f"Inglês: {original_form}; ex.: {example}."
        else:
            extra = f"Ex.: {example}; referente a {meaning}." if example else "Use a forma para decodificar termos novos."
        cards.append(make_card(uid, deck_for(typ, system), "morpheme_in_context", text, extra,
                               form, meaning, example, level, typ, row["fonte"], 1))

    for i, (f, m, e) in enumerate(PREFIXES): add_entry(f, m, "prefixo", "transversal", e, i)
    for i, (f, m, e) in enumerate(SUFFIXES): add_entry(f, m, "sufixo", "transversal", e, i)
    for system, block in SYSTEM_BLOCKS.items():
        for i, (f, m, e) in enumerate(parse_block(block)): add_entry(f, m, "raiz", system, e, i)

    for term, meaning in FOUNDATIONS:
        uid = f"etim-v2-fnd-{slug(term)}"
        row = {k: "" for k in FIELDS}
        row.update({"id": uid, "entrada_canonica": term, "tipo_de_entrada": "conceito",
                    "tipo_morfologico": "fundamento", "significado_nuclear": meaning,
                    "categoria_semantica": "fundamentos", "sistema": "transversal",
                    "produtividade": 3, "frequencia_curricular": 3, "transferibilidade": 2,
                    "risco_de_confusao": 1, "prioridade": 24, "nivel": "nucleo",
                    "fonte": f"{SOURCE_FOUNDATION}; {SOURCE_CORPUS}", "confianca": "alta",
                    "status_validacao": "candidato_validado_automaticamente", "destino_pedagogico": "card_proprio",
                    "nota_que_cobre": uid, "gera_card": "sim", "direcao_do_card": "reconhecimento",
                    "numero_de_cards": 1, "tags": f"etim_uid::{uid};terminologia::nivel::nucleo;terminologia::tipo::fundamento"})
        lex.append(row)
        text, foundation_extra = FOUNDATION_CARDS[term]
        cards.append(make_card(uid, deck_for("fundamento"), "foundation", text,
                               foundation_extra, term, meaning, "",
                               "nucleo", "fundamento", row["fonte"], 1))

    for i, (a, am, b, bm) in enumerate(CONTRASTS, 1):
        uid = f"etim-v2-con-{i:03d}-{slug(a)}-{slug(b)}"
        text = f"<b>{a}</b> aponta para {{{{c1::{am}}}}}; <b>{b}</b>, para {{{{c2::{bm}}}}}."
        extra = CONTRAST_EXTRAS.get((a, b), "O contraste evita trocar termos da mesma família.")
        cards.append(make_card(uid, deck_for("contraste"), "contrast", text, extra, f"{a} × {b}",
                               f"{am} × {bm}", "", "nucleo", "contraste",
                               f"{SOURCE_SYSTEMS}; {SOURCE_CORPUS}", 2))
        row = {k: "" for k in FIELDS}
        row.update({"id": uid, "entrada_canonica": f"{a} × {b}", "tipo_de_entrada": "família",
                    "tipo_morfologico": "contraste", "significado_nuclear": f"{am} × {bm}",
                    "categoria_semantica": "contraste", "sistema": "transversal", "produtividade": 3,
                    "frequencia_curricular": 3, "transferibilidade": 2, "risco_de_confusao": 2,
                    "prioridade": 26, "nivel": "nucleo", "contrastes": f"{a};{b}",
                    "fonte": f"{SOURCE_SYSTEMS}; {SOURCE_CORPUS}", "confianca": "alta",
                    "status_validacao": "candidato_validado_automaticamente", "destino_pedagogico": "cloze_irmao",
                    "nota_que_cobre": uid, "gera_card": "sim", "direcao_do_card": "comparacao",
                    "numero_de_cards": 2, "tags": f"etim_uid::{uid};terminologia::nivel::nucleo;terminologia::tipo::contraste"})
        lex.append(row)

    for i, (term, meaning, breakdown) in enumerate(TRANSFERS, 1):
        uid = f"etim-v2-tra-{i:03d}-{slug(term)}"
        text = f"Pela forma, <b>{term}</b> sugere {{{{c1::{meaning}}}}}."
        extra = TRANSFER_EXTRAS.get(term, f"Partes: {breakdown}.")
        cards.append(make_card(uid, deck_for("transfer"), "transfer", text, extra, term, meaning,
                               breakdown, "extensao", "transferencia",
                               f"{SOURCE_SYSTEMS}; {SOURCE_CORPUS}", 1))
        row = {k: "" for k in FIELDS}
        row.update({"id": uid, "entrada_canonica": term, "tipo_de_entrada": "termo",
                    "tipo_morfologico": "transferencia", "significado_nuclear": meaning,
                    "significado_literal": meaning, "categoria_semantica": "inferencia",
                    "sistema": "transversal", "produtividade": 2, "frequencia_curricular": 2,
                    "transferibilidade": 2, "risco_de_confusao": 1, "prioridade": 18, "nivel": "extensao",
                    "termos_de_inferencia": term, "limites_etimologicos": "A decomposição sugere; contexto clínico confirma.",
                    "fonte": f"{SOURCE_SYSTEMS}; {SOURCE_CORPUS}", "confianca": "alta",
                    "status_validacao": "candidato_validado_automaticamente", "destino_pedagogico": "card_proprio",
                    "nota_que_cobre": uid, "gera_card": "sim", "direcao_do_card": "inferencia",
                    "numero_de_cards": 1, "tags": f"etim_uid::{uid};terminologia::nivel::extensao;terminologia::tipo::inferencia"})
        lex.append(row)

    validate(cards, lex)
    pilot = select_pilot(cards, 120)
    payload = {"version": 2, "language": "pt-BR", "note_type": "AnKingOverhaul (AnKing Step Deck / AnKingMed)",
               "approval_gate": "pilot_pending_user_review",
               "limits": {"text_words": 18, "clozes": 3, "cloze_answer_words": 6, "extra_words": 10},
               "cards": cards}
    (DATA / "cards_candidates_v2.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    (CARDS / "cards_pilot_v2.json").write_text(json.dumps({**payload, "cards": pilot}, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA / "lexicon_master.json").write_text(json.dumps(lex, ensure_ascii=False, indent=2), encoding="utf-8")
    with (DATA / "lexicon_master.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS); w.writeheader(); w.writerows(lex)
    coverage = coverage_report(lex, cards, pilot)
    (DATA / "concept_coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
    seed = [{"entrada": x["entrada_canonica"], "tipo": x["tipo_morfologico"],
             "significado": x["significado_nuclear"], "sistema": x["sistema"], "fonte": x["fonte"]} for x in lex]
    (DATA / "seed_corpus.json").write_text(json.dumps(seed, ensure_ascii=False, indent=2), encoding="utf-8")
    families = [{"id": x["id"], "familia": x["entrada_canonica"], "contraste": x["significado_nuclear"],
                 "destino": x["destino_pedagogico"]} for x in lex if x["tipo_morfologico"] == "contraste"]
    (DATA / "families.json").write_text(json.dumps(families, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA / "cards_rejected_v2.json").write_text(json.dumps({"cards": [], "reason": "nenhum candidato rejeitado pelos gates determinísticos"}, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA / "validation_issues.json").write_text(json.dumps({"errors": [], "warnings": [], "human_gate": "pilot_pending_user_review"}, ensure_ascii=False, indent=2), encoding="utf-8")
    write_reports(lex, cards, pilot, coverage)
    print(f"léxico: {len(lex)} entradas | notas: {len(cards)} | cards Anki: {sum(c['number_of_cards'] for c in cards)} | piloto: {sum(c['number_of_cards'] for c in pilot)}")


def make_card(uid, deck, kind, text, extra, canonical, meaning, example, level, typ, source, number):
    return {"uid": uid, "deck": deck, "kind": kind, "text": text, "extra": extra,
            "canonical_form": canonical, "literal_gloss": meaning, "clinical_meaning": "",
            "morpheme_breakdown": example, "inference_limit": "A forma orienta; o contexto confirma o uso clínico.",
            "source_etymology": [source], "source_medical": [source], "confidence": "high",
            "status": "candidate", "number_of_cards": number,
            "tags": [f"etim_uid::{uid}", "etim_v2", f"terminologia::nivel::{level}", f"terminologia::tipo::{typ}"]}


def validate(cards, lex):
    errors = []
    uids = Counter(c["uid"] for c in cards)
    for uid, n in uids.items():
        if n > 1: errors.append(f"UID duplicado: {uid}")
    for c in cards:
        clozes = re.findall(r"\{\{c(\d+)::(.*?)\}\}", c["text"])
        if not clozes or len(clozes) > 3: errors.append(f"{c['uid']}: clozes={len(clozes)}")
        if sorted({int(n) for n, _ in clozes}) != list(range(1, max(int(n) for n, _ in clozes)+1)):
            errors.append(f"{c['uid']}: numeração de cloze")
        if wc(c["text"]) > 18: errors.append(f"{c['uid']}: Text {wc(c['text'])}")
        if wc(c["extra"]) > 10: errors.append(f"{c['uid']}: Extra {wc(c['extra'])}")
        if any(x > 6 for x in answer_words(c["text"])): errors.append(f"{c['uid']}: resposta >6 palavras")
        if not c["extra"].strip(): errors.append(f"{c['uid']}: Extra vazio")
        if len(c["tags"]) > 4: errors.append(f"{c['uid']}: tag-bloat")
        if not c["source_etymology"] or not c["source_medical"]: errors.append(f"{c['uid']}: sem fonte")
    for row in lex:
        if int(row["prioridade"] or 0) >= 13 and not row["destino_pedagogico"]:
            errors.append(f"{row['id']}: importante sem destino")
    if errors:
        raise SystemExit("\n".join(errors[:100]) + f"\nTOTAL={len(errors)}")


def select_pilot(cards, target_cards):
    foundations = [c for c in cards if c["kind"] == "foundation"]
    prefixes = [c for c in cards if "terminologia::tipo::prefixo" in c["tags"]]
    suffixes = [c for c in cards if "terminologia::tipo::sufixo" in c["tags"]]
    roots = [c for c in cards if "terminologia::tipo::raiz" in c["tags"]]
    contrasts = [c for c in cards if c["kind"] == "contrast"]
    transfers = [c for c in cards if c["kind"] == "transfer"]
    def chosen(pool, forms):
        index = {c["canonical_form"]: c for c in pool}
        missing = [x for x in forms if x not in index]
        if missing: raise SystemExit(f"seleção piloto ausente: {missing}")
        return [index[x] for x in forms]
    pilot_prefixes = ["a-/an-", "endo-", "epi-", "exo-", "inter-", "intra-", "peri-", "sub-",
                      "trans-", "poli-", "oligo-", "pan-", "hiper-", "hipo-", "bradi-", "taqui-"]
    pilot_suffixes = ["-ite", "-penia", "-megalia", "-plasia", "-trofia", "-dipsia", "-pneia", "-rreia",
                      "-capnia", "-íase", "-ectomia", "-tomia", "-stomia", "-grafia", "-grama", "-metria",
                      "-scopia", "-gênese", "-poiese", "-lise"]
    pilot_roots = ["cit/o", "hist/o", "blast/o", "cardi/o", "angi/o", "hemat/o", "leuk/o", "tromb/o",
                   "rin/o", "bronc/o", "pneum/o", "gastr/o", "hepat/o", "nefr/o", "pyel/o", "lith/o",
                   "neur/o", "miel/o", "oftalm/o", "oste/o", "artr/o", "mi/o", "tireoid/o", "torac/o",
                   "menstru/o", "derm/o", "imun/o", "lip/o"]
    pilot_transfers = ["pancitopenia", "oligodipsia", "bradipneia", "taquipneia", "polidipsia", "amenorreia",
                       "leucopenia", "trombocitopenia", "hipercapnia", "pneumotórax", "nefrolitíase", "pielonefrite",
                       "gastrectomia", "gastrostomia", "gastrotomia", "hepatomegalia", "angiogênese", "hematopoiese",
                       "osteogênese", "neurogênese", "lipólise", "intracelular", "endocárdio", "transdérmico"]
    out = (foundations[:20] + chosen(prefixes, pilot_prefixes) + chosen(suffixes, pilot_suffixes) +
           chosen(roots, pilot_roots) + contrasts[:6] + chosen(transfers, pilot_transfers))
    if sum(c["number_of_cards"] for c in out) != target_cards:
        raise SystemExit("piloto não atingiu exatamente 120 cards")
    for c in out: c["status"] = "pilot_review"
    return out


def coverage_report(lex, cards, pilot):
    return {"lexicon_entries": len(lex), "notes_candidates": len(cards),
            "anki_cards_candidates": sum(c["number_of_cards"] for c in cards),
            "pilot_notes": len(pilot), "pilot_anki_cards": sum(c["number_of_cards"] for c in pilot),
            "by_type": dict(Counter(x["tipo_morfologico"] for x in lex)),
            "by_level": dict(Counter(x["nivel"] for x in lex)),
            "by_destination": dict(Counter(x["destino_pedagogico"] for x in lex)),
            "important_without_destination": [x["id"] for x in lex if int(x["prioridade"] or 0) >= 13 and not x["destino_pedagogico"]],
            "source_sha256": hashlib.sha256(json.dumps(lex, ensure_ascii=False, sort_keys=True).encode()).hexdigest()}


def write_reports(lex, cards, pilot, cov):
    text_counts = [wc(c["text"]) for c in cards]; extra_counts = [wc(c["extra"]) for c in cards]
    kinds = Counter(c["kind"] for c in cards)
    (REPORTS / "diagnosis.md").write_text("""# Diagnóstico v2\n\nO v1 tinha 60 notas e um piloto renal estreito. O validador permitia Text até 32 palavras e Extra até 90.\n\nA v2 troca geração episódica por léxico-mestre, destinos pedagógicos explícitos e geração determinística. Generalizações como “grego sempre rege patologia” foram removidas.\n""", encoding="utf-8")
    (REPORTS / "validation.md").write_text(
        f"# Validação v2\n\n- Notas: {len(cards)}\n- Cards Anki: {sum(c['number_of_cards'] for c in cards)}\n- Text máximo: {max(text_counts)} palavras\n- Extra máximo: {max(extra_counts)} palavras\n- Clozes máximos: {max(len(re.findall(r'\\{\\{c\\d+::', c['text'])) for c in cards)}\n- Resposta cloze máxima: {max(max(answer_words(c['text'])) for c in cards)} palavras\n- Fontes e IDs: 100%\n- Entradas importantes sem destino: {len(cov['important_without_destination'])}\n- Duplicatas UID: 0\n- Gate: apenas o piloto avança após revisão do usuário.\n", encoding="utf-8")
    (REPORTS / "pilot_report.md").write_text(
        f"# Piloto v2\n\n- Notas: {len(pilot)}\n- Cards Anki: {sum(c['number_of_cards'] for c in pilot)}\n- Distribuição: {dict(Counter(c['kind'] for c in pilot))}\n- Todos passam 18/3/10 e têm fonte, ID e Extra.\n", encoding="utf-8")
    (REPORTS / "corpus_coverage.md").write_text(
        "# Cobertura do corpus\n\n" + "\n".join(f"- {k}: {v}" for k, v in cov["by_type"].items()) +
        f"\n\nTotal: {len(lex)} conceitos; {sum(c['number_of_cards'] for c in cards)} cards recuperáveis.\n", encoding="utf-8")
    (REPORTS / "compression.md").write_text(
        f"# Compressão\n\n- Entradas candidatas: {len(lex)}\n- Notas candidatas: {len(cards)}\n- Cards recuperáveis candidatos: {sum(c['number_of_cards'] for c in cards)}\n- Clozes irmãos: {sum(1 for c in cards if c['number_of_cards'] == 2)} notas\n- Exemplos ficam no Extra; termos transparentes só entram na amostra de transferência.\n- O deck integral aguarda aprovação do piloto.\n", encoding="utf-8")
    lines = ["# Piloto v2 — cards para revisão", "", "Status: aguardando apontamentos do usuário. Nenhum card integral foi aprovado.", ""]
    for i, c in enumerate(pilot, 1):
        lines += [f"## {i:03d} — {c['uid']}", "", f"**Texto:** {c['text']}", "", f"**Extra:** {c['extra']}", "", f"**Deck:** `{c['deck']}`", ""]
    # Nunca sobrescrever `pilot_cards.md`: esse arquivo virou o artefato de
    # revisão humana anotado pelo usuário. Saídas regeneráveis ficam separadas.
    (REPORTS / "pilot_cards_generated_v2.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
