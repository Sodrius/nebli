# CHECKPOINT — imuno-02-organizacao-sistema-imune

Pipeline: `e1-deck-v9` · backend `ankidroid` · schema `nebli-ankidroid-deck-v3`
Fase: **concluída** (E1 congelada, gate card a card 100%, release gate aprovado, manifesto gerado).

## Metadados do deck

| campo | valor | base da inferência |
|---|---|---|
| UC | UC03 | capa do slide: "Unidade curricular-3 – Curso de Medicina" |
| Prova | P1 | aula de abertura do bloco de imunologia da UC03 (a aula anterior citada é da UC02); não há cronograma de UC03 no repo |
| Componente | Imunologia | disciplina do slide e da transcrição |
| Nome curto | Organização do sistema imune | título da videoaula, encurtado |

Deck canônico: `NEBLI::UC03::P1::Imunologia::Organização do sistema imune`
Subdeck de opcionais: `…::Optional` (1 card).

## Fontes da aula

1. Apresentação da videoaula (26 slides) — objetivos, esquemas de recirculação, aferência, regionalização, adesão e quimiocinas.
2. Transcrição integral da videoaula (50 páginas) — mecanismos, exemplos e o que o professor marca como fora do escopo desta aula.
3. Gabarito das palavras cruzadas — triado: entram os itens do tema (linfócito B, transmigração, BALT, MHC, medula óssea, plasmócito, fagocitose, seleção negativa, bursa); ficam fora, por exigirem aula própria, inflamassoma/IL-1β, defensinas, CTLA-4, imunoterapia, AIRE como item isolado de autoimunidade, doenças autoinflamatórias/autoimunes, basófilos e eosinófilos.

## E1

- `typst-build/etapa1.typ` (4 PARTES, 18 subtópicos) + `resumindo.typ` (20 blocos) + `main.typ`.
- PDF: `typst-build/imuno-02-organizacao-sistema-imune.pdf` (24 páginas).
- Figuras: `figuras/imuno-02-organizacao-sistema-imune/slide-NN.png` (renderizadas do PDF da aula; não versionadas).
- Revisão independente registrada em `release_gate.e1_review`: inventário dos 26 slides, os 5 objetivos, mecanismos explícitos, diagramas interpretados em prosa, Step 1 revisado, nenhuma omissão ou ambiguidade nuclear pendente.

## Aprofundamento Step 1 incorporado à E1 antes dos cards

Seleção positiva no córtex / negativa na medula · AIRE e APECED · L-selectina e CCR7 na HEV · gradiente de S1P e fingolimode · CD40L–CD40 e hiper-IgM · apresentação cruzada em MHC I · asplenia e encapsulados (ancorado na própria leitura complementar da aula) · hipermutação somática e troca de classe no centro germinativo · plasmócito de vida longa e mieloma múltiplo · cascata de extravasamento (selectina → integrina β2/ICAM-1 → PECAM-1) · LAD tipo 1 · CXCL8 e CCL2.

Rejeitados explicitamente (registro em `release_gate.concepts[].step1`): receptores de reconhecimento de padrão e inflamassoma (a própria aula os adia), coestimulação/anergia como mecanismo da tolerância.

## Orçamento e gate

- `card_budget.hard_max` congelado em **52**; deck real com **50** cards (porte grande, faixa de sanidade 35–55).
- Fontes: **26 AnKing** (todos com `anking_required=true` e fallback autoral validado), **22 autorais**, **2 Image Occlusion**.
- `validar_deck_card_a_card.py`: `expected = validated = passed = 50`, `failed = 0`.
- `validar_release_e1_deck.py`: aprovado — 44 conceitos, 41 nucleares, 41 com cobertura ≥ 2.
- `finalizar_entrega_canonica.py`: manifesto `nebli-ankidroid-deck-v3` com `expected_card_count=50` e 2 mídias embutidas por SHA-256.

## Image Occlusion

| card | slide | máscaras | tarefa |
|---|---|---|---|
| `io-recirculacao-hev-linfa` | 13 | HEV, Linfa | localizar entrada (sangue → HEV) e saída (linfa) do circuito do linfócito naïve |
| `io-foliculo-fdc-centro-germinativo` | 20 | FDC, Centro germinativo | reconhecer a célula estrelada residente e a zona que surge com o estímulo correto |

Geometria calculada a partir das caixas reais de texto do PDF da aula; previews de pergunta e resposta renderizados e conferidos visualmente antes de marcar `question_preview_validated` / `answer_preview_validated`.

## Limitação registrada desta corrida

A coleção AnkiDroid não é acessível a partir deste ambiente de execução (o Companion resolve AnKing localmente, no tablet). Os 26 cards `source="anking"` foram curados por conhecimento do conteúdo AnKing/First Aid e viajam no manifesto com `search_queries`, `expected_answers`, restrições e fallback autoral validado; o `score` registrado na validação é o mínimo contratual (`score_basis="plan_contract_minimum"`), não uma medida local. Como `anking_required=true`, uma nota ausente na coleção bloqueia o lote em vez de cair em fallback silencioso — comportamento canônico esperado.

## Incidente de instalação (corrigido)

Primeira tentativa de instalação bloqueou com
`IllegalArgumentException: io-recirculacao-hev-linfa IO gate: [io_mode_must_be_hide_all_guess_all]`
e nenhum lote parcial foi mantido — o rollback funcionou como previsto.

Causa: o APK instalado no tablet é anterior ao commit `4e1d678` (PR #19), que
renomeou o modo IO de `hide_all_guess_all` para `hide_two_guess_two`. O plano
estava correto; o runtime instalado é que ainda valida o nome antigo. Comparado o
`FullDeckInstaller` pré-#19: o caminho IO é idêntico ao atual, e a única
divergência é o nome do modo (o limite de duas máscaras já é cumprido).

Correção em três frentes:

1. `CardRules.validateIo` passa a aceitar o nome canônico **e** o legado,
   mantendo o teto de duas máscaras nos dois — testado no runtime real da classe.
2. `gerar_manifesto_ankidroid.py` ganhou `companion_compat.io_mode`: o plano e os
   gates seguem em `hide_two_guess_two` e só o valor gravado no manifesto
   acompanha o runtime instalado; o manifesto declara `io_mode_contract`.
3. `ERROS.md` #52 registra a regra geral para qualquer valor de protocolo.

Quando o APK for reconstruído a partir do `main` atual, basta remover o bloco
`companion_compat` do `deck-data.json` e regerar.

## Metadados confirmados

Planilha mestre "2026" (Drive do Davi), linha `07/08 · 08:00–10:00 ·
Anfiteatro Microbiologia nº 2104 · IM · Organização e funcionamento do sistema
imune · P1`. Confirma componente Imunologia e **prova P1**; a UC03 vem do bloco
em que a aula está, o mesmo de `radiologia-01-ferramentas-diagnostico`. A aula
seguinte na planilha, "Reconhecimento pelo sistema imune na resposta inata"
(11/08, P1), é exatamente o gancho deixado na conclusão da E1.

Slug corrigido para `imuno-02-…`: a numeração é por disciplina e a UC02 já tem
`imuno-01-disturbios-imunidade`, do mesmo docente.

## Próximo passo

Abrir `entregas/imuno-02-organizacao-sistema-imune/imuno-02-organizacao-sistema-imune.ankidroid.json` no Nebli Companion e conferir no recibo `installed_card_count == 50`.
