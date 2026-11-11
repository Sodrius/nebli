"""Textos da aula 04: reserva reaproveitada (TEXT_RES/EXTRA_RES), AnKing traduzidos (AK, de ak_textos.py) e organizadores autorais (AU).
Frente em português; Extra em inglês (MEMORY UC07). Organizadores: um índice (c1) por card, uma linha por item, negrito só no critério."""
import ak_textos

RENOMEAR = {}
KH_TEXTO, KH_TXT = {}, {}
TEXT_RES = {
 1792588687068: "Na face lateral do hemisfério, o ramo {{c1::ascendente}} do sulco lateral entra no lobo frontal",
}
EXTRA_RES = {
 1792588687081: "It crosses the third ventricle; it may be absent in about 30% of people (Machado).",
 1792588687027: "The lateral ventricle lies above the thalamus, which is the professor's upper limit.",
 1792588687028: "The medial limit of the thalamus is the third ventricle.",
 1792588687033: "Below the hypothalamic sulcus, in the walls and floor of the third ventricle.",
 1792345320950: "Its lesion causes hyperthermia; heat loss is parasympathetic.",
 1792345320649: "Its lesion causes poikilothermia; heat conservation is sympathetic.",
 1792261811748: "It is the sulcus of Sylvius; the middle cerebral artery runs inside it.",
 1792588687042: "The temporal lobe matches the temporal bone below the lateral sulcus.",
 1792588687058: "Precentral gyrus in front (motor) and postcentral gyrus behind (somatosensory).",
 1792588687051: "On the left, these three parts form Broca area.",
 1792588687068: "The anterior and ascending rami divide the inferior frontal gyrus into orbital, triangular and opercular parts.",
 1792588687067: "Only the anterior and ascending rami enter the frontal lobe; the posterior ramus is long.",
 1792588687059: "An unnamed sulcus separates it from the angular gyrus.",
 1792588687061: "A lobule is larger than a gyrus and smaller than a lobe.",
 1792588687078: "Parallel to it lies the cingulate sulcus; the cingulate gyrus is between them.",
 1792588687071: "It lies between the marginal and parieto-occipital sulci.",
 1792588687075: "It lies between the parieto-occipital and calcarine sulci.",
 1792588687076: "The primary visual cortex lies on its lips.",
 1792588687080: "Below the corpus callosum the medial view shows diencephalon; above it, telencephalon.",
 1792588687092: "It also gives the posterior communicating and ophthalmic arteries.",
 1792588687093: "The posterior cerebral arteries supply the occipital lobe and the inferior surface.",
 1792588687095: "These include the cerebellar arteries, pontine branches and the labyrinthine artery.",
 1792588687099: "The central sulcus artery supplies the lateral motor and sensory cortex.",
 1792350083811: "It runs in the lateral sulcus from front to back.",
 1792350077635: "Up to the parieto-occipital sulcus.",
 1792350077936: "This is the superior strip of the superolateral surface the professor gives to the ACA.",
 1792348025216: "Face and upper limb areas are there, hence the deficit in MCA stroke.",
}
AK = {n: (t, e) for n, (u, t, e) in ak_textos.AK.items()}

