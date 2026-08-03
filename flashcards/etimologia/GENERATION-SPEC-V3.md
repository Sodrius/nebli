# Especificação de geração v3 — etimologia

Esta especificação incorpora o feedback humano de `reports/pilot_cards.md` e governa o piloto pt2 e a futura geração integral.

## Objetivo de seleção

O deck deve maximizar capacidade de decompor termos inéditos e rigor de linguagem. Frequência isolada não basta.

Prioridade: `Q = 3T + 3C + 2E + 2R + F - 2O`.

- `T`: transferência;
- `C`: risco de confusão;
- `E`: déficit de exposição;
- `R`: reutilização;
- `F`: frequência curricular;
- `O`: obviedade para o estudante.

Raízes óbvias, como `derm/o → pele`, não recebem card isolado sem ganho adicional. Podem sustentar decomposição difícil, contraste ou limite clínico.

## Camadas obrigatórias

1. método morfológico mínimo;
2. famílias e contrastes recuperados em conjunto;
3. morfemas produtivos de baixa exposição;
4. aplicações em termos não usados como exemplo;
5. polissemias, falsas segmentações e limites da etimologia;
6. pares gregos e latinos;
7. linguagem médica discriminativa em semiologia, patologia e farmacologia.

## Gates de cada nota

- Começar por rótulo neutro de 1–2 palavras: `<b>Etimologia.</b>`.
- Texto com até 25 palavras; alvo habitual abaixo de 18.
- Extra geralmente com até 25 palavras; pode chegar a 40 quando um termo novo exige explicação, exemplo ou contexto inicial.
- Uma a três ocorrências de cloze; uma é o padrão. Quatro ou mais são proibidas.
- Resposta com até três palavras; uma palavra é preferível.
- Cloze integralmente em negrito: `<b>{{c1::...}}</b>`.
- Contrastes usam somente `c1`, escondendo todos os membros juntos e gerando um único card.
- Transferências exigem decomposição e interpretação no Extra (`partes = sentido`).
- Termos polissêmicos exigem contexto de sistema ou contraste explícito.
- Termos pouco familiares recebem didática reforçada: definição simples, exemplo concreto e explicação da decomposição, sem pressupor conhecimento clínico prévio.
- O deck preserva uma amostra pequena e deliberada de pares gregos e latinos úteis.
- Toda nota exige ID estável, fonte etimológica, fonte médica e confiança alta.

## Rejeições automáticas

- Extra que apenas repete a frente;
- Extra do tipo `Partes:` sem interpretar o resultado;
- fórmulas genéricas como “referente a”, “preserva esse núcleo” ou “evita trocar”;
- contraste repartido em `c1`, `c2` ou `c3`;
- resposta com mais de três palavras;
- card óbvio sem ganho de transferência;
- definição clínica tratada como consequência necessária da glosa literal;
- múltiplas direções geradas automaticamente;
- fonte ausente ou confiança baixa.

## Gate antes da geração integral

O usuário revisa `reports/pilot_cards_pt2.md`. A geração integral permanece bloqueada até esse retorno. O piloto pt2 fica suspenso no Anki.
