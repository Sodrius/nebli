#!/usr/bin/env python3
"""Monta o deck-data.json da aula imuno-01-reconhecimento-inato.

Artefato interno do pipeline: mantém o plano legível e garante que os campos
repetitivos (idioma, qualidade autoral, procedência da busca) sejam idênticos
em todos os cards em vez de copiados à mão 52 vezes.
"""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO = BASE.parents[1]
E1_SOURCE = "../../typst-build/etapa1.typ"
E1_PDF = "../../typst-build/main.pdf"

DEFERRAL = (
    "Nenhuma coleção AnKing está ao alcance desta sessão de planejamento — ela vive no "
    "AnkiDroid do tablet e só o Nebli Companion a enxerga. Em vez de declarar uma busca "
    "que não aconteceu, o card foi autorado para a recuperação exata da aula."
)

QUALITY = {
    "single_retrieval": True,
    "unambiguous_prompt": True,
    "no_functional_duplicate": True,
    "extra_only_supports_answer": True,
    "medical_english_reviewed": True,
}


def a(key, concept, text, extra, target, **kw):
    """Card autoral."""
    card = {
        "card_key": key,
        "concept_id": concept,
        "source": "authored",
        "tier": "nucleo",
        "atomic": True,
        "relevant": True,
        "text": text,
        "extra": extra,
        "front_language": "en",
        "extra_language": "pt-BR",
        "retrieval_target": target,
        "authored_quality": dict(QUALITY),
        "anking_search_mode": "unavailable",
        "anking_deferral_reason": DEFERRAL,
    }
    card.update(kw)
    return card


def io(key, concept, image, masks, answers, pair, purpose, credit):
    return {
        "card_key": key,
        "concept_id": concept,
        "source": "io",
        "tier": "nucleo",
        "atomic": True,
        "relevant": True,
        "requires_visual": True,
        "mode": "hide_two_guess_two",
        "image_path": image,
        "masks": masks,
        "answers": answers,
        "coherent_set": True,
        "pair_rationale": pair,
        "cognitive_purpose": purpose,
        "source_credit": credit,
        "masks_labels_not_structures": True,
        "question_preview_validated": True,
        "answer_preview_validated": True,
        "didactic_value_reviewed": True,
        "visual_ok": True,
        "real_source": True,
        "answer_leak": False,
        "anking_search_mode": "unavailable",
        "anking_deferral_reason": DEFERRAL,
    }


