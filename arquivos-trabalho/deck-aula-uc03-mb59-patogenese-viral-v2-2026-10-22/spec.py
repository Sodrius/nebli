# Especificação curada — 59 Patogênese da infecção viral (UC03 P3, Microbiologia; Prof. Enrique Boccardo; 178 lâminas = versão I (1–61,
# Zanotto), versão II (62–119) e versão III (120–178, "Infecção do hospedeiro suscetível", a da fala)). Pipeline v7 (refação de 23/10): o deck
# nasce de compreensao-aula.json (aprender por bloco) e segue a versão III; as versões I e II são repetição; vírus entram pelo mecanismo.
# História: o vírus só vive em células, então a doença é uma questão de quais tecidos ele alcança → entra por uma porta (respiratória é a
# maior; receptores são moléculas de adesão; o intestino exige resistência a ácido e bile) → espalha-se (sítio primário, linfa, viremia,
# órgão-alvo) → depois do primeiro pico segue um padrão (aguda; latente, persistente, progressiva) que depende do vírus, da via e da resposta
# → a doença depende de suscetibilidade, permissividade, acesso e resposta, e da virulência (rotavírus, influenza, HPV) e do tropismo
# (rinovírus × poliovírus) → para ficar, o vírus precisa de evasão ativa ou passiva.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 7
# v7 (F-20261023-CLAUDE-02): as seções de rinovírus e rotavírus deixaram de ser "da aula"; elas puxavam a ficha técnica inteira
SECOES_MOTIVO = ("Aula de princípio geral (patogênese viral): nenhuma seção de recurso do AnKing é do seu assunto; as de rinovírus, rotavírus, "
                 "influenza, HPV e herpes são de vírus que a aula usa como exemplo, e delas entra só o card que responde a um item aprender")
SECOES_DA_AULA = []
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb59-20261023a"
SHORT = "mb59"
LESSON = "2026-uc03-microbiologia-59-patogenese-viral"
DECK = "NEBLI::UC03::P3::Microbiologia::Patogênese da infecção viral"
CRITERIOS = "MEMORY.md + pipeline v7 (EXECUCAO-DECK-AULA) + FEEDBACKS até F-20261023-CLAUDE-03 + GUIA_CARDS.md de 23/10"
_IMGS = ("disseminacao", "padroes", "padroes-comp", "hsv-latencia", "ebv-latencia", "hbv-aguda", "hbv-cronica", "hiv-setpoint",
         "rota-nsp4", "polio-trajeto", "hiv-inoculo", "hpv-tropismo", "resp-sitios")
MEDIA = {f"mb59-{n}.png": f"img/mb59-{n}.png" for n in _IMGS}
IMG = lambda n, w=460: f'<img src="mb59-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (23/10): seções de recurso do AnKing (rinovírus, rotavírus, poliovírus, influenza, herpes, HBV, HPV, mecanismos de "
         "infectividade; busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em AnKing, nos 9 acervos "
         "externos e no NEBLI vivo, uma consulta por conceito do mapa (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


_EPI = "epidemiologia ou clínica do rotavírus (estação, creche, faixa etária, complicação), fora do mecanismo que a aula ensina"
_VAC = "vacina do rotavírus (esquema, contraindicação, efeito adverso): aula de vacinas"
EXCLUIDOS = [
 (1473536754044, "quadro clínico do resfriado: clínica, fora do recorte"),
 (1537564104535, "conduta num caso de resfriado: clínica"),
 (1502063631440, "todo vírus nu é icosaédrico: card da 57 Princípios gerais dos vírus"),
 (1506609599866, "poliproteína dos picornavírus: ciclo, card da 58"),
 (1506627151740, "protease dos picornavírus: ciclo, card da 58"),
 (1516665187703, "reovírus de dupla fita: repete 1516321085226, que entra"),
 (1516665846802, _EPI), (1516666059911, _EPI), (1516666107599, _EPI), (1516666216326, _EPI), (1516666378248, _EPI),
 (1525354034637, _EPI), (1581619827487, _EPI), (1482289615950, _EPI),
 (1516666476206, "coltivírus: outro vírus da família, fora da aula"), (1516666961676, "coltivírus: fora da aula"),
 (1516667142242, "tratamento do rotavírus (reidratação): clínica"),
 (1516666695540, _VAC), (1516666766803, _VAC), (1516666812794, _VAC), (1516667209562, _VAC), (1517013683033, _VAC), (1517598229958, _VAC),
]
FORA_DO_RECORTE = [
 "Oncogênese viral (E6 ⊣ p53, E7 ⊣ pRb, latências do EBV e linfomas, HBV e carcinoma hepatocelular): Agentes carcinogênicos biológicos (P4); E6/E7 aqui só como evasão ativa e o HPV pelo risco de cada tipo.",
 "Patogênese do HIV em detalhe (CD4, correceptores, fases clínicas): aula específica de HIV; aqui só o padrão progressivo, o set point e a latência clínica.",
 "Resposta imune antiviral (IFN, NK, CTL, anticorpos): 63 Organização da resposta imune aos vírus; aqui só como determinante do padrão e da doença.",
 "Efeito citopático e inclusões: 60 Virologia prática e 61 Patologia da infecção viral.",
 "Sorologia completa das hepatites e manifestações extra-hepáticas: clínica; entram só o HBsAg > 6 meses (crônica) e o anti-HBs (recuperação), que as curvas das lâminas 139–140 mostram.",
 "Vacinas (Salk × Sabin em detalhe, esquemas, rotavírus): aula de vacinas; entra só a vacina oral da pólio como exemplo de atenuação que muda o tropismo (lâmina 167).",
 "Versões I (1–61) e II (62–119) repetem a versão III; os cards apontam para a III.",
]
A_, B_, C_, D_, E_, F_, G_, H_, I_ = ("A-infeccao", "B-entrada", "C-disseminacao", "D-padroes", "E-determinantes", "F-virulencia",
                                       "G-tropismo", "H-evasao", "I-balanco")

