"""Curadoria explícita desta aula. Produz plano local, não escreve no Anki."""
import hashlib, html, json, re
from pathlib import Path
import fitz
from inspecionar_v2 import call, ROOT

LESSON='2026-uc03-patologia-38-inflamacao-aguda'
SLIDE='https://drive.google.com/file/d/1O5qLt4JANr93Hv7tEXeZ8TddmsiHKAjw/view'
OUT=ROOT/'revisao-v2'
OUT.mkdir(exist_ok=True)

# ID, páginas, objetivo efetivamente perguntado, prioridade local.
ADDITIONS=[
 (1474503768203,[6,7],'transudato-hidrostatica','alta'),
 (1474503771577,[6,7],'transudato-oncotica','alta'),
 (1474503784942,[6,7],'exsudato-permeabilidade','alta'),
 (1487640059152,[13],'origem-acido-araquidonico','alta'),
 (1487640061733,[13],'via-cox','alta'),
 (1487640101055,[13],'via-lox','alta'),
 (1488854972928,[13],'aine-cox','alta'),
 (1463883746350,[13],'corticoide-pla2','alta'),
 (1488854998221,[13],'aine-lesao-gastrica','alta'),
 (1474580780060,[13],'bloqueio-leucotrienos','media'),
 (1474571630796,[9,12],'histamina-permeabilidade','alta'),
 (1487642661164,[33,34,35],'fagossomo-lisossomo','alta'),
 (1487642714884,[35],'burst-oxidativo','alta'),
 (1487640219508,[33,34],'opsoninas','media'),
 (1487642791049,[35],'digestao-enzimatica','media'),
 (1487642786172,[29],'neutrofilos-macrofagos','alta'),
 (1479267395454,[36,38],'limpeza-macrofagos','alta'),
 (1489970026548,[32],'fase-aguda-il6','media'),
 (1482275776638,[39],'erosao','alta'),
 (1482275780185,[39],'ulcera','alta'),
 (1701515819045,[24,25,38],'colagenases-mec','alta'),
]

