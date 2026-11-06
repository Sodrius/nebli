# Especificação curada — 61 Patologia da infecção viral v3 (UC03 P3, Patologia; Prof. Luiz Fernando Ferraz da Silva; 29 lâminas). Pipeline v10
# (29/10, F-20261029-CLAUDE-03: "VIROU UM DECK DE HEPATITE, MAS ISSO ERA SÓ PARA ILUSTRAR / O COMEÇO DA AULA É MAIS IMPORTANTE").
# O deck é a patologia de QUALQUER infecção viral: o vírus lesa a célula diretamente (lise → inflamação aguda; transformação → neoplasia; o resto é
# o efeito citopático: inclusões no compartimento onde o vírus faz seus componentes, sincícios, coilócitos) e lesa pelo que provoca na resposta
# (inata no agudo, com IFN-I e NK; adaptativa no crônico, porque o vírus está dentro da célula). As lâminas 14–29 são o exemplo da hepatite
# ("a combinação de tudo") e entram só pelos princípios gerais que mostram, escritos como princípios.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 10
SECOES_MOTIVO = ("Aula de princípio geral (morfologia da infecção viral): nenhuma seção de recurso do AnKing é do seu assunto; as de mecanismos de "
                 "infectividade, NK, interferons, CTL, inflamação crônica, herpesvírus, sarampo e HPV foram lidas e delas entra só o card que responde a um item aprender")
SECOES_DA_AULA = []
AUTORAL_EXCECAO = ("Aula de princípio geral de patologia com pouco AnKing do seu assunto: a busca nos três caminhos achou acervo para inclusões, sincícios, "
                   "coilócito, IFN e NK (entram os cards de acervo, a maioria já viva em outras aulas e associada), mas não para os princípios de patologia geral da fala "
                   "(dois efeitos, destinos dos efeitos diretos, inclusão por montagem desproporcional, sincício × granuloma, curva da resposta, IFN-I que ganha "
                   "tempo, apoptose dirigida × necrose que destrói a matriz). Cobertura da aula vem antes do teto (F-20261029-CLAUDE-02); todo autoral está num item do mapa.")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt61-20261029a"
SHORT = "pt61"
LESSON = "2026-uc03-patologia-61-patologia-infeccao-viral"
DECK = "NEBLI::UC03::P3::Patologia::61 Patologia da infecção viral"
CRITERIOS = "MEMORY.md + pipeline v10 (EXECUCAO-DECK-AULA) + FEEDBACKS até F-20261029-CLAUDE-03 + GUIA-1 a GUIA-4 de 29/10"
_IMGS = ("raiva", "sarampo", "sincicio", "coilocito", "curva2", "vidro-fosco", "ihq-hbsag", "ihq-hbcag", "infiltrado", "necrose",
         "apoptose", "interface", "linf-b", "septos")
MEDIA = {f"pt61-{n}.png": f"img/pt61-{n}.png" for n in _IMGS}
IMG = lambda n, w=300: f'<img src="pt61-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (29/10): seções de recurso do AnKing (mecanismos de infectividade viral, NK, interferons, CTL, inflamação crônica, herpesvírus, "
         "sarampo, HPV; busca/secoes); palavra-chave com sinônimos em AnKing e Referências Externas (busca/anking.txt); significado em AnKing, nos "
         "acervos externos e no NEBLI vivo, uma consulta por card planejado (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


