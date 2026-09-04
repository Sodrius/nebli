# ERROS.md — armadilhas e feedbacks de processo NEBLI

**Função:** absorve `errosComuns_nebli.md` (memory pessoal) + 9 feedbacks únicos. Faxina canônica 2026-05-29. Consultar **antes de fechar qualquer resumo**.

**Estrutura:** § Erros recorrentes (armadilhas técnicas) + § Feedbacks de processo (como trabalhar com Davi).

**Onde a regra duplicada foi:** 5 feedbacks duplicados foram descartados na faxina porque a regra já vive no `CLAUDE.md` monolítico — paridade de distratoras, fluidez/perguntas ingênuas (substituída pela proibição total de pergunta âncora/retórica), capa sem "Nota de uso", figura ancorada (regra removida 2026-05-28), subagentes-bug-original (resolvido pelo Routing Map de 2026-05-26).

**Auto-correção pós-pipeline disponível em `typst-build/auto_fix_etapas.py`** — roda antes de `precompile-check.py` e remove: `#etapa-header`/`#set-etapa` duplicados, markdown `**bold**`, trailing whitespace.

---

## § Erros recorrentes

### 1. Paridade de distratoras — banda dupla 0.80-1.25 em Q01–Q30

**Sintoma (dois lados):**
- Correta longa demais (ratio > 1.25): aluno acerta por exclusão visual ("a maior é a certa").
- Correta curta demais (ratio < 0.80): sintoma de overfit, distratoras infladas artificialmente — aluno acerta por exclusão invertida.

**Como evitar:** redigir as 5 distratoras ANTES da correta, 25-35 palavras cada com mecanismo plausível-mas-errado do `mapa-confusoes/<slug>.md`. Calibrar correta para entrar na banda. Remediação tem direção: correta longa → engordar DISTRATORAS; correta curta → engordar a CORRETA (nunca inflar distratora com prosa vazia — se não há mecanismo errado para 25-35 palavras, **trocar a distratora**). Relatório das 30 no chat antes de fechar E2. Detalhes em `CLAUDE.md` § Rules globais e `ROLES.md` § Questionador.

### 2. Siglas sem `#sigla()` na 1ª aparição

**Sintoma:** sigla aparece N vezes no texto mas nunca foi declarada. Casos típicos: NADH, NAD⁺, ADP, Pi, cAMP/AMPc, CoA, NADP⁺, FAD, FADH₂, GDP, AMP. Aparecem dentro da expansão de outras siglas mas não ganham footnote próprio.

**Como evitar:** antes de fechar `etapa1.typ`, rodar `grep -oE '[A-Z]{2,}[0-9]?[A-Za-z⁺⁻-]*' typst-build/etapa1.typ | sort -u` e cross-check com `grep '#sigla(' typst-build/etapa1.typ`. Toda sigla no corpo precisa de `#sigla(` antes da 1ª aparição.

### 3. Subagentes Opus customizados aposentados (REDATOR-E1, QUESTIONADOR)

**Status:** APOSENTADOS 2026-05-26. Sessão principal (Claude Code, Opus) acumula os 3 papéis no mesmo thread.

**Histórico do bug:** REDATOR-E1 simulava tool calls como texto inline em vez de disparar Read; QUESTIONADOR loopava em "vou ler" sem disparar Read. Fix de ANCORAGEM em 2026-05-25 não segurou. Refatoração de 2026-05-28 também não — piloto morte celular confirmou 2 spawns Opus reproduzindo o bug. Hipótese: incompatibilidade Opus 4.7 + Agent tool customizado, não problema de prompt. CADERNISTA (Sonnet 4.6) nunca apresentou o bug.

**Como evitar:** **não tentar reabilitar REDATOR-E1/QUESTIONADOR como Task subagent sem mudar modelo.** Opções futuras: (a) manter fundido (default atual), (b) migrar pra Sonnet 4.6, (c) só QUESTIONADOR como Sonnet, REDATOR fica fundido.

### 4. Heredoc atômico `ENAMETOOLONG` no Windows

**Sintoma:** `cat > arquivo.typ << 'EOF' ... EOF` falha para `.typ` > 30k chars no Windows + Claude Code.

**Como evitar:** usar Write tool para gravação inicial de `.typ` grandes. `precompile-check.py` pega truncamento via NULL bytes e última linha incompleta. Heredoc continua válido para `.typ` pequenos (etapa3, resumindo).

