# Revisão Opus — Integração metabólica II (bq33), 11/10/2026

Escopo: 107 notas com `tag:NEBLI::2026-uc03-bioquimica-33-integracao-metabolica-ii` (lidas por AnkiConnect, `notesInfo`). Só leitura. Base: lâminas 54–100 (visual/folha-10…17), slides.txt, provas.txt, guia de veteranos aula 7, Lehninger cap. 23, inventario.py.

Nota de ferramenta: `python3 -m nebli.revisar arquivos-trabalho/deck-aula-uc03-bq33-integracao-ii-2026-10-11` despeja **outro deck** (genética bacteriana, 114 itens, com comentários antigos) e sai com código 1. Por isso a revisão usou AnkiConnect. Conferir o `io/`/manifesto da corrida.

## 1. Erros científicos / afirmações imprecisas

| # | nid | Atual | Problema | Correção proposta |
|---|---|---|---|---|
| E1 | 1791729317887 | Insulin lowers cAMP by inactivating PKA and activating {{c1::phosphodiesterase}} | Causalidade invertida: PKA fica depois do cAMP. Inativar a PKA não baixa o cAMP. Na lâmina 61, "PKA inativa" e "PDE ativa" aparecem lado a lado, mas a PKA cai *porque* o cAMP cai. | Insulin activates {{c1::phosphodiesterase}}, which lowers cAMP and switches PKA off. Extra: - This cancels the glucagon signal |
| E2 | 1791729324061 (Extra) | "…one NAD+ is used in the process" | A tioforase (succinyl-CoA:3-ketoacid CoA transferase) só transfere CoA do succinil-CoA para o acetoacetato. Não usa NAD+. O NAD+ entra na β-hidroxibutirato desidrogenase (β-OHB → acetoacetato, gera NADH). | - This enzyme is absent in the liver, so the liver cannot use ketone bodies / - It transfers CoA from succinyl-CoA to acetoacetate / - Thiophorase is also called succinyl-CoA:3-ketoacid CoA transferase |
| E3 | 1791729321513 (Extra) | "Glycerophosphate is old name for DHAP" | Errado: glycerophosphate = glicerol-3-fosfato, não DHAP. A linha "Whereas metformin decreases gluconeogenesis via activation of AMPK" fica sem sentido (os dois mecanismos não se opõem). | - Glycerophosphate is the old name for glycerol 3-phosphate / - mGPD oxidizes glycerol 3-phosphate to DHAP / - Metformin also activates AMPK. Cor: o mecanismo via mGPD é conexão lateral (prova 2023 sobre glicerol), então é **rosa**, não verde. |
| E4 | 1791729325663 | In type 2 diabetes, insulin resistance appears years before the {{c1::compensatory}} rise in plasma insulin | Fisiologicamente a hiperinsulinemia compensatória vem *junto* com a resistência. O que demora anos é a subida da **glicemia**. A frase da lâmina 99 é uma tradução ambígua. O próprio Extra ("Hyperinsulinemia keeps glucose near normal until the β cells fail") contradiz a frente. O cloze em "compensatory" também é um alvo fraco. | In type 2 diabetes, insulin resistance appears years before blood {{c1::glucose}} rises, because compensatory hyperinsulinemia keeps glycemia near normal. Extra: - Hyperglycemia appears when the β cells can no longer compensate |
| E5 | 1791729325413 | Metabolic syndrome in type 2 diabetes includes obesity, high LDL, low HDL and {{c1::hypertension}} | O LDL alto não é critério da síndrome metabólica (os critérios são TG alto, HDL baixo, PA, glicemia de jejum, cintura). O LDL vem da lâmina 97, mas o card irmão 1791054012847 diz "high triglycerides and low HDL", o que é incoerente dentro do deck. "in type 2 diabetes" dá a entender que a síndrome é parte do DM2. | Type 2 diabetes is associated with metabolic syndrome, which includes obesity, high triglycerides, low HDL and {{c1::hypertension}}. Extra: - The lecture also lists high LDL / - Insulin resistance links these findings |
| E6 | 1791054012847 (Extra) | "i.e., fasting glucose > 100–110 mg/dL" | "i.e." solto, sem referente. Do jeito que está, define a resistência à insulina como glicemia de jejum >100. | - Fasting glucose ≥ 100 mg/dL is one of its criteria |
| E7 | 1791647349695 (Extra) | "Insulin does not change hepatic glucose uptake, which depends on GLUT2" | Amplo demais. A insulina não regula o GLUT2, mas *aumenta* a captação hepática líquida ao induzir a glicoquinase e reter a glicose como G6P (lâmina 60: "retenção da glicose no fígado"). | - Insulin does not regulate GLUT2, but glucokinase traps glucose in the liver as glucose 6-phosphate |
| E8 | 1791647348245 | Muscle cannot participate in gluconeogenesis because it lacks the enzyme {{c1::glucose-6-phosphatase}} | Ideia certa, verbo errado: o que a falta de G6Pase impede é a liberação de glicose livre no sangue. | Muscle cannot release glucose into the blood because it lacks {{c1::glucose-6-phosphatase}} |
| E9 | 1791054011246 (Extra) | "The liver keeps releasing glucose despite hyperglycemia" | Fora de contexto, num card de fisiologia normal, é falso: na hiperglicemia normal o glucagon é suprimido. Só vale no diabetes. | - In diabetes, unopposed glucagon keeps the liver releasing glucose despite hyperglycemia |
| E10 | 1791729320636 | Glucagon causes decreased fatty acid synthesis and increased lipolysis, which shunts substrates towards gluconeogenesis | Ácidos graxos não viram glicose. Da lipólise, o substrato gliconeogênico é só o glicerol. Os AG dão ATP e acetil-CoA (ativador da PC). | Glucagon {{c1::decreases}} hepatic fatty acid synthesis and {{c1::increases}} adipose lipolysis, so fatty acids replace glucose as fuel. Extra: - Only the glycerol from lipolysis is a gluconeogenic substrate |
| E11 | 1791729319038 | Carnitine acyltransferase-1 (CAT1) is regulated via negative feedback by {{c1::malonyl-CoA}} | Não é retroalimentação negativa: malonil-CoA (intermediário da síntese) inibe a entrada de AG na β-oxidação, o que é regulação recíproca. Também falta o "por quê" da lâmina 68. | Malonyl-CoA inhibits {{c1::carnitine acyltransferase I}}, so newly made fatty acids are not oxidized |
| E12 | 1791647350296 | Hormone sensitive lipase is regulated via negative feedback by {{c1::insulin}} | Mesmo erro de termo: a insulina inibe a HSL, não há alça de retroalimentação. | {{c1::Insulin}} inhibits hormone-sensitive lipase in adipose tissue |
| E13 | 1791729319338 | In the {{c1::liver::organ}}, the HMP shunt provides a source of NADPH for biosynthesis of fatty acids, cholesterol, and steroids | Resposta não é única: o adiposo também faz pentoses e lipogênese (lâmina 73), e esteroides são adrenal e gônadas, não fígado. | In the fed liver, the pentose phosphate pathway supplies the {{c1::NADPH}} consumed by fatty acid synthesis. Ou suprimir, porque 1791729319463 já cobre o mesmo item. |
| E14 | 1791729319463 | Insulin increases the activity of {{c1::glucose-6-phosphate dehydrogenase}}… | A lâmina 69 diz que a síntese de AG (NADP+ gerado) ativa a via das pentoses. A G6PD é regulada sobretudo pela razão NADP+/NADPH. A insulina só induz a enzima a longo prazo. | The NADP+ released by fatty acid synthesis activates {{c1::glucose-6-phosphate dehydrogenase}}, the first enzyme of the pentose phosphate pathway. Extra: - Insulin also induces this enzyme in the fed state |
| E15 | 1791054012320 | glucose retained in the renal tubules causes {{c1::osmotic diuresis}} | "retained in the renal tubules" sugere acúmulo no epitélio. É a glicose não reabsorvida no fluido tubular. | Glucose filtered above the renal threshold stays in the tubular fluid and causes {{c1::osmotic diuresis}} |
| E16 | 1791054010747 (Extra) | "glucose is stuck in the blood and can't get into cells" + "→ no insulin- DKA" (linhas fundidas) | Amplo demais (cérebro, hemácias e fígado captam glicose sem insulina). Formatação quebrada. | - Without insulin, muscle and fat cannot take up glucose and lipolysis is unchecked / - The liver turns the fatty acids into ketone bodies |
| E17 | 1791729322786 | TAG … can fuel basal metabolism for about {{c1::three months}} | Lehninger (Tab. 23-5) dá ~3 meses para o **total** de combustíveis. Só o TAG (140 mil kcal ÷ 1.800 kcal/dia) dá ≈ 2,5 meses. Pequeno, mas o card atribui ao TAG o que o livro atribui ao total. | The fuel stored in a normal-weight adult, mostly adipose triacylglycerols, can sustain basal metabolism for about {{c1::three months}} |
| E18 | 1791647354296 (baixa prioridade) | GLUT-2 into the pancreatic β cell | Fiel à figura (Lehninger), mas na célula β **humana** predomina o GLUT1. O GLUT2 é o de roedor. | Manter o card; Extra: - In human β cells GLUT1 predominates; GLUT2 is the classic rodent transporter. Sem ';' isso fica em duas linhas: "- Human β cells rely mainly on GLUT1" |

