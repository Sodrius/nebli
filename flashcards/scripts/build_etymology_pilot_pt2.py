#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constrói o piloto pt2 curado e aplica gates derivados do feedback humano."""
from __future__ import annotations

import json
import re
import unicodedata
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ETIM = ROOT / "etimologia"
OUT = ETIM / "cards" / "cards_pilot_pt2.json"
REPORT = ETIM / "reports" / "pilot_cards_pt2.md"
VALIDATION = ETIM / "reports" / "pilot_pt2_validation.md"
LEXICON_JSON = ETIM / "data" / "lexicon_master.json"
LEXICON_CSV = ETIM / "data" / "lexicon_master.csv"
EXPANSION = ETIM / "data" / "lexicon_expansion_pt2.json"

SRC_FOUND = "NCBI Medical Terminology, cap. 1 (2024), NBK607453"
SRC_SYSTEM = "NCBI Medical Terminology, 2a ed. (2024), NBK607454"
SRC_NCI = "NCI Dictionary of Cancer Terms"
SRC_HEMATOMA = "NCBI MedGen C0018944 — https://www.ncbi.nlm.nih.gov/medgen/5484"
SRC_GLAUCOMA = "MedlinePlus Glaucoma — https://medlineplus.gov/glaucoma.html"
SRC_PSEUDOCYST = "NCBI StatPearls NBK557594 — https://www.ncbi.nlm.nih.gov/books/NBK557594/"
SRC_CIS = "NCI carcinoma in situ — https://www.cancer.gov/publications/dictionaries/cancer-terms/def/carcinoma-in-situ"
SRC_ILEUS = "NCBI StatPearls NBK558937 — https://www.ncbi.nlm.nih.gov/books/NBK558937/"
SRC_ANGINA = "NCBI MedGen C0002962 — https://www.ncbi.nlm.nih.gov/medgen/1929"
SRC_DIABETES = "NCBI Bookshelf NBK310272 — diabetes mellitus e insipidus"
SRC_LUPUS = "PubMed PMID 32380218 — história do termo lupus"
DECK = "NEBLI::Etimologia::Piloto pt2"


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def cloze(text: str) -> str:
    """[[x]] vira cloze c1 em negrito; contrastes recuperam tudo junto."""
    return re.sub(r"\[\[(.+?)\]\]", r"<b>{{c1::\1}}</b>", text)


cards: list[dict] = []


def add(name: str, kind: str, body: str, extra: str, canonical: str,
        breakdown: str, literal: str, clinical: str, limit: str,
        family: str, source_medical: str = SRC_SYSTEM) -> None:
    text = "<b>Etimologia.</b> " + cloze(body)
    cards.append({
        "uid": f"etim-pt2-{slugify(name)}",
        "deck": DECK,
        "kind": kind,
        "term_en": "",
        "term_ptbr": canonical,
        "canonical_form": canonical,
        "origin_language": "Not_applicable",
        "morpheme_breakdown": breakdown,
        "literal_gloss": literal,
        "clinical_meaning": clinical,
        "inference_limit": limit,
        "variants": [],
        "text": text,
        "extra": extra,
        "source_etymology": [SRC_FOUND],
        "source_medical": [source_medical],
        "license": "CC BY 4.0 (NCBI/Open RN); definições NCI são domínio público",
        "confidence": "high",
        "number_of_cards": 1,
        "tags": [
            "etim_pilot_pt2", f"etim_uid::{slugify('etim-pt2-' + name)}",
            f"terminologia::card::{kind}", f"terminologia::familia::{family}",
            "terminologia::status::piloto_pt2",
        ],
        "status": "pilot_review",
    })


# Fundamentos mínimos: ensinam o método; não repetem quatro vezes a mesma noção.
add("morfema", "foundation",
    "A menor unidade estrutural de uma palavra com significado ou função gramatical chama-se [[morfema]].",
    "Hipoglicemia contém hipo-, glic- e -emia; cada parte restringe o sentido.",
    "morfema", "hipo- + glic- + -emia", "unidade mínima significativa", "unidade morfológica", "Morfema não é sinônimo de sílaba.", "fundamentos", SRC_FOUND)
