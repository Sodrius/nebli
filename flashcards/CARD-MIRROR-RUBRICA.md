# CARD-MIRROR — rubrica viva (o que faz um NEBLIcard parecer AnKing-nativo)

> Depósito do aprendizado do loop adversarial (`CARD-MIRROR-PLANO.md`). Cada linha nasceu de um **tell** que o discriminador `card-mirror` pegou e o refinador corrigiu. Isto é a spec de geração: NEBLIcard novo deve satisfazer tudo aqui **antes** de entrar. Alvo do linter futuro (`lint_neblicard.py`).

## Regras aprendidas (por rodada)

### Rodada 0 — baseline (2026-07-12)
- **[IMAGEM] Nunca usar slide de PowerPoint como imagem.** Slide colorido, 4:3, 3000×2250, com título em português = tell gritante. → Reusar a **imagem-mãe de um card AnKing irmão** do mesmo tema (nativa, inglês, ~1080px, leve, já no dispositivo). Fonte na ordem: outro card AnKing > internet limpa > recorte de slide (último recurso, resize p/ ~1080px). *Também conserta o lag: imagem já cacheada não baixa.*
- **[IDIOMA] Corpo do card em inglês.** AnKing é inglês; português no Text/Extra denuncia na hora.
- **[MODELO] Usar o note type AnKingOverhaul.** Herda a ergonomia visual (cor do cloze, reveal do Extra, responsividade) idêntica aos 500M de cards validados. Modelo NEBLI genérico tem CSS/tamanho diferente = tell.
- **[SELO] O selo `❖ NEBLIcard` é a ÚNICA marca permitida.** Discreto, gold mudo, rodapé do verso. Fora dele, zero diferença de manufatura.

### Rodada 1 (2026-07-12) — 5/5 pegos, conf ~85%, veredito distinguível
Tells estruturais fatais corrigidos:
- **[REFERÊNCIA] Nunca citar banca/curso no corpo.** "FMUSP P2/2023", "taught in the course", "classic yields taught" = assinatura autoral imediata. A proveniência de prova vive na tag/curado.json, nunca no card visível.
- **[CRÉDITO] Reusar a imagem de irmão implica herdar o crédito dela.** AnKing carrega "Photo credit: Image licensed by Physeo…". Card com imagem Physeo mas SEM o crédito = híbrido denunciável → adicionei o crédito real (a imagem é Physeo, então blenda e é honesto).
- **[MARCAS] Sem travessão "—", aspas curvas "" nem reticências.** São assinatura de prosa autoral. Usar pontuação reta.

### Rodada 2 (2026-07-12) — 5/5 pegos, conf ~80%, "só a textura do verso denuncia"
- **[VOZ — a regra-mãe] O Extra é ANOTAÇÃO, não EXPLICAÇÃO. Card ≠ E1.** O tell que sobreviveu a tudo foi a voz: prosa de monitor com conectivos causais ("The −2 comes from…", "hence the…", "It only describes…") vs. o fragmento nominal telegráfico do AnKing ("Carnitine acyltransferase-2 (CAT2)", "e.g., ALT or AST"). Reescrever todo Extra como fragmento: nomes, setas →, ponto-e-vírgula, sem oração completa nem conectivo. É o reflexo mais difícil de quebrar porque a voz de monitor é a voz canônica da E1.

### Rodada 3 (2026-07-12) — ≈ indistinguível: 2 falsos-positivos, conf ~65%, "chute informado"
- O discriminador passou a **errar cards AnKing reais** (chamou 2 de vazio-Extra de "NEBLI minimalista") e declarou chute nos meus de lipídeo. Convergência atingida para os eixos manejáveis.
- **Resíduo aceito (inerente ao conteúdo):** o verso de contagem de ATP (#10) lista números que o AnKing não carda — não há como escondê-lo sem perder o fato FMUSP. Fica.
- **Resíduo menor não perseguido:** o par de aminoácidos divide a mesma imagem Sketchy (o discriminador leu como "par autoral"), mas cards AnKing também compartilham imagem — over-fitting ao discriminador não valeria a pena.

## Checklist de conformidade (estado atual)
Um NEBLIcard passa se:
- [ ] Imagem = card AnKing irmão (ou limpa EN ~1080px); nunca slide PT; peso leve.
- [ ] Text e Extra em inglês.
- [ ] Note type = AnKingOverhaul.
- [ ] Cloze single, branco de ~1–3 palavras no token de maior valor (não oração inteira).
- [ ] Frente ~10–20 palavras; a frase dá a pista de recuperação sem entregar o branco.
- [ ] Extra = **fragmento telegráfico** (nomes, →, ponto-e-vírgula), NÃO prosa de monitor com conectivos. Card ≠ E1.
- [ ] Sem travessão "—", aspas curvas "" ou reticências … (assinatura de prosa autoral).
- [ ] Sem referência a banca/curso no corpo ("FMUSP", "taught in the course"); proveniência só na tag/curado.json.
- [ ] Se reusa imagem de card irmão, herda o crédito dela ("Photo credit: …") para não virar híbrido.
- [ ] Só o selo `❖ NEBLIcard` distingue; tag `NEBLI::gerado` para auditoria.

## Métrica de convergência (loop 2026-07-12, aminoácidos+lipídeos)
| Rodada | NEBLI pegos | Conf. média | Falsos-positivos | Veredito |
|---|---|---|---|---|
| 1 | 5/5 | ~85% | 0 | distinguível (tells estruturais) |
| 2 | 5/5 | ~80% | 0 | distinguível (só o verso) |
| 3 | 5/5 (chute) | ~65% | 2 | ≈ indistinguível (resíduo inerente ao conteúdo) |
