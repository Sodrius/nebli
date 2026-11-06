# Especificação curada — 46 Expressão gênica em eucariotos I (UC03 P3, Biologia Molecular; Prof. Alexandre Bruni Cardoso; 39 lâminas). Pipeline v8
# (23/10): cada autoral nasce de uma motivação congelada na E3 (motivacoes.json); as notas que Davi já estuda e manteve ativas entram por sh()
# (histórico preservado); o resto da aula antiga sai pela refação (nebli.refacao).
# História: todas as células têm o mesmo DNA e a escolha dos genes se faz no início da transcrição. Em eucarioto o ativador não toca a Pol II,
# contata fatores gerais e o Mediador por alças de DNA, a cromatina reprime por padrão e a sinergia entre ativadores dá a especificidade do tecido.
# O ativador é modular (ligação ao DNA × ativação, Gal4: universalidade e modularidade) e o sinal chega ao fator por transdução: hormônio lipofílico
# e receptor nuclear, fosforilação e localização (FOXO1).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 8
SECOES_MOTIVO = ""
SECOES_DA_AULA = [
    "_FirstAid_01_Biochem_01_Molecular_11_Regulation_of_gene_expression_01_Promoter.txt",
    "_FirstAid_01_Biochem_01_Molecular_11_Regulation_of_gene_expression_02_Enhancer_Basics.txt",
    "_FirstAid_01_Biochem_01_Molecular_11_Regulation_of_gene_expression_03_Silencer.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-bm46-20261023a"
SHORT = "bm46"
LESSON = "2026-uc03-biologia-molecular-46-expressao-eucariotos-i"
DECK = "NEBLI::UC03::P3::Biologia Molecular::46 Expressão gênica em eucariotos I"
CRITERIOS = "MEMORY.md + pipeline v8 (EXECUCAO-DECK-AULA) + FEEDBACKS até F-20261023-CLAUDE-05 + GUIA_CARDS.md de 23/10"
MEDIA = {}
BUSCA = ("Três caminhos (23/10): seções de recurso do AnKing (Promoter, Enhancer, Silencer, hormônios esteroides; busca/secoes); palavra-chave em AnKing "
         "e Referências Externas (busca/anking.txt); significado em AnKing, acervos externos e NEBLI vivo, uma consulta por motivação (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


EXCLUIDOS = [
 (1467833441597, "afirmação óbvia (cada gene tem o seu promotor); a fala só diz que cada gene tem o seu promotor proximal"),
 (1467833693475, "repete 1467833682877 (enhancer aumenta a transcrição)"),
 (1467833712322, "repete 1467833724957 e o card do enhancer (perto, longe ou em íntron)"),
]
FORA_DO_RECORTE = [
 "Estrutura da cromatina, acetilação e metilação de histonas e remodeladores: 52 Expressão em eucariotos II.",
 "Elementos TATA, INR, DPE, BRE e a ordem TFIIA, TFIIB, TFIIF, TFIIH: cadeia de nomes que Davi suspendeu; fica só quem reconhece o promotor.",
 "Classes de domínios de ligação ao DNA em detalhe, JAK-STAT, GFP-Pho4, mutante serina→alanina, transtiretina além do HNF1/HNF3 e Gal80/Gal3 (extras): exemplos que ilustram princípios já cobertos.",
 "Operon lac, regulação negativa e positiva: 29 Operon em procariotos.",
]
A_, B_, C_, D_, E_, F_, G_ = "A-por-que-regular", "B-procarioto-eucarioto", "C-fatores-gerais", "D-enhancers", "E-sinergia-mediador", "F-gal4", "G-sinais"

CARDS = [
 # ---------- Por que regular (lâminas 7–8) ----------
 sh(1791627546300, "azul", A_, "Regular serve à diferenciação", 7, "A-aula: card já estudado por Davi"),
 sh(1791627546427, "azul", A_, "Housekeeping × regulado", 8, "A-aula: card já estudado por Davi"),
 # ---------- Procarioto × eucarioto (lâminas 9–11) ----------
 K(1467682184880, "V-hy", B_, "Heterocromatina é inacessível", 9, "lâmina 9 (a cromatina é uma camada extra de controle)"),
 au("au-cromatina-reprime", "Eukaryotes need fewer <b>repressors</b> than bacteria, because {{c1::chromatin}} already keeps most genes off",
    "A-aula", B_, "Cromatina reprime por padrão", 9, "lâmina 9; transcrição", motivacao="m4",
    extra="Bacterial DNA is naked, so a repressor has to block the promoter.<br>Eukaryotic DNA is wrapped in nucleosomes, so repression is mostly exerted on chromatin structure, through histone modifications.<br>That is also why positive regulation predominates in eukaryotes."),
 au("au-ativador-indireto", "Unlike bacterial <b>CAP</b>, a eukaryotic activator never touches RNA polymerase II, but contacts the {{c1::Mediator}} or general factors",
    "V-pilar", B_, "Ativador eucariótico não toca a Pol II", 10, "lâminas 9–10; transcrição; exercício 1", motivacao="m3",
    extra="In bacteria the activator recruits the polymerase directly.<br>In eukaryotes the polymerase sits inside a large complex of general factors and Mediator, so the contact is made with those proteins.<br>This is why a DNA loop is needed to bring distant sequences close to them."),
 sh(1791627546678, "azul", B_, "Cis × trans", 11, "A-aula: card já estudado por Davi"),
 # ---------- Fatores gerais e promotor (lâminas 12–13) ----------
 K(1467833651277, "V-hy", C_, "Promotor: Pol II e fatores gerais", 12, "lâmina 12"),
 K(1467833666692, "A-aula", C_, "Promotor liga fatores gerais", 12, "lâmina 12 (gerais × específicos)"),
 K(1467833846822, "R-detalhe", C_, "Pol I e III transcrevem genes constitutivos", 12, "lâmina 12 (a Pol II é a que interessa; Pol I e III fazem tRNA e rRNA)"),
 K(1467833654903, "V-hy", C_, "TATA e CAAT", 13, "lâmina 13"),
 K(1467833662315, "A-aula", C_, "Mutação no promotor reduz a transcrição", 13, "lâmina 13 (e se um sítio mutar)"),
 au("au-sigma-gerais", "Bacterial polymerase finds the promoter by its <b>sigma</b> factor, whereas in eukaryotes {{c1::general transcription factors}} do it",
    "A-aula", C_, "Quem reconhece o promotor", 13, "lâminas 12–13; transcrição", motivacao="m7",
    extra="TFIID binds the TATA box first, through its TBP subunit, and the polymerase joins later.<br>No eukaryotic protein is homologous to sigma, and none of the 12 polymerase subunits recognizes the promoter."),
 # ---------- Enhancers (lâminas 14–15) ----------
 K(1467833682877, "V-hy", D_, "Enhancer liga fatores específicos", 14, "lâmina 14"),
 K(1467833697927, "A-aula", D_, "Enhancer: sítio de fatores específicos", 14, "lâmina 14 (gerais × específicos)"),
 K(1467833716981, "A-aula", D_, "Elementos de resposta no enhancer", 14, "lâmina 14 (sítios regulatórios)"),
 au("au-enhancer-proximal", "An <b>enhancer</b> works at {{c1::any}} distance and orientation, whereas a promoter-proximal element works only {{c1::near}} the promoter",
    "V-pilar", D_, "Enhancer × promotor proximal", 14, "lâminas 11 e 14; transcrição; meta da lâmina 6", motivacao="m8",
    extra="Moving a proximal element thousands of base pairs away abolishes its effect, while an enhancer can lie upstream, downstream or inside an intron.<br>One enhancer can regulate several genes, and one gene can have several enhancers, for example one for each stage of development."),
 K(1467833724957, "V-hy", D_, "Alça de DNA leva o enhancer ao promotor", 15, "lâmina 15"),
 K(1467833689549, "A-aula", D_, "Silenciador", 15, "lâmina 15 (regulação negativa)"),
 # ---------- Sinergia, especificidade e Mediador (lâminas 16–17) ----------
 sh(1791627548775, "verde", E_, "Sinergia", 16, "V-pilar: card já estudado por Davi"),
 au("au-especificidade", "The <b>transthyretin</b> gene is liver-specific because only liver cells make {{c1::HNF1}} and {{c1::HNF3}}",
    "A-aula", E_, "Especificidade do tecido por combinação", 16, "lâmina 16; transcrição", motivacao="m11",
    extra="The gene also needs activators found in many tissues, but without the two liver-only factors its enhancer and promoter never work together.<br>This is how synergy and signal integration produce tissue specificity."),
 sh(1791627547475, "verde", E_, "Pol II precisa de fatores gerais e Mediador", 17, "V-pilar: card já estudado por Davi"),
 au("au-coativador", "A <b>coactivator</b>, such as the Mediator, activates transcription without {{c1::binding DNA}}",
    "A-aula", E_, "Coativador e Mediador", 17, "lâmina 17; transcrição", motivacao="m12",
    extra="It works through activators bound to DNA.<br>Its many contact points make the Mediator a platform that integrates the signals of several enhancers."),
 au("au-alosteria", "An <b>activator</b> can switch on a promoter already loaded with machinery by positioning {{c1::TFIIH}} to phosphorylate the polymerase tail",
    "A-aula", E_, "Ativação alostérica", 17, "lâmina 17; transcrição", motivacao="m13",
    extra="Phosphorylation of the tail lets RNA polymerase II escape the promoter and start elongating, so the activator acts allosterically instead of recruiting.<br>Activators can also recruit elongation factors that free a polymerase paused on a sequence that is hard to transcribe."),
 au("au-repressor-modos", ORG("<b>Eukaryotic repressors</b> act by<br>- {{c1::competing}} with the activator for the site<br>- {{c1::masking}} the activation domain<br>- {{c1::allosteric}} change of the machinery"),
    "R-org", E_, "Três maneiras de reprimir", 17, "lâmina 17; transcrição", motivacao="m14", organizador=True,
    extra="Competition depends on affinity and on the amount of active protein, so small changes in the active fraction tune the outcome.<br>Masking works because the repressor and the activator bind side by side, and the repressor covers the activation domain."),
 K(1467682246440, "V-hy", E_, "Acetilação ativa a transcrição", 17, "lâmina 17 (ativadores recrutam modificadores de cromatina)"),
 # ---------- Gal4 (lâminas 19–28) ----------
 au("au-dbd-ad", "Cutting a piece of an <b>activation domain</b> {{c1::weakens}} the factor, whereas altering its DNA-binding domain {{c1::abolishes}} binding",
    "V-pilar", F_, "Ligação tudo ou nada, ativação incremental", 21, "lâmina 21; transcrição", motivacao="m15",
    extra="A DNA-binding domain fits its sequence like a key in a lock, so it works all or none.<br>Activation domains are small repeated units that add up, like Velcro that grips better when larger.<br>That is why factors are classified by their DNA-binding domain."),
 sh(1791627549152, "verde", F_, "Domínios do ativador", 22, "V-pilar: card já estudado por Davi"),
 sh(1791627549403, "verde", F_, "Universalidade", 24, "V-pilar: card já estudado por Davi"),
 au("au-modularidade", "A Gal4 activation domain fused to the <b>LexA</b> DNA-binding domain still activates, so the domains are {{c1::modular}}",
    "A-aula", F_, "Modularidade", 28, "lâminas 27–28; exercício 2 (duplo híbrido)", motivacao="m18",
    extra="The DNA-binding domain only anchors the factor, and without the activation domain Gal4 binds DNA but does not activate.<br>The yeast two-hybrid system rests on this: a bait fused to a DNA-binding domain and a prey fused to an activation domain activate a reporter only when the two proteins interact."),
 # ---------- Sinais (lâminas 29–38) ----------
 sh(1792082068909, "azul", G_, "Pho: cascata de transdução", 31, "A-aula: card já estudado por Davi"),
 K(1461867085192, "V-hy", G_, "Receptores de peptídeo × esteroide", 32, "lâmina 32; prova 2019 P3 5.4"),
 K(1461867876279, "V-hy", G_, "Dímero receptor-esteroide é fator de transcrição", 33, "lâmina 33"),
 K(1467833758513, "A-aula", G_, "Dedo de zinco nos receptores nucleares", 33, "lâmina 33"),
 K(1462038493029, "A-aula", G_, "T3 e o elemento de resposta", 34, "lâmina 34"),
 K(1463883728414, "A-aula", G_, "GR no citoplasma até o hormônio", 35, "lâmina 35"),
 K(1463883738825, "A-aula", G_, "GR ativado entra no núcleo", 35, "lâmina 35"),
 au("au-nls", "<b>Phosphorylation</b> can keep a factor in the cytoplasm by hiding its {{c1::nuclear localization}} sequence from importins",
    "A-aula", G_, "Fosforilação esconde o NLS", 36, "lâmina 36; transcrição; prova 2019 P3 5.2", motivacao="m23",
    extra="Importins recognize the NLS and carry the protein through the nuclear pore, so a hidden NLS means no entry and the target genes stay off.<br>Phosphorylation can also change the shape of the DNA-binding domain, so the factor enters the nucleus but cannot bind DNA."),
 sh(1791627550702, "verde", G_, "FOXO1: insulina o mantém fora do núcleo", 37, "V-pilar: card já estudado por Davi"),
]
for c in CARDS:
    if c["kind"] == "autoral":
        c["text"] = _re.sub(r"\{\{c(\d+)::(.*?)((?:::[^}]*)?)\}\}", lambda m: "{{c%s::<b>%s</b>%s}}" % (m.group(1), m.group(2), m.group(3)), c["text"])

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1467682184880": "Chromatin is a layer of control that bacteria do not have, so access of the machinery to DNA is also regulated.",
 "ak1467833662315": "A mutation in a regulatory site makes the gene lose that signal, so its expression falls or loses its tissue specificity.",
 "ak1467833716981": "Each response element binds one specific factor, and the sum of the factors bound defines the output of the enhancer.",
 "ak1467682246440": "Activators recruit histone acetyltransferases, so they open chromatin as well as recruit the machinery.",
 "ak1461867085192": "Steroids and thyroid hormone are lipophilic and cross the membrane, so their receptors are inside the cell and act as transcription factors.",
 "ak1461867876279": "The receptor is an activator that only binds DNA after the hormone binds it.",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {"objetivo": "Entender como a transcrição eucariótica é regulada: promotor e fatores gerais, enhancers, sinergia e Mediador, a estrutura modular dos ativadores (Gal4) e como sinais chegam aos fatores.",
          "centrais": [
           ["ativador eucariótico não toca a Pol II", "au-ativador-indireto"],
           ["enhancer × promotor proximal", "au-enhancer-proximal"],
           ["domínios do ativador", "au-dbd-ad"],
           ["sinergia", "sh-1791627548775"],
           ["universalidade", "sh-1791627549403"]],
          "exemplos": ["au-especificidade", "au-modularidade", "au-nls"],
          "outras_aulas": ["29 Operon em procariotos", "52 Expressão em eucariotos II", "54 RNAs não codificadores"]}
import re as _r2
CARDS.sort(key=lambda c: int(_r2.search(r"\d+", c["evid"]).group()))
