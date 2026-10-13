# Análise do corpus vivo — 01/10/2026

Este documento é evidência da corrida, não memória normativa nem aprovação de deck. Consulta SQLite em URI `mode=ro`, `PRAGMA query_only=ON`, collation `unicase` registrada. Nenhum campo, agendamento, mídia ou configuração Anki foi alterado. O script reproduzível é `extract_corpus.py`; os dados são privados e não devem entrar em commit.

## Escopo e partições congeladas

Originais são exclusivamente notas com card físico no deck ID **1782836097813**, `Referências::Anking Step Deck`. Não foram usados MCAT, outros acervos ou cópias NEBLI como originais. Autorais são notas com card no ramo **NEBLI (1774)** e tag exata `NEBLI::origem::Autoral`.

- População: **28.649 notas AnKing** e **238 autorais** com tipo textual nesse escopo. Unidade é nota, não card; irmãos nunca viram observações independentes.
- Nativos elegíveis: **28.007**, retirando frente com imagem/áudio e algumas referências explícitas a imagem. A filtragem é conservadora, mas não é prova semântica de independência visual de todas as frentes.
- Corpus amostral: **480 nativos**, 60 em cada uma de oito famílias heurísticas; isso amplia diversidade e **não reproduz as proporções do deck**.
- `calibration.json`: 128 nativos, 16/família, permitidos ao juiz.
- `authoring-reference.json`: 80 nativos, 10/família, permitidos ao redator.
- `native-reserve.json`: 144 nativos, 18/família; não expostos em leitura textual ao analista/root.
- `untouched-validation.json`: 128 nativos, 16/família; não expostos em leitura textual, destinados a avaliação posterior.
- `native-dev.json`: visão derivada de 64 itens da reserva, 8/família.
- `native-holdout.json`: visão derivada dos 80 restantes da reserva + 128 intocados. **Essas duas visões NÃO são novos dados e não devem ser somadas às partições principais.**
- `authors-existing.json`: todos os 238 autorais textuais; contém EN/PT históricos, frentes com mídia e anotações de fonte. Filtrar simetricamente antes de compor teste.

As quatro partições principais são disjuntas por ID de nota e por hash do texto frontal normalizado (HTML removido, caixa/pontuação normalizadas, ordinal de cloze ignorado). Verificação executada com asserts. Isso não detecta paráfrases nem garante separação semântica por conceito. Nenhuma observação deve ser tratada como inédita apenas porque tem outro ID se o mesmo alvo já foi ensinado ao juiz.

`anking-io-separated.json` e `authors-io-separated.json` estão vazios **nesses filtros**. Isso não significa ausência de IO na coleção; os IO conhecidos podem estar em outros acervos/tags. **Esta rodada não avalia nem aprova IO ou reconhecimento visual.**

As famílias combinam disciplina e formato de recuperação: anatomia, histologia, bioquímica, micro/imuno/farma, mecanismos/fisiologia, clínica/diagnóstico, fatos/listas, cálculos/comparações. São buckets heurísticos, não classificação clínica definitiva: uma pergunta de nervo pode ser clínica, um contraste pode ser farmacológico. Houve correção antes do congelamento de falsos positivos de substring, como `nervosa`/`nerve`, `sustained`/`stain` e `formula` infantil. Persistem sobreposições e casos imperfeitos, e a cobertura por família precisa de leitura no lote final.

## Medidas observadas

Estatísticas integrais em `population-statistics.json`. Contagens de palavras são aproximações de texto desmarcado por regex, incluem resposta/dica do cloze e créditos do Extra; não equivalem a tempo de recuperação nem a palavras visíveis de cada irmão.