_O = '<div data-nebli-organizacao="true">'
AU = {
 "diencefalo-partes-org": (_O + "<b>Partes do diencéfalo</b>:<br><br>Acima do sulco da parede do III ventrículo: {{c1::tálamo}}<br>Abaixo desse sulco: {{c1::hipotálamo}}<br>Posterior: {{c1::epitálamo}}<br>Lateral ao hipotálamo: {{c1::subtálamo}}</div>",
                           "Some authors add a fifth part, the metathalamus (geniculate bodies); the professor keeps them in the thalamus."),
 "talamo-limites-org": (_O + "<b>Limites do tálamo</b>:<br><br>Superior: {{c1::ventrículo lateral}}<br>Medial: {{c1::terceiro ventrículo}}<br>Lateral: {{c1::cápsula interna}}<br>Inferior e medial: {{c1::hipotálamo}}<br>Inferior e lateral: {{c1::subtálamo}}</div>",
                        "All come from one coronal section seen from behind, the professor's drawing."),
 "talamo-nucleos-org": (_O + "<b>Núcleos do tálamo</b> por função:<br><br>Anteriores e mediais: {{c1::sistema límbico}}<br>Laterais: {{c1::motricidade e sensibilidade}}<br>Posteriores (geniculados): {{c1::visão e audição}}<br>Medianos: {{c1::pouco conhecida}}</div>",
                        "Lateral geniculate (higher, like the eye) is vision; medial geniculate (lower, like the ear) is hearing."),
 "hipotalamo-limites-org": (_O + "<b>Limites do hipotálamo</b>:<br><br>Superior: {{c1::tálamo}}<br>Medial: {{c1::terceiro ventrículo}}<br>Lateral: {{c1::subtálamo}}<br>Inferior anterior: {{c1::quiasma óptico}}<br>Inferior médio: {{c1::túber cinéreo}} e infundíbulo<br>Inferior posterior: {{c1::corpos mamilares}}</div>",
                            "The anterior commissure lies in front and is not part of the inferior limit."),
 "hipotalamo-nucleos-org": (_O + "<b>Núcleos do hipotálamo</b> por região:<br><br>Supraóptica: supraóptico, {{c1::supraquiasmático}} e {{c1::paraventricular}}<br>Tuberal: ventromedial, {{c1::dorsomedial}} e {{c1::arqueado}}<br>Mamilar: {{c1::mamilares}} e posteriores</div>",
                            "Each region is named after the floor structure below it: optic chiasm, tuber cinereum, mammillary bodies."),
 "subtalamo-limites-org": (_O + "<b>Limites do subtálamo</b>:<br><br>Superior: {{c1::tálamo}}<br>Inferior: {{c1::mesencéfalo}}<br>Medial: {{c1::hipotálamo}}<br>Lateral: {{c1::cápsula interna}}</div>",
                           "Its subthalamic nucleus is motor; its lesion causes contralateral hemiballismus."),
 "lobos-limites-org": (_O + "<b>Sulcos que limitam os lobos</b>:<br><br>Frontal e parietal: sulco {{c1::central}}<br>Temporal e os de cima: sulco {{c1::lateral}}<br>Parietal e occipital (face medial): sulco {{c1::parietoccipital}}</div>",
                       "Lobes are named after the skull bones above them; the insula lies deep in the lateral sulcus with no bone."),
 "corpo-caloso-partes-org": (_O + "<b>Partes do corpo caloso</b>, de anterior para posterior:<br><br>1ª: {{c1::rostro}}<br>2ª: {{c1::joelho}}<br>3ª: {{c1::tronco}}<br>4ª: {{c1::esplênio}}</div>",
                             "It is the largest commissure joining the two hemispheres."),
 "face-inferior-org": (_O + "<b>Grande giro da face inferior</b>, de trás para frente:<br><br>Posterior: giro {{c1::occipitotemporal medial}}<br>Medial: giro {{c1::para-hipocampal}}<br>Anterior: {{c1::úncus}}</div>",
                       "Lateral to it lies the lateral occipitotemporal gyrus; uncus and parahippocampal gyrus belong to the limbic system."),
 "corte-horizontal-org": (_O + "<b>Corte horizontal do hemisfério</b>, de lateral para medial:<br><br>Córtex da {{c1::ínsula}}<br>Cápsula {{c1::extrema}}<br>{{c1::Claustro}}<br>Cápsula {{c1::externa}}<br>{{c1::Putâmen}}<br>Globo {{c1::pálido}}<br>Cápsula {{c1::interna}}<br>Núcleo caudado e tálamo</div>",
                          "Putamen + globus pallidus = lentiform nucleus; lentiform + caudate = corpus striatum (lesson)."),
 "estriado-org": (_O + "<b>Conjuntos dos núcleos da base</b> (aula):<br><br>Putâmen + globo pálido: núcleo {{c1::lentiforme}}<br>Lentiforme + caudado: corpo {{c1::estriado}}</div>",
                  "Machado calls caudate + putamen the striatum; the lesson's corpus striatum is lentiform + caudate."),
 "capsula-interna-partes-org": (_O + "<b>Cápsula interna</b>:<br><br>Perna anterior: entre a cabeça do caudado e o {{c1::lentiforme}}<br>Perna posterior: entre o lentiforme e o {{c1::tálamo}}<br>Entre as duas pernas: {{c1::joelho}}</div>",
                                "Corticospinal fibers descend in the posterior limb; a small infarct there gives pure motor hemiparesis."),
 "aci-ramos-org": (_O + "<b>Ramos da carótida interna</b> no crânio:<br><br>Antes de perfurar a dura-máter: artéria {{c1::oftálmica}}<br>Para lateral: artéria cerebral {{c1::média}}<br>Para anterior: artéria cerebral {{c1::anterior}}<br>Para posterior: artéria {{c1::comunicante posterior}}</div>",
                   "The internal carotid gives no branches in the neck; it enters through the carotid canal and makes the siphon."),
 "vertebrobasilar-org": (_O + "<b>Sistema vertebrobasilar</b>:<br><br>Ramo da vertebral: artéria {{c1::cerebelar inferior posterior}}<br>União das vertebrais: artéria {{c1::basilar}}<br>Ramos da basilar: cerebelar inferior anterior, {{c1::do labirinto}}, pontinos, cerebelar superior<br>Ramos terminais: artérias {{c1::cerebrais posteriores}}</div>",
                         "The vertebral arteries join at the pontomedullary sulcus; the basilar lies in the basilar sulcus."),
 "territorios-org": (_O + "<b>Território cortical</b> das artérias cerebrais:<br><br>Face lateral: cerebral {{c1::média}}<br>Face medial até o sulco parietoccipital e faixa superior: cerebral {{c1::anterior}}<br>Face inferior e lobo occipital: cerebral {{c1::posterior}}</div>",
                     "The professor uses the three faces of the hemisphere from the telencephalon lecture."),
 "willis-org": (_O + "<b>Círculo arterial do cérebro</b> (polígono de Willis):<br><br>Liga as duas cerebrais anteriores: comunicante {{c1::anterior}}<br>Liga a carótida interna à cerebral posterior: comunicante {{c1::posterior}}<br>Une os sistemas: carotídeo e {{c1::vertebrobasilar}}</div>",
                "It surrounds the optic chiasm and tuber cinereum at the base of the brain."),
}
AU_FONTE = {
 "diencefalo-partes-org": "T1 diencéfalo min 06–11 (quatro partes, sulco hipotalâmico, subtálamo lateral); apostila Aula 4 cap1; Machado cap6 §1–2.",
 "talamo-limites-org": "T1 diencéfalo min 18–26 (limites do tálamo no corte coronal); veteranos p13; GaKa aula 4.",
 "talamo-nucleos-org": "T1 diencéfalo min 29–34 (anteriores, posteriores, laterais, mediais, medianos); veteranos p14.",
 "hipotalamo-limites-org": "T1 diencéfalo min 35–43 (limites e assoalho do hipotálamo); veteranos p15; Machado cap6 §4.",
 "hipotalamo-nucleos-org": "T1 diencéfalo min 43–50 (regiões supraóptica, tuberal e mamilar e seus núcleos); veteranos p15; GaKa aula 4.",
 "subtalamo-limites-org": "T1 diencéfalo min 54–58 (limites e núcleo subtalâmico); veteranos p16; Machado cap6 §6.",
 "lobos-limites-org": "T2 telencéfalo min 07–11 e T4 prática min 23–24 (três sulcos separam os lobos); Machado cap7 §2.",
 "corpo-caloso-partes-org": "T2 telencéfalo min 33–36 (rostro, joelho, tronco, esplênio); T4 min 20–21; Machado cap7 §3.2.1.",
 "face-inferior-org": "T2 telencéfalo min 43–47 (occipitotemporal medial, para-hipocampal, úncus); apostila Aula 6 cap4; Machado cap7 §3.3.1.",
 "corte-horizontal-org": "Apostila-guia Aula 6 cap5 (corte horizontal de fora para dentro); veteranos p24; Machado cap7 §5.1.3.",
 "estriado-org": "Apostila-guia Aula 6 cap5 (lentiforme e corpo estriado); veteranos p24; GaKa aula 4.",
 "capsula-interna-partes-org": "GaKa aula 4 (perna anterior, joelho, perna posterior); veteranos p24; Machado cap7 §5.2.",
 "aci-ramos-org": "T3 irrigação min 07–10 (carótida interna sem ramos no pescoço, oftálmica, três ramos); Machado cap9 §2.2.2.",
 "vertebrobasilar-org": "T3 irrigação min 00–05 (vertebral, PICA, basilar, AICA, labirinto, pontinos, cerebelar superior, cerebrais posteriores); Machado cap9 §2.2.3.",
 "territorios-org": "T3 irrigação min 05–14 e 18 (territórios pelas faces do hemisfério); Machado cap9 §2.2.5.",
 "willis-org": "T3 irrigação min 15–18 (comunicantes e polígono de Willis); Machado cap9 §2.2.4.",
}