EXCLUIDOS = [
 (1516475620459, "repete a inclusão citoplasmática da raiva (fica 1516474665512, com os dois irmãos)"),
 (1516475256424, "repete a localização citoplasmática do Negri"),
 (1516474771301, "locais do Negri no hipocampo e no cerebelo: detalhe da raiva, fora do ponto da lâmina 5"),
 (1502152318872, "Cowdry em herpesvírus com três clozes: o mesmo fato de 1516475827100, que pergunta pelo compartimento"),
 (1502152099123, "repete o compartimento nuclear do Cowdry"),
 (1403141269124, "CMV e olho de coruja no sentido inverso: fica 1503861947945, que descreve a inclusão"),
 (1506459892639, "repete 1506298786823 (proteína F funde células)"),
 (1506299214372, "Warthin-Finkeldey em linfócitos: detalhe; fica 1506298973285"),
 (1506290563519, "Tzanck: método diagnóstico de herpes, fora do recorte morfológico da lâmina 7"),
 (1394242914870, "repete o coilócito (fica 1385335604751 com o halo perinuclear)"),
 (1463094113348, "repete o coilócito"),
 (1394239958498, "tipos de HPV de alto risco sem a displasia: fica 1405375421095, que liga à prova 2016"),
 (1489970516941, "IFN-γ e MHC II: o contraste com o tipo I fica em au-ifn-tipo"),
 (1503876244084, "repete 1503876156644 (CMV bloqueia MHC I)"),
 (1487117295752, "perforina e granzima do CTL: repete a via da NK (1487117308213); a via do CD8 entra por Fas-FasL"),
 (1486522630094, "hepatite crônica no espaço porta: o princípio entra por au-periportal e pela zona I"),
 (1521044225681, "'só anti-HBs = vacinação': sorologia da doença do exemplo; o princípio entra por au-anti-hbc"),
 (1502066053913, "vacina recombinante de HBsAg: vai no verso de au-anti-hbc"),
 (1521044306629, "HBeAg e infectividade: detalhe da doença do exemplo; vai no verso de au-anti-hbc"),
 (1584230461040, "caso de sorologia: clínica"),
 (1495743863878, "interpretação de painel sorológico: clínica"),
 (1506628692802, "Councilman em HAV e febre amarela: detalhe da doença"),
 (1486522654540, "células de Ito e TGF-β: aula de reparo (65)"),
 (1468250259504, "reticulina = colágeno III: vai no verso de au-colageno"),
 (1461794652364, "IFN-α como fármaco: farmacologia, fora do ciclo básico desta aula"),
 (1519852532171, "miocardite viral: o princípio do infiltrado linfocitário entra por au-mononuclear sem puxar outra doença"),
]
FORA_DO_RECORTE = [
 "Capa (lâmina 1): sem conteúdo.",
 "Estrutura e ciclo do HBV (lâminas 14–15: Baltimore VII, cccDNA, montagem no retículo): ciclo é da 58; aqui só onde cada antígeno aparece, no verso de au-ihq.",
 "Esteatose do HCV (lâmina 18): mecanismo da doença do exemplo; o princípio (maquinaria sequestrada) já está em au-sequestro e no verso de au-vidro-fosco.",
 "Sorologia completa, janela imunológica, painel e tratamento das hepatites: o exemplo entra só pelo princípio estrutural (au-anti-hbc).",
 "Galeria vírus a vírus do material (EBV/Reed-Sternberg, zika, influenza, HIV, adenovírus): entra só o que mostra onde o vírus replica (Cowdry, olho de coruja, Guarnieri) ou o sincício (sarampo).",
 "Sensores, ISGs e sinalização do IFN: 63 Resposta imune a vírus.",
]
A_, B_, C_, D_, E_, X1, X2, X3, X4, X5, X6 = ("A-dois-efeitos", "B-efeitos-diretos", "C-citopatico", "D-resposta", "E-ifn-nk",
                                             "X1-exemplo-destino", "X2-exemplo-efeito-do-virus", "X3-exemplo-onde", "X4-exemplo-morte",
                                             "X5-exemplo-atividade", "X6-exemplo-arquitetura")

