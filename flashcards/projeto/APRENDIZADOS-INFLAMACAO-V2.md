# Aprendizados práticos — revisão de Inflamação aguda

> Superado pela recalibração registrada em [CALIBRACAO-DECK-AULA-V3.md](CALIBRACAO-DECK-AULA-V3.md). Este documento preserva o histórico da expansão v2; não use suas contagens de núcleo, rodapés ou política de bandeiras para uma nova aula.

22/09/2026. Resultado aplicado ao perfil Davi acessível no Windows, aguardando avaliação do usuário. Não confundir instalação conferida com aprovação pedagógica pelo estudante.

## Resultado e próxima aula

- O deck passou de 31 notas / 45 cards para **80 notas / 116 cards**: 71 cards acrescentados, nenhum card antigo apagado, esquecido ou suspenso.
- Origem dos cards finais: **75 AnKing, 1 Histology, 33 complementos textuais NEBLI e 7 visuais com imagens da aula**. Os 33 complementos textuais vêm de 22 notas; os 7 visuais vêm de 6 notas. Contar notas e cards separadamente.
- Grupos: 110 núcleo durável, 2 detalhes locais de prova, 4 reserva. Grupos são rótulos; nenhuma suspensão automática foi aplicada.
- A maioria dos novos fatos recuperados do acervo veio do AnKing. Autoria ainda foi necessária para encadeamentos e distinções locais: não esconder esse número nem chamar todos os complementos de AnKing.
- Próxima aula: **UC08, Histologia; materiais no Drive. Só começar após aprovação deste deck de Patologia.** O tema exato ainda não foi escolhido; não inferir uma aula pela UC.
- Prioridade agora: calibrar um bom deck-aula, não iniciar geração em massa ou construir toda a infraestrutura antes de aprender com o piloto.

## O que funcionou e deve ser repetido

1. **Ler o que o professor diz para aprender e para não decorar.** Na p. 12 ele restringe os mediadores à tabela; na p. 13 pede COX/LOX, produtos principais e intervenções, sem decorar toda a cascata. Essa fala decide a profundidade melhor que o tamanho da tag AnKing.
2. **Mapear lacunas antes de importar mais cards.** O primeiro piloto tinha forte recrutamento e pouca morfologia/permeabilidade/resolução. Quantidade não era a medida de cobertura.
3. **AnKing-first com busca fora da primeira tag.** Exsudato/transudato estava em contexto pleural; erosão/úlcera em GI; AINEs e corticoides em farmacologia. Perguntas pertinentes podem estar fora da disciplina esperada.
4. **Busca por texto e por taxonomia são complementares.** A tag Pathoma trouxe mecanismo e doenças que não pertencem a esta aula. Termos como `stasis` trouxeram `metastasis`; resultado lexical não prova pertinência. Pontuação literal no termo (por exemplo, `acute.phase`) não substitui espaço numa busca Anki.
5. **AnKing é preferência, não garantia de formulação perfeita.** Foram corrigidos o comparador de LDH, a definição de abscesso, a generalização etiológica do abscesso e duas formulações mecanísticas, preservando o alvo dos cards existentes.
6. **Não importar irmãos fora do recorte.** A nota Histology selecionada gerava três clozes. Só c1 (MEC/colagenases) foi mantido como pergunta; os demais ficaram legíveis como contexto, sem gerar cards. A origem e a alteração estão registradas.
7. **Pergunta visual exige imagem sem resposta embutida.** Foram extraídas imagens nativas do PDF para úlcera, flegmão, abscesso, marginação e diapedese. Na figura comparativa do pulmão, renderizou-se somente a área ilustrada, sem a linha de legendas que entregava a resposta. A versão integral fica no apoio.
8. **Uma foto estática não prova movimento.** A imagem da p. 20 permite perguntar posição marginal dos leucócitos; não permite afirmar que o aluno observou o rolamento em movimento.
9. **Autoral deve fechar uma lacuna definida.** Os complementos não são uma reescrita estilística do AnKing. Cobrem, por exemplo, cadeia hemoconcentração→estase→marginação, temporalidade da permeabilidade, linfa, PAF e flegmão. A busca não provou inexistência universal: somente ausência de candidato adequado nas consultas documentadas e corpora acessíveis.
10. **Precisão vence erro de transcrição.** Não repetir inversão exsudato/transudato, chamar ICAM/VCAM de integrinas ou dizer que antibiótico nunca chega a nenhum abscesso. Manter o princípio cobrado, corrigindo o absoluto incorreto.
11. **Aplicar a auditoria também às próprias adições.** A revisão final percebeu que as fontes de PG/LT estavam só no apoio e que a figura vascular/celular não estava sendo perguntada. Foram acrescentados três cards, sem mudar o recorte ou preencher uma cota.

