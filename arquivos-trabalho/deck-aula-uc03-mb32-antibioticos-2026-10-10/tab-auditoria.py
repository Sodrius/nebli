"""Revisa os Tabs afetados pela segunda auditoria científica, sem tocar os cards."""
from datetime import datetime, timezone

from nebli.decks import Anki
from nebli.explicacoes import STYLE, item, open_store, problema_estilo, style_version

REPLACE = {
1791668517165: [
    ("ela surge quando o alvo da droga existe na bactéria e não em nós", "ela surge quando o alvo está ausente no humano ou é suficientemente diferente para que a droga prefira o alvo bacteriano"),
    ("então drogas que a bloqueiam não nos atingem", "então drogas que a bloqueiam tendem a poupar nossas células"),
    ("o que permite bloquear só o bacteriano", "o que permite bloquear preferencialmente o bacteriano"),
    ("e por isso pode ser inibida isoladamente", "e por isso pode ser inibida com seletividade, embora não absoluta"),
],
1791668519063: [
    ("Drogas bactericidas matam a bactéria; as bacteriostáticas só a paralisam.", "Em ensaios, uma droga bactericida reduz bactérias viáveis; uma bacteriostática impede a multiplicação sem necessariamente matá-las."),
    ("um bacteriostático depende do sistema imune para eliminar as bactérias paradas. Nos imunocomprometidos, esse sistema falha, então a bactéria ficaria viva e voltaria a crescer.", "uma resposta imune fraca pode dificultar a eliminação de bactérias apenas inibidas, mas isso varia com o patógeno e com a condição do paciente."),
    ("Em ambos os casos, a droga precisa matar sozinha.", "Por isso, em algumas dessas situações, uma opção bactericida pode ser preferida quando há atividade e penetração adequadas."),
    ("infecção do sistema nervoso central é rapidamente fatal e não tolera erradicação incompleta, o que reforça a necessidade de bactericida.", "na meningite bacteriana, rapidez e penetração no líquor são essenciais; a classificação in vitro não substitui a avaliação do fármaco, do patógeno e do foco."),
],
1791668520464: [
    ("por essa diferença de estrutura, as β-lactamases comuns (penicilinases) reconhecem mal as cefalosporinas e não conseguem hidrolisá-las com facilidade. Assim, a cefalosporina continua intacta e chega às PBPs, o que explica o seu papel contra muitas bactérias resistentes à penicilina.", "a estabilidade depende da cefalosporina e da enzima presente na bactéria. Uma penicilinase pode poupar certos fármacos, mas ESBL e AmpC hidrolisam muitas cefalosporinas; se a droga for destruída, ela não alcança as PBPs em quantidade eficaz."),
    ("a resistência não é absoluta. Algumas bactérias produzem cefalosporinases (enzimas específicas) e, nesse caso, as cefalosporinas voltam a ser destruídas e a bactéria fica resistente.", "não existe uma propriedade universal 'resistente à β-lactamase' para toda a classe. É preciso interpretar a enzima provável e o resultado de suscetibilidade do isolado."),
],
1791668521089: [
    ("então continua intacto mesmo em bactérias que as produzem e consegue ligar-se às PBPs e bloquear a parede.", "por isso a MBL isoladamente não o hidrolisa. Entretanto, uma bactéria pode produzir ao mesmo tempo ESBL, AmpC ou outra β-lactamase que inative aztreonam; o resultado do antibiograma decide se ele permanece ativo."),
    ("isso não o torna imune a tudo, porque as ESBL e as KPC (carbapenemases) ainda o hidrolisam.", "estabilidade à MBL não significa eficácia da monoterapia contra todo produtor de MBL: enzimas coexistentes podem eliminar essa vantagem."),
],
1791668522214: [
    ("ao se encaixar no 23S, o macrolídeo obstrui o canal por onde a cadeia nascente sai e atrapalha a transpeptidação. Sem o ribossomo conseguir andar, a translocação também não ocorre. A cadeia não cresce e a síntese de proteínas para.", "ao se ligar ao 23S, o macrolídeo estreita o túnel por onde sai a cadeia nascente. O peptídeo em formação não progride normalmente, a elongação pode parar e a bactéria perde capacidade de produzir proteínas. Isso não é o bloqueio direto da formação da ligação peptídica típico de outros inibidores."),
    ("que bloqueia o avanço do ribossomo", "que prejudica a elongação pelo túnel de saída"),
],
1791668523989: [
    ("carbapenêmicos (imipenem, meropenem) são β-lactâmicos que precisam chegar ao espaço periplasmático para agir. Na Pseudomonas, o canal principal por onde eles entram é a porina OprD.", "carbapenêmicos são β-lactâmicos que precisam chegar ao espaço periplasmático para agir. A porina OprD é particularmente importante para a entrada do imipeném em Pseudomonas."),
    ("O carbapenêmico não consegue atravessar a membrana externa, não alcança as PBPs e não mata a bactéria. A membrana fica impermeável a ele.", "A entrada de imipeném cai, menos droga alcança as PBPs e a resistência pode aumentar. Isso não torna a membrana impermeável a todos os carbapenêmicos; meropeném requer interpretação própria."),
],
1791668524388: [
    ("Com menos atração elétrica, a colistina quase não se liga ao LPS e a membrana permanece intacta, então a droga perde efeito.", "Com menos atração elétrica, a ligação da colistina ao LPS pode cair e a CIM pode subir. O fenótipo depende do alelo e de sua expressão; a presença do gene sozinha não prova resistência clínica."),
],
1791668524763: [
    ("Por isso a mutação do alvo é o mecanismo central, e vale tanto para Gram-negativas quanto para Gram-positivas.", "Por isso a alteração do alvo pode gerar resistência. Qual topoisomerase é o alvo principal varia entre espécies e fluoroquinolonas."),
    ("Em algumas Gram-positivas ela é o alvo primário, mas gyrA continua sendo a mutação de referência.", "Em algumas Gram-positivas a topoisomerase IV é o alvo primário; mutações em gyrA e parC/grlA podem se somar."),
],
1791668525138: [
    ("o MRSA carrega o gene mecA", "a maioria dos MRSA carrega o gene mecA"),
    ("Para detectar MRSA, pesquisa-se o mecA ou a PBP2a.", "Na investigação de MRSA, mecA ou PBP2a são alvos comuns, mas cepas com mecC também existem."),
],
1791668526411: [
    ("Um MIC baixo significa que basta pouco fármaco para inibir a bactéria, então a droga é muito ativa contra ela.", "Dentro do mesmo par bactéria–droga, uma CIM menor indica inibição com menor concentração; não se comparam valores brutos de fármacos distintos."),
    ("Se o MIC está abaixo do breakpoint", "Se a CIM está no ponto de corte sensível ou abaixo dele"),
    ("Se o MIC fica acima, a dose necessária seria inatingível ou tóxica, e a cepa é considerada resistente.", "Acima desse limite, a interpretação depende das faixas intermediária e resistente do padrão adotado, além da exposição prevista."),
],
}

