"""Inventário atômico — 2026-uc03-patologia-65-reparo-tecidual (gerado por nebli.rapido a partir dos cards e das classes das lâminas)."""
PREFIXO = "pt65"
AULA = 'Reparo tecidual e cicatrização de feridas (UC03 P3; Patologia)'
EXC = "EXC: "

SLIDES = [
 (1, 'capa', 'Capa', []),
 (2, 'conteudo', 'Lâmina 2', [('i2-1', 'Quatro destinos da lesão', 'c-org-destinos')]),
 (3, 'conteudo', 'Lâmina 3', [('i3-1', 'O arcabouço decide regeneração ou cicatriz', 'c-arcabouco')]),
 (4, 'conteudo', 'Lâmina 4', [('i4-1', 'Tecido permanente sem regeneração', 'ak1487981520428'), ('i4-2', 'Tecido lábil', 'sh-1792240567845'), ('i4-3', 'Tecido estável', 'sh-1792240568095')]),
 (5, 'conteudo', 'Lâmina 5', [('i5-v4-0', 'Pluripotente', 'ak1554057652314'), ('i5-v4-00', 'Multipotente', 'ak1554057667664'), ('i5-v4-1', 'Potência das células-tronco em ordem: totipotente (zigoto) →', 'ak1554057640901')]),
 (6, 'conteudo', 'Lâmina 6', [('i6-1', 'O que cada nicho de célula-tronco somática origina', 'c-org-nichos'), ('i6-2', 'Células-tronco do intestino na cripta', 'sh-1790980910905')]),
 (7, 'conteudo', 'Lâmina 7', [('i7-1', 'Célula estável entra em G1 quando estimulada', 'ak1468101709109'), ('i7-2', 'Célula lábil nunca entra em G0', 'ak1468101721156')]),
 (8, 'conteudo', 'Lâmina 8', [('i8-1', 'TGF-β medeia fibrose e angiogênese', 'sh-1791983683185'), ('i8-2', 'PDGF estimula o fibroblasto', 'sh-1791983683760'), ('i8-v4-a', 'EGF', 'ak1487981570164'), ('i8-v4-b', 'TGF-α', 'ak1526322147796'), ('i8-v4-c', 'VEGF', 'ak1487981568284'), ('i8-v4-d', 'FGF-2', 'ak1487981566131'), ('i8-v4-e', 'KGF e HGF', 'c-org-fatores')]),
 (9, 'conteudo', 'Lâmina 9', [('i9-v4-0', 'TGF-β inibe proliferação', 'sh-1791625435532'), ('i9-v4-1', 'O TGF-β inibe a proliferação da maioria das células, mas pro', 'sh-1791983683185')]),
 (10, 'conteudo', 'Lâmina 10', [('i10-1', 'Crescimento compensatório do fígado', 'c-crescimento-comp')]),
 (11, 'conteudo', 'Lâmina 11', [('i11-1', 'A matriz guarda fatores de crescimento', 'c-mec-funcoes')]),
 (12, 'conteudo', 'Lâmina 12', [('i12-1', 'Integrinas sinalizam célula-matriz', 'c-integrinas')]),
 (13, 'conteudo', 'Lâmina 13', [('i13-1', 'Fases da cicatrização e seus tempos', 'c-org-fases')]),
 (14, 'conteudo', 'Lâmina 14', [('i14-1', 'Primeira intenção: bordas aproximadas', 'ak1487981574852')]),
 (15, 'conteudo', 'Lâmina 15', [('i15-0', 'Quatro fases', 'c-org-fases'), ('i15-1', 'Imunossupressão bloqueia a fase inflamatória', 'c-imunossupressao')]),
 (16, 'conteudo', 'Lâmina 16', [('i16-v4-1', 'No gráfico das fases, inflamação (4 a 6 dias), proliferação ', 'c-grafico-fases')]),
 (17, 'conteudo', 'Lâmina 17', [('i17-1', 'Quatro fases da cicatrização', 'c-org-fases')]),
 (18, 'conteudo', 'Lâmina 18', [('i18-v4-1', 'No 1º dia, a vasoconstrição e o tampão plaquetário limitam a', 'ak1473985997545')]),
 (19, 'conteudo', 'Lâmina 19', [('i19-1', 'Hemostasia secundária estabiliza com fibrina', 'ak1473985984856')]),
 (20, 'conteudo', 'Lâmina 20', [('i20-v4-1', 'A plaqueta ativada libera serotonina e histamina, que causam', 'sh-1791780353997')]),
 (21, 'conteudo', 'Lâmina 21', [('i21-1', 'Neutrófilo migra por produtos bacterianos e DAMPs', 'c-neutrofilo-dano'), ('i21-2', 'Macrófagos depois dos neutrófilos', 'sh-1792242119048')]),
 (22, 'conteudo', 'Lâmina 22', [('i22-1', 'M1 depois M2 na ferida', 'c-m1-m2')]),
 (23, 'conteudo', 'Lâmina 23', [('i23-1', 'IL-10 e TGF-β mediam a resolução', 'sh-1791743349160')]),
 (24, 'conteudo', 'Lâmina 24', [('i24-v4-1', 'No gráfico de células por dia, o neutrófilo tem pico primeir', 'c-grafico-celulas'), ('i24-v4-2', 'O oxigênio do tecido cai no começo do reparo (vasoconstrição', 'c-oxigenio')]),
 (25, 'conteudo', 'Lâmina 25', [('i25-v4-1', 'TNF e IL-1 comandam a fase inflamatória inicial; TGF-β e os ', 'c-citocinas-fase')]),
 (26, 'conteudo', 'Lâmina 26', [('i26-1', 'Fase proliferativa é o tecido de granulação', 'ak1487981531796')]),
 (27, 'conteudo', 'Lâmina 27', [('i27-1', 'Fibroblasto deposita colágeno III', 'ak1487981539804')]),
 (28, 'conteudo', 'Lâmina 28', [('i28-1', 'Vitamina C hidroxila prolina e lisina no colágeno', 'ak1476583833764')]),
 (29, 'conteudo', 'Lâmina 29', [('i29-1', 'Colágeno III vira I no remodelamento', 'ak1487981545623')]),
 (30, 'conteudo', 'Lâmina 30', [('i30-v4-1', 'No gráfico da matriz, fibronectina e colágeno III são sintet', 'c-grafico-matriz')]),
 (31, 'conteudo', 'Lâmina 31', [('i31-1', 'Angiogênese com vasos imaturos e permeáveis', 'c-angiogenese')]),
 (32, 'conteudo', 'Lâmina 32', [('i32-v4-1', 'O leito vermelho do tecido de granulação é sinal de boa evol', 'c-desbridamento')]),
 (33, 'conteudo', 'Lâmina 33', [('i33-1', 'Tecido de granulação: colágeno III, capilares e miofibroblastos', 'ak1487981537242')]),
 (34, 'conteudo', 'Lâmina 34', [('i34-1', 'Tecido de granulação: componentes', 'ak1487981537242'), ('i34-2', 'Leito vermelho e desbridamento', 'c-desbridamento')]),
 (35, 'conteudo', 'Lâmina 35', [('i35-v4-1', 'A reepitelização repõe a célula basal, mas o melanócito prol', 'c-reepitelizacao')]),
 (36, 'conteudo', 'Lâmina 36', [('i36-1', 'Maturação regride vasos e remodela colágeno', 'c-maturacao')]),
 (37, 'conteudo', 'Lâmina 37', [('i37-1', 'Redução do edema na maturação', 'c-maturacao'), ('i37-2', 'Força tênsil', 'ak1487981594443'), ('i37-3', 'Contração da cicatriz', 'ak1487981543711')]),
 (38, 'conteudo', 'Lâmina 38', [('i38-1', '70 a 80% da força em 3 meses', 'ak1487981594443'), ('i38-2', 'Deiscência após cirurgia abdominal', 'ak1487981592613')]),
 (39, 'conteudo', 'Lâmina 39', [('i39-1', 'Segunda intenção: bordas não aproximadas', 'ak1487981578907')]),
 (40, 'conteudo', 'Lâmina 40', [('i40-1', 'Miofibroblasto contrai a ferida', 'ak1487981543711')]),
 (41, 'conteudo', 'Lâmina 41', [('i41-0', 'Eventos de cada fase no tempo', 'c-org-fases'), ('i41-1', 'Infecção atrasa a cicatrização', 'ak1487981587235')]),
 (42, 'conteudo', 'Lâmina 42', [('i42-1', 'Mediadores do macrófago por papel no reparo', 'c-macrofago-reparo')]),
 (43, 'conteudo', 'Lâmina 43', [('i43-1', 'Fibrose: mais síntese e menos degradação', 'c-fibrose-mec')]),
 (44, 'conteudo', 'Lâmina 44', [('i44-1', 'Cicatriz hipertrófica respeita a borda', 'ak1487981599441'), ('i44-2', 'Queloide ultrapassa a borda', 'ak1487981612881')]),
 (45, 'capa', 'Encerramento', []),
]
JUSTIFICATIVAS = {'capa': 'capa sem conteúdo', 'fora_do_recorte': 'figura ou detalhe sem card próprio; o conceito está no card vizinho ou no FORA_DO_RECORTE', 'logistica': 'divisória, leitura recomendada, agradecimento ou repetição'}
CAPITULO = [('Robbins, Bases Patológicas das Doenças, cap. 3', [('p', 'Cura de feridas: fases, intenções, granulação', 'ak1487981531796'), ('q', 'Queloide e cicatriz hipertrófica', 'ak1487981612881'), ('r', 'Fibrose e TGF-β', 'c-fibrose-mec')])]
EXERCICIOS = [('Provas UC03 (índice pat-11-reparo-tecidual-cicatrizacao)', [('u', '2025 P3 4.2 fase inflamatória', 'c-imunossupressao'), ('v', '2025 P3 4.3 primeira × segunda intenção', 'ak1487981578907'), ('w', '2016 P2 2.4 tecido de granulação', 'ak1487981537242'), ('x', '2015 P2sub 3.1 ponto', 'ak1487981574852'), ('y', '2016 P2 1.7 arcabouço', 'c-arcabouco')]), ('Monitoria P3, aula 11 (reparo)', [('m', 'Regeneração × reparo e arcabouço', 'c-arcabouco')]), ('Apostila guia de Patologia, aula 9', [('z', 'Tip e stalk cells; Notch', 'EXC: só na apostila; sem card de acervo; vai no Tab')]), ('Palavras-cruzadas da aula', [('aa', 'Macrófago, queloide, miofibroblasto, MMP, hérnia incisional', 'ak1487981612881')])]

# F-20261106-CLAUDE-01: lâmina visual sem figura no card, com motivo próprio
FIGURA_SEM_CARD = {31: 'o esquema de brotamento da lâmina 31 não mostra o capilar imaturo e permeável que o card cobra; retirado na formatação final', 35: "a figura da lâmina 35 é pele normal em camadas; o card cobra a proliferação menor do melanócito, e o verificador rejeitou a figura por não mostrar reepitelização nem cicatriz clara"}
