# Convenções do banco NEBLI

Este arquivo documenta como o banco é estruturado, como questões são adicionadas e como as tags evoluem. É o contrato entre Davi e Claude — qualquer mudança aqui muda o jeito como o banco se comporta.

## Estrutura física

```
banco/
├── questoes/           # Um arquivo q-NNNN.md por questão
├── indice/             # banco.json gerado pelo script de indexação
├── meta/               # Convenções, taxonomia, log de mudanças
└── figuras/            # Imagens compartilhadas entre questões
```

## Schema da questão

Cada questão é um arquivo `q-NNNN.md` em `questoes/`, onde NNNN é o id sequencial com 4 dígitos (q-0001, q-0042, q-1337). Frontmatter YAML no topo, conteúdo em markdown abaixo.

### Campos obrigatórios

- `id`: número sequencial (igual ao do nome do arquivo, sem prefixo q-)
- `tags`: array de tags da taxonomia. Mínimo 1, sem máximo prático. Se a questão é multi-item, ver campo `itens` abaixo
- `nivel`: `facil` | `medio` | `dificil`
- `formato`: `MC` (múltipla escolha) | `CE` (certo/errado) | `discursiva`
- `conceito_central`: uma frase definindo o que a questão testa de fato (não o que ela parece testar). Exemplo: "diferença entre transporte ativo primário e secundário do ponto de vista do gasto direto de ATP"
- `gabarito`: para MC use letra (`A`-`E`); para CE use array com C/E por item (ex: `[C, E, C, E]`); para discursiva use texto curto ou referência ao corpo
- `explicacao`: explicação concisa do gabarito. Pode ir no frontmatter (curta) ou no corpo do arquivo (longa, com seção `## Explicação`)

### Campos opcionais

- `uc_origem`: UC onde a questão caiu (ex: `UC1`, `UC21`). Deixe vazio se não souber
- `prova`: `P1` | `P2` | `P3` | `sub` | `recup`. Deixe vazio se não souber
- `ano`: ano da prova (ex: `2024`). Deixe vazio se não souber
- `armadilha`: descrição curta da confusão que o examinador explora. Exemplo: "alunos confundem gradiente eletroquímico com gradiente químico puro"
- `figura`: caminho relativo a partir de banco/, ex: `figuras/respiratorio_curva_pv.png`
- `fonte`: campo livre — `FMUSP turma 113`, `USMLE step 1`, `Enare 2023`, `Berne capítulo 4`, etc.
- `itens`: para MC com distratores conceitualmente diferentes ou CE com itens independentes. Lista de objetos `{letra, conceito, tags}` permitindo busca granular sem fragmentar o arquivo

### Exemplo de frontmatter completo

```yaml
---
id: 42
tags: [transporte-membrana, transporte-ativo-primario, bomba-na-k]
nivel: medio
formato: MC
conceito_central: identificação da bomba Na/K como transporte ativo primário pelo gasto direto de ATP
gabarito: C
armadilha: aluno confunde "ativo primário" com "rápido" — velocidade não define a categoria
fonte: USMLE step 1 banco aberto
itens:
  - letra: A
    conceito: difusao-simples
    tags: [transporte-membrana, difusao]
  - letra: B
    conceito: difusao-facilitada
    tags: [transporte-membrana, difusao-facilitada]
  - letra: C
    conceito: bomba-na-k
    tags: [bomba-na-k, transporte-ativo-primario]
  - letra: D
    conceito: cotransporte-secundario
    tags: [transporte-ativo-secundario]
  - letra: E
    conceito: endocitose
    tags: [endocitose]
---
```

## Regras de tagging

### Forma das tags

- **kebab-case**: `transporte-ativo`, não `Transporte Ativo` ou `transporte_ativo`
- **Sem acentos**: `acido-base`, não `ácido-base`. (Acentos no enunciado e na explicação são livres — só nas tags que evitamos.)
- **Substantivos**: `osmose` em vez de `osmotico`. Conceito é coisa, não adjetivo.
- **Sem hierarquia embutida no nome**: use `bomba-na-k`, não `transporte/ativo/bomba-na-k`. A hierarquia vive na taxonomia.md, não no nome da tag.

