# Especificação curada — Inflamação granulomatosa (UC03 P3, Patologia; Amaro Duarte Neto/Luiz Fernando Ferraz da Silva; 72 lâminas em duas apresentações).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-pt47-20261010a"
SHORT = "pt47"
LESSON = "2026-uc03-patologia-47-inflamacao-granulomatosa"
DECK = "NEBLI::UC03::P3::Patologia::Inflamação granulomatosa"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CODEX-03) + inventário e fontes da corrida, 10/10/2026"
MEDIA = {f"pt47-s{n:02}-visual.png": f"img/pt47-s{n:02}-visual.png"
         for n in (10, 14, 20, 21, 23, 24, 26, 27, 31, 33, 35)}
MEDIA["pt47-s13-clean.jpeg"] = "img/pt47-s13-clean.jpeg"
MEDIA["pt47-s16-clean.jpeg"] = "img/pt47-s16-clean.jpeg"
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, busca/ext.txt), tags de seção "
         "FirstAid/Pathoma/Bootcamp de granuloma e tuberculose (busca/tags-secao.txt), 10/10: ")
EXCLUIDOS = [
 (1503252725841, "Liga Langhans/caseificação a TB secundária como se fosse característica específica; formulação enganosa."),
 (1487643789145, "Esconde apenas o algarismo 4 em CD4; recuperação trivial para o alvo MHC II–T helper."),
 (1473638595730, "Chama corpo asteroide de característico; o slide ressalta que é inespecífico."),
 (1503252081815, "Reduz TB secundária a reativação, sem reinfecção que a aula inclui."),
]
FORA_DO_RECORTE = [
 "Risco epidemiológico, testes moleculares detalhados e tratamento de TB não abordados na aula.",
 "Figura experimental de zebrafish é marcada como modelo; não extrapolar sequência celular inteira a toda TB humana.",
 "Repetições das lâminas 38, 40, 44–45 e 47–70 da apresentação II não geram cópias de cards já cobertos.",
]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok="", **kw):
    sem_imagem = kw.pop("sem_imagem", "Mecanismo ou relação textual; a imagem não melhoraria esta recuperação.")
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok,
                sem_imagem=sem_imagem, **kw)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


def vi(key, slide, prompt, answer, flag, bloco, alvo, mirrors, motivo, extra):
    """Pergunta visual em cloze, com recorte da figura da própria aula na frente."""
    text = f'<img src="pt47-s{slide:02}-visual.png"><br>{prompt} {{' + f'{{c1::{answer}}}' + '}'
    return au(key, text, {1: flag}, bloco, alvo, slide, "central" if flag == V else "prova" if flag == Z else "lateral",
              "recorte da figura docente testado após busca nos acervos", mirrors, motivo,
              extra=extra, sem_imagem="")