# fio da aula sem card de acervo (falas do professor)
AU.update({
 "diencefalo-escondido": ("O <b>diencéfalo</b> só aparece na vista medial, depois do corte sagital, porque o {{c1::telencéfalo}} cresce e o esconde", "From the side only telencephalon and cerebellum are visible; the diencephalon stays in the midline, seen also on the base (Machado)."),
 "nucleo-x-ganglio": ("Acúmulo de corpos de neurônios dentro do SNC é {{c1::núcleo}}; fora dele, é {{c1::gânglio}}", "The thalamus is almost all gray matter organized in nuclei."),
 "faces-hemisferio": ('<div data-nebli-organizacao="true"><b>Faces do hemisfério cerebral</b>:<br><br>Vista de lado: face {{c1::superolateral}}<br>Vista após o corte sagital: face {{c1::medial}}<br>Vista após tirar tronco e cerebelo: face {{c1::inferior}}</div>', "The professor studies the telencephalon face by face."),
 "giro-x-sulco": ("No telencéfalo, as saliências são os {{c1::giros}} e as depressões entre elas são os {{c1::sulcos}}", "About two thirds of the cortex is hidden inside the sulci (Machado)."),
 "sulco-central-unico": ("O único sulco que vai da margem superior do hemisfério até o sulco lateral é o sulco {{c1::central}}", "It separates the precentral (motor) and postcentral (somatosensory) gyri."),
 "achar-sulco-central": ("Na peça, o sulco central fica entre os dois únicos giros transversais e {{c1::paralelos}}", "They are the precentral and postcentral gyri; the other gyri run irregularly."),
})
AU_FONTE.update({
 "diencefalo-escondido": "T1 diencéfalo min 03–05 (o telencéfalo esconde o diencéfalo; vista medial); Machado cap6 §1.",
 "nucleo-x-ganglio": "T1 diencéfalo min 26–27 (gânglio fora do SNC, núcleo dentro; tálamo cinzento).",
 "faces-hemisferio": "T2 telencéfalo min 02–05 (faces superolateral, medial e inferior); apostila Aula 6 cap1.",
 "giro-x-sulco": "T2 telencéfalo min 06–07 (giros e sulcos); Machado cap7 §2.",
 "sulco-central-unico": "T2 telencéfalo min 11–12 (o central é o único que vai de ponta a ponta); T4 min 22.",
 "achar-sulco-central": "T2 telencéfalo min 51–53 e T4 min 21–22 (dois giros transversais e paralelos).",
})

# fonte da aula nomeada primeiro (gate: livro sozinho não origina autoral)
AU_FONTE = {k: ("Transcrição " + v if v.startswith(("T1", "T2", "T3", "T4")) else ("Apostila-guia (veteranos) " + v[len("Apostila-guia "):] if v.startswith("Apostila-guia") else ("GaKa (veteranos) " + v[5:] if v.startswith("GaKa") else v))) for k, v in AU_FONTE.items()}