CARDS = [
 # ---------- O vírus como parasita de tecidos; infecção ≠ doença (lâminas 120–122) ----------
 sh(1792677732277, "verde", A_, "Vírus é parasita intracelular obrigatório", 121, "V-pilar: retoma a 57 (sem ribossomo nem ATP); é a premissa da aula"),
 au("au-tecidos", "Because viruses are obligate <b>intracellular</b> parasites, inside an organism they are obligate parasites of {{c1::tissues}}",
    "A-aula", A_, "Parasita de tecidos e órgãos", 121, "lâmina 121; transcrição (parasitas de tecidos e órgãos)",
    extra="So viral disease depends on which tissues the virus reaches and can use.<br>Entry, spread and tropism decide those tissues."),
 sh(1792695018040, "verde", A_, "Infecção produtiva × abortiva", 122, "V-pilar: card da 58; a lâmina 122 retoma a definição"),
 sh(1791746116702, "azul", A_, "Infecção ≠ doença (iceberg)", 122, "A-aula: card da 35, geral; a lâmina 122 fixa infecção ≠ doença"),
 # ---------- Portas de entrada (lâminas 123–128) ----------
 sh(1791780622904, "azul", B_, "Portas de entrada", 124, "A-aula: card da 39 (pele, mucosas, vias aéreas, fecal-oral); lâmina 124"),
 au("au-resp-comum", "The <b>respiratory tract</b> is the main viral portal of entry, despite mucus and IgA, because of its huge {{c1::surface area}}",
    "V-pilar", B_, "Via respiratória é a mais comum: superfície enorme", 125, "lâminas 124–125; transcrição (140 m², 14 × 10 m); Trabulsi cap. 77",
    extra="About <b>140 m²</b>, and we breathe all day.<br>Mucociliary clearance and secretory IgA defend it, yet many viruses still enter there."),
 K(1473289461901, "A-aula", B_, "Defesa respiratória: escada mucociliar", 125, "lâmina 125 (epitélio mucociliar como defesa)",
   extra_add="- <b>Secretory IgA</b> is the other barrier a respiratory virus must overcome"),
 K(1516325251980, "A-aula", B_, "Influenza: transmissão por gotículas/aerossol", 125, "lâmina 125 (aerossóis: influenza)"),
 K(1516222208131, "A-aula", B_, "Rinovírus: gotículas e fômites", 125, "lâmina 125 (contato direto: rinovírus)"),
 au("au-local-sist", "<b>Rhinovirus</b> stays at the portal of entry, a {{c1::localized::localized/systemic}} infection, whereas <b>measles</b> spreads {{c1::systemically::localized/systemic}}",
    "A-aula", B_, "Infecção localizada × sistêmica", 125, "lâmina 125; transcrição (sarampo: entra pela via aérea, rash na periferia); Jawetz quadro 30.1",
    extra="Local infections need no viremia and have short incubation.<br>Systemic ones reach distant organs, like the measles rash in the skin."),
 au("au-regiao", "In the <b>respiratory tract</b>, the {{c1::site of replication}} decides whether a virus causes rhinitis, laryngitis or pneumonia",
    "R-detalhe", B_, "Região do trato define o quadro", 126, "lâmina 126; transcrição (rinite, faringite, laringite → bronquiolite, broncopneumonia)",
    extra="The deeper the virus replicates, the more severe the disease.<br>" + IMG("resp-sitios")),
 au("au-adesao", "Many viral <b>receptors</b> are cell {{c1::adhesion}} molecules, such as ICAM-1 and the CAR tight-junction protein",
    "A-aula", B_, "Receptores virais são moléculas de adesão", 127, "lâmina 127; apostila guia de Micro; UC3.pdf",
    extra="Binding them can loosen the epithelium and impair its function."),
 K(1516222322469, "A-aula", B_, "Rinovírus usa ICAM-1", 127, "lâmina 127 (ICAM-1 para rinovírus)"),
 sh(1792677742326, "azul", B_, "Entrada pelo trato alimentar: resistir a ácido e bile", 128, "A-aula: card da 57 (vírus nu resiste a ácido, bile e dessecação); lâmina 128"),
 au("au-entericos", ORG("<b>Enteric viruses</b>:<br>- localized, causing diarrhea: {{c1::rotavirus}}, norovirus<br>- systemic, reaching far organs: {{c2::poliovirus}} (CNS), hepatitis A (liver)"),
    "A-aula", B_, "Entéricos localizados × sistêmicos", 128, "lâmina 128; transcrição (pólio → SNC, hepatite A → fígado)",
    extra="Both start in the intestinal epithelium, but only systemic ones go on to viremia."),
 # ---------- Disseminação (lâminas 129–130) ----------
 au("au-dissemina", ORG("<b>Systemic viral spread</b>:<br>- replication at {{c1::portal of entry}}<br>- lymph nodes<br>- {{c1::primary viremia}}<br>- liver, spleen<br>- secondary viremia to {{c1::target organ}}"),
    "V-pilar", C_, "Sítio primário → linfa → viremia → órgão-alvo", 129, "lâmina 129; transcrição; Jawetz fig. 30.2",
    extra="From the target organ the virus is shed (skin, urine, feces) or causes the disease.<br>" + IMG("disseminacao")),
 au("au-viremia", "Viruses reach the blood from the epithelium through the {{c1::lymphatics}}, then circulate free in plasma or inside <b>leukocytes</b>",
    "A-aula", C_, "Viremia: livre ou em leucócitos", 130, "lâmina 130; Jawetz quadro 30.3",
    extra="Virus in the blood is viremia; it carries the virus to distant target organs, the secondary site of replication."),
 au("au-viremia-passiva", "Viremia from viral <b>replication</b> is {{c1::active::active/passive}}, while virus injected by needle or mosquito causes {{c1::passive::active/passive}} viremia",
    "A-aula", C_, "Viremia ativa × passiva", 130, "lâmina 130; transcrição (transfusão, droga injetável, mosquito, mordida)",
    extra="Passive viremia skips the epithelial barriers altogether."),
 au("au-incubacao", "<b>Localized</b> viral infections have a {{c1::short::short/long}} incubation, whereas <b>systemic</b> ones, which must spread first, have a {{c1::long::short/long}} one",
    "A-aula", C_, "Incubação curta (local) × longa (sistêmica)", 129, "Jawetz quadro 30.1; prova 2025 P3 3.6 (sarampo 14 dias × influenza 3 dias)",
    extra="A long incubation lets <b>measles</b> spread to others before symptoms appear."),
 # ---------- Padrões de infecção (lâminas 131–145) ----------
 au("au-padroes", ORG("<b>Viral infection patterns</b>:<br>- {{c1::acute}}: virus cleared<br>- {{c1::latent}}: silent, reactivates<br>- {{c1::persistent}}: steady replication<br>- {{c1::progressive}}: rising until death"),
    "V-pilar", D_, "Padrões: aguda, latente, persistente, progressiva", 133, "lâminas 132–133 e 145; transcrição; prova 2015 P2sub 2.5",
    extra="Every infection starts with the same peak; what follows defines the pattern.<br>Pattern is typical of each virus: all herpesviruses become latent, influenza never chronic.<br>" + IMG("padroes")),
 au("au-falha", "An <b>HPV</b> genome that stays in cells without replicating or being cleared is {{c1::failure to clear}}, not latency",
    "A-aula", D_, "Falha em eliminar ≠ latência", 133, "lâmina 133 (quinta curva); transcrição ('não gosto de falar latente, porque latência é uma característica dos herpesvírus')",
    extra="The immune response stopped replication but could not remove the genome.<br>True latency, a switchable viral program, belongs to the <b>herpesviruses</b>"),
 au("au-aguda", "An <b>acute</b> viral infection is limited in time and ends with {{c1::clearance}} of the virus or death of the host",
    "A-aula", D_, "Infecção aguda: começo, meio e fim", 134, "lâminas 132 e 134; transcrição; apostila guia (aguda ≠ rápida)",
    extra="Acute is not fast: a cold lasts days, acute hepatitis B about 6 months."),
 au("au-latencia", "In viral <b>latency</b> the genome stays in the cell without making virions, but the cycle can be {{c1::reactivated}}",
    "V-pilar", D_, "Latência viral: ciclo desligado e reativável", 135, "lâmina 135 (estado transcricional e traducional único)",
    extra="Between reactivations viral replication is zero.<br>True viral latency belongs to the <b>herpesviruses</b>"),
 au("au-hsv-axonio", "<b>HSV</b> replicates lytically in mucosal epithelium, then travels up {{c1::sensory axons}} to lie latent in the ganglion",
    "A-aula", D_, "HSV: lítico no epitélio, latente no neurônio", 136, "lâmina 136; transcrição; Jawetz fig. 30.4",
    extra="On reactivation it travels back down the axon to the epithelium.<br>" + IMG("hsv-latencia")),
 K(1502153397982, "A-aula", D_, "HSV-1 latente no gânglio trigeminal", 136, "lâmina 136; Jawetz (gânglios sensitivos)"),
 K(1502152875721, "A-aula", D_, "Estresse reativa o HSV-1", 136, "transcrição (reativação por estresse do hospedeiro)"),
 au("au-reativ", "Herpes <b>reactivations</b> reach lower viral loads than the primary infection because {{c1::immune memory}} already exists",
    "A-aula", D_, "Reativação com pico menor", 136, "transcrição (padrão latente); UC3.pdf (segunda resposta mais branda)",
    extra="On a graph, each peak returns to zero: draw it this way."),
 au("au-celula-longa", "<b>Herpesviruses</b> replicate lytically in one cell type and stay latent in a long-lived one, like {{c1::memory B cells}} for EBV",
    "A-aula", D_, "Latência em célula de vida longa", 137, "lâmina 137; apostila guia e UC3.pdf; transcrição (lâmina 146)",
    extra="HSV: lytic in mucosal epithelium, latent in sensory neurons.<br>A virus in constantly shed intestinal epithelium is lost with the cells."),
 K(1503853508872, "A-aula", D_, "EBV transmitido pela saliva", 137, "lâmina 137; transcrição"),
 K(1503854280231, "R-detalhe", D_, "EBV infecta primeiro o epitélio da orofaringe", 137, "lâmina 137 (mucosa orofaríngea)"),
 K(1503854748516, "A-aula", D_, "EBV latente na célula B", 137, "lâmina 137"),
 au("au-ebv-0", "In memory B cells <b>EBV</b> expresses no viral protein, latency type {{c1::0}}, so it is invisible to T cells",
    "A-aula", D_, "EBV: latência 0 invisível", 137, "lâmina 137; transcrição (quatro tipos de latência; latência 0 sem proteína)",
    extra="Proliferating B cells: latency III, many proteins, killed by T cells.<br>EBV fits its genes to the B-cell state.<br>" + IMG("ebv-latencia")),
 au("au-persistente", "A {{c1::persistent}} infection, unlike a <b>latent</b> one, keeps producing virions at a steady level for years",
    "A-aula", D_, "Persistente: replicação contínua", 132, "lâmina 132 (crônica: replicação contínua × latência); lâminas 138–142; transcrição",
    extra="Virus and host coexist in a balance, as in chronic hepatitis B and C."),
 au("au-hbv-adulto", "About {{c1::90}}% of adults infected with <b>HBV</b> clear it in an acute infection lasting about 6 months",
    "A-aula", D_, "HBV no adulto: 90% agudo", 139, "lâmina 139; transcrição; prova 2015 P2 2.4",
    extra="The other 10% become chronic carriers.<br>Clearing HBV takes a vigorous immune response, which also injures the liver.<br>" + IMG("hbv-aguda")),
 au("au-hbv-imune", "In acute <b>HBV</b> infection, liver injury comes mainly from {{c1::cytotoxic T cells}} killing infected hepatocytes",
    "A-aula", D_, "HBV: lesão pela resposta imune", 139, "transcrição (o sistema imune causa o dano hepático tentando eliminar o vírus); Ninja Nerd",
    extra="Transaminases rise when the immune response begins, after the peak of viral DNA."),
 K(1506552371527, "V-prova", D_, "HBV vertical: 90% crônico", 140, "lâmina 140; transcrição (90% das crianças de mães infectadas)",
   extra_add=IMG("hbv-cronica")),
 K(1521044243769, "V-prova", D_, "HBsAg > 6 meses = crônico", 140, "lâminas 139–140 (curvas de HBsAg); prova 2015 P2 2.4 (o que as curvas mostram)"),
 K(1552683158377, "A-aula", D_, "Anti-HBs = recuperação", 139, "lâmina 139 (anticorpos anti-HBs na recuperação); prova 2015 P2 2.4"),
 K(1506630060423, "A-aula", D_, "HCV cronifica na maioria", 142, "lâminas 141–142; transcrição; UC3.pdf"),
 au("au-progressiva", "In a {{c1::progressive}} infection such as <b>HIV</b>, replication never stops and finally overcomes the immune response",
    "A-aula", D_, "Progressiva: o vírus vence aos poucos", 143, "lâminas 143–144; transcrição",
    extra="Viral load rises as CD4 T cells fall below a threshold, giving AIDS."),
 au("au-setpoint", "After acute <b>HIV</b> infection, viral load settles at a {{c1::set point}} that predicts how fast AIDS develops",
    "A-aula", D_, "Set point do HIV", 144, "lâmina 144; transcrição; UC3.pdf",
    extra="Lower set point, slower progression.<br>It reflects how well the immune response controls the virus.<br>" + IMG("hiv-setpoint")),
 au("au-lat-clin", "HIV <b>clinical latency</b> has no symptoms but continuous viral {{c1::replication}}, unlike herpesvirus latency",
    "V-prova", D_, "Latência clínica × latência viral", 144, "lâmina 144; transcrição ('latência clínica está aqui para complicar a vida'); apostila e UC3.pdf",
    extra="Herpes latency: replication switched off.<br>HIV clinical latency: replication on, symptoms off."),
 # ---------- Determinantes do padrão (lâminas 146–147) ----------
 au("au-dep-padrao", ORG("<b>The pattern of a viral infection</b> depends on:<br>- the virus, its virulence and {{c1::tropism}}<br>- the {{c1::route}} of transmission<br>- the host {{c1::immune response}}"),
    "V-pilar", E_, "Do que dependem os padrões", 146, "lâmina 146; transcrição; monitoria",
    extra="HBV by needle in adults: mostly acute.<br>HBV from mother to child: mostly chronic."),
 au("au-inata-adapt", "<b>Acute</b> viral infections are mainly controlled by {{c1::innate::innate/adaptive}} immunity, and <b>chronic</b> ones by {{c1::adaptive::innate/adaptive}} immunity",
    "A-aula", E_, "Aguda: inata; crônica: adaptativa", 147, "lâmina 147; transcrição; apostila guia",
    extra="When the adaptive response cannot clear the virus, the host learns to live with it."),
 au("au-cronificar", "To establish a <b>chronic</b> infection, a virus needs mechanisms of immune {{c1::evasion}}",
    "A-aula", E_, "Cronificar exige evasão", 147, "lâmina 147; transcrição",
    extra="Evasion can be active, with viral proteins, or passive, by where and how the virus is."),
 # ---------- Infecção × patogênese (lâminas 148–150) ----------
 au("au-doenca-dep", ORG("<b>Whether infection causes disease</b>, and how severe, depends on:<br>- the virus {{c1::type}}<br>- the host {{c1::species}}<br>- the {{c1::individual}}<br>- the route of infection"),
    "A-aula", E_, "Doença depende de vírus, espécie, indivíduo, via", 148, "lâmina 148; transcrição; apostila guia",
    extra="Most SARS-CoV-2 infections are asymptomatic.<br>Bats carry rabies with little disease."),
 au("au-manifest", ORG("<b>Ways a virus causes disease</b>:<br>- tissue {{c1::destruction}}<br>- inflammatory {{c1::cytokines}}<br>- cell dysfunction<br>- {{c1::paracrine}} effect on uninfected cells<br>- tumor induction"),
    "V-pilar", E_, "Manifestações da patogênese viral", 150, "lâmina 150; transcrição; monitoria",
    extra="Paracrine example: rotavirus NSP4 acting on neighboring cells."),
 au("au-imunopatologia", "In severe <b>influenza</b> and COVID-19, much of the tissue damage comes from the host's own {{c1::inflammatory response}}, called immunopathology",
    "A-aula", E_, "Imunopatologia", 150, "transcrição (casos graves de COVID-19 e influenza: a resposta inflamatória é o grande problema)",
    extra="Hepatitis B is another example: T cells, not the virus, injure the liver."),
 au("au-tumores", "Viral infections cause about {{c1::15–20}}% of <b>human cancers</b>",
    "R-detalhe", E_, "Indução de tumores", 150, "UC3.pdf (15 a 20% dos tumores); transcrição (1 em cada 5 ou 6)",
    extra="Main examples: high-risk HPV, HBV, HCV and EBV."),
 # ---------- Suscetibilidade, permissividade, acesso, resposta (lâminas 151–152) ----------
 sh(1792695018289, "azul", E_, "Condições da infecção produtiva", 152, "A-aula: organizador da 58; a lâmina 152 é este quadro"),
 au("au-susc-perm", "A cell with the viral <b>receptor</b> is {{c1::susceptible::susceptible/permissive}}, and one that also lets the virus replicate is {{c1::permissive::susceptible/permissive}}",
    "V-prova", E_, "Suscetível × permissiva", 152, "lâmina 152; transcrição; prova 2019 P3 3.3",
    extra="A susceptible but nonpermissive cell gives an abortive infection."),
 au("au-hemacia", "A <b>red blood cell</b> may bind a virus but is not {{c1::permissive}}, lacking machinery to copy a genome",
    "A-aula", E_, "Hemácia: entra mas não replica", 152, "transcrição (exemplo da hemácia)",
    extra="No nucleus, no ribosomes: only hemoglobin inside."),
 au("au-acess", "<b>Yellow fever</b> virus on intact skin is harmless, but a mosquito bite makes its target cells {{c1::accessible}}",
    "A-aula", E_, "Acessibilidade à célula-alvo", 152, "lâmina 152; transcrição (exemplo da febre amarela)",
    extra="Infection needs receptor, permissive cell and access to it."),
 au("au-sarampo", "<b>Measles</b> is systemic because many tissues, including {{c1::immune cells}}, are susceptible and permissive to it",
    "V-prova", E_, "Sarampo sistêmico: muitas células suscetíveis e permissivas", 152, "prova 2019 P3 3.3 e 2025 P3 3.6; Jawetz quadro 30.3 (sarampo em linfócitos e monócitos)",
    extra="Infecting immune cells also makes measles <b>immunosuppressive</b><br>Influenza, by contrast, stays in the respiratory epithelium."),
 # ---------- Virulência (lâminas 153–155) ----------
 au("au-virulencia", "<b>Virulence</b> is a virus's relative ability to cause disease and usually follows its {{c1::replicative capacity}}",
    "V-pilar", F_, "Virulência", 153, "lâmina 153; apostila guia; monitoria",
    extra="Tropism and the host response also shape it.<br>It shows as rapid death, organ failure or tumors."),
 au("au-atenuada", "<b>Virulent</b> strains like the 1918 influenza cause disease, whereas {{c1::attenuated}} strains infect harmlessly and serve as live vaccines",
    "A-aula", F_, "Estirpe virulenta × atenuada", 154, "lâmina 154; transcrição",
    extra="Same virus, different strain: virulence is relative to the strain, the dose, the route and the host."),
 au("au-vir-dep", ORG("<b>Virulence depends on</b>:<br>- the viral {{c1::variant}}<br>- the {{c1::dose}} received<br>- the {{c1::route}} of inoculation<br>- host susceptibility"),
    "A-aula", F_, "Do que depende a virulência", 154, "lâmina 154; transcrição; apostila guia",
    extra="HBV acquired vertically is more often chronic, so the route matters."),
 au("au-fatores", ORG("<b>Viral virulence factors</b> help a virus:<br>- replicate more<br>- {{c1::colonize}} and spread<br>- {{c1::evade}} immunity<br>- act as a toxin, like {{c1::NSP4}}"),
    "A-aula", F_, "Fatores de virulência", 155, "lâmina 155; monitoria; apostila guia",
    extra="Spread includes adhesion, entry and exit from cells and from the body."),
 # ---------- Rotavírus (lâminas 156–157) ----------
 K(1516666167898, "A-aula", F_, "Rotavírus: principal diarreia grave infantil", 156, "lâmina 156"),
 K(1516666902436, "A-aula", F_, "Deficiência secundária de lactase", 157, "lâmina 157 (lise das células produtoras de lactase); transcrição"),
 au("au-rota-duas", ORG("<b>Rotavirus diarrhea</b> has two mechanisms:<br>- NSP4 raises Ca2+ and Cl− secretion: {{c1::secretory::secretory/osmotic}}<br>- lysed lactase cells leave lactose in the lumen: {{c1::osmotic::secretory/osmotic}}"),
    "V-pilar", F_, "Rotavírus: diarreia secretória e osmótica", 157, "lâminas 156–157; transcrição (segunda etapa: lise das células de lactase; por isso não se dá leite)",
    extra="So children with rotavirus should not drink milk: the lactose pulls even more water."),
 K(1516665751235, "A-aula", F_, "NSP4: enterotoxina do rotavírus", 156, "lâmina 156 (NSP4 semelhante a enterotoxina)"),
 au("au-nsp4-ca", "Rotavirus <b>NSP4</b> releases {{c1::Ca2+}} from the endoplasmic reticulum, which drives chloride secretion, and water follows into the lumen",
    "A-aula", F_, "NSP4 → Ca2+ → Cl− → diarreia", 157, "lâminas 156–157; transcrição",
    extra="That is why NSP4 is called a viral enterotoxin.<br>" + IMG("rota-nsp4")),
 au("au-paracrino", "Released <b>NSP4</b> also acts on {{c1::uninfected}} neighboring enterocytes, a paracrine effect",
    "A-aula", F_, "NSP4: efeito parácrino", 157, "lâmina 157; transcrição; apostila guia",
    extra="So diarrhea is larger than the number of infected cells suggests."),
 # ---------- Influenza (lâminas 158–159) ----------
 K(1516322197499, "A-aula", F_, "Influenza nomeado por HA e NA", 158, "lâmina 158 (HA e NA)"),
 K(1516321589458, "A-aula", F_, "Variação antigênica em HA e NA", 158, "transcrição (varia muito, vacina anual); apostila guia"),
 K(1516322946030, "A-aula", F_, "Drift → vacina anual", 158, "transcrição (vacina nova a cada ano)"),
 sh(1792695053893, "verde", F_, "Rearranjo causa shift", 159, "V-hy: card da 58"),
 K(1516323168130, "A-aula", F_, "Shift → pandemias", 159, "lâmina 159 (pandemias)",
   extra_add="- Pandemic strains are far more virulent: 1918 H1N1 killed tens of millions"),
 # ---------- HPV (lâminas 160–164) ----------
 K(1394240219632, "A-aula", F_, "HPV baixo risco: 6 e 11", 160, "lâmina 160"),
 au("au-papiloma-laringe", "A benign <b>HPV 6/11</b> papilloma becomes dangerous in the {{c1::larynx}}, where it can obstruct the airway",
    "R-detalhe", F_, "Mesma lesão, gravidade conforme o local", 162, "lâmina 162; transcrição (asfixia, cirurgia)",
    extra="Virulence also depends on the anatomical site infected."),
 K(1394239958498, "A-aula", F_, "HPV alto risco: 16 e 18", 160, "lâmina 160"),
 au("au-hpv-70", "Among high-risk types, <b>HPV 16 and 18</b> together cause about {{c1::70}}% of cervical cancers",
    "A-aula", F_, "HPV 16 + 18 ≈ 70%", 164, "lâmina 164; transcrição; apostila guia",
    extra="HPV 16 alone causes more than half.<br>Virulence differs even among high-risk types."),
 # ---------- Tropismo (lâminas 165–167) ----------
 K(1516324044281, "A-aula", G_, "HA define o tropismo do influenza", 165, "transcrição (influenza muda de receptor e de virulência)"),
 au("au-influenza-inferior", "<b>Influenza</b> strains that bind receptors of the {{c1::lower::upper/lower}} airway cause more severe disease",
    "R-detalhe", G_, "Influenza: receptor das vias inferiores", 165, "transcrição (mudar de receptores das vias superiores para as inferiores aumenta a virulência)",
    extra="Same virus, deeper site, worse disease: pneumonia instead of a cold."),
 K(1516222286888, "A-aula", G_, "Rinovírus: principal causa de resfriado", 166, "lâmina 166 (~50% dos resfriados)"),
 K(1516222135232, "A-aula", G_, "Rinovírus é ácido-lábil", 166, "lâmina 166 (inativado por ácido); transcrição (se engolido, é inativado)",
   extra_add="- Swallowed rhinovirus is killed in the stomach, so it replicates only in the airway"),
 K(1516222409950, "A-aula", G_, "Rinovírus cresce melhor a 33 °C", 166, "lâmina 166 (32–33 °C); transcrição (ar mais frio da rinofaringe)",
   extra_add="- Inhaled air cools the nasal mucosa to about 33 °C, which is why the cold stays in the nose"),
 au("au-alcool", "<b>Alcohol gel</b> inactivates enveloped viruses but not naked ones such as {{c1::rhinovirus}}",
    "R-detalhe", G_, "Álcool-gel não inativa rinovírus", 166, "lâmina 166 (resistente a éter e etanol); transcrição",
    extra="Rhinovirus spreads on hands and fomites, so hand washing matters."),
 K(1516218404816, "A-aula", G_, "Poliovírus é ácido-estável", 167, "lâmina 167 (resistentes ao ácido)"),
 au("au-polio-capsid", "<b>Poliovirus</b> and <b>rhinovirus</b> are close relatives whose different tropism comes from small changes in their {{c1::capsid}}",
    "A-aula", G_, "Rinovírus × poliovírus: o capsídeo decide", 167, "transcrição (pequenas substituições de aminoácidos do capsídeo)",
    extra="Rhinovirus: acid-labile, nose.<br>Poliovirus: acid-stable, gut, then CNS."),
 au("au-polio-trajeto", "After replicating in the gut and its lymph nodes, poliovirus reaches the <b>CNS</b> through {{c1::viremia}}",
    "A-aula", G_, "Trajeto do poliovírus", 167, "lâmina 167; transcrição; Jawetz fig. 30.3",
    extra="Only a minority of infections reach the CNS.<br>" + IMG("polio-trajeto")),
 K(1516219553378, "A-aula", G_, "Sabin: vírus vivo atenuado", 167, "transcrição (vacina da gotinha)"),
 au("au-sabin", "The oral <b>Sabin</b> vaccine replicates in the gut but cannot reach the {{c1::CNS}}, so it causes no paralysis",
    "A-aula", G_, "Atenuação restringe o tropismo", 167, "transcrição (versão atenuada não passa ao sangue e ao SNC)",
    extra="A few mutations changed where it can go, and thus its virulence."),
 # ---------- Evasão (lâminas 168–175) ----------
 au("au-evasao", ORG("<b>Viral immune evasion</b>:<br>- {{c1::active::active/passive}}: needs viral proteins (anti-apoptosis, immune modulation, latency)<br>- {{c1::passive::active/passive}}: no viral proteins (inoculum, tropism, route, variability)"),
    "V-pilar", H_, "Evasão ativa × passiva", 168, "lâminas 168 e 171; transcrição; apostila guia; monitoria",
    extra="Viruses combine both to establish infection."),
 au("au-e6e7", "HPV <b>E6 and E7</b> blunt the cell's interferon response, an example of {{c1::active::active/passive}} evasion",
    "A-aula", H_, "E6/E7: evasão ativa", 169, "lâmina 169; transcrição (alteram a resposta ao interferon)",
    extra="Their effect on p53 and Rb belongs to viral oncogenesis."),
 au("au-latencia-evasao", "Shutting down its own genes in <b>latency</b> is a form of {{c1::active::active/passive}} immune evasion",
    "A-aula", H_, "Latência como evasão ativa", 170, "lâmina 170; transcrição (EBV inibe os próprios genes para não ser visto)",
    extra="EBV latency 0 in memory B cells is the extreme case."),
 au("au-inoculo", "A large viral {{c1::inoculum}}, like a <b>transfusion</b> of HBV-infected blood, overwhelms defenses as passive evasion",
    "A-aula", H_, "Tamanho do inóculo", 171, "lâminas 171–172; transcrição (espirro a 5 m × na frente; transfusão × picada)",
    extra="HIV transmission risk is highest when viral load peaks.<br>" + IMG("hiv-inoculo")),
 K(1517092173199, "R-detalhe", H_, "Carga viral alta e transmissão do HIV", 172, "lâmina 172 (risco de transmissão × carga viral)"),
 au("au-hpv-suprabasal", "<b>HPV</b> completes its cycle in {{c1::suprabasal}} epithelial layers, far from dermal immune cells",
    "A-aula", H_, "Tropismo do HPV como evasão passiva", 173, "lâminas 173–174; transcrição",
    extra="Its replication stays above the basal layer, away from the dermis.<br>" + IMG("hpv-tropismo")),
 sh(1792695028263, "verde", H_, "HPV infecta a camada basal", 173, "V-hy: card da 58; lâmina 173"),
 K(1516474304091, "A-aula", H_, "Raiva viaja retrógrada nos nervos", 171, "lâmina 171 (raiva); transcrição (transitando dentro dos axônios)"),
 au("au-via-evasao", "Viruses <b>injected into blood</b> by needles or insects bypass {{c1::epithelial}} barriers, a passive evasion by route",
    "A-aula", H_, "Via de infecção como evasão passiva", 171, "lâmina 171; transcrição",
    extra="Examples: poliovirus, HSV and HIV reaching tissues without crossing an epithelium."),
 sh(1792695053292, "azul", H_, "RNA viral muta rápido", 175, "A-aula: card da 58; lâmina 175 (vírus de RNA variam mais)"),
 au("au-variabilidade", "Antigenic {{c1::variability}} of <b>RNA viruses</b> such as influenza and HIV is passive evasion, needing no dedicated viral protein",
    "A-aula", H_, "Variabilidade como evasão passiva", 175, "lâmina 175; transcrição",
    extra="Error-prone copying changes the antigens on its own."),
 K(1506629798167, "V-prova", H_, "HCV: sem revisão → variação antigênica", 175, "prova 2017 P3 4.3 (variabilidade mantém o HCV crônico)"),
 # ---------- Barreiras e destino (lâminas 176–178) ----------
 au("au-barreiras", ORG("<b>Barriers a virus must cross</b> to infect:<br>- {{c1::intrinsic}}: skin, mucosa, receptor, cell defenses<br>- {{c1::innate}} immunity<br>- {{c1::adaptive}} immunity"),
    "A-aula", I_, "Barreiras: intrínseca, inata, adaptativa", 176, "lâmina 176; transcrição",
    extra="Only a virus that crosses all of them establishes a productive infection."),
]

