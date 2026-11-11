"""Planejamento E3 da aula 04 (UC07 Anatomia): itens do mapa → chaves de card, na ordem do percurso (unidades 1–62).
id-* = identificação visual (Kenhub primeiro); sh-* = nota viva da Anatomia 01 associada; demais chaves = relação/fato/organizador.
Fonte concreta é decidida na E4/E5 (curadoria.py). Gera mapa-de-profundidade.json, inventário, motivacoes.json e escopo.json por gerar_e3.py."""

T1, T2, T3, T4, AP, MAC, VET = "T1 diencéfalo", "T2 telencéfalo", "T3 irrigação", "T4 prática", "apostila-guia", "Machado", "veteranos"

# (unidade, id_item, tipo, o_que, fonte, termos, [chaves])
ITENS = [
 # ---------- DIENCÉFALO ----------
 (1, "u01-cerebro", "organizar", "Situar o diencéfalo no cérebro: cérebro = telencéfalo + diencéfalo; diencéfalo é a parte menor", f"{T1} min 00-03; {MAC} cap6 §1", ["diencéfalo"], ["sh-cerebro-partes", "sh-id-diencefalo", "sh-id-cerebro"]),
 (2, "u02-escondido", "explicar", "Explicar por que o diencéfalo só aparece na vista medial: o telencéfalo cresce e o esconde", f"{T1} min 03-05; {MAC} cap6 §1", ["escondido"], ["diencefalo-escondido"]),
 (3, "u03-partes", "organizar", "Nomear as quatro partes do diencéfalo e o metatálamo como opção de alguns autores", f"{T1} min 06-08; {AP} Aula 4 cap1", ["metatálamo"], ["diencefalo-partes-org", "metatalamo"]),
 (4, "u04-vizinhos", "decorar", "Situar o ventrículo lateral e o corpo caloso acima do diencéfalo na vista medial", f"{T1} min 08-09", ["ventrículo lateral"], ["sh-id-ventriculo-lateral", "sh-id-corpo-caloso"]),
 (5, "u05-sulco", "distinguir", "Usar o sulco hipotalâmico para separar tálamo (acima) de hipotálamo (abaixo); epitálamo atrás; subtálamo lateral e invisível", f"{T1} min 09-11; {MAC} cap6 §2", ["sulco hipotalâmico"], ["sulco-hipotalamico", "id-sulco-hipotalamico", "sh-id-talamo", "sh-id-hipotalamo", "id-epitalamo", "subtalamo-invisivel"]),
 (6, "u06-aderencia", "decorar", "Reconhecer a aderência intertalâmica unindo os tálamos através do III ventrículo", f"{T1} min 11-13; {MAC} cap6 §2", ["aderência intertalâmica"], ["aderencia-intertalamica", "id-aderencia-intertalamica"]),
 (7, "u07-divisao-talamo", "organizar", "Dividir o tálamo em tubérculo anterior, pulvinar e corpos geniculados (posteriores)", f"{T1} min 13-17; {MAC} cap6 §3", ["pulvinar"], ["talamo-divisao", "id-tuberculo-anterior", "id-pulvinar", "id-geniculado-medial", "id-geniculado-lateral"]),
 (8, "u08-limites-talamo", "organizar", "Dar os limites do tálamo: ventrículo lateral acima, III ventrículo medial, cápsula interna lateral, hipotálamo e subtálamo abaixo", f"{T1} min 18-26; {VET} p13; GaKa aula 4", ["cápsula interna"], ["talamo-limites-org", "sh-id-capsula-interna", "id-terceiro-ventriculo"]),
 (9, "u09-nucleo-ganglio", "distinguir", "Distinguir núcleo (corpos celulares no SNC) de gânglio (fora); o tálamo é substância cinzenta", f"{T1} min 26-27", ["núcleo"], ["nucleo-x-ganglio", "talamo-cinzento"]),
 (10, "u10-anteriores", "decorar", "Ligar os núcleos anteriores do tálamo ao sistema límbico", f"{T1} min 29-30", ["sistema límbico"], ["talamo-nucleos-org", "id-nucleos-anteriores-talamo"]),
 (11, "u11-geniculados", "distinguir", "Distinguir geniculado lateral (visão, mais alto como o olho) de medial (audição, mais baixo como a orelha)", f"{T1} min 30-32; {MAC} cap6 §3", ["geniculado"], ["geniculados-funcao"]),
 (12, "u12-lat-med", "organizar", "Ligar núcleos laterais à motricidade e sensibilidade, mediais ao límbico e medianos a função pouco conhecida", f"{T1} min 32-34", ["núcleos laterais"], ["talamo-nucleos-org", "id-nucleos-laterais-talamo", "id-nucleo-medial-dorsal", "id-nucleos-medianos-talamo"]),
 (13, "u13-limites-hipo", "organizar", "Dar os limites do hipotálamo: tálamo acima, subtálamo lateral, III ventrículo medial", f"{T1} min 35-37; {VET} p15", ["hipotálamo"], ["hipotalamo-limites"]),
 (14, "u14-assoalho", "organizar", "Ordenar o limite inferior do hipotálamo: quiasma óptico, túber cinéreo + infundíbulo, corpos mamilares", f"{T1} min 37-43; {MAC} cap6 §4", ["túber cinéreo"], ["assoalho-hipotalamo-org", "id-quiasma-optico", "id-tuber-cinereo", "id-infundibulo", "id-corpo-mamilar", "infundibulo-hipofise", "id-hipofise", "comissura-anterior-nao-limite", "id-comissura-anterior"]),
 (15, "u15-regioes", "explicar", "Explicar os nomes das regiões do hipotálamo pela estrutura do assoalho abaixo de cada uma", f"{T1} min 43-46; {VET} p15", ["tuberal"], ["hipotalamo-regioes-org"]),
 (16, "u16-nucleos-hipo", "organizar", "Pôr cada núcleo do hipotálamo na sua região (supraóptica, tuberal, mamilar)", f"{T1} min 46-50; {VET} p15", ["supraquiasmático"], ["hipotalamo-nucleos-org", "id-nucleo-supraoptico", "id-nucleo-supraquiasmatico", "id-nucleo-paraventricular", "id-nucleo-ventromedial", "id-nucleo-dorsomedial", "supraquiasmatico-ritmo", "supraoptico-adh"]),
 (17, "u17-epitalamo", "decorar", "Situar o epitálamo na parte posterior do diencéfalo", f"{T1} min 50-52; {MAC} cap6 §5", ["epitálamo"], ["epitalamo-posicao"]),
 (18, "u18-epitalamo-estr", "organizar", "Reconhecer as estruturas do epitálamo: corpo pineal, habênula (núcleo e comissura, límbicos), comissura posterior", f"{T1} min 52-54; {MAC} cap6 §5", ["pineal"], ["epitalamo-org", "id-glandula-pineal", "id-comissura-habenular", "id-comissura-posterior", "pineal-melatonina"]),
 (19, "u19-subtalamo", "organizar", "Dar os limites do subtálamo: tálamo acima, mesencéfalo abaixo, hipotálamo medial, cápsula interna lateral", f"{T1} min 54-57; {MAC} cap6 §6", ["subtálamo"], ["subtalamo-limites", "id-subtalamo"]),
 (20, "u20-subtalamico", "e-se", "Ligar o núcleo subtalâmico à motricidade e prever o hemibalismo na lesão", f"{T1} min 57-58; {MAC} cap6 §6", ["núcleo subtalâmico"], ["subtalamico-motor", "id-nucleo-subtalamico", "hemibalismo"]),
 (21, "u21-septo", "decorar", "Reconhecer o septo pelúcido separando os ventrículos laterais, entre o corpo caloso e o fórnix", f"{T1} min 63-69; {MAC} cap7 §3.2.1", ["septo pelúcido"], ["septo-pelucido", "id-septo-pelucido", "id-fornix"]),
 # ---------- TELENCÉFALO ----------
 (23, "u23-faces", "organizar", "Nomear as três faces do hemisfério (superolateral, medial, inferior) e como se veem", f"{T2} min 02-05; {MAC} cap7 §1", ["face superolateral"], ["faces-hemisferio"]),
 (24, "u24-giros", "distinguir", "Distinguir giro (saliência) de sulco (depressão)", f"{T2} min 06-07", ["giros"], ["giro-x-sulco"]),
 (25, "u25-tres-sulcos", "decorar", "Reconhecer os sulcos lateral (Sylvius), central (Rolando) e semilunar (inconstante)", f"{T2} min 07-10; {MAC} cap7 §2", ["Rolando"], ["sulcos-eponimos", "id-sulco-lateral", "sh-id-sulco-central"]),
 (26, "u26-lobos", "organizar", "Delimitar os lobos frontal, parietal, occipital e temporal pelos sulcos e ossos", f"{T2} min 10-11; {T4} min 22-24", ["lobo"], ["lobos-limites-org", "sh-id-lobo-frontal", "sh-id-lobo-parietal", "sh-id-lobo-occipital", "sh-id-lobo-temporal"]),
 (27, "u27-central", "decorar", "Reconhecer o sulco central como limite frontal-parietal; termina habitualmente antes do sulco lateral", f"{T2} min 11-12; {MAC} cap7 §2", ["ponta a ponta"], ["sulco-central-unico"]),
 (28, "u28-pre-central", "decorar", "Situar o giro pré-central entre os sulcos pré-central e central como principal área motora", f"{T2} min 12-13; {MAC} cap7 §3.1.1", ["giro pré-central"], ["pre-central-motor", "id-giro-pre-central"]),
 (29, "u29-frontais", "organizar", "Nomear os giros frontais superior, médio e inferior pelos sulcos frontais superior e inferior", f"{T2} min 14-16", ["giro frontal médio"], ["frontais-org", "id-giro-frontal-superior", "id-giro-frontal-medio", "id-giro-frontal-inferior", "id-sulco-frontal-superior", "id-sulco-frontal-inferior"]),
 (30, "u30-broca", "e-se", "Dividir o giro frontal inferior em partes orbital, triangular e opercular e ligar o esquerdo à área de Broca (articulação da palavra)", f"{T2} min 16-21; {MAC} cap7 §3.1.1", ["Broca"], ["frontal-inferior-partes", "id-parte-triangular", "broca-giro", "sh-broca-local", "sh-broca-afasia"]),
 (31, "u31-pos-central", "decorar", "Situar o giro pós-central entre os sulcos central e pós-central como área somestésica", f"{T2} min 21-23; {MAC} cap7 §3.1.3", ["giro pós-central"], ["pos-central-somestesica", "id-giro-pos-central", "id-sulco-pos-central"]),
 (32, "u32-parietal", "organizar", "Dividir o lobo parietal pelo sulco intraparietal em lóbulos superior e inferior; giros supramarginal e angular no inferior", f"{T2} min 23-28; {MAC} cap7 §3.1.3", ["sulco intraparietal"], ["parietal-org", "id-sulco-intraparietal", "id-lobulo-parietal-superior", "id-lobulo-parietal-inferior", "id-giro-supramarginal", "id-giro-angular", "lobulo-definicao"]),
 (34, "u34-temporal", "organizar", "Nomear os giros temporais superior, médio e inferior pelos sulcos temporais", f"{T2} min 28-30", ["giro temporal"], ["temporais-org", "id-giro-temporal-superior", "id-giro-temporal-medio", "id-giro-temporal-inferior", "id-sulco-temporal-superior"]),
 (35, "u35-insula", "decorar", "Situar a ínsula no fundo do sulco lateral, sem osso correspondente; giros curtos e longo, sulco central da ínsula", f"{T2} min 30-32, 50-51; {MAC} cap7 §3.1.4", ["ínsula"], ["insula-posicao", "sh-id-insula", "insula-giros"]),
 (36, "u36-caloso", "organizar", "Ordenar as partes do corpo caloso (rostro, joelho, tronco, esplênio) e saber que une os hemisférios", f"{T2} min 33-36; {MAC} cap7 §3.2.1", ["esplênio"], ["corpo-caloso-partes-org", "id-joelho-corpo-caloso", "id-esplenio-corpo-caloso", "corpo-caloso-comissura"]),
 (37, "u37-cingulo", "decorar", "Situar o giro do cíngulo entre o sulco do corpo caloso e o sulco do cíngulo", f"{T2} min 37-38; {MAC} cap7 §3.2.3", ["cíngulo"], ["cingulo-limites", "id-giro-cingulo", "id-sulco-corpo-caloso"]),
 (38, "u38-paracentral", "decorar", "Delimitar o lóbulo paracentral pelos sulcos paracentral e marginal", f"{T2} min 38-41; {MAC} cap7 §3.2.3", ["paracentral"], ["paracentral-limites", "id-lobulo-paracentral", "id-sulco-paracentral", "id-sulco-marginal"]),
 (39, "u39-cuneo", "organizar", "Delimitar pré-cúneo e cúneo pelos sulcos marginal, parietoccipital e calcarino; área visual no calcarino", f"{T2} min 41-43; {MAC} cap7 §3.2.2", ["cúneo"], ["parietoccipital-separa", "precuneo-cuneo-org", "id-precuneo", "id-cuneo", "calcarino-visao", "id-sulco-calcarino"]),
 (40, "u40-face-medial", "distinguir", "Distinguir na vista medial o telencéfalo e o diencéfalo sem usar o corpo caloso como fronteira absoluta", f"{T2} min 47-48", ["corpo caloso"], ["face-medial-limite"]),
 (41, "u41-face-inferior", "organizar", "Reconhecer na face inferior os giros occipitotemporal medial, para-hipocampal, úncus e occipitotemporal lateral", f"{T2} min 43-47; {MAC} cap7 §3.3.1", ["úncus"], ["face-inferior-org", "id-giro-occipitotemporal-medial", "id-giro-parahipocampal", "id-unco", "id-giro-occipitotemporal-lateral", "parahipocampal-limbico"]),
 (42, "u42-achar-central", "e-se", "Achar o sulco central na peça pelos dois únicos giros transversais e paralelos", f"{T2} min 51-53; {T4} min 21-23", ["paralelos"], ["achar-sulco-central"]),
 # ---------- NÚCLEOS DA BASE ----------
 (43, "u43-centro-branco", "explicar", "Explicar núcleos da base como substância cinzenta no centro branco medular do hemisfério", f"{AP} Aula 6 cap5; {MAC} cap7 §5", ["centro branco medular"], ["nucleos-base-definicao"]),
 (44, "u44-corte", "organizar", "Ordenar, no corte horizontal, de fora para dentro: córtex da ínsula, cápsula extrema, claustro, cápsula externa, putâmen, globo pálido, cápsula interna, caudado/tálamo", f"{AP} Aula 6 cap5; {VET} p24; {MAC} cap7 §5.1.3", ["claustro"], ["corte-horizontal-org", "id-claustro", "id-putamen", "id-globo-palido", "id-nucleo-caudado"]),
 (45, "u45-lentiforme", "organizar", "Agrupar putâmen + globo pálido em núcleo lentiforme e lentiforme + caudado em corpo estriado", f"{AP} Aula 6 cap5; {VET} p24", ["lentiforme"], ["lentiforme", "corpo-estriado", "id-nucleo-lentiforme", "id-corpo-estriado"]),
 (46, "u46-capsulas", "distinguir", "Distinguir cápsulas extrema, externa e interna pelo que separam; partes da cápsula interna", f"{VET} p24; {MAC} cap7 §5.2; GaKa aula 4", ["cápsula externa"], ["capsulas-org", "capsula-interna-separa", "capsula-interna-partes", "id-capsula-externa", "id-capsula-extrema"]),
 # ---------- IRRIGAÇÃO ----------
 (47, "u47-vertebral", "decorar", "Seguir a artéria vertebral: subclávia, forames transversos, forame magno, face anterior do bulbo", f"{T3} min 00-02; {MAC} cap9 §2.2.3", ["forames transversos"], ["vertebral-trajeto", "id-arteria-vertebral"]),
 (48, "u48-cerebelares-inf", "decorar", "Saber que a cerebelar inferior posterior sai da vertebral e a inferior anterior da basilar", f"{T3} min 02-03; {MAC} cap9 §2.2.3", ["cerebelar inferior posterior"], ["pica-vertebral", "id-arteria-pica", "id-arteria-aica", "pica-wallenberg"]),
 (49, "u49-basilar", "decorar", "Formar a basilar pela união das vertebrais e situar a artéria do labirinto no meato acústico interno", f"{T3} min 03-04; {MAC} cap9 §2.2.3", ["artéria basilar"], ["basilar-formacao", "id-arteria-basilar", "labirinto-meato", "id-arteria-labirinto"]),
 (50, "u50-sca", "decorar", "Situar os ramos pontinos e a cerebelar superior, e a bifurcação da basilar nas cerebrais posteriores", f"{T3} min 04-05", ["cerebelar superior"], ["sca-territorio", "id-arteria-cerebelar-superior", "id-ramos-pontinos", "basilar-termina-acp"]),
 (51, "u51-acp", "e-se", "Dar o território da cerebral posterior (face inferior e lobo occipital) e prever o déficit visual na obstrução", f"{T3} min 05-07; {MAC} cap9 §2.2.5", ["cerebral posterior"], ["acp-territorio", "id-arteria-cerebral-posterior", "acp-visao"]),
 (52, "u52-carotida", "decorar", "Saber que a carótida interna não dá ramos no pescoço e entra pelo canal carotídeo, com o sifão", f"{T3} min 07-08; {MAC} cap9 §2.2.2", ["sifão carotídeo"], ["carotida-interna-sem-ramos", "id-arteria-carotida-interna"]),
 (53, "u53-oftalmica", "decorar", "Saber que a oftálmica é ramo da carótida interna para o bulbo ocular", f"{T3} min 08-09; {MAC} cap9 §2.2.2", ["oftálmica"], ["oftalmica-ramo"]),
 (54, "u54-ramos-aci", "organizar", "Nomear os ramos da carótida interna: cerebral média, cerebral anterior, comunicante posterior", f"{T3} min 09-10; {MAC} cap9 §2.2.2", ["cerebral média"], ["aci-ramos-org", "id-arteria-cerebral-media", "id-arteria-cerebral-anterior"]),
 (55, "u55-acm", "e-se", "Dar o território da cerebral média (face lateral pelo sulco lateral) e prever o déficit na obstrução", f"{T3} min 10-12; {MAC} cap9 §2.2.5", ["sulco lateral"], ["acm-territorio", "acm-deficit"]),
 (56, "u56-aca", "e-se", "Dar o território da cerebral anterior (face medial até o parietoccipital + faixa superior) e prever o déficit no membro inferior", f"{T3} min 12-14; {MAC} cap9 §2.2.5", ["fissura longitudinal"], ["aca-territorio", "aca-deficit"]),
 (57, "u57-hipofisarias", "decorar", "Saber que as hipofisárias superior e inferior saem da carótida interna", f"{T3} min 14-15", ["hipofisária"], ["hipofisarias", "id-arteria-hipofisaria-superior"]),
 (58, "u58-comunicantes", "distinguir", "Distinguir comunicante anterior (liga as cerebrais anteriores) de posterior (carótida interna à cerebral posterior)", f"{T3} min 15-16; {MAC} cap9 §2.2.4", ["comunicante"], ["comunicantes-org", "id-arteria-comunicante-anterior", "id-arteria-comunicante-posterior", "aneurisma-acom"]),
 (59, "u59-willis", "organizar", "Montar o círculo arterial do cérebro (polígono de Willis) unindo sistemas carotídeo e vertebrobasilar", f"{T3} min 16-18; {MAC} cap9 §2.2.4", ["polígono de Willis"], ["willis-composicao", "territorios-org"]),
]

