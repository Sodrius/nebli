import hashlib,json,re,sys
from pathlib import Path
from inventory import call
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc03-microbiologia-27-fisiologia-bacteriana'
DECK='NEBLI::UC03::P2::Microbiologia::Fisiologia bacteriana'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
RESOURCE_FIELDS=['Lecture Notes','Missed Questions','Pathoma','Boards and Beyond','First Aid','Sketchy','Sketchy 2','Sketchy Extra','Picmonic','Pixorize','Physeo','Bootcamp','OME']
ON_TOPIC=re.compile(r'Fundamentals of Bacteriology',re.I)
SLIDE='<i><span style="font-size: 10pt;">Fonte: slides da aula de Fisiologia bacteriana (UC03)</span></i>'
def img(name,caption=SLIDE): return f'<br><br><img src="{name}"><br>{caption}'
# mídia a gravar antes do apply: (arquivo local, nome na coleção)
MEDIA=[('img/p6_2.png','nebli-fisio-temperatura.png'),('img/p10_1.png','nebli-fisio-ferro.png'),('img/p19_2.png','nebli-fisio-fermentacao.png'),
       ('img/p22_2.png','nebli-fisio-curva.png'),('img/virulencia-fases.png','nebli-fisio-virulencia-fases.png'),('img/p39_1.png','nebli-fisio-esgotamento.png'),
       ('img/p50_3.png','nebli-fisio-tioglicolato.png')]
def yt(vid,t,label): return f'<a href="https://www.youtube.com/watch?v={vid}'+(f'&t={t}s' if t else '')+f'">{label}</a>'
VID_CURVA=yt('ZebbwJ6H_DI',0,"Shomu's Biology — Bacterial growth curve (45 min; basta a parte das 4 fases, a cinética vai além da aula)")
# nid -> (objetivo, [edições])  edições: ('replace',campo,antigo,novo) | ('append',campo,html) | ('uncloze',[n]) | ('set',campo,html)
SOURCES={
 1500498257612:('O2-classes',[]),
 1500499431143:('O2-classes',[('append','Extra','Ex. da aula: <i>E. coli</i>. Tubo de tioglicolato: aeróbio estrito no topo (1), anaeróbio estrito no fundo (2), facultativo em todo o tubo, mais no topo (3), microaerófilo logo abaixo da superfície (4), aerotolerante uniforme (5).'+img('nebli-fisio-tioglicolato.png'))]),
 1500498894447:('O2-classes',[('uncloze',[2]),('append','Extra','<br>Ex. da aula: <i>Clostridium tetani</i>.')]),
 1510191036224:('O2-classes',[]),
 1500497965459:('E-energia',[('set','Extra','Na respiração anaeróbia o aceptor final é outro composto inorgânico (NO<sub>3</sub><sup>−</sup>, SO<sub>4</sub><sup>2−</sup>, CO<sub>3</sub><sup>2−</sup>); na fermentação não há cadeia respiratória.')]),
 1500671879509:('C-curva',[('append','Extra','<br>A aula acrescenta a <b>fase de declínio</b>: a morte supera a divisão até a cultura se esterilizar.')]),
 1500672897393:('C-curva',[('append','Extra','<br>Não há divisão, mas há aumento de massa e síntese de enzimas (adaptação ao meio).')]),
 1500672960517:('C-curva',[]),
 1500673093880:('C-curva',[]),
 1500673150522:('C-curva',[('append','Extra','<br>Antibióticos que atacam síntese (parede, proteína, DNA) agem melhor em células em divisão ativa.')]),
 1500490858110:('M-meios',[]),
 1500491274684:('M-meios',[('append','Extra','<br>Não confundir com <b>caldo de enriquecimento</b> (selenito, tetrationato): meio líquido que favorece <i>Salmonella</i> frente à microbiota.')]),
 1500491508023:('M-meios',[]),
 1500491849175:('M-meios',[('uncloze',[1,3])]),
 1500492267320:('M-hemolise',[]),
 1500492032825:('M-hemolise',[]),
 1500492284543:('M-hemolise',[]),
 1500496061553:('M-meios',[('uncloze',[2]),('append','Extra','Também contém cristal violeta; lactose é o único açúcar e o vermelho neutro é o indicador de pH.')]),
 1402600814505:('M-meios',[]),
 1515889860040:('M-meios',[]),
 1500493993054:('M-meios',[]),
 1510260138577:('M-meios',[('uncloze',[1]),('append','Extra','<br>TCBS: amarelo = fermentação de sacarose (<i>V. cholerae</i>); <i>V. parahaemolyticus</i> não fermenta (verde).')]),
 1510187224507:('M-meios',[('append','Extra','<br>No ágar SS, tiossulfato + citrato férrico revelam o H<sub>2</sub>S (colônias de centro negro); sais biliares e citrato inibem Gram+ e coliformes.')]),
}
VIDEOS={'C-curva':VID_CURVA}
AUTHORED=[
 ('mesofilos','Bacteria that grow best at moderate temperatures (about 20–45 °C), including most human pathogens such as <i>E. coli</i>, are {{c1::mesophiles}}',
  'A maioria cresce melhor em pH ~7 (neutro). Tolerância a sal: <i>S. aureus</i> é halotolerante.'+img('nebli-fisio-temperatura.png'),'N-ambiente'),
 ('ferro','The host keeps free iron very low by sequestering it in transferrin, lactoferrin, and ferritin ({{c1::nutritional immunity}}); pathogenic bacteria counter with iron-chelating {{c2::siderophores}}',
  'Ferro baixo ativa, via proteína Fur, genes de captação de ferro e de virulência (hemolisinas, toxinas).'+img('nebli-fisio-ferro.png'),'N-ferro'),
 ('respiracao-fermentacao','In anaerobic respiration the final electron acceptor is an inorganic compound other than O<sub>2</sub> (e.g., {{c1::nitrate or sulfate}}), whereas fermentation regenerates NAD<sup>+</sup> by reducing an {{c2::organic molecule}} (e.g., pyruvate → lactate)',
  'Em procariotos a cadeia respiratória fica na membrana plasmática. A fermentação gera ATP só por fosforilação no nível do substrato (2 ATP/glicose).'+img('nebli-fisio-fermentacao.png'),'E-energia'),
 ('tempo-duplicacao','Under optimal conditions, <i>E. coli</i> doubles about every {{c1::20 minutes}}, whereas <i>M. tuberculosis</i> takes about {{c2::18–24 hours}}',
  'Por isso a cultura de <i>M. tuberculosis</i> leva semanas, com fase lag longa e fase log pouco inclinada.'+img('nebli-fisio-curva.png'),'C-curva'),
 ('virulencia-fases','In <i>S. aureus</i>, surface adhesins are expressed mainly in the exponential phase, whereas secreted toxins predominate in the {{c1::stationary}} phase',
  'Adesinas (fator <i>clumping</i>, proteínas ligadoras de fibronectina e colágeno, proteína A) na fase log; coagulase e toxinas na transição para a estacionária.'+img('nebli-fisio-virulencia-fases.png'),'C-curva'),
 ('esgotamento','Streaking an inoculum across successive areas of a solid medium (esgotamento) dilutes it to obtain {{c1::isolated colonies}}, each arising from a single cell',
  'Incubação típica: 37 °C por 24 h; uma colônia visível leva 12–48 h.'+img('nebli-fisio-esgotamento.png'),'M-isolamento'),
]
def digest(v): return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def clozes(v): return sorted({int(x) for x in re.findall(r'{{c(\d+)::',v)})
CLOZE=re.compile(r'\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}',re.S)
def uncloze(text,nums): return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0),text)
def clean_resources(f):
    changed=[]
    for k in RESOURCE_FIELDS:
        v=f.get(k,'')
        if not v.strip(): continue
        if k=='Bootcamp':
            parts=[p for p in re.split(r'(?:\s*<br>\s*)+',v) if p.strip()]
            new='<br><br>'.join(p for p in parts if ON_TOPIC.search(p))
        else: new=''
        if new!=v: f[k]=new; changed.append(k)
    return changed
