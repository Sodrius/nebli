# Especificação curada — Deck-prova UC19 1: Farmacodinâmica (UC19 P1, Farmacologia; modo prova, base = apostila + extras; F-20261029-CLAUDE-04).
# Davi (29/10): "deck-prova de farmáco independente das minhas aulas, mas cobrindo tudo da apostila e tudo dos materiais extras",
# "vou querer principalmente anking", "realmente cobrindo tudo e um pouco mais", "pode usar lâmina de vez em quando".
# A base da prova (fontes/slides.pdf, 35 páginas de excertos literais) faz o papel das lâminas: o "slide" de cada card é a página da base.
# Ordem: fundamentos → alvos → curva e segurança → agonismo → antagonismo → perda de resposta → casos. Acervo primeiro (cópias NEBLI com
# histórico entram por acervo()); autoral só para o que nenhum acervo tem; autorais antigos que Davi aprovou ou corrigiu entram por sh().
import pathlib as _pl, re as _re, sys as _sys, json as _json
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo  # noqa: E402

PIPELINE_VERSAO = 11
MODO = "prova"
SECOES_MOTIVO = ""  # 30/10 (F-20261030-CLAUDE-01): Bootcamp 08 Receptor Physiology e OME General Principles lidos inteiros, mas fora do recorte: são fisiologia autonômica/endócrina; delas entram só as notas do assunto (NO/GMPc, organofosforado)
_SEC = ("_FirstAid_05_Pharm_01_Pharmacokinetics_and_Pharmacodynamics_07_Efficacy_vs_potency", "_FirstAid_05_Pharm_01_Pharmacokinetics_and_Pharmacodynamics_08_Receptor_binding",
        "_FirstAid_05_Pharm_01_Pharmacokinetics_and_Pharmacodynamics_09_Therapeutic_index",
        "_FirstAid_05_Pharm_01_Pharmacokinetics_and_Pharmacodynamics_10_Drug_effect_modifications_Types_of_Drug_Interactions",
        "_B_B_02_Basic_Pharmacology_01_General_02_Enzyme_Inhibitors", "_B_B_02_Basic_Pharmacology_01_General_02_Enzyme_Inhibitors_Extra",
        "_B_B_02_Basic_Pharmacology_01_General_03_Dose_Response", "_B_B_02_Basic_Pharmacology_01_General_03_Dose_Response_Extra",
        "_Bootcamp_Pharmacology_01_Pharmacodynamics_05_Drug_Enzyme_Interactions",
        "_Bootcamp_Pharmacology_01_Pharmacodynamics_09_Drug_Receptor_Interactions",
        "_SketchyPharm_09_Pharmacology_Foundations_06_Pharmacodynamic_Basics_01_Agonists_Antagonists_Allosteric_Modulators",
        "_SketchyPharm_09_Pharmacology_Foundations_07_Drug_Drug_Interactions_01_Introduction_to_Pharmacodynamic_Pharmacokinetic_D",
        "_SketchyPharm_09_Pharmacology_Foundations_01_Pharmacokinetic_Basics_02_Plasma_Concentration_Therapeutic_Range",
        "_Physeo_09_Pharm_15_Pharm_Fundamentals_04_Efficacy_Potency_Activity_at_Cell_Receptors_and_Therapeutic_Index",
        "_Physeo_09_Pharm_15_Pharm_Fundamentals_05_Drug_Drug_Interactions")
SECOES_DA_AULA = [f"{s}.txt" for s in _SEC]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc19-dp1-20261030a"
SHORT = "dp1"
LESSON = "2026-uc19-deck-prova-1-farmacodinamica"
DECK = "NEBLI::UC19::P1::Farmacologia::Deck-prova 1 — Farmacodinâmica"
CRITERIOS = "MEMORY.md + pipeline v11 (modo prova) + FEEDBACKS até F-20261029-CLAUDE-04 + GUIA-1 a GUIA-4 + PLANO-DECK-PROVA-UC19, 30/10"
MEDIA = {}
IMG = lambda n, w=320: f'<img src="dp1-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (30/10): seções de recurso de farmacologia geral do AnKing (First Aid, B&B, Bootcamp, Sketchy, Physeo, OME; busca/secoes); "
         "palavra-chave com sinônimos em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e no NEBLI vivo, uma consulta "
         "por card planejado (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


