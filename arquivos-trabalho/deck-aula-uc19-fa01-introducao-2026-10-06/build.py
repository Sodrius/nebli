"""Constroi o plano UC19/P1 a partir de cards AnKing e complementos autorais curtos."""
import hashlib, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki

HERE = Path(__file__).parent
A = Anki()
RUN_ID = "2026-uc19-p1-fa01-introducao"
LESSON = "UC19::P1::FA01"
SHORT = "uc19p1fa01"
DECK = "NEBLI::UC19::P1::Farmacologia::Introdução à farmacologia e mecanismos de ação"
MODEL = "NEBLI AnKing independente - v3"
CLOZE = re.compile(r"\{\{c(\d+)::")

# Fonte AnKing primeiro: os cards abaixo foram revisados pela relação explícita com a lâmina.
SOURCES = [
 ("varenicline_partial",1475115425348,"Slide 49","agonista parcial: exemplo clínico"),
 ("flumazenil_comp",1484768629105,"Slide 54","antagonismo competitivo: exemplo clínico"),
 ("comp_right",1490066300391,"Slide 54","antagonista competitivo desloca curva"),
 ("comp_emax",1490066305390,"Slide 54","antagonista competitivo preserva Emax"),
 ("theophylline_ti",1474580915632,"Slide 60","índice terapêutico estreito"),
 ("ti_formula",1490066320396,"Slide 60","TD50/ED50"),
 ("allosteric_rev",1472426609949,"Slide 38","ligação reversível ao sítio do substrato"),
 ("allosteric_irrev",1472426614133,"Slide 54","inibição irreversível"),
 ("noncompetitive",1472426616871,"Slide 54","inibição não competitiva"),
 ("bupe_partial",1484950383414,"Slide 49","buprenorfina como agonista parcial"),
 ("bupe_mu",1484950408050,"Slide 49","agonismo parcial mu"),
 ("clavulanate",1489344367311,"Slide 19","clavulanato bloqueia beta-lactamase"),
 ("clav_suicide",1503672347649,"Slide 19","inibidor suicida: aplicação"),
 ("sulbactam",1503672403149,"Slide 19","inibição irreversível: aplicação"),
 ("mannitol_ecf",1474746837185,"Slide 32","manitol e compartimento extracelular"),
 ("mannitol_membrane",1474746866845,"Slide 32","manitol não cruza membrana"),
 ("hyperk_binder",1532613551528,"Slide 34","quelantes de potássio: aplicação"),
 ("oligomycin",1474253567960,"Slide 31","ATP sintase como alvo enzimático"),
 ("etc_gradient",1474253601690,"Slide 31","consequência de bloquear cadeia respiratória"),
 ("atp_synthase",1474253610434,"Slide 31","consequência de inibir ATP sintase"),
 ("nuclear_zinc",1467833758513,"Slide 26","receptores nucleares e zinc finger"),
 ("cisplatin_nephro",1475353590850,"Slide 27","cisplatina: toxicidade renal"),
 ("anthracycline",1472078824458,"Slide 28","doxorrubicina: cardiotoxicidade"),
 ("affinity_receptors",1461852748718,"Slide 39","número/afinidade de receptores mudam responsividade"),
 ("h1_window",1522298083351,"Slide 60","janela terapêutica pode estreitar"),
 ("pde5_cgmp",1463081026525,"Slide 30","PDE5 e degradação de cGMP"),
 ("pde5_nitrate",1472747945251,"Slide 30","interação nitrato–PDE5"),
 ("pde5_class",1499356681385,"Slide 30","inibidores de PDE5"),
 ("nitrate_preload",1472147101610,"Slide 30","vasodilatação venosa por nitrato"),
 ("nitrate_firstpass",1472747814325,"Slide 30","via sublingual de nitrato"),
 ("nitrate_class",1472747829983,"Slide 30","classe dos nitratos"),
 ("digoxin_na",1471224713065,"Slide 67","Na+/K+ ATPase: consequência de inibição"),
 ("digoxin_ncx",1471224723342,"Slide 67","Na+/Ca2+ exchanger: consequência"),
 ("digoxin_ca",1471224741979,"Slide 67","Ca2+ intracelular e efeito"),
 ("bile_resin",1472672275670,"Slide 34","resina sequestrante como alvo químico"),
 ("bile_binding",1472673094113,"Slide 34","ligação química no lúmen intestinal"),
 ("h1_gq",1474571586703,"Slide 25","GPCR H1 acoplado a Gq"),
 ("h2_gs",1474571591865,"Slide 25","GPCR H2 acoplado a Gs"),
 ("pde_camp",1461857288204,"Slide 30","fosfodiesterase degrada cAMP"),
]

