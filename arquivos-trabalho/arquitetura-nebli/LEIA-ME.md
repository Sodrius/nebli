# Arquitetura NEBLI — entrega v1

> **Histórico:** decisões refinadas após o piloto em [NEBLI Decks v2](../../flashcards/projeto/README.md). Usar a v2 para a calibração de escopo, prioridade AnKing, sinalização e implementação atual; este arquivo preserva a entrega anterior.

O projeto será um sistema pessoal de aprendizagem por aula: um comando gera E1, deck completo e recursos de estudo; um registro permanente evita duplicações e acompanha o que fica ativo ao longo da faculdade.

## Arquivos

1. [ARQUITETURA.md](ARQUITETURA.md): desenho funcional e técnico completo, incluindo escopo, curadoria, E1, identidades, calendário, carga, dispositivos, dados e distribuição.
2. [IMPLEMENTACAO.md](IMPLEMENTACAO.md): entregas A–H, contratos, testes, migração e texto pronto para iniciar o modelo executor.
3. [DESCOBERTAS.md](DESCOBERTAS.md): caminhos reais no Drive, estrutura da planilha, aula piloto, divergências e problemas observados no código atual.
4. [Decisões da conversa](../arquitetura-nebli-decisoes-2026-09-22.md): respostas 1–37 e rastreabilidade das escolhas.

## Decisões que sustentam o projeto

| Tema | Decisão |
| --- | --- |
| Entrega por aula | E1 sempre + deck + guia de onde estudar; E2/E3 fora |
| Conteúdo | Mapa de objetivos cruzando materiais, não dependência exclusiva da E1 |
| Seleção | Reutilizar NEBLI → AnKing → outros decks → autorais para lacunas |
| Tamanho | Cobertura completa do recorte, sem teto artificial; núcleo e reserva explícitos |
| Prioridades | Núcleo durável, complemento de prova e reserva |
| Identidade | Uma cópia NEBLI por origem; cada card pode pertencer a várias aulas |
| Revisão | 50 minutos para novos+revisões; esforço extra dirigido separado |
| Calendário | Mês vence datas; Matérias informa aulas e vínculos; atualizar ao executar comando |
| Infraestrutura | Codex na sessão + scripts locais; aplicação recomendada no Mac; estudo Android |
| Publicação | APKG por aula/UC, E1 e guia; saída pessoal em destino privado |
| Piloto | UC03, Patologia, conteúdo 38 — Inflamação aguda |

## Ajustes essenciais em relação às ideias iniciais

- Acervo completo não significa ativar tudo para revisão permanente.
- A lista de cards de uma aula não precisa ser uma segunda cópia física de cada pergunta.
- “Encontrou uma palavra no Extra” não prova que o card cobra o objetivo.
- Uma tag high yield não substitui classificação local, valor longitudinal e justificativa.
- Estatística de palavras, quantidade fixa de clozes e percentual de AnKing não são critérios principais de qualidade.
- Calendário e estado observado precisam ser persistentes: a memória da conversa não substitui o registro.
- O Windows atual não tem, por suposição, acesso ao Anki principal no Mac.

## Estado desta entrega

A especificação e o roteiro estão concluídos. Foram lidos o prompt, documentos/código do projeto, estrutura do Drive e células da planilha; referências técnicas do Anki e matriz oficial do Step 1 foram consultadas.

Nenhum deck foi criado nesta etapa; nenhuma regra de produção, coleção Anki ou planilha foi alterada. Os PDFs do piloto foram localizados, mas a leitura científica, seleção de cards e produção da E1 pertencem à implementação.

As pendências de implantação são concretas: inventariar a coleção no Mac, verificar versões/integrações e modelos, identificar bibliografia quando necessária e configurar destino privado. O roteiro explica em que etapa resolvê-las.

Começar pela Entrega A do roteiro, validar uma aula e só então expandir. A primeira prova do desenho é repetir a geração sem duplicar e reutilizar a mesma pergunta entre Patologia e Imunologia sem perder o histórico.
