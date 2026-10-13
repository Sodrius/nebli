# Revisão de qualidade — Digestão e absorção dos nutrientes (UC08 P2, Fisiologia)

**Run:** `uc08-fi05-20261002a` (Claude, 02/10/2026), piloto do pipeline E1 + deck, refeito do zero (o deck de 29/09 tinha sido apagado por Davi). Deck `NEBLI::UC08::P2::Fisiologia::Digestão e absorção dos nutrientes`. Critérios: MEMORY + FEEDBACKS até F-20261002-CLAUDE-03. Sem revisão de outra IA.

## Fontes
| Família | Estado | O que foi feito |
|---|---|---|
| Material docente | consultada | `Aula-3_MED_2026.pdf` (Drive `1njH73JxBBnxyXjclsBDk6-JuiXntNsKm`, sha256 `90ecb250…`), 12 lâminas, texto extraído e **todas vistas** como imagem |
| Demais aulas da P2 | não localizadas | As outras seis pastas da P2 continuam vazias em 02/10 (aulas de 19/10 em diante); aula de secreções não existe no Drive |
| Provas UC08 | não localizadas | Busca por título (UC8/UC08/Digest + prova/P1/P2/gabarito) vazia |
| Livro do curso (Aires) | **não consultado** | PDF de 92 MB inacessível pelo conector; nenhum livro de fisiologia local. E1 e cards foram conferidos contra os slides e contra o conteúdo dos cards AnKing (bloco Costanzo), não contra capítulo lido |
| Step do recorte | consultada | AnKing: bloco Costanzo GI 05 Digestion, First Aid (ferro, B12, vitaminas), buscas em `q.py` |
| Vídeos | não consultados | Nenhum vídeo assistido nem listado nesta corrida |

Pela regra Q020, livro ausente não foi tratado como bloqueio porque o deck anterior da mesma aula também foi instalado sem ele; fica como pendência declarada.

## Percurso da aula e cobertura (ordem dos slides)
| Slide | Bloco | Cobertura |
|---|---|---|
| 1 | Título | — |
| 2 | A. Epitélio absortivo | amplificação 3/10/20, água não agitada, via paracelular, delgado × grosso; vilosidades e pregas por cards já vivos |
| 3 | A. Jejuno | 1 card (mensagem do slide); dados do equinacosídeo fora |
| 4 | B. Carboidratos | amilase, distribuição da digestão do amido, produtos, 4 oligossacaridases, SGLT1/GLUT5/GLUT2, proporções, intolerância à lactose |
| 5 | C. Proteínas | pepsina e sua fração, CCK, zimogênios, enteropeptidase, tripsina, PepT1, aminoácidos, peptidases citosólicas, destino portal |
| 6 | D. Lipídios | lipases lingual e gástrica, CCK e bile, emulsificação, lipases, colipase, produtos, micelas, reesterificação, quilomícrons, linfa |
| 7 | E. Íons e água | 9 L/dia, 7,5 e 1,4 L, osmose, bomba Na⁺/K⁺, NHE3, ENaC, arraste, K⁺ |
| 8 | "Informações extras" | separador: slides 9–12 receberam mais azul/rosa |
| 9 | F. HCO₃⁻, ferro, cálcio | HCO₃⁻ (rosa), ferro completo (heme, Dcytb, DMT-1, ferritina, ferroportina, ferroxidase, transferrina, hepcidina, facilitadores e inibidores), cálcio (TRPV6, calbindina, Ca²⁺-ATPase, vitamina D) |
| 10 | G. Vitaminas | lipossolúveis × hidrossolúveis, K (K2, recém-nascido, varfarina), D (pele, fígado, rim), B12 (haptocorrina, proteases, FI, íleo, três causas de falha) |
| 11–12 | H. Via paracelular | proteínas da junção, claudinas 2/15, SGLT1 → MLCK |

Excluídos com motivo e fora do recorte: `plan.json` (`excluidos`, `fora_do_recorte`). Principal: secreções gástrica, pancreática e biliar ficam para a aula própria.

## Seleção e bandeiras
**Estado final após o delta de 02/10:** 92 notas novas / 106 cards (AnKing 64 notas / 76 cards; MCAT 2 / 3; autoral 26 / 27) + 9 notas já vivas associadas por tag. **38 verdes, 57 azuis, 11 rosas** nos novos; entre as associadas, 3 verdes e 6 azuis nesta aula.