# 09/11 — lint: critério de cada linha em negrito curto, organizador ≤ 26 palavras, clozes com negrito de contexto e sem ';'
_O = '<div data-nebli-organizacao="true">'
_N = {
 "diencefalo-partes-org": "<b>Diencéfalo</b>, partes:<br><br><b>Acima</b> do sulco da parede do III ventrículo: {{c1::tálamo}}<br><b>Abaixo</b> desse sulco: {{c1::hipotálamo}}<br><b>Atrás</b>: {{c1::epitálamo}}<br><b>Ao lado</b> do hipotálamo: {{c1::subtálamo}}",
 "talamo-limites-org": "<b>Tálamo</b>, limites:<br><br><b>Superior</b>: {{c1::ventrículo lateral}}<br><b>Medial</b>: {{c1::terceiro ventrículo}}<br><b>Lateral</b>: {{c1::cápsula interna}}<br><b>Inferomedial</b>: {{c1::hipotálamo}}<br><b>Inferolateral</b>: {{c1::subtálamo}}",
 "talamo-nucleos-org": "<b>Núcleos do tálamo</b>, função:<br><br><b>Anteriores</b> e mediais: {{c1::sistema límbico}}<br><b>Laterais</b>: {{c1::motricidade}} e sensibilidade<br><b>Posteriores</b>: {{c1::visão}} e audição<br><b>Medianos</b>: {{c1::pouco conhecida}}",
 "hipotalamo-limites-org": "<b>Hipotálamo</b>, limites:<br><br><b>Superior</b>: {{c1::tálamo}}<br><b>Medial</b>: {{c1::terceiro ventrículo}}<br><b>Lateral</b>: {{c1::subtálamo}}<br><b>Inferior anterior</b>: {{c1::quiasma óptico}}<br><b>Inferior médio</b>: {{c1::túber cinéreo}}<br><b>Inferior posterior</b>: {{c1::corpos mamilares}}",
 "hipotalamo-nucleos-org": "<b>Hipotálamo</b>, núcleos por região:<br><br><b>Supraóptica</b>: supraóptico, {{c1::supraquiasmático}}, {{c1::paraventricular}}<br><b>Tuberal</b>: ventromedial, {{c1::dorsomedial}}, {{c1::arqueado}}<br><b>Mamilar</b>: {{c1::mamilares}} e posteriores",
 "subtalamo-limites-org": "<b>Subtálamo</b>, limites:<br><br><b>Superior</b>: {{c1::tálamo}}<br><b>Inferior</b>: {{c1::mesencéfalo}}<br><b>Medial</b>: {{c1::hipotálamo}}<br><b>Lateral</b>: {{c1::cápsula interna}}",
 "faces-hemisferio": "<b>Hemisfério cerebral</b>, faces:<br><br><b>De lado</b>: {{c1::superolateral}}<br><b>Após o corte</b> sagital: {{c1::medial}}<br><b>Sem tronco</b> e cerebelo: {{c1::inferior}}",
 "lobos-limites-org": "<b>Lobos</b>, sulcos que os separam:<br><br><b>Frontal e parietal</b>: {{c1::central}}<br><b>Temporal</b> dos de cima: {{c1::lateral}}<br><b>Parietal e occipital</b>: {{c1::parietoccipital}}",
 "corpo-caloso-partes-org": "<b>Corpo caloso</b>, de anterior para posterior:<br><br><b>1ª</b>: {{c1::rostro}}<br><b>2ª</b>: {{c1::joelho}}<br><b>3ª</b>: {{c1::tronco}}<br><b>4ª</b>: {{c1::esplênio}}",
 "face-inferior-org": "<b>Face inferior</b>, o grande giro:<br><br><b>Posterior</b>: occipitotemporal {{c1::medial}}<br><b>Meio</b>: {{c1::para-hipocampal}}<br><b>Ponta anterior</b>: {{c1::úncus}}",
 "corte-horizontal-org": "<b>Corte horizontal</b>, de lateral para medial:<br><br><b>1</b>: córtex da {{c1::ínsula}}<br><b>2</b>: cápsula {{c1::extrema}}<br><b>3</b>: {{c1::claustro}}<br><b>4</b>: cápsula {{c1::externa}}<br><b>5</b>: {{c1::putâmen}}<br><b>6</b>: globo {{c1::pálido}}<br><b>7</b>: cápsula {{c1::interna}}",
 "estriado-org": "<b>Núcleos da base</b>, conjuntos:<br><br><b>Putâmen + globo pálido</b>: núcleo {{c1::lentiforme}}<br><b>Lentiforme + caudado</b>: corpo {{c1::estriado}}",
 "capsula-interna-partes-org": "<b>Cápsula interna</b>, partes:<br><br><b>Perna anterior</b>: entre caudado e {{c1::lentiforme}}<br><b>Perna posterior</b>: entre lentiforme e {{c1::tálamo}}<br><b>Entre as pernas</b>: {{c1::joelho}}",
 "aci-ramos-org": "<b>Carótida interna</b>, ramos no crânio:<br><br><b>Antes da dura</b>: {{c1::oftálmica}}<br><b>Lateral</b>: cerebral {{c1::média}}<br><b>Anterior</b>: cerebral {{c1::anterior}}<br><b>Posterior</b>: {{c1::comunicante posterior}}",
 "vertebrobasilar-org": "<b>Sistema vertebrobasilar</b>:<br><br><b>Ramo da vertebral</b>: cerebelar inferior {{c1::posterior}}<br><b>União das vertebrais</b>: artéria {{c1::basilar}}<br><b>Ramos terminais</b>: cerebrais {{c1::posteriores}}",
 "territorios-org": "<b>Território cortical</b>:<br><br><b>Face lateral</b>: cerebral {{c1::média}}<br><b>Face medial</b> e faixa superior: cerebral {{c1::anterior}}<br><b>Face inferior</b> e occipital: cerebral {{c1::posterior}}",
 "willis-org": "<b>Polígono de Willis</b>:<br><br><b>Entre as cerebrais anteriores</b>: comunicante {{c1::anterior}}<br><b>Carótida → cerebral posterior</b>: comunicante {{c1::posterior}}",
}
for _k, _t in _N.items():
    AU[_k] = (_O + _t + "</div>", AU[_k][1])
