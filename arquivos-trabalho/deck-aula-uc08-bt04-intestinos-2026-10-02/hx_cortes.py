# Recortes das notas do Histology da BT04 (F-20261003-CLAUDE-14, 03/10/2026): uma frase, um fato, cloze de palavra inteira.
# Só os alvos que a v2 já marcava; cor herdada do cloze original. Texto do Histology/Junqueira cap. 15, recortado.
V, Z, R = 3, 4, 5
CORTES = {
 "delgado-mucosa": [
  ("pregas", "Permanent circular folds of mucosa and submucosa in the small intestine are the {{c1::plicae circulares}}", {1: Z}, "Pregas circulares", 1),
  ("jejuno", "Plicae circulares are best developed in the {{c1::jejunum}}", {1: Z}, "Pregas maiores no jejuno", 1),
  ("eixo", "The core of each intestinal villus is an extension of the {{c1::lamina propria}}", {1: Z}, "Eixo do vilo"),
  ("lacteo", "The blind-ended lymphatic in the center of each villus is the {{c1::lacteal}}", {1: Z}, "Lácteo"),
  ("capilares", "Capillaries in the villus core are {{c1::fenestrated}}, easing uptake of absorbed nutrients", {1: R}, "Capilares fenestrados do vilo"),
 ],
 "criptas-epitelio": [
  ("criptas", "Short tubular glands that open between the villi are the {{c1::crypts of Lieberkühn}}", {1: Z}, "Criptas", "1702228171156#0"),
 ],
 "enterocito": [
  ("forma", "Enterocytes are tall {{c1::columnar}} cells with oval basal nuclei", {1: Z}, "Forma do enterócito"),
  ("borda", "Dense microvilli on the apical surface of enterocytes form the {{c1::brush border}}", {1: V}, "Borda estriada"),
  ("glicocalice", "Enterocyte microvilli are covered by a {{c1::glycocalyx}} that holds digestive enzymes", {1: Z}, "Glicocálice"),
  ("ampliacao", "Microvilli enlarge the intestinal surface about {{c1::20}}-fold, villi 10-fold and plicae 3-fold", {1: Z}, "Ampliação da superfície", 1),
 ],
 "caliciforme": [
  ("celula", "Mucus-secreting cells scattered among the enterocytes are the {{c1::goblet}} cells", {1: Z}, "Caliciformes"),
  ("mucinas", "Goblet cells secrete glycoprotein {{c1::mucins}}, which hydrate into protective mucus", {1: Z}, "Mucinas"),
 ],
 "enteroendocrina-aberta": [
  ("quimiorreceptores", "Open-type enteroendocrine cells reach the lumen and carry {{c1::chemoreceptors}} that sense nutrients", {1: Z}, "Enteroendócrina aberta", 1),
 ],
 "enteroendocrina-efeitos": [
  ("efeitos", "Gut enteroendocrine hormones regulate motility, enzyme and electrolyte secretion, and {{c1::satiety}}", {1: Z}, "Efeitos dos hormônios intestinais", 2),
 ],
 "absorcao-carbo-prot": [
  ("enzimas", "Enterocytes keep {{c1::disaccharidases}} and peptidases in the glycocalyx, finishing digestion at the brush border", {1: Z}, "Dissacaridases e peptidases"),
 ],
 "absorcao-gordura": [
  ("micelas", "Bile salts package lipid digestion products into {{c1::micelles}}", {1: Z}, "Micelas"),
  ("reesterificacao", "Inside the enterocyte, absorbed lipids are rebuilt into triglycerides in the {{c1::smooth ER}}", {1: R}, "Reesterificação no REL"),
  ("quilomicron", "Enterocytes export triglycerides as {{c1::chylomicrons}}, which enter the lacteal", {1: Z}, "Quilomícrons"),
 ],
 "vilo-musculo": [
  ("origem", "Smooth muscle fibers in the villus core come from the {{c1::muscularis mucosae}}", {1: Z}, "Músculo do vilo"),
  ("bomba", "Rhythmic contraction of villus smooth muscle pumps lymph out of the {{c1::lacteals}}", {1: R}, "Vilo bombeia linfa"),
 ],
 "paneth-celula": [
  ("posicao", "Paneth cells sit at the {{c1::base}} of the intestinal crypts", {1: Z}, "Paneth na base da cripta"),
  ("granulos", "Paneth cells have large apical {{c1::eosinophilic}} secretory granules", {1: Z}, "Grânulos da Paneth"),
  ("funcao", "By secreting lysozyme and defensins, Paneth cells provide {{c1::innate}} immunity in the crypt", {1: Z}, "Função da Paneth"),
 ],
 "iga-transcitose": [
  ("iga", "The main antibody secreted into the gut lumen is {{c1::IgA}}", {1: Z}, "IgA secretora"),
  ("transcitose", "IgA crosses the epithelium by {{c1::transcytosis}}, bound to a secretory protein made by epithelial cells", {1: Z}, "Transcitose da IgA"),
 ],
 "grosso-mucosa": [
  ("sem-vilos", "Unlike the small intestine, the large-intestine mucosa has no {{c1::villi}}", {1: V}, "Grosso sem vilos", 2),
 ],
 "grosso-regioes": [
  ("funcao", "The large intestine absorbs water and electrolytes and turns {{c1::indigestible}} material into feces", {1: Z}, "Função do grosso"),
 ],
 "grosso-lamina-propria": [
  ("nodulos", "The large-intestine lamina propria is rich in lymphoid {{c1::nodules}}, often reaching the submucosa", {1: Z}, "Nódulos linfoides do grosso", 2),
  ("apendice", "The {{c1::appendix}} contributes little to absorption but is a major site of MALT", {1: R}, "Apêndice como MALT"),
 ],
 "grosso-glandulas": [
  ("celulas", "Large-intestine glands are lined mainly by {{c1::goblet}} cells and absorptive colonocytes", {1: Z}, "Células das glândulas do grosso", 2),
  ("reto", "Goblet cells of the large intestine become more numerous toward the {{c1::rectum}}", {1: Z}, "Caliciformes aumentam até o reto", 1),
  ("microvilos", "Colonocytes have short irregular {{c1::microvilli}}, reflecting fluid absorption", {1: R}, "Microvilos do colonócito", 2),
 ],
 "tenias": [
  ("faixas", "The outer longitudinal muscle of the colon is gathered into three bands called {{c1::teniae coli}}", {1: Z}, "Tênias do colo", 1),
 ],
}
