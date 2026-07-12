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

> Nota: o Drive NÃO tem nível de prova. O Anki (`NEBLI::UC::Prova::Componente::Aula`) é por prova (pra estudo dirigido); o Drive é por componente (arquivo). Os dois **compartilham o nome da aula** — é isso que casa os dois. Não forçar prova no Drive nem componente-separado (bioq/biomol ficam juntos no Drive).

## Pasta da aula: `NN - <Nome da aula>` (NN = ordem de ensino no componente)
Conteúdo por aula:
- **Resumo:** `<Nome da aula> - Etapas 1 a 3 - <prof>` (PDF; sufixo `- <prof>` quando conhecido)
- **Slide:** `<Nome da aula> - slides - <prof>`
- **Deck (novo, NEBLI):** `<Nome da aula>.apkg`
- Extras existentes (não mexer): `RP - Aula N.pdf`, `RT - Aula N.pdf`, `Material Complementar`, `Mapa mental - ...`

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
