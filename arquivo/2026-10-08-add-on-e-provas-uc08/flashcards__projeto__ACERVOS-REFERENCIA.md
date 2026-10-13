# Fontes e acervos — localizadores e modelos

Inventário vivo em 23/09/2026, atualizado em 24/09/2026 (`arquivos-trabalho/lote-uc03p2-uc08p1-2026-09-24/catalogo.json`), perfil Davi, após reorganização e novas importações. Fonte completa: `arquivos-trabalho/reinicio-uc-2026-09-23/catalogo-vivo.json`. Foram mapeados todos os modelos presentes por contagem/consulta, com zero cards sem modelo identificado; conteúdo e tags lidos por amostra, não auditoria científica integral. Descoberta dinâmica, sem depender do nome da pasta-pai.

## O que está disponível

Todos os acervos externos abaixo estão em `Referências::Referências Externas::<nome>` nesta fotografia. AnKing Step Deck permanece no topo. Contagens de corpus não são contagens de cards selecionados para aulas.

| Acervo | Cards | Quando buscar antes de autorar |
|---|---:|---|
| AnKing Step Deck | 35.067 | Primeiro em todo alvo pertinente: fatos, relações, mecanismos e aplicação Step do mesmo assunto |
| AnKing-MCAT | 6.320 | Fundamentos de bioquímica/biologia e técnicas básicas quando forem da aula; não importar o currículo MCAT |
| Dope Anatomy | 3.186 | Anatomia regional, relações, pranchas, perguntas textuais e visuais |
| 100 Concepts (Dorian) | 303 | Relações anatômicas e aplicação curta dentro do recorte |
| Histology | 6.023 | Teoria/estrutura-função e figuras histológicas |
| LLU Histology | 135 | Identificação histológica/prática e apoio sucinto |
| University of Michigan - BlueLink Atlas | 2.992 | Reconhecimento anatômico/oclusão, alternativa visual ao AnKing |
| AnatoKing (V2) | 3.493 | **Última opção entre acervos anatômicos, pedido de Davi em 28/09:** AnKing → outros (Dope/BlueLink/Dorian conforme alvo) → AnatoKing. Modelo `AnatoKingOverhaul V2`; conferir figura, destaque e resposta, além da existência da mídia. Imagem principal precisa ser grande e visível |
| USMLE Lab Values | 232 | **Novo, 24/09.** Valores laboratoriais (modelo `LabValue`, subdecks Normal Range/Practice). Só quando a aula cobra um valor de referência; não importar a tabela inteira |

São **22.684 cards externos** (vistoria de 24/09/2026), além do AnKing Step (35.068, em `Referências::Anking Step Deck` — com "k" minúsculo; o filho `Instructions` usa "AnKing"). O deck `Ankisthesia` (anestesia) apareceu no topo, mas estava vazio na vistoria. Nenhum deles deve ser incluído por quantidade ou reputação; todo candidato passa por alvo, qualidade e modelo. Ter um acervo não demonstra cobertura de uma lacuna antes da busca.

## Novidade: AnKing-MCAT

Subdecks observados: Biochemistry 919; Biology 1.238; Behavioral 2.429; General-Chemistry 477; Organic-Chemistry 554; Physics-and-Math 585; Essential-Equations 95; uma nota demonstrativa em AnKing-Note-Types. A pasta-pai e seu filho demonstrativo representam o mesmo card: não somar duas vezes.

Modelo `AnKingMCAT (AnKing-MCAT / AnKingMed)`, campos Text, Extra, Lecture Notes, Missed Questions, Pixorize, Sketchy, Additional Resources, One by one e ankihub_id. Há tags `#AK_MCAT_v2`, Kaplan, KhanAcademy, Subjects, UWorld/Books e AnkiHub_Subdeck. Usar essas rotas para localizar, não como prova de escopo ou qualidade.

