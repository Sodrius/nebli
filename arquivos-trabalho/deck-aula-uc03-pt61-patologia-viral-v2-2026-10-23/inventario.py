"""Inventário atômico da 61 Patologia da infecção viral (UC03 P3; Patologia; Prof. Luiz Fernando Ferraz da Silva; 29 lâminas), escrito em
23/10 (refação v7) a partir do material lido: lâminas vistas em visual/folha-01..05, transcrição inteira (anotações do PDF), provas por
termo, monitoria e apostila guia (conferência), Robbins caps. 8 e 18. Blocos e papéis: compreensao-aula.json. Destinos preenchidos
depois da busca (E4).
"""
PREFIXO = "pt61"
AULA = "Patologia da infecção viral (UC03 P3; Patologia; Prof. Luiz Fernando Ferraz da Silva)"
EXC = "EXC: "
_C = "conteudo"
D = {"2a": "au-dois-efeitos", "3a": "au-efeitos", "4a": "au-efeitos", "4b": "au-efeitos", "4c": "au-efeitos", "4d": "au-sequestro", "5a": ["au-inclusao", "sh-1792695054492"], "5b": ["ak1516474665512", "au-raiva-sarampo"], "6a": "au-raiva-sarampo", "7a": "ak1506457588894", "7b": "au-sincicio-granuloma", "8a": "ak1385335604751", "8b": "ak1385335604751", "9a": ["sh-1792753615215", "au-intracelular"], "9b": "au-complemento", "9c": "sh-1791625429957", "10a": ["au-curva", "au-complemento"], "10b": "au-intracelular", "11a": "ak1489970693302", "11b": ["au-ifn-tempo", "ak1520301328706"], "12a": "ak1520301453074", "12b": ["ak1487117310594", "ak1520301453074"], "13a": "ak1487117314403", "13b": ["ak1487117308213", "sh-1792242117388"], "14a": "au-hbv-antigenos", "14b": "au-hav", "15a": "au-ihq", "16a": ["ak1715273523479", "au-vidro-fosco"], "17a": "au-ihq", "18a": "au-ihq", "18b": "au-hcv-esteatose", "18c": ["au-anti-hbc", "ak1521044225681", "ak1502066053913"], "18d": "ak1521044306629", "19a": "ak1486522630094", "20a": ["au-periportal", "ak1486776378880"], "21a": "sh-1791625429957", "22a": ["au-necrose-matriz", "au-apoptose-necrose"], "23a": "au-apoptose-necrose", "24a": "sh-1792117361820", "25a": "au-interface", "26a": "au-linf-b", "27a": "sh-1791625429957", "28a": ["au-colageno", "ak1468250259504", "sh-1791022173275"], "29a": ["sh-1791022172624", "au-masson"], "l1": "au-dois-efeitos", "l2": "au-vidro-fosco", "l3": "ak1521044306629", "p1": "au-inclusao", "p2": "au-sincicio-granuloma", "p3": "ak1385335604751", "p4": "ak1489970693302", "m1": "au-efeitos", "a1": "ak1487117314403"}  # ideia → chave do card (preenchido depois da busca, 23/10)

