# Estrutura do Drive do Davi — template canônico de upload (2026-07-12)

Mapeada via rclone (remote `nebli-drive:`, My Drive do Davi). **Regra dura:** seguir EXATAMENTE esta organização ao subir material; nunca impor estrutura própria. A cada UC nova, replicar o mesmo padrão guiado pelo cronograma.

## Caminho-raiz dos resumos
```
nebli-drive:RESUMOS - Davi Sousa/B - Primeiro ano/UC<NN>/<Componente>/<NN - Nome da aula>/
```
(Existe um espelho em `Medicina - Davi Sousa/Resumos e exercícios/` — usar o `RESUMOS - Davi Sousa` como canônico.)

## Componentes (UC02) — organiza por COMPONENTE, não por prova
- `Anatomia`
- `Biologia Celular, tecidual e imunologia`  (histologia + embriologia + imunologia)
- `Bioquímica e biologia molecular`  (bioquímica + biologia molecular)

## Componentes (UC-8 Digestório, canon 2026-08-08 — 2º sem 2026)
- `Anatomia` — id `1UJsKopZu4_ksjJsn69NdTIWahFukPO2q`
- `Fisiologia` — id `1h3q2XFGY25zMzqGgVLqcwhWCbI2-R7v7`
- `Biologia Tecidual` — id `1SX2rxGmUMTvgvCOruTmwvPrPN-0mZDx0`
- `Biologia Celular` — id `1qSt3vsu2vPQzgsRDowmwJdw4tiWTO-0r`

Pastas de aula (Anatomia UC-8, já criadas pelo Davi):
- `01 - Esôfago, estômago e delgado` — id `1sg4WMtpGzA3LhdZg9M8sXXM0MJkP0llG` (P1)
- `02 - Intestino grosso e canal anal` — id `1GATNLKY4BG7oR-iCUBtWpuKXjkRA03Pi` (P1)
- `07 - Vascularização das vísceras` — id `1anr09zp44SG100cQsQ-4jMVk6b0rcM2W` (P1)
- `11 - Fígado, pâncreas e vias biliares` — id `1g2MAvaZlq8SuvTr1DPSDYtxlM5BVz2bp` (P2)
- `13 - Cavidade abdominal e peritônio` — id `1OWV6s-dry8hV4a_HoRYNyKWA0Y9eYh84` (P2)
- `14 - Inervação do digestório` — id `1YLZmqgZVGJmXNNe58tSt2oLSK0VJhH72` (P2)

> Nota: o Drive NÃO tem nível de prova. O Anki (`NEBLI::UC::Prova::Componente::Aula`) é por prova (pra estudo dirigido); o Drive é por componente (arquivo). Os dois **compartilham o nome da aula** — é isso que casa os dois. Não forçar prova no Drive nem componente-separado (bioq/biomol ficam juntos no Drive).

## Pasta da aula: `NN - <Nome da aula>` (NN = ordem de ensino no componente)
Conteúdo por aula:
- **Resumo:** `<Nome da aula> - Etapas 1 a 3 - <prof>` (PDF; sufixo `- <prof>` quando conhecido)
- **Slide:** `<Nome da aula> - slides - <prof>`
- **Deck (novo, NEBLI):** `<Nome da aula>.apkg`
- Extras existentes (não mexer): `RP - Aula N.pdf`, `RT - Aula N.pdf`, `Material Complementar`, `Mapa mental - ...`

## Mapa slug → pasta Drive (UC-8 Digestório, canon 2026-08-08)
| slug NEBLI | Componente | Pasta da aula |
|---|---|---|
| digest-01-esofago-estomago-intestino | Anatomia | `01 - Esôfago, estômago e delgado` |

## Mapa slug → pasta Drive (UC02, pastas já existentes)
| slug NEBLI | Componente | Pasta da aula |
|---|---|---|
| bioq-20-pentoses-radicais-livres | Bioquímica e biologia molecular | `01 - Via das pentoses` |
| biomol-25-mutacao-reparo-recombinacao | Bioquímica e biologia molecular | `02 - DNA mutação, lesão e reparo` |
| biomol-26-dna-recombinante-pcr | Bioquímica e biologia molecular | `03 - DNA recombinante` |
| bioq-21-lipideos-rotas | Bioquímica e biologia molecular | `04 - Metabolismo dos lipídeos` |
| bioq-24-glicogenio | Bioquímica e biologia molecular | `05 - Metabolismo do glicogênio` |
| bioq-23-aminoacidos-ureia | Bioquímica e biologia molecular | `06 - Metabolismo dos aminoácidos` |
| embrio-01-gametogenese-fertilizacao | Biologia Celular, tecidual e imunologia | `11 - Embriologia I` |
| embrio-02-03-gastrulacao-neurulacao | Biologia Celular, tecidual e imunologia | `12 - Embriologia II e III` |

## Regras operacionais
- **Não modificar permissões de compartilhamento** (proibido pra mim). Se um material precisar ir a terceiros (ex.: Arthur), eu subo/entrego o arquivo, mas o compartilhamento é o Davi que faz.
- Upload via `flashcards/scripts/subir_drive.py` (rclone `copyto` pro caminho da aula).
- Antes de subir aula nova de UC nova: `rclone lsd` na UC pra achar/confirmar o componente e o número da aula (ordem do cronograma daquela UC).
- Remote rclone: `nebli-drive` (service via OAuth com refresh_token — headless, renova sozinho).
