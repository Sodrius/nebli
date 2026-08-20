# MEMORY — estado vivo do projeto NEBLI

> **Função:** carrega em toda sessão. Fatos que mudam no tempo (estado, projetos ativos, decisões fechadas, identidade, **diário de revisões**, backlog, histórico). Prescrições ("sempre/nunca") vivem no `CLAUDE.md`. Armadilhas e feedbacks de processo vivem no `ERROS.md`. Papéis do pipeline vivem no `ROLES.md`.
>
> **Faxina canônica 2026-05-29:** absorveu `pendências de melhora.md` (§ Pendências abertas) e `CHANGELOG_CLAUDE.md` (§ Histórico de decisões canônicas em forma compacta). FILOSOFIA.md e ARCHIVE.md deletados (conteúdo já estava aqui ou no CLAUDE.md). Versão completa do CHANGELOG preservada em `backups/pre-faxina-2026-05-29/raiz/CHANGELOG_CLAUDE.md` (619 linhas) — acessar via Read explícito para auditoria histórica anterior a 2026-05-22.

---

## § Active Projects

- **2º semestre 2026 ativo (virada 2026-08-03):** Davi passou para o **2º semestre**, cursando duas UCs em paralelo — **Ciclo da Vida I (UC-16, MSP 3161)** [Pediatria + Geriatria, prova final única 28-29/09] e **Digestório (UC-8, Med5043)** [Anatomia/Histologia/Fisiologia/Embrio, P1 05-08/out · P2 26-30/nov]. Davi é da **Turma B** (usar a coluna Turma B dos cronogramas). Cronogramas assimilados em `cronogramas/` (fontes PDF + digests `ciclo-da-vida-i-uc16-2026.md`, `digestorio-uc8-med5043-2026.md`, `README.md`). Ainda **sem** `banco/aulas_uc16.yml`/`aulas_uc8.yml` (novas UCs não têm banco de questões; resumos usam slide + bibliografia + AnKing). 1º resumo do 2º sem gerado: **Ciclo da Vida I Aula 1 — Crescimento e Desenvolvimento na Primeira Infância** (`pediatria-01-desenvolvimento-primeira-infancia`, Profa. Brentani) — 16 marcos AnKing curados + fila de NEBLIcards para o núcleo conceitual (AnKing é Step 1, não cobre pediatria conceitual BR).
- **Subagentes REDATOR/QUESTIONADOR aposentados (2026-05-26):** sessão principal Claude Code (Opus) acumula ORQUESTRADOR + REDATOR + QUESTIONADOR no mesmo thread. CADERNISTA (Sonnet, pipeline determinístico) e COMPILADOR (local, bash) mantidos. Tentativa de reabilitar REDATOR-E1 em Opus 4.7 falhou em 2 spawns em 2026-05-28 — ver `ERROS.md` F9.
- **Pipeline de cadernos automatizado (2026-05-25):** `typst-build/pipeline_caderno.py` orquestra gerar+render+audit+verify. Agente CADERNISTA em `ROLES.md` § Cadernista. Davi pede "faça a prova X da matéria Y" → `resumos-gerados/CADERNO-UC<N>-<P>.pdf`.
- **Geração 20 (UC01 — 1º semestre):** ✅ ENCERRADA. 30/30 resumos entre 2026-05-14 e 2026-05-21.
- **Remoção da E4 do pipeline (2026-05-22):** PDF termina em E3 + Gabarito. Banco vira calibração + artefato avulso sob demanda.
- **Etapa 4 Flashcards RemNote (2026-05-27):** ativa. `/flashcards <slug>` gera 6 cloze + 2 Q→A em `flashcards/<slug>.md` sob demanda. Parser `typst-build/extrair_clinica.py`. Regras em `flashcards/_REGRAS.md`. Helpers Typst `#neblicard`/`#cloze` continuam no-op no template.
- **Site NEBLI (Next.js, planejado, não iniciado):** plano aprovado em 2026-05-25 em `C:\Users\João\.claude\plans\quero-criar-um-site-floofy-frog.md`. Stack: Next.js 16 App Router + TypeScript + Tailwind + Drizzle/Postgres (Neon) + Vercel Blob + react-pdf + senha boba via env. Pasta `C:\AI use\nebli-site\` (sibling, não dentro do gerador). Design herdado de `lixo/limpeza-2026-05-25/plataforma/plataforma/` (Vite+React com paleta OKLCH navy/gold/cream/ink, Merriweather+Montserrat, 4 telas). MVP 4 semanas. Drive sync via Vercel Cron horário. Usuário único, senha em `NEBLI_PASSWORD` env. **Gatilho:** Davi disser "cria o site" / "começa o site" → ler o plano integralmente antes de tocar em arquivo.
- **Liga de Clínica Médica FMUSP (2026, dormente):** plano fechado em 2026-05-29 em `C:\Users\João\.claude\plans\tenho-uma-prova-de-crispy-cosmos.md`. 2 PDFs NEBLI separados: PDF 1 "Sintomas-chave do raciocínio clínico" (Dor Torácica + Dispneia + Edema, ~35-40pp, slug `liga-clinica-sintomas`); PDF 2 "Fundamentos do bom clínico" (Osler + Uso Racional do Laboratório + MCP/Bioética, ~20-25pp, slug `liga-clinica-fundamentos`). Slides em `C:\AI use\nebli\slides\slides-liga-clinica-medica\`. **Gatilho verbal:** "as coisas da liga de clínica médica" (forma canônica), "gera o PDF 1/2 da liga", "manda os dois", "vai com a liga" → ler o plano antes de tocar em arquivo.
- **Limpa-geral 2026-05-25:** raiz reduzida (plataforma/, Inspiração de FORMA/, template 2.0/, AIbundle.js → `lixo/limpeza-2026-05-25/`). Manifesto em `lixo/MANIFESTO_LIMPEZA_2026-05-25.md`.

## § Scheduled Tasks

- **Faxina semanal Cowork:** planejada mas não criada (tool travou em sessões anteriores). Prompt em `arquivos-trabalho/task_faxina_semanal_prompt.md`.
- **`banco/indice/banco_slim.json`:** roda manualmente via `python3 banco/gerar_slim.py` quando banco é atualizado.

## § Diário de revisões (feedback acumulável com peso dinâmico)

**Função:** quando Davi nota um problema num resumo (mesmo que a regra já exista no canônico), anota aqui. Sessão principal lê esta seção ANTES de gerar qualquer resumo e converte as entradas vivas em **lista de prioridades pra esta corrida**, declarada no Tema Card Seção A.

**Formato fixo:**
```
### 2026-MM-DD · <slug do resumo>
- **Observei:** <o que Davi viu>
- **Regra envolvida:** <link pra regra no CLAUDE.md ou ERROS.md, se existir>
- **Peso:** alto | médio | baixo
- **Decai em:** <N resumos ou data>
```

**Mecânica de decaimento:** peso alto → médio após 5 resumos consecutivos sem reincidência; → baixo após mais 5; → arquivado. Davi pode resetar a qualquer momento dizendo "isso aqui ficou ruim de novo".

**Como Davi anota:** simplesmente dizer "anota no diário: no resumo X, problema Y, peso alto" — sessão principal grava a entrada e confirma. Sem ritual.

**Entradas:**

### 2026-05-29 · biocel-07-divisao-celular
- **Observei:** Davi pediu "100% do zero" sem anexar slide, e a sessão entregou 35 páginas SEM nenhuma figura. Tratei "sem slide" como "sem figura possível" — decisão unilateral errada. Coreografia espacial (mitose, anel contrátil, eixo APC/C-securina-separatase) precisava de figura mesmo sem slide do professor.
- **Regra envolvida:** Redator-E1 regra 7 (figura é canônica, slide é PRIORIDADE não única fonte) + ERROS erro 12 (cadeia ≥4 setas sem figura — warning saiu e foi ignorado).
- **Peso:** alto
- **Decai em:** 5 resumos sem reincidência

## § Pendências abertas

Backlog vivo (absorveu `pendências de melhora.md` em 2026-05-29; itens já executados foram podados ou movidos pra § Histórico). Revisitar antes de cada sessão.

### Canonizados 2026-07-12 (sancionados a construir)
- **`paridade_fix.py`** — aid pré-compilação: sugere alongar a correta OU as distratoras pra cair na banda 0.80-1.25 **antes** do relatório de ratio da E2. É o único bug do backlog técnico com ganho real (paridade é o gate que mais falha). Sancionado por Davi.
- **Helper `#roxo-box`** no template (via `frontend-design` na 1ª apostila que usar) — a 4ª caixa: roxo = "algo a mais que agrega, fora do que a aula deu" (legenda vermelho=confusão prova · azul=clínica · amarelo=Mapa de Confusões · roxo=aprofundamento). Regra já em `CLAUDE.md` § Profundidade item 4.
- **`.apkg` por deck-aula → Drive automático + upload de resumo/slide pro Drive** — pedido de Davi. **Viável e não difícil, MAS gated em auth Google Drive uma vez (rclone).** Fluxo: `exportPackage` (AnkiConnect) por deck → `rclone copy` pra pasta da UC; e `rclone copy` do PDF+slide com naming "<aula curta> + Etapas 1 a 3 + <sigla prof>". Setup: `rclone config` (OAuth Google, ~5 min, Davi clica autorizar — dá pra fazer do celular com token). **Montar deck-aula de TODAS as aulas passadas** = plano grande, viável incremental (cada aula = curadoria + gate + apply), casar com o .apkg→Drive.

