"""Inventário atômico de Micoses subcutâneas (UC03 P3, Microbiologia; Prof. Benedito Corrêa, 2026; 42 lâminas, Drive pessoal
48 - Micoses subcutâneas). Escrito em 10/10/2026 antes da seleção: lâminas 2026 (visual/folha-01..07), transcrição oficial (turma,
fala do próprio professor), PDF da turma (versão anterior das lâminas), monitoria P2 aula 11 (esporotricose e cromoblastomicose),
Trabulsi cap. 68 (livros/trabulsi-micoses-subcutaneas.txt). Sem questões de prova antigas desta aula no acervo (busca registrada).
"""
PREFIXO = "mb48"
AULA = "Micoses subcutâneas (UC03 P3; Prof. Benedito Corrêa, 2026)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Micoses subcutâneas: conceito", [
   ("implantacao", "Implantação traumática de fungos sapróbios (vegetais)", "subcut-def"),
   ("localizadas", "Ficam no subcutâneo; às vezes disseminam por via linfática", "subcut-def")]),
 (3, "conteudo", "Classificação (superficiais, cutâneas, subcutâneas)", [
   ("lista-sub", "Esporotricose, cromomicose, maduromicose, Jorge Lobo", ["subcut-def", "espinho", "cromo-agentes", "micetoma-tipos", "lacazia"])]),
 (4, "conteudo", "Classificação (sistêmicas)", [("sist", "Histoplasmose, PCM, criptococose, candidose, aspergilose", EXC + "aula seguinte (micoses sistêmicas)")]),
 (5, "conteudo", "História da esporotricose", [
   ("schenck", "Schenck 1898; África do Sul 1941–44 (mineiros, madeira)", EXC + "histórico de datas; a ideia útil (inoculação por espinho/madeira) está em espinho")]),
 (6, "conteudo", "Epidemia no Brasil", [("rj", "1ª epidemia no Rio de Janeiro; epidemias atuais (gatos)", "gatos")]),
 (7, "conteudo", "Complexo Sporothrix schenckii", [("complexo", "S. brasiliensis, mexicana, globosa, albicans; separadas por biologia molecular", "brasiliensis")]),
 (8, "conteudo", "Epidemiologia: agente, reservatório, porta de entrada", [
   ("reservatorio", "Fungo ubiquitário; solo e vegetais", "espinho"),
   ("vias", "Via direta (ferimento) e indireta (arranhadura de gato)", ["espinho", "gatos"])]),
 (9, "conteudo", "População de risco e incidência", [("risco", "Caçadores, manipuladores de plantas, recreação; homens 20–50 anos", "ocupacional")]),
 (10, "conteudo", "Contágio por inoculação", [("inoculacao", "Espinho de rosa e lesões em cadeia no braço", ["espinho", "linfocutanea"])]),
 (11, "conteudo", "Esporotricose: resumo", [
   ("dimorfico", "Dimórfico: bolor a 25 °C, levedura a 37 °C", ["levedura-tecido", "hifas-25"]),
   ("formas", "Linfocutânea, cutânea fixa, extracutânea, pulmonar, disseminada", ["linfocutanea", "fixa", "disseminada", "pulmonar-primaria"])]),
 (12, "conteudo", "Lesão inicial", [("inicial", "Pústula/úlcera no ponto de inoculação", "lesao-inicial")]),
 (13, "conteudo", "Forma cutânea localizada", [("localizada", "Lesão restrita ao ponto de inoculação", "fixa")]),
 (14, "conteudo", "Forma cutânea localizada (foto)", [("localizada2", "Lesão ulcerada no dedo", "fixa")]),
 (15, "conteudo", "Forma linfocutânea", [("linfo", "Nódulos ascendendo pelo linfático", "linfocutanea")]),
 (16, "conteudo", "Forma linfocutânea (fotos)", [("linfo2", "Nódulos em cadeia no antebraço", "linfocutanea")]),
 (17, "conteudo", "Forma localizada na face", [("face", "Lesão localizada no mento", "fixa")]),
 (18, "conteudo", "Forma linfocutânea (antebraço)", [("linfo3", "Cadeia de lesões", "linfocutanea")]),
 (19, "conteudo", "Esporotricose disseminada", [("dissem", "Lesões múltiplas em imunodeprimido", "disseminada")]),
 (20, "conteudo", "Esporotricose em cão", [("cao", "Forma disseminada em cão", "gatos")]),
 (21, "conteudo", "Esporotricose em gatos", [("gato", "Lesões faciais em gatos, principais transmissores", "gatos")]),
 (22, "conteudo", "Exame direto", [("charuto", "Leveduras alongadas em charuto/naveta", ["charuto", "hialino", "grocott"])]),
 (23, "conteudo", "Cultivo a 25 °C", [("colonia", "Colônia membranosa que escurece", "margarida")]),
 (24, "conteudo", "Microscopia a 25 °C", [("margarida", "Conídios em margarida na ponta do conidióforo", "margarida")]),
 (25, "conteudo", "Fase leveduriforme", [("fase-y", "Levedura em tecido/37 °C", ["levedura-tecido", "reversao"]),
   ("dx-cultura", "Exame direto falha com frequência; cultura confirma (transcrição)", "cultura")]),
 (26, "conteudo", "Cromomicose: etiologia e epidemiologia", [
   ("cromo-agentes", "Fonsecaea, Cladosporium, Phialophora, Rhinocladiella", "cromo-agentes"),
   ("cromo-epi", "Tropical/subtropical; solo e madeira; micose ocupacional", "cromo-ocupacional")]),
 (27, "conteudo", "Cromomicose: clínica", [("couve-flor", "Nódulos verrucosos nos membros inferiores", "couve-flor")]),
 (28, "conteudo", "Cromomicose: diagnóstico laboratorial", [("cromo-dx", "Coleta, KOH, biópsia, cultivo", "corpos-escleroticos")]),
 (29, "conteudo", "Exame direto: corpos escleróticos", [("escleroticos", "Corpos escleróticos em pus/crostas", "corpos-escleroticos")]),
 (30, "conteudo", "Cultivo de Fonsecaea pedrosoi", [("cromo-cultivo", "Colônia escura em Sabouraud", "cromo-agentes")]),
 (31, "conteudo", "Tipos de conidiação", [("conidiacao", "Garrafa (fiálide), acrógena, acropleurógena", "conidiacao")]),
 (32, "conteudo", "Histopatológico da cromomicose", [("histo-cromo", "Corpos escleróticos no granuloma", "corpos-escleroticos")]),
 (33, "conteudo", "Maduromicose podal", [("podal", "Pé com tumoração e fístulas", ["triade", "micetoma-pe"])]),
 (34, "conteudo", "Micetomas", [
   ("tipos", "Actinomicose, nocardiose (bactérias) e maduromicose (fungos)", ["micetoma-tipos", "actinomyces", "nocardia"])]),
 (35, "conteudo", "Tríade do micetoma", [("triade", "Tumor, fístula, grãos parasitários", "triade")]),
 (36, "conteudo", "Diagnóstico: grãos", [("graos", "Grãos no exame direto ou histopatológico", ["triade", "madurella", "grao-hifas", "grao-branco"])]),
 (37, "conteudo", "Maduromicose podal (raio X)", [("rx", "Destruição óssea no pé", EXC + "foto ilustrativa sem texto; extensão ao osso não é explicada na aula")]),
 (38, "conteudo", "Jorge Lobo: etiologia", [
   ("lacazia", "Lacazia loboi (Paracoccidioides loboi)", "lacazia"),
   ("recife", "1º caso em Recife (paciente da Amazônia)", EXC + "detalhe histórico")]),
 (39, "conteudo", "Jorge Lobo: epidemiologia", [("lobo-epi", "Homens 20–45 anos, seringueiros; também golfinhos", "lobo-epi")]),
 (40, "conteudo", "Jorge Lobo: lesões queloidianas", [("queloide", "Lesões queloidianas (orelha)", "queloide")]),
 (41, "conteudo", "Jorge Lobo: diagnóstico", [("sem-cultura", "Não cresce em cultura; exame direto e biópsia", "lobo-cultura")]),
 (42, "conteudo", "Jorge Lobo: exame direto e histopatológico", [("cadeias", "Células refringentes de parede grossa em cadeias", "lobo-cadeias")]),
]

