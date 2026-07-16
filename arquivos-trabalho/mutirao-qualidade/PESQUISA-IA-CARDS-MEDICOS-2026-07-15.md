# Pesquisa de IA para cards médicos — síntese do debate

Data: 2026-07-15  
Escopo: plataformas e repositórios para criação e manutenção de flashcards, com aplicação ao NEBLI.  
Método: confronto entre três frentes independentes — auditoria do NEBLI, pesquisa de plataformas e pesquisa de repositórios open source.

## Resumo executivo

O NEBLI deve continuar usando o Anki com FSRS como ambiente de estudo. Nenhuma plataforma pesquisada reúne, sozinha, fidelidade à aula, curadoria médica, controle de carga, Image Occlusion, proveniência, licença de mídia, feedback operacional e alterações auditáveis.

O melhor caminho é incorporar ao pipeline local quatro ideias externas:

1. contexto e proveniência por card, como RemNote e StudyFetch;
2. recuperação de cards curados antes de gerar novos, como o Smart Search do AnkiHub;
3. ingestão multimodal de PDF, slides, imagens e aulas, como Quizlet, Knowt, Gizmo e StudyFetch;
4. geração versionada, retomável e revisável, como `anki-llm`.

O debate também corrigiu o significado de “imagem duplicada” neste mutirão: o problema imediato é a mesma imagem aparecer duas vezes no mesmo card. Reutilizar um asset em cards diferentes é aceitável quando ele é pertinente a cada tarefa visual.

A auditoria local encontrou 16 notas com a mesma referência `src` repetida literalmente duas vezes no campo `Extra`. Uma busca ingênua no HTML final apontou 32 notas/43 cards, mas parte disso é falso positivo: templates AnKing podem renderizar o mesmo conteúdo em elementos alternativos para desktop e mobile, deixando apenas um visível por CSS. Portanto, o gate deve combinar análise dos campos-fonte com preview ou DOM visível; não deve condenar automaticamente toda repetição no HTML bruto.

## O que as plataformas fazem bem

### RemNote

É o benchmark mais completo para conteúdo visual e vínculo com a fonte:

- cria cards a partir de notas, texto selecionado, páginas web e PDFs;
- permite configurar o tipo de card e revisar o resultado antes de aceitar;
- gera máscaras de Image Occlusion com IA e permite corrigir, mover, girar, dividir ou mesclar máscaras;
- reconhece o texto sob as máscaras e pode exigir resposta digitada;
- oferece recorte e autozoom específicos para cada alvo;
- permite Hide All, Guess One e teste de várias máscaras em sequência;
- mantém o PDF-fonte acessível durante a revisão;
- oferece FSRS, planejamento para data de prova e estatísticas por card.

O aprendizado central para o NEBLI é que IA em Image Occlusion deve funcionar como editor assistido. A decisão sobre quais estruturas são nucleares não pode ser delegada à detecção automática de caixas.

Referências:

- https://www.remnote.com/feature/ai-flashcards
- https://help.remnote.com/en/articles/6511625-image-occlusion-cards
- https://help.remnote.com/en/articles/9124137-the-fsrs-spaced-repetition-algorithm
- https://help.remnote.com/en/articles/7970392-flashcard-statistics

### StudyFetch

Destaca-se pela ligação entre cards gerados e o material de origem:

- recebe PDF, slides, notas, vídeo e aula gravada;
- cria cards básicos, cloze, preenchimento, múltipla escolha e Image Occlusion;
- permite imagens na pergunta e explicações visuais;
- mostra no card o trecho do material que originou a informação;
- coleta feedback positivo ou negativo sobre cards gerados;
- importa decks Anki, preservando campos e formatação quando compatíveis.

Para o NEBLI, a ideia mais valiosa é a proveniência clicável no nível de página, slide, trecho ou região da página.

Referências:

- https://www.studyfetch.com/docs
- https://www.studyfetch.com/docs/tutorial-doc-format/flashcards
- https://www.studyfetch.com/use-case/flashcard

### AnkiHub e AnKing