### Chuva de ideias 2026-07-07 (triada — norte: reter medicina a longo prazo, NEBLI como monitor)

**Contexto:** Davi despejou ~45 ideias numa sessão. Escopo executado nessa mesma sessão: consertos de matching de card (`buscar_tags_lote`), ancoragem da checklist nos subtópicos (`gerar_checklist`), remoção do "Onde aprofundar", bandeiras redefinidas, RemNote aposentado, bug termo-nota → ERROS #20, pycache limpo. O que ficou de pendência, por prioridade:

**P1 — Cobertura de card (continuar o que começou):**
- **Fila pendente-gerado → cards NEBLI autorais.** Depois que `verificar_cobertura` marca subtópico como LACUNA/PENDENTE-GERADO, gerar card NEBLI autoral (calibrado, ver [[calibrar-antes-de-gerar-cards]]) pra tapar. Ordem de prioridade do Davi: (1) curar bons AnKing, (2) achar outros decks, (3) criar autoral. Incluir **cloze de imagem tirada do slide** quando o conceito é visual.
- **Auditoria de pertinência dos dessuspensos (bandeira laranja).** Modo `--laranja` no monitor: card flag:2 = "audite se faz sentido no que estudo"; NEBLI julga pertinência ao subtópico, sugere suspender/substituir. Ver [[bandeira-vermelha-21h]].
- **"Mais cards, Davi poda o resto."** Afrouxar teto 30-50; NEBLI cobre com folga (recall alto), Davi suspende manualmente o nada-a-ver e pede substituição do mal-escrito. Precisão migra pro fim (humano), recall pro começo (máquina).
- **Ledger cumulativo (NEBLI-monitor de verdade).** Índice do que já foi coberto por aula → não repete card entre aulas, sabe onde aprofundar, e habilita fisiopatologia por camadas só quando o pré-requisito já foi estudado.
- **Playlists de YT como fonte de cobertura** (além da E1) — o que um bom vídeo do tema cobre vira checklist adicional.
- **Quantos cards/dia:** montar a aritmética FSRS (X novos/dia → Y revisões estacionárias → Z min) pra Davi regular sem comprometer a faculdade. Escalável lá na frente.
- **`.apkg` por aula no Drive + upload automático pelo Claude** (ver Infra abaixo).

**P2 — Qualidade E1/E2 (deixadas como pendência a pedido de Davi, calibrar em piloto antes de canonizar):**
- **Bloco ROXO na E1** — "algo a mais que agrega na formação, não visto em sala mas diretamente relacionado". Nova cor: vermelho=confusão de prova, azul=clínica, amarelo=confusão elaborada no mapa, **roxo=expansão formativa**. Exige helper novo no template (aprovação Davi via amostra).
- **E1 aprofunda "um pouquinho" em tópicos relacionados não vistos em sala.** Grande minoria, onde for útil. Definir critério ("onde o mecanismo fica coxo sem isso").
- **Etapa cards→E1 (pós-E3, pré-compile).** Depois de escolher os cards, a minoria que agrega e não está na E1 é costurada na prosa → cobre mais conteúdo e reduz card sem contato prévio.
- **E2 integração mais difícil e criativa** — cobrar periféricos relacionados não mencionados na E1; subir o nível ao longo do tempo.
- **E2 aplicação estilo USMLE** — cenários que estimulam raciocínio clínico geral (pensar como médico). Comparar com vinhetas USMLE reais.
- **Distratoras que roubam pedaços da correta** e **apontam pra outros subtópicos** (misturar subtópicos) → força saber o mecanismo, não reconhecer.
- **Tópicos/tabelas subusados** — usar quando facilitam visualização de conteúdo que precisa ser decorado (reforçar gatilhos da Categoria 18 do EXEMPLARES).
- **Legenda rica em foto de peça anatômica real / corte histológico** — Davi tem provas práticas; a legenda deve traduzir o conceito pra vida real.
- **Curadoria de imagem por "aqui vale visualizar?"** — em cada trecho, perguntar se algo ganha sendo visto; se sim, imagem. Exemplar + curadoria de livros didáticos ensina o tipo de mecanismo que pede figura.

**P3 — Infra / token / expansão (projetos):**
- **`.git` = 2.8G (elefante de disco).** Daemon de auto-commit versiona PDFs/PNGs binários toda sessão. **Fix (requer OK de Davi, destrutivo):** `.gitignore` pra `figuras/*.png`, `resumos-gerados/*.pdf` (para o sangramento futuro) + eventual `git gc`/filter-repo pra encolher histórico. NÃO tocar sem confirmação. NB: disco ≠ context overload (git não entra no meu contexto; o que pesa contexto são CLAUDE/MEMORY/ERROS/ROLES + memory recall).
- **Upload pro Drive organizado** (resumo + slide + `.apkg`, nome do jeito do Davi) — pasta-alvo: `drive.google.com/drive/u/0/folders/1D9cPEn40EQl7sKx1z8KIZZ7lzBqFa5_8`. MCP Google Drive disponível.
- **Email da bandeira via API do Claude** (em vez de `claude -p`+SMTP) — levantar custo estimado.
- **Economia de token no pipeline inteiro:** Sonnet em papéis já isolados (compilador/revisores/cadernista — cortes seguros); IA local (Ollama) pra compilar/validar; mais scripts/skills determinísticos; **NÃO** mover redação de E1/E2 pra Sonnet sem auditoria (risco de qualidade). Medir % cortável.
- **Fisiopatologia de doenças no deck, por camadas.** Incluir cards de fisiopatologia SÓ com um caminho fácil de aprender antes, com conceitos que Davi já tem — senão erra por falta de contato, não por dificuldade, e o card auto-suspende. Maturar como expandir de forma organizada ao longo dos conteúdos.
- **Reestudar 1º semestre?** Como compensar o que vai esquecer. Decisão estratégica pendente — provável resposta: curadoria de retenção via Anki dos temas já dados, não reestudo do zero.
- **Site de questões (Vercel + Supabase)** pra responder pelo celular — já em § Active Projects como "Site NEBLI".

### Pipeline

- **`gerar_main.py` quebra com `*` literal em tag do "Onde aprofundar" (achado 2026-07-03).** Tags AnKing com nó especial (`::*Anatomy`, `::*Basics`, `::*Lymph_Node_Clusters`) têm `*` que o `_esc_typst_content` preserva (ele mantém `*` de propósito pro negrito dos rótulos `*Cobre melhor*`), e o Typst lê como negrito não-fechado → "unclosed delimiter". **Workaround atual:** usar a tag-pai sem o `::*Folha` (o dessuspender pega os filhos com `tag:X::*`). **Fix real pendente:** no `_esc_typst_content`, escapar `*` que vem logo após `::` ou `_` (contexto de tag), preservando o `*` de negrito dos rótulos. ~10 linhas.

- **Unificação dos 3 auditores Python.** `typst-build/` tem 5 scripts com responsabilidade parcialmente sobreposta (`precompile-check.py`, `auditar_pdf.py`, `auditar_pdf_visual.py`, `pos_pipeline_check.py`, `auto_fix_etapas.py`). COMPILADOR roda 3-4 passes redundantes por resumo; falha tem 3 lugares possíveis. Proposta: manter `precompile-check.py` como gate único pré-compilação + criar `audit.py` unificando textual+visual+fóssil pós-compilação com flags `--textual`/`--visual`/`--full`; migrar lógica de `pos_pipeline_check.py` para o precompile; aposentar `auto_fix_etapas.py` quando precompile barrar duplicatas direto. **Não-objetivo:** consolidar `auditar_caderno_*.py` no mesmo movimento. **Quando atacar:** após pausa entre Gerações 20→21.

- **Hook auto-auditor visual (BLOQUEADO 2026-05-26).** `auditar_pdf_visual.py` não rodava consistentemente em PDFs de 26-mai (Diferenciação, Cadeia Respiratória, Biocel-07). Solução: hook PostToolUse:Bash em `.claude/settings.json` chamando `.claude/hooks/auditar_pdf_recente.ps1`. Criação de script foi negada pelo classificador de auto-mode. **Para desbloquear:** Davi adicionar permissão `Write(.claude/hooks/**)` em `.claude/settings.local.json`. **Mitigação:** slash command `/auditar <slug>` permite invocação manual.

### Pipeline de simulados inéditos por prova

Pedido de 2026-05-22. Pipeline que, dado conteúdo de prova segundo cronograma, gera **simulado inédito** com questões novas (não-presentes no banco) para Davi usar **antes da prova**. Inputs: cronograma da UC + resumos NEBLI já gerados + slides do professor + banco histórico (calibração de nível/taxonomia/armadilhas). Output: PDF estilo NEBLI (capa navy, identidade) com 20-30 MC + 3-5 discursivas + gabarito explicado. Diferente do caderno-de-questões (que é anônimo e usa banco histórico). **Sub-pendências a esclarecer com Davi:** quantidade parametrizável? Subagente novo `simulador-prova`? Versionamento (v1, v2)? Onde armazenar (`simulados-gerados/`)? Discursivas com modelo ou completo? Esboço de arquitetura em `typst-build/gerar_simulado.py` + `.claude/agents/simulador-prova.md`.

### Aguardando empiria

