"""Completa as especificações locais; não escreve no Anki."""
import importlib.util,json,re,pprint
from pathlib import Path
P=Path(__file__).parent
N={n['noteId']:n for n in json.loads((P/'live-notes.json').read_text()) if n}
N.update({n['noteId']:n for n in json.loads((P/'busca/alternativos-notes.json').read_text()) if n})
for filename in ['extra-notes.json','final-notes.json']:
 N.update({n['noteId']:n for n in json.loads((P/'busca'/filename).read_text()) if n})
def plain(t): return re.sub('<[^>]+>','',t)
def source(nid,flags,block,evidence,**kw):
 n=N[nid]; target=plain(n['fields']['Text']['value'])
 return dict(key=f'ak-{nid}',kind='text',src=nid,flags=flags,bloco=block,alvo=target,evid=evidence,
             uso='Reconstruir a resposta inflamatória e relacionar seu mecanismo aos sinais e aos defeitos de defesa.',
             motivo='Verde: mecanismo reutilizado na interpretação de inflamação; azul: detalhe válido de menor manutenção.',**kw)
def author(key,flags,block,text,extra,evid,**kw):
 return dict(key=key,kind='autoral',flags=flags,bloco=block,text=text,extra=extra,alvo=plain(text),evid=evid,
             uso='Relacionar o fundamento da aula ao mecanismo e à interpretação das provas UC03.',
             motivo='Verde para relação central; azul para nomenclatura/localização ou aprofundamento do mesmo mecanismo.',
             busca='Duas rotas: seções First Aid e conteúdo/sinônimos. Consulta também aos externos (MCAT e demais modelos); candidatos em busca/alternativos*.json. Nenhum candidato recupera este alvo no recorte.',**kw)
def save_spec(where,lesson,short,deck,cards,shared,excluded,out):
 where.mkdir(exist_ok=True)
 values={'RUN_ID':f'uc03-{short}-20260930-codex','SHORT':short,'LESSON':lesson,'DECK':deck,
 'CRITERIOS':'MEMORY + FEEDBACKS até F-20260930-CLAUDE-15; continuação Codex 30/09. Só decks.',
 'AUTHOR':'uc03','MEDIA':{},'CARDS':cards,'COMPARTILHADOS':shared,'EXCLUIDOS':excluded,'FORA_DO_RECORTE':out}
 (where/'spec-revisada.py').write_text('\n\n'.join(k+' = '+pprint.pformat(v,width=120,sort_dicts=False) for k,v in values.items())+'\n')

# Complemento: preserva o rascunho recebido em spec.py; versão nova independente.
s=importlib.util.spec_from_file_location('old',P/'complemento/spec.py');old=importlib.util.module_from_spec(s);s.loader.exec_module(old)
cards=old.CARDS; excluded=list(old.EXCLUIDOS)
drop={'c1inh-anafilatoxinas':'Formulação não confiável para AEH: edema por bradicinina, não por aumento generalizado de anafilatoxinas.',
      'aeh-diagnostico':'Repete C4 baixo e C1-INH já recuperados; subtipos clínicos laterais.',
      'lectinas-c1-like':'Substituído pelo alvo preciso MBL/MASP; C1-like é rótulo vago.'}
cards=[c for c in cards if c['key'] not in drop]
excluded += [(c.get('src'),drop[c['key']]) for c in old.CARDS if c['key'] in drop]
by={c['key']:c for c in cards}
by['fragmentos-a-b'].update(text='Cleavage of C3 releases soluble {{c1::C3a}}, which promotes inflammation, and {{c2::C3b}}, which covalently tags nearby surfaces for opsonization.',
 extra='C3b exposes a reactive thioester that can bind microbial surfaces. C4b also binds covalently, but this is not a property of every fragment named “b”. C2 naming varies between references; the lecture uses C4b2a, while this AnKing version uses C4b2b.')
