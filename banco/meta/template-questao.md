---
# === OBRIGATÓRIOS ===
id: 0
tags: []                          # array, ex: [transporte-membrana, bomba-na-k]
nivel:                            # facil | medio | dificil
formato:                          # MC | CE | discursiva
conceito_central: ""              # uma frase: o que a questão testa de fato
gabarito:                         # MC: letra A-E | CE: array [C,E,C,E] | discursiva: ver corpo

# === OPCIONAIS — deixar em branco se não souber, NÃO preencher com "?" ou "n/a" ===
uc_origem:                        # UC1, UC21, etc.
aula:                             # slug canônico da aula. Ver banco/aulas_uc01.yml.
                                  # Ex: bioq-15-glicolise, fisio-05-potencial-acao.
                                  # OBRIGATÓRIO para questões de UC01 a partir de 2026-05-14.
                                  # Para outras UCs: deixar vazio até a UC virar ativa.
prova:                            # P1 | P2 | P3 | sub | recup
ano:                              # 2024
armadilha: ""                     # qual confusão a questão explora
figura:                           # figuras/respiratorio_curva_pv.png
fonte: ""                         # FMUSP turma 113, USMLE step 1, Berne cap 4, etc.

# === SUB-ITENS (só se a questão tem múltiplos conceitos por alternativa/item) ===
itens: []
# Exemplo:
# itens:
#   - letra: A
#     conceito: difusao-simples
#     tags: [difusao, transporte-membrana]
#   - letra: B
#     conceito: bomba-na-k
#     tags: [bomba-na-k, transporte-ativo-primario]

# === CAMPOS PROCEDIMENTAIS (Claude usa durante ingestão) ===
tags_pendentes_aprovacao: []      # tags novas que Claude propôs mas Davi ainda não validou
ingestao_data:                    # YYYY-MM-DD da entrada no banco
---

## Enunciado

(Texto integral do enunciado da questão, preservando formatação original quando possível.)

## Alternativas

(A) ...
(B) ...
(C) ...
(D) ...
(E) ...

<!-- Para CE, listar os 4 itens numerados -->
<!-- Para discursiva, omitir esta seção -->

## Gabarito

(Letra ou array C/E. Repetir o que está no frontmatter, por conveniência de leitura humana.)

## Explicação

(Explicação concisa do gabarito. Causa → mecanismo → consequência. Por que as outras alternativas estão erradas, especialmente a armadilha.)

## Notas

(Opcional. Observações de Davi durante revisão, conexões com aulas, dúvidas pendentes.)
