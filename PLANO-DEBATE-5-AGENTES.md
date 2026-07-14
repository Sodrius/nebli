# PLANO — 5 agentes adversariais que brigam pra evoluir o deck-aula

> Criado 2026-07-13. Davi: "cria 5 agentes que brigam entre si pra achar ajustes que gerem deck-aulas mais do jeito que quero. Propõem soluções criativas, discutem até uma solução inequívoca. Que critiquem MUITO pra criar MUITO." Aterrissado na pesquisa de multi-agent debate (fontes no fim).

## 0. O que a pesquisa diz (pra não repetir os erros conhecidos)

Multi-Agent Debate (MAD) melhora raciocínio, MAS falha de 3 jeitos previsíveis — o plano é desenhado contra eles:

1. **Sifofancia → convergência prematura / mode collapse** (o erro nº1). Agentes homogêneos "concordam" cedo e colapsam num consenso raso. → **Fix:** papéis adversariais distintos (mistura "troublemaker" + "peacemaker"), e o crítico é instruído a **apontar falhas**, nunca a "concordar".
2. **Persuasão vence verdade.** Um agente confiante-errado ganha no retórico. → **Fix:** juiz pontua **evidência, não retórica**; "evidence-admission" (afirmação sem exemplar/métrica é inadmissível).
3. **Nunca converge / loop infinito.** → **Fix:** detecção de estabilidade (crença estável 2 rodadas → convergiu) + teto de rodadas + escalonamento pro Davi.

Regra-mãe do projeto: **o debate é ancorado em EVIDÊNCIA NEBLI, não em opinião.** A "verdade" que eles perseguem = (a) preferências declaradas do Davi (CLAUDE.md/MEMORY.md), (b) veredito do card-mirror + exemplares AnKing reais, (c) métricas medidas (ex.: 57% Extra-com-imagem no AnKing, ratio de indução, cobertura E1). Sem âncora, MAD vira ruído persuasivo.

## 1. Os 5 agentes (papéis distintos e adversariais — heterogeneidade combate sifofancia)

| # | Agente | Instinto | Função no ringue |
|---|---|---|---|
| 1 | **PROPOSITOR (Inovador)** | troublemaker criativo | Gera MUITOS ajustes ousados ao pipeline/craft do deck-aula. Cota mínima de propostas novas por rodada. Nunca defende status quo. |
| 2 | **PURISTA AnKing** | fidelidade ao exemplar | Ataca tudo que se afasta dos cards AnKing reais. Arma: os dossiês (`ANKING-DOSSIE-*`) + card-mirror. "Isso não é como o AnKing faz — prova?" |
| 3 | **ADVOGADO DA RETENÇÃO** | objetivo do Davi | Defende aprendizado real (recall > reconhecimento, profundidade Step 1 no escopo do slide, retenção até a prova). Ataca o que parece bonito mas não ensina. |
| 4 | **CÉTICO / RED-TEAM** | epistemic vigilance | **Só destrói, nunca propõe.** Caça falhas, modos de falha, convergência falsa, custo escondido, efeito colateral. Instruído a listar FLAWS, não a opinar se concorda. É o antídoto da sifofancia. |
| 5 | **JUIZ / SINTETIZADOR** | peacemaker rigoroso | Pontua cada proposta numa rubrica contra evidência, detecta estabilidade, quebra empate, força a decisão inequívoca, e ESCREVE o veredito + a dissidência vencida. Pesa evidência, não retórica. |

Heterogeneidade extra (opcional, reduz conformidade): rodar 1-4 em modelos/temperaturas diferentes; o Juiz num modelo forte (Opus).

## 2. Protocolo de debate (estruturado, anti-colapso)

**Pacote de aтерramento (todos recebem antes):** prefs do Davi, `CARD-MIRROR-RUBRICA.md`, dossiês AnKing, `PIPELINE-CANDIDATOS.md`, métricas atuais, e a QUESTÃO da rodada (ex.: "como fazer os cards de anatomia mais AnKing?").

**Rodada (repete até convergir):**
1. **Propor:** Propositor lança N ajustes concretos (não vagos: "X vira Y no passo Z, medido por métrica M").
2. **Cruzar fogo:** Purista, Retenção e Cético criticam CADA proposta pela sua lente. Regra dura anti-sifofancia: **proibido "concordo" sem uma razão NOVA + evidência**; cada agente tem de introduzir uma crítica/evidência inédita por rodada ou fica em silêncio (não enche linguiça).
3. **Red-team:** Cético tenta quebrar as propostas sobreviventes (modo de falha, custo, gameabilidade).
4. **Julgar:** Juiz pontua cada proposta 0-5 em 4 eixos — **(a) fidelidade ao exemplar AnKing · (b) valor de retenção/didática · (c) viabilidade no pipeline · (d) alinhamento ao Davi** — só com evidência admitida. Marca a crença/ranking da rodada.
5. **Convergência:** Juiz declara "inequívoco" SÓ se as 3 baterem: **(i)** top vence o 2º por margem ≥ limiar no placar; **(ii)** o Cético não tem objeção red-team sem resposta; **(iii)** ranking estável por 2 rodadas. Senão: mais uma rodada (até teto ~5), ou escala pro Davi com o dissenso explícito.

