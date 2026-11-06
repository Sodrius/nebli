# 65 Reparo tecidual v4 — plano para a próxima sessão (06/11/2026, Claude)

Motivo (Davi, 06/11): "ajusta o deck da aula de cicatrização, que ficou raso, não abordou tudo (ex: o gráfico com fases da inflamação)". Antes dele, F-20261105-CLAUDE-01: "faltou card de fases da cicatrização" e "essa é uma aula da P4 já".

## Diagnóstico (verificado)
- `inventario.py` da v3 marca 13 das 43 lâminas de conteúdo como `fora_do_recorte` ("figura ou detalhe sem card próprio"): **5, 9, 16, 17, 18, 20, 24, 25, 30, 32, 34, 35, 37** = 30% da aula. É a causa do raso: tudo que era figura/gráfico foi cortado, inclusive os três gráficos (16 fases sobrepostas; 24 células × dias e oxigênio; 30 fibronectina/colágeno III × I e força tênsil).
- O deck tem 29 cards para 45 lâminas; as lâminas 8 e 9 (tabela de fatores de crescimento) só têm TGF-β e PDGF.
- O deck está em `NEBLI::UC03::P3::Patologia::Reparo tecidual…`, mas Davi diz que a 65 é P4 (ver cronograma-uc03-2026: P4 = 65, 69, 66, 67, 70, 72, 74–79, 81–85). Mudar `DECK` no spec para `...::P4::Patologia::...` junto da reorganização pedida.

## Já feito nesta corrida (v4, copiada da v3 com fontes, spec, mapa, motivações)
- `img/im65-celulas-tempo.png` (lâmina 24: neutrófilo pico ~dia 2, macrófago ~dia 3, fibroblasto ~dia 5–6, linfócito ~dia 6) e `img/im65-colageno-tempo.png` (lâmina 30: fibronectina e colágeno III sobem cedo e caem; colágeno I e força tênsil sobem) recortados; `im65-fases.png`, `im65-potencia.png`, `im65-reepit.png`, `im65-intencoes.png` já existiam.
- E0 NÃO registrada (a leitura obrigatória inteira ainda falta: MEMORY linhas 118–218 e o resto do pipeline; fazer na próxima sessão antes de `nebli.etapa … E0`; `exemplares-lidos.json` copiado da v3 está desatualizado e reprova).

## Cards novos planejados (autorais só depois de busca em AnKing/externos; cada um com motivação, item do mapa, tipos.tsv, REVISAO-AUTORAIS com EXEMPLAR/ANTI)
Figuras vão no Extra (convenção da v3), nunca na frente.
1. Lâm. 16–17, **gráfico das fases** (exemplar de gráfico 1791826286643/1791826286795): fases sobrepostas, inflamação 4–6 d, proliferação 4–24 d, remodelação 21 d–2 anos; imagem `im65-fases.png`.
2. Lâm. 13, cinco eventos do reparo em ordem (inflamação, angiogênese, migração/proliferação de fibroblastos, cicatriz, remodelamento).
3. Lâm. 18: dia 1, vasoconstrição + plug primário limitam a perda de sangue e ocluem a ferida.
4. Lâm. 20: plaqueta libera PDGF, serotonina e histamina → vasodilatação e permeabilidade.
5. Lâm. 24, **gráfico de células por dia** (ordem de pico: neutrófilo, macrófago, linfócito, fibroblasto; oxigênio cai e depois sobe com a angiogênese); imagem `im65-celulas-tempo.png`.
6. Lâm. 25: fatores de crescimento da ferida no dia 3 (quem libera o quê); KGF do fibroblasto estimula o queratinócito.
7. Lâm. 30, **gráfico da matriz**: fibronectina/colágeno III cedo, colágeno I depois, força tênsil acompanha o colágeno I; imagem `im65-colageno-tempo.png`.
8. Lâm. 32/34: tecido de granulação como leito vermelho; desbrida-se a ferida necrótica até aparecer (sinal de boa evolução).
9. Lâm. 35: reepitelização por células basais; epiderme mais fina, menos queratina, pigmento alterado; imagem `im65-reepit.png`.
10. Lâm. 5: células-tronco, totipotente (zigoto) → pluripotente embrionária → multipotente → comprometida → somática; imagem `im65-potencia.png`.
11. Lâm. 8–9: organizador de fatores de crescimento por célula-alvo (EGF/TGF-α/KGF queratinócito; HGF hepatócito; VEGF endotélio; FGF fibroblasto/angiogênese; PDGF fibroblasto) e paradoxo do TGF-β (inibe crescimento celular, promove fibrose).
12. Lâm. 37: mapear aos cards existentes de maturação/força/contração (só se verdadeiro) ou card próprio de redução do edema.
Regras que valem: F-20261105-CLAUDE-01 (depois da 3ª rodada o parecer vira sugestão; não cortar card para passar no revisor); GUIA-1 (cloze ≤3 palavras, negrito fora do cloze, Extra ≤51 palavras, sem travessão, sem legenda sob figura); gráfico = pergunta direta sobre a figura, interpretação no Extra (MEMORY §7).

## Depois da 65 (ordem pedida por Davi)
1. **Gates anti-raso** em `nebli/gates.py` (+ teste em `nebli/tests/test_gates.py`, subir `PIPELINE_VERSAO`, arquivar o pipeline em `arquivo/` com hash, reescrever a etapa no EXECUCAO-DECK-AULA e MEMORY §2): (a) `fora_do_recorte` ≤ 10% das lâminas de conteúdo e nenhuma lâmina de gráfico/esquema/tabela fora sem motivo próprio por lâmina; (b) toda lâmina de conteúdo aponta card ou `EXC` com motivo individual; (c) lâmina com gráfico (detectar por imagem sem texto/slide com poucas palavras) exige card com a figura; (d) piso de densidade cards ÷ lâminas de conteúdo calculado dos decks que Davi aprovou (64 Hipersensibilidade, UC08-BC10) e alerta duro abaixo dele; (e) o encolhimento do plano entre rodadas (ex.: 54→29 notas) bloqueia sem justificativa.
2. **Ordem P1–P4 pelo Moodle**: o e-Disciplinas da UC3 NÃO traz a aula→prova (a lista de material é por aula; as provas só aparecem como arquivos antigos P1–P4 em "Avaliações"; P1 2026 tem gabarito em 10/09). A fonte que existe é a planilha/cronograma colado por Davi em 21/10 (P3 em 06/11 = conteúdos 3–5, 12, 40, 43–68; P4 = 65, 69, 66, 67, 70, 72, 74–79, 81–85). Conflito: a 65 está dentro de 43–68 mas Davi diz P4. Perguntar a Davi, ou conferir com o PDF `P4 - UC3-2025 - Final` do Moodle, e então mover os subdecks (hoje `P3` tem Reparo tecidual, Inflamação crônica/granulomatosa, Infecção viral etc.) via `nebli.decks.escrita()`, sem mexer na nota em tela.
3. **Deck da 69 Hemostasia, trombose, embolia e infarto**: existe no Moodle (objetivos, slides PDF, transcrição, 4 artigos, cruzadas); o ESTADO-ATUAL dizia pasta do Drive vazia, conferir no Drive pessoal primeiro. Há corrida antiga `deck-aula-uc03-pt69-hemostasia-trombose-v2-2026-10-22`. Pipeline v15 completo, E0–E8, com os gates novos.