# Lacunas após buscas: termos + tag Pathoma + corpus externo. Perguntas curtas,
# sem reconstruir todo o capítulo. Imagens docentes são necessárias à tarefa visual.
LOCAL=[
 ('finalidade',[2,3], 'Acute inflammation is an initial response to tissue injury aimed at {{c1::eliminating the injurious stimulus and restoring tissue homeostasis}}.', 'Não é sinônimo de infecção: trauma, necrose, corpos estranhos e hipersensibilidade também podem desencadear a resposta.','alta','durable'),
 ('edema-funcao',[2,4], 'In acute inflammation, <b>swelling (tumor)</b> results mainly from {{c1::extravasation of fluid into the interstitium (edema)}}. Pain, edema and tissue injury may also cause {{c2::loss of function (functio laesa)}}.', 'Rubor/calor: hiperemia. Dor: mediadores e pressão local sobre terminações. Tumor aqui significa inchaço, não neoplasia.','alta','durable'),
 ('estase',[8,17,18], 'Inflammatory fluid loss from vessels causes {{c1::hemoconcentration and increased blood viscosity}}, slowing blood flow (stasis) and favoring leukocyte {{c2::margination}}.', 'Vasodilatação aumenta inicialmente a chegada de sangue. A saída de plasma concentra células e favorece a aproximação dos leucócitos do endotélio. Não confundir aumento inicial de fluxo com manutenção de alta velocidade.','alta','durable'),
 ('contracao-lesao',[9,10], 'Inflammatory vascular leakage due to <b>endothelial contraction</b> is usually {{c1::rapid, transient and reversible}}; leakage due to <b>direct endothelial injury</b> persists until {{c2::the damaged endothelial barrier is repaired}}.', 'Contração/retração abre junções sem matar necessariamente a célula. Lesão direta causa necrose/descolamento. Queimadura grave pode causar extravasamento imediato e sustentado: não decorar que toda lesão direta começa tarde.','alta','durable'),
 ('lesao-leucocitaria',[10,35,38], 'Activated leukocytes can prolong vascular leakage and damage nearby tissue by releasing {{c1::reactive oxygen species and proteolytic enzymes}} outside phagolysosomes.', 'A mesma maquinaria que destrói agentes pode lesar endotélio e matriz. A lesão mediada por leucócitos mantém/amplifica a permeabilidade; não é um mecanismo totalmente separado do dano colateral.','alta','durable'),
 ('transcitose',[10], 'In inflammation, <b>transcytosis</b> increases vascular permeability by transporting fluid and proteins {{c1::through endothelial cells in vesicular channels}}, rather than between their junctions.', 'É a via transcelular; não confundir com passagem por espaços interendoteliais nem com transcitose de IgA no epitélio. Nesta aula foi um mecanismo complementar, não o principal.','media','durable'),
 ('linfa',[11], 'Acute inflammation {{c1::increases::increases/decreases}} lymphatic drainage, carrying excess interstitial fluid, antigens and antigen-presenting cells toward {{c2::regional lymph nodes}}.', 'A resposta pode incluir proliferação de vasos linfáticos. Drenagem ajuda a retirar líquido e conecta a resposta local à adaptativa, sem exigir repetir aqui toda a apresentação de antígeno.','alta','durable'),
 ('linfonodo',[11], 'Why may regional lymph nodes enlarge during local inflammation?<br><br>{{c1::Increased antigen/cell delivery stimulates reactive immune-cell activation and proliferation.}}', 'Linfonodomegalia reativa não significa automaticamente metástase. É possível, não uma regra de que toda inflamação produza linfonodo palpável.','alta','durable'),
 ('histamina-fontes',[12], 'In the lecture\'s vascular-mediator table, histamine is released by {{c1::mast cells and platelets}} and promotes vasodilation and increased permeability.', 'Retém a combinação de fontes explicitamente solicitada na tabela. Mastócitos são uma fonte tecidual importante; basófilos também liberam histamina, sem precisar estudar sua biologia inteira aqui.','media','durable'),
 ('no',[12], 'Nitric oxide (NO) from {{c1::endothelial cells and macrophages}} contributes to inflammatory {{c2::vasodilation}}.', 'NO relaxa músculo liso vascular. Separar esse papel dos mecanismos de abertura de junções; não atribuir genericamente toda contração endotelial ao NO.','alta','durable'),
 ('paf',[12], 'Platelet-activating factor (PAF), produced by leukocytes, can promote {{c1::platelet activation}} and, at low concentrations, {{c2::vasodilation and increased vascular permeability}}.', 'A tabela da aula destaca origem leucocitária e efeitos vasculares. Não é necessário listar todos os produtores ou receptores do PAF.','alta','durable'),
 ('residentes',[4,5,15], 'Which resident cells help initiate acute inflammation before circulating neutrophils are recruited?<br><br>{{c1::Tissue macrophages and mast cells}}', 'Reconhecimento local → mediadores → recrutamento. Monócitos e neutrófilos vêm do sangue; plaquetas e eosinófilos também participam conforme o contexto. Não transformar cada célula citada em uma aula nova.','alta','durable'),
 ('cinética',[29], 'What is the usual sequence of dominant changes in an acute inflammatory response?<br><br>{{c1::Early edema → neutrophil influx → later monocyte/macrophage predominance}}', 'Os fenômenos se sobrepõem. Não existe uma divisão rígida em que a fase vascular precisa terminar para começar a celular; a janela depende do estímulo.','alta','durable'),
 ('afinidade',[21,22,23], 'Chemokine signaling changes leukocyte integrins from a low-affinity to a {{c1::high-affinity}} state, converting rolling into {{c2::firm adhesion}} to endothelial ICAM/VCAM.', 'ICAM/VCAM são ligantes endoteliais da superfamília das imunoglobulinas, não integrinas. Selectinas predominam no rolamento; ativação de integrinas permite adesão firme.','alta','durable'),
 ('quimiotaxia-gradiente',[24,28], 'Chemotaxis directs leukocyte migration {{c1::up a chemical concentration gradient, toward its source}}.', 'A lista de quimiotáticos já está em AnKing. Esta pergunta cobre o mecanismo direcional, não apenas os nomes. C5a é quimiotático importante; C3a não é equivalente em potência/função.','alta','durable'),
 ('sistemico',[31,32], 'Beyond local endothelial activation, inflammatory cytokines can cause {{c1::fever, leukocytosis and increased hepatic acute-phase protein production}}.', 'TNF/IL-1 participam da resposta sistêmica; IL-6 é central na síntese hepática de fase aguda (ex.: PCR). Mal-estar, sonolência e redução do apetite são efeitos associados.','alta','durable'),
 ('resolucao-lipidica',[36], 'Resolution of acute inflammation includes a shift from proinflammatory lipid mediators toward {{c1::pro-resolving mediators, such as lipoxins}}.', 'Além da retirada do estímulo: mediadores de meia-vida curta desaparecem, neutrófilos sofrem apoptose e macrófagos removem restos e favorecem IL-10/TGF-β. Não requer decorar todas as resolvinas.','media','durable'),
 ('desfechos',[37,38], 'After acute inflammation, preserved tissue architecture and removal of the stimulus favor {{c1::complete resolution}}; extensive tissue/ECM destruction favors {{c2::fibrosis (scar formation)}}; persistence of the stimulus favors {{c3::chronic inflammation}}.', 'São destinos condicionados pelo dano e pelo estímulo, não uma sequência obrigatória. Granulomas e mecanismos de inflamação crônica ficam para a aula própria.','alta','durable'),
 ('flegmao',[40,41,42], 'Suppurative inflammation spreading diffusely through tissue planes, without a localized pus-filled cavity, is a {{c1::phlegmon}}; a localized collection of pus is an {{c2::abscess}}.', 'A distinção é distribuição difusa × coleção delimitada. P2 2025, questão 2.2, cobra padrão flegmonoso/supurativo necrosante. Pode coexistir ulceração, como na inflamação ulcero-flegmonosa.','alta','durable'),
 ('drenagem',[42], 'Why may antibiotics alone fail to eliminate an abscess?<br><br>{{c1::The poorly perfused, pus-filled cavity can require drainage for source control.}}', 'Não significa que antibióticos nunca penetram, nunca ajudam ou que todo abscesso deve ser tratado do mesmo modo. Local, tamanho e estado clínico determinam a conduta; aqui importa o princípio anatomopatológico. Referência de segurança: https://www.merckmanuals.com/professional/infectious-diseases/bacterial-skin-infections/cutaneous-abscess','alta','durable'),
 ('tabela-local',[7], 'In this lecture\'s simplified table, exudate is associated with protein concentration {{c1::> 3 g/dL}} and specific gravity {{c2::> 1.020}}; transudate tends to be lower.', 'Detalhe local da tabela, não critério diagnóstico universal. Ela também contrasta LDH >200 versus <200 sem unidade explícita: não transformar esse número em regra clínica. Para derrame pleural, usar critérios específicos (Light).','baixa','exam'),
]

