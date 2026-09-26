# Aprendizados — Fisiologia bacteriana (Microbiologia)

Executado em 23/09/2026 por escolha do Claude (Davi pediu "uma outra aula à sua escolha"). **Aguarda feedback.** Primeira aula gerada já com as três regras de 23/09: imagem nos autorais, vídeos dos canais preferidos junto do deck, APKG só local.

## Resultado

- Deck `NEBLI::UC03::P2::Microbiologia::Fisiologia bacteriana`: 29 notas / 35 cards. São 26 AnKing (23 notas) e 9 autorais (6 notas); 5 verdes, 0 vermelhos, 0 suspensos. APKG verificado (3,6 MB), origens intactas.
- Pasta privada: https://drive.google.com/drive/folders/1OTuF0EtbQemdroU4d8vjfUUNyYtM-kG5 (guia e mapa).

## O que esta aula ensinou

- **Antibióticos ficou sem deck** porque a pasta docente está vazia. A regra "sem material docente não roda" funcionou; escolhi outra aula em vez de inventar o recorte.
- **O AnKing pode estar errado no verso:** o card 1500497965459 afirmava "only aerobic bacteria perform cellular respiration", o que contradiz a respiração anaeróbia ensinada na aula. Foi corrigido na cópia. Ler o Extra continua obrigatório, não opcional.
- **Microbiologia básica tem muito AnKing, mas organizado por organismo.** Os campos Sketchy/Pixorize são cenas de organismos (H. influenzae, clostrídios, Salmonella), então esta aula limpou todos os recursos, exceto os Bootcamp "Fundamentals of Bacteriology". A regra de tema de cada aula precisa ser escrita caso a caso.
- **Economia de cards em meios de cultura:** ágar sangue tinha 4 clozes e 3 cards de hemólise; ficaram 2 + 3. MacConkey tinha 3 notas; ficaram 2.
- **Imagem herdada inadequada de novo** (algoritmo de identificação no card das colônias rosa no MacConkey); corrigida pela inspeção visual. Em 3 aulas seguidas a inspeção pegou erro.
- **Correção desleixada:** ao reaproveitar o crédito da foto, a regex capturou a imagem junto e a duplicou; o readback mostrou e a duplicata foi removida. Lição: nunca montar HTML por regex sem conferir o resultado.
- **Tags AnKing aparecem no rodapé do card** (ex.: `Streptococcus_pneumoniae`). Não é conteúdo de verso, mas polui a varredura de "clínica lateral". Decidir com Davi se as cópias devem manter as tags de recurso visíveis.
- **Vídeos:** só um dos canais preferidos cobre a aula (Shomu, curva). Para oxigênio, meios, ferro e respiração, nenhum vídeo dos canais listados apareceu; lacuna declarada.

## Feedback de Davi (23/09/2026, tarde)

- "O vídeo tem que vir aqui no chat, não nos cards." Revoga a regra da manhã: vídeos vão na resposta do chat (e no guia), nunca em `Additional Resources`. Remoção dos links já inseridos (7 notas aqui, 27 na Genética) ficou pendente: o classificador de permissões bloqueou a edição da coleção; backup/restauração planejados via `journal.jsonl` da Genética.
- "Cards autorais tem que ser menos, cards normais mais, proporcionalmente" e "os autorais estão muito grandes". Aqui as frentes autorais tinham 17–33 palavras (AnKing típico: 8–15). Autoral 31% (9/29 cards únicos de 35). Regra nova em README/EXECUCAO: segunda busca AnKing obrigatória antes de autorar, recuperar recusados por "redundância com o verso", frente ~8–15 palavras.
- Revisão da busca achou AnKing que poderia ter entrado: lactoferrina quelando ferro (1487642782702), hepcidina contra acesso do patógeno ao ferro (1478973207060), SOD (1487642726245, HY) e catalase/GPx (1487470255062, HY) para a toxicidade do O₂, *M. tb* cresce em 2–6 semanas (1503250260788, recusado antes), tempo de geração (1500673014315), MacConkey diferencia fermentadores de lactose (1500496166406, HY), ágar sangue não seletivo (1500491213487), subprodutos da fermentação (1500498676105). Opcional: bactérias siderofílicas × hemocromatose (1521573734382).

## Ajuste aplicado (23/09/2026, noite) — por que os AnKing ficaram de fora

Aplicado por `ajuste_pos_feedback.py` (backup em `before-ajuste-2026-09-23.json`, journal atualizado, APKG reexportado, `verify.py` passou): 38 notas / 45 cards (35 AnKing, 10 autorais), 8 verdes. Vídeos removidos dos 34 cards (7 aqui, 27 na Genética, restaurados do journal). Autorais encolhidos para frentes de 10–16 palavras. Temperatura (psicrófilo/mesófilo/termófilo) virou 1 card e sal (halotolerante/halófilo) virou 1 autoral novo com a figura do slide, ambos candidatos à suspensão pós-prova. Entraram 8 AnKing: lactoferrina, hepcidina, SOD, catalase/GPx, *M. tb* 2–6 semanas, tempo de geração, MacConkey × lactose e produtos da fermentação. Ágar sangue "non-selective" não entrou porque já é o c2 da nota de ágar sangue (duplicata exata).

Por que ficaram de fora na 1ª corrida (erros de método, não de acervo):
1. **Pool só por tags de micro.** O lado do hospedeiro (lactoferrina, hepcidina) mora em imuno/hemato e as enzimas do O₂ (SOD, catalase) em bioquímica/neutrófilo. A busca textual usou termos do lado bacteriano ("sideróforo", "imunidade nutricional"), e não as moléculas citadas no próprio slide.
2. **Recusa por "redundância com o verso".** Contraria a V4 (seleção ampla até a prova): se o AnKing tem a pergunta, ela entra; o verso não substitui a recuperação ativa.
3. **Autoral-primeiro quando faltava a frase exata.** Em vez de montar o alvo com 2–3 cards AnKing + 1 autoral pequeno, escrevi um autoral grande que juntava tudo.

Correção de método: buscar **cada substantivo do slide** (moléculas, enzimas, meios), também fora das tags da disciplina; só depois autorar.
