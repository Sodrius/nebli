# Ligar a curadoria AnKing — o que falta e como resolver

Estado hoje: o pipeline produz a aula inteira, mas **sem consultar o AnKing**. Não é um
problema de código — é uma credencial que falta. Este documento é a lista de passos.

## Por que estava travado

O índice está pronto e íntegro no Drive (`Anking/AnKing-index-v2`, 564 MB descompactado,
103 MB em duas partes). Os scripts de indexar e buscar existem há tempos
(`index_private_apkg.py`, `search_private_index.py`). O que faltava era o meio-termo: pôr o
arquivo dentro do container onde a aula é produzida.

A tentativa óbvia — o conector do Drive — não serve: ele devolve arquivo em **base64 dentro
do contexto do modelo**, e 103 MB não passam por ali de jeito nenhum.

## O que foi verificado neste ambiente

| Verificação | Resultado |
|---|---|
| `www.googleapis.com` alcançável pelo container | **sim** (`200`) |
| `https://www.googleapis.com/drive/v3/files/<id>?alt=media` | **sim** — responde `403 missing a valid API key`, ou seja, é o Google respondendo, não o proxy bloqueando |
| `https://oauth2.googleapis.com/token` alcançável | **sim** |
| Disco livre no container | ~29 GB — sobra para 103 MB + 564 MB |
| Credencial do Drive no ambiente | **não existe** ← único bloqueio |
| Assinatura RS256 de conta de serviço (chave PKCS#8) | **validada** com chave sintética; o Google processou o JWT |

Conclusão: o caminho de rede funciona ponta a ponta. Falta só a chave.

## O que você precisa fazer (~10 minutos, uma vez só)

Recomendo **conta de serviço**, não OAuth pessoal: não expira, não pede consentimento a cada
tanto, e enxerga só a pasta que você compartilhar — nada do resto do seu Drive.

1. Em <https://console.cloud.google.com>, crie um projeto (ou use um existente).
2. **APIs e serviços → Biblioteca → Google Drive API → Ativar.**
3. **APIs e serviços → Credenciais → Criar credenciais → Conta de serviço.**
   Nome à escolha, por exemplo `nebli-leitor`. Não precisa dar papel nenhum de IAM.
4. Na conta de serviço criada, aba **Chaves → Adicionar chave → Criar nova chave → JSON**.
   Baixa um arquivo `.json`. **Ele é um segredo** — não commite, não cole em chat.
5. Copie o `client_email` de dentro desse JSON (algo como
   `nebli-leitor@seu-projeto.iam.gserviceaccount.com`).
6. No Drive, na pasta **`Anking`**: Compartilhar → cole esse e-mail → permissão **Leitor**.
7. No Claude Code, guarde o JSON na variável `NEBLI_DRIVE_SA_JSON` do ambiente — o caminho
   exato está na seção seguinte, porque não é óbvio.

Pronto. Nada mais.

## Onde ficam as variáveis de ambiente

Não existe página de configurações nem URL direta para isso — é a razão pela qual ninguém
acha de primeira. O seletor de ambiente fica **dentro** da tela de sessões:

1. Abra <https://claude.ai/code>.
2. Na linha **acima da caixa de mensagem**, clique no ícone de nuvem que mostra o nome do
   ambiente atual (normalmente `Default`).
3. Passe o mouse sobre o ambiente na lista e clique na **engrenagem** que aparece à direita.
   (Ou **Add cloud environment**, para criar um novo.)
4. O diálogo tem quatro campos: nome, nível de acesso de rede, **Environment variables** e
   setup script.
5. Em Environment variables, formato `.env`, uma linha por variável. O JSON da conta de
   serviço ocupa várias linhas, então envolva em **aspas simples**:

   ```
   NEBLI_DRIVE_SA_JSON='{ ...conteúdo inteiro do arquivo .json... }'
   ```

   O leitor também aceita o JSON numa linha só, em base64, ou o caminho de um arquivo — o
   que for mais fácil de colar.

**As variáveis são copiadas no início da sessão.** Sessão que já está rodando não relê a
configuração: depois de salvar, é preciso **abrir uma sessão nova** para a credencial existir.

### O aviso que a documentação faz, e por que seguimos assim

A documentação diz que o ambiente **não tem cofre de segredos** e que quem usa o ambiente
consegue ler os valores — por isso recomenda não pôr credenciais ali, e completa: "se uma
sessão precisar de uma credencial mesmo assim, adicione com essa visibilidade em mente."

No nosso caso a conta é aceitável, e é por isso:

- o ambiente é **pessoal**, não compartilhado com organização — "quem usa o ambiente" é o Davi;
- a credencial é **somente leitura** e enxerga **uma pasta só** do Drive, nada mais;
- é revogável em um clique: apagar a chave em Contas de serviço → Chaves invalida na hora.

O que **não** se deve fazer é usar a chave pessoal do Google ou um token de escopo amplo.

### Alternativa, se preferir não criar conta de serviço

Use um cliente OAuth "Desktop" e faça o consentimento uma vez na sua máquina, guardando três
segredos: `NEBLI_DRIVE_CLIENT_ID`, `NEBLI_DRIVE_CLIENT_SECRET`, `NEBLI_DRIVE_REFRESH_TOKEN`.
Funciona igual, mas se o app ficar em modo "Teste" no console, o refresh token **expira em 7
dias** e você refaz o consentimento. Por isso a conta de serviço é melhor.

## Como conferir que ficou de pé

```bash
python flashcards/scripts/fetch_private_index.py --check
```

- `"status": "no_credential"` → a variável não chegou ao ambiente.
- `"status": "download_required"` → credencial OK e a pasta foi encontrada; falta só baixar.
- `"status": "already_current"` → índice presente e com o hash do manifesto.

Se der `403` ou "pasta não encontrada", quase sempre é o passo 6: a pasta `Anking` não foi
compartilhada com o `client_email` da conta de serviço.

## O que passa a acontecer sozinho

Com a credencial no lugar, o passo 4 do `/resumo` deixa de ser bloqueado:

```bash
python flashcards/scripts/fetch_private_index.py          # ~103 MB, uma vez por container
python flashcards/scripts/search_private_index.py \
    flashcards/private-cache/anking-index-v2.private.sqlite \
    "anal canal" "pectinate line" "linha pectinada" "taeniae coli" --limit-per-query 30
```

A busca devolve GUID, note type, tags e texto dos candidatos. A sessão então roteia cada
conceito em `AnKing → externo → autoral` de verdade, e só os cards sem candidato real ficam
autorais — que é o que o canon sempre pediu.

Para acelerar o começo de sessão, vale pôr o `fetch_private_index.py` no **script de setup do
ambiente**: aí o índice já está em disco quando a aula começa.

## Sobre a mídia

O índice guarda só os **nomes** dos arquivos de mídia, não os bytes. Quando um card copiado
do AnKing trouxer imagem, a mídia vem depois, pelos shards
(`media-shards-manifest.json` mapeia arquivo → shard), baixando apenas os shards dos GUIDs
escolhidos. O mesmo `fetch_private_index.py` serve de base para isso.

## Uma opção que existe e eu não usei

O container já tem `GH_TOKEN`, e o GitHub é alcançável — daria para hospedar o índice como
asset de release privada e dispensar credencial nova. **Não fiz** porque o canon é explícito
(`CLAUDE.md`, `ERROS.md` §19): AnKing e decks externos nunca entram no GitHub. Se você quiser
abrir exceção para um índice derivado, só de texto, em repositório privado, é decisão sua —
mas hoje seria violar a regra escrita.