by['tickover-b-d-properdina'].update(text='Alternative-pathway tickover begins with spontaneous {{c1::hydrolysis}} of C3; {{c2::factor D}} cleaves bound factor B, and {{c3::properdin}} stabilizes the surface convertase C3bBb.',
 extra='First, C3(H2O) binds B and D cleaves B, making fluid-phase C3(H2O)Bb. This enzyme cleaves C3; deposited C3b then binds B, and D forms surface C3bBb. Properdin stabilizes this surface enzyme, amplifying C3 cleavage without antibody.')
by['fator-i-h'].update(text='{{c1::Factor I}} proteolytically inactivates C3b, using cofactors such as {{c2::factor H}} or CR1.',
 extra='Factor H accelerates decay of C3bBb and serves as a cofactor for factor I. iC3b cannot form convertases, but remains an opsonin for CR3/CR4. Factor I also cleaves C4b, with appropriate cofactors such as C4BP, MCP or CR1; factor H regulates the alternative pathway.')
by['acido-sialico'].update(text='Host-cell {{c1::sialic acid}} favors factor H binding, helping limit alternative-pathway amplification on the host surface.',
 extra='Factor H promotes C3b inactivation and convertase decay. DAF/CD55 also accelerates convertase decay; MCP/CD46 supports factor I. CD59 acts later by preventing MAC assembly, not by inactivating C3b. Some microbes recruit factor H to evade complement.')
by['vias-inicio-infeccao']['extra']='Antibody-independent alternative and lectin activation can act immediately. Natural IgM and C-reactive protein may also activate the classical pathway early. As specific IgM/IgG accumulate, classical activation becomes more important; persistence of infection does not mean other pathways were never activated.'
by['fator-h-deficiencia']['text']='Severe factor H or factor I deficiency can cause uncontrolled alternative-pathway consumption: serum C3 is {{c1::low}}, while C4 may remain {{c2::normal}}.'
by['fator-h-deficiencia']['extra']='Failure to control C3 convertase consumes C3 and weakens opsonization. Some complement-regulatory defects also injure renal microvascular endothelium, producing atypical hemolytic uremic syndrome; normal C3 does not exclude that disorder.'
by['padrao-c3-c4']['text']='In immune-complex disease, low C3 plus low C4 suggests {{c1::classical}} pathway consumption; low C3 with preserved C4 suggests {{c2::alternative}} pathway consumption.'
by['padrao-c3-c4']['extra']='C4 is used by classical and lectin pathways, but not by the alternative pathway. These patterns guide investigation; they do not establish an individual protein deficiency by themselves.'
by['ch50-ah50']['text']='{{c1::CH50}} screens classical-pathway hemolytic function and {{c2::AH50}} screens alternative-pathway function; normal CH50 with absent AH50 suggests a defect in {{c3::factor B, factor D or properdin}}.'
by['ch50-ah50']['extra']='Both assays also require intact C3 and terminal components. Absent CH50 with preserved AH50 suggests C1, C2 or C4 deficiency. Low/absent results in both suggest a shared-component defect or complement consumption. Abnormal samples require confirmation.'
by['receptores-cr1-cr3']['text']='{{c1::CR1 (CD35)}} binds C3b/C4b and helps clear immune complexes; {{c2::CR3 (CD11b/CD18)}} binds iC3b and promotes phagocytosis.'
by['receptores-cr1-cr3']['extra']='Erythrocyte CR1 carries immune complexes to liver and spleen for removal by phagocytes; red cells do not phagocytose. CR1 also assists factor I. CR4 (CD11c/CD18) recognizes iC3b; C5aR mediates leukocyte recruitment/activation.'
by['precoces-les']['text']='Deficiency of early classical complement components (especially {{c1::C1q, C2 or C4}}) increases the risk of lupus and immune-complex disease.'
by['precoces-sinopulmonares']['extra']='Complement deficiency impairs bacterial defense; severe recurrent pyogenic infection is especially characteristic of C3 deficiency. C1q/C2/C4 deficiencies are also strongly associated with defective immune-complex clearance and autoimmunity.'
by['c1inh-angioedema']['extra']='C1-INH inhibits C1r/C1s and the contact/kinin system. Deficiency permits excessive kallikrein activity and bradykinin formation, causing vascular leakage and angioedema. The edema is not driven by histamine.'
by['aeh-sem-urticaria']['extra']='Bradykinin increases vascular permeability without the mast-cell histamine response responsible for typical itchy wheals. This contrasts with histaminergic angioedema.'
by['les-ch50']['text']='Active immune-complex disease in SLE may cause {{c1::decreased}} CH50 through complement consumption.'
by['les-ch50']['extra']='CH50 reflects functional classical-to-terminal pathway activity, not simply the concentration of one component. SLE does not invariably produce a low CH50.'
cards += [author('cd59-c9',{1:3},'F-regulacao','{{c1::CD59}} protects host membranes by preventing C9 polymerization and completion of the membrane attack complex.',
 'CD55/DAF acts earlier, accelerating convertase decay. CD59 blocks the final pore. Loss of GPI-linked CD55/CD59 explains complement-mediated hemolysis in PNH.','Slide CD59 e regulação; Abbas cap. 13, figura 13-16'),
 author('cr2-costimulo',{1:3},'E-funcoes','When an antigen binds the B-cell receptor and its attached C3d engages CR2, the threshold for B-cell activation {{c1::decreases}}.',
 'CR2/CD21 works with CD19 and CD81 as a B-cell co-receptor. Complement therefore supports antibody responses as well as directly opsonizing and lysing microbes.','Slide co-estímulo de linfócito B; Abbas cap. 13'),
 author('mbl-deficiencia',{1:4},'G-deficiencias','Mannose-binding lectin deficiency impairs the {{c1::lectin}} complement pathway and can increase susceptibility to infection.',
 'The effect is variable because classical and alternative pathways remain available. MBL deficiency does not imply that all complement activation is absent.','Slide deficiências da via das lectinas; Abbas cap. 13')]
