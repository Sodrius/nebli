# Retrospectiva do processo — primeira corrida integral do pipeline E1 + deck

Aula-cobaia: `anato-intestino-grosso` (Intestino grosso, reto e canal anal), 2026-08-10.
Primeira execução do `e1-deck-v3` do início ao fim numa aula nova, sem reaproveitar deck antigo.

O que segue é o que a corrida ensinou sobre **o processo**, não sobre a aula. Cada item traz
o que estava errado, o que foi feito e o que fica combinado para a próxima aula.

---

## 1. O gargalo manual era o Image Occlusion — e ele não precisava ser manual

**Antes.** Desenhar caixa de oclusão à mão, uma por uma, era o passo mais caro e o mais
sujeito a erro do pipeline. `io_from_slide.py` tentava resolver com OCR (tesseract), o que
depende de instalação externa e erra em rótulo pequeno.

**Descoberta.** Os rótulos das pranchas nos slides são **texto vetorial dentro do PDF**. O
PDF sabe a caixa exata de cada linha. Não há nada para reconhecer: basta ler.

**Feito.** `flashcards/scripts/pdf_figura_io.py`, com três modos — `dump` (lista as linhas
do recorte com índice e bbox), `crop` (grava a figura) e `build` (grava figura + campo `I0`
+ preview de pergunta e de resposta + manifesto com SHA-256). Os 11 IO desta aula, com 76
máscaras somadas, saíram de um shell script de 100 linhas
(`arquivos-trabalho/anato-intestino-grosso/build_io.sh`), reproduzível e versionado.

**Combinado.** IO de prancha rotulada nunca mais é desenhado à mão. Quando a figura for
raster sem texto (histologia, foto de peça sem legenda no PDF), aí sim entra marcador manual.

---

## 2. Rótulo rasterizado dentro da prancha vaza a resposta

A prancha do colo (Moore) traz "Colo transverso", "Tênia omental" e "Pregas semilunares"
**impressos na própria imagem**, não como texto do PDF. Mascarando só os rótulos do slide,
"Tênia omental" continuava visível enquanto "Tênias" estava coberto — exatamente o caso
reprovado em `docs/canon/EXEMPLOS-CARDS.md` ("um rótulo duplicado continua visível").

**Feito.** `--pixel-label "Nome:x,y,w,h"` (rótulo rasterizado vira máscara de resposta) e
`--blank "x,y,w,h"` (pinta de branco figura secundária que reexibiria um rótulo já
mascarado — foi o caso do inset de puborretal na prancha dos esfíncteres).

**Combinado.** Antes de aprovar qualquer IO, olhar o preview de **pergunta** procurando
nome de estrutura ainda legível. É um passo de olho, não de script.

---

## 3. A regra da legenda: a primeira versão estava errada, e a revisão pegou

Vários rótulos vêm como `Seio anal (liberam muco) (espaço entre as colunas)`. A primeira
regra desta corrida foi: mascarar só o **nome**, deixando a explicação visível — o raciocínio
era evitar que o IO cobrasse duas coisas e repetisse o que um cloze já cobra.

O `revisor-cards-visual` derrubou isso com o argumento certo: `(espaço entre as colunas)`,
`(porção superior das colunas)` e `6-10 cm, tecido linfoide` **não citam o nome, mas entregam
a identidade**. Com elas à vista, a tarefa deixa de ser reconhecimento visual e vira leitura
de definição — e ainda por cima adianta a resposta de quatro cloze cards.

**Combinado.** A máscara cobre o nome **e todo texto que defina ou localize a estrutura**.
Fica visível só o que não nomeia nem define: crédito da fonte, título de orientação da
prancha, qualificador neutro. Na dúvida, mascarar.

A lição de processo é maior que a regra: o erro era invisível no contrato (o `leakage_check`
dizia, com razão, que a legenda "não nomeia a estrutura") e só apareceu quando alguém olhou
o preview de pergunta perguntando *o que o aluno consegue responder sem saber a resposta*.

---

## 4. O note type de IO do AnKing não serve a mapa coerente

