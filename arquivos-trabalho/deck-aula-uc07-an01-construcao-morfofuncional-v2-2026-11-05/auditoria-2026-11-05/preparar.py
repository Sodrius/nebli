"""Auditoria incremental: fontes e candidatos explícitos; somente leitura do Anki."""
from pathlib import Path
import sys,json,re
A_DIR=Path(__file__).resolve().parent; R=A_DIR.parent
sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
A=Anki()
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
# fonte, posição na aula, significado que a imagem deve permitir recuperar.
defs=[
(1792265004509,8,'Axônio periférico mielínico','Myelin surrounds this peripheral axon in successive internodes. Nodes interrupt the sheath and permit saltatory conduction.'),
(1792265005765,8,'Axônio periférico amielínico','This peripheral axon lacks a compact myelin sheath. Absence of myelin differs from absence of Schwann-cell support.'),
(1792261717146,11,'Diencéfalo','The diencephalon lies between the cerebral hemispheres and the midbrain. It includes the thalamus and hypothalamus.'),
(1792261718340,11,'Tronco encefálico','The brainstem comprises midbrain, pons and medulla. It connects the spinal cord with more rostral structures and contains cranial nerve nuclei.'),
(1792261732545,11,'Mesencéfalo','The midbrain is the rostral brainstem division, above the pons. Its cavity is the cerebral aqueduct.'),
(1792244779394,11,'Ponte','The pons lies between midbrain and medulla, ventral to the cerebellum. Its broad ventral contour helps distinguish it from adjacent divisions.'),
(1792261734342,11,'Bulbo','The medulla is the caudal brainstem division, continuous with the spinal cord. Most corticospinal fibers cross in its caudal part.'),
(1792264998014,12,'Raiz anterior do nervo espinal','The anterior root carries motor axons leaving the spinal cord. It joins the sensory posterior root before the spinal nerve divides into mixed rami.'),
(1792328891560,12,'Ramo anterior do nervo espinal','The anterior ramus is mixed, carrying sensory and motor fibers. These rami form the major plexuses, while typical thoracic rami continue as intercostal nerves.'),
(1792328894044,12,'Ramo posterior','The posterior ramus supplies the deep back muscles and overlying skin. It is mixed, unlike the purely sensory posterior root.'),
(1792265017714,12,'Plexo cervical','The cervical plexus is formed by anterior rami of upper cervical nerves. Its position in the neck distinguishes it from the brachial plexus.'),
(1792265018865,12,'Plexo braquial','The brachial plexus redistributes fibers from spinal anterior rami to the upper limb. It is not formed by posterior roots or posterior rami.'),
(1792265020039,12,'Plexo lombar','The lumbar plexus contributes peripheral nerves to the lower limb. It is part of the lumbosacral organization introduced with spinal nerve plexuses.'),
(1792265021239,12,'Plexo sacral','The sacral plexus redistributes spinal fibers to the pelvis and lower limb. It continues the organization introduced by the lumbosacral plexus.'),
(1792261720696,13,'Lobo frontal','The frontal lobe lies anterior to the central sulcus. Its posterior part contains primary motor cortex; other frontal regions contribute to planning and behavior.'),
(1792261723219,13,'Lobo parietal','The parietal lobe lies posterior to the central sulcus. Its anterior portion contains primary somatosensory cortex.'),
(1792261725721,13,'Lobo temporal','The temporal lobe lies below the lateral sulcus. Its location helps orient lateral views before studying its auditory and memory-related regions.'),
(1792261728496,13,'Lobo insular','The insula lies deep within the lateral sulcus, covered by the opercula. It completes the five major lobes introduced with the cerebral hemispheres.'),
(1792261727072,13,'Lobo occipital','The occipital lobe occupies the posterior pole of the hemisphere. Visual cortical areas are situated here.'),
(1792348020020,13,'Sulco central','The central sulcus separates frontal and parietal lobes. The precentral motor gyrus lies anterior to it and the postcentral sensory gyrus posterior to it.'),
(1792345318994,14,'Corpo caloso','The corpus callosum is a major commissural white-matter bundle joining the cerebral hemispheres. Its arch is a key landmark in midsagittal views.'),
(1792345656566,14,'Ventrículo lateral','Each lateral ventricle is a cavity within a cerebral hemisphere. The cavity is distinct from surrounding white matter and deep gray nuclei.'),
(1792338018612,14,'Cápsula interna','The internal capsule is projection white matter between deep gray nuclei. Corticospinal fibers pass through it, linking the anatomy here to the lesion example later in the lecture.'),
(1792244844444,14,'Tálamo','The thalamus is diencephalic gray matter bordering the third ventricle. It must not be mistaken for the adjacent internal capsule or ventricular cavity.'),
(1792338030235,14,'Núcleo caudado','The caudate is a deep telencephalic gray nucleus associated with the lateral ventricle. It illustrates that gray matter is not restricted to the superficial cortex.'),
(1792338022186,14,'Putâmen','The putamen is a deep gray nucleus lateral to the globus pallidus. Together with the caudate it forms the dorsal striatum.'),
(1792338019837,14,'Globo pálido','The globus pallidus lies medial to the putamen and lateral to the internal capsule. It is deep gray matter rather than a white-matter tract.'),
(1792329448415,14,'Substância branca','White matter contains predominantly myelinated axons. In the spinal cord it surrounds the central gray matter; its arrangement differs from a superficial cortical ribbon.'),
(1792329449566,14,'Substância cinzenta','Spinal gray matter forms the central H-shaped region. It contains neuronal somata, dendrites and local synaptic circuits.'),
(1792329743638,14,'Canal central da medula espinal','The central canal is the small ependyma-lined cavity within the spinal cord. It is the caudal remnant of the embryonic neural-tube lumen.'),
(1792329748263,14,'Corno posterior da medula espinal','The posterior horn receives and processes sensory input. Primary sensory neuron somata are in the spinal ganglion, not in this horn.'),
(1792329749413,14,'Corno anterior da medula espinal','The anterior horn contains somatic lower motor neuron somata. Their axons leave through anterior roots to innervate skeletal muscle.'),
(1792338878331,15,'Núcleo do nervo oculomotor','The oculomotor motor nucleus is situated in the midbrain. It provides a concrete example of a cranial nerve nucleus within brainstem gray matter.'),
(1792338885887,15,'Núcleo do nervo abducente','The abducens nucleus is pontine gray matter. This position distinguishes it from the midbrain oculomotor nucleus and medullary hypoglossal nucleus.'),
(1792338706934,15,'Núcleo do nervo hipoglosso','The hypoglossal motor nucleus lies in the medulla. These brainstem somata send axons through a cranial nerve, analogous to spinal somatic motor output.'),
(1792338033014,16,'Aqueduto mesencefálico','The cerebral aqueduct is the narrow midbrain cavity linking the third and fourth ventricles. Its position helps identify a midbrain section.'),
(1792344606194,16,'Quarto ventrículo','The fourth ventricle lies dorsal to the pons and open medulla and ventral to the cerebellum. This relationship helps orient brainstem sections.'),
(1792244837493,16,'Colículo superior','The superior colliculus is part of the dorsal midbrain tectum. Its position supplies a landmark for the rostral midbrain section shown in the lecture.'),
(1792244821868,16,'Colículo inferior','The inferior colliculus lies caudal to the superior colliculus in the midbrain tectum. The lecture contrasts sections at these two levels.'),
(1792244781791,16,'Pedúnculo cerebral','The cerebral peduncle is a ventral midbrain landmark. Descending motor fibers occupy its ventral base, in contrast with the dorsal tectum.'),
(1792338737784,16,'Núcleo olivar inferior','The folded inferior olivary nucleus is a landmark of the open medulla. It lies dorsal to the ventral pyramid and helps orient the transverse section.'),
(1792438294828,16,'Tegmento mesencefálico','The midbrain tegmentum lies ventral to the cerebral aqueduct and dorsal to the peduncular base. It is distinct from the tectum dorsal to the aqueduct.'),
(1792328845991,17,'Intumescência cervical','The cervical enlargement contains expanded neuronal circuits for upper-limb innervation. It corresponds to a greater demand for limb motor and sensory connections.'),
(1792328848446,17,'Intumescência lombossacral','The lumbosacral enlargement contains expanded neuronal circuits for lower-limb innervation. Enlargement concerns neural circuitry, not simply vertebral width.'),
(1792244771792,19,'Pirâmides do bulbo raquidiano','The medullary pyramids contain descending corticospinal fibers. Their caudal decussation explains why lesion side must be interpreted relative to the crossing.'),
]
ADIAR={1792338030235,1792338022186,1792338019837,1792338878331,1792338885887,1792338706934,1792244837493,1792244821868,1792244781791,1792338737784,1792438294828}
put(A_DIR/"io-aulas-proprias.json",[{"src":src,"nome":name,"fonte":f"Lâmina {slide}","aula_destino": "Anatomia03 Medula/tronco/cerebelo" if src not in {1792338030235,1792338022186,1792338019837} else "Anatomia04 Diencéfalo/núcleos da base/telencéfalo", "estado":"previsto, não entregue na refação", "motivo":"IO regional aprofundado; básico na introdução, F-20261105-CODEX-07"} for src,slide,name,extra in defs if src in ADIAR])
defs=[x for x in defs if x[0] not in ADIAR]
allkh={n['nid']:n for n in json.loads((A_DIR/'kenhub-candidatos.json').read_text())}
rows=[]
for src,slide,name,extra in defs:
 n=allkh[src]; assert n['fields']['Nome PT']==name
 copies=A('findNotes',query='"tag:NEBLI::source::nid-'+str(src)+'"');ns=A('notesInfo',notes=copies)
 ns=[x for x in ns if x['modelName']=='NEBLI Kenhub IO v1' and x['fields']['Nome PT']['value']==name]
 # Preferir a identidade já estudada do curso, nunca deslocar original de referência.
 ci=A('cardsInfo',cards=[c for x in ns for c in x['cards']]);rank={x['noteId']:sum(c['reps'] for c in ci if c['note']==x['noteId']) for x in ns}
 ns.sort(key=lambda x:(-rank[x['noteId']],x['noteId']))
 row={'src':src,'slide':slide,'name':name,'extra':extra,'kind':'kenhub','key':'kh-'+str(src),'fonte':f'Lâmina {slide}; '+('apostila Aula1,cap6' if slide>=13 else 'Machado cap2–3'),'ganho':'Reconhecer a estrutura sem o nome visível,além da relação teórica já cobrada.','nid':ns[0]['noteId'] if ns else None}
 if ns:row['key']='sh-'+str(row['nid'])
 row['fields_source']=n['fields']; rows.append(row)
put(A_DIR/'selecao-kenhub.json',rows)
print(len(rows),'identificações;',sum(bool(x['nid']) for x in rows),'reusos com IDs existentes')