CARDS = [
    # ---------------------------------------------------------- PARTE I
    a("k03-contexto", "k03",
      "Whether a presented antigen ends in elimination or in acceptance is decided by the "
      "{{c1::homeostatic}} state of the tissue it was collected from.",
      "Não é a identidade química do antígeno que decide o desfecho, e sim o contexto do tecido de onde ele veio.",
      "O fator que decide entre resposta e tolerância."),
    a("k04-memoria", "k04",
      "Not only an eliminating response but also immunological tolerance leaves lasting {{c1::memory}}.",
      "Tolerância é desfecho ativo do reconhecimento: o sistema se adapta para repetir o mesmo tratamento na próxima vez.",
      "Que tolerância também deixa memória."),
    a("k05-tolerancia", "k05",
      "When an antigen reaches the lymph node with no concurrent innate signal, the adaptive "
      "outcome is biased toward {{c1::tolerance}}.",
      "A inata autoriza a adquirida: sem sinal de perda de homeostasia, o antígeno apresentado tende a ser aceito.",
      "O desfecho adquirido na ausência de sinal inato."),
    a("k07-pamp", "k07",
      "A molecular signature restricted to microorganisms and read by ready-made innate sensors is a {{c1::PAMP}}.",
      "Pathogen associated molecular pattern — padrão molecular associado a patógeno.",
      "O nome do padrão de origem microbiana."),
    a("k08-damp", "k08",
      "Sterile inflammation after a burn, an infarction or a trauma is triggered by host molecules "
      "displaced by injury, the {{c1::DAMPs}}.",
      "É por ler DAMP que a resposta inata dispara sem que exista infecção alguma.",
      "O padrão que explica inflamação sem infecção."),

    # --------------------------------------------------------- PARTE II
    a("k10-rlr", "k10",
      "Sensors that detect replicating viral RNA free in the cytosol, such as RIG-I and MDA5, "
      "belong to the {{c1::RLR}} family.",
      "RIG-I-like receptors. O endereço citoplasmático combina com o lugar onde o vírus replica.",
      "A família de PRR exclusivamente citoplasmática de RNA."),
    a("k10-alr", "k10",
      "The PRR family described with a nuclear localization, comprising AIM2 and IFI16, is the {{c1::ALR}} family.",
      "AIM2-like receptors. É a única família da tabela cujo endereço é o núcleo.",
      "A família de PRR de localização nuclear."),
    a("k11-dectina", "k11",
      "Fungal β-glucan is recognized at the plasma membrane by the C-type lectin receptor {{c1::Dectin-1}}.",
      "Dectina-1 e Dectina-2 leem β-glucano de parede fúngica; MINCLE lê SAP130.",
      "O CLR que reconhece β-glucano."),
    a("k12-endolisossomo", "k12",
      "Every TLR that senses nucleic acid is placed in the {{c1::endolysosome}} instead of on the cell surface.",
      "Regra topológica: superfície lê lipídio e proteína; compartimento interno lê ácido nucleico.",
      "O compartimento de todos os TLR de ácido nucleico."),
    a("k12-extracelular", "k12",
      "Keeping nucleic-acid sensors inside an acidified compartment prevents reaction to host DNA, "
      "which circulates freely in the {{c1::extracellular}} space.",
      "A separação entre próprio e não-próprio, aqui, é topológica e não química — daí o elo com autoimunidade.",
      "Por que o sensor de ácido nucleico não fica na superfície."),
    a("k13-tlr4", "k13",
      "Bacterial endotoxin, LPS, is sensed at the plasma membrane by {{c1::TLR4}}.",
      "Lipopolissacarídeo da parede de Gram-negativas. A origem listada do ligante inclui vírus e próprio.",
      "O TLR que reconhece LPS."),
    a("k13-tlr5", "k13",
      "Bacterial flagellin is the typical plasma-membrane ligand of {{c1::TLR5}}.",
      "Flagelina é proteína de superfície bacteriana — coerente com um sensor voltado para fora.",
      "O TLR que reconhece flagelina."),
    a("k13-tlr2", "k13",
      "Bacterial lipoprotein, whose listed origin spans viruses, parasites and even self, is read by {{c1::TLR2}}.",
      "A coluna de origem mostra que a tabela não é uma lista de ligantes exclusivamente microbianos.",
      "O TLR que reconhece lipoproteína."),
    a("k14-tlr3", "k14",
      "Double-stranded RNA formed during viral replication is sensed inside the endolysosome by {{c1::TLR3}}.",
      "dsRNA é intermediário de replicação de muitos vírus.",
      "O TLR endolisossomal de dsRNA."),
    a("k14-tlr9", "k14",
      "Unmethylated CpG-DNA is the typical endolysosomal ligand of {{c1::TLR9}}.",
      "O DNA bacteriano e viral tem motivos CpG não metilados; o DNA próprio é metilado.",
      "O TLR endolisossomal de CpG-DNA."),
    a("k14-tlr8", "k14",
      "In humans the endolysosomal sensor of single-stranded RNA is {{c1::TLR8}}, whereas the mouse uses TLR7.",
      "Peculiaridade de espécie explicitada na aula: o humano não tem TLR7 funcional e o camundongo não tem TLR8.",
      "O sensor humano de ssRNA."),
    a("k15-tlr10", "k15",
      "Among the TLRs of the ligand table, the one still listed with an unknown ligand is {{c1::TLR10}}.",
      "A tabela traz o ligante típico de cada receptor, não uma lista exclusiva nem completa — onze receptores jamais cobririam todos os padrões existentes.",
      "O TLR cujo ligante permanece desconhecido."),
    a("k16-rigi", "k16",
      "Short double-stranded RNA bearing a 5'-triphosphate is the cytosolic ligand of {{c1::RIG-I}}.",
      "O trifosfato na extremidade 5′ é marca química que o RNA próprio maduro não tem.",
      "O RLR que lê dsRNA curto com 5′-trifosfato."),
    a("k16-mda5", "k16",
      "Long double-stranded RNA, characteristic of picornaviruses, is sensed in the cytosol by {{c1::MDA5}}.",
      "O comprimento do dsRNA separa MDA5 de RIG-I.",
      "O RLR que lê dsRNA longo."),
    a("k17-nod2", "k17",
      "Muramyl dipeptide, a fragment of bacterial peptidoglycan, is the cytosolic ligand of {{c1::NOD2}}.",
      "Variantes de perda de função no NOD2 estão entre os fatores de risco genético mais estabelecidos para doença de Crohn.",
      "O NLR citoplasmático que lê MDP."),

    # -------------------------------------------------------- PARTE III
    a("k19-dimero", "k19",
      "When a TLR already sits in the membrane as a preformed dimer, the ligand starts signalling by "
      "changing its {{c1::conformation}}.",
      "A outra possibilidade é o ligante forçar a dimerização de receptores isolados. Nos dois casos muda a geometria das caudas citoplasmáticas.",
      "Como um dímero pré-formado passa a sinalizar."),
    a("k20-myd88", "k20",
      "The adaptor recruited by most TLRs, and knocked out in mice to abolish that signalling route, "
      "is {{c1::MyD88}}.",
      "Myeloid differentiation primary response protein 88 — a rota da inflamação.",
      "O adaptador da rota inflamatória do TLR."),
    a("k21-trif", "k21",
      "The adaptor that couples TLR signalling to the IRFs, and therefore to type I interferon, "
      "is {{c1::TRIF}}.",
      "TIR domain-containing adaptor protein inducing IFN-β — a rota antiviral.",
      "O adaptador da rota antiviral do TLR."),
    io("k22-io-vias", "k22",
       "../../figuras/imuno-01-reconhecimento-inato/io-tlr-vias.png",
       [{"x": 0.415, "y": 0.532, "w": 0.062, "h": 0.052},
        {"x": 0.462, "y": 0.860, "w": 0.048, "h": 0.052}],
       ["NF-kB", "IRFs"],
       "As duas máscaras cobrem os fatores de transcrição terminais das duas rotas: o da rota que "
       "termina em citocinas inflamatórias e o da rota que termina em interferon do tipo I. "
       "Cobrar um sem o outro perde justamente a distinção entre as rotas.",
       "Localizar no mapa qual fator de transcrição pertence ao ramo inflamatório e qual pertence ao "
       "ramo do interferon, tarefa espacial que um card verbal não reproduz.",
       "Slide 18 da aula (Barbuto, Reconhecimento inato no sistema imune, UC-3), recorte sem a legenda."),
    a("k23-caspase8", "k23",
      "Besides transcription, TLR signalling can also drive cell death by activating {{c1::caspase-8}}.",
      "A mesma ativação sinaliza sobrevivência pela AKT e morte pela caspase-8 — o saldo depende do contexto.",
      "A caspase pela qual o TLR sinaliza apoptose."),
    a("k24-cruzamento", "k24",
      "Because the two adaptor routes branch and cross, a ligand acting on an essentially "
      "MyD88-coupled TLR can still end in the production of {{c1::interferon}}.",
      "Entre adaptador e fator de transcrição há muitas moléculas intermediárias, com ramificações.",
      "A consequência prática do cruzamento entre as vias."),
    a("k25-localizacao", "k25",
      "MyD88 cannot pass the signal on unless it has been actively brought close to the kinases "
      "{{c1::IRAK4}} and IRAK1.",
      "O citoplasma não é um saco homogêneo. Como a pré-ativação muda onde as moléculas estão, o mesmo estímulo pode render resultados diferentes em duas células.",
      "A quinase de que o MyD88 precisa estar perto."),
    a("k26-maturacao", "k26",
      "Unlike the transcriptional routes, the inflammasome acts on cytokines the cell already made, "
      "promoting their {{c1::maturation}}.",
      "A pró-citocina existe mas não é funcional; a plataforma corta e gera a forma ativa.",
      "A função específica da plataforma do inflamassoma."),
    a("k26-caspase1", "k26",
      "The protease activated inside the assembled platform, which cleaves pro-IL-1β into its mature "
      "form, is {{c1::caspase-1}}.",
      "A ativação se dá por proximidade, quando a plataforma junta várias pró-caspases.",
      "A enzima efetora do inflamassoma."),
    a("k26-il18", "k26",
      "The inflammasome matures IL-1β and one further pro-inflammatory cytokine, {{c1::IL-18}}.",
      "As duas citocinas maduras dependem da mesma clivagem por caspase-1.",
      "A segunda citocina madurada pelo inflamassoma."),
    a("k27-nod", "k27",
      "Despite belonging to the NLR family, the NODs assemble no platform at all: they act on gene "
      "{{c1::transcription}} through NF-κB.",
      "Dentro dos sensores citoplasmáticos há dois destinos: transcrição pelos NOD e clivagem pelos NLRP, IPAF e AIM2.",
      "O destino de sinalização dos NOD, oposto ao do inflamassoma."),
    a("k28-proil1b", "k28",
      "The priming signal of NLRP3 activation is what makes the cell synthesize {{c1::pro-IL-1β}}.",
      "Sem priming não existe substrato para cortar — a célula que recebeu só o sinal de perigo não libera IL-1β.",
      "O produto que o priming fabrica."),
    io("k29-io-nlrp3", "k29",
       "../../figuras/imuno-01-reconhecimento-inato/io-nlrp3-membrana.png",
       [{"x": 0.045, "y": 0.268, "w": 0.085, "h": 0.062},
        {"x": 0.245, "y": 0.198, "w": 0.150, "h": 0.062}],
       ["P2X7", "Pannexin-1"],
       "As duas máscaras cobrem as duas proteínas de membrana do mesmo braço do segundo sinal: o "
       "receptor que o ATP extracelular aciona e o canal por onde o potássio sai. Elas formam uma "
       "unidade funcional e são reconhecidas pela posição na membrana.",
       "Reconhecer, pela posição na membrana e pelo ligante desenhado, quais são as duas proteínas "
       "que traduzem ATP extracelular em efluxo de potássio.",
       "Schroder K, Tschopp J. The inflammasomes. Cell 2010;140(6):821–32, reproduzida no slide 21 da aula."),
    a("k29-lisossomo", "k29",
      "Crystalline and particulate ligands activate NLRP3 after being phagocytosed and causing "
      "lysosomal {{c1::rupture}}.",
      "É o mecanismo por trás da gota: cristais de urato fagocitados rompem o lisossomo e acionam o NLRP3.",
      "Como um cristal aciona o NLRP3."),
    a("k30-asc", "k30",
      "NLRP3 does not bind pro-caspase-1 directly; it reaches the protease through the adaptor {{c1::ASC}}.",
      "NLRP3 oligomeriza pelo NACHT, recruta ASC pelo PYD, e o ASC recruta a pró-caspase-1 pelo CARD.",
      "O adaptador entre o sensor e a protease."),

    # --------------------------------------------------------- PARTE IV
    a("k32-replicacao", "k32",
      "Type I interferon protects an uninfected neighbour cell by blocking, inside it, viral {{c1::replication}}.",
      "A célula que produziu o interferon será destruída assim mesmo: o que ela compra é a sobrevivência das vizinhas.",
      "O que o interferon bloqueia dentro da célula vizinha."),
    a("k32-sistemico", "k32",
      "Type I interferon does not act only where it was made; among its systemic effects, the most "
      "obvious one is {{c1::fever}}.",
      "Boa parte dos sintomas de gripe vem do interferon, e não diretamente do vírus.",
      "O efeito sistêmico mais visível do interferon."),
    a("k34-apoptose", "k34",
      "Cell-mediated cytotoxicity does not destroy the target from the outside; it induces the target "
      "cell to undergo {{c1::apoptosis}}.",
      "É um suicídio induzido — um convencimento da célula-alvo a morrer, não um tiro.",
      "O tipo de morte que a citotoxicidade celular induz."),
    a("k34-fas", "k34",
      "One cytotoxic route needs no granules at all: membrane molecules that were already there are "
      "simply brought close, as in the {{c1::FasL-Fas}} pair.",
      "Quem faz a aproximação é o próprio reconhecimento específico entre efetora e alvo.",
      "O par de membrana que mata sem desgranulação."),
    a("k34-prr", "k34",
      "A cytotoxic effector can identify its target through clonal receptors or, with no prior "
      "adaptation whatsoever, through {{c1::PRRs}}.",
      "É o elo entre esta aula e a citotoxicidade: parte do reconhecimento do alvo é inata.",
      "O receptor inato usado no reconhecimento do alvo."),
    a("k35-complemento", "k35",
      "The plasma proteins that behave as a soluble pattern-recognition system and generate "
      "chemotactic signals are known collectively as {{c1::complement}}.",
      "Nem todo PRR é de membrana: há um sistema solúvel de reconhecimento de padrões no plasma.",
      "O sistema de PRR solúvel do plasma."),
    a("k36-opsonizacao", "k36",
      "Coating a particle with host molecules for which the phagocyte carries receptors is called "
      "{{c1::opsonization}}.",
      "Encostar não basta: a partícula pode não interagir bem com a membrana do fagócito.",
      "O nome do revestimento que viabiliza a adesão."),
    a("k37-ziper", "k37",
      "The phagocyte membrane closes around the particle through successive receptor-ligand "
      "interactions, much like a {{c1::zipper}}.",
      "Motilidade da membrana e fechamento em zíper são as duas etapas explicitamente moduláveis.",
      "A metáfora mecânica do englobamento."),
    a("k37-explosao", "k37",
      "A phagocytosing cell consumes far more oxygen than a resting one because free-radical "
      "generation drives the respiratory {{c1::burst}}.",
      "A destruição do conteúdo do fagossoma soma enzimas lisossômicas e radicais livres de oxigênio.",
      "O fenômeno que explica o consumo extra de oxigênio."),
    a("k38-pleiotropica", "k38",
      "One cytokine produces many different effects depending on the target cell, which is why "
      "cytokines are described as {{c1::pleiotropic}}.",
      "É a pleiotropia que dá plasticidade à resposta — e que torna fácil demonstrar quase qualquer efeito no experimento certo.",
      "A propriedade que define o comportamento das citocinas."),
    a("k38-receptor", "k38",
      "A cytokine flooding a tissue changes only the cells that express its matching {{c1::receptor}}.",
      "Não adianta ter a citocina: quem escuta a mensagem é definido pela expressão do receptor.",
      "O que determina quais células respondem a uma citocina.",
      generic_answer_reason=(
          "A palavra é comum, mas aqui é a resposta exata e única: a frase pergunta o que "
          "seleciona as células respondedoras, e nenhum sinônimo — ligante, sinal, via — cabe "
          "na lacuna sem tornar a afirmação falsa."
      )),
    a("k40-araquidonico", "k40",
      "Prostaglandins and leukotrienes are produced when the activated cell cleaves membrane "
      "{{c1::arachidonic}} acid.",
      "O ácido araquidônico está pendurado no fosfolipídio de membrana; dele saem também o PAF.",
      "O lipídio de membrana que origina prostaglandinas e leucotrienos."),
    a("k42-cisteina", "k42",
      "Chemokines, unlike the other cytokines, are classified by structure — the arrangement of "
      "their first {{c1::cysteine}} residues.",
      "Daí as quatro famílias: CXC, CC, CX3C e XC.",
      "O critério estrutural que classifica as quimiocinas."),
    a("k42-cxcl8", "k42",
      "The chemokine also called IL-8, the clearest case of one molecule named twice, is {{c1::CXCL8}}.",
      "Foi batizada uma vez pela função entre leucócitos e outra pela estrutura.",
      "A quimiocina com nomenclatura dupla."),
    a("k43-il6", "k43",
      "The interleukin neutralized by therapeutic antibodies in severe COVID-19 is {{c1::IL-6}}.",
      "Exemplo de citocina que virou alvo clínico direto.",
      "A interleucina bloqueada na COVID-19 grave."),
    a("k44-febre", "k44",
      "In the classic lizard experiment, preventing an infected animal from warming itself raised "
      "its {{c1::mortality}}.",
      "O lagarto regula a temperatura expondo-se ao sol; impedir isso é impedir a febre. A febre é mecanismo de defesa.",
      "A evidência experimental de que a febre é defesa."),
    a("k45-modificado", "k45",
      "Pro-IL-1β cleaved into IL-1β is the example of an innate product that is only {{c1::modified}} "
      "after cell activation.",
      "Os outros três tipos são produtos já estocados, produtos sintetizados só após ativação e produtos de degradação celular.",
      "A categoria de produto que a clivagem da pró-IL-1β exemplifica."),
]

