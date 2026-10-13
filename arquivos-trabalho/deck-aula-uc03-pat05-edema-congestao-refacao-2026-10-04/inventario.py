"""Inventário atômico de Edema e congestão (16 lâminas vistas em 09/10; F-20261009-CLAUDE-02), para python3 -m nebli.inventario.
Fontes: lâminas (fontes/edema-slides-01-16.pdf, visual-slide-*.png), apostila de veteranos aula 6 (fontes/veteranos-patologia.txt
pp. 31–32), monitoria P1 aula 6 (../deck-aula-uc03-micro01-morfologia-2026-10-04/fontes/monitoria/micro-P1.txt pp. 15–16), Robbins
cap. 4 pp. 111–114 (fontes/robbins-cap4-…), provas P2 2024–2025 (fontes/provas-originais-edema.txt). fontes/exercicios-etapas-1-3 é a
apostila NEBLI de Davi, não material da aula: não entra como base.
"""
PREFIXO = "pat05"
AULA = "Edema e congestão (UC03, Patologia, aula 23; Prof. Luiz Fernando Ferraz da Silva)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Objetivos", [
   ("conceitos", "Conceituar edema, hiperemia e congestão", ["edema", "hiperemia-ativa", "congestao"]),
   ("hidrotorax", "Hidrotórax", "hidrotorax"),
   ("hidropericardio", "Hidropericárdio", "hidropericardio"),
   ("ascite", "Ascite", "ascite"),
   ("anasarca", "Anasarca", "anasarca"),
   ("fisiopatologia", "Fisiopatologia dos principais tipos de edema", ["hidrostatica", "edema-generalizado", "permeabilidade-exsudato", "linfedema-obstrucao"]),
   ("morfologia", "Correlatos morfológicos macro e microscópicos", ["morfologia-pulmonar-s09", "morfologia-pulmonar-s14", "nutmeg-direita"])]),
 (3, "conteudo", "Definições (congestão, hiperemia, edema com cacifo)", [
   ("congestao", "Congestão: sangue retido nos vasos, processo passivo", "congestao"),
   ("hiperemia", "Hiperemia: avermelhamento ativo por vasodilatação", "hiperemia-ativa"),
   ("edema", "Edema: líquido no interstício", "edema")]),
 (4, "conteudo", "Fisiologia da circulação capilar", [
   ("hidrostatica-oncotica", "Pressão hidrostática empurra, oncótica retém", ["filtracao", "reabsorcao", "oncotica", "gradiente-hidrostatico-capilar"]),
   ("linfaticos", "Linfáticos drenam o excedente", "linfa-retorno"),
   ("ducto", "Para o ducto torácico e a veia subclávia esquerda", "ducto-toracico")]),
 (5, "conteudo", "Mecanismos do edema", [
   ("hidrostatica", "Aumento da pressão hidrostática (limitação de fluxo, congestão)", "hidrostatica"),
   ("oncotica", "Redução da pressão oncótica (perda ou menor produção de proteínas)", ["edema-generalizado", "sindrome-nefrotica", "cirrose-edema"]),
   ("permeabilidade", "Aumento da permeabilidade vascular", "permeabilidade-exsudato")]),
 (6, "conteudo", "Derrames (pleural, pericárdico)", [
   ("derrame", "Líquido nas cavidades: derrame", ["derrame", "hidrotorax", "hidropericardio"]),
   ("transudato", "Transudato hidrostático, pobre em proteína", ["transudato-proteina", "transudato-hidrostatica"])]),
 (7, "conteudo", "Edema de membro, linfedema e ascite", [
   ("linfedema", "Linfedema por obstrução linfática (elefantíase, pós-mastectomia)", ["linfedema-obstrucao", "filariose", "linfedema-mastectomia"]),
   ("ascite-imagem", "Ascite na cavidade peritoneal", "ascite")]),
 (8, "conteudo", "Ciclo da insuficiência cardíaca", [
   ("bomba", "Disfunção miocárdica, volume sistólico menor", "disfuncao-bomba"),
   ("raas", "Ativação do RAAS e retenção de Na/H2O", ["raas-insuficiencia-cardiaca", "sodio-agua", "raas-agrava-edema"]),
   ("territorios", "IC esquerda → pulmão; direita → fígado e membros", ["insuficiencia-esquerda", "insuficiencia-esquerda-congestao", "insuficiencia-direita"])]),
 (9, "conteudo", "Edema pulmonar: macro, RX e histologia", [
   ("macro", "Pulmão pesado com espuma (surfactante)", "morfologia-pulmonar-s09"),
   ("rx", "Radiografia com edema pulmonar", "edema-pulmonar-rx"),
   ("venoso", "Hipertensão venosa pulmonar produz edema", "edema-pulmonar-venoso")]),
 (10, "conteudo", "Edema renal", [
   ("nefrotica", "Proteinúria, hipoalbuminemia (nefrótica)", "sindrome-nefrotica"),
   ("nefritica", "Retenção primária de Na por lesão glomerular", ["retencao-renal-primaria", "nefrite-retencao-sal", "nefrite-versus-nefrotica"])]),
 (11, "conteudo", "Cascata da ascite na cirrose", [
   ("portal", "Hipertensão portal", "hipertensao-portal-cirrose"),
   ("esplancnica", "Vasodilatação esplâncnica, volume efetivo menor", "vasodilatacao-esplancnica"),
   ("raas", "RAAS: avidez de sódio → ascite", ["raas-cirrose", "ascite-portal"]),
   ("hepatorrenal", "Vasoconstrição renal → síndrome hepatorrenal", "hepatorrenal")]),
 (12, "conteudo", "Ascite e fígado em noz-moscada", [
   ("ascite", "Abdome com ascite", "ascite-portal"),
   ("noz-moscada", "Congestão hepática crônica: noz-moscada", ["congestao-hepatica", "nutmeg-direita"])]),
 (13, "conteudo", "Dano alveolar e permeabilidade", [
   ("cascata", "Agente lesivo → macrófago (TNF, IL-8) → neutrófilos (PAF, leucotrienos, proteases)", ["neutrofilos-lesao-alveolar", "leucotrienos-permeabilidade"]),
   ("barreira", "Lesão endotelial e de pneumócito destrói a barreira alvéolo-capilar", ["lesao-alveolocapilar", "permeabilidade-capilar-edema", "edema-proteico-ards"]),
   ("resultado", "Aumento de permeabilidade, extravasamento, membrana hialina", ["membrana-hialina", "exsudato-proteina"])]),
 (14, "conteudo", "Histologia: edema hidrostático", [("transudato-histo", "Líquido claro, pobre em células, capilares congestos", "morfologia-pulmonar-s14")]),
 (15, "conteudo", "Histologia: edema por permeabilidade", [
   ("exsudato-histo", "Exsudato com membranas hialinas", ["morfologia-pulmonar-s13", "cardiogenico-versus-permeabilidade"]),
   ("hemossiderina", "Macrófagos com hemossiderina na congestão crônica", "celulas-insuficiencia-cardiaca")]),
 (16, "capa", "Encerramento", []),
]

