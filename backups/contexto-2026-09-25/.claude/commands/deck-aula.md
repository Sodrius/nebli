---
description: Gera, instala, verifica e publica um deck-aula NEBLI AnKing-first
argument-hint: <nome, link ou pasta da aula> [observações]
---

Argumentos recebidos: $ARGUMENTS

Atualização 25/09: após README, ler `flashcards/projeto/CALIBRACAO-2026-09-25.md` e `AUDITORIA-2026-09-25.md` antes da v4. Azul (4) substitui rosa (5). A fila vigente define exceções de entrega: neste lote, só deck, sem E1/guia/upload. Não reintroduzir alvos rejeitados nem reutilizar planos antigos como seleção atual. Núcleo de manutenção (referência até 35/aula) ainda requer curadoria própria.

Preferência de Davi: qualidade máxima, Opus 5.5 com esforço alto selecionado por ele. Ler `flashcards/projeto/HANDOFF-CLAUDE.md` na primeira sessão. Não compensar fontes ausentes com confiança verbal, nem confundir teste técnico com qualidade de curadoria. Não alterar modelo/configuração por conta própria.

Execute o pipeline atual de deck-aula. Não use o antigo pipeline RemNote, os gates GH1–GH5 do resumo completo, E2/E3, cota de cards ou scripts antigos de dessuspensão em massa.

## Leitura obrigatória, nesta ordem

1. `flashcards/projeto/README.md` — preferências e estado atual.
2. `flashcards/projeto/CALIBRACAO-ESCALA-V4.md` — 30 respostas vigentes; prevalece sobre v3 e pilotos.
3. `flashcards/projeto/CONTRATO-DE-QUALIDADE.md` e `OPERACAO-CODEX-CLAUDE.md` no mesmo diretório — aceite, acervos, diagnóstico e publicação.
4. `flashcards/projeto/EXECUCAO-DECK-AULA.md`, `ACERVOS-REFERENCIA.md` e `PUBLICACAO-POR-UC.md` no mesmo diretório — execução, busca nos acervos e empacotamento da UC. V3 é histórico opcional.
5. Caso real mais parecido:
   - `flashcards/projeto/APRENDIZADOS-INFLAMACAO-V2.md`; ou
   - `flashcards/projeto/APRENDIZADOS-VASCULARIZACAO-VISCERAS.md`; ou
   - `flashcards/projeto/APRENDIZADOS-INTESTINOS.md` para histologia, lembrando que este último ainda aguarda feedback.

Leia cada arquivo inteiro antes de agir. Esses documentos atuais e a instrução mais recente de Davi vencem regras legadas de cards, RemNote e resumo completo. Não escolher uma próxima aula automaticamente se o pedido for só ajustar o pipeline.

As decisões da seção **“Decisões fechadas — não perguntar novamente”** do README já foram dadas por Davi. Não as reapresente como questionário. Pergunte apenas um dado específico da aula que não possa ser localizado e que mude materialmente o resultado.

## Interpretação do pedido

- Se Davi pediu “gere”, “rode”, “faça” ou “vai até o fim”, execute até Anki + APKG + Drive privado + E1 + verificação.
- Se pediu apenas avaliação, auditoria ou planejamento, mantenha Anki e Drive em leitura.
- Pergunte somente uma ambiguidade que mude materialmente o recorte/destino; fora disso, investigue e avance.

## Resultado obrigatório

Siga todos os passos e gates de `EXECUCAO-DECK-AULA.md`. Em particular:

- material docente delimita o assunto, aprofundado por bibliografia, vídeos e AnKing pertinentes sem importar outras aulas;
- iniciar pelo diagnóstico de acervos e pendências anteriores; resolver comentários/vermelhos conservadoramente e relatar;
- separar conteúdo ensinado de exemplo;
- verificar identidade antes de copiar;
- buscar AnKing amplamente dentro do assunto, mesmo se outro card já o cobre → outros decks locais adequados para lacunas → autoria mínima; cada autoral exige busca documentada e inspeção do resultado;
- ler frente, verso, imagens e cada cloze;
- auditar objetivo → cobertura antes de aplicar;
- usar cópias NEBLI independentes, preservando originais e histórico;
- verde somente para `1-HighYield` literal do AnKing;
- vermelho = melhorar; laranja = comentário pendente, limpar após resolver/conferir; rosa = qualquer bom candidato a suspensão pós-prova, sinalizado na criação e mantido ativo; preservar bandeiras pessoais e colisões conforme v4;
- não criar rodapé meta, não suspender automaticamente;
- verificar contagem, renderização, mídia, flags, fontes e APKG;
- E1 explicativa + guia curto com vídeos/bibliografia (links no guia/chat, não nos cards); guia sozinho não substitui E1;
- publicar E1/guia por aula; APKG único da UC inteira, comprimido internamente, sem flags, atualizado pelo mesmo file_id na pasta privada da UC. Usar o empacotador testado e preservar todas as flags vivas;
- padrão é manter; Davi decide a cada prova se suspende rosas. Não suspender automaticamente nem alterar 35 novos/50 min no Anki;
- respeitar limpeza intencional: não restaurar decks/cards excluídos, reimportar APKG histórico ou reexecutar scripts velhos para sanar pendências; partir da coleção viva. Ainda restavam 89 cards em duas aulas na vistoria, não apagar esses remanescentes sem pedido;
- registrar aprendizados da aula.

Não declare “pipeline genérico pronto”: o comando ainda orquestra um fluxo assistido. Informe separadamente o que foi instalado, exportado, publicado e o que depende de sincronização do usuário.
