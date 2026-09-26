# NEBLI Decks — arquitetura v2

> **Plano histórico de arquitetura, não regra de produção.** Política atual em [README.md](README.md), incluindo E1 + cards, não redundância sem ganho e retenção verde/azul/incerto. Regras antigas de cor, volume ou entrega neste plano não prevalecem. Use [OPERACAO-CODEX-CLAUDE.md](OPERACAO-CODEX-CLAUDE.md) para o estado implementado; upload APKG pausado.

Estado: especificação do produto futuro, não implementação concluída. Para executar uma aula hoje, usar [EXECUCAO-DECK-AULA.md](EXECUCAO-DECK-AULA.md). Preferências em [README.md](README.md); construção do comando genérico em [IMPLEMENTACAO.md](IMPLEMENTACAO.md).

## 1. Contrato do produto

Entrada usual: “gere o deck da aula X”, por título, link, slug ou material. A sessão resolve fontes e identidade, executa a curadoria, entrega E1/guia e seleção, instala no perfil configurado, exporta/publica os artefatos e informa o resultado. Pergunta somente dados ausentes que realmente mudam a decisão.

Uma ação para o usuário; etapas internas retomáveis para o sistema. Sem aplicação nova, serviço permanente, assinatura adicional, subagentes obrigatórios ou chamadas pagas de LLM. A sessão faz o julgamento; scripts locais fazem busca, validação, estado e operações.

Saída de uma execução concluída:

- seleção completa do recorte, com cards já existentes, novos e compartilhados discriminados;
- yield de origem e seleção auditável; escolhas de importância para a faculdade ficam com o estudante;
- E1 e guia curto de onde aprender, vinculados à versão do escopo;
- Anki conferido após aplicação; APKG da aula e da UC, com mídia e manifesto;
- links em destino privado configurado, atualizados sem duplicar arquivos;
- resumo de cobertura, exceções, carga estimada e ações de calendário.

Se faltar fonte, acesso ao Anki ou publicação, entregar o que foi possível com estado parcial explícito. “Preparado”, “instalado”, “exportado” e “publicado” são estados diferentes.

## 2. Escopo: o que entra e o que fica em outra aula

Cada objetivo tem localização na fonte, profundidade exigida, recuperação desejada e uma decisão:

| Classe | Destino padrão |
|---|---|
| `taught` — ensinado ou material obrigatório desta aula | Seleção principal, com prioridade proporcional à importância. |
| `assessed_recap` — retomado e efetivamente exigido nesta aula | Reutilizar o card já existente e associá-lo à aula; não copiar novamente. |
| `prerequisite` — apenas pressuposto para acompanhar | Referência “revisar antes”, fora da seleção principal; recuperação opcional explícita. |
| `bridge` — pequena ponte clínica diretamente explicativa | Seção identificada; somente quando compreensível e útil. Não abrir novos ramos recursivamente. |
| `illustration` — exemplo incidental sem objetivo de retenção | E1/guia se útil; sem card obrigatório. |
| `future` — aprofundamento de aula posterior | Registrar onde será abordado, se conhecido; não incluir agora. |
| `out_of_scope` — coincidência de termo/tema sem pertinência | Excluir com motivo. |

O deck principal é a união dos cards pertinentes a `taught` e `assessed_recap`. Pontes aparecem separadas no relatório. Pré-requisito não é conteúdo faltante do deck. Um conceito necessário para responder ao próprio alvo da aula pode receber apoio no Extra/guia sem abrir uma série de novos cards.

Não converter a classificação em uma forma de esconder lacunas: se o docente ensina, enfatiza ou exige o conhecimento, não chamá-lo de pré-requisito/ilustração só porque a busca foi difícil. Auditar exclusões de itens relevantes contra a fonte.

Um objetivo composto deve ser decomposto na medida necessária para avaliar cobertura. “Entender inflamação” é amplo demais; “diferenciar flegmão e abscesso pelo padrão de distribuição” é auditável. Não decompor mecanicamente cada frase.

### Fontes e seus papéis

- Material docente/obrigatório define o recorte e a profundidade contextual.
- Provas antigas pertinentes calibram o que precisa ser recuperado/aplicado e a prioridade local, sem alargar para outras aulas.
- Bibliografia valida precisão e esclarece o mesmo recorte. Livro citado não é livro acessado; capítulo inteiro não vira checklist obrigatório.
- E1, tema-card e mapa de confusões ajudam a organizar; não são únicos árbitros do escopo.
- Vídeo ajuda a aprender e a encontrar tags/candidatos; o conteúdo extra do vídeo não entra automaticamente.
- AnKing é repositório de perguntas, não currículo da aula.

