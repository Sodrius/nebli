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

"Sempre se atentar à bibliografia... não precisa pôr tudo deles, mas são a bibliografia do curso." Usar o livro para conferir recorte, profundidade e precisão, e citar no relatório o capítulo realmente consultado. Não transformar o capítulo em deck. Livro ausente → usar substituto de acesso livre e declarar.

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