A_ = "A-fundamento"
B_ = "B-macrofagos"
C_ = "C-tb-imunidade"
D_ = "D-morfologia"
E_ = "E-apresentacoes"
F_ = "F-outras-etiologias"
G_ = "G-dinamica"
CARDS = [
 # ---------- Definição e causas (slides 2–3) ----------
 ak("definicao", 1487642936903, {1: V, 2: V}, A_, "definição celular e reconhecimento do granuloma", 2, "Verde: arquitetura transferível entre etiologias."),
 au("persistencia", "Persistent material that resists clearance can trigger {{c1::granuloma formation}}", {1: V}, A_, "persistência leva à contenção organizada", 2, "central", "AnKing define a estrutura, mas não cobra por que ela se forma.", [1487642936903,1487643792482], "Verde: mecanismo que organiza a aula.", extra="- Granulomas localize a stimulus that macrophages cannot readily eliminate.", duplicacao_ok="Ganho: causa da formação; definição AnKing cobra composição celular."),
 au("conter-nao-esterilizar", "A healed tuberculous granuloma may still harbor {{c1::viable bacilli}}", {1: V}, A_, "contenção não é esterilização", 2, "central", "AnKing de Ghon/Ranke não recupera a diferença entre conter e erradicar.", [1503253387295,1503251647055], "Verde: explica latência e reativação.", extra="- Fibrosis shows healing, but does not itself prove sterilization."),
 au("tb-prototipo", "{{c1::Tuberculosis}} is the prototype of infectious granulomatous inflammation", {1: Z}, A_, "TB como protótipo infeccioso", 3, "prova", "Candidatos AnKing abordam TB, sem cobrar a comparação etiológica introdutória.", [1487642936903,1503252659967], "Azul: enquadra as doenças da aula.", extra="- Fungi and leprosy are other infectious granulomatous causes.", duplicacao_ok="Ganho: classifica TB como protótipo etiológico; card de sílica cobra suscetibilidade a TB."),
 au("fungos", "Fungal causes of granulomatous inflammation include {{c1::Paracoccidioides}} and {{c2::Histoplasma}}", {1: Z, 2: Z}, A_, "Paracoccidioides e Histoplasma formam granulomas", 3, "prova", "AnKing não recupera o par fúngico da aula; prova 2024 cobra Paracoccidioides.", [1487469962274,1482374233392], "Azul: etiologias ensinadas e uma cobrada na prova.", extra="- Granulomas depend on the host cellular response, not on a single pathogen."),
 au("imune-corpoestranho", "<b>Foreign-body granulomas</b> form around {{c1::indigestible material}}", {1: V}, A_, "distinguir estímulo de corpo estranho do imune", 3, "central", "AnKing 1487643775029 confunde beriliose com corpo estranho; não é fonte fiel.", [1487642936903,1487643778956], "Verde: separa mecanismos de granuloma.", extra="- Immune granulomas instead organize a cell-mediated response to persistent antigen."),
 au("sarcoidose-causa", "<b>Sarcoidosis</b> is a granulomatous disease of {{c1::unknown}} cause", {1: Z}, A_, "sarcoidose de causa não definida", 3, "prova", "AnKing cobra morfologia sarcoidótica, não a causa ainda desconhecida ensinada.", [1473638571391,1473638601304], "Azul: ressalva etiológica da aula.", extra="- Diagnosis also requires excluding alternative granulomatous causes."),
 au("gpa", "{{c1::Granulomatosis with polyangiitis}} is a noninfectious cause of granulomatous inflammation", {1: R}, A_, "GPA como exemplo não infeccioso", 3, "lateral", "Exemplo da lâmina, sem card externo que cobre esta classificação específica.", [1471806603801,1471806107034], "Rosa: exemplo para a prova, pouco ganho longitudinal nesta aula.", extra="- It is a granulomatous vasculitis, rather than an infection."),
 au("tipoiv", "T-cell–mediated immune granulomas involve {{c1::type IV}} hypersensitivity", {1: V}, A_, "reação granulomatosa imune pode ser tipo IV", 3, "central", "AnKing da área cobre Th1/IFN-γ, mas não a classificação ensinada.", [1487643792482,1487643795892], "Verde: ponte entre imunologia e patologia.", extra="- Foreign-body reactions can form without antigen-specific T-cell activation."),
 ak("crohn", 1482374233392, {1: Z}, A_, "Crohn pode apresentar granulomas não caseosos", 3, "Azul: exemplo clínico lateral dado na aula; HY do acervo não o torna núcleo desta aula.", clinica_lateral=True),
 au("hanseniase", "{{c1::Leprosy}} can also produce granulomatous inflammation", {1: Z}, A_, "hanseníase como causa infecciosa", 3, "prova", "Busca de granuloma/hanseníase não revelou candidato que cobra a associação.", [1503250180112,1487642936903], "Azul: etiologia ensinada no panorama da aula.", extra="- The host cellular response affects its histologic pattern."),
 # ---------- Macrófagos e mediadores (slides 4–6) ----------
 ak("monocito", 1479267390511, {1: V}, B_, "monócito sanguíneo origina macrófago recrutado", 4, "Verde: origem de efetores da inflamação crônica."),
 sh(1791147097386, "verde", B_, "macrófago alveolar é defesa residente inicial", 4, "Verde: nota viva da aula Ambiental, associada sem duplicação."),
 ak("epitelioide", 1487643760880, {1: V}, B_, "histiocito epitelioide deriva de macrófago", 4, "Verde: linhagem evita confusão com epitélio."),
 au("ativacao-lisossomos", "Activated macrophages increase in {{c1::size}} and gain more {{c2::lysosomal enzymes}}", {1: Z, 2: Z}, B_, "mudança morfológica e lisossomal do macrófago ativado", 5, "prova", "AnKing cobre identidade e citocinas, mas não as duas mudanças descritas no slide.", [1487643760880,1487642791049], "Azul: duas consequências da ativação ensinadas.", extra="- Activation also increases metabolic and microbicidal activity."),
 au("recrutamento", "Granulomas expand partly through continued {{c1::monocyte recruitment}}", {1: V}, B_, "quimiotaxia aumenta população macrofágica", 6, "central", "AnKing cobre diferenciação de monócito, sem recuperar influxo sustentado.", [1479267390511,1487642936903], "Verde: manutenção dinâmica do granuloma.", extra="- Recruited monocytes differentiate into tissue macrophages."),
 au("mcp1", "Which chemokine recruits monocytes to a granulomatous focus?<br><br>{{c1::MCP-1 (CCL2)}}", {1: Z}, B_, "MCP-1 recruta monócitos", 6, "prova", "MCP-1 do slide ausente nos candidatos AnKing/externos.", [1489970247629,1487642795725], "Azul: mediador nomeado pelo professor.", extra="- MCP-1 is a monocyte chemoattractant."),
 au("c5a", "{{c1::C5a}} can help recruit inflammatory cells to a granulomatous focus", {1: R}, B_, "C5a como quimiotático", 6, "lateral", "Não há card do acervo que recupere C5a neste contexto da aula.", [1487642795725,1489970247629], "Rosa: detalhe da lista docente.", extra="- The enduring principle is recruitment; C5a is one of several signals."),
 au("proliferacao", "Macrophages accumulate by recruitment and {{c1::local proliferation}} within granulomas", {1: Z}, B_, "proliferação local aumenta macrófagos", 6, "prova", "AnKing diferencia monócitos, sem testar expansão local ensinada.", [1479267390511,1487642936903], "Azul: parte da sequência de mecanismos da aula.", extra="- Proliferation supplements continued influx of monocytes."),
 au("mif", "{{c1::MIF}} is a cytokine that can limit macrophage migration from an inflammatory focus", {1: Z}, B_, "MIF como mediador de retenção", 6, "prova", "Prova P2 2023 q3.5 nomeia o fator; candidatos externos não recuperam o termo.", [1489970247629,1487642936903], "Azul: nome cobrado; não atribuir a MIF sozinho toda a retenção.", extra="- Recruitment, proliferation and multiple local signals also shape macrophage accumulation."),
 au("proteases", "Macrophage {{c1::proteases}} can degrade the matrix around a granuloma", {1: Z}, B_, "proteases degradam matriz e causam lesão", 6, "prova", "AnKing cavitação relaciona proteases, mas não cobra função de degradação da matriz neste ponto.", [1524260701776,1489970247629], "Azul: liga efetor a dano tecidual.", extra="- Elastases and collagenases can injure surrounding tissue."),
 au("ros", "Macrophage {{c1::reactive oxygen species}} can damage host tissue while killing microbes", {1: Z}, B_, "ROS/RNS geram controle e dano colateral", 6, "prova", "AnKing de cavitação menciona ROS, mas não recupera o duplo efeito.", [1524260701776,1489970364081], "Azul: conecta defesa a necrose.", extra="- Reactive nitrogen species contribute to antimicrobial activity too."),
 au("complemento", "Activated macrophages can amplify inflammation by releasing {{c1::complement and coagulation}} mediators", {1: R}, B_, "mediadores de complemento/coagulação amplificam resposta", 6, "lateral", "Lista docente sem candidato externo que recupere este par.", [1489970247629,1487642816623], "Rosa: detalhe de menor transferência.", extra="- This supplements cytokine-mediated recruitment."),
 au("m2", "<b>IL-4 and IL-13</b> favor a {{c1::reparative}} macrophage program", {1: Z}, B_, "IL-4/IL-13 favorecem reparo", 6, "prova", "AnKing M2 cobre Th2/anti-inflamatório, não os dois mediadores da lâmina.", [1520717070355,1520716108281], "Azul: contrasta resposta microbicida e reparativa.", extra="- Reparative macrophages support tissue remodeling and fibrosis."),
 au("tgfb", "{{c1::TGF-β}} promotes collagen deposition during granuloma repair", {1: Z}, B_, "TGF-β favorece fibrose", 6, "prova", "AnKing pesquisado não recupera TGF-β→colágeno no granuloma.", [1487981560574,1520717070355], "Azul: mediador de reparo cobrável.", extra="- Fibrosis can wall off injury but does not prove microbial sterilization."),
 au("pdgf", "{{c1::PDGF}} supports fibroblast proliferation during granuloma repair", {1: Z}, B_, "PDGF promove fibroblastos", 6, "prova", "AnKing 1487981560574 cobra o nome/secreção, não proliferação fibroblástica da aula.", [1487981560574,1520717070355], "Azul: detalhe reparativo ensinado.", extra="- Fibroblasts later deposit collagen in the lesion."),
 # ---------- Entrada do bacilo e resposta celular (slides 7–9) ----------
 au("inalacao", "Pulmonary tuberculosis begins when inhaled bacilli reach the {{c1::alveoli}}", {1: Z}, C_, "entrada alveolar por inalação", 7, "prova", "AnKing 1473548833305 nomeia bacilo, mas deixa a via visível; não cobra o destino alveolar.", [1473548833305,1473289622374], "Azul: etapa introdutória da sequência.", extra="- Alveolar macrophages are the first resident phagocytes encountered."),
 au("manose", "<i>M. tuberculosis</i> can enter macrophages through {{c1::mannose receptors}}", {1: Z}, C_, "receptor de manose na captação", 7, "prova", "Mecanismo explicitado no slide sem card AnKing fiel.", [1503250702223,1503251440902], "Azul: receptor específico de entrada.", extra="- Uptake does not ensure killing because the bacillus can block phagosome maturation."),
 au("cr3", "The complement receptor {{c1::CR3}} can also mediate mycobacterial uptake by macrophages", {1: Z}, C_, "CR3 participa da entrada", 7, "prova", "CR3 da aula ausente nas buscas de TB no AnKing/externos.", [1503250702223,1503251440902], "Azul: rota adicional ensinada.", extra="- Several receptors can participate in phagocytosis."),
 ak("fagolisossomo", 1503251440902, {2: V}, C_, "M. tuberculosis bloqueia fusão fagolisossomal", 7, "Verde: mecanismo central de persistência intracelular."),
 au("intracelular", "Intracellular bacilli are less accessible to circulating {{c1::antibodies}}", {1: Z}, C_, "nicho intracelular limita anticorpos extracelulares", 7, "prova", "AnKing cobre sobrevivência no macrófago, não a consequência para anticorpos.", [1503250702223,1503251440902], "Azul: consequência direta do nicho; não confundir com ausência de imunidade celular.", extra="- T-cell–activated macrophages remain critical for control."),
 ak("replicacao", 1503250702223, {1: V}, C_, "macrófago é nicho de replicação de TB", 7, "Verde: liga falha inicial ao crescimento bacilar.", sem_imagem="Relação funcional entre patógeno e célula, não identificação estrutural."),
 au("linfonodo", "Initial priming of TB-specific CD4<sup>+</sup> T cells occurs in {{c1::draining lymph nodes}}", {1: V}, C_, "priming T no linfonodo drenante", 8, "central", "AnKing vizinho cobre MHC II/CD4, não o local do priming.", [1487643789145,1487116928027], "Verde: distingue foco pulmonar de ativação T inicial.", extra="- Effector T cells later return to the infected lung."),
 sh(1791625427059, "azul", C_, "MHC II apresenta antígeno a CD4", 8, "Azul: identidade NEBLI viva, sem duplicar o piloto autoral."),
 sh(1791625429033, "azul", C_, "IL-2 participa da expansão clonal T", 8, "Azul: identidade NEBLI viva; conferir cloze específico no readback."),
 au("retorno-t", "Primed TB-specific T cells return from lymph nodes to the {{c1::lung}}", {1: Z}, C_, "retorno de efetores T ao foco", 8, "prova", "AnKing cobre priming/efetor, não a transição espacial da aula.", [1487643789145,1487116928027], "Azul: transição da sequência docente.", extra="- Circulating effectors reach the pulmonary focus and activate macrophages."),
 au("il1", "{{c1::IL-1}} contributes to early inflammation during mycobacterial infection", {1: R}, C_, "IL-1 na sinalização inicial", 8, "lateral", "AnKing IL-1 generalista não recupera seu papel nesta sequência; baixo ganho próprio.", [1489970022577,1487640278577], "Rosa: mediador citado, sem promovê-lo a sinal exclusivo de priming.", extra="- Antigen presentation and costimulation are still required for T-cell priming."),
 ak("il12", 1487643792482, {1: V}, C_, "IL-12 polariza Th1", 9, "Verde: citocina que organiza a resposta celular da aula."),
 au("il18", "{{c1::IL-18}} can cooperate with IL-12 to increase IFN-γ production", {1: Z}, C_, "IL-18 coopera na resposta Th1", 9, "prova", "AnKing IL-18 do inflamassoma não cobre a cooperação ensinada.", [1487643792482,1520715849479], "Azul: mediador adicional explícito.", extra="- IL-12 remains the central Th1-polarizing signal here."),
 sh(1791625436658, "verde", C_, "IFN-γ ativa macrófagos e favorece histiócito epitelioide", 9, "Verde: identidade NEBLI viva representa o eixo efetor principal."),
 ak("tnf", 1489970247629, {1: V}, C_, "TNF ajuda manter granuloma", 9, "Verde: mecanismo durável e consequência do bloqueio de TNF."),
 au("cd8", "{{c1::CD8⁺ T cells}} can kill macrophages infected with <i>M. tuberculosis</i>", {1: Z}, C_, "CD8 citotóxicos na infecção", 9, "prova", "Acervo de Th1 menciona ativação CD8, sem recuperar seu efeito sobre macrófago infectado.", [1487116928027,1489970364081], "Azul: braço adicional da aula.", extra="- This can release bacilli and inflammatory material; Th1 remains central to macrophage activation."),
 au("feedback", "Persistent antigen sustains a macrophage–Th1 circuit through IL-12 and {{c1::IFN-γ}}", {1: V}, C_, "circuito de retroalimentação Th1–macrófago", 9, "central", "AnKing isola IL-12 e IFN-γ em cards distintos, sem recuperar o circuito.", [1487643792482,1487643795892], "Verde: integração causal, não mais uma citocina isolada.", extra="- Macrophage antigen presentation and IL-12 support Th1 cells; Th1 IFN-γ activates macrophages."),
 # ---------- Arquitetura e evolução do granuloma (slides 10–19) ----------
 au("palisada", "Epithelioid macrophages can form a {{c1::palisade}} around the center of an immune granuloma", {1: Z}, D_, "arranjo em paliçada", 10, "prova", "AnKing define epitelioide, sem o arranjo da figura.", [1487642936903,1487643760880], "Azul: arquitetura docente.", extra="- A peripheral lymphocyte rim can supply continued cytokine signals."),
 au("rima", "The peripheral T-cell rim supports macrophages mainly through {{c1::cytokine signaling}}", {1: V}, D_, "rima linfocitária mantém ativação", 10, "central", "AnKing Th1 cobra IFN-γ, sem função da rima na estrutura.", [1487643795892,1487642936903], "Verde: componente funcional, cobrado nas provas.", extra="- Th1 IFN-γ is a major activating signal within immune granulomas."),
 au("gigante-fusao", "Multinucleated giant cells in granulomas arise from fusion of {{c1::macrophages}}", {1: V}, D_, "origem das células gigantes", 10, "central", "AnKing histiócito epitelioide não cobra formação de gigante.", [1487643760880,1487642936903], "Verde: linhagem e formação cobradas em exercício/prova.", extra="- A giant cell contains multiple nuclei in shared cytoplasm.", duplicacao_ok="Ganho: fusão que gera célula gigante; card AnKing cobra origem do macrófago a partir do monócito."),
 au("langhans", "Langhans giant cells have nuclei arranged at the {{c1::periphery}} in a horseshoe-like pattern", {1: Z}, D_, "padrão nuclear de Langhans", 10, "prova", "AnKing encontrado liga Langhans indevidamente a TB secundária específica.", [1487642936903,1503252725841], "Azul: reconhecimento morfológico sem atribuir exclusividade à TB.", extra="- Nuclear arrangement identifies a giant-cell pattern, not an etiology."),
 au("gigante-estranho", "Foreign-body giant cells tend to have {{c1::irregularly scattered}} nuclei", {1: Z}, D_, "padrão nuclear de gigante de corpo estranho", 10, "prova", "Acervo não cobre o contraste morfológico fiel.", [1487643775029,1487642936903], "Azul: comparação com Langhans.", extra="- Nuclear position alone does not establish the cause of a granuloma."),
 au("nao-obrigatorio", "Neither caseous necrosis nor giant cells are {{c1::required}} to diagnose a granuloma", {1: V}, D_, "granuloma não exige caseificação ou gigante", 10, "central", "AnKing exemplo de TB pode induzir a tratá-los como critérios obrigatórios.", [1487642936903,1473638571391], "Verde: princípio diagnóstico cobrado em monitoria/prova.", extra="- The defining feature is an organized aggregate of activated macrophages."),
 vi("visual-arquitetura", 10, "The circumscribed aggregate of epithelioid macrophages is a", "granuloma", V, D_, "reconhecer arquitetura granulomatosa na microfotografia", [1487642936903,1487643760880], "Verde: reconhecimento morfológico geral.", "- The rim contains lymphocytes and the center may vary by cause and stage."),
 ak("caseosa", 1487469944925, {1: V}, D_, "necrose caseosa macroscópica", 13, "Verde: padrão morfológico transferível da aula."),
 au("visual-caseosa-fibrose", '<img src="pt47-s13-clean.jpeg"><br>The center shows {{c1::caseous necrosis}} within an outer zone of {{c2::fibrosis}}', {1: V, 2: Z}, D_, "centro caseoso e borda fibrótica na histologia", 13, "central", "AnKing necrose caseosa mostra peça, sem esta leitura da histologia docente.", [1487469944925,1487642936903], "Centro verde e fibrose azul: dois alvos da mesma imagem.", extra="- Black pigment is anthracosis, not the acid-fast bacilli or calcification.", sem_imagem="", duplicacao_ok="ganho: reconhecimento histológico de centro e borda; caseosa cobra padrão macroscópico"),
 au("fases", "Granulomas in one lung can show different degrees of necrosis and {{c1::fibrosis}}", {1: Z}, D_, "lesões coexistem em fases diferentes", 12, "prova", "Acervo de TB lista fases, mas não cobra coexistência no mesmo órgão.", [1503253387295,1487469944925], "Azul: leitura da sequência morfológica dos slides 11–16.", extra="- Each focus reflects a local balance of bacillary growth, immune injury and repair."),
 au("calcificacao-distrofica", "Calcium deposited in necrotic granuloma tissue despite normal serum calcium is {{c1::dystrophic}} calcification", {1: Z}, D_, "calcificação distrófica de necrose", 13, "prova", "AnKing de Ranke nomeia calcificação, sem distinguir o mecanismo distrófico.", [1503255474593,1487469944925], "Azul: relação patológica da imagem e do reparo.", extra="- Dystrophic calcification follows local tissue injury; it does not require hypercalcemia.", duplicacao_ok="Ganho: mecanismo distrófico com cálcio sérico normal; Ranke cobra nome do complexo calcificado."),
 ak("ziehl", 1503250044141, {1: Z, 2: Z}, D_, "Ziehl-Neelsen e bacilos acidorresistentes", 14, "Azul: técnica da lâmina e interpretação do BAAR."),
 vi("visual-baar", 14, "The red slender organisms on this blue background are", "acid-fast bacilli", V, D_, "identificar BAAR na coloração especial", [1503250044141,1503250180112], "Verde: reconhecimento visual do achado central.", "- This stain does not by itself identify the mycobacterial species."),
 au("baar-limite", "A positive acid-fast stain shows acid-fast organisms but does not by itself prove {{c1::M. tuberculosis}}", {1: Z}, D_, "limite da Ziehl-Neelsen", 14, "prova", "AnKing cobre a cor, não a limitação de espécie.", [1503250044141,1503250180112], "Azul: evita diagnóstico específico pelo corante sozinho.", extra="- Staining also cannot establish whether the organisms remain viable."),
 au("reativacao-cicatriz", "Fibrosis in a tuberculous granuloma does not exclude later {{c1::reactivation}}", {1: V}, D_, "fibrose não esteriliza o foco", 16, "central", "Card de Ghon/Ranke não recupera persistência após cicatriz.", [1503253387295,1503251647055], "Verde: explica TB latente e recorrência.", extra="- Viable bacilli can persist in a healed-appearing focus.", duplicacao_ok="ganho: liga cicatriz histológica à reativação; conter-nao-esterilizar cobra presença de bacilos"),
 au("visual-exsudacao", '<img src="pt47-s16-clean.jpeg"><br>The peripheral inflammatory infiltrate around compact fibrosis marks an {{c1::exudative}} focus', {1: Z}, D_, "reconhecer foco exsudativo adjacente à fibrose", 16, "prova", "Acervo não oferece a microfotografia da evolução exibida.", [1503253387295,1487469944925], "Azul: imagem documenta atividade em lesão com cicatriz.", extra="- Fibrosis and ongoing inflammation can coexist; scar does not prove sterilization.", sem_imagem=""),
 au("sem-caseosa", "A granuloma without caseation on one biopsy does {{c1::not}} exclude tuberculosis", {1: Z}, D_, "ausência de caseificação não exclui TB", 17, "prova", "AnKing sarcoidose não permite esta inferência diagnóstica.", [1487643778956,1503252659967], "Azul: limite de uma amostra histológica.", extra="- Interpret morphology with clinical and microbiologic findings."),
 au("fibrose-funcao", "Residual pulmonary fibrosis may impair gas exchange by replacing functional {{c1::parenchyma}}", {1: Z}, D_, "fibrose residual compromete função", 18, "prova", "AnKing de TB foca sequela e imagem, não o mecanismo funcional.", [1473638623505,1503253387295], "Azul: consequência da evolução morfológica.", extra="- A healed lesion can still leave structural damage."),
 au("dna-viabilidade", "Detection of mycobacterial {{c1::DNA}} in tissue does not by itself prove viable bacilli", {1: R}, D_, "DNA não demonstra viabilidade", 19, "lateral", "AnKing diagnóstico de TB não separa presença de DNA e viabilidade.", [1503255940872,1503253427380], "Rosa: ressalva técnica do slide.", extra="- RNA can suggest activity but also needs clinical and laboratory interpretation."),
 au("necrose-dissemina", "Necrosis of infected macrophages can release bacilli and favor {{c1::spread}} of tuberculosis", {1: V}, D_, "necrose facilita dispersão bacilar", 19, "central", "AnKing cobre necrose e bacilo separadamente, sem o elo causal.", [1503250702223,1503253872817], "Verde: ligação dano tecidual → disseminação.", extra="- The same immune response that contains bacilli can damage host tissue."),
 # ---------- Apresentações de TB e granulomas mal organizados (slides 20–25) ----------
 ak("ghon-foco", 1503252549322, {2: V}, E_, "foco pulmonar primário de Ghon", 20, "Verde: HY e localização fundamental da TB primária."),
 vi("visual-primaria", 20, "The small peripheral pale pulmonary focus is compatible with a", "primary Ghon focus", Z, E_, "reconhecer foco pulmonar primário em peça", [1503252549322,1503255474593], "Azul: transfere o conceito à macroscopia; não presume linfonodo pela foto.", "- A Ghon complex also includes the draining hilar node, which is not demonstrated here."),
 au("ghon-complexo", "A Ghon complex includes the primary lung focus and its draining {{c1::hilar lymph nodes}}", {1: V}, E_, "complexo de Ghon une foco e linfonodo", 20, "central", "Candidato AnKing foca só o foco; relação anatômica é central na aula.", [1503252549322,1503255474593], "Verde: padrão de disseminação linfática primária.", extra="- Calcification of this complex is called a Ranke complex."),
 ak("ranke", 1503255474593, {1: V, 2: V}, E_, "complexo de Ranke calcificado", 20, "Verde: HY e evolução do complexo primário."),
 au("secundaria", "Post-primary tuberculosis may follow reactivation of latent bacilli or new {{c1::reinfection}}", {1: V}, E_, "reativação ou reinfecção na TB secundária", 21, "central", "AnKing encontrado reduz TB secundária à reativação.", [1503252081815,1503254160003], "Verde: duas origens possíveis ensinadas.", extra="- Do not equate every post-primary lesion with reactivation."),
 au("cavitacao", "A TB cavity forms when caseous material liquefies and drains into an {{c1::airway}}", {1: V}, E_, "liquefação e drenagem criam cavidade", 21, "central", "AnKing cavitação aborda proteases, sem recuperar drenagem bronquial da aula.", [1524260701776,1487469962274], "Verde: mecanismo e propagação broncogênica.", extra="- Drainage leaves an air-filled space and can carry bacilli through bronchi."),
 au("apice", "Post-primary pulmonary tuberculosis often favors the {{c1::apices}}, where oxygen tension is relatively high", {1: Z}, E_, "predileção apical", 21, "prova", "AnKing localizado não liga sítio à tensão de oxigênio nesta recuperação.", [1503250466324,1503252224928], "Azul: topografia da aula.", extra="- Reactivation and reinfection can both produce post-primary TB."),
 vi("visual-cavidade", 21, "The irregular empty space left after caseous material drains is a TB", "cavity", V, E_, "reconhecer cavitação pulmonar na peça", [1524260701776,1503252081815], "Verde: imagem da consequência do mecanismo.", "- A cavity can communicate with a bronchus and release bacilli."),
 ak("miliar", 1503253872817, {1: V}, E_, "disseminação hematogênica miliar", 23, "Verde: padrão sistêmico fundamental."),
 vi("visual-miliar", 23, "Numerous tiny pale nodules scattered through the lung show a", "miliary pattern", V, E_, "reconhecer padrão miliar macroscópico", [1503253872817,1503253919933], "Verde: reconhecimento da disseminação hematogênica.", "- The distribution reflects widespread seeding, not one solitary primary focus."),
 au("cd4-malformado", "In advanced HIV infection, loss of CD4<sup>+</sup> Th1 support can leave TB granulomas {{c1::poorly organized}}", {1: V}, E_, "ausência de CD4 desorganiza granuloma", 24, "central", "AnKing imunodeficiência não conecta CD4 à morfologia do slide.", [1487643795892,1503254160003], "Verde: mecanismo de granuloma malformado.", extra="- Reduced IFN-γ signaling weakens macrophage activation; high bacillary burden may follow."),
 vi("visual-malformado", 24, "Compared with a compact granuloma, this focus has a", "sparse lymphocyte rim", Z, E_, "reconhecer rima escassa em imunossupressão", [1487642936903,1487643795892], "Azul: observação morfológica, sem diagnosticar AIDS pela imagem.", "- The image alone does not establish the cause of immune dysfunction."),
 # ---------- Outras causas e padrões (slides 26–35) ----------
 ak("sarcoidose-morfologia", 1473638571391, {1: V}, F_, "sarcoidose tem granulomas geralmente não necrosantes", 26, "Verde: padrão morfológico, sem diagnóstico exclusivo."),
 vi("visual-nao-caseoso", 26, "These compact epithelioid granulomas lack central", "caseous necrosis", Z, F_, "reconhecer granulomas não caseosos", [1473638571391,1487643760880], "Azul: forma histológica; não determina etiologia sozinha.", "- Noncaseating morphology alone does not establish sarcoidosis."),
 au("sarcoidose-exclusao", "A noncaseating granuloma alone cannot establish {{c1::sarcoidosis}}", {1: V}, F_, "sarcoidose exige excluir outras causas", 26, "central", "AnKing não explicita limitação diagnóstica do padrão.", [1473638571391,1487643766184], "Verde: evita concluir etiologia pela histologia isolada.", extra="- Infection and other inflammatory conditions can also be noncaseating."),
 ak("schaumann", 1473638601304, {1: R}, F_, "corpo de Schaumann", 28, "Rosa: inclusão morfológica ensinada, inespecífica."),
 au("asteroide", "Asteroid bodies in giant cells are {{c1::nonspecific}} for sarcoidosis", {1: R}, F_, "corpos asteroides inespecíficos", 27, "lateral", "AnKing candidato os chama característicos, o que induz exclusividade incorreta.", [1473638601304,1473638595730], "Rosa: ponto explícito da lâmina, sem diagnóstico pelo achado.", extra="- They are stellate cytoplasmic inclusions in multinucleated giant cells."),
 vi("visual-asteroide", 27, "The stellate inclusion within this giant cell is an", "asteroid body", R, F_, "identificar corpo asteroide", [1473638601304,1473638595730], "Rosa: identificação visual docente, inespecífica.", "- It can occur in conditions besides sarcoidosis."),
 au("cristais", "Foreign material or crystalline oxalate/carbonate may appear inside granuloma {{c1::giant cells}}", {1: R}, F_, "inclusões cristalinas em gigantes", 29, "lateral", "AnKing não recupera inclusão da lâmina.", [1473638601304,1487642936903], "Rosa: imagem histológica de baixo ganho futuro.", extra="- An inclusion alone does not establish etiology."),
 au("hamazaki", "Hamazaki–Wesenberg bodies are ovoid, pigmented inclusions containing {{c1::ceroid}} material", {1: R}, F_, "corpúsculo de Hamazaki-Wesenberg", 30, "lateral", "Acervo não cobre a inclusão específica da lâmina.", [1473638601304,1487642936903], "Rosa: detalhe histológico docente.", extra="- These inclusions are not diagnostic by themselves."),
 au("celulose", "Aspirated plant cellulose can persist because macrophages cannot readily {{c1::digest}} it", {1: Z}, F_, "celulose vegetal como corpo estranho", 31, "prova", "AnKing corpo estranho não recupera o exemplo de aspiração vegetal.", [1487643775029,1487642936903], "Azul: mecanismo aplicado à imagem da aula.", extra="- Persistent fibers can become surrounded by foreign-body giant cells."),
 vi("visual-vegetal", 31, "Giant cells surround translucent retained plant material, a", "foreign-body granuloma", Z, F_, "reconhecer reação de corpo estranho a vegetal", [1487643775029,1487642936903], "Azul: imagem demonstra material exógeno cercado por gigantes.", "- Retained material sustains inflammation without a specific infectious agent."),
 au("corpoestranho-sem-th1", "Foreign-body granulomas can form without antigen-specific {{c1::T-cell}} activation", {1: V}, F_, "corpo estranho não exige Th1", 31, "central", "AnKing encontrado aproxima todo granuloma de resposta Th1.", [1487643775029,1487643795892], "Verde: distingue duas vias patogênicas.", extra="- Macrophages still fuse around material they cannot clear."),
 au("sutura", "A retained nonabsorbable suture can cause a persistent {{c1::foreign-body granuloma}}", {1: Z}, F_, "sutura retida como corpo estranho", 32, "prova", "Acervo conceitual não recupera o exemplo da lâmina.", [1487643775029,1487642936903], "Azul: transfere o mecanismo a material cirúrgico.", extra="- The thread remains a physical stimulus until removed or degraded."),
 ak("silica", 1473638470562, {2: V}, F_, "sílica de jateamento causa pneumoconiose", 33, "Verde: HY e exposição clássica da patologia pulmonar.", sem_imagem="Cobra exposição ocupacional, não reconhecimento morfológico; card visual silicose cobre a imagem."),
 vi("visual-silicose", 33, "The concentric, collagen-rich pulmonary nodule suggests", "silicosis", Z, F_, "reconhecer nódulo silicótico", [1473638470562,1473638477155], "Azul: morfologia do exemplo ocupacional.", "- The image suggests a pattern; exposure history is needed for diagnosis."),
 ak("silica-tb", 1473638477155, {2: V}, F_, "silicose prejudica macrófagos e aumenta risco de TB", 33, "Verde: ligação mecanística de alta utilidade.", sem_imagem="Cobra mecanismo de risco, não padrão visual; imagem de nódulo silicótico é cobrada em outro card."),
 au("sericita", "Inhaled {{c1::sericite}} dust can cause a granulomatous pneumoconiosis", {1: R}, F_, "sericita como poeira causal", 34, "lateral", "AnKing de pneumoconiose não aborda este exemplo docente.", [1473638467997,1473638470562], "Rosa: exemplo específico da lâmina.", extra="- The tissue response reflects persistence of inhaled particles."),
 au("polarizacao", "Under polarized light, birefringent inhaled particles appear {{c1::bright}} against a dark field", {1: Z}, F_, "luz polarizada evidencia partículas", 34, "prova", "Acervo não recupera técnica visual da figura docente.", [1473638467997,1473638470562], "Azul: ajuda reconhecer exposição mineral no tecido.", extra="- Birefringence is a material property, not a diagnosis by itself."),
 au("asbesto-fagocitose", "Long asbestos fibers can cause {{c1::frustrated phagocytosis}} when a macrophage cannot engulf them completely", {1: Z}, F_, "fagocitose incompleta de fibra longa", 35, "prova", "AnKing corpo ferruginoso não recupera o mecanismo físico.", [1473638546856,1473638557173], "Azul: persistência e lesão macrofágica da aula.", extra="- Persisting fibers can promote chronic inflammation and fibrosis."),
 ak("asbesto-corpo", 1473638546856, {1: V}, F_, "corpos ferruginosos/asbesto", 35, "Verde: HY e reconhecimento histológico duradouro."),
 vi("visual-asbesto", 35, "The golden-brown beaded rods are", "ferruginous bodies", Z, F_, "reconhecer corpos ferruginosos", [1473638546856,1473638557173], "Azul: reconhecimento na figura docente, com AnKing conceitual verde.", "- An iron-rich protein coat forms around inhaled fibers."),
 # ---------- Segunda apresentação: dinâmica e estratégias bacilares (slides 39–52) ----------
 au("dinamico", "A granuloma is a {{c1::dynamic}} cell network, not an impermeable wall around bacilli", {1: V}, G_, "granuloma muda e permite tráfego celular", 39, "central", "AnKing definição estática não recupera a dinâmica do artigo docente.", [1487642936903,1503250702223], "Verde: tese da segunda parte da aula.", extra="- Macrophages enter and leave while bacterial and host processes continue."),
 au("inato-inicial", "In experimental zebrafish TB models, early macrophage aggregation can precede adaptive {{c1::T-cell}} immunity", {1: Z}, G_, "agregação inicial pode preceder T adaptativo no modelo", 39, "prova", "AnKing Th1 descreve manutenção, não começo experimental.", [1487642936903,1487643792482], "Azul: qualifica estágio e modelo experimental.", extra="- This does not mean that T cells are unnecessary for durable control."),
 au("atraso-adaptativo", "Delayed T-cell priming lets mycobacteria {{c1::expand}} before strong macrophage activation", {1: Z}, G_, "atraso adaptativo favorece expansão inicial", 41, "prova", "AnKing cobre efetor, não o atraso inicial da sequência docente.", [1503250702223,1487643792482], "Azul: explica janela inicial de crescimento.", extra="- Effector T cells later reach the infected tissue and supply IFN-γ."),
 ak("acidos-micolicos", 1503250180112, {1: V}, G_, "ácidos micólicos conferem acidorresistência", 42, "Verde: propriedade estrutural central da micobactéria.", sem_imagem="Cobra composição química da parede; a aparência em Ziehl-Neelsen é recuperada em card visual próprio."),
 au("arabinogalactano", "Mycobacterial arabinogalactan links peptidoglycan to the outer {{c1::mycolic acid}} layer", {1: Z}, G_, "arabinogalactano une camadas do envelope", 42, "prova", "AnKing ácidos micólicos não recupera a ponte estrutural da lâmina.", [1503250180112,1503250807472], "Azul: organização da parede na aula.", extra="- The lipid-rich outer layer contributes to acid-fast staining."),
 au("lam-envelope", "Lipoarabinomannan (LAM) is a component of the mycobacterial {{c1::cell envelope}}", {1: Z}, G_, "LAM integra parede micobacteriana", 42, "prova", "Acervo não tem card fiel para o componente estrutural.", [1503250180112,1503250807472], "Azul: prepara efeito imune da lâmina seguinte.", extra="- LAM can also modulate macrophage responses."),
 ak("fator-corda", 1503250807472, {1: V}, G_, "fator corda e virulência", 43, "Verde: HY e molécula de virulência central da lâmina."),
 au("fator-corda-quimica", "The mycobacterial <b>cord factor</b> is {{c1::<b>trehalose dimycolate</b>}}", {1: Z}, G_, "fator corda é trealose dimicolato", 43, "prova", "AnKing selecionado cobra o nome fator corda, sem recuperar sua composição ensinada.", [1503250807472,1503251300569], "Azul: detalhe químico da lâmina, sem promover ao núcleo longitudinal.", extra="- Trehalose carries two mycolic-acid chains."),
 au("fator-corda-tnf", "The mycobacterial cord factor can stimulate macrophage {{c1::TNF}} release", {1: Z}, G_, "fator corda estimula TNF", 43, "prova", "AnKing fator corda mistura identidade e citocina; este isola consequência da aula.", [1503250807472,1503251300569], "Azul: conecta molécula bacilar a inflamação.", extra="- TNF helps organize granulomas but excess inflammation can injure tissue."),
 au("lam-apresentacao", "Mycobacterial LAM can impair macrophage {{c1::antigen presentation}}", {1: Z}, G_, "LAM prejudica apresentação antigênica", 43, "prova", "Acervo nomeia LAM, sem esta consequência do artigo docente.", [1503250180112,1487643792482], "Azul: mecanismo de evasão.", extra="- Weaker presentation can delay effective T-cell responses."),
 au("catalase", "Mycobacterial catalase helps detoxify {{c1::hydrogen peroxide}} inside phagocytes", {1: Z}, G_, "catalase reduz dano oxidativo", 43, "prova", "AnKing mecanismo fagolisossomal não recupera defesa contra peróxido.", [1503251440902,1503250702223], "Azul: defesa bacilar específica ensinada.", extra="- Peroxide is one reactive product macrophages use to kill microbes."),
 au("amonia", "Mycobacterial ammonia may make a phagosome less {{c1::acidic}}", {1: R}, G_, "amônia pode elevar pH fagossomal", 43, "lateral", "Acervo não cobre detalhe do slide; afirmação qualificada por 'may'.", [1503251440902,1503250702223], "Rosa: mecanismo acessório, sem afirmar causalidade única.", extra="- Reduced acidification impairs lysosomal killing."),
 au("pkng", "Mycobacterial PknG contributes to impaired phagosome {{c1::maturation}}", {1: Z}, G_, "PknG contribui para bloqueio de maturação", 43, "prova", "AnKing fusão fagolisossomal não nomeia PknG.", [1503251440902,1503250702223], "Azul: fator específico do mecanismo docente.", extra="- PknG is one of several effectors; it does not alone explain every V-ATPase change."),
 au("vatpase", "Reduced recruitment of {{c1::V-ATPase}} limits acidification of the mycobacterial phagosome", {1: Z}, G_, "V-ATPase e acidificação", 43, "prova", "AnKing não recupera a bomba de prótons desta figura.", [1503251440902,1503250702223], "Azul: elo molecular do bloqueio lisossomal.", extra="- The pump normally transfers protons into the compartment."),
 sh(1791625430632, "verde", G_, "IFN-γ induz iNOS e NO microbicida", 46, "Verde: card NEBLI vivo representa o efetor sem duplicação."),
 au("ppd", "A positive tuberculin skin test reflects delayed, {{c1::T-cell–mediated}} hypersensitivity", {1: Z}, G_, "PPD e hipersensibilidade tardia", 46, "prova", "Busca de TB e hipersensibilidade no acervo não achou formulação fiel.", [1487643792482,1487642936903], "Azul: aplicação imune da aula.", extra="- A prior cellular response causes local induration after antigen exposure; it does not alone establish active TB."),
 au("il10", "{{c1::IL-10}} can dampen antigen presentation and macrophage activation during TB", {1: Z}, G_, "IL-10 pode reduzir resposta protetora", 52, "prova", "AnKing de TB foca Th1, sem mediador regulador desta figura.", [1487643792482,1489970516941], "Azul: contrapeso à resposta efetora.", extra="- Immune restraint may limit tissue damage but can also weaken bacterial control."),
 sh(1791625430332, "verde", G_, "IFN-γ aumenta MHC II", 52, "Verde: nota viva de Ativação de células T, associada sem duplicação."),
 au("esat6-mmp9", "In experimental zebrafish TB, ESAT-6 induces epithelial {{c1::MMP9}} and recruits new macrophages", {1: Z}, G_, "ESAT-6 induz MMP9 no modelo", 52, "prova", "AnKing não cobre observação experimental do artigo docente.", [1503250702223,1487642936903], "Azul: exemplo delimitado ao modelo, sem extrapolar cronologia humana.", extra="- Recruited macrophages can provide new intracellular niches for bacilli."),
 au("eferocitose", "Engulfment of dead infected macrophages can transfer mycobacteria to {{c1::new macrophages}}", {1: Z}, G_, "restos de macrófagos infectados transferem bacilos", 52, "prova", "Acervo cobre persistência intracelular, não transferência entre células.", [1503250702223,1503253872817], "Azul: granuloma dinâmico no modelo experimental.", extra="- The outcome depends on how the receiving macrophage handles the bacilli."),
 au("saem-macrofagos", "In experimental TB models, infected macrophages can leave a granuloma and seed {{c1::secondary granulomas}}", {1: Z}, G_, "macrófagos infectados podem semear novos focos", 52, "prova", "AnKing miliar cobra via hematogênica, não tráfego celular local experimental.", [1503253872817,1503250702223], "Azul: ressalta dinâmica, qualificada pelo modelo.", extra="- Human lesions need not follow precisely the same experimental sequence."),
 au("treg", "Regulatory T cells may delay effector T-cell accumulation and favor mycobacterial {{c1::persistence}}", {1: Z}, G_, "Treg pode atrasar resposta efetora", 52, "prova", "AnKing Treg genérico não recupera papel proposto na aula de TB.", [1487643792482,1489970516941], "Azul: modulação do controle, sem tornar Treg causa única.", extra="- Persistent bacilli remain despite an organized host response."),
 au("tnf-equilibrio", "Both too little and excessive TNF signaling can undermine TB control by disturbing the balance between containment and {{c1::tissue damage}}", {1: V}, G_, "TNF exige equilíbrio entre contenção e lesão", 52, "central", "AnKing manutenção do granuloma cobra apenas deficiência de TNF.", [1489970247629,1487642936903], "Verde: síntese causal da segunda parte.", extra="- Effective granulomas contain bacilli while limiting destructive necrosis."),
]

