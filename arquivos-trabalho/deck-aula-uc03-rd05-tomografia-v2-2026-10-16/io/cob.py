import json,re,sys,urllib.request
run=sys.argv[1]; AU=json.load(open(sys.argv[2]))
def call(a,**p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765",json.dumps({"action":a,"version":6,"params":p}).encode())))["result"]
p=json.load(open(f"{run}/plan.json"))
cl=lambda t: re.sub(r"<[^>]+>","",(re.findall(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", t) or [""])[0]).strip()
rows=["chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao"]
for e in p["entries"]:
    k=e["key"]
    if k in AU:
        c,f,l,d,dec=AU[k]; rows.append("\t".join([k,c,f,"parcial" if dec.startswith("Parcial") else "lacuna",l,d,dec])); continue
    rows.append("\t".join([k,e.get("alvo",""),e["evid"],"coberto",str(e.get("src","")),"","card de acervo achado por seção, palavra-chave ou significado"]))
for nid,v in p["compartilhados"].items():
    rows.append("\t".join([f"sh-{nid}",v["alvo"],v["evid"],"coberto",str(v.get("source_nid") or nid),"","card NEBLI vivo de outra aula associado (sh), histórico preservado"]))
open(f"{run}/busca/cobertura.tsv","w").write("\n".join(rows)+"\n"); print(len(rows)-1,"linhas")
