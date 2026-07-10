# Mapa de Confusões — Ciclo de Krebs

**Slug:** `ciclo-krebs` · **Aula UC01:** `bioq-17-ciclo-krebs-TE-I` · **Versão:** 2026-05-25 (rev. para formato canônico do validador)

Catálogo dos erros mecanísticos típicos do tema. Distratoras da E2 puxam DESTE arquivo.

## 1.1 Por que o piruvato não entra direto no ciclo

1. **Acetil-CoA atravessa a membrana mitocondrial interna** — falso. Não há transportador para acetil-CoA. O que atravessa é o citrato (via transportador tricarboxilato), clivado no citosol pela ATP-citrato liase. *Origem: q-0312.*
2. **PDH é parte do ciclo de Krebs** — falso. PDH é a porta de entrada; o ciclo começa formalmente na citrato sintase. O NADH da PDH não é "do ciclo", é da reação preparatória. *Origem: q-0320.*
3. **O piruvato atravessa por difusão simples** — falso. Usa transportador específico (MPC, monocarboxylate pyruvate carrier) em simporte com H⁺. *Origem: livro.*
4. **Os 2 CO₂ saem da reação da PDH** — falso. PDH perde 1 CO₂ (antes do ciclo); os outros 2 CO₂ saem nos passos 3 e 4 do ciclo (IDH e α-KGDH). *Origem: q-0288, q-0320.*

## 1.2 Complexo PDH: 3 enzimas, 5 coenzimas

1. **PDH usa só NAD⁺ como cofator** — falso. Usa cinco coenzimas: TPP, ácido lipóico, CoA, FAD, NAD⁺. *Origem: q-0288.*
2. **E1 reduz NAD⁺** — falso. Quem reduz NAD⁺ é o E3. E1 descarboxila o piruvato via TPP. *Origem: banco NEBLI.*
3. **O grupo acetila sai do complexo como aldeído** — falso. Sai como tioéster acetil-CoA — ligação rica em energia (~31 kJ/mol). *Origem: livro.*
4. **As 5 coenzimas da PDH só servem aqui** — falso. As mesmas 5 (TPP, ácido lipóico, CoA, FAD, NAD⁺) aparecem no passo 4 do ciclo (α-KGDH, mecanismo idêntico). *Origem: q-0288.*

## 1.3 Beribéri e Wernicke (vit B1)

1. **B1 deficiency só afeta a PDH** — falso. Paralisa PDH E α-KGDH. Daí o quadro de Wernicke (cérebro depende de glicose oxidativa). *Origem: integração clínica.*
2. **Em deficiência de tiamina o lactato cai** — falso. Sobe. Sem PDH, piruvato acumula e vira lactato pela LDH — acidose láctica. *Origem: livro.*
3. **Alcoolista hipoglicêmico recebe glicose primeiro** — *invertido e perigoso*. Tiamina vem antes. Glicose pura em paciente B1-depletado precipita Wernicke agudo. *Origem: regra prática de PS.*
4. **B1 = B12** — falso. B1 (tiamina) entra em PDH e α-KGDH. B12 (cobalamina) entra na metionina sintase e na metilmalonil-CoA mutase — não toca em Krebs. Deficiência de B12 dá anemia megaloblástica + degeneração combinada subaguda da medula. *Origem: livro.*

## 2.1 Visão geral e saldo por volta

1. **Saldo por volta = 2 NADH** — falso. São 3 NADH (IDH, α-KGDH, MDH) + 1 FADH₂ (SDH) + 1 GTP + 2 CO₂. *Origem: q-0169, q-0288, q-0320.*
2. **Saldo da PDH é "do ciclo"** — falso. Os 2 NADH da PDH (por glicose) vêm antes do ciclo começar. Por glicose: 2 NADH (PDH) + 6 NADH (ciclo, 2 voltas) + 2 NADH (glicólise). *Origem: q-0169.*
3. **Glicose aeróbica = 36 ATP exatos** — número antigo. Valor moderno: 30–32 ATP (depende do shuttle citosólico do NADH glicolítico). *Origem: q-0169.*
4. **NADH citosólico da glicólise entra direto na mitocôndria** — falso. Membrana interna é impermeável a NADH. Os elétrons entram via shuttle malato-aspartato (mantém como NADH na matriz, ~2,5 ATP) ou glicerol-3P (entrega como FADH₂ via UQ, ~1,5 ATP). *Origem: q-0388.*

## 2.2 Passos 1–4: condensação, isomerização, oxidações

1. **Citrato sintase consome ATP** — falso. Não consome. A energia vem da hidrólise da ligação tioéster do acetil-CoA. *Origem: livro.*
2. **Fluoracetato bloqueia diretamente a aconitase** — parcialmente falso. Mecanismo: fluoracetato → fluoracetil-CoA → fluorocitrato (via citrato sintase) → inibe aconitase. Síntese letal. *Origem: slide 21, livro.*
3. **Isocitrato desidrogenase usa FAD** — falso. Usa NAD⁺. FAD aparece só na SDH no ciclo (e indiretamente em E3 da α-KGDH). *Origem: livro.*
4. **α-KGDH é uma enzima simples (monomérica)** — falso. É um complexo análogo à PDH (3 enzimas, mesmas 5 coenzimas: TPP, ácido lipóico, CoA, FAD, NAD⁺). *Origem: q-0288.*