add("prefixo", "foundation",
    "Em subcutâneo, sub- funciona morfologicamente como [[prefixo]].",
    "Prefixos antecedem a base: peri- em pericárdio situa, mas não nomeia, a estrutura.",
    "prefixo", "sub- + cutâne/o", "afixo anterior", "modifica a base", "Nem todo termo contém prefixo.", "fundamentos", SRC_FOUND)
add("raiz", "foundation",
    "Em colangite, colang- funciona morfologicamente como [[raiz]].",
    "A raiz concentra o referente; aqui, colang- remete aos ductos biliares.",
    "raiz", "colang- + -ite", "núcleo lexical", "referente principal", "Uma palavra pode conter mais de uma raiz.", "fundamentos", SRC_FOUND)
add("sufixo", "foundation",
    "Em gastrite, -ite age morfologicamente como [[sufixo]].",
    "O sufixo fecha a palavra e frequentemente indica processo, condição ou procedimento.",
    "sufixo", "gastr- + -ite", "afixo final", "classifica o processo", "Nem toda terminação aparente é sufixo.", "fundamentos", SRC_FOUND)
add("forma-combinatoria-vogal", "foundation",
    "Cardi/o é [[forma combinatória]]; nela, o é a [[vogal de ligação]].",
    "A forma reúne raiz e vogal; cardi/o + -logia mantém o, mas cardi/o + -ite o perde.",
    "forma combinatória", "cardi + o", "raiz preparada para combinar", "unidade de composição", "A vogal facilita a junção; não acrescenta sentido.", "fundamentos", SRC_FOUND)
add("decomposicao-composicao", "foundation",
    "Separar pancitopenia em pan- + cit/o + -penia é [[decomposição]]; reuni-los é [[composição]].",
    "Decompor extrai pistas; compor propõe uma glosa que ainda precisa de confirmação clínica.",
    "decomposição e composição", "pan- + cit/o + -penia", "separar e reunir", "processos inversos", "A composição literal não garante definição clínica.", "fundamentos", SRC_FOUND)
add("glosa-definicao", "foundation",
    "A tradução dos morfemas fornece a [[glosa literal]]; o uso médico vigente fornece a [[definição clínica]].",
    "Em hematoma, “massa sanguínea” orienta; não autoriza concluir neoplasia.",
    "glosa literal e definição clínica", "hemat- + -oma", "massa de sangue", "coleção de sangue extravasado", "O literal é hipótese de leitura, não diagnóstico.", "fundamentos", SRC_FOUND)
add("pontes-ortograficas", "foundation",
    "Em português médico, ph costuma virar [[f]], th vira [[t]] e y vira [[i]].",
    "Assim, phleb-, thorac- e glyc- aparecem como fleb-, torac- e glic-.",
    "pontes ortográficas", "ph→f; th→t; y→i", "adaptações gráficas", "reconhecimento entre línguas", "São tendências, não regras fonológicas universais.", "fundamentos", SRC_FOUND)

