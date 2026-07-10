---
description: Gera 8 flashcards clínicos (RemNote) a partir de um resumo NEBLI já compilado
argument-hint: <slug-do-resumo>
---

Argumentos recebidos: $ARGUMENTS

Você é responsável por gerar a **Etapa 4** do resumo NEBLI: 8 flashcards clínicos (6 cloze + 2 Q→A) prontos para colar no RemNote. **Sessão principal executa, sem subagente** (decisão canônica 2026-05-26 — `ERROS.md` erro 3).

## Pré-condições

1. `$ARGUMENTS` é um slug não-vazio (ex: `ciclo-de-krebs`).
2. Existe `resumos-gerados/<SLUG-MAIUSCULO>.pdf` (o resumo já foi compilado e auditado). Se não existir, **pare** e avise o Davi que ele precisa rodar o pipeline do resumo primeiro.
3. Existe `typst-build/_par_<slug>/etapa1.typ` OU `typst-build/etapa1.typ` corresponde ao mesmo tema. Se nenhum dos dois bater, pare e peça o slug correto.

## Pipeline

### Passo 1 — Extrair material clínico bruto

```bash
python typst-build/extrair_clinica.py <slug>
```

Saída esperada: `arquivos-trabalho/clinica-bruta-<slug>.json`. Stderr não-vazio com `ERRO:` → parar.

Leia o JSON inteiro. Os campos relevantes para a redação são:
- `clinica_boxes[]` — caixas azuis com aplicação clínica explícita.
- `atencao_boxes[]` — caixas vermelhas com risco/intervenção crítica.
- `confusoes_previstas[]` — pares "aluno acha X / mecanismo correto Y". **Alvo prioritário da Regra 4.**
- `resumindo_secoes[]` — 8-12 seções destiladas, qualquer uma pode virar cloze.
- `mapa_confusoes_raw` — texto bruto do Mapa de Confusões; se não-nulo, leia-o e identifique 2-4 candidatas de alta alavanca para cloze de discriminação.

### Passo 2 — Ler as regras inegociáveis

Abra `flashcards/_REGRAS.md`. Internalize as 6 regras antes de redigir. **Toda decisão de redação volta a elas.**

### Passo 3 — Ler o `_INDEX.md` para cross-check

Abra `flashcards/_INDEX.md`. Para cada slug já listado, abra rapidamente o `.md` correspondente e verifique se há cloze que duplica exatamente um conceito que você está prestes a redigir. Se houver duplicata literal (ex: cianeto + Complexo IV já saiu em `cadeia-respiratoria`), faça uma de duas coisas:
- (a) refraseie seu card para enfocar um ângulo diferente (ex: antídoto em vez do alvo molecular); OU
- (b) deixe o card e marque no comentário-cabeçalho como "reforço cruzado de `<outro-slug>`" — útil quando o conceito merece reforço.

### Passo 4 — Redigir os 8 cards seguindo o orçamento

Mix obrigatório: **6 cloze + 2 Q→A**.

Distribuição-alvo (use como guia, não como camisa-de-força):
- 2 cloze de discriminação a partir do Mapa de Confusões (Regra 4).
- 2 cloze de cadeia causal central (clinica-box ou atencao-box).
- 1 cloze de cofator/enzima/farmacologia (Resumindo, seção mais densa em mecanismo).
- 1 cloze de antídoto/intervenção ou consequência clínica (atencao-box preferido).
- 2 Q→A: cenário clínico narrado em 1 frase → mecanismo molecular em ≤ 30 palavras.

Se o Mapa de Confusões está ausente, redistribua: 4 cloze de cadeia causal + 2 cloze de discriminação inventada a partir dos `confusoes_previstas` do JSON + 2 Q→A. Sinalize a ausência no comentário-cabeçalho.

### Passo 5 — Auto-verificação (hard gates)

Antes de gravar, percorra esta checklist. Falha em qualquer item → reescreva o card específico.