AU["estriado-org"] = (AU["estriado-org"][0], "Machado calls caudate + putamen the striatum; here corpus striatum means lentiform + caudate.")
AU["vertebrobasilar-org"] = (AU["vertebrobasilar-org"][0], "The basilar also gives the anterior inferior cerebellar, labyrinthine, pontine and superior cerebellar arteries.")
AU["diencefalo-escondido"] = ("No cérebro, o <b>diencéfalo</b> só aparece na vista medial porque o {{c1::telencéfalo}} cresce e o esconde", AU["diencefalo-escondido"][1])
AU["nucleo-x-ganglio"] = ("Acúmulo de corpos de neurônios dentro do <b>SNC</b> é {{c1::núcleo}} e, fora dele, {{c1::gânglio}}", AU["nucleo-x-ganglio"][1])
AU["giro-x-sulco"] = ("No <b>telencéfalo</b>, as saliências são os {{c1::giros}} e as depressões entre elas, os {{c1::sulcos}}", AU["giro-x-sulco"][1])
AU["sulco-central-unico"] = ("O único sulco que vai da <b>margem superior</b> até o <b>sulco lateral</b> é o {{c1::central}}", AU["sulco-central-unico"][1])
AU["achar-sulco-central"] = ("Na <b>peça</b>, o sulco central fica entre os dois únicos giros transversais e {{c1::paralelos}}", AU["achar-sulco-central"][1])
AU["sulco-central-unico"] = ("Entre os sulcos do hemisfério, só o {{c1::central}} vai da <b>margem superior</b> até o <b>sulco lateral</b>", AU["sulco-central-unico"][1])

AU["diencefalo-partes-org"] = ('<div data-nebli-organizacao="true"><b>Diencéfalo</b>, partes:<br><br><b>Acima</b> do sulco da parede do III ventrículo: {{c1::tálamo}}<br><b>Abaixo</b> desse sulco: {{c1::hipotálamo}}<br><b>Atrás</b>: {{c1::epitálamo}}<br><b>Lateral</b>, invisível na vista medial: {{c1::subtálamo}}</div>', AU["diencefalo-partes-org"][1])
AU["hipotalamo-limites-org"] = (AU["hipotalamo-limites-org"][0].replace("<b>Inferior anterior</b>", "Inferior <b>anterior</b>").replace("<b>Inferior médio</b>", "Inferior <b>médio</b>").replace("<b>Inferior posterior</b>", "Inferior <b>posterior</b>"), AU["hipotalamo-limites-org"][1])
AU["faces-hemisferio"] = (AU["faces-hemisferio"][0].replace("<b>Após o corte</b> sagital", "Após o <b>corte</b> sagital").replace("<b>Sem tronco</b> e cerebelo", "Sem <b>tronco</b> e cerebelo").replace("<b>De lado</b>", "De <b>lado</b>"), AU["faces-hemisferio"][1])

# 09/11 — verificador por casos (1ª rodada)
_O = '<div data-nebli-organizacao="true">'
AU["diencefalo-escondido"] = ("Na vista <b>lateral</b> do encéfalo o diencéfalo não aparece porque o {{c1::telencéfalo}} o recobre", AU["diencefalo-escondido"][1])
AU["talamo-nucleos-org"] = (_O + "<b>Núcleos do tálamo</b>, função:<br><br><b>Anteriores</b> e mediais: {{c1::sistema límbico}}<br><b>Laterais</b>: {{c1::motricidade}} e sensibilidade<br><b>Posteriores</b>: {{c1::visão}} e audição<br><b>Medianos</b>: função pouco conhecida</div>", AU["talamo-nucleos-org"][1])
AU["achar-sulco-central"] = ("Na <b>peça</b>, o sulco central fica entre os únicos dois giros transversais e paralelos, o {{c1::pré-central}} e o {{c1::pós-central}}", AU["achar-sulco-central"][1])
AU["estriado-org"] = ("O núcleo lentiforme somado ao núcleo <b>caudado</b> forma o corpo {{c1::estriado}}", AU["estriado-org"][1])
AU["capsula-interna-partes-org"] = (_O + "<b>Cápsula interna</b>, partes:<br><br><b>Perna anterior</b>: entre caudado e {{c1::lentiforme}}<br><b>Perna posterior</b>: entre {{c1::lentiforme}} e {{c1::tálamo}}<br><b>Entre as pernas</b>: {{c1::joelho}}</div>", AU["capsula-interna-partes-org"][1])
AU["aci-ramos-org"] = (_O + "<b>Carótida interna</b>, ramos no crânio:<br><br><b>Ao atravessar</b> a dura-máter: {{c1::oftálmica}}<br><b>Para o sulco</b> lateral: cerebral {{c1::média}}<br><b>Para a fissura</b> longitudinal: cerebral {{c1::anterior}}<br><b>Para trás</b>, até a cerebral posterior: {{c1::comunicante posterior}}</div>", AU["aci-ramos-org"][1])
AU["willis-org"] = (_O + "<b>Polígono de Willis</b>:<br><br><b>Une</b> os dois sistemas carotídeos: comunicante {{c1::anterior}}<br><b>Une</b> carótida e vertebrobasilar: comunicante {{c1::posterior}}</div>", AU["willis-org"][1])
AU["hipotalamo-limites-org"] = (_O + "<b>Hipotálamo</b>, limites:<br><br>Limite <b>superior</b>: {{c1::tálamo}}<br>Limite <b>medial</b>: {{c1::terceiro ventrículo}}<br>Limite <b>lateral</b>: {{c1::subtálamo}}<br>Limite inferior, parte <b>anterior</b>: {{c1::quiasma óptico}}<br>Limite inferior, parte <b>média</b>: {{c1::túber cinéreo}}<br>Limite inferior, parte <b>posterior</b>: {{c1::corpos mamilares}}</div>", AU["hipotalamo-limites-org"][1])
AU["estriado-org"] = ("Na aula, núcleo lentiforme somado ao núcleo <b>caudado</b> forma o corpo {{c1::estriado}}", AU["estriado-org"][1])
AU["vertebrobasilar-org"] = (AU["vertebrobasilar-org"][0].replace("<b>Ramo da vertebral</b>", "Ramo da <b>vertebral</b>").replace("<b>União das vertebrais</b>", "<b>União</b> das vertebrais").replace("<b>Ramos terminais</b>", "Ramos <b>terminais</b>"), AU["vertebrobasilar-org"][1])

