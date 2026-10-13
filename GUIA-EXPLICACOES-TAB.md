# Explicação do card com Tab (Anki)

Você está revisando no Anki, vira um card que errou ou não entendeu e aperta **Tab**. Aparece, num balão flutuante na parte de baixo da tela, por cima do card, a explicação com fonte de 21 px: do conceito básico até a resposta, e como isso se encaixa na aula. **Tab novamente, enquanto o balão está aberto, marca essa explicação como ruim e fecha.** Outra tecla apenas fecha; se for tecla de resposta, o card é respondido na mesma hora. A reprovação fica no `tab-log.jsonl` com o ID do card e uma assinatura da versão da explicação, para revisão posterior.

- **Uma explicação por card.** Irmãos de cloze da mesma nota têm explicações diferentes, cada uma focada no que aquele card esconde.
- **Nada muda nos seus cards.** As explicações ficam num arquivo do add-on, fora da coleção. Não sincronizam, não aparecem no editor e não mexem no agendamento.
- **Instantânea.** As explicações são geradas antes, em lote. O Tab só mostra.
- **Gerada pela assinatura do Claude ou, com `--backend codex`, pela assinatura do Codex CLI.** Não usa API paga.

Funciona hoje no **Anki para computador** (Mac, Windows, Linux). No AnkiDroid/tablet ainda não: está planejado.

## Formato da explicação

**Padrão ativo desde 12/10:** quatro blocos presentes e úteis, na ordem **Básico → Explicação → Na aula → Não confundir**. O primeiro define o que faltou para entender a pergunta; o segundo constrói a resposta por mecanismo ou relação; o terceiro mostra a função daquela ideia na aula; o quarto distingue uma alternativa realmente confundível. [Três exemplos editoriais](../Documents/NEBLI-investigacao-2026-10-11/GUIA.md). O gerador aplica o estilo novo à aula que está sendo produzida e seus cards compartilhados. Os Tabs antigos continuam visíveis; o resumo os chama de desatualizados até a atualização por aula. Não há regeneração geral automática.

Formato das explicações anteriores, em português (legado que permanece visível até a atualização daquela aula):

> **Base:** o conceito básico de que a resposta depende.
> **Por quê:** a cadeia causal da base até a resposta, em poucos passos.
> **Na aula:** onde isso se encaixa na aula (o nome do deck).
> **Liga com:** algo que você **já estudou** em outro card (só aparece quando existe).
> **Não confundir:** só quando há uma confusão clássica.

Em card clínico, a explicação vai do fundamento (anatomia, fisiologia, micro, farmaco) até o achado ou efeito que o card cobra. Quando o card parece errado ou não oferece contexto suficiente, ele não é explicado: aparece "Card marcado para revisão", com o motivo.

## O que precisa ter

1. **Anki para computador** (testado no 26.9) com o add-on **AnkiConnect** (código `2055492159`, em Ferramentas → Complementos → Obter complementos).
2. **Python 3.9 ou mais novo** e este repositório baixado (`git clone`).
3. **Claude Code** instalado e com login feito **com a sua assinatura do Claude**: no terminal, `claude` deve abrir sem pedir chave de API. Se a variável `ANTHROPIC_API_KEY` estiver configurada, o gerador interrompe a execução para evitar uso de API paga; remova-a para usar a assinatura.

## Instalar (uma vez)

Com o Anki aberto, no terminal, dentro da pasta do repositório:

```bash
python3 -m nebli.explicacoes instalar
```

Depois feche e abra o Anki. Esse comando instala **só** o add-on do Tab (`nebli_explicacoes`), que não mexe em nenhuma outra tecla.

> O `python3 -m nebli.decks instalar-addon` instala também os add-ons pessoais do dono do repositório: troca as teclas de resposta para a/s/d/f, as bandeiras para q/w/e/r e põe o total de cards no nome dos decks NEBLI. Use-o só se quiser esse jeito de estudar.

## Gerar as explicações

Com o Anki aberto, escolha os cards por uma **busca do Anki**, a mesma sintaxe da barra do navegador:

```bash
# todos os cards de um deck (o * no fim pega também os subdecks)
python3 -m nebli.explicacoes gerar 'deck:"Minha UC::Microbiologia*"'

# NEBLI: use a tag da aula (os nomes de deck do NEBLI levam o total, ex. "UC03 (992)",
# e deck:"NEBLI::UC03::..." exato não acha nada)
python3 -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc03-imunologia-31-sistema-complemento"'

# só os que você errou hoje (bom para começar)
python3 -m nebli.explicacoes gerar 'deck:*Microbiologia* rated:1:1'

# ver o que seria enviado, sem gerar nada
python3 -m nebli.explicacoes gerar 'deck:*Microbiologia*' --simular

# testar com poucos cards
python3 -m nebli.explicacoes gerar 'deck:*Microbiologia*' --limite 20
```

