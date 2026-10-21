# Especificação curada — 58 Multiplicação viral e antivirais (UC03 P3, Microbiologia; Prof. Enrique Boccardo; 242 lâminas = Multiplicação viral Ia/Ib
# (1–92), Antivirais (93–178) e Replicação viral II (179–242, repetição condensada de Ia/Ib)). Gerada a partir de inventario.py (escrito antes).
# Ordem = lâminas. Seções AnKing declaradas: replicação/genética viral (Physeo, Bootcamp), receptores (FirstAid) e antivirais (B&B, Bootcamp 39).
# Cards que já têm cópia NEBLI viva (57, 61, 34, 51…) entram por acervo()/sh(), não repetidos.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("O AnKing cobre o Step 1 de replicação viral (onde replica, polaridade do RNA, mecanismo de cada antiviral), mas quase não tem os "
                   "mecanismos que a aula ensina: primers e extremidade 5′, antígeno T, E1/E2, proteína iniciadora do adenovírus, círculo rolante, "
                   "inclusões e etapas do ciclo; busca em seções, palavra-chave e significado (busca/semantica.jsonl) não achou esses cards.")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb58-20261021a"
SHORT = "mb58"
LESSON = "2026-uc03-microbiologia-58-multiplicacao-viral-antivirais"
DECK = "NEBLI::UC03::P3::Microbiologia::Multiplicação viral e antivirais"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261021-CODEX-03 + ANTI-EXEMPLARES §1–16, 21/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (21/10): seções de recurso do AnKing (replicação e genética viral, receptores, antivirais; busca/secoes); palavra-chave e "
         "significado em AnKing, Referências Externas e NEBLI vivo (busca/semantica.jsonl, uma consulta por conceito). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    """Nota de acervo: entra pela cópia NEBLI viva quando existe (histórico), senão cópia nova do AnKing (todos os irmãos)."""
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


A_, B_, C_, D_, E_, F_, G_, H_ = ("A-definicao-infeccao", "B-etapas-do-ciclo", "C-adsorcao-penetracao", "D-desnudamento-sintese",
                                  "E-virus-de-dna", "F-virus-de-rna", "G-montagem-liberacao", "H-antivirais")

EXCLUIDOS = []  # preenchido abaixo por exclusoes.py (cada nota das seções declaradas que não entrou, com o motivo)
FORA_DO_RECORTE = [
    "Capas, leitura recomendada, agradecimentos e a repetição condensada (lâminas 179–242) apontam para os mesmos cards das lâminas 3–92.",
    "Estruturas químicas, tabelas de fármacos e figuras de cristalografia (lâminas 108–142, 152, 159–160): o card ensina a classe e o mecanismo, não a molécula.",
    "Inibidores experimentais de helicase-primase e de ribonucleotídeo redutase de herpesvírus, LJ001 e favipiravir (lâminas 132–133, 145–148): exemplos sem cobrança.",
    "Efeitos adversos, doses e indicações clínicas dos antivirais: farmacologia (UC19) e clínica; a aula só pede o alvo e o mecanismo.",
    "Gráficos de desenvolvimento de fármacos, número de ensaios e aprovações recentes (lâminas 165–175): panorama sem cobrança.",
    "Tabela de fármacos para COVID-19 (lâminas 171–175): entram os três que a aula nomeia com mecanismo (remdesivir, nirmatrelvir, tocilizumabe).",
    "Seção de efeito citopático da 'Transcrição Ib' (páginas 94–124, 'estudo dirigido para a aula prática'): é da aula 60 Prática de virologia; entram só o conceito (cópia da 61) e a lise do poliovírus que a lâmina 238 mostra.",
]

CARDS = [
    # ---------- A. Definição e infecção (lâminas 3–6) ----------
    sh(1792243070220, "azul", A_, "Vírions são montados, não crescem nem se dividem", 3, "A-aula: lâmina 3 (definição); card da 57"),
    sh(1792243070545, "azul", A_, "Vírus sem atividade metabólica", 3, "A-aula: lâmina 3 (sem informação para energia nem ribossomos); card da 57"),
    au("au-permissiva", "A <b>cell</b> with the viral receptor is {{c1::susceptible}}, and one that also supports replication is {{c2::permissive}}",
       "A-aula", A_, "Célula suscetível × permissiva", 4, "lâmina 4 (células permissivas); apostila guia de Micro e monitoria P3 (suscetibilidade e permissividade)",
       extra="- Infection also depends on access to the target cell and on the immune response"),
    au("au-mutacao", "<b>RNA viruses</b> mutate at a high rate because their polymerase cannot {{c1::correct}} {{c2::errors}}", "A-aula", F_,
       "Alta taxa de mutação dos vírus de RNA", 83, "lâmina 83; apostila guia de Micro (taxa de mutação e evasão imune)",
       extra="- Segmented genomes also reassort, as in influenza"),
    au("au-produtiva", "A(n) {{c1::productive}} <b>infection</b> yields new infectious virions, whereas a(n) {{c2::abortive}} one does not",
       "V-pilar", A_, "Infecção produtiva × abortiva", 6, "lâmina 6; monitoria P3 de Micro (infecção produtiva e abortiva)",
       extra="- Abortive: the cell is not permissive or the virus is defective<br>- Infection = the virus introduces its genetic material into the cell"),
    # ---------- B. Etapas do ciclo (lâminas 7–8) ----------
    au("au-etapas", ORG("<b>Steps of viral replication</b>:<br>- {{c1::Adsorption}}<br>- {{c1::Penetration}}<br>- {{c1::Uncoating}}<br>"
                        "- Synthesis of {{c2::proteins}} and {{c2::nucleic acid}}<br>- {{c3::Assembly}}<br>- {{c3::Maturation}}<br>- {{c3::Release}}"),
       "V-pilar", B_, "As etapas do ciclo de replicação, em ordem", 8, "lâminas 7–8 e 96 (etapas comuns a todos os vírus); monitoria P3 de Micro",
      
       extra="- In the influenza scheme the cycle splits into entry, synthesis in the cell and exit"),
    # ---------- C. Adsorção e penetração (lâminas 9–16) ----------
    sh(1792243082496, "azul", C_, "Glicoproteínas do envelope: ligam a célula e são antígenos", 9, "A-aula: lâmina 9 (receptores reconhecidos pelo vírus); card da 57"),
    K(1502066766747, "A-aula", C_, "gp120 é a glicoproteína externa do HIV", 10, "lâmina 10 (gp120 e CD4); seção FirstAid de receptores"),
    sh(1792166995490, "azul", C_, "gp120 liga CD4 e os correceptores CCR5 e CXCR4", 10, "A-aula: lâmina 10; card da aula 51"),
    K(1506805847290, "V-hy", C_, "gp120 permite a ligação do HIV ao CD4", 10, "lâmina 10 (gp120 e CD4); seção Bootcamp 39"),
    K(1502068331161, "A-aula", C_, "Início da infecção: HIV entra em macrófagos por CCR5", 10, "lâmina 10 (correceptor); seção FirstAid de receptores"),
    K(1502068440036, "A-aula", C_, "Fase tardia: HIV entra em linfócitos T por CXCR4", 10, "lâmina 10 (correceptor); seção FirstAid de receptores"),
    K(1516222322469, "A-aula", C_, "Rinovírus entra pelo ICAM-1", 10, "lâmina 10 (exemplo de receptor); seção FirstAid de receptores"),
    au("au-penetracao", ORG("<b>Viruses enter the cell by</b>:<br>- {{c1::endocytosis}}<br>- translocation<br>- {{c2::membrane fusion}}"),
       "V-pilar", C_, "Penetração: endocitose, translocação ou fusão", 11, "lâmina 11; monitoria P3 de Micro (penetração)",
       extra="- Endocytosis: poliovirus, adenovirus, influenza, HCV<br>- Fusion: herpesviruses, paramyxoviruses, HIV"),
    K(1516323635408, "A-aula", C_, "Hemaglutinina promove a endocitose do influenza", 14, "lâmina 14 (via endocítica do influenza A); seção Bootcamp 39"),
    K(1502066667272, "A-aula", C_, "gp41 do HIV medeia a fusão", 15, "lâmina 15 (inibidores de fusão do HIV); seção Bootcamp 39"),
    # ---------- D. Desnudamento e síntese dos componentes (lâminas 17–20) ----------
    au("au-desnud", ORG("<b>Uncoating</b> can occur:<br>- directly in the {{c1::cytoplasm}}<br>- after acidification of the {{c2::endosomal}} vesicle<br>"
                        "- at the {{c3::nuclear pore}}"),
       "V-pilar", D_, "Desnudamento: três locais", 17, "lâmina 17; monitoria P3 de Micro (desnudamento)",
       extra="- Uncoating separates the nucleic acid from the capsid, partly or completely"),
    au("au-precoces", "<b>Early</b> viral mRNAs encode {{c1::nonstructural}} proteins, whereas late mRNAs encode {{c2::structural}} proteins",
       "A-aula", D_, "mRNAs precoces × tardios", 20, "lâmina 20; monitoria P3 de Micro (síntese dos componentes)",
       extra="- Genome replication is prioritized over capsid proteins, which could trigger an immune response if made without genomes"),
    K(1502152021975, "A-aula", D_, "A maioria dos vírus de DNA replica no núcleo", 20, "lâminas 20 e 27 (DNA no núcleo); seção Bootcamp 27"),
    K(1516321076508, "A-aula", D_, "Vírus de RNA em geral replicam no citoplasma", 20, "lâmina 20 (RNA no citoplasma); seção Bootcamp 27"),
    K(1483913062659, "V-prova", D_, "Exceções: orthomyxovírus e retrovírus replicam no núcleo", 20, "lâminas 70 e 91; seção Bootcamp 27"),
    sh(1792243072244, "azul", D_, "Baltimore: caminho do genoma até o mRNA", 22, "A-aula: lâmina 22 (estratégia depende do genoma); card da 57"),
    # ---------- E. Vírus de DNA (lâminas 23–61) ----------
    au("au-pequenos-dna", ORG("<b>DNA viruses</b>:<br>- host-dependent (small): {{c1::papillomavirus}}, {{c1::polyomavirus}}, {{c1::parvovirus}}<br>- self-sufficient (large): {{c2::herpesvirus}}, {{c2::adenovirus}}, {{c2::poxvirus}}"),
       "V-pilar", E_, "Vírus de DNA pequenos dependem da célula", 29, "lâminas 28–29; apostila guia de Micro (menor vírus, mais simples)",
       extra="- They depend more on host proteins for DNA replication<br>- Replication of viral DNA always needs at least one viral protein"),
    au("au-prot-dna", ORG("<b>Large DNA viruses</b> encode:<br>- {{c1::DNA polymerase}} and helicases<br>- {{c3::exonucleases}}<br>- nucleotide enzymes such as {{c2::thymidine kinase}}"),
       "A-aula", E_, "Proteínas virais da replicação do DNA", 30, "lâmina 30 (proteínas virais); apostila guia de Micro",
       extra="- Others: ribonucleotide reductase and dUTPase<br>- Thymidine kinase is what activates acyclovir"),
    au("au-primers", ORG("<b>Viral DNA primers</b>:<br>- RNA at a fork: {{c1::papillomavirus}}, {{c1::polyomavirus}}, {{c1::herpesvirus}}<br>- protein: {{c2::adenovirus}}<br>"
                         "- DNA hairpin: {{c2::parvovirus}}, {{c2::poxvirus}}"),
       "V-pilar", E_, "Dois mecanismos de síntese de DNA e seus iniciadores", 32, "lâmina 32; monitoria P3 de Micro (forquilha × primer proteico ou de DNA)",
        extra="- Retroviral proviruses also replicate at a fork with RNA primers"),
    K(1493398712106, "A-aula", E_, "HPV: nu, icosaédrico, DNA circular de fita dupla", 41, "lâmina 41; busca por palavra-chave"),
    K(1516930208305, "A-aula", E_, "Adenovírus tem genoma de DNA linear", 47, "lâmina 47 (genoma com origens nas duas extremidades); busca por palavra-chave"),
    au("au-polyoma-t", "<b>Polyomavirus</b> large T antigen binds the {{c1::origin of replication}} and acts as a {{c2::helicase}}", "V-prova", E_,
       "Antígeno T: reconhece a origem e é helicase", 36, "lâminas 36–37; apostila guia de Micro e monitoria P3 (antígeno T)",
       extra="- It recruits the host replication machinery and unwinds the SV40 origin with ATP<br>- Cellular topoisomerases then relieve the supercoiling"),
    K(1463105909117, "V-hy", E_, "E6 do HPV de alto risco leva à destruição de p53", 43, "lâmina 43; seção FirstAid de HPV"),
    K(1463105915437, "V-hy", E_, "E7 do HPV de alto risco leva à destruição de Rb", 43, "lâmina 43"),
    au("au-adeno-pol", "<b>Adenovirus</b> uses the host {{c1::RNA}} polymerase but encodes its own {{c2::DNA}} polymerase", "A-aula", E_,
       "Adenovírus: RNA pol da célula, DNA pol própria", 46, "lâmina 46; apostila guia de Micro e monitoria P3",
       extra="- The viral DNA polymerase is an early protein"),
    au("au-adeno-primer", "<b>Adenovirus</b> DNA synthesis is primed by a {{c1::protein}} that binds dCMP and supplies the 3′-OH", "V-prova", E_,
       "Adenovírus: o primer é uma proteína", 47, "lâminas 47–49 (terminal protein); apostila guia de Micro e monitoria P3",
       extra="- The origins lie at both ends of the linear genome"),
    au("au-herpes-circ", "<b>Herpesvirus</b> DNA enters linear, {{c1::circularizes}} in the cell, and replicates by {{c2::rolling circle}}",
       "V-prova", E_, "Herpesvírus: circulariza e replica por círculo rolante", 51, "lâminas 51–52; apostila guia de Micro e monitoria P3",
       extra="- Host proteins carry out the circularization<br>- Origins: two oriS and one oriL"),
    K(1502570386887, "V-prova", E_, "Poxvírus: único DNA vírus que replica só no citoplasma", 54, "lâmina 54; seção Physeo de replicação"),
    K(1502570452327, "V-prova", E_, "Poxvírus tem a própria RNA polimerase dependente de DNA", 55, "lâmina 55; seção Physeo de replicação"),
    au("au-pox-precoces", "Right after losing its envelope, <b>poxvirus</b> makes {{c1::early}} mRNAs using the polymerase carried in the {{c2::virion}}",
       "A-aula", E_, "Poxvírus: mRNAs precoces pela polimerase do vírion", 55, "lâmina 55 (mRNAs precoces imediatos); monitoria P3 de Micro",
       extra="- The host RNA polymerase is in the nucleus, out of reach of a cytoplasmic virus"),
    K(1516927536764, "V-hy", E_, "Parvoviridae: únicos vírus de DNA de fita simples", 59, "lâmina 59 (grupo II de Baltimore); seção de genomas"),
    # ---------- F. Vírus de RNA (lâminas 62–83) ----------
    sh(1792243072575, "azul", F_, "RNA viral tem polaridade + ou −", 65, "A-aula: lâminas 65–66 (RNA polaridade + e −); card da 57"),
    sh(1792243072820, "azul", F_, "RNA + tem a estrutura do mRNA", 65, "A-aula: lâmina 65; card da 57"),
    sh(1792243073069, "azul", F_, "RNA + é traduzido de imediato", 68, "A-aula: lâmina 68 (genoma = mRNA, infeccioso); card da 57"),
    K(1506627151740, "A-aula", F_, "Picornavírus fazem poliproteína clivada por protease viral", 68, "lâminas 68–69 (poliproteína direta); seção Bootcamp 28"),
    K(1608910179425, "A-aula", F_, "A RdRp é a peça central do complexo de replicação", 79, "lâmina 79 (RNA polimerase dependente de RNA); coronavírus"),
    sh(1792243073320, "azul", F_, "RNA − precisa virar + antes de ser usado", 70, "A-aula: lâmina 70 (grupo V); card da 57"),
    sh(1792243073569, "azul", F_, "RNA − produz a própria RNA polimerase", 70, "A-aula: lâmina 70; card da 57"),
    sh(1792243073819, "azul", F_, "Genoma RNA − sozinho não é infeccioso", 80, "A-aula: lâmina 80 (genomas não infecciosos); card da 57"),
    K(1516320980606, "V-prova", F_, "Orthomyxoviridae: único RNA − que replica no núcleo", 70, "lâminas 70 e 91; seção Bootcamp 27"),
    sh(1792243074070, "azul", F_, "Transcrição reversa: RNA → DNA", 71, "A-aula: lâmina 71 (grupo VI); card da 57"),
    sh(1792243083345, "azul", F_, "Retrovírus: genoma diploide", 71, "A-aula: lâmina 71 (genoma diploide); card da 57"),
    au("au-retro-rt", "A <b>retrovirus</b> packages {{c1::reverse transcriptase}} and integrates its DNA copy as a {{c2::provirus}}", "A-aula", F_,
       "Retrovírus: transcriptase reversa no vírion e provírus", 73, "lâminas 71–75 e 229–230; apostila guia de Micro e prova 2024 P3 1.1",
       extra="- The incoming (+) RNA is not translated: it is the template for the reverse transcriptase<br>- Integration into the host genome is obligatory"),
    K(1502069441823, "A-aula", F_, "Transcriptase reversa gera dsDNA que a integrase insere", 74, "lâminas 74–75 (transcrição reversa); seção Bootcamp 39"),
    sh(1792243081124, "azul", F_, "env codifica gp120 e gp41", 73, "A-aula: lâmina 73 (genoma do retrovírus: gag, pro, pol, env); card da 57"),
    sh(1792243081596, "azul", F_, "pol codifica transcriptase reversa, protease e integrase", 73, "A-aula: lâmina 73; card da 57"),
    K(1506551550710, "V-hy", F_, "Hepatite B: DNA parcialmente de fita dupla", 76, "lâminas 76–77 (hepadnavírus); seção Bootcamp 39"),
    K(1506551774430, "A-aula", F_, "No núcleo, a DNA polimerase do HBV completa a fita dupla", 77, "lâmina 77 (reparo no núcleo); seção Bootcamp 39"),
    K(1506551930834, "V-prova", F_, "Transcriptase reversa do HBV faz o DNA da progênie a partir do RNA", 77, "lâminas 76–78 (DNA com intermediário de RNA); seção Bootcamp 39"),
    au("au-rdrp-todos", "All <b>RNA viruses</b> except {{c1::retroviruses}} encode an {{c2::RNA-dependent RNA polymerase}}", "V-pilar", F_,
       "Todo vírus de RNA, menos retrovírus, codifica RdRp", 79, "lâminas 79 e 224; monitoria P3 de Micro e prova 2024 P3 1.1 (RdRp)",
       extra="- The enzyme makes new genomes and mRNA<br>- The cell has no RNA-dependent RNA polymerase, so the virus must supply it"),
    au("au-reo-pol", "<b>dsRNA</b> and (−)ssRNA virions carry the {{c1::polymerase}}, so their genomes are not {{c2::infectious}} alone",
       "A-aula", F_, "Vírus de RNA − e dsRNA trazem a polimerase", 80, "lâmina 80; apostila guia de Micro e monitoria P3",
       extra="- (+)ssRNA viruses carry no polymerase: it is translated from the infectious genome"),
    K(1516321532745, "V-hy", F_, "Segmentados: mnemônico BOAR", 83, "lâmina 83 (genomas segmentados); seção Bootcamp 27"),
    K(1523806216737, "A-aula", F_, "Reassortment: troca de segmentos do genoma", 83, "lâmina 83 (reordenamento de segmentos); seção Bootcamp 27"),
    K(1516323064948, "V-hy", F_, "Antigenic shift: reassortment de HA e NA entre espécies", 83, "lâmina 83 (exemplo influenza); seção Bootcamp 27"),
    K(1523926575639, "V-hy", F_, "Reassortment ocorre em vírus segmentados", 83, "lâmina 83 (reordenamento de segmentos, influenza); seção Bootcamp 27"),
    # ---------- G. Montagem e liberação (lâminas 84–91) ----------
    au("au-inclusoes", ORG("<b>Viral inclusion bodies</b>:<br>- cytoplasmic: {{c1::poxvirus}}, {{c1::reovirus}}, {{c1::paramyxovirus}}, {{c1::rabies virus}}<br>"
                           "- nuclear: {{c2::herpesvirus}}, {{c2::adenovirus}}, {{c2::parvovirus}}"),
       "A-aula", G_, "Corpúsculos de inclusão: citoplasmáticos × nucleares", 85, "lâmina 85; provas 2015 P2 4.8 (corpúsculos de inclusão)",
       extra="- Only some viruses make inclusion bodies; the presence of one helps recognize a viral infection"),
    sh(1791984887454, "azul", G_, "Inclusões: acúmulos de proteínas ou partículas no local de montagem", 85, "A-aula: lâminas 85–86; card da 61"),
    K(1502570605009, "A-aula", G_, "Guarnieri: inclusões citoplasmáticas do poxvírus", 85, "lâminas 85–86; seção Physeo de replicação"),
    K(1516475620459, "A-aula", G_, "Corpos de Negri: inclusões citoplasmáticas da raiva", 85, "lâmina 85 (vírus da raiva); seção Physeo"),
    K(1516475827100, "A-aula", G_, "Corpos de Cowdry: inclusões nucleares dos herpesvírus", 85, "lâmina 85 (herpesvírus: intranuclear); seção Physeo"),
    au("au-liberacao", ORG("<b>Viruses are released by</b>:<br>- {{c1::lysis}}<br>- {{c2::budding}}<br>- cell-to-cell passage<br>"
                           "- formation of {{c3::syncytia}}"),
       "V-pilar", G_, "Formas de liberação do vírus", 87, "lâminas 87 e 237; apostila guia de Micro e prova 2015 P2 4.3 (sincícios e lise)",
       extra="- Budding gives enveloped viruses their envelope<br>- Syncytia come from fusion of infected cells with neighbors"),
    sh(1792243082169, "azul", G_, "Envelope vem da membrana da célula", 88, "A-aula: lâminas 88–89 (brotamento); card da 57"),
    sh(1791984888354, "azul", G_, "Sincícios: células multinucleadas por fusão", 87, "A-aula: lâmina 87; card da 61"),
    sh(1791984887204, "azul", G_, "Efeito citopático: alterações estruturais da replicação viral", 238, "A-aula: lâmina 238 e apostila guia de Micro (efeito citopático); card da 61"),
    au("au-resumo-dna", "<b>Polyomavirus and papillomavirus</b> use the {{c1::host}} polymerase, whereas adenovirus and herpesvirus use a {{c2::viral}} one",
       "A-aula", G_, "Resumo: polimerase celular × viral nos vírus de DNA", 91, "lâminas 91 e 241 (resumão da replicação viral)",
       extra="- Poxviruses are the DNA-virus exception: they replicate in the cytoplasm with a viral polymerase<br>- Hepadnaviruses are a special case"),
    # ---------- H. Antivirais (lâminas 93–178) ----------
    au("au-antiv-mec", ORG("<b>An antiviral blocks</b>:<br>- {{c1::extracellular}} virions<br>- {{c1::attachment}} or entry<br>- genome {{c1::replication}}<br>"
                           "- viral {{c1::protein}} synthesis or function<br>- {{c1::assembly}} or release"),
       "V-pilar", H_, "Pontos do ciclo onde o antiviral age", 95, "lâmina 95; monitoria P3 de Micro (mecanismos de ação)",
       extra="- A molecule works as an antiviral if it inhibits a step of replication without being too toxic to the host"),
    K(1506806715774, "V-hy", H_, "Enfuvirtida liga gp41 e impede a fusão", 102, "lâmina 102 (inibidores de fusão); seção Bootcamp 39"),
    K(1506806433678, "V-hy", H_, "Maraviroque inibe a ligação da gp120 ao CCR5", 103, "lâmina 103 (inibidor de entrada); seção Bootcamp 39"),
    K(1516324096049, "V-hy", H_, "Canal M2 garante o pH para o desnudamento do influenza", 104, "lâmina 104 (inibidor do desnudamento); seção Bootcamp 39"),
    K(1516324301529, "V-hy", H_, "Amantadina e rimantadina inibem o canal M2 do influenza A", 105, "lâmina 105; seção B&B de antivirais"),
    au("au-antiv-pol-propria", "Viral <b>polymerase inhibitors</b> only work on viruses that encode their {{c1::own}} {{c2::polymerase}}", "V-prova", H_,
       "Inibidores de polimerase: só para vírus com polimerase própria", 107, "lâmina 107; monitoria P3 (não serve para HPV nem poliomavírus)",
       extra="- They can be nucleoside/nucleotide analogs or non-analogs<br>- HPV and polyomaviruses use the host polymerase, so these drugs do not work"),
    K(1467683788745, "A-aula", H_, "Nucleosídeo = base + açúcar", 108, "lâmina 108 (nucleosídeo × nucleotídeo); seção Bootcamp 39"),
    K(1467683795991, "A-aula", H_, "Nucleotídeo = base + açúcar + fosfato", 108, "lâmina 108; seção B&B de antivirais"),
    K(1506723403021, "A-aula", H_, "Aciclovir, famciclovir e valaciclovir são análogos da guanosina", 109, "lâminas 109–116 (análogos de nucleosídeos); seção Bootcamp 39"),
    K(1506723704374, "A-aula", H_, "Timidina quinase viral monofosforila o aciclovir", 111, "lâmina 111 (ativação do aciclovir); seção Bootcamp 39"),
    K(1506724128411, "A-aula", H_, "Aciclovir trifosfato entra no DNA viral e inibe a polimerase", 111, "lâmina 111; apostila guia de Micro (pausa a síntese do DNA do herpes)"),
    K(1403635898739, "A-aula", H_, "Resistência ao aciclovir: timidina quinase mutada ou ausente", 111, "lâmina 111; apostila guia de Micro (uma mutação reduz a eficácia)"),
    K(1506724515933, "A-aula", H_, "Sem timidina quinase viral, o aciclovir não age em CMV e EBV", 111, "lâmina 111; seção Bootcamp 39"),
    K(1506724662638, "V-hy", H_, "Cidofovir e foscarnet não precisam de timidina quinase", 117, "lâminas 116–117; seção Bootcamp 39"),
    K(1403636336526, "V-hy", H_, "Foscarnet liga o sítio do pirofosfato da polimerase", 117, "lâmina 117 (foscarnet); seção B&B de antivirais"),
    K(1506784777103, "V-hy", H_, "Inibidores da transcriptase reversa impedem o RNA virar DNA", 119, "lâmina 119 (inibidores da transcriptase reversa); seção Bootcamp 39"),
    K(1506784318198, "A-aula", H_, "NRTIs não têm hidroxila 3′", 119, "lâminas 119–122 (análogos de nucleosídeos); seção Bootcamp 39"),
    K(1506784353867, "A-aula", H_, "NRTIs terminam a cadeia de DNA precocemente", 122, "lâmina 122 (AZT trifosfato); seção Bootcamp 39"),
    K(1506784514467, "A-aula", H_, "A maioria dos NRTIs precisa ser fosforilada", 122, "lâmina 122 (AZT: três fosforilações); seção Bootcamp 39"),
    K(1506785118508, "A-aula", H_, "Tenofovir é nucleotídeo, não nucleosídeo", 120, "lâmina 120 (tenofovir, PMPA); seção Bootcamp 39"),
    K(1506789392960, "V-hy", H_, "NNRTIs ligam a transcriptase reversa em sítio diferente do NRTI", 123, "lâminas 123–124 (não análogos); seção Bootcamp 39"),
    K(1506789263570, "A-aula", H_, "NNRTIs não precisam de fosforilação", 123, "lâmina 123; seção Bootcamp 39"),
    K(1461797689978, "A-aula", H_, "Sofosbuvir é um análogo de nucleotídeo que inibe a NS5B do HCV", 127, "lâminas 126–127 (inibidores da NS5B); seção Bootcamp 39"),
    K(1514740864172, "A-aula", H_, "Ribavirina é um análogo da guanosina que inibe a IMP desidrogenase", 127, "lâmina 127 (ribavirina); seção Bootcamp 39"),
    K(1506807161520, "V-hy", H_, "Qual enzima integra o dsDNA do HIV ao genoma da célula? Integrase", 131, "lâmina 131 (inibidores da integrase); seção Bootcamp 39"),
    K(1506807835841, "V-hy", H_, "Inibidores da integrase bloqueiam a inserção do dsDNA no genoma", 131, "lâmina 131; seção Bootcamp 39"),
    K(1516324778471, "V-hy", H_, "Zanamivir e oseltamivir inibem a neuraminidase do influenza A e B", 134, "lâminas 134–135 (inibidores do brotamento); seção Bootcamp 39"),
    K(1516323747313, "A-aula", H_, "Neuraminidase cliva a ligação entre HA e ácido siálico", 135, "lâmina 135 (HA e NA); seção Bootcamp 39"),
    sh(1792243080522, "azul", H_, "Neuraminidase libera o vírion maduro", 135, "A-aula: lâmina 135; card da 57"),
    sh(1792243080096, "azul", H_, "Hemaglutinina liga o ácido siálico", 135, "A-aula: lâmina 135; card da 57"),
    K(1502070156173, "A-aula", H_, "Inibidores da protease bloqueiam o corte das proteínas virais", 137, "lâmina 137 (inibidores de proteases); seção Bootcamp 39"),
    K(1506795652147, "V-hy", H_, "Inibidores da protease impedem o vírion maduro a partir de poliproteínas", 138, "lâminas 138–139 (poliproteínas); seção Bootcamp 39"),
    K(1506631004332, "A-aula", H_, "Hepatite C é tratada com inibidores de protease e de polimerase", 151, "lâminas 150–154 (história de sucesso); seção Bootcamp 39"),
    K(1506783017772, "V-hy", H_, "HAART usa no mínimo três fármacos para evitar resistência", 156, "lâminas 156 e 163; seção Bootcamp 39"),
    K(1506783163535, "V-hy", H_, "HAART: dois NRTIs mais NNRTI, inibidor de protease ou da integrase", 163, "lâmina 163 (terapia combinada); seção Bootcamp 39"),
    K(1502069492941, "V-hy", H_, "O alicerce do HAART são os NRTIs", 157, "lâmina 157; seção Bootcamp 39"),
    K(1489970693302, "V-hy", H_, "Interferon α e β: glicoproteínas que preparam as células vizinhas", 176, "lâmina 176 (interferon como medida simples); seção Bootcamp 39"),
]

_CZ = _re.compile(r"\{\{c(\d+)::((?:(?!\}\}).)*?)(::(?:(?!\}\}).)*?)?\}\}", _re.S)
def _bold_cloze(t):
    """F-20261020-CODEX-03: toda resposta de cloze autoral em negrito."""
    def sub(m):
        corpo = m.group(2)
        if "<b>" not in corpo and "<strong>" not in corpo:
            corpo = f"<b>{corpo}</b>"
        return "{{c%s::%s%s}}" % (m.group(1), corpo, m.group(3) or "")
    return _CZ.sub(sub, t)
for _c in CARDS:
    if _c["kind"] == "autoral":
        _c["text"] = _bold_cloze(_c["text"])

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1483913062659": "- Retroviral DNA is transcribed in the nucleus, and influenza makes its mRNA there",
 "ak1516850294247": "- A circular genome has no ends, so it avoids the 5′-end replication problem",
 "ak1493398712106": "- The HPV 16 genome has 7,906 base pairs",
 "ak1516930208305": "- The origins lie at both ends and a terminal protein primes the synthesis",
 "ak1506554995533": "- Hepatitis D is a circular (−) RNA that needs the HBsAg of hepatitis B",
 "ak1506627151740": "- The (+) RNA is translated into one polyprotein, which the viral protease cleaves",
 "ak1506554976089": "- The partially double-stranded circle is completed by the viral polymerase in the nucleus",
 "ak1516321532745": "- Segmented genomes allow reassortment between strains",
 "ak1523806616492": "- Reassortment swaps whole segments and can create new antigens (antigenic shift)",
 "ak1608910407576": "- Coronavirus virions assemble on the ER–Golgi membranes and leave in vesicles",
 "ak1516475620459": "- Negri bodies sit in the cytoplasm of neurons, such as hippocampal and Purkinje cells",
 "ak1516475827100": "- Adenovirus and parvovirus also form intranuclear inclusions",
 "ak1506783569000": "- It blocks CCR5, the coreceptor HIV uses early in infection",
 "ak1516324096049": "- Amantadine and rimantadine block this channel and trap the virus in the endosome",
 "ak1516324579285": "- Resistance made them obsolete; neuraminidase inhibitors replaced them",
 "ak1467683788745": "- Nucleoside analogs, such as acyclovir, receive their phosphates inside the cell",
 "ak1467683795991": "- Tenofovir is a nucleotide analog, so it needs only two more phosphates",
 "ak1506783462443": "- Didanosine is a nucleoside analog that terminates the viral DNA chain",
 "ak1506724574195": "- The viral thymidine kinase gives the first phosphate to acyclovir",
 "ak1506724128411": "- Acyclovir has no 3′-OH, so the DNA chain cannot be extended",
 "ak1403635898739": "- Without the viral kinase, acyclovir is never activated",
 "ak1506724515933": "- Only HSV and VZV encode a thymidine kinase that activates it well",
 "ak1506727367546": "- A viral kinase adds the first phosphate (UL97 in CMV) and cellular kinases the rest",
 "ak1506726911137": "- Like acyclovir, they are activated by a viral kinase",
 "ak1506727746723": "- Its incorporation slows and stops the elongation of viral DNA",
 "ak1506727932519": "- Valganciclovir is the oral prodrug of ganciclovir",
 "ak1403636599345": "- Cidofovir is already a nucleotide analog, so it does not need the viral kinase",
 "ak1506724662638": "- Resistance to these drugs comes from mutations of the viral DNA polymerase",
 "ak1506728737669": "- Foscarnet binds the pyrophosphate site of the polymerase and needs no phosphorylation",
 "ak1506784318198": "- Without the 3′-OH, the next nucleotide cannot be added",
 "ak1506783521685": "- AZT triphosphate ends the DNA chain made by reverse transcriptase",
 "ak1506783486518": "- A cytidine analog, used together with other NRTIs in HAART",
 "ak1506783497051": "- A thymidine analog, listed among the nucleoside analogs of the lecture",
 "ak1506783296016": "- Its active form is carbovir, a guanosine analog",
 "ak1506783471847": "- Often combined with tenofovir in PrEP",
 "ak1506784467378": "- With no 3′-OH there is no phosphodiester bond with the next nucleotide",
 "ak1506789392960": "- NNRTIs bind an allosteric pocket and need no phosphorylation",
 "ak1506783862734": "- Etravirine and rilpivirine belong to the same class",
 "ak1506783854533": "- Efavirenz is part of first-line HAART regimens with two NRTIs",
 "ak1506783836022": "- NNRTIs do not compete with nucleotides for the active site",
 "ak1514740864172": "- Ribavirin depletes the guanine nucleotide pool needed for viral RNA synthesis",
 "ak1514740606355": "- It acts through IMP dehydrogenase, lowering GTP",
 "ak1476496198826": "- Both drugs reduce the guanine nucleotides needed for nucleic acid synthesis",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

exec((HERE / "exclusoes.py").read_text(encoding="utf-8")) if (HERE / "exclusoes.py").exists() else None

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer; as figuras da aula são esquemas de cada vírus, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
DUPLICACAO = {
    "au-pequenos-dna": "poxvírus e adenovírus aparecem em outros cards; aqui é a divisão dos vírus de DNA entre os que dependem da célula e os que codificam a maquinaria",
    "au-antiv-pol-propria": "polimerase própria aparece nos cards do poxvírus e do RNA −; aqui é a condição para um inibidor de polimerase funcionar",
    "au-nirmatrelvir": "protease aparece nos cards dos inibidores de protease do HIV e do HCV; aqui é o antiviral de uso emergencial na COVID-19",
    "au-neg-pol-proteina": "a polimerase do RNA − aparece no card da polimerase própria; aqui é a condição de a polimerase só copiar RNA no nucleocapsídeo",
    "au-montagem": "citosol, RE-Golgi, membrana e núcleo aparecem em cards de replicação e de HIV; aqui é a lista dos locais de montagem",
    "au-inclusoes": "Negri, Cowdry e Guarnieri aparecem em cards isolados; aqui é a classificação por local (citoplasma × núcleo) e por vírus",
    "au-antiv-poucos": "latência e alvos aparecem em cards de HIV e herpes; aqui são os motivos gerais da escassez de antivirais",
    "au-antiv-mec": "adsorção, replicação e liberação aparecem nos cards de cada classe; aqui é o mapa dos pontos do ciclo atacados",
    "au-haart-classes": "as classes aparecem nos cards por fármaco; aqui é o conjunto das cinco classes do HAART",
    "au-herpes-circ": "forma linear ou circular aparece nos cards de genoma; aqui é a estratégia de replicação por círculo rolante",
    "au-pox-precoces": "polimerase do vírion aparece no card da pol própria do poxvírus; aqui é o momento dos mRNAs precoces imediatos",
    "au-pox-dna-nu": "a RNA polimerase do poxvírus aparece no card da pol própria; aqui é a consequência, o DNA purificado não infeccioso",
    "au-rna-genomas": "tipos de genoma aparecem nos cards por vírus; aqui é o quadro da lâmina 63 reunido",
    "au-retro-rt": "a transcriptase reversa aparece nos cards de HIV e dos NRTIs; aqui é o empacotamento no vírion e o provírus",
    "au-reo-pol": "polimerase no vírion aparece no card do RNA −; aqui inclui o dsRNA e o genoma não infeccioso",
    "au-etapas": "adsorção, penetração e desnudamento aparecem em cards isolados de cada etapa; aqui é a sequência completa do ciclo",
    "au-desnud": "citoplasma e endossomo aparecem nos cards de local de replicação; aqui é onde ocorre o desnudamento",
    "au-grandes-dna": "poxvírus aparece nos cards de replicação citoplasmática; aqui é o grupo de vírus de DNA que codificam a maquinaria",
    "au-prot-dna": "timidina quinase aparece nos cards do aciclovir; aqui é uma das proteínas que o vírus de DNA codifica",
    "au-primers": "adenovírus, parvovírus e poxvírus aparecem em outros cards; aqui é o tipo de primer de cada grupo",
    "au-polyoma-t": "helicase aparece nos cards da replicação celular; aqui é a função do antígeno T do poliomavírus",
    "au-fusao-env": "gp41 e a fusão aparecem também no card do HIV; aqui o alvo é quais vírus envelopados entram por fusão",
    "au-rdrp-todos": "RdRp aparece também no card do coronavírus; aqui o alvo é a regra geral e a exceção dos retrovírus",
    "au-resumo-dna": "polimerase celular × viral aparece nos cards de adenovírus e HPV; aqui é o resumo comparativo da aula",
}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Definir as etapas do ciclo viral, comparar a replicação de vírus de DNA e de RNA por grupo de Baltimore e explicar os mecanismos "
                "de ação das classes de antivirais sobre cada etapa.",
    "centrais": [
        ("ciclo", "au-produtiva", "au-etapas", "au-penetracao", "au-desnud"),
        ("vírus de DNA", "au-pequenos-dna", "au-grandes-dna", "au-primers", "au-polyoma-t", "au-adeno-primer", "au-herpes-circ"),
        ("vírus de RNA", "au-rdrp-todos"),
        ("montagem e liberação", "au-liberacao"),
        ("antivirais", "au-antiv-mec", "au-antiv-pol-propria", "au-haart-classes"),
    ],
    "exemplos": ["estruturas químicas dos fármacos", "tabela de fármacos para COVID-19", "gráficos de desenvolvimento de fármacos"],
    "outras_aulas": [("classificação e estrutura dos vírus", "57 Princípios gerais dos vírus (sh)"),
                     ("efeito citopático e patologia viral", "61 Patologia da infecção viral (sh)"),
                     ("patogênese viral", "59 Patogênese da infecção viral"),
                     ("efeitos adversos dos antivirais", "UC19 Farmacologia"),
                     ("HPV e câncer", "78 Agentes carcinogênicos biológicos")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