SLIDES = [
 (1, "capa", "Capa", []),
 (2, _C, "Dois efeitos: o do vírus e o da resposta", [("a", "Lesão viral = efeito do vírus + efeito da resposta", D.get("2a", ""))]),
 (3, _C, "Efeitos do vírus sobre a célula (lista)", [("a", "Sete efeitos diretos", D.get("3a", ""))]),
 (4, _C, "Lise → inflamação aguda; efeito citopático; transformação → neoplasia",
  [("a", "Lise libera DAMP e dá inflamação aguda", D.get("4a", "")), ("b", "Efeito citopático = alterações morfológicas", D.get("4b", "")),
   ("c", "Transformação → neoplasia", D.get("4c", "")), ("d", "Síntese sequestrada; ciclo parado", D.get("4d", ""))]),
 (5, _C, "Inclusão citoplasmática: raiva", [("a", "Inclusão = acúmulo desproporcional", D.get("5a", "")), ("b", "Citoplasmática eosinofílica na raiva", D.get("5b", ""))]),
 (6, _C, "Inclusão nuclear: sarampo", [("a", "Inclusão nuclear no sarampo", D.get("6a", ""))]),
 (7, _C, "Sincícios: VSR", [("a", "Sincício por fusão de células infectadas", D.get("7a", "")), ("b", "Sincício × célula gigante de granuloma", D.get("7b", ""))]),
 (8, _C, "Coilocitose: HPV", [("a", "Coilócito: halo perinuclear", D.get("8a", "")), ("b", "Coilocitose indica HPV e seguimento", D.get("8b", ""))]),
 (9, _C, "Resposta: agudo inata × crônico adaptativa",
  [("a", "Agudo: inata; crônico: adaptativa", D.get("9a", "")), ("b", "Complemento: neutraliza e lisa célula infectada", D.get("9b", "")),
   ("c", "Apoptose por TNF/FAS na resposta", D.get("9c", ""))]),
 (10, _C, "Curva da resposta: IFN-I e NK → T → anticorpos", [("a", "Curva temporal", D.get("10a", "")), ("b", "Inata não basta: vírus intracelular", D.get("10b", ""))]),
 (11, _C, "Interferon: efeito parácrino, proteínas antivirais", [("a", "IFN-I age nas vizinhas", D.get("11a", "")), ("b", "Bloqueia replicação e ganha tempo", D.get("11b", ""))]),
 (12, _C, "Interferon: MHC I, NK, macrófagos; estado antiviral", [("a", "IFN sobe MHC I", D.get("12a", "")), ("b", "IFN ativa NK e macrófagos", D.get("12b", ""))]),
 (13, _C, "Célula NK", [("a", "NK mata célula sem MHC I", D.get("13a", "")), ("b", "Perforina e granzima", D.get("13b", ""))]),
 (14, _C, "HBV: estrutura e antígenos", [("a", "HBsAg, HBcAg, HBeAg", D.get("14a", "")), ("b", "HAV aguda preserva reticulina × B/C crônicas", D.get("14b", ""))]),
 (15, _C, "HBV: ciclo", [("a", "Core no núcleo, HBsAg no RE/Golgi", D.get("15a", ""))]),
 (16, _C, "Efeito citopático: hepatócito em vidro fosco", [("a", "Vidro fosco = HBsAg acumulado", D.get("16a", ""))]),
 (17, _C, "Imuno-histoquímica: HBsAg", [("a", "HBsAg no citoplasma", D.get("17a", ""))]),
 (18, _C, "Imuno-histoquímica: HBcAg; HCV e esteatose; sorologia",
  [("a", "HBcAg no núcleo", D.get("18a", "")), ("b", "HCV → esteatose", D.get("18b", "")), ("c", "Anti-HBs × anti-HBc", D.get("18c", "")), ("d", "HBeAg = replicação", D.get("18d", ""))]),
 (19, _C, "Infiltrado inflamatório crônico portal", [("a", "Espaço porta expandido por linfócitos", D.get("19a", ""))]),
 (20, _C, "Fígado normal: zonas", [("a", "Periportal (zona 1) × metabólica (zona 3)", D.get("20a", ""))]),
 (21, _C, "Necrose hepatocitária", [("a", "CTL mata hepatócito", D.get("21a", ""))]),
 (22, _C, "Necrose → neutrófilo → matriz", [("a", "Necrose destrói a matriz e impede a regeneração", D.get("22a", ""))]),
 (23, _C, "Necrose extensa", [("a", "Lesões grandes", D.get("23a", ""))]),
 (24, _C, "Apoptose do hepatócito", [("a", "Hepatócito apoptótico", D.get("24a", ""))]),
 (25, _C, "Distribuição: interface", [("a", "Atividade de interface = tratar", D.get("25a", ""))]),
 (26, _C, "Infiltrado: linfócitos B", [("a", "B para neutralizar vírus liberado", D.get("26a", ""))]),
 (27, _C, "Infiltrado: T CD8", [("a", "CD8 citotóxico", D.get("27a", ""))]),
 (28, _C, "Alteração arquitetural: septos", [("a", "Reticulina → colágeno → septos → nódulos", D.get("28a", ""))]),
 (29, _C, "Cirrose (Masson)", [("a", "Cirrose estabelecida; Masson azul", D.get("29a", ""))]),
]
JUSTIFICATIVAS = {}
CAPITULO = [("Robbins cap. 8 (mecanismos de injúria viral) e cap. 18 (hepatite viral)", [
 ("l1", "Três mecanismos de lesão; o do HBV/HCV é pela resposta", D.get("l1", "")),
 ("l2", "Vidro despolido por HBsAg; esteatose no HCV; hepatite de interface", D.get("l2", "")),
 ("l3", "HBeAg = replicação; anti-HBc", D.get("l3", ""))])]
EXERCICIOS = [
 ("Provas UC03 (busca por termo)", [
  ("p1", "Inclusão por subunidades desproporcionais (2024 P3 1.2)", D.get("p1", "")),
  ("p2", "Sincício × célula gigante de granuloma (2017 P3 1.3)", D.get("p2", "")),
  ("p3", "Coilocitose e HPV 16 (2016 P3 1.2)", D.get("p3", "")),
  ("p4", "Como o vírus dispara a resposta e as repercussões (2018 P3 1.7)", D.get("p4", ""))]),
 ("Monitoria P3 de Patologia, aula 9", [("m1", "Efeito citopático, resposta inata × adaptativa, vidro despolido", D.get("m1", ""))]),
 ("Apostila guia de Patologia, aula 10", [("a1", "Efeitos, IFN-I, NK, HBV", D.get("a1", ""))])]