## Prioridades sem falsa precisão

- Rótulos aparecem no verso: Faculdade + Step + grupo de retenção; também há tags de busca.
- Tags AnKing originais foram preservadas: HY, HY relativo e HY provisório não viraram uma única certeza. Sem tag = não classificado, não LY.
- Resultado por card: 11 HY; 29 HY relativo; 17 HY provisório; 15 LY; 44 não classificados.
- Não inventar yield Step para os complementos locais. Faculdade alta pode coexistir com LY ou yield desconhecido.
- Bandeiras não foram alteradas: roxo ainda precisa de definição; vermelho já tem outro uso no projeto.
- Núcleo durável não significa estudar tudo hoje. Os 116 estão disponíveis, sem mudar limites diários ou agendador.

## Aprendizados operacionais comprovados

- **Inventário anterior envelhece.** Os seis IDs antigos de Patologia usados como exemplos na auditoria não existiam mais na coleção atual. Não foram restaurados nem copiados a partir de evidência desatualizada.
- Perfil identificado pelo diretório de mídia `Anki2/Davi`; API não dispõe de `getActiveProfile` nesta instalação. Não inventar suporte de método.
- Backup APKG com agendamento antes da aplicação; snapshots dos campos e agendamento; diário de operações e readback depois.
- Modelos novos clonados podem gerar cards no deck Padrão apesar do destino da requisição. Isso aconteceu e foi detectado. O corretivo só moveu cópias recém-criadas por esta execução e ainda sem revisões; nunca cards antigos/compartilhados.
- Reexecução após interrupção localizou a cópia criada pela tag e não a duplicou. Precondições pós-aplicação também passaram. Isso é evidência de retomada desta execução, não teste completo de todos os cenários do pipeline.
- As 31 notas existentes mantêm IDs e tipo de nota original. **Não houve migração arriscada de modelo.** Novas cópias usam modelos independentes; templates originais não foram alterados.
- Campos/tags das 52 notas de origem selecionadas, templates de origem, agendamento e bandeiras dos 45 cards anteriores foram conferidos e preservados.
- O APKG deve ser conferido contra o recibo final: IDs, campos, contagens e mídia, não apenas existência do arquivo. O resultado final dessa conferência fica em `revisao-v2/verification.json`; a amostra foi renderizada visualmente no navegador.
- Exportação **sem agendamento** é o artefato portátil. Não usá-la para substituir o fluxo normal de sincronização da coleção revisada. Mac/Android e importação em perfil limpo não foram testados.
- Publicação somente em pasta pessoal privada verificada; não copiar AnKing para a pasta compartilhada de materiais docentes.

## Limites que permanecem honestos

- Bibliografia declarada: Robbins & Cotran. O capítulo integral/edição do usuário continua não acessado; figuras do Robbins no slide não fecham essa revisão.
- Cobertura foi calibrada para os alvos da aula e cobranças pertinentes, não para cada frase, rótulo secundário de figura ou todo o capítulo.
- Nesta correção o foco foi o deck; não foram regeneradas E1/E2/E3, calendário ou limites diários. E1 legada permanece acessível, E2/E3 continuam suspensas.
- Ainda não é o comando único de produção validado para qualquer aula. Aprovação deste piloto vem antes da próxima UC.

## Evidências e artefatos

- [Deck publicado](https://drive.google.com/file/d/1oPVxY7nhrBG6D-X9u1HQi_8lnpI3CjIc/view?usp=drivesdk).
- [Pasta pessoal de entrega](https://drive.google.com/drive/folders/1JfJgEH9zEYxiDUkfff7RWvm3WJanN6H3).
- Plano, recibo, verificação, snapshots, pacote e prévia: `arquivos-trabalho/auditoria-inflamacao-aguda-2026-09-22/revisao-v2/`.
- Scripts desta rodada são específicos da aula; não executá-los para outra UC ou chamar o plano de arquitetura de implementação concluída.