## 2. Ambiguidade ou resposta dada na frente

| nid | Problema | Correção |
|---|---|---|
| 1791054012596 | "As β-cell function declines…, insulin secretion {{c1::decreases}}": a frente dá a resposta. Também é duplicata de 1791729325288. | Suprimir (manter 1791729325288). |
| 1791729317038 | A frente já diz "closure of select K+ channels with consequent membrane depolarization", que é a resposta de 1791729317165. | In the pancreatic β cell, glucose metabolism raises the cytosolic {{c1::ATP}}/ADP ratio. Extra: - Glucokinase makes this rise proportional to blood glucose |
| 1791729317338 | c2 "open… {{c2::increase}}": o "increase" é óbvio pelo "open". Ca2+ aparece duas vezes no c1. | Depolarization of the β cell opens voltage-gated {{c1::Ca2+}} channels, and the Ca2+ influx triggers insulin release |
| 1791729323138 | c1 "muscle": a resposta poderia ser heart (as lâminas 89/90 mostram coração). | Ketone bodies are used for energy by the {{c2::brain}} in starvation and by {{c1::heart and skeletal muscle}} |
| 1791054011119 (Extra) | "Without insulin, glucagon is unopposed" é a resposta de 1791054011545. | Trocar por: - Hyperglycemia and somatostatin also suppress glucagon |
| 1791054010222 (Extra) | Lista T1 = absoluta e T2 = resistência + relativa, que é a resposta de 1791729324668. | - Both types share hyperglycemia and its chronic complications |
| 1791647352896 / 1791729322913 / 1791729323313 | Os Extras de 352896 e 322913 trazem "spares … muscle protein", que é o cloze de 323313. | 352896 Extra: - Ketone bodies cross the blood-brain barrier. 322913 Extra: - Plasma ketone bodies rise over days while glucose falls (lâmina 88). |
| 1791729321990 (Extra) | "e.g., alanine aminotransferase (ALT) or aspartate aminotransferase (AST)" fica solto. | - Alanine aminotransferase moves the amino group onto pyruvate |
| 1791054015196 (Extra) | "Glycation is non-enzymatic…" repete a frente. | - HbA1c reflects mean glycemia over about 3 months |
| 1791729316911 (Extra) | "The amino acids go to the liver for gluconeogenesis" repete a frente. | - Glucocorticoids are catabolic for muscle and anabolic for the liver |

