# Especificação curada — Mecanismos de ação hormonal (UC03 P1, Bioquímica; 56 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → cópias NEBLI vivas (GR2, integração I/II, biomol, farmaco) por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing; cópias NEBLI por sh)
    "_FirstAid_Endocrine_Insulin_Synthesis_Secretion.txt",
    "_FirstAid_Endocrine_Signaling_Peptide_Hormones.txt",
    "_FirstAid_Endocrine_Signaling_Steroid_Hormones.txt",
    "_FirstAid_Biochem_Glycogen_regulation_Protein_Signalling.txt",
    "_FirstAid_Endocrine_Glucagon_Function.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-bq10-20261017a"
SHORT = "bq10n"
LESSON = "2026-uc03-bioquimica-10-acao-hormonal"
DECK = "NEBLI::UC03::P1::Bioquímica::Ação hormonal"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid insulina, glucagon, sinalização de hormônios, regulação do glicogênio, "
         "catecolaminas, tireoide, cortisol; busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em "
         "todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
_COP = "entra a cópia NEBLI viva"
EXCLUIDOS = [
 (1462122564570, "seção insulina: gene no cromossomo 11 — número sem uso na aula"),
 (1462122701249, f"seção insulina: peptídeo C monitora a célula β — {_COP} (sh-1791054008921)"),
 (1462123239655, f"seção insulina: glicose regula a secreção — {_COP} (sh-1791647354170)"),
 (1462127745460, f"seção insulina: GLUT2 na célula β — {_COP} (sh-1791647354296)"),
 (1462127781248, f"seção insulina: ATP fecha K+ — {_COP} (sh-1791729317038)"),
 (1462127805913, f"seção insulina: ATP:ADP fecha K-ATP — {_COP} (sh-1791729317165)"),
 (1462127846011, f"seção insulina: canais de Ca²⁺ — {_COP} (sh-1791731883157)"),
 (1462127869624, f"seção insulina: Ca²⁺ dispara exocitose — {_COP} (sh-1791729317515)"),
 (1482021939459, f"seção insulina: glicose oral e incretinas — {_COP} (sh-1790999836955)"),
 (1472435673376, f"seção glicogênio: fosforilase fosforilada ativa — {_COP} (sh-1791647344895)"),
 (1472435681635, f"seção glicogênio: sintase fosforilada inativa — {_COP} (sh-1791647345145)"),
 (1524705541467, f"seções glicogênio/glucagon: resistência à insulina por Ser/Thr — {_COP} (sh-1791054013222)"),
 (1462131799037, f"seção glucagon: AMPc — {_COP} (sh-1791647349571)"),
 (1462131802276, f"seção glucagon: glicogenólise e gliconeogênese — {_COP} (sh-1791054011246)"),
 (1462131823875, f"seção glucagon: frutose-2,6-bisfosfato — {_COP} (sh-1791729320461)"),
 (1462131831506, f"seção glucagon: lipólise — {_COP} (sh-1791729320636)"),
 (1524258762201, f"seção glucagon: glucagon IM na hipoglicemia — {_COP} (sh-1791054010097)"),
 (1461866207939, f"receptor tirosina quinase — {_COP} (sh-1791762411098)"),
 (1474164674426, f"glicoquinase Km alto — {_COP} (sh-1791647346746)"),
 (1474164568985, f"hexoquinase Km baixo — {_COP} (sh-1791647346871)"),
 (1462128186045, f"GLUT4 pela insulina — {_COP} (sh-1791054011372)"),
 (1474253761770, f"fosforilase e AMP — {_COP} (sh-1791647351996)"),
 (1474253744082, f"epinefrina e fosforilase — {_COP} (sh-1791647350546)"),
 (1474253707546, f"sintase regulada por insulina, cortisol, G6P — {_COP} (sh-1791647352121)"),
 (1462131726115, f"hipoglicemia estimula glucagon — {_COP} (sh-1791647354044)"),
 (1462131783153, f"insulina inibe glucagon — {_COP} (sh-1791054011119)"),
 (1462128205014, f"insulina e estoque de glicogênio — {_COP} (sh-1791729316389)"),
 (1462128277353, f"insulina e síntese proteica — {_COP} (sh-1791729320088)"),
 (1462038493029, f"T3 no TRE — {_COP} (sh-1791627550153)"),
 (1467833758513, f"dedo de zinco dos receptores nucleares — {_COP} (sh-1791627550277)"),
 (1463883738825, f"receptor de glicocorticoide vai ao núcleo — {_COP} (sh-1791627550527)"),
 (1462061124035, f"cortisol e proteólise — {_COP} (sh-1791729316911)"),
 (1461852748718, f"sensibilidade do alvo — {_COP} (sh-1791762417900)"),
 (1462849248763, f"sulfonilureias fecham K-ATP — {_COP} (sh-1791054014146)"),
 (1489963815147, "minoxidil como vasodilatador direto: farmacologia cardiovascular; o uso que a aula cita entra em ak-minoxidil"),
]
FORA_DO_RECORTE = [
 "Descoberta da insulina, vídeo e RIA (lâminas 6, 12, 21): história e técnica, sem fato cobrado.",
 "Eixo TRH–TSH e sintomas de hipo/hipertireoidismo (lâminas 44–46): endocrinologia; aqui só o mecanismo de ação.",
 "SHBG, androgênios adrenais e StAR (seção FirstAid de esteroides): fora da aula.",
 "Antidiabéticos além das sulfonilureias (GLP-1, DPP-4, glitazonas): aulas de farmacologia e GR2.",
]
A_, B_, C_, D_, E_, F_, G_ = ("A-regulacao-receptores", "B-insulina-sintese-secrecao", "C-insulina-acao-glicogenio", "D-glucagon",
                              "E-catecolaminas", "F-tireoide-esteroides", "G-cortisol")

