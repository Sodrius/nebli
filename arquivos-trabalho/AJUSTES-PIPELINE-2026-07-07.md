# Ajustes do pipeline NEBLI — achados da corrida histo-11 (2026-07-07)

Lista honesta do que travou/atritou ao gerar o resumo de Tecido Linfoide + avaliar a busca de cards. Para a sessão de tuning. Ordenado por impacto.

## A. Problemas que TRAVARAM (bloqueio real, custaram retrabalho)

1. **`#questao-ce` — doc contraditória. [ALTO]**
   `TEMPLATE_API.md` mostra o exemplo com conteúdo cru `([...], [...], ...)`; o helper real e o `ERROS.md` erro 5 exigem pares `(("I", [...]), ("II", [...]))`. Segui o API → `verificar_gabarito_resumo` leu "0 itens" → 10 erros bloqueantes → reescrevi a E2 inteira. **Fix:** corrigir o exemplo do `TEMPLATE_API.md` para o formato de pares (fonte única de verdade), ou fazer o helper aceitar os dois.

2. **Paridade estourou na 1ª passada (8/20 MC longas demais). [ALTO]**
   Escrevi as corretas no comprimento natural (~31-34 palavras) e as distratoras saíram ~23-26 → ratio 1.3-1.43. Tive de alongar distratoras de 9 questões. A "ordem invertida" (distratora primeiro) está na regra, mas nada no fluxo me força a segui-la. **Fix:** (a) um "orçamento de palavras" explícito no momento de redigir (correta ≤ maior distratora); (b) idealmente um script `paridade_fix.py` que, dado etapa2, sugere quais distratoras alongar e em quantas palavras, ANTES do precompile.

3. **`buscar_tags_lote.py` — recall quebrado em termos EN multi-palavra. [ALTO — é o coração da busca de cards]**
   Tokeniza "natural killer cell" em tokens soltos e casa ruído (`ankle`, `Frank-Starling`, `X-linked palsy`). Declarou **20/24 conceitos como LACUNA** quando a cobertura real (lendo o texto dos cards) é **87%**. O gargalo de recall está na ferramenta, não no deck. **Fix:** ver seção D — é o item que mais rende pro objetivo de reter conteúdo.

## B. Problemas que geraram RUÍDO (não travaram, mas confundem/mascaram)

4. **`auditar_pdf.py` conta palavras da E1 errado. [MÉDIO]**
   Reportou "1035 palavras (miolo curto)" quando a E1 real tem ~4.400. A detecção de fronteira E1↔Resumindo está quebrada. Risco: warning falso agora, mas pode MASCARAR uma E1 genuinamente curta no futuro. **Fix:** corrigir o recorte de páginas da E1 (usar marcadores de etapa, não heurística de texto).

5. **`auditar_pdf_visual.py` — 2 falsos positivos recorrentes. [MÉDIO]**
   (a) Marca os `#mini-resumo` como "banner de resumindo no corpo" (págs 5/7/11). (b) Diz "helpers de cor faltando: Consolidação/Integração/Aplicação" quando os badges ESTÃO coloridos. Ruído que treina a gente a ignorar o auditor. **Fix:** distinguir `#mini-resumo` de `#resumindo-page`; detectar a cor pelo badge, não por string de header.

6. **`verificar_gabarito_resumo.py` ignora `--tema-card` e infere `tema-cards/`. [BAIXO]**
   Tive de copiar o YAML pra `arquivos-trabalho/tema-cards/`. Agora o tema card vive em 2 lugares (risco de drift). **Fix:** respeitar a flag; ou padronizar 1 diretório só.

7. **Header desincronizado na página do gabarito. [BAIXO/cosmético]**
   O gabarito (última seção) mostra header "ETAPA 3 — 5 DISCURSIVAS" com título "Gabarito — Etapa 2". **Fix:** setar o state da etapa na página do gabarito.

## C. Atritos de ingestão/plumbing

8. **Read de PDF depende de `pdftoppm` (ausente no ambiente). [BAIXO]**
   Não consegui `Read` o PDF do slide direto; usei `extrair_slides.py` + PyMuPDF. Funciona, mas atrasa a leitura inicial. **Fix:** documentar que a leitura de slide é sempre via extrair_slides + fitz, ou instalar poppler.

9. **Caminho de upload com UUID longo → erro de digitação. [BAIXO]**
   Errei o UUID na 1ª tentativa. **Fix:** um helper `achar_upload.py "<palavra>"` que resolve o path do upload mais recente por palavra-chave.