### 5. `questao-ce` exige tupla `("I", [conteúdo])`, não `[I. conteúdo]`

**Sintoma:** Typst erro `cannot destructure content` ao compilar etapa2.typ.

**Como evitar:** sempre usar pares:
```typst
#questao-ce("12", badge-integracao, [enunciado],
  (("I", [conteúdo I]), ("II", [conteúdo II]), ("III", [conteúdo III])))
```

### 6. Termo-notas abaixo do alvo (4 em vez de 6–8)

**Sintoma:** alvo canônico é 6–8 `#termo-nota` por resumo; viés do redator é parar em 3–4. Termos categorizados como "comum" são novidade pura para o aluno em dificuldade (biotina, glicose-alanina, von Gierke).

**Como evitar:** Tema Card Seção C lista 6–8 termos-nota nominalmente obrigatórios. Lista vai direto para a sessão redatora.

### 7. Tema-card com teto E1 errado

**Sintoma:** declarar "piso 9, teto 14" ou "teto 20" no Tema Card — ou, a partir de 2026-09-03, repetir o teto antigo de 22.

**Como evitar:** Tema Card Seção A sempre declara "piso 2, **teto 15** páginas" (canônico 2026-09-03, era 22). Alvo mais estreito é permitido dentro disso ("alvo 11-14"), mas o teto absoluto é 15. O teto caiu junto com a mudança de registro (`CLAUDE.md` § Registro científico): 15 páginas é o que sobra quando a prosa perde as frases sem função, não um corte de conteúdo.

**Deixou de ser manual, e depois virou bloqueio (2026-09-03).** Primeiro o `auditar_pdf.py` ganhou `check_paginas_e1`, que conta as páginas entre o banner da Etapa 1 e o do Resumindo. Na mesma data, a pedido de Davi ("garante que os próximos sairão nesse padrão com certeza"), o mesmo check entrou no `pos_pipeline_check.py` como **bloqueio de mover o PDF**. A `§ Missão` continua permitindo estourar o teto quando ensinar bem exigir — mas a exceção passou a ser **declarada**, com `--quebra-declarada "motivo"`; exceção silenciosa deixou de existir. Motivo do endurecimento: enquanto a linha era "manual", as corridas `imuno-07` e `gr-02` v1 fecharam com 25 e 18 páginas sem que nenhum auditor dissesse nada.

### 25 e 26. Forma da E1 e Consolidação decoreba — gates de 2026-09-03

**Por que estes números.** São os que **discriminam**, medidos nos três resumos que existiam quando a regra nasceu:

| Resumo | Palavras | Subtópicos | Páginas E1 | Média das alternativas de Consolidação |
|---|---|---|---|---|
| `imuno-07` (Davi marcou como inflado) | 10.147 | 14 | 25 | — |
| `gr-02` v1 (canônico antigo) | 6.852 | 12 | 18 | 29,3 |
| `gr-02` v2 (registro científico) | 4.770 | 10 | 13 | 11,4 |

**O que NÃO virou gate, e por quê.** Padrões lexicais de baboseira (`vale notar`, `é fundamental compreender`) e de jargão adiado (`(chamado X)`) foram escritos e testados contra os três resumos acima: **não acusaram nada em nenhum**, inclusive no que Davi marcou como inflado. Não servem de gate e não foram implementados — seriam teatro de verificação. O sintoma auditável do registro frouxo é a inflação, e é ela que se trava.

### 8. Página em branco entre etapas (`#etapa-header` duplicado)

**Sintoma:** PDF tem página vazia entre Resumindo→E2, E2→E3, E3→Gabarito.

**Como evitar:** **Auto-fix disponível.** Rodar `python typst-build/auto_fix_etapas.py` antes do `precompile-check.py`. Arquivos de etapa começam DIRETO no conteúdo (intro-box, parte-title, questao-mc) — sem `#etapa-header` ou `#set-etapa` (o `main.typ` já chama).

### 9. Gabarito embaralhado / letra errada (chunking quebrado)

**Sintoma histórico:** UC01-BC-07 marcou letra DIFERENTE da correta em 13/30 (43%) — risco pedagógico bloqueador.

**Como evitar:** **Fix aplicado 2026-05-26 no template.** `gabarito-bloco` agora reordena `items` para column-major em grid de 3 colunas. Validar visualmente: Q01-Q04 coluna esquerda, Q05-Q07 meio, Q08-Q10 direita.

