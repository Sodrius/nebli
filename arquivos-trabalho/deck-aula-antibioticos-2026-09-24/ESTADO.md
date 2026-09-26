# Estado da corrida — Antibióticos (24/09/2026, Claude)

Feito:
- Fontes: provas (`provas.txt`, 24 firmes), texto integral do slide (conector), escopo (`MAPA-ESCOPO.md`).
- Pool AnKing: 688 notas lidas (`pool.json`, `pool-lines.txt`) + segunda busca (lacunas) + MCAT.
- Seleção: `selection.py` — 130 AnKing Step + 1 MCAT; 4 NEBLI vivas de Genética/Fisiologia a **associar por tag** (sem duplicar). Rosa marcado no dicionário.
- Versos revisados (`verso-review.txt`): limpar Sketchy/Sketchy 2/Pixorize/Sketchy Extra; manter Bootcamp só linhas "Antibiotics:"; aparar Extra clínico de 1503683672620.

Autorais planejados (lacuna comprovada em AnKing + MCAT + Histology):
1. FQ resistance: gyrA point mutation. Imagem: slide (gyrA).
2. Carbapenemases (KPC, NDM). Extra: avibactam inibe KPC. Imagem: slide (β-lactamases).
3. MIC (µg/mL, diluição) × halo (mm, disco-difusão). Imagem: slide antibiograma.
4. MDR ≥3 classes × XDR 1–2 classes. Imagem: slide (Magiorakis).
5. Seletividade das sulfas: humanos obtêm folato da dieta (bacteriostáticas). Imagem: AnKing via do folato.
6. Antagonismo bacteriostático × β-lactâmico (precisa de célula em crescimento). Imagem: talvez nenhuma.
7. (rosa) Quimioterápico = sintético (quinolonas, sulfas) × antibiótico = produto microbiano. Imagem: slide.

Bloqueio: o conector Drive lê texto mas falha no download binário ("session expired"). Pedido a Davi para baixar via Chrome: slide (7,2 MB) e Trabulsi (68,8 MB, capítulo de antibióticos).

Próximo: prepare.py (plan.json) → apply (lock global `arquivos-trabalho/ANKI-ESCRITA.lock`, preset NEBLI, rosa=5, verde=3) → verify → nebli_novos.py --alinhar → REVISAO-DE-QUALIDADE.md → vídeos no chat.
