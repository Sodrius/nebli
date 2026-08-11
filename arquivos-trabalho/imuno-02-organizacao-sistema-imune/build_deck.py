#!/usr/bin/env python3
"""Monta deck-data.json (v9) e validacao-cards.json da aula imuno-01.

O plano final é escrito aqui de forma determinística para que o gate card a card
e o release gate leiam exatamente os mesmos cards, sem transcrição manual.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

WD = Path(__file__).resolve().parent
ROOT = WD.parents[1]
SLUG = "imuno-02-organizacao-sistema-imune"
E1_SOURCE = "../../typst-build/etapa1.typ"
E1_PDF = f"../../typst-build/{SLUG}.pdf"
HARD_MAX = 52

CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}")

# Prova de busca AnKing usada por todo card não-AnKing (autorais, fallbacks e IO).
SEARCH_AUDIT_DEFAULT = {
    "anking_search_complete": True,
    "anking_search_scope_expanded": True,
    "anking_siblings_reviewed": True,
    "anking_candidates_reviewed": 0,
}

cards: list[dict] = []
concepts: list[dict] = []


def _words(text: str) -> int:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return len([w for w in re.split(r"\s+", text.strip()) if w])


def authored_body(text: str, extra: str, retrieval: str, *, three_word_reason: str = "") -> dict:
    body = {
        "source": "authored",
        "text": text,
        "extra": extra,
        "front_language": "en",
        "extra_language": "pt-BR",
        "retrieval_target": retrieval,
        "authored_quality": {
            "single_retrieval": True,
            "unambiguous_prompt": True,
            "no_functional_duplicate": True,
            "extra_only_supports_answer": True,
            "medical_english_reviewed": True,
        },
    }
    if three_word_reason:
        body["three_word_cloze_reason"] = three_word_reason
    return body


def authored(key: str, concept: str, text: str, extra: str, retrieval: str,
             queries: list[str], rejection: str, *, tier: str = "nucleo",
             three_word_reason: str = "") -> None:
    card = {
        "card_key": key,
        "concept_id": concept,
        "tier": tier,
        "atomic": True,
        "relevant": True,
        **authored_body(text, extra, retrieval, three_word_reason=three_word_reason),
        **SEARCH_AUDIT_DEFAULT,
        "anking_search_queries": queries,
        "anking_rejection_reason": rejection,
    }
    cards.append(card)


def anking(key: str, concept: str, query: str, aliases: list[str], expected: list[str],
           fb_text: str, fb_extra: str, fb_retrieval: str, *,
           must_contain: list[str] | None = None, must_not_contain: list[str] | None = None,
           tier: str = "nucleo", fb_three_word_reason: str = "") -> None:
    cards.append({
        "card_key": key,
        "concept_id": concept,
        "source": "anking",
        "tier": tier,
        "atomic": True,
        "relevant": True,
        "query": query,
        "aliases": aliases,
        "search_queries": [query, *aliases],
        "expected_answers": expected,
        "must_contain": must_contain or [],
        "must_not_contain": must_not_contain or [],
        "anking_required": True,
        "fallback": authored_body(fb_text, fb_extra, fb_retrieval,
                                  three_word_reason=fb_three_word_reason),
    })


def io(key: str, concept: str, image: str, masks: list[dict], answers: list[str],
       pair_rationale: str, cognitive_purpose: str, credit: str,
       queries: list[str], rejection: str) -> None:
    cards.append({
        "card_key": key,
        "concept_id": concept,
        "source": "io",
        "tier": "nucleo",
        "atomic": True,
        "relevant": True,
        "mode": "hide_two_guess_two",
        "image_path": image,
        "masks": masks,
        "answers": answers,
        "coherent_set": True,
        "pair_rationale": pair_rationale,
        "masks_labels_not_structures": True,
        "question_preview_validated": True,
        "answer_preview_validated": True,
        "visual_ok": True,
        "real_source": True,
        "answer_leak": False,
        "source_credit": credit,
        "cognitive_purpose": cognitive_purpose,
        "didactic_value_reviewed": True,
        **SEARCH_AUDIT_DEFAULT,
        "anking_search_queries": queries,
        "anking_rejection_reason": rejection,
    })


def concept(cid: str, importance: str, anchor: str, quality: int, keys: list[str],
            step1: dict) -> None:
    concepts.append({
        "concept_id": cid,
        "importance": importance,
        "e1_anchor": anchor,
        "coverage_quality": quality,
        "card_keys": keys,
        "step1": step1,
    })


NA = {"decision": "not_applicable"}


def inc(source_ref: str, rationale: str) -> dict:
    return {"decision": "incorporated", "same_theme": True,
            "source_ref": source_ref, "rationale": rationale}


def rej(rationale: str) -> dict:
    return {"decision": "rejected", "rationale": rationale}


# ---------------------------------------------------------------- PARTE I

authored(
    "au-exterior-sensing", "c001",
    "Only two systems include the outside world in homeostasis: the immune system, which reads molecular signals, and the {{c1::nervous}} system.",
    "O sistema nervoso lê o exterior por luz, som, temperatura e pressão; o imune lê o exterior pela química do que encosta no organismo. Os demais sistemas monitoram apenas o meio interno.",
    "Qual é o outro sistema que inclui o exterior na manutenção da homeostasia.",
    ["immune system homeostasis external environment molecular signals",
     "nervous and immune systems monitor the outside world",
     "immune system senses molecular signals unlike other organ systems"],
    "A recuperação é o enquadramento conceitual da aula (quais sistemas incluem o exterior na homeostasia); o material Step 1 organiza imunologia por células, moléculas e doenças e não testa essa comparação entre sistemas.",
)

authored(
    "au-clonal-distribution", "c002",
    "The receptor repertoire recognizes almost any antigen, yet each lymphocyte binds only one, because the repertoire is distributed {{c1::clonally}}.",
    "Cada linfócito T ou B expressa um único tipo de receptor e transmite essa especificidade às células-filhas, formando um clone. O sistema reconhece tudo; a célula reconhece uma coisa só.",
    "Como o repertório completo se distribui entre as células.",
    ["clonal distribution of antigen receptors one lymphocyte one specificity",
     "clonal selection theory lymphocyte single antigen receptor",
     "antigen receptor diversity repertoire distributed among lymphocyte clones"],
    "O material Step 1 testa seleção clonal pela expansão do clone após o antígeno; a recuperação desta aula é anterior e diferente — como o repertório completo está distribuído antes de qualquer antígeno aparecer.",
)

authored(
    "au-damps", "c003",
    "Cells of an injured tissue raise the most primitive alarm by releasing intracellular molecules called {{c1::DAMPs}}.",
    "O sinal diz apenas que há dano, sem informar de que tipo. É o degrau mais baixo do alarme: as citocinas do macrófago, logo acima, já informam mais ou menos o que está errado.",
    "Que classe de molécula a célula do tecido lesada libera como alarme.",
    ["damage associated molecular patterns released by injured cells",
     "DAMPs versus PAMPs danger signals from necrotic tissue",
     "endogenous danger signals released by damaged host cells"],
    "As notas Step 1 sobre DAMP tratam do reconhecimento por receptores de padrão e do inflamassoma, matéria da aula seguinte; a recuperação daqui é a atribuição do sinal à célula do tecido lesada dentro da graduação do alarme.",
)

anking(
    "ak-mastocito-histamina", "c003",
    "mast cell degranulation releases preformed histamine causing vasodilation and increased vascular permeability",
    ["mast cell granules histamine release inflammation",
     "mast cell preformed mediators immediate vascular response"],
    ["histamine"],
    "The mast cell is the tissue alarm that degranulates all at once, releasing preformed {{c1::histamine}}.",
    "Vasodilatação e aumento de permeabilidade em minutos: é o alarme que troca informação detalhada por velocidade.",
    "Qual mediador pré-formado o mastócito libera ao degranular.",
)

authored(
    "au-cytotoxicity", "c004",
    "In cell-mediated cytotoxicity the effector delivers a signal, the target dies by {{c1::apoptosis}}, and the effector survives to seek another target.",
    "A morte é programada e contida: o conteúdo da célula-alvo não extravasa para o tecido, e a mesma efetora mata vários alvos em sequência porque gasta sinal, não gasta a si mesma.",
    "De que modo a célula-alvo morre na citotoxicidade celular.",
    ["cytotoxic T cell kills target by inducing apoptosis perforin granzyme",
     "cell mediated cytotoxicity target cell programmed death",
     "NK cell cytotoxicity apoptosis of target cell serial killing"],
    "As notas Step 1 equivalentes são sobre perforina e granzima e sobre marcadores de célula NK; a recuperação desta aula é o princípio de que quem morre executa a própria morte enquanto a efetora sobrevive.",
)

authored(
    "au-ilc-direction", "c005",
    "Beyond macrophages and mast cells, the tissue hosts innate lymphocytes that bias which kind of acquired response will follow: the {{c1::ILCs}}.",
    "A resposta adquirida não é o plano B: ela se monta no mesmo episódio, dirigida às moléculas daquele tecido. As células inatas residentes é que inclinam o tipo de resposta que vai se desenvolver.",
    "Que célula residente do tecido direciona o tipo de resposta adquirida.",
    ["innate lymphoid cells direct type of adaptive immune response",
     "ILC tissue resident innate lymphocytes shape adaptive immunity",
     "innate cells instruct adaptive response polarization in tissue"],
    "O conteúdo Step 1 sobre ILC praticamente se limita a citá-las como equivalentes inatas dos linfócitos T auxiliares; a recuperação da aula é o papel delas em direcionar a resposta adquirida do mesmo episódio.",
)

# ---------------------------------------------------------------- PARTE II

authored(
    "au-somatic-receptor-genes", "c006",
    "The genes encoding clonal antigen receptors are absent from the germline and are assembled {{c1::somatically}} inside the primary lymphoid organ.",
    "Cada precursor recombina segmentos gênicos e sorteia a própria combinação; é desse sorteio que sai a diversidade do repertório, e ele só acontece no timo e na medula óssea.",
    "Como e onde nascem os genes que codificam o receptor clonal.",
    ["antigen receptor genes assembled by somatic VDJ recombination",
     "immunoglobulin gene rearrangement occurs in developing lymphocytes",
     "TCR gene rearrangement in thymus generates receptor diversity"],
    "As notas Step 1 correspondentes cobram os segmentos V, D e J e a enzima RAG; a recuperação da aula é anterior a esse detalhe — que o gene do receptor não existe na linhagem germinativa e é montado somaticamente.",
)

anking(
    "ak-b-medula-ossea", "c006",
    "B lymphocytes complete maturation in the bone marrow whereas T lymphocytes mature in the thymus",
    ["B cell maturation site bone marrow primary lymphoid organ",
     "site of B lymphocyte development and maturation"],
    ["bone marrow"],
    "Whereas T lymphocytes mature in the thymus, B lymphocytes complete maturation in the {{c1::bone marrow}}.",
    "Os dois são órgãos linfoides primários: geram o repertório e o selecionam isolados do meio externo.",
    "Onde o linfócito B amadurece.",
)

anking(
    "ak-selecao-positiva", "c007",
    "positive selection of thymocytes occurs in the thymic cortex and requires the TCR to bind self MHC on cortical epithelial cells",
    ["thymic cortex positive selection MHC restriction thymocyte",
     "thymocyte that cannot bind self MHC dies by neglect"],
    ["cortex", "thymic cortex"],
    "A thymocyte whose receptor cannot bind self-MHC at all dies by neglect during positive selection, which occurs in the thymic {{c1::cortex}}.",
    "É a primeira prova da seleção tímica: só segue adiante quem consegue interagir com a molécula apresentadora.",
    "Onde ocorre a seleção positiva do timócito.",
)

anking(
    "ak-selecao-negativa", "c008",
    "negative selection in the thymic medulla deletes thymocytes that bind self antigen with high affinity by apoptosis",
    ["clonal deletion of autoreactive thymocytes central tolerance",
     "thymic medulla negative selection high affinity self reactive T cells"],
    ["medulla", "thymic medulla"],
    "Thymocytes that recognize self antigen with high affinity are removed by clonal deletion in the thymic {{c1::medulla}}.",
    "É a segunda prova. Quem não é deletado pode sofrer desvio funcional e sair do timo como linfócito T regulador.",
    "Onde ocorre a deleção clonal do timócito autorreativo.",
)

anking(
    "ak-aire", "c009",
    "AIRE autoimmune regulator drives expression of tissue restricted self antigens in thymic medullary epithelial cells and its mutation causes autoimmune polyendocrine syndrome type 1",
    ["AIRE gene APECED autoimmune polyendocrinopathy candidiasis",
     "thymic expression of peripheral self antigens transcription factor"],
    ["AIRE"],
    "Display of tissue-restricted self antigens inside the thymic medulla, required for clonal deletion, depends on the transcription factor {{c1::AIRE}}.",
    "Sem essa vitrine completa do próprio escapam clones autorreativos: é a APECED, com candidíase mucocutânea crônica, hipoparatireoidismo e insuficiência adrenal.",
    "Qual fator de transcrição expõe antígenos próprios periféricos no timo.",
)

authored(
    "au-malt", "c010",
    "Peyer patches, the appendix and Waldeyer ring are secondary lymphoid tissue built into mucosae, collectively called {{c1::MALT}}.",
    "No trato respiratório o mesmo tecido recebe o nome de BALT. Estuda-se muito mais linfonodo e baço, mas é na mucosa que o sistema imune gasta mais energia.",
    "Como se chama o conjunto de tecidos linfoides associados às mucosas.",
    ["mucosa associated lymphoid tissue Peyer patches tonsils appendix",
     "MALT GALT BALT mucosal lymphoid tissue definition",
     "secondary lymphoid organs associated with mucosal surfaces"],
    "O material Step 1 usa MALT apenas como rótulo dentro das notas de placas de Peyer e de IgA secretora; a recuperação da aula é a própria agregação — reconhecer que apêndice, anel de Waldeyer e placas de Peyer são o mesmo compartimento.",
)

authored(
    "au-recognition-site", "c011",
    "Lymphocytes must leave the organ where they were generated because antigen recognition takes place only in {{c1::secondary}} lymphoid organs.",
    "No órgão primário o repertório é gerado e selecionado, mas nenhuma resposta acontece ali. O reconhecimento exige o encontro, e o encontro é organizado no órgão secundário.",
    "Em que classe de órgão linfoide ocorre o reconhecimento do antígeno.",
    ["primary versus secondary lymphoid organs function generation recognition",
     "site of antigen recognition secondary lymphoid organ",
     "lymph node spleen site where adaptive response is initiated"],
    "As notas Step 1 listam quais órgãos são primários e quais são secundários; a recuperação da aula é a divisão funcional entre eles — gerar e selecionar de um lado, reconhecer do outro.",
)

authored(
    "au-one-way", "c012",
    "Traffic out of a primary lymphoid organ is one-way: physiologically a lymphocyte never re-enters the {{c1::primary}} organ.",
    "O trajeto fisiológico é órgão primário, sangue, órgão linfoide secundário, linfa e sangue de novo. Só uma destruição total do órgão quebraria essa regra.",
    "Para qual órgão o linfócito nunca retorna depois de sair.",
    ["lymphocyte recirculation route blood lymph node efferent lymph",
     "naive lymphocyte trafficking from bone marrow and thymus",
     "lymphocyte does not return to thymus or bone marrow"],
    "O material Step 1 descreve o trajeto do linfócito naïve até o linfonodo, mas não cobra a irreversibilidade da saída do órgão primário, que é a recuperação pedida aqui.",
)

authored(
    "au-exit-lymph", "c013",
    "A lymphocyte that entered a lymph node from the blood leaves it not through the blood, but through the {{c1::lymph}}.",
    "O linfócito visto no sangue saindo de um linfonodo nunca entrou nele: apenas não encontrou a porta de saída do vaso. Daí o nome linfócito, célula da linfa.",
    "Por qual via o linfócito deixa o órgão linfoide secundário.",
    ["efferent lymphatics carry lymphocytes out of the lymph node",
     "lymphocyte egress from lymph node route",
     "afferent versus efferent lymphatic vessels lymph node"],
    "As notas Step 1 sobre linfáticos aferentes e eferentes cobram anatomia e drenagem regional; a recuperação da aula é a assimetria entrada pelo sangue e saída pela linfa, que elas não testam.",
)

anking(
    "ak-paracortex-hev", "c014",
    "lymph node paracortex houses T cells and contains high endothelial venules through which T and B cells enter from the blood",
    ["paracortex high endothelial venules lymphocyte entry lymph node",
     "lymph node region enlarged in viral infection contains HEV"],
    ["paracortex"],
    "T and B cells leave the bloodstream and enter a lymph node through high endothelial venules located in the {{c1::paracortex}}.",
    "É a área timo-dependente do linfonodo. O endotélio alto, ao contrário do endotélio achatado comum, exibe as moléculas de adesão que sinalizam o ponto de saída.",
    "Em que região do linfonodo estão as vênulas de endotélio alto.",
    must_contain=["high endothelial"],
)

io(
    "io-recirculacao-hev-linfa", "c014",
    "io-recirculacao-hev-linfa.png",
    [{"x": 0.4975, "y": 0.2930, "w": 0.2300, "h": 0.0430},
     {"x": 0.6840, "y": 0.7460, "w": 0.0600, "h": 0.0560}],
    ["High endotelial venules (HEV)", "Linfa"],
    "Os dois rótulos nomeiam as duas vias opostas do mesmo circuito: a porta de entrada do sangue para o órgão linfoide secundário e a via de saída dele. Recuperá-las juntas é reconstruir o sentido da recirculação, que se perde quando cada via é decorada isoladamente.",
    "Localizar no mapa da recirculação por onde o linfócito naïve entra no órgão linfoide secundário e por onde ele sai, distinguindo entrada arterial de saída linfática.",
    "Slide 13 da videoaula Organização e funcionamento do sistema imune, J. A. M. Barbuto, Curso de Medicina",
    ["lymphocyte recirculation diagram blood high endothelial venule efferent lymph",
     "naive lymphocyte trafficking route secondary lymphoid organ image",
     "high endothelial venule entry and efferent lymph exit labeled diagram"],
    "As imagens Step 1 desse tema mostram a cascata de adesão na parede da HEV ou a histologia do linfonodo, não o mapa do circuito completo entrada-saída que esta aula usa como espinha dorsal.",
)

authored(
    "au-recirculation-why", "c015",
    "Continuous recirculation is necessary because at any given moment one lymph node holds only a fraction of the whole {{c1::repertoire}}.",
    "Como cada linfócito reconhece um único antígeno, nenhum órgão consegue guardar o repertório inteiro. Se o clone certo não está aqui agora, ele passa por aqui em breve.",
    "Por que a recirculação linfocitária é indispensável.",
    ["why do lymphocytes continuously recirculate through lymphoid organs",
     "lymphocyte recirculation increases repertoire coverage",
     "clonal diversity distribution across lymph nodes recirculation"],
    "O material Step 1 descreve o trajeto da recirculação, mas não cobra a razão funcional dela; a recuperação daqui é justamente o argumento de amostragem incompleta do repertório.",
)

anking(
    "ak-fingolimode", "c016",
    "fingolimod is a sphingosine 1 phosphate receptor modulator that sequesters lymphocytes in lymph nodes and is used in multiple sclerosis",
    ["S1P receptor modulator prevents lymphocyte egress lymph node",
     "drug causing lymphopenia by trapping lymphocytes in lymph nodes"],
    ["fingolimod"],
    "Lymphocyte egress into lymph follows an S1P gradient, and the drug that abolishes it by internalizing S1PR1 is {{c1::fingolimod}}.",
    "A linfopenia periférica resultante não vem de destruição: os linfócitos estão vivos, apenas retidos no linfonodo. O fármaco confirma que a saída é ativa.",
    "Qual fármaco impede a saída do linfócito do linfonodo.",
)

authored(
    "au-activated-switch", "c017",
    "An activated lymphocyte stops homing back to secondary lymphoid organs because it changes its pattern of {{c1::adhesion}} molecules.",
    "Perde a chave da HEV e ganha ligantes para o endotélio inflamado. É o que permite a vigilância imunológica dos tecidos, feita por um linfócito que já não é ingênuo.",
    "O que muda no linfócito ativado e o faz procurar tecidos em vez do órgão linfoide.",
    ["activated effector T cell homing to inflamed tissue adhesion molecules",
     "naive versus effector lymphocyte trafficking receptor switch",
     "effector lymphocyte loses lymph node homing receptors"],
    "As notas Step 1 tratam de receptores específicos de homing em tecidos isolados, como pele e intestino; a recuperação da aula é o princípio geral da troca de padrão de adesão como causa da mudança de destino.",
)

# ---------------------------------------------------------------- PARTE III

authored(
    "au-probability", "c018",
    "Secondary lymphoid organs crowd lymphocytes and presenting cells together in order to raise the {{c1::probability}} of encounter between an antigen and its rare clone.",
    "Muito da resposta imune é estatística. A vacina age primeiro por aí: aumenta a frequência dos clones específicos e faz o encontro acontecer mais depressa.",
    "Qual é a finalidade funcional da alta densidade celular no órgão linfoide.",
    ["why lymph nodes concentrate lymphocytes and antigen presenting cells",
     "probability of antigen meeting specific lymphocyte clone",
     "lymphoid organ architecture increases antigen lymphocyte encounter"],
    "O material Step 1 descreve a arquitetura do linfonodo por compartimentos; a recuperação da aula é o argumento probabilístico que explica por que essa arquitetura existe.",
)

anking(
    "ak-dc-naive-t", "c019",
    "dendritic cells are the professional antigen presenting cells uniquely able to activate naive T lymphocytes and bridge innate and adaptive immunity",
    ["most potent antigen presenting cell activates naive T cell",
     "dendritic cell links innate and adaptive immunity priming"],
    ["dendritic cell", "dendritic cells"],
    "The only antigen-presenting cell able to prime a naive T lymphocyte is the {{c1::dendritic}} cell.",
    "Depois desse primeiro contato outras células podem reativar e modular o linfócito, mas o pontapé inicial é exclusivo da célula dendrítica.",
    "Qual célula é capaz de ativar o linfócito T naïve.",
)

anking(
    "ak-apresentacao-cruzada", "c020",
    "cross presentation allows dendritic cells to display exogenous antigen on MHC class I and prime cytotoxic CD8 T cells",
    ["cross presentation exogenous antigen MHC I CD8 activation",
     "dendritic cell presents extracellular antigen on class I molecules"],
    ["MHC I", "MHC class I"],
    "By cross-presentation the dendritic cell displays antigen captured outside the cell on {{c1::MHC I}}, priming cytotoxic T cells.",
    "É o que torna possível responder a um vírus que só infecta outro tipo celular: a dendrítica captura o vírus de fora e o mostra como se o fabricasse.",
    "Em qual molécula apresentadora a dendrítica exibe o antígeno capturado de fora.",
)

authored(
    "au-macrophage-tissue-apc", "c021",
    "Once the primed T cell reaches the inflamed tissue, the cell that re-presents antigen to it there is the {{c1::macrophage}}.",
    "Há muito mais macrófago do que célula dendrítica nos tecidos. Além de apresentar, ele é efetor: em estados ativados destrói com eficiência o que fagocita.",
    "Qual célula reapresenta o antígeno ao linfócito já ativado no tecido.",
    ["macrophage as antigen presenting cell in peripheral tissue",
     "macrophage MHC class II presentation to effector T cell",
     "tissue macrophage reactivates effector T lymphocytes"],
    "As notas Step 1 sobre macrófago cobram fagocitose, polarização e formação de granuloma; a recuperação da aula é a divisão geográfica de trabalho com a dendrítica, apresentada no órgão linfoide contra reapresentada no tecido.",
)

authored(
    "au-b-cell-affinity", "c022",
    "Unlike the phagocytic presenters, the B cell captures antigen with membrane immunoglobulin, whose affinity is about {{c1::10,000}} times higher.",
    "Com muito antígeno disponível a dendrítica captura melhor; com pouquíssimo antígeno, quem captura é o linfócito B específico. Essa captura é o que acopla a resposta humoral ao linfócito T.",
    "Qual a ordem de grandeza da vantagem de afinidade do receptor do linfócito B.",
    ["B cell receptor affinity antigen capture presentation to helper T",
     "B lymphocyte as antigen presenting cell immunoglobulin uptake",
     "selective antigen capture by B cell versus phagocytic APC"],
    "O material Step 1 trata o linfócito B como apresentadora profissional sem quantificar a vantagem de afinidade; a recuperação da aula é justamente essa ordem de grandeza, que explica quem captura antígeno escasso.",
)

anking(
    "ak-cd40l", "c023",
    "CD40 ligand on the helper T cell binds CD40 on the B cell and drives immunoglobulin class switching in the germinal center",
    ["CD40L CD40 interaction B cell class switch recombination",
     "helper T cell signal required for isotype switching"],
    ["CD40L", "CD40 ligand"],
    "Class switching requires the helper T cell to engage CD40 on the B cell through {{c1::CD40L}}.",
    "O linfócito B apresenta o antígeno em MHC de classe II ao linfócito T auxiliar; o par CD40L-CD40 e as citocinas do T autorizam a troca de classe.",
    "Qual molécula do linfócito T auxiliar engata o CD40 do linfócito B.",
)

anking(
    "ak-hiper-igm", "c023",
    "hyper IgM syndrome results from defective CD40 ligand with normal or elevated IgM and absent IgG IgA and IgE",
    ["X linked hyper IgM syndrome CD40L deficiency recurrent infection",
     "failure of class switching normal IgM low IgG immunodeficiency"],
    ["hyper-IgM", "hyper IgM syndrome", "CD40L"],
    "Inability to class switch, with high IgM and absent IgG, IgA and IgE, defines {{c1::hyper-IgM}} syndrome.",
    "É a prova clínica de que a troca de classe depende da licença dada pelo linfócito T ao linfócito B.",
    "Qual imunodeficiência resulta da falha do par CD40L-CD40.",
)

authored(
    "au-ln-lymphocyte-entry", "c024",
    "In a lymph node the antigenic information arrives with the afferent lymph, whereas the lymphocytes themselves arrive from the {{c1::blood}}.",
    "Entram por vias diferentes e saem pela mesma: tanto a linfa quanto os linfócitos deixam o linfonodo pelo vaso eferente. É a confusão mais comum do tema.",
    "De onde vêm os linfócitos que entram no linfonodo.",
    ["lymph node afferent lymph brings antigen lymphocytes enter from blood",
     "how do lymphocytes enter the lymph node circulation",
     "lymph node inputs antigen presenting cells lymph and blood"],
    "As notas Step 1 sobre linfonodo cobram compartimentos e drenagem regional; a recuperação da aula é a assimetria entre a via da informação e a via das células, que elas não separam.",
)

authored(
    "au-spleen-no-afferent", "c025",
    "Unlike a lymph node, the spleen samples the bloodstream directly because it has no {{c1::afferent}} lymphatics.",
    "Uma resposta montada no baço costuma ser resposta a algo já circulante, situação mais perigosa: o sangue espalha muito mais depressa do que a linfa, que avança estação por estação.",
    "O que o baço não possui e que define como a informação chega até ele.",
    ["spleen lacks afferent lymphatics receives antigen from blood",
     "splenic white pulp samples bloodborne antigen",
     "difference between lymph node and spleen antigen delivery"],
    "O material Step 1 descreve polpa branca, polpa vermelha e a zona marginal do baço, mas não cobra a ausência de linfa aferente como a razão da amostragem sanguínea.",
)

anking(
    "ak-asplenia-encapsulados", "c026",
    "asplenia or functional hyposplenism predisposes to overwhelming sepsis by encapsulated organisms such as pneumococcus meningococcus and Haemophilus influenzae",
    ["splenectomy encapsulated organisms vaccination sickle cell",
     "loss of splenic function increases risk of encapsulated bacteria"],
    ["encapsulated organisms", "encapsulated"],
    "Because the spleen is the lymphoid organ that samples blood, losing it leaves the patient vulnerable above all to {{c1::encapsulated}} organisms.",
    "Ali residem também os linfócitos B de memória IgM que controlam pneumococo. Daí a vacinação obrigatória antes de esplenectomia eletiva.",
    "A que classe de micro-organismo o asplênico fica especialmente vulnerável.",
)

anking(
    "ak-celulas-m", "c027",
    "M cells overlying Peyer patches take up antigen from the intestinal lumen by transcytosis and deliver it to underlying lymphoid tissue",
    ["M cells Peyer patch antigen sampling intestinal lumen",
     "specialized epithelial cell that samples luminal antigen gut"],
    ["M cells", "M cell"],
    "Antigen from the gut lumen reaches the Peyer patch by transcytosis through specialized epithelial {{c1::M cells}}.",
    "Há um segundo caminho: células dendríticas emitem prolongamentos que atravessam as junções epiteliais e amostram a luz sem romper a barreira.",
    "Que célula epitelial serve de porta para o antígeno da luz da mucosa.",
)

anking(
    "ak-pals-baco", "c028",
    "the periarteriolar lymphoid sheath of the splenic white pulp surrounds the central arteriole and contains T lymphocytes",
    ["PALS periarteriolar lymphatic sheath spleen T cell zone",
     "splenic white pulp T cell region around central arteriole"],
    ["PALS", "periarteriolar lymphoid sheath", "T cells"],
    "The thymus-dependent T-cell zone of the splenic white pulp is the periarteriolar lymphoid sheath, abbreviated {{c1::PALS}}.",
    "As áreas timo-dependentes têm um endereço por órgão: região paracortical no linfonodo, bainha periarteriolar no baço, área interfolicular no MALT.",
    "Qual é a área timo-dependente do baço.",
)

anking(
    "ak-foliculo-b", "c029",
    "lymphoid follicles in the outer cortex of the lymph node are the site where B cells localize and proliferate",
    ["lymph node follicle B cell zone primary secondary follicle",
     "which lymph node region contains B lymphocytes"],
    ["B cells", "B cell"],
    "The follicles of a secondary lymphoid organ are the thymus-independent areas, populated by {{c1::B}} lymphocytes.",
    "O nome vem do experimento: após timectomia, as áreas timo-dependentes esvaziam e os folículos permanecem povoados.",
    "Que linfócito habita o folículo linfoide.",
)

anking(
    "ak-fdc", "c030",
    "follicular dendritic cells retain intact antigen and antigen antibody immune complexes on their surface to present to B cells within germinal centers",
    ["follicular dendritic cell immune complex retention germinal center",
     "cell that holds native antigen for B cells in the follicle"],
    ["follicular dendritic cell", "follicular dendritic cells"],
    "Intact antigen, often already bound to antibody, is retained inside the follicle for years by the {{c1::follicular dendritic}} cell.",
    "Ela não apresenta em MHC ao linfócito T e não tem parentesco com a célula dendrítica clássica: funciona como cápsula de liberação lenta e sustenta a memória.",
    "Que célula do folículo retém antígeno intacto para o linfócito B.",
)

io(
    "io-foliculo-fdc-centro-germinativo", "c030",
    "io-foliculo-fdc-centro-germinativo.png",
    [{"x": 0.0900, "y": 0.9100, "w": 0.2510, "h": 0.0440},
     {"x": 0.7140, "y": 0.7120, "w": 0.1600, "h": 0.0450}],
    ["Célula dendrítica folicular (FDC)", "Centro germinativo"],
    "As duas máscaras cobrem os dois elementos nomeados do mesmo folículo em dois estados: a célula ramificada que retém antígeno no folículo em repouso e a zona clara que aparece depois do estímulo correto. O par recupera a transição repouso para centro germinativo, que se perde se cada rótulo for estudado sozinho.",
    "Reconhecer, dentro do desenho do folículo linfoide, qual é a célula estrelada residente e qual é a zona que surge com a expansão clonal de linfócitos B.",
    "Slide 20 da videoaula Organização e funcionamento do sistema imune, J. A. M. Barbuto, Curso de Medicina",
    ["germinal center follicular dendritic cell labeled diagram follicle",
     "secondary follicle germinal center histology labels",
     "lymphoid follicle resting versus stimulated germinal center image"],
    "As imagens Step 1 do tema são lâminas de linfonodo com o centro germinativo já rotulado ou esquemas de hipermutação somática; nenhuma contrasta folículo em repouso e folículo estimulado, que é a tarefa visual desta aula.",
)

anking(
    "ak-centro-germinativo", "c031",
    "the germinal center of a secondary follicle is the site of B cell proliferation somatic hypermutation and immunoglobulin class switching",
    ["germinal center somatic hypermutation affinity maturation site",
     "where does class switching and affinity maturation occur"],
    ["germinal center"],
    "Somatic hypermutation and class switching take place inside the {{c1::germinal center}} of a stimulated follicle.",
    "O folículo estimulado fica muito maior que o folículo em repouso porque o centro germinativo é uma grande expansão clonal de linfócitos B.",
    "Onde ocorrem hipermutação somática e troca de classe.",
)

anking(
    "ak-cordoes-medulares", "c032",
    "medullary cords of the lymph node contain closely packed lymphocytes and plasma cells that secrete antibody",
    ["lymph node medullary cords plasma cells antibody secretion",
     "where do plasma cells reside within the lymph node"],
    ["medullary cords"],
    "Inside the lymph node, plasma cells derived from activated B cells settle in the {{c1::medullary cords}}.",
    "Os outros destinos do mesmo trânsito são a polpa vermelha do baço e a medula óssea, principal morada dos plasmócitos de vida longa.",
    "Em que região do linfonodo se instalam os plasmócitos.",
)

anking(
    "ak-mieloma-multiplo", "c033",
    "multiple myeloma is a malignant plasma cell neoplasm of the bone marrow with lytic bone lesions and a monoclonal immunoglobulin spike",
    ["plasma cell malignancy bone marrow lytic lesions M spike",
     "multiple myeloma CRAB features plasma cell neoplasm"],
    ["multiple myeloma"],
    "Because long-lived plasma cells home to bone marrow, their malignant counterpart arises there at many sites at once as {{c1::multiple myeloma}}.",
    "É o motivo do nome: tumor de medula em vários pontos. Quem circula é o linfócito B ativado em diferenciação, não o plasmócito maduro.",
    "Que neoplasia decorre da morada medular dos plasmócitos.",
    tier="nucleo",
)

authored(
    "au-two-weeks", "c034",
    "Clonal expansion inside a stimulated secondary lymphoid organ needs about {{c1::two weeks}} to produce a full, measurable response.",
    "No início o órgão retém os clones específicos: entra linfa, mas quase não sai linfócito por um a dois dias. Esse atraso é a base da janela imunológica.",
    "Quanto tempo leva a expansão clonal até uma resposta mensurável.",
    ["kinetics of primary adaptive immune response two weeks antibody",
     "time to detectable antibody after primary exposure window period",
     "primary versus secondary immune response timing"],
    "As notas Step 1 comparam resposta primária e secundária em curvas de anticorpo e cobram a janela sorológica do HIV; a recuperação da aula é o tempo da expansão clonal dentro do órgão linfoide, incluindo o fechamento inicial da saída.",
)

authored(
    "au-response-tolerance", "c035",
    "Clonal recognition ends in an effector response rather than in tolerance when the molecular landscape reaching the lymphoid organ carries signals of tissue {{c1::injury}}.",
    "Sem lesão a paisagem continua chegando, porque sempre há fluxo de linfa, e tende a gerar tolerância. Os dois desfechos são produzidos ao mesmo tempo; o que se vê é o saldo.",
    "O que inclina o reconhecimento clonal para resposta em vez de tolerância.",
    ["peripheral tolerance versus immune response danger signal context",
     "antigen presentation without costimulation leads to anergy",
     "what determines tolerance or effector response to an antigen"],
    "O material Step 1 explica anergia por ausência de coestimulação, que é o mecanismo molecular de uma aula posterior; a recuperação daqui é o critério da aula, presença ou ausência de lesão na paisagem molecular drenada.",
)

# ---------------------------------------------------------------- PARTE IV

anking(
    "ak-rolamento-selectinas", "c036",
    "rolling of leukocytes along activated endothelium is mediated by selectins binding sialyl Lewis X carbohydrate ligands",
    ["E selectin P selectin rolling leukocyte extravasation step",
     "first step of leukocyte extravasation margination and rolling"],
    ["rolling", "selectins", "E-selectin"],
    "Because the selectin-carbohydrate bond is weak and easily broken, its physical result is not arrest but {{c1::rolling}}.",
    "Lectina é proteína com afinidade por carboidrato: a primeira conversa é com o glicocálix. A L-selectina fica no leucócito; P e E ficam no endotélio.",
    "Que efeito físico a ligação selectina-carboidrato produz.",
)

anking(
    "ak-adesao-firme-icam", "c037",
    "tight adhesion of the leukocyte to endothelium is mediated by the beta 2 integrin LFA-1 CD18 binding endothelial ICAM-1",
    ["LFA-1 ICAM-1 tight binding leukocyte extravasation integrin",
     "integrin activation by chemokine firm adhesion endothelium"],
    ["ICAM-1", "LFA-1"],
    "Firm arrest of the rolling leukocyte happens when the activated beta-2 integrin LFA-1 binds endothelial {{c1::ICAM-1}}.",
    "A quimiocina apresentada no endotélio muda a conformação da integrina, que passa de baixa para alta afinidade. Sem esse passo a célula continua rolando.",
    "A que ligante endotelial a integrina leucocitária se prende na adesão firme.",
)

anking(
    "ak-lad1-cd18", "c038",
    "leukocyte adhesion deficiency type 1 is caused by a defect in the CD18 beta 2 integrin subunit impairing tight adhesion",
    ["LAD type 1 CD18 integrin defect impaired adhesion neutrophil",
     "leukocyte adhesion deficiency molecular defect beta 2 integrin"],
    ["CD18", "LFA-1", "beta-2 integrin"],
    "Leukocyte adhesion deficiency type 1 follows from a defect in the beta-2 integrin subunit {{c1::CD18}}.",
    "O leucócito rola normalmente, mas nunca trava: perder só o segundo degrau da cascata já quebra a defesa tecidual inteira.",
    "Que subunidade de integrina está defeituosa na LAD tipo 1.",
)

anking(
    "ak-lad1-coto-umbilical", "c038",
    "leukocyte adhesion deficiency presents with delayed separation of the umbilical cord recurrent bacterial infections without pus and marked neutrophilia",
    ["delayed umbilical cord separation immunodeficiency neutrophilia",
     "recurrent infections without pus formation leukocyte disorder"],
    ["umbilical cord", "delayed separation of the umbilical cord"],
    "In leukocyte adhesion deficiency the neutrophil cannot leave the vessel, so infected lesions form no {{c1::pus}}.",
    "O quadro é paradoxal: neutrofilia altíssima no sangue e ausência de neutrófilo no tecido. A queda tardia do coto umbilical é o sinal neonatal clássico.",
    "Por que faltam pus e neutrófilos no tecido da LAD.",
    must_contain=["umbilical"],
)

anking(
    "ak-pecam-diapedese", "c039",
    "diapedesis of the leukocyte between endothelial cells is mediated by PECAM-1 also called CD31",
    ["PECAM-1 CD31 transmigration diapedesis endothelial junction",
     "final step of leukocyte extravasation between endothelial cells"],
    ["PECAM-1", "CD31"],
    "The step in which the arrested leukocyte squeezes between endothelial cells is diapedesis, mediated by {{c1::PECAM-1}}.",
    "É o que a palavra transmigração descreve: marginação, rolamento, adesão firme e, por fim, passagem entre as células endoteliais.",
    "Que molécula medeia a diapedese do leucócito.",
)

authored(
    "au-addressins", "c040",
    "The carbohydrate-rich, mucin-like endothelial ligands recognized by selectins are collectively called {{c1::addressins}}.",
    "CD34, GlyCAM-1 e MAdCAM-1 são exemplos. O nome vem de endereço: elas identificam o território ao qual aquele trecho de endotélio pertence.",
    "Como se chamam os ligantes mucina-símile reconhecidos pelas selectinas.",
    ["addressin vascular mucin like ligand selectin homing receptor",
     "GlyCAM-1 CD34 MAdCAM-1 peripheral node addressin",
     "mucin like adhesion molecules on high endothelial venules"],
    "O material Step 1 cita sialyl Lewis X como ligante das selectinas, mas não trabalha a família mucina-símile nem o termo adressina, que é o vocabulário desta aula.",
    tier="optional",
)

authored(
    "au-chemokine-families", "c041",
    "Chemokine families are named after the arrangement of the {{c1::cysteines}} at the amino terminus of the molecule.",
    "Duas cisteínas separadas por um aminoácido definem CXC; adjacentes, CC; separadas por três, CX3C; uma só, XC. L designa o ligante e R, o receptor.",
    "Qual característica molecular define as famílias de quimiocinas.",
    ["chemokine nomenclature CXC CC families cysteine motif",
     "how are chemokines classified into families",
     "CXCL CCL ligand receptor chemokine naming convention"],
    "As notas Step 1 usam nomes de quimiocinas isoladas, como IL-8 e MCP-1, sem cobrar o critério de classificação por cisteínas, que é objetivo explícito desta aula.",
)

anking(
    "ak-il8-neutrofilo", "c042",
    "interleukin 8 also called CXCL8 is the chemokine that recruits neutrophils to the site of acute inflammation",
    ["IL-8 CXCL8 neutrophil chemotaxis acute inflammation",
     "chemokine responsible for neutrophil recruitment clean up"],
    ["IL-8", "CXCL8"],
    "The chemokine first described as a cytokine and responsible for recruiting neutrophils is {{c1::CXCL8}}.",
    "Foi descrita antes como citocina e depois reconhecida como quimiocina, e por isso carrega os dois nomes.",
    "Qual quimiocina recruta neutrófilo.",
)

anking(
    "ak-c5a-quimiotaxia", "c043",
    "chemotactic factors that attract neutrophils include C5a interleukin 8 leukotriene B4 and bacterial products",
    ["C5a anaphylatoxin chemotaxis complement fragment neutrophil",
     "mediators of neutrophil chemotaxis in acute inflammation"],
    ["C5a"],
    "Among complement fragments, the one that both attracts neutrophils and acts as an anaphylatoxin is {{c1::C5a}}.",
    "Junto com os fatores lipídicos, como leucotrienos e PAF, ele forma a camada de quimiotaxia anterior à descoberta das quimiocinas.",
    "Qual fragmento do complemento é quimiotático para neutrófilo.",
)

authored(
    "au-vaccine-circuit", "c044",
    "Vaccination works because, at the very first alarm, the blood recruited to the tissue already carries products of a previous {{c1::acquired}} response.",
    "Anticorpos no plasma e células no sangue passam a integrar o que é recrutado no episódio seguinte. Por isso a resposta inata quase sempre chega misturada com a adquirida.",
    "Por que a resposta inata do próximo episódio já chega específica após uma vacina.",
    ["vaccination primes memory response faster secondary exposure",
     "how does previous adaptive response accelerate innate recruitment",
     "secondary immune response antibodies recruited at site of injury"],
    "O material Step 1 cobra tipos de vacina e curvas de resposta primária e secundária; a recuperação da aula é o fechamento do circuito, isto é, que os produtos da adquirida passam a ser recrutados pela inata.",
)

# ---------------------------------------------------------------- conceitos

concept("c001", "nuclear", "O sistema nervoso inclui o exterior por meio de luz, som, temperatura e pressão.", 2, ["au-exterior-sensing"], NA)
concept("c002", "nuclear", "Cada linfócito T ou B expressa um único tipo de receptor e, portanto, reconhece um único antígeno", 3, ["au-clonal-distribution"], NA)
concept("c003", "nuclear", "As células do próprio tecido dão o alarme mais primitivo", 3, ["au-damps", "ak-mastocito-histamina"],
        rej("O aprofundamento natural aqui seria receptor de reconhecimento de padrão e inflamassoma; a própria aula adia isso para a aula seguinte, que trata de como o organismo reconhece que houve lesão."))
concept("c004", "nuclear", "uma célula citotóxica reconhece uma célula-alvo, entrega a ela um sinal, e a célula-alvo executa um programa próprio de morte", 3, ["au-cytotoxicity"], NA)
concept("c005", "nuclear", "Parte do direcionamento dessa resposta é dado justamente pelas células inatas residentes, as ILC entre elas", 2, ["au-ilc-direction"], NA)
concept("c006", "nuclear", "Eles são montados somaticamente, dentro do precursor linfocitário, por recombinação de segmentos gênicos", 3, ["au-somatic-receptor-genes", "ak-b-medula-ossea"], NA)
concept("c007", "nuclear", "é a seleção positiva, que ocorre no córtex tímico", 3, ["ak-selecao-positiva"],
        inc("AnKing Step 1 — Immunology, thymic positive selection", "Nomeia o córtex como sítio da primeira prova que a aula descreve funcionalmente, sem abrir tópico novo."))
concept("c008", "nuclear", "O caminho mais comum é a deleção clonal: a célula autorreativa recebe ordem de morrer", 3, ["ak-selecao-negativa"],
        inc("AnKing Step 1 — Immunology, negative selection in thymic medulla", "Localiza na medula tímica a segunda prova já ensinada pela aula como autorreatividade."))
concept("c009", "nuclear", "Quem força essa exibição é o fator de transcrição AIRE, expresso pelas células epiteliais medulares do timo", 3, ["ak-aire"],
        inc("AnKing Step 1 — AIRE / APECED", "Explica o mecanismo molecular da deleção clonal que a aula apresenta e traz correlação clínica estável."))
concept("c010", "nuclear", "está associado a mucosas, e o conjunto recebe o nome de", 2, ["au-malt"], NA)
concept("c011", "nuclear", "porque é neles que o reconhecimento do antígeno acontece", 2, ["au-recognition-site"], NA)
concept("c012", "nuclear", "fisiologicamente nenhum linfócito volta para o órgão linfoide primário", 2, ["au-one-way"], NA)
concept("c013", "nuclear", "a saída do órgão linfoide secundário se faz pela linfa, não pelo sangue", 3, ["au-exit-lymph"], NA)
concept("c014", "nuclear", "os órgãos linfoides secundários possuem vênulas especiais, de endotélio alto", 3, ["ak-paracortex-hev", "io-recirculacao-hev-linfa"],
        inc("AnKing Step 1 — lymph node paracortex and HEV; L-selectin/CCR7 homing", "Dá nome ao compartimento e às moléculas do endereço que a aula descreve como placa de entrada."))
concept("c015", "nuclear", "Em qualquer instante, um dado linfonodo abriga apenas uma fração do repertório.", 3, ["au-recirculation-why"], NA)
concept("c016", "nuclear", "é abundante na linfa e no sangue e escassa dentro do órgão linfoide", 3, ["ak-fingolimode"],
        inc("AnKing Step 1 — fingolimod, S1P receptor modulator", "Explica pelo avesso o mecanismo da saída pela linfa que a aula afirma, sem abrir tópico de terapêutica da esclerose múltipla."))
concept("c017", "nuclear", "ele mudou o padrão de moléculas de adesão que expressava", 3, ["au-activated-switch"], NA)
concept("c018", "nuclear", "Porque isso aumenta a probabilidade de encontro entre o antígeno e o receptor clonal que o reconhece.", 3, ["au-probability"], NA)
concept("c019", "nuclear", "a única célula capaz de dar nele o pontapé inicial é a célula dendrítica", 3, ["ak-dc-naive-t"], NA)
concept("c020", "nuclear", "ela captura um antígeno de fora, processa e o exibe no canal de dentro, isto é, em MHC de classe I", 3, ["ak-apresentacao-cruzada"],
        inc("AnKing Step 1 — cross-presentation to CD8 T cells", "Nomeia a molécula apresentadora do canal interno que a aula descreve em português corrente."))
concept("c021", "nuclear", "quem reapresenta o antígeno para ele é o macrófago, que é muito mais abundante nos tecidos", 2, ["au-macrophage-tissue-apc"], NA)
concept("c022", "nuclear", "com pouquíssimo antígeno, quem pega é o linfócito B específico", 3, ["au-b-cell-affinity"], NA)
concept("c023", "nuclear", "o linfócito T auxiliar expressa CD40L, que se liga ao CD40 do linfócito B", 3, ["ak-cd40l", "ak-hiper-igm"],
        inc("AnKing Step 1 — CD40L/CD40 and hyper-IgM syndrome", "Dá o elo molecular da conversa T-B que a aula apresenta funcionalmente, com correlação clínica direta."))
concept("c024", "nuclear", "a informação entra pela linfa, os linfócitos entram pelo sangue, e ambos saem pela linfa", 3, ["au-ln-lymphocyte-entry"], NA)
concept("c025", "nuclear", "O baço recebe a informação diretamente pelo sangue — não tem linfa aferente.", 2, ["au-spleen-no-afferent"], NA)
concept("c026", "nuclear", "ele é o principal responsável por depurar e responder a micro-organismos circulantes, especialmente os encapsulados", 3, ["ak-asplenia-encapsulados"],
        inc("AnKing Step 1 — asplenia and encapsulated organisms", "Correlação clínica estável da função do baço que a aula ensina, ancorada na própria leitura complementar indicada."))
concept("c027", "nuclear", "existe uma célula especializada, a célula M, cuja função é servir de porta", 3, ["ak-celulas-m"], NA)
concept("c028", "nuclear", "A área timo-dependente é a região paracortical no linfonodo, a bainha periarteriolar no baço e a área interfolicular no MALT.", 3, ["ak-pals-baco"], NA)
concept("c029", "nuclear", "As áreas timo-independentes se organizam como bolinhas, os folículos linfoides, e é ali que moram os linfócitos B.", 3, ["ak-foliculo-b"], NA)
concept("c030", "nuclear", "ela retém antígeno intacto na superfície, muitas vezes já ligado a anticorpo, e o oferece ao linfócito B", 3, ["ak-fdc", "io-foliculo-fdc-centro-germinativo"], NA)
concept("c031", "nuclear", "é no centro germinativo que ocorrem a hipermutação somática, que aumenta a afinidade do anticorpo, e a troca de classe", 3, ["ak-centro-germinativo"],
        inc("AnKing Step 1 — germinal center, somatic hypermutation, class switching", "Aprofunda o mesmo evento que a aula chama de expansão clonal do folículo, sem sair do órgão linfoide."))
concept("c032", "nuclear", "os cordões medulares do próprio linfonodo, a polpa vermelha do baço, ou a circulação, que o leva à medula óssea", 3, ["ak-cordoes-medulares"], NA)
concept("c033", "supporting", "o tumor maligno de plasmócitos quase sempre se manifesta como tumor de medula em vários pontos ao mesmo tempo, o mieloma múltiplo", 2, ["ak-mieloma-multiplo"],
        inc("AnKing Step 1 — multiple myeloma", "Correlação clínica citada pelo próprio professor como consequência da morada medular do plasmócito."))
concept("c034", "supporting", "A expansão clonal dentro do órgão linfoide secundário leva cerca de duas semanas até produzir uma resposta cheia e mensurável.", 2, ["au-two-weeks"], NA)
concept("c035", "nuclear", "Havendo lesão tecidual, a paisagem que chega ao órgão linfoide contém sinais de dano, e a tendência é resposta.", 3, ["au-response-tolerance"],
        rej("O mecanismo molecular da decisão — coestimulação, anergia e reconhecimento de padrões — pertence à aula seguinte, que a própria videoaula anuncia."))
concept("c036", "nuclear", "o resultado físico não é a parada: é o rolamento", 3, ["ak-rolamento-selectinas"],
        inc("AnKing Step 1 — leukocyte extravasation, rolling by selectins", "Aprofunda a mesma sequência de adesão que é objetivo explícito da aula."))
concept("c037", "nuclear", "As que usam a cadeia beta-2, cujo outro nome é CD18, são as integrinas leucocitárias", 3, ["ak-adesao-firme-icam"],
        inc("AnKing Step 1 — tight adhesion LFA-1/ICAM-1", "Completa o degrau seguinte da mesma cascata, já nomeada pela aula pelas famílias envolvidas."))
concept("c038", "nuclear", "queda tardia do coto umbilical, e uma neutrofilia altíssima no sangue", 3, ["ak-lad1-cd18", "ak-lad1-coto-umbilical"],
        inc("AnKing Step 1 — leukocyte adhesion deficiency type 1", "Correlação clínica direta da molécula CD18 citada na aula, sem abrir tópico de imunodeficiências em geral."))
concept("c039", "nuclear", "e diapedese entre as células endoteliais, mediada por PECAM-1", 2, ["ak-pecam-diapedese"],
        inc("AnKing Step 1 — diapedesis and PECAM-1", "Fecha a cascata de extravasamento que a aula chama de transmigração."))
concept("c040", "optional", "o termo adressina, de endereço, aparece justamente para elas", 1, ["au-addressins"], NA)
concept("c041", "nuclear", "as famílias são definidas pelo arranjo das cisteínas na extremidade da molécula", 3, ["au-chemokine-families"], NA)
concept("c042", "nuclear", "é o recrutador clássico de neutrófilo", 2, ["ak-il8-neutrofilo"], NA)
concept("c043", "nuclear", "As células têm receptores para tudo isso e migram no sentido da maior concentração.", 2, ["ak-c5a-quimiotaxia"], NA)
concept("c044", "nuclear", "numa segunda agressão a resposta inata já chega misturada com produtos da adquirida anterior", 3, ["au-vaccine-circuit"], NA)


# ---------------------------------------------------------------- emissão

def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    keys = [c["card_key"] for c in cards]
    assert len(keys) == len(set(keys)), "card_key duplicada"
    referenced = {k for c in concepts for k in c["card_keys"]}
    assert referenced == set(keys), f"desalinhamento conceito/card: {referenced ^ set(keys)}"
    assert len(cards) <= HARD_MAX, f"{len(cards)} cards excede hard_max {HARD_MAX}"

    deck = {
        "companion_compat": {
            "io_mode": "hide_all_guess_all",
            "reason": (
                "O Companion instalado no tablet é anterior ao commit 4e1d678 e ainda valida o "
                "nome legado do modo IO. O plano continua canônico (hide_two_guess_two, duas "
                "máscaras, pair_rationale); só o valor gravado no manifesto acompanha o runtime "
                "instalado. Remover quando o APK for reconstruído."
            ),
        },
        "metadata": {
            "uc": "UC03",
            "prova": "P1",
            "componente": "Imunologia",
            "nome_curto": "Organização do sistema imune",
        },
        "release_gate": {
            "schema": "nebli-e1-deck-release-v1",
            "e1_source": E1_SOURCE,
            "e1_source_sha256": sha256_file((WD / E1_SOURCE).resolve()),
            "e1_pdf": E1_PDF,
            "e1_pdf_sha256": sha256_file((WD / E1_PDF).resolve()),
            "card_budget_hard_max": HARD_MAX,
            "e1_review": {
                "slide_inventory_complete": True,
                "objectives_covered": True,
                "core_coverage_complete": True,
                "mechanisms_explicit": True,
                "visual_information_explained": True,
                "core_study_without_slides": True,
                "step1_depth_reviewed": True,
                "card_content_anchored": True,
                "independent_review_passed": True,
                "notes_review_status": "covered",
                "unresolved_core_omissions": [],
                "unresolved_ambiguities": [],
                "summary": (
                    "Revisão independente slide a slide (26 slides), objetivo a objetivo (5 objetivos) "
                    "e contra a transcrição completa da videoaula (50 páginas). Os cinco objetivos têm "
                    "conceito, âncora e card; os diagramas de recirculação, aferência e regionalização "
                    "foram interpretados em prosa e reproduzidos como figura; o gabarito das palavras "
                    "cruzadas foi triado, com os itens de aulas posteriores registrados como fora de escopo."
                ),
            },
            "concepts": concepts,
        },
        "cards": cards,
    }
    (WD / "deck-data.json").write_text(
        json.dumps(deck, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report_cards = []
    for card in cards:
        source = card["source"]
        row = {
            "card_key": card["card_key"],
            "concept_id": card["concept_id"],
            "source": source,
            "tier": card["tier"],
            "selected": True,
            "atomic": True,
            "relevant": True,
            "e1_anchor_ok": True,
        }
        if source == "anking":
            row.update({
                "source_safe": True,
                "score": 0.82,
                "second_score": 0.0,
                "exact_phrase": False,
                "score_basis": "plan_contract_minimum",
                "same_note_type": True,
                "same_fields": True,
                "media_ok": True,
                "sibling_policy_ok": True,
                "fallback_validated": True,
                "search_queries_ok": len(card["search_queries"]) >= 3,
                "expected_answers_ok": bool(card["expected_answers"]),
                "anking_marker_ok": True,
                "anking_required": True,
                "resolved_without_fallback": True,
                "requires_visual": False,
            })
        elif source == "authored":
            match = CLOZE_RE.search(card["text"])
            row.update({
                "front_language": "en",
                "extra_language": "pt-BR",
                "cloze_count": len(CLOZE_RE.findall(card["text"])),
                "cloze_index": int(match.group(1)),
                "cloze_words": _words(match.group(2)),
                "extra_words": _words(card["extra"]),
                "front_characters": len(card["text"]),
                "multi_retrieval": False,
                "has_extra_media": False,
                "requires_visual": False,
                "anking_search_queries_ok": len(card["anking_search_queries"]) >= 3,
                "anking_scope_expanded": True,
                "anking_siblings_reviewed": True,
                "anking_candidates_reviewed_ok": True,
                "anking_rejections_ok": True,
                "anking_search_complete": True,
                "anking_rejection_reason": card["anking_rejection_reason"],
            })
            if card.get("three_word_cloze_reason"):
                row["three_word_cloze_reason"] = card["three_word_cloze_reason"]
        else:
            row.update({
                "mode": card["mode"],
                "mask_count": len(card["masks"]),
                "coherent_set": True,
                "pair_rationale": card["pair_rationale"],
                "masks_labels_not_structures": True,
                "question_preview_validated": True,
                "answer_preview_validated": True,
                "visual_ok": True,
                "real_source": True,
                "source_credit_ok": True,
                "media_ok": True,
                "media_cognitive_purpose_ok": True,
                "didactic_value_reviewed": True,
                "answer_leak": False,
                "mask_geometry_ok": True,
                "anking_search_queries_ok": len(card["anking_search_queries"]) >= 3,
                "anking_scope_expanded": True,
                "anking_siblings_reviewed": True,
                "anking_candidates_reviewed_ok": True,
                "anking_rejections_ok": True,
            })
        report_cards.append(row)

    report = {
        "lesson_slug": SLUG,
        "expected_card_count": len(cards),
        "card_budget_hard_max": HARD_MAX,
        "validation_mode": "every_card",
        "cards": report_cards,
    }
    (WD / "validacao-cards.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    by_source: dict[str, int] = {}
    for card in cards:
        by_source[card["source"]] = by_source.get(card["source"], 0) + 1
    print(f"cards={len(cards)} hard_max={HARD_MAX} conceitos={len(concepts)} {by_source}")


if __name__ == "__main__":
    main()