# Ajustes editoriais de construção: pergunta quando a resposta é um nome único,
# ênfase seletiva quando o contexto (e não apenas o cloze) orienta a recuperação.
# Não transformar todos os autorais numa mesma fórmula visual.
STYLED_TEXT = {
 "persistencia": "<b>Persistent material</b> that resists macrophage clearance can lead to a {{c1::<b>granuloma</b>}}",
 "mcp1": "Which <b>chemokine</b> recruits monocytes to a granulomatous focus?<br><br>{{c1::<b>MCP-1 (CCL2)</b>}}",
 "linfonodo": "<b>Initial priming</b> of TB-specific CD4<sup>+</sup> T cells occurs in {{c1::<b>draining lymph nodes</b>}}",
 "calcificacao-distrofica": "Calcium deposited in <b>necrotic tissue</b> despite normal serum calcium is {{c1::<b>dystrophic calcification</b>}}",
 "ghon-complexo": "A <b>Ghon complex</b> includes a primary lung focus and its draining {{c1::<b>hilar lymph nodes</b>}}",
 "secundaria": "<b>Post-primary TB</b> can result from reactivation of latent bacilli or {{c1::<b>reinfection</b>}}",
 "cavitacao": "A <b>TB cavity</b> forms when liquefied caseum drains into a(n) {{c1::<b>airway</b>}}",
 "cd4-malformado": "Loss of <b>CD4<sup>+</sup> Th1 support</b> in advanced HIV infection can leave TB granulomas {{c1::<b>poorly organized</b>}}",
 "sarcoidose-exclusao": "A <b>noncaseating granuloma</b> alone cannot establish {{c1::<b>sarcoidosis</b>}}",
 "corpoestranho-sem-th1": "<b>Foreign-body granulomas</b> can form without antigen-specific {{c1::<b>T-cell</b>}} activation",
 "pkng": "Mycobacterial <b>PknG</b> contributes to impaired phagosome {{c1::<b>maturation</b>}}",
 "dinamico": "A <b>granuloma</b> is a {{c1::<b>dynamic</b>}} cell network, not an impermeable wall",
 "manose": "Which <b>macrophage receptor</b> can take up <i>M. tuberculosis</i>?<br><br>{{c1::<b>Mannose receptor</b>}}",
 "cr3": "Which <b>complement receptor</b> can mediate mycobacterial uptake by macrophages?<br><br>{{c1::<b>CR3</b>}}",
 "tgfb": "Which cytokine promotes <b>collagen deposition</b> during granuloma repair?<br><br>{{c1::<b>TGF-β</b>}}",
 "pdgf": "Which growth factor supports <b>fibroblast proliferation</b> in granuloma repair?<br><br>{{c1::<b>PDGF</b>}}",
 "apice": "<b>Post-primary pulmonary TB</b> favors the {{c1::<b>apices</b>}}, where oxygen tension is relatively high",
 "fator-corda-tnf": "Which macrophage cytokine can be stimulated by the mycobacterial <b>cord factor</b>?<br><br>{{c1::<b>TNF</b>}}",
 "il10": "Which cytokine can <b>dampen antigen presentation</b> and macrophage activation during TB?<br><br>{{c1::<b>IL-10</b>}}",
 "ppd": "A positive <b>tuberculin skin test</b> reflects delayed {{c1::<b>T-cell–mediated</b>}} hypersensitivity",
 "mif": "Which cytokine was historically named for <b>inhibiting macrophage migration</b>?<br><br>{{c1::<b>MIF</b>}}",
 "il18": "Which cytokine can cooperate with <b>IL-12</b> to increase IFN-γ production?<br><br>{{c1::<b>IL-18</b>}}",
 "arabinogalactano": "<b>Arabinogalactan</b> links mycobacterial peptidoglycan to the outer {{c1::<b>mycolic acid</b>}} layer",
 "lam-envelope": "<b>Lipoarabinomannan</b> is a component of the mycobacterial {{c1::<b>cell envelope</b>}}",
 "proteases": "Which macrophage enzymes can <b>degrade the extracellular matrix</b> around a granuloma?<br><br>{{c1::<b>Proteases</b>}}",
 "retorno-t": "After priming in draining lymph nodes, TB-specific T cells return to the {{c1::<b>lung</b>}}",
 "polarizacao": "<b>Birefringent particles</b> appear {{c1::<b>bright</b>}} against a dark field under polarized light",
 "necrose-dissemina": "Necrosis of macrophages infected by <i>M. tuberculosis</i> releases {{c1::<b>bacilli</b>}} that can infect new cells",
 "sem-caseosa": "The absence of <b>caseous necrosis</b> on one biopsy does {{c1::<b>not</b>}} exclude tuberculosis",
 "tnf-equilibrio": "Excess <b>TNF</b> can favor {{c1::<b>necrosis</b>}}, while too little impairs granuloma maintenance",
 "fases": "Granulomas in the same lung may differ in their degree of <b>necrosis</b> and {{c1::<b>fibrosis</b>}}",
 "conter-nao-esterilizar": "A <b>fibrotic tuberculous granuloma</b> can still harbor {{c1::<b>viable bacilli</b>}}",
 "asbesto-fagocitose": "<b>Long asbestos fibers</b> can cause {{c1::<b>frustrated phagocytosis</b>}} when macrophages fail to engulf them completely",
}
for card in CARDS:
    if card["key"] in STYLED_TEXT:
        assert card["kind"] == "autoral"
        card["text"] = STYLED_TEXT[card["key"]]

