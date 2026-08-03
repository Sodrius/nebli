#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gera o deck integral v3 a partir do léxico mestre e de lacunas curadas."""
from __future__ import annotations

import csv
import importlib.util
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ETIM = ROOT / "etimologia"
LEXICON_JSON = ETIM / "data" / "lexicon_master.json"
LEXICON_CSV = ETIM / "data" / "lexicon_master.csv"
CURRICULUM = ETIM / "data" / "curriculum_expansion_v3.json"
OUT = ETIM / "cards" / "cards_approved_v3.json"
REPORT = ETIM / "reports" / "full_deck_v3.md"
VALIDATION = ETIM / "reports" / "validation_full_v3.md"
COMPRESSION = ETIM / "reports" / "compression_full_v3.md"

SRC_TERM = "Open RN Medical Terminology, 2a ed., NCBI NBK607453/NBK607454"
SRC_PHYS = "NCBI StatPearls Physiology/Homeostasis NBK559138"
SRC_PATH = "NLM MeSH e NCBI Bookshelf, terminologia patológica"
SRC_SEMI = "NCBI Clinical Methods e StatPearls, semiologia"
SRC_PHARM = "NCBI Nursing Pharmacology NBK595006 e Pharmacodynamics NBK507791"
SRC_TA = "FIPAT, Terminologia Anatomica, 2a ed. (2019; IFAA aprovada em 2020)"


def load_transfer_breakdowns() -> dict[str, str]:
    source = Path(__file__).with_name("build_etymology_v2.py").read_text(encoding="utf-8")
    match = re.search(r'TRANSFERS\s*=\s*parse_block\(r"""(.*?)"""\)', source, re.S)
    if not match: return {}
    out = {}
    for line in match.group(1).splitlines():
        if "=" not in line or "|" not in line: continue
        term, rest = line.split("=", 1); _, breakdown = rest.split("|", 1)
        out[norm(term.strip())] = breakdown.strip()
    return out


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def norm(s: str) -> str:
    return slug(s).replace("-", "")


TRANSFER_BREAKDOWNS = load_transfer_breakdowns()


def wc(s: str) -> int:
    s = re.sub(r"<[^>]+>|\{\{c\d+::|\}\}", " ", s)
    return len(re.findall(r"\b[\wÀ-ÿ/-]+\b", s))


def cloze(s: str) -> str:
    return re.sub(r"\[\[(.+?)\]\]", r"<b>{{c1::\1}}</b>", s)


def load_pilot() -> list[dict]:
    path = Path(__file__).with_name("build_etymology_pilot_pt2.py")
    spec = importlib.util.spec_from_file_location("pilot_pt2", path)
    module = importlib.util.module_from_spec(spec); assert spec.loader
    spec.loader.exec_module(module)
    return [dict(c) for c in module.cards]


DECKS = {
    "fundamentos": "NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo",
    "prefixos": "NEBLI::Etimologia::02_Prefixos::00_Visao_integral",
    "sufixos": "NEBLI::Etimologia::03_Sufixos::00_Visao_integral",
    "anatomia": "NEBLI::Etimologia::04_Raizes_por_sistema::11_Transversal_e_formas",
    "latim_anatomico": "NEBLI::Etimologia::04_Raizes_por_sistema::00_Nomenclatura_anatomica_latina",
    "fisiologia": "NEBLI::Etimologia::05_Processos_medicos::00_Fisiologia_e_bioquimica",
    "patologia": "NEBLI::Etimologia::05_Processos_medicos::01_Patologia_geral",
    "semiologia": "NEBLI::Etimologia::05_Processos_medicos::05_Clinica_e_exame_fisico",
    "farmacologia": "NEBLI::Etimologia::05_Processos_medicos::03_Farmacologia",
    "contrastes": "NEBLI::Etimologia::06_Familias_e_contrastes::03_Processos_confundiveis",
    "duplas": "NEBLI::Etimologia::06_Familias_e_contrastes::01_Pares_grego_latim",
    "armadilhas": "NEBLI::Etimologia::07_Excecoes_e_armadilhas::03_Sentido_literal_vs_clinico",
    "transferencia": "NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo",
}

CURATED: list[dict] = []


def curate(name: str, kind: str, discipline: str, body: str, extra: str,
           canonical: str, meaning: str, source: str = SRC_TERM,
           unfamiliar: bool = False) -> None:
    CURATED.append({"name": name, "kind": kind, "discipline": discipline,
                    "body": body, "extra": extra, "canonical": canonical,
                    "meaning": meaning, "source": source, "unfamiliar": unfamiliar})


# Procedimentos raros e frequentemente confundidos.
for x in [
    ("clasia-dese", "-clasia indica [[fratura cirúrgica]]; -dese, [[fusão cirúrgica]].", "Osteoclasia quebra osso deliberadamente; artrodese imobiliza uma articulação pela fusão.", "-clasia × -dese", "quebrar × fundir"),
    ("tripsia-clasia", "-tripsia indica [[fragmentação]]; -clasia, [[fratura]].", "Litotripsia fragmenta cálculos por energia; osteoclasia fratura osso para corrigir deformidade.", "-tripsia × -clasia", "fragmentar × fraturar"),
    ("ablacao-excisao-resseccao", "Ablação [[destrói]] tecido; excisão o [[retira]]; ressecção remove [[parte estrutural]].", "A ablação pode não retirar a peça; excisão corta uma lesão; ressecção remove segmento de órgão.", "ablação × excisão × ressecção", "destruir × retirar × segmentar"),
    ("anastomose-derivacao", "Anastomose cria [[união]] entre estruturas; derivação cria [[rota alternativa]].", "Anastomose reconecta alças; derivação desvia o fluxo, podendo usar uma anastomose para construir o novo trajeto.", "anastomose × derivação", "união × desvio"),
    ("rrexis", "O sufixo -rrexis indica [[ruptura]].", "Amniorrexe é ruptura da bolsa amniótica; o sufixo não informa se foi espontânea ou artificial.", "-rrexis", "ruptura"),
]: curate(x[0], "contrast" if "×" in x[3] else "morpheme_in_context", "contrastes", x[1], x[2], x[3], x[4], unfamiliar=True)

