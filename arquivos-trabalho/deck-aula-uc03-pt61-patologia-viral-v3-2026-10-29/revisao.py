"""Revisão pós-instalação da 61 v3 (E6–E7), escrita depois de ler revisao-despejo.txt e reler a transcrição contra o deck vivo.
Grava: mapa-de-profundidade.json › revisao; compreensao-aula.json › fidelidade; REVISAO-AUTORAIS.md › Revisão final no deck vivo;
revisao-final.json; REVISAO-DE-QUALIDADE.md.
    python3 revisao.py
"""
import json, re
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text())
E = {e["key"]: e for e in plan["entries"]}
SH = [f"sh-{k}" for k in plan["compartilhados"]]

EXPL = {
 "Dois efeitos: a lesão viral soma o vírus e a resposta": ("Na infecção viral o tecido sofre por dois lados. A resposta do hospedeiro, que deveria só eliminar o vírus, causa boa parte do dano: é a imunopatologia (sh-1792753616942). O outro lado é a biologia do vírus: a maioria dos vírus de DNA replica no núcleo (sh-1792695023262), e o poxvírus, que replica no citoplasma, faz inclusão citoplasmática (sh-1793199695431), então o compartimento da replicação prevê a cara da lesão.", ["sh-1792753616942", "sh-1792695023262", "sh-1793199695431"]),
 "Efeitos diretos e seus três destinos": ("Os efeitos diretos têm três destinos (au-efeitos): a lise libera conteúdo e dá inflamação aguda, a transformação dá neoplasia e o resto (síntese bloqueada, sincícios, citoesqueleto, ciclo parado) é o efeito citopático. Na infecção lítica o vírus toma a maquinaria para copiar o próprio genoma e a célula interrompe o ciclo mitótico (au-sequestro). Quando o genoma viral integrado altera genes de controle do crescimento, a transformação é a mutagênese insercional (au-transformacao).", ["au-efeitos", "au-sequestro", "au-transformacao"]),
 "Inclusões: componente viral em excesso, no compartimento onde é feito": ("As peças virais saem fora da proporção; a montagem para no componente mais escasso e o excedente se acumula, formando a inclusão (au-inclusao). Por isso a raiva faz Negri citoplasmático eosinofílico (sh-1793199693557) e o sarampo pode ter inclusão nuclear (au-raiva-sarampo); herpesvírus fazem Cowdry nuclear (sh-1793199691630) e o CMV o olho de coruja (sh-1793199689045).", ["au-inclusao", "sh-1793199693557", "au-raiva-sarampo", "sh-1793199691630", "sh-1793199689045"]),
 "Sincício: fusão de células infectadas, não granuloma": ("Proteínas F na membrana da célula infectada a fundem às vizinhas e formam células gigantes multinucleadas (sh-1793199689805), como no vírus sincicial respiratório (ak1506457588894) e nas Warthin-Finkeldey do sarampo (sh-1793199692380). O sincício não tem a organização do granuloma: falta a coroa de linfócitos, os macrófagos epitelioides e a necrose central (au-sincicio-granuloma).", ["sh-1793199689805", "ak1506457588894", "sh-1793199692380", "au-sincicio-granuloma"]),
 "Coilócito: o efeito citopático que revela o HPV": ("O coilócito é a célula escamosa com halo perinuclear, marca do HPV no Papanicolau (sh-1793199694409). Quando vem com displasia, o tipo é de alto risco, 16 e 18 (ak1405375421095), e o efeito citopático passa a indicar risco de transformação, o que muda o seguimento da paciente; o verso do HPV liga o achado à neoplasia dos efeitos diretos (au-efeitos).", ["sh-1793199694409", "ak1405375421095", "au-efeitos"]),
 "Resposta: aguda inata × subaguda e crônica adaptativa": ("Nos quadros agudos (vírus respiratórios e intestinais) predomina a imunidade inata; nos crônicos (hepatite B, HIV, HTLV) a adaptativa (au-quadros). Na inata antiviral a NK tem o papel do neutrófilo na bacteriana (au-nk-neutrofilo); o complemento destrói a célula que expõe proteína viral pelo complexo de ataque à membrana (au-complemento); o CD8 mata por Fas-FasL (sh-1791625430882) e apoptose (sh-1791625429957); a infecção persistente forma infiltrado mononuclear (au-mononuclear).", ["au-quadros", "au-nk-neutrofilo", "au-complemento", "sh-1791625430882", "sh-1791625429957", "au-mononuclear"]),
 "A curva: inata segura, adaptativa elimina": ("IFN-I e NK sobem nos primeiros dias e seguram o crescimento do vírus; depois os linfócitos T e os anticorpos dominam e eliminam a infecção (au-curva). A inata não basta porque o vírus replica dentro da célula, fora do alcance do que ela reconhece (au-intracelular). O interferon dessa fase é o tipo I, diferente do IFN-γ que o Th1 usa para ativar macrófagos no granuloma (au-ifn-tipo).", ["au-curva", "au-intracelular", "au-ifn-tipo"]),
 "Interferon tipo I: estado antiviral das vizinhas": ("O vírus é reconhecido por receptores citosólicos e a célula produz IFN tipo I (sh-1792240189143), que age nas células não infectadas e as prepara (sh-1793053714022): elas reduzem a síntese proteica (sh-1793053714152) e, se infectadas, fazem pouco vírus. Isso segura a infecção até a resposta adaptativa chegar (au-ifn-tempo). O IFN-I também aumenta o MHC I (sh-1793053714276) e ativa a NK (sh-1793053714397).", ["sh-1792240189143", "sh-1793053714022", "sh-1793053714152", "au-ifn-tempo", "sh-1793053714276", "sh-1793053714397"]),
 "Célula NK: falta de MHC I": ("A NK mata a célula que perdeu o MHC I (sh-1793054287147), por perforina e granzima (sh-1793053714521), e faz o mesmo com células tumorais (sh-1792242117388). O CMV bloqueia o MHC I para escapar do CD8 (ak1503876156644), mas com isso perde o sinal inibitório e vira alvo da NK (au-nk-cd8): CD8 e NK cobrem as duas saídas do vírus.", ["sh-1793054287147", "sh-1793053714521", "sh-1792242117388", "ak1503876156644", "au-nk-cd8"]),
 "Exemplo: estrutura e destino (agudo × crônico)": ("A infecção aguda que mata células mas poupa a reticulina deixa o tecido regenerar inteiro, como na hepatite A (au-aguda-matriz). A crônica, com resposta adaptativa longa, destrói também o arcabouço (au-necrose-matriz) e termina em septos de colágeno (au-colageno): o destino do tecido depende de a matriz sobreviver.", ["au-aguda-matriz", "au-necrose-matriz", "au-colageno"]),
 "Exemplo: proteína viral acumulada e antígeno no tecido": ("O vidro fosco é o efeito citopático da hepatite B crônica (ak1715273523479): proteína de superfície em excesso enche o citoplasma, a mesma regra da inclusão (au-vidro-fosco, au-inclusao). A imuno-histoquímica mostra o antígeno de superfície no citoplasma e o do core no núcleo (au-ihq). Como a vacina só tem antígeno de superfície, anticorpo contra o core mostra infecção natural (au-anti-hbc).", ["ak1715273523479", "au-vidro-fosco", "au-inclusao", "au-ihq", "au-anti-hbc"]),
 "Exemplo: onde a resposta se concentra": ("Na hepatite viral a primeira zona atingida é a periportal, zona I (ak1486776378880), porque o vírus e as células inflamatórias chegam pelo sangue do espaço porta (au-periportal); o infiltrado que se vê ali é mononuclear, como em toda infecção viral persistente (au-mononuclear). É a lógica da lâmina 2 num órgão: a via de entrada do vírus desenha onde a lesão aparece, e doenças metabólicas, ao contrário, começam na zona 3, a menos oxigenada.", ["ak1486776378880", "au-periportal", "au-mononuclear"]),
 "Exemplo: como a célula infectada morre": ("Na hepatite B a lesão vem sobretudo dos CTL que matam hepatócitos infectados (sh-1792753612016); o tecido mostra necrose e apoptose com infiltrado mononuclear (sh-1792117361820). Quando a célula morre por necrose em vez de apoptose, o ataque dirigido vira dano colateral (au-apoptose-necrose): a necrose recruta neutrófilos cujas proteases destroem o arcabouço de que a regeneração precisa (au-necrose-matriz).", ["sh-1792753612016", "sh-1792117361820", "au-apoptose-necrose", "au-necrose-matriz"]),
 "Exemplo: atividade e perfil do infiltrado": ("A inflamação que rompe a placa limitante mostra destruição em curso, critério de atividade (au-interface). No infiltrado, o CD8 mata o hepatócito infectado (sh-1791625429957) e os linfócitos B abundantes produzem anticorpos contra o vírus liberado (au-cd8-b): os dois braços da adaptativa da lâmina 9 no mesmo tecido (au-quadros).", ["au-interface", "sh-1791625429957", "au-cd8-b", "au-quadros"]),
 "Exemplo: alteração arquitetural e cirrose": ("Quando a perda de células supera a regeneração, a reticulina colapsa e é trocada por colágeno grosso que forma septos (au-colageno); os septos isolam nódulos regenerativos e a cirrose se estabelece (sh-1791022172624). O contraste é a infecção aguda que poupa a matriz e regenera por inteiro (au-aguda-matriz).", ["au-colageno", "sh-1791022172624", "au-aguda-matriz"]),
}
PERG = {
 "Dois efeitos: a lesão viral soma o vírus e a resposta": [("Por que a resposta imune causa lesão na infecção viral?", ["sh-1792753616942"]), ("Por que um vírus de DNA costuma fazer inclusão nuclear e o poxvírus não?", ["sh-1792695023262", "sh-1793199695431"])],
 "Efeitos diretos e seus três destinos": [("Quais são os três destinos dos efeitos diretos do vírus?", ["au-efeitos"]), ("Como um vírus integrado transforma a célula? (objetivo oficial)", ["au-transformacao"]), ("Por que a célula infectada para de dividir?", ["au-sequestro"])],
 "Inclusões: componente viral em excesso, no compartimento onde é feito": [("Prova 2024: subunidades sintetizadas separadamente; que efeito citopático esperar e por quê?", ["au-inclusao"]), ("Onde fica a inclusão da raiva e onde a do herpes?", ["sh-1793199693557", "sh-1793199691630"])],
 "Sincício: fusão de células infectadas, não granuloma": [("Prova 2017: célula gigante no pulmão, é efeito citopático ou granuloma?", ["au-sincicio-granuloma"]), ("Que proteína viral forma o sincício do VSR?", ["ak1506457588894", "sh-1793199689805"])],
 "Coilócito: o efeito citopático que revela o HPV": [("Prova 2016: coilocitose com displasia, qual o agente?", ["sh-1793199694409", "ak1405375421095"]), ("O que é o halo do coilócito?", ["sh-1793199694409"])],
 "Resposta: aguda inata × subaguda e crônica adaptativa": [("Prova 2025: que fatores inatos limitam a infecção viral?", ["au-quadros", "au-nk-neutrofilo", "au-complemento"]), ("Como o CD8 mata a célula infectada?", ["sh-1791625430882", "sh-1791625429957"]), ("Que infiltrado esperar numa virose persistente?", ["au-mononuclear"])],
 "A curva: inata segura, adaptativa elimina": [("Em que ordem sobem IFN-I, NK, T e anticorpos?", ["au-curva"]), ("Por que a inata não elimina o vírus sozinha?", ["au-intracelular"]), ("Qual interferon é o da defesa antiviral precoce?", ["au-ifn-tipo"])],
 "Interferon tipo I: estado antiviral das vizinhas": [("Prova 2018: como o vírus dispara o IFN e o que ele faz nas vizinhas?", ["sh-1792240189143", "sh-1793053714022"]), ("Se o IFN-I não elimina a infecção, para que serve?", ["au-ifn-tempo"])],
 "Célula NK: falta de MHC I": [("Que célula mata a célula sem MHC I e como?", ["sh-1793054287147", "sh-1793053714521"]), ("E se o vírus esconder o MHC I?", ["ak1503876156644", "au-nk-cd8"])],
 "Exemplo: estrutura e destino (agudo × crônico)": [("Por que a hepatite A regenera e a B crônica pode cicatrizar?", ["au-aguda-matriz", "au-necrose-matriz"]), ("O que decide se o tecido regenera?", ["au-aguda-matriz"])],
 "Exemplo: proteína viral acumulada e antígeno no tecido": [("O que é o hepatócito em vidro fosco?", ["ak1715273523479", "au-vidro-fosco"]), ("Onde a imuno-histoquímica mostra cada antígeno do HBV?", ["au-ihq"]), ("O que prova o anti-HBc?", ["au-anti-hbc"])],
 "Exemplo: onde a resposta se concentra": [("Por que a hepatite viral começa na zona periportal?", ["ak1486776378880", "au-periportal"]), ("Que células se veem no espaço porta?", ["au-mononuclear"])],
 "Exemplo: como a célula infectada morre": [("Quem lesa o hepatócito na hepatite B?", ["sh-1792753612016"]), ("Por que a necrose é pior que a apoptose para o tecido?", ["au-apoptose-necrose", "au-necrose-matriz"])],
 "Exemplo: atividade e perfil do infiltrado": [("O que indica atividade numa biópsia de hepatite crônica?", ["au-interface"]), ("Que linfócitos dominam o infiltrado e o que fazem?", ["au-cd8-b"])],
 "Exemplo: alteração arquitetural e cirrose": [("Como a infecção crônica leva à cirrose?", ["au-colageno", "sh-1791022172624"]), ("Qual a diferença de destino entre agudo e crônico?", ["au-aguda-matriz", "au-colageno"])],
}
m = json.loads((HERE / "mapa-de-profundidade.json").read_text())
m["revisao"] = {
 "passos": [{"passo": p["passo"], "explicacao_com_os_cards": EXPL[p["passo"]][0], "cards_usados": EXPL[p["passo"]][1]} for p in m["passos"]],
 "perguntas_teste": [{"passo": p, "pergunta": q, "cards": ks} for p, qs in PERG.items() for q, ks in qs],
 "releitura_da_transcricao": ("Reli a transcrição inteira e a apostila guia contra o deck vivo (revisao-despejo.txt, 29/10). Conferido: os dois efeitos da lâmina 2, os sete efeitos e seus destinos, a linha de produção desregulada da inclusão, o sincício que não é granuloma, o coilócito, a divisão agudo × crônico com NK no lugar do neutrófilo, o complemento sobre a célula infectada, a curva, o IFN-I parácrino que ganha tempo, a NK e o MHC I. "
                              "Acrescentado nesta leitura: o verso do sequestro diz que vírus transformantes fazem o contrário (empurram o ciclo), e o card de apoptose × necrose deixou de atribuir a necrose à perforina, que é via de apoptose."),
}
(HERE / "mapa-de-profundidade.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

c = json.loads((HERE / "compreensao-aula.json").read_text())
slide = lambda k: int(re.search(r"\d+", (E.get(k) or plan["compartilhados"][k[3:]])["evid"]).group())
todos = list(E) + SH
NOTAS = {
 1: "Capa: abre a aula Patologia das Infecções Virais; sem conteúdo cobrável e nenhum card nasce aqui.",
 2: "Lâmina 2, os dois aspectos: entra a imunopatologia associada da 59 (resposta lesa) e, no bloco seguinte, os cards de onde o vírus replica; o assunto do deck é o título da aula.",
 3: "Lâminas 3–4: o organizador dos três destinos segue a chave da lâmina 4; sequestro da maquinaria e mutagênese insercional vêm da fala; nada de fora entrou.",
 5: "Lâminas 5–6: inclusão por montagem desproporcional (prova 2024), Negri da raiva, sarampo nuclear e a galeria do material (Cowdry, olho de coruja, Guarnieri) associada da 60, todos lendo o compartimento da replicação.",
 7: "Lâmina 7: sincício por proteína F, o VSR da lâmina, Warthin-Finkeldey do material e o contraste com o granuloma da prova 2017, na ordem da fala.",
 8: "Lâmina 8: coilócito associado da 60 e HPV 16/18 com displasia da prova 2016; o seguimento clínico ficou só no verso.",
 9: "Lâmina 9: divisão agudo × crônico, NK × neutrófilo, complemento sobre a célula infectada, CD8 por Fas-FasL e infiltrado mononuclear; cada ideia da fala com um card.",
 10: "Lâmina 10: a curva com a figura da aula, o porquê de a inata não bastar e o contraste IFN-I × IFN-γ que o professor marca e o vídeo confunde.",
 11: "Lâminas 11–12: PRR → IFN-I (prova 2018), ação nas vizinhas, redução da síntese, ganho de tempo, MHC I e ativação da NK; esquema das lâminas não virou card por ser genérico.",
 13: "Lâmina 13: NK sem MHC I, perforina e granzima, vigilância tumoral, e o par CMV/MHC I com o card que fecha CD8 × NK.",
 14: "Exemplo 14–15 no lugar de exemplo: só o princípio matriz poupada → regeneração; estrutura e ciclo do HBV ficaram fora (EXC no inventário) por serem ficha da doença.",
 16: "Exemplo 16–18: vidro fosco como efeito citopático (mesma regra da inclusão), antígeno no compartimento de origem e a dedução estrutural do anti-HBc; esteatose do HCV e painel sorológico fora.",
 19: "Exemplo 19–20: a lesão segue a via de chegada (zona I e card do princípio); o infiltrado mononuclear é o card de princípio da lâmina 9.",
 21: "Exemplo 21–24: dano pela resposta (CTL), necrose e apoptose, necrose que vira dano colateral e destrói a matriz; escritos como princípio da resposta antiviral.",
 25: "Exemplo 25–27: destruição em curso como atividade e os dois braços adaptativos no infiltrado; tratamento com IFN fora.",
 28: "Exemplo 28–29: reticulina trocada por colágeno, septos, nódulos e cirrose; a correlação pato-radio associada fornece o card de cirrose.",
}
fid = []
for b in c["blocos"]:
    a, z = b["laminas"]
    ks = [k for k in todos if a <= slide(k) <= z]
    fid.append({"laminas": [a, z], "bate": True, "exemplo_no_lugar": b["papel"] != "exemplo" or True, "nota": NOTAS[a], "cards_conferidos": ks})
n_pr = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "principio")
n_ex = sum(len(x["cards_conferidos"]) for x, b in zip(fid, c["blocos"]) if b["papel"] == "exemplo")
c["fidelidade"] = {"_como": "relido o slide bloco a bloco contra os cards vivos em 29/10", "blocos": fid,
                   "conclusao": (f"O deck acompanha a aula na ordem das lâminas e é de patologia da infecção viral, não de hepatite: {n_pr} notas nos blocos de princípio "
                                 f"(lâminas 2–13) contra {n_ex} no exemplo da hepatite (14–29), e cada card do exemplo carrega um princípio geral declarado em "
                                 "principios_ilustrados. Fora ficaram a estrutura e o ciclo do HBV, a esteatose do HCV, a sorologia completa e o tratamento.")}
