# Descobertas verificadas para implementação

Inspeção em 22/09/2026. Somente leituras em Drive/Sheets e código local. Não houve inspeção da coleção viva no Mac, importação, mudança de agendamento ou publicação no Drive.

## Planilha

[Planilha 2026](https://docs.google.com/spreadsheets/d/1T1RZ_vpqtchmdM8U2BXYmlHk7e-Ov-iCGM51PFIEqMU/edit).

| Uso | Aba / identificador | Estrutura observada |
| --- | --- | --- |
| Datas efetivas — prioridade confirmada pelo usuário | Mês / 742023752 | Semanas em blocos: cabeçalho de datas, manhã, tarde, espaçamento |
| Identificação de aulas e associação a provas | Matérias / 1361835520 | Linha 1: UCs; linha 2: Data, Horário, Local, N, C, Tema, P, E |
| Registro de tempo de estudo | Diário de Estudo / 0 | Blocos de 25 minutos; não confundir atividade registrada com data oficial da aula |
| Rotina semanal | Rotina / 821379345 | Horários e atividades por dia; não é cadastro das aulas |

`Matérias`: UC03 em A:H; UC04 em J:Q; UC07 em S:Z; UC08 em AB:AI; UC16 em AK:AR; UC19 em AT:BA; UC21 em BC:BJ. Descobrir os blocos pelos cabeçalhos a cada leitura, não fixar offsets como identidade permanente.

Observações com coordenadas da leitura, não identificadores estáveis:

- `Matérias!A35:H35`: conteúdo 38, PT, Patologia da inflamação aguda, 11/09, P2.
- `Matérias!A37:H37`: conteúdo 37, IM, Inflamação: início e resolução, 17/09, P2.
- `Matérias!A44:H44`: P2 UC03 em 02/10, 14h–18h.
- `Mês!F36`: P2 UC03 no bloco cuja data de sexta é 02/10. Revalidar coordenada e cabeçalho antes de usar.
- P1 UC03: `Matérias!A23` = texto 28/08; `Mês!F20` = P1 UC03 sob a data 04/09 em F18. Mês prevalece por resposta explícita.
- `Matérias!A51:H51`: Grand Round 3, conteúdo 42, 13/10, associado a P2, que está em 02/10. Isso exige confirmação do vínculo/escopo quando afetar uma ação; não corrigir automaticamente a associação.
- Há datas textuais, datas nativas, `A confirmar`, datas múltiplas como `03 e 05/11`, números ausentes, `#ERROR!` em linhas de prova e múltiplas provas numa célula (`P1; P2; P3; P4`).
- O significado da coluna `E` não foi confirmado. Não inferir que TRUE signifique conteúdo dominado, cards prontos ou liberação autorizada.
- O título do arquivo é 2026, mas o Diário contém histórico com datas de outros anos. Cada parser precisa de contexto explícito de ano e não deve reescrever datas históricas.

A integração deve ler os valores efetivos e o tipo da célula, normalizar para ISO com fuso America/Sao_Paulo, preservar o texto original e citar a origem de cada data. Uma célula vazia em Mês não cancela automaticamente uma aula encontrada em Matérias.

## Piloto localizado

[UC03](https://drive.google.com/drive/folders/1UhCGXx44bfSLT8FUrrry3xND7vYrKx3d) → [Patologia](https://drive.google.com/drive/folders/1gQFoZ-EixjrgnUpA064yu6BlpX8nzK7x) → [38 — Inflamação aguda](https://drive.google.com/drive/folders/1apmeYFBAs8fHkc1wMw7AIsGdHUOtIxT3).

Arquivos observados:

| Arquivo | ID | Tipo |
| --- | --- | --- |
| Inflamação aguda — transcrição | 1O5qLt4JANr93Hv7tEXeZ8TddmsiHKAjw | PDF, cerca de 2,76 MB |
| Inflamação aguda — etapas 1 a 3 | 1uvoBwMJA4HPSb-pTQmtLx9wXzkSylTR4 | PDF, cerca de 2,70 MB |

Nesta listagem não apareceu um arquivo separado de slides. Não afirmar que os slides foram lidos, nem tratar a E1 antiga como fonte primária independente. Os PDFs foram localizados por metadados; seu conteúdo não foi auditado nesta etapa de arquitetura.

Aula relacionada, mantida separada para testar associação sem duplicação:

[Imunologia → 37 — Inflamação — início e resolução](https://drive.google.com/drive/folders/1saNqGX0T8J3XMb8KvHmH-83l6urgLXK3).

- Slides: `1qAeOJhQmlhkXPH1QFWreleIi5HS28Qu-`, PDF, cerca de 17,6 MB.
- Etapas 1 a 3 antigas: `1uhw7Q8-hGx9AtXcd7ovd-IVNUI0XzK-i`, PDF, cerca de 2,89 MB.

Inflamação granulomatosa (conteúdo 47, P3) e crônica (conteúdo 62, P3) têm pastas próprias. Não expandir o piloto para essas aulas só por compartilharem o termo inflamação.

As pastas localizadas constam como compartilhadas. Fontes podem ser lidas daí, mas a saída pessoal deve usar destino privado explicitamente identificado. Manter fontes e PDFs antigos intactos.

## Pontos de código a corrigir antes de reutilizar

| Arquivo | Evidência da inspeção | Consequência |
| --- | --- | --- |
| `flashcards/scripts/copiar_curadoria_para_deck.py` | Dedup por primeiro campo apenas no destino; remoção de tags #AK; prefixo inserido em Text | Não serve como escritor global sem refatoração |
| `flashcards/scripts/montar_deck_aula.py` | `createDeck` antes de avaliar modo dry; dedup por texto no destino | dry-run atual não é estritamente sem escrita |
| `flashcards/scripts/verificar_cobertura_deck.py` | Palavra na frente OU Extra conta como cobertura; leitura da tabela notes | Não prova recuperação do objetivo; não conta carga por card |
| `flashcards/scripts/validate_lesson_coverage.py` | Inventário útil, mas E1 obrigatória e referências por trechos de texto | Migrar para objetivos e identidades de cards |
| `flashcards/scripts/anki.py` | Repetição automática após timeout | Separar leitura repetível de escrita com resultado desconhecido |
| `flashcards/scripts/subir_drive.py` | Lista fixa de slugs e caminhos | Descoberta por IDs e registro de destino |
| `.claude/commands/resumo.md` | Caminhos absolutos antigos, limpeza dos arquivos comuns, E2/E3 e loop obrigatório | Novo comando isolado e migração pontual das regras |

O worktree já tinha mudanças em `.claude/commands/resumo.md`, `CLAUDE.md`, `FLASHCARDS.md` e arquivos Typst, além de materiais novos de glicogênio. São mudanças anteriores do usuário; preservar.

## Limites desta verificação

Não foram testados AnkiConnect no Mac, versões de Anki/AnkiDroid, AnkiHub, corpus atual, templates, IO, importação cruzada, exportação de pacotes ou sincronização dos dispositivos. Esses são testes de implementação, não resultados já obtidos. As diferenças de datas e os problemas de código acima foram observados diretamente.
