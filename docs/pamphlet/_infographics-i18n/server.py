#!/usr/bin/env python3
"""Box editor server — TRVALÉ místo (~/Downloads/personix-boxtool), přežije restart.
Fallback: když imgtexts/{name}.json chybí, seznam textů vlevo se dočte z uložených boxů.
"""
import os, json, glob
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
GFX = "/Users/pavelkudrna/RiderProjects/new-world-order/Prezentace/Info Graphics/v5"
TEXTS = os.path.join(ROOT, "imgtexts")
BOXES = os.path.join(ROOT, "imgboxes")
os.makedirs(BOXES, exist_ok=True); os.makedirs(TEXTS, exist_ok=True)

def texts_for(n):
    """Texty pro panel vlevo: primárně z imgtexts, fallback z uložených boxů."""
    tf = f"{TEXTS}/{n}.json"
    if os.path.exists(tf):
        try: return json.load(open(tf)).get("texts", [])
        except: pass
    bf = f"{BOXES}/{n}.json"
    if os.path.exists(bf):
        seen, out = set(), []
        for b in json.load(open(bf)):
            if b["text"] not in seen:
                seen.add(b["text"]); out.append({"role": b.get("role",""), "text": b["text"]})
        return out
    return []

def img_list():
    names = sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(f"{GFX}/*.webp"))
    out = []
    for n in names:
        bf = f"{BOXES}/{n}.json"
        nb = len(json.load(open(bf))) if os.path.exists(bf) else 0
        nt = len(texts_for(n))
        out.append({"name": n, "ntexts": nt, "nboxes": nb, "done": os.path.exists(bf)})
    return out

class H(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Access-Control-Allow-Origin", "*"); self.end_headers()
        if isinstance(body, str): body = body.encode()
        self.wfile.write(body)
    def log_message(self, *a): pass
    def do_GET(self):
        p = unquote(self.path.split("?")[0])
        if p in ("/", "/index.html"):
            return self._send(200, open(f"{ROOT}/index.html","rb").read(), "text/html; charset=utf-8")
        if p == "/api/list": return self._send(200, json.dumps(img_list()))
        if p.startswith("/api/img/"):
            fp = f"{GFX}/{p[len('/api/img/'):]}.webp"
            if not os.path.exists(fp): return self._send(404, "{}")
            return self._send(200, open(fp,"rb").read(), "image/webp")
        if p.startswith("/api/data/"):
            n = p[len("/api/data/"):]
            bf = f"{BOXES}/{n}.json"
            boxes = json.load(open(bf)) if os.path.exists(bf) else []
            try: w,h = Image.open(f"{GFX}/{n}.webp").size
            except: w,h = 2912,1440
            return self._send(200, json.dumps({"w":w,"h":h,"texts":texts_for(n),"boxes":boxes}))
        return self._send(404, "{}")
    def do_POST(self):
        p = unquote(self.path.split("?")[0])
        if p.startswith("/api/save/"):
            n = p[len("/api/save/"):]
            data = self.rfile.read(int(self.headers.get("Content-Length", 0)))
            try:
                boxes = json.loads(data)
                json.dump(boxes, open(f"{BOXES}/{n}.json","w"), ensure_ascii=False, indent=1)
                return self._send(200, json.dumps({"ok":True,"n":len(boxes)}))
            except Exception as e:
                return self._send(400, json.dumps({"error":str(e)}))
        return self._send(404, "{}")

if __name__ == "__main__":
    print("Box editor (trvalý) na http://127.0.0.1:8770")
    HTTPServer(("127.0.0.1", 8770), H).serve_forever()