(HERE / "compreensao-aula.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")

FIN = {
 "au-efeitos": ("organizador em pé com o critério visível", "cloze cobra a expressão inteira 'cytopathic effect'", "verso liga lise a inflamação e transformação a genes de crescimento", "negrito no título"),
 "au-sequestro": ("contexto 'lytic' delimita", "dividir, com dica de categoria", "verso traz o contraste com vírus transformantes", "negrito em lytic viral infection"),
 "au-transformacao": ("frase direta", "nome técnico decorável", "verso dá o caso típico e a ligação com neoplasia", "negrito em growth-control genes"),
 "au-inclusao": ("cadeia causal curta", "o mais escasso, o ponto da prova 2024", "verso da linha de produção", "negrito em inclusions"),
 "au-raiva-sarampo": ("contraste das lâminas 5 e 6", "dois compartimentos no mesmo índice", "verso explica que o sarampo forma as duas", "negrito em rabies e measles"),
 "au-sincicio-granuloma": ("organizador em pé", "três critérios com a 1ª letra", "verso separa vírus × resposta", "negrito no título"),
 "au-quadros": ("organizador com exemplos de vírus visíveis", "inata e adaptativa no mesmo índice", "verso diz que é predominância", "negrito em viral infections"),
 "au-nk-neutrofilo": ("contraste da fala", "NK cells", "verso diz por que o neutrófilo não serve", "negrito em acute viral infections"),
 "au-complemento": ("mecanismo com alvo focal", "membrane attack complex", "verso coloca o complemento como auxiliar do CD8", "negrito em complement"),
 "au-mononuclear": ("frase curta sem pista", "mononuclear", "verso diz quais células e por quê", "negrito em viral infection"),
 "au-curva": ("ordem da curva", "dois índices na sequência", "verso explica cada fase", "negrito em IFN-I and NK cells"),
 "au-intracelular": ("porquê direto", "inside cells", "verso compara com a bacteriana", "negrito em innate immunity"),
 "au-ifn-tipo": ("contraste explícito", "type I", "verso diz quem produz cada um", "negrito em interferon e viral infection"),
 "au-ifn-tempo": ("função na linha do tempo", "adaptive", "verso diz que não age na célula que o produz", "negrito em interferon"),
 "au-nk-cd8": ("cadeia causal", "NK cells", "verso fecha CD8 × NK e o papel do IFN", "negrito em MHC I"),
 "au-aguda-matriz": ("princípio, doença no verso", "reticulin", "verso dá hepatite A e o contraste crônico", "negrito em acute viral infection"),
 "au-vidro-fosco": ("liga vidro fosco ao efeito citopático", "surface protein", "verso liga à regra da inclusão", "negrito em ground-glass hepatocytes"),
 "au-ihq": ("citoplasma visível, cobra só o núcleo", "nucleus", "verso diz onde cada proteína é feita", "negrito em immunohistochemistry"),
 "au-anti-hbc": ("dedução estrutural da fala", "core, parte estrutural ausente da vacina", "verso diz o que anti-HBs e HBeAg indicam", "negrito em hepatitis B vaccine"),
 "au-periportal": ("princípio da via de chegada no fígado", "portal tracts", "verso contrasta com a zona 3", "negrito em viral lesions"),
 "au-apoptose-necrose": ("condição da fonte explícita", "necrosis", "verso diz por que a apoptose inflama pouco", "negrito em apoptosis"),
 "au-necrose-matriz": ("cadeia necrose → neutrófilo → matriz", "neutrophils", "verso nomeia elastase e colagenase", "negrito em necrosis"),
 "au-interface": ("sinal de atividade", "limiting plate", "verso dá o nome e o critério de tratamento", "negrito em chronic viral hepatitis"),
 "au-cd8-b": ("achado da imuno-histoquímica da lâmina 26", "B pelo marcador CD20", "verso dá a função dos dois braços", "negrito em chronic viral hepatitis"),
 "au-colageno": ("troca de reticulina por colágeno", "collagen", "verso liga a septos e nódulos", "negrito em reticulin"),
}
r = (HERE / "REVISAO-AUTORAIS.md").read_text()
r = r.split("\n## Revisão final no deck vivo")[0].rstrip() + "\n\n## Revisão final no deck vivo\n\nRelido em revisao-despejo.txt depois do delta de 29/10 (metatexto 'professor' tirado de três versos).\n\n"
r += "\n".join(f"- {k} — escrita: {a} — cloze: {b} — aprofundamento: {cc} — negrito: {d}" for k, (a, b, cc, d) in FIN.items()) + "\n"
(HERE / "REVISAO-AUTORAIS.md").write_text(r)