- **Token economy (B2):** modo observação contínua em `arquivos-trabalho/observacao_tokens.md`. Sprint A (baixo risco) decidido após 3-5 resumos medidos da G20; Sprint B conservador depois; Sprint C (pipeline 2 fases) descartado por risco arquitetural.
- **`#mapa-parte` aplicado em resumo real (L5 Fase 2-3):** helper pronto. Aplicar em Glicólise; critério de aprovação: olhando só o mapa, identifica o que a PARTE ensinou? Se passar, vira canônico + Exemplar 19.

### Manutenção pós-G20

- **2.2 Auditoria semântica no `precompile-check`.** Cobertura dupla por subtópico, densidade, boxes por subtópico, footnotes `#sigla` (5-10). ~150 linhas, meio dia.
- **2.3 Pipeline 2-passos E2.** Sonnet redige 30 questões, Opus revisa em 1 passada (paridade, distratoras, cobertura). -40% Opus por resumo sem perda.
- **2.5 Diário prova ↔ resumo.** Quando Davi tiver gabarito de P1/P2, ligar erros aos subtópicos (foto + OCR + matching).

### Pacote pós-G20 grande (gatilho disparado 2026-05-22)

- **Marker como camada B do `extrair_slides.py` (OCR fallback).** Pendente.
- **Ollama local (Qwen 2.5 7B Q4)** — extração de siglas, validação de paridade, auditoria de Tema Card. Pendente.
- **SciDraw + Servier Medical Art** — adoção ad-hoc, não vira marco. Pendente.

### Ideias pequenas (revisitar a cada 5 resumos)

- **I2 — Quebra de página com imagem na E2.** `block(breakable: false)` em `#questao-mc` quando há figura.
- **I3 — Paleta NEBLI por evidência de concentração/foco.**
- **I4 — Auditor reporta contagem de palavras da E1.** Aviso fora da faixa 3.500-5.000.
- **I8 — Análise visual sistemática da apostila do Poliedro.** Pegar 3-5 páginas, decompor o que funciona, mapear o que NEBLI já faz parecido e o que falta. Pasta `Inspiração de FORMA/` é ponto de partida.

### Projetos grandes (longo prazo, dormentes)

- **Podcast NEBLI (E1 audiotrack).** TTS adaptando cada resumo a episódio curto.
- **Plataforma web Vercel.** Substituiu pelo plano de "Site NEBLI" em § Active Projects.
- **Tier 3 propostas** — UI editável de Tema Card, banco colaborativo turma 114, SRS inteligente, mini-resumo on-demand.

## § Histórico de decisões canônicas

### 2026-08-20
- **Resumo `radiologia-02-principios-fisicos` gerado — "Física dos métodos de imagem" (Radiologia, Preceptoria FMUSP).** Fonte: 3 transcrições de aula anexadas por Davi (Princípios da Radiografia convencional e da USG — Raphael Oliveira; Princípios da TC — Mauricio R. M. da Silva Filho; Princípios da RM — César, neurorradiologia). Pedido explícito: "um capítulo generoso por exame e bem aprofundado, sem perder fluidez". **Duas exceções declaradas ao default canônico, aprovadas pelo escopo do pedido:** (a) **E1 em 4 PARTES**, não 3 — um capítulo por método (RX · USG · TC · RM), porque as 3 aulas cobrem 4 exames; (b) **teto de páginas da E1 elevado de 22 para ~38** nesta corrida, por ser material de 3 aulas somadas. 57 pp no total, 38 figuras (todas do slide dos professores), 20 subtópicos, 11 termo-notas, 4 siglas, Resumindo em 1 página com 9 seções. E2 PROFUNDO 8/17/5 (Q01–Q08 · Q09–Q25 · Q26–Q30), 20 MC + 10 C/E de 4 itens + 3 "assinale a incorreta"; paridade 20/20 PASS na banda dupla (média 1.04, máx 1.20); gabarito sorteado A4·B4·C4·D4·E4, sem corrida. Mapa de confusões com 101 itens (20 subtópicos × ≥5) + mapa de integração A+B para Q09–Q25. Master 18,0 MB → leve 4,55 MB.
- **`gerar_main.py`: faixa do gabarito passa a ser derivada dos dados, não fixa.** Os rótulos do gabarito consolidado eram literais `Q01–Q10 / Q11–Q25 / Q26–Q30`, o que imprimia faixa **errada** em qualquer distribuição fora do PADRÃO (PROFUNDO 8/17/5, SUPERFICIAL 12/13/5). Novo helper `_faixa(items, fallback)` calcula min/max dos números presentes em cada bloco; fallback preserva o comportamento antigo quando o bloco vem vazio. Detectado na validação visual desta corrida (imprimia "Consolidação (Q01–Q10)" com apenas 8 questões).
- **Armadilha nova de renderização: expoente Unicode mistura duas fontes.** `10¹⁶` saiu tipograficamente quebrado porque `¹²³` (Latin-1) existem no Merriweather e `⁰⁴-⁹⁻` (bloco U+2070) não — caem no fallback, com tamanho e peso diferentes. Verificado com amostra compilada. Trocado por math mode (`$10^(-12)$`, `$10^(16)$`); `B₀` virou `B#sub[0]` no conteúdo e "campo principal" nas strings (título de `#subtopico` e sumário do Tema Card não aceitam markup). Fórmulas químicas correntes (H₂O, NAD⁺, FADH₂) seguem OK — o problema é a mistura dentro de um expoente multi-dígito. Registrado como `ERROS.md` #21.
- **Falso-positivo conhecido de `auditar_pdf.py` (aviso, não bloqueia):** a contagem "palavras E1" delimita o miolo entre a 1ª ocorrência de "Etapa 1" e a 1ª de "Resumindo" — e o helper `#mini-resumo` imprime "Resumindo até aqui:". Em resumo com mini-resumo cedo, a contagem para no 1º deles (aqui: 1035 em vez de ~12.500). Contar por `pdftotext` até o banner real quando o número parecer absurdo.

### 2026-08-03
- **Deck-aula COMPLETO dentro do `/resumo` + já no Anki (pedido de Davi: "sempre gerar o deck-aula com neblicards + curados anking e outros decks... completo e já no anki cada deck").** Reverte a regra de deferir NEBLIcards autorais para sessão separada — `PENDENTE-GERADO` deixa de ser estado de ship. Toda corrida de `/resumo` monta o deck-aula das **3 fontes em ordem de prioridade** (1. AnKing curado → 2. decks externos de referência [BlueLink/Dope/Histo/LLU/Dorian] → 3. NEBLIcards autorais para lacuna tipo-a) numa árvore `NEBLI::<UC>::<Prova>::<Componente>::<Aula>` por cópia (fontes intocadas), dessuspenso e sincronizado. **3 decisões de Davi:** (a) autorais entram **auto-dessuspensos** (aparecem no estudo já; QA fina pós-hoc pelas bandeiras); (b) **card-mirror roda SEMPRE por ora** — período de aprendizado do gerador, relaxar quando não render mais benefício (lint_neblicard sempre; e1_e2_contract sempre); (c) **lacuna nuclear sem card bom BLOQUEIA** o fechamento (gate_deck_aula_completo --verify-anki, hard). Wiring: `CLAUDE.md` § Profundidade (novo bloco "DECK-AULA COMPLETO DENTRO DO /resumo"), `FLASHCARDS.md` (§ Pipeline por aula reescrito + § NEBLIcards "Quando gerar" revertido), `.claude/commands/resumo.md` passo 11 (e2 externos, e3 autorais, f montar+apply, g gate hard, h ritmo+apkg) + § Gate deck-aula completo. Infra já existe: `montar_deck_aula.py`, `build_card.py --canonical`, `lint_neblicard.py`, `card_mirror_blind.py`+agente card-mirror, `copiar_externos_para_deck.py`, `gate_deck_aula_completo.py`, `e1_e2_contract.py`. `.apkg`→Drive segue gated em rclone.

### 2026-07-11
- **Teste do pipeline de cards: 3 deck-aula recurados do zero + gate absoluto + busca por conteúdo + plano de pesquisa (pedido de Davi).** Deck de teste separado `UC02::Componente::Aula` (Biologia Molecular/DNA-mutação-reparo=biomol-25; Bioquímica/aminoácidos=bioq-23, lipídeos=bioq-21), **cópias** (não move; AnKing intacto) auto-contidas (só tag `NEBLI::<slug>`, sem `#AK`), dessuspensas e sincronizadas. Novo script `copiar_curadoria_para_deck.py`. Faxina "fresh": apagados 56 mapa-confusoes + 14 curadorias + 20 artefatos (recuperáveis via git); memória do pipeline intacta; `_INDEX.md` resetado. **Diagnóstico da curadoria antiga ruim:** `buscar_tags_lote` casava keyword × caminho-de-tag → lacunas fantasma. **Correção Estágio 1 (aplicada):** `descobrir_cards_por_conceito.py` busca por CONTEÚDO (findNotes no texto), filtro IDF (tira factor/base/mutation) + filtro meta-tags; limite = polissemia de keyword ("repair" casa hérnia) → recall-orientado, Camada 2 faz precisão; conserto real = embeddings (no plano). **GATE ABSOLUTO (CANON, CLAUDE.md):** card de deck-aula NUNCA no deck se o conceito não está na E1; aprofundamento entra **pela E1** (AnKing propõe→Orquestrador injeta 1-3 frases→vira card); sem etapa de E1, trava seco. `FLASHCARDS.md` § Regras de busca e admissão (B1 conteúdo, B2 gate, B3 dosagem periférico ≥8/10 + baixa carga de pré-requisito = flexibilidade do Orquestrador, B4 clínico poucos-e-naturais, B5 menos-é-mais). Estágio 3 (dedup/mecanismo/narrativa) **recusado por Davi** — não aplicado. Plano `flashcards/PLANO-PESQUISA-CARDS-IA.md`: 4 correntes (dissecar corpus AnKing, princípios SuperMemo/Matuschak/Nielsen, estado-arte repos IA [raine/anki-llm, AnkiAIUtils, clanki-MCP], busca semântica) → rubrica do bom card + spec de geração + completude mútua E1↔deck. Banco vazio p/ essas aulas (0-1 q) → lacunas tipo-a só cobríveis por card NEBLI gerado da E1 (Fase 2, após calibrar). Ver [[busca-cards-dirigida-conceito]], [[calibrar-antes-de-gerar-cards]].

