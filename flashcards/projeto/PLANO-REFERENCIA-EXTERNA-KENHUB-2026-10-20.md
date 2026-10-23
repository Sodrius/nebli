# Plano — Referência externa Kenhub em massa

Destino exato: `Referências::Referências Externas::Kenhub`. Acervo privado, puro Kenhub, separado dos decks-aula e da UC07.

Escrita no Anki: toda a coleta, mídia, identidade, destino e validação da leva são preparadas antes do lock. A leva inteira entra em uma única janela curta por ações vetorizadas/`multi`, sem escrita por card, sem sync durante o estudo e com um único readback final (G44).

## Resultado

Um acervo retomável e idempotente, na ordem oficial do Kenhub, com uma identidade por `estrutura × vista/unidade`, figuras limpas, seta e caixa legíveis no PC e no celular, cobertura comprovada e instalação suspensa por padrão. O acervo não recebe AnKing, AnatoKing nem autoral; decks-aula apenas reutilizam suas notas depois.

## Arquitetura de produção

O orquestrador determinístico mantém manifesto, fila, hashes, estados e métricas. Agentes especializados nunca escrevem no Anki:

1. **Descobridor/coletor** — percorre o catálogo e as unidades em uma única sessão serial do Kenhub, salva HTML/JSON/mídia e retoma por checkpoint. Não usa LLM.
2. **Normalizador** — resolve nome oficial PT/EN, estrutura, vista, módulo/unidade, coordenadas, SHA-256 e pHash. Não colapsa vistas pedagogicamente distintas.
3. **Montadores paralelos** — transformam lotes locais em JSON fechado; recebem apenas fonte, glossário e regras compactas.
4. **QA independente** — executa cobertura, identidade, mídia, visual e renderização de 100% dos cards; não corrige silenciosamente.
5. **Regulador forte** — vê somente divergências, baixa confiança, tradução não atestada, possível duplicata e amostra aleatória.
6. **Instalador único** — grava uma vez, em lote, somente por `nebli.decks.escrita()`, quando o Anki estiver livre; readback obrigatório e sem sync durante o estudo.
7. **Auditor** — compara manifesto e coleção viva, mede custo, retrabalho e cobertura, e emite o relatório final.

Estados: `DISCOVERED → COLLECTED → NORMALIZED → BUILT → GATED → REVIEWED → STAGED → INSTALLED → VERIFIED`. Cada transição grava artefato e hash; uma falha retoma do último estado válido.

## Identidade, ordem e hierarquia

- IDs imutáveis: `catalog_id`, `module_order`, `section_order`, `unit_order`, `learnable_id`, `structure_id`, `view_id`, `source_hash`, `asset_hash`, `output_hash`.
- Hierarquia: raiz exata acima, seguida por domínio, módulo, seção oficial do Kenhub e aula, todos em ordem lógica; seção e aula aparecem nominalmente nos decks. O piloto ocupa sua posição definitiva nessa mesma árvore.
- Alvo sem figura recebe card escrito curto no modelo AnKing-like, com fonte Kenhub; G46 proíbe fechar a aula com exceção vazia.
- Deduplicação em duas camadas: SHA-256 para cópia exata; pHash + identidade para possível repetição visual. Estrutura igual em outra vista não é eliminada.
- A UC07 continua onde está. Neuro não é duplicada no acervo externo sem decisão explícita.

## Visual da seta e da caixa

- Uma imagem grande e limpa; coordenadas normalizadas e overlay SVG, evitando recomprimir a figura para cada card.
- Seta de 3–4 px, halo branco de 2 px, cabeça triangular menor; cor âmbar ou ciano de alto contraste, nunca cor como única pista.
- Caixa quase opaca e levemente tingida, borda de 2 px na cor da seta, raio 6–8 px, sombra discreta e padding 6–10 px.
- Frente: `?` ou “Qual estrutura?”, sem revelar extensão do nome. Verso: mesma posição e seta, com o nome oficial PT.
- Posicionamento por custo contínuo: reprova sobreposição com alvo, rótulos e marca; penaliza distância, bordas e cruzamentos. Substitui a busca atual limitada a 24 ângulos.
- O piloto comparou âmbar e ciano; **ciano** é o token único definitivo da produção. A variante âmbar duplicada foi retirada após backup.

## Economia de tokens

- Descoberta, OCR/CV, segmentação verde, posicionamento, hashes, dedupe, schema e gates são locais/determinísticos.
- Uma figura é analisada uma vez e produz todos os alvos num único JSON; nunca uma chamada por card.
- Cache por `hash(fonte + candidatos + glossário + prompt + schema)`. Repetição custa zero tokens.
- Prompt estável e curto, exemplos só do mesmo tipo; processamento em lote para aproveitar cache de prefixo.
- Modelo barato monta e revisa JSON; modelo forte recebe apenas exceções e amostra. Métricas obrigatórias: tokens/card, cache hit, escaladas, falhas e retrabalho.