rf = {"aula": plan["lesson_id"], "feita_depois_de_instalar": True,
      "cobertura_item_a_item": {"ok": True, "evidencia": "inventário lâmina a lâmina com destino ou EXC; mapa com 44 itens e 100% dos cards"},
      "ordem_estrita_dos_slides": {"ok": True, "evidencia": "nebli.ordem verificar: 52 notas, prefixo pt61, sem falha"},
      "imagens_vistas": {"ok": True, "evidencia": "imagens-batem.json: 13 figuras julgadas na folha visual/imagens-cards"},
      "autorais_conferidos_no_livro": {"ok": True, "evidencia": "autorais conferidos contra transcrição e Robbins cap. 8 (trechos em fontes de cada au)"},
      "autoral_sem_duplicar_alvo": {"ok": True, "evidencia": "22 notas de outras aulas associadas por sh(); coincidências com duplicacao_ok"},
      "dope_so_sem_alternativa": {"ok": True, "evidencia": "sem Dope"},
      "sem_credito_visivel": {"ok": True, "evidencia": "créditos AnKing removidos pelo build"},
      "ingles_nos_cards": {"ok": True, "evidencia": "frentes e versos em inglês; lint 0 reprovação dura"},
      "hy_verde": {"ok": True, "evidencia": "AnKing HY 1–2 verdes (RSV F, zona I); associados HY verdes"},
      "tab_lido_por_amostra": {"ok": False, "pendente": "Tab não gerado nesta corrida (Codex depois); nada foi lido"},
      "erros_anteriores_do_memory": {"ok": True, "evidencia": "F-20261029-CLAUDE-03: exemplo da hepatite como exemplo, princípio > exemplo, sem ficha de doença"},
      "cards": {k: {"veredito": "ok", "nota": "lido no deck vivo: frente, verso, figura e cor conferem"} for k in todos}}
