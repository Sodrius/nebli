"""Helper mínimo p/ AnkiConnect (localhost:8765). Uso: from anki import call."""
import json, urllib.request

def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request("http://localhost:8765", payload,
                                 {"Content-Type": "application/json"})
    for _ in range(4):
        try:
            r = json.load(urllib.request.urlopen(req, timeout=25))
            if r.get("error"):
                raise RuntimeError(f"AnkiConnect error [{action}]: {r['error']}")
            return r["result"]
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
    raise last

if __name__ == "__main__":
    import sys
    print(call("version"))
    m = "IO-one by one (AnKing Step Deck / AnKingMed)"
    print("cards for 5 notes:", len(call("findCards", query=f'note:"{m}"')))
    t = call("modelTemplates", modelName=m)
    for k, v in t.items():
        print("TEMPLATE:", k, "| front chars:", len(v["Front"]))
