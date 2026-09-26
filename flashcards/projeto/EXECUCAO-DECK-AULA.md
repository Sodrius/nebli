# Execução — E1 + cards
Runbook vigente, 25/09/2026. Ler contexto segundo README.md; critérios no CONTRATO-DE-QUALIDADE, feedbacks no registro único, cores em BANDEIRAS-E-PROGRESSAO. **Não executar scripts antigos de uma aula para reconstruir seu estado atual.**

## 1. Entrada e segurança
Nome/link/slide → localizar UC, componente, recorte, material, perfil Anki e pasta privada. Conferir fila (Codex só suas aulas). Resolver ambiguidade material; não repetir preferências fechadas.
Uma aula por vez, assim que o material cair no Drive, de preferência antes da aula; não acumular lote para a semana da prova. O tamanho vem da aula, não do tempo até a prova (F-C18).
Pedido de gerar autoriza fluxo; auditoria/planejamento sem correção são leitura externa. Não iniciar outra aula se pedido é só manutenção do projeto.
Criar pasta única `arquivos-trabalho/deck-aula-<slug>-<data>/`. Preflight --catalog vivo. Reconciliar comentários/vermelhos/pendências anteriores conservadoramente; não recriar apagados. Separar resolvido, retirado pelo usuário e ainda pendente.

## 2. Fontes e escopo
Manifesto das seis famílias do README, com localizador/hash quando disponível e acesso real. Buscar pastas relacionadas/roteiro, não somente PDF inicial. Biblioteca/canais no README; acervos no ACERVOS-REFERENCIA.
**Ler as provas pertinentes logo no começo, junto com o slide**, antes de montar o mapa: o que foi cobrado e em que profundidade. UC03 pelo índice local; outras UCs, pasta de provas no Drive antes de declarar ausência.
Mapa de objetivos teóricos e práticos com categorias: ensinado; retomado/cobrado; ponte curta; exemplo; pré-requisito; futuro; fora do recorte. Cada alvo aponta para o trecho da aula/prova; fato adjacente de Step/livro que a aula não trouxe sai (F-C15). Pontes exigem ligação direta e fonte, não “é importante na medicina”. Prova antiga sem confirmação atual não amplia recorte sozinha.
Slide regula assunto, não cada frase necessária à compreensão. Não completar toda a medicina explicativa de um exemplo. Ausência de fonte pode tornar resultado parcial; declarar impacto.

## 3. E1 e busca de candidatos
Rascunhar/revisar E1 conforme didatica/E1.md, usando os mesmos objetivos do deck. E1 existente boa pode ser reutilizada após conferência. Guia e vídeos não substituem E1.
Procurar primeiro cópia NEBLI viva da origem/pergunta. Uma identidade e histórico; registrar associação **por card/cloze**, não apenas nota.
Buscar amplamente AnKing por texto, sinônimos, estruturas, mecanismo, sistema, tags de recursos e vizinhança. Ler cada frente, resposta, verso e imagem. Modelo visual exige campos/rótulos/máscaras, não apenas Text.
Lacuna importante → reformular busca → consultar externos apropriados descobertos dinamicamente (incluindo AnatoKing/Dope/Dorian/BlueLink/Histology/LLU/MCAT, quando acessíveis). Ler candidatos recusados e motivo antes de concluir ausência. Não repetir pesquisa de downloads a cada aula; usar mapa e indicar aquisição útil quando necessário.

## 4. Seleção sem duplicação e autoria excepcional
Uma recuperação por informação, salvo ganho claro de habilidade/contexto/transferência. Comparar alvo+resposta+habilidade em **toda a seleção viva**, não só textos idênticos. Inversos e imagens variantes não são automaticamente bons nem automaticamente redundantes.
Verso pertinente conta para aprender; frente adicional só se recuperar ativamente agregar. Uma nota com três clozes custa três cards: avaliar irmãos individualmente. Cards compartilhados não contam como novos.
Autoral só cobre lacuna muito importante após buscas comprovadas. Registrar: objetivo → lacuna → duas rotas AnKing → externos consultados → candidatos inadequados → decisão. Alta autoria dispara nova auditoria de escopo/busca.
Autoral focal, inglês, cloze, aparência AnKing, curto (~8–18 palavras como referência, não mutilar contexto), Extra útil em 1–3 frases; imagem quando ensina. Não virar lista/dissertação ou definição sem contexto. Rever todos autorais e adaptações, não amostra.
Limpar clínica/recurso lateral na cópia, inclusive Clinical, Extra e campos Bootcamp/Sketchy/B&B/Additional Resources. Vídeo só guia/chat. Não apagar fontes/apoio científico relevante confundindo-os com link promocional.