| Medida por nota | AnKing população (28.649) | Autorais existentes (238) | AnKing amostra (480) |
|---|---:|---:|---:|
| Palavras frente, mediana | 16 | 15 | 16 |
| Palavras frente, P10–P90 | 10–25 | 10–22 | 11–27 |
| Palavras Extra, mediana | 15 | 23 | 16 |
| Palavras Extra, P10–P90 | 0–51 | 6–43 | 0–55 |
| Ocorrências cloze, mediana | 1 | 1 | 1 |
| Ordinais distintos cloze, mediana | 1 | 1 | 1 |
| Frente com `?` | 10.206 (35,6%) | 4 (1,7%) | 155 (32,3%) |
| Frente com bold HTML | 27.084 (94,5%) | 0 (0%) | 466 (97,1%) |
| Frente com `<u>` | 20.021 (69,9%) | 0 (0%) | 335 (69,8%) |
| Frente com dica cloze | 4.951 (17,3%) | 0 (0%) | 98 (20,4%) |
| Frente com imagem | 631 (2,2%) | 3 (1,3%) | 0 |
| Extra com imagem | 16.286 (56,8%) | 155 (65,1%) | 306 (63,8%) |
| Extra não vazio, contando mídia | 24.968 (87,2%) | 220 (92,4%) | 432 (90%) |

Na amostra: ponto-e-vírgula em 7/480 nativos (1,5%) versus 31/238 autorais (13,0%); dois-pontos fora delimitadores cloze em 32/480 (6,7%) versus 29/238 (12,2%). Descrição da coleção não revoga a preferência explícita vigente de evitar `;` e `:` nos novos autorais. O fato de existirem dois-pontos legítimos no AnKing impede usar esse sinal sozinho como certificado de origem.

**O problema atual não é simplesmente “autorais compridos”: a mediana já é ligeiramente menor.** As diferenças mais fortes são a baixa diversidade de construção e apresentação, a quase ausência de perguntas/dicas e o Extra histórico com português, referência docente ou prosa explicativa recorrente. Um discriminador com bold preservado pode obter sucesso por um único atalho superficial; uma avaliação de prosa precisa também de uma vista que neutralize a formatação de ambos os lados.

## Leitura substantiva realizada

Lidos Text/Extra de **64 nativos da referência de autoria**, **40 autorais iniciais** e **32 autorais sorteados** (com sobreposição possível entre os dois grupos de autores). Leitura não incluiu reserva/holdout. Fonte local `reading-sample.txt` contém 64 + 40; o segundo sorteio foi executado com seed 981 sobre os 238. Não houve conferência médica externa nesta etapa; os exemplos analisam construção, não certificam a afirmação científica.

1. **Recuperação variada com relação clara.** Há nome de estrutura por função (exonucleases, 1468549172824), propriedade relativa (sensitivity/PPV, 1485917667823), localização ou raiz (bíceps, 1550600491028), fórmula (fração de filtração, 1474763686814), valor, aspecto histológico e decisão clínica. O padrão útil é tornar inequívoca a informação a recuperar com contexto suficiente. “Sempre um nome oculto numa frase de processo” descreve apenas parte do acervo e precisa conviver com outros tipos solicitados pelo usuário.
2. **Perguntas são normais.** Pergunta direta + resposta cloze é recorrente. Os 238 autorais históricos são quase todos declarativos, o que fornece uma assinatura de lote mesmo quando cada frase isolada é boa. Variação deve seguir a pergunta cognitiva, sem quota decorativa de interrogações.
3. **Cloze único não significa uma palavra nem uma única ocultação.** RIPE (1503254970224) e as constrições ureterais (1515539356519) usam vários segmentos `c1` para uma recuperação de conjunto. Outros usam `c1`/`c2` para alvos distintos numa relação. Isso não autoriza listas extensas arbitrárias: é necessário decidir se o conjunto é uma unidade útil ou se os alvos precisam de revisões independentes.
4. **Dicas delimitam resposta.** Exemplos `innervation`, `spinal roots`, direção/alternativas e número de nomes ajudam a tornar a resposta esperada definida. Não são necessárias em tudo e podem reduzir demasiado a recuperação se entregarem o fato. Ausência total de dicas nos autorais históricos é uma diferença, não uma recomendação de acrescentar dica em cada card.
5. **O Extra real tem cauda longa e muitas funções.** Pode ser vazio, um contraste, uma razão, tabela, observação prática ou mnemônico existente. Os exemplos de hipernatremia corrigida, transposição bacteriana e estenose renal mostram Extras com funções distintas e tamanhos diferentes. “Extra sempre vazio ou bullets curtos” é uma preferência de produção, não descrição universal do AnKing. Não inventar mnemônico para imitar frequência.
6. **Autores antigos mostram duas gerações.** Frentes antigas combinam duas proposições por `;`, rótulos de tópico e esclarecimentos professorais. Notas recentes de complemento/operon já estão mais focais e alguns Extras estão vazios ou em uma linha. Não generalizar a assinatura de 238 notas heterogêneas para a versão nova nem apagar bons cards apenas por origem.
7. **Alguns autorais já cumprem a recuperação.** IPTG definido por sua função, efereocitose ligada à remoção de neutrófilos e hidrólise espontânea do C3 são focais na leitura. Ausência de negrito não os transforma em cards pedagogicamente ruins. Outros ainda usam referências como “the lecture table”, que exigem contexto externo ou denunciam procedência; no teste de estilo essas pistas devem ser separadas de qualidade factual.
8. **AnKing não tem monopólio de assunto.** Mutantes de operon, diploide parcial, detalhes docentes ou outro tema fora Step devem poder ser escritos nesse estilo. Um juiz que usa “isso não cai no Step” está classificando conteúdo/origem provável, não a construção. Para transferência real, avaliar esses itens com critério funcional sem incluí-los numa acurácia supostamente balanceada por tema quando não houver controles comparáveis.

