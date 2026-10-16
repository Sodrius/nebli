"""Enxuga Tabs que atravessaram a fronteira das aulas específicas de imagem."""
from nebli import explicacoes


TEXTOS = {
    1792141769157: """Um contraste exógeno é uma substância administrada ao paciente para tornar uma estrutura mais distinguível do tecido vizinho. Como cada método de imagem registra uma propriedade diferente, o agente precisa ser compatível com o método: iodo na tomografia, gadolínio na ressonância e microbolhas no ultrassom.

As microbolhas são pequenas bolhas de gás que permanecem dentro dos vasos e produzem ecos intensos. Assim, realçam o sangue e permitem observar perfusão e vascularização ao ultrassom. A ideia importante é funcional: elas tornam visível o compartimento vascular; a física detalhada do eco pertence ao estudo específico do ultrassom.""",
    1792141769158: """Na tomografia, tecidos vizinhos podem ter aparência semelhante e esconder vasos ou lesões. O contraste iodado é administrado para aumentar essa diferença: por atenuar fortemente os raios X, deixa mais claros os vasos e os tecidos que o recebem.

A distribuição do iodo, e não apenas sua presença, é o que informa: uma região que recebe muito contraste é bem vascularizada ou tem permeabilidade aumentada, enquanto uma que não recebe permanece menos destacada. O princípio físico detalhado e as janelas de visualização ficam para o estudo específico da tomografia.""",
    1792141769159: """Na ressonância magnética, o contraste entre tecidos vem do sinal dos núcleos de hidrogênio, sobretudo na água e na gordura. Um agente exógeno pode modificar esse sinal e tornar mais evidente uma região vascularizada ou com alteração da barreira entre sangue e tecido.

O gadolínio é o agente típico: ele altera o comportamento magnético da água ao redor e costuma aumentar o brilho das regiões que o captam em imagens ponderadas em T1. Para organizar os métodos, iodo realça a tomografia, gadolínio realça a ressonância e microbolhas realçam o ultrassom; os detalhes de T1 e T2 pertencem ao estudo específico da ressonância.""",
    1792141772957: """A ressonância magnética não usa raios X. Em uma frase, ela combina campo magnético, gradientes espaciais e pulsos de radiofrequência para localizar o sinal dos núcleos de hidrogênio dos tecidos e transformá-lo em imagem.

Essa origem do sinal explica duas características práticas: não há radiação ionizante e existe excelente diferenciação entre tecidos moles. A tomografia continua sendo mais rápida e muito útil para osso, pulmão e urgências; a escolha entre os métodos depende da estrutura e da pergunta diagnóstica, enquanto a física detalhada da ressonância e de T1/T2 fica para seu estudo específico.""",
    1792141773207: """Resolução de contraste é a capacidade de distinguir tecidos vizinhos que têm aparência parecida; resolução espacial é a capacidade de separar detalhes pequenos. Um exame pode ter ótimo detalhe geométrico e ainda mostrar dois tecidos moles quase no mesmo tom.

A ressonância magnética tem excelente resolução de contraste porque permite obter sinais diferentes da água e da gordura dos tecidos, enquanto radiografia e tomografia dependem da atenuação dos raios X. Por isso ela se destaca em cérebro, medula, articulações e músculos. Os ajustes de sequência que produzem esse contraste, como T1 e T2, ficam para o estudo específico da ressonância.""",
    1792141774957: """Cada método usa um vocabulário que descreve a propriedade transformada em imagem. Na ressonância magnética, essa propriedade é a intensidade do sinal: uma região hiperintensa produz sinal relativamente forte e aparece clara; uma região hipointensa produz sinal relativamente fraco e aparece escura.

Esses termos não nomeiam uma composição fixa, porque a aparência depende da sequência escolhida; T1 e T2 serão aprofundados no estudo específico da ressonância. O contraste útil aqui é linguístico: radiografia usa radiopaco e radiolucente, tomografia usa hiperatenuante e hipoatenuante, ultrassom usa hiperecoico e hipoecoico ou anecoico, e ressonância usa hiperintenso e hipointenso.""",
}


def main():
    db = explicacoes.open_store()
    version = explicacoes.style_version(explicacoes.STYLE.read_text(encoding="utf-8"))
    for card_id, texto in TEXTOS.items():
        problema = explicacoes.problema_estilo(texto)
        if problema:
            raise SystemExit(f"{card_id}: {problema}")
        changed = db.execute(
            "update explicacoes set status='ok', texto=?, motivo=null, estilo=?, modelo='curadoria-codex', gerado_em=datetime('now','localtime') where card_id=?",
            (texto, version, card_id),
        ).rowcount
        if changed != 1:
            raise SystemExit(f"card ausente: {card_id}")
    db.commit()
    print(f"{len(TEXTOS)} Tabs ajustados à fronteira da aula 02.")


if __name__ == "__main__":
    main()
