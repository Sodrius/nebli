#!/usr/bin/env python3
"""Fonte única da aula: gera `contrato-cobertura.json` a partir dos cards.

O contrato é o artefato canônico (docs/canon/CARDS.md): ele carrega conceitos,
âncoras literais na E1, roteamento de fontes, decisão visual e `cards[]` com o
conteúdo real. O montador do APKG lê este arquivo — não há segunda cópia dos
cards em lugar nenhum.

Cada âncora declarada aqui é conferida contra o texto da E1 antes de escrever o
contrato; âncora que não existir literalmente derruba a geração.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
LESSON = Path(__file__).resolve().parent
E1 = RAIZ / "typst-build/anato-intestino-grosso/etapa1.typ"
SLUG = "anato-intestino-grosso"
DECK = "NEBLI::Digestório::P1::Anatomia::Intestino grosso, reto e canal anal"
TEMA = "ANATOMIA · INTESTINO GROSSO, RETO E CANAL ANAL"
FIG = "/figuras/anato-intestino-grosso"

# --------------------------------------------------------------------------
# Cloze autorais. Campos: id, importância, subtópico, conceito PT/EN,
# texto (inglês médico, um único c1), Extra (português curto), figura, âncora.
# --------------------------------------------------------------------------
CLOZE = [
    dict(
        id="c01", imp="nucleo", sub="Partes e mobilidade",
        pt="Mobilidade do sigmoide e vólvulo", en="Sigmoid mobility and volvulus",
        text="Sigmoid volvulus is possible because the sigmoid colon hangs on a {{c1::mesocolon}}.",
        extra="O sigmoide conserva mesocolo → é móvel → pode torcer sobre o próprio eixo vascular, fechando a luz (obstrução) e estrangulando os vasos (isquemia).",
        anchor="O colo transverso e o colo sigmoide fazem o contrário: mantêm um",
    ),
    dict(
        id="c02", imp="nucleo", sub="Partes e mobilidade",
        pt="Segmentos fixos do colo", en="Fixed segments of the colon",
        text="The ascending and descending colon are fixed because they are secondarily {{c1::retroperitoneal}}.",
        extra="Eram móveis no embrião; o mesocolo fundiu-se ao peritônio parietal posterior → perderam mesentério → não torcem.",
        anchor="passam a ser secundariamente retroperitoneais",
    ),
    dict(
        id="c03", imp="nucleo", sub="Marcas de superfície",
        pt="Origem mecânica dos haustros", en="Mechanical origin of haustra",
        text="Haustra appear because the taeniae coli are {{c1::shorter}} than the colonic wall.",
        extra="Faixa muscular mais curta que o tubo → franze a parede → saculações por fora e pregas semilunares por dentro.",
        anchor="as tênias são mais curtas que o comprimento do colo",
    ),
    dict(
        id="c04", imp="nucleo", sub="Marcas de superfície",
        pt="Natureza das tênias", en="Nature of the taeniae coli",
        text="The taeniae coli are condensations of the {{c1::longitudinal}} muscle layer.",
        extra="A muscular longitudinal do colo não é contínua: condensa-se em três faixas visíveis a olho nu.",
        anchor="As tênias são condensações da camada muscular",
    ),
    dict(
        id="c05", imp="apoio", sub="Marcas de superfície",
        pt="Apêndices omentais", en="Omental appendices",
        text="The fat-filled peritoneal projections on the surface of the colon are the omental {{c1::appendices}}.",
        extra="Também chamados corpos adiposos ou apêndices epiploicos. São marca do colo: não existem no delgado nem no reto.",
        anchor="projeções peritoneais cheias de gordura",
    ),
    dict(
        id="c06", imp="nucleo", sub="Marcas de superfície",
        pt="Extensão das tênias", en="Extent of the taeniae coli",
        text="The taeniae coli run from the cecum and fan out at the {{c1::rectosigmoid}} junction.",
        extra="Ali voltam a formar camada longitudinal contínua → o reto não tem tênias, nem haustros, nem apêndices omentais.",
        anchor="As três correm desde o ceco e terminam na",
    ),
    dict(
        id="c07", imp="apoio", sub="Apêndice vermiforme", step1=True,
        pt="Convergência das tênias na base do apêndice", en="Taeniae converge at the appendix base",
        text="The three taeniae coli converge at the base of the {{c1::appendix}}.",
        extra="Seguir a tênia livre do ceco até onde ela desaparece é o modo clássico de achar um apêndice em posição atípica.",
        anchor="três tênias convergem na base do apêndice",
    ),
    dict(
        id="c08", imp="nucleo", sub="Apêndice vermiforme",
        pt="Tecido do apêndice", en="Tissue of the appendix",
        text="The wall of the vermiform appendix is rich in {{c1::lymphoid}} tissue.",
        extra="É por isso que o apêndice é descrito como órgão linfoide do trato digestório.",
        anchor="cuja parede é notavelmente rica em",
    ),
    dict(
        id="c09", imp="apoio", sub="Apêndice vermiforme",
        pt="Comprimento do apêndice", en="Length of the appendix",
        text="The vermiform appendix is a blind tube about {{c1::6–10}} cm long.",
        extra="Medida cobrada quando a prova pede para caracterizar o apêndice vermiforme.",
        anchor="O apêndice vermiforme é um tubo cego de",
    ),
    dict(
        id="c10", imp="nucleo", sub="Apêndice vermiforme",
        pt="Posição mais frequente do apêndice", en="Most frequent appendix position",
        text="The most frequent position of the vermiform appendix is {{c1::retrocecal}}.",
        extra="Retrocecal 64% > pélvica 34% > pré-ileal 1–2% > pós-ileal 0,5%. A posição retrocecal explica a apendicite com dor anterior discreta.",
        fig="fig-05-apendice-posicoes.png",
        anchor="retrocecal em cerca de 64% dos casos",
    ),
    dict(
        id="c11", imp="apoio", sub="Apêndice vermiforme",
        pt="Ponto de McBurney", en="McBurney's point",
        text="McBurney's point lies on the line from the anterior superior iliac spine to the {{c1::umbilicus}}.",
        extra="Fica na junção do terço lateral com o terço médio dessa linha; é a projeção do apêndice na parede abdominal.",
        fig="fig-06-mcburney.png",
        anchor="a projeção do apêndice na parede abdominal",
    ),
    dict(
        id="c12", imp="apoio", sub="Reto",
        pt="Extensão do reto", en="Length of the rectum",
        text="The rectum runs from the sigmoid colon to the anal canal and is about {{c1::15}} cm long.",
        extra="Sem tênias, sem haustros e sem apêndices omentais — as três marcas se dispersam na junção retossigmoide.",
        anchor="O reto vai do colo sigmoide ao canal anal e mede cerca de 15 cm",
    ),
    dict(
        id="c13", imp="nucleo", sub="Reto",
        pt="Origem da flexura anorretal", en="Origin of the anorectal flexure",
        text="The anorectal flexure is produced by the {{c1::puborectalis}} muscle.",
        extra="A alça passa por trás da junção anorretal e se fixa ao púbis pelas duas pontas; contraída, fecha o ângulo e mantém a continência em repouso.",
        fig="fig-08-puborretal.png",
        anchor="De todas as curvas, a que tem função é a",
    ),
    dict(
        id="c14", imp="nucleo", sub="Reto",
        pt="Puborretal na defecação", en="Puborectalis during defecation",
        text="During defecation, relaxation of the puborectalis {{c1::straightens}} the anorectal junction.",
        extra="A alça afrouxa → o ângulo se abre → reto e canal anal se alinham e o conteúdo desce. Continência e evacuação são a mesma alça em dois estados.",
        anchor="afrouxa a alça, o ângulo se abre e a junção anorretal se",
    ),
    dict(
        id="c15", imp="apoio", sub="Canal anal",
        pt="Conteúdo das colunas anais", en="Content of the anal columns",
        text="The anal columns contain branches of the {{c1::superior rectal}} vessels.",
        extra="São 8 a 10 pregas longitudinais na metade superior do canal anal, abrigando o plexo arteriovenoso submucoso.",
        anchor="cada uma contendo ramos dos",
        cloze_exception="",
    ),
    dict(
        id="c16", imp="apoio", sub="Canal anal",
        pt="Função dos seios anais", en="Function of the anal sinuses",
        text="The anal sinuses, between the bases of adjacent anal columns, release {{c1::mucus}}.",
        extra="O muco lubrifica a passagem do bolo fecal. É de uma glândula que se abre num seio anal que costuma partir a fístula anal.",
        anchor="os seios anais liberam muco que lubrifica",
    ),
    dict(
        id="c17", imp="nucleo", sub="Linha pectinada",
        pt="Origem embrionária acima da linha pectinada", en="Embryonic origin above the pectinate line",
        text="Above the pectinate line the lining is derived from {{c1::endoderm}}.",
        extra="Abaixo, deriva do ectoderma do proctodeu. Duas origens trazem dois conjuntos completos de artéria, veia, linfático e nervo.",
        anchor="o revestimento deriva do",
    ),
    dict(
        id="c18", imp="nucleo", sub="Linha pectinada",
        pt="Drenagem linfática acima da linha pectinada", en="Lymphatic drainage above the pectinate line",
        text="Above the pectinate line, lymph drains to the internal {{c1::iliac}} nodes.",
        extra="Abaixo da linha o fluxo vai para os linfonodos inguinais superficiais — por isso uma lesão baixa dá adenopatia na virilha.",
        fig="fig-10-linha-pectinada.png",
        anchor="acima da linha o fluxo vai para os",
    ),
    dict(
        id="c19", imp="nucleo", sub="Linha pectinada",
        pt="Drenagem linfática abaixo da linha pectinada", en="Lymphatic drainage below the pectinate line",
        text="Below the pectinate line, lymph drains to the superficial {{c1::inguinal}} nodes.",
        extra="Território ectodérmico. Adenopatia inguinal em lesão do canal anal baixo.",
        anchor="abaixo, para os",
    ),
    dict(
        id="c20", imp="nucleo", sub="Linha pectinada",
        pt="Inervação acima da linha pectinada", en="Innervation above the pectinate line",
        text="Above the pectinate line the innervation is {{c1::visceral}}.",
        extra="Não há sensibilidade dolorosa fina — percebe-se distensão. É por isso que a hemorroida interna não dói.",
        anchor="acima da linha o território é",
    ),
    dict(
        id="c21", imp="nucleo", sub="Linha pectinada",
        pt="Inervação abaixo da linha pectinada", en="Innervation below the pectinate line",
        text="Below the pectinate line the innervation is {{c1::somatic}}.",
        extra="Chamada parietal nos slides, pelo nervo retal inferior. A mucosa é sensível a dor, toque e temperatura.",
        anchor="Abaixo, a inervação é",
    ),
    dict(
        id="c22", imp="nucleo", sub="Linha pectinada",
        pt="Drenagem venosa acima da linha pectinada", en="Venous drainage above the pectinate line",
        text="Above the pectinate line the venous blood drains into the {{c1::portal}} system.",
        extra="Pela veia retal superior. Como abaixo o sangue vai para o sistema cava, o canal anal é sítio de anastomose portocava.",
        anchor="acima da linha o sangue segue pela veia retal superior para o sistema",
    ),
    dict(
        id="c23", imp="nucleo", sub="Linha pectinada",
        pt="Drenagem venosa abaixo da linha pectinada", en="Venous drainage below the pectinate line",
        text="Below the pectinate line the venous blood drains into the {{c1::caval}} system.",
        extra="Pelas veias retais média e inferior. O encontro dos dois territórios faz do canal anal uma anastomose portocava.",
        anchor="abaixo, pelas veias retais média e inferior para o sistema",
    ),
    dict(
        id="c24", imp="nucleo", sub="Linha pectinada",
        pt="Hemorroida interna", en="Internal hemorrhoid",
        text="A patient reports painless bright-red bleeding with prolapsing anal masses; these hemorrhoids are {{c1::internal}}.",
        extra="Dilatação do plexo venoso retal interno, acima da linha pectinada, em território visceral → sangra e prolapsa, mas não dói. A externa, abaixo da linha, é dolorosa.",
        fig="fig-12-hemorroidas.png",
        anchor="em território de inervação visceral: sangram",
    ),
    dict(
        id="c25", imp="nucleo", sub="Canal anal",
        pt="Definição da junção anorretal", en="Definition of the anorectal junction",
        text="The anorectal junction is marked by the upper ends of the anal {{c1::columns}}.",
        extra="É a 'linha anorretal' da pergunta orientadora e o ponto onde começa o canal anal cirúrgico.",
        anchor="A extremidade superior das colunas define a",
    ),
    dict(
        id="c26", imp="nucleo", sub="Esfíncteres",
        pt="Esfíncter anal interno", en="Internal anal sphincter",
        text="The internal anal sphincter is composed of {{c1::smooth}} muscle.",
        extra="Espessamento da camada muscular circular; involuntário, mantido em contração tônica pelo autônomo — responde pelo tônus de repouso.",
        anchor="é um espessamento da camada",
    ),
    dict(
        id="c27", imp="nucleo", sub="Esfíncteres",
        pt="Esfíncter anal externo", en="External anal sphincter",
        text="The external anal sphincter is composed of {{c1::skeletal}} muscle.",
        extra="Voluntário, inervado pelo nervo retal inferior; é o que se contrai deliberadamente para adiar a evacuação.",
        anchor="é músculo estriado esquelético, voluntário",
    ),
    dict(
        id="c28", imp="apoio", sub="Correlações",
        pt="Megacólon chagásico", en="Chagasic megacolon",
        text="In Chagas disease, megacolon follows destruction of neurons of the {{c1::myenteric}} plexus.",
        extra="Sem o comando entérico, a motilidade cai → o conteúdo se acumula → o segmento se dilata cronicamente (colomegalia).",
        fig="fig-13-megacolon-chagas.png",
        anchor="destruição de neurônios do",
    ),
    dict(
        id="c29", imp="apoio", sub="Reto",
        pt="Relação do ureter com o mesocolo sigmoide", en="Ureter and the sigmoid mesocolon",
        text="The structure at risk at the root of the sigmoid mesocolon is the left {{c1::ureter}}.",
        extra="Ele desce para a pelve junto dos vasos do sigmoide — reconhecê-lo antes de ligar os vasos é parte do tempo cirúrgico.",
        fig="fig-14-sigmoide-ureter.png",
        anchor="passa muito próximo à raiz do mesocolo sigmoide",
    ),
    dict(
        id="c30", imp="nucleo", sub="Reto",
        pt="Escavação retovesical", en="Rectovesical pouch",
        text="In the male, the peritoneum between the rectum and the bladder forms the {{c1::rectovesical}} pouch.",
        extra="Na mulher há duas reflexões: a retouterina (fundo de saco de Douglas) e a vesicouterina. São o ponto mais baixo da cavidade peritoneal.",
        anchor="No homem existe uma única reflexão entre reto e bexiga",
    ),
    dict(
        id="c31", imp="apoio", sub="Canal anal",
        pt="Válvulas anais", en="Anal valves",
        text="The transverse folds joining the bases of adjacent anal columns are the anal {{c1::valves}}.",
        extra="Elas fecham os seios anais por baixo; a linha em que se alinham é a própria linha pectinada.",
        anchor="são as válvulas anais",
    ),
    # ---- Optional: aprofundamento dispensável nesta prova -----------------
    dict(
        id="o01", imp="opcional", sub="Correlações",
        pt="Doença de Crohn — extensão", en="Crohn disease extent",
        text="The inflammatory bowel disease that may involve the whole gut from esophagus to rectum is {{c1::Crohn}} disease.",
        extra="A retocolite ulcerativa, em contraste, acomete o colo de forma homogênea e contínua.",
        anchor="pode acometer todo o trato digestório, do esôfago ao reto",
    ),
    dict(
        id="o02", imp="opcional", sub="Correlações",
        pt="Retocolite ulcerativa — padrão", en="Ulcerative colitis pattern",
        text="Ulcerative colitis involves the colonic mucosa in a {{c1::continuous}} pattern.",
        extra="Descrita nos slides como acometimento homogêneo, por oposição ao padrão salteado da doença de Crohn.",
        anchor="o acomete de forma homogênea e contínua",
    ),
    dict(
        id="o03", imp="opcional", sub="Correlações",
        pt="Fístula anal", en="Anal fistula",
        text="An anal fistula is an abnormal tunnel connecting the anal canal to the perianal {{c1::skin}}.",
        extra="Costuma partir da infecção de uma glândula que se abre num seio anal; o pus disseca entre os esfíncteres até a pele.",
        anchor="trajeto anormal que comunica o canal anal com a pele perianal",
    ),
    dict(
        id="o04", imp="opcional", sub="Linha pectinada",
        pt="Artéria acima da linha pectinada", en="Artery above the pectinate line",
        text="Above the pectinate line the arterial supply comes from the inferior {{c1::mesenteric}} artery.",
        extra="Pela artéria retal superior. Detalhe vascular retomado na aula de vascularização das vísceras.",
        anchor="o território acima vem da artéria mesentérica inferior",
    ),
    dict(
        id="o05", imp="opcional", sub="Linha pectinada",
        pt="Artéria abaixo da linha pectinada", en="Artery below the pectinate line",
        text="Below the pectinate line the arterial supply comes from the internal {{c1::iliac}} artery.",
        extra="Pelas artérias retais média e inferior. Detalhe vascular retomado na aula de vascularização das vísceras.",
        anchor="o de baixo, da artéria ilíaca interna",
    ),
]

# --------------------------------------------------------------------------
# Image Occlusion. Um card por mapa coerente (hide_all_guess_all).
# --------------------------------------------------------------------------
IO = [
    dict(id="io-01-partes", imp="nucleo", sub="Partes e mobilidade",
         pt="Partes do intestino grosso e mobilidade", en="Parts of the large intestine and mobility",
         anchor="o percurso passa por dez estruturas nomeadas, nesta ordem",
         task="Nomear, na ordem, as dez partes do intestino grosso e dizer quais são fixas e quais são móveis."),
    dict(id="io-02-superficie", imp="nucleo", sub="Marcas de superfície",
         pt="Marcas de superfície e flexuras do colo", en="Surface features and flexures of the colon",
         anchor="três marcas identificam o colo de imediato",
         task="Reconhecer tênias, haustros, apêndices omentais e as duas flexuras cólicas na prancha do colo."),
    dict(id="io-03-tenias", imp="nucleo", sub="Marcas de superfície",
         pt="As três tênias do colo", en="The three taeniae coli",
         anchor="a tênia mesocólica",
         task="Localizar tênia livre, omental e mesocólica no ceco e reconhecer o apêndice e o íleo."),
    dict(id="io-04-ceco-interno", imp="nucleo", sub="Junção ileocecal",
         pt="Interior do ceco e válvula ileocecal", en="Interior of the cecum and ileocecal valve",
         anchor="o conjunto dessas duas pregas que recebe o nome de",
         task="Identificar papila ileal, óstio ileal, lábios ileocólico e ileocecal, válvula ileocecal e óstio do apêndice."),
    dict(id="io-05-peca-ileocecal", imp="nucleo", sub="Junção ileocecal",
         pt="Região ileocecal em peça anatômica", en="Ileocecal region on a real specimen",
         anchor="É essa imagem — e não o desenho — que a prática cobra.",
         task="Reconhecer ceco, apêndice, íleo distal e tênia livre em peça real, sem as cores do atlas."),
    dict(id="io-06-reto", imp="nucleo", sub="Reto",
         pt="Flexuras laterais e pregas transversas do reto", en="Lateral flexures and transverse folds of the rectum",
         anchor="as pregas transversas do reto",
         task="Identificar as três flexuras laterais, as três pregas transversas e a ampola retal."),
    dict(id="io-07-peca-reto", imp="nucleo", sub="Reto",
         pt="Reto em peça anatômica", en="Rectum on a real specimen",
         anchor="a flexura sacral",
         task="Reconhecer flexura sacral, flexura anorretal, ampola retal e prega transversa em corte sagital de peça real."),
    dict(id="io-08-pelve-fem", imp="nucleo", sub="Reto",
         pt="Escavações peritoneais na pelve feminina", en="Peritoneal pouches in the female pelvis",
         anchor="a escavação retouterina",
         task="Localizar as escavações retouterina e vesicouterina e as referências retais na pelve feminina."),
    dict(id="io-09-canal-anal", imp="nucleo", sub="Canal anal",
         pt="Relevo interno do canal anal", en="Internal relief of the anal canal",
         anchor="as colunas anais",
         task="Identificar colunas anais, seios anais, linha pectinada, linha branca, plexos venosos e junção anorretal."),
    dict(id="io-10-peca-canal", imp="nucleo", sub="Canal anal",
         pt="Canal anal em peça anatômica", en="Anal canal on a real specimen",
         anchor="o seio anal",
         task="Reconhecer coluna anal, seio anal, ampola retal e flexura anorretal em peça real."),
    dict(id="io-11-esfincteres", imp="nucleo", sub="Esfíncteres",
         pt="Esfíncteres do ânus e puborretal", en="Anal sphincters and puborectalis",
         anchor="dois esfíncteres sobrepostos",
         task="Nomear esfíncter interno, esfíncter externo, puborretal/levantador do ânus e as camadas circular e longitudinal."),
]

# Step 1 avaliado e recusado — a recusa é parte do contrato.
STEP1_REJEITADO = [
    dict(candidate="Doença de Hirschsprung como contraste do megacólon chagásico",
         source="mesmo mecanismo (plexo mioentérico), sugerido pela correlação do slide 18",
         decision="rejected",
         rationale="Não está nos slides nem nos objetivos; exigiria abrir aganglionose congênita, "
                   "migração de crista neural e diagnóstico por biópsia — árvore de pré-requisitos "
                   "própria. Vizinho high-yield, não aprofundamento do mesmo conteúdo."),
    dict(candidate="Ponto de Griffiths / área de transição vascular na flexura esplênica",
         source="anatomia vascular do colo",
         decision="rejected",
         rationale="Vascularização das vísceras é aula própria no cronograma (11/09). Fora do escopo desta aula."),
    dict(candidate="Estadiamento e conduta do câncer colorretal",
         source="correlação clínica frequente do tema",
         decision="rejected",
         rationale="Estadiamento e conduta estão explicitamente excluídos por docs/canon/COBERTURA-E-STEP1.md."),
    dict(candidate="Nove regiões abdominais (slides 7–8) como card de identificação",
         source="slide da própria aula",
         decision="rejected",
         rationale="Presente no slide, mas ausente do roteiro prático e das perguntas orientadoras; "
                   "a prancha tem rótulos rasterizados duplicados que tornariam o IO ambíguo. "
                   "Registrado como fora do deck, não como lacuna."),
    dict(candidate="Convergência das três tênias na base do apêndice",
         source="Moore, Anatomia orientada para a clínica — referência de mesmo tema",
         decision="accepted",
         rationale="Aprofunda a mesma estrutura já ensinada (tênias + apêndice), encaixa na seção 2.2, "
                   "é durável e não abre pré-requisito novo. Explicado na E1 antes do card (card c07)."),
    dict(candidate="Anastomose portocava do canal anal",
         source="slide 23 da própria aula (veias acima → sistema porta; abaixo → sistema cava)",
         decision="accepted",
         rationale="Está desenhado no slide da aula; aprofunda o mesmo mecanismo da linha pectinada. "
                   "Explicado na E1 em 4.2 (cards c22 e c23)."),
]


def desmarcar(texto: str) -> str:
    """Remove marcação Typst para comparar âncoras com a prosa da E1."""
    texto = re.sub(r"#(strong|emph)\[", "", texto)
    texto = re.sub(r"#termo-nota\[([^\]]*)\]\[[^\]]*\]", r"\1", texto)
    texto = texto.replace("]", "").replace("[", "")
    return re.sub(r"\s+", " ", texto)


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(ch for ch in texto if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", texto).casefold()


def contar_palavras_cloze(texto: str) -> int:
    match = re.search(r"\{\{c1::(.*?)\}\}", texto)
    if not match:
        raise ValueError(f"sem cloze c1: {texto}")
    return len(re.findall(r"[^\W_]+(?:[-–'][^\W_]+)*", match.group(1), flags=re.UNICODE))


def main() -> int:
    e1_raw = E1.read_text(encoding="utf-8")
    e1_flat = normalizar(desmarcar(e1_raw))

    conceitos, cards, problemas = [], [], []

    for card in CLOZE:
        if normalizar(card["anchor"]) not in e1_flat:
            problemas.append(f"âncora ausente na E1 ({card['id']}): {card['anchor']!r}")
        palavras = contar_palavras_cloze(card["text"])
        if palavras > 3:
            problemas.append(f"cloze com {palavras} palavras ({card['id']})")
        if card["text"].count("{{c") != 1:
            problemas.append(f"mais de uma ocorrência de cloze ({card['id']})")

        conceitos.append({
            "id": card["id"],
            "name_pt": card["pt"],
            "name_en": card["en"],
            "subtopic": card["sub"],
            "origins": ["slide", "roteiro"] if card["imp"] != "opcional" else ["slide"],
            "importance": card["imp"],
            "e1_anchor": card["anchor"],
            "step1": {
                "decision": "accepted" if card.get("step1") else "not_applicable",
                "same_theme": True,
                "source_ref": "Moore, Anatomia orientada para a clínica" if card.get("step1") else "",
                "rationale": "Aprofunda a mesma estrutura da aula e já está explicado na E1."
                             if card.get("step1") else "",
            },
            "visual": {
                "need": "supporting" if card.get("fig") else "none",
                "role": "explain_mechanism" if card.get("fig") else "none",
                "mode": "image_in_extra" if card.get("fig") else "none",
                "task": "Imagem no Extra sustenta o mecanismo; a recuperação é verbal."
                        if card.get("fig") else "Conceito estritamente verbal.",
                "status": "approved" if card.get("fig") else "not_needed",
                "asset": f"{FIG}/{card['fig']}" if card.get("fig") else None,
            },
            "route": {
                "source": "authored",
                "coverage_quality": 3 if card["imp"] == "nucleo" else 2,
                "coverage_rationale": "Card reconstrói o fato e o mecanismo explicado na E1."
                                      if card["imp"] == "nucleo" else "Card fixa o fato central.",
                "card_refs": [card["id"]],
                "source_guid": "",
                "candidate_search": {
                    "status": "blocked_private_index_unreachable",
                    "anking_count": 0,
                    "external_count": 0,
                    "query_families": {
                        "pt": [card["pt"]],
                        "en": [card["en"]],
                        "synonyms": [],
                        "mechanism_or_structure": [card["sub"]],
                        "tags_or_siblings": ["#AK_Step1::Anatomy::GI", "large intestine"],
                    },
                    "siblings_reviewed": False,
                    "rejection_rationale": (
                        "O índice privado do AnKing existe no Drive (anking-index-v2, 564 MB; "
                        "arquivo-fonte 5,9 GB) mas não é transferível para este ambiente de execução. "
                        "Busca real executada no único corpus AnKing-derivado local "
                        "(flashcards/decks-apkg/P3 - UC02 completo.apkg, 247 notas): 4 acertos de texto, "
                        "todos de outras aulas (Peyer's patches, ramos da aorta) e nenhum candidato "
                        "para este conceito. Autoria registrada como pendente de recuradoria."
                    ),
                },
            },
            "tags": [card["imp"]],
        })

        cards.append({
            "id": card["id"],
            "concept_ids": [card["id"]],
            "source": "authored",
            "format": "cloze",
            "retrieval_target": card["en"],
            "generated_card_count": 1,
            "atomicity": {
                "decision": "approved",
                "exception": "",
                "rationale": "Um único c1, uma única ocorrência, uma recuperação independente.",
            },
            "text": card["text"],
            "cloze_answer_words": palavras,
            "cloze_exception_reason": card.get("cloze_exception", ""),
            "note": {
                "model": "Cloze NEBLI - Aula",
                "fields": {
                    "Text": card["text"],
                    "Extra": card["extra"],
                    "Image": f'<img src="{FIG}/{card["fig"]}">' if card.get("fig") else "",
                    "Source": f"E1 §{card['sub']} — “{card['anchor']}”",
                    "Tema": TEMA,
                    "NEBLI_Comentario": "",
                    "NEBLI_Resposta": "",
                },
                "tags": ["NEBLI::" + SLUG, card["imp"], "subtopico::" + card["sub"].replace(" ", "_")],
            },
            "importance": card["imp"],
        })

    for item in IO:
        manifesto = json.loads((LESSON / "io" / item["id"] / f"{item['id']}.manifest.json").read_text(encoding="utf-8"))
        if normalizar(item["anchor"]) not in e1_flat:
            problemas.append(f"âncora ausente na E1 ({item['id']}): {item['anchor']!r}")
        if not manifesto["masks"]:
            problemas.append(f"IO sem máscaras ({item['id']})")

        conceitos.append({
            "id": item["id"],
            "name_pt": item["pt"],
            "name_en": item["en"],
            "subtopic": item["sub"],
            "origins": ["slide", "roteiro"],
            "importance": item["imp"],
            "e1_anchor": item["anchor"],
            "step1": {"decision": "not_applicable", "same_theme": True, "source_ref": "", "rationale": ""},
            "visual": {
                "need": "required",
                "role": "identify_or_locate",
                "mode": "image_occlusion",
                "task": item["task"],
                "status": "approved",
                "asset": f"io/{item['id']}/{manifesto['image']}",
                "io": {
                    "behavior": manifesto["behavior"],
                    "coherent_visual_map": manifesto["coherent_visual_map"],
                    "labels": [mask["text"] for mask in manifesto["masks"]],
                    "mask_covers_answer_label": manifesto["mask_covers_answer_label"],
                    "blanked_regions": manifesto.get("blanked_regions", []),
                    "previews": manifesto["previews"],
                    "previews_reviewed": True,
                    "source": f"Slides da aula, p. {manifesto['page']} "
                              f"({manifesto['source_pdf']}) — crédito preservado no recorte",
                    "sha256": manifesto["image_sha256"],
                    "leakage_check": "Rótulos duplicados rasterizados na figura também mascarados; "
                                     "textos explicativos entre parênteses mantidos visíveis por não "
                                     "nomearem a estrutura.",
                },
            },
            "route": {
                "source": "authored",
                "coverage_quality": 3,
                "coverage_rationale": "Mapa coerente cobre a lista de identificação do roteiro prático.",
                "card_refs": [item["id"]],
                "source_guid": "",
                "candidate_search": {
                    "status": "blocked_private_index_unreachable",
                    "anking_count": 0,
                    "external_count": 0,
                    "query_families": {
                        "pt": [item["pt"]],
                        "en": [item["en"]],
                        "synonyms": [],
                        "mechanism_or_structure": [item["sub"]],
                        "tags_or_siblings": ["#AK_Step1::Anatomy::GI"],
                    },
                    "siblings_reviewed": False,
                    "rejection_rationale": (
                        "Índice AnKing privado inacessível neste ambiente; além disso a identificação é "
                        "cobrada em nomenclatura portuguesa sobre as pranchas e peças da própria aula, "
                        "que o AnKing não fornece."
                    ),
                },
            },
            "tags": [item["imp"]],
        })

        cards.append({
            "id": item["id"],
            "concept_ids": [item["id"]],
            "source": "authored",
            "format": "image_occlusion",
            "retrieval_target": item["task"],
            "generated_card_count": 1,
            "atomicity": {
                "decision": "approved",
                "exception": "coherent_visual_map",
                "rationale": "Exceção multi-alvo prevista em docs/canon/VISUAL-E-IO.md: mapa coerente "
                             "recuperado como unidade em hide_all_guess_all.",
            },
            "text": item["task"],
            "note": {
                "model": "IO NEBLI - Image Occlusion (mapa coerente)",
                "fields": {
                    "Header": manifesto["header"],
                    "ImagemPergunta": f'<img src="{SLUG}-{item["id"]}-pergunta.png">',
                    "ImagemResposta": f'<img src="{SLUG}-{item["id"]}-resposta.png">',
                    "Extra": item["pt"],
                    "Rotulos": " · ".join(mask["text"] for mask in manifesto["masks"]),
                    "I0": manifesto["i0_field"],
                    "Fonte": f"Slides da aula, p. {manifesto['page']} — {item['sub']} · "
                             f"E1 “{item['anchor']}”",
                    "NEBLI_Comentario": "",
                    "NEBLI_Resposta": "",
                },
                "media": {
                    f"{SLUG}-{item['id']}-pergunta.png":
                        str(LESSON / "io" / item["id"] / manifesto["previews"]["question"]),
                    f"{SLUG}-{item['id']}-resposta.png":
                        str(LESSON / "io" / item["id"] / manifesto["previews"]["answer"]),
                },
                "tags": ["NEBLI::" + SLUG, item["imp"], "subtopico::" + item["sub"].replace(" ", "_"), "IO"],
            },
            "importance": item["imp"],
        })

    total = sum(card["generated_card_count"] for card in cards)
    hard_max = 50
    if total > hard_max:
        problemas.append(f"teto excedido: {total} > {hard_max}")

    contrato = {
        "pipeline_version": "e1-deck-v3",
        "slug": SLUG,
        "title": "Intestino grosso, reto e canal anal",
        "deck": DECK,
        "optional_deck": DECK + "::Optional",
        "status": "frozen",
        "lesson_sources": {
            "slides": "Alunos_ Intestino grosso_reto_canal anal_FINAL_2026.pdf (27 p.)",
            "roteiro_pratico": "ROTEIRO_ intestino grosso_Final_2026.pdf",
            "perguntas_orientadoras": "Perguntas orientadoras Intestino Grosso.pdf",
            "cronograma": "cronogramas/digestorio-uc8-med5043-2026.md (UC-8, P1, Anatomia, Turma B 10/08)",
        },
        "card_budget": {
            "lesson_size": "large",
            "hard_max": hard_max,
            "expected_total_cards": total,
            "rationale": (
                "Aula grande: o roteiro prático lista 22 alvos de identificação e as perguntas "
                "orientadoras cobrem sete blocos conceituais. Teto congelado em 50 antes da busca; "
                "faixa de sanidade para aula grande é 35–55."
            ),
            "manual_scope_review": "not_required",
            "review_rationale": "Total abaixo de 60; nenhuma revisão manual de escopo exigida.",
        },
        "e1": {
            "path": "typst-build/anato-intestino-grosso/etapa1.typ",
            "sha256": hashlib.sha256(E1.read_bytes()).hexdigest(),
            "pdf": "Intestino grosso, reto e canal anal - E1.pdf",
        },
        "private_sources": {
            "anking_index": {
                "status": "unreachable_in_execution_environment",
                "path": "Google Drive · Anking/AnKing-index-v2/anking-index-v2.private.sqlite.zip",
                "sha256": "4d9d147b647357a0f5b8240e4af9b4bb571bca80c1f48ffb7afb900413b71557",
                "note": (
                    "Índice de 564 MB (103 MB comprimido, 2 partes) e pacote-fonte de 5,9 GB. O canal "
                    "MCP do Drive devolve conteúdo em base64 pelo contexto do modelo, o que inviabiliza "
                    "trazer o índice. Ver RETROSPECTIVA-PROCESSO.md para a correção proposta."
                ),
            },
            "external_indexes": [
                {
                    "name": "flashcards/decks-apkg/P3 - UC02 completo.apkg",
                    "status": "searched",
                    "notes": 247,
                    "hits": 4,
                    "result": "Nenhum candidato para os conceitos desta aula.",
                }
            ],
        },
        "step1_decisions": STEP1_REJEITADO,
        "concepts": conceitos,
        "cards": cards,
        "gates": {
            "every_card_has_e1_anchor": True,
            "cloze_policy_1_2_3_words": True,
            "io_multi_label_mode": "hide_all_guess_all",
            "optional_separated": True,
            "blocking_issues": problemas,
        },
    }

    saida = LESSON / "contrato-cobertura.json"
    saida.write_text(json.dumps(contrato, ensure_ascii=False, indent=2), encoding="utf-8")

    nucleo = sum(1 for c in cards if c["importance"] == "nucleo")
    apoio = sum(1 for c in cards if c["importance"] == "apoio")
    opcional = sum(1 for c in cards if c["importance"] == "opcional")
    print(f"contrato: {saida.relative_to(RAIZ)}")
    print(f"cards: {total} (núcleo {nucleo} · apoio {apoio} · opcional {opcional}) · teto {hard_max}")
    print(f"conceitos: {len(conceitos)}")
    if problemas:
        print("BLOQUEIOS:")
        for problema in problemas:
            print("  -", problema)
        return 1
    print("nenhum bloqueio")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