Rota sugerida: uma lacuna de bioquímica/célula vai primeiro ao AnKing Step, depois MCAT Biochemistry/Biology e demais fontes adequadas. Química/física/comportamental só se o alvo da aula realmente exigir aquilo. Não acrescentar química geral ou pré-requisitos só porque MCAT os oferece. **MCAT não é Step 1 e não recebe verde por carregar o nome AnKing.** Não selecionar o card demonstrativo de modelo.

## Modelos: por que busca só em Text falha

- **AnKing Step:** 34.967 cards no AnKingOverhaul principal, 95 em `AnKingOverhaul (NEBLI glicogenio)` e 5 em IO-one by one. O nome NEBLI de um modelo dentro do acervo não autoriza tratá-lo como cópia descartável; preservar a origem e verificar proveniência. Procurar por conteúdo e tags de recursos/sistemas, não exclusivamente por nome do modelo.
- **Dope:** Anatomy 2.371; Basic-4a67b 45; Cloze deletion 54; Cloze-34931 3; Image Occlusion Enhanced 2: 26; três modelos Image Q/A somando 687. Buscar Title, rótulos 1a…20a, Front/Back ou campos visuais conforme modelo. Não ignorar 815 cards por ter lido só o modelo Anatomy.
- **Dorian:** Cloze-b12d6 287 e Image Q/A 16; não é exclusivamente textual.
- **Histology:** Cloze-AnKingMaster-v3, 6.023. Buscar Text/Extra, tags como H::EpithelialTissue e as figuras. Uma palavra no Extra pode revelar a nota certa, mas cada cloze precisa ser julgado.
- **LLU:** dois AnKingOverhaul adaptados, 65 + 70; tags de prova prática/histologia. Preservar imagens e inspecionar identificação de fato.
- **BlueLink:** Image Occlusion Enhanced+, 2.992; Image, Question Mask, Answer Mask e Original Mask precisam viajar juntos. Tags regionais como BlueLink::PectoralRegion+SuperficialBack ajudam a localizar.

Templates e campos completos estão no JSON, sem precisar carregar toda a coleção em cada conversa. Modelos visuais exigem renderização/inspeção dos candidatos: inventário estrutural não aprova as imagens.

## Procedimento de busca por lacuna

1. Definir alvo da aula e sinônimos PT/EN; primeiro procurar identidade NEBLI viva para não duplicar histórico.
2. AnKing Step: texto + tags amplas → recursos específicos (Ninja Nerd/First Aid/Bootcamp etc.) → vizinhança semântica → leitura card a card. Tag é pista, nunca seleção automática da tag inteira.
3. Se nada adequado, reformular fora da disciplina aparente. Procurar estrutura, relação, molécula ou contraste em outro sistema, sem importar assuntos laterais.
4. Consultar os acervos adequados acima usando os caminhos da descoberta atual. Registrar consultas e candidatos rejeitados. Um resultado vazio não demonstra ausência no corpus.
5. Antes da autoria, verificar se o verso ou um bom visual existente resolve; autoria só para lacuna importante real. Uma imagem de apoio pode enriquecer um card sem gerar outro card.
6. Se os acervos atuais continuarem insuficientes, registrar o tipo de falta (por exemplo, peça/plano anatômico não representado) e orientar aquisição específica em tarefa separada. ComprehensiveCadaver, Netter Better e Foundations aparecem como ideias no Docs, mas **não foram encontrados como acervos instalados sob esses nomes** (o AnatoKing foi instalado em 24/09); não fingir busca neles nem baixar automaticamente.

Atualizar com `python -m nebli.preflight --catalog --output <pasta-da-execucao>/catalogo.json`. Toda importação/reorganização invalida caminhos/contagens anteriores; a descoberta inclui automaticamente novos filhos de Referências Externas.

## Anatoking — instalado em 24/09/2026 (histórico da avaliação abaixo)

