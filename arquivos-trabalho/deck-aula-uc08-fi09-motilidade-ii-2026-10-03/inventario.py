"""Inventário atômico da Motilidade II (FI09), refeito em 09/10 (F-20261009-CLAUDE-02) a partir de: 15 lâminas (fontes/slides.txt e
visual/folha1–3), Aires cap. 60 (livros/aires-cap60-motilidade.txt, lido inteiro), Apostila Guia UC08 aula 2 (fontes/monitoria-motilidade.txt)
e P1 2026 da UC08 (provas/p1-2026-TB; Fisiologia Q1 esvaziamento gástrico/piloro, Q2 limiar contrátil × elétrico, gabarito da professora).
O inventário de 03/10 agrupava várias ideias por linha e contava menção no verso como cobertura; aqui cada ideia aponta para o card que a cobra.
"""
PREFIXO = "fi09"
AULA = "Motilidade II (UC08 P1, Fisiologia, Profa. Fran Goulart da Silva)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Eletrofisiologia do músculo liso", [
   ("unitario", "Músculo liso unitário: células acopladas", "sh-1791023270450"),
   ("ondas-lentas", "PM instável; oscilações = ondas lentas (REB)", "ondas-lentas"),
   ("cajal", "Células intersticiais de Cajal: marca-passo", "cajal"),
   ("frequencia", "Ondas lentas por minuto variam por região (estômago 3, duodeno 12, íleo 8–9)", ["ondas-estomago", "ondas-duodeno", "ondas-ileo"]),
   ("canais", "Canais catiônicos: Ca2+/Na+ despolarizam, K+ repolariza (-58 a -40 mV)", "ondas-canais")]),
 (3, "conteudo", "Limiar contrátil × elétrico", [
   ("limiar-contratil", "Atingir o limiar contrátil: pouco Ca2+, contração fraca, sem potenciais", "limiar-contratil"),
   ("limiar-eletrico", "Atingir o limiar elétrico: potenciais em pico na crista da onda", "limiar-eletrico"),
   ("canais-l", "Canais de Ca2+ tipo L não participam das ondas lentas (só dos picos)", "canais-l"),
   ("forca", "Mais PAs na crista = mais força de contração", "picos-forca")]),
 (4, "conteudo", "Distensão e SNE/SNA modulam as ondas", [
   ("amplitude", "Distensão e SNE/SNA aumentam a amplitude (e os picos); repouso × estimulado", "ach-amplitude")]),
 (5, "conteudo", "Mastigação", [
   ("v3", "N. trigêmeo, ramo mandibular", "v3-mastigacao"),
   ("nucleo-motor", "Núcleo motor do trigêmeo no tronco", "nucleo-motor-v"),
   ("musculos", "Masseter, temporal e pterigoideo medial fecham", "fechar-mandibula"),
   ("pterigoideo-lateral", "Pterigoideo lateral abre", "pterigoideo-lateral"),
   ("receptores", "Receptores sensoriais do teto da boca/orofaringe disparam as fases reflexas da deglutição", "receptores-degluticao"),
   ("feedback", "Feedback sensorial ajusta força, direção e número de mastigações",
    EXC + "ideia de controle geral, sem alvo recuperável próprio além de 'receptores → tronco' (receptores-degluticao) e do núcleo motor; nem Aires nem provas a cobram")]),
 (6, "conteudo", "Deglutição", [
   ("fase-oral", "Fase oral voluntária; faríngea e esofágica reflexas (tronco encefálico)", "fase-oral"),
   ("centro", "Centro da deglutição no tronco; eferência vagal (núcleo ambíguo)", ["vago-degluticao", "nucleo-ambiguo"]),
   ("palato", "Fase faríngea 1: elevação do palato mole e dobras palatofaríngeas", "palato-mole"),
   ("constritores", "Fase faríngea 2: contração dos constritores da faringe", "constritores"),
   ("laringe", "Fase faríngea 3: fechamento da laringe (epiglote)", "epiglote"),
   ("respiracao", "Fase faríngea 4: supressão neural da respiração", "respiracao-degluticao"),
   ("ees-relaxa", "Fase faríngea 5: relaxamento do EES", "ees"),
   ("ees-contrai", "Fase esofágica 1: contração do EES", "ees"),
   ("peristalse-primaria", "Fase esofágica 2: peristalse primária", "peristalse-primaria"),
   ("eei-fundo", "Fase esofágica 3: relaxamento do EEI e do fundo gástrico", ["vip-eei-degluticao", "relaxamento-receptivo"]),
   ("peristalse-secundaria", "Peristalse secundária: distensão, não faz parte do reflexo", "peristalse-secundaria")]),
 (7, "video", "Vídeo", []),
 (8, "conteudo", "Relaxamento receptivo", [
   ("receptivo", "Nervo vago e relaxamento receptivo (vagovagal; vagotomia abole)", "relaxamento-receptivo"),
   ("capacidade", "Capacidade de armazenamento 1,0–1,5 L", "capacidade-estomago")]),
 (9, "conteudo", "Sístole antral e piloro", [
   ("sistole", "Sístole antral: retropropulsão do quimo", "sistole-antral"),
   ("regulacao-piloro", "Regulação antral-anterógrada (relaxa) e duodenal-retrógrada (contrai) do piloro", "sh-1790999271207"),
   ("secretina", "Contraem o piloro: secretina", "secretina-piloro"),
   ("cck", "Contraem o piloro: CCK", "cck-esvaziamento"),
   ("gastrina", "Contraem o piloro: gastrina (e aumenta motilidade antral)", "gastrina-motilidade"),
   ("grelina", "Relaxa o piloro: grelina", "grelina-piloro"),
   ("hcl-duodeno", "HCl no duodeno inibe a contração antral (experimento em cão)", "gordura-h")]),
 (10, "conteudo", "Hormônios do esvaziamento", [
   ("acidez-secretina", "Acidez do quimo → secretina (células S)", ["secretina-s", "secretina-estimulo"]),
   ("nutrientes-cck-gip", "Nutrientes → CCK (I) e GIP (K)", ["cck-i", "cck-estimulo", "gip-k"]),
   ("nutrientes-l", "Nutrientes → GLP-1/GLP-2/PYY (células L)", ["glp1-esvaziamento", "pyy"]),
   ("inibicao", "Inibição do esvaziamento: relaxamento do estômago e contração do piloro", "esvaziamento-integracao"),
   ("velocidade", "Velocidade de esvaziamento compatível com a capacidade de processar o quimo", ["esvaziamento-integracao", "gordura-h"]),
   ("insulina", "GLP-1/2 e GIP → insulina", "incretinas"),
   ("saciedade", "CCK e GLP-1 → saciedade", ["glp1-esvaziamento", "pyy"])]),
 (11, "conteudo", "Padrões motores do delgado", [
   ("segmentacao", "Segmentações (1–4 cm): mistura e renovação", "segmentacao"),
   ("peristalse-curta", "Peristalses curtas (10–14 cm): propulsão; relaxamento do esfíncter ileocecal", "peristalse-curta"),
   ("moduladores", "SNE, SNA, CCK e insulina aumentam a motilidade do delgado",
    EXC + "lista de moduladores sem alvo próprio; SNE/SNA já em ach-amplitude e CCK nos cards de esvaziamento; insulina é detalhe muito pequeno"),
   ("transito", "Trânsito intestinal 2–4 h", "transito"),
   ("cmm", "CMM e motilina no jejum (Aires; Ninja Nerd)", ["motilina-cmm", "motilina-jejum"])]),
 (12, "conteudo", "Padrões motores do grosso", [
   ("haustracoes", "Haustrações; cólon proximal absorve água/eletrólitos", "haustracoes"),
   ("distal", "Cólon distal: amassa e lubrifica fezes; absorção de água limitada",
    EXC + "contraste já dado no verso de haustracoes e movimento-massa; sem pergunta própria que valha um card além do de trânsito"),
   ("massa", "Movimentos de massa, 3–4×/dia, levam fezes ao reto", "movimento-massa"),
   ("gastrocolico", "Reflexo gastrocólico (SNA, CCK, gastrina)", "gastrocolico-ak"),
   ("transito", "Trânsito até 48 h", "transito")]),
 (13, "conteudo", "Reflexo da evacuação", [
   ("reflexo", "Estiramento do reto → medula sacral (S1–S4) → nervo pélvico → contração do reto", "reflexo-defecacao"),
   ("parassimpatico", "Parassimpático pélvico", "parassimpatico-tgi"),
   ("eai", "Relaxamento do EAI, involuntário", ["reflexo-defecacao", "sh-1791052036733"]),
   ("eae", "Relaxamento do EAE, voluntário", "sh-1790974699480"),
   ("puborretal", "Relaxamento do puborretal, voluntário", ["sh-1790974694881", "sh-1790974695006"]),
   ("abdominais", "Contração dos músculos abdominais e respiratórios, voluntária", "defecacao-voluntaria")]),
 (14, "conteudo", "Mecanismo do vômito", [
   ("estimulos", "Estímulos: área postrema, córtex, límbico, vestibular, distensão, quimiorradioterapia", ["causas-vomito", "area-postrema-emeticos"]),
   ("area-postrema", "Área postrema junto ao NTS", "area-postrema-local"),
   ("integrador", "Integrador no tronco (NTS)", ["nts-vomito", "nts-coordena"]),
   ("retroperistalse", "Contração reversa do intestino proximal", "vomito-retroperistalse"),
   ("pressao", "Inspiração profunda, contração abdominal, pressão intra-abdominal; relaxamento de esfíncteres", "vomito-pressao")]),
 (15, "capa", "Encerramento", []),
]