# 11/11 — correções da auditoria independente, antes de instalar.
TEXT_RES.update({
 1792345320950: 'O <b>hipotálamo anterior</b> coordena respostas de perda de calor, associadas à atividade {{c1::parassimpática}}.',
 1792345320649: 'O <b>hipotálamo posterior</b> coordena respostas de conservação de calor, associadas à atividade {{c1::simpática}}.',
})
EXTRA_RES[1792588687051] = 'The inferior frontal gyrus has orbital, triangular and opercular parts. Classical Broca area occupies the opercular and triangular parts of the dominant hemisphere; the orbital part is not included.'
AU['hipotalamo-limites-org'] = (_O + '<b>Hipotálamo</b>, limites:<br><br><b>Superior</b>: {{c1::tálamo}}<br><b>Medial</b>: {{c1::terceiro ventrículo}}<br><b>Lateral</b>: {{c1::subtálamo}}<br><b>Assoalho, de anterior para posterior</b>: quiasma óptico → {{c1::infundíbulo}} → {{c1::túber cinéreo}} → corpos mamilares</div>', 'The four floor landmarks are the optic chiasm, infundibulum, tuber cinereum and mammillary bodies. The infundibulum projects from the tuber cinereum; the sequence follows the course teaching and past exam.')
AU['territorios-org'] = (_O + '<b>Território cortical</b>:<br><br><b>Maior parte da face lateral</b>: cerebral {{c1::média}}<br><b>Face medial frontal/parietal</b>: cerebral {{c1::anterior}}<br><b>Occipital e temporal inferomedial</b>: cerebral {{c1::posterior}}</div>', 'The inferior surface is not supplied entirely by the PCA: orbitofrontal and anterior temporal regions receive branches of the anterior circulation. Territories have border zones and anatomical variants.')
AU['estriado-org'] = (AU['estriado-org'][0], 'Macroscopic corpus striatum (corpo estriado dorsal in Machado) may group caudate and lentiform nuclei. Functional striatum is caudate plus putamen. Distinguish this terminology from the amygdala and from the lentiform nucleus itself.')

TEXT_RES[1792348022615] = 'Na <b>face medial</b>, o sulco {{c1::parietoccipital}} separa os lobos parietal e occipital.'

# Recuperação térmica no termo essencial; não ensinar que sudorese é parassimpática.
TEXT_RES[1792345320950] = 'O <b>hipotálamo anterior</b> coordena a {{c1::perda de calor}}.'
TEXT_RES[1792345320649] = 'O <b>hipotálamo posterior</b> coordena a {{c1::conservação de calor}}.'
EXTRA_RES[1792345320950] = 'Anterior hypothalamic circuits coordinate heat loss. Sweating uses sympathetic cholinergic fibers, so heat loss must not be equated with a purely parasympathetic response.'
EXTRA_RES[1792345320649] = 'Posterior hypothalamic circuits coordinate heat conservation and production, including cutaneous vasoconstriction and shivering. The hypothalamus coordinates effectors; the direction of control is not reversed.'

# 11/11 — auditoria das frentes compartilhadas.
TEXT_RES[1792588687068] = 'O ramo do <b>sulco lateral</b> entre as partes triangular e opercular é o {{c1::ascendente}}.'
TEXT_RES[1792588687033] = 'O <b>hipotálamo</b> forma as paredes inferolaterais e o {{c1::assoalho}} do terceiro ventrículo.'
TEXT_RES[1792588687028] = 'O <b>tálamo</b> forma a porção superior das paredes laterais do {{c1::terceiro ventrículo}}.'

# 11/11 — conexões explicitamente cobradas nas provas de 2023, reuso do Kenhub textual.
TEXT_RES[1792345652947] = 'O <b>fórnix</b> conduz fibras do {{c1::hipocampo}} aos corpos mamilares.'
EXTRA_RES[1792345652947] = 'Postcommissural fornix fibers reach the mammillary bodies. This connection participates in the hippocampal memory circuit; precommissural fibers have other septal and basal forebrain targets.'
TEXT_RES[1792350073731] = 'As anastomoses do <b>círculo arterial do cérebro</b> permitem circulação {{c1::colateral}}.'
EXTRA_RES[1792350073731] = 'Communicating arteries can redirect flow between arterial systems after a proximal obstruction. Protection depends on vessel caliber, anatomical variants and the site of occlusion; the circle does not guarantee adequate collateral flow in every patient.'
AU['hipotalamo-limites-org'] = (_O + 'Limites do <b>hipotálamo</b>:<br><br>Limite <b>superior</b>: {{c1::tálamo}}<br>Limite <b>medial</b>: {{c1::terceiro ventrículo}}<br>Limite <b>lateral</b>: {{c1::subtálamo}}<br>Assoalho, de <b>anterior para posterior</b>: {{c1::quiasma óptico}} → {{c1::infundíbulo}} → {{c1::túber cinéreo}} → {{c1::corpos mamilares}}</div>', AU['hipotalamo-limites-org'][1])
AK[1481596931776] = ('Na <b>face medial</b>, o sulco acima do giro que contorna o corpo caloso é o sulco do {{c1::cíngulo}}.', AK[1481596931776][1])
AK[1481244840641] = ('A oclusão da <b>artéria cerebral posterior</b> pode causar hemianopsia homônima contralateral com {{c1::preservação macular}}.', AK[1481244840641][1])