### 10. Header fóssil "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" no gabarito

**Sintoma:** após remoção canônica da E4 em 2026-05-22, PDFs históricos ainda imprimem header da E4 no gabarito.

**Como evitar:** `pos_pipeline_check.py` bloqueia se `pdftotext output.pdf | grep "ETAPA 4"` retornar matches.

### 11. Numeração de página inflada (helper conta página fantasma)

**Sintoma:** rodapé mostra "44" em PDF de 41 páginas reais. Após remoção da E4, contador ainda incrementa páginas que existiriam na E4.

**Como evitar:** validar visualmente — contar páginas reais vs número impresso. Se divergente, ajustar template para reset do counter.

### 12. Cadeia ≥4 setas sem `#figura-nebli` adjacente

**Sintoma:** parágrafos com 4+ setas causais (`→`/`->`) sem figura de cascata adjacente.

**Como evitar:** durante a redação da E1, contar setas por parágrafo. Se ≥4, `#figura-nebli` precisa estar adjacente. Se não há figura no slide, SVG esquemático ou parar a redação até ter.

**Caso confirmatório 2026-05-29 (biocel-07-divisao-celular):** resumo fechado com 35 páginas e ZERO figuras porque Davi não anexou slide. Sessão tratou "sem slide" como "sem figura" — decisão unilateral errada. Warning do precompile sobre cadeia ≥4 setas (eixo APC/C-securina-separatase) foi ignorado. **Reflexo a fixar:** sem slide ≠ sem figura. Alternativas SEMPRE disponíveis: (a) SVG esquemático em Typst nativo (`box`/`rect`/`line`) para mecanismos espaciais; (b) figuras reaproveitadas de resumos vizinhos (`figuras/<tema-irmão>/`); (c) Servier Medical Art (biblioteca livre — pendência grande pós-G20); (d) pausar e perguntar antes de fechar sem figura. Quando o tema tem componente espacial (mitose, anel contrátil, fuso, cascata multi-passo), figura é OBRIGATÓRIA mesmo sem slide.

### 13. Conclusão integradora travada em 3 camadas (falta projeção)

**Sintoma:** `#conclusao-box` cobre "estrutura → mecanismo → clínica" mas falta projeção para o próximo resumo da UC.

**Como evitar:** as 4 camadas obrigatórias: (1) princípio unificador; (2) mecanismo nuclear; (3) clínica retomada com mecanismo; (4) projeção explícita para o próximo resumo.

### 14. Variação de registro homogênea entre subtópicos vizinhos

**Sintoma:** subtópicos consecutivos abrem no mesmo registro. Texto fica previsível a partir da metade da E1.

**Como evitar:** declarar registro de abertura de cada subtópico no Tema Card Seção B.bis. Rotacionar entre (1) enquadramento, (2) integração-anterior, (3) integração-posterior, (4) analogia concreta, (5) ponto-de-quebra. Nenhum par vizinho compartilha registro. **Atenção 2026-05-29:** abertura por pergunta âncora/retórica foi banida — substitui pelos 5 registros acima.

### 15. Markdown `**bold**` vazado em vez de Typst `*bold*`

**Sintoma:** strings tipo `**negrito**` no .typ não renderizam — warning "no text within stars" e perda de formatação.

**Como evitar:** **Auto-fix disponível.** `auto_fix_etapas.py` converte `**X**` → `*X*` automaticamente.

### 16. Excesso de `#atencao-box` (caixas vermelhas), prosa explicativa insuficiente

**Sintoma:** resumos com 3-5 boxes por PARTE viram "pular de caixa em caixa" — perde textura de monitor explicando ao vivo.

**Como evitar:** cota máxima **1-2 atencao-box por PARTE**. Confusões educativas viram parágrafos dialogados ("a confusão clássica aqui é...", "vale notar que..."). Reservar caixa para inversões letais (ex.: cianeto bloqueia o IV não o I — diagnóstico errado mata).

### 17. Flashcards genéricos sem cadeia causal clínica → molecular

**Sintoma:** cards com cloze escondendo palavra acessória, resposta Q→A > 30 palavras, pergunta "o que é X?" em vez de "no cenário Y, qual mecanismo molecular?".