CAPITULO = [
 ("Aires cap. 60", [
   ("eletrofisiologia", "Contração já no limiar contrátil; PAs na crista elevam a força (Fig. 60.12)", ["limiar-contratil", "picos-forca"]),
   ("degluticao", "Fase faríngea <1 s: palato, laringe, respiração inibida, constritores, EES relaxa; depois EES contrai", ["constritores", "ees", "respiracao-degluticao"]),
   ("estomago", "Armazenamento 1–2 h no fundo; sístole antral; piloro contrai após cada onda", ["capacidade-estomago", "sistole-antral", "sh-1790999271207"]),
   ("piloro-hormonios", "Gastrina, secretina, CCK e GIP contraem o piloro", ["secretina-piloro", "cck-esvaziamento"]),
   ("delgado", "Segmentação, peristalses curtas, CMM/motilina, ileocecal", ["segmentacao", "peristalse-curta", "motilina-cmm"]),
   ("colon", "Haustrações, movimento de massa, gastrocólico, reflexo da defecação, controle voluntário (pudendo, abdominais)",
    ["haustracoes", "movimento-massa", "gastrocolico-ak", "reflexo-defecacao", "defecacao-voluntaria"]),
   ("vomito", "Peristalse reversa, inspiração profunda, contração abdominal; centros bulbares e zona quimiorreceptora",
    ["vomito-retroperistalse", "vomito-pressao", "area-postrema-local"])]),
]

EXERCICIOS = [
 ("P1 2026 UC08 (Fisiologia)", [
   ("q1-esvaziamento", "Q1: motilidade gástrica e regulação do piloro durante o esvaziamento", ["esvaziamento-integracao", "sistole-antral", "sh-1790999271207"]),
   ("q2-limiares", "Q2: onda lenta no limiar contrátil × elétrico (Ca2+ e força)", ["limiar-contratil", "limiar-eletrico"])]),
 ("Apostila Guia UC08, aula 2", [
   ("ees-fechado", "EES fechado e contraído precisa relaxar; volta a contrair na fase esofágica", "ees"),
   ("duodeno-potente", "Sinais do duodeno são mais potentes que os do estômago no esvaziamento", "esvaziamento-integracao")]),
]
