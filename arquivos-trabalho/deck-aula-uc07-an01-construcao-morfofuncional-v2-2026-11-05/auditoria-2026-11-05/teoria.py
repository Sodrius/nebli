from pathlib import Path
import sys,json,re
D=Path(__file__).resolve().parent;R=D.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
A=Anki()
defs=[
('telencefalo-adulto',1479351793884,3,'O <b>telencéfalo embrionário</b> origina os {{c1::hemisférios cerebrais}}.','The telencephalic vesicles expand into the paired cerebral hemispheres. Their cavities become the lateral ventricles.','vesiculas'),
('diencefalo-adulto',1479351810861,3,'O <b>diencéfalo embrionário</b> origina o {{c1::tálamo}} e o {{c1::hipotálamo}}.','The thalamus and hypothalamus are major diencephalic derivatives. They are not divisions of the brainstem.','vesiculas'),
('cavidade-telencefalo',1479351805802,3,'A <b>cavidade do telencéfalo</b> origina os {{c1::ventrículos laterais}}.','The walls become the cerebral hemispheres, while the paired cavities remain as lateral ventricles. Wall derivatives and cavity derivatives are different targets.','vesiculas'),
('cavidade-diencefalo',1479353800465,3,'A <b>cavidade do diencéfalo</b> origina o {{c1::terceiro ventrículo}}.','The third ventricle is a midline cavity related to the diencephalon. The thalamus and hypothalamus form parts of its surrounding walls.','vesiculas'),
('cavidade-mesencefalo',1479351825915,3,'A <b>cavidade do mesencéfalo</b> permanece como {{c1::aqueduto cerebral}}.','The narrow midbrain cavity connects the third and fourth ventricles. The surrounding midbrain tissue and the aqueduct must not be confused.','vesiculas'),
('cavidade-metencefalo',1479351840610,3,'A <b>cavidade do metencéfalo</b> contribui para a parte {{c1::superior do quarto ventrículo}}.','Metencephalon and myelencephalon contribute to the fourth ventricular cavity; their walls form pons/cerebellum and medulla respectively.','vesiculas'),
('cavidade-mielencefalo',1479351848667,3,'A <b>cavidade do mielencéfalo</b> contribui para a parte {{c1::inferior do quarto ventrículo}}.','The caudal hindbrain cavity contributes to the lower fourth ventricle. Its walls form the medulla, while the caudal neural-tube lumen continues into the central canal.','vesiculas'),
('glia-radial',1701811410368,3,'Na <b>migração cortical embrionária</b>, neurônios utilizam prolongamentos da {{c1::glia radial}} como suporte.','Radial glial processes provide a scaffold from the ventricular region toward the developing cortex. Axonal growth cones instead guide an extending axon toward its target.','glia'),
('ependima',1479430544195,6,'Os <b>ventrículos encefálicos</b> são revestidos por células {{c1::ependimárias}}.','Ependymal cells line the ventricular system and central canal. This epithelial arrangement differs from astrocytes within the neural parenchyma.','medula'),
('satelites',1701814678887,6,'Nos <b>gânglios periféricos</b>, células {{c1::satélites}} envolvem os corpos neuronais.','Satellite glia support neuronal somata and regulate their local environment. Schwann cells instead associate with peripheral axons; both derive from neural crest.','raizes'),
('lamina-alar',1479351856218,15,'No <b>tubo neural embrionário</b>, a lâmina alar origina componentes {{c1::sensitivos}}.','Alar derivatives contribute sensory gray matter. Basal derivatives contribute motor gray matter, explaining the functional organization of spinal and brainstem nuclei.','nucleos'),
('lamina-basal',1479351861109,15,'No <b>tubo neural embrionário</b>, a lâmina basal origina componentes {{c1::motores}}.','Motor neuron groups arise from the basal plate. Cranial nerve motor nuclei and spinal motor neurons are central gray matter, whereas peripheral ganglia lie outside the CNS.','nucleos'),
('motoneuronios-centrais',1480389622314,15,'Motoneurônios {{c1::inferiores}} ficam no corno {{c2::anterior}} medular e em <b>núcleos motores cranianos</b> do tronco.','Their axons reach skeletal muscle through spinal or cranial nerves. A nucleus is the central group of somata; the nerve contains the outgoing axons.','nucleos'),
('walleriana',1479430645161,19,'Após <b>lesão axonal</b>, a degeneração {{c1::walleriana}} ocorre {{c2::distalmente}} ao local lesado.','The axonal segment disconnected from its soma degenerates. Following the degenerating fibers through serial sections can reveal a pathway and its crossing.','lesao'),
('decussacao',1480389648940,19,'A maioria das <b>fibras corticoespinais</b> cruza na decussação {{c1::piramidal}}, no {{c2::bulbo caudal}}.','A lesion above the crossing affects the opposite side of the body. A lesion of the lateral corticospinal tract below the crossing affects the same side, so the section level is essential.','lesao'),
]
rows=[]
sources={}
for key,src,slide,text,extra,img in defs:
 n=A('notesInfo',notes=[src])[0];sources[str(src)]=n
 copies=A('findNotes',query='"tag:NEBLI::source::nid-'+str(src)+'"');ns=A('notesInfo',notes=copies)
 # Outra UC não muda de idioma: fazer cópia pessoal traduzida, com origem explícita.
 copies=[n for n in ns if n['modelName']=='NEBLI UC07 AnKing v1']
 rows.append(dict(key=key,src=src,slide=slide,text=text,extra=extra,img=img,kind='teoria',origin='Histology' if src in (1701811410368,1701814678887) else 'AnKing',nid=copies[0]['noteId'] if copies else None,fonte='Machado cap2–3; apostila Aula1; lâmina '+str(slide)))
(D/'selecao-teoria.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(D/'teoria-fontes-integrais.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2))
for key,n in sources.items():
 print(key,n['modelName'])
 for f in ('Text','Extra'):
  print(f,re.sub('<[^>]+>',' ',n['fields'].get(f,{}).get('value',''))[:1900])
