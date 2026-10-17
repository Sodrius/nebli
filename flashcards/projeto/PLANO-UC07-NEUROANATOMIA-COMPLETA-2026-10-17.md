# Plano — deck de neuroanatomia completo a partir do Kenhub, unidade por unidade (17/10/2026)

Pedido de Davi (F-20261017-CLAUDE-01/02/03): um deck por unidade do Kenhub, na ordem do Kenhub, `NEBLI::UC07::<módulo>::<submódulo>`, para
estudar neuroanatomia a longo prazo e saber de verdade. O piloto (tronco encefálico › visão geral e anatomia de superfície, 117 notas,
67/67 estruturas) foi aprovado: “é exatamente isso que quero”. Este plano replica o piloto 50 vezes, uma unidade por vez.
Regras e limites: [PLANO-UC07-KENHUB](PLANO-UC07-KENHUB-2026-10-17.md), MEMORY §2/§6/§15. Depois da neuro: outros temas de anatomia (nome do deck a decidir).

## Como rodar uma unidade (um comando, gates duros)

```
./kenhub-deck <slug-da-unidade> "<Módulo>" "<Submódulo>"      # na raiz do repo
```
O comando: sobe o navegador invisível do Kenhub (sessão de Davi) → coleta a unidade (estruturas, nomes PT/EN/latim, uma figura por
estrutura, ritmo humano) → busca nos acervos e gera `curadoria.rascunho.json` → **para** se a curadoria não está pronta → instala o deck
(dessuspenso, bandeiras, ordem do Kenhub) → lê o Anki de volta → **renderiza o deck inteiro** (PC e celular) e reprova o que renderiza mal.
Só termina com sucesso se TODOS os gates passarem; depois eu olho as folhas de contato antes de entregar.

### Gates duros (cada um nasceu de um feedback de Davi; feedback novo vira gate novo — MEMORY §15)
| Gate | O que reprova | Feedback |
|---|---|---|
| Cobertura | estrutura da unidade sem nenhum card planejado, ou sem card no deck instalado | 17/10-01 |
| Kenhub primeiro | estrutura com figura no Kenhub que não entra pelo Kenhub (exclusão só com motivo escrito) | 17/10-02 |
| Máscara | marcação verde da figura não totalmente coberta na frente do card | 17/10-02 |
| G1 frente só imagem | qualquer texto visível na frente do card do Kenhub | 17/10-02 |
| G2 nome sem rolar | nome em português fora da primeira tela (PC ou celular) no verso | 17/10-02 |
| G3 AnatoKing PT+EN | verso do AnatoKing sem o nome em português e em inglês | 17/10-02 |
| G4 imagens inteiras | imagem quebrada; figura que não cabe na tela; **nota de acervo com imagem ausente na mídia** (barrada antes de instalar) | 17/10-02 |
| G5 máscara esconde | verde visível na frente / marcação ausente no verso | 17/10-02 |
| G6 deck todo | nem todos os cards renderizados (nunca passa no vazio) | 17/10-02 |
| Nome em PT | nome em português igual ao inglês sem liberação (`nome_igual_ok`) | 17/10-02 |
| Anki livre | gravação recusada por janela de edição aberta: avisa antes de escrever, retoma depois | 17/10-03 |
| Dessuspenso + bandeira | card suspenso ou com bandeira diferente da cor planejada | 17/10-01/02 |

## Formato do card (v2, 17/10 noite — F-20261017-CLAUDE-04)
- **Figura (seta + IO)**: frente = figura com a estrutura mascarada, seta amarela até ela e “?”; verso = nome em português no topo e escrito na figura no lugar do “?”. Fontes: Kenhub (máscara no verde), Netter (rótulo coberto; seta na linha-guia), AnKing (máscara no “ID”), níveis do tronco (figura sem legenda; a legendada no verso).
- **Cloze**: só o nome, em português; AnatoKing com modelo (seta vermelha) e peça à vista, sem botões; AnKing conceitual traduzido com as mesmas lacunas.
- Toda nota com campo de comentário. Ver o painel (`./kenhub-deck --painel`) para os gates vigentes.

