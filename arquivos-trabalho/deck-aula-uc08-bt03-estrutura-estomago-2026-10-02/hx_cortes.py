# Recortes das notas do Histology da BT03 (F-20261003-CLAUDE-14, 03/10/2026): uma frase, um fato, cloze de palavra inteira.
# Só os alvos que a v2 já marcava; cor herdada do cloze original. Texto do Histology/Junqueira cap. 15–16, recortado.
V, Z, R = 3, 4, 5
CORTES = {
 "papilas-tipos": [
  ("filiformes", "The most numerous lingual papillae, conical and heavily keratinized, are the {{c1::filiform}} papillae", {1: Z}, "Papilas filiformes"),
  ("fungiformes", "Mushroom-shaped, lightly keratinized papillae scattered among the filiform ones are the {{c1::fungiform}} papillae", {1: Z}, "Papilas fungiformes"),
  ("valadas", "The largest lingual papillae, lined up just in front of the sulcus terminalis, are the {{c1::vallate}} papillae", {1: Z}, "Papilas valadas"),
  ("folhadas", "Parallel ridges on the sides of the tongue, rudimentary in adults, are the {{c1::foliate}} papillae", {1: Z}, "Papilas folhadas"),
  ("von-ebner", "Serous {{c1::von Ebner}} glands empty into the groove around each vallate papilla", {1: R}, "Glândulas de von Ebner"),
  ("superficie-aspera", "Filiform papillae give the tongue a {{c1::rough}} surface that helps move food during chewing", {1: R}, "Função das filiformes"),
 ],
 "botoes-papilas": [
  ("papilas", "Taste buds lie within the epithelium of the lingual {{c1::papillae}} on the dorsal and lateral tongue", {1: Z}, "Botões gustativos nas papilas"),
  ("sem-filiforme", "The only lingual papillae without taste buds are the keratinized {{c1::filiform}} papillae", {1: R}, "Filiformes sem botões"),
  ("valadas", "Each {{c1::vallate}} papilla carries about 250 taste buds on its lateral walls", {1: R}, "Valadas concentram botões"),
 ],
 "epitelio-oral": [
  ("tipo", "The oral cavity is lined by {{c1::stratified squamous}} epithelium, keratinized or not depending on the site", {1: Z}, "Epitélio da boca", "1702140950842#0"),
 ],
 "mucosa-oral-tipos": [
  ("mastigatoria", "The gingiva and hard palate have {{c1::masticatory}} mucosa, whose keratinized epithelium resists abrasion", {1: Z}, "Mucosa mastigatória"),
  ("revestimento", "The cheeks, soft palate and floor of the mouth have {{c1::lining}} mucosa, with nonkeratinized epithelium", {1: Z}, "Mucosa de revestimento"),
 ],
 "lingua-musculo": [
  ("composicao", "The tongue is a mass of {{c1::striated muscle}} covered by mucosa", {1: Z}, "Língua: músculo estriado"),
 ],
 "lingua-superficies": [
  ("ventral", "The ventral surface of the tongue is smooth and covered by {{c1::lining}} mucosa", {1: Z}, "Face ventral da língua"),
  ("sulco", "The V-shaped {{c1::sulcus terminalis}} separates the papillary anterior two-thirds of the tongue from its posterior third", {1: R}, "Sulco terminal"),
 ],
 "dente-composicao": [
  ("esmalte", "The crown of a tooth is covered by {{c1::enamel}}, a hard acellular material", {1: Z}, "Esmalte"),
  ("cemento", "The roots of a tooth are covered by {{c1::cementum}}, a bone-like tissue", {1: Z}, "Cemento"),
  ("dentina", "The calcified material that makes up most of a tooth is {{c1::dentin}}", {1: Z}, "Dentina"),
  ("forame-apical", "Vessels and nerves reach the dental pulp through the {{c1::apical foramen}} at the root tip", {1: R}, "Polpa e forame apical"),
 ],
 "odontoblastos": [
  ("dentina", "Dentin is secreted as predentin by {{c1::odontoblasts}}, neural crest cells lining the pulp cavity", {1: R}, "Odontoblastos"),
 ],
 "ameloblastos": [
  ("esmalte", "The enamel matrix is secreted by {{c1::ameloblasts}} of the enamel organ", {1: R}, "Ameloblastos"),
 ],
 "ligamento-periodontal": [
  ("ancora", "The periodontal ligament anchors the {{c1::cementum}} to the alveolar bone", {1: R}, "Ligamento periodontal"),
 ],
 "parotida": [
  ("serosa", "The parotid gland has exclusively {{c1::serous}} acini", {1: V}, "Parótida serosa"),  # verde: calibração Ninja Nerd (salivação), F-14
  ("amilase", "Parotid saliva is rich in {{c1::α-amylase}}, which starts starch digestion", {1: R}, "Amilase da parótida"),
 ],
 "submandibular": [
  ("dois-tercos", "About two-thirds of all saliva comes from the {{c1::submandibular}} glands", {1: Z}, "Submandibular produz a maior parte", "1702294558765#0"),
  ("semiluas", "In mixed salivary units, serous cells capping mucous tubules form {{c1::serous demilunes}}", {1: R}, "Semiluas serosas", "1702294558765#0"),
 ],
 "sublingual": [
  ("menor", "The smallest major salivary gland is the {{c1::sublingual}} gland", {1: Z}, "Sublingual, a menor", "1702294558765#0"),
  ("mucosa", "The sublingual gland is made mostly of {{c1::mucous}} tubules", {1: Z}, "Sublingual mucosa", "1702294558765#0"),
 ],
 "celula-serosa": [
  ("aspecto", "Pyramidal protein-secreting salivary cells with round nuclei and apical granules are {{c1::serous}} cells", {1: Z}, "Célula serosa"),
  ("acino", "Serous cells are grouped into a rounded {{c1::acinus}} with a small central lumen", {1: R}, "Ácino seroso"),
 ],
 "celula-mucosa-salivar": [
  ("aspecto", "Salivary cells with flattened basal nuclei and pale-staining cytoplasm are {{c1::mucous}} cells", {1: Z}, "Célula mucosa"),
  ("mucinas", "Mucous cells stain poorly in H&E because their granules hold hydrophilic {{c1::mucins}}", {1: R}, "Mucinas coram pouco"),
 ],
 "mioepitelial": [
  ("funcao", "Flattened contractile cells inside the basal lamina of acini that squeeze secretion into the ducts are {{c1::myoepithelial}} cells", {1: R}, "Células mioepiteliais"),
 ],
 "lamina-propria": [
  ("tecido", "The lamina propria is {{c1::loose}} connective tissue rich in vessels, lymphatics and lymphocytes", {1: Z}, "Lâmina própria"),
 ],
 "muscular-mucosa": [
  ("limite", "The thin smooth muscle layer that separates the mucosa from the submucosa is the {{c1::muscularis mucosae}}", {1: Z}, "Muscular da mucosa"),
 ],
 "submucosa-conteudo": [
  ("denso", "The submucosa is {{c1::denser}} connective tissue that carries the larger blood and lymph vessels", {1: Z}, "Submucosa: conjuntivo denso"),
  ("meissner", "The autonomic nerve network inside the submucosa is the {{c1::submucosal (Meissner)}} plexus", {1: Z}, "Plexo de Meissner"),
 ],
 "serosa-mesotelio": [
  ("mesotelio", "The serosa is covered by a simple squamous epithelium called {{c1::mesothelium}}", {1: Z}, "Serosa com mesotélio"),
 ],
 "malt": [
  ("definicao", "Free immune cells and lymphoid nodules in the gut mucosa and submucosa form the {{c1::MALT}}", {1: R}, "MALT"),
 ],
 "esofago-glandulas": [
  ("submucosa", "The esophageal glands, which secrete lubricating mucus, lie in the {{c1::submucosa}}", {1: Z}, "Glândulas esofágicas na submucosa"),
  ("cardicas", "Near the stomach, esophageal {{c1::cardiac}} glands in the lamina propria add mucus", {1: R}, "Glândulas cárdicas do esôfago"),
 ],
 "esfincter-pilorico": [
  ("obliqua", "Besides its circular and longitudinal layers, the gastric muscularis has an innermost {{c1::oblique}} layer", {1: Z}, "Três camadas musculares do estômago"),
  ("camada", "The pyloric sphincter is a thickening of the {{c1::middle circular}} layer of the gastric muscularis", {1: Z}, "Esfíncter pilórico"),
 ],
 "rugas": [
  ("pregas", "Longitudinal folds of gastric mucosa and submucosa that flatten when the stomach fills are the {{c1::rugae}}", {1: Z}, "Rugas gástricas"),
 ],
 "juncao-esofagogastrica": [
  ("epitelio", "At the esophagogastric junction, stratified squamous epithelium changes abruptly to {{c1::simple columnar}} epithelium", {1: V}, "Transição esôfago–estômago"),
  ("fossetas", "The gastric surface epithelium dips into the lamina propria to form the {{c1::gastric pits}}", {1: Z}, "Fossetas gástricas"),
 ],
 "cardia-piloro-glandulas": [
  ("fossetas", "Cardiac and pyloric mucosa have {{c1::long}} pits leading into coiled glands", {1: V}, "Cárdia e piloro: fossetas longas", "1702214216607#0"),
  ("muco", "Cardiac and pyloric glands secrete mainly {{c1::mucus}}", {1: Z}, "Glândulas cárdicas e pilóricas mucosas", "1702214216607#0"),
  ("sem-parietal", "Cardiac and pyloric glands lack {{c1::parietal}} and {{c2::chief}} cells", {1: Z, 2: Z}, "Sem parietais nem principais", "1702214216607#0"),
 ],
 "fundo-corpo-iguais": [
  ("regioes", "The two gastric regions with identical histology, their mucosa filled by branched gastric glands, are the {{c1::fundus and body}}", {1: V}, "Fundo e corpo iguais"),
 ],
 "mucosas-superficiais": [
  ("celulas", "The gastric lumen and pits are lined by surface {{c1::mucous}} cells", {1: V}, "Células mucosas superficiais"),
  ("camada", "Surface mucous cells coat the gastric mucosa with a thick, bicarbonate-rich {{c1::mucus layer}}", {1: Z}, "Camada de muco"),
 ],
 "celulas-tronco-istmo": [
  ("istmo", "Gastric stem cells sit in the {{c1::isthmus}}, between the pit and the gland", {1: Z}, "Células-tronco no istmo"),
  ("renovacao", "Progenitor cells that move upward replace the surface mucous cells every {{c1::4–7}} days", {1: R}, "Renovação da superfície"),
 ],
 "progenitoras-glandula": [
  ("descem", "Progenitor cells that migrate down into the gland become {{c1::secretory}} cells, renewed more slowly than surface cells", {1: R}, "Progenitoras viram secretoras", "1702215136161#0"),
 ],
 "parietal-estrutura": [
  ("posicao", "Parietal cells lie among {{c1::mucous neck}} cells and in the deeper part of the gland", {1: Z}, "Posição da parietal"),
  ("eosinofilia", "Parietal cell cytoplasm is intensely eosinophilic because it is packed with {{c1::mitochondria}}", {1: Z}, "Parietal eosinófila"),
  ("canaliculo", "The apical membrane of the parietal cell folds inward to form an intracellular {{c1::canaliculus}} lined with microvilli", {1: Z}, "Canalículo intracelular", 1),
 ],
 "mucosas-colo": [
  ("celula", "Irregular mucus-secreting cells clustered in the necks of gastric glands are the {{c1::mucous neck}} cells", {1: Z}, "Células mucosas do colo"),
  ("nucleo", "Unlike surface mucous cells, mucous neck cells have {{c1::round}} nuclei", {1: R}, "Núcleo da mucosa do colo"),
 ],
 "principal-rer": [
  ("rer", "Chief cells secrete protein, so their basal cytoplasm is packed with {{c1::rough ER}}", {1: Z}, "Principal rica em RER"),
 ],
 "enteroendocrinas-estomago": [
  ("definicao", "Scattered gastric cells with endocrine or paracrine function are the {{c1::enteroendocrine}} cells", {1: Z}, "Enteroendócrinas gástricas"),
  ("celula-g", "Gastrin is made by {{c1::G}} cells of the pyloric glands", {1: Z}, "Células G no piloro"),
  ("serotonina", "In the fundus, enteroendocrine cells mainly secrete {{c1::serotonin}}", {1: R}, "Serotonina no fundo"),
 ],
}