# 11/11: cópias AnKing já existentes preservam ID e histórico.
TEXT_RES[1792347682942] = 'A via {{c1::direta}} dos <b>núcleos da base</b> facilita o movimento.'
EXTRA_RES[1792347682942] = 'Striatal inhibition of GPi reduces its tonic inhibition of the thalamus, increasing thalamocortical excitation.'
TEXT_RES[1792347671169] = 'Na <b>via direta</b>, o estriado {{c2::inibe}} o {{c1::globo pálido interno}}.'
EXTRA_RES[1792347671169] = 'GABAergic striatal neurons suppress the tonic inhibitory output from GPi to the motor thalamus.'
TEXT_RES[1792347664967] = 'Na <b>via direta</b>, a {{c1::inibição}} do globo pálido interno desinibe o núcleo {{c2::ventral lateral}} do tálamo.'
EXTRA_RES[1792347664967] = 'Removing pallidal inhibition permits greater thalamic excitation of motor cortex; this is disinhibition, not a direct excitatory striatothalamic connection.'
TEXT_RES[1792347683193] = 'A via {{c1::indireta}} dos <b>núcleos da base</b> reduz o movimento.'
EXTRA_RES[1792347683193] = 'The indirect route ultimately increases GPi inhibition of the motor thalamus. Interrupting this brake can cause hyperkinetic movement.'
TEXT_RES[1792347675467] = 'Na <b>via indireta</b>, o núcleo subtalâmico {{c2::excita}} o {{c1::globo pálido interno}}.'
EXTRA_RES[1792347675467] = 'Glutamatergic subthalamic input increases the inhibitory pallidal output to the motor thalamus.'
TEXT_RES[1792347683444] = 'A <b>dopamina</b> estimula a via {{c1::direta}} por receptores {{c2::D1}}.'
EXTRA_RES[1792347683444] = 'D1 activation facilitates the movement promoting route. Without this drive, the relative inhibitory influence of the indirect route rises.'

# 11/11 — nomenclatura mínima, sempre regerando o rótulo visual junto.
RENOMEAR.update({1792438779776:'Habênula',1792346367591:'Núcleo pré-óptico medial',1792244787869:'Infundíbulo',1792346376214:'Núcleo paraventricular',1792346381716:'Núcleo ventromedial',1792346383240:'Núcleo dorsomedial',1792346802214:'Eminência mediana',1792346789065:'Parte distal',1792346790590:'Parte intermédia',1792346792089:'Parte tuberal',1792346810265:'Rede capilar primária',1792346811715:'Rede capilar secundária'})
TEXT_RES[1792588687061] = 'Os lóbulos parietais superior e inferior são separados pelo sulco {{c1::intraparietal}}.'
TEXT_RES[1792588687095] = 'A artéria do {{c1::labirinto}} irriga a <b>orelha interna</b>.'
EXTRA_RES[1792588687095] = 'It commonly arises from AICA and may arise directly from the basilar artery. It accompanies VII and VIII through the internal acoustic meatus.'
EXTRA_RES[1792696998756] = 'The vertebral arteries arise from the subclavian arteries and unite near the pontomedullary junction. The basilar artery ascends in the basilar sulcus.'
EXTRA_RES[1792588687093] = 'The posterior cerebral arteries supply the occipital cortex and inferomedial temporal cortex. The entire inferior surface is not a single PCA territory.'

TEXT_RES[1793966747232] = '<b>Qual estrutura a seta indica?</b> {{c1::Hipotálamo}}<br><img src="paste-66931b3f01188d01938c84116d67e996e4a64061.jpg" style="width:100%;max-width:850px;height:auto">'

AU['willis-org'] = (AU['willis-org'][0].replace('</div>','<br>Fora do <b>anel arterial</b>: cerebral {{c1::média}}</div>'), 'The ring includes proximal anterior cerebral arteries, the anterior communicating artery, terminal internal carotids, posterior communicating arteries and proximal posterior cerebral arteries. The middle cerebral arteries branch laterally outside the ring.')

TEXT_RES[1793966747232] = '<b>Qual estrutura a seta indica?</b> {{c1::Hipotálamo}}<br><img src="u7an04-hipotalamo-focal.jpg" style="width:100%;max-width:850px;height:auto">'

# 11/11: listas verticais, contexto discriminante e sulco variável citado na fala.
AU['hipotalamo-limites-org'] = (_O + 'Limites do <b>hipotálamo</b>:<br><br>Limite <b>superior</b>: {{c1::tálamo}}<br>Limite <b>medial</b>: {{c1::terceiro ventrículo}}<br>Limite <b>lateral</b>: {{c1::subtálamo}}<br>Assoalho, em ordem <b>anteroposterior</b>:<br>1. {{c1::quiasma óptico}}<br>2. {{c1::infundíbulo}}<br>3. {{c1::túber cinéreo}}<br>4. {{c1::corpos mamilares}}</div>', AU['hipotalamo-limites-org'][1])
AU['territorios-org'] = (_O + 'Território cortical das <b>artérias cerebrais</b>:<br><br>Maior parte da face <b>lateral</b>: cerebral {{c1::média}}<br>Face <b>medial</b> frontal/parietal: cerebral {{c1::anterior}}<br><b>Occipital</b> e temporal inferomedial: cerebral {{c1::posterior}}</div>', AU['territorios-org'][1])
AU['lobos-limites-org'] = (AU['lobos-limites-org'][0].replace('</div>','<br>Sulco occipital lateral <b>variável</b>: {{c1::semilunar}}</div>'), AU['lobos-limites-org'][1] + ' The lunate (semilunar) sulcus is variable in humans; it does not provide a reliable universal boundary for the occipital lobe.')
TEXT_RES[1792588687061] = 'Os <b>lóbulos parietais</b> superior e inferior são separados pelo sulco {{c1::intraparietal}}.'

TEXT_RES[1792348031994] = 'No <b>giro temporal transverso anterior</b> (Heschl), localiza-se o córtex {{c1::auditivo primário}}.'
EXTRA_RES[1792348031994] = 'The anterior transverse temporal gyrus lies on the superior temporal plane, within the lateral sulcus. It houses primary auditory cortex (Brodmann area 41); it is distinct from the insula.'

