# UC07 — painel de sessão (gerado; não editar à mão)

Gerado em 17/10/2026 14:57 por `./kenhub-deck --painel`. **Ler no início de toda sessão da UC07.**

## Onde estamos

| Deck | Notas | Verde/azul/rosa | Estado | Última execução | Corrida |
|---|---|---|---|---|---|
| NEBLI::UC07::Tronco encefálico::Visão geral e anatomia de superfície | 116 | 45/54/17 | ENTREGUE (gates ok) | 2026-10-17T17:54 | `uc07-kenhub-tronco-encefalico-2026-10-17` |

Fila e tabela das 51 unidades: [PLANO-UC07-NEUROANATOMIA-COMPLETA-2026-10-17.md](PLANO-UC07-NEUROANATOMIA-COMPLETA-2026-10-17.md). Próxima: a primeira “a fazer” na ordem sugerida do plano.

## Rodar uma unidade

```
./kenhub-deck <slug-da-unidade> "<Módulo>" "<Submódulo>"
```
Para pedindo curadoria (rascunho gerado); depois instala, reconcilia e só termina com TODOS os gates ok. Olhar as folhas de contato.
Antes de instalar: navegador de cards do Anki fechado (o comando avisa). No fim: `pkill -f nebli.kenhub.navegador` (Kenhub = 1 aparelho por vez).

## Feedbacks de Davi → gates duros (teste dos gates: OK)

| Id | Regra | Gates (onde reprova) | Prova |
|---|---|---|---|
| F-20261017-CLAUDE-01 | Deck por unidade do Kenhub, na ordem dele; toda estrutura ≥ 1 card; Kenhub primeiro, acervos completam; fisiopatologia só por acervo. | `[cobertura]` (deck.py)<br>`[kenhub-primeiro]` (deck.py) | teste_gates: estrutura sem card → [cobertura] reprova |
| F-20261017-CLAUDE-02 | Frente só com a figura; nome em PT no topo do verso sem rolar; deck inteiro renderizado (PC e celular) e olhado no fim. | `G1 frente com texto` (render.py)<br>`G2` (render.py)<br>`G4` (render.py)<br>`G5` (render.py)<br>`G6` (render.py)<br>`[G8 português]` (deck.py)<br>`[G4 mídia]` (deck.py) | teste_gates: G6 reprova no vazio; G8 reprova nome em inglês |
| F-20261017-CLAUDE-03 | Nada abre janela na tela de Davi; o comando espera o Anki ficar livre, testa antes de escrever e é retomável. | `lifecycle operation is active` (deck.py)<br>`def pode_gravar_bandeira` (deck.py)<br>`headless=True` (navegador.py) | teste_gates: o navegador do Kenhub é invisível |
| F-20261017-CLAUDE-04 | Toda nota aceita comentário; cloze/nome = só o nome, em PT; todas as imagens à vista, sem botões; seta + IO em toda figura (máscara no alvo, seta até ele, nome em PT escrito no lugar do “?”); no AnKing, a máscara fica no “ID”; a frente nunca mostra a resposta; a seta termina sobre a anatomia. | `[G7 comentário]` (deck.py)<br>`[G8 só o nome]` (deck.py)<br>`G9 botão ou imagem escondida` (render.py)<br>`[G10 direcionamento]` (deck.py)<br>`G11 verso sem a figura com o nome` (render.py)<br>`[G12 resposta vazada]` (deck.py)<br>`[G13 seta na anatomia]` (deck.py)<br>`[histórico]` (deck.py) | teste_gates: G8 reprova “Pyramid / Pirâmide” e cloze longo; G12 reprova frente que mostra o nome; G13 reprova ponta no branco; tipo desconhecido reprova |

Feedback novo: literal em FEEDBACKS → regra no MEMORY §15 → entrada em `nebli/kenhub/feedbacks.json` → gate no código → caso ruim em `teste_gates.py` → `./kenhub-deck --painel` verde.