**Como evitar:** 7 regras de `flashcards/_REGRAS.md`: (1) direção clínico→molecular; (2) um card = uma cadeia mínima; (3) formato `**Tema.**` + ≤12 palavras + 1 `{{}}` por frase; (4) ≥2 cards do Mapa de Confusões; (5) teste do underscore; (6) voz NEBLI; (7) auto-contido. **Aritmética RemNote:** cada `{{}}` = 1 card — para 8 reais, são 6 frases-cloze com 1 `{{}}` cada + 2 Q→A.

### 18. Integração disfarçada de Consolidação avançada (Q11-Q25)

**Sintoma:** ~40-45% das Integrações não cruzam dois domínios — pedem mecanismo refinado da mesma proteína/via. Detectado em MORTE-CELULAR (40%), CICLO-KREBS (40%), CADEIA-RESPIRATORIA (41%).

**Como evitar:** antes de redigir cada Q11-Q25, gravar em `arquivos-trabalho/integracao-mapa-<slug>.md` linha no formato `Qxx conecta [A] + [B]` (dois domínios distintos). Se não preenche o `+`, questão volta para Consolidação. Gate operacional único — tipos de cruzamento e padrões de stem em `ROLES.md` § Questionador como sugestão.

### 19. Título da capa grande demais (30pt fixo, sem adaptar ao comprimento do tema)

**Sintoma:** o título do resumo na faixa navy da capa sai visualmente grande demais, principalmente em temas de nome longo ou de duas linhas — engole o espaço da faixa, quebra feio ou aperta contra a meta. Causa: o tamanho é fixo em `size: 30pt` no helper de capa (`typst-template/nebli_v2_apostila.typ:611`), então não importa se o tema é curto ("Glicose") ou longo ("Regulação da glicemia na transição jejum-alimentado") — ambos renderizam no mesmo corpo grande.

**Como evitar:** na **validação visual obrigatória** da capa (antes de mover o PDF), conferir que o título não está desproporcional nem quebrando mal na faixa. Se estiver grande demais, reduzir o `size` do título de capa para o tema em questão — títulos longos pedem 22–26pt; 30pt fica reservado a temas curtos de uma linha. Preferir tamanho proporcional ao comprimento do tema em vez de deixar o 30pt como default cego. Mudança pontual de tamanho no `.typ` do resumo é OK; alterar o template canônico (ex.: tornar o título length-aware de vez) exige aprovação do Davi via amostra antes/depois (regra da pasta `typst-template/`).

**Reforço 2026-07-07 (Davi: "título grande na capa"):** RESOLVIDO na origem — o `size` do título agora é **length-aware** no helper `#capa` (`nebli_v2_apostila.typ:611`): 30pt até ~22 chars, 26pt até 34, 22pt até 48, 19pt acima. Amostra curta/longa validada visualmente (capa cabe na faixa navy sem apertar a meta). O `size` fixo de 30pt deixou de existir. Continua valendo preferir **título enxuto** ("Tecido nervoso", "Ciclo de Krebs") no `titulo` do Tema Card — o degrau salva o caso longo, mas título curto rende capa melhor. Backup do template: `nebli_v2_apostila.typ.bak-2026-07-07-A1`.

### 20. `#termo-nota` com o termo repetido na prosa ("fibra reticular² fibra reticular")

**Sintoma (Davi, 2026-07-07):** ao mandar uma palavra pro glossário via `#termo-nota[fibra reticular][def]`, o termo aparece **duplicado no corpo** — "fibra reticular² fibra reticular". Causa: o helper `#termo-nota(termo, def)` (`typst-template/nebli_v2_apostila.typ:749`) JÁ imprime o termo + a footnote; o redator, por hábito, repete o termo logo depois (`#termo-nota[fibra reticular][...] fibra reticular`), achando que o helper só cria a nota. Não é bug de template — é padrão de redação.

**Como evitar:** `#termo-nota[X][def]` **substitui** a primeira menção de X na prosa — escrever a frase como se o helper *fosse* a palavra X, sem repetir X antes nem depois. Ex.: "A matriz é sustentada por #termo-nota[fibras reticulares][colágeno III, finas e ramificadas], que formam a trama." Auto-check antes de fechar a E1: para cada `#termo-nota[T]`, procurar `T` solto adjacente e remover. Mesmo cuidado vale pra `#sigla("X",...)` seguido de "X" repetido.