# Forma e microarquitetura anatômica.
ANATOMY = [
    ("braqui", "braqui-", "curto", "Braquicefalia descreve crânio proporcionalmente curto; não significa cabeça pequena."),
    ("dolico", "dolico-", "longo", "Dolicocefalia descreve crânio proporcionalmente alongado; contrasta com braquicefalia."),
    ("plati", "plati-", "plano", "Platispondilia descreve achatamento dos corpos vertebrais: plati- + spondil/o."),
    ("lepto", "lepto-", "delgado", "Leptomeninges são as meninges finas: aracnoide e pia-máter."),
    ("paqui", "paqui-", "espesso", "Paquimeninge é a meninge espessa: a dura-máter."),
    ("papil", "papil/o", "papila", "Papila é uma pequena projeção; papiledema é edema do disco óptico, não de qualquer papila."),
    ("vil", "vil/o", "vilo", "Vilosidades intestinais são projeções da mucosa que ampliam a superfície absortiva."),
    ("fascicul", "fascicul/o", "feixe", "Fascículo é um conjunto organizado de fibras, como axônios ou fibras musculares."),
    ("lobul", "lobul/o", "pequeno lobo", "Lóbulo é subdivisão de um lobo; no fígado, organiza placas celulares ao redor da veia central."),
    ("fissur", "fissur/o", "fenda", "Fissura é uma abertura alongada e profunda; costuma separar partes anatômicas maiores."),
    ("sulc", "sulc/o", "sulco", "Sulco é uma depressão linear; no cérebro, separa giros sem atravessar todo o órgão."),
    ("antr", "antr/o", "cavidade", "Antro é uma cavidade dentro de osso ou órgão, como o antro maxilar ou gástrico."),
    ("lamin", "lamin/o", "lâmina", "Lâmina é uma placa fina; a lâmina vertebral integra o arco posterior da vértebra."),
    ("sept", "sept/o", "septo", "Septo é uma parede divisória, como o septo interventricular entre os ventrículos."),
    ("plex", "plex/o", "rede", "Plexo é uma rede entrelaçada de nervos ou vasos, como o plexo braquial."),
    ("lumen", "lumin/o", "luz interna", "Lúmen é o espaço interno de um tubo, como vaso, intestino ou ducto."),
    ("duct", "duct/o", "ducto", "Ducto é um canal que conduz secreção ou fluido, como o colédoco."),
    ("sacc", "sacc/o", "saco", "Saco é uma cavidade em fundo cego; cist/o também pode expressar ideia semelhante."),
    ("apic", "apic/o", "ápice", "Ápice é a extremidade pontuda ou terminal; o ápice cardíaco aponta inferolateralmente."),
    ("bas", "bas/o", "base", "Base é a parte de apoio; no coração, fica oposta ao ápice e é predominantemente posterior."),
]
for name, form, meaning, extra in ANATOMY:
    curate(name, "morpheme_in_context", "anatomia", f"A forma {form} indica [[{meaning}]].", extra, form, meaning, unfamiliar=True)

# Cor e aparência: úteis em anatomia, patologia e semiologia.
for name, form, meaning, extra in [
    ("alb", "alb/o", "branco", "Albinismo envolve redução ou ausência de melanina; alb/o descreve a cor, não o mecanismo."),
    ("clor", "clor/o", "verde", "Cloroma é nome histórico do sarcoma mieloide pela coloração esverdeada causada por mieloperoxidase."),
    ("cian", "cian/o", "azul", "Cianose é coloração azulada de pele ou mucosas; a raiz descreve aparência, não a causa."),
    ("rubr", "rubr/o", "vermelho", "Núcleo rubro recebe o nome pela coloração avermelhada observada anatomicamente."),
    ("nigr", "nigr/o", "negro", "Substância negra é pigmentada por neuromelanina; nigr/o descreve sua aparência macroscópica."),
    ("poli-cor", "poli/o", "cinzento", "Poliomielite combina poli/o, medula e inflamação: historicamente, alude à substância cinzenta."),
    ("lute", "lute/o", "amarelo", "Corpo lúteo significa corpo amarelo; sua cor decorre de pigmentos lipídicos."),
    ("purpur", "purpur/o", "púrpura", "Púrpura descreve extravasamento sanguíneo cutâneo; a cor não informa a causa da hemorragia."),
]: curate(name, "morpheme_in_context", "anatomia", f"A forma {form} indica [[{meaning}]].", extra, form, meaning, unfamiliar=True)

# Curso temporal e evolução clínica.
for name, body, extra, canonical, meaning in [
    ("agudo-cronico", "Agudo indica início [[rápido]]; crônico, duração [[prolongada]].", "Os termos descrevem tempo, não gravidade: uma doença aguda pode ser leve; uma crônica, estável.", "agudo × crônico", "rápido × prolongado"),
    ("subagudo", "Subagudo ocupa intervalo [[intermediário]] entre agudo e crônico.", "O limite temporal varia conforme a doença; subagudo não possui duração universal.", "subagudo", "intermediário"),
    ("recorrente-persistente", "Recorrente [[reaparece]] após intervalos; persistente [[permanece]].", "Crises recorrentes têm períodos sem manifestação; quadro persistente continua além do tempo esperado.", "recorrente × persistente", "reaparece × permanece"),
    ("intermitente-continuo", "Intermitente apresenta [[intervalos]]; contínuo ocorre [[sem interrupção]].", "Febre intermitente retorna após períodos afebris; febre contínua permanece elevada com pouca oscilação.", "intermitente × contínuo", "intervalos × continuidade"),
    ("episodico-paroxistico", "Episódico ocorre em [[eventos separados]]; paroxístico começa [[subitamente]].", "Paroxismo é ataque abrupto e intenso; episódico apenas informa que há episódios delimitados.", "episódico × paroxístico", "eventos × súbito"),
    ("transitorio-persistente", "Transitório [[cessa]] em pouco tempo; persistente [[continua]].", "Transitório não significa benigno: um déficit neurológico breve ainda pode exigir investigação urgente.", "transitório × persistente", "cessa × continua"),
    ("congenito-adquirido", "Congênito está [[presente ao nascer]]; adquirido surge [[depois]].", "Congênito não é sinônimo de hereditário: infecções intrauterinas podem produzir alterações congênitas não genéticas.", "congênito × adquirido", "ao nascer × depois"),
    ("pre-peri-pos-natal", "Pré-natal é [[antes do nascimento]]; perinatal, [[ao redor dele]]; pós-natal, [[depois]].", "Perinatal cobre período próximo ao parto; seus limites exatos variam conforme a convenção usada.", "pré-natal × perinatal × pós-natal", "antes × ao redor × depois"),
    ("progressivo-regressivo", "Progressivo [[avança]] ao longo do tempo; regressivo [[recua]].", "Progressão pode aumentar extensão ou gravidade; regressão pode ser espontânea ou terapêutica.", "progressivo × regressivo", "avança × recua"),
    ("remitente-recidivante", "Remissão indica [[redução]] da atividade; recidiva, [[retorno]].", "Na forma remitente-recidivante, surtos são seguidos por melhora parcial ou completa.", "remitente × recidivante", "redução × retorno"),
    ("fulminante", "Fulminante descreve evolução [[rápida e grave]].", "O termo comunica velocidade e intensidade extremas; não identifica a causa.", "fulminante", "rápida e grave"),
    ("neonatal", "Neonatal refere-se aos [[primeiros 28 dias]] após o nascimento.", "Neo- significa novo; natal relaciona-se ao nascimento. O período neonatal possui limite clínico convencional de 28 dias.", "neonatal", "primeiros 28 dias"),
]: curate(name, "contrast" if "×" in canonical else "morpheme_in_context", "semiologia", body, extra, canonical, meaning, SRC_SEMI)

