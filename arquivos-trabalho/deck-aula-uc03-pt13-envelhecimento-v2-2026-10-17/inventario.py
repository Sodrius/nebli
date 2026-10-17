"""Inventário atômico de Envelhecimento celular e tecidual (UC03 P1; Patologia; Prof. Luiz F. Ferraz da Silva), escrito ANTES de
escolher cards (17/10, pipeline v4). Sequência = 22 lâminas (fontes/slides.pdf = pasta pessoal = pasta da turma, mesmo sha1 30310d66),
vistas inteiras nesta sessão (io/g0..g1). Lido nesta sessão: transcrição integral (46 pp.), provas pat-04 (9 subquestões), palavras-cruzadas
com gabarito, monitoria P1 aula 3, apostila guia de Patologia Aula 4, apostila UC3, Robbins cap. 1 “Envelhecimento celular”
(livros/robbins-cap1-envelhecimento.txt, pdf pp. 59–62) e bibliografia da aula (Guarente, Sirtuins, aging, and medicine, NEJM 2011).
Atenção: a transcrição diz que Werner é defeito da “histona desacetilase”; o Robbins (e as cruzadas, item 10) dizem DNA helicase, e a
atividade desacetilase é das sirtuínas — seguido o Robbins.
Fronteira (MEMORY §3): radicais livres e proteínas mal dobradas são da 09 → sh(); lipofuscina é da 11 → sh() da cópia que a 11 instalar
(vaga PT11 no spec); telomerase em detalhe molecular é Biomol, mas a seção FirstAid Telomerase entra inteira (todo AnKing do conteúdo).
"""
PREFIXO = "pt13"
AULA = "Envelhecimento celular e tecidual (UC03 P1; Patologia)"
EXC = "EXC: "
LIPO, LIPO_LOCAIS = "sh-PT11-LIPO", "sh-PT11-LIPO-LOCAIS"
RESP = ["ak-pulm-complacencia", "ak-parede-complacencia", "ak-vr", "ak-cvf", "ak-vef1", "ak-cpt", "ak-vq", "ak-aa", "ak-musculo-resp"]

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Definições: menos capacidade adaptativa e reserva; senescência × senilidade",
  [("a1", "Envelhecer = perder capacidade adaptativa e reserva funcional", "au-reserva"),
   ("a2", "Senescência: efeitos naturais do envelhecimento", "au-senescencia"),
   ("a3", "Senilidade: alterações por doenças do idoso", "au-senescencia")]),
 (3, "conteudo", "Curva da reserva funcional: máximo × basal, pico aos 40",
  [("a4", "Reserva = máximo − basal", "au-reserva"), ("a5", "Pico perto dos 35–40 anos", "au-reserva")]),
 (4, "conteudo", "Esquema do Robbins: mecanismos gerais do envelhecimento",
  [("a6", "Dano ao DNA, senescência replicativa, homeostase proteica, sensores de nutrientes", ["au-replicativa", "sh-1792117369568", "au-proteostase", "au-sirtuinas"])]),
 (5, "conteudo", "Esquema: senescência celular (encurtamento do telômero → perda de células)", [("a7", "Senescência replicativa", "au-replicativa")]),
 (6, "conteudo", "Telômeros: células germinativas, tronco, normal, câncer; telomerase com molde de RNA",
  [("a8", "Encurtamento a cada divisão → parada", "au-replicativa"),
   ("a9", "Telomerase adiciona TTAGGG", "ak-ttaggg"), ("a10", "Telomerase é transcriptase reversa", "ak-telomerase-rt"),
   ("a11", "Telomerase alta no câncer", ["ak-telomerase-cancer", "ak-cancer-telomerase2"]),
   ("a12", "Potencial replicativo ilimitado (Hayflick)", "ak-hayflick"),
   ("a13", "Telomerase baixa → envelhecimento precoce", "ak-progeria")]),
 (7, "conteudo", "Esquema: dano ao DNA, reparo defeituoso, mutações", [("a14", "Mutações se acumulam com reparo pior", ["sh-1792117369568", "au-werner"])]),
 (8, "conteudo", "Formação de radicais livres: UV, radiação ionizante, cigarro, inflamação, metabolismo, poluição",
  [("a15", "Radicais livres lesam DNA, lipídios e proteínas", "sh-1792117369568")]),
 (9, "conteudo", "Esquema: proteínas danificadas, homeostase proteica defeituosa",
  [("a16", "Perda da homeostase proteica", ["au-proteostase", "ak-chaperona", "ak-proteassomo-danificada", "sh-1792117372320"])]),
 (10, "conteudo", "Esquema: sensores de nutrientes (insulina/IGF, TOR, sirtuínas)", [("a17", "Restrição calórica e sirtuínas", "au-sirtuinas")]),
 (11, "conteudo", "Síndrome de Werner (fotos aos 15 e 48 anos)", [("a18", "Werner: envelhecimento precoce", "au-werner")]),
 (12, "conteudo", "Aspectos gerais: estatura, peso, água, pelos, turgor, olfato, presbiopia e presbiacusia",
  [("a19", "Perda de estatura e de água; mais gordura", "ak-massa-gordura"),
   ("a20", "Turgor e elasticidade da pele", ["au-turgor", "ak-rugas", "ak-rugas-colageno"]),
   ("a21", "Presbiopia", ["ak-presbiopia", "ak-presbiopia-cristalino", "ak-presbiopia-oculos", "ak-presbiopia-miopia"]),
   ("a22", "Presbiacusia", ["ak-presbiacusia", "ak-presbiacusia-def", "ak-presbiacusia-base"]),
   ("a23", "Perda de pelos, olfato e gustação", EXC + "lista sem mecanismo próprio; no verso de ak-massa-gordura")]),
 (13, "conteudo", "Respiratório: expansibilidade, transporte mucociliar, tosse, volume residual, elasticidade",
  [("a24", "Pulmão do idoso", RESP)]),
 (14, "conteudo", "Curvas de CVF, VEF1/CVF e VEF1 em fumantes", [("a25", "VEF1 cai com a idade; fumo acelera", ["ak-vef1", "ak-cvf"])]),
 (15, "conteudo", "Sistema nervoso: menos neurônios, peso, condução e neurotransmissores", [("a26", "Cérebro do idoso; cognição preservada", "ak-inteligencia")]),
 (16, "conteudo", "Alzheimer × normal; placa senil", [("a27", "Alzheimer é senilidade", "au-senescencia")]),
 (17, "conteudo", "Cardiovascular: espessamento valvar, complacência, frequência, rigidez vascular",
  [("a28", "Artérias rígidas", ["ak-arterias", "ak-arterias-elastina", "ak-has-sistolica"]),
   ("a29", "Valvas e septo do idoso", ["ak-ea-calcificacao", "ak-septo-sigmoide"])]),
 (18, "conteudo", "Urinário: fluxo renal −1%/ano após 50, concentração urinária, TFG",
  [("a30", "TFG cai com a idade", ["au-tfg", "ak-tfg-idade"])]),
 (19, "conteudo", "Locomotor: fibras musculares, fibras elásticas, osteopenia, cartilagem",
  [("a31", "Sarcopenia e creatinina", "au-creatinina"), ("a32", "Massa óssea", ["ak-pico-osso", "ak-perda-osso"]),
   ("a33", "Cartilagem desidratada → artrose", "ak-artrose")]),
 (20, "conteudo", "Coração: débito, complacência, rigidez; lipofuscina no miocárdio",
  [("a34", "Lipofuscina no miocárdio", [LIPO, LIPO_LOCAIS])]),
 (21, "conteudo", "Tabela-resumo das alterações fisiológicas", [("a35", "Resumo", EXC + "quadro-resumo; cada sistema tem card próprio")]),
 (22, "logistica", "Imagem de humor", []),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "logistica": "imagem de humor sem conteúdo"}