### 21. Contador de palavras da E1 do `auditar_pdf.py` fecha a janela no primeiro `#mini-resumo` — ✅ CORRIGIDO 2026-08-28

**Sintoma:** `auditar_pdf.py` acusa um miolo absurdamente curto. Em `correlacao-radio-pato-2` acusou `726` num miolo real de 7227; em `micro-01-morfologia-estrutura-bacterias`, `800` num miolo real de 9784. Warning não bloqueia, mas induz a sessão a "engordar" um miolo que já está no ponto — ou a fechar achando que o resumo saiu raso.

**Causa-raiz (mais ampla do que o registro original de 2026-08-28 supunha):** o contador delimitava o miolo entre a primeira ocorrência de `"Etapa 1"` e a primeira de `"Resumindo"` no texto do PDF. O diagnóstico inicial culpou o autor por abrir um `#mini-resumo` com a palavra "Resumindo" — mas o helper `#mini-resumo` do template **sempre** imprime a etiqueta fixa `"Resumindo até aqui:"` (`nebli_v2_apostila.typ:254`). Ou seja: a janela fechava no **primeiro mini-resumo da E1** em *todo* resumo que usa o helper, independentemente do texto escrito.

**Correção aplicada:** o fim do miolo agora ancora no **banner** da página Resumindo, que sai do extrator como uma **linha isolada** `Resumindo` (regex `^[ \t]*Resumindo[ \t]*$`, buscada a partir do início da E1); a etiqueta do mini-resumo nunca é linha isolada porque vem colada ao conteúdo. Fallback continua o banner da `Etapa 2`. Na mesma passada, a faixa esperada foi recalibrada de `3500-5000` para `3500-10500`. **Recalibrada de novo em 2026-09-03 para `3000-7200`**, quando o teto da E1 caiu de 22 para 15 páginas (`CLAUDE.md` § Registro científico): a ~450 palavras por página impressa, 15 páginas equivalem a ~6.750 palavras, e o teto de aviso fica em 7.200 com folga.

### 22. Sessão remota (nuvem) não vem com `typst` nem com o poppler

**Sintoma (2026-08-28):** numa sessão de Claude Code na nuvem, `typst compile` não existe no PATH e `auditar_pdf.py` morre em `x pdftotext nao encontrado. Instale poppler-utils.` — o pipeline trava sem que haja nada de errado com o resumo. O container remoto clona o repositório, mas não traz o ambiente da máquina do Davi.

**Como resolver (duas etapas, ~1 minuto):**

1. **Typst** — baixar o binário estático e pôr no PATH:
```bash
cd /tmp && curl -sSL -o typst.tar.xz \
  "https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-musl.tar.xz" \
  && tar xf typst.tar.xz && cp typst-*/typst /usr/local/bin/ && typst --version
```

2. **Poppler** — `auditar_pdf.py` e `pos_pipeline_check.py` chamam `pdftotext`, `pdfinfo` e `pdffonts` por `subprocess`. Se o `apt` não estiver disponível, criar os três como *shims* de uma linha sobre o **pymupdf**, que já é dependência do `extrair_slides.py`. O `pdftotext` precisa aceitar `-f`/`-l` (faixa de páginas) e `-` como saída; o `pdffonts`, imprimir as duas linhas de cabeçalho antes das fontes, senão o parser do auditor não casa.

**Nota:** os shims são de sessão, não vão para o repositório. Em máquina local com poppler instalado nada disso é necessário — é armadilha exclusiva de corrida remota.

### 23. Gabarito C/E sorteado antes da redação sai divergente dos itens

**Sintoma (`micro-01-morfologia-estrutura-bacterias`, 2026-08-28):** **6 das 10** questões C/E tinham, no Tema Card, uma sequência diferente da verdade real das assertivas escritas. Nenhum gate automático pega isso: o `precompile-check` só audita paridade de MC e distribuição de letras, e o `verificar_gabarito_resumo.py` confere numeração e formato, não semântica.

**Causa:** a regra do § Gabarito sorteado manda sortear o sinal de cada questão *antes* de redigir. Em múltipla escolha isso funciona, porque a correta é uma só e basta posicioná-la na letra sorteada. Em C/E não funciona: a verdade de cada uma das 4 assertivas nasce do conteúdo no momento em que ela é escrita, e forçar a assertiva a caber numa sequência pré-sorteada é exatamente a "engenharia da resposta" que o canônico proíbe.