# F-20261022-CLAUDE-04: a resposta do cloze autoral vai em negrito, como no AnKing
for c in CARDS:
    if c["kind"] == "autoral":
        c["text"] = _re.sub(r"\{\{c(\d+)::(.*?)((?:::[^}]*)?)\}\}", lambda m: "{{c%s::<b>%s</b>%s}}" % (m.group(1), m.group(2), m.group(3)), c["text"])

finalizar(CARDS, HERE, BUSCA)

VERSO = {  # chave: "- linha curta" para nota de acervo sem Extra (gate de verso)
 "ak1516325251980": "Enveloped respiratory viruses spread in droplets and aerosols, not on dry surfaces for long.",
 "ak1516237532611": "Both stay in the gut epithelium: a localized enteric infection.",
 "ak1502154338212": "Sensory ganglia innervating the genital area, reached by axonal transport.",
 "ak1502067560663": "No symptoms, but the virus keeps replicating the whole time.",
 "ak1516666167898": "It also leads viral diarrhea worldwide in unvaccinated infants.",
 "ak1516665391803": "A segmented genome allows reassortment between strains.",
 "ak1516665343741": "No envelope, so it survives acid, bile and drying: fecal-oral spread.",
 "ak1516320758799": "Like all negative-sense viruses, it carries its own RNA polymerase.",
 "ak1516321367173": "Segments let two strains swap genes in one cell (antigenic shift).",
 "ak1516322197499": "HA and NA are the targets of neutralizing antibodies.",
 "ak1394240219632": "Low-risk types cause benign warts and papillomas.",
 "ak1394239958498": "High-risk types drive progression to high-grade lesions and invasive carcinoma.",
 "ak1394068322402": "Benign lesions that rarely progress to cancer.",
 "ak1463105840341": "The squamocolumnar junction, where reserve cells divide.",
 "ak1516474508193": "Moving inside axons keeps the virus away from antibodies.",
 "ak1517092173199": "The larger the inoculum, the higher the chance of infection.",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "au-resp-comum": "ganho: o AnKing dá a via de cada vírus; aqui a via respiratória como a porta mais comum de todos",
 "au-entericos": "ganho: o AnKing dá rotavírus como causa de gastroenterite; aqui o contraste entérico localizado × sistêmico",
 "au-doenca-dep": "ganho: organizador do que decide a doença; a coincidência com um card AnKing é só a palavra 'type'",
 "au-fatores": "ganho: organizador das funções dos fatores de virulência; o AnKing só dá a NSP4 como enterotoxina",
 "au-alcool": "ganho: o AnKing dá rinovírus nu e álcool rompendo envelope; aqui a consequência prática (álcool-gel não o inativa)",
 "au-susc-perm": "ganho: a 58 tem o organizador das quatro condições; aqui o contraste suscetível × permissiva que a prova 2019 P3 3.3 pede",
 "au-latencia-evasao": "ganho: a latência aparece como padrão (au-latencia) e aqui como mecanismo de evasão ativa, como na lâmina 170",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "mb59-resp-sitios.png": "lâmina 126: epitélio mucociliar e sítios de replicação por região do trato com a síndrome de cada um",
 "mb59-disseminacao.png": "lâmina 129: superfície → linfonodo → sangue → fígado/baço → viremia secundária → órgãos-alvo e eliminação",
 "mb59-padroes.png": "lâmina 133: as cinco curvas (aguda, latente, progressiva, persistente, falha em eliminar)",
 "mb59-padroes-comp.png": "lâmina 145: aguda (flu), persistente (HBV), latente (HSV) e HIV na mesma escala",
 "mb59-hsv-latencia.png": "lâmina 136: HSV lítico no epitélio, latente no neurônio e reativado descendo o axônio",
 "mb59-ebv-latencia.png": "lâmina 137: EBV da orofaringe às células B, latências III, II, 0 e I",
 "mb59-hbv-aguda.png": "lâmina 139: DNA viral sobe e cai antes da ALT; anticorpos surgem; recuperação",
 "mb59-hbv-cronica.png": "lâmina 140: HBsAg persiste décadas com DNA e ALT oscilando; hepatite crônica",
 "mb59-hiv-setpoint.png": "lâmina 144: carga viral e CD4 no HIV, set point e latência clínica",
 "mb59-rota-nsp4.png": "lâmina 157: NSP4 eleva Ca2+ na célula infectada e nas vizinhas; segundo ciclo lítico",
 "mb59-polio-trajeto.png": "lâmina 167: intestino → linfonodos mesentéricos → viremia primária e secundária → SNC",
 "mb59-hiv-inoculo.png": "lâmina 172: risco de transmissão do HIV acompanha a carga viral em cada fase",
 "mb59-hpv-tropismo.png": "lâmina 173: HPV entra pela camada basal por microtrauma e completa o ciclo nas camadas suprabasais",
}
REVISAO = {}
ESCOPO_ = {"objetivo": "Entender o que decide se um vírus infecta, como se espalha, por quanto tempo fica e se causa doença: entrada, disseminação, padrões, determinantes (suscetibilidade, permissividade, acesso, resposta), virulência, tropismo e evasão.",
          "centrais": ["au-resp-comum", "au-dissemina", "au-padroes", "au-latencia", "au-dep-padrao", "au-manifest", "au-virulencia", "au-evasao",
                       "sh-1792677732277", "sh-1792695018040", "au-polio-capsid"],
          "exemplos": ["au-papiloma-laringe", "au-hpv-70", "au-hbv-adulto"],
          "outras_aulas": ["57 Princípios gerais dos vírus", "58 Multiplicação viral", "61 Patologia da infecção viral", "63 Resposta imune aos vírus",
                           "Agentes carcinogênicos biológicos"]}
ESCOPO = dict(ESCOPO_, centrais=[
 ["vírus é parasita de tecidos; produtiva × abortiva", "sh-1792677732277", "sh-1792695018040"],
 ["via respiratória é a porta mais comum", "au-resp-comum"],
 ["trajeto da disseminação", "au-dissemina"],
 ["padrões de infecção", "au-padroes", "au-latencia"],
 ["latência clínica × viral", "au-lat-clin"],
 ["HBV vertical cronifica", "ak1506552371527"],
 ["do que depende o padrão", "au-dep-padrao"],
 ["modos de causar doença", "au-manifest"],
 ["suscetível × permissiva; sarampo sistêmico", "au-susc-perm", "au-sarampo"],
 ["virulência", "au-virulencia"],
 ["tropismo: rinovírus × poliovírus; atenuação restringe o tropismo", "ak1516222409950", "au-polio-capsid", "au-sabin"],
 ["rotavírus: diarreia secretória e osmótica", "au-rota-duas"],
 ["evasão ativa × passiva", "au-evasao"],
 ["variabilidade do HCV", "ak1506629798167"]])
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