CAPITULO = [
 ("Robbins cap. 4 (edema, hiperemia e congestão)", [
   ("starling", "Forças de Starling e drenagem linfática", ["filtracao", "reabsorcao", "linfa-retorno"]),
   ("causas", "Causas: hidrostática, oncótica, obstrução linfática, retenção de sódio, inflamação", ["hidrostatica", "edema-generalizado", "linfedema-obstrucao", "sodio-agua", "permeabilidade-exsudato"]),
   ("hiperemia-congestao", "Hiperemia ativa × congestão passiva; noz-moscada; células da insuficiência cardíaca", ["hiperemia-ativa", "congestao", "nutmeg-direita", "celulas-insuficiencia-cardiaca"])]),
]

EXERCICIOS = [
 ("Apostila de veteranos, aula 6", [
   ("passivo-ativo", "Congestão passiva × hiperemia ativa", ["congestao", "hiperemia-ativa"]),
   ("cavidades", "Hidrotórax (IC), hidropericárdio (pericardite), ascite (cirrose); derrame", ["hidrotorax", "hidropericardio", "ascite", "derrame"]),
   ("anasarca", "Anasarca na IC, nefrótica, cirrose", "anasarca"),
   ("linfedema", "Linfedema por elefantíase ou iatrogênico (mastectomia)", ["filariose", "linfedema-mastectomia"]),
   ("transudato-exsudato", "Transudato × exsudato; empiema", ["transudato-proteina", "exsudato-proteina", "empiema"]),
   ("ic-raas", "IC: mácula densa e barorreceptores ativam RAAS", "raas-insuficiencia-cardiaca"),
   ("hepatico", "Insuficiência hepática: hipertensão portal + albumina baixa", ["cirrose-edema", "hipertensao-portal-cirrose"])]),
 ("Monitoria P1, aula 6", [
   ("generalizado", "Oncótico generalizado × hidrostático localizado", "edema-generalizado"),
   ("retracao", "Permeabilidade: retração endotelial, exsudato", "contracao-endotelial"),
   ("piema", "Exsudato purulento na pleura", "empiema"),
   ("misto", "Hepatopata misto; translocação bacteriana e peritonite", "pbe"),
   ("histo", "Hidrostático: transudato pálido; permeabilidade: exsudato e membranas hialinas", ["morfologia-pulmonar-s14", "morfologia-pulmonar-s13"])]),
 ("Edema e Congestão II (37 lâminas, drive da turma)", [
   ("ii-mixedema", "Mixedema", "mixedema"),
   ("ii-mole-duro", "Transudato: edema mole com cacifo, gravidade; exsudato: duro", "edema-mole-duro"),
   ("ii-derrame-causas", "Derrame pleural: transudato (ICC, IH, nefrótica) × exsudato (pneumonia, neoplasia, pancreatite, AR)", ["transudato-hidrostatica", "permeabilidade-exsudato"]),
   ("ii-light", "Critérios de Light para exsudato", "light"),
   ("ii-ascite-causas", "Ascite: cirrose, obstrução vascular, nefrótica", ["ascite-portal", "sindrome-nefrotica"]),
   ("ii-underfill", "Teorias underfill × overflow na cirrose", "underfill-overflow"),
   ("ii-gsaa", "Avaliação da ascite: aspecto, celularidade, GSAA, BAAR", "gsaa"),
   ("ii-anamnese", "Anamnese: face, matutino (oncótico) × vespertino (gravitacional), início", "edema-horario"),
   ("ii-exame", "Exame físico: cacifo, sinais flogísticos, derrames, ausculta, estase jugular", ["estase-jugular", "hidrostatica"])]),
 ("Palavras-cruzadas da aula (gabarito)", [
   ("pc-hemossiderina", "Hemossiderina e células do vício cardíaco", "celulas-insuficiencia-cardiaca"),
   ("pc-eritema", "Eritema pela hiperemia; vasodilatação arteriolar", "hiperemia-ativa"),
   ("pc-elefantiase", "Elefantíase (filariose) com linfedema localizado", "filariose"),
   ("pc-hepatica", "Insuficiência hepática: oncótica + permeabilidade", "cirrose-edema"),
   ("pc-venula", "Recaptação maior no lado venoso", "reabsorcao")]),
 ("Provas UC03 P2", [
   ("2024-iam", "2024: edema pulmonar hidrostático (transudato) após IAM", ["insuficiencia-esquerda", "transudato-hidrostatica"]),
   ("2024-exsudato", "2024: líquido pericapsular renal é exsudato (histamina, bradicinina, leucotrienos)", ["permeabilidade-exsudato", "histamina-permeabilidade", "contracao-endotelial"]),
   ("2025-mediadores", "2025: histamina/bradicinina no edema inicial", ["histamina-permeabilidade", "bradicinina-permeabilidade"])]),
]