AU['capsula-interna-partes-org'] = (AU['capsula-interna-partes-org'][0].replace('</div>', '<br>Fórnix e cápsula interna: fibras de {{c1::projeção}}</div>'), AU['capsula-interna-partes-org'][1] + ' The fornix contains hippocampal projection fibers; the commissure of the fornix is a distinct interhemispheric bundle. The corpus callosum and anterior commissure carry commissural fibers. This follows Machado chapter 7, section 5.2, rather than the inaccurate old answer-key explanation.')

AU['aci-ramos-org'] = (AU['aci-ramos-org'][0].replace('</div>', '<br>Segmento <b>cervical</b>: {{c1::sem ramos}}<br>Entrada no <b>crânio</b>: canal {{c1::carotídeo}}<br>Curvatura <b>intracraniana</b>: sifão {{c1::carotídeo}}<br>Oftálmica: bulbo {{c1::ocular}} e anexos</div>'), AU['aci-ramos-org'][1])

TEXT_RES[1792588687043] = 'O <b>lobo occipital</b> fica posterior aos lobos {{c1::parietal}} e temporal.'
TEXT_RES[1792588687044] = 'O sulco {{c1::lateral}} separa o <b>lobo temporal</b> dos lobos frontal e parietal.'
TEXT_RES[1792588687069] = 'Na face <b>superolateral</b>, reconhecem-se os lobos frontal, temporal, parietal e {{c1::occipital}}.'

AU['achar-sulco-central'] = ('Na face <b>superolateral</b>, os giros que ladeiam o sulco central são {{c1::pré-central}} e {{c1::pós-central}}.', 'The precentral and postcentral gyri border the central sulcus. Identify them together rather than assuming that no other cortical gyri can run transversely.')

AU['aci-ramos-org'] = (_O + '<b>Carótida interna</b>: trajeto e ramos:<br><br>Segmento <b>cervical</b>: {{c1::sem ramos}}<br>Entrada no <b>crânio</b>: {{c1::canal carotídeo}}<br>Curvatura <b>intracraniana</b>: {{c1::sifão carotídeo}}<br>Ramo para a <b>órbita</b>: {{c1::oftálmica}}<br>Território desse ramo: {{c1::olho e anexos}}<br>Para o sulco <b>lateral</b>: cerebral {{c1::média}}<br>Para a fissura <b>longitudinal</b>: cerebral {{c1::anterior}}<br>Para <b>trás</b>, até a cerebral posterior: {{c1::comunicante posterior}}</div>', AU['aci-ramos-org'][1])
AU['lobos-limites-org'] = (AU['lobos-limites-org'][0].replace('Sulco occipital lateral <b>variável</b>', 'Sulco occipital <b>variável</b>'), AU['lobos-limites-org'][1])

AU_FONTE['capsula-interna-partes-org'] = 'Apostila-guia Aula6 cap5; GaKa Aula4 PDF16 (braços da cápsula interna); Prova coletânea Q13; Machado cap7 §5.2.'

# Pré-checagem mecânica: negrito nos critérios, sem metacomentário no verso.
AU['hipotalamo-limites-org'] = (AU['hipotalamo-limites-org'][0].replace('<br>1.', '<br><b>1º</b>:').replace('<br>2.', '<br><b>2º</b>:').replace('<br>3.', '<br><b>3º</b>:').replace('<br>4.', '<br><b>4º</b>:'), AU['hipotalamo-limites-org'][1])
AU['capsula-interna-partes-org'] = (AU['capsula-interna-partes-org'][0].replace('Fórnix e cápsula interna:', '<b>Fórnix</b> e cápsula interna:'), AU['capsula-interna-partes-org'][1].split(' This follows')[0])
AU['aci-ramos-org'] = (AU['aci-ramos-org'][0].replace('Território desse ramo:', 'Ramo <b>orbitário</b>, território:'), AU['aci-ramos-org'][1])

# Segunda leitura do executor: retirar metatexto e corrigir exclusividade falsa da vista lateral.
AU['diencefalo-escondido'] = (AU['diencefalo-escondido'][0], 'The telencephalic hemispheres cover most of the diencephalon. Medial and inferior views expose its landmarks; lateral views mainly show the telencephalon, cerebellum and brainstem.')
AU['diencefalo-partes-org'] = (AU['diencefalo-partes-org'][0], 'The metathalamus comprises the medial and lateral geniculate bodies and is often included in the thalamus.')
AU['talamo-limites-org'] = (AU['talamo-limites-org'][0], 'In a coronal section, the thalamus borders the third ventricle medially and the internal capsule laterally. The hypothalamus and subthalamus lie below it, with the hypothalamus more medial.')
AU['hipotalamo-limites-org'] = (AU['hipotalamo-limites-org'][0], 'The infundibulum projects from the tuber cinereum and connects the hypothalamus to the pituitary. These ventral landmarks help orient the floor of the third ventricle.')
AU['faces-hemisferio'] = (AU['faces-hemisferio'][0], 'The medial surface faces the longitudinal fissure; the inferior surface rests on the cranial base. The superolateral surface faces the cranial vault.')
AU['estriado-org'] = ('Na nomenclatura <b>macroscópica</b>, núcleo lentiforme somado ao núcleo caudado forma o corpo {{c1::estriado}}.', 'Macroscopic corpus striatum groups the caudate and lentiform nuclei. Functional dorsal striatum comprises caudate plus putamen; globus pallidus belongs to the pallidum. The amygdala is a separate basal nuclear complex.')
AU['corte-horizontal-org'] = (AU['corte-horizontal-org'][0], AU['corte-horizontal-org'][1].replace(' (lesson)', ''))
EXTRA_RES[1792697125350] = 'The encephalon comprises the cerebrum, cerebellum and brainstem. The cerebrum includes the telencephalon and diencephalon; it is not synonymous with the whole encephalon.'
