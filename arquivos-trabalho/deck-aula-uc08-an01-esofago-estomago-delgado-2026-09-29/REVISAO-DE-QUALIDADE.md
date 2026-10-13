# Revisão de qualidade — AN01 Esôfago, estômago e intestino delgado (UC08 P1)

**Aula / run / versão:** AN01 · `uc08-an01-20260929a` · `selection_hash dab89df2dcf0f009` (v1 instalada `2679cd0d01658546`, corrigida na mesma corrida). Executor: Claude, 29/09. E1: não aplicável (pedido "sem e1"). Critérios: MEMORY de 29/09 + FEEDBACKS até F-20260929-CODEX-04; nenhuma revisão Codex nesta corrida.
**Deck:** `NEBLI::UC08::P1::Anatomia::Esôfago, estômago e intestino delgado`, preset da raiz.

## Fontes (detalhe em `fontes.json`)
- Slides (24 lâminas) lidos e **renderizados/vistos integralmente**; roteiro prático (7 itens) e 12 questões orientadoras lidos; E1 histórica consultada.
- Prova: não localizada (buscas registradas). Netter do Drive (118 MB) inacessível pelo conector: pranchas Netter usadas como aparecem nos slides. Substitutos lidos: OpenStax A&P 2e 23.4/23.5; Wikipedia (músculo suspensor do duodeno, ângulo de His); TeachMeAnatomy (estômago); dicionário/IMAIOS (canal gástrico). **Conflito registrado:** OpenStax diz que o íleo é mais espesso/vascular que o jejuno; slide, Netter, Dope e AnKing dizem o contrário — cards seguem o slide.
- Pista de Davi (doc "cards UC08"): nids pertinentes conferidos (dois já vivos na FI08; dois selecionados; vasculares → AN07).

## Cobertura
Matriz lâmina a lâmina em `matriz-objetivos.tsv` (27 blocos). Todos os objetivos, os 7 itens do roteiro e as 12 questões têm card ou associação. Fora, com motivo: faringe, 9 regiões abdominais como sistema, funções/motilidade (FI), irrigação (AN07), ligamentos peritoneais (AN13), conduta dos casos clínicos.

## Escolhas que mostram o padrão
- **Busca antes de autorar:** AnKing por texto (regex no campo Text) e por tags FirstAid/Systems; depois Dorian, Dope, BlueLink e, por último, AnatoKing. Cinco autorais, cada um com lacuna registrada (lig. frenoesofágico, incisura cárdica, canal gástrico, estrutura de Treitz, quadrantes jejuno/íleo); forma curta AnKing-like, frase que ensina a relação, verso causal curto e figura do slide ou de card AnKing.
- **Compartilhados sem duplicar:** 7 alvos já vivos na FI08/BT03 (terço estriado/liso, EES/EEI, Chagas, camadas, oblíqua) foram associados por tag `NEBLI::2026-uc08-anatomia-01-…` + `NEBLI::compartilhado::an01`, sem mudar conteúdo, deck ou flag.
- **Irmãos:** T10 com c1/c2/c3; colédoco/pancreático c1/c2; Meckel ectópico c1/c2. Desfeitos só c3/c4 de T12 (ducto torácico/ázigo, não ensinados).
- **Clínica pertinente (Q044):** perfuração endoscópica ↔ constrições; úlcera na curvatura menor; úlcera posterior ↔ a. esplênica; Barrett ↔ linha Z; cálculo na ampola; síndrome da AMS; Treitz como marco alto/baixo. Sem abrir doenças.
- **Anatomia visual:** peças BlueLink (cadáver) preferidas ao AnatoKing; AnatoKing só onde nenhum outro acervo rotula (cárdia, fundo, corpo, antro, canal, porção pilórica, incisura angular, esôfago cervical), com imagem principal ampliada no modelo NEBLI (F-C23).
- **Cores (27 verdes / 43 azuis):** verdes = regiões gástricas e bordas, piloro, porções 1ª/2ª do duodeno e papila maior, constrições, níveis T8/T10/T12, abdominal do esôfago, vasos retos do jejuno, Treitz como marco e HY do mesmo alvo (úlcera na curvatura menor, Barrett, colédoco+pancreático, Meckel). Azuis = identificações secundárias, relações e clínica de apoio.

## Revisão realizada (Q040 — amostra + riscos)
- **Estrutural, todos os 70 cards:** readback de campos, tags, ordinais, flags, deck, não suspensos; zero problemas (`receipt.json`). Compartilhados conferidos sem mudança de deck.
- **Renderizados e lidos (frente/verso):** 34 notas — todos os 5 autorais, 5 Dope/Dorian adaptados, 8 AnatoKing, 9 BlueLink (com CSS que força a imagem, pois o Quick Look não roda o JS do template), 7 AnKing.
- **Achados corrigidos na mesma corrida:** clínica de Crohn (lateral) no verso da prancha de arcadas → trocada; AnatoKing cárdia/corpo com foto retroperitoneal ilegível na frente → retirada; AnatoKing esôfago cervical com número ilegível → imagem do modelo com seta na frente. Readback e sync após a correção.
- **Não lidos individualmente:** 25 notas AnKing/BlueLink restantes, do mesmo modelo/padrão das amostras (clozes conferidos por script).

## Estados
- Conteúdo: revisado pelo executor; sem revisão Codex. Limites: prova e PDF do Netter indisponíveis.
- Técnico: instalado e verificado; sync solicitado pelo `escrita()` (chegada em outros aparelhos não conferida).
- Contabilidade: 59 notas novas / 70 cards (AnKing 20 notas/26 cards, BlueLink 18/18, AnatoKing 8/8, Dope 5/8, Dorian 3/5, autorais 5/5); 27 verdes, 43 azuis, 0 suspensos; + 7 notas compartilhadas associadas.