EMPHASIS = {
 "fungos": "Fungal causes", "imune-corpoestranho": "Foreign-body granulomas",
 "sarcoidose-causa": "Sarcoidosis", "gpa": "noninfectious cause",
 "tipoiv": "T-cell–mediated immune granulomas", "hanseniase": "granulomatous inflammation",
 "ativacao-lisossomos": "Activated macrophages", "recrutamento": "Granulomas expand",
 "c5a": "recruit inflammatory cells", "proliferacao": "Macrophages accumulate",
 "ros": "damage host tissue", "complemento": "Activated macrophages",
 "m2": "IL-4 and IL-13", "inalacao": "Pulmonary tuberculosis",
 "intracelular": "Intracellular bacilli", "il1": "early inflammation",
 "cd8": "kill macrophages", "feedback": "macrophage–Th1 circuit",
 "palisada": "Epithelioid macrophages", "rima": "peripheral T-cell rim",
 "gigante-fusao": "Multinucleated giant cells", "langhans": "Langhans giant cells",
 "gigante-estranho": "Foreign-body giant cells", "nao-obrigatorio": "caseous necrosis nor giant cells",
 "baar-limite": "positive acid-fast stain", "reativacao-cicatriz": "Fibrosis",
 "fibrose-funcao": "Residual pulmonary fibrosis", "dna-viabilidade": "mycobacterial",
 "asteroide": "Asteroid bodies", "cristais": "crystalline oxalate/carbonate",
 "hamazaki": "Hamazaki–Wesenberg bodies", "celulose": "plant cellulose",
 "sutura": "nonabsorbable suture", "sericita": "granulomatous pneumoconiosis",
 "inato-inicial": "experimental zebrafish TB models", "atraso-adaptativo": "Delayed T-cell priming",
 "lam-apresentacao": "Mycobacterial LAM", "catalase": "Mycobacterial catalase",
 "amonia": "Mycobacterial ammonia", "vatpase": "acidification",
 "esat6-mmp9": "experimental zebrafish TB", "eferocitose": "dead infected macrophages",
 "saem-macrofagos": "infected macrophages", "treg": "Regulatory T cells",
}
for card in CARDS:
    phrase = EMPHASIS.get(card["key"])
    if phrase:
        assert phrase in card["text"], card["key"]
        card["text"] = card["text"].replace(phrase, f"<b>{phrase}</b>", 1)