É a referência mais próxima do uso médico do NEBLI:

- mantém decks médicos colaborativos e atualizados;
- recebe materiais de aula no Smart Search e recupera cards existentes;
- oferece explicações baseadas no conteúdo do próprio deck;
- sugere cards relevantes e sua dessuspensão;
- organiza conteúdo por recursos médicos, faculdades e IDs de bancos de questões.

O NEBLI deve importar o princípio “recuperar antes de gerar”, sem depender de uma plataforma externa: dado um trecho da aula, primeiro procurar um card autoral ou AnKing compatível; gerar um novo apenas quando houver lacuna real.

Referências:

- https://www.ankihub.net/step-deck?lang=en
- https://community.ankihub.net/t/pre-release-powerful-new-features-with-ankihub-premium/343224

### Quizlet, Knowt e Gizmo

São bons benchmarks de experiência de ingestão:

- recebem PDF, PowerPoint, notas, fotos, áudio, vídeo, URL e gravações de aula, conforme a plataforma;
- produzem rapidamente um rascunho editável;
- combinam cards, resumos, quizzes e modos de revisão;
- o Gizmo recomenda segmentar documentos grandes para reduzir omissões.

São úteis como referência de interface, mas as páginas oficiais consultadas não demonstram o mesmo controle necessário ao NEBLI sobre fidelidade médica, proveniência, Image Occlusion, exportação fiel para Anki, licença de imagens e auditoria de alterações.

Referências:

- https://quizlet.com/features/ai-flashcard-generator
- https://quizlet.com/features/ai-study-tools
- https://knowt.com/flashcards
- https://help.gizmo.ai/en/articles/15647624-what-is-magic-import

## O que os repositórios oferecem

### `anki-llm`

É o repositório mais aproveitável como referência de engenharia:

- processa notas em lote diretamente pelo AnkiConnect ou por arquivos;
- exporta CSV/YAML legível e versionável;
- aceita prompts customizados e diferentes provedores de modelo;
- possui retries, salvamento incremental e retomada;
- oferece dry-run, logs e revisão interativa de candidatos;
- cria snapshots antes de alterar templates e verifica divergências antes do push.

O NEBLI já possui Git, staging, manifesto e scripts próprios. Portanto, é mais útil incorporar esses padrões do que substituir o pipeline.

Referência:

- https://github.com/raine/anki-llm

### Extração de documentos

Os projetos `pdf-flashcards-autogen` e `pdf-to-anki-flashcards` exemplificam extração e exportação para Anki, mas são mais simples do que a exigência médica do NEBLI.

O Docling é uma base promissora para conservar página, bloco e bounding box na extração de PDFs. O PaddleOCR pode sugerir caixas de rótulos e ajudar a detectar vazamento de resposta em figuras. Nenhum dos dois resolve com segurança a associação seta–estrutura nem decide o que é nuclear para a prova; são ferramentas de proposta, não de aprovação.

Referências:

- https://github.com/quocdat-le-insacvl/pdf-flashcards-autogen
- https://github.com/JavierOrtunoRoig/pdf-to-anki-flashcards
- https://github.com/docling-project/docling
- https://github.com/PaddlePaddle/PaddleOCR

## Comparação com a base Anki

O Anki já oferece os componentes que devem permanecer como núcleo:

- Image Occlusion nativa desde a versão 23.10;
- máscaras retangulares, elípticas e poligonais;
- FSRS com retenção desejada e parâmetros otimizáveis;
- estatísticas de estabilidade, dificuldade, recuperabilidade e retenção real;
- formatos de importação/exportação e pacotes com mídia;
- flexibilidade de campos, templates e integração via AnkiConnect.

Referências:

- https://docs.ankiweb.net/editing.html
- https://docs.ankiweb.net/deck-options
- https://docs.ankiweb.net/stats.html
- https://docs.ankiweb.net/exporting.html

## Arquitetura recomendada para o NEBLI

### 1. Proveniência como dado obrigatório

Cada card gerado ou modificado deve registrar, quando aplicável:

- arquivo-fonte;
- página ou slide;
- bounding box ou trecho textual;
- âncora E1;
- URL e licença da imagem;
- hash do asset;
- modelo, prompt e versão do pipeline;
- decisão do curador.

A proveniência deve ser clicável e permitir reabrir o contexto da aula. Isso reduz alucinação, facilita correção e torna possível comparar o card com a fonte sem nova busca.

### 2. Recuperar antes de gerar

O pipeline deve buscar primeiro:

1. card NEBLI autoral equivalente;
2. cópia AnKing superior e já curada;
3. card externo compatível;
4. somente então, uma nova geração.

A compatibilidade deve considerar o objetivo pedagógico, e não apenas palavras-chave. Para imagens, o `visual_task` deve preceder a busca: identificar estrutura, reconhecer padrão histológico, ordenar mecanismo ou explicar relação causal são tarefas diferentes, mesmo quando tratam do mesmo órgão.

### 3. Dois trilhos visuais distintos

#### Image Occlusion

Use quando a própria imagem é a pergunta: anatomia, histologia, radiologia, embriologia espacial ou identificação de componentes.

Fluxo recomendado:

1. definir o que o aluno precisa localizar ou reconhecer;
2. selecionar uma imagem adequada à tarefa;
3. OCR ou visão computacional sugere máscaras;
4. o curador escolhe inicialmente 2–4 alvos nucleares;
5. ajustar crop e zoom por alvo;
6. gerar preview de todas as máscaras;
7. verificar vazamento, resolução, contexto e licença;
8. promover somente após aprovação humana.

OCR não deve inferir sozinho qual rótulo corresponde a uma seta, escolher estruturas de alto rendimento ou transformar todos os rótulos detectados em cards.

#### Imagem explicativa

Use quando a imagem reconstrói mecanismo, comparação, sequência ou relação espacial que o texto isolado não explica bem.

Ela deve normalmente ficar no verso/`Extra`, com uma função explícita. Uma imagem meramente temática ou decorativa não melhora o card. Reconhecimento anatômico e histológico deve priorizar imagens reais ou diagramas validados; imagens geradas por IA podem ser úteis para esquemas conceituais, nunca como verdade visual não revisada.

### 4. Estado visual único e inserção idempotente

Cada nota deve ter um estado visual canônico, com papéis explícitos como:

- `front_prompt`;
- `back_explanation`;
- `io_source`.

Cada bloco visual deve possuir um identificador estável. Reaplicar o pipeline deve fazer upsert pelo identificador/hash, não concatenar novo HTML ao campo. Isso impede que uma segunda execução cole a mesma imagem novamente.

Upsert idempotente e aprovação por diff resolvem problemas diferentes e ambos são necessários:

- o upsert impede duplicação por reexecução;
- o diff/preview permite perceber mudanças indevidas antes da promoção.

### 5. Gate correto contra duplicidade intranota

O gate deve:

1. extrair todas as imagens de cada campo-fonte;
2. normalizar `src`, URL e nome da mídia;
3. comparar referências literais e, quando necessário, SHA-256 do conteúdo;
4. detectar repetição dentro do mesmo campo e entre campos da mesma face;
5. renderizar `cardsInfo.question` e `cardsInfo.answer`;
6. considerar visibilidade no DOM/CSS, evitando falsos positivos de elementos alternativos ocultos;
7. não comparar frente com verso como se fossem a mesma face;
8. não considerar erro o uso pertinente do mesmo asset em cards distintos.

Para as duplicações confirmadas, deve-se manter a ocorrência no campo canônico definido pelo papel visual e remover somente as cópias secundárias. Hash perceptual pode ser uma checagem P1 para arquivos diferentes com pixels praticamente iguais; embeddings visuais não são necessários para corrigir a duplicação literal atual.

## Ciclo transacional de feedback

Flag, comentário e suspensão representam uma pendência ativa, não um arquivo histórico permanente. O fluxo padrão deve ser:

