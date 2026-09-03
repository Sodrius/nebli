# Auditoria de gabarito — gr-02-diabetes-mellitus

**Data:** 2026-09-03 · **Executor:** passada manual da sessão principal.
**Por que manual:** o subagente `revisor-gabarito` recusou o spawn nesta sessão — o frontmatter `tools:` dos stubs em `.claude/agents/` estava em lista minúscula (`- read`, `- bash`), que o harness não reconhece. O frontmatter foi corrigido para `tools: Read, Bash` (e equivalentes nos 9 stubs afetados), mas o registro de agentes é carregado no início da sessão, então a correção só passa a valer na próxima. `ERROS.md` #23 prevê exatamente este caso: quando o revisor não pode rodar, a passada item a item é obrigatória à mão.

## 1. Impresso == correta real

### Certo/Errado (10 questões, 40 assertivas)

Cada assertiva foi lida e teve o seu valor de verdade decidido pelo conteúdo, contra a E1. **40/40 conferem com o gabarito impresso.**

| Q | Sequência | Assertiva falsa e por quê |
|---|---|---|
| 02 | ECCE | I — glicação é espontânea, sem enzima. IV — quem acumula AGE é a proteína de meia-vida *longa*. |
| 05 | CCEE | III — é a mesma reação química; muda a proteína. IV — hemólise *reduz* a HbA1c. |
| 07 | CCCE | IV — escore de cálcio mede carga de placa, não estenose. |
| 10 | CCEC | III — a respiração de Kussmaul é compensação respiratória, não doença pulmonar. |
| 13 | CECC | II — sorbitol não atravessa a membrana; acumula e puxa água. |
| 16 | ECCC | I — a perda de dor não protege; ela permite o trauma repetir. |
| 19 | CEEC | II — a neuropatia autonômica *retém* urina. III — a hiperglicemia *piora* a função do neutrófilo. |
| 22 | EECC | I — Charcot é destruição mecânica, não infecção. II — a radiografia atrasa 1–2 semanas. |
| 25 | CEEE | II — a alça é auto-amplificada, não autolimitada. III — predominam lesão endotelial e turbulência. IV — o evento agudo vem da ruptura com trombose. |
| 30 | EECE | I — a creatinina normal é mascarada pela hiperfiltração. II — rim reduzido é o estágio *final*. IV — úlcera indolor com sondagem óssea exige investigar osteomielite. |

### Múltipla escolha (20 questões)

**20/20 conferem.** Q04 e Q18 pedem a alternativa *incorreta* e o gabarito aponta corretamente a assertiva falsa:

- **Q04 = E** — "cetose como consequência aritmética da hiperglicemia" é falso: os cetoácidos vêm da lipólise desinibida, não da conversão direta de glicose.
- **Q18 = C** — "disfunção endotelial só depois da placa visível" é falso: o primeiro dano vascular é funcional (inativação do óxido nítrico), anterior a qualquer achado de imagem.

As 18 restantes tiveram a alternativa marcada conferida contra o mecanismo da E1, uma a uma.

## 2. Corrida degenerada

- **MC, em ordem numérica:** C · B · E · A · D · B · E · A · B · D · B · C · E · A · D · A · C · E · A · D. Corrida máxima = 1. Sem 4+ consecutivas.
- **C/E:** as 10 sequências são ECCE, CCEE, CCCE, CCEC, CECC, ECCC, CEEC, EECC, CEEE, EECE. Nenhuma é `CCCC`, `EEEE`, `CECE` ou `ECEC`; todas as 10 são distintas entre si.
- **Balanço global C/E:** 22 C e 18 E em 40 itens (55%/45%) — próximo do equilíbrio sem ser 50/50 forçado.

## 3. Distribuição das MC

`{A: 5, B: 4, C: 3, D: 4, E: 4}` sobre 20 questões — letra dominante A com 25%, bem abaixo do teto de ~40%. Correta em A em 25% (média esperada por letra é 20%), dentro do normal.

**Nota de procedimento:** a distribuição saiu inicialmente 4/4/4/4/4, uniformidade que é sintoma de gabarito montado e não sorteado. Duas corretas foram **reposicionadas entre alternativas equivalentes** (Q14 de C para B, Q24 de B para A) — reposicionamento é permitido pelo canônico; mudar *qual* é a correta não seria.

## Veredito

**APROVADO.** Nenhuma divergência entre gabarito impresso e correta real; nenhuma corrida degenerada; distribuição sã.