CARDS = [
 # ---------- A. Regulação e receptores (lâminas 2–18) ----------
 sh(1791647344393, "azul", A_, "Mudar a quantidade de enzima: controle mais lento e decisivo", 2, "lâmina 2; card da integração I"),
 sh(1791647344895, "verde", A_, "Fosforilase fosforilada é ativa", 3, "lâmina 3 e transcrição (fosforilase fosforilada ativa); card da integração I"),
 sh(1791647345145, "verde", A_, "Sintase fosforilada é inativa", 3, "lâmina 3 e transcrição; card da integração I"),
 sh(1791762417900, "rosa", A_, "Sensibilidade do alvo depende dos receptores", 7, "lâmina 7; card da farmacologia"),
 ak("ak-aminas-tirosina", 1461852700804, "A-aula", A_, "Hormônios aminas derivam da tirosina", 9, "lâminas 9 e 40; seção FirstAid"),
 ak("ak-aminas-classes", 1461852703655, "A-step", A_, "Aminas: tireoidianos e catecolaminas", 9, "lâminas 9 e 17; seção FirstAid"),
 ak("ak-esteroide-colesterol", 1461852697255, "A-aula", A_, "Esteroides derivam do colesterol", 9, "lâminas 9, 47 e 51; seção FirstAid"),
 sh(1791743348861, "azul", A_, "Sinalização endócrina", 10, "lâmina 10; card da 08"),
 sh(1791743348682, "azul", A_, "Sinalização parácrina", 10, "lâmina 10; card da 08"),
 sh(1791743348483, "azul", A_, "Sinalização autócrina", 10, "lâmina 10; card da 08"),
 sh(1791762411098, "azul", A_, "Receptor tirosina quinase", 13, "lâminas 13–14 (receptor da insulina); card da farmacologia"),
 sh(1791762410700, "rosa", A_, "Receptores β acoplados a Gs", 13, "lâminas 13–14 (receptor da epinefrina); card da farmacologia"),
 ak("ak-receptor-membrana", 1461867085192, "V-prova", A_, "Peptídeos: receptor de membrana; esteroides e tireoide: intracelular", 14, "lâminas 14–15; prova 2017 P1 4.1; apostila de exercícios (questão 1)"),
 ak("ak-peptideo-rapido", 1461867860665, "A-step", A_, "Peptídeos agem em minutos; esteroides em horas", 15, "lâmina 15; apostila de exercícios"),
 sh(1791627550027, "verde", A_, "Esteroide e tireoide em receptores nucleares", 15, "lâminas 15 e 48; provas 2024 P4 1.3 e 2017 P1 3.7; card da biomol"),
 ak("ak-gs-ac", 1461857237570, "A-aula", A_, "αs-GTP ativa a adenilato ciclase", 16, "lâminas 16 e 37 e transcrição (GDP por GTP, Gα solta βγ)"),
 ak("ak-camp-pka", 1461857273344, "V-pilar", A_, "AMPc ativa a PKA", 16, "lâmina 16 (amplificação pelo AMPc); apostila de exercícios (questão 8)"),
 ak("ak-pde", 1461857288204, "A-step", A_, "Fosfodiesterase degrada o AMPc", 16, "lâmina 32 e transcrição (insulina ativa a fosfodiesterase)"),
 # ---------- B. Insulina: estrutura, síntese, secreção (lâminas 19–28) ----------
 ak("ak-insulina-cadeias", 1462121573747, "R-detalhe", B_, "Insulina: cadeias A e B com pontes dissulfeto", 19, "lâmina 19; seção FirstAid"),
 sh(1791647354170, "verde", B_, "Glicose é o principal regulador da insulina", 20, "lâmina 20 e transcrição; card da integração I"),
 sh(1791647354044, "azul", B_, "Hipoglicemia estimula o glucagon", 20, "lâminas 20 e 35; card da integração I"),
 ak("ak-preproinsulina", 1462122572408, "A-aula", B_, "Pré-pró-insulina", 22, "lâmina 22 e transcrição (processamento pós-traducional)"),
 ak("ak-peptideo-sinal", 1462122608618, "A-aula", B_, "Retirar o peptídeo sinal dá pró-insulina", 22, "lâmina 22"),
 ak("ak-golgi", 1462122640848, "A-step", B_, "Pró-insulina vai para grânulos no Golgi", 22, "lâmina 22"),
 ak("ak-peptideo-c", 1462122652771, "V-pilar", B_, "Proteases cortam o peptídeo C", 22, "lâmina 22"),
 ak("ak-granulos-c", 1462122670792, "A-step", B_, "Insulina e peptídeo C no mesmo grânulo", 22, "lâmina 22"),
 ak("ak-equimolar", 1462122681020, "A-step", B_, "Insulina e peptídeo C saem em quantidades iguais", 22, "seção FirstAid"),
 sh(1791054008921, "azul", B_, "Peptídeo C monitora a célula β", 22, "lâmina 22; card do GR2"),
 ak("ak-insulinoma-c", 1462122709023, "A-step", B_, "Insulina e peptídeo C altos: insulinoma, sulfonilureia", 22, "lâmina 28 (insulinoma); apostila de exercícios (questões 2 e 6)"),
 ak("ak-exogena-c", 1462122859168, "A-step", B_, "Insulina alta com peptídeo C baixo: insulina exógena", 22, "par do anterior"),
 ak("ak-insulina-locais", 1462128178981, "A-aula", C_, "Insulina age em fígado, músculo e adiposo", 23, "lâminas 23 e 33 e transcrição"),
 ak("ak-insulina-musculo", 1462849092193, "A-step", C_, "No músculo: mais glicogênio e proteína", 23, "lâmina 23"),
 sh(1791054011372, "verde", C_, "Insulina insere GLUT4 em músculo e adiposo", 24, "lâmina 24; prova 2017 P1 4.1 (exposição dos GLUT); card do GR2"),
 sh(1791729320761, "azul", C_, "Sem insulina, GLUT4 fica em vesículas", 24, "transcrição (diabetes tipo 1); card da integração II"),
 ak("ak-glut4-expressao", 1462809232452, "R-detalhe", C_, "Insulina aumenta GLUT4 pela via PI3K", 24, "lâmina 24"),
 sh(1791647354296, "azul", B_, "GLUT2 leva glicose à célula β", 24, "lâminas 24 e 26; card da integração I"),
 sh(1791647346746, "azul", B_, "Glicoquinase: Km alto", 25, "lâmina 25; card da integração I"),
 sh(1791647346871, "azul", B_, "Hexoquinase: Km baixo", 25, "lâmina 25; card da integração I"),
 ak("ak-gk-orgaos", 1474164565607, "A-step", B_, "Glicoquinase no fígado e na célula β", 25, "lâminas 25–26"),
 ak("ak-gk-beta", 1462127759504, "A-aula", B_, "Na célula β, a glicoquinase fosforila a glicose", 26, "lâmina 26 (células β possuem glicoquinase); seção FirstAid"),
 sh(1791729317038, "verde", B_, "Metabolismo da glicose gera ATP e fecha K+", 26, "lâmina 26; card da integração II"),
 sh(1791729317165, "verde", B_, "ATP:ADP alto fecha K-ATP e despolariza", 26, "lâmina 26; card da integração II"),
 sh(1791731883157, "verde", B_, "Despolarização abre canais de Ca²⁺", 26, "lâmina 26; card da integração II"),
 sh(1791729317515, "azul", B_, "Ca²⁺ dispara exocitose da insulina", 26, "lâmina 26; card da integração II"),
 sh(1791054014146, "verde", B_, "Sulfonilureias fecham K-ATP", 27, "lâmina 27; card do GR2"),
 ak("ak-sulfo-classes", 1462127903018, "R-detalhe", B_, "Sulfonilureias e meglitinidas", 27, "seção FirstAid"),
 au("au-diazoxido", "Drugs that <b>open</b> β-cell K-ATP channels keep the membrane polarized and block insulin release, treating {{c1::insulinoma}}",
    "A-aula", B_, "Abrir K-ATP impede a secreção", 28, "lâmina 28 (agonistas de K-ATP na hiperinsulinemia); transcrição (minoxidil)",
    extra="- Diazoxide is the classic example; surgery is the definitive treatment<br>- Opposite of sulfonylureas, which close the channel"),
 ak("ak-minoxidil", 1489963845288, "R-detalhe", B_, "Minoxidil: alopecia e hipertensão grave", 28, "lâmina 28 e transcrição (minoxidil faz crescer cabelo)",
    extra_add="- It opens K-ATP channels, the same target as the drugs used for insulinoma"),
 # ---------- C. Ação da insulina e glicogênio (lâminas 29–34) ----------
 sh(1791647352121, "azul", C_, "Sintase ativada por insulina, cortisol e G6P", 29, "lâmina 29; card da integração I"),
 sh(1791729317761, "verde", C_, "Insulina: PKB inativa GSK-3", 30, "lâminas 30 e 32 e transcrição; card da integração II"),
 sh(1791647349819, "verde", C_, "Insulina ativa a fosfatase PP1", 30, "lâmina 30 e transcrição; card da integração I"),
 ak("ak-desfosfo-sintase", 1472435698856, "A-step", C_, "Sintase desfosforilada é ativa", 30, "seção FirstAid glicogênio"),
 sh(1791647351996, "azul", C_, "AMP ativa a fosforilase muscular", 31, "lâmina 31 e transcrição; card da integração I"),
 ak("ak-fosforilase-inibe", 1474253765696, "A-step", C_, "ATP, insulina e G6P inibem a fosforilase", 31, "lâmina 31 e transcrição (ATP alto: não degradar)"),
 sh(1791647348495, "rosa", C_, "Fosforilase hepática não responde ao AMP", 31, "card da integração I"),
 sh(1791647345020, "azul", C_, "No fígado, glicose deixa a fosforilase a inativa (T)", 31, "transcrição (glicose regula a fosforilase a); card da integração I"),
 ak("ak-desfosfo-fosforilase", 1472435688940, "A-step", C_, "Fosforilase desfosforilada é inativa", 31, "seção FirstAid glicogênio"),
 ak("ak-receptor-dimeriza", 1472435618038, "V-prova", C_, "Receptor de insulina dimeriza e é tirosina quinase", 32, "lâmina 32; prova 2017 P1 4.1"),
 ak("ak-irs", 1472435625919, "V-prova", C_, "Autofosforilação recruta IRS-1", 32, "prova 2017 P1 4.1 (IRS1 e cascata)"),
 ak("ak-sh2", 1472435632014, "A-step", C_, "Proteínas SH2 ligam o IRS-1", 32, "seção FirstAid glicogênio"),
 ak("ak-pi3k", 1472435639812, "A-step", C_, "PI3K leva o GLUT4 à membrana", 32, "seção FirstAid; prova 2017 P1 4.1"),
 sh(1791729317887, "azul", C_, "Insulina ativa PDE e desliga a PKA", 32, "transcrição; card da integração II"),
 sh(1791627551127, "rosa", C_, "AKT tira o FOXO1 do núcleo", 32, "card da biomol"),
 sh(1791729316389, "verde", C_, "Insulina estoca glicogênio no fígado", 33, "lâmina 33; card da integração II"),
 sh(1791729320088, "azul", C_, "Insulina aumenta a síntese proteica", 33, "lâmina 33; card da integração II"),
 sh(1791647352471, "azul", C_, "No adipócito, insulina leva glicose à síntese de TAG", 33, "lâmina 33; card da integração I"),
 sh(1791054011119, "azul", C_, "Insulina reduz o glucagon", 34, "lâminas 34–35; card do GR2"),
 ak("ak-glucagon-insulina", 1462127985068, "R-detalhe", C_, "Glucagon aumenta a insulina", 34, "seção FirstAid insulina"),
 ak("ak-somatostatina", 1462128017601, "R-detalhe", C_, "Somatostatina reduz a insulina", 34, "seção FirstAid insulina"),
 ak("ak-amilina", 1584122235393, "R-detalhe", C_, "Amilina é cossecretada com a insulina", 34, "seção FirstAid insulina"),
 sh(1790999836955, "rosa", C_, "Glicose oral libera mais insulina (incretinas)", 34, "card da UC08"),
 # ---------- D. Glucagon (lâminas 35–38) ----------
 sh(1791647353670, "azul", D_, "Célula α secreta glucagon", 35, "lâmina 35; card da integração I"),
 sh(1791054010097, "azul", D_, "Glucagon IM na hipoglicemia grave", 35, "lâmina 35 (uso clínico); card do GR2"),
 ak("ak-hipoglicemia-iv", 1524259092731, "R-detalhe", D_, "No hospital, glicose IV", 35, "par do anterior; seção FirstAid glucagon"),
 sh(1791054014447, "rosa", D_, "GLP-1 estimula insulina e inibe glucagon", 36, "lâmina 36 (pró-glucagon → GLP-1); card do GR2"),
 sh(1791647349571, "verde", D_, "Glucagon age por AMPc", 37, "lâmina 37; card da integração I"),
 sh(1791647347621, "azul", D_, "Glucagon → AMPc → PKA", 37, "lâmina 37 e transcrição; card da integração I"),
 sh(1791731887453, "azul", D_, "PKA ativa a fosforilase quinase e inativa a sintase", 37, "lâmina 37 e transcrição; card da integração II"),
 sh(1791054011246, "verde", D_, "Glucagon: glicogenólise e gliconeogênese", 38, "lâmina 38; card do GR2"),
 sh(1791729320461, "azul", D_, "Glucagon reduz frutose-2,6-bisfosfato", 38, "card da integração II"),
 sh(1791729320636, "azul", D_, "Glucagon: lipólise, menos síntese de ácidos graxos", 38, "lâmina 38; card da integração II"),
 ak("ak-glucagon-locais", 1462131701878, "A-step", D_, "Glucagon age no fígado e no adiposo", 38, "lâmina 38; seção FirstAid glucagon"),
 ak("ak-glucagon-cetoacidos", 1462131849821, "A-step", D_, "Glucagon aumenta ácidos graxos e cetoácidos", 38, "lâmina 38 e transcrição (corpos cetônicos)"),
 ak("ak-glucagon-ureia", 1462131857829, "R-detalhe", D_, "Glucagon aumenta a ureia", 38, "seção FirstAid glucagon"),
 ak("ak-glucagon-catabolico", 1462809734046, "A-step", D_, "Glucagon é catabólico", 38, "seção FirstAid glucagon"),
 sh(1791647350720, "azul", D_, "Músculo não tem receptor de glucagon", 38, "apostila de exercícios (questão 3); card da integração I"),
 # ---------- E. Catecolaminas (lâminas 40–41) ----------
 ak("ak-th", 1476416089486, "V-pilar", E_, "Tirosina hidroxilase: tirosina → DOPA", 40, "lâmina 40 (etapa limitante)"),
 ak("ak-dbh", 1476416108145, "A-step", E_, "Dopamina β-hidroxilase: dopamina → noradrenalina", 40, "lâmina 40"),
 ak("ak-pnmt", 1476416112396, "A-step", E_, "PNMT: noradrenalina → adrenalina", 40, "lâmina 40"),
 sh(1791647350546, "azul", E_, "Epinefrina ativa a fosforilase pelo receptor β", 41, "lâmina 41; card da integração I"),
 sh(1791647349446, "verde", E_, "Glucagon no fígado, epinefrina no músculo", 41, "lâmina 41; apostila de exercícios (questão 3); card da integração I"),
 ak("ak-estresse", 1584375808030, "A-step", E_, "Estresse: epinefrina e cortisol", 41, "lâmina 41 (resposta ao estresse)"),
 sh(1791054013222, "azul", E_, "Glucagon, cortisol e epinefrina causam resistência à insulina", 41, "transcrição (excesso de glicocorticoide simula diabetes); card do GR2"),
 # ---------- F. Tireoide e esteroides (lâminas 42–49) ----------
 au("au-mct8", "<b>Thyroid hormones</b> enter target cells through membrane {{c1::transporters}} such as MCT8 before binding nuclear receptors",
    "V-prova", F_, "Hormônio tireoidiano entra por transportador", 42, "lâmina 42 (transportador de membrana); provas 2024 P1 2.2 e 2017 P1 3.7 (MCT8)",
    extra="- Despite being lipophilic, T3/T4 need carriers; MCT8 mutations leave cells without hormone<br>- Inside, T4 is converted to the more active T3"),
 ak("ak-t3-nucleo", 1462038445101, "V-prova", F_, "T3 entra no núcleo e liga receptor nuclear", 42, "lâmina 42; provas 2024 P1 2.2 e 2017 P1 3.7"),
 sh(1791627550153, "verde", F_, "Complexo T3-receptor liga o TRE", 42, "prova 2017 P1 3.7 (THR e TRE); card da biomol"),
 ak("ak-t3-afinidade", 1461986072634, "A-step", F_, "T3 liga o receptor com mais afinidade", 42, "lâmina 42 (T4, T3, rT3)"),
 ak("ak-bmr", 1493668150043, "A-aula", F_, "Tireoide aumenta metabolismo basal e consumo de O2", 43, "lâminas 43–46; prova 2024 P1 2.2; apostila de exercícios (termogênese)"),
 ak("ak-tireoide-catabolico", 1462811101121, "R-detalhe", F_, "Efeitos tireoidianos são catabólicos", 45, "lâmina 45"),
 sh(1791627550277, "azul", F_, "Receptores nucleares têm dedos de zinco", 48, "lâmina 48; prova 2024 P4 1.3 (PPAR); card da biomol"),
 ak("ak-esteroide-dimeriza", 1461867864150, "A-step", F_, "Complexo esteroide-receptor dimeriza", 49, "lâmina 49"),
 ak("ak-sre", 1461867876279, "A-aula", F_, "Dímeros ligam elementos de resposta (SRE)", 49, "lâmina 49 (coativador e DNA)"),
 ak("ak-novas-proteinas", 1461867900413, "A-step", F_, "Efeito final: síntese de novas proteínas", 49, "transcrição (regulação hormonal ativa transcrição gênica)"),
 # ---------- G. Cortisol (lâminas 50–55) ----------
 ak("ak-cortisol-feedback", 1462053341905, "A-step", G_, "Cortisol alto reduz CRH e ACTH", 50, "lâmina 50 (eixo e feedback)"),
 ak("ak-desmolase", 1462049776032, "A-aula", G_, "Primeiro passo: colesterol → pregnenolona (desmolase)", 51, "lâmina 51"),
 ak("ak-acth-desmolase", 1462053248848, "R-detalhe", G_, "ACTH estimula a desmolase", 51, "lâmina 51"),
 sh(1791627550527, "azul", G_, "Receptor de glicocorticoide vai ao núcleo", 52, "lâmina 52; card da biomol"),
 ak("ak-cortisol-catabolico", 1462810386376, "A-step", G_, "Cortisol é catabólico", 53, "lâmina 53"),
 sh(1791729316911, "azul", G_, "Cortisol aumenta a proteólise", 53, "lâmina 53; card da integração II"),
 ak("ak-cortisol-lipolise", 1462061159065, "A-step", G_, "Cortisol aumenta a lipólise (glicerol para gliconeogênese)", 53, "lâmina 53"),
 ak("ak-cortisol-gng", 1463883917060, "V-pilar", G_, "Cortisol estimula a gliconeogênese", 53, "lâmina 53; apostila de exercícios (questão 7)"),
 ak("ak-cortisol-insulina", 1463883909077, "A-step", G_, "Cortisol reduz a sensibilidade à insulina", 53, "transcrição (excesso prolongado simula diabetes)"),
 ak("ak-addison", 1462390476322, "A-aula", G_, "Addison: insuficiência adrenal primária crônica", 54, "lâmina 54 (autoimunidade contra o córtex)"),
 ak("ak-cushing-sindrome", 1462066801144, "A-aula", G_, "Síndrome de Cushing: excesso crônico de glicocorticoide", 54, "lâmina 54"),
 ak("ak-cushing-doenca", 1462066845454, "A-step", G_, "Doença de Cushing: ACTH da hipófise", 54, "lâmina 54"),
 au("au-disruptores", "Chemicals that mimic or block hormones at their <b>receptors</b> are called endocrine {{c1::disruptors}}",
    "A-aula", G_, "Disruptores endócrinos", 55, "lâmina 55 (hormônio normal, imitador, bloqueador)",
    extra="- A mimic triggers the response without the hormone; a blocker prevents the real hormone from acting<br>- Examples: bisphenol A and some pesticides act on estrogen receptors"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "vias de sinalização e efeitos metabólicos sem estrutura a reconhecer em imagem; os esquemas das lâminas são diagramas de livro"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM

VERSO = {
 "ak-aminas-classes": "- Both come from tyrosine, but thyroid hormones act like steroids (nuclear receptor)",
 "ak-esteroide-colesterol": "- Cortisol, aldosterone and sex hormones; the first step is cholesterol → pregnenolone",
 "ak-peptideo-rapido": "- Membrane receptors change existing enzymes; nuclear receptors must make new proteins",
 "ak-peptideo-sinal": "- The signal peptide sends the chain into the endoplasmic reticulum",
 "ak-golgi": "- Disulfide bridges hold A and B chains before the C-peptide is cut",
 "ak-peptideo-c": "- C-peptide connects A and B chains in proinsulin",
 "ak-granulos-c": "- Both leave the β cell together when it is stimulated",
 "ak-insulina-locais": "- The brain takes up glucose without insulin (GLUT1/3)",
 "ak-insulina-musculo": "- GLUT4 brings glucose in; glycogen synthase is switched on",
 "ak-glut4-expressao": "- PI3K → AKT moves GLUT4 vesicles to the membrane",
 "ak-gk-orgaos": "- Its high Km lets it sense glucose levels after a meal",
 "ak-sulfo-classes": "- Both mimic high ATP, closing K-ATP and releasing insulin",
 "ak-fosforilase-inibe": "- High energy and high glucose mean no need to break glycogen",
 "ak-glucagon-cetoacidos": "- Fatty acids reach the liver and become ketone bodies in prolonged fasting",
 "ak-glucagon-catabolico": "- It breaks down glycogen, fat and protein to keep glucose for the brain",
 "ak-th": "- This is the rate-limiting step of catecholamine synthesis",
 "ak-dbh": "- It happens inside synaptic vesicles",
 "ak-t3-nucleo": "- The T3–receptor complex binds thyroid response elements and changes transcription",
 "ak-t3-afinidade": "- Most secreted hormone is T4, converted to T3 in tissues by deiodinases",
 "ak-esteroide-dimeriza": "- The dimer then binds DNA",
 "ak-sre": "- Coactivators join and switch transcription on",
 "ak-novas-proteinas": "- That is why steroid effects take hours",
 "ak-cortisol-feedback": "- Exogenous steroids therefore suppress ACTH and atrophy the adrenal cortex",
 "ak-acth-desmolase": "- Desmolase (side-chain cleavage) is the first step of all adrenal steroids",
 "ak-cortisol-lipolise": "- Glycerol from fat and amino acids from muscle feed hepatic gluconeogenesis",
 "ak-cortisol-gng": "- Prolonged excess mimics diabetes (steroid-induced hyperglycemia)",
 "ak-cortisol-insulina": "- It interferes with insulin signaling in muscle and adipose tissue",
 "ak-addison": "- Autoimmune destruction is the commonest cause in developed countries; all adrenal steroids fall",
 "ak-cushing-sindrome": "- The most common cause is exogenous glucocorticoid therapy",
 "ak-cushing-doenca": "- ACTH-secreting pituitary adenoma: high ACTH and high cortisol",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-diazoxido": "ganho: o lado oposto (abrir o canal bloqueia a secreção, no insulinoma); os cards de sulfonilureia cobram só fechar o canal"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (63 notas novas, 84 cards; frentes, clozes, versos e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Entender o que são hormônios, suas classes e receptores (membrana × nucleares, AMPc), a síntese e secreção da insulina, a ação "
             "de insulina, glucagon e epinefrina sobre o glicogênio e o metabolismo, a síntese de catecolaminas e o mecanismo dos hormônios "
             "tireoidianos e esteroides, com o cortisol como exemplo.",
 "centrais": [
   ("receptores e AMPc", "ak-receptor-membrana", "sh-1791627550027", "ak-camp-pka", "ak-receptor-dimeriza", "ak-irs"),
   ("insulina", "ak-peptideo-c", "sh-1791729317165", "sh-1791054011372", "sh-1791729317761", "sh-1791647349819"),
   ("glucagon e epinefrina", "sh-1791647349571", "sh-1791054011246", "sh-1791647349446", "ak-th"),
   ("tireoide e esteroides", "au-mct8", "ak-t3-nucleo", "ak-cortisol-gng"),
 ],
 "exemplos": ["insulinoma", "diabetes tipo 1 e 2", "sulfonilureias", "MCT8", "Addison e Cushing", "hipoglicemia grave"],
 "outras_aulas": [("integração metabólica", "25 e 33 (sh)"), ("diabetes", "GR2 (sh)"), ("receptores nucleares", "biomol (sh)"),
                  ("regulação hormonal e massa corpórea", "16")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