FULL = {
1791668517539: """Base: tetraciclinas são antibióticos que se ligam à subunidade 30S bacteriana. Algumas se ligam também ao cálcio, e esse composto pode se depositar em dentes e ossos durante o desenvolvimento.
Por quê: quando há exposição fetal ou infantil relevante, a droga pode alcançar tecidos que estão mineralizando. Ao se associar ao cálcio desses tecidos, pode permanecer na dentição em formação e provocar alteração de cor. A relação depende do medicamento, da idade, da duração e da dose, portanto não é uma consequência inevitável de qualquer contato com a classe.
Por quê: a formação dentária atravessa etapas diferentes da gestação e infância; por isso o momento da exposição ajuda a definir o risco. A associação química com íons divalentes também reduz a absorção oral quando algumas tetraciclinas são tomadas com leite ou antiácidos.
Mais a fundo: cursos curtos de doxiciclina podem ser indicados em circunstâncias específicas, inclusive na infância; amamentação não é contraindicação categórica para toda exposição breve. A decisão clínica considera benefício e risco.
Na aula: a toxicidade em dentes e ossos ilustra que seletividade para a bactéria não elimina efeitos no hospedeiro.""",
1791668522358: """Base: a parede de bactérias Gram-negativas é coberta por uma membrana externa rica em LPS. Bactérias Gram-positivas não possuem essa barreira externa, embora tenham uma camada espessa de peptidoglicano. Macrolídeos precisam alcançar o ribossomo dentro da bactéria para impedir síntese proteica.
Por quê: a entrada por membranas e porinas pode limitar a atividade de algumas moléculas contra diversos bacilos entéricos Gram-negativos. Isso ajuda a explicar por que a cobertura clássica de macrolídeos favorece muitos patógenos Gram-positivos.
Por quê: a classe, porém, não é homogênea. A azitromicina tem atividade contra alguns Gram-negativos e contra agentes chamados atípicos; por isso não se pode transformar a barreira externa em proibição absoluta de atividade.
Mais a fundo: espectro efetivo depende da molécula, da espécie, da resistência e da concentração no local da infecção. O antibiograma e o contexto clínico importam mais que uma regra baseada apenas na coloração de Gram.
Na aula: esse exemplo mostra como a chegada do antibiótico ao ribossomo influencia seu espectro, mesmo quando o alvo existe em várias bactérias.""",
1791668526914: """Base: a CIM é a menor concentração que impede crescimento visível de uma bactéria no laboratório. Cmax é o pico de concentração que um antibiótico atinge no paciente após a dose. Dividir Cmax pela CIM compara o pico alcançado com a concentração que inibe o isolado.
Por quê: para antibióticos cuja eficácia depende da intensidade do pico, um Cmax/MIC maior pode acompanhar melhor atividade. Mas essa não é a única forma de exposição relevante. Em outras classes, importa por quanto tempo a concentração permanece acima da CIM ou a exposição total ao longo do dia.
Por quê: o sítio da infecção também muda quanto fármaco chega à bactéria. Uma concentração sanguínea pode não representar a concentração no líquor ou em outro tecido, e o resultado in vitro não substitui a farmacocinética real.
Mais a fundo: os números gerais de 4–8 vezes no sangue e 10 vezes no líquor mostrados na lâmina são heurísticas, não metas universais para todas as drogas e microrganismos. O índice PK/PD e a meta dependem da classe, espécie e situação clínica.
Na aula: a relação Cmax/CIM faz a ponte entre o ensaio de diluição e a exposição alcançada durante o tratamento.""",
}