VISUAL=[
 ('v-ulcera',[39],[1872,1874],'Identify the morphological pattern and its key structural feature.', 'Ulceration: loss of surface continuity with a deeper tissue defect, with necrotic/inflammatory material at its base.','Úlcera péptica como exemplo da aula. Não é necessário diagnosticar a etiologia apenas pela fotografia.'),
 ('v-flegmao',[40],[1920,1921],'Which inflammatory pattern is illustrated by diffuse extension through the tissue wall?', 'Phlegmonous inflammation: diffuse suppurative infiltration through tissue planes, rather than a discrete abscess cavity.','Associar à distribuição na parede. A histologia isolada não identifica o microrganismo.'),
 ('v-abscesso',[41,42],[1968,2015],'Identify the inflammatory pattern and the material concentrated in its center.', 'Abscess: a localized collection of pus, containing neutrophils and necrotic cellular debris.','Delimitação do foco é o contraste com flegmão. Cápsula fibrosa pode se desenvolver, mas não é requisito universal.'),
 ('v-marginacao',[20],[987],'Where are the leukocytes positioned relative to the vessel lumen, and what recruitment step does this illustrate?', 'Near the endothelial surface (vessel periphery): leukocyte margination.','Imagem estática mostra posição; não demonstra sozinha o movimento de rolamento.'),
 ('v-diapedese',[27],[1303],'Which recruitment step is illustrated by leukocytes crossing the vessel wall into tissue?', 'Transmigration (diapedesis).','Distinguir célula junto à parede, ainda intravascular, de célula atravessando a parede.'),
]

def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def strip_clozes(text,keep):
    return re.sub(r'\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}',lambda m:m.group(0) if int(m[1]) in keep else m[2],text,flags=re.S)
def yield_label(tags):
    ys=[t for t in tags if '::#Low/HighYield::' in t]
    levels={t.rsplit('::',1)[-1] for t in ys}
    if len(levels)>1:return 'conflitante',ys
    raw=next(iter(levels),'')
    return {'1-HighYield':'HY','2-RelativelyHighYield':'HY relativo','3-HighYield-temporary':'HY provisório','4-LowerYield':'LY','5-LowYield':'LY'}.get(raw,'não classificado'),ys