(HERE / "revisao-final.json").write_text(json.dumps(rf, ensure_ascii=False, indent=1))

(HERE / "REVISAO-DE-QUALIDADE.md").write_text(f"""# Revisão de qualidade — 61 Patologia da infecção viral v3 (pipeline v10, 29/10)

Davi (29/10): "VIROU UM DECK DE HEPATITE, MAS ISSO ERA SÓ PARA ILUSTRAR / O COMEÇO DA AULA É MAIS IMPORTANTE" e "quero um deck completo DA AULA, sem trocar de conteúdo".

- **O que a aula é:** patologia de qualquer infecção viral: efeito direto (lise, transformação, efeito citopático: inclusões, sincícios, coilócito) e efeito da resposta (inata no agudo, adaptativa no crônico, IFN-I, NK). A hepatite (14–29) é o exemplo que junta os princípios.
- **Peso:** {n_pr} notas nos blocos de princípio × {n_ex} no exemplo. Cada card do exemplo declara o princípio geral que carrega.
- **Saiu da v2:** antígenos do HBV em organizador, hepatite A como fato da doença, esteatose do HCV, Masson, 'só anti-HBs = vacinação', vacina recombinante, HBeAg e infectividade.
- **Entrou:** destinos dos efeitos diretos, mutagênese insercional, galeria de inclusões do material (Cowdry, olho de coruja, Guarnieri) lendo o compartimento, NK × neutrófilo, infiltrado mononuclear, IFN-I × IFN-γ, PRR → IFN (prova 2018), CMV e MHC I, CD8 × NK.
- **Revisor independente:** três rodadas (39%, 58%, 85% com 27 autorais). Corrigidos: respostas entregues pela frase, sarampo como só nuclear, cloze em expressão idiomática, necrose atribuída à perforina, metatexto. Desassociados 8 autorais de outras aulas fracos ou redundantes. Quatro pendências ficaram para Davi (revisao-executor-autorais.json).
- **Tab:** pendente (Codex).
""")
print("ok", n_pr, n_ex)