Cards com explicação do conteúdo e do estilo atuais são pulados. Cards editados ou com explicação em estilo antigo são atualizados. `--refazer` força a geração mesmo dos atuais.

Outros comandos:

```bash
python3 -m nebli.explicacoes resumo              # quantas existem, quantas no estilo antigo
python3 -m nebli.explicacoes resumo 'deck:*Microbiologia*'   # cobertura exata: atual / faltando / desatualizada
python3 -m nebli.explicacoes mostrar 1790248163066   # ler a explicação de um card (id do card)
```

**Tempo e cota:** lotes de 10 cards; o tempo de preparação e geração varia. No teste inicial, cada explicação consumiu por volta de US$ 0,005 **equivalentes** da cota da assinatura. Isso não é cobrança de API. Lotes grandes podem atingir o limite do plano. Quando a cota liberar, repita o mesmo comando sem `--refazer`: as explicações atuais já salvas são preservadas.

O comportamento padrão tenta a assinatura do Claude e, se ela atingir o limite, passa para o Codex CLI autenticado sem perder o lote. Para escolher diretamente, use `--backend claude` ou `--backend codex`. O comando preserva as explicações atuais e usa o mesmo estilo e as mesmas checagens. Com `OPENAI_API_KEY` definida, o Codex para antes de gerar para evitar uma API paga.

## Mudar o estilo

O estilo ativo é o arquivo [`config/explicacao-tab.md`](config/explicacao-tab.md); a versão anterior foi preservada em `arquivo/2026-10-12-tab-estilo-legado.md`. O próximo `gerar '"tag:NEBLI::<aula>"'` atualiza só os cards daquela aula, inclusive compartilhados. `python3 -m nebli.explicacoes ruins` mostra os Tabs reprovados pelo segundo toque de Tab que ainda não foram reescritos. Ler o texto e a fonte ao corrigi-los; uma alteração automática de palavras não resolve necessariamente a dúvida.

## Onde ficam as coisas

| O quê | Onde |
|---|---|
| Add-on | `anki-addon/nebli_explicacoes/` (instalado em `Anki2/addons21/nebli_explicacoes/`) |
| Explicações geradas | `Anki2/addons21/nebli_explicacoes/user_files/explicacoes.sqlite` |
| Registro de cada Tab | `.../user_files/tab-log.jsonl` (mostra os cards que mais pegam) |
| Gerador | `nebli/explicacoes.py` |
| Estilo | `config/explicacao-tab.md` |

A pasta `Anki2` fica em `~/Library/Application Support/Anki2` (Mac), `%APPDATA%\Anki2` (Windows) ou `~/.local/share/Anki2` (Linux).

## Problemas comuns

- **Tab não faz nada:** ele só funciona no **verso** do card. Confira se o Anki foi reiniciado depois de instalar e veja `user_files/log.txt` do add-on.
- **"Ainda sem explicação para este card":** esse card ainda não foi gerado. Rode `gerar` com uma busca que o inclua.
- **"O card mudou depois desta explicação":** o card foi editado. `gerar '<busca>' --refazer` atualiza.
- **Erro ao gerar:** confira se o Anki está aberto com o AnkiConnect e se `claude` funciona no terminal.
- **Outro add-on usa Tab na revisão:** os dois vão disputar a tecla. Desative um deles.

## Limites atuais

- Só no Anki para computador. A versão para tablet (AnkiDroid) usará uma função nos modelos dos cards, chamada pela "Ação do usuário". Está planejada, ainda não existe.
- As explicações **não acompanham o APKG nem o AnkiWeb** nesta etapa. Outro computador precisa do add-on e da base `explicacoes.sqlite` (copiada com o Anki/gerador fechados, ou por backup SQLite), além de IDs de cards correspondentes. Uma importação pode mudar IDs; portanto copiar a base não garante que as explicações apareçam. Se isso acontecer, gere novamente no destino. Exportar não remove as explicações do computador de origem.
- A IA pode errar. Ela parte do conteúdo do card e é instruída a não inventar, mas trate a explicação como apoio: se algo não bater com a aula, confie na aula e ajuste o card ou o estilo.

## Decisão vigente em 08/10/2026

Manter **uma explicação por card**, com a interação atual. Davi cancelou variantes curta/longa; não implementar duas colunas ou migrar cache por essa proposta. Revisar fundamentos, cadeia causal, termos definidos e contexto da aula, sem apoio genérico. Conferir atualidade do Tab após alterar cards.

Proposta antiga integral em [arquivo](arquivo/2026-10-08-organizacao/GUIA-EXPLICACOES-TAB.md). Prompt, cache e add-on não foram alterados nesta organização. Limites técnicos acima continuam sujeitos à verificação na execução.