# Fisiologia e bioquímica: famílias que ajudam a ler processos novos.
PHYS = [
    ("absorcao-adsorcao", "Absorção leva algo [[para dentro]]; adsorção o prende à [[superfície]].", "A letra d ajuda: adsorver é aderir à superfície; absorver é incorporar ao volume.", "absorção × adsorção"),
    ("secrecao-excrecao", "Secreção [[libera produto]] funcional; excreção elimina [[resíduo]].", "Insulina é secretada para agir; ureia é excretada por ser produto de descarte.", "secreção × excreção"),
    ("filtracao-ultrafiltracao", "Filtração separa por [[barreira]]; ultrafiltração usa [[pressão]].", "No glomérulo, pressão força água e pequenos solutos através da barreira de filtração.", "filtração × ultrafiltração"),
    ("difusao-facilitada", "Difusão simples atravessa a [[membrana]]; facilitada requer [[proteína transportadora]].", "Ambas seguem o gradiente e não consomem ATP diretamente; muda a necessidade de proteína.", "difusão simples × facilitada"),
    ("osmose", "Osmose é o movimento de [[água]] através de membrana semipermeável.", "A água desloca-se em resposta à diferença de concentração efetiva de solutos não permeantes.", "osmose"),
    ("transporte-ativo-passivo", "Transporte ativo requer [[energia]]; passivo segue o [[gradiente]].", "Ativo pode mover contra o gradiente; passivo não usa energia metabólica diretamente.", "transporte ativo × passivo"),
    ("endocitose-exocitose", "Endocitose traz material [[para dentro]]; exocitose envia [[para fora]].", "Ambas usam vesículas: a membrana invagina na endocitose e funde-se na exocitose.", "endocitose × exocitose"),
    ("fagocitose-pinocitose", "Fagocitose engloba [[partículas]]; pinocitose incorpora [[líquido]].", "Fago- alude a comer; pino- a beber. Ambas são formas de endocitose.", "fagocitose × pinocitose"),
    ("transcitose", "Transcitose transporta material [[através da célula]].", "Combina endocitose em uma face, tráfego vesicular e exocitose na face oposta.", "transcitose"),
    ("ventilacao-perfusao", "Ventilação movimenta [[ar]]; perfusão movimenta [[sangue]].", "A troca gasosa eficiente exige correspondência entre alvéolos ventilados e capilares perfundidos.", "ventilação × perfusão"),
    ("des-re-hiperpolarizacao", "Despolarização reduz a [[polaridade]]; repolarização a [[restaura]]; hiperpolarização a [[aumenta]].", "Os termos descrevem mudança do potencial de membrana, não necessariamente excitação ou inibição por si só.", "despolarização × repolarização × hiperpolarização"),
    ("oxidacao-reducao", "Oxidação perde [[elétrons]]; redução os [[ganha]].", "O agente oxidado doa elétrons; o reduzido os recebe. As reações sempre ocorrem acopladas.", "oxidação × redução"),
    ("fosforilacao-desfosforilacao", "Fosforilação adiciona [[fosfato]]; desfosforilação o [[remove]].", "Quinases geralmente adicionam fosfato; fosfatases o retiram, alterando atividade ou localização proteica.", "fosforilação × desfosforilação"),
    ("carboxilacao-descarboxilacao", "Carboxilação adiciona [[carboxila]]; descarboxilação libera [[dióxido de carbono]].", "O prefixo des- marca retirada; a consequência química depende do substrato.", "carboxilação × descarboxilação"),
    ("transaminacao-desaminacao", "Transaminação transfere [[grupo amino]]; desaminação o [[remove]].", "Transaminases movem nitrogênio entre moléculas; desaminação pode liberar amônia.", "transaminação × desaminação"),
    ("glicolise-gliconeogenese", "Glicólise [[degrada glicose]]; gliconeogênese [[forma glicose]].", "Glico- indica açúcar; lise, quebra; neo-gênese, nova formação a partir de precursores.", "glicólise × gliconeogênese"),
    ("glicogenese-glicogenolise", "Glicogênese [[forma glicogênio]]; glicogenólise o [[degrada]].", "Não confundir glicogênio, reserva polimérica, com glicose, monossacarídeo circulante.", "glicogênese × glicogenólise"),
    ("lipogenese-lipolise", "Lipogênese [[forma lipídios]]; lipólise os [[degrada]].", "Lipo- indica gordura; -gênese forma; -lise quebra. O contexto define quais lipídios e vias.", "lipogênese × lipólise"),
    ("cetogenese-cetolise", "Cetogênese [[forma cetonas]]; cetólise as [[utiliza]].", "O fígado produz corpos cetônicos; tecidos extra-hepáticos podem oxidá-los como combustível.", "cetogênese × cetólise"),
    ("homeostase-alostase", "Homeostase mantém [[estabilidade]]; alostase alcança estabilidade pela [[mudança]].", "Homeostase defende faixas internas; alostase ajusta respostas e, às vezes, os pontos de operação.", "homeostase × alostase"),
    ("angiogenese-vasculogenese", "Angiogênese brota de [[vasos existentes]]; vasculogênese forma vasos [[de precursores]].", "Angioblastos participam da vasculogênese embrionária; angiogênese remodela redes já formadas.", "angiogênese × vasculogênese"),
    ("hematopoiese", "Hematopoiese é a [[produção sanguínea]].", "Hemat/o (sangue) + -poiese (produção) = formação contínua das células do sangue, principalmente na medula óssea.", "hematopoiese"),
]
for name, body, extra, canonical in PHYS:
    curate(name, "contrast" if "×" in canonical else "term_decomposition", "fisiologia", body, extra, canonical, canonical, SRC_PHYS, unfamiliar=True)

# Patologia: distinções que a forma sozinha não resolve completamente.
PATH = [
    ("inflamacao-infeccao", "Inflamação é uma [[resposta tecidual]]; infecção é [[invasão microbiana]].", "Infecção pode causar inflamação, mas trauma, autoimunidade e cristais também inflamam sem microrganismos.", "inflamação × infecção"),
    ("colonizacao-infeccao", "Colonização tem microrganismos sem [[dano invasivo]]; infecção envolve [[invasão ou resposta]].", "Uma cultura positiva pode representar colonização; sintomas e contexto ajudam a identificar infecção.", "colonização × infecção"),
    ("exsudato-transudato", "Exsudato decorre de [[inflamação]]; transudato, de desequilíbrio [[hidrostático-oncótico]].", "Exsudato costuma ter mais proteínas e células; transudato é relativamente pobre em ambos.", "exsudato × transudato"),
    ("trombo-embolo", "Trombo se forma [[localmente]]; êmbolo [[viaja]].", "O êmbolo pode ser fragmento de trombo, gordura, ar ou outro material intravascular.", "trombo × êmbolo"),
    ("isquemia-infarto", "Isquemia reduz a [[perfusão]]; infarto produz [[necrose]].", "Isquemia pode ser reversível; infarto implica morte tecidual por isquemia prolongada.", "isquemia × infarto"),
    ("obstrucao-oclusao", "Obstrução dificulta o [[fluxo]]; oclusão o [[fecha]].", "Obstrução pode ser parcial; oclusão sugere fechamento completo, embora o uso clínico varie.", "obstrução × oclusão"),
    ("estenose-atresia", "Estenose é [[estreitamento]]; atresia, ausência ou [[fechamento congênito]].", "Na atresia, a luz pode não ter se formado; na estenose, existe, mas está reduzida.", "estenose × atresia"),
    ("erosao-ulcera", "Erosão é perda [[superficial]]; úlcera alcança plano [[mais profundo]].", "Na mucosa gastrointestinal, úlcera ultrapassa a muscular da mucosa; erosão não.", "erosão × úlcera"),
    ("abscesso-fistula", "Abscesso é coleção de [[pus]]; fístula é trajeto [[anormal]].", "Um abscesso pode drenar e formar fístula, mas os conceitos não são sinônimos.", "abscesso × fístula"),
    ("hiperplasia-neoplasia", "Hiperplasia é crescimento [[regulado]]; neoplasia, proliferação [[autônoma]].", "Ambas aumentam células; a diferença central é dependência ou autonomia dos sinais de crescimento.", "hiperplasia × neoplasia"),
    ("metaplasia-displasia-anaplasia", "Metaplasia troca o [[tipo maduro]]; displasia altera a [[organização]]; anaplasia perde [[diferenciação]].", "A sequência não é obrigatória. Os termos descrevem alterações diferentes, embora possam coexistir na carcinogênese.", "metaplasia × displasia × anaplasia"),
    ("apoptose-necrose", "Apoptose é morte [[programada]]; necrose resulta de [[lesão]].", "Apoptose preserva membranas por mais tempo; necrose frequentemente libera conteúdo e provoca inflamação.", "apoptose × necrose"),
    ("metastase", "Metástase é disseminação para um local [[não contíguo]].", "Meta- alude a mudança; clinicamente, células tumorais formam foco distante descontínuo do tumor primário.", "metástase"),
]
for name, body, extra, canonical in PATH:
    curate(name, "contrast" if "×" in canonical else "exception", "patologia", body, extra, canonical, canonical, SRC_PATH, unfamiliar=True)