## 2.3 Passos 5–8: GTP, SDH, OAA

1. **GTP do passo 5 = 2 ATP** — falso. 1 GTP equivale a 1 ATP (convertido por nucleosídeo difosfato quinase). *Origem: q-0288.*
2. **SDH está na matriz** — falso. SDH é a única enzima do ciclo embutida na membrana mitocondrial interna — é o Complexo II da cadeia respiratória. *Origem: q-0157, q-0388, q-0400.*
3. **FADH₂ rende mesmo ATP que NADH** — falso. FADH₂ ~1,5 ATP, NADH ~2,5 ATP. Diferença mecanística: FADH₂ entra na cadeia mais a jusante (via Complexo II/UQ), bombeia menos H⁺. *Origem: q-0157, q-0388.*
4. **MDH não roda porque ΔG⁰' positivo** — falso. Roda por princípio de Le Chatelier: citrato sintase consome OAA imediatamente, puxando a reação para frente. Razão NAD⁺/NADH alta também favorece. *Origem: livro.*

## 2.4 Regulação por carga energética

1. **ATP ativa o ciclo** — invertido. ATP INIBE o ciclo (sinal "energia OK, freia"). ADP/AMP ATIVAM. *Origem: livro.*
2. **Oligomicina/cianeto inibem enzima do ciclo diretamente** — falso. Bloqueiam ATP-sintase / Complexo IV. Cadeia para → NADH acumula → NAD⁺ desaparece → IDH/α-KGDH/MDH ficam sem aceptor → ciclo para por falta de NAD⁺. *Origem: q-0312, q-0325, q-0387.*
3. **Desacoplador = mesmo efeito que oligomicina** — falso. DNP faz o oposto: colapsa gradiente, ciclo dispara, O₂ sobe, ATP cai. Hipertermia. *Origem: q-0312, q-0325.*
4. **Ca²⁺ inibe o ciclo** — falso. Ca²⁺ na matriz ATIVA IDH e α-KGDH. Sinal de "contração começou, preciso de mais ATP" — feed-forward. *Origem: livro.*

## 3.1 Krebs como hub biossintético

1. **Krebs é só catabolismo** — falso. É anfibólico — cede α-KG (glutamato), OAA (aspartato), succinil-CoA (heme), citrato (acetil-CoA citosólico → AG). Toda saída drena OAA. *Origem: q-0211, q-0388.*
2. **Citrato sai da mitocôndria para virar ATP no citosol** — falso. Citrato sai para virar acetil-CoA citosólico (síntese de AG e colesterol). Saída anabólica. *Origem: livro.*
3. **α-KG só serve para virar succinil-CoA** — falso. α-KG sai do ciclo para virar glutamato (e a partir dele, glutamina, prolina, arginina). Entrada catabólica de muitos aminoácidos. *Origem: livro.*
4. **Succinil-CoA só serve para virar succinato** — falso. Succinil-CoA é precursor obrigatório de porfirinas (heme da hemoglobina, citocromo, catalase). *Origem: livro.*

## 3.2 Anaplerose e piruvato carboxilase

1. **Anaplerose significa retirar intermediários** — falso. Anaplerose ("preencher de novo") significa REPOR. O contrário é cataplerose. *Origem: livro.*
2. **Piruvato carboxilase usa piruvato + acetil-CoA como substratos** — falso. Usa piruvato + HCO₃⁻ + ATP. Acetil-CoA é o ATIVADOR alostérico (sem ele, enzima virtualmente inativa). *Origem: q-0211.*
3. **AG par é anaplerótico** — falso. β-oxidação de AG par gera só acetil-CoA, que entra com 2C e sai como 2 CO₂ — saldo líquido = 0. AG ímpar repõe (via propionil-CoA → succinil-CoA, B12-dependente). *Origem: livro, integração com gliconeogênese.*
4. **Piruvato carboxilase está em todos os tecidos igualmente** — falso. Restrita a fígado e rim. Por isso músculo não consegue fazer gliconeogênese a partir de piruvato. *Origem: livro.*

## 3.3 Jejum prolongado e cetose

1. **Cetoacidose por excesso de glicose** — invertido. Cetoacidose por falta de OAA disponível (drenado pela gliconeogênese em jejum/DM1). Sem OAA, acetil-CoA da β-oxidação vira corpo cetônico. *Origem: integração clínica.*
2. **"AG queima na fogueira dos carboidratos" = exigência energética** — falso. A fogueira é OAA. Sem carboidrato → sem piruvato → sem piruvato carboxilase → sem OAA → sem combustão completa. *Origem: integração clínica.*
3. **Em jejum bem adaptado, o cérebro continua dependendo só de glicose** — falso. Após 2–3 semanas o cérebro adapta transportadores e passa a queimar corpos cetônicos como combustível principal, poupando glicose. *Origem: livro.*
4. **DKA = cetose patológica por excesso de insulina** — invertido. DKA é por insulina baixa/ausente em DM1 — lipólise descontrolada, β-oxidação em torrente, OAA drenado, acetil-CoA → cetônicos em quantidade que ultrapassa o tamponamento sanguíneo. *Origem: integração clínica.*