## Gates duros antes de qualquer escala

1. raiz e ordem vivas = manifesto; lote vazio reprova;
2. referência contém somente Kenhub e proveniência estruturada;
3. cada item aprendível tem card ou exceção explícita;
4. nomes PT oficiais; EN só no verso/metadado;
5. `estrutura × vista` preservado, sem duplicata exata;
6. mídia íntegra, hashes estáveis e nenhuma resposta vazada;
7. ponta da seta toca o alvo; haste/caixa não cobrem alvo, rótulos nem marca;
8. caixa dentro da figura, texto cabe, contraste acessível;
9. renderização de 100% em PC e celular, frente e verso;
10. IDs, tags, ordem, comentários, histórico e suspensão preservados;
11. segunda execução é idempotente e não regrava sem delta;
12. uso privado: nada de mídia Kenhub em Git, Drive compartilhado ou APKG público.

Todo gate novo terá teste ruim que precisa falhar; exceção entra numa fila de revisão, nunca é aprovada pelo próprio produtor.

## Execução

### Fase 0 — fundação

Criar `modo=referencia_kenhub` separado da UC07, schema/manifesto, catálogo global, estado retomável, adaptador de coleção e gates G31–G42. Reutilizar apenas sessão/coleta, máscara, modelo e renderizador; não reutilizar regras de seleção/dessuspensão da UC07.

### Fase 1 — piloto

Escolher três unidades não neuro heterogêneas: osso/músculo, víscera/vasos e uma unidade pequena/densa. Produzir 50–150 cards; renderizar e revisar 100%; comparar tema âmbar × ciano; medir custo e erro.

Critério de saída: cobertura e render 100%, zero resposta vazada, zero duplicata exata, zero escrita não idempotente, traduções atestadas e nenhuma correção manual recorrente sem gate.

### Fase 2 — levas com feedback

Rodar **10 unidades por vez**, na ordem oficial e agrupadas pelos módulos do Kenhub. Coleta continua serial; normalização, montagem e renderização trabalham em paralelo. Auditoria integral ao final da leva; parar para feedback de Davi antes da próxima dezena e pausar automaticamente se qualquer gate regredir.

### Fase 3 — escala

Liberar a fila completa em levas de **50 unidades de estudo**, sempre na hierarquia oficial `domínio → módulo → seção → unidade`. Cada leva só fecha com checkpoint de completude: todos os alvos descobertos precisam corresponder a card visual verificado, reuso exato ou card escrito AnKing-like e estar vinculados à aula no Anki vivo. O regulador forte vê exceções + amostra; relatório por módulo e global. Instalação permanece serial e suspensa por padrão. O conteúdo textual dos quizzes será uma leva separada, reutilizando catálogo, identidade, ordem e checkpoints.

### Cobertura integral do Kenhub

O projeto só termina após percorrer todos os cursos não excluídos de Anatomia, Histologia e Fisiologia. Para cada aula, preservar duas camadas auditáveis: **(A)** todos os `learnables` do quiz, sem amostragem, cobertos por visual, reuso exato ou fallback escrito sem figura; **(B)** todos os objetivos, explicações, resumos e legendas aproveitáveis coletados da página, deduplicados e convertidos na fase textual. Cada página registra contagens brutas, hashes e vínculos vivos. “Completo” exige zero aula não visitada, zero alvo sem vínculo e zero trecho aproveitável sem decisão documentada. Neuroanatomia é a única exclusão de conteúdo, porque já foi produzida integralmente na UC07.

## Métricas de aceite

- 100% de itens aprendíveis reconciliados;
- 100% de cards renderizados nos quatro estados (PC/celular × frente/verso);
- 0 mídia ausente, resposta vazada, colisão visual ou escrita duplicada;
- ≥95% resolvido localmente/cacheado; modelo forte em ≤5% dos casos;
- registro do custo total e por card, sem afirmar economia sem medir.

## Decisões fechadas por Davi em 20/10/2026

1. Escopo: anatomia + histologia + fisiologia.
2. Neuro já feita na UC07: excluir da Referência externa.
3. Cards entram todos suspensos.
4. Fase 1: somente identificação visual; texto dos quizzes vem depois.
5. Piloto comparou ambos os temas; Davi escolheu **somente ciano** para a produção e autorizou apagar a duplicata âmbar.

Comando preparado: `./kenhub-referencia preparar`; após OK explícito, `./kenhub-referencia autorizar --confirmar-piloto` e `./kenhub-referencia piloto --dry-run`. A autorização do piloto não autoriza escrever no Anki.