CONCEPTS = [
    ("k03", "nuclear", "O que hoje parece ser o principal fator de diferenciação é o estado homeostático do tecido de onde o antígeno veio quando foi levado ao sistema imune", 3, None),
    ("k04", "supporting", "Tanto a resposta quanto a tolerância deixam", 2, None),
    ("k05", "nuclear", "Havendo o sinal da imunidade inata, aqueles antígenos desencadeiam uma resposta imune adquirida; não havendo, o mesmo antígeno tende à tolerância", 3, None),
    ("k07", "nuclear", "Quando a assinatura molecular pertence a um micro-organismo, fala-se em", 3, None),
    ("k08", "nuclear", "É por incluir os DAMP que o sistema consegue disparar sem que exista qualquer infecção", 3, None),
    ("k10", "nuclear", "eles estão distribuídos por toda a célula, na membrana externa, nas membranas internas, soltos no citoplasma e até dentro do núcleo", 3, None),
    ("k11", "supporting", "Entre os CLR, de membrana plasmática: Dectina-1 e Dectina-2 reconhecem β-glucano de fungos", 3, None),
    ("k12", "nuclear", "Por que os TLR que leem ácido nucleico são endossomais e não de superfície?", 3,
     ("incorporated", "Abbas, Imunologia Celular e Molecular, cap. 4 — compartimentalização dos TLR de ácido nucleico",
      "Aprofunda o mesmo mecanismo do slide (localização dos TLR) explicando por que a segregação topológica existe e o que acontece quando ela falha.")),
    ("k13", "nuclear", "Na membrana plasmática: TLR1 reconhece lipoproteína triacilada de bactérias", 3, None),
    ("k14", "nuclear", "No endossomo/lisossomo: TLR3 reconhece", 3, None),
    ("k15", "nuclear", "TLR10 permanece com ligante desconhecido", 3, None),
    ("k16", "nuclear", "RIG-I reconhece dsRNA curto e dsRNA com trifosfato na extremidade 5′", 3, None),
    ("k17", "nuclear", "NOD1 reconhece iE-DAP e NOD2 reconhece", 3,
     ("incorporated", "Takeuchi O, Akira S. Cell 2010;140:805–820 — NOD2 e doença de Crohn",
      "Mantém o mesmo mecanismo (NOD2 lendo peptidoglicano no citosol) e apenas mostra a consequência de um sensor mal calibrado.")),
    ("k19", "nuclear", "O primeiro evento é mecânico, não químico.", 3, None),
    ("k20", "nuclear", "a rota MyD88 é a rota da inflamação", 3, None),
    ("k21", "nuclear", "a rota TRIF é a rota antiviral", 3, None),
    ("k22", "nuclear", "que leva a NF-κB e AP-1 e às citocinas inflamatórias, ou TRIF, que leva aos IRF e aos interferons do tipo I", 3, None),
    ("k23", "nuclear", "A ativação de TLR também sinaliza sobrevivência celular pela via da AKT, morte por ativação da caspase-8", 3, None),
    ("k24", "supporting", "de modo que um ligante que aciona um TLR essencialmente MyD88 pode acabar produzindo interferon", 3, None),
    ("k25", "supporting", "Não adianta ativar a molécula MyD88 se ela não estiver perto das quinases IRAK4 e IRAK1 para poder ativá-las", 3, None),
    ("k26", "nuclear", "A função dessa plataforma é muito específica — promover a maturação de citocinas pró-inflamatórias", 3, None),
    ("k27", "nuclear", "eles ficam soltos no citoplasma, reconhecem produtos bacterianos e ativam a via do NF-κB", 3, None),
    ("k28", "nuclear", "um estímulo pró-inflamatório — TLR, TNF, a própria IL-1β — ativa NF-κB e faz a célula transcrever e sintetizar a pró-IL-1β", 3,
     ("incorporated", "Schroder K, Tschopp J. Cell 2010;140(6):821–32 — priming e sinal 2 do NLRP3",
      "O slide já traz a figura do NLRP3; a E1 apenas explicita a exigência de dois sinais que a figura desenha.")),
    ("k29", "nuclear", "sinais de perigo que incluem ATP extracelular agindo no receptor P2X7 com efluxo de potássio pela panexina-1", 3,
     ("incorporated", "Schroder K, Tschopp J. Cell 2010;140(6):821–32 — vias de ativação do NLRP3",
      "Mesmo mecanismo da figura do slide, com os três braços do segundo sinal nomeados.")),
    ("k30", "supporting", "o NLRP3 oligomeriza pelos seus domínios NACHT, recruta o adaptador ASC pelo domínio PYD, e o ASC recruta a pró-caspase-1 pelo domínio CARD", 3, None),
    ("k32", "nuclear", "O que o interferon faz não é curar a célula que o produziu; é induzir um estado antiviral nas vizinhas ainda sadias", 3, None),
    ("k34", "nuclear", "é um convencimento da célula-alvo a morrer, um suicídio induzido", 3, None),
    ("k35", "supporting", "proteínas do plasma que funcionam como um sistema de PRR solúvel, e cujo nome é complemento", 3, None),
    ("k36", "nuclear", "o sistema também produz moléculas que grudam na partícula e para as quais existem receptores no fagócito", 3, None),
    ("k37", "nuclear", "os receptores da superfície do fagócito vão grudando na partícula, ponto a ponto, e a membrana vai se fechando em volta", 3, None),
    ("k38", "nuclear", "As citocinas são proteínas ou glicoproteínas produzidas pelas células com múltiplas ações", 3, None),
    ("k40", "supporting", "O ácido araquidônico, pendurado no fosfolipídio de membrana, é fragmentado e gera prostaglandinas e leucotrienos", 3, None),
    ("k42", "nuclear", "as quatro famílias — CXC, CC, CX3C e XC — são definidas pelo arranjo dos primeiros resíduos de cisteína da molécula", 3, None),
    ("k43", "supporting", "a IL-6 tornou-se alvo terapêutico com anticorpos que bloqueiam sua ação em formas graves de COVID-19", 3, None),
    ("k44", "nuclear", "infectando o animal e impedindo que ele se aqueça, ou seja, impedindo que desenvolva febre, ele morre com muito mais facilidade", 3, None),
    ("k45", "nuclear", "Produtos previamente produzidos e armazenados, prontos para sair; produtos modificados após a ativação", 3, None),
]