## 3. Lacunas (lâminas 54–100 e provas)

| Item da base | Situação | Card proposto |
|---|---|---|
| L94: tratamento do DM1 (insulina diária, dieta, exercício, ajuste de dose) | Inventário mapeia para `t1-idade`, que não cobra o item | Type 1 diabetes requires daily {{c1::insulin}} injections with dose adjustment, diet and exercise |
| L93: DM1 sintomas (polidipsia, poliúria, polifagia, emagrecimento) | Só no Extra (menção não conta) | Untreated type 1 diabetes causes polyuria, polydipsia, polyphagia and {{c1::weight loss}} |
| L93: DM2 início insidioso, às vezes assintomático ou diagnosticado por complicações crônicas | Sem card | Type 2 diabetes often begins {{c1::insidiously}} and may be diagnosed only through its chronic complications |
| L68/82 + guia cap. 5 + prova 2024: no jejum a ACC é inativada → malonil-CoA cai → CAT I libera a β-oxidação | Só o lado absortivo tem card | In fasting, inactive acetyl-CoA carboxylase lowers {{c1::malonyl-CoA}}, so carnitine acyltransferase I lets fatty acids into the mitochondria |
| L68: insulina ativa a ACC (desfosforilação) | Só em Extra | Insulin activates {{c1::acetyl-CoA carboxylase}} by dephosphorylation, committing acetyl-CoA to fatty acid synthesis |
| L66: ATP/NADH altos inibem a isocitrato desidrogenase → citrato acumula e sai | Só em Extra (2×) | In the fed liver, high ATP and NADH inhibit {{c1::isocitrate dehydrogenase}}, so citrate accumulates and exits to the cytosol |
| L77 + prova 2024: glucagon → cAMP → PKA → fosforilase-cinase ativa e glicogênio sintase inativa | Sem card no bq33 nem no bq25 | In fasting, PKA activates {{c1::phosphorylase kinase}} and inactivates glycogen synthase |
| L62/78: F-2,6-BP ativa a PFK-1 e inibe a FBPase-1 | Existe em bq25 (4 cards com PFK-1), não compartilhado | Compartilhar 1 card de bq25 pela tag de cor bq33 (sem cópia) |
| L95: proteínas glicadas perdem a atividade | HbA1c cobre a glicação, não a perda de função | Excess glucose glycates proteins non-enzymatically and {{c1::impairs their function}} |
| L96: DM2 >90% dos casos | Só em Extra | Type 2 accounts for more than {{c1::90}}% of diabetes cases (verde/azul) |

