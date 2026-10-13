"""Plano de correções pontuais; não escreve no Anki."""
import json
import re
from pathlib import Path
P = Path(__file__).resolve().parent
notes = {}
for f in ('related-before.json', 'before.json', 'refresh.json'):
    notes.update({n['noteId']: n for n in json.loads((P/f).read_text())['notes']})
changes = {}
def put(nid, reason, **fields):
    changes.setdefault(nid, {'nid':nid, 'fields':{}, 'reason':[]})
    changes[nid]['fields'].update(fields)
    changes[nid]['reason'].append(reason)
def img(name, width=760):
    return f'<img src="{name}" style="width:100%;max-width:{width}px;height:auto">'
def crop(name, size, box, width=760):
    # Enquadramento HTML responsivo: preserva os pixels e a mídia originais.
    w,h = size; x,y,x1,y1=box; cw,ch=x1-x,y1-y
    return (f'<div style="width:100%;max-width:{width}px;margin:12px auto;background:white">'
            f'<div style="position:relative;height:0;padding-bottom:{100*ch/cw:.4f}%;overflow:hidden">'
            f'<img src="{name}" style="position:absolute;left:{-100*x/cw:.4f}%;top:{-100*y/ch:.4f}%;'
            f'width:{100*w/cw:.4f}%;max-width:none;height:auto;margin:0"></div></div>')
def table(head, rows):
    return '<table style="border-collapse:collapse;width:100%;max-width:760px;margin:12px auto;font-size:0.85em;text-align:left"><tr>'+''.join(f'<th style="border-bottom:2px solid #888;padding:5px">{x}</th>' for x in head)+'</tr>'+''.join('<tr>'+''.join(f'<td style="border-bottom:1px solid #aaa;padding:5px">{x}</td>' for x in r)+'</tr>' for r in rows)+'</table>'

papilla_table=table(['Papilla','Shape / location','Taste buds'],[
    ['Filiform','Pointed; most of the anterior dorsum','None — friction'],
    ['Fungiform','Mushroom; scattered, especially tip and sides','On the upper surface'],
    ['Foliate','Parallel folds on the posterolateral edges','In the fold walls'],
    ['Vallate','Large, in a V just anterior to terminal sulcus','In the trench walls']])
papilla_img=crop('576cbd235527ed0da189465acdf9daa7.webp',(836,859),(0,40,590,659))
for nid,n in notes.items():
    extra=n['fields'].get('Extra',{}).get('value','')
    text=n['fields'].get('Text',{}).get('value','')
    if '576cbd235527ed0da189465acdf9daa7.webp' in extra:
        extra=re.sub(r'<img[^>]*src="576cbd235527ed0da189465acdf9daa7.webp"[^>]*>',papilla_img,extra)
        if any(t in text.lower() for t in ['papilla','von ebner']): extra += papilla_table
        put(nid,'Figura de papilas enquadrada e comparação por forma, posição e botões gustativos',Extra=extra)
    if '477f80c20c979758e5f388cc1e5639dc.webp' in extra:
        extra=re.sub(r'<img[^>]*src="477f80c20c979758e5f388cc1e5639dc.webp"[^>]*>',img('paste-c48392999e02addb2523601703c99452e50a5af4.jpg'),extra)
        put(nid,'Treitz: peça com inserção e junção duodenojejunal legíveis',Extra=extra)

plexus_table=table(['Plexus','Where','Main role'],[['Submucosal (Meissner)','Submucosa','Secretion and local blood flow'],['Myenteric (Auerbach)','Between circular and longitudinal muscle','Motility']])
for nid in [1790979864034,1790979864785,1791023357268]:
    extra=notes[nid]['fields']['Extra']['value']
    extra=re.sub(r'<img[^>]*>', '', extra)
    put(nid,'Preservar mnemônico S–secretion/M–motility e mostrar a posição dos dois plexos',Extra=extra+plexus_table+img('7622bdccaa72d53bb3fae2ccf397d414-fig.png'))

oral_img=crop('238874aec9d1f27de9c5a3649f56a870.webp',(403,615),(25,45,398,420),520)
for nid in [1791023353318,1791023353068,1791023353568]:
    put(nid,'Substituir panorama do aparelho digestivo por mucosa oral reconhecível',Extra='- <b>Lining mucosa</b> is flexible and nonkeratinized.<br>- On this lip section, <b>OM</b> marks oral mucosa; the opposite side is skin.'+oral_img)