### 2026-07-10
- **Regras de card R9-R12 + bandeiras + proporcionalidade + migração física p/ `flashcards/` EXECUTADA (pedido de Davi na mesma sessão).** R9 card autoral = cloze deletion 1-por-card + Extra sucinto + imagem quando viável; R10 menos-é-mais (poucos da aula > muitos sem relação; ótimo = aula + um pouco mais fundo); R11 subtópicos maiores representados proporcionalmente mais (E1 e cards — refletido no § Aprofundamento do CLAUDE.md); R12 norte E1-E3+cards mais fundos com menos atrito (ver [[feedback-cards-e-resumos-mais-fundos]]). **Bandeiras:** Ctrl+1 quebrou → laranja=vermelha (`--bandeira` coleta flag:1 E flag:2); verde=bom card→exemplar; ao ver marcados, julgar se mereciam o deck (marcado ~ não explicado na E1). **Migração:** scripts/curadoria/addon/deck-cards/export → `flashcards/`; RAIZ dos 13 scripts +1 nível, verificado (compilam + acham os dados); refs atualizadas em CLAUDE/ROLES/FLASHCARDS/resumo.md/INFRA-REMOTO/docstrings/14 memórias; git mv reversível. Pendências: add-on dúvida-no-Anki, add-on dicionário médico grátis, pesquisa GitHub repos IA-deck, deck-aula espelhando Drive NEBLI. Limpeza conservadora: só dedup no FLASHCARDS (bandeira 3×); CLAUDE/ERROS intactos de propósito. Processo de cards em evolução ativa.
- **Regras gerais de curadoria de cards R1-R8 + lar `flashcards/` canonizados (pedido de Davi após comparar o resumo embrio com os 50 cards curados).** Diagnóstico: o deck cobre bem *derivados* (folhetos, crista, mesoderma, DTN) e mal *processo* (EMT=0, dobramentos=0, linha-primitiva-organizadora/membranas=1) — descasamento estrutural (AnKing drilla "X→Y"; a aula ensina mecanismo), não erro de curadoria. Davi sentiu que o "match forte" era superestimado (conceito similar contava como cobertura). Gravado em `FLASHCARDS.md` § Regras gerais: R1 nada órfão (todo card respondível pela E1; senão E1 sobe via loop), R2 cards um tico mais fundos que o slide → E1 além, R3 Ctrl+1 suspende/email dessuspende, **R4 admissão em 3 baldes (ANCORADO/ANCORÁVEL-via-patch/FORA) — flexível, substitui o "critério rígido" que Davi rejeitou**, R5 sobra-mas-bom tem 2 destinos, **R6 cobertura quali+quanti com rubrica 0-3 por subtópico** (1=conceito-similar=falso forte), R7 podar Step 2 no pré-filtro, R8 relatório reporta os 2 eixos. Nova pasta `flashcards/` = hub (README + EXEMPLARES-CARDS + ANTI-EXEMPLARES-CARDS + estrutura-deck-mestre + cards-nebli/). Deck-mestre espelha FMUSP (Modelo B: changeDeck p/ `NEBLI::UCxx::NN_Componente::PX-NN_slug`, ordem por cronograma). Consolidação física → flashcards/ foi EXECUTADA na mesma data (ver entrada R9-R12 acima). Ver [[regras-curadoria-cards-r1-r8]].
- **Resumo embrio-gastrulacao-neurulacao gerado (Embriologia, UC02/P3 — combina embrio-02 gastrulação + embrio-03 neurulação + dobramento do corpo; docente Marilene H. Lopes).** 35 pp, blueprint MÉDIO. E1 em 3 PARTES (gastrulação/folhetos → neurulação/tubo neural/crista → mesoderma/dobramento) + conclusão integradora; 9 figuras do slide; ~3661 palavras. E2 com paridade 21/21 PASS (banda dupla), gabarito sorteado A4·B4·C4·D5·E4 sem corrida, 9 C/E variados (falso em posições diferentes, sem CCCE degenerado), 2 "assinale a incorreta". Mapa de confusões (21) + integração A+B gravados. Master 16,3 MB → leve 1,62 MB (10×). **Curadoria AnKing: SÓ SELEÇÃO (offline).** `buscar_tags_lote` deu 0 (bug termos EN multi-palavra); cobertura veio do mapeamento das subárvores de embriologia no export (6/12 COBERTOS, 4 parciais, 2 lacunas — EMT e dobramento não são drillados no Step 1). **Apply+sync BLOQUEADOS: não há Anki vivo nesta máquina (sem container Docker/imagem/perfil).** Davi escolheu deixar a seleção pronta e aplicar depois. Plano em `flashcards/curadoria/embrio-gastrulacao-neurulacao.md` com comando pronto. Ver [[retomada-anking]].
- **Loop card→E1→E2 rodado como piloto (pedido de Davi: "roda o loop e1 e2 e o slide regular o conteúdo").** Após a seleção offline de cards, a E1 recebeu **1 injeção mecanística por subtópico (11 no total, +882 palavras → 4543)**, cada uma colada a um mecanismo que o slide já abriu e com profundidade calibrada pelo que o AnKing/livro trata como núcleo. Injeções: anexos extraembrionários (âmnion/saco vitelino), cílios do nó→lateralidade/situs inversus, EMT→metástase, notocorda→SHH, indução como remoção do freio BMP, luz do tubo→ventrículos/canal central, AFP+poli-hidrâmnio (detecção de DTN), crista→Hirschsprung, somito→esclerótomo/miótomo/dermátomo, dobramento→descida do coração/frênico C3-5, intestino ant/médio/post→artérias + ânus imperfurado. E2 atualizada em 5 pontos (SHH, esclerótomo/miótomo/dermátomo, Hirschsprung, 3 porções do intestino, cílios/lateralidade) sem quebrar paridade (0.80-1.25) nem gabarito. **Regra-mestra canonizada:** slide regula O QUE entra; AnKing/bibliografia regula ATÉ QUE PROFUNDIDADE; se não há onde encaixar, não encaixa. Backlog das demais ideias (estudo do corpus AnKing, bibliografia em pasta, deck-aula→deck-mestre, image occlusion) em `PENDENCIAS.md` (novo, raiz).
- **Canonização do aprofundamento + loop + índice de completude (pedido de Davi: "adiciona essas coisas no pipeline canônico").** Três regras novas gravadas nos 4 arquivos vivos: (1) **passe de aprofundamento da E1** (≈1 injeção mecanística/subtópico; slide regula O QUE, AnKing/bibliografia regula ATÉ QUE PROFUNDIDADE; se não encaixa, não injeta) — `CLAUDE.md` § Aprofundamento + `ROLES.md` Redator diretriz 17; (2) **reordenação:** seleção de cards + aprofundamento ANTES da E2 (a E2 sobe de teto junto; cards do AnKing *induzem* os aprofundamentos e vão pro deck-aula) — `FLASHCARDS.md` § Pipeline reordenado + `.claude/commands/resumo.md` passo 6b; (3) **Índice de completude 0-10 × 3 eixos** no relatório de fechamento (E1×slide meta 8-9 "vai um tiquinho além", E2×E1 ≥8, Cards×E1 ≥7) — `ROLES.md` § Índice de completude. Tudo convite auditável (F7), não gate hard. Norte: E1 além do slide → base durável → reflete na E2 e nos cards.