- **Verde (exemplos):** `sglt1`, `glut2`, `enteropeptidase`, `tripsina-todas`, `micelas-borda`, `quilomicrons`, `porta` (portal × linfa), `bomba` (Na⁺/K⁺-ATPase como motor), `agua-osmose`, `ferro-fe2`, `ferroportina`, `hepcidina`, `b12-proteases`, `b12-ileo`. Critério: transportador ou princípio que volta em rim, endócrino, hematologia.
- **Azul (exemplos):** números e listas do professor (`amplificacao`, `amido-estomago`, `pepsina-fracao`, `volume-total`), zimogênios individuais, `nhe3`, `enac`, `colipase`, `mlck`. Necessários para a prova, sem valor duradouro próprio.
- **Rosa (exemplos):** `agua-nao-agitada`, `proporcao-monos`, `hco3`, `trpv6`, `ca-atpase`, `claudinas`, `k-colon`, `enteropeptidase-def`. Slides de "informações extras" ou detalhe de figura.
- **Casos limítrofes:** `lactase-diarreia` entrou verde como a única clínica do bloco de carboidratos (encaixe direto com a borda em escova); `k-colon` não está no slide e entrou rosa pelo contraste; regulação da hepcidina por inflamação/hipóxia ficou fora.
- **Comparação com outras aulas da UC08:** as sete aulas da P1 têm 37–76 cards e 15–36 verdes; esta tem 106 e 38. É a aula mais densa da UC (12 slides, cada um um esquema completo). Carga verde única agregada da UC08: 208 em 510 cards.
- **Ordem das fontes e autoria (27 de 106 cards, 25%):** a primeira versão instalada tinha 30 autorais e **a busca nos acervos externos não tinha sido feita**, embora o plano dissesse que sim. Davi lembrou a ordem AnKing → outros → MCAT/AnatoKing/Dope → autoral; a busca externa foi então executada (`busca/ext.txt`): 2 autorais deram lugar a cards MCAT (`mcat-jejuno-ileo`, `mcat-dissacaridases`) e 2 rosas de baixo ganho saíram (`proporcao-monos`, `ca-atpase`). Versão anterior em `plan-v1-instalado.json`. O restante continua acima de 20% porque as lacunas são conteúdo do professor que o AnKing não cobre (balanço hídrico, NHE3/ENaC intestinal, fatores de amplificação, colipase, claudinas, MLCK, percentuais).

## Autorais: método e teste cego
Cada autoral foi escrito por um agente a partir do alvo em português e de 3 espelhos AnKing (`author-briefs.json`, nids em `espelhos` no plano), e depois revisado por mim. Lint: 0 reprovações duras.

Teste cego **dentro da aula** (30 autorais × 30 AnKing do mesmo plano, só texto, juízes sem gabarito):

| Rodada | Autorais identificados | Acurácia | AUC |
|---|---|---|---|
| 1 (texto do redator) | 27/30 | 0,95 | 0,98 |
| 2 (após revisão; outros 30 AnKing, outro juiz) | 27/30 | 0,90 | 0,95 |

**O gate de indistinguibilidade não foi atingido nesta aula.** As pistas mudaram de natureza: na rodada 1, aberturas repetidas, Extras gêmeos e números com til; na 2, molde único "sujeito + verbo + nome oculto", Extra aritmético e ausência da sujeira de marcação dos AnKing. Os juízes declararam que o conteúdo (números e mecanismos de livro que o AnKing não tem) pesa na decisão e que receberam o CLAUDE.md do projeto no contexto. Nenhum autoral foi piorado para enganar o juiz. A decisão que vale é a de Davi estudando.

Correções de qualidade vindas dos juízes: `mlck` com o nome por extenso, `trpv6` com a isoforma, `jejuno` mais específico, `enac` sem "also".

## Pontos científicos a conferir (não resolvidos sem o livro)
- **Digestão do amido 3–5% / 75% / 25%** (slide 4): são os números da aula e estão no card `amido-estomago` e na E1, atribuídos à aula. Guyton dá 30–40% no estômago. Conflito registrado, não corrigido.
- **Pepsina 10–15%** (slide 5): Guyton dá 10–20%.
- **Calbindina D-28K** no Extra do card AnKing `calbindina`: a intestinal é a D-9K. Texto AnKing preservado.
- **Ferroxidase "in the plasma"** (AnKing): a hefestina é de membrana; preservado.

## Imagens
Autorais: 5 figuras AnKing reaproveitadas dos espelhos (amido → dextrinas, enterócito SGLT1/GLUT, peptídeos, lipídios, ciclo do ferro), **vistas** em folha de contato (`visual/sheet.png`), e 9 slides da aula como apoio no Extra. Créditos visíveis retirados de 12 cópias AnKing, com o texto original guardado em `credito_removido` no plano. **Não renderizei os cards no Anki**: a conferência foi de campos e mídia existente, não da aparência final.

## Ordem no Browser
`python3 -m nebli.ordem verificar … --plan plan.json`: **ok**, 101 notas com posição `fi05-NN` (inclusive as 9 associadas). Um recuo de slide avisado (posição 102, slide 11 depois do 12): a composição da junção foi posta antes das claudinas 2/15 de propósito. Coluna "Ordem da aula" corrigida para esta versão do Anki em 02/10; **ainda não vista por Davi na tela**.

## Tab
`resumo "tag:NEBLI::2026-uc08-fisiologia-05-digestao-absorcao-nutrientes"`: **atual 120, revisar 0, desatualizada 0, faltando 0** (106 novos + 14 cards das notas associadas). Lidas 4 explicações (`amido-estomago`, `mlck`, `hepcidina`, `mcat-dissacaridases`): seguem Base → Por quê → Na aula, sem erro encontrado. Tab não visto abrindo na tela.

## E1
`Digestão e absorção dos nutrientes - E1.pdf` (19 páginas: capa, Antes da aula, sumário, 14 de texto, Resumindo). 10 subtópicos, 5.841 palavras de miolo (alvo 4.800–5.500; aviso, não bloqueio), 3.4 mais longo que o alvo. `precompile-check --somente-e1`: 0 erros. Todas as 19 páginas vistas em folhas de contato (`e1-render/`). Figuras: 9 slides da aula. Fontes Merriweather/Montserrat; "α" cai em fonte de reserva (11 ocorrências). `auditar_pdf.py` não rodou (falta `pdftotext` neste Mac). **Não publicada no Drive**: o conector não envia PDF de 4 MB.

## Estados
Conteúdo revisado por amostra e pelos juízes: sim. Instalação: sim, readback sem problemas (`receipt.json`). Sync: solicitado pelo `escrita`, não conferido em outro aparelho. Pacote APKG e tradução: não feitos nesta corrida.
