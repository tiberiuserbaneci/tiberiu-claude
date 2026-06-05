#!/usr/bin/env python3
"""Autonomous portal server. Serves the dashboard and writes every change
(posted status, analytics upload, cross-post) straight to manifest.json and
auto-commits, so the operator never has to commit by hand.

Run:  python3 portal/server.py    then open http://127.0.0.1:8753
"""
import json, os, re, pathlib, threading, subprocess, datetime, urllib.parse, mimetypes, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PORTAL = CONTENT / "portal"
MANIFEST = PORTAL / "manifest.json"
ANALYTICS = CONTENT / "analytics"
ANALYTICS.mkdir(exist_ok=True)
PORT = int(os.environ.get("PORTAL_PORT", "8753"))
HOST = os.environ.get("PORTAL_HOST", "127.0.0.1")
BRANCH = os.environ.get("PORTAL_BRANCH", "claude/epic-davinci-eGOGS")
AUTOPUSH = os.environ.get("PORTAL_PUSH", "1") != "0"
_lock = threading.Lock()

def load(): return json.loads(MANIFEST.read_text())
def save(m): MANIFEST.write_text(json.dumps(m, indent=2))

def git(args):
    try: return subprocess.run(["git"]+args, cwd=ROOT, capture_output=True, text=True, timeout=40)
    except Exception as e: print("git error", e); return None

def autocommit(paths, msg):
    def _run():
        with _lock:
            git(["add"]+[str(p) for p in paths])
            r = git(["commit","-m",msg])
            if r and r.returncode==0:
                print("committed:", msg)
                if AUTOPUSH:
                    for delay in (0,2,4,8):
                        if delay: time.sleep(delay)
                        git(["pull","--no-rebase","--no-edit","origin",BRANCH])  # absorb my new-material commits (different files)
                        p = git(["push","-u","origin",BRANCH])
                        if p and p.returncode==0: print("pushed"); break
    threading.Thread(target=_run, daemon=True).start()

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, code, body=b"", ctype="application/json"):
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body))); self.end_headers()
        if body: self.wfile.write(body)
    def _json(self, obj, code=200): self._send(code, json.dumps(obj).encode(), "application/json")

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path in ("/","/index.html"):
            f = PORTAL/"index.html"
            return self._send(200, f.read_bytes(), "text/html; charset=utf-8")
        if path == "/manifest.json":
            return self._send(200, MANIFEST.read_bytes(), "application/json")
        # serve any file under the repo (images, thumbs, zips, html, analytics)
        rel = path.lstrip("/")
        fp = (ROOT/rel).resolve()
        if str(fp).startswith(str(ROOT)) and fp.is_file():
            ctype = mimetypes.guess_type(str(fp))[0] or "application/octet-stream"
            return self._send(200, fp.read_bytes(), ctype)
        return self._send(404, b'{"error":"not found"}')

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n) if n else b""
        if path == "/api/save":
            data = json.loads(body or b"{}")
            mid = data.get("id"); patch = data.get("patch", {})
            with _lock:
                m = load(); hit=None
                for x in m["materials"]:
                    if x["id"]==mid: x.update(patch); hit=x
                if not hit: return self._json({"error":"id not found"}, 404)
                save(m)
            autocommit([MANIFEST], f"portal: update {mid} ({', '.join(patch)})")
            return self._json({"ok":True, "material":hit})
        if path == "/api/analytics":
            mid = qs.get("id",[""])[0]; fname = qs.get("filename",["analytics.csv"])[0]
            fname = re.sub(r"[^A-Za-z0-9._-]","_", fname)
            dest = ANALYTICS / f"{mid}__{fname}"
            dest.write_bytes(body)
            with _lock:
                m = load()
                for x in m["materials"]:
                    if x["id"]==mid:
                        x["analytics"] = "content/analytics/"+dest.name
                        x["analytics_uploaded"] = datetime.date.today().isoformat()
                save(m)
            autocommit([MANIFEST, dest], f"portal: analytics for {mid}")
            return self._json({"ok":True, "path":"content/analytics/"+dest.name})
        if path == "/api/rescan":
            git(["pull","--no-rebase","--no-edit","origin",BRANCH])  # pull newly-added materials, then reindex
            subprocess.run(["python3","portal/scan.py"], cwd=ROOT, timeout=600)
            autocommit([MANIFEST], "portal: sync + rescan")
            return self._json({"ok":True})
        return self._json({"error":"unknown endpoint"}, 404)

if __name__ == "__main__":
    where = f"http://127.0.0.1:{PORT}" if HOST in ("127.0.0.1","localhost") else f"port {PORT} (forwarded by Codespaces, Private)"
    print(f"Portal -> {where}   (auto-commit on, push={'on' if AUTOPUSH else 'off'}, branch={BRANCH})")
    ThreadingHTTPServer((HOST, PORT), H).serve_forever()
