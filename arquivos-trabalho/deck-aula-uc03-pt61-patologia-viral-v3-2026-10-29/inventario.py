"""Inventário atômico da 61 Patologia da infecção viral v3 (UC03 P3; Patologia; Prof. Luiz Fernando Ferraz da Silva; 29 lâminas), escrito
em 29/10 (refação v10, F-20261029-CLAUDE-03) a partir do material relido: lâminas em visual/folha-01..05, transcrição, UC3.pdf com os
objetivos oficiais, monitoria e apostila guia, provas 2016–2024, Robbins cap. 8 (injúria viral; reação citopática-citoproliferativa).
Lâminas 2–13 são o núcleo; 14–29 são o exemplo da hepatite ("a combinação de tudo") e só entram pelo princípio que ilustram.
Destinos (D) finais preenchidos depois da busca (E4) a partir do spec.
"""
PREFIXO = "pt61"
AULA = "Patologia da infecção viral (UC03 P3; Patologia; Prof. Luiz Fernando Ferraz da Silva)"
EXC = "EXC: "
_C = "conteudo"
_E = "conteudo"  # inventario só conhece capa|conteudo; o papel de exemplo está em compreensao-aula.json
D = {"2a": ["sh-1792695023262", "sh-1792753616942"], "2b": ["sh-1792695023262"], "3a": ["au-efeitos"], "4a": ["au-efeitos"], "4b": ["au-efeitos"], "4c": ["au-transformacao"], "4d": ["au-sequestro"], "4e": ["au-efeitos"], "5a": ["au-inclusao"], "5b": ["sh-1793199693557"], "6a": ["au-raiva-sarampo", "sh-1793199689045", "sh-1793199695431"], "6b": ["sh-1793199691630"], "7a": ["sh-1793199689805", "ak1506457588894", "sh-1793199692380"], "7b": ["au-sincicio-granuloma"], "8a": ["sh-1793199694409"], "8b": ["ak1405375421095"], "9a": ["au-quadros", "sh-1791625429957"], "9b": ["au-nk-neutrofilo"], "9c": ["au-complemento"], "9d": ["sh-1791625430882"], "9e": ["au-mononuclear"], "10a": ["au-curva"], "10b": ["au-intracelular"], "10c": ["au-ifn-tipo"], "11a": ["sh-1793053714022", "sh-1792240189143"], "11b": ["au-ifn-tempo"], "12a": ["sh-1793053714276", "sh-1793053714152"], "12b": ["sh-1793053714397"], "13a": ["sh-1793054287147", "ak1503876156644", "sh-1792242117388"], "13b": ["sh-1793053714521"], "13c": ["au-nk-cd8"], "14a": ["au-aguda-matriz"], "16a": ["au-vidro-fosco", "ak1715273523479"], "17a": ["au-ihq"], "18a": ["au-ihq"], "18c": ["au-anti-hbc"], "18d": ["au-anti-hbc"], "19a": ["au-mononuclear"], "20a": ["au-periportal", "ak1486776378880"], "21a": ["sh-1792753612016", "sh-1792117361820"], "22a": ["au-necrose-matriz"], "23a": ["au-necrose-matriz"], "24a": ["au-apoptose-necrose"], "25a": ["au-interface"], "26a": ["au-cd8-b"], "27a": ["au-cd8-b"], "28a": ["au-colageno"], "29a": ["sh-1791022172624"], "l1": ["sh-1792695023262"], "l2": ["sh-1793199689805"], "l3": ["au-mononuclear"], "p1": ["au-inclusao"], "p2": ["au-sincicio-granuloma"], "p3": ["ak1405375421095"], "p4": ["au-ifn-tempo"], "o1": ["au-efeitos"], "o2": ["au-quadros"], "m1": ["sh-1793199691630"], "a1": ["sh-1793054287147"]}

