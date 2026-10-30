# Retomar — deck-prova UC19 lote 2 (Farmacocinética)

Modelo vivo: `arquivos-trabalho/deck-prova-uc19-1-farmacodinamica-2026-10-30` (base-prova.json, planejar.py, spec.py, excluidos.py,
evidencias.py, contexto.py, revisao.py, retirar_antigo.py — copiar e adaptar, na mesma ordem).

Regras novas (30/10): F-20261030-CLAUDE-01 — nota AnKing HY 1–2 das seções da prova só sai por `duplica <nid>` ou `lote-N` (gate
`deck_prova`); escolher SECOES só do assunto (seções de fisiologia/autonômico ampla ficam fora, com SECOES_MOTIVO).
Mudar deck só com o nome canônico do plano DENTRO de `nebli.decks.escrita` (lição do lote 1).

## Feito
- E0 registrada; fontes copiadas para fontes/ e fontes/laminas/ (fc1, fc2, oral, tipos, clearance2); canais/ninja-pk-absorcao.txt
  (lido integral na FC03) e livros/rang-cap8-9.txt copiados da FC03.
- Lidos nesta sessão (30/10): apostila p. 11–21 inteira; questões orientadoras FC 1–40 com gabarito; De Nucci cap. 1 INTEIRO (18 p.).
- De Nucci acrescenta ao lote 2: compartimentos de água (60/40/15/5%), Vd de vários fármacos (quinacrina 40.000 L … eritropoietina 5 L),
  aminofilina IT estreito e dose por Vd; peso molecular > 1.000 não atravessa; lipofilicidade (coeficiente octanol/água); ligação a
  proteínas (>0,9 extensa; ácidos/neutros → albumina, básicos → α1-glicoproteína ácida; fu; deslocamento 99,9→99,8% dobra a livre;
  propranolol: fu varia com α1-GPA, mais fu → maior Vd); transportadores (SLC × ABC; OCT secreta cátions no túbulo proximal; OAT
  ânions: betalactâmicos, diuréticos, AINH; P-gp: MDR1, apical, limita absorção, protege BHE/testículo/placenta, excreta na bile/urina,
  só relevante se transporte ativo > difusão); BHE (tight junctions, sem fenestras; fenobarbital e fenitoína substratos de P-gp);
  clearance (E = (Ca–Cv)/Ca; Cl = E × fluxo; alta E fluxo-dependente, baixa independente; R0 = Cl × Css); rim (32% dos 200 mais
  prescritos são renais; renal se > 25% inalterado; secreção por transportador de cátions/ânions); Cockcroft-Gault ((140–idade)×peso/
  creatinina; superestima em IRA, cirrose e obesidade); pH urinário (ácido fraco ionizado em meio alcalino: bicarbonato aumenta
  clearance de salicilato; metanfetamina pKa 9,9 aumenta com acidificação); metabolismo: funcionalização × conjugação, CYP e UGT > 90%;
  pró-fármaco (enalapril → enalaprilato; tenofovir TDF/TAF; codeína → morfina pela CYP2D6; morfina-glicuronida ativa); CYP2D6
  (nortriptilina varia 100×, cópias do gene); varfarina S pela CYP2C9 (*3/*3 lenta), R pela 3A4; fatias CYP (3A4/5 36%, 2D6 21%,
  2C8/9 17%, 1A2 8%, 2C19 8%, 2E1 4%); UGT (glicuronidação, retículo liso; UGT1 e UGT2); outras: esterases, MAO, FMO, NAT.

## Recorte do lote 2 (blocos)
6 Química e membranas (HH, pKa, ionização, captura iônica, lipossolubilidade, transporte) · 7 Vias e medicamentos (vias enteral,
parenteral, outras; formas, liberação modificada, depósito/glargina, PEG; referência/genérico/similar; equivalência × bioequivalência,
ASC e Cmáx) · 8 Absorção e biodisponibilidade (F, primeira passagem, P-gp, fatores) · 9 Distribuição (compartimentos 4/14/42 L,
ligação a proteínas, fu, albumina × α1-glicoproteína ácida, redistribuição, BHE, placenta, Vd e t½) · 10 Metabolismo (fase I/II,
CYPs, indução: rifampicina, fumo-CYP1A2; inibição: cetoconazol, claritromicina, toranja, dissulfiram-2E1; pró-fármaco clopidogrel-2C19
+ omeprazol; NAT2; idade; Child-Pugh) · 11 Excreção e clearance (Cl = E × Q, alta × baixa extração, aditividade, taxa = Cl × C,
filtração/secreção/reabsorção, pH urinário, inulina, creatinina, cilastatina, êntero-hepático).
Lote 3: ke, t½, bolus, infusão/Css, dose de ataque, doses repetidas, MRT, oral (ka), ordem zero, saturação.

## Questões que vão para o lote 2 (orientadoras FC)
2–7, 9, 10, 11–20, 21–30, 36–40 (as de cálculo 1 e 8 e as de cinética 31–35 → lote 3).
Banco "Todas as questões" (fontes/todas-questoes.pdf, 91 p.): ler inteiro e dividir FC qualitativa (lote 2) × quantitativa (lote 3).

## Próximo
Terminar De Nucci (a partir de "Ligação às proteínas plasmáticas"), ler o banco, base-prova.json, E1–E8 como no lote 1.

## Banco "Todas as questões" — leitura
- p. 1–28 lidas (30/10). Qualitativas para o lote 2: 1º passagem (G1TA q1), vias IM/SC/IV/aérea/oral (G1TB q1, p.5 q2–3, p.23 q5),
  P-gp + loperamida (G1TB q2), bioequivalência digoxina (G1TB q4), ligação a proteínas (G1TB q5, p.27 q3), lidocaína + epinefrina
  (G1TB q6), propranolol e α1-GPA na nefropatia (p.5 q1), primeira passagem por oxidação (p.5 q5), peso molecular/lipofilicidade
  (G2 q1), Vd aparente > corpo (G2 q4), alcalinização da urina (p.9 q1), clearance definição (p.9 q4), sublingual × bucal (G3TB q5),
  morfina oral × IV × M6G (G4TA q5), furosemida ligada a proteínas e Vd baixo (G4B q1), dipirona e insuficiência (G4B q4),
  placebo/nocebo (p.20 q1), biodisponibilidade (p.20 q2, q4), ITU e fármaco renal (p.20 q3), tipos de medicamento (p.23 q2, p.25),
  fatores da PK (p.26). Cálculo → lote 3: G1TA q2–5, p.5 q4, G2 q2–3, q5, p.9 q2, q5, G3TB q1–4, G4TA q1–4, G4B q2–3, q5, p.23 q1, q3–4,
  p.25 meia-vida, p.27 q1–2, q4.
- p. 28–54 lidas. Lote 2: AUC significa extensão da absorção (G7TA q2), bioequivalência/tipos (G7TA q3, G8 q5 Cialis/tadalafila,
  107B q15), inconsciente → IV/SC/IM (G7TA q4), via pulmonar sem 1ª passagem grande (G7TA q5), pKa clorotiazida estômago (G7TB q3),
  biodisponibilidade máxima lipofílico solúvel (G7TB q4), conjugação aumenta hidrossolubilidade (p.32 q1), vômito → via parenteral
  (p.32 q2), desafios da via oral/alimento (p.32 q3), Vd por dose/C0 (p.32 q4 → lote 3), interação oral×IV (p.34–37), 1ª passagem e
  drenagem portal/gastrorresistente (p.35 q3), ciclo êntero-hepático inclui metabólitos (p.35 q4), alimentos (p.35 q5), Questões 104/105
  (sublingual evita 1ª passagem, metanfetamina pKa, interação, PK × PD, solubilidade para absorção, P-gp e toranja, benzodiazepínicos
  lipossolúveis, alendronato, rifampicina reduz anticoncepcional), 107B: hemodiálise só para Vd baixo (q1), biodisponibilidade (q2),
  meia-vida longa → equilíbrio demora (q3 → lote 3), direcionamento (q4), taxa = Cl × C (q5), genérico não altera absorção (q6),
  vias (q8), fatores de biodisponibilidade (q9, q16), perdas na luz/parede/fígado (q11), rifampicina × varfarina (q12), fluvoxamina ×
  cafeína (q13, inibição CYP1A2), excreção: líquido peritoneal não (q18), propriedades que influenciam absorção (q19), efeito local (q20).
- p. 54–91 lidas: banco INTEIRO lido em 30/10. Lote 2 também: intercambiável = bioequivalente (107B 22), IV e precipitados (p.60 q4),
  absorção passiva de lipídico não ionizado (q5), genéricos/ANVISA (p.58–59), bioequivalência = Tmax e F parecidos (24), F depende do
  paciente/acloridria (25), absorção não é filtração (26), enteral = oral + sublingual (27), Cl serve para taxa de infusão (28 → lote 3),
  via arterial para tumores (29), codeína pró-fármaco (p.63), F absoluta 0 (12), partição pelo pH/lipossolubilidade (13, 35), liofilização
  (14), sublingual não exige dose maior (17), hemodiálise só Vd pequeno (18 e), idosos/crianças/placenta (21), Vd aparente (22),
  reciclagem intracelular não afeta F (23), biotransformação no fígado (24), pKa e absorção no estômago (25), genérico × referência (26,
  38), PK = ADME (39, p.79 q3), clearance aditivo (40), 4 compartimentos sangue→VRG→músculo→gordura (41), biotransformação favorece
  eliminação (42, 45), F absoluta × relativa (46), evitar 1ª passagem por IV/SC (p.78 q1), partição na gordura/morfina/tiopental/amiodarona
  (q2), dose de ataque (q5 → lote 3), fração ligada não é ativa; albumina prefere ácidos (q7), coeficiente de partição não sai do gráfico
  (q8), clearance soma órgãos (q10), referência/genérico (q11–12), benzodiazepínicos/alendronato/rifampicina-anticoncepcional (p.84),
  metanfetamina e urina ácida (p.87 q1), varfarina × AAS por proteínas não é inerte (q2), toranja inibe P-gp (p.89 q3).
