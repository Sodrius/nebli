# Plano — NEBLI como um único add-on instalável

## Decisão

Entregar um único add-on `NEBLI` com módulos internos para atalhos, comentários, Tabs e organização dos decks. O usuário escolhe um de dois caminhos:

1. **Mais fácil:** Ferramentas → Add-ons → Obter Add-ons, colar um código numérico publicado no AnkiWeb e reiniciar.
2. **GitHub:** baixar `NEBLI.ankiaddon` da última Release, abrir o arquivo e reiniciar. Para desenvolvedores, clonar o repositório e rodar um instalador de um comando.

O código numérico só existe depois da publicação no AnkiWeb. GitHub sozinho não fornece um código compatível com “Obter Add-ons”.

## Arquitetura

- Um diretório de add-on com um único `__init__.py` mínimo e módulos `shortcuts`, `comments`, `tabs`, `decks` e `settings`.
- Um único `manifest.json`, com `package`, `name`, versões mínima/máxima do Anki e conflitos declarados com os add-ons NEBLI antigos.
- `config.json` contém apenas padrões versionados. Dados mutáveis ficam em `user_files/`, que o empacotamento oficial preserva e não deve sobrescrever.
- Migração idempotente na primeira abertura: importa configurações, log e `explicacoes.sqlite` dos add-ons antigos; cria backup; só então os desativa. Nunca move nem apaga o banco antes do readback.
- Tela única “NEBLI” em Ferramentas com diagnóstico, atalhos, zoom, caminho do banco de Tabs, exportação/importação e versão.
- Recursos que dependem do repositório local ficam opcionais. Revisão, comentários, zoom e leitura de Tabs funcionam sem clonar o NEBLI.

## Entrega com pouco trabalho

1. Criar `addon/nebli/` e migrar um módulo por vez, mantendo uma camada de compatibilidade com os três add-ons atuais.
2. Adicionar testes de carregamento sem Anki, conflitos de teclas, migração, persistência do zoom e preservação de `user_files`.
3. Gerar `dist/NEBLI.ankiaddon` por script reproduzível e publicar como artefato de GitHub Release.
4. Adicionar workflow do GitHub Actions: em cada tag `addon-v*`, testar, empacotar, calcular SHA-256 e anexar o `.ankiaddon` à Release.
5. Fazer piloto local com backup, reinício e readback; depois piloto em perfil limpo.
6. Publicar no AnkiWeb para obter o código numérico. Atualizações normais passam pelo gerenciador do Anki; GitHub Releases permanece como alternativa.

## Instalação proposta

- **AnkiWeb:** colar um único código e reiniciar.
- **GitHub, usuário comum:** baixar e abrir `NEBLI.ankiaddon`.
- **Git:** `git clone ...` e `./install-nebli-addon`; o instalador localiza `addons21`, faz backup do add-on anterior e copia/atualiza apenas o código, preservando `user_files`.

## Gates de publicação

- Instalação limpa e atualização sobre os add-ons atuais passam em macOS e Windows.
- Nenhuma coleção é aberta ou alterada durante instalação/migração.
- `explicacoes.sqlite`, comentários, configurações e zoom sobrevivem à atualização.
- Nenhum atalho duplicado; conflito produz aviso acionável.
- Desinstalar o add-on não apaga dados sem confirmação e backup.
- O pacote não contém banco pessoal, mídia de decks, logs, caminhos locais ou conteúdo licenciado.
- SHA-256 publicado e build reproduzível a partir da tag.

## Evidência pesquisada

- A documentação oficial define um diretório por add-on sob `addons21`, carregado por `__init__.py`, e o formato de compartilhamento/empacotamento do add-on.
- O fluxo de menor atrito do Anki é o código numérico do AnkiWeb; `.ankiaddon` é o caminho portátil para Releases do GitHub.
- Relatos da comunidade enfatizam que add-ons desktop não sincronizam entre dispositivos e que `user_files`/configuração precisam de estratégia própria; portanto o mega add-on não deve prometer instalação no AnkiDroid nem sincronização automática de dados locais.
- A busca direta no Reddit foi bloqueada pela política de rede nesta sessão; não tratei snippets de busca como evidência. Repetir a leitura dos tópicos pelo navegador antes da publicação pública.

## Ordem de implementação

1. Fechar comentários e gates do deck.
2. Entregar zoom e teste local após reinício.
3. Consolidar atalhos + comentários.
4. Migrar leitor/banco de Tabs.
5. Integrar organização de decks como módulo opcional.
6. Build, perfil limpo, Release e AnkiWeb.
