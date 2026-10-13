"""Inventário atômico de Integração metabólica I – especialização por órgãos e tecidos (UC03 P2, Bioquímica; 70 lâminas da turma;
a pasta pessoal 25 tem uma apostila NEBLI, não lâminas). Escrito em 10/10/2026 antes da seleção: lâminas (visual/folha-NN), transcrição
da videoaula (fontes/transcricao.txt), provas biomol-04 (3 subquestões: jejum inflamatório, jejum prolongado, glicerol), guia de veteranos
de Biologia Molecular aula 7 (fontes/apostila-veteranos-guia.txt), apostila NEBLI E1 (fontes/apostila-nebli.txt, só apoio).
"""
PREFIXO = "bq25"
AULA = "Integração metabólica I – especialização por órgãos e tecidos (UC03 P2; Bioquímica)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Nutrientes, armazenamento, produção de energia", [("regulacao", "Ajuste a situações fisiológicas = regulação metabólica", "insulina-alimentado")]),
 (3, "capa", "Divisória: regulação metabólica", []),
 (4, "conteudo", "Síntese e degradação de enzimas", [("longo-prazo", "Alterar a quantidade de enzima é a forma mais decisiva (longo prazo)", "quantidade-enzima")]),
 (5, "conteudo", "Formas de alterar atividade", [("formas", "Alostérica, covalente, hormonal", ["feedback", "fosforilase-ativa", "insulina-alimentado"])]),
 (6, "capa", "Divisória: alostérica", []),
 (7, "conteudo", "Retroinibição", [("feedback", "Produto final inibe enzima inicial", "feedback"), ("duplo", "Mesmo composto + numa via e − noutra", "efetor-duplo")]),
 (8, "conteudo", "Enzimas alostéricas", [("sitio", "Efetores ligam sítio alostérico", "feedback")]),
 (9, "conteudo", "Krebs por cofatores", [("krebs", "Ciclo de Krebs regulado por NADH, ATP, substratos", "krebs-nadh")]),
 (10, "capa", "Divisória: covalente", []),
 (11, "conteudo", "Modificação covalente", [("cov", "Grupo ligado muda conformação e atividade", "fosforilase-ativa")]),
 (12, "conteudo", "Fosforilação/desfosforilação", [("quinase", "Quinase e fosfatase", "fosforilase-ativa")]),
 (13, "conteudo", "Glicogênio fosforilase", [("fosforilase", "Fosforilase b/a; AMP, ATP, G6P, glicose", ["fosforilase-ativa", "fosforilase-figado-glicose"])]),
 (14, "conteudo", "Sintase × fosforilase", [("sintase", "PKA fosforila: sintase inativa, fosforilase ativa", ["sintase-inativa", "fosforilase-ativa"])]),
 (15, "conteudo", "PDH por modificação covalente", [("pdh", "E1 fosforilado inativo; ADP, Ca²⁺ ativam", ["pdh-fosforilada", "pdh-ativadores"])]),
 (16, "capa", "Divisória: hormonal", []),
 (17, "conteudo", "Tecidos especializados, ação conjunta por hormônios", [("conjunto", "Hormônios coordenam os tecidos (transcrição: maestro)", "insulina-alimentado")]),
 (18, "conteudo", "Gangorra insulina × glucagon", [("gangorra", "Alimentado: insulina; jejum: glucagon", ["insulina-alimentado", "sh-1791054011246"])]),
 (19, "conteudo", "Tecidos (figura)", [("tecidos", "Coração, fígado, pâncreas, adiposo, rim, cérebro, músculo, hemácias", "reserva-figado-musculo")]),
 (20, "conteudo", "Vias metabólicas (tabela)", [("vias", "Tabela de vias catabólicas e anabólicas", EXC + "tabela de revisão da UC01, sem foco próprio na aula")]),
 (21, "capa", "Divisória: fígado", []),
 (22, "conteudo", "Papel dos órgãos (figura)", [("orgaos", "Fígado processa e distribui; veia porta; adiposo; músculo", ["reserva-figado-musculo", "porta"])]),
 (23, "conteudo", "Funções do fígado", [("funcoes", "Mais de 500 funções", "reserva-figado-musculo")]),
 (24, "conteudo", "Funções do fígado (tabela)", [("funcoes2", "Detoxificação, síntese de proteínas e lipídeos", "reserva-figado-musculo")]),
 (25, "conteudo", "Câmara de compensação", [("compensacao", "Grande capacidade adaptativa; mantém a glicemia", "reserva-figado-musculo")]),
 (26, "conteudo", "Vídeo (veia porta)", [("video", "Link", EXC + "link externo")]),
 (27, "conteudo", "Vias de carboidratos no fígado", [("vias-fig", "Gliconeogênese, glicogenólise, glicólise, glicogênese, pentoses", ["reserva-figado-musculo", "rim-gliconeogenese"])]),
 (28, "conteudo", "Regulação de enzimas e transportadores", [("reg", "Transportadores e enzimas", "glut2-km")]),
 (29, "conteudo", "GLUTs", [("gluts", "GLUT1, 3, 4 alta afinidade", ["glut1", "glut2"])]),
 (30, "conteudo", "GLUT1–4", [("glut-dist", "GLUT1 hemácia/cérebro, GLUT2 fígado/β, GLUT3 cérebro, GLUT4 insulina", ["glut1", "glut2", "glut3", "sh-1791054011372"])]),
 (31, "conteudo", "GLUT2 Km alto", [("glut2", "Transporta na hiperglicemia; [glicose] hepatócito = sangue", "glut2-km")]),
 (32, "conteudo", "Glicoquinase", [("gk", "Km alto, não inibida por G6P; na hipoglicemia glicose sai", ["gk-km", "hk-km", "gk-g6p", "gk-hipoglicemia", "aprisionamento"])]),
 (33, "conteudo", "Enzimas irreversíveis", [("irrev", "Pontos de controle: reações irreversíveis", "irreversiveis")]),
 (34, "conteudo", "PFK-1", [("pfk1", "F6P → F1,6BP", "pfk1-limitante")]),
 (35, "conteudo", "Frutose-2,6-bisfosfato", [("f26bp", "F2,6BP", ["f26-pka", "f26-glucagon", "pfk2-efeito"])]),
 (36, "conteudo", "PFK-1 × FBPase-1", [("pfk-fbp", "ATP/citrato inibem PFK1; AMP e F2,6BP ativam; F2,6BP inibe FBPase", ["pfk1-inibe", "pfk1-ativa", "fbpase-inibe"])]),
 (37, "conteudo", "Glicose-6-fosfatase", [("g6pase", "Ativa na glicogenólise e gliconeogênese; músculo não tem", ["g6pase-musculo", "g6pase-re"])]),
 (38, "conteudo", "Fosforilase hepática", [("fos-fig", "Fosforilase a sensível à glicose, não ao AMP", ["fosforilase-figado-glicose", "fosforilase-figado-amp"])]),
 (39, "conteudo", "Vídeo (ciclo da ureia)", [("video2", "Link", EXC + "link externo")]),
 (40, "conteudo", "Fígado e aminoácidos", [("aa", "Dieta: síntese; do músculo: desaminação → gliconeogênese", ["cahill", "proteina-musculo"])]),
 (41, "conteudo", "Fígado e lipídeos (figura)", [("lip-fig", "Vias de lipídeos no fígado", "acc-insulina")]),
 (42, "conteudo", "Fígado: insulina × glucagon nos lipídeos", [
   ("lip-ins", "Insulina: síntese de AG e TAG, exporta", ["acc-insulina", "acc-glucagon"]),
   ("lip-glu", "Glucagon: β-oxidação, corpos cetônicos", ["betaox-cetogenese", "cetogenese-figado"])]),
 (43, "conteudo", "Glicogênio hepático regulado pelo glucagon", [("glico-glucagon", "Atende à demanda do organismo", "glicogenio-figado-glucagon")]),
 (44, "conteudo", "Glucagon degrada glicogênio", [("glucagon-ampc", "Glucagon → AMPc → PKA", ["glucagon-ampc", "sh-1791054011246"])]),
 (45, "conteudo", "Insulina e glicoquinase", [("ins-gk", "Insulina não muda captação hepática; induz glicoquinase", "gk-insulina")]),
 (46, "conteudo", "Insulina ativa PP1", [("pp1", "PP1 desfosforila: sintase ativa, fosforilase inativa", "pp1")]),
 (47, "conteudo", "Lipase hormônio-sensível", [("hsl", "Glucagon/epinefrina → AMPc → PKA → HSL", ["hsl", "hsl-hormonios"])]),
 (48, "conteudo", "Insulina inibe lipólise", [("ins-lip", "Desfosforila lipases", "hsl-insulina")]),
 (49, "capa", "Divisória: músculo", []),
 (50, "conteudo", "Papel do músculo (figura)", [("mus-fig", "Usa ATP para trabalho mecânico", "reserva-figado-musculo")]),
 (51, "conteudo", "Músculo: demanda, epinefrina, insulina", [("mus-reg", "Energia para consumo próprio", ["reserva-figado-musculo", "epinefrina-beta"])]),
 (52, "conteudo", "Músculo esquelético", [
   ("sem-glucagon", "Sem modulação por glucagon", "musculo-sem-glucagon"),
   ("adrenalina", "Adrenalina ativa glicólise e glicogenólise", "epinefrina-beta"),
   ("fibras", "Vermelhas oxidativas; brancas glicolíticas", ["fibra-lenta", "fibra-rapida"]),
   ("pcr", "Fosfocreatina", "fosfocreatina")]),
 (53, "conteudo", "Músculo cardíaco", [("cardiaco", "Oxidativo; AG e corpos cetônicos; pouco glicogênio", "cardiaco")]),
 (54, "conteudo", "Energia para contração", [("energia", "ATP, fosfocreatina, glicogênio, AG", ["fosfocreatina", "atp-segundos"])]),
 (55, "conteudo", "Ciclo de Cori", [("cori", "Lactato muscular → glicose hepática", ["cori", "cori-nad"])]),
 (56, "conteudo", "Glicogenólise muscular", [("glicogenolise-m", "Ativação da fosforilase", ["fosforilase-ativa", "musculo-g6p"])]),
 (57, "conteudo", "Fosforilase muscular", [("fos-m", "AMP ativa (R); ATP e G6P favorecem T; sem G6Pase", ["fosforilase-amp-musculo", "g6pase-musculo"])]),
 (58, "conteudo", "G6P ativa glicogênio sintase", [("g6p-gs", "PFK inibida → G6P ↑ → sintase ativa", "g6p-sintase")]),
 (59, "conteudo", "Epinefrina degrada glicogênio", [("epi", "Cascata da epinefrina", "epinefrina-beta")]),
 (60, "conteudo", "Fim do estímulo", [("fim", "GTPase da Gα, fosfodiesterase, PKA reassocia", "fim-sinal")]),
 (61, "conteudo", "Insulina e síntese de glicogênio", [("ins-glico", "Insulina: GSK3 e PKA inativas, PP1 ativa", "pp1")]),
 (62, "conteudo", "Papel do adiposo (figura)", [("adip-fig", "Sintetiza, armazena e mobiliza TAG", "adiposo-insulina")]),
 (63, "conteudo", "Tecido adiposo", [
   ("adip", "15% da massa; insulina → glicólise → TAG", "adiposo-insulina"),
   ("lipase", "Glucagon/adrenalina ↑ lipase", "hsl-hormonios"),
   ("marrom", "Marrom: mitocôndrias, UCP1", "ucp1")]),
 (64, "conteudo", "Papel do cérebro (figura)", [("cer-fig", "Integra sinais", "cerebro-glicose")]),
 (65, "conteudo", "Cérebro", [("cerebro", "Glicose; cetonas no jejum prolongado; 20% do O₂", ["cerebro-glicose", "cetonas-cerebro"])]),
 (66, "conteudo", "Rins", [("rins", "Removem ureia; gliconeogênese (G6Pase)", ["rim-ureia", "rim-gliconeogenese"])]),
 (67, "conteudo", "Linfático e porta (figura)", [("linfa", "Linfático leva lipídeos; porta leva nutrientes", "porta")]),
 (68, "conteudo", "Sangue", [("hemacia", "Hemácias sem mitocôndria: glicólise anaeróbia, lactato", ["hemacia-lactato", "hemacia-cetona"])]),
 (69, "conteudo", "Papel do pâncreas (figura)", [("pan-fig", "Secreta insulina e glucagon", "alfa-glucagon")]),
 (70, "conteudo", "Pâncreas", [
   ("alfa", "α: glucagon (↓glicemia, ↑AA, ↑adrenalina)", ["alfa-glucagon", "glucagon-hipoglicemia"]),
   ("beta", "β: insulina (↑glicemia); GLUT2 e glicoquinase", ["beta-insulina", "insulina-glicose", "beta-glut2"]),
   ("pan-nao-hormonio", "Metabolismo próprio não responde a hormônios", "beta-glut2")]),
]
JUSTIFICATIVAS = {"capa": "capa ou divisória, sem conteúdo"}