REPETICAO = {
 22: "Telencéfalo como maior parte do cérebro: repete a unidade 1–2 (sh-cerebro-partes, diencefalo-escondido).",
 33: "O professor diz que o lobo occipital na face lateral não tem nada importante; a face medial é coberta na unidade 39.",
 60: "Prática: base do encéfalo e tronco repetem a aula 03 (cards no deck da aula 03).",
 61: "Prática: diencéfalo e telencéfalo nas peças repetem as unidades 5–42; cada estrutura tem card no bloco próprio.",
27: "O sulco central como marco frontal-parietal, corrigindo a simplificação da fala: coberto pelo IO do sulco central (unidade 25), pelo organizador dos lobos e pelo card de como achá-lo na peça.",
 62: "Prática: os três sulcos que separam os lobos repetem as unidades 25–26.",
}

DESTINO_AN01 = {
 "Caudado, putâmen, pálido e relações de cápsulas/núcleos em cortes": "agora: corte-horizontal-org, lentiforme, corpo-estriado, capsulas-org e identificações (unidades 43–46)",
 "Detalhes dos conjuntos diencefálicos": "agora: limites do tálamo, hipotálamo e subtálamo; núcleos do tálamo e do hipotálamo (unidades 3–20)",
}

ITENS += [(21,'u21-papez','explicar','Reconstruir hipocampo–fórnix–mamilares e mamilares–fascículo mamilotalâmico–tálamo anterior–cíngulo no circuito de Papez','Prova2023 Q14/Q17; Machado cap7', ['mamilotalâmico'],['ak-1483930154512','res-1792345652947']),(44,'u44-circuitos','explicar','Reconstruir vias direta e indireta e prever efeito dopaminérgico D1/D2','P1 2025 Q4/Q16/Q22', ['direta'],['res-1792347682942','res-1792347671169','res-1792347664967','res-1792347683193','ak-1481162377083','ak-1481162387832','res-1792347675467','ak-1481162415359','res-1792347683444','ak-1481162436810'])]

REPETICAO[40] = 'Vista medial retoma identificações dos blocos anteriores. Não transformar corpo caloso em fronteira absoluta: há estruturas telencefálicas abaixo dele.'

REPETICAO[40] = 'Vista medial retoma identificações dos blocos anteriores. Não transformar corpo caloso em fronteira absoluta: há estruturas telencefálicas abaixo dele.'

ITENS = [(u,i,t,o,f,ts,(['achar-sulco-central','sh-1792348020020'] if u==27 else ['sh-1792588687028','sh-1792588687033','sh-1792345652643'] if u==40 else ks)) for u,i,t,o,f,ts,ks in ITENS]