**Como evitar (procedimento correto para C/E):**
1. Redigir as 4 assertivas pelo conteúdo, decidindo livremente quais são verdadeiras.
2. **Ler item a item e anotar a sequência REAL** — é este o gabarito, não o sorteado.
3. Só então aplicar a guarda anti-degeneração sobre as sequências reais: sem `CCCC`/`EEEE`, sem `CECE`/`ECEC`, sem que quase todas fiquem 2C-2E (padrão que o aluno explora), e contagem global de C e E próxima do equilíbrio sem ser exatamente 50/50 forçado.
4. Quando a guarda pedir mudança, **reescrever a assertiva** para inverter a verdade dela (isso é autoria e é legítimo) — nunca trocar a letra no gabarito.
5. Gravar a sequência real no Tema Card e regerar o `main.typ`.

O `revisor-gabarito` (Haiku) existe para essa conferência; quando ele não puder rodar, a passada item a item é obrigatória à mão antes de compilar.

---

## § Erros que viram CHECK no pipeline (auditoria automática)

| # | Erro | Detecção | Auto-fix? | Bloqueio |
|---|---|---|---|---|
| 1 | Paridade Q01-Q30 fora da banda | precompile-check | não | sim |
| 2 | Sigla sem `#sigla()` | grep manual | não | warn |
| 3 | Subagente loopa | inspeção output | não | fallback humano |
| 4 | Heredoc ENAMETOOLONG | falha shell | usar Write | sim |
| 5 | `questao-ce` string em vez de tupla | compilação Typst | não | sim |
| 6 | Termo-notas < 6 | grep | não | warn |
| 7 | Teto E1 > 15 páginas (era 22 até 2026-09-03) | pos_pipeline (`check_paginas_e1`) + auditar_pdf | não | **sim** (escape `--quebra-declarada`) |
| 25 | E1 fora de 8-10 subtópicos ou miolo > 6.000 palavras | precompile (`check_forma_e1`) | não | sim |
| 26 | Alternativas de Consolidação com média > 20 palavras (decoreba) | precompile (`check_consolidacao_decoreba`) | não | sim |
| 8 | `#etapa-header` duplicado | precompile + auto-fix | SIM | sim |
| 9 | Gabarito embaralhado | template fix + verificar_gabarito_resumo | não | sim |
| 10 | "ETAPA 4" no PDF | pos_pipeline_check | não | sim |
| 11 | Numeração inflada | visual | não | warn |
| 12 | Cadeia ≥4 setas sem figura | grep heurístico | não | warn |
| 13 | Conclusão sem camada 4 | revisor-didatico | não | warn |
| 14 | Registro homogêneo | revisor-didatico | não | warn |
| 15 | Markdown bold vazado | precompile + auto-fix | SIM | warn |
| 18 | Integração disfarçada de Consolidação | mapa A+B pré-redação | não | sim |
| 19 | Título da capa grande demais (30pt fixo) | validação visual da capa | não | warn |
| 21 | Contagem de palavras da E1 falseada pelo mini-resumo | auditar_pdf (âncora no banner) | SIM (corrigido) | warn |
| 23 | Gabarito C/E divergente dos itens | revisor-gabarito ou passada manual | não | sim |
| 24 | `pre-aula.typ` ausente ou fora da forma canônica | precompile (`check_pre_aula`) | não | sim |

---

## § Feedbacks de processo

Orientações sobre **como trabalhar com Davi**, não regras de conteúdo. Cada item é um padrão a respeitar quando a situação se repetir.

### F1. Modo autônomo de execução

Quando Davi diz "pode rodar", "vai fazendo", "ajustando no caminho": **autonomia total**, auto-correção em loop, perguntar só em ambiguidade conceitual real (não em preferência de estilo). Erros não-bloqueantes → continuar e reportar no final. Padrão de relatório final: ✅ deu certo · ⚠ deu errado/pendências · → próximos passos.

### F2. Verificação automática + checkpointing a cada 30min

Davi NÃO quer "spot-check humano" em fase de verificação — substituir por artefatos verificáveis (arquivos gerados, contagens, marcadores binários em relatórios). Para tarefas longas (>5 itens ou >30min), criar `CHECKPOINT-<operacao>.md` atualizado ao final de cada batch — fase atual, itens concluídos, próximo passo literal se sessão morrer.