### 2026-07-07
- **Compactação reforçada como passo explícito do `/resumo` (pedido de Davi: "adiciona a compactação como canônica").** Já era canônica desde 2026-07-03 (ROLES § Compilador passo 9), mas o comando `/resumo` não a invocava — só documentava. Agora o passo 9 do `.claude/commands/resumo.md` diz explicitamente "Mover + compactar (SEMPRE)", gera a cópia leve sidecar em `resumos-gerados/leves/` e, em remote-control, envia a leve pelo chat. Corrida piloto histo-11: master 60,8 MB → leve 1,76 MB (34,6×), micrografias legíveis.
- **Resumo histo-11-orgaos-linfaticos gerado (Histologia, Tecido/Órgãos Linfoides, Profa. Marilene).** 31 pp, blueprint ALTO confirmado. Mapa de Confusões (estava vazio) preenchido. Curadoria AnKing rodada em MODO AVALIAÇÃO (não aplicada ao deck, a pedido): cobertura 15/24 COBERTO (87% ao menos parcial). **Achado forte:** `buscar_tags_lote` subestima recall com termos EN multi-palavra (declarou 20 lacunas; real 87%) — a verdade veio de ler o texto real dos cards da subárvore-âncora. Lista completa de atritos + ideias em `arquivos-trabalho/AJUSTES-PIPELINE-2026-07-07.md` (para a sessão de tuning à tarde).
- **Sessão de tuning (triagem da chuva de ~45 ideias de Davi). Escopo travado: P0 + fundação do P1 + cortes de token seguros.** Feito: (1) **`buscar_tags_lote` matching consertado** — substring-regex → whole-word AND-de-frase com normalização das duas pontas (tag e termo). Conserta a lacuna falsa do "20/24" (multiword c/ espaço nunca casava tag c/ `_`) E o ruído de palavra curta; descarta placeholder `<EN?>`. (2) **`gerar_checklist` ancorado nos subtópicos do Tema Card** — antes só semeava `#termo-nota`/`#sigla` (perdia órgão/zona/etapa ensinada em prosa); agora lê os subtopicos do YAML como esqueleto oficial (numerados por posição, pois o dado real é frase pura sem "1.1"), unidade de cobertura = subtópico (mesmo eixo da regra "≥2 questões E2/subtópico"). Smoke-test histo-10: 10 subtópicos + 18 termo-notas. (3) **"Onde aprofundar" REMOVIDO da capa** — `gerar_main.render_capa` filtra rótulo "aprofund"; CLAUDE.md capa atualizado + bloco marcado SUSPENSO; memory pessoal idem. (4) **Bandeiras redefinidas** ([[bandeira-vermelha-21h]]): vermelha(flag:1)=me explique (NEBLI, 2 parágrafos); laranja(flag:2)=audite pertinência; **email SÓ sob demanda** (tasks `NEBLI-monitor-diario/-semanal` a desabilitar — requer PowerShell elevado, ação do Davi). (5) **RemNote aposentado** — seção Etapa 4 do CLAUDE.md colapsada (-2,8k chars do doc always-loaded). (6) **ERROS #20** — termo-nota com termo repetido na prosa ("fibra reticular² fibra reticular"); #19 reforçado (título verboso). (7) **`__pycache__` limpo.** Elefante de disco identificado: `.git`=2,8G (auto-commit versiona binários) → pendência com OK de Davi, não cortado. Chuva completa triada em § Pendências → "Chuva de ideias 2026-07-07".

### 2026-07-04
- **Roda de bandeira vermelha 21h + perfil decoreba + sprint P4 (pedidos de Davi: "montar decks pra toda aula", "cards decoreba curados com carinho", "bandeira vermelha explicada e removida às 21h").** (1) **Modo `--bandeira`** em `monitor_email_anking.py`: às 21h coleta `tag:NEBLI::* -tag:NEBLI::zerado::* flag:1`, explica em voz NEBLI (`claude -p`), entrega email **+ HTML local** (`arquivos-trabalho/bandeira-<data>.html`, sempre gravado), e **tira a bandeira** (reset). Descoberta técnica: AnkiConnect do Davi **não tem `setFlag`**; un-flag via `setSpecificValueOfCard(keys=["flags"], newValues=[0])` com **inteiro** (string faz no-op silencioso); `cardsInfo` não expõe flags. Fallback = tag `NEBLI::explicado::<data>`. Task Scheduler 21:00 (antes do diário 21:05). Testado ponta a ponta. Memória [[bandeira-vermelha-21h]]. (2) **Perfil decoreba** (CURADORIA-ANKING.md): metabolismo/anatomia pedem completude dos fatos úteis DENTRO do escopo (enzima-chave, passo limitante, cofatores, regulação, saldo, gancho) + mecanismo suficiente por card — precisão-na-vizinhança e completude-no-escopo não se contradizem. Ordem pedagógica no manifesto; ordem nativa AnKing no deck (sem reposicionar). (3) **Fonte-verdade = E1, não tema_card** (correção de Davi: "o card vem da E1"). (4) **Sprint P4 primeiro** (exame 13/jul, antes da P3 16/jul): curar as 6 aulas bioq/biomol da E1, ~40-50 novos/dia até as provas, meta 150 revisões/dia; P3 e resto = fase 2. Plano: `plans/pensa-como-buscar-cards-resilient-alpaca.md`. Wiring: `monitor_email_anking.py`, `CURADORIA-ANKING.md` (E1 + § Perfil decoreba), `INFRA-REMOTO.md` (tarefa 21h), `_INDEX.md`.
- **Curadoria AnKing invertida: fluxo dirigido por conceito + prova de cobertura X/Y (pergunta de Davi: "como buscar cards que cubram especificamente o conteúdo da aula, dessuspender só esses, e que cubram tudo de forma satisfatória").** O fluxo era tag-first / cobertura-last (chutar keyword → ler cards → gap-analysis no fim), que vazava recall (conceito sem keyword digitada nunca tinha tag buscada — ANATO-06 quase perdeu anatomia venosa/ázigo) e deixava cobertura sem métrica (coluna "Cobertura AnKing" do `_INDEX.md` vazia). **Inversão:** passo 1 vira **checklist-alvo a partir da E1 redigida** (`typst-build/etapa1.typ` + Seção B do Tema Card, fonte-verdade escolhida por Davi), gravada em `arquivos-trabalho/checklist-<slug>.tsv` (`id\tfrase\ttermos pt/en`); a Camada 1 passa a ser dirigida pela checklist via **`buscar_tags_lote.py` (novo)** — busca a união dos termos de uma vez, liga cada tag ao(s) conceito(s) que a motivou, e lista conceito-sem-tag como LACUNA declarada (não silêncio); o gap-analysis vira **matriz conceito×card** com coluna "Conceito-alvo" obrigatória (card kept sem id = drop). **Cobertura vira número:** `verificar_cobertura_anking.py` (novo) lê o manifesto e reporta **X/Y COBERTOS**, exige checklist inteira avaliada + toda LACUNA/PARCIAL com fonte (erro trava fechamento), devolve a linha pro `_INDEX.md` — análogo do relatório de ratio Q01-Q30. **Match segue leitura Opus na sessão** (sem embedding, evita bug F9); os scripts só alimentam o pool (recall) e provam cobertura (métrica); `extrair_cards`/`aplicar_curadoria`/schema `curado.json`/casamento por `raw0` **inalterados**, precisão do gate de keep preservada. Piloto ANATO-06 validado: `buscar_tags_lote` reachou `SketchyAnatomy::…Superior_Vena_Cava` (conceito 2.3, o quase-perdido); `verificar_cobertura` = **5/8 COBERTOS** (3 parciais com fonte). Wiring: `CURADORIA-ANKING.md` (§ fluxo dirigido por conceito + 6 passos reordenados + § Reuso), `_TEMPLATE.md` (seção Checklist-alvo + Camada 1 sem PURA + Conceito-alvo obrigatória + Cobertura X/Y), `.claude/commands/resumo.md` passo 11, `_INDEX.md` (linha ANATO-06). Constrói sobre o critério rígido de keep (entrada abaixo).
- **Critério de inclusão RÍGIDO na curadoria AnKing (pedido de Davi: "quero que entrem no deck somente cards da aula que tive... menos cards, mais conceitos exatos da aula é ideal").** Objetivo declarado e gravado na memória: usar o Anki para **reter a longo prazo o que já estudou, sem ciclo de aprender/reaprender** — o deck é memória do que passou pela aula, não acúmulo de vizinhança. Duas mudanças no método (`flashcards/CURADORIA-ANKING.md`): (1) **atalho de tag PURA ABOLIDO** — era a porta por onde entrava card não-idealmente-da-aula; agora toda tag candidata passa por keep/drop card-a-card. (2) **Gate de keep:** card entra só se o conceito que testa aparece na **Seção B (esqueleto de conteúdo) do Tema Card** da aula; vizinhança anatômica/fisiológica (topografia de relação, condução, etiologia, complicação, detalhe métrico) NÃO basta. Precisão > recall; na dúvida, fora (gap vira fonte externa). **Contar por note** (cloze multi-`{{cN}}` vira vários cards). **Piloto ANATO-06 recurado 37→31 kept** (cortados: parte posterior do coração=AE, VD superfície anterior, irrigação nós SA/AV, bifurcação carotídea C4, quilotórax por lesão do ducto, síndrome VCS por câncer de pulmão); aplicado no deck (podados os 6 do apply anterior: tag removida + re-suspensos; re-aplicados → 30 notes/42 cards ativos; 1 card do Coronary não casou por divergência export×coleção). Memória nova `anki-retencao-longo-prazo.md`. Wiring: `CURADORIA-ANKING.md` (§ Camada 1 sem PURA + § Critério de inclusão) + `flashcards/curadoria/anato-06-…-curado.json` + `_INDEX.md`.