Só apareceu porque a renderização virou gate de verdade (item 6). O
`IO-one by one (AnKing Step Deck / AnKingMed)`:

- **não mostra imagem na frente** — exibe "This is an Image Occlusion one by one card:
  Please flip to the backside", porque foi desenhado para revelação incremental no verso;
- depende do JS do add-on do AnKing para desenhar as oclusões;
- referencia `_AnKingRound.png`, mídia do AnKing que não acompanha o pacote NEBLI (e não
  pode acompanhar, por `ERROS.md` §19).

Nada disso combina com `hide_all_guess_all`, em que o mapa inteiro é uma recuperação só.

**Feito.** `IO NEBLI - Image Occlusion (mapa coerente)`, definido em
`build_apkg_offline.py`: frente = imagem com todas as máscaras queimadas; verso = imagem
revelada + lista de rótulos + fonte. Sem JS, sem add-on, idêntico em desktop, AnkiDroid e
AnkiMobile. As coordenadas continuam no campo `I0`, para auditoria e regeração.

**Combinado.** `hide_all_guess_all` usa o note type NEBLI. Se um dia existir card de
revelação incremental de verdade, aí o note type do AnKing volta a fazer sentido.

---

## 5. Faltava o montador offline que o canon exige

`docs/canon/APKG.md` proíbe depender do AnkiConnect, mas o único montador existente
(`montar_deck_aula.py`) fala com `localhost:8765`. Na prática o canon não era executável.

**Feito.** `flashcards/scripts/build_apkg_offline.py` escreve a coleção Anki legada
(schema 11) direto em SQLite: note types, árvore de decks com todos os níveis
intermediários, cloze com um card por ordinal, subdeck `Optional`, mídia deduplicada por
hash com renomeação em colisão, `dconf` com 25 novos/dia e 9999 revisões/dia. GUIDs são
derivados de `slug:card_id`, então reimportar **atualiza** as notas em vez de duplicá-las.

O montador lê o `contrato-cobertura.json` — os cards moram no contrato, não numa segunda
cópia. O script aborta se o total real divergir do previsto ou passar do teto.

---

## 6. Renderizar em navegador de verdade é o gate que mais achou defeito

**Feito.** `flashcards/scripts/render_apkg_previews.py` abre o `.apkg`, monta o HTML de
pergunta e de resposta aplicando o template do note type (incluindo o filtro `cloze:`) e
fotografa as duas faces com o Chromium que já existe no ambiente. Saída: 94 PNGs e um
`render-report.json` com mídia referenciada × presente.

Foi esse gate que expôs o item 4 — o relatório JSON dizia `passed: true` com o note type
quebrado, porque JSON não vê tela. É a diferença entre "auditar o arquivo" e "olhar o card".

**Combinado.** Nenhuma aula fecha sem os previews renderizados e olhados.

---

## 7. Dois defeitos que os gates pegaram sozinhos (e é assim que deve ser)

- **Âncora literal na E1.** O gerador do contrato confere cada âncora contra o texto da E1 e
  reprovou os cards de Crohn e retocolite ulcerativa: o conteúdo estava no slide 17, mas não
  na E1. A E1 recebeu o box de doença inflamatória intestinal **antes** de os cards voltarem.
  Foi exatamente o comportamento que `ERROS.md` §2 pede.
- **Mídia órfã.** O campo `Image` dos cloze saía com o nome do arquivo em vez do caminho do
  repositório; 7 figuras não entravam no pacote e virariam imagem quebrada no celular. O gate
  `referenced_media == packaged_media` pegou na hora.

**Combinado.** Gate que só relata não serve; gate que **derruba a geração** é o que funciona.

---

## 8. O AnKing privado não atravessa para o ambiente de execução

Este é o furo real desta corrida, e não foi resolvido.

O índice existe e está íntegro no Drive: `Anking/AnKing-index-v2`, 564 MB descompactado
(103 MB em duas partes), a partir de um pacote-fonte de 5,9 GB. O problema é o canal: o
conector do Drive devolve arquivo em **base64 dentro do contexto do modelo**. Um índice de
103 MB não passa por ali, e nem o extrato seletivo `anking-selected-digestorio.apkg`
(13,7 MB, quase tudo mídia).