## Pesquisa (17/10): como fazer seta + IO e decks de anatomia com menos atrito
- Não existe add-on de **seta** para oclusão de imagem: o IO nativo do Anki tem retângulo, elipse e polígono; o autor do Image Occlusion Enhanced citou setas como plano, não lançado. Estudantes de anatomia fazem “cards de seta” com a seta desenhada na figura — é o que o pipeline gera automaticamente ([fórum do Anki](https://forums.ankiweb.net/t/image-occlusion-new-feature-concept/45229); [Image Occlusion Enhanced](https://github.com/Glutanimate/image-occlusion-2-enhanced)).
- Guias de estudo recomendam IO com **uma estrutura por card** (“hide all, guess one”) ([MedSchoolCoach](https://www.medschoolcoach.com/resource/how-to-use-anki-for-med-students?hsLang=en)); um post do r/medicalschoolanki aponta o excesso de notas do IO em diagramas grandes ([snapshot](https://reddit.sentinel-team.org/posts/1q3sh0z/snapshots/2026-01-10T01%3A31%3A03.63275Z)) — aqui resolvido por usar uma figura por estrutura (Kenhub já traz isso).
- Menos atrito daqui em diante: curadoria em rascunho automático; gates que reprovam antes de escrever; reconciliação no lugar (feedback corrige o deck sem perder histórico); painel de sessão; renderização inteira com folhas para olhar.

## Ordem de geração = cronograma da UC07, Turma B (F-20261017-CLAUDE-05)

Fonte: `Cronograma 2026 — UC07 — Sistema Nervoso I — Turma B.pdf` (Drive, `Não compartilhar/Menores/Cronogramas`). A “planilha mestra” é um atalho do Google Sheets que não abre daqui; se a ordem dela divergir do PDF, vale a planilha (Davi avisa).

| Ordem | Aula (cronograma) | # | Módulo (deck) | Submódulo (deck) | Slug Kenhub | Estruturas | Exerc. identificação | Estado |
|---|---|---|---|---|---|---|---|---|
| 1 | 13/10 · Construção morfofuncional do SN (Gerson) | 1 | Introdução ao sistema nervoso | Sistema nervoso central: introdução ao encéfalo | `basic-anatomy-of-the-brain` | 18 | 17 | **ENTREGUE 17/10** (31 notas) |
| 2 | 13/10 · Construção morfofuncional do SN (Gerson) | 2 | Introdução ao sistema nervoso | Sistema nervoso periférico: nervos, gânglios e plexos | `peripheral-nervous-system-nerves-ganglia-and-plexuses` | 22 | 23 | **ENTREGUE 17/10** (26 notas) |
| 3 | 14/10 · Medula espinal, plexos, nervos (Jácomo) | 29 | Medula espinal | Topografia e morfologia da medula espinal | `spinal-cord-in-situ` | 44 | 54 | curadoria pronta (56 notas, gates pré ok); **falta instalar** — Anki com janela de edição aberta |
| 4 | 14/10 · Medula espinal, plexos, nervos (Jácomo) | 30 | Medula espinal | Meninges espinais e raízes nervosas | `spinal-membranes-and-nerve-roots` | 14 | 14 | curadoria pronta (20 notas, gates pré ok); **falta instalar** |
| 5 | 14/10 · Medula espinal, plexos, nervos (Jácomo) | 31 | Medula espinal | Morfologia interna da medula espinal | `anatomy-spinal-cord-cross-section` | 46 | 46 | a fazer |
| 6 | 14/10 · Medula espinal, plexos, nervos (Jácomo) | 32 | Medula espinal | Nervos espinais | `anatomy-vertebral-column` | 20 | 19 | a fazer |
| 7 | 14/10 · Medula espinal, plexos, nervos (Jácomo) | 50 | Sistema nervoso periférico e autônomo | Dermátomos e miótomos | `anatomy-pns-dermatomes` | 30 | 46 | a fazer |
| 8 | 14/10 · Medula espinal, plexos, nervos (Jácomo) | 34 | Vias neurais | Tratos piramidais | `pyramidal-tracts` | 24 | 24 | a fazer |
| 9 | 14/10 · Medula espinal, plexos, nervos (Jácomo) | 35 | Vias neurais | Via coluna posterior–lemnisco medial | `posterior-column-medial-lemniscus-pathway` | 22 | 22 | a fazer |
| 10 | 14/10 · Tronco encefálico (Jácomo) | 20 | Tronco encefálico | Visão geral e anatomia de superfície | `brainstem-and-related-structures` | 67 | 68 | **ENTREGUE 17/10** |
| 11 | 14/10 · Tronco encefálico (Jácomo) | 21 | Tronco encefálico | Bulbo (anatomia interna) | `medulla-hypoglossal-level` | 29 | 30 | a fazer |
| 12 | 14/10 · Tronco encefálico (Jácomo) | 22 | Tronco encefálico | Núcleos dos nervos cranianos | `the-cranial-nerve-nuclei` | 33 | 57 | a fazer |
| 13 | 14/10 · Nervos cranianos (Jácomo) | 37 | Nervos cranianos | Os 12 nervos cranianos | `overview-of-cranial-nerves` | 13 | 12 | a fazer |
| 14 | 14/10 · Nervos cranianos (Jácomo) | 38 | Nervos cranianos | Nervo olfatório (I) | `the-olfactory-nerve` | 32 | 35 | a fazer |
| 15 | 14/10 · Nervos cranianos (Jácomo) | 39 | Nervos cranianos | Nervo óptico (II) | `the-optic-nerve` | 9 | 9 | a fazer |
| 16 | 14/10 · Nervos cranianos (Jácomo) | 40 | Nervos cranianos | Nervos oculomotor, troclear e abducente (III, IV, VI) | `the-oculomotor-trochlear-and-abducens-nerves` | 12 | 12 | a fazer |
| 17 | 14/10 · Nervos cranianos (Jácomo) | 41 | Nervos cranianos | Nervo oftálmico (V1) | `the-ophthalmic-nerve` | 19 | 19 | a fazer |
| 18 | 14/10 · Nervos cranianos (Jácomo) | 42 | Nervos cranianos | Nervo maxilar (V2) | `the-maxillary-nerve` | 18 | 18 | a fazer |
| 19 | 14/10 · Nervos cranianos (Jácomo) | 43 | Nervos cranianos | Nervo mandibular (V3) | `the-mandibular-nerve` | 28 | 28 | a fazer |
| 20 | 14/10 · Nervos cranianos (Jácomo) | 44 | Nervos cranianos | Nervo facial (VII) | `course-and-branches-of-facial-nerve` | 27 | 26 | a fazer |
| 21 | 14/10 · Nervos cranianos (Jácomo) | 45 | Nervos cranianos | Nervo vestibulococlear (VIII) | `course-and-branches-of-vestibulocochlear-nerve` | 19 | 19 | a fazer |
| 22 | 14/10 · Nervos cranianos (Jácomo) | 46 | Nervos cranianos | Nervo glossofaríngeo (IX) | `branches-and-nuclei-of-ninth-cranial-nerve` | 50 | 50 | a fazer |
| 23 | 14/10 · Nervos cranianos (Jácomo) | 47 | Nervos cranianos | Nervo vago (X) | `course-and-branches-of-vagus-nerve` | 31 | 32 | a fazer |
| 24 | 14/10 · Nervos cranianos (Jácomo) | 48 | Nervos cranianos | Nervo acessório (XI) | `course-of-accessory-nerve` | 15 | 15 | a fazer |
| 25 | 14/10 · Nervos cranianos (Jácomo) | 49 | Nervos cranianos | Nervo hipoglosso (XII) | `course-of-hypoglossal-nerve` | 17 | 17 | a fazer |
| 26 | 14/10 · Nervos cranianos (Jácomo) | 36 | Vias neurais | Via da gustação | `anatomy-of-taste-patway` | 29 | 29 | a fazer |
| 27 | 14/10 · Cerebelo (Jácomo) | 18 | Cerebelo | Córtex cerebelar | `structure-of-cerebellum` | 35 | 35 | a fazer |
| 28 | 14/10 · Cerebelo (Jácomo) | 19 | Cerebelo | Núcleos do cerebelo | `cerebellar-nuclei` | 16 | 16 | a fazer |
| 29 | 27/10 · Diencéfalo (Jácomo) | 13 | Estruturas subcorticais | Visão geral do diencéfalo | `diencephalon` | 17 | 17 | a fazer |
| 30 | 27/10 · Diencéfalo (Jácomo) | 14 | Estruturas subcorticais | Tálamo | `thalamus-and-related-structures` | 23 | 23 | a fazer |
| 31 | 27/10 · Diencéfalo (Jácomo) | 15 | Estruturas subcorticais | Núcleos do tálamo | `thalamic-nuclei` | 17 | 17 | a fazer |
| 32 | 27/10 · Diencéfalo (Jácomo) | 16 | Estruturas subcorticais | Hipotálamo | `anatomy-hypothalamus` | 25 | 25 | a fazer |
| 33 | 27/10 · Diencéfalo (Jácomo) | 17 | Estruturas subcorticais | Hipófise | `anatomy-pituitary-gland` | 32 | 32 | a fazer |
| 34 | 27/10 · Núcleos da base e telencéfalo (Jácomo) | 10 | Estruturas subcorticais | Núcleos da base | `anatomy-basal-ganglia` | 20 | 20 | a fazer |
| 35 | 27/10 · Núcleos da base e telencéfalo (Jácomo) | 3 | Telencéfalo e córtex cerebral | Visão geral do cérebro | `overview-of-the-cerebrum` | 23 | 22 | a fazer |
| 36 | 27/10 · Núcleos da base e telencéfalo (Jácomo) | 4 | Telencéfalo e córtex cerebral | Vista lateral do encéfalo | `lateral-views-of-the-brain` | 36 | 36 | a fazer |
| 37 | 27/10 · Núcleos da base e telencéfalo (Jácomo) | 5 | Telencéfalo e córtex cerebral | Vista medial do encéfalo | `medial-view-of-the-brain` | 45 | 45 | a fazer |
| 38 | 27/10 · Núcleos da base e telencéfalo (Jácomo) | 6 | Telencéfalo e córtex cerebral | Vista inferior do encéfalo | `basal-view-of-the-brain` | 41 | 41 | a fazer |
| 39 | 27/10 · Irrigação do SNC (Jácomo) | 26 | Vascularização do encéfalo | Artérias do encéfalo | `arteries-of-brain` | 42 | 49 | a fazer |
| 40 | 27/10 · Irrigação do SNC (Jácomo) | 27 | Vascularização do encéfalo | Veias do encéfalo | `the-superficial-veins-of-the-brain` | 43 | 43 | a fazer |
| 41 | 27/10 · Irrigação do SNC (Jácomo) | 28 | Vascularização do encéfalo | Seios venosos da dura-máter | `the-dural-venous-sinuses` | 21 | 34 | a fazer |
| 42 | 27/10 · Irrigação do SNC (Jácomo) | 33 | Medula espinal | Vasos sanguíneos da medula espinal | `blood-vessels-of-spinal-cord` | 20 | 20 | a fazer |
| 43 | 03/11 · Sistemas neurovegetativos (Britto) | 51 | Sistema nervoso periférico e autônomo | Sistema nervoso autônomo | `anatomy-pns-ans` | 55 | 54 | a fazer |
| 44 | 04/11 · Meninges e líquor (Jácomo) | 23 | Meninges, ventrículos e líquor | Meninges cranianas | `the-brain-meninges-and-superficial-blood-vessels` | 21 | 26 | a fazer |
| 45 | 04/11 · Meninges e líquor (Jácomo) | 24 | Meninges, ventrículos e líquor | Ventrículos do encéfalo | `the-ventricles-of-the-brain` | 16 | 16 | a fazer |
| 46 | 04/11 · Meninges e líquor (Jácomo) | 25 | Meninges, ventrículos e líquor | Produção e circulação do líquor | `subarachnoid-cisterns-of-the-brain` | 34 | 39 | a fazer |
| 47 | 04/11 · Cortes seriados do SNC (Gerson) | 11 | Estruturas subcorticais | Corte horizontal do encéfalo | `horizontal-section-brain-1` | 31 | 31 | a fazer |
| 48 | 04/11 · Cortes seriados do SNC (Gerson) | 12 | Estruturas subcorticais | Corte coronal do encéfalo (nível do tálamo) | `coronal-section-brain-thalamus-level` | 26 | 26 | a fazer |
| 49 | 18/11 · Sistema límbico (Jácomo) | 9 | Telencéfalo e córtex cerebral | Hipocampo, fórnice e corpo amigdaloide | `the-hippocampus-and-fornix` | 21 | 22 | a fazer |
| 50 | 18/11 · Organização do córtex cerebral (Britto) | 7 | Telencéfalo e córtex cerebral | Áreas de Brodmann | `anatomy-brodmann-areas` | 41 | 41 | a fazer |
| 51 | 18/11 · Organização do córtex cerebral (Britto) | 8 | Telencéfalo e córtex cerebral | Homúnculo motor e sensitivo | `cortical-homunculi` | 9 | 8 | a fazer |

## Trabalho a fazer antes/durante as próximas unidades
1. **Cadastro único de estruturas** (`~/NEBLI-privado/kenhub/estruturas.json`: id Kenhub, nome PT/EN/latim, unidades em que aparece, nota do deck):
   a mesma estrutura aparece em várias unidades (1.398 entradas para bem menos estruturas). Regra: o card nasce na primeira unidade em que
   a estrutura aparece; as seguintes **associam** a nota existente (etiqueta da unidade, sem repetir o card), exceto quando a figura
   da unidade é de outra vista/escala e ensina algo novo (decisão registrada). Gate novo “sem duplicata” entra na unidade 21.
2. **Glossário PT** de termos anatômicos (um termo, uma tradução) — o Kenhub PT já traz o nome; o que falta ele, vem do glossário.
3. **Curadoria assistida**: o rascunho já lista, por estrutura, as melhores notas de AnatoKing/AnKing/outros acervos; falta só confirmar
   cores (verde = pilares, azul = secundárias, rosa = distantes para Davi suspender) e o nome em português dos cards do AnatoKing.
4. **Imagens do acervo**: parte do AnatoKing não tem a imagem no Mac de Davi (17 de 36 no piloto). O gate barra; a cobertura passa a
   vir de Kenhub, Machado, AnKing ou Netter. Verificar a sincronização de mídia do Anki antes de depender do AnatoKing.
5. **Fisiopatologia ligada à neuroanatomia**: só AnKing, nunca autoral (ex.: lesões de nervos cranianos, síndromes do tronco). Entra por
   unidade quando o AnKing tem o card; sem limite de cards.
6. **Machado e veteranos**: ler o capítulo/apostila da unidade e acrescentar o que o Kenhub não traz (decisão por unidade, registrada na curadoria).
7. **Carga**: decks entram dessuspensos (decisão de Davi 17/10); as estruturas distantes têm bandeira rosa para ele suspender depois.

## Regras de operação (Davi está sempre no Anki — F-20261017-CLAUDE-03)
- Navegador do Kenhub e renderização **sempre invisíveis**; nada abre janela na tela dele.
- Escrita no Anki em lote curto, nunca na nota em tela, sync só quando ocioso; o instalador espera o Anki ficar livre e é retomável.
- Antes de gravar bandeira o comando testa se o Anki aceita; se houver janela de edição aberta, pede **uma vez** que a feche.
- Kenhub aceita um aparelho logado por vez: o navegador automatizado derruba o login do celular de Davi enquanto estiver aberto.
  Encerrar com `pkill -f nebli.kenhub.navegador` ao terminar uma sessão de coleta.
- Uso pessoal: figuras só na coleção de Davi (`NEBLI::fonte::kenhub`; `nebli.package_uc` recusa empacotar). Módulo a módulo, ritmo humano.
  Não há (nem haverá) caminho para acessar o Kenhub sem assinatura.