### 2026-07-03
- **Execução: piloto ANATO-06 aplicado + deck zerado + monitor/infra construídos.** Curadoria card-a-card da ANATO-06: 103 candidatos → **37 kept** (36 casaram na coleção → 49 cards), toda patologia/fisiologia de Step 1 descartada; gaps (fetal, Willis, aorta torácica, veias/safenas, porta, ázigo) marcados com fonte (Netter/Moore+slide) em `flashcards/curadoria/anato-06-…md`. **Deck zerado** (`zerar_deck_anking.py`, novo): 336 cards ativos do lote1 re-suspensos e marcados `NEBLI::zerado::2026-07-03` (reversível via `--reverter --data`); único bloco ativo agora = ANATO-06. **Descoberta técnica importante:** o AnkiConnect do Davi **não expõe `guid` no `notesInfo`** (só noteId/fields/tags) — o casamento card-a-card passou a ser por **texto bruto do campo 1** (`raw0` no pool + `_norm` no apply; fallback pra guid se versão futura expuser). **Monitor reduzido a 2** (pedido de Davi): `monitor_email_anking.py` modos `--diario` (cards Again de hoje) e `--semanal` (leeches/lapses≥3), voz NEBLI via API Claude (`claude-sonnet-4-6`) + Gmail SMTP para dpbdes@gmail.com. **Infra remota** desenhada em `referencias-externas/INFRA-REMOTO.md`: Anki headless em Docker (sempre-on, sync AnkiWeb), `claude remote-control` (celular dirige o PC; nuvem não alcança localhost — confirmado), Task Scheduler pros 2 emails. Emails/tarefas dormentes até Davi criar `GMAIL_APP_PASSWORD`+`ANTHROPIC_API_KEY`.
- **Sistema de curadoria AnKing v12 por aula (pedido de Davi: "toda aula ter cards MUITO bem curados... um sistema pra escolher o card certo e deixar o errado").** Máquina de 2 camadas: tag grossa (`buscar_tags_anking.py`) classifica leaf-tags em PURA/IMPURA/RUÍDO; card fino (`extrair_cards_anking.py`, novo — dá o texto real de cada card, limpa HTML/cloze) permite keep/drop nas IMPURAS. Alvo 30–50 cards/aula. Gap-analysis proativo: conceito não coberto pelo AnKing → sinalizar e **apontar a fonte** (Netter/deck dedicado/slide), nunca forçar card ruim (decisão de Davi: "usa separado e sempre indica o que falta e onde pegar"). Aplicação via AnkiConnect (`aplicar_curadoria_anking.py`, novo): marca `NEBLI::<slug>` nos notes curados, dessuspende, atualiza o painel sozinho. Estado em nova pasta `flashcards/curadoria/` (`_INDEX.md` = razão-mestra + aviso vivo de dessuspendidos; `_TEMPLATE.md`; `<slug>.md` + `<slug>-curado.json` por aula). Lote1 (336 cards bioq) migrado como entradas legado tag-level. **Hook no pipeline:** `/resumo` passo 11 auto-aplica a curadoria no fim (pedido: "ao pedir o pipeline completo vc adiciona os cards ao meu deck"). **Monitor:** `revisao_diaria_anking.py` (novo) puxa cards errados hoje (Again) nos blocos NEBLI:: com texto real → base do email diário de explicação de erros (pedido: "me mandando email com explicação dos cards que errei"). Escopo desta rodada: só a máquina + estado, nenhuma aula dessuspendida ainda (Davi escolheu "só o sistema/método primeiro"; revisa antes do 1º piloto, provável ANATO-06). Método completo: `flashcards/CURADORIA-ANKING.md`. Wiring: `CLAUDE.md` § References + `.claude/commands/resumo.md` passo 11.
- **Conclusão integradora VOLTA a ser canônica/obrigatória (pedido de Davi: "volta a conclusão integradora pro canônico").** Reverte as decisões de 2026-06-24 (tornou opcional) e 2026-07-01 (removeu o gate). Toda E1 fecha no `#conclusao-box` em 4 camadas (princípio unificador → mecanismo nuclear → clínica retomada → projeção), antes do `#resumindo-page`. Volta a ser gate hard do `precompile-check.py` (`>=1 #conclusao-box` em `etapa1.typ`). Não é redundante com o Resumindo: a conclusão argumenta em prosa, o Resumindo enumera cápsulas. Wiring: `CLAUDE.md` Ordem do PDF item 3 + § Mapas mentais suspensos; `ROLES.md` § Redator diretriz 11 + linha do escopo do Redator-E1; `precompile-check.py` EXPECTATIONS["etapa1.typ"].
- **Cópia leve automática no fim do pipeline (pedido de Davi: "adiciona essa compressão sempre no final do pipeline, pra upar pro drive mais fácil").** Novo passo 9 do COMPILADOR: após mover o master full-res, `comprimir_pdf.py` gera uma cópia comprimida em `resumos-gerados/leves/[SLUG].pdf`. Política **sidecar** (Davi escolheu "manter os dois"): master em `resumos-gerados/` continua full-res (figura = mecanismo); a leve é sidecar Drive-ready. Compressão via PyMuPDF `rewrite_images` (dpi_target=225, q85) — os slides saem do `extrair_slides.py` a ~3000 px (~600 DPI na página), reamostrar pra ~290 DPI corta ~10-12× o tamanho sem perda visível (ANATO-06: 30,4→2,44 MB; HISTO-10: 23,8→2,09 MB). Motivo do fluxo: conectores MCP de Gmail/Drive exigem base64 inline (inviável em MB) e Gmail só cria rascunho — a cópia leve resolve o gargalo de distribuição. Backfill dos 2 PDFs existentes feito. Wiring: `ROLES.md` § Compilador passo 9 + `CLAUDE.md` Routing Map + `typst-build/comprimir_pdf.py` (novo).

### 2026-07-02
- **Resumo histo-10-tecido-nervoso gerado inteiramente em Fable** (sessão trocada para Fable 5 a pedido de Davi — "pode usar o FABLE em tudo"). Contorna o bug F9 (era Opus 4.7 + Agent tool). Ver memória `feedback-opus-para-e1-e2` atualizada.
- **Duas correções visuais no template (pedido de Davi, amostra antes/depois aprovada).** (1) **Figura flutuante:** `figura-nebli` virou `figure(placement: auto)` — antes era bloco inline `breakable:false` que, sem caber no rodapé, era empurrado inteiro para a próxima página deixando buraco branco. Como float, o texto preenche o vão e a figura vai pro topo/rodapé; imagem+legenda seguem juntas. Reduziu histo-10 de 35→34pp. Tradeoff: figuras podem agrupar no topo da página, levemente à frente do parágrafo — layout de livro-texto, aceitável; se Davi quiser figura colada ao parágrafo exato, reverter para inline. (2) **Tags da capa "Onde aprofundar":** os caminhos AnKing longos (`#FirstAid::…::01_Cells_of_the_nervous_system`) transbordavam a margem direita. `gerar_main.py` agora insere zero-width-space (U+200B) após cada `::` e `_` (`_quebrar_tags_longas`) + fonte do bloco 8pt→7.3pt, deixando o Typst quebrar nos limites naturais da tag sem mudar o texto visível. Backups em `backups/tecnicos/*-20260702-*`.

### 2026-07-01
- **Conclusão integradora deixa de ser gate (pedido de Davi).** `#conclusao-box` era exigido `>=1` pelo `precompile-check.py`, mas a regra canônica desde 2026-06-24 já dizia opcional. Removida a exigência do gate — conclusão entra **só quando o tema pede** (forte integração). Wiring: `CLAUDE.md` Ordem do PDF item 3 + `precompile-check.py` EXPECTATIONS["etapa1.typ"]. **⟶ REVERTIDO em 2026-07-03: conclusão voltou a ser obrigatória e gate. Ver entrada de 2026-07-03.**
- **C/E sempre 4 itens (I-IV) — gate hard (pedido de Davi).** Toda `#questao-ce` passa a exigir exatamente 4 assertivas. Novo check `check_ce_quatro_itens` no `precompile-check.py`. Wiring: `CLAUDE.md` Formatos de item + `ROLES.md` § Formatos de item. Aplicado retroativo ao histo-09 (6 questões C/E de 3 itens ganharam 4º item; gabarito do Tema Card atualizado).
- **Cobertura da E1 na E2: todo subtópico testado ≥2x (pedido de Davi).** Diretriz auditável (não gate por regex — mapeamento é semântico): tabela subtópico→questões no relatório de fechamento. Truque: 4º item de C/E reforça o subtópico mais fraco. Wiring: `CLAUDE.md` + `ROLES.md` § Formatos de item.
- **"Onde aprofundar" ordenado por completude no tema (pedido de Davi).** Decks do grupo 2 do bloco da capa vêm rotulados *Cobre melhor* → *Complementa* → *Mais distante*, do que aborda o tema mais completamente (dessuspender primeiro) ao tangencial. **Objetivo canônico:** guiar Davi a ter cards dessuspendidos que cubram o tema de cada aula. Wiring: `CLAUDE.md` Ordem do PDF (bloco Onde aprofundar) + `referencias-externas/onde-aprofundar.md` + memória `onde-aprofundar-anking-capa.md`.

