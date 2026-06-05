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
AUTOCOMMIT = os.environ.get("PORTAL_COMMIT", "1") != "0"   # PORTAL_COMMIT=0 -> write manifest but no git (testing)
_lock = threading.Lock()

def load(): return json.loads(MANIFEST.read_text())
def save(m): MANIFEST.write_text(json.dumps(m, indent=2))

def git(args):
    try: return subprocess.run(["git"]+args, cwd=ROOT, capture_output=True, text=True, timeout=40)
    except Exception as e: print("git error", e); return None

def autocommit(paths, msg):
    if not AUTOCOMMIT: return
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
        if path == "/api/crosspost":
            data = json.loads(body or b"{}")
            mid = data.get("id"); target = data.get("target")
            if target not in ("linkedin","tiktok","instagram"):
                return self._json({"error":"bad target"}, 400)
            with _lock:
                m = load()
                src = next((x for x in m["materials"] if x["id"]==mid), None)
                if not src: return self._json({"error":"id not found"}, 404)
                clone_id = f"{mid}--as-{target}"
                if any(x["id"]==clone_id for x in m["materials"]):
                    return self._json({"ok":True, "id":clone_id, "already":True})
                clone = dict(src)
                clone.update({"id":clone_id, "channel":target, "source":"crosspost", "origin":mid,
                              "posted":False, "posted_date":None, "analytics":None,
                              "analytics_uploaded":None, "crossposts":[], "status":"ready"})
                m["materials"].append(clone)
                xp = set(src.get("crossposts") or []); xp.add(target); src["crossposts"] = sorted(xp)
                save(m)
            autocommit([MANIFEST], f"portal: crosspost {mid} -> {target}")
            return self._json({"ok":True, "id":clone_id})
        if path == "/api/delete":
            data = json.loads(body or b"{}"); mid = data.get("id")
            with _lock:
                m = load(); m.setdefault("deleted", [])
                idx = next((i for i,x in enumerate(m["materials"]) if x["id"]==mid), None)
                if idx is None: return self._json({"error":"id not found"}, 404)
                mat = m["materials"].pop(idx)
                mat["deleted_date"] = datetime.date.today().isoformat()
                if mat.get("source")=="crosspost" and mat.get("origin"):  # untag the origin
                    for x in m["materials"]:
                        if x["id"]==mat["origin"]:
                            x["crossposts"] = [c for c in (x.get("crossposts") or []) if c!=mat.get("channel")]
                m["deleted"] = [d for d in m["deleted"] if d["id"]!=mid] + [mat]
                save(m)
            autocommit([MANIFEST], f"portal: delete {mid}")
            return self._json({"ok":True})
        if path == "/api/restore":
            data = json.loads(body or b"{}"); mid = data.get("id")
            with _lock:
                m = load(); m.setdefault("deleted", [])
                idx = next((i for i,d in enumerate(m["deleted"]) if d["id"]==mid), None)
                if idx is None: return self._json({"error":"id not found"}, 404)
                mat = m["deleted"].pop(idx); mat.pop("deleted_date", None)
                if mat.get("source")=="crosspost" and mat.get("origin"):  # re-tag the origin
                    for x in m["materials"]:
                        if x["id"]==mat["origin"]:
                            xp = set(x.get("crossposts") or []); xp.add(mat.get("channel")); x["crossposts"] = sorted(xp)
                m["materials"].append(mat)
                save(m)
            autocommit([MANIFEST], f"portal: restore {mid}")
            return self._json({"ok":True})
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