### Quando criar tag nova vs usar existente

Antes de criar uma tag nova, Claude consulta `taxonomia.md`. Regras:

1. Se existe tag para o mesmo conceito (mesmo que com nome diferente), use a existente.
2. Se a confusão é por sinônimo (ex: pensei em `atpase-sodio-potassio` mas a taxonomia tem `bomba-na-k`), Claude propõe usar a existente e adiciona o sinônimo aos "rejeitados" da taxonomia.
3. Tag nova só nasce quando o conceito não tem cobertura. Nesse caso, Claude marca a questão com `tags-pendentes-aprovacao: [nome-novo]` no frontmatter, e a tag entra em `taxonomia.md` na seção "pendentes" até Davi confirmar.

### Granularidade

- Uma questão tem **3 a 7 tags** tipicamente. Menos que isso é raso (perde-se busca); mais que isso é ruído.
- A primeira tag é a **mais central** ao conceito da questão. As demais são suporte.
- Tags devem refletir o que a questão **testa**, não tudo que ela **menciona**. Uma questão que tem como tema central a bomba Na/K e cita osmose só de passagem deve ter `bomba-na-k` mas não `osmose`.

## Fluxo de ingestão em lote

Quando Davi manda um PDF (ou foto, ou texto) com questões novas:

### Etapa 1 — Extração
Claude extrai cada questão preservando enunciado, alternativas/itens e gabarito original.

### Etapa 2 — Classificação automática
Para cada questão, Claude propõe:
- Tags (consultando taxonomia.md)
- Nível (fácil/médio/difícil) — calibrado pelo grau de raciocínio exigido, não pelo "tema parecer difícil"
- Conceito central (uma frase)
- Armadilha (se houver)
- Tags pendentes (se conceito novo apareceu)

### Etapa 3 — Commit autônomo (sem aprovação)
Claude comita diretamente, sem apresentar tabela de revisão nem esperar Davi.
1. Cria os arquivos `q-NNNN.md` definitivos
2. Adiciona tags novas à `taxonomia.md` (sem marcar como pendentes — vai direto para ESTÁVEIS)
3. Roda `indexar.py` para regenerar `banco.json`
4. Registra no `LOG.md` quantas questões, quais fontes e quais tags novas entraram

**Regra de qualidade autônoma:** Se uma questão tiver gabarito incerto ou enunciado parcialmente ilegível (OCR), Claude infere o mais plausível dado o contexto médico e comita assim mesmo. Pequenas imprecisões são aceitáveis — o que importa é o conceito central estar correto.

## Rotina de consolidação (a cada ~50 questões novas)

Quando o banco cresce em ~50 questões, Claude faz uma **passada de consolidação**:

- Lista tags com baixa cobertura (1–2 questões só) — candidatas a fusão
- Lista tags com cobertura altíssima (>30 questões) — candidatas a quebrar em sub-tags
- Aponta tags semanticamente próximas que poderiam virar uma só
- Apresenta a Davi uma lista de fusões/divisões/renomeações propostas, com impacto em quantas questões cada mudança afeta
- Após Davi aprovar, Claude refator todas as questões afetadas e atualiza taxonomia + índice

## Versionamento

- `meta/LOG.md` registra cada lote ingerido (data, quantas questões, tags novas, refators de consolidação)
- O banco não usa git (ainda) — a auditoria visual fica no LOG e na pasta de arquivos

## O que NÃO entra no banco

- Questões inventadas pelo Claude para resumos (essas são geradas on-the-fly nas Etapas 3 e 4 do NEBLI)
- Questões duplicadas entre fontes — fica a primeira, a segunda referencia a primeira no campo `fonte`
]
Extra: não importa o gabarito apontado, o que importa é que o Claude resolva o item e gere o gabarito correto para o item, daí ele vai pro banco com gabarito correto