## Falhas documentadas no legado

O script `flashcards/scripts/card_mirror_blind.py` tem riscos concretos:

- Consulta Anki por termos sem delimitar deck nativo; pode chamar de “ANKING” um autoral ou uma cópia NEBLI.
- Aplica `clean()` em Text/Extra dos supostos AnKing, mas não aplica a mesma transformação ao Text autoral. No Extra autoral apenas remove a substring `img`.
- Expõe **nome de arquivo de imagem** (`[img ...]`), extraído por rotas diferentes; isso é pista de origem/layout, não estilo.
- Trunca Extra em 180 caracteres; pode esconder diferenças substantivas e cortar frases em posições arbitrárias.
- Não grava seed reprodutível completo, separação calibração/dev/teste, agrupamento de irmãos, probabilidades ou métricas de discriminador.

O veredito `.../deck-aula-uc03-imuno-p2-2026-09-30/card-mirror-verdict-round4.txt` declara explicitamente **“Não se exige acertar origem”** e termina em compatibilidade editorial. Isso é revisão útil de qualidade, mas **não demonstra que um agente tentou identificar a origem e falhou**. A própria revisão reconhece que ausência de assinatura não comprova identidade. Não converter seu “compatível” em acurácia próxima do acaso.

O módulo novo `nebli.card_mirror` apareceu durante esta sessão com intenção de normalização simétrica e métricas. Ele deve ser avaliado pelos resultados desta corrida, separadamente do script legado. O relatório aqui não certifica sua implementação.

## Consequências para o experimento

O juiz deve receber exemplos calibradores amplos, mas nenhum gabarito, tags, ID de origem, caminho de imagem, referência docente ou histórico de produção do lote a classificar. Comparar pelo menos frente pura e frente + Extra; uma vista adicional sem markup serve para distinguir domínio da prosa de assinatura visual. Créditos devem ser removidos simetricamente na visão cega, mantendo os originais e auditoria privada; nunca fabricar créditos ou inserir defeitos para enganar.

Registrar palpite AnKing/Autoral, probabilidade e evidência por item. Medir acurácia balanceada, AUC, tendência de chamar tudo AnKing e desempenho por família. Julgar separadamente clareza da recuperação, ambiguidade, tamanho da resposta, pista que entrega resposta, erro factual e ganho do Extra. Falhar em distinguir não basta se os cards ficaram piores.

Rodadas de refinamento são desenvolvimento; um juiz novo e itens novos são necessários para uma avaliação final. Acerto perto de 50% em poucas dezenas tem grande incerteza; acerto abaixo de 50% pode indicar assinatura invertida. O holdout não deve ser consumido repetidamente até sair resultado favorável. “Treinar” nesta arquitetura significa calibrar por exemplos no contexto e persistir uma receita verificável; não há ajuste de pesos do modelo.

Este corpus torna o teste possível e corrige premissas estreitas. Não demonstra sozinho que os autorais ficaram indistinguíveis, que todos os assuntos foram cobertos ou que estudar 30/dia já produzirá retenção ideal. Essas conclusões precisam, respectivamente, dos julgamentos cegos, de novos tipos/IO e dos dados reais de revisão do usuário.
