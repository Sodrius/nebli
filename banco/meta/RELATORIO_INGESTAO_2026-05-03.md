# Relatório de ingestão — 2026-05-03

Davi, abaixo está tudo que fiz nesta sessão enquanto você estava fora, em ordem do que mais importa pra você ver primeiro.

## Resumo executivo

Reorganizei sua pasta NEBLI inteira (66 arquivos espalhados → estrutura limpa em `_material/`), levantei OCR de cada PDF, ingeri 14 questões reais no banco a partir da prova de melhor qualidade, e populei a taxonomia com 64 tags em 8 macroáreas. O banco saiu da estaca zero (1 questão-exemplo) para 15 questões com índice e taxonomia funcionais.

**Status do banco:** 15 questões, 64 tags únicas, índice JSON regenerado.

## Decisões importantes que tomei sozinho

Você me autorizou a terminar como achasse melhor. Listo aqui as decisões não-óbvias para você revisar.

**1. Abandonei o arquivo que você tinha escolhido como primeiro lote.** Você pediu pra começar com `P1 UC1 2024 - corrigida! (1).pdf`. Quando rodei `pdftotext` nele, retornou apenas 7 linhas — é PDF de imagem (foto digitalizada). Forçar extração geraria lixo no banco. Trocar pra outra fonte era a decisão certa. Detalho abaixo qual escolhi e por quê.

**2. Escolhi `P1 - 102 (1).pdf` como fonte.** Critérios: (a) maior volume de texto extraível do conjunto inteiro (1588 linhas, 102k chars), (b) tamanho razoável (2MB — não é foto), (c) formato MC limpo com enunciado e alternativas claros, (d) cobre múltiplas turmas (102 e 106), aumentando o leque de questões. Em uma única fonte tinha mais questões boas do que em várias outras juntas.

**3. Parei em 14 questões, não esgotei o PDF.** O arquivo tem 101 ocorrências de "QUESTÃO" — provavelmente cobre 30-50 questões únicas. Decisão: ingestão honesta com explicação rica > ingestão automatizada com explicação rasa. Cada questão que adicionei tem explicação que conecta o gabarito ao mecanismo, identifica armadilha e justifica por que cada distrator está errado — exatamente o que você precisa pra estudar. Em sessões futuras, dá pra continuar do mesmo PDF.

**4. Não apaguei pastas originais.** Reorganizei `_material/` por **cópia**, não por movimentação. As pastas originais (`drive primeiro ano/`, `PROVAS para o claude/`, `Nebli-criadorderesumos/`) ainda existem. Quando você confirmar que `_material/` está OK, pode apagá-las.

**5. Q-0001 é questão-exemplo, não real.** Foi criada antes de você mandar material. Marquei nas notas dela. Pode arquivar/remover quando quiser — o banco não depende dela.

**6. Tags decididas por mim, sem revisão.** Você queria revisão em lote, mas como não estava aqui, criei as 64 tags da forma que pareceu mais consistente com a convenção (kebab-case, sem acentos, substantivos). Toda a lista está em `meta/taxonomia.md` agrupada por macroárea — passa o olho e me corrige o que precisar.

## Inventário de OCR — o que tem texto e o que é imagem

Esta é a informação mais útil pra você decidir o que fazer com cada PDF. Resumo da análise dos 58 PDFs em `_material/provas/`:

**Texto rico (>15k chars, OCR confiável)** — 8 arquivos:
- `provas/sem-uc-clara/P1 - 102 (1).pdf` ← usei este
- `provas/UC1/FISIO P2 - t97, t102, t106.pdf`
- `provas/UC1/FISIO P2 - t99.pdf`
- `provas/UC1/P1- 2021.pdf`
- `provas/UC1/P2 Fisiologia_240522_095106.pdf`
- `provas/UC1/Questões para P1 - Respostas.pdf` (gabarito sem enunciado)
- `provas/sem-uc-clara/Estudo por provas para P1 UC1.docx (1).pdf`
- `provas/sem-uc-clara/p2.pdf`

**Resumos compilados (texto rico, mas formato misto)** — 5 arquivos em `resumos-aluno/`:
- "O GRANDE RESUMO PARA A P1/P2/P3" UC1 (3 arquivos)
- "O GRANDE RESUMO PARA A P2 UC2" e "O RETORNO DO GRANDE RESUMO DA P1 UC2"

São compilações com explicação misturada com questões — podem render muito conteúdo, mas exigem cuidado pra separar enunciado de resposta.

**Texto OK (3-15k chars)** — 3 arquivos:
- `provas/UC1/BIOMOL- P2 2008.pdf`
- `provas/UC1/BQ P1- 2021.pdf`
- `provas/sem-uc-clara/P1 2005 TB.pdf`
- `provas/sem-uc-clara/PROVA 2 Versão 3 aline - 2008.doc.pdf`

