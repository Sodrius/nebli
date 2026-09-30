# Explicação do card com Tab (Anki)

Você está revisando no Anki, vira um card que errou ou não entendeu e aperta **Tab**. Aparece, logo abaixo do texto, um bloco de explicação com fonte de 21 px: do conceito básico até a resposta, e como isso se encaixa na aula. Tab ou qualquer outra tecla fecha. Se a tecla for de resposta, o card é respondido na mesma hora.

- **Uma explicação por card.** Irmãos de cloze da mesma nota têm explicações diferentes, cada uma focada no que aquele card esconde.
- **Nada muda nos seus cards.** As explicações ficam num arquivo do add-on, fora da coleção. Não sincronizam, não aparecem no editor e não mexem no agendamento.
- **Instantânea.** As explicações são geradas antes, em lote. O Tab só mostra.
- **Gerada pelo Claude da sua assinatura**, pelo Claude Code instalado no computador. Não usa API paga.

Funciona hoje no **Anki para computador** (Mac, Windows, Linux). No AnkiDroid/tablet ainda não: está planejado.

## Formato da explicação

Umas 8 linhas, em português:

> **Base:** o conceito básico de que a resposta depende.
> **Por quê:** a cadeia causal da base até a resposta, em poucos passos.
> **Na aula:** onde isso se encaixa na aula (o nome do deck).
> **Liga com:** algo que você **já estudou** em outro card (só aparece quando existe).
> **Não confundir:** só quando há uma confusão clássica.

Em card clínico, a explicação vai do fundamento (anatomia, fisiologia, micro, farmaco) até o achado ou efeito que o card cobra. Quando o card parece errado ou não oferece contexto suficiente, ele não é explicado: aparece "Card marcado para revisão", com o motivo.

## O que precisa ter

1. **Anki para computador** (testado no 26.9) com o add-on **AnkiConnect** (código `2055492159`, em Ferramentas → Complementos → Obter complementos).
2. **Python 3.9 ou mais novo** e este repositório baixado (`git clone`).
3. **Claude Code** instalado e com login feito **com a sua assinatura do Claude**: no terminal, `claude` deve abrir sem pedir chave de API. Se você tiver a variável `ANTHROPIC_API_KEY` configurada, o uso vai para a API paga; remova-a para usar a assinatura.

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

**Tempo e cota:** lotes de 10 cards, uns 20–30 s por lote. No teste, cada explicação gastou por volta de US$ 0,005 **equivalentes** da cota da assinatura. Não é cobrado; conta no limite de uso do seu plano. Algumas centenas de cards cabem tranquilamente num dia normal.

## Mudar o estilo

O estilo é o arquivo [`config/explicacao-tab.md`](config/explicacao-tab.md), escrito em linguagem comum: tamanho, ordem das linhas, ano do estudante, regras e exemplos. Edite, rode `gerar ... --refazer` nos cards que quiser e veja com Tab. Quando uma explicação ficar do jeito que você gosta, cole-a na seção "Exemplos aprovados" do arquivo: ela passa a servir de modelo para as próximas.

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
