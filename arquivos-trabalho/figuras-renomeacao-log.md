# Log de renomeação de scans em banco/figuras/

Sufixo `__` adicionado ao final do nome (antes da extensão) com os IDs das questões
do banco que aparecem fisicamente em cada página.

Convenções de sufixo:
- `__q0262-q0263` → questões q-0262 e q-0263 visíveis nessa página
- `__respostas` → página é só gabarito/cartão-resposta, sem enunciados
- `__novel` → contém questão que não existe no banco (não foi ingerida)
- `__cauda` → continuação visual da questão da página anterior (alternativas/imagem cortada)
- `__nobanco` → fonte do scan não tem nenhuma questão no banco
- `__indecifravel` → vision não conseguiu ler

## Renomeações aplicadas

| Arquivo antigo | Arquivo novo | Conteúdo identificado | Confiança |
|---|---|---|---|
| `PROVA_UC2_anatomia_P2_2023_p02.png` | `PROVA_UC2_anatomia_P2_2023_p02__q0262-q0263.png` | q-0262 (planos coronal/sagital/transversal) + q-0263 (cavidades, início) | alta |
| `PROVA_UC2_anatomia_P2_2023_p03.png` | `PROVA_UC2_anatomia_P2_2023_p03__q0263-novel.png` | q-0263 (cavidades, alternativas finais) + questão NOVA sobre figura abdominal (1-5) | alta |
| `PROVA_UC2_anatomia_P2_2023_p04.png` | `PROVA_UC2_anatomia_P2_2023_p04__novel-cauda.png` | cauda da questão abdominal de p03 (legenda "Posterior" + alternativas finais) | alta |
| `PROVA_UC2_bioquimica_P2_2023_p01.png` | `PROVA_UC2_bioquimica_P2_2023_p01__novel-q0264.png` | questao NOVA Krebs/AG (CE R:FVFVV) + q-0264 (cetogenese) | alta |
| `PROVA_UC2_bioquimica_P2_2023_p02.png` | `PROVA_UC2_bioquimica_P2_2023_p02__q0267-q0265.png` | q-0267 (NADPH lipogenese, R:I) + q-0265 (sintese AG 5 etapas) | alta |
| `PROVA_UC2_bioquimica_P2_2023_p04.png` | `PROVA_UC2_bioquimica_P2_2023_p04__novel-q0266-q0268.png` | novel radicais livres + q-0266 (G6PD/anemia) + q-0268 (NADPH/pentoses, R:I) | media |
| `PROVA_UC2_histologia_P2_2023_p02.png` | `PROVA_UC2_histologia_P2_2023_p02__novel-glandulas.png` | novel CE glandulas (R: A não marcada) | alta |
| `PROVA_UC2_histologia_P2_2023_p03.png` | `PROVA_UC2_histologia_P2_2023_p03__novel-epitelio-revestimento.png` | novel V/F epitelio revestimento (R: VFFVF) | alta |
| `PROVA_UC2_histologia_P2_2023_p06.png` | `PROVA_UC2_histologia_P2_2023_p06__novel-carcinoma-metastase.png` | novel V/F adiposo + MC carcinoma metastase (R: B) | alta |
| `PROVA_UC2_histologia_P2_2023_p07.png` | `PROVA_UC2_histologia_P2_2023_p07__novel-conjuntivo-frouxo-denso.png` | novel classifique tecido A=frouxo B=denso nao modelado | alta |
| `PROVA_UC2_histologia_P2_2023_p08.png` | `PROVA_UC2_histologia_P2_2023_p08__novel-frouxo-vs-denso.png` | novel laminas A vs TCD; R: frouxo + lamina A com B | alta |
| `PROVA_UC2_histologia_P2_2023_p09.png` | `PROVA_UC2_histologia_P2_2023_p09__novel-elastina-glandulas.png` | novel fibras R: Elastina + novel glandulas A vs B | alta |
| `PROVA_UC2_histologia_P2_2023_p10.png` | `PROVA_UC2_histologia_P2_2023_p10__novel-cauda-glandulas.png` | cauda V/F glandulas A acinos B endocrina | alta |
| `PROVA_UC2_histologia_P4_p02.png` | `PROVA_UC2_histologia_P4_p02__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p03.png` | `PROVA_UC2_histologia_P4_p03__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p04.png` | `PROVA_UC2_histologia_P4_p04__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p06.png` | `PROVA_UC2_histologia_P4_p06__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p07.png` | `PROVA_UC2_histologia_P4_p07__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p09.png` | `PROVA_UC2_histologia_P4_p09__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p10.png` | `PROVA_UC2_histologia_P4_p10__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p11.png` | `PROVA_UC2_histologia_P4_p11__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p12.png` | `PROVA_UC2_histologia_P4_p12__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| `PROVA_UC2_histologia_P4_p13.png` | `PROVA_UC2_histologia_P4_p13__nobanco-histo-P4.png` | fonte sem match no banco; conteudo histo P4 (musculo, tecido nervoso, etc) | media |
| | | NOTA: q-0276 (Michaelis-Menten) tem fonte PROVA_UC2_P2_online_turma108 mas NAO foi encontrada visualmente em p01-p05; possivelmente foi excluida do scan ou esta em pagina nao-numerada. | flag |
| `PROVA_UC2_P2_online_turma108_p01.png` | `PROVA_UC2_P2_online_turma108_p01__novel-conjuntivo-adiposo.png` | 5 novel: conjuntivo denso, lacunas, adiposo, fig A/B, fig classificar | alta |
| `PROVA_UC2_P2_online_turma108_p02.png` | `PROVA_UC2_P2_online_turma108_p02__novel-epitelio-glandulas.png` | V/F epitelio 5 itens + fig ABC glandulas exo/endo | alta |
| `PROVA_UC2_P2_online_turma108_p03.png` | `PROVA_UC2_P2_online_turma108_p03__novel-glandulas-epitelio.png` | fig A B glandulas + V/F + MC epitelio + MC conjuntivo | alta |
| `PROVA_UC2_P2_online_turma108_p04.png` | `PROVA_UC2_P2_online_turma108_p04__novel-revestimento.png` | V/F revestimento + figura V/F com A B | alta |
| `PROVA_UC2_P2_online_turma108_p05.png` | `PROVA_UC2_P2_online_turma108_p05__novel-carcinoma-adiposo.png` | carcinoma/metastase + glicosaminoglicanos + fig adiposo A B V/F | alta |
| `PROVA_UC2_P3_online_turma108_p01.png` | `PROVA_UC2_P3_online_turma108_p01__novel-musculo-laminas.png` | identifique tecidos musc liso/cardiaco + discos intercalares | alta |
| `PROVA_UC2_P3_online_turma108_p02.png` | `PROVA_UC2_P3_online_turma108_p02__novel-discos-intercalares-musculo.png` | MC discos intercalares + lamina musc esqueletico | alta |
| `PROVA_UC2_P3_online_turma108_p04.png` | `PROVA_UC2_P3_online_turma108_p04__q0189-q0275.png` | q-0189 (canal Havers, discursiva) + q-0275 (V/F osteoblastos/osteoclastos). NOTA: fontes WRONG no banco - apontam pra anatomia_P2_2023 em vez de aqui. | alta |
| `PROVA_UC2_P3_online_turma108_p05.png` | `PROVA_UC2_P3_online_turma108_p05__novel-osseo-ossificacao.png` | V/F tecidos osseos A vs B + ossificacao endocondral | alta |
| `PROVA_UC2_P3_online_turma108_p07.png` | `PROVA_UC2_P3_online_turma108_p07__novel-cartilaginoso.png` | V/F cartilaginoso + figura A B C MC | alta |
| `PROVA_UC2_P3_online_turma108_p08.png` | `PROVA_UC2_P3_online_turma108_p08__novel-anato-termos-planos.png` | termos orientacao + planos anatomicos + INCORRETA formas estudo | alta |
| `PROVA_UC2_P3_online_turma108_p12.png` | `PROVA_UC2_P3_online_turma108_p12__novel-bioq-curvas-glicogenio.png` | V/F curvas A B C bioq jejum (glicogenio, transaminases, FBPase) | alta |

> NOTA: q-0271 (embrio gastrulacao), q-0272 (caracteristicas musculos) e q-0278 (articulacoes) declaram fonte PROVA_UC2_P3_online_turma108 mas nao foram identificadas nas 7 paginas inspecionadas (p01,p02,p04,p05,p07,p08,p12). Podem estar em paginas faltantes (p03,p06,p09,p10,p11) que nao existem no scan, ou foram redigidas como sinteticas.
| `PROVA_UC2_P4_online_turma108_p01.png` | `PROVA_UC2_P4_online_turma108_p01__q0270-q0271.png` | q-0270 (V/F artéria/veia A B) + q-0271 (derivados ectoderme/mesoderme/endoderme) + embrio extra | alta |
| `PROVA_UC2_P4_online_turma108_p03.png` | `PROVA_UC2_P4_online_turma108_p03__novel-vasos-baco.png` | V/F vasos sang/linfaticos 5 itens + lamina baço | alta |
| `PROVA_UC2_P4_online_turma108_p04.png` | `PROVA_UC2_P4_online_turma108_p04__novel-timo-Hassall.png` | tecidos linfoides timo adulto + Hassall | alta |
| `PROVA_UC2_P4_online_turma108_p05.png` | `PROVA_UC2_P4_online_turma108_p05__novel-nervo-linfonodo-foliculo.png` | nervo + linfonodos errada + foliculos LH/ovulacao | alta |
| `PROVA_UC2_P4_online_turma108_p07.png` | `PROVA_UC2_P4_online_turma108_p07__novel-timo-vaso.png` | Timo (Hassall) + lamina vaso linfatico/sang | alta |
| `PROVA_UC2_P4_online_turma108_p08.png` | `PROVA_UC2_P4_online_turma108_p08__novel-neuronio-glia-vaso.png` | identifique neuronio+glia + V/F vaso A B C | alta |
| `PROVA_UC2_P4_online_turma108_p09.png` | `PROVA_UC2_P4_online_turma108_p09__novel-satelites-trofoblasto-notocorda.png` | cels satelites + sincicio/citotrofoblasto + notocorda | alta |
| `PROVA_UC2_P4_online_turma108_p11.png` | `PROVA_UC2_P4_online_turma108_p11__novel-snc-substancia-Hassall.png` | subst cinzenta/branca + Hassall | alta |
| `PROVA_UC2_P4_online_turma108_p12.png` | `PROVA_UC2_P4_online_turma108_p12__novel-vasos-blastocisto.png` | lamina arteria/capilar/linfatico + INCORRETA blastocisto | alta |
| `PROVA_UC2_P4_online_turma108_p13.png` | `PROVA_UC2_P4_online_turma108_p13__novel-trofoblasto-espermato-implantacao.png` | trofoblasto + espermatogenese + implantacao endometrial | alta |

> NOTA: q-0269 (arteria elastica vs muscular) e q-0279 (PFK-1) declaram fonte PROVA_UC2_P4_online_turma108 mas nao foram identificadas nas 10 paginas inspecionadas. Possivelmente fontes erradas no banco.

## UC1 — bloco marcado __nobanco (sem vision)

UC1 scans não têm questão no banco com campo `fonte:` que bata com seus prefixos. Marcação em bloco; vision detalhada pendente.

| Arquivo antigo | Arquivo novo |
|---|---|
| `PROVA_UC1_biocel_P3-v2_p01.png` | `PROVA_UC1_biocel_P3-v2_p01__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3-v2_p02.png` | `PROVA_UC1_biocel_P3-v2_p02__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3-v2_p03.png` | `PROVA_UC1_biocel_P3-v2_p03__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3-v2_p04.png` | `PROVA_UC1_biocel_P3-v2_p04__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3-v2_p05.png` | `PROVA_UC1_biocel_P3-v2_p05__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3_p01.png` | `PROVA_UC1_biocel_P3_p01__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3_p02.png` | `PROVA_UC1_biocel_P3_p02__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3_p03.png` | `PROVA_UC1_biocel_P3_p03__nobanco-UC1.png` |
| `PROVA_UC1_biocel_P3_p05.png` | `PROVA_UC1_biocel_P3_p05__nobanco-UC1.png` |
| `PROVA_UC1_bioquimica_P3-v2_p01.png` | `PROVA_UC1_bioquimica_P3-v2_p01__nobanco-UC1.png` |
| `PROVA_UC1_bioquimica_P3-v2_p05.png` | `PROVA_UC1_bioquimica_P3-v2_p05__nobanco-UC1.png` |
| `PROVA_UC1_bioquimica_P3-v2_p06.png` | `PROVA_UC1_bioquimica_P3-v2_p06__nobanco-UC1.png` |
| `PROVA_UC1_bioquimica_P3-v2_p07.png` | `PROVA_UC1_bioquimica_P3-v2_p07__nobanco-UC1.png` |
| `PROVA_UC1_bioquimica_P3_p07.png` | `PROVA_UC1_bioquimica_P3_p07__nobanco-UC1.png` |
| `PROVA_UC1_compilado_2023_p03.png` | `PROVA_UC1_compilado_2023_p03__nobanco-UC1.png` |
| `PROVA_UC1_compilado_2023_p05.png` | `PROVA_UC1_compilado_2023_p05__nobanco-UC1.png` |
| `PROVA_UC1_compilado_2023_p07.png` | `PROVA_UC1_compilado_2023_p07__nobanco-UC1.png` |
| `PROVA_UC1_compilado_2023_p10.png` | `PROVA_UC1_compilado_2023_p10__nobanco-UC1.png` |
| `PROVA_UC1_compilado_2023_p13.png` | `PROVA_UC1_compilado_2023_p13__nobanco-UC1.png` |
| `PROVA_UC1_fisiologia_cassola_p01.png` | `PROVA_UC1_fisiologia_cassola_p01__nobanco-UC1.png` |
| `PROVA_UC1_fisiologia_cassola_p06.png` | `PROVA_UC1_fisiologia_cassola_p06__nobanco-UC1.png` |
| `PROVA_UC1_fisiologia_cassola_p08.png` | `PROVA_UC1_fisiologia_cassola_p08__nobanco-UC1.png` |
| `PROVA_UC1_fisiologia_P2_turmas97-102-106_p06.png` | `PROVA_UC1_fisiologia_P2_turmas97-102-106_p06__nobanco-UC1.png` |
| `PROVA_UC1_fisiologia_P2_turmas97-102-106_p07.png` | `PROVA_UC1_fisiologia_P2_turmas97-102-106_p07__nobanco-UC1.png` |
| `PROVA_UC1_fisiologia_P2eP3_p11.png` | `PROVA_UC1_fisiologia_P2eP3_p11__nobanco-UC1.png` |
| `PROVA_UC1_P1_2005_TB_p02.png` | `PROVA_UC1_P1_2005_TB_p02__nobanco-UC1.png` |
| `PROVA_UC1_P1_2005_TB_p03.png` | `PROVA_UC1_P1_2005_TB_p03__nobanco-UC1.png` |
| `PROVA_UC1_P2_2008_aline-v3_p01.png` | `PROVA_UC1_P2_2008_aline-v3_p01__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados-v2_p01.png` | `PROVA_UC1_questoes-P1_enunciados-v2_p01__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados-v2_p02.png` | `PROVA_UC1_questoes-P1_enunciados-v2_p02__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados-v2_p03.png` | `PROVA_UC1_questoes-P1_enunciados-v2_p03__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados-v2_p04.png` | `PROVA_UC1_questoes-P1_enunciados-v2_p04__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados-v2_p06.png` | `PROVA_UC1_questoes-P1_enunciados-v2_p06__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados-v2_p09.png` | `PROVA_UC1_questoes-P1_enunciados-v2_p09__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados-v2_p10.png` | `PROVA_UC1_questoes-P1_enunciados-v2_p10__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados_p01.png` | `PROVA_UC1_questoes-P1_enunciados_p01__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados_p02.png` | `PROVA_UC1_questoes-P1_enunciados_p02__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados_p03.png` | `PROVA_UC1_questoes-P1_enunciados_p03__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados_p04.png` | `PROVA_UC1_questoes-P1_enunciados_p04__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados_p06.png` | `PROVA_UC1_questoes-P1_enunciados_p06__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_enunciados_p09.png` | `PROVA_UC1_questoes-P1_enunciados_p09__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_respostas_p01.png` | `PROVA_UC1_questoes-P1_respostas_p01__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_respostas_p03.png` | `PROVA_UC1_questoes-P1_respostas_p03__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_respostas_p04.png` | `PROVA_UC1_questoes-P1_respostas_p04__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_respostas_p06.png` | `PROVA_UC1_questoes-P1_respostas_p06__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_respostas_p10.png` | `PROVA_UC1_questoes-P1_respostas_p10__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_respostas_p12.png` | `PROVA_UC1_questoes-P1_respostas_p12__nobanco-UC1.png` |
| `PROVA_UC1_questoes-P1_respostas_p14.png` | `PROVA_UC1_questoes-P1_respostas_p14__nobanco-UC1.png` |

---

## Resumo final (2026-06-03)

| Categoria | Contagem | % do total |
|---|---:|---:|
| **Total scans processados** | 93 | 100% |
| Matches confirmados com banco (>=1 banco_id no sufixo) | 7 | 7.5% |
| Novel puro (questão visível, mas não está no banco) | 28 | 30.1% |
| `__nobanco-UC1` (UC1 em bloco, sem vision) | 48 | 51.6% |
| `__nobanco-histo-P4` (UC2 histo P4 sem fonte matching) | 10 | 10.8% |
| Sem sufixo (não renomeados) | 0 | 0% |

**11 questões do banco fisicamente localizadas em scans:**
q-0189, q-0262, q-0263, q-0264, q-0265, q-0266, q-0267, q-0268, q-0270, q-0271, q-0275.

## Auditoria — discrepâncias no campo `fonte:` do banco

Vários `fonte:` no banco apontam erradamente ou não foram encontrados nos scans:

| Questão | `fonte:` declarado | Realidade observada |
|---|---|---|
| q-0189 (canal de Havers, discursiva) | (vazia ou outra) | encontrada em `PROVA_UC2_P3_online_turma108_p04` |
| q-0275 (V/F osteoblastos) | `PROVA_UC2_anatomia_P2_2023` | encontrada em `PROVA_UC2_P3_online_turma108_p04` |
| q-0271 (derivados germinativos) | `PROVA_UC2_P3_online_turma108` | encontrada em `PROVA_UC2_P4_online_turma108_p01` |
| q-0276 (Michaelis-Menten) | `PROVA_UC2_P2_online_turma108` | NÃO ENCONTRADA nos 5 scans p01-p05 |
| q-0269 (artéria elástica vs muscular) | `PROVA_UC2_P4_online_turma108` | NÃO ENCONTRADA nas 10 páginas inspecionadas |
| q-0272 (tipos de músculo) | `PROVA_UC2_P3_online_turma108` | NÃO ENCONTRADA nas 7 páginas inspecionadas |
| q-0278 (articulações) | `PROVA_UC2_P3_online_turma108` | NÃO ENCONTRADA nas 7 páginas inspecionadas |
| q-0279 (PFK-1) | `PROVA_UC2_P4_online_turma108` | NÃO ENCONTRADA nas 10 páginas inspecionadas |
| q-0273, q-0274 (epitelial/conjuntivo) | `PROVA_UC2_histologia_P2_2023` | NÃO ENCONTRADAS — todas as 7 páginas eram NOVEL |

Hipóteses para essas discrepâncias:
1. Questões redigidas como sintéticas/representativas usando o nome de uma prova como "fonte temática" (não literal).
2. Páginas faltantes nos scans (p03, p06, p10, etc. — sequências têm gaps).
3. Fontes preenchidas durante ingestão sem confirmação visual.

## Limitações pendentes

- **UC1 (48 scans)**: marcados em bloco como `__nobanco-UC1`. Vision detalhada não foi feita para economizar tokens. Davi pode pedir numa próxima sessão.
- **UC2 histo P4 (10 scans)**: marcados como `__nobanco-histo-P4`. Conteúdo identificado em amostra (p02): tecido muscular + nervoso (SNC). Nenhum match com `fonte:` do banco.
- **Páginas faltantes**: muitas séries têm gaps (p03 missing, p06 missing, etc.) — não tenho como conferir se há questões nessas páginas.
