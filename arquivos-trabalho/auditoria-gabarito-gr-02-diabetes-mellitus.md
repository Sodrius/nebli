# Auditoria de gabarito — gr-02-diabetes-mellitus (v2)

**Data:** 2026-09-03 · **Executor:** passada manual da sessão principal.
**Por que manual:** o subagente `revisor-gabarito` recusa o spawn nesta sessão. O frontmatter `tools:` dos stubs em `.claude/agents/` estava em lista minúscula (`- read`, `- bash`), que o harness não reconhece; foi corrigido para `tools: Read, Bash` nos 9 stubs afetados, mas o registro de agentes é carregado no início da sessão — a correção só passa a valer na próxima. `ERROS.md` #23 prevê o caso: sem o revisor, a passada item a item é obrigatória à mão.

**O que mudou da v1 para a v2:** regeração sob o `CLAUDE.md` § Registro científico. Q01–Q08 foram reescritas como **decoreba** (alternativas de 10–20 palavras); Q11 e Q24 foram re-ancoradas porque cruzavam dois subtópicos que a fusão de 12 → 10 transformou em um só; Q12 virou "assinale a incorreta" para restaurar a parcimônia de 2 itens desse formato. Q09, Q10, Q13–Q23, Q25–Q30 permanecem da v1.

## 1. Impresso == correta real

### Certo/Errado (10 questões, 40 assertivas) — 40/40 conferem

| Q | Sequência | Assertiva falsa e por quê |
|---|---|---|
| 02 | ECCE | I — a glicação é espontânea, sem enzima. IV — a frutosamina lê janela *menor* (2–3 semanas contra 8–12). |
| 05 | CCCE | IV — o escore de cálcio mede carga de placa, não estenose. |
| 07 | CCEE | III — a radiografia atrasa 1–2 semanas. IV — o edema medular é *baixo* sinal em T1; alto sinal é em T2 com saturação de gordura. |
| 10 | CCEC | III — a respiração de Kussmaul é compensação respiratória, não doença pulmonar. |
| 13 | CECC | II — o sorbitol não atravessa a membrana; acumula e puxa água. |
| 16 | ECCC | I — a perda de dor não protege; ela permite o trauma repetir. |
| 19 | CEEC | II — a neuropatia autonômica *retém* urina. III — a hiperglicemia *piora* a função do neutrófilo. |
| 22 | EECC | I — Charcot é destruição mecânica, não infecção. II — a radiografia atrasa. |
| 25 | CEEE | II — a alça é auto-amplificada. III — predominam lesão endotelial e turbulência. IV — o evento agudo vem da ruptura com trombose. |
| 30 | EECE | I — creatinina normal é mascarada pela hiperfiltração. II — rim reduzido é o estágio *final*. IV — úlcera indolor com sondagem óssea exige investigar osteomielite. |

### Múltipla escolha (20 questões) — 20/20 conferem

**Q12 e Q18 pedem a alternativa *incorreta*** e o gabarito aponta corretamente a assertiva falsa:

- **Q12 = A** — "captação da LDL glicada por receptores de LDL clássicos, cuja expressão cai com o colesterol intracelular" é falso: a captação se dá por receptores *scavenger*, que não têm essa regulação — e é justamente isso que produz a célula espumosa.
- **Q18 = C** — "disfunção endotelial só depois da placa visível" é falso: o primeiro dano vascular é funcional, por inativação do óxido nítrico, e antecede qualquer achado de imagem.

As oito de Consolidação foram conferidas contra a E1 uma a uma: Q01 GLUT-4 (1.1) · Q03 limiar de 180 mg/dL (1.4) · Q04 secreção endógena residual (1.2) · Q06 rim reduzido, córtex afilado, hiperecogênico (3.1) · Q08 diacilglicerol e ceramida (1.3). As dez restantes de Integração e Aplicação idem.

## 2. Corrida degenerada

- **MC, em ordem numérica:** D · C · A · E · C · B · D · A · B · D · B · C · E · A · D · B · C · E · A · D. **Corrida máxima = 1** — nenhuma letra se repete sequer em questões consecutivas.
- **C/E:** ECCE, CCCE, CCEE, CCEC, CECC, ECCC, CEEC, EECC, CEEE, EECE. As dez são **distintas entre si**; nenhuma é `CCCC`, `EEEE`, `CECE` ou `ECEC`.
- **Balanço global C/E:** 22 C e 18 E em 40 itens (55%/45%) — próximo do equilíbrio sem ser 50/50 forçado.

## 3. Distribuição das MC

`{A: 4, B: 4, C: 4, D: 5, E: 3}` sobre 20 questões — letra dominante D com **25%**, bem abaixo do teto de ~40%. Correta em A em 20%, exatamente a média esperada por letra.

**Nota de procedimento:** na v1 a distribuição saiu 4/4/4/4/4, uniformidade que é sintoma de gabarito montado e não sorteado, e duas corretas foram reposicionadas entre alternativas equivalentes. Na v2 as sete questões novas ou reescritas receberam letra por sorteio, e o resultado (4/4/4/5/3) não precisou de correção.

## 4. Paridade

20/20 MC dentro da banda 0.80–1.25, média 1.05. As oito de Consolidação, agora decoreba, medem entre 10 e 15 palavras por alternativa — a banda foi verificada entre alternativas curtas, como manda o `ROLES.md` § Questionador § Consolidação.

## Veredito

**APROVADO.** Nenhuma divergência entre gabarito impresso e correta real; nenhuma corrida degenerada; distribuição sã; paridade integral.