CAPITULO = [("Trabulsi 6ª ed., cap. 68 (micoses subcutâneas)", [
   ("tb-conceito", "Sapróbios do solo/vegetais, parasitas acidentais após trauma", "subcut-def"),
   ("tb-linfo", "Forma linfocutânea é a mais comum", "linfocutanea"),
   ("tb-gatos", "Transmissão zoonótica por gatos no Rio de Janeiro", "gatos"),
   ("tb-reversao", "Conversão a levedura diferencia Sporothrix de sapróbios semelhantes", "reversao"),
   ("tb-ki", "Iodeto de potássio é tratamento clássico", "ki"),
   ("tb-cromo", "Fonsecaea pedrosoi predomina no Brasil; lesões verrucosas em couve-flor", ["cromo-agentes", "couve-flor"])])]

EXERCICIOS = [
 ("Monitoria P2, aula 11", [
   ("mon-transmissao", "Via saprofítica (trauma) e zoonótica (gato)", ["espinho", "gatos", "gato-levedura"]),
   ("mon-formas", "Linfocutânea mais comum; fixa, disseminada, mucosa", ["linfocutanea", "fixa", "disseminada"]),
   ("mon-dimorfismo", "Conversão filamentosa (floral) → levedura (charuto)", ["margarida", "charuto"]),
   ("mon-tratamento", "Itraconazol, terbinafina, iodeto de potássio; anfotericina na disseminada", ["itraconazol", "ki"]),
   ("mon-cromo", "Fonsecaea pedrosoi, demáceo; lesões verrucosas em membros inferiores; 3 tipos de conidiação", ["cromo-agentes", "couve-flor", "conidiacao"])]),
]