saliva=crop('64488be5c84f06ac3036fdb6d536e599.webp',(800,743),(20,50,784,600))
put(1791023355318,'Comparação histológica que mostra o predomínio mucoso',Extra='- <b>Right: sublingual</b>, predominantly pale mucous tubules (M).<br>- <b>Left: submandibular</b>, predominantly darker serous acini (A).<br>- Mucin-rich secretion lubricates food and the oral lining.'+saliva)
put(1791023355818,'Mucinas: mostrar o citoplasma pálido, não anatomia das glândulas',Extra='- Mucin-rich granules stain weakly with routine H&E.<br>- Compare pale <b>mucous tubules (M)</b> with dark <b>serous acini (A)</b>.'+saliva)
parietal=crop('4534b7a2f4a6be49ccb02757d26c2325.webp',(838,966),(360,420,728,785),650)
put(1790979868887,'Mostrar estado de repouso versus estimulado e cobrar o destino da fusão',Text='During parietal cell stimulation, proton pump-containing tubulovesicles fuse with the {{c1::<b>canalicular membrane</b>}}.',Extra='- <b>Left: resting</b> — pumps are stored in tubulovesicles (TV).<br>- <b>Right: stimulated</b> — vesicles fuse with the canalicular membrane, adding pumps and expanding the microvillar surface.'+parietal)
put(1791023364492,'Ampliar canalículo e explicar que é invaginação contínua com o lúmen',Extra='- <b>IC = intracellular canaliculus</b>, an inward fold of the apical surface, continuous with the gastric lumen.<br>- <b>MV = microvilli</b> lining that space; pumps in their membrane secrete H⁺ into it.'+parietal)
put(1791023270891,'Uma frase natural, sem juntar duas afirmações com ponto e vírgula',Text='Unlike skeletal muscle, smooth muscle lacks {{c1::<b>troponin</b>}}.',Extra=table(['Muscle','Ca²⁺ sensor','How contraction is enabled'],[['Skeletal','Troponin C','Moves tropomyosin off actin sites'],['Smooth','Calmodulin','Activates MLCK, which phosphorylates myosin']]))
put(1791023270317,'Substituir foto de músculo por representação do local de liberação',Extra='- Varicosities are swellings along autonomic axons that release transmitter near several muscle cells.<div style="max-width:620px;margin:12px auto;padding:16px;border:1px solid #888"><b>Autonomic axon</b><div style="font-size:30px;color:#4478a8">──●────●────●──</div><div>Varicosities containing vesicles</div><div>↓ &nbsp; transmitter diffusion &nbsp; ↓</div><div style="border:2px solid #999;border-radius:40%;padding:12px">Smooth muscle cells</div></div>')
put(1791023357918,'Mapa de camadas específico para glândulas cárdicas esofágicas',Extra='- Near the stomach, <b>esophageal cardiac glands</b> add protective mucus from the <b>lamina propria</b>.'+table(['From lumen outward','Glands'],[['Stratified squamous epithelium','Surface lining'],['Lamina propria — mucosa','Esophageal cardiac glands, especially near the stomach'],['Muscularis mucosae','Boundary below the lamina propria'],['Submucosa','Esophageal glands proper']]))