# Correções pontuais de cópias AnKing: preservar a imagem e a identidade do card,
# mas não propagar absolutos ou mecanismos que a aula não demonstra.
SOURCE_CORRECTIONS = {
    "crohn": {
        "text": "<b>Crohn disease</b> can show {{c1::<b>noncaseating granulomas</b>}} in intestinal biopsies",
        "extra": '- The finding is possible, not required for diagnosis.<br><img src="1e59c9b08f76cf96afb83a31508f9485.webp" width="800"><img src="61152fc3386f10bb585b60803d386bd3.webp" width="1200">',
    },
    "monocito": {
        "text": "Macrophages recruited to a granuloma can differentiate from circulating {{c1::<b>monocytes</b>}}",
    },
    "ghon-foco": {
        "text": "A {{c2::<u>Ghon focus</u>}} is the subpleural primary pulmonary lesion of tuberculosis",
        "extra": '- Often in the lower part of an upper lobe or upper part of a lower lobe.<br><img src="32e6c383932ef0bd39d5bc6f2732a74a.webp" width="1136"><br><img src="14c677f099bb4d1ae25c1ac5c73b123c.jpg" width="524">',
    },
    "silica-tb": {
        "text": "<b>Silica</b> can injure macrophages and increase susceptibility to {{c2::<b>tuberculosis</b>}}",
    },
    "fator-corda": {
        "extra": '- Cord factor is trehalose dimycolate, a glycolipid in the mycobacterial cell envelope.<br><img src="6d4fc122ab50103f39f28d3ca418d033.webp" width="532">',
    },
    "asbesto-corpo": {
        "text": "In asbestosis, coated asbestos fibers may form {{c1::<b>asbestos bodies</b>}}, a type of ferruginous body",
        "extra": '- The golden-brown iron-rich coat forms around an inhaled fiber.<br><img src="3c1c023cb7c8f558170a0d68b059ee01.webp" width="621">',
    },
}
for card in CARDS:
    card.update(SOURCE_CORRECTIONS.get(card["key"], {}))

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
    "monocito": "- Recruited monocytes mature into tissue macrophages, adding cells to a persistent inflammatory focus.",
    "epitelioide": "- Epithelioid histiocytes are activated macrophages; the name describes appearance, not epithelial lineage.",
    "miliar": "- Blood-borne dissemination seeds many small foci in the lungs and potentially other organs.",
    "sarcoidose-morfologia": "- Noncaseating granulomas are typical but not specific; infectious causes still need exclusion.",
    "silica-tb": "- Silica injury weakens macrophage control of inhaled mycobacteria; a nodule alone does not diagnose tuberculosis.",
}
DUPLICACAO = {
    "visual-arquitetura": "Ganho: identificar o agregado na microfotografia; definição AnKing cobra composição em texto.",
    "visual-baar": "Ganho: reconhecimento visual dos bacilos na coloração; Ziehl textual cobra propriedade acidorresistente.",
    "baar-limite": "Ganho: delimita inferência da coloração, sem afirmar espécie; card de sílica cobra risco de TB.",
    "visual-primaria": "Ganho: reconhecer foco de Ghon na peça; AnKing cobra definição textual.",
    "visual-nao-caseoso": "Ganho: reconhecer ausência de necrose na lâmina; card de caseificação cobra padrão positivo.",
    "arabinogalactano": "Ganho: ligação química peptidoglicano–ácidos micólicos; AnKing cobra propriedade acidorresistente.",
    "eferocitose": "Ganho: entrada de bacilos em novos macrófagos; card AnKing cobra morfologia de histiócito.",
    "saem-macrofagos": "Ganho: saída/disseminação de macrófagos infectados no modelo experimental; definição AnKing cobra estrutura granulomatosa.",
    "tnf-equilibrio": "Ganho: relaciona excesso de TNF à necrose e deficiência à perda de manutenção; card AnKing cobra uma ação isolada do TNF.",
}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