CARDS = [
 # ---------- Lâmina 2: dois efeitos (princípio) ----------
 sh(1792753616942, "azul", A_, "Imunopatologia: dano pela própria resposta", 2, "A-aula: card da 59; a lâmina 2 diz que a resposta é um dos dois efeitos"),
 # ---------- Lâminas 3–4: efeitos diretos e seus destinos (princípio) ----------
 au("au-efeitos", ORG("<b>Direct viral effects on the cell</b> lead to:<br>- cell lysis: {{c1::acute inflammation}}<br>- transformation: {{c1::neoplasia}}<br>- blocked synthesis, syncytia, cytoskeleton, arrested cycle: {{c1::cytopathic effect}}"),
    "V-pilar", B_, "Três destinos dos efeitos diretos", 4, "lâminas 3–4; apostila guia p. 43; UC3.pdf p. 429", motivacao="m3", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Quando eu tenho lise celular, normalmente eu vou ter um quadro de inflamação aguda.",
    fontes=F("lâmina 4", "Lise celular Inflamação Aguda … Transformação celular e proliferação celular Neoplasia … Efeito citopático"),
    sem_imagem="lâmina 4 é lista sem figura",
    extra="Lysis spills cell contents, so the tissue mounts acute inflammation.<br>Transformation needs viral genes acting on host growth control.<br>The cytopathic effect is what the pathologist sees in the infected cell."),
 au("au-sequestro", "In a <b>lytic viral infection</b>, the host machinery is diverted to viral genomes and proteins, so the cell usually stops {{c1::dividing::cell activity}}",
    "A-aula", B_, "Síntese sequestrada para o vírus", 4, "transcrição lâmina 4", motivacao="m5",
    fontes=F("transcrição, lâmina 4", "uma célula infectada pelo vírus não está afim de fazer replicação do material genético dela. Ela está também com a maquinaria sequestrada"),
    sem_imagem="mecanismo, lâmina sem figura",
    extra="Synthesis is not switched off, it is redirected to viral proteins.<br>Transforming viruses do the opposite and push the cell into the cycle.<br>Proteins the cell can no longer process pile up, which is how cytopathic accumulations start."),
 au("au-transformacao", "When an integrated viral genome alters host <b>growth-control genes</b>, the transforming mechanism is called {{c1::insertional mutagenesis}}",
    "A-aula", B_, "Transformação viral por inserção", 4, "transcrição lâmina 4; Robbins cap. 8 p. 344", motivacao="m6",
    fontes=F("Robbins cap. 8 p. 344", "mutagêneses insercionais (nas quais a função dos genes do hospedeiro é alterada por genes virais inseridos no genoma do hospedeiro)"),
    sem_imagem="mecanismo, lâmina sem figura",
    extra="Typical case: viral DNA lands next to the promoter of a cell-cycle gene.<br>The cell then proliferates without control, the path from infection to neoplasia."),
 # ---------- Lâminas 5–6: inclusões (princípio) ----------
 au("au-inclusao", "Viral <b>inclusions</b> form when assembly stops at the {{c1::scarcest}} component and the excess components pile up",
    "V-prova", C_, "Inclusão por produção desproporcional", 5, "lâmina 5; transcrição; prova 2024 P3 1.2", motivacao="m8",
    fontes=F("transcrição, lâmina 5", "para eu montar a partícula viral inteira, quem manda é o que tem menos."),
    sem_imagem="princípio; as figuras de inclusão estão em au-raiva-sarampo",
    extra="Viral parts are made out of proportion, like an unbalanced production line.<br>Lots of protein without genome cannot become virions.<br>The excess stays where it is made, in the cytoplasm or in the nucleus."),
 K(1516474665512, "V-prova", C_, "Negri: inclusão citoplasmática eosinofílica da raiva", 5, "lâmina 5 (raiva, inclusão citoplasmática)"),
 au("au-raiva-sarampo", "In infected neurons, <b>rabies</b> forms only {{c1::cytoplasmic}} inclusions, whereas <b>measles</b> can also form {{c1::intranuclear}} ones",
    "A-aula", C_, "Citoplasmática × nuclear", 6, "lâminas 5–6; transcrição", motivacao="m9",
    fontes=F("transcrição, lâmina 6", "Eu posso ter esses acúmulos no núcleo. Seja porque eu tenho um papel de material genético associado ou porque alguns desses elementos são produzidos ou processados em ambiente nuclear."),
    slide_sem_alternativa="a figura é a lâmina que o professor comenta; não há equivalente no AnKing",
    extra="The inclusion sits in the compartment where viral parts are made or processed.<br>Measles inclusions can be cytoplasmic and nuclear; a neuron with a nuclear one is the classic image.<br>" + IMG("raiva") + IMG("sarampo")),
 K(1502152021975, "A-aula", C_, "Vírus de DNA replicam no núcleo", 6, "lâmina 2 (biologia do vírus decide a lesão) e 6 (inclusão nuclear)"),
 K(1516475827100, "A-aula", C_, "Herpesvírus: inclusão nuclear (Cowdry)", 6, "UC3.pdf e monitoria (galeria de efeitos citopáticos); Robbins p. 348"),
 K(1503861947945, "R-detalhe", C_, "CMV: olho de coruja nuclear", 6, "UC3.pdf p. 431 e monitoria (olho de coruja)"),
 K(1502570605009, "R-detalhe", C_, "Poxvírus: inclusão citoplasmática (Guarnieri)", 6, "e-se da lâmina 2: vírus de DNA que replica no citoplasma faz inclusão citoplasmática"),
 # ---------- Lâmina 7: sincício (princípio) ----------
 K(1506298786823, "A-aula", C_, "Proteína F funde células em gigantes multinucleadas", 7, "lâmina 7; transcrição; Robbins p. 348 (policárions)"),
 K(1506457588894, "V-prova", C_, "VSR: proteína F → células gigantes", 7, "lâmina 7 (vírus sincicial respiratório)", sem_imagem="a microscopia do sincício está em au-sincicio-granuloma"),
 K(1506298973285, "R-detalhe", C_, "Sarampo: Warthin-Finkeldey", 7, "UC3.pdf p. 433 e monitoria (sarampo com células gigantes); Robbins p. 348"),
 au("au-sincicio-granuloma", ORG("<b>Viral syncytium vs. granuloma giant cell</b>: the syncytium has no<br>- rim of {{c1::lymphocytes::l…}}<br>- {{c1::epithelioid::e…}} macrophages<br>- central {{c1::necrosis::n…}}"),
    "A-aula", C_, "Sincício × granuloma", 7, "lâmina 7; transcrição; prova 2017 P3 1.3", motivacao="m11", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Não tem aquela estrutura com um halo de linfócitos, com um grupo de células epitelióides e uma necrose central.",
    fontes=F("transcrição, lâmina 7", "Não tem aquela estrutura com um halo de linfócitos, com um grupo de células epitelióides e uma necrose central."),
    extra="The syncytium is the virus fusing infected cells, even epithelial ones.<br>The granuloma giant cell is the immune response organizing activated macrophages.<br>" + IMG("sincicio")),
 # ---------- Lâmina 8: coilócito (princípio) ----------
 sh(1793199694409, "verde", C_, "Coilócito: halo perinuclear do HPV", 8, "V-hy: card da 60 (AnKing 1385335604751); lâmina 8"),
 K(1405375421095, "A-aula", C_, "HPV 16 e 18 na displasia cervical", 8, "lâmina 8; prova 2016 P3 1.2 (coilocitose + displasia → HPV-16)", sem_imagem="o coilócito com figura é o card da 60 associado logo antes"),
 # ---------- Lâmina 9: resposta aguda × crônica (princípio) ----------
 au("au-quadros", ORG("<b>Viral infections</b> by course:<br>- acute (respiratory, gut viruses): mostly {{c1::innate}} immunity<br>- chronic (hepatitis B, HIV): mostly {{c1::adaptive}} immunity"),
    "V-pilar", D_, "Tipo de quadro decide o braço imune", 9, "lâmina 9; transcrição lâmina 9", motivacao="m13", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Quadros sub-agudos e crônicos – Resposta Imune Adaptativa",
    fontes=F("transcrição, lâmina 9", "Os vírus de hepatite, que cronificam, HIV, HTLV, uma série de outros vírus, que têm um processo patológico muito mais complexo"),
    sem_imagem="lâmina 9 é lista",
    extra="It is predominance, not exclusivity: both arms act in every infection.<br>Innate: barriers, NK cells, macrophages and complement. Adaptive: T cells, B cells and antibodies.<br>In acute infections adaptive immunity matters most for finishing the job and for memory."),
 au("au-nk-neutrofilo", "In <b>acute viral infections</b>, {{c1::NK cells}} are central innate killers, a role neutrophils play in bacterial infections",
    "A-aula", D_, "NK na virose × neutrófilo na bacteriana", 9, "transcrição lâmina 9", motivacao="m14",
    fontes=F("transcrição, lâmina 9", "dos quadros bacterianos em geral, a gente fala muito de macrófago e muito de neutrófilo. … Aqui, gente, a gente tem uma participação importante também de células NK."),
    sem_imagem="contraste da fala, sem figura",
    extra="Neutrophil enzymes and oxygen radicals act outside cells, where bacteria are.<br>Viruses hide inside cells, so the killer has to recognize and destroy the infected cell itself."),
 au("au-complemento", "Besides neutralizing enveloped viruses, <b>complement</b> can destroy infected cells that display viral proteins through the {{c1::membrane attack complex}}",
    "A-aula", D_, "Complemento contra célula infectada", 9, "lâmina 9; transcrição", motivacao="m15",
    fontes=F("transcrição, lâmina 9", "Uma, neutralizar as próprias partículas, o que é menos comum e acaba sendo mais útil em vírus envelopados."),
    sem_imagem="mecanismo, lâmina sem figura",
    extra="Neutralizing free virions is the less common role, more useful against enveloped viruses.<br>Complement is a helper: most infected cells are killed by CD8 T cells."),
 K(1487117300306, "V-pilar", D_, "CD8 mata por Fas-FasL", 9, "transcrição lâmina 9 (CD8 induzindo apoptose por via FAS-FAS ligante)"),
 sh(1791625429957, "verde", D_, "CD8 mata célula infectada por apoptose", 9, "V-hy: card de imuno; a lâmina 9 diz que é o principal meio"),
 au("au-mononuclear", "The inflammatory infiltrate of a persistent <b>viral infection</b> is typically {{c1::mononuclear}}",
    "A-aula", D_, "Infiltrado mononuclear na virose", 9, "transcrição lâminas 9 e 19; Robbins cap. 8 p. 348", motivacao="m16",
    fontes=F("Robbins cap. 8 p. 348", "linfócitos predominam na infecção pelo HBV ou infecções virais do cérebro. A presença destes linfócitos reflete respostas imunes mediadas por células"),
    extra="Lymphocytes and macrophages dominate, unlike the neutrophils of pyogenic bacteria.<br>The lymphocytes are cell-mediated immunity against infected cells.<br>Where the virus acts mostly by cytopathic effect, inflammatory cells are sparse.<br>" + IMG("infiltrado")),
 # ---------- Lâmina 10: a curva (princípio) ----------
 au("au-curva", "<b>Type I interferon (IFN-I)</b> and NK cells peak early in a viral infection, while {{c1::T cells}} and then {{c2::antibodies}} dominate later",
    "V-pilar", D_, "Curva temporal da resposta", 10, "lâmina 10 (curva); transcrição", motivacao="m17",
    fontes=F("lâmina 10", "Resposta natural … Resposta adquirida … Linfócitos T … Anticorpos"),
    extra="Early innate responses stop the exponential rise of the virus.<br>T cells then kill infected cells, and antibodies neutralize virus released when they burst.<br>" + IMG("curva2", 380)),
 au("au-intracelular", "<b>Innate immunity</b> rarely clears a viral infection alone because the virus replicates {{c1::inside cells}}",
    "V-pilar", D_, "Inata não basta: vírus intracelular", 10, "transcrição lâmina 10", motivacao="m18",
    fontes=F("transcrição, lâmina 10", "Porque tem um monte de gente dentro da célula. A imunidade inata gosta de enxergar coisas ou na superfície ou fora da célula"),
    sem_imagem="princípio; a curva está em au-curva",
    extra="So clearance needs the full arsenal: cells that kill infected cells and antibodies that catch released virus.<br>A bacterial infection, by contrast, is often cleared by neutrophils and macrophages alone."),
 au("au-ifn-tipo", "The <b>interferon</b> that rises early in a <b>viral infection</b> is type {{c1::I}}, not the IFN-γ of Th1 cells",
    "A-aula", D_, "IFN-I × IFN-γ", 10, "transcrição lâmina 10; vídeo Shomu's Biology (confunde os dois)", motivacao="m19",
    fontes=F("transcrição, lâmina 10", "O IFN-1 aqui. Não o IFN-γ gama lá do Th1, do granuloma."),
    sem_imagem="contraste da fala, sem figura",
    extra="Type I interferon is made by the infected cell and puts its neighbours in an antiviral state.<br>IFN-γ comes from Th1 and NK cells and activates macrophages, as in granulomas."),
 # ---------- Lâminas 11–12: interferon tipo I (princípio) ----------
 K(1497440851060, "V-prova", E_, "Vírus dispara PRR citosólico → IFN tipo I", 11, "lâmina 11; prova 2018 P3 1.7 (padrões moleculares e IFN alfa/beta)"),
 sh(1793053714022, "verde", E_, "IFN-α/β agem nas células não infectadas", 11, "V-hy: card de imuno (AnKing 1489970693302); a lâmina 11 é este efeito"),
 au("au-ifn-tempo", "During a <b>viral infection</b>, type I interferon makes neighboring cells enter an {{c1::antiviral state}}, reducing viral protein synthesis and spread before T-cell control.",
    "V-pilar", E_, "IFN-I ganha tempo", 11, "transcrição lâmina 11", motivacao="m21",
    fontes=F("transcrição, lâmina 11", "Ele não impede a infecção de outras células, necessariamente, mas ele bloqueia ou dificulta a replicação viral. Na medida em que ele faz isso, ele ganha tempo"),
    sem_imagem="a figura da lâmina 11 é um esquema sem o alvo",
    extra="The infected cell releases IFN-α/β; neighboring cells induce antiviral proteins. This slows production of new virions and buys time for the adaptive response, but does not guarantee that neighboring cells avoid infection."),
 K(1520301328706, "R-detalhe", E_, "IFN-I reduz síntese proteica (estado antiviral)", 12, "lâmina 12 (estado de resistência antiviral: inibição da síntese proteica)"),
 sh(1793053714276, "verde", E_, "IFN-I aumenta MHC I", 12, "V-hy: card de imuno (AnKing 1520301453074); lâmina 12"),
 sh(1793053714397, "verde", E_, "IFN-α/β ativam NK", 12, "V-hy: card de imuno (AnKing 1487117310594); lâmina 12"),
 # ---------- Lâmina 13: NK (princípio) ----------
 K(1487117314403, "V-pilar", E_, "NK mata célula sem MHC I", 13, "lâmina 13"),
 sh(1793053714521, "azul", E_, "NK: perforina e granzima", 13, "A-aula: card de imuno (AnKing 1487117308213); lâmina 13"),
 sh(1792242117388, "azul", E_, "NK destrói tumor sem MHC I", 13, "A-aula: card de imuno; a lâmina 13 cita a vigilância antitumoral"),
 K(1503876156644, "R-detalhe", E_, "CMV bloqueia MHC I e escapa do CTL", 13, "transcrição lâmina 12 (vírus que bloqueiam MHC); apostila p. 44", sem_imagem="mecanismo molecular, sem figura útil"),
 au("au-nk-cd8", "A virus that hides <b>MHC I</b> from cytotoxic T cells loses the inhibitory signal and becomes a target of {{c1::NK cells}}",
    "A-aula", E_, "CD8 × NK quando o vírus esconde MHC I", 13, "transcrição lâminas 12–13; apostila guia p. 44", motivacao="m24",
    fontes=F("apostila guia p. 44", "Alguns vírus tentam inibir o sistema imune ao impedir a apresentação do MHC-I para CTLs. No entanto, as células NK destroem quaisquer células que não apresentem MHC-I."),
    sem_imagem="a figura da lâmina 13 está no card de AnKing da NK",
    extra="With MHC I the infected cell is visible to CD8 T cells; without it, to NK cells.<br>Interferon raises MHC I and also arms NK cells with more granzyme, so the two balance out."),
 # ---------- Exemplo (lâminas 14–29): só pelo princípio que ilustra ----------
 au("au-aguda-matriz", "An <b>acute viral infection</b> that kills cells but spares the {{c1::reticulin}} framework lets the tissue regenerate fully",
    "A-aula", X1, "Matriz poupada → regeneração (hepatite A)", 14, "lâmina 14; transcrição", motivacao="m25",
    fontes=F("transcrição, lâmina 14", "Eu não destruo mais, por exemplo, arcabouço de reticulina, de matriz extracelular, isso fica relativamente preservado, o que faz com que, depois que eu elimino o vírus, eu consiga repopular esse fígado"),
    sem_imagem="a lâmina 14 é o esquema do HBV, sem o alvo",
    extra="Hepatitis A is the model: heavy hepatocyte loss, then full recovery.<br>Chronic hepatitis B and C differ because a long adaptive response destroys the framework too."),
 K(1715273523479, "A-aula", X2, "Vidro fosco na hepatite B crônica", 16, "lâmina 16 (efeito citopático no hepatócito)"),
 au("au-vidro-fosco", "<b>Ground-glass hepatocytes</b> are a cytopathic effect in which the cytoplasm is packed with accumulated viral {{c1::surface protein}}",
    "A-aula", X2, "Proteína viral acumulada = efeito citopático", 16, "lâminas 16–17; transcrição", motivacao="m26",
    fontes=F("transcrição, lâmina 17", "Que proteína é essa? Normalmente, é proteína de superfície"),
    extra="It is the same rule as the inclusion: a viral part made in excess piles up where it is made.<br>The protein in hepatitis B is HBsAg, and it steals machinery the hepatocyte needs for albumin and clotting factors.<br>" + IMG("vidro-fosco")),
 au("au-ihq", "On <b>immunohistochemistry</b>, hepatitis B surface antigen stays in the cytoplasm, whereas core antigen appears in the {{c1::nucleus}}",
    "A-aula", X2, "Antígeno viral no compartimento de origem", 18, "lâminas 17–18", motivacao="m27",
    fontes=F("lâminas 17–18", "Imunohistoquímica - HBsAg … Imunohistoquímica - HBcAg"),
    extra="Surface protein (HBsAg) is made on the endoplasmic reticulum and stays in the cytoplasm.<br>Core protein (HBcAg) assembles with the genome near the nucleus.<br>" + IMG("ihq-hbsag", 220) + IMG("ihq-hbcag", 220)),
 au("au-anti-hbc", "Because the <b>hepatitis B vaccine</b> contains only surface antigen, an antibody against the viral {{c1::core}} protein, a structural part absent from the vaccine, shows natural infection",
    "A-aula", X2, "Anticorpo contra proteína ausente da vacina prova infecção", 18, "transcrição lâmina 18", motivacao="m28",
    fontes=F("transcrição, lâmina 18", "E se ele tem anti-HBC positivo (anticorpo contra a proteína do core)? Faz sentido ter uma vacina que usa a proteína do core? Não. Então esse paciente teve contato."),
    sem_imagem="raciocínio sorológico, sem figura",
    extra="Anti-HBs alone can come from vaccine or infection.<br>HBeAg, used during replication, marks a virus that is actively replicating.<br>Serology is read from the virus's structure."),
 K(1486776378880, "A-aula", X3, "Zona I (periportal) primeiro na hepatite viral", 20, "lâmina 20; transcrição"),
 au("au-periportal", "In <b>viral hepatitis</b>, inflammation concentrates around the {{c1::portal tracts}}, where both the virus and the inflammatory cells arrive",
    "A-aula", X3, "A lesão segue a via de chegada", 20, "lâminas 19–20; transcrição", motivacao="m29",
    fontes=F("transcrição, lâmina 20", "Como eu tenho mais células infectadas aqui, e aqui também é a via principal por onde chegam as células inflamatórias, é normal que eu tenha mais inflamação perto dos espaços porta."),
    extra="The virus arrives with the blood and infects the first cells it meets.<br>Metabolic injuries instead hit zone 3, the least oxygenated.<br>" + IMG("infiltrado")),
 sh(1792753612016, "verde", X4, "Lesão do HBV vem dos CTL", 21, "V-pilar: card da 59; Robbins: o dano é sobretudo pela resposta"),
 sh(1792117361820, "azul", X4, "Hepatite viral: necrose e apoptose com infiltrado mononuclear", 21, "A-aula: card da 09; lâminas 21–24"),
 au("au-apoptose-necrose", "When infected cells die by {{c1::necrosis}} rather than <b>apoptosis</b>, the targeted lymphocyte attack turns into collateral tissue damage",
    "V-pilar", X4, "Apoptose dirigida × necrose", 22, "lâminas 21–24; transcrição lâmina 22", motivacao="m30",
    fontes=F("transcrição, lâmina 22", "a hora que eu gero necrose celular, quando eu não consigo induzir apoptose em todo mundo, eu uso granzima, perforina e isso libera muito material intracelular"),
    extra="Apoptosis keeps contents inside membrane-bound fragments, so it causes little inflammation.<br>Lymphocytes also cause necrosis when apoptosis is not achieved in every infected cell.<br>" + IMG("apoptose", 220) + IMG("necrose", 220)),
 au("au-necrose-matriz", "<b>Necrosis</b> of infected cells recruits {{c1::neutrophils}}, whose proteases destroy the matrix framework the regenerating cells need",
    "V-pilar", X4, "Necrose → neutrófilo → matriz destruída", 22, "transcrição lâmina 22", motivacao="m31",
    fontes=F("transcrição, lâmina 22", "ativa… neutrófilo, que tem protease, tem elastase, tem colagenase. Que vão começar a destruir... tudo. Tudo, inclusive o arcabouço de matriz extracelular."),
    sem_imagem="a necrose está em au-apoptose-necrose",
    extra="Elastase and collagenase digest the reticulin scaffold.<br>Cells can still divide, but without the scaffold they cannot rebuild the original architecture."),
 au("au-interface", "In <b>chronic viral hepatitis</b>, inflammation breaking through the {{c1::limiting plate}} shows ongoing cell destruction, a sign of active disease",
    "A-aula", X5, "Destruição em curso = atividade", 25, "lâmina 25; transcrição", motivacao="m32",
    fontes=F("transcrição, lâmina 25", "Eu tenho a agressão daquilo que a gente chama de placa limitante. … Porque isso é critério de atividade."),
    extra="This is interface hepatitis, or piecemeal necrosis.<br>It is a biopsy criterion to start treatment.<br>" + IMG("interface")),
 au("au-cd8-b", "In <b>chronic viral hepatitis</b>, immunohistochemistry for CD20 in the portal infiltrate marks abundant {{c1::B lymphocytes}}",
    "A-aula", X5, "CD8 e B no infiltrado", 26, "lâminas 26–27; transcrição", motivacao="m33",
    fontes=F("transcrição, lâmina 26", "Se eu estou destruindo um monte de hepatócito infectada, quando esses vírus saem, eu não quero que eles vão para o hepatócito vizinho. Então eu tenho que produzir um montão de anticorpo aqui."),
    extra="CD8 T cells kill infected hepatocytes, and B-cell antibodies keep the released virus from infecting neighbours.<br>Both arms of adaptive immunity act together in the tissue.<br>" + IMG("linf-b")),
 au("au-colageno", "When cell loss outpaces regeneration, the collapsed <b>reticulin</b> is replaced by thick {{c1::collagen}} that forms septa",
    "V-pilar", X6, "Reticulina → colágeno → septos", 28, "lâmina 28; transcrição", motivacao="m34",
    fontes=F("transcrição, lâmina 28", "a trama de reticulina meio que desabou, como eu tenho o DAMP, eu ativo o neutrófilo, começo a quebrar essa reticulina, que é um colágeno muito fininho, começo a fazer um colágeno mais grosso."),
    extra="Reticulin is thin type III collagen.<br>Septa join and isolate regenerative nodules, which is cirrhosis.<br>" + IMG("septos")),
 sh(1791022172624, "verde", X6, "Cirrose: fibrose e nódulos regenerativos", 29, "V-hy: card da correlação pato-radio 2; lâmina 29"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1516474665512": "The inclusion is where rabies virus is made: eosinophilic, in the neuron cytoplasm.",
 "ak1502152021975": "So DNA-virus inclusions are usually nuclear; poxvirus, which replicates in the cytoplasm, is the exception.",
 "ak1516475827100": "Herpesviruses replicate in the nucleus, so the inclusion is nuclear.",
 "ak1503861947945": "A large nuclear inclusion with a clear halo, in an enlarged cell.",
 "ak1502570605009": "A DNA virus with its own polymerase replicates in the cytoplasm, so its inclusion is cytoplasmic.",
 "ak1506298786823": "Fusion proteins on the infected cell membrane join it to its neighbours.",
 "ak1506457588894": "Hence the name respiratory syncytial virus: fused pneumocytes and macrophages.",
 "ak1506298973285": "Giant cells formed by fusion, seen in measles pneumonia and lymphoid tissue.",
 "ak1405375421095": "Koilocytes plus dysplasia point to an oncogenic type: transformation leads to neoplasia.",
 "ak1487117300306": "This is the main way infected cells are destroyed in viral infections.",
 "ak1497440851060": "Interferon is the first link between recognizing a virus and protecting nearby cells.",
 "ak1520301328706": "Together with mRNA degradation this is the antiviral state of neighbouring cells.",
 "ak1487117314403": "MHC I gives an inhibitory signal; without it the NK cell degranulates.",
 "ak1503876156644": "Hiding MHC I escapes CD8 T cells but removes the brake on NK cells.",
 "ak1715273523479": "The cytoplasm looks homogeneous because it is full of accumulated surface protein.",
 "ak1486776378880": "The virus and the inflammatory cells arrive by portal blood.",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "au-vidro-fosco": "ganho: o AnKing nomeia o vidro fosco; aqui o princípio (proteína viral acumulada é efeito citopático, como a inclusão) e a perda de função",
 "au-periportal": "ganho: o AnKing dá a zona I; aqui o princípio geral (a lesão segue a via de chegada do vírus e das células)",
 "au-raiva-sarampo": "ganho: o AnKing dá o Negri; aqui o contraste das lâminas 5 e 6, que mostra que o compartimento decide a inclusão",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "pt61-raiva.png": "lâmina 5: neurônio com inclusão citoplasmática eosinofílica (raiva), seta",
 "pt61-sarampo.png": "lâmina 6: neurônio com inclusão nuclear (sarampo)",
 "pt61-sincicio.png": "lâmina 7: pulmão com sincícios do vírus sincicial respiratório nos septos",
 "pt61-coilocito.png": "lâmina 8: Papanicolau com coilócitos (halo claro perinuclear)",
 "pt61-curva2.png": "lâmina 10 recortada só no gráfico: curva de vírus, IFN-I, NK, linfócitos T e anticorpos por dia",
 "pt61-vidro-fosco.png": "lâmina 16: hepatócitos em vidro fosco (seta)",
 "pt61-ihq-hbsag.png": "lâmina 17: imuno-histoquímica de HBsAg no citoplasma",
 "pt61-ihq-hbcag.png": "lâmina 18: imuno-histoquímica de HBcAg nos núcleos",
 "pt61-infiltrado.png": "lâmina 19: espaço porta expandido por infiltrado linfocitário",
 "pt61-necrose.png": "lâmina 22: necrose de hepatócitos com infiltrado",
 "pt61-apoptose.png": "lâmina 24: hepatócito apoptótico eosinofílico",
 "pt61-interface.png": "lâmina 25: inflamação portal invadindo o lóbulo (interface)",
 "pt61-linf-b.png": "lâmina 26: imuno-histoquímica de linfócitos B no infiltrado portal",
 "pt61-septos.png": "lâmina 28: reticulina com septos isolando nódulos",
}
REVISAO = {}
ESCOPO = {"objetivo": "Entender como qualquer infecção viral aparece no tecido: o efeito direto do vírus (lise, transformação e o efeito citopático que se reconhece) e o efeito da resposta (inata no agudo, adaptativa no crônico), com a hepatite como exemplo dos mesmos princípios.",
          "centrais": [
           ["dois efeitos", "sh-1792753616942"],
           ["efeitos diretos e efeito citopático", "au-efeitos", "au-inclusao", "au-sincicio-granuloma"],
           ["agudo inata × crônico adaptativa; vírus intracelular", "au-quadros", "au-intracelular", "au-curva"],
           ["CD8 e apoptose", "sh-1791625430882", "sh-1791625429957"],
           ["IFN-I", "au-ifn-tempo"],
           ["NK e MHC I", "sh-1793054287147"],
           ["dano pela resposta e destino do tecido", "sh-1792753612016", "au-apoptose-necrose", "au-necrose-matriz", "au-colageno"],
           ["cirrose", "sh-1791022172624"]],
          "exemplos": ["au-aguda-matriz", "au-vidro-fosco", "au-ihq", "au-anti-hbc", "au-periportal", "au-interface", "au-cd8-b"],
          "outras_aulas": ["58 Multiplicação viral", "59 Patogênese da infecção viral", "60 Prática de virologia", "47 Inflamação granulomatosa", "09 Lesão celular", "62 Inflamação crônica", "63 Resposta imune aos vírus", "65 Reparo tecidual"]}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