1. capturar o estado anterior do card, incluindo flag, suspensão e comentário;
2. registrar o problema em um ledger estruturado;
3. classificar o motivo: factual, ambiguidade, carga, imagem duplicada, imagem inadequada, vazamento, formatação ou outro;
4. corrigir ou decidir conscientemente não alterar;
5. executar lint, render e preview;
6. obter aprovação humana quando houver julgamento médico ou visual;
7. no mesmo processo transacional, limpar a flag, retirar a suspensão e encerrar o comentário;
8. manter no ledger a decisão, evidência, data, hashes e responsável.

Se qualquer etapa falhar, o estado ativo anterior deve ser preservado ou restaurado. Assim, uma sinalização antiga já tratada não se mistura às próximas flags do usuário.

## Prioridades

### P0 — corrigir agora

1. Remover as duplicações literais confirmadas nas 16 notas, preservando apenas o bloco visual canônico.
2. Criar lint por campo-fonte para `src` repetido e gate de preview/DOM visível.
3. Tornar a aplicação visual idempotente por block ID/hash.
4. Implementar ledger e ciclo transacional: analisar → corrigir → validar → limpar flag → dessuspender → registrar encerramento.
5. Exigir `visual_task`, papel e placement explícitos em toda nova inserção de imagem.

### P1 — próximo ciclo

1. Adicionar proveniência de página/slide/trecho/bounding box.
2. Criar preview automatizado por face e por máscara de Image Occlusion.
3. Usar OCR apenas para sugerir máscaras e detectar possíveis vazamentos.
4. Adicionar hash perceptual para encontrar recodificações da mesma imagem dentro da nota.
5. Medir feedback, lapses, dificuldade, tempo de resposta e retenção por card para priorizar reformulações.

### P2 — evolução

1. Indexar E1, NEBLI e referências externas para busca semântica antes da geração.
2. Construir interface de revisão de candidatos com fonte, diff e preview lado a lado.
3. Gerar esquemas explicativos versionados, com revisão médica e visual.
4. Criar agenda adaptativa ligada à data de prova, mantendo FSRS como scheduler.
5. Avaliar embeddings de texto e imagem somente para ranking, nunca como aprovação autônoma.

## Cinco melhorias de maior impacto

1. **Dedupe intranota consciente do render:** detectar duplicação no campo e confirmar o que realmente fica visível, sem falsos positivos do template.
2. **Proveniência clicável:** abrir página, slide ou trecho exato que fundamentou o card.
3. **Image Occlusion assistida, não automática:** OCR sugere; curador escolhe 2–4 alvos nucleares e aprova preview.
4. **Feedback fechado e transacional:** depois da análise e correção, limpar flag e dessuspender automaticamente, mantendo histórico no ledger.
5. **Geração idempotente e versionada:** upsert por block ID/hash, candidatos em JSON/YAML, dry-run, diff, logs, staging e rollback.

## Critérios de sucesso

O processo estará maduro quando:

- nenhuma face visível contiver a mesma imagem duas vezes sem intenção explícita;
- reaplicar o pipeline não alterar cards já convergidos;
- toda imagem tiver tarefa, placement e proveniência definidos;
- todo IO tiver preview aprovado e poucos alvos nucleares;
- todo feedback tratado deixar de aparecer como pendência ativa;
- toda mudança puder ser explicada, reproduzida e revertida;
- os ganhos forem medidos por retenção, tempo, lapses e carga, não apenas por quantidade de cards gerados.

## Decisão do debate

As três frentes convergiram no seguinte desenho:

- Anki/FSRS permanece como runtime;
- Git, manifestos e staging permanecem como infraestrutura de curadoria;
- contexto de fonte e preview vêm antes da automação em escala;
- upsert determinístico e diff aprovado são requisitos complementares;
- Image Occlusion e imagem explicativa são produtos diferentes e exigem gates diferentes;
- IA pode extrair, sugerir, ordenar e criticar, mas não deve aprovar sozinha conteúdo médico ou visual;
- o próximo ganho estrutural do NEBLI não vem de gerar mais cards, e sim de tornar cada geração rastreável, idempotente, visualmente verificável e fechada pelo feedback real do usuário.