### 2026-06-30
- **Bloco "Onde aprofundar" na capa (`referencias-externas/onde-aprofundar.md`).** Recurso pedido por Davi (usuário de AnKing v12): toda apostila mostra na capa onde aprofundar o tema nas plataformas Step 1, **sem fricção pra saber qual deck dessuspender**. Estrutura em 2 grupos: (1) **Assistir/ler** (B&B/Bootcamp, NinjaNerd, Sketchy, UWorld, Pathoma; "não cobre" quando aplicável); (2) **Dessuspender no AnKing v12** com 1 bullet por deck = **caminho de tag pro Browse** + contagem de cards + **variedade de decks** (o conteúdo é taggeado em paralelo por vários recursos). Fonte-verdade = export real das tags do v12 de Davi (`anking-v12-export.txt`, 28k cards Step 1, coluna 22, prefixo `#AK_Step1_v12`), buscado via `flashcards/scripts/buscar_tags_anking.py <termo>`. **Irmão INVERSO do blueprint:** este VAI pro PDF (exceção escopada à regra de banimento Step 1 — nomes de plataforma/deck só nesse bloco da capa). Infra: `gerar_main.py` aceita `meta` com valor em lista → bullets navy (`_esc_typst_content` escapa `#`/`_`, preserva `*`). Wiring: `CLAUDE.md` Ordem do PDF (capa) + § References; `ROLES.md` Seção A; `TEMPLATE_API.md` capa. Amostra aprovada visualmente no glicogênio (640 cards em 9 decks). Aplicar nos próximos resumos.
- **Calibração externa invisível por aula (`referencias-externas/blueprint-step1.md`).** Nova régua que espelha o papel do `banco_slim.json`: tabela slug→(rendimento ALTO/MÉDIO/BAIXO, aprofundar 1-2 frases na E1, ângulo E2/E3, gancho clínico de residência BR), cobrindo as 71 aulas (41 UC01 + 30 UC02). Fonte = blueprint USMLE Step 1 (único alinhado a ciências básicas; sem provas literais — NBME não libera) + padrões de banca de residência BR (HC-FMUSP/Einstein/UNICAMP) como biblioteca de ganchos clínicos. **Consultada na redação, nunca colada no PDF** — vocabulário "USMLE/Step 1/residência" continua banido. Wiring: ponteiro em `CLAUDE.md` § References + Redator diretriz 16 + Questionador § "Segunda régua". Convite, não gate (F7). Coluna BAIXO = "não force clínica aqui". Decisão de Davi: aprofundamento sucinto na prosa + acionado nos exercícios + .md de referência. Descartado: baixar 10 anos de provas (USMLE não existe; residência BR fragmentada/paywall e majoritariamente clínica, descasa do 1º ano).

### 2026-06-24
- **Operação "pequenos ajustes" (Sugestões (3).pdf, 45 itens).** Plano consolidado em `pequenos_ajustes/PLANO_pequenos_ajustes.md`; pesquisa focada Mankiw+Poliedro em `arquivos-trabalho/pesquisa-didatica/ACHADOS-topico-tabela.md`. Buckets 1-4 executados; 5 (imagens), 6 (2 colunas/legibilidade) e 7 (flashcards/token-split/mapa-confusões) pendentes por decisão de Davi.
- **Gabarito horizontal (item 14).** Template `gabarito-bloco` voltou a leitura row-major nativa (5 colunas, "Q1 Q2 Q3 Q4 Q5 / Q6…"), removendo o reorder column-major de 2026-05-26 — que era também fonte do bug de letra desalinhada (item 8). Backup em `backups/tecnicos/`. Validado visualmente.
- **Gabarito sorteado de verdade + guarda anti-degeneração (itens 5/9/17).** ROLES § "Gabarito sorteado de verdade" reescrita: sortear o sinal, nenhuma letra >~40%, sem corrida 4+, C/E sem bloco longo nem CECECE. Guarda **reposiciona a correta**, nunca muda a correta. Limiares do `precompile-check.py` endurecidos (corrida ≥5 erro / ≥4 warn; dominância ≥50% erro / ≥40% warn).
- **Revisor-gabarito (Haiku) NOVO (item 8).** Stub `.claude/agents/revisor-gabarito.md` + ROLES § Revisor-gabarito + Routing Map. Passada final: impresso==real (bloqueia), sem corrida, distribuição sã.
- **C/E reintroduzido em ~1/3 + "assinale a incorreta" (itens 6/9/10).** ROLES § Formatos de item. Paridade não se aplica a C/E.
- **Questões de cálculo + cálculo bem explicado (itens 1/18).** ROLES § Escrita matemática: etapas rotuladas (modelo Mankiw). ANTI-EXEMPLARES A1.
- **ANTI-EXEMPLARES.md criado** (par negativo do EXEMPLARES). Semeado com A1/A2/A3/A4; A1-A3 com placeholders aguardando Davi colar os trechos reais (itens 1/27/28).
- **EXEMPLARES Categoria 18 "Quando quebrar a prosa".** 4 gatilhos (catálogo de tipos, cadeia de premissas, tabela de cruzamento, Resumindo frase-completa) + cálculo em etapas. Itens 21/33/34/36/40/42/43.
- **Conclusão integradora OPCIONAL (item 29).** Default = E1 termina na última PARTE. ROLES diretriz 11 + CLAUDE Ordem do PDF. **⟶ REVERTIDO em 2026-07-03: voltou a ser obrigatória. Ver entrada de 2026-07-03.**
- **Resumindo mais enxuto (item 36):** 6-10 seções, ~30-45 palavras de frase encadeada. **Nome de subtópico direto, não-poético (item 35).** ROLES § Redator.
- **Elogio registrado (item 39):** Davi gosta da fluidez da prosa atual — preservar; mudanças desta operação são no aparato de decisão, não na prosa.

Forma compacta absorvida do `CHANGELOG_CLAUDE.md` original (619 linhas) em 2026-05-29. **Auditoria histórica detalhada anterior a 2026-05-22 fica no backup** (`backups/pre-faxina-2026-05-29/raiz/CHANGELOG_CLAUDE.md`).

### 2026-05-29
- **Faxina extrema do processo.** 8 arquivos vivos + 14 feedbacks + 9 agents → 4 arquivos vivos + 9 agent-stubs. Criados ERROS.md (consolida errosComuns + 9 feedbacks únicos) e ROLES.md (funde 9 agents). MEMORY.md absorve pendências + changelog compactado + § Diário de revisões. CLAUDE.md monolítico preservado com 3 atualizações pontuais.
- **Diário de revisões com peso dinâmico.** Nova § em MEMORY.md. Feedback de Davi sobre resumos individuais vira lista de prioridades temporárias na corrida seguinte, com decaimento automático após 5 resumos sem reincidência.
- **Pergunta âncora / pergunta retórica / pergunta ingênua BANIDAS como recurso editorial.** Substitui o antigo "teto de 3 perguntas ingênuas" (2026-05-28). Abertura de subtópico = afirmação direta + mecanismo.
- **EXEMPLARES.md ganha papel DUPLO.** Referência de gesto pedagógico E de prosa modelo (voz textual). Em conflito de voz entre regra abstrata e exemplar, exemplar vence também no texto literal.
- **Paridade de distratoras estendida de Q26-Q30 para Q01-Q30.** Tell visual opera idêntico em qualquer categoria. Relatório das 30 no chat obrigatório antes de fechar E2.
- **Banda dupla 0.80-1.25 para paridade.** Substituiu o gate teto-único de 1.25 (que gerava distratoras infladas + correta enxuta como overfit). Banda simétrica.
- **Rodada de poda canônica.** "Diálogo" → "prosa expositiva de monitor" no CLAUDE.md + agents. Encolhimento do redator-e1.md de 266 → 213 linhas.

### 2026-05-28
- **Filtro de admissão para Integração na E2.** Antes de redigir cada Q11-Q25, gravar `arquivos-trabalho/integracao-mapa-<slug>.md` no formato `Qxx conecta [A] + [B]`. Sem dois domínios distintos, volta para Consolidação. Gate operacional único — tipos de cruzamento entram como sugestão.
- **Densificação do template** (margens 2.0→1.7cm verticais; `spacing` 1.5→1.2em; v() reduzidos). Resultado em Krebs: -3 páginas (-8,8%) sem cortar conteúdo.
- **`#mindmap-fechamento` SUSPENSO.** E1 termina na Conclusão integradora; `#resumindo-page(...)` vem direto. Helper vira no-op no template.
- **Figuras: largura variável 40-80%** com análise caso a caso (default 65% aposentado). Relatório auditável obrigatório no fechamento (tabela Figura | PARTE | Origem | Mecanismo | Largura).
- **EXEMPLARES como implementação canônica das diretrizes.** Regras = princípios; EXEMPLARES = a regra acontecendo em prosa real. "Exemplar vence regra abstrata" deixa de ser exceção.
- **Tema Card ganha Seção E (exemplares-âncora).** Higiene de voz por PARTE no redator.
- **Refatoração REDATOR-E1 (M1-M5).** Contexto MAIOR > economia de tokens. Lazy-load de EXEMPLARES recusado por Davi.
- **Remoção canônica de "figura ancorada na prosa".** Davi: "isso de ancora quero que vc tire".
- **Anti-engessamento meta-coerente.** Regras sobre voz/fluidez não em tom prescritivo duro. Convite > obrigação. Default > gate.

### 2026-05-27
- **Etapa 4 reativada como Flashcards clínicos RemNote.** E5 NEBLIcards sai do standby. `.md` colável no RemNote (sintaxe nativa `>>` Q→A, `{{}}` cloze). 6+2 fixos. Direção clínico→molecular.

### 2026-05-26
- **Subagentes REDATOR-E1 e QUESTIONADOR aposentados.** Sessão principal Opus acumula os 3 papéis no mesmo thread.
- **Cota de `#atencao-box`: máx 1-2 por PARTE.** Confusões educativas viram parágrafos dialogados.
- **Capa sem "Nota de uso".** Bloco meta = Disciplina + Onde estudar.
- **Pipeline para de pedir confirmação preventiva.** Inferir e seguir; Davi corrige depois.
- **Voz vira "apostila explicativa", não conversa simulada.**
- **Slash command `/auditar <slug>`** criado como mitigação do hook visual bloqueado.
- **Gabarito column-major** no template (fix do bug de letra errada UC01-BC-07 43%).
- **Markers de gabarito expandidos:** A-Z, a-z, romanos, dígitos 1..99.