Resultado: a ordem `AnKing → externos → autoral` não foi executada no passo 1. Foi feita a
busca possível — o corpus AnKing-derivado local (`P3 - UC02 completo.apkg`, 247 notas), com
famílias PT, EN e mecanismo, 4 acertos, todos de outras aulas — e todos os 47 cards ficaram
com `candidate_search.status = blocked_private_index_unreachable`.

**Três saídas, em ordem de preferência:**

1. **Dossiê compacto de candidatos.** O que precisa atravessar não é o pacote, é a *decisão*:
   GUID, note type, tags, primeiro campo truncado e nomes de mídia dos candidatos. Para uma
   aula isso cabe em ~60 KB de JSON — passa pelo canal sem problema. O extrator roda onde o
   índice mora (o Colab `Extrator seletivo AnKing` já existe no Drive) e deposita
   `anking-dossie-<slug>.json` na pasta privada. A sessão então cura de verdade e só puxa a
   mídia dos GUIDs escolhidos.
2. **Rodar o pipeline onde o índice está**, em vez de trazer o índice para o pipeline.
3. **Aceitar autoria com recuradoria marcada**, que foi o caso aqui — funciona, mas só uma vez.

Enquanto (1) não existir, toda aula sai com o mesmo débito. Vale registrar que, para *esta*
aula, o débito é pequeno: identificação em nomenclatura portuguesa sobre pranchas e peças da
própria disciplina é coisa que o AnKing não fornece, e o extrato de digestório que já foi
feito rendeu 15 notas para o sistema digestório inteiro.

---

## 9. Achados menores, já corrigidos

- **Note type de cloze com cabeçalho de outra aula fixo no template.** O
  `Cloze Medicina - Mecanismo Único` trazia `BIOQUÍMICA · METABOLISMO DO GLICOGÊNIO` escrito
  dentro do `qfmt`/`afmt`: toda aula nova herdava o cabeçalho da aula de glicogênio. O
  montador agora deriva `Cloze NEBLI - Aula` com campo `Tema`.
- **`typst-template/TEMPLATE_API.md` está desatualizado.** `mapa-parte` exige `id` em cada nó
  (o doc mostra só `titulo`/`texto`) e cada aresta precisa de 3 elementos (o doc sugere `()`).
  Custou dois ciclos de compilação.
- **Fonte Merriweather no Linux.** Os `.ttf` de `typst-build/fonts` registram a família como
  `Merriweather Light 18pt`, e o template pede `Merriweather` — o PDF saía com fonte de
  fallback. Normalizado para a corrida; convém consertar os arquivos na origem.

---

## 10. A rodada de revisão pagou o próprio custo

Os três revisores rodaram sobre artefatos completos, em modo somente leitura, e devolveram
**zero BLOCK** — mas cinco correções reais que a sessão principal não tinha visto: o item
"válvulas anais" do roteiro sem card, as legendas do IO que entregavam a resposta (item 3),
o enunciado inconsistente do IO dos esfíncteres e o recorte largo demais de uma figura de
Extra. Um achado foi **rejeitado com evidência** (um typo em `innervation` que não existe no
contrato — erro de leitura do preview, não do card).

Duas coisas valem guardar. A primeira: o revisor de cobertura, que só lê texto, encontrou
uma lacuna de *identificação* justamente porque foi conferir item a item do roteiro prático
contra o contrato — trabalho chato que a sessão principal tende a declarar feito. A segunda:
o revisor de cards/visual só achou o problema das legendas porque **abriu os 94 PNGs**. Sem
o gate de renderização do item 6, não haveria o que abrir.

**Combinado.** Revisor recebe os previews renderizados junto com o contrato, sempre. E
achado de revisor não é ordem: dois dos sete foram confirmados como decisão intencional e um
foi rejeitado com evidência — o destino de cada um fica escrito em `revisao-independente.json`.

---

## 11. Sobre o volume de cards

