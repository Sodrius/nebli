# Revisão de qualidade — Operon em procariotos (UC03 P2, Biologia Molecular, aula 29)

Corrida `uc03-operon-20261001a`, Claude, 01/10/2026. Refeito do zero a pedido de Davi (F-20261001-CLAUDE-08/09); o deck de 24/09 (51 cards) já estava apagado da coleção quando a sessão começou e não foi restaurado. Critérios: MEMORY + FEEDBACKS até F-20261001-CLAUDE-09 + EXECUCAO-DECK-AULA.

## Escopo e fontes
- **Consultadas:** slides da aula (46 lâminas, `fontes/slides.pdf`, texto de todas e imagem de todas as lâminas só-figura); exercícios da aula 29 (`fontes/exercicios.pdf`); P2 antigas de BM no índice `referencias-externas/uc03/provas-questoes.json` (2019 q2.6–2.9, 2024 q1.12–1.13, 2025 q1.9).
- **Não consultadas:** livro (Harper não localizado; Berg/Lodish não abertos nesta corrida) e vídeos. Os autorais foram conferidos contra os slides e o gabarito das provas, não contra livro. A lista de vídeos de 24/09 continua em `deck-aula-operon-procariotos-2026-09-24/VIDEOS.md` (títulos/capítulos, não assistidos).
- **E1:** não incluída; o pedido foi o deck de cards.

## Cobertura (todos os blocos da aula)
| Bloco | Slides | Cards |
|---|---|---|
| A. Níveis e lógica da regulação (negativa/positiva, cis/trans, indutor, co-repressor) | 3–12 | 13 |
| B. Operon, mRNA policistrônico, promotor e operador | 4, 7, 13–14, 33 | 10 (+1 associado: promotores ricos em AT) |
| C. Operon lac: genes, indução, alolactose, basal | 15–20, 34 | 13 |
| D. Mutantes e ferramentas (lacI−, Oc, lacIS, lacZ−, lacY−, P−, IPTG, X-gal, merozigoto) | 21–25; exercícios 4–5 | 9 |
| E. Diploide parcial: dominância, cis e trans | 26–29; exercício 3 | 4 |
| F. Estrutura do repressor (tetrâmero, HTH, alosteria) | 30–32 | 3 |
| G. Glicose, cAMP, CAP, quatro cenários, repressão por catabólito | 35–37, 44–46; exercícios 2 e 6 | 12 |
| H. Promotor bacteriano, σ, consenso, promotor fraco, recrutamento da RNAP | 38–45 | 7 |

Fora do recorte e exclusões com motivo: `plan.json` → `fora_do_recorte` e `excluidos`. Todo item das P2 antigas de BM tem card (componentes do operon, com/sem lactose, glicose/cAMP/CAP, IPTG e X-gal, Oc no diploide: dominante, constitutivo, cis; mutantes de CAP/sítio CAP).

## Busca e autoria
Ordem pedida em F-20261001-CLAUDE-09: AnKing → outros acervos → AnatoKing/MCAT → autoral. Duas rotas (texto com ~65 termos em `deck:Referências*` e `deck:NEBLI*`; tags First Aid 09_Lac_operon / Bootcamp 06_Lac_Operon), candidatos em `busca/candidatos.json` e `candidatos2.json`. Resultado: AnKing Step tem 7 notas do lac + policistrônico, Shine-Dalgarno, mutação de promotor e AT-rich; nos demais acervos só o MCAT tem operon (12 notas usadas); Histology, Dope, BlueLink, AnatoKing etc. não têm o tema.
**Autoria: 39 de 74 cards (53%), acima do sinal de 20%.** Motivo conferido, não cota: a aula é a genética de Jacob e Monod (mutantes, diploide parcial, cis/trans, IPTG/X-gal, σ e consenso do promotor), que não existe em nenhum acervo instalado (zero resultado para IPTG, X-gal, merodiploid, partial diploid, cis-/trans-acting, helix-turn-helix, sigma factor). Cada autoral tem `autoria` e `busca` no plano.

## Forma dos autorais
- `nebli.lint_cards plan.json`: 38 autorais, 0 reprovação dura (1 aviso: contraste negativo×positivo com dois clozes, mantido porque o contraste é o alvo).
- Amostra cega, rodada 1 (`card-mirror-blind-round1.txt`, 38 autorais + 38 AnKing): identificados com confiança 75–90; tells: cauda “because/so/which” na frente, aposto explicativo, Extra em frase. **Todos reescritos** (`spec-v1-antes-card-mirror.py` guarda a versão anterior).
- Rodada 2 (`card-mirror-blind-round2.txt`, autorais + AnKing/MCAT do mesmo tema + 20 AnKing): confiança caiu para 52–82; veredito “parcialmente distinguível”; tells restantes: famílias de frase gêmea, notação de mutantes, hint que lista opções, Extra que cita card irmão. Os 8 apontados foram reescritos. **Não houve rodada 3:** o conjunto final não foi rejulgado às cegas, e a notação de mutantes continua denunciando o tema.
- O juiz foi um subagente Sonnet com a especificação `.claude/agents/card-mirror.md` (o tipo `card-mirror` não estava disponível nesta sessão).

## Bandeiras
34 verdes (46%), 33 azuis, 7 rosas. Verde: núcleo do modelo, os alvos cobrados nas P2 e os mecanismos centrais (σ, recrutamento pela CAP, basal). Azul: básico de apoio, sentido inverso, exercícios da aula, estrutura do repressor. Rosa (`NEBLI::lateral`): Jacob e Monod, lacA, tetrâmero, CRP, consensos TATAAT/TTGACA, αCTD. Nenhum card do AnKing lac é HY no v12 (todos 4-LowerYield); verde veio do peso na aula e na prova. Cor por aula em `NEBLI::cor::2026-uc03-biomol-29-operon-procariotos::*`, inclusive no associado (azul).

## Mídia e precisão
- Sete imagens herdadas vistas (`busca/midia-herdada.png`): corretas. Vinte figuras dos slides no verso dos autorais, com crédito.
- Cópias MCAT: link Khan Academy e crédito OpenStax com HTML quebrado limpos na cópia; clozes triviais desfeitos (“off/on”, “transcription”, “prokaryotic/several”).
- Decisões de precisão: lacZ− testado com IPTG (sem β-gal não se forma alolactose); MCAT “digest it into glucose” excluído por impreciso.

## Instalação e Tab
- `apply.py` com `escrita()`: 60 notas / 74 cards no deck `NEBLI::UC03::P2::Biologia Molecular::Operon em procariotos`, readback sem divergência (`receipt.json`), `NEBLI_Comentario` vazio, nada suspenso; sync solicitado ao AnkiWeb (chegada no tablet não conferida). Cópias MCAT no modelo `NEBLI AnKing independente - v3` (o clone MCAT não tem o campo de comentário).
- Associado 1790166169397 (Genética bacteriana) recebeu só tags; segue suspenso pelo cram de 01/10.
- Tab: `explicacoes resumo '"tag:NEBLI::2026-uc03-biomol-29-operon-procariotos"'` → atual 75, revisar 0, desatualizada 0, faltando 0. Amostra de 8 lida (irmãos, autorais, AnKing, MCAT). O Tab não foi visto abrindo no Anki.
- Pacote APKG da UC03 não regenerado nesta corrida.