Conflito científico entre slide, transcrição, gabarito e livro exige checagem e nota explícita. Preservar contexto de cobrança sem transformar erro de transcrição em verdade no card.

## 3. Curadoria AnKing-first sem falsos negativos fáceis

### 3.1 Identidade antes da seleção

Consultar o registro e o Anki vivo: o card já tem cópia NEBLI? Já foi estudado? Cobre exatamente este alvo? Se sim, reutilizar identidade; se só é pré-requisito, referenciar sem associar ao principal. Não substituir silenciosamente um card revisado por uma variante mais bonita.

Para uma nova pergunta, prioridade: **AnKing → decks externos adequados → autoria mínima**. A qualidade e o escopo continuam sendo condições de entrada, não consequências da origem.

### 3.2 Busca em camadas

1. **Mapa de termos por objetivo:** português/inglês, sinônimos, nomes antigos, siglas, mecanismos, estruturas e contrastes. Buscar o alvo perguntado, não só o título da aula.
2. **Tags temáticas e de recursos:** sistema, disciplina, Pathoma, First Aid, B&B, Ninja Nerd e demais tags presentes. Ler ramos irmãos pertinentes. Preferência por Ninja Nerd não é filtro eliminatório.
3. **Texto independente de tags:** frente/Text serve à recuperação ativa; Extra/verso também pode fornecer cobertura para aprender quando explica, com precisão e pertinência, o alvo da aula. Uma ocorrência solta ou referência incidental nunca aprova automaticamente.
4. **Vizinhança dos bons resultados:** outras notas nas tags relevantes e perguntas complementares. IDs cronologicamente próximos não são prova de relação semântica.
5. **Segunda busca das lacunas:** reformular pelo mecanismo/contraste, usar outra taxonomia/recurso e retirar filtro temático restritivo. Registrar resultado e inadequações.
6. **Outros decks:** rotear por necessidade — cadáver/atlas, histologia, IO, fisiologia etc. Verificar imagem e pergunta. Não forçar um deck externo quando AnKing já é melhor.
7. **Autoria:** só para alvo pertinente sem pergunta adequada após essas checagens, com fonte verificável. Falha de acesso ao corpus é `unavailable`, não ausência comprovada.

Índice local incremental com SQLite FTS, campos pesquisáveis separados, tags hierárquicas e texto normalizado. Não precisa de embeddings/API no MVP. Paginar até avaliar candidatos relevantes; limite de contexto não vira teto oculto de seleção. Guardar consultas, quantidade, IDs avaliados, decisões e justificativas, sem guardar segredo/token.

### 3.3 Decisão por card, não só por nota

Uma nota pode gerar vários clozes. Registrar qual cloze/template testa qual alvo; irmãos fora do escopo não podem entrar ativos por acidente. Ler frente e verso renderizados, além dos campos originais. Uma nota de Crohn que menciona abscesso não testa a definição de abscesso.

Preservar bons cards externos com alterações mínimas. Ajustar ambiguidade/contexto ou acrescentar apoio em português quando necessário, mantendo origem e diff. Não traduzir/reformatar tudo por reflexo.

Fatos nominais e relações curtas favorecem cloze; mecanismo pode pedir etapa, consequência ou contraste; imagens exigem identificação visual quando isso foi ensinado. Não impor uma forma universal, um cloze único ou quota de imagens/palavras. Não fundir clozes revisados só para reduzir contagem. Antônimos não são automaticamente perguntas redundantes.

### 3.4 Critério para parar de buscar

Encerrar um objetivo quando houver conjunto suficiente, preciso, pertinente e sem duplicação semântica injustificada. Não importar todas as variantes existentes. Para objetivo ainda sem solução, concluir apenas com exceção explícita ou autoria fundamentada; nunca com “não apareceu na primeira tag”. Não prometer prova exaustiva de inexistência num corpus grande.

## 4. Prioridade, yield e visualização

Manter eixos distintos:

| Campo | Valores | Evidência |
|---|---|---|
| `step_yield`, por card | HY, MY, LY, desconhecido, conflitante | Tags originais e avaliação contextual registrada. Não inventar equivalência de níveis heterogêneos. |
| `scope_role` | classes da seção 2 | Onde e por que foi dado. |
| `learning_state` | não iniciado, em estudo, revisão ativa etc. | Estado observado, não classificação de importância. |

Step HY fora do escopo não entra no principal. Step LY pode ser obrigatório para uma prova local. Tag desconhecida não é LY. Conceito durável não deixa de sê-lo por ter aparecido em uma prova. Anatomia e bioquímica recebem a atenção longitudinal que o usuário valoriza, sem blindagem automática de todo detalhe.

Armazenar tags de yield originais literalmente, derivação normalizada e justificativa. Uma nota com múltiplos clozes pode exigir avaliações distintas. A importância para a faculdade e a decisão pós-prova pertencem ao estudante e não devem ser inferidas ou exibidas pelo sistema.

Origem e justificativa ficam no manifesto/relatório de cobertura, não em rodapés visíveis no verso. O card preserva o formato da sua origem e não dá pistas da resposta.

Bandeira vermelha é um indicador pessoal de card a revisar, remover ou melhorar — inclusive com imagem quando apropriado. Verde é aplicado somente à tag AnKing literal `#AK_Step1_v12::#Low/HighYield::1-HighYield`; HY relativo, temporário, LY e ausência de tag não recebem verde. Flags pessoais vencem qualquer automação. [Manual Anki: bandeiras e suspensão](https://docs.ankiweb.net/studying.html).

Não prefixar todas as aulas com HY. O rótulo de aula, se usado, precisa de justificativa curricular, não do simples fato de conter um card HY; nomes/IDs estáveis não dependem dessa etiqueta mutável.

## 5. Um acervo, várias aulas, uma revisão

Camadas separadas:

1. **Originais externos:** referência, sem escrita do pipeline.
2. **Notas/cards canônicos NEBLI:** única cópia adotada de cada origem, com campos independentes, mídia rastreável e histórico preservado.
3. **Associações por objetivo/aula:** quais cards pertencem ao recorte e por quê, compartilháveis.
4. **Visualizações de estudo e pacotes:** por aula, prova, UC, sistema e seleções longitudinais explicitamente escolhidas pelo estudante.

Mesmo card ensinado em Patologia e Imunologia: duas associações, uma identidade. Conceito só pressuposto em Imunologia: referência de pré-requisito, não nova associação obrigatória. Mesmo texto não basta para deduplicar; comparar alvo e contexto, mantendo direção de pergunta quando acrescenta valor.

No Anki, uma localização física estável; seleções por busca e decks filtrados quando adequados. Na geração de outra aula, não mover automaticamente todo o conteúdo anterior para o novo deck. Decks filtrados têm limitações — não puxam suspensos nem cards que já estejam em outro filtrado — e precisam de reconstrução. Não prometer duas cópias físicas simultâneas da mesma revisão. [Manual Anki: decks filtrados](https://docs.ankiweb.net/filtered-decks.html).

Hierarquia proposta de apresentação, sem migrar a coleção agora: `NEBLI::2026::UC03::P2::Patologia::38 - Inflamação aguda`. Identidade estável por lesson_id, não pelo nome. A visualização inclui compartilhados independentemente do home deck. Na plataforma móvel, validar a experiência real; não prometer criação automática de filtrados sem adaptador disponível.

Para clozes: preservar numeração e identidade. Separar metadados de nota e de card. Tags nativas são de nota; não bastam para selecionar irmãos de forma diferente. Usar registro por card e consultas com card IDs/template/cloze onde suportado. Projeção visual por cloze precisa de teste; um campo comum não pode rotular todos os irmãos incorretamente.

Modelos NEBLI independentes do tipo de nota AnKing, visual equivalente e mídia/credits/campos úteis preservados. Remover vínculo ativo com AnkiHub no clone; registrar o identificador original em campo de proveniência separado. Não editar template compartilhado com AnKing. Não fazer migração que regenere IDs/histórico sem ensaio em perfil isolado.

## 6. E1 e onde aprender

Mapa comum orienta E1, cards e guia, mas são entregáveis distintos. Geração padrão produz E1 ou reutiliza versão já validada para os mesmos inputs, sem omiti-la da entrega. E2/E3 não são dependências. A seleção não força a E1 a crescer a cada candidato ou Extra encontrado.

Guia por objetivo: livro/edição/capítulo efetivamente consultado; vídeo/título/link/trecho verificado; lacunas e pré-requisitos referenciados. Preferir poucos bons vídeos. Se a transcrição não estiver disponível, marcar cobertura ainda não verificada em vez de inventar timestamps.

Pontes Step podem ter explicação curta no guia. Não criar obrigatoriamente mais um PDF de duas páginas se o guia já resolve. A opção de tutorial de card difícil fica para versão posterior.

## 7. Calendário, carga e progressão

Ler planilha ao executar, com aba Mês prevalecendo em datas. Resolver aula, evento e prova por identidade/contexto; não por posição fixa da linha. Preservar origem das datas, fuso America/Sao_Paulo e conflitos não resolvidos.

Estados de política e observados são distintos. Suspensão manual/desconhecida nunca é levantada silenciosamente. A versão atual **não infere nem grava automaticamente** “núcleo”, “prova” ou “reserva”. Leech/enterramento e suspensão não são a mesma coisa. Aulas futuras não suspendem revisão já iniciada.

Novo conteúdo pode usar data e ritmo diário para informar elegibilidade e carga. No primeiro comando posterior a uma prova, atualizar pendências e relatar a mudança de calendário, mas não pausar cards sem decisão explícita de Davi ou uma classificação persistida que ele tenha aprovado. Se data de prova faltar, não inventar pausa. Múltiplas associações precisam ser mostradas antes de qualquer mudança de estudo.

Estimar carga com dados reais: minutos, repetições, novos, reaprendizado, backlog, intervalos e sessões extras. Quantidade disponível não é quantidade introduzida por dia. Manter 50 minutos como orçamento de referência, não garantia; respeitar aumento temporário escolhido conforme prova. Preservar configuração de agendamento inicialmente; não reduzir retenção nem esconder revisões vencidas para maquiar excesso.

Mapa Step 1 pequeno e versionado por sistemas/objetivos: não abordado, planejado em aula futura, abordado, selecionado, em revisão. Não confundir presença de card com domínio. Revisão periódica no fechamento de UC/sistema, não pesquisa gigantesca em toda aula. Lacuna longitudinal vai para aula futura ou tarefa separada, não invade a próxima aula. A matriz oficial orienta áreas/competências, não HY de cada fato. [USMLE: conteúdo Step 1](https://www.usmle.org/exam-resources/step-1-materials/step-1-content-outline-and-specifications).

## 8. Dados mínimos e artefatos

SQLite é o registro operacional; arquivos JSON/Markdown versionados são interfaces para o modelo e relatórios legíveis. Migrações explícitas, chaves estrangeiras e unicidade; não criar várias fontes concorrentes de verdade.

| Entidade | Campos/contrato essencial |
|---|---|
| lesson | lesson_id estável, UC/componente/ano, título, referências de cronograma e fontes |
| source + lesson_source | identidade/versionamento/hash, acesso real, papel, páginas/comentários/mídia; N:N com aulas |
| objective | alvo, resposta esperada, profundidade, classe de escopo, evidência, decisão de card |
| curriculum_relation | conceito relacionado, aula de origem/destino, taught/recap/prerequisite/future, estado confirmado/incerto |
| source_note/source_card | corpus/namespace, GUID ou fallback documentado, nid/cid do host, cloze/template, conteúdo/hash |
| neb_note/neb_card | chave NEBLI recuperável, origem, IDs locais, modelo/mídia, histórico adotado |
| objective_card | alvo, `cobertura_para_aprender` (frente/verso/guia), `recall_ativo` por cloze quando aplicável, seleção e grupo |
| priority | dimensão, valor, evidência, regra de derivação, decisão manual |
| search_run/candidate_decision | consultas, corpus/versão, candidatos, decisão e razão |
| calendar_event/override | datas/vínculos/origens, correção manual, efeito e vigência |
| run/operation | hash de inputs, estado, idempotency_key, antes/depois, erro, resultado desconhecido |
| artifact/publication | versão/hash, dependências, caminho, file_id/destino, estado e readback |

`source_nid` sozinho não é identidade global. Chave = corpus/namespace + identidade estável disponível; nid é localizador por instalação. Não supor que AnkiConnect expõe GUID; se necessário, obtê-lo por exportação consistente suportada. Não abrir/escrever diretamente o SQLite vivo do Anki.

Artefatos de aula propostos: `source-manifest.json`, `scope.json`, `candidate-decisions.jsonl`, `selection.json`, `coverage.json`, `study-guide.md`, E1, `change-plan.json`, `receipt.json`, `package-manifest.json`. Hashes invalidam dependências: mudou data, recalcular política; mudou fonte, revisar escopo/seleção/E1; mudou card compartilhado, revisar aulas/pacotes afetados.

Estados: `discovered → scoped → curated → audited → planned → applied → exported → published`. Suportar `partial`, `blocked` e operações `unknown` sem afirmar sucesso. A consulta de status não migra DB nem altera recibos. Planejamento não sobrescreve recibo de aplicação.

## 9. Aplicação e publicação seguras

Preflight confirma perfil/host, compatibilidade, snapshot recente e ausência de operação concorrente. Dry-run só lê sistemas externos. Escritas têm lock, diário, precondições e readback. Timeout de criação exige procurar identidade antes de repetir; múltiplas cópias encontradas são conflito, não autorização para escolher/apagar uma.

Atualizações de campos usam base planejada, estado atual e proposta; preservar comentários e edição manual. Rollback desfaz apenas operações atribuídas à execução, sem apagar revisões feitas depois. Não usar reset/forget/deleção em massa como atualização. Parear com AnkiSync existente, sem presumir que aplicar no Windows já instalou no Mac/Android.

APKG por aula/UC deriva das mesmas identidades canônicas; união por UC sem duplicar notas. Exportar via snapshot/perfil isolado suportado. Testar importação aula→UC→aula e o inverso. Não usar o pacote como rotina de atualização da coleção principal se isso fizer regressão de conteúdo/histórico; o registro/apply é a rota primária, APKG é entrega portátil.

**Limite que precisa de protótipo:** notas cloze compartilhadas podem gerar irmãos não selecionados ao exportar/importar. Nunca presumir que exportar a nota preserva uma seleção por card. Testar GUID, conteúdo, cartões gerados, suspensão e mídia numa importação limpa e numa coleção existente. Se o exportador não preservar a seleção exata, manter irmãos técnicos fora da seleção/ativos por manifesto reconciliado, explicitando a dependência de importador; não chamar esse pacote de APKG autossuficiente validado. Não resolver criando cópias diferentes da mesma nota por aula.

Publicação só em pasta pessoal explicitamente configurada; aula existente em pasta compartilhada não autoriza redistribuir AnKing. Upsert por file_id registrado e leitura de metadados/hash quando possível. Falha de upload retoma upload, não recria cards. Atualizar links na planilha somente nos campos de saída autorizados, sem alterar calendário-fonte.

## 10. Auditoria de qualidade e critério de pronto

Duas auditorias semânticas: fontes→escopo e escopo→cards. Mais uma de excesso: cards→justificativa de pertinência. Só esta combinação evita deck pequeno incompleto e deck enorme fora da aula.

Cobertura: todos os objetivos relevantes classificados em duas dimensões. Um verso explicativo pode fechar `cobertura_para_aprender`; `recall_ativo` exige uma frente/cloze/imagem realmente adequada. Nem todo alvo coberto para aprender exige recuperação própria. Nenhuma obrigação silenciosamente descartada por ser LY; uma menção solta no Extra não substitui explicação. Nenhuma evidência de imagem sem inspeção quando a imagem decide a resposta.

Qualidade: precisão, pergunta clara, alvo recuperável, carga razoável, sem pista indevida ou redundância injustificada. Uma boa pergunta pode ter mais de um cloze; volume não substitui verificação. Preservar a forma aprovada do AnKing.

Operação: mesmo input não duplica; outra aula acrescenta associação sem criar revisão; histórico e intervenções manuais preservados; mídia testada; resultado instalado e exportado conferidos. Datas e flags não alteram o conteúdo científico. Nenhuma mutação nos originais.

Avaliar resultado real pelos cards e pelas provas do usuário. Não pedir um teste adicional ao estudante para compensar falta de validação do software.

## 11. Fora da primeira versão

Tutor dentro do Anki; app/dashboard/site novo; importação massiva das UCs antigas; compartilhamento público; deduplicação destrutiva em massa; migração automática de todos os cards antigos; mapa exaustivo de toda medicina; compra de decks/assinaturas; API paga de IA; fusão automática de históricos/clozes; geração obrigatória de questões E2/E3. Todos podem ser avaliados depois sem bloquear um bom deck-aula.
