import json,re,sys
from collections import defaultdict
from ak import call,strip
sys.stdout.reconfigure(encoding='utf-8')
P='#AK_Step1_v12::'
FA=P+'#FirstAid::'
TAGS={
 'islet':[FA+'08_Endocrine::02_Anatomy::03_Endocrine_pancreas_cell_types*'],
 'insulin':[FA+'08_Endocrine::03_Physiology::10_Insulin*',P+'#B&B::09_Endocrinology::03_Pancreas::01_Insulin*',FA+'08_Endocrine::03_Physiology::01_Hypothalamic-pituitary_hormones::*Somatostatin::Insulin'],
 'glucagon':[FA+'08_Endocrine::03_Physiology::09_Glucagon*',P+'#B&B::09_Endocrinology::03_Pancreas::02_Glucagon_&_Hypoglycemia*'],
 'signal':[FA+'08_Endocrine::03_Physiology::14_Signaling_pathways_of_endocrine_hormones::01_cAMP::*G-Protein_Signalling::Catalytic_Receptor_Mechanism::Tyrosine_Kinase_Mechanism'],
 'dm':[FA+'08_Endocrine::04_Pathology::15_Diabetes_mellitus*',FA+'08_Endocrine::04_Pathology::16_Type_1_vs_type_2_diabetes_mellitus*',FA+'08_Endocrine::04_Pathology::17_Hyperglycemic_emergencies*',P+'#B&B::09_Endocrinology::03_Pancreas::03_Type_I_Diabetes*',P+'#B&B::09_Endocrinology::03_Pancreas::04_Type_II_Diabetes*',P+'#Pathoma::15_Endocrine::09_Endocrine_Pancreas*'],
 'pharm':[FA+'08_Endocrine::05_Pharm::01_Diabetes_mellitus_therapy::*SGLT2_Inhibitors',FA+'08_Endocrine::05_Pharm::01_Diabetes_mellitus_therapy::*Sulfonylureas',FA+'08_Endocrine::05_Pharm::01_Diabetes_mellitus_therapy::*Basics'],
 'incretin':[FA+'09_Gastrointestinal::03_Physiology::01_Gastrointestinal_regulatory_substances::*Glucagon-Like_Peptide',FA+'09_Gastrointestinal::03_Physiology::01_Gastrointestinal_regulatory_substances::*Glucose_Dependent_Insulinotropic_Peptide'],
 'hk':[FA+'01_Biochem::06_Metabolism::07_Hexokinase_vs_glucokinase*'],
 'sorbitol':[FA+'01_Biochem::06_Metabolism::20_Sorbitol*',P+'#Bootcamp::Biochemistry::05_Carbohydrates::06_Sorbitol_and_the_Polyol_Pathway'],
 'glycogen_reg':[FA+'01_Biochem::06_Metabolism::35_Glycogen_regulation_by_insulin_and_glucagon/epinephrine*'],
 'ketone':[FA+'01_Biochem::06_Metabolism::40_Ketone_bodies*',P+'#B&B::04_Biochem::02_Metabolism::11_Ketone_Bodies*',P+'#Bootcamp::Biochemistry::09_Lipid_Metabolism::16_Ketones:_Ketone_Synthesis',P+'#Bootcamp::Biochemistry::09_Lipid_Metabolism::17_Ketones:_Ketoacidosis_Review_and_Ketogenolysis'],
 'fuel':[FA+'01_Biochem::06_Metabolism::42_Metabolic_fuel_use*',P+'#Bootcamp::Biochemistry::09_Lipid_Metabolism::18_Fed_vs._Fasting_State'],
 'cortisol_gh':[FA+'08_Endocrine::03_Physiology::12_Cortisol::02_Function',FA+'08_Endocrine::03_Physiology::02_Growth_hormone::*Function'],
 'hla':[FA+'02_Immunology::02_Cellular_Components::04_HLA_subtypes_associated_with_diseases'],
 'amylin':[FA+'04_Pathology::01_Cellular_Injury::11_Amyloidosis::*Amylin_Diabetes'],
 'hyaline':[FA+'07_Cardiovascular::04_Pathology::09_Arteriolosclerosis::*Arteriosclerosis::Hyaline_Arteriosclerosis'],
 'acanthosis':[FA+'11_Musculoskeletal_Skin_and_Connective_Tissue::03_Derm::15_Miscellaneous_skin_disorders::01_Acanthosis_nigricans'],
 'retina':[FA+'12_Neurology_and_Special_Senses::05_Ophthalmology::07_Retinal_disorders::02_Diabetic_retinopathy'],
 'nephro':[FA+'14_Renal::04_Pathology::05_Nephrotic_syndrome::*Diabetes'],
 'kshift':[FA+'14_Renal::03_Physiology::18_Potassium_shifts*'],
 'acidosis':[FA+'14_Renal::03_Physiology::22_Acidosis_and_alkalosis::*Metabolic_Acidosis*'],
 'aki':[FA+'14_Renal::04_Pathology::11_Acute_kidney_injury::*Prerenal',FA+'14_Renal::04_Pathology::11_Acute_kidney_injury::*Basics'],
 'nak':[FA+'01_Biochem::02_Cellular::11_Sodium-potassium_pump'],
}
TEXT=['glucosuria','glycosuria','renal threshold','splay','glucose clearance','osmotic diuresis','hemoglobin A1c','HbA1c','glycated','nonenzymatic glycation','advanced glycation','Kussmaul','fruity','acetone','beta-hydroxybutyrate','β-hydroxybutyrate','acetoacetate','ketogenesis','ketonuria','C-peptide','proinsulin','GLUT-4','GLUT4','GLUT-2','GLUT2','GLUT-1','GLUT-3','insulin-independent','insulin independent','insulin receptor','IRS-1','PI3K','glucokinase','ATP-sensitive K','K ATP','KATP','insulitis','GAD','islet cell autoantibod','anti-insulin','HLA-DR3','HLA-DR4','HHS','hyperosmolar','diabetic ketoacidosis','DKA','pseudohyponatremia','Kimmelstiel','microalbuminuria','diabetic nephropathy','diabetic retinopathy','diabetic neuropathy','aldose reductase','sorbitol','hyperkalemia insulin','total body potassium','prerenal','BUN:Cr','BUN/Cr','hormone-sensitive lipase','lipolysis insulin','counterregulatory','somatostatin','incretin','acanthosis nigricans','insulin resistance','mucormycosis','diabetes mellitus','hyperglycemia']
def main():
    hits=defaultdict(set)
    for g,ts in TAGS.items():
        for t in ts:
            for nid in call('findNotes',query=f'"tag:{t}" "deck:AnKing Step Deck"'): hits[nid].add('T:'+g)
    counts={}
    for t in TEXT:
        ids=call('findNotes',query=f'"deck:AnKing Step Deck" "{t}"'); counts[t]=len(ids)
        if len(ids)>250: continue
        for nid in ids: hits[nid].add('Q:'+t)
    ids=sorted(hits); rows=[]
    for s in range(0,len(ids),250):
        for n in call('notesInfo',notes=ids[s:s+250]):
            f={k:v['value'] for k,v in n['fields'].items()}
            rows.append({'nid':n['noteId'],'model':n['modelName'],'tags':n['tags'],'fields':f,'cards':n['cards'],'hits':sorted(hits[n['noteId']])})
    json.dump({'counts':counts,'notes':rows},open('inventory.json','w',encoding='utf-8'),ensure_ascii=False)
    print(json.dumps(counts,ensure_ascii=False)); print(len(rows))
main()