put(1790979866060,'Uma resposta anatômica curta; sinônimo no verso',Text=notes[1790979866060]['fields']['Text']['value'].replace('antral/pyloric stomach','pylorus'),Extra='- Pyloric (antral) mucosa has deep gastric pits and coiled, predominantly mucous glands.')
put(1790980911405,'Cobrar a origem da renovação em vez da palavra tip',Text='Most intestinal epithelial cells arise in the {{c1::<b>crypts</b>}} and differentiate while migrating toward the villus tip.')
put(1790980916280,'Cobrar a função central e explicar o nome; retirar ausência absoluta de Paneth no cólon',Text='Deep crypt secretory cells help maintain the colonic {{c1::<b>stem cells</b>}}.',Extra='- <b>Deep crypt</b> describes their position beside stem cells at the crypt base.<br>- They provide niche support analogous to Paneth cells in the small intestine; the REG4+ niche was demonstrated in mouse colon.')
put(1791054012018,'Retirar ketoacidosis/ DKA da pista visível sem perder nenhum irmão',Text='In uncontrolled <b>diabetes mellitus</b>, {{c1::<b>Kussmaul</b>}} breathing compensates for the metabolic {{c2::<b>acidosis</b>}} caused by ketone accumulation.',Extra='- Deep breathing lowers CO₂ and partially compensates for the pH fall.<br>- Ketone accumulation produces the metabolic disorder; ventilation does not remove its cause.')
put(1791054015697,'Cloze de um termo, preservando o mecanismo sem alegação ambígua de first change',Text='Hyperglycemia damages the glomerular basement membrane through nonenzymatic {{c1::<b>glycation</b>}}.',Extra=notes[1791054015697]['fields']['Extra']['value'])
put(1791023366868,'Distinguir EC de ECL em vez de atribuir serotonina a todas as células do fundo',Text='Gastrointestinal <b>enterochromaffin (EC)</b> cells release {{c1::<b>serotonin</b>}}.',Extra=table(['Cell','Mediator','Role'],[['EC','Serotonin (5-HT)','Coordinates intestinal secretion and motility'],['ECL, gastric body/fundus','Histamine','Stimulates acid secretion by parietal cells']]))
put(1791014716874,'Corrigir exclusividade falsa no verso e reescrever ambos os Tabs',Extra='- Vagal acetylcholine stimulates <b>chief cells</b> to release pepsinogen.<br>- Luminal acid also stimulates secretion through local reflexes and converts pepsinogen into pepsin.')
colipase_diagram='<div style="max-width:620px;margin:16px auto;padding:14px;border:1px solid #888;border-radius:12px"><div><b>Intestinal lumen</b></div><div style="padding:10px;border:2px solid #5b8fb9;margin:8px">Pancreatic lipase</div><div>↕</div><div style="padding:10px;border:2px solid #a98454;margin:8px"><b>Colipase</b> — anchoring cofactor</div><div>↕</div><div style="padding:14px;border:3px solid #a98454;border-radius:45%;margin:8px">Bile salt-coated <b>fat droplet</b><br>Triglycerides</div><div>Lipase at the interface → fatty acids + monoglycerides</div></div>'
put(1791000309552,'Trocar slide genérico por esquema do mecanismo e Tab narrativo',Extra='- Bile salts emulsify fat but interfere with lipase attachment.<br>- <b>Colipase anchors lipase</b> at the fat–water interface; lipase performs the hydrolysis.'+colipase_diagram)

# Identificação visual com resposta manual curta, mesmos IDs e mesmo histórico.
put(1790980909978,'Identificação manual do duodeno, sem legenda longa e sem resposta exposta',Header='Identify the intestinal segment.',Image=img('paste-23f15a744b47e12b54f1bf00c0856efef881399f.png'),**{'Question Mask':'','Answer Mask':'','Original Mask':'','Remarks':'<b>Duodenum</b><br>Villi plus pale submucosal Brunner glands distinguish this segment from jejunum and ileum.'})
put(1790980912277,'Micrografia de livro legível, com células granulares no fundo da cripta',Header='Identify the cells with red apical granules at the crypt base.',Image=img('bt04-paneth.png',560),**{'Question Mask':'','Answer Mask':'','Original Mask':'','Remarks':'<b>Paneth cells</b><br>The red apical granules contain antimicrobial products. The pale cell labelled G is a goblet cell.'})
put(1790980916154,'Uma micrografia legível e uma resposta; comparação somente no verso',Text='This mucosa belongs to the {{c1::<b>small intestine</b>}}.<br>'+img('paste-c0d5f2212078b85ae5387902cc5e8619aa9d014c.png',760),Extra='- Villi project above the crypts in the <b>small intestine</b>.<br>- In contrast, the <b>colon</b> has crypts but no villi.'+img('bt04-colon-glands.png',400))
put(1790973210184,'Seta adicionada ao asset compartilhado das três constrições esofágicas')
for nid,answer in [(1790973222133,'Long vasa recta (jejunum)'),(1790973222856,'Short vasa recta (ileum)')]:
    put(nid,'Comparação imediata no verso; preservar o agendamento dos cards já estudados',Remarks='<b>'+answer+'</b>'+table(['Segment','Arterial arcades','Vasa recta'],[['Jejunum','Few tiers','Long'],['Ileum','Many tiers','Short']])+img('nebli-moore-fig-5-48.png'))