# Famílias confundíveis: as lacunas compartilham c1 para recuperar o contraste inteiro.
CONTRASTS = [
    ("tomia-ectomia-stomia", "-tomia indica [[incisão]]; -ectomia, [[remoção]]; -stomia, [[abertura criada]].", "Laparotomia abre; gastrectomia retira; gastrostomia cria comunicação com o estômago.", "-tomia × -ectomia × -stomia"),
    ("plastia-pexia-rafia", "-plastia indica [[reconstrução]]; -pexia, [[fixação]]; -rafia, [[sutura]].", "Rinoplastia remodela; gastropexia fixa; herniorrafia sutura.", "-plastia × -pexia × -rafia"),
    ("grafia-grama-grafo", "-grafia nomeia o [[processo de registro]]; -grama, o [[resultado]]; -grafo, o [[instrumento]].", "Eletrocardiografia produz eletrocardiograma; o eletrocardiógrafo registra.", "-grafia × -grama × -grafo"),
    ("metria-metro", "-metria nomeia a [[medição]]; -metro, o [[instrumento]].", "Espirometria é o procedimento; espirômetro é o aparelho.", "-metria × -metro"),
    ("scopia-scopio", "-scopia nomeia a [[visualização]]; -scópio, o [[instrumento]].", "Endoscopia é o exame; endoscópio é o instrumento.", "-scopia × -scópio"),
    ("centese-biopsia-aspiracao", "-centese indica [[punção]]; biópsia obtém [[tecido]]; aspiração remove [[conteúdo]].", "Amniocentese punciona; biópsia amostra tecido; aspiração retira líquido ou gás.", "-centese × biópsia × aspiração"),
    ("algia-odinia", "-algia indica [[dor]]; -odinia também indica [[dor]], geralmente em termos mais específicos.", "Disfagia é dificuldade; odinofagia é dor ao engolir.", "-algia × -odinia"),
    ("penia-citose", "-penia indica [[redução numérica]]; -citose, [[aumento celular]].", "Leucopenia reduz leucócitos; leucocitose os aumenta.", "-penia × -citose"),
    ("ectasia-estenose", "-ectasia indica [[dilatação]]; -estenose, [[estreitamento]].", "Bronquiectasia dilata brônquios; broncoestenose estreita sua luz.", "-ectasia × -estenose"),
    ("rreia-rragia", "-rreia indica [[fluxo]]; -rragia, [[sangramento intenso]].", "Diarreia descreve fluxo; metrorragia, sangramento uterino.", "-rreia × -rragia"),
    ("paresia-plegia", "-paresia indica [[fraqueza]]; -plegia, [[paralisia]].", "Hemiparesia preserva movimento parcial; hemiplegia implica paralisia do hemicorpo.", "-paresia × -plegia"),
    ("emia-uria", "-emia situa algo no [[sangue]]; -úria, na [[urina]].", "Glicemia mede glicose sanguínea; glicosúria indica glicose urinária.", "-emia × -úria"),
    ("pneia-capnia", "-pneia refere-se à [[respiração]]; -capnia, ao [[dióxido de carbono]].", "Taquipneia altera frequência respiratória; hipercapnia eleva CO₂.", "-pneia × -capnia"),
    ("plasia-trofia", "Hiperplasia aumenta o [[número celular]]; hipertrofia aumenta o [[tamanho celular]].", "-plasia alude à formação; -trofia, ao crescimento. O contraste clínico aqui é número versus tamanho.", "hiperplasia × hipertrofia"),
    ("genese-poiese", "-gênese indica [[formação]] ampla; -poiese enfatiza [[produção]].", "Angiogênese forma vasos; hematopoiese produz células sanguíneas.", "-gênese × -poiese"),
    ("ab-ad", "ab- indica [[afastamento]]; ad-, [[aproximação]].", "Abdução afasta da linha média; adução aproxima.", "ab- × ad-"),
    ("ecto-exo", "ecto- descreve posição [[externa]]; exo- marca movimento ou origem [[para fora]].", "Ectoderma é camada externa; exocitose transporta conteúdo para fora.", "ecto- × exo-"),
    ("epi-peri-para", "epi- indica [[sobre]]; peri-, [[ao redor]]; para-, [[ao lado]].", "Epicárdio reveste a superfície; pericárdio circunda; paratireoide fica junto à tireoide.", "epi- × peri- × para-"),
]
for name, body, extra, canonical in CONTRASTS:
    add(name, "contrast", body, extra, canonical, canonical, canonical, canonical,
        "O contexto do termo pode especializar o valor do morfema.", "contrastes", SRC_FOUND)