UNCHANGED_MEANING = {1791668521716, 1791668527289}
ALL = set(REPLACE) | set(FULL) | UNCHANGED_MEANING

if __name__ == "__main__":
    A = Anki(); db = open_store(); version = style_version(STYLE.read_text(encoding="utf-8"))
    stamp = datetime.now(timezone.utc).isoformat()
    cards = A("cardsInfo", cards=sorted(ALL))
    if {c["cardId"] for c in cards} != ALL:
        raise RuntimeError("Card da auditoria não encontrado")
    for card in cards:
        cid = card["cardId"]
        old = db.execute("select texto from explicacoes where card_id=? and status='ok'", (cid,)).fetchone()
        if not old or not old[0]:
            raise RuntimeError(f"Tab anterior ausente: {cid}")
        value = FULL.get(cid, old[0])
        if cid in REPLACE:
            for before, after in REPLACE[cid]:
                if value.count(before) != 1:
                    raise RuntimeError(f"Trecho de revisão não é único em {cid}: {before[:70]}")
                value = value.replace(before, after)
        if issue := problema_estilo(value):
            raise RuntimeError(f"{cid}: {issue}")
        payload, digest, nid = item(A, card)
        db.execute("insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)",
                   (cid, nid, digest, "ok", value, None, version, "manual-codex-auditado", stamp))
    db.commit()
    print(f"{len(cards)} Tabs conferidos, incluindo {len(UNCHANGED_MEANING)} cujo conteúdo permaneceu correto")