put(1784300091178,'Definir evaginação sacular com linguagem simples',Text='Diverticul/o indica uma pequena {{c1::<b>bolsa</b>}} que se projeta para fora da parede de um órgão.',Extra='<b>Evaginação sacular</b> significa uma projeção para fora em forma de saco. Um divertículo intestinal comunica-se com o interior do intestino; diverticulite é sua inflamação.')
put(1784308054026,'Separar duas recuperações; clasia já tem card próprio',Text='Em <b>litotripsia</b>, -tripsia indica {{c1::<b>fragmentação</b>}}.',Extra='Litotripsia fragmenta um cálculo em pedaços menores. O termo -clasia é estudado separadamente em osteoclasia.')
put(1784308062270,'Resposta curta para clasia em seu card próprio',Text='Em <b>osteoclasia</b>, -clasia indica {{c1::<b>fratura</b>}}.',Extra='Osteo- = osso. Osteoclasia é a fratura deliberada de um osso para corrigir uma deformidade.')
put(1784308054011,'Mesmo padrão de duas respostas independentes no mesmo cloze',Text='Em <b>artrodese</b>, -dese indica {{c1::<b>fusão</b>}}.',Extra='Artro- = articulação. Artrodese produz fusão cirúrgica para impedir o movimento daquela articulação; -clasia refere-se a fratura.')
put(1784308059853,'Base antes do termo, resposta curta',Text='Em <b>atresia</b>, a- indica {{c1::<b>ausência</b>}} de uma abertura normal.',Extra='<b>a-</b> = ausência; <b>trēsis</b> = abertura/perfuração. A luz é o espaço interno de um órgão tubular. Na atresia esofágica, a passagem pelo esôfago não é contínua; estenose significa estreitamento.')
put(1784308059925,'Separar etimologia e condição clínica',Text='Em <b>eosinófilo</b>, -filo indica {{c1::<b>afinidade</b>}} pela eosina.',Extra='Eosina é um corante. Os grânulos do eosinófilo têm afinidade por ele. <b>Eosinofilia</b> é aumento de eosinófilos; esse é o significado do termo clínico completo.')
put(1784308059948,'Um elemento recuperável por card',Text='Em <b>litíase</b>, lit/o significa {{c1::<b>cálculo</b>}}.',Extra='<b>lit/o</b> = pedra/cálculo; <b>-íase</b> = condição patológica. Litíase é a condição caracterizada por cálculos.')
put(1784300091186,'Desmembrar mentalmente sem cobrar três respostas juntas',Text='Em <b>sialolitíase</b>, o cálculo se forma no sistema {{c1::<b>salivar</b>}}.',Extra='<b>sial/o</b> = saliva; <b>lit/o</b> = cálculo; <b>-íase</b> = condição. O termo reúne as três partes: cálculo em glândula ou ducto salivar.')
put(1784308062198,'Separar raiz etimológica do efeito do prefixo',Text='O elemento <b>-trofia</b> refere-se à {{c1::<b>nutrição</b>}} dos tecidos.',Extra='Do grego <i>trophḗ</i>, nutrição. O termo completo descreve a condição do tecido: hipertrofia = aumento do tamanho celular; atrofia = redução. A raiz não significa que todo termo com -trofia indique crescimento.')

# Feedbacks antigos já atendidos: marcar somente após conferência do estado vivo.
verified=[1784308057250,1784308057313,1784308057390,1784308059839,1790974691830,1790978724448,1790980910230,1790981527126,1791023294146,1791023296668,1791023363069,1791034105561,1790974692329,1791023302118]
for nid in verified: put(nid,'Conferido: correção anterior presente no card vivo')
for nid,c in changes.items():
    comment=notes[nid]['fields'].get('NEBLI_Comentario',{}).get('value','')
    if comment and 'CORRIGIDO, 05/10/2026' not in comment:
        c['fields']['NEBLI_Comentario']=comment+'<br>CORRIGIDO, 05/10/2026.'
    c['before']={k:notes[nid]['fields'][k]['value'] for k in c['fields']}
    c['fields']={k:v for k,v in c['fields'].items() if v != c['before'][k]}
    c['before']={k:v for k,v in c['before'].items() if k in c['fields']}
changes={nid:c for nid,c in changes.items() if c['fields']}
(P/'changes.json').write_text(json.dumps(list(changes.values()),ensure_ascii=False,indent=2))
print(len(changes),'notas preparadas')
for nid,c in changes.items(): print(nid, ', '.join(c['fields']), '; '.join(c['reason']))