# Raízes menos expostas e produtivas. O Extra apresenta uso que justifica o card.
ROOTS = [
    ("sial-o", "A forma combinatória sial/o refere-se à [[saliva]].", "Sialolitíase é cálculo no sistema salivar: sial/o + lit/o + -íase.", "sial/o", "saliva"),
    ("dacri-o", "A forma combinatória dacri/o refere-se às [[lágrimas]].", "Dacriocistite inflama o saco lacrimal: dacri/o + cist/o + -ite.", "dacri/o", "lágrima"),
    ("blefar-o", "A forma combinatória blefar/o refere-se à [[pálpebra]].", "Blefaroptose é queda palpebral: blefar/o + -ptose.", "blefar/o", "pálpebra"),
    ("piel-o", "No sistema urinário, piel/o refere-se à [[pelve renal]].", "Pielonefrite combina pelve renal, rim e inflamação.", "piel/o", "pelve renal"),
    ("pi-o", "A forma combinatória pi/o refere-se a [[pus]].", "Piotórax é presença de pus na cavidade torácica.", "pi/o", "pus"),
    ("calic-o", "A forma combinatória calic/o refere-se ao [[cálice renal]].", "Calicectasia é dilatação dos cálices renais.", "calic/o", "cálice renal"),
    ("colangi-o", "A forma combinatória colangi/o refere-se aos [[ductos biliares]].", "Colangite inflama ductos biliares; não a vesícula.", "colangi/o", "ducto biliar"),
    ("colecist-o", "A forma combinatória colecist/o refere-se à [[vesícula biliar]].", "Colecistectomia remove a vesícula; colangite envolve os ductos.", "colecist/o", "vesícula biliar"),
    ("miring-o", "A forma combinatória miring/o refere-se à [[membrana timpânica]].", "Miringotomia é incisão da membrana timpânica.", "miring/o", "membrana timpânica"),
    ("estaped-o", "A forma combinatória estaped/o refere-se ao [[estribo]].", "Estapedectomia remove parcial ou totalmente esse ossículo.", "estaped/o", "estribo"),
    ("esfigm-o", "A forma combinatória esfigm/o refere-se ao [[pulso]].", "Esfigmomanômetro contém esfigm/o, embora meça pressão arterial.", "esfigm/o", "pulso"),
    ("onic-o", "A forma combinatória onic/o refere-se à [[unha]].", "Onicomicose é micose ungueal: onic/o + mic/o + -ose.", "onic/o", "unha"),
    ("xant-o", "A forma combinatória xant/o refere-se à cor [[amarela]].", "Xantocromia descreve coloração amarelada, como no líquor.", "xant/o", "amarelo"),
    ("hial-o", "A forma combinatória hial/o indica aspecto [[vítreo]].", "Hialino descreve aparência translúcida; não uma composição química única.", "hial/o", "vidro"),
    ("acin-o", "A forma combinatória acin/o indica estrutura em [[bago]].", "Ácinos são unidades secretoras arredondadas, semelhantes a pequenos cachos.", "acin/o", "bago"),
    ("trabecul-o", "A forma combinatória trabecul/o refere-se a uma [[pequena viga]].", "Trabéculas são suportes em rede, como no osso esponjoso.", "trabecul/o", "pequena viga"),
    ("glomerul-o", "A forma combinatória glomerul/o refere-se a um [[pequeno novelo]].", "Glomérulo nomeia a rede capilar renal por sua forma enovelada.", "glomerul/o", "pequeno novelo"),
    ("hil-o", "A forma combinatória hil/o refere-se ao [[hilo]].", "No pulmão, hilo é a região medial por onde passam brônquios, vasos, linfáticos e nervos; hilar significa relativo a essa região.", "hil/o", "hilo"),
    ("foramin-o", "A forma foramin/o refere-se a uma [[abertura]].", "Forame é uma abertura anatômica para nervos ou vasos. Na estenose foraminal, esse espaço estreita e pode comprimir a raiz nervosa.", "foramin/o", "abertura"),
    ("diverticul-o", "A forma combinatória diverticul/o refere-se a uma [[evaginação sacular]].", "Diverticulite é inflamação de divertículo; diverticulose indica sua presença.", "diverticul/o", "desvio ou bolsa"),
]
for name, body, extra, canonical, meaning in ROOTS:
    add(name, "morpheme_in_context", body, extra, canonical, canonical, meaning, meaning,
        "A raiz orienta a estrutura; não determina doença ou mecanismo.", "raizes-raras")