save_spec(P/'complemento',old.LESSON,'imuno31',old.DECK,cards,old.COMPARTILHADOS,excluded,old.FORA_DO_RECORTE)

# Inflamação: seleção registrada pelo Claude, reavaliada no snapshot vivo.
groups=[
('A-reconhecimento','Slides definição, funções, PRR, TLR, sensores citosólicos e ácido úrico',[
(1487640028986,{1:4,2:3,3:4}),(1487640050564,{1:3}),(1500572039288,{3:3}),
(1520715624658,{1:3}),(1520715849479,{1:3})]),
('B-celulas-vasos','Slides acúmulo celular, eventos iniciais e sinais cardinais',[
(1487640248028,{1:4}),(1487640253946,{1:4}),(1487640263698,{1:4}),(1487640274492,{1:4}),(1520443529180,{1:4}),
(1487640261037,{1:3,2:3,3:3}),(1487640269487,{1:3,2:3,3:3}),
(1479267395454,{1:3}),(1487207084334,{1:3,2:4}),(1487207091819,{2:4}),
(1487640132837,{1:4}),(1487640136892,{1:4})]),
('C-migracao','Slides migração leucocitária, selectinas, integrinas, ICAM, PECAM, quimioatraentes',[
(1487642579270,{1:4,2:4}),(1487642582069,{1:4}),(1487642620769,{1:3,2:3}),
(1487642625895,{1:3,2:3}),(1487642632527,{1:3}),(1487642637710,{1:3})]),
('D-efetores','Slides fagocitose, burst oxidativo, degranulação e NETs',[
(1475890914685,{1:4}),(1487642733736,{1:3,2:3})]),
('E-mediadores','Slides cininas, sistemas plasmáticos, mediadores lipídicos e intervenção terapêutica',[
(1487640225601,{1:4}),(1487640230861,{1:4,2:3}),
(1487640059152,{1:3,2:3}),(1487640061733,{1:3}),(1487640068745,{1:3}),(1487640078840,{1:3}),
(1487640089158,{1:4,2:4}),(1487640101055,{1:3}),(1487640108934,{1:4}),
(1488847671701,{1:3,2:3}),(1488847679422,{1:3}),(1488854922125,{1:4}),(1488854930174,{1:4}),
(1488847688890,{1:3}),(1488847696894,{1:4}),(1473986398130,{2:3,3:3}),
(1463883753623,{1:3}),(1462061188088,{1:4,2:4}),(1474580819655,{1:4})]),
('F-sistemico','Slides IL-1/IL-6/TNF, fase aguda, febre, resposta sistêmica',[
(1487640278577,{1:3,2:3}),(1489969950421,{1:3}),(1489970026548,{1:3}),
(1489970181312,{1:3}),(1487642795725,{1:3}),(1520444046369,{1:3,2:4}),
(1520445108362,{1:3}),(1520445157941,{1:4}),(1520444298927,{1:4})]),
('G-resolucao','Slides resolução IL-10/TGF-beta, reparo e ligação à imunidade adaptativa; prova P2 2019 1.8',[
(1487642784485,{1:3}),(1520715124462,{1:3,2:3}),
(1520716108281,{1:3,2:4}),(1520717070355,{1:3,2:4})])]
cards=[source(nid,flags,block,evid) for block,evid,items in groups for nid,flags in items]
by={c['src']:c for c in cards}
by[1487640068745].update(text='Which prostaglandins promote vasodilation during inflammation? {{c1::PGD2, PGI2 (prostacyclin), and PGE2}}',extra='Increased blood flow produces redness and warmth. These prostaglandins can enhance edema through vasodilation and cooperation with permeability mediators; do not equate vasodilation with direct endothelial contraction.')
by[1487640108934]['extra']='The cysteinyl leukotrienes LTC4, LTD4 and LTE4 cause bronchial smooth-muscle contraction and increase microvascular permeability. LTB4 mainly recruits and activates leukocytes.'
by[1487640225601]['extra']='Activated factor XII connects contact activation to kallikrein/kinin formation and links inflammatory, coagulation and fibrinolytic pathways. Kallikrein releases bradykinin from high-molecular-weight kininogen.'
by[1475890914685]['extra']='The pentose phosphate pathway supplies NADPH; NADPH oxidase transfers electrons to oxygen to generate superoxide. Downstream oxidants help kill ingested microbes.'
by[1488847688890]['extra']='Aspirin covalently acetylates COX. Platelets cannot synthesize new enzyme, so their antiaggregant effect lasts for the affected platelet’s lifespan. Nucleated cells can replace COX; anti-inflammatory effects do not all last a platelet lifetime.'
by[1489970181312].update(text='Systemic release of TNF-α from activated {{c1::macrophages}} can cause widespread endothelial activation and shock.',extra='A local TNF response helps recruit leukocytes. Excessive systemic TNF promotes vascular leakage, vasodilation and coagulation activation, which can impair tissue perfusion.')
by[1520715849479]['extra']='Inflammasome assembly activates caspase-1, which cleaves pro-IL-1β and pro-IL-18 into active cytokines. This processing step differs from the transcriptional induction of their precursors.'
by[1520716108281]['extra']='IFN-γ (from NK or Th1 cells) and microbial signals promote classical activation: ROS/NO production and inflammatory cytokines. M1/M2 is a useful teaching contrast; real macrophage states form a spectrum.'
by[1520717070355]['extra']='IL-4/IL-13 promote alternative activation: tissue repair, fibrosis and dampening of inflammation. Resolution also requires removal of the stimulus and dead cells; it is not merely absence of cytokine production.'
by[1487642733736]['extra']='NADPH oxidase generates superoxide during the respiratory burst. Its deficiency impairs oxidant-dependent intracellular killing despite preserved ingestion. This clinical example tests the killing mechanism, not a separate catalogue of infections.'
cards += [
source(1479267468509,{1:3},'G-resolucao','Slides células da inflamação e ativação adaptativa',extra='Dendritic cells sense microbial/damage signals, acquire antigen and migrate to draining lymph nodes. They present antigen and co-stimulatory signals to naive T cells, linking local innate recognition to a specific adaptive response.'),
source(1487116849895,{1:3},'G-resolucao','Slide ativação e modulação da resposta adaptativa',extra='Innate recognition induces B7 and cytokines on dendritic cells. Antigen recognition and co-stimulation together activate naive T cells; the response then feeds back on phagocytes through cytokines.'),
source(1487117308213,{1:3},'B-celulas-vasos','Slide células da inflamação: células NK e lise de infectadas',extra='Perforin facilitates delivery of granzymes, which activate apoptotic pathways in the target cell. NK cells also produce IFN-γ that activates macrophages; this differs from phagocytosis by neutrophils.'),
source(1497451553581,{2:3},'D-efetores','Slides espécies reativas e células da inflamação',extra='iNOS converts arginine into nitric oxide. NO can react with superoxide to form peroxynitrite, supporting microbial killing. Microbial PRR signals and IFN-γ enhance this effector program; extracellular oxidants can also injure host tissue.'),
source(1554063916591,{1:4},'F-sistemico','Slide citocinas: ação autócrina',origin='AnKing-MCAT'),
source(1554064102112,{1:4},'F-sistemico','Slide citocinas: ação parácrina',origin='AnKing-MCAT'),
source(1554064278093,{1:4},'F-sistemico','Slide citocinas: ação endócrina',origin='AnKing-MCAT'),
author('tlr-endossomais',{1:3,2:4},'A-reconhecimento','TLRs that detect microbial nucleic acids (TLR3/7/8/9) are mainly {{c1::endosomal}}, whereas surface TLR5 recognizes bacterial {{c2::flagellin}}.',
 'Endosomal TLR3 senses dsRNA, TLR7/8 ssRNA, and TLR9 CpG-rich DNA. Surface TLR4 senses LPS; TLR2 heterodimers recognize microbial lipoproteins. Compartmentalization helps detect where microbial material is encountered.','Slides família TLR; Abbas cap. 4'),
author('nod-rig',{1:4,2:4},'A-reconhecimento','Cytosolic {{c1::NOD1/NOD2}} detect bacterial peptidoglycan fragments; {{c2::RIG-I-like receptors}} detect viral RNA.',
 'PRRs occur in distinct compartments: soluble (CRP, MBL), membrane/endosomal (TLRs), and cytosolic (NLRs and RLRs). NOD signaling promotes inflammatory gene expression; RLR signaling promotes antiviral interferons.','Slides tipos de receptores; Abbas cap. 4'),
author('dectina',{1:4},'A-reconhecimento','Fungal cell-wall β-glucans are recognized by {{c1::Dectin-1}}, a C-type lectin receptor on phagocytes.',
 'Recognition promotes phagocytosis and inflammatory signaling. Fungal sensing also involves other receptors; Dectin-1 is not a TLR.','Slides Dectina-1; provas P2 2017 2.8 / 2018 1.5; Abbas cap. 4'),
author('damps',{1:3},'A-reconhecimento','Necrotic tissue can trigger inflammation without infection by releasing {{c1::damage-associated molecular patterns (DAMPs)}}.',
 'ATP, nuclear proteins and other misplaced cellular contents alert resident phagocytes through innate sensors. After infarction, this response removes debris but activated neutrophils can also injure neighboring viable tissue.','Slides agressão não infecciosa; prova P1 2017 2.5; Abbas cap. 4'),
author('urato-nlrp3',{1:3},'A-reconhecimento','Monosodium urate crystals can activate the {{c1::NLRP3 inflammasome}}, leading to caspase-1-dependent IL-1β release.',
 'Crystal-induced cell stress promotes inflammasome assembly; NLRP3 is not simply a surface receptor binding dissolved uric acid. IL-1 recruits and activates inflammatory cells, explaining sterile inflammation in gout.','Slide ácido úrico; prova P1 2017 1.6; Abbas cap. 4; Martinon 2006'),
author('gota-il1',{1:4},'A-reconhecimento','Blocking {{c1::IL-1}} can suppress crystal-driven inflammation in gout downstream of NLRP3 activation.',
 'This targets the inflammatory signal rather than removing urate crystals. IL-1 blockade is a mechanism-based option in selected refractory cases, not the routine first treatment for every gout flare.','Prova P1 2017 1.6; slide ácido úrico e Abbas cap. 4'),
author('sequencia-vascular',{1:4,2:3},'B-celulas-vasos','A brief initial vasoconstriction may be followed by arteriolar {{c1::vasodilation}} and increased {{c2::postcapillary venular permeability}} during acute inflammation.',
 'Dilation increases blood flow (redness/warmth); vascular leakage creates protein-rich exudate and edema. Plasma loss increases blood viscosity and promotes stasis and leukocyte margination.','Slides sequência de eventos e sinais cardinais'),
author('cinetica-celular',{1:4},'B-celulas-vasos','After the initial neutrophil wave, recruited {{c1::monocytes/macrophages}} become more prominent over roughly the next 1–2 days of acute inflammation.',
 'The lecture gives macrophage recruitment at 12–48 h and later lymphocytes; eosinophils may increase after 72 h in allergic inflammation. These are teaching timelines, not fixed cutoffs: the stimulus and tissue change the pattern. Resident macrophages are already present at the start.','Slide acúmulo celular; prova P2 2025 2.4'),
author('eotaxina',{1:4},'C-migracao','{{c1::Eotaxin}} preferentially recruits eosinophils, whereas IL-8 and LTB4 are major neutrophil chemoattractants.',
 'PAF can also activate/recruit eosinophils but has broader effects and is not an eosinophil-specific chemokine. Chemotaxis follows a chemical gradient into the affected tissue.','Slide migração por quimioatraentes'),
author('nets',{1:4},'D-efetores','Neutrophil extracellular traps (NETs) are webs of {{c1::chromatin coated with antimicrobial proteins}} that trap microbes outside the cell.',
 'NETs concentrate granule proteins around microbes. They complement phagocytosis but extracellular histones/proteases can also damage host tissue; trapping a microbe is not the same as internalizing it into a phagosome.','Slide ativação completa do neutrófilo; Rigby/DeLeo 2011 citado na aula'),
author('neuropeptideos',{1:4,2:4},'E-mediadores','In neurogenic inflammation, sensory nerves release {{c1::substance P}}, which promotes vascular leakage, and {{c2::CGRP}}, a potent vasodilator.',
 'Local sensory nerve activity can amplify edema and blood flow and interact with mast cells. This is a local inflammatory mechanism as well as pain signaling.','Slide inflamação neurogênica'),
author('cinetica-mediadores',{1:3,2:4},'E-mediadores','Mast-cell {{c1::histamine}} acts rapidly because it is stored in granules; prostaglandins and leukotrienes must be {{c2::synthesized after activation}}.',
 'Histamine/bradykinin dominate early vascular events; lipid mediators and cytokines sustain the response, while pro-resolving mediators help terminate it. These waves overlap rather than following strict exclusive time windows.','Slides pré-formados/neoformados; prova P2 2025 2.4'),
author('lipoxinas-resolvinas',{1:3,2:4},'G-resolucao','Lipoxins and resolvins promote resolution by limiting further {{c1::neutrophil recruitment}} and enhancing macrophage clearance of {{c2::apoptotic cells}}.',
 'Resolution is an active program. Lipoxins derive from arachidonic acid and resolvins from omega-3 fatty acids; both help end inflammation without simply preventing all immune defense.','Slide resolução; prova P2 2025 2.4; Schwab et al., Nature 2007'),
author('eferocitose',{1:3},'G-resolucao','During resolution, macrophages remove apoptotic neutrophils by {{c1::efferocytosis}}, limiting release of their damaging contents.',
 'Clearance of dying cells, withdrawal of the stimulus, and IL-10/TGF-β help switch the tissue toward repair. Failure to clear debris can perpetuate inflammation.','Slides resolução; Abbas cap. 4'),
source(1475966862515,{1:4},'A-reconhecimento','Slide tipos de receptores: scavengers e oxLDL',extra='Scavenger receptors recognize modified host molecules as well as some microbial ligands. Here oxidized LDL illustrates this receptor class; the wider pathogenesis of atherosclerosis belongs to another lesson.'),
]
# Alvos já vivos: adicionar associação, nunca criar cópia nem mudar marca pessoal.
tag='NEBLI::2026-uc03-imunologia-37-inflamacao-inicio-resolucao'
shared={n['noteId']:'Associação prévia da aula: mecanismo inflamatório pertinente, conferido no snapshot.' for n in N.values() if tag in n['tags']}
shared.update({nid:'Mecanismo pré-existente pertinente: PRR, marginação, ROS, estase, PAF ou permeabilidade.' for nid in [1790253141963,1790253142871,1790253144373,1790253144533,1790253537100,1790253537574,1790253537195]})
excluded=[(1479267358567,'Mesmo alvo de neutrófilos já testado no compartilhado 1790253141778; figura pode apoiar outros cards.'),
(1520299451730,'PRR/PAMP já recuperados no compartilhado 1790253141963.'),
(1520299562982,'IκB quinase detalha sinalização além da recuperação necessária no slide; NF-kB preservado.'),
(1471541327679,'Vasodilatação/permeabilidade já testadas; contração venosa genérica não acrescenta ao mecanismo central.'),
(1471541598687,'Mesmo motivo: manter bradicinina/vasodilatação/permeabilidade nos compartilhados.'),
(1487640120758,'Absoluto sobre permeabilidade por prostaglandinas é impreciso; apoio corrigido no alvo de vasodilatação.'),
(1487640124653,'Cisteinil-leucotrienos já recuperados; LTB4 não deve ser generalizado como vasoconstritor.'),
(1488854891621,'Precursor ácido araquidônico já recuperado na liberação por PLA2.'),
(1499356681150,'COX e seus produtos já recuperados, sem ganho na inversa.'),
(1488854963588,'COX-2, PGE2 e dor já recuperados.'),(1488854967929,'COX-2, PGE2 e febre já recuperados.'),
(1489970022577,'Macrófagos como fonte de citocinas já recuperados no card de febre.'),
(1489970054827,'Fonte de IL-6 já recuperada no card de febre.'),(1489970091921,'IL-8 de macrófagos já recuperada no card de recrutamento.'),
(1489970615786,'IL-10 já recuperada no card de resolução.'),(1520445172196,'Albumina negativa ausente no texto atual; não necessária para recuperar os efeitos sistêmicos centrais.'),
(1487642801171,'Abscesso morfológico pertence à Patologia; rascunho trazia também absoluto incorreto sobre S. aureus.'),
(1480563969014,'Desvio à esquerda acrescentaria hematologia fora do mecanismo desta aula.')]
save_spec(P/'inflamacao','2026-uc03-imunologia-37-inflamacao-inicio-resolucao','imuno37','NEBLI::UC03::P2::Imunologia::Inflamação: início e resolução',cards,shared,excluded,
 ['Subtipos de hipersensibilidade, granulomas e diferenciação adaptativa completa são aulas próprias.',
  'Mastocitose, Chédiak-Higashi, critérios SIRS, tratamentos de sepse e catálogo clínico de imunodeficiências não são importados.',
  'LAD e CGD entram apenas como consequência compreensível da falha de adesão/killing; os demais irmãos clínicos ficam fora.',
  'Transcrição de fatos das provas não revoga a precisão científica nem amplia automaticamente o recorte.'])
print('Especificações revisadas salvas.')