# Semiologia: precisão na descrição de sintomas e sinais.
SEMI = [
    ("disfagia-odinofagia", "Disfagia é [[dificuldade]] ao engolir; odinofagia é [[dor]].", "O paciente pode ter uma, ambas ou nenhuma; a pergunta clínica deve separar dificuldade mecânica de dor.", "disfagia × odinofagia"),
    ("afasia-disartria", "Afasia altera a [[linguagem]]; disartria, a [[articulação motora]].", "Na disartria, a formulação linguística pode estar preservada, mas a fala fica pouco inteligível.", "afasia × disartria"),
    ("disfasia-disartria", "Disfasia altera a [[linguagem]]; disartria, a [[execução motora]].", "Disfasia é usada para comprometimento de linguagem; disartria afeta articulação, voz e prosódia com linguagem formulada.", "disfasia × disartria"),
    ("parestesia-disestesia", "Parestesia é sensação [[anormal]]; disestesia é sensação anormal [[desagradável]].", "Formigamento indolor pode ser parestesia; ardor ou choque incômodo caracteriza disestesia.", "parestesia × disestesia"),
    ("nausea-vomito-regurgitacao", "Náusea é vontade de [[vomitar]]; vômito é expulsão [[ativa]]; regurgitação, retorno [[passivo]].", "Regurgitação não exige contrações abdominais vigorosas; vômito envolve reflexo motor coordenado.", "náusea × vômito × regurgitação"),
    ("ortopneia-platipneia", "Ortopneia piora ao [[deitar]]; platipneia piora na [[posição ereta]].", "Ortopneia costuma aliviar sentado; platipneia, incomum, melhora em decúbito.", "ortopneia × platipneia"),
    ("dispneia-ortopneia", "Dispneia é [[desconforto respiratório]]; ortopneia é dispneia ao [[deitar]].", "Dispneia é termo amplo; ortopneia acrescenta uma posição desencadeante e costuma melhorar sentado.", "dispneia × ortopneia"),
    ("trepopneia", "Trepopneia varia conforme o [[decúbito lateral]].", "É dispneia que piora em um lado e melhora no outro; trepo- alude a virar.", "trepopneia"),
    ("anosmia-hiposmia-hiperosmia", "Anosmia é [[ausência]] de olfato; hiposmia, [[redução]]; hiperosmia, [[aumento]].", "-osmia refere-se ao olfato; os prefixos graduam ausência, redução ou aumento.", "anosmia × hiposmia × hiperosmia"),
    ("anorexia-hiporexia-hiperorexia", "Anorexia é [[ausência]] de apetite; hiporexia, [[redução]]; hiperorexia, [[aumento]].", "-orexia significa apetite; anorexia como sintoma não é sinônimo de anorexia nervosa.", "anorexia × hiporexia × hiperorexia"),
    ("hematemese-hemoptise", "Hematêmese elimina sangue pelo [[vômito]]; hemoptise, pela [[tosse]].", "A via de exteriorização orienta a origem: digestiva alta na hematêmese, respiratória na hemoptise.", "hematêmese × hemoptise"),
    ("melena-hematoquezia", "Melena é fezes [[negras]]; hematoquezia é sangue [[vermelho vivo]].", "A aparência sugere tempo de trânsito e origem, mas sangramento alto volumoso também pode causar hematoquezia.", "melena × hematoquezia"),
]
for name, body, extra, canonical in SEMI:
    curate(name, "contrast" if "×" in canonical else "term_decomposition", "semiologia", body, extra, canonical, canonical, SRC_SEMI, unfamiliar=True)

# Farmacologia: termos cuja troca prejudica o raciocínio.
PHARM = [
    ("farmacocinetica-dinamica", "Farmacocinética descreve o que o [[corpo faz]] ao fármaco; farmacodinâmica, o que o [[fármaco faz]].", "Cinética cobre ADME; dinâmica cobre alvos, mecanismos e relação concentração-efeito.", "farmacocinética × farmacodinâmica"),
    ("potencia-eficacia", "Potência depende da [[dose necessária]]; eficácia, do [[efeito máximo]].", "Um fármaco mais potente precisa de menor dose, mas não necessariamente produz efeito máximo maior.", "potência × eficácia"),
    ("afinidade-eficacia", "Afinidade mede a [[ligação]] ao receptor; eficácia mede a capacidade de [[ativá-lo]].", "Um antagonista pode ter alta afinidade e eficácia intrínseca nula.", "afinidade × eficácia"),
    ("agonistas", "Agonista total alcança efeito [[máximo]]; parcial, [[submáximo]]; inverso reduz atividade [[constitutiva]].", "O agonista parcial pode antagonizar o total ao competir pelos mesmos receptores.", "agonista total × parcial × inverso"),
    ("antagonistas", "Antagonista competitivo desloca a curva [[à direita]]; não competitivo reduz o [[efeito máximo]].", "Mais agonista pode superar competição reversível; não restaura Emax diante de antagonismo não competitivo efetivo.", "antagonista competitivo × não competitivo"),
    ("tolerancia-taquifilaxia", "Tolerância surge [[gradualmente]]; taquifilaxia, [[rapidamente]].", "Ambas reduzem resposta com repetição; a diferença útil é a velocidade de instalação.", "tolerância × taquifilaxia"),
    ("dependencia-abstinencia", "Dependência é [[adaptação]] ao uso; abstinência é o quadro após [[interrupção]].", "Dependência fisiológica não equivale necessariamente a transtorno por uso de substância.", "dependência × abstinência"),
    ("efeito-adverso-toxicidade", "Efeito adverso ocorre em uso [[terapêutico]]; toxicidade implica efeito [[nocivo excessivo]].", "A fronteira depende de dose, suscetibilidade e contexto; efeito adverso não exige superdose.", "efeito adverso × toxicidade"),
    ("efeito-toxicidade-contraindicacao", "Efeito adverso é uma [[resposta nociva]]; toxicidade é dano por [[exposição]]; contraindicação desaconselha o [[uso]].", "Os dois primeiros são efeitos observados; contraindicação é uma condição prévia que muda a decisão terapêutica.", "efeito adverso × toxicidade × contraindicação"),
    ("contraindicacao", "Contraindicação é condição que torna o uso [[desaconselhado]].", "Pode ser absoluta ou relativa; descreve decisão de uso, não um efeito produzido pelo fármaco.", "contraindicação"),
    ("clearance-meia-vida", "Clearance expressa volume depurado por [[tempo]]; meia-vida, tempo para cair à [[metade]].", "A meia-vida depende do volume de distribuição e do clearance; não são medidas equivalentes.", "clearance × meia-vida"),
]
for name, body, extra, canonical in PHARM:
    curate(name, "contrast" if "×" in canonical else "term_decomposition", "farmacologia", body, extra, canonical, canonical, SRC_PHARM, unfamiliar=True)