# Transferência: os Extras sempre decompõem e interpretam; nunca dizem apenas “partes”.
TRANSFERS = [
    ("sialolitíase", "Pelos componentes, sialolitíase sugere [[cálculo salivar]].", "sial/o (saliva) + lit/o (cálculo) + -íase (condição) = cálculo no sistema salivar."),
    ("dacriocistite", "Pelos componentes, dacriocistite sugere inflamação do [[saco lacrimal]].", "dacri/o (lágrima) + cist/o (saco) + -ite (inflamação) = inflamação do saco lacrimal."),
    ("blefaroptose", "Pelos componentes, blefaroptose sugere [[queda palpebral]].", "blefar/o (pálpebra) + -ptose (queda) = descenso da pálpebra."),
    ("piotórax", "Pelos componentes, piotórax sugere [[pus torácico]].", "pi/o (pus) + torac/o (tórax) = pus na cavidade torácica; equivale a empiema pleural."),
    ("calicectasia", "Pelos componentes, calicectasia sugere [[dilatação calicial]].", "calic/o (cálice renal) + -ectasia (dilatação) = dilatação dos cálices renais."),
    ("coledocolitíase", "Pelos componentes, coledocolitíase sugere cálculo no [[colédoco]].", "coledoc/o (colédoco) + lit/o (cálculo) + -íase = cálculo no ducto biliar comum."),
    ("colecistectomia", "Pelos componentes, colecistectomia indica [[remoção vesicular]].", "colecist/o (vesícula biliar) + -ectomia (remoção) = retirada cirúrgica da vesícula."),
    ("miringotomia", "Pelos componentes, miringotomia indica [[incisão timpânica]].", "miring/o (tímpano) + -tomia (incisão) = abertura cirúrgica da membrana timpânica."),
    ("estapedectomia", "Pelos componentes, estapedectomia indica remoção do [[estribo]].", "estaped/o (estribo) + -ectomia (remoção) = retirada parcial ou total do ossículo."),
    ("esfigmomanômetro", "A raiz esfigm/o em esfigmomanômetro alude ao [[pulso]].", "esfigm/o (pulso) + man/o (pressão) + -metro = instrumento de pressão; hoje mede pressão arterial."),
    ("onicomicose", "Pelos componentes, onicomicose sugere [[micose ungueal]].", "onic/o (unha) + mic/o (fungo) + -ose = infecção fúngica da unha."),
    ("xantocromia", "Pelos componentes, xantocromia indica coloração [[amarelada]].", "xant/o (amarelo) + -cromia (cor) = aspecto amarelado; a etiologia depende do contexto."),
    ("hialinose", "Pelos componentes, hialinose sugere depósito de aspecto [[vítreo]].", "hial/o (vítreo) + -ose (condição) = material hialino; o termo não define composição única."),
    ("acinar", "Morfologicamente, acinar significa semelhante a [[bago]].", "acin/o (bago) + -ar (relativo a) = organização em pequenas unidades secretoras arredondadas."),
    ("trabecular", "Morfologicamente, trabecular significa organizado em [[pequenas vigas]].", "trabecul/o (pequena viga) + -ar = arquitetura em barras ou lâminas de sustentação."),
    ("glomerulopatia", "Pelos componentes, glomerulopatia indica doença do [[glomérulo]].", "glomerul/o (glomérulo) + -patia (doença) = categoria ampla; não especifica o mecanismo."),
    ("hilar", "Morfologicamente, hilar significa relativo ao [[hilo]].", "hil/o (hilo) + -ar (relativo a) = região de trânsito de vasos, nervos ou ductos."),
    ("foraminal", "Morfologicamente, foraminal significa relativo a uma [[abertura]].", "foramin/o (forame) + -al (relativo a) = relacionado a um forame anatômico."),
    ("diverticulite", "Pelos componentes, diverticulite sugere [[inflamação diverticular]].", "diverticul/o (divertículo) + -ite (inflamação) = divertículo inflamado; não apenas sua presença."),
    ("broncorreia", "Pelos componentes, broncorreia sugere [[fluxo brônquico]].", "bronc/o (brônquio) + -rreia (fluxo) = secreção brônquica excessiva; não significa hemorragia."),
]
for name, body, extra in TRANSFERS:
    add(name, "transfer", body, extra, name, extra.split("=")[0].strip(), "inferência morfológica", "ver Texto",
        "A decomposição prevê uma classe de sentido, não etiologia ou gravidade.", "transferencia")

