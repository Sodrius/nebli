# UC07 — painel de sessão (gerado; não editar à mão)

Gerado em 18/10/2026 12:09 por `./kenhub-deck --painel`. **Ler no início de toda sessão da UC07.**

## Onde estamos

| Deck | Notas | Verde/azul/rosa | Estado | Última execução | Corrida |
|---|---|---|---|---|---|
| NEBLI::UC07::Introdução ao sistema nervoso::Sistema nervoso central: introdução ao encéfalo | 43 | 15/28/0 | AGUARDANDO REVISÃO (revisao.md) | 2026-10-18T14:50 | `uc07-kenhub-introducao-ao-sistema-nervoso-sistema-nervoso-central-introducao-ao-encefalo-2026-10-17` |
| NEBLI::UC07::Introdução ao sistema nervoso::Sistema nervoso periférico: nervos, gânglios e plexos | 59 | 8/50/1 | AGUARDANDO REVISÃO (revisao.md) | 2026-10-18T14:48 | `uc07-kenhub-introducao-ao-sistema-nervoso-sistema-nervoso-periferico-nervos-ganglios-e-plexos-2026-10-17` |
| NEBLI::UC07::Medula espinal::Meninges espinais e raízes nervosas | 38 | 10/27/1 | AGUARDANDO REVISÃO (revisao.md) | 2026-10-18T14:30 | `uc07-kenhub-medula-espinal-meninges-espinais-e-raizes-nervosas-2026-10-17` |
| NEBLI::UC07::Medula espinal::Morfologia interna da medula espinal | 110 | 12/93/5 | AGUARDANDO REVISÃO (revisao.md) | 2026-10-18T14:44 | `uc07-kenhub-medula-espinal-morfologia-interna-da-medula-espinal-2026-10-18` |
| NEBLI::UC07::Medula espinal::Nervos espinais | 63 | 14/49/0 | AGUARDANDO REVISÃO (revisao.md) | 2026-10-18T15:08 | `uc07-kenhub-medula-espinal-nervos-espinais-2026-10-18` |
| NEBLI::UC07::Medula espinal::Topografia e morfologia da medula espinal | 78 | 19/52/7 | ENTREGUE (gates ok + revisão card a card e do deck) | 2026-10-18T15:00 | `uc07-kenhub-medula-espinal-topografia-e-morfologia-da-medula-espinal-2026-10-17` |
| NEBLI::UC07::Tronco encefálico::Visão geral e anatomia de superfície | 153 | 29/110/14 | ENTREGUE (gates ok + revisão card a card e do deck) | 2026-10-18T15:06 | `uc07-kenhub-tronco-encefalico-2026-10-17` |

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
| F-20261017-CLAUDE-01 | Deck por unidade do Kenhub, na ordem dele; toda estrutura ≥ 1 card; Kenhub primeiro, acervos completam; fisiopatologia só por acervo. | `[cobertura]` (deck.py)<br>`[kenhub-sempre]` (deck.py) | teste_gates: estrutura sem card → [cobertura] reprova |
| F-20261017-CLAUDE-02 | Frente só com a figura; nome em PT no topo do verso sem rolar; deck inteiro renderizado (PC e celular) e olhado no fim. | `G1 frente com texto` (render.py)<br>`G2` (render.py)<br>`G4` (render.py)<br>`G5` (render.py)<br>`G6` (render.py)<br>`[G8 português]` (deck.py)<br>`[G4 mídia]` (deck.py) | teste_gates: G6 reprova no vazio; G8 reprova nome em inglês |
| F-20261017-CLAUDE-03 | Nada abre janela na tela de Davi; o comando espera o Anki ficar livre, testa antes de escrever e é retomável. | `lifecycle operation is active` (deck.py)<br>`def pode_gravar_bandeira` (deck.py)<br>`headless=True` (navegador.py) | teste_gates: o navegador do Kenhub é invisível |
| F-20261017-CLAUDE-04 | Toda nota aceita comentário; cloze/nome = só o nome, em PT; todas as imagens à vista, sem botões; seta + IO em toda figura (máscara no alvo, seta até ele, nome em PT escrito no lugar do “?”); no AnKing, a máscara fica no “ID”; a frente nunca mostra a resposta; a seta termina sobre a anatomia. | `[G7 comentário]` (deck.py)<br>`[G8 só o nome]` (deck.py)<br>`G9 botão ou imagem escondida` (render.py)<br>`[G10 direcionamento]` (deck.py)<br>`G11 verso sem a figura com o nome` (render.py)<br>`[G12 resposta vazada]` (deck.py)<br>`[G13 seta na anatomia]` (deck.py)<br>`[histórico]` (deck.py) | teste_gates: G8 reprova “Pyramid / Pirâmide” e cloze longo; G12 reprova frente que mostra o nome; G13 reprova ponta no branco; tipo desconhecido reprova |
| F-20261017-CLAUDE-05 | IO padrão AnKing (retângulo vermelho com borda + seta vermelha limpa, sem “?” nem frase); verso sem nome em cima quando há seta (nome na ponta da seta); uma figura por card; Kenhub sempre (sem exclusão); nenhuma fonte em texto; figura de tamanho adequado; ordem das unidades = cronograma da UC07. Estrutura já existente em outra unidade é associada, nunca repetida. A máscara tem de ser vista de relance (G17); figura do AnatoKing que serve a muitos cards não conta como direcionamento. | `[kenhub-sempre]` (deck.py)<br>`[G14 sem fonte]` (deck.py)<br>`G14 fonte/crédito em texto` (render.py)<br>`G15 frente com` (render.py)<br>`G16 figura com` (render.py)<br>`G2 nome em cima com seta` (render.py)<br>`def retangulos` (mascara.py)<br>`[sem duplicata]` (deck.py)<br>`[G17 seta evidente]` (deck.py)<br>`figura do modelo é genérica` (deck.py)<br>`sem seta vermelha` (deck.py) | teste_gates: figura do Kenhub excluída → [kenhub-sempre]; campo Fonte preenchido → [G14]; máscara vira retângulos |
| F-20261018-CLAUDE-01 | Card do AnatoKing com uma só figura; além das estruturas, todo trecho do texto de estudo da unidade (objetivos, parágrafos, legendas do atlas, tabela-resumo) tem card — o quiz cobra os dois. | `[G20 uma figura]` (deck.py)<br>`[cobertura-quiz]` (deck.py)<br>`[chave de texto repetida]` (deck.py) | teste_gates: AnatoKing com 2 figuras e trecho de texto sem card reprovam |
| F-20261018-CLAUDE-02 | Termo traduzido por nós só passa se constar no Kenhub PT (locale=pt), no Ângelo Machado (Drive) ou na lista de aceitos com fonte (glossario_aceitos.json). | `[G18 tradução oficial]` (deck.py) | teste_gates: termo inventado reprova, termo do Machado passa |
| F-20261018-CLAUDE-03 | Depois de instalar e olhar as folhas, cada deck tem revisão card a card e do deck inteiro (revisao.md); só vira ENTREGUE com `./kenhub-deck --revisado`. | `AGUARDANDO REVISÃO` (painel.py)<br>`def revisado` (pipeline.py) | painel: sem revisao.json da mesma corrida a unidade não aparece como ENTREGUE |
| F-20261018-CLAUDE-04 | Card do Kenhub = figura com o destaque verde do próprio Kenhub + seta (sem máscara); nome na ponta da seta no verso. Cards de texto/AnKing com formatação AnKing clássica (sujeito em negrito) e figura no Extra. Gravar no Anki em lote e poucas vezes, nunca a toda hora. | `[G21 sem IO nas estruturas]` (deck.py)<br>`[G17 seta evidente]` (deck.py)<br>`G5 destaque verde` (render.py)<br>`[G22 formatação AnKing]` (deck.py)<br>`[G23 imagem no cloze]` (deck.py)<br>`[sem regravar à toa]` (deck.py) | teste_gates: máscara sobre estrutura, seta curta, card sem negrito, cloze sem figura reprovam; regravação < 6 h recusada |
| F-20261018-CLAUDE-05 | Cards da mesma estrutura em sequência na ordem da aula (Kenhub primeiro); só um verde por estrutura; cards de texto no tipo de nota do AnKing (clone fiel); figuras maiores e overlay em 2x. Vale para todo deck do Kenhub. | `[G25 estrutura junta]` (deck.py)<br>`[G26 uma verde por estrutura]` (deck.py)<br>`[G24 formato AnKing]` (modelo.py)<br>`ESCALA = 2` (mascara.py)<br>`G16 figura` (render.py)<br>`[G10 seta evidente]` (deck.py)<br>`[G27 termo explicado]` (deck.py) | teste_gates: estrutura espalhada, duas verdes na mesma estrutura reprovam; tipo de nota igual ao AnKing e figuras maiores verificados |

Feedback novo: literal em FEEDBACKS → regra no MEMORY §15 → entrada em `nebli/kenhub/feedbacks.json` → gate no código → caso ruim em `teste_gates.py` → `./kenhub-deck --painel` verde.

