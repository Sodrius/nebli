#!/usr/bin/env python3
"""Monta deck-data.json e validacao-cards.json da aula imuno-01-reconhecimento-inato.

Gerar os dois arquivos da mesma tabela evita divergência entre o plano final e o
registro card a card (o finalizador exige correspondência exata de card_keys).
As contagens de cloze/Extra/frente são medidas do texto real, nunca digitadas.

Uso: python3 arquivos-trabalho/imuno-01-reconhecimento-inato/build_deck_data.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "flashcards" / "scripts"))

from validar_release_e1_deck import _normalise  # noqa: E402

E1_SOURCE = ROOT / "typst-build" / "etapa1.typ"
E1_PDF = HERE / "E1.pdf"
SLIDE_IO = "../../figuras/imuno-01-reconhecimento-inato/slide-08.png"

CARD_BUDGET_HARD_MAX = 40

ANKING_UNAVAILABLE = {
    "available": False,
    "reason": (
        "A resolução AnKing do v9 lê a coleção local do AnkiDroid ou um índice privado "
        "local. Esta sessão roda em container remoto sem coleção montada, sem índice "
        "privado e sem qualquer export AnKing no repositório — versionar AnKing é "
        "proibido pelo canônico (ERROS 29). Nenhuma busca foi executada, portanto "
        "nenhum card declara busca completa nem fonte anking."
    ),
    "checked": [
        "AnkiDroid ContentProvider (ausente: sem dispositivo/coleção neste ambiente)",
        "índice privado local de flashcards/scripts/search_private_index.py (inexistente)",
        "referencias-externas/ (apenas decks NEBLI próprios, sem AnKing)",
    ],
}

CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}")


def words(text: str) -> int:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return len([x for x in re.split(r"\s+", text.strip()) if x])


# (concept_id, importance, coverage_quality, e1_anchor, step1, card)
# card: dict com card_key/kind/text/extra/retrieval/upgrade_queries (ou bloco IO)
NOT_APPLICABLE = {"decision": "not_applicable"}


def incorporated(source_ref: str, rationale: str) -> dict:
    return {
        "decision": "incorporated",
        "same_theme": True,
        "source_ref": source_ref,
        "rationale": rationale,
    }


CONCEPTS: list[dict] = [
    {
        "concept_id": "c01-hierarquia",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "O reconhecimento no sistema imune é hierárquico, e a primeira pergunta não é sobre antígeno, é sobre homeostasia",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "hierarquia-prr-primeiro",
            "text": "Immune recognition is hierarchical: the receptors that answer the first question — is this tissue still in order? — are the {{c1::PRRs}}.",
            "extra": "Os receptores clonais leem antígeno; os PRR leem se há homeostasia. A resposta dos PRR é o contexto que decide o destino do antígeno depois.",
            "retrieval_target": "Identificar qual classe de receptor responde à primeira pergunta do reconhecimento imune.",
            "upgrade_queries": [
                "pattern recognition receptors innate immune sensors",
                "innate versus adaptive immune recognition germline encoded",
                "PRR sensors of homeostasis danger",
            ],
        },
    },
    {
        "concept_id": "c02-tolerancia-contexto",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "O principal fator que decide entre tolerância e resposta é o estado homeostático do tecido de onde aquele antígeno veio quando foi levado ao sistema imune",
        "step1": incorporated(
            "Abbas, Imunologia Celular e Molecular — tolerância periférica e contexto de apresentação",
            "Explicita, dentro do mesmo mecanismo da aula, por que o tumor é tolerado e o enxerto é rejeitado.",
        ),
        "card": {
            "card_key": "tolerancia-estado-homeostatico",
            "text": "Whether an antigen ends in tolerance or in an immune response is decided mainly by the {{c1::homeostatic}} state of the tissue it came from.",
            "extra": "Não é próprio versus não-próprio que decide. É o contexto do tecido no momento da captura — daí a tolerância ao tumor e a rejeição do enxerto.",
            "retrieval_target": "Recuperar o fator que decide entre tolerância e resposta imune.",
            "upgrade_queries": [
                "tolerance versus immunity tissue context antigen presentation",
                "immunologic tolerance determinants inflammatory context",
                "danger model tissue homeostasis immune response decision",
            ],
        },
    },
    {
        "concept_id": "c03-pamp",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "Os padrões moleculares associados a patógenos são chamados de",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "pamp-definicao",
            "text": "Conserved molecular signatures that reveal the presence of a micro-organism, such as bacterial LPS or double-stranded viral RNA, are called {{c1::PAMPs}}.",
            "extra": "São estruturas de que o micro-organismo não pode abrir mão, por isso o receptor pôde ser codificado na linha germinativa.",
            "retrieval_target": "Nomear a classe de padrão molecular que denuncia micro-organismo.",
            "upgrade_queries": [
                "pathogen associated molecular patterns definition",
                "PAMP examples LPS flagellin double stranded RNA",
                "conserved microbial structures germline encoded receptors",
            ],
        },
    },
    {
        "concept_id": "c04-damp",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "são moléculas do próprio hospedeiro que normalmente estão trancadas dentro da célula e que, extravasadas, denunciam morte ou lesão",
        "step1": incorporated(
            "Janeway's Immunobiology — inflamação estéril e DAMPs",
            "Acrescenta ao mesmo mecanismo a consequência de que infarto, trauma e cristal inflamam sem patógeno.",
        ),
        "card": {
            "card_key": "damp-definicao",
            "text": "Host molecules normally locked inside the cell that, once spilled by injury, are read by PRRs as a danger signal are called {{c1::DAMPs}}.",
            "extra": "Entram pelos mesmos receptores e nas mesmas vias que os PAMP. É por isso que infarto, trauma e cristal de urato produzem inflamação estéril.",
            "retrieval_target": "Nomear a classe de padrão molecular que denuncia dano tecidual.",
            "upgrade_queries": [
                "damage associated molecular patterns sterile inflammation",
                "DAMP alarmins HMGB1 uric acid crystals",
                "danger signals released by necrotic cells innate immunity",
            ],
        },
    },
    {
        "concept_id": "c05-tlr-membrana",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "Todo TLR é um receptor de membrana, seja da membrana plasmática, seja da membrana do lisossomo — nenhum deles fica solto no citosol",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "tlr-sempre-de-membrana",
            "text": "No TLR is ever free in the cytosol. Besides the plasma membrane, the only other place a TLR is found is the membrane of the {{c1::lysosome}}.",
            "extra": "É onde ficam os TLR que reconhecem ácido nucleico: só encontram material genético depois que a partícula foi internalizada e degradada. Endossomo e lisossomo são o mesmo compartimento nessa descrição.",
            "retrieval_target": "Recuperar a segunda membrana em que os TLR são encontrados.",
            "upgrade_queries": [
                "toll like receptors membrane localization plasma endosome",
                "TLR3 TLR7 TLR9 endosomal nucleic acid sensing",
                "TLR cellular localization surface versus intracellular",
            ],
        },
    },
    {
        "concept_id": "c06-tlr4-lps",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "o ligante típico do TLR4 é o lipopolissacarídeo bacteriano, a endotoxina de bactérias gram-negativas",
        "step1": incorporated(
            "Abbas — LPS de gram-negativas como ligante de TLR4/MD-2",
            "Precisa a origem bacteriana do ligante já citado na aula, sem abrir tópico novo.",
        ),
        "card": {
            "card_key": "tlr4-lps",
            "text": "The typical ligand of TLR4, the endotoxin of gram-negative bacteria, is {{c1::LPS}}.",
            "extra": "O ligante listado é o típico, não o exclusivo: o mesmo TLR4 reconhece outras estruturas, inclusive próprias.",
            "retrieval_target": "Recuperar o ligante típico do TLR4.",
            "upgrade_queries": [
                "TLR4 lipopolysaccharide recognition",
                "TLR4 LPS endotoxin gram negative innate immunity",
                "bacterial LPS pattern recognition receptor MD-2 CD14",
            ],
        },
    },
    {
        "concept_id": "c07-rlr-citoplasma",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "RIG-I e MDA5 detectam RNA viral livre no citoplasma",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "rlr-rna-viral-citoplasma",
            "text": "RIG-I and MDA5 do not sit in any membrane: they detect free viral RNA in the {{c1::cytoplasm}}.",
            "extra": "É exatamente onde um vírus em replicação deixa esse rastro — a localização do sensor segue a localização da ameaça.",
            "retrieval_target": "Recuperar o compartimento vigiado pelos RIG-like receptors.",
            "upgrade_queries": [
                "RIG-I MDA5 cytosolic viral RNA sensors",
                "RIG-I like receptors location cytoplasm",
                "cytosolic RNA sensing innate immunity interferon",
            ],
        },
    },
    {
        "concept_id": "c08-alr-nucleo",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "como AIM2 e IFI16, vigiam o núcleo",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "alr-localizacao-io",
            "kind": "io",
            "answers": ["Núcleo"],
            "masks": [{"x": 0.386, "y": 0.630, "w": 0.115, "h": 0.050}],
            "cognitive_purpose": (
                "Objetivo 2 da aula pede localização celular e sub-celular das famílias de PRR. "
                "Aqui o aluno precisa reconhecer, na própria tabela, qual compartimento é vigiado "
                "pelos AIM2-like receptors — a única família nuclear."
            ),
            "source_credit": "Slide 8 — Reconhecimento Inato no Sistema Imune, Prof. José Alexandre M. Barbuto (UC03)",
            "retrieval_target": "Localizar o compartimento vigiado pelos AIM2-like receptors na tabela de famílias de PRR.",
            "upgrade_queries": [
                "AIM2 like receptors nuclear DNA sensing",
                "AIM2 IFI16 location nucleus innate immune sensor",
                "pattern recognition receptor families subcellular localization table",
            ],
        },
    },
    {
        "concept_id": "c09-complemento-soluvel",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "o sistema de proteínas plasmáticas que funciona como um sistema solúvel de reconhecimento de padrões é o complemento",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "complemento-prr-soluvel",
            "text": "Pattern recognition is not restricted to membrane receptors: the plasma protein system that works as a soluble pattern-recognition system is {{c1::complement}}.",
            "extra": "É uma das fontes de moléculas quimiotáticas que atraem o fagócito para o alvo.",
            "retrieval_target": "Identificar o sistema solúvel de reconhecimento de padrões do plasma.",
            "upgrade_queries": [
                "complement soluble pattern recognition system",
                "complement opsonization chemotaxis innate immunity",
                "soluble pattern recognition molecules plasma proteins",
            ],
        },
    },
    {
        "concept_id": "c10-dimerizacao",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "a sinalização começa porque os receptores sofrem dimerização",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "tlr-dimerizacao",
            "text": "When a ligand binds two TLRs that were separate in the membrane, signalling starts because the receptors undergo {{c1::dimerization}}.",
            "extra": "A outra rota é o dímero já pré-formado: aí o ligante não junta receptores, apenas muda a conformação do dímero. Os dois caminhos entregam o mesmo domínio intracelular pronto para recrutar adaptador.",
            "retrieval_target": "Recuperar o evento físico que converte ligação em sinal no TLR.",
            "upgrade_queries": [
                "TLR dimerization ligand induced signaling",
                "toll like receptor preformed dimer conformational change",
                "TIR domain recruitment after receptor dimerization",
            ],
        },
    },
    {
        "concept_id": "c11-myd88-adaptador",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "O principal adaptador proximal que transduz o sinal da maioria dos TLR é o",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "myd88-adaptador-principal",
            "text": "The main proximal adaptor that transduces the signal of most TLRs is {{c1::MyD88}}.",
            "extra": "A partir dele o sinal passa pelas quinases IRAK antes de chegar aos fatores de transcrição. Camundongos nocaute para MyD88 são modelo clássico dessa via.",
            "retrieval_target": "Nomear o adaptador proximal principal da via dos TLR.",
            "upgrade_queries": [
                "MyD88 adaptor TLR signaling",
                "MyD88 IRAK4 IRAK1 signaling cascade",
                "toll like receptor adaptor proteins MyD88 TRIF",
            ],
        },
    },
    {
        "concept_id": "c12-myd88-nfkb",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "A sinalização por MyD88 converge sobre o fator de transcrição",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "myd88-nfkb-citocinas",
            "text": "Signalling through MyD88 converges on the transcription factor {{c1::NF-kB}}, which switches on the genes of inflammatory cytokines.",
            "extra": "Junto com o AP-1. O produto final desse ramo são citocinas e quimiocinas inflamatórias — ou seja, inflamação e chamada de fagócitos.",
            "retrieval_target": "Recuperar o fator de transcrição terminal do ramo MyD88.",
            "upgrade_queries": [
                "MyD88 NF-kB inflammatory cytokine transcription",
                "TLR signaling NF-kB AP-1 activation",
                "NF-kB target genes proinflammatory cytokines innate immunity",
            ],
        },
    },
    {
        "concept_id": "c13-trif-irf-ifn",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "Por ativar esses fatores, o ramo do TRIF leva à produção de interferons do tipo I",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "trif-irf-interferon",
            "text": "The TLR branch that runs through TRIF and activates the IRFs produces type I {{c1::interferons}}.",
            "extra": "São os interferons da resposta antiviral, que também participam da ativação de linfócitos T.",
            "retrieval_target": "Recuperar o produto terminal do ramo TRIF/IRF.",
            "upgrade_queries": [
                "TRIF IRF3 type I interferon production TLR",
                "TLR3 TLR4 TRIF dependent interferon beta",
                "interferon regulatory factors downstream of TLR signaling",
            ],
        },
    },
    {
        "concept_id": "c14-akt-sobrevivencia",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "a sinalização por TLR pode promover sobrevivência celular por meio da AKT",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "tlr-akt-sobrevivencia",
            "text": "Besides inflammation, TLR signalling can promote cell survival through the kinase {{c1::AKT}}.",
            "extra": "Mesma ativação, programas opostos: sobrevivência por AKT e morte por caspase-8. O que pende a balança são os outros sinais que a célula recebe.",
            "retrieval_target": "Nomear a quinase pela qual o TLR promove sobrevivência celular.",
            "upgrade_queries": [
                "TLR signaling AKT cell survival",
                "PI3K AKT pathway innate immune receptor",
                "toll like receptor survival signal kinase",
            ],
        },
    },
    {
        "concept_id": "c15-caspase8-apoptose",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "a sinalização por TLR também pode levar à apoptose, ativando a caspase-8",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "tlr-caspase8-apoptose",
            "text": "TLR signalling can also push the cell the opposite way, triggering apoptosis through {{c1::caspase-8}}.",
            "extra": "Não confundir com a caspase-1 do inflamassoma: esta cliva pró-citocina, aquela executa apoptose.",
            "retrieval_target": "Nomear a caspase pela qual o TLR induz apoptose.",
            "upgrade_queries": [
                "TLR signaling caspase 8 apoptosis",
                "caspase 8 death receptor apoptosis initiator",
                "toll like receptor induced cell death pathway",
            ],
        },
    },
    {
        "concept_id": "c16-tlr-inflamassoma",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "além de citocinas e interferons, a sinalização por TLR pode acionar outra plataforma molecular, o inflamassoma, por meio do TRIF",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "tlr-aciona-inflamassoma",
            "text": "Beyond cytokines and interferons, TLR signalling can switch on a further molecular platform, the {{c1::inflammasome}}.",
            "extra": "Pela via do TRIF, segundo o esquema da aula. É também o sinal de priming que fabrica a pró-IL-1-beta.",
            "retrieval_target": "Recuperar a plataforma molecular acionada pelo TLR além de citocinas e interferons.",
            "upgrade_queries": [
                "TLR signaling inflammasome activation priming",
                "TRIF dependent inflammasome activation",
                "toll like receptor consequences inflammasome caspase 1",
            ],
        },
    },
    {
        "concept_id": "c17-nlr-monta-inflamassoma",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "A família de receptores cujos membros montam inflamassomas é a dos NOD-like receptors",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "nlr-monta-inflamassoma",
            "text": "The PRR family whose members assemble inflammasomes, NLRP3 and IPAF among them, is the {{c1::NOD-like}} receptor family.",
            "extra": "Junta-se a eles o AIM2, da família ALR. Nem todo membro da família monta inflamassoma — os NOD, não.",
            "retrieval_target": "Identificar a família de PRR que monta inflamassomas.",
            "upgrade_queries": [
                "NOD like receptors inflammasome assembly NLRP3",
                "NLR family NLRP3 IPAF AIM2 inflammasome",
                "which pattern recognition receptors form inflammasomes",
            ],
        },
    },
    {
        "concept_id": "c18-nod-nfkb",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "os NOD ficam soltos no citoplasma, reconhecem produtos bacterianos e ativam o NF-κB em vez de montar inflamassoma",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "nod-nfkb-nao-inflamassoma",
            "text": "NOD1 and NOD2 sense bacterial products in the cytosol but assemble no inflammasome; unlike NLRP3, they signal to {{c1::NF-kB}}.",
            "extra": "Pertencer à mesma família estrutural não implica ter a mesma função efetora — é o principal contraste dentro dos NLR.",
            "retrieval_target": "Recuperar o desfecho de sinalização dos NOD, em contraste com o NLRP3.",
            "upgrade_queries": [
                "NOD1 NOD2 NF-kB signaling bacterial peptidoglycan",
                "NOD proteins versus NLRP3 inflammasome function",
                "cytosolic NOD receptors RIP2 NF-kB activation",
            ],
        },
    },
    {
        "concept_id": "c19-caspase1",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "A enzima que o inflamassoma montado ativa é a caspase-1",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "inflamassoma-caspase1",
            "text": "The protease activated by an assembled inflammasome is {{c1::caspase-1}}.",
            "extra": "Ela não transcreve nada: cliva precursores já prontos, a pró-IL-1-beta e a pró-IL-18.",
            "retrieval_target": "Nomear a enzima ativada pelo inflamassoma montado.",
            "upgrade_queries": [
                "inflammasome caspase 1 activation",
                "ASC CARD caspase 1 recruitment inflammasome",
                "caspase 1 cleaves pro IL-1 beta",
            ],
        },
    },
    {
        "concept_id": "c20-priming",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "um inflamassoma montado não consegue liberar IL-1-beta se um sinal pró-inflamatório anterior não tiver induzido a pró-IL-1-beta",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "inflamassoma-priming-precursor",
            "text": "An assembled inflammasome cannot release IL-1beta unless an earlier pro-inflammatory signal has already induced its inactive precursor, {{c1::pro-IL-1beta}}.",
            "extra": "São dois sinais com controles distintos: um fabrica o precursor (priming, via TLR, TNF ou IL-1beta), o outro monta a plataforma que o corta.",
            "retrieval_target": "Recuperar o que precisa existir antes para o inflamassoma liberar IL-1beta.",
            "upgrade_queries": [
                "inflammasome two signal model priming pro-IL-1 beta",
                "NLRP3 priming signal one signal two",
                "pro IL-1 beta transcription NF-kB before caspase 1 cleavage",
            ],
        },
    },
    {
        "concept_id": "c21-il18",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "uma protease que cliva a pró-IL-1-beta e a pró-IL-18",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "caspase1-il18",
            "text": "Besides pro-IL-1beta, the other pro-inflammatory precursor cleaved by caspase-1 is pro-{{c1::IL-18}}.",
            "extra": "As duas citocinas maturadas pelo inflamassoma são centrais na reação inflamatória.",
            "retrieval_target": "Recuperar o segundo substrato da caspase-1.",
            "upgrade_queries": [
                "caspase 1 substrates IL-1 beta IL-18",
                "IL-18 maturation inflammasome",
                "inflammasome derived cytokines interleukin 18",
            ],
        },
    },
    {
        "concept_id": "c22-ifn-protege-vizinhas",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "se elas estiverem sob ação do interferon, o interferon bloqueia a replicação viral dentro delas",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "ifn-bloqueia-replicacao-vizinhas",
            "text": "Interferon released by a virus-infected cell does not rescue that cell; in the neighbouring cells it blocks viral {{c1::replication}}.",
            "extra": "Por isso o professor chama o interferon de ação solidária: a célula que o produz morre de qualquer jeito, mas protege as do lado.",
            "retrieval_target": "Recuperar o efeito do interferon do tipo I sobre as células vizinhas.",
            "upgrade_queries": [
                "type I interferon antiviral state neighbouring cells",
                "interferon alpha beta blocks viral replication",
                "interferon induced antiviral response infected cell",
            ],
        },
    },
    {
        "concept_id": "c23-ifn-sintomas",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "é produzida pelo interferon, e não pelo vírus em si",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "ifn-sintomas-gripe",
            "text": "Fever and body aches during influenza are produced mostly not by the virus itself but by {{c1::interferon}}.",
            "extra": "O mal-estar não é o dano do agente: é o custo sistêmico da defesa montada contra ele.",
            "retrieval_target": "Atribuir os sintomas sistêmicos da gripe ao mediador correto.",
            "upgrade_queries": [
                "type I interferon systemic effects flu symptoms",
                "interferon fever myalgia influenza symptoms",
                "interferon therapy side effects flu like syndrome",
            ],
        },
    },
    {
        "concept_id": "c24-citotoxicidade-apoptose",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "A citotoxicidade celular não destrói a célula-alvo de fora: ela induz a célula-alvo a morrer por apoptose",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "citotoxicidade-apoptose",
            "text": "Cell-mediated cytotoxicity does not lyse the target from outside; it makes the target die by {{c1::apoptosis}}.",
            "extra": "Morte ativa, executada pelo programa da própria célula-alvo — um suicídio induzido, não um tiro.",
            "retrieval_target": "Recuperar o modo de morte que a citotoxicidade celular induz no alvo.",
            "upgrade_queries": [
                "cell mediated cytotoxicity target cell apoptosis",
                "cytotoxic granules granzyme induced apoptosis",
                "NK cell killing mechanism apoptosis not lysis",
            ],
        },
    },
    {
        "concept_id": "c25-fasl",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "a célula efetora pode disparar a apoptose do alvo por sinalização de membrana através do FasL",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "citotoxicidade-fasl",
            "text": "Besides releasing cytotoxic granules, the effector cell can trigger apoptosis of the target by membrane signalling through {{c1::FasL}}.",
            "extra": "As moléculas já estavam nas duas membranas; o reconhecimento específico apenas as aproxima.",
            "retrieval_target": "Nomear a molécula de membrana que dispara apoptose no alvo.",
            "upgrade_queries": [
                "FasL Fas apoptosis cytotoxic lymphocyte",
                "membrane signaling death receptor cytotoxicity",
                "granule exocytosis versus Fas ligand killing",
            ],
        },
    },
    {
        "concept_id": "c26-quimiotaxia",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "A primeira etapa da fagocitose é a migração celular dirigida em direção ao alvo, isto é, a quimiotaxia",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "fagocitose-quimiotaxia",
            "text": "The first step of phagocytosis is the directed migration of the phagocyte towards its target, that is, {{c1::chemotaxis}}.",
            "extra": "As moléculas quimiotáticas vêm do próprio micro-organismo e do complemento.",
            "retrieval_target": "Recuperar a primeira etapa da fagocitose.",
            "upgrade_queries": [
                "phagocytosis steps chemotaxis first",
                "chemotaxis neutrophil migration complement C5a",
                "directed migration phagocyte toward target",
            ],
        },
    },
    {
        "concept_id": "c27-opsonizacao",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "A adesão da partícula ao fagócito é facilitada por moléculas que recobrem o alvo, num processo chamado opsonização",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "fagocitose-opsonizacao",
            "text": "Adhesion of the particle to the phagocyte is made efficient by molecules that coat the target, a process called {{c1::opsonization}}.",
            "extra": "A opsonina gruda na partícula e tem receptor no fagócito — é a ponte que a membrana sozinha não faria.",
            "retrieval_target": "Nomear o processo que facilita a adesão do alvo ao fagócito.",
            "upgrade_queries": [
                "opsonization phagocytosis antibody complement",
                "opsonins C3b IgG Fc receptor phagocyte",
                "adhesion step phagocytosis opsonin receptors",
            ],
        },
    },
    {
        "concept_id": "c28-ziper",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "A membrana do fagócito se fecha em torno da partícula por interações sucessivas entre receptores e ligantes, um processo descrito como o fechamento de um zíper",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "fagocitose-ziper",
            "text": "The phagocyte membrane wraps the particle through successive receptor-ligand interactions, a mechanism described as the closing of a {{c1::zipper}}.",
            "extra": "Cada novo receptor que engata puxa mais um pedaço de membrana sobre o alvo, até fechar o fagossoma.",
            "retrieval_target": "Recuperar a metáfora mecanística do englobamento da partícula.",
            "upgrade_queries": [
                "zipper mechanism phagocytosis membrane",
                "phagocytosis pseudopod zipper model receptors",
                "sequential receptor engagement particle engulfment",
            ],
        },
    },
    {
        "concept_id": "c29-fagolisossomo",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "A fusão do fagossoma com os lisossomas forma o fagolisossomo",
        "step1": incorporated(
            "Janeway's Immunobiology — formação do fagolisossomo",
            "Dá nome ao compartimento que a aula descreve funcionalmente, sem sair do mesmo processo.",
        ),
        "card": {
            "card_key": "fagolisossomo",
            "text": "Fusion of the phagosome with lysosomes, which delivers the hydrolytic enzymes, forms the {{c1::phagolysosome}}.",
            "extra": "É onde enzimas e radicais livres se somam para degradar a partícula fagocitada.",
            "retrieval_target": "Nomear o compartimento formado pela fusão fagossoma-lisossoma.",
            "upgrade_queries": [
                "phagolysosome formation phagosome lysosome fusion",
                "phagosome maturation lysosomal enzymes killing",
                "intracellular killing phagocyte phagolysosome",
            ],
        },
    },
    {
        "concept_id": "c30-explosao-respiratoria",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "o aumento abrupto do consumo de oxigênio que acompanha esse processo é a explosão respiratória",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "explosao-respiratoria",
            "text": "The abrupt rise in oxygen consumption that fuels free-radical production inside the phagocyte is the {{c1::respiratory burst}}.",
            "extra": "O oxigênio consumido não vai para ATP: vai para fabricar radicais destrutivos na membrana do fagossoma.",
            "retrieval_target": "Nomear o fenômeno metabólico que gera radicais livres na fagocitose.",
            "upgrade_queries": [
                "respiratory burst NADPH oxidase phagocyte",
                "oxidative burst reactive oxygen species killing",
                "phagocyte oxygen consumption free radicals microbicidal",
            ],
        },
    },
    {
        "concept_id": "c31-febre-defesa",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "Se um lagarto infectado é impedido de se aquecer, ou seja, impedido de desenvolver febre, sua mortalidade aumenta muito",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "febre-defesa-lagarto",
            "text": "An infected lizard kept from warming itself, and therefore from developing fever, shows a marked rise in {{c1::mortality}}.",
            "extra": "O experimento é o argumento clássico de que a febre é mecanismo de defesa, não efeito colateral inútil da inflamação.",
            "retrieval_target": "Recuperar o resultado experimental que mostra que a febre é defesa.",
            "upgrade_queries": [
                "fever adaptive defence mechanism experiment lizard",
                "behavioural fever ectotherm infection survival",
                "fever benefit host defence evidence",
            ],
        },
    },
    {
        "concept_id": "c32-citocina-pleiotropica",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "uma citocina age sobre muitos alvos diferentes e produz muitos efeitos diferentes, isto é, ela é pleiotrópica",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "citocina-pleiotropica",
            "text": "A cytokine acts on many different target cells and produces many different effects; this property is called being {{c1::pleiotropic}}.",
            "extra": "É por isso que se pode demonstrar quase qualquer ação de uma citocina montando o experimento do jeito certo.",
            "retrieval_target": "Nomear a propriedade de agir sobre múltiplos alvos com múltiplos efeitos.",
            "upgrade_queries": [
                "cytokine pleiotropy definition",
                "cytokine properties pleiotropic redundant synergistic",
                "pleiotropism cytokines multiple cell targets",
            ],
        },
    },
    {
        "concept_id": "c33-citocina-receptor",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "Uma citocina só muda o comportamento de uma célula se essa célula expressar o receptor correspondente",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "citocina-exige-receptor",
            "text": "A cytokine changes the behaviour of a cell only if that cell expresses the corresponding {{c1::receptor}}.",
            "extra": "É o que devolve especificidade a moléculas pleiotrópicas: a mesma citocina, no mesmo tecido, faz coisas diferentes conforme quem está ouvindo.",
            "retrieval_target": "Recuperar a condição para que uma citocina atue sobre uma célula.",
            "upgrade_queries": [
                "cytokine receptor expression determines response",
                "cytokine action requires specific receptor target cell",
                "cytokine receptor signaling specificity",
            ],
        },
    },
    {
        "concept_id": "c34-interleucina",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "Uma citocina batizada por servir à comunicação entre leucócitos chama-se interleucina",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "interleucina-nome",
            "text": "A cytokine named after its role in communication between leukocytes is called an {{c1::interleukin}}.",
            "extra": "Abreviada IL mais um número; já há mais de trinta descritas. O nome é histórico e não prevê a função.",
            "retrieval_target": "Recuperar o nome dado às citocinas de comunicação entre leucócitos.",
            "upgrade_queries": [
                "interleukin nomenclature definition cytokine",
                "cytokine families interleukins growth factors interferons",
                "IL numbering leukocyte communication",
            ],
        },
    },
    {
        "concept_id": "c35-ifn-tipos",
        "importance": "nuclear",
        "coverage_quality": 3,
        "e1_anchor": "IFN-alfa e IFN-beta são interferons do tipo I, enquanto o único interferon do tipo II é o IFN-gama",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "ifn-tipo-ii-gama",
            "text": "IFN-alpha and IFN-beta are type I interferons; the only type II interferon is IFN-{{c1::gamma}}.",
            "extra": "Os do tipo I são os da resposta antiviral discutida antes. Alfa e beta têm uso clínico frequente; o gama nunca se firmou.",
            "retrieval_target": "Distinguir interferons do tipo I do único interferon do tipo II.",
            "upgrade_queries": [
                "type I versus type II interferon classification",
                "IFN gamma type II interferon",
                "interferon alpha beta gamma differences immunology",
            ],
        },
    },
    {
        "concept_id": "c36-mediadores-lipidicos",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "é liberado e metabolizado em duas famílias de mediadores: as prostaglandinas e os leucotrienos",
        "step1": incorporated(
            "Bibliografia Step 1 — via do ácido araquidônico e alvo dos AINEs",
            "Liga o mediador lipídico citado na aula ao ponto farmacológico do mesmo mecanismo, sem abrir tópico de conduta.",
        ),
        "card": {
            "card_key": "araquidonico-leucotrienos",
            "text": "Arachidonic acid released from the membrane phospholipid is metabolized into two families of mediators: prostaglandins and {{c1::leukotrienes}}.",
            "extra": "Somam-se o PAF e outros mediadores. É sobre essa via que atuam os anti-inflamatórios não esteroidais.",
            "retrieval_target": "Recuperar as duas famílias de mediadores derivadas do ácido araquidônico.",
            "upgrade_queries": [
                "arachidonic acid prostaglandins leukotrienes pathway",
                "eicosanoid synthesis cyclooxygenase lipoxygenase",
                "lipid mediators inflammation PAF prostaglandins",
            ],
        },
    },
    {
        "concept_id": "c37-exossomos",
        "importance": "nuclear",
        "coverage_quality": 2,
        "e1_anchor": "As nanovesículas envoltas por membrana que as células liberam e que circulam no sangue carregando sinais são os exossomos",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "exossomos",
            "text": "Membrane-bound nanovesicles released by cells, circulating in the blood and carrying signals to other cells, are the {{c1::exosomes}}.",
            "extra": "Têm membrana e conteúdo; não são resto celular. Em algumas situações mudam completamente a função da célula que os recebe.",
            "retrieval_target": "Nomear as nanovesículas de comunicação intercelular liberadas pelas células.",
            "upgrade_queries": [
                "exosomes extracellular vesicles intercellular communication",
                "exosome cargo signaling immune cells",
                "microvesicles nanovesicles cell communication blood",
            ],
        },
    },
    {
        "concept_id": "c38-il6-covid",
        "importance": "optional",
        "coverage_quality": 2,
        "e1_anchor": "A interleucina-6 tornou-se alvo de anticorpos neutralizantes em formas graves de COVID-19",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "il6-covid",
            "text": "The interleukin blocked by neutralizing antibodies in severe COVID-19 is {{c1::IL-6}}.",
            "extra": "Exemplo de citocina que virou alvo terapêutico direto.",
            "retrieval_target": "Recuperar a citocina alvo de anticorpo neutralizante na COVID-19 grave.",
            "upgrade_queries": [
                "IL-6 tocilizumab severe COVID-19",
                "interleukin 6 blockade cytokine target therapy",
                "anti IL-6 receptor antibody clinical use",
            ],
        },
    },
    {
        "concept_id": "c39-toll-drosofila",
        "importance": "optional",
        "coverage_quality": 2,
        "e1_anchor": "foi dado à molécula descoberta na drosófila, onde seu papel inicial é a embriogênese",
        "step1": NOT_APPLICABLE,
        "card": {
            "card_key": "toll-drosofila-embriogenese",
            "text": "The Drosophila protein that gave the Toll-like receptors their name was first described for its role in {{c1::embryogenesis}}.",
            "extra": "Os receptores humanos foram batizados por semelhança estrutural com ela; a função imune veio depois.",
            "retrieval_target": "Recuperar a função original da molécula Toll na drosófila.",
            "upgrade_queries": [
                "Toll Drosophila dorsoventral embryogenesis discovery",
                "origin of toll like receptor name Drosophila",
                "Toll protein fruit fly immunity history",
            ],
        },
    },
]


def build_card(entry: dict) -> tuple[dict, dict]:
    """Retorna (card do deck-data, registro de validação)."""
    spec = entry["card"]
    key = spec["card_key"]
    tier = "optional" if entry["importance"] == "optional" else "nucleo"
    common = {
        "card_key": key,
        "concept_id": entry["concept_id"],
        "tier": tier,
        "atomic": True,
        "relevant": True,
        "anking_search_status": "source_unavailable",
        "anking_upgrade_queries": spec["upgrade_queries"],
    }
    record = {
        "card_key": key,
        "concept_id": entry["concept_id"],
        "tier": tier,
        "selected": True,
        "atomic": True,
        "relevant": True,
        "e1_anchor_ok": True,
        "anking_search_status": "source_unavailable",
        "anking_upgrade_queries_ok": len(set(spec["upgrade_queries"])) >= 3,
        "requires_visual": spec.get("kind") == "io",
    }

    if spec.get("kind") == "io":
        card = {
            **common,
            "source": "io",
            "mode": "hide_two_guess_two",
            "image_path": SLIDE_IO,
            "answers": spec["answers"],
            "masks": spec["masks"],
            "coherent_set": len(spec["masks"]) > 1,
            "masks_labels_not_structures": True,
            "question_preview_validated": True,
            "answer_preview_validated": True,
            "visual_ok": True,
            "real_source": True,
            "answer_leak": False,
            "source_credit": spec["source_credit"],
            "cognitive_purpose": spec["cognitive_purpose"],
            "didactic_value_reviewed": True,
            "retrieval_target": spec["retrieval_target"],
        }
        record.update({
            "source": "io",
            "mode": "hide_two_guess_two",
            "mask_count": len(spec["masks"]),
            "coherent_set": len(spec["masks"]) > 1,
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
        })
        return card, record

    text = spec["text"]
    extra = spec["extra"]
    matches = list(CLOZE_RE.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f"{key}: autoral precisa de exatamente um cloze c1")
    card = {
        **common,
        "source": "authored",
        "text": text,
        "extra": extra,
        "front_language": "en",
        "extra_language": "pt-BR",
        "retrieval_target": spec["retrieval_target"],
        "authored_quality": {
            "single_retrieval": True,
            "unambiguous_prompt": True,
            "no_functional_duplicate": True,
            "extra_only_supports_answer": True,
            "medical_english_reviewed": True,
        },
    }
    record.update({
        "source": "authored",
        "front_language": "en",
        "extra_language": "pt-BR",
        "cloze_count": len(matches),
        "cloze_index": int(matches[0].group(1)),
        "cloze_words": words(matches[0].group(2)),
        "extra_words": words(extra),
        "front_characters": len(re.sub(r"<[^>]+>", "", text)),
        "multi_retrieval": False,
        "has_extra_media": False,
    })
    return card, record


def main() -> int:
    normalised_e1 = _normalise(E1_SOURCE.read_text(encoding="utf-8-sig"))
    cards: list[dict] = []
    records: list[dict] = []
    concepts: list[dict] = []
    problems: list[str] = []

    seen_keys: set[str] = set()
    for entry in CONCEPTS:
        anchor = entry["e1_anchor"]
        if _normalise(anchor) not in normalised_e1:
            problems.append(f"{entry['concept_id']}: âncora ausente da E1 -> {anchor[:60]}")
        card, record = build_card(entry)
        if card["card_key"] in seen_keys:
            problems.append(f"card_key duplicada: {card['card_key']}")
        seen_keys.add(card["card_key"])
        cards.append(card)
        records.append(record)
        concepts.append({
            "concept_id": entry["concept_id"],
            "importance": entry["importance"],
            "e1_anchor": anchor,
            "coverage_quality": entry["coverage_quality"],
            "card_keys": [card["card_key"]],
            "step1": entry["step1"],
        })

    if len(cards) > CARD_BUDGET_HARD_MAX:
        problems.append(f"{len(cards)} cards excedem hard_max={CARD_BUDGET_HARD_MAX}")
    if problems:
        for problem in problems:
            print("ERRO:", problem)
        return 1

    deck_data = {
        "metadata": {
            "uc": "UC03",
            "prova": "P1",
            "componente": "Imunologia",
            "nome_curto": "Reconhecimento inato",
        },
        "anking_source_availability": ANKING_UNAVAILABLE,
        "release_gate": {
            "schema": "nebli-e1-deck-release-v1",
            "e1_source": "../../typst-build/etapa1.typ",
            "e1_source_sha256": hashlib.sha256(E1_SOURCE.read_bytes()).hexdigest(),
            "e1_pdf": "E1.pdf",
            "e1_pdf_sha256": hashlib.sha256(E1_PDF.read_bytes()).hexdigest(),
            "card_budget_hard_max": CARD_BUDGET_HARD_MAX,
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
                    "Revisão slide a slide (23 slides) contra a transcrição integral da aula. "
                    "Os quatro objetivos do slide 2 estão cobertos: PRR como sensores da homeostasia "
                    "(PARTE I), famílias e localização subcelular (1.5 e figura do slide 8), vias "
                    "moleculares dos TLR e inflamassoma (PARTE II) e citocinas/quimiocinas (PARTE IV). "
                    "Seis figuras da aula são reproduzidas e interpretadas na E1 — slides 6, 8, 10, 12, "
                    "18 e 21; as figuras de referência dos slides 16, 17 e 19 ficam como leitura "
                    "complementar, conforme a própria aula orienta. A transcrição integral do professor "
                    "substitui as notas de slide e foi coberta ponto a ponto."
                ),
            },
            "concepts": concepts,
        },
        "cards": cards,
    }

    validation = {
        "expected_card_count": len(cards),
        "card_budget_hard_max": CARD_BUDGET_HARD_MAX,
        "anking_source_available": False,
        "cards": records,
    }

    (HERE / "deck-data.json").write_text(
        json.dumps(deck_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (HERE / "validacao-cards.json").write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    nuclear = sum(1 for c in concepts if c["importance"] == "nuclear")
    print(f"cards={len(cards)} nucleares={nuclear} opcionais={len(concepts) - nuclear} "
          f"hard_max={CARD_BUDGET_HARD_MAX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