# Nomenclatura anatômica latina: uma camada de leitura, não uma lista enciclopédica.
# Seleciona substantivos, genitivos e adjetivos que se repetem em atlas, laudos e dissecção.
LATIN_ANATOMY = [
    ("latim-substantivo-adjetivo", "Na Terminologia Anatômica, o substantivo nomeia a [[estrutura]]; o adjetivo a especifica.", "Em foramen ovale, foramen é abertura e ovale descreve a forma. A ordem evita traduzir o termo ao acaso.", "substantivo × adjetivo", "estrutura"),
    ("latim-genitivo-singular", "Em musculus biceps brachii, brachii significa “do [[braço]]”.", "Formas em -i frequentemente equivalem a “do/da”. Leia primeiro o núcleo: músculo bíceps.", "brachii", "braço"),
    ("latim-genitivo-plural", "Em musculus flexor digitorum, digitorum significa “dos [[dedos]]”.", "A terminação -orum frequentemente equivale a “dos”. Profundus acrescenta que o flexor é profundo.", "digitorum", "dedos"),
    ("latim-musculus", "No latim anatômico, musculus designa um [[músculo]].", "Em atlas, M. costuma abreviar musculus. O termo seguinte especifica forma, função ou região.", "musculus", "músculo"),
    ("latim-nervus", "No latim anatômico, nervus designa um [[nervo]].", "N. é abreviação frequente. Em nervus vagus, vagus é o adjetivo que nomeia esse nervo.", "nervus", "nervo"),
    ("latim-arteria", "No latim anatômico, arteria designa uma [[artéria]].", "A. costuma abreviar arteria. Em arteria carotis communis, os dois termos seguintes especificam qual artéria.", "arteria", "artéria"),
    ("latim-vena", "No latim anatômico, vena designa uma [[veia]].", "V. costuma abreviar vena. Em vena cava inferior, cava e inferior distinguem a veia.", "vena", "veia"),
    ("latim-ligamentum", "No latim anatômico, ligamentum designa um [[ligamento]].", "Ligamentum cruciatum anterius é o ligamento cruzado anterior; os adjetivos refinam a identificação.", "ligamentum", "ligamento"),
    ("latim-foramen", "No latim anatômico, foramen designa uma [[abertura]].", "Foramen ovale é abertura oval; foramen magnum é abertura grande. O nome não define sozinho o conteúdo que passa.", "foramen", "abertura"),
    ("latim-sulcus", "No latim anatômico, sulcus designa um [[sulco]].", "Sulcus é uma depressão linear, como sulcus interventricularis. Não confundir com fossa, geralmente mais ampla.", "sulcus", "sulco"),
    ("latim-fossa", "No latim anatômico, fossa designa uma [[depressão]].", "Fossa costuma ser uma escavação mais ampla que sulcus. Exemplo: fossa cubital.", "fossa", "depressão"),
    ("latim-facies", "No latim anatômico, facies designa uma [[superfície]].", "Facies articularis é a superfície que participa de articulação; facies não significa necessariamente “rosto”.", "facies", "superfície"),
    ("latim-ramus", "No latim anatômico, ramus designa um [[ramo]].", "Ramus pode ser ramo de nervo, artéria, veia ou osso. O genitivo ou adjetivo identifica sua origem.", "ramus", "ramo"),
    ("latim-caput", "No latim anatômico, caput designa uma [[cabeça]].", "Caput costuma nomear extremidade arredondada de osso ou porção de músculo, não apenas a cabeça corporal.", "caput", "cabeça"),
    ("latim-corpus", "No latim anatômico, corpus designa um [[corpo]].", "Corpus pode indicar a porção principal de um órgão ou estrutura, como corpus vertebrae.", "corpus", "corpo"),
    ("latim-renis", "Em hilum renis, renis significa “do [[rim]]”.", "Renis é genitivo de ren. A forma aparece em expressões anatômicas; renal é o adjetivo português correspondente.", "renis", "rim"),
    ("latim-cordis", "Em apex cordis, cordis significa “do [[coração]]”.", "Cordis é genitivo de cor. Reconhecê-lo liga ápice, base e faces à anatomia cardíaca.", "cordis", "coração"),
    ("latim-pulmonis", "Em hilum pulmonis, pulmonis significa “do [[pulmão]]”.", "Pulmonis é genitivo de pulmo. Ajuda a ler relações anatômicas sem confundir com pneum/o, de origem grega.", "pulmonis", "pulmão"),
    ("latim-cerebri", "Em arteria cerebri media, cerebri significa “do [[cérebro]]”.", "Cerebri é genitivo de cerebrum. A forma aparece em artérias, sulcos e superfícies cerebrais.", "cerebri", "cérebro"),
    ("latim-femoris", "Em arteria profunda femoris, femoris significa “da [[coxa]]”.", "Femoris é genitivo de femur. A expressão nomeia a artéria profunda da coxa, não uma artéria dentro do fêmur.", "femoris", "coxa"),
    ("latim-cava", "Em vena cava, cava significa [[oca]].", "Cava concorda com vena. A expressão descreve grande veia de parede relativamente colapsável, não uma cavidade isolada.", "cava", "oca"),
    ("latim-profundus", "Em arteria profunda femoris, profunda significa [[profunda]].", "O adjetivo concorda com arteria. Em outros substantivos, a terminação muda, mas a ideia espacial permanece.", "profunda", "profunda"),
    ("latim-anterius", "Em ligamentum cruciatum anterius, anterius indica posição [[anterior]].", "Anterius concorda com ligamentum. O par posterius aparece no ligamento cruzado posterior.", "anterius", "anterior"),
    ("latim-medialis", "Em malleolus medialis, medialis indica posição [[medial]].", "Medialis aponta em direção ao plano mediano; lateralis aponta para longe dele.", "medialis", "medial"),
    ("latim-dexter", "Em ren dexter, dexter significa [[direito]].", "Dexter e sinister distinguem lado direito e esquerdo. A terminação pode variar com o substantivo.", "dexter", "direito"),
    ("latim-major", "Em pectoralis major, major significa [[maior]].", "Major contrasta com minor. O par costuma separar estruturas homônimas por tamanho relativo, não por importância.", "major", "maior"),
    ("latim-longus", "Em musculus fibularis longus, longus significa [[longo]].", "Longus contrasta com brevis. O adjetivo descreve o comprimento relativo da estrutura.", "longus", "longo"),
]
for name, body, extra, canonical, meaning in LATIN_ANATOMY:
    curate(name, "morpheme_in_context", "latim_anatomico", body, extra, canonical, meaning, SRC_TA, unfamiliar=False)