### F3. Prosa expositiva > boxes

Resumos NEBLI tendem ao excesso de `#atencao-box` (vermelhos). Cota máxima 1-2 por PARTE. Default é prosa. Confusão educativa vira parágrafo dialogado ("a confusão clássica aqui é..."). Reservar box para inversões com risco letal (cianeto bloqueia o IV — diagnóstico errado mata). Ver erro #16 acima e regra 13 do § Redator em `ROLES.md`.

### F4. Calibração de tamanho da E1 (teto 15 páginas — revisto 2026-09-03)

Quatro alavancas quando o tema é denso e o resumo estoura o teto, **em ordem de aplicação**:
1. **Filtro das três funções** (`CLAUDE.md` § Registro científico): toda frase afirma um fato novo, faz uma ponte causal ou nomeia um termo — as outras saem. É a alavanca de maior rendimento e a única que não custa conteúdo.
2. **Fundir subtópicos conceitualmente irmãos** até chegar a 8–10 no total ("via extrínseca" + "via intrínseca" → "as duas vias para o mesmo destino"). Com teto 15, a PARTE de 5-6 subtópicos deixou de caber.
3. **Máx 2 boxes pesados** (`confusao-prevista` + `atencao-box` somados) por PARTE — o restante vira prosa.
4. **Figuras 50–55%** em resumos com 12+ figuras, reservando 65–80% só para as estruturais críticas.

Aplicar no planejamento (orçamento de páginas prévio no Tema Card), não na cirurgia pós-redação. Empírico da corrida `imuno-07`: reduzir largura de figura sozinha **não rendeu página nenhuma** — o texto é o binding constraint, então a alavanca 1 vem primeiro.

### F5. Figuras: largura 40-80% + relatório auditável

**Largura caso a caso:** 40-50% (detalhe pontual, lateral, ícone), 55-65% (informativa média), 70-80% (cadeia multi-passo, mapa orientador, comparativo lado-a-lado), >80% só se a figura **é** o mecanismo. Default 65% foi aposentado em 2026-05-28.

**Relatório auditável obrigatório no fechamento da E1** (junto do ratio Q01-Q30):

| Figura | PARTE | Origem (slide-XX / externa) | Mecanismo que carrega | Largura |

Convite auditável — força verbalizar "essa figura existe porque…". Não é gate hard, mas a tabela é obrigatória no relatório.

### F6. Contexto MAIOR nos agents, não menor

Subagentes do NEBLI devem **ler mais**, não menos. Token gasto em contexto é barato; qualidade perdida por agent desinformado é cara. Default ao refatorar agent: leitura completa de arquivos prescritivos relevantes. **Não propor lazy-load como otimização** — Davi recusou explicitamente em 2026-05-28. Exceção: arquivo claramente irrelevante (ex.: cadernista lendo `figuras/<outro-tema>/MAPA_CONTEUDO.txt`).

### F7. Anti-engessamento meta-coerente

Regras sobre **voz / fluidez / exemplar / julgamento editorial** não podem ser escritas em tom prescritivo duro. Convites > obrigações. Default > gate. Tom imperativo só para piso técnico (precompile, auditar_pdf, paridade Q01-Q30).

**Sinais de que estou engessando demais:** usar "obrigatório/deve/sempre/exige" em regras sobre voz; criar sub-passos numerados com formato fechado de output; definir tetos numéricos onde julgamento bastava. Caso confirmatório 2026-05-28: minha v1 do plano de Integração propôs cotas rígidas (≥6/15 cruzamentos, ≥8/15 stems integrativos); Davi cortou ao vivo — "lista vira inspiração, padrões viram sugestão, sem cota — operador tem julgamento".

### F8. Flashcards RemNote — aritmética, prefixo, 15s

- **Cada `{{}}` = 1 card no RemNote** (não card multi-cloze). Para 8 reais, são **6 frases-cloze com exatamente 1 `{{}}` cada** + 2 frases Q→A. Empilhar `{{}}` proibido.
- **Prefixo `**Tema.**`** em negrito + espaço + corpo, idêntico nos 8 cards. Resolve auto-contenção no shuffle do RemNote.
- **15 segundos por card.** Frase ≤ 12 palavras *após* o prefixo. Resposta Q→A ≤ 12 palavras. Se cadeia causal não cabe, quebrar em 2 cards consecutivos. Não comprimir jargão para caber.
- **Auto-contido.** RemNote mostra só a frase — sem documento, sem cards vizinhos. Prefixo `**Tema.**` resolve 99%; corpo precisa nomear agente/condição no 1% restante.