1. **Contagem real no RemNote.** Conte: cada bloco `{{}}` = 1 card + cada `>>` = 1 card. Total deve ser exatamente 8. Toda frase-cloze deve ter **exatamente 1 `{{}}`** (se tem 2+, quebre em duas frases — cada `{{}}` extra é card extra).
2. **Formato `**Tema.**`.** Todos os 8 cards começam com `**<Tema do resumo>.**` em negrito, idêntico. Esse prefixo é obrigatório.
3. **Tamanho.** Frase ≤ 12 palavras *após* o prefixo `**Tema.**`. Resposta Q→A ≤ 12 palavras. Card respondível em ~15 segundos. Se passar, encurte ou quebre em dois.
4. **Teste do underscore.** Para cada `{{X}}`, leia a frase trocando `{{X}}` por `______`. Se X é inferível pelo contexto, refaça o cloze.
5. **Auto-contenção.** Leia cada card isolado. O prefixo `**Tema.**` resolve a maioria, mas verifique se o corpo não tem "antídoto é Y" sem dizer "de quê", "R6 é também o Complexo II" sem dizer de qual via etc.
6. **Origens.** Cada card deve ter origem rastreável no JSON ou no Mapa. Liste essas origens no comentário-cabeçalho.
7. **Voz NEBLI.** Banidas: "é definido como", "consiste em", "caracteriza-se por", "trata-se de". Substitua por verbo ativo.
8. **Direção.** Cards perguntam do clínico/fenômeno e resgatam o molecular. Não o inverso.

### Passo 6 — Backup se já existe

```bash
test -f flashcards/<slug>.md && mv flashcards/<slug>.md flashcards/_backup/<slug>-$(date +%Y%m%d-%H%M%S).md
```

(Em PowerShell: `if (Test-Path flashcards/<slug>.md) { Move-Item flashcards/<slug>.md flashcards/_backup/<slug>-(Get-Date -Format yyyyMMdd-HHmmss).md }`)

### Passo 7 — Gravar `flashcards/<slug>.md`

Use o esqueleto de `flashcards/_TEMPLATE.md` (HTML comment + bullet pai + cards aninhados). Preencha o comentário-cabeçalho com: slug, tema (título do PDF), disciplina (inferir do slug se prefixo `bioq-/fisio-/biocel-/biomol-`; senão, ler `etapa1_path` e inferir), data, fontes, mix, presença do mapa, lista de origens dos 8 cards.

### Passo 8 — Atualizar `_INDEX.md`

Edite `flashcards/_INDEX.md` inserindo, **entre os marcadores `<!-- BEGIN-INDEX -->` e `<!-- END-INDEX -->`**, uma linha:

```
- [`<slug>`](<slug>.md) — <título do tema> — <YYYY-MM-DD> — 6c+2qa<sinalização opcional>
```

Sinalização opcional: ` · sem mapa-confusões` se não houve mapa; ` · reforço cruzado de <outro-slug>` se algum card foi marcado assim.

Mantenha ordem cronológica (geração mais recente no fim).

### Passo 9 — Reportar no chat

Imprima:
1. Path completo de `flashcards/<slug>.md`.
2. Os 8 cards renderizados (copie literalmente do arquivo).
3. Sinalize "✅ Pronto para colar no RemNote" se todos os gates passaram.
4. Se algum card foi marcado como "reforço cruzado", liste o slug de origem.

## O que você NÃO faz

- **Não modifica `etapa1.typ`, `resumindo.typ`, ou qualquer arquivo do resumo.** O comando é leitor; só escreve em `flashcards/`.
- **Não roda o pipeline do resumo.** Se o PDF não existe, avise e pare.
- **Não delega para subagente.** Sessão principal executa tudo.
- **Não inventa cards.** Toda afirmação tem que ter origem rastreável em uma das 4 fontes (`clinica_boxes`, `atencao_boxes`, `confusoes_previstas`, `resumindo_secoes`) ou no Mapa de Confusões. Se quiser citar algo que está só no corpo da E1 fora dessas caixas, marque explicitamente no campo de origens "E1 prosa, fora de caixa" — mas evite (a caixa já foi escolhida pelo redator como o ponto-chave).

## Quando algo falha

- **Extrator retorna 2 (etapa1 não encontrado):** o slug pode estar errado, ou o resumo nunca foi gerado. Liste os `typst-build/_par_*` existentes para o Davi escolher.
- **0 clínica/atenção boxes:** improvável, mas pode acontecer em tema 100% molecular puro. Avise o Davi e gere os 8 cards usando só Resumindo + Mapa (se houver). Se não houver nem mapa, gere 6 cloze (sem os 2 de discriminação) e mantenha os 2 Q→A; sinalize "sem âncora clínica explícita".
- **Mapa de Confusões parece desatualizado** (formato diferente do esperado): use mesmo assim, é texto bruto.