# Poucas duplas greco-latinas produtivas, preservadas deliberadamente.
for name, body, extra, canonical in [
    ("oto-auro", "Ot/o é a forma [[grega]] para orelha; aur/o, a [[latina]].", "Otite usa a forma grega; auricular conserva a forma latina.", "ot/o × aur/o"),
    ("pneumo-pulmono", "Pneum/o é a forma [[grega]] para pulmão; pulmon/o, a [[latina]].", "Pneumonia usa a forma grega; pulmonar conserva a latina. Pneum/o também pode indicar ar.", "pneum/o × pulmon/o"),
    ("histero-utero", "Hister/o é a forma [[grega]] para útero; uter/o, a [[latina]].", "Histerectomia usa a forma grega; uterino conserva a latina.", "hister/o × uter/o"),
    ("orquo-testiculo", "Orqu/o é a forma [[grega]] para testículo; testicul/o, a [[latina]].", "Orquite usa a forma grega; testicular conserva a latina.", "orqu/o × testicul/o"),
    ("masto-mamo", "Mast/o é a forma [[grega]] para mama; mam/o, a [[latina]].", "Mastite usa a forma grega; mamário conserva a latina.", "mast/o × mam/o"),
    ("encefalo-cerebro", "Encefal/o é a forma [[grega]] para encéfalo; cerebr/o, a [[latina]].", "Encefalite usa a forma grega; cerebral conserva a latina.", "encefal/o × cerebr/o"),
]: curate(name, "contrast", "duplas", body, extra, canonical, canonical, SRC_TERM, unfamiliar=True)


def card_from_curated(spec: dict) -> dict:
    uid = "etim-v3-cur-" + slug(spec["name"])
    return {
        "uid": uid, "deck": DECKS[spec["discipline"]], "kind": spec["kind"],
        "term_en": "", "term_ptbr": spec["canonical"], "canonical_form": spec["canonical"],
        "origin_language": "Not_applicable", "morpheme_breakdown": spec["canonical"],
        "literal_gloss": spec["meaning"], "clinical_meaning": spec["meaning"],
        "inference_limit": "A forma orienta a leitura; o contexto clínico define o uso preciso.",
        "variants": [], "text": "<b>Etimologia.</b> " + cloze(spec["body"]),
        "extra": spec["extra"], "source_etymology": [spec["source"]],
        "source_medical": [spec["source"]], "license": "Uso educacional; consultar fonte indicada",
        "confidence": "high", "number_of_cards": 1,
        "tags": ["etim_full_v3", f"etim_uid::{uid}", f"terminologia::card::{spec['kind']}",
                 f"terminologia::disciplina::{spec['discipline']}", "terminologia::status::aprovado"] +
                (["terminologia::origem::latim"] if spec["discipline"] == "latim_anatomico" else []) +
                (["terminologia::didatica::termo_novo"] if spec["unfamiliar"] else []),
        "status": "approved",
    }


SYSTEM_DECK = {
    "celula_tecidos_embriologia": "01_Celula_tecidos_e_embriologia",
    "cardiovascular_hematologico": "02_Cardiovascular_e_hematologico",
    "respiratorio": "03_Respiratorio", "gastro_hepatobiliar": "04_Gastrointestinal_e_hepatobiliar",
    "renal_urinario": "05_Renal_e_urinario", "nervoso_sentidos": "06_Nervoso_e_sentidos",
    "musculoesqueletico": "07_Musculoesqueletico", "endocrino_metabolico": "08_Endocrino_e_metabolico",
    "reprodutor_obstetricia": "09_Reprodutor_e_obstetricia", "pele_imune_micro": "10_Pele_imune_e_linfatico",
}


def compact_answer(s: str) -> str:
    tokens = re.findall(r"[\wÀ-ÿ/-]+", s)
    if len(tokens) <= 3:
        return " ".join(tokens)
    stop = {"de", "da", "do", "das", "dos", "ou", "e", "a", "o", "em", "para"}
    reduced = [t for t in tokens if t.casefold() not in stop]
    return " ".join((reduced or tokens)[:3])


def render_answer_phrase(s: str) -> str:
    """Mantém a glosa natural e fecha apenas 1–3 palavras finais."""
    tokens = re.findall(r"[\wÀ-ÿ/₂-]+", s)
    if len(tokens) <= 3:
        return f"[[{' '.join(tokens)}]]"
    take = 3 if tokens[-2].casefold() in {"e", "ou", "do", "da", "de"} else 2
    take = min(3, take)
    return " ".join(tokens[:-take]) + " [[" + " ".join(tokens[-take:]) + "]]"


AUTO_CONTRAST_EXTRAS = {
    norm("aferente × eferente"): "Aferente leva informação sensorial ao SNC; eferente conduz comandos motores ou autonômicos para a periferia.",
    norm("hipóxia × hipoxemia"): "Hipoxemia é pouco oxigênio arterial; hipóxia é oferta ou utilização insuficiente no tecido. Uma não implica automaticamente a outra.",
    norm("analgesia × anestesia"): "Analgesia reduz dor; anestesia reduz sensibilidade de modo mais amplo e pode também alterar consciência ou movimento.",
    norm("oligúria × anúria"): "Oligúria é débito urinário reduzido; anúria é produção praticamente ausente. Os limites clínicos dependem de tempo e peso.",
    norm("proteinúria × albuminúria"): "Albumina é uma proteína: toda albuminúria é proteinúria, mas outras proteínas urinárias podem predominar.",
    norm("mosaico × quimera"): "Mosaicismo surge de um zigoto com linhagens divergentes; quimerismo reúne células derivadas de zigotos diferentes.",
    norm("penetrância × expressividade"): "Penetrância pergunta se o fenótipo aparece; expressividade pergunta quanto ou de que forma ele aparece.",
    norm("sinal × sintoma"): "Sinal é observado ou medido pelo examinador; sintoma é experiência relatada pelo paciente.",
    norm("bacteremia × sepse"): "Bacteremia é bactéria no sangue; sepse é disfunção orgânica por resposta desregulada à infecção e pode ocorrer sem bacteremia detectada.",
}

PT_FORM = {
    "leuk/o": "leuc/o", "pyel/o": "piel/o", "oophor/o": "oofor/o",
    "hypoderm/o": "hipoderm/o", "sphygm/o": "esfigm/o",
}