def build():
    by_concept: dict[str, list[str]] = {}
    for card in CARDS:
        by_concept.setdefault(card["concept_id"], []).append(card["card_key"])

    concepts = []
    for cid, importance, anchor, quality, step1 in CONCEPTS:
        row = {
            "concept_id": cid,
            "importance": importance,
            "e1_anchor": anchor,
            "coverage_quality": quality,
            "card_keys": by_concept.get(cid, []),
        }
        if step1 is None:
            row["step1"] = {"decision": "not_applicable"}
        else:
            decision, ref, rationale = step1
            row["step1"] = {"decision": decision, "same_theme": True,
                            "source_ref": ref, "rationale": rationale}
        concepts.append(row)

    def sha(rel):
        return hashlib.sha256((BASE / rel).resolve().read_bytes()).hexdigest()

    return {
        "metadata": {
            "uc": "UC03",
            "prova": "P1",
            "componente": "Imunologia",
            "nome_curto": "Reconhecimento inato",
        },
        "lesson_slug": "imuno-01-reconhecimento-inato",
        "release_gate": {
            "schema": "nebli-e1-deck-release-v1",
            "e1_source": E1_SOURCE,
            "e1_source_sha256": sha(E1_SOURCE),
            "e1_pdf": E1_PDF,
            "e1_pdf_sha256": sha(E1_PDF),
            "card_budget_hard_max": 54,
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
                    "Revisão slide a slide dos 23 slides contra a transcrição integral da aula. "
                    "Os quatro objetivos têm conceito e card. As duas tabelas de ligantes (slides 16 "
                    "e 17) foram lidas da imagem e transcritas para a E1, incluindo localização e "
                    "origem do ligante. As figuras de IFN, citotoxicidade, fagocitose, vias do TLR e "
                    "NLRP3 estão explicadas em texto. A narração do professor foi usada como nota de "
                    "aula e está coberta, inclusive o experimento do lagarto, a advertência sobre "
                    "nomenclatura de citocinas e a separação NOD versus NLRP dentro da família NLR."
                ),
            },
            "concepts": concepts,
        },
        "cards": CARDS,
    }


if __name__ == "__main__":
    out = BASE / "deck-data.json"
    out.write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out, len(CARDS), "cards")
