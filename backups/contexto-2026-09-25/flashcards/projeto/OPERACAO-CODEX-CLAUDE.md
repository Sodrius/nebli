# Operação compartilhada — Codex e Claude

> **25/09:** ler [CALIBRACAO-2026-09-25.md](CALIBRACAO-2026-09-25.md) antes de operar. Azul (`4`) substitui rosa. Leia a fila para exceções: lote só deck/sem upload. Relatório atual: [AUDITORIA-2026-09-25.md](AUDITORIA-2026-09-25.md); números, estados e previsão de primeiro teste de 23/09 abaixo são históricos.

Revisão final de 24/09/2026. Fluxo assistido, sem API paga adicional obrigatória. A v4 governa conteúdo; PUBLICACAO-POR-UC governa a entrega. Não confundir especificação com automação concluída.

## Entrada e diagnóstico

Abrir na raiz NEBLI. Ler README → CALIBRACAO-ESCALA-V4 → CONTRATO-DE-QUALIDADE → este arquivo → EXECUCAO-DECK-AULA, ACERVOS-REFERENCIA e PUBLICACAO-POR-UC. Claude: `/deck-aula <link ou nome>`; Codex: pedido equivalente.

Anki aberto, perfil e acesso confirmados. A última vistoria respondeu perfil Davi; antes getActiveProfile não era suportado. Conferir em cada sessão, sem adivinhar ou reutilizar um caminho de outro computador.

```text
python -m nebli.preflight --catalog --output arquivos-trabalho/deck-aula-<slug>-<data>/catalogo.json
```

Somente leitura no Anki; grava JSON local sem sobrescrever recibo existente. Sem --catalog há amostra estrutural; com ele são mapeados modelos por corpus, subdecks e união de IDs. Nenhum desses modos aprova conteúdo/imagens. Se partial, ler errors e resolver o que impede escrita segura.

Reconciliar pendências pela coleção viva. Card apagado intencionalmente não deve ser restaurado para resolver comentário antigo. Não executar nebli/anki_apply.py como gerador universal: é legado com decisões específicas, atuação por nota e movimentação de cards.

## Acervos e busca

Usar [ACERVOS-REFERENCIA.md](ACERVOS-REFERENCIA.md): AnKing Step primeiro; MCAT e demais externos adequados antes de autoria. Descoberta dinâmica inclui filhos novos de Referências Externas, independentemente da pasta-pai.

Buscar por texto, sinônimos, tags de recursos (Ninja Nerd inclusive), sistemas e vizinhança semântica. Depois ler cada card/cloze/verso/imagem. Tags são portas de busca, não conjuntos automaticamente pertinentes. Em modelos visuais procurar Header/Title/rótulos/máscaras, não apenas Text.

Registrar buscas e recusas antes da autoria; segunda auditoria quando houver muita autoria. Preservar modelos/fontes originais. Autoral curto, focal, aparência AnKing e imagem quando ensina; inspecionar todo autoral e imagem adaptada.

## E1 e aprendizado

E1 explicativa sempre; reutilizar boa E1 conferida. Guia curto separado ou junto, nunca substituto. E2/E3 desligadas. Bibliografia distingue consultada, indicada e não acessada; não alegar leitura de capítulo a partir de figura no slide.

Vídeos no guia/chat, nunca nos cards. Verificar pertinência e canal/título; timestamp somente com evidência. O pacote Python typst estava disponível mesmo sem executável no PATH; testar o ambiente antes de declarar compilação impossível. Aplicar revisão visual do PDF.

O assunto deve progredir entre aulas: registrar o que já foi coberto e o que fica para depois. Não construir um currículo adicional dentro de cada deck nem prometer porcentagem de Step coberto por tags.

## Publicação por UC

Seguir [PUBLICACAO-POR-UC.md](PUBLICACAO-POR-UC.md):

```text
python -m nebli.package_uc --uc UC03 --output <pasta-da-execucao>/NEBLI-UC03.apkg
```

UC inteira viva, comprimida, sem bandeiras no arquivo; flags vivas preservadas. E1/guia por aula. Atualizar o mesmo file_id no Drive e registro local config/publicacoes-uc.json. Se ainda ausente, criar a partir do exemplo; nunca sobrescrever IDs existentes.

Codex: upload local/readback testados, inclusive arquivo de 26 MB. Claude: conexão Drive pela conta confirmada; descobrir as ferramentas da sessão e testar upload binário, não copiar nomes de ferramentas do Codex. Ainda falta validação de uma aula completa pelo Claude.

Pacotes históricos não são fonte para reconstruir UCs após a limpeza manual. O empacotador confere o conjunto físico. Se há card compartilhado fisicamente em outra UC, a união lógica exige operação isolada ainda não implementada no utilitário; não publicar um conjunto incompleto como completo, duplicar ou mover cards vivos para contornar.

## Primeiro teste e escala

Aula escolhida por Davi → fontes/recorte → buscas → revisão de qualidade → E1/guia → plano/backup → Anki → APKG/Drive → relatório. O normal é manter cards; candidatos pós-prova já rosas, decisão de suspensão pessoal. Não alterar 35 novos/50 min automaticamente.

Validar uma aula ponta a ponta, depois 2–3 da mesma UC. Amostra aprovada + uso real + tipos diferentes de aula + execução satisfatória pelo Claude são o aceite, não apenas ZIP/contagem corretos.

Q18/Q22 ainda requerem explicação da interface compartilhada, sem duplicar história. Q25 está simplificada (manter/rosa/decisão pessoal); Q26 depende de carga real. Guia da próxima sessão em [HANDOFF-CLAUDE.md](HANDOFF-CLAUDE.md).