B1, B2, B3, B4, B5, B6, B7 = ("1-fundamentos", "2-alvos", "3-curva-seguranca", "4-agonismo", "5-antagonismo", "6-perda-resposta", "7-casos")
BASE = "fontes/slides.txt"

CARDS = [
 # ---------- 1 Fundamentos (base p. 1–5) ----------
 K(1565120487647, "V-pilar", B1, "Farmacocinética × farmacodinâmica", 1, "objetivos FD 1; resumo p.1; orientadoras 4–5"),
 au("farmaco-medicamento", ORG("<b>Basic pharmacology terms</b>, by definition:<br>- active substance of known structure: {{c1::drug::d…}}<br>- drug plus excipients for the patient: {{c1::medicine::m…}}<br>- any resource for cure or relief: {{c1::remedy::r…}}"),
    "V-pilar", B1, "Fármaco × medicamento × remédio", 1, "objetivos FD 1; resumo p.2; Ferro et al. p.3–4; questões de prova (orientadoras 3 e 7)", motivacao="m-f2", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="Remédio é uma substância ou recurso com efeito benéfico, administrado para obter cura ou alívio.",
    fontes=F("resumo da aula 1, p.2", "Medicamento é um fármaco manipulado para administração ao paciente, com propriedades benéficas."),
    sem_imagem="definições, sem figura na base",
    extra="In Portuguese: fármaco, medicamento, remédio.<br>Every medicine is a remedy, but a remedy may contain no drug at all (rest, a meal).<br>Excipients help formulation, stability or administration. Toxicology, the study of adverse effects of chemicals, is a subarea of pharmacology."),
 au("dose-veneno", "The Greek <b>phármakon</b> meant both remedy and {{c1::poison}}, and Paracelsus held that the {{c2::dose}} separates the two",
    "A-aula", B1, "Phármakon e Paracelso", 3, "Ferro et al. p.2; questões de prova (orientadoras 1–2)", motivacao="m-f3",
    fontes=F("Ferro et al., Uma breve história, p.2", "Mas, phármakon também significava, entre outros, “veneno\", “mal”."),
    sem_imagem="conceito histórico, sem figura",
    extra="Wanted and unwanted effects come from the same molecule and cannot be fully separated.<br>The therapeutic index measures how far apart they are."),
 K(1485913667420, "A-step", B1, "Fase I: segurança, toxicidade, PK e PD", 2, "resumo p.2 (ensaios pré-clínicos e fases clínicas); Emer 1"),
 K(1485913675748, "A-step", B1, "Fase II: dose, eficácia, efeitos adversos", 2, "resumo p.2; Emer 1"),
 K(1485913688921, "A-step", B1, "Fase III: eficácia × padrão", 2, "resumo p.2; Emer 1"),
 K(1485913697186, "A-step", B1, "Fase IV: efeitos raros e tardios", 2, "resumo p.2; Emer 1"),
 sh(1791762409798, "azul", B1, "Fase biofarmacêutica: desintegrar e dissolver", 2, "A-aula: autoral antigo da UC19 (5 revisões, sem crítica); resumo p.2–3 (etapas da ação)"),
 # ---------- 2 Alvos (base p. 6–12) ----------
 au("classes-alvo", ORG("<b>Drug targets</b>, the macromolecules a drug binds:<br>- receptors<br>- {{c1::ion channels::i…}}<br>- {{c1::transporters::t…}}<br>- {{c1::enzymes::e…}}<br>- {{c1::nucleic acids::n…}}"),
    "V-pilar", B2, "Cinco classes de alvo", 6, "objetivos FD 2; resumo p.3; questões de prova (orientadoras 6, 11–13; Emer 4)", motivacao="m-a1", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="5 principais alvos moleculares Os fármacos atuam interagindo seletivamente com componentes macromoleculares celulares.",
    fontes=F("resumo da aula 1, p.3", "5 principais alvos moleculares Os fármacos atuam interagindo seletivamente com componentes macromoleculares celulares."),
    sem_imagem="lista; os exemplos de cada alvo vêm nos cards seguintes",
    extra="A few drugs act with no target at all: mannitol (osmosis), antacids (neutralization), chelators (binding a metal).<br>Langley saw atropine and pilocarpine cancel each other in fixed proportions and inferred a receptive substance, the idea behind receptors."),
 au("seletividade", "Testing <b>chemical analogues</b> for which groups give agonist or antagonist activity defines a drug's {{c1::structure–activity}} relationship",
    "A-aula", B2, "Especificidade: estrutura-atividade", 8, "objetivos FD 3; Ferro et al. p.4 (Ehrlich) e p.8 (Bovet); questão de prova (orientadora 9)", motivacao="m-a7",
    fontes=F("Ferro et al., p.4", "\"descrever os princípios da toxicidade seletiva dos fármacos"),
    sem_imagem="conceito, sem figura",
    extra="A drug acts only where its shape fits a target, which is why specificity comes from structure.<br>Ehrlich's \"magic bullet\" is the same idea: selective toxicity to the germ or tumor, not the host."),
 K(1484768461819, "A-aula", B2, "Receptor ionotrópico: GABA-A", 7, "resumo p.3 (receptores ionotrópicos; canais controlados por ligante)"),
 K(1555083517363, "A-aula", B2, "Ionotrópico: ação direta", 7, "resumo p.3; Emer 2–3"),
 K(1522203660054, "V-prova", B2, "Receptor acoplado à proteína G", 7, "resumo p.3 (GPCR); Emer 2–3"),
 K(1461866207939, "A-aula", B2, "Receptor tirosina-quinase", 7, "resumo p.3 (receptores ligados a quinases)"),
 K(1461867085192, "V-prova", B2, "Peptídeo: receptor de membrana; esteroide: nuclear", 7, "resumo p.3 (receptores nucleares); Emer 2"),
 K(1509225252310, "A-aula", B2, "Platinas: ligações cruzadas no DNA", 7, "resumo p.4; orientadora 14"),
 K(1509225571827, "A-aula", B2, "Platinas: nefrotoxicidade", 7, "orientadoras 20 e 34"),
 K(1509235247004, "A-aula", B2, "Antraciclinas: intercalam no DNA", 7, "resumo p.4 (doxorrubicina)"),
 K(1509235473720, "A-aula", B2, "Antraciclinas: cardiotoxicidade", 7, "orientadoras 20 e 33"),
 K(1475636907165, "V-prova", B2, "Manitol: diurético osmótico", 7, "resumo p.4; orientadoras 17 e 32"),
 sh(1791762415623, "azul", B2, "Antiácido: sem alvo, neutraliza", 7, "A-aula: autoral antigo que Davi melhorou ('melhorei o card para ficar mais atômico'); orientadora 18"),
 K(1490137896605, "R-detalhe", B2, "Quelante: dimercaprol", 7, "orientadora 19; resumo p.8 (dimercaprol)"),
 K(1461865849072, "V-prova", B2, "NO → guanilato ciclase solúvel → GMPc", 10, "Ferro et al. p.15–16; orientadoras 15 e 31"),
 K(1461865801747, "A-aula", B2, "GMPc ativa PKG", 10, "Ferro et al. p.15–16"),
 K(1472747780684, "A-aula", B2, "GMPc → desfosforila cadeia leve da miosina", 10, "orientadora 31 (relaxamento vascular)"),
 K(1712002843254, "A-aula", B2, "Vasodilatadores que liberam NO", 10, "orientadora 31 (nitroglicerina libera NO)"),
 K(1463081026525, "V-prova", B2, "Inibidor de PDE5 reduz a degradação do GMPc", 10, "Ferro et al. p.16; orientadora 16"),
 K(1461857288204, "A-step", B2, "Fosfodiesterase degrada AMPc", 10, "um pouco mais: a mesma família de enzimas que a PDE5 (degrada nucleotídeo cíclico)"),
 K(1472747945251, "A-step", B2, "PDE5 + nitrato: evitar", 10, "um pouco mais: mesma via do GMPc somada (hipotensão)"),
 K(1503672347649, "A-aula", B2, "Clavulanato inibe β-lactamase", 11, "orientadoras 8 e 35"),
 K(1461624498591, "V-prova", B2, "IBP inibe a bomba H+/K+ irreversivelmente", 12, "lâmina 66 (bomba de prótons); objetivos FD 7 (omeprazol irreversível)"),
 K(1475023258287, "A-aula", B2, "Diurético de alça: cotransportador Na-K-2Cl", 12, "lâmina 66 (transportadores); orientadora 12"),
 K(1484950518844, "A-aula", B2, "Anestésico local bloqueia canal de Na", 12, "lâmina 67; orientadora 13"),
 # ---------- 3 Curva dose-resposta e segurança (base p. 13–19) ----------
 sh(1791762425949, "azul", B3, "Curva quantal: terapêutico, tóxico, letal", 13, "A-aula: autoral antigo corrigido a pedido de Davi ('faltou imagem'); objetivos FD 4"),
 sh(1791762418025, "verde", B3, "Afinidade × atividade intrínseca", 15, "V-pilar: autoral antigo, exemplar do GUIA-2 (B); objetivos FD 6; orientadoras 21–22"),
 K(1490066290359, "V-prova", B3, "Potência: quantidade para um efeito", 15, "resumo p.5; orientadora 23"),
 K(1490066293330, "V-prova", B3, "EC50 indica potência", 15, "resumo p.5; Stephen 3"),
 K(1490066276769, "V-prova", B3, "Eficácia: efeito máximo", 15, "resumo p.5; orientadora 22"),
 K(1490066280055, "A-step", B3, "Vmax indica eficácia", 15, "orientadora 24 (resposta máxima)"),
 sh(1791826286643, "verde", B3, "Gráfico: mais potente", 17, "V-prova: autoral antigo, exemplar do GUIA-2 (D); orientadora 23"),
 sh(1791826286795, "verde", B3, "Gráfico: mesma eficácia", 17, "V-prova: autoral antigo que Davi melhorou; exemplar do GUIA-2 (D); orientadora 24"),
 K(1490066320396, "V-prova", B3, "Índice terapêutico = TD50/ED50", 16, "resumo p.8; objetivos FD 4"),
 K(1490066323578, "V-prova", B3, "Mais seguro: IT maior", 16, "resumo p.8; orientadora 40"),
 K(1490066326802, "A-aula", B3, "IT estreito: varfarina, teofilina, digoxina, antiepilépticos, lítio", 16, "resumo p.8 (digoxina, varfarina, lítio)"),
 au("janela", "The range of <b>plasma concentration</b> between the minimum effective and the minimum toxic level is the {{c1::therapeutic window}}",
    "V-prova", B3, "IT estreito → janela estreita", 16, "objetivos FD 4; resumo p.8; questão de prova (orientadora 40)", motivacao="m-c6",
    fontes=F("resumo da aula 1, p.8", "Janela terapêutica: faixa de doses ou concentrações plasmáticas compreendida entre a concentração mínima eficaz e a concentração mínima tóxica."),
    sem_imagem="a curva quantal com DE50 e DT50 está no verso do card do índice terapêutico, logo antes",
    extra="A narrow therapeutic index (TD50 close to ED50) usually comes with a narrow window.<br>Dosing aims to keep the drug inside it, and narrow windows (digoxin, lithium, warfarin) need monitoring."),
 # ---------- 4 Agonismo (base p. 20–24) ----------
 au("agonismo-org", ORG("<b>Agonists by their effect on the receptor</b>:<br>- maximal response: {{c1::full::f…}} agonist<br>- submaximal response at any dose: {{c1::partial::p…}} agonist<br>- activity below baseline: {{c1::inverse::i…}} agonist<br>- one signaling pathway favored: {{c1::biased::b…}} agonist"),
    "V-pilar", B4, "Quatro tipos de agonista", 20, "objetivos FD 5; resumo p.6; questões de prova (orientadoras 24, 25, 28)", motivacao="m-g1", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="Agonista Parcial: Ativa o receptor mas produz uma resposta submáxima, independentemente da concentração aplicada.",
    fontes=F("resumo da aula 1, p.6", "Agonista Parcial: Ativa o receptor mas produz uma resposta submáxima, independentemente da concentração aplicada."),
    sem_imagem="organizador; o modelo de dois estados está nos cards do agonista inverso",
    extra="Efficacy is how far a ligand shifts the receptor toward its active state.<br>A full agonist may reach the maximum with spare receptors left over.<br>Examples: acetylcholine, buprenorphine, loratadine at H1, oliceridine."),
 K(1490066314616, "V-prova", B4, "Agonista parcial: curva desce", 21, "resumo p.6; orientadora 24"),
 K(1484950415236, "V-prova", B4, "Parcial + pleno: abstinência", 21, "resumo p.6; orientadora 37; exemplar de Davi"),
 K(1484950383414, "A-aula", B4, "Buprenorfina: agonista μ parcial", 21, "resumo p.6; orientadora 37"),
 K(1484950460397, "A-step", B4, "Butorfanol: agonista κ e parcial μ", 21, "Step HY 2 da seção de dose-resposta: outro agonista parcial opioide"),
 K(1477447295771, "A-step", B4, "β-bloqueadores com atividade agonista parcial", 21, "Step HY 2 da seção de dose-resposta: agonista parcial fora dos opioides"),
 K(1489960356460, "A-step", B4, "Clomifeno aumenta FSH e LH", 21, "Step HY 1 da seção de dose-resposta (B&B): modulador seletivo como agonista parcial/antagonista"),
 sh(1791762419072, "verde", B4, "Agonista inverso: abaixo do basal", 22, "V-prova: autoral antigo (12 revisões, sem crítica); orientadora 25; Stephen 1"),
 sh(1791762419199, "azul", B4, "Antagonista neutro: não muda o basal", 22, "A-aula: autoral antigo (11 revisões); orientadora 26; Stephen 1"),
 sh(1791762421022, "azul", B4, "Agonista tendencioso", 23, "A-aula: autoral antigo corrigido a pedido de Davi; orientadora 28"),
 # ---------- 5 Antagonismo, alosterismo e quiralidade (base p. 25–32) ----------
 K(1490066300391, "V-prova", B5, "Competitivo: potência cai (direita)", 26, "resumo p.7; orientadora 27"),
 K(1490066305390, "V-prova", B5, "Competitivo: eficácia igual", 26, "resumo p.7; orientadora 27"),
 K(1490066308677, "V-prova", B5, "Não competitivo: potência igual", 26, "resumo p.8"),
 K(1490066311609, "V-prova", B5, "Não competitivo: eficácia cai", 26, "resumo p.8"),
 K(1472426576894, "A-step", B5, "Inibidor competitivo reversível muda Km", 26, "objetivos FD 7 (reversível × irreversível); enzima como alvo"),
 K(1472426585896, "A-step", B5, "Não competitivo ou irreversível muda Vmax", 26, "objetivos FD 7"),
 K(1472426619514, "A-step", B5, "Competitivo reversível é superado", 26, "resumo p.7 (Emax restabelecido)"),
 K(1472426621969, "A-step", B5, "Irreversível não é superado", 26, "resumo p.7 (aspirina)"),
 K(1472426624361, "A-step", B5, "Não competitivo não é superado", 26, "resumo p.8"),
 K(1472426609949, "R-detalhe", B5, "Competitivo reversível lembra o substrato", 26, "Sketchy/B&B, um pouco mais"),
 K(1472426614133, "R-detalhe", B5, "Irreversível lembra o substrato", 26, "Sketchy/B&B, um pouco mais"),
 K(1472426616871, "R-detalhe", B5, "Não competitivo não lembra o substrato", 26, "Sketchy/B&B, um pouco mais"),
 K(1472426626716, "R-detalhe", B5, "Competitivo reversível: sítio ativo", 26, "Sketchy/B&B, um pouco mais"),
 K(1472426629660, "R-detalhe", B5, "Irreversível: sítio ativo", 26, "Sketchy/B&B, um pouco mais"),
 K(1472426631686, "R-detalhe", B5, "Não competitivo: fora do sítio ativo", 26, "Sketchy/B&B, um pouco mais"),
 K(1488847696894, "V-prova", B5, "Aspirina: acetilação covalente irreversível", 26, "objetivos FD 7; resumo p.7"),
 K(1485048808436, "A-aula", B5, "iMAO: irreversíveis", 26, "objetivos FD 7 (iMOA)"),
 K(1477432981161, "R-detalhe", B5, "Fenoxibenzamina: irreversível", 26, "um pouco mais: outro antagonista irreversível clássico"),
 au("antagonismo-sem-receptor", ORG("<b>Antagonism away from the agonist's receptor</b>:<br>- drugs combine in solution: {{c1::chemical::c…}}<br>- lower concentration at the target: {{c1::pharmacokinetic::p…}}<br>- opposite effects via other receptors: {{c1::physiological::p…}}"),
    "V-pilar", B5, "Químico, farmacocinético, fisiológico", 26, "objetivos FD 7; resumo p.8; questões de prova (orientadora 39; banco p.25–26)", motivacao="m-n4", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="Antagonismo químico Ocorre quando dois compostos reagem quimicamente entre si em solução",
    fontes=F("resumo da aula 1, p.8", "Antagonismo químico Ocorre quando dois compostos reagem quimicamente entre si em solução"),
    sem_imagem="organizador de conceitos, sem figura",
    extra="Chemical: dimercaprol binds metals. Pharmacokinetic: phenobarbital induces CYP and lowers warfarin.<br>Physiological: insulin and glucagon act through different receptors.<br>Competitive blockers such as propranolol and atropine occupy the agonist's own receptor instead."),
 K(1490066214478, "A-step", B5, "Interação aditiva", 26, "um pouco mais: tipos de interação (Medicosis)"),
 K(1490066222678, "A-step", B5, "Interação sinérgica", 26, "um pouco mais"),
 K(1490066217772, "R-detalhe", B5, "Interação permissiva", 26, "um pouco mais"),
 sh(1791762416798, "azul", B5, "Ortostérico × alostérico", 27, "A-aula: autoral antigo (4 revisões); objetivos FD 8; orientadora 29"),
 K(1484768430296, "A-aula", B5, "Benzodiazepínico: sítio alostérico do GABA-A", 27, "resumo p.4 (modulador alostérico)"),
 K(1484768435794, "A-aula", B5, "Benzodiazepínico potencializa o GABA-A (PAM)", 27, "resumo p.4 (PAM)"),
 K(1484768467897, "A-step", B5, "Benzodiazepínico aumenta a frequência de abertura do canal", 27, "Step HY 2 (Sketchy): como o modulador alostérico positivo muda o canal"),
 K(1484768472408, "R-detalhe", B5, "Benzo, barbitúrico, álcool: sítios alostéricos diferentes", 27, "um pouco mais: vários moduladores no mesmo alvo"),
 K(1484768629105, "A-step", B5, "Flumazenil: competitivo no sítio do benzodiazepínico", 27, "um pouco mais: antagonista competitivo de um sítio alostérico"),
 K(1554208492401, "A-aula", B5, "Enantiômeros: imagens especulares", 27, "resumo p.4; orientadora 30"),
 K(1555560638891, "R-detalhe", B5, "Mistura racêmica 50:50", 27, "um pouco mais (Medicosis: mistura racêmica)"),
 K(1701897271054, "A-aula", B5, "Enantiômero R(+) do anestésico local: mais tóxico", 27, "resumo p.4 (um enantiômero ativo e outro tóxico)"),
 K(1484950422509, "A-step", B5, "Naloxona: antagonista μ", 30, "Stephen 2 (antagonista usado na clínica)"),
 # ---------- 6 Perda de resposta (base p. 33) ----------
 au("perda-resposta", ORG("<b>Loss of drug response</b>:<br>- minutes, repeated doses: {{c1::tachyphylaxis::t…}}<br>- days to weeks: {{c1::tolerance::t…}}<br>- therapeutic efficacy lost in a patient: {{c1::refractoriness::r…}}<br>- microbes or tumor cells: {{c1::resistance::r…}}"),
    "V-pilar", B6, "Cinco nomes da perda de resposta", 33, "objetivos FD 9 (roteiro de prova); resumo p.1", motivacao="m-r1", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="dessensibilização, taxifilaxia, tolerância, refratariedade e resitência aos fármacos/medicamentos.",
    fontes=F("objetivos cognitivos FD, item 9", "dessensibilização, taxifilaxia, tolerância, refratariedade e resitência aos fármacos/medicamentos."),
    sem_imagem="organizador; mecanismos nos cards seguintes",
    extra="Desensitization is the receptor side of tachyphylaxis (same idea, minutes).<br>Mechanisms: receptor change or loss, mediator depletion, faster metabolism, physiological adaptation, drug efflux."),
 K(1490066226073, "A-aula", B6, "Taquifilaxia: queda aguda (nitratos)", 33, "objetivos FD 9"),
 K(1695594779845, "A-aula", B6, "Taquifilaxia é tolerância aguda", 33, "objetivos FD 9"),
 K(1605210863862, "A-aula", B6, "Taquifilaxia: depleção × receptor", 33, "objetivos FD 9 (mecanismos)"),
 K(1610988344275, "A-aula", B6, "Ativação prolongada → dessensibilização", 33, "objetivos FD 9"),
 K(1472747925827, "A-aula", B6, "Intervalo sem nitrato evita tolerância", 33, "orientadora 31 (nitroglicerina); Medicosis"),
 K(1560780655468, "A-aula", B6, "Tolerância: mais dose para o mesmo efeito", 33, "objetivos FD 9"),
 K(1560791719068, "R-detalhe", B6, "Tolerância cruzada", 33, "um pouco mais (Medicosis)"),
 K(1484768590208, "A-aula", B6, "Tolerância por regulação para baixo (GABA-A)", 33, "objetivos FD 9 (mecanismo de receptor)"),
 K(1461852748718, "A-step", B6, "Sensibilidade muda pelo número ou afinidade dos receptores", 33, "objetivos FD 9"),
 K(1518398747905, "A-aula", B6, "P-gp: resistência tumoral", 33, "objetivos FD 9 (resistência; extrusão ativa)"),
 # ---------- 7 Casos clínicos (base p. 34–35): só o princípio que cada caso carrega ----------
 K(1485382222368, "V-prova", B7, "Organofosforado: atropina, competitiva muscarínica", 35, "Emer 5 (envenenamento por acúmulo de ACh)"),
 K(1485382227392, "A-aula", B7, "Atropina não reverte a paralisia (nicotínica)", 35, "Emer 5 (paralisia do músculo esquelético)"),
 K(1485382192161, "R-detalhe", B7, "Organofosforado inibe a acetilcolinesterase", 35, "Emer 5 (agente que acumula acetilcolina)"),
 K(1485382187439, "A-aula", B7, "Envenenamento anticolinesterásico: paralisia flácida nicotínica", 35, "Emer 5 (paralisia do músculo esquelético)"),
 K(1470880181246, "A-aula", B7, "Potencial de repouso depende do K+", 34, "orientadora 38 (hipercalemia)"),
 K(1475704571141, "A-aula", B7, "Hipo e hipercalemia: arritmias", 34, "orientadora 38"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {  # porquê em uma linha para nota de acervo sem verso explicativo (gate de verso)
 "ak1509225571827": "The DNA damage that kills tumor cells also hits normal tissues; for cisplatin the kidney is the classic one.",
 "ak1509235473720": "Same idea from the other drug: an anticancer drug acting on DNA can be toxic to non-tumor tissue, here the heart.",
 "ak1490137896605": "Chelators bind the metal directly in solution and help remove it: a drug acting with no receptor (chemical antagonism).",
 "ak1461865801747": "This kinase step is what turns a cGMP rise into smooth muscle relaxation.",
 "ak1712002843254": "All three end in the same step: NO activates guanylyl cyclase and raises cGMP.",
 "ak1490066326802": "Small changes in dose or clearance push these drugs into toxicity, so their levels are monitored.",
 "ak1472426585896": "Same logic as receptors: when the agonist cannot outcompete the blocker, the maximum falls.",
 "ak1472426619514": "The inhibitor leaves the site, so enough substrate wins the competition back.",
 "ak1472426621969": "A covalent bond does not let go; adding substrate cannot free the site.",
 "ak1472426624361": "It acts at another site, so more substrate does not compete with it.",
 "ak1472426609949": "Looking like the substrate is what lets it occupy the same site.",
 "ak1472426614133": "It fits the active site like the substrate but then binds for good.",
 "ak1472426616871": "It binds elsewhere, so it does not need to look like the substrate.",
 "ak1472426626716": "Same site as the substrate: that is why they compete.",
 "ak1472426629660": "Same site, but the bond is permanent.",
 "ak1472426631686": "It changes the enzyme from another site, lowering maximal activity.",
 "ak1485048808436": "Effect lasts until the cell makes new enzyme, like aspirin and omeprazole.",
 "ak1477432981161": "Covalent block: more agonist does not restore the maximal response.",
 "ak1490066214478": "Each drug adds its own effect, as one plus one equals two.",
 "ak1490066222678": "Together they do more than the sum, as one plus one equals three.",
 "ak1484768472408": "Each one binds its own allosteric site and changes how the receptor answers GABA.",
 "ak1554208492401": "Same formula, different 3D shape, so a target may bind only one of them.",
 "ak1701897271054": "One enantiomer can carry most of the toxicity, which is why single-enantiomer drugs exist.",
 "ak1475704571141": "Potassium sets the resting membrane potential, so changing it alters excitability.",
 "ak1485382227392": "Atropine blocks only muscarinic receptors; the neuromuscular junction is nicotinic.",
 "ak1477447295771": "A partial agonist keeps some β stimulation while blocking catecholamines, so resting heart rate falls less.",
 "ak1484768467897": "Raising how often the channel opens is how this positive allosteric modulator boosts the GABA response.",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

DUPLICACAO = {"perda-resposta": "ganho: o AnKing dá a taquifilaxia em pergunta isolada; aqui os cinco nomes do objetivo FD 9 lado a lado, com o critério de tempo e de alvo que os separa"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {"objetivo": "Farmacodinâmica da prova de Farmacologia Básica: o que é fármaco, onde age, como se medem afinidade, eficácia, potência e segurança, os tipos de agonismo e antagonismo e por que a resposta cai com o uso.",
          "centrais": [["fármaco e alvos", "farmaco-medicamento", "classes-alvo"], ["curva", "sh-1791762418025", "sh-1791826286643", "sh-1791826286795"],
                       ["segurança", "janela"], ["agonismo", "agonismo-org"], ["antagonismo", "antagonismo-sem-receptor"], ["perda de resposta", "perda-resposta"]],
          "exemplos": [], "outras_aulas": ["Deck-prova 2 Farmacocinética (indução de CYP, absorção)", "Deck-prova 3 Farmacocinética quantitativa"]}

# EXCLUIDOS: toda nota das seções de recurso que não entra, com motivo da lista fechada do modo prova (gate deck_prova)
EXCLUIDOS = []  # preenchido por excluidos.py (lido aqui para o build)
_exc = HERE / "excluidos.json"
if _exc.exists():
    EXCLUIDOS = [tuple(x) for x in _json.loads(_exc.read_text(encoding="utf-8"))]
FORA_DO_RECORTE = ["Neandertais, Lavoisier e a galeria de Nobel do artigo de Ferro et al.: ilustração histórica; nenhum objetivo nem questão cobra.",
                   "Druggable genome: números conflitantes entre o resumo e Ferro et al.; nenhuma questão cobra."]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