Regras completas em `flashcards/_REGRAS.md`. Ver § Flashcards em `ROLES.md`.

### F9. REDATOR-E1 Opus como subagente: bug persistente

**Não tentar reabilitar REDATOR-E1 como Task subagent Opus sem mudar modelo.** Piloto morte celular 2026-05-28 confirmou em 2 spawns: ANCORAGEM correta + simulação de tool calls como texto inline + `tool_uses: 0` + turno encerrado. Hipótese: incompatibilidade Opus 4.7 + Agent tool customizado neste ambiente, não problema de system prompt. CADERNISTA (Sonnet 4.6) nunca apresentou o bug.

Caminhos viáveis (ordem de risco crescente): (1) manter fundido na sessão principal (padrão desde 2026-05-26); (2) migrar REDATOR-E1 para Sonnet 4.6 (testa hipótese, voz pode degradar); (3) só QUESTIONADOR vira Sonnet, REDATOR permanece fundido. Re-spawnar com prompts diferentes NÃO resolve — é determinístico no nível modelo+tool.

### F10. Economia de palavra na E1

**Observado (Davi, 2026-08-31):** *"você tem escrito demais ora falar pouca coisa, dá pra falar mais com menos palavras."* Dito sobre a **E1** do resumo de inflamação — 10.547 palavras, 25 páginas contra o teto de 22, 660 palavras por subtópico. O chat está bom; o que inflou foi a apostila.

**A regra.** Mesma profundidade, menos palavra. Não é cortar mecanismo — é cortar o que não é mecanismo. (O dial `profundidade:` que servia de desculpa aqui foi aposentado em 2026-09-03: profundidade nunca foi licença de verbosidade, e agora nem existe seletor para ela.)

**Os cinco desperdícios a caçar antes de fechar a E1:**
1. **Moldura antes do conteúdo.** Parágrafo que anuncia o que o subtópico vai fazer ("aqui está o problema que o sistema precisa resolver…") antes de resolvê-lo. Abrir já no mecanismo — é o que os 5 registros canônicos pedem.
2. **Legenda que repete o corpo.** A legenda dirige o olhar para o que o texto *não* disse; se ela reconta o parágrafo, uma das duas some.
3. **Repetição do mesmo achado em pontos diferentes.** Se a arquitetura de tempo dos mediadores já foi montada, as reaparições dela são meia frase de retomada, não o argumento inteiro de novo.
4. **Conclusão que reconta.** O `#conclusao-box` amarra em 4 camadas; ele não é um segundo Resumindo. Recontar PARTE por PARTE é gordura.
5. **Duas frases onde uma cabe.** Reformulação ("ou seja", "dito de outro modo") vale 2 ou 3 vezes no resumo inteiro (Categoria 17, manobra 6) — acima disso vira tique.

6. **Frase que não cumpre nenhuma das três funções** (acrescentado 2026-09-03). Generaliza os cinco anteriores: toda frase afirma um fato/passo de mecanismo novo, faz a ponte causal entre dois fatos já postos, ou nomeia/define/delimita um termo. As que não fazem nenhuma das três são as "baboseiras" que Davi nomeou — adjetivo avaliativo sem conteúdo, analogia decorativa, reafirmação com outras palavras.

**Réguas (revistas 2026-09-03).** Alvo **450–550 palavras por subtópico**, **8–10 subtópicos**, **teto de 15 páginas** (era 22) e ~5.000–5.500 palavras de miolo. Estourar o teto é sinal de gordura, não de profundidade — checar os seis desperdícios acima antes de qualquer outra coisa. O dial `profundidade:` que este feedback culpava foi aposentado em 2026-09-03; a profundidade agora é única e definida pela prova, não por um seletor. Na dúvida entre cortar mecanismo e cortar moldura, corta moldura; se ainda não couber, é aí que a `§ Missão` decide (ensinar bem vence o teto) — e a quebra vai declarada no relatório.

**O que a regra NÃO autoriza.** Tirar o "porquê", encurtar cadeia causal, virar bullet, ou trocar prosa por lista para economizar linha. O alvo é o texto que não ensina nada; o mecanismo é intocável.
