"""Inventário atômico de Integração metabólica II – estados alimentares (UC03 P2, Bioquímica; Profa. Deborah, IQ-USP; 102 lâminas da turma =
Estados Alimentares I [1–52] e II [53–102]). Escrito em 11/10/2026 antes da seleção. A versão I repete as lâminas 2–52 da II (a II acrescenta o
diabetes, 92–100); por isso os itens estão nas lâminas da versão II. Fontes: lâminas (visual/folha-NN), transcrição oficial (= texto das lâminas),
provas biomol-06 (fontes/provas.txt), guia de veteranos de Biologia Molecular aula 7 (fontes/apostila-veteranos-guia.txt), Lehninger cap. 23
(livros/lehninger-cap23-integracao.txt), apostila NEBLI E1 (fontes/apostila-nebli.txt, só apoio).
"""
PREFIXO = "bq33"
AULA = "Integração metabólica II – estados alimentares (UC03 P2; Bioquímica)"
EXC = "EXC: "
DUP = EXC + "lâmina da versão I, mesmo conteúdo da lâmina correspondente da versão II (53–102)"

SLIDES = [(n, "conteudo", f"Versão I, lâmina {n}", [("dup", "Mesmo conteúdo da lâmina {} da versão II".format(n + 52 if n > 1 else 54), DUP)]) for n in range(1, 53)] + [
 (53, "capa", "Referências (versão II)", []),
 (54, "conteudo", "Insulina e glucagon (figura)", [("ciclo", "Alimento: glicose ↑ → β libera insulina → fígado armazena; glicose ↓ → α libera glucagon → fígado libera glicose", ["insulina-glicogenio", "sh-1791054011246", "sh-1791054011119"])]),
 (55, "conteudo", "Variação hormonal no sangue", [("curvas", "Glucagon, glicose e insulina ao longo do dia, picos após cada refeição", "curvas-refeicao")]),
 (56, "conteudo", "Insulina × glucagon/cortisol", [
   ("abs", "Absorção: insulina ↑ vias biossintéticas (glicogênese, lipogênese), ↓ gliconeogênese e mobilização", ["insulina-glicogenio", "sh-1791647345621"]),
   ("pos", "Entre refeições: glucagon e cortisol ↑ gliconeogênese e enzimas de mobilização", ["cortisol-gliconeogenese", "cortisol-proteolise", "glucagon-gliconeogenese"])]),
 (57, "conteudo", "Glicose e hormônios após a refeição", [("gh", "Glicemia sobe a ~7–8 mM; insulina sobe; glucagon cai", "curvas-refeicao")]),
 (58, "conteudo", "Período absortivo (órgãos)", [("orgaos", "Pâncreas, fígado, músculo e tecido adiposo após a refeição", "sh-1791647345621")]),
 (59, "conteudo", "Secreção de insulina (célula β)", [("beta", "GLUT2 → glicoquinase → ATP → K-ATP fecha → despolariza → Ca²⁺ → exocitose", ["sh-1791647354296", "katp-atp", "katp-fecha", "katp-calcio", "katp-exocitose"])]),
 (60, "conteudo", "Alta razão insulina/glucagon (fígado)", [
   ("gk", "Glicoquinase transloca do núcleo para o citoplasma e retém a glicose", ["gk-transloca", "sh-1791647349695"]),
   ("fosforilase", "Glicose inibe a glicogênio fosforilase", "sh-1791647345020"),
   ("destinos", "Glicose-6-P: glicogênio, pentoses-P e TAG", ["insulina-glicogenio", "pentoses-nadph"])]),
 (61, "conteudo", "Regulação do metabolismo do glicogênio", [
   ("pkb", "Insulina → PKB: PP1 ativa, GSK-3 inativa, PKA inativa, PDE ativa", ["pkb-gsk3", "pkb-pde", "sh-1791647349819"]),
   ("sintase", "Sintase ativa e fosforilase inativa: síntese de glicogênio", "sh-1791647349819")]),
 (62, "conteudo", "Absortivo: carboidratos (glicólise × gliconeogênese)", [("pfk", "↑ Frutose-2,6-bisfosfato; ATP/AMP/citrato; setas para glicólise", ["insulina-pfk2", "sh-1791647347996"])]),
 (63, "conteudo", "Absortivo: metabolismo de carboidratos (PDH)", [("pdh", "Glicose alta → insulina → PFK-2; piruvato desidrogenase ↑ → acetil-CoA ↑ → TCA", "pdh-insulina")]),
 (64, "conteudo", "Acetil-CoA central no metabolismo", [("central", "Acetil-CoA integra glicose, aminoácidos, ácidos graxos, PDH", "pdh-insulina")]),
 (65, "conteudo", "Acetil-CoA ↑ e oxaloacetato ↑", [("krebs", "Aumento de oxaloacetato e acetil-CoA acelera o Krebs: NADH e FADH₂ → ATP", ["pc-acetilcoa", "sh-1791647344769"])]),
 (66, "conteudo", "ATP ↑, NADH ↑, citrato ↑", [("freio", "ATP alto freia a cadeia; NADH acumula e freia o Krebs; citrato acumula", ["sh-1791647344769", "isocitrato-dh"])]),
 (67, "conteudo", "Síntese de lipídeos: citrato no citosol", [("citrato", "Citrato sai para o citosol; citrato liase e acetil-CoA carboxilase fazem malonil-CoA", ["citrato-citosol", "citrato-liase", "acc-malonil"])]),
 (68, "conteudo", "Síntese de lipídeos: insulina", [("malonil", "Ativa a síntese de ácidos graxos e inibe a CAT I, protegendo os ácidos graxos novos da degradação", ["malonil-cat1", "acc-insulina"])]),
 (69, "conteudo", "Síntese de ácidos graxos: NADPH e pentoses", [("nadph", "Síntese de AG consome NADPH e ativa a via das pentoses-P", ["pentoses-nadph", "g6pd-insulina"])]),
 (70, "conteudo", "Absortivo: glicólise e pentose fosfato", [("integra", "Glicólise → piruvato → acetil-CoA e oxaloacetato → NADH/FADH₂ → ATP e citrato → produção de AG e NADPH", ["pentoses-nadph", "malonil-cat1", "citrato-citosol"])]),
 (71, "conteudo", "Exportação hepática", [("export", "AG, TAG, fosfolipídios, colesterol e apoproteínas viram lipoproteínas liberadas na circulação", ["vldl-figado", "exporta-lipoproteinas", "lpl-vldl"])]),
 (72, "conteudo", "Síntese de proteínas", [("prot", "Insulina → entrada de aminoácidos nos tecidos → síntese de proteínas", "insulina-proteina")]),
 (73, "conteudo", "Período absortivo: músculo, fígado e adiposo", [
   ("figura", "Glicogênio muscular, glicogênio e TAG hepáticos, TAG adiposo", ["insulina-glicogenio", "insulina-adiposo"]),
   ("glut4", "GLUT4 no músculo e adiposo captam glicose sob insulina", "sh-1791054011372")]),
 (74, "conteudo", "Glicose e hormônios após a refeição", [("gh2", "Mesmo gráfico da lâmina 57", "curvas-refeicao")]),
 (75, "conteudo", "Utilização da glicose ao longo do jejum", [("util", "Glicose exógena, glicogenólise e gliconeogênese em horas e dias", ["sh-1791647354421", "sh-1791647354545", "sh-1791647354671"])]),
 (76, "conteudo", "Pós-absortivo: glucagon e fígado", [
   ("pos1", "↓ insulina e ↑ glucagon", "pos-razao"),
   ("pos2", "Glucagon sinaliza o jejum; alvo principal fígado", "pos-razao"),
   ("pos3", "No fígado glucagon inibe síntese de glicogênio e AG e estimula gliconeogênese", ["glucagon-gliconeogenese", "glucagon-lipolise"])]),
 (77, "conteudo", "Metabolismo do glicogênio no jejum", [("glicogenolise", "↓ glicemia → glucagon → glicogenólise → manutenção da glicemia (cérebro, hemácias)", ["sh-1791647349571", "sh-1791647354421", "pka-fosforilase"])]),
 (78, "conteudo", "Pós-absortivo: glicólise × gliconeogênese", [("pfk-pos", "Gliconeogênese ativa e glicólise inibida", ["glucagon-gliconeogenese"])]),
 (79, "conteudo", "PFK-2 / FBPase-2", [("bif", "Enzima bifuncional: insulina ativa PFK-2; glucagon via cAMP e PKA ativa FBPase-2", ["sh-1791647347495", "sh-1791647347621"])]),
 (80, "conteudo", "Captação de glicose no jejum", [
   ("indep", "Só tecidos independentes de insulina captam: cérebro, hemácias e medula renal", "tecidos-independentes"),
   ("musculo", "Músculo e adiposo não captam glicose (GLUT4 sem insulina)", "glut4-jejum")]),
 (81, "conteudo", "Lipase hormônio-sensível", [
   ("hsl", "Glucagon ativa a lipase; TAG vira AG e glicerol", "sh-1791647349946"),
   ("alb", "AG viajam no sangue ligados à albumina", "ag-albumina"),
   ("hsl-ins", "Insulina inibe a lipase", "sh-1791647350296")]),
 (82, "conteudo", "Pós-absortivo: lipídeos", [("betaox", "β-oxidação hepática gera acetil-CoA; ACC inativa e malonil-CoA cai", ["betaox-acetilcoa", "acc-jejum"])]),
 (83, "conteudo", "Pós-absortivo: carboidratos e acetil-CoA", [
   ("pdk4", "Acetil-CoA da β-oxidação ativa PDK4 e inibe a PDH", "pdk4-acetilcoa"),
   ("pc", "Ativa a carboxilação do piruvato a oxaloacetato (piruvato carboxilase)", "pc-acetilcoa"),
   ("glicerol", "Gliconeogênese a partir do glicerol", "sh-1791647350421")]),
 (84, "conteudo", "Pós-absortivo: integração músculo, fígado, adiposo", [
   ("glicerol2", "Glicerol → fígado → gliconeogênese", ["glicerol-quinase", "metformina-gpdh"]),
   ("musculo", "Músculo: proteólise e alanina; sem glicose-6-fosfatase", ["sh-1791647348245", "alanina-musculo"]),
   ("inflam", "Jejum relativo inflamatório: citocinas e resistência à insulina", "jejum-inflamatorio")]),
 (85, "conteudo", "Absortivo × pós-absortivo (figuras)", [("comp", "Comparação absortivo e pós-absortivo dos três tecidos", ["curvas-refeicao", "pos-razao"])]),
 (86, "conteudo", "Jejum: aminoácidos", [
   ("ala-gln", "Maioria dos aminoácidos vira alanina e glutamina; piruvato e α-cetoglutarato", ["aa-alanina-glutamina", "alanina-musculo", "glutamina-transporte", "alanina-gliconeogenica"]),
   ("classes", "Aminoácidos glicogênicos e cetogênicos (figura)", "cetogenicos"),
   ("rim", "Glutamina na gliconeogênese renal; balanço nitrogenado negativo", ["gln-rim", "balanco-n-negativo"])]),
 (87, "conteudo", "Ciclo de Cori", [("cori", "Lactato muscular → fígado → glicose", "sh-1791647351570")]),
 (88, "conteudo", "Jejum: corpos cetônicos no sangue", [
   ("grafico", "Cetonas sobem ao longo dos dias, glicose cai, AG constantes", ["sh-1791647352896", "cetonas-poupam", "cetonas-cerebro-2-3"]),
   ("reserva", "Reservas de combustível (TAG ~3 meses)", "reservas-tag")]),
 (89, "conteudo", "Jejum: corpos cetônicos (órgãos)", [
   ("orgaos", "Tecido adiposo → fígado → corpos cetônicos → cérebro, coração e músculo; hemácias não usam", ["sh-1791647349321", "sh-1791647349146", "sh-1791647353546"])]),
 (90, "conteudo", "Corpos cetônicos: formação e uso", [
   ("formacao", "Formação no fígado (acetoacetato, β-hidroxibutirato, acetona; HMG-CoA sintase)", ["tres-cetonas", "hmg-sintase", "acetona-pulmao"]),
   ("uso", "Aproveitamento nos músculos e coração: acetoacetil-CoA, Krebs", ["bhb-extra-hepatico", "tioforase", "cetonas-tecidos"]),
   ("porque", "Oxaloacetato desviado para gliconeogênese: acetil-CoA vira corpos cetônicos", "cetogenese-oaa")]),
 (91, "conteudo", "Pós-absortivo (jejum): figura de integração", [("fig", "Alanina, lactato, glicerol e corpos cetônicos entre tecidos", ["sh-1791647351570", "alanina-musculo", "tres-cetonas"])]),
 (92, "conteudo", "Diabetes mellitus: definição", [("def", "Grupo de doenças metabólicas com hiperglicemia por defeito de secreção, ação ou ambos; tipos 1 e 2", "sh-1791054010222")]),
 (93, "conteudo", "DM1 × DM2: perfil", [
   ("idade", "DM1 <20 anos, magro; DM2 >40 anos, obeso", ["t1-idade", "t2-idade"]),
   ("def", "DM1 deficiência absoluta; DM2 relativa + resistência", "t1-absoluta"),
   ("sintomas", "DM1: polidipsia, poliúria, polifagia, emagrecimento", "t1-sintomas"),
   ("insidioso", "DM2: início insidioso, às vezes assintomático", "t2-insidioso"),
   ("descomp", "DM1 descompensa em cetoacidose; DM2 em coma hiperosmolar", ["sh-1791054010747", "sh-1791054010873"]),
   ("hla", "Herança do DM1 associada ao HLA; DM2 poligênica", ["t1-hla", "t1-hla"])]),
 (94, "conteudo", "DM1: células β e tratamento", [
   ("auto", "Deficiência das células β por reação autoimune", "sh-1791054010997"),
   ("trat", "Requer insulina diária, dieta e exercícios; sobrevida reduzida por complicações; ajuste da dose", "t1-tratamento")]),
 (95, "conteudo", "DM1 semelhante ao jejum", [
   ("jejum", "Sem inibição da síntese de glucagon: hiperglucagonemia agrava a hiperglicemia", ["sh-1791054011545", "t1-jejum"]),
   ("razao", "Razão insulina/glucagon baixa: gliconeogênese, lipólise, proteólise, corpos cetônicos", ["t1-jejum", "sh-1791054011671"]),
   ("cetoac", "Cetoacidose, balanço nitrogenado negativo, carência celular de glicose e aminoácidos", ["sh-1791054011671", "balanco-n-negativo"]),
   ("osm", "Hiperglicemia: hiperosmolaridade e sobrecarga renal", "sh-1791054012320"),
   ("glic", "Proteínas glicadas têm a atividade prejudicada", ["sh-1791054015196", "glicacao-funcao"])]),
 (96, "conteudo", "DM2: características", [
   ("res", "Resistência à insulina e secreção perturbada", ["t1-absoluta", "t2-triangulo"]),
   ("pct", ">90% dos casos, obesos", ["t2-idade", "t2-noventa"]),
   ("pred", "Predisposição genética", "t1-hla"),
   ("niveis", "Insulina normal ou elevada, sem resposta", "t2-insulina-normal")]),
 (97, "conteudo", "DM2: captação e células β", [
   ("capt", "Inibição da entrada de glicose no músculo e adiposo", "t2-captacao"),
   ("glicemia", "A glicemia estimula a secreção, mas os níveis seguem altos", "t2-resistencia-antes"),
   ("falencia", "Estimulação crônica leva à falência e à secreção deficiente", ["t2-falencia", "sh-1791054012719"]),
   ("sm", "Síndrome metabólica: obesidade, LDL ↑, HDL ↓, hipertensão", ["t2-sindrome-metabolica", "sh-1791054012847"])]),
 (98, "conteudo", "Defeitos metabólicos no DM2", [("tri", "Resistência à insulina, secreção deficiente, produção hepática ↑, captação ↓", "t2-triangulo")]),
 (99, "conteudo", "DM2 desenvolve-se com o tempo", [
   ("antes", "Resistência vários anos antes de a insulina sérica subir; compensação", "t2-resistencia-antes"),
   ("dificuldade", "Dificuldade do pâncreas leva ao aumento da glicose", "t2-falencia")]),
 (100, "conteudo", "Tratamento do DM2", [
   ("dieta", "Dieta e exercício no começo", "t2-dieta"),
   ("oral", "Antidiabéticos: ↓ produção hepática, ↑ captação, ↑ secreção, retardam digestão", ["sh-1791054013770", "sh-1791054013895", "sh-1791054014146", "sh-1791054014320", "sh-1791054014020"])]),
 (101, "video", "Link de vídeo", []),
 (102, "capa", "Referências", []),
]
JUSTIFICATIVAS = {"capa": "capa ou referências, sem conteúdo", "video": "link para vídeo do YouTube, dispensado por Davi (F-20261010-CLAUDE-06)"}