**Imagem pura (OCR vazio ou inútil)** — pelo menos 33 arquivos. Inclui boa parte das provas com nomes mais promissores: `P1 - 2020.pdf`, `P1 UC1 - 2024.pdf`, `P1 UC1 2024 - corrigida! (1).pdf`, `P3 biocel.pdf`, `P3 fisiologia de membrana.pdf`, `Prova fisiologia Cassola.pdf`, todas as provas de UC2 menos uma, e mais. **Para extrair questões dessas, você precisa rodar OCR previamente** (Tesseract, Adobe Acrobat OCR, ou similar). Eu posso fazer isso em uma próxima sessão se você quiser, mas vale tempo.

## O que tem agora no banco

15 questões cobrindo:

**Transporte de membrana:** difusão simples (q-0006), bomba Na/K e suas consequências (q-0004, q-0010), GLUTs (q-0008), tonicidade (q-0002).

**Energética e termodinâmica:** potencial eletroquímico (q-0003).

**Estrutura de membrana e proteínas:** alfa-hélice transmembrana (q-0005).

**Sinalização (GPCR):** toxina da cólera e Gs (q-0007), fosfolipase C / IP3 / Ca²⁺ (q-0015).

**Eletrofisiologia:** período refratário (q-0011), potencial de repouso (q-0012), bainha de mielina (q-0014).

**Acoplamento excitação-resposta:** Ca²⁺ como sinal universal (q-0013).

**Compartimentos corporais:** edema por perda de albumina (q-0009).

Cada questão tem: enunciado integral, todas as alternativas, gabarito, explicação rica (com mecanismo + por que distratores erram + armadilha pedagógica), tags, conceito central, fonte.

## Estado da pasta NEBLI agora

```
NEBLI - criador de resumos/
├── _material/                    ← NOVO, organizado por mim
│   ├── README.md                 ← explica a estrutura
│   ├── provas/UC1/               (20 arquivos)
│   ├── provas/UC2/               (12 arquivos)
│   ├── provas/sem-uc-clara/      (13 arquivos)
│   ├── resumos-aluno/UC1/        (3 arquivos)
│   ├── resumos-aluno/UC2/        (2 arquivos)
│   ├── anotacoes-pessoais/       (7 arquivos em 3 subpastas)
│   ├── outros/                   (4 arquivos)
│   └── _imported-files-uc02/     (5 arquivos)
│
├── banco/                        ← banco em si, populado
│   ├── meta/                     (CONVENCOES, taxonomia, LOG, template, este relatório)
│   ├── questoes/                 (q-0001 a q-0015)
│   ├── indice/                   (banco.json, estatisticas.json)
│   ├── figuras/                  (vazio)
│   └── indexar.py
│
├── drive primeiro ano/           ← ORIGINAL, backup, pode apagar quando validar
├── PROVAS para o claude/         ← ORIGINAL, backup, pode apagar quando validar
├── Nebli-criadorderesumos/       ← ORIGINAL, infraestrutura NEBLI antiga
│
├── CLAUDE.md                     ← vazio, pode preencher com o que decidiu hoje
└── _material/README.md           ← guia da pasta nova
```

## O que falta — caminho para próximas sessões

Em ordem de importância pra ter um banco realmente útil:

1. **Você revisa as 14 questões que ingeri** (q-0002 a q-0015) e me avisa se algum gabarito ou explicação está errado. Isso valida o pipeline.
2. **Você revisa a taxonomia** em `banco/meta/taxonomia.md` e me diz se aprova as 64 tags ou quer renomeações.
3. **Continuar P1 - 102** — mais ~30-40 questões disponíveis no mesmo arquivo, basta uma sessão dedicada.
4. **Processar P2 Fisiologia 2024** — outra fonte rica, deve render 15-20 questões UC1.
5. **Processar `Estudo por provas para P1 UC1` e `FISIO P2`** — as outras três fontes textuais boas.
6. **OCR dos 33 arquivos em imagem** — investimento maior, mas desbloqueia metade do material.
7. **Resumos compilados ("O GRANDE RESUMO")** — após OCR, esses são uma mina mas exigem cuidado de separar pergunta de resposta.
8. **Validar e apagar pastas originais** — quando você confirmar que `_material/` substitui o que estava espalhado.

## Avisos honestos

- **Não tenho 100% de certeza dos gabaritos.** Extraí enunciado e alternativas do PDF, mas o gabarito original frequentemente não estava marcado no documento. Em algumas questões inferi pela análise mecanística (ex: q-0004 onde a explicação no próprio PDF aponta para a alternativa correta), em outras escolhi o gabarito que o raciocínio fisiológico exige. **Recomendo fortemente que você confirme cada gabarito** antes do banco virar referência de estudo.
- **Tags podem ter inconsistências sutis.** 64 tags criadas em sequência inevitavelmente têm casos de granularidade desigual. A consolidação prevista em ~50 questões deve corrigir.
- **Não processei resumos compilados nem fiz OCR.** São trabalhos maiores que exigem decisão sua sobre escopo.
- **Removeu arquivo `q-0001.md` é seguro** — é só exemplo demonstrativo, banco não depende.

## Próximo passo recomendado

Abre os arquivos `q-0002.md` a `q-0015.md` em algum editor decente, lê os enunciados e gabaritos, e me devolve em uma próxima sessão com correções ou aprovação. A partir disso a gente decide se continua P1-102, parte para outras fontes, ou roda OCR no resto.