### 2026-05-25
- **Missão canônica:** "Apostila de extrema qualidade, do básico ao aprofundado". Aluno presumido com dificuldade real. Ensinar bem > concisão.
- **Teto E1 ampliado para 22 páginas** (era 20). Comprimir essencial trai a missão.
- **Limpa-geral da raiz.** plataforma/, Inspiração de FORMA/, template 2.0/, AIbundle.js → `lixo/limpeza-2026-05-25/`.
- **Pipeline de cadernos automatizado.** `pipeline_caderno.py` + agente CADERNISTA. Numeração sequencial 1..N (IDs do banco têm colisões em UC1).
- **Fix de ancoragem de tema nos subagentes.** Bloco ANCORAGEM no system prompt + limpeza preventiva de `typst-build/`. (Não segurou — ver 2026-05-26.)
- **Rubrica de qualidade em 3 tiers.** Tier 1 mecânico/visual (Ollama), Tier 2 didática (Sonnet), Tier 3 revisão profunda (Opus).

### 2026-05-24
- **Apêndice de explicações removido do caderno.**
- **Numeração sequencial 1..N dentro do PDF de caderno.**

### 2026-05-22
- **Etapa 4 removida do pipeline canônico.** PDF termina em E3 + Gabarito.
- **Banco como calibração + artefato avulso sob demanda.** Não entra mais no PDF.
- **Seção D do Tema Card** (Pontos de quebra). `banco/extrair_armadilhas.py` alimenta.
- **`aulas_uc02.yml` criado** (31 aulas). `classifier.py` rodado: cobertura 44% → 94.7%.
- **`validar_tema_card.py` + `auditar_pdf_visual.py`** novos validadores.
- **Mindmap de fechamento canonizado** como `#mindmap-fechamento` (Typst nativo). *Suspenso em 2026-05-28.*
- **Banda 1.25 para paridade nasceu** (depois virou banda dupla 0.80-1.25 em 2026-05-29).
- **Escrita matemática canônica.** Display math para razões conceituais; inline para triviais.

### 2026-05-20
- **Sonnet para COMPILADOR** (canônico). Opus para REDATOR-E1, QUESTIONADOR, ORQUESTRADOR.
- **Estrutura `.claude/agents/` criada** (4 arquivos formato Claude Code).
- **Plano consolidado de tokens v3** em execução.

### 2026-05-19
- **Pacote visual v3:** Merriweather corpo + Montserrat títulos. Negrito preto, sem indentação de primeira linha.
- **Mapas mentais SVG suspensos** (helper `#mapa-parte` proibido).

### 2026-05-18
- **Redesenho da E2 em 4 peças:** Mapa de Confusões, paridade intra-questão, sorteio do sinal, ordem invertida de redação.
- **Caixa alta para ênfase proibida** (exceções: siglas, numeração estrutural).

### Antes de 2026-05-18
Auditoria detalhada em `backups/pre-faxina-2026-05-29/raiz/CHANGELOG_CLAUDE.md` (619 linhas). Marcos relevantes: criação do template `nebli_v2_apostila.typ`, definição do pipeline canônico Typst, criação do banco de questões com YAML rico, primeiras gerações da G20.

---

## § Core Memory

### Identidade do autor

- **Davi Sousa** — aluno FMUSP turma 114, 1º ano (2026). **2º semestre ativo (desde ago/2026): Ciclo da Vida I (UC-16) + Digestório (UC-8), Turma B.** (1º sem foi UC01/UC02.)
- **Contato (rodapé da capa):** "Davi Sousa — Turma 114" / "(61) 98264-7208 · dpbdes@gmail.com · PIX: dpbdes@gmail.com".
- **Conhecimento inicial:** ensino médio + meses de medicina, **com dificuldade real** no tema. Mecanismo antes de nome; jargão como etiqueta para conceito já entendido; pré-requisitos sempre retomados em 1-2 frases.

### Missão NEBLI (canônica 2026-05-25)

**Apostila de extrema qualidade, do básico ao aprofundado**, para aluno que sabe pouco aprender muito. Ensinar bem > concisão. Teto E1 = 22 páginas. Comprimir essencial trai a missão.

### Identidade visual ativa (pacote v2, canônico 2026-05-19)

Template ativo: `typst-template/nebli_v2_apostila.typ` (monolítico, ~42 KB). Pacote visual v2 com Merriweather (corpo) + Montserrat (títulos). Apostila brasileira A4 fundo creme, navy escuro como cor estrutural, gold como spark.

- **Tipografia:** corpo Merriweather, títulos Montserrat. Negrito em preto, sem indentação de primeira linha de parágrafo.
- **Callouts canônicos:** `clinica-box`, `atencao-box`, `confusao-prevista` com fundo colorido e cantos arredondados (gramática clássica do v2).
- **Capa:** faixa navy + título + subtítulo (opcional, em geral vazio ou disciplina seca) + bloco meta (Disciplina · Onde estudar) + rodapé identificador (Davi + contato). Sem bloco/prova/turma/semestre/slug em nenhuma página.
- **Resumindo:** banner gold + 2 colunas, 8–12 seções de ~25–35 palavras.
- **Categorias E2:** 3 cores (consolidação verde, integração azul, aplicação roxa) no badge da questão e no cabeçalho da Etapa 2.
- **Mapas mentais suspensos.** Helpers `#mapa-parte` e `#mindmap-fechamento` são no-op silencioso no template.
- **Backups do template:** `backups/tecnicos/nebli_v2_apostila.bak_pre-fix-resumindo.20260520_154028.typ`, `nebli_v2_apostila_pre-colbreak-fix_2026-05-20.typ`, `nebli_v2_apostila.typ.bak-2026-05-28-Ax-densidade`. **Tentativa de migração v3 (fundo branco / Nunito / accent azul-céu) revertida em 2026-05-30** — v3 arquivado em `backups/tecnicos/v3-revertida-2026-05-30/`.

### Restrições visuais ativas

- **Mapas mentais suspensos** (2026-05-19, ampliado 2026-05-28). Helpers `#mapa-parte` (SVG) e `#mindmap-fechamento` proibidos. No-op silencioso no template.
- **Caixa alta para ênfase proibida** (2026-05-18). Exceções: siglas, numeração estrutural, acrônimos clínicos.
- **Capa e PDF:** proibido bloco/prova (P1/P2/P3), número/posição de aula, slug, turma/semestre. Identificação Davi só no rodapé da capa.
- **Pergunta âncora / pergunta retórica / pergunta ingênua BANIDAS como recurso editorial** (2026-05-29). Abertura de subtópico = afirmação direta + mecanismo.

### Pipeline canônico (em vigor)

- **PDF termina em E3 + Gabarito** (2026-05-22). E4 removida; banco vira calibração.
- **Seção D do Tema Card** (Pontos de quebra). ORQUESTRADOR roda `banco/extrair_armadilhas.py <slug>`. Vocabulário de prova banido em qualquer lugar da E1 com check no `precompile-check.py` (erro, não warning).
- **Comando de compilação canônico:** `cd typst-build && typst compile --root .. --font-path ../fonts [tema].typ [tema].pdf`.
- **Pipeline paralelo (`_par_<slug>/`):** `gerar_main.py` grava em `typst-build/` raiz por bug — workaround em `ROLES.md` § Compilador.

### Delegação a subagentes

- **Model IDs canônicos:** `claude-opus-4-7` para Opus, `claude-sonnet-4-6` para Sonnet. Aliases (`sonnet`, `claude-opus-4`) quebram o spawn.
- **COMPILADOR local, NUNCA delegado.**
- **REDATOR-E1 e QUESTIONADOR aposentados como Task subagent** desde 2026-05-26 — sessão principal acumula. Stubs em `.claude/agents/` mantêm dispatchabilidade caso volte.

### Banco de questões

- **413+ questões** em `banco/questoes/q-XXXX.md` com frontmatter YAML.
- **Papel atual:** calibração + artefato avulso. Não entra mais no PDF.
- **Slim canônico:** `banco/indice/banco_slim.json` (~36k tokens) — calibração de nível/jargão/armadilha por aula.
- **Aulas:** `banco/aulas_uc01.yml` (41 aulas), `banco/aulas_uc02.yml` (31 aulas, 2026-05-22).
- **Classificador:** `banco/classifier.py` — keyword + sinônimos curados, propõe top-3 candidatas com score, exige revisão humana antes de gravar `aula:`.

### Backup, histórico e arquivamento

- **`backups/`** centraliza tudo: `pre-faxina-2026-05-29/` (snapshot completo), `planos-historicos/`, `tecnicos/`, `operacoes-fechadas/`.
- **`MEMORY.md` (este arquivo)** absorveu `pendências de melhora.md` e versão compacta do `CHANGELOG_CLAUDE.md`. Versão completa do changelog (619 linhas) preservada em `backups/pre-faxina-2026-05-29/raiz/`.
- **ARCHIVE.md deletado** em 2026-05-29 (esqueleto vazio, nunca acionado).
- **FILOSOFIA.md deletado** em 2026-05-29 (congelado desde 2026-05-04, conteúdo já migrado).
