"""Dois alvos finais da auditoria fonte→cards; não escreve no Anki."""
import json
import fitz
from preparar_v2 import OUT, ROOT, metadata

def main():
    p=json.loads((OUT/'plan.json').read_text(encoding='utf-8'))
    entries=[
     {'key':'fontes-pg-lt','origin':'NEBLI-local','fields':{'Text':'In the lecture\'s vascular-mediator table, prostaglandins and leukotrienes are produced by {{c1::mast cells and other leukocytes}}.','Extra':'A tabela da p. 12 pede origem e efeito. Os efeitos vasculares e vias COX/LOX já têm perguntas AnKing próprias.'+metadata([12],'alta','durable','não classificado','NEBLI — complemento da aula','Fontes celulares de PG e LT')},'clozes':[1],'pages':[12],'objective':'fontes-pg-lt','local_priority':'alta','retention_group':'durable','step_yield':'não classificado','search_evidence':['candidatos-v2.json'],'reason':'A origem de PG/LT na tabela não estava efetivamente sendo perguntada; não contar menção no apoio como cobertura ativa.'},
     {'key':'v-fases-pulmao','origin':'NEBLI-visual','fields':{'Text':'Compared with normal lung (A), panel B shows {{c1::dilated, blood-filled septal capillaries (vascular congestion)}}; panel C additionally shows {{c2::a prominent leukocyte infiltrate in alveolar spaces}}.<br><img src="nebli-ia-v2-fig-06.png" style="max-width:100%">','Extra':'Comparação da própria aula: alterações vasculares predominam em B; recrutamento celular é evidente em C. As fases se sobrepõem. A imagem foi extraída da área ilustrada do PDF sem os títulos que entregavam a resposta.'+metadata([14,30],'alta','durable','não classificado','Imagem docente/Robbins reproduzida na aula, uso pessoal','Distinguir alterações vasculares e celulares na histologia')},'clozes':[1,2],'pages':[14,30],'objective':'v-fases-pulmao','local_priority':'alta','retention_group':'durable','step_yield':'não classificado','search_evidence':['busca-acervo.json','candidatos-v2.json'],'reason':'Figura comparativa inicialmente só no Extra; faltava testar a distinção visual efetivamente ensinada.'}
    ]
    pdf=fitz.open(ROOT/'slides.pdf')
    # Renderização de região do PDF, excluindo apenas a linha de legendas textuais.
    pdf[29].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(0,191,717,382),annots=False).save(str(OUT/'nebli-ia-v2-fig-06.png'))
    for e in entries:
        if not any(x['key']==e['key'] for x in p['entries']):p['entries'].append(e)
    p['media']=list(dict.fromkeys(p['media']+['nebli-ia-v2-fig-06.png']))
    (OUT/'plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
    print({'notes':len(p['entries']),'cards':sum(len(e['clozes']) for e in p['entries'])})

if __name__=='__main__':main()