# Armadilhas em que a forma engana ou é insuficiente.
EXCEPTIONS = [
    ("hematoma", "Apesar de -oma, hematoma não implica [[neoplasia]].", "hemat- (sangue) + -oma (massa) = coleção localizada de sangue extravasado.", "coleção sanguínea", SRC_HEMATOMA),
    ("glaucoma", "Em glaucoma, a terminação -oma não significa [[tumor]].", "Glaucoma nomeia neuropatia óptica; segmentá-lo como neoplasia produz falsa etimologia.", "neuropatia óptica", SRC_GLAUCOMA),
    ("pseudocisto", "Um pseudocisto, apesar do nome, não possui [[revestimento epitelial]].", "pseudo- (falso) + cist/o (cisto) = coleção encapsulada sem epitélio verdadeiro.", "coleção sem epitélio", SRC_PSEUDOCYST),
    ("carcinoma-in-situ", "Carcinoma in situ permanece sem [[invasão estromal]].", "in situ significa “no lugar”: células malignas ainda não atravessaram a membrana basal.", "neoplasia não invasiva", SRC_CIS),
    ("ileo", "O termo íleo não significa doença restrita ao [[íleo intestinal]].", "Íleo é parada funcional do trânsito; a semelhança gráfica com o segmento intestinal engana.", "obstrução funcional", SRC_ILEUS),
    ("angina-pectoris", "Em angina pectoris, angina não designa inflamação da [[garganta]].", "Angina alude a aperto; pectoris situa no peito. O termo vigente descreve desconforto isquêmico.", "desconforto isquêmico", SRC_ANGINA),
    ("diabetes-mellitus-insipidus", "Mellitus significa [[doce]]; insipidus, [[sem sabor]].", "Os qualificadores vêm da urina historicamente provada; não explicam os mecanismos atuais.", "qualificadores históricos", SRC_DIABETES),
    ("lupus", "A origem “lobo” de lúpus não fornece sua [[definição clínica]].", "A imagem histórica pode ajudar a lembrar o nome, mas não permite inferir autoimunidade.", "termo histórico", SRC_LUPUS),
]
for name, body, extra, clinical, source in EXCEPTIONS:
    add(name, "exception", body, extra, name, name, "origem ou aparência histórica", clinical,
        "O uso médico vigente prevalece sobre uma segmentação literal.", "armadilhas", source)

# Polissemias e duplas greco-latinas que aumentam rigor de leitura e fala.
NUANCES = [
    ("mielo-polissemia", "A forma miel/o pode indicar [[medula óssea]] ou [[medula espinal]].", "Mielograma hematológico examina medula óssea; mielopatia neurológica envolve medula espinal.", "miel/o", "medula"),
    ("cisto-polissemia", "A forma cist/o pode indicar [[bexiga]] ou [[cisto]].", "Cistoscopia examina a bexiga; pseudocisto nomeia uma coleção semelhante a cisto.", "cist/o", "bexiga ou cisto"),
    ("metro-polissemia", "Metr/o pode indicar [[útero]]; -metro indica [[instrumento medidor]].", "Endométrio contém metr/o uterino; termômetro termina em -metro instrumental.", "metr/o × -metro", "útero ou medidor"),
    ("vaso-polissemia", "Vas/o pode indicar [[vaso]] sanguíneo ou [[ducto]].", "Vasodilatação envolve vasos; vasectomia secciona o ducto deferente.", "vas/o", "vaso ou ducto"),
    ("nefro-reno", "Nefr/o é a forma [[grega]] para rim; ren/o, a [[latina]].", "Nefropatia e renal compartilham referente, mas seguem tradições lexicais diferentes.", "nefr/o × ren/o", "rim"),
    ("oftalmo-oculo", "Oftalm/o é a forma [[grega]] para olho; ocul/o, a [[latina]].", "Oftalmologia usa a forma grega; oculomotor conserva a latina.", "oftalm/o × ocul/o", "olho"),
    ("flebo-veno", "Fleb/o é a forma [[grega]] para veia; ven/o, a [[latina]].", "Flebite usa a forma grega; venoso e intravenoso, a latina.", "fleb/o × ven/o", "veia"),
    ("odonto-dento", "Odont/o é a forma [[grega]] para dente; dent/o, a [[latina]].", "Odontologia usa a forma grega; dental e dentição, a latina.", "odont/o × dent/o", "dente"),
]
for name, body, extra, canonical, meaning in NUANCES:
    add(name, "contrast", body, extra, canonical, canonical, meaning, meaning,
        "A forma ativa depende do termo e da tradição lexical.", "polissemia-duplas")