CAPITULO = [("Lehninger, cap. 23 — jejum, cetogênese e diabetes", [
   ("lh-oaa", "Oxaloacetato depletado pela gliconeogênese: acetil-CoA se acumula e forma corpos cetônicos", "cetogenese-oaa"),
   ("lh-acetilcoa", "Acetil-CoA inibe a PDH e estimula a piruvato carboxilase", ["pdk4-acetilcoa", "pc-acetilcoa"]),
   ("lh-reserva", "Reservas de combustível e sobrevivência", "reservas-tag"),
   ("lh-dm", "DM1 por destruição autoimune; DM2 por resistência; glicosúria, poliúria, polidipsia", ["t1-absoluta", "sh-1791054012320"]),
   ("lh-cetoacidose", "Superprodução de corpos cetônicos leva à cetoacidose no diabetes não controlado", ["sh-1791054011671", "tres-cetonas"])])]

EXERCICIOS = [
 ("Provas UC03 (índice biomol-06)", [
   ("p2025", "2025 P2 1.8: jejum relativo inflamatório (citocinas, glicogenólise, gliconeogênese, proteólise, resistência à insulina)", ["jejum-inflamatorio", "cortisol-proteolise", "alanina-musculo"]),
   ("p2024", "2024 P2 1.3: jejum prolongado por tecido (glucagon, PKA, GLUT4, cetonas, proteólise)", ["glut4-jejum", "cetonas-poupam", "cetonas-tecidos", "sh-1791647349571"]),
   ("p2023", "2023 P1 2.2: inibir a captação de glicerol no fígado no DM2", ["glicerol-quinase", "metformina-gpdh", "sh-1791647350421"])]),
 ("Guia de veteranos, aula 7", [
   ("vet-fases", "Fases do jejum e perfil de integração pós-prandial/jejum", ["sh-1791647354421", "sh-1791647354545", "sh-1791647354671", "cetonas-tecidos"]),
   ("vet-secrecao", "Secreção de insulina: GLUT2, ATP, K⁺, Ca²⁺, exocitose", ["katp-fecha", "katp-calcio", "katp-exocitose"]),
   ("vet-gsk3", "GSK3, PP1 e PKA na glicogênese", ["pkb-gsk3", "sh-1791647349819"]),
   ("vet-lipideos", "Citrato, malonil-CoA, CAT I e NADPH", ["citrato-citosol", "malonil-cat1", "g6pd-insulina"]),
   ("vet-glicerol", "Glicerol: glicerol-quinase e glicerol-3-fosfato desidrogenase", "glicerol-quinase"),
   ("vet-aa", "Alanina e glutamina; glicogênicos e cetogênicos; balanço nitrogenado", ["aa-alanina-glutamina", "gln-rim", "balanco-n-negativo", "cetogenicos"]),
   ("vet-dm", "DM: resistência, falência β, cetoacidose, hiperosmolaridade e glicação", ["t2-falencia", "t1-jejum", "sh-1791054015196"]),])
]