CAPITULO = [("Robbins cap. 1, Envelhecimento celular (pp. 39–42) e bibliografia da aula (Guarente 2011)", [
 ("l1", "Diminuição da replicação: telômeros, telomerase em germinativas e tronco", ["au-replicativa", "ak-ttaggg"]),
 ("l2", "Werner: DNA helicase", "au-werner"),
 ("l3", "Lesão oxidativa e reparo do DNA", "sh-1792117369568"),
 ("l4", "Declínio do proteassomo", "au-proteostase"),
 ("l5", "Restrição calórica, sirtuínas, IGF", "au-sirtuinas")])]
EXERCICIOS = [
 ("Provas UC03 (índice pat-04)", [
   ("p1", "Perda óssea: senescência × senilidade (2024 P1 1.3)", "au-senescencia"),
   ("p2", "Creatinina baixa no idoso (2023 P1 1.8)", "au-creatinina"),
   ("p3", "VEF1, função renal e turgor no idoso (2019 P1 1.3)", ["ak-vef1", "au-tfg", "au-turgor"]),
   ("p4", "Plasticidade sináptica do avô: perda de reserva, mutações, estresse oxidativo (2018 P1 2.4)", ["au-reserva", "sh-1792117369568"]),
   ("p5", "TFG normal para a idade (2017 P1 1.5)", "au-tfg"),
   ("p6", "Telomerase nas marcas do câncer (2017 P4 4.1)", ["ak-telomerase-cancer", "ak-hayflick"]),
   ("p7", "Antibiótico e reserva renal da idosa (2016 P1 3.5)", ["au-reserva", "au-tfg"]),
   ("p8", "Telomerase evita a senescência; não encurta telômeros (2016 P3 2.5)", ["ak-ttaggg", "ak-telomerase-cancer"]),
   ("p9", "Pneumonia no idoso × aos 40 anos (2015 P1sub 3.6)", ["au-reserva", "ak-vef1"])]),
 ("Palavras-cruzadas (gabarito)", [
   ("c1", "TFG cai à metade aos 90", "au-tfg"), ("c2", "Mutação como causa de senescência", "sh-1792117369568"),
   ("c3", "Somáticas sem telomerase; germinativas com muita", "au-replicativa"), ("c4", "Sirtuínas", "au-sirtuinas"),
   ("c5", "Telômeros", "ak-ttaggg"), ("c6", "Senescência", "au-replicativa"), ("c7", "Lipofuscina", LIPO),
   ("c10", "Werner: DNA helicase", "au-werner"), ("c11", "Senilidade", "au-senescencia"), ("c12", "Elasticidade", "ak-rugas"),
   ("c14", "Turgor", "au-turgor"), ("c15", "Encurtamento", "au-replicativa"), ("c16", "Dose menor de remédios", "ak-tfg-idade"),
   ("c17", "Reserva funcional", "au-reserva")]),
 ("Monitoria P1 aula 3 e apostilas", [("m1", "Cérebro: perdas sem afetar cognição", "ak-inteligencia"),
                                     ("m2", "Valvas: colágeno na matriz", "ak-ea-calcificacao")]),
]
