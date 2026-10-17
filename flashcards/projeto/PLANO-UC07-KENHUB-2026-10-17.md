# Plano UC07 — deck de neuroanatomia a partir do Kenhub (decisões de Davi, 17/10/2026)

Complementa o PLANO-KENHUB-2026-10-16.md (limites, ferramenta, reconhecimento). Onde divergir, vale este.

## Decisões

- **Deck:** `NEBLI::UC07::<módulo>::<submódulo>` (nomes como no Kenhub, em português). Primeiro módulo: **tronco encefálico**.
- **Lógica:** UC07 não segue prova. É um deck de neuroanatomia **completo**, organizado como o Kenhub, complementado por outras fontes.
- **Sem limite de cards.** Toda estrutura listada no módulo recebe ≥ 1 card (gate: estrutura sem card = falha, exceto exclusão com motivo).
- **Oclusão:** **uma imagem por estrutura**. Imagem do quiz do Kenhub é o padrão; AnKing e AnatoKing (e outros decks de referência) complementam com peças de cadáver quando úteis. Sem legenda/crédito visível; nunca desenhar esquema (ver nebli-imagem-real).
- **Idioma:** cards em **português**; nome em inglês pode ficar ao lado no verso.
- **Estrutura sem figura no Kenhub:** avisar Davi no relatório; pode buscar em outros decks ou no Netter.
- **Fisiopatologia associada à neuroanatomia** (ex.: AVC hemorrágico afetando o trigêmeo → o que acontece): pode haver, mas **só AnKing, nunca autoral**.
- **Complementos de conteúdo:** Machado (Neuroanatomia funcional) + o que os veteranos colocam (GaKa, Monitoria etc.), para o deck cobrir tudo. Origem dos cards: AnKing → AnatoKing/outros acervos → autoral só para lacuna (regras do cloze: nebli-cloze-onde-decora).
- **Depois de neuro:** outros temas de anatomia (Davi quer), pelo mesmo `coleta → deck`; nome do deck desses temas a decidir depois.
- **Liberação:** instalar tudo na ordem do Kenhub e deixar suspensos os módulos seguintes até a vez deles (≈ 40 novos/dia).
- **Pipeline para todos os módulos:** cadastro único de estruturas (ID, PT, EN, sinônimos, módulos) para não duplicar entre módulos; glossário PT; GUID estável; estado por módulo; gate de privacidade Kenhub; cobertura por módulo. Objetivo: estudo de neuroanatomia a longo prazo, de verdade.

## Limites (não mudam)

- Imagens do Kenhub só uso pessoal: `~/NEBLI-privado/kenhub/`, fora do git, do pacote da UC (`nebli.package_uc` exclui a tag `NEBLI::fonte::kenhub`, a fazer antes do piloto) e do AnkiHub.
- Ritmo humano, só os módulos pedidos, um por vez. Sem contornar acesso/assinatura; não se constrói nada para acessar o Kenhub sem assinatura. Os decks prontos ficam no Anki de Davi.
- Login do Kenhub é por e-mail/senha (Google bloqueia navegador automatizado); sessão no perfil local.

## Fluxo do piloto (tronco encefálico)

1. `espia.py` no módulo: como o quiz entrega pergunta/imagem/resposta; lista oficial de submódulos e estruturas.
2. `coleta.py`: por estrutura, imagem limpa + nome (+ coordenada se houver) → `~/NEBLI-privado/kenhub/<módulo>/itens.json`.
3. Mapear cada estrutura nas fontes: AnKing/AnatoKing (peças de cadáver), Machado, veteranos; marcar lacunas sem figura.
4. `deck.py`: oclusão (1 por estrutura) + cloze/fisiopato (AnKing) → deck por submódulo; gates; amostra renderizada com `nebli.io_render`.
5. Relatório a Davi: estruturas cobertas, sem figura, % autoral.
