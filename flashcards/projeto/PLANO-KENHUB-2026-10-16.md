# Plano — decks a partir do Kenhub (16/10/2026)

Pedido (F-20261016-CLAUDE-10): um deck por módulo de estudo do Kenhub, com todas as estruturas, imagens dos testes/revisões
(limpas, uma estrutura marcada), oclusão + cloze; automatizado e reaproveitável para anatomia e fisiologia do ano que vem.
O deck de referência do Machado (443 notas básicas) foi descartado por Davi (“achei ruim”).

## 0. Limites (não mudam)

- **Uso pessoal.** Os termos do Kenhub (§11) proíbem reproduzir e distribuir; o próprio site permite baixar imagens para uso
  pessoal. Logo: imagens Kenhub só na coleção de Davi. Nunca no git, no pacote compartilhável da UC (`nebli.package_uc`
  passará a excluir a tag `NEBLI::fonte::kenhub` — a fazer antes do piloto), nem no AnkiHub. A mídia fica em `~/NEBLI-privado/kenhub/` (fora do repo).
- **Conta e sessão são de Davi.** Ele faz o login uma vez numa janela do navegador automatizado; a sessão fica num perfil
  local. Senha e cookies nunca vão para arquivo do repo, mensagem ou registro.
- **Ritmo humano.** Uma página por vez, com pausas, só os módulos pedidos; nada de baixar o catálogo inteiro. Se o Kenhub
  bloquear ou pedir captcha, parar e avisar.
- Cards seguem as regras de sempre (MEMORY §§5–8): AnKing/BlueLink primeiro onde já cobrem; cores; sem Tab na criação.

## 1. A ideia do vídeo (Fireship, “Every app on Earth is now open source…”)

O vídeo mostra um agente reconstruindo apps observando como funcionam por fora. Aplicado aqui: em vez de copiar tela por
tela, observar o que o site do Kenhub carrega quando Davi abre um quiz (as chamadas de rede que trazem a pergunta, a imagem
e a resposta). Se existir uma chamada estruturada (lista de perguntas com imagem + nome da estrutura), o robô a repete com a
sessão de Davi e obtém o módulo inteiro de forma limpa; se não existir, o robô lê a tela (imagem + resposta certa após
responder).

## 2. Ferramenta

Hoje não há navegador automatizável aqui: sem Chrome instalado, sem Node (o servidor Playwright do Claude Code falha com
`npx` ausente), sem Playwright para Python. Caminho proposto (baixo atrito):

1. `pip install playwright` no Python do NEBLI + `playwright install chromium` (navegador próprio, isolado).
2. `nebli/kenhub/login.py`: abre o Chromium **com janela visível** num perfil em `~/NEBLI-privado/kenhub/perfil`;
   Davi entra na conta; fecha. A sessão fica guardada ali.
3. Alternativa: extensão Claude in Chrome (exige instalar o Chrome) — mais lenta e menos repetível; fica de reserva.

## 3. Reconhecimento (uma vez, ~1 h, com Davi logado)

`nebli/kenhub/espia.py <url-do-módulo>`: abre um módulo de neuro (ex.: “Ventricles of the brain”), grava as chamadas de rede
(HAR) e capturas de tela enquanto passa por: página do módulo → quiz → revisão/“identify” → galeria/atlas. Saída:
`~/NEBLI-privado/kenhub/recon/<módulo>/` + um resumo em `arquivos-trabalho/kenhub-recon-2026-10/RECON.md` (sem imagens),
respondendo:
- como os módulos de neuro se organizam (lista oficial e URLs; a página pública de neuroanatomia mostra 21 unidades:
  neurônios, sistema nervoso, vista lateral do cérebro, tálamo, núcleos da base, tronco encefálico, córtex e núcleos do
  cerebelo, medula interna e topografia, meninges cranianas, LCR, ventrículos, artérias e veias do encéfalo, 12 nervos
  cranianos, núcleos dos nervos cranianos, meninges espinais e raízes, nervos espinais, coluna dorsal-lemnisco medial,
  tratos piramidais);
- de onde vêm as perguntas de imagem (endpoint/JSON? IDs de estrutura? imagem com o marcador já desenhado ou marcador
  sobreposto com coordenadas?);
- se cada estrutura tem nome em inglês **e** português, e se há texto curto de função/clínica que sirva ao cloze;
- se o quiz cobre todas as estruturas do módulo ou sorteia (quantas passadas até fechar a lista).

## 4. Coleta por módulo (`nebli/kenhub/coleta.py <módulo>`)

- Para cada estrutura do módulo: imagem(ns) limpa(s) com a estrutura marcada, nome EN/PT, vista (lateral, medial, corte),
  e o texto curto associado. Se o marcador vier como coordenada, guardar a imagem sem marcador + (x, y) — melhor para oclusão.
- Saída: `~/NEBLI-privado/kenhub/<módulo>/itens.json` + imagens; conferência: toda estrutura listada no módulo tem ≥ 1 imagem.
- Repetível: rodar de novo só baixa o que falta.

## 5. Montagem do deck (`nebli/kenhub/deck.py <módulo>`)

- **Oclusão (uma estrutura por card):** imagem do Kenhub; se vier com marcador, o card é “qual estrutura?” com a imagem
  como está; se vier com coordenada, usar `nebli.io_novo` (caixa de pergunta + seta até a estrutura) que já existe no NEBLI.
  Resposta no verso em negrito, nome em inglês (padrão do AnKing) com o português ao lado.
- **Cloze normal:** função, relação e clínica de cada estrutura que o módulo e o Machado tratam (ex.: “O {{c1::aqueduto do
  mesencéfalo}} liga o III ao IV ventrículo”). Primeiro AnKing/BlueLink/AnatoKing (busca semântica de sempre); autoral só
  para lacuna, dentro do teto.
- **Deck:** `NEBLI::UC07::Kenhub::<NN módulo>`; tags `NEBLI::fonte::kenhub`, `NEBLI::uc07::<aula>` (mapa módulo → aula);
  ordem: vista geral → estruturas → função/clínica.
- **Gates:** cada estrutura do módulo tem card (ou exclusão com motivo); toda imagem vista (amostra renderizada com
  `nebli.io_render`); nada do Kenhub no pacote compartilhável.

## 6. Reaproveitamento

O mesmo `coleta → deck` serve a qualquer módulo do Kenhub (membros, tórax, abdome, histologia; fisiologia tem menos imagens
de identificação, então lá o peso vai para cloze). Só muda a lista de módulos e o mapa módulo → aula/UC.

## 7. UC07 sem lâminas (o resto das aulas)

Para o conteúdo que não é estrutura (vias, síndromes, funções), seguem os decks por aula do pipeline normal, com o Machado
(“Neuroanatomia funcional”) + Bear + resumos de veteranos (GaKa, Monitoria) + aulas gravadas. Os 4 links das aulas no Drive
da USP não abrem daqui (conta USP): Davi precisa baixá-los para a pasta da UC07 no Drive pessoal ou compartilhar com
dpbdes@gmail.com.

## 8. Ordem

1. Davi responde às perguntas do chat. 2. Instalar Playwright + login (Davi, 2 min). 3. Reconhecimento num módulo →
RECON.md. 4. Piloto: um módulo completo (ex.: Ventrículos ou 12 nervos cranianos) → feedback de Davi. 5. Demais módulos de
neuro, um por vez. 6. Generalizar para as matérias do ano que vem.