**"Criticar muito pra criar muito":** a crítica do round vira o combustível do Propositor no próximo — cada falha apontada é um pedido de proposta nova. Métrica de saúde do debate: nº de propostas geradas e nº de falhas resolvidas por rodada (se cair a zero cedo demais = sifofancia, o Juiz força dissenso).

## 3. Implementação no harness (real e factível)

- **Sessão principal = orquestrador + Juiz** (evita over-spawn e o bug F9 de Task simulando inline). Os agentes 1-4 são **Task subagents reais**, spawnados por rodada com o estado do debate.
- **Transcrição persistida** em `arquivos-trabalho/debate/<tema>/rodada-N.md` — cada rodada é um artefato auditável (crença, propostas, críticas, placar). Nada de estado só na cabeça.
- **Round-robin, não todos-de-uma-vez:** orquestrador spawna Propositor → coleta → spawna os 3 críticos com as propostas → coleta → Juiz pontua. 1 rodada = 4-5 spawns. Teto 5 rodadas.
- **Saída final:** `arquivos-trabalho/debate/<tema>/VEREDITO.md` — o ajuste vencedor (inequívoco), rubrica de por que venceu, e a **dissidência registrada** (o que foi vencido e por quê — transparência anti-persuasão).
- **Fecha o loop com dados, não só argumento:** o ajuste vencedor é **A/B testado** num deck-amostra e passado pelo card-mirror cego (o placar do debate só vira canônico se sobrevive ao teste real). É o que separa "debate bonito" de "melhoria medida".

## 4. Como pluga no NEBLI (o objetivo)

O ringue opera sobre a **spec de geração do deck-aula** (`PIPELINE-CANDIDATOS.md`, `CARD-MIRROR-RUBRICA.md`, regras de craft). Cada debate resolve UMA pergunta de ajuste (ex.: "quando imagem no Extra?", "quanto aprofundar anatomia?", "IO por subtópico ou por aula?"). Veredito inequívoco → vira regra canônica (com entrada no `MEMORY.md` § Histórico) → aplicado no `/deck-aula`. Assim o sistema **evolui a própria régua** rumo ao "peço e sai bom".

## 5. Primeiros temas pro ringue (fila)
1. Imagem no Extra: gatilho e fonte (casável com `PLANO-IMAGENS-NA-EXPLICACAO.md`).
2. IO: uma nota rica (15 caixas) vs várias notas temáticas (5-6) — qual retém mais?
3. Profundidade Step 1 na E1 sem virar toca-de-coelho: onde é o teto?
4. Curar-real vs autorar: limiar de quando parar de curar e autorar.
5. Anti-indução: métrica automática de "dá pra adivinhar o cloze?" (semente do `lint_neblicard.py`).

## 6. Guardrails de qualidade (checklist do orquestrador)
- [ ] Papéis distintos e adversariais (não 5 clones). 
- [ ] Cético só destrói; Propositor só cria; Juiz pesa evidência.
- [ ] Proibido "concordo" sem razão+evidência nova; silêncio > enchimento.
- [ ] Toda afirmação admite exemplar/métrica (evidence-admission).
- [ ] Detecção de estabilidade + teto de rodadas + escalona pro Davi se não converge.
- [ ] Veredito registra a dissidência vencida.
- [ ] Ajuste vencedor é A/B testado + card-mirror antes de virar canônico.

## Fontes (multi-agent debate — estado da arte consultado 2026-07-13)
- Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate — https://arxiv.org/html/2509.23055v1
- Multi-LLM-Agents Debate: Performance, Efficiency, Scaling (ICLR 2025 blogpost) — https://d2jud02ci9yv69.cloudfront.net/2025-04-28-mad-159/blog/mad/
- Courtroom-Style Multi-Agent Debate (papéis explícitos + admissão de evidência) — https://arxiv.org/html/2603.28488v1
- Multi-Agent Debate for LLM Judges with Adaptive Stability Detection — https://openreview.net/forum?id=Vusd1Hw2D9
- When collaboration fails: persuasion-driven adversarial influence (Nature Sci Reports) — https://www.nature.com/articles/s41598-026-42705-7
- The Confident Liar: Diagnosing Multi-Agent Debate — https://arxiv.org/pdf/2606.10296
- Multi-Agent Debate Frameworks (overview) — https://www.emergentmind.com/topics/multi-agent-debate-mad-frameworks