def count_words(s: str) -> int:
    clean = re.sub(r"<[^>]+>", " ", s)
    clean = re.sub(r"\{\{c\d+::|\}\}", " ", clean)
    return len(re.findall(r"\b[\wÀ-ÿ/-]+\b", clean))


def validate() -> tuple[list[str], dict]:
    errors: list[str] = []
    uids: set[str] = set()
    fronts: set[str] = set()
    answer_lengths: list[int] = []
    forbidden_extra = ("referente a ", "preserva esse núcleo", "partes:", "evita trocar")
    for c in cards:
        uid = c["uid"]
        if uid in uids: errors.append(f"{uid}: UID duplicado")
        uids.add(uid)
        if c["text"] in fronts: errors.append(f"{uid}: frente duplicada")
        fronts.add(c["text"])
        if not c["text"].startswith("<b>Etimologia.</b> "):
            errors.append(f"{uid}: rótulo temático ausente")
        if count_words(c["text"]) > 25: errors.append(f"{uid}: Texto >25 palavras")
        if count_words(c["extra"]) > 40: errors.append(f"{uid}: Extra >40 palavras")
        found = re.findall(r"<b>\{\{c(\d+)::(.+?)\}\}</b>", c["text"])
        raw = re.findall(r"\{\{c(\d+)::(.+?)\}\}", c["text"])
        if found != raw: errors.append(f"{uid}: cloze não está integralmente em negrito")
        if not 1 <= len(found) <= 3: errors.append(f"{uid}: exige 1–3 ocorrências de cloze")
        if any(n != "1" for n, _ in found): errors.append(f"{uid}: contraste deve usar somente c1")
        for _, answer in found:
            n = count_words(answer); answer_lengths.append(n)
            if n > 3: errors.append(f"{uid}: resposta com {n} palavras")
        low_extra = c["extra"].casefold()
        if any(x in low_extra for x in forbidden_extra): errors.append(f"{uid}: Extra genérico proibido")
        if c["kind"] == "transfer" and not ("+" in c["extra"] and "=" in c["extra"]):
            errors.append(f"{uid}: transferência sem decomposição interpretada")
        if c["kind"] == "contrast" and len(found) < 2:
            errors.append(f"{uid}: contraste sem recuperação conjunta")
        if not c["source_etymology"] or not c["source_medical"]:
            errors.append(f"{uid}: fonte ausente")
        if c["confidence"] != "high": errors.append(f"{uid}: confiança não alta")
    stats = {
        "notes": len(cards), "anki_cards": len(cards),
        "max_text_words": max(map(lambda c: count_words(c["text"]), cards)),
        "max_extra_words": max(map(lambda c: count_words(c["extra"]), cards)),
        "max_answer_words": max(answer_lengths),
        "one_word_answer_pct": round(100 * sum(x == 1 for x in answer_lengths) / len(answer_lengths), 1),
        "kinds": dict(Counter(c["kind"] for c in cards)),
    }
    return errors, stats