Pesquisa de 24/09/2026 na [publicação do autor da V2](https://www.reddit.com/r/medicalschoolanki/comments/sgmmms/anatoking_v2_better_late_than_never/). A V2 foi anunciada com 3.493 cards, campos Cadaver/Illustration/Model/Imaging, relações musculares e estilo inspirado no AnKing. O autor também documenta cerca de 250 estruturas sem imagem testável e mídia faltante. São características daquela versão, não inspeção de pacote atual.

Davi avaliou em 28/09: “anato king não é bom, preferir anking, depois outros de anato depois anatoking”. Usar AnatoKing por último entre os acervos, somente quando a figura e o alvo forem bons; aumentar as imagens das cópias existentes. Pode haver várias práticas da mesma estrutura, com **um único representante verde**. Antes de incorporar: testar mídia/template, verificar conflitos de IDs/modelos e avaliar a região pertinente. Importar como referência, sem ativar milhares de revisões. Incompletos não cobrem lacunas. Não executar instruções antigas de apagar decks para completar mídia.

## Bibliografia por matéria (Davi, 24/09/2026 — ele avisa quando mudar)

"Sempre se atentar à bibliografia... não precisa pôr tudo deles, mas são a bibliografia do curso." Usar o livro para conferir recorte, profundidade e precisão, e citar no relatório o capítulo realmente consultado. Não transformar o capítulo em deck. Livro desconhecido/ambíguo → perguntar a Davi após consultar a lista atual; livro conhecido mas inacessível → buscar acesso/alternativa e avaliar a falta conforme MEMORY, sem substituição silenciosa nem instalar com fonte importante pendente.

Pasta **Livros** no Drive: `1ZYH9ezNk8lH4h0ArsX2PgdOpsnf4N-ss`.

| Matéria | Livro do curso | No Drive | Substituto se faltar |
|---|---|---|---|
| Patologia | Robbins | `1u6R2qzAKb7zEDeBzkD6_NSvDh7sjdvn6` (Livros; presença confirmada 28/09, conteúdo não lido nesta confirmação) | StatPearls (NCBI Bookshelf) do tópico; figuras do Robbins nos slides não equivalem a capítulo lido |
| Microbiologia | Trabulsi-Alterthum, 6ª ed. | `1QiU-YUYL85MM0kTfHOQetm5VKJRO2PJ3` (Livros) | Murray/Medical Microbiology (Baron, NCBI Bookshelf) |
| Imunologia | **Abbas** (confirmado 24/09) | `1JfWlKNQeGkEUh5Ih0CNqnZH4ft8mN_aT` (compartilhado pelo ICB) | Janeway 8ª ed. `1L45MKuyfHC_bbN2hhlWTjYq7UkJqC350` (Livros) |
| Histologia / Biologia Tecidual | Junqueira | `1u14iVQGia6FwrZvubVcAMCiTXwU8QZVp` | Histology Guide (atlas indicado nos roteiros) |
| Fisiologia | Margarida (de Mello Aires) | `1kyImyBETHBfM7Rp2o9gUqEn2-VE29XMr` | Guyton / Costanzo, se acessível |
| Bioquímica / Biologia Molecular | Harper | não localizado | Berg *Biochemistry* 5ª ed. e Lodish *Molecular Cell Biology* 4ª ed. (NCBI Bookshelf, livres) |
| Anatomia | Netter | Atlas `1nnetoiEhQCcsABxyuoAS3sUvw5HXukX_` (Livros) | — |
| Endocrinologia (Grand Round DM) | — | Williams 11ª ed. `1Tt-NrQxSwbwirD_PMRT6eqxFqlpTNLec` (Livros, 587 MB) | — |

Acesso aos PDFs: o conector Drive do Claude devolveu texto vazio para o Trabulsi (PDF grande). Baixar pelo navegador para uma pasta local ignorada pelo Git (`arquivos-trabalho/livros/`) e extrair só o capítulo com `pymupdf`. Não declarar leitura de capítulo que não foi aberto.

Canais preferidos declarados: Ninja Nerd; Medicosis Perfectionalis e Patologia Fácil; Dirty Medicine; Armando Hasudungan, Osmosis e Professor Dave; Shomu's Biology. Q028, 29/09: oferecer uma seleção mais ampla de recursos pertinentes para Davi escolher, sem alegar cobertura de vídeo não assistido. O idioma e os critérios são os do MEMORY atual.

## Fontes de toda aula — Davi, 02/10/2026 (F-20261002-CLAUDE-06; substitui a tabela e a lista de canais acima onde divergirem)

**Base do que é a aula:** slides + provas antigas + exercícios + material do CAOC (arquivos). Tudo no Drive montado: `~/Library/CloudStorage/GoogleDrive-dpbdes@gmail.com/Mon Drive/` (aulas em `MEGA DRIVE/Medicina/Resumos e exercícios/B - Primeiro ano/UC<NN>/`; `Margarida.pdf` na raiz; pasta de livros no Drive `10URthATN63lr0GSxN9ekgQrGJ1abzxNn`). Procurar na montagem antes de declarar fonte ausente.

**Bibliografia por UC (ler o capítulo pertinente da aula, sempre; UC01/02/03/08 e canais reconfirmados por Davi em F-20261002-CODEX-10):**
- UC01: Lehninger, Alberts, Guyton
- UC02: Lehninger, Alberts, Guyton, Junqueira, Netter
- UC03: Abbas, Robbins, Lehninger, Trabulsi (no MEGA DRIVE), Netter; para clínica, os livros do HCFMUSP
- UC07: Netter
- UC08: Guyton, Margarida (Aires), Junqueira, Alberts, Netter
- UC19: **Rang & Dale**, confirmado por Davi em 06/10/2026. PDF 7ª ed. no Drive pessoal, `MEGA DRIVE/Outros/Livros/Bibliografia principal - medicina/Rang _ Dale Farmacologia 7 Ed.pdf`; conector ID `1yStxtNxwnZuBYTeOYKRZtz0US5zhunVL`. Explorar também `UC19/Outros` (questões, objetivos, De Nucci e apostila).

**Canais que Davi acompanha — conferir sempre, em toda aula, para entender o assunto e calibrar o que importa:** Ninja Nerd, Medicosis Perfectionalis, Osler, Osmosis, Professor Mike, AK Lectures, MK Fisiologia, Dirty Medicine, Shomu's Biology. Transcrição lida não é vídeo assistido; declarar o que foi de fato consultado (`youtube-transcript-api` funciona neste Mac).


### Localização complementar — busca de 02/10/2026 (Codex)

- [MEGA DRIVE](https://drive.google.com/drive/folders/18HEmYCd--zhu5KRi9IutMggaoNAtBqcK): confirmado pelo conector; montagem local contém `Medicina/Resumos e exercícios/B - Primeiro ano/UC<NN>` e `Medicina/Sem compartilhar/Provas/UC<NN>`. Algumas subpastas deram timeout na listagem local; isso não prova ausência de arquivos.
- [Pipeline criação de cards](https://docs.google.com/document/d/1gHGICvzQMe_B5CJFPAKwo6SvtIjcqEwBPCV5v-dBhD0/edit): texto lido, confirma referência a “CAOC arquivos”, bibliografia e canais. Contém metas antigas conflitantes (30/35/350 semanal); a fala atual e MEMORY, 40 novos/dia, prevalecem.
- [Gliconeogênese — Etapas 1 a 4 — drive do CAOC](https://drive.google.com/file/d/1h_LnK-Hg0_Kiqn8DFvgU8AGPoqkZB_dQ/view): PDF localizado, não lido nesta busca; local `Mon Drive/Guardar para mim/com E4/Gliconeogênese - Etapas 1 a 4 - drive do CAOC.pdf`. O título não certifica autoria ou acesso ao acervo inteiro. Revisões locais de ácidos nucleicos também citam CAOC, mas outra revisão identifica o PDF como NEBLI: não usar como prova de procedência.
- [ARQUIVOS 114](https://drive.google.com/drive/folders/16JQUsZKD4sp1O2HG7Y0UZ9tb2MtSqeGU): pasta compartilhada listada com Livros, arquivos diversos, Provas antigas, Resumos, SLIDES e Cards. [Provas antigas](https://drive.google.com/drive/folders/1hdnxUY-WB-mBb-CE_MeFL30mqhoEmGky) contém 1º e 4º semestres na listagem. **Não confirmado que seja o CAOC.** Pesquisa nominal CAOC não encontrou pasta geral; localização dessa raiz continua pendente.
- Provas UC03: consultado `consultar.py --slug pat-07-inflamacao-aguda --desde 2023`; exemplos P2 2025 1.2/2.2 e P2 2024 1.16. Índice tem ecos e trechos mal segmentados; consultar originais antes de usar como evidência final. Consulta não equivale a leitura integral das provas.


### Acesso ao acervo indicado por Davi — 02/10 (F-20261002-CODEX-11)

Davi identificou explicitamente [esta pasta](https://drive.google.com/drive/folders/10URthATN63lr0GSxN9ekgQrGJ1abzxNn) como o acervo ao qual devemos ter acesso. O ID já constava acima como pasta de livros; não inferir o nome/conteúdo da raiz sem abri-la. Ele confirmou que **a conta FMUSP tem acesso e dpbdes@gmail.com não**. Conector e montagem disponíveis nesta verificação usam dpbdes@gmail.com. `get_file_metadata` retornou 404; listagem retornou vazia, o que não comprova pasta vazia. Acesso/conteúdo ainda não verificados. Próximo passo: conectar conta FMUSP ao Google Drive e repetir metadados, listagem e leitura de um arquivo pertinente antes de declarar fonte disponível.

**Atualização de 02/10, tarde (F-20261002-CLAUDE-08).** Davi: o livro de cada matéria vem **sempre do CAOC arquivos** ([link](https://drive.google.com/drive/u/1/folders/10URthATN63lr0GSxN9ekgQrGJ1abzxNn)) e “o plugin do google drive vai ter acesso ao drive do caoc arquivos”. Teste desta sessão: o conector `claude.ai Google Drive` ainda responde como dpbdes@gmail.com (`get_file_metadata` 404 na pasta; `parentId` não suportado). A pasta também não aparece na montagem local da conta FMUSP, porque item “compartilhado comigo” só é montado se houver atalho em “Mon Drive”. **Em toda aula, testar primeiro o conector na pasta do CAOC; se 404, dizer a Davi e usar as rotas abaixo, sem declarar o CAOC consultado.**

Rotas que funcionam hoje, sem conector:
- **Drive da turma (conta FMUSP, montado):** `~/Library/CloudStorage/GoogleDrive-davi.sousa@fm.usp.br/Drive partagés/TURMA 114/1º ano/UC<NN> - <nome>/<Componente>/`. Na UC08 há `Aula NN - …` com os slides, `Material para Estudos` (Exercícios de Anatomia I/II, Prática de Anatomia I/II, Monitoria - Resumo Geral) e `Bibliografia Básica` (Anatomia: Moore, Gray, Dângelo; Histologia: Junqueira, Ross, Kierszenbaum). Fisiologia da UC08 estava com as pastas vazias na listagem de 02/10.
- **Drive pessoal (Gmail, montado; caminhos de 03/10/2026):** aulas em `MEGA DRIVE/Medicina/Material de estudo/A - Primeiro ano (2026)/UC<NN>/`, `Margarida.pdf` na raiz, provas em `MEGA DRIVE/Medicina/Outros/Provas/` (UC01, UC02, UC03, UC21; **sem UC08**). Livros em `MEGA DRIVE/Medicina/Outros/Livros/`, `MEGA DRIVE/Outros/Livros/` e `.../Bibliografia principal/` (inventário no MEMORY, item 4).

- **Netter (atlas, PDF com rótulos em texto):** `MEGA DRIVE/Medicina/Outros/Livros/Atlas of Human Anatomy by Frank H. Netter (z-lib.org).pdf` no Drive pessoal montado; digestório nas páginas 335–338 e 397–400 do PDF (pranchas 237–239, 276–279). Serve para conferir a aula e para oclusão com `nebli.slide_io` (half="full").

Busca anterior: o [site oficial CAOC](https://www.caoc.org.br/links) aponta materiais de estudo para [Med nas Nuvens](https://drive.google.com/drive/folders/1P34Q14neVrke0XorAGwOy6_Rv9K6WeMT), com acesso @fm.usp.br. Esse link também retornou 404 com o Gmail, mas **não substitui a pasta específica indicada por Davi**. ARQUIVOS 114 foi listada pelo conector; vínculo com o CAOC continua não comprovado. A busca nominal CAOC retornou o PDF de gliconeogênese e o documento de pipeline, sem localizar uma raiz adicional.


## Imagens de fonte aberta (F-20261003-CLAUDE-19, 03/10/2026)

Quando a figura do livro for ruim mesmo recortada: histologia em **Histology Guide** (https://histologyguide.com, lâminas virtuais da University of Minnesota) e **Leeds Histology Guide** (https://histology.leeds.ac.uk). Guardar URL e arquivo no registro da corrida (`imagens-vistas.json`), sem crédito visível no card. Vale a mesma ideia para outras matérias: escolher a imagem mais nítida e intencional disponível.


## Atualização — 08/10/2026

Toda a bibliografia está no Drive segundo Davi; ele poderá copiar para `bibliografia/` na raiz. Não presumir presença local. Explorar **Outros, Materiais complementares e equivalentes em cada UC**. Extras de veteranos/professores são essenciais nas matérias anteriores. Registrar arquivos, leitura e contribuição efetiva.

A apostila de lâminas UC02 **já está no Drive segundo Davi**; localizar/ler antes de produzir. Histology Guide também é apoio pertinente. Não registrar como material ainda a enviar. UC17: Neuroanatomia Funcional, Angelo Machado, 3ª ed., Manole. Demais bibliografias/canais no MEMORY. E1 existente é auxiliar; não gerar E1 nesta campanha.


## Drive reorganizado — conferido em 08/10/2026 (leva 1)

Raiz `~/Library/CloudStorage/GoogleDrive-dpbdes@gmail.com/Mon Drive/MEGA DRIVE/Medicina/` tem agora só `Material de estudo/` e `Não compartilhar/`. **Livros:** `Não compartilhar/Bibliografia principal - medicina/` — Alberts 5ª, Moore (Anatomia Orientada), Netter Atlas, Machado Neuroanatomia 3ª (UC17), Goodman & Gilman 12ª, Guyton 12ª, Janeway 8ª, Junqueira 12ª, Lehninger, Trabulsi 6ª, Harrison (manual), Margarida Aires 4ª, Netter Neurologia, Rang & Dale 7ª (UC19), Robbins Bases Patológicas, Williams Endocrinologia 11ª. Também em `Não compartilhar/`: Cronogramas, IC, Imuno P2 deck, Notas, Provas, UC21. Caminhos anteriores (`Medicina/Outros/...`) não existem mais.

**Imagens de histologia (leva 1):** Histology Guide via `python3 -m nebli.zif` (recorte por região das lâminas virtuais; `--buscar <termo>` usa o índice do site; `--anotacoes <url>` lista as estruturas anotadas de uma lâmina). Atlas Sorenson cap. 14 (GI), amostra gratuita do próprio Histology Guide, em `arquivos-trabalho/livros/sorenson/ch14-clean.pdf` (recorte com `nebli.atlas_pdf`). Setas com `nebli.seta`. Registro de cada imagem no lote da corrida.
