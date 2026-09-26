import hashlib,json,re,sys
from pathlib import Path
from inventory import call

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).parent
LESSON='2026-uc08-biologia-tecidual-intestinos'
DECK='NEBLI::UC08::Biologia Tecidual::Intestinos'
HY='#AK_Step1_v12::#Low/HighYield::1-HighYield'
SOURCES={
  1486608749626:'intestinal-epithelium',
  1486608754106:'small-intestine-surface',
  1486608758394:'intestinal-crypt',
  1486608763486:'crypt-stem-cell',
  1486608768857:'paneth-antimicrobial',
  1486608774946:'duodenum-brunner',
  1486608779650:'brunner-bicarbonate',
  1486608782562:'jejunum-plicae',
  1486608789738:'ileum-peyer',
  1486608796832:'ileum-goblet',
  1486608805821:'colon-no-villi',
  1486608813182:'colon-goblet',
  1486831445995:'peyer-location',
  1486831448616:'m-cell-sampling',
  1486831451445:'peyer-iga',
  1482115445612:'enterocyte-sglt1',
  1482115575316:'villus-lacteal',
  1474164981030:'brush-border-lactase',
  1668632250119:'duodenum-image',
  1668632387853:'ileum-image',
  1668633014837:'small-intestine-image',
  1668633106589:'colon-image',
}
AUTHORED=[
 ('plica-layers','A plica circularis contains {{c1::mucosa and submucosa}}, whereas a villus contains {{c1::mucosa only}}.','Plica circular: prega maior, com submucosa. Vilo: projeção apenas da mucosa.','surface-levels'),
 ('crypt-villus-direction','Intestinal epithelial cells are generated in the {{c1::crypt}} and generally migrate toward the {{c1::villus tip}}.','A exceção importante é a célula de Paneth, que permanece junto à base da cripta.','epithelial-renewal'),
 ('cbc-markers','Active crypt-base columnar intestinal stem cells are marked by {{c1::Lgr5, Ascl2, and Olfm4}}.','Marcadores agrupados conforme o esquema docente; não decorar cada um em card separado.','cbc-markers'),
 ('reserve-markers','The intestinal crypt +4 reserve stem-cell population is associated with {{c1::Bmi1, Hopx, and Tert}}.','A posição +4 aparece no esquema do nicho.','reserve-markers'),
 ('ta-cells','Transit-amplifying cells are {{c1::proliferating progenitors}} between intestinal stem cells and differentiated epithelial cells.','TA = amplificação transitória na cripta.','transit-amplifying'),
 ('crypt-gradient','Along the intestinal crypt–villus axis, {{c1::Wnt}} is highest near the crypt base and {{c1::BMP}} increases toward the villus.','O esquema associa Wnt basal à manutenção/proliferação e BMP apical à diferenciação.','crypt-signaling'),
 ('lineage-fates','Intestinal stem cells give rise to an absorptive {{c1::enterocyte}} lineage and secretory {{c2::goblet, enteroendocrine, and Paneth}} lineages.','Linhagens do esquema docente; o mecanismo de Notch fica como aprofundamento.','epithelial-lineages'),
 ('goblet-muc2','Intestinal goblet cells secrete {{c1::MUC2 mucin}}.','Mucina 2 contribui para a barreira de muco.','goblet-function'),
 ('enterocyte-brush-border','The enterocyte brush border contains {{c1::lactase and sucrase}} and uses {{c2::villin}} as a microvillar structural protein.','Lactase e sacarase são enzimas; vilina participa da estrutura das microvilosidades.','enterocyte-brush-border'),
 ('enteroendocrine-hormones','Intestinal enteroendocrine cells secrete {{c1::hormones}} that regulate digestion, metabolism, and appetite.','Função no nível pedido pelo slide; sem lista de subtipos hormonais.','enteroendocrine-function'),
 ('paneth-niche','Besides antimicrobial products, Paneth cells support {{c1::Lgr5+ intestinal stem cells}} at the crypt base.','O card AnKing existente cobre defensinas e lisozima; este cobre o papel adicional explícito no slide.','paneth-niche'),
 ('ki67-location','Ki67-positive proliferating intestinal epithelial cells are concentrated in the {{c1::crypts}}.','Ki67 marca células em ciclo; p. 13.','proliferation-apoptosis'),
 ('tunel-location','TUNEL-positive apoptotic cells are concentrated near intestinal {{c1::villus tips}}.','TUNEL detecta fragmentação de DNA associada à apoptose; p. 13.','proliferation-apoptosis'),
 ('colon-dcs','In the normal colon, deep crypt secretory (DCS) cells support the {{c1::stem-cell niche}}.','O esquema da p. 32 mostra DCS no nicho; não exige memorizar todos os fatores secretados.','colon-niche'),
 ('colon-ilc2','ILC2-derived {{c1::IL-13}} participates in regulation of the colonic crypt secretory niche.','Ponte curta com o esquema da p. 32.','colon-niche'),
]

def digest(value): return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def clozes(value): return sorted({int(x) for x in re.findall(r'{{c(\d+)::',value)})

def main():
    notes={n['noteId']:n for n in call('notesInfo',notes=list(SOURCES))}
    if set(notes)!=set(SOURCES): raise RuntimeError('Fonte ausente')
    entries=[]; collisions={}
    for nid,obj in SOURCES.items():
        n=notes[nid]; f={k:v['value'] for k,v in n['fields'].items()}
        found=call('findNotes',query=f'tag:"NEBLI::source::nid-{nid}"')
        if found: collisions[nid]=found
        origin='AnKing' if n['modelName'].startswith('AnKingOverhaul (AnKing') else 'LLU Histology'
        if origin=='LLU Histology':
            for field in f:
                if field not in ('Text','Extra'):
                    f[field]=''
        entries.append({'key':f'source-{nid}','source_nid':nid,'source_model':n['modelName'],'source_tags':n['tags'],'source_fields_hash':digest(n['fields']),'fields':f,'objective':obj,'origin':origin,'expected_cards':len(clozes(f['Text'])),'high_yield':HY in n['tags'],'existing_copy':found})
    for key,text,extra,obj in AUTHORED:
        entries.append({'key':'authored-'+key,'source_nid':None,'source_model':None,'source_tags':[],'source_fields_hash':None,'fields':{'Text':text,'Extra':extra},'objective':obj,'origin':'Autoral','expected_cards':len(clozes(text)),'high_yield':False})
    plan={'lesson_id':LESSON,'target_deck':DECK,'profile_evidence':call('getMediaDirPath'),'source_folder':'https://drive.google.com/drive/folders/1GSN_lBnaYQh4d1zdMUjQfYnWeXVFs5vd','source_files':['https://drive.google.com/file/d/1RSAOynVb4CfC1FqItxkU7KvxCl-DRc1r/view','https://drive.google.com/file/d/1ZpaD30u9bT7-4ZGFYBsvC3J5C7f3yD-B/view'],'entries':entries,'collisions':collisions,'totals':{'notes':len(entries),'cards':sum(x['expected_cards'] for x in entries),'AnKing':sum(x['expected_cards'] for x in entries if x['origin']=='AnKing'),'LLU_Histology':sum(x['expected_cards'] for x in entries if x['origin']=='LLU Histology'),'Autoral':sum(x['expected_cards'] for x in entries if x['origin']=='Autoral'),'HY_green':sum(x['expected_cards'] for x in entries if x['high_yield'])}}
    (ROOT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'totals':plan['totals'],'collisions':collisions},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