def sync_lexicon() -> int:
    """Acrescenta ao corpus mestre os conceitos novos do piloto, sem duplicar."""
    rows = json.loads(LEXICON_JSON.read_text(encoding="utf-8"))
    fields = list(rows[0])
    present = {slugify(r["entrada_canonica"]): r for r in rows}
    additions = []
    for c in cards:
        key = slugify(c["canonical_form"])
        existing = present.get(key)
        if existing and not str(existing.get("id", "")).startswith("etim-pt2-"):
            continue
        typ = "familia" if c["kind"] == "contrast" else ("termo" if c["kind"] in {"transfer", "exception"} else "morfema")
        row = {field: "" for field in fields}
        row.update({
            "id": c["uid"], "entrada_canonica": c["canonical_form"],
            "tipo_de_entrada": typ, "tipo_morfologico": c["kind"],
            "origem": c["origin_language"], "significado_nuclear": c["literal_gloss"],
            "significado_literal": c["literal_gloss"], "definicao_medica": c["clinical_meaning"],
            "categoria_semantica": c["tags"][3].split("::")[-1], "sistema": "transversal",
            "disciplinas": "terminologia médica", "produtividade": 2,
            "frequencia_curricular": 2, "transferibilidade": 2,
            "risco_de_confusao": 2 if c["kind"] in {"contrast", "exception"} else 1,
            "prioridade": 18 if c["kind"] in {"contrast", "exception", "transfer"} else 15,
            "nivel": "nucleo" if c["kind"] in {"contrast", "exception"} else "extensao",
            "exemplos": c["extra"], "limites_etimologicos": c["inference_limit"],
            "fonte": "; ".join(dict.fromkeys(c["source_etymology"] + c["source_medical"])),
            "confianca": "alta", "status_validacao": "piloto_pt2_validado_automaticamente",
            "destino_pedagogico": "card_proprio", "nota_que_cobre": c["uid"],
            "gera_card": "sim", "direcao_do_card": "aplicacao" if c["kind"] == "transfer" else "reconhecimento",
            "numero_de_cards": 1, "tags": ";".join(c["tags"]),
            "observacoes": "Incluído após feedback humano do piloto v2; prioriza confusão, baixa exposição e transferência.",
        })
        if existing:
            existing.update(row)
        else:
            additions.append(row); rows.append(row)
        present[key] = row
    LEXICON_JSON.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    with LEXICON_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(rows)
    expansion_rows = [r for r in rows if str(r.get("id", "")).startswith("etim-pt2-")]
    EXPANSION.write_text(json.dumps(expansion_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(additions)


def main() -> int:
    errors, stats = validate()
    if errors:
        print("\n".join("ERRO " + e for e in errors))
        return 1
    added = sync_lexicon()
    payload = {
        "version": "pilot-pt2-2026-07-17",
        "approval_gate": "pilot_pt2_pending_user_review",
        "policy": {
            "text_words": 25, "extra_words_preferred": 25, "extra_words": 40, "cloze_answer_words": 3,
            "same_c1_for_contrasts": True, "neutral_theme_label": "Etimologia",
            "obvious_roots_without_transfer_gain": "rejected",
        },
        "stats": stats,
        "cards": cards,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Piloto de etimologia — pt2", "",
        "> Piloto novo e independente. O arquivo `pilot_cards.md` anotado foi preservado.", "",
        f"- Notas/cards: {len(cards)}", "- Status: aguardando revisão humana",
        "- Todos os contrastes usam apenas `c1` e geram um único card.", "",
    ]
    for i, c in enumerate(cards, 1):
        lines += [f"## {i:03d} — {c['uid']}", "", f"**Texto:** {c['text']}", "",
                  f"**Extra:** {c['extra']}", "", f"**Família:** `{c['tags'][3]}`", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    VALIDATION.write_text(
        "# Validação do piloto pt2\n\n" +
        "\n".join(f"- {k}: {v}" for k, v in stats.items()) +
        "\n- Violações: 0\n- Gate humano: pendente\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    print(f"léxico mestre: +{added} entradas (total idempotente)")
    print(f"OK: {OUT}\nOK: {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
