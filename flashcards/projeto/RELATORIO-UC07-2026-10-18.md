# UC07 / Kenhub — relatório de 18/10/2026: como estamos e como fazer em massa

## Onde estamos

- **15 das 51 unidades do cronograma da UC07 já estão instaladas no Anki** (1.147 notas), dessuspensas, com bandeira por cor, todas com os gates duros aprovados (PRÉ, leitura do Anki e renderização PC + celular do deck inteiro). A 16 está com a curadoria pronta (78 notas) e as 17–19 estão coletadas. Faltam 32 unidades.
- Ordem seguida: o cronograma da UC07 (Turma B): 1–2 (SN), 3–9 (medula e vias), 10–12 (tronco e núcleos), 13–19 (nervos cranianos), depois cerebelo, diencéfalo, telencéfalo, irrigação, SNA, meninges/líquor, cortes, límbico, córtex.
- Cada unidade = **estruturas do quiz** (um card do Kenhub por figura) + **texto do quiz** (cards de texto no tipo AnKing) + AnKing traduzido + AnatoKing/Netter só quando a seta é evidente ou o Kenhub não tem figura.
- Revisão card a card registrada (`--revisado`) só nas unidades 3 e tronco; nas demais vi a maioria das folhas de contato, mas **o registro formal ainda está pendente** (painel mostra “AGUARDANDO REVISÃO”).

## O que o pipeline garante hoje (gates duros)

Cobertura 100% das estruturas e de todo o texto de estudo do quiz; Kenhub sempre; card do Kenhub = figura com o destaque verde + seta (sem IO), nome na ponta da seta; cards de texto no tipo de nota do AnKing (clone fiel), sujeito em negrito, cloze curto e só no termo central, figura no Extra, termo técnico explicado; tradução oficial (Kenhub PT, Machado, Moore); mesma estrutura em sequência e só uma bandeira verde por estrutura; AnatoKing só com seta evidente; nada de fonte em texto; ids únicos entre unidades; comentário em toda nota; gravação em lote, sem sync, sem regravar a mesma unidade em < 6 h. Cada feedback seu tem gate + caso ruim testado (`./kenhub-deck --painel`).

## O que ainda não sei / limites

- **As 17 questões de texto do quiz** só aparecem se eu iniciar o quiz na sua conta (não fiz). Cobri todo o texto de estudo da unidade (objetivos, parágrafos, legendas do atlas, tabela-resumo). Se você me mostrar uma questão de texto, confiro se esse critério cobre as mesmas.
- Os textos dos cards de texto são **traduções minhas** (o Kenhub não tem a página em português); só os termos são verificados em fonte oficial. Vale você bater o olho nos que achar estranhos (comentário no card, que eu corrijo e generalizo).
- **Sync com a nuvem do Anki pendente** (de propósito, para não atrapalhar quem estuda): arquivo `arquivos-trabalho/ANKI-SYNC-PENDENTE`.

## Como fazer o resto em massa sem perder qualidade

1. **Esteira em lotes de 4–5 unidades** (por data de aula), uma unidade por vez dentro do lote:
   - A. **Coleta automática** (Kenhub, ritmo humano, ~4 min/unidade): estruturas, imagens, texto e figuras do atlas. Sem Anki.
   - B. **Curadoria** (a parte de julgamento): cor por estrutura, AnKing a traduzir (candidatos já pré-checados), cards de texto, `cobre_texto`. Sem Anki. Os gates PRÉ são o juiz: a unidade só avança quando passam. **Hoje isso é o gargalo (~1 h por unidade)**; dá para paralelizar com subagentes (um por unidade, cada um rodando `--dry-run` até passar) — mas só com a sua autorização explícita (“use um workflow”), porque gasta mais.
   - C. **Gravação em lote** num horário que você escolher (você fora do Anki), sem sync; depois, um sync único quando você estiver ocioso.
   - D. **Olhar as folhas de contato** de cada unidade (80–230 cards) e só então `--revisado`. É a única etapa que não dá para automatizar; custa ~15–20 min por unidade.
2. **Controle de qualidade para não decair**: (a) toda correção sua vira gate (já é a regra); (b) amostra de 15% dos cards de texto lida por inteiro em cada lote; (c) acompanhar o nº de comentários seus por 100 cards (se subir, o lote para); (d) `RODADAS-UC07.md` registra o que melhorar a cada rodada.
3. **Melhorias que valem fazer antes de escalar**: pré-visualização offline das folhas (para olhar antes de gravar no Anki e regravar menos); glossário PT único e cadastro único de estruturas (evita repetir cards entre unidades); mais fontes de tradução (Gray/Dângelo por OCR).
4. **Estimativa honesta**: com a curadoria como hoje, ~1–1,5 h de trabalho por unidade + revisão visual; 32 unidades ≈ 40–60 h de trabalho do executor, ~3–4M tokens. Com subagentes em paralelo (4–5 por lote), cai para ~1–2 dias corridos, mantendo o mesmo conjunto de gates.

## Próximos passos já definidos

Instalar a 16; curar 17 (V1), 18 (V2), 19 (V3), depois 20–26 (facial, vestibulococlear, IX, X, XI, XII, via da gustação), cerebelo (27–28), diencéfalo (29–33), núcleos da base e telencéfalo (34–38), irrigação (39–42), SNA (43), meninges/líquor (44–46), cortes (47–48), límbico (49), córtex (50–51). Retomar por `./kenhub-deck --painel` e `ESTADO-ATUAL.md`.
