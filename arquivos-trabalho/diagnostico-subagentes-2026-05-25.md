# Diagnóstico — Subagentes `redator-e1` e `questionador` falhando

**Data:** 2026-05-25
**Sintoma:** ao gerar o resumo de Gliconeogênese via `Task tool`, os dois subagentes Opus customizados falharam:
- **REDATOR-E1** entregou um `etapa1.typ` inteiramente sobre **cadeia respiratória** (tema do último resumo gerado), ignorando completamente o prompt explícito sobre gliconeogênese.
- **QUESTIONADOR** entrou em loop infinito de "Vou ler. Vou começar. Vou ler." sem disparar nenhum tool call de Read, totalizando ~95 linhas de texto vazio antes de timeout.

---

## Hipótese 1 (REJEITADA) — System prompt longo estoura atenção

System prompts: `redator-e1.md` (163 linhas), `questionador.md` (121 linhas) — não são exorbitantes. Modelos Opus aguentam prompts dessa ordem sem comportamento degradado. Plausível como contribuinte, mas não explica os sintomas específicos.

## Hipótese 2 (CONFIRMADA — causa principal) — Contaminação por estado anterior no `typst-build/`

**Evidência:**
- O diretório `typst-build/` contém os arquivos `etapa1.typ`, `etapa2.typ`, `etapa3.typ`, `resumindo.typ`, `main.typ` que persistem entre resumos — cada nova geração sobrescreve os anteriores.
- Quando o REDATOR-E1 foi invocado, esses arquivos ainda continham o **último resumo gerado** (cadeia respiratória). Provavelmente o agent fez Read em `typst-build/etapa1.typ` para "entender o estilo do projeto" como parte das instruções de leitura obrigatória (CHEATSHEET diz "consultar exemplos antes de redigir"), e o contexto de cadeia respiratória contaminou a redação.
- Em paralelo, existe `figuras/cadeia-respiratoria/` com 68 slides — o subagente pode ter listado `figuras/` para encontrar o MAPA_CONTEUDO do tema, viu `cadeia-respiratoria/` antes de `gliconeogenese/`, e fixou nele.
- `EXEMPLARES.md` (724 linhas) tem múltiplas referências a cadeia respiratória (linhas 306, 489, 547, 551, 554) — quando o subagente segue a regra "leia EXEMPLARES.md primeiro", esses exemplares específicos reforçam o contexto errado.

**Mecanismo:** o subagente, ao iniciar, faz uma sequência de Reads para "entender o projeto" e termina priorizando o conteúdo mais recente que vê (`typst-build/etapa1.typ` da geração anterior) sobre o prompt do orquestrador, que descreve o NOVO tema. É um efeito tipo "recency bias" do contexto fresh-loaded sobrepondo o objetivo.

## Hipótese 3 (PARCIALMENTE VÁLIDA) — Falta guardrail de tema no início

Os dois agents começam com "Você é o REDATOR-E1 do pipeline NEBLI..." mas **não exigem** que o agent (a) escreva o tema do prompt em voz alta como primeira ação, (b) liste 3 conceitos centrais antes de qualquer Read de exemplares ou estado anterior. Sem esse guardrail, o agent começa a ler EXEMPLARES e estado anterior antes de ancorar firmemente o tema novo. Combinado com Hipótese 2, fica fácil contaminar.

Para o QUESTIONADOR, o loop "vou ler. vou ler." é provavelmente outro efeito: o agent reconhece que precisa fazer Read mas não consegue decidir QUAL arquivo ler primeiro porque a lista de leitura obrigatória tem 5 itens e nenhuma ordem clara. Cai em paralisia de decisão e cuspira frases de transição sem ação real.

---

## Fix mínimo viável proposto (NÃO APLICADO — aguardando aprovação)

### Fix 1 — Limpar `typst-build/` antes de spawnar subagentes

No ORQUESTRADOR (thread principal), ANTES de invocar Task com `redator-e1`:

```bash
# Mover etapa*.typ e resumindo.typ atuais para arquivos-trabalho/etapas-anteriores/<slug-anterior>/
mkdir -p arquivos-trabalho/etapas-anteriores/<slug-anterior>
mv typst-build/etapa{1,2,3}.typ typst-build/resumindo.typ typst-build/main.typ \
   arquivos-trabalho/etapas-anteriores/<slug-anterior>/ 2>/dev/null || true
```

Resultado: subagente abre um `typst-build/` vazio e não vê o resumo anterior.

### Fix 2 — Bloco "ANCORAGEM DE TEMA" no topo dos 2 agents

Adicionar logo após `Você é o REDATOR-E1...` em ambos `.claude/agents/redator-e1.md` e `questionador.md`:

```markdown
## ANCORAGEM DE TEMA (obrigatório — PRIMEIRO passo, antes de qualquer Read)

Antes de fazer Read em qualquer arquivo, você DEVE produzir como texto de resposta (não como tool call):

1. **Tema canônico:** copie literalmente o nome do tema mencionado no prompt do orquestrador (ex.: "Tema: GLICONEOGÊNESE — bioq-16-gliconeogenese").
2. **3 conceitos centrais:** liste 3 conceitos-chave que você JÁ SABE sobre esse tema (do seu conhecimento geral, sem ler nada ainda). Ex.: "1. Síntese de glicose a partir de não-carboidrato; 2. Hepática + renal em jejum prolongado; 3. Custo de 6 ATP/glicose".
3. **Negação ativa:** declare qual NÃO é o tema. Ex.: "NÃO é glicólise. NÃO é cadeia respiratória. NÃO é Krebs."

Só DEPOIS desses 3 itens você começa a Read os arquivos obrigatórios. Se você se pegar lendo um arquivo que não menciona o tema declarado em (1), PARE e volte ao prompt do orquestrador.
```

Esse bloco custa ~50 tokens de output extra por invocação, mas elimina contaminação de tema anterior.

### Fix 3 — Quebrar `EXEMPLARES.md` em arquivos por categoria

`EXEMPLARES.md` atual tem 724 linhas com 17 categorias misturando exemplos de Sinapse, Enzimas, Membrana, Cadeia respiratória, etc. O subagente lê tudo e o contexto cruza temas.

Alternativa: dividir em `EXEMPLARES/01-dialogo.md`, `EXEMPLARES/02-confusao.md`, etc., e o agent só lê 1–2 categorias específicas baseadas no Tema Card.

**Custo de implementação:** ~30 min de refatoração. **Ganho:** redução estimada de 60% no input do subagente (de ~5k tokens de EXEMPLARES para ~1k tokens), além de eliminar a contaminação cruzada.

### Fix 4 (opcional) — Reduzir verbosidade do system prompt

Os agents têm ~150 linhas cada com regras detalhadas. Algumas regras podem virar referências a arquivos curtos lidos só quando relevante. Trade-off: menos contexto fresh = menos atenção desviada vs. mais idas e voltas de Read.

---

## Plano de teste (sessão futura)

1. Aplicar **Fix 1** (limpar `typst-build/`) — barato, testável imediatamente.
2. Aplicar **Fix 2** (ANCORAGEM DE TEMA) — barato, alto retorno esperado.
3. Gerar 1 resumo novo via Task (tema diferente do último gerado, ex.: "ciclo do glicogênio") e verificar se REDATOR-E1 produz o tema correto.
4. Se ainda contaminar, aplicar **Fix 3** (quebrar EXEMPLARES.md).
5. Se ainda falhar, considerar abandonar delegação e padronizar redação no thread principal.

---

## Recomendação

**Prioridade alta** para sessão próxima:
- Fix 1 (limpar typst-build/ antes de Task)
- Fix 2 (ANCORAGEM DE TEMA nos 2 agents)

**Prioridade média:**
- Fix 3 (quebrar EXEMPLARES.md) — se Fix 1+2 não bastarem.

**Prioridade baixa:**
- Fix 4 — esperar evidência de que verbosidade é problema independente.

Davi aprova qual desses na próxima sessão antes da aplicação.