def infer_example_extra(term: str, meaning: str, example: str, typ: str) -> str:
    if not example:
        return f"A forma fornece a pista “{meaning}”. Leia o termo completo antes de inferir processo, localização ou diagnóstico."
    suffixes = [
        ("ectomia", "remoção cirúrgica"), ("tomia", "incisão"), ("stomia", "abertura criada"),
        ("ite", "inflamação"), ("ose", "condição"), ("patia", "doença"),
        ("megalia", "aumento"), ("algia", "dor"), ("penia", "redução numérica"),
        ("scopia", "visualização"), ("grafia", "registro"), ("metria", "medição"),
    ]
    for ending, gloss in suffixes:
        if example.casefold().endswith(ending):
            if typ == "sufixo":
                return f"Exemplo: {example}. Nesse termo, {term} acrescenta “{gloss}”; a base informa a estrutura ou processo envolvido."
            if typ == "prefixo":
                return f"Exemplo: {example}. {term} modifica a base com a ideia de “{meaning}”; a terminação ajuda a definir o processo."
            return f"Exemplo: {example}. A raiz fornece “{meaning}” e -{ending} acrescenta “{gloss}”; juntos orientam o sentido do termo."
    if typ == "raiz":
        return f"Exemplo: {example}. A raiz identifica “{meaning}”; as demais partes informam processo, condição ou relação anatômica."
    return f"Exemplo: {example}. Nesse termo, {term} acrescenta a ideia de “{meaning}”; o restante especifica o uso médico."


def auto_card(row: dict) -> dict | None:
    term = str(row["entrada_canonica"]).strip(); meaning = str(row["significado_nuclear"]).strip()
    typ = str(row["tipo_morfologico"]); uid = "etim-v3-auto-" + slug(row["id"] or term)
    if typ in {"fundamento", "foundation"}: return None
    if typ in {"contraste", "contrast"} or "×" in term:
        members = [x.strip() for x in term.split("×")]
        answers = [x.strip() for x in meaning.split("×")]
        if not 2 <= len(members) <= 3 or len(members) != len(answers): return None
        # As duplas greco-latinas são uma amostra curada pequena; não gerar o
        # catálogo inteiro automaticamente.
        if {norm(x) for x in answers} == {norm("grego"), norm("latim")}:
            return None
        if all(norm(m) == norm(a) for m, a in zip(members, answers)): return None
        rendered = [render_answer_phrase(x) for x in answers]
        body = "; ".join(f"{m}: {a}" for m, a in zip(members, rendered)) + "."
        extra = str(row.get("exemplos", "")).strip() or AUTO_CONTRAST_EXTRAS.get(
            norm(term), f"O contraste decisivo é: {meaning}. Compare os termos no mesmo eixo antes de aplicá-los clinicamente.")
        discipline = "contrastes"
        kind = "contrast"
    elif typ in {"transferencia", "transfer"} or row["tipo_de_entrada"] == "termo":
        body = f"Pelos componentes, {term} sugere {render_answer_phrase(meaning)}."
        breakdown = TRANSFER_BREAKDOWNS.get(norm(term), term)
        extra = f"{breakdown} = {meaning}. A decomposição prevê a classe de sentido; o contexto confirma o uso clínico."
        discipline = "transferencia"; kind = "transfer"
    else:
        rendered = render_answer_phrase(meaning)
        if typ == "prefixo": body = f"O prefixo {term} acrescenta a ideia de {rendered}."
        elif typ == "sufixo": body = f"O sufixo {term} acrescenta a ideia de {rendered}."
        else: body = f"A forma combinatória {term} indica {rendered}."
        extra = infer_example_extra(term, meaning, str(row.get("exemplos", "")).strip(), typ)
        if term in PT_FORM:
            extra = f"Em português, {term} costuma aparecer como {PT_FORM[term]}. " + extra
        system = str(row.get("sistema", "")).split(";")[0]
        if typ == "prefixo": discipline = "prefixos"
        elif typ == "sufixo": discipline = "sufixos"
        else: discipline = "anatomia"
        kind = "morpheme_in_context"
    if discipline == "anatomia":
        sys = str(row.get("sistema", "")).split(";")[0]
        deck = ("NEBLI::Etimologia::04_Raizes_por_sistema::" + SYSTEM_DECK[sys]) if sys in SYSTEM_DECK else DECKS["anatomia"]
    else: deck = DECKS[discipline]
    source = str(row.get("fonte", "")).strip() or SRC_TERM
    unfamiliar = typ == "raiz" and (str(row.get("risco_de_confusao", 0)) == "2" or str(row.get("nivel", "")) == "extensao")
    return {
        "uid": uid, "deck": deck, "kind": kind, "term_en": str(row.get("equivalente_ingles", "")),
        "term_ptbr": term, "canonical_form": term, "origin_language": "Not_applicable",
        "morpheme_breakdown": term, "literal_gloss": meaning,
        "clinical_meaning": str(row.get("definicao_medica", "")) or meaning,
        "inference_limit": str(row.get("limites_etimologicos", "")) or "A glosa não substitui a definição clínica.",
        "variants": [], "text": "<b>Etimologia.</b> " + cloze(body), "extra": extra,
        "source_etymology": [source], "source_medical": [source], "license": "Conforme fonte do léxico mestre",
        "confidence": "high", "number_of_cards": 1,
        "tags": ["etim_full_v3", f"etim_uid::{uid}", f"terminologia::card::{kind}",
                 f"terminologia::nivel::{row.get('nivel','nucleo')}", "terminologia::status::aprovado"] +
                (["terminologia::didatica::termo_novo"] if unfamiliar else []),
        "status": "approved",
    }


