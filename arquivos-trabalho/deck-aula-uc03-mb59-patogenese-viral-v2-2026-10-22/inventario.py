"""Inventário atômico da 59 Patogênese da infecção viral (UC03 P3; Microbiologia; Prof. Enrique Boccardo), escrito a partir do material lido
nesta sessão (23/10; refação v7 no mesmo dia: ficha técnica dos vírus vira EXC): 178 lâminas em três versões (I 1–61 Zanotto, II 62–119, III 120–178 "Infecção do hospedeiro suscetível", vista como
imagem e seguida pela fala), transcrição inteira, apostila guia de Micro (aula 14), monitoria P3 (aula 16), UC3.pdf (pp. 417–427), provas
(índice micro-15 e busca por termo), Jawetz cap. 30 e Ninja Nerd (hepatites). Blocos e papéis: compreensao-aula.json.
"""
PREFIXO = "mb59"
AULA = "Patogênese da infecção viral (UC03 P3; Microbiologia; Prof. Enrique Boccardo)"
EXC = "EXC: "
_C, _R = "conteudo", "revisao"

M = {  # lâmina da versão III: (classe, título, [(id, ideia, destino)])
 120: ("capa", "Capa: infecção do hospedeiro suscetível", []),
 121: (_C, "Vírus: parasitas intracelulares obrigatórios, logo de tecidos", [("a", "Parasita intracelular obrigatório", "sh-1792677732277"), ("b", "Parasita de tecidos e órgãos", "au-tecidos")]),
 122: (_C, "Infecção produtiva × abortiva; infecção ≠ doença", [("a", "Produtiva × abortiva", "sh-1792695018040"), ("b", "Infecção não é doença", "sh-1791746116702")]),
 123: ("capa", "Divisória: entrada e disseminação", []),
 124: (_C, "Portas de entrada; a respiratória é a mais comum", [("a", "Portas de entrada", "sh-1791780622904"), ("b", "Respiratória é a mais comum", "au-resp-comum")]),
 125: (_C, "Trato respiratório: área, defesas, aerossol × contato, local × sistêmica",
       [("a", "Defesa mucociliar e IgA", "sh-1791147098269"), ("b", "Aerossol: influenza", "ak1516325251980"), ("c", "Contato: rinovírus", "ak1516222208131"),
        ("d", "Localizada × sistêmica", "au-local-sist")]),
 126: (_C, "Sítio de replicação no trato e quadro clínico", [("a", "Região do trato define o quadro", "au-regiao")]),
 127: (_C, "Receptores são moléculas de adesão: ICAM-1, CAR", [("a", "Receptor = molécula de adesão", "au-adesao"), ("b", "ICAM-1 do rinovírus", "ak1516222322469"), ("c", "CAR do adenovírus", "EXC: CAR do adenovírus: card da 58; aqui basta o princípio (au-adesao)")]),
 128: (_C, "Trato alimentar: resistência a pH, bile e enzimas; entéricos local × sistêmico",
       [("a", "Vírus entérico resiste a ácido e bile", "sh-1792677742326"), ("b", "Gastroenterite por rotavírus e norovírus", "EXC: repete au-entericos"), ("c", "Entéricos localizados × sistêmicos", "au-entericos")]),
 129: (_C, "Disseminação: sítio primário, linfa, viremia, sítio secundário", [("a", "Trajeto da disseminação", "au-dissemina"), ("b", "Incubação local × sistêmica", "au-incubacao")]),
 130: (_C, "Viremia: livre ou em linfócitos; ativa × passiva", [("a", "Viremia", "au-viremia"), ("b", "Viremia ativa × passiva", "au-viremia-passiva")]),
 131: ("capa", "Divisória: padrões de infecção", []),
 132: (_C, "Aguda × crônica (replicação contínua ou latência)", [("a", "Aguda × crônica", ["au-padroes", "au-aguda"])]),
 133: (_C, "As cinco curvas de padrão; infecção não é doença", [("a", "Padrões", "au-padroes"), ("b", "Falha em eliminar ≠ latência", "au-falha")]),
 134: (_C, "Infecção aguda: restrita no tempo", [("a", "Aguda", "au-aguda")]),
 135: (_C, "Latência: estado transcricional único, reativável", [("a", "Latência", "au-latencia")]),
 136: (_C, "HSV: latência no neurônio e reativação",
       [("a", "Trajeto do HSV", "au-hsv-axonio"), ("b", "HSV-1 trigêmeo", "ak1502153397982"), ("c", "HSV-2 sacral", "EXC: HSV-2 sacral não está na fala; ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"),
        ("d", "Estresse reativa", "ak1502152875721"), ("e", "Pico de reativação menor", "au-reativ")]),
 137: (_C, "EBV: orofaringe, célula B e tipos de latência",
       [("a", "Célula de vida longa", "au-celula-longa"), ("b", "Saliva", "ak1503853508872"), ("c", "Epitélio da orofaringe", "ak1503854280231"),
        ("d", "CD21", "EXC: CD21 e anticorpo heterófilo: clínica/diagnóstico da mononucleose"), ("e", "Latente na célula B", "ak1503854748516"), ("f", "Latência 0", "au-ebv-0")]),
 138: (_C, "Aguda × crônica persistente", [("a", "Persistente", "au-persistente")]),
 139: (_C, "Hepatite B aguda: curvas", [("a", "90% dos adultos curam", "au-hbv-adulto"), ("b", "Lesão imunomediada", "au-hbv-imune"), ("c", "Anti-HBs na recuperação", "ak1552683158377")]),
 140: (_C, "Hepatite B crônica: curvas", [("a", "Vertical cronifica", "ak1506552371527"), ("b", "HBsAg > 6 meses", "ak1521044243769")]),
 141: (_C, "Hepatite C aguda", [("a", "HCV cronifica na maioria", "ak1506630060423")]),
 142: (_C, "Hepatite C crônica", [("a", "HCV cronifica na maioria", "ak1506630060423"), ("b", "HBV cronifica menos que HCV", "EXC: repete ak1506630060423 e au-hbv-adulto")]),
 143: (_C, "Infecção progressiva", [("a", "Progressiva", "au-progressiva")]),
 144: (_C, "HIV: set point e latência clínica",
       [("a", "Set point", "au-setpoint"), ("b", "Latência clínica × viral", "au-lat-clin"), ("c", "Duração da latência clínica", "EXC: duração em anos: aula de HIV"), ("d", "CD4 baixo: AIDS", "EXC: CD4 < 200: aula de HIV")]),
 145: (_C, "Comparação dos padrões", [("a", "Padrões comparados", "au-padroes")]),
 146: (_C, "Do que dependem os padrões", [("a", "Vírus, via, resposta", "au-dep-padrao")]),
 147: (_C, "Resposta do hospedeiro e evasão", [("a", "Aguda: inata; crônica: adaptativa", "au-inata-adapt"), ("b", "Cronificar exige evasão", "au-cronificar")]),
 148: (_C, "Patogênese: vírus, espécie, indivíduo, via", [("a", "Do que depende a doença", "au-doenca-dep"), ("b", "Tipo de vírus: SARS-CoV-2 × sazonais", "EXC: doenças por coronavírus: clínica; o ponto (tipo de vírus) está em au-doenca-dep")]),
 149: (_C, "Infecção ≠ doença; comparar assintomáticos e doentes", [("a", "Infecção não é doença", ["sh-1791746116702", "au-doenca-dep"])]),
 150: (_C, "Manifestações da patogênese", [("a", "Modos de causar doença", "au-manifest"), ("b", "Imunopatologia", "au-imunopatologia"), ("c", "Tumores", "au-tumores")]),
 151: (_C, "Infecção produtiva × abortiva (retomada)", [("a", "Produtiva × abortiva", "sh-1792695018040")]),
 152: (_C, "Suscetibilidade, permissividade, acessibilidade, resposta imune",
       [("a", "Condições da infecção produtiva", "sh-1792695018289"), ("b", "Suscetível × permissiva", "au-susc-perm"), ("c", "Hemácia", "au-hemacia"),
        ("d", "Acessibilidade", "au-acess"), ("e", "Sarampo sistêmico", "au-sarampo")]),
 153: (_C, "Virulência: capacidade relativa de causar doença", [("a", "Virulência", "au-virulencia")]),
 154: (_C, "Estirpes virulentas × atenuadas; do que depende", [("a", "Atenuada", "au-atenuada"), ("b", "Do que depende a virulência", "au-vir-dep")]),
 155: (_C, "Fatores de virulência", [("a", "Fatores de virulência", "au-fatores")]),
 156: (_C, "Rotavírus: família, genoma, NSP4",
       [("a", "Principal diarreia grave infantil", "ak1516666167898"), ("b", "Reovírus", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("c", "Dupla fita", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"),
        ("d", "Segmentado", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("e", "Não envelopado", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("f", "Forma de roda", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"),
        ("g", "Fecal-oral", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("h", "Diarreia aquosa", "EXC: repete au-rota-duas"), ("i", "NSP4 enterotoxina", "ak1516665751235")]),
 157: (_C, "Rotavírus: NSP4, Ca²⁺, Cl⁻; lise das células de lactase",
       [("a", "NSP4 → Ca²⁺", "au-nsp4-ca"), ("b", "NSP4 → Cl⁻", "EXC: repete au-nsp4-ca"), ("c", "Parácrino", "au-paracrino"), ("d", "Vilosidades", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"),
        ("e", "Lactase secundária", "ak1516666902436"), ("f", "Diarreia osmótica", "EXC: coberto por au-rota-duas"), ("g", "Evitar leite", "EXC: coberto por au-rota-duas"), ("h", "Diarreia secretória × osmótica", "au-rota-duas")]),
 158: (_C, "Influenza: estrutura, HA e NA",
       [("a", "RNA −", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("b", "8 segmentos", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("c", "Nome por HA e NA", "ak1516322197499"), ("d", "HA liga ácido siálico", "EXC: HA liga ácido siálico: card da 58"),
        ("e", "NA libera", "EXC: NA libera: card da 58"), ("f", "Variação em HA e NA", "ak1516321589458"), ("g", "Drift ou shift", "EXC: mecanismo de drift/shift: fica a consequência (vacina anual, pandemias)"),
        ("h", "Drift: mutações pontuais", "EXC: mecanismo de drift: fica a consequência"), ("i", "Drift: epidemias", "EXC: repete ak1516322946030"), ("j", "Drift: vacina anual", "ak1516322946030")]),
 159: (_C, "Pandemias de influenza", [("a", "Shift: rearranjo entre espécies", "EXC: coberto por sh-1792695053893"), ("b", "Rearranjo", "sh-1792695053893"), ("c", "Shift: pandemias", "ak1516323168130")]),
 160: (_C, "HPV: ~40 tipos anogenitais, baixo × alto risco", [("a", "Baixo risco 6/11", "ak1394240219632"), ("b", "Alto risco 16/18", "ak1394239958498")]),
 161: (_C, "Verrugas genitais", [("a", "Verrugas por HPV 6/11", "EXC: verruga por HPV 6/11: clínica; o tipo de baixo risco está em ak1394240219632")]),
 162: (_C, "Papilomatose de laringe", [("a", "Papiloma laríngeo HPV 6/11", "EXC: coberto por au-papiloma-laringe (o ponto da lâmina é a gravidade pelo local)"), ("b", "Gravidade pelo local", "au-papiloma-laringe")]),
 163: (_C, "HPV e câncer cervical", [("a", "Zona de transformação", "EXC: zona de transformação: aula de patologia do colo")]),
 164: (_C, "HPV 16 e 18 ≈ 70% dos cânceres cervicais", [("a", "70%", "au-hpv-70")]),
 165: (_C, "Tropismo: rota dos vírus respiratórios",
       [("a", "Receptor define tropismo", "EXC: receptor define tropismo: card da 58"), ("b", "HA define o tropismo do influenza", "ak1516324044281"), ("c", "Vias inferiores, mais grave", "au-influenza-inferior")]),
 166: (_C, "Rinovírus",
       [("a", "Picornaviridae", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("b", "RNA +", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("c", "Não envelopado", "EXC: coberto por au-alcool"), ("d", "Resfriado", "ak1516222286888"),
        ("e", "> 100 sorotipos", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("f", "Via aérea superior", "EXC: coberto pelo verso de ak1516222409950 (só no nariz)"), ("g", "Ácido-lábil", "ak1516222135232"), ("h", "33 °C", "ak1516222409950"),
        ("i", "Por que só no nariz", "ak1516222409950"), ("j", "Álcool rompe envelope", "EXC: álcool e envelope: card da 57; aqui au-alcool"), ("k", "Álcool-gel não inativa", "au-alcool")]),
 167: (_C, "Poliovírus: resistente ao ácido, intestino → SNC",
       [("a", "Picornavírus fecal-oral", "EXC: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("b", "Ácido-estável", "ak1516218404816"), ("c", "Capsídeo decide o tropismo", "au-polio-capsid"),
        ("d", "Tonsilas e Peyer", "EXC: coberto por au-polio-trajeto"), ("e", "Viremia até o SNC", "au-polio-trajeto"), ("f", "Corno anterior", "EXC: neurônio motor: patologia da pólio, fora da aula"),
        ("g", "Sabin atenuada", "ak1516219553378"), ("h", "Sabin não chega ao SNC", "au-sabin"), ("i", "Sabin: IgA", "EXC: IgA da Sabin: aula de vacinas")]),
 168: (_C, "Evasão ativa × passiva", [("a", "Ativa × passiva", "au-evasao")]),
 169: (_C, "E6 e E7 do HPV", [("a", "E6/E7 bloqueiam interferon", "au-e6e7")]),
 170: (_C, "Latência do EBV como evasão ativa", [("a", "Latência como evasão", "au-latencia-evasao")]),
 171: (_C, "Evasão passiva: inóculo, tropismo, via, variabilidade",
       [("a", "Inóculo", "au-inoculo"), ("b", "Raiva retrógrada", "ak1516474304091"), ("c", "Raiva até o gânglio", "EXC: gânglio da raiz dorsal: ficha técnica do vírus, fora do mecanismo que a lâmina ensina (v7)"), ("d", "Via", "au-via-evasao")]),
 172: (_C, "Inóculo: risco de transmissão do HIV × carga viral", [("a", "Carga viral e transmissão", "ak1517092173199")]),
 173: (_C, "Tropismo do HPV: camadas suprabasais", [("a", "Suprabasal", "au-hpv-suprabasal"), ("b", "Camada basal", "sh-1792695028263")]),
 174: (_C, "Tropismo do HPV: lesão longe da derme", [("a", "Suprabasal", "au-hpv-suprabasal")]),
 175: (_C, "Variabilidade: influenza, HIV", [("a", "RNA muta", "sh-1792695053292"), ("b", "Variabilidade como evasão", "au-variabilidade"), ("c", "HCV", "ak1506629798167")]),
 176: (_C, "Barreiras: intrínseca, inata, adaptativa", [("a", "Barreiras", "au-barreiras")]),
 177: (_C, "Resumo: balanço vírus × hospedeiro", [("a", "Balanço", "au-barreiras")]),
 178: ("capa", "Agradecimento", []),
}
# Versões I e II: mesmas lâminas da III (a II não tem a 127 e a I traz o texto do EBV na 18 e SARS-CoV-2 na 58).
_ESPELHO_I = {1: 120, 2: 121, 3: 122, 4: 123, 5: 124, 6: 129, 7: 125, 8: 126, 9: 128, 10: 130, 11: 131, 12: 132, 13: 133, 14: 134, 15: 135, 16: 136,
              17: 137, 18: 137, 19: 138, 20: 139, 21: 139, 22: 140, 23: 140, 24: 141, 25: 142, 26: 143, 27: 144, 28: 145, 29: 146, 30: 147, 31: 148,
              32: 149, 33: 150, 34: 151, 35: 152, 36: 153, 37: 154, 38: 155, 39: 156, 40: 157, 41: 158, 42: 159, 43: 160, 44: 161, 45: 162, 46: 163,
              47: 164, 48: 165, 49: 166, 50: 167, 51: 168, 52: 169, 53: 170, 54: 171, 55: 172, 56: 173, 57: 174, 58: 175, 59: 176, 60: 177, 61: 178}
SLIDES = []
for _n in range(1, 120):
    _i = _n if _n <= 61 else (_n - 61 if _n <= 78 else {79: 19, 80: 20, 81: 22}.get(_n, _n - 58))  # a II não tem I-18, I-21, I-23
    _ref = _ESPELHO_I[_i]
    SLIDES.append((_n, _R, M[_ref][1] + f" (repete a lâmina {_ref})", []))
SLIDES += [(n,) + M[n] for n in range(120, 179)]
JUSTIFICATIVAS = {"revisao": "versão I ou II das lâminas, repetição da versão III que a fala segue; os cards apontam para a III"}
CAPITULO = [("Jawetz cap. 30 (patogênese e controle das doenças virais)", [
 ("l1", "Maioria das infecções é subclínica", "sh-1791746116702"),
 ("l2", "Infecção local × sistêmica; incubação curta × longa", ["au-local-sist", "au-incubacao"]),
 ("l3", "Viremia livre ou em células; propagação neural", ["au-viremia", "ak1516474304091"]),
 ("l4", "Herpes latente em gânglios sensitivos, reativado por imunossupressão", ["au-hsv-axonio", "ak1502153397982"]),
 ("l5", "Poliomielite: intestino → linfonodos → viremia → SNC", "au-polio-trajeto"),
 ("l6", "Vírus entéricos resistem a ácido e bile", "sh-1792677742326")])]
EXERCICIOS = [
 ("Provas UC03 (índice micro-15 e busca por termo)", [
  ("p1", "Suscetibilidade e permissividade; sarampo sistêmico (2019 P3 3.3)", ["au-susc-perm", "au-sarampo"]),
  ("p2", "Sarampo × influenza: tropismo, incubação, imunossupressão (2025 P3 3.6)", ["au-sarampo", "au-incubacao", "au-local-sist"]),
  ("p3", "Padrão de infecção da hepatite B e curvas (2015 P2 2.4)", ["au-hbv-adulto", "ak1506552371527", "ak1521044243769"]),
  ("p4", "Principais padrões com exemplos (2015 P2sub 2.5)", ["au-padroes", "au-latencia", "au-persistente", "au-progressiva"]),
  ("p5", "Evasão do HCV para cronificar (2017 P3 4.3)", ["au-variabilidade", "ak1506629798167"])]),
 ("Monitoria P3 de Micro, aula 16", [
  ("m1", "Quatro formas crônicas, inclusive falha em eliminar", ["au-padroes", "au-falha"]),
  ("m2", "Latência só nos herpesvírus, em célula de vida longa", ["au-latencia", "au-celula-longa"])]),
 ("Apostila guia de Micro, aula 14", [
  ("a1", "Receptores de adesão causam disfunção", "au-adesao"),
  ("a2", "Drift × shift", ["ak1516322946030", "ak1516323168130"])])]
