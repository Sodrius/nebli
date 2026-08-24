# Infra remota — deck sempre-on, controle pelo celular, emails do monitor

Objetivo do Davi: mexer no deck **sem o Anki aberto**, controlar o Claude Code **pelo celular** de fora de casa, e receber os **emails do monitor** todo dia.

> **Atualização 2026-08-24 — a premissa mudou.** Este documento nascia de uma restrição que parecia dura: "o AnkiConnect exige uma instância Anki rodando, agentes na nuvem não alcançam o `localhost` do PC, logo a nuvem não serve". A primeira metade continua verdadeira — a nuvem realmente não alcança o seu PC. A conclusão, não: o caminho não é a nuvem chegar ao AnkiConnect, é **a nuvem ter a própria coleção**, sincronizada pelo AnkiWeb. Ver § 0. As três peças abaixo seguem válidas para o que roda no PC.

## 0. Caminho da nuvem — coleção via AnkiWeb (§ novo, 2026-08-24)

Uma sessão do Claude Code na nuvem (tablet, celular, web) opera a coleção **diretamente**, com o PC desligado: baixa a coleção do AnkiWeb pela lib oficial `anki`, faz curadoria AnKing e deck injection, e devolve as mudanças no sync. Três peças em `flashcards/scripts/`:

| Peça | Papel |
|---|---|
| `anki_collection_backend.py` | Opera a coleção pela lib `anki` + sync AnkiWeb. Mesma superfície do AnkiConnect (36 ações). |
| `ankiconnect_local.py` | Sobe um **AnkiConnect emulado** em `127.0.0.1:8765` sobre esse backend. É o que faz os ~31 scripts com `urllib` próprio funcionarem sem edição. |
| `nebli_anki.py` | O helper `call()` de sempre (era `anki.py`), agora com dois transportes e escolha automática. |

```bash
pip install anki                                    # 1x por sessão na nuvem
python flashcards/scripts/ankiconnect_local.py &    # a porta 8765 passa a existir
# daqui em diante todo script do NEBLI roda como se o Anki estivesse aberto
python flashcards/scripts/testar_backend_anki.py    # 38 checagens, coleção descartável
```

**Credencial (env var do environment, nunca no git):** `ANKIWEB_HKEY` — token de sync, não a senha, revogável trocando a senha do AnkiWeb. Alternativa `ANKIWEB_USER`/`ANKIWEB_PASS`: o primeiro login imprime o hkey para guardar, e a senha não é mais necessária. Mesma mecânica de `NEBLI_DRIVE_SA_JSON` — configurada uma vez, vale para todas as sessões futuras.

**Regra de segurança dura:** um sync que exigiria `FULL_UPLOAD` ou `FULL_SYNC` **aborta com mensagem explicativa**. A sessão na nuvem nunca decide sozinha qual lado da coleção sobrevive. `FULL_DOWNLOAD` só é aceito quando a coleção local está vazia (servidor → cliente, seguro). Antes de operar pela nuvem: sincronize o PC/celular, e não revise em outro lugar enquanto a sessão trabalha.

**Mídia:** o sync é sem mídia por padrão (rápido). Image Occlusion e `.apkg` com figuras exigem `NEBLI_ANKI_SYNC_MEDIA=1` — pesado, e o `exportPackage` avisa quando exporta sem mídia.

**Ganho lateral:** o `guid` das notas, que o AnkiConnect **não** expõe no `notesInfo`, aparece aqui. O casamento card-a-card do apply deixa de depender do texto bruto do campo 1 (`raw0`) e vira identidade exata — some a perda de 1–2 cards quando o AnKing atualiza um texto.

Outras variáveis: `NEBLI_ANKI_DIR` (onde mora a coleção, default `~/.nebli-anki`), `NEBLI_ANKI_BACKEND` (`connect|collection|auto`), `NEBLI_ANKI_AUTOSYNC=0`, `NEBLI_ANKI_OFFLINE=1` (testes, sem rede).

