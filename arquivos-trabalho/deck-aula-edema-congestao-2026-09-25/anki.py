import json, urllib.request, re, html
def call(a, **p):
    r = urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action":a,"version":6,"params":p}).encode()), timeout=300)
    d = json.load(r)
    if d["error"]: raise RuntimeError(f"{a}: {d['error']}")
    return d["result"]
def clean(s):
    s = re.sub(r"<br\s*/?>", " / ", s or ""); s = re.sub(r"<img[^>]*src=\"([^\"]+)\"[^>]*>", r"[IMG \1]", s)
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s); return re.sub(r"\s+", " ", s).strip()