def metadata(pages,priority,group,label,origin,why):
    return ('<div class="nebli-aula-v2" style="font-size:15px;border-top:1px solid #888;padding-top:8px;margin-top:14px;text-align:left">'
     f'<b>Faculdade: {priority} · Step: {label} · {dict(durable="Núcleo durável",exam="Detalhe de prova",reserve="Reserva")[group]}</b>'
     f'<br>{html.escape(why)}<br><a href="{SLIDE}">Aula — pp. {", ".join(map(str,pages))}</a>'
     f'<br><small>Origem: {html.escape(origin)}. Yield herdado, quando disponível; não é classificação oficial do USMLE.</small></div>')

def main():
    before=json.loads((ROOT/'before-v2.json').read_text(encoding='utf-8'))
    v1=json.loads(Path('curriculum/lessons/'+LESSON+'/selection.json').read_text(encoding='utf-8'))
    page_by_old={'ia-01-definicao-sinais':[2,4],'ia-02-desencadeantes-reconhecimento':[3,5],'ia-03-exsudato-transudato':[6,7],'ia-04-fluxo-estase':[8,17,18],'ia-05-permeabilidade':[9,10],'ia-06-mediadores-vasculares':[12,13],'ia-07-recrutamento-leucocitario':[16,21,23,25],'ia-08-quimiotaxia-citocinas':[28,31,32],'ia-09-resolucao':[36,38],'ia-10-padroes-morfologicos':[41,42]}
    old_rows=[(x['source_nid'],sorted({p for o in x['objectives'] for p in page_by_old[o]}),x['reason'],'alta') for x in v1['candidates']]
    wanted=[x[0] for x in old_rows+ADDITIONS]
    sources=call('notesInfo',notes=wanted)
    assert all(n.get('noteId') for n in sources),'Fonte indisponível'
    byid={n['noteId']:n for n in sources}
    existing={int(t.split('nid-')[-1]):n for n in before['notes'] for t in n['tags'] if t.startswith('NEBLI::source::nid-')}
    entries=[]
    for nid,pages,obj,priority in old_rows+ADDITIONS:
        src=byid[nid];fields={k:v['value'] for k,v in src['fields'].items()}; fields['ankihub_id']=''
        prior=existing.get(nid)
        if prior:fields={k:v['value'] for k,v in prior['fields'].items()}
        keep=sorted({int(c) for c in re.findall(r'\{\{c(\d+)::',fields['Text'])})
        edits=[];group='durable'
        if nid==1487207084334:
            keep=[1];fields['Text']=strip_clozes(fields['Text'],keep);edits.append('Somente c1 histamina; tryptase sem novo card.')
        if nid==1701515819045:
            keep=[1];fields['Text']=strip_clozes(fields['Text'],keep);edits.append('Somente c1 MEC/colagenases; c2/c3 apenas contexto visível.')
        if nid in [1487981833078,1487982014218]:
            direction='increased' if nid==1487981833078 else 'decreased'
            kind='Exudative' if nid==1487981833078 else 'Transudative'
            opposite='transudative' if nid==1487981833078 else 'exudative'
            fields['Text']=f'{kind} fluid generally has {{{{c1::{direction}}}}} LDH compared with {opposite} fluid.'
            fields['Extra']='<p>Comparação qualitativa entre exsudato e transudato; não afirmar que LDH do exsudato precisa exceder a sérica. Os critérios de Light são específicos para derrame pleural e usam relações e limites laboratoriais.</p>'+fields['Extra']
            priority='media';group='reserve';edits.append('Corrigido comparador LDH, mantendo alvo e cloze.')
        if nid==1535296447535:group='reserve';priority='media'
        if nid==1487642801171:
            fields['Text']='Acute inflammation may result in an {{c1::abscess}}, a localized collection of pus within tissue.'
            fields['Extra']='<p>Pus contains neutrophils and necrotic debris. Fibrous encapsulation may develop but is not required to define an abscess. Multiple organisms can cause abscesses; etiology depends on the site and context.</p>'
            edits.append('Corrigida definição e removida generalização sobre S. aureus.')
        if nid==1487642791049:
            fields['Text']='Which lysosomal enzyme helps macrophages destroy bacterial cell walls?<br>{{c1::Lysozyme}}'
            edits.append('Retirada alegação excessiva de enzima principal para todo material.')
        if nid==1487640068745:
            fields['Text']='Which prostaglandins promote vasodilation in acute inflammation?<br>{{c1::PGD<sub>2</sub>, PGI<sub>2</sub> (prostacyclin), and PGE<sub>2</sub>}}'
            edits.append('Separado efeito vasodilatador da abertura direta de junções.')
        if nid==1487642620769:
            fields['Text']='Leukocyte integrins can be activated by {{c1::C5a}} and {{c2::LTB<sub>4</sub>}}, facilitating firm adhesion.'
            edits.append('Ativação/afinidade não confundida com simples aumento de expressão.')
        if nid==1474580780060:group='reserve'
        label,yields=yield_label(src['tags'])
        origin='AnKing' if nid!=1701515819045 else 'Histology (ploirodon)'
        extra=metadata(pages,priority,group,label,origin,obj)
        fields['Extra']=fields.get('Extra','')+extra
        # Em atualização, somente campos realmente alterados; nenhum template compartilhado.
        changed={k:v for k,v in fields.items() if not prior or v!=prior['fields'].get(k,{}).get('value')}
        entries.append({'key':f'source-{nid}','source_nid':nid,'source_hash':digest(src['fields']),'source_model':src['modelName'],'origin':origin,'existing_nid':prior['noteId'] if prior else None,'before_fields':{k:v['value'] for k,v in prior['fields'].items()} if prior else None,'fields':changed,'clozes':keep,'pages':pages,'objective':obj,'local_priority':priority,'retention_group':group,'step_yield':label,'yield_tags':yields,'source_tags':src['tags'],'adaptations':edits})
    for key,pages,text,extra,priority,group in LOCAL:
        fields={'Text':text,'Extra':extra+metadata(pages,priority,group,'não classificado','NEBLI — complemento da aula',key)}
        entries.append({'key':key,'origin':'NEBLI-local','fields':fields,'clozes':sorted({int(c) for c in re.findall(r'\{\{c(\d+)::',text)}),'pages':pages,'objective':key,'local_priority':priority,'retention_group':group,'step_yield':'não classificado','search_evidence':['busca-acervo.json','candidatos-v2.json'],'reason':'Nenhum candidato adequado identificado nas buscas; recorte docente explícito.'})
    pdf=fitz.open(ROOT/'slides.pdf');media=[]
    for num,(key,pages,xrefs,q,a,extra) in enumerate(VISUAL,1):
        names=[]
        for j,xref in enumerate(xrefs):
            img=pdf.extract_image(xref);name=f'nebli-ia-v2-fig-{num:02}-{j+1}.{img["ext"]}'
            (OUT/name).write_bytes(img['image']);names.append(name);media.append(name)
        text=q+'<br>'+''.join(f'<img src="{name}" style="max-width:100%;max-height:380px">' for name in names)+'<br>{{c1::'+a+'}}'
        fields={'Text':text,'Extra':extra+metadata(pages,'alta','durable','não classificado','Imagens da aula, uso pessoal',key)}
        entries.append({'key':key,'origin':'NEBLI-visual','fields':fields,'clozes':[1],'pages':pages,'objective':key,'local_priority':'alta','retention_group':'durable','step_yield':'não classificado','search_evidence':['busca-acervo.json','candidatos-v2.json'],'reason':'AnKing não testa as imagens específicas ensinadas; extração nativa sem gerar/desenhar histologia.'})
    # Duas figuras comparativas do pulmão já rotuladas: apoio no verso, não pergunta que entrega a resposta.
    for xref,name in [(707,'nebli-ia-v2-apoio-vascular.png'),(1440,'nebli-ia-v2-apoio-celular.png')]:
        pix=fitz.Pixmap(pdf,xref);pix.save(str(OUT/name));media.append(name)
    for e in entries:
        if e['key']=='cinética':e['fields']['Extra']+='<br><img src="nebli-ia-v2-apoio-vascular.png"><br><img src="nebli-ia-v2-apoio-celular.png">'
    plan={'lesson_id':LESSON,'target_deck':before['deck'],'profile_evidence':before['media_dir'],'source_pdf_sha256':hashlib.sha256((ROOT/'slides.pdf').read_bytes()).hexdigest(),'book_status':'Robbins & Cotran informado; capítulo integral indisponível','sources':sources,'entries':entries,'media':media,'flags_policy':'preserve; color choice pending','next_lesson':'UC08 Histologia, somente após aprovação deste deck; fontes no Drive'}
    (OUT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'notes':len(entries),'cards':sum(len(e['clozes']) for e in entries),'existing_notes':sum(bool(e.get('existing_nid')) for e in entries),'new_anking_notes':sum(e['origin']=='AnKing' and not e.get('existing_nid') for e in entries),'other_deck_notes':sum(e['origin'].startswith('Histology') for e in entries),'local_notes':len(LOCAL),'visual_notes':len(VISUAL),'media':len(media)},ensure_ascii=False))

if __name__=='__main__':main()
