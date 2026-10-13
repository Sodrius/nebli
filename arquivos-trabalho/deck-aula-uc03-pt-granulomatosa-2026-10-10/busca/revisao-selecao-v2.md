# Revisão editorial antes de materializar cards — PT47, 10/10

Esta é uma decisão sobre **objetivos**, não um deck nem bandeiras aplicadas. A triagem original está em `../triagem-cores-v1.json`; a versão de trabalho em `../triagem-cores.json`. Nenhum alvo foi excluído apenas para atingir uma contagem. Os 127 objetivos únicos de slides passaram de 41/72/14 para **36 verdes, 78 azuis, 13 rosas**. Dez foram rebaixados por menor ganho longitudinal; cinco foram promovidos após conciliar mecanismos, reconhecimento visual e provas, e MIF passou de rosa a azul por cobrança nominal. Um card pode recuperar dois objetivos e um objetivo pode exigir imagem; essas contagens não são total físico de cards.

## O que saiu do núcleo longitudinal

| Objetivo | Decisão | Motivo |
|---|---|---|
| Via de inalação da TB | azul | Passo de entrada necessário à aula, de baixo ganho isolado após compreender persistência alveolar. |
| Paliçada | azul | Útil para a prova e a leitura da lâmina; a função da rima linfocitária foi promovida a verde após prova antiga cobrá-la diretamente. |
| Fusão de macrófagos; padrão nuclear de Langhans | azul | Morfologia cobrável, sem exigir duas recuperações longitudinais além da identificação do granuloma. Langhans não determina etiologia. |
| Nome/cores de Ziehl-Neelsen | azul | Reconhecimento visual dos BAAR continua verde; técnica e cor são preparo de prova. |
| Ausência de caseificação em amostra de TB | azul | Ressalva da aula preservada; deriva do verde “necrose não é obrigatória”. |
| Foco de Ghon subpleural | azul | Localização cobrável; o complexo foco + linfonodo permanece verde como relação primária. |
| Agregação inata antes da resposta adaptativa | azul | Evidência de modelo experimental; ensinar com qualificador, sem extrapolar cronologia universal humana. |
| Equilíbrio da intensidade de TNF | azul | Nuance da parte II, enquanto a função de TNF na manutenção do granuloma já é verde. |

Quatro objetivos passaram de azul a verde após confrontar a proposta visual com o mecanismo: morte macrofágica → liberação bacilar, reconhecimento da cavidade, reconhecimento do padrão miliar e relação silicose–TB por disfunção macrofágica. O achado de fibrose da lâmina 13 continua azul como objetivo secundário coberto no mesmo card visual verde da necrose; DNA/RNA como índice de viabilidade fica rosa, e o visual de sarcoidose fica azul, com diagnóstico diferencial conceitual verde.

A **função da coroa linfocitária** passou de azul a verde: a prova UC03 P2 2015 (questão 1.1) pediu a periferia do granuloma e sua função de manter ativação macrofágica; a P2 2016 (questão 3.4) usou perda de CD4 para explicar granuloma malformado. **MIF** passou de rosa a azul porque a P2 2023 (questão 3.5) o nomeia; o card continua retido até revisão científica. Evidência textual em `../fontes/provas-trechos.txt`.

## Piloto autoral: disposição antes do spec

O lote `autorais-piloto-v2.json` foi um ensaio, não uma lista de instalação. Não “consertar” por estilização em cima do conjunto revelado. Decisões pendentes/novas para a produção:

- `pt47-a-s08-mhcii`: **associar identidade NEBLI viva** `1791625427059` e conferir o cloze; não criar autoral equivalente.
- `pt47-a-s08-il2`: **confrontar identidades vivas** `1791625429033` e `1791625429158`; só autorar se o alvo particular da aula continuar descoberto.
- `pt47-a-s06-mif`: **segurar para revisão de conteúdo**; a prova P2 2023 justifica azul e recuperação nominal, mas a atribuição exclusiva de retenção a MIF exige conferência. Não copiar sem revisão um mecanismo simplificado do gabarito.
- `pt47-a-s02-purpose`: o cloze em “contain” cobra verbo genérico; testar se o par persistência → contenção é melhor recuperado num card mais específico, sem duplicar a definição celular.
- `pt47-a-s07-shield`: “antibodies and extracellular complement” junta dois mecanismos num cloze amplo; separar alvo útil de inferência trivial e conferir com microbiologia antes de reescrever.
- `pt47-a-s43-ammonia`: cloze em “pH” é muito fácil; manter o mecanismo nos alvos da aula, mas pedir uma recuperação com ganho próprio antes de criar card.
- `pt47-a-s10-fusion`: proposta piloto dizia verde; a triagem v2 recomenda **azul**. A revisão da bandeira vale no spec, preservando o candidato experimental como evidência.

Os demais candidatos ainda precisam de conferência científica, busca externa por alvo, comparação com visuais e revisão de duplicações. A série curta sobre mecanismos de TB e seus Extras vazios foi identificada por dois juízes novos em 18/18 autorais mesmo na v2. Os controles incluíam muitas associações clínicas e imagens; o ensaio é falha de transferência e também teste misto de assunto/função. Não há alegação de que autorais estejam AnKing-like para Davi.

## Próxima decisão de produção

Montar um mapa final alvo → card físico/cloze/visual/compartilhado na ordem dos slides, conferindo as duas apresentações sem duplicar a segunda volta. Para cada verde, registrar ganho incremental frente aos outros verdes da UC03 e custo de revisão; para cada azul, evidência de aula/prova; para rosa, ganho de prova de menor prioridade. Só então gerar spec, inspecionar imagens reais, rodar lint/gates e testar no Anki.