## 5. Revisão de qualidade e bandeiras
Matriz objetivo → seção E1 → card/cloze/verso/identificação. Conferir cobertura, proporcionalidade, precisão científica, exemplos excluídos e reconhecimento prático.
Ler verso renderizado, inspecionar imagens. Procurar vazamento de resposta, cloze ambíguo, outro card que já recupera a mesma informação e feedback rejeitado reaparecendo. Origem real pelo ID no corpus, não tag declarada.
Aplicar critérios de BANDEIRAS-E-PROGRESSAO: verde recomendação durável, azul aprendizado de menor custo de esquecimento, branco só incerteza real. **A cor é decidida aqui, junto com a seleção, e gravada no plano com motivo curto por card**; sem bandeira só com a dúvida escrita. Não calcular cor pela tag HY. Média ~50 verdes/aula não é cota nem teto. Cor não corrige má seleção.

## 6. Plano e aplicação
`plan.json`: lesson_id, fontes/versões, nota/card de origem, objetivo, campos/mídia, clozes/templates selecionados, identidade NEBLI existente/nova, autoria e busca, recomendação/cor e motivo, ganho de pares mantidos, totais reais.
Dry-run: perfil/mídia corretos, fontes estáveis, templates condicionais, identidade sem colisão, conjunto de cards esperado. Snapshot e backup para alterações/exclusões. Aquisição exclusiva de ANKI-ESCRITA.lock **por `nebli.decks.escrita()`**, que também tira o total de cards dos nomes enquanto se escreve e sincroniza ao sair; deck e busca pelo nome canônico. Diário de operações e liberação só do próprio lock.
Cópias NEBLI independentes; originais/modelos/AnkiHub preservados, ankihub_id vazio no clone. Não mover compartilhado para fingir que pertence a dois decks. Não excluir nota inteira se irmão útil/associação/revisão depender dela sem resolver isso primeiro.
Criar ancestrais de decks e conferir árvore. Preset NEBLI para novos decks (`nebli_novos.py --alinhar`), sem mudar número de novos/agendador. Manter ativos; suspensão pessoal. Flags de feedback/pessoais prevalecem sobre cor proposta.
Após timeout, readback por identidade antes de repetir. **Instalar e sincronizar no mesmo dia** em que a seleção passa na revisão (F-C16); livro, figuras e ajustes finos atualizam as mesmas notas depois, declarando parcial. Não marcar pronto com fonte/precisão indispensável ainda pendente.

## 7. Verificar o que Davi realmente recebe
Contagem do plano vs coleção, notas/cards/clozes, origens, modelos, campos, mídia/legibilidade, ausência de rodapé meta e recursos laterais, flags previstas sem sobrescrever marcas pessoais, histórico/agendamento/originais preservados.
Provar seleção compartilhada por **conjunto exato de IDs**. Se só há tag ou busca no navegador, dizer; não anunciar botão de revisão por aula pronto. Não duplicar para contornar interface.
Salvar before, journal, receipt, verification e REVISAO-DE-QUALIDADE na mesma pasta. Sincronizar após escrita autorizada; distinguir resposta da API de chegada real aos aparelhos.
Falha técnica bloqueia aquela entrega; revisão semântica parcial não vira conteúdo aprovado por teste unitário.

## 8. E1, pacote e relatório
E1 rigorosa/didática (ou reutilização conferida) + guia breve com poucos vídeos pertinentes, bibliografia realmente usada e lacunas. Links no chat/guia; timestamps só verificados. PDF com revisão textual/visual, versão leve sem perda de legibilidade. Publicar na pasta privada existente quando autorizado.
APKG **UC inteira viva**, comprimido internamente, sem flags no arquivo, preservando coleção; PUBLICACAO-POR-UC.md. Upload APKG continua pausado; não publicar por inferência. Empacotador físico não garante união lógica de compartilhados de outra UC.
Relatório sucinto: onde aprender, cobertura/limites, E1, instalado/exportado/publicado/sync separados, notas/cards únicos, novos/reutilizados/compartilhados, origem, autorais, verdes/azuis/incertos/marcas pessoais/suspensos. Total por aula e união real da UC/lote; média dos verdes somente para calibrar.
Feedback generalizável vai a FEEDBACKS; estado fica MEMORY/fila; detalhes da execução na pasta da corrida. Não espalhar nova política em todas as memórias. Fechar por suficiência com precisão, não por alcançar número de cards.