---

As três peças abaixo continuam sendo o caminho do **PC** — pode ligar uma de cada vez.

## 1. Anki headless em Docker (o "sem Anki aberto")
Roda o Anki como serviço permanente, sem janela, com AnkiConnect na 8765 e sync com o AnkiWeb (o celular vê as mudanças pelo app AnkiDroid/AnkiMobile).

Pré-requisito: **Docker Desktop** instalado. Imagem sugerida: [`ankimcp/headless-anki`](https://github.com/ankimcp/headless-anki) (Anki + AnkiConnect + VNC).

```bash
# 1) subir o container (ajuste o volume pro perfil do Davi e a versão da imagem):
docker run -d --name anki-nebli --restart unless-stopped \
  -p 8765:8765 -p 5900:5900 \
  -v anki_data:/root/.local/share/Anki2 \
  ankimcp/headless-anki:latest

# 2) na 1a vez, entrar por VNC (localhost:5900) e logar no AnkiWeb (sync).
# 3) conferir que responde:
curl http://localhost:8765   # deve dizer "AnkiConnect v.6"
```

Depois disso, `zerar_deck_anking.py`, `aplicar_curadoria_anking.py`, `revisao_diaria_anking.py` e `monitor_email_anking.py` falam com esse container — sem abrir o Anki na tela. O `--restart unless-stopped` faz voltar sozinho no boot.

> Config do AnkiConnect: manter `webBindAddress=127.0.0.1` (só o PC acessa). Sync AnkiWeb bidirecional mantém o celular do Davi espelhado. Antes de operações grandes, o container deve sincronizar (`sync` via AnkiConnect) pra não divergir do celular.

## 2. Controle pelo celular — `claude remote-control`
A sessão do Claude Code roda no PC (acesso total a arquivos locais + AnkiConnect); o celular vira uma janela. Não é a versão web (essa é sandbox na nuvem e não fala com o localhost).

```bash
# no PC sempre ligado, dentro de C:\AI use\nebli :
claude remote-control --name "NEBLI"
# abre uma URL + QR; escaneie no celular ou abra a URL no navegador do celular.
```

O PC precisa estar **ligado e com o processo rodando**. Para sobreviver a logoff/reboot, rodar como tarefa no logon (ver §3, mesma ideia). Docs oficiais: Remote Control (code.claude.com/docs/en/remote-control).

## 3. Emails do monitor — Windows Task Scheduler (local)
As duas tarefas rodam no PC (alcançam o Docker/AnkiConnect). **A explicação de IA usa a assinatura do Claude Code (`claude -p`), não a API paga** — então o único segredo obrigatório é a App Password do Gmail:

```powershell
# App Password do Gmail (gere em myaccount.google.com > Segurança > Senhas de app):
setx GMAIL_USER "dpbdes@gmail.com"
setx GMAIL_APP_PASSWORD "xxxxxxxxxxxxxxxx"
# ANTHROPIC_API_KEY é OPCIONAL — só se um dia quiser o cérebro "api" (metered).
```

### Quem redige a explicação (`--cerebro`)
O `monitor_email_anking.py` tem um seletor de cérebro (env `NEBLI_MONITOR_CEREBRO`, default `claude`):

| `--cerebro` | Quem explica | Precisa de | Serve pra tarefa agendada? |
|---|---|---|---|
| `claude` (padrão) | `claude -p` (assinatura Claude Code) | nada além do login do Claude Code | **sim** — explicação + agendada + sem API |
| `colar` | você mesmo, colando no Gemini | nada | sim (email traz bloco pronto pra colar) |
| `api` | API Anthropic (metered) | `ANTHROPIC_API_KEY` | sim |
| `nenhum` | ninguém (cards crus) | nada | sim |

Se o `claude -p` falhar na hora (sem rede, CLI deslogado), o email **cai automaticamente no bloco colável** — nunca fica sem sair. O `claude` precisa estar no PATH da tarefa; se não estiver, aponte `NEBLI_CLAUDE_BIN` pro caminho do executável.

Registrar as tarefas (bandeira 21h; diária 21h; semanal domingo 21h):

```powershell
schtasks /create /tn "NEBLI-monitor-bandeira" /sc daily /st 21:00 /tr ^
  "python \"C:\AI use\nebli\referencias-externas\monitor_email_anking.py\" --bandeira"

schtasks /create /tn "NEBLI-monitor-diario" /sc daily /st 21:05 /tr ^
  "python \"C:\AI use\nebli\referencias-externas\monitor_email_anking.py\" --diario"

schtasks /create /tn "NEBLI-monitor-semanal" /sc weekly /d SUN /st 21:10 /tr ^
  "python \"C:\AI use\nebli\referencias-externas\monitor_email_anking.py\" --semanal"
```

Teste antes sem enviar:
```bash
python flashcards/scripts/monitor_email_anking.py --bandeira --dry-run
python flashcards/scripts/monitor_email_anking.py --diario --dry-run
```

> **Roda de bandeira vermelha (21h, `--bandeira`):** durante o dia o Davi marca com **bandeira vermelha (flag:1)** os cards que quer entender a fundo; às 21h a roda explica cada um em voz NEBLI, entrega por email **+ registro HTML local** (`arquivos-trabalho/bandeira-<data>.html`, sempre gravado — vale como entrega se o email falhar), e no fim **tira a bandeira** (reset), pra ele re-marcar no dia seguinte. Query: `tag:NEBLI::* -tag:NEBLI::zerado::* flag:1`, top 14. O reset usa `setSpecificValueOfCard(keys=["flags"], newValues=[0])` — **valor inteiro `0`, não string** (com string o AnkiConnect faz no-op silencioso; verificado 2026-07-04); `setFlag` não existe nesta versão. Se a escrita de flag falhar, cai pro fallback de tag `NEBLI::explicado::<data>` e o Davi tira a bandeira na mão. `--dry-run` grava o HTML e **não** remove a bandeira.

> Seleção de cards (medição): **diário** = cards com nota Again hoje (`rated:1:1`) nos blocos `NEBLI::`, top 8 por nº de lapsos. **Semanal** = leeches / `lapses>=3`, top 10. Ambos ignoram `NEBLI::zerado::*`. A explicação sai em voz NEBLI (causa→mecanismo→consequência) — por padrão via `claude -p` (assinatura, sem API). Só o cérebro `api` usa o modelo `claude-sonnet-4-6` (`NEBLI_MONITOR_MODEL`).

> **Formato do email (2026-07-04):** nos cérebros `claude`/`api`, o email é **HTML com identidade NEBLI** (faixa navy, card-box creme, resposta âmbar, caixa gold "Vale estudar mais") + fallback texto puro (multipart). Agrupa por tema (`NEBLI::<slug>`), mostra contagem total + por tema, e a explicação de cada card. Quando um tema concentra muitos erros (≥3 no diário, ≥2 no semanal — `DICA_MIN_*`), inclui a caixa "Vale estudar mais" com **Revê** (conceito base) + **Aprofunda um tiquinho** (nuance, hint do `blueprint-step1.md`). Título acentuado vem do manifesto `flashcards/curadoria/<slug>.md`. Uma só chamada ao cérebro devolve JSON `{cards, dicas}`; se o JSON falhar, degrada pro bloco colável (email nunca deixa de sair). `--dry-run` grava `arquivos-trabalho/preview-email-<modo>.html` pra abrir no navegador. Cérebros `colar`/`nenhum` seguem em texto simples.

## Ordem de ativação sugerida
1. Docker headless (deixa o deck sempre acessível).
2. App Password do Gmail + as duas tarefas do Task Scheduler (liga os emails; a explicação usa `claude -p`, sem API).
3. `remote-control` quando quiser dirigir o PC pelo celular.

Nada aqui envia email ou dessuspende sozinho até o Davi criar a App Password e as tarefas.