def sync_curated_lexicon(rows: list[dict]) -> int:
    for row in rows:
        if row.get("exemplos") == "anorretaI": row["exemplos"] = "anorretal"
        if row.get("entrada_canonica") == "quilotorax": row["entrada_canonica"] = "quilotórax"
        if row.get("termos_de_inferencia") == "quilotorax": row["termos_de_inferencia"] = "quilotórax"
    fields = list(rows[0]); present = {norm(r["entrada_canonica"]): r for r in rows}; added = 0
    curriculum_rows = []
    for spec in CURATED:
        key = norm(spec["canonical"])
        if key in present: continue
        row = {f: "" for f in fields}
        row.update({"id": "etim-v3-cur-" + slug(spec["name"]), "entrada_canonica": spec["canonical"],
                    "tipo_de_entrada": "família" if "×" in spec["canonical"] else "conceito",
                    "tipo_morfologico": spec["kind"], "origem": "greco-latina ou terminologia médica moderna",
                    "significado_nuclear": spec["meaning"], "significado_literal": spec["meaning"],
                    "definicao_medica": spec["extra"], "categoria_semantica": spec["discipline"],
                    "sistema": "transversal", "disciplinas": spec["discipline"],
                    "produtividade": 2, "frequencia_curricular": 2, "transferibilidade": 2,
                    "risco_de_confusao": 2, "prioridade": 18, "nivel": "nucleo",
                    "exemplos": spec["extra"], "fonte": spec["source"], "confianca": "alta",
                    "status_validacao": "curadoria_v3", "destino_pedagogico": "card_proprio",
                    "nota_que_cobre": "etim-v3-cur-" + slug(spec["name"]), "gera_card": "sim",
                    "direcao_do_card": "reconhecimento", "numero_de_cards": 1,
                    "tags": f"terminologia::disciplina::{spec['discipline']}",
                    "observacoes": "Expansão curricular v3 orientada por lacuna, confusão e baixa exposição."})
        rows.append(row); present[key] = row; curriculum_rows.append(row); added += 1
    expansion_rows = [r for r in rows if str(r.get("id", "")).startswith("etim-v3-cur-")]
    CURRICULUM.write_text(json.dumps(expansion_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    LEXICON_JSON.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    with LEXICON_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(rows)
    return added


def validate(cards: list[dict]) -> tuple[list[str], dict]:
    errors = []; seen_uid = set(); seen_semantic = set(); lengths = []
    for c in cards:
        uid = c["uid"]
        if uid in seen_uid: errors.append(f"{uid}: UID duplicado")
        seen_uid.add(uid)
        if not c["text"].startswith("<b>Etimologia.</b> "): errors.append(f"{uid}: tema ausente")
        raw = re.findall(r"\{\{c(\d+)::(.+?)\}\}", c["text"])
        bold = re.findall(r"<b>\{\{c(\d+)::(.+?)\}\}</b>", c["text"])
        if raw != bold: errors.append(f"{uid}: cloze fora do negrito")
        if not 1 <= len(raw) <= 3: errors.append(f"{uid}: {len(raw)} clozes; máximo 3")
        if any(n != "1" for n, _ in raw): errors.append(f"{uid}: somente c1 permitido")
        if any(wc(a) > 3 for _, a in raw): errors.append(f"{uid}: resposta cloze >3 palavras")
        if wc(c["text"]) > 25: errors.append(f"{uid}: Texto >25")
        if wc(c["extra"]) > 40: errors.append(f"{uid}: Extra >40")
        lengths.append(wc(c["extra"]))
        if not c["extra"].strip(): errors.append(f"{uid}: Extra vazio")
        if c["kind"] == "transfer" and not ("+" in c["extra"] and "=" in c["extra"]):
            errors.append(f"{uid}: transferência sem decomposição interpretada")
        if not c["source_etymology"] or not c["source_medical"]: errors.append(f"{uid}: fonte ausente")
        if c["confidence"] != "high": errors.append(f"{uid}: confiança não alta")
        key = (norm(c["canonical_form"]), c["kind"])
        if key in seen_semantic: errors.append(f"{uid}: duplicata semântica {key}")
        seen_semantic.add(key)
    stats = {"notes": len(cards), "anki_cards": len(cards),
             "max_clozes": max(len(re.findall(r"\{\{c\d+::", c["text"])) for c in cards),
             "max_text_words": max(wc(c["text"]) for c in cards),
             "max_extra_words": max(lengths),
             "extras_le_25_pct": round(100 * sum(x <= 25 for x in lengths) / len(lengths), 1),
             "kinds": dict(Counter(c["kind"] for c in cards)),
             "decks": dict(Counter(c["deck"] for c in cards))}
    if stats["extras_le_25_pct"] < 85: errors.append("menos de 85% dos Extras têm até 25 palavras")
    return errors, stats


def main() -> int:
    rows = json.loads(LEXICON_JSON.read_text(encoding="utf-8"))
    added = sync_curated_lexicon(rows)
    pilot = load_pilot()
    # Piloto aprovado vira parte do deck integral com UID e tag próprios preservados.
    for c in pilot:
        if c["kind"] == "foundation": c["deck"] = DECKS["fundamentos"]
        elif c["kind"] == "transfer": c["deck"] = DECKS["transferencia"]
        elif c["kind"] == "exception": c["deck"] = DECKS["armadilhas"]
        elif c["kind"] == "contrast":
            c["deck"] = DECKS["duplas"] if "polissemia-duplas" in " ".join(c["tags"]) else DECKS["contrastes"]
        else: c["deck"] = "NEBLI::Etimologia::04_Raizes_por_sistema::11_Transversal_e_formas"
        c["tags"] = [t for t in c["tags"] if t != "etim_pilot_pt2"] + ["etim_full_v3"]
        c["status"] = "approved"
    curated_cards = [card_from_curated(s) for s in CURATED]
    preferred = {(norm(c["canonical_form"]), c["kind"]) for c in pilot + curated_cards}
    preferred_canon = {norm(c["canonical_form"]) for c in pilot + curated_cards}
    covered_contrast_sets = []
    for existing in pilot + curated_cards:
        if existing["kind"] == "contrast" and "×" in existing["canonical_form"]:
            covered_contrast_sets.append({norm(x) for x in existing["canonical_form"].split("×")})
    auto = []
    for row in rows:
        c = auto_card(row)
        if not c: continue
        if norm(c["canonical_form"]) in preferred_canon:
            continue
        if c["kind"] == "contrast" and "×" in c["canonical_form"]:
            members = {norm(x) for x in c["canonical_form"].split("×")}
            if any(members <= covered for covered in covered_contrast_sets):
                continue
        key = (norm(c["canonical_form"]), c["kind"])
        if key in preferred: continue
        preferred.add(key); auto.append(c)
    cards = pilot + curated_cards + auto
    errors, stats = validate(cards)
    if errors:
        print("\n".join("ERRO " + x for x in errors[:200])); print(f"TOTAL ERROS {len(errors)}")
        return 1
    payload = {"version": "full-v3-2026-07-17", "approval_gate": "user_authorized_full_generation",
               "policy": {"clozes_max": 3, "extra_words_preferred": 25, "extra_words_max": 40,
                          "didactic_unknown_terms": True, "selected_greek_latin_pairs": True},
               "stats": stats, "cards": cards}
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Deck integral de etimologia v3", "", f"- Notas/cards: {len(cards)}", "- Status: aprovado para sincronização", ""]
    for i, c in enumerate(cards, 1):
        lines += [f"## {i:04d} — {c['uid']}", "", f"**Texto:** {c['text']}", "", f"**Extra:** {c['extra']}", "", f"**Deck:** `{c['deck']}`", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    VALIDATION.write_text("# Validação integral v3\n\n" + "\n".join(f"- {k}: {v}" for k, v in stats.items()) + "\n- Violações: 0\n", encoding="utf-8")
    COMPRESSION.write_text(
        "# Compressão integral v3\n\n" +
        f"- Léxico após expansão: {len(rows)} entradas\n- Expansões novas nesta execução: {added}\n"
        f"- Cards do piloto preservados: {len(pilot)}\n- Cards curriculares curados: {len(curated_cards)}\n"
        f"- Cards derivados do léxico: {len(auto)}\n- Total aprovado: {len(cards)}\n"
        "- Fundamentos antigos redundantes: omitidos em favor do piloto aprovado.\n"
        "- Duplicatas de conceito: removidas por chave canônica + tipo.\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2)); print(f"lexicon +{added}; cards {len(cards)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
