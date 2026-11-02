# Plano NEBLI no tablet, no celular e no controle (01/11/2026)

Pedido de Davi (01/11): "planeja como deixar tudo, desde os tabs até os comentários até uma forma de fazer o que faço no pc pelo tablet, pelo celular e pelo controlezinho de anki". Respostas: celular e tablet com **AnkiDroid**; no celular e no tablet, "tudo que der no mac, com usabilidade adaptada" (Tab, comentar, bandeiras e comandos, suspender e enterrar); no controle, "tudo menos comentar" (responder, suspender/enterrar, bandeira vermelha, desfazer); modelo do controle fica para depois.

## Diagnóstico

| Função no Mac | Onde mora hoje | Chega no AnkiDroid? |
|---|---|---|
| Bandeiras 1–4 | bandeira do cartão | sim (sincroniza) |
| Comandos q/w/e/r | tags `NEBLI::comando::*` | sim, mas sem atalho |
| Comentário (c) | campo `NEBLI_Comentario` | sim, pela tela de edição |
| Tab (explicação) | `explicacoes.sqlite` do add-on, local | **não** |
| X (gostei) | `tab-log.jsonl` local | **não** |
| Suspender com proteção (HY, verde em dois toques, Caps+9) | lógica do add-on | **não** (o suspender nativo não protege) |
| Histórico da bandeira anterior | `flag-history.jsonl` local | **não** |

Add-on de desktop não roda no AnkiDroid. Tudo que precisa chegar no celular tem de morar **no próprio card** (campo, tag, bandeira) e a lógica no **JavaScript do modelo do card**, que o AnkiDroid executa e liga a gestos, teclas e controle ("ações do usuário" `userJs1…9` e a API JavaScript do AnkiDroid).

## Tudo por gesto (Davi, 02/11: "quero tudo por gesto, especialmente o que mais uso")

Uso medido (últimos 30 dias / outubro): Bom ~7.500, Errei ~4.300, Fácil ~1.000, comentar ~770, suspender ~620, Tab ~440, X ~120, Difícil 50; bandeira vermelha e comandos, poucos. O mais usado ganha o gesto mais fácil; deslizar para cima/baixo fica livre porque o verso com figura precisa rolar.

| Ação | Gesto (verso) | Como |
|---|---|---|
| Mostrar resposta | toque em qualquer lugar | nativo |
| Bom | deslizar para a direita | nativo |
| Errei | deslizar para a esquerda | nativo |
| Fácil | toque no canto inferior direito | nativo |
| Difícil | toque no canto inferior esquerdo | nativo |
| Comentar | toque duplo | nativo "Editar nota" |
| Suspender (com proteção: HY não; verde pede repetir) | pressionar e segurar | ação do usuário 1 |
| Tab (explicação) | toque no canto superior direito | ação do usuário 2 |
| Desfazer | toque no canto superior esquerdo | nativo |
| Bandeira vermelha (liga/desliga) | toque no centro superior | nativo |
| X gostei | toque no centro direito | ação do usuário 3 |
| Enterrar | toque no centro esquerdo | nativo |
| Verde / azul / rosa | dois dedos: para cima / direita / esquerda | nativo |
| Comandos imagem / comentário / escrita / vários | três dedos, ou balançar + menu | ações do usuário 4–7 |

Gestos com dois e três dedos e balançar dependem da versão (F0 confere). Toda ação de gesto mostra um aviso curto na tela ("suspenso", "verde: repita para suspender"), para não ser acidental.

## Fases

**F0 — Conferir o que o AnkiDroid de Davi permite (1 sessão curta).** Pronto em 02/11: deck `NEBLI Teste gestos`, nota 1793630055890 (modelo `NEBLI Teste AnkiDroid`, `anki-addon/mobile/teste-gestos.html`), que lista sozinha as funções da API disponíveis. Um deck de teste com um card cujos botões chamam a API (`ankiToggleFlag`, `ankiSuspendCard`, `ankiBuryCard`, `ankiMarkCard`, e marcar tag, se a versão tiver). Davi toca os botões no tablet e no celular e diz o que funcionou; anotar a versão do AnkiDroid. Decide se os comandos q/w/e/r viram tag direto no celular ou precisam de alternativa.

**F1 — Tab dentro do card.** Campo novo `NEBLI_Tab` nos 6 modelos NEBLI (4.615 + 313 + 205 + 185 + 55 + 1 notas); o verso ganha o botão "Explicação" que abre e fecha o texto (no Mac, a tecla Tab faz o mesmo). Script copia o `explicacoes.sqlite` para o campo, com o aviso "o card mudou depois desta explicação" quando o hash não bate. **Depende do Codex**, que está gerando os Tabs: fazer depois que ele terminar, e o gerador passa a gravar no campo. **Mudar campo de modelo exige uma sincronização completa, uma vez**: sincronizar todos os aparelhos antes, depois um envio único do Mac. As 475 notas de etimologia usam o modelo do AnKing (compartilhado); ficam sem Tab ou migram para um modelo NEBLI.

**F2 — Barra NEBLI no verso (celular e tablet).** Um `_nebli.js` na mídia (sincroniza) incluído nos modelos, com botões grandes:
- bandeiras vermelha, verde, azul, rosa;
- comandos imagem, comentário, escrita, vários (tags);
- X gostei (vira tag `NEBLI::gostei`, também no Mac; os 80 X atuais migram);
- Explicação (Tab);
- suspender com a mesma proteção do Mac (HY não suspende; verde pede dois toques);
- enterrar.

Comentar: o AnkiDroid não deixa o card escrever no próprio campo, então o botão "Comentar" fica no gesto "Editar nota", que abre direto no campo de comentário. A rodada de comentários já lê esse campo.

**F3 — Gestos e teclas do AnkiDroid.** Tabela de configuração (Configurações › Controles) para o celular e o tablet, ligando gestos às ações nativas e às `userJs` da F2. Davi aplica uma vez em cada aparelho, com o passo a passo e as capturas de tela.

**F4 — Controle.** Quando Davi disser o modelo: mapear responder, suspender/enterrar (com proteção, via `userJs`), bandeira vermelha e desfazer nos botões dele.

**F5 — Mac na mesma lógica.** Os add-ons `nebli_atalhos` e `nebli_explicacoes` passam a usar os mesmos dados sincronizados (Tab no campo, gostei em tag, bandeira anterior em tag), para PC, tablet e celular mostrarem a mesma coisa. Gates: o gerador de Tab e a rodada de comentários leem e gravam só o que sincroniza.

## Riscos

- Sincronização completa uma vez (F1).
- Versão do AnkiDroid pode não ter alguma função da API (F0 decide).
- O suspender nativo do AnkiDroid continua sem proteção; a proteção só vale pelos botões e pelas `userJs`.
- Tab é trabalho do Codex: combinar a troca do sqlite pelo campo antes.