SLIDES = [
 (1, "capa", "Capa", []),
 (2, _C, "Dois aspectos: biologia do vírus e resposta", [("a", "Lesão = efeito direto + efeito da resposta", D.get("2a", "")), ("b", "Onde o vírus replica decide a cara da lesão", D.get("2b", ""))]),
 (3, _C, "Sete efeitos diretos", [("a", "Lise, apoptose, síntese, sincícios, citoesqueleto, ciclo, transformação", D.get("3a", ""))]),
 (4, _C, "Três destinos dos efeitos diretos",
  [("a", "Lise libera DAMP → inflamação aguda", D.get("4a", "")), ("b", "Bloqueio de síntese, sincícios, citoesqueleto, ciclo → efeito citopático", D.get("4b", "")),
   ("c", "Transformação (genoma perto de gene do ciclo) → neoplasia", D.get("4c", "")), ("d", "Síntese sequestrada: célula para de fazer suas proteínas e de dividir", D.get("4d", "")),
   ("e", "Apoptose pelo vírus ou pela resposta", D.get("4e", ""))]),
 (5, _C, "Inclusão citoplasmática: raiva", [("a", "Inclusão = acúmulo desproporcional; montagem para no que falta", D.get("5a", "")), ("b", "Citoplasmática eosinofílica na raiva", D.get("5b", ""))]),
 (6, _C, "Inclusão nuclear: sarampo", [("a", "Inclusão nuclear no sarampo", D.get("6a", "")), ("b", "Inclusões nucleares do material: Cowdry A, olho de coruja", D.get("6b", ""))]),
 (7, _C, "Sincícios: VSR", [("a", "Fusão de células infectadas, também epiteliais", D.get("7a", "")), ("b", "Sincício × célula gigante de granuloma", D.get("7b", ""))]),
 (8, _C, "Coilocitose: HPV", [("a", "Coilócito: halo perinuclear", D.get("8a", "")), ("b", "Tipo oncogênico, seguimento", D.get("8b", ""))]),
 (9, _C, "Resposta: agudo inata × crônico adaptativa",
  [("a", "Agudo: barreiras, NK e macrófagos, complemento; crônico: T, B, anticorpos", D.get("9a", "")), ("b", "NK na virose como neutrófilo na bacteriana", D.get("9b", "")),
   ("c", "Complemento: neutraliza e lisa célula infectada", D.get("9c", "")), ("d", "CD8 Fas-FasL é o principal; TNF no agudo", D.get("9d", "")),
   ("e", "Infiltrado mononuclear na virose persistente", D.get("9e", ""))]),
 (10, _C, "Curva: IFN-I e NK → T → anticorpos", [("a", "Curva temporal", D.get("10a", "")), ("b", "Inata não basta: vírus intracelular", D.get("10b", "")), ("c", "IFN-I, não IFN-γ", D.get("10c", ""))]),
 (11, _C, "Interferon: efeito parácrino", [("a", "IFN-I age nas vizinhas, proteína antiviral", D.get("11a", "")), ("b", "Bloqueia replicação e ganha tempo", D.get("11b", ""))]),
 (12, _C, "Interferon: MHC I, NK, macrófagos; estado antiviral", [("a", "IFN sobe MHC I", D.get("12a", "")), ("b", "IFN ativa NK e macrófagos", D.get("12b", ""))]),
 (13, _C, "Célula NK", [("a", "NK mata célula sem MHC I", D.get("13a", "")), ("b", "Perforina e granzima", D.get("13b", "")), ("c", "CD8 × NK quando o vírus esconde MHC I", D.get("13c", ""))]),
 (14, _E, "Exemplo: hepatite A × crônicas; estrutura do HBV", [("a", "Aguda que poupa a matriz regenera", D.get("14a", "")), ("b", "HBsAg, HBcAg, HBeAg", "EXC: estrutura do HBV entra só no verso dos cards de imuno-histoquímica e sorologia")]),
 (15, _E, "Exemplo: ciclo do HBV", [("a", "Core no núcleo, HBsAg no RE/Golgi", "EXC: ciclo do HBV é da 58; aqui só explica onde cada antígeno aparece (verso do card de imuno-histoquímica)")]),
 (16, _E, "Exemplo: vidro fosco", [("a", "Proteína de superfície acumulada no citoplasma", D.get("16a", ""))]),
 (17, _E, "Exemplo: imuno-histoquímica HBsAg", [("a", "Antígeno no citoplasma; ocupa a maquinaria", D.get("17a", ""))]),
 (18, _E, "Exemplo: imuno-histoquímica HBcAg; sorologia",
  [("a", "HBcAg no núcleo", D.get("18a", "")), ("b", "HCV → esteatose", "EXC: mecanismo da doença do exemplo, sem princípio próprio além do sequestro da maquinaria (lâmina 4)"),
   ("c", "Anti-HBs × anti-HBc", D.get("18c", "")), ("d", "HBeAg = replicação", D.get("18d", ""))]),
 (19, _E, "Exemplo: infiltrado crônico portal", [("a", "Espaço porta expandido por linfócitos", D.get("19a", ""))]),
 (20, _E, "Exemplo: zonas do lóbulo", [("a", "Periportal (zona 1) × metabólica (zona 3)", D.get("20a", ""))]),
 (21, _E, "Exemplo: necrose por linfócitos", [("a", "Célula mononuclear mata a infectada", D.get("21a", ""))]),
 (22, _E, "Exemplo: necrose → neutrófilo → matriz", [("a", "Necrose destrói a matriz e impede a regeneração", D.get("22a", ""))]),
 (23, _E, "Exemplo: necrose extensa", [("a", "Lesões grandes", D.get("23a", ""))]),
 (24, _E, "Exemplo: apoptose", [("a", "Apoptose pelo vírus ou por estímulo linfocitário", D.get("24a", ""))]),
 (25, _E, "Exemplo: atividade de interface", [("a", "Destruição em curso = atividade", D.get("25a", ""))]),
 (26, _E, "Exemplo: linfócitos B", [("a", "B para neutralizar vírus liberado", D.get("26a", ""))]),
 (27, _E, "Exemplo: T CD8", [("a", "CD8 citotóxico", D.get("27a", ""))]),
 (28, _E, "Exemplo: alteração arquitetural", [("a", "Reticulina → colágeno → septos → nódulos", D.get("28a", ""))]),
 (29, _E, "Exemplo: cirrose (Masson)", [("a", "Cirrose estabelecida", D.get("29a", ""))]),
]
JUSTIFICATIVAS = {}
CAPITULO = [("Robbins cap. 8: injúria viral (pp. 343–345) e reação citopática-citoproliferativa (p. 348)", [
 ("l1", "Três mecanismos de lesão; resposta como faca de dois gumes; no HBV/HCV o dano é sobretudo pela resposta", D.get("l1", "")),
 ("l2", "Corpos de inclusão (herpes, adenovírus), policárions (sarampo, herpes), proliferação (HPV)", D.get("l2", "")),
 ("l3", "Infiltrado de linfócitos em infecção pelo HBV e viroses do cérebro", D.get("l3", ""))])]
EXERCICIOS = [
 ("Provas UC03 (busca por termo)", [
  ("p1", "Inclusão por subunidades desproporcionais (2024 P3 1.2)", D.get("p1", "")),
  ("p2", "Sincício × célula gigante de granuloma (2017 P3 1.3)", D.get("p2", "")),
  ("p3", "Coilocitose e HPV 16 (2016 P3 1.2)", D.get("p3", "")),
  ("p4", "Como o vírus dispara a resposta e as repercussões (2018 P3 1.7)", D.get("p4", ""))]),
 ("Objetivos oficiais (UC3.pdf)", [("o1", "Citar 3 efeitos citopáticos explicando a formação", D.get("o1", "")), ("o2", "Elementos inflamatórios da resposta viral", D.get("o2", ""))]),
 ("Monitoria P3 de Patologia, aula 9", [("m1", "Efeito citopático, Cowdry, resposta inata × adaptativa", D.get("m1", ""))]),
 ("Apostila guia de Patologia, aula 10", [("a1", "Efeitos, IFN-I, NK, HBV", D.get("a1", ""))])]