def main():
    notes={n['noteId']:n for n in call('notesInfo',notes=list(SOURCES))}
    if set(notes)!=set(SOURCES): raise RuntimeError('Fonte ausente')
    entries=[];collisions={}
    for nid,(obj,edits) in SOURCES.items():
        n=notes[nid]; f={k:v['value'] for k,v in n['fields'].items()}
        if not n['modelName'].startswith('AnKingOverhaul (AnKing'): raise RuntimeError(f'Modelo {nid}')
        found=call('findNotes',query=f'tag:"NEBLI::source::nid-{nid}"')
        if found: collisions[nid]=found
        log=[]
        for e in edits:
            if e[0]=='replace':
                if e[2] not in f[e[1]]: raise RuntimeError(f'Trecho ausente {nid}')
                f[e[1]]=f[e[1]].replace(e[2],e[3])
            elif e[0]=='append': f[e[1]]=(f[e[1]]+'<br>' if f[e[1]].strip() else '')+e[2]
            elif e[0]=='set': f[e[1]]=e[2]
            elif e[0]=='uncloze':
                before=clozes(f['Text']); f['Text']=uncloze(f['Text'],set(e[1]))
                if set(clozes(f['Text']))!=set(before)-set(e[1]): raise RuntimeError(f'Uncloze {nid}')
            log.append([e[0],e[1]])
        res=clean_resources(f)
        if res: log.append(['resources_cleared',res])
        if obj in VIDEOS: f['Additional Resources']=VIDEOS[obj]; log.append(['videos'])
        entries.append({'key':f'source-{nid}','source_nid':nid,'source_model':n['modelName'],'source_tags':n['tags'],'source_fields_hash':digest(n['fields']),'fields':f,'copy_changes':log,'objective':obj,'origin':'AnKing','expected_cards':len(clozes(f['Text'])),'high_yield':HY in n['tags']})
    for key,text,extra,obj in AUTHORED:
        fields={'Text':text,'Extra':extra}
        if obj in VIDEOS: fields['Additional Resources']=VIDEOS[obj]
        entries.append({'key':'authored-'+key,'source_nid':None,'source_model':None,'source_tags':[],'source_fields_hash':None,'fields':fields,'copy_changes':[],'objective':obj,'origin':'Autoral','expected_cards':len(clozes(text)),'high_yield':False})
    t=lambda o: sum(x['expected_cards'] for x in entries if x['origin']==o)
    plan={'lesson_id':LESSON,'target_deck':DECK,'lesson_date':'2026-09-04','profile_evidence':call('getMediaDirPath'),'media':MEDIA,
      'source_manifest':'source-manifest.json','entries':entries,'associate_existing':[],'collisions':collisions,
      'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':t('AnKing'),'Autoral':t('Autoral'),'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield']),'associated_existing_notes':0}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'totals':plan['totals'],'collisions':collisions},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
