# MEMORY.md — estado vivo do NEBLI

> Memória operacional curta. **Não guardar aqui histórico de resumos/aulas antigas, decisões já substituídas, pilotos fechados ou diários de geração.** O Git preserva esse histórico. Este arquivo existe para a próxima corrida começar com as regras atuais, sem carregar o peso das anteriores.

## Davi / objetivo atual

- Medicina FMUSP, ciclo básico.
- O resumo NEBLI ensina; o Anki retém e transfere.
- Cards devem servir ao mesmo tempo à prova local, à retenção ao longo do curso e à construção gradual de base Step 1, sem virar um currículo Step 2/residência paralelo.
- Preferência por intervenção simples e conservadora: básico bem feito, pouca regra artificial.

## Flashcards — estado canônico

- Deck único por aula: `NEBLI::<UC>::<Prova>::<Matéria>::<Aula>`.
- Duas velocidades no mesmo deck: **25 novos/dia + FSRS** no uso normal; antes da prova, acelerar temporariamente apenas o subdeck da prova. Não duplicar cards para cram.
- Primeiro classificar conceitos da E1 em `nuclear | supporting | no_card`. Nem todo detalhe da E1 merece spaced repetition.
- Fonte por conceito: **AnKing → outros decks de referência → autoral**. Autoral é último recurso. Se uma fonte melhor for encontrada depois, substituir o autoral em vez de acumular.
- `curar_anking_v2.py` encontra/rankeia candidatos; aprovação final é semântica, card a card.
- Frente/cloze autoral em inglês médico natural; Extra em português.
- Fonte visual real é preferência absoluta. Identificação/localização tende a Image Occlusion; mecanismo/comparação tende a imagem pertinente no Extra.
- Um alvo de recuperação independente tende a um card. Não há quota por subtópico.
- Guardrails de volume por aula: pequena ~15–25; média ~25–40; grande/densa ~35–55. Acima de 60 exige revisão explícita de redundância e justificativa.
- Hard gate: 100% dos `nuclear` cobertos; nenhum `no_card` indevido; E1 anchor; prioridade de fontes respeitada; sem retrieval target duplicado; visual obrigatório resolvido; carga plausível; refs presentes no Anki.
- E2 é auditoria de cobertura, não gerador automático de novos conceitos de card.

Detalhe prescritivo: `FLASHCARDS.md` + `flashcards/DECK-AULA-PIPELINE.md`.

## Resumos — memória intencionalmente limpa

- Não manter nesta memória lembranças de resumos antigos nem regras derivadas de uma aula específica.
- Não refatorar resumos antigos só para adequá-los a uma regra nova. Só tocar neles quando houver ganho concreto para o pipeline ou pedido explícito do Davi.
- Próximas aulas usam o pipeline atual; material legado não vira precedente editorial automaticamente.

## Pendências vivas

- A política nova passou pelo primeiro run completo e limpo em Digestório; ainda não fazer backfill em massa sem feedback de uso real.
- Quando houver feedback do Davi sobre um deck novo, corrigir primeiro a regra/validador que permitiu o defeito; só depois considerar correção retrospectiva.