AUTORAL = [
 ("pk_pd", "Pharmacokinetics describes what the body does to a drug; pharmacodynamics describes what the {{c1::drug}} does to the body.", "Slide 21 · Rang & Dale ch. 2", [1475115425348,1461852748718]),
 ("targets", "The principal drug targets are {{c1::receptors, enzymes, ion channels, and transporters}}.", "Slide 25 · objetivos cognitivos UC19", [1467833758513,1474253567960]),
 ("potency_efficacy", "On a graded dose-response curve, a leftward shift indicates greater {{c1::potency}}, whereas a higher plateau indicates greater {{c2::efficacy}}.", "Slides 39–40 · Rang & Dale ch. 2", [1490066300391,1490066305390]),
 ("inverse", "A neutral antagonist has {{c1::zero}} efficacy; an inverse agonist reduces {{c2::constitutive (basal)}} receptor activity.", "Slides 41–46 · objetivos cognitivos UC19", [1484768629105,1475115425348]),
 ("no_pde5", "Nitrates increase {{c1::cGMP}}; combining them with a PDE5 inhibitor can cause dangerous {{c2::hypotension}}.", "Slide 30 · Rang & Dale ch. 2", [1490066300391,1474580915632]),
 ("local_anesthetic", "Local anesthetics reduce action-potential propagation by blocking voltage-gated {{c1::Na+}} channels.", "Slide 69 · objetivos cognitivos UC19", [1474746866845,1474253567960]),
]

def digest(v):
 return hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]

def main():
 info={x['noteId']:x for x in A('notesInfo',notes=[x[1] for x in SOURCES])}
 entries=[]
 for order,(key,nid,evid,alvo) in enumerate(SOURCES,1):
  n=info[nid]; text=n['fields']['Text']['value']; extra=n['fields'].get('Extra',{}).get('value','')
  nums=sorted({int(x) for x in CLOZE.findall(text)})
  fields={'Text':text,'Extra':extra,'NEBLI_Comentario':''}
  tags=sorted(set(n['tags']+[f'NEBLI::{LESSON}','NEBLI::escopo::aula',f'NEBLI::objetivo::farmacodinamica',f'NEBLI::ordem::{SHORT}-{order:02d}',f'NEBLI::run::{RUN_ID}',f'NEBLI::source::nid-{nid}','NEBLI::origem::AnKing',f'NEBLI::cor::{LESSON}::verde']))
  entries.append({'key':key,'kind':'text','src':nid,'origin':'AnKing','model':MODEL,'evid':evid,'alvo':alvo,'bloco':'farmacodinamica','order':order,'tags':tags,'fields':fields,'fields_hash':digest(fields),'cards':[{'n':x,'ord':x-1,'flag':3,'cor':'verde'} for x in nums],'source_fields_hash':digest({'Text':text,'Extra':extra})})
 for key,text,extra,mirrors in AUTORAL:
  order=len(entries)+1; nums=sorted({int(x) for x in CLOZE.findall(text)}); fields={'Text':text,'Extra':extra,'NEBLI_Comentario':''}
  tags=[f'NEBLI::{LESSON}','NEBLI::escopo::aula','NEBLI::objetivo::farmacodinamica',f'NEBLI::ordem::{SHORT}-{order:02d}',f'NEBLI::run::{RUN_ID}',f'NEBLI::author::{SHORT}-{key}','NEBLI::origem::Autoral',f'NEBLI::cor::{LESSON}::verde']
  entries.append({'key':key,'kind':'autoral','origin':'Autoral','model':MODEL,'evid':extra.split(' · ')[0],'alvo':key,'bloco':'farmacodinamica','espelhos':mirrors,'order':order,'tags':tags,'fields':fields,'fields_hash':digest(fields),'cards':[{'n':x,'ord':x-1,'flag':3,'cor':'verde'} for x in nums]})
 cards=sum(len(e['cards']) for e in entries)
 plan={'run_id':RUN_ID,'short':SHORT,'lesson_id':LESSON,'deck':DECK,'criterios':'Cobertura dos slides; história excluída por solicitação do estudante; clínica apenas quando dedutível do mecanismo.','E1':'não incluída por solicitação explícita','entries':entries,'compartilhados':{},'excluidos':[],'fora_do_recorte':['história das lâminas 4–8 e 10–15: sem autorais, conforme pedido'], 'media':{},'clones':{},'totais':{'notas':len(entries),'cards':cards,'verdes':cards,'azuis':0,'rosas':0,'origens_notas':{'AnKing':len(SOURCES),'Autoral':len(AUTORAL)},'origens_cards':{'AnKing':cards-sum(len(sorted({int(x) for x in CLOZE.findall(t)})) for _,t,_,_ in AUTORAL),'Autoral':sum(len(sorted({int(x) for x in CLOZE.findall(t)})) for _,t,_,_ in AUTORAL)},'compartilhados_associados':0,'creditos_removidos':0}}
 plan['selection_hash']=digest([(e['key'],e['fields_hash'],e['cards']) for e in entries])
 (HERE/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
 print(json.dumps(plan['totais'],ensure_ascii=False)); print('authorial',len(AUTORAL),'of',len(entries),'notes')
if __name__=='__main__': main()