47 para uma aula grande, com teto congelado em 50 (faixa de sanidade 35–55). O que segurou
o número não foi cortar conteúdo, foi **escolher o formato certo**: 11 IO em
`hide_all_guess_all` absorveram os 22 alvos de identificação do roteiro prático que, um a
um, teriam virado 40 cards verbais ruins. A concentração ficou onde a prova concentra —
10 cards no bloco da linha pectinada, que é o tema das perguntas orientadoras 2.1 e 2.2.

A heurística que fica: **antes de escrever o enésimo cloze de "qual é o nome de", pergunte
se aquilo não é um mapa**. Mapa coerente é um card; lista de nomes é dez cards ruins.

---

---

## 12. Segui o doc em vez do dado, e o deck saiu fora da coleção

O cronograma da UC sugeria a árvore `NEBLI::Digestório::<P1|P2>::<Componente>::<aula>`. Segui
essa linha. A coleção real, porém, usa o **código** da UC — `NEBLI::UC02::P3::Componente::Aula`
—, e `referencias-externas/DRIVE-ESTRUTURA.md` já dizia `NEBLI::UC::Prova::Componente::Aula`.

Resultado: o deck da aula caía num galho de topo `NEBLI::Digestório`, separado de todo o
resto. Nada acusava erro — auditoria passava, o Anki importava sem reclamar — e só aparece
quando alguém olha a árvore no aplicativo.

Duas lições. A primeira: **quando um documento e o artefato real discordam, o artefato real
manda.** Os decks existentes eram consultáveis o tempo todo dentro do próprio repositório.
A segunda: convenção que não é validada não é convenção, é intenção. Virou gate em
`build_apkg_offline.py`, que se recusa a montar árvore fora de
`NEBLI::<UC de 2 dígitos>::<P\d>::<Componente>::<Aula>` com `::Optional` pendurado nela.
A sugestão enganosa foi corrigida no próprio cronograma.

---

## 13. O harness de preview estava mentindo

O item 6 comemorou cedo demais. O renderizador embrulhava o card num contêiner próprio
(`#qa { max-width: 1100px; margin: 0 auto }`), coisa que o Anki não faz — ele põe o card
dentro de um único `<div class="card">` e deixa o CSS do note type mandar. Esse contêiner
extra **centralizava e limitava tudo**, e com isso escondeu um defeito real do CSS herdado:
`.meta` não tinha `max-width`/`margin: auto` e colava na borda esquerda, enquanto o texto
ficava numa tira centralizada de 760 px. No tablet o card parecia partido ao meio.

Também faltava simular o fundo: em modo noturno o Anki pinta escuro, o harness não pintava,
e um preview de texto claro sobre branco não diz nada sobre contraste.

**Feito.** O harness passou a reproduzir o DOM do Anki (`<div class="card">`, sem contêiner
extra), a aceitar `--width` para simular tablet em paisagem e `--night` para modo noturno com
o fundo certo. O CSS do cloze foi reescrito: uma coluna só para cabeçalho, enunciado, Extra,
imagem e fonte; medidas relativas; realce de cloze; e `.night_mode` **e** `.nightMode`, porque
AnkiDroid antigo usa o segundo. O fundo do card ficou por conta do Anki — pintar só a `div`
cobre a altura do conteúdo e deixa o resto da tela na cor padrão.

**Combinado.** Preview que não reproduz o ambiente real não é gate, é enfeite. Toda aula
renderiza em largura de tablet e em modo noturno, e o preview é olhado nos dois.

---

## Mudanças de canon — aplicadas nesta corrida

1. `docs/canon/VISUAL-E-IO.md` — regra da máscara (item 3), varredura de rótulos
   rasterizados (item 2) e exigência de que o note type de IO mostre a imagem mascarada na
   frente (item 4).
2. `docs/canon/APKG.md` — montagem offline por `build_apkg_offline.py` e renderização em
   navegador como gate.
3. `docs/canon/ANKING-PRIVADO.md` — dossiê compacto de candidatos como forma canônica de a
   curadoria atravessar quando o índice não está no mesmo ambiente.
4. `docs/canon/PIPELINE-E1-DECK.md` — passo 16 passa a exigir renderização em navegador e
   olhar os previews.