CAPITULO = [("Lehninger, cap. 23 — metabolismo específico dos tecidos", [
   ("lh-figado", "Fígado: GLUT2 e glicoquinase mantêm a glicemia", ["glut2-km", "gk-km"]),
   ("lh-musculo", "Músculo: fosfocreatina, glicogênio próprio, ciclo de Cori", ["fosfocreatina", "cori"]),
   ("lh-coracao", "Coração oxidativo, ácidos graxos", "cardiaco"),
   ("lh-cerebro", "Cérebro depende de glicose; corpos cetônicos no jejum", "cetonas-cerebro")])]

EXERCICIOS = [
 ("Transcrição da videoaula", [
   ("tr-reservas", "Músculo tem a maior reserva de proteína mobilizável; glicogênio muscular é para uso próprio, o hepático para o organismo", ["proteina-musculo", "reserva-figado-musculo"]),
   ("tr-aprisiona", "Glicose fosforilada não atravessa a membrana", "aprisionamento")]),
 ("Provas UC03 (índice biomol-04)", [
   ("p2025", "2025 P2 1.8: jejum inflamatório; ciclo alanina-glicose; β-oxidação", ["cahill", "jejum-1-3", "jejum-ag"]),
   ("p2024", "2024 P2 1.3: jejum prolongado por tecido (glucagon, PKA, GLUT4, corpos cetônicos)", ["jejum-entre-refeicoes", "jejum-1-3", "cetonas-cerebro", "jejum-prioridade"]),
   ("p2023", "2023 P1 2.2: glicerol → gliconeogênese", "glicerol")]),
 ("Guia de veteranos, aula 7", [
   ("vet-figado", "G6P hepática: glicemia, glicogênio, pentoses, glicólise", ["reserva-figado-musculo", "g6pase-re"]),
   ("vet-fases", "Fases do jejum (glicogênio → gliconeogênese)", ["jejum-entre-refeicoes", "glicogenio-12-18"])]),
]
