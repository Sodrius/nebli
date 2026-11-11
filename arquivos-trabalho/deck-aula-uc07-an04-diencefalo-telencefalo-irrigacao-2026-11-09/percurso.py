"""Percurso da aula 04 (27/10/2026), sem lâminas no Drive (pasta pessoal '05 - Diencéfalo…' e da turma 'Aula 04 Diencéfalo' e
'Aula 06 Núcleos da Base' vazias; Davi 08/11: "se não tem slide mas tem transcrição segue"). Cada unidade faz o papel de uma lâmina:
ordem = fala do professor (T1 diencéfalo, T2 telencéfalo, Núcleos da base pela apostila-guia, T3 irrigação, T4 prática no laboratório).
Núcleos da base não têm vídeo: a apostila-guia (Aula 6 cap 5) e o manuscrito dos veteranos (p24) são o roteiro desse bloco.
Gera fontes/slides.txt e percurso-aula.md."""
from pathlib import Path

HERE = Path(__file__).parent
T1, T2, T3, T4 = "T1 diencéfalo (Jacomo)", "T2 telencéfalo (Jacomo)", "T3 irrigação (Jacomo)", "T4 prática"
AP = "APOSTILA Aula 6 cap 5 + veteranos p24"
U = [
 # ---------------- DIENCÉFALO (T1, Prof. Alfredo Jacomo, lousa + imagens) ----------------
 (T1, "00-03", "Divisão anatômica e lugar do diencéfalo",
  "Encéfalo = cérebro + cerebelo + tronco encefálico; cérebro = telencéfalo + diencéfalo (cérebro não é sinônimo de encéfalo). O diencéfalo é a parte menor do cérebro."),
 (T1, "03-05", "Diencéfalo escondido pelo telencéfalo",
  "O telencéfalo cresce tanto que envolve e esconde o diencéfalo: na vista lateral só se vê telencéfalo e cerebelo; para ver o diencéfalo é preciso cortar no plano sagital mediano e olhar a vista medial."),
 (T1, "06-08", "Partes do diencéfalo",
  "Tálamo (a maior), hipotálamo, epitálamo e subtálamo. Alguns autores separam uma quinta parte, o metatálamo (corpos geniculados); o professor a inclui no tálamo, como a maioria dos autores."),
 (T1, "08-09", "Vista medial: ventrículo lateral e corpo caloso acima",
  "Na vista medial do esquema, acima do diencéfalo fica o ventrículo lateral (líquor) e, acima dele, o corpo caloso; abaixo, o tronco encefálico; atrás, o cerebelo."),
 (T1, "09-11", "Sulco hipotalâmico divide tálamo e hipotálamo",
  "Na vista medial, um sulco raso, o sulco hipotalâmico, separa o tálamo (acima) do hipotálamo (abaixo); o epitálamo fica na parte posterior. O subtálamo não aparece na vista medial porque fica lateral ao hipotálamo."),
 (T1, "11-13", "Aderência intertalâmica",
  "Estrutura ovalada que liga o tálamo de um lado ao do outro, atravessando o III ventrículo; o corpo caloso também liga os dois hemisférios. Apostila: ausente em cerca de 30% das pessoas."),
 (T1, "13-17", "Divisão do tálamo: tubérculo anterior, pulvinar e corpos geniculados",
  "Na vista superior, a parte anterossuperior do tálamo é o tubérculo anterior; a posterior é o pulvinar, onde ficam duas saliências, os corpos geniculados medial e lateral. Quem separa os geniculados chama essa região de metatálamo."),
 (T1, "18-26", "Limites do tálamo",
  "Superior: ventrículo lateral. Inferior e medial: hipotálamo. Inferior e lateral: subtálamo. Medial: III ventrículo (espaço entre os dois tálamos). Lateral: cápsula interna (já do telencéfalo). O corte coronal visto por trás mostra corpo caloso, ventrículo lateral, tálamos com aderência e III ventrículo no meio."),
 (T1, "26-27", "Núcleos = corpos celulares no SNC; tálamo é cinzento",
  "Acúmulo de corpos celulares fora do SNC é gânglio; dentro do SNC é núcleo. O tálamo é praticamente todo substância cinzenta, organizada em núcleos."),
 (T1, "29-30", "Núcleos anteriores do tálamo: sistema límbico",
  "No tubérculo anterior ficam os núcleos anteriores, ligados ao sistema límbico (comportamento emocional); a aula de sistema límbico volta a eles."),
 (T1, "30-32", "Núcleos posteriores: corpos geniculados (visão e audição)",
  "Na região posterior (pulvinar) ficam os corpos geniculados. Olhando por trás, o lateral fica mais alto e o medial mais baixo: o olho é mais alto que a orelha, então geniculado lateral = visão e geniculado medial = audição."),
 (T1, "32-34", "Núcleos laterais, mediais e medianos",
  "Laterais: motricidade e sensibilidade. Mediais: sistema límbico (como os anteriores). Medianos: pouco conhecidos, os autores não descrevem bem a função. A fisiologia detalha."),
 (T1, "35-37", "Limites do hipotálamo: superior, lateral, medial",
  "Superior: tálamo. Lateral: subtálamo. Medial: III ventrículo."),
 (T1, "37-43", "Limite inferior do hipotálamo",
  "De anterior para posterior: quiasma óptico (inferior anterior), túber cinéreo + infundíbulo (inferior médio) e corpos mamilares (inferior posterior). O infundíbulo (haste) prende a hipófise ao túber cinéreo. A comissura anterior fica na frente e não faz parte do limite inferior."),
 (T1, "43-46", "Divisão do hipotálamo: supraóptica, tuberal, mamilar",
  "Cada região leva o nome da estrutura do assoalho abaixo dela: região supraóptica (acima do quiasma óptico), tuberal (acima do túber cinéreo) e mamilar (acima dos corpos mamilares)."),
 (T1, "46-50", "Núcleos do hipotálamo por região",
  "Supraóptica: núcleos supraóptico, supraquiasmático e paraventricular. Tuberal: ventromedial, dorsomedial e arqueado. Mamilar: mamilares e posteriores. Fisiologia explica as funções; aqui, nome e região."),
 (T1, "50-52", "Epitálamo: posição",
  "O epitálamo fica na região posterior do diencéfalo (limita posteriormente o III ventrículo, acima do sulco hipotalâmico)."),
 (T1, "52-54", "Estruturas do epitálamo",
  "Corpo pineal (glândula pineal, epífise) — o mais visível; núcleo da habênula e comissura das habênulas (sistema límbico); comissura posterior. No laboratório se veem o corpo pineal e a comissura posterior."),
 (T1, "54-57", "Subtálamo: limites",
  "Superior: tálamo. Inferior: mesencéfalo (parte mais alta do tronco). Medial: hipotálamo. Lateral: cápsula interna. Difícil de ver na peça; os cortes mostram os limites."),
 (T1, "57-58", "Núcleo subtalâmico: motricidade",
  "Os núcleos do subtálamo são os núcleos subtalâmicos, relacionados com a motricidade (regulação somática)."),
 (T1, "59-71", "Imagens: corte sagital, corte coronal pelos corpos mamilares e vista posterior",
  "Revisão nas imagens: vista medial com fórnix, corpo caloso, sulco hipotalâmico, aderência, comissuras anterior e posterior, quiasma, túber, infundíbulo, hipófise e corpo mamilar; corte coronal no nível dos corpos mamilares com septo pelúcido entre os ventrículos laterais; vista posterior com pulvinar, geniculados e corpo pineal. O septo pelúcido fecha medialmente o ventrículo lateral."),
 # ---------------- TELENCÉFALO (T2, Prof. Alfredo Jacomo) ----------------
 (T2, "00-02", "Telencéfalo: a maior parte do cérebro",
  "Cérebro = diencéfalo + telencéfalo; o telencéfalo é a maior parte e esconde o diencéfalo. Apostila: dois hemisférios e a lâmina terminal."),
 (T2, "02-05", "Três faces do hemisfério",
  "Face superolateral, face medial (vista após o corte sagital mediano) e face inferior (só vista depois de retirar cerebelo, tronco e diencéfalo)."),
 (T2, "06-07", "Giros e sulcos",
  "As saliências do telencéfalo são os giros; os cortes entre eles são os sulcos."),
 (T2, "07-10", "Três sulcos da face superolateral",
  "Sulco lateral (de Sylvius), sulco central (de Rolando) e sulco semilunar (lunatus), este menos constante e menos evidente."),
 (T2, "10-11", "Quatro lobos pelos ossos",
  "Os três sulcos dividem o telencéfalo em lobos que coincidem com os ossos do crânio: frontal (à frente do sulco central), parietal (entre o central e o semilunar), occipital (atrás do semilunar) e temporal (abaixo do sulco lateral)."),
 (T2, "11-12", "Sulco central vai de ponta a ponta",
  "O sulco central é o único que vai da margem superior do hemisfério até o sulco lateral."),
 (T2, "12-13", "Giro pré-central: principal área motora",
  "O sulco pré-central é paralelo ao central; entre os dois fica o giro pré-central, a principal área motora (de onde sai a ordem para o movimento)."),
 (T2, "14-16", "Giros frontais superior, médio e inferior",
  "Os sulcos frontais superior e inferior, anteroposteriores, delimitam os giros frontais superior, médio e inferior."),
 (T2, "16-21", "Giro frontal inferior esquerdo: área de Broca",
  "Só no hemisfério esquerdo, os ramos anterior e ascendente do sulco lateral dividem o giro frontal inferior em partes orbital, triangular e opercular. Esse conjunto é a área (giro) de Broca, centro da palavra falada: lesão aí faz perder a capacidade de articular a palavra."),
 (T2, "21-23", "Giro pós-central: área somestésica",
  "O sulco pós-central é paralelo ao central; entre os dois fica o giro pós-central, a principal área somestésica, onde a sensibilidade se torna consciente."),
 (T2, "23-28", "Lóbulos parietais; giros supramarginal e angular",
  "O sulco intraparietal divide o lobo parietal em lóbulo parietal superior e inferior (lóbulo: maior que giro e menor que lobo). Um sulco sem nome divide o lóbulo parietal inferior em giro supramarginal (anterior) e giro angular."),
 (T2, "28", "Lobo occipital na face lateral",
  "Na face lateral, o lobo occipital não tem nada importante para a aula; o importante dele está na face medial."),
 (T2, "28-30", "Giros temporais superior, médio e inferior",
  "Os sulcos temporais superior e inferior dividem o lobo temporal em giros temporais superior, médio e inferior."),
 (T2, "30-32 e 50-51", "Lobo da ínsula",
  "Abrindo o sulco lateral aparece, no fundo, o lobo da ínsula, que não corresponde a osso nenhum. Tem giros curtos (anteriores), o sulco central da ínsula e o giro longo (posterior)."),
 (T2, "33-36", "Corpo caloso e suas partes",
  "Na face medial, a estrutura mais evidente é o corpo caloso, que liga os dois hemisférios; partes, de anterior para posterior: rostro, joelho, tronco e esplênio. Abaixo dele, o fórnix e o ventrículo lateral."),
 (T2, "37-38", "Sulco do corpo caloso e giro do cíngulo",
  "Acima do corpo caloso, o sulco do corpo caloso; paralelo a ele, o sulco do cíngulo; entre os dois, o giro do cíngulo."),
 (T2, "38-41", "Lóbulo paracentral",
  "O sulco paracentral e o sulco marginal (ramo do sulco do cíngulo) delimitam o lóbulo paracentral. À frente do sulco paracentral, a face medial é a continuação do giro frontal superior."),
 (T2, "41-43", "Sulcos parietoccipital e calcarino; pré-cúneo e cúneo",
  "O sulco parietoccipital separa o lobo parietal do occipital; o sulco calcarino encontra-se com ele. Entre o sulco marginal e o parietoccipital fica o pré-cúneo; entre o parietoccipital e o calcarino, o cúneo (lobo occipital). Junto ao sulco calcarino está a principal área visual."),
 (T2, "47-48", "Face medial do telencéfalo: do corpo caloso para cima",
  "Na vista medial, a face medial do telencéfalo vai do corpo caloso para cima; do corpo caloso para baixo é diencéfalo."),
 (T2, "43-47", "Face inferior: giros occipitotemporal medial, para-hipocampal, úncus e occipitotemporal lateral",
  "Retirados cerebelo e tronco, um grande giro tem três nomes: giro occipitotemporal medial (posterior), giro para-hipocampal e, na ponta anterior, o úncus; o sulco do hipocampo o acompanha. Abaixo dele, o giro occipitotemporal lateral. Úncus e para-hipocampal ligam-se ao sistema límbico."),
 (T2, "51-53", "Como achar o sulco central na peça",
  "Procurar os dois únicos giros transversais e paralelos: são o pré-central e o pós-central; entre eles está o sulco central."),
 # ---------------- NÚCLEOS DA BASE (apostila-guia; sem vídeo) ----------------
 (AP, "AP", "Núcleos da base no centro branco medular",
  "O hemisfério tem córtex (substância cinzenta) por fora e, por dentro, o centro branco medular (substância branca). No centro branco há massas de substância cinzenta: os núcleos da base."),
 (AP, "AP", "Corte horizontal: de fora para dentro",
  "Córtex da ínsula, cápsula extrema, claustro, cápsula externa, putâmen, globo pálido, cápsula interna e, medialmente, núcleo caudado (acima) e tálamo (abaixo)."),
 (AP, "AP", "Núcleo lentiforme e corpo estriado",
  "Putâmen + globo pálido = núcleo lentiforme. Núcleo lentiforme + núcleo caudado = corpo estriado. Veteranos acrescentam núcleo accumbens e corpo amigdaloide à lista."),
 (AP, "AP", "As três cápsulas",
  "Cápsula extrema: entre córtex da ínsula e claustro. Cápsula externa: entre claustro e putâmen. Cápsula interna: entre o núcleo lentiforme e, medialmente, tálamo e núcleo caudado."),
 # ---------------- IRRIGAÇÃO (T3, Prof. Alfredo Jacomo, imagens) ----------------
 (T3, "00-02", "Artéria vertebral: trajeto",
  "Primeiro ramo ascendente da subclávia; sobe pelos forames transversos das vértebras cervicais, entra no crânio pelo forame magno, perfura dura-máter e aracnoide e chega à face anterior do bulbo."),
 (T3, "02-03", "Cerebelares inferiores posterior e anterior",
  "A vertebral dá a artéria cerebelar inferior posterior (parte inferior e posterior do cerebelo); depois sai a cerebelar inferior anterior (parte inferior e anterior)."),
 (T3, "03-04", "Artéria basilar e artéria do labirinto",
  "No sulco bulbopontino as duas vertebrais se unem e formam a artéria basilar, que percorre o sulco basilar da ponte. Logo depois sai a artéria do labirinto, que entra no meato acústico interno com os nervos facial e vestibulococlear para a orelha interna."),
 (T3, "04-05", "Ramos pontinos e artéria cerebelar superior",
  "A basilar dá ramos pontinos e, na parte mais anterior, a artéria cerebelar superior (cerebelo e mesencéfalo); depois se bifurca nas duas artérias cerebrais posteriores."),
 (T3, "05-07", "Artéria cerebral posterior: território",
  "Irriga a face inferior do hemisfério (giro occipitotemporal medial, giro para-hipocampal, úncus) e o lobo occipital até o sulco parietoccipital."),
 (T3, "07-08", "Carótida comum e carótida interna",
  "A carótida comum bifurca-se perto do hioide: a externa irriga face e tireoide; a interna não dá ramos no pescoço, entra no crânio pelo canal carotídeo e faz o sifão carotídeo."),
 (T3, "08-09", "Artéria oftálmica",
  "Antes de perfurar a dura-máter, a carótida interna dá a artéria oftálmica: bulbo ocular, glândula lacrimal e, ao sair da órbita, a fronte."),
 (T3, "09-10", "Três ramos da carótida interna",
  "Depois da dura-máter, a carótida interna dá a artéria cerebral média (para lateral), a cerebral anterior (para anterior) e a comunicante posterior (para posterior, anastomosa-se com a cerebral posterior)."),
 (T3, "10-12", "Artéria cerebral média: território",
  "Entra no sulco lateral e o percorre de anterior para posterior; irriga quase toda a face lateral do hemisfério (lobos frontal, parietal e temporal), exceto a faixa superior (cerebral anterior) e o occipital (cerebral posterior)."),
 (T3, "12-14", "Artéria cerebral anterior: território",
  "Vai para a fissura longitudinal do cérebro e irriga toda a face medial até o sulco parietoccipital, mais a faixa superior da face superolateral."),
 (T3, "14-15", "Artérias hipofisárias",
  "A carótida interna manda as artérias hipofisárias superior e inferior à hipófise, que é muito irrigada."),
 (T3, "15-16", "Comunicantes anterior e posterior",
  "A comunicante anterior liga as duas cerebrais anteriores, na frente do quiasma óptico; a comunicante posterior liga a carótida interna à cerebral posterior."),
 (T3, "16-18", "Círculo arterial do cérebro (polígono de Willis)",
  "As anastomoses formam o círculo arterial do cérebro, na base do encéfalo, mais conhecido como polígono de Willis, unindo o sistema vertebrobasilar e o carotídeo."),
 # ---------------- PRÁTICA (T4) ----------------
 (T4, "00-17", "Prática: base do encéfalo e tronco (repetição da aula 03)",
  "Na peça: bulbo (fissura mediana anterior, pirâmides, oliva, sulco pré-olivar com o hipoglosso, decussação), sulco bulbopontino (VI, VII, VIII), ponte (sulco basilar, pedúnculo cerebelar médio, trigêmeo, flóculo), pedúnculos cerebrais e fossa interpeduncular (oculomotor), quiasma, tratos ópticos, trato e bulbo olfatórios; IV ventrículo, aqueduto e colículos. Repetição da aula 03."),
 (T4, "17-21", "Prática: diencéfalo e telencéfalo na peça",
  "Glândula pineal acima do mesencéfalo; sulco hipotalâmico entre tálamo e hipotálamo; de anterior para posterior quiasma óptico, infundíbulo e corpo mamilar; septo pelúcido fechando o ventrículo lateral; corpo caloso (rostro, joelho, tronco, esplênio), fórnix, sulco do corpo caloso, giro do cíngulo; giros pré e pós-central com o sulco central, sulco lateral, sulcos parietoccipital e calcarino."),
 (T4, "23-24", "Os três sulcos que separam os lobos",
  "Sulco central separa frontal de parietal; sulco lateral separa temporal de frontal e parietal; na face medial, o sulco parietoccipital separa parietal de occipital."),
]


def main():
    linhas, md = [], ["# Percurso da aula 04 — Diencéfalo, núcleos da base, telencéfalo e irrigação (27/10/2026)",
                      "", "Sem lâminas no Drive; cada unidade abaixo faz papel de lâmina (número = posição). Fonte: transcrição (minutos) ou apostila-guia.", ""]
    bloco = None
    for i, (src, mins, titulo, texto) in enumerate(U, 1):
        if src != bloco:
            md += ["", f"## {src}", ""]
            bloco = src
        linhas.append(f"===== página {i} =====\n{titulo}\n[{src} {('min ' + mins) if mins != 'AP' else ''}]\n{texto}\n")
        md.append(f"{i}. **{titulo}** ({src}{', min ' + mins if mins != 'AP' else ''}) — {texto}")
    (HERE / "fontes" / "slides.txt").write_text("\n".join(linhas), encoding="utf-8")
    (HERE / "percurso-aula.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(len(U), "unidades")


if __name__ == "__main__":
    main()
