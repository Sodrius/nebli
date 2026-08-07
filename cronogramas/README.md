# cronogramas/ — índice de cronogramas por UC

Fonte-verdade dos cronogramas oficiais das UCs do Davi (FMUSP, Turma 114). Cada UC tem o **PDF/imagem-fonte** e, quando destilado, um **`.md` digest** legível (mapa aula → data → prova → componente → docente) — o digest é o que o pipeline usa para encaixar resumo→prova, nomear o PDF (`<aula curta> - Etapas 1 a 3 - <sigla prof>`) e organizar deck/Drive.

| UC | Período | Fonte | Digest | Componentes | Provas |
|---|---|---|---|---|---|
| **UC01** (1º sem) | 1º semestre 2026 | `cronograma UC01 2026.png` | — (ver `banco/aulas_uc01.yml`) | Bioquímica, Biocel, Biomol, Fisio | P1·P2·P3 |
| **UC02** (1º sem) | 1º semestre 2026 | `cronograma UC2 2026 v 1 de julho.pdf` | — (ver `banco/aulas_uc02.yml`) | Histo, Anato, Embrio, Bioq, Biomol, Imuno | P3·P4 (pós-greve) |
| **UC03** | 2º sem 2026 | Planilha mestra Drive (`1AJx4unhfGmEl_…`) | `uc03-2026.md` | RD · PT · IM · BM · MB (+ PT-RD, Grand Rounds) | P1 28/08 · P2 02/10 · P3 06/11 · P4 04/12 |
| **Ciclo da Vida I (UC-16)** | 2º sem 2026 | `cronograma Ciclo da Vida I (UC-16) 2026.pdf` | `ciclo-da-vida-i-uc16-2026.md` | Pediatria, Geriatria | **prova final única** (28-29/09) |
| **Digestório (UC-8 / Med5043)** | 2º sem 2026 | `cronograma Digestorio (UC-8 Med5043) 2026.pdf` · `cronograma Anatomia Digestorio (UC-8) 2026.pdf` | `digestorio-uc8-med5043-2026.md` | Anatomia, Histologia (BioTec II), Fisiologia, Biocel/Embrio | P1 (08/05-out) · P2 (26/30-nov) |

## Notas
- **2º semestre (agora):** o Davi cursa **UC03**, **Ciclo da Vida I (UC-16)** e **Digestório (UC-8)** em paralelo. As UCs 01/02 são do 1º semestre (ciências básicas, banco de questões em `banco/`).
- **Planilha mestra viva no Drive** (`2026 - Matérias e Mês`, id `1AJx4unhfGmEl_4dqhO7OTpVhZ0TFAR5QgTorfmxSess`): cobre UC03/UC04/UC07/UC08/UC16/UC19/UC21-DIC/UC30 numa grade única (colunas por UC + aba mensal). É a **fonte-verdade viva** — quando um digest divergir, a planilha vence. Ler via `mcp__Google_Drive__read_file_content` antes de gerar resumo ou canonizar mudança de data.
- **Turmas:** o Davi é da **Turma 114** e, na subdivisão A/B destas UCs do 2º semestre, cursa a **Turma B** — usar sempre a **coluna Turma B** dos cronogramas para as datas dele (Ciclo da Vida I: prova final 28/09; Digestório: P1 05/10, P2 30/11).
- **Banco de questões:** ainda não há `banco/aulas_uc16.yml` nem `aulas_uc8.yml` — as novas UCs não têm calibração de banco (resumos usam slide + bibliografia + AnKing).
- **Padrão de nomes:** arquivos-fonte seguem `cronograma <UC> <ano>[.ext]`; digests seguem `<uc-slug>-<ano>.md`.