## 4. Fuga (não ensinado na aula)

- 1791054010347 "type 1 has a {{c1::weaker}} genetic predisposition": a aula diz DM1 = HLA e "susceptibilidade genética" (lâm. 94), DM2 = poligênica. Comparar a força da predisposição não está na base e conflita com a leitura da lâmina 94. Mover para o Extra de 1791729324792 ou rebaixar para rosa. O Extra "Environmental triggers matter more in type 1" é discutível: tirar.
- 1791054010997 (CD8+ T): a aula diz só "autoimune". Está verde no bq33. Rebaixar para azul/rosa nesta aula (o verde vale para o GR21).
- 1791729319161 (CPT1 no espaço intermembranas, rosa): a aula só cita a inibição da CAT I. Topografia e "conflicting sources" fogem dela. Suprimir no bq33 ou deixar só como compartilhado de outra aula.
- 1791647349946 (Extra): a lista de LPL, lipase hepática e pancreática é carga fora da aula. Cortar para: - It releases fatty acids and glycerol into the blood.
- 1791729319338 (HMP com esteroides): ver E13.

## 5. Duplicatas internas

- 1791054012596 ≈ 1791729325288 (falência β): suprimir 012596.
- 1791647350421 (glicerol → gliconeogênese, Extra "glycerol kinase") ≈ 1791729321388 (cloze glycerol kinase). Manter os dois, trocar o Extra de 350421 por: - Glycerol enters as dihydroxyacetone phosphate.
- 1791729318437 e 1791729318861: Extras com o mesmo parágrafo (ATP inibe isocitrato DH, citrate shuttle). Cortar o do 318861 para: - Citrate allosterically activates this enzyme, and insulin dephosphorylates it.
- "The liver makes/exports ketone bodies but cannot use them" se repete em 5 Extras (1791647349321, 1791729323438, 1791729323812, 1791729323138, 1791729324238). Deixar só no card da tioforase/fígado.
- 1791729324668 ≈ 1791054010222 Extra (ver seção 2).

## Redação AnKing (menor)

- 1791054013770 "a(n) biguanide" → "a biguanide".
- 1791729316389 Extra "Insulin is the hormone of storage: it also…" e 1791729316613 Extra "…mirror each other: the ratio…": tirar o ':' e quebrar em duas linhas.
- 1791647349946 Extra: "cylomicron" → chylomicron.
- 1791729322238 Extra: linhas fundidas ("gluconeogenesis- Alanine") e "G3P" ambíguo → glycerol 3-phosphate.

## Resumo

- Erros científicos e imprecisões: **18** (E1–E18). Graves: E1, E2, E3, E4, E5. Médios: E6–E14. Menores: E15–E18.
- Ajustes de redação, ambiguidade e vazamento: **14** (10 na seção 2 + 4 menores).
- Lacunas: **10**.
- Fugas: **5**. Duplicatas: **5** grupos.

### Correções a aplicar, por prioridade

1. E1 1791729317887: inverter a causalidade (PDE → cAMP ↓ → PKA off).
2. E2 1791729324061: tirar "one NAD+ is used" do Extra da tioforase.
3. E3 1791729321513: corrigir "glycerophosphate = DHAP" e a frase do AMPK, e passar o card para rosa.
4. E4 1791729325663: resistência anos antes da *glicemia* subir, com cloze em glucose.
5. E5/E6 1791729325413 e 1791054012847: critérios da síndrome metabólica (TG/HDL) e Extra "i.e." solto.
6. Lacunas DM: tratamento do DM1, sintomas do DM1, início insidioso do DM2.
7. Lacunas de jejum: ACC inativa → malonil-CoA ↓ → CAT I livre, e PKA → fosforilase-cinase / sintase inativa.
8. E10, E11, E12: glucagon/lipólise "shunts substrates", e "negative feedback" (CAT1, HSL).
9. E7, E8, E9: GLUT2/glicoquinase, músculo sem G6Pase, Extra do glucagon fora de contexto.
10. Suprimir 1791054012596 (duplicata que dá a resposta). Reescrever 1791729317038 e 1791729317338.
11. E13/E14: HMP no fígado ambíguo, e G6PD ativada por NADP+ (lâmina 69).
12. Limpar os Extras que vazam respostas (seção 2) e as repetições "liver cannot use ketones".
13. Fugas: rebaixar 1791054010347 e 1791054010997, e tratar 1791729319161.
14. Lacunas menores (isocitrato DH, ACC/insulina, glicação com perda de função, >90%, compartilhar F-2,6-BP/PFK-1 do bq25).
15. Menores: E15–E18 e a redação.
16. Ferramenta: `nebli.revisar` dessa corrida despeja outro deck. Corrigir antes da próxima revisão.