10. **Tema Card duplicado (.md rico + .yml). [MÉDIO — dívida de design]**
    Escrevo um `.md` didático (Seções A-E) E um `.yml` separado pro `gerar_main`. Dois artefatos, redundância parcial, drift. **Fix:** ou gerar o `.yml` a partir do `.md` (frontmatter), ou o `gerar_main` ler o `.md`.

11. **`gerar_checklist.py` semeia só termo-notas. [MÉDIO — afeta a busca de cards]**
    Semeou 16 conceitos, todos footnotes; faltaram os conceitos centrais (linfonodo, baço, zonas B/T, polpas). Enriqueci à mão pra 24. **Fix:** o seeder deveria puxar também os subtópicos da Seção B do Tema Card, não só os `#termo-nota`.

## D. Ideias grandes para a busca de cards (o TODO de reter a longo prazo)

12. **Reescrever a camada 1 de recall.** Para termos EN multi-palavra: exigir match de **frase** ou ≥2 tokens contíguos, não token isolado. Rankear por especificidade da tag, não por contagem bruta. Isso sozinho conserta o item 3.

13. **Pivô "subárvore-âncora → texto do card" como caminho primário.** Para aulas de histologia/anatomia, a verdade veio de `extrair_cards` de uma subárvore (`Lymphoid_Structures`), lendo o TEXTO — não de buscar tag por conceito. Proposta: adicionar ao `blueprint-step1.md` uma coluna **"subárvore-âncora AnKing"** por slug (ex.: histo-11 → `Immunology::01_Lymphoid_Structures` + B&B `Lymph_Nodes_and_Spleen`). O pipeline extrai a subárvore inteira e a matriz conceito×card roda sobre o texto real.

14. **"Modo histologia" no pipeline de cards.** O AnKing Step 1 cobre a FUNÇÃO dos órgãos (zonas, polpas, seleção T) mas NÃO a leitura de lâmina (seio subcapsular, barreira hematotímica, Billroth nomeado, arranjos frouxo/denso/nodular). Reconhecer isso e rotear esses conceitos histológicos direto pra **PENDENTE-GERADO** (cloze NEBLI da E1) numa sessão de calibração, sem fingir que há card Step 1.

15. **Gerar os cloze NEBLI da E1 (o TODO real de retenção).** Hoje o pipeline PARA em "achar os cards do AnKing". O que falta pra reter de verdade: a máquina de gerar cloze NEBLI a partir da E1 (regra `calibrar-antes-de-gerar-cards` — destilar o padrão de cards reais primeiro, validar, só então gerar). As 3 LACUNAS + PARCIAIS histológicas desta aula são o caso de teste natural.

16. **Prova de cobertura como gate visível.** `verificar_cobertura_anking.py` deveria emitir a linha X/Y COBERTO pro `_INDEX.md` automaticamente (hoje montei a matriz à mão). Fechar o loop: toda aula com sua % de cobertura e fila pendente-gerado.

## E. Ideias para E1-E3 (detalhes finos)

17. **Densidade por PARTE auditável de verdade.** A regra 14 pede desvio ≤±20% entre PARTES, mas eu reporto "no olho". Um contador de palavras por PARTE (fácil, regex nos `#parte-title`) fecharia isso como número.

18. **Cobertura E1→E2 (≥2 questões/subtópico) sem tabela manual.** É diretriz auditável hoje; um mapeador semântico leve (ou até manual estruturado no Tema Card) evitaria subtópico órfão.

19. **`#mini-resumo` vs Resumindo — ícone/estilo distinto.** Além de confundir o auditor (item 5), visualmente o mini-resumo e o banner Resumindo competem. Talvez diferenciar mais.

20. **Checklist de "diagnóstico diferencial" como padrão para histologia.** Esta aula rendeu muito com a tríade "uma estrutura → um órgão". Vale virar um gesto recomendado no EXEMPLARES para toda aula de histologia de órgão (timo/linfonodo/baço; ou córtex renal/medular; etc.).

---

**Já aplicado nesta corrida (não precisa refazer):**
- Compactação virou passo explícito do `/resumo` (passo 9) — sidecar leve automático.
- Mapa de Confusões do histo-11 preenchido (estava vazio).
- Blueprint já marca histo-11 como ALTO — bateu com a densidade real.
